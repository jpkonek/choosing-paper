"""S1 referee / mu_equal_density.py -- a FULL ranking on M_U (n = 2) satisfying strict (G), (IB), (LA), (S)
(competitiveness on supp p, closed sections for EVERY model, selected models coherent and undominated), whose
selection is NOT nested.  These are exactly the hypotheses of Prop Q35 (n >= 2, e_12 = Delta, R_12 = M), so
(Nest_e) is not a consequence of them.  Only (C) fails.  This sharpens Example S1.9 (which is an edge system with
non-coherent 'selected' sets and no ranking on M_U).

Worlds: psi_1(X) = mu(E_1 X), psi_2(X) = mu(E_2 X), mu standard Gaussian on R^2 (equal densities).
Key identity (proved in S1_referee section 6): for every model X subset of U,
      psi_1(X) + psi_2(X) = mu(M) + 2 mu(N_+ \\ X)  >=  mu(M),   equality iff X regular.
Hence every regular model is undominated and competitive on {1,2}.  Sections {p : m(p) <= psi_1(X)} and
{p : mu(M) - m(p) <= psi_2(X)} are closed when m(p) = mu(E_1 C_p) is continuous.
Masses of the cones {sigma < alpha}, {beta' < tau <= beta} are computed exactly from angles (mu is rotation
invariant); the identity and competitiveness are also checked by Monte Carlo on random models.
Run: python3 -I mu_equal_density.py
"""
import math
import numpy as np

al_, be_ = 0.35, 0.60            # K' = [alpha', beta'] (weight t of world 2)


def theta_sigma(alpha):          # M^-: theta in (pi/2, pi), sigma = -cos/(sin-cos) increasing in theta
    return math.pi + math.atan((alpha - 1) / alpha) if alpha > 0 else math.pi / 2


def theta_tau(beta):             # M^+: theta in (-pi/2, 0), tau = cos/(cos-sin) increasing in theta
    return -math.atan((1 - beta) / beta)


def Fm(alpha):                   # mu{g in M^- : sigma < alpha}
    return (theta_sigma(alpha) - math.pi / 2) / (2 * math.pi)


def Fp(beta):                    # mu{g in M^+ : beta' < tau <= beta}
    return (theta_tau(beta) - theta_tau(be_)) / (2 * math.pi)


muM = Fm(al_) + Fp(1.0)
print("mu(M^-), mu(M^+), mu(M):", round(Fm(al_), 6), round(Fp(1.0), 6), round(muM, 6))


def mass(al, be):
    return Fm(al) + Fp(be)


# non-comonotone path of lattice points: (0,b') -> (a',b') -> slide at constant mass to (a1,b1) -> (a',b1) -> (a',1)
a1 = 0.10
target = Fm(al_) - Fm(a1)                 # increase of Fp needed to keep mass constant
lo, hi = be_, 1.0
for _ in range(200):
    mid = (lo + hi) / 2
    (lo, hi) = (mid, hi) if Fp(mid) < target else (lo, mid)
b1 = hi
assert b1 < 1.0
print("slide end point (a1, b1):", a1, round(b1, 6))


def path(p):
    s = 4 * p
    if s <= 1:
        return (al_ * s, be_)
    if s <= 2:                            # alpha decreases from a' to a1, beta chosen to keep mass constant
        al = al_ + (a1 - al_) * (s - 1)
        need = Fm(al_) - Fm(al)
        lo, hi = be_, 1.0
        for _ in range(100):
            mid = (lo + hi) / 2
            (lo, hi) = (mid, hi) if Fp(mid) < need else (lo, mid)
        return (al, (lo + hi) / 2)
    if s <= 3:
        return (a1 + (al_ - a1) * (s - 2), b1)
    return (al_, b1 + (1.0 - b1) * (s - 3))


ps = np.linspace(0, 1, 4001)
ms = np.array([mass(*path(p)) for p in ps])
print("m(0) = %.3g, m(1) - mu(M) = %.3g" % (ms[0], ms[-1] - muM))
print("m nondecreasing:", bool(np.all(np.diff(ms) >= -1e-9)), "  max step:", float(np.max(np.abs(np.diff(ms)))))
P, Q = path(0.25), path(0.5)
print("C_{1/4} = D_[%.3f,%.3f],  C_{1/2} = D_[%.3f,%.3f]  -> alpha down, beta up: crossing" % (*P, *Q))
print("   mu(E1 C_1/4 \\ E1 C_1/2) = %.4f,  mu(E1 C_1/2 \\ E1 C_1/4) = %.4f"
      % (Fm(P[0]) - Fm(Q[0]), Fp(Q[1]) - Fp(P[1])))

# Monte Carlo check of the identity psi1 + psi2 = mu(M) + 2 mu(N+ \ X) and of competitiveness
rng = np.random.default_rng(1)
g = rng.standard_normal((400000, 2))
t = np.linspace(al_, be_, 41)
inU = np.min((1 - t)[None, :] * g[:, :1] + t[None, :] * g[:, 1:], axis=1) > 0
g = g[inU]
w = 1.0 / 400000
pos1, pos2 = g[:, 0] > 0, g[:, 1] > 0
Nplus = pos1 & pos2
Mmask = ~Nplus
print("MC mu(M) = %.4f (exact %.4f)" % (Mmask.sum() * w, muM))
bad_id = bad_K = 0
Cerr = None
for trial in range(300):
    X = rng.random(len(g)) < rng.random()                  # random model (subset of U)
    E1X = X ^ pos1
    E2X = X ^ pos2
    lhs = (E1X.sum() + E2X.sum()) * w
    rhs = Mmask.sum() * w + 2 * (Nplus & ~X).sum() * w
    bad_id += abs(lhs - rhs) > 1e-12
    # competitiveness of a random selected C_p: psi1(C) <= psi1(X) or psi2(C) <= psi2(X)
    p = rng.random()
    al, be = path(p)
    sig = -g[:, 0] / (g[:, 1] - g[:, 0])
    tau = g[:, 0] / (g[:, 0] - g[:, 1])
    E1C = (Mmask & ~pos1 & (sig < al)) | (Mmask & pos1 & (tau <= be))
    E2C = Mmask & ~E1C
    bad_K += not (E1C.sum() <= E1X.sum() or E2C.sum() <= E2X.sum())
print("identity violations:", bad_id, "  competitiveness violations:", bad_K, " (300 random models)")
# (C) fails: an incoherent regular model tied with C_{1/2} at both worlds (swap two sigma-bands of equal mass)
print("(C) fails: E1 = E1(C_1/2) with a middle sigma-band removed and an equal-mass band beyond alpha added is")
print("   incoherent, regular, and has the same (psi1, psi2) as C_1/2.")
