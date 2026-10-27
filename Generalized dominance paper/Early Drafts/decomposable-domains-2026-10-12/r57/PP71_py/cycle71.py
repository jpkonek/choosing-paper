"""cycle71: the uniform 4-cycle C1 -> C2 -> C3 -> C4 -> C1 on its exact cell census (PP71 §3).

C_i = D_{[v3, v3 + lam*(theta_i, 1-theta_i, -1)]}, lam = 1/5, theta = 9/10, 13/20, 7/20, 1/10 (geom71).
Cells: every non-constant (class, pattern) of the EXACT face census (geom71.exact_points); the common class-3 silence SSSS split in bounded atoms P1, P2 and a rest P~; every other class-3 cell
with a silent model split into a bounded piece and its rest ('~').  Fills: every union of bounded pieces
(non-conic) and every union of whole silent regions (conic, e.g. the whole class-3 silence); see fill_sets.
Sub-universe U0: the four models and ALL their class-3 fills C_i[F -> A] (F any non-empty union of class-3 cells
where C_i is silent).  Optionally U1 = U0 + random splices/fills (stress test).
Hypotheses Hi: C_{i+1} <=_w C_i[F -> A] for every such F and every w (C_{i+1} dominates every fill of C_i).
Run: python3 -I -B cycle71.py
"""
import itertools, os, sys, random
PIECES = os.environ.get('PIECES', '1') == '1'   # PIECES=0: cells are whole regions (P split in two halves)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom71 import *
from lib71 import Inst, W


def seg(theta, lam):
    d = (theta, 1 - theta, -1)
    return [v3, tuple(v3[i] + lam * d[i] for i in range(3))]


TH = [F(9, 10), F(13, 20), F(7, 20), F(1, 10)]
LAM = F(1, 5)
Ks = [seg(t, LAM) for t in TH]


def make_cells(Ks, G):
    C = census(Ks, G)
    cells, pats = [], []
    for (k, a) in sorted(C):
        if len(set(a)) == 1:
            if k == 3 and a[0] == 'S':
                cells += [('P1', 3), ('P2', 3)] + ([('P~', 3)] if PIECES else [])
                pats += [a, a] + ([a] if PIECES else [])
            continue
        cells.append(('%d%s' % (k, ''.join(a)), k))
        pats.append(a)
        if k == 3 and 'S' in a and PIECES:   # bounded piece (the named cell) + the rest of the region ('~')
            cells.append(('%d%s~' % (k, ''.join(a)), k))
            pats.append(a)
    return cells, pats


def fillable(cells, model):
    """indices of bounded class-3 pieces where the model is silent (fills are bounded: never on a '~' rest)"""
    return [j for j, (c, k) in enumerate(cells) if k == 3 and model[j] == 'S' and not c.endswith('~')]


def fill_sets(cells, model, maxbounded=None, maxregions=None):
    """Fill sets of a model: (a) every non-empty union of its silent bounded pieces (bounded, non-conic fills),
    and (b) every non-empty union of its silent WHOLE regions (piece(s) + rest: conic fills, e.g. E = the whole
    class-3 silence, as in PP67).  maxbounded limits the size of the unions in (a)."""
    pieces = fillable(cells, model)
    names = [c for c, _ in cells]
    regions = {}
    for j in pieces:
        c = names[j]
        key = 'P' if c in ('P1', 'P2') else c
        regions.setdefault(key, set()).add(j)
    for key in regions:
        rest = 'P~' if key == 'P' else key + '~'
        if rest in names:
            regions[key].add(names.index(rest))
    out = []
    top = len(pieces) if maxbounded is None else maxbounded
    for r in range(1, top + 1):
        out += [tuple(E) for E in itertools.combinations(pieces, r)]
    if maxbounded is not None:
        out.append(tuple(pieces))
    keys = sorted(regions)
    for r in range(1, (len(keys) if maxregions is None else maxregions) + 1):
        for R in itertools.combinations(keys, r):
            out.append(tuple(sorted(set().union(*[regions[k] for k in R]))))
    if maxregions is not None and keys:
        out.append(tuple(sorted(set().union(*[regions[k] for k in keys]))))
    return list(dict.fromkeys(out))


def setup(extra_random=0, seed=1):
    G = exact_points(Ks)
    cells, pats = make_cells(Ks, G)
    n = len(Ks)
    Cm = [tuple(p[i] for p in pats) for i in range(n)]
    sil3 = [fillable(cells, Cm[i]) for i in range(n)]
    fills = {}
    for i in range(n):
        fills[i] = [tuple('A' if j in E else Cm[i][j] for j in range(len(cells))) for E in fill_sets(cells, Cm[i])]
    models = list(Cm) + [f for i in range(n) for f in fills[i]]
    if extra_random:
        rnd = random.Random(seed)
        vals = [sorted(set(p) | ({'A'} if cells[j][1] == 3 and 'S' in p else set())) for j, p in enumerate(pats)]
        while len(set(models)) < len(set(models)) + 0 + extra_random and extra_random > 0:
            base = list(Cm[rnd.randrange(n)])
            for j in rnd.sample(range(len(cells)), rnd.randint(1, 3)):
                base[j] = rnd.choice(vals[j])
            models.append(tuple(base))
            extra_random -= 1
    return cells, Cm, fills, models


if __name__ == '__main__':
    cells, Cm, fills, models = setup()
    print('cells (%d):' % len(cells), ' '.join(c for c, _ in cells))
    for i, m in enumerate(Cm):
        print('  C%d' % (i + 1), ''.join(m))
    I = Inst(cells, models)
    sel = {m: W for m in Cm}
    I.build(selected=sel, registered=Cm, coherent=set(Cm))
    n = 4
    H = {i: [I.lit(Cm[(i + 1) % n], f, w) for f in fills[i] for w in W] for i in range(n)}
    print('sub-universe U0: %d models' % len(I.models))
    res = {}
    for name, hs in [('no hypotheses', []), ('H1 (C2 serves C1)', H[0]), ('H1+H2', H[0] + H[1]),
                     ('H1+H2+H3', H[0] + H[1] + H[2]), ('4-cycle H1..H4', H[0] + H[1] + H[2] + H[3])]:
        res[name] = I.solve(hs)
        print('%-22s %s' % (name, 'SAT' if res[name] else 'UNSAT'))
    allh = H[0] + H[1] + H[2] + H[3]
    if res['4-cycle H1..H4']:
        print('forced verdicts among C1..C4 under the 4-cycle (worlds 1,2,3):')
        for a in range(n):
            for b in range(n):
                if a != b:
                    print('   C%d <=_w C%d  %s' % (a + 1, b + 1, [I.forced(Cm[a], Cm[b], w, allh) for w in W]))
    # contrast: 2-cycle C1 <-> C2 (C1 serves C2's fills too)
    back = [I.lit(Cm[0], f, w) for f in fills[1] for w in W]
    print('2-cycle C1<->C2 (H1 + C1 serves C2):', 'SAT' if I.solve(H[0] + back) else 'UNSAT')
    three = [I.lit(Cm[0], f, w) for f in fills[2] for w in W]
    print('3-cycle C1->C2->C3->C1 (H1+H2 + C1 serves C3):', 'SAT' if I.solve(H[0] + H[1] + three) else 'UNSAT')
    print('lazy (TC) clauses added:', I.ntc)
