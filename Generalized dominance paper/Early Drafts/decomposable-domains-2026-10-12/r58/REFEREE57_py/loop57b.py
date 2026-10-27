"""loop57b: pointwise prerequisites for the loop's repair edges (exact chamber census).
Edge C -> B of class k: for each chamber-level class-k fill Y = C[E -> A] (E = one chamber of class k where C is
silent, and E = the whole class-k silence of C), report whether B is excluded by strict (G) alone
(B pointwise no better than Y at some world i != k, and different) or by agreement (B = A on all of E).
Not a domination proof: a pass only means the fill is not excluded pointwise."""
import sys
sys.path.insert(0, '.')
from rlib import *

for s in (F(1, 2), F(19, 20)):
    m = {0: (F(1), F(1), F(1)), 1: (F(1), F(1), s), 2: (s, F(1), s)}
    Ks = {i: post(m[i], VM) for i in m}
    pts, _ = chambers(list(Ks.values()))
    Cm = {i: {g: adv(Ks[i], g) for g in pts} for i in m}
    print('s = %s' % s)
    for (x, y, k) in [(0, 1, 3), (1, 2, 1), (2, 0, 2)]:
        src, dfd = Cm[x], Cm[y]
        sil = [g for g in pts if cls(g) == k and src[g] == 'S']
        res = []
        for E in [[g] for g in sil] + [sil]:
            Y = dict(src)
            for g in E:
                Y[g] = 'A'
            agree = all(dfd[g] == 'A' for g in E)
            excl = []
            for i in (1, 2, 3):
                if i == k:
                    continue
                if all(rank(cls(g), dfd[g], i) >= rank(cls(g), Y[g], i) for g in pts) and any(dfd[g] != Y[g] for g in pts):
                    excl.append(i)
            res.append((agree, excl))
        ok = sum(1 for r in res[:-1] if not r[0] and not r[1])
        print('  edge C_m%d -> C_m%d (class %d): %d silent class-%d chambers of the source; single-chamber fills not '
              'excluded pointwise: %d; whole-silence fill: agreement=%s, strict-(G) exclusion at worlds %s'
              % (x, y, k, len(sil), k, ok, res[-1][0], res[-1][1]))
        for r, g in zip(res[:-1], sil):
            if r[0] or r[1]:
                print('     excluded chamber fill: agreement=%s, strict-(G) at %s ; defender advice there %s'
                      % (r[0], r[1], dfd[g]))
