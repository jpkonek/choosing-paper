"""cells7_ref (REFEREE56): exact cell count and type census of PP67's seven-model module (Theorem 6.1).
Run: python3 -I -B cells7_ref.py > cells7_ref.out"""
import os, sys, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geomlib import *
def projk(m, k):
    s = sum(m[j] for j in range(3) if j != k)
    return tuple(F(0) if j == k else m[j] / s for j in range(3))
E3 = [(1,0,0),(0,1,0),(0,0,1)]
M0k = {k: [projk(M[j], k) for j in range(3) if j != k] for k in range(3)}
mid = {k: projk(M[k], k) for k in range(3)}
for k in range(3):
    assert mid[k] == tuple((a+b)/2 for a, b in zip(*M0k[k]))
P12 = E3 + M + [p for k in range(3) for p in M0k[k]]
P15 = P12 + [mid[k] for k in range(3)]
for nm, P in (('12 planes (generators of every credal set)', P12), ('15 planes (adding the three midpoints)', P15)):
    pts, (V, Ed, Fc) = cells(P)
    print('%s: %d cells, Euler V=%d E=%d F=%d, complete=%s' % (nm, len(pts), V, Ed, Fc, len(pts) == Fc))
    MOD = [('T', M)] + [('N%d' % (k+1), M + M0k[k]) for k in range(3)] + [('D%d' % (k+1), M0k[k]) for k in range(3)]
    types = set()
    for g in pts:
        if cls(g) == 0: continue
        types.add((cls(g),) + tuple(AB(g, adv(K, g)) for _, K in MOD))
    print('   mixed (class, T, N1, N2, N3, D1, D2, D3) types: %d' % len(types))
    if nm.startswith('15'): T15 = types
    else: T12 = types
print('type sets equal:', T12 == T15)
# store for the certificate check
import json
json.dump(sorted(T12), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'types7_ref.json'), 'w'))
