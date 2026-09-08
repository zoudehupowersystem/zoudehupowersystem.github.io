---
layout: article
lang: en
title: "From Ybus to an Industrial-Grade Power Flow Solver"
permalink: "/ac-power-flow-ybus-newton.html"
seo_title: "From Ybus to an Industrial-Grade Power Flow Solver | Dehu Zou"
description: "Derive AC power flow from Ybus to sparse Newton, then connect controls, limits, diagnostics, and reproducible verification to trustworthy engineering software."
updated: "2026-09-08"
---

# From Ybus to an Industrial-Grade Power Flow Solver

<p class="article-subtitle" style="font-size:1.2rem;line-height:1.55;color:#475467;">The mathematics, control logic, and verification behind trustworthy AC power flow.</p>

<div class="article-meta" style="margin:16px 0 28px;color:#667085;font-size:.9rem;display:flex;gap:8px 18px;flex-wrap:wrap;"><span>Dehu Zou</span><span>Updated September 8, 2026</span><span>Technical essay · Derivation and executable example</span></div>

A power-flow program can converge to a very small residual and still answer the wrong engineering question. It may have used the wrong transformer convention, allowed a generator to supply unavailable reactive power, or solved a control configuration different from the one the operator intended. Newton's method cannot detect those mistakes merely by converging.

The distance between a textbook calculation and a trustworthy solver is therefore not another clever iteration formula. It is the work required to make **network physics, control assumptions, numerical methods, and verification agree**.

This article follows that work from the beginning. Topology and terminal models produce a sparse admittance operator. Voltage determines current through a linear map. Complex power introduces the familiar nonlinearity. Device controls determine which equations are enforced and which variables remain free. Newton's method then produces a sequence of sparse linear systems—not a sequence of explicit matrix inverses.

The central idea is simple:

> **Ybus describes the network. Controls define the problem. The solver must make both numerically and physically accountable.**

The mathematics is classical, not a new power-flow algorithm. The contribution here is to connect the derivation to implementation decisions that are easy to miss when the subject is presented only as bus-by-bus trigonometric formulas. A small, executable example makes those connections testable.

