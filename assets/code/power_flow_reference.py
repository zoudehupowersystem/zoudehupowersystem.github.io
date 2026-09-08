#!/usr/bin/env python3
"""Reproducible companion to Dehu Zou's Ybus-to-power-flow article.

Scope: a balanced, positive-sequence, per-unit, fixed-network Newton kernel.
This is an executable teaching and verification artifact, not an industrial
solver. General controller coordination, automatic island handling, and a
multi-generator reactive-limit allocator are deliberately outside its scope.

Run: python power_flow_reference.py [--json results.json]
Dependencies: NumPy and SciPy. No network connection or external case is used.
"""
from __future__ import annotations

import argparse
import json
import platform
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import scipy
from numpy.typing import NDArray
from scipy.optimize import root
from scipy.sparse import bmat, coo_matrix, csr_matrix, diags
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import splu

ComplexArray = NDArray[np.complex128]
RealArray = NDArray[np.float64]


@dataclass(frozen=True)
class Branch:
    """Zero-based terminals; total charging b; tap at the from terminal."""
    f: int
    t: int
    r: float
    x: float
    b: float = 0.0
    tap: float = 1.0
    shift_deg: float = 0.0


@dataclass(frozen=True)
class Network:
    ybus: csr_matrix
    yf: csr_matrix
    yt: csr_matrix
    cf: csr_matrix
    ct: csr_matrix
    ysh: ComplexArray
    branches: tuple[Branch, ...]


def assemble(n: int, branches: tuple[Branch, ...],
             ysh: ComplexArray | None = None) -> Network:
    if n < 1:
        raise ValueError("The bus count must be positive.")
    ysh = np.zeros(n, dtype=complex) if ysh is None else np.asarray(ysh, complex)
    if ysh.shape != (n,) or not np.isfinite(ysh).all():
        raise ValueError("ysh must be a finite vector with one entry per bus.")
    for e in branches:
        if not (0 <= e.f < n and 0 <= e.t < n) or e.f == e.t:
            raise ValueError("Invalid branch terminals.")
        if not np.isfinite([e.r, e.x, e.b, e.tap, e.shift_deg]).all():
            raise ValueError("Non-finite branch data.")
        if abs(complex(e.r, e.x)) <= 1e-12 or e.tap <= 0:
            raise ValueError("Zero/near-zero impedance or non-positive tap.")
    rows = np.arange(len(branches))
    cf = coo_matrix((np.ones(len(branches)),
                     (rows, [e.f for e in branches])), shape=(len(branches), n)).tocsr()
    ct = coo_matrix((np.ones(len(branches)),
                     (rows, [e.t for e in branches])), shape=(len(branches), n)).tocsr()
    ys = np.array([1 / complex(e.r, e.x) for e in branches])
    bc = np.array([e.b for e in branches])
    tap = np.array([e.tap * np.exp(1j * np.deg2rad(e.shift_deg)) for e in branches])
    ytt = ys + 0.5j * bc
    yf = (diags(ytt / abs(tap)**2) @ cf - diags(ys / tap.conj()) @ ct).tocsr()
    yt = (-diags(ys / tap) @ cf + diags(ytt) @ ct).tocsr()
    ybus = (cf.T @ yf + ct.T @ yt + diags(ysh)).tocsr()
    return Network(ybus, yf, yt, cf, ct, ysh.copy(), branches)


@dataclass(frozen=True)
class Injections:
    """P/Q ZIP fractions may differ; each row must sum to one.

    Only entries selected by the active residual are specified constraints.
    REF P/Q and PV Q entries are ignored by the reduced solve.
    """
    generation: ComplexArray
    demand: ComplexArray
    p_zip: RealArray
    q_zip: RealArray

    def evaluate(self, m: RealArray) -> tuple[ComplexArray, ComplexArray]:
        pz, pi, pp = self.p_zip.T
        qz, qi, qp = self.q_zip.T
        load = (self.demand.real * (pz*m*m + pi*m + pp)
                + 1j*self.demand.imag * (qz*m*m + qi*m + qp))
        dload = (self.demand.real * (2*pz*m + pi)
                 + 1j*self.demand.imag * (2*qz*m + qi))
        return self.generation - load, -dload


def derivatives(ybus: csr_matrix, v: ComplexArray) -> tuple[csr_matrix, csr_matrix]:
    """Complex network-injection derivatives w.r.t. real angles/magnitudes."""
    m = abs(v)
    if not np.isfinite(v).all() or np.any(m <= 0):
        raise ValueError("Polar derivatives require finite, nonzero voltages.")
    current = ybus @ v
    u = v / m
    dv = diags(v)
    dtheta = 1j * dv @ (diags(current.conj()) - ybus.conj() @ diags(v.conj()))
    dm = diags(current.conj()*u) + dv @ ybus.conj() @ diags(u.conj())
    return dtheta.tocsr(), dm.tocsr()


