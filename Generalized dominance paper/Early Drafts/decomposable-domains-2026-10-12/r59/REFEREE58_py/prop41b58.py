"""prop41b58: PP73 Prop 4.1, both orders of scales, every odd world (which world carries both signs?)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lib58 import *
G = sample(200000); g = Geo(G)
def signs(x0, x1, w):
    A0, A1 = advice(G, x0), advice(G, x1)
    L = (A0 != A1) & (g.o == w)
    imp = L & (((A1 != 0) & (A0 == 0) & g.co) | ((A1 == 0) & (A0 != 0) & ~g.co))
    return round(g.mass(imp), 5), round(g.mass(L & ~imp), 5)
for (a, ap) in ((1.10, 1.05), (1.05, 1.10), (1.03, 1.06)):
    x0 = np.log(a) * D3; x1 = np.log(ap) * (D3 + D1)
    d = x1 - x0; d = d - d.mean()
    print('m1(%.2f) -> m2(%.2f): log ratio (centred) %s; (improving, worsening) mass of own odd world, per world:'
          % (a, ap, np.round(d, 4)), [signs(x0, x1, w) for w in range(3)])
x0 = np.zeros(3)
for (s, t) in ((0.06, 0.03), (0.03, 0.06)):
    x1 = s * D3 + t * D1
    print('u -> s d3 + t d1 (s=%.2f,t=%.2f): log %s;' % (s, t, np.round(x1, 3)), [signs(x0, x1, w) for w in range(3)])
