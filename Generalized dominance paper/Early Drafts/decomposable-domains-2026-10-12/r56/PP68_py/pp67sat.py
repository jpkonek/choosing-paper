"""pp67sat: PP67's draft commitments on a block instance with PP67's own models (PP68 §5).

PP67 draft: T = D_M; D* = D_{M0} (M0 = [(16,7,0),(7,16,0)]/23) at (1/2,1/2,0), support {1,2};
N = D_{conv(M u M0)} = T ^ D* at an interior index.  Cells = PP67's type census (geom67.out):
  P1,P2 : class 3 (S,S,A) [T,N,D*]    RB : class 3 (B,S,A)
  e1 : class 1 (S,S,B)   l1a : class 1 (A,S,S)   l1b : class 1 (A,S,B)   (e2,l2a,l2b in class 2)
Sub-universe (108 models): P-atoms in {S,A}, RB in {B,S,A}, each block (e_k,l_ka,l_kb) one of the
T-, N-, D*-patterns.  T, N selected with support {1,2,3}, D* with {1,2}; all registered.
PP67 commitments (all E = non-empty unions of P-atoms):
  C1  N <=_w X_E (w=1,2,3)            C2  D* <=_1 X_E, D* <=_2 X_E
  C3  N <=_w T (w=1,2)                C4  D* <=_w T (w=1,2)
  C5  D* <=_w N (w=1,2)               C6  D* <=_w N[E->A] (w=1,2)
Run: python3 -I -B pp67sat.py
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib68 import Instance, W

cells = [('P1', 3), ('P2', 3), ('RB', 3), ('e1', 1), ('l1a', 1), ('l1b', 1), ('e2', 2), ('l2a', 2), ('l2b', 2)]
R = {'T': ('S', 'A', 'A'), 'N': ('S', 'S', 'S'), 'D': ('B', 'S', 'B')}
mk = lambda p1, p2, rb, r1, r2: (p1, p2, rb) + R[r1] + R[r2]
models = [mk(*v) for v in itertools.product('SA', 'SA', 'BSA', 'TND', 'TND')]
I = Instance(cells, models=models)
T, N, D = mk('S', 'S', 'B', 'T', 'T'), mk('S', 'S', 'S', 'N', 'N'), mk('A', 'A', 'A', 'D', 'D')
I.build(selected={T: W, N: W, D: (1, 2)}, registered=[T, N, D], coherent={T, N, D})
Es = [('P1',), ('P2',), ('P1', 'P2')]
fill = lambda base, E: tuple('A' if I.cells[n] in E else base[n] for n in range(len(base)))
C = {'C1': [I.lit(N, fill(T, E), w) for E in Es for w in W],
     'C2': [I.lit(D, fill(T, E), w) for E in Es for w in (1, 2)],
     'C3': [I.lit(N, T, w) for w in (1, 2)],
     'C4': [I.lit(D, T, w) for w in (1, 2)],
     'C5': [I.lit(D, N, w) for w in (1, 2)],
     'C6': [I.lit(D, fill(N, E), w) for E in Es for w in (1, 2)]}
allc = sum(C.values(), [])
print('each commitment group alone:', {k: ('SAT' if I.sat(v) else 'UNSAT') for k, v in C.items()})
ok = I.sat(allc)
print('all PP67 commitments together:', 'SAT' if ok else 'UNSAT')
if not ok:
    core = list(allc)
    i = 0
    while i < len(core):
        t = core[:i] + core[i + 1:]
        if not I.sat(t):
            core = t
        else:
            i += 1
    inv = {v: k for k, v in I.var.items()}
    print('minimal core:')
    for l in core:
        r, w = inv[l]
        print('   accept at w=%d: %s' % (w, ' '.join('%s:%s->%s' % x for x in r)))
else:
    nm = {T: 'T', N: 'N', D: 'D*'}
    for a in (T, N, D):
        for b in (T, N, D):
            if a != b:
                print('   %-3s <=_w %-3s %s' % (nm[a], nm[b], [I.forced(a, b, w, allc) for w in W]))
