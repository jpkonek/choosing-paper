"""Forced refusals of committed family members (Theorem 4.1(c) and Theorem C) for X = small class-3
A-fill of T.  Committed: T and Z = C_c with c on the lower-1, lower-2, lower-3, raise-1 rays.
Reports base refusal worlds F(Z,X) (independent of m) and, over the candidate grid, which order
types of m/c are removed by Z's copy-defeat (exact atom checker)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from geo75 import *
from fills75 import grid, U

q = F(10, 11)
FAM = {'lower1': (q, 1, 1), 'lower2': (1, q, 1), 'lower3': (1, 1, q), 'raise1': (1 / q, 1, 1)}
for name, c in FAM.items():
    c = tuple(F(x) for x in c)
    removed = {}; base = None
    for m in grid():
        if m == c: continue
        cs = cells([U, c, m])
        tgt = None
        for ci, cc in enumerate(cs):
            h = cc['pt']
            if htype(h) == ('A', 2) and answer(U, h) == 'S' and answer(c, h) == 'S' and answer(m, h) == 'S':
                tgt = ci; break
        if tgt is None: continue
        atoms = []
        for ci, cc in enumerate(cs):
            h = cc['pt']; v = {'T': answer(U, h), 'Z': answer(c, h), 'B': answer(m, h)}
            atoms.append({'cell': ci, 'h': h, 'vals': dict(v, X=v['T'])})
            if ci == tgt: atoms.append({'cell': ci, 'h': h, 'vals': dict(v, X='h')})
        base = base_refusals(atoms, 'Z')
        d = defeated(atoms, 'Z')
        r = order_type(tuple(m[i] / c[i] for i in range(3)))
        if d is not None: removed.setdefault(r, set()).add(order_type(m))
    print('committed Z = C_%s (%s): base refusal worlds %s; copy-defeat removes m with ot(m/c) in %s'
          % (tuple(str(x) for x in c), name, [w + 1 for w in base], sorted(removed)))
print('done')
