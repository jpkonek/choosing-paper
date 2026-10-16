"""Gap test restricted to ONE sub-range of ONE facet: lines Phi(Lam) for Lam through q whose two
crossings are admissible (non-failing) and both supplied by facet k with the given edge pair."""
import numpy as np, sys
from general import *
def family(S,q,k,pair,nth=1440):
    G=[];TH=[]
    for th in np.linspace(0,2*np.pi,nth,endpoint=False):
        cr,n=crossings(q,th)
        if len(cr)!=2 or tuple(sorted(e for e,s in cr))!=pair: continue
        okk=True; pts=[]
        for (i,j),s in cr:
            if not S.nonfail(i,j,s): okk=False;break
            o='j' if n@(E[j]-q)>0 else 'i'
            sz=S.inv(i,j,o,s); z=(1-sz)*E[i]+sz*E[j]
            ks=[kk for kk,h in S.tangents(z) if ((o=='j' and h[j]>0>h[i]) or (o=='i' and h[i]>0>h[j]))]
            if ks[0]!=k: okk=False;break
            pts.append(z)
        if not okk: continue
        g=np.cross(pts[0],pts[1]); plus=[kk for kk in range(3) if n@(E[kk]-q)>0]
        if g@E[plus[0]]<0: g=-g
        G.append(g/np.linalg.norm(g)); TH.append(th)
    return np.array(TH),np.array(G)
if __name__=="__main__":
    eps=float(sys.argv[1]); w=sys.argv[2]
    S,x,kap=T1_system(eps,w); u=np.ones(3)/3
    k=0
    for pair,name in [(((1,2),(2,0)),'outer (V0=e3)'),(((0,1),(2,0)),'middle (V0=e1=e_k)')]:
        for dname,d in [('+d1',np.array([0,1,-1.])),('-d1',np.array([0,-1,1.])),('+d2',np.array([2,-1,-1.])),('-d2',np.array([-2,1,1.]))]:
            d=d/np.linalg.norm(d); r=1e-3; q=u+r*d
            TH,G=family(S,q,k,pair)
            gp=gaps(G) if len(G) else np.array([np.nan])
            print(f"eps={eps} x{w} facet1 {name} delta {dname}: n={len(G)} max gap/r = {np.nanmax(gp)/r:.4f}",flush=True)
