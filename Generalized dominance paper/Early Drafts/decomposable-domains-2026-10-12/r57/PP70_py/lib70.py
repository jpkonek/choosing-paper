"""lib70: independent SAT encoding of the finitary axioms on an abstract cell instance (PP70).

Verdict variables are indexed by (record, world): (IB) is built in.
Clauses: weak (G) acceptances and strict (G) refusals for every record of the universe;
(TC) on every ordered triple of the universe at every world (an accepted triangle forces its three
reverses); competitiveness of each SELECTED model on its support against every universe model;
rule III (protection) for each REGISTERED model, and direct (C): no all-world tie with a model
labelled incoherent. Sections and indices are not encoded.
Sub-universe principle: every clause is an instance of an axiom, so UNSAT on a sub-universe
implies UNSAT in the full model domain; SAT is evidence only.
Cells are (name, cls); cls 1..3 is the odd world of a mixed cell (A = majority answer, correct at
the two other worlds; B = minority answer, correct only at cls). Values 'A', 'B', 'S'.
"""
import itertools
from pysat.solvers import Minisat22

W = (1, 2, 3)


def rank(cls, a, w):
    if a == 'S':
        return 1
    good = 'B' if cls == w else 'A'
    return 0 if a == good else 2


class Inst:
    def __init__(self, cells, models):
        self.cells = [c for c, _ in cells]
        self.cls = dict(cells)
        self.models = list(dict.fromkeys(models))
        self.idx = {}
        self.clauses = []

    def m(self, base=None, **kw):
        d = dict(zip(self.cells, base)) if base is not None else {}
        d.update(kw)
        return tuple(d[c] for c in self.cells)

    def rec(self, X, Y):
        return tuple((c, X[i], Y[i]) for i, c in enumerate(self.cells) if X[i] != Y[i])

    def var(self, r, w):
        k = (r, w)
        if k not in self.idx:
            self.idx[k] = len(self.idx) + 1
        return self.idx[k]

    def L(self, X, Y, w):
        return self.var(self.rec(X, Y), w)

    def gstat(self, r, w):
        """+1 if old side weakly w-better (accept), -1 if new side strictly better (refuse), 0 mixed"""
        d = [rank(self.cls[c], n, w) - rank(self.cls[c], o, w) for (c, o, n) in r]
        if all(x >= 0 for x in d):
            return 1
        if all(x <= 0 for x in d) and any(x < 0 for x in d):
            return -1
        return 0

    def build(self, selected, registered, incoherent):
        cl = self.clauses
        recs = {self.rec(X, Y) for X in self.models for Y in self.models}
        for r in recs:
            for w in W:
                s = self.gstat(r, w)
                if s == 1:
                    cl.append([self.var(r, w)])
                elif s == -1:
                    cl.append([-self.var(r, w)])
        for X, Y, Z in itertools.permutations(self.models, 3):
            a, b, c = self.rec(X, Y), self.rec(Y, Z), self.rec(Z, X)
            for w in W:
                pre = [-self.var(a, w), -self.var(b, w), -self.var(c, w)]
                for (P, Q) in ((Y, X), (Z, Y), (X, Z)):
                    cl.append(pre + [self.var(self.rec(P, Q), w)])
        for S_, supp in selected.items():
            for X in self.models:
                cl.append([self.L(S_, X, w) for w in supp])
        for N in registered:
            for X in self.models:
                if X == N:
                    continue
                pre = [-self.L(X, N, w) for w in W]
                if X in incoherent:
                    cl.append(pre)
                else:
                    for w in W:
                        cl.append(pre + [self.L(N, X, w)])
        self.solver = Minisat22(bootstrap_with=cl)
        return self

    def sat(self, lits=()):
        return self.solver.solve(assumptions=list(lits))

    def forced(self, X, Y, w, lits=()):
        l = self.L(X, Y, w)
        p, n = self.sat(list(lits) + [l]), self.sat(list(lits) + [-l])
        return {(True, False): 'A', (False, True): 'R', (True, True): '?', (False, False): 'X'}[(p, n)]
