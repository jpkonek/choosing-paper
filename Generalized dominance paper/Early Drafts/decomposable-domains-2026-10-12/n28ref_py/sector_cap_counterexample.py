"""Referee counterexample to N28's inference 'the R4 sec.9 evidence no longer has support'.
For each eps, x in {x+,x-} and vertex b (failing edge a from failing_edge.py), the identity K_q={q} restricted to the
vertex sector S_b = {q = e_b + rho((1-phi)(e_a-e_b)+phi(e_c-e_b)) : phi <= phi_max} passes the GLOBAL chord
constraints (A) [N21.1'] and (B) [referee Lemma R1] for all three facets, and contains the identity cut d-faces of
box witnesses near the b-crossing of F_a (apex -> e_b, endpoint on the failing edge)."""
import numpy as np, sys
sys.path.insert(0,'.')
from sector_caps2 import setup, cvec, viol, E, corner
fail={'x+':{0:2,1:0,2:1},'x-':{0:1,1:2,2:0}}
for eps in [0.05,0.2,0.3,0.6,0.9]:
    kap,v,xp=setup(eps)
    for x,name in [(xp,'x+'),(1/xp,'x-')]:
        line=[]
        for b in range(3):
            a=fail[name][b]; c=3-a-b
            phis=np.linspace(0,0.6,601)
            pm=[]
            for rho in [1e-2,1e-4]:
                okk=np.array([not viol(q,q,v,x) for q in [E[b]+rho*((1-p)*(E[a]-E[b])+p*(E[c]-E[b])) for p in phis]])
                # largest phi such that all phi'<=phi are ok
                bad=np.where(~okk)[0]; pm.append(phis[bad[0]-1] if len(bad) else phis[-1])
            # identity cut witnesses: gambles on F_a near its b-crossing, slightly into h_b>0 (A-family)
            i,j=[l for l in range(3) if l!=a]
            r0,r1=corner(a,i,v),corner(a,j,v)
            ts=np.linspace(0,1,200001); H=(1-ts)[:,None]*r0+ts[:,None]*r1
            tb=ts[np.argmin(np.abs(H[:,b]))]
            ins=0; tot=0; apd=[]
            for dt in [1e-3,3e-4,1e-4]:
                for sgn in [+1,-1]:
                    A=(1-(tb+sgn*dt))*r0+(tb+sgn*dt)*r1
                    if not (A[a]<0<A[b]): continue
                    cA=cvec(a,A,x)
                    try: apex=np.linalg.solve(np.vstack([cA,A,np.ones(3)]),np.array([0,0,1.0]))
                    except np.linalg.LinAlgError: continue
                    Ez=np.zeros(3); Ez[b]=-A[a]; Ez[a]=A[b]; Ez/=Ez.sum()     # d-line on failing edge
                    if apex.min()<=0: continue
                    apd.append(np.linalg.norm(apex-E[b]))
                    for t in np.linspace(0.02,0.98,15):
                        p=apex+t*(Ez-apex); tot+=1; ins+= (not viol(p,p,v,x))
            line.append(f"e{b+1}(fail->e{a+1}): phi_max~{min(pm):.3f}; cut d-face pts admissible {ins}/{tot}; apex dist {min(apd) if apd else float('nan'):.1e}")
        print(f"eps={eps} {name}: "+" | ".join(line))
