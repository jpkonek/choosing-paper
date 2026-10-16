import numpy as np, sys, time
from dcf import DCF, PT
from families import gambles, priors
eps=float(sys.argv[1]) if len(sys.argv)>1 else 0.3
F,tags,v=gambles(eps,taus=(0.25,0.5,0.75),shifts=(-0.01,0.01),box=True)
G=priors(rings=(0.05,),nring=6,vert=(0.03,),nvert=3,chords=(0.5,),edges=True)
print("ng",len(F),"nq",len(G))
fixed={0:np.array([1 if PT(g,v)>0 else (-1 if PT(-g,v)>0 else 0) for g in F])}
print("target pattern counts",np.unique(fixed[0],return_counts=True))
D=DCF(G,F,fixed)
t=time.time(); Z,res=D.run(rounds=200,time_limit=600); print("time",time.time()-t)
if Z is not None:
    np.save('run1_Z.npy',Z)
