"""cycle71g: robustness and core of the pinning conflict found by cycle71d (PP71 §5).
For lam' in argv (default 11/50): D + P_a (only C'_i refuses C_{i+1} at 1,2), D + P_b (only C_i refuses
C'_{i+1} at 1,2), D + P (both); then a greedy-minimal set of pinning literals (with all of D).
Run: python3 -I -B cycle71g.py [lam' ...]"""
import itertools, os, sys
FILLMAX = int(os.environ.get('FILLMAX', '1'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom71 import *
from lib71 import Inst, W
from cycle71 import seg, TH, make_cells, fillable, fill_sets

lams = [F(a) for a in sys.argv[1:]] or [F(11, 50)]
for lam2 in lams:
    Ks = [seg(t, F(1, 5)) for t in TH] + [seg(t, lam2) for t in TH]
    cells, pats = make_cells(Ks, exact_points(Ks))
    nc = len(cells)
    Cm = [tuple(p[i] for p in pats) for i in range(8)]
    fills = {}
    for i in range(8):
        L = fillable(cells, Cm[i])
        Es = fill_sets(cells, Cm[i], maxbounded=FILLMAX, maxregions=1)
        fills[i] = list(dict.fromkeys(tuple('A' if j in E else Cm[i][j] for j in range(nc)) for E in Es))
    models = Cm + [f for i in range(8) for f in fills[i]]
    I = Inst(cells, models)
    I.build(selected={m: W for m in Cm}, registered=Cm, coherent=set(Cm))
    nxt = lambda i: (i // 4) * 4 + (i % 4 + 1) % 4
    D = [I.lit(Cm[nxt(i)], f, w) for i in range(8) for f in fills[i] for w in W]
    Pa = [I.lit(Cm[4 + i], Cm[nxt(i)], w, False) for i in range(4) for w in (1, 2)]
    Pb = [I.lit(Cm[i], Cm[nxt(4 + i)], w, False) for i in range(4) for w in (1, 2)]
    print("lam' = %s: %d cells, |U| = %d" % (lam2, nc, len(I.models)))
    ra, rb = I.solve(D + Pa), I.solve(D + Pb)
    print('   D+Pa (C\'_i refuses C_{i+1}): %s;  D+Pb (C_i refuses C\'_{i+1}): %s' % (
        'SAT' if ra else 'UNSAT', 'SAT' if rb else 'UNSAT'))
    if lam2 == lams[0]:
        core = Pa + Pb if (ra and rb) else (Pa if not ra else Pb)
        if not I.solve(D + core):
            k = 0
            while k < len(core):
                t = core[:k] + core[k + 1:]
                if not I.solve(D + t):
                    core = t
                else:
                    k += 1
            lab = {}
            for i in range(4):
                for w in (1, 2):
                    lab[I.lit(Cm[4 + i], Cm[nxt(i)], w, False)] = "C'%d refuses C%d at %d" % (i + 1, nxt(i) + 1, w)
                    lab[I.lit(Cm[i], Cm[nxt(4 + i)], w, False)] = "C%d refuses C'%d at %d" % (i + 1, nxt(i) + 1, w)
            print('   greedy-minimal pinning core:', [lab[x] for x in core])
