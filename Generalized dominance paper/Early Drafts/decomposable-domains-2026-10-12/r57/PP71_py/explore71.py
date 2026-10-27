"""explore71: pointwise necessary conditions for a uniform 4-cycle C1->C2->C3->C4->C1
(C_{i+1} dominates every class-3 fill of C_i).  NUMERICS on samples (exact arithmetic per sample)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom71 import *

def seg(theta, lam):
    d = (theta, 1 - theta, -1)
    return [v3, tuple(v3[i] + lam * d[i] for i in range(3))]

def report(Ks, names, G):
    C = census(Ks, G)
    n = len(Ks)
    for key in sorted(C):
        print('  class %d %s  n=%d' % (key[0], ''.join(key[1]), len(C[key])))
    def better(i, j, w):   # model j strictly w-better than model i somewhere
        return any(rank(k, a[j], w) < rank(k, a[i], w) for (k, a) in C)
    ok = True
    for i in range(n):
        j = (i + 1) % n
        sil = any(k == 3 and a[i] == 'S' for (k, a) in C)
        agree = not any(k == 3 and a[i] == 'S' and a[j] == 'A' for (k, a) in C)
        g12 = better(i, j, 1) and better(i, j, 2)
        not3 = better(j, i, 3)   # C_i strictly 3-better somewhere than C_{i+1}
        print('  edge %s->%s: C_i silent on M3 %s; agreement exclusion %s; C_j 1-,2-gain %s; C_j 3-loss %s'
              % (names[i], names[j], sil, agree, g12, not3))
        ok &= sil and agree and g12 and not3
    for i in range(n):
        for j in range(n):
            if i < j:
                m3 = better(i, j, 3) and better(j, i, 3)
                print('  pair %s,%s 3-mixed: %s' % (names[i], names[j], m3))
    return ok

if __name__ == '__main__':
    G = exact_points([seg(t, F(1, 5)) for t in [F(9, 10), F(13, 20), F(7, 20), F(1, 10)]] + [seg(t, F(3, 10)) for t in [F(9, 10), F(13, 20), F(7, 20), F(1, 10)]])
    th = [F(9, 10), F(13, 20), F(7, 20), F(1, 10)]
    for lam in [F(1, 5), F(3, 10)]:
        Ks = [seg(t, lam) for t in th]
        print('segments [v3, v3 + lam(theta,1-theta,-1)], lam =', lam, 'theta =', th)
        print('  necessary conditions:', report(Ks, ['C1', 'C2', 'C3', 'C4'], G))
