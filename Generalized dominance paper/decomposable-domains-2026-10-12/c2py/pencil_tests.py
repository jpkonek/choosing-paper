"""CHECKS of Lemma C consequences with the per-prior MILP (pencil.py).
(1) on lambda_b: no admissible K pokes strictly beyond l' or l (Cor C2), but admissible K exist;
(2) precise K: admissible exactly on the C1 sector next to the failing edge (reproduces C1);
(3) a coarse map of the triangle: is SOME admissible K available at every prior?  which kinds?"""
import numpy as np, sys
from dcf import setup, E
from pencil import admissible

eps = float(sys.argv[1]) if len(sys.argv) > 1 else 0.3
kap, v, xp = setup(eps)
u = np.ones(3) / 3
for x, name in [(xp, 'x+')]:
    print(f"eps={eps} {name}={x:.4f} kappa={kap:.4f}")
    # b = world 2 (index 1); failing a = world 1 (index 0) for x+ ; c = world 3 (index 2)
    b, a, c = 1, 0, 2
    wp = np.array([-1.0, 0, kap]); w = np.array([kap, 0, -1.0])   # w' in F_1, w in F_3 (b-crossings)
    print("(1) chord lambda_b, t = distance parameter from e_b")
    for t in [0.02, 0.1, 0.3, 0.6, 0.9]:
        q = (1 - t) * E[b] + t * u
        st0, M0, _ = admissible(q, eps, x, N=4)
        d2 = 1e-3 * t
        stA, MA, _ = admissible(q, eps, x, N=4, extra=[({i: wp[i] for i in range(3)}, -np.inf, -d2)])
        stB, MB, _ = admissible(q, eps, x, N=4, extra=[({i: w[i] for i in range(3)}, -np.inf, -d2)])
        st1, M1, _ = admissible(q, eps, x, N=1)
        print(f"  t={t}: status {st0},{stA},{stB},{st1}; some K {'yes' if M0 is not None else 'NO'};"
              f" K beyond l' {'yes' if MA is not None else 'no'}; beyond l {'yes' if MB is not None else 'no'};"
              f" precise {'yes' if M1 is not None else 'no'}")
    print("(2)/(3) arc around e_b at radius rho; phi=0 failing edge [e_b,e_a], phi=.5 chord, phi=1 edge [e_b,e_c]")
    for rho in [0.05, 0.01]:
        out = []
        for phi in np.linspace(0.02, 0.98, 25):
            q = E[b] + rho * ((1 - phi) * (E[a] - E[b]) + phi * (E[c] - E[b]))
            q = 0.999 * q + 0.001 * u
            s4, M4, _ = admissible(q, eps, x, N=4)
            s1, M1, _ = admissible(q, eps, x, N=1)
            sid, Mid, _ = admissible(q, eps, x, N=1, extra=[({i: 1.0}, q[i] - 1e-12, q[i] + 1e-12) for i in range(2)])
            out.append((round(phi, 2), 'K' if M4 is not None else '-', 'P' if M1 is not None else '-', 'I' if Mid is not None else '-'))
        print("  rho", rho, " ".join(f"{p}:{k}{pp}{i}" for p, k, pp, i in out))
