"""P1 NUMERICS: the facet-data system of Thm main (corner equations + box) for T1 at p*=u,
and its relaxation when one corner equation is removed (an atom chord through p* at that corner).

Facet data (writeup Prop T1 normalisation): x1=lambda_21, x2=lambda_32, x3=lambda_13,
 c1(h)=(-(x1 h2+h3), x1 h2, h3), c2(h)=(h1, -(h1+x2 h3), x2 h3), c3(h)=(x3 h1, h2, -(x3 h1+h2)).
Box certificate (Prop boxbridge(c)): A in relint F_k, B in relint F_k', q0 in edge [e_a,e_b],
 A_a<0<A_b, B_b<0<B_a, A_b B_a<|A_a||B_b|, c_k(A).q0>0, c_k'(B).q0>0  ==> contradiction.
We search for certificates on grids; 'margin' = best min(c_k(A).q0, c_k'(B).q0, ratio slack) found.
"""
import numpy as np, itertools, sys

def setup(eps):
    c0=(1-eps)/3
    v=[c0*np.ones(3)+eps*np.eye(3)[k] for k in range(3)]
    kap=(1+2*eps)/(1-eps)
    r12=np.array([-1,-1,kap+1.]); r23=np.array([kap+1,-1,-1.]); r31=np.array([-1,kap+1,-1.])
    # facet k between its two corner rays
    F={0:(r31,r12),1:(r12,r23),2:(r23,r31)}
    return v,kap,F

def cvec(k,h,x):
    x1,x2,x3=x
    h1,h2,h3=h[...,0],h[...,1],h[...,2]
    if k==0: return np.stack([-(x1*h2+h3),x1*h2,h3],-1)
    if k==1: return np.stack([h1,-(h1+x2*h3),x2*h3],-1)
    return np.stack([x3*h1,h2,-(x3*h1+h2)],-1)

def best_cert(x,eps,nt=401,ns=200,skip=None):
    """skip: dict k->(tau_lo,tau_hi) intervals of facet k excluded (atom arcs)."""
    v,kap,F=setup(eps)
    taus=np.linspace(0.0025,0.9975,nt)
    H={}
    for k in range(3):
        r,rp=F[k]
        h=(1-taus)[:,None]*r+taus[:,None]*rp
        h=h/np.linalg.norm(h,axis=1,keepdims=True)
        keep=np.ones(nt,bool)
        if skip and k in skip:
            lo,hi=skip[k]; keep&=~((taus>=lo)&(taus<=hi))
        H[k]=(h[keep],cvec(k,h[keep],x))
    ss=np.linspace(0.0005,0.9995,ns)
    best=-np.inf; arg=None
    for a,b in itertools.permutations(range(3),2):
        q0=np.zeros((ns,3)); q0[:,a]=1-ss; q0[:,b]=ss
        for k in range(3):
            hA,cA=H[k]; mA=(hA[:,a]<0)&(hA[:,b]>0)
            if not mA.any(): continue
            for kk in range(3):
                hB,cB=H[kk]; mB=(hB[:,b]<0)&(hB[:,a]>0)
                if not mB.any(): continue
                A=hA[mA]; B=hB[mB]; CA=cA[mA]@q0.T; CB=cB[mB]@q0.T   # (nA,ns),(nB,ns)
                ratio=np.abs(A[:,a])[:,None]*np.abs(B[:,b])[None,:]-A[:,b][:,None]*B[:,a][None,:]  # >0 needed
                # margin over (A,B,s): min(CA[A,s],CB[B,s],ratio[A,B])
                for j in range(ns):
                    m=np.minimum(np.minimum(CA[:,j][:,None],CB[:,j][None,:]),ratio)
                    mm=m.max()
                    if mm>best: best=mm; i0=np.unravel_index(m.argmax(),m.shape); arg=(a,b,k,kk,ss[j])
    return best,arg

if __name__=="__main__":
    for eps in [0.1,0.3,0.6]:
        v,kap,F=setup(eps)
        xp=((kap+1)+np.sqrt((kap+1)**2-4))/2
        print("eps",eps,"kappa",kap,"x+",xp)
        print("  all corners (x+,x+,x+): best cert margin",best_cert((xp,xp,xp),eps)[0])
        print("  all corners (x-,x-,x-):",best_cert((1/xp,1/xp,1/xp),eps)[0])
        print("  control x=(1,1,1) (no corner eqs):",best_cert((1,1,1),eps)[0])
