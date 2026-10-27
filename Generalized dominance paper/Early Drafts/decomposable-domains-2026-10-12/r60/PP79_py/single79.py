"""single79: REFEREE59 relay (1) applied to the SECOND repair: can ONE splice domination leave T or B
without a defence once strict-guidance refusals are counted?  Exact cells, pool of mixed79,
families M, a, gen; defeat search of defeat79 (sources per world: guidance or the one record)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mixed79 import *
from defeat79 import defeated
P = pool()
for fam in ('M', 'a', 'gen'):
    n = dT = dB = 0; ex = []
    for name, K in P.items():
        At = atoms({'T': T, 'B': B, 'B2': K})
        Bv = [a['vals']['B2'] for a in At]
        X = splice(At, fam)
        if not (N1(At, Bv, X) and corr(At, 'T', Bv, X) and corr(At, 'B', Bv, X)): continue
        n += 1
        a1 = defeated(At, 'T', [(Bv, X)]) is not None
        a2 = defeated(At, 'B', [(Bv, X)]) is not None
        dT += a1; dB += a2
        if (a1 or a2) and len(ex) < 5: ex.append((name, 'T' if a1 else '', 'B' if a2 else ''))
    print('family %-3s passing %d: single-domination defeats of T %d, of B %d; examples %s' % (fam, n, dT, dB, ex))
print('done')
