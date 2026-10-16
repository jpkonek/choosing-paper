"""B2 geometric checks for T1 (NUMERICS / CHECKED support for B2_notes.md).

Checks, for several eps:
 G1  facet sign structure (Lemma signs): on F_k, h_k<0, two crossings, patterns.
 G2  six crossing lines = tangent lines from the vertices of Delta; each meets T1 only at one vertex.
 G3  hexagon W = {m in Delta: m.w >= 0 for the six crossings w} = T1 u three caps beyond the edges of T1;
     cap beyond [v_i,v_j] is the triangle (v_i, v_j, o_ij), o_ij = line(v_i,e_j) ^ line(v_j,e_i).
 G4  C_i = co(T1 u e_i) meets the boundary of Delta only at e_i; cap_ij subset C_i and C_j.
 G5  wedge W_i at v_i (T1-side of line(v_i,e_j), line(v_i,e_k)) has angle < pi, e_i strictly in the
     opposite wedge.
 G6  Step S8(c): on F_k (k != i) the corner portion with h_i>0 exists and P_{C_i}(h)=0 there.
 G7  Lemma L5 / L7 witnesses: g0 with g0_a=0, g0_c<0, P_T1(g0)>0; lines through e_j strictly separating e_i
     from co(T1 u m*) for m* in C_i\{e_i}.
 G8  Step S13/S17: a point m of cap_12 gives m.h<0 for facet gambles of F_1 near r_12; the corner
     pattern (-,-,+) chord through u separates e_3 from e_1,e_2; middle-arc gambles of F_1 are >0 at 2,3.
"""
import numpy as np
from itertools import permutations

rng = np.random.default_rng(0)
E = np.eye(3)


def T1_vertices(eps):
    c0 = (1 - eps) / 3
    return [c0 * np.ones(3) + eps * E[k] for k in range(3)]


def P(K, g):  # lower prevision of a polytope given by vertices
    return min(float(np.dot(m, g)) for m in K)


def Pbar(K, g):
    return max(float(np.dot(m, g)) for m in K)


def corner_rays(V):
    # r_kj propto v_k x v_j, oriented so that T1 is on the nonnegative side
    R = {}
    for k in range(3):
        for j in range(3):
            if k < j:
                r = np.cross(V[k], V[j])
                l = 3 - k - j
                if np.dot(r, V[l]) < 0:
                    r = -r
                R[(k, j)] = R[(j, k)] = r / np.linalg.norm(r)
    return R


def facet(V, k):
    """return the two corner rays bounding F_k (h.v_k=0, h.v_j>=0)."""
    R = corner_rays(V)
    others = [j for j in range(3) if j != k]
    return R[(k, others[0])], R[(k, others[1])]


def crossing(V, k, c):
    """crossing on F_k with h_c = 0 (c != k)."""
    r0, r1 = facet(V, k)
    # solve (1-t) r0 + t r1 has c-coordinate 0
    t = r0[c] / (r0[c] - r1[c])
    w = (1 - t) * r0 + t * r1
    return w / np.linalg.norm(w), t


def line_intersection(n1, n2):
    """intersection of {m: m.n1=0} and {m: m.n2=0} in aff Delta (m.1=1)."""
    A = np.vstack([n1, n2, np.ones(3)])
    return np.linalg.solve(A, np.array([0, 0, 1.0]))


