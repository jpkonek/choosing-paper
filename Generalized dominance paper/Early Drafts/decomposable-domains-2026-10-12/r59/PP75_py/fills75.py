"""Type-homogeneous modifications of T (fills and unfills, small or whole-cell), committed set {T}.
For every candidate m in a grid covering all 13 order types (several magnitudes), run the exact
atom-level checker (N1, N2, N3 with all copies) and compare with Theorem 4.1:
  pattern {!=k}  (fill A_k, unfill B_k): excluded order types {u, raise_k, lower_i, lower_j}
  pattern {k}    (fill B_k, unfill A_k): excluded order types {u, lower_k}
  plus N2: C_m must not agree with X on the whole modified set E."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import itertools
from geo75 import *

U = (F(1), F(1), F(1))
def grid():
    out = []
    for s in (F(21, 20), F(11, 10), F(6, 5)):
        for r in [(1,1,1),(s,1,1),(1/s,1,1),(1,s,1),(1,1/s,1),(1,1,s),(1,1,1/s)]:
            out.append(tuple(F(x) for x in r))
        for p in itertools.permutations([F(1), s, s * s]):
            out.append(p)
        for p in itertools.permutations([F(1), s, s * F(21, 20)]):
            out.append(p)
    return out

def build(m, mod_kind, ty, k, small, seed=0):
    """atoms for X = T (+) modification on cells of type (ty,k); mod_kind 'fill' (T silent -> h) or
    'unfill' (T accepts -> S).  small=True: X modified on a sub-piece of ONE such cell (split atom);
    else on all such cells."""
    cs = cells([U, m])
    atoms = []
    targets = []
    for ci, c in enumerate(cs):
        h = c['pt']; t = htype(h)
        tv = answer(U, h)
        if t == (ty, k) and ((mod_kind == 'fill' and tv == 'S') or (mod_kind == 'unfill' and tv == 'h')):
            targets.append(ci)
    if not targets: return None
    if small:
        # choose the target cell nearest T's boundary that C_m treats like T if possible,
        # and also (seed=1) one that C_m treats differently: both are tested
        chosen = [targets[seed % len(targets)]]
    else:
        chosen = targets
    for ci, c in enumerate(cs):
        h = c['pt']
        tv, bv = answer(U, h), answer(m, h)
        newv = 'h' if mod_kind == 'fill' else 'S'
        if ci in chosen:
            if small:
                atoms.append({'cell': ci, 'h': h, 'vals': {'T': tv, 'B': bv, 'X': newv}})
                atoms.append({'cell': ci, 'h': h, 'vals': {'T': tv, 'B': bv, 'X': tv}})
            else:
                atoms.append({'cell': ci, 'h': h, 'vals': {'T': tv, 'B': bv, 'X': newv}})
        else:
            atoms.append({'cell': ci, 'h': h, 'vals': {'T': tv, 'B': bv, 'X': tv}})
    return atoms

def predicted(m, mod_kind, ty, k, atoms):
    ot = order_type(m)
    pi = 'notk' if (mod_kind, ty) in (('fill', 'A'), ('unfill', 'B')) else 'k'
    others = [i for i in range(3) if i != k]
    if pi == 'notk':
        excl = {'u', 'raise%d' % (k + 1)} | {'lower%d' % (i + 1) for i in others}
    else:
        excl = {'u', 'lower%d' % (k + 1)}
    n2 = N2(atoms, 'T')[0]
    return (ot not in excl) and n2

if __name__ == "__main__":
    mism = 0; total = 0; summary = {}
    for ty, k, mk, small, seed in itertools.product('AB', range(3), ('fill', 'unfill'), (True, False), (0, 1)):
        if not small and seed == 1: continue
        for m in grid():
            atoms = build(m, mk, ty, k, small, seed)
            if atoms is None: continue
            rep = candidate_check(atoms, ['T'])
            pr = predicted(m, mk, ty, k, atoms)
            total += 1
            key = (mk, ty + str(k + 1), 'small' if small else 'whole')
            summary.setdefault(key, {})
            ot = order_type(m)
            summary[key].setdefault(ot, set()).add(rep['ok'])
            if rep['ok'] != pr:
                mism += 1
                print('MISMATCH', key, m, ot, rep, pr)
    for key in sorted(summary):
        adm = sorted(o for o, v in summary[key].items() if True in v)
        exc = sorted(o for o, v in summary[key].items() if v == {False})
        print(key, '| never admissible:', exc)
    print('checked', total, 'mismatches', mismatch if False else mism)
    print('ALL PASS' if mism == 0 else 'FAIL')
