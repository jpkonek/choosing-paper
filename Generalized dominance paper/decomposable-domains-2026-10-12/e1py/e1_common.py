"""Shared geometry for the E1 scripts (NUMERICS only). T1 with eps = 0.3, U = D_{K'}, K' = u + s(T1 - u), s = 0.9."""
import numpy as np

eps, s = 0.3, 0.9
c0 = (1 - eps) / 3
u = np.ones(3) / 3
V = np.array([c0 * np.ones(3) + eps * np.eye(3)[k] for k in range(3)])     # vertices of T1
Vp = np.array([u + s * (V[k] - u) for k in range(3)])                      # vertices of K'


def in_DT(g):
    return np.all(g @ V.T > 0, axis=-1)


def in_U(g):
    return np.all(g @ Vp.T > 0, axis=-1)


def sample_U(rng, n):
    out, m = [], 0
    while m < n:
        g = rng.normal(size=(4 * n, 3))
        g /= np.linalg.norm(g, axis=1, keepdims=True)
        g = g[in_U(g)]
        out.append(g)
        m += len(g)
    return np.concatenate(out)[:n]


def correct(G, T):
    """correct[i] at gamble g: T1 (mask T) gives the right advice at world i."""
    pos = G > 0
    return (T[:, None] & pos) | (~T[:, None] & ~pos)


def bayes(G, W, t):
    """strict Bayes set of the shadow with densities W (n x 3) at weight t; returns (accept mask, tie mask)."""
    val = (np.sign(G) * W) @ t
    return val > 0, val == 0
