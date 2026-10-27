"""Step 6 of C2_notes section 5: two pinned caps cannot coexist.
Caps (x+): at e_b, sigma_b(q)=nu(W_b q) with W_b = kappa off b, 1 at b, on the sector between the failing edge and
the line through e_b with direction (a-component 1, c-component 1/x).  A gamble g whose line g^perp meets both image
caps sigma_1(O_1), sigma_2(O_2) must have d-vector proportional to W_1 g and to W_2 g.  We exhibit an open set of
such g and print the angle between W_1 g and W_2 g (nonzero => contradiction)."""
import numpy as np
from dcf import setup, E

for eps in (0.3, 0.6):
    kap, v, xp = setup(eps)
    tab = {1: 0, 2: 1, 0: 2}            # x+: failing a for each b (0-based)
    W = {b: np.where(np.arange(3) == b, 1.0, kap) for b in range(3)}
    def cap_point(b, rho, frac):
        a = tab[b]; c = 3 - a - b
        # direction in the cap: c-share/a-share = frac * (1/x)  (frac<1: strictly inside the sector)
        d = (E[a] - E[b]) + frac / xp * (E[c] - E[b])
        return E[b] + rho * d / np.abs(d).sum()
    rng = np.random.default_rng(0)
    angs = []
    for _ in range(2000):
        q1 = cap_point(0, 10 ** rng.uniform(-3, -1.5), rng.uniform(0.1, 0.9))   # in O_1 (near e_1)
        q2 = cap_point(1, 10 ** rng.uniform(-3, -1.5), rng.uniform(0.1, 0.9))   # in O_2 (near e_2)
        m1 = W[0] * q1 / (W[0] @ q1); m2 = W[1] * q2 / (W[1] @ q2)            # image points
        g = np.cross(m1, m2)                                                  # g^perp passes through m1, m2
        g = g / np.linalg.norm(g)
        assert g.max() > 0 > g.min()                                          # mixed
        a1, a2 = W[0] * g, W[1] * g
        angs.append(np.degrees(np.arccos(abs(a1 @ a2) / np.linalg.norm(a1) / np.linalg.norm(a2))))
    print(f"eps={eps}: kappa={kap:.4f}; angle between W_1 g and W_2 g over 2000 double-cap gambles:"
          f" min {min(angs):.3f} deg, median {np.median(angs):.3f} deg")
