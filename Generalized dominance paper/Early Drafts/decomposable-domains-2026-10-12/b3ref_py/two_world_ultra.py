"""B3 referee / two_world_ultra.py -- Proposition R-B3.4' (referee): the B3.4 world inside a two-world
ranking on M_U that satisfies strict (G), (IB), (LA), (S) with closed sections for EVERY model, and fails only (C)
(mechanism of writeup Prop. R7.1, with mu replaced by pi = mu + c*delta_U at both worlds).

n = 2, K' = [a1, b1] = [0.35, 0.6].  Gaussian mu is rotation invariant: mu(sector) = angle / (2 pi) (we use angle).
Gamble g = (cos th, sin th).
  M+  = {g1 > 0 > g2} cap U = {th in (th(a1), 0)},     th(a) := -atan(a / (1 - a)).
  M-  = {g1 < 0 < g2} cap U = {phi in (phi(b1), pi/2)}, phi := pi - th, phi(b) := atan(b / (1 - b)).
  Coherent model D_[a,b] (a <= a1, b >= b1) has world-1 error set on M:
      S+(a) = (th(a1), th(a)]  in M+   (grows as a decreases),
      S-(b) = (phi(b), pi/2)   in M-   (shrinks as b increases).
Ultrafilter U of the measure algebra containing every (th(a0), th(a0) + h) in M+ (germ just outside S+(a0)).
  delta_U(S+(a)) = 1 iff a < a0.   On interval unions, U-membership is decided by that germ.
Path (index p in [0,1], p = 0 <-> e_2, model P_2 = D_[0,b1]; p = 1 <-> e_1, model P_1 = D_[a1,1]):
  A: p in [0, .25]   a = 0,                b: b1 -> bA     (E- shrinks)
  B: p in (.25, .5)  a: 0 -> a0 (open),     b = bA
  J: p = .5          a = a0,                b = bB < bA     (E- jumps UP by exactly c: compensates the lost germ)
  C: p in (.5, 1]    a: a0 -> a1,           b: bB -> 1
Checks: m(p) = pi(E1 C_p) continuous (=> every section {m <= v}, {m >= v} closed: (S) for regular X; for non-regular
X the lex-first N+ coordinate makes C_p strictly better at both worlds, section = [0,1]); the sum identity
pi(E1 X) + pi(E2 X) = pi(M) on regular X (=> every regular model undominated and competitive on {1,2});
crossing of C_.25 and C_.5; non-fineness of world 1 on M.
Run: python3 -I two_world_ultra.py
"""
import math
import random

random.seed(11)
a1, b1 = 0.35, 0.6
c = 0.2
a0 = 0.2


def th(a):
    return -math.atan(a / (1 - a))


def ph(b):
    return math.pi / 2 if b >= 1 else math.atan(b / (1 - b))


Mp = (th(a1), 0.0)            # M+ in theta
Mm = (ph(b1), math.pi / 2)    # M- in phi
lenM = (Mp[1] - Mp[0]) + (Mm[1] - Mm[0])
g0 = th(a0)                   # germ point in M+, germ on the right (th > g0)


def pi_val(plus, minus):
    """plus: list of theta-intervals in M+, minus: list of phi-intervals in M-."""
    lam = sum(b - a for a, b in plus) + sum(b - a for a, b in minus)
    germ = any(a <= g0 < b for a, b in plus)
    return lam + (c if germ else 0.0)


def E1(a, b):
    plus = [(Mp[0], th(a))] if th(a) > Mp[0] else []
    minus = [(ph(b), Mm[1])] if ph(b) < Mm[1] else []
    return plus, minus


# choose bA so that E-(bA) has mass len(M-) - 0.3, and bB so that it has mass len(M-) - 0.3 + c
def b_of_mass(mass):         # mass of S-(b) = pi/2 - phi(b)
    phi = math.pi / 2 - mass
    t = math.tan(phi)
    return t / (1 + t)


lenMm = Mm[1] - Mm[0]
bA = b_of_mass(lenMm - 0.3)
bB = b_of_mass(lenMm - 0.3 + c)
assert b1 <= bB < bA < 1


