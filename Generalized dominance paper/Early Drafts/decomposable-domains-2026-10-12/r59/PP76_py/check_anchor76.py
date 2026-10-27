"""PP76 check_anchor76 (CHECKED, exact): PP74 item 4 / (U2).  For an admissible domination B <= X and an
affected committed C with an anchor world v (B pointwise weakly v-worse than C), are all rivals that C
must refuse (all copies, Theorem 1.1) defended by weak guidance at some world?  Count rivals with
no guidance defence at any non-refused world: these need a NEW, non-guidance acceptance."""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hlib76 import *
n = 4; allm = models(n)
aff = need = need_restr = 0; ex = None
for O, C in itertools.product(itertools.product(range(3), repeat=n), [(1,1,1,1),(1,1,1,0),(1,1,0,0)]):
    for B in allm:
        for X in allm:
            if B == X or any(strictly_worse(O, w, B, X) for w in range(3)): continue
            if not any(B[g] == C[g] != X[g] for g in range(n)): continue
            forced = {w: {apply(C, r) for r in coupled_refusals(O, B, X, w, allm) if carries(C, r)} for w in range(3)}
            for w in range(3):
                if not forced[w]: continue
                anchors = [v for v in range(3) if v != w and weakly_worse(O, v, B, C)]
                if not anchors: continue                     # (U2) fails: PP74 would not install B
                aff += 1
                for W in forced[w]:
                    refused = {x for x in range(3) if W in forced[x] or strictly_worse(O, x, C, W)}
                    guided = [x for x in range(3) if x not in refused and weakly_worse(O, x, W, C)]
                    if not guided:
                        need += 1
                        restr = all(C[g] == W[g] or B[g] == W[g] for g in range(n))
                        need_restr += restr
                        if ex is None: ex = (O, C, B, X, w, anchors, W)
print('affected (C, w) with an anchor:', aff)
print('refused rivals with no guidance defence at any open world:', need, ' of which of the form C[S -> B]:', need_restr)
print('example (O, C, B, X, w, anchors, rival):', ex)
