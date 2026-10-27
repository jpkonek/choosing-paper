"""(R1) test for the two candidate cap maps sigma = nu(W q) of pin_caps.py, at priors near the failing edge.
(R1): c_k(h_k(tau)).q < 0  =>  sigma(q).h_k(tau) < 0 , all facets k, dense tau.   Also Lemma C' is automatic for
singletons.  Reports, per vertex and candidate, the largest angular parameter phi (phi=0 failing edge, phi=1/2 chord)
up to which (R1) holds, against the predicted boundary phi* = r/(1+r), r = min(x,1/x)."""
import numpy as np, sys
from dcf import setup, facet_h, E
from pencil import cvec

eps = float(sys.argv[1]) if len(sys.argv) > 1 else 0.3
kap, v, xp = setup(eps)
taus = np.linspace(0, 1, 4001)[1:-1]
Hs = [np.array([facet_h(k, t, v) for t in taus]) for k in range(3)]


def r1_ok(q, sig, x):
    # chi and sigma.h are affine in tau: (R1) fails iff some tau in (0,1) has chi<0<=S.  Exact test: the set
    # {chi<0} is an interval with endpoint at the root of chi; S is affine; check endpoints and the root of S.
    for k in range(3):
        h0, h1 = facet_h(k, 0.0, v), facet_h(k, 1.0, v)
        C0, C1 = cvec(k, h0, x) @ q, cvec(k, h1, x) @ q
        S0, S1 = sig @ h0, sig @ h1
        cand = [1e-12, 1 - 1e-12]
        for (p0, p1) in [(C0, C1), (S0, S1)]:
            if abs(p1 - p0) > 1e-18:
                t = p0 / (p0 - p1)
                for dlt in (-1e-12, 0.0, 1e-12):
                    if 0 < t + dlt < 1:
                        cand.append(t + dlt)
        for t in cand:
            C = (1 - t) * C0 + t * C1; S = (1 - t) * S0 + t * S1
            if C < -1e-15 * abs(C1 - C0) and S >= 0:
                return False
    return True


tab = {'x+': {1: 0, 2: 1, 0: 2}, 'x-': {0: 1, 1: 2, 2: 0}}
for xname, x in [('x+', xp), ('x-', 1 / xp)]:
    for b in range(3):
        a = tab[xname][b]; c = 3 - a - b
        WI = np.ones(3); WI[a], WI[c] = xp, 1 / xp
        WII = np.ones(3); WII[a], WII[c] = kap, kap
        rstar = min(x, 1 / x); phistar = rstar / (1 + rstar)
        out = []
        for name, W in [('I (conic)', WI), ('II (line)', WII), ('identity', np.ones(3))]:
            row = []
            for rho in (1e-2, 1e-3):
                ok = []
                for phi in np.linspace(0.0, 0.6, 121)[1:]:
                    q = E[b] + rho * ((1 - phi) * (E[a] - E[b]) + phi * (E[c] - E[b]))
                    sig = W * q / (W @ q)
                    ok.append((phi, r1_ok(q, sig, x)))
                good = [p for p, o in ok if o]
                # largest phi such that all smaller sampled phi are ok
                mx = 0.0
                for p, o in ok:
                    if not o:
                        break
                    mx = p
                row.append((rho, round(mx, 3), len(good)))
            out.append((name, row))
        print(f"eps={eps} {xname} b={b+1} a={a+1} c={c+1}: predicted phi*={phistar:.4f}")
        for name, row in out:
            print("    ", name, " (rho, phi_max with R1 on [0,phi_max], #ok of 120):", row)
