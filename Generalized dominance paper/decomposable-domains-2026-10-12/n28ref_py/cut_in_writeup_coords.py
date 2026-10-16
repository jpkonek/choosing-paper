"""R4-sec.9-type identity cuts, redone in the writeup's conventions (Prop T1: x+ fails the box at (a,b)=(1,2)).
Witness A=(-beta(1+eta), eta, 1) in relint F_1 near the 2-crossing; identity d-line {A.q=0}; alpha-line {c_1(A).q=0}.
Report apex position (phi measured from e_b=e2 toward e3; phi=0 is the failing edge [e2,e1]) and whether the
identity K_q={q} passes the global chord constraints along the d-face."""
import numpy as np, sys
sys.path.insert(0,'.')
from sector_caps2 import setup, cvec, viol, E
for eps in [0.2,0.3]:
    kap,v,xp=setup(eps); x=xp; beta=1/kap
    for eta in [0.02,0.005,0.001]:
        A=np.array([-beta*(1+eta),eta,1.0])
        assert abs(A@v[0])<1e-12
        c=cvec(0,A,x)
        apex=np.linalg.solve(np.vstack([c,A,np.ones(3)]),np.array([0,0,1.0]))
        # d-line meets edge [e2,e1] (q3=0) at:
        Ez=np.array([A[1],-A[0],0]); Ez/=Ez.sum()
        rel=apex-E[1]; phi=rel[2]/(rel[0]+rel[2])
        # sample d-face points (apex, Ez) and test identity admissibility
        ts=np.linspace(0.02,0.98,25)
        pts=[apex+t*(Ez-apex) for t in ts]
        okc=[not viol(p,p,v,x) for p in pts]
        print(f"eps={eps} eta={eta}: apex={np.round(apex,5)} in Delta:{bool(apex.min()>0)} |apex-e2|/eta={np.linalg.norm(apex-E[1])/eta:.2f} phi(apex)={phi:.3f};"
              f" alpha(apex)>0 side? d-face endpoint on [e2,e1] at q1={Ez[0]:.2e}; identity admissible at {sum(okc)}/{len(okc)} d-face points")
