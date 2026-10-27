#!/usr/bin/env python3
"""P2 / holonomy_onekink.py (NUMERICS): as holonomy_pl.py, but only ONE facet (F_m) may have a kink;
the other two facet maps are linear (rates x_k). Also refines the box test on a 20000-point grid
and checks orientation (monotone rotation) on every sector.  Usage: python3 -I holonomy_onekink.py eps m ntrials"""
import sys
import numpy as np
from scipy.optimize import minimize, fsolve
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import holonomy_pl as H

M = int(sys.argv[2]) if len(sys.argv) > 2 else 0
NTR = int(sys.argv[3]) if len(sys.argv) > 3 else 8

def unpack(z):
    P = {}
    zz = list(z)
    for k in range(3):
        if k == M:
            lamA, alA, beA, alB, tb = zz[:5]; zz = zz[5:]
            ti, tj = H.cross_tau(k, H.FAC[k]['i']), H.cross_tau(k, H.FAC[k]['j'])
            tb = ti + (tj - ti) / (1 + np.exp(-tb))
            P[k] = (np.exp(lamA), alA, np.exp(beA), 1.0, alB, 0.0, tb)
        else:
            lx = zz[0]; zz = zz[1:]
            x = np.exp(lx)
            P[k] = (x, 0.0, 1.0, 1.0, x, 0.0, 0.5)
    Q = H.continuity_fix({M: P[M]} | {k: (0, 0, 1, 1, 0, 0, .5) for k in range(3) if k != M})
    for k in range(3):
        if k != M: Q[k] = P[k]
    return Q

def obj(z):
    P = unpack(z)
    ns = H.ns_residual(P)
    sv = H.sign_violation(P, tau=np.linspace(0, 1, 161)[1:-1])
    bm, _ = H.box_margin(P, tau=np.linspace(0, 1, 161)[1:-1])
    return 50 * (ns ** 2).sum() + 50 * min(0, sv) ** 2 - min(bm, 0.05)

def polish(z):
    # free for NS: the two linear rates and alB of the kinked facet
    idx = [3, 5, 6]
    def F(y):
        w = np.array(z, float); w[idx] = y
        return H.ns_residual(unpack(w))[0::2]
    y = fsolve(F, np.array(z)[idx], xtol=1e-14)
    w = np.array(z, float); w[idx] = y
    return w

def orient(P):
    out = []
    for k in range(3):
        lamA, alA, beA, lamB, alB, beB, tb = P[k]
        out.append((lamA * beA, alB * lamB))
    return out

if __name__ == '__main__':
    rng = np.random.default_rng(7 + M)
    best = None
    for t in range(NTR):
        z0 = rng.normal(0, 0.7, 7)
        r = minimize(obj, z0, method='Nelder-Mead', options=dict(maxiter=8000, xatol=1e-10, fatol=1e-13))
        if best is None or r.fun < best.fun: best = r
    zb = polish(best.x)
    P = unpack(zb)
    print(f"eps={H.EPS} kinked facet F_{M+1}")
    print("  NS residual", np.abs(H.ns_residual(P)).max())
    tau = np.linspace(0, 1, 20001)[1:-1]
    print("  sign check (>=0 ok)", H.sign_violation(P, tau=tau))
    print("  sector determinants (all >0 = monotone rotation)", np.round(orient(P), 6))
    bm, arg = H.box_margin(P, tau=tau)
    print("  box margin, 20000-pt grid (>=0 ok)", bm, arg)
    for k in range(3):
        print("  facet", k + 1, np.round(P[k], 6))
    np.save(f"holonomy_onekink_F{M+1}_eps{H.EPS}.npy", zb)
