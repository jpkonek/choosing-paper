# Independent exact-integer finite proxy for the D2 world-1 rule (R-, R+, R0 with base cone K0 + generators).
# Different design from the author's: levels q=3 (PG(2,3), 13 points) and q=5 (PG(2,5), 31 points),
# product sub-cells (pi1, pi2) inside each of two near-one blocks, the last block proxies "near x = 1".
# Tests: generator comparisons, strict (G) (random, incl. non-regular), transitivity on an adversarial pool,
# (K) at every cut, no weak domination of any C_b, section shape and D2.4(i) formula, D2.4(ii) union formula,
# and the sigma-finite endorsement (rho nondecreasing, huge on the last block).
import random, itertools, sys
import numpy as np

random.seed(20261015)

def pg2(q):
    pts = [(x, y, 1) for x in range(q) for y in range(q)] + [(x, 1, 0) for x in range(q)] + [(1, 0, 0)]
    P = np.array(pts)
    inc = (P @ P.T) % q == 0
    return [list(np.nonzero(inc[j])[0]) for j in range(len(pts))]

L1, L2 = pg2(3), pg2(5)   # 13 and 31 lines
P1n, P2n = 13, 31
SUB = P1n * P2n           # 403 sub-cells per block

# ---- cells (left to right), integer weights; total scale S = 16*403 = 6448 means lambda(M)=1
# c_a = [0,1/2): 4 cells of 1/8 (weight 806); [1/2,3/4): 4 cells of 1/16 (403); blocks [3/4,7/8),[7/8,1): 403 sub-cells weight 2
w = [806]*4 + [403]*4 + [2]*SUB + [2]*SUB
w = np.array(w, dtype=np.int64)
NM = len(w)
S = int(w.sum()); assert S == 6448
A_CELLS = 4                        # c_a = first 4 cells, a = 1/2
LAST0 = 8 + SUB                    # first index of last block (near-one proxy)
BLK0 = 8
NPLUS = 4; wN = np.array([403]*NPLUS, dtype=np.int64)   # N+ split into 4 sub-cells, lambda(N+) = 1/4
# boundaries t: left endpoints of cells, plus t=1 (index NM)
def tails(dM, dN):
    # tau(t_k) for t_k = left endpoint of cell k, k=0..NM (k=NM is t=1)
    v = dM * w
    rc = np.concatenate([np.cumsum(v[::-1])[::-1], [0]])
    return rc + int((dN * wN).sum())

# generators
gens = []
def subidx(p1, p2): return p1 * P2n + p2
for i in range(2):          # level 1: K=2 strips, each strip = 2 cells of c_a; L = floor(13/2)=6
    for l in range(6):
        line = L1[i*6 + l]
        P = np.zeros(NM, dtype=np.int64); P[2*i:2*i+2] = 1
        Q = np.zeros(NM, dtype=np.int64)
        for blk in (BLK0, LAST0):
            for p1 in line:
                for p2 in range(P2n):
                    Q[blk + subidx(p1, p2)] = 1
        gens.append((P, Q))
for i in range(4):          # level 2: K=4 strips = cells of c_a; L = floor(31/4)=7
    for l in range(7):
        line = L2[i*7 + l]
        P = np.zeros(NM, dtype=np.int64); P[i] = 1
        Q = np.zeros(NM, dtype=np.int64)
        for blk in (BLK0, LAST0):
            for p1 in range(P1n):
                for p2 in line:
                    Q[blk + subidx(p1, p2)] = 1
        gens.append((P, Q))
G = len(gens)
gstar = [Q - P for (P, Q) in gens]

def in_K0(fM, fN):
    if (fN < 0).any(): return False
    if (fM[LAST0:] < 0).any(): return False
    return bool((tails(fM, fN) >= 0).all())

