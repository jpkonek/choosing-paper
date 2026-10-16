"""S34 referee, independent checks of S3.1 / S3.2 (exact rationals; piecewise-constant sets in the chain coordinate x).
A set is a finite union of disjoint half-open intervals [l,r) in [0,1). World 1 = band U translates g_F = 1_F - 1_{c_a}.
Tail tau_delta(x) = int_{x(h)>=x} delta d(mu-bar) is piecewise linear, so 'tau_delta >= tau_g on [0,1]' is checked
exactly at all breakpoints (both functions linear between consecutive breakpoints).
(1) S3.2 formula: S_1(X_D) end = a+d+h - mu(F) for F in F_D (G_F <= G_D), band end d+h; bisection vs formula.
(2) Simplest open-section witness in S3.1 / Q1: D = d_a (E_1 X = [a,1)): accepted via F iff b <= 1 - mu(F); band iff b <= 1-a.
    Disjoint family => section [0,1), not closed.
(3) Referee counterexample: min_F mu(F) attained (kappa>0) but a world-1 section is still open
    (S3.2's 'closedness <=> attained' holds only for the test models D_{d,h}).
Run: python3 -I s3_sections.py
"""
from fractions import Fraction as Fr

def norm(iv):
    iv = sorted((l, r) for l, r in iv if r > l)
    out = []
    for l, r in iv:
        if out and l <= out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], r))
        else:
            out.append((l, r))
    return out

def meas(S): return sum(r - l for l, r in S)
def tailset(S, x): return sum(max(Fr(0), r - max(l, x)) for l, r in S)

def tau(pos, neg, x):  # delta = 1_pos - 1_neg (pos, neg disjoint)
    return tailset(pos, x) - tailset(neg, x)

def bps(*sets):
    pts = {Fr(0), Fr(1)}
    for S in sets:
        for l, r in S: pts.add(l); pts.add(r)
    return sorted(pts)

def minus(S, T):  # S \ T
    out = []
    for l, r in S:
        cur = [(l, r)]
        for a, b in T:
            nxt = []
            for u, v in cur:
                if b <= u or a >= v: nxt.append((u, v))
                else:
                    if a > u: nxt.append((u, a))
                    if b < v: nxt.append((b, v))
            cur = nxt
        out += cur
    return norm(out)

def accepted_cb_le_E(E, b, a, fam):
    """Is c_b <=_1 E, i.e. delta = 1_{E\\c_b} - 1_{c_b\\E} in band U translates? Returns (band, list of F indices)."""
    cb = [(Fr(0), b)]
    pos, neg = minus(E, cb), minus(cb, E)
    pts = bps(pos, neg, [(Fr(0), a)], *fam)
    band = all(tau(pos, neg, x) >= 0 for x in pts)
    ok = []
    for i, F in enumerate(fam):
        if all(tau(pos, neg, x) >= tau(F, [(Fr(0), a)], x) for x in pts):
            ok.append(i)
    return band, ok

def section_end(E, a, fam, which):
    """largest b (bisection, exact rationals, 40 steps) with c_b <=_1 E through the band (which=None) or F_which"""
    def acc(b):
        band, ok = accepted_cb_le_E(E, b, a, fam)
        return band if which is None else (which in ok)
    if not acc(Fr(0)): return None
    lo, hi = Fr(0), Fr(1)
    if acc(hi): return hi
    for _ in range(40):
        mid = (lo + hi) / 2
        if acc(mid): lo = mid
        else: hi = mid
    return lo

import random
random.seed(11)
a = Fr(3, 10)
print("(1) S3.2 formula, a = 0.3, D = [a,a+d) u [1-h,1)")
worst = 0
for trial in range(12):
    d = Fr(random.randint(5, 15), 100); h = Fr(random.randint(5, 12), 100)
    if a + d + 2*h >= 1: continue
    D = norm([(a, a + d), (1 - h, Fr(1))])
    # random F inside d_a with mu(F) <= h: a few small intervals
    F = []
    for _ in range(random.randint(1, 4)):
        l = Fr(random.randint(300, 990), 1000); w = Fr(random.randint(1, 20), 1000)
        F.append((l, min(Fr(1), l + w)))
    F = norm(F)
    if meas(F) > h: continue
    fam = [F]
    be = section_end(D, a, fam, 0); bb = section_end(D, a, fam, None)
    pred = a + d + h - meas(F)
    err = abs(be - pred)
    worst = max(worst, err)
    print(f"  d={float(d):.2f} h={float(h):.2f} mu(F)={float(meas(F)):.4f}: bisection {float(be):.6f}  formula {float(pred):.6f}  band {float(bb):.4f} (pred {float(d+h):.4f})")
print("  max |bisection - formula| =", float(worst))

print("(2) open-section witness D = d_a = [a,1) with the disjoint dyadic family of Q1.3")
# dyadic blocks J_k = [1-(1-a)2^-k, 1-(1-a)2^-(k+1)), A_j = one subinterval of length 2^-j |J_k| of each J_k, disjoint across j
K = 10
fam = []
for j in range(1, 7):
    S = []
    for k in range(K):
        L = 1 - (1 - a) * Fr(1, 2**k); R = 1 - (1 - a) * Fr(1, 2**(k + 1)); w = R - L
        off = sum(w * Fr(1, 2**i) for i in range(1, j))   # disjoint placement
        S.append((L + off, L + off + w * Fr(1, 2**j)))
    fam.append(norm(S))
E = [(a, Fr(1))]
for j, F in enumerate(fam):
    be = section_end(E, a, fam, j)
    print(f"  A_{j+1}: mu = {float(meas(F)):.6f}, section end via A_j = {float(be):.6f}, 1 - mu = {float(1-meas(F)):.6f}")
print("  band end:", float(section_end(E, a, fam, None)), "(pred 1-a = 0.7); sup over j -> 1, 1 not attained (C_1 = P_2 not <=_1 X by strict (G))")
# check 1 itself is never accepted
band, ok = accepted_cb_le_E(E, Fr(1), a, fam)
print("  c_1 <=_1 d_a accepted?", band or bool(ok))

print("(3) counterexample to 'min mu(F) attained => all world-1 sections closed'")
F0 = [(Fr(99, 100), Fr(1))]                     # mu = 0.01 = min
fam3 = [F0] + [norm([(Fr(1, 2), Fr(6, 10) + Fr(1, n))]) for n in range(5, 40, 3)]
D3 = [(a, Fr(8, 10))]
print("  measures:", [round(float(meas(F)), 4) for F in fam3])
ends = []
for j in range(len(fam3)):
    e = section_end(D3, a, fam3, j)
    ends.append(None if e is None else float(e))
print("  section ends per member (None = empty):", [None if e is None else round(e, 6) for e in ends])
print("  band end:", float(section_end(D3, a, fam3, None)))
print("  predicted 0.7 - 1/n for F_n:", [round(0.7 - 1/n, 6) for n in range(5, 40, 3)])
band, ok = accepted_cb_le_E(D3, Fr(7, 10), a, fam3)
print("  b = 0.7 accepted?", band or bool(ok), " -> with F_n for all n the section is [0,0.7), open, although min mu(F) = 0.01 is attained")
