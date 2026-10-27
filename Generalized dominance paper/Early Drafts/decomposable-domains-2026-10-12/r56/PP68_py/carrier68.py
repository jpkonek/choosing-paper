"""carrier68: carrier exclusion for a strict all-world dominator (PP68 Prop 2.3).

Same cells as single68, with P3 also allowed the minority answer B.  Dm is a precise model with
m in M: equal to T on T's answer set (t3, l1, l2), A on P1, P2 and B on P3.  It carries
rec(X_{P1P2}, N*), which is refused at every world once N* serves every fill (Prop 1.1).
Prediction: with Dm selected (support {1,2,3}) and registered, the hypothesis 'N* accepts every X_E at
every world' is UNSAT; without Dm selected it is SAT; with Dm selected but N* serving only the
maximal fill X_{P1P2P3} it is SAT (so the exclusion is caused by uniformity).
Run: python3 -I -B carrier68.py
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib68 import Instance, W

cells = [('P1', 3), ('P2', 3), ('P3', 3), ('t3', 3), ('l1', 1), ('l2', 2)]
allowed = {'P1': 'SA', 'P2': 'SA', 'P3': 'SAB', 't3': 'BS', 'l1': 'AS', 'l2': 'AS'}
P = ['P1', 'P2', 'P3']


def run(select_dm, uniform):
    I = Instance(cells, allowed)
    T = I.M(P1='S', P2='S', P3='S', t3='B', l1='A', l2='A')
    N = I.M(P1='S', P2='S', P3='S', t3='S', l1='S', l2='S')
    Dm = I.M(P1='A', P2='A', P3='B', t3='B', l1='A', l2='A')
    sel = {T: W, N: W}
    reg = [T, N]
    if select_dm:
        sel[Dm] = W
        reg.append(Dm)
    I.build(selected=sel, registered=reg, coherent={T, N, Dm})
    Es = [E for r in (1, 2, 3) for E in itertools.combinations(P, r)] if uniform else [tuple(P)]
    hyp = [I.lit(N, I.splice(T, **{c: 'A' for c in E}), w) for E in Es for w in W]
    return I.sat(hyp)


a = run(True, True)
b = run(False, True)
c = run(True, False)
print('Dm selected, N* serves every fill      :', 'SAT' if a else 'UNSAT')
print('Dm not selected, N* serves every fill  :', 'SAT' if b else 'UNSAT')
print('Dm selected, N* serves only X_{P1P2P3} :', 'SAT' if c else 'UNSAT')
ok = (not a) and b and c
print('ALL PASS' if ok else 'SOME FAIL')
