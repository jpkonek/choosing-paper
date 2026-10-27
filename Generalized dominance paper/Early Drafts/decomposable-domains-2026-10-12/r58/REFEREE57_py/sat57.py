"""sat57: referee's independent re-implementation of PP71's cell SAT tests (V1 whole-region instance).

Census: complete chamber enumeration by LP over all sign vectors (rlib.chambers), NOT PP71's face walk.
Cells: (class, advice pattern of C1..C4,T); constant patterns dropped (all models agree there); the common class-3
silence split into two conic halves P1, P2.
Clauses (all axiom instances on the sub-universe; my own encoding):
  weak (G) acceptance + strict (G) refusal of the inverse for pointwise-ordered pairs (every advice change is
  strict at every world, since the advice set is {A,S,B} on mixed cells);
  (IB): one Boolean per (record, world), record = frozenset of (cell, old, new);
  (TC): every accepted directed triangle has its reverses accepted -- lazily added, final model checked on ALL
        ordered triples at all worlds;
  defence: each selected model against every model of the sub-universe, at some world (full support);
  protection (rule III) for registered models; (C) clauses omitted entirely (ALLCOH: strongest UNSAT).
Hypotheses: H_i: C_{i+1} <=_w F for every class-3 fill F of C_i and every w; splice domination by some member.
"""
import sys, itertools
sys.path.insert(0, '.')
import numpy as np
from rlib import *
from pysat.solvers import Glucose4

v3 = VM[2]
def seg(th, lam):
    d = (th, 1 - th, F(-1))
    return [v3, tuple(v3[i] + lam * d[i] for i in range(3))]
TH = [F(9, 10), F(13, 20), F(7, 20), F(1, 10)]
Ks = [seg(t, F(1, 5)) for t in TH] + [list(VM)]
NAMES = ['C1', 'C2', 'C3', 'C4', 'T']

pts, ns = chambers(Ks)
types = {}
for g in pts:
    k = cls(g)
    if k == 0: continue
    pat = ''.join(adv(K, g) for K in Ks)
    types.setdefault((k, pat), []).append(g)
cells = []          # (name, class, pattern)
for (k, pat) in sorted(types):
    if len(set(pat)) == 1:
        if k == 3 and pat[0] == 'S':
            cells += [('P1', 3, pat), ('P2', 3, pat)]
        continue
    cells.append(('%d%s' % (k, pat), k, pat))
nc = len(cells)
print('chambers: %d ; cells (%d): %s' % (len(pts), nc, ' '.join(c[0] for c in cells)))
base = [tuple(c[2][i] for c in cells) for i in range(5)]
C, T = base[:4], base[4]

def fills(m):
    sil = [j for j in range(nc) if cells[j][1] == 3 and m[j] == 'S']
    out = []
    for r in range(1, len(sil) + 1):
        for E in itertools.combinations(sil, r):
            out.append(tuple('A' if j in E else m[j] for j in range(nc)))
    return out
FILLS = {i: fills(C[i]) for i in range(4)}

def splice(i, Hnames):
    a, b = C[i], C[(i + 1) % 4]
    idx = [j for j in range(nc) if cells[j][0] in Hnames]
    assert len(idx) == len(Hnames), (Hnames, idx)
    for j in idx: assert a[j] != b[j]
    return tuple(b[j] if j in idx else a[j] for j in range(nc))

CORE = [(0, ['1SAAAS', '3BSSSS', '3SBBBS']), (1, ['3BBSSS']),
        (2, ['1BBBSS', '1SSSAS', '2AAASS', '3BBBSS']), (2, ['1BBBSS', '1SSSAS', '3BBBSS']),
        (2, ['1BBBSS', '1SSSAS', '3BBBSS', '3SSSBS']), (2, ['1SSSAS']), (2, ['3BBBSS']),
        (3, ['1BBBSS', '1SSSAS', '2AAASS', '2ASSSS', '2SBBBS', '3BBBSS', '3BBSSS', '3BSSSS', '3SSSBS']),
        (3, ['1BBSSS', '1SAAAS', '1SSAAS', '1SSSAS', '2AAASS', '2AASSS', '2ASSSS', '2SBBBS', '2SSBBS', '3BBBSS',
             '3BBSSS', '3BSSSS', '3SBBBS', '3SSBBS', '3SSSBS']),
        (3, ['3BBBSS', '3SSBBS', '3SSSBS']), (3, ['3BBSSS'])]

def rk(m, w):
    return np.array([rank(cells[j][1], m[j], w) for j in range(nc)])

