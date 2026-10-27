"""Referee C12: independent checks of Theorem C2.1 (NUMERICS; no verdict rests on them).

Run: python3 -I ref_c2.py
Independent of c2py/ld_two_world.py: Monte Carlo Gaussian atoms in R^2 (not angle cells),
a radius-dependent base density rho0, and an exact per-pair knapsack test of competitiveness.
"""
import math
import random

rng = random.Random(7)
AL, BE = 0.3, 0.55          # K' = [alpha', beta'] (weight t of world 2)
N = 60000

def in_DK(g, a, b):
    """g in D_[a,b]: (1-t)g1 + t g2 > 0 on [a,b], or g >= 0 (nonzero)."""
    if g[0] >= 0 and g[1] >= 0:
        return True
    return min((1 - a) * g[0] + a * g[1], (1 - b) * g[0] + b * g[1]) > 0

pts = []
for _ in range(N):
    g = (rng.gauss(0, 1), rng.gauss(0, 1))
    if not in_DK(g, AL, BE):
        continue                       # outside U
    if g[0] > 0 and g[1] > 0:
        pts.append((g, 'N', None))
        continue
    if g[0] < 0 < g[1]:
        sig = -g[0] / (g[1] - g[0]); x = sig / AL
    else:
        tau = g[0] / (g[0] - g[1]); x = (tau - BE) / (1 - BE)
    assert 0 < x < 1
    pts.append((g, 'M', x))
M = [p for p in pts if p[1] == 'M']
print(f"U-samples {len(pts)}, M-samples {len(M)}")

# 1. error sets of the path: E_1(C_s) cap M == {x < s}, E_2(C_s) cap M == {x >= s}; C_s accepts N_+
bad = 0
for s in [0.0, 0.07, 0.31, 0.5, 0.88, 1.0]:
    a, b = AL * s, BE + (1 - BE) * s
    for g, kind, x in pts:
        acc = in_DK(g, a, b)
        if kind == 'N':
            bad += (not acc)
            continue
        e1 = (not acc) if g[0] > 0 else acc
        e2 = (not acc) if g[1] > 0 else acc
        bad += (e1 != (x < s)) + (e2 == e1)
print("1. path error-set mismatches (world 1, world 2 complementarity, N_+ accepted):", bad)

# members: rho0 radius dependent; F_a, G_b functions of x
rho0 = lambda g: math.exp(-0.3 * math.hypot(*g)) * (1 + 0.5 * math.sin(3 * math.atan2(g[1], g[0])) ** 2)
FA = [lambda x: 1 + x, lambda x: 1 + 3 * x * x, lambda x: 1 / math.sqrt(1 - x)]   # last: unbounded ratio near 1
GB = [lambda x: 1.0, lambda x: 2 - x]
wF = [[f(x) * rho0(g) for g, _, x in M] for f in FA]
wG = [[h(x) * rho0(g) for g, _, x in M] for h in GB]
X = [x for _, _, x in M]

def cs(s):
    return [1.0 if x < s else 0.0 for x in X]

# 2. exact worst case of competitiveness for each (a, b): minimise wF_a(A) s.t. wG_b(A) >= wG_b(c_s)
#    (fractional knapsack = Lyapunov in the continuum); must be >= wF_a(c_s)
worst = float('inf')
for s in [0.05 * k for k in range(1, 20)]:
    c = cs(s)
    for fa in wF:
        for gb in wG:
            tgt = sum(p * q for p, q in zip(gb, c))
            order = sorted(range(len(X)), key=lambda i: fa[i] / gb[i])
            accg = accf = 0.0
            for i in order:
                if accg >= tgt:
                    break
                t = min(1.0, (tgt - accg) / gb[i])
                accg += t * gb[i]; accf += t * fa[i]
            fc = sum(p * q for p, q in zip(fa, c))
            worst = min(worst, (accf - fc) / max(fc, 1e-12))
print(f"2. min relative slack of competitiveness over s, (a,b): {worst:.3e}  (>= -1e-12 expected)")

# 3. negative control: world-2 density NOT a function of x (depends on the half M-/M+)
GBn = [lambda g, x: 1.0 + (4.0 if g[0] > 0 else 0.0)]
wGn = [[h(g, x) * rho0(g) for g, _, x in M] for h in GBn]
fails = 0
for s in [0.05 * k for k in range(1, 20)]:
    c = cs(s)
    for fa in wF[:2]:
        for gb in wGn:
            tgt = sum(p * q for p, q in zip(gb, c)) * 1.0001
            order = sorted(range(len(X)), key=lambda i: fa[i] / gb[i])
            accg = accf = 0.0
            for i in order:
                if accg >= tgt:
                    break
                t = min(1.0, (tgt - accg) / gb[i])
                accg += t * gb[i]; accf += t * fa[i]
            fc = sum(p * q for p, q in zip(fa, c))
            fails += accf < fc - 1e-9
print("3. negative control (ratio not monotone in x): competitiveness failures", fails, "(> 0 expected)")

# 4. sections are closed intervals [0,s1], [s2,1] with s2 <= s1, for random arbitrary models
def le1(Ae, n1, Be, n2, nd=1.0):
    return all(sum(w[i] * Ae[i] for i in range(len(X))) + nd * n1 <= sum(w[i] * Be[i] for i in range(len(X))) + nd * n2 + 1e-12 for w in wF)
def le2(Ae, n1, Be, n2, nd=1.0):
    return all(sum(w[i] * (1 - Ae[i]) for i in range(len(X))) + nd * n1 <= sum(w[i] * (1 - Be[i]) for i in range(len(X))) + nd * n2 + 1e-12 for w in wG)
grid = [k / 40 for k in range(41)]
viol = 0
for trial in range(25):
    A = [float(rng.random() < (x ** rng.choice([0.5, 1, 2]) if rng.random() < 0.5 else 0.5)) for x in X]
    nm = rng.random() * 50 if rng.random() < 0.5 else 0.0
    S1 = [s for s in grid if le1(cs(s), 0, A, nm)]
    S2 = [s for s in grid if le2(cs(s), 0, A, nm)]
    i1 = [grid.index(s) for s in S1]; i2 = [grid.index(s) for s in S2]
    ok = (i1 == list(range(0, len(i1)))) and (i2 == list(range(41 - len(i2), 41))) and (set(S1) | set(S2) == set(grid))
    viol += not ok
print("4. section shape / cover violations over 25 random models (incl. non-regular):", viol)

# 5. C2.8 identity (Tp).u_b = c p.u_a pointwise, random numbers
err = 0.0
for _ in range(1000):
    ra, r2, r3 = [rng.uniform(0.5, 2) for _ in range(3)]
    s1, s2, s3 = [rng.choice([-1, 1]) for _ in range(3)]
    s11, c, s12, s13 = rng.uniform(.5, 2), rng.uniform(.5, 2), rng.uniform(0, .3), rng.uniform(0, .3)
    rb = (c * ra - s12 * s1 * s2 * r2 - s13 * s1 * s3 * r3) / s11
    p = [rng.random() for _ in range(3)]
    ua = (ra * s1, r2 * s2, r3 * s3); ub = (rb * s1, r2 * s2, r3 * s3)
    Tp = (s11 * p[0], s12 * p[0] + c * p[1], s13 * p[0] + c * p[2])
    err = max(err, abs(sum(a * b for a, b in zip(Tp, ub)) - c * sum(a * b for a, b in zip(p, ua))))
print(f"5. C2.8 identity max error: {err:.2e}")