def residual(net: Network, model: Injections, v: ComplexArray,
             a: NDArray[np.int64], pq: NDArray[np.int64]) -> RealArray:
    spec, _ = model.evaluate(abs(v))
    mis = v * (net.ybus @ v).conj() - spec
    return np.r_[mis.real[a], mis.imag[pq]]


def jacobian(net: Network, model: Injections, v: ComplexArray,
             a: NDArray[np.int64], pq: NDArray[np.int64]):
    da, dm = derivatives(net.ybus, v)
    _, dspec = model.evaluate(abs(v))
    dm = dm - diags(dspec)
    return bmat([[da[a][:, a].real, dm[a][:, pq].real],
                 [da[pq][:, a].imag, dm[pq][:, pq].imag]], format="csc")


def displaced(v: ComplexArray, a: NDArray[np.int64], pq: NDArray[np.int64],
              dx: RealArray, alpha: float = 1.0) -> ComplexArray | None:
    theta, m = np.angle(v), abs(v)
    theta[a] += alpha*dx[:len(a)]
    m[pq] += alpha*dx[len(a):]
    if not np.isfinite(m).all() or np.any(m <= 1e-6):
        return None
    return m*np.exp(1j*theta)


def solve(net: Network, model: Injections, v0: ComplexArray,
          ref: list[int], pv: list[int], pq: list[int],
          tol: float = 1e-11, max_steps: int = 30) -> tuple[ComplexArray, list[float]]:
    """Fixed-mode Newton with sparse LU and squared-residual backtracking.

    Input v0 contains the prescribed reference voltages and PV magnitudes.
    The mode lists must partition all buses; every connected component must
    have one reference. References are ideal balancing sources in this demo.
    """
    n = net.ybus.shape[0]
    if sorted(ref+pv+pq) != list(range(n)):
        raise ValueError("ref, pv, pq must partition the internal bus indices.")
    if not np.isfinite(tol) or tol <= 0 or max_steps < 0:
        raise ValueError("Invalid termination options.")
    for array in (model.generation, model.demand):
        if array.shape != (n,) or not np.isfinite(array).all():
            raise ValueError("Invalid injection data.")
    for z in (model.p_zip, model.q_zip):
        if (z.shape != (n, 3) or not np.isfinite(z).all()
                or (z < 0).any() or not np.allclose(z.sum(axis=1), 1)):
            raise ValueError("ZIP rows must contain nonnegative fractions summing to one.")
    graph = net.cf.T @ net.ct + net.ct.T @ net.cf
    count, labels = connected_components(graph, directed=False)
    for k in range(count):
        if sum(labels[r] == k for r in ref) != 1:
            raise ValueError("Every component requires exactly one reference in this demo.")
    a, q = np.asarray(pv+pq, dtype=int), np.asarray(pq, dtype=int)
    v = np.asarray(v0, complex).copy()
    if v.shape != (n,) or not np.isfinite(v).all() or (abs(v) <= 1e-6).any():
        raise ValueError("Invalid initial voltage vector.")
    history: list[float] = []
    for k in range(max_steps+1):
        f = residual(net, model, v, a, q)
        if not np.isfinite(f).all():
            raise RuntimeError(f"Non-finite residual at step {k}.")
        norm = float(np.linalg.norm(f, np.inf)) if f.size else 0.0
        history.append(norm)
        if norm <= tol:
            return v, history
        if k == max_steps:
            break
        try:
            dx = splu(jacobian(net, model, v, a, q)).solve(-f)
        except RuntimeError as exc:
            raise RuntimeError(f"Sparse factorization failed at step {k}.") from exc
        if not np.isfinite(dx).all():
            raise RuntimeError("Non-finite Newton direction.")
        phi, alpha = 0.5*float(f @ f), 1.0
        accepted = False
        for _ in range(25):
            trial = displaced(v, a, q, dx, alpha)
            if trial is not None:
                ft = residual(net, model, trial, a, q)
                if np.isfinite(ft).all() and 0.5*float(ft @ ft) <= phi*(1-2e-4*alpha):
                    v, accepted = trial, True
                    break
            alpha *= 0.5
        if not accepted:
            raise RuntimeError(f"Line search failed at step {k}; residual={norm:.3e}.")
    raise RuntimeError(f"Iteration limit reached; residual={history[-1]:.3e}.")


