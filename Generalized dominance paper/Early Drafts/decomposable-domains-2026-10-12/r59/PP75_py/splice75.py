"""Splices X = T[A -> C_b] between two posterior models (WLOG source T by transport), committed
{T, D=C_b}.  A = a small sub-piece of one cell of the layer L = Delta(T,C_b) (arbitrarily small,
non-conic), or A = all layer cells of one pattern class.  For candidate m over a grid, exact
atom-level check of N1, N2 (both ends), N3 with copies (both ends).  Reports, per (b, A-class),
the candidate order types (of m and of m/b) that are never admissible, and whether any m is
admissible; and verifies the rule of Theorem 5.1 (see PP75 §5)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import itertools
from geo75 import *

U = (F(1), F(1), F(1))
s = F(11, 10)
BS = {'raise1': (s, 1, 1), 'lower3': (1, 1, 1 / s), 'gen123': (1, s, s * s), 'gen312': (s, s * s, 1)}
def mgrid():
    out = []
    for t in (F(21, 20), F(23, 20)):
        for r in [(t,1,1),(1/t,1,1),(1,t,1),(1,1/t,1),(1,1,t),(1,1,1/t)]:
            out.append(tuple(F(x) for x in r))
        for p in itertools.permutations([F(1), t, t * t]):
            out.append(p)
    return out

def build(b, m, mode, which):
    cs = cells([U, b, m])
    layer = [ci for ci, c in enumerate(cs) if answer(U, c['pt']) != answer(b, c['pt'])]
    pats = {}
    for ci in layer:
        h = cs[ci]['pt']
        pats.setdefault(pattern(answer(U, h), answer(b, h), h), []).append(ci)
    if which not in pats: return None
    if mode == 'small':
        A = {pats[which][0]: 'split'}
    else:
        A = {ci: 'full' for ci in pats[which]}
    atoms = []
    for ci, c in enumerate(cs):
        h = c['pt']; tv, dv, bv = answer(U, h), answer(b, h), answer(m, h)
        if ci in A:
            atoms.append({'cell': ci, 'h': h, 'vals': {'T': tv, 'D': dv, 'B': bv, 'X': dv}})
            if A[ci] == 'split':
                atoms.append({'cell': ci, 'h': h, 'vals': {'T': tv, 'D': dv, 'B': bv, 'X': tv}})
        else:
            atoms.append({'cell': ci, 'h': h, 'vals': {'T': tv, 'D': dv, 'B': bv, 'X': tv}})
    return atoms

if __name__ == "__main__":
    res = {}
    for bn, b in BS.items():
        b = tuple(F(x) for x in b)
        for which in sorted(pattern_formula(b), key=lambda P: (len(P), sorted(P))):
            for mode in ('small', 'whole'):
                key = (bn, pname(which), mode)
                for m in mgrid():
                    atoms = build(b, m, mode, which)
                    if atoms is None: continue
                    rep = candidate_check(atoms, ['T', 'D'])
                    ot1 = order_type(m); ot2 = order_type(tuple(m[i] / b[i] for i in range(3)))
                    why = []
                    if not rep['N1']: why.append('N1')
                    for Z in ('T', 'D'):
                        if not rep['N2'][Z][0]: why.append('N2' + Z)
                        if rep['N3'][Z] is not None: why.append('N3' + Z)
                    res.setdefault(key, []).append((ot1, ot2, rep['ok'], why))
    for key in res:
        adm = [(a, b2) for a, b2, ok, w in res[key] if ok]
        bad = [(a, b2, w) for a, b2, ok, w in res[key] if not ok]
        print(key, 'admissible', len(adm), 'of', len(res[key]))
        for a, b2, w in bad:
            print('    excluded: ot(m)=%s ot(m/b)=%s by %s' % (a, b2, ','.join(w)))
