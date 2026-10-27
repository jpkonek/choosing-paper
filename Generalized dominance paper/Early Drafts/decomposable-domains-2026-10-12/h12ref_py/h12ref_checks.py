"""Referee checks for H1/H2 (NUMERICS only; no verdict rests on them). Run: python3 -I h12ref_checks.py

(1) H1.0(b) pointwise identity and the bound |t.c| <= t2 rho2 + t3 rho3 where B_t errs at world 1,
    with a NON-integrable rho1 (blows up like 1/dist at the dU collar inside {h1<0}).
(2) H1.0(b) finiteness: Phi(Y) <= sum_k t_k rho_k(E_k Y) pointwise (the bound the note omits).
(3) H2 Sec. 5.1 geometry: in the dU collar, T1 rejects; signs of A=(+,+,-), B=(-,+,+) pieces; arrows 1->3, 3->1.
(4) H2.4 (K): exact check of the base-cone (R0/R+) acceptance at world 1 (tails in x) or world 2 (heads in x)
    for random unions of intervals A, random n >= 0, interior cuts b (piecewise-linear, checked at breakpoints).
"""
import numpy as np
from fractions import Fraction as Fr
rng = np.random.default_rng(151015)
eps, s = 0.3, 0.9
u = np.ones(3) / 3
V = np.array([(1 - eps) * u + eps * np.eye(3)[k] for k in range(3)])
Vp = np.array([u + s * (v - u) for v in V])
P = lambda K, g: (g @ K.T).min(axis=1)

g = rng.standard_normal((600000, 3)); g = g[P(Vp, g) > 0]
sig = np.sign(g); inT = P(V, g) > 0
rel = P(Vp, g) / np.linalg.norm(g, axis=1)
rho = np.ones_like(g)
rho[:, 0] = np.where(g[:, 0] < 0, 1.0 + 1.0 / np.maximum(rel, 1e-12), 1.0)     # non-integrable at dU, h1<0
c = rho * sig
fail1 = fail2 = fail3 = 0
for _ in range(200):
    t = rng.dirichlet(np.ones(3)); tc = c @ t; B = tc > 0
    wrong1 = (B != (sig[:, 0] > 0))
    fail1 += int(np.sum(np.abs(tc[wrong1]) > (t[1] * rho[wrong1, 1] + t[2] * rho[wrong1, 2]) * (1 + 1e-12)))
    Y = rng.random(len(g)) < 0.5; Y |= (g > 0).all(axis=1); Yp = rng.random(len(g)) < 0.5; Yp |= (g > 0).all(axis=1)
    E = lambda X: X[:, None] != (sig > 0)                                  # error indicator matrix (n,3)
    lhs = (np.where(Y != B, 1, 0) - np.where(Yp != B, 1, 0)) * np.abs(tc)
    rhs = ((E(Y).astype(int) - E(Yp).astype(int)) * rho) @ t
    fail2 += int(np.sum(np.abs(lhs - rhs) > 1e-9 * (1 + np.abs(rhs))))
    phiY = np.where(Y != B, np.abs(tc), 0.0)
    fail3 += int(np.sum(phiY > (E(Y) * rho) @ t * (1 + 1e-12) + 1e-12))
print(f"(1) |t.c| <= t2rho2+t3rho3 where B_t wrong at 1: failures {fail1}")
print(f"(1) H1.0(b) pointwise identity: failures {fail2}")
print(f"(2) pointwise Phi-integrand <= sum_k t_k rho_k 1_[E_k Y]: failures {fail3}")

coll = rel < 1e-2
print(f"(3) collar samples {coll.sum()}, T1 accepts any: {bool(inT[coll].any())}")
A = coll & (sig == np.array([1, 1, -1])).all(axis=1); Bb = coll & (sig == np.array([-1, 1, 1])).all(axis=1)
print(f"    A=(+,+,-) collar samples {A.sum()}: T1 wrong at 1,2 / right at 3; B=(-,+,+) {Bb.sum()}: wrong at 2,3 / right at 1")

# (4) H2.4 (K) with exact rationals. lambda on M = Lebesgue on [0,1) in x. Sets = finite unions of intervals.
def measure(iv, lo, hi):
    return sum(max(Fr(0), min(b, hi) - max(a, lo)) for a, b in iv)
def rand_union(k):
    pts = sorted(set(Fr(int(x), 997) for x in rng.integers(0, 998, 2 * k)))
    if len(pts) % 2: pts = pts[:-1]
    return [(pts[i], pts[i + 1]) for i in range(0, len(pts), 2)]
fails = tests = only1 = only2 = 0
for _ in range(1500):
    Aset = rand_union(int(rng.integers(1, 6)))
    b = Fr(int(rng.integers(1, 997)), 997)
    n = Fr(0) if rng.random() < 0.5 else Fr(int(rng.integers(1, 60)), 997)
    a, a2 = Fr(1, 4), Fr(1, 4)          # design parameters a (world 1) and a' (world 2)
    brk = sorted(set([Fr(0), Fr(1), b, a, 1 - a2] + [p for iv in Aset for p in iv]))
    # delta1 = 1_Q - 1_P + n*[N+], P = c_b \ A = [0,b)\A, Q = A\c_b ;  tails tau(t) = int_{x>=t} delta1 + n
    def tail1(t):
        Pmass = (b - t) - measure(Aset, t, b) if t < b else Fr(0)     # lambda(P cap [t,1))
        return measure(Aset, max(t, b), Fr(1)) - Pmass + n
    def head2(uu):    # world 2 mirrored: heads int_{x<=u} delta2 + n, delta2 = 1_P - 1_Q + n
        Pm = (min(uu, b) - measure(Aset, 0, min(uu, b)))
        Qm = measure(Aset, b, uu) if uu > b else Fr(0)
        return Pm - Qm + n
    if n > 0:
        acc1 = all(tail1(t) >= 0 for t in brk if t >= a)
        acc2 = all(head2(uu) >= 0 for uu in brk if uu <= 1 - a2)
    else:
        acc1 = all(tail1(t) >= 0 for t in brk)            # base cone: tails >=0, >=0 near 1 automatic (b<1)
        acc2 = all(head2(uu) >= 0 for uu in brk)          # mirrored base cone: heads >=0, >=0 near 0 (b>0)
    tests += 1; fails += int(not (acc1 or acc2)); only1 += int(acc1 and not acc2); only2 += int(acc2 and not acc1)
print(f"(4) H2.4 (K) via base cones at an interior cut: tests {tests}, failures {fails} (non-trivial: accepted only at w1 {only1}, only at w2 {only2})")
