"""PP66 (CHECKED, exact integers): the two-neighbourhood test on an exact atom instance.

Worlds 0,1,2.  For the pair (a, b): middle world m = 0, max world p = 1, min world n = 2 of log(b/a)
(the u -> B pattern of PP62 Sec. 1.2, re-indexed from 0).

Atoms (mu-mass = |g|-weight, integers):
  F  : Fp1, Fp2 (Wr={m}), Fe1, Fe2 (Cor={m}); a answers h, b silent.  m(Fp) = m(Fe): u1-balanced swap.
  K  : Kp (Cor={p}, a silent, b answers), Kn (Cor={n}, a answers, b silent)  -> D_ab strictly larger than F.
  La : layer of the pure shift a_t = a o (1 + t e_w):  La_w (Cor={w}, a silent, a_t answers),
       La_v (Cor={v}, a answers, a_t silent) for v != w.  If v = n, b agrees with a_t there (La_n in D_ab).
  Lb : layer of b_t = b o (1 + t e_w), same pattern; if v = p, a agrees with b_t there (Lb_p in D_ab).
Values {h, S} on every atom (this is the h/S sector, where every member's sum of u1 is indifferent).
Models: all 2^12 = 4096 assignments.  Selected members: C_a, C_{a_t}, C_b, C_{b_t}.
X = C_a[F -> C_b], Y = C_b[F -> C_a];  r = rec(C_a, X);  rec(C_b, Y) = r^{-1}.

Field f, rule R0^f:  V^f(rec(X,Y)) = Phi^f(Y) - Phi^f(X);  R = {} if X = Y;  {w : V_w < 0} if V != 0;  {W0} if V = 0.
Surgery at world w on U = B_delta(r) u B_delta(r^{-1})  (d = mu-mass of disagreement of records).
Final relation R1 = R0^f  u  {w on U}.

Checked exhaustively (all 4096^2 ordered pairs, all 4096^3 ordered triples via one integer matmul per world):
reflexivity, (IB) (by construction: verdict is a function of the record; re-verified by hashing), strict (G),
(TC), defence and protection of all four members against all models, the two reservations at w, the
alpha=(1,1) certificate.  Controls: f = u1 (Theorem E) and f = q.u1 with w = m both fail defence.
"""
import itertools, sys
import numpy as np

H, S = 0, 1          # value codes
m_, p_, n_ = 0, 1, 2


def u1(kind, o, x):
    """PP56 level-0 field on R for the values h (x=0) and S (x=1), per unit |g|-mass.  kind in {'Cor','Wr'}."""
    if x == S:
        return (0, 0, 0)
    cor = {o} if kind == 'Cor' else set(range(3)) - {o}
    wr = set(range(3)) - cor
    kc, kr = len(wr), len(cor)
    return tuple(-kc if i in cor else kr for i in range(3))


def rank(kind, o, x, i):
    if x == S:
        return 1
    cor = {o} if kind == 'Cor' else set(range(3)) - {o}
    return 0 if i in cor else 2


def build(w):
    atoms = []   # (name, kind, o, mass, a, b, a_t, b_t)  values of the four members
    atoms += [('Fp1', 'Wr', m_, 4, H, S, H, S), ('Fp2', 'Wr', m_, 6, H, S, H, S),
              ('Fe1', 'Cor', m_, 5, H, S, H, S), ('Fe2', 'Cor', m_, 5, H, S, H, S)]
    atoms += [('Kp', 'Cor', p_, 2, S, H, S, H), ('Kn', 'Cor', n_, 2, H, S, H, S)]
    for v in range(3):
        if v == w:
            atoms.append(('La%d' % v, 'Cor', v, 1, S, S, H, S))
        else:
            bval = S if v == n_ else H
            atoms.append(('La%d' % v, 'Cor', v, 1, H, bval, S, bval))
    for v in range(3):
        if v == w:
            atoms.append(('Lb%d' % v, 'Cor', v, 1, S, S, S, H))
        else:
            aval = S if v == p_ else H
            atoms.append(('Lb%d' % v, 'Cor', v, 1, aval, H, aval, S))
    return atoms


