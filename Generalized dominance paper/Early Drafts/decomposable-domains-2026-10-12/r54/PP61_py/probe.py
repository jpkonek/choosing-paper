import sys, os
sys.path.insert(0, '../PP56_py')
from fractions import Fraction as Fr
from pp50_lib_copy import cell_points, advice
EPS = Fr(3,10)
u = [Fr(1,3)]*3
B = [Fr(406,1200),Fr(421,1200),Fr(373,1200)]
D = [Fr(406,1200),Fr(373,1200),Fr(421,1200)]
Bp = [2*u[i]-B[i] for i in range(3)]; Dp=[2*u[i]-D[i] for i in range(3)]
for G in ({'u':u,'B':B,'D':D}, {'u':u,'B':B,'D':D,'Bp':Bp,'Dp':Dp}):
    seen={}
    for g in cell_points(EPS,G):
        if any(x==0 for x in g): continue
        if sum(g)<=0: continue
        adv=tuple(advice(EPS,G[k],g) for k in sorted(G))
        key=(tuple((x>0)-(x<0) for x in g),adv)
        seen.setdefault(key,g)
    dis=[k for k in seen if len(set(k[1]))>1]
    print(len(G), 'cells(u.g>0)',len(seen),'dis',len(dis), 'advice values', set(v for k in seen for v in k[1]))
