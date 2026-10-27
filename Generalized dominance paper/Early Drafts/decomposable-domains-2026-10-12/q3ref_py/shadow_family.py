"""Q3 referee, independent checks of Q3 §§2-3 (NUMERICS; no verdict depends on them alone).

(1) Lemma 2.1 of Q3 for nu^L, exact per-sign-pattern formula vs Monte Carlo.
(2) Bathtub closure (referee Lemma R1): if nu endorses every comparison out of T1 at world i, so does
    f*nu whenever f <= lam on E_i(T1) and f >= lam off it.  Spot check on a discretised U.
(3) Referee Prop R2 (explicit, for nu^L): a T1-favouring reweighting nu' of nu^L and a weight t with
    t_3 = 1/(L+1) - delta at which B'_t = T1 minus a thin cone around an interior ray w0 of S_3:
    null ties, incoherent (robust convexity witness), and mu(B'_t Δ T1) -> 0 as delta -> 0.
(4) Referee Prop R2 (general recipe) applied to the facet-switching shadow nu^fs: normalise, inflate
    off a cone C_eta, pick t near e_1; B'_t = T1 minus part of C_eta.
Run: python3 -I shadow_family.py
"""
import numpy as np

rng = np.random.default_rng(7)
eps, s = 0.3, 0.9
L = 21.0
c0 = (1 - eps) / 3
kap = (1 + 2 * eps) / (1 - eps)
u = np.ones(3) / 3
V = np.array([c0 * np.ones(3) + eps * np.eye(3)[k] for k in range(3)])
Vp = np.array([u + s * (V[k] - u) for k in range(3)])


def in_DT(g):
    return np.all(g @ V.T > 0, axis=-1)


def in_U(g):
    return np.all(g @ Vp.T > 0, axis=-1)


def sample_U(n):
    out, m = [], 0
    while m < n:
        g = rng.normal(size=(4 * n, 3))
        g /= np.linalg.norm(g, axis=1, keepdims=True)
        g = g[in_U(g)]
        out.append(g)
        m += len(g)
    return np.concatenate(out)[:n]


G = sample_U(300000)
T1 = in_DT(G)
sg = np.sign(G)


def wL(g, t1mask):
    pos = g > 0
    return np.where((t1mask[:, None] & pos) | (~t1mask[:, None] & ~pos), L, 1.0)


W = wL(G, T1)
C = sg * W                                   # c^L field

# (1) Lemma 2.1
bad_a = bad_b = 0
for _ in range(300):
    t = rng.dirichlet(np.ones(3))
    B = (C @ t) > 0
    if t.min() > 1 / (L + 1):
        bad_a += int(np.any(B != T1))
    elif t.min() < 1 / (L + 1):
        k = int(np.argmin(t))
        Sk = T1 & (G[:, k] > 0) & (np.delete(G, k, 1) < 0).all(1)
        bad_b += int(np.any(B & Sk))
print(f"(1) Lemma 2.1: violations of (a) {bad_a}, of (b) {bad_b} (300 random weights, {len(G)} gambles)")

# (2) bathtub closure on a discretised U (atoms = 3000 sampled gambles, equal mass)
Ga = G[:3000]; Ta = T1[:3000]; Wa = W[:3000]; sa = sg[:3000]
viol = tested = 0
for _ in range(200):
    i = rng.integers(3)
    err_T1 = (Ta & (sa[:, i] < 0)) | (~Ta & (sa[:, i] > 0))         # E_i(T1)
    lam = rng.uniform(0.5, 2)
    f = np.where(err_T1, lam * rng.uniform(0, 1, 3000), lam * (1 + rng.exponential(1, 3000)))
    nuL = Wa[:, i]; nup = f * nuL
    for _ in range(50):
        # random model X near or far from T1; E_i(X) = X Δ P_i
        flip = rng.random(3000) < rng.choice([0.01, 0.1, 0.5])
        X = Ta ^ flip
        EX = (X & (sa[:, i] < 0)) | (~X & (sa[:, i] > 0))
        if nuL[EX].sum() >= nuL[err_T1].sum():           # comparison T1 <=_i X endorsed by nu^L
            tested += 1
            viol += int(nup[EX].sum() < nup[err_T1].sum() - 1e-9)
print(f"(2) bathtub closure: {tested} nu^L-endorsed comparisons out of T1, nu' violations {viol}")

