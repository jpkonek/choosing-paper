# F1 (C): exact-integer finite proxy of D2' (the D2 rule with the near-one clause restricted to a window W, sources in a
# proper part S of c_a, targets inside W).  Each near-one block contains W sub-cells (product cells (pi1,pi2) of
# PG(2,3) x PG(2,5)) and interleaved non-W cells at the same "x-level" (proxy for the M+ fibre near the ray (1,0) in
# host A, or for radii outside the annulus).  The last block proxies "x near 1"; the clause is "f >= 0 on the W cells
# of the last block".  Tests: generator comparisons, strict (G), transitivity on an adversarial pool, sections
# (initial segments, D2.4(i) formula, D2.4(ii) union formula with W-eligibility), (K), no weak domination, sigma-finite
# endorsement by a nondecreasing rho, and REJECTION of a rho that is heavy on W but not on the non-W cells at the same
# x-levels (the coupling that forces blow-up at the interior ray in host A).
import random, itertools
import numpy as np
random.seed(20261015)
def pg2(q):
    pts = [(x, y, 1) for x in range(q) for y in range(q)] + [(x, 1, 0) for x in range(q)] + [(1, 0, 0)]
    P = np.array(pts); inc = (P @ P.T) % q == 0
    return [list(np.nonzero(inc[j])[0]) for j in range(len(pts))]
L1, L2 = pg2(3), pg2(5); P1n, P2n = 13, 31; SUB = P1n * P2n
NONW_POS = (100, 200, 300)           # positions (within a block) of the 3 interleaved non-W cells
def block():
    cells, isW, sub = [], [], []
    k = 0
    for j in range(SUB + len(NONW_POS)):
        if j in [p + i for i, p in enumerate(NONW_POS)]:
            cells.append(100); isW.append(False); sub.append(-1)
        else:
            cells.append(2); isW.append(True); sub.append(k); k += 1
    return cells, isW, sub
wl, Wl, subl = [], [], []
for c in [806] * 4 + [403] + [403] * 3:     # 4 source cells (S), 1 non-source cell of c_a, 3 middle cells
    wl.append(c); Wl.append(False); subl.append(-1)
BLK0 = len(wl)
for _ in range(2):
    c, i, s = block(); wl += c; Wl += i; subl += s
LAST0 = BLK0 + SUB + len(NONW_POS)
w = np.array(wl, dtype=np.int64); isW = np.array(Wl); sub = np.array(subl)
NM = len(w); S_TOT = int(w.sum())
A_IDX = 5                                   # c_a = first 5 cells
NPLUS = 4; wN = np.array([403] * NPLUS, dtype=np.int64)
lastW = np.zeros(NM, dtype=bool); lastW[LAST0:] = isW[LAST0:]
def tails(dM, dN):
    v = dM * w
    return np.concatenate([np.cumsum(v[::-1])[::-1], [0]]) + int((dN * wN).sum())
def Wcells_of(lineset, coord):
    Q = np.zeros(NM, dtype=np.int64)
    for j in range(BLK0, NM):
        if sub[j] >= 0:
            p1, p2 = divmod(int(sub[j]), P2n)
            if (p1 if coord == 1 else p2) in lineset: Q[j] = 1
    return Q
gens = []
for i in range(2):
    for l in range(6):
        P = np.zeros(NM, dtype=np.int64); P[2 * i:2 * i + 2] = 1
        gens.append((P, Wcells_of(set(L1[i * 6 + l]), 1)))
for i in range(4):
    for l in range(7):
        P = np.zeros(NM, dtype=np.int64); P[i] = 1
        gens.append((P, Wcells_of(set(L2[i * 7 + l]), 2)))
G = len(gens); gstar = [Q - P for (P, Q) in gens]
assert all((Q[~isW] == 0).all() for _, Q in gens)
def in_K0(fM, fN):
    if (fN < 0).any(): return False
    if (fM[lastW] < 0).any(): return False
    return bool((tails(fM, fN) >= 0).all())
