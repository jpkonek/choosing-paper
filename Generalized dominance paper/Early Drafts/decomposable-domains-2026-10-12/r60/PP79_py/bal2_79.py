"""bal2_79: attack on PP78's allocation B (cyclic margin rule) once a second-generation defender N
outside G is committed.

In B, a null record carried by an INTERIOR member of ray k (approached from both sides, support off
the moving level set) is accepted at k (inward approach) and at k+1 (outward approach: exact
(k+1,k+2) tie, which the cyclic rule sends to k+1).  So a null record with interior carriers on TWO
different rays k, m is accepted at all three worlds ({k,k+1} u {m,m+1} = {1,2,3} for k != m).
If a committed coherent N carries its REVERSE on a radially non-conic support, Y := N[supp -> old]
satisfies rec(Y -> N) = r, accepted at every world: N is weakly dominated by an incoherent model.

For each candidate N, each ray pair (k, m) and interior scales (a, b) from a grid, this script finds
the cells where the record can live:
  old := B_{k,a} = B_{m,b} there, also = B_{k,a-} = B_{k,a+} and = B_{m,b-} = B_{m,b+}
  (so every approximating source carries it), and N != old there;
and solves the LP "nonnegative masses on these cells, total 1, u1-vector zero".
Radial halves make the support non-conic.  Exact cells; LP in floating point (scipy highs).
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib79 import *
from mixed79 import T, B, r
from balanced79 import u1
import numpy as np
from scipy.optimize import linprog

def ray(k, s):
    m = [F(1)] * 3; m[k] = s; return post(m)

SC = {'in': (F(199, 200), F(99, 100), F(197, 200)),     # (a-, a, a+): small shift
      'mid': (F(49, 50), F(39, 40), F(97, 100)),
      'nearB': (F(24, 25), F(21, 22), F(19, 20))}       # brackets B's index 20/21 from both sides

def attack(N, label, verbose=False):
    hits = []
    for k, m in itertools.combinations(range(3), 2):
        for sk, sm in itertools.product(SC, SC):
            mods = {'T': T, 'N': N}
            for j, s in enumerate(SC[sk]): mods['k%d' % j] = ray(k, s)
            for j, s in enumerate(SC[sm]): mods['m%d' % j] = ray(m, s)
            At = atoms(mods)
            vecs = []
            for a in At:
                if a['half'] == 1: continue
                v = a['vals']
                old = v['k1']
                if not (v['k0'] == v['k1'] == v['k2'] == v['m0'] == v['m1'] == v['m2'] == old): continue
                if v['N'] == old: continue
                vecs.append(u1(v['N'], a['h']) - u1(old, a['h']))
            if not vecs: continue
            A = np.array(vecs).T; n = A.shape[1]
            res = linprog(np.zeros(n), A_eq=np.vstack([A, np.ones((1, n))]), b_eq=[0, 0, 0, 1.0],
                          bounds=[(0, None)] * n, method='highs')
            if res.status == 0:
                hits.append((k + 1, m + 1, sk, sm))
    return hits

if __name__ == '__main__':
    cands = {
        'B (first defender, member)': B,
        'same-ray B_{3,t\'} (1,1,41/42)': post((1, 1, F(41, 42))),
        'band corner cut K_B + {v1+v3}': list(B) + [tuple(F(V[0][i] + V[2][i]) for i in range(3))],
        'band corner cut K_B + {v1+2v3}': list(B) + [tuple(F(V[0][i] + 2 * V[2][i]) for i in range(3))],
        'generic posterior (21/20,441/400,1)': post((F(21, 20), F(441, 400), 1)),
        'vertex-wise: vertex 3 of B, others T': [V[0], V[1], tuple(F(V[2][i]) * (r if i == 2 else 1) for i in range(3))],
    }
    out = {}
    for lab, K in cands.items():
        h = attack(K, lab)
        out[lab] = h
        print('%-40s fatal two-ray configurations: %d  %s' % (lab, len(h), h[:4]))
    assert out['B (first defender, member)'] == [] and out["same-ray B_{3,t'} (1,1,41/42)"] == []
    print('members carry no reverse of a two-ray-carried null record (PP78 Lemma 2.2 consistent): PASS')
