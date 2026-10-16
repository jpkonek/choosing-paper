# NUMERICS (sanity only) for P4 Theorem B1 (n = 2, nested chain c_b = [0,b)).
# World 1 is lexicographic with countably additive levels w_1, w_2 (piecewise-constant densities
# on a grid of M cells).  Sets A are unions of cell fractions (each cell [x,x+h) contributes its
# initial fraction f in [0,1]); every measure below is then exact.
# (1) out-of-order levels (w_1 = 0 on an initial piece, > 0 later): A = c_b \ (Z cap c_a) has
#     c_{b'} <=_1 A for b' < b near b but not c_b <=_1 A: the section is not closed.
# (2) in-order levels: nu = density of the first positive level satisfies nu(A) >= nu(c_b)
#     for every sampled comparison c_b <=_1 A.
import numpy as np
from fractions import Fraction as Fr
rng = np.random.default_rng(3)
M = 40; h = Fr(1, M)
def lexle(x, y):              # x <=_lex y for tuples
    for a, b in zip(x, y):
        if a < b: return True
        if a > b: return False
    return True
def val(fr, w):               # valuation of set with cell fractions fr under densities w
    return tuple(sum(Fr(f)*h*Fr(wk[i]) for i, f in enumerate(fr)) for wk in w)
def chain(b):                 # cell fractions of [0,b)
    fr = []
    for i in range(M):
        lo = Fr(i, M)
        fr.append(min(max((b-lo)/h, 0), 1))
    return fr
# (1) out of order: w1 = 0 on [0,0.3), 1 on [0.3,1); w2 = 1 everywhere
w = [[0 if i < 12 else 1 for i in range(M)], [1]*M]
b = Fr(7, 10); a = Fr(3, 10)
A = chain(b); A = [0 if i < 12 else f for i, f in enumerate(A)]   # remove c_a (all of Z cap c_a)
vA = val(A, w)
ok_below = all(lexle(val(chain(b - Fr(1, 10**k)), w), vA) for k in range(2, 8))
at_b = lexle(val(chain(b), w), vA)
print('(1) c_{b-eta} <=_1 A for eta=1e-2..1e-7:', ok_below, '; c_b <=_1 A:', at_b,
      '=> section of A not closed:', ok_below and not at_b)
# (2) in order: levels enter along the chain in order 1,1,...,2,2
w = [[rng.integers(1, 5) if i < 25 else 0 for i in range(M)],
     [rng.integers(0, 5) if i < 25 else rng.integers(1, 5) for i in range(M)]]
nu = [w[0][i] if i < 25 else w[1][i] for i in range(M)]
viol = 0; tested = 0
for t in range(20000):
    bb = Fr(int(rng.integers(0, 401)), 400)
    fr = [Fr(int(x), 8) for x in rng.integers(0, 9, M)]
    if rng.random() < 0.5:                       # often contain the first region
        fr = [Fr(1) if i < 25 and rng.random() < 0.9 else f for i, f in enumerate(fr)]
    if lexle(val(chain(bb), w), val(fr, w)):
        tested += 1
        if val(fr, [nu])[0] < val(chain(bb), [nu])[0]: viol += 1
print('(2) sampled comparisons c_b <=_1 A:', tested, '; violations of nu(A) >= nu(c_b):', viol)
