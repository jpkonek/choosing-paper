"""PP76 anchor_num76 (NUMERICS): Prop 3.3.  B = C_{tau d3} (PP72's class-3 repairer of a class-3 fill of T),
anchor world 3 (T <=_3 B by guidance).  Neighbours q of u: on R3 (inside tau) and on R2.
Is B pointwise weakly 3-worse than C_q (guidance defence of C_q at world 3)?"""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib73copy import sample, advice, ranks
d3 = np.array([1., 1., -2.]); r2 = np.array([-1., 2., -1.])
G = sample(2_000_000, seed=763); nrm = np.linalg.norm(G, axis=1)
tau = 0.03
B = advice(G, np.exp(tau * d3)); rB = ranks(G, B)[:, 2]
for name, m in [('R3 s=0.01', 0.01 * d3), ('R3 s=0.002', 0.002 * d3), ('R2 s=0.01', 0.01 * r2), ('R2 s=0.002', 0.002 * r2), ('R2 s=0.0005', 0.0005 * r2)]:
    Cq = advice(G, np.exp(m)); rq = ranks(G, Cq)[:, 2]
    viol = rB < rq   # B strictly 3-better than C_q at g
    print(f'{name}: |g|-mass where B is strictly 3-better than C_q: {(nrm*viol).mean():.3e} (points {int(viol.sum())})')
