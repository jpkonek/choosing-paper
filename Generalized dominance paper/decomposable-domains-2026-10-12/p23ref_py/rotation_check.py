#!/usr/bin/env python3
"""P2P3 referee: monotone rotation (Thm pivot) of the kinked facet maps, and the twoslope obstruction:
a kink in a(tau)=c(h(tau)) violates concavity of a.delta on the cone C_J (Lemma twoslope), i.e. the
kinked data cannot be the facet data of a coherent family with half-plane charts."""
import sys, numpy as np
sys.argv = ['x', '0.3', '../p2py/holonomy_onekink_F1_eps0.3.npy']
exec(open('box_exact.py').read().split('# --- checks')[0])
for k in range(3):
    ts = np.linspace(1e-6, 1-1e-6, 200001)
    C = np.array([chart(k,t)[1] for t in ts])
    cr = np.cross(C[:-1], C[1:]) @ np.ones(3)/np.sqrt(3)   # signed area in 1-perp
    print(f"facet {k+1}: rotation increments sign: min {cr.min():.3e} max {cr.max():.3e} (one sign = monotone)")
# kink jump of a'(tau) on F_1 and its pairing with the cone C_J of directions delta with n(tau).delta>0 near tb
tb = P[0][-1]; d = 1e-6
a = lambda t: chart(0,t)[1]
jump = (a(tb+2*d)-a(tb+d))/d - (a(tb-d)-a(tb-2*d))/d
n = a(tb)/np.linalg.norm(a(tb))
w = np.cross(np.ones(3)/np.sqrt(3), n)          # tangent direction in 1-perp
print("jump of a' at the break (in 1-perp):", jump, " components along n, w:", jump@n, jump@w)
# on C_J (delta with n.delta>0 for tau near tb) the values jump.delta take both signs iff jump not prop. to -n... :
for s in [-1, 1]:
    delta = n + 5*s*w
    print(f"  delta=n{'+' if s>0 else '-'}5w: n.delta={n@delta:.2f}, jump.delta={jump@delta:.3e}")
print("concavity of a.delta on C_J needs jump.delta<=0 for all delta in C_J; f_delta=b.delta (b=(beta/alpha)a) on -C_J needs jump.delta>=0 there -> jump=0.")
