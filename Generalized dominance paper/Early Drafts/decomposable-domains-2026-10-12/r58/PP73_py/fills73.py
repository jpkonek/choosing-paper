"""N6 (NUMERICS): u1 accounting of class-3 fills of T against ray repairers C_{m1(a)}.
V(C1(a) -> X_E) = Phi(X_E) - Phi(C1(a)).  Prediction (PP73 Prop 4.2):
  = (p(a) - e - f, p(a) - e - f, -2 p(a) + 2e + 4f),  e = |g|-mass of E^h, f = of E^{-h}, p(a) = V_3(T->C1(a))/2.
So V >= 0 iff e + f <= p(a) <= e + 2f: a knife-edge for pure-h fills (f = 0)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib73 import *

G = sample(1_000_000, seed=7)
odd = classes(G); A = majority(G); h = np.sign(G.sum(1)); nrm = np.linalg.norm(G, axis=1)
T = advice(G, [1/3]*3)
Q3 = (T == 0) & (odd == 2)
Eh_all = Q3 & (A == h); Emh_all = Q3 & (A != h)
rng = np.random.default_rng(1)
scales = np.linspace(1.0, 1.17, 341)
PT = Phi(G, T)
pa = np.array([(Phi(G, advice(G, loop(a)[1])) - PT)[2] / 2 for a in scales])
P1 = [Phi(G, advice(G, loop(a)[1])) for a in scales]
for name, frac_h, frac_mh in [('pure-h', 0.03, 0.0), ('pure -h', 0.0, 0.03), ('mixed', 0.02, 0.01)]:
    E = (Eh_all & (rng.random(len(G)) < frac_h * 10)) | (Emh_all & (rng.random(len(G)) < frac_mh * 10))
    X = np.where(E, A, T)
    e = nrm[E & (A == h)].sum() / len(G); f = nrm[E & (A != h)].sum() / len(G)
    V = np.array([Phi(G, X) - P for P in P1])
    pred = np.stack([pa - e - f, pa - e - f, -2 * pa + 2 * e + 4 * f], 1)
    ok = (V >= -1e-12).all(1)
    print(f'{name}: e = {e:.5f}, f = {f:.5f}; max |V - prediction| over the scale grid = {np.abs(V - pred).max():.2e}')
    if ok.any():
        print(f'   scales with V >= 0 (u1-endorsed domination possible): a in [{scales[ok].min():.4f}, {scales[ok].max():.4f}],'
              f' p there in [{pa[ok].min():.5f}, {pa[ok].max():.5f}] vs window [e+f, e+2f] = [{e+f:.5f}, {e+2*f:.5f}]')
    else:
        i = np.argmin(np.abs(pa - e - f))
        print(f'   no grid scale has V >= 0; closest: a = {scales[i]:.4f}, V = {np.round(V[i], 6)} (knife-edge p(a) = e)')
