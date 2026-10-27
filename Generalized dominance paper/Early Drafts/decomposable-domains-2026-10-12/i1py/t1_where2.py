import numpy as np
from general import *
eps=0.3; S,x,kap=T1_system(eps,'+')
u=np.ones(3)/3; d=np.array([2,-1,-1.]); d/=np.linalg.norm(d); r=0.01; q=u+r*d
fam={1:[],2:[],3:[]}
for th in np.linspace(0,np.pi*2,720,endpoint=False):
    cr,n=crossings(q,th)
    if len(cr)!=2: continue
    okk=True; ks=[]; pts=[]
    for (i,j),s in cr:
        if not S.nonfail(i,j,s): okk=False;break
        o='j' if n@(E[j]-q)>0 else 'i'
        sz=S.inv(i,j,o,s); z=(1-sz)*E[i]+sz*E[j]; pts.append(z)
        ks.append([k for k,h in S.tangents(z) if ((o=='j' and h[j]>0>h[i]) or (o=='i' and h[i]>0>h[j]))][0]+1)
    if not okk or ks[0]!=ks[1]: continue
    g=np.cross(pts[0],pts[1]); plus=[k for k in range(3) if n@(E[k]-q)>0]
    if g@E[plus[0]]<0: g=-g
    fam[ks[0]].append((th,g/np.linalg.norm(g)))
for k in fam:
    G=np.array([g for th,g in fam[k]]); gp=gaps(G)
    print(f"facet {k} alone: n={len(G)} max gap/r={np.nanmax(gp)/r:.4f}")
    # first-order: offsets of the lines relative to v_k: g.v_k (normalised so that g restricted to aff has unit normal)
    vk=S.V[k-1]
    offs=[]
    for th,g in fam[k]:
        gn=g-g.mean()            # normal in 1-perp
        offs.append((th,(g@vk)/np.linalg.norm(gn)/r))
    o=np.array(offs)
    print("   theta range",o[0,0].round(3),o[-1,0].round(3)," offset at v_k /r: ",np.round(o[::max(1,len(o)//8),1],4))
allG=np.array([g for k in fam for th,g in fam[k]]); gp=gaps(allG); print("all three:",np.nanmax(gp)/r)
