"""PP76 check_gen2_76 (CHECKED, exact): Section 1.6.  Source B, accepted record rec(T -> B) at world o
(the forced defence), and B's (o,1)-fill X' = B + E' dominated by B'.  Brute-force: is B left without
a defence?  Compare with the sufficient condition of Section 1.6 (L' contains P, and L' minus {T != B}
avoids types (i,0), (j,0), (o,1) relative to B)."""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hlib76 import *
random.seed(762)
def upB(O, B, g, i): return better(O[g], i, 1 - B[g], B[g])
n = 4; allm = models(n); B = (1, 0, 1, 0)
tested = cond_true = cond_true_exh = exh_any = 0
for O in itertools.product(range(3), repeat=n):
    for o in range(3):
        i, j = [w for w in range(3) if w != o]
        typ = [g for g in range(n) if O[g] == o and set(w for w in range(3) if upB(O, B, g, w)) == {i, j}]
        if not typ: continue
        for T in allm:
            if T == B or any(strictly_worse(O, w, T, B) for w in range(3)): continue
            if not weakly_worse(O, o, B, T) and False: pass
            r1 = {apply(B, r) for r in coupled_refusals(O, T, B, o, allm) if carries(B, r)}
            for mask in range(1, 2 ** len(typ)):
                E = [typ[q] for q in range(len(typ)) if mask >> q & 1]
                Xp = tuple(1 - B[g] if g in E else B[g] for g in range(n))
                for Bp in allm:
                    if Bp in (Xp,) or any(strictly_worse(O, w, Bp, Xp) for w in range(3)): continue
                    if not any(Bp[g] == B[g] for g in E): continue      # Lemma 1.3 at the protected B
                    ri = {apply(B, r) for r in coupled_refusals(O, Bp, Xp, i, allm) if carries(B, r)}
                    rj = {apply(B, r) for r in coupled_refusals(O, Bp, Xp, j, allm) if carries(B, r)}
                    exh = bool(r1 & ri & rj); tested += 1; exh_any += exh
                    DTB = {g for g in range(n) if T[g] != B[g]}
                    P = {g for g in DTB if better(O[g], o, T[g], B[g])}
                    Lp = {g for g in range(n) if Bp[g] != B[g] == Xp[g]}
                    bad = {g for g in Lp - DTB if (O[g] in (i, j) and set(w for w in range(3) if upB(O, B, g, w)) == {O[g]})
                           or (O[g] == o and set(w for w in range(3) if upB(O, B, g, w)) == {i, j})}
                    cond = P <= Lp and not bad
                    cond_true += cond; cond_true_exh += (cond and exh)
print('configurations:', tested, ' B exhausted:', exh_any, ' condition holds:', cond_true, ' condition holds and exhausted:', cond_true_exh)
