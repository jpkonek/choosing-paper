# Independent exact check of Q1 Prop Q1.3 (non-closed world-1 section of attempt A).
# Chain coordinate x in [0,1], mu-bar = Lebesgue. Sets = finite unions of half-open intervals, Fractions.
# Regular model X with E1 X cap M = D (N empty). World-1 cone: band U union_F G(F), g_F = 1_F - 1_[0,a).
# delta in G(F) iff tau_{delta - g_F} >= 0 on [0,1]; band iff tau_delta >= 0. tau piecewise linear -> check breakpoints.
from fractions import Fraction as Fr
def tau_at(terms, x):       # terms: list of (coef, lo, hi); tau(x) = sum coef*|[lo,hi) cap [x,1)|
    return sum(c*max(Fr(0), hi - max(lo, x)) for c, lo, hi in terms if hi > x)
def nonneg_tail(terms):
    pts = {Fr(0), Fr(1)}
    for _, lo, hi in terms: pts |= {lo, hi}
    return all(tau_at(terms, p) >= 0 for p in pts if 0 <= p <= 1)
a, d, h = Fr(3,10), Fr(1,10), Fr(1,10)
D = [(a, a+d), (1-h, Fr(1))]
K = 12                                       # J_0..J_{K-1}, truncated dyadic blocks of [a,1)
J = [(1-(1-a)/2**k, 1-(1-a)/2**(k+1)) for k in range(K)]
def A_j(j):                                  # in each J_k one sub-interval of length 2^-j |J_k|, disjoint across j
    out = []
    for lo, hi in J:
        L = hi - lo
        start = lo + L*(1 - Fr(1, 2**(j-1)))  # offsets: j=1 -> [lo, lo+L/2), j=2 -> [lo+L/2, lo+3L/4), ...
        out.append((start, start + L/2**j))
    return out
def delta_b(b): return [(Fr(1), lo, hi) for lo, hi in D] + [(Fr(-1), Fr(0), b)]
def in_G(b, F):  # delta_b - g_F
    return nonneg_tail(delta_b(b) + [(Fr(-1), lo, hi) for lo, hi in F] + [(Fr(1), Fr(0), a)])
def in_band(b): return nonneg_tail(delta_b(b))
def G(S, x): return sum(max(Fr(0), hi - max(lo, x)) for lo, hi in S if hi > x)
def beta_formula(F):
    pts = sorted({a, Fr(1)} | {p for lo, hi in D + F for p in (lo, hi) if p >= a})
    if any(G(D, p) < G(F, p) for p in pts): return None
    return min(Fr(1), min(p + G(D, p) - G(F, p) for p in pts))
def beta_bisect(test):
    lo, hi = Fr(0), Fr(1)
    if test(hi): return hi
    assert test(lo)
    for _ in range(60):
        mid = (lo + hi)/2
        if test(mid): lo = mid
        else: hi = mid
    return lo
# disjointness check of the family
fam = [A_j(j) for j in range(1, 9)]
ints = sorted(i for F in fam for i in F)
assert all(ints[k][1] <= ints[k+1][0] for k in range(len(ints)-1)), "family not disjoint"
print("A_1..A_8 pairwise disjoint: OK")
target = a + d + h
print("band value: formula", float(min(G(D,Fr(0)), d+h)), " bisection", float(beta_bisect(in_band)))
for j, F in enumerate(fam, 1):
    bf = beta_formula(F)
    if bf is None:
        emp = not any(in_G(Fr(k, 200), F) for k in range(201))
        print(f"j={j}: G_D >= G_F fails; formula says empty; grid check empty: {emp}"); assert emp; continue
    bb = beta_bisect(lambda b: in_G(b, F))
    print(f"j={j}: beta formula {float(bf):.10f}  bisection {float(bb):.10f}  < a+d+h? {bf < target}  gap {float(target-bf):.3e}")
    assert abs(bf - bb) < Fr(1, 10**12) and bf < target
print("a+d+h =", float(target), "in section?", in_band(target) or any(in_G(target, F) for F in fam))
