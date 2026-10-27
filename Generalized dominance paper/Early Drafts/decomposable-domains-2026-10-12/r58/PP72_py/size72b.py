import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inst72 import *
txt = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sat72b.py')).read()
exec(txt.split('t0 = time.time()')[0])
Ks = [post(idx[n]) for n in idx]
cells, pats = make_cells(Ks)
print('installed', len(idx), list(idx)); print('cells', len(cells))
