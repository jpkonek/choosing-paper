"""P1 NUMERICS: atoms at a set S of corners (chords through p*). Corner c in S: overlap inequality
 (x1+1/x2, x2+1/x3, x3+1/x1 for r12,r23,r31) > k+1 ; corners not in S: equality. Box product bounds
 1/k <= x_i x_j <= k (necessary, PROVED for the direct three and via transposition for the mirror three when no
 box gamble lies in an atom arc). Maximise the minimum slack over log-x by random search + local refinement."""
import numpy as np, itertools
from scipy.optimize import minimize
def slack(lx,kap,S):
    x=np.exp(lx); c=[x[0]+1/x[1],x[1]+1/x[2],x[2]+1/x[0]]
    s=[]
    for i in range(3):
        s.append(c[i]-kap-1 if i in S else -abs(c[i]-kap-1))
    for i,j in itertools.combinations(range(3),2):
        p=np.log(x[i]*x[j]); s+= [np.log(kap)-p, p+np.log(kap)]
    return min(s)
for eps in [0.1,0.3,0.7]:
    kap=(1+2*eps)/(1-eps)
    for S in [(0,),(0,1),(0,1,2)]:
        best=-np.inf; bx=None
        rng=np.random.default_rng(0)
        for _ in range(400):
            x0=rng.uniform(-3,3,3)
            r=minimize(lambda z:-slack(z,kap,S),x0,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-12,'maxiter':4000})
            if -r.fun>best: best=-r.fun; bx=np.exp(r.x)
        print(f"eps={eps} kappa={kap:.3f} atoms at corners {S}: best min-slack={best:+.5f} at x={np.round(bx,4)}")
