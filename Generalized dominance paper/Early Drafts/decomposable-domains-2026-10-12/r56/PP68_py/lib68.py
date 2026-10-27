"""lib68: exact SAT encoding of the axioms on an abstract cell instance (PP68).

Axioms encoded (no others):
  reflexivity / weak (G): a record whose old side is pointwise no worse at w is accepted at w;
  strict (G): a record whose new side is pointwise no worse and strictly better somewhere is refused;
  (IB): verdicts are variables of RECORDS (support, old values, new values), so all common-context
        copies share one variable;
  (TC): for every ordered triple (X,Y,Z) and world w: X<=Y, Y<=Z, Z<=X accepted => all reverses accepted;
  defence (competitiveness on the support) for every SELECTED model, against every model of the universe;
  undominatedness (rule III) and direct (C) for every REGISTERED model N:
        X<=_w N at every w  =>  N<=_w X at every w;   and an incoherent X is never all-world tied with N.
Sections cannot be encoded (no indices); they are handled in the text.

Cells: (name, cls).  cls in {1,2,3}: the odd world (A correct at the other two, B correct at cls);
cls 0: unmixed (A correct at all worlds).  Advice: 'A', 'B', 'S'.
"""
import itertools
from pysat.solvers import Cadical153

W = (1, 2, 3)


def rank(cls, adv, w):
    if adv == 'S':
        return 1
    if cls == 0:
        return 0 if adv == 'A' else 2
    corr = 'B' if cls == w else 'A'
    return 0 if adv == corr else 2


class Instance:
    def __init__(self, cells, allowed=None, models=None):
        """cells: list of (name, cls); allowed: dict name -> tuple of advice values
        (full product universe), or models: an explicit list of models (a sub-universe; UNSAT on a
        sub-universe implies UNSAT on any larger one, since every encoded clause is an axiom instance)."""
        self.cells = [c for c, _ in cells]
        self.cls = dict(cells)
        if models is not None:
            self.models = sorted(set(models))
        else:
            self.models = [tuple(v) for v in itertools.product(*[allowed[c] for c in self.cells])]
        self.var = {}
        self.cl = []

    def M(self, **kw):
        """model from per-cell values; unspecified cells must be given via base."""
        return tuple(kw[c] for c in self.cells)

    def splice(self, base, **kw):
        b = dict(zip(self.cells, base))
        b.update(kw)
        return tuple(b[c] for c in self.cells)

    def rec(self, X, Y):
        return tuple((self.cells[n], X[n], Y[n]) for n in range(len(self.cells)) if X[n] != Y[n])

    @staticmethod
    def inv(r):
        return tuple((c, n, o) for (c, o, n) in r)

    def v(self, r, w):
        k = (r, w)
        if k not in self.var:
            self.var[k] = len(self.var) + 1
        return self.var[k]

    def lit(self, X, Y, w, positive=True):
        x = self.v(self.rec(X, Y), w)
        return x if positive else -x

    def weakbetter(self, r, w):
        """old side pointwise no worse at w"""
        return all(rank(self.cls[c], o, w) <= rank(self.cls[c], n, w) for (c, o, n) in r)

    def pw_le(self, X, Y, w):
        """X pointwise no worse than Y at w"""
        return all(rank(self.cls[c], X[n], w) <= rank(self.cls[c], Y[n], w)
                   for n, c in enumerate(self.cells))

    def build(self, selected, registered, coherent):
        """selected: dict model -> support tuple; registered: list of models; coherent: set."""
        cl = self.cl
        recs = set()
        for X in self.models:
            for Y in self.models:
                if X != Y:
                    recs.add(self.rec(X, Y))
        for r in recs:
            for w in W:
                if self.weakbetter(r, w):
                    cl.append([self.v(r, w)])
                    cl.append([-self.v(self.inv(r), w)])
        for X, Y, Z in itertools.permutations(self.models, 3):
            a, b, c = self.rec(X, Y), self.rec(Y, Z), self.rec(Z, X)
            for w in W:
                base = [-self.v(a, w), -self.v(b, w), -self.v(c, w)]
                for rr in (self.inv(a), self.inv(b), self.inv(c)):
                    cl.append(base + [self.v(rr, w)])
        for S_, supp in selected.items():
            for X in self.models:
                if X != S_:
                    cl.append([self.v(self.rec(S_, X), w) for w in supp])
        for N in registered:
            for X in self.models:
                if X == N:
                    continue
                allin = [-self.v(self.rec(X, N), w) for w in W]
                if X not in coherent:
                    cl.append(allin)  # protection + direct (C)
                else:
                    for w2 in W:
                        cl.append(allin + [self.v(self.rec(N, X), w2)])
        self.solver = Cadical153(bootstrap_with=cl)
        return self

    def add(self, clause):
        self.solver.add_clause(clause)

    def sat(self, assumptions=()):
        return self.solver.solve(assumptions=list(assumptions))

    def forced(self, X, Y, w, assumptions=()):
        """return 'A' if acceptance forced, 'R' if refusal forced, '?' if free, 'X' if base UNSAT"""
        l = self.lit(X, Y, w)
        p = self.sat(list(assumptions) + [l])
        n = self.sat(list(assumptions) + [-l])
        if p and not n:
            return 'A'
        if n and not p:
            return 'R'
        if p and n:
            return '?'
        return 'X'
