"""Where do R4 sec.9's identity-cap cuts sit relative to the crossing chord lambda_1 = line(u,e1)?
lambda_1 = {q2 = q3}.  e1-cap, witness a(t) in F3 near the 1-crossing (0,kappa,-1)/kappa of F3."""
import numpy as np
eps = 0.2; kap = 1 + 3*eps/(1-eps); s = kap+1; x = (s+np.sqrt(s*s-4))/2
def M3(g): return np.array([g[0], x*g[1], -(g[0]+x*g[1])])
for t in [0.08,0.02,0.005,0.00125]:
    a = np.array([-t*x, 1.0, -(1-t*x)/kap])
    c = M3(a)
    A = np.linalg.solve(np.vstack([c, a, np.ones(3)]), np.array([0,0,1.0]))
    E = np.array([a[1], -a[0], 0]); E/=E.sum()
    # signed position relative to lambda_1: q2 - q3 (>0: e2 side, <0: e3 side); angle ratio r = min/max
    print(f"t={t}: apex A={np.round(A,6)}  A2-A3={A[1]-A[2]:+.3e}  (A2-A3)/|A-e1|={(A[1]-A[2])/np.linalg.norm(A-np.eye(3)[0]):+.3f}"
          f"  endpoint E on edge e1e2 (E2={E[1]:.2e})")
    # does the d-face segment (A,E) cross lambda_1?  sign change of q2-q3 along it
    print("     d-face crosses lambda_1:", np.sign(A[1]-A[2]) != np.sign(E[1]-E[2]))
# The F3 chord through u and e1 has which side for e2/e3?  M3 at crossing w=(0,kap,-1):
w = np.array([0,kap,-1.0]); cw = M3(w); print("F3 crossing chord vector", cw, " .u=", cw@np.ones(3)/3, " .e2=",cw[1]," .e3=",cw[2])
