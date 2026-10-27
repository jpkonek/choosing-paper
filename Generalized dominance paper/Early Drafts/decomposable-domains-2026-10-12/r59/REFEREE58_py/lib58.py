"""lib58 (referee, round 58/59): independent re-implementation of the posterior family and of PP56's level-0
balanced field u^1 on H-records.  Nothing is imported from the authors' scripts.

Conventions
- Problem g in R^3 (mod sign).  Index x in log-likelihood coordinates (mod (1,1,1)); m = exp(x).
- C_m answers +1 (accept g) iff sum_i m_i v^a_i g_i > 0 for the three vertices v^a = c*1 + eps*e_a,
  -1 iff all < 0, 0 (silent) otherwise.  This is the rescaling inequality of AUDIT_round59_rescaling.
- h(g) = sign(g1+g2+g3).  Odd world o(g) of a mixed-sign g: the world whose sign differs from the other two.
- u^1 on R for the values {h, S}: u1(S) = 0; u1(h) = eps_o |g| if Cor(h) = {o}, -eps_o |g| if Wr(h) = {o},
  eps_o := (1,1,1) - 3 e_o.  V(rec(X->Y)) = Phi(Y) - Phi(X) (positive = old side better).
- Samples are symmetrised over all six coordinate permutations, so the empirical measure is exactly S3-invariant
  and the exact (1 2) / (1 3) ties of PP73 Lemma 4.7 hold up to rounding.
"""
import numpy as np, itertools

EPS = 0.3
C0 = (1 - EPS) / 3
VERT = np.array([[C0 + (EPS if i == a else 0.0) for i in range(3)] for a in range(3)])
D3 = np.array([1.0, 1.0, -2.0]); D1 = np.array([-2.0, 1.0, 1.0]); D2 = np.array([1.0, -2.0, 1.0])


def sample(n=400_000, seed=58):
    rng = np.random.default_rng(seed)
    G = rng.standard_normal((n, 3))
    return np.concatenate([G[:, list(p)] for p in itertools.permutations(range(3))])


def advice(G, x):
    m = np.exp(np.asarray(x, float))
    s = (G * m) @ VERT.T
    return np.where((s > 0).all(1), 1, np.where((s < 0).all(1), -1, 0)).astype(np.int8)


def hsign(G):
    return np.sign(G.sum(1)).astype(np.int8)


def odd(G):
    sg = np.sign(G)
    npos = (sg > 0).sum(1)
    return np.where(npos == 1, np.argmax(sg > 0, 1), np.where(npos == 2, np.argmin(sg > 0, 1), -1))


def corodd(G):
    """True where h is correct exactly at the odd world (Cor(h) = {o}); False where Wr(h) = {o}."""
    o = odd(G)
    h = hsign(G)
    return (np.sign(G[np.arange(len(G)), np.where(o < 0, 0, o)]) == h)


class Geo:
    def __init__(self, G):
        self.G = G
        self.N = len(G)
        self.nrm = np.linalg.norm(G, axis=1)
        self.h = hsign(G)
        self.o = odd(G)
        self.co = corodd(G)
        E = np.ones((3, 3)) - 3 * np.eye(3)       # row o = eps_o
        sgn = np.where(self.co, 1.0, -1.0)
        U = np.zeros((self.N, 3))
        mix = self.o >= 0
        U[mix] = E[self.o[mix]] * (sgn[mix] * self.nrm[mix])[:, None]
        self.Uh = U                               # u1(g, h) - u1(g, S)  (on R)

    def check2V(self, adv):
        """(2V): the model never answers -h."""
        return int(((adv != 0) & (adv != self.h)).sum())

    def V(self, X, Y):
        """u1 record vector of rec(X -> Y) for H-type advice arrays X, Y (values in {h, 0})."""
        assert not ((X != 0) & (X != self.h)).any() and not ((Y != 0) & (Y != self.h)).any()
        dY = (Y != 0).astype(float) - (X != 0).astype(float)   # +1: S -> h, -1: h -> S
        return (self.Uh * dY[:, None]).sum(0) / self.N

    def mass(self, mask):
        return self.nrm[mask].sum() / self.N
