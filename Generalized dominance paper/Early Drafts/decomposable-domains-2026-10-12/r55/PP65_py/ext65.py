"""PP65 ext65: exact check of the forced verdict pattern at the first nontrivial extension
(PP65 Prop 2.4) on an abstract cell instance.  Pure axioms only: weak/strict (G), (IB) (verdicts
are variables of RECORDS), (TC) on every ordered triple at every world, defence of T on {1,2,3}
and of the edge defender Cp on {1,2}, direct (C) and undominatedness for T and Cp.
No sections (there are no indices here); no field, no endorsement.

Worlds 1,2,3 (i=1, j=2, k=3).  Advice: 'A' (majority answer), 'B' (minority answer), 'S'.
Cell classes: class m = odd world m.  On class m, A is correct at the two worlds != m, B at m.
Cells (all inside Sil(T), so T = S on all of them):
  P1,P2,P3 : class 3 (worlds 1,2 agree)   Cp = A    -- the nested sets E are unions of these
  R1       : class 1                      Cp = A   (wrong at world 1)
  R2a      : class 2                      Cp = A   (wrong at world 2)
  R2b      : class 2                      Cp = B   (right at world 2 only)
So Cp is pointwise better than T at neither world 1 nor world 2 (no guidance shortcut).
Cp is the edge model on [e1,e2]: it must answer A on class 3 (PP65 Lemma 2.1).
Models: all 64 splices  T on some cells, Cp on the others.  T and Cp coherent, all others
incoherent (non-conic splices, Lemma H).
Run:  python3 -I -B ext65.py
"""
import itertools, sys
from pysat.solvers import Cadical153

CELLS = ['P1', 'P2', 'P3', 'R1', 'R2a', 'R2b']
CLS = {'P1': 3, 'P2': 3, 'P3': 3, 'R1': 1, 'R2a': 2, 'R2b': 2}
T0 = {c: 'S' for c in CELLS}
CP = {'P1': 'A', 'P2': 'A', 'P3': 'A', 'R1': 'A', 'R2a': 'A', 'R2b': 'B'}
W = (1, 2, 3)


def rank(c, adv, w):
    if adv == 'S':
        return 1
    corr = 'B' if CLS[c] == w else 'A'
    return 0 if adv == corr else 2


def model(sub):
    return tuple(CP[c] if c in sub else T0[c] for c in CELLS)


MODELS = []
for r in range(len(CELLS) + 1):
    for sub in itertools.combinations(CELLS, r):
        MODELS.append(model(set(sub)))
MODELS = sorted(set(MODELS))
T = model(set())
C = model(set(CELLS))
COH = {T, C}


def rec(X, Y):
    return tuple((CELLS[n], X[n], Y[n]) for n in range(len(CELLS)) if X[n] != Y[n])


VAR = {}


def v(r, w):
    key = (r, w)
    if key not in VAR:
        VAR[key] = len(VAR) + 1
    return VAR[key]


def guid(r, w):
    """True if the record's old side is pointwise no worse at w (non-empty r)."""
    return all(rank(c, o, w) <= rank(c, n, w) for (c, o, n) in r)


def inv(r):
    return tuple((c, n, o) for (c, o, n) in r)


def base_clauses(hyp=True):
    cl = []
    recs = set()
    for X in MODELS:
        for Y in MODELS:
            if X != Y:
                recs.add(rec(X, Y))
    for r in recs:
        for w in W:
            if guid(r, w):
                cl.append([v(r, w)])
                cl.append([-v(inv(r), w)])
    for X, Y, Z in itertools.permutations(MODELS, 3):
        a, b, c = rec(X, Y), rec(Y, Z), rec(Z, X)
        for w in W:
            for rr in (inv(a), inv(b), inv(c)):
                cl.append([-v(a, w), -v(b, w), -v(c, w), v(rr, w)])
    for X in MODELS:
        if X != T:
            cl.append([v(rec(T, X), w) for w in W])
        if X != C:
            cl.append([v(rec(C, X), w) for w in (1, 2)])
    for S_ in (T, C):
        for X in MODELS:
            if X == S_:
                continue
            if X not in COH:
                cl.append([-v(rec(X, S_), w) for w in W])
    for S_, X in ((T, C), (C, T)):
        for w2 in W:
            cl.append([-v(rec(X, S_), w) for w in W] + [v(rec(S_, X), w2)])
    if hyp:
        XE = model({'P1', 'P2', 'P3'})
        cl.append([v(rec(C, XE), 1)])
        cl.append([v(rec(C, XE), 2)])
    return cl


