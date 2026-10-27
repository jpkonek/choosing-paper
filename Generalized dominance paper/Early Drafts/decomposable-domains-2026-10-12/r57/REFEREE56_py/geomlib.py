"""geomlib (REFEREE56): independent exact geometry for the three-world module.

Written from scratch for the round-57 referee report; no code shared with PP67_py / PP68_py.
Everything is exact (fractions.Fraction / Python ints).

Conventions
- A problem is g in R^3 (modulo sign).  World w's correct answer is sign(g_w).
- D_K for K = conv(V) (V a finite list of points of the simplex) answers '+' iff v.g > 0 for all v in V,
  '-' iff v.g < 0 for all v in V, and 'S' otherwise.
- For a mixed g the odd world o is the one whose sign differs from the other two; 'A' (majority) is the
  sign shared by the other two worlds, 'B' (minority) is sign(g_o).  Unanimous g: class 0.
- rank at world w: 0 correct, 1 silent, 2 wrong (coherent models are never contradictory).
"""
from fractions import Fraction as F
import itertools, math

def dot(a, b): return sum(x * y for x, y in zip(a, b))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def scal(c, a): return tuple(c * x for x in a)
def sgn(x): return (x > 0) - (x < 0)

EPS = F(3, 10); C = (1 - EPS) / 3
def vtx(i): return tuple(C + (EPS if j == i else 0) for j in range(3))
v1, v2, v3 = vtx(0), vtx(1), vtx(2)
M = [v1, v2, v3]
def proj3(m):            # radial projection from e3 onto the {1,2} edge
    s = m[0] + m[1]; return (m[0] / s, m[1] / s, F(0))
d1, d2 = proj3(v1), proj3(v2)
h12 = (F(1, 2), F(1, 2), F(0))
assert d1 == (F(16, 23), F(7, 23), 0) and d2 == (F(7, 23), F(16, 23), 0) and proj3(v3) == h12
M0 = [d1, d2]
KT = M                      # T  = D_M
KN = M + M0                 # N  = D_conv(M u M0)
KD = M0                     # D* = D_M0
KL0 = [v3] + M0             # L0 = F_0 = D_conv(v3, M0)
def vt(t): return add(scal(1 - t, v3), scal(t, h12))
def KF(t): return [vt(t)] + M0          # F_t = D_conv(v_t, M0)

def adv(V, g):
    s = [sgn(dot(v, g)) for v in V]
    if all(x > 0 for x in s): return '+'
    if all(x < 0 for x in s): return '-'
    return 'S'

def cls(g):
    s = [sgn(x) for x in g]
    assert 0 not in s
    if len(set(s)) == 1: return 0
    for o in range(3):
        if s.count(s[o]) == 1: return o + 1
def AB(g, a):
    """translate '+'/'-'/'S' into 'A'/'B'/'S' (class 0: 'A' = correct)."""
    if a == 'S': return 'S'
    k = cls(g)
    if k == 0: return 'A' if (a == '+') == (g[0] > 0) else 'B'
    maj = [g[w] for w in range(3) if w != k - 1][0]
    return 'A' if (a == '+') == (maj > 0) else 'B'
def rank(g, a, w):
    if a == 'S': return 1
    return 0 if (a == '+') == (g[w - 1] > 0) else 2

# ---------------- exact cell enumeration of a central plane arrangement ----------------
def prim(v):
    """primitive integer vector in the direction of the rational vector v"""
    den = 1
    for x in v: den = den * F(x).denominator // math.gcd(den, F(x).denominator)
    iv = [int(F(x) * den) for x in v]
    g = 0
    for x in iv: g = math.gcd(g, abs(x))
    return tuple(x // g for x in iv)

def cells(normals):
    """Return (list of integer interior points, one per open cell of the arrangement on the sphere,
    and (V, E, F) from Euler's formula).  Every cell of a central arrangement of >= 3 planes in general
    enough position has a vertex; we take, around every vertex d, one point in every sector."""
    normals = [prim(n) for n in normals]
    assert len(set(normals) | set(tuple(-x for x in n) for n in normals)) == 2 * len(normals), 'parallel planes'
    lines = set()
    for a, b in itertools.combinations(normals, 2):
        d = prim(cross(a, b))
        lines.add(d); lines.add(tuple(-x for x in d))
    pts = {}
    Esum = 0
    for d in lines:
        through = [n for n in normals if dot(n, d) == 0]
        Esum += len(through)
        rays = []
        for n in through:
            t = cross(n, d); rays += [t, tuple(-x for x in t)]
        # an orthonormal-ish frame of the tangent plane (floats only for sorting)
        ea = rays[0]; eb = cross(d, ea)
        rays.sort(key=lambda r: math.atan2(float(dot(r, eb)), float(dot(r, ea))))
        for i in range(len(rays)):
            r = add(rays[i], rays[(i + 1) % len(rays)])
            others = [n for n in normals if dot(n, d) != 0]
            K = 1
            for n in others:
                K = max(K, 2 * abs(dot(n, r)) // abs(dot(n, d)) + 2)
            p = add(scal(K, d), r)
            sv = tuple(sgn(dot(n, p)) for n in normals)
            assert 0 not in sv
            for n in others: assert sgn(dot(n, p)) == sgn(dot(n, d))
            pts.setdefault(sv, p)
    V = len(lines); E = Esum      # each vertex on k circles contributes k to sum of arcs
    return list(pts.values()), (V, E, 2 - V + E)
