# I2: exact check of the transition-point equation sigma_w(q) = Phi(q) near e_2 (T1, p*=u, x=x+)
import numpy as np
def data(eps):
    k=(1+2*eps)/(1-eps); x=((k+1)+np.sqrt((k+1)**2-4))/2; return k,x
def c1(h,x): return np.array([-(x*h[1]+h[2]), x*h[1], h[2]])
def c3(h,x): return np.array([x*h[0], h[1], -(x*h[0]+h[1])])
def F1(z,k): return np.array([-1.0, z, k-z])      # F_1 gambles near w'=(-1,0,k)
def F3(z,k): return np.array([k-z, z, -1.0])      # F_3 gambles near w=(k,0,-1)
def Phi(q,k,x):
    # facet gambles whose chord passes through q (c.q affine in z -> solve), then intersect their zero lines
    a0=c1(F1(0,k),x)@q; a1=c1(F1(1,k),x)@q-a0; z=-a0/a1
    b0=c3(F3(0,k),x)@q; b1=c3(F3(1,k),x)@q-b0; zp=-b0/b1
    h=F1(z,k); hp=F3(zp,k)
    m=np.cross(h,hp); return m/m.sum(), z, zp
def sig(q,w): m=w*q; return m/m.sum()
for eps in [0.05,0.2,0.3,0.6,0.9]:
    k,x=data(eps)
    v=k/(1-k*k)*np.array([1/x-k*x, k/x-x])
    print(f"eps={eps}: kappa={k:.4f} x+={x:.4f}  v=({v[0]:.4f},{v[1]:.4f})  v1-v3={v[0]-v[1]:.6f} (kappa={k:.6f})")
    # finite-scale check of blow-up of Phi at e_2
    for y in [(1,0.3),(1,0.0),(2,1)]:
        t=1e-6; q=np.array([t*y[0],1-t*(y[0]+y[1]),t*y[1]])
        m,_,_=Phi(q,k,x); mu=np.array([m[0],m[2]])/t
        print("   y=",y," Phi blowup=",np.round(mu,5)," predicted=",np.round((y[0]-y[1])*v,5))
    # identity (w=1): |G(q)|/|q-e2| bounded below on the e_a side sector?  (det != 0)
    W=np.eye(2); M=W-np.outer(v,[1,-1]); print("   det(W-Phihat) identity:",np.linalg.det(M))
