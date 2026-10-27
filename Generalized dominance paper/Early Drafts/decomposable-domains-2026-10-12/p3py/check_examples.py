"""P3 numerics (illustration only; no proof in P3_notes.md depends on this file).

Setting: n = 3, eps = 0.3, T1 = (1-eps)u + eps*Delta, K' = u + s(T1-u), s = 0.9, U = D_{K'}.
Brier family B_q = U ∩ {q.h > 0} (Bayes family of psi_i(X) = int_{E_i X} rho(h)|h_i| dmu, any common rho > 0).

Example 1 (P3.5): A = small balls around a, a'; s = 1_A (the exchange "remove A").
Example 2 (P3.6): base p0 not in K', r_k = p0 + delta_k (e1 - p0), X = B_{p0} ∪ W.
Run: python3 -I check_examples.py
"""
import numpy as np

rng = np.random.default_rng(0)
eps, s = 0.3, 0.9
u = np.ones(3) / 3
E = np.eye(3)
T1v = np.array([(1 - eps) * u + eps * E[k] for k in range(3)])     # vertices of T1
Kpv = np.array([u + s * (v - u) for v in T1v])                      # vertices of K'


def lower(Kv, h):
    """lower prevision min_{m in conv Kv} m.h for an array of gambles h (N,3)."""
    return np.min(h @ Kv.T, axis=-1)


def inU(h):
    return lower(Kpv, h) > 0


def inB(q, h):
    return inU(h) & (h @ q > 0)


print("=== Example 1: transported reservation ===")
a = np.array([-0.1, 1.0, 1.0])
ap = np.array([1.0, -0.1, -0.1])
for name, g in [("a", a), ("a'", ap)]:
    print(f"{name}={g}: P_T1={lower(T1v, g[None])[0]:.4f}  P_K'={lower(Kpv, g[None])[0]:.4f}  "
          f"u.g={g @ u:.4f}  r.g (r=(1/2,1/2,0))={g @ np.array([.5, .5, 0]):.4f}")
# Comp(1_A) = {q : q.a > 0 and q.a' > 0} (A inside U; B_q = U ∩ {q.h>0}); faces met by Comp:
faces = {"e1": [0], "e2": [1], "e3": [2], "[e1,e2]": [0, 1], "[e1,e3]": [0, 2], "[e2,e3]": [1, 2]}
for nm, idx in faces.items():
    if len(idx) == 1:
        qs = E[idx[0]][None]
    else:
        t = np.linspace(0.001, 0.999, 999)[:, None]
        qs = t * E[idx[0]] + (1 - t) * E[idx[1]]
    ok = (qs @ a > 0) & (qs @ ap > 0)
    print(f"  Comp(1_A) meets relint {nm}: {bool(ok.any())}")
# Ball radius: check balls of radius rad around a, a' stay inside B_u ∩ B_r and in D_T1
rad = 0.05
for name, g in [("a", a), ("a'", ap)]:
    pts = g + rad * rng.uniform(-1, 1, size=(20000, 3))
    print(f"  ball({name},{rad}) inside D_T1: {bool((lower(T1v, pts) > 0).all())}, "
          f"inside B_r: {bool((pts @ np.array([.5, .5, 0]) > 0).all())}")
# world signs on A: s*sgn_i takes both signs at every world -> no world accepts 1_A by background
for i in range(3):
    print(f"  world {i+1}: sgn(a_i)={np.sign(a[i]):+.0f}, sgn(a'_i)={np.sign(ap[i]):+.0f}")
# In the Brier system itself, 1_A is accepted at world i iff int_A h_i >= 0 (equal balls):
print("  Brier: int_A h_i ∝", a + ap, "-> accepted at all three worlds in Psi (so the reservations are bad choices)")

print("\n=== Example 2: limit step (L5) ===")
p0 = np.array([0.6, 0.2, 0.2])
print("p0 in K'? (needs all coords >= (1-0.27)/3 = %.4f):" % ((1 - 0.27) / 3), bool((p0 >= (1 - 0.27) / 3).all()))
delta1 = 0.05
r1 = p0 + delta1 * (E[0] - p0)
N = 2_000_000
H = rng.normal(size=(N, 3))
H = H[inU(H)]
print("sampled gambles in U:", len(H))
# W' = U ∩ {h1 < 0} ∩ {r1.h > 0}: accepted by B_{p0} and by every B_{r_k}; X = B_{p0} minus W'
Wp = H[(H[:, 0] < 0) & (H @ r1 > 0)]
print("W' = U ∩ {h1<0} ∩ {r1.h>0}: fraction %.4f (non-null); all in B_p0: %s"
      % (len(Wp) / len(H), bool((Wp @ p0 > 0).all())))
eta = 0.2
w = np.abs(Wp[:, 0]).sum() / len(H)
for dk in [0.05, 0.02, 0.01, 0.005, 0.002]:
    rk = p0 + dk * (E[0] - p0)
    shp = H[(H @ p0 <= 0) & (H @ rk > 0)]          # B_{rk} \ B_{p0}
    shm = H[(H @ p0 > 0) & (H @ rk <= 0)]          # B_{p0} \ B_{rk}
    nrm = np.linalg.norm(shm, axis=1)
    R = shm[shm[:, 0] <= -eta * nrm]
    ak = np.abs(R[:, 0]).sum() / len(H)
    rest = (shp[:, 0].sum() - shm[shm[:, 0] > -eta * nrm][:, 0].sum()) / len(H)
    print(f"  delta={dk}: |B_rk minus B_p0|={len(shp)}, a_k={ak:.2e} (removed part with h1<=-eta|h|), "
          f"rest of world-1 gain={rest:+.2e}, M needed={(w - min(rest, 0)) / ak if ak > 0 else float('inf'):.1f}")
print("  w = int_W' |h1| =", f"{w:.2e}")
print("  world-1 gain of moving p0 -> r_k with common density rho: G_k = M a_k + rest_k; stage m admissible if G_k >= w, k<=m")
