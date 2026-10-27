"""lib77: |g|-masses and u1-vectors on the exact cell model of lib79 (atoms = cells x radial halves).

Masses are Monte Carlo (NUMERICS): g ~ N(0, I_3), weight |g|; chart point h = g / sum(g) (problems modulo
sign); a sample is assigned to the cell with the same sign vector w.r.t. every line; half 0 := {|g| < R}.
u1 on H-values (PP78 lib78 convention): S -> h at an odd-o point moves V by sgn * (e - 3 e_o) * |g|,
sgn = +1 if h is correct only at o (type ('B', o)), -1 if h is wrong only at o (type ('A', o)).
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP79_py'))
sys.path.insert(0, os.path.join(HERE, '..', 'PP75_py'))
import numpy as np
from lib79 import *
from geo75 import cells as _cells, COORD

E = np.ones((3, 3)) - 3 * np.eye(3)

def _lines(models):
    L = []
    for K in models.values():
        L += lines(K)
    return list(COORD) + L

def masses(models, At, n=200_000, R=1.0, seed=77):
    """returns array m[i] = |g|-mass (per sample) of atom i (same order as lib79.atoms(models))."""
    L = _lines(models)
    extra = L[len(COORD):]
    cl = _cells([], extra_lines=extra)
    key = {}
    for ci, c in enumerate(cl):
        h = c['pt']
        key[tuple(1 if (a * h[0] + b * h[1] + cc) > 0 else 0 for (a, b, cc) in L)] = ci
    rng = np.random.default_rng(seed)
    g = rng.standard_normal((n, 3))
    s = g.sum(1)
    ok = np.abs(s) > 1e-9
    g, s = g[ok], s[ok]
    h = g / s[:, None]
    nrm = np.linalg.norm(g, axis=1)
    A = np.array([[float(a), float(b), float(cc)] for (a, b, cc) in L])
    sv = (h[:, 0:1] * A[:, 0] + h[:, 1:2] * A[:, 1] + A[:, 2]) > 0
    assert len(L) < 63
    pw = (1 << np.arange(len(L), dtype=np.int64))
    ikey = {sum(int(b) << k for k, b in enumerate(kk)): ci for kk, ci in key.items()}
    codes = sv.astype(np.int64) @ pw
    half = (nrm >= R).astype(int)
    cm = {}
    uc, inv = np.unique(codes * 2 + half, return_inverse=True)
    sums = np.bincount(inv, weights=nrm)
    for u, sm in zip(uc, sums):
        ci = ikey.get(int(u) // 2)
        if ci is None: continue
        cm[(ci, int(u) % 2)] = sm
    return np.array([cm.get((a['cell'], a['half']), 0.0) / len(g) for a in At])

def unit(a):
    t = a['type']
    o = t[1]
    sgn = 1.0 if t[0] == 'B' else -1.0
    return sgn * E[o]

def Vrec(At, m, Xv, Yv):
    """u1 vector of rec(X -> Y) for H-valued X, Y (lists of 'h'/'S')."""
    v = np.zeros(3)
    for i, a in enumerate(At):
        if Xv[i] == Yv[i]: continue
        assert Xv[i] in ('h', 'S') and Yv[i] in ('h', 'S'), (Xv[i], Yv[i])
        d = (1.0 if Yv[i] == 'h' else 0.0) - (1.0 if Xv[i] == 'h' else 0.0)
        v += d * m[i] * unit(a)
    return v
