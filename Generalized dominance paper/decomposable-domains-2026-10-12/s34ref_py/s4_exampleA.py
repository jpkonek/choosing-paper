"""S34 referee: independent checks of S4 Example A, MP-sharp and the Loop lemma.
Example A: chain coordinate x in [0,1), world 2 = mu-bar (Lebesgue), world 1 additive with density theta(x) = (1-x)^(-1/2).
Closed forms (referee): R(x) := int_0^x theta = 2(1 - sqrt(1-x)); int_t^1 theta = 2 sqrt(1-t).
  tau(c_s) = T(s) = 1 - (1 - sqrt(1-s))^2   (valid for t >= s AND t < s, by cancellation), so T(s) < s iff s > 3/4.
  eta_1(P,1) = 1 - tau(P) = (rho_1(P)/2)^2; bathtub inf{mu(A): c_s <=_1 A} = 1 - T(s).
(1) grid check of the closed forms; (2) (K) on random cut pairs; (3) Loop lemma: for s > 3/4 the interval (T(s), s] is
nonempty, so S4's proof ('(K) at a cut in (s,t)') does not apply there; the conclusion S(t) <= s still holds (repaired
proof by cancellation). (4) MP-sharp (b),(c) on random targets.
Run: python3 -I s4_exampleA.py"""
import numpy as np
rng = np.random.default_rng(5)
n = 400000
x = (np.arange(n) + 0.5) / n
th = (1 - x) ** -0.5
cum = np.concatenate([[0.0], np.cumsum(th) / n])     # rho1(c_{k/n})
tot = cum[-1]
T = lambda s: 1 - (1 - np.sqrt(1 - s)) ** 2
print("(1) tau(c_s): grid vs closed form; T(s) < s ?")
for s in [0.1, 0.5, 0.75, 0.8, 0.9, 0.99]:
    ks = int(round(s * n))
    # c_s <=_1 d_t  iff  rho1(c_s \ d_t) <= rho1(d_t \ c_s)
    best = 0.0
    lo, hi = 0, n - 1
    def ok(kt):
        if kt >= ks: return cum[ks] <= tot - cum[kt]
        return cum[kt] <= tot - cum[ks]
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if ok(mid): lo = mid
        else: hi = mid - 1
    tg = lo / n
    print(f"  s={s:5.2f}: grid tau={tg:.5f}  closed form T(s)={T(s):.5f}  T(s)<s: {T(s) < s}")
print("(2) (K) on 20000 random cut pairs (P <=_1 Q or Q <=_2 P, P in c_b, Q in d_b, finite unions of cells)")
m = 200
xc = (np.arange(m) + 0.5) / m
w1 = ((1 - np.arange(m) / m) ** 0.5 - (1 - np.arange(1, m + 1) / m) ** 0.5) * 2  # exact theta-mass of cells
w2 = np.full(m, 1.0 / m)
bad = 0
for _ in range(20000):
    b = rng.integers(1, m)
    P = (rng.random(m) < rng.random()) & (np.arange(m) < b)
    Q = (rng.random(m) < rng.random()) & (np.arange(m) >= b)
    if not ((w1[P].sum() <= w1[Q].sum()) or (w2[Q].sum() <= w2[P].sum())): bad += 1
print("  (K) failures:", bad)
print("(3) Loop lemma, case t in (T(s), s]:  S(t) = inf{s': d_t <=_2 c_s'} = 1 - t (world 2 = mu-bar); check S(t) <= s")
for s in [0.8, 0.9, 0.99]:
    ts = np.linspace(T(s) + 1e-6, s, 5)
    print(f"  s={s}: (T(s),s] = ({T(s):.4f},{s}] nonempty; S(t) <= s for t in grid: {all(1 - t <= s for t in ts)};"
          f"  c_s <=_1 d_t fails there: {all(not (R := (2*(1-np.sqrt(1-t)) <= 2*np.sqrt(1-s))) for t in ts)}")
print("(4) MP-sharp: random A with c_s <=_1 A has mu(A) >= 1 - T(s) (so d_t <=_2 A for t >= T(s)); and A = d_t' for t' < T(s)")
viol = 0
for _ in range(5000):
    s = rng.uniform(0.05, 0.95)
    k = int(s * m)
    need = w1[:k].sum()
    A = rng.random(m) < rng.uniform(0.01, 0.6)
    A[:k] |= False
    if w1[A].sum() + 1e-12 >= need:          # c_s <=_1 A (additive, overlap cancels)
        if A.sum() / m < 1 - T(k / m) - 2.0 / m: viol += 1
print("  violations of mu(A) >= 1 - T(s):", viol)
print("  eta_1(P_m,1)/m^2 for P_m=[1/2-m,1/2):", [round(((2*(np.sqrt(0.5+mm)-np.sqrt(0.5)))/2)**2/mm**2, 4) for mm in (0.1, 0.01, 0.001)])
