"""cycle68: a three-model core for the class-3 fill hierarchy (PP68 §4.2).

T = D_M;  N* = D_{conv(M u {h12})};  Y = D_{[v3, h12]} with v3 = c*1 + eps*e3 (M's e3-vertex).
Exact patterns (class, T, N*, Y) from geom68-style sampling:
  P1,P2 : class 3 (S,S,S)      t3 : class 3 (B,S,S)
  l1 : class 1 (A,S,S)   a1 : class 1 (S,S,A)   b1 : class 1 (S,S,B)   (and l2, a2, b2 in class 2)
Sub-universe: P1, P2 in {S,A}; t3 in {B,S,A}; each block R_k = (l_k, a_k, b_k) is the T-, N*- or Y-pattern.
Co-design hypotheses (all at every world):
  N* dominates every T-fill X_E = T[E -> A], E a non-empty union of P-atoms;
  Y  dominates every N*-fill Z_F = N*[F -> A], F a non-empty union of {P1,P2,t3};
  N* dominates every Y-fill  Y[F -> A] (Y = N* on class 3, so these are the same F's).
T, N*, Y selected with support {1,2,3} and registered.  Run: python3 -I -B cycle68.py
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib68 import Instance, W

cells = [('P1', 3), ('P2', 3), ('t3', 3), ('l1', 1), ('a1', 1), ('b1', 1), ('l2', 2), ('a2', 2), ('b2', 2)]
R = {'T': ('A', 'S', 'S'), 'N': ('S', 'S', 'S'), 'Y': ('S', 'A', 'B')}
mk = lambda p1, p2, t3, r1, r2: (p1, p2, t3) + R[r1] + R[r2]
models = [mk(*v) for v in itertools.product('SA', 'SA', 'BSA', 'TNY', 'TNY')]
I = Instance(cells, models=models)
T, N, Y = mk('S', 'S', 'B', 'T', 'T'), mk('S', 'S', 'S', 'N', 'N'), mk('S', 'S', 'S', 'Y', 'Y')
I.build(selected={T: W, N: W, Y: W}, registered=[T, N, Y], coherent={T, N, Y})
subsets = lambda L: [E for r in range(1, len(L) + 1) for E in itertools.combinations(L, r)]
fill = lambda base, E: tuple('A' if I.cells[n] in E else base[n] for n in range(len(base)))
H = {'N* dominates T-fills': [I.lit(N, fill(T, E), w) for E in subsets(['P1', 'P2']) for w in W],
     'Y dominates N*-fills': [I.lit(Y, fill(N, F), w) for F in subsets(['P1', 'P2', 't3']) for w in W],
     'N* dominates Y-fills': [I.lit(N, fill(Y, F), w) for F in subsets(['P1', 'P2', 't3']) for w in W]}
allh = sum(H.values(), [])
for k, h in H.items():
    print('%-24s alone: %s' % (k, 'SAT' if I.sat(h) else 'UNSAT'))
ok = I.sat(allh)
print('all three together       : %s' % ('SAT' if ok else 'UNSAT'))
if ok:
    nm = {T: 'T', N: 'N*', Y: 'Y'}
    for a in (T, N, Y):
        for b in (T, N, Y):
            if a != b:
                print('   %-3s <=_w %-3s  %s' % (nm[a], nm[b], [I.forced(a, b, w, allh) for w in W]))
print('ALL PASS' if ok else 'RESULT: UNSAT')
