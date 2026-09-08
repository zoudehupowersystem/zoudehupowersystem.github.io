---
layout: article
lang: en
title: "AC Power Flow from Ybus to Newton: Complex-Matrix Derivatives and Sparse Implementation"
permalink: "/ac-power-flow-ybus-newton.html"
seo_title: "AC Power Flow from Ybus to Newton: Complex-Matrix Derivatives and Sparse Implementation | Dehu Zou"
description: "A rigorous, implementation-oriented derivation of AC power flow from network topology and Ybus to Newton's method, complex-matrix Jacobians, PV/PQ controls, sparse factorization, limits, approximations, and verification."
updated: "2026-09-08"
---

# AC Power Flow from Ybus to Newton: Complex-Matrix Derivatives and Sparse Implementation

<div class="article-meta" style="margin:-4px 0 24px;color:#667085;font-size:.9rem;display:flex;gap:8px 18px;flex-wrap:wrap;"><span>Author: Dehu Zou</span><span>Updated: 2026-09-08</span><span>Language: English</span></div>

AC power flow—also called load flow—is often taught as a large collection of bus-by-bus trigonometric formulas. That route is valid, but it can hide the structure that matters most in analysis and software: **topology builds a sparse network operator; voltage determines current linearly; complex power introduces the essential nonlinearity; Newton's method repeatedly linearizes that nonlinear map; and industrial performance is dominated by sparse assembly and sparse linear solves rather than by the scalar formulas themselves.**

This article develops that chain from first principles. It is not a new power-flow algorithm. It is a matrix-centric derivation of the standard AC formulation, written to make the mathematics, the control interpretation, and the implementation line up with each other.

A few points are stated explicitly because they are common sources of confusion:

- The matrix formulation and the conventional elementwise formulation are mathematically equivalent when they represent the same equations. Matrix notation does **not** improve Newton convergence by itself.
- We never form an explicit inverse of the Jacobian. We solve a sparse linear system.
- PQ, PV, and reference/slack "bus types" are best understood as reduced forms of device control equations, not immutable properties of a bus.
- Convergence of a numerical iteration is not the same as physical feasibility. Reactive limits, active-power limits, tap ranges, island references, and operating constraints still matter.
- The complex derivatives below are **real differentials of complex-valued functions**. No assumption of holomorphic complex analysis is required.

The presentation assumes a balanced positive-sequence steady-state AC network in per unit. Unbalanced multiphase distribution power flow requires a larger phase-domain model, but the same structural ideas—network assembly, residual equations, Jacobians, sparse solves, controls, and verification—still apply.

---

## 1. Notation and sign convention

Let the network contain $n$ buses and $\ell$ branches.

The bus-voltage phasor vector is

$$
V \in \mathbb C^n,
\qquad
V = m \odot e^{j\theta},
$$

where

$$
m = |V| \in \mathbb R_{>0}^n,
\qquad
\theta \in \mathbb R^n.
$$

For a vector $a$, define

$$
[a] \equiv \operatorname{diag}(a).
$$

The symbol $\odot$ denotes elementwise multiplication. In this article,

$$
A^*
$$

means **elementwise complex conjugation**, while

$$
A^T
$$

is transpose and

$$
A^H=(A^*)^T
$$

is conjugate transpose.

Positive $P_i$ and $Q_i$ mean **net injection from bus $i$ into the network**. A consuming load therefore normally appears as a negative net injection after generation and load are aggregated.

When $Y$ is fixed, the basic network equation is

$$
\boxed{I=YV.}
$$

The nonlinear nodal complex-power map is

$$
\boxed{
S(V)=[V]I^*=[V](YV)^*
}
$$

with

$$
S=P+jQ.
$$

For a fixed linear network and constant specified injections, this product $V\odot I^*$ is where the familiar AC power-flow nonlinearity enters. Voltage-dependent loads, converter controls, tap controls, and other device models can add further nonlinear terms.

---