def accept(dM, dN):
    D = int((dN * wN).sum())
    if D < 0: return False
    if D > 0: return bool((tails(dM, dN)[A_IDX:] >= 0).all())
    if in_K0(dM, dN): return True
    return any(in_K0(dM - g, dN) for g in gstar)
prec = lambda X, Y: accept(Y[0] - X[0], Y[1] - X[1])
lam2 = lambda Z: int(((1 - Z[0]) * w).sum() + (Z[1] * wN).sum())
prec2 = lambda X, Y: lam2(X) <= lam2(Y)
zN = np.zeros(NPLUS, dtype=np.int64)
def C(k):
    A = np.zeros(NM, dtype=np.int64); A[:k] = 1; return (A, zN.copy())
fails = {}
def bump(key, ok):
    fails.setdefault(key, [0, 0]); fails[key][0] += 1; fails[key][1] += (not ok)
CA = C(A_IDX)
for (P, Q) in gens:
    bump("generator comparisons C_a <=_1 X_g accepted", prec(CA, ((CA[0] - P) + Q, zN.copy())))
for g, h in itertools.combinations_with_replacement(range(G), 2):
    bump("targets meet in W of last block (D2')", int((gens[g][1] * gens[h][1] * lastW).sum()) > 0)
# strict (G)
for _ in range(500):
    dM = np.array([0 if random.random() < 0.9 else 1 for _ in range(NM)], dtype=np.int64)
    dN = np.array([0 if random.random() < 0.6 else 1 for _ in range(NPLUS)], dtype=np.int64)
    if random.random() < 0.5: dN[:] = 0
    if not dM.any() and not dN.any(): continue
    bump("(G): delta>=0 accepted", accept(dM, dN)); bump("(G): -delta rejected", not accept(-dM, -dN))
for (P, Q) in gens: bump("(G): -1_Q rejected", not accept(-Q, zN))
# pool
pool = [C(k) for k in (0, 1, 2, 4, 5, 6, 8, BLK0 + 57, BLK0 + 250, LAST0, LAST0 + 101, LAST0 + 300, NM)]
for gi in random.sample(range(G), 12):
    P, Q = gens[gi]; pool.append(((CA[0] - P) + Q, zN.copy()))
for _ in range(10):
    g, h = random.sample(range(G), 2); (P, Q), (P2, Q2) = gens[g], gens[h]
    if (P * P2).any(): continue
    A = np.clip(CA[0] - P - P2 + Q + Q2, 0, 1); pool.append((A, zN.copy()))
    A2 = A.copy(); A2[6] = 1; A2[4] = 0; pool.append((A2, zN.copy()))
    # move the target overlap into a non-W cell of the last block (allowed transport? it is not: overlap in W)
    A3 = A.copy(); j = LAST0 + 100 + 0; A3[j] = 1; pool.append((A3, zN.copy()))
for _ in range(8):   # generator model with mass moved from non-W last-block cells to the left (non-W is unprotected)
    gi = random.randrange(G); P, Q = gens[gi]; A = (CA[0] - P) + Q
    for p in NONW_POS: A[LAST0 + p + NONW_POS.index(p)] = 1
    pool.append((A.copy(), zN.copy())); B = A.copy(); B[LAST0 + 100] = 0; B[5] = 1; pool.append((B, zN.copy()))
for _ in range(10):
    A = np.array([random.random() < 0.4 for _ in range(NM)], dtype=np.int64)
    N = np.array([random.random() < 0.5 for _ in range(NPLUS)], dtype=np.int64)
    if not N.any(): N[0] = 1
    pool.append((A, N))
for _ in range(10):
    k = random.randrange(NM); A = np.zeros(NM, dtype=np.int64); A[:k] = 1
    for j in random.sample(range(NM), 30): A[j] ^= 1
    pool.append((A, zN.copy()))
for _ in range(6):
    A = np.array([random.random() < 0.3 for _ in range(NM)], dtype=np.int64); A[LAST0:] = 1; pool.append((A, zN.copy()))
