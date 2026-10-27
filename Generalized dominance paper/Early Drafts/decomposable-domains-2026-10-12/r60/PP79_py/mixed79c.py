"""mixed79c: an explicit coherent second defender that escapes every mixed coupled refusal for the
S_a family (corner cut inside the T-B band), and fails for the Theorem M family, as Theorem M says.
K = vertices of B plus k = v^1 + v^3 (a member of T's credal set), which cuts B's B_2-corner."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mixed79 import *
for lam in (F(1), F(1, 2), F(2)):
    k = tuple(F(V[0][i]) + lam * V[2][i] for i in range(3))
    K = list(B) + [k]
    At = atoms({'T': T, 'B': B, 'B2': K})
    Bv = [a['vals']['B2'] for a in At]
    moves = sorted(set((a['type'], a['vals']['T'], a['vals']['B'], a['vals']['B2']) for a in At if a['vals']['B2'] != a['vals']['B']))
    print('k = v1 + %s v3; B->B2 moves (type, T, B, B2):' % lam, moves)
    for fam in ('a', 'M', 'gen'):
        X = splice(At, fam)
        ok = N1(At, Bv, X) and corr(At, 'T', Bv, X) and corr(At, 'B', Bv, X)
        res = {(Cn, w + 1): mixed_available(At, Cn, w, Bv, X) for Cn in ('T', 'B') for w in range(3)}
        print('  family %-3s passes N1+agreement: %s; affected (carrier, world): mixed? %s'
              % (fam, ok, {k_: v for k_, v in res.items() if v is not None}))
