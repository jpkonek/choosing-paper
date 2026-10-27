"""N27 (ii): tie thresholds for T1 (evidence only; the closed forms are proved in N5/N6/N7).

For each eps:
  theta_x  = sup_{h in F_k \\ 0} h_i/||h||   (i a crossing coordinate of F_k): threshold for (X_ik)
             -> N5 Thm 3.3 facet clause, hence UVN(a) at every relint facet point with h_l > 0.
  Theta_NT = phi_i(corner ray r) (Euclidean), the corner clause threshold of N7 (not needed in N27).
  phi_j(w) = positive-coordinate ratio at a crossing w (the point where Lemma 4.1/nopin needs UVN(a) for world j).
  For a grid of theta: fraction of the facet parameter interval (0,1) at which SOME positive coordinate of h(tau)
  is in its band (so that, without N5 Thm 3.3, UVN(a) there is not supplied by strictness).
"""
import numpy as np

def t1(eps):
    kap = (1 + 2 * eps) / (1 - eps)
    r12 = np.array([-1.0, -1.0, kap + 1])
    r31 = np.array([-1.0, kap + 1, -1.0])
    return kap, r12, r31

def facet(eps, tau):
    kap, r, rp = t1(eps)
    return (1 - tau)[:, None] * r + tau[:, None] * rp   # F_1: h_1 < 0, coordinates 2,3 cross

def norms(H, kind):
    return np.abs(H).max(axis=1) if kind == 'sup' else np.linalg.norm(H, axis=1)

tau = np.linspace(1e-6, 1 - 1e-6, 400001)
print("eps   kappa   theta_x(sup) theta_x(Eucl) formula   Theta_NT  phi_j(w)Eucl  phi_j(w)sup")
for eps in [0.05, 0.1, 0.3, 0.6, 0.9]:
    kap, r, rp = t1(eps)
    H = facet(eps, tau)
    out = []
    for kind in ['sup', 'eucl']:
        nr = norms(H, kind)
        out.append(max((H[:, 1] / nr).max(), (H[:, 2] / nr).max()))
    form = np.sqrt((kap**2 + 1) / (kap**2 + 2))
    ThNT = (kap + 1) / np.sqrt((kap + 1)**2 + 2)
    w = np.array([-1.0, 0.0, kap])          # crossing of coordinate 2 on F_1 (w_21 in the writeup)
    print(f"{eps:4.2f} {kap:7.4f}   {out[0]:.6f}     {out[1]:.6f}   {form:.6f}  {ThNT:.6f}   "
          f"{kap/np.linalg.norm(w):.6f}     {kap/np.abs(w).max():.6f}")

print("\nFraction of tau in (0,1) where some positive coordinate of h(tau) is a band point (eps = 0.3):")
eps = 0.3
H = facet(eps, tau)
for kind in ['sup', 'eucl']:
    nr = norms(H, kind)
    for th in [0.01, 0.05, 0.1, 0.3, 0.5]:
        band = ((H[:, 1] > 0) & (H[:, 1] <= th * nr)) | ((H[:, 2] > 0) & (H[:, 2] <= th * nr))
        print(f"  {kind:4s} theta={th:4.2f}: {band.mean():.4f}  (nonzero for every theta>0: crossings are band points)")
