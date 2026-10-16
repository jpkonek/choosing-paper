"""S1 referee / eu_zonoid.py -- check of the S1.10 remark: (EU_ij) holds when worlds i, j are additive with
densities > 0 on R_ij.  Discretised: R_ij = N cells with weights w_i, w_j; psi_i(A) = w_i(A), psi_j(A) = w_j(R\\A).
A set c is competitive among edge test models iff no A is strictly better at both worlds (weak Pareto).
(EU) for the edge family means: no A is weakly better at both and strictly better at one (Pareto).
We enumerate all 2^N subsets and check weak-Pareto => Pareto; then show it fails when some w_j vanishes on a cell
(so positivity of BOTH densities is needed).
Run: python3 -I eu_zonoid.py
"""
import itertools
import numpy as np


def check(wi, wj):
    N = len(wi)
    pts = []
    for mask in range(1 << N):
        A = np.array([(mask >> t) & 1 for t in range(N)], bool)
        pts.append((wi[A].sum(), wj[~A].sum()))
    pts = np.array(pts)
    eps = 1e-12
    weak_not_pareto = 0
    for x, y in pts:
        strict_better = np.any((pts[:, 0] < x - eps) & (pts[:, 1] < y - eps))
        if strict_better:
            continue                                          # not competitive
        weakly = (pts[:, 0] <= x + eps) & (pts[:, 1] <= y + eps) & \
                 ((pts[:, 0] < x - eps) | (pts[:, 1] < y - eps))
        weak_not_pareto += bool(np.any(weakly))
    return weak_not_pareto


rng = np.random.default_rng(3)
tot = 0
for trial in range(40):
    N = 10
    wi = rng.random(N) + 0.05
    wj = rng.random(N) + 0.05
    tot += check(wi, wj)
print("positive densities, 40 random instances, N = 10: competitive-but-not-Pareto sets:", tot)
wi = rng.random(10) + 0.05
wj = rng.random(10) + 0.05
wj[3] = 0.0
print("w_j = 0 on one cell: competitive-but-not-Pareto sets:", check(wi, wj))
