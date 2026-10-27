"""geo75: exact cell geometry for PP75 (geometer, round 59).  Own code; Fractions only.

Chart: problems g mod sign are represented by h with h1+h2+h3 = 1 (h = (x, y, 1-x-y)); the
set {sum g = 0} is null.  T = D_M, M = c1 + eps*Delta, eps = 3/10, c = 7/30; vertices
v^a = (7,7,7) + 9 e_a (scaled by 30).  Posterior C_m: g in C_m iff sum_i m_i v^a_i g_i > 0 for all a.
Answer of C_m at h: 'h' if all three > 0, '-h' if all < 0, 'S' otherwise ('C' never).
World w: answer h correct iff h_w > 0; -h correct iff h_w < 0.  Ranks 0/1/2/3.
Cells: open cells of the line arrangement {h_i = 0} u {L_{m,a} = 0}, enumerated by exact
convex-polygon splitting inside a box containing every pairwise intersection point.
"""
from fractions import Fraction as F
import itertools

V = [(16, 7, 7), (7, 16, 7), (7, 7, 16)]

def lines_of_model(m):
    # line a*x + b*y + c (with h3 = 1-x-y): sum_i m_i v_i h_i
    out = []
    for v in V:
        w = [F(m[i]) * v[i] for i in range(3)]
        out.append((w[0] - w[2], w[1] - w[2], w[2]))
    return out

COORD = [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(-1), F(-1), F(1))]  # h1, h2, h3

def ev(l, p):
    return l[0] * p[0] + l[1] * p[1] + l[2]

def inter(l1, l2):
    d = l1[0] * l2[1] - l1[1] * l2[0]
    if d == 0:
        return None
    x = (l1[1] * l2[2] - l1[2] * l2[1]) / d
    y = (l1[2] * l2[0] - l1[0] * l2[2]) / d
    return (x, y)

def split(poly, l):
    """split convex polygon (list of vertices) by line l; return (pos, neg) polygons or None"""
    pos, neg = [], []
    n = len(poly)
    for i in range(n):
        p, q = poly[i], poly[(i + 1) % n]
        ep, eq = ev(l, p), ev(l, q)
        if ep >= 0: pos.append(p)
        if ep <= 0: neg.append(p)
        if (ep > 0 and eq < 0) or (ep < 0 and eq > 0):
            t = ep / (ep - eq)
            r = (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))
            pos.append(r); neg.append(r)
    def area(P):
        if len(P) < 3: return F(0)
        s = F(0)
        for i in range(len(P)):
            a, b = P[i], P[(i + 1) % len(P)]
            s += a[0] * b[1] - a[1] * b[0]
        return abs(s) / 2
    return (pos if area(pos) > 0 else None), (neg if area(neg) > 0 else None)

def centroid(P):
    n = len(P)
    return (sum(p[0] for p in P) / n, sum(p[1] for p in P) / n)

def cells(models, extra_lines=()):
    L = list(COORD)
    for m in models:
        L += lines_of_model(m)
    L += list(extra_lines)
    pts = [inter(a, b) for a, b in itertools.combinations(L, 2)]
    pts = [p for p in pts if p is not None]
    lo = min(min(p[0] for p in pts), min(p[1] for p in pts)) - 1
    hi = max(max(p[0] for p in pts), max(p[1] for p in pts)) + 1
    polys = [[(lo, lo), (hi, lo), (hi, hi), (lo, hi)]]
    for l in L:
        new = []
        for P in polys:
            a, b = split(P, l)
            if a: new.append(a)
            if b: new.append(b)
        polys = new
    out = []
    for P in polys:
        c = centroid(P)
        out.append({'poly': P, 'pt': (c[0], c[1], 1 - c[0] - c[1])})
    return out

def sgn(x): return (x > 0) - (x < 0)

