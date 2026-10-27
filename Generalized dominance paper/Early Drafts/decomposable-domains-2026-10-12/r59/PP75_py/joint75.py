"""Joint copy-defeat (Theorem J): two installed dominations B1 <= X1, B2 <= X2 (all worlds), committed T.
A record (S : T -> B) with B1 = B2 on S is the same record for both, so its refused worlds are the
union of those forced by either domination; T must keep an unblocked world against T[S -> B1].
X1 = small class-3 A-fill of T, X2 = small class-1 A-fill of T.  For grid pairs (B1, B2), each
individually admissible (Theorem 4.1/C), search exhaustively for a jointly defeating S."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import itertools
from geo75 import *
from fills75 import grid, U
from theoremC75 import closed_forms

def silent_cell(cs, ty, k, avoid):
    for ci, c in enumerate(cs):
        h = c['pt']
        if htype(h) == (ty, k) and answer(U, h) == 'S' and all(answer(b, h) == 'S' for b in avoid):
            return ci
    return None

def joint_defeat(atoms):
    # S lives on atoms with T != B1 = B2.  modes per world: 'R1','R2','G'
    for modes in itertools.product(('R1', 'R2', 'G'), repeat=3):
        allowed = []; feas = True
        for a in atoms:
            h = a['h']; v = a['vals']; t = v['T']
            st = []
            inok = (v['B1'] == v['B2'] != t)
            outok = True
            for w, md in enumerate(modes):
                if md == 'G':
                    inok = inok and strictly(v['B1'], t, h, w)
                else:
                    r = md[1]; X, B = v['X' + r], v['B' + r]
                    inok = inok and better_eq(X, t, h, w)
                    outok = outok and better_eq(X, B, h, w)
            if outok: st.append('out')
            if inok: st.append('in')
            if inok and outok: st.append('split')
            if not st: feas = False; break
            allowed.append(st)
        if not feas: continue
        # need S nonnull; for each R_r mode used, X_r differs from Y^r_S = B_r[S->T] somewhere
        need = set(md for md in modes if md != 'G')
        idx_in = [i for i, st in enumerate(allowed) if 'in' in st or 'split' in st]
        if not idx_in: continue
        ok = True
        for r in need:
            rr = r[1]
            def diff(a, s):
                v = a['vals']
                return (s in ('in', 'split') and v['X' + rr] != v['T']) or (s in ('out', 'split') and v['X' + rr] != v['B' + rr])
            if not any(diff(atoms[i], s) for i in range(len(atoms)) for s in allowed[i]):
                ok = False
        if ok: return modes
    return None

pairs = jd = 0; examples = []; rec = []
G = [m for m in grid() if order_type(m) not in ('u',)]
for B1 in G:
    for B2 in G:
        cs = cells([U, B1, B2])
        c3 = silent_cell(cs, 'A', 2, [B1, B2]); c1 = silent_cell(cs, 'A', 0, [B1, B2])
        if c3 is None or c1 is None: continue
        atoms = []
        for ci, c in enumerate(cs):
            h = c['pt']; t = answer(U, h)
            base = {'T': t, 'B1': answer(B1, h), 'B2': answer(B2, h)}
            atoms.append({'cell': ci, 'h': h, 'vals': dict(base, X1=t, X2=t)})
            if ci == c3: atoms.append({'cell': ci, 'h': h, 'vals': dict(base, X1='h', X2=t)})
            if ci == c1: atoms.append({'cell': ci, 'h': h, 'vals': dict(base, X1=t, X2='h')})
        def proj(r):
            return [{'cell': a['cell'], 'h': a['h'], 'vals': {'T': a['vals']['T'], 'B': a['vals']['B' + r], 'X': a['vals']['X' + r]}} for a in atoms]
        ok1 = candidate_check(proj('1'), ['T'])['ok']; ok2 = candidate_check(proj('2'), ['T'])['ok']
        if not (ok1 and ok2): continue
        pairs += 1
        md = joint_defeat(atoms)
        rec.append((B1, B2, md is not None))
        if md:
            jd += 1
            if len(examples) < 12: examples.append((order_type(B1), order_type(B2), [str(x) for x in B1], [str(x) for x in B2], md))
print('individually admissible pairs', pairs, 'jointly defeating', jd)
for e in examples: print('  ', e)
same = sum(1 for e in examples if e[2] == e[3])
print('done')

# summary by B1: same-model cases, distinct-model cases, and survival of some B2
import collections
same = sum(1 for b1, b2, d in rec if d and b1 == b2)
samepairs = sum(1 for b1, b2, d in rec if b1 == b2)
dist = sum(1 for b1, b2, d in rec if d and b1 != b2)
print('same-model pairs', samepairs, 'of which jointly defeated', same)
print('distinct-model jointly defeated pairs', dist)
by = collections.defaultdict(list)
for b1, b2, d in rec: by[b1].append(d)
print('every B1 has a jointly surviving B2:', all(not all(v) for v in by.values()))
