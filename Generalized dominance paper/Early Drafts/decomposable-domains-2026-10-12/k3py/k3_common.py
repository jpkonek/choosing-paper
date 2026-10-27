"""Shared geometry for the K3 scripts (NUMERICS only; no proof depends on them).
T1 with eps = 0.3; U = D_{K'}, K' = u + s(T1 - u), s = 0.9.  Run with python3 -I from this folder's parent."""
import numpy as np

eps, s = 0.3, 0.9
c0 = (1 - eps) / 3
u = np.ones(3) / 3
V = np.array([c0 * np.ones(3) + eps * np.eye(3)[k] for k in range(3)])   # vertices of T1
Vp = np.array([u + s * (V[k] - u) for k in range(3)])                    # vertices of K'
E = np.eye(3)


def in_D(g, K):
    """D_K (mixed part): min over the vertices of K of m.g > 0."""
    return np.min(g @ np.asarray(K).T, axis=-1) > 0


def in_U(g):
    return in_D(g, Vp)


def sample_U(rng, n, scale_tail=True):
    """Gaussian directions in U; with scale_tail, also some directions near the unanimous / boundary rays."""
    out, m = [], 0
    while m < n:
        g = rng.normal(size=(4 * n, 3))
        if scale_tail:
            k = rng.integers(0, 3, size=len(g))
            lam = np.exp(rng.uniform(0, 4, size=len(g)))
            g[np.arange(len(g)), k] *= lam
        g /= np.linalg.norm(g, axis=1, keepdims=True)
        g = g[in_U(g)]
        out.append(g)
        m += len(g)
    return np.concatenate(out)[:n]


def orthant(g):
    """sign pattern as a tuple of +-1 per row"""
    return np.sign(g).astype(int)


def mixed(g):
    sg = np.sign(g)
    return (sg.max(axis=1) > 0) & (sg.min(axis=1) < 0)


def midpoint_violations(acc, G, rng, trials=20000):
    """count pairs (a,b) of accepted gambles whose sum is in U but rejected (non-convexity witnesses)
    acc: function g -> bool array"""
    A = G[acc(G)]
    if len(A) < 2:
        return 0, 0
    i = rng.integers(0, len(A), size=trials)
    j = rng.integers(0, len(A), size=trials)
    S = A[i] + A[j]
    inU = in_U(S)
    S = S[inU]
    bad = ~acc(S)
    return int(bad.sum()), int(inU.sum())
