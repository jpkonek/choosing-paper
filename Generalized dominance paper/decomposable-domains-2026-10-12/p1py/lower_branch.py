"""P1 NUMERICS (semi-exact): single atom at corner r31 (corner eqs at r12,r23 kept, r31 replaced by the overlap
inequality x3+1/x1>k+1). Both branches; certificates searched with the MAXIMAL r31 arcs excluded from F1 and F3."""
import numpy as np
from box_exact import box_margin
from box_relax import setup
for eps in [0.02,0.1,0.3,0.5,0.7,0.9,0.95,0.99]:
    v,kap,F=setup(eps)
    r31,r12=F[0]; r23,_=F[2]
    t1=(-r31[2])/(r12[2]-r31[2]); t3=(r23[0])/(r23[0]-r31[0])
    xm=((kap+1)-np.sqrt((kap+1)**2-4))/2; xp=1/xm
    out=[]
    for x2 in list(np.linspace(1/(kap+1),xm,6)[1:-1])+list(np.linspace(xp,kap+1,6)[1:-1]):
        x1=kap+1-1/x2; x3=1/(kap+1-x2); d=x3+1/x1-kap-1
        m,arg=box_margin((x1,x2,x3),eps,ns=800,excl={0:(0,t1),2:(t3,1)})
        out.append(f"x2={x2:.4g}:d={d:+.2f},logm={m:+.3f}{arg[:4]}")
    print(f"eps={eps}: "+" | ".join(out))
