"""gen2_68: second and third generation over PP67's module (PP68 §4).

Models: T, N (PP67), D* (PP67), L0 := D_{conv(v3, M0)} (PP68 Prop 4.5).  Cells (exact census, chain68/geom68):
  P1,P2 : class 3, (T,N,D*,L0) = (S,S,A,S)      RB : class 3, (B,S,A,S)
  b1 : class 1, (S,S,B,B)     l1 : class 1, (A,S,S,S)      (b2, l2 the same in class 2)
Sub-universe (108 models): P-atoms in {S,A}; RB in {B,S,A}; each block (b_k,l_k) one of the patterns
of T, N, D* (= L0's pattern on the block).  T, N, L0 selected with support {1,2,3}, D* with {1,2}.
Tests:
  G1  PP67's commitments C1-C3  +  'L0 dominates every N-fill Y_E' (E in P, all worlds): expected SAT;
  G2  third generation: each of T, N, D*, L0 dominating the L0-fill on P1P2: expected UNSAT each
      (PP68 Lemma 4.2 for T and N, Lemma E(ii) for D*, strict (G) for L0 itself).
Run: python3 -I -B gen2_68.py
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib68 import Instance, W

cells = [('P1', 3), ('P2', 3), ('RB', 3), ('b1', 1), ('l1', 1), ('b2', 2), ('l2', 2)]
R = {'T': ('S', 'A'), 'N': ('S', 'S'), 'D': ('B', 'S')}
mk = lambda p1, p2, rb, r1, r2: (p1, p2, rb) + R[r1] + R[r2]
models = [mk(*v) for v in itertools.product('SA', 'SA', 'BSA', 'TND', 'TND')]
I = Instance(cells, models=models)
T, N, D, L0 = mk('S', 'S', 'B', 'T', 'T'), mk('S', 'S', 'S', 'N', 'N'), mk('A', 'A', 'A', 'D', 'D'), mk('S', 'S', 'S', 'D', 'D')
I.build(selected={T: W, N: W, L0: W, D: (1, 2)}, registered=[T, N, D, L0], coherent={T, N, D, L0})
Es = [('P1',), ('P2',), ('P1', 'P2')]
fill = lambda base, E: tuple('A' if I.cells[n] in E else base[n] for n in range(len(base)))
C = ([I.lit(N, fill(T, E), w) for E in Es for w in W] + [I.lit(D, fill(T, E), w) for E in Es for w in (1, 2)]
     + [I.lit(a, b, w) for (a, b) in ((N, T), (D, T), (D, N)) for w in (1, 2)])
G = [I.lit(L0, fill(N, E), w) for E in Es for w in W]
g1 = I.sat(C + G)
print('G1 PP67 module + L0 dominates all N-fills:', 'SAT' if g1 else 'UNSAT')
ok = g1
Y = fill(L0, ('P1', 'P2'))
for nm, M in (('T', T), ('N', N), ('D*', D), ('L0', L0)):
    s = I.sat(C + G + [I.lit(M, Y, w) for w in W])
    print('G2 %-3s dominates the L0-fill on P1P2: %s' % (nm, 'SAT' if s else 'UNSAT'))
    ok &= not s
if g1:
    nm = {T: 'T', N: 'N', D: 'D*', L0: 'L0'}
    for a in (T, N, L0):
        for b in (T, N, D, L0):
            if a != b:
                print('   %-3s <=_w %-3s %s' % (nm[a], nm[b], [I.forced(a, b, w, C + G) for w in W]))
print('ALL PASS' if ok else 'SOME FAIL')
