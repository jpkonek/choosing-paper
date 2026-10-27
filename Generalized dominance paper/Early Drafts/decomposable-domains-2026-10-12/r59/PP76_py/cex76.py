"""PP76 cex76 (NUMERICS): section-limit-then-copy counterexample to PP72 Theorem 6.2.
Indices in log-likelihood coordinates; likelihood = exp(m).  C_m(g) = T(exp(m) o g).
R3 = {s d3}, R2 = {s (-1,2,-1)};  N = s d3 + t d1 with s = 2t (a PP72 defender, k = 1).
Base a = sig*(-1,2,-1) in R2 (sig < t); a_n inward; carrier u approached along R3.
Advice: +1/-1 answer that sign, 0 silent.  u1 from PP73 lib (loss: larger = worse).
"""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib73copy import sample, advice, ranks, classes, u1

d3 = np.array([1., 1., -2.]); d1 = np.array([-2., 1., 1.]); r2 = np.array([-1., 2., -1.])
def C(G, m): return advice(G, np.exp(m))
def Phi(G, x): return u1(G, x).mean(0)

G = sample(4_000_000, seed=76)
nrm = np.linalg.norm(G, axis=1); odd = classes(G); h = np.sign(G.sum(1))
t = 0.04; s = 2 * t; sig = 0.01
mN = s * d3 + t * d1; ma = sig * r2; u = np.zeros(3)
T = C(G, u); N = C(G, mN); Ca = C(G, ma)
for nm, x in [('T', T), ('N', N), ('Ca', Ca)]:
    print(nm, 'answers -h on', int(((x != 0) & (x != h)).sum()), 'sample points')
# 1. nestedness along R2
for sn in [0.002, 0.005, 0.008]:
    Can = C(G, sn * r2)
    bad = ~((Can == T) | (Can == Ca))
    inner = (Can != T) & (Ca == T)
    print(f'sig_n={sn}: points with C_an not in {{T,Ca}}: {int(bad.sum())};  L(u,a_n) not inside L(u,a): {int(inner.sum())}')
# 2. odd-1 part of L(u,N) outside L(u,a), split by sign of world-1 change
rT = ranks(G, T)[:, 0]; rN = ranks(G, N)[:, 0]
base = (N != T) & (Ca == T) & (odd == 0)
Fp = base & (rN < rT); Fm = base & (rN > rT)
print('odd-1, N!=T, Ca==T: improving-1 mass %.3e (pts %d), worsening-1 mass %.3e (pts %d)' %
      ((nrm * Fp).mean(), Fp.sum(), (nrm * Fm).mean(), Fm.sum()))
# 3. build balanced F: radial band 1<|g|<2 (non-conic), then trim F+ to equal |g|-mass
band = (nrm > 1.0) & (nrm < 2.0)
Fp &= band; Fm &= band
mp, mm = (nrm * Fp).sum(), (nrm * Fm).sum()
if mp > mm:  # trim the larger part by |g|-mass
    idx = np.where(Fp)[0]; cs = np.cumsum(nrm[idx]); keep = idx[cs <= mm]; Fp = np.zeros_like(Fp); Fp[keep] = True
else:
    idx = np.where(Fm)[0]; cs = np.cumsum(nrm[idx]); keep = idx[cs <= mp]; Fm = np.zeros_like(Fm); Fm[keep] = True
F = Fp | Fm
X = Ca.copy(); X[F] = N[F]
VF = Phi(G, X) - Phi(G, Ca)
print('V(C_a -> X) = V(F : T -> N) =', VF, ' (scale: per-point mass of F %.3e)' % (nrm * F).mean())
# 4. the base sequence, carrier check and the argmax at the carrier's approximants
for sn in [0.006, 0.008, 0.009]:
    Can = C(G, sn * r2)
    supp = Can != X
    carried = np.all(T[supp] == Can[supp])
    Vrho = Phi(G, X) - Phi(G, Can)
    print(f'a_n = {sn}*r2: V(rho_n) = {np.round(Vrho, 5)}; T carries rho_n: {carried}')
    X2 = T.copy(); X2[supp] = X[supp]          # X''_n = T + rho_n
    for z in [0.004, 0.002, 0.001]:
        Ccm = C(G, z * d3)
        V = Phi(G, X2) - Phi(G, Ccm)
        print(f'    c_m = {z}*d3: V(C_cm -> X\'\'_n) = {np.round(V, 5)}  argmax world {int(np.argmax(V)) + 1}')
