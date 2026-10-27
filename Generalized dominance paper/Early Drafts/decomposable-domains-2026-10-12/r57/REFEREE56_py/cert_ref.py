"""cert_ref (REFEREE56): independent checks of the certificate fields of PP67 Thm 4.1 / Thm 6.1, and a
full-domain certificate for PP68 Prop 4.5's claim that L0 dominates every class-3 fill of N.

Run: python3 -I -B cert_ref.py > cert_ref.out

Part 1. PP67's 15 per-type vectors (data copied from PP67_py/witness67.py, logic re-implemented):
        sign pattern + unique argmins of lam_T=(1,1,1), lam_N=(1,1,1/2), lam_D=(1,1,0).
Part 2. Theorem 6.1: for the 39 mixed types of the seven-model module (types7_ref.json, from my own exact
        cell enumeration) solve an LP for per-type vectors and re-check EXACTLY in rationals.
Part 3. Four-model module T, N, D*, L0 with lam_L = (1,1,nu): per-type LP on my census (geom_ref), exact
        re-check; then an exhaustive finite instance (3^k models) of the resulting relation W+ with weights,
        checking protection, defence of all four models against every model, PP67's C1-C3, the fourth
        inequality, and L0 <=_w N[E -> A] at every world for every union E of E0-atoms and of R_B-atoms.
"""
import os, sys, json, itertools
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ok = True
def chk(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)

# ---------- Part 1 ----------
def M3v(aw, ao, bw, bo): return ((-aw[0], -aw[1], ao), (bw[0], bw[1], -bo))
def M1v(ao, aw, bo, bw): return ((ao, -aw[0], -aw[1]), (-bo, bw[0], bw[1]))
P67 = {(3, 'SSA'): M3v((1, 1), 5, (1, 1), 1), (3, 'AAA'): M3v((1, 1), 1, (1, 1), 1),
       (3, 'BSA'): M3v((1, 1), 10, (1, 1), F(5, 2)),
       (1, 'SSS'): M1v(3, (1, 1), 1, (2, 1)), (1, 'SSB'): M1v(3, (1, 1), F(3, 2), (1, 2)),
       (1, 'AAA'): M1v(1, (2, 1), 1, (1, 1)), (1, 'ASS'): M1v(3, (1, 3), 1, (2, 1)),
       (1, 'ASB'): M1v(3, (1, 3), F(3, 2), (1, 2)), (1, 'BBB'): M1v(2, (1, 1), 3, (1, 1))}
for (k, t), (a, b) in list(P67.items()):
    if k == 1: P67[(2, t)] = ((a[1], a[0], a[2]), (b[1], b[0], b[2]))
def val(lam, a, b):
    return {'S': F(0), 'A': sum(F(l) * x for l, x in zip(lam, a)), 'B': sum(F(l) * x for l, x in zip(lam, b))}
def uargmin(lam, a, b):
    v = val(lam, a, b); m = min(v.values()); w = [x for x in v if v[x] == m]
    return w[0] if len(w) == 1 else None
def signs_ok(k, a, b):
    o = k - 1
    return all((a[w] < 0 < b[w]) if w != o else (b[w] < 0 < a[w]) for w in range(3))
LT, LN, LD = (1, 1, 1), (1, 1, F(1, 2)), (1, 1, 0)
p1 = all(signs_ok(k, a, b) and [uargmin(l, a, b) for l in (LT, LN, LD)] == list(t) for (k, t), (a, b) in P67.items())
chk('P1 PP67 field (15 types): rank-monotone signs; T, N, D* unique argmins', p1)
print('   note: type (B,S,A) on M3 has b = %s; PP67 text prints (1,1,5/2): sign typo in b_3' % (P67[(3, 'BSA')][1],))

