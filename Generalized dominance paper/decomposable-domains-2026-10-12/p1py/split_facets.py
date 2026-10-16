"""P1 NUMERICS (semi-exact): split facet data.  Each facet F_k carries two linear chart maps: on the piece adjacent to
its first corner (tau<tau_a) ratio a_k, on the piece adjacent to its second corner (tau>tau_b) ratio b_k; between them
an atom arc (mid-facet, pattern constant) whose chart line is one chord through p*=u.  Facets in the order
F1:(r31->r12), F2:(r12->r23), F3:(r23->r31); for F1 the ratio multiplies h2 (rows: c=(-(x h2+h3), x h2, h3)), etc.
Corner equations kept (NS): b1+1/a2 = b2+1/a3 = b3+1/a1 = k+1.  Arc consistency (pivot normal continuous and
constant on the arc): rho_b/rho_a = b_k/a_k where rho = h_{j}/h_{i} ratio of the two positive coordinates.
Box test as in box_exact.py, with the arc gambles excluded (conservative) and also with the arc gambles given
the common chord normal (exact)."""
import numpy as np, itertools
from box_relax import setup

def cmap(k,h,x):
    h1,h2,h3=h
    if k==0: return np.array([-(x*h2+h3),x*h2,h3])
    if k==1: return np.array([h1,-(h1+x*h3),x*h3])
    return np.array([x*h1,h2,-(x*h1+h2)])

def facet_data(eps,a,b,center=0.5):
    """returns per facet: corners (r,rp), tau_a, tau_b, chord normal on arc."""
    v,kap,F=setup(eps); out={}
    for k in range(3):
        r,rp=F[k]
        # middle region: coordinates that are positive there; ratio rho = coordinate multiplied by x / other one
        # F1 middle: h2>0,h3>0, c-normal direction param u=h3/(x h2+h3) -> continuity: h3/h2 at a / a == at b / b
        idx={0:(1,2),1:(2,0),2:(0,1)}[k]   # (coordinate multiplied by x, other positive coordinate)
        ts=np.linspace(0,1,200001); H=(1-ts)[:,None]*r+ts[:,None]*rp
        mid=(H[:,idx[0]]>0)&(H[:,idx[1]]>0)
        tm=ts[mid]; rho=H[mid,idx[1]]/H[mid,idx[0]]      # increasing or decreasing along tau
        # choose arc: geometric centre of rho-range, rho_b/rho_a = b/a  (rho_a at tau_a, rho_b at tau_b)
        lr=np.log(rho); target=lr.min()+center*(lr.max()-lr.min())
        half=0.5*abs(np.log(b[k]/a[k]))
        if lr[-1]>lr[0]: la,lb=target-half,target+half      # rho increasing along tau
        else: la,lb=target+half,target-half
        ta=tm[np.argmin(abs(lr-la))]; tb=tm[np.argmin(abs(lr-lb))]
        ha=(1-ta)*r+ta*rp; hb=(1-tb)*r+tb*rp
        na=cmap(k,ha,a[k]); nb=cmap(k,hb,b[k])
        out[k]=dict(r=r,rp=rp,ta=min(ta,tb),tb=max(ta,tb),na=na/np.linalg.norm(na),nb=nb/np.linalg.norm(nb),
                    a=a[k],b=b[k],okarc=(lr.min()<min(la,lb) and max(la,lb)<lr.max()))
    return out,kap

def cvec_piece(fd,k,t):
    d=fd[k]; h=(1-t)*d['r']+t*d['rp']
    if t<=d['ta']: return h,cmap(k,h,d['a'])
    if t>=d['tb']: return h,cmap(k,h,d['b'])
    return h,d['na']*np.linalg.norm(h)     # arc: chord normal

def box_margin(fd,ns=600,nt=1500,use_arc=False):
    best=-np.inf; arg=None
    ts=np.linspace(1e-5,1-1e-5,nt)
    HC={}
    for k in range(3):
        L=[]
        for t in ts:
            d=fd[k]
            if (not use_arc) and d['ta']<t<d['tb']: continue
            L.append(cvec_piece(fd,k,t))
        HC[k]=(np.array([h for h,_ in L]),np.array([c for _,c in L]))
    ss=np.linspace(1e-4,1-1e-4,ns)
    for a,b in itertools.permutations(range(3),2):
        q=np.zeros((ns,3)); q[:,a]=1-ss; q[:,b]=ss
        for k in range(3):
            HA,CA=HC[k]; mA=(HA[:,a]<0)&(HA[:,b]>0)
            if not mA.any(): continue
            RA=-HA[mA,a]/HA[mA,b]; PA=(CA[mA]@q.T)>0           # (nA,ns)
            SA=np.where(PA,RA[:,None],0).max(0)
            for kk in range(3):
                HB,CB=HC[kk]; mB=(HB[:,b]<0)&(HB[:,a]>0)
                if not mB.any(): continue
                RB=-HB[mB,b]/HB[mB,a]; PB=(CB[mB]@q.T)>0
                SB=np.where(PB,RB[:,None],0).max(0)
                pr=SA*SB; j=pr.argmax()
                if pr[j]>0 and np.log(pr[j])>best: best=np.log(pr[j]); arg=(a+1,b+1,k+1,kk+1,round(ss[j],4))
    return best,arg

if __name__=="__main__":
    for eps in [0.1,0.3,0.6,0.9]:
        kap=(1+2*eps)/(1-eps)
        for aa in [1/kap+0.25*(1-1/kap),0.5*(1/kap+1),1/kap+0.75*(1-1/kap)]:
            bb=kap+1-1/aa
            fd,_=setup_fd=facet_data(eps,(aa,)*3,(bb,)*3)
            print(f"eps={eps} a={aa:.4f} b={bb:.4f} ab={aa*bb:.4f} arcs ok={[fd[k]['okarc'] for k in range(3)]}",
                  "excl:",box_margin(fd),"arc-normal:",box_margin(fd,use_arc=True))
        # control: unsplit (a=b=x+): must give certificate
        xp=((kap+1)+np.sqrt((kap+1)**2-4))/2
        fd,_=facet_data(eps,(xp,)*3,(xp,)*3)
        print("   control x+ unsplit:",box_margin(fd))