def path(p):
    if p <= 0.25:
        s = p / 0.25
        return 0.0, b1 + s * (bA - b1)
    if p < 0.5:
        s = (p - 0.25) / 0.25
        return s * a0, bA
    s = (p - 0.5) / 0.5
    return a0 + s * (a1 - a0), bB + s * (1 - bB)


N = 40000
ps = [k / N for k in range(N + 1)]
m = [pi_val(*E1(*path(p))) for p in ps]
print("pi(M) =", round(lenM + c, 6), " m(0) =", round(m[0], 6), " m(1) =", round(m[-1], 6))
steps = [abs(m[k + 1] - m[k]) for k in range(N)]
print("max |m step| on grid 1/%d: %.2e  (continuity)" % (N, max(steps)))
kJ = N // 2
print("m just before / at the jump index p=.5: %.6f / %.6f" % (m[kJ - 1], m[kJ]))
print("measure jump of the selection at p=.5 (lambda part only): %.6f"
      % (abs((lambda P: sum(b - a for a, b in P[0] + P[1]))(E1(*path(0.5)))
             - (lambda P: sum(b - a for a, b in P[0] + P[1]))(E1(*path(0.5 - 1e-9))))))

# crossing: C_.25 vs C_.5
P25, P5 = E1(*path(0.25)), E1(*path(0.5))
d1 = (P25[0][0][1] - P5[0][0][1])            # S+(0) \ S+(a0) mass
d2 = (P25[1][0][0] - P5[1][0][0])            # S-(bB) \ S-(bA) mass (phi lower endpoints)
print("crossing C_.25 / C_.5: mass in E1C_.25 \\ E1C_.5 = %.4f, in E1C_.5 \\ E1C_.25 = %.4f" % (d1, d2))


# sum identity and competitiveness on random regular models (interval unions in M+, M-)
def rand_union(lo, hi):
    out = []
    for _ in range(random.randint(0, 3)):
        a = random.uniform(lo, hi)
        b = min(hi, a + random.uniform(0, (hi - lo) / 2))
        out.append((a, b))
    out.sort()
    merged = []
    for a, b in out:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))
    return merged


def complement(iv, lo, hi):
    out, cur = [], lo
    for a, b in iv:
        if a > cur:
            out.append((cur, a))
        cur = max(cur, b)
    if cur < hi:
        out.append((cur, hi))
    return out


def germ_force(iv):
    if random.random() < 0.3:
        iv = iv + [(g0 - 1e-3, g0 + random.uniform(1e-4, 0.05))]
        iv.sort()
        merged = []
        for a, b in iv:
            if merged and a <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], b))
            else:
                merged.append((a, b))
        iv = merged
    return iv


bad_sum = bad_comp = 0
for _ in range(3000):
    Ep = germ_force(rand_union(*Mp))          # world-1 error of X on M+
    Em = rand_union(*Mm)                      # world-1 error of X on M-
    v1 = pi_val(Ep, Em)
    v2 = pi_val(complement(Ep, *Mp), complement(Em, *Mm))   # world-2 error on M is the complement
    if abs(v1 + v2 - (lenM + c)) > 1e-9:
        bad_sum += 1
    p = random.random()
    mp = pi_val(*E1(*path(p)))
    if not (mp <= v1 + 1e-12 or (lenM + c - mp) <= v2 + 1e-12):
        bad_comp += 1
print("sum identity failures:", bad_sum, "; competitiveness failures:", bad_comp, "(3000 random regular X)")

# non-fineness: Z not in U, lambda(Z) = 0.05 < c; random finite partitions of M+ u M- into intervals
worst = 1e9
for _ in range(2000):
    k = random.randint(1, 40)
    cuts = sorted(random.uniform(*Mp) for _ in range(k))
    pts = [Mp[0]] + cuts + [Mp[1]]
    vals = [pi_val([(pts[r], pts[r + 1])], []) for r in range(len(pts) - 1)]
    worst = min(worst, max(vals))
print("pi(Z) = 0.05; min over random partitions of the largest piece: %.4f (>= c = %.2f: not fine)" % (worst, c))
