"""B3 / prop7_kappa.py -- algebraic core of Proposition B3.7 (exchangeable signatures are additive).

Setting (see B3_notes.md, B3.7).  A complete world whose top level is the value
    Phi(A) = nu(A) + kappa(Sigma(A)),   Sigma(A) = {j : A in U_j}  (finitely many ultrafilters U_1..U_m),
with nu a non-atomic measure.  For s, t subsets of [m] put
    D(s,t)  = kappa(s) - kappa(t),        D'(s,t) = kappa(s \\ t) - kappa(t \\ s).
The proof realises, for every s, t and every x in (-X, X) (X = nu(M) - 2 eta), sets A, B with
Sigma(A) = s, Sigma(B) = t and nu(A\\B) - nu(B\\A) = x.  Cancellation of the world gives the
"weak cancellation" of the top level:
    x + D < 0  =>  x + D' <= 0     and     x + D > 0  =>  x + D' >= 0.
If D != D', any x strictly between -D and -D' violates one of these.  So (when 4 max|kappa| < X)
D = D' for all s, t, which forces kappa additive (kappa(empty) = 0).

This script checks the finite algebra exactly (fractions): for random integer kappa on 2^[m], m <= 4,
  - additive kappa: no violating (s, t, x) on a fine rational grid of x;
  - non-additive kappa: a violating (s, t, x) exists, with x in the realisable range.
It does NOT model ultrafilters (they cannot be simulated); realisability is proved in the note.
Run: python3 -I prop7_kappa.py
"""
from fractions import Fraction as Fr
from itertools import product
import random

random.seed(7)


def subsets(m):
    return [frozenset(j for j in range(m) if (mask >> j) & 1) for mask in range(1 << m)]


def is_additive(kap, m):
    return all(kap[s] == sum(kap[frozenset([j])] for j in s) for s in subsets(m))


def violations(kap, m, X):
    """Return list of (s, t, x) violating weak cancellation, x in the open interval (-X, X)."""
    out = []
    S = subsets(m)
    for s, t in product(S, S):
        D = kap[s] - kap[t]
        Dp = kap[s - t] - kap[t - s]
        if D == Dp:
            continue
        x = -(D + Dp) / 2          # strictly between -D and -D'
        if -X < x < X:
            out.append((tuple(sorted(s)), tuple(sorted(t)), x))
    return out


def grid_check_additive(kap, m, X, N=40):
    S = subsets(m)
    bad = 0
    for s, t in product(S, S):
        D = kap[s] - kap[t]
        Dp = kap[s - t] - kap[t - s]
        for k in range(-N, N + 1):
            x = Fr(k, N) * X
            if (x + D < 0 and x + Dp > 0) or (x + D > 0 and x + Dp < 0):
                bad += 1
    return bad


n_add = n_nonadd = n_nonadd_found = 0
for trial in range(400):
    m = random.choice([2, 3, 4])
    S = subsets(m)
    if trial % 2 == 0:  # additive kappa with nonnegative atoms
        w = [Fr(random.randint(0, 5)) for _ in range(m)]
        kap = {s: sum((w[j] for j in s), Fr(0)) for s in S}
    else:               # arbitrary kappa with kappa(empty) = 0
        kap = {s: (Fr(0) if not s else Fr(random.randint(0, 9))) for s in S}
    maxk = max(abs(v) for v in kap.values())
    X = 4 * maxk + 1   # realisable range assumption of B3.7: 4 max|kappa| < X
    if is_additive(kap, m):
        n_add += 1
        assert not violations(kap, m, X), "additive kappa produced a violation"
        assert grid_check_additive(kap, m, X) == 0
    else:
        n_nonadd += 1
        v = violations(kap, m, X)
        if v:
            n_nonadd_found += 1
        else:
            raise AssertionError("non-additive kappa without violation: %r" % kap)

print("additive kappas checked (no violation):", n_add)
print("non-additive kappas:", n_nonadd, " with an explicit violating (s,t,x):", n_nonadd_found)
print("RESULT: weak cancellation on the realisable x-range holds iff kappa is additive  [NUMERICS, exact]")
