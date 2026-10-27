"""cycle68c: 3-cycles of fill domination on the cycle68 instance (PP68 §4.3).
H1: N* dominates T-fills (E in P); H2: Y dominates N*-fills (F in P u t3);
H3: T dominates Y-fills (F in P u t3);  H3p: T dominates Y-fills on P only.
Run: python3 -I -B cycle68c.py
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cycle68.py')).read()
exec(src.split("H = {")[0])
subsets = lambda L: [E for r in range(1, len(L) + 1) for E in itertools.combinations(L, r)]
fill = lambda base, E: tuple('A' if I.cells[n] in E else base[n] for n in range(len(base)))
H1 = [I.lit(N, fill(T, E), w) for E in subsets(['P1', 'P2']) for w in W]
H2 = [I.lit(Y, fill(N, F), w) for F in subsets(['P1', 'P2', 't3']) for w in W]
H3 = [I.lit(T, fill(Y, F), w) for F in subsets(['P1', 'P2', 't3']) for w in W]
H3p = [I.lit(T, fill(Y, F), w) for F in subsets(['P1', 'P2']) for w in W]
for name, h in [('H1+H2', H1 + H2), ('H1+H2+H3', H1 + H2 + H3), ('H1+H2+H3p', H1 + H2 + H3p),
                ('H2+H3', H2 + H3), ('H1+H3', H1 + H3), ('H3 alone', H3)]:
    print('%-10s %s' % (name, 'SAT' if I.sat(h) else 'UNSAT'))
h = H1 + H2 + H3
if I.sat(h):
    nm = {T: 'T', N: 'N*', Y: 'Y'}
    for a in (T, N, Y):
        for b in (T, N, Y):
            if a != b:
                print('   %-3s <=_w %-3s  %s' % (nm[a], nm[b], [I.forced(a, b, w, h) for w in W]))
