"""S1 / plateau_edge.py  --  NUMERICS for Example S1.9 (the edge-system axioms do not force nestedness).

Two-world edge system on R ~ [0,2) with Lebesgue measure (discretised into N cells), worlds i, j additive with
EQUAL densities: psi_i(c) = mu(c), psi_j(c) = mu(R \\ c) (world-i error set c, world-j error set R \\ c).
Selection p in [0,1] -> c_p, continuous in measure, from {} to R, NOT nested:
   p in [0,1/3]:   c_p = [0, 1.5 p)                         grows to [0, 0.5)
   p in [1/3,2/3]: c_p = [s/2, 0.5) u [1, 1 + s/2), s = 3p-1  slides [0,0.5) -> [1,1.5)  (crossing)
   p in [2/3,1]:   c_p = [1, 1.5) u [0, 1.5 s) u [1.5,1.5+0.5 s) ... grows to R
Checks:
 (K)   for random test sets A: psi_i(c_p) <= psi_i(A) or psi_j(c_p) <= psi_j(A)   (always true here)
 (Cl)  sections {p : psi_i(c_p) <= psi_i(A)} and {p : psi_j(c_p) <= psi_j(A)} are closed sub-intervals
       (p -> mu(c_p) is continuous and nondecreasing)
 non-nestedness of c_{1/3} and c_{2/3 - 0}.
Run: python3 -I plateau_edge.py
"""
import numpy as np

N = 4000
x = (np.arange(N) + 0.5) * (2.0 / N)     # cell midpoints in [0,2)
w = 2.0 / N                              # cell measure

def c_of(p):
    if p <= 1/3:
        return x < 1.5 * p
    if p <= 2/3:
        s = 3 * p - 1
        return ((x >= s / 2) & (x < 0.5)) | ((x >= 1.0) & (x < 1.0 + s / 2))
    s = 3 * p - 2
    return ((x >= 1.0) & (x < 1.5)) | (x < 1.0 * s) | ((x >= 1.5) & (x < 1.5 + 0.5 * s)) | \
           ((x >= 0.5) & (x < 0.5 + 0.5 * s))

ps = np.linspace(0, 1, 601)
mass = np.array([c_of(p).sum() * w for p in ps])
print("mu(c_0), mu(c_1):", mass[0], mass[-1])
print("p -> mu(c_p) nondecreasing:", bool(np.all(np.diff(mass) >= -1e-12)))
print("max jump of mu(c_p) on the grid:", float(np.max(np.abs(np.diff(mass)))))

rng = np.random.default_rng(0)
bad_K = 0
bad_cl = 0
for _ in range(300):
    A = rng.random(N) < rng.random()
    mA = A.sum() * w
    s1 = mass <= mA + 1e-12
    s2 = (2.0 - mass) <= (2.0 - mA) + 1e-12
    bad_K += int(np.any(~(s1 | s2)))
    # closed sub-intervals: s1 must be an initial segment, s2 a final segment, on the grid
    def is_initial(b):
        k = np.argmin(b) if not b.all() else len(b)
        return bool(np.all(b[:k]) and not np.any(b[k:]))
    bad_cl += int(not is_initial(s1)) + int(not is_initial(s2[::-1]))
print("(K) violations:", bad_K, "   section-shape violations:", bad_cl)

c1, c2 = c_of(1/3), c_of(2/3 - 1e-9)
print("c_{1/3} \\ c_{2/3-}:", (c1 & ~c2).sum() * w, "  c_{2/3-} \\ c_{1/3}:", (c2 & ~c1).sum() * w,
      " -> crossing (not nested)")
