"""REFEREE round 56 (REFEREE_round55.md): independent re-implementation of PP66 Theorem 2 on a
DIFFERENT exact instance (own field code from PP56 Sec. 4.1, own record metric, own (TC) test).

Differences from PP66's instance: middle world m = 1 (PP66: m = 0); the balanced swap F has BOTH
signs s(g) = +1 and s(g) = -1 (PP66: only s = +1) and both odd-world-m kinds; a four-valued atom
off R (values h0, S, -h0, C) exercises the rank gaps of all four values; w0 (null-record world)
is taken different from the surgery world w.

Worlds 0,1,2.  d = log(b/a) has max p = 2, min n = 0, middle m = 1.  Atoms (|g|-mass, kind, odd world):
  F:  Fa  (30, Wr ={m})  a = h, b = S   (s = +1; r improves m)
      Fb  (20, Wr ={m})  a = S, b = h   (s = -1; r worsens m)
      Fc  (10, Cor={m})  a = h, b = S   (s = +1; r worsens m)        c_m = 30 - 20 - 10 = 0: balanced
  Kp  (2, Cor={p})  a = S, b = h        (D_ab bigger than F, so X != C_b; b improves p: Lemma 1.1)
  La_w (1, Cor={w}) a = S, a_t = h; La_v (1, Cor={v}) a = h, a_t = S (v != w); b = a_t on La_n
  Lb_w (1, Cor={w}) b = S, b_t = h; Lb_v (1, Cor={v}) b = h, b_t = S (v != w); a = b_t on Lb_p
  G   (1) off R, mixed signs, Cor(h0) = {0, 1}; all members say h0; rivals take h0, S, -h0, C.
Models: 2^10 * 4 = 4096.  Members a, b, a_t, b_t.
Checked exhaustively: field (U1) strict rank-monotonicity incl. four values, (U2) for members;
strict (G) on all ordered pairs; (TC) on all ordered triples (one matrix product per world);
defence and protection of the four members against every model; the four reservations at w;
centre verdicts.  Controls: u1 base (Theorem E) and common q at w = m (Prop 3) must fail.
Run: python3 -I -B twonbhd_ref.py
"""
import itertools
import numpy as np

m_, p_, n_ = 1, 2, 0
H, S_, NH, C_ = 0, 1, 2, 3          # h, S, -h, C


def kinds_sets(kind, o):
    cor = {o} if kind == 'Cor' else {0, 1, 2} - {o}     # worlds where h is correct
    return cor, {0, 1, 2} - cor


def field_R(kind, o):
    """PP56 level-0 field per unit |g| at a point of R with common answer h; values h,S,-h,C."""
    cor, wr = kinds_sets(kind, o)
    kc, kr = len(wr), len(cor)                       # h: (|Wr|, |Cor|)
    kc2, kr2 = len(cor), 2 * len(wr)                 # -h: Cor(-h) = wr, Wr(-h) = cor -> (|Wr(-h)|, 2|Cor(-h)|)
    h = [(-kc if i in cor else kr) for i in range(3)]
    nh = [(-kc2 if i in wr else kr2) for i in range(3)]
    cc = 1 + max(kc, kr, kc2, kr2)
    return {H: h, S_: [0, 0, 0], NH: nh, C_: [cc] * 3}


def field_off(cor):
    """off R, common advice h0 (correct on cor): h0 row (2|Wr|, |Cor|), -h0 row (|Wr|, 2|Cor|) of -h0."""
    wr = {0, 1, 2} - cor
    kc, kr = 2 * len(wr), len(cor)
    kc2, kr2 = len(cor), 2 * len(wr)
    h = [(-kc if i in cor else kr) for i in range(3)]
    nh = [(-kc2 if i in wr else kr2) for i in range(3)]
    cc = 1 + max(kc, kr, kc2, kr2)
    return {H: h, S_: [0, 0, 0], NH: nh, C_: [cc] * 3}


def rank(cor, x, i):
    if x == S_:
        return 1
    if x == C_:
        return 3
    good = (i in cor) == (x == H)
    return 0 if good else 2


