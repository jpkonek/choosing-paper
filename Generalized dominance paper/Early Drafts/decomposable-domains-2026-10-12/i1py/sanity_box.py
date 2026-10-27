"""Sanity check of Prop E and Thm R / envelope test on a GENUINE CF solution (normalized boxes)."""
import numpy as np
from general import *
lam=np.array([1.0,1.0,1.0]); eta=np.array([2.0,3.0,1.5]); p=np.array([0.3,0.3,0.4])
S,V=box_system(lam,eta,p)
print("target vertices:",len(V))
# 1. edge limit sets
for (i,j) in [(0,1),(1,2),(2,0)]:
    for s in [0.05,0.3,0.6,0.9]:
        q0=(1-s)*E[i]+s*E[j]
        K=box_K(lam,eta,q0)   # points on the edge
        sv=K[:,j]/(K[:,i]+K[:,j])
        Zj,Zi=S.Z(i,j,s)
        print(f"edge e{i+1}e{j+1} s={s}: predicted [{Zj:.5f},{Zi:.5f}]  actual [{sv.min():.5f},{sv.max():.5f}]")
# 2. envelope gaps at interior q and comparison with actual support values
for q in [p, np.array([.35,.3,.35]), np.array([.5,.3,.2]), np.array([.2,.6,.2]),np.array([.1,.1,.8])]:
    TH,G,gp,bad=envelope(S,q,nth=180)
    K=box_K(lam,eta,q)
    supp=np.array([ (K@g).min() for g in G])
    print(f"q={q}: lines={len(G)} signbad={bad} max LP gap={np.nanmax(gp):.2e}  max|min_K g.m| over lines={np.abs(supp).max():.2e}")
