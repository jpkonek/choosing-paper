"""Referee check of C2 Thm 4.1 step 1 (box witnesses near e_2; s0 shrinks as eps->1, so s<=1e-5 is used for eps>=0.8, failing pair (a,b)=(1,2), x=x+):
A=(-beta(1+eta),eta,1) in relint F_1, B=(1,-zeta,-beta(1-zeta)) in relint F_3, q0=(s,1-s,0).
Checks: A.v_1=0, A.v_j>0; B.v_3=0, B.v_j>0; c_1(A).q0>0, c_3(B).q0>0; ratio A_b B_a < |A_a||B_b|;
an interval of lambda with (A+lambda B)_1<0, (A+lambda B)_2<0.  Then: for the line through a W_II-cap point
parallel to the failing edge, the crossing points with lambda_2=line(u,e2) and lambda_3=line(u,e3) are interior."""
import numpy as np
for eps in (0.01,0.05,0.3,0.6,0.9,0.99):
    k=(1+2*eps)/(1-eps); x=((k+1)+np.sqrt((k+1)**2-4))/2; beta=1/k; c0=(1-eps)/3
    v=[c0*np.ones(3)+eps*np.eye(3)[i] for i in range(3)]
    C1=np.array([[0,-x,-1],[0,x,0],[0,0,1.]]); C3=np.array([[x,0,0],[0,1,0],[-x,-1,0.]])
    ok=True; worst=[]
    for s in ((1e-2,1e-3,1e-4) if eps<0.8 else (1e-5,1e-6,1e-7)):
        th=0.5*(1+1/np.sqrt(beta*x*x))   # theta in (1/sqrt(beta x^2),1)
        zeta=th*s*x/(1-s); eta=s/(th*x*(1-2*s))
        A=np.array([-beta*(1+eta),eta,1.]); B=np.array([1.,-zeta,-beta*(1-zeta)]); q0=np.array([s,1-s,0.])
        memb=abs(A@v[0])<1e-12 and A@v[1]>0 and A@v[2]>0 and abs(B@v[2])<1e-12 and B@v[0]>0 and B@v[1]>0
        ca=(C1@A)@q0; cc=(C3@B)@q0; ratio=A[1]*B[0]<abs(A[0])*abs(B[1])
        lo,hi=eta/zeta,beta*(1+eta)
        ok&= memb and ca>0 and cc>0 and ratio and lo<hi
        worst.append((s,round(ca,8),round(cc,8),round(hi-lo,4)))
    print(f"eps={eps}: x^2/kappa={x*x/k:.3f}  all witness conditions hold: {ok}  (s, c1(A).q0, c3(B).q0, lambda-window) {worst}")
    # Thm A geometry for the W_II cap: cap point at angle slope r=d3/d1 = 0.5/x from e2, radius rho
    u=np.ones(3)/3; e1,e2,e3=np.eye(3)
    for rho in (1e-2,1e-3):
        q=e2+rho*np.array([1,-(1+0.5/x),0.5/x])
        d=e1-e2   # direction of failing edge
        def hit(P,Q):  # intersection of line q+t d with line(P,Q) in aff Delta
            M=np.array([d,-(Q-P)]).T; sol=np.linalg.lstsq(M,P-q,rcond=None)[0]; return q+sol[0]*d
        y1=hit(u,e2); y2=hit(u,e3)
        print(f"     rho={rho}: y1 on lambda_2 = {np.round(y1,5)} interior {bool(np.all(y1>0))}; y2 on lambda_3 = {np.round(y2,5)} interior {bool(np.all(y2>0))}")
