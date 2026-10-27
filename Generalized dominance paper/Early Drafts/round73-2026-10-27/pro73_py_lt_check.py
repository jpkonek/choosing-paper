# NUMERICS for PRO73: (1) local matched triples for the Gaussian on R^n (n=2,3), sum and midpoint,
# built as: polar map in the plane P=span(x,y) with parameter h_perp, identity on P-perp for T.
# (2) separable loss-averse F with {F>0} = D_Q for Q=[a,b] (two worlds).
import numpy as np
rng=np.random.default_rng(0)

def rho(v): return np.exp(-0.5*np.sum(v**2))/(2*np.pi)**(len(v)/2)

def make_maps(x,y,kind,n):
    # x,y in R^2 (plane coords); returns T,S on R^n (first two coords = plane)
    r0=np.hypot(*x); phi0=np.arctan2(x[1],x[0])
    ty=np.hypot(*y); s_target = np.hypot(*(x+y)) if kind=='sum' else np.hypot(*((x+y)/2))
    ang = np.arctan2(y[1],y[0])-phi0
    sgn = np.sign(np.sin(ang))
    m=n-2
    def lamS(hp):
        if kind=='sum': return 2.0**(-m)*np.exp(1.5*np.sum(hp**2))   # mass factor for S in the plane
        return 2.0
    def tau(r):   # e^{-tau^2/2} = e^{-r^2/2} + C,  lambda_T = 1
        C=np.exp(-ty**2/2)-np.exp(-r0**2/2)
        return np.sqrt(-2*np.log(np.exp(-r**2/2)+C))
    def sig(r,hp):
        L=lamS(hp); C=np.exp(-s_target**2/2)-L*np.exp(-r0**2/2)
        return np.sqrt(-2*np.log(L*np.exp(-r**2/2)+C))
    def T(h):
        hp=h[2:]; r=np.hypot(h[0],h[1]); phi=np.arctan2(h[1],h[0])
        t=tau(r); s=sig(r,hp)
        c=((s**2-r**2-t**2)/(2*r*t)) if kind=='sum' else ((4*s**2-r**2-t**2)/(2*r*t))
        th=sgn*np.arccos(c)
        return np.concatenate([[t*np.cos(phi+th), t*np.sin(phi+th)], hp])
    def S(h):
        th=T(h)
        if kind=='sum': return h+th
        return (h+th)/2
    return T,S

def jac(F,h,eps=1e-6):
    n=len(h); J=np.zeros((n,n))
    for i in range(n):
        e=np.zeros(n); e[i]=eps
        J[:,i]=(F(h+e)-F(h-e))/(2*eps)
    return J

worst=0
for n in (2,3,4):
    for kind in ('sum','mid'):
        x=np.array([-1.5,1.0]); y=np.array([1.0,-1.5])
        T,S=make_maps(x,y,kind,n)
        k = 1.0 if kind=='sum' else 0.5   # S_*(mu|G1) = k^{-1}... : rho(Sh)|detDS| = rho(h)/k
        for _ in range(200):
            h=np.concatenate([x,np.zeros(n-2)])+0.02*rng.standard_normal(n)
            a=abs(rho(T(h))*abs(np.linalg.det(jac(T,h)))-rho(h))/rho(h)
            # sum: S pushes mu|G1 to mu|G3  -> rho(Sh)|det DS| = rho(h)
            # mid: S pushes mu|G1 to 1/2 mu|G3 -> rho(Sh)|det DS| = 2 rho(h)
            target = rho(h) if kind=='sum' else 2*rho(h)
            b=abs(rho(S(h))*abs(np.linalg.det(jac(S,h)))-target)/target
            assert np.isfinite(a) and np.isfinite(b); worst=max(worst,a,b)
        h0=np.concatenate([x,np.zeros(n-2)])
        print(n,kind,'T(x)=',np.round(T(h0),6),'S(x)=',np.round(S(h0),6))
print('max relative Jacobian error',worst)

# (2) separable F for Q=[a,b]: q=(t,1-t)
bad=0
for _ in range(2000):
    a,b=np.sort(rng.uniform(0.02,0.98,2))
    cp1=1.0; cm2=(1-a)/a; s=rng.uniform((1-b)/b,(1-a)/a); cp2=s; cm1=s*b/(1-b)
    assert cm1>=cp1-1e-12 and cm2>=cp2-1e-12
    f1=lambda t: np.where(t>0,cp1*t,cm1*t); f2=lambda t: np.where(t>0,cp2*t,cm2*t)
    H=rng.standard_normal((500,2))*3
    F=f1(H[:,0])+f2(H[:,1])
    PQ=np.minimum(a*H[:,0]+(1-a)*H[:,1], b*H[:,0]+(1-b)*H[:,1])
    bad+=np.sum((F>0)!=(PQ>0))
print('sandwich mismatches',bad)
