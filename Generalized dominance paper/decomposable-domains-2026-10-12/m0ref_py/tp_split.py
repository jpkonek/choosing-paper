"""M0 referee, independent check 2 (NUMERICS; (HC)-model only).
Configuration (TP)+(mid-facet arcs): each facet F_k carries
   [corner arc at its first corner] [piece, ratio a_k] [mid arc] [piece, ratio b_k] [corner arc at its second corner].
Arcs have constant (chord) normal; normal direction continuous along the boundary of D_T1 (hypothesis (HC)).
Corner arcs exist iff the 'overlap' inequality b_k + 1/a_{k+1} > kappa+1 holds (Lemma P1.3); the corner-arc normal is
chosen at fraction f of the overlap.  Mid arcs need b_k > a_k.  Box certificates searched over ALL facet gambles,
arc gambles carrying their chord normal (no exclusion).  Also variant (TP) without mid arcs (a_k=b_k=x_k): must be
infeasible by Lemma P1.1.  Own code, independent of p1py."""
import numpy as np, itertools
def setup(eps):
    kap=(1+2*eps)/(1-eps)
    r12=np.array([-1,-1,kap+1.]); r23=np.array([kap+1,-1,-1.]); r31=np.array([-1,kap+1,-1.])
    return kap,[(r31,r12),(r12,r23),(r23,r31)]
def cmap(k,H,x):
    a,b,c=H[...,0],H[...,1],H[...,2]
    if k==0: return np.stack([-(x*b+c),x*b,c],-1)
    if k==1: return np.stack([a,-(a+x*c),x*c],-1)
    return np.stack([x*a,b,-(x*a+b)],-1)
# orthonormal basis of 1-perp for angles
e1=np.array([1,-1,0])/np.sqrt(2); e2=np.array([1,1,-2])/np.sqrt(6)
def ang(C): return np.unwrap(np.arctan2(C@e2,C@e1))
def build(eps,a,b,fc=0.5,fm=0.5,nt=3001):
    kap,F=setup(eps); t=np.linspace(0,1,nt)
    H=[(1-t)[:,None]*F[k][0]+t[:,None]*F[k][1] for k in range(3)]
    Ca=[cmap(k,H[k],a[k]) for k in range(3)]; Cb=[cmap(k,H[k],b[k]) for k in range(3)]
    th_a=[np.arctan2(Ca[k]@e2,Ca[k]@e1) for k in range(3)]; th_b=[np.arctan2(Cb[k]@e2,Cb[k]@e1) for k in range(3)]
    # global unwrap reference: follow boundary order F1,F2,F3
    def wrap(x,ref): return ref+((x-ref+np.pi)%(2*np.pi)-np.pi)
    data=[]
    # crossings: indices where a coordinate other than k changes sign
    cross=[]
    for k in range(3):
        idx=[i for i in range(3) if i!=k]
        cs=sorted(np.argmin(np.abs(H[k][:,i])) for i in idx); cross.append(cs)
    ok=True; arcs=[]
    for k in range(3):
        # mid arc: angle of a-piece at tau_a equals angle of b-piece at tau_b, both in middle (between crossings)
        lo,hi=cross[k]
        A=np.unwrap(th_a[k][lo:hi+1]); B=wrap(np.unwrap(th_b[k][lo:hi+1]),A[0])
        # monotone increasing? normalise direction
        sgn=np.sign(A[-1]-A[0])
        rng_lo=max(min(A),min(B)); rng_hi=min(max(A),max(B))
        if not rng_lo<rng_hi: ok=False; arcs.append(None); continue
        th=rng_lo+fm*(rng_hi-rng_lo)
        ia=lo+np.argmin(np.abs(A-th)); ib=lo+np.argmin(np.abs(B-th))
        if not ia<ib: ok=False
        arcs.append((ia,ib))
    # corner arcs: at end of F_k (b_k piece) and start of F_{k+1} (a_{k+1} piece)
    carcs=[]
    for k in range(3):
        kn=(k+1)%3
        thb_end=th_b[k][-1]; tha_start=wrap(th_a[kn][0],thb_end)
        # direction of travel (increasing angle along boundary) from F_k's b piece near its end
        d=np.sign(np.unwrap(th_b[k][-200:])[-1]-np.unwrap(th_b[k][-200:])[0])
        overlap=d*(thb_end-tha_start)   # >0 : the two pieces' normal ranges overlap at the corner
        if overlap<=0: ok=False; carcs.append(None); continue
        th=tha_start+fc*(thb_end-tha_start)
        Bk=wrap(np.unwrap(th_b[k][cross[k][1]:]),thb_end); iR=cross[k][1]+np.argmin(np.abs(Bk-th))
        An=wrap(np.unwrap(th_a[kn][:cross[kn][0]+1]),tha_start); iL=np.argmin(np.abs(An-th))
        carcs.append((iR,iL,th))
        if not (iR>cross[k][1] and iL<cross[kn][0]): ok=False
    return dict(kap=kap,H=H,Ca=Ca,Cb=Cb,arcs=arcs,carcs=carcs,ok=ok,t=t)
