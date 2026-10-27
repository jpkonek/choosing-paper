"""loop57: the exact rescaling loop of BRIEF58 on the posterior family (exact rationals, complete chamber census).

For s = a^-3 in (0,1): m0 = u, m1 ~ d3 = (a,a,a^-2) ~ (1,1,s), m2 ~ d1 d3 = (a^-1,a^2,a^-1) ~ (s,1,s), m3 = u.
C_m = D_{M_m}, M_m = {m o p / m.p : p in M}.  For every ordered pair (X,Y) of loop members and every world w we
report the pointwise status: 'X>=Y' (X weakly w-better on every chamber, strictly on some), 'X<=Y', 'mixed'.
Then the forced pattern of each loop edge (C -> B repairs class k): needs C <=_k B (here: guidance?) and
C refuses B at i != k, which guidance forbids iff C is pointwise weakly i-better than B.
Also: Lemma 4.1 (pure likelihood shifts) on random interior a and all three worlds, and the toy vectors.
"""
import sys, random
sys.path.insert(0, '.')
from rlib import *

def status(cx, cy, pts, w):
    better = worse = False
    for g in pts:
        k = cls(g)
        rx, ry = rank(k, cx[g], w), rank(k, cy[g], w)
        if rx < ry: better = True
        if rx > ry: worse = True
    if better and worse: return 'mixed'
    if better: return 'X>=Y strict'
    if worse: return 'X<=Y strict'
    return 'equal'

def advmap(K, pts):
    return {g: adv(K, g) for g in pts}

print('== rescaling loop, exact chamber census ==')
for s in (F(1, 2), F(4, 5), F(19, 20), F(99, 100)):
    m = {0: (F(1), F(1), F(1)), 1: (F(1), F(1), s), 2: (s, F(1), s)}
    Ks = {i: post(m[i], VM) for i in m}
    pts, ns = chambers(list(Ks.values()))
    C = {i: advmap(Ks[i], pts) for i in m}
    print('s = a^-3 = %s : %d chambers' % (s, len(pts)))
    for (x, y) in [(0, 1), (1, 2), (2, 0), (1, 0), (2, 1), (0, 2)]:
        print('   C_m%d vs C_m%d : ' % (x, y) + '  '.join('w%d %s' % (w, status(C[x], C[y], pts, w)) for w in (1, 2, 3)))
    # forced-pattern bookkeeping for the loop edges
    for (x, y, k) in [(0, 1, 3), (1, 2, 1), (2, 0, 2)]:
        acc = status(C[x], C[y], pts, k)
        ref = [status(C[x], C[y], pts, i) for i in (1, 2, 3) if i != k]
        print('   edge C_m%d -> C_m%d (class %d): C <=_%d B by guidance: %s ; refusals at i!=%d guidance-compatible: %s'
              % (x, y, k, k, acc.startswith('X>=Y'), k, all(not r.startswith('X>=Y') and r != 'equal' for r in ref)))

print('== Lemma 4.1 on random interior a (exact) ==')
rnd = random.Random(57)
bad = 0; tested = 0
for trial in range(12):
    a = tuple(F(rnd.randint(1, 50)) for _ in range(3))
    t = F(rnd.randint(1, 40), 20)
    for w in range(3):
        b = tuple(a[i] * (1 + (t if i == w else 0)) for i in range(3))
        Ka, Kb = post(a, VM), post(b, VM)
        pts, _ = chambers([Ka, Kb])
        for g in pts:
            k = cls(g); tested += 1
            if rank(k, adv(Kb, g), w + 1) > rank(k, adv(Ka, g), w + 1): bad += 1
        st = status(advmap(Kb, pts), advmap(Ka, pts), pts, w + 1)
        assert st == 'X>=Y strict', st
print('   %d chamber comparisons, %d violations; every shift strictly w-better somewhere' % (tested, bad))

print('== toy vectors (lower loss = better; X <=_w Y iff l_w(X) <= l_w(Y)) ==')
L = {0: (0, 0, 0), 1: (-1, -1, 2), 2: (1, -2, 1)}
le = lambda x, y, w: L[x][w - 1] <= L[y][w - 1]
ok = True
for (x, y, k) in [(0, 1, 3), (1, 2, 1), (2, 0, 2)]:
    ok &= le(x, y, k)
    ok &= all(not le(x, y, i) for i in (1, 2, 3) if i != k)
print('   required source-to-defender verdicts of 3 -> 1 -> 2 realised:', ok)
# transitivity is automatic (real scores); also report the induced orders
for w in (1, 2, 3):
    print('   world %d order (best first):' % w, sorted(L, key=lambda i: L[i][w - 1]))