def report(eps):
    out = []
    V = T1_vertices(eps)
    ok = True
    # G1
    for k in range(3):
        r0, r1 = facet(V, k)
        ts = np.linspace(0, 1, 2001)
        H = np.array([(1 - t) * r0 + t * r1 for t in ts])
        ok &= bool(np.all(H[:, k] < 0))
        for c in range(3):
            if c == k:
                continue
            s = np.sign(H[:, c])
            ok &= int(np.sum(s[1:] != s[:-1])) == 1
        ok &= all(abs(np.dot(h, V[k])) < 1e-12 for h in H)
    out.append(("G1 facet signs", ok))
    # G2
    ok = True
    W = {}
    for k in range(3):
        for c in range(3):
            if c == k:
                continue
            w, _ = crossing(V, k, c)
            W[(k, c)] = w
            ok &= abs(w[c]) < 1e-12 and abs(np.dot(w, V[k])) < 1e-12
            ok &= abs(np.dot(w, E[c])) < 1e-12  # line passes through e_c
            ok &= all(np.dot(w, V[j]) > 1e-9 for j in range(3) if j != k)
    out.append(("G2 crossings = tangent lines from vertices, touching T1 at one vertex", ok))
    # G3 hexagon: sample Delta, compare membership
    ok = True
    o = {}
    for i in range(3):
        for j in range(3):
            if i < j:
                # o_ij = line(v_i, e_j) ^ line(v_j, e_i): crossing on F_i with coordinate j, on F_j with i
                o[(i, j)] = line_intersection(W[(i, j)], W[(j, i)])
    pts = rng.dirichlet(np.ones(3), size=200000)
    inW = np.all(np.stack([pts @ W[key] >= -1e-12 for key in W], 1), 1)

    def in_tri(p, a, b, c):
        M = np.vstack([a, b, c]).T
        lam = np.linalg.solve(M, p.T).T
        return np.all(lam >= -1e-9, 1)

    inT = in_tri(pts, *V)
    caps = np.zeros(len(pts), bool)
    for (i, j), oo in o.items():
        caps |= in_tri(pts, V[i], V[j], oo)
    ok &= bool(np.all(inW == (inT | caps)))
    out.append(("G3 hexagon = T1 u 3 caps (200000 samples)", ok))
    # G4
    ok = True
    for i in range(3):
        # C_i = co(e_i, v_j, v_k) (v_i interior): boundary points of Delta in C_i
        others = [j for j in range(3) if j != i]
        Ci = [E[i], V[others[0]], V[others[1]]]
        lam = np.linalg.solve(np.vstack(Ci).T, V[i])
        ok &= bool(np.all(lam > 0))  # all-facing
        # exact boundary points of Delta: sample each edge densely
        bd = []
        for a in range(3):
            for b2 in range(a + 1, 3):
                for s_ in np.linspace(0, 1, 2001):
                    bd.append((1 - s_) * E[a] + s_ * E[b2])
        bd = np.array(bd)
        M = np.vstack(Ci).T
        lam_bd = np.linalg.solve(M, bd.T).T
        mem = np.all(lam_bd >= -1e-12, 1)
        ok &= bool(np.all(np.linalg.norm(bd[mem] - E[i], axis=1) < 1e-9))
        for j in others:
            key = (min(i, j), max(i, j))
            oo = o[key]
            capc = in_tri(np.vstack([oo, (V[i] + V[j] + oo) / 3]), *Ci)
            ok &= bool(np.all(capc))
    out.append(("G4 C_i meets bd Delta only at e_i; caps beyond edges at v_i lie in C_i", ok))
    # G5
    ok = True
    for i in range(3):
        j, k = [x for x in range(3) if x != i]
        n1, n2 = W[(i, j)], W[(i, k)]
        # opposite wedge: e_i negative for both
        ok &= np.dot(E[i], n1) < 0 and np.dot(E[i], n2) < 0
        # angle < pi: n1, n2 not antiparallel within 1^perp
        P1 = n1 - n1.mean()
        P2 = n2 - n2.mean()
        ok &= np.dot(P1, P2) / np.linalg.norm(P1) / np.linalg.norm(P2) > -1 + 1e-9
    out.append(("G5 wedges W_i pointed, e_i in opposite wedge", ok))
    # G6
    ok = True
    for i in range(3):
        Ci = [E[i]] + [V[j] for j in range(3) if j != i] + [V[i]]
        for k in range(3):
            if k == i:
                continue
            r0, r1 = facet(V, k)
            ts = np.linspace(0, 1, 4001)
            H = np.array([(1 - t) * r0 + t * r1 for t in ts])
            pos = H[:, i] > 1e-12
            vals = np.array([P(Ci, h) for h in H])
            ok &= bool(np.any(pos))
            ok &= bool(np.all(np.abs(vals[pos]) < 1e-12))
            # the positive set is an interval containing a corner end
            idx = np.where(pos)[0]
            ok &= (idx[0] == 0 or idx[-1] == len(ts) - 1)
    out.append(("G6 corner portion with h_i>0 on F_k, P_{C_i}=0 there", ok))
    # G7
    ok = True
    for c in range(3):
        for a in range(3):
            if a == c:
                continue
            b = 3 - a - c
            g0 = np.zeros(3)
            g0[c] = -1.0
            g0[b] = 1.0
            while P(V, g0) <= 0:
                g0[b] *= 2
            ok &= P(V, g0) > 0
    # L7 lines through e_j separating e_i from co(T1 u m*), m* random in C_i \ {e_i}
    for i in range(3):
        others = [j for j in range(3) if j != i]
        Ci = [E[i], V[others[0]], V[others[1]]]
        for trial in range(50):
            lam = rng.dirichlet(np.ones(3))
            lam[0] *= 0.95
            lam /= lam.sum()
            mstar = lam @ np.vstack(Ci)
            for j in others:
                kk = 3 - i - j
                found = False
                for s in np.linspace(1e-4, 0.5, 400):
                    y = (1 - s) * E[i] + s * E[kk]  # point on edge [e_i,e_k] near e_i
                    n = np.cross(E[j], y)  # line through e_j and y
                    if np.dot(n, E[kk]) < 0:
                        n = -n
                    vals = [np.dot(n, m) for m in V] + [np.dot(n, mstar)]
                    if np.dot(n, E[i]) < 0 and min(vals) > 0:
                        found = True
                        break
                ok &= found
    out.append(("G7 witnesses for L5 and L7 exist", ok))
    # G8
    ok = True
    oo = o[(0, 1)]
    m = (V[0] + V[1] + oo) / 3  # interior point of cap_12
    r = corner_rays(V)[(0, 1)]
    ok &= np.dot(m, r) < 0
    r0, r1 = facet(V, 0)
    # identify which end of F_1 is r_12
    end = 0 if np.allclose(r0, r) else 1
    ts = np.linspace(0, 1, 2001)
    H = np.array([(1 - t) * r0 + t * r1 for t in ts])
    tc = min(crossing(V, 0, 1)[1], crossing(V, 0, 2)[1]) if end == 0 else max(crossing(V, 0, 1)[1], crossing(V, 0, 2)[1])
    sel = (ts < 0.02 * tc) if end == 0 else (ts > 1 - 0.02 * (1 - tc))
    near = H[sel]
    ok &= bool(np.all(near @ m < 0))
    ok &= bool(np.all(near[:, 0] < 0) and np.all(near[:, 1] < 0) and np.all(near[:, 2] > 0))
    # corner-pattern chord through u: b with pattern (-,-,+), b.u = 0
    b = np.array([-1.0, -2.0, 3.0])
    ok &= abs(b.sum()) < 1e-12 and np.dot(b, E[2]) > 0 > np.dot(b, E[1])
    # middle arc of F_1: h_2>0, h_3>0
    mid = H[(H[:, 1] > 0) & (H[:, 2] > 0)]
    ok &= len(mid) > 0
    out.append(("G8 cap point negative near r_12 on F_1; middle arc positive at 2,3", ok))
    return out


