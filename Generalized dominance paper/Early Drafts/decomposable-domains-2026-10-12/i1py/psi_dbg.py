import numpy as np
from psi_maps import *
eps=0.3; S,x,kap=T1_system(eps,'+'); u=np.ones(3)/3
k=0
i,j=1,2
r0=np.cross(S.V[k],S.V[i]); r0=r0 if r0@S.V[j]>0 else -r0
r1=np.cross(S.V[k],S.V[j]); r1=r1 if r1@S.V[i]>0 else -r1
for t in [0.15,0.2,0.4,0.6]:
    h=(1-t)*r0+t*r1; th=chord_dir(S,k,h,u)
    g,pair=phi_k(S,k,u,th)
    print(t,pair,"Phi(chord) vs l_h:",np.round(np.cross(g/np.linalg.norm(g),h/np.linalg.norm(h)),8))
for (ta,tb) in [(0.15,0.2),(0.4,0.6)]:
    ths=[chord_dir(S,k,(1-t)*r0+t*r1,u) for t in (ta,tb)]
    P,pair=psi_point(S,k,u,*ths); print(pair,"psi(u)=",np.round(P,6),"v_k=",np.round(S.V[k],6))