def normals(D):
    H,Ca,Cb=D['H'],D['Ca'],D['Cb']; N=[]
    for k in range(3):
        kp=(k-1)%3
        ia,ib=D['arcs'][k]; iL=D['carcs'][kp][1]; iR=D['carcs'][k][0]
        C=np.where((np.arange(len(D['t']))<=ia)[:,None],Ca[k],Cb[k]).copy()
        # mid arc chord normal = a-piece normal at ia (direction), scaled; sign kept
        C[ia:ib+1]=Ca[k][ia]
        C[:iL+1]=Ca[k][iL]          # corner arc at first corner
        C[iR:]=Cb[k][iR]            # corner arc at second corner
        N.append(C)
    return N
def box(H,N,ns=500):
    s=np.concatenate([np.geomspace(1e-7,1e-2,120),np.linspace(1e-2,1-1e-2,ns),1-np.geomspace(1e-7,1e-2,120)])
    best=-np.inf; arg=None
    for a,b in itertools.permutations(range(3),2):
        q=np.zeros((len(s),3)); q[:,a]=1-s; q[:,b]=s
        SA=[];SB=[]
        for k in range(3):
            h=H[k]; pos=(N[k]@q.T)>0
            mA=(h[:,a]<0)&(h[:,b]>0); RA=np.where(mA,-h[:,a]/np.where(mA,h[:,b],1),0)
            mB=(h[:,b]<0)&(h[:,a]>0); RB=np.where(mB,-h[:,b]/np.where(mB,h[:,a],1),0)
            SA.append(np.where(pos,RA[:,None],0).max(0)); SB.append(np.where(pos,RB[:,None],0).max(0))
        for k in range(3):
            for kk in range(3):
                pr=SA[k]*SB[kk]; j=pr.argmax()
                if pr[j]>0 and np.log(pr[j])>best: best=np.log(pr[j]); arg=(a+1,b+1,k+1,kk+1,float(s[j]))
    return best,arg
if __name__=="__main__":
    print("== (TP)+mid arcs, corners STRICT (overlap), all arcs with chord normals ==")
    for eps in [0.1,0.3,0.6,0.9]:
        kap=(1+2*eps)/(1-eps)
        for fa in [0.25,0.5,0.75]:
            aa=1/kap+fa*(1-1/kap)
            for eta in [0.02,0.2]:
                bb=kap+1-1/aa+eta*(kap+1)
                for fc in [0.1,0.5,0.9]:
                    D=build(eps,(aa,)*3,(bb,)*3,fc=fc)
                    if not D['ok']: print(f"eps={eps} a={aa:.3f} b={bb:.3f} fc={fc}: geometry infeasible"); continue
                    m,arg=box(D['H'],normals(D))
                    print(f"eps={eps} a={aa:.4f} b={bb:.4f} (b+1/a-k-1={bb+1/aa-kap-1:+.3f}) fc={fc}: box log-margin {m:+.3f} {arg}")
    print("== control: (TP) without mid arcs, x_k=a=b (Lemma P1.1 says certificate must exist) ==")
    for eps in [0.1,0.3,0.6,0.9]:
        kap=(1+2*eps)/(1-eps); xp=((kap+1)+np.sqrt((kap+1)**2-4))/2
        for x in [xp*1.05,(1/xp)*0.95,kap+0.9]:
            # unsplit: mid arc degenerate; emulate with build using a=b would fail mid-arc, so do direct
            kap_,F=setup(eps); t=np.linspace(0,1,3001)
            H=[(1-t)[:,None]*F[k][0]+t[:,None]*F[k][1] for k in range(3)]
            N=[cmap(k,H[k],x) for k in range(3)]
            m,arg=box(H,N)
            print(f"eps={eps} x={x:.4f} overlap x+1/x-k-1={x+1/x-kap-1:+.3f}: box log-margin {m:+.3f} {arg}")
