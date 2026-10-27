"""cycle71b: stress test of the 4-cycle on larger sub-universes (PP71 §3).
U = U0 (cycle71) + every single-cell modification of each C_i (value in {A,S,B}) + R random multi-cell
modifications (2-4 cells, values in {A,S,B}), for several seeds.  Hypotheses H1..H4 as in cycle71.
Also reports: the 3-cycle on the same U, and whether world-3 ties are forced in the 3-cycle.
Run: python3 -I -B cycle71b.py
"""
import itertools, os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cycle71 import setup
from lib71 import Inst, W

cells, Cm, fills, models0 = setup()
nc = len(cells)


def universe(R, seed):
    rnd = random.Random(seed)
    U = list(models0)
    for m in Cm:
        for j in range(nc):
            for a in 'ASB':
                if a != m[j]:
                    U.append(m[:j] + (a,) + m[j + 1:])
    while len(set(U)) < len(set(models0)) + 4 * nc * 2 + R:
        b = list(rnd.choice(Cm))
        for j in rnd.sample(range(nc), rnd.randint(2, 4)):
            b[j] = rnd.choice('ASB')
        U.append(tuple(b))
    return U


n = 4
for R, seed in [(100, 1), (200, 2)]:
    I = Inst(cells, universe(R, seed))
    I.build(selected={m: W for m in Cm}, registered=Cm, coherent=set(Cm))
    H = [I.lit(Cm[(i + 1) % n], f, w) for i in range(n) for f in fills[i] for w in W]
    s4 = I.solve(H)
    H3 = ([I.lit(Cm[1], f, w) for f in fills[0] for w in W] + [I.lit(Cm[2], f, w) for f in fills[1] for w in W]
          + [I.lit(Cm[0], f, w) for f in fills[2] for w in W])
    s3 = I.solve(H3)
    print('|U| = %d (seed %d): 4-cycle %s; 3-cycle %s' % (len(I.models), seed, 'SAT' if s4 else 'UNSAT',
                                                         'SAT' if s3 else 'UNSAT'))
    if seed == 1:
        if s4:
            print('  4-cycle forced verdicts (diagonals and reverse edges):')
            for a, b in [(0, 2), (2, 0), (1, 3), (3, 1), (1, 0), (2, 1), (3, 2), (0, 3)]:
                print('    C%d <=_w C%d %s' % (a + 1, b + 1, [I.forced(Cm[a], Cm[b], w, H) for w in W]))
            # can the diagonals be refused at world 3 in both directions simultaneously?
            d = [I.lit(Cm[0], Cm[2], 3, False), I.lit(Cm[2], Cm[0], 3, False),
                 I.lit(Cm[1], Cm[3], 3, False), I.lit(Cm[3], Cm[1], 3, False)]
            print('  4-cycle with both diagonals refused both ways at world 3 (no ties):', I.solve(H + d))
            t = [I.lit(Cm[a], Cm[b], 3) for a in range(n) for b in range(n) if a != b]
            print('  4-cycle with all world-3 ties:', I.solve(H + t))
        if s3:
            print('  3-cycle forced world-3 verdicts:')
            for a in range(3):
                for b in range(3):
                    if a != b:
                        print('    C%d <=_3 C%d %s' % (a + 1, b + 1, I.forced(Cm[a], Cm[b], 3, H3)))
