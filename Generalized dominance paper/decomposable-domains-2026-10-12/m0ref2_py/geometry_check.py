"""Second M0 referee: independent geometric checks (NUMERICS / exact where noted).
Run: python3 -I geometry_check.py
1. Facet structure of D_K for a polygon K: corner rays, crossings, sign patterns.
2. T1 (eps grid) and random all-facing triangles: two crossings per facet, corner rays
   in two-negative orthants, middle arcs one-negative (Lemma signs) -- the inputs of
   R.1 (corner portions), P4 Lemma 2.4(b)/Prop 4.1(ii) and Thm 4.3 (separation).
3. Normalised box (hexagon): which of these inputs fail (task 4).
4. R.1 inequalities at crossings; Thm 4.3 separation for corner-pattern chords.
5. R.2 hull of opposite sectors.  6. n = 2 (N26.1 target): no crossings.
"""
import numpy as np
rng = np.random.default_rng(20261014)
one = np.ones(3)

def hull_order(V):
    c = V.mean(0)
    # coordinates in 1^perp
    a = np.array([1, -1, 0]) / np.sqrt(2); b = np.array([1, 1, -2]) / np.sqrt(6)
    ang = np.arctan2((V - c) @ b, (V - c) @ a)
    return V[np.argsort(ang)]

def facets(V):
    """V: vertices of polygon K (in order). Facet F_v = {h: h.v=0, h.v'>=0}.
    Returns list of (v, r_prev, r_next)."""
    V = hull_order(V); m = len(V); out = []
    rays = []
    for i in range(m):
        v, w = V[i], V[(i + 1) % m]
        r = np.cross(v, w)
        others = [V[j] for j in range(m) if j not in (i, (i + 1) % m)]
        if np.mean([r @ o for o in others]) < 0: r = -r
        rays.append(r / np.abs(r).max())
    for i in range(m):
        out.append((V[i], rays[i - 1], rays[i]))
    return out

def PK(V, g):
    return min(v @ g for v in V)

def facet_info(V, v, r0, r1, N=4001):
    ts = np.linspace(0, 1, N)
    H = np.outer(1 - ts, r0) + np.outer(ts, r1)
    cross = []
    for c in range(3):
        a, b = r0[c], r1[c]
        if abs(a) < 1e-9: cross.append((c, 0.0))
        elif abs(b) < 1e-9: cross.append((c, 1.0))
        elif a * b < 0:
            t = a / (a - b); cross.append((c, t))
    return sorted(cross, key=lambda x: x[1])

def pattern(h):
    return ''.join('0' if abs(x) < 1e-9 else ('+' if x > 0 else '-') for x in h)

def analyse(V, label, verbose=True):
    F = facets(V)
    res = {'two_cross_all': True, 'corner_two_neg': True, 'middle_one_neg': True}
    lines = []
    for (v, r0, r1) in F:
        cr = facet_info(V, v, r0, r1)
        lines.append(f"  facet v={np.round(v,3)}: corner {pattern(r0)} -> {pattern(r1)}, crossings {[(c+1, round(t,3)) for c,t in cr]}")
        inner = [x for x in cr if 1e-9 < x[1] < 1 - 1e-9]
        res.setdefault('n_relint_crossings', []).append(len(inner))
        if len(inner) != 2: res['two_cross_all'] = False
        else:
            tm = 0.5 * (cr[0][1] + cr[1][1]); hm = (1 - tm) * r0 + tm * r1
            if (hm < 0).sum() != 1: res['middle_one_neg'] = False
        for r in (r0, r1):
            if not ((r < -1e-9).sum() == 2 and (r > 1e-9).sum() == 1): res['corner_two_neg'] = False
    if verbose:
        print(label); print('\n'.join(lines)); print('  ', res)
    return res, F

# ---- 2. T1 ----
print('=== T1 ===')
for eps in [0.02, 0.1, 0.3, 0.6, 0.9, 0.99]:
    c0 = (1 - eps) / 3
    V = np.array([c0 * one + eps * np.eye(3)[k] for k in range(3)])
    res, F = analyse(V, f'eps={eps}', verbose=(eps == 0.3))
    if eps != 0.3: print(f'eps={eps}', res)

# random all-facing triangles in general position
def allfacing(V):
    for k in range(3):
        i, j = [x for x in range(3) if x != k]
        A = np.column_stack([np.eye(3)[k], V[i], V[j]])
        coef = np.linalg.solve(A, V[k])
        if not (coef > 0).all(): return False
    return True
cnt = 0; bad = 0; tried = 0
while cnt < 2000 and tried < 200000:
    tried += 1
    V = rng.dirichlet(np.ones(3) * 3, size=3)
    if not allfacing(V): continue
    cnt += 1
    res, _ = analyse(V, '', verbose=False)
    if not all(v for k, v in res.items() if k != 'n_relint_crossings'): bad += 1
