"""REFEREE round 56 (REFEREE_round55.md): independent SAT/closure checks for PP65 Props 2.3, 4.1,
the referee's generalised trap, the audit's signed-propagation derivation, and the
accumulation (limit-stage) counterexample.  Own encoding; nothing imported from PP65_py.

Abstract cell instances.  A cell has a sign pattern: the set COR of worlds at which the answer '+'
is correct ('-' is correct at the complement).  Advice values '+', '-', 'S'.  Ranks: correct 0,
silent 1, wrong 2.  Models = all splices of two base models T and D (every cell takes T's or D's
advice).  Verdict variables are indexed by (record, world): (IB) is built in.

Axiom clauses (on the whole splice universe):
  guidance  : old side weakly better at w  => accepted; new side strictly better => refused;
  (TC)      : every ordered triple of distinct models, every world, all three reverses;
  defence   : each selected model S, against every X != S, on its support worlds;
  direct (C): each selected S, against every incoherent X: not all-world X <= S;
  undominated: each selected S, against every coherent X: all-world X <= S  =>  all-world S <= X.
Closure test ((I2)-(I4) of PP64, no defence): Acc = guidance + commitments, Ref = guidance refusals,
P = selected models; close under (TC)-reverses, rule III, rule IV; report conflicts.
Run: python3 -I -B trap_ref.py
"""
import itertools
from pysat.solvers import Cadical153, Glucose4

W = (1, 2, 3)


class Inst:
    def __init__(self, cells, T, D):
        self.cells = list(cells)            # name -> COR set
        self.COR = cells
        self.Tv, self.Dv = T, D
        n = len(self.cells)
        self.models = sorted(set(tuple(D[c] if bit else T[c] for c, bit in zip(self.cells, bits))
                                 for bits in itertools.product((0, 1), repeat=n)))
        self.var = {}

    def M(self, on=()):
        return tuple(self.Dv[c] if c in on else self.Tv[c] for c in self.cells)

    def rank(self, c, a, w):
        if a == 'S':
            return 1
        ok = (w in self.COR[c]) == (a == '+')
        return 0 if ok else 2

    def rec(self, X, Y):
        return tuple((c, x, y) for c, x, y in zip(self.cells, X, Y) if x != y)

    @staticmethod
    def inv(r):
        return tuple((c, y, x) for c, x, y in r)

    def v(self, r, w):
        return self.var.setdefault((r, w), len(self.var) + 1)

    def weak(self, r, w):      # old side weakly w-better
        return all(self.rank(c, x, w) <= self.rank(c, y, w) for c, x, y in r)

    def clauses(self, selected, coherent):
        cl = []
        recs = {self.rec(X, Y) for X in self.models for Y in self.models if X != Y}
        for r in recs:
            for w in W:
                if self.weak(r, w):
                    cl.append([self.v(r, w)])
                    cl.append([-self.v(self.inv(r), w)])
        for X, Y, Z in itertools.permutations(self.models, 3):
            a, b, c = self.rec(X, Y), self.rec(Y, Z), self.rec(Z, X)
            for w in W:
                va, vb, vc = self.v(a, w), self.v(b, w), self.v(c, w)
                for rr in (a, b, c):
                    cl.append([-va, -vb, -vc, self.v(self.inv(rr), w)])
        for S_, sup in selected:
            for X in self.models:
                if X == S_:
                    continue
                cl.append([self.v(self.rec(S_, X), w) for w in sup])
                if X not in coherent:
                    cl.append([-self.v(self.rec(X, S_), w) for w in W])
                else:
                    for w2 in W:
                        cl.append([-self.v(self.rec(X, S_), w) for w in W] + [self.v(self.rec(S_, X), w2)])
        return cl

    def closure(self, commits, registered, coherent):
        """PP64 (I2)-(I4) closure.  commits: list of (record, world) acceptances."""
        acc, ref = set(), set()
        recs = {self.rec(X, Y) for X in self.models for Y in self.models if X != Y}
        for r in recs:
            for w in W:
                if self.weak(r, w):
                    acc.add((r, w))
                    ref.add((self.inv(r), w))
        acc |= set(commits)
        P = set(registered)
        changed = True
        while changed:
            changed = False
            for X, Y, Z in itertools.permutations(self.models, 3):
                a, b, c = self.rec(X, Y), self.rec(Y, Z), self.rec(Z, X)
                for w in W:
                    if (a, w) in acc and (b, w) in acc and (c, w) in acc:
                        for rr in (a, b, c):
                            if (self.inv(rr), w) not in acc:
                                acc.add((self.inv(rr), w)); changed = True
            for N in list(P):
                for X in self.models:
                    if X != N and all((self.rec(X, N), w) in acc for w in W):
                        for w in W:
                            if (self.rec(N, X), w) not in acc:
                                acc.add((self.rec(N, X), w)); changed = True
                        if X not in P:
                            P.add(X); changed = True
        conflict = acc & ref
        F2 = [X for X in P if X not in coherent]
        return conflict, F2


ok = True


