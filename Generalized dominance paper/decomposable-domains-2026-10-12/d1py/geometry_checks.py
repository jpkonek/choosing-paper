"""D1 geometric inputs (NUMERICS; each item also has a one-line proof in D1_notes.md).
GA  For p* in int Delta and a corner normal b (pattern of r_ij, odd world o, b.p* = 0): the chord {b.q=0}
    meets relint[e_i,e_o] and relint[e_j,e_o]; the ray from p* to the [e_j,e_o] point lies in the open wedge
    spanned by e_j - p*, e_o - p*  (used in Lemma D1.4).
GB  Hull estimate: for x with |x-p*| = r and points e'_j, e'_o within rho of e_j, e_o, the triangle
    co(x, e'_j, e'_o) contains points of that ray at distance <= C r from p*; report max C over samples.
GC  T1 facets (all eps tested): h_k<0 on F_k; middle arc positive at the two other worlds; crossings
    w (one zero coordinate) with the exterior near-crossing ball containing two patterns that differ in one
    coordinate (never +-sigma of a single pattern)  (used in Lemma D1.6, case A).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from t1geom import T1, corner_ray, P, E, facet_param

rng = np.random.default_rng(5)

# GA, GB
badA = 0; Cmax = 0.0; n = 0
for _ in range(4000):
    p = rng.dirichlet(np.ones(3) * rng.uniform(0.5, 4))
    o = rng.integers(3); i, j = [x for x in range(3) if x != o]
    a, c = rng.uniform(0.1, 3, 2)
    b = np.zeros(3); b[i] = -a; b[j] = -c; b[o] = (a * p[i] + c * p[j]) / p[o]
    assert abs(b @ p) < 1e-12
    # intersection with edge [e_j, e_o]: (1-s) e_j + s e_o
    s = -b[j] / (b[o] - b[j]); L = (1 - s) * E[j] + s * E[o]
    s2 = -b[i] / (b[o] - b[i])
    if not (0 < s < 1 and 0 < s2 < 1):
        badA += 1; continue
    M = np.vstack([E[j] - p, E[o] - p]).T
    coef, *_ = np.linalg.lstsq(M, L - p, rcond=None)
    if not (np.all(coef > 0) and np.allclose(M @ coef, L - p)):
        badA += 1
    # GB
    d = (L - p) / np.linalg.norm(L - p)
    for _k in range(5):
        r = 10 ** rng.uniform(-4, -2)
        ang = rng.uniform(0, 2 * np.pi)
        t1 = np.array([1, -1, 0]) / np.sqrt(2); t2 = np.array([1, 1, -2]) / np.sqrt(6)
        x = p + r * (np.cos(ang) * t1 + np.sin(ang) * t2)
        if np.any(x <= 0):
            continue
        rho = 0.05
        ej = E[j] + rho * (p - E[j]); eo = E[o] + rho * (p - E[o])
        # smallest lam>0 with p + lam d in co(x, ej, eo): barycentric coordinates are affine in lam
        Mi = np.linalg.inv(np.vstack([x, ej, eo]).T)
        b0 = Mi @ p; b1 = Mi @ d
        lo, hi = 0.0, np.inf
        for q0, q1 in zip(b0, b1):
            if abs(q1) < 1e-15:
                if q0 < 0: lo, hi = 1.0, 0.0
                continue
            root = -q0 / q1
            if q1 > 0: lo = max(lo, root)
            else: hi = min(hi, root)
        best = lo if lo <= hi else None
        if best is None:
            badA += 1
        else:
            n += 1; Cmax = max(Cmax, best / r)
print(f"GA: chord/edge/wedge failures (incl. GB misses): {badA}")
print(f"GB: {n} hull samples, max C = (distance along ray)/(|x-p*|) = {Cmax:.3f}")

# GC
badC = 0
for eps in [0.01, 0.05, 1 / 7, 0.3, 0.5, 0.8, 0.99]:
    V = T1(eps)
    for k in range(3):
        h, r0, r1 = facet_param(V, k)
        others = [x for x in range(3) if x != k]
        taus = np.linspace(0, 1, 4001)
        H = np.array([h(t) for t in taus])
        if not np.all(H[:, k] < 0):
            badC += 1
        mid = (H[:, others[0]] > 0) & (H[:, others[1]] > 0)
        if mid.sum() == 0:
            badC += 1
        for c in others:
            t = r0[c] / (r0[c] - r1[c]); w = (1 - t) * r0 + t * r1
            # exterior points near w on both sides of {g_c = 0}
            pats = set()
            for s in [-1, 1]:
                g = w - 1e-3 * (np.ones(3) - E[c]) + s * 1e-4 * E[c]
                if P(V, g) >= 0:
                    badC += 1
                pats.add(tuple(np.sign(g).astype(int)))
            pl = list(pats)
            if len(pl) != 2 or tuple(-np.array(pl[0])) == pl[1]:
                badC += 1
print(f"GC: facet sign / middle-arc / crossing-pattern failures over 7 eps: {badC}")
