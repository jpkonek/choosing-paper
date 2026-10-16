"""AUDIT_fU NUMERICS: do the U-domain constructions handle pairs whose U-orientation lies outside H = {g_1 > 0}?

Part A (n = 2, K' = {1/2}, U = {g_1 + g_2 > 0}; the N26.1 setting).
  A1  every pair {g,-g} meets U (a.e.), so no pair is "outside the domain";
  A2  r(g) = -g_2/(g_1-g_2) is invariant under g -> -g, and for mixed pairs r > 1/2 iff the U-orientation has g_1 < 0;
  A3  psi_i computed from the definition E_i(X) = X sym-diff (U cap {h_i > 0}) on Monte Carlo samples of U-orientations
      agrees with the bin formula of N26 / check_n26_1 (which has a '+ side' r < 1/2 and a '- side' r > 1/2);
  A4  the pointwise Bayes rule derived from E_i on the U-orientation agrees with N26's rule
      ('+ side: accept iff p > theta_+(r)'; '- side: accept -g iff p < theta_-(r)');
  A5  the WRONG reading (integrate only over H cap U, i.e. drop the - side) is detectably different: it loses the upper
      end beta of every credal set, so the target D_[0.25,0.625] is not even representable.
Part B (n = 3, T1, eps = 0.3, s = 0.9): U cap {g_1 < 0} is non-null, facet F_1 lies in {h_1 < 0}, and the box
  witness A of Prop. T1 lies in U cap {g_1 < 0}; so any argument that kept only U cap H would lose a whole facet.
Run: python3 -I orientation_check.py
"""
import numpy as np

rng = np.random.default_rng(7)

# ---------------- Part A ----------------
M = 2_000_000
g = rng.standard_normal((M, 2))
inU = g[:, 0] + g[:, 1] > 0
inmU = -(g[:, 0] + g[:, 1]) > 0
print("A1 fraction of gambles g with neither g nor -g in U: %.2e" % np.mean(~inU & ~inmU))

o = np.where(inU[:, None], g, -g)                     # U-orientation of each pair (each pair sampled twice: harmless)
mixed = o[:, 0] * o[:, 1] < 0
r_of = lambda x: -x[:, 1] / (x[:, 0] - x[:, 1])
r = r_of(o[mixed]); r_neg = r_of(-o[mixed])
print("A2 max |r(g) - r(-g)| on mixed pairs: %.2e" % np.max(np.abs(r - r_neg)))
om = o[mixed]
print("A2 mixed pairs: P(U-orientation has g1<0 | r>1/2) = %.6f,  P(g1<0 | r<1/2) = %.6f"
      % (np.mean(om[r > 0.5, 0] < 0), np.mean(om[r < 0.5, 0] < 0)))
print("   share of ALL pairs whose U-orientation has g1<0: %.4f (expect 1/4)" % np.mean(o[:, 0] < 0))

t0, b0 = 0.3, 0.625
def theta(rr):  # N26 theta_+ on r<1/2, theta_- on r>1/2
    tp = np.where(rr <= 0.2, 0.2 + 0.5 * rr, np.where(rr <= 0.3, t0, 0.3 + 0.5 * (rr - 0.3)))
    tm = 0.1 + 1.6 * (rr - 0.5)
    return np.where(rr < 0.5, tp, tm)
# error weights on U-orientations
rr_all = np.where(mixed, r_of(o), np.nan)
rho1 = np.where(mixed, 1 - theta(np.nan_to_num(rr_all)), 1.0)
rho2 = np.where(mixed, theta(np.nan_to_num(rr_all)), 1.0)

def coherent_model(al, be):
    """X = D_[al,be] cap U as a boolean on U-orientations o: accept iff min over m1 in [al,be] of m.o > 0."""
    v_al = al * o[:, 0] + (1 - al) * o[:, 1]
    v_be = be * o[:, 0] + (1 - be) * o[:, 1]
    return (np.minimum(v_al, v_be) > 0)

def psi_def(X):
    E1 = X ^ (o[:, 0] > 0)                           # E_i(X) = X sym-diff (U cap {h_i > 0})
    E2 = X ^ (o[:, 1] > 0)
    w = 0.5 / M                                      # mu(pairs) normalised to 1/2 (mass of H), each pair sampled twice
    return np.array([np.sum(rho1 * E1), np.sum(rho2 * E2)]) * w * 2 / 2

