import numpy as np, sys, time
from dcf import DCF, PT
from families import gambles, priors
eps=float(sys.argv[1]); tag=sys.argv[2]
F,tags,v=gambles(eps,taus=(0.3,0.7),shifts=(-0.01,0.01),box=True,crossings=True)
G=priors(rings=(0.05,),nring=4,vert=(0.03,),nvert=2,chords=(0.5,),edges=False)
print("eps",eps,"ng",len(F),"nq",len(G),flush=True)
fixed={0:np.array([1 if PT(g,v)>0 else (-1 if PT(-g,v)>0 else 0) for g in F])}
D=DCF(G,F,fixed)
t=time.time()
Z,res=D.run(rounds=300,time_limit=900,log=lambda s: print(s, round(time.time()-t,1), flush=True))
print("done; time",time.time()-t, flush=True)
if Z is not None:
    np.save(f'run2_{tag}_Z.npy',Z); np.save(f'run2_{tag}_G.npy',G); np.save(f'run2_{tag}_F.npy',F)
    import pickle; pickle.dump(D.clauses,open(f'run2_{tag}_clauses.pkl','wb'))
