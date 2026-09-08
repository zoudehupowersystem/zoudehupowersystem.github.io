function mpc = case3_zou
%CASE3_ZOU Synthetic case for Dehu Zou's Ybus-to-power-flow article.
% Balanced positive-sequence, 100 MVA base; no separate bus shunts.
% Branch 1-2 has a from-side tap 1.02 * exp(j*4 degrees).
% This is an illustrative verification case, not an IEEE benchmark.
% Q limits are initially wide. For the limiting experiment, set
% mpc.gen(2, QMAX) = 10 and enable pf.enforce_q_lims.

mpc.version = '2';
mpc.baseMVA = 100;
% bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
mpc.bus = [
    1 3  0  0 0 0 1 1.04 0 230 1 1.10 0.90;
    2 2  0  0 0 0 1 1.02 0 230 1 1.10 0.90;
    3 1 90 35 0 0 1 1.00 0 230 1 1.10 0.90;
];
% bus Pg Qg Qmax Qmin Vg mBase status Pmax Pmin [remaining fields]
mpc.gen = [
    1  0 0 999 -999 1.04 100 1 999 -999 0 0 0 0 0 0 0 0 0 0 0;
    2 50 0 999 -999 1.02 100 1 999 -999 0 0 0 0 0 0 0 0 0 0 0;
];
% f t r x total_b rateA rateB rateC tap shift status angmin angmax
mpc.branch = [
    1 2 0.02 0.06 0.030 0 0 0 1.02 4 1 -360 360;
    1 3 0.08 0.24 0.025 0 0 0 1.00 0 1 -360 360;
    2 3 0.06 0.18 0.020 0 0 0 1.00 0 1 -360 360;
];
end
