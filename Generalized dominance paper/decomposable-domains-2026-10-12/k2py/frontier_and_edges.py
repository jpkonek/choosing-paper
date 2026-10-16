"""K2.4 / K2.6 NUMERICS on the Brier base (rho_i = |g_i|) over U = D_{K'}, T1 with eps=0.3, s=0.9.

(A) Frontier models F_s (Bayes for worlds 2,3 at weight (s,1-s)): accept g iff s*g2+(1-s)*g3>0.
    Check the formula E_1(F_s) = Q1 u (Q2 & {r<kappa}) u (Q3 & {r>kappa}), r=|g3|/|g2|, kappa=s/(1-s),
    and that F_s, F_s' cross (both differences have positive sampled mass).
(B) Edge (1,2) forced 2-ball vectors versus linear endorsers phi_c = c0*rho1 + c1*rt2 + c2*rt3
    (rt_j = rho_j where world j disagrees with world 1, -rho_j where it agrees).
    For theta = q1/q2, a gamble h in Q1 with r2=|g2/g1| just above theta (world-1 error of the
    edge Bayes model) and h' in Q1 with r2 just below (not an error): moving error mass from h to h'
    with rho2-mass ratio (1+eta) is forced (world 2 strictly improves). Endorsement by phi_c needs
    (phi_c/rho2)(h) <= (1+eta)(phi_c/rho2)(h'). We exhibit sampled pairs violating it for c2>0.
"""
import random, math

EPS, S = 0.3, 0.9
c0 = (1 - EPS) / 3
V = [[c0 + (EPS if j == k else 0.0) for j in range(3)] for k in range(3)]
U3 = [1/3]*3
VP = [[U3[j] + S*(V[k][j]-U3[j]) for j in range(3)] for k in range(3)]

def inU(g):
    return min(sum(VP[k][j]*g[j] for j in range(3)) for k in range(3)) > 0

def sign(x):
    return 1 if x > 0 else -1

def cls(g):
    s = [sign(x) for x in g]
    if s[0] == s[1] == s[2]:
        return 0  # N_+ (in U only the all-positive pattern occurs)
    for l in range(3):
        o = [s[m] for m in range(3) if m != l]
        if o[0] == o[1] and s[l] != o[0]:
            return l + 1
    raise ValueError

def sample(n, seed):
    rng = random.Random(seed)
    pts = []
    while len(pts) < n:
        g = [rng.gauss(0, 1) for _ in range(3)]
        if inU(g):
            pts.append(g)
    return pts

def partA(pts):
    mism = 0
    def E1(g, s):
        acc = s*g[1] + (1-s)*g[2] > 0
        return acc != (g[0] > 0)
    def E1formula(g, s):
        k = s/(1-s)
        c = cls(g)
        r = abs(g[2])/abs(g[1])
        if c == 0: return False
        if c == 1: return True
        if c == 2: return r < k
        return r > k
    for g in pts:
        for s in (0.3, 0.5, 0.7):
            if E1(g, s) != E1formula(g, s):
                mism += 1
    s1, s2 = 0.4, 0.6
    d12 = sum(1 for g in pts if E1(g, s1) and not E1(g, s2))
    d21 = sum(1 for g in pts if E1(g, s2) and not E1(g, s1))
    print("(A) formula mismatches: %d over %d samples x 3 weights" % (mism, len(pts)))
    print("(A) F_0.4 vs F_0.6: |E1(F_0.4) minus E1(F_0.6)| = %d, |E1(F_0.6) minus E1(F_0.4)| = %d (both >0: crossing)" % (d12, d21))

def partB(pts, theta=1.0, band=0.05):
    q1pts = [g for g in pts if cls(g) == 1]
    above = [g for g in q1pts if theta < abs(g[1]/g[0]) < theta + band]
    below = [g for g in q1pts if theta - band < abs(g[1]/g[0]) <= theta]
    def ratio(g, c):  # phi_c / rho2 on Q1 (both worlds 2,3 disagree with 1 there)
        r1, r2, r3 = abs(g[0]), abs(g[1]), abs(g[2])
        return (c[0]*r1 + c[1]*r2 + c[2]*r3)/r2
    for c in [(1, 0, 0), (1, 0, 0.05), (1, 0, 0.2), (1, 0.3, 0.0)]:
        worst = 0.0
        for h in above:
            for hp in below[:400]:
                v = ratio(h, c) - (1+1e-3)*ratio(hp, c)
                worst = max(worst, v)
        print("(B) c=%s: max over sampled forced pairs of (phi/rho2)(h)-(1+eta)(phi/rho2)(h') = %.4f %s"
              % (c, worst, "(violation)" if worst > 0 else "(endorsed on sample)"))
    print("(B) pairs: %d above x %d below theta=%.2f (band %.2f)" % (len(above), min(len(below),400), theta, band))

def main():
    pts = sample(60000, 7)
    partA(pts)
    partB(pts)

if __name__ == "__main__":
    main()
