# Set-configuration check (no ranking): one earlier end W (cone over caps around r),
# later ends S'_l (cones over caps around r'_l, r'_l -> r). Each pair (W, S'_l) is
# eventually disjoint, yet for every depth a of W, every J and every M > a,
# some S'_{l,J} meets the shell W_a \ W_M non-nully (whole cap inside the shell).
import numpy as np
rng = np.random.default_rng(1)
th  = lambda m: 0.2 * 2.0**(-m)            # W_m: cap radius around r
phi = lambda l: 0.15 * 2.0**(-l)           # angle(r'_l, r)
psi = lambda l, n: 0.01 * 2.0**(-l - n)    # S'_{l,n}: cap radius around r'_l
# (i) pairwise eventual disjointness: at depth d = l+1, th(d) + psi(l,d) < phi(l)
ok_i = all(th(l + 1) + psi(l, l + 1) < phi(l) for l in range(60))
# (ii) for every a, J (any), M > a: l := max(a, M) ... pick l in [a, M-1] with cap inside shell
bad = 0
for a in range(0, 25):
    for M in range(a + 1, a + 25):
        for Jfun in (lambda l: 0, lambda l: l, lambda l: 10**3):
            found = False
            for l in range(a, M):
                J = Jfun(l)
                if phi(l) + psi(l, J) < th(a) and phi(l) - psi(l, J) > th(M):
                    found = True; break
            bad += (not found)
print("pairwise eventually disjoint:", ok_i)
print("cases (a,M,J) with no shell-hitting later end:", bad)
# Monte Carlo sanity check that a cap inside the shell has positive measure (a=2, M=6, l=3, J=5)
def unit(v): return v / np.linalg.norm(v)
r = unit(np.array([1.0, -0.6, -0.5]))      # a direction in the orthant (+,-,-)
e = unit(np.cross(r, [0, 0, 1.0]))
a, M, l, J = 2, 6, 3, 5
rl = unit(np.cos(phi(l)) * r + np.sin(phi(l)) * e)
# sample directions in the S'_{l,J} cap
n = 20000
z = rng.normal(size=(n, 3)); z -= (z @ rl)[:, None] * rl; z = z / np.linalg.norm(z, axis=1)[:, None]
ang = psi(l, J) * np.sqrt(rng.random(n))
d = np.cos(ang)[:, None] * rl + np.sin(ang)[:, None] * z
dr = np.arccos(np.clip(d @ r, -1, 1))
print("MC: fraction of S'_{l,J} cap in W_a minus W_M:", np.mean((dr < th(a)) & (dr > th(M))))
