"""Check that the certificate windows are admissible: prior crossings in the non-failing parts and
probability crossings supplied by facet F_1 (general.py, full piecewise edge maps)."""
import numpy as np
from general import *
for eps in [0.05,0.3,0.6,0.9]:
    for w,ys,y2 in [('+',[0.52,0.54,0.56],None),('-',[0.96,0.97,0.98],None)]:
        S,x,kap=T1_system(eps,w); u=np.ones(3)/3
        ok=True; info=[]
        for y1 in ys:
            Y1=(1-y1)*E[0]+y1*E[1]
            # crossing of line(u,Y1) with [e3,e1]
            d=Y1-u
            A=np.array([E[0]-E[2],-d]).T; t,l=np.linalg.lstsq(A,u-E[2],rcond=None)[0]
            nf1=S.nonfail(0,1,y1); nf2=S.nonfail(2,0,t)
            # facet supplying the tangents
            z1=S.inv(0,1,'j',y1); z2=S.inv(2,0,'i',t)
            k1=[k for k,h in S.tangents((1-z1)*E[0]+z1*E[1]) if h[1]>0>h[0]][0]
            k2=[k for k,h in S.tangents((1-z2)*E[2]+z2*E[0]) if h[2]>0>h[0]][0]
            ok&= nf1 and nf2 and k1==0 and k2==0 and 0<t<1
            info.append((y1,round(t,4),nf1,nf2,k1+1,k2+1))
        print(f"eps={eps} x{w}: admissible={ok}  (y1, y2, nonfail1, nonfail2, facet@z1, facet@z2): {info}")
