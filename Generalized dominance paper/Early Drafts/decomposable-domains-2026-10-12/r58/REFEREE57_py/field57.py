"""field57: checks of PP69 Lemma 2.1, Lemma 2.2, Prop 5.1 premise, PP70 Lemma 1.1(b), Prop 2.7 ratio, threshold ranges.
Exact rationals on random integer problems.  Run: python3 -I -B field57.py"""
import sys, random
sys.path.insert(0, '.')
from rlib import *
from curve57 import *

rnd = random.Random(5757)
G = []
while len(G) < 2500:
    g = tuple(F(rnd.randint(-300, 300), rnd.randint(1, 40)) for _ in range(3))
    if cls(g) in (1, 2, 3): G.append(g)
pat_count = {}; fails = []
ranges = {}
nb = 0
for g in G:
    k = cls(g)
    advs, th = thresholds(g)
    key = (k, '>'.join(advs))
    pat_count[key] = pat_count.get(key, 0) + 1
    for i, t in enumerate(th):
        ranges.setdefault((k, '>'.join(advs), i), []).append(t)
    # (Lemma 2.1(b)/PP70 1.1(b)) at most two changes; 3-rank non-decreasing; ranks monotone at every world
    for w in (1, 2, 3):
        rs = [rank(k, a, w) for a in advs]
        mono = all(rs[i] <= rs[i + 1] for i in range(len(rs) - 1)) or all(rs[i] >= rs[i + 1] for i in range(len(rs) - 1))
        if not mono: fails.append(('monotone', g, w))
        if w == 3 and not all(rs[i] <= rs[i + 1] for i in range(len(rs) - 1)): fails.append(('3-desc', g))
    if len(advs) > 3: fails.append(('changes', g))
    # swap invariance of advice along theta
    gs = (g[1], g[0], g[2])
    if [a for a, _ in pattern(gs)] != advs or thresholds(gs)[1] != th: fails.append(('swap', g))
    ph = phi(g)
    # strict rank monotonicity of phi at every world
    for w in (1, 2, 3):
        order = sorted(['A', 'S', 'B', 'X'], key=lambda a: rank(k, a, w))
        vals = [ph[a][w - 1] for a in order]
        if not all(vals[i] < vals[i + 1] for i in range(3)): fails.append(('rankmono', g, w))
    if k == 3 and any(ph[a][0] != ph[a][1] for a in ph): fails.append(('f1=f2 on M3', g))
    # swap equivariance: phi(sigma g, a) = swap phi(g, a)
    ps = phi(gs)
    if any(ps[a] != (ph[a][1], ph[a][0], ph[a][2]) for a in ph): fails.append(('equivariance', g))
    # pathwise Bayes: unique argmin at theta on a grid and next to thresholds
    thetas = [F(i, 48) for i in range(49)] + [t + d for t in th for d in (F(1, 10**6), -F(1, 10**6))]
    for theta in thetas:
        if theta < 0 or theta > 1 or theta in th: continue
        pt = p(theta)
        U = {a: dot(pt, ph[a]) for a in ph}
        best = min(U.values())
        am = [a for a in U if U[a] == best]
        if am != [advice(theta, g)]: fails.append(('bayes', g, theta, am, advice(theta, g)))
    # switches: forward change lowers phi1+phi2, raises phi3; PP70 Prop 2.7 ratio
    for i in range(len(advs) - 1):
        a0, a1 = ph[advs[i]], ph[advs[i + 1]]
        d = [a1[j] - a0[j] for j in range(3)]
        if not (d[0] + d[1] < 0 and d[2] > 0): fails.append(('switch', g))
        # ratio: decrease of Phi1 (= mean of d1,d2 over the swap pair, or d1 on M3) <= half increase of Phi3
        dec = -(d[0] + d[1]) / 2
        if dec > d[2] / 2: fails.append(('ratio', g, dec, d[2]))
        nb += 1
print('problems: %d ; switches checked: %d' % (len(G), nb))
print('patterns (class, pattern): count')
for key in sorted(pat_count): print('  ', key, pat_count[key])
print('threshold ranges (sampled min, max) by (class, pattern, change index):')
for key in sorted(ranges):
    v = ranges[key]; print('  ', key, float(min(v)), float(max(v)))
print('failures:', len(fails), fails[:5])
