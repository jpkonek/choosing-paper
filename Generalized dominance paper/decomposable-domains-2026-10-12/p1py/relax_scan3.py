"""P1 NUMERICS: on the corner-relaxed family (r12,r23 equations kept) the atom at r31 needs defect>0, i.e.
x2 in (1/(k+1), x_-). Test box certificates there, excluding the MAXIMAL atom arcs (from r31 to the first crossing
on F1 and on F3), so that no gamble whose chart could be the atom chord is used."""
import numpy as np
from box_relax import best_cert, setup
for eps in [0.05,0.3,0.7,0.95]:
    v,kap,F=setup(eps)
    r31,r12=F[0]; r23,_=F[2]
    # F1: h=(1-t)r31+t r12; first crossing: h3=0 -> t=1/(k+2)... solve
    t1=(-r31[2])/(r12[2]-r31[2])          # h3 crosses zero on F1
    # F3: h=(1-t)r23+t r31; crossing nearest r31 where h1=0
    t3=(r23[0])/(r23[0]-r31[0])
    xm=((kap+1)-np.sqrt((kap+1)**2-4))/2
    print(f"eps={eps} kappa={kap:.3f} x-={xm:.4f} arcs: F1 tau<{t1:.3f}, F3 tau>{t3:.3f}")
    for x2 in np.linspace(1/(kap+1),xm,9)[1:-1]:
        x1=kap+1-1/x2; x3=1/(kap+1-x2); d=x3+1/x1-kap-1
        m,arg=best_cert((x1,x2,x3),eps,nt=241,ns=160,skip={0:(0,t1),2:(t3,1)})
        print(f"   x2={x2:.4f} x1={x1:.4f} x3={x3:.4f} defect={d:+.3f} margin={m:+.5f} {arg}")
