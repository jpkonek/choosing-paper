"""F2 NUMERICS (no proof rests on this). Where ends of a protected world can sit for T1 (eps=0.3, s=0.9),
and Lemma E1.4 for an end at dU. Run: python3 -I f2_ends_T1.py"""
import numpy as np
eps, s = 0.3, 0.9
c0 = (1 - eps) / 3; u = np.ones(3) / 3
V = np.array([c0 * np.ones(3) + eps * np.eye(3)[k] for k in range(3)])
Vp = np.array([u + s * (V[k] - u) for k in range(3)])
kap = (1 + 2 * eps) / (1 - eps)
P = lambda K, g: (g @ K.T).min(axis=-1)          # lower prevision of a polytope credal set (vertices K)
rng = np.random.default_rng(11)

def unit(g): return g / np.linalg.norm(g, axis=-1, keepdims=True)

# (1) directions approaching dU, by sign class: is T1 world-1-correct there?
G = unit(rng.normal(size=(4_000_000, 3)))
G = G[P(Vp, G) > 0]
mar = P(Vp, G)                                   # distance-like margin to dU (unit gambles)
near = mar < 2e-3
T = P(V, G) > 0
sg = np.sign(G).astype(int)
print("(1) unit gambles of U within margin 2e-3 of dU, by sign class: count, T1 accepts, T1 world-1-correct")
for cls in sorted(set(map(lambda r: tuple(int(v) for v in r), sg[near]))):
    m = near & np.all(sg == cls, axis=1)
    acc = T[m].mean()
    cor1 = np.mean(np.where(T[m], G[m, 0] > 0, G[m, 0] < 0))
    print(f"    {cls}: n={m.sum():6d}  accept={acc:.3f}  world-1-correct={cor1:.3f}")

# (2) far end of the e12 edge chain: margin of P_2 = D_{co(K' u e2)} vanishes only at dU or at {h2 = 0}
K2 = np.vstack([Vp, [0, 1, 0]])
R12 = G[:, 0] * G[:, 1] < 0
marg = np.where(G[:, 1] > 0, np.minimum(P(Vp, G), G[:, 1]), -G[:, 1])   # acceptance / rejection margin of P_2 on R12
small = R12 & (np.abs(marg) < 1e-3)
on_dU = P(Vp, G[small]) < 2e-3
on_pl = np.abs(G[small, 1]) < 2e-3
print(f"(2) R12 unit gambles with P_2-margin < 1e-3: {small.sum()}; near dU: {on_dU.mean():.3f}, near h2=0: {on_pl.mean():.3f}, either: {np.mean(on_dU | on_pl):.3f}")
# (-,0,+) and (+,0,-) directions inside U (mixed, two payoffs bounded away from 0)
bs = np.linspace(0.05, 30, 600)
inU_m = [b for b in bs if P(Vp, np.array([-1.0, 0, b])) > 0]
inU_p = [b for b in bs if P(Vp, np.array([1.0, 0, -b])) > 0]
print(f"    (-1,0,b) in U for b in [{min(inU_m):.2f},{max(inU_m):.2f}] (kappa={kap:.3f}); T1 accepts iff b > kappa")
print(f"    (1,0,-b) in U for b in [{min(inU_p):.2f},{max(inU_p):.2f}]")

# (3) Lemma E1.4 at a dU end of world 1: end S_m = (-,+,+) gambles with margin < 2^-m. T1 is world-1-correct there.
COR = np.where(T[:, None], G > 0, G < 0)
L = 4.0
W = np.where(COR, L, 1.0)                        # nu^L (admissible, B_u = T1)
Sm = lambda m: (G[:, 0] < 0) & (G[:, 1] > 0) & (G[:, 2] > 0) & (mar < 2.0 ** -m)
print("    T1 world-1-correct on S_m (m=4..8):", [bool(np.all(COR[Sm(m), 0])) for m in range(4, 9)])
Wh = W.copy()
for l, m in enumerate(range(6, 14), start=1):   # depths start where T1 is world-1-correct (E1.4 hypothesis)   # f_1 = l (rho2+rho3)/rho1 on S_{m_l}
    idx = Sm(m); Wh[idx, 0] = W[idx, 0] * (1 + l * (W[idx, 1] + W[idx, 2]) / W[idx, 0])
val = (np.sign(G) * Wh) @ u
print("(3) heavy reweighting at the dU end keeps B_u = T1:", bool(np.all((val > 0) == T)), " ties:", int((val == 0).sum()))
bad = 0; tot = 0
for _ in range(200):
    t = rng.dirichlet([1, 1, 1])
    if 1 / t[0] >= 8: continue                   # only depths l <= 8 were reweighted; need l > 1/t1
    l = int(np.floor(1 / t[0])) + 1; m = 5 + l
    idx = Sm(m)
    acc = ((np.sign(G[idx]) * Wh[idx]) @ t) > 0
    bad += int(acc.sum()); tot += int(idx.sum())    # accepting h1<0 is a world-1 error
print(f"    heavy-shadow Bayes models accept (world-1 error) {bad} of {tot} end samples at depth beyond 1/t1 (must be 0)")
