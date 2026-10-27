"""single68: one coherent model N* serving every fill X_E (E a non-empty union of atoms P1,P2,P3).

N* = D_{K*}, K* = conv(M u {(1/2,1/2,0)}): T with its answers silenced exactly where they disagree
with sign(g1+g2) (PP68 Lemma 2.1).  Cells:
  P1,P2,P3 : class 3, T = N* = S   (the fill atoms; X_E puts A there)
  t3       : class 3, T = B, N* = S
  l1       : class 1, T = A, N* = S
  l2       : class 2, T = A, N* = S
Run: python3 -I -B single68.py
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib68 import Instance, W

cells = [('P1', 3), ('P2', 3), ('P3', 3), ('t3', 3), ('l1', 1), ('l2', 2)]
allowed = {'P1': 'SA', 'P2': 'SA', 'P3': 'SA', 't3': 'BS', 'l1': 'AS', 'l2': 'AS'}
I = Instance(cells, allowed)
T = I.M(P1='S', P2='S', P3='S', t3='B', l1='A', l2='A')
N = I.M(P1='S', P2='S', P3='S', t3='S', l1='S', l2='S')
P = ['P1', 'P2', 'P3']


def X(E, base=T):
    return I.splice(base, **{c: 'A' for c in E})


Es = [E for r in (1, 2, 3) for E in itertools.combinations(P, r)]
I.build(selected={T: W, N: W}, registered=[T, N], coherent={T, N})
hyp = [I.lit(N, X(E), w) for E in Es for w in W]
ok = I.sat(hyp)
print('N* accepts every X_E at every world, with all axioms:', 'SAT' if ok else 'UNSAT')
res = {}
for E in Es:
    res[E] = [I.forced(X(E), N, w, hyp) for w in W]
print('verdict of X_E <=_w N* (w=1,2,3) under the hypothesis (A forced / R forced / ? free):')
for E in Es:
    print('   E=%-10s %s' % (''.join(E), res[E]))
print('T vs N*:', [I.forced(T, N, w, hyp) for w in W], ' N* vs T:', [I.forced(N, T, w, hyp) for w in W])
# expected (PP68 Prop 1.1): X_E refused at 1,2 when E is a proper subset; refused at 3 when E has a proper
# non-empty subset (and X_{E} for |E|=1 at 3 is free on atoms: no smaller non-null set in the cell model).
chk = all(res[E][0] == 'R' and res[E][1] == 'R' for E in Es if len(E) < 3) and \
      all(res[E][2] == 'R' for E in Es if len(E) >= 2)
print('Prop 1.1 pattern:', 'PASS' if chk else 'FAIL')
print('ALL PASS' if ok and chk else 'SOME FAIL')
