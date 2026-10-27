"""diag72: pointwise screening of candidate dominators (no SAT).  B can dominate f only if, at every world w,
f is not pointwise weakly better than B with strict somewhere (strict (G)), and B does not answer A on all of E."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inst72 import *
import numpy as np
exec(open('sat72b.py').read().split('t0 = time.time()')[0])
B = Build(idx, maxr=MAXR)
I = B.I
names = [c for c, _ in B.cells]
def viable(X, f):
    a, b = I.idx[X], I.idx[f]
    for w in W:
        rX, rf = I.R[w - 1, a], I.R[w - 1, b]
        if (rf <= rX).all() and (rf < rX).any():
            return False
    return True
bad = 0
for s in src:
    for k in (1, 2, 3):
        for f in B.F[(s, k)]:
            E = [j for j in range(len(names)) if f[j] != B.M[s][j]]
            cand = [x for x in idx if B.M[x] != f and not all(B.M[x][j] == 'A' for j in E) and viable(B.M[x], f)]
            if not cand:
                bad += 1
                print('no viable candidate: source %s class %d fill on %s' % (s, k, [names[j] for j in E]))
            elif os.environ.get('V'):
                print(s, k, [names[j] for j in E], cand)
print('fills without viable candidate:', bad)