def terminal_flows(net: Network, v: ComplexArray) -> tuple[ComplexArray, ComplexArray]:
    return ((net.cf @ v) * (net.yf @ v).conj(),
            (net.ct @ v) * (net.yt @ v).conj())


def scalar_terminal_injections(net: Network, v: ComplexArray) -> ComplexArray:
    """A separate terminal-law evaluation: no Ybus and no matrix Jacobian.

    This path checks the implementation, not the correctness of the physical
    assumptions or of the input data shared by both paths.
    """
    current = net.ysh*v
    for e in net.branches:
        tap = e.tap*np.exp(1j*np.deg2rad(e.shift_deg))
        vf_internal = v[e.f]/tap
        series = (vf_internal-v[e.t])/complex(e.r, e.x)
        current[e.f] += (series + 0.5j*e.b*vf_internal)/tap.conjugate()
        current[e.t] += -series + 0.5j*e.b*v[e.t]
    return v*current.conj()


def directional_error(net: Network, model: Injections, v: ComplexArray,
                      a: NDArray[np.int64], pq: NDArray[np.int64]) -> dict[str, float]:
    rng = np.random.default_rng(20260908)
    p = rng.normal(size=len(a)+len(pq))
    p /= np.linalg.norm(p)
    jp = jacobian(net, model, v, a, pq) @ p
    result = {}
    for h in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
        vp, vm = displaced(v, a, pq, p, h), displaced(v, a, pq, p, -h)
        if vp is None or vm is None:
            raise AssertionError("Invalid finite-difference test point.")
        fd = (residual(net, model, vp, a, pq)-residual(net, model, vm, a, pq))/(2*h)
        result[f"{h:.0e}"] = float(np.linalg.norm(fd-jp, np.inf)/max(1., np.linalg.norm(jp, np.inf)))
    return result


def pair(v: complex) -> list[float]:
    return [float(v.real), float(v.imag)]


