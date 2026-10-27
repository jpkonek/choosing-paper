"""PP65 balls65: exact check of PP65 Prop 5.1 (ball exhaustion) on a small two-valued instance.

Claim: if an inverse-closed d-open set of records refused at world w1 and another refused at a
different world w2 both contain a member-swap record rho = rec(C_a, C_a[F -> C_b]) that is mixed at
the third world k, with C_a, C_b selected interior members, then some member is undefended.
Mechanism: C_a must accept rho at k; PP66 Lemma T then refuses at k the records rho^-1|off E
(E small inside the k-improving part), which lie in both balls and are realised out of C_b.

Instance: cells (mass), the set of worlds at which h is correct, (C_a, C_b):
  x  (2)  h correct at {3}      (h, S)    F
  y1 (1)  h correct at {1,2}    (h, S)    F
  y2 (1)  h correct at {1,2}    (h, S)    F
  z  (1)  h correct at {1}      (S, h)    off F (so X != C_b)
  c  (1)  h correct at {1,2,3}  (h, h)
All 32 {h,S}-models.  Axioms: reflexivity, strict (G), (IB) (verdicts on records), (TC) on all
ordered triples at all worlds, defence of C_a and C_b on {1,2,3} against every model, direct (C)
for C_a, C_b against every other model (all others treated as incoherent), undominatedness of
C_a vs C_b.  Balls: every instance record within d < delta of rho or of rho^-1 is refused at
the ball's world.  Run: python3 -I -B balls65.py
"""
import itertools
from pysat.solvers import Cadical153

CELLS = ['x', 'y1', 'y2', 'z', 'c']
MASS = {'x': 2, 'y1': 1, 'y2': 1, 'z': 1, 'c': 1}
COR = {'x': {3}, 'y1': {1, 2}, 'y2': {1, 2}, 'z': {1}, 'c': {1, 2, 3}}
CA = ('h', 'h', 'h', 'S', 'h')
CB = ('S', 'S', 'S', 'h', 'h')
F = {'x', 'y1', 'y2'}
W = (1, 2, 3)
MODELS = list(itertools.product('hS', repeat=len(CELLS)))
X = tuple(CB[n] if CELLS[n] in F else CA[n] for n in range(len(CELLS)))


def rank(c, a, w):
    if a == 'S':
        return 1
    return 0 if w in COR[c] else 2


def rec(P, Q):
    return tuple((CELLS[n], P[n], Q[n]) for n in range(len(CELLS)) if P[n] != Q[n])


def inv(r):
    return tuple((c, n, o) for (c, o, n) in r)


def dist(r, s):
    a, b = dict((c, (o, n)) for c, o, n in r), dict((c, (o, n)) for c, o, n in s)
    return sum(MASS[c] for c in CELLS if a.get(c) != b.get(c))


VAR = {}


def v(r, w):
    return VAR.setdefault((r, w), len(VAR) + 1)


def clauses(balls):
    cl, recs = [], set()
    for P in MODELS:
        for Q in MODELS:
            if P != Q:
                recs.add(rec(P, Q))
    for r in recs:
        for w in W:
            if all(rank(c, o, w) <= rank(c, n, w) for c, o, n in r):
                cl += [[v(r, w)], [-v(inv(r), w)]]
    for P, Q, R in itertools.permutations(MODELS, 3):
        a, b, c = rec(P, Q), rec(Q, R), rec(R, P)
        for w in W:
            for rr in (inv(a), inv(b), inv(c)):
                cl.append([-v(a, w), -v(b, w), -v(c, w), v(rr, w)])
    for S_ in (CA, CB):
        for P in MODELS:
            if P == S_:
                continue
            cl.append([v(rec(S_, P), w) for w in W])            # defence on {1,2,3}
            if P not in (CA, CB):
                cl.append([-v(rec(P, S_), w) for w in W])       # direct (C), incoherent rival
    for S_, P in ((CA, CB), (CB, CA)):
        for w2 in W:
            cl.append([-v(rec(P, S_), w) for w in W] + [v(rec(S_, P), w2)])
    rho = rec(CA, X)
    for (w, delta) in balls:
        for r in recs:
            if dist(r, rho) < delta or dist(r, inv(rho)) < delta:
                cl.append([-v(r, w)])
    return cl


def run(balls):
    s = Cadical153(bootstrap_with=clauses(balls))
    return s.solve()


def main():
    rho = rec(CA, X)
    mixed3 = any(rank(c, o, 3) > rank(c, n, 3) for c, o, n in rho) and any(rank(c, o, 3) < rank(c, n, 3) for c, o, n in rho)
    print('rho =', rho, ' mixed at world 3:', mixed3)
    tests = [
        ('no balls (control)', [], True),
        ('one inverse-closed ball at world 1, delta=1.5', [(1, 1.5)], True),
        ('balls at worlds 1 and 1 (same world), delta=1.5', [(1, 1.5), (1, 1.5)], True),
        ('balls at worlds 1 and 2 (different), delta=1.5', [(1, 1.5), (2, 1.5)], False),
        ('balls at worlds 1 and 2, delta=0.5 (centres only: rho, rho^-1)', [(1, 0.5), (2, 0.5)], True),
    ]
    allok = True
    for name, balls, expect in tests:
        got = run(balls)
        ok = (got == expect)
        allok &= ok
        print('  %-66s %s (expected %s)  %s' % (name, 'SAT' if got else 'UNSAT', 'SAT' if expect else 'UNSAT', 'PASS' if ok else 'FAIL'))
    print('ALL PASS' if allok else 'SOME FAIL')


if __name__ == '__main__':
    main()
