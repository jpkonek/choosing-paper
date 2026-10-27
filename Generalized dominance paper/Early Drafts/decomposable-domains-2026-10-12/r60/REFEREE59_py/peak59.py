"""peak59: sup alpha/p and sup alphaA/p on the (2V) range of the k = 3 down-shift ray.
Geometric grid in delta = 1 - lam (ratio 1.01) from 1e-6 to the (2V) edge lam = 7/16, plus a bound valid on the
whole interval [1e-6, 9/16] by monotonicity: alpha, beta, alphaA are non-decreasing in delta (nested layers), so
on [delta_j, delta_{j+1}]:  alpha/p <= alpha(d_{j+1}) / (alpha(d_{j+1}) + beta(d_j)),  alphaA/p <= alphaA(d_{j+1}) / p(d_j).
(Below delta = 1e-6 the limit 2/3 resp. 0.4891 is PROVED / computed in layer59.)"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib59 import *
from layer59 import layer
ds = []
d = F(1, 10 ** 6)
while d < F(9, 16):
    ds.append(d)
    d = F(round(float(d) * 1.01 * 10 ** 12), 10 ** 12)
ds.append(F(9, 16) - F(1, 10 ** 9))
vals = []
for d in ds:
    m = layer(2, 1 - d)
    vals.append((d, m['odd'][2], m['odd'][0], m['gainA']))
best = max(vals, key=lambda v: v[1] / (v[1] + v[2]))
bestA = max(vals, key=lambda v: v[3] / (v[1] + v[2]))
print('grid points: %d' % len(vals))
print('grid max alpha/p  = %.6f at lam = %.4f' % (best[1] / (best[1] + best[2]), 1 - float(best[0])))
print('grid max alphaA/p = %.6f at lam = %.4f' % (bestA[3] / (bestA[1] + bestA[2]), 1 - float(bestA[0])))
ub = max(vals[j + 1][1] / (vals[j + 1][1] + vals[j][2]) for j in range(len(vals) - 1))
ubA = max(vals[j + 1][3] / (vals[j][1] + vals[j][2]) for j in range(len(vals) - 1))
print('bounds valid on all of 1e-6 <= 1 - lam <= 9/16: alpha/p <= %.4f ; alphaA/p <= %.4f' % (ub, ubA))
print('=> theta* = (1-a)/(1+a) >= %.4f (alpha route), %.4f (alphaA route)' % ((1 - ub) / (1 + ub), (1 - ubA) / (1 + ubA)))
