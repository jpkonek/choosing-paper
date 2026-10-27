# Exact consolidation configurations for the standard Gaussian on R^2 (radial-angular construction)
import numpy as np
Psi=lambda r: 1-np.exp(-r*r/2); Psiinv=lambda u: np.sqrt(-2*np.log(1-u))
rho=lambda x,y: np.exp(-(x*x+y*y)/2)/(2*np.pi)
a=np.array([-1.5,1.0]); b=np.array([1.0,-1.5])
r0=np.hypot(*a); t0=np.hypot(*b)
def build(kind):
    s0=np.hypot(*(a+b)) if kind=='sum' else np.hypot(*(a+b))/2
    k=1.0 if kind=='sum' else 2.0   # mass factor: S_* mu|G1 = (1/k) mu|G3
    tau=lambda r: Psiinv(Psi(r)-Psi(r0)+Psi(t0))
    sig=lambda r: Psiinv(k*(Psi(r)-Psi(r0))+Psi(s0))
    c=1.0 if kind=='sum' else 2.0
    def theta(r):
        t=tau(r); s=c*sig(r); cs=(s*s-r*r-t*t)/(2*r*t)
        assert np.all(np.abs(cs)<1), "triangle condition fails"
        return np.arccos(cs)            # theta in (0,pi): b is a rotated by +157.4 deg
    def T(x,y):
        r=np.hypot(x,y); ph=np.arctan2(y,x); t=tau(r); th=theta(r)
        return t*np.cos(ph+th), t*np.sin(ph+th)
    def S(x,y):
        tx,ty=T(x,y); return (x+tx)/c,(y+ty)/c
    return T,S,k
phia=np.arctan2(a[1],a[0]); delta=0.05; beta=0.03
def jac(F,x,y,e=1e-6):
    fx1=np.array(F(x+e,y)); fx0=np.array(F(x-e,y)); fy1=np.array(F(x,y+e)); fy0=np.array(F(x,y-e))
    J=np.column_stack([(fx1-fx0)/(2*e),(fy1-fy0)/(2*e)]); return abs(np.linalg.det(J))
fk=np.vectorize(lambda t: 2*t if t>=0 else t/2)
for kind in ['sum','mid']:
    T,S,k=build(kind)
    errT=errS=0
    for _ in range(200):
        r=r0+delta*np.random.rand(); ph=phia+beta*np.random.rand(); x,y=r*np.cos(ph),r*np.sin(ph)
        tx,ty=T(x,y); sx,sy=S(x,y)
        errT=max(errT,abs(rho(tx,ty)*jac(T,x,y)/rho(x,y)-1))
        errS=max(errS,abs(rho(sx,sy)*jac(S,x,y)/(k*rho(x,y))-1))
    # sample G1 ~ mu|G1 by rejection-free polar sampling weighted by rho
    N=200000; r=Psiinv(Psi(r0)+(Psi(r0+delta)-Psi(r0))*np.random.rand(N)); ph=phia+beta*np.random.rand(N)
    x,y=r*np.cos(ph),r*np.sin(ph); tx,ty=T(x,y); sx,sy=S(x,y)
    massG1=(Psi(r0+delta)-Psi(r0))*beta/(2*np.pi)
    # splitting increment (Z'->Z adds G1,G2 removes G3): world w: int_G1 [v(h)+v(Th)] - int_G3 v
    # int_G3 v dmu = k * int_G1 v(Sh) dmu
    d1=massG1*np.mean(x+tx-k*sx); d2=massG1*np.mean(fk(y)+fk(ty)-k*fk(sy))
    print(kind,": max rel Jacobian err T,S =",errT,errS,
          "| G2 centre",np.round([tx.mean(),ty.mean()],3),"G3 centre",np.round([sx.mean(),sy.mean()],3))
    print("   splitting increment under R_s': world1 =",d1," world2 =",d2," (mass G1 =",massG1,")")
