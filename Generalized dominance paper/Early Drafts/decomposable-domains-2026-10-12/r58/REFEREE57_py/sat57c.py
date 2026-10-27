"""sat57c: PP71's U0 instance (four cycle models only, bounded pieces) with the referee's encoder.
Cells: (class, pattern of C1..C4) from the complete LP chamber census; common class-3 silence -> P1, P2 (bounded
atoms) + P~ (rest); every other class-3 cell with a silent model -> bounded piece + rest '~'.
Fills of C_i: every union of its silent bounded pieces (non-conic) and every union of its silent whole regions.
For SAT runs the (C) clause is ADDED for every non-selected model (all treated as incoherent: strongest SAT);
for UNSAT runs it is dropped (strongest UNSAT)."""
import sys, itertools
sys.path.insert(0, '.')
import numpy as np
from rlib import *
import sat57 as S57
from pysat.solvers import Glucose4

Ks = S57.Ks[:4]
pts, _ = chambers(Ks)
types = {}
for g in pts:
    k = cls(g)
    if k == 0: continue
    types.setdefault((k, ''.join(adv(K, g) for K in Ks)), []).append(g)
cells = []
for (k, pat) in sorted(types):
    if len(set(pat)) == 1:
        if k == 3 and pat[0] == 'S':
            cells += [('P1', 3, pat), ('P2', 3, pat), ('P~', 3, pat)]
        continue
    cells.append(('%d%s' % (k, pat), k, pat))
    if k == 3 and 'S' in pat:
        cells.append(('%d%s~' % (k, pat), k, pat))
nc = len(cells)
print('cells (%d):' % nc, ' '.join(c[0] for c in cells))
C = [tuple(c[2][i] for c in cells) for i in range(4)]
names = [c[0] for c in cells]
def fills(m):
    pieces = [j for j in range(nc) if cells[j][1] == 3 and m[j] == 'S' and not names[j].endswith('~')]
    regions = {}
    for j in pieces:
        key = 'P' if names[j] in ('P1', 'P2') else names[j]
        regions.setdefault(key, set()).add(j)
    for key in regions:
        rest = 'P~' if key == 'P' else key + '~'
        regions[key].add(names.index(rest))
    sets = []
    for r in range(1, len(pieces) + 1):
        sets += [set(E) for E in itertools.combinations(pieces, r)]
    keys = sorted(regions)
    for r in range(1, len(keys) + 1):
        for R in itertools.combinations(keys, r):
            sets.append(set().union(*[regions[k] for k in R]))
    out = [tuple('A' if j in E else m[j] for j in range(nc)) for E in sets]
    return list(dict.fromkeys(out))
FL = {i: fills(C[i]) for i in range(4)}
print('fills per model:', [len(FL[i]) for i in range(4)])
S57.cells = cells; S57.nc = nc     # reuse the encoder with these cells

def run(label, hyps, withC):
    models = C + [f for i in range(4) for f in FL[i]]
    E = S57.Enc(models, C, C)
    if withC:
        for N in C:
            ni = E.ix[N]
            for X in E.M:
                if X in C: continue
                E.S.add_clause([-E.le(X, N, w) for w in (1, 2, 3)])
    assume = []
    for (D, X) in hyps: assume += E.dom(D, X)
    r = E.solve(assume)
    print('%-44s %3d models, (C) %s: %s' % (label, len(E.M), 'on ' if withC else 'off', 'SAT' if r else 'UNSAT'))
    return E, r

cyc = [(C[(i + 1) % 4], f) for i in range(4) for f in FL[i]]
E, r = run('4-cycle H1..H4', cyc, True)
if r:
    val = E.model
    print('   forced verdicts C_i <=_w C_{i+1} (w=1,2,3) under the cycle:')
    for i in range(4):
        a, b = C[i], C[(i + 1) % 4]
        out = []
        for w in (1, 2, 3):
            l = E.le(a, b, w)
            pa = E.solve([x for (D, X) in cyc for x in E.dom(D, X)] + [l])
            pb = E.solve([x for (D, X) in cyc for x in E.dom(D, X)] + [-l])
            out.append({(True, False): 'A', (False, True): 'R', (True, True): '?'}.get((pa, pb), 'X'))
        print('     C%d -> C%d : %s' % (i + 1, (i + 1) % 4 + 1, out))
run('2-cycle C1<->C2', [(C[1], f) for f in FL[0]] + [(C[0], f) for f in FL[1]], False)
run('3-cycle C1->C2->C3->C1', [(C[1], f) for f in FL[0]] + [(C[2], f) for f in FL[1]] + [(C[0], f) for f in FL[2]], True)