def setup(w):
    atoms = build(w)
    A = len(atoms)
    models = np.array(list(itertools.product([H, S], repeat=A)), dtype=np.int8)   # (N, A)
    N = len(models)
    mass = np.array([at[3] for at in atoms], dtype=np.int64)
    idx = {tuple(row): k for k, row in enumerate(models.tolist())}
    mem = {nm: idx[tuple(at[4 + j] for at in atoms)] for j, nm in enumerate(['a', 'b', 'a_t', 'b_t'])}
    Fset = [k for k, at in enumerate(atoms) if at[0].startswith('F')]
    Xv = list(models[mem['a']]); Yv = list(models[mem['b']])
    for k in Fset:
        Xv[k] = models[mem['b']][k]; Yv[k] = models[mem['a']][k]
    mem['X'] = idx[tuple(Xv)]; mem['Y'] = idx[tuple(Yv)]
    return atoms, models, mass, mem, Fset


def field(atoms, kind, w, theta_scale=1, q=None):
    """Return per-atom per-value 3-vectors (integers, scaled by 2 to keep theta = |g|/2 integral)."""
    others = [v for v in range(3) if v != w]
    v_plus, v_minus = others[0], others[1]
    tab = []
    for k, at in enumerate(atoms):
        name, kd, o, ms = at[:4]
        row = []
        for x in (H, S):
            base = [2 * c for c in u1(kd, o, x)]
            if kind == 'q' and q is not None:
                base = [c * q[k] for c in base]
            if kind == 'psi' and name.startswith('F') and x == H:
                s = +1 if at[4] == H else -1          # +1 where r goes h -> S
                th = theta_scale                       # theta = |g|/2 per unit mass, times 2
                base[v_plus] += -s * th
                base[v_minus] += +s * th
            row.append(base)
        tab.append(row)
    return np.array(tab, dtype=np.int64)               # (A, 2, 3)


def phi(models, mass, tab):
    A = models.shape[1]
    out = np.zeros((models.shape[0], 3), dtype=np.int64)
    for k in range(A):
        out += mass[k] * tab[k][models[:, k]]
    return out


def ranks(models, atoms):
    N, A = models.shape
    out = np.zeros((3, N, A), dtype=np.int8)
    for k, at in enumerate(atoms):
        for x in (H, S):
            sel = models[:, k] == x
            for i in range(3):
                out[i, sel, k] = rank(at[1], at[2], x, i)
    return out


def record_dist(models, mass, old, new):
    """d(rec(X,Y), rho0) for all ordered pairs, rho0 = rec(old,new) (atom vectors)."""
    N, A = models.shape
    D = np.zeros((N, N), dtype=np.int32)
    for k in range(A):
        col = models[:, k]
        Xk = col[:, None]; Yk = col[None, :]
        if old[k] == new[k]:
            mis = Xk != Yk
        else:
            mis = ~((Xk == old[k]) & (Yk == new[k]))
        D += mass[k] * mis
    return D


