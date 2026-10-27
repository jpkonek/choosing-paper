"""Mixed small modifications of T (two or three small pieces of different elementary kinds),
committed {T}.  Prediction (Theorem 4.2, generic position): with Pi = set of patterns of T -> X and
F = intersection of Pi (worlds where X is pointwise better than T):
  excluded order types = {u} u {lower_j : j in F} u {raise_k : F = {!=k}}  (+ N2).
Exact atom-level check over the 13-order-type grid.
RESULT: this naive "generic position" rule is FALSE in general (a small piece can lie inside C_m's
own change region, so a pattern is shared rather than unshared); the correct statement is Theorem C
(closed forms in the unshared pattern sets P1, P2), which is checked here on the same configurations (every 3rd combination, 17 candidates)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import itertools
from geo75 import *
from fills75 import grid, U
from theoremC75 import closed_forms

ELEM = [(mk, ty, k) for mk in ('fill', 'unfill') for ty in 'AB' for k in range(3)]
def elem_pattern(mk, ty, k):
    if (mk, ty) in (('fill', 'A'), ('unfill', 'B')):
        return frozenset(i for i in range(3) if i != k)
    return frozenset([k])

def build(m, pieces):
    cs = cells([U, m])
    chosen = {}
    for (mk, ty, k) in pieces:
        for ci, c in enumerate(cs):
            h = c['pt']; tv = answer(U, h)
            if htype(h) == (ty, k) and ((mk == 'fill' and tv == 'S') or (mk == 'unfill' and tv == 'h')):
                if ci not in chosen:
                    chosen[ci] = 'h' if mk == 'fill' else 'S'; break
        else:
            return None
    atoms = []
    for ci, c in enumerate(cs):
        h = c['pt']; tv, bv = answer(U, h), answer(m, h)
        atoms.append({'cell': ci, 'h': h, 'vals': {'T': tv, 'B': bv, 'X': tv}})
        if ci in chosen:
            atoms.append({'cell': ci, 'h': h, 'vals': {'T': tv, 'B': bv, 'X': chosen[ci]}})
    return atoms

def predicted(m, pieces, atoms):
    Pi = [elem_pattern(*p) for p in pieces]
    Fw = set(range(3))
    for P in Pi: Fw &= P
    excl = {'u'} | {'lower%d' % (j + 1) for j in Fw}
    if len(Fw) == 2:
        k = [i for i in range(3) if i not in Fw][0]
        excl.add('raise%d' % (k + 1))
    return (order_type(m) not in excl) and N2(atoms, 'T')[0]

if __name__ == "__main__":
    mism = 0; tot = 0; mismC = 0
    for r in (2, 3):
        for pieces in list(itertools.combinations(ELEM, r))[::3]:
            if r == 3 and len(set(elem_pattern(*p) for p in pieces)) < 2: continue
            for m in grid()[:33:2]:
                atoms = build(m, pieces)
                if atoms is None: continue
                rep = candidate_check(atoms, ['T'])
                pr = predicted(m, pieces, atoms)
                n1, n2, d, P1, P2 = closed_forms(atoms, 'T')
                if rep['ok'] != (n1 and n2 and not d): mismC += 1
                tot += 1
                if rep['ok'] != pr:
                    mism += 1
                    if mism < 4: print('MISMATCH', pieces, m, order_type(m), rep['N1w'], rep['N2'], rep['N3'], pr)
    print('checked', tot, 'mismatches', mism)
    print('naive rule mismatches (expected nonzero):', mism)
    print('Theorem C mismatches:', mismC)
    print('ALL PASS (Theorem C)' if mismC == 0 else 'FAIL')