def report(name, b):
    global ok
    ok &= bool(b)
    print('  %-92s %s' % (name, 'PASS' if b else 'FAIL'))


def sat(cl, assum):
    s = Cadical153(bootstrap_with=cl)
    r = s.solve(assumptions=assum)
    s.delete()
    return r


# ------------------------------------------------------------------------------------------
# Instance B: a 3-mixed precise edge model D' (geometry of edge_ref.py, worlds 1-based).
#   P1,P2,P3 : Q_3 points (+ correct at {1,2}); T silent, D' = +          (E' = P1 u P2 u P3)
#   c1       : + correct at {1,3}; T silent, D' = +   (D' better at 1,3, worse at 2)
#   c2       : + correct at {2,3}; T silent, D' = +   (D' better at 2,3, worse at 1)
#   c3       : + correct at {3};   T = +,   D' = -    (D' better at 1,2, worse at 3)
# ------------------------------------------------------------------------------------------
print('Instance B (3-mixed edge model D\'), 64 splices')
cellsB = {'P1': {1, 2}, 'P2': {1, 2}, 'P3': {1, 2}, 'c1': {1, 3}, 'c2': {2, 3}, 'c3': {3}}
TB = {'P1': 'S', 'P2': 'S', 'P3': 'S', 'c1': 'S', 'c2': 'S', 'c3': '+'}
DB = {'P1': '+', 'P2': '+', 'P3': '+', 'c1': '+', 'c2': '+', 'c3': '-'}
B = Inst(cellsB, TB, DB)
T, D = B.M(), B.M(cellsB)
coh = {T, D}
sel = [(T, W), (D, (1, 2))]
clB = B.clauses(sel, coh)
X = lambda *on: B.M(on)
XEp = X('P1', 'P2', 'P3')
a = {w: B.v(B.rec(T, D), w) for w in W}
b = {w: B.v(B.rec(D, XEp), w) for w in W}
report('base SAT', sat(clB, []))
# Prop 4.1 mechanism
report('Prop 4.1: T<=_1 D\' alone SAT; T<=_2 D\' alone SAT; both UNSAT',
       sat(clB, [a[1]]) and sat(clB, [a[2]]) and not sat(clB, [a[1], a[2]]))
conf, F2 = B.closure([(B.rec(T, D), 1), (B.rec(T, D), 2)], {T, D}, coh)
report('Prop 4.1: (I2)-(I4) closure of {T<=_1 D\', T<=_2 D\'} is clean (rule III does not fire)', not conf and not F2)
# audit's signed propagation by unit propagation alone
g = Glucose4(bootstrap_with=clB)
st, lits = g.propagate(assumptions=[a[1]])
L = set(lits)
report('signed propagation: unit propagation from a_1 gives -b_1, b_2, -a_2 (no search)',
       st and (-b[1]) in L and b[2] in L and (-a[2]) in L)
st0, lits0 = g.propagate(assumptions=[])
report('  ... and without a_1 none of a_1, a_2, b_1, b_2 is fixed by propagation',
       all(x not in set(lits0) and -x not in set(lits0) for x in (a[1], a[2], b[1], b[2])))
g.delete()
# Prop 2.3 forced literals under hypothesis (a) at E'
hyp = [b[1], b[2]]
s = Cadical153(bootstrap_with=clB + [[h] for h in hyp])
report('Prop 2.3 hypothesis (D\' accepts X_E\' at 1 and 2) SAT', s.solve())


def forced(lit):
    return not s.solve(assumptions=[-lit])


report('Prop 2.3(b): D\' !<=_3 X_E\'; T !<=_1 D\'; T !<=_2 D\'; T <=_3 D\'',
       forced(-b[3]) and forced(-a[1]) and forced(-a[2]) and forced(a[3]))
subsE = [(), ('P1',), ('P2',), ('P1', 'P2'), ('P1', 'P3')]
okc = all(forced(-B.v(B.rec(X(*e), D), 1)) and forced(-B.v(B.rec(X(*e), D), 2)) and forced(B.v(B.rec(X(*e), D), 3))
          for e in subsE)
report('Prop 2.3(c): X_E !<=_1,2 D\', X_E <=_3 D\' for E strictly inside E\'', okc)
okd = all(forced(-B.v(B.rec(D, X(*e)), 3)) for e in [(), ('P1',), ('P2',), ('P3',)])
report('Prop 2.3(d): D\' !<=_3 X_E\'\' whenever E\'\\E\'\' contains >= 2 atoms', okd)
report('Prop 2.3(d) needs an intermediate set: D\' !<=_3 X_{P1P2} is NOT forced',
       not forced(-B.v(B.rec(D, X('P1', 'P2')), 3)))
s.delete()

