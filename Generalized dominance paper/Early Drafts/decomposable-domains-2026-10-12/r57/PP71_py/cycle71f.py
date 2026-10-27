"""cycle71f: locate the joint obstruction of cycle71c K2 (splices individually dominable, jointly not).
For each consecutive pair: all its splices dominated by members, with and without the 4-cycle.
Then a greedy-minimal UNSAT set of splice-domination requirements (with the cycle).
Run: python3 -I -B cycle71f.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = [sys.argv[0], '40']
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cycle71c.py')).read()
exec(src.split("k1 = I.solve(H)")[0])
names = ['C1', 'C2', 'C3', 'C4', 'T']
sel = {}
for z in splices:
    row = [I.v(('aux', I.idx[z], k), 0) for k in range(len(reg))]
    s = I.v(('sel', I.idx[z]), 0)
    sel[z] = s
    I.solver.add_clause([-s] + row)
    for k, D_ in enumerate(reg):
        for w in W:
            I.solver.add_clause([-row[k], I.lit(D_, z, w)])
def pair_of(z):
    for i in range(n):
        a, b = Cm[i], Cm[(i + 1) % n]
        if all(z[j] in (a[j], b[j]) for j in range(nc)):
            return i
groups = {i: [z for z in splices if pair_of(z) == i] for i in range(n)}
for i in range(n):
    g = [sel[z] for z in groups[i]]
    print('pair %s/%s: all splices dominated, no cycle: %s; with cycle: %s' % (
        names[i], names[(i + 1) % n], 'SAT' if I.solve(g) else 'UNSAT', 'SAT' if I.solve(H + g) else 'UNSAT'))
allsel = [sel[z] for z in splices]
print('all pairs, no cycle:', 'SAT' if I.solve(allsel) else 'UNSAT')
core = list(splices)
if not I.solve(H + allsel):
    k = 0
    while k < len(core):
        trial = core[:k] + core[k + 1:]
        if not I.solve(H + [sel[z] for z in trial]):
            core = trial
        else:
            k += 1
    print('greedy-minimal set of splices that cannot all be dominated by members (with the cycle):')
    for z in core:
        i = pair_of(z)
        a = Cm[i]
        H_ = [cells[j][0] for j in range(nc) if z[j] != a[j]]
        print('   %s[H -> %s], H = %s' % (names[i], names[(i + 1) % n], H_))
    print('same set without the cycle:', 'SAT' if I.solve([sel[z] for z in core]) else 'UNSAT')
