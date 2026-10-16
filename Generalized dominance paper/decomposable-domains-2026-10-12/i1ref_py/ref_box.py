"""I1 referee: independent test of Prop E, Thm R, Lemma S and the middle-window certificate on a GENUINE
CF solution, the normalised-box system K_q = nu(q (.) a), a in prod [lam_i, eta_i]  (own code).
Chart data: c(g)_i = min(lam_i g_i, eta_i g_i)  (P(q,g)>0 iff c(g).q>0), c'(g) = c(-g).
Target T = K_{p*} (a hexagon), facet gamble h of T: chord {c(h).q = 0}.

Tests
 (E) Prop E: edge limit K_{q0} (q0 on an edge) equals [Z_j, Z_i] computed from T's tangents + chords.
 (R) Thm R: for random mixed g whose zero line crosses edge E at t with e_o positive, the c-line of g passes
     through mu_o(t) and c'(g).mu_o(t) <= 0.
 (S) Lemma S: random q, random line through q: forced line L has min_{K_q} g_L = 0.
 (W) middle-window analogue: forced lines from one sign piece are concurrent (gamma = 0) for q on both sides
     of every line through p*, i.e. the certificate of Thm I1 does NOT fire on a genuine solution.
"""
import numpy as np
from itertools import product
rng=np.random.default_rng(7)
E=np.eye(3)
lam=np.array([1.0,1.0,1.0]); eta=np.array([2.0,3.0,1.5]); ps=np.array([0.3,0.3,0.4])
corners=np.array(list(product(*zip(lam,eta))))
def Kpts(q):
    m=q*corners; return m/m.sum(1,keepdims=True)
def P(q,g): return (Kpts(q)@g).min()
def c(g): return np.minimum(lam*g,eta*g)
T=Kpts(ps)
def tangents(z):
    """facet gambles of conv(T) through z (T on + side)"""
    out=[]
    for v in T:
        h=np.cross(z,v)
        if np.linalg.norm(h)<1e-13: continue
        vals=T@h
        if vals.min()>=-1e-12: out.append(h)
        elif vals.max()<=1e-12: out.append(-h)
    return out
def mu(i,j,o,t):
    z=(1-t)*E[i]+t*E[j]; oth=j if o==i else i
    for h in tangents(z):
        if h[o]>0>h[oth]:
            cc=c(h); return cc[i]/(cc[i]-cc[j])
    raise RuntimeError
def Zinv(i,j,o,s,it=60):
    a,b=0.0,1.0
    for _ in range(it):
        m=(a+b)/2
        if mu(i,j,o,m)<s: a=m
        else: b=m
    return (a+b)/2
EDG=[(0,1),(1,2),(2,0)]
# (E)
worst=0
for (i,j) in EDG:
    for s in np.linspace(0.02,0.98,25):
        q0=(1-s)*E[i]+s*E[j]; K=Kpts(q0); tv=K[:,j]
        Zj,Zi=Zinv(i,j,j,s),Zinv(i,j,i,s)
        worst=max(worst,abs(tv.min()-Zj),abs(tv.max()-Zi))
print(f"(E) Prop E on box system: max |edge limit - [Z_j,Z_i]| over 75 edge priors = {worst:.2e}")
# (R)
worst=0;worstS=-1;n=0
for _ in range(3000):
    g=rng.normal(size=3)
    if g.min()>0 or g.max()<0: continue
    for (i,j) in EDG:
        if g[i]*g[j]>=0: continue
        t=g[i]/(g[i]-g[j])           # (1-t)g_i + t g_j = 0
        o=i if g[i]>0 else j
        s=mu(i,j,o,t); y=(1-s)*E[i]+s*E[j]
        Zj,Zi=Zinv(i,j,j,s,45),Zinv(i,j,i,s,45)
        if not Zj<Zi: continue
        n+=1; worst=max(worst,abs(c(g)@y)/np.linalg.norm(c(g))); worstS=max(worstS,c(-g)@y)
print(f"(R) Thm R on box system: {n} (gamble,edge) cases; max |c(g).mu_o(t)|/|c| = {worst:.2e}; max c'(g).y = {worstS:.3e} (must be <=0)")
# (S)
worst=0;cnt=0
for _ in range(400):
    q=rng.dirichlet([2,2,2]); th=rng.uniform(0,np.pi)
    B1=np.array([1,-1,0])/np.sqrt(2); B2=np.array([1,1,-2])/np.sqrt(6)
    d=np.cos(th)*B1+np.sin(th)*B2
    pts=[]
    for (i,j) in EDG:
        A=np.array([E[j]-E[i],-d]).T; s,l=np.linalg.lstsq(A,q-E[i],rcond=None)[0]
        if 1e-6<s<1-1e-6: pts.append((i,j,s))
    if len(pts)!=2: continue
    nrm=-np.sin(th)*B1+np.cos(th)*B2
    zs=[];ok=True
    for (i,j,s) in pts:
        if not Zinv(i,j,j,s,45)<Zinv(i,j,i,s,45): ok=False;break
        o=j if nrm@(E[j]-q)>0 else i
        z=Zinv(i,j,o,s); zs.append((1-z)*E[i]+z*E[j])
    if not ok: continue
    gL=np.cross(zs[0],zs[1])
    plus=[k for k in range(3) if nrm@(E[k]-q)>0][0]
    if gL@E[plus]<0: gL=-gL
    cnt+=1; worst=max(worst,abs(P(q,gL))/np.linalg.norm(gL))
print(f"(S) Lemma S on box system: {cnt} random (q, line) pairs; max |min_K_q g_L| = {worst:.2e}")
# (W) concurrency of forced lines in a 'middle window': lines through q crossing E1=[e1,e2] and E2=[e3,e1]
def forced(q,y):
    Y=(1-y)*E[0]+y*E[1]; d=Y-q; l=-q[1]/d[1]; Pp=q+l*d; y2=Pp[0]
    z1=Zinv(0,1,1,y); z2=Zinv(2,0,2,y2)
    g=np.cross((1-z1)*E[0]+z1*E[1],(1-z2)*E[2]+z2*E[0])
    return g if g@E[1]>0 else -g
for ys in ([0.52,0.55,0.58],[0.62,0.68,0.74],[0.9,0.93,0.96]):
    out=[]
    for dirn in [np.array([0,1,-1.0]),np.array([2,-1,-1.0]),np.array([1,0,-1.0])]:
        dirn=dirn/np.linalg.norm(dirn)
        for sg in [1,-1]:
            q=ps+sg*1e-3*dirn
            G=[forced(q,y) for y in ys]
            al,be,ga=np.linalg.solve(np.c_[G[0],G[2],np.ones(3)],G[1])
            out.append(f"{ga:+.1e}")
    print(f"(W) box system, window y={ys}: gamma at q=p*+-1e-3*dir (3 dirs): {out}")
