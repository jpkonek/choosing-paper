"""REFEREE round 56 (file REFEREE_round55.md), independent geometry check, exact rationals.

Own advice code (not copied from PP64/PP65).  eps = 3/10, c = (1-eps)/3, T = D_M.
D_K for a finite set of vertices K: answers +1 if k.g > 0 for all k in K, -1 if all < 0, else 0 (silent).
Rank at world w: 0 correct (answer*g_w > 0), 1 silent, 2 wrong.

Checks
 1. D' = precise (1/2,1/2,0) is strictly better and strictly worse than T at each of worlds 1,2,3,
    each on an OPEN set (witness with all relevant dot products non-zero).          [PP65 edge65]
 2. D = PP64's edge posterior K=[(16,7,0),(7,16,0)]/23 is weakly 3-worse than T on a large sample,
    strictly somewhere; and mixed at worlds 1 and 2 (open witnesses).               [PP64 Lemma 4.2]
 3. Generalised trap prerequisite (referee): for several edge models D_K, K in the edge {1,2},
    K != {e1}, there is an open set where T is 1-correct and D_K is not (strictly 1-worse), and an
    open set where it is strictly 1-better (on E near (1,1,-2)); same at world 2 for K != {e2}.
 4. g0 = (1,1,-2): T silent; posterior along a=(1,1,s) answers + iff s < 7/16.        [PP64 Prop 4.4(iii)]
 5. K0 = conv{c1+eps e1, c1+eps e2}: new answers relative to T are all 3-wrong (sample), example
    g=(1,1,-3/2) is a new answer in Q_3.                                               [PP65 Prop 2.6(c)]
Run: python3 -I -B edge_ref.py
"""
from fractions import Fraction as Fr
import random

