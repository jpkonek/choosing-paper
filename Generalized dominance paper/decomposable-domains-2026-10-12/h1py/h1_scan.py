"""Scan weights t (min t < 1/(L+1)) for incoherent nu^L-Bayes sets: convexity test on unit directions."""
import numpy as np
rng = np.random.default_rng(7)
eps, s, L = 0.3, 0.9, 5.0
u = np.ones(3)/3
V = np.array([(1-eps)*u + eps*np.eye(3)[k] for k in range(3)])
Vp = np.array([u + s*(v-u) for v in V])
P = lambda K, g: (g @ K.T).min(axis=1)
def field(g):
    sig = np.sign(g); inT = P(V, g) > 0
    corr = np.where(inT[:,None], sig > 0, sig < 0)
    return np.where(corr, L, 1.0)*sig
g = rng.standard_normal((400000,3)); g = g[P(Vp,g) > 0]; g /= np.linalg.norm(g,axis=1)[:,None]
c = field(g)
for t in [(0.45,0.45,0.10),(0.6,0.3,0.1),(0.47,0.47,0.06),(0.3,0.6,0.1),(0.5,0.4,0.1),(0.2,0.7,0.1),(0.12,0.12,0.76),(0.15,0.15,0.7)]:
    t = np.array(t); B = (c @ t) > 0
    A = g[B]; hits = 0
    a = A[rng.integers(0,len(A),20000)]; b = A[rng.integers(0,len(A),20000)]
    mid = 0.5*(a+b); ok = P(Vp, mid) > 0
    rej = (field(mid[ok]) @ t) < 0
    print(t, " accepted frac %.3f" % B.mean(), " midpoint-rejections:", int(rej.sum()), "of", int(ok.sum()))
