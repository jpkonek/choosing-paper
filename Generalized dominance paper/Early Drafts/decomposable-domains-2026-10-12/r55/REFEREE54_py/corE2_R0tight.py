# REFEREE54: R0-minimal-modification test; otherwise a copy of PP61_py/run61d.py, only (i) sys.path pointed at PP61_py and (ii) each run pickled for the independent checker.
"""PP61 run D: the PP62 Cor E.2 configuration at u, as an exact germ-literal SAT problem.

Sources u, B (coherent, selected) and the pure shifts u_t^w = u o (1 + t e_w), w = 1,2,3, at TWO scales
t = s*tau, tau in {1, 1/10}, s -> 0 (six shifted members, all selected).
Rival X = C_u[F -> C_B], F = Ep.c1 u Em.c1 (kink cells; each slab split radially into halves a, b, all
four halves of equal |g|-mass, so F is u^1-balanced: V(F: u -> B) = 0 at all three worlds).
Models: C_u[E -> C_B] and C_B[E -> C_u] for all 16 E subset of F (so X, Y, all Lyapunov-type splits of
the base record and their reverses/copies); at every shifted source u_t: C_{u_t}[E -> C_B] and
C_{u_t}[E -> C_B][S -> C_u] for S in {whole layer, half the layer atoms} (= the splits Z = C_{u_t}[E' -> X]
of the record rec(C_{u_t}, X), E' = E u (layer \\ S)), and the copy C_B[F -> C_u, layer -> C_{u_t}].
Exact refined arrangement (u, B, and all six shifted members' planes) at s* = 1e-5; oriented-matroid
stability on (0, s*] is checked exactly (sympy), so the instance is the same for every s in (0, s*].
Clauses: G, DEF, UND/C, TC on ALL ordered triples (explicit, not lazy), SEC along s -> 0 for every
fixed (s-independent) rival.  Variants:
  V0  axioms only (the coordinator's run; Theorem C predicts SAT)
  V1  + u^1-endorsement of every acceptance on records supported in F (no layer atoms)
  V2  + u^1-endorsement also of acceptances out of the shifted members against the 16 base swaps
      (Theorem E predicts UNSAT; the core is printed)
"""
import sys, os, itertools, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP61_py'))
sys.path.insert(0, os.path.join(HERE, '..', 'PP56_py'))
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from pp50_lib_copy import cell_points, advice, mverts
from geom61 import EPS, U, B, sig, sgnv, field, CODE
from cells56 import rank

VALS = ('P', 'M', 'S', 'C')
VI = {v: k for k, v in enumerate(VALS)}
SSTAR = Fr(1, 10 ** 5)
TAU = (Fr(1), Fr(1, 10))
G = {'B': B, 'u': U}
NAMES = ['B', 'u']


def shifted(a, w, t):
    b = [a[i] * (1 + (t if i == w else 0)) for i in range(3)]
    s = sum(b)
    return tuple(x / s for x in b)


SH = [(w, k) for w in range(3) for k in range(len(TAU))]


def stability():
    S = sp.Symbol('s')
    base = []
    for nm in NAMES:
        a = G[nm]
        for m in mverts(EPS):
            base.append(([sp.Rational(m[j] * a[j]) for j in range(3)], False))
    base += [([1, 0, 0], False), ([0, 1, 0], False), ([0, 0, 1], False)]
    mov = []
    for (w, k) in SH:
        for m in mverts(EPS):
            v = [sp.Rational(m[j] * U[j]) for j in range(3)]
            v[w] = v[w] * (1 + sp.Rational(TAU[k]) * S)
            mov.append((v, True))
    bad = n = 0
    for (x, fx), (y, fy), (z, fz) in itertools.combinations(base + mov, 3):
        if not (fx or fy or fz):
            continue
        d = sp.expand(sp.Matrix([x, y, z]).det())
        if d == 0:
            continue
        p = sp.Poly(d, S)
        while p.eval(0) == 0:
            p = sp.Poly(sp.cancel(p.as_expr() / S), S)
        n += 1
        bad += 1 if int(p.count_roots(0, sp.Rational(SSTAR))) != 0 else 0
    return bad == 0, n


