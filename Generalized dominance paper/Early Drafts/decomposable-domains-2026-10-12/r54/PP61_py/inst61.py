"""PP61 exact finite instance + relational SAT encoding + Lambda_w evaluator.

Models are value vectors over atoms (P, M, S, C relative to the atom's ray).
Records are canonical: sorted tuple of (atom id, old value, new value) over the atoms where the two
models differ, with sub-atoms merged back into their parent whenever the pair is the same on all of
them (so a record is literally the set {X != Y} with the two restrictions: exact (IB)).

Variables: v(r, i) = [r accepted at world i] = [i not in R(r)].
Clauses (all from the axioms of BRIEF54):
  G   strict guidance units (old side strictly better at i on every atom -> accept; worse -> refuse)
  DEF defence: OR_i v(rec(S -> X), i) for every selected S and every other model X
  UND undominatedness (coherent X): AND_i v(rec(X->S),i) -> AND_i v(rec(S->X),i)
  C   direct (C) (incoherent X): OR_i NOT v(rec(X -> S), i)
  TC  A<=B, B<=C, C<=A at i  ->  B<=A, C<=B, A<=C at i   (all ordered triples, generated lazily)
  SEC sections via actual pure-shift sequences (subsequence argument, see note):
      v(rec(C_{a_t} -> X), i) -> v(rec(C_a -> X), i) for every FIXED base model X.
"""
import sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'PP56_py'))
from fractions import Fraction as Fr
import numpy as np
from geom61 import Geometry, sig, VALS
from cells56 import rank

VI = {v: k for k, v in enumerate(VALS)}       # P0 M1 S2 C3
FLIP = {'P': 'M', 'M': 'P', 'S': 'S', 'C': 'C'}


class Atom:
    __slots__ = ('id', 'label', 'ray', 'key', 'role', 'shift', 'parent', 'phi', 'rk', 'sigma')

    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)


