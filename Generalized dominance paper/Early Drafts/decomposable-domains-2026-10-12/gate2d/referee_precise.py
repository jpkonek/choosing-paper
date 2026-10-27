# Targeted run: cells placed inside the precise band of 'precise_band' (l = u on [0.7,0.8], t in [0.7,0.75]).
import sys; sys.path.insert(0, '.')
from fractions import Fraction as F
from referee_check import Sys, acyclic, system_checks
cases = [([F(71,100), F(73,100), F(5,10)], 1), ([F(705,1000), F(745,1000)], 2), ([F(72,100), F(3,10), F(74,100)], 2)]
for ts, U in cases:
    for seed in (1, 2):
        S = Sys(len(ts), U, seed, 'precise_band', 'note')
        S.ts = sorted(ts)
        # rebuild keys for the new ts
        S.__init__.__func__  # no-op
        N = len(ts)
        for c in range(N):
            t = S.ts[c]
            S.K[1][(c, 1)] = S.linv(t); S.K[1][(c, 2)] = S.uinv(t)
            S.K[2][(c, 1)] = 1 - S.uinv(t); S.K[2][(c, 2)] = 1 - S.linv(t)
        S.Ucache = {1: {}, 2: {}}
        print([str(t) for t in S.ts], U, seed, 'acyclic', {w: acyclic(S, w)[0] for w in (1, 2)}, system_checks(S), flush=True)
