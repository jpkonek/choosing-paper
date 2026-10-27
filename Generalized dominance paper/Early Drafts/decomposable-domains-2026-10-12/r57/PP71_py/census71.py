"""census71: exact face enumeration (geom71.exact_points) versus the sampled census.
(1) the single cycle (lam = 1/5), with and without T: does sampling miss any type?
(2) two cycles lam = 1/5, lam': exact type sets as lam' -> 1/5 (stability of the joint census).
Run: python3 -I -B census71.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom71 import *
from cycle71 import seg, TH
def types(Ks, G):
    return set((cls(g), tuple(adv(K, g) for K in Ks)) for g in G)
base = [seg(t, F(1, 5)) for t in TH]
KT = list(V)
S = samples(6, 3000)
for name, Ks in [('cycle', base), ('cycle + T', base + [KT])]:
    E = exact_points(Ks)
    te, ts = types(Ks, E), types(Ks, S)
    print('%-10s exact types %d (from %d face points); sampled %d; missed by sampling: %s; extra in sample: %s'
          % (name, len(te), len(E), len(ts), sorted(te - ts), sorted(ts - te)))
prev = None
for l2 in [F(11, 50), F(21, 100), F(201, 1000), F(2001, 10000)]:
    Ks = base + [seg(x, l2) for x in TH]
    te = types(Ks, exact_points(Ks))
    ts = types(Ks, S)
    print("lam' = %-10s exact types %d; sampled %d (missed %d); same exact type set as previous: %s"
          % (l2, len(te), len(ts), len(te - ts), te == prev))
    prev = te
