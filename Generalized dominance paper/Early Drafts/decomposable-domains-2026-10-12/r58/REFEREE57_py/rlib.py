"""rlib: referee's own exact geometry (round 58 referee of round 57).  Independent of geom69/geom70/geom71.

Problems g in R^3 mod sign.  D_K (K = finite vertex list in the simplex) answers s*g (s = +-1) iff
s * k.g > 0 for every vertex k; silent otherwise.  Class k: g_k's sign differs from the other two;
A = majority-sign answer (correct at the two worlds != k), B = opposite (correct at world k).
Unanimous problems: every K inside the open simplex answers correctly; class 0.
Chamber census: every open chamber of the central arrangement {n.g = 0} (n over coordinate vectors and all
vertices) found by LP feasibility over ALL sign vectors (complete by construction), exact point verified.
"""
from fractions import Fraction as F
import itertools
import numpy as np
from scipy.optimize import linprog

def dot(a, b): return sum(x * y for x, y in zip(a, b))
def sgn(x): return (x > 0) - (x < 0)

def cls(g):
    s = [sgn(x) for x in g]
    if 0 in s: return None
    if s[0] == s[1] == s[2]: return 0
    for k in range(3):
        o = [s[j] for j in range(3) if j != k]
        if o[0] == o[1]: return k + 1

def majsign(g):
    k = cls(g)
    return sgn(g[1]) if k == 1 else sgn(g[0])

def adv(K, g):
    """'A','B','S' at a mixed problem; 'C' (correct) at unanimous ones (checked)."""
    vals = [dot(v, g) for v in K]
    k = cls(g)
    if k == 0:
        assert all(sgn(x) == sgn(g[0]) for x in vals)
        return 'C'
    m = majsign(g)
    if all(m * x > 0 for x in vals): return 'A'
    if all(m * x < 0 for x in vals): return 'B'
    return 'S'

def rank(k, a, w):
    if a == 'C': return 0
    if a == 'S': return 1
    if a == 'X': return 3
    corr = 'B' if k == w else 'A'
    return 0 if a == corr else 2

def normals_of(Ks):
    ns = [(F(1),F(0),F(0)), (F(0),F(1),F(0)), (F(0),F(0),F(1))]
    for K in Ks:
        for v in K:
            v = tuple(F(x) for x in v)
            # skip parallel duplicates
            if any(all(v[i]*n[j] == v[j]*n[i] for i in range(3) for j in range(3)) for n in ns):
                continue
            ns.append(v)
    return ns

def chambers(Ks):
    """exact interior point of every open chamber (one per sign vector, mod global sign)"""
    ns = normals_of(Ks)
    A = np.array([[float(x) for x in n] for n in ns])
    pts = []
    nn = len(ns)
    for bits in itertools.product((1, -1), repeat=nn - 1):
        s = (1,) + bits
        S = np.array(s, dtype=float)
        # s_j n_j.g >= 1  <=>  -(s_j n_j).g <= -1
        res = linprog(np.zeros(3), A_ub=-(S[:, None] * A), b_ub=-np.ones(nn), bounds=[(-1e4, 1e4)] * 3,
                      method='highs')
        if res.status != 0:
            continue
        x = res.x
        ok = False
        for den in (10**3, 10**5, 10**7):
            g = tuple(F(round(xi * den)) / den for xi in x)
            if all(sgn(dot(n, g)) == sj for n, sj in zip(ns, s)):
                ok = True
                break
        assert ok, ('rounding failed', s)
        pts.append(g)
    return pts, ns

def post(m, K):
    """posterior image of the vertex list K under likelihood m"""
    out = []
    for p in K:
        z = dot(m, p)
        out.append(tuple(m[i] * p[i] / z for i in range(3)))
    return out

eps = F(3, 10); c = (1 - eps) / 3
VM = [tuple(c + (eps if j == i else 0) for j in range(3)) for i in range(3)]   # vertices of M
