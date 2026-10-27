"""C1 notes Sec. 2 (NUMERICS): what degenerates in the gauge-mixture approximants of R10a Prop M'.

K_q = nu(sum_i q_i M_i), M_i = conv{a e_i, b w_1, b w_2, b w_3}, W = T1(eps'), target T1(eps=0.3).
We report d_H(K_q, W) along the ray q(s) = (1-2s, s, s) from e_1 to u, for decreasing a/b.
First guess (a boundary layer) was WRONG: choosing x_i = a e_i for every i puts q itself in K_q.
Correct limit (Sec. 2, Lemma 2.2): K_q -> conv(W u {q}) as a/b -> 0, uniformly in q; a plateau K_q = W on W.
Also: every pair is split (c + c' <= 0 on Delta), checked on random gambles.
"""
import numpy as np
from itertools import product
E = np.eye(3)
def T1(e): return [(1 - e) / 3 * np.ones(3) + e * E[k] for k in range(3)]
def hull_pts(q, a, b, W):
    Ms = [[a * E[i]] + [b * w for w in W] for i in range(3)]
    pts = [sum(q[i] * Ms[i][j[i]] for i in range(3)) for j in product(range(4), repeat=3)]
    return np.array([p / p.sum() for p in pts])
def support(P, dirs): return (P @ dirs.T).max(axis=0)
th = np.linspace(0, 2 * np.pi, 721)[:-1]
B2 = np.array([[1, -1, 0], [1, 1, -2]]) / np.array([[np.sqrt(2)], [np.sqrt(6)]])
dirs = np.cos(th)[:, None] * B2[0] + np.sin(th)[:, None] * B2[1]
def dH(P, Q): return np.abs(support(P, dirs) - support(Q, dirs)).max()   # Hausdorff distance of convex hulls
epsp = 0.29
W = np.array(T1(epsp))
print("d_H(K_q, W), W = T1(%.2f), q = (1-2s,s,s)" % epsp)
ss = [1 / 3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
print("a/b     " + " ".join("s=%-7.3g" % s for s in ss))
for ab in [0.05, 0.01, 0.002, 0.0004]:
    row = []
    for s in ss:
        q = np.array([1 - 2 * s, s, s])
        row.append(dH(hull_pts(q, ab, 1.0, W), W))
    print("%-7.4g " % ab + " ".join("%-9.4f" % r for r in row))
print("d_H(conv(W u e1), W) =", round(dH(np.vstack([W, E[0]]), W), 4), "(vertex model)")
# split check
rng = np.random.default_rng(0)
def f(g, a, b, W): return np.array([min(a * g[i], min(b * w @ g for w in W)) for i in range(3)])
bad = 0
for _ in range(20000):
    g = rng.normal(size=3)
    if (g > 0).all() or (g < 0).all(): continue
    c, cp = f(g, 0.01, 1, W), f(-g, 0.01, 1, W)
    if ((c + cp) > 1e-15).any(): bad += 1
print("random mixed g with some (c+c')_i > 0:", bad, "(0 means every pair split: no d-face in Delta)")

print("\nd_H(K_q, conv(W u {q})) along the same ray")
print("a/b     " + " ".join("s=%-7.3g" % s for s in ss))
for ab in [0.05, 0.01, 0.002, 0.0004]:
    row = []
    for s in ss:
        q = np.array([1 - 2 * s, s, s])
        row.append(dH(hull_pts(q, ab, 1.0, W), np.vstack([W, q])))
    print("%-7.4g " % ab + " ".join("%-9.4f" % r for r in row))