## 2. From topology and device models to $Y_{\mathrm{bus}}$

A robust power-flow implementation should separate two questions:

1. **How are devices connected?**
2. **What terminal relation does each device obey?**

That separation is more general than memorizing entries of $Y_{\mathrm{bus}}$.

### 2.1 Simple series branches

First consider a network containing only reciprocal series admittances and bus shunts. Assign an arbitrary orientation to each branch and define an incidence matrix

$$
D\in\mathbb R^{\ell\times n}.
$$

If branch $k$ is oriented from bus $i$ to bus $j$,

$$
D_{ki}=1,
\qquad
D_{kj}=-1.
$$

Let the vector of series branch admittances be

$$
y=(y_1,\ldots,y_\ell)^T.
$$

The branch voltage differences are

$$
v_{\mathrm{br}}=DV,
$$

the oriented branch currents are

$$
i_{\mathrm{br}}=[y]DV,
$$

and KCL maps those branch currents back to buses:

$$
I=D^Ti_{\mathrm{br}}.
$$

Therefore

$$
\boxed{
Y=D^T[y]D+Y_{\mathrm{sh}}.
}
$$

Reversing the arbitrary orientation of a branch changes the sign of one row of $D$, but it does not change $D^T[y]D$.

This compact expression is valuable conceptually, but it is not general enough for every practical branch model.

### 2.2 General two-port branch model

A transmission line with charging, an off-nominal transformer, or a phase-shifting transformer is more naturally written as a two-port relation:

$$
\begin{bmatrix}
I_{f,k}\\
I_{t,k}
\end{bmatrix}
=
\begin{bmatrix}
y_{ff,k} & y_{ft,k}\\
y_{tf,k} & y_{tt,k}
\end{bmatrix}
\begin{bmatrix}
V_{f,k}\\
V_{t,k}
\end{bmatrix}.
$$

Define connection matrices

$$
C_f,C_t\in\{0,1\}^{\ell\times n}
$$

such that

$$
V_f=C_fV,
\qquad
V_t=C_tV.
$$

Collecting all branch primitive admittances,

$$
Y_f=[y_{ff}]C_f+[y_{ft}]C_t,
$$

$$
Y_t=[y_{tf}]C_f+[y_{tt}]C_t.
$$

Then

$$
I_f=Y_fV,
\qquad
I_t=Y_tV,
$$

and the nodal admittance matrix is assembled as

$$
\boxed{
Y_{\mathrm{bus}}
=
C_f^T Y_f
+
C_t^T Y_t
+
Y_{\mathrm{sh}}.
}
$$

For a standard $\pi$-model branch with series admittance $y_s$, total charging susceptance $b_c$, and a complex tap at the from side

$$
t=\tau e^{j\phi},
$$

one common primitive model is

$$
y_{ff}=\frac{y_s+j b_c/2}{|t|^2},
\qquad
y_{ft}=-\frac{y_s}{t^*},
$$

$$
y_{tf}=-\frac{y_s}{t},
\qquad
y_{tt}=y_s+j b_c/2.
$$

A phase shift can make

$$
y_{ft}\neq y_{tf},
$$

so $Y_{\mathrm{bus}}$ should not be assumed to be an ordinary symmetric matrix in a general implementation.

The practical lesson is simple: **assemble a global sparse operator from local terminal models.** This is the same software pattern used in many network and finite-element computations.

---

## 3. The AC nodal power equations

Given

$$
I=YV,
$$

the net complex power injected at every bus is

$$
\boxed{
S=[V](YV)^*.
}
$$

This one vector equation contains the standard real and reactive power equations.

Let

$$
Y_{ij}=G_{ij}+jB_{ij},
\qquad
V_i=m_i e^{j\theta_i},
$$

and define

$$
\theta_{ij}=\theta_i-\theta_j.
$$

Expanding the matrix equation at bus $i$ gives the familiar formulas

