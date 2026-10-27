"""lib59 (referee, round 60 / file REFEREE_round59): independent exact cell geometry.

Nothing is imported from the authors' scripts (PP74_py, PP75_py, PP76_py) or from REFEREE58_py.

Conventions
- Problems g in R^3 modulo sign, oriented so that s = g1+g2+g3 > 0; chart plane s = 1,
  h = (x, y, 1-x-y).  The great circle s = 0 is null.
- A coherent model is a finite list K of positive vertex vectors (scale irrelevant):
  value +1 ('h') iff k.h > 0 for every k in K, -1 ('-h') iff every k.h < 0, 0 (silent) otherwise.
- T = D_M, M = c1 + eps*Delta, eps = 3/10, c = 7/30: vertices (scaled by 30) v^a = (7,7,7) + 9 e_a.
- Posterior C_m: K = {m o v^a}.  Vertex-wise rescaling: K = {m_a o v^a}.
- World w: the correct answer at h is sign(h_w).  Ranks: correct 0, silent 1, wrong 2.
- Cells: open cells of the line arrangement {h_i = 0} u {k.h = 0 : k in K, K in models}, found by exact
  (Fraction) convex-polygon splitting in a box containing every vertex of the arrangement.
- Solid angles are computed in floating point from the exact vertices (Van Oosterom-Strackee).
  For a standard Gaussian, |g| and g/|g| are independent, so |g|-masses of conic sets are proportional
  to solid angles; we report solid angles (hemisphere total = 2 pi).
"""
from fractions import Fraction as F
import math, itertools

V = [(16, 7, 7), (7, 16, 7), (7, 7, 16)]


def post(m):
    return [tuple(F(m[i]) * v[i] for i in range(3)) for v in V]


def vwise(ms):
    return [tuple(F(ms[a][i]) * V[a][i] for i in range(3)) for a in range(3)]


def line_of(k):
    # k.h with h = (x, y, 1-x-y):  (k1-k3) x + (k2-k3) y + k3
    return (F(k[0]) - F(k[2]), F(k[1]) - F(k[2]), F(k[2]))


COORD = [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(-1), F(-1), F(1))]


def ev(l, p):
    return l[0] * p[0] + l[1] * p[1] + l[2]


def _inter(l1, l2):
    d = l1[0] * l2[1] - l1[1] * l2[0]
    if d == 0:
        return None
    return ((l1[1] * l2[2] - l1[2] * l2[1]) / d, (l1[2] * l2[0] - l1[0] * l2[2]) / d)


def _area2(P):
    s = F(0)
    for i in range(len(P)):
        a, b = P[i], P[(i + 1) % len(P)]
        s += a[0] * b[1] - a[1] * b[0]
    return s


def _split(P, l):
    pos, neg = [], []
    n = len(P)
    for i in range(n):
        p, q = P[i], P[(i + 1) % n]
        ep, eq = ev(l, p), ev(l, q)
        if ep >= 0:
            pos.append(p)
        if ep <= 0:
            neg.append(p)
        if (ep > 0 > eq) or (ep < 0 < eq):
            t = ep / (ep - eq)
            r = (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))
            pos.append(r)
            neg.append(r)
    out = []
    for Q in (pos, neg):
        if len(Q) >= 3 and _area2(Q) != 0:
            out.append(Q)
    return out


def _dedup(lines):
    out = []
    seen = set()
    for l in lines:
        # normalise by the first non-zero coefficient's absolute value (keep orientation irrelevant)
        for c in l:
            if c != 0:
                key = tuple(x / abs(c) for x in l)
                key2 = tuple(-x for x in key)
                break
        if key in seen or key2 in seen:
            continue
        seen.add(key)
        out.append(l)
    return out


def cells(models):
    """models: dict name -> K.  Returns list of dicts {'poly', 'pt', 'vals'} for all open cells."""
    L = list(COORD)
    for K in models.values():
        L += [line_of(k) for k in K]
    L = _dedup(L)
    M = F(4)
    for a, b in itertools.combinations(L, 2):
        p = _inter(a, b)
        if p is not None:
            M = max(M, abs(p[0]) + 1, abs(p[1]) + 1)
    M = 2 * M
    polys = [[(-M, -M), (M, -M), (M, M), (-M, M)]]
    for l in L:
        new = []
        for P in polys:
            new += _split(P, l)
        polys = new
    out = []
    for P in polys:
        cx = sum(p[0] for p in P) / len(P)
        cy = sum(p[1] for p in P) / len(P)
        h = (cx, cy, 1 - cx - cy)
        out.append({'poly': P, 'pt': h, 'vals': {n: answer(K, h) for n, K in models.items()}})
    return out


def answer(K, h):
    vals = [sum(F(k[i]) * h[i] for i in range(3)) for k in K]
    assert all(v != 0 for v in vals)
    if all(v > 0 for v in vals):
        return 1
    if all(v < 0 for v in vals):
        return -1
    return 0


def htype(h):
    """('U',) unanimous; ('A', k): one negative coordinate k; ('B', k): one positive coordinate k."""
    pos = [i for i in range(3) if h[i] > 0]
    neg = [i for i in range(3) if h[i] < 0]
    if len(neg) == 0:
        return ('U', None)
    if len(neg) == 1:
        return ('A', neg[0])
    return ('B', pos[0])


def rank(v, h, w):
    cor = 1 if h[w] > 0 else -1
    if v == cor:
        return 0
    if v == 0:
        return 1
    if v == -cor:
        return 2
    return 3


def solid(P):
    """solid angle of the cone over chart polygon P (float)."""
    Q = [(float(x), float(y), 1.0 - float(x) - float(y)) for (x, y) in P]
    c = [sum(q[i] for q in Q) / len(Q) for i in range(3)]

    def dot(a, b):
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    def cr(a, b):
        return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])

    def nr(a):
        return math.sqrt(dot(a, a))
    tot = 0.0
    for i in range(len(Q)):
        a, b = Q[i], Q[(i + 1) % len(Q)]
        num = abs(dot(c, cr(a, b)))
        den = nr(c) * nr(a) * nr(b) + dot(c, a) * nr(b) + dot(c, b) * nr(a) + dot(a, b) * nr(c)
        tot += 2 * math.atan2(num, den)
    return tot


def down(k, lam):
    m = [F(1), F(1), F(1)]
    m[k] = F(lam)
    return tuple(m)
