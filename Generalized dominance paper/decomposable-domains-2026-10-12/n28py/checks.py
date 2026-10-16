"""N28 sanity checks.  Run:  python3 checks.py > checks.out
All checks are NUMERICS / exact-arithmetic sanity checks of statements proved by hand in N28_notes.md.
No theorem in N28 depends on them.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.optimize import linprog

rng = np.random.default_rng(28)
E = np.eye(3)
u = np.ones(3) / 3


def t1(eps):
    kap = (1 + 2 * eps) / (1 - eps)
    c0 = (1 - eps) / 3
    v = [c0 * np.ones(3) + eps * E[k] for k in range(3)]
    return kap, c0, v


def crossing(i, k, kap):
    """crossing of coordinate i on facet F_k of D_{T1}: w_k=-1, w_i=0, w_j=kappa (j third)."""
    j = 3 - i - k
    w = np.zeros(3)
    w[k] = -1.0
    w[j] = kap
    return w


# ---------------------------------------------------------------------------------------------
print("(1) T1 geometry at the two b-crossings (exact for eps=3/10 with sympy; float for others)")
e = sp.Rational(3, 10)
K = (1 + 2 * e) / (1 - e)
c0 = (1 - e) / 3
vs = [sp.Matrix([c0 + (e if l == k else 0) for l in range(3)]) for k in range(3)]
for k in range(3):
    for i in range(3):
        if i == k:
            continue
        j = 3 - i - k
        w = sp.Matrix([0, 0, 0]); w[k] = -1; w[j] = K
        assert sp.simplify(w.dot(vs[k])) == 0           # on the plane v_k^perp
        assert sp.simplify(w.dot(vs[i])) > 0 and sp.simplify(w.dot(vs[j])) > 0   # relint F_k
print("   exact: every w_ik lies in relint F_k (w.v_k = 0, w.v_i, w.v_j > 0)")
for eps in [0.05, 0.3, 0.6, 0.9]:
    kap, c0f, v = t1(eps)
    worst_lp, worst_pos = 0.0, np.inf
    for b in range(3):
        a, c = [l for l in range(3) if l != b]
        wp = crossing(b, a, kap)   # b-crossing on F_a  (w'_a<0<w'_c)
        w = crossing(b, c, kap)    # b-crossing on F_c  (w_c<0<w_a)
        # LP: maximise 1-m_b over m in Delta with m.w' <= 0, m.w <= 0
        cobj = np.zeros(3); cobj[b] = 1.0              # minimise m_b  <=> maximise 1-m_b
        res = linprog(cobj, A_ub=np.vstack([wp, w]), b_ub=[0, 0], A_eq=np.ones((1, 3)), b_eq=[1],
                      bounds=[(0, None)] * 3, method="highs")
        worst_lp = max(worst_lp, 1 - res.fun)
        # v_{k*}.w** > 0 in both cases (k*=a, w**=w ; k*=c, w**=w')
        worst_pos = min(worst_pos, v[a] @ w, v[c] @ wp)
    print(f"   eps={eps}: max_b max{{1-m_b : m in Delta, m.w'<=0, m.w<=0}} = {worst_lp:.2e} (0 <=> only e_b);"
          f"  min v_k*.w** = {worst_pos:.4f} (>0)")

# ---------------------------------------------------------------------------------------------
print("\n(2) Chord orientations from the (PC) facet maps of T1 at p*=u, both corner solutions x+-")


def cvec(k, h, x):
    h1, h2, h3 = h
    if k == 0:
        return np.array([-(x * h2 + h3), x * h2, h3])
    if k == 1:
        return np.array([h1, -(h1 + x * h3), x * h3])
    return np.array([x * h1, h2, -(x * h1 + h2)])


bad = 0
for eps in [0.05, 0.3, 0.6, 0.9]:
    kap, _, _ = t1(eps)
    for xs in [+1, -1]:
        xp = ((kap + 1) + np.sqrt((kap + 1) ** 2 - 4)) / 2
        x = xp if xs > 0 else 1 / xp
        for b in range(3):
            for k in range(3):
                if k == b:
                    continue
                j = 3 - b - k
                w = crossing(b, k, kap)
                cv = cvec(k, w, x)
                ok = abs(cv @ u) < 1e-12 and abs(cv @ E[b]) < 1e-12 and cv @ E[k] < 0 < cv @ E[j]
                bad += (not ok)
print(f"   chord of every b-crossing on F_k passes through u and e_b, with e_k on the negative and e_third on the"
      f" positive side: violations = {bad} / 48")

# ---------------------------------------------------------------------------------------------
print("\n(3) Precise caps on the crossing chord near e_b violate the chord constraint")
kap, _, v = t1(0.2)          # R4 section 9 used eps = 0.2
for b in range(3):
    a, c = [l for l in range(3) if l != b]
    wp, w = crossing(b, a, kap), crossing(b, c, kap)
    ts = np.linspace(1e-4, 0.5, 200)
    q = E[b][None, :] + ts[:, None] * (u - E[b])[None, :]
    ident = np.minimum(q @ wp, q @ w)   # identity cap K_q={q}: need BOTH <= 0
    viol_diag = 0
    for _ in range(2000):
        D = np.exp(rng.normal(size=3) * 2)
        s = (q * D) / (q * D).sum(1, keepdims=True)
        viol_diag += np.sum((s @ wp <= 0) & (s @ w <= 0))
    print(f"   b={b+1}: identity cap: min_t max(q.w', q.w) = {np.max(np.vstack([q@wp, q@w]),0).min():.3e} > 0,"
          f"  i.e. P(q,w')>0 or P(q,w)>0 everywhere on the chord;  diagonal-projective caps with both <= 0: {viol_diag}")

# ---------------------------------------------------------------------------------------------
print("\n(4) Surround lemma: o_i within delta of p*, v_i within delta of e_i, Q_i on [o_i,v_i] with |Q_i-p*|>=d")


def in_conv2(p, Q):
    # barycentric test in the plane aff Delta (use first two coordinates)
    A = np.array([[Q[0][0] - Q[2][0], Q[1][0] - Q[2][0]], [Q[0][1] - Q[2][1], Q[1][1] - Q[2][1]]])
    try:
        lam = np.linalg.solve(A, p[:2] - Q[2][:2])
    except np.linalg.LinAlgError:
        return False
    return lam.min() >= -1e-12 and lam.sum() <= 1 + 1e-12


def rand_simplex_near(x, r):
    while True:
        y = x + rng.normal(size=3) * r
        y -= (y.sum() - 1) / 3
        if y.min() > 0 and np.linalg.norm(y - x) < r:
            return y


for ratio in [0.02, 0.1, 0.5, 0.9]:
    fails, trials = 0, 3000
    for _ in range(trials):
        p = rng.dirichlet([3, 3, 3])
        dist_b = min(np.linalg.norm(p - E[i]) for i in range(3))
        d = 0.5 * dist_b * rng.uniform(0.2, 1)
        delta = ratio * d
        Qs = []
        for i in range(3):
            o = rand_simplex_near(p, delta)
            vv = rand_simplex_near(E[i], delta) if delta < 1 else E[i]
            # pick a point on [o,vv] at distance >= d from p (random t beyond the first such point)
            ts = np.linspace(0, 1, 2001)
            pts = o[None, :] + ts[:, None] * (vv - o)[None, :]
            far = np.where(np.linalg.norm(pts - p, axis=1) >= d)[0]
            Qs.append(pts[rng.choice(far)] if len(far) else pts[-1])
        fails += not in_conv2(p, Qs)
    print(f"   delta/d = {ratio}: p* not in conv(Q_1,Q_2,Q_3) in {fails}/{trials} trials")

# ---------------------------------------------------------------------------------------------
print("\n(5) Wall-vs-half-plane estimate (Prop 3.1): points of [o,v] in H+ lie within C*|o-p*| of p*")
worst = 0.0
for _ in range(20000):
    p = rng.dirichlet([3, 3, 3])
    l = rng.integers(3)
    # random unit normal n in 1^perp with n.(e_l - p) <= 0
    while True:
        n = rng.normal(size=3); n -= n.mean(); n /= np.linalg.norm(n)
        if n @ (E[l] - p) <= 0:
            break
    vv = None
    for _k in range(200):
        cand = rand_simplex_near(E[l], 0.05)
        if n @ (cand - p) < -1e-3:
            vv = cand; break
    if vv is None:
        continue
    b = -(n @ (vv - p))
    dlt = 10 ** rng.uniform(-6, -2)
    o = rand_simplex_near(p, dlt)
    ts = np.linspace(0, 1, 4001)
    pts = o[None, :] + ts[:, None] * (vv - o)[None, :]
    inH = pts[(pts - p) @ n > 0]
    if len(inH):
        r = np.linalg.norm(inH - p, axis=1).max() / (np.linalg.norm(o - p) * (1 + 2 / b))
        worst = max(worst, r)
print(f"   max over trials of  dist(x,p*) / (|o-p*| (1+2/b))  for x in [o,v] with n.(x-p*)>0 : {worst:.3f} (<= 1)")

# ---------------------------------------------------------------------------------------------
print("\n(6) Quasi-concavity sanity (N21.1) in a genuine realisation: hexagon gauge mixture (R10a Thm M)")
# M_i = conv{e_i, u}; F_p(g) = sum_i p_i min(g_i, u.g) ; P(p,g) = F_p(g) / (1.S_p) with 1.S_p = 1 (all M_i in Delta)
# K_p = nu(sum p_i M_i) ; vertices: choose e_i or u for each i
verts = list(itertools.product([0, 1], repeat=3))


def Kverts(p):
    out = []
    for ch in verts:
        s = sum(p[i] * (E[i] if ch[i] == 0 else u) for i in range(3))
        out.append(s / s.sum())
    return np.array(out)


def P(p, g):
    return (Kverts(p) @ g).min()


viol = 0
for _ in range(4000):
    g = rng.normal(size=3)
    a_, b_ = rng.dirichlet([1, 1, 1]), rng.dirichlet([1, 1, 1])
    lam = rng.uniform()
    m = (1 - lam) * a_ + lam * b_
    viol += P(m, g) < min(P(a_, g), P(b_, g)) - 1e-12
print(f"   quasi-concavity violations along random segments: {viol}/4000")
# Z_{e_b} empty and C_b = Omega in this system (no interior K_p contains a vertex)
mx = max(Kverts(rng.dirichlet([1, 1, 1]))[:, b].max() for _ in range(2000) for b in range(3))
print(f"   max over 2000 interior priors of max_K m_b = {mx:.4f} (<1: no interior credal set contains a vertex)")
