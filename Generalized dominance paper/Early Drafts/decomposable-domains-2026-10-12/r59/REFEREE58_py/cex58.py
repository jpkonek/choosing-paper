"""cex58: the 'section closure followed by copying' counterexample to PP72 Theorem 6.2, step 3 (NUMERICS
illustration of an argument that is PROVED in REFEREE_round58 section 1.3).

Objects (log-likelihood indices):
  a   = s_a (-1,2,-1) in R2;  a_n = s_n (-1,2,-1), s_n increasing to s_a (inward approach);
  c   = s_c d3 + t_c d1, an installed defender of PP72's set I (m = s_c d3 in R3, class-1 move t_c);
  b_j = s_j d3 in R3, s_j -> 0 (approach to u along R3).
  F   = balanced odd-1 subset of {T != C_c} on which C_a = T;  X = C_a[F -> C_c].
  F_n = {C_{a_n} != X};  Y_n = T[F_n -> X].
Claims checked on the sample:
  (i)   (2V) for every index used;  (ii) C_{a_n} = T on F_n, so rec(T -> Y_n) = rec(C_{a_n} -> X) exactly;
  (iii) V(C_a -> X) ~ 0, V(C_{a_n} -> X) ~ (q,-2q,q);  (iv) V(C_{b_j} -> Y_n) has a STRICT maximum at world 1,
  so PP72's argmax defence D0 (priority 2>3>1) installs C_{b_j} <=_1 Y_n; the section at u then gives T <=_1 Y_n,
  whose record is rec(C_{a_n} -> X); the section at a then gives C_a <=_1 X (a u1-null record at world 1).
  (v)   the margin rule of section 1.4 sends the same stage-1 records to world 3 instead.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lib58 import *

G = sample(int(os.environ.get('NS', '400000')))
g = Geo(G)
s_a, s_c, t_c = 0.02, 0.06, 0.03
R2dir = np.array([-1.0, 2.0, -1.0])
xa = s_a * R2dir
xc = s_c * D3 + t_c * D1
T = advice(G, [0, 0, 0]); Ca = advice(G, xa); Cc = advice(G, xc)
print('N =', g.N, '; log(c/u) =', xc, '(strictly middle coordinate: world 1)')
for nm, A in [('T', T), ('C_a', Ca), ('C_c', Cc)]:
    print('  (2V) violations for %s: %d' % (nm, g.check2V(A)))

La = T != Ca; Lc = T != Cc
ann = (g.nrm > 0.5) & (g.nrm < 2.0)
base = Lc & ~La & (g.o == 0) & ann
imp = base & (((Cc != 0) & (T == 0) & g.co) | ((Cc == 0) & (T != 0) & ~g.co))
wor = base & ~imp
print('odd-1 points of L(u,c) \\ L(u,a) in the annulus: improving world 1 mass %.5f, worsening mass %.5f'
      % (g.mass(imp), g.mass(wor)))
print('  (for comparison: mass of L(u,a) = %.5f, of L(u,c) = %.5f)' % (g.mass(La), g.mass(Lc)))
# balance: keep the smaller side, take a radial slab of the larger side, fine-tune by single points
Mi, Mw = g.mass(imp), g.mass(wor)
small, large = (imp, wor) if Mi <= Mw else (wor, imp)
target = g.mass(small) * g.N
idx = np.nonzero(large)[0]
idx = idx[np.argsort(g.nrm[idx])]
cs = np.cumsum(g.nrm[idx])
k = int(np.searchsorted(cs, target))
F = small.copy(); F[idx[:k]] = True
print('F: %d points, mass %.5f; residual imbalance %.2e' % (F.sum(), g.mass(F), abs(cs[k - 1] - target) / g.N))
X = Ca.copy(); X[F] = Cc[F]
assert (Ca[F] == T[F]).all()
VaX = g.V(Ca, X)
print('V(C_a -> X) =', np.round(VaX, 7), '  (u1-null up to the sampling residual)')
print('V(T -> C_c) on F: c_2 = c_3 = 0 exactly since F is odd-1 only')

ok_all = True
for n in range(1, 6):
    s_n = s_a * (1 - 2.0 ** (-n))
    Can = advice(G, s_n * R2dir)
    assert g.check2V(Can) == 0
    Fn = Can != X
    copy_ok = bool((Can[Fn] == T[Fn]).all())
    Yn = T.copy(); Yn[Fn] = X[Fn]
    same_record = bool(((T != Yn) == Fn).all() and (T[Fn] == Can[Fn]).all() and (Yn[Fn] == X[Fn]).all())
    Vn = g.V(Can, X)
    Gam = g.V(Can, Ca)                        # Gamma(a, a_n) = Phi(C_a) - Phi(C_{a_n})
    print('n=%d s_n=%.5f: C_{a_n}=T on F_n: %s; rec(T->Y_n)=rec(C_{a_n}->X): %s' % (n, s_n, copy_ok, same_record))
    print('      V(C_{a_n}->X) = %s ; Gamma(a,a_n) = %s' % (np.round(Vn, 6), np.round(Gam, 6)))
    for j in range(1, 5):
        s_j = 0.01 * 2.0 ** (-j)
        Cb = advice(G, s_j * D3)
        assert g.check2V(Cb) == 0
        Vb = g.V(Cb, Yn)
        Gu = g.V(Cb, T)                       # Gamma(u, b_j)
        order = np.argsort(-Vb)
        strict1 = Vb[0] > Vb[1] and Vb[0] > Vb[2]
        ok_all &= strict1 and copy_ok and same_record
        # margin rule (section 1.4): world 1 only if V1 >= max(V2,V3) + kappa*|V|_inf
        kap = 0.25
        m1 = Vb[0] >= max(Vb[1], Vb[2]) + kap * np.abs(Vb).max()
        alt = 1 + int(np.argmax(Vb[1:])) + 1 if not m1 else 1
        if j in (1, 4):
            print('      j=%d: Gamma(u,b_j)=%s  V(C_bj->Y_n)=%s  strict max at 1: %s; V1-V2=%.2e V1-V3=%.2e; '
                  'margin rule (kappa=%.2f) picks world %d' % (j, np.round(Gu, 6), np.round(Vb, 6), strict1,
                                                                Vb[0] - Vb[1], Vb[0] - Vb[2], kap, alt))
print('ALL STAGE-1 CHECKS PASS' if ok_all else 'SOME CHECK FAILED')
# the defender's protection failure: Y' = C_c[F -> T] and rec(Y' -> C_c) = rec(C_a -> X)
Yp = Cc.copy(); Yp[F] = T[F]
supp = Yp != Cc
print("rec(Y'->C_c) = rec(C_a->X): %s" % bool((supp == (Ca != X)).all() and (Yp[supp] == Ca[supp]).all()
                                             and (Cc[supp] == X[supp]).all()))
