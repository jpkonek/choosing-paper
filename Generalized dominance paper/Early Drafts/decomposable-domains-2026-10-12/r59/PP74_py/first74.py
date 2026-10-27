"""first74: ASR's FIRST application, exact at cell level.
Committed: T.  Rivals: H-fills X = T[E -> h] of class k (E a non-empty union of T-silent atoms of type A_k
on which some (2V) ray model C_{u o (k -> r^j)}, j <= 3, answers h), all subsets E.
Candidates: the pure down-shift ray of world k, B_j = C_{u o (k -> r^j)}, j = 1..6 (rival-dependent scale).
Reports for every E: the admissible ray scales, the affected pairs and their anchors.
Atoms: joint arrangement of T and all ray models, so every E is a union of atoms."""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from asr74 import *

r = F(20, 21)
def down(k, s):
    m = [F(1)] * 3; m[k] = s; return tuple(m)

T = post((1, 1, 1))
for k in range(3):
    ray = {'B%d' % j: post(down(k, r ** j)) for j in range(1, 7)}
    mods = {'T': T}; mods.update(ray)
    At = atoms(mods)
    n = len(At)
    Tv = [a['vals']['T'] for a in At]
    pool = [i for i, a in enumerate(At) if Tv[i] == 'S' and a['type'] == ('A', k)
            and any(a['vals']['B%d' % j] == 'h' for j in (1, 2, 3))]
    tot = ok = 0
    aff_all = set()
    noray = []
    for q in range(1, len(pool) + 1):
        for E in itertools.combinations(pool, q):
            X = ['h' if i in E else Tv[i] for i in range(n)]
            tot += 1
            good = []
            for j in range(1, 7):
                rep = asr(At, X, [a['vals']['B%d' % j] for a in At], {'T': Tv})
                if rep['ok']:
                    good.append(j)
                    aff_all |= set((c, w + 1, tuple(v + 1 for v in rep['anchors'][(c, w)])) for (c, w) in rep['affected'])
            if good: ok += 1
            else: noray.append(E)
    print('class %d: pool atoms %d, fills %d, fills with an ASR-admissible ray scale %d' % (k + 1, len(pool), tot, ok))
    print('   affected (carrier, world, anchors) over all admissible pairs:', sorted(aff_all))
    print('   fills with no admissible ray scale:', len(noray))
