"""P1 NUMERICS: identify the box region exactly: compare semi-exact margin with
 M(x)=max over pairs {i,j} of max(log(x_i x_j/k), log(1/(k x_i x_j)))."""
import numpy as np, itertools
from box_exact import box_margin
from box_relax import setup
rng=np.random.default_rng(7)
for eps in [0.2,0.5]:
    v,kap,F=setup(eps)
    for _ in range(8):
        x=np.exp(rng.uniform(-1.5,1.5,3))
        m,arg=box_margin(tuple(x),eps,ns=600)
        cands={}
        for i,j in itertools.combinations(range(3),2):
            p=x[i]*x[j]; cands[(i+1,j+1,'up')]=np.log(p/kap); cands[(i+1,j+1,'lo')]=np.log(1/(kap*p))
        km=max(cands,key=cands.get)
        print(f"eps={eps} x={np.round(x,3)} margin={m:+.4f} {arg}  bestcand={km}:{cands[km]:+.4f}")