$$
P_i
=
m_i\sum_{j=1}^{n}m_j
\left(
G_{ij}\cos\theta_{ij}
+
B_{ij}\sin\theta_{ij}
\right),
$$

$$
Q_i
=
m_i\sum_{j=1}^{n}m_j
\left(
G_{ij}\sin\theta_{ij}
-
B_{ij}\cos\theta_{ij}
\right).
$$

These scalar formulas are not a different model. They are simply the real-coordinate expansion of

$$
S=[V](YV)^*.
$$

The matrix form keeps the network structure visible; the scalar form is often useful when inspecting one bus or one derivative by hand.

---

## 4. PQ, PV, and reference buses are control equations in disguise

A bus is a connection point. It does not physically "know" whether it is PQ or PV. The classification appears after device equations are reduced.

Suppose an aggregated controllable generator at bus $i$ has steady-state outputs

$$
p_{g,i},\qquad q_{g,i}.
$$

Three standard control modes are:

### 4.1 PQ mode

The device fixes active and reactive power:

$$
p_{g,i}=p_{g,i}^{\star},
\qquad
q_{g,i}=q_{g,i}^{\star}.
$$

The network solution determines

$$
\theta_i,\qquad m_i.
$$

A constant-power load is also a PQ injection with the opposite sign convention.

### 4.2 PV mode

The device fixes active power and voltage magnitude:

$$
p_{g,i}=p_{g,i}^{\star},
\qquad
m_i=m_i^{\star}.
$$

Reactive power becomes an algebraic output required to satisfy the network equations.

This model is valid only while the required reactive power lies inside the regulating capability:

$$
q_{g,i}^{\min}
\le q_{g,i}
\le q_{g,i}^{\max}.
$$

If a limit is binding, the correct model change is not to clip $q_g$ while continuing to enforce the voltage target. The voltage-control equation must be released and the reactive limit enforced; in the classical reduced formulation this is the familiar **PV-to-PQ switching**.

### 4.3 Reference/slack mode

A classical reference bus fixes

$$
\theta_i=\theta_i^\star,
\qquad
m_i=m_i^\star,
$$

while its net $P$ and $Q$ become outputs.

Two roles are often bundled together here:

1. providing an angular reference for the synchronous island;
2. absorbing active/reactive mismatch and losses.

They are conceptually separable. A system may keep one angle reference while distributing active-power balancing among several generators through participation factors. For each connected synchronous island, however, the angular degree of freedom must be anchored somewhere.

### 4.4 The classical reduced state

Let

- $\mathcal A$ be the set of non-reference buses, i.e. PV and PQ buses;
- $\mathcal Q$ be the set of PQ buses.

The classical polar Newton state is

$$
x=
\begin{bmatrix}
\theta_{\mathcal A}\\
m_{\mathcal Q}
\end{bmatrix}.
$$

The active-power equations are enforced for $\mathcal A$, while reactive-power equations are enforced only for $\mathcal Q$.

This reduction is convenient, but it should not hide the underlying control logic. Remote voltage control, multiple generators on one bus, distributed slack, switched shunts, converter modes, tap controllers, and limit handling are easier to reason about when written as explicit device equations or active-set logic.

---

## 5. Newton's method: what it does and what it does not guarantee

For a nonlinear system

$$
F(x)=0,
$$

Newton's method linearizes around $x_k$:

$$
F(x_k+\Delta x)
\approx
F(x_k)+J(x_k)\Delta x,
$$

where

$$
J(x_k)=\frac{\partial F}{\partial x}(x_k).
$$

The Newton correction is obtained from

$$
\boxed{
J(x_k)\Delta x=-F(x_k)
}
$$

and

$$
x_{k+1}=x_k+\Delta x.
$$

No explicit inverse is needed or desirable.

If $F$ is sufficiently smooth, the Jacobian at the solution is nonsingular, and the initial point is sufficiently close to that solution, Newton's method is locally quadratically convergent. Those conditions matter. Newton is a powerful local method, not a global guarantee.

