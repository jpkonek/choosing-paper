# I2 referee: Theorem 3 input = Prop T1 box certificate at the failing pair (a,b)=(1,2), x=x_+, p*=u.
# Check for small s: A in relint F_1, B in relint F_3, c_1(A).q0>0, c_3(B).q0>0, an interval of lambda>0
# with (A+lam B)_1<0, (A+lam B)_2<0, and A,B -> Sigma limits (-beta,0,1), (1,0,-beta).
import numpy as np
def c1(h,x): return np.array([-(x*h[1]+h[2]), x*h[1], h[2]])
def c3(h,x): return np.array([x*h[0], h[1], -(x*h[0]+h[1])])
for eps in [0.05,0.3,0.6,0.9]:
    k=(1+2*eps)/(1-eps); x=((k+1)+np.sqrt((k+1)**2-4))/2; beta=1/k; c0=(1-eps)/3
    v=[c0*np.ones(3)+eps*np.eye(3)[i] for i in range(3)]
    print(f"eps={eps} kappa={k:.4f} x+^2/kappa={x*x/k:.4f}")
    for s in [1e-2,1e-3,1e-4]:
        th=0.5*(1+1/np.sqrt(x*x*beta))+0.25*(1-1/np.sqrt(x*x*beta))   # theta in (1/sqrt(beta x^2),1)
        zeta=th*s*x/(1-s); eta=s/(th*x*(1-2*s))
        A=np.array([-beta*(1+eta),eta,1.0]); B=np.array([1.0,-zeta,-beta*(1-zeta)])
        q0=np.array([s,1-s,0.0])
        onF1=(abs(A@v[0])<1e-12, A@v[1]>0, A@v[2]>0); onF3=(abs(B@v[2])<1e-12, B@v[0]>0, B@v[1]>0)
        pa, pb = c1(A,x)@q0, c3(B,x)@q0
        lo=A[1]/abs(B[1]); hi=abs(A[0])/B[0]     # need lam>A_2/|B_2| and lam<|A_1|/B_1
        print(f"  s={s:.0e}: A on F1 {onF1}, B on F3 {onF3}, c1(A).q0={pa:.2e}>0:{pa>0}, c3(B).q0={pb:.2e}>0:{pb>0}, lambda in ({lo:.4f},{hi:.4f}) nonempty:{lo<hi}, |A-(-b,0,1)|={np.linalg.norm(A-[-beta,0,1]):.1e}")