class Inst:
    def __init__(self, geo, swap_spec, pads=True, shifts=(), sub_swaps=None, pad_kinds=('bal2',), kinds=None):
        self.geo = geo
        self.pad_swaps = set()
        self.atoms = []
        for (lab, g, key, role) in geo.atoms:
            self._add_atom(lab, g, key, role, None, None, False)
        self.nbase = len(self.atoms)
        self.base_ids = list(range(self.nbase))
        self.by_label = {a.label: a.id for a in self.atoms}
        # base models
        self.models = {}       # name -> (vector over base atoms)
        self.coherent = {}
        self.selected = {}
        for nm in geo.names:
            self._add_model('S:' + nm, tuple(VI[geo.src_value(nm, a)] for a in geo.atoms), True, True)
        self.swaps = []        # (name, a, b, F)
        for (a, b, F) in swap_spec:
            n = self.add_swap(a, b, F)
            if n and kinds is not None and kinds.get((a, b, F)) in pad_kinds:
                self.pad_swaps.add(n)
        if pads:
            self._add_pads()
        self.base_models = list(self.models)
        # shifts
        self.subs = {}
        for s in shifts:
            self._add_shift(s, sub_swaps)

    # ---------- atoms ----------
    def _add_atom(self, lab, g, key, role, shift, parent, sigma):
        a = Atom(id=len(self.atoms), label=lab, ray=g, key=key, role=role, shift=shift, parent=parent,
                 phi=None, rk=None, sigma=sigma)
        ph = self.geo.phi(g)
        a.phi = [tuple(ph[v][w] for v in VALS) for w in range(3)]     # a.phi[w][value index]
        a.rk = [tuple(rank(v, list(g), w) for v in VALS) for w in range(3)]
        self.atoms.append(a)
        return a.id

    def core_atoms(self, key):
        c = self.geo.cname[key]
        return [self.by_label[c + '.c1'], self.by_label[c + '.c2']]

    def slab_group(self, key, slab='c1'):
        """all atoms whose union is the ORIGINAL slab (radial sub-slabs after splits)"""
        c = self.geo.cname[key] + '.' + slab
        return [a.id for a in self.atoms[:self.nbase] if a.label == c or (a.label.startswith(c) and a.label[len(c):].isalpha())]

    def _add_model(self, name, vec, coherent, selected):
        if name in self.models:
            return name
        self.models[name] = vec
        self.coherent[name] = coherent
        self.selected[name] = selected
        return name

    def src(self, nm):
        return self.models['S:' + nm]

    def add_swap(self, a, b, F, extra=None):
        """X = C_a[F -> C_b], F a tuple of base atom ids (core slabs)."""
        va, vb = list(self.src(a)), self.src(b)
        for p in F:
            va[p] = vb[p]
        name = 'X:%s>%s:%s' % (a, b, ','.join(self.atoms[p].label for p in F))
        if tuple(va) == self.src(a):
            return None
        self._add_model(name, tuple(va), False, False)
        self.swaps.append((name, a, b, tuple(F)))
        return name

    def _add_pads(self):
        """Guidance pads: C_a[E -> w-correct] and C_a[E -> contradiction] on silent core slabs E;
        also pads on single-piece swaps (PP30 / Prop K auxiliary models)."""
        geo = self.geo
        for nm in geo.names:
            v0 = self.src(nm)
            for key in geo.dis:
                Es = self.slab_group(key, 'c1')
                E = Es[0]
                if VALS[v0[E]] != 'S':
                    continue
                for w in range(3):
                    vv = list(v0)
                    for E in Es:
                        vv[E] = VI['P'] if self.atoms[E].ray[w] > 0 else VI['M']
                    self._add_model('PAD:%s:%s.c1:w%d' % (nm, geo.cname[key], w + 1), tuple(vv), False, False)
        for (name, a, b, F) in list(self.swaps):
            if len(F) != 2 or name not in self.pad_swaps:
                continue
            x = self.models[name]
            for E in F:
                if VALS[x[E]] != 'S':
                    continue
                for w in range(3):
                    vv = list(x)
                    vv[E] = VI['P'] if self.atoms[E].ray[w] > 0 else VI['M']
                    self._add_model('PAD:%s:%s:w%d' % (name, self.atoms[E].label, w + 1), tuple(vv), False, False)

    # ---------- shifts ----------
    def _add_shift(self, s, sub_swaps):
        nm, w = s
        geo = self.geo
        wedge, (stab, _) = geo.shift_wedge(nm, w)
        assert stab
        sig_ids, children = [], {}
        cv = {}
        for (key, side, vt) in wedge:
            g = geo.cls[key] if side == '+' else tuple(-x for x in geo.cls[key])
            if key in geo.dis:
                c = geo.cname[key]
                parent = self.by_label[c + ('.r' if side == '+' else '.n')]
            else:
                parent = None
            lab = 'sig[%s,e%d]:%s%s>%s' % (nm, w + 1, geo.cname[key], side, vt)
            aid = self._add_atom(lab, g, key, 'sigma', s, parent, True)
            sig_ids.append(aid)
            cv[aid] = VI[vt]
            if parent is not None:
                children.setdefault(parent, []).append(aid)
        # p minus sigma atoms
        minus = {}
        for p, ch in children.items():
            pa = self.atoms[p]
            minus[p] = self._add_atom('%s\\sig[%s,e%d]' % (pa.label, nm, w + 1), pa.ray, pa.key, 'minus', s, p, False)
        loc = self.base_ids + sig_ids          # local coordinates: base atoms then sigma atoms
        # extend base models: sigma atom value = parent's value, or common source value (agreement class)
        def ext(vec):
            out = list(vec)
            for aid in sig_ids:
                at = self.atoms[aid]
                if at.parent is not None:
                    out.append(vec[at.parent])
                else:
                    k = at.key
                    v = k[1][0]
                    if sum(at.ray) < 0:
                        v = FLIP[v]
                    out.append(VI[v])
            return tuple(out)
        mods = {n: ext(v) for n, v in self.models.items()}
        coh, sel = dict(self.coherent), dict(self.selected)
        newn = []
        ca = mods['S:' + nm]
        cat = list(ca)
        for j, aid in enumerate(sig_ids):
            cat[self.nbase + j] = cv[aid]
        cat = tuple(cat)
        tn = 'S:%s_t(e%d)' % (nm, w + 1)
        mods[tn] = cat
        coh[tn] = sel[tn] = True
        newn.append(tn)
        for (name, a, b, F) in self.swaps:
            if a != nm or (sub_swaps is not None and name not in sub_swaps):
                continue
            # X_t = C_{a_t}[F -> C_b]
            xt = list(cat)
            cb = mods['S:' + b]
            for p in F:
                xt[p] = cb[p]
            n1 = 'Xt:%s|%s' % (tn, name)
            mods[n1] = tuple(xt)
            coh[n1] = sel[n1] = False
            newn.append(n1)
            # P = C_b[F -> C_a, sigma -> C_{a_t}]   (common-context copy of rec(C_{a_t} -> X))
            pp = list(cb)
            for p in F:
                pp[p] = ca[p]
            for j in range(len(sig_ids)):
                pp[self.nbase + j] = cat[self.nbase + j]
            n2 = 'Pc:%s|%s' % (tn, name)
            mods[n2] = tuple(pp)
            coh[n2] = sel[n2] = False
            newn.append(n2)
        self.subs[s] = dict(sig=sig_ids, children=children, minus=minus, loc=loc, models=mods,
                            coherent=coh, selected=sel, new=newn, tname=tn)

    # ---------- records ----------
    def record(self, x, y, sub=None):
        """canonical record of (x -> y); x, y value vectors in local coordinates of sub (or base)."""
        if sub is None:
            return tuple((p, x[p], y[p]) for p in range(self.nbase) if x[p] != y[p])
        S = self.subs[sub]
        nb = self.nbase
        out = []
        sig = S['sig']
        pos = {aid: nb + j for j, aid in enumerate(sig)}
        ch = S['children']
        for p in range(nb):
            if p in ch:
                pr = (x[p], y[p])
                if all((x[pos[c]], y[pos[c]]) == pr for c in ch[p]):
                    if pr[0] != pr[1]:
                        out.append((p, pr[0], pr[1]))
                else:
                    if pr[0] != pr[1]:
                        out.append((S['minus'][p], pr[0], pr[1]))
                    for c in ch[p]:
                        if x[pos[c]] != y[pos[c]]:
                            out.append((c, x[pos[c]], y[pos[c]]))
            elif x[p] != y[p]:
                out.append((p, x[p], y[p]))
        for c in sig:
            if self.atoms[c].parent is None and x[pos[c]] != y[pos[c]]:
                out.append((c, x[pos[c]], y[pos[c]]))
        return tuple(sorted(out))

    def guidance(self, rec, i):
        """+1: accepted by strict guidance (old strictly better on every atom); -1: refused; 0: mixed."""
        if not rec:
            return 1
        better = worse = False
        for (p, x, y) in rec:
            rx, ry = self.atoms[p].rk[i][x], self.atoms[p].rk[i][y]
            if rx < ry:
                better = True
            else:
                worse = True
        if better and not worse:
            return 1
        if worse and not better:
            return -1
        return 0

    def rtype(self, rec, mode):
        """combinatorial type of a record (for uniformity hypotheses)."""
        if mode == 'sig':
            return tuple(sorted(set((sig(self.atoms[p].ray) if sum(self.atoms[p].ray) > 0 else
                                     'n' + sig(tuple(-c for c in self.atoms[p].ray)), x, y) for (p, x, y) in rec)))
        if mode == 'class':
            return tuple(sorted(set((self.atoms[p].key, sum(self.atoms[p].ray) > 0, x, y) for (p, x, y) in rec)))
        raise ValueError


