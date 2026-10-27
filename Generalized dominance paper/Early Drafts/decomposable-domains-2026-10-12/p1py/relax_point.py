"""P1 NUMERICS: test the candidate (x1,x2,x3)=(kappa,1,1/kappa), which satisfies the corner equations at r12,r23
 and the box product bounds 1/kappa<=x_i x_j<=kappa with equality; and nearby points."""
import numpy as np
from box_relax import best_cert, setup
for eps in [0.1,0.3,0.6]:
    v,kap,F=setup(eps)
    x=(kap,1.0,1/kap)
    print("eps",eps,"corner r12:",x[0]+1/x[1]-kap-1,"r23:",x[1]+1/x[2]-kap-1,"r31 defect:",x[2]+1/x[0]-kap-1)
    for d in [0,0.02,-0.02]:
        xx=(x[0]*(1+d),x[1],x[2])
        m,arg=best_cert(xx,eps,nt=301,ns=200,skip={0:(0,0.05),2:(0.95,1)})
        print("   x1 scaled by",1+d,"margin",m,arg)
    m,arg=best_cert(x,eps,nt=301,ns=200)   # no skipped arcs
    print("   no arcs skipped: margin",m,arg)
