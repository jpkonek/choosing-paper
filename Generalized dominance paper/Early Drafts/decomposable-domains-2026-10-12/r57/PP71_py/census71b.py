"""census71b: exact joint census of two segment cycles (lam, lam') for several base values lam and
lam' slightly larger; and for a theta-rotated second cycle.  Compares the type sets (classes x patterns of
the 8 models, ordered C1..C4, C'1..C'4).  Run: python3 -I -B census71b.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom71 import *
from cycle71 import seg, TH
def types(Ks):
    return frozenset((cls(g), tuple(adv(K, g) for K in Ks)) for g in exact_points(Ks))
ref = None
for lam, l2 in [(F(1, 5), F(11, 50)), (F(1, 5), F(2001, 10000)), (F(21, 100), F(211, 1000)),
                (F(1, 4), F(2501, 10000)), (F(29, 100), F(2901, 10000)), (F(3, 10), F(3001, 10000))]:
    t = types([seg(x, lam) for x in TH] + [seg(x, l2) for x in TH])
    if ref is None:
        ref = t
    print("lam = %-7s lam' = %-11s types %d  same as (1/5, 11/50): %s" % (lam, l2, len(t), t == ref))
for d in [F(1, 100), F(1, 1000)]:
    t = types([seg(x, F(1, 5)) for x in TH] + [seg(x + d, F(1, 5)) for x in TH])
    print("theta-rotation d = %-7s types %d" % (d, len(t)))
