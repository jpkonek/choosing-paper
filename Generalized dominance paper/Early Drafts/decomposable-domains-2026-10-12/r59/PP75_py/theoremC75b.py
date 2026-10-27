"""Theorem C on the structured configurations (fills, mixed fills, splices), every committed model:
closed forms (N1, N2, defeat) versus the brute-force atom checker."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import itertools
from geo75 import *
from theoremC75 import closed_forms
import fills75, mixed75, splice75

tot = mism = nd = 0
def cmp(atoms, Z):
    global tot, mism, nd
    b = (N1(atoms)[0], N2(atoms, Z)[0], defeated(atoms, Z) is not None)
    c = closed_forms(atoms, Z)[:3]
    tot += 1; nd += b[2]
    if b != c:
        mism += 1; print('MISMATCH', Z, b, c)
for ty, k, mk, small in itertools.product('AB', range(3), ('fill', 'unfill'), (True, False)):
    for m in fills75.grid()[::2]:
        a = fills75.build(m, mk, ty, k, small)
        if a: cmp(a, 'T')
for pieces in list(itertools.combinations(mixed75.ELEM, 2))[::3]:
    for m in fills75.grid()[:33:2]:
        a = mixed75.build(m, pieces)
        if a: cmp(a, 'T')
for bn, b in splice75.BS.items():
    b = tuple(F(x) for x in b)
    for which in pattern_formula(b):
        for mode in ('small', 'whole'):
            for m in splice75.mgrid()[::2]:
                a = splice75.build(b, m, mode, which)
                if a:
                    cmp(a, 'T'); cmp(a, 'D')
print('comparisons', tot, 'brute-force defeats', nd, 'mismatches', mism)
print('ALL PASS' if mism == 0 else 'FAIL')
