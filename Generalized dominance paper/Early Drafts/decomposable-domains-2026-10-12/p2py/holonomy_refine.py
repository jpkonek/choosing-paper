#!/usr/bin/env python3
"""P2 / holonomy_refine.py (NUMERICS): box margin of saved solutions on facet grids refined
geometrically (down to 1e-9) around every crossing parameter and both corners; also the linear case.
Usage: python3 -I holonomy_refine.py eps file.npy mode"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import holonomy_pl as H
import holonomy_check as Ck
eps, fname, mode = sys.argv[1], sys.argv[2], sys.argv[3]
P = Ck.load(fname, mode)
pts = set(np.linspace(0, 1, 6001)[1:-1])
cr = set()
for k in range(3):
    for c in range(3):
        if c == k: continue
        cr.add(H.cross_tau(k, c))
cr |= {0.0, 1.0}
g = np.geomspace(1e-9, 0.05, 400)
for c in cr:
    for d in g:
        for s in (-1, 1):
            t = c + s * d
            if 0 < t < 1: pts.add(t)
tau = np.array(sorted(pts))
bm, arg = H.box_margin(P, tau=tau)
print(f"eps={eps} {fname}: refined grid ({len(tau)} pts/facet) box margin = {bm:.3e}  worst {arg}")
x = ((H.KAP + 1) + np.sqrt((H.KAP + 1) ** 2 - 4)) / 2
print(f"   linear x+ on same grid: box margin = {H.box_margin(H.linear_params([x,x,x]), tau=tau)[0]:.3e}")
