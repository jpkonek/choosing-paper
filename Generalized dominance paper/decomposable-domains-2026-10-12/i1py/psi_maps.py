"""For each facet F_k of T1 and each sub-range of its pencil (edge pair crossed), the Moebius maps
mu^k_E (prob edge -> prior edge via facet k's chord map) on the two crossed edges extend to a unique
projective map psi^k_{E1E2} of the plane fixing E1 cap E2.  psi(p*) = v_k.  We compute
    w_A(delta) = (psi_A(p*+r delta) - v_k)/r   (r small)
and test whether it is the same for the different sub-ranges A (I1 Lemma FO), and which sub-ranges are
admissible near p* (chord crossings in the non-failing parts)."""
import numpy as np, sys
from general import *
EDGES=[(0,1),(1,2),(2,0)]
def mob_k(S,k,i,j,sz,orient):
    """chord crossing (prior s) of facet-k gamble through z=P(sz) on edge (i,j), Moebius-extended"""
    z=(1-sz)*E[i]+sz*E[j]
    h=np.cross(z,S.V[k])
    # orientation: + toward e_j if orient=='j'
    if (orient=='j' and h[j]<0) or (orient=='i' and h[i]<0): h=-h
    c=S.cfun(k,h); return c[i]/(c[i]-c[j])
def mob_k_inv(S,k,i,j,s,orient):
    # Moebius: find sz with mob_k(sz)=s ; mob is projective in sz -> solve via 3-point fit
    xs=np.array([0.2,0.5,0.8]); ys=np.array([mob_k(S,k,i,j,t,orient) for t in xs])
    # fit y=(a x+b)/(c x+1)
    A=np.array([[x_,1,-x_*y_] for x_,y_ in zip(xs,ys)]); a,b,c=np.linalg.solve(A,ys)
    # invert: x=(y - b)/(a - c y)
    return (s-b)/(a-c*s)
def phi_k(S,k,q,theta):
    cr,n=crossings(q,theta)
    if len(cr)!=2: return None
    pts=[];pair=[]
    for (i,j),s in cr:
        o='j' if n@(E[j]-q)>0 else 'i'
        sz=mob_k_inv(S,k,i,j,s,o); pts.append((1-sz)*E[i]+sz*E[j]); pair.append((i,j))
    g=np.cross(pts[0],pts[1]); return g,tuple(sorted(pair))
def psi_point(S,k,q,th1,th2):
    g1,p1=phi_k(S,k,q,th1); g2,p2=phi_k(S,k,q,th2)
    assert p1==p2
    m=np.cross(g1,g2); return m/m.sum(),p1
def chord_dir(S,k,h,q0):
    c=S.cfun(k,h); n=c-c.mean()
    nb=np.array([n@B1,n@B2]); d=np.array([-nb[1],nb[0]])
    return np.arctan2(d[1],d[0])%np.pi
if __name__=="__main__":
    eps=float(sys.argv[1]); w=sys.argv[2]
    S,x,kap=T1_system(eps,w); u=np.ones(3)/3
    for k in range(3):
        i,j=[l for l in range(3) if l!=k]
        r0=np.cross(S.V[k],S.V[i]); r0=r0 if r0@S.V[j]>0 else -r0
        r1=np.cross(S.V[k],S.V[j]); r1=r1 if r1@S.V[i]>0 else -r1
        sub={}
        for t in np.linspace(0.002,0.998,499):
            h=(1-t)*r0+t*r1
            th=chord_dir(S,k,h,u)
            cr,n=crossings(u,th)
            pair=tuple(sorted([e for e,s in cr]))
            adm=all(S.nonfail(a,b,s) for (a,b),s in cr)
            sub.setdefault(pair,[]).append((t,th,adm))
        print(f"eps={eps} x{w} facet {k+1}:")
        for pair,L in sub.items():
            ts=[l[0] for l in L]; ad=[l[0] for l in L if l[2]]
            th_ad=[l[1] for l in L if l[2]]
            msg=f"   pair {pair}: tau in [{min(ts):.3f},{max(ts):.3f}], admissible tau: "+(f"[{min(ad):.3f},{max(ad):.3f}] ({len(ad)}/{len(L)})" if ad else "none")
            if len(th_ad)>=2:
                tha,thb=th_ad[len(th_ad)//3],th_ad[2*len(th_ad)//3]
                ws=[]
                for dlt in [np.array([1,-1,0.])/np.sqrt(2),np.array([1,1,-2.])/np.sqrt(6)]:
                    r=1e-5; q=u+r*dlt
                    P,_=psi_point(S,k,q,tha,thb)
                    ws.append((P-S.V[k])/r)
                W=np.array([[w_@B1 for w_ in ws],[w_@B2 for w_ in ws]])
                # ratio to the facet chord map: compare W with W of other pairs
                msg+=f"\n      Dpsi(p*) in basis (B1,B2): {np.round(W,5).tolist()}"
                sub[pair]=W
            print(msg)
