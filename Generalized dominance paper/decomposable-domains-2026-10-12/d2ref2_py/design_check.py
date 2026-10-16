# Independent check of Lemma D2.2 (designs exist): projective planes PG(2,q) for q_n >= 4^n,
# incidence facts, (D2) intersection masses, (D4) multiplicity bound, exact arithmetic.
import itertools, sys
from fractions import Fraction as F
import numpy as np

def pg2(q):
    # points/lines of PG(2,q), q prime: normalised nonzero vectors in F_q^3
    pts = []
    for x in range(q):
        for y in range(q):
            pts.append((x, y, 1))
    for x in range(q):
        pts.append((x, 1, 0))
    pts.append((1, 0, 0))
    idx = {p: i for i, p in enumerate(pts)}
    P = np.array(pts, dtype=np.int64)
    inc = ((P @ P.T) % q == 0)   # inc[line, point], line coefficient vector = point vector (duality)
    lines = [np.nonzero(inc[j])[0] for j in range(len(pts))]
    return pts, lines

def next_prime(m):
    import sympy
    return sympy.nextprime(m - 1)

out = []
fail = 0
for n in (1, 2, 3):
    q = next_prime(4**n)
    pts, lines = pg2(q)
    Pi = q*q + q + 1
    assert len(pts) == Pi and len(lines) == Pi
    I = np.zeros((Pi, Pi), dtype=np.float64)
    for j, l in enumerate(lines):
        I[l, j] = 1
    # every line has q+1 points, every point on q+1 lines, two distinct lines meet in exactly 1 point
    G = np.rint(I.T @ I).astype(np.int64)  # entries <= 68, exact in float64
    ok_lines = np.all(np.diag(G) == q + 1) and np.all(G[~np.eye(Pi, dtype=bool)] == 1)
    ok_pts = np.all(I.sum(axis=1) == q + 1)
    K = 2**n
    L = Pi // K
    assert K * L <= Pi and L >= 1
    # (D4) multiplicity: assigned lines are the first K*L; at each point count assigned lines through it
    assigned = I[:, :K*L]
    mult = assigned.sum(axis=1).max()
    bound = F(int(mult), L)
    claimed = F(2*(q+1)*2**n, q*q)
    ok_bound = (F(q+1, L) >= bound) and (claimed >= F(q+1, L))
    # (D2) same level, distinct lines: Leb(Y cap Y') = 1/Pi ; same line: (q+1)/Pi
    # cross levels: product, by independence of coordinates
    out.append(f"n={n} q={q} Pi={Pi} K={K} L={L} lines_ok={ok_lines} pts_ok={ok_pts} "
               f"max_mult={mult} (q+1)/L={F(q+1,L)} = {float(F(q+1,L)):.4g} claimed_bound={float(claimed):.4g} ok={ok_bound} "
               f"lambda(Q)/h0=(q+1)/Pi={float(F(q+1,Pi)):.4g} lambda(P)/a=2^-n={2.0**-n}")
    fail += (not ok_lines) + (not ok_pts) + (not ok_bound)

# (D4) source cover: sum_{i,l} 1_{P_{n,i,l}}/L_n = 1_{c_a} exactly: each strip i has L_n generators.
for n in (1, 2, 3):
    K = 2**n
    # strips [i a/K,(i+1)a/K) partition [0,a): check with a = 1/2 at dyadic sample points
    a = F(1, 2)
    for k in range(4*K):
        x = a * F(2*k + 1, 8*K)
        cover = sum(1 for i in range(K) if i*a/K <= x < (i+1)*a/K)
        if cover != 1:
            fail += 1

# measure preservation of iota: v_n digits at positions with 2-adic valuation n-1. Exact check on all
# dyadic cylinders of depth 12: the joint law of the first digits of v_1, v_2, v_3 is uniform.
def val2(k):
    v = 0
    while k % 2 == 0:
        k //= 2; v += 1
    return v
depth = 12
from collections import Counter
cnt = Counter()
for bits in range(2**depth):
    digs = [(bits >> (depth - 1 - j)) & 1 for j in range(depth)]  # positions 1..depth
    comps = {1: [], 2: [], 3: []}
    for pos in range(1, depth + 1):
        nn = val2(pos) + 1
        if nn in comps:
            comps[nn].append(digs[pos - 1])
    key = (tuple(comps[1][:3]), tuple(comps[2][:2]), tuple(comps[3][:1]))
    cnt[key] += 1
vals = set(cnt.values())
out.append(f"iota: {len(cnt)} joint cylinders (expect 2^6=64), counts {vals} (uniform iff one value)")
fail += (len(cnt) != 64) + (len(vals) != 1)
out.append(f"FAILURES: {fail}")
print("\n".join(out))