For classical power flow it is convenient to define the mismatch vector

$$
r(x)=
\begin{bmatrix}
P_{\mathcal A}^{\mathrm{spec}}-P_{\mathcal A}^{\mathrm{calc}}(x)\\
Q_{\mathcal Q}^{\mathrm{spec}}-Q_{\mathcal Q}^{\mathrm{calc}}(x)
\end{bmatrix}.
$$

If $J$ is assembled as the derivative of the calculated injections with respect to the state,

$$
J=
\frac{\partial
\begin{bmatrix}
P_{\mathcal A}^{\mathrm{calc}}\\
Q_{\mathcal Q}^{\mathrm{calc}}
\end{bmatrix}}
{\partial
\begin{bmatrix}
\theta_{\mathcal A}\\
m_{\mathcal Q}
\end{bmatrix}},
$$

then each Newton step solves

$$
\boxed{
J\Delta x=r.
}
$$

A production solver usually monitors at least the mismatch norm

$$
\|r\|_\infty
$$

and often the state correction as well. Convergence tolerance should be defined in a consistent per-unit system and should not be confused with engineering acceptability.

### 5.1 Why Newton power flow can fail

Typical causes include:

- a poor initial state;
- incorrect topology or parameters;
- disconnected islands without proper references;
- a physically infeasible dispatch or voltage-control request;
- reactive-power limits that have not been modeled correctly;
- severe voltage stress, where the power-flow Jacobian becomes ill-conditioned;
- zero or near-zero impedance branches handled without suitable preprocessing;
- large $R/X$ ratios or device behavior that makes the chosen formulation poorly conditioned.

Near a saddle-node voltage-collapse point, singularity of the relevant power-flow Jacobian is part of the physics, not merely a software defect. A solver should therefore distinguish "bad numerics" from "the modeled operating point is close to or beyond a solvability boundary."

Damped Newton or a line search,

$$
x_{k+1}=x_k+\alpha_k\Delta x,
\qquad
0<\alpha_k\le 1,
$$

can enlarge the practical basin of convergence. Continuation methods, trust-region strategies, better initializations, and alternative formulations may be needed for very stressed cases.

---

## 6. A complex-matrix derivation of the AC Jacobian

This section is the core of the article.

The objective is not to invent a different Jacobian. It is to derive the conventional four real Jacobian blocks from two compact complex derivative matrices.

### 6.1 Voltage differential

Write

$$
V=m\odot e^{j\theta}.
$$

Define the unit phasor vector

$$
u=V\oslash m=e^{j\theta}.
$$

For each bus,

$$
\frac{\partial V_i}{\partial\theta_i}=jV_i,
\qquad
\frac{\partial V_i}{\partial m_i}=u_i.
$$

For all buses together,

$$
\boxed{
dV=j[V]\,d\theta+[u]\,dm.
}
$$

Taking the elementwise conjugate,

$$
\boxed{
dV^*=-j[V^*]\,d\theta+[u^*]\,dm.
}
$$

Geometrically, an angle perturbation moves a voltage phasor tangentially; a magnitude perturbation moves it radially.

### 6.2 Complex-power differential

Start from

$$
S=[V]I^*.
$$

By the product rule,

$$
dS=[dV]I^*+[V]\,dI^*.
$$

Using

$$
[dV]I^*=[I^*]dV
$$

and, for fixed $Y$,

$$
dI=Y\,dV,
\qquad
dI^*=Y^*\,dV^*,
$$

we obtain

$$
\boxed{
dS=[I^*]\,dV+[V]Y^*\,dV^*.
}
$$

Substitute the voltage differentials:

$$
dS=S_\theta\,d\theta+S_m\,dm
$$

with

$$
\boxed{
S_\theta
=
j[V]\left([I^*]-Y^*[V^*]\right),
}
$$

and

$$
\boxed{
S_m
=
[I^*][u]+[V]Y^*[u^*].
}
$$

Here

