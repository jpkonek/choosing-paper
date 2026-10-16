"""Referee re-check of N26.1 (n = 2 lexicographic warm-up). Independent of n26py/warmup.py:
closed-form Bayes path, Gaussian-implied density of r, models = fractional acceptance per bin
(Lyapunov relaxation), arbitrary (also NON-regular) test models, exact lex comparisons, KKM.
NUMERICS only."""
import numpy as np
rng = np.random.default_rng(1)
t0, r1, r2, b0 = 0.3, 0.2, 0.3, 0.625
N = 6000
rp = (np.arange(N) + 0.5) / N * 0.5            # + side r in (0, 1/2)
rm = 0.5 + (np.arange(N) + 0.5) / N * 0.5      # - side r in (1/2, 1)
dens = lambda r: 1.0 / (2*np.pi*(r**2 + (1-r)**2))   # law of r for standard Gaussian g, mixed pairs
mp, mm = dens(rp)*0.5/N, dens(rm)*0.5/N
U0 = 0.25                                      # mass of unanimous pairs
thp = np.where(rp <= r1, 0.2 + 0.5*rp, np.where(rp <= r2, t0, 0.3 + 0.5*(rp - r2)))
thm = 0.1 + 1.6*(rm - 0.5)
# closed-form Bayes cut points
def aB(p):  # sup{r<1/2: th+ < p}
    if p <= 0.2: return 0.0
    if p <= 0.3: return 2*(p - 0.2)
    if p < 0.4: return 0.3 + 2*(p - 0.3)
    return 0.5
def bB(p):  # inf{r>1/2: th- > p}
    return float(np.clip(0.5 + (p - 0.1)/1.6, 0.5, 1.0))
def aB_left(p):
    return 0.2 if abs(p - t0) < 1e-15 else aB(p)
# secondaries from the path (closed forms derived from Gamma)
def Uplus(r):   # inf{u : alpha(u) > r}
    if r < 0.2: p = 0.2 + r/2
    elif r < 0.3: return r + b0
    else: p = 0.3 + (r - 0.3)/2
    return r + bB(p)
def Vfun(r):    # sup{u : beta(u) < r} = r + alpha(left limit at p = th-(r))
    p = 0.1 + 1.6*(r - 0.5)
    return r + (aB_left(p) if p > 0.2 else 0.0)
Up = np.array([Uplus(r) for r in rp]); Vm = np.array([Vfun(r) for r in rm])
assert np.all(np.diff(Up) > 0) and np.all(np.diff(Vm) > 0)
print("V jump at beta0:", Vm[rm < b0].max(), "->", Vm[rm > b0].min(), "(expect 0.825 -> 0.925)")
rho1p, rho2p, rho1m, rho2m = 1-thp, thp, 1-thm, thm
# model = (xp, xm, xu): acceptance fractions on + bins, on - bins (accept -g), unanimous
def psi(X):
    xp, xm, xu = X
    return np.array([U0*(1-xu) + np.sum(rho1p*mp*(1-xp)) + np.sum(rho1m*mm*xm),
                     U0*(1-xu) + np.sum(rho2p*mp*xp) + np.sum(rho2m*mm*(1-xm))])
def sec(X):
    xp, xm, xu = X
    return np.array([np.sum(Up*rho1p*mp*xp) - np.sum(Vm*rho1m*mm*xm),
                     np.sum((Up-3)*rho2p*mp*xp) + np.sum((3-Vm)*rho2m*mm*xm)])
def C(u):  # pointwise minimiser of S1 + u psi1 (Lemma 1.1)
    return ((Up < u).astype(float), (Vm > u).astype(float), 1.0)
def leq(X, Y, i, tol=1e-13):  # X <=_i Y lexicographically
    a, b = psi(X)[i], psi(Y)[i]
    if a < b - tol: return True
    if a > b + tol: return False
    return sec(X)[i] <= sec(Y)[i] + tol
# (1) Lemma 1.1 at world 2 and Bayes property of every C_u
bad2 = badB = 0
for u in np.linspace(0.5, 1.5, 401):
    X = C(u)
    accp2 = (Up - u)*rho2p < 0; accm2 = (3-Vm)*rho2m < (3-u)*rho2m
    bad2 += np.sum(accp2 != X[0].astype(bool)) + np.sum(accm2 != X[1].astype(bool))
    # exists p in (0,1) with X Bayes at p (ties allowed): + accepted => th+ <= p, + rejected => th+ >= p, etc.
    lo = max([0.0] + list(thp[X[0] == 1]) + list(thm[X[1] == 0]))
    hi = min([1.0] + list(thp[X[0] == 0]) + list(thm[X[1] == 1]))
    badB += not (lo <= hi + 1e-12 and hi > 0 and lo < 1)
print("(1) world-2 Lagrangian mismatches:", bad2, "; C_u not psi-Bayes at an interior p:", badB, "of 401")
# (2) non-improvability via exact fractional knapsack (greedy) at both worlds
def gmin(i, x):
    if i == 0:   # error units: + bin silent (S decreases by U+), - bin accepted (S decreases by V), unanimous (0)
        base = np.sum(Up*rho1p*mp); w = np.concatenate([rho1p*mp, rho1m*mm, [U0]]); gain = np.concatenate([Up, Vm, [0.0]])
    else:        # + bin accepted (S decreases by 3-U+), - bin silent (decrease 3-V), unanimous (0)
        base = np.sum((3-Vm)*rho2m*mm); w = np.concatenate([rho2p*mp, rho2m*mm, [U0]]); gain = np.concatenate([3-Up, 3-Vm, [0.0]])
    o = np.argsort(-gain); cw = np.cumsum(w[o]); k = np.searchsorted(cw, x)
    take = np.sum((w[o]*gain[o])[:k]) + (x - (cw[k-1] if k else 0.0))*gain[o][k]
    return base - take
