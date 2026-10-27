#!/usr/bin/env python3
"""P2P3 referee: Monte Carlo spot-check of P2 Lemma 6.1 (nested world-1 error sets), own code.
E_1(D) = (D triangle P_1) on R^3 (P_1 = {h1>0}); D_M = {min_{m in M} m.h > 0}. Inclusion tested a.e. by sampling."""
import numpy as np
rng = np.random.default_rng(3)
H = rng.standard_normal((2_000_000,3))
eps=0.3; u=np.ones(3)/3; E=np.eye(3)
T1=[(1-eps)*u+eps*E[k] for k in range(3)]
def D(vs): return np.min(np.stack([H@v for v in vs]),0) > 0
def err1(vs): d=D(vs); return d ^ (H[:,0]>0)
def frac_not_incl(M, Mp):
    a, b = err1(M), err1(Mp); return (a & ~b).mean()
cases = {
 "homothety at e1, factor 1.2 (radial push, criterion: nested)": [E[0]+1.2*(v-E[0]) for v in T1],
 "homothety at e1, factor 0.8 (radial pull, criterion: reverse nested)": [E[0]+0.8*(v-E[0]) for v in T1],
 "homothety at u, factor 1.1 (criterion: not nested)": [u+1.1*(v-u) for v in T1],
 "translate by (0,.02,-.02) (criterion: not nested)": [v+np.array([0,.02,-.02]) for v in T1],
}
for name, Mp in cases.items():
    print(f"{name}: mu(E1(D_T1) minus E1(D_M')) = {frac_not_incl(T1,Mp):.2e} ; reverse = {frac_not_incl(Mp,T1):.2e}")