n = len(pool)
R = np.array([[prec(pool[i], pool[j]) for j in range(n)] for i in range(n)])
tt = tv = 0
for i in range(n):
    for j in range(n):
        if R[i, j]:
            for k in range(n):
                if R[j, k]:
                    tt += 1; tv += (not R[i, k])
fails["transitivity triples (pool of %d)" % n] = [tt, tv]
cuts = list(range(NM + 1)); cum = np.concatenate([[0], np.cumsum(w)])
for X in pool:
    A, N = X
    sec = [prec(C(k), X) for k in cuts]
    last = max([k for k in cuts if sec[k]], default=-1)
    bump("world-1 section is an initial segment", all(sec[:last + 1]))
    if N.any():
        psi = int(cum[A_IDX]) + int((N * wN).sum()) + int((A[A_IDX:] * w[A_IDX:]).sum())
        bump("D2.4(i) formula (non-regular)", [cum[k] <= min(S_TOT, psi) for k in cuts] == sec)
    else:
        best = int((A * w).sum())
        uA = np.concatenate([np.cumsum((A * w)[::-1])[::-1], [0]])
        for (P, Q) in gens:
            if ((Q == 1) & lastW & (A == 0)).any(): continue          # W-eligibility
            u = uA - np.concatenate([np.cumsum(((Q - P) * w)[::-1])[::-1], [0]])
            for k in range(LAST0, -1, -1):
                b = cum[k]
                if all(max(b - cum[j], 0) <= u[j] for j in range(NM + 1)):
                    best = max(best, int(b)); break
        pred = [cum[k] <= best for k in cuts]
        bump("D2.4(ii) union formula (cuts up to the proxy block)", pred[:LAST0 + 1] == sec[:LAST0 + 1])
for X in pool:
    for k in range(1, LAST0 + 1):
        Cb = C(k); bump("(K) at interior cuts up to the proxy block", prec(Cb, X) or prec2(Cb, X))
        if not ((X[0] == Cb[0]).all() and (X[1] == 0).all()):
            bump("no weak domination of C_b", not (prec(X, Cb) and prec2(X, Cb)))
# sigma-finite endorsement: rho nondecreasing along x, huge on the whole last block (W and non-W alike)
def endorses(rho, X, Y):   # X <=_1 Y endorsed by rho (regular models): rho(E1 X) <= rho(E1 Y)
    return int((X[0] * w * rho).sum()) <= int((Y[0] * w * rho).sum())
rho_mono = np.ones(NM, dtype=np.int64); rho_mono[BLK0:LAST0] = 3; rho_mono[LAST0:] = 10 ** 9
rho_split = rho_mono.copy(); rho_split[BLK0:][~isW[BLK0:]] = 1     # heavy on W only, light on non-W at same levels
cutpool = [C(k) for k in range(0, LAST0 + 1, 7)]
relcount = 0; bad_mono = 0; bad_split = 0
for Cb in cutpool:
    for X in pool:
        if X[1].any(): continue
        if prec(Cb, X):
            relcount += 1; bad_mono += (not endorses(rho_mono, Cb, X)); bad_split += (not endorses(rho_split, Cb, X))
# explicit cut moves W -> non-W at a cut inside block 1 (relevant, accepted by (K))
for p in NONW_POS:
    k = BLK0 + p + NONW_POS.index(p)            # index of the non-W cell; cut just before it
    Cb = C(k); A = Cb[0].copy(); A[k - 49:k] = 0; A[k] = 1  # trade 49 W cells (mass 98) left of the cut for the non-W cell (mass 100)
    X = (A, zN.copy())
    if prec(Cb, X):
        relcount += 1; bad_mono += (not endorses(rho_mono, Cb, X)); bad_split += (not endorses(rho_split, Cb, X))
fails["relevant comparisons endorsed by nondecreasing rho (%d tested)" % relcount] = [relcount, bad_mono]
fails["W-only-heavy rho: relevant comparisons it FAILS to endorse (expected > 0)"] = [relcount, bad_split]
w_ = max(len(k) for k in fails)
for k, (t, f) in fails.items(): print("%-*s  tests %7d  failures %d" % (w_, k, t, f))
