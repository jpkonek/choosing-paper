"""S34 referee: grid check of S3.4 (fibrewise band U translates fails (K)).
M = [0,1)_x * [0,1)_y on an n x ny grid (cell mass 1/(n*ny)). World 1: delta accepted iff delta - g in fband1 for g in {0} U {g_j},
g_j = 1_{A_j} - 1_{c_a}, A_j = [a,1) x Y_j (Y_j disjoint rows); fband1 = every fibre (row) has nonnegative tails in x.
World 2: mirror (heads in x), g'_j = 1_{A_j cap c_b0} - 1_{d_b0}.
Cut pair P = [b-e,b) x Y', Q = [b,b+e) x Y'' (Y', Y'' disjoint rows, equal measure). (K) needs 1_Q-1_P acc. at world 1 or
1_P-1_Q acc. at world 2. Also: the global (non-fibrewise) band accepts both, so the failure is due to fibrewise-ness.
Run: python3 -I s34_fibre.py"""
import numpy as np
n, ny = 40, 8
ia, ib0 = 10, 30
Y = [[j] for j in range(4)]           # A_j rows 0..3
def A(j):
    z = np.zeros((ny, n), int); z[Y[j], ia:] = 1; return z
def cset(k):  z = np.zeros((ny, n), int); z[:, :k] = 1; return z
def dset(k):  z = np.zeros((ny, n), int); z[:, k:] = 1; return z
g1 = [A(j) - cset(ia) for j in range(4)]
g2 = [A(j) * cset(ib0) - dset(ib0) for j in range(4)]
def ftails(d): return np.cumsum(d[:, ::-1], axis=1)[:, ::-1]
def fheads(d): return np.cumsum(d, axis=1)
def acc1(d): return any((ftails(d - g) >= 0).all() for g in [0 * d] + g1)
def acc2(d): return any((fheads(d - g) >= 0).all() for g in [0 * d] + g2)
def gband1(d): return (np.cumsum(d.sum(0)[::-1])[::-1] >= 0).all()
def gband2(d): return (np.cumsum(d.sum(0)) >= 0).all()
assert all(acc1(g) for g in g1) and all(acc2(g) for g in g2)
fails = 0; tested = 0
for b in range(ia + 2, ib0 - 2):
    for e in (1, 2):
        if b - e <= ia or b + e >= ib0: continue
        for (r1, r2) in [(4, 5), (5, 6), (6, 7), (0, 5)]:
            P = np.zeros((ny, n), int); P[r1, b - e:b] = 1
            Q = np.zeros((ny, n), int); Q[r2, b:b + e] = 1
            tested += 1
            k1 = acc1(Q - P); k2 = acc2(P - Q)
            if not (k1 or k2):
                fails += 1
                assert gband1(Q - P) and gband2(P - Q)
print(f"cut pairs tested: {tested}; (K) failures (neither world accepts its competitive comparison): {fails}")
print("in every failure the GLOBAL bands accept both comparisons (so the failure is the fibrewise restriction)")
