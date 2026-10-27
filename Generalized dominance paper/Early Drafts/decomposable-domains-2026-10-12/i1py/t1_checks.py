"""T1: checks of the (PC) data used (corner equations, vertex signs), then the envelope test."""
import numpy as np
from general import *
for eps in [0.3]:
  for w in ['+','-']:
    S,x,kap=T1_system(eps,w)
    V=S.V
    # corners
    for k,j in [(0,1),(1,2),(2,0)]:
        r=np.cross(V[k],V[j]); t=3-k-j
        if r@V[t]<0: r=-r
        a=S.cfun(k,r); b=S.cfun(j,r)
        print(f"eps={eps} x{w}: corner r{k+1}{j+1}: c_k={np.round(a,4)} c_j={np.round(b,4)} cross={np.linalg.norm(np.cross(a,b)):.1e} dot>0 {a@b>0}")
    # vertex signs on facets
    worst=0
    for k in range(3):
        i,j=[l for l in range(3) if l!=k]
        r0=np.cross(V[k],V[i]); r0=r0 if r0@V[j]>0 else -r0
        r1=np.cross(V[k],V[j]); r1=r1 if r1@V[i]>0 else -r1
        for t in np.linspace(0.001,0.999,999):
            h=(1-t)*r0+t*r1; c=S.cfun(k,h)
            u=np.ones(3)/3
            assert abs(c@u)<1e-12
            for l in range(3):
                if abs(h[l])>1e-6 and np.sign(c[l])!=np.sign(h[l]): worst+=1
    print("vertex sign violations:",worst)
