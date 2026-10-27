"""REFEREE54: independent re-check of PP63 Theorem J's kite certificate (exact Fractions).

Own implementation of the posterior advice: C_a answers +g iff (m_v * a) . g > 0 for every vertex m_v of
M = c*1 + eps*Delta (c = (1-eps)/3, eps = 3/10); answers -g iff all < 0; silent otherwise.
Checks, at scales 1e-3 and 1e-6: (i) every one of the 7 bipartitions {answerers, silent} of the four kite
points is realised by a problem g, with all 12 inequalities strict (so on an open cone); (ii) the answerers
share one sign; (iii) (2V) at every kite point; (iv) g has mixed signs (g in the disagreement region).
"""
from fractions import Fraction as Fr
from itertools import combinations

EPS = Fr(3, 10)
C = (1 - EPS) / 3
MV = [[C + (EPS if i == j else 0) for j in range(3)] for i in range(3)]
U = [Fr(1, 3)] * 3


def forms(a, g):
    return [sum(MV[v][j] * a[j] * g[j] for j in range(3)) for v in range(3)]


def adv(a, g):
    f = forms(a, g)
    if min(f) > 0:
        return 1
    if max(f) < 0:
        return -1
    return 0


def twoV(a):
    inv = [1 / x for x in a]
    s = sum(inv)
    return all(x / s >= C for x in inv)


OFF = [(Fr(-1, 10), Fr(-1, 10), Fr(1, 5)), (Fr(27, 5), Fr(-33, 5), Fr(6, 5)),
       (Fr(-11, 10), Fr(-11, 10), Fr(11, 5)), (Fr(-33, 5), Fr(27, 5), Fr(6, 5))]


def problems(sc):
    # the certificate problems printed in kite63.out, as functions of the scale where they depend on it
    if sc == Fr(1, 1000):
        G = [('-90189/3500', '-90189/3500', '179811/8000'), ('-11277/1000', '-7554/875', '4278/125'),
             ('-7', '-7', '23'), ('-44973/4000', '-2139/250', '60027/1750'),
             ('-74973/8000', '12861/500', '-2139/500'), ('-90459/3500', '-90459/3500', '179541/8000'),
             ('-45243/4000', '-15243/1750', '59757/1750')]
    else:
        G = [('-90000189/3500000', '-90000189/3500000', '179999811/8000000'),
             ('-11250027/1000000', '-3750027/437500', '14999973/437500'), ('-7', '-7', '23'),
             ('-44999973/4000000', '-14999973/1750000', '60000027/1750000'),
             ('-74999973/8000000', '90000027/3500000', '-14999973/3500000'),
             ('-90000459/3500000', '-90000459/3500000', '179999541/8000000'),
             ('-45000243/4000000', '-15000243/1750000', '59999757/1750000')]
    return [tuple(Fr(x) for x in g) for g in G]


allok = True
for sc in (Fr(1, 1000), Fr(1, 10 ** 6)):
    P = [[U[j] + sc * o[j] for j in range(3)] for o in OFF]
    ok2v = all(twoV(p) and abs(sum(p) - 1) == 0 for p in P)
    want = set()
    for r in (1, 2):
        for S in combinations(range(4), r):
            T = tuple(sorted(set(range(4)) - set(S)))
            want.add(frozenset([S, T]))
    got = set()
    strict = True
    signs_ok = True
    mixed = True
    for g in problems(sc):
        A = tuple(i for i in range(4) if adv(P[i], g) != 0)
        Sil = tuple(i for i in range(4) if adv(P[i], g) == 0)
        if not A or not Sil:
            continue
        got.add(frozenset([A, Sil]))
        strict &= all(x != 0 for p in P for x in forms(p, g))
        signs_ok &= len({adv(P[i], g) for i in A}) == 1
        mixed &= (max(g) > 0 > min(g))
    print('scale', sc, ': (2V) at kite points', ok2v, '; bipartitions realised', len(got & want), 'of', len(want),
          '; all forms nonzero (open cones)', strict, '; one answer sign', signs_ok, '; mixed-sign problems', mixed)
    allok &= ok2v and got == want and strict and signs_ok and mixed
print('KITE RE-CHECK:', 'PASS' if allok else 'FAIL')
