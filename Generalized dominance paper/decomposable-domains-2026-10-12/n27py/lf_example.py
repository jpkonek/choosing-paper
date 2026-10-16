"""N27 (i): the auditor's (LF) set N = {g : dist(g, bd D_T) < exp(-|g|)} for T1 (eps = 0.3). Evidence only.

(a) N contains every nonzero boundary point but no conic neighbourhood of bd D_T \\ 0:
    for a unit boundary point h0 and a fixed outward offset rho, t*(h0 + rho*n) leaves N for large t.
(b) Every gamble used by the N15/N21/N23 chain lies near a COMPACT set Sigma of boundary gambles
    (normalised corner rays, the facet segments h(tau), both normalisations of the crossings, the box
    witnesses A, B of the writeup, the N21.6 test gambles w* - delta*1 + eta*e_b).  We compute
    b := max norm on Sigma and the collar width exp(-b'), b' = b + margin, available inside N; the levels
    c0 and witness parameters must be below it.  This is the bounded-collar repair N0^b.
"""
import numpy as np
from scipy.optimize import nnls

eps = 0.3
kap = (1 + 2 * eps) / (1 - eps)
c0 = (1 - eps) / 3
V = np.array([c0 * np.ones(3) + eps * np.eye(3)[k] for k in range(3)])   # vertices v_k
R = np.array([[-1, -1, kap + 1], [kap + 1, -1, -1], [-1, kap + 1, -1]], float).T  # corner rays r12, r23, r31 (columns)

def dist_to_boundary(g):
    """distance from g to bd(cl D_T); cl D_T = cone(R) = {V g >= 0}."""
    s = V @ g
    if np.all(s >= 0):                       # inside: distance to nearest facet plane (facets are full faces)
        # distance to the boundary of a polyhedral cone from inside = min over facets of dist to facet cone;
        # for a point inside, nearest boundary point lies on some facet plane; check it is in the facet.
        best = np.inf
        for k in range(3):
            p = g - (V[k] @ g) / (V[k] @ V[k]) * V[k]
            if np.all(V @ p >= -1e-12):
                best = min(best, np.linalg.norm(g - p))
            else:                            # nearest point on that facet is on an edge ray
                for j in range(3):
                    r = R[:, j]
                    if abs(V[k] @ r) < 1e-9:
                        t = max(0.0, g @ r / (r @ r))
                        best = min(best, np.linalg.norm(g - t * r))
        return best
    lam, res = nnls(R, g)                    # outside: projection onto the cone
    return res

def in_N(g):
    return dist_to_boundary(g) < np.exp(-np.linalg.norm(g))

# (a) no conic neighbourhood
h0 = 0.5 * (R[:, 0] / np.linalg.norm(R[:, 0]) + R[:, 2] / np.linalg.norm(R[:, 2]))   # a relint point of F_1
h0 /= np.linalg.norm(h0)
n_out = -V[0] / np.linalg.norm(V[0])                                                   # outward normal of F_1
print("(a) rho = 0.01 offset outside F_1 along the ray t*(h0 + rho n):")
for t in [0.1, 1, 2, 4, 6, 8]:
    g = t * (h0 + 0.01 * n_out)
    print(f"   t = {t:4}: dist = {dist_to_boundary(g):.4g}, exp(-|g|) = {np.exp(-np.linalg.norm(g)):.4g}, in N: {in_N(g)}")

# (b) the compact set Sigma of gambles used by the chain
tau = np.linspace(0, 1, 2001)
Sigma = []
for (a, b) in [(0, 2), (0, 1), (1, 2)]:      # the three facets as segments between corner rays
    for t in tau:
        Sigma.append((1 - t) * R[:, a] + t * R[:, b])
beta = 1 / kap
Sigma += [np.array([-1, 0, kap]), np.array([-beta, 0, 1]), np.array([-1, kap, 0]), np.array([1, -beta, 0])]
Sigma = np.array(Sigma)
bmax = np.linalg.norm(Sigma, axis=1).max()
bmin = np.linalg.norm(Sigma, axis=1).min()
print(f"\n(b) norms on Sigma lie in [{bmin:.3f}, {bmax:.3f}]")
margin = 0.5
width = np.exp(-(bmax + margin))
print(f"    collar width available inside N on the shell |g| <= {bmax + margin:.3f}: exp(-{bmax+margin:.3f}) = {width:.4g}")
print(f"    so N0^b := {{g : dist(g, Sigma) <= {width/2:.4g}}} is a compact subset of N; levels |c| <= c0 need c0*sqrt(3) < {width/2:.4g}")
# sanity: random points of N0^b are in N
rng = np.random.default_rng(0)
bad = 0
for _ in range(20000):
    s = Sigma[rng.integers(len(Sigma))]
    d = rng.normal(size=3); d *= (width / 2) * rng.random() / np.linalg.norm(d)
    bad += not in_N(s + d)
print(f"    random check: {bad} of 20000 points of the collar outside N")
