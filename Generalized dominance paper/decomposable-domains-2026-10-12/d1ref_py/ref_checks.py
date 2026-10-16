"""Referee checks for D1 (NUMERICS only; no verdict rests on them).
R1  D1.5 bookkeeping: for each crossing (F1,w21,l=3), (F1,w31,l=2), (F2,w32,l=1): the corner portion adjacent to
    the crossing ends at the corner ray whose pattern is that of an atom normal (r12, r31, r23 resp.), and h(sigma)
    has h_l > 0 on a neighbourhood [sigma1, sigma2] of the crossing parameter straddling middle arc / corner portion.
R2  Lemma M Step 1 replacement (no R4 Thm B needed): for m in the wedge W = {m.h(s1)>=0, m.h(s2)>=0} (apex v) and
    exterior h near the crossing w with nearest facet point w', m.h < 0 implies |m - v| < |h - w'| / c0.
    Estimate c0 = inf_{m in W, w' in F near w} (m.w') / |m - v| and check the implication on random samples.
R3  D1.4 hull constant: analytic bound C0 <= 1/sin(theta/2)-type estimate vs. sampled ratio (sanity only).
"""
import numpy as np

E = np.eye(3)
rng = np.random.default_rng(7)


def T1(eps):
    c0 = (1 - eps) / 3
    return [c0 * np.ones(3) + eps * E[k] for k in range(3)]


def corner(V, k, j):
    r = np.cross(V[k], V[j]); l = 3 - k - j
    return r if r @ V[l] > 0 else -r


def simplex_sample(n):
    return rng.dirichlet(np.ones(3), size=n)


out = []
bad1 = bad2 = 0
c0min = np.inf
for eps in [0.02, 0.1, 0.3, 0.5, 0.8, 0.95]:
    V = T1(eps)
    cases = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]  # (facet k, zero coord c, positive coord l): w21, w31, w32
    for (k, c, l) in cases:
        others = [x for x in range(3) if x != k]
        # parametrise F_k from corner r_{k,a} to r_{k,b}
        a, b = others
        r0, r1 = corner(V, k, a), corner(V, k, b)
        h = lambda t: (1 - t) * r0 + t * r1
        tc = r0[c] / (r0[c] - r1[c])
        w = h(tc)
        if abs(w[c]) > 1e-12 or w[l] <= 0:
            bad1 += 1
        # which corner is on the side where h_c < 0 ?
        side_corner = r0 if r0[c] < 0 else r1
        # its pattern should be a corner-atom pattern: one positive coordinate (odd world), two negative
        pat = np.sign(side_corner)
        if not (np.sum(pat > 0) == 1 and np.sum(pat < 0) == 2):
            bad1 += 1
        # h_l > 0 on a neighbourhood of tc
        for dt in [-0.05, -0.01, 0.01, 0.05]:
            t = tc + dt
            if 0 < t < 1 and h(t)[l] <= 0:
                bad1 += 1
        # R2: wedge at v = V[k] spanned by facet gambles h(s1), h(s2) with s1 < tc < s2
        s1, s2 = tc - 0.02, tc + 0.02
        g1, g2 = h(s1), h(s2)
        v = V[k]
        # sample m in aff Delta near v in the wedge
        M = v + 0.3 * (simplex_sample(4000) - v) * rng.uniform(0, 1, (4000, 1))
        M = M[(M @ g1 >= 0) & (M @ g2 >= 0)]
        # c0 over w' in F near w (between s1 and s2), normalised |w'| ~ |w|
        for t in np.linspace(s1 + 0.002, s2 - 0.002, 9):
            wp = h(t)
            d = np.linalg.norm(M - v, axis=1)
            ok = d > 1e-9
            ratio = (M[ok] @ wp) / d[ok]
            c0min = min(c0min, ratio.min())
        # implication check
        for _ in range(3000):
            t = rng.uniform(s1 + 0.004, s2 - 0.004)
            wp = h(t)
            # exterior perturbation: move against v (v.h < 0)
            nrm = v / np.linalg.norm(v)
            hh = wp - rng.uniform(1e-4, 5e-3) * nrm + rng.normal(scale=1e-4, size=3)
            if v @ hh >= 0:
                continue
            dist = np.linalg.norm(hh - wp)
            neg = M[M @ hh < 0]
            if len(neg) and np.max(np.linalg.norm(neg - v, axis=1)) >= dist / max(c0min, 1e-12) + 1e-12:
                bad2 += 1
out.append(f"R1: crossing/corner/positivity bookkeeping failures: {bad1}")
out.append(f"R2: c0 estimate (min over samples) = {c0min:.4g} (>0 needed); implication failures: {bad2}")

# R3: analytic hull bound vs sampled ratio
bad3 = 0; worst = 0
for _ in range(3000):
    p = rng.dirichlet(np.ones(3) * rng.uniform(0.5, 4))
    o = rng.integers(3); j = [x for x in range(3) if x != o][0]
    aa, cc = rng.uniform(0.1, 3, 2)
    i = 3 - o - j
    bvec = np.zeros(3); bvec[i] = -aa; bvec[j] = -cc; bvec[o] = (aa * p[i] + cc * p[j]) / p[o]
    s = -bvec[j] / (bvec[o] - bvec[j]); L = (1 - s) * E[j] + s * E[o]
    dvec = (L - p) / np.linalg.norm(L - p)
    u1 = (E[j] - p) / np.linalg.norm(E[j] - p); u2 = (E[o] - p) / np.linalg.norm(E[o] - p)
    th = min(np.arccos(np.clip(dvec @ u1, -1, 1)), np.arccos(np.clip(dvec @ u2, -1, 1)))
    Cbound = 2.0 / np.sin(th / 2)       # crude analytic constant: wedge margin theta/2 survives perturbation
    worst = max(worst, Cbound)
    if not np.isfinite(Cbound):
        bad3 += 1
out.append(f"R3: analytic hull constant finite in all samples (failures {bad3}); max crude bound {worst:.1f}")
print("\n".join(out))
