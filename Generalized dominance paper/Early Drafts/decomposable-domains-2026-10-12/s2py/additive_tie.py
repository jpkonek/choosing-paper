"""S2 numerics (1): two-world additive system on a discretised U-domain with a double atom tie.

Setting (Prop. lattice of the write-up): M^- cells indexed by sigma (increasing), M^+ cells by tau
(increasing). A coherent model is (alpha, beta): world-1 errors = {sigma < alpha} u {tau <= beta},
i.e. an initial block of M^- cells and an initial block of M^+ cells.

Additive field: densities rho1, rho2 > 0 per cell; t-Bayes (t = weight of world 2):
cell g in E_1 iff (1-t) rho1(g) < t rho2(g), i.e. r(g) := rho1/(rho1+rho2) < t ; tie iff r = t.
For coherence r must be nondecreasing along sigma on M^- and along tau on M^+ (here: increasing,
with a flat atom r = t0 on a block of each side).

Checks (exact rationals):
 (a) Bayes error sets at t < t' are nested (any tie-breaking), on a grid of t.
 (b) At t0 the coherent Bayes models form a rectangle; it contains crossing pairs.
 (c) For a crossing pair there is an INCOHERENT model with exactly the same (psi1, psi2) profile
     as a coherent t0-Bayes model, so (C) fails for the pure additive system (it is t0-Bayes,
     hence undominated, and tied at both worlds with a coherent undominated model).
"""
from fractions import Fraction as Fr
import itertools, random

random.seed(1)
n = 12                      # cells per side
t0 = Fr(2, 5)
atomM = range(4, 8)          # sigma-cells with r = t0
atomP = range(5, 9)          # tau-cells with r = t0

def ratio(side, k):
    atom = atomM if side == '-' else atomP
    if k in atom:
        return t0
    lo, hi = atom.start, atom.stop
    if k < lo:
        return t0 * Fr(k + 1, lo + 1)          # < t0, increasing
    return t0 + (1 - t0) * Fr(k - hi + 1, n - hi + 1)   # > t0, increasing

cells = [('-', k) for k in range(n)] + [('+', k) for k in range(n)]
rho1 = {c: Fr(random.randint(1, 9), 3) for c in cells}
# inside the atoms use a constant density (a discretisation of a non-atomic atom: cells are
# exchangeable pieces of equal rho1-mass, as Lyapunov provides in the continuum)
for c in cells:
    if (c[0] == '-' and c[1] in atomM) or (c[0] == '+' and c[1] in atomP):
        rho1[c] = Fr(2)
rho2 = {c: rho1[c] * (1 - ratio(*c)) / ratio(*c) for c in cells}   # so rho1/(rho1+rho2) = r
mass = {c: Fr(1) for c in cells}                                   # mu-mass of each cell

def profile(E1):
    psi1 = sum(rho1[c] for c in E1)
    psi2 = sum(rho2[c] for c in cells if c not in E1)   # world-2 errors = M \ E_1
    return psi1, psi2

def bayes_sets(t):
    """all tie-breakings: return (strict part, tie part) of E_1 at weight t."""
    strict = {c for c in cells if (1 - t) * rho1[c] < t * rho2[c]}
    tie = {c for c in cells if (1 - t) * rho1[c] == t * rho2[c]}
    return strict, tie

# (a) nestedness across weights, for the extreme tie-breakings
ok_a = True
grid = sorted({Fr(k, 40) for k in range(1, 40)} | {t0})
for t, u in itertools.combinations(grid, 2):
    s_t, z_t = bayes_sets(t)
    s_u, z_u = bayes_sets(u)
    big_t = s_t | z_t          # largest t-Bayes error set
    small_u = s_u              # smallest u-Bayes error set
    if not big_t <= small_u:
        ok_a = False
        print('nesting fails', t, u)
print('(a) Bayes error sets nested across distinct weights (all tie-breaks):', ok_a)

# (b) coherent t0-Bayes models: initial blocks inside the atoms
s0, z0 = bayes_sets(t0)
print('    tie set at t0 =', sorted(z0))
alphas = [atomM.start + a for a in range(len(atomM) + 1)]   # number of M^- cells erred
betas = [atomP.start + b for b in range(len(atomP) + 1)]
def coherent(a, b):
    return {('-', k) for k in range(a)} | {('+', k) for k in range(b)}
rect = [(a, b) for a in alphas for b in betas]
assert all(s0 <= coherent(a, b) <= s0 | z0 for a, b in rect)
cross = [((a, b), (a2, b2)) for (a, b), (a2, b2) in itertools.combinations(rect, 2)
         if (a - a2) * (b - b2) < 0]
print('(b) coherent t0-Bayes models:', len(rect), '; crossing pairs among them:', len(cross))

# (c) incoherent splice with equal profile
(a, b), (a2, b2) = cross[0]
C = coherent(a, b)
found = None
inside = sorted(z0)
for r in range(1, len(inside) + 1):
    for S in itertools.combinations(inside, r):
        E = s0 | set(S)
        # coherent iff it is an initial block on each side
        km = sorted(k for s, k in E if s == '-'); kp = sorted(k for s, k in E if s == '+')
        coh = km == list(range(len(km))) and kp == list(range(len(kp)))
        if not coh and profile(E) == profile(C) and E != C:
            found = E; break
    if found: break
print('(c) coherent C =', (a, b), 'profile', profile(C))
print('    incoherent tied splice found:', found is not None)
if found:
    print('    splice error cells in the tie set:', sorted(found & z0), 'profile', profile(found))