# ---------- LP helper ----------
def solve_type(k, lams, advs):
    """find a, b (6 vars) with rank-monotone signs (margin 1) and advs[i] unique argmin of lams[i] (margin 1)."""
    o = k - 1
    A_ub, b_ub = [], []
    def row(ca, cb, rhs):   # ca.a + cb.b <= rhs
        A_ub.append(list(ca) + list(cb)); b_ub.append(rhs)
    z = [0, 0, 0]
    for w in range(3):
        e = [0, 0, 0]; e[w] = 1; me = [-x for x in e]
        if w != o: row(e, z, -1); row(z, me, -1)
        else: row(me, z, -1); row(z, e, -1)
    for lam, x in zip(lams, advs):
        lam = [float(l) for l in lam]
        vec = {'S': ([0, 0, 0], [0, 0, 0]), 'A': (lam, [0, 0, 0]), 'B': ([0, 0, 0], lam)}
        for y in 'SAB':
            if y != x:   # val(x) - val(y) <= -1
                ca = [p - q for p, q in zip(vec[x][0], vec[y][0])]; cb = [p - q for p, q in zip(vec[x][1], vec[y][1])]
                row(ca, cb, -1)
    # minimise the L1 norm: variables (a, b, u) with -u <= x <= u
    A = np.array(A_ub, float); A = np.hstack([A, np.zeros((len(A), 6))])
    I6 = np.eye(6)
    A = np.vstack([A, np.hstack([I6, -I6]), np.hstack([-I6, -I6])])
    bb = np.array(list(b_ub) + [0] * 12, float)
    res = linprog(np.r_[np.zeros(6), np.ones(6)], A_ub=A, b_ub=bb, bounds=[(-50, 50)] * 6 + [(0, 50)] * 6,
                  method='highs')
    if res.success: res.x = res.x[:6]
    if not res.success: return None
    xs = [F(x).limit_denominator(64) for x in res.x]
    a, b = tuple(xs[:3]), tuple(xs[3:])
    if signs_ok(k, a, b) and [uargmin(l, a, b) for l in lams] == list(advs): return a, b
    return 'ROUNDING'

# ---------- Part 2 ----------
T7 = [tuple(t) for t in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'types7_ref.json')))]
lam7 = [(1, 1, 1)] + [tuple(F(1, 2) if j == k else 1 for j in range(3)) for k in range(3)] + \
       [tuple(0 if j == k else 1 for j in range(3)) for k in range(3)]
bad = []
for t in T7:
    r = solve_type(t[0], lam7, t[1:])
    if not isinstance(r, tuple): bad.append((t, r))
chk('P2 Thm 6.1: all %d mixed types of the seven-model module admit exact rational vectors with the seven '
    'unique argmins (independent LP + exact check)' % len(T7), not bad)
if bad: print('   failures:', bad)

# ---------- Part 3 ----------
from geomlib import cells, cls, AB, adv, KT, KN, KD, KL0
pts, _ = cells([(1, 0, 0), (0, 1, 0), (0, 0, 1)] + KN)
T4 = sorted({(cls(g),) + tuple(AB(g, adv(K, g)) for K in (KT, KN, KD, KL0)) for g in pts if cls(g) != 0})
print('   four-model mixed types:', T4)
NU = None
def mirror(v): return (v[1], v[0], v[2])
for nu in (F(1, 4), F(1, 3), F(1, 5), F(2, 5)):
    lams = [LT, LN, LD, (1, 1, nu)]
    sol = {t: solve_type(t[0], lams, t[1:]) for t in T4 if t[0] != 2}
    for t in T4:
        if t[0] == 2:
            a, b = sol[(1,) + t[1:]]; sol[t] = (mirror(a), mirror(b))
    if all(isinstance(x, tuple) for x in sol.values()) and \
       all(signs_ok(t[0], *sol[t]) and [uargmin(l, *sol[t]) for l in lams] == list(t[1:]) for t in T4):
        NU = nu; break
chk('P3a lam_L = (1,1,%s): T, N, D*, L0 are unique argmins on every four-model type (exact; class 2 = mirror '
    'of class 1)' % NU, NU is not None)
for t in T4: print('     %s  a=%s  b=%s' % (t, [str(x) for x in sol[t][0]], [str(x) for x in sol[t][1]]))
lam4 = {'T': LT, 'N': LN, 'D': LD, 'L': (1, 1, NU)}

results = []
def rep(name, cond):
    results.append((name, bool(cond)))
