"""Second-referee sanity checks for Thm TSalways and its satellites (NUMERICS only).

(1) Fact 4.0 by LP, all b, several eps; Fact 4.0' sign v_{k*}.w** > 0.
(2) b-crossing chords from PC data: both pass through u and e_b; strict orientation of e_a, e_c.
(3) x_+^2 > kappa and x_-^2 < 1/kappa (failing box at (1,2) for x_+, at (2,1) for x_-).
(4) Lemma signs on T1 facets (h_k < 0, sign patterns, crossings in order).
(5) Prop 5.1(=>) {+,-} conversion: strict signs and identical cells on random priors.
(6) Lemma 3.4 (surround): constant t_i >= (d - delta)/sqrt2 and conclusion p* in conv(Q_i).
(7) Prop 3.1 estimate |x - p*| <= delta(1 + 2/b) whenever n.(x - p*) > 0.
(8) Lemma 2.1 separating gamble: m.h = 0 < m0.h.
"""
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(20261014)
out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

def T1(eps):
    c0 = (1 - eps) / 3
    V = np.array([c0 * np.ones(3) + eps * np.eye(3)[k] for k in range(3)])
    kap = (1 + 2 * eps) / (1 - eps)
    return V, kap

def xpm(kap):
    s = np.sqrt((kap + 1) ** 2 - 4)
    return ((kap + 1) + s) / 2, ((kap + 1) - s) / 2

def ck(k, h, x):
    h1, h2, h3 = h
    if k == 0: return np.array([-(x * h2 + h3), x * h2, h3])
    if k == 1: return np.array([h1, -(h1 + x * h3), x * h3])
    return np.array([x * h1, h2, -(x * h1 + h2)])

def crossing(k, b, kap):
    """gamble on F_k with h_b = 0, h_k = -1, third coordinate kappa"""
    h = np.zeros(3); h[k] = -1.0
    o = 3 - k - b; h[o] = kap
    return h

u = np.ones(3) / 3
E = np.eye(3)
eps_list = [0.05, 0.2, 0.3, 0.6, 0.9]

# (1)
worst = 0; minvw = np.inf
for eps in eps_list:
    V, kap = T1(eps)
    for b in range(3):
        others = [k for k in range(3) if k != b]
        wA = crossing(others[0], b, kap); wC = crossing(others[1], b, kap)
        for k, w in ((others[0], wA), (others[1], wC)):
            assert abs(w @ V[k]) < 1e-12 and all(w @ V[j] > 0 for j in range(3) if j != k)
        cobj = E[b].copy()  # minimise m_b  <=> maximise 1 - m_b
        res = linprog(cobj, A_ub=np.vstack([wA, wC]), b_ub=[0, 0],
                      A_eq=np.ones((1, 3)), b_eq=[1], bounds=[(0, None)] * 3)
        worst = max(worst, 1 - res.fun)
        minvw = min(minvw, V[others[0]] @ wC, V[others[1]] @ wA)
P("(1) Fact 4.0: max(1 - m_b) over {m.w'<=0, m.w<=0} =", f"{worst:.2e}", "; min v_k*.w** =", f"{minvw:.4f}")

# (2)
viol = 0; cnt = 0
for eps in eps_list:
    V, kap = T1(eps)
    for x in xpm(kap):
        for b in range(3):
            for k in range(3):
                if k == b: continue
                w = crossing(k, b, kap); c = ck(k, w, x); o = 3 - k - b
                cnt += 1
                ok = abs(c @ u) < 1e-12 and abs(c @ E[b]) < 1e-12 and c @ E[k] < 0 < c @ E[o]
                viol += (not ok)
P("(2) b-crossing chords = line(u,e_b), e_k strictly negative, other vertex strictly positive:", f"{viol}/{cnt} violations")

# (3)
for eps in eps_list:
    V, kap = T1(eps); xp, xm = xpm(kap)
    P(f"(3) eps={eps}: x+^2/kappa = {xp**2/kap:.4f} (>1), x-^2*kappa = {xm**2*kap:.4f} (<1), x+ + 1/x+ - kappa - 1 = {xp+1/xp-kap-1:.1e}")

