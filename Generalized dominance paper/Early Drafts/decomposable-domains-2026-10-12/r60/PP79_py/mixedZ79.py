"""mixedZ79: direct check of Theorem M's sharper form: the forced rival Z3 = B[D2 -> B2] itself lies in
B's world-1 AND world-3 refusal families (Prop 1.3) and is MIXED at world 1 or 3, for every pool
candidate passing (N1) + both agreement obstructions on the S_M splice."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mixed79 import *

def in_family(At, Cn, w, Bv, X, Z):
    fam = family(At, Cn, None, None, w, Xvals=X, Bvals=Bv)
    if fam is None: return False
    strict = False
    for i, o in enumerate(fam):
        d = dict(o)
        if Z[i] not in d: return False
        strict = strict or d[Z[i]]
    return strict

P = pool()
n = ok13 = mixed = 0
for name, K in P.items():
    At = atoms({'T': T, 'B': B, 'B2': K})
    Bv = [a['vals']['B2'] for a in At]
    X = splice(At, 'M')
    if not (N1(At, Bv, X) and corr(At, 'T', Bv, X) and corr(At, 'B', Bv, X)): continue
    n += 1
    Z = [Bv[i] if Bv[i] != X[i] else a['vals']['B'] for i, a in enumerate(At)]
    f1 = in_family(At, 'B', 0, Bv, X, Z); f3 = in_family(At, 'B', 2, Bv, X, Z)
    ok13 += (f1 and f3)
    def mixed_at(w):
        better = any(lt(Z[i], a['vals']['B'], a['h'], w) for i, a in enumerate(At))
        worse = any(lt(a['vals']['B'], Z[i], a['h'], w) for i, a in enumerate(At))
        return better and worse
    mixed += (mixed_at(0) or mixed_at(2))
print('S_M passing candidates %d; Z3 refused at 1 and 3 (in both families): %d; Z3 mixed at 1 or 3: %d' % (n, ok13, mixed))
assert n == ok13 == mixed
print('Prop 1.3 + Theorem M (Z3 form): PASS')
