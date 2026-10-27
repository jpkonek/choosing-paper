"""defeat79: joint defeat (PP76 Prop 1.6 / PP75 Thm 4.3, here for arbitrary values) of the committed
T and B by two second-generation dominations, one of an S_a splice and one of an S_b splice.

C is DEFEATED iff some rival Z is refused at all three worlds, each refusal coming from the coupled
rule of one of the installed dominations (PP76 Thm 1.1, all copies) or from strict guidance.
Exact on cells with radial halves.

(D1) same-ray dominators B_{3,t'} (index (1,1,s)) for S_a and S_b at scales s_a, s_b.
(D2) all pairs of pool candidates passing (N1) and the agreement obstruction.
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib79 import *
from mixed79 import pool, r, T, B

def splice_S(At, fam):
    X = []
    for a in At:
        t, b = a['vals']['T'], a['vals']['B']
        if t == b: X.append(t); continue
        o = a['o']
        if fam == 'a':   inS = (o in (0, 2)) or (o == 1 and a['half'] == 0)
        elif fam == 'b': inS = (o in (1, 2)) or (o == 0 and a['half'] == 0)
        X.append(b if inS else t)
    return X

def guid_opts(C, h, w):
    o = [(C, False)]
    for n in VALS:
        if lt(n, C, h, w): o.append((n, True))
    return o

def defeated(At, Cn, recs):
    """recs: list of (Bvals, Xvals).  Returns a witness description or None."""
    srcs = ['G'] + list(range(len(recs)))
    for choice in itertools.product(srcs, repeat=3):
        per = []
        ok = True
        for i, a in enumerate(At):
            C = a['vals'][Cn]; h = a['h']
            sets = []
            for w in range(3):
                c = choice[w]
                if c == 'G': o = guid_opts(C, h, w)
                else:
                    Bv, Xv = recs[c]
                    o = options(C, Bv[i], Xv[i], h, w)
                sets.append({v: s for v, s in o})
            common = set(sets[0]) & set(sets[1]) & set(sets[2])
            if not common: ok = False; break
            per.append({v: tuple(sets[w][v] for w in range(3)) for v in common})
        if not ok: continue
        # need, for each world, some atom whose chosen value carries the strict flag at that world
        prov = {w: [(i, v) for i, d in enumerate(per) for v, f in d.items() if f[w]] for w in range(3)}
        if any(not prov[w] for w in range(3)): continue
        found = False
        for p0 in prov[0][:40]:
            for p1 in prov[1][:40]:
                for p2 in prov[2][:40]:
                    pts = [p0, p1, p2]
                    if all(not (pts[x][0] == pts[y][0] and pts[x][1] != pts[y][1]) for x in range(3) for y in range(3)):
                        found = True; break
                if found: break
            if found: break
        if found: return choice
    return None

def admissible(At, Bv, X):
    return N1(At, Bv, X) and corr(At, 'T', Bv, X) and corr(At, 'B', Bv, X)

def D1():
    print('(D1) same-ray dominators: index (1,1,s), B = (1,1,%s)' % r)
    scales = [F(83, 84), F(41, 42), F(27, 28), F(81, 84)]
    for sa in scales:
        for sb in scales:
            Ka, Kb = post((1, 1, sa)), post((1, 1, sb))
            At = atoms({'T': T, 'B': B, 'Ba': Ka, 'Bb': Kb})
            Xa, Xb = splice_S(At, 'a'), splice_S(At, 'b')
            Ba = [a['vals']['Ba'] for a in At]; Bb = [a['vals']['Bb'] for a in At]
            adm = (admissible(At, Ba, Xa), admissible(At, Bb, Xb))
            dB = defeated(At, 'B', [(Ba, Xa), (Bb, Xb)])
            dT = defeated(At, 'T', [(Ba, Xa), (Bb, Xb)])
            print('  s_a=%s s_b=%s admissible=%s  B defeated: %s  T defeated: %s' % (sa, sb, adm, dB, dT))
            if adm == (True, True):
                assert (dB is not None) == (sa == sb), 'D1 prediction fails'
    print('(D1) B is defeated iff s_a = s_b: PASS')

def D2(limit=60):
    P = pool()
    names = list(P)
    good = {'a': [], 'b': []}
    # pre-screen individually (on the T,B,cand arrangement)
    for n in names:
        At = atoms({'T': T, 'B': B, 'B2': P[n]})
        Bv = [a['vals']['B2'] for a in At]
        for fam in ('a', 'b'):
            if admissible(At, Bv, splice_S(At, fam)):
                good[fam].append(n)
    import random
    rnd = random.Random(7)
    A = rnd.sample(good['a'], min(limit, len(good['a'])))
    Bl = rnd.sample(good['b'], min(limit, len(good['b'])))
    nB = nT = tot = 0
    partner = {x: False for x in A}
    for x in A:
        for y in Bl:
            At = atoms({'T': T, 'B': B, 'Ba': P[x], 'Bb': P[y]})
            Xa, Xb = splice_S(At, 'a'), splice_S(At, 'b')
            Ba = [a['vals']['Ba'] for a in At]; Bb = [a['vals']['Bb'] for a in At]
            tot += 1
            dB = defeated(At, 'B', [(Ba, Xa), (Bb, Xb)]) is not None
            dT = defeated(At, 'T', [(Ba, Xa), (Bb, Xb)]) is not None
            nB += dB; nT += dT
            if not (dB or dT): partner[x] = True
    print('(D2) pairs %d: B jointly defeated %d, T jointly defeated %d; every S_a-dominator keeps a partner: %s'
          % (tot, nB, nT, all(partner.values())))

if __name__ == '__main__':
    D1()
    D2(int(sys.argv[1]) if len(sys.argv) > 1 else 40)
