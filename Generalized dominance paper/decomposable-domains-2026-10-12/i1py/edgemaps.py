"""I1: edge maps forced by the (PC) facet data of T1 (p* = u).

For an edge E=[e_i,e_j] parametrised by s (point (1-s)e_i + s e_j, s=0 at e_i), and a probability point
z=P(s_z) on E, the two tangent lines from z to T1 are facet gambles h (T on the + side).  Their chords
{c_k(h).q=0} (Contamination Triangle, Prop T1 normalisation) cross the prior edge E at mu(s_z).
  orientation 'j' : h_j>0>h_i   -> mu_j
  orientation 'i' : h_i>0>h_j   -> mu_i
Edge limit sets (I1 Prop E):  Z_j(q0)=mu_j^{-1}(s(q0)), Z_i(q0)=mu_i^{-1}(s(q0));
  Z_j<Z_i : every limit set at q0 is exactly [Z_j,Z_i]   (non-failing)
  Z_j>Z_i : every limit set is a point in [Z_i,Z_j]      (failing)
"""
import numpy as np
E=np.eye(3)
def setup(eps):
    kap=(1+2*eps)/(1-eps); c0=(1-eps)/3
    v=[c0*np.ones(3)+eps*E[k] for k in range(3)]
    s=kap+1; xp=(s+np.sqrt(s*s-4))/2
    return kap,v,xp
def cvec(k,h,x):
    h1,h2,h3=h
    if k==0: return np.array([-(x*h2+h3),x*h2,h3])
    if k==1: return np.array([h1,-(h1+x*h3),x*h3])
    return np.array([x*h1,h2,-(x*h1+h2)])
def tangents(z,v):
    """facet gambles through z tangent to T (T on + side), with their facet index"""
    out=[]
    for k in range(3):
        h=np.cross(z,v[k])            # h.z=0, h.v_k=0
        if np.linalg.norm(h)<1e-14: continue
        o=[l for l in range(3) if l!=k]
        a,b=h@v[o[0]],h@v[o[1]]
        if a>-1e-12 and b>-1e-12: out.append((k,h))
        elif a<1e-12 and b<1e-12: out.append((k,-h))
    return out
def mu(i,j,sz,v,x,orient):
    z=(1-sz)*E[i]+sz*E[j]
    for k,h in tangents(z,v):
        if orient=='j' and h[j]>0>h[i] or orient=='i' and h[i]>0>h[j]:
            c=cvec(k,h,x)
            # c.((1-s)e_i+s e_j)=0
            ci,cj=c[i],c[j]
            return ci/(ci-cj), k
    return None,None
def inv(f,s,lo=1e-9,hi=1-1e-9,it=80):
    # f increasing on [0,1]
    a,b=lo,hi
    for _ in range(it):
        m=(a+b)/2
        if f(m)<s: a=m
        else: b=m
    return (a+b)/2
if __name__=="__main__":
    for eps in [0.05,0.3,0.6]:
        kap,v,xp=setup(eps)
        for x,name in [(xp,'x+'),(1/xp,'x-')]:
            print(f"eps={eps} {name} x={x:.4f} kappa={kap:.4f}")
            for (i,j) in [(0,1),(1,2),(2,0)]:
                fj=lambda s: mu(i,j,s,v,x,'j')[0]
                fi=lambda s: mu(i,j,s,v,x,'i')[0]
                # monotonicity check
                ss=np.linspace(0.001,0.999,999)
                mj=np.array([fj(s) for s in ss]); mi=np.array([fi(s) for s in ss])
                mono=(np.all(np.diff(mj)>0),np.all(np.diff(mi)>0))
                rows=[]
                for s0 in [0.001,0.01,0.1,0.3,0.5,0.7,0.9,0.99,0.999]:
                    Zj=inv(fj,s0); Zi=inv(fi,s0)
                    rows.append(f"s={s0}: Zj={Zj:.5f} Zi={Zi:.5f} {'NONFAIL' if Zj<Zi else 'FAIL'}")
                # crossover
                g=lambda s0: inv(fj,s0)-inv(fi,s0)
                xs=np.linspace(0.0005,0.9995,400); gv=np.array([g(t) for t in xs])
                cross=xs[np.where(np.diff(np.sign(gv))!=0)[0]]
                print(f"  edge [e{i+1},e{j+1}] (s=0 at e{i+1}) mu monotone {mono}; sign changes of Zj-Zi at s ~ {np.round(cross,4)}")
                for r in rows: print("    ",r)
