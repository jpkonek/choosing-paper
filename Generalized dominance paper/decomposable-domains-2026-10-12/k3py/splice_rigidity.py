"""NUMERICS for Theorem K3.7(c) in K3_notes.md (blind-set rigidity next to two integrable worlds).
(1) A blind set built as Z = (E_1(C_12) n R_12) u (E_1(C_13) n R_13), with C_12 = D_{K_1}, K_1 = conv(K' u {e1, m12}),
    C_13 = D_{K_0}, K_0 = conv(K' u {e1, m13}): the two splices S_1 = (P_1 off Z, P_2 on Z) and S_0 = (P_1 off Z,
    P_3 on Z) coincide with D_{K_1}, D_{K_0} on the sample (so they are coherent).
(2) A blind set of another shape (a slab in the orthant (+,-,+)) makes S_1 non-convex: midpoint witnesses."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from k3_common import Vp, E, in_D, in_U, sample_U, mixed, midpoint_violations

rng = np.random.default_rng(7)
G = sample_U(rng, 300000)
G = G[mixed(G)]
lam = mu = 0.5
m12 = lam * E[0] + (1 - lam) * E[1]
m13 = mu * E[0] + (1 - mu) * E[2]
K1 = np.vstack([Vp, E[0], m12])
K0 = np.vstack([Vp, E[0], m13])


def R12(g): return np.sign(g[:, 0]) != np.sign(g[:, 1])
def R13(g): return np.sign(g[:, 0]) != np.sign(g[:, 2])
def P(i, g): return g[:, i] > 0


def Zrigid(g):
    a = R12(g) & (in_D(g, K1) != P(0, g))
    b = R13(g) & (in_D(g, K0) != P(0, g))
    return a | b


def S(Zf, j):
    def acc(g):
        z = Zf(g)
        out = P(0, g).copy()
        out[z] = P(j, g)[z]
        return out
    return acc


Z = Zrigid(G)
print("(1) rigid blind set: fraction of mixed sample in Z = %.4f" % Z.mean())
print("    S_1 == D_K1 on sample:", bool(np.all(S(Zrigid, 1)(G) == in_D(G, K1))))
print("    S_0 == D_K0 on sample:", bool(np.all(S(Zrigid, 2)(G) == in_D(G, K0))))
cons = (R12(G) & R13(G))
print("    consistency on R12 n R13 (both descriptions agree):",
      bool(np.all((in_D(G, K1) != P(0, G))[cons] == (in_D(G, K0) != P(0, G))[cons])))
for name, j in (("S_1", 1), ("S_0", 2)):
    bad, tot = midpoint_violations(S(Zrigid, j), G, rng)
    print("    midpoint violations for %s: %d of %d sums in U" % (name, bad, tot))


def Zslab(g):
    o = (g[:, 0] > 0) & (g[:, 1] < 0) & (g[:, 2] > 0)
    r = g[:, 1] / np.maximum(g[:, 0], 1e-300)
    return o & (r > -3) & (r < -1)


Z2 = Zslab(G)
print("(2) slab blind set in (+,-,+): fraction = %.4f" % Z2.mean())
for name, j in (("S_1", 1), ("S_0", 2)):
    bad, tot = midpoint_violations(S(Zslab, j), G, rng, trials=200000)
    print("    midpoint violations for %s: %d of %d sums in U" % (name, bad, tot))