$$
S_\theta=\frac{\partial S}{\partial\theta},
\qquad
S_m=\frac{\partial S}{\partial m}
$$

are complex $n\times n$ matrices.

This is a real-variable differential of a complex-valued function. It does not rely on complex analyticity; conjugation is handled explicitly.

### 6.3 Recovering the four real Jacobian blocks

Because

$$
S=P+jQ,
$$

we have

$$
dP=\operatorname{Re}(dS),
\qquad
dQ=\operatorname{Im}(dS).
$$

Therefore the full polar Jacobian is

$$
\boxed{
J_{\mathrm{full}}
=
\begin{bmatrix}
\operatorname{Re}(S_\theta) & \operatorname{Re}(S_m)\\
\operatorname{Im}(S_\theta) & \operatorname{Im}(S_m)
\end{bmatrix}.
}
$$

These are exactly the conventional blocks

$$
H=\frac{\partial P}{\partial\theta},
\qquad
N=\frac{\partial P}{\partial m},
$$

$$
M=\frac{\partial Q}{\partial\theta},
\qquad
L=\frac{\partial Q}{\partial m}.
$$

For the standard reduced state, select the required rows and columns:

$$
\boxed{
J=
\begin{bmatrix}
\operatorname{Re}(S_\theta)_{\mathcal A,\mathcal A}
&
\operatorname{Re}(S_m)_{\mathcal A,\mathcal Q}
\\[4pt]
\operatorname{Im}(S_\theta)_{\mathcal Q,\mathcal A}
&
\operatorname{Im}(S_m)_{\mathcal Q,\mathcal Q}
\end{bmatrix}.
}
$$

This is the Jacobian used in the classical polar Newton power flow.

### 6.4 Relation to MATPOWER notation

The same derivatives can be written in the style used by MATPOWER:

```text
I       = Ybus * V
Vnorm   = V ./ abs(V)

dS_dVa  = 1j * diag(V) * conj(diag(I) - Ybus * diag(V))
dS_dVm  = diag(V) * conj(Ybus * diag(Vnorm)) \
           + conj(diag(I)) * diag(Vnorm)
```

The formulas are equivalent to the expressions above and are documented in MATPOWER Technical Note 2 [4].

A critical point: if an elementwise implementation and a matrix implementation assemble the same mathematical Jacobian, they should generate the same Newton direction to floating-point accuracy. Any material difference in convergence indicates a difference in equations, indexing, limit logic, initialization, numerical linear algebra, or implementation error—not a mysterious advantage of matrix notation.

### 6.5 When the specified injection depends on voltage

The reduced Jacobian above assumes the specified $P$ and $Q$ in the active equations are constants.

If a load is ZIP-like, for example,

$$
S_{\mathrm{load}}=S_{\mathrm{load}}(m),
$$

or if a converter/controller injection depends on $V$, the true residual is

$$
F(x)
=
S^{\mathrm{calc}}(x)-S^{\mathrm{spec}}(x),
$$

and the Jacobian must include

$$
\frac{\partial F}{\partial x}
=
\frac{\partial S^{\mathrm{calc}}}{\partial x}
-
\frac{\partial S^{\mathrm{spec}}}{\partial x}.
$$

Treating a voltage-dependent injection as a constant-power specification changes the model, not merely the solver.

---

## 7. Branch flows fit the same matrix pattern

After solving the bus voltages, branch terminal flows are obtained without introducing a new conceptual framework.

Recall

$$
V_f=C_fV,
\qquad
V_t=C_tV,
$$

$$
I_f=Y_fV,
\qquad
I_t=Y_tV.
$$

The complex powers injected from each terminal into each branch are

$$
\boxed{
S_f=[V_f]I_f^*,
\qquad
S_t=[V_t]I_t^*.
}
$$

With this terminal sign convention, branch complex loss is

$$
\boxed{
S_{\mathrm{loss}}=S_f+S_t.
}
$$

If branch-flow sensitivities are needed for OPF, security analysis, or state estimation, the same product-rule pattern applies:

