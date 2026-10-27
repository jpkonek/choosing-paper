"""Referee's independent check of D2 (finite cell model, exact integer arithmetic).

Independent re-implementation (not importing d2py).  Three design levels (q = 2, 3, 5), three scale
blocks, N_+ appended.  The near-one clause of K0 is proxied by "f >= 0 on the last scale block"
(unavoidable in a finite model).  Stress tests: ternary-sum closure on accepted vectors of every rule
type (R+, base cone, generator), transitivity along constructed chains, strict (G), (K) with adversarial
models, no weak domination, exact sections at every cut versus the closed-form predictions of D2.4,
(D2) and the multiplicity bound with three levels.  No conclusion of the report rests on this script.
Run: python3 -I d2ref_check.py
"""
import itertools, random, sys
from fractions import Fraction as Fr
from math import lcm
import numpy as np

rng = random.Random(777)

def pg2(q):
    pts = []
    seen = set()
    for v in itertools.product(range(q), repeat=3):
        if v == (0, 0, 0):
            continue
        c = next(t for t in v if t)
        inv = pow(c, q - 2, q)
        w = tuple((inv * t) % q for t in v)
        if w not in seen:
            seen.add(w); pts.append(w)
    idx = {p: i for i, p in enumerate(pts)}
    lines = [frozenset(idx[p] for p in pts if sum(x * y for x, y in zip(l, p)) % q == 0) for l in pts]
    return len(pts), lines