def instance(Wbig, Wp, report):
    global ok
    # finite instance: atoms = (type, mass, tag)
    atoms = []
    INST = [('S','S','A','S'), ('B','S','A','S'), ('S','S','B','B'), ('S','S','B','S'), ('A','S','B','S'), ('A','S','S','S')]
    for t in T4:
        if t[1:] not in INST: continue
        if t[0] == 3 and t[1:] == ('S', 'S', 'A', 'S'):
            atoms += [(t, 1, 'E0'), (t, 2, 'E0'), (t, 1, None)]
        elif t[0] == 3 and t[1:] == ('B', 'S', 'A', 'S'):
            atoms += [(t, Wbig, 'RB'), (t, Wbig, 'RB')]
        elif t[1:] == ('S', 'S', 'B', 'B'):
            atoms += [(t, Wp, None)]
        else:
            atoms += [(t, 1, None)]
    n = len(atoms); print('   finite instance: %d atoms, 3^%d = %d models' % (n, n, 3 ** n))
    VAL = 'ASB'
    Fv = np.zeros((n, 3, 3))
    for i, (t, m, _) in enumerate(atoms):
        a, b = sol[t]
        for w in range(3): Fv[i, 0, w] = m * float(a[w]); Fv[i, 2, w] = m * float(b[w])
    mods = np.array(list(itertools.product(range(3), repeat=n)), dtype=np.int8)
    Phi = np.zeros((len(mods), 3))
    for i in range(n): Phi += Fv[i, mods[:, i], :]
    KEY = [i for i, at in enumerate(atoms) if at[2] in ('E0', 'RB')]     # key region: Sil(N) n M3
    kap = np.zeros(len(mods))
    for i in KEY: kap += (mods[:, i] == 0) * atoms[i][1]                   # A on M3 is 3-wrong
    def idx(v): return int(sum(x * 3 ** (n - 1 - k) for k, x in enumerate(v)))
    def mk(j): return [VAL.index(at[0][1 + j]) for at in atoms]
    T_, N_, D_, L_ = (mk(j) for j in range(4)); iT, iN, iD, iL = map(idx, (T_, N_, D_, L_))
    tol = 1e-7
    def leq_vec(i, w, rev=False):
        if w < 2: return (Phi[:, w] <= Phi[i, w] + tol) if rev else (Phi[i, w] <= Phi[:, w] + tol)
        if rev: return (kap < kap[i]) | ((kap == kap[i]) & (Phi[:, 2] <= Phi[i, 2] + tol))
        return (kap[i] < kap) | ((kap[i] == kap) & (Phi[i, 2] <= Phi[:, 2] + tol))
    def leq(i, j, w): return bool(leq_vec(i, w)[j])
    for nm, i, supp in (('T', iT, (0, 1, 2)), ('N', iN, (0, 1, 2)), ('D*', iD, (0, 1)), ('L0', iL, (0, 1, 2))):
        dom = np.ones(len(mods), bool)
        for w in supp: dom &= leq_vec(i, w, rev=True)
        dom[i] = False
        defd = np.zeros(len(mods), bool)
        for w in supp: defd |= leq_vec(i, w)
        rep('P3b %s: protected on its support (no other model <= it there) and defended against all models' % nm,
            (not dom.any()) and defd.all())
    def fill(base, S):
        v = list(base)
        for i in S: v[i] = 0
        return idx(v)
    E0 = [i for i, at in enumerate(atoms) if at[2] == 'E0']; RB = [i for i, at in enumerate(atoms) if at[2] == 'RB']
    subs = lambda L: [list(c) for r in range(1, len(L) + 1) for c in itertools.combinations(L, r)]
    c = True
    for S in subs(E0):                         # PP67 C1, C2 and the fourth inequality, all E
        x, y = fill(T_, S), fill(N_, S)
        c &= all(leq(iN, x, w) for w in range(3)) and not leq(x, iN, 2)
        c &= leq(iD, x, 0) and leq(iD, x, 1) and leq(iD, y, 0) and leq(iD, y, 1)
    c &= all(leq(iN, iT, w) and leq(iD, iT, w) and leq(iD, iN, w) for w in (0, 1))       # C3
    rep('P3c PP67 C1-C3 and D* <=_{1,2} N-fills hold in W+ (every union of E0-atoms)', c)
    g = all(all(leq(iL, fill(N_, S), w) for w in range(3)) and not leq(fill(N_, S), iL, 2)
            for S in subs(E0 + RB))
    rep('P3d L0 <=_w N[E -> A] at all three worlds, strictly at 3, for EVERY union E of atoms of Sil(N) n M3 '
        '(E0-atoms and R_B-atoms)', g)


    return results
for Wbig, Wp in ((20, 200), (50, 1000), (100, 5000), (200, 20000), (500, 100000)):
    results = []
    res = instance(Wbig, Wp, False)
    if all(c for _, c in res):
        print('   finite instance passes with W = %d on R_B atoms and W\' = %d on the (S,S,B,B) atoms' % (Wbig, Wp))
        break
for name, c in res: chk(name, c)
print('ALL PASS' if ok else 'SOME FAIL')
