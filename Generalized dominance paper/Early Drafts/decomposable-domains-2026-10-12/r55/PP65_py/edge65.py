"""PP65 edge65: exact witnesses for PP65 Prop 4.1 (the precise edge model D' = D_{(1/2,1/2,0)} is
mixed against T = D_M at every world, so committing T <=_1 D' and T <=_2 D' does not trigger rule III,
and closure stays clean; yet Def(p, X_E) is then dead by (TC)).  Exact rationals, eps = 3/10.
Run: python3 -I -B edge65.py
"""
from fractions import Fraction as Fr
import itertools, random

eps = Fr(3, 10)
c = (1 - eps) / 3
VERT = [tuple(c + (eps if j == i else 0) for j in range(3)) for i in range(3)]


def dot(m, g):
    return sum(a * b for a, b in zip(m, g))


def T(g):
    s = [dot(v, g) for v in VERT]
    if all(x > 0 for x in s):
        return 1
    if all(x < 0 for x in s):
        return -1
    return 0


def Dp(g):
    s = g[0] + g[1]
    return 1 if s > 0 else (-1 if s < 0 else 0)


def rank(adv, g, w):
    if adv == 0:
        return 1
    return 0 if adv * g[w] > 0 else 2


def cmp(g, w):
    """+1 if D' strictly better than T at w, -1 if strictly worse, 0 if equal."""
    a, b = rank(Dp(g), g, w), rank(T(g), g, w)
    return (a < b) - (a > b)


def main():
    wit = {
        'D\' better at 1 (T silent, D\' 1-correct)': ((Fr(2), Fr(-3, 2), Fr(1, 5)), 0, +1),
        'D\' worse at 1 (T silent, D\' 1-wrong)': ((Fr(-3, 2), Fr(2), Fr(1, 5)), 0, -1),
        'D\' better at 2': ((Fr(-3, 2), Fr(2), Fr(1, 5)), 1, +1),
        'D\' worse at 2': ((Fr(2), Fr(-3, 2), Fr(1, 5)), 1, -1),
        'D\' better at 3 (T silent, D\' 3-correct)': ((Fr(2), Fr(-3, 2), Fr(1, 5)), 2, +1),
        'D\' worse at 3 (T 3-correct, D\' opposite)': ((Fr(-1), Fr(-1), Fr(10)), 2, -1),
        'class M_3 point (1,1,-2): T silent, D\' = A': ((Fr(1), Fr(1), Fr(-2)), None, None),
    }
    ok = True
    for name, (g, w, want) in wit.items():
        if w is None:
            good = T(g) == 0 and Dp(g) == 1
        else:
            good = cmp(g, w) == want
        ok &= good
        print('  %-48s g=%s  %s' % (name, tuple(str(x) for x in g), 'PASS' if good else 'FAIL'))
    # face-admissibility sanity: D' answers the common sign on every sampled class-3 point
    random.seed(65)
    bad = 0
    for _ in range(20000):
        g = tuple(Fr(random.randint(-50, 50), random.randint(1, 20)) for _ in range(3))
        if g[0] * g[1] > 0 and Dp(g) * g[0] <= 0:
            bad += 1
    print('  D\' answers sign(g1)=sign(g2) wherever g1 g2 > 0 (20000 samples): %s' % ('PASS' if bad == 0 else 'FAIL'))
    ok &= bad == 0
    print('ALL PASS' if ok else 'SOME FAIL')


if __name__ == '__main__':
    main()
