"""REFEREE round 54: exact check of PP56 Prop 5.2 (the one-parameter staircase), independent of kink56.py.

Every clause is a condition on which closed intervals contain one point s, or on an ordered pair s < s'.
All six sets are closed intervals with endpoints in E = {0, 3/8, 1/2, 3/2, 13/8, 2}.  The truth value of every
one-point clause is constant on each atom of the partition of [0,2] into the points of E and the open gaps
between them; for the two-point (TC) clauses it is constant on ordered pairs of atoms, plus pairs inside one
open gap.  So checking the points of E, two interior points of every gap, and all ordered pairs of these is a
complete (exact) check, not a grid sample.
Sign data (strict guidance): X_s improves at world 1 and worsens at worlds 2, 3 as s increases.
"""
from fractions import Fraction as Fr
import itertools

F = [(Fr(0), Fr(1, 2)), (Fr(1, 2), Fr(2)), (Fr(13, 8), Fr(2))]
G = [(Fr(3, 2), Fr(2)), (Fr(0), Fr(3, 8)), (Fr(0), Fr(3, 2))]
inn = lambda I, s: I[0] <= s <= I[1]
E = sorted({x for I in F + G for x in I})
pts = list(E)
for a, b in zip(E, E[1:]):
    pts += [a + (b - a) / 3, a + 2 * (b - a) / 3]
pts.sort()
ok = True
for s in pts:
    Fs = [inn(I, s) for I in F]
    Gs = [inn(I, s) for I in G]
    ok &= any(Fs) and any(Gs)                    # A's defence; B's and D's defences (via (IB), record D1)
    ok &= not all(Fs) and not all(Gs)            # protection with direct (C) on both sides
    ok &= not any(f and g for f, g in zip(Fs, Gs))  # no single-world tie
ok &= [inn(I, 0) for I in F] == [True, False, False] and [inn(I, 0) for I in G] == [False, True, True]
ok &= [inn(I, 2) for I in F] == [False, True, True] and [inn(I, 2) for I in G] == [True, False, False]
for s, sp in itertools.combinations(pts, 2):     # s < sp
    ok &= not (inn(F[0], sp) and inn(G[0], s))   # world 1: X_sp strictly better than X_s
    for w in (1, 2):
        ok &= not (inn(F[w], s) and inn(G[w], sp))   # worlds 2, 3: X_s strictly better than X_sp
print('points checked:', len(pts), '; staircase satisfies every listed clause (exact):', ok)
print('NOTE: the parameter s indexes the RIVAL X_s with the source A fixed; closedness of F_w, G_w is closedness')
print('      along a changing-rival path (PP52 / Ct+ type), not (S) fixed-rival closedness in the source index.')
print('ALL PASS' if ok else 'FAIL')