class Encoding:
    """Builds records/variables/clauses for base instance + all shift sub-instances."""

    def __init__(self, inst):
        self.I = inst
        self.rid = {}
        self.recs = []
        self.clauses = []              # list of (tag, clause)
        self.groups = []               # model-name lists per instance (for TC)
        self.mat = {}                  # instance label -> (names, rec-id matrix)
        self._build()

    def r(self, rec):
        if rec not in self.rid:
            self.rid[rec] = len(self.recs)
            self.recs.append(rec)
        return self.rid[rec]

    def v(self, rid, i):
        return int(3 * rid + i + 1)

    def _matrix(self, label, names, vecs, sub, nbase_block=0):
        n = len(names)
        M = np.zeros((n, n), dtype=np.int64)
        k = nbase_block
        if k:
            M[:k, :k] = self.mat['base'][1]
        for a in range(n):
            for b in range(n):
                if a < k and b < k:
                    continue
                M[a, b] = self.r(self.I.record(vecs[a], vecs[b], sub))
        self.mat[label] = (names, M)

    def _build(self):
        I = self.I
        names0 = list(I.base_models)
        self._matrix('base', names0, [I.models[n] for n in names0], None)
        for s, S in I.subs.items():
            nm = list(I.base_models) + S['new']
            self._matrix(s, nm, [S['models'][n] for n in nm], s, nbase_block=len(I.base_models))
        # guidance units
        for rid, rec in enumerate(self.recs):
            for i in range(3):
                g = self.I.guidance(rec, i)
                if g == 1:
                    self.clauses.append(('G', (self.v(rid, i),)))
                elif g == -1:
                    self.clauses.append(('G', (-self.v(rid, i),)))
        # selected-model clauses
        for label, (names, M) in self.mat.items():
            if label == 'base':
                coh, sel = I.coherent, I.selected
            else:
                coh, sel = I.subs[label]['coherent'], I.subs[label]['selected']
            for a, Sn in enumerate(names):
                if not sel[Sn]:
                    continue
                for b, Xn in enumerate(names):
                    if a == b:
                        continue
                    f, bk = M[a, b], M[b, a]
                    tag = ('%s|%s' % (Sn, Xn))
                    self.clauses.append(('DEF:' + tag, tuple(self.v(f, i) for i in range(3))))
                    if coh[Xn]:
                        for j in range(3):
                            self.clauses.append(('UND:' + tag, tuple(-self.v(bk, i) for i in range(3)) + (self.v(f, j),)))
                    else:
                        self.clauses.append(('C:' + tag, tuple(-self.v(bk, i) for i in range(3))))
        # sections via shift subsequences
        for s, S in I.subs.items():
            names, M = self.mat[s]
            ia = names.index('S:' + s[0])
            it = names.index(S['tname'])
            for b, Xn in enumerate(names):
                if Xn not in I.models or b in (ia, it):
                    continue          # only fixed (t-independent) base rivals
                for i in range(3):
                    self.clauses.append(('SEC:%s|%s|w%d' % (S['tname'], Xn, i + 1),
                                         (-self.v(M[it, b], i), self.v(M[ia, b], i))))
        self.nvars = 3 * len(self.recs)

    # ---------- lazy TC ----------
    def tc_violations(self, assign, limit=20000):
        """assign: function var -> bool.  Returns list of TC clauses violated by the assignment."""
        out = []
        A = np.array([[assign(self.v(r, i)) for i in range(3)] for r in range(len(self.recs))], dtype=bool)
        for label, (names, M) in self.mat.items():
            for i in range(3):
                Ai = A[M, i]
                Ai = Ai.copy()
                np.fill_diagonal(Ai, True)
                S = Ai & ~Ai.T                    # x <= y strictly (reverse refused)
                AA = (Ai.astype(np.int32) @ Ai.astype(np.int32))
                V = S & (AA.T > 0)
                xs, ys = np.nonzero(V)
                for x, y in zip(xs, ys):
                    zs = np.nonzero(Ai[y, :] & Ai[:, x])[0]
                    for z in zs[:2]:
                        lits = (-self.v(M[x, y], i), -self.v(M[y, z], i), -self.v(M[z, x], i))
                        for rev in (M[y, x], M[z, y], M[x, z]):
                            out.append(('TC', lits + (self.v(rev, i),)))
                    if len(out) > limit:
                        return out
        return out

    def tc_check_full(self, acc):
        """acc[r][i] boolean; exact check of TC on every ordered triple (numpy), returns #violations."""
        A = np.array(acc, dtype=bool)
        bad = 0
        for label, (names, M) in self.mat.items():
            for i in range(3):
                Ai = A[M, i].copy()
                np.fill_diagonal(Ai, True)
                S = Ai & ~Ai.T
                AA = (Ai.astype(np.int32) @ Ai.astype(np.int32))
                bad += int((S & (AA.T > 0)).sum())
        return bad


