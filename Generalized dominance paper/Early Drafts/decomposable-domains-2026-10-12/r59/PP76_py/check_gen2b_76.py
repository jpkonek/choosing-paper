"""PP76 check_gen2b_76 (CHECKED, exact): the forced new acceptances of check_anchor76.  For each
admissible domination d = rec(B -> X) with an affected, anchored committed C, and each refused rival W
of C with no guidance defence, C must accept W at some open world x (a generated acceptance a').
Does every choice of x leave C or B (both committed) defeated by the first-generation refusals of
d and a' together (plus strict guidance)?"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hlib76 import *
n = 4; allm = models(n)
cases = all_bad = some_bad = 0; ex = None
def fg(O, old, new, w, src):
    return {apply(src, r) for r in coupled_refusals(O, old, new, w, allm) if carries(src, r)}
for O, C in itertools.product(itertools.product(range(3), repeat=n), [(1,1,1,1),(1,1,1,0),(1,1,0,0)]):
    for B in allm:
        for X in allm:
            if B == X or any(strictly_worse(O, w, B, X) for w in range(3)): continue
            if not any(B[g] == C[g] != X[g] for g in range(n)): continue
            if not any(B[g] == B[g] != X[g] for g in range(n)): pass
            fC = {w: fg(O, B, X, w, C) for w in range(3)}
            fB = {w: fg(O, B, X, w, B) for w in range(3)}
            for w in range(3):
                if not fC[w] or not [v for v in range(3) if v != w and weakly_worse(O, v, B, C)]: continue
                for W in fC[w]:
                    refused = {x for x in range(3) if W in fC[x] or strictly_worse(O, x, C, W)}
                    if [x for x in range(3) if x not in refused and weakly_worse(O, x, W, C)]: continue
                    opts = [x for x in range(3) if x not in refused]
                    cases += 1; bad = 0
                    for x in opts:
                        gC = fg(O, C, W, x, C); gB = fg(O, C, W, x, B)
                        def defeated(S, f1, f2):
                            return any(V != S and all(strictly_worse(O, y, S, V) or V in f1[y] or (y == x and V in f2) for y in range(3)) for V in allm)
                        if defeated(C, fC, gC) or defeated(B, fB, gB): bad += 1
                    if bad == len(opts): all_bad += 1; ex = ex or (O, C, B, X, w, W, opts)
                    elif bad: some_bad += 1
print('forced generated acceptances examined:', cases, ' every choice of world defeats C or B:', all_bad, ' some choices do:', some_bad)
print('example:', ex)
