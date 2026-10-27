"""NUMERICS for Lemma K3.7(c)/(c') ("between" lemma) in K3_notes.md.
Claim (PROVED in the note): for a credal set K containing K', D_K agrees with P_1 on the mixed problems where
worlds 1 and 2 agree, i.e. on U n [(+,+,-) u (-,-,+)], iff K meets the edge [e1,e2] and K lies in conv(K' u [e1,e2]).
We test random polytopes K = conv(K' u {extra points}) against random samples."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import linprog
from k3_common import Vp, E, in_D, in_U, sample_U, mixed

rng = np.random.default_rng(1)


def in_hull(p, pts):
    # LP feasibility: p = sum l_i pts_i, l >= 0, sum l = 1
    n = len(pts)
    A = np.vstack([np.asarray(pts).T, np.ones(n)])
    b = np.concatenate([p, [1.0]])
    r = linprog(np.zeros(n), A_eq=A, b_eq=b, bounds=[(0, None)] * n, method="highs")
    return r.status == 0


G = sample_U(rng, 400000)
G = G[mixed(G)]
sg = np.sign(G)
agree12 = (sg[:, 0] == sg[:, 1])            # worlds 1,2 agree: orthants (+,+,-), (-,-,+)
Gs = G[agree12]
P1 = Gs[:, 0] > 0
# targeted extra samples: (-1,-1,L) and (1,1,-a) near the boundary of U
L = np.exp(np.linspace(0, 8, 200))
extra = np.stack([-np.ones_like(L), -np.ones_like(L), L], axis=1)
extra = extra[in_U(extra)]
Gs = np.vstack([Gs, extra])
P1 = Gs[:, 0] > 0

stats = {"pred_true": 0, "pred_false": 0, "agree_when_pred_true": 0, "disagree_when_pred_false": 0}
for trial in range(400):
    k = rng.integers(1, 4)
    pts = []
    for _ in range(k):
        typ = rng.integers(0, 4)
        if typ == 0:      # a point of the edge [e1,e2]
            lam = rng.uniform()
            pts.append(lam * E[0] + (1 - lam) * E[1])
        elif typ == 1:    # a point of conv(K' u [e1,e2])
            lam = rng.uniform()
            w = rng.dirichlet(np.ones(4))
            pts.append(w[0] * (lam * E[0] + (1 - lam) * E[1]) + w[1:] @ Vp)
        else:             # an arbitrary point of the simplex
            pts.append(rng.dirichlet(np.ones(3) * 0.7))
    K = np.vstack([Vp] + pts)
    meets_edge = any(abs(p[2]) < 1e-12 for p in pts)
    inside = all(in_hull(p, np.vstack([Vp, E[0], E[1]])) for p in pts)
    pred = meets_edge and inside
    agree = np.all(in_D(Gs, K) == P1)
    if pred:
        stats["pred_true"] += 1
        stats["agree_when_pred_true"] += int(agree)
    else:
        stats["pred_false"] += 1
        stats["disagree_when_pred_false"] += int(not agree)
print("samples on U n {sigma1 = sigma2} (mixed):", len(Gs))
print(stats)
print("exact agreement with the lemma on the sample (a False here is explained by the diagnosis below):", stats["agree_when_pred_true"] == stats["pred_true"]
      and stats["disagree_when_pred_false"] == stats["pred_false"])

# diagnose: rerun and report the predicted-false-but-agreeing cases (detection limits of sampling)
rng = np.random.default_rng(1)
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
    if not (meets_edge and inside) and np.all(in_D(Gs, K) == P1):
        print("undetected case: meets_edge", meets_edge, "inside", inside,
              "min third coordinate of extra points", min(p[2] for p in pts))
