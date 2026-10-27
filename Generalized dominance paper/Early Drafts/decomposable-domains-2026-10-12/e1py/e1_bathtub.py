"""E1.2 (R3 without the case split): starting from the admissible shadow nu^L (T1 is nu^L-Bayes at u), inflate the
correct-world densities by M off a thin cone C_eta inside D_T1; T1 stays Bayes at u, while at a weight t near e_j
(w_j < 0) the Bayes model is T1 minus part of C_eta, an incoherent model within mu(C_eta) of T1.
NUMERICS only. Run: python3 -I e1_bathtub.py"""
import numpy as np
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e1_common import *

rng = np.random.default_rng(11)
G = sample_U(rng, 400000)
T = in_DT(G)
COR = correct(G, T)
L = 5.0
W = np.where(COR, L, 1.0)
acc_u, tie_u = bayes(G, W, u)
print("nu^L: B_u == T1 on all samples:", bool(np.all(acc_u == T)), " ties:", int(tie_u.sum()))

w = np.array([1.0, 1.0, -0.3]); w /= np.linalg.norm(w)
print("ray w in D_T1:", bool(in_DT(w[None])[0]))
for theta in [0.20, 0.10, 0.05]:
    cosang = G @ w
    Ceta = cosang > np.cos(theta)
    # closure of C_eta inside D_T1: check on a ring of boundary directions
    a = np.cross(w, [0, 0, 1.0]); a /= np.linalg.norm(a); b = np.cross(w, a)
    ring = np.array([np.cos(theta) * w + np.sin(theta) * (np.cos(p) * a + np.sin(p) * b) for p in np.linspace(0, 2 * np.pi, 720)])
    for d in [0.02, 0.01, 0.005]:
        t = np.array([d, d, 1 - 2 * d])
        M = 2 / t.min() + 1
        W2 = W.copy()
        W2[COR & ~Ceta[:, None]] *= M
        acc_u2, tie_u2 = bayes(G, W2, u)
        acc_t, tie_t = bayes(G, W2, t)
        removed = T & ~acc_t
        ok_off = np.all(acc_t[~Ceta] == T[~Ceta])
        ok_sub = not np.any(acc_t & ~T)
        frac = removed[Ceta].sum() / max(1, Ceta.sum())
        # convexity witness: a removed g that is the midpoint of two accepted samples-free points g +- r*d in D_T1 \ C_eta
        wit = 0
        idx = np.where(removed)[0][:200]
        for k in idx:
            g = G[k]
            for _ in range(20):
                dvec = rng.normal(size=3); dvec -= (dvec @ g) * g; dvec /= np.linalg.norm(dvec)
                p1, p2 = g + 0.6 * dvec, g - 0.6 * dvec
                P = np.array([p1, p2])
                if np.all(in_DT(P)) and np.all((P / np.linalg.norm(P, axis=1, keepdims=True)) @ w < np.cos(theta)):
                    A, _ = bayes(P, np.where(correct(P, in_DT(P)), L * M, 1.0), t)
                    if np.all(A):
                        wit += 1
                        break
        print(f"theta={theta:.2f} mu(C_eta)/mu(U)~{Ceta.mean():.2e} t=({d},{d},{1-2*d}) ring in D_T1:{bool(np.all(in_DT(ring)))} "
              f"B'_u==T1:{bool(np.all(acc_u2 == T))} ties_t:{int(tie_t.sum())} B'_t==T1 off C_eta:{bool(ok_off)} "
              f"B'_t subset T1:{ok_sub} removed frac of C_eta:{frac:.3f} midpoint witnesses:{wit}/{len(idx)}")
