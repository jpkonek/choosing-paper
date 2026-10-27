"""REFEREE round 56: independent SAT check of PP65 Prop 5.1 (two d-open inverse-closed refusal
sets at different worlds sharing a member-swap record exhaust a member), on an instance different
from balls65 (four F-cells, one of them correct at a single world; all single balls tested).

Cells (mass, worlds where h is correct), (C_a, C_b):
  x  (2, {3})    (h, S)  F
  y1 (1, {1,2})  (h, S)  F
  y2 (1, {1,2})  (h, S)  F
  t  (2, {1})    (h, S)  F
  z  (1, {1,2})  (S, h)  off F
rho = rec(C_a, X), X = C_a[F -> C_b] = (F: h -> S).  With delta = 1.5 both parts F_w^+ and F_w^-
have mass >= 2 > delta at every world (robust mixing, PP66), so ball refusals never contradict
guidance; the 3-improving part contains the mass-1 atom y1 (mu(E) = 1 < delta), so Prop 5.1
applies to the pair of worlds {1, 2}.  (A first version of this check used masses violating
robust mixing at world 3; a single ball there was then UNSAT for that reason alone.)
Axioms: reflexivity, strict (G), (IB) (record variables), (TC) on all ordered triples, defence of
C_a and C_b on {1,2,3}, direct (C) against incoherent models, undominatedness between C_a, C_b.
Run: python3 -I -B balls_ref.py
"""
import itertools
from pysat.solvers import Cadical153

CELLS = ['x', 'y1', 'y2', 't', 'z']
MASS = dict(x=2, y1=1, y2=1, t=2, z=1)
COR = dict(x={3}, y1={1, 2}, y2={1, 2}, t={1}, z={1, 2})
CA = ('h', 'h', 'h', 'h', 'S')
CB = ('S', 'S', 'S', 'S', 'h')
FS = {'x', 'y1', 'y2', 't'}
W = (1, 2, 3)
MODELS = list(itertools.product('hS', repeat=5))
X = tuple(CB[i] if CELLS[i] in FS else CA[i] for i in range(5))


def rank(c, a, w):
    return 1 if a == 'S' else (0 if w in COR[c] else 2)


def rec(P, Q):
    return frozenset((CELLS[i], P[i], Q[i]) for i in range(5) if P[i] != Q[i])


def inv(r):
    return frozenset((c, y, x) for c, x, y in r)


def dist(r, s):
    a = {c: (x, y) for c, x, y in r}
    b = {c: (x, y) for c, x, y in s}
    return sum(MASS[c] for c in CELLS if a.get(c) != b.get(c))


var = {}
v = lambda r, w: var.setdefault((r, w), len(var) + 1)


def clauses(balls):
    cl = []
    recs = {rec(P, Q) for P in MODELS for Q in MODELS if P != Q}
    for r in recs:
        for w in W:
            if all(rank(c, x, w) <= rank(c, y, w) for c, x, y in r):
                cl += [[v(r, w)], [-v(inv(r), w)]]
    for P, Q, R in itertools.permutations(MODELS, 3):
        a, b, c = rec(P, Q), rec(Q, R), rec(R, P)
        for w in W:
            for rr in (a, b, c):
                cl.append([-v(a, w), -v(b, w), -v(c, w), v(inv(rr), w)])
    for S in (CA, CB):
        for P in MODELS:
            if P == S:
                continue
            cl.append([v(rec(S, P), w) for w in W])
            if P not in (CA, CB):
                cl.append([-v(rec(P, S), w) for w in W])
    for S, P in ((CA, CB), (CB, CA)):
        for w2 in W:
            cl.append([-v(rec(P, S), w) for w in W] + [v(rec(S, P), w2)])
    rho = rec(CA, X)
    for (w, d2) in balls:                 # d2 = 2*delta
        for r in recs:
            if 2 * dist(r, rho) < d2 or 2 * dist(r, inv(rho)) < d2:
                cl.append([-v(r, w)])
    return cl


ok = True
for name, balls, expect in [
        ('no balls', [], True),
        ('one ball, world 1, delta 1.5', [(1, 3)], True),
        ('one ball, world 2, delta 1.5', [(2, 3)], True),
        ('one ball, world 3, delta 1.5', [(3, 3)], True),
        ('two balls, both at world 1', [(1, 3), (1, 3)], True),
        ('balls at 1 and 2 (Prop 5.1, k = 3, E = y1)', [(1, 3), (2, 3)], False),
        ('centres only at 1 and 2 (delta 0.5)', [(1, 1), (2, 1)], True),
        ('centres only at 1, 2 and 3 (direct exhaustion)', [(1, 1), (2, 1), (3, 1)], False)]:
    s = Cadical153(bootstrap_with=clauses(balls))
    got = s.solve()
    s.delete()
    good = got == expect
    ok &= good
    print('  %-44s %s (expected %s) %s' % (name, 'SAT' if got else 'UNSAT', 'SAT' if expect else 'UNSAT', 'PASS' if good else 'FAIL'))
print('ALL PASS' if ok else 'SOME FAIL')
