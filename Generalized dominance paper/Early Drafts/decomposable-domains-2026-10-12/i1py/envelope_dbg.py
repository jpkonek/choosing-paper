import numpy as np
from envelope import *
eps=0.3; kap,v,xp=setup(eps)
x=xp
u=np.ones(3)/3
d=np.array([1,-0.5,-0.5]); d/=np.linalg.norm(d)
for r in [0.03,0.01,0.003,0.001]:
    q=u+r*d
    TH,G,gaps=test(eps,x,q,nth=360)
    print(f"r={r} lines={len(G)} maxgap={np.nanmax(gaps):.3e} maxgap/r={np.nanmax(gaps)/r:.3f} #>1e-9 {np.sum(gaps>1e-9*1)}")