$$
dS_f=[I_f^*]C_f\,dV+[V_f]Y_f^*\,dV^*,
$$

and similarly for the to end.

The important pattern is reusable:

$$
\boxed{
\text{power differential}
=
\text{voltage-change term}
+
\text{current-change term}.
}
$$

---

## 8. Sparse implementation: where industrial performance actually comes from

For a large grid, $Y_{\mathrm{bus}}$ and the Newton Jacobian are sparse. The central implementation rule is therefore:

> **Preserve sparsity from model assembly to the linear solve.**

The 1967 work of Tinney and Hart made Newton power flow practical by combining the method with sparse elimination and careful ordering [1]. Tinney and Walker's sparse-factorization work from the same period remains historically important for understanding why network problems can be solved efficiently [2].

### 8.1 Do not explicitly invert the Jacobian

Never compute

$$
J^{-1}
$$

just to form

$$
\Delta x=J^{-1}r.
$$

The inverse is generally much denser than the original sparse matrix and is unnecessary. Use a sparse direct solve,

$$
J\Delta x=r,
$$

typically based on sparse LU for the general unsymmetric real Jacobian.

### 8.2 Separate symbolic structure from numerical values

For fixed topology and a fixed PV/PQ active set, the sparsity pattern of the Jacobian is largely fixed even though its numerical values change every Newton iteration.

A high-performance implementation can therefore separate:

- network/topology preprocessing;
- sparse pattern construction;
- fill-reducing ordering;
- repeated numerical Jacobian updates;
- repeated numerical factorizations and triangular solves.

The symbolic analysis or ordering can often be reused while the structure is unchanged, although numerical pivoting behavior depends on the sparse solver.

### 8.3 Do not materialize dense diagonal matrices

Expressions such as

$$
[V]Y^*[u^*]
$$

are excellent for derivation. They do not imply that software should create an $n\times n$ dense diagonal matrix.

Multiplication by $[V]$ is row scaling; multiplication by $[u^*]$ is column scaling. Sparse libraries or custom kernels should exploit that structure directly.

### 8.4 A minimal Newton kernel

A clean implementation can be organized around the following skeleton:

```text
build Ybus and branch matrices
identify reference, PV and PQ sets
initialize V

repeat:
    I = Ybus * V
    S = V .* conj(I)

    dP = Pspec - real(S)
    dQ = Qspec - imag(S)
    r  = [dP[pv ∪ pq]; dQ[pq]]

    if norm_inf(r) < tolerance:
        converged

    build dS_dVa and dS_dVm
    extract reduced real Jacobian J

    dx = sparse_solve(J, r)

    Va[pv ∪ pq] += alpha * dx_angle
    Vm[pq]      += alpha * dx_magnitude

    V = Vm .* exp(1j * Va)
```

Reactive limits and other discrete control changes should usually be handled by a clearly defined outer active-set/state-machine policy rather than by uncontrolled mode switching inside every incomplete Newton step.

### 8.5 Initial conditions matter

A flat start,

$$
m_i=1,\qquad \theta_i=0,
$$

is useful for many transmission cases but is not universal.

For online applications, the previous solved operating point or state-estimator solution is usually a much better initialization. For difficult distribution or stressed-network cases, a continuation strategy or an alternative formulation may be more reliable.

---

## 9. Why fast-decoupled and DC power flow work—and where they do not

The Jacobian itself exposes the approximations behind classical simplified power-flow methods.

In many high-voltage transmission systems,

$$
X\gg R,
$$

voltage magnitudes are near 1 p.u., and angle differences are moderate. Under those conditions, the dominant couplings are often approximately

$$
P \leftrightarrow \theta,
\qquad
Q \leftrightarrow m,
$$

while the cross-couplings are weaker.

The fast-decoupled load flow of Stott and Alsac [3] exploits this structure and replaces changing Jacobian blocks with simplified, nearly constant susceptance matrices. The main computational advantage is that those matrices can be factored once and reused over iterations.

