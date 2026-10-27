"""layerA59: the sharper route for PP74 Lemma 4.2.  E meets L_k(t) only in its 'gain A_k' part, of mass
alphaA.  If betaA := mass of 'lose A_i' (i != k, each) satisfies 2*betaA >= alphaA, then
p = alpha + beta >= alphaA + betaA >= (3/2) alphaA, i.e. alphaA <= (2/3) p, which is exactly what theta = 1/5 needs.
Deterministic exact-cell computation on the whole (2V) range of the k = 3 down-shift ray."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib59 import *
T = post((1, 1, 1))
lams = [F(1) - F(1, 10 ** j) for j in (6, 4, 3, 2)] + [F(i, 100) for i in range(95, 43, -3)] + [F(7, 16) + F(1, 10 ** 6)]
worst = 10.0
print('   lam      alphaA      betaA(each)   2*betaA/alphaA   alphaA/p')
for lam in lams:
    cs = cells({'T': T, 'B': post(down(2, lam))})
    aA = bA = al = b1 = 0.0
    for c in cs:
        t = htype(c['pt'])
        vT, vB = c['vals']['T'], c['vals']['B']
        if t[0] == 'U' or vT == vB: continue
        s = solid(c['poly'])
        if t[1] == 2: al += s
        if t[1] == 0: b1 += s
        if t == ('A', 2) and vT == 0: aA += s
        if t == ('A', 0) and vT == 1: bA += s
    r = 2 * bA / aA; worst = min(worst, r)
    print('  %.6f  %.9f  %.9f  %.6f  %.6f' % (float(lam), aA, bA, r, aA / (al + b1)))
print('min over grid of 2*betaA/alphaA = %.6f' % worst)
