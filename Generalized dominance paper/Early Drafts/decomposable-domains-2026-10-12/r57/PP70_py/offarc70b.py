"""offarc70b: Bayes acts of PP69's field at small off-arc perturbations of arc weights (PP70 §2.7).
lam = p(theta) + eps*d, d in {(1,-1,0), (1,0,-1)/.., (0,1,-1)..} normalised; same coherence test as offarc70.
NUMERICS.  Run: python3 -I -B offarc70b.py > offarc70b.out
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from offarc70 import bayes, coherent_test
random.seed(7072)
G = [tuple(Fr(random.randint(-300, 300), random.randint(1, 30)) for _ in range(3)) for _ in range(700)]
G = [g for g in G if all(x != 0 for x in g) and g[0] + g[1] != 0]
for th in (0.15, 0.5, 0.85):
    p = ((2 + th) / 6, (2 + th) / 6, (2 - 2 * th) / 6)
    for d, dn in (((1, -1, 0), 'tilt 1 vs 2'), ((1, 0, -1), 'tilt 1 vs 3')):
        for eps in (0.02, 0.005):
            lam = tuple(pi + eps * di for pi, di in zip(p, d))
            v, bad = coherent_test(G, [bayes(g, lam) for g in G])
            print('theta=%.2f %-12s eps=%.3f  %-20s forced silent: %s' % (th, dn, eps, v, bad))