def name(M):
    if M == T:
        return 'T'
    if M == C:
        return 'Cp'
    on = [CELLS[n] for n in range(len(CELLS)) if M[n] != T0[CELLS[n]]]
    off = [c for c in CELLS if c not in on]
    if set(on) <= {'P1', 'P2', 'P3'}:
        return 'X[' + ''.join(on) + ']'
    if set(off) <= {'P1', 'P2', 'P3'}:
        return 'Cp[' + ''.join(off) + '->S]'
    return None


def main():
    cl = base_clauses(hyp=True)
    s = Cadical153(bootstrap_with=cl)
    ok = s.solve()
    print('instance: %d models, %d record-world variables, %d clauses' % (len(MODELS), len(VAR), len(cl)))
    print('base + hypothesis (Cp accepts X[P1P2P3] at worlds 1 and 2): %s' % ('SAT' if ok else 'UNSAT'))
    assert ok
    named = [M for M in MODELS if name(M) is not None]
    forced = []
    for X in named:
        for Y in named:
            if X == Y or (X not in (T, C) and Y not in (T, C)):
                continue
            r = rec(X, Y)
            for w in W:
                lit = v(r, w)
                pos = s.solve(assumptions=[lit])
                neg = s.solve(assumptions=[-lit])
                if pos and not neg:
                    forced.append((name(X), '<=_%d' % w, name(Y), 'ACCEPT', guid(r, w)))
                elif neg and not pos:
                    forced.append((name(X), '<=_%d' % w, name(Y), 'REFUSE', guid(inv(r), w)))
    print('forced literals with T or Cp on one side (G = forced by guidance alone):')
    for f in forced:
        tag = 'G' if f[4] else 'derived'
        print('  %-14s %s %-14s %s  [%s]' % (f[0], f[1], f[2], f[3], tag))
    # checks of PP65 Prop 2.4 items
    def forced_ref(X, Y, w):
        return not s.solve(assumptions=[v(rec(X, Y), w)])

    def forced_acc(X, Y, w):
        return not s.solve(assumptions=[-v(rec(X, Y), w)])
    X = {k: model(set(k)) for k in [(), ('P1',), ('P1', 'P2'), ('P1', 'P2', 'P3'), ('P2',), ('P1', 'P3')]}
    full = ('P1', 'P2', 'P3')
    res = []
    res.append(('(a) T refuses Cp at 1 and 2', forced_ref(T, C, 1) and forced_ref(T, C, 2)))
    res.append(('(b) T accepts Cp at 3', forced_acc(T, C, 3)))
    # (c) needs an intermediate E (E'' < E < E'), i.e. E'\E'' splittable; on atoms: >= 2 atoms, or E''=E'
    split = [k for k in X if len(full) - len(k) >= 2 or k == full]
    res.append(('(c) Cp refuses X_E\'\' at 3 whenever E\'\\E\'\' is splittable, and at E\'\'=E\'',
                all(forced_ref(C, X[k], 3) for k in split)))
    res.append(('(c\') atom artefact: with no intermediate E (E\'\'=P1P2) the refusal is NOT forced',
                not forced_ref(C, X[('P1', 'P2')], 3)))
    res.append(('(d) X_E refuses Cp at 1,2 for E strictly inside E\'',
                all(forced_ref(X[k], C, 1) and forced_ref(X[k], C, 2) for k in X if k != full)))
    res.append(('(e) X_E accepts Cp at 3 (= T <=_3 Cp[E->S]) for E strictly inside E\'',
                all(forced_acc(X[k], C, 3) for k in X if k != full)))
    for t, b in res:
        print('  %-75s %s' % (t, 'PASS' if b else 'FAIL'))
    # control: without the hypothesis nothing of (a)-(e) is forced
    s2 = Cadical153(bootstrap_with=base_clauses(hyp=False))
    ctrl = s2.solve(assumptions=[v(rec(T, C), 1)]) and s2.solve(assumptions=[v(rec(C, X[full]), 3)])
    print('  control without hypothesis: T<=_1 Cp and Cp<=_3 X_E\' are each satisfiable: %s' % ('PASS' if ctrl else 'FAIL'))
    # PP65 Prop 4.1: committing T <=_1 Cp and T <=_2 Cp (each legal alone) kills Cp's defence vs X_E'
    one1 = s2.solve(assumptions=[v(rec(T, C), 1)])
    one2 = s2.solve(assumptions=[v(rec(T, C), 2)])
    both = s2.solve(assumptions=[v(rec(T, C), 1), v(rec(T, C), 2)])
    p41 = one1 and one2 and not both
    print('  Prop 4.1: T<=_1 Cp alone SAT, T<=_2 Cp alone SAT, both UNSAT: %s' % ('PASS' if p41 else 'FAIL'))
    allok = all(b for _, b in res) and ctrl and p41
    print('ALL PASS' if allok else 'SOME FAIL')


if __name__ == '__main__':
    main()