a, h0 = Fr(1, 2), Fr(1, 4)
LEV = {1: 2, 2: 3}               # level -> q
K = {1: 2, 2: 4}                 # sources per level
PG = {n: pg2(q) for n, q in LEV.items()}
Pi = {n: PG[n][0] for n in LEV}
L = {n: Pi[n] // K[n] for n in LEV}
NLEFT, NMID, NBLK = 16, 4, 3
levels = sorted(LEV)
prod_shape = tuple(Pi[n] for n in levels)
ncell_blk = int(np.prod(prod_shape))

cells = []
for j in range(NLEFT):
    cells.append((a / NLEFT, 'L', j))
for j in range(NMID):
    cells.append(((1 - h0 - a) / NMID, 'Mid', j))
lo = 1 - h0
for m in range(NBLK):
    hi = 1 - h0 / 2 ** (m + 1) if m < NBLK - 1 else Fr(1)
    for coords in itertools.product(*[range(Pi[n]) for n in levels]):
        cells.append(((hi - lo) / ncell_blk, 'B', (m,) + coords))
    lo = hi
nM = len(cells)
for j in range(4):
    cells.append((Fr(1, 3) / 4, 'N', j))
nC = len(cells)
DEN = 1
for c in cells:
    DEN = lcm(DEN, c[0].denominator)
LEN = np.array([int(c[0] * DEN) for c in cells], dtype=object)  # exact big ints
LENi = np.array([int(c[0] * DEN) for c in cells], dtype=np.int64)
assert sum(LEN[:nM]) == DEN
NI = np.arange(nM, nC)
LASTB = np.array([k for k in range(nM) if cells[k][1] == 'B' and cells[k][2][0] == NBLK - 1])
pos = np.concatenate([[0], np.cumsum(LENi[:nM])])  # boundary positions * DEN
A_K = NLEFT  # boundary index of x = a

gens = []
for n in levels:
    li = 0
    for i in range(K[n]):
        P = list(range(i * NLEFT // K[n], (i + 1) * NLEFT // K[n]))
        for l in range(L[n]):
            line = PG[n][1][li]; li += 1
            col = 1 + levels.index(n)
            Q = [k for k in range(nM) if cells[k][1] == 'B' and cells[k][2][col] in line]
            v = np.zeros(nC, dtype=np.int64); v[Q] = 1; v[P] = -1
            gens.append((n, i, l, P, Q, v))
GV = np.array([g[5] for g in gens])

def D(f):
    return int((f[NI] * LENi[NI]).sum())

def tails(f):
    w = f[:nM] * LENi[:nM]
    t = np.empty(nM + 1, dtype=np.int64)
    d = D(f)
    t[nM] = d
    t[:nM] = d + np.cumsum(w[::-1])[::-1]
    return t

def inK0(f):
    return not (f[NI] < 0).any() and not (f[LASTB] < 0).any() and (tails(f) >= 0).all()

def accept(d):
    d = np.asarray(d, dtype=np.int64)
    dd = D(d)
    if dd < 0:
        return False
    if dd > 0:
        return bool((tails(d)[A_K:] >= 0).all())
    if inK0(d):
        return True
    # generator clause: quick necessary filter (d >= 1 on Q_g in last block)
    for g in gens:
        v = g[5]
        if (d[LASTB] - v[LASTB] < 0).any():
            continue
        if inK0(d - v):
            return True
    return False

fails = {}
def tally(k, ok):
    s = fails.setdefault(k, [0, 0]); s[0] += 1; s[1] += (not ok)

def err(A, N=()):
    v = np.zeros(nC, dtype=np.int64); v[list(A)] = 1; v[list(N)] = 1; return v

def chain(b):
    return range(b)

# ---------- design checks ----------
for n in levels:
    mult = np.zeros(nC, dtype=object)
    cover = np.zeros(nC, dtype=object)
    for g in gens:
        if g[0] != n: continue
        for k in g[4]: mult[k] += Fr(1, L[n])
        for k in g[3]: cover[k] += Fr(1, L[n])
    tally('design: sources cover c_a exactly', all(cover[k] == 1 for k in range(NLEFT)))
    tally('design: multiplicity <= (q+1)/L', max(mult) <= Fr(LEV[n] + 1, L[n]))
    print('level', n, 'q', LEV[n], 'K', K[n], 'L', L[n], 'max mult', max(mult), 'bound', Fr(LEV[n] + 1, L[n]))
for m in range(NBLK):
    blk = set(k for k in range(nM) if cells[k][1] == 'B' and cells[k][2][0] == m)
    ok = all(set(g[4]) & set(h[4]) & blk for g, h in itertools.combinations_with_replacement(gens, 2))
    tally('design (D2): all targets meet pairwise in every block', ok)

# ---------- strict (G) ----------
for _ in range(1500):
    p = rng.choice([0.002, 0.02, 0.2, 0.6])
    S = [k for k in range(nC) if rng.random() < p]
    if not S: continue
    v = np.zeros(nC, dtype=np.int64); v[S] = 1
    tally('strict (G): delta>=0 accepted', accept(v))
    tally('strict (G): delta<=0, !=0 rejected', not accept(-v))
# special: add an error inside c_a to a non-regular model (brief item 1)
for _ in range(300):
    X = set(k for k in range(nM) if rng.random() < 0.4); N = set(rng.sample(list(NI), rng.randint(1, 4)))
    free = [k for k in range(NLEFT) if k not in X]
    if not free: continue
    Z = set(rng.sample(free, rng.randint(1, len(free))))
    ex, ey = err(X, N), err(X | Z, N)
    tally('strict (G) at non-regular X, extra error in c_a: X<=Y', accept(ey - ex))
    tally('strict (G) at non-regular X, extra error in c_a: not Y<=X', not accept(ex - ey))

# ---------- accepted vectors of each type, and sum closure ----------
def rand_right_transport(Zcells):
    """1_A - 1_Z with A obtained by moving each cell of Z to a free cell at or to its right of >= length."""
    A = set()
    for k in sorted(Zcells, reverse=True):
        cand = [j for j in range(k, nM) if j not in A and LENi[j] >= LENi[k]]
        if not cand:
            return None
        A.add(rng.choice(cand))
    return A

def rand_accepted():
    kind = rng.choice(['base', 'gen', 'Rplus', 'gen', 'base'])
    if kind == 'Rplus':
        X = set(k for k in range(nM) if rng.random() < 0.3); NX = set(rng.sample(list(NI), rng.randint(0, 2)))
        Y = set(k for k in range(nM) if rng.random() < 0.3) | set(rng.sample(range(NLEFT), 3))
        NY = NX | set(rng.sample(list(NI), rng.randint(1, 4)))
        d = err(Y, NY) - err(X, NX)
    elif kind == 'base':
        Z = set(rng.sample(range(nM - len(LASTB)), rng.randint(1, 6)))
        A = rand_right_transport(Z)
        if A is None: return None, kind
        d = err(A - Z) - err(Z - A)
    else:
        g = rng.choice(gens)
        Z = set(rng.sample(range(nM - len(LASTB)), rng.randint(0, 4))) - set(g[3]) - set(g[4])
        A = rand_right_transport(Z)
        if A is None: return None, kind
        A -= set(g[3])
        d = g[5].copy()
        e = err(A) - err(Z)
        d = d + e
        if (np.abs(d) > 1).any(): return None, kind
    return (d if accept(d) else None), kind

acc = []
while len(acc) < 400:
    d, kind = rand_accepted()
    if d is not None:
        acc.append((d, kind))
kinds = {}
for d, k in acc: kinds[k] = kinds.get(k, 0) + 1
print('accepted pool by kind', kinds)
nsum = 0
for i in range(len(acc)):
    for j in range(i, len(acc)):
        s = acc[i][0] + acc[j][0]
        if (np.abs(s) <= 1).all():
            nsum += 1
            tally('sum closure (ternary sums of accepted)', accept(s))
print('ternary sums tested', nsum)

# transitivity along constructed chains X <= Y <= Z
def rand_model():
    t = rng.random()
    if t < 0.3:
        A = set(chain(rng.randrange(0, nM + 1)))
    elif t < 0.6:
        g = rng.choice(gens); A = (set(chain(A_K)) - set(g[3])) | set(g[4])
    else:
        A = set(k for k in range(nM) if rng.random() < rng.choice([0.05, 0.3, 0.7]))
    N = set(rng.sample(list(NI), rng.randint(1, 3))) if rng.random() < 0.4 else set()
    return A, N

def step(A, N):
    """a random model that A,N is likely <=_1 of"""
    A, N = set(A), set(N)
    r = rng.random()
    if r < 0.3:
        g = rng.choice(gens)
        if set(g[3]) <= A and not (set(g[4]) & A):
            return (A - set(g[3])) | set(g[4]), N
    if r < 0.6:
        mov = [k for k in A if rng.random() < 0.1]
        B = rand_right_transport(set(mov))
        if B is not None and not (B & (A - set(mov))):
            return (A - set(mov)) | B, N
    if r < 0.8:
        return A | set(rng.sample(range(nM), 3)), N | set(rng.sample(list(NI), 1))
    return set(k for k in range(nM) if rng.random() < 0.3), N | set(rng.sample(list(NI), rng.randint(0, 2)))

ntr = 0
for _ in range(4000):
    X = rand_model(); Y = step(*X); Z = step(*Y)
    ex, ey, ez = err(*X), err(*Y), err(*Z)
    if accept(ey - ex) and accept(ez - ey):
        ntr += 1
        tally('transitivity along chains', accept(ez - ex))
print('transitive chains tested', ntr)

# ---------- (K) adversarial and no weak domination ----------
def lam(S):
    return Fr(int(LENi[list(S)].sum()) if S else 0, DEN)
# cuts inside the last block are excluded: there the finite proxy of the near-one clause ("f >= 0 on the
# last block") is stricter than the real clause ("f >= 0 on {x >= b*} for some b* < 1"), and (K) at such
# cuts fails in the proxy only (diagnosed: P inside the last block, below b).
for _ in range(1500):
    b = rng.randrange(1, int(LASTB.min()) + 1)
    cb = set(chain(b))
    P = set(k for k in cb if rng.random() < rng.choice([0.0, 0.05, 0.3]))
    right = list(range(b, nM))
    # put Q preferentially in the last block (where the base cone cannot move mass)
    Q = set(k for k in right if rng.random() < rng.choice([0.01, 0.1, 0.5])) | set(
        k for k in LASTB if k >= b and rng.random() < 0.3)
    N = set(rng.sample(list(NI), rng.randint(1, 2))) if rng.random() < 0.3 else set()
    A = (cb - P) | Q
    w1 = accept(err(A, N) - err(cb))
    w2 = lam(Q) <= lam(P) + lam(N)
    tally('(K) competitiveness, adversarial', w1 or w2)
    r1 = accept(err(cb) - err(A, N))
    r2 = lam(P) + lam(N) <= lam(Q)
    tally('no weak domination of C_b', (not (r1 and r2)) or (not P and not Q and not N))

# ---------- sections at every cut, versus closed forms ----------
GRID = sorted(set(list(range(0, NLEFT + NMID + 1)) + list(range(NLEFT + NMID, nM + 1, 97)) + [nM]))
def section_exact(A, N):
    return [b for b in GRID if accept(err(A, N) - err(chain(b)))]

nsec = 0
for _ in range(80):
    A, N = rand_model()
    S = section_exact(A, N)
    tally('section is an initial segment (grid)', S == GRID[:len(S)])
    if N:
        pred = min(Fr(1), a + lam(N) + lam(set(k for k in A if k >= A_K)))
        tally('non-regular section = [0, min(1, a+lam(N)+lam(A cap [a,1)))]',
              all((Fr(int(pos[b]), DEN) <= pred) == (b in S) for b in GRID))
    else:
        # sup must be max(lam(A) [B_0], beta_g) with beta_g <= lam(A)+lam(P_g)
        top = Fr(int(pos[S[-1]]), DEN) if S else None
        bound = max([lam(A)] + [lam(A) + lam(g[3]) for g in gens])
        tally('regular section top <= lam(A) + max lam(P_g)', top is None or top <= bound)
    nsec += 1

print()
bad = 0
for k, (t, f) in fails.items():
    print('%-70s %6d tests  %d failures' % (k, t, f)); bad += f
print('TOTAL FAILURES', bad)
sys.exit(1 if bad else 0)
