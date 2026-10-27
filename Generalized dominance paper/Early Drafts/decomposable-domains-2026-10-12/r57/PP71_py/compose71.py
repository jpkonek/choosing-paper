"""compose71: the (T2) condition of PP71 Lemma 4.1 on the explicit cycle (exact on the cell census).
For each i and w in {1,2}: is C_{i+2} strictly w-better than the full class-3 fill of C_i somewhere?
Also lists the cells where it is.  Run: python3 -I -B compose71.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cycle71 import setup
from lib71 import rank
cells, Cm, fills, models = setup()
ok = True
for i in range(4):
    full = tuple('A' if (k == 3 and a == 'S') else a for (c, k), a in zip(cells, Cm[i]))
    j = (i + 2) % 4
    for w in (1, 2):
        where = [c for (c, k), x, y in zip(cells, Cm[j], full) if rank(k, x, w) < rank(k, y, w)]
        print('C%d vs full fill of C%d at world %d: C%d better on %s' % (j + 1, i + 1, w, j + 1, where))
        ok &= bool(where)
print('ALL PASS' if ok else 'SOME FAIL')
