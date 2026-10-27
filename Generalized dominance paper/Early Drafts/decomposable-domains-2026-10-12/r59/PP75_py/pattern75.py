"""Pattern Lemma check (exact): patterns occurring in rec(C_a -> C_b) are exactly
{k} iff r_k > min_{i!=k} r_i  and  {!=k} iff r_k < max_{i!=k} r_i, r = b/a,
with the type sources: {k} = lost A_k u gained B_k, {!=k} = gained A_k u lost B_k.
Also checks (2V) on the disagreement cells (answers only h or S) and the 13 order types."""
import random
from fractions import Fraction as F
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geo75 import *

random.seed(75)
def rnd_near(spread):
    return tuple(F(random.randint(1000 - spread, 1000 + spread), 1000) for _ in range(3))

fails = 0; n = 0
tests = []
for _ in range(120):
    tests.append((rnd_near(150), rnd_near(150)))
# all 13 order types explicitly, around a random base
for _ in range(20):
    a = rnd_near(100)
    for r in [(1,1,1),(F(6,5),1,1),(F(5,6),1,1),(1,F(6,5),1),(1,F(5,6),1),(1,1,F(6,5)),(1,1,F(5,6)),
              (1,F(11,10),F(6,5)),(1,F(6,5),F(11,10)),(F(11,10),1,F(6,5)),(F(6,5),1,F(11,10)),(F(11,10),F(6,5),1),(F(6,5),F(11,10),1)]:
        b = tuple(a[i] * F(r[i]) for i in range(3))
        tests.append((a, b))
types_seen = set()
for a, b in tests:
    cs = cells([a, b])
    pats = set(); src = {}
    for c in cs:
        h = c['pt']
        t = htype(h)
        xa, xb = answer(a, h), answer(b, h)
        if xa != xb:
            assert t[0] != 'U'
            assert xa in ('h', 'S') and xb in ('h', 'S'), (a, b, xa, xb)   # (2V)
            P = pattern(xa, xb, h)
            pats.add(P)
            kind = ('gained' if xb == 'h' else 'lost') + ' ' + t[0] + str(t[1] + 1)
            src.setdefault(P, set()).add(kind)
    r = tuple(b[i] / a[i] for i in range(3))
    pf = pattern_formula(r)
    n += 1
    types_seen.add(order_type(r))
    if pats != pf:
        fails += 1
        print('FAIL', a, b, sorted(map(pname, pats)), sorted(map(pname, pf)))
    # type sources
    for P, kinds in src.items():
        if len(P) == 1:
            k = list(P)[0] + 1
            assert kinds <= {'lost A%d' % k, 'gained B%d' % k}, (P, kinds)
        else:
            k = [w for w in range(3) if w not in P][0] + 1
            assert kinds <= {'gained A%d' % k, 'lost B%d' % k}, (P, kinds)
print('pairs tested', n, 'order types seen', len(types_seen), sorted(types_seen))
print('Pattern Lemma failures', fails)
# guidance consequences: pointwise comparability only for single shifts
for a, b in tests[:60]:
    r = tuple(b[i] / a[i] for i in range(3))
    pf = pattern_formula(r)
    for w in range(3):
        allin = all(w in P for P in pf) and pf
        nonein = all(w not in P for P in pf) and pf
        ot = order_type(r)
        if allin: assert ot == 'raise%d' % (w + 1), (ot, w)
        if nonein: assert ot == 'lower%d' % (w + 1), (ot, w)
print('ALL PASS' if fails == 0 else 'FAILURES')
