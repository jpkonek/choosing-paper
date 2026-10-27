"""PP76 check_t1_76 (CHECKED, exact): Theorem 1.1's description of the first-generation coupled refusals
at a committed source C, and Corollary 1.2 (no single acceptance exhausts a full-support source;
two-world exhaustion only on odd-k records), on all small H-instances."""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hlib76 import *

def formula(O, B, X, C, w):
    """Theorem 1.1 in H: rivals C+G refused at w.  G1 = G & D, G2 = G - D."""
    n = len(O); D = {g for g in range(n) if B[g] != X[g]}; res = set()
    for mask in range(1, 2 ** n):
        G = {g for g in range(n) if mask >> g & 1}
        G1, G2 = G & D, G - D
        if any(B[g] == C[g] for g in G1): continue                         # G1 inside {C != B}
        if any(better(O[g], w, C[g], X[g]) for g in G1): continue           # C weakly w-worse than X on G1
        if any(better(O[g], w, B[g], X[g]) for g in D - G1): continue       # B weakly w-worse than X on D-G1
        if any(not better(O[g], w, 1 - C[g], C[g]) for g in G2): continue   # flip strictly w-better on G2
        strict = (any(better(O[g], w, X[g], C[g]) for g in G1) or
                  any(better(O[g], w, X[g], B[g]) for g in D - G1) or len(G2) > 0)
        if not strict: continue
        Z = tuple(1 - C[g] if g in G else C[g] for g in range(n))
        res.add(Z)
    return res


random.seed(76)
tot = 0; mism = 0; exh3 = 0; exh2 = 0; exh2_bad = 0
for n in (3, 4):
    allm = models(n)
    for O in itertools.product(range(3), repeat=n):
        pairs = [(B, X) for B in allm for X in allm if B != X and not any(strictly_worse(O, w, B, X) for w in range(3))]  # strict (G) admits B <=_w X at all w
        if n == 5: pairs = random.sample(pairs, 120)
        for B, X in pairs:
            refs = {w: coupled_refusals(O, B, X, w, allm) for w in range(3)}
            for C in allm:
                forced = {}
                for w in range(3):
                    brute = {apply(C, r) for r in refs[w] if carries(C, r)}
                    f = formula(O, B, X, C, w)
                    tot += 1
                    if brute != f: mism += 1
                    forced[w] = brute
                if forced[0] & forced[1] & forced[2]: exh3 += 1
                for (i, j) in ((0, 1), (0, 2), (1, 2)):
                    k = 3 - i - j
                    for Z in forced[i] & forced[j]:
                        exh2 += 1
                        if any(O[g] != k for g in range(n) if Z[g] != C[g] and B[g] == X[g]): exh2_bad += 1
print('source/world checks:', tot, ' formula mismatches:', mism)
print('rivals refused at all three worlds by one acceptance:', exh3)
print('rivals refused at two worlds {i,j}:', exh2, ' of which the part off D is not on odd-k points:', exh2_bad)
