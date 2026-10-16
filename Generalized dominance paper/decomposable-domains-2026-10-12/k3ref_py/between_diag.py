"""Referee check of k3py/between_lemma.py: the author's diagnosis loop re-seeds rng(1) WITHOUT first drawing the
sample G, so it inspects a different stream of random K than the main loop.  Here we reproduce the main loop
exactly, capture the predicted-false-but-agreeing K, and test it with targeted gambles (-1,-1,L), L up to 1e8,
and with separating gambles in (+,+,-)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "k3py"))
import numpy as np
from scipy.optimize import linprog
from k3_common import Vp, E, in_D, in_U, sample_U, mixed

def in_hull(p, pts):
    n = len(pts)
    A = np.vstack([np.asarray(pts).T, np.ones(n)])
    b = np.concatenate([p, [1.0]])
    r = linprog(np.zeros(n), A_eq=A, b_eq=b, bounds=[(0, None)] * n, method="highs")
    return r.status == 0

rng = np.random.default_rng(1)
G = sample_U(rng, 400000)
G = G[mixed(G)]
sg = np.sign(G)
Gs = G[sg[:, 0] == sg[:, 1]]
L = np.exp(np.linspace(0, 8, 200))
extra = np.stack([-np.ones_like(L), -np.ones_like(L), L], axis=1)
Gs = np.vstack([Gs, extra[in_U(extra)]])
P1 = Gs[:, 0] > 0
bad = []
for trial in range(400):
    k = rng.integers(1, 4)
    pts = []
    for _ in range(k):
        typ = rng.integers(0, 4)
        if typ == 0:
            lam = rng.uniform(); pts.append(lam * E[0] + (1 - lam) * E[1])
        elif typ == 1:
            lam = rng.uniform(); w = rng.dirichlet(np.ones(4))
            pts.append(w[0] * (lam * E[0] + (1 - lam) * E[1]) + w[1:] @ Vp)
        else:
            pts.append(rng.dirichlet(np.ones(3) * 0.7))
    K = np.vstack([Vp] + pts)
    meets_edge = any(abs(p[2]) < 1e-12 for p in pts)
    inside = all(in_hull(p, np.vstack([Vp, E[0], E[1]])) for p in pts)
    pred = meets_edge and inside
    agree = np.all(in_D(Gs, K) == P1)
    if pred != agree:
        bad.append((trial, pred, agree, meets_edge, inside, np.array(pts)))
print("main-loop mismatches:", len(bad))
for trial, pred, agree, me, ins, pts in bad:
    print(" trial", trial, "pred", pred, "agree_on_sample", agree, "meets_edge", me, "inside", ins)
    print("   extra points:\n", np.array2string(pts, precision=8))
    K = np.vstack([Vp, pts])
    # (-1,-1,L): rejected by D_K iff some m in K has L m3 <= m1+m2
    for Lv in [1e3, 1e4, 1e5, 1e6, 1e8]:
        g = np.array([[-1.0, -1.0, Lv]])
        print("   L=%.0e  in U:" % Lv, bool(in_U(g)[0]), " accepted by D_K:", bool(in_D(g, K)[0]),
              " (lemma predicts some such g is accepted iff K misses [e1,e2])")
    # if not inside: separating gamble in (+,+,-)
    if not ins:
        H = np.vstack([Vp, E[0], E[1]])
        for p in pts:
            if not in_hull(p, H):
                # LP: maximise margin min_H h.g - p.g over g in a box, g normalised via shift
                from scipy.optimize import linprog as lp
                # variables g (3), s ; maximise s subject to h.g - p.g >= s for h in H, |g|<=1
                A = np.hstack([-(H - p), np.ones((len(H), 1))])
                r = lp(c=[0, 0, 0, -1], A_ub=A, b_ub=np.zeros(len(H)), bounds=[(-1, 1)] * 3 + [(None, None)], method="highs")
                gsep = r.x[:3]; gsep = gsep - (p @ gsep + 0.5 * r.x[3]) * np.ones(3)
                print("   separating gamble", np.round(gsep, 6), "in U:", bool(in_U(gsep[None])[0]),
                      "accepted by D_K:", bool(in_D(gsep[None], K)[0]), "P1:", gsep[0] > 0)
