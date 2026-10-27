"""sat72a: one loop at scale b.  Tests:
 L : loop edges only (C1 dominates every class-3 fill of T, C2 every class-1 fill of C1, T every class-2 fill of C2);
 L+forced verdicts among T, C1, C2;
 ALL3: every fill of every class of every member dominated by SOME installed model;
 with the six one-move defenders added (T: classes 1,2; C1: classes 2,3; C2: classes 1,3)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inst72 import *
b = F(sys.argv[1]) if len(sys.argv) > 1 else F(5, 4)
c = F(sys.argv[2]) if len(sys.argv) > 2 else b
L = loop(b)
print('b =', b, 'defender move c =', c)
def run(idx, tests, registered=None, maxr=2):
    B = Build(idx, maxr=maxr)
    reg = registered or list(idx)
    B.build(selected=list(idx), registered=reg)
    print(' installed:', list(idx), ' cells:', len(B.cells), ' models:', len(B.I.models))
    for name, mk in tests:
        cl = mk(B)
        for x in cl: B.I.solver.add_clause(x)
        # each test is cumulative only within its own build: rebuild per test
    return B
def edges(B):
    cl = []
    for (src, k, dst) in [('T', 3, 'C1'), ('C1', 1, 'C2'), ('C2', 2, 'T')]:
        for f in B.F[(src, k)]:
            for w in W: cl.append([B.I.lit(B.M[dst], f, w)])
    return cl
def allfills(B, inst):
    cl = []
    for n in ['T', 'C1', 'C2']:
        for k in (1, 2, 3):
            for f in B.F[(n, k)]:
                cl += B.dominated_by_some(f, [B.M[x] for x in inst if B.M[x] != f])
    return cl
def test(idx, name, mk):
    B = Build(idx)
    B.build(selected=list(idx), registered=list(idx), extra_clauses=[])
    cl = mk(B)
    for x in cl: B.I.solver.add_clause(x)
    r = B.I.solve()
    print('  %-48s %s   (cells %d, models %d, TC clauses %d)' % (name, 'SAT' if r else 'UNSAT', len(B.cells), len(B.I.models), B.I.ntc))
    return B, r
B, r = test(L, 'loop edges only (L)', edges)
if r:
    print('  forced verdicts among T, C1, C2 under L:')
    nm = ['T', 'C1', 'C2']
    for x in nm:
        for y in nm:
            if x != y:
                print('    %s <=_w %s : %s' % (x, y, [B.I.forced(B.M[x], B.M[y], w) for w in W]))
test(L, 'every fill, dominator among {T,C1,C2}', lambda B: allfills(B, ['T', 'C1', 'C2']))
D = dict(L)
D['T1'] = shift(L['T'], 1, c); D['T2'] = shift(L['T'], 2, c)
D['C1_2'] = shift(L['C1'], 2, c); D['C1_3'] = shift(L['C1'], 3, c)
D['C2_1'] = shift(L['C2'], 1, c); D['C2_3'] = shift(L['C2'], 3, c)
print(' defenders (2V):', {n: in2V(m) for n, m in D.items()})
#test(D, 'L only, with defenders installed', edges)
#test(D, 'every fill dominated by some installed model', lambda B: allfills(B, list(D)))
#test(D, 'L + every fill dominated', lambda B: edges(B) + allfills(B, list(D)))
