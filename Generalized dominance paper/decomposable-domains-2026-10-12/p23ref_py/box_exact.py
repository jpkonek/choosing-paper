#!/usr/bin/env python3
"""P2P3 referee: independent check of P2.2 (one kink makes chart data consistent).
Own code (does not import p2py). Reads only the saved parameter vector z from p2py/*.npy.
Box test of writeup Prop boxbridge(c), evaluated by parametrising A and B by the ratio rho/sigma
directly (exact inversion of the affine facet parametrisation), on log grids 1e-13..1e13, plus
first-order asymptotics at the crossings (where the margin tends to 0).
Usage: python3 -I box_exact.py eps npyfile [mode]  mode: onekinkF1 | linear
"""
import sys, numpy as np
eps = float(sys.argv[1]); fn = sys.argv[2]; mode = sys.argv[3] if len(sys.argv) > 3 else 'onekinkF1'
kap = (1+2*eps)/(1-eps)
R12 = np.array([-1., -1., kap+1]); R23 = np.array([kap+1, -1., -1.]); R31 = np.array([-1., kap+1, -1.])
# facet k: crossing coords i (negative at corner ri), j (negative at corner rj)
FAC = {0: (1, 2, R12, R31), 1: (2, 0, R23, R12), 2: (0, 1, R31, R23)}
v = [(1-eps)/3*np.ones(3)+eps*np.eye(3)[k] for k in range(3)]
for k,(i,j,ri,rj) in FAC.items(): assert abs(v[k]@ri)<1e-12 and abs(v[k]@rj)<1e-12
def ctau(k, c):
    i,j,ri,rj = FAC[k]; return ri[c]/(ri[c]-rj[c])
def params(z):
    P = {}
    if mode == 'linear':
        x = ((kap+1)+np.sqrt((kap+1)**2-4))/2
        for k in range(3): P[k] = ('lin', x)
        return P
    lamA, alA, beA, alB, tb = z[:5]
    lamA, beA = np.exp(lamA), np.exp(beA)
    i,j,ri,rj = FAC[0]; ti, tj = ctau(0,i), ctau(0,j)
    tb = ti+(tj-ti)/(1+np.exp(-tb)); b = (1-tb)*ri+tb*rj
    ci = lamA*b[i]; cj = alA*b[i]+beA*b[j]
    lamB = cj/b[j]; beB = (ci-alB*b[i])/b[j]
    P[0] = ('pl', lamA, alA, beA, lamB, alB, beB, tb)
    P[1] = ('lin', np.exp(z[5])); P[2] = ('lin', np.exp(z[6]))
    return P
P = params(np.load(fn) if mode != 'linear' else None)
def chart(k, tau):
    i,j,ri,rj = FAC[k]; h = (1-tau)*ri+tau*rj; c = np.zeros(3)
    p = P[k]
    if p[0]=='lin':
        c[i] = p[1]*h[i]; c[j] = h[j]          # crossing rows (rates x on row i, 1 on row j)
    else:
        _, lamA, alA, beA, lamB, alB, beB, tb = p
        if tau <= tb: c[i] = lamA*h[i]; c[j] = alA*h[i]+beA*h[j]
        else:         c[j] = lamB*h[j]; c[i] = alB*h[i]+beB*h[j]
    c[k] = -(c[i]+c[j]); return h, c
# --- checks: signs, NS, rotation
def signs():
    worst = np.inf
    for k in range(3):
        for t in np.concatenate([np.linspace(1e-6,1-1e-6,20001)]):
            h,c = chart(k,t); m = np.abs(h) > 1e-3*np.abs(h).max()
            worst = min(worst, (c*np.sign(h))[m].min()/np.abs(c).max())
    return worst
def ns():
    out=[]
    for (k,j,r) in [(0,1,R12),(1,2,R23),(2,0,R31)]:
        tk = 0.0 if np.allclose(FAC[k][2], r) else 1.0
        tj = 0.0 if np.allclose(FAC[j][2], r) else 1.0
        _,a = chart(k,tk); _,b = chart(j,tj)
        out.append(np.linalg.norm(np.cross(a,b))/np.linalg.norm(a)/np.linalg.norm(b)); out.append(a@b>0)
    return out
# --- box: parametrise by ratio
def tau_of_ratio(k, a, b, rho):
    """tau with h_b = rho*|h_a| (h_a<0<h_b): h_b + rho h_a = 0, h affine in tau."""
    i,j,ri,rj = FAC[k]; d = rj-ri
    den = d[b]+rho*d[a]
    if abs(den) < 1e-300: return None
    t = -(ri[b]+rho*ri[a])/den
    if not (0 < t < 1): return None
    h = (1-t)*ri+t*rj
    if not (h[a] < 0 < h[b]): return None
    return t
def sA_of(k, a, b, t):
    h,c = chart(k,t)
    assert c[a] < 0 < c[b], (k,a,b,t,h,c)
    return c[b]/(c[b]-c[a])
grid = np.logspace(-13, 13, 120001)
worst_abs = np.inf; worst_rel = np.inf; where=None
for a in range(3):
    for b in range(3):
        if a==b: continue
        # A side: h_a<0<h_b, ratio rho = h_b/|h_a|; B side: h_b<0<h_a, sigma = |h_b|/h_a
        SA = np.full(grid.size, -np.inf)
        for k in range(3):
            for n,r in enumerate(grid):
                t = tau_of_ratio(k,a,b,r)
                if t is not None: SA[n] = max(SA[n], sA_of(k,a,b,t))
        # sup over rho < sigma : running max shifted by one grid point (conservative lower bound of sup)
        run = np.maximum.accumulate(SA)
        for k in range(3):
            for n,s in enumerate(grid):
                if n == 0: continue
                t = tau_of_ratio(k,b,a,1/s)       # B: h_a>0>h_b, |h_b|/h_a = s  <=>  h_a/|h_b| = 1/s
                if t is None: continue
                h,c = chart(k,t)
                assert c[b] < 0 < c[a]
                sB = -c[b]/(c[a]-c[b])
                sup = run[n-1]
                if sup == -np.inf: continue
                m = sB - sup
                rel = m/min(sB, 1-sB, sup if sup>0 else 1, 1-sup if sup<1 else 1)
                if m < worst_abs: worst_abs = m
                if rel < worst_rel: worst_rel, where = rel, (a+1,b+1,k+1,s,sB,sup)
print(f"eps={eps} mode={mode} file={fn}")
print(" kink params:", P[0])
print(" sign margin (normalised, |h_l|>=1e-3|h|):", signs())
print(" NS (cross-norm, positive dot) per corner:", ns())
print(f" box: min absolute margin {worst_abs:.3e}; min RELATIVE margin {worst_rel:.4f} at (a,b,facetB,sigma,sB,supA)={where}")
