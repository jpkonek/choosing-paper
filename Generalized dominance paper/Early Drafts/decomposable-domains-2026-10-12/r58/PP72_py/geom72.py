"""geom72: exact geometry of the rescaling loop (PP72).
Index m (unnormalised positive vector); C_m = D_{M_m}; vertices of M_m are m o v, v in vert M (normalisation
irrelevant for advice).  Loop at scale b = a^3:  u=(1,1,1) -> m1=(b,b,1) -> m2=(1,b,1) -> u.
Advice conventions are PP71's geom71 (A = majority sign, correct at the two worlds != class)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'PP71_py'))
from geom71 import F, V, dot, sgn, cls, maj, adv, rank, exact_points, census

def post(m):
    return [tuple(m[i] * v[i] for i in range(3)) for v in V]

def loop(b):
    b = F(b)
    return {'T': (F(1), F(1), F(1)), 'C1': (b, b, F(1)), 'C2': (F(1), b, F(1))}

def shift(m, k, c):
    """multiply world k's likelihood by 1/c (c>1: pure decrease of world k)"""
    return tuple(m[i] / c if i == k - 1 else m[i] for i in range(3))

def in2V(m, eta=F(1, 100)):
    c = (1 - F(3, 10)) / 3
    r = [1 / x for x in m]; s = sum(r)
    return all(x / s >= c + eta for x in r)
