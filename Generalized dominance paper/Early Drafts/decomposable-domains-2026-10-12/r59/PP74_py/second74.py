"""second74: ASR's SECOND application, exact at cell level.
Committed: T = C_u and its class-k defender B = C_{u o (1 at k -> r)} (pure down-shift of world k, r < 1).
Rivals: every splice Y = T[S -> B], S a non-empty proper union of coarse cells of {T != B}
(coarse cells = cells of the T/B arrangement); also splices B[S -> B'] between two defenders of
different classes, with committed {T, B, B'}.
Candidates: posterior grid (inside and beyond (2V)) and vertex-wise rescalings (escape family).
For each rival: does some candidate pass N1 + (U1) for all committed + (U2) anchoring of every
affected committed pair?  Reported separately for candidates in H (h/S only) and outside H.
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from asr74 import *

r = F(20, 21)
def down(k, s):
    m = [F(1)] * 3; m[k] = s; return tuple(m)

def coarse_key(h, Ks):
    return tuple(tuple(sum(k[i] * h[i] for i in range(3)) > 0 for k in K) for K in Ks)

def candidates():
    out = {}
    g = [F(21, 20) ** e for e in range(-3, 4)]
    for a in g:
        for b in g:
            out['P(%s,%s,1)' % (a, b)] = post((a, b, F(1)))
    # vertex-wise single-world down-shifts (anchoring family) and mixed vertex rescalings
    sh = [F(1), r, r * r, r ** 3]
    for k in range(3):
        for s in itertools.product(sh, repeat=3):
            if len(set(s)) == 1: continue
            out['VW%d%s' % (k + 1, ''.join(str(sh.index(x)) for x in s))] = vwise([down(k, x) for x in s])
    mix = [F(1), F(21, 20), r]
    for ms in itertools.product(itertools.product(mix, repeat=2), repeat=3):
        mm = [(p[0], p[1], F(1)) for p in ms]
        if len(set(mm)) == 1: continue
        out['VM' + str(abs(hash(tuple(mm))) % 10**6)] = vwise(mm)
    return out

def run(committed, pair, label):
    Z1, Z2 = pair
    Ks = [committed[Z1], committed[Z2]]
    base = atoms(committed)
    Lkeys = sorted(set(coarse_key(a['h'], Ks) for a in base if a['vals'][Z1] != a['vals'][Z2]))
    n = len(Lkeys)
    Ss = [frozenset(c) for k in range(1, n) for c in itertools.combinations(range(n), k)]
    print('%s: coarse layer cells n = %d, splices = %d' % (label, n, len(Ss)))
    cand = candidates()
    good_in = {S: [] for S in Ss}; good_out = {S: [] for S in Ss}
    for cname, K in cand.items():
        mods = dict(committed); mods['Bc'] = K
        At = atoms(mods)
        isH = all(a['vals']['Bc'] in ('h', 'S') for a in At)
        keyidx = [Lkeys.index(coarse_key(a['h'], Ks)) if a['vals'][Z1] != a['vals'][Z2] else None for a in At]
        com = {c: [a['vals'][c] for a in At] for c in committed}
        Bv = [a['vals']['Bc'] for a in At]
        for S in Ss:
            Y = [com[Z2][i] if keyidx[i] is not None and keyidx[i] in S else com[Z1][i] for i in range(len(At))]
            rep = asr(At, Y, Bv, com)
            if rep['ok']:
                (good_in if isH else good_out)[S].append(cname)
    nin = sum(1 for S in Ss if good_in[S]); nout = sum(1 for S in Ss if good_out[S])
    nany = sum(1 for S in Ss if good_in[S] or good_out[S])
    print('  splices with an ASR-admissible candidate: in H %d / %d; outside H %d / %d; any %d / %d'
          % (nin, len(Ss), nout, len(Ss), nany, len(Ss)))
    bad = [S for S in Ss if not (good_in[S] or good_out[S])]
    print('  first unrepaired splice classes (coarse-cell index sets):', [sorted(S) for S in bad[:8]])
    kinds = {}
    for S in Ss:
        for c in good_in[S] + good_out[S]:
            kinds[c[:3]] = kinds.get(c[:3], 0) + 1
    print('  admissible (splice, candidate) pairs by family:', kinds)
    return good_in, good_out

if __name__ == '__main__':
    T = post((1, 1, 1))
    for k in (2, 0):
        B = post(down(k, r))
        run({'T': T, 'B': B}, ('T', 'B'), 'T--B%d splices' % (k + 1))
    B3 = post(down(2, r)); B1 = post(down(0, r))
    run({'T': T, 'B3': B3, 'B1': B1}, ('B3', 'B1'), 'B3--B1 splices (defender-defender)')
