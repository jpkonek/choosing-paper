# Finite sanity check of the separation-gated two-world construction.
# Problems: N mixed cells (t_i) + U unanimous cells. Advice per cell in {P,S,M,C}
# (accept g, silent, accept -g, contradiction). Ranks: w1 (P0,S1,M2,C3), w2 (P2,S1,M0,C3);
# unanimous cells: correct=0 (we use advice P as correct), S1, M2, C3 at both worlds.
import itertools, random
from fractions import Fraction as F

def make(N, U, seed=0):
    rnd = random.Random(seed)
    ts = sorted(F(rnd.randint(1, 999), 1000) for _ in range(N))
    mass = [F(rnd.randint(1, 9), 1) for _ in range(N + U)]
    return ts, mass

def lfun(p):  # l(p): piecewise linear through (1/2,1/3)
    return F(2,3)*p if p <= F(1,2) else F(1,3) + F(4,3)*(p-F(1,2))
def ufun(p):
    return F(4,3)*p if p <= F(1,2) else F(2,3) + F(2,3)*(p-F(1,2))
def linv(t):
    return F(3,2)*t if t <= F(1,3) else F(1,2) + F(3,4)*(t-F(1,3))
def uinv(t):
    return F(3,4)*t if t <= F(2,3) else F(1,2) + F(3,2)*(t-F(2,3))

R1 = {'P':0,'S':1,'M':2,'C':3}
R2 = {'P':2,'S':1,'M':0,'C':3}
RU = {'P':0,'S':1,'M':2,'C':3}

def ranks(X, N, U, w):
    r = []
    for c, a in enumerate(X):
        if c < N: r.append((R1 if w == 1 else R2)[a])
        else: r.append(RU[a])
    return r

def keys(ts, N, U, w):
    # key of indicator (cell c, level j) at world w
    K = {}
    for c in range(N + U):
        for j in (1, 2, 3):
            if c < N and j in (1, 2):
                base = linv(ts[c]) if j == 1 else uinv(ts[c])
                if w == 2:  # world 2: j=1 <-> u, j=2 <-> l, reversed
                    base = 1 - (uinv(ts[c]) if j == 1 else linv(ts[c]))
                K[(c, j)] = base
            else:
                K[(c, j)] = F(-1) - F(c*3 + j, 10*(N+U)*3 + 10)  # distinct, in (-2,-1)
    return K

def indic(r):
    return {(c, j) for c, rc in enumerate(r) for j in (1, 2, 3) if rc >= j}

def accept(X, Y, ctx, w, Phi):
    N, U, mass, K = ctx['N'], ctx['U'], ctx['mass'], ctx['K'][w]
    if X == Y: return True
    UX, UY = indic(ranks(X, N, U, w)), indic(ranks(Y, N, U, w))
    on, off = UY - UX, UX - UY
    if not off: return True                       # guidance
    if not on: return False                       # pure improvement
    if max(K[e] for e in on) > min(K[e] for e in off): return False   # gate
    return Phi(X, Y, w, on, off, ctx) >= 0

def phi_sticky(X, Y, w, on, off, ctx):
    m = lambda S: sum(ctx['mass'][c] for (c, j) in S)
    return 2*m(on) - m(off)  # the note's verdict, both worlds

def selected(p, ts, N, U):
    l, u = lfun(p), ufun(p)
    X = []
    for c in range(N):
        t = ts[c]
        X.append('P' if t < l else ('M' if t > u else 'S'))
    X += ['P'] * U
    return tuple(X)

def run(N, U, seed, ntri, nriv, Phi=phi_sticky):
    ts, mass = make(N, U, seed)
    ctx = dict(N=N, U=U, mass=mass, K={1: keys(ts, N, U, 1), 2: keys(ts, N, U, 2)})
    models = list(itertools.product('PSMC', repeat=N+U))
    rnd = random.Random(seed+1)
    # (TC) / acyclicity on triples
    bad = 0
    if len(models)**3 <= 300000:
        triples = itertools.product(models, repeat=3)
    else:
        triples = ((rnd.choice(models), rnd.choice(models), rnd.choice(models)) for _ in range(ntri))
    for X, Y, Z in triples:
        for w in (1, 2):
            if accept(X, Y, ctx, w, Phi) and accept(Y, Z, ctx, w, Phi) and accept(Z, X, ctx, w, Phi):
                if not (X == Y == Z): bad += 1
    # competitiveness, undominatedness on a p-grid
    grid = [F(k, 64) for k in range(65)]
    sel = {p: selected(p, ts, N, U) for p in grid}
    comp_fail = dom_fail = 0
    rivals = models if len(models) <= 5000 else [rnd.choice(models) for _ in range(nriv)]
    for p in grid:
        C = sel[p]
        for X in rivals:
            a1, a2 = accept(C, X, ctx, 1, Phi), accept(C, X, ctx, 2, Phi)
            if p == 1: ok = a1
            elif p == 0: ok = a2
            else: ok = a1 or a2
            if not ok: comp_fail += 1
            if X != C and accept(X, C, ctx, 1, Phi) and accept(X, C, ctx, 2, Phi): dom_fail += 1
    # guidance strictness
    g_fail = 0
    for X in rivals[:2000]:
        for Y in rivals[:200]:
            for w in (1, 2):
                rX, rY = ranks(X, N, U, w), ranks(Y, N, U, w)
                if all(a <= b for a, b in zip(rY, rX)) and rY != rX:
                    if not accept(Y, X, ctx, w, Phi) or accept(X, Y, ctx, w, Phi): g_fail += 1
    return dict(N=N, U=U, seed=seed, cycles=bad, comp_fail=comp_fail, dom_fail=dom_fail, guid_fail=g_fail)

if __name__ == '__main__':
    print(run(3, 0, 1, 0, 0))
    print(run(3, 1, 2, 0, 0))
    for s in range(3):
        print(run(6, 1, 10+s, 200000, 3000))
