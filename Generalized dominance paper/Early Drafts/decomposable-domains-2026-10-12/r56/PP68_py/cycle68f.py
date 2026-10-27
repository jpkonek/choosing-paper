"""cycle68f: T dominating N*-fills (PP68 Lemma 4.2(a)) on the cycle68 instance.
H1: N* dominates T-fills; H4: T dominates N*-fills (F in P); H4t: T dominates the N*-fill on t3 only.
Prediction (Lemma 4.2(a)): H4 and H4t are UNSAT even without H1, because an edge B ->_3 C forces
C <=_3 B, and N* <=_3 T is refused by strict (G) (N* is weakly 3-worse than T).
Run: python3 -I -B cycle68f.py
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cycle68c.py')).read()
exec(src.split("for name, h in")[0])
H4 = [I.lit(T, fill(N, F), w) for F in subsets(['P1', 'P2']) for w in W]
H4t = [I.lit(T, fill(N, ('t3',)), w) for w in W]
r = {'H1': I.sat(H1), 'H4': I.sat(H4), 'H4t': I.sat(H4t), 'H1+H4': I.sat(H1 + H4), 'H1+H4t': I.sat(H1 + H4t)}
for k, v in r.items():
    print('%-7s %s' % (k, 'SAT' if v else 'UNSAT'))
ok = r['H1'] and not r['H4'] and not r['H4t']
print('ALL PASS' if ok else 'SOME FAIL')
