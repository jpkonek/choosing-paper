"""N7 (NUMERICS): PP72's u1-argmax defence D0 along the family rays, for a rival X with V(C_a -> X) = 0
(balanced swap): D0 at a family point b near a picks argmax_w Gamma_w(a, b).  Reports Gamma/t for
R3 outward (-e3) and inward (+e3) at u and m1(a); R2 outward (+e2) and inward (-e2) at u and m2(a)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib73 import *
G = sample(2_000_000, seed=11)
def gam(a0, d, t=0.01):
    a0 = np.asarray(a0, float); b = norm(a0 * np.exp(t * np.asarray(d, float)))
    return (Phi(G, advice(G, a0)) - Phi(G, advice(G, b))) / t
e = np.eye(3)
for name, a0 in [('u', loop(1.0)[0]), ('m1(1.05)', loop(1.05)[1]), ('m1(1.10)', loop(1.10)[1]),
                 ('m2(1.05)', loop(1.05)[2]), ('m2(1.10)', loop(1.10)[2])]:
    for dn, d in [('-e3 (R3 out)', -e[2]), ('+e3 (R3 in)', e[2]), ('+e2 (R2 out)', e[1]), ('-e2 (R2 in)', -e[1])]:
        g = gam(a0, d)
        print(f'{name:9s} {dn:13s} Gamma/t = {np.round(g,4)}  argmax world {np.argmax(g)+1}  gap(top two) = {np.sort(g)[-1]-np.sort(g)[-2]:.4f}')