eps = Fr(3, 10)
c = (1 - eps) / 3
M = [tuple(c + (eps if j == i else 0) for j in range(3)) for i in range(3)]
E1, E2 = (Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def DK(K, g):
    s = [dot(k, g) for k in K]
    if all(x > 0 for x in s):
        return 1
    if all(x < 0 for x in s):
        return -1
    return 0


def nondeg(K, g):
    return all(dot(k, g) != 0 for k in K)


def rank(a, g, w):
    if a == 0:
        return 1
    return 0 if a * g[w] > 0 else 2


def better(K1, K2, g, w):
    """+1 if D_K1 strictly better than D_K2 at world w (0-based) at g, -1 if worse, 0 equal."""
    r1, r2 = rank(DK(K1, g), g, w), rank(DK(K2, g), g, w)
    return (r1 < r2) - (r1 > r2)


def edge(k):
    return (Fr(k), 1 - Fr(k), Fr(0))


Dp = [edge(Fr(1, 2))]
Dint = [(Fr(16, 23), Fr(7, 23), Fr(0)), (Fr(7, 23), Fr(16, 23), Fr(0))]
K0 = [M[0], M[1]]
ok = True


def report(name, b):
    global ok
    ok &= bool(b)
    print('  %-86s %s' % (name, 'PASS' if b else 'FAIL'))


def rand_g(rng, lim=60, den=17):
    return tuple(Fr(rng.randint(-lim, lim), rng.randint(1, den)) for _ in range(3))


rng = random.Random(5655)
SAMPLE = [rand_g(rng) for _ in range(40000)]
SAMPLE += [tuple(Fr(x) for x in (a, b, cc)) for a in range(-6, 7) for b in range(-6, 7) for cc in range(-6, 7)]


def find(K1, K2, w, sign, extra=None):
    for g in SAMPLE:
        if extra is not None and not extra(g):
            continue
        if nondeg(K1, g) and nondeg(K2, g) and all(x != 0 for x in g) and better(K1, K2, g, w) == sign:
            return g
    return None


print('1. precise edge model D\' = D_(1/2,1/2,0) against T')
for w in range(3):
    gb, gw = find(Dp, M, w, +1), find(Dp, M, w, -1)
    report('world %d: open witness D\' strictly better %s, strictly worse %s' % (w + 1, gb, gw), gb is not None and gw is not None)

print('2. PP64 edge posterior D = D_[(16,7,0),(7,16,0)]/23')
bad = sum(1 for g in SAMPLE if better(Dint, M, g, 2) == +1)
report('D never strictly 3-better than T on %d samples' % len(SAMPLE), bad == 0)
report('D strictly 3-worse somewhere (open): %s' % (find(Dint, M, 2, -1),), find(Dint, M, 2, -1) is not None)
for w in (0, 1):
    gb, gw = find(Dint, M, w, +1), find(Dint, M, w, -1)
    report('world %d mixed: better %s, worse %s' % (w + 1, gb, gw), gb is not None and gw is not None)

print('3. generalised trap prerequisites for edge models D_K, K in edge {1,2}')
E0 = lambda g: (DK(M, g) == 0 and g[0] > 0 and g[1] > 0 and g[2] < 0)   # Q_3 points (T silent, worlds 1,2 agree)
for K in ([edge(Fr(1, 2))], Dint, [edge(Fr(9, 10))], [edge(Fr(1, 10)), edge(Fr(3, 10))], [edge(Fr(99, 100))]):
    lab = '[' + ','.join('%s' % k[0] for k in K) + ']'
    for w in (0, 1):
        # constructive witness: g_w = 1, g_other = -R, g_3 = G large, with R > k/(1-k) for the extreme k
        kk = min(k_[w] for k_ in K)
        R = 2 * kk / (1 - kk) + 1
        gw = [Fr(0)] * 3
        gw[w], gw[1 - w], gw[2] = Fr(1), -R, 10 * (R + 1)
        gw = tuple(gw)
        if not (nondeg(K, gw) and nondeg(M, gw) and rank(DK(M, gw), gw, w) == 0 and better(K, M, gw, w) == -1):
            gw = None
        gb = find(K, M, w, +1, extra=E0)
        report('K=%s world %d: T-correct/D_K-not open witness %s; better on Q_3 %s' % (lab, w + 1, gw, gb),
               gw is not None and gb is not None)
# explicit large-g3 construction for k close to 1 (the analytic argument of the report)
k = Fr(999, 1000)
g = (Fr(1), Fr(-1) * (k / (1 - k)) * 2, Fr(10) ** 6)
report('k=999/1000: g=(1,-2k/(1-k),1e6): T says + (1-correct), D_k says -', DK(M, g) == 1 and DK([edge(k)], g) == -1)

print('4. threshold 7/16 at g0 = (1,1,-2) along a = (1,1,s)')
g0 = (Fr(1), Fr(1), Fr(-2))
report('T silent at g0', DK(M, g0) == 0)


def post(a):
    K = []
    for m in M:
        v = tuple(ai * mi for ai, mi in zip(a, m))
        s = sum(v)
        K.append(tuple(x / s for x in v))
    return K


thr = all((DK(post((Fr(1), Fr(1), s)), g0) == 1) == (s < Fr(7, 16))
          for s in [Fr(n, 1600) for n in range(1, 1601)])
report('posterior at (1,1,s) answers + at g0 iff s < 7/16 (s = n/1600)', thr)

print('5. K0 = conv{c1+eps e1, c1+eps e2}')
gex = (Fr(1), Fr(1), Fr(-3, 2))
report('g=(1,1,-3/2): T silent, D_K0 answers +, class M_3', DK(M, gex) == 0 and DK(K0, gex) == 1)
viol = 0
for g in SAMPLE:
    t, d = DK(M, g), DK(K0, g)
    if t != 0 and d != t:
        viol += 1
    if t == 0 and d != 0 and d * g[2] > 0:
        viol += 1
report('D_K0 agrees with T where T answers; every new answer is 3-wrong (%d samples)' % len(SAMPLE), viol == 0)
print('ALL PASS' if ok else 'SOME FAIL')
