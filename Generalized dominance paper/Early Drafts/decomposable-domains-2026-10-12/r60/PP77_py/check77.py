"""check77 (NUMERICS, lib78 sample of PP78): hypotheses of PP77 Section 5 on the continuous star.
 [a] mass window for the outer-full family: gamma = p(t1)-p(tau); need (1+theta) gamma/2 <= beta(tau) < 2 gamma
 [b] (H1): the outer odd-2 shell Sh2 = L3^(2)(t1) \\ L3(tau) is NOT inside L1(t1)   (mass outside > 0)
 [c] L3^(2)(tau) \\ L1(t1) non-null (room for radially non-conic G);  L3^(2)(s) n L1(t1) non-null for small s
 [d] (Y): odd-3 points with T silent and h correct at worlds 1,2, outside L3(t1): mass >= beta(t1)
 [e] increment ratio (alpha(t)-alpha(s))/(beta(t)-beta(s)) in [3/2, 5/2] (used for q3 > q1)
Run: python3 -I -B check77.py > check77.out"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP78_py'))
import numpy as np
from lib78 import *
G = sample(int(os.environ.get('NS', '400000')))
g = Geo(G)
t1 = 0.05
L3 = {t: g.member(2, t) != g.T for t in (0.005, 0.01, 0.02, 0.03, 0.035, 0.04, 0.045, 0.05)}
L1t1 = g.member(0, t1) != g.T
odd = lambda o: g.o == o
def ab(t):
    return g.mass(L3[t] & odd(2)), g.mass(L3[t] & odd(0)), g.mass(L3[t] & odd(1))
a1, b1, b1b = ab(t1)
print('t1=%.3f alpha=%.5f beta1=%.5f beta2=%.5f p=%.5f' % (t1, a1, b1, b1b, a1 + b1))
print('[a] window and [b],[c] per tau:')
for tau in (0.02, 0.03, 0.035, 0.04):
    a, b, _ = ab(tau); gam = (a1 + b1) - (a + b)
    Sh2 = L3[t1] & ~L3[tau] & odd(1)
    print('  tau=%.3f beta(tau)/beta(t1)=%.3f gamma=%.5f  window [(1.1)g/2 <= beta < 2g]: %s | Sh2 mass %.5f, outside L1(t1) %.5f | L3^(2)(tau)\\L1(t1) %.5f'
          % (tau, b / b1, gam, 1.1 * gam / 2 <= b < 2 * gam, g.mass(Sh2), g.mass(Sh2 & ~L1t1), g.mass(L3[tau] & odd(1) & ~L1t1)))
for s in (0.005, 0.01, 0.02):
    print('  [c] mass L3^(2)(%.3f) n L1(t1) = %.6f' % (s, g.mass(L3[s] & odd(1) & L1t1)))
Y = odd(2) & (g.T == 0) & ~g.co & ~L3[t1]
print('[d] Y mass %.5f  vs beta(t1) %.5f' % (g.mass(Y), b1))
print('[e] increment ratios:')
ts = sorted(L3)
for i in range(len(ts) - 1):
    s, t = ts[i], ts[i + 1]
    (as_, bs, _), (at, bt, _) = ab(s), ab(t)
    print('   (%.3f,%.3f): %.3f' % (s, t, (at - as_) / (bt - bs)))
print('[f] mirror family S_o^b (holes in L3^(1)(tau), covers by ray 2):')
L2t1 = g.member(1, t1) != g.T
for tau in (0.035, 0.04):
    a, b, _ = ab(tau); gam = (a1 + b1) - (a + b)
    Sh1 = L3[t1] & ~L3[tau] & odd(0)
    C1 = L3[tau] & odd(0) & L2t1
    print('  tau=%.3f: beta(tau)=%.5f gamma=%.5f  (1.1)g/2<=beta: %s  beta<=gamma: %s | Sh1 outside L2(t1) %.5f of %.5f | mass C\' %.5f'
          % (tau, b, gam, 1.1 * gam / 2 <= b, b <= gam, g.mass(Sh1 & ~L2t1), g.mass(Sh1), g.mass(C1)))
    for s in (0.005, 0.01):
        print('     L3^(1)(%.3f) n L2(t1) = %.6f' % (s, g.mass(L3[s] & odd(0) & L2t1)))
