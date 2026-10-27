#!/usr/bin/env python3
"""P2 / holonomy_signs.py (NUMERICS): strict-sign margins of saved facet maps:
min over relint points and coordinates l with |h_l| >= 1e-3|h| of c_l*sign(h_l)/|c|, and the value at the corners."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import holonomy_pl as H
import holonomy_check as Ck
for fname, mode in [("holonomy_pl_best.npy", "pl"), ("holonomy_onekink_F1_eps0.3.npy", "onekink1"), ("holonomy_onekink_F2_eps0.3.npy", "onekink2")]:
    P = Ck.load(fname, mode)
    worst = np.inf
    for k in range(3):
        for t in np.linspace(0, 1, 20001)[1:-1]:
            h = H.pt(k, t); c = H.chart(k, h, P)
            for l in range(3):
                if abs(h[l]) >= 1e-3 * np.linalg.norm(h):
                    worst = min(worst, c[l] * np.sign(h[l]) / np.linalg.norm(c))
        cr = [H.chart(k, H.FAC[k]['ri'], P), H.chart(k, H.FAC[k]['rj'], P)]
        cs = [np.sign(c) for c in cr]
    print(fname, "strict-sign margin (relint):", round(worst, 6))