# ------------------------------------------------------------------------------------------
# Instance C: PP64's kind of edge defender, weakly 3-worse than T (Lemma 4.2 pattern).
#   E   : + correct at {1,2}; T silent, D = +    (D better at 1,2, worse at 3)
#   W1a, W1b : + correct at {1,3}; T = +, D silent (D worse at 1 and 3, better at 2)
#   W2a, W2b : + correct at {2,3}; T = +, D silent (D worse at 2 and 3, better at 1)
# ------------------------------------------------------------------------------------------
print('Instance C (edge model weakly 3-worse than T, as PP64 Lemma 4.2), 32 splices')
cellsC = {'E': {1, 2}, 'W1a': {1, 3}, 'W1b': {1, 3}, 'W2a': {2, 3}, 'W2b': {2, 3}}
TC_ = {'E': 'S', 'W1a': '+', 'W1b': '+', 'W2a': '+', 'W2b': '+'}
DC = {'E': '+', 'W1a': 'S', 'W1b': 'S', 'W2a': 'S', 'W2b': 'S'}
C = Inst(cellsC, TC_, DC)
T, D = C.M(), C.M(cellsC)
coh = {T, D}
report('D weakly 3-worse than T', C.weak(C.rec(T, D), 3) and not C.weak(C.rec(D, T), 3))
clC = C.clauses([(T, W), (D, (1, 2))], coh)
aC = {w: C.v(C.rec(T, D), w) for w in W}
conf, F2 = C.closure([(C.rec(T, D), 1), (C.rec(T, D), 2)], {T, D}, coh)
report('PP65 Prop 4.1 version is CAUGHT by (H4)-closure here (rule III fires, guidance reverse)', bool(conf))
Z1, Z2 = C.M(('W1a',)), C.M(('W2a',))        # Z_w = T[G_w -> D], G_1 = W1a, G_2 = W2a
r1, r2 = C.rec(Z1, D), C.rec(Z2, D)
report('r_1 = rec(T[W1a->D], D) and r_2 = rec(T[W2a->D], D) are mixed at worlds 1 and 2',
       all(not C.weak(r, w) and not C.weak(C.inv(r), w) for r in (r1, r2) for w in (1, 2)))
v1, v2 = C.v(r1, 1), C.v(r2, 2)
report('generalised trap: r_1 at 1 alone SAT; r_2 at 2 alone SAT; both UNSAT (defence of D vs X_E dies)',
       sat(clC, [v1]) and sat(clC, [v2]) and not sat(clC, [v1, v2]))
conf, F2 = C.closure([(r1, 1), (r2, 2)], {T, D}, coh)
report('generalised trap: (I2)-(I4) closure of {r_1@1, r_2@2} is clean (invisible to H4)', not conf and not F2)
XE = C.M(('E',))
bC = {w: C.v(C.rec(D, XE), w) for w in W}
report('  ... the kills: r_1@1 forces b_1 refused (r_1@1 + b_1 UNSAT); r_2@2 forces b_2 refused',
       not sat(clC, [v1, bC[1]]) and not sat(clC, [v2, bC[2]]) and sat(clC, [v1, bC[2]]) and sat(clC, [v2, bC[1]]))

# ------------------------------------------------------------------------------------------
# Instance L: one stage of the accumulation counterexample (report section 5).
#   cells of instance B with E' = P (one atom), plus layer cells of two near-T members:
#   L  : + correct at {1};  T silent, D' = +  ;  Q  = T[L -> +]  (1-better than T, near T)
#   L' : + correct at {2};  T silent, D' = +  ;  Q' = T[L' -> +] (2-better than T, near T)
# Selected: T (all worlds), D' (worlds 1,2), Q and Q' (interior, all worlds).
# Stage commitments: Q <=_1 D'  and  Q' <=_2 D'.
# ------------------------------------------------------------------------------------------
print('Instance L (one stage of the accumulation counterexample), 64 splices')
cellsL = {'P': {1, 2}, 'c1': {1, 3}, 'c2': {2, 3}, 'c3': {3}, 'L': {1}, 'Lp': {2}}
TL = {'P': 'S', 'c1': 'S', 'c2': 'S', 'c3': '+', 'L': 'S', 'Lp': 'S'}
DL = {'P': '+', 'c1': '+', 'c2': '+', 'c3': '-', 'L': '+', 'Lp': '+'}
Li = Inst(cellsL, TL, DL)
T, D = Li.M(), Li.M(cellsL)
Q, Qp = Li.M(('L',)), Li.M(('Lp',))
coh = {T, D, Q, Qp}
clL = Li.clauses([(T, W), (D, (1, 2)), (Q, W), (Qp, W)], coh)
stage = [Li.v(Li.rec(Q, D), 1), Li.v(Li.rec(Qp, D), 2)]
aL = {w: Li.v(Li.rec(T, D), w) for w in W}
report('stage SAT; stage + a_1 SAT; stage + a_2 SAT (no literal on a_1, a_2 is entailed)',
       sat(clL, stage) and sat(clL, stage + [aL[1]]) and sat(clL, stage + [aL[2]]))
report('stage + a_1 + a_2 UNSAT (this is what the limit acceptances force)', not sat(clL, stage + [aL[1], aL[2]]))
conf, F2 = Li.closure([(Li.rec(Q, D), 1), (Li.rec(Qp, D), 2)], coh, coh)
report('stage commitments are (I2)-(I4)-clean', not conf and not F2)
print('ALL PASS' if ok else 'SOME FAIL')