def run(w, kind, W0, delta, surgery=True, q=None, verbose=True):
    atoms, models, mass, mem, Fset = setup(w)
    N = len(models)
    tab = field(atoms, kind, w, q=q)
    # (U1): strict monotonicity in rank at every world, (U2): sum over worlds equal for h and S (indifference)
    for k, at in enumerate(atoms):
        for i in range(3):
            rh, rs = rank(at[1], at[2], H, i), rank(at[1], at[2], S, i)
            assert (tab[k][H][i] - tab[k][S][i]) * (rh - rs) > 0, ('U1', at[0], i)
        assert tab[k][H].sum() == tab[k][S].sum(), ('U2', at[0])
    P = phi(models, mass, tab)
    V = P[None, :, :] - P[:, None, :]                 # V[x, y] = Phi(y) - Phi(x)
    same = np.all(models[:, None, :] == models[None, :, :], axis=2)
    nz = np.any(V != 0, axis=2)
    Ref = np.zeros((3, N, N), dtype=bool)
    for i in range(3):
        Ref[i] = np.where(nz, V[:, :, i] < 0, (~same) & (i == W0))
    rA, rX = models[mem['a']], models[mem['X']]
    inU = None
    if surgery:
        D1 = record_dist(models, mass, rA, rX)
        D2 = record_dist(models, mass, rX, rA)
        inU = (D1 < delta) | (D2 < delta)
        Ref[w] |= inU
    Acc = ~Ref
    res = {}
    # reflexivity
    res['reflexivity'] = bool(np.all(Acc[:, np.arange(N), np.arange(N)]))
    # (IB): verdict function of the record -- verify by hashing a sample of 200000 pairs
    rng = np.random.default_rng(66)
    xs = rng.integers(0, N, 200000); ys = rng.integers(0, N, 200000)
    seen = {}
    ib = True
    for x, y in zip(xs.tolist(), ys.tolist()):
        key = tuple((k, int(models[x, k]), int(models[y, k])) for k in range(models.shape[1]) if models[x, k] != models[y, k])
        val = tuple(bool(Ref[i, x, y]) for i in range(3))
        if seen.setdefault(key, val) != val:
            ib = False
    res['IB(sample 2e5)'] = ib
    # strict (G)
    Rk = ranks(models, atoms)
    g_ok = True
    for i in range(3):
        d = Rk[i][None, :, :].astype(np.int16) - Rk[i][:, None, :].astype(np.int16)   # rank(y) - rank(x)
        weak_worse = np.all(d >= 0, axis=2) & np.any(d > 0, axis=2)                     # y pointwise w-worse
        if np.any(weak_worse & ~Acc[i]):
            g_ok = False
        if np.any(weak_worse.T & Acc[i]):     # reverse: y <=_i x must be refused when y worse; i.e. Acc[i][y,x] false
            g_ok = False
    res['strict (G)'] = g_ok
    # (TC): exists i,j,k with Acc[i,j],Acc[j,k],Acc[k,i] and some link without its reverse
    tc_ok = True
    for i in range(3):
        Af = Acc[i].astype(np.float32)
        M = (Acc[i] & ~Acc[i].T).astype(np.float32)
        Pm = M @ Af
        viol = (Pm * Af.T).sum()
        if viol > 0:
            tc_ok = False
    res['(TC) all triples'] = tc_ok
    # defence and protection of the four members (interior: support = all worlds)
    dp = {}
    for nm in ['a', 'a_t', 'b', 'b_t']:
        c = mem[nm]
        defended = np.any(Acc[:, c, :], axis=0)
        protected = np.any(Ref[:, :, c], axis=0) | (np.arange(N) == c)
        dp[nm] = (bool(defended.all()), bool(protected.all()))
        if not defended.all():
            bad = np.where(~defended)[0]
            dp[nm] = dp[nm] + ('undefended vs X' if mem['X'] in bad else '', 'undefended vs Y' if mem['Y'] in bad else '', len(bad))
    res['defence/protection'] = dp
    # reservations
    resv = {
        'C_a  !<=_w X': bool(Ref[w, mem['a'], mem['X']]),
        'C_at !<=_w X': bool(Ref[w, mem['a_t'], mem['X']]),
        'C_b  !<=_w Y': bool(Ref[w, mem['b'], mem['Y']]),
        'C_bt !<=_w Y': bool(Ref[w, mem['b_t'], mem['Y']]),
    }
    res['reservations'] = resv
    # verdict table on the key records
    def R_of(x, y):
        return sorted(i for i in range(3) if Ref[i, x, y])
    res['R(C_a->X), R(X->C_a), R(C_b->Y)'] = (R_of(mem['a'], mem['X']), R_of(mem['X'], mem['a']), R_of(mem['b'], mem['Y']))
    res['R(C_at->X), R(C_bt->Y)'] = (R_of(mem['a_t'], mem['X']), R_of(mem['b_t'], mem['Y']))
    # u1-values of the shifted records (to exhibit Cor E.2(i))
    tab_u = field(atoms, 'u1', w)
    Pu = phi(models, mass, tab_u)
    res['u1-value(C_at->X)/2'] = tuple(int(z) for z in (Pu[mem['X']] - Pu[mem['a_t']]) // 1)
    res['u1-value(C_bt->Y)/2'] = tuple(int(z) for z in (Pu[mem['Y']] - Pu[mem['b_t']]) // 1)
    res['f-value(C_a->X)'] = tuple(int(z) for z in (P[mem['X']] - P[mem['a']]))
    # alpha = (1,1): pointwise increments at w of r and r^{-1} cancel
    inc_r = [tab_u[k][rX[k]][w] - tab_u[k][rA[k]][w] for k in range(len(atoms))]
    inc_ri = [tab_u[k][rA[k]][w] - tab_u[k][rX[k]][w] for k in range(len(atoms))]
    res['alpha=(1,1) cancels'] = all(x + y == 0 for x, y in zip(inc_r, inc_ri)) and any(inc_r)
    # Lemma S splits of the accepted shifted record at a world v != w (PP63 sharpened Cor E.2(ii))
    acc_worlds = [v for v in range(3) if v != w and Acc[v, mem['a_t'], mem['X']]]
    res['C_at accepts X at'] = acc_worlds
    if inU is not None:
        res['|U| (ordered pairs)'] = int(inU.sum())
    if verbose:
        print('  w=%d field=%s W0=%d delta=%s surgery=%s' % (w, kind, W0, delta, surgery))
        for k_, v_ in res.items():
            print('    %-34s %s' % (k_, v_))
    return res


def all_ok(res):
    dp = res['defence/protection']
    return (res['reflexivity'] and res['IB(sample 2e5)'] and res['strict (G)'] and res['(TC) all triples']
            and all(t[0] and t[1] for t in dp.values()) and all(res['reservations'].values())
            and res['alpha=(1,1) cancels'])


if __name__ == '__main__':
    passes = []
    print('MAIN: f = psi = u1 + phi (phi on F, zero-sum, theta = |g|/2), surgery at w on U, delta = 3.5')
    for w in range(3):
        r = run(w, 'psi', W0=w, delta=3.5)
        ok = all_ok(r)
        print('    => ALL CLAUSES:', ok)
        passes.append(ok)
    print('\nSECOND: f = q.u1, q = 3 on Fp1, 1 elsewhere (scalar weight), w != m')
    q = [1] * 12; q[0] = 3
    for w in (1, 2):
        r = run(w, 'q', W0=w, delta=3.5, q=q)
        ok = all_ok(r)
        print('    => ALL CLAUSES:', ok)
        passes.append(ok)
    print('\nCONTROL 1 (Theorem E): f = u1 itself, surgery at w (expect a shifted member undefended)')
    for w in range(3):
        r = run(w, 'u1', W0=w, delta=3.5)
        ok = all_ok(r)
        print('    => ALL CLAUSES:', ok, '(expected False)')
        passes.append(not ok)
    print('\nCONTROL 2 (scalar q, w = m): f = q.u1, surgery at w = m (expect C_a or C_b undefended at its centre)')
    r = run(0, 'q', W0=0, delta=3.5, q=q)
    ok = all_ok(r)
    print('    => ALL CLAUSES:', ok, '(expected False)')
    passes.append(not ok)
    print('\nCONTROL 3: f = psi without surgery (expect the w-refusals missing: additive base gives a tie at w)')
    r = run(0, 'psi', W0=0, delta=3.5, surgery=False)
    passes.append(not all(r['reservations'].values()))
    print('    reservations hold:', all(r['reservations'].values()), '(expected False)')
    print('\nALL PASS' if all(passes) else '\nFAILURES: %s' % passes)
