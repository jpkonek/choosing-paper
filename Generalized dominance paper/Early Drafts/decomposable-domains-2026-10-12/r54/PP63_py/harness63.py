"""PP63 attack harness (NUMERICS): Monte Carlo problem sample, members, swaps, records.

A model is a boolean array ANS over the sample (answers h = sign(g1+g2+g3) g, else silent) restricted to
mixed problems (two-valued domain of (2V)).  A record is (P, Q): boolean masks of silenced / answered points.
A rule is a function rule(P, Q) -> tuple of 3 bools (accepted at worlds 1,2,3).

Tests offered:
  balanced_swap(rule)      : Prop 5.4 / Theorem Q shape -- incoherent copy accepted at all worlds?
  sections(rule, a, X)     : verdicts of rec(C_{a_t} -> X) along a ray, t -> 0, vs at a
  triangle_tc(rule, models): (TC) on all ordered triples of given models
  defence(rule, a, rivals) : some world accepts rec(C_a -> X)
"""
import numpy as np

rng = np.random.default_rng(63)
EPS = 0.3
C0 = (1 - EPS) / 3
VERT = np.array([[C0 + (EPS if i == v else 0) for i in range(3)] for v in range(3)])
NS = 400_000
G = rng.standard_normal((NS, 3))
NORM = np.linalg.norm(G, axis=1)
H = np.sign(G.sum(axis=1))[:, None] * G
COR = H > 0
NCOR = COR.sum(axis=1)
MIXED = (NCOR == 1) | (NCOR == 2)
G, H, NORM, COR, NCOR = G[MIXED], H[MIXED], NORM[MIXED], COR[MIXED], NCOR[MIXED]
N = len(G)
# balanced level-0 increment of silencing h -> S, per point (u1 of PP56): +|Wr| at Cor worlds, -|Cor| at Wr worlds
NU = np.where(COR, (3 - NCOR)[:, None], -NCOR[:, None]) * NORM[:, None]
ODD = np.where(NCOR == 1, np.argmax(COR, axis=1), np.argmin(COR, axis=1))
U = np.array([1 / 3] * 3)
B = np.array([406, 421, 373]) / 1200
D = np.array([406, 373, 421]) / 1200


def member(a):
    s = H @ (VERT * np.asarray(a)).T
    return (s > 0).all(axis=1)


def rec(X, Y):
    """X, Y: answer masks. Returns (P, Q)."""
    return X & ~Y, ~X & Y


def V(P, Q):
    """level-0 vector (sum over sample / NS): silencing adds NU, answering adds -NU."""
    return (NU[P].sum(axis=0) - NU[Q].sum(axis=0)) / N


def balanced_swap(a=U, b=B, seed=0):
    """F = F+ (a answers, b silent, odd world 1 wrong-only) + F- (a answers, b silent, odd world 1 right-only),
    trimmed to equal level-0 at every world (balanced), radially sliced so non-conic."""
    Ca, Cb = member(a), member(b)
    Ep = Ca & ~Cb & (ODD == 0) & (NCOR == 2)
    Em = Ca & ~Cb & (ODD == 0) & (NCOR == 1)
    ip, im = np.where(Ep)[0], np.where(Em)[0]
    r = np.random.default_rng(seed)
    r.shuffle(ip); r.shuffle(im)
    cp, cm = np.cumsum(NORM[ip]), np.cumsum(NORM[im])
    tot = min(cp[-1], cm[-1]) / 2
    F = np.zeros(N, bool)
    F[ip[cp <= tot]] = True
    F[im[cm <= tot]] = True
    return F, Ca, Cb
