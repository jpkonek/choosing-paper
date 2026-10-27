"""cycle71e: diagnose cycle71c K2 -- which consecutive splices can be dominated by a member, with and
without the 4-cycle hypotheses, splice by splice (same sub-universe as cycle71c).
Run: python3 -I -B cycle71e.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = [sys.argv[0], '40']
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cycle71c.py')).read()
exec(src.split("k1 = I.solve(H)")[0])
names = ['C1', 'C2', 'C3', 'C4', 'T']
from collections import defaultdict
tab = defaultdict(lambda: [0, 0, 0])
for z in splices:
    pair = None
    for i in range(n):
        a, b = Cm[i], Cm[(i + 1) % n]
        if all(z[j] in (a[j], b[j]) for j in range(nc)):
            pair = '%s/%s' % (names[i], names[(i + 1) % n]); break
    ok_free = [k for k, D_ in enumerate(reg) if I.solve([I.lit(D_, z, w) for w in W])]
    ok_cyc = [k for k in ok_free if I.solve(H + [I.lit(reg[k], z, w) for w in W])]
    t = tab[pair]
    t[0] += 1; t[1] += bool(ok_free); t[2] += bool(ok_cyc)
    if not ok_cyc:
        print('  %s splice %s: dominable without cycle by %s; with cycle by %s' %
              (pair, ''.join(z), [names[k] for k in ok_free], [names[k] for k in ok_cyc]))
for p, t in tab.items():
    print('%s: %d splices; dominable by a member without the cycle: %d; with the cycle: %d' % (p, *t))