print(f'random all-facing triangles: {cnt}, failures of Lemma-signs structure: {bad}')

# ---- 3. normalised box (hexagon) ----
print('\n=== normalised box ===')
def box_vertices(l, u):
    pts = []
    import itertools
    # vertices of normalised box: normalise vertices of the box [l,u]
    for s in itertools.product([0, 1], repeat=3):
        a = np.where(np.array(s) == 1, u, l); pts.append(a / a.sum())
    pts = np.array(pts)
    # convex hull in 2D
    from scipy.spatial import ConvexHull
    P2 = pts[:, :2]; h = ConvexHull(P2)
    return pts[h.vertices]
for (l, u) in [(np.array([.2, .25, .3]), np.array([.4, .45, .5])),
               (np.array([.3, .3, .3]), np.array([.5, .5, .5]))]:
    V = box_vertices(l, u)
    analyse(V, f'box l={l}, u={u}: {len(V)} vertices')

# ---- 4. R.1 inequalities and Thm 4.3 separation (T1) ----
print('\n=== R.1 / Thm 4.3 checks on T1 ===')
fails = 0; sepfail = 0; tot = 0
for eps in np.linspace(0.02, 0.98, 25):
    c0 = (1 - eps) / 3
    V = np.array([c0 * one + eps * np.eye(3)[k] for k in range(3)])
    for (v, r0, r1) in facets(V):
        for (c, t) in facet_info(V, v, r0, r1):
            w = (1 - t) * r0 + t * r1
            for s in [1e-3, 1e-2, 1e-1]:
                g1 = w - s * (one - np.eye(3)[c]); g2 = w + s * (one - np.eye(3)[c])
                tot += 1
                if not (abs(g1[c]) < 1e-12 and PK(V, g1) < 0 and abs(g2[c]) < 1e-12 and PK(V, g2) > 0):
                    fails += 1
        # Thm 4.3: corner r1 (pattern two negatives k,j, positive o); middle arc positive at j,o
        for r in (r0, r1):
            o = int(np.argmax(r)); neg = [x for x in range(3) if r[x] < 0]
            cr = facet_info(V, v, r0, r1); tm = 0.5 * (cr[0][1] + cr[1][1]); hm = (1 - tm) * r0 + tm * r1
            k = int(np.argmin(hm))  # facet's negative world
            j = [x for x in neg if x != k][0]
            if not (hm[o] > 0 and hm[j] > 0): sepfail += 1
            # random corner-pattern normals b through random interior p: b.p = 0, sign(b) = sign(r)
            for _ in range(20):
                p = rng.dirichlet(np.ones(3) * 2)
                b = np.abs(rng.normal(size=3)) * np.sign(r)
                # adjust b_o so b.p = 0
                b[o] = -(b[neg[0]] * p[neg[0]] + b[neg[1]] * p[neg[1]]) / p[o]
                if not (np.sign(b) == np.sign(r)).all(): sepfail += 1; continue
                if not (b[o] > 0 and b[j] < 0): sepfail += 1   # e_o in H+, e_j in H-
print(f'R.1 constructions: {tot}, failures {fails};  Thm 4.3 separation failures: {sepfail}')

# ---- 5. R.2: hull of two opposite sectors meets the third ----
bad = 0
for _ in range(20000):
    n1, n2 = rng.normal(size=2), rng.normal(size=2)
    if abs(n1[0]*n2[1]-n1[1]*n2[0]) < 0.05*np.linalg.norm(n1)*np.linalg.norm(n2): continue
    def samp(s1, s2):
        while True:
            x = rng.normal(size=2)
            if np.sign(n1 @ x) == s1 and np.sign(n2 @ x) == s2: return x
    x, y = samp(1, -1), samp(-1, 1)
    ok = False
    for lam in np.linspace(0.01, 0.99, 99):
        z = lam * x + (1 - lam) * y
        if n1 @ z > 0 and n2 @ z > 0: ok = True; break
    if not ok:
        # try more pairs before declaring failure
        for _ in range(50):
            x, y = samp(1, -1), samp(-1, 1)
            for lam in np.linspace(0.01, 0.99, 99):
                z = lam * x + (1 - lam) * y
                if n1 @ z > 0 and n2 @ z > 0: ok = True; break
            if ok: break
    if not ok: bad += 1
print(f'R.2 sector-hull failures: {bad}')

# ---- 6. n = 2: N26.1 target K = {m_1 in [0.25, 0.625]} ----
for m1 in (0.25, 0.625):
    m = np.array([m1, 1 - m1]); h = np.array([m[1], -m[0]])
    print(f'n=2 boundary ray of D_K at m1={m1}: h ~ {np.round(h,3)}, zero coordinate: {bool((np.abs(h) < 1e-12).any())}')
