# NUMERICS: sign patterns around the boundary of D_{T1} (eps=0.3); checks the
# 6-cycle of patterns used in the location statements of N25 Thm 9.1.
import numpy as np
eps=0.3; c0=(1-eps)/3
V=[c0*np.ones(3)+eps*np.eye(3)[k] for k in range(3)]
def cr(a,b):
    x=np.cross(V[a],V[b]); o=3-a-b
    return x if x@V[o]>0 else -x
seq=[]
for k,(i,j) in [(0,(2,1)),(1,(0,2)),(2,(1,0))]:
    r1,r2=cr(k,i),cr(k,j)
    for tau in np.linspace(1e-4,1-1e-4,4000):
        h=(1-tau)*r1+tau*r2
        assert abs(h@V[k])<1e-9 and all(h@V[m]>=-1e-9 for m in range(3))
        s=''.join('+' if x>0 else '-' for x in h)
        if not seq or seq[-1][1]!=s: seq.append(('F%d'%(k+1),s))
print(seq)
