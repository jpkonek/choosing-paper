"""mixed79: Theorem M (forced mixed refusal at the first defender) and its sharpness, exact cells.

Committed: T = C_u, B = C_(1,1,r) (pure world-3 down-shift, the first defender).
Splice families X2 = T[S -> B], S given by coarse layer pieces and radial halves:
  M  : S = L1 u L3 u (half 0 of the lose-A2 part of L2)          [Theorem M family]
  a  : S = L1 u L3 u (half 0 of all of L2)                          [S_a family]
  gen: S = half 0 of every cell of L                                 [generic]
Candidates: posteriors (fine grid, same-ray points), vertex-wise rescalings, B or T plus one
extra vertex (corner cuts), random 3- and 4-vertex credal sets.  For each candidate that passes
the necessary conditions (N1) and the agreement obstruction at T and at B, record:
  affected worlds of T and of B (coupled refusal rule over all copies, PP76 Thm 1.1),
  whether some refused rival is MIXED at that world.
Theorem M predicts: family M -> every passing candidate forces a mixed refusal at B at world 1 or 3.
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib79 import *

r = F(20, 21)
T = post((1, 1, 1)); B = post((1, 1, r))

def pool(seed=79):
    rnd = random.Random(seed)
    out = {}
    g = [F(41, 40) ** e for e in range(-3, 4)]
    for a in g:
        for b in g:
            out['P(%s,%s)' % (a, b)] = post((a, b, F(1)))
    for s in [F(n, 84) for n in range(81, 84)] + [F(161, 168), F(167, 168)]:
        out['ray(%s)' % s] = post((1, 1, s))
    sh = [F(1), F(41, 40), F(40, 41), r]
    for ms in itertools.product(itertools.product(sh, repeat=2), repeat=3):
        mm = [(p[0], p[1], F(1)) for p in ms]
        if len(set(mm)) == 1: continue
        if rnd.random() < 0.06:
            out['VW' + str(len(out))] = vwise(mm)
    # corner cuts: B (or T) plus one extra positive vertex
    for base, nm in ((B, 'B+'), (T, 'T+')):
        for _ in range(150):
            k = tuple(F(rnd.randint(1, 40), 1) for _ in range(3))
            out[nm + str(len(out))] = list(base) + [k]
    for _ in range(150):
        K = []
        for a in range(3):
            K.append(tuple(F(V[a][i]) * F(rnd.randint(90, 110), 100) for i in range(3)))
        if rnd.random() < 0.5:
            K.append(tuple(F(rnd.randint(5, 20)) for _ in range(3)))
        out['R' + str(len(out))] = K
    return out

def splice(At, fam):
    X = []
    for a in At:
        t, b = a['vals']['T'], a['vals']['B']
        if t == b: X.append(t); continue
        o = a['o']
        if fam == 'M':
            loseA2 = (a['type'] == ('A', 1) and t == 'h' and b == 'S')
            inS = (o in (0, 2)) or (o == 1 and loseA2 and a['half'] == 0)
        elif fam == 'a':
            inS = (o in (0, 2)) or (o == 1 and a['half'] == 0)
        elif fam == 'gen':
            inS = (a['half'] == 0)
        X.append(b if inS else t)
    return X

def run():
    P = pool()
    stats = {}
    examples = {}
    for fam in ('M', 'a', 'gen'):
        stats[fam] = {'pass': 0, 'mixedB13': 0, 'nomixed_any': 0, 'Baff3': 0, 'anti': 0}
        examples[fam] = []
    for name, K in P.items():
        At = atoms({'T': T, 'B': B, 'B2': K})
        Bv = [a['vals']['B2'] for a in At]
        for fam in ('M', 'a', 'gen'):
            X = splice(At, fam)
            if not (N1(At, Bv, X) and corr(At, 'T', Bv, X) and corr(At, 'B', Bv, X)):
                continue
            st = stats[fam]; st['pass'] += 1
            res = {}
            for Cn in ('T', 'B'):
                for w in range(3):
                    res[(Cn, w)] = mixed_available(At, Cn, w, Bv, X)
            if res[('B', 2)] is not None: st['Baff3'] += 1
            if res[('B', 0)] or res[('B', 2)]: st['mixedB13'] += 1
            if not any(v for v in res.values()):
                st['nomixed_any'] += 1
                if len(examples[fam]) < 4: examples[fam].append(name)
    for fam in ('M', 'a', 'gen'):
        print(fam, stats[fam], 'mixed-free examples:', examples[fam])
    s = stats['M']
    assert s['pass'] > 0 and s['mixedB13'] == s['pass'], 'Theorem M violated'
    assert stats['M']['Baff3'] == stats['M']['pass'] == stats['M']['pass']
    print('Theorem M: every passing candidate forces a mixed refusal at B at world 1 or 3: PASS')

if __name__ == '__main__':
    run()
