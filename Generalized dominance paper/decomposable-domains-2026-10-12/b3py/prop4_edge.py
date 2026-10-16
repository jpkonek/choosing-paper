"""B3 / prop4_edge.py -- sanity check of Proposition B3.4 (crossing defeats Savage fineness, edge level).

Edge region R = [0,2) with Lebesgue lambda; U an ultrafilter of the measure algebra containing every (1, 1+h).
pi = lambda + c * delta_U  (0 < c < 1).  Both edge worlds order their error sets by pi:
    c <=_i A  iff  pi(c) <= pi(A);      R\\c <=_j R\\A  iff  pi(c) >= pi(A).
Path p -> c_p:  [0, 3pc)  (p <= 1/3);   (1, 1 + 1.5(p - 1/3))  (1/3 < p <= 2/3);
                (1, 1.5) u [0, 3(p-2/3)) u [1.5, 1.5 + 1.5(p-2/3))  (p > 2/3).
Ultrafilters cannot be simulated; on finite unions of intervals, membership in U is decided by the
right-germ at 1 ("contains (1, 1+h) for small h"), which is what this script uses for test sets.
Checks (NUMERICS): m(p) = pi(c_p) is continuous with m(0) = 0, m(1) = 2 + c; sections
S_i(A) = {p : m(p) <= pi(A)} and S_j(A) = {p : m(p) >= pi(A)} are closed (closed preimages of a continuous
m), and cover [0,1] ((K)); c_{1/3} and c_{1/2} cross; for a small Z (pi(Z) < c, no germ) every random
finite partition of R into intervals has a piece with pi > pi(Z) (non-fineness).
Run: python3 -I prop4_edge.py
"""
import random

random.seed(4)
c = 0.4


def norm(iv):
    iv = sorted((a, b) for a, b in iv if b > a)
    out = []
    for a, b in iv:
        if out and a <= out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], b))
        else:
            out.append((a, b))
    return out


def lam(iv):
    return sum(b - a for a, b in iv)


def germ(iv):  # contains (1, 1+h) for some h > 0
    return any(a <= 1 < b for a, b in iv)


def pi(iv):
    return lam(iv) + (c if germ(iv) else 0.0)


def path(p):
    if p <= 1 / 3:
        return norm([(0, 3 * p * c)])
    if p <= 2 / 3:
        return norm([(1, 1 + 1.5 * (p - 1 / 3))]) if p > 1 / 3 else []
    s = p - 2 / 3
    return norm([(1, 1.5), (0, 3 * s), (1.5, 1.5 + 1.5 * s)])


ps = [k / 30000 for k in range(30001)]
m = [pi(path(p)) for p in ps]
jumps = max(abs(m[k + 1] - m[k]) for k in range(len(m) - 1))
print("m(0) =", m[0], " m(1) =", round(m[-1], 9), " (expected 2 + c =", 2 + c, ")")
print("max |m(p_{k+1}) - m(p_k)| on a grid of step 1/30000:", round(jumps, 6), "(continuity)")


def rand_set():
    k = random.randint(1, 4)
    iv = []
    for _ in range(k):
        a = random.uniform(0, 2)
        b = min(2, a + random.uniform(0, 0.6))
        iv.append((a, b))
    if random.random() < 0.3:          # sometimes force the germ
        iv.append((1, 1 + random.uniform(1e-4, 0.05)))
    return norm(iv)


bad_K = 0
for _ in range(2000):
    A = rand_set()
    v = pi(A)
    Si = [x <= v + 1e-12 for x in m]
    Sj = [x >= v - 1e-12 for x in m]
    if not all(a or b for a, b in zip(Si, Sj)):
        bad_K += 1
print("(K) failures over 2000 random test sets:", bad_K)

c13, c12 = path(1 / 3), path(0.5)
print("c_{1/3} =", c13, " c_{1/2} =", c12, " disjoint & both non-null -> crossing:",
      lam(c13) > 0 and lam(c12) > 0 and all(b <= a2 or b2 <= a for a, b in c13 for a2, b2 in c12))

Z = [(0.2, 0.25)]            # pi(Z) = 0.05 < c, no germ
worst = 1e9
for _ in range(2000):
    k = random.randint(2, 60)
    cuts = sorted(random.uniform(0, 2) for _ in range(k - 1))
    pts = [0.0] + cuts + [2.0]
    pieces = [[(pts[r], pts[r + 1])] for r in range(k)]
    worst = min(worst, max(pi(P) for P in pieces))
print("pi(Z) =", pi(Z), "; min over random partitions of max piece value:", round(worst, 6),
      "(> pi(Z): the germ piece always has pi >= c)")
