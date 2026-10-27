import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bal2_79 import *
N = list(B) + [tuple(F(V[0][i] + V[2][i]) for i in range(3))]
k, m = 0, 2
mods = {'T': T, 'N': N, 'B': B}
for j, s in enumerate(SC['in']): mods['k%d' % j] = ray(k, s)
for j, s in enumerate(SC['in']): mods['m%d' % j] = ray(m, s)
At = atoms(mods)
rows = {}
for a in At:
    if a['half'] == 1: continue
    v = a['vals']; old = v['k1']
    if not (v['k0'] == v['k1'] == v['k2'] == v['m0'] == v['m1'] == v['m2'] == old): continue
    if v['N'] == old: continue
    key = (a['type'], v['T'], old, v['B'], v['N'], tuple(u1(v['N'], a['h']) - u1(old, a['h'])))
    rows[key] = rows.get(key, 0) + 1
for kk, c in sorted(rows.items(), key=str): print(c, kk)