A_IDX = A_CELLS   # tau at t=a is tails index 4
def accept(dM, dN):
    D = int((dN * wN).sum())
    if D < 0: return False
    if D > 0:
        return bool((tails(dM, dN)[A_IDX:] >= 0).all())
    if in_K0(dM, dN): return True
    return any(in_K0(dM - g, dN) for g in gstar)

def prec(X, Y):   # X <=_1 Y ; models given by (A, N) error-indicator vectors
    return accept(Y[0] - X[0], Y[1] - X[1])
def prec2(X, Y):
    lam = lambda Z: int(((1 - Z[0]) * w).sum() + (Z[1] * wN).sum())
    return lam(X) <= lam(Y)

zN = np.zeros(NPLUS, dtype=np.int64)
def C(k):  # cut model at boundary k (c_b = first k cells)
    A = np.zeros(NM, dtype=np.int64); A[:k] = 1; return (A, zN.copy())

fails = {}
def bump(key, ok):
    fails.setdefault(key, [0, 0]); fails[key][0] += 1; fails[key][1] += (not ok)

# 1. generator comparisons C_a <=_1 X_g
CA = C(A_CELLS)
for (P, Q) in gens:
    Xg = ((CA[0] - P) + Q, zN.copy())
    bump("generator comparisons accepted", prec(CA, Xg))
# pairwise meeting of targets in the last block (D2 proxy)
for g, h in itertools.combinations_with_replacement(range(G), 2):
    bump("targets meet in last block", int((gens[g][1][LAST0:] * gens[h][1][LAST0:]).sum()) > 0)

# 2. strict (G): random delta >= 0 accepted, -delta rejected
def rand_tern(p0=0.9):
    dM = np.array([0 if random.random() < p0 else random.choice((-1, 1)) for _ in range(NM)], dtype=np.int64)
    dN = np.array([0 if random.random() < 0.6 else random.choice((-1, 1)) for _ in range(NPLUS)], dtype=np.int64)
    return dM, dN
for _ in range(400):
    dM, dN = rand_tern()
    dM, dN = np.abs(dM), np.abs(dN)
    if random.random() < 0.5: dN[:] = 0
    if not dM.any() and not dN.any(): continue
    bump("(G): delta>=0 accepted", accept(dM, dN))
    bump("(G): -delta rejected", not accept(-dM, -dN))
# also nonpositive delta that equal -g* on targets (closest to generator shape)
for (P, Q) in gens:
    bump("(G): -1_Q rejected", not accept(-Q, zN))

# 3. adversarial pool for transitivity
pool = [C(k) for k in (0, 1, 2, 3, 4, 6, 8, BLK0 + 50, LAST0, LAST0 + 200, NM)]
for gi in random.sample(range(G), 10):
    P, Q = gens[gi]
    pool.append(((CA[0] - P) + Q, zN.copy()))
# chains of two generators (disjoint sources), with and without the overlap of targets
for _ in range(8):
    g, h = random.sample(range(G), 2)
    (P, Q), (P2, Q2) = gens[g], gens[h]
    if (P * P2).any(): continue
    A = np.clip(CA[0] - P - P2 + Q + Q2, 0, 1)
    pool.append((A, zN.copy()))
    # "plus base-cone packing": also move left mass right
    A2 = A.copy(); A2[5] = 1; A2[0] = 0
    pool.append((A2, zN.copy()))
# non-regular models
for _ in range(10):
    A = np.array([random.random() < 0.4 for _ in range(NM)], dtype=np.int64)
    N = np.array([random.random() < 0.5 for _ in range(NPLUS)], dtype=np.int64)
    if not N.any(): N[0] = 1
    pool.append((A, N))
for _ in range(10):
    k = random.randrange(NM)
    A = np.zeros(NM, dtype=np.int64); A[:k] = 1
    for j in random.sample(range(NM), 30): A[j] ^= 1
    pool.append((A, zN.copy()))
