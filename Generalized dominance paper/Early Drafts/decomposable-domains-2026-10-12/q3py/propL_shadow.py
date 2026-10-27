"""Q3 §2 NUMERICS: a strictly positive additive shadow whose Bayes model is T1 at EVERY weight of
Q_delta = {t : min_i t_i >= delta}, so that all incoherent Bayes models (forced to exist on a
non-null set of weights by Theorem M0closed(a)) sit in the collar {min_i t_i < delta}.

Shadow: c_i(g) = sign(g_i) * w_i(g), with w_i = L if (g in D_T1 and g_i > 0) or (g not in D_T1 and
g_i < 0), and w_i = 1 otherwise.  L = 2/delta + 1.  Densities rho_i = w_i in {1, L}: bounded, > 0.

Checks:
 (A) for random t in Q_delta and random g in U: [t.c(g) > 0] == [g in D_T1]   (T1 = B_t on Q_delta);
 (B) for random t in the collar: search for robust convexity failures of B_t
     (g, g' in B_t, g+g' in U \\ B_t, stable under small perturbations) = incoherence witnesses;
 (C) report the distribution of min_i t_i over weights with a witness.
Run: python3 -I propL_shadow.py
"""
import numpy as np

rng = np.random.default_rng(20261015)
eps, s, delta = 0.3, 0.9, 0.1
L = 2.0 / delta + 1.0
c0 = (1 - eps) / 3
u = np.ones(3) / 3
V = np.array([c0 * np.ones(3) + eps * np.eye(3)[k] for k in range(3)])      # vertices of T1
Vp = np.array([u + s * (V[k] - u) for k in range(3)])                         # vertices of K'


def in_DT(g):
    return np.all(g @ V.T > 0, axis=-1)


def in_U(g):
    return np.all(g @ Vp.T > 0, axis=-1)


def cfield(g):
    dt = in_DT(g)[..., None]
    pos = g > 0
    w = np.where((dt & pos) | (~dt & ~pos), L, 1.0)
    return np.sign(g) * w


def in_B(t, g):
    return in_U(g) & (cfield(g) @ t > 0)


def sample_U(n):
    out = []
    while sum(len(o) for o in out) < n:
        g = rng.normal(size=(4 * n, 3))
        g /= np.linalg.norm(g, axis=1, keepdims=True)
        out.append(g[in_U(g)])
    return np.concatenate(out)[:n]


def sample_simplex(n):
    return rng.dirichlet(np.ones(3), size=n)


# (A)
G = sample_U(200000)
mixed = (G.max(axis=1) > 0) & (G.min(axis=1) < 0)
T = sample_simplex(20000)
TQ = T[T.min(axis=1) >= delta][:200]
bad = 0
for t in TQ:
    bad += int(np.sum(in_B(t, G) != in_DT(G)))
print(f"(A) {len(TQ)} weights in Q_delta x {len(G)} gambles: disagreements B_t vs D_T1 = {bad}")


# (B) robust witnesses
def robust(t, g, want_in, r=2e-3, k=12):
    P = g + r * rng.normal(size=(k, 3))
    inB = in_B(t, P)
    inU = in_U(P)
    if want_in:
        return bool(np.all(inB))
    return bool(np.all(inU & ~inB))


TC = T[T.min(axis=1) < delta][:400]
found = []
for t in TC:
    B = G[in_B(t, G) & mixed]
    if len(B) < 2:
        continue
    for _ in range(400):
        i, j = rng.integers(len(B), size=2)
        a = rng.uniform(0.2, 5.0)
        g, h = B[i], a * B[j]
        f = g + h
        if in_U(f[None])[0] and not in_B(t, f[None])[0]:
            if robust(t, g, True) and robust(t, h, True) and robust(t, f, False):
                found.append((t, g, h))
                break
print(f"(B) collar weights tested: {len(TC)}; weights with a robust incoherence witness: {len(found)}")
mins = np.array([w[0].min() for w in found])
if len(mins):
    print(f"(C) min_i t_i over witnessed weights: min {mins.min():.4f}, median {np.median(mins):.4f}, "
          f"max {mins.max():.4f}  (all < delta = {delta})")
    t, g, h = found[0]
    print("    example: t =", np.round(t, 4), " g =", np.round(g, 4), " h =", np.round(h, 4),
          " g+h =", np.round(g + h, 4), " in D_T1:", in_DT(np.array([g, h, g + h])))


# (D) exact description: B_t = D_T1 iff min_i t_i > 1/(L+1); otherwise B_t misses
#     S_k = D_T1 ∩ {g_k > 0 > g_i, g_j} for the k with t_k = min t (so it is far from T1).
thr = 1.0 / (L + 1.0)
inT = in_DT(G)
S = [inT & (G[:, k] > 0) & (np.delete(G, k, axis=1) < 0).all(axis=1) for k in range(3)]
fracS = [s_.mean() for s_ in S]
print(f"(D) threshold 1/(L+1) = {thr:.5f}; mu(S_k)/mu(U) (MC) = {np.round(fracS, 4)}")
T2 = sample_simplex(3000)
viol_in, viol_out, dmin = 0, 0, 1.0
for t in T2:
    Bt = in_B(t, G)
    d = np.mean(Bt != inT)
    if t.min() > thr + 1e-9:
        viol_in += int(d > 0)
    elif t.min() < thr - 1e-9:
        k = int(np.argmin(t))
        viol_out += int(np.any(Bt & S[k]))
        dmin = min(dmin, d)
print(f"    weights with min t > 1/(L+1) and B_t != D_T1: {viol_in};  weights with min t < 1/(L+1) "
      f"whose B_t meets S_argmin: {viol_out};  min distance mu(B_t Δ T1)/mu(U) there = {dmin:.4f}")