# (4)
viol = 0
for eps in eps_list:
    V, kap = T1(eps)
    for k in range(3):
        i, j = [l for l in range(3) if l != k]
        r1 = np.cross(V[k], V[i]); r2 = np.cross(V[k], V[j])
        # orient so that the rays are in F_k (m.h >= 0 on T)
        if r1 @ V[j] < 0: r1 = -r1
        if r2 @ V[i] < 0: r2 = -r2
        for tau in np.linspace(1e-3, 1 - 1e-3, 999):
            h = (1 - tau) * r1 + tau * r2
            if not (h[k] < 0): viol += 1
            if (h[i] <= 0) and (h[j] <= 0): viol += 1
P("(4) Lemma signs on T1 facets (h_k<0; never h_i,h_j<=0 together):", f"{viol} violations")

# (5)
viol = 0
for _ in range(3000):
    g = rng.normal(size=3)
    if np.all(g > 0) or np.all(g < 0): continue
    d = np.sign(g) * rng.uniform(0.1, 2, 3)
    lam = rng.uniform(0.05, 0.95)
    e0 = 0.5 * min(lam, 1 - lam) * np.min(np.abs(d))
    c = lam * d + e0; cp = (lam - 1) * d + e0
    if not (np.all(np.sign(c) == np.sign(g)) and np.all(np.sign(cp) == -np.sign(g))): viol += 1
    Q = rng.dirichlet(np.ones(3), 200)
    W1 = (Q @ c > np.maximum(0, Q @ cp)); W2 = (Q @ cp > np.maximum(0, Q @ c))
    if np.any(W1 != (Q @ d > 0)) or np.any(W2 != (Q @ d < 0)): viol += 1
P("(5) {+,-} -> CF data: sign/cell violations", viol)

# (6)
Ebar = np.eye(3)
fails = 0; tfail = 0; trials = 0
for _ in range(3000):
    p = rng.dirichlet(3 * np.ones(3))
    d = rng.uniform(0.05, 0.3); delta = 0.02 * d
    Qs = []; ts = []
    for i in range(3):
        o = p + delta * (lambda z: z - z.mean())(rng.normal(size=3)) / 2
        v = Ebar[i] + delta * (np.ones(3) / 3 - Ebar[i]) * rng.uniform(0, 1)
        # Q: first point on [o,v] at distance >= d from p (a worst-case wall point)
        ts_ = np.linspace(0, 1, 4001)
        pts = o[None] + ts_[:, None] * (v - o)[None]
        dist = np.linalg.norm(pts - p, axis=1)
        idx = np.argmax(dist >= d)
        if dist[idx] < d: break
        Qs.append(pts[idx]); ts.append(ts_[idx])
    else:
        trials += 1
        if min(ts) < (d - delta) / np.sqrt(2) - 1e-3: tfail += 1
        A = np.vstack([np.array(Qs).T[:2], np.ones(3)])
        try:
            lamb = np.linalg.solve(A, np.append(p[:2], 1.0))
            if np.any(lamb < -1e-9): fails += 1
        except np.linalg.LinAlgError:
            fails += 1
P("(6) surround: trials", trials, "; conv failures", fails, "; t-bound failures", tfail)

# (7)
bad = 0
for _ in range(20000):
    p = rng.dirichlet(3 * np.ones(3))
    n = rng.normal(size=3); n -= n.mean(); n /= np.linalg.norm(n)
    b = rng.uniform(0.01, 0.5); delta = rng.uniform(1e-4, 0.05)
    o = p + delta * rng.uniform(0, 1) * (lambda z: z / np.linalg.norm(z))((lambda z: z - z.mean())(rng.normal(size=3)))
    # v with n.(v-p) = -b, |v - p| <= sqrt2
    t_ = rng.normal(size=3); t_ -= t_.mean(); t_ -= (t_ @ n) * n; t_ /= max(np.linalg.norm(t_), 1e-12)
    v = p - b * n + rng.uniform(-1, 1) * np.sqrt(max(2 - b * b, 0)) * t_
    for t in np.linspace(0, 1, 201):
        xx = (1 - t) * o + t * v
        if n @ (xx - p) > 0 and np.linalg.norm(xx - p) > delta * (1 + 2 / b) + 1e-12: bad += 1
P("(7) Prop 3.1 estimate violations:", bad)

# (8)
bad = 0
for _ in range(5000):
    m0, m = rng.dirichlet(np.ones(3), 2)
    h = (m0 - m) - ((m0 - m) @ m) * np.ones(3)
    if not (abs(m @ h) < 1e-12 and m0 @ h > 0): bad += 1
P("(8) Lemma 2.1 separating gamble failures:", bad)

open(__file__.replace('.py', '.out'), 'w').write("\n".join(out) + "\n")
