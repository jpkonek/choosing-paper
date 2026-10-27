"""Where do the envelope gaps occur?  For each admissible line Phi(Lam): which facets supply z1,z2,
and the gap.  q = u + r d."""
import numpy as np
from general import *
eps=0.3; S,x,kap=T1_system(eps,'+')
u=np.ones(3)/3; d=np.array([2,-1,-1.]); d/=np.linalg.norm(d); r=0.01; q=u+r*d
rows=[]
for th in np.linspace(0,np.pi*2,360,endpoint=False):
    cr,n=crossings(q,th)
    if len(cr)!=2: continue
    okk=True; info=[]; pts=[]
    for (i,j),s in cr:
        if not S.nonfail(i,j,s): okk=False;break
        o='j' if n@(E[j]-q)>0 else 'i'
        sz=S.inv(i,j,o,s); z=(1-sz)*E[i]+sz*E[j]; pts.append(z)
        # which facet's tangent was used
        ks=[k for k,h in S.tangents(z) if ((o=='j' and h[j]>0>h[i]) or (o=='i' and h[i]>0>h[j]))]
        info.append((f"e{i+1}e{j+1}",round(s,3),o,ks[0]+1))
    if not okk: continue
    g=np.cross(pts[0],pts[1]); plus=[k for k in range(3) if n@(E[k]-q)>0]
    if g@E[plus[0]]<0: g=-g
    rows.append((th,g/np.linalg.norm(g),info))
G=np.array([r_[1] for r_ in rows]); gp=gaps(G)
for (th,g,info),gg in zip(rows,gp):
    same = info[0][3]==info[1][3]
    print(f"th={th:.3f} facets {info[0][3]},{info[1][3]} {'SAME' if same else 'mixed'} gap/r={gg/r:+.4f}  {info}")
