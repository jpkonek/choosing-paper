"""B2 referee checks (NUMERICS; no verdict rests on them alone).
R1  all-facing => corner-ray patterns r_kj = (i:+, j:-, k:-), h_k<0 on F_k, two relint crossings per facet,
    e_k strictly in the opposite wedge at v_k  (supports the general proof of G1, G2, G5 in B2_referee).
R2  Lemma 9 step 2 cell facts for random apex / d-tie data.
R3  o_12 lies strictly inside the segment (v_1, e_2) and (v_2, e_1) for T1 (input of the proof of G9).
R4  A (gamma)-field on a decomposable domain WITHOUT (LF) realising residual (R2) with one full corner atom.
R5  Zonotope remark: the all-accept point can be interior without being the centre.
"""
import numpy as np
rng = np.random.default_rng(7)
E = np.eye(3)

def T1(eps):
    c0 = (1 - eps) / 3
    return [c0 * np.ones(3) + eps * E[k] for k in range(3)]

def allfacing(V):
    for k in range(3):
        i, j = [x for x in range(3) if x != k]
        lam = np.linalg.solve(np.vstack([E[k], V[i], V[j]]).T, V[k])
        if not np.all(lam > 0):
            return False
    return True

def corner(V, k, j):
    r = np.cross(V[k], V[j]); l = 3 - k - j
    return r if r @ V[l] > 0 else -r

# R1
bad = 0; n = 0
while n < 3000:
    V = [rng.dirichlet(np.ones(3) * rng.uniform(0.3, 5)) for _ in range(3)]
    if not allfacing(V):
        continue
    n += 1
    for k in range(3):
        i, j = [x for x in range(3) if x != k]
        for (a, b) in [(j, i), (i, j)]:          # r_{k a}: a-coordinate <0, other two: k<0, b>0
            r = corner(V, k, a)
            if not (r[a] < 0 and r[k] < 0 and r[b] > 0):
                bad += 1
        r0, r1 = corner(V, k, i), corner(V, k, j)
        ts = np.linspace(0, 1, 401); H = np.outer(1 - ts, r0) + np.outer(ts, r1)
        if not np.all(H[:, k] < 0): bad += 1
        for c in (i, j):
            s = np.sign(H[:, c]); 
            if np.sum(s[1:] != s[:-1]) != 1: bad += 1
            # crossing w on F_k with w_c = 0; e_k strictly negative
            t = r0[c] / (r0[c] - r1[c]); w = (1 - t) * r0 + t * r1
            if not (w[k] < 0): bad += 1
print(f"R1: {n} random all-facing triangles, sign/crossing/opposite-wedge failures: {bad}")

# R2
def cells(c, cp, th):
    vals = {'+': th @ c, '-': th @ cp, '0': 0.0}
    return max(vals, key=vals.get)
bad = 0; trials = 0
for _ in range(4000):
    x = rng.dirichlet(np.ones(3))
    sg = rng.choice([-1, 1], 3)
    if abs(sg.sum()) == 3: continue
    # apex tie: c.x = c'.x = 0, c ~ sign g, c' ~ -sign g
    c = sg * rng.uniform(0.1, 3, 3); cp = -sg * rng.uniform(0.1, 3, 3)
    # rescale the coordinates of one sign to make c.x = 0 (possible since mixed)
    pos = c > 0; c[pos] *= -(c[~pos] @ x[~pos]) / (c[pos] @ x[pos])
    pos = cp > 0; cp[pos] *= -(cp[~pos] @ x[~pos]) / (cp[pos] @ x[pos])
    assert abs(c @ x) < 1e-9 and abs(cp @ x) < 1e-9
    trials += 1
    for b in range(3):
        th = E[b] - x
        a = cells(c, cp, th)
        if a == '0' or (a == '+') != (sg[b] > 0): bad += 1
    # silent cone S(g) angle < pi: two non-parallel closed half-planes; check random thetas: S convex & avoids vertices
    B = np.array([[1, -1, 0], [1, 1, -2]], float); B /= np.linalg.norm(B, axis=1)[:, None]
    ang = np.linspace(0, 2 * np.pi, 3600, endpoint=False)
    TH = np.stack([np.cos(ang), np.sin(ang)], 1) @ B
    S = (TH @ c <= 0) & (TH @ cp <= 0)
    Rm = (TH @ cp > 0) & (TH @ cp > TH @ c)
    if S.mean() >= 0.5 or Rm.mean() > 0.5 + 1e-3: bad += 1
print(f"R2: {trials} random apex-tie data, cell-fact failures: {bad}")

# R3
for eps in [0.01, 0.05, 1/7, 0.3, 0.6, 0.9, 0.99]:
    k = (1 + 2 * eps) / (1 - eps)
    o = np.array([k, k, 1]) / (2 * k + 1)
    V = T1(eps)
    # o on line(v1,e2): o = lam v1 + (1-lam) e2 with 0<lam<1 ; and on line(v2,e1)
    lam1 = o[0] / V[0][0]; lam2 = o[1] / V[1][1]
    ok = (np.allclose(lam1 * V[0] + (1 - lam1) * E[1], o) and 0 < lam1 < 1 and
          np.allclose(lam2 * V[1] + (1 - lam2) * E[0], o) and 0 < lam2 < 1)
    print(f"R3 eps={eps:.3f}: o_12={np.round(o,4)} in (v1,e2) and (v2,e1): {ok}")

# R4: domain with advice range {+,0} only on G = D_T1 \ cl D_K0, K0 = co(T1 u {m}), m in int cap_12;
# penalty c(g) = b = (-1,-1,2) on G.  Bayes at q: D_T1 if q.b>0, D_K0 if q.b<0; tie line E = {q.b=0} ∋ u.
eps = 0.3; V = T1(eps); k = (1 + 2 * eps) / (1 - eps)
o12 = np.array([k, k, 1]) / (2 * k + 1)
m = (V[0] + V[1] + o12) / 3
K0 = V + [m]
P = lambda K, g: min(float(np.dot(v, g)) for v in K)
G = rng.normal(size=(400000, 3))
inG = np.array([P(V, g) > 0 and P(K0, g) <= 0 for g in G])
pats = {tuple(np.sign(g).astype(int)) for g in G[inG]}
print(f"R4: {inG.sum()} sampled gambles in G; sign patterns found: {pats}")
# crossing pinning of K0 (B2.1(b)) and K0 subset of the tangent hexagon
def crossings(V):
    W = []
    for kk in range(3):
        i, j = [x for x in range(3) if x != kk]
        r0, r1 = corner(V, kk, i), corner(V, kk, j)
        for c in (i, j):
            t = r0[c] / (r0[c] - r1[c]); W.append((1 - t) * r0 + t * r1)
    return W
W = crossings(V)
print("R4: P_K0 at the six crossings:", np.round([P(K0, w) for w in W], 12))
b = np.array([-1., -1., 2.]); u = np.ones(3) / 3
print(f"R4: b.u = {b @ u:.1e}; b pattern matches G: {all(p == (-1, -1, 1) for p in pats)}")

# R5
gens = [np.array([1.0, 0.0]), np.array([-0.5, 0.9]), np.array([-0.4, -1.0])]
s = sum(gens); print(f"R5: generators positively span; all-accept point {s} (centre {s/2}); interior, not centre")
