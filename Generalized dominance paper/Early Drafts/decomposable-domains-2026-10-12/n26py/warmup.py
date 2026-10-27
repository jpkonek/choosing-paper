"""N26 warm-up (n = 2) NUMERICS. Discretised check of the lexicographic system of N26 §1.
Mixed problems are binned by r = -g2/(g1-g2); a model is a vector of acceptance fractions per bin
(relaxation is exact for ranges by Lyapunov). Unanimous mass is lumped into one bin, always accepted
by the candidates. Checks: (1) path; (2) non-improvability of each C_u at both worlds (LP);
(3) random t0-face models dominated by the coherent one with the same psi-profile; (4) monotone,
continuous primaries along u (closed sections)."""
import numpy as np
from scipy.optimize import linprog

a, b = 0.5, 0.5                      # K' = {1/2}
r1, r2, t0 = 0.2, 0.3, 0.3           # plateau of theta on the + side
N = 4000
rp = (np.arange(N)+0.5)/N*a          # + side bins, r in (0, a)
rm = b + (np.arange(N)+0.5)/N*(1-b)  # - side bins, r in (b, 1)
dens = lambda r: 1.0 + 0.5*np.sin(3*r)   # any positive density of r
wp, wm = dens(rp)*a/N, dens(rm)*(1-b)/N
def th_plus(r):
    return np.where(r <= r1, 0.2 + 0.5*r, np.where(r <= r2, t0, 0.3 + 0.5*(r - r2)))
def th_minus(r):
    return 0.1 + 0.8*(r - b)/(1 - b)
tp, tm = th_plus(rp), th_minus(rm)
# error weights rho1 = 1-theta, rho2 = theta (mixed); 1 on unanimous (mass U0)
U0 = 1.0
r1p, r2p = (1-tp)*wp, tp*wp          # + side: silence = error at 1 (weight r1p), accept = error at 2 (r2p)
r1m, r2m = (1-tm)*wm, tm*wm          # - side: accept = error at 1 (r1m), silence = error at 2 (r2m)

def psi(xp, xm, xu=1.0):
    P1 = U0*(1-xu) + np.sum(r1p*(1-xp)) + np.sum(r1m*xm)
    P2 = U0*(1-xu) + np.sum(r2p*xp) + np.sum(r2m*(1-xm))
    return P1, P2

# Bayes path: alpha_B(p), beta_B(p); plateau segment inserted at t0
ps = np.linspace(0, 1, 2001)
def alphaB(p):
    acc = rp[tp < p]; return acc.max()+0.5*a/N if acc.size else 0.0
def betaB(p):
    acc = rm[tm > p]; return acc.min()-0.5*(1-b)/N if acc.size else 1.0
path = [(alphaB(p), betaB(p)) for p in ps if abs(p - t0) > 1e-9]
beta0 = betaB(t0)
path += [(al, beta0) for al in np.linspace(r1, r2, 201)]
path = sorted(set((round(x, 6), round(y, 6)) for x, y in path), key=lambda z: z[0]+z[1])
us = np.array([x+y for x, y in path]); A = np.array([x for x, y in path]); B = np.array([y for x, y in path])
assert np.all(np.diff(A) >= -1e-9) and np.all(np.diff(B) >= -1e-9), "path not monotone"
# U^+(r) = inf{u : alpha(u) > r},  V(r) = sup{u : beta(u) < r}
def Uplus(r):
    idx = np.searchsorted(A, r, side='right'); return us[min(idx, len(us)-1)]
def Vfun(r):
    idx = np.searchsorted(B, r, side='left') - 1; return us[max(idx, 0)]
Up = np.array([Uplus(r) for r in rp]); Vm = np.array([Vfun(r) for r in rm])
M3 = 3.0
# secondaries: cost of accepting a bin
s1p, s1m = Up*(1-tp)*wp, -Vm*(1-tm)*wm
s2p, s2m = (Up - M3)*tp*wp, (M3 - Vm)*tm*wm
def sec(xp, xm):
    return np.sum(s1p*xp)+np.sum(s1m*xm), np.sum(s2p*xp)+np.sum(s2m*xm)
def model(al, be):
    return (rp < al).astype(float), (rm > be).astype(float)

# (2) non-improvability: min S_i s.t. P_i = P_i(C_u), 0<=x<=1 (unanimous fraction free)
def lp_min(i, target):
    # variables: xp (N), xm (N), xu (1)
    if i == 1:
        c = np.concatenate([s1p, s1m, [0.0]])
        Aeq = np.concatenate([-r1p, r1m, [-U0]]); beq = target - U0 - r1p.sum()
    else:
        c = np.concatenate([s2p, s2m, [0.0]])
        Aeq = np.concatenate([r2p, -r2m, [-U0]]); beq = target - U0 - r2m.sum()
    res = linprog(c, A_eq=[Aeq], b_eq=[beq], bounds=[(0, 1)]*(2*N+1), method='highs')
    return res.fun
worst = 0.0
for k in np.linspace(0, len(path)-1, 25).astype(int):
    al, be = path[k]; xp, xm = model(al, be); P = psi(xp, xm); S = sec(xp, xm)
    for i in (1, 2):
        gap = S[i-1] - lp_min(i, P[i-1]); worst = max(worst, gap)
print("(2) max (S_i(C_u) - min_{P_i = P_i(C_u)} S_i) over 25 path points, both worlds: %.2e" % worst)

# (3) random face models at t0: accept r<r1 on + side, random subset of plateau, beta0 on - side
rng = np.random.default_rng(0)
Z = (rp >= r1) & (rp <= r2); bad = 0
for trial in range(200):
    xp, xm = model(r1, beta0); xp = xp.copy()
    xp[Z] = (rng.random(Z.sum()) < rng.random()).astype(float)
    P = psi(xp, xm); S = sec(xp, xm)
    # coherent face model with the same P1: alpha solving mass equation
    mass = np.sum(r1p[Z]*xp[Z]); cum = np.cumsum(r1p[Z]); j = np.searchsorted(cum, mass)
    xc, xmc = model(r1, beta0); xc = xc.copy(); zi = np.where(Z)[0]
    xc[zi[:j]] = 1.0
    if j < len(zi): xc[zi[j]] = (mass - (cum[j-1] if j else 0.0))/r1p[zi[j]]
    Pc = psi(xc, xmc); Sc = sec(xc, xmc)
    ok = abs(Pc[0]-P[0]) < 1e-12 and abs(Pc[1]-P[1]) < 1e-9 and Sc[0] <= S[0]+1e-12 and Sc[1] <= S[1]+1e-12
    strict = (Sc[0] < S[0]-1e-12) or (Sc[1] < S[1]-1e-12)
    bad += (not ok) or (not strict and np.abs(xc-xp).sum() > 1e-6)
print("(3) random incoherent t0-face models not dominated by the coherent one: %d / 200" % bad)

# (4) primaries along u: P1 strictly decreasing, P2 strictly increasing
P1s, P2s = zip(*[psi(*model(al, be)) for al, be in path])
print("(4) P1 decreasing:", bool(np.all(np.diff(P1s) <= 1e-12)), " P2 increasing:", bool(np.all(np.diff(P2s) >= -1e-12)),
      " max jump P1: %.2e" % np.max(np.abs(np.diff(P1s))))
print("plateau: psi-ties at t0 on Z: max |t0*c1 + (1-t0)*c2| =",
      np.max(np.abs(t0*r1p[Z] - (1-t0)*r2p[Z])))