def solve(enc, extra=(), assumptions=(), max_rounds=400, verbose=False, solver_name='cadical153', seed_tc=(), phases=None):
    """CEGAR loop: SAT on non-TC clauses, add violated TC clauses until none.  Returns (status, model, tc_clauses)."""
    from pysat.solvers import Solver
    S = Solver(name=solver_name)
    for tag, c in enc.clauses:
        S.add_clause(list(c))
    for tag, c in extra:
        S.add_clause(list(c))
    tcs = list(seed_tc)
    for tag, c in tcs:
        S.add_clause(list(c))
    if phases is not None:
        S.set_phases([int(l) for l in phases])
    for rnd in range(max_rounds):
        ok = S.solve(assumptions=list(assumptions))
        if not ok:
            core = S.get_core()
            S.delete()
            return 'UNSAT', core, tcs
        model = S.get_model()
        val = np.zeros(max(enc.nvars, max(abs(l) for l in model)) + 1, dtype=bool)
        for l in model:
            val[abs(l)] = l > 0
        viol = enc.tc_violations(lambda x: val[x])
        if verbose:
            print('   round', rnd, 'TC violations added:', len(viol), flush=True)
        if not viol:
            S.delete()
            return 'SAT', val, tcs
        for tag, c in viol:
            S.add_clause(list(c))
        tcs += viol
    S.delete()
    return 'UNKNOWN', None, tcs


