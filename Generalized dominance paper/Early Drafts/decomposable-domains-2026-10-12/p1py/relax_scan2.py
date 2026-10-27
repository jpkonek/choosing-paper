"""P1 NUMERICS: (1) test the conjectured exact box region {1/k<=x1x3,x2x1,x3x2<=k}? (2) scan the corner-relaxed family
by x2 in (1/(k+1),1], x1=phi(x2), x3=1/(k+1-x2); report r31 defect x3+1/x1-(k+1) (atom needs >0) and box margin."""
import numpy as np
from box_relax import best_cert, setup
rng=np.random.default_rng(1)
eps=0.3; v,kap,F=setup(eps)
print("(1) random x, predicted feasible iff all products in [1/k,k]")
for _ in range(12):
    x=np.exp(rng.uniform(-1.2,1.2,3))
    pr=[x[0]*x[2],x[1]*x[0],x[2]*x[1]]
    pred=all(1/kap<=p<=kap for p in pr)
    m,arg=best_cert(tuple(x),eps,nt=201,ns=120)
    print(f"  x={np.round(x,3)} prods={np.round(pr,3)} pred_feasible={pred} margin={m:+.4f} {arg}")
print("(2) relaxed family")
for x2 in np.linspace(1/(kap+1)+0.02,1.0,10):
    x1=kap+1-1/x2; x3=1/(kap+1-x2)
    d=x3+1/x1-kap-1
    for delta in [0.05,0.2]:
        m,arg=best_cert((x1,x2,x3),eps,nt=201,ns=120,skip={0:(0,delta),2:(1-delta,1)})
        print(f"  x2={x2:.3f} x1={x1:.3f} x3={x3:.3f} defect={d:+.3f} arc={delta} margin={m:+.4f} {arg}")
