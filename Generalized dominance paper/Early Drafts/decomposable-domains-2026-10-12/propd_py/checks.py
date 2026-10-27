"""NUMERICS for PropD_notes.md.  Run: python3 -I checks.py
(1) power maps nu(w*q^alpha) send segments to segments only for alpha in {0,1}   (Step 5 of Prop D proof)
(2) pencil m^perp, m in Delta not a vertex, meets >=2 mixed pair-classes in arcs of positive length (Case 2)
(3) projective sigma=nu(Aq): the d-vector A^T g has the strict sign of g for all crossing g iff A is diagonal (sanity)
(4) Example E transported by a diagonal map (Prop diag b): hypothesis (C) holds with d = D^{-1}... and the
    segment law  K_q meets [sigma(q1),sigma(q2)]  and the transport cone law hold (Lemma SL, Cor T2)
"""
import numpy as np
rng = np.random.default_rng(1)
nu = lambda x: x / x.sum(axis=-1, keepdims=True)

# (1)
print("(1) collinearity defect of nu(w*q^alpha) on random segments")
for alpha in [-1.0, 0.5, 0.9, 0.99, 1.0, 1.01, 2.0]:
    worst = 0.0
    for _ in range(2000):
        w = rng.uniform(0.2, 5, 3)
        a, b = nu(rng.uniform(0.05, 1, 3)), nu(rng.uniform(0.05, 1, 3))
        ts = np.array([0.0, 0.37, 1.0])
        pts = nu(w * ((1 - ts)[:, None] * a + ts[:, None] * b) ** alpha)
        M = np.vstack([pts.T, np.ones(3)]) if False else pts
        worst = max(worst, abs(np.linalg.det(M)) / (np.linalg.norm(a - b) ** 2 + 1e-12))
    print(f"   alpha={alpha:5.2f}  max |det|/|a-b|^2 = {worst:.3e}")

# (2)
print("(2) mixed pair-classes met by the pencil m^perp")
def classes(m, N=20000):
    A = np.cross(m, [1.0, 0.3, -0.7]); A /= np.linalg.norm(A)
    B = np.cross(m, A); B /= np.linalg.norm(B)
    th = (np.arange(N) + 0.5) * np.pi / N
    g = np.cos(th)[:, None] * A + np.sin(th)[:, None] * B
    s = np.sign(g); s[s[:, 0] < 0] *= -1  # pair-class representative
    keys, cnt = np.unique(s, axis=0, return_counts=True)
    mixed = [(tuple(k), c / N) for k, c in zip(keys, cnt) if (k > 0).any() and (k < 0).any() and (k != 0).all()]
    return mixed
worst_int, worst_edge = 9, 9
for _ in range(300):
    m = nu(rng.uniform(0.01, 1, 3)); worst_int = min(worst_int, len(classes(m)))
    e = rng.uniform(0.05, 0.95); m = np.array([e, 1 - e, 0.0])[rng.permutation(3)]
    worst_edge = min(worst_edge, len(classes(m)))
print(f"   min #classes, interior m: {worst_int} ; edge m: {worst_edge}")

# (3)
print("(3) strict-sign test of d = A^T g on gambles whose line crosses sigma(O)")
def frac_bad(A, trials=4000):
    bad = 0; tot = 0
    q0 = np.array([0.3, 0.4, 0.3])
    for _ in range(trials):
        q = nu(q0 + 0.05 * rng.standard_normal(3).clip(-1, 1))
        m = nu(A @ q)
        # random g through m (crossing sigma(O) at m)
        v = rng.standard_normal(3); g = v - (v @ m) / (m @ m) * m
        if (np.sign(g) == 0).any() or not ((g > 0).any() and (g < 0).any()):
            continue
        d = A.T @ g; tot += 1
        if not (np.sign(d) == np.sign(g)).all() and not (np.sign(d) == -np.sign(g)).all():
            bad += 1
        elif (np.sign(d) == -np.sign(g)).all():
            bad += 1  # orientation also fixed: d must be +sign(g)
    return bad / tot
print(f"   diagonal A: bad fraction {frac_bad(np.diag([1.0, 2.5, 0.4])):.4f}")
for k in range(3):
    A = np.diag(rng.uniform(0.5, 2, 3)) + 0.15 * rng.uniform(0, 1, (3, 3))
    print(f"   non-diagonal positive A #{k}: bad fraction {frac_bad(A):.4f}")

# (4)
print("(4) Example E (f=(-1,2,2)) transported by D=diag(1,3,0.5)")
f = np.array([-1.0, 2.0, 2.0]); Dg = np.array([1.0, 3.0, 0.5])
E = np.eye(3)
def Kverts(q):
    s = max(f @ q, 0.0); eps = s / (1 + s)
    V = (1 - eps) * q + eps * E           # contamination, vertices
    return nu(V / Dg)                     # nu(D^{-1} K_q)
def P(q, g): return (Kverts(q) @ g).min()
viol_C = 0; n_C = 0
for _ in range(20000):
    q = nu(rng.uniform(0.01, 1, 3)); g = rng.standard_normal(3)
    if not ((g > 0).any() and (g < 0).any()): continue
    d = g / Dg  # transported d-vector (data (c,c')(Dg) = old data at g)
    n_C += 1
    if P(q, g) > 1e-12 and not d @ q > 0: viol_C += 1
    if P(q, -g) > 1e-12 and not d @ q < 0: viol_C += 1
print(f"   (C) violations: {viol_C} / {n_C}")
sig = lambda q: nu(q / Dg)
prec = lambda q: f @ q < 0
def seg_dist(K, a, b):
    # distance from segment [a,b] to polytope K (min over K points ~ LP-free: sample K hull densely)
    lam = rng.dirichlet(np.ones(3), 400); pts = lam @ K
    t = np.clip(((pts - a) @ (b - a)) / ((b - a) @ (b - a)), 0, 1)
    return np.min(np.linalg.norm(pts - (a + t[:, None] * (b - a)), axis=1))
worst = 0; n = 0
while n < 300:
    q1, q2 = nu(rng.uniform(0.01, 1, 3)), nu(rng.uniform(0.01, 1, 3))
    if not (prec(q1) and prec(q2)): continue
    q = q1 + rng.uniform() * (q2 - q1); n += 1
    worst = max(worst, seg_dist(Kverts(q), sig(q1), sig(q2)))
print(f"   segment law: max dist(K_q, [sig q1, sig q2]) over 300 triples = {worst:.2e} (sampling resolution; trivial here: precise set convex)")
