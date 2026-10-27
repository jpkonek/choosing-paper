#!/usr/bin/env python3
"""P2P3 referee: independent Monte Carlo check of P3 Examples 1 and 2 (own code).
eps=0.3, K' = u + 0.9(T1-u). Gaussian mu on R^3. Models = subsets of U = D_{K'}."""
import numpy as np
rng = np.random.default_rng(12345)
eps, s = 0.3, 0.9
u = np.ones(3)/3
T1v = [(1-eps)*u + eps*np.eye(3)[k] for k in range(3)]
Kv = [u + s*(v-u) for v in T1v]
def P(vs, h): return np.min(np.stack([h@v for v in vs]), axis=0)
N = 4_000_000
H = rng.standard_normal((N,3))
inU = (P(Kv,H) > 0) | np.all(H >= 0, axis=1)
Hu = H[inU]; print("mu(U) fraction", inU.mean())
# ---------- Example 1
a = np.array([-0.1, 1, 1.]); ap = np.array([1, -0.1, -0.1]); r = np.array([.5,.5,0.])
print("P_T1(a), P_T1(a')", P(T1v,a), P(T1v,ap), " r.a, r.a'", r@a, r@ap)
def cone(c, rad):   # conic ball: angle-based, equal angular radius
    cn = c/np.linalg.norm(c); x = Hu/np.linalg.norm(Hu,axis=1)[:,None]
    return np.linalg.norm(x - cn, axis=1) < rad
A = cone(a, 0.035) | cone(ap, 0.035)
print("A fraction of U", A.mean(), " A inside D_T1:", np.all(P(T1v,Hu[A])>0), " inside B_r:", np.all(Hu[A]@r>0))
# Comp(1_A) = {q : q.h>0 on A}; check vertices and edge points
def inComp(q): return np.all(Hu[A]@q > 0)
for name,q in [("e1",[1,0,0]),("e2",[0,1,0]),("e3",[0,0,1]),("u",u),("r=(.5,.5,0)",r),("(.5,0,.5)",[.5,0,.5]),("(0,.5,.5)",[0,.5,.5])]:
    print("  ", name, "in Comp:", inComp(np.array(q,float)))
# signs of sigma*sgn_i on A
for i in range(3):
    sg = np.sign(Hu[A][:,i]); print(f"  world {i+1}: sigma*sgn takes +1: {np.any(sg>0)}, -1: {np.any(sg<0)};  int_A h_i = {Hu[A][:,i].sum()/N:.4e}")
# ---------- Example 2
p0 = np.array([.6,.2,.2]); print("p0 in K'?  P_{K'} test: p0 not in K' since min over... ", )
d1 = 0.05
def rk(d): return p0 + d*(np.array([1,0,0.])-p0)
Bp0 = Hu@p0 > 0
Wp = (Hu[:,0] < 0) & (Hu@rk(d1) > 0)
print("W' fraction of U", Wp.mean(), " W' subset B_p0:", np.all(Bp0[Wp]))
w = np.abs(Hu[Wp,0]).sum()/N
print("w = int_W' |h1| dmu =", w)
eta = 0.05
for d in [0.05, 0.02, 0.01, 0.005, 0.002, 0.001]:
    Br = Hu@rk(d) > 0
    assert np.all(Br[Wp]), "W' not inside B_rk"
    Sh = Bp0 & ~Br
    assert np.all(Hu[Sh,0] < 0)
    G_plus = Hu[Br & ~Bp0, 0].sum()/N           # >= 0
    G_sh = np.abs(Hu[Sh,0]).sum()/N
    ak = np.abs(Hu[Sh & (Hu[:,0] <= -eta*np.linalg.norm(Hu,axis=1)),0]).sum()/N
    # with rho=1 (fixed): psi_1(B_rk) - psi_1(X) = w - G_k ; G_k = G_sh + G_plus
    print(f" delta={d}: G_k(rho=1)={G_sh+G_plus:.4e} (vs w={w:.4e}) ; a_k={ak:.4e} ; M needed ~ (w)/a_k = {w/ak if ak>0 else np.inf:.1f}")
# all h in U with p0.h ~ 0 have h1<0 (analytic: 3h1+h2+h3=0 and 2h1-h2-h3<0 -> h1<0)
near = np.abs(Hu@p0) < 1e-3*np.linalg.norm(Hu,axis=1)
print("on U near p0-perp: max h1/|h| =", (Hu[near,0]/np.linalg.norm(Hu[near],axis=1)).max())