def build(w):
    others = [v for v in range(3) if v != w]
    at = []   # name, mass, cor(h), field, values (a, b, a_t, b_t), inF, s
    def R_atom(name, mass, kind, o, vals, inF=False, s=0):
        cor, _ = kinds_sets(kind, o)
        at.append(dict(name=name, mass=mass, cor=cor, f=field_R(kind, o), vals=vals, inF=inF, s=s, two=True))
    R_atom('Fa', 30, 'Wr', m_, (H, S_, H, S_), True, +1)
    R_atom('Fb', 20, 'Wr', m_, (S_, H, S_, H), True, -1)
    R_atom('Fc', 10, 'Cor', m_, (H, S_, H, S_), True, +1)
    R_atom('Kp', 2, 'Cor', p_, (S_, H, S_, H))
    for v in range(3):
        if v == w:
            R_atom('La%d' % v, 1, 'Cor', v, (S_, S_, H, S_))
        else:
            bv = S_ if v == n_ else H
            R_atom('La%d' % v, 1, 'Cor', v, (H, bv, S_, bv))
    for v in range(3):
        if v == w:
            R_atom('Lb%d' % v, 1, 'Cor', v, (S_, S_, S_, H))
        else:
            av = S_ if v == p_ else H
            R_atom('Lb%d' % v, 1, 'Cor', v, (av, H, av, S_))
    at.append(dict(name='G', mass=1, cor={0, 1}, f=field_off({0, 1}), vals=(H, H, H, H), inF=False, s=0, two=False))
    return at, others


