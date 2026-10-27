"""cycle71d: two neighbouring cycles and the pinning forced by closed fixed-rival sections (PP71 §5).

Cycle s : C_i  = D_{[v3, v3 + lam (theta_i, 1-theta_i, -1)]}, lam = 1/5   (cycle71)
Cycle s': C'_i = same with lam' (argv[1], default 11/50).
Fills: for each of the 8 models, its class-3 fills: unions of at most FILLMAX (env, default 1) bounded pieces, all bounded pieces,
       each whole silent region, and the whole class-3 silence (fill_sets).
Optional: FRAC2 (env) adds that fraction of the 2-cell fills at random (SEED).
Hypotheses:
  D   both cycles: C_{i+1} dominates the listed fills of C_i, C'_{i+1} those of C'_i;
  P   pinning (closed sections + edge lemma, PP71 Lemma 5.1): C'_i refuses C_{i+1} at worlds 1,2 and
      C_i refuses C'_{i+1} at worlds 1,2 (s' close to s);
  N   no world-3 ties on diagonals: C_i, C_{i+2} refuse each other at 3, in each cycle and across cycles.
Run: python3 -I -B cycle71d.py [lam']
"""
import itertools, os, sys
FILLMAX = int(os.environ.get('FILLMAX', '1'))
FRAC2 = float(os.environ.get('FRAC2', '0'))   # fraction of 2-cell fills added at random
SEED = int(os.environ.get('SEED', '0'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom71 import *
from lib71 import Inst, W
from cycle71 import seg, TH, make_cells, fillable, fill_sets

lam2 = F(sys.argv[1]) if len(sys.argv) > 1 else F(11, 50)
Ks = [seg(t, F(1, 5)) for t in TH] + [seg(t, lam2) for t in TH]
G = exact_points(Ks)
cells, pats = make_cells(Ks, G)
nc = len(cells)
Cm = [tuple(p[i] for p in pats) for i in range(8)]
print('lam\' =', lam2, '; cells:', nc, '; distinct models:', len(set(Cm)))
fills = {}
for i in range(8):
    L = fillable(cells, Cm[i])
    Es = fill_sets(cells, Cm[i], maxbounded=FILLMAX, maxregions=1)
    if FRAC2 > 0:
        import random
        rnd = random.Random(SEED * 100 + i)
        Es += [E for E in itertools.combinations(L, 2) if rnd.random() < FRAC2]
    fills[i] = list(dict.fromkeys(tuple('A' if j in E else Cm[i][j] for j in range(nc)) for E in Es))
models = Cm + [f for i in range(8) for f in fills[i]]
I = Inst(cells, models)
I.build(selected={m: W for m in Cm}, registered=Cm, coherent=set(Cm))
print('sub-universe:', len(I.models))
nxt = lambda i: (i // 4) * 4 + (i % 4 + 1) % 4
D = [I.lit(Cm[nxt(i)], f, w) for i in range(8) for f in fills[i] for w in W]
P = []
for i in range(4):
    P += [I.lit(Cm[4 + i], Cm[nxt(i)], w, False) for w in (1, 2)]
    P += [I.lit(Cm[i], Cm[nxt(4 + i)], w, False) for w in (1, 2)]
Nd = []
for a in range(8):
    for b in range(8):
        if a != b and (a % 4 - b % 4) % 2 == 0 and a % 4 != b % 4:
            Nd.append(I.lit(Cm[a], Cm[b], 3, False))
for name, h in [('D', D), ('D+P', D + P), ('D+P+N', D + P + Nd)]:
    print('%-6s %s' % (name, 'SAT' if I.solve(h) else 'UNSAT'))
h = D + P + Nd
if I.solve(h):
    print('forced world-3 verdicts C_i(s\') vs C_{i+1}(s) and same-position pairs under D+P+N:')
    for i in range(4):
        print('   C\'%d <=_3 C%d: %s   C%d <=_3 C\'%d: %s   C\'%d <=_w C%d: %s' % (
            i + 1, nxt(i) + 1, I.forced(Cm[4 + i], Cm[nxt(i)], 3, h), i + 1, nxt(i) + 1,
            I.forced(Cm[i], Cm[nxt(4 + i)], 3, h), i + 1, i + 1, [I.forced(Cm[4 + i], Cm[i], w, h) for w in W]))
