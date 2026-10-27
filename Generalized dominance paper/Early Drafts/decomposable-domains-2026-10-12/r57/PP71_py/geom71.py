"""geom71: exact rational geometry for PP71 (four-model recurrent repair).

Conventions as PP68/geom68: worlds 1,2,3; problem g mod sign; D_K answers s at g iff s*min_{v in vert K} v.g > 0.
Class k (k=1,2,3): sign of g_k differs from the other two; A = majority sign (correct at the two worlds != k),
B = the other sign (correct at world k).  Unmixed problems: every model in the open simplex says A; they are
common to all models considered here and are omitted.
"""
from fractions import Fraction as F
import itertools, random

eps = F(3, 10)
c = (1 - eps) / 3
V = [tuple(c + (eps if j == i else 0) for j in range(3)) for i in range(3)]   # vertices of M
v3 = V[2]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def sgn(x):
    return 1 if x > 0 else (-1 if x < 0 else 0)


def cls(g):
    s = [sgn(x) for x in g]
    if 0 in s:
        return None
    if s[0] == s[1] == s[2]:
        return 0
    for k in range(3):
        o = [s[j] for j in range(3) if j != k]
        if o[0] == o[1]:
            return k + 1


def maj(g):
    k = cls(g)
    return sgn(g[1] if k == 1 else g[0])


def adv(K, g):
    """A/B/S advice of D_K at a mixed g"""
    m = maj(g)
    vals = [m * dot(v, g) for v in K]
    if all(x > 0 for x in vals):
        return 'A'
    if all(x < 0 for x in vals):
        return 'B'
    return 'S'


def rank(k, a, w):
    if a == 'S':
        return 1
    corr = 'B' if k == w else 'A'
    return 0 if a == corr else 2


def samples(n_grid=7, n_rand=6000, seed=71):
    pts = set()
    R = range(-n_grid, n_grid + 1)
    for g in itertools.product(R, R, R):
        if cls(g) in (1, 2, 3):
            pts.add(tuple(F(x) for x in g))
    rnd = random.Random(seed)
    for _ in range(n_rand):
        g = tuple(F(rnd.randint(-400, 400), rnd.randint(1, 60)) for _ in range(3))
        if cls(g) in (1, 2, 3):
            pts.add(g)
    return sorted(pts)


def census(Ks, G):
    """map (class, advice tuple) -> list of sample problems"""
    out = {}
    for g in G:
        key = (cls(g), tuple(adv(K, g) for K in Ks))
        out.setdefault(key, []).append(g)
    return out


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def exact_points(Ks):
    """One point in every face of the arrangement of great circles {g : n.g = 0}, n ranging over the
    coordinate vectors and every vertex of every K (exact).  Every face has a vertex d on its boundary; the
    faces at d are hit by d + eps*(t_a + t_b), t ranging over the tangent rays at d (all pairs), with eps
    small enough that no plane not through d is crossed."""
    normals = [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))]
    for K in Ks:
        for v in K:
            v = tuple(F(x) for x in v)
            if not any(cross(v, n) == (0, 0, 0) for n in normals):
                normals.append(v)
    pts = set()
    for a in range(len(normals)):
        for b in range(a + 1, len(normals)):
            d0 = cross(normals[a], normals[b])
            if d0 == (0, 0, 0):
                continue
            for d in (d0, tuple(-x for x in d0)):
                through = [n for n in normals if dot(n, d) == 0]
                rays = []
                for n in through:
                    t = cross(n, d)
                    rays += [t, tuple(-x for x in t)]
                others = [n for n in normals if dot(n, d) != 0]
                for i in range(len(rays)):
                    for j in range(i + 1, len(rays)):
                        u = tuple(x + y for x, y in zip(rays[i], rays[j]))
                        if u == (0, 0, 0):
                            continue
                        m = max(abs(dot(n, u)) for n in others) or F(1)
                        eps = min(abs(dot(n, d)) for n in others) / (4 * m)
                        g = tuple(x + eps * y for x, y in zip(d, u))
                        if all(dot(n, g) != 0 for n in normals) and cls(g) in (1, 2, 3):
                            pts.add(g)
    return sorted(pts)
