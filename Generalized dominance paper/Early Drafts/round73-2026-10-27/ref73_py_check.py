import numpy as np
rng=np.random.default_rng(73)
# (1) unified functional F = a h1+ - b h1- + (1-b) h2+ - (1-a) h2-  vs D_Q, Q={(t,1-t): a<=t<=b}
H=rng.standard_normal((400000,2))
def DQ(H,a,b): return np.minimum(a*H[:,0]+(1-a)*H[:,1], b*H[:,0]+(1-b)*H[:,1])>0
def F(H,a,b):
    p=lambda t: np.maximum(t,0); m=lambda t: np.maximum(-t,0)
    return a*p(H[:,0])-b*m(H[:,0])+(1-b)*p(H[:,1])-(1-a)*m(H[:,1])
cases=[(0.3,0.6),(0.5,0.5),(0,0.4),(0.4,1),(0,0),(1,1),(0.2,0.2)]+[tuple(sorted(rng.random(2))) for _ in range(20)]
bad=0
for a,b in cases:
    f=F(H,a,b); d=DQ(H,a,b)
    bad+=np.sum((f>0)!=d)+np.sum((f<0)!=(~d))  # zero set measure-zero
    assert b>=a and (1-a)>=(1-b)       # c- >= c+ at both worlds
print("F mismatches over",len(cases),"credal sets:",bad)
a,b=0,1; f=F(H,a,b); print("Q=S: max F on D_S",f[DQ(H,0,1)].max()," (F=0 there, two-case argument needed)")
# (2) independent LT check, sum case, n=3: T(h)=(T_P(h_P),w), S=id+T, Gaussian
x=np.array([1.2,0.3]); y=np.array([-0.4,1.1]); s=x+y
r0=np.linalg.norm(x); ry=np.linalg.norm(y); rs=np.linalg.norm(s)
m=1
def maps(h):
    hp=h[:2]; w=h[2:]; r=np.linalg.norm(hp); phi=np.arctan2(hp[1],hp[0])
    C=np.exp(-ry**2/2)-np.exp(-r0**2/2); tau=np.sqrt(-2*np.log(np.exp(-r**2/2)+C))
    lam=2.0**(-m)*np.exp(1.5*np.dot(w,w)); Cp=np.exp(-rs**2/2)-lam*np.exp(-r0**2/2)
    sig=np.sqrt(-2*np.log(lam*np.exp(-r**2/2)+Cp))
    cth=(sig**2-r**2-tau**2)/(2*r*tau); sgn=np.sign(np.cross(x,y))
    th=sgn*np.arccos(cth)
    th0=np.arctan2(y[1],y[0])-np.arctan2(x[1],x[0])
    Tp=tau*np.array([np.cos(phi+th),np.sin(phi+th)])
    return np.concatenate([Tp,w])
def jac(f,h,e=1e-6):
    n=len(h); J=np.zeros((n,n))
    for i in range(n):
        d=np.zeros(n); d[i]=e; J[:,i]=(f(h+d)-f(h-d))/(2*e)
    return J
rho=lambda h: np.exp(-h@h/2)
h0=np.array([x[0],x[1],0.0]); print("T(x)=",maps(h0)," S(x)=",h0+maps(h0))
err=0
for _ in range(200):
    h=h0+0.05*rng.standard_normal(3)
    T=maps; S=lambda g: g+maps(g)
    e1=rho(T(h))*abs(np.linalg.det(jac(T,h)))-rho(h)
    e2=rho(S(h))*abs(np.linalg.det(jac(S,h)))-rho(h)
    err=max(err,abs(e1),abs(e2))
print("LT n=3 sum, max Jacobian-identity error:",err)
