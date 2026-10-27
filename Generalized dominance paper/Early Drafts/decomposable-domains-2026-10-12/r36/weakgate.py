import itertools, random
from fractions import Fraction as F
import check
from check import make, keys, ranks, indic, selected

def mk_accept(weak):
    def accept(X, Y, ctx, w, Phi):
        N, U, K = ctx['N'], ctx['U'], ctx['K'][w]
        if X == Y: return True
        UX, UY = indic(ranks(X, N, U, w)), indic(ranks(Y, N, U, w))
        on, off = UY - UX, UX - UY
        if not off: return True
        if not on: return False
        if weak:
            if min(K[e] for e in on) >= min(K[e] for e in off): return False
        else:
            if max(K[e] for e in on) > min(K[e] for e in off): return False
        return Phi(X, Y, w, on, off, ctx) >= 0
    return accept

def phi_coord(X, Y, w, on, off, ctx):
    ts, mass, N = ctx['ts'], ctx['mass'], ctx['N']
    al = lambda c: (F(2) if ts[c] < F(1,2) else F(1,2)) if c < N else F(1)
    if w == 1:
        return sum(al(c)*mass[c] for (c,j) in on) - sum(mass[c] for (c,j) in off)
    return sum(mass[c] for (c,j) in on) - sum(al(c)*mass[c] for (c,j) in off)

def run(N, U, seed, weak, Phi):
    ts, mass = make(N, U, seed)
    ctx = dict(N=N, U=U, mass=mass, ts=ts, K={1: keys(ts, N, U, 1), 2: keys(ts, N, U, 2)})
    acc = mk_accept(weak)
    models = list(itertools.product('PSMC', repeat=N+U))
    cyc = 0
    for w in (1, 2):
        succ = {X: [Y for Y in models if Y != X and acc(X, Y, ctx, w, Phi)] for X in models}
        # cycle detection by DFS colouring
        col = {X: 0 for X in models}
        import sys; sys.setrecursionlimit(100000)
        def dfs(X):
            nonlocal cyc
            col[X] = 1
            for Y in succ[X]:
                if col[Y] == 1: cyc += 1
                elif col[Y] == 0: dfs(Y)
            col[X] = 2
        for X in models:
            if col[X] == 0: dfs(X)
    grid = [F(k, 64) for k in range(65)]
    comp = dom = 0
    for p in grid:
        C = selected(p, ts, N, U)
        for X in models:
            a1, a2 = acc(C, X, ctx, 1, Phi), acc(C, X, ctx, 2, Phi)
            ok = a1 if p == 1 else (a2 if p == 0 else (a1 or a2))
            comp += (not ok)
            if X != C and acc(X, C, ctx, 1, Phi) and acc(X, C, ctx, 2, Phi): dom += 1
    return dict(N=N, U=U, seed=seed, weak=weak, cycles=cyc, comp_fail=comp, dom_fail=dom)

for weak in (False, True):
    for (N,U,s) in [(3,1,1),(4,0,2),(2,2,3),(3,1,4)]:
        print(run(N,U,s,weak,phi_coord))
