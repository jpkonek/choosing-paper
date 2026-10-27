"""P1 (semi-exact) box test.  For ordered pair (a,b), facets k,k', edge prior q0=(1-s)e_a+s e_b:
a certificate exists iff  sup|A_a| * sup|B_b| > 1, where A ranges over h in relint F_k normalised by A_b=1 with
A_a<0, c_k(A).q0>0, and B over relint F_k' normalised by B_a=1 with B_b<0, c_k'(B).q0>0
(ratio condition A_b B_a < |A_a||B_b|).  On each facet the admissible tau-set is an interval (affine sign conditions)
and |A_a| is linear-fractional in tau, so the sup is attained at an end of that interval: computed exactly per s.
Only s is gridded.  'excl' removes atom arcs (tau-intervals) from facets."""
import numpy as np, itertools
from box_relax import setup, cvec

def interval(k,r,rp,conds,excl):
    # conds: list of affine functions of tau given as (f(0),f(1)) required >0 ; returns list of open intervals
    lo,hi=0.0,1.0
    for f0,f1 in conds:
        # f(t)=f0+(f1-f0)t >0
        if f1==f0:
            if f0<=0: return []
            continue
        t0=-f0/(f1-f0)
        if f1>f0: lo=max(lo,t0)
        else: hi=min(hi,t0)
    if lo>=hi: return []
    ivs=[(lo,hi)]
    if excl and k in excl:
        e0,e1=excl[k]; new=[]
        for (u,w) in ivs:
            if w<=e0 or u>=e1: new.append((u,w)); continue
            if u<e0: new.append((u,e0))
            if w>e1: new.append((e1,w))
        ivs=new
    return ivs

def sup_ratio(k,F,x,q0,num,den,excl):
    """sup of -h_num/h_den over admissible tau, with h_den>0, h_num<0, c_k(h).q0>0."""
    r,rp=F[k]
    cr=cvec(k,r,x)@q0; crp=cvec(k,rp,x)@q0
    ivs=interval(k,r,rp,[(r[den],rp[den]),(-r[num],-rp[num]),(cr,crp)],excl)
    best=0.0
    for (u,w) in ivs:
        for t in (u,w):
            t=min(max(t,1e-12),1-1e-12)
            h=(1-t)*r+t*rp
            if h[den]>1e-14: best=max(best,-h[num]/h[den])
            else: best=np.inf
    return best

def box_margin(x,eps,ns=4000,excl=None):
    v,kap,F=setup(eps)
    best=-np.inf; arg=None
    ss=np.linspace(1e-4,1-1e-4,ns)
    for a,b in itertools.permutations(range(3),2):
        for k in range(3):
            for kk in range(3):
                for s in ss:
                    q0=np.zeros(3); q0[a]=1-s; q0[b]=s
                    SA=sup_ratio(k,F,x,q0,a,b,excl)
                    if SA==0: continue
                    SB=sup_ratio(kk,F,x,q0,b,a,excl)
                    val=np.log(SA*SB) if SA*SB>0 else -np.inf
                    if val>best: best=val; arg=(a+1,b+1,k+1,kk+1,round(s,4))
    return best,arg   # certificate iff best>0

if __name__=="__main__":
    for eps in [0.1,0.3,0.6]:
        v,kap,F=setup(eps)
        xp=((kap+1)+np.sqrt((kap+1)**2-4))/2
        print(eps,"x+:",box_margin((xp,xp,xp),eps,ns=1500),"x-:",box_margin((1/xp,)*3,eps,ns=1500),
              "ones:",box_margin((1,1,1),eps,ns=1500),"(k,1,1/k):",box_margin((kap,1,1/kap),eps,ns=1500))
