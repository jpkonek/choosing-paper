"""Exact version of sector_caps.py: for precise K_q={s}, facet k, tau in (0,1), both a(tau)=s.h(tau) and
c(tau)=c_k(h(tau)).q are affine in tau.  Constraint (i) a>0 => c>0 ; (ii) c<0 => a<0.
Violation iff some tau in (0,1) has a>=0>=c with (a,c) != (0,0) in the wrong pattern; test at the
endpoints and on both sides of the two roots."""
import numpy as np
E=np.eye(3)
def setup(eps):
    kap=(1+2*eps)/(1-eps); c0=(1-eps)/3
    v=[c0*np.ones(3)+eps*E[k] for k in range(3)]
    s=kap+1; xp=(s+np.sqrt(s*s-4))/2
    return kap,v,xp
def corner(k,j,v):
    r=np.cross(v[k],v[j]); t=3-k-j
    return r if r@v[t]>0 else -r
def cvec(k,h,x):
    h1,h2,h3=h
    if k==0: return np.array([-(x*h2+h3),x*h2,h3])
    if k==1: return np.array([h1,-(h1+x*h3),x*h3])
    return np.array([x*h1,h2,-(x*h1+h2)])
def viol(sq,q,v,x):
    worst=0
    for k in range(3):
        i,j=[l for l in range(3) if l!=k]
        r0,r1=corner(k,i,v),corner(k,j,v)
        a0,a1=sq@r0, sq@(r1-r0)
        C0,C1=cvec(k,r0,x)@q, cvec(k,r1-r0,x)@q
        cand=[1e-9,1-1e-9]
        for (p0,p1) in [(a0,a1),(C0,C1)]:
            if abs(p1)>1e-15:
                t=-p0/p1
                for d in [-1e-9,0,1e-9]:
                    if 0<t+d<1: cand.append(t+d)
        for t in cand:
            a=a0+a1*t; c=C0+C1*t
            if (a>0 and c<=0) or (c<0 and a>=0): return True
    return False
if __name__=="__main__":
 for eps in [0.2,0.3]:
     kap,v,xp=setup(eps)
     for x,name in [(xp,'x+'),(1/xp,'x-')]:
         out=[]
         for b in range(3):
             a,c=[l for l in range(3) if l!=b]
             row=[]
             for rho in [0.05,0.01,0.001,0.0001]:
                 phis=np.linspace(0.0005,0.9995,1999)
                 good=np.array([not viol(q,q,v,x) for q in [E[b]+rho*((1-p)*(E[a]-E[b])+p*(E[c]-E[b])) for p in phis]])
                 row.append((rho,(round(phis[good].min(),3),round(phis[good].max(),3)) if good.any() else None, bool(good[999])))
             out.append((b+1,row))
         for b,row in out: print(f"eps={eps} {name} b={b} (phi=0: edge to e_a={['e2','e1','e1'][b-1] if False else ''} ; phi=.5 chord):",row)
