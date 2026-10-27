#!/usr/bin/env python3
"""P2 / holonomy_flat.py (NUMERICS; python3 -I holonomy_flat.py eps)

Degenerate kink ('flat sector'): on F_1 the facet map has CONSTANT direction on the corner sector
[r12, b] (b strictly between r12 and the first crossing w21), and is linear (crossing rows x1, 1)
on [b, r31]; F_2, F_3 linear (rates x2, x3).  Constant direction on a sector = all those facet
gambles share ONE chart line through p* (an atom chord through the target weighting, configuration
R-a' of the write-up).  Unknowns x1, x2, x3, tau_b; equations: NS at the three corners.
We scan tau_b, solve NS for (x1,x2,x3) and evaluate the exact box reduction (holonomy_pl.box_margin)
on a crossing-refined grid; strict signs are checked, rotation is required to be weakly monotone.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import fsolve
import holonomy_pl as H

def params(x1, x2, x3, tb):
    # F_1 linear part L1: c_2 = x1 h_2, c_3 = h_3 ; on [r12,b] direction frozen at L1(b)
    return {0: ('flat', x1, tb), 1: (x2, 0.0, 1.0, 1.0, x2, 0.0, 0.5), 2: (x3, 0.0, 1.0, 1.0, x3, 0.0, 0.5)}

def chart_flat(k, h, P):
    if k != 0 or P[0][0] != 'flat':
        return H.chart(k, h, P)
    _, x1, tb = P[0]
    f = H.FAC[0]
    L = lambda g: np.array([-(x1 * g[1] + g[2]), x1 * g[1], g[2]])
    b = H.pt(0, tb)
    Mt = np.array([f['ri'][[1, 2]], b[[1, 2]]]).T
    lam, mu = np.linalg.solve(Mt, h[[1, 2]])
    if lam >= -1e-12 and mu >= -1e-12:           # sector [r12, b]: constant direction L(b)
        return (lam * 1.0 + mu) * L(b)
    return L(h)

def charts_flat(k, tau, P):
    Hs = np.array([H.pt(k, t) for t in tau]); C = np.array([chart_flat(k, h, P) for h in Hs])
    return Hs, C

def box_margin(P, tau):
    HC = [charts_flat(k, tau, P) for k in range(3)]
    Hh = np.vstack([x[0] for x in HC]); C = np.vstack([x[1] for x in HC])
    worst = np.inf
    for a in range(3):
        for b in range(3):
            if a == b: continue
            mA = (Hh[:, a] < 0) & (Hh[:, b] > 0) & (C[:, a] < 0) & (C[:, b] > 0)
            mB = (Hh[:, b] < 0) & (Hh[:, a] > 0) & (C[:, b] < 0) & (C[:, a] > 0)
            if not mA.any() or not mB.any(): continue
            rho = Hh[mA, b] / -Hh[mA, a]; sA = C[mA, b] / (C[mA, b] - C[mA, a])
            sig = -Hh[mB, b] / Hh[mB, a]; sB = -C[mB, b] / (C[mB, a] - C[mB, b])
            o = np.argsort(-sig); sig = sig[o]; sB = np.minimum.accumulate(sB[o])
            n = np.searchsorted(-sig, -rho, side='left'); ok = n > 0
            if ok.any(): worst = min(worst, (sB[n[ok] - 1] - sA[ok]).min())
    return worst

def signs(P, tau):
    w = np.inf
    for k in range(3):
        Hs, C = charts_flat(k, tau, P)
        for h, c in zip(Hs, C):
            for l in range(3):
                if abs(h[l]) > 1e-3 * np.linalg.norm(h):
                    w = min(w, c[l] * np.sign(h[l]) / np.linalg.norm(c))
    return w

def ns(P):
    out = []
    for (k, j, r) in [(0, 1, H.R12), (1, 2, H.R23), (2, 0, H.R31)]:
        a = chart_flat(k, r, P); b = chart_flat(j, r, P)
        a2 = a - a.mean(); b2 = b - b.mean()
        out.append((a2[0] * b2[1] - a2[1] * b2[0]) / (np.linalg.norm(a2) * np.linalg.norm(b2)))
    return np.array(out)

if __name__ == '__main__':
    tw = H.cross_tau(0, 1)          # first crossing on F_1 (coordinate 2)
    tau = np.unique(np.concatenate([np.linspace(0, 1, 1601)[1:-1],
                                    *[np.clip(c + s * np.geomspace(1e-7, 0.05, 120), 1e-9, 1 - 1e-9)
                                      for c in [0, 1, tw, H.cross_tau(0, 2), H.cross_tau(1, 2), H.cross_tau(1, 0),
                                                H.cross_tau(2, 0), H.cross_tau(2, 1)] for s in (-1, 1)]]))
    print(f"eps={H.EPS} kappa={H.KAP:.4f}; first crossing on F_1 at tau={tw:.4f}")
    best = None
    x0 = np.array([1.0, 1.0, 1.0])
    for frac in np.linspace(0.05, 0.95, 19):
        tb = frac * tw
        for guess in [x0, np.array([2.9, 2.9, 2.9]), np.array([0.34, 0.34, 0.34]), np.array([1.5, 0.7, 1.2])]:
            sol, info, ier, msg = fsolve(lambda y: ns(params(*np.abs(y), tb)), guess, full_output=True, xtol=1e-13)
            if ier != 1: continue
            x = np.abs(sol); P = params(*x, tb)
            if np.abs(ns(P)).max() > 1e-10: continue
            # NS also needs positive (not anti-) proportionality
            okpos = all(((chart_flat(k, r, P) - chart_flat(k, r, P).mean()) @ (chart_flat(j, r, P) - chart_flat(j, r, P).mean())) > 0
                        for (k, j, r) in [(0, 1, H.R12), (1, 2, H.R23), (2, 0, H.R31)])
            if not okpos: continue
            sg = signs(P, np.linspace(0, 1, 801)[1:-1])
            bm = box_margin(P, tau)
            print(f"  tau_b={tb:.4f}  x=({x[0]:.5f},{x[1]:.5f},{x[2]:.5f})  sign margin {sg:.2e}  box margin {bm:.3e}")
            if sg > 0 and (best is None or bm > best[0]): best = (bm, tb, x)
    print("best:", best)
