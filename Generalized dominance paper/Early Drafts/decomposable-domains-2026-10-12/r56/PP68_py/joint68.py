"""joint68: the two-model uniform co-design (N* in the interior, D on the edge {1,2}) on a block instance.

Cells are the value patterns (class, T, N*, D) found exactly by geom68 (all patterns where two of the
three models differ):
  P1,P2 : class 3, (S,S,A)   -- fill atoms (X_E puts A)
  t3    : class 3, (B,S,A)
  l1a   : class 1, (A,S,S);  d1 : class 1, (A,A,S);  e1 : class 1, (S,S,B)
  l2a,d2,e2 : the same in class 2.
Sub-universe: every model whose value on P1, P2 is S or A, on t3 is B, S or A, and on each block
R1 = (l1a,d1,e1), R2 = (l2a,d2,e2) is the T-, the N*- or the D-pattern (108 models).
Axioms on the sub-universe: lib68.  T and N* selected with support {1,2,3}; D selected with support {1,2};
all three registered; only they are coherent.
Hypotheses (the co-design): N* <=_w X_E for all E and all w; D <=_1 X_E and D <=_2 X_E for all E.
Run: python3 -I -B joint68.py
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib68 import Instance, W

cells = [('P1', 3), ('P2', 3), ('t3', 3), ('l1a', 1), ('d1', 1), ('e1', 1), ('l2a', 2), ('d2', 2), ('e2', 2)]
R = {'T': ('A', 'A', 'S'), 'N': ('S', 'A', 'S'), 'D': ('S', 'S', 'B')}
models = []
for p1, p2, t3, r1, r2 in itertools.product('SA', 'SA', 'BSA', 'TND', 'TND'):
    models.append((p1, p2, t3) + R[r1] + R[r2])
I = Instance(cells, models=models)


def mk(p1, p2, t3, r1, r2):
    return (p1, p2, t3) + R[r1] + R[r2]


T = mk('S', 'S', 'B', 'T', 'T')
N = mk('S', 'S', 'S', 'N', 'N')
D = mk('A', 'A', 'A', 'D', 'D')
X = {E: mk('A' if 'P1' in E else 'S', 'A' if 'P2' in E else 'S', 'B', 'T', 'T')
     for E in [('P1',), ('P2',), ('P1', 'P2')]}
I.build(selected={T: W, N: W, D: (1, 2)}, registered=[T, N, D], coherent={T, N, D})
hyp = [I.lit(N, x, w) for x in X.values() for w in W] + [I.lit(D, x, w) for x in X.values() for w in (1, 2)]
ok = I.sat(hyp)
print('models %d; co-design hypotheses with all axioms: %s' % (len(I.models), 'SAT' if ok else 'UNSAT'))
names = {T: 'T', N: 'N*', D: 'D'}
for E, x in X.items():
    names[x] = 'X_' + ''.join(E)
print('forced verdicts among T, N*, D, X_E under the hypotheses (A / R / ? free):')
rows = []
for a in [T, N, D]:
    for b in [T, N, D] + list(X.values()):
        if a == b:
            continue
        rows.append((names[a], names[b], [I.forced(a, b, w, hyp) for w in W]))
for b in [T, N, D]:
    for a in X.values():
        rows.append((names[a], names[b], [I.forced(a, b, w, hyp) for w in W]))
for r in rows:
    print('   %-5s <=_w %-7s  w=1,2,3: %s' % r)
# guidance-trap style pair tests: which pairs of defence choices are jointly allowed
print('joint defence options (SAT = allowed):')
tests = {
    'N*<=1 T and N*<=2 T': [I.lit(N, T, 1), I.lit(N, T, 2)],
    'D<=1 N* and D<=2 N*': [I.lit(D, N, 1), I.lit(D, N, 2)],
    'N*<=1 D and N*<=2 D': [I.lit(N, D, 1), I.lit(N, D, 2)],
    'D<=1 T and D<=2 T': [I.lit(D, T, 1), I.lit(D, T, 2)],
}
for k, a in tests.items():
    print('   %-22s %s' % (k, 'SAT' if I.sat(hyp + a) else 'UNSAT'))
print('ALL PASS' if ok else 'SOME FAIL')
