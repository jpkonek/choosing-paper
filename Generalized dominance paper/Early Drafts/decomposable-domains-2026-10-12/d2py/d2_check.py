"""D2 NUMERICS: finite cell model of the system of Theorem D2.1 (exact rationals).

Chain coordinate x in [0,1) (world-2 measure lambda = Lebesgue in x after reparametrisation),
N_+ appended as an extra region of mass 1/4.  The "near 1" clause of K0' (delta >= 0 on
{x >= b*} for some b* < 1) is proxied by "delta >= 0 on the last scale block"; the truncation
to finitely many scale blocks is the only artefact.  No proof depends on this script.
Run: python3 -I d2_check.py
"""
from fractions import Fraction as Fr
import random, itertools, sys
import numpy as np

random.seed(20261015)

# ---------- projective planes PG(2,q), q prime ----------
def pg2(q):
    pts = []
    for v in itertools.product(range(q), repeat=3):
        if v == (0, 0, 0):
            continue
        # normalise: first nonzero coordinate = 1
        for c in v:
            if c:
                inv = pow(c, q - 2, q)
                break
        w = tuple((inv * t) % q for t in v)
        if w not in pts:
            pts.append(w)
    idx = {p: i for i, p in enumerate(pts)}
    lines = []
    for l in pts:
        lines.append(frozenset(idx[p] for p in pts if sum(a * b for a, b in zip(l, p)) % q == 0))
    return len(pts), lines

