"""P1 NUMERICS: drop the corner equation at r31 (atom chord through p* at that corner); scan the 1-parameter family
x2=k+1-1/x3, x1=k+1-1/x2 and test for box certificates, excluding atom arcs of length delta at r31 on F1 and F3."""
import numpy as np
from box_relax import best_cert, setup
for eps in [0.1,0.3,0.6]:
    v,kap,F=setup(eps)
    print("eps",eps,"kappa",round(kap,4))
    for x3 in np.concatenate([np.linspace(0.3,1.0,8),np.linspace(1.1,3,8)]):
        x2=kap+1-1/x3
        if x2<=0: continue
        x1=kap+1-1/x2
        if x1<=0: continue
        m,arg=best_cert((x1,x2,x3),eps,nt=201,ns=120,skip={0:(0,0.05),2:(0.95,1)})
        print(f"  x3={x3:.3f} x2={x2:.3f} x1={x1:.3f} defect(r31)={x3+1/x1-kap-1:+.3f} margin={m:+.4f} {arg}")
