"""J1 referee, NUMERICS only: Example J1.4 (cap inside a tube) realised in the T1 setting
(eps = 0.3, s = 0.9) in the collar of dU inside the orthant (+,+,-), where T1 rejects.
Checks: (1) the tube and cap lie in U, in (+,+,-), and in {T1 rejects}, so the cap is a
T1-wrong end of world 1 (and 2) and the tube a T1-correct end of world 3;
(2) W_n is inside S_n; (3) the shell S_d cap W_m minus W_M is non-null for every tested depth d
(importance sampling of directions near the arc), i.e. the arrow 1 -> 3 is misaligned.
Run: python3 -I j1ref_geometry.py
"""
import numpy as np

eps, s = 0.3, 0.9
c0 = (1 - eps) / 3
u = np.ones(3) / 3
V = np.array([c0 * np.ones(3) + eps * np.eye(3)[k] for k in range(3)])
Vp = np.array([u + s * (V[k] - u) for k in range(3)])


def nrm(x):
    return x / np.linalg.norm(x, axis=-1, keepdims=True)


# arc gamma: tau in [-0.3, 0.3], h(tau) = (1+tau, 1-tau, -0.91); rhat = gamma(0)
taus = np.linspace(-0.3, 0.3, 4001)
gam = nrm(np.stack([1 + taus, 1 - taus, -0.91 * np.ones_like(taus)], axis=1))
rhat = nrm(np.array([1.0, 1.0, -0.91]))


def ang(a, b):
    return np.arccos(np.clip(a @ b.T, -1, 1))


def dist_gamma(G):
    # angular distance to the arc (discretised; arc step << radii used below)
    best = np.full(len(G), np.inf)
    for k in range(0, len(gam), 200):
        best = np.minimum(best, ang(G, gam[k:k + 200]).min(axis=1))
    return best


theta = lambda m: 0.04 * 2.0 ** (-m)
rng = np.random.default_rng(1)

# (1) containment of the depth-n tube in U, O=(+,+,-), {T1 rejects}: ends need only be eventually pure
for n in range(0, 6):
    G = nrm(gam[rng.integers(len(gam), size=100000)] + theta(n) * rng.normal(size=(100000, 3)) / np.sqrt(3))
    T = G[dist_gamma(G) < theta(n)]
    inU = np.all(T @ Vp.T > 0, axis=1)
    inO = (T[:, 0] > 0) & (T[:, 1] > 0) & (T[:, 2] < 0)
    T1acc = np.all(T @ V.T > 0, axis=1)
    print(f"(1) depth {n} (theta={theta(n):.4f}) tube samples {len(T)}: in U {inU.mean():.4f}, "
          f"in (+,+,-) {inO.mean():.4f}, T1 accepts {T1acc.mean():.4f}")

# (2) W_n subset S_n is exact (rhat on gamma); check numerically
for n in range(4):
    Gc = nrm(rhat + theta(n) * rng.normal(size=(50000, 3)))
    Wn = ang(Gc, rhat[None])[:, 0] < theta(n)
    print(f"(2) n={n}: cap points outside tube: {int((dist_gamma(Gc[Wn]) >= theta(n)).sum())} of {int(Wn.sum())}")

# (3) shell S_d cap (W_m minus W_M): directions within theta(d) of gamma, angle to rhat in (theta(M), theta(m))
m, M = 0, 3
for dd in [2, 4, 6, 8, 10]:
    # sample near arc points at angle ~ (theta(M)+theta(m))/2 from rhat
    k = np.argmin(np.abs(ang(gam, rhat[None])[:, 0] - 0.5 * (theta(m) + theta(M))))
    Gs = nrm(gam[k] + theta(dd) * rng.normal(size=(20000, 3)) / np.sqrt(3))
    inS = dist_gamma(Gs) < theta(dd)
    a = ang(Gs, rhat[None])[:, 0]
    shell = inS & (a > theta(M)) & (a < theta(m))
    print(f"(3) d={dd:2d}: theta_d={theta(dd):.2e}, shell hits {int(shell.sum())} / {len(Gs)} local samples")
