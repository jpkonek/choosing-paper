"""lib71: SAT encoding of the axioms on a cell sub-universe, with lazy (TC) (counterexample-guided).

Same axiom instances as PP68's lib68 (every clause is an axiom instance on the sub-universe):
  weak (G): a record whose old side is pointwise no worse at w is accepted at w; strict (G): its inverse refused;
  (IB): one variable per (record, world): all common-context copies inside the sub-universe share it;
  (TC): accepted triangle => all reverses accepted -- added lazily, but the final model is checked against
        EVERY ordered triple of the sub-universe (so a SAT answer satisfies all (TC) instances);
  defence: every selected model, against every model of the sub-universe, at some world of its support;
  protection + direct (C): for registered N, X <=_w N at all w => N <=_w X at all w; an incoherent X is never
        all-world tied with N.
Sections are not encodable (no indices).  UNSAT on a sub-universe => UNSAT on the full domain; SAT is evidence.
"""
import itertools
import numpy as np
from pysat.solvers import Cadical153

W = (1, 2, 3)


def rank(k, a, w):
    if a == 'S':
        return 1
    corr = 'B' if k == w else 'A'
    return 0 if a == corr else 2


class Inst:
    def __init__(self, cells, models):
        self.cells = [c for c, _ in cells]
        self.cls = dict(cells)
        self.models = list(dict.fromkeys(models))
        self.idx = {m: i for i, m in enumerate(self.models)}
        self.var = {}
        self.base = []
        n, nc = len(self.models), len(self.cells)
        R = np.zeros((3, n, nc), dtype=np.int8)
        for i, m in enumerate(self.models):
            for j, c in enumerate(self.cells):
                for w in W:
                    R[w - 1, i, j] = rank(self.cls[c], m[j], w)
        self.R = R

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

    def lit(self, X, Y, w, pos=True):
        x = self.v(self.rec(X, Y), w)
        return x if pos else -x

    def build(self, selected, registered, coherent, extra=()):
        M = self.models
        n = len(M)
        self.recv = {}
        cl = self.base
        for a in range(n):
            for b in range(n):
                if a != b:
                    r = self.rec(M[a], M[b])
                    for w in W:
                        self.recv[(a, b, w)] = self.v(r, w)
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                for w in W:
                    if (self.R[w - 1, a] <= self.R[w - 1, b]).all():
                        cl.append([self.recv[(a, b, w)]])
                        cl.append([-self.recv[(b, a, w)]])
        for S_, supp in selected.items():
            s = self.idx[S_]
            for b in range(n):
                if b != s:
                    cl.append([self.recv[(s, b, w)] for w in supp])
        for N in registered:
            m = self.idx[N]
            for b in range(n):
                if b == m:
                    continue
                allin = [-self.recv[(b, m, w)] for w in W]
                if M[b] not in coherent:
                    cl.append(allin)
                else:
                    for w2 in W:
                        cl.append(allin + [self.recv[(m, b, w2)]])
        cl.extend(extra)
        self.solver = Cadical153(bootstrap_with=cl)
        self.ntc = 0
        return self

    def tc_clauses(self, a, b, c, w):
        X = [(a, b), (b, c), (c, a)]
        base = [-self.recv[(x, y, w)] for (x, y) in X]
        return [base + [self.recv[(y, x, w)]] for (x, y) in X]

    def violations(self, model_set, cap=15000):
        n = len(self.models)
        out = []
        if not hasattr(self, 'Vw'):
            self.Vw = np.zeros((3, n, n), dtype=np.int64)
            for (a, b, ww), x in self.recv.items():
                self.Vw[ww - 1, a, b] = x
        val = np.zeros(len(self.var) + 1, dtype=np.int32)
        for x in model_set:
            if x < len(val):
                val[x] = 1
        for w in W:
            A = val[self.Vw[w - 1]]
            np.fill_diagonal(A, 1)
            P = (A == 1) & (A.T == 0)          # accepted, reverse refused
            A2 = A @ A                          # A2[b,a] = #z with b->z->a
            bad = np.argwhere(P & (A2.T > 0))
            for (a, b) in bad:
                zs = np.nonzero(A[b] & A[:, a])[0]
                for z in zs[:1]:
                    if z != a and z != b:
                        out.append((a, b, int(z), w))
                if len(out) > cap:
                    return out
        return out

    def solve(self, assumptions=(), maxit=3000, verbose=False):
        for it in range(maxit):
            ok = self.solver.solve(assumptions=list(assumptions))
            if not ok:
                return False
            mdl = set(x for x in self.solver.get_model() if x > 0)
            viol = self.violations(mdl)
            if not viol:
                self.last = mdl
                return True
            for (a, b, c, w) in viol:
                for cl in self.tc_clauses(a, b, c, w):
                    self.solver.add_clause(cl)
                    self.ntc += 1
            if verbose:
                print('   iteration', it, 'violations', len(viol))
        raise RuntimeError('no convergence')

    def forced(self, X, Y, w, assumptions=()):
        l = self.lit(X, Y, w)
        p = self.solve(list(assumptions) + [l])
        q = self.solve(list(assumptions) + [-l])
        return {(True, False): 'A', (False, True): 'R', (True, True): '?', (False, False): 'X'}[(p, q)]