def check_assignment(enc, val, extra=()):
    """exact re-check of every clause + full TC; returns list of violated tags."""
    bad = []
    for tag, c in list(enc.clauses) + list(extra):
        if not any((val[abs(l)] if l > 0 else not val[abs(l)]) for l in c):
            bad.append(tag)
    acc = [[bool(val[enc.v(r, i)]) for i in range(3)] for r in range(len(enc.recs))]
    nt = enc.tc_check_full(acc)
    if nt:
        bad.append('TC x%d' % nt)
    return bad


# ---------- Lambda_w (PP56 relation with atom weights w; sigma atoms infinitesimal) ----------
def lambda_assignment(enc, w):
    """w: dict base atom id -> positive INTEGER weight (int q|g| over the atom; any positive vector is
    realisable by q since q is free per atom).  sigma atoms carry mass eps*1 (t -> 0+), so every level
    value is a pair (main, eps-coefficient) compared lexicographically.
    Levels: 0 = whole space; then one level per base atom p (the set p, which contains its sigma
    children); then one level per sigma atom.  (A countable separating family listed first; PP56 Thm L.)
    Returns val array of the eventual (t -> 0+) verdicts."""
    I = enc.I
    val = np.zeros(enc.nvars + 1, dtype=bool)
    nch = {}
    for s, S in I.subs.items():
        for p, ch in S['children'].items():
            nch[S['minus'][p]] = len(ch)
    W = []
    LP = []
    for at in I.atoms:
        if at.sigma:
            W.append((0, 1))
        elif at.role == 'minus':
            W.append((int(w[at.parent]), -nch[at.id]))
        else:
            W.append((int(w[at.id]), 0))
        LP.append(at.parent if (at.role == 'minus' or (at.sigma and at.parent is not None)) else at.id)
    PHI = [at.phi for at in I.atoms]
    BIG = 10 ** 7
    for rid, rec in enumerate(enc.recs):
        for i in range(3):
            t0 = t1 = 0
            for (p, x, y) in rec:
                ph = PHI[p][i]
                d = ph[y] - ph[x]
                wm, we = W[p]
                t0 += wm * d
                t1 += we * d
            if (t0, t1) != (0, 0):
                val[3 * rid + i + 1] = (t0, t1) > (0, 0)
                continue
            levels = {}
            for (p, x, y) in rec:
                ph = PHI[p][i]
                d = ph[y] - ph[x]
                wm, we = W[p]
                L = levels.setdefault(LP[p], [0, 0])
                L[0] += wm * d
                L[1] += we * d
                if I.atoms[p].sigma:
                    levels.setdefault(BIG + p, [0, 0])[1] += d
            ok = True
            for k in sorted(levels):
                comp = tuple(levels[k])
                if comp != (0, 0):
                    ok = comp > (0, 0)
                    break
            val[3 * rid + i + 1] = ok
    return val
