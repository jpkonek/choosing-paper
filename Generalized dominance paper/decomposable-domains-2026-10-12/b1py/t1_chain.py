"""B1 notes: the transfer chain of Lemma B1.2 on a sampled T1 instance (NUMERICS).

U = D_{K'}, K' = u + s(T1 - u), eps = 0.3, s = 0.9.  C = D_K for K = conv(T1 u {q})
(coherent, K contains K'), X = T1 minus a thin cone around a mixed ray w of D_{T1} with
w_1 < 0 (the kind of incoherent near-T1 model forced by Theorem R3).  For each world i and a
non-constant positive density rho_i, every sample gamble is an atomless cell of mass
rho_i(g)/N; the chain of transfer_chain.py is built between C and X (or X and C) and each
step is checked to lie in one edge region R_ij or R_ik of world i.  It derives the strict
world-i comparison that rho_i favours, so the opposite comparison (a reversal) cannot be
added to a world with leading edge densities rho_i.  Run:  python3 -I t1_chain.py
"""
import sys
import os
from fractions import Fraction as F
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transfer_chain import chain  # noqa: E402

eps, s = 0.3, 0.9
u = np.ones(3) / 3
c0 = (1 - eps) / 3
V = np.array([c0 * np.ones(3) + eps * np.eye(3)[k] for k in range(3)])   # vertices of T1
Kp = u + s * (V - u)                                                      # vertices of K'
q = np.array([0.12, 0.62, 0.26])
KC = np.vstack([V, q])            # C = D_K, K = conv(T1 u {q}) contains T1, hence K'

rng = np.random.default_rng(15102026)
G = rng.standard_normal((400000, 3))
inU = (G @ Kp.T).min(axis=1) > 0
G = G[inU]
mixed = ~((G > 0).all(axis=1) | (G < 0).all(axis=1))
inT1 = (G @ V.T).min(axis=1) > 0
inC = (G @ KC.T).min(axis=1) > 0
w = np.array([-0.5, 1.0, 1.0])
assert (V @ w > 0).all()
cosang = (G @ w) / (np.linalg.norm(G, axis=1) * np.linalg.norm(w))
cone = cosang > np.cos(0.15)
inX = inT1 & ~cone
D = (inC != inX)
assert not (D & ~mixed).any(), 'D must lie in M'
print('samples in U:', len(G), ' |C xor X| =', int(D.sum()), ' |X xor T1| =',
      int((inX != inT1).sum()))


def cls_of(g, i):
    """'L' if g in Q_i (g_i opposite to both others), 'J'/'K' for Q_j/Q_k, None if not mixed."""
    sg = np.sign(g)
    j, k = [x for x in range(3) if x != i]
    if sg[i] != sg[j] and sg[i] != sg[k]:
        return 'L'
    if sg[j] != sg[i] and sg[j] != sg[k]:
        return 'J'
    if sg[k] != sg[i] and sg[k] != sg[j]:
        return 'K'
    return None


def rho(g, i):
    return abs(g[i]) * (1.0 + 0.5 * np.sin(2 * g[0] - g[1] + 0.7 * g[2])) + 0.05


for i in range(3):
    # world-i error: accept g errs iff g_i < 0; reject errs iff g_i > 0
    errC = np.where(inC, G[:, i] < 0, G[:, i] > 0)
    errX = np.where(inX, G[:, i] < 0, G[:, i] > 0)
    idx = np.where(mixed)[0]
    # ensure some room exists in the link class (Q_i outside D); keep a subsample for speed
    sub = rng.choice(idx, size=min(len(idx), 3000), replace=False)
    sub = np.union1d(sub, np.where(D)[0])
    base_is_C = None
    cells_C, cells_X = [], []
    for n in sub:
        g = G[n]
        cl = cls_of(g, i)
        m = F(int(round(rho(g, i) * 1e6)), 10**6 * len(G))
        cells_C.append(dict(cls=cl, m=m, err=bool(errC[n]), inD=bool(D[n])))
        cells_X.append(dict(cls=cl, m=m, err=bool(errX[n]), inD=bool(D[n])))
    delta = sum(c['m'] * (-1 if c['err'] else 1) for c in cells_C if c['inD'])
    if delta > 0:
        steps, dd, mode = chain(cells_C)
        verdict = 'C strictly better than X at world %d (C < X)' % (i + 1)
    else:
        steps, dd, mode = chain(cells_X)
        verdict = 'X strictly better than C at world %d (X < C)' % (i + 1)
    regions = set(st[0] for st in steps)
    assert all(st[1] > 0 for st in steps)
    j, k = [x + 1 for x in range(3) if x != i]
    names = {'LJ': 'R_%d%d' % (i + 1, j), 'LK': 'R_%d%d' % (i + 1, k)}
    print('world %d: rho-error(X) - rho-error(C) = %+.3e ; chain %s, %d steps, regions %s, '
          'each step change %.3e > 0 ;  derived: %s'
          % (i + 1, float(delta), mode, len(steps), sorted(names[r] for r in regions),
             float(steps[0][1]), verdict))
print('A reversal of any derived comparison would give a strict cycle Y < Y at that world.')