def htype(h):
    """('U',None) unanimous; ('A',k) one negative coord k (h = majority answer, wrong only at k);
       ('B',k) one positive coord k (h = minority answer, right only at k)."""
    s = [sgn(x) for x in h]
    assert 0 not in s
    neg = [i for i in range(3) if s[i] < 0]
    if len(neg) == 0: return ('U', None)
    if len(neg) == 1: return ('A', neg[0])
    pos = [i for i in range(3) if s[i] > 0]
    return ('B', pos[0])

def answer(m, h):
    vals = [sum(F(m[i]) * V[a][i] * h[i] for i in range(3)) for a in range(3)]
    if all(v > 0 for v in vals): return 'h'
    if all(v < 0 for v in vals): return '-h'
    assert all(v != 0 for v in vals)
    return 'S'

def rank(ans, h, w):
    if ans == 'S': return 1
    if ans == 'C': return 3
    if ans == 'h': return 0 if h[w] > 0 else 2
    if ans == '-h': return 0 if h[w] < 0 else 2
    raise ValueError(ans)

def pattern(old, new, h):
    """worlds at which new is strictly better than old (old != new)"""
    return frozenset(w for w in range(3) if rank(new, h, w) < rank(old, h, w))

def pname(P):
    return '{' + ','.join(str(w + 1) for w in sorted(P)) + '}'

# ---------------- atoms and the necessary-condition checker -----------------
# An atom is a dict: 'h' (point), 'vals' (dict model-name -> answer).  Rival X may be split:
# then the cell yields several atoms (one per X value), all non-null.

def better_eq(a, b, h, w):   # a weakly better than b at w
    return rank(a, h, w) <= rank(b, h, w)

def strictly(a, b, h, w):
    return rank(a, h, w) < rank(b, h, w)

def N1(atoms, X='X', B='B'):
    """B strictly better than X at every world somewhere (else X >=_w B pointwise: B <=_w X refused)."""
    ok = []
    for w in range(3):
        ok.append(any(strictly(a['vals'][B], a['vals'][X], a['h'], w) for a in atoms))
    return all(ok), ok

def N2(atoms, Z, X='X', B='B'):
    """agreement obstruction for committed Z: B must not agree with X a.e. on Delta(Z,X).
    Returns (ok, hybrid_nonconic_flag).  The hybrid B[Delta(Z,X) -> Z] is non-conic iff some cell
    carries both a Delta(Z,X)-atom and a non-Delta atom with B != Z on the latter... (computed on cells)."""
    D = [a for a in atoms if a['vals'][Z] != a['vals'][X]]
    agree = all(a['vals'][B] == a['vals'][X] for a in D) and len(D) > 0
    # non-conicity of the hybrid: within a cell, hybrid value = Z on Delta part, B elsewhere
    noncon = False
    bycell = {}
    for a in atoms:
        bycell.setdefault(a['cell'], []).append(a)
    for c, As in bycell.items():
        hv = set((a['vals'][Z] if a['vals'][Z] != a['vals'][X] else a['vals'][B]) for a in As)
        if len(hv) > 1: noncon = True
    return (not agree), noncon