def build():
    models = dict(G)
    for (w, k) in SH:
        models['t%d%d' % (w, k)] = shifted(U, w, SSTAR * TAU[k])
    order = NAMES + ['t%d%d' % sk for sk in SH]
    cells = {}
    for g in cell_points(EPS, {k: list(v) for k, v in models.items()}):
        if any(x == 0 for x in g) or sum(g) <= 0:
            continue
        adv = tuple(CODE[advice(EPS, list(models[n]), g)] for n in order)
        cells.setdefault((sgnv(g), adv), tuple(g))
    return cells, order


def main():
    t0 = time.time()
    stab, ndet = stability()
    print('oriented matroid of {u, B, six shifted members} constant on (0, s*]: %s (%d determinants)' % (stab, ndet))
    assert stab
    cells, order = build()
    # base classes (u, B advice) and the kink cells
    base_cls = {}
    for (sv, adv), g in cells.items():
        base_cls.setdefault((sv, adv[:2]), g)
    Ep = [k for k in base_cls if sig(base_cls[k]) == 'Maj1' and k[1] == ('S', 'P')]
    Em = [k for k in base_cls if sig(base_cls[k]) == 'Min1' and k[1] == ('S', 'P')]
    assert len(Ep) == 1 and len(Em) == 1
    Ep, Em = Ep[0], Em[0]
    # atoms: F halves (4), then one atom per refined cell (u.g>0) and its antipode, restricted to cells where
    # some model differs (every other point is a common agreement point, irrelevant to every record)
    atoms = []   # (label, ray, role)
    for lab, k in (('Ep.a', Ep), ('Ep.b', Ep), ('Em.a', Em), ('Em.b', Em)):
        atoms.append((lab, base_cls[k], 'F', k))
    vals_of = {}   # atom index -> dict model -> value
    for (lab, g, role, k) in atoms:
        vals_of[len(vals_of)] = {n: k[1][NAMES.index(n)] if n in NAMES else 'P' for n in order}
    # shifted members agree with u on F (cores are at positive angular distance from the moving planes)
    for i in range(4):
        for n in order[2:]:
            vals_of[i][n] = vals_of[i]['u']
    for (sv, adv), g in sorted(cells.items()):
        if len(set(adv)) == 1:
            continue
        for side in (1, -1):
            gg = tuple(side * x for x in g)
            v = {n: (a if side == 1 else {'P': 'M', 'S': 'S'}[a]) for n, a in zip(order, adv)}
            role = 'L' if any(v[n] != v['u'] for n in order[2:]) else 'R'   # L = in some shift layer
            atoms.append(('c%s%s%s' % (''.join('+-'[x < 0] for x in sv), ''.join(adv), '+' if side == 1 else '-'), gg, role, (sv, adv[:2])))
            vals_of[len(vals_of)] = v
    nA = len(atoms)
    PHI = []
    for (lab, g, role, k) in atoms:
        ph = field(g) if sum(g) > 0 else {kk: vv for kk, vv in zip(('M', 'P', 'S', 'C'), (field(tuple(-x for x in g))[q] for q in ('P', 'M', 'S', 'C')))}
        PHI.append([tuple(ph[v][w] for v in VALS) for w in range(3)])
    RK = [[tuple(rank(v, list(g), w) for v in VALS) for w in range(3)] for (lab, g, role, k) in atoms]
    W = [(1, 0) if role == 'F' else ((0, 1) if role == 'L' else (None, None)) for (lab, g, role, k) in atoms]
    print('atoms: %d (4 F-halves, %d layer atoms, %d other disagreement atoms)' % (
        nA, sum(a[2] == 'L' for a in atoms), sum(a[2] == 'R' for a in atoms)))
    def src(n):
        return tuple(VI[vals_of[i][n]] for i in range(nA))
    Fidx = [0, 1, 2, 3]
    layer = {sk: [i for i in range(nA) if atoms[i][2] == 'L' and vals_of[i]['t%d%d' % sk] != vals_of[i]['u']] for sk in SH}
    M = {}          # name -> (vector, coherent, selected, fixed (s-independent))
    M['S:u'] = (src('u'), True, True, True)
    M['S:B'] = (src('B'), True, True, True)
    cu, cb = src('u'), src('B')
    subsets = [E for r in range(1, 5) for E in itertools.combinations(Fidx, r)]
    def put(vec, E, srcvec):
        v = list(vec)
        for i in E:
            v[i] = srcvec[i]
        return tuple(v)
    for E in subsets:
        tag = ''.join(atoms[i][0] for i in E)
        M['X:%s' % tag] = (put(cu, E, cb), False, False, True)
        M['Y:%s' % tag] = (put(cb, E, cu), False, False, True)
    for sk in SH:
        tn = 'S:t%d%d' % sk
        ct = src('t%d%d' % sk)
        M[tn] = (ct, True, True, False)
        L = layer[sk]
        half = L[:len(L) // 2]
        for E in subsets:
            tag = ''.join(atoms[i][0] for i in E)
            z = put(ct, E, cb)
            M['Z:%s|%s' % (tn, tag)] = (z, False, False, False)
            for Sn, S_ in (('L', L), ('Lh', half)):
                M['Z:%s|%s|%s' % (tn, tag, Sn)] = (put(z, S_, cu), False, False, False)
        M['Pc:%s' % tn] = (put(put(cb, Fidx, cu), L, ct), False, False, False)
    names = list(M)
    n = len(names)
    print('models: %d; shifted members %d; |layer| per shift: %s' % (n, len(SH), [len(layer[sk]) for sk in SH]))
    # records
    rid, recs = {}, []
    R = np.zeros((n, n), dtype=np.int64)
    for a in range(n):
        xa = M[names[a]][0]
        for b in range(n):
            xb = M[names[b]][0]
            rec = tuple((i, xa[i], xb[i]) for i in range(nA) if xa[i] != xb[i])
            if rec not in rid:
                rid[rec] = len(recs)
                recs.append(rec)
            R[a, b] = rid[rec]
    v = lambda r, i: int(3 * r + i + 1)
    cl = []
    for r, rec in enumerate(recs):
        for i in range(3):
            if not rec:
                cl.append(('REFL', (v(r, i),)))
                continue
            bt = [RK[p][i][x] < RK[p][i][y] for (p, x, y) in rec]
            if all(bt):
                cl.append(('G', (v(r, i),)))
            elif not any(bt):
                cl.append(('G', (-v(r, i),)))
    for a, Sn in enumerate(names):
        if not M[Sn][2]:
            continue
        for b, Xn in enumerate(names):
            if a == b:
                continue
            f, bk = R[a, b], R[b, a]
            cl.append(('DEF:%s|%s' % (Sn, Xn), tuple(v(f, i) for i in range(3))))
            if M[Xn][1]:
                for j in range(3):
                    cl.append(('UND:%s|%s' % (Sn, Xn), tuple(-v(bk, i) for i in range(3)) + (v(f, j),)))
            else:
                cl.append(('C:%s|%s' % (Sn, Xn), tuple(-v(bk, i) for i in range(3))))
    iu = names.index('S:u')
    for sk in SH:
        it = names.index('S:t%d%d' % sk)
        for b, Xn in enumerate(names):
            if M[Xn][3] and b != iu:
                for i in range(3):
                    cl.append(('SEC:t%d%d|%s|w%d' % (sk + (Xn, i + 1)), (-v(R[it, b], i), v(R[iu, b], i))))
    # TC on all ordered triples: generated lazily (CEGAR), every final model re-checked on ALL triples
    print('records %d, clauses %d  (%.0fs)' % (len(recs), len(cl), time.time() - t0))

    def V(rec):
        """u^1 value per world as (main, eps) pairs; None if the record touches an atom of unknown mass."""
        out = []
        for i in range(3):
            m0 = m1 = 0
            for (p, x, y) in rec:
                if W[p][0] is None:
                    return None
                d = PHI[p][i][y] - PHI[p][i][x]
                m0 += W[p][0] * d
                m1 += W[p][1] * d
            out.append((m0, m1))
        return out

    end1, end2 = [], []
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            rec = recs[R[a, b]]
            Vr = V(rec)
            if Vr is None:
                continue
            onlyF = all(atoms[p][2] == 'F' for (p, x, y) in rec)
            for i in range(3):
                if Vr[i] < (0, 0):
                    if onlyF:
                        end1.append(('END1', (-v(R[a, b], i),)))
                    if names[a].startswith('S:t') and names[b].startswith('X:'):
                        end2.append(('END2', (-v(R[a, b], i),)))
    from inst61 import Encoding, solve, check_assignment
    from run61b import minimal_core
    enc = Encoding.__new__(Encoding)
    enc.I = None
    enc.recs = recs
    enc.mat = {'all': (names, R)}
    enc.clauses = cl
    enc.nvars = 3 * len(recs)
    # REFEREE54 test: is there a model equal to R0 (w0 = 3) on every record not touching an e3-shifted model?
    free = set()
    for k, nm in enumerate(names):
        if nm in ('S:t20', 'S:t21'):
            free.update(R[k, :].tolist()); free.update(R[:, k].tolist())
    fix = []
    for r_, rec in enumerate(recs):
        if r_ in free or not rec:
            continue
        Vr = V(rec)
        if Vr is None:
            continue
        null = all(x == (0, 0) for x in Vr)
        for i in range(3):
            a_ = (i != 2) if null else (Vr[i] >= (0, 0))
            fix.append(('R0FIX', (v(r_, i) if a_ else -v(r_, i),)))
    print('REFEREE54: R0-fixing units %d; free records %d' % (len(fix), len(free)))
    for tag, extra in (('R0tight R0(w0=3) fixed off the rows and columns of the two e3-shifted members', fix),):
        st, val, tcs = solve(enc, extra=extra)
        import pickle
        pickle.dump(dict(tag=tag, st=st, val=(val if st == 'SAT' else None), names=names, vecs=[M[n][0] for n in names], flags={n: M[n][1:] for n in names}, atoms=[(a[0], a[1], a[2]) for a in atoms], R=R, recs=recs, PHI=PHI, W=W, extra=extra), open(os.path.join(HERE, 'corE2test_%s.pkl' % tag.split()[0]), 'wb'))
        print('\n[%s] %s   (lazy TC clauses: %d)' % (tag, st, len(tcs)))
        if st == 'SAT':
            bad = check_assignment(enc, val, extra)
            print('  exact re-check of every clause and of TC on all ordered triples: violations', len(bad))
            Rs = lambda a, b: ''.join(str(i + 1) for i in range(3) if not val[v(R[a, b], i)]) or '-'
            ix = names.index('X:Ep.aEp.bEm.aEm.b')
            iy = names.index('Y:Ep.aEp.bEm.aEm.b')
            ib = names.index('S:B')
            print('  R(rec(C_u -> X)) = {%s}; R(rec(X -> C_u)) = {%s}; R(rec(C_B -> Y)) = {%s}' % (Rs(iu, ix), Rs(ix, iu), Rs(ib, iy)))
            for sk in SH:
                it = names.index('S:t%d%d' % sk)
                acc = [i for i in range(3) if val[v(R[it, ix], i)]]
                Vr = V(recs[R[it, ix]])
                unf = [i + 1 for i in acc if Vr[i] < (0, 0)]
                print('  shift e%d, scale %s: R(rec(C_ut -> X)) = {%s}; accepted at %s; u1-unfavourable acceptances at %s; V = %s' % (
                    sk[0] + 1, TAU[sk[1]], Rs(it, ix), [i + 1 for i in acc], unf, [(int(a_), int(b_)) for a_, b_ in Vr]))
            cnt = {}
            for sk in SH:
                it = names.index('S:t%d%d' % sk)
                for b, Xn in enumerate(names):
                    if not Xn.startswith('Z:S:t%d%d|' % sk):
                        continue
                    Vr = V(recs[R[it, b]])
                    for i in range(3):
                        acc = val[v(R[it, b], i)]
                        key = ('acc' if acc else 'ref', 'fav' if Vr[i] > (0, 0) else ('null' if Vr[i] == (0, 0) else 'unfav'))
                        cnt[key] = cnt.get(key, 0) + 1
            print('  records out of shifted members to the splits Z, counted by (verdict, u1-sign at that world):', dict(sorted(cnt.items())))
            inc = sum(1 for a in range(n) for b in range(n) if a < b for i in range(3) if not val[v(R[a, b], i)] and not val[v(R[b, a], i)])
            print('  single-world incomparabilities (pairs x worlds):', inc)
        elif st == 'UNSAT':
            core, minimal = minimal_core(enc, extra, tcs)
            print('  minimal unsatisfiable core (%s), %d clauses:' % ('minimal' if minimal else 'reduced', len(core)))
            for t_, c in core:
                desc = []
                for l in c:
                    r_, i_ = divmod(abs(l) - 1, 3)
                    desc.append('%s[%s @w%d]' % ('' if l > 0 else 'NOT ', ','.join('%s:%s>%s' % (atoms[p][0][:14], VALS[x], VALS[y]) for (p, x, y) in recs[r_])[:160], i_ + 1))
                print('    %-34s %s' % (t_[:34], ' OR '.join(desc)))
    print('\n(%.0fs)' % (time.time() - t0))


if __name__ == '__main__':
    main()
