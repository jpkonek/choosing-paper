"""check78: numerical checks for PP78 (three-ray allocation).  Run: python3 -I -B check78.py > check78.out
Sections:
 1  (2V) on the star; layer-type lemma (Lemma 1.1): L_k(t) contains only points of type (k,-) and (o,+), o != k.
 2  Gamma-shapes: V(T -> B_{k,t}) = p (3 e_k - 1) and V(B_{k,s} -> B_{k,t}) = (p(t)-p(s)) (3 e_k - 1).
 3  Path monotonicity (Lemma 3.2): on the path P_w = ray w u ray w-1, moving up the path coordinate
    improves every changed odd-(w-1) point at world w-1 and worsens every changed odd-w point at world w.
 4  Dangerous cross-ray swaps exist (odd-n points on both sides) and their member carriers lie on ONE ray.
 5  Relay test: null records carried by interior members of all three rays exist (T-carried), and no
    star member carries their reverse.
 6  Margin rule: every Gamma-shape lies in exactly one closed class; endorsement margin on random vectors.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lib78 import *

G = sample(int(os.environ.get('NS', '300000')))
g = Geo(G)
TS = [0.01, 0.02, 0.03, 0.04, 0.05]
print('N =', g.N)
mem = {(k, t): g.member(k, t) for k in range(3) for t in TS}

print('\n[1] (2V) violations and layer types')
bad_types = 0
for (k, t), B in mem.items():
    L = B != g.T
    v2 = g.viol2V(B)
    wrong = L & (((g.o == k) & (g.sigma == 1)) | ((g.o != k) & (g.sigma == -1)) | (g.o < 0))
    bad_types += int(wrong.sum())
    if t in (0.01, 0.05):
        print('  ray %d t=%.2f: (2V) viol %d; layer pts %d; wrong-type pts %d' % (k + 1, t, v2, L.sum(), wrong.sum()))
print('  total wrong-type layer points over all 15 members:', bad_types)

print('\n[2] Gamma-shapes (exact up to sampling; sample is S3-symmetric)')
for k in range(3):
    for t in (0.02, 0.05):
        V = g.V(g.T, mem[(k, t)])
        p = V[k] / 2
        dev = np.abs(V - p * (3 * np.eye(3)[k] - 1)).max()
        print('  V(T->B_%d,%.2f) = %s ; p = %.5f ; max deviation from p(3e_k-1): %.1e' % (k + 1, t, np.round(V, 5), p, dev))
    V = g.V(mem[(k, 0.02)], mem[(k, 0.05)])
    p = V[k] / 2
    print('  V(B_%d,.02 -> B_%d,.05) = %s ; deviation %.1e' % (k + 1, k + 1, np.round(V, 5), np.abs(V - p * (3 * np.eye(3)[k] - 1)).max()))

print('\n[3] path monotonicity')
def path(w):  # list of (x, model) along P_w = ray (w-1) [x<0] u {T} u ray w [x>0]; w is 0-based
    pm = (w - 1) % 3
    out = [(-t, mem[(pm, t)]) for t in reversed(TS)] + [(0.0, g.T)] + [(t, mem[(w, t)]) for t in TS]
    return out
viol = 0; checked = 0
for w in range(3):
    pm = (w - 1) % 3
    P = path(w)
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            A, B = P[i][1], P[j][1]          # x_B > x_A
            D = A != B
            d = (B != 0).astype(int) - (A != 0).astype(int)
            imp = np.zeros(g.N, bool)
            # B improves the odd world at g  <=>  (S->h and Cor={o}) or (h->S and Wr={o})
            imp = D & (((d == 1) & g.co) | ((d == -1) & ~g.co))
            v1 = D & (g.o == pm) & ~imp       # odd-(w-1) point worsened: violation
            v2 = D & (g.o == w) & imp         # odd-w point improved: violation
            viol += int(v1.sum() + v2.sum()); checked += int(D.sum())
print('  pairs on the three paths: changed points checked %d, violations %d' % (checked, viol))

print('\n[4] dangerous cross-ray swaps and their carriers')
for (k, m) in [(0, 1), (1, 2), (2, 0), (0, 2)]:
    n = 3 - k - m
    Bk, Bm = mem[(k, 0.03)], mem[(m, 0.03)]
    P1 = (Bk != g.T) & (Bm == g.T) & (g.o == n)
    P2 = (Bm != g.T) & (Bk == g.T) & (g.o == n)
    print('  k=%d m=%d n=%d: odd-n mass of L_k\\L_m = %.5f, of L_m\\L_k = %.5f' % (k + 1, m + 1, n + 1, g.mass(P1), g.mass(P2)))
    # balanced F: P1 plus a radial prefix of P2 of equal mass (or vice versa)
    small, large = (P1, P2) if g.mass(P1) <= g.mass(P2) else (P2, P1)
    idx = np.nonzero(large)[0]; idx = idx[np.argsort(g.nrm[idx])]
    cs = np.cumsum(g.nrm[idx]); kk = int(np.searchsorted(cs, g.mass(small) * g.N))
    F = small.copy(); F[idx[:kk]] = True
    X = Bk.copy(); X[F] = Bm[F]
    VF = g.V(Bk, X)
    carriers = [('T', 0)] if (g.T[F] == Bk[F]).all() else []
    carriers += [('B%d,%.2f' % (kk2 + 1, t), 1) for (kk2, t), B in mem.items() if (B[F] == Bk[F]).all()]
    rev = [('B%d,%.2f' % (kk2 + 1, t)) for (kk2, t), B in mem.items() if (B[F] == Bm[F]).all()]
    print('    V(r) = %s (null up to sampling); carriers of r: %s; members carrying r^-1: %s'
          % (np.round(VF, 6), [c[0] for c in carriers], rev))

print('\n[5] relay test: null records carried by interior members of all three rays')
Lall = np.zeros(g.N, bool)
for k in range(3):
    Lall |= mem[(k, 0.05)] != g.T
anyR = (g.o >= 0)
# R(S0) proxy: points where some star member differs, or near T's boundary; we use points where T and
# a moderately shifted member differ (x = 0.15 delta_k), outside the t1 = 0.05 layers
Rp = np.zeros(g.N, bool)
for k in range(3):
    Rp |= advice(G, 0.15 * DELTA[k]) != g.T
Q = Rp & ~Lall & anyR
for o in range(3):
    print('  odd-%d points outside all t1-layers (inside the 0.15-layers): sigma=+1 mass %.5f, sigma=-1 mass %.5f'
          % (o + 1, g.mass(Q & (g.o == o) & (g.sigma == 1)), g.mass(Q & (g.o == o) & (g.sigma == -1))))
# build F: in each odd world take equal masses of (+) and (-) points -> c = 0, null; carried by T and all members
F = np.zeros(g.N, bool)
for o in range(3):
    Pp = np.nonzero(Q & (g.o == o) & (g.sigma == 1))[0]; Pm = np.nonzero(Q & (g.o == o) & (g.sigma == -1))[0]
    a, b = (Pp, Pm) if g.nrm[Pp].sum() <= g.nrm[Pm].sum() else (Pm, Pp)
    b = b[np.argsort(g.nrm[b])]; cs = np.cumsum(g.nrm[b]); kk = int(np.searchsorted(cs, g.nrm[a].sum()))
    F[a] = True; F[b[:kk]] = True
X = g.T.copy(); X[F] = np.where(g.T[F] == 0, g.h[F], 0)
print('  F: %d points; V(T -> T[F flipped]) = %s' % (F.sum(), np.round(g.V(g.T, X), 6)))
ncar = sum(int((B[F] == g.T[F]).all()) for B in mem.values())
nrev = sum(int((B[F] == X[F]).all()) for B in mem.values())
print('  members (15 sampled) carrying r: %d ; members carrying r^-1: %d' % (ncar, nrev))

print('\n[6] margin rule (cyclic, kappa = 1/4)')
for k in range(3):
    e = np.eye(3)[k]
    print('  inward shape 3e_%d-1 -> classes %s ; outward shape 1-3e_%d -> classes %s'
          % (k + 1, margin_rule_classes(3 * e - 1), k + 1, margin_rule_classes(1 - 3 * e)))
rng = np.random.default_rng(1)
worst = 9.0; cover_fail = 0
for _ in range(200000):
    v = rng.standard_normal(3)
    if v.sum() < 0:
        continue
    cl = margin_rule_classes(v)
    if not cl:
        cover_fail += 1; continue
    nv = np.abs(v).max()
    worst = min(worst, min(v[w - 1] for w in cl) / nv)
print('  random v with sum >= 0: uncovered %d ; min over classes of v_w/|v| = %.4f (bound 1/2 - kappa = 0.25)' % (cover_fail, worst))
