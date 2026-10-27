import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inst72 import *
b = F(sys.argv[1]); mr = int(sys.argv[2])
L = loop(b)
names = list(L); Ks = [post(L[n]) for n in names]
cells, pats = make_cells(Ks)
M = {n: tuple(p[i] for p in pats) for i, n in enumerate(names)}
print('cells', len(cells))
tot = 3
for n in names:
    for k in (1, 2, 3):
        fl = fills(cells, M[n], k, mr)
        print(n, k, 'silent pieces', sum(1 for j, (c, kk) in enumerate(cells) if kk == k and M[n][j] == 'S' and not c.endswith('~')), 'fills', len(fl))
        tot += len(fl)
print('total models', tot)
