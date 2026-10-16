"""Blow-up at e_b of the global chord constraints for PRECISE priors K_q={sigma} (writeup conventions, PC data
at p*=u).  Constraints, for all facets k and tau in (0,1):
   (A) sigma.h(tau)>0 => c_k(h(tau)).q>0      [N21.1': A_tau inside H+_tau]
   (B) c_k(h(tau)).q<0 => sigma.h(tau)<0      [referee strengthening: open H-_tau inside B_tau]
Prior q = e_b + rho*((1-phi)(e_a-e_b)+phi(e_c-e_b)) with e_a the FAILING edge (computed in failing_edge.py),
image sigma = e_b + rho*(z_a(e_a-e_b)+z_c(e_c-e_b)), z on a log grid.  phi=0: failing edge; phi=1/2: chord."""
import numpy as np, sys
sys.path.insert(0,'.')
from sector_caps2 import setup, viol, E
fail={'x+':{0:2,1:0,2:1},'x-':{0:1,1:2,2:0}}   # b -> a (0-based), from failing_edge.py
eps=float(sys.argv[1]) if len(sys.argv)>1 else 0.2
kap,v,xp=setup(eps)
rho=1e-7
PHIS=[float(p) for p in sys.argv[2].split(",")] if len(sys.argv)>2 else [0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.4,0.5,0.6,0.8,1.0]
g=np.concatenate([[0],np.geomspace(1e-3,1e3,90)])
for x,name in [(xp,'x+'),(1/xp,'x-')]:
  for b in range(3):
    a=fail[name][b]; c=3-a-b
    print(f"eps={eps} {name} vertex e{b+1}: failing edge toward e{a+1}")
    for phi in PHIS:
        q=E[b]+rho*((1-phi)*(E[a]-E[b])+phi*(E[c]-E[b]))
        adm=[(za,zc) for za in g for zc in g if (za>0 or zc>0) and not viol(E[b]+rho*(za*(E[a]-E[b])+zc*(E[c]-E[b])),q,v,x)]
        adm=np.array(adm)
        if len(adm):
            ang=adm[:,1]/(adm[:,0]+adm[:,1]); nm=adm.sum(1)
            print(f"   phi={phi:.2f}: {len(adm):5d} admissible; image phi in [{ang.min():.3f},{ang.max():.3f}]; |z|_1 in [{nm.min():.3g},{nm.max():.3g}]; identity admissible: {not viol(q,q,v,x)}")
        else:
            print(f"   phi={phi:.2f}: NO admissible precise image (identity admissible: {not viol(q,q,v,x)})")
    if b==0: pass