def run(w, base, surgery=True, w0=None, extra_world=None, delta2=7):
    at, others = build(w)
    v, vp = others
    if w0 is None:
        w0 = v
    A = len(at)
    # field values per atom, per value, times 2 (integers), with perturbation phi_F or weight q
    F = np.zeros((A, 4, 3), dtype=np.int64)
    for k, x in enumerate(at):
        for val in range(4):
            F[k, val] = [2 * x['mass'] * t for t in x['f'][val]]
        if base == 'psi' and x['inF']:
            # phi_F(g, h) = -s |g|/2 (e_v - e_v');  doubled: -s * mass * (e_v - e_v')
            F[k, H, v] += -x['s'] * x['mass']
            F[k, H, vp] -= -x['s'] * x['mass']
        if base == 'q' and x['name'] == 'Fa':
            F[k] *= 3
    # (U1) strict monotonicity in rank at each world, all four values; (U2)/(U3) for members
    u1ok = True
    for k, x in enumerate(at):
        for i in range(3):
            order = sorted(range(4), key=lambda val: rank(x['cor'], val, i))
            vals = [F[k, val, i] for val in order]
            u1ok &= all(vals[j] < vals[j + 1] for j in range(3))
        for mem in range(4):
            cv = x['vals'][mem]
            u1ok &= all(F[k, val].sum() >= F[k, cv].sum() for val in range(4))
    vals_list = [[H, S_] if x['two'] else [H, S_, NH, C_] for x in at]
    models = np.array(list(itertools.product(*vals_list)), dtype=np.int64)
    N = len(models)
    idx = {tuple(r): i for i, r in enumerate(models.tolist())}
    mem = [idx[tuple(x['vals'][j] for x in at)] for j in range(4)]   # a, b, a_t, b_t
    Ca, Cb = models[mem[0]], models[mem[1]]
    Xm, Ym = Ca.copy(), Cb.copy()
    for k, x in enumerate(at):
        if x['inF']:
            Xm[k], Ym[k] = Cb[k], Ca[k]
    iX, iY = idx[tuple(Xm)], idx[tuple(Ym)]
    Phi = np.stack([F[k, models[:, k], :] for k in range(A)]).sum(axis=0)      # (N, 3)
    V = Phi[None, :, :] - Phi[:, None, :]                                       # V[x, y] = Phi(y) - Phi(x)
    eq = (models[:, None, :] == models[None, :, :]).all(axis=2)
    null = (V == 0).all(axis=2) & ~eq
    Ref = (V < 0)
    Ref[null] = False
    Ref[null, w0] = True
    Ref[eq] = False
    # record distance to r = rec(C_a, X) and r^-1, per atom table
    def dist_to(oldm, newm):
        D = np.zeros((N, N), dtype=np.int64)
        for k, x in enumerate(at):
            nv = len(vals_list[k])
            tab = np.zeros((4, 4), dtype=np.int64)
            for p in range(4):
                for q in range(4):
                    tok = None if p == q else (p, q)
                    rt = None if oldm[k] == newm[k] else (oldm[k], newm[k])
                    tab[p, q] = x['mass'] if tok != rt else 0
            D += tab[models[:, k][:, None], models[:, k][None, :]]
        return D
    d_r, d_ri = dist_to(Ca, Xm), dist_to(Xm, Ca)
    delta2 = delta2          # 2*delta (delta = 3.5)
    Uset = (2 * d_r < delta2) | (2 * d_ri < delta2)
    if surgery:
        Ref[Uset, w] = True
        if extra_world is not None:
            Ref[Uset, extra_world] = True
    res = {'U1,U2': u1ok}
    # strict (G)
    rk = np.array([[[rank(x['cor'], val, i) for i in range(3)] for val in range(4)] for x in at])  # (A,4,3)
    R_ = np.stack([rk[k, models[:, k], :] for k in range(A)], axis=1)   # (N, A, 3)
    gok = True
    for i in range(3):
        ri = R_[:, :, i]
        weak = (ri[:, None, :] <= ri[None, :, :]).all(axis=2) & ~eq        # x weakly better than y
        gok &= not (Ref[:, :, i] & weak).any()
        gok &= (Ref[:, :, i].T[weak]).all()                                # y <=_i x refused
    res['strict G'] = gok
    # (TC)
    tc = True
    for i in range(3):
        Acc = (~Ref[:, :, i]).astype(np.float32)
        P2 = Acc @ Acc
        bad = (Acc > 0) & (Acc.T == 0) & (P2.T > 0)
        tc &= not bad.any()
    res['TC'] = tc
    # defence / protection of the four members
    dp = True
    for j in mem:
        others_idx = np.arange(N) != j
        dp &= (~Ref[j, others_idx, :]).any(axis=1).all()        # some world accepts C_j <= Z
        dp &= (Ref[others_idx, j, :]).any(axis=1).all()         # some world refuses Z <= C_j
    res['defence+protection'] = bool(dp)
    res['reservations'] = bool(Ref[mem[0], iX, w] and Ref[mem[2], iX, w] and Ref[mem[1], iY, w] and Ref[mem[3], iY, w])
    res['R(C_a->X)'] = [i for i in range(3) if Ref[mem[0], iX, i]]
    res['R(C_b->Y)'] = [i for i in range(3) if Ref[mem[1], iY, i]]
    res['V(r)/2'] = list(V[mem[0], iX] // 2)
    return res


ok = True


def show(tag, res, expect):
    global ok
    allc = res['U1,U2'] and res['strict G'] and res['TC'] and res['defence+protection'] and res['reservations']
    good = (allc == expect)
    ok &= good
    print('  %-34s %s  -> all clauses %s (expected %s) %s' % (tag, {k: res[k] for k in res}, allc, expect, 'PASS' if good else 'FAIL'))


print('MAIN: psi = u1 + phi_F, ball surgery at w, delta = 3.5, w0 != w')
for w in range(3):
    show('w=%d psi' % w, run(w, 'psi'), True)
print('CONTROLS')
for w in range(3):
    show('w=%d u1 base (Thm E)' % w, run(w, 'u1'), False)
show('w=m=1 common q base (Prop 3)', run(m_, 'q'), False)
for w in (0, 2):
    show('w=%d common q base (w != m)' % w, run(w, 'q'), True)
show('w=0 psi, NO surgery', run(0, 'psi', surgery=False), False)
print('PP65 Prop 5.1 (balls at two worlds on the same U)')
show('w=0 psi, balls at 0 and 1', run(0, 'psi', extra_world=1), False)
print('ALL PASS' if ok else 'SOME FAIL')
