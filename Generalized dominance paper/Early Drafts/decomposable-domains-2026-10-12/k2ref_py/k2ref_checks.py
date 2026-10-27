"""Referee checks for K2 (run with python3 -I). NUMERICS only.

(1) Edge (1,3) kills c1: on the Brier base, the edge-(1,3) forced two-ball trades (error moved from
    Q1 & {r3 > theta} to Q1 & {r3 <= theta}, rho3-mass ratio 1+eta) violate endorsement by
    phi_c = c0 rho1 + c1 rt2 + c2 rt3 when c1 > 0.  On Q1: phi_c/rho3 = c0/r3 + c1 rho2/rho3 + c2.
    (K2's table asserts "killed by edge (1,3)" for c = (1,0.3,0) but its script tests only edge (1,2).)
(2) ADJ_12 on the Brier base: Q1 & {r2 just above theta, rho3/rho2 > a} and Q2 & {r2 just below theta,
    rho3/rho2 > a} both sampled non-empty (K2's outcome says "both hold for the Brier base").
(3) Referee strengthening (scheme-free endorsers): on Q1 & {g1<0} = (-,+,+) & U, with x=|g2/g1|,
    y=|g3/g1|, the region W = {(x,y): (-1,x,y) in U} is up-closed and its x-projection is (0,inf);
    on Q1 & {g1>0} = (+,-,-) & U the region {(x,y): (1,-x,-y) in U} is down-closed.  Up/down-closedness
    gives overlapping sections, which forces x H2(x) = y H3(y) = const (see K2_referee.md, R6.2).
(4) K2.4(e) sanity: for random finite families of frontier weights, the region outside E_1(F_smin)
    meets the union of the other error sets only in Q2 (world j = 2), and for smax only in Q3.
"""
import random

EPS, S = 0.3, 0.9
c0 = (1 - EPS) / 3
V = [[c0 + (EPS if j == k else 0.0) for j in range(3)] for k in range(3)]
VP = [[1/3 + S*(V[k][j]-1/3) for j in range(3)] for k in range(3)]

def inU(g):
    return min(sum(VP[k][j]*g[j] for j in range(3)) for k in range(3)) > 0

def sgn(x):
    return 1 if x > 0 else -1

def cls(g):
    s = [sgn(x) for x in g]
    if s[0] == s[1] == s[2]:
        return 0
    for l in range(3):
        o = [s[m] for m in range(3) if m != l]
        if o[0] == o[1] and s[l] != o[0]:
            return l + 1

def sample(n, seed):
    rng = random.Random(seed)
    pts = []
    while len(pts) < n:
        g = [rng.gauss(0, 1) for _ in range(3)]
        if inU(g):
            pts.append(g)
    return pts

def part1(pts, theta=1.0, band=0.05):
    q1 = [g for g in pts if cls(g) == 1]
    above = [g for g in q1 if theta < abs(g[2]/g[0]) < theta + band]
    below = [g for g in q1 if theta - band < abs(g[2]/g[0]) <= theta]
    def ratio(g, c):  # phi_c / rho3 on Q1
        r1, r2, r3 = abs(g[0]), abs(g[1]), abs(g[2])
        return (c[0]*r1 + c[1]*r2 + c[2]*r3)/r3
    for c in [(1, 0, 0), (1, 0.3, 0), (1, 0.05, 0), (1, 0, 0.3)]:
        worst = -1e9
        for h in above:
            for hp in below:
                worst = max(worst, ratio(h, c) - (1+1e-3)*ratio(hp, c))
        print("(1) edge(1,3) c=%s: max (phi/rho3)(h)-(1+eta)(phi/rho3)(h') = %+.4f %s"
              % (c, worst, "violation" if worst > 0 else "endorsed on sample"))
    print("(1) pairs %d x %d" % (len(above), len(below)))

def part2(pts, theta=1.0, band=0.05):
    best = None
    for a in [0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0]:
        A = [g for g in pts if cls(g) == 1 and theta < abs(g[1]/g[0]) < theta+band and abs(g[2]/g[1]) > a]
        B = [g for g in pts if cls(g) == 2 and theta-band < abs(g[1]/g[0]) <= theta and abs(g[2]/g[1]) > a]
        print("(2) ADJ_12 theta=%.2f a=%.2f: |Q1 above|=%d |Q2 below|=%d" % (theta, a, len(A), len(B)))

def part3(rng):
    viol_up = viol_dn = 0
    for _ in range(200000):
        x, y = rng.expovariate(0.3), rng.expovariate(0.3)
        dx, dy = rng.random(), rng.random()
        if inU((-1, x, y)) and not inU((-1, x+dx, y+dy)):
            viol_up += 1
        if inU((1, -x-dx, -y-dy)) and not inU((1, -x, -y)):
            viol_dn += 1
    # x-projection of the up-closed region reaches small x (with y large)
    smallx = [x for x in (1e-3, 1e-2, 0.1, 0.5) if inU((-1, x, 1e4))]
    print("(3) up-closure violations (-,+,+): %d; down-closure violations (+,-,-): %d" % (viol_up, viol_dn))
    print("(3) small x attained on (-,+,+)&U with y large: %s" % smallx)

def part4(pts, rng):
    bad = 0
    trials = 0
    for _ in range(200):
        ss = sorted(rng.uniform(0.05, 0.95) for _ in range(rng.randint(2, 5)))
        ks = [s/(1-s) for s in ss]
        def E1(g, k):
            c = cls(g)
            r = abs(g[2])/abs(g[1])
            return c == 1 or (c == 2 and r < k) or (c == 3 and r > k)
        for g in pts[:6000]:
            if cls(g) == 0:
                continue
            # possible gain point for the min-s base: outside E1(F_min), inside some other E1(F_l)
            if not E1(g, ks[0]) and any(E1(g, k) for k in ks[1:]):
                trials += 1
                if cls(g) != 2:
                    bad += 1
            if not E1(g, ks[-1]) and any(E1(g, k) for k in ks[:-1]):
                trials += 1
                if cls(g) != 3:
                    bad += 1
    print("(4) K2.4(e): %d candidate gain points, %d outside the predicted class" % (trials, bad))

def main():
    pts = sample(60000, 11)
    part1(pts)
    part2(pts)
    rng = random.Random(5)
    part3(rng)
    part4(pts, rng)

if __name__ == "__main__":
    main()
