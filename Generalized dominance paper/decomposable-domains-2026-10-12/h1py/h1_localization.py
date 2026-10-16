"""H1 NUMERICS (illustrative only; no proof depends on it).

Setting: T1 with eps=0.3, U = D_{K'}, K' = u + s(T1-u), s=0.9; shadow nu^L (L=5) of Prop Q31.
At a weight t in I_nu (null ties, incoherent Bayes set B_t) we estimate by Monte Carlo
  Phi(Y) := int_{Y triangle B_t} |t.c| dmu
(1) for the localized corrections X_m := B_t made world-1-correct on the collar
    D_m = {P_{K'}(h) < 2^{-m}|h|} cap {h_1 < 0}  (an end at dU cap {h_1<0}),
(2) for many coherent models D_K (random credal sets K containing K'), to see that
    d_t = min_coherent Phi stays bounded away from 0 while Phi(X_m) -> 0  (Lemma H1.0 / Thm H1.2).
(3) incoherence of B_t (midpoint test).
"""
import numpy as np
rng = np.random.default_rng(20261015)
eps, s, L = 0.3, 0.9, 5.0
u = np.ones(3)/3
V = np.array([(1-eps)*u + eps*np.eye(3)[k] for k in range(3)])          # vertices of T1
Vp = np.array([u + s*(v-u) for v in V])                                  # vertices of K'
def P(Kpts, g):                      # lower prevision, g: (n,3)
    return (g @ Kpts.T).min(axis=1)
N = 1_500_000
g = rng.standard_normal((N,3))
inU = P(Vp, g) > 0
g = g[inU]; n = len(g); wmass = 1.0/N                                  # mu-mass per sample (mu standard Gaussian)
sig = np.sign(g)
inT = P(V, g) > 0
corr = np.where(inT[:,None], sig > 0, sig < 0)                         # T1 correct at world i
w = np.where(corr, L, 1.0)
c = w*sig
def bayes(t): return (c @ t) > 0
def Phi(Y, B, tc): return np.abs(tc)[Y != B].sum()*wmass
nonneg = (g > 0).all(axis=1)
print(f"samples in U: {n};  B_u == T1 on all samples: {np.all(bayes(u)==inT)}")
for t in (np.array([0.45,0.45,0.10]), np.array([0.15,0.15,0.70])):
    tc = c @ t; B = tc > 0
    print(f"\n t = {t}:  mu(B_t xor T1) = {(B!=inT).sum()*wmass:.4f}")
    # (3) incoherence: midpoints of accepted pairs that are rejected (cone not convex)
    gu = g/np.linalg.norm(g,axis=1)[:,None]; A = gu[B]
    a = A[rng.integers(0,len(A),40000)]; b = A[rng.integers(0,len(A),40000)]
    mid = 0.5*(a+b); ok = P(Vp, mid) > 0; mo = mid[ok]; sm = np.sign(mo)
    cm = sm*np.where(np.where((P(V, mo) > 0)[:,None], sm > 0, sm < 0), L, 1.0)
    print(f"   midpoints of accepted pairs that B_t rejects: {int(((cm @ t) < 0).sum())} of {int(ok.sum())} (>0 => B_t not convex, incoherent)")
    # (1) localized corrections on the dU collar in {h1<0}
    rel = P(Vp, g)/np.linalg.norm(g, axis=1)
    for m in range(2, 11, 2):
        Dm = (rel < 2.0**-m) & (g[:,0] < 0)
        X = B.copy(); X[Dm] = False                                     # world-1-correct on D_m (reject h1<0)
        print(f"   m={m:2d}: mu(D_m)={Dm.sum()*wmass:.2e}  Phi(X_m)={Phi(X,B,tc):.2e}")
    # (2) coherent models: random credal sets K = co(K' + up to 4 random points of Delta)
    sub = rng.choice(n, 300_000, replace=False)
    def phiK(K):
        DK = (P(K, g[sub]) > 0) | nonneg[sub]
        return np.abs(tc[sub])[DK != B[sub]].sum()*wmass*n/len(sub)
    cands = [V, Vp] + [np.vstack([Vp, np.eye(3)[k]]) for k in range(3)]
    for _ in range(1500):
        k = rng.integers(1, 6)
        cands.append(np.vstack([Vp, rng.dirichlet(np.ones(3)*rng.choice([0.3, 1, 3]), size=k)]))
    vals = [phiK(K) for K in cands]
    order = np.argsort(vals)[:20]; best = vals[order[0]]
    for i in order:                                   # local refinement by random perturbation
        K = cands[i]; v = vals[i]
        for _ in range(150):
            K2 = K.copy(); j = rng.integers(len(Vp), len(K)) if len(K) > len(Vp) else None
            if j is None: break
            p = np.clip(K2[j] + 0.05*rng.standard_normal(3), 1e-6, None); K2[j] = p/p.sum()
            v2 = phiK(K2)
            if v2 < v: K, v = K2, v2
        best = min(best, v)
    cands = cands  # for the count below
    print(f"   min Phi over {len(cands)} coherent D_K (upper estimate of d_t): {best:.3e}")
