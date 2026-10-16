"""Independent check of a DCF+ solution: recompute P_{K_q}(+-g) from the witness hulls, compare with the cells,
re-solve each chart LP from scratch, and test (R1),(C) on a FINE tau grid (not the MILP grid).
Also prints the structure of K_q at each prior.  usage: verify_plus.py file.pkl eps"""
import numpy as np, sys, pickle
from scipy.optimize import linprog
from dcf import setup, facet_h, PT, E
from pencil import cvec

d = pickle.load(open(sys.argv[1], 'rb')); eps = float(sys.argv[2])
kap, v, xp = setup(eps); u = np.ones(3) / 3
F, G, Z, K = d['F'], d['G'], d['Z'], d['K']


def Kq(qi):
    return v if qi not in K else K[qi]


def chart_lp(g, cells):
    s = np.sign(g)
    A, b = [], []
    for i in range(3):
        r = np.zeros(6); r[i] = -s[i]; A.append(r); b.append(-1)
        r = np.zeros(6); r[3 + i] = s[i]; A.append(r); b.append(-1)
    for q, z in zip(G, cells):
        c = np.r_[q, 0, 0, 0]; cp = np.r_[0, 0, 0, q]
        if z == 1:
            A += [-c, -(c - cp)]; b += [-1, -1]
        elif z == -1:
            A += [-cp, -(cp - c)]; b += [-1, -1]
        else:
            A += [c, cp]; b += [0, 0]
    res = linprog(np.zeros(6), A_ub=np.array(A), b_ub=np.array(b), bounds=[(None, None)] * 6, method='highs')
    return res.status == 0


bad_cells = 0
for qi in range(len(G)):
    M = Kq(qi)
    for gi, g in enumerate(F):
        Pp, Pm = (M @ g).min(), (M @ -g).min()
        cell = 1 if Pp > 1e-9 else (-1 if Pm > 1e-9 else 0)
        if cell != Z[qi, gi]:
            bad_cells += 1
print("cell mismatches (recomputed from K):", bad_cells)
print("charts realisable from scratch:", sum(chart_lp(g, Z[:, gi]) for gi, g in enumerate(F)), "/", len(F))
viol = 0
for qi, q in enumerate(G):
    if qi not in K:
        continue
    M = K[qi]
    for k in range(3):
        for tau in np.linspace(0, 1, 2001)[1:-1]:
            h = facet_h(k, tau, v); h /= np.linalg.norm(h)
            chi = cvec(k, h, xp) @ q; vals = M @ h
            if chi < -1e-9 and vals.min() > 1e-9:
                viol += 1
            if chi > 1e-9 and vals.min() < -1e-7 and vals.max() > 1e-7:
                viol += 1
print("fine-grid (R1)/(C) violations:", viol)
wp = np.array([-1.0, 0, kap]); w = np.array([kap, 0, -1.0])
for qi, q in enumerate(G):
    M = Kq(qi)
    ext = M[np.unique(np.round(M, 6), axis=0, return_index=True)[1]]
    print(f"q={np.round(q,4)}  #pts={len(ext)}  min K.w'={(M@wp).min():+.4f} min K.w={(M@w).min():+.4f}"
          f"  maxdist(K,q)={np.abs(M-q).sum(1).max():.3f}  K_b range=[{M[:,1].min():.3f},{M[:,1].max():.3f}]")
