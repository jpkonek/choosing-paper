"""S2 numerics (3): three-world additive edge face.

On the edge e_12 a non-null tie set Z (cells of R_12 where (1-s0) rho1 = s0 rho2) is a face: every split
of Z has the same (psi1, psi2) once its rho1-level is fixed. Undominated face members at a level are
the psi3-minimal splits (Neyman-Pearson in the ratio f = world-3 gain per unit rho1). We check on random
discretisations (cells of equal rho1-mass, i.e. exchangeable pieces) that
 (a) the psi3-optimal splits form a nested family as the level varies, when f has no ties;
 (b) when f has a flat block, two optimal splits at different levels may cross inside the block, and
     then an equal-profile (psi1, psi2, psi3) splice exists, so (C) fails.
Cells carry: rho1 (=1), sign of h_3 (world-3 error flips with acceptance), rho3 > 0.
'Erring at world 1' on a cell of Z (h1>0>h2 or h1<0<h2) flips world-3 correctness: the world-3 cost of
world-1 error on cell c is w(c) = +rho3 if that advice is world-3-wrong, -rho3 otherwise.
"""
import random, itertools
random.seed(3)

def np_split(w, level):
    order = sorted(range(len(w)), key=lambda c: w[c])          # cheapest world-3 cost first
    return frozenset(order[:level])

def nested(fam):
    return all(a <= b or b <= a for a, b in itertools.combinations(fam, 2))

ok = True
for trial in range(500):
    m = random.randint(3, 12)
    w = [random.uniform(-1, 1) for _ in range(m)]               # generic: no ties
    fam = [np_split(w, l) for l in range(m + 1)]
    ok &= nested(fam)
print('(a) NP splits nested across levels (500 random faces, no ties):', ok)

# (b) a flat block: cells 0..3 have equal w; NP optimal sets at levels 1..3 may be any subsets of the block
w = [0.0, 0.0, 0.0, 0.0, 0.5, 0.7]
optimal = {l: [frozenset(S) for S in itertools.combinations(range(4), l)] for l in range(1, 4)}
A1, A2 = optimal[1][0], optimal[2][-1]
print('(b) level-1 optimum', sorted(A1), 'level-2 optimum', sorted(A2), 'crossing:',
      not (A1 <= A2 or A2 <= A1))
splice = optimal[1][1]
prof = lambda S: (len(S), sum(w[c] for c in S))
print('    equal (level, psi3) profile of two distinct level-1 optima', sorted(A1), sorted(splice), ':',
      prof(A1) == prof(splice))
