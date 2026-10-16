"""NUMERICS for Theorem K3.3 in K3_notes.md: the tilted world of Q12_referee N3 (two worlds, chain coordinate x
uniform on [0,1), unanimous problems ignored here).  World 1 accepts delta iff for some K > 0 every tail
int_{x>=y} e^{Kx} delta dx is >= 0.  We check, on exact piecewise-constant data:
 (a) every cut pair (P,Q) with non-null target is accepted for some K;
 (b) for random positive step densities rho and random localizing sets D (unions of small intervals), there is an
     accepted, D-localized cut pair with rho(P) > rho(Q)  (so no density endorses the localized comparisons);
 (c) the section of X with E_1 X = c_x minus Z (Z inside c_{x-eta}) is [0, x): open at x."""
import numpy as np
import mpmath as mp
mp.mp.dps = 60

rng = np.random.default_rng(3)


def tails_ok(intervals, K, ys):
    """intervals: list of (a, b, sign); delta = sum sign*1_[a,b). tail(y) = int_{x>=y} e^{Kx} delta."""
    def F(a, b):  # int_a^b e^{Kx} dx, in high precision (no under/overflow)
        K_ = mp.mpf(K)
        return (mp.e ** (K_ * b) - mp.e ** (K_ * a)) / K_
    vals = []
    for y in ys:
        t = mp.mpf(0)
        for a, b, sg in intervals:
            lo = max(a, y)
            if lo < b:
                t += sg * F(lo, b)
        vals.append(t)
    return min(vals) >= 0


def accepted(intervals, Kmax=400.0):
    ys = sorted({a for a, _, _ in intervals} | {b for _, b, _ in intervals} | {0.0})
    for K in np.geomspace(0.1, Kmax, 60):
        if tails_ok(intervals, K, ys):
            return K
    return None


# (a)
ok = 0
for _ in range(300):
    b = rng.uniform(0.1, 0.9)
    p0 = rng.uniform(0, b * 0.9); al = rng.uniform(0, b - p0)
    q0 = rng.uniform(b, 0.99); be = rng.uniform(1e-4, 1e-2) * (1 - q0)
    K = accepted([(p0, p0 + al, -1), (q0, q0 + be, +1)], Kmax=4000.0)
    ok += K is not None
print("(a) cut pairs with tiny targets accepted for some K:", ok, "/ 300")

# (b)
fails = 0
for _ in range(200):
    cells = 50
    rho = np.exp(rng.normal(size=cells) * 1.5)          # positive step density on [0,1)
    eta = 0.05
    D = [(c, c + eta / 10) for c in rng.uniform(0, 1 - eta / 10, size=10)]   # localizing set, measure <= eta
    b = 0.5
    P = (0.1, 0.2)
    rhoP = sum(rho[int(x * cells)] for x in np.linspace(0.1, 0.2, 1001)[:-1]) * 0.1 / 1000
    # find a target interval in [b,1) avoiding D with rho(Q) < rho(P): a short interval at a point outside D
    found = False
    for q0 in np.linspace(b, 0.98, 400):
        q1 = q0 + 1e-4
        if any(not (q1 <= a or q0 >= c) for a, c in D):
            continue
        rhoQ = rho[int(q0 * cells)] * 1e-4
        if rhoQ < rhoP and accepted([(P[0], P[1], -1), (q0, q1, +1)], Kmax=4000.0) is not None:
            found = True
            break
    fails += not found
print("(b) cases with no unendorsed accepted D-localized cut pair found:", fails, "/ 200")

# (c) section of X: E_1 X = c_x \ Z with Z = [x - 0.3, x - 0.2) (inside c_{x - eta}); comparison C_b <= X has
#     delta = 1_{A \ c_b} - 1_{c_b \ A}; for b < x: A \ c_b = [b, x) minus Z part, c_b \ A = Z n c_b.
x = 0.7
Z = (x - 0.3, x - 0.2)
res = []
for b in [0.5, 0.6, 0.65, 0.69, 0.699, 0.6999, 0.7]:
    pos = [(max(b, Z[1]), x, +1)] if b < x else []
    neg = [(Z[0], min(b, Z[1]), -1)] if b > Z[0] else []
    res.append((b, accepted(pos + neg, Kmax=1e5) is not None))
print("(c) b, accepted:", res)
