"""check58: independent checks of PP73 (Cor 1.3, Thm 2.3, Prop 4.1, Lemma 4.7), PP72 (Lemma 6.0 shapes, (D3') ledger
formula, Prop 4.2) and the rescaling inequalities / composition (AUDIT_round59_rescaling).  NUMERICS on an
S3-symmetrised Gaussian sample; exact identities are checked to rounding."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lib58 import *

G = sample(int(os.environ.get('NS', '300000')))
g = Geo(G)
rng = np.random.default_rng(5859)
print('N =', g.N)

# ---------- 5. rescaling inequalities and composition ----------
def credal_accept(Gs, m, K=4000):
    """g in D_{M_m} tested on K random points of M_m (plus its vertices): p.g > 0 for all."""
    w = rng.dirichlet(np.ones(3), K)
    P = np.vstack([VERT, w @ VERT])                    # points of M
    Q = P * m; Q /= Q.sum(1, keepdims=True)            # points of M_m
    s = Gs @ Q.T
    return np.where((s > 0).all(1), 1, np.where((s < 0).all(1), -1, 0))
Gs = G[:20000]
bad = 0
for _ in range(5):
    x = rng.normal(0, 0.5, 3); m = np.exp(x)
    bad += int((credal_accept(Gs, m) != advice(Gs, x)).sum())
print('[5a] vertex inequalities vs sampled credal set: disagreements =', bad, '(expected 0 up to boundary)')
bad = 0
for _ in range(5):
    x, y = rng.normal(0, 0.5, 3), rng.normal(0, 0.5, 3)
    # C_{m o b}(g) = C_m(b o g)   and   M_m rescaled by b = M_{m o b}
    bad += int((advice(Gs, x + y) != advice(Gs * np.exp(y), x)).sum())
    V1 = VERT * np.exp(x); V1 /= V1.sum(1, keepdims=True)
    V2 = V1 * np.exp(y); V2 /= V2.sum(1, keepdims=True)
    V3 = VERT * np.exp(x + y); V3 /= V3.sum(1, keepdims=True)
    assert np.allclose(V2, V3)
print('[5b] composition C_m o b = C_{m o b} (pointwise and vertexwise): disagreements =', bad)

# ---------- PP73 Cor 1.3 and Thm 2.3 on one loop ----------
for a in (1.03, 1.10):
    s = np.log(a)
    P0 = advice(G, [0, 0, 0]); P1 = advice(G, s * D3); P2 = advice(G, s * (D3 + D1))
    P = [P0, P1, P2]
    for nm, A in zip(('P0', 'P1', 'P2'), P):
        assert g.check2V(A) == 0, nm
    rk = lambda A, w: np.where(A == 0, 1, np.where(np.sign(G[:, w]) * A > 0, 0, 2))
    # edges: P0 ->(3) P1, P1 ->(1) P2, P2 ->(2) P0 : successor pointwise weakly worse at the class world
    msg = []
    for (i, j, w) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        d = rk(P[j], w) - rk(P[i], w)
        msg.append('P%d->P%d world %d: worse pts %d, better pts %d' % (i, j, w + 1, (d > 0).sum(), (d < 0).sum()))
    print('[Cor1.3] a=%.2f ' % a + '; '.join(msg))
    # Thm 2.3: S_i = Sil(P_i) & M_{k_i} & {P_i != P_{i-1}};  P_{i-1} = A and P_{i+1} = A there
    k = {0: 2, 1: 0, 2: 1}
    A = np.where((np.sign(G) > 0).sum(1) >= 2, 1, -1)
    out = []
    for i in range(3):
        Si = (P[i] == 0) & (g.o == k[i]) & (P[i] != P[i - 1])
        out.append('S_%d mass %.4f, P_{i-1}=A %.4f, P_{i+1}=A %.4f' % (i, g.mass(Si), (P[i - 1][Si] == A[Si]).mean(),
                                                                       (P[(i + 1) % 3][Si] == A[Si]).mean()))
    print('[Thm2.3] a=%.2f ' % a + '; '.join(out))

# ---------- PP73 Prop 4.1: balanced swaps across scales; none within one loop ----------
def signs(x0, x1, w):
    A0, A1 = advice(G, x0), advice(G, x1)
    L = (A0 != A1) & (g.o == w)
    imp = L & (((A1 != 0) & (A0 == 0) & g.co) | ((A1 == 0) & (A0 != 0) & ~g.co))
    return g.mass(imp), g.mass(L & ~imp)
for (a, ap) in ((1.10, 1.05), (1.05, 1.10)):
    m1 = np.log(a) * D3; m2 = np.log(ap) * (D3 + D1)
    print('[Prop4.1] m1(%.2f) vs m2(%.2f): odd-2 layer improving/worsening world-2 masses %.5f / %.5f'
          % ((a, ap) + signs(m1, m2, 1)))
s = np.log(1.10)
for (x0, x1, nm) in ((0 * D3, s * D3, 'P0,P1'), (s * D3, s * (D3 + D1), 'P1,P2'), (s * (D3 + D1), 0 * D3, 'P2,P0')):
    print('[Cor1.3] same loop %s: per odd world (imp, wor) masses: %s' % (nm, [tuple(np.round(signs(x0, x1, w), 5))
                                                                         for w in range(3)]))

# ---------- Lemma 6.0 / PP73 Lemma 4.7: exact shapes along family directions; asymmetric rows ----------
def Gam(x0, x1):
    return g.V(advice(G, x1), advice(G, x0))       # Phi(C_x0) - Phi(C_x1)
t = 0.004
R2 = D3 + D1
for nm, x0 in (('u', 0 * D3), ('m1(1.05)', np.log(1.05) * D3), ('m2(1.05)', np.log(1.05) * R2)):
    rows = []
    for dn, d in (('R3 out (+d3)', D3), ('R3 in (-d3)', -D3), ('R2 out (+R2)', R2), ('R2 in (-R2)', -R2)):
        v = Gam(x0, x0 + t * d) / t
        rows.append('%s %s' % (dn, np.round(v, 4)))
    print('[L6.0/4.7] at %s: ' % nm + '; '.join(rows))

# ---------- (D3') ledger formula at u, class 3, with a fill having an h-part and a -h part ----------
T = advice(G, [0, 0, 0])
Amaj = np.where((np.sign(G) > 0).sum(1) >= 2, 1, -1)
k = 2
sil = (T == 0) & (g.o == k)
for tt in (0.01, 0.03):
    B = advice(G, tt * D3)
    L = T != B
    Eh = sil & (Amaj == g.h) & L & (g.nrm < 1.0)        # h-part inside the layer (so inside R)
    Emh = sil & (Amaj != g.h) & (g.nrm < 0.6)           # -h part
    E = Eh | Emh
    e, f = g.mass(Eh), g.mass(Emh)
    al = g.mass(L & (g.o == k)); bi = g.mass(L & (g.o == 0)); bj = g.mass(L & (g.o == 1))
    # direct computation: Phi with -h values (otherwise row (|Wr|,2|Cor|) = (1,4) at odd-k majority points)
    def Phi(Xa):
        U = np.zeros((g.N, 3))
        on = Xa != 0
        hpos = on & (Xa == g.h)
        U[hpos] = g.Uh[hpos]
        mh = on & (Xa != g.h)
        row = -np.ones(3); row[k] = 4.0                # A = -h is correct at the two non-odd worlds, wrong at k
        U[mh] = row * g.nrm[mh][:, None]
        return U.sum(0) / g.N
    X = T.copy(); X[E] = Amaj[E]
    Vd = Phi(X) - Phi(B)
    x = e + f
    Vi = al + 2 * bi - bj - x; Vj = al + 2 * bj - bi - x; Vk = 2 * e + 4 * f - (2 * al + bi + bj)
    print("[D3'] t=%.2f e=%.4f f=%.4f: direct V(B->X)=%s  formula (i,j,k)=(%.5f, %.5f, %.5f)  beta_i-beta_j=%.1e"
          % (tt, e, f, np.round(Vd, 5), Vi, Vj, Vk, bi - bj))
# Prop 4.2 (pure-h class-3 fill of T): V(B->X) = (p-e, p-e, 2e-2p)
B = advice(G, 0.02 * D3); L = T != B
Eh = sil & (Amaj == g.h) & L & (B == 0) & (g.nrm < 1.5)
X = T.copy(); X[Eh] = g.h[Eh]
p = g.mass(L & (g.o == k)) + g.mass(L & (g.o == 0)); e = g.mass(Eh)
print('[Prop4.2] V(B->X) = %s ; formula (p-e, p-e, 2e-2p) = %s' % (np.round(g.V(B, X), 6),
                                                                   np.round([p - e, p - e, 2 * e - 2 * p], 6)))
print('[H] sum of V over worlds for an H-record out of a member (should be 0):', round(float(g.V(B, X).sum()), 9))
