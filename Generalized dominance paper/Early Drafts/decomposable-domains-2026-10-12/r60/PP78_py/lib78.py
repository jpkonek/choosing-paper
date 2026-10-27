"""lib78 (allocator, round 60): three-ray star G = {T} u {B_{k,t} = C_{t*delta_k}}.
Independent of the authors' code; same conventions as REFEREE58's lib58 (re-implemented here).

- g in R^3, S3-symmetrised Gaussian sample.  Index x in log-likelihood coordinates.
- C_x answers h (+1) iff sum_i m_i v^a_i g_i > 0 for the three vertices v^a = c*1 + eps*e_a (m = exp x),
  -1 iff all < 0, 0 = silent.
- delta_k = 1 - 3 e_k (pure down-shift of world k).
- odd world o(g); co(g): Cor(h) = {o}.  u1 on H-records: changing S -> h at g moves V by
  +eps_o|g| if Cor(h)={o} ... (we use U(g) = u1(g,h) - u1(g,S) = sgn * |g| * eps_o, eps_o = 1 - 3 e_o,
  sgn = +1 if Cor(h)={o}, -1 if Wr(h)={o}); V(rec(X->Y)) = Phi(Y) - Phi(X).
- type sigma(g) = +1 if flipping T's value at g improves the odd world o(g), else -1.
"""
import numpy as np, itertools

EPS = 0.3
C0 = (1 - EPS) / 3
VERT = np.array([[C0 + (EPS if i == a else 0.0) for i in range(3)] for a in range(3)])
DELTA = [np.ones(3) - 3 * np.eye(3)[k] for k in range(3)]


def sample(n=300_000, seed=78):
    rng = np.random.default_rng(seed)
    G = rng.standard_normal((n, 3))
    return np.concatenate([G[:, list(p)] for p in itertools.permutations(range(3))])


def advice(G, x):
    m = np.exp(np.asarray(x, float))
    s = (G * m) @ VERT.T
    return np.where((s > 0).all(1), 1, np.where((s < 0).all(1), -1, 0)).astype(np.int8)


class Geo:
    def __init__(self, G):
        self.G, self.N = G, len(G)
        self.nrm = np.linalg.norm(G, axis=1)
        self.h = np.sign(G.sum(1)).astype(np.int8)
        sg = np.sign(G)
        npos = (sg > 0).sum(1)
        self.o = np.where(npos == 1, np.argmax(sg > 0, 1), np.where(npos == 2, np.argmin(sg > 0, 1), -1))
        oo = np.where(self.o < 0, 0, self.o)
        self.co = np.sign(G[np.arange(self.N), oo]) == self.h
        E = np.ones((3, 3)) - 3 * np.eye(3)
        U = np.zeros((self.N, 3))
        mix = self.o >= 0
        sgn = np.where(self.co, 1.0, -1.0)
        U[mix] = E[self.o[mix]] * (sgn[mix] * self.nrm[mix])[:, None]
        self.U = U
        self.T = advice(G, np.zeros(3))
        # sigma: flipping T improves o  <=>  (T = h and Wr = {o}) or (T = S and Cor = {o})
        self.sigma = np.where(((self.T != 0) & ~self.co) | ((self.T == 0) & self.co), 1, -1)

    def member(self, k, t):
        return self.T.copy() if t == 0 else advice(self.G, t * DELTA[k])

    def viol2V(self, A):
        return int(((A != 0) & (A != self.h)).sum())

    def V(self, X, Y, mask=None):
        """u1 vector of rec(X -> Y) (H-type arrays), optionally restricted to mask."""
        d = (Y != 0).astype(float) - (X != 0).astype(float)
        if mask is not None:
            d = d * mask
        return (self.U * d[:, None]).sum(0) / self.N

    def mass(self, m):
        return self.nrm[m].sum() / self.N


def margin_rule_classes(v, kappa=0.25):
    """Closed classes cl(A_w) of the cyclic margin rule (PP78 Def. 2.1) containing v (v != 0, sum v >= 0)."""
    v = np.asarray(v, float)
    nv = np.abs(v).max()
    M = v.max()
    out = []
    for w in range(3):
        p, q = (w - 1) % 3, (w + 1) % 3      # predecessor, successor
        near = v[w] >= M - kappa * nv
        # w is chosen iff w is near-max and (q near-max implies ... w precedes q), and not (p near-max with p preceding w)
        # closure of A_w: near-max at w, and NOT strictly beaten by margin, and p not near-max (closure: v_p <= M - kappa nv)
        cond_p = v[p] <= M - kappa * nv          # p is not (strictly) near-max  (closure of 'p not in N')
        out.append(bool(near and cond_p))
    # three-way near-tie region (all near-max) goes to world 0 (world 1) as a fallback
    if all(v[w] >= M - kappa * nv for w in range(3)):
        out[0] = True
    return [w + 1 for w in range(3) if out[w]]
