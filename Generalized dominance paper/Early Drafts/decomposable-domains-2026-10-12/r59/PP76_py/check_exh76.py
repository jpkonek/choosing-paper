"""PP76 check_exh76 (CHECKED, exact): Cor 1.3 (refusal worlds at the source N = T are
W = ess-intersection of Up_T over U = {B = T != X}) and Prop 1.6 (multi-acceptance exhaustion
criterion with minimal G_0) on small H-instances, against brute-force coupled refusals."""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hlib76 import *
random.seed(761)

def up(O, T, g, i):  # flipping T at g improves world i
    return better(O[g], i, 1 - T[g], T[g])

def forced_at(O, B, X, T, allm):
    refs = {w: coupled_refusals(O, B, X, w, allm) for w in range(3)}
    return {w: {apply(T, r) for r in refs[w] if carries(T, r)} for w in range(3)}

def criterion(O, T, doms, n):
    """exists assignment world -> domination with i in W(d) and minimal G0 admissible"""
    data = []
    for (B, X) in doms:
        U = {g for g in range(n) if B[g] == T[g] != X[g]}
        L = {g for g in range(n) if B[g] != T[g] == X[g]}
        W = {i for i in range(3) if all(up(O, T, g, i) for g in U)}
        data.append((U, L, W))
    for sig in itertools.product(range(len(doms)), repeat=3):
        if any(i not in data[sig[i]][2] for i in range(3)): continue
        if any(not data[sig[i]][0] for i in range(3)): continue   # criterion stated for U non-empty
        G0 = set()
        for i in range(3):
            G0 |= {g for g in data[sig[i]][1] if up(O, T, g, i)}
        ok = all(not (G0 & data[sig[i]][0]) for i in range(3)) and \
             all({g for g in G0 if not up(O, T, g, i)} <= data[sig[i]][1] for i in range(3))
        if ok: return True
    return False

n = 4; allm = models(n); T = (1, 0, 1, 0)
ncheck = mis_w = mis_e = nexh = 0; cache = {}
for O in itertools.product(range(3), repeat=n):
    adm = [(B, X) for B in allm for X in allm if B != X and not any(strictly_worse(O, w, B, X) for w in range(3))
           and any(B[g] == T[g] != X[g] for g in range(n))]
    for (B, X) in adm:
        f = forced_at(O, B, X, T, allm); cache[(O, B, X)] = f
        U = [g for g in range(n) if B[g] == T[g] != X[g]]
        W = {i for i in range(3) if all(up(O, T, g, i) for g in U)}
        if {w for w in range(3) if f[w]} != W: mis_w += 1
    for _ in range(300):
        d1, d2 = random.sample(adm, 2)
        f1, f2 = cache[(O,) + d1], cache[(O,) + d2]
        brute = any(Z in (f1[0] | f2[0]) and Z in (f1[1] | f2[1]) and Z in (f1[2] | f2[2]) for Z in allm)
        crit = criterion(O, T, [d1, d2], n)
        ncheck += 1; nexh += brute
        if brute != crit: mis_e += 1
print('Cor 1.3 refusal-world mismatches:', mis_w)
print('pairs of acceptances checked:', ncheck, ' exhausting T:', nexh, ' criterion mismatches:', mis_e)
