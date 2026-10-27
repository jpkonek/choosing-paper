# Sanity checks (NUMERICS only) for the X* geometry used in INC72_report.md
import numpy as np
rng=np.random.default_rng(0)
f=lambda t: np.where(t>=0,2*t,t/2)
H=rng.normal(size=(400000,2))*3
h1,h2=H[:,0],H[:,1]
inX=h1+f(h2)>0
R1=(h1>0)&(h2<-2*h1); R2=(h2>0)&(h1<-2*h2); Qmm=(h1<0)&(h2<0)
S1=(h1>0)&(h2<0)&(h2>-2*h1); S2=(h2>0)&(h1<0)&(h1>-2*h2); Qpp=(h1>0)&(h2>0)
print("complement of X* = R1+R2+Q--:", np.all((~inX)==(R1|R2|Qmm)))
print("X* = Q++ + S1 + S2:", np.all(inX==(Qpp|S1|S2)))
# hull bound: any q with q.h>=0 at some h in R1 has q1>=2 q2
qs=rng.dirichlet([1,1],size=2000)
ok=True
for q in qs:
    if np.any(H[R1]@q>=0) and q[0]<2*q[1]-1e-12: ok=False
print("q.h>=0 somewhere on R1 => q1>=2q2:", ok)
# D_{q1>=2q2} = {h1>0, h2>-2h1}: extreme states (1,0),(2/3,1/3)
D=(h1>0)&((2*h1+h2)/3>0)
print("D_{conv(d1,(2/3,1/3))} = Q++ u S1 (mod axes):", np.all(D==(Qpp|S1)))
# score-sum maximiser: phi=h1+f(h2)
phi=h1+f(h2); print("phi>0 exactly on X*:", np.all((phi>0)==inX))
