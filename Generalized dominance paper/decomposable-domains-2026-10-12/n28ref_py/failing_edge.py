"""Which edge carries the failing box at each vertex b, for x+ and x- (Prop boxbridge (c) with the PC data)?"""
import numpy as np, sys
sys.path.insert(0,'.')
from sector_caps2 import setup, corner, cvec, E
def facet_pts(k,v,n=4001):
    i,j=[l for l in range(3) if l!=k]
    r0,r1=corner(k,i,v),corner(k,j,v)
    ts=np.linspace(0,1,n)[1:-1]
    return (1-ts)[:,None]*r0+ts[:,None]*r1
for eps in [0.2,0.3,0.6]:
    kap,v,xp=setup(eps)
    for x,name in [(xp,'x+'),(1/xp,'x-')]:
        res=[]
        for b in range(3):
            for a in range(3):
                if a==b: continue
                c=3-a-b
                FA=facet_pts(a,v); FB=facet_pts(c,v)
                FA=FA[(FA[:,a]<0)&(FA[:,b]>0)]; FB=FB[(FB[:,b]<0)&(FB[:,a]>0)]
                CA=np.array([cvec(a,h,x) for h in FA]); CB=np.array([cvec(c,h,x) for h in FB])
                fail=False
                for s in [1e-3,1e-2,5e-2]:
                    q0=s*E[a]+(1-s)*E[b]
                    okA=FA[(CA@q0)>0]; okB=FB[(CB@q0)>0]
                    if len(okA) and len(okB):
                        # ratio condition A_b B_a < |A_a||B_b| for some pair
                        rA=(okA[:,b]/np.abs(okA[:,a])).min(); rB=(np.abs(okB[:,b])/okB[:,a]).max()
                        if rA<rB: fail=True
                res.append(f"(a={a+1},b={b+1}):{'FAIL' if fail else 'ok'}")
        print(eps,name,' '.join(res))
