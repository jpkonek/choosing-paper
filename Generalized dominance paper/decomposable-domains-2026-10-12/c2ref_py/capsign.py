"""Referee check: do the cap maps W_I=(x,1,1/x) and W_II=(kappa,1,kappa) at b=2 satisfy, near e_2,
 (N) N21.1':  sigma.h(tau) > 0  =>  c_k(h(tau)).q > 0       (once refereed; consequence of quasiconcavity + pivot)
 (R) Lemma R1: c_k(h(tau)).q < 0 =>  sigma.h(tau) < 0       (one reader)
for all three facets and all tau in (0,1)?  Both sides affine in tau: test on a fine grid plus both roots +- 1e-9.
Prior directions: q = e2 + rho*((1-phi)*(e1-e2) + phi*(u-e2)/|..|)-type angular parameter phi in [0,1],
phi=0 failing edge [e2,e1], phi=1/2 chord lambda_2 (as in N28_referee), phi=1 edge [e2,e3]."""
import numpy as np
def setup(eps):
    k = (1+2*eps)/(1-eps); x = ((k+1)+np.sqrt((k+1)**2-4))/2
    C = [np.array([[0,-x,-1],[0,x,0],[0,0,1.]]), np.array([[1,0,0],[-1,0,-x],[0,0,x]]), np.array([[x,0,0],[0,1,0],[-x,-1,0.]])]
    r12=np.array([-1,-1,k+1.]); r23=np.array([k+1,-1,-1.]); r31=np.array([-1,k+1,-1.])
    F=[(r31,r12),(r12,r23),(r23,r31)]
    return k,x,C,F
def prior(rho,phi):
    e1,e2,e3=np.eye(3); u=np.ones(3)/3
    # piecewise-linear angle: phi in [0,1/2] between edge dir and chord dir, [1/2,1] between chord and other edge
    d1=(e1-e2)/np.linalg.norm(e1-e2); dm=(u-e2)/np.linalg.norm(u-e2); d3=(e3-e2)/np.linalg.norm(e3-e2)
    a=np.arccos(np.clip(d1@dm,-1,1))
    if phi<=.5: ang=2*phi*a; base,other=d1,dm
    else: ang=(2*phi-1)*a; base,other=dm,d3
    perp=other-(other@base)*base; perp/=np.linalg.norm(perp)
    d=np.cos(ang)*base+np.sin(ang)*perp
    return e2+rho*d
def test(eps,W,rho,phis):
    k,x,C,F=setup(eps); out=[]
    taus=np.linspace(1e-6,1-1e-6,4001)
    for phi in phis:
        q=prior(rho,phi); s=W*q; s=s/s.sum(); vN=vR=0
        for kk,(r0,r1) in enumerate(F):
            def P(t): return s@((1-t)*r0+t*r1)
            def X(t): return (C[kk]@((1-t)*r0+t*r1))@q
            ts=list(taus)
            for f in (P,X):
                a0,a1=f(0.),f(1.)
                if a1!=a0:
                    t0=a0/(a0-a1)
                    if 0<t0<1: ts+= [t0-1e-9,t0+1e-9]
            for t in ts:
                p,c=P(t),X(t)
                if p>1e-14 and c<=0: vN+=1
                if c< -1e-14 and p>=0: vR+=1
        out.append((phi,vN,vR))
    return out
for eps in (0.05,0.3,0.6):
    k,x,_,_=setup(eps)
    WI=np.array([x,1,1/x]); WII=np.array([k,1,k])
    phis=np.round(np.linspace(0.01,0.99,50),3)
    for name,W in (('W_I',WI),('W_II',WII)):
        for rho in (1e-2,1e-3):
            res=test(eps,W,rho,phis)
            okN=[p for p,vn,vr in res if vn==0]; okR=[p for p,vn,vr in res if vr==0]
            print(f"eps={eps} {name} rho={rho}: N21.1' holds at phi in {okN[:3]}..max {max(okN) if okN else None} ({len(okN)}/50); R1 holds at {len(okR)}/50, max phi {max(okR) if okR else None}")
    # predicted angular boundary for W_II: line slope d_c/d_a = 1/x
    q=np.array([1.,0,1/x]); e2=np.eye(3)[1]; d=q-(1+1/x)*e2  # direction (1,-(1+1/x),1/x)
    print("   W_II line direction (1,-(1+1/x),1/x):", d)
