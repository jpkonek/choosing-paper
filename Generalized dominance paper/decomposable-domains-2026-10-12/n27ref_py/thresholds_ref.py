"""N27 referee: independent recomputation of the tie thresholds for T1 (evidence + symbolic check).

theta_x(T)   = min_{k, i in C_k} sup_{h in F_k\\0} h_i/||h||       (threshold for (X_ik) from facet points)
theta_x(T,U) = min_{k,i} sup{x_i/||x|| : x in U = D_{K'}, v_k.x < 0} (threshold read with U; K' = u + s(T-u))
Theta_NT     = corner-ray value (N7), not needed by N27.

Facet F_1 of T1: cone{r12, r31}, r12 = (-1,-1,k+1), r31 = (-1,k+1,-1); coordinates 2,3 cross.
"""
import numpy as np
import sympy as sp
from scipy.optimize import minimize

# ---------- symbolic: Euclidean sup of h_3/|h| on F_1 ----------
k, t = sp.symbols('kappa t', positive=True)
r12 = sp.Matrix([-1, -1, k + 1]); r31 = sp.Matrix([-1, k + 1, -1])
h = (1 - t) * r12 + t * r31
f2 = h[2]**2 / (h.T * h)[0]                      # (h_3/|h|)^2 where h_3 > 0
crit = sp.solve(sp.Eq(sp.diff(h[2] / sp.sqrt((h.T * h)[0]), t), 0), t)
print("stationary t:", [sp.simplify(c) for c in crit])
for c in crit:
    val = sp.simplify(f2.subs(t, c))
    print("  ratio^2 at stationary point:", sp.factor(val),
          "  equals (k^2+1)/(k^2+2)?", sp.simplify(val - (k**2 + 1) / (k**2 + 2)) == 0)
    print("  point (scaled):", sp.simplify((h.subs(t, c) / (-h.subs(t, c)[0])).T))
print("corner value^2 (t=0):", sp.simplify(f2.subs(t, 0)), " -> Theta_NT = (k+1)/sqrt((k+1)^2+2)")
print("theta_x^2 - 2/3 =", sp.factor((k**2 + 1) / (k**2 + 2) - sp.Rational(2, 3)), "(>0 iff k>1)")

# ---------- numerics ----------
def T1(eps):
    kap = (1 + 2 * eps) / (1 - eps)
    c0 = (1 - eps) / 3
    V = np.array([c0 + eps * np.eye(3)[i] for i in range(3)])
    return kap, V

def facet_sup(eps, kind, n=400001):
    kap, _ = T1(eps)
    a = np.array([-1, -1, kap + 1.]); b = np.array([-1, kap + 1, -1.])
    tt = np.linspace(0, 1, n)[:, None]
    H = (1 - tt) * a + tt * b
    nr = np.abs(H).max(1) if kind == 'sup' else np.linalg.norm(H, axis=1)
    r3 = H[:, 2] / nr; r2 = H[:, 1] / nr
    i3 = r3.argmax()
    return max(r3.max(), r2.max()), tt[i3, 0], (r3 >= 1 - 1e-12).mean()

def theta_xU(eps, s, kind='eucl', trials=60, seed=0):
    """sup x_3/||x|| over U=D_{K'} (K' = u+s(T1-u)) intersect {v_1.x < 0}. K' is eps' = s*eps contamination."""
    kap, V = T1(eps)
    ep = s * eps
    rng = np.random.default_rng(seed)
    cons = [{'type': 'ineq', 'fun': lambda x: -(V[0] @ x)}]
    for i in range(3):
        cons.append({'type': 'ineq', 'fun': lambda x, i=i: (1 - ep) / 3 * x.sum() + ep * x[i]})
    cons.append({'type': 'eq', 'fun': lambda x: x @ x - 1})
    best = -1
    for _ in range(trials):
        x0 = rng.normal(size=3); x0 /= np.linalg.norm(x0)
        res = minimize(lambda x: -x[2], x0, constraints=cons, method='SLSQP', options={'ftol': 1e-12, 'maxiter': 500})
        if res.success and all(c['fun'](res.x) > -1e-9 for c in cons[:-1]):
            best = max(best, res.x[2])
    return best

print("\n eps   kappa   thx_sup  (t*, sup-arc frac)   thx_eucl  closed    Theta_NT   thx(T,U) s=.9  s=.99")
for eps in [0.05, 0.1, 0.3, 0.6, 0.9]:
    kap, V = T1(eps)
    ts, _, arc = facet_sup(eps, 'sup')
    te, tstar, _ = facet_sup(eps, 'eucl')
    closed = np.sqrt((kap**2 + 1) / (kap**2 + 2))
    thnt = (kap + 1) / np.sqrt((kap + 1)**2 + 2)
    u9, u99 = theta_xU(eps, 0.9), theta_xU(eps, 0.99)
    print(f"{eps:4.2f} {kap:7.4f}  {ts:.6f}  (arc {arc:.3f})        {te:.6f}  {closed:.6f}  {thnt:.6f}   "
          f"{u9:.6f}  {u99:.6f}   t*={tstar:.4f} in (0,1)")

# membership of the claimed maximiser in relint F_k and its facet equations (N5 coordinates (i,j,k))
for eps in [0.05, 0.3, 0.9]:
    kap, V = T1(eps)
    x = np.array([-1.0, -1 / kap, kap + 1 / kap])   # world order (1,2,3) = (k,j,i) for F_1, i = 3
    print(f"eps={eps}: v.x = {V @ x}  (v_1.x = 0, others > 0 => relint F_1);  x_3/|x| = {x[2]/np.linalg.norm(x):.6f}")
