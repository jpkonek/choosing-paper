"""F2 NUMERICS (no proof rests on this). Geometry of the far end x -> 1 of the D2 chain (n = 2).
Run: python3 -I f2_d2_geometry.py
Coordinates: K' = [al, be] = weights on world 2; standard Gaussian => uniform angle phi.
C_s = D_[al*s, be+(1-be)*s]. On M+ (h1>0>h2): entry s = (tau-be)/(1-be), tau = h1/(h1-h2).
On M- (h1<0<h2): entry s = th/al, th = -h1/(h2-h1); h in U iff th < al (M+: tau > be)."""
import numpy as np

al, be = 0.3, 0.6
N = 2_000_000
phi = np.linspace(-np.pi, np.pi, N, endpoint=False) + np.pi / N
h1, h2 = np.cos(phi), np.sin(phi)
Mp = (h1 > 0) & (h2 < 0)
Mm = (h1 < 0) & (h2 > 0)
tau = np.where(Mp, h1 / (h1 - h2), np.nan)
th = np.where(Mm, -h1 / (h2 - h1), np.nan)
inUp = Mp & (tau > be)
inUm = Mm & (th < al)
s = np.full(N, np.nan)
s[inUp] = (tau[inUp] - be) / (1 - be)
s[inUm] = th[inUm] / al
M = inUp | inUm
# x := lambda-cdf of s over M (uniform angle measure restricted to M)
order = np.argsort(s[M]); sv = s[M][order]
x = np.full(N, np.nan); xm = np.empty(M.sum()); xm[order] = (np.arange(M.sum()) + 0.5) / M.sum(); x[M] = xm

print("(1) (1,0) is in U (P_K'((1,0)) = 1-be > 0):", 1 - be > 0)
for eps in [1e-1, 1e-2, 1e-3, 1e-4]:
    sel = inUp & (phi > -eps)
    print(f"    M+ directions within angle {eps:g} of (1,0): min x = {np.nanmin(x[sel]):.6f}")
for eps in [1e-1, 1e-2, 1e-3]:
    sel = inUm & (th > al - eps)
    print(f"    M- directions with theta within {eps:g} of alpha' (dU): min x = {np.nanmin(x[sel]):.6f}")

# (2) share of the near-unanimous part (M+) among levels x in [1-d, 1)
for d in [0.1, 0.03, 0.01, 0.003]:
    lev = M & (x >= 1 - d)
    print(f"(2) levels x >= 1-{d}: fraction in near-unanimous part M+ = {np.mean(inUp[lev]):.4f}")

# (3) pushforward of a small angular sector around (1,0) has density bounded below near x = 1
sec = inUp & (phi > -0.05)
hist, edges = np.histogram(x[sec], bins=40, range=(0.9, 1.0))
dens = hist / (M.sum() * (edges[1] - edges[0]))
print(f"(3) density of lambda|sector(1,0) in x on [0.9,1): min {dens[dens > 0].min():.3f}, max {dens.max():.3f} (should be > 0 up to 1)")

# (4) rho = 1/(1-x) (Prop. D2sigma): integral over the sector around (1,0), truncated at x <= 1-2^-k, grows like log
for k in [4, 8, 12, 16]:
    sel = sec & (x <= 1 - 2.0 ** -k)
    print(f"(4) int_sector 1/(1-x) dlambda over x <= 1-2^-{k}: {np.sum(1 / (1 - x[sel])) / M.sum():.4f}")
