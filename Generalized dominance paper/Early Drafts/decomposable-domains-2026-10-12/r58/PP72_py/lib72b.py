"""lib72b: memory-lean re-implementation of PP71's lib71 encoding (same clauses).  Records are keyed exactly by
bytes (changed positions, old advice, new advice); one SAT variable per (record, world), so all (IB) copies inside
the sub-universe share it.  Clauses: weak (G) + strict (G) reverse; defence of selected models at a world of the
support; protection + direct (C) for registered models; (TC) lazily, with a final check over EVERY ordered triple."""
import numpy as np, hashlib, os
from pysat.solvers import Cadical153
W = (1, 2, 3)
CODE = {'A': 0, 'S': 1, 'B': 2, 'X': 3}

def rank(k, a, w):
    if a == 'S': return 1
    if a == 'X': return 3
    corr = 'B' if k == w else 'A'
    return 0 if a == corr else 2

class Inst:
    def __init__(self, cells, models):
        self.cells = [c for c, _ in cells]
        self.cls = [k for _, k in cells]
        self.models = list(dict.fromkeys(models))
        self.idx = {m: i for i, m in enumerate(self.models)}
        n, nc = len(self.models), len(self.cells)
        self.A = np.array([[CODE[x] for x in m] for m in self.models], dtype=np.int8)
        R = np.zeros((3, n, nc), dtype=np.int8)
        for i, m in enumerate(self.models):
            for j in range(nc):
                for w in W:
                    R[w - 1, i, j] = rank(self.cls[j], m[j], w)
        self.R = R
        self.var = {}
        self.ntc = 0

    def key(self, a, b):
        d = np.nonzero(self.A[a] != self.A[b])[0]
        k = d.astype(np.int16).tobytes() + b'|' + self.A[a, d].tobytes() + self.A[b, d].tobytes()
        if os.environ.get('DIGEST') == '1':   # 128-bit digest; a collision can only ADD constraints (SAT stays valid)
            return hashlib.blake2b(k, digest_size=16).digest()
        return k

    def v(self, k, w):
        kk = (k, w)
        x = self.var.get(kk)
        if x is None:
            x = len(self.var) + 1
            self.var[kk] = x
        return x

    def lit(self, X, Y, w, pos=True):
        x = self.Vw[w - 1, self.idx[X], self.idx[Y]]
        return int(x) if pos else -int(x)

    def build(self, selected, registered, coherent, extra=()):
        n = len(self.models)
        self.Vw = np.zeros((3, n, n), dtype=np.int64)
        for a in range(n):
            for b in range(n):
                if a != b:
                    k = self.key(a, b)
                    for w in W:
                        self.Vw[w - 1, a, b] = self.v(k, w)
        cl = []
        for w in W:
            Rw = self.R[w - 1]
            for a in range(n):
                le = (Rw[a][None, :] <= Rw).all(axis=1)
                for b in np.nonzero(le)[0]:
                    if b != a:
                        cl.append([int(self.Vw[w - 1, a, b])])
                        cl.append([-int(self.Vw[w - 1, b, a])])
        for S_, supp in selected.items():
            s = self.idx[S_]
            for b in range(n):
                if b != s:
                    cl.append([int(self.Vw[w - 1, s, b]) for w in supp])
        for N in registered:
            m = self.idx[N]
            for b in range(n):
                if b == m: continue
                allin = [-int(self.Vw[w - 1, b, m]) for w in W]
                if self.models[b] not in coherent:
                    cl.append(allin)
                else:
                    for w2 in W:
                        cl.append(allin + [int(self.Vw[w2 - 1, m, b])])
        cl.extend(extra)
        self.nbase = len(cl)
        self.solver = Cadical153(bootstrap_with=cl)
        return self

    def add(self, c):
        self.solver.add_clause(c)

    def violations(self, mdl, cap=20000):
        val = np.zeros(len(self.var) + 2, dtype=np.int32)
        mm = np.array([x for x in mdl if 0 < x < len(val)], dtype=np.int64)
        val[mm] = 1
        out = []
        for w in W:
            Acc = val[self.Vw[w - 1]].astype(np.int32)
            np.fill_diagonal(Acc, 1)
            P = (Acc == 1) & (Acc.T == 0)
            A2 = Acc @ Acc
            bad = np.argwhere(P & (A2.T > 0))
            for (a, b) in bad:
                zs = np.nonzero(Acc[b] & Acc[:, a])[0]
                for z in zs:
                    if z != a and z != b:
                        out.append((int(a), int(b), int(z), w)); break
                if len(out) > cap: return out
        return out

    def solve(self, assumptions=(), maxit=5000):
        for it in range(maxit):
            if not self.solver.solve(assumptions=list(assumptions)):
                return False
            mdl = set(x for x in self.solver.get_model() if x > 0)
            viol = self.violations(mdl)
            if not viol:
                self.last = mdl
                return True
            for (a, b, c, w) in viol:
                X = [(a, b), (b, c), (c, a)]
                base = [-int(self.Vw[w - 1, x, y]) for (x, y) in X]
                for (x, y) in X:
                    self.add(base + [int(self.Vw[w - 1, y, x])]); self.ntc += 1
        raise RuntimeError('no convergence')

    def acc(self, X, Y, w):
        return self.lit(X, Y, w) in self.last
