"""I1: general version of the edge-map / envelope machinery, for any polygonal target V (vertices, at p*)
with a facet chart map cfun(k,h) -> c-vector of the facet gamble h through vertex k (chord {c.q=0}).
Used (1) on T1 with the (PC) data, (2) on the normalized-box system of 'Coverage after Neutral
Abstention' eq. (4), a genuine CF solution, as a sanity check of every step."""
import numpy as np
from scipy.optimize import linprog
E=np.eye(3)
B1=np.array([1,-1,0])/np.sqrt(2); B2=np.array([1,1,-2])/np.sqrt(6)

class System:
    def __init__(self,V,cfun):
        self.V=[np.asarray(v,float) for v in V]; self.cfun=cfun
        self.cache={}
    def tangents(self,z):
        out=[]
        for k,vk in enumerate(self.V):
            h=np.cross(z,vk)
            if np.linalg.norm(h)<1e-14: continue
            vals=np.array([h@w for w in self.V])
            if np.all(vals>-1e-12): out.append((k,h))
            elif np.all(vals<1e-12): out.append((k,-h))
        return out
    def mu(self,i,j,sz,orient):
        z=(1-sz)*E[i]+sz*E[j]
        best=None
        for k,h in self.tangents(z):
            if (orient=='j' and h[j]>0>h[i]) or (orient=='i' and h[i]>0>h[j]):
                c=self.cfun(k,h)
                best=c[i]/(c[i]-c[j])
        return best
    def inv(self,i,j,orient,s,it=60):
        a,b=1e-12,1-1e-12
        for _ in range(it):
            m=(a+b)/2
            if self.mu(i,j,m,orient)<s: a=m
            else: b=m
        return (a+b)/2
    def Z(self,i,j,s):
        return self.inv(i,j,'j',s), self.inv(i,j,'i',s)    # (Z_j, Z_i)
    def nonfail(self,i,j,s,margin=0.0):
        Zj,Zi=self.Z(i,j,s); return Zj+margin<Zi

def edge_of(i,j):
    return (i,j) if (i,j) in [(0,1),(1,2),(2,0)] else (j,i)

def crossings(q,theta):
    d=np.cos(theta)*B1+np.sin(theta)*B2
    n=-np.sin(theta)*B1+np.cos(theta)*B2
    out=[]
    for (i,j) in [(0,1),(1,2),(2,0)]:
        A=np.array([E[j]-E[i],-d]).T
        sol=np.linalg.lstsq(A,q-E[i],rcond=None)[0]; s,t=sol
        if 1e-9<s<1-1e-9: out.append(((i,j),s))
    return out,n

def Phi(S,q,theta,margin=0.0):
    cr,n=crossings(q,theta)
    if len(cr)!=2: return None
    pts=[]
    for (i,j),s in cr:
        if not S.nonfail(i,j,s,margin): return None
        o='j' if n@(E[j]-q)>0 else 'i'
        sz=S.inv(i,j,o,s)
        pts.append((1-sz)*E[i]+sz*E[j])
    g=np.cross(pts[0],pts[1])
    plus=[k for k in range(3) if n@(E[k]-q)>0]
    if g@E[plus[0]]<0: g=-g
    ok=np.all(np.sign(g)==np.sign([n@(E[k]-q) for k in range(3)]))
    return g/np.linalg.norm(g),ok

def gaps(G,extra=None):
    A=[[-(g[0]-g[2]),-(g[1]-g[2])] for g in G]; b=[g[2] for g in G]
    out=[]
    for g in G:
        r=linprog([g[0]-g[2],g[1]-g[2]],A_ub=A,b_ub=b,bounds=[(None,None)]*2,method='highs')
        out.append(r.fun+g[2] if r.status==0 else np.nan)
    return np.array(out)

def envelope(S,q,nth=240,margin=0.0):
    G=[];TH=[];bad=0
    for th in np.linspace(0,2*np.pi,nth,endpoint=False):
        r=Phi(S,q,th,margin)
        if r is None: continue
        g,ok=r
        if not ok: bad+=1
        G.append(g);TH.append(th)
    G=np.array(G)
    return np.array(TH),G,(gaps(G) if len(G) else np.array([])),bad

# ---------------- systems ----------------
def T1_system(eps,which='+'):
    kap=(1+2*eps)/(1-eps); c0=(1-eps)/3
    V=[c0*np.ones(3)+eps*E[k] for k in range(3)]
    s=kap+1; xp=(s+np.sqrt(s*s-4))/2; x=xp if which=='+' else 1/xp
    def cfun(k,h):
        h1,h2,h3=h
        if k==0: return np.array([-(x*h2+h3),x*h2,h3])
        if k==1: return np.array([h1,-(h1+x*h3),x*h3])
        return np.array([x*h1,h2,-(x*h1+h2)])
    return System(V,cfun),x,kap

def box_system(lam,eta,p):
    """K_p = nu(p (.) a), lam<=a<=eta.  c(g)_i = min(lam_i g_i, eta_i g_i)."""
    lam=np.asarray(lam,float); eta=np.asarray(eta,float); p=np.asarray(p,float)
    # vertices of K_p: nu(p*a) over the 8 corners a, then hull
    from itertools import product
    pts=[]
    for a in product(*zip(lam,eta)):
        m=p*np.array(a); pts.append(m/m.sum())
    pts=np.array(pts)
    # convex hull in 2D
    from scipy.spatial import ConvexHull
    P2=np.c_[pts@B1,pts@B2]; hull=ConvexHull(P2)
    V=[pts[i] for i in hull.vertices]
    def cfun(k,h):
        return np.minimum(lam*h,eta*h)
    return System(V,cfun),V

def box_K(lam,eta,q):
    from itertools import product
    pts=[]
    for a in product(*zip(lam,eta)):
        m=np.asarray(q)*np.array(a); pts.append(m/m.sum())
    return np.array(pts)
