"""N27 referee: the open Euclidean regime (sec 2.7) for T1, eps = 0.3, world l = 3, facet k = 1.

(1) theta_x(T1) is the max of x_l/|x| over the WHOLE half-space {v_k.x <= 0} (projection of e_l onto v_k^perp):
    theta_x = sqrt(1 - v_kl^2/|v_k|^2).  So for theta >= theta_x NO gamble beyond the plane of F_k (in any domain)
    is off-band at l; (X_lk) can then hold only if the ranking leaves some band points strict.
(2) N27's escape W = [e_l, v_k] does not contain K' (required: K_q contains K' on M_U); the admissible version is
    W' = co(K' u {e_l, v_k}).  Check: D_{W'} subset {h_l > 0}; P_{W'} = 0 on F_k where h_l > 0 (VP fails);
    D_{W'} contains a.e. off-band l-positive point of U when theta >= theta_x.
(3) VP reformulated: every directional limit W at e_l lies in {m.w_lk >= 0} and {m.r > 0} (r = corner ray at the
    l-positive end of F_k).  Check on vertices of candidate W.
"""
import numpy as np
eps, s = 0.3, 0.9
kap = (1 + 2 * eps) / (1 - eps); c0 = (1 - eps) / 3
E = np.eye(3); u = np.ones(3) / 3
V = np.array([c0 + eps * E[i] for i in range(3)])
Kp = np.array([u + s * (V[i] - u) for i in range(3)])          # K' vertices
l, k = 2, 0                                                       # world 3, facet F_1 (0-based)
vk = V[k]
thx = np.sqrt(1 - vk[l]**2 / (vk @ vk))
print(f"(1) theta_x via projection = {thx:.6f};  closed form sqrt((k^2+1)/(k^2+2)) = {np.sqrt((kap**2+1)/(kap**2+2)):.6f}")
rng = np.random.default_rng(1)
X = rng.normal(size=(2_000_000, 3)); X /= np.linalg.norm(X, axis=1)[:, None]
beyond = X @ vk < 0
print(f"    max x_3/|x| over 2e6 random directions with v_1.x<0: {X[beyond, l].max():.6f} (<= theta_x)")

PK = lambda pts, x: (x @ pts.T).min(axis=-1)                     # lower prevision of a polytope (by vertices)
inU = PK(Kp, X) > 0
W2 = np.vstack([Kp, E[l], vk])                                   # W' = co(K' u {e_l, v_k})
print("(2) [e_3, v_1] contains K'?  ", False, "(a segment cannot contain the 2-dim K')")
DW = PK(W2, X) > 0
print("    D_W' within {h_3 > 0}:", bool(np.all(X[DW, l] > 0)))
r12 = np.array([-1, -1, kap + 1.]); r31 = np.array([-1, kap + 1, -1.])
tt = np.linspace(0, 1, 2001)[:, None]; F = (1 - tt) * r12 + tt * r31
Fpos = F[F[:, l] > 1e-9]
print(f"    max |P_W'(x)| on F_1 with x_3>0: {np.abs(PK(W2, Fpos)).max():.2e}  (VP fails on that arc)")
for th in [thx - 0.02, thx + 1e-3]:
    off = inU & (X[:, l] > th * 1.0)                              # |x| = 1
    bad = off & ~DW
    print(f"    theta={th:.4f}: off-band 3-positive points of U: {off.sum()}, of which beyond F_1 (v_1.x<0): "
          f"{(off & beyond).sum()}, not in D_W': {bad.sum()}")
w31 = np.array([-1, kap, 0.])
for name, m in [("e_3", E[l]), ("v_1", vk), ("K' vertices min", None)]:
    if m is None:
        a = (Kp @ w31).min(); b = (Kp @ r12).min()
    else:
        a, b = m @ w31, m @ r12
    print(f"(3) {name:16s}: m.w_31 = {a:+.4f} (need >= 0),  m.r_12 = {b:+.4f} (need > 0)")