def main() -> dict:
    branches = (Branch(0, 1, .02, .06, .03, 1.02, 4.),
                Branch(0, 2, .08, .24, .025),
                Branch(1, 2, .06, .18, .02))
    net = assemble(3, branches)
    cp = np.tile([0., 0., 1.], (3, 1))
    model = Injections(np.array([0., .5, 0.], complex),
                       np.array([0., 0., .9+.35j]), cp, cp)
    v0 = np.array([1.04, 1.02, 1.], complex)
    a, pq = np.array([1, 2]), np.array([2])
    v, history = solve(net, model, v0, [0], [1], [2])
    sf, st = terminal_flows(net, v)
    s = v*(net.ybus @ v).conj()
    balance = s.sum() - (sf+st).sum() - (abs(v)**2*net.ysh.conj()).sum()
    scalar_error = float(np.max(abs(s-scalar_terminal_injections(net, v))))
    rotation_error = float(np.max(abs(s-v*np.exp(.37j)*(net.ybus @ (v*np.exp(.37j))).conj())))
    da, _ = derivatives(net.ybus, v)
    null_error = float(np.max(abs(da @ np.ones(3))))
    fd_error = directional_error(net, model, v0, a, pq)

    # Different nonlinear algorithm, direct terminal laws, numerical Jacobian.
    def scalar_residual(x: RealArray) -> RealArray:
        vs = np.array([1.04, 1.02*np.exp(1j*x[0]), x[2]*np.exp(1j*x[1])])
        mis = scalar_terminal_injections(net, vs)-model.evaluate(abs(vs))[0]
        return np.r_[mis.real[a], mis.imag[pq]]
    other = root(scalar_residual, np.array([0., 0., 1.]), method="hybr", options={"xtol": 1e-11})
    if not other.success or np.max(abs(scalar_residual(other.x))) > 1e-9:
        raise AssertionError("The independent residual-path root check failed.")
    v_other = np.array([1.04, 1.02*np.exp(1j*other.x[0]), other.x[2]*np.exp(1j*other.x[1])])
    alternative_error = float(np.max(abs(v-v_other)))

    # Enforce one intentionally tight Q limit by explicitly changing equations.
    qmax = 0.10
    if not s[1].imag > qmax:
        raise AssertionError("The example must activate the bus-2 Q limit.")
    limited_model = Injections(np.array([0., .5+1j*qmax, 0.]), model.demand, cp, cp)
    limited, limited_history = solve(net, limited_model, v, [0], [], [1, 2])
    sl = limited*(net.ybus @ limited).conj()
    if abs(sl[1].imag-qmax) > 1e-9 or abs(limited[1]) >= 1.02:
        raise AssertionError("Q-limited equations or expected voltage release failed.")

    # ZIP derivative check; P and Q use distinct coefficients.
    zp, zq = cp.copy(), cp.copy()
    zp[2], zq[2] = [.2, .3, .5], [.1, .2, .7]
    zip_model = Injections(model.generation, model.demand, zp, zq)
    zip_error = directional_error(net, zip_model, v0, a, pq)
    zip_v, _ = solve(net, zip_model, v0, [0], [1], [2])
    zip_residual = float(np.max(abs(residual(net, zip_model, zip_v, a, pq))))

    # Additional shunt, parallel-branch, permutation, and invalid-island checks.
    net_sh = assemble(3, branches+(branches[2],), np.array([.001+.01j, 0., -.02j]))
    shunt_scalar_error = float(np.max(abs(v*(net_sh.ybus@v).conj()-scalar_terminal_injections(net_sh, v))))
    shf, sht = terminal_flows(net_sh, v)
    shunt_balance = float(abs((v*(net_sh.ybus@v).conj()).sum()-(shf+sht).sum()-(abs(v)**2*net_sh.ysh.conj()).sum()))
    permutation = np.array([2, 0, 1])  # new index for each old bus
    pb = tuple(Branch(int(permutation[e.f]), int(permutation[e.t]), e.r, e.x, e.b, e.tap, e.shift_deg) for e in branches)
    vp0 = np.empty_like(v0); vp0[permutation] = v0
    pg, pd = np.empty_like(model.generation), np.empty_like(model.demand)
    pg[permutation], pd[permutation] = model.generation, model.demand
    permuted, _ = solve(assemble(3, pb), Injections(pg, pd, cp, cp), vp0, [2], [0], [1])
    permutation_error = float(np.max(abs(permuted[permutation]-v)))
    island_rejected = False
    try:
        solve(assemble(3, branches[:1]), model, v0, [0], [1], [2])
    except ValueError as exc:
        island_rejected = "reference" in str(exc)

    tests = {
        "complex_power_balance_abs_pu": float(abs(balance)),
        "terminal_law_vs_ybus_max_abs_pu": scalar_error,
        "uniform_angle_rotation_max_abs_pu": rotation_error,
        "angle_derivative_null_vector_max_abs": null_error,
        "alternative_nonlinear_solve_max_voltage_error_pu": alternative_error,
        "directional_jacobian_relative_errors": fd_error,
        "zip_directional_jacobian_relative_errors": zip_error,
        "zip_final_residual_pu": zip_residual,
        "shunt_parallel_branch_scalar_error_pu": shunt_scalar_error,
        "shunt_parallel_branch_power_balance_pu": shunt_balance,
        "bus_permutation_max_voltage_error_pu": permutation_error,
        "unreferenced_island_rejected": island_rejected,
    }
    if max(abs(balance), scalar_error, rotation_error, null_error,
           alternative_error, shunt_scalar_error, shunt_balance, permutation_error) > 1e-9:
        raise AssertionError("A structural regression test failed.")
    if min(fd_error.values()) > 1e-8 or min(zip_error.values()) > 1e-8 or not island_rejected:
        raise AssertionError("A derivative or validation test failed.")
    return {
        "scope": "Synthetic three-bus verification example; not an industrial benchmark.",
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "base_mva": 100.0,
        "base_case": {
            "newton_steps": len(history)-1,
            "residual_history_pu": history,
            "voltage_magnitudes_pu": abs(v).tolist(),
            "voltage_angles_degrees": np.rad2deg(np.angle(v)).tolist(),
            "net_bus_injections_pu_P_Q": [pair(si) for si in s],
            "branch_from_powers_pu_P_Q": [pair(si) for si in sf],
            "branch_to_powers_pu_P_Q": [pair(si) for si in st],
            "total_branch_absorption_pu_P_Q": pair((sf+st).sum()),
        },
        "q_limited_case": {
            "bus_2_qmax_pu": qmax,
            "newton_steps_after_mode_change": len(limited_history)-1,
            "residual_history_pu": limited_history,
            "voltage_magnitudes_pu": abs(limited).tolist(),
            "voltage_angles_degrees": np.rad2deg(np.angle(limited)).tolist(),
            "net_bus_injections_pu_P_Q": [pair(si) for si in sl],
        },
        "verification": tests,
        "external_validation": "MATPOWER case supplied separately; MATLAB/Octave comparison not executed here.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Write the same results to a JSON file.")
    args = parser.parse_args()
    results = main()
    text = json.dumps(results, indent=2, allow_nan=False)
    print(text)
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text+'\n', encoding="utf-8")