# bin formula of check_n26_1 (Gaussian-implied density of r; unanimous mass 1/4)
N = 6000
rp = (np.arange(N) + 0.5) / N * 0.5; rm = 0.5 + (np.arange(N) + 0.5) / N * 0.5
dens = lambda x: 1.0 / (2 * np.pi * (x ** 2 + (1 - x) ** 2))
mp, mm = dens(rp) * 0.5 / N, dens(rm) * 0.5 / N
thp, thm = theta(rp), theta(rm)
def psi_bins(al, be):
    xp = (rp < al).astype(float); xm = (rm > be).astype(float)
    return np.array([np.sum((1 - thp) * mp * (1 - xp)) + np.sum((1 - thm) * mm * xm),
                     np.sum(thp * mp * xp) + np.sum(thm * mm * (1 - xm))])

worst = 0.0
for al, be in [(0.25, 0.625), (0.2, 0.625), (0.3, 0.7), (0.0, 0.5), (0.5, 1.0), (0.1, 0.9)]:
    X = coherent_model(al, be)
    a, b = psi_def(X), psi_bins(al, be)
    worst = max(worst, np.max(np.abs(a - b)))
    print("A3 D_[%.3f,%.3f]: psi from E_i definition %s   bin formula %s" % (al, be, np.round(a, 4), np.round(b, 4)))
print("A3 max discrepancy (Monte Carlo, n = %d): %.1e" % (M, worst))

# A4: Bayes rule from E_i on U-orientations: accept o iff p*rho1*[err1 if accept] + (1-p)*rho2*[err2 if accept]
#     < p*rho1*[err1 if silent] + (1-p)*rho2*[err2 if silent]
bad = 0
for p in np.linspace(0.01, 0.99, 99):
    acc_cost = p * rho1 * (o[:, 0] < 0) + (1 - p) * rho2 * (o[:, 1] < 0)
    sil_cost = p * rho1 * (o[:, 0] > 0) + (1 - p) * rho2 * (o[:, 1] > 0)
    accept = acc_cost < sil_cost
    th = theta(np.nan_to_num(rr_all))
    rule = np.where(~mixed, True, np.where(rr_all < 0.5, p > th, p < th))
    keep = ~np.isclose(acc_cost, sil_cost)
    bad += np.sum(accept[keep] != rule[keep])
print("A4 mismatches between E_i-derived Bayes rule and N26's two-sided rule (99 weights): %d" % bad)

# A5: wrong reading, only H cap U
Hside = o[:, 0] > 0
X = coherent_model(0.25, 0.625)
print("A5 target D_[0.25,0.625]: share of its accepted mixed U-orientations with g1<0: %.3f"
      % (np.sum(X & mixed & ~Hside) / np.sum(X & mixed)))
print("   (an H cap U-only bookkeeping would treat these as outside the domain and could not represent beta = 0.625)")

# ---------------- Part B ----------------
eps, s = 0.3, 0.9
u = np.ones(3) / 3
V = np.array([(1 - eps) * u + eps * np.eye(3)[k] for k in range(3)])
Vp = u + s * (V - u)                                  # vertices of K'
G = rng.standard_normal((1_000_000, 3))
PU = (G @ Vp.T).min(axis=1) > 0
print("B  mu(U) = %.4f, mu(U cap {g1<0}) = %.4f, mu(U cap {g1>0}) = %.4f" %
      (PU.mean(), (PU & (G[:, 0] < 0)).mean(), (PU & (G[:, 0] > 0)).mean()))
print("   (-0.1,1,1) in U:", bool((np.array([-0.1, 1, 1]) @ Vp.T).min() > 0))
kappa = (1 + 2 * eps) / (1 - eps); beta = 1 / kappa
r12, r31 = np.array([-1, -1, kappa + 1]), np.array([-1, kappa + 1, -1])
taus = np.linspace(0, 1, 201)
F1 = np.array([(1 - t) * r12 + t * r31 for t in taus])   # facet F_1 between its corner rays
print("   facet F_1: max h_1 = %.3f (all < 0), and min_k v_k.h = %.2e (on the facet)" %
      (F1[:, 0].max(), np.abs((F1 @ V.T).min(axis=1)).max()))
eta = 0.01
A = np.array([-beta * (1 + eta), eta, 1.0])
print("   box witness A =", np.round(A, 4), " in U:", bool((A @ Vp.T).min() > 0), " A_1 < 0:", A[0] < 0)
