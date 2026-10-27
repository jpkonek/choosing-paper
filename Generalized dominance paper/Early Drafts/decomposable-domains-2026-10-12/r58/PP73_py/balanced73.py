"""N4-N5 (NUMERICS): (i) member pairs with a strictly middle log-coordinate and the u1 sign structure of
their middle-world layer (both signs present => a balanced swap exists, PP62 Cor 1.2 + Lyapunov);
(ii) (H_Gamma) for u1 at loop members: Gamma(a, a o (1+t e_w)) in O_w."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib73 import *

G = sample(2_000_000)
odd = classes(G); nrm = np.linalg.norm(G, axis=1)
ranksG = lambda x: ranks(G, x)


def pair(name, a, b):
    Xa, Xb = advice(G, a), advice(G, b)
    lay = Xa != Xb
    d = np.log(np.asarray(b) / np.asarray(a)); d -= d.mean()
    o = np.argsort(d)
    print(f'  {name}: d = {np.round(d,4)}  (min w{o[0]+1}, mid w{o[1]+1}, max w{o[2]+1})')
    Ra, Rb = ranksG(Xa), ranksG(Xb)
    for k in range(3):
        sel = lay & (odd == k)
        imp = (sel & (Rb[:, k] < Ra[:, k])); wor = (sel & (Rb[:, k] > Ra[:, k]))
        print(f'     odd-{k+1} layer: |g|-mass improving w{k+1}: {nrm[imp].sum()/len(G):.5f}, worsening: {nrm[wor].sum()/len(G):.5f}')
    m = o[1]
    sel = lay & (odd == m)
    imp = sel & (Rb[:, m] < Ra[:, m]); wor = sel & (Rb[:, m] > Ra[:, m])
    if imp.any() and wor.any():
        # explicit balanced swap: all of the smaller side + a radial slab of the larger side with equal |g|-mass
        mi, mw = nrm[imp].sum(), nrm[wor].sum()
        small, big = (imp, wor) if mi < mw else (wor, imp)
        target = min(mi, mw)
        idx = np.where(big)[0]; idx = idx[np.argsort(nrm[idx])]
        cum = np.cumsum(nrm[idx]); take = idx[cum <= target]
        F = small.copy(); F[take] = True
        V = Phi(G, np.where(F, Xb, Xa)) - Phi(G, Xa)
        print(f'     balanced swap F (mid world {m+1}): mass {F.sum()} pts, V(F: a->b) = {np.round(V, 6)}')


a, a2 = 1.10, 1.05
u, m1, m2 = loop(a)
_, m1b, m2b = loop(a2)
print('=== balanced swaps')
pair('m1(1.10) vs m2(1.10) [same loop]', m1, m2)
pair('u vs m1(1.10)  [same loop]', u, m1)
pair('m1(1.05) vs m2(1.10)', m1b, m2)
pair('m1(1.10) vs m2(1.05)', m1, m2b)
d1 = lambda s: np.array([s ** -2, s, s])
pair('u vs m1(1.10) o d1(1.05)', u, norm(m1 * d1(1.05)))
pair('u vs m1(1.05) o d1(1.10)', u, norm(m1b * d1(1.10)))

print('=== (H_Gamma) at loop members, t = 0.01')
for name, a0 in [('u', u), ('m1(1.10)', m1), ('m2(1.10)', m2), ('m1(1.05)', m1b)]:
    X0 = advice(G, a0); P0 = Phi(G, X0)
    for w in range(3):
        b = norm(a0 * (1 + 0.01 * np.eye(3)[w]))
        gam = (P0 - Phi(G, advice(G, b))) / 0.01
        inO = all(gam[v] < 0 for v in range(3) if v != w)
        print(f'  {name} shift +e{w+1}: Gamma/t = {np.round(gam,4)}  in O_{w+1}: {inO}')