**Reading paths.** Start with [the network and equations](#network), go directly to [the Jacobian derivation](#jacobian), inspect [the reproducible example](#example), or use [the verification and architecture sections](#verification) as an implementation review. The appendices collect scalar derivatives and extensions without interrupting the main argument.

<a id="scope"></a>

## 1. Establish the model before choosing the solver

The baseline is a **balanced, positive-sequence, steady-state AC network**, expressed in per unit. Branch parameters and discrete control settings are fixed during each inner Newton solve. Constant-power injections are the starting point; voltage-dependent loads and additional controls are introduced explicitly later.

This scope matters. A positive-sequence model does not resolve phase unbalance, neutral behavior, harmonics, or electromagnetic transients. Those applications require different or larger device and network models. The architectural principles still transfer, but the equations cannot simply be relabeled.

Let the system have $n$ buses and $\ell$ branches. Write

$$
V=m\odot e^{j\theta},\qquad m=|V|>0,
$$

where $V\in\mathbb C^n$, $m,\theta\in\mathbb R^n$, and angles are in **radians** unless explicitly stated otherwise. For a vector $a$, define $[a]=\operatorname{diag}(a)$. The symbols $\odot$ and $\oslash$ denote elementwise multiplication and division. An overbar denotes elementwise complex conjugation; $T$ denotes transpose, not conjugate transpose.

Positive bus power means **net injection into the modeled network**. With consuming demand taken as positive,

$$
S^{\mathrm{spec}}=S_g-S_d.
$$

For fixed network admittance $Y\equiv Y_{\mathrm{bus}}$,

$$
\boxed{I=YV,\qquad S^{\mathrm{calc}}(V)=[V]\overline{YV}.}
\tag{1}
$$

The network's voltage-to-current relation is linear. Constant-power boundary conditions make the voltage problem nonlinear because power multiplies voltage by conjugate current. Nonlinear loads and controls can add further dependencies.

A shunt already included in $Y$ belongs on the network side of (1). Do not also subtract its power as a separate load. For $y_{\mathrm{sh}}=g+jb$, its absorbed complex power is $m^2(g-jb)$: a capacitive shunt has negative reactive absorption. This small bookkeeping decision affects residuals, generator outputs, and reported losses simultaneously.

<a id="network"></a>

## 2. Build Ybus from local terminal laws

Network assembly has two distinct inputs: **connectivity** and **device behavior**. Keeping them separate makes the implementation both more general and easier to verify.

### 2.1 The incidence-matrix starting point

For reciprocal series branches, give each branch an arbitrary orientation and construct $D\in\mathbb R^{\ell\times n}$. Its row has $+1$ at the from bus and $-1$ at the to bus. If $y$ contains the series admittances,

$$
v_{\mathrm{br}}=DV,\qquad i_{\mathrm{br}}=[y]DV.
$$

Kirchhoff's current law then gives

$$
\boxed{Y=D^T[y]D+Y_{\mathrm{sh}}.}
\tag{2}
$$

Reversing one arbitrary branch orientation changes two signs that cancel in (2). Connectivity is not a physical direction of power flow.

Equation (2) is a useful starting point, but ordinary incidence stamping is not sufficient for general transformer models.

### 2.2 The general two-terminal stamp

For branch $k$, define currents as flowing **from each bus into the branch**:

$$
\begin{bmatrix}I_{f,k}\\I_{t,k}\end{bmatrix}
=
\begin{bmatrix}y_{ff,k}&y_{ft,k}\\y_{tf,k}&y_{tt,k}\end{bmatrix}
\begin{bmatrix}V_{f,k}\\V_{t,k}\end{bmatrix}.
\tag{3}
$$

The connection matrices $C_f,C_t\in\{0,1\}^{\ell\times n}$ select terminal voltages: $V_f=C_fV$ and $V_t=C_tV$. Collect the branch stamps into

$$
Y_f=[y_{ff}]C_f+[y_{ft}]C_t,\qquad
Y_t=[y_{tf}]C_f+[y_{tt}]C_t.
$$

The global operator is

$$
\boxed{Y=C_f^TY_f+C_t^TY_t+Y_{\mathrm{sh}}.}
\tag{4}
$$

This is the reusable pattern: local constitutive relations, connected and accumulated into a global sparse operator.

For a standard $\pi$ branch, let $y_s=1/(r+jx)$, let $b_c$ be the **total** charging susceptance, and place the complex tap $t=\tau e^{j\phi}$ at the from terminal. With the internal branch-side voltage defined as $V_f/t$,

$$
\begin{aligned}
y_{ff}&=\frac{y_s+jb_c/2}{|t|^2},
&y_{ft}&=-\frac{y_s}{\overline t},\\
y_{tf}&=-\frac{y_s}{t},
&y_{tt}&=y_s+jb_c/2.
\end{aligned}
\tag{5}
$$

This convention agrees with MATPOWER's branch assembly [6]. Stating the internal voltage relation is important: “tap ratio” alone does not specify a model.

With phase shifting, $y_{ft}$ and $y_{tf}$ need not be equal. Even without phase shifting, a complex-symmetric $Y$ is generally not Hermitian. Neither observation licenses a symmetric positive-definite solver for the real power-flow Jacobian.

Branch availability also belongs here. An out-of-service branch contributes no series or charging stamp under the fully disconnected branch model. An open terminal that leaves equipment energized is a different model and must be represented accordingly.

### 2.3 Recover the familiar power equations

Let $Y_{ij}=G_{ij}+jB_{ij}$ and $\theta_{ij}=\theta_i-\theta_j$. Expanding (1) gives

$$
\begin{aligned}
P_i&=m_i\sum_jm_j\left(G_{ij}\cos\theta_{ij}+B_{ij}\sin\theta_{ij}\right),\\
Q_i&=m_i\sum_jm_j\left(G_{ij}\sin\theta_{ij}-B_{ij}\cos\theta_{ij}\right).
\end{aligned}
\tag{6}
$$

The matrix and scalar forms are the same equations. Matrix notation exposes composition and sparsity; scalar notation remains useful for hand calculations and independent checks.

<a id="controls"></a>

## 3. Bus types are reduced control equations

A bus is a connection point. Its classification as PQ, PV, or reference is a consequence of the connected devices and the equations retained after elimination—not an immutable physical property.

For the classical local-control model:

| Mode | Prescribed quantities | Quantities determined by the solution |
|---|---|---|
| PQ | Net $P$ and $Q$ | Angle $\theta$ and magnitude $m$ |
| PV | Net $P$ and voltage magnitude $m$ | Angle $\theta$ and net $Q$ |
| Reference/slack | Angle $\theta$ and magnitude $m$ | Net $P$ and $Q$ |

At a PV bus, the generator's reactive output is not generally the net bus injection. With a local load and no other explicit injection, $Q_g=Q^{\mathrm{calc}}+Q_d$. With several devices, the allocation must follow their actual control and sharing rules.

A PV equation is valid only while sufficient regulating capability remains. A generator's reactive limit is therefore more than a number to check after convergence: it can change the equations to be solved. The classical formulation and its reduced variables are described in MATPOWER's power-flow documentation [7].

### 3.1 Why an angle reference is unavoidable

For a uniform phase rotation $V'=e^{j\gamma}V$,

$$
[V']\overline{YV'}=[V]\overline{YV}.
$$

Thus absolute angle cannot be identified from the power equations of a floating synchronous island. Differentiating this invariance gives the useful identity

$$
\boxed{S_\theta\mathbf 1=0.}
\tag{7}
$$

Each independently rotating island contributes such a direction. Fixing one angle per island removes this freedom in the classical formulation.

Notice what this argument does **not** require: $Y$ itself need not be singular. Shunts may make $Y$ invertible while the power equations still retain their uniform-angle invariance. Confusing these two singularity questions leads to misleading diagnostics.

A reference also does not create an energy source. Every energized island needs a modeled balancing mechanism and appropriate device capability. Renaming an isolated load bus “slack” silently introduces an ideal source rather than repairing the original case.

### 3.2 The reduced state and residual

Let $\mathcal A$ contain all non-reference buses, and let $\mathcal Q$ contain the PQ buses. Fix an ordering and preserve it in every residual, Jacobian, and state update:

$$
x=\begin{bmatrix}\theta_{\mathcal A}\\m_{\mathcal Q}\end{bmatrix},\qquad
F(x)=\begin{bmatrix}
P^{\mathrm{calc}}_{\mathcal A}-P^{\mathrm{spec}}_{\mathcal A}\\
Q^{\mathrm{calc}}_{\mathcal Q}-Q^{\mathrm{spec}}_{\mathcal Q}
\end{bmatrix}.
\tag{8}
$$

For one reference bus, there are $n_{\mathrm{PV}}+2n_{\mathrm{PQ}}$ equations and unknowns. The omitted balance equations have not disappeared physically: after solving, they determine the outputs of the balancing and voltage-regulating devices.

Throughout this article, **residual means calculated minus specified**. Newton therefore solves $J\Delta x=-F$. Using the opposite convention is equally valid; mixing the two is not.

<a id="jacobian"></a>

## 4. Derive the Jacobian once, in complex form

The four real Jacobian blocks follow from one product rule. The derivation below is a real differential of a complex-valued function; it does not assume holomorphic complex analysis. It is the same derivative structure documented in MATPOWER Technical Note 2 [4].

### 4.1 Differentiate voltage

Define the unit phasor $u=V\oslash m=e^{j\theta}$. Since angle perturbations move a phasor tangentially and magnitude perturbations move it radially,

$$
dV=j[V]d\theta+[u]dm,\qquad
d\overline V=-j[\overline V]d\theta+[\overline u]dm.
\tag{9}
$$

### 4.2 Differentiate complex power

For $I=YV$ with fixed $Y$,

$$
\begin{aligned}
dS
&=[dV]\overline I+[V]d\overline I\\
&=[\overline I]dV+[V]\overline Y\,d\overline V.
\end{aligned}
\tag{10}
$$

Substituting (9) yields

$$
dS=S_\theta d\theta+S_mdm,
$$

where

$$
\boxed{S_\theta=j[V]\left([\overline I]-\overline Y[\overline V]\right)}
\tag{11}
$$

and

$$
\boxed{S_m=[\overline I][u]+[V]\overline Y[\overline u].}
\tag{12}
$$

Two complex matrices now contain every polar derivative. Their real and imaginary parts give

$$
J_{\mathrm{full}}=
\begin{bmatrix}
\operatorname{Re}S_\theta&\operatorname{Re}S_m\\
\operatorname{Im}S_\theta&\operatorname{Im}S_m
\end{bmatrix}
=\begin{bmatrix}H&N\\M&L\end{bmatrix}.
\tag{13}
$$

For constant specifications, select the rows and columns associated with (8):

$$
\boxed{J=
\begin{bmatrix}
(\operatorname{Re}S_\theta)_{\mathcal A,\mathcal A}&
(\operatorname{Re}S_m)_{\mathcal A,\mathcal Q}\\
(\operatorname{Im}S_\theta)_{\mathcal Q,\mathcal A}&
(\operatorname{Im}S_m)_{\mathcal Q,\mathcal Q}
\end{bmatrix}.}
\tag{14}
$$

This is the conventional polar Newton Jacobian, not an approximation or an alternative algorithm.

### 4.3 What the notation buys—and what it does not

Equations (11)–(14) separate differentiation from indexing. That makes it possible to test the full complex derivatives before testing the reduced real system. It also exposes row and column scaling operations that can be implemented without dense diagonal matrices.

It does **not** improve convergence by itself. With identical equations, states, active sets, and exact arithmetic, equivalent scalar and matrix implementations produce the same Newton direction. In floating-point arithmetic, differences can arise from assembly, ordering, pivoting, and conditioning; near a control threshold, even small differences can alter a subsequent mode decision.

The right comparison is therefore an end-to-end comparison under matched assumptions—not a claim that vector notation has a larger convergence region.

<a id="complete-residual"></a>

## 5. Differentiate the complete residual, not just the network

The network derivatives are only part of $J$ when specified injections depend on voltage. For the selected real equations,

$$
J=\frac{\partial F}{\partial x}
=\frac{\partial S^{\mathrm{calc}}}{\partial x}
-\frac{\partial S^{\mathrm{spec}}}{\partial x},
\tag{15}
$$

with real/imaginary extraction and row selection understood. MATPOWER's `newtonpf` and `makeSbus` provide an inspectable example of including this dependency [6].

For a ZIP load at nominal magnitude $1$ p.u., write

$$
\begin{aligned}
P_d(m)&=P_0(a_Zm^2+a_Im+a_P),\\
Q_d(m)&=Q_0(b_Zm^2+b_Im+b_P),
\end{aligned}
\tag{16}
$$

where each set of coefficients sums to one. Active and reactive demand need not use the same fractions. The derivatives are

$$
\frac{dP_d}{dm}=P_0(2a_Zm+a_I),\qquad
\frac{dQ_d}{dm}=Q_0(2b_Zm+b_I).
$$

Because $F=S^{\mathrm{calc}}-S_g+S_d$, the load derivatives enter with a **plus** sign. Updating ZIP demand in the residual but omitting its derivatives gives an inexact linearization. Freezing the demand itself instead changes the model. These are different errors.

The same discipline applies to controllers. If a continuous control variable $c$ changes a tap or other network parameter so that $Y=Y(c)$, then

$$
dS=[\overline I]dV+[V]\overline Y\,d\overline V
+[V]\overline{(dY)V}.
\tag{17}
$$

The last term is absent only when $Y$ is fixed during differentiation. Additional variables also require additional control equations. Adding a “tap variable” without both its network derivative and its regulating equation does not create a complete Newton formulation.

<a id="newton"></a>

## 6. Turn the equations into a dependable Newton kernel

At iteration $k$,

$$
\boxed{J(x_k)\Delta x_k=-F(x_k),\qquad
x_{k+1}=x_k+\alpha_k\Delta x_k.}
\tag{18}
$$

Full Newton uses $\alpha_k=1$. Local quadratic convergence requires a sufficiently smooth residual, a nonsingular solution Jacobian, an adequately accurate linear solve, and an initial point sufficiently close to the solution. A change of control mode changes the local problem; the smooth fixed-mode theory does not cover arbitrary switching.

A minimal implementation should preserve the following boundaries:

```text
validate data, topology, references, and control ownership
assemble the network and establish the active control configuration

for each permitted outer control iteration:
    build or refresh state/equation maps and affected sparse structures
    initialize from a compatible previous state

    for each permitted Newton iteration:
        evaluate the complete residual F
        reject non-finite values
        if residual tolerances are satisfied:
            finish the inner solve

        assemble J = dF/dx
        solve J dx = -F using a sparse linear solver
        choose an acceptable step length
        update free variables; preserve prescribed quantities

    if the inner solve failed:
        invoke a defined recovery policy or return a classified failure

    recover device outputs and evaluate control/limit consistency
    if no control change is required:
        compute flows, check operating limits, and return the result
    apply a permitted mode or discrete-control change; invalidate affected caches

return a control-iteration-limit or cycling diagnostic
```

The distinction between an **inner numerical solve** and an **outer control decision** prevents an incomplete Newton iterate from being mistaken for a physically settled operating point.

### 6.1 Globalization, scaling, and termination

A practical safeguard is backtracking on a merit function

$$
\psi(x)=\tfrac12\|WF(x)\|_2^2,
$$

where $W$ is a fixed positive diagonal residual scaling for the current solve. An Armijo-style rule seeks a sufficient reduction while keeping trial voltages within the mathematical domain. For the exact Newton direction,

$$
\nabla\psi(x)^T\Delta x=-\|WF(x)\|_2^2.
$$

This gives a principled step-selection test, not a guarantee that a feasible operating point will be found. Scaling, line searches, and distinct residual/step termination tests are established nonlinear-solver practices [9].

A positive lower safeguard on a polar voltage magnitude is a numerical domain restriction. It is not the same as enforcing an operational lower voltage limit. Likewise, clipping a Newton iterate to engineering limits generally changes neither the equations nor the controls in a consistent way.

For power-balance equations, report the mismatch in p.u. on a stated system base and, where useful, convert it to MW/MVAr. Additional controller equations need appropriate scales and tolerances of their own. A small correction with a large residual is **stagnation**, not convergence.

A warm start should preserve prescribed reference angles and regulating magnitudes. A “flat start” normally means zero initial unknown angles and near-unit **free** magnitudes—not overwriting a specified 1.04 p.u. voltage with 1.00 p.u.

### 6.2 Sparse linear algebra is part of the method

Tinney and Hart's Newton power-flow work, together with Tinney and Walker's sparse-factorization work, established the importance of sparse elimination and ordering in practical network computation [1,2]. The lesson remains operational: **solve a sparse system; do not form its inverse**.

For a general power-flow Jacobian, sparse LU is a natural direct-solver baseline. The expression $[V]\overline Y[\overline u]$ means row and column scaling; a dense $n\times n$ diagonal matrix is unnecessary. Assemble into a stable sparse pattern and exploit reusable workspaces.

Three kinds of reuse must not be confused:

| Object | When reuse is justified | What invalidates it |
|---|---|---|
| Network matrices | Same connected network and admittance parameters | Outages, tap changes, shunt changes, parameter changes |
| State maps, sparse pattern, symbolic analysis | Same equation/variable structure and compatible backend assumptions | Bus-mode changes, new control couplings, structural topology changes |
| Numerical factors | Same numerical matrix, possibly with several right-hand sides | A changed Jacobian, unless deliberately using a modified-Newton strategy |

A fixed network usually permits extensive structural reuse, but **ordinary full Newton still updates and numerically factors its Jacobian**. Whether symbolic analysis can be retained separately depends on the chosen backend. The small Python companion uses SciPy's `splu`; it is not an implementation of a persistent symbolic-factorization cache [10].

For a large workload, measure preprocessing, assembly, factorization, solve time, control iterations, and memory separately. Bus count alone is a weak performance descriptor: fill-in, topology, controls, and scenario reuse also matter. Neither “vectorized” nor “GPU-accelerated” is evidence of speed without a defined workload and measurements.

<a id="limits"></a>

## 7. Limits change equations; balancing needs an explicit policy

### 7.1 Reactive limits are an active-set problem

Suppose a voltage-regulating generator requires $Q_g>Q_g^{\max}$. Continuing to enforce $m=m^\star$ while clipping $Q_g$ generally makes the model inconsistent. In the classical single-regulator case, the correct transition is

$$
m=m^\star\quad\longrightarrow\quad Q_g=Q_g^{\max},
\tag{19}
$$

with voltage magnitude becoming a free variable. This is PV-to-PQ switching. The required reactive-power balance is then included in the inner solve. A corresponding outer-loop implementation is described in MATPOWER's documentation [7].

The single-regulator qualification is important. If several devices regulate the same bus, one device reaching a limit need not release bus-voltage control. Remaining devices may absorb the additional requirement within their capabilities. The program needs a constrained sharing rule, a consistent voltage target, and explicit ownership of the controlled quantity.

Return from a limited mode also needs a policy. Use declared tolerances, a release criterion, and safeguards against cycling; do not let floating-point noise toggle modes indefinitely. Capability curves or converter current limits may depend on active power and voltage, so a rectangular $Q_{\min}/Q_{\max}$ interval is not always an adequate device model.

### 7.2 Separate the angle reference from active-power balancing

A conventional slack bus bundles two roles: fixing the angular coordinate and providing unspecified active power. These roles can be separated.

For one island, let bus-aggregated participation factors satisfy $\alpha_i\ge0$ and $\sum_i\alpha_i=1$. Introduce a balancing variable $\Delta P_b$:

$$
P_{g,i}=P_{g,i}^{0}+\alpha_i\Delta P_b.
\tag{20}
$$

Retain **all** active-power balance equations, including the reference-bus equation, while fixing one angle. The active residual is

$$
F_P=P^{\mathrm{calc}}-P_g^0-\alpha\Delta P_b+P_d,
$$

so its additional Jacobian column is $-\alpha$. The extra unknown and the restored balance equation preserve the equation count. For multiple islands, the construction must provide independent balancing variables and participation policies where appropriate.

Active-power limits can force participation changes or a redispatch. Post-solve clipping does not rebalance the network. The same principle applies when a reference generator reaches a reactive limit: angle anchoring must remain valid, but its voltage-regulating role need not remain unchanged.

### 7.3 Discrete controllers need coordination, not hidden relaxation

Tap changers and switched shunts may have discrete positions, deadbands, priorities, and limits. A continuous relaxation can be useful, but it is not the original discrete-control problem. If a relaxed solution is rounded, the network must be solved again and all affected checks repeated.

For an outer control loop, record what changed, why it changed, and which equations or matrix values it invalidated. A bounded sequence of explicit decisions is diagnosable. An uncontrolled mixture of Newton steps, tap jumps, and PV/PQ switches is not.

<a id="flows"></a>

## 8. Recover branch flows without changing conventions

With the terminal currents and voltages from Section 2,

$$
\boxed{S_f=[C_fV]\overline{Y_fV},\qquad
S_t=[C_tV]\overline{Y_tV}.}
\tag{21}
$$

Both powers are positive **into** the branch. Hence $S_f+S_t$ is its net complex absorption. For a passive branch with nonnegative resistance, the real part represents active loss. The reactive part can be negative when charging supplies more reactive power than the series element absorbs. Calling every component a nonnegative “loss” obscures this distinction.

When bus shunts are stored separately from branch charging, the model obeys

$$
\boxed{
\sum_iS_i^{\mathrm{calc}}
=\sum_k(S_{f,k}+S_{t,k})
+\sum_i|V_i|^2\overline{y_{\mathrm{sh},i}}.
}
\tag{22}
$$

This identity holds for any voltage vector, not only a converged solution. It is an excellent assembly and post-processing check—but not independent evidence that demand, generation, or equipment data are correct.

<a id="example"></a>

## 9. A reproducible three-bus example

A useful verification case should be small enough to inspect and rich enough to expose mistakes. The following **synthetic example** includes a PV bus, a PQ bus, line charging, an off-nominal tap, and a phase shift. It is not an IEEE benchmark or a performance claim.

Use a 100 MVA system base, no separate bus shunts, and the branch convention in (5). All impedances and susceptances are in p.u.; the listed phase shift is in degrees.

| From–to | $r$ | $x$ | Total $b_c$ | $\tau$ | $\phi$ |
|---|---:|---:|---:|---:|---:|
| 1–2 | 0.020 | 0.060 | 0.030 | 1.020 | $4^\circ$ |
| 1–3 | 0.080 | 0.240 | 0.025 | 1.000 | $0^\circ$ |
| 2–3 | 0.060 | 0.180 | 0.020 | 1.000 | $0^\circ$ |

Bus 1 is the reference at $1.04\angle0^\circ$. Bus 2 injects $P_2=0.50$ and regulates $m_2=1.02$, with no local load. Bus 3 consumes $0.90+j0.35$, so its specified injection is $-0.90-j0.35$. Initialize

$$
V^{(0)}=\begin{bmatrix}1.04&1.02&1.00\end{bmatrix}^T.
$$

With state ordering $x=[\theta_2,\theta_3,m_3]^T$, the companion's sparse Newton solve gives:

| Bus | $m$ (p.u.) | Angle (degrees) | Net $P$ (p.u.) | Net $Q$ (p.u.) |
|---|---:|---:|---:|---:|
| 1 | 1.040000000 | 0.000000000 | 0.437912108 | 0.207635287 |
| 2 | 1.020000000 | −3.572405502 | 0.500000000 | 0.180374183 |
| 3 | 0.956912891 | −6.763479175 | −0.900000000 | −0.350000000 |

The maximum absolute residual, including the initial point, was

```text
Newton step       ||F||_infinity (p.u.)
0                 8.1666666667e-01
1                 4.1857352040e-02
2                 3.1060632124e-04
3                 1.8586325479e-08
4                 1.8873791419e-15
```

The stopping tolerance was $10^{-11}$ p.u. The final residual below that threshold is an observed result, not a recommendation to demand machine-precision residuals in operational studies. The run used Python 3.13.5, NumPy 2.3.5, and SciPy 1.17.0; last-bit results can vary across environments.

Total active branch loss is $0.037912108$ p.u., or approximately **3.79121 MW**. Power on branch 1–2 flows opposite to its assigned orientation at the from terminal: $P_{f,12}\approx-0.118275080$ p.u. This is a useful reminder that from/to labels define bookkeeping, not the physical direction of transfer.

### 9.1 Activate a limit and solve a different problem

The unrestricted PV solution requires $Q_{g,2}\approx0.180374183$ p.u. Now impose $Q_{g,2}^{\max}=0.10$ p.u. With no other regulator at bus 2, release its voltage target and impose its reactive injection. The re-solved state has

$$
m_2=1.015831801,\qquad m_3=0.954331971,
$$

and $Q_{g,2}=0.10$ p.u. to the solve tolerance. The additional solve takes three Newton updates from the previous operating point.

Clipping the original reported $Q_{g,2}$ to 0.10 while retaining the original voltages would leave a reactive mismatch of approximately $0.080374183$ p.u.—about **8.03742 MVAr**. The numbers make the modeling issue concrete: a limit is not enforced until the equations and the resulting state agree.

### 9.2 What was actually checked

The [Python companion](assets/code/power_flow_reference.py) executes the case and checks the Jacobian, angle invariance, branch/bus power consistency, bus renumbering, ZIP-load derivatives, shunts, parallel branches, and rejection of an unreferenced island. It also compares with a second residual implementation based directly on terminal currents, solved using SciPy's hybrid root method without the analytic Jacobian [10].

For this run, the best centered-difference directional Jacobian error was approximately $1.64\times10^{-11}$ in the relative metric defined below. The two nonlinear-solution paths differed by less than $10^{-12}$ p.u. in complex voltage, and the complex-power balance discrepancy was below $10^{-12}$ p.u. Full-precision values and the environment are in the [verification record](assets/code/power-flow-verification-results.json).

These are implementation checks on a small case. They are **not** external validation of the physical model, broad robustness evidence, or a large-network benchmark. A [MATPOWER case](assets/code/case3_zou.m) and [comparison script](assets/code/check_case3_zou.m) are supplied for external reproduction; that MATLAB/Octave comparison was not executed for the results reported here.

Use the accompanying [tested dependency versions](assets/code/requirements-tested.txt), then run the example:

```bash
python -m pip install -r requirements-tested.txt
python power_flow_reference.py --json results.json
```

<a id="robustness"></a>

## 10. Distinguish nonconvergence, infeasibility, and instability

An unsuccessful Newton run establishes that this algorithm, initialization, and control sequence did not produce an accepted solution. It does not, by itself, prove that the modeled equations have no solution.

Before interpreting nonconvergence physically, examine topology, units, setpoints, references, scaling, derivatives, and control consistency. A near-zero series impedance can produce extreme admittances; replacing it by an arbitrary “small” impedance changes the case. Ideal switches may justify bus merging, while ideal transformers or other constraints may require a different treatment. There is no universal merge rule for all low-impedance equipment.

A high $R/X$ ratio is especially problematic for decoupling assumptions; it is not, on its own, a diagnosis that full Newton cannot solve a network. Initialization, operating stress, model formulation, and numerical conditioning need to be assessed separately.

Near a generic saddle-node of a fixed-mode power-flow problem, the relevant reduced Jacobian becomes singular. Continuation power flow augments the problem with a loading parameter and a path-following condition so that a regular solution curve can be traced through an ordinary fold [8]. The loading direction, balancing policy, and treatment of control limits are part of that analysis. A large condition number alone is not a voltage-stability certificate: it depends on scaling and may also reflect modeling or data problems.

After a solve, keep four questions distinct:

| Question | Evidence required |
|---|---|
| Did the equations converge? | Residuals meet declared numerical tolerances. |
| Are the control modes consistent? | Prescribed quantities, limits, and mode-selection rules agree with recovered outputs. |
| Is the operating point acceptable? | Relevant voltage, thermal, generation, and equipment constraints pass their checks. |
| Is the system dynamically stable? | A suitable dynamic model and stability analysis support that conclusion. |

A power flow can converge with a thermal overload. It can also converge at an equilibrium whose dynamic stability has not been assessed. “Converged,” “acceptable,” and “stable” should never be interchangeable status labels.

### Where fast-decoupled and DC power flow fit

Fast-decoupled power flow exploits regimes where $P$–$\theta$ and $Q$–$m$ couplings dominate the cross-couplings, typically in predominantly inductive transmission networks with moderate angle differences and near-nominal voltages. It uses simplified fixed matrices that can be factored once for a fixed configuration [3]. It still iterates toward AC mismatch equations; its approximations concern the update strategy, not a claim that reactive power disappears.

DC power flow instead approximates the model itself: it retains a linear active-power/angle relation while omitting reactive-power and voltage-magnitude behavior. Transformer taps and phase shifts still require consistent treatment. A successful DC solution does not establish AC voltage or reactive feasibility.

The two methods are useful for different reasons. Their value comes from matching an approximation to the study—not from being universally faster or more reliable substitutes for full AC analysis.

<a id="verification"></a>

## 11. Make verification part of the solver, not its final demonstration

The three-bus example illustrates a verification process. A defensible codebase turns that process into a permanent test system.

### 11.1 Test derivatives with the active set frozen

For a normalized real direction $p$, compare $J(x)p$ with

$$
d_h=\frac{F(x+hp)-F(x-hp)}{2h},\qquad
\varepsilon(h)=\frac{\|d_h-Jp\|_\infty}{\max(1,\|Jp\|_\infty)}.
\tag{23}
$$

Sweep $h$ over several orders of magnitude. For a smooth residual, a centered difference exhibits a truncation-error region before floating-point cancellation takes over. One arbitrary step size is a weaker test than the error trend.

Freeze discrete states, bus classifications, and active constraints during the perturbation. Otherwise the test crosses between different residual functions and no longer checks the advertised fixed-mode Jacobian. Include voltage-dependent specifications in both the analytic and perturbed evaluations.

Do not apply the standard complex-step recipe blindly to a black-box implementation containing conjugation, absolute values, and real/imaginary extraction. Those operations do not provide the holomorphic extension that recipe assumes. Centered differences in real state variables, or automatic differentiation of an explicitly real computational graph, avoid that ambiguity.

### 11.2 Test identities and model boundaries

Use the angle-invariance identity (7), terminal-current assembly, and the power identity (22). Include cases with reversed branch descriptions under correctly transformed parameters, parallel branches, phase shifters, shunts, and bus permutations. Exercise invalid data and island detection before testing elaborate nonlinear recovery strategies.

These tests should be layered. Recomputing branch powers from the same incorrect stamp can satisfy a global balance identity perfectly. A separately implemented terminal relation, hand-checkable cases, and an external solver each help address different shared-error risks.

### 11.3 Compare like with like

MATPOWER is a useful open reference [5–7]. Before comparing results, align bases, transformer conventions, load models, slack participation, voltage targets, limits, and controller settings. Align the angle reference independently within each island. Compare branch flows, generator outputs, and final control modes—not only bus-voltage magnitudes.

A discrepancy between two packages is not automatically a numerical bug. Different defaults may define different problems. Record both configurations before interpreting the difference.

### 11.4 Publish the limits of the evidence

A regression corpus should span ordinary, stressed, mode-switching, disconnected, and intentionally invalid cases. For performance studies, state the hardware, software versions, tolerances, initialization, model features, warm/cold-start policy, and timing boundary. Report failures and fallback usage alongside successful runtimes.

Passing public transmission cases does not establish correctness for unbalanced distribution controls or converter-specific limits. Verification claims should be no broader than the tested model and workload.

<a id="architecture"></a>

## 12. Industrial-grade implementation: features, principles, and architecture

The derivation above is enough to build a correct Newton kernel. It is **not** enough to build an industrial power-flow program.

In production work, the solver is only one layer in a larger numerical system. The program must decide what equations are active, reject or repair invalid network representations before iteration, coordinate continuous and discrete controls, preserve sparse structure, explain failure, recover all reported quantities from the same model, and remain verifiable as the codebase evolves. A solver that is fast but opaque is difficult to trust; a solver that is mathematically elegant but fragile under real data is difficult to use.

For this article, *industrial-grade* means a program designed around the following properties:

| Property | Concrete requirement | Typical failure when omitted |
|---|---|---|
| Model fidelity | Device equations, controls, limits, and mode transitions match the declared study scope. | The program converges to the wrong engineering problem. |
| Data integrity | Topology, bases, status, references, and parameters are validated before nonlinear iteration. | Singular systems, implausible flows, or failures misdiagnosed as “Newton problems.” |
| Numerical robustness | The nonlinear method has warm starts, safeguards, bounded recovery policies, and classified termination. | Easy cases solve; stressed or imperfect cases fail unpredictably. |
| Sparse performance | Assembly, ordering, factorization, memory, and structural reuse are engineered as first-class subsystems. | Runtime and memory scale poorly even though the equations are sparse. |
| Control coordination | Limits and discrete devices are handled by explicit state machines or active-set logic. | Chattering, contradictory controls, or post-solve clipping that violates the equations. |
| Diagnostics | Every solve exposes residuals, mode changes, limiting devices, factorization status, and reason for termination. | Engineers receive only “did not converge.” |
| Verification | Derivatives, identities, benchmark comparisons, regression cases, and failure behavior are continuously tested. | Refactors silently change results or break rare control modes. |
| Reproducibility | Results carry model/options/version provenance and deterministic policies where practical. | A result cannot be reconstructed or audited later. |
| Extensibility | Data, physics, controls, nonlinear strategy, linear algebra, and reporting are separated by stable interfaces. | Adding one device model forces changes throughout the solver. |

These are not cosmetic software qualities. Each one changes whether the final voltage vector is defensible.

### 12.1 Three levels of power-flow implementation maturity

Programs that solve the same Newton equations can still differ radically in engineering quality. A useful maturity model has three levels. The boundaries are not absolute, but the distinction is valuable because it separates *knowing the equations* from *engineering a sustainable numerical product*.

| Level | Typical implementation | What it gets right | Where it reaches its limit |
|---|---|---|---|
| I. Formula translation | Bus-by-bus loops that mirror textbook equations; often dense or only lightly optimized. | Excellent for learning, independent checks, and small prototypes. | Jacobian code becomes repetitive; sparse structure, controls, diagnostics, and large workloads are secondary. |
| II. Traditional industrialization | Custom sparse storage, ordering, factorization interfaces, extensive special-case control logic, and many performance-oriented code paths. | Can be fast, feature-rich, and proven on real networks. | Physics, sparse kernels, control state, and application data easily become entangled; maintenance cost grows rapidly as features accumulate. |
| III. Modern industrial architecture | The application layer expresses topology, devices, controls, residuals, derivatives, and sparse structure; mature numerical libraries execute generic linear-algebra kernels behind replaceable interfaces. | Preserves industrial performance while making models, solvers, controls, and backends independently testable and evolvable. | Requires disciplined abstractions, explicit cache dependencies, and strong regression tests; abstraction without measurement can still waste performance. |

The third level is not a return to a classroom script, nor does it mean that every operation should literally be written as one high-level matrix expression. It means that the program should avoid reimplementing generic numerical machinery when a mature library can do it better, while keeping domain-specific work—network stamping, equation selection, limit logic, controller coordination, diagnostics—in explicit engineering code.

This is where **matrix thinking** becomes a software principle rather than a notation preference. The application code should translate the power-system problem into algebraic objects that optimized kernels understand: sparse matrices, index maps, residual vectors, block structures, factorizations, and batched right-hand sides. In a C++ implementation, for example, modern language mechanisms can be used to pass residual evaluators, device contributions, callbacks, or policies without forcing every module to know every other module. The exact mechanism is secondary; reducing unnecessary coupling is the point.

The distinction also corrects a common misconception. Rewriting the same Jacobian with matrix expressions does **not** enlarge Newton's mathematical convergence region. Its engineering advantages are different: clearer structure, fewer hand-coded element formulas, easier derivative testing, better access to high-performance sparse libraries, and a more maintainable path from derivation to implementation. Specialized kernels, loop-level optimization, SIMD, or GPU code may still be appropriate underneath that architecture when measurement justifies them.

For a flagship industrial solver, the target is therefore not merely Level II—"many optimized lines of code"—but Level III: **a compact and explicit domain model driving replaceable high-performance numerical machinery, with every control transition and cache dependency visible.** The remaining subsections make that statement concrete.

### 12.2 Model coverage must follow control semantics

A production program needs more than lines, transformers, constant-power loads, and ideal PV generators. It must represent the steady-state behavior that materially changes the solved operating point for the intended application. Depending on scope, that can include:

- transmission lines with charging and explicit terminal status;
- off-nominal and phase-shifting transformers;
- bus shunts and switched shunts;
- multiple generators at one bus;
- generator reactive capability and active-power limits;
- local and remote voltage regulation;
- reactive-power sharing among regulating devices;
- distributed active-power balancing;
- tap-changing transformers with deadbands and discrete positions;
- ZIP or other voltage-dependent demand models;
- HVDC, FACTS, and inverter-based resources when their controls matter to the study.

The important design principle is not to accumulate device types as special cases. A device model should make its **equations, unknowns, controlled quantities, free quantities, limits, derivatives, and allowed mode transitions** explicit.

For example, a regulating generator should not merely carry a flag named `PV`. Its model should establish which voltage is controlled, what active power is prescribed, how required reactive power is recovered, what capability is available, how sharing works if several devices regulate the same quantity, and what happens when the active set changes. The classical PV bus is then a reduced consequence of those rules.

This becomes essential when controls interact. Two devices cannot independently enforce inconsistent targets on the same controlled variable. A remote-voltage controller, a local generator AVR abstraction, an LTC, and a switched shunt may all influence one voltage region. The program therefore needs explicit **control ownership, coordination, priority, and conflict resolution** rather than relying on whichever object happens to update first.

A useful internal contract for each device family is conceptually:

```text
network_contribution(state, mode)       -> sparse stamps / injections
residual_contribution(state, mode)      -> equations
jacobian_contribution(state, mode)      -> derivatives
recover_outputs(solution, mode)         -> P, Q, currents, flows, reserves
check_limits(solution, mode)            -> margins / violations
propose_transition(solution, mode)      -> optional next mode
structural_dependencies(mode)           -> what caches become invalid
```

The exact API can differ. The principle should not: the physics object describes physics and control semantics; the nonlinear solver should not invent them implicitly.

### 12.3 Network preprocessing is part of the numerical method

Many apparent convergence failures are model failures that occur before the first Newton step. A production implementation should therefore treat validation and preprocessing as part of the solver pipeline, not as optional input hygiene.

At minimum, preprocessing should establish:

1. **Per-unit consistency.** Convert equipment data through one controlled base-conversion path. MVA base, nominal voltage, transformer-side bases, shunt conventions, and load/generation signs must be unambiguous.
2. **Connectivity and islands.** Determine energized components from actual status. Every independently rotating energized island needs an angular reference and a modeled balancing mechanism appropriate to the study.
3. **Stable internal indexing.** External bus numbers, database keys, UUIDs, or CIM identifiers belong to the data layer. Numerical kernels should use compact internal indices with reversible mappings.
4. **Terminal consistency.** Transformer orientation, tap side, phase-shift sign, charging allocation, and from/to definitions must agree with the branch stamp used in both the solve and post-processing.
5. **Parameter sanity.** Detect non-finite values, contradictory limits, invalid tap positions, impossible voltage targets, duplicate equipment, disconnected controllers, and other obviously malformed inputs.
6. **Zero- and near-zero-impedance treatment.** Do not hide extreme admittances behind arbitrary epsilon impedances. Depending on the physical device and application, bus merging, explicit constraints, topology reduction, or controlled regularization may be appropriate.
7. **Reference and control ownership.** Identify missing or conflicting controls before constructing the reduced equation set.

The output of preprocessing should be an internally consistent **network snapshot**: topology, active equipment, normalized parameters, control configuration, state/equation maps, and cache-validity metadata. The inner Newton solve should operate on that snapshot rather than continuously reading mutable application data.

This separation matters in EMS, contingency, and time-series environments where topology can change while other processes are running. A numerical solve should have a defined model version. Otherwise a case can begin with one topology and end with another without any mathematical meaning.

### 12.4 State maps and active sets should be explicit objects

In small teaching programs, arrays named `pv`, `pq`, and `ref` are sufficient. In a large solver, those arrays are consequences of a richer active control configuration and should be treated as derived state.

For every inner solve, construct explicit mappings for:

- free state variables;
- enforced residual equations;
- prescribed variables;
- active limits;
- balancing variables and participation factors;
- controller equations;
- device outputs that will be recovered after convergence.

A mode transition may change only numerical values, or it may change the equation structure. Those two cases must be distinguished because they invalidate different caches. For example, changing a continuous transformer tap value changes network coefficients; converting a PV bus to PQ changes the reduced state/equation map; opening a branch can change both topology and sparsity.

The program should therefore avoid hidden global state such as a mutable “bus type” table that is modified from many subsystems. A better pattern is a versioned control/active-set object whose transitions are explicit and logged.

### 12.5 Robustness requires a nonlinear-solver hierarchy

Full Newton with an accurate Jacobian is an excellent default. Industrial robustness comes from defining what happens when that default is not enough.

A practical hierarchy can include:

1. a warm start from the previous solved state, state estimator, or nearby scenario;
2. conventional full-step Newton;
3. damping or line search when the full step does not provide acceptable progress;
4. scaling and stagnation checks when residual and correction behavior disagree;
5. controlled active-set updates when limits become binding;
6. continuation, homotopy, or a supported formulation change for difficult but important cases;
7. a classified failure when the permitted recovery budget is exhausted.

The hierarchy should be **bounded and deterministic enough to diagnose**. A production program should know which path solved the case. “Converged in 14 iterations” is less informative than “four Newton steps, one reactive-limit transition, three Newton steps, accepted.”

Termination also needs more than one scalar test. Useful evidence includes:

- maximum and scaled residual norms;
- state-correction norms;
- non-finite-value checks;
- line-search step length or damping factor;
- linear-solver status;
- iteration and outer-control budgets;
- stagnation or cycling detection.

A tiny step with a large residual is not convergence. A small power mismatch while a controller equation remains violated is not convergence. A numerically converged fixed-mode solution whose recovered device output violates the active-set assumptions is not the final operating point.

Most importantly, failure of this hierarchy does **not** automatically prove infeasibility. The failure status should say what the numerical process established and what it did not.

### 12.6 Sparse linear algebra is a first-class subsystem

For large AC networks, the dominant cost is frequently sparse factorization rather than evaluation of the scalar power equations. The linear-algebra layer therefore deserves an explicit design, performance model, and diagnostics.

A serious implementation should address:

- compressed sparse storage and deterministic nonzero assembly;
- preallocation or stable insertion patterns rather than repeated dynamic allocation;
- fill-reducing ordering such as an appropriate AMD/COLAMD-style strategy supported by the backend;
- distinction between sparsity-pattern analysis, numerical factorization, and triangular solves;
- numerical pivoting and singularity reporting;
- efficient row/column scaling instead of materializing dense diagonal matrices;
- reuse of state maps and symbolic structure while their validity conditions hold;
- workspace and memory reuse across iterations;
- multiple right-hand sides when sensitivities or related solves can reuse one factorization;
- instrumentation of factorization time, fill-in, memory, and solve time.

The cache hierarchy should be explicit. A useful mental model is:

| Cached object | Reusable when | Invalidated by |
|---|---|---|
| Normalized equipment data | Same source data and base assumptions | Parameter or base change |
| Topology / connection maps | Same energized connectivity | Outage, switching, bus merge/split |
| $Y$, $Y_f$, $Y_t$ numerical values | Same topology and admittance/control parameters | Tap, phase shift, shunt, status, impedance changes |
| State/equation maps | Same active control structure | PV/PQ or other mode changes, added/removed equations |
| Sparse pattern / ordering | Same structural nonzero graph and backend assumptions | Structural topology or control-coupling change |
| Numerical factorization | Same numerical Jacobian | Ordinary Newton update changes $J$ |
| Warm-start state | Compatible topology/control variables | Incompatible islanding or variable-set change |

This table prevents a common optimization mistake: treating every form of reuse as “reuse the Jacobian.” In ordinary full Newton, the numerical Jacobian changes. The performance opportunity is often to reuse **everything around** the changing numerical values.

Hardware acceleration should be justified by workload measurements. Sparse factorization has irregular memory access and synchronization costs; transfer overhead and small/medium case sizes can dominate. A GPU label is not an industrial performance argument. Throughput, latency, memory footprint, robustness, and scenario reuse are.

### 12.7 Limits and discrete controls need explicit state machines

Reactive limits, active-power limits, tap positions, switched shunts, converter modes, and controller deadbands introduce nonsmooth or discrete behavior around the smooth Newton solve. Industrial software should make these transitions visible.

A useful outer-loop pattern is:

```text
solve the current smooth active set
recover controlled-device outputs
measure violations and control errors
rank permitted actions by declared policy
apply a bounded set of state transitions
invalidate exactly the affected structures
re-solve from a compatible warm start
stop when controls are settled or a control failure is classified
```

For reactive limits, this includes the PV-to-PQ logic discussed in Section 7, but a production implementation must also handle multiple regulators, capability curves, sharing, release criteria, and possible return from a limited state.

For discrete controllers, define:

- deadbands and measurement quantities;
- discrete step sizes and bounds;
- control priority and ownership;
- whether several moves may occur per outer iteration;
- hysteresis or lockout rules;
- maximum move counts;
- oscillation/cycling detection;
- deterministic tie-breaking where several actions are equally eligible.

A controller event should be logged as an engineering decision, for example:

```text
outer=3  device=T17  action=tap  1.0125 -> 1.01875
reason=remote_bus_402_voltage_below_deadband
invalidated=Ybus_numeric,jacobian_numeric
```

That level of traceability is far more useful than discovering after the fact that a sparse matrix changed “somewhere in the loop.”

### 12.8 Engineer for workloads, not only for one solved case

Industrial applications rarely solve one isolated base case. They solve families of related cases:

- N-1 and N-k contingencies;
- hourly or sub-hourly time-series studies;
- dispatch and market scenarios;
- security assessment batches;
- parameter sweeps;
- Monte Carlo or probabilistic studies;
- repeated initialization of downstream dynamic simulations.

For these workloads, the key optimization is often **structural reuse across solves**. Keep topology products, internal mappings, sparse patterns, orderings, and compatible warm starts as long as their validity rules permit. Rebuild only what changed.

Independent scenarios can often run in parallel, but the numerical core must then avoid mutable global scratch state and nondeterministic control ownership. Thread safety and reproducibility are architecture properties, not afterthoughts.

Benchmark the whole pipeline. Useful measurements include:

- preprocessing time;
- residual/Jacobian assembly time;
- sparse analysis/factorization/solve time;
- number of Newton and outer-control iterations;
- number and type of active-set transitions;
- peak memory and factor fill;
- cold-start versus warm-start performance;
- success/fallback rates;
- throughput and tail latency for the actual scenario distribution.

A benchmark that reports only “milliseconds per Newton iteration” can miss the dominant cost of topology processing, controls, retries, or repeated sparse analysis.

### 12.9 Diagnostics are part of the product

A mature solver should be able to explain both success and failure to an engineer who did not write the numerical kernel.

During iteration, retain enough information to answer:

- Which buses currently have the largest active and reactive mismatches?
- Are residuals decreasing, stagnating, or oscillating?
- What is the largest voltage/angle correction?
- Was the Newton step damped, and why?
- Did sparse factorization report singularity, severe pivoting, or another warning?
- Which generators, taps, shunts, or converters are at limits?
- Which control modes changed, in what order, and for what reason?
- Which island/reference/balancing policy is active?

Useful termination classes are more specific than `success=false`:

| Class | Meaning |
|---|---|
| `INVALID_MODEL` | Input or preprocessing checks found a case the solver is not permitted to interpret. |
| `MISSING_REFERENCE_OR_BALANCE` | An energized island lacks required reference/balancing support. |
| `NONFINITE_EVALUATION` | Residual or derivative evaluation produced NaN/Inf. |
| `LINEAR_SOLVE_FAILURE` | The Jacobian factorization/solve failed or was judged unusable. |
| `GLOBALIZATION_FAILURE` | No acceptable safeguarded step was found under the configured policy. |
| `NEWTON_ITERATION_LIMIT` | The smooth active set did not converge within its budget. |
| `CONTROL_CYCLING` | Discrete/active-set transitions repeated without settling. |
| `CONTROL_ITERATION_LIMIT` | The outer control policy exhausted its move/iteration budget. |
| `SOLVED_WITH_VIOLATIONS` | Equations and control modes settled, but engineering operating limits remain violated. |
| `SOLVED` | Numerical and control acceptance criteria were satisfied; separate downstream criteria may still apply. |

The precise names are implementation choices. The distinction is the important part. A factorization failure, a control cycle, and an engineering overload are not the same event and should not be collapsed into “power flow did not converge.”

Condition estimates or pivot statistics can be valuable diagnostic evidence, but they should not be over-interpreted. Poor conditioning can result from scaling, data, formulation, or actual proximity to a solvability boundary. The program should report evidence before asserting a physical cause.

### 12.10 Post-processing must use the same model as the solve

Once the voltage state is accepted, the program still has substantial work to do. It should recover, from the same terminal conventions and active control configuration:

- branch terminal currents and complex powers;
- active and reactive losses/absorptions;
- generator outputs implied by reference, PV, distributed-slack, or other controls;
- reactive reserves and capability margins;
- final transformer taps, shunt steps, and controller states;
- bus-voltage and branch-loading violations;
- island active/reactive balances;
- selected sensitivities required by downstream applications.

Do not use one transformer convention in $Y_{\mathrm{bus}}$ and another in the reporting layer. Do not compute a generator's reactive output from a bus injection without subtracting local load and other devices according to the same aggregation rules used in the residual. Post-processing inconsistency can make a converged voltage solution appear physically contradictory.

Acceptance should therefore be layered. A result object can distinguish:

```text
numerical_converged = true/false
controls_settled    = true/false
model_consistent    = true/false
operating_acceptable= true/false
```

These flags are more informative than a single Boolean because a solved power flow can still contain an overload or voltage violation, and a physically unacceptable operating point is not the same as a failed nonlinear solve.

### 12.11 Verification must be continuous and release-oriented

Section 11 described derivative and cross-solver tests. In an industrial codebase, those checks become a release discipline.

Maintain a regression corpus containing:

- tiny hand-checkable networks;
- public benchmark cases where licensing permits;
- phase shifters and off-nominal taps;
- multiple generators and shared controls;
- reactive-limit activation and release;
- distributed balancing;
- discrete taps and shunts;
- islands and intentionally missing references;
- near-zero-impedance equipment under the supported preprocessing policy;
- high-$R/X$ and stressed cases;
- voltage-dependent loads;
- historical cases that previously exposed defects;
- intentionally invalid or unsolved cases whose **failure classification** is itself part of the expected result.

Regression should compare more than the final $V$: bus injections, branch terminal flows, losses, device outputs, active control modes, event sequence where deterministic, iteration/fallback metadata, and failure class all matter.

Numerical tolerances should be chosen with awareness of sparse backend and platform variation. Reproducibility does not require pretending that every last floating-point bit is invariant; it requires defining which quantities and decisions are expected to remain stable and investigating deviations that exceed those bounds.

Every performance claim should also be reproducible: case set, hardware, software versions, tolerances, initialization, enabled controls, warm/cold state, parallelism, and timing boundary belong with the number.

### 12.12 Architecture should make invalid coupling difficult

A maintainable solver separates the major responsibilities strongly enough that one layer cannot silently redefine another. One possible decomposition is:

```text
External case / database / file formats
            |
            v
Input normalization and validation
            |
            v
Internal network + device model  <---->  topology snapshot
            |
            +---- network stamping / injections
            +---- control equations / active-set state
            +---- derivative contributions
            |
            v
Residual/Jacobian assembly
            |
            v
Nonlinear driver  <---->  sparse linear-algebra backend
            |
            v
Control coordinator / state machine
            |
            v
Post-processing + diagnostics + result provenance
            |
            v
Planning / EMS / security / simulation APIs
```

The interfaces should enforce several boundaries:

- external identifiers never become implicit matrix indices;
- device models do not directly manipulate sparse-solver internals;
- the linear solver does not decide control ownership;
- control logic does not silently rewrite raw engineering data;
- post-processing reads the accepted internal model, not a parallel reimplementation;
- caches declare their dependency/version keys rather than relying on “remember to rebuild this matrix.”

This architecture also makes the codebase evolvable. A new sparse backend can be introduced without rewriting device physics. A new device model can expose residual and derivative contributions without changing every solver loop. Automatic differentiation can be added behind derivative interfaces. A contingency engine can reuse topology products without knowing the details of Newton globalization.

Determinism deserves explicit attention. Given the same case, options, active sparse backend, and thread policy, repeated runs should normally produce the same control decisions and practically identical numerical results. If several controls are equally eligible, define tie-breaking rather than accepting hash-table or thread-scheduling order as part of the engineering model.

### 12.13 A practical production-readiness checklist

The following checklist summarizes the implementation standard implied by this article.

| Layer | Production question | Minimum evidence before calling the solver industrial-grade |
|---|---|---|
| Model scope | Are all represented controls and limits explicit? | Documented device equations, modes, ownership, limits, and unsupported cases. |
| Data | Can bad or ambiguous cases be rejected before iteration? | Base/topology/reference validation, stable indexing, parameter diagnostics. |
| Equations | Is the solved residual the declared physical/control problem? | Explicit state/equation maps and derivative tests for all active continuous dependencies. |
| Nonlinear solve | Can difficult cases fail predictably rather than mysteriously? | Warm starts, safeguards, bounded recovery hierarchy, classified termination. |
| Linear algebra | Does performance scale with sparse structure? | Sparse assembly/factorization, ordering, cache rules, memory and timing instrumentation. |
| Controls | Are limits and discrete devices coordinated? | Active-set/state-machine logic, hysteresis, priorities, cycling protection, event logs. |
| Results | Are reported flows and outputs consistent with the solved model? | Same terminal/sign conventions, conservation checks, recovered limits and reserves. |
| Diagnostics | Can an engineer identify the dominant reason for failure or stress? | Mismatch ranking, control history, island status, factorization warnings, final violation report. |
| Verification | Can changes be defended release after release? | Regression corpus, independent comparisons, derivative tests, expected failure cases. |
| Workloads | Does the design exploit repeated related solves? | Validity-aware caching, warm starts, safe parallel scenarios, workload-level benchmarks. |
| Architecture | Can models and numerical backends evolve independently? | Stable module interfaces, versioned model snapshots, explicit dependency invalidation. |
| Provenance | Can a result be reconstructed? | Case/model/options/backend versions, tolerances, initialization, mode history, warnings. |

The key engineering principle is therefore stronger than “use Newton with sparse matrices”:

> **Industrial quality comes from making the model, active controls, numerical method, sparse computation, diagnostics, verification, and software architecture obey one another's contracts.**

The nonlinear equations remain the mathematical center of the program, but the surrounding systems determine whether those equations are the right ones, whether they are solved predictably, and whether anyone can trust the answer afterward.


## Closing perspective

The matrix view of power flow is more than compact notation. It reveals a chain of responsibilities:

$$
\begin{gathered}
\text{topology and terminal laws}\longrightarrow Y_{\mathrm{bus}}\longrightarrow I=YV\\
\longrightarrow S=[V]\overline I\longrightarrow
\text{controls and residuals}\longrightarrow
\text{Jacobians and sparse solves}.
\end{gathered}
$$

That chain also reveals where errors enter. A wrong terminal convention corrupts the network operator. A wrong control assumption changes the problem. An incomplete derivative changes the iteration. A weak acceptance test changes what “solved” means.

Getting the Jacobian right is essential. Keeping every layer consistent with it is what turns a correct calculation into trustworthy engineering software.

**The goal is not merely a voltage vector. It is a voltage vector whose equations, controls, limits, and numerical evidence can all be explained.**

---

<a id="appendix-a"></a>

## Appendix A. Scalar Jacobian formulas for independent checks

For fixed $Y$ and constant specifications, let $J_{\mathrm{full}}=[H\ N;\ M\ L]$ as in (13). For $i\ne j$,

$$
\begin{aligned}
H_{ij}&=m_im_j(G_{ij}\sin\theta_{ij}-B_{ij}\cos\theta_{ij}),\\
N_{ij}&=m_i(G_{ij}\cos\theta_{ij}+B_{ij}\sin\theta_{ij}),\\
M_{ij}&=-m_im_j(G_{ij}\cos\theta_{ij}+B_{ij}\sin\theta_{ij}),\\
L_{ij}&=m_i(G_{ij}\sin\theta_{ij}-B_{ij}\cos\theta_{ij}).
\end{aligned}
$$

The diagonal terms are

$$
\begin{aligned}
H_{ii}&=-Q_i-B_{ii}m_i^2,&
N_{ii}&=P_i/m_i+G_{ii}m_i,\\
M_{ii}&=P_i-G_{ii}m_i^2,&
L_{ii}&=Q_i/m_i-B_{ii}m_i.
\end{aligned}
$$

Here $P_i,Q_i$ are calculated **net network injections**, not generator outputs. These expressions follow by differentiating (6), and they agree with (11)–(13). Add the specified-injection derivative corrections from Section 5 before interpreting them as the Jacobian of a more general residual.

<a id="appendix-b"></a>

## Appendix B. The same differential supports other formulations

For Cartesian voltage $V=v_r+jv_i$, equation (10) gives

$$
\frac{\partial S}{\partial v_r}=[\overline I]+[V]\overline Y,\qquad
\frac{\partial S}{\partial v_i}=j[\overline I]-j[V]\overline Y.
$$

The appropriate real equations and controls must still be supplied. For example, a PV magnitude constraint can be written $v_{r,i}^2+v_{i,i}^2-(m_i^\star)^2=0$ when those Cartesian components are retained as independent variables. Changing coordinates preserves the represented physical solutions, but it need not preserve Newton's trajectory away from a solution. Power-balance and current-balance formulations similarly require a consistent treatment of their unknown device outputs [6,7].

For branch-flow derivatives, the same product rule yields

$$
dS_f=[\overline I_f]C_f\,dV+[V_f]\overline{Y_f}\,d\overline V
$$

for fixed branch matrices, with an analogous expression at the to end.

Finally, consider a parameterized fixed-mode problem $F(x,\lambda)=0$. At a solution with nonsingular $J$,

$$
J\frac{dx}{d\lambda}=-\frac{\partial F}{\partial\lambda}.
$$

Sensitivities therefore reuse a linear solve at the converged state rather than requiring an explicit inverse. They are local to the current smooth mode. At a limit transition, the equation set and its sensitivities may change; near a singularity, ordinary implicit-function sensitivities may cease to be well defined. This is where power flow connects naturally to continuation, optimization, and security analysis—provided its modeling boundaries remain visible.

<a id="references"></a>

## References and implementation sources

1. W. F. Tinney and C. E. Hart, “Power Flow Solution by Newton's Method,” *IEEE Transactions on Power Apparatus and Systems*, vol. PAS-86, no. 11, pp. 1449–1460, 1967. DOI: [10.1109/TPAS.1967.291823](https://doi.org/10.1109/TPAS.1967.291823).

2. W. F. Tinney and J. W. Walker, “Direct Solutions of Sparse Network Equations by Optimally Ordered Triangular Factorization,” *Proceedings of the IEEE*, vol. 55, no. 11, pp. 1801–1809, 1967. DOI: [10.1109/PROC.1967.6011](https://doi.org/10.1109/PROC.1967.6011).

3. B. Stott and O. Alsaç, “Fast Decoupled Load Flow,” *IEEE Transactions on Power Apparatus and Systems*, vol. PAS-93, no. 3, pp. 859–869, 1974. DOI: [10.1109/TPAS.1974.293985](https://doi.org/10.1109/TPAS.1974.293985).

4. R. D. Zimmerman, “AC Power Flows, Generalized OPF Costs and their Derivatives using Complex Matrix Notation,” *MATPOWER Technical Note 2*, February 2010; revision 7, June 20, 2019. See especially Sections 3–5. [Technical note](https://matpower.org/docs/TN2-OPF-Derivatives.pdf).

5. R. D. Zimmerman, C. E. Murillo-Sánchez, and R. J. Thomas, “MATPOWER: Steady-State Operations, Planning, and Analysis Tools for Power Systems Research and Education,” *IEEE Transactions on Power Systems*, vol. 26, no. 1, pp. 12–19, 2011. DOI: [10.1109/TPWRS.2010.2051168](https://doi.org/10.1109/TPWRS.2010.2051168).

6. MATPOWER 7.1 source reference: [`makeYbus`](https://matpower.org/docs/ref/matpower7.1/lib/makeYbus.html), [`dSbus_dV`](https://matpower.org/docs/ref/matpower7.1/lib/dSbus_dV.html), [`newtonpf`](https://matpower.org/docs/ref/matpower7.1/lib/newtonpf.html), and [`makeSbus`](https://matpower.org/docs/ref/matpower7.1/lib/makeSbus.html). Version-specific links are used to make the cited implementation inspectable, not to identify the latest release.

7. MATPOWER User's Manual, Section 4.1, [“AC Power Flow”](https://matpower.app/manual/matpower/ACPowerFlow.html), including reduced variables, alternative formulations, and reactive-limit enforcement.

8. V. Ajjarapu and C. Christy, “The Continuation Power Flow: A Tool for Steady State Voltage Stability Analysis,” *IEEE Transactions on Power Systems*, vol. 7, no. 1, pp. 416–423, 1992. [IEEE record](https://ieeexplore.ieee.org/document/141737/).

9. SUNDIALS, KINSOL documentation, [“Mathematical Considerations”](https://sundials.readthedocs.io/en/latest/kinsol/Mathematics_link.html), especially scaling, globalization, and nonlinear stopping criteria. Consult the documentation matching the deployed version when implementing these policies.

10. SciPy reference documentation: [`scipy.sparse.linalg.splu`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.splu.html) and [`scipy.optimize.root`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html). The companion's tested package versions are recorded with its numerical results.
