import numpy as np, sys
from general import *
eps=float(sys.argv[1]); w=sys.argv[2]
S,x,kap=T1_system(eps,w)
u=np.ones(3)/3
for dname,d in [('to e1',np.array([2,-1,-1.])),('to e2',np.array([-1,2,-1.])),('mid',np.array([1,1,-2.])),('rand',np.array([0.3,-1.1,0.8]))]:
    d=d/np.linalg.norm(d)
    for r in [0.02,0.002]:
        q=u+r*d
        TH,G,gp,bad=envelope(S,q,nth=180)
        print(f"eps={eps} x{w} dir {dname} r={r}: lines={len(G)} signbad={bad} maxgap={np.nanmax(gp):.3e} gap/r={np.nanmax(gp)/r:.3f} #gap>1e-9={np.sum(gp>1e-9)}",flush=True)