# models with full last block + random left (eligible for every generator)
for _ in range(6):
    A = np.array([random.random() < 0.3 for _ in range(NM)], dtype=np.int64); A[LAST0:] = 1
    pool.append((A, zN.copy()))
n = len(pool)
R = np.zeros((n, n), dtype=bool)
for i in range(n):
    for j in range(n):
        R[i, j] = prec(pool[i], pool[j])
tv = 0; tt = 0
for i in range(n):
    for j in range(n):
        if not R[i, j]: continue
        for k in range(n):
            if R[j, k]:
                tt += 1
                if not R[i, k]: tv += 1
fails["transitivity triples (pool of %d)" % n] = [tt, tv]
for i in range(n): bump("reflexive", R[i, i])

# 4. sections: initial segments; D2.4(i) formula for non-regular; D2.4(ii) formula for regular
cuts = list(range(NM + 1))
lamA_tail = lambda A, k: int((A[k:] * w[k:]).sum())
cum = np.concatenate([[0], np.cumsum(w)])
for X in pool:
    A, N = X
    sec = [prec(C(k), X) for k in cuts]
    # initial segment
    last = max([k for k in cuts if sec[k]], default=-1)
    bump("world-1 section initial segment", all(sec[:last + 1]))
    if N.any():
        psi_a = int(cum[A_CELLS]) + int((N * wN).sum()) + lamA_tail(A, A_CELLS)
        pred = [cum[k] <= min(S, psi_a) for k in cuts]
        bump("D2.4(i) formula", pred == sec)
    else:
        beta0 = int((A * w).sum())
        best = beta0 if beta0 < S else S
        for (P, Q) in gens:
            # eligibility: Q in last block contained in A
            if ((Q[LAST0:] == 1) & (A[LAST0:] == 0)).any(): continue
            u = np.concatenate([np.cumsum((A * w)[::-1])[::-1], [0]]) - np.concatenate([np.cumsum(((Q - P) * w)[::-1])[::-1], [0]])
            # beta_g = max cut index value b=cum[k] (k<NM) with (b - t)^+ <= u(t) at all boundaries t
            for k in range(LAST0, -1, -1):   # b must stay below the proxy near-one block (b* < 1)
                b = cum[k]
                if all(max(b - cum[j], 0) <= u[j] for j in range(NM + 1)):
                    best = max(best, int(b)); break
        pred = [cum[k] <= best for k in cuts]
        # the proxy near-one clause ("delta >= 0 on the last block") is faithful only for cuts b below that block
        bump("D2.4(ii) union formula (cuts below the proxy near-one block)", pred[:LAST0 + 1] == sec[:LAST0 + 1])
# 5. (K) and no weak domination, every pool model and every interior cut
for X in pool:
    for k in range(1, NM):
        Cb = C(k)
        okK = prec(Cb, X) or prec2(Cb, X)
        bump("(K) at interior cuts below the proxy near-one block" if k <= LAST0 else "(K) at cuts inside the proxy near-one block (proxy artefact expected)", okK)
        same = (X[0] == Cb[0]).all() and (X[1] == 0).all()
        if not same:
            bump("no weak domination of C_b", not (prec(X, Cb) and prec2(X, Cb)))

# 6. sigma-finite endorsement proxy: rho nondecreasing in cell order, huge (W) on the last block;
#    every accepted relevant comparison C_b <=_1 X (X regular) is endorsed.
W = 10**9
rho = np.concatenate([np.linspace(1, 3, LAST0).round().astype(np.int64), np.full(NM - LAST0, W, dtype=np.int64)])
for X in pool:
    if X[1].any(): continue
    for k in range(NM):
        Cb = C(k)
        if prec(Cb, X):
            d = X[0] - Cb[0]
            bump("rho-endorsement of relevant comparisons", int((d * w * rho).sum()) >= 0)

tot = 0
for k, (a, b) in fails.items():
    print(f"{k}: {a} tests, {b} failures"); tot += b
print("TOTAL FAILURES:", tot)