gap = 0.0
for u in np.linspace(0.5, 1.5, 101):
    X = C(u); P = psi(X); S = sec(X)
    for i in (0, 1): gap = max(gap, S[i] - gmin(i, P[i]))
print("(2) max S_i(C_u) - min{S_i : psi_i = psi_i(C_u)}: %.2e" % gap)
# (3) closed sections, competitiveness, KKM for arbitrary models (incl. non-regular)
ps = np.linspace(0, 1, 2001); Cs = [C(0.5 + p) for p in ps]
P1s = np.array([psi(Z)[0] for Z in Cs]); P2s = np.array([psi(Z)[1] for Z in Cs])
S1s = np.array([sec(Z)[0] for Z in Cs]); S2s = np.array([sec(Z)[1] for Z in Cs])
print("    psi1(C_p) nonincreasing:", bool(np.all(np.diff(P1s) <= 1e-15)), " psi2(C_p) nondecreasing:", bool(np.all(np.diff(P2s) >= -1e-15)))
def randmodel():
    kind = rng.integers(3)
    if kind == 0: return (rng.random(N), rng.random(N), rng.random())
    if kind == 1: return ((rng.random(N) < rng.random()).astype(float), (rng.random(N) < rng.random()).astype(float), float(rng.random() < 0.7))
    a, b = rng.random()*0.5, 0.5 + rng.random()*0.5   # coherent-shaped D_[a,b]
    return ((rp < a).astype(float), (rm > b).astype(float), 1.0)
shape_bad = kkm_bad = dom_bad = 0
for trial in range(300):
    X = randmodel()
    PX, SX = psi(X), sec(X); tol = 1e-13
    A1 = (P1s < PX[0]-tol) | ((np.abs(P1s-PX[0]) <= tol) & (S1s <= SX[0]+tol))
    A2 = (P2s < PX[1]-tol) | ((np.abs(P2s-PX[1]) <= tol) & (S2s <= SX[1]+tol))
    # A1 should be a terminal interval [a,1] (or all/empty), A2 an initial interval [0,b]
    shape_bad += (A1.any() and not np.all(A1[np.argmax(A1):])) or (A2.any() and not np.all(A2[:len(A2)-np.argmax(A2[::-1])]))
    shape_bad += not A1[-1] or not A2[0]           # vertex selections ideal
    kkm_bad += not np.all(A1 | A2)                   # covering (competitiveness)
    # exact intersection by bisection in u (grid can straddle a one-point intersection)
    def bis(f, lo, hi):
        for _ in range(60):
            mid = (lo+hi)/2
            if f(mid): hi = mid
            else: lo = mid
        return hi
    PX = psi(X)
    u1 = bis(lambda u: psi(C(u))[0] <= PX[0], 0.5, 1.5)          # A1 = [u1, 3/2]
    u2 = 2.0 - bis(lambda v: psi(C(2.0-v))[1] <= PX[1], 0.5, 1.5)  # A2 = [1/2, u2]
    if u1 > u2 + 1e-9: kkm_bad += 1; continue
    Cp = C(u1)
    same = np.abs(Cp[0]-X[0]).sum() + np.abs(Cp[1]-X[1]).sum() + abs(Cp[2]-X[2]) < 1e-9
    strict = (not leq(X, Cp, 0)) or (not leq(X, Cp, 1))
    dom_bad += not (same or strict)
print("(3) section-shape failures: %d, KKM/covering failures: %d, KKM point not dominating: %d  (300 models)" % (shape_bad, kkm_bad, dom_bad))
# (4) t0-face: incoherent face models strictly dominated at BOTH worlds by the coherent one with equal psi
Z = (rp >= r1) & (rp <= r2); zi = np.where(Z)[0]; nb = 0
base = ((rp < r1).astype(float), (rm > b0).astype(float), 1.0)
for trial in range(300):
    xp = base[0].copy(); xp[Z] = rng.random(Z.sum()) * (rng.random(Z.sum()) < rng.random())
    X = (xp, base[1], 1.0)
    w = rho1p[zi]*mp[zi]; mass = np.sum(w*xp[zi]); cw = np.cumsum(w); k = np.searchsorted(cw, mass)
    yp = base[0].copy(); yp[zi[:k]] = 1.0
    if k < zi.size: yp[zi[k]] = (mass - (cw[k-1] if k else 0.0))/w[k]
    Y = (yp, base[1], 1.0)
    okpsi = np.allclose(psi(X), psi(Y), atol=1e-14)
    if np.abs(xp - yp).sum() < 1e-9: continue
    nb += not (okpsi and sec(Y)[0] < sec(X)[0] - 1e-14 and sec(Y)[1] < sec(X)[1] - 1e-14)
print("(4) incoherent t0-face models NOT strictly dominated at both worlds: %d / 300" % nb)
# (5) index is not the Bayes weight; target on the plateau
u = 0.5 + 0.3; X = C(u)
print("(5) C_{u(0.3)} accepts + up to r =", rp[X[0] == 1].max().round(4), "(0.3-face has + cut in [0.2,0.3]); target T = C_{0.875}: + cut",
      rp[C(0.875)[0] == 1].max().round(4), ", - cut", rm[C(0.875)[1] == 1].min().round(4))
