"""cycle71h: does the whole-region splice core of cycle71f_v1 (PIECES=0) survive in the finer instance
(PIECES=1: class-3 regions split into bounded piece + rest; fills = bounded unions + whole-region unions)?
The 11 core splices are embedded with each whole region = piece + rest.  Reports SAT/UNSAT with the default
coherence labelling and with ALLCOH (no labelling).  Run: python3 -I -B cycle71h.py"""
import itertools, os, sys
os.environ['PIECES'] = '1'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom71 import *
from lib71 import Inst, W
from cycle71 import Ks, make_cells, fill_sets
CORE = [(0, ['1SAAAS', '3BSSSS', '3SBBBS']), (1, ['3BBSSS']), (2, ['1BBBSS', '1SSSAS', '2AAASS', '3BBBSS']),
        (2, ['1BBBSS', '1SSSAS', '3BBBSS']), (2, ['1BBBSS', '1SSSAS', '3BBBSS', '3SSSBS']), (2, ['1SSSAS']),
        (2, ['3BBBSS']),
        (3, ['1BBBSS', '1SSSAS', '2AAASS', '2ASSSS', '2SBBBS', '3BBBSS', '3BBSSS', '3BSSSS', '3SSSBS']),
        (3, ['1BBSSS', '1SAAAS', '1SSAAS', '1SSSAS', '2AAASS', '2AASSS', '2ASSSS', '2SBBBS', '2SSBBS', '3BBBSS',
             '3BBSSS', '3BSSSS', '3SBBBS', '3SSBBS', '3SSSBS']),
        (3, ['3BBBSS', '3SSBBS', '3SSSBS']), (3, ['3BBSSS'])]
G = exact_points(Ks + [list(V)])
cells, pats = make_cells(Ks + [list(V)], G)
nc = len(cells)
names = [c for c, _ in cells]
Cm = [tuple(p[i] for p in pats) for i in range(4)]
T = tuple(p[4] for p in pats)
reg = Cm + [T]
fills = {i: [tuple('A' if j in E else Cm[i][j] for j in range(nc)) for E in fill_sets(cells, Cm[i])] for i in range(4)}
# the full V1 splice list of cycle71c (PIECES=0, seed 71, 40 per pair), embedded as rivals
import random, cycle71
cycle71.PIECES = False
c1, p1 = make_cells(Ks + [list(V)], G)
cycle71.PIECES = True
n1 = [c for c, _ in c1]
C1m = [tuple(p[i] for p in p1) for i in range(4)]
rnd = random.Random(71)
v1spl = []
for i in range(4):
    a, b = C1m[i], C1m[(i + 1) % 4]
    D = [j for j in range(len(n1)) if a[j] != b[j]]
    seen = set()
    while len(seen) < min(40, 2 ** len(D) - 2):
        seen.add(tuple(sorted(rnd.sample(D, rnd.randint(1, len(D) - 1)))))
    for Hs in sorted(seen):
        v1spl.append((i, [n1[j] for j in Hs]))
spl = []
for i, H in CORE:
    a, b = Cm[i], Cm[(i + 1) % 4]
    Hset = set(H) | set(h + '~' for h in H)
    spl.append(tuple(b[j] if names[j] in Hset else a[j] for j in range(nc)))
def embed(i, H):
    a, b = Cm[i], Cm[(i + 1) % 4]
    Hset = set(H) | set(h + '~' for h in H)
    if 'P1' in Hset or 'P2' in Hset:
        Hset |= {'P~'}
    return tuple(b[j] if names[j] in Hset else a[j] for j in range(nc))
rivals = [embed(i, H) for i, H in v1spl]
models = list(dict.fromkeys(reg + [f for i in range(4) for f in fills[i]] + spl + rivals))
print('V1 splices embedded as rivals:', len(rivals))
for allcoh in (False, True):
    I = Inst(cells, models)
    I.build(selected={m: W for m in reg}, registered=reg, coherent=set(I.models) if allcoh else set(reg))
    H = [I.lit(Cm[(i + 1) % 4], f, w) for i in range(4) for f in fills[i] for w in W]
    for z in spl:
        row = [I.v(('aux', I.idx[z], k), 0) for k in range(5)]
        I.solver.add_clause(row)
        for k, D_ in enumerate(reg):
            for w in W:
                I.solver.add_clause([-row[k], I.lit(D_, z, w)])
    print('%s: |U| = %d; 4-cycle + the 11 whole-region core splices dominated by members/T: %s; same without the cycle: %s'
          % ('ALLCOH' if allcoh else 'default labelling', len(I.models), 'SAT' if I.solve(H) else 'UNSAT',
             'SAT' if I.solve([]) else 'UNSAT'))
