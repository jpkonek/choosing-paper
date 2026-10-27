"""Prop 5.2 check: small splice X = T[A -> C_b] along a single-shift edge b = u o (1 + t e_w);
the weaker shift C_{u o (1 + t' e_w)} with t' below the threshold where it reaches A passes every
guidance-level necessary condition for committed {T, C_b} (exact atom check, all cells of L).
Also the transported version at a rescaled source a (Theorem 7.1): same verdicts for a o X."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from geo75 import *

def run(a, w, t):
    b = tuple(a[i] * (1 + t if i == w else 1) for i in range(3))
    allok = True; n = 0
    for tp in (t / 8, t / 4, t / 2, 3 * t / 4):
        m = tuple(a[i] * (1 + tp if i == w else 1) for i in range(3))
        cs = cells([a, b, m])
        for ci, c in enumerate(cs):
            h = c['pt']
            if answer(a, h) == answer(b, h): continue
            if answer(m, h) != answer(a, h): continue        # A must lie where C_m still sides with the source
            atoms = []
            for cj, d in enumerate(cs):
                g = d['pt']; tv, dv, bv = answer(a, g), answer(b, g), answer(m, g)
                atoms.append({'cell': cj, 'h': g, 'vals': {'T': tv, 'D': dv, 'B': bv, 'X': tv}})
                if cj == ci:
                    atoms.append({'cell': cj, 'h': g, 'vals': {'T': tv, 'D': dv, 'B': bv, 'X': dv}})
            rep = candidate_check(atoms, ['T', 'D'])
            n += 1
            if not rep['ok']:
                allok = False; print('FAIL', a, w, t, tp, ci, rep)
    return allok, n

ok = True; N = 0
for a in [(F(1), F(1), F(1)), (F(21, 20), F(1), F(19, 20)), (F(9, 10), F(11, 10), F(1))]:
    for w in range(3):
        for t in (F(1, 10), F(1, 5)):
            r, n = run(a, w, t); ok &= r; N += n
print('small splices tested', N)
print('ALL PASS' if ok else 'FAIL')
