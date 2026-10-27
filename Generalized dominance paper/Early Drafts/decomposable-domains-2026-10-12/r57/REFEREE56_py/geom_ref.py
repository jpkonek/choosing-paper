"""geom_ref (REFEREE56): independent exact checks of the module geometry.

Run: python3 -I -B geom_ref.py > geom_ref.out
Checks (all exact; cells of the plane arrangement are enumerated exactly and counted against Euler):
  A1  type census of (T, N, D*, L0) by class; PP67 Lemma 1.2(b) list
  A2  N = T ^ D* on every cell; weak 3-worseness N <=3 T, D* <=3 N, L0 <=3 N
  A3  L0 = N on class 3 (= "F0 and N agree on the world-3 minority region"); L0's new answers are B on M1, M2
  A4  L = {T != N}: on every cell of L, N is strictly better than T at world 1 or at world 2 (P1 u P2 = L),
      and P1, P2 are both proper subsets of L
  A5  PP67 Prop 1.1: Delta n P* = conv(M u M0), computed as a polygon (P* via extreme rays of P)
  A6  K_L0 subset K_N; F_1 = D*
"""
import os, sys, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geomlib import *

ok = True
def chk(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
planes = E + [v1, v2, v3, d1, d2]
pts, (V, Ed, Fc) = cells(planes)
print('arrangement of %d planes: %d cells found; Euler V=%d E=%d F=%d' % (len(planes), len(pts), V, Ed, Fc))
chk('cell enumeration complete (Euler)', len(pts) == Fc)

MODELS = {'T': KT, 'N': KN, 'D': KD, 'L0': KL0}
census = {}
for g in pts:
    k = cls(g)
    ty = tuple(AB(g, adv(MODELS[m], g)) for m in ('T', 'N', 'D', 'L0'))
    census.setdefault(k, set()).add(ty)
for k in sorted(census):
    print('  class %d: (T,N,D*,L0) types %s' % (k, sorted(census[k])))
exp = {3: {('S', 'S', 'A'), ('A', 'A', 'A'), ('B', 'S', 'A')},
       1: {('S', 'S', 'S'), ('S', 'S', 'B'), ('A', 'A', 'A'), ('A', 'S', 'S'), ('A', 'S', 'B'), ('B', 'B', 'B')}}
exp[2] = exp[1]
chk('A1 PP67 Lemma 1.2(b): (T,N,D*) types by class exactly as listed',
    all({t[:3] for t in census[k]} == exp[k] for k in (1, 2, 3)) and {t[:3] for t in census[0]} == {('A', 'A', 'A')})

def meet(a, b):   # T ^ D*
    return a if a == b else 'S'
a2 = True
for g in pts:
    T_, N_, D_, L_ = (adv(MODELS[m], g) for m in ('T', 'N', 'D', 'L0'))
    a2 &= N_ == meet(T_, D_)
    a2 &= rank(g, N_, 3) >= rank(g, T_, 3) and rank(g, D_, 3) >= rank(g, N_, 3) and rank(g, L_, 3) >= rank(g, N_, 3)
chk('A2 N = T ^ D*; N weakly 3-worse than T; D* and L0 weakly 3-worse than N (every cell)', a2)

a3 = True; newL0 = set()
for g in pts:
    N_, L_ = adv(KN, g), adv(KL0, g)
    if cls(g) == 3: a3 &= N_ == L_
    if N_ != L_: newL0.add((cls(g), AB(g, N_), AB(g, L_)))
chk('A3 L0 = N on all of class 3; L0 differs from N only by new B answers on M1, M2: %s' % sorted(newL0),
    a3 and newL0 == {(1, 'S', 'B'), (2, 'S', 'B')})

a4 = True; P1only = P2only = False
for g in pts:
    T_, N_ = adv(KT, g), adv(KN, g)
    if T_ != N_:
        assert N_ == 'S' and rank(g, T_, 3) == 0
        b1 = rank(g, N_, 1) < rank(g, T_, 1); b2 = rank(g, N_, 2) < rank(g, T_, 2)
        a4 &= b1 or b2
        P1only |= b1 and not b2; P2only |= b2 and not b1
chk('A4 on every cell of L = {T != N}: T is 3-correct, N = S, and N is strictly better at world 1 or 2 '
    '(so P1 u P2 = L, the retreat half of PP67 Prop 7.1 is vacuous)', a4)
chk('A4b P1 != L and P2 != L (cells of L where N improves only at 1, resp. only at 2)', P1only and P2only)

# A5: P = {g : m.g > 0 for m in M, g3 < 0} is a convex polyhedral cone; extreme rays from pairs of facets
facets = [v1, v2, v3, (0, 0, -1)]
rays = []
for a, b in itertools.combinations(facets, 2):
    d = prim(cross(a, b))
    for r in (d, tuple(-x for x in d)):
        if all(dot(f, r) >= 0 for f in facets): rays.append(r)
rays = sorted(set(rays))
print('  extreme rays of cl(P):', rays)
# Delta n P* as a polygon: constraints k_i >= 0, k.r >= 0 on the plane sum k = 1
cons = list(E) + rays
def solve2(a, b):     # intersection of a.k = 0, b.k = 0, sum k = 1
    import fractions
    A = [list(map(F, a)), list(map(F, b)), [F(1)] * 3]; rhs = [F(0), F(0), F(1)]
    # Cramer
    def det(m): return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
                        + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
    D = det(A)
    if D == 0: return None
    sol = []
    for j in range(3):
        Mj = [row[:] for row in A]
        for i in range(3): Mj[i][j] = rhs[i]
        sol.append(det(Mj) / D)
    return tuple(sol)
verts = set()
for a, b in itertools.combinations(cons, 2):
    k = solve2(a, b)
    if k is not None and all(dot(c, k) >= 0 for c in cons): verts.add(k)
print('  vertices of Delta n P*:', sorted(verts))
# membership in K_N = conv(v1, v2, v3, d1, d2): K_N is the polygon with these vertices; test by LP-free
# barycentric check over triangles of a fan
KNv = [v1, v2, v3, d1, d2]
def in_tri(p, a, b, c):
    # solve p = x a + y b + z c, x+y+z = 1 (the points lie in the plane sum = 1, so use two coordinates)
    m = [[a[0], b[0], c[0]], [a[1], b[1], c[1]], [1, 1, 1]]
    s = solve_lin(m, [p[0], p[1], 1])
    return s is not None and all(x >= 0 for x in s)
def solve_lin(m, rhs):
    m = [list(map(F, r)) for r in m]; rhs = list(map(F, rhs))
    def det(q): return (q[0][0]*(q[1][1]*q[2][2]-q[1][2]*q[2][1]) - q[0][1]*(q[1][0]*q[2][2]-q[1][2]*q[2][0])
                        + q[0][2]*(q[1][0]*q[2][1]-q[1][1]*q[2][0]))
    D = det(m)
    if D == 0: return None
    out = []
    for j in range(3):
        q = [r[:] for r in m]
        for i in range(3): q[i][j] = rhs[i]
        out.append(det(q) / D)
    return out
def in_KN(p): return any(in_tri(p, *t) for t in itertools.combinations(KNv, 3))
a5 = all(in_KN(k) for k in verts) and all(all(dot(c, k) >= 0 for c in cons) for k in KNv)
chk('A5 PP67 Prop 1.1: every vertex of Delta n P* lies in conv(M u M0), and every vertex of conv(M u M0) '
    'lies in Delta n P*  (so Delta n P* = K_N)', a5)

chk('A6 K_L0 = conv(v3, M0) subset K_N (generators), and F_1 = conv(h12, M0) = M0 (h12 = midpoint of M0)',
    all(in_KN(k) for k in KL0) and h12 == tuple((a + b) / 2 for a, b in zip(d1, d2)))
print('ALL PASS' if ok else 'SOME FAIL')
