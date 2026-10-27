# NUMERICS (sanity only) for P4 Lemmas 2.4-2.6: shells between D_K and D_{T1}.
# (a'')  K strictly inside T1  => shell D_K \ D_T1 meets >= 3 open orthants, and contains
#        points arbitrarily close to {g_c = 0} on both sides near a crossing.
# (b'')  K strictly containing T1 with shell in ONE orthant => that orthant is a corner pattern.
# (c)    -sigma of a corner pattern is a middle pattern (so +-sigma are never both corner).
# (d)    a chord through u whose normal b has a corner pattern cuts off the odd vertex.
import numpy as np
rng = np.random.default_rng(1)
eps = 0.3; c0 = (1-eps)/3
V = np.array([c0*np.ones(3)+eps*np.eye(3)[k] for k in range(3)])
u = np.ones(3)/3
s = 0.6; Kp = u + s*(V-u)          # K' vertices
def P(Kpts, g):                    # lower prevision of polytope with vertex list Kpts
    return np.min(Kpts @ g, axis=-1) if g.ndim == 1 else np.min(g @ Kpts.T, axis=1)
def pat(g): return ''.join('+' if x > 0 else '-' for x in g)
def cr(a, b):
    x = np.cross(V[a], V[b]); o = 3-a-b
    return x if x @ V[o] > 0 else -x
corner = {pat(cr(0,1)), pat(cr(1,2)), pat(cr(2,0))}
print('corner patterns', sorted(corner))
neg = lambda p: ''.join('+' if ch == '-' else '-' for ch in p)
print('(c) -corner are', sorted(neg(p) for p in corner), 'none corner:',
      all(neg(p) not in corner for p in corner))
G = rng.normal(size=(400000, 3))
PT = P(V, G); PKp = P(Kp, G)
inU = PKp > 0
# (a'')
bad_a = 0
for trial in range(200):
    k = rng.integers(3)
    w = rng.dirichlet(np.ones(3), size=4)
    pts = w @ V
    pts = np.vstack([pts, Kp])
    # drop vertex k: keep points inside T1 but strictly away from v_k
    pts = pts[np.linalg.norm(pts-V[k], axis=1) > 0.02]
    K = np.vstack([pts, Kp])
    PK = P(K, G)
    sh = inU & (PK > 0) & (PT <= 0)
    pats = set(pat(g) for g in G[sh])
    if len(pats) < 3: bad_a += 1
print('(a\'\') trials with <3 patterns in shell:', bad_a, 'of 200')
# (b'')
single = {}; total = 0
for trial in range(3000):
    d = rng.normal(size=3); d -= d.mean(); d /= np.linalg.norm(d)
    m = V.mean(0) + rng.uniform(0.05, 0.6)*d
    if np.any(m <= 0): continue
    x = np.linalg.solve(V.T, m)
    if np.all(x > 0): continue                    # m inside T1: skip
    K = np.vstack([V, m[None, :]])
    PK = P(K, G)
    sh = inU & (PT > 0) & (PK <= 0)
    if sh.sum() < 50: continue
    pats = set(pat(g) for g in G[sh]); total += 1
    if len(pats) == 1:
        p = pats.pop(); single[p] = single.get(p, 0) + 1
print('(b\'\') shells in a single orthant, by pattern:', single, 'of', total,
      '; all corner:', all(p in corner for p in single))
# (d)
okd = True
for p in corner:
    sg = np.array([1 if ch == '+' else -1 for ch in p])
    for t in range(200):
        b = sg*rng.uniform(0.1, 2, 3)
        # project so that u.b = 0 (chord through u), keeping the sign pattern if possible
        b = b - (b @ u)/(np.abs(sg) @ u) * np.where(sg > 0, 1, 1)*0
        b = b - (b.sum()/3)
        if pat(b) != p: continue
        odd = int(np.where(sg == (1 if p.count('+') == 1 else -1))[0][0])
        sides = np.sign(np.eye(3) @ b)
        if not (sides[odd] != sides[(odd+1) % 3] == sides[(odd+2) % 3]): okd = False
print('(d) chords through u with corner-pattern normal cut off the odd vertex:', okd)
