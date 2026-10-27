"""explore72: pointwise structure of one loop (exact census).  For each ordered pair of loop members and each
class, list the cells where they differ, and the pointwise world-by-world status of each loop edge."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom72 import *
b = F(sys.argv[1]) if len(sys.argv) > 1 else F(5, 4)
L = loop(b)
names = ['T', 'C1', 'C2']
Ks = [post(L[n]) for n in names]
print('scale b =', b, ' (2V):', [in2V(L[n]) for n in names])
G = exact_points(Ks)
C = census(Ks, G)
print('cells (class, advice T C1 C2):', len(C))
for key in sorted(C):
    if len(set(key[1])) > 1 or 'S' in key[1]:
        print('  ', key[0], ''.join(key[1]))
def ptw(i, j):
    """status of rec(Ci -> Cj) at each world: '+' new side pointwise no worse..."""
    out = []
    for w in (1, 2, 3):
        better = worse = False
        for (k, a) in C:
            if k == 0 or a[i] == a[j]: continue
            ro, rn = rank(k, a[i], w), rank(k, a[j], w)
            if rn < ro: better = True
            if rn > ro: worse = True
        out.append({(True, False): 'new better', (False, True): 'new worse', (True, True): 'mixed', (False, False): 'equal'}[(better, worse)])
    return out
for i, j in [(0, 1), (1, 2), (2, 0)]:
    print('rec(%s -> %s):' % (names[i], names[j]), ptw(i, j))
