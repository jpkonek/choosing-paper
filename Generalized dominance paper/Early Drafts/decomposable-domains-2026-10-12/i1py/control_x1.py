"""Control: same pipeline with the (non-admissible, corner-equation-violating) value x=1, for which
C_k = line(p*,e_k).  The envelope gaps near p* should vanish (vertex maps nu(v_k * q))."""
import numpy as np
from general import *
eps=0.3
kap=(1+2*eps)/(1-eps); c0=(1-eps)/3
V=[c0*np.ones(3)+eps*E[k] for k in range(3)]
x=1.0
def cfun(k,h):
    h1,h2,h3=h
    if k==0: return np.array([-(x*h2+h3),x*h2,h3])
    if k==1: return np.array([h1,-(h1+x*h3),x*h3])
    return np.array([x*h1,h2,-(x*h1+h2)])
S=System(V,cfun); u=np.ones(3)/3
for d in [np.array([2,-1,-1.]),np.array([0,1,-1.]),np.array([-1,2,-1.])]:
    d/=np.linalg.norm(d)
    for r in [0.01,-0.01]:
        q=u+r*d; TH,G,gp,bad=envelope(S,q,nth=180)
        # compare with nu(v_k * q)
        Ks=np.array([V[k]*q/(V[k]@q) for k in range(3)])
        supp=np.array([(Ks@g).min() for g in G])
        print(f"x=1 control q-u={np.round(r*d,4)}: lines={len(G)} max gap={np.nanmax(gp):.2e}; max|min over conv(nu(v_k q)) of g.m|={np.abs(supp).max():.2e}")
