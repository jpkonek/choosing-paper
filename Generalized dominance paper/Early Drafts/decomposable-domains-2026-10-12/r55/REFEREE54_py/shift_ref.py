"""REFEREE54: t-uniform re-proof of PP63 Prop 2.2 (sigma_t meets D_ab in an open set for EVERY small t).

At a point g on a facet {f_v(a; g) = 0} of the answer cone A_a (the other two forms > 0), the pure shift
a_t = a o (1 + s t e_w) changes f_v by s t m_{v,w} a_w g_w (normalisation is a positive factor).  So the layer
sigma_t near g lies on the a-SILENT side if s g_w > 0 and on the a-ANSWERING side if s g_w < 0, with width ~t.
If g is off the boundary of A_b, then C_b is constant near g, and sigma_t meets D_ab = {C_a != C_b} in an open
set for every small t > 0 iff  (s g_w > 0 and b answers at g)  or  (s g_w < 0 and b is silent at g).
We search exact rational facet points for all 36 cases (ordered pairs of the kink triple, w, s).
"""
import random
from fractions import Fraction as Fr

EPS = Fr(3, 10)
C = (1 - EPS) / 3
MV = [[C + (EPS if i == j else 0) for j in range(3)] for i in range(3)]
A = [Fr(1, 3)] * 3
B = [Fr(406, 1200), Fr(421, 1200), Fr(373, 1200)]
D = [Fr(406, 1200), Fr(373, 1200), Fr(421, 1200)]
MOD = {'A': A, 'B': B, 'D': D}


def f(a, g, v):
    return sum(MV[v][j] * a[j] * g[j] for j in range(3))


def adv(a, g):
    fs = [f(a, g, v) for v in range(3)]
    return 1 if min(fs) > 0 else (-1 if max(fs) < 0 else 0)


random.seed(54)
allok = True
for an in 'ABD':
    for bn in 'ABD':
        if an == bn:
            continue
        a, b = MOD[an], MOD[bn]
        for w in range(3):
            for s in (1, -1):
                found = None
                for trial in range(20000):
                    v = random.randrange(3)
                    n = [MV[v][j] * a[j] for j in range(3)]
                    r = [Fr(random.randint(-60, 60)) for _ in range(3)]
                    lam = sum(x * y for x, y in zip(n, r)) / sum(x * x for x in n)
                    g = [r[j] - lam * n[j] for j in range(3)]
                    if f(a, g, v) != 0 or any(f(a, g, u) <= 0 for u in range(3) if u != v) or g[w] == 0:
                        continue
                    if any(f(b, g, u) == 0 for u in range(3)):
                        continue
                    if (s * g[w] > 0 and adv(b, g) == 1) or (s * g[w] < 0 and adv(b, g) == 0):
                        found = (v, g)
                        break
                ok = found is not None
                allok &= ok
                print('%s %s w=%d s=%+d: facet witness %s' % (an, bn, w + 1, s, ('facet v=%d, g=%s' % (found[0] + 1, [str(x) for x in found[1]])) if ok else 'NONE'))
print('sigma_t meets D_ab in an open set for every small t, all 36 cases:', allok)
