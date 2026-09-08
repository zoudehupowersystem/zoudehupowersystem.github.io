function check_case3_zou
%CHECK_CASE3_ZOU External reproduction against an installed MATPOWER.
% Put this file and case3_zou.m on the MATLAB/Octave path, install MATPOWER,
% then run: check_case3_zou
% This script was supplied but NOT executed when the article was prepared.

if exist('runpf', 'file') ~= 2 || exist('define_constants', 'file') ~= 2
    error('MATPOWER is not on the MATLAB/Octave path. Install and initialize it first.');
end
define_constants;
opts = mpoption('pf.alg', 'NR', 'pf.tol', 1e-11, ...
    'pf.nr.max_it', 30, 'pf.enforce_q_lims', 0, ...
    'verbose', 0, 'out.all', 0);
[r, ok] = runpf(case3_zou, opts);
assert(ok, 'Base-case AC power flow did not converge.');
expected_vm = [1.04; 1.02; 0.956912891031405];
expected_va = [0; -3.572405502168944; -6.763479175367291];
expected_flows = 100 * [ ...
    -0.11827508000257361, 0.017649611619485483, 0.11856546342280673, -0.047978463665593545;
     0.5561871879022029, 0.1899856758803431, -0.5302434935159547, -0.1371206212343751;
     0.3814345365771917, 0.22835264623484347, -0.36975650648404496, -0.21287937876562338];
assert(max(abs(r.bus(:,VM)-expected_vm)) < 1e-8, 'Voltage magnitudes differ.');
assert(max(abs((r.bus(:,VA)-r.bus(1,VA))-expected_va)) < 1e-6, 'Angles differ.');
d = r.branch(:,[PF QF PT QT])-expected_flows;
assert(max(abs(d(:))) < 1e-6, 'Branch flows differ (MW/MVAr).');
assert(abs(r.gen(2,QG)-18.037418256925267) < 1e-6, 'PV reactive output differs.');

limited = case3_zou;
limited.gen(2,QMAX) = 10;
[q, ok] = runpf(limited, mpoption(opts, 'pf.enforce_q_lims', 1));
assert(ok, 'Q-limited AC power flow did not converge.');
assert(abs(q.gen(2,QG)-10) < 1e-6, 'Reactive limit was not enforced.');
assert(abs(q.bus(2,VM)-1.0158318005392462) < 1e-8, 'Limited bus voltage differs.');
assert(abs(q.bus(3,VM)-0.9543319714030899) < 1e-8, 'PQ voltage differs after switching.');
fprintf('Base and Q-limited cases agree with the supplied Python reference.\n');
end
