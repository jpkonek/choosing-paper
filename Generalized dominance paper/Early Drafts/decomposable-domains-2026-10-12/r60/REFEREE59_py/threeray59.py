"""threeray59: the audit's three-ray calculation, computed directly between two members of one down-shift ray
(not via T).  For a = B_{k, lam_a} and a_n = B_{k, lam_n} closer to T (lam_n > lam_a), V(C_{a_n} -> C_a) should be
gamma_n (2e_k - e_i - e_j) with gamma_n = p(lam_a) - p(lam_n) > 0.  Then for X balanced against C_a
(V(C_a -> X) = 0), V(C_{a_n} -> X) = V(C_{a_n} -> C_a) + V(C_a -> X) is the same vector (additivity of Phi).
u1 on R: u1(S) = 0, u1(h) = eps_o if Cor(h) = {o} (type B_o), -eps_o if Wr(h) = {o} (type A_o), eps_o = 1 - 3e_o."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib59 import *
from layer59 import layer
T = post((1, 1, 1))
def Vrec(P, Q):
    cs = cells({'P': P, 'Q': Q}); V = [0.0] * 3
    for c in cs:
        t = htype(c['pt'])
        if t[0] == 'U' or c['vals']['P'] == c['vals']['Q']: continue
        assert -1 not in (c['vals']['P'], c['vals']['Q'])
        o = t[1]; a = solid(c['poly'])
        u1h = [((1.0 - 3.0 * (i == o)) * (1 if t[0] == 'B' else -1)) for i in range(3)]
        sg = (1 if c['vals']['Q'] == 1 else 0) - (1 if c['vals']['P'] == 1 else 0)
        for i in range(3): V[i] += sg * u1h[i] * a
    return V
for k in range(3):
    for (ln, la) in ((F(99, 100), F(9, 10)), (F(20, 21), F(3, 4)), (F(1) - F(1, 1000), F(1) - F(1, 100))):
        V = Vrec(post(down(k, ln)), post(down(k, la)))
        pa = sum(layer(k, la)['odd'][i] for i in (k, (k + 1) % 3)); pn = sum(layer(k, ln)['odd'][i] for i in (k, (k + 1) % 3))
        g = pa - pn
        print('ray %d: lam_n=%.4f lam_a=%.4f  V/gamma = (%.6f, %.6f, %.6f), gamma = %.6e' % (k + 1, float(ln), float(la), V[0] / g, V[1] / g, V[2] / g, g))
