# F1.4 combinatorial core (NUMERICS only): from a fractional cover sum_g w_g 1_{P_g} >= 1_S (w_g <= 1) with target cost
# Gamma = sum_g w_g c_g, independent rounding (keep g with prob w_g) yields, with positive probability, a subfamily
# covering >= (1-1/e)/2 of S at cost <= 4 Gamma.  Checked exhaustively-by-sampling on random instances, including
# "projective" covers whose sources pairwise intersect (no disjoint subfamily larger than one set).
import random, math
random.seed(7)
def pg2_lines(q):
    pts = [(x, y, 1) for x in range(q) for y in range(q)] + [(x, 1, 0) for x in range(q)] + [(1, 0, 0)]
    return [[j for j, p in enumerate(pts) if sum(a * b for a, b in zip(l, p)) % q == 0] for l in pts], len(pts)
worst_unc = 0.0; ok = 0; tot = 0
for inst in range(300):
    if inst % 3 == 0:
        q = random.choice((2, 3, 5)); fam, npts = pg2_lines(q); w = [1 / (q + 1)] * len(fam)   # exact fractional cover
    else:
        npts = random.randint(5, 40); fam = [];
        for _ in range(random.randint(5, 30)):
            fam.append(random.sample(range(npts), random.randint(1, npts // 2 + 1)))
        cov = [0.0] * npts; w = []
        for P in fam: w.append(random.random())
        for P, x in zip(fam, w):
            for h in P: cov[h] += x
        # rescale so every covered point has coverage >= 1, cap at 1
        m = min((cov[h] for h in range(npts) if cov[h] > 0), default=1)
        w = [min(1.0, x / m) for x in w]
    S = sorted({h for P in fam for h in P})
    c = [random.random() for _ in fam]
    Gam = sum(x * y for x, y in zip(w, c))
    # per-point uncovered probability
    for h in S:
        pu = 1.0
        for P, x in zip(fam, w):
            if h in P: pu *= (1 - x)
        worst_unc = max(worst_unc, pu)
    good = False
    for trial in range(400):
        J = [i for i in range(len(fam)) if random.random() < w[i]]
        cv = len({h for i in J for h in fam[i]}); cost = sum(c[i] for i in J)
        if cv >= (1 - 1 / math.e) / 2 * len(S) and cost <= 4 * Gam + 1e-12: good = True; break
    tot += 1; ok += good
print("max per-point uncovered probability: %.4f (bound 1/e = %.4f)" % (worst_unc, 1 / math.e))
print("instances with a good selection found: %d / %d" % (ok, tot))