That approximation is particularly attractive when the transmission assumptions are good. It can degrade when:

- $R/X$ is high;
- the system is heavily stressed;
- voltage magnitudes deviate substantially;
- phase-shifting or other controls are influential;
- distribution-network physics dominate;
- the operating point weakens the $P$-$\theta$, $Q$-$V$ decoupling.

DC power flow goes further: it neglects reactive-power/voltage-magnitude behavior and typically assumes small angle differences, near-unit voltage magnitudes, and predominantly reactive branches. It is extremely useful for screening, market optimization, and planning models where a linear active-power approximation is appropriate. It should not be interpreted as a universally accurate surrogate for full AC power flow.

The general principle is broader than these two algorithms:

> **Approximation should follow from a stated physical regime, not from habit.**

---

## 10. Convergence, solvability, and physical validity are different questions

A mature power-flow program should not reduce every failure to "Newton did not converge."

At least three questions must be separated.

### 10.1 Did the numerical iteration converge?

This is a statement about residuals and steps:

$$
\|r\| \rightarrow 0.
$$

### 10.2 Does a nearby mathematical solution exist and is it well conditioned?

A severely ill-conditioned Jacobian may indicate proximity to a solvability boundary. Multiple power-flow solutions can exist, and Newton converges only to the basin reached from its initial point.

### 10.3 Is the converged solution physically admissible?

A numerically converged solution may still violate:

- generator $P/Q$ capability;
- bus-voltage limits;
- branch thermal limits;
- transformer tap ranges;
- switched-shunt limits;
- converter current limits;
- controller mode assumptions.

This distinction is essential in planning, online security analysis, and industrial simulation. "Converged" is necessary, not sufficient.

---

## 11. What usually breaks real implementations

The hardest bugs in a power-flow solver are rarely the Newton formula itself.

### 11.1 Sign conventions

Choose one convention for bus injection, branch terminal direction, load sign, and line loss, then enforce it everywhere.

### 11.2 Transformer conventions

Off-nominal tap direction, phase-shift sign, base-voltage conversion, and from/to terminal definitions must agree with the data model.

### 11.3 Per-unit bases

A mathematically correct solver with inconsistent MVA or voltage bases can return plausible-looking but wrong results.

### 11.4 Island handling

Every electrical island needs an angular reference. An accidentally isolated subnetwork can make the reduced Jacobian singular.

### 11.5 PV/PQ switching

Reactive limits are an active-set problem. Hysteresis or an outer-loop policy is useful to avoid chattering near a limit.

### 11.6 Discrete controls

Transformer taps and switched shunts are discrete decisions in many applications. They should not be silently treated as ordinary smooth Newton variables unless the model deliberately relaxes them.

### 11.7 Model-data inconsistency

A convergent algorithm cannot repair a wrong topology, a 100-fold impedance error, an impossible dispatch, or a duplicated device. Diagnostics are part of the solver.

---

## 12. Verification: how to make the implementation defensible

A solver intended for serious engineering should be verified at several levels.

### 12.1 Derivative test

For a random direction $p$, compare the analytic Jacobian-vector product with a centered finite difference:

$$
J(x)p
$$

against

$$
\frac{F(x+hp)-F(x-hp)}{2h}.
$$

Over a sensible range of $h$, the error should decrease before roundoff dominates.

This directional test is more scalable than checking every individual Jacobian element and catches indexing, sign, conjugation, and selection errors effectively.

### 12.2 Cross-check against an independent implementation

Run standard cases and compare:

- bus voltage magnitudes;
- bus voltage angles;
- generator $P/Q$;
- branch terminal $P/Q$;
- total losses;
- limit-mode outcomes.

MATPOWER is a useful open reference implementation for this purpose [4,5].

### 12.3 Check conservation laws

After convergence, verify KCL/KCL-derived power balance consistently with the modeled shunts and branch losses.

### 12.4 Test difficult cases deliberately