# (3) explicit reweighting of nu^L at world 3
w0 = np.array([-1.0, -1.0, kap + 3.0]); w0 /= np.linalg.norm(w0)
assert in_DT(w0[None])[0]
ang = np.arccos(np.clip(G @ w0, -1, 1))
S3 = T1 & (G[:, 2] > 0) & (G[:, 0] < 0) & (G[:, 1] < 0)
alpha0 = 0.15                                   # cone of angle alpha0 around w0 lies inside S3?
P = w0 + 0.0
zeta = np.minimum(1.0, ang / alpha0)
corr3 = ~((T1 & (sg[:, 2] < 0)) | (~T1 & (sg[:, 2] > 0)))       # correct at world 3 for T1
f3 = np.where(corr3, 2.0, 1.0)
f3 = np.where(S3, 1.0 + zeta, f3)
Wp = W.copy(); Wp[:, 2] = W[:, 2] * f3
Cp = sg * Wp
print("(3) explicit nu' (densities in [1, 2L]):")
for delta in [1e-2, 3e-3, 1e-3, 3e-4]:
    t3 = 1 / (L + 1) - delta
    t = np.array([(1 - t3) / 2, (1 - t3) / 2, t3])
    val = Cp @ t
    B = val > 0
    D = B != T1
    removed = T1 & ~B
    added = B & ~T1
    theta = (1 - t3) / (L * t3)
    pred = S3 & (zeta <= theta - 1)
    cone_ok = np.all(removed == pred)
    # incoherence witness: two points of B whose sum (scaled) lies in removed set
    wit = 0
    R = G[removed]
    if len(R):
        for r in R[:200]:
            # perturb r in two opposite directions orthogonal to w0
            v = np.cross(r, rng.normal(size=3)); v /= np.linalg.norm(v)
            rad = alpha0 * (theta - 1)
            for scale in [1.5 * rad, 2.0 * rad, 3.0 * rad]:
                g1, g2 = r + scale * v, r - scale * v
                q = np.array([g1, g2])
                q /= np.linalg.norm(q, axis=1, keepdims=True)
                tq = in_DT(q)
                wq = wL(q, tq)
                f3q = np.where(~((tq & (q[:, 2] < 0)) | (~tq & (q[:, 2] > 0))), 2.0, 1.0)
                s3q = tq & (q[:, 2] > 0) & (q[:, 0] < 0) & (q[:, 1] < 0)
                zq = np.minimum(1.0, np.arccos(np.clip(q @ w0, -1, 1)) / alpha0)
                f3q = np.where(s3q, 1 + zq, f3q)
                wq[:, 2] *= f3q
                if np.all((np.sign(q) * wq) @ t > 0):
                    wit += 1
                    break
    print(f"   delta={delta:.0e}: t={np.round(t,4)}, mu(B'Δ T1)/mu(U)={D.mean():.5f}, added={added.sum()}, "
          f"removed = predicted thin cone: {cone_ok}, near-tie fraction(|val|<1e-9)={np.mean(np.abs(val)<1e-9):.1e}, "
          f"midpoint witnesses (g1,g2 in B', (g1+g2)/2 removed): {wit}/{min(len(R),200)}")

# (4) general recipe on the facet-switching shadow
jh = np.argmin(G @ V.T, axis=1)
rho = V[jh] * np.abs(G)                          # rho_i = v_{j(h),i} |h_i|
cfs = sg * rho
assert np.all(((cfs @ u) > 0) == T1)             # T1 is nu^fs-Bayes at u
# per world: errors / correct of T1
err = (T1[:, None] & (sg < 0)) | (~T1[:, None] & (sg > 0))
rho1 = np.where(err, np.minimum(rho, 1.0), np.maximum(rho, 1.0))   # bathtub with lam = 1
w1 = np.array([-0.2, 1.0, 0.45]); w1 /= np.linalg.norm(w1)            # interior ray of D_T1, w1_1 < 0
assert in_DT(w1[None])[0]
ang1 = np.arccos(np.clip(G @ w1, -1, 1))
Ceta = ang1 <= 0.08
print("(4) general recipe on nu^fs (cone C_eta of angle 0.08 around", np.round(w1, 3), "):",
      f"mu(C_eta)/mu(U)={Ceta.mean():.4f}")
for tt in [np.array([0.9, 0.05, 0.05]), np.array([0.97, 0.015, 0.015]), np.array([0.995, 0.0025, 0.0025])]:
    M = 2 / tt.min() + 1
    infl = np.where(~err & ~Ceta[:, None], M, 1.0)
    rhop = rho1 * infl
    val = (sg * rhop) @ tt
    B = val > 0
    removed = T1 & ~B
    added = B & ~T1
    print(f"   t={tt}: removed outside C_eta: {np.sum(removed & ~Ceta)}, added: {added.sum()}, "
          f"removed inside C_eta: {np.sum(removed & Ceta)}/{Ceta.sum()}, mu(B'ΔT1)/mu(U)={np.mean(B != T1):.5f}")

# (5) structure of coherent edge models (n = 3, edge [e1,e2]): M = co(K' ∪ [x,y]) with [x,y] a segment of the
#     edge (m = (a,1-a,0), a in [x,y]).  Check: agrees with P_1 off R_12 (Q3.4), and world-1 error sets on R_12
#     are nested iff (x,y) move comonotonically (so (Nest_e) is a two-parameter comonotonicity condition,
#     the analogue of the n = 2 question Q2.N).
def DM(g, x, y):
    ext = np.array([[x, 1 - x, 0.0], [y, 1 - y, 0.0]])
    pts = np.vstack([Vp, ext])
    return np.all(g @ pts.T > 0, axis=-1)
R12 = (G[:, 0] * G[:, 1] < 0)
P1 = G[:, 0] > 0
def E1(x, y):
    D = DM(G, x, y)
    return (D & (G[:, 0] < 0)) | (~D & (G[:, 0] > 0))
off = 0
for (x, y) in [(0.2, 0.7), (0.5, 0.9), (0.05, 0.3)]:
    D = DM(G, x, y)
    off += int(np.sum((D != P1) & ~R12))
print(f"(5) edge models co(K'∪[x,y]): disagreements with P_1 off R_12 = {off}")
A, B_, Cc = E1(0.6, 0.8), E1(0.4, 0.7), E1(0.4, 0.9)
def nested(a, b):
    return (not np.any(a & ~b)) or (not np.any(b & ~a))
print(f"    (0.6,0.8) vs (0.4,0.7) comonotone: nested {nested(A, B_)};  (0.6,0.8) vs (0.4,0.9) crossing: nested {nested(A, Cc)}"
      f" (|A\\C|={np.sum(A & ~Cc)}, |C\\A|={np.sum(Cc & ~A)})")
