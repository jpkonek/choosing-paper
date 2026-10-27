"""inst72: cell sub-universes for the rescaling loop, fills of ALL three classes, splices, disjunctive dominators.
Every clause is an axiom instance on the sub-universe (lib72 = unmodified copy of PP71's lib71), so UNSAT is a
full-domain fact (for these installed models); SAT is evidence only.  Sections are not encoded except through
explicit pinning literals."""
import itertools, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom72 import *
from lib72b import Inst, W

def make_cells(Ks):
    G = exact_points(Ks)
    Cn = census(Ks, G)
    cells, pats = [], []
    for (k, a) in sorted(Cn):
        if k == 0:
            continue
        nm = '%d%s' % (k, ''.join(a))
        if 'S' in a:      # bounded piece (fillable) + its rest
            cells += [(nm, k), (nm + '~', k)]
            pats += [a, a]
        elif len(set(a)) > 1:
            cells.append((nm, k)); pats.append(a)
    return cells, pats

def fills(cells, model, k, maxr=2):
    """class-k fills of a model: unions (size <= maxr, plus all) of its silent bounded class-k pieces (non-conic),
    each single whole silent region (conic), and its whole class-k silence (conic)."""
    pieces = [j for j, (c, kk) in enumerate(cells) if kk == k and model[j] == 'S' and not c.endswith('~')]
    names = [c for c, _ in cells]
    out = []
    for r in range(1, min(maxr, len(pieces)) + 1):
        out += [tuple(E) for E in itertools.combinations(pieces, r)]
    if pieces:
        out.append(tuple(pieces))
        if maxr >= 2:
            regs = [tuple(sorted((j, names.index(names[j] + '~')))) for j in pieces]
            out += regs
        out.append(tuple(sorted(set(x for j in pieces for x in (j, names.index(names[j] + '~'))))))
    res = []
    for E in dict.fromkeys(out):
        res.append((tuple('A' if j in E else model[j] for j in range(len(cells))), all(not names[j].endswith('~') for j in E)))
    return res   # (model, bounded?)

def splices(cells, X, Y, maxr=1):
    D = [j for j in range(len(cells)) if X[j] != Y[j]]
    out = []
    for r in list(range(1, min(maxr, len(D)) + 1)) + [len(D) - x for x in range(1, min(maxr, len(D) - 1) + 1)]:
        for H in itertools.combinations(D, r):
            out.append(tuple(Y[j] if j in H else X[j] for j in range(len(cells))))
    return [s for s in dict.fromkeys(out) if s != X and s != Y]

class Build:
    def __init__(self, idx, maxr=2, splice_pairs=(), splice_r=1, extra=(), fill_sources=None):
        self.names = list(idx)
        Ks = [post(idx[n]) for n in self.names]
        self.cells, pats = make_cells(Ks)
        self.M = {n: tuple(p[i] for p in pats) for i, n in enumerate(self.names)}
        self.F = {}
        models = list(self.M.values())
        bounded = set()
        for n in self.names:
            for k in (1, 2, 3):
                if fill_sources is not None and n not in fill_sources:
                    self.F[(n, k)] = []
                    continue
                fl = fills(self.cells, self.M[n], k, maxr)
                self.F[(n, k)] = [f for f, _ in fl]
                models += self.F[(n, k)]
                bounded |= set(f for f, bd in fl if bd)
        self.S = {}
        import random
        smax = int(os.environ.get('SPLMAX', '0'))
        for (x, y) in splice_pairs:
            zs = splices(self.cells, self.M[x], self.M[y], splice_r)
            if smax and len(zs) > smax:
                zs = random.Random(72).sample(zs, smax)
            self.S[(x, y)] = zs
            models += zs
        models += list(extra)
        self.I = Inst(self.cells, models)
        self.bounded = bounded
        # coherence labelling: only the installed posterior models are known coherent; every other model is
        # treated as POSSIBLY coherent (weakest constraint) except bounded fills, which are incoherent.
        allm = set(self.I.models)
        self.coh = allm - bounded

    def build(self, selected, registered, extra_clauses=()):
        sel = {self.M[n]: W for n in selected}
        self.I.build(selected=sel, registered=[self.M[n] for n in registered], coherent=self.coh,
                     extra=list(extra_clauses))
        self.aux = len(self.I.var) + 100000
        return self

    def newvar(self):
        self.aux += 1
        return self.aux

    def dominated_by_some(self, f, Bs):
        """clauses: OR_B [B <=_w f all w, and f not<=_w B at some w]"""
        I = self.I
        sel = []
        cl = []
        for B in Bs:
            d = self.newvar(); sel.append(d)
            for w in W:
                cl.append([-d, I.lit(B, f, w)])
            cl.append([-d] + [-I.lit(f, B, w) for w in W])
        cl.append(sel)
        return cl
