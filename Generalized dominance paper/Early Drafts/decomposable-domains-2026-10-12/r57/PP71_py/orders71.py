"""orders71: which cyclic orders of the four segment models carry a uniform 4-cycle on U0 (cycle71).
Run: python3 -I -B orders71.py"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cycle71 import setup
from lib71 import Inst, W
cells, Cm, fills, models = setup()
for perm in itertools.permutations([1, 2, 3]):
    order = (0,) + perm
    I = Inst(cells, models)
    I.build(selected={m: W for m in Cm}, registered=Cm, coherent=set(Cm))
    H = [I.lit(Cm[order[(k + 1) % 4]], f, w) for k in range(4) for f in fills[order[k]] for w in W]
    print('cycle', ' -> '.join('C%d' % (o + 1) for o in order + (0,)), ':', 'SAT' if I.solve(H) else 'UNSAT')