if __name__ == "__main__":
    for eps in [0.01, 0.05, 1 / 7, 0.2, 0.3, 0.5, 0.6, 0.8, 0.9, 0.99]:
        res = report(eps)
        print(f"eps={eps:.4f}: " + "; ".join(f"{name}: {'OK' if v else 'FAIL'}" for name, v in res))


def cap_patterns(eps, trials=20000):
    """G9: every line strictly separating a point of cap_12 from T1 has vertex pattern (-,-,+)
    (oriented T1-positive); every line through a vertex and a hexagon point meets T1."""
    V = T1_vertices(eps)
    W = {}
    for k in range(3):
        for c in range(3):
            if c != k:
                W[(k, c)] = crossing(V, k, c)[0]
    o12 = line_intersection(W[(0, 1)], W[(1, 0)])
    ok = True
    cnt = 0
    for _ in range(trials):
        lam = rng.dirichlet(np.ones(3))
        m = lam @ np.vstack([V[0], V[1], o12])
        # random direction; line through a point between m and T1 hull, check if it separates
        th = rng.uniform(0, np.pi)
        d2 = np.array([np.cos(th), np.sin(th)])
        # basis of 1-perp
        B = np.array([[1, -1, 0], [1, 1, -2]], float)
        B[0] /= np.linalg.norm(B[0]); B[1] /= np.linalg.norm(B[1])
        nvec = d2 @ B  # normal within 1-perp
        vals = [np.dot(nvec, v) for v in V]
        lo, hi = min(vals), max(vals)
        mv = np.dot(nvec, m)
        if lo <= mv <= hi:
            continue
        # choose offset strictly between
        if mv < lo:
            off = rng.uniform(mv, lo)
            g = nvec - off  # g.m = n.m - off, using m.1 = 1
        else:
            off = rng.uniform(hi, mv)
            g = off - nvec
        # orientation: T1 positive
        assert min(np.dot(g, v) for v in V) > 0 and np.dot(g, m) < 0
        cnt += 1
        ok &= (g[0] < 0 and g[1] < 0 and g[2] > 0)
    # lines through e_l and a random hexagon point meet T1
    for _ in range(trials // 4):
        p = rng.dirichlet(np.ones(3))
        if not all(np.dot(p, w) >= 0 for w in W.values()):
            continue
        for l in range(3):
            n = np.cross(E[l], p)
            vals = [np.dot(n, v) for v in V]
            if np.linalg.norm(p - E[l]) < 1e-9:
                continue
            ok &= min(vals) <= 1e-12 <= max(vals) or min(vals) <= 0 <= max(vals)
    return ok, cnt


if __name__ == "__main__":
    for eps in [0.01, 0.05, 1 / 7, 0.3, 0.6, 0.9, 0.99]:
        ok, cnt = cap_patterns(eps)
        print(f"G9 eps={eps:.4f}: separating lines from cap_12 have pattern (-,-,+) [{cnt} lines]; "
              f"vertex lines through hexagon meet T1: {'OK' if ok else 'FAIL'}")


def g10(eps, n=200000):
    """G10: C_i cap W_i is strictly larger than T1 (so crossing pinning plus betweenness alone do not
    give K^i = T1; the extra (K2) step at v_i in the note is needed)."""
    V = T1_vertices(eps)
    W = {}
    for k in range(3):
        for c in range(3):
            if c != k:
                W[(k, c)] = crossing(V, k, c)[0]
    pts = rng.dirichlet(np.ones(3), size=n)
    M = np.vstack(V).T
    lamT = np.linalg.solve(M, pts.T).T
    inT = np.all(lamT >= -1e-12, 1)
    i = 0
    Ci = np.vstack([E[0], V[1], V[2]]).T
    inC = np.all(np.linalg.solve(Ci, pts.T).T >= -1e-12, 1)
    inWi = (pts @ W[(0, 1)] >= 0) & (pts @ W[(0, 2)] >= 0)
    extra = inC & inWi & ~inT
    return int(extra.sum())


if __name__ == "__main__":
    for eps in [0.05, 0.3, 0.6, 0.9]:
        print(f"G10 eps={eps}: sample points in (C_1 cap W_1) minus T1: {g10(eps)} (expected > 0)")