def defeated(atoms, Z, X='X', B='B', worlds=(0, 1, 2)):
    """Copy-coupled defeat of committed Z by the installed domination B <=_w X (all w).
    Z is defeated iff there is a non-null S subset Delta(Z,B) such that at every world j in supp(Z)
    either (R_j) X >_j Y_S := B[S -> Z] by guidance, or (G_j) Z[S -> B] >_j Z by guidance.
    Atom states: 'in', 'out', 'split' (only atoms with Z != B may be in/split).  Exhaustive over
    mode vectors; per atom allowed states; existential witnesses handled by brute force over pairs.
    Returns None if not defeated, else a witness (modes, chosen S description)."""
    for modes in itertools.product('RG', repeat=len(worlds)):
        Rw = [w for w, md in zip(worlds, modes) if md == 'R']
        Gw = [w for w, md in zip(worlds, modes) if md == 'G']
        allowed = []
        feasible = True
        for a in atoms:
            h, z, b, x = a['h'], a['vals'][Z], a['vals'][B], a['vals'][X]
            st = []
            in_ok = (z != b) and all(better_eq(x, z, h, w) for w in Rw) and all(strictly(b, z, h, w) for w in Gw)
            out_ok = all(better_eq(x, b, h, w) for w in Rw)
            if out_ok: st.append('out')
            if in_ok: st.append('in')
            if in_ok and out_ok: st.append('split')
            if not st:
                feasible = False; break
            allowed.append(st)
        if not feasible: continue
        def gives_in(s): return s in ('in', 'split')
        def gives_diff(a, s):
            h, z, b, x = a['h'], a['vals'][Z], a['vals'][B], a['vals'][X]
            d = False
            if s in ('in', 'split') and x != z: d = True
            if s in ('out', 'split') and x != b: d = True
            return d
        needG = len(Gw) > 0
        needR = len(Rw) > 0
        cand = [(i, s) for i, a in enumerate(atoms) for s in allowed[i]]
        ok = False
        wit = None
        if not needG and not needR:
            continue
        for (i, s) in cand:
            if needG and not gives_in(s): continue
            if needR and not gives_diff(atoms[i], s):
                # need a second atom for diff
                for (k, t) in cand:
                    if k == i: continue
                    if gives_diff(atoms[k], t):
                        ok = True; wit = (modes, i, s, k, t); break
                if ok: break
                continue
            ok = True; wit = (modes, i, s); break
        if not needG and needR and not ok:
            for (i, s) in cand:
                if gives_diff(atoms[i], s):
                    ok = True; wit = (modes, i, s); break
        if ok:
            return wit
    return None

def base_refusals(atoms, Z, X='X'):
    """worlds j with X >_j Z by strict guidance (coupled rule: Z must refuse B at j)"""
    out = []
    for w in range(3):
        diff = [a for a in atoms if a['vals'][X] != a['vals'][Z]]
        if diff and all(better_eq(a['vals'][X], a['vals'][Z], a['h'], w) for a in diff):
            out.append(w)
    return out

def guidance_status(atoms, P, Q, w):
    """'>' if P strictly better than Q pointwise at w, '<', '=' (equal), 'mix'"""
    diff = [a for a in atoms if a['vals'][P] != a['vals'][Q]]
    if not diff: return '='
    b = all(better_eq(a['vals'][P], a['vals'][Q], a['h'], w) for a in diff)
    c = all(better_eq(a['vals'][Q], a['vals'][P], a['h'], w) for a in diff)
    if b: return '>'
    if c: return '<'
    return 'mix'

def candidate_check(atoms, committed, X='X', B='B'):
    """All guidance-level necessary conditions for B to dominate X, given committed models."""
    rep = {}
    n1, n1w = N1(atoms, X, B)
    rep['N1'] = n1
    rep['N1w'] = n1w
    rep['N2'] = {}
    rep['N3'] = {}
    ok = n1
    for Z in committed:
        n2, nc = N2(atoms, Z, X, B)
        rep['N2'][Z] = (n2, nc)
        if not n2: ok = False
        d = defeated(atoms, Z, X, B)
        rep['N3'][Z] = d
        if d is not None: ok = False
    rep['ok'] = ok
    return rep

def order_type(m):
    """13 order types of a positive triple (mod scale)."""
    a, b, c = (F(x) for x in m)
    vals = [a, b, c]
    if a == b == c: return 'u'
    for k in range(3):
        o = [vals[i] for i in range(3) if i != k]
        if o[0] == o[1]:
            return ('raise%d' % (k + 1)) if vals[k] > o[0] else ('lower%d' % (k + 1))
    srt = sorted(range(3), key=lambda i: vals[i])
    return 'gen' + ''.join(str(i + 1) for i in srt)   # bottom..top

def pattern_formula(r):
    """Pattern Lemma: patterns occurring in rec(C_a -> C_b), r = b/a."""
    r = [F(x) for x in r]
    out = set()
    for k in range(3):
        o = [r[i] for i in range(3) if i != k]
        if r[k] > min(o): out.add(frozenset([k]))
        if r[k] < max(o): out.add(frozenset(i for i in range(3) if i != k))
    return out
