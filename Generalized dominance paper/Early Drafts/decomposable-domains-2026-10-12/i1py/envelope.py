"""I1 envelope test.  For an interior prior q and an oriented prior line Lam through q that crosses two
edges E1,E2 at priors y1,y2 lying in the NON-FAILING parts N_E, the map
   Phi(Lam) = line(z1,z2),   z_k = mu^{E_k}_{o_k}^{-1}(y_k),
(o_k = the endpoint of E_k on the + side of Lam) is a supporting line of K_q with K_q on its + side
(I1 Thm R).  Test: are the lines {Phi(Lam)} the supporting lines of ONE convex set?
For each sampled direction, compute the support value of the candidate set
   C = intersection of closed + sides of all Phi(Lam)
in the normal direction of each line and compare with the line's own offset ("gap" > 0 means the line
does not touch C: contradiction)."""
import numpy as np, sys
from edgemaps import setup, mu, inv, E
from scipy.optimize import linprog

def edge_data(v,x):
    D={}
    for (i,j) in [(0,1),(1,2),(2,0)]:
        D[(i,j)]=dict(fj=lambda s,i=i,j=j: mu(i,j,s,v,x,'j')[0], fi=lambda s,i=i,j=j: mu(i,j,s,v,x,'i')[0])
    return D
def nonfail(D,i,j,s):
    d=D[(i,j)]
    return inv(d['fj'],s) < inv(d['fi'],s)

def line_edges(q,theta):
    """prior line through q with direction theta (in aff Delta, coords via basis); return crossings
       as list of (edge(i,j), s) and the oriented normal (3-vector n with n.1=0)"""
    b1=np.array([1,-1,0])/np.sqrt(2); b2=np.array([1,1,-2])/np.sqrt(6)
    d=np.cos(theta)*b1+np.sin(theta)*b2
    n=-np.sin(theta)*b1+np.cos(theta)*b2      # normal; + side = {n.(p-q)>0}
    out=[]
    for (i,j) in [(0,1),(1,2),(2,0)]:
        # point (1-s)e_i+s e_j = q + t d  -> solve
        A=np.array([E[j]-E[i], -d]).T
        sol,res,rk,sv=np.linalg.lstsq(A,q-E[i],rcond=None)
        s,t=sol
        if 1e-9<s<1-1e-9 and np.allclose(E[i]+s*(E[j]-E[i]),q+t*d,atol=1e-9):
            out.append(((i,j),s))
    return out,n

def Phi(D,q,theta):
    cr,n=line_edges(q,theta)
    if len(cr)!=2: return None
    pts=[]
    for (i,j),s in cr:
        if not nonfail(D,i,j,s): return None
        # which endpoint is on + side
        o='j' if n@(E[j]-q)>0 else 'i'
        f=D[(i,j)]['f'+o]
        sz=inv(f,s)
        pts.append(((1-sz)*E[i]+sz*E[j], o, (i,j)))
    z1,z2=pts[0][0],pts[1][0]
    g=np.cross(z1,z2)       # gamble vanishing on line(z1,z2)
    # orient: + side must contain the vertices on the + side of Lam
    plus=[k for k in range(3) if n@(E[k]-q)>0]
    k=plus[0]
    if g@E[k]<0: g=-g
    # sanity: same sign pattern
    sg=np.sign(g); sn=np.sign([n@(E[k]-q) for k in range(3)])
    ok=np.all(sg==sn)
    return g/np.linalg.norm(g), ok

def test(eps,x,q,nth=720,verbose=False):
    kap,v,xp=setup(eps)
    D=edge_data(v,x)
    G=[];TH=[]
    for th in np.linspace(0,2*np.pi,nth,endpoint=False):
        r=Phi(D,q,th)
        if r is None: continue
        g,ok=r
        if not ok: print("sign mismatch",th)
        G.append(g);TH.append(th)
    G=np.array(G)
    # C = {m in aff: g.m >= 0 for all g}, m in simplex plane: m = (m1,m2,1-m1-m2)
    # support value in direction of each g: min_{m in C} g.m  should be 0
    A_ub=[];b_ub=[]
    for g in G:
        # g.m>=0 -> -(g1-g3)m1-(g2-g3)m2 <= g3
        A_ub.append([-(g[0]-g[2]),-(g[1]-g[2])]); b_ub.append(g[2])
    gaps=[]
    for g in G:
        cobj=[g[0]-g[2],g[1]-g[2]]
        res=linprog(cobj,A_ub=A_ub,b_ub=b_ub,bounds=[(None,None)]*2,method='highs')
        if res.status!=0: gaps.append(np.nan); continue
        val=res.fun+g[2]
        gaps.append(val)
    gaps=np.array(gaps)
    return np.array(TH),G,gaps

if __name__=="__main__":
    for eps in [0.3,0.05,0.6]:
        kap,v,xp=setup(eps)
        for x,name in [(xp,'x+'),(1/xp,'x-')]:
            for q in [np.ones(3)/3, np.array([.36,.33,.31]), np.array([.30,.40,.30]), np.array([.5,.3,.2]),np.array([.2,.2,.6])]:
                TH,G,gaps=test(eps,x,q)
                if len(gaps)==0:
                    print(eps,name,q,'no admissible lines'); continue
                print(f"eps={eps} {name} q={np.round(q,3)} lines={len(G)} max gap={np.nanmax(gaps):.3e} (#gap>1e-6: {np.sum(gaps>1e-6)}) min={np.nanmin(gaps):.2e}")
