"""H2 NUMERICS for Theorem H2.4 (mirrored D2: a two-world full system in which NEITHER world adds up).
Exact integer cell model, symmetric under x -> 1-x.  World 1 = D2's world-1 rule (end x -> 1);
world 2 = the same rule applied to the mirrored vector (end x -> 0).  "Near the end" is proxied by
"the outermost scale block" (the only artefact).  No proof depends on this script.
Run: python3 -I h2_mirrored_d2.py
"""
import itertools, random
from fractions import Fraction as Fr
from math import lcm
import numpy as np
random.seed(17)

def pg2(q):
    pts = []
    for v in itertools.product(range(q), repeat=3):
        if v == (0, 0, 0): continue
        c = next(t for t in v if t); inv = pow(c, q - 2, q)
        w = tuple((inv * t) % q for t in v)
        if w not in pts: pts.append(w)
    idx = {p: i for i, p in enumerate(pts)}
    return len(pts), [frozenset(idx[p] for p in pts if sum(x*y for x, y in zip(l, p)) % q == 0) for l in pts]

a, h0 = Fr(1, 2), Fr(1, 8)
qs, Ks = {1: 3, 2: 5}, {1: 2, 2: 4}
PG = {n: pg2(q) for n, q in qs.items()}; Pi = {n: PG[n][0] for n in qs}; Ls = {n: Pi[n] // Ks[n] for n in qs}
right_blocks = [(Fr(7, 8), Fr(15, 16)), (Fr(15, 16), Fr(31, 32)), (Fr(31, 32), Fr(1))]
cells = []                      # (lo, hi, kind, data)
for bi, (lo, hi) in reversed(list(enumerate(right_blocks))):          # mirrored blocks near 0
    L0, H0 = 1 - hi, 1 - lo; n = Pi[1] * Pi[2]
    for j in reversed(range(n)):
        j1, j2 = divmod(j, Pi[2])
        cells.append((L0 + (H0 - L0) * (n - 1 - j) / n, L0 + (H0 - L0) * (n - j) / n, "B'", (bi, j1, j2)))
for k in range(24):                                                    # strips [1/8, 7/8)
    cells.append((Fr(1, 8) + Fr(k, 32), Fr(1, 8) + Fr(k + 1, 32), 'S', k))
for bi, (lo, hi) in enumerate(right_blocks):                           # blocks near 1
    n = Pi[1] * Pi[2]
    for j in range(n):
        j1, j2 = divmod(j, Pi[2])
        cells.append((lo + (hi - lo) * j / n, lo + (hi - lo) * (j + 1) / n, 'B', (bi, j1, j2)))
nM = len(cells)
for j in range(4): cells.append((None, None, 'N', j))
nC = len(cells)
lens = [c[1] - c[0] if c[2] != 'N' else Fr(1, 16) for c in cells]
DEN = 1
for l in lens: DEN = lcm(DEN, l.denominator)
LEN = np.array([int(l * DEN) for l in lens], dtype=np.int64)
assert sum(lens[:nM]) == 1
# mirror symmetry check
mir = list(reversed(range(nM)))
assert all(LEN[i] == LEN[mir[i]] for i in range(nM))
NIDX = np.arange(nM, nC)
bnd = [Fr(0)]
for i in range(nM): bnd.append(bnd[-1] + lens[i])
a_k = bnd.index(a)
last = np.array([i for i in range(nM) if cells[i][2] == 'B' and cells[i][3][0] == 2])
# design of world 1 (sources tile c_a, targets in blocks near 1)
gens = []
for n in qs:
    K, L = Ks[n], Ls[n]; li = 0
    for i in range(K):
        P = [k for k in range(nM) if bnd[k] >= i * a / K and bnd[k + 1] <= (i + 1) * a / K]
        assert sum(lens[k] for k in P) == a / K
        for l in range(L):
            line = PG[n][1][li]; li += 1
            Q = [k for k in range(nM) if cells[k][2] == 'B' and cells[k][3][n] in line]
            g = np.zeros(nC, dtype=np.int64); g[Q] += 1; g[P] -= 1
            gens.append(g)
GV = np.array(gens)

def tails(f):
    D = int((f[NIDX] * LEN[NIDX]).sum()); w = f[:nM] * LEN[:nM]
    t = np.empty(nM + 1, dtype=np.int64); t[nM] = D; t[:nM] = D + np.cumsum(w[::-1])[::-1]; return t
def inK0(f):
    if (f[NIDX] < 0).any() or (f[last] < 0).any(): return False
    return bool((tails(f) >= 0).all())
def acc1(d):
    D = int((d[NIDX] * LEN[NIDX]).sum())
    if D < 0: return False
    if D > 0: return bool((tails(d)[a_k:] >= 0).all())
    if inK0(d): return True
    return any(inK0(d - g) for g in GV)
def mirror(d):
    e = d.copy(); e[:nM] = d[:nM][::-1]; return e
def acc2(d): return acc1(mirror(d))
ACC = {1: acc1, 2: acc2}

def errs(A, N):            # error vectors at worlds 1, 2 of the model with E_1 X ∩ M = A, unanimous errors N
    e1 = np.zeros(nC, dtype=np.int64); e1[list(A)] = 1; e1[list(N)] = 1
    e2 = np.zeros(nC, dtype=np.int64); e2[[k for k in range(nM) if k not in A]] = 1; e2[list(N)] = 1
    return {1: e1, 2: e2}
def leq(X, Y, i): return ACC[i](errs(*Y)[i] - errs(*X)[i])   # X <=_i Y
def C(b): return (set(range(b)), set())

def rand_model():
    r = random.random()
    if r < 0.3:
        A = set(k for k in range(nM) if random.random() < random.choice([.1, .3, .5, .7, .9]))
    else:
        b = random.randrange(1, nM); A = set(range(b))
        g = GV[random.randrange(len(GV))]
        if random.random() < .5: g = mirror(g)
        A = (A - set(np.where(g[:nM] < 0)[0])) | set(np.where(g[:nM] > 0)[0])
        A ^= set(k for k in range(nM) if random.random() < 0.01)
    N = set(k for k in range(nM, nC) if random.random() < .3) if random.random() < .4 else set()
    return (A, N)

tal = {}
def T(name, ok):
    tal.setdefault(name, [0, 0]); tal[name][0] += 1; tal[name][1] += (not ok)

ca = set(range(a_k)); da = set(range(nM - a_k, nM))
for g in GV:
    T('generator accepted at world 1', acc1(g)); T('mirrored generator accepted at world 2', acc2(mirror(g)))
cuts = sorted(set([random.randrange(1, nM) for _ in range(300)] + [a_k, nM - a_k]))
for trial in range(1500):
    X = rand_model(); b = random.choice(cuts); Cb = C(b)
    T('(K) competitiveness at interior cut', leq(Cb, X, 1) or leq(Cb, X, 2))
    if X[0] != Cb[0] or X[1]:
        T('no weak domination of C_b', not (leq(X, Cb, 1) and leq(X, Cb, 2)))
for trial in range(600):
    d = -np.array([1 if random.random() < .2 else 0 for _ in range(nC)], dtype=np.int64)
    if not d.any(): continue
    T('strict (G): nonzero delta<=0 rejected (w1)', not acc1(d)); T('strict (G) (w2)', not acc2(d))
pool = [rand_model() for _ in range(26)] + [C(random.choice(cuts)) for _ in range(10)]
for X, Y, Z in itertools.permutations(pool, 3):
    for i in (1, 2):
        if random.random() < 0.15 and leq(X, Y, i) and leq(Y, Z, i):
            T('transitivity w%d' % i, leq(X, Z, i))
# sections: initial segment at world 1, final segment at world 2
for trial in range(40):
    X = rand_model(); s1 = [leq(C(b), X, 1) for b in range(0, nM + 1, 37)]
    s2 = [leq(C(b), X, 2) for b in range(0, nM + 1, 37)]
    T('world-1 section is an initial segment', s1 == sorted(s1, reverse=True))
    T('world-2 section is a final segment', s2 == sorted(s2))
for k, (n, f) in sorted(tal.items()): print('%-48s tests %6d  failures %d' % (k, n, f))
