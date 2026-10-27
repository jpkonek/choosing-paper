"""PP63 Theorem J: exact kite certificate (Fractions only).

Posterior family C_a = D_{M_a}, M = c*1 + eps*Delta, eps = 3/10, c = 7/30.
C_a answers g (positive) iff (a o m_v) . g > 0 for the three vertices m_v of M,
i.e. C_a(g) = T(a o g).  For a fixed problem g, Ans(g) := {a : C_a answers g}.

We exhibit four indices p1..p4 (a kite, convex position, inside any ball around u
of radius > 2*scale) and, for each of the 7 bipartitions {S, P\\S} of P (S nonempty,
proper, up to complement), an exact problem g with Ans(g) cap P = S or = P\\S,
every inequality strict (so it holds on an open cone of problems, hence on a non-null set).
g must lie in the disagreement region R of the family (it does: members of P disagree on it).
Radon's theorem then gives Theorem J (see PP63 s.5).
"""
from fractions import Fraction as Fr
import itertools, sys

EPS = Fr(3, 10)
C = (1 - EPS) / 3
MV = [tuple(C + (EPS if i == j else 0) for j in range(3)) for i in range(3)]
U = (Fr(1, 3),) * 3


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def vals(a, g):
    return [sum(a[i] * m[i] * g[i] for i in range(3)) for m in MV]


def advice(a, g):
    v = vals(a, g)
    if min(v) > 0:
        return 1
    if max(v) < 0:
        return -1
    if 0 in v:
        return None          # on a boundary plane: not allowed in a certificate
    return 0


def kite(scale):
    d = (Fr(-1), Fr(-1), Fr(2))           # axis of the corner wedge at u (in-plane)
    e = (Fr(1), Fr(-1), Fr(0))            # in-plane perpendicular
    def pt(t, s):
        return tuple(U[i] + scale * (t * d[i] + s * e[i]) for i in range(3))
    tau, delta, eta = Fr(1, 10), Fr(1), Fr(6)
    # p1, p3 on the axis; p2, p4 off it at the middle (eta*|e| vs (delta/2)*|d|*tan(half-angle))
    return [pt(tau, 0), pt(tau + delta / 2, eta), pt(tau + delta, 0), pt(tau + delta / 2, -eta)]


def convex_position(P):
    # in-plane coords (x,y) via basis d, e (orthogonal); check cyclic order p1,p2,p3,p4 convex
    def xy(p):
        q = [p[i] - U[i] for i in range(3)]
        return (dot(q, (-1, -1, 2)) / 6, dot(q, (1, -1, 0)) / 2)
    Q = [xy(p) for p in P]
    signs = []
    for k in range(4):
        a, b, c = Q[k], Q[(k + 1) % 4], Q[(k + 2) % 4]
        signs.append((b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]))
    return all(s > 0 for s in signs) or all(s < 0 for s in signs)


def run(scale):
    P = kite(scale)
    assert all(abs(sum(p) - 1) == 0 for p in P)
    assert convex_position(P)
    # every member of P must contain u in its posterior set (2V hypothesis); checked as in post51.u_in_Ma
    for p in P:
        inv = [1 / x for x in p]
        s = sum(inv)
        assert min(x / s for x in inv) >= C
    want = set()
    for r in (1, 2):
        for S in itertools.combinations(range(4), r):
            S = frozenset(S)
            comp = frozenset(range(4)) - S
            want.add(frozenset([S, comp]))
    assert len(want) == 7
    found = {}
    # (a) corner problems: apex at u, pair {1,2} active:  u o g  proportional to (-7,-7,23)
    cands = [(Fr(-7), Fr(-7), Fr(23))]
    # (b) single-active-constraint problems whose boundary line passes through the kite:
    #     for active vertex v, in-plane normal n and offset k, take G = n - k*1 and
    #     g_v = G_v/(c+eps), g_w = G_w/c (w != v); then f_v(a) = G.a on the plane sum(a) = 1.
    dirs = []
    for i in range(-6, 7):
        for j in range(-6, 7):
            n = (Fr(i), Fr(j), Fr(-i - j))
            if n != (0, 0, 0):
                dirs.append(n)
    for v in range(3):
        for n in dirs:
            offs = sorted(set(dot(n, p) for p in P))
            mids = [(offs[k] + offs[k + 1]) / 2 for k in range(len(offs) - 1)]
            for kap in mids:
                G = tuple(n[i] - kap for i in range(3))
                g = tuple(G[i] / (C + EPS) if i == v else G[i] / C for i in range(3))
                cands.append(g)
                cands.append(tuple(-x for x in g))
    for g in cands:
        adv = [advice(p, g) for p in P]
        if None in adv:
            continue
        nz = [x for x in adv if x != 0]
        if not nz or len(set(nz)) > 1:
            continue            # need exactly one answer sign (2V) and at least one answerer
        S = frozenset(k for k in range(4) if adv[k] != 0)
        if len(S) in (0, 4):
            continue
        key = frozenset([S, frozenset(range(4)) - S])
        if key not in found:
            found[key] = (g, S)
    return P, want, found


if __name__ == '__main__':
    allok = True
    for scale in (Fr(1, 1000), Fr(1, 10 ** 6)):
        P, want, found = run(scale)
        print(f'scale {scale}: kite indices (x 1/scale offsets from u):')
        for k, p in enumerate(P):
            print(f'   p{k+1} = u + {[str((p[i]-U[i])/scale) for i in range(3)]} * scale')
        for key in sorted(want, key=lambda k: sorted(min(k, key=len))):
            if key in found:
                g, S = found[key]
                print(f'   bipartition {sorted(sorted(x) for x in key)}: problem g = {[str(x) for x in g]}, answerers = {sorted(k+1 for k in S)}')
            else:
                print(f'   bipartition {sorted(sorted(x) for x in key)}: NOT FOUND')
                allok = False
        allok &= len(found) == 7
    print('all 7 bipartitions of the kite realised by answer/silence splits at both scales:', allok)
    print('ALL PASS' if allok else 'SOME FAIL')
