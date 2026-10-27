"""cycle71c: the 4-cycle together with T, and with splices (PP71 §3-§4).

Models: C1..C4 (cycle71) and T = D_M (selected, registered; no hypotheses about T's own fills).
Cells: the exact census of the five models (class-3 common silence split in P1, P2).
Sub-universe: the five models, all class-3 fills of C1..C4, and NSPL random consecutive splices per pair (argv[1], default 40) of the form
Z = C_i[H -> C_{i+1}] (H a proper non-empty union of cells where they differ).
Tests:
  K1  4-cycle H1..H4 with T present: SAT expected;
  K2  K1 + every consecutive splice is dominated by SOME member of {T, C1..C4} (one auxiliary variable
      per splice and dominator): SAT/UNSAT reported; on SAT, the dominator chosen for each splice type.
Run: python3 -I -B cycle71c.py
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom71 import *
from lib71 import Inst, W
from cycle71 import Ks, make_cells, fillable, fill_sets

KT = list(V)
G = exact_points(Ks + [KT])
cells, pats = make_cells(Ks + [KT], G)
n = 4
Cm = [tuple(p[i] for p in pats) for i in range(n)]
T = tuple(p[4] for p in pats)
nc = len(cells)
print('cells (%d):' % nc, ' '.join(c for c, _ in cells))
for i, m in enumerate(Cm + [T]):
    print('  %s %s' % (('C%d' % (i + 1)) if i < 4 else 'T ', ''.join(m)))
fills = {}
for i in range(n):
    fills[i] = [tuple('A' if j in E else Cm[i][j] for j in range(nc)) for E in fill_sets(cells, Cm[i])]
import random
rnd = random.Random(71)
NSPL = int(sys.argv[1]) if len(sys.argv) > 1 else 40
splices = []
for i in range(n):
    a, b = Cm[i], Cm[(i + 1) % n]
    D = [j for j in range(nc) if a[j] != b[j]]
    seen = set()
    while len(seen) < min(NSPL, 2 ** len(D) - 2):
        H = tuple(sorted(rnd.sample(D, rnd.randint(1, len(D) - 1))))
        seen.add(H)
    for H in sorted(seen):
        splices.append(tuple(b[j] if j in H else a[j] for j in range(nc)))
splices = [z for z in dict.fromkeys(splices) if z not in Cm and z != T]
models = Cm + [T] + [f for i in range(n) for f in fills[i]] + splices
I = Inst(cells, models)
reg = Cm + [T]
ALLCOH = os.environ.get('ALLCOH') == '1'   # treat every model as possibly coherent (drops all (C) clauses)
I.build(selected={m: W for m in reg}, registered=reg, coherent=set(I.models) if ALLCOH else set(reg))
print('coherence labelling:', 'every model possibly coherent (only rule III)' if ALLCOH else 'only the five selected models coherent')
print('sub-universe: %d models (%d splices)' % (len(I.models), len(splices)))
H = [I.lit(Cm[(i + 1) % n], f, w) for i in range(n) for f in fills[i] for w in W]
k1 = I.solve(H)
print('K1 4-cycle with T present:', 'SAT' if k1 else 'UNSAT')
for z in splices:
    row = [I.v(('aux', I.idx[z], k), 0) for k in range(len(reg))]
    I.solver.add_clause(row)
    for k, D_ in enumerate(reg):
        for w in W:
            I.solver.add_clause([-row[k], I.lit(D_, z, w)])
I2 = I
H2 = [I2.lit(Cm[(i + 1) % n], f, w) for i in range(n) for f in fills[i] for w in W]
k2 = I2.solve(H2)
print('K2 K1 + every consecutive splice dominated by a member of {C1..C4, T}:', 'SAT' if k2 else 'UNSAT')
if k2:
    mdl = I2.last
    names = ['C1', 'C2', 'C3', 'C4', 'T']
    from collections import Counter
    cnt = Counter()
    for z in splices:
        ks = [names[k] for k in range(len(reg)) if I2.v(('aux', I2.idx[z], k), 0) in mdl]
        cnt[ks[0]] += 1
    print('   dominators used (first true):', dict(cnt))
