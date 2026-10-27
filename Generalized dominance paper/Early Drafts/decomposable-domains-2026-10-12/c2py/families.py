"""Test gamble families and prior grids for DCF(G,F) at the target prior p* = u."""
import numpy as np
from dcf import setup, facet_h, corner, PT, mixed, unit, E

rng = np.random.default_rng(1)


def jitter(g, s=1e-4):
    return g + s * rng.standard_normal(3)


def gambles(eps, taus=(0.1, 0.3, 0.5, 0.7, 0.9), shifts=(-0.01, 0.01), nrand=0, box=True, crossings=True):
    kap, v, xp = setup(eps)
    out, tags = [], []
    for k in range(3):
        for tau in taus:
            h = unit(facet_h(k, tau, v))
            for t in shifts:
                out.append(jitter(h - t * np.ones(3))); tags.append(('facet', k, tau, t))
        # corner rays
        i, j = [l for l in range(3) if l != k]
    for k in range(3):
        for j in range(k + 1, 3):
            r = unit(corner(k, j, v))
            for t in shifts:
                out.append(jitter(r - t * np.ones(3))); tags.append(('corner', k, j, t))
    if crossings:
        for k in range(3):
            i, j = [l for l in range(3) if l != k]
            # crossing parameters: where h_i=0 and h_j=0 along the facet
            r0, r1 = corner(k, i, v), corner(k, j, v)
            for l in (i, j):
                tau = r0[l] / (r0[l] - r1[l])
                h = unit(facet_h(k, tau, v))
                for t in shifts:
                    for dl in (-0.02, 0.02):
                        g = h.copy(); g[l] += dl
                        out.append(jitter(g - t * np.ones(3))); tags.append(('cross', k, l, dl, t))
    if box:
        beta = 1 / kap
        for (eta, zeta) in [(0.02, 0.05), (0.05, 0.02), (0.01, 0.01)]:
            for perm in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
                A = np.zeros(3); B = np.zeros(3)
                a, b, c = perm
                A[a], A[b], A[c] = -beta * (1 + eta), eta, 1
                B[a], B[b], B[c] = 1, -zeta, -beta * (1 - zeta)
                out.append(jitter(unit(A))); tags.append(('boxA', perm, eta))
                out.append(jitter(unit(B))); tags.append(('boxB', perm, zeta))
    for _ in range(nrand):
        while True:
            g = rng.standard_normal(3)
            if mixed(g):
                break
        out.append(unit(g)); tags.append(('rand',))
    F = np.array(out)
    keep = [i for i in range(len(F)) if mixed(F[i])]
    return F[keep], [tags[i] for i in keep], v


def priors(rings=(0.03, 0.1), nring=8, vert=(0.05, 0.01), nvert=5, chords=(0.3, 0.6), edges=True):
    u = np.ones(3) / 3
    P = [u]
    # orthonormal basis of 1-perp
    b1 = np.array([1, -1, 0]) / np.sqrt(2); b2 = np.array([1, 1, -2]) / np.sqrt(6)
    for r in rings:
        for k in range(nring):
            a = 2 * np.pi * (k + 0.5) / nring
            P.append(u + r * (np.cos(a) * b1 + np.sin(a) * b2))
    for b in range(3):
        a, c = [l for l in range(3) if l != b]
        for rho in vert:
            for phi in np.linspace(0.05, 0.95, nvert):
                P.append(E[b] + rho * ((1 - phi) * (E[a] - E[b]) + phi * (E[c] - E[b])))
        for t in chords:
            P.append((1 - t) * u + t * E[b])
    if edges:
        for b in range(3):
            for a in range(3):
                if a != b:
                    for s in (0.05, 0.2):
                        q = (1 - s) * E[b] + s * E[a]
                        P.append(0.995 * q + 0.005 * u)
    return np.array(P)
