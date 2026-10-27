"""endpoint74: the splice-endpoint clause (PP74 Thm 5.1) for the SECOND application, at cell level (NUMERICS:
exact cells, float solid-angle masses, level 0 of u1 only).
Committed T and B = C_{u o (3 -> 20/21)}; rivals X = T[S -> B], S a non-empty proper union of coarse layer cells.
Candidate dominators B'': posterior grid inside (2V) (H-models).  Necessary conditions: N1, (U1) at T and B.
For each world w with V_w(d'') < 0 (d'' = rec(B'' -> X)), the two-carrier covers (C1, C2) = (B, T) and (T, B) give
accepted triangles in any base that accepts every committed-carried u1-favourable record, unless the cover is
blocked for every D'' subset of {T != B} minus supp d''.  B'' is *endpoint-safe* if every cover is blocked."""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'PP75_py'))
from asr74 import post, lines, ans
from geo75 import cells as _cells, htype
from layer74 import solid
from fractions import Fraction as F

def in2V(m, eta=F(1, 100)):
    c = F(7, 30); rr = [1 / F(x) for x in m]; s = sum(rr)
    return all(x / s >= c + eta for x in rr)

def vec(t, mass, sign):
    """u1 change for S -> h at an atom of type t (sign +1), or h -> S (sign -1)"""
    o = t[1]
    v = [-1.0, -1.0, -1.0]; v[o] = 2.0
    if t[0] == 'B':
        v = [-x for x in v]
    return [sign * mass * x for x in v]

def change(a, b, t, m):
    if a == b: return [0.0, 0.0, 0.0]
    if a == 'S' and b == 'h': return vec(t, m, +1)
    if a == 'h' and b == 'S': return vec(t, m, -1)
    raise ValueError((a, b))

T = post((1, 1, 1)); Bm = post((1, 1, F(20, 21)))
g = [F(21, 20) ** e for e in range(-3, 4)]
cands = [(a, b, F(1)) for a in g for b in g if in2V((a, b, F(1))) and (a, b) != (1, 1) and (a, b, 1) != (1, 1, F(20, 21))]
base = {'T': T, 'B': Bm}
coarse = sorted(set(tuple(tuple(sum(k[i] * c['pt'][i] for i in range(3)) > 0 for k in K) for K in (T, Bm))
                    for c in _cells([], extra_lines=lines(T) + lines(Bm))
                    if all(x != 0 for x in c['pt']) and htype(c['pt'])[0] != 'U' and ans(T, c['pt']) != ans(Bm, c['pt'])))
n = len(coarse)
Ss = [frozenset(c) for k in range(1, n) for c in itertools.combinations(range(n), k)]
safe = {S: [] for S in Ss}; adm = {S: 0 for S in Ss}
for m in cands:
    K = post(m)
    At = []
    for c in _cells([], extra_lines=lines(T) + lines(Bm) + lines(K)):
        h = c['pt']
        if any(x == 0 for x in h): continue
        t = htype(h)
        if t[0] == 'U': continue
        vT, vB, vK = ans(T, h), ans(Bm, h), ans(K, h)
        if '-h' in (vT, vB, vK): break
        key = tuple(tuple(sum(k[i] * h[i] for i in range(3)) > 0 for k in KK) for KK in (T, Bm))
        At.append((t, solid(c['poly']), vT, vB, vK, coarse.index(key) if vT != vB else None))
    else:
        for S in Ss:
            X = [(a[3] if (a[5] is not None and a[5] in S) else a[2]) for a in At]
            supp = [i for i, a in enumerate(At) if a[4] != X[i]]
            # N1: B'' strictly better than X somewhere at every world (two-valued: pattern of X -> B'')
            def better(i, w):
                v = change(X[i], At[i][4], At[i][0], 1.0); return v[w] < 0
            if not all(any(better(i, w) for i in supp) for w in range(3)): continue
            # U1 at T: T = X on supp?  at B: B = X on supp?
            if all(At[i][2] == X[i] for i in supp) or all(At[i][3] == X[i] for i in supp): continue
            adm[S] += 1
            Vd = [sum(change(At[i][4], X[i], At[i][0], At[i][1])[w] for i in supp) for w in range(3)]
            P = [i for i in supp if At[i][5] is not None and At[i][5] in S]
            Q = [i for i in supp if i not in P]
            off = [i for i, a in enumerate(At) if a[2] != a[3] and i not in supp]
            ok = True
            for w in range(3):
                if Vd[w] >= 0: continue
                for (C1, P1, C2, Q2) in (('B', P, 'T', Q), ('T', P, 'B', Q)):
                    # cover requires C1 = X on P1 and C2 = X on Q2
                    col = {'T': 2, 'B': 3}
                    if not all(At[i][col[C1]] == X[i] for i in P1): continue
                    if not all(At[i][col[C2]] == X[i] for i in Q2): continue
                    vs = sum(change(X[i], At[i][4], At[i][0], At[i][1])[w] for i in P1)
                    vt = sum(change(X[i], At[i][4], At[i][0], At[i][1])[w] for i in Q2)
                    xs = [change(At[i][col[C1]], At[i][col[C2]], At[i][0], At[i][1])[w] for i in off]
                    lo = sum(x for x in xs if x < 0); hi = sum(x for x in xs if x > 0)
                    if not (vt <= lo or -vs >= hi):
                        ok = False
            if ok:
                safe[S].append(m)
nadm = sum(1 for S in Ss if adm[S]); nsafe = sum(1 for S in Ss if safe[S])
print('coarse layer cells %d, splices %d, candidates %d' % (n, len(Ss), len(cands)))
print('splices with an N1+U1 posterior candidate: %d; with an endpoint-safe one: %d' % (nadm, nsafe))
print('examples of endpoint-safe (S, candidate):', [(sorted(S), [str(x) for x in safe[S][0]]) for S in Ss if safe[S]][:5])
print('examples of splices with N1+U1 candidates but none endpoint-safe:', [sorted(S) for S in Ss if adm[S] and not safe[S]][:8])
