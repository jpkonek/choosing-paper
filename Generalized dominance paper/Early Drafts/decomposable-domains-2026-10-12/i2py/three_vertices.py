# I2: at each vertex b (x=x+, failing pairs (1,2),(2,3),(3,1)), transition points q (precise, limit of
# non-precise) must satisfy sigma_w(q) = Phi_b(q). Measure m_b(w) = min over the closed sector between
# lambda_b and the failing edge, at radius r, of |sigma_w(q)-Phi_b(q)|/r.  Escape needs m_b(w)=0 for all b.
import numpy as np, itertools
def data(eps):
    k=(1+2*eps)/(1-eps); x=((k+1)+np.sqrt((k+1)**2-4))/2; return k,x
def cvec(kf,h,x):  # writeup c_k(h)
    h1,h2,h3=h
    if kf==1: return np.array([-(x*h2+h3), x*h2, h3])
    if kf==2: return np.array([h1, -(h1+x*h3), x*h3])
    if kf==3: return np.array([x*h1, h2, -(x*h1+h2)])
def facet_gamble(kf,i,z,k):
    # gamble on F_kf with coordinate i equal z, other non-kf coordinate solved; h_kf=-1
    eps=None
    h=np.zeros(3); h[kf-1]=-1.0; h[i-1]=z; j=6-kf-i; h[j-1]=k-z   # c0*(sum)+eps*h_kf=0 <=> sum = kappa-1 ... check below
    return h
def on_facet(kf,h,k,eps):
    c0=(1-eps)/3; v=c0*np.ones(3); v[kf-1]+=eps; return v@h
def Phi(q,b,a,c,k,x):
    # b-crossing gambles: on F_a (coordinate b ~ 0) and on F_c (coordinate b ~ 0)
    out=[]
    for kf in (a,c):
        g=lambda z: facet_gamble(kf,b,z,k)
        a0=cvec(kf,g(0.0),x)@q; a1=cvec(kf,g(1.0),x)@q-a0
        out.append(g(-a0/a1))
    m=np.cross(out[0],out[1]); return m/m.sum()
def sig(q,w): m=w*q; return m/m.sum()
pairs={2:(1,3),3:(2,1),1:(3,2)}  # b:(a,c) for x+
for eps in [0.05,0.3,0.6,0.9]:
    k,x=data(eps)
    # sanity: facet gambles lie on facets
    assert abs(on_facet(1,facet_gamble(1,2,0.3,k),k,eps))<1e-12
    r=1e-4; best=1e9; bestw=None
    def mb(w,b):
        a,c=pairs[b]; eb=np.eye(3)[b-1]; ea=np.eye(3)[a-1]; ec=np.eye(3)[c-1]
        u=np.ones(3)/3; dl=(u-eb)/np.linalg.norm(u-eb); de=(ea-eb)/np.linalg.norm(ea-eb)
        vals=[]
        for s in np.linspace(0,1,41):
            d=(1-s)*dl+s*de; d/=np.linalg.norm(d); q=eb+r*d
            vals.append(np.linalg.norm(sig(q,w)-Phi(q,b,a,c,k,x))/r)
        return min(vals)
    for l1 in np.linspace(-3,3,31):
        for l2 in np.linspace(-3,3,31):
            w=np.array([1.0,np.exp(l1),np.exp(l2)])
            val=max(mb(w,b) for b in (1,2,3))
            if val<best: best,bestw=val,w
    print(f"eps={eps}: min_w max_b m_b(w) = {best:.4f} at w={np.round(bestw,3)};  identity: {[round(mb(np.ones(3),b),4) for b in (1,2,3)]}")
