#!/usr/bin/env python3
"""P2 / holonomy_flatmid.py (NUMERICS; python3 -I holonomy_flatmid.py eps ntrials)

Degenerate kink in the MIDDLE of F_1: the facet map of F_1 is linear on [r12, b1] (containing the
crossing w21; c_2 = lamA h_2, c_3 = alA h_2 + beA h_3), has CONSTANT direction on [b1, b2]
(w21 < b1 < b2 < w31), and is linear on [b2, r31] (containing w31; c_3 = lamB h_3, c_2 = gam h_2 + del h_3)
with L_B(b2) parallel to L_A(b1).  F_2, F_3 linear.  The flat middle sector means: all facet gambles of
that sub-arc have ONE chart line, an atom chord through p* of sign pattern (-,+,+) (cf. Thm pstarE).
Search: maximise the exact box margin subject to exact NS (polished), strict signs, monotone (weak) rotation.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import minimize, fsolve
import holonomy_pl as H

F = H.FAC[0]
T21, T31 = H.cross_tau(0, 1), H.cross_tau(0, 2)

def unpack(z):
    lamA, alA, beA, lamB, gam, s1, s2, lx2, lx3 = z
    lamA, beA, lamB = np.exp(lamA), np.exp(beA), np.exp(lamB)
    u1, u2 = 1 / (1 + np.exp(-s1)), 1 / (1 + np.exp(-s2))
    W = float(os.environ.get('FLATW', '0'))          # minimum flat width as a fraction of the middle arc
    lo = u1 * (1 - W); tb1 = T21 + (T31 - T21) * lo; tb2 = T21 + (T31 - T21) * (lo + W + (1 - W - lo) * u2 * 0)
    b1, b2 = H.pt(0, tb1), H.pt(0, tb2)
    cA = np.array([lamA * b1[1], alA * b1[1] + beA * b1[2]])          # (c_2, c_3) at b1
    # L_B(b2) = (gam b2_2 + del b2_3, lamB b2_3) parallel to cA:
    #   (gam b2_2 + del b2_3) * cA[1] = lamB b2_3 * cA[0]
    dl = (lamB * b2[2] * cA[0] / cA[1] - gam * b2[1]) / b2[2]
    return dict(lamA=lamA, alA=alA, beA=beA, lamB=lamB, gam=gam, dl=dl, tb1=tb1, tb2=tb2,
                x2=np.exp(lx2), x3=np.exp(lx3))

def c1(h, q):
    """chart of F_1 at h (homogeneous)."""
    b1, b2 = H.pt(0, q['tb1']), H.pt(0, q['tb2'])
    def LA(g): c2 = q['lamA'] * g[1]; c3 = q['alA'] * g[1] + q['beA'] * g[2]; return np.array([-(c2 + c3), c2, c3])
    def LB(g): c3 = q['lamB'] * g[2]; c2 = q['gam'] * g[1] + q['dl'] * g[2]; return np.array([-(c2 + c3), c2, c3])
    def coords(x, y):
        M = np.array([x[[1, 2]], y[[1, 2]]]).T
        return np.linalg.solve(M, h[[1, 2]])
    l, m = coords(F['ri'], b1)
    if l >= -1e-12 and m >= -1e-12: return LA(h)
    l, m = coords(b2, F['rj'])
    if l >= -1e-12 and m >= -1e-12: return LB(h)
    l, m = coords(b1, b2)        # flat sector: direction of LA(b1), positive homogeneous weight
    d = LA(b1) / np.linalg.norm(LA(b1))
    return (l * np.linalg.norm(LA(b1)) + m * np.linalg.norm(LB(b2))) * d

def chart(k, h, q):
    if k == 0: return c1(h, q)
    x = q['x2'] if k == 1 else q['x3']
    return H.chart(k, h, {k: (x, 0.0, 1.0, 1.0, x, 0.0, 0.5)})

def allcharts(tau, q):
    out = []
    # facet 1 vectorised
    Hs = (1 - tau)[:, None] * F['ri'][None, :] + tau[:, None] * F['rj'][None, :]
    b1, b2 = H.pt(0, q['tb1']), H.pt(0, q['tb2'])
    C = np.zeros_like(Hs)
    A = tau <= q['tb1']; B = tau >= q['tb2']; M = ~(A | B)
    c2 = q['lamA'] * Hs[:, 1]; c3 = q['alA'] * Hs[:, 1] + q['beA'] * Hs[:, 2]
    C[A, 1], C[A, 2] = c2[A], c3[A]
    c3b = q['lamB'] * Hs[:, 2]; c2b = q['gam'] * Hs[:, 1] + q['dl'] * Hs[:, 2]
    C[B, 1], C[B, 2] = c2b[B], c3b[B]
    LAb1 = np.array([q['lamA'] * b1[1], q['alA'] * b1[1] + q['beA'] * b1[2]])
    LBb2 = np.array([q['gam'] * b2[1] + q['dl'] * b2[2], q['lamB'] * b2[2]])
    Mt = np.array([b1[[1, 2]], b2[[1, 2]]]).T
    lm = np.linalg.solve(Mt, Hs[M][:, [1, 2]].T).T
    d = LAb1 / np.linalg.norm(LAb1)
    wgt = lm[:, 0] * np.linalg.norm(LAb1) + lm[:, 1] * np.linalg.norm(LBb2)
    C[M, 1], C[M, 2] = wgt * d[0], wgt * d[1]
    C[:, 0] = -(C[:, 1] + C[:, 2])
    out.append((Hs, C))
    for k in (1, 2):
        x = q['x2'] if k == 1 else q['x3']
        out.append(H.charts(k, tau, {k: (x, 0.0, 1.0, 1.0, x, 0.0, 0.5)}))
    return out

def box_margin(q, tau):
    HC = allcharts(tau, q)
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

def signs(q, tau):
    w = np.inf
    for Hs, C in allcharts(tau, q):
        m = np.abs(Hs) > 1e-3 * np.linalg.norm(Hs, axis=1)[:, None]
        v = C * np.sign(Hs) / np.linalg.norm(C, axis=1)[:, None]
        w = min(w, v[m].min())
    return w

def ns(q):
    out = []
    for (k, j, r) in [(0, 1, H.R12), (1, 2, H.R23), (2, 0, H.R31)]:
        a = chart(k, r, q); b = chart(j, r, q); a2 = a - a.mean(); b2 = b - b.mean()
        out.append((a2[0] * b2[1] - a2[1] * b2[0]) / (np.linalg.norm(a2) * np.linalg.norm(b2)))
        out.append(-min(0.0, a2 @ b2))
    return np.array(out)

def rot_ok(q):
    # sector determinants of the two linear pieces (flat piece has det 0 by construction)
    return q['lamA'] * q['beA'] > 0 and q['lamB'] * q['gam'] > 0

TAU_C = np.linspace(0, 1, 121)[1:-1]
def obj(z):
    q = unpack(z)
    if not np.isfinite(q['dl']): return 1e6
    return 50 * (ns(q) ** 2).sum() + 50 * min(0, signs(q, TAU_C)) ** 2 - min(box_margin(q, TAU_C), 0.05) + (0 if rot_ok(q) else 1)

if __name__ == '__main__':
    ntr = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    rng = np.random.default_rng(11)
    best = None
    for t in range(ntr):
        z0 = rng.normal(0, 0.6, 9)
        r = minimize(obj, z0, method='Nelder-Mead', options=dict(maxiter=5000, xatol=1e-9, fatol=1e-12))
        if best is None or r.fun < best.fun: best = r
    z = best.x.copy()
    idx = [4, 7, 8]
    y = fsolve(lambda y: ns(unpack(np.concatenate([z[:4], [y[0]], z[5:7], y[1:]])))[0::2], z[idx], xtol=1e-14)
    z = np.concatenate([z[:4], [y[0]], z[5:7], y[1:]])
    q = unpack(z)
    tau = np.unique(np.concatenate([np.linspace(0, 1, 3001)[1:-1],
                                    *[np.clip(c + s * np.geomspace(1e-8, 0.05, 150), 1e-10, 1 - 1e-10)
                                      for c in [0, 1, T21, T31, q['tb1'], q['tb2'], H.cross_tau(1, 2), H.cross_tau(1, 0),
                                                H.cross_tau(2, 0), H.cross_tau(2, 1)] for s in (-1, 1)]]))
    print(f"eps={H.EPS}: flat middle sector on F_1, tau in [{q['tb1']:.4f},{q['tb2']:.4f}] (crossings {T21:.4f},{T31:.4f})")
    print("  NS residual", np.abs(ns(q)).max(), " rotation ok", rot_ok(q))
    print("  sign margin", signs(q, np.linspace(0, 1, 2001)[1:-1]))
    print("  box margin (refined grid)", box_margin(q, tau))
    print("  params", {k: round(float(v), 6) for k, v in q.items()})
    np.save(f"holonomy_flatmid_eps{H.EPS}.npy", z)
