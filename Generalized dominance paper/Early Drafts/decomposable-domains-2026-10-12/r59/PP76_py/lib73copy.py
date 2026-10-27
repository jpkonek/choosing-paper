"""PP73 library (NUMERICS): posterior members C_a(g) = T(a o g), the exact rescaling loop,
odd worlds, u1 increments, fills. Monte Carlo on a standard Gaussian sample.
Advice coding: +1 / -1 = answer that sign, 0 = silent.  (No member is contradictory.)
Loss convention for u1: larger = worse (Phi_w(X->Y) > 0 means X is at least as good as Y at w).
"""
import numpy as np

EPS = 0.3
C0 = (1 - EPS) / 3
VERT = np.array([[C0 + (EPS if i == v else 0) for i in range(3)] for v in range(3)])


def sample(n=2_000_000, seed=73):
    rng = np.random.default_rng(seed)
    G = rng.standard_normal((n, 3))
    return G


def norm(a):
    a = np.asarray(a, float)
    return a / a.sum()


def advice(G, a):
    """D_{M_a}(g) = T(a o g): +1 if p.(a o g) > 0 for all vertices p, -1 if < 0 for all, else 0."""
    s = (G * np.asarray(a, float)) @ VERT.T
    return np.where((s > 0).all(1), 1, np.where((s < 0).all(1), -1, 0))


def ranks(G, x):
    """rank_w of advice x at g: 0 correct, 1 silent, 2 wrong."""
    sg = np.sign(G)
    r = np.where(x[:, None] == 0, 1, np.where(sg * x[:, None] > 0, 0, 2))
    return r


def classes(G):
    """odd world k (index 0..2) for mixed-sign g; -1 for unanimous."""
    sg = np.sign(G)
    npos = (sg > 0).sum(1)
    odd = np.where(npos == 1, np.argmax(sg > 0, 1), np.where(npos == 2, np.argmin(sg > 0, 1), -1))
    return odd


def majority(G):
    """majority answer A (sign shared by the two non-odd worlds)."""
    sg = np.sign(G)
    return np.where((sg > 0).sum(1) >= 2, 1, -1)


def u1(G, x):
    """PP56 level-0 field on the (2V) region, per world: answering h: -|Wr|*|g| at Cor worlds,
    +|Cor|*|g| at Wr worlds; S = 0; answering -h: (k_c,k_r) = (|Wr|, 2|Cor|).
    Unanimous g: rank_w * |g| (only used for consistency; no fills there)."""
    nrm = np.linalg.norm(G, axis=1)
    h = np.sign(G.sum(1))
    cor = (np.sign(G) * x[:, None]) > 0
    ncor = cor.sum(1)
    nwr = 3 - ncor
    mixed = (ncor > 0) & (ncor < 3)
    kc = np.where(x == h, nwr, nwr)          # |Wr| in both rows
    kr = np.where(x == h, ncor, 2 * ncor)
    val = np.where(cor, -kc[:, None], kr[:, None]) * nrm[:, None]
    val = np.where((x == 0)[:, None], 0.0, val)
    un = ~mixed & (x != 0)
    val[un] = ranks(G[un], x[un]) * nrm[un, None]
    return val


def Phi(G, x):
    return u1(G, x).mean(0)


def loop(a):
    b = a ** -3.0
    return norm([1, 1, 1]), norm([1, 1, b]), norm([b, 1, b])