A test suite should include more than easy IEEE cases:

- phase-shifting transformers;
- off-nominal taps;
- multiple generators at one bus;
- reactive-limit activation;
- islands;
- near-zero impedance branches;
- high $R/X$ networks;
- stressed voltage conditions;
- voltage-dependent loads.

### 12.5 Keep numerical and physical tests separate

A regression test should distinguish:

- residual convergence;
- numerical agreement with a trusted solver;
- satisfaction of engineering limits.

That separation makes debugging much faster.

---

## 13. The broader lesson: matrix thinking is not shorthand

The deepest advantage of the matrix view is not that it makes formulas shorter.

It exposes the composition

$$
\boxed{
\text{topology}
\rightarrow
\text{device terminal laws}
\rightarrow
Y_{\mathrm{bus}}
\rightarrow
I=YV
\rightarrow
S=[V]I^*
\rightarrow
\text{residual}
\rightarrow
\text{Jacobian}
\rightarrow
\text{sparse linear solve}.
}
$$

That structure scales naturally from a derivation to software.

It also clarifies what should remain separate:

- topology versus control mode;
- physics versus numerical method;
- full equations versus reduced variables;
- analytic derivatives versus sparse assembly;
- convergence versus feasibility.

Once these distinctions are clear, many extensions become less mysterious. State estimation, optimal power flow, branch-flow sensitivities, continuation power flow, and parameter estimation all reuse parts of the same computational grammar.

The classic Newton power flow remains important not because the equations are old, but because it is an unusually clean example of how physical modeling, nonlinear analysis, sparse linear algebra, and software architecture meet in one engineering problem.

---

## References

1. W. F. Tinney and C. E. Hart, "Power Flow Solution by Newton's Method," *IEEE Transactions on Power Apparatus and Systems*, vol. PAS-86, no. 11, pp. 1449–1460, 1967. DOI: [10.1109/TPAS.1967.291823](https://doi.org/10.1109/TPAS.1967.291823).

2. W. F. Tinney and J. W. Walker, "Direct Solutions of Sparse Network Equations by Optimally Ordered Triangular Factorization," *Proceedings of the IEEE*, vol. 55, no. 11, pp. 1801–1809, 1967. DOI: [10.1109/PROC.1967.6011](https://doi.org/10.1109/PROC.1967.6011).

3. B. Stott and O. Alsac, "Fast Decoupled Load Flow," *IEEE Transactions on Power Apparatus and Systems*, vol. PAS-93, no. 3, pp. 859–869, 1974. DOI: [10.1109/TPAS.1974.293985](https://doi.org/10.1109/TPAS.1974.293985).

4. R. D. Zimmerman, "AC Power Flows, Generalized OPF Costs and their Derivatives using Complex Matrix Notation," *MATPOWER Technical Note 2*, 2010. [MATPOWER technical note](https://matpower.org/docs/TN2-OPF-Derivatives.pdf).

5. R. D. Zimmerman, C. E. Murillo-Sánchez, and R. J. Thomas, "MATPOWER: Steady-State Operations, Planning, and Analysis Tools for Power Systems Research and Education," *IEEE Transactions on Power Systems*, vol. 26, no. 1, pp. 12–19, 2011. DOI: [10.1109/TPWRS.2010.2051168](https://doi.org/10.1109/TPWRS.2010.2051168).

---

## Note on provenance

This English article is a substantial synthesis and rewrite of three earlier Chinese essays by the author:

- [重温牛顿-拉夫逊法](重温牛顿-拉夫逊法.html)
- [深入理解潮流计算](深入理解潮流计算.html)
- [矩阵思维下的潮流计算](矩阵思维下的潮流计算.html)

The earlier essays remain online because they serve a different audience and already have independent links. Historical discussion, a generic two-variable Newton example, dynamic power-flow material, product surveys, and several side topics were intentionally omitted here so that the English version stays focused on the mathematical and computational core of AC power flow.