class Enc:
    def __init__(self, models, selected, registered):
        self.M = list(dict.fromkeys(models)); n = len(self.M)
        self.ix = {m: i for i, m in enumerate(self.M)}
        self.vars = {}
        self.cl = []
        R = np.array([[rk(m, w) for m in self.M] for w in (1, 2, 3)])
        self.V = np.zeros((3, n, n), dtype=np.int64)
        for a in range(n):
            for b in range(n):
                if a == b: continue
                r = frozenset((j, self.M[a][j], self.M[b][j]) for j in range(nc) if self.M[a][j] != self.M[b][j])
                for w in range(3):
                    self.V[w, a, b] = self.var(('rec', r, w))
        for w in range(3):
            for a in range(n):
                for b in range(n):
                    if a != b and (R[w, a] <= R[w, b]).all():
                        self.cl += [[int(self.V[w, a, b])], [-int(self.V[w, b, a])]]
        for s in selected:
            si = self.ix[s]
            for b in range(n):
                if b != si: self.cl.append([int(self.V[w, si, b]) for w in range(3)])
        for N in registered:
            ni = self.ix[N]
            for b in range(n):
                if b == ni: continue
                prem = [-int(self.V[w, b, ni]) for w in range(3)]
                for w2 in range(3): self.cl.append(prem + [int(self.V[w2, ni, b])])
        self.S = Glucose4(bootstrap_with=self.cl)
        self.added = 0
    def var(self, key):
        if key not in self.vars: self.vars[key] = len(self.vars) + 1
        return self.vars[key]
    def le(self, X, Y, w): return int(self.V[w - 1, self.ix[X], self.ix[Y]])
    def dom(self, D, X): return [self.le(D, X, w) for w in (1, 2, 3)]
    def solve(self, assume):
        n = len(self.M)
        while True:
            if not self.S.solve(assumptions=assume): return False
            model = self.S.get_model()
            val = np.zeros(len(self.vars) + 2, dtype=np.int64)
            for x in model:
                if x > 0 and x < len(val): val[x] = 1
            viol = 0
            for w in range(3):
                A = val[self.V[w]]; np.fill_diagonal(A, 1)
                # accepted 2-paths b->z->a with a->b accepted and some reverse missing
                A2 = A @ A
                cand = np.argwhere((A == 1) & (A2.T > 0))
                for (a, b) in cand:
                    zs = np.nonzero(A[b] & A[:, a])[0]
                    for z in zs:
                        if z == a or z == b: continue
                        tri = [(a, b), (b, z), (z, a)]
                        if all(A[y, x] for (x, y) in tri): continue
                        pre = [-int(self.V[w, x, y]) for (x, y) in tri]
                        for (x, y) in tri:
                            self.S.add_clause(pre + [int(self.V[w, y, x])])
                        viol += 1; self.added += 1
                        break
                    if viol > 20000: break
            if viol == 0:
                self.model = val
                return True

def run(label, models, hyps_dom, splice_dom, extra_assume=()):
    sel = C + [T]
    E = Enc(models, sel, sel)
    assume = list(extra_assume)
    for (D, X) in hyps_dom: assume += E.dom(D, X)
    for z in splice_dom:
        aux = [E.var(('aux', z, k)) for k in range(5)]
        E.S.add_clause(aux)
        for k, D in enumerate(sel):
            for l in E.dom(D, z): E.S.add_clause([-aux[k], l])
    res = E.solve(assume)
    print('%-58s %4d models : %s   (lazy TC clauses %d)' % (label, len(E.M), 'SAT' if res else 'UNSAT', E.added))
    return E, res

if __name__ == '__main__':
    core = [splice(i, H) for i, H in CORE]
    allfills = [f for i in range(4) for f in FILLS[i]]
    cyc = [(C[(i + 1) % 4], f) for i in range(4) for f in FILLS[i]]
    base_models = C + [T] + allfills
    run('K1: 4-cycle, T present (fills only)', base_models, cyc, [])
    run('2-cycle C1<->C2 (C2 serves C1, C1 serves C2)', base_models,
        [(C[1], f) for f in FILLS[0]] + [(C[0], f) for f in FILLS[1]], [])
    run('3-cycle C1->C2->C3->C1', base_models,
        [(C[1], f) for f in FILLS[0]] + [(C[2], f) for f in FILLS[1]] + [(C[0], f) for f in FILLS[2]], [])
    run('core: 4-cycle + 11 core splices dominated by members', base_models + core, cyc, core)
    run('core without the cycle', base_models + core, [], core)
    # minimality probe: drop each core splice in turn
    for t in range(len(core)):
        sub = core[:t] + core[t + 1:]
        E, r = run('   core minus #%d (pair %s/%s)' % (t + 1, NAMES[CORE[t][0]], NAMES[(CORE[t][0] + 1) % 4]),
                   base_models + core, cyc, sub)
