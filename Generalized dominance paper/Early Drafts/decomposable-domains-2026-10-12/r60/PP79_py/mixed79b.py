"""mixed79b: which candidates escape a mixed refusal at B for the S_a family, and where their
mixed refusal sits instead (companion to mixed79)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mixed79 import *
P = pool()
for name, K in P.items():
    At = atoms({'T': T, 'B': B, 'B2': K})
    Bv = [a['vals']['B2'] for a in At]
    X = splice(At, 'a')
    if not (N1(At, Bv, X) and corr(At, 'T', Bv, X) and corr(At, 'B', Bv, X)): continue
    res = {(Cn, w): mixed_available(At, Cn, w, Bv, X) for Cn in ('T', 'B') for w in range(3)}
    if not (res[('B', 0)] or res[('B', 2)]):
        diffB = sorted(set((a['type'], a['vals']['B'], a['vals']['B2']) for a in At if a['vals']['B2'] != a['vals']['B']))
        print(name, 'res', {k: v for k, v in res.items() if v is not None}, 'B->B2 moves', diffB)