a = Fr(1, 2)
h0 = Fr(1, 4)
qs = {1: 3, 2: 5}           # level -> prime order
Ks = {1: 2, 2: 4}           # level -> number of sources
PG = {n: pg2(q) for n, q in qs.items()}
Pi = {n: PG[n][0] for n in qs}
Ls = {n: Pi[n] // Ks[n] for n in qs}

# ---------- cells ----------
cells = []   # (length, kind, data)
NLEFT = 8
for j in range(NLEFT):
    cells.append((a / NLEFT, 'L', j))
NMID = 4
for j in range(NMID):
    cells.append(((1 - h0 - a) / NMID, 'Mid', j))
blocks = [(Fr(3, 4), Fr(7, 8)), (Fr(7, 8), Fr(15, 16)), (Fr(15, 16), Fr(1))]
for bi, (lo, hi) in enumerate(blocks):
    ncell = Pi[1] * Pi[2]
    for j1 in range(Pi[1]):
        for j2 in range(Pi[2]):
            cells.append(((hi - lo) / ncell, 'B', (bi, j1, j2)))
nM = len(cells)
NN = 4
for j in range(NN):
    cells.append((Fr(1, 4) / NN, 'N', j))
nC = len(cells)
from math import lcm
DEN = 1
for c in cells: DEN = lcm(DEN, c[0].denominator)
length = [int(c[0] * DEN) for c in cells]
LEN = np.array(length, dtype=np.int64)
Midx = list(range(nM))
Nidx = list(range(nM, nC))
lastblock = [i for i in range(nM) if cells[i][1] == 'B' and cells[i][2][0] == len(blocks) - 1]
# cut boundaries (cuts allowed at cell boundaries of M); boundary k = left end of cell k
bpos = [Fr(0)]
for i in range(nM):
    bpos.append(bpos[-1] + Fr(length[i], DEN))
assert bpos[-1] == 1
a_k = NLEFT  # boundary index of x = a

# ---------- generators ----------
gens = []
for n in qs:
    K, L = Ks[n], Ls[n]
    lines = PG[n][1]
    li = 0
    for i in range(K):
        P = set(range(i * NLEFT // K, (i + 1) * NLEFT // K))
        for l in range(L):
            line = lines[li]; li += 1
            Q = set(k for k in range(nM) if cells[k][1] == 'B' and cells[k][2][n] in line)
            gens.append((n, i, l, frozenset(P), frozenset(Q)))

def vec(pos=(), neg=()):
    v = [0] * nC
    for k in pos: v[k] += 1
    for k in neg: v[k] -= 1
    return v

genvec = [vec(Q, P) for (_, _, _, P, Q) in gens]

NIDX = np.array(Nidx); LB = np.array(lastblock)
def tails(f):
    """tau_f at every M-boundary k (x = bpos[k]), including the N mass; array of length nM+1."""
    f = np.asarray(f, dtype=np.int64)
    D = int((f[NIDX] * LEN[NIDX]).sum())
    w = f[:nM] * LEN[:nM]
    t = np.empty(nM + 1, dtype=np.int64)
    t[nM] = D
    t[:nM] = D + np.cumsum(w[::-1])[::-1]
    return t

def in_K0p(f):
    f = np.asarray(f, dtype=np.int64)
    if (f[NIDX] < 0).any() or (f[LB] < 0).any():
        return False
    return bool((tails(f) >= 0).all())

GV = np.array(genvec, dtype=np.int64)
def accept(d):
    d = np.asarray(d, dtype=np.int64)
    D = int((d[NIDX] * LEN[NIDX]).sum())
    if D < 0:
        return False
    if D > 0:
        t = tails(d)
        return bool((t[a_k:] >= 0).all())
    if (d[NIDX] < 0).any():
        return False
    if in_K0p(d):
        return True
    for g in GV:
        if in_K0p(d - g):
            return True
    return False

def lam(S):
    return Fr(sum(length[k] for k in S), DEN)

def chain(b):  # c_b for boundary index b
    return set(range(b))

def err_vec(A, N):
    return [1 if (k in A or k in N) else 0 for k in range(nC)]

def delta(EX_better, EY_worse):
    """delta = 1_{E worse} - 1_{E better}; accepted <=> better <=1 worse."""
    return [y - x for x, y in zip(EX_better, EY_worse)]

def rand_model(structured):
    A = set(k for k in Midx if random.random() < random.choice([0.1, 0.3, 0.5, 0.7, 0.9]))
    if structured:
        g = random.choice(gens)
        b = random.choice([a_k, random.randrange(1, nM)])
        A = (chain(b) - set(g[3])) | set(g[4]) | set(k for k in Midx if random.random() < 0.02)
        if random.random() < 0.5:
            A -= set(k for k in A if random.random() < 0.05)
    N = set(k for k in Nidx if random.random() < 0.3) if random.random() < 0.5 else set()
    return A, N

fails = {}
def tally(name, ok):
    fails.setdefault(name, [0, 0])
    fails[name][0] += 1
    if not ok:
        fails[name][1] += 1

# T0: relevant comparisons c_a <=_1 (c_a \ P_g) u Q_g
for g, gv in zip(gens, genvec):
    tally('T0 generator comparison accepted', accept(gv))

# T6: certificate multiplicity and source cover
for n in qs:
    w = Fr(1, Ls[n])
    cover = [Fr(0)] * nC
    mult = [Fr(0)] * nC
    for (m, i, l, P, Q) in gens:
        if m != n: continue
        for k in P: cover[k] += w
        for k in Q: mult[k] += w
    tally('T6 sources cover c_a exactly once (level %d)' % n, all(cover[k] == 1 for k in range(NLEFT)))
    print('level', n, 'q', qs[n], 'K', Ks[n], 'L', Ls[n], 'max target multiplicity', max(mult),
          'bound (q+1)/L =', Fr(qs[n] + 1, Ls[n]))

# T8: pairwise intersection of all targets inside the last block
lb = set(lastblock)
ok = all((set(g[4]) & set(h[4]) & lb) for g, h in itertools.combinations(gens, 2))
tally('T8 all targets meet pairwise in the last block', ok)

# T1 (K) and T2 (U) for random models and cuts
for trial in range(1000):
    A, N = rand_model(trial % 2 == 0)
    b = random.randrange(1, nM)          # interior cut
    cb = chain(b)
    P, Q = cb - A, A - cb
    w1 = accept(delta(err_vec(cb, set()), err_vec(A, N)))
    w2 = lam(Q) <= lam(P) + lam(N)
    tally('T1 (K) competitiveness', w1 or w2)
    r1 = accept(delta(err_vec(A, N), err_vec(cb, set())))
    r2 = lam(P) + lam(N) <= lam(Q)
    tally('T2 (U) no weak domination of C_b', not (r1 and r2) or (A == cb and not N))

# T3 strict (G): nonzero delta <= 0 never accepted
for trial in range(800):
    S = [k for k in range(nC) if random.random() < random.choice([0.01, 0.1, 0.5])]
    if not S: continue
    d = vec((), S)
    tally('T3 strict (G)', not accept(d))

# T4 closure under ternary sums, on accepted deltas from structured families
def rand_accepted():
    while True:
        A, N = rand_model(random.random() < 0.6)
        B, N2 = rand_model(random.random() < 0.6)
        if random.random() < 0.5:
            b = random.randrange(0, nM + 1)
            B, N2 = chain(b), set()
        d = delta(err_vec(B, N2), err_vec(A, N))
        if accept(d):
            return d
for trial in range(300):
    d1, d2 = rand_accepted(), rand_accepted()
    s = [x + y for x, y in zip(d1, d2)]
    if all(-1 <= v <= 1 for v in s):
        tally('T4 closure under ternary sums', accept(s))
# targeted: shifted translates with disjoint sources never sum
for trial in range(200):
    g, h = random.sample(range(len(gens)), 2)
    s = [x + y for x, y in zip(genvec[g], genvec[h])]
    tally('T4b two generators never compatible', not all(-1 <= v <= 1 for v in s))

# T4c transitivity on a pool of structured models (chain models, generator models, band moves, N-models)
def band_move(A):
    A = set(A)
    src = [k for k in A if k < nM and random.random() < 0.05]
    for k in src:
        A.discard(k)
        cand = [j for j in range(k + 1, nM) if j not in A]
        if cand:
            A.add(random.choice(cand[-max(1, len(cand)//3):]))  # move right
    return A
pool = []
for b in [0, 3, a_k, 10, 30, 400, nM]:
    pool.append((chain(b), set()))
for g in random.sample(gens, 12):
    Ag = (chain(a_k) - set(g[3])) | set(g[4])
    pool.append((Ag, set()))
    pool.append((band_move(Ag), set()))
for t in range(20):
    pool.append(rand_model(t % 2 == 0))
pool.append((set(), set(Nidx[:1])))
pool.append((set(gens[0][4]), set(Nidx[:2])))
R = [[accept(delta(err_vec(*X), err_vec(*Y))) for Y in pool] for X in pool]
nt = 0
for i in range(len(pool)):
    for j in range(len(pool)):
        if not R[i][j]: continue
        for k in range(len(pool)):
            if R[j][k]:
                nt += 1
                tally('T4c transitivity on model pool', R[i][k])
print('pool size', len(pool), 'transitivity triples checked', nt)

# T7 sections: initial segments, and sup matches the formula of Lemma D2.4
def section(A, N):
    # sections are initial segments by Lemma D2.4; test on a sparse grid of cuts plus a bisection for the end
    grid = sorted(set(list(range(0, NLEFT + NMID + 1)) + list(range(NLEFT + NMID, nM + 1, 37)) + [nM]))
    acc = [b for b in grid if accept(delta(err_vec(chain(b), set()), err_vec(A, N)))]
    return grid, acc
for trial in range(60):
    A, N = rand_model(trial % 3 != 0)
    grid, S = section(A, N)
    tally('T7 section is an initial segment (sparse grid)', S == grid[:len(S)])
    if N:
        pred = min(Fr(1), a + lam(N) + lam(A - chain(a_k)))
        tally('T7b N-model section matches formula', all((bpos[b] <= pred) == (b in S) for b in grid))

print()
bad = 0
for k, (tot, f) in fails.items():
    print('%-55s %5d tests  %d failures' % (k, tot, f))
    bad += f
print('TOTAL FAILURES', bad)
sys.exit(1 if bad else 0)
