"""Run DCF+ on a vertex-b-focused grid.  usage: run_plus.py eps tag [ngscale]"""
import numpy as np, sys, time, pickle
from dcf import setup, facet_h, corner, unit, mixed, E
from dcfplus import DCFPlus

eps = float(sys.argv[1]); tag = sys.argv[2]
kap, v, xp = setup(eps)
rng = np.random.default_rng(7)
u = np.ones(3) / 3
b, a, c = 1, 0, 2          # vertex e_2 ; failing edge [e_1,e_2] for x+
wp = np.array([-1.0, 0, kap]); w = np.array([kap, 0, -1.0])


def jit(g, s=1e-4):
    return unit(g) + s * rng.standard_normal(3)


F = []
for k in range(3):
    for tau in (0.2, 0.5, 0.8):
        h = unit(facet_h(k, tau, v))
        for t in (-0.02, 0.02):
            F.append(jit(h - t))
for dl in (-0.05, -0.01, 0.01, 0.05):       # gambles through the vertex region of e_b
    F.append(jit(wp + dl * E[b])); F.append(jit(w + dl * E[b]))
beta = 1 / kap
for (eta, zeta) in [(0.02, 0.05), (0.01, 0.03)]:
    F.append(jit(np.array([-beta * (1 + eta), eta, 1.0])))
    F.append(jit(np.array([1.0, -zeta, -beta * (1 - zeta)])))
for s in (0.05, 0.2):                          # near-vertex level gambles e_b - s
    F.append(jit(E[b] - s))
for _ in range(4):
    while True:
        g = rng.standard_normal(3)
        if mixed(g):
            break
    F.append(unit(g))
F = np.array([g for g in F if mixed(g)])

G = [u]
b1 = np.array([1, -1, 0]) / np.sqrt(2); b2 = np.array([1, 1, -2]) / np.sqrt(6)
for kk in range(4):
    ang = 2 * np.pi * (kk + 0.5) / 4
    G.append(u + 0.04 * (np.cos(ang) * b1 + np.sin(ang) * b2))
for t in (0.5, 0.8, 0.95):
    G.append((1 - t) * u + t * E[b])          # on lambda_b
for rho in (0.1, 0.03):
    for phi in (0.1, 0.3, 0.7, 0.9):
        q = E[b] + rho * ((1 - phi) * (E[a] - E[b]) + phi * (E[c] - E[b]))
        G.append(0.99 * q + 0.01 * u)
G = np.array(G)
print(f"eps={eps} x+={xp:.4f} ng={len(F)} nq={len(G)}", flush=True)
D = DCFPlus(eps, xp, G, F, ntau=10, pencil=(len(sys.argv) <= 4 or sys.argv[4] != 'nopencil'))
t0 = time.time(); D.build()
print("built", D.var, "vars", D.nrow, "rows", int(D.integ.sum()), "integer", round(time.time() - t0, 1), flush=True)
res = D.solve(time_limit=float(sys.argv[3]) if len(sys.argv) > 3 else 1800)
print("status", res.status, res.message, "time", round(time.time() - t0, 1), flush=True)
if res.x is not None:
    print("delta*", res.x[D.delta])
    Z = D.cells(res.x)
    pickle.dump(dict(F=F, G=G, Z=Z, x=res.x, K={qi: D.credal(res.x, qi) for qi in D.wit}), open(f'plus_{tag}.pkl', 'wb'))
