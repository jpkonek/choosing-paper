import numpy as np
from general import *
from middle_test import family
eps=0.3; kap=(1+2*eps)/(1-eps); c0=(1-eps)/3
V=[c0*np.ones(3)+eps*E[k] for k in range(3)]
def mk(x):
    def cfun(k,h):
        h1,h2,h3=h
        if k==0: return np.array([-(x*h2+h3),x*h2,h3])
        if k==1: return np.array([h1,-(h1+x*h3),x*h3])
        return np.array([x*h1,h2,-(x*h1+h2)])
    return System(V,cfun)
u=np.ones(3)/3
for x in [1.0,1.2]:
    S=mk(x)
    for d in [np.array([0,1,-1.]),np.array([0,-1,1.]),np.array([2,-1,-1.]),np.array([-2,1,1.])]:
        d/=np.linalg.norm(d); r=1e-3; q=u+r*d
        TH,G=family(S,q,0,((0,1),(2,0)))
        gp=gaps(G) if len(G) else np.array([np.nan])
        print(f"x={x} facet1 middle window, delta={np.round(d,3)}: n={len(G)} max gap/r={np.nanmax(gp)/r:.4f}")
