"""layer59: the layer masses alpha, beta along the pure down-shift ray of world k at u (exact cells,
float solid angles; deterministic, no sampling).

B_lam := C_m with m = (1,1,lam) for k = 3 (lam = e^{-3t} < 1), etc.  L(lam) := {T != B_lam}.
alpha = mass of the odd-k part of L, beta_i = mass of the odd-i part (i != k), p = alpha + beta.
alphaA = mass of the 'gain A_k' part (T silent, B answers h, type A_k): the only part E can meet.
Also: (2V) along the ray (no -h answer), the u1 ledger V(T -> B) = p (3e_k - 1), monotone nesting,
Lemma 4.1 overlaps, and the first-order identity alpha'(0) = 2 beta'(0) (by quadrature of the
boundary integrals derived in REFEREE_round59 Section 2).
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib59 import *

T = post((1, 1, 1))


def layer(k, lam):
    B = post(down(k, lam))
    cs = cells({'T': T, 'B': B})
    m = {'odd': [0.0, 0.0, 0.0], 'gainA': 0.0, 'loseB': 0.0, 'minus': 0, 'V': [0.0, 0.0, 0.0]}
    for c in cs:
        h = c['pt']
        t = htype(h)
        vT, vB = c['vals']['T'], c['vals']['B']
        if vB == -1 or vT == -1:
            m['minus'] += 1
        if vT == vB or t[0] == 'U':
            continue
        o = t[1]
        a = solid(c['poly'])
        m['odd'][o] += a
        if o == k and t[0] == 'A' and vT == 0:
            m['gainA'] += a
        if o == k and t[0] == 'B' and vT == 1:
            m['loseB'] += a
        # u1 increment Phi(B) - Phi(T) at this cell: u1(h) = eps_o |g| if Cor(h) = {o}, -eps_o if Wr(h) = {o}
        corodd = (t[0] == 'B')      # B_o: h right only at o
        eps = [1.0 - 3.0 * (i == o) for i in range(3)]
        u1h = [(e if corodd else -e) for e in eps]
        sgn = (1 if vB == 1 else 0) - (1 if vT == 1 else 0)
        for i in range(3):
            m['V'][i] += sgn * u1h[i] * a
    return m


def first_order():
    c = 16.0 / 7.0
    w = lambda a, b: (1 + a * a + b * b) ** -1.5
    N = 200000
    # A_k gain rate: c * int_0^c w(x, c-x) dx ; A_i lose rate: int_0^c z w(c-z, z) dz
    xs = [(i + 0.5) * c / N for i in range(N)]
    Ag = c * sum(w(x, c - x) for x in xs) * c / N
    Al = sum(z * w(c - z, z) for z in xs) * c / N
    # kite Q = conv{0, (0,-7/16), (-7/23,-7/23), (-7/16,0)}; outer edges e1: (0,-7/16)->(-7/23,-7/23), e2 symmetric
    P0, P1, P2 = (0.0, -7 / 16), (-7 / 23, -7 / 23), (-7 / 16, 0.0)
    def edge(p, q):
        L = math.hypot(q[0] - p[0], q[1] - p[1])
        nx, ny = (q[1] - p[1]) / L, -(q[0] - p[0]) / L
        # outward normal: pointing away from origin
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        if nx * mx + ny * my < 0:
            nx, ny = -nx, -ny
        rad = stretch = 0.0
        for i in range(N):
            s = (i + 0.5) / N
            x, y = p[0] + s * (q[0] - p[0]), p[1] + s * (q[1] - p[1])
            ww = w(x, y) * L / N
            rad += (x * nx + y * ny) * ww
            stretch += (y * ny) * ww
        return rad, stretch
    r1, s1 = edge(P0, P1)
    r2, s2 = edge(P1, P2)
    Bl = r1 + r2          # B_k lose rate (radial contraction)
    Bg = s1 + s2          # B_i gain rate (stretch of the second coordinate)
    return Ag, Bl, Al, Bg


def main():
    print('first-order rates per unit (1 - lam):')
    Ag, Bl, Al, Bg = first_order()
    print('  alpha\'(0) = A_k gain %.9f + B_k lose %.9f = %.9f' % (Ag, Bl, Ag + Bl))
    print('  beta\'(0)  = A_i lose %.9f + B_i gain %.9f = %.9f' % (Al, Bg, Al + Bg))
    print('  ratios: Al/Ag = %.9f, Bg/Bl = %.9f, alpha\'/beta\' = %.9f, alphaA\'/p\' = %.6f'
          % (Al / Ag, Bg / Bl, (Ag + Bl) / (Al + Bg), Ag / (Ag + Bl + Al + Bg)))
    lams = [F(1) - F(1, 10 ** j) for j in (6, 5, 4, 3)] + [F(99, 100), F(95, 100), F(20, 21), F(9, 10),
            F(8, 10), F(3, 4), F(7, 10), F(6, 10), F(1, 2), F(45, 100), F(7, 16) + F(1, 10 ** 6)]
    lams += [F(20, 21) ** j for j in (1, 2, 3, 4, 6)]
    lams = sorted(set(lams), reverse=True)
    print('\nk = 3 ray (lam = m_3; 2V needs lam >= 7/16):')
    print('   lam        t=-ln(lam)/3   alpha        beta1        beta2      a/b      alpha/p   alphaA/p  '
          ' V/p (should be (-1,-1,2))   -h cells')
    worst = 0.0; worstA = 0.0
    prev = None
    for lam in lams:
        m = layer(2, lam)
        al, b1, b2 = m['odd'][2], m['odd'][0], m['odd'][1]
        p = al + b1
        V = [v / p for v in m['V']]
        worst = max(worst, al / p); worstA = max(worstA, m['gainA'] / p)
        print('  %.7f  %.7f  %.9f  %.9f  %.9f  %.6f  %.6f  %.6f   (%.6f, %.6f, %.6f)  %d'
              % (float(lam), -math.log(float(lam)) / 3, al, b1, b2, al / b1, al / p, m['gainA'] / p,
                 V[0], V[1], V[2], m['minus']))
    print('max alpha/p on the grid = %.6f ; max alphaA/p = %.6f' % (worst, worstA))
    print('theta* = (1-a)/(1+a) for a = max alpha/p: %.6f ; for a = max alphaA/p: %.6f'
          % ((1 - worst) / (1 + worst), (1 - worstA) / (1 + worstA)))
    # other rays by symmetry (spot check)
    for k in (0, 1):
        m = layer(k, F(20, 21) ** 6)
        al = m['odd'][k]; bs = [m['odd'][i] for i in range(3) if i != k]
        print('ray k=%d at lam=(20/21)^6: alpha=%.9f beta=%.9f,%.9f  alpha/p=%.6f' % (k + 1, al, bs[0], bs[1], al / (al + bs[0])))
    # Lemma 4.1 overlaps: L_k^{(i)}(t) cap L_j^{(i)}(s), i the third world
    print('\nLemma 4.1 overlap masses (odd-i part of L_k(lam) cap L_j(lam\'), i third world):')
    for (k, j) in ((2, 0), (2, 1), (0, 1)):
        i = 3 - k - j
        for (l1, l2) in ((F(20, 21), F(20, 21)), (F(1) - F(1, 1000), F(1) - F(1, 100)), (F(1, 2), F(1) - F(1, 1000))):
            cs = cells({'T': T, 'Bk': post(down(k, l1)), 'Bj': post(down(j, l2))})
            ov = sum(solid(c['poly']) for c in cs if htype(c['pt'])[0] != 'U' and htype(c['pt'])[1] == i
                     and c['vals']['Bk'] != c['vals']['T'] and c['vals']['Bj'] != c['vals']['T'])
            print('  k=%d j=%d i=%d lam_k=%.4f lam_j=%.4f overlap=%.3e' % (k + 1, j + 1, i + 1, float(l1), float(l2), ov))
    # nesting: along the ray each point changes at most once
    print('\nnesting check (L(lam1) subset L(lam2), B_lam2 = B_lam1 on L(lam1)) for lam2 < lam1:')
    for (l1, l2) in ((F(20, 21), F(8, 10)), (F(99, 100), F(1, 2))):
        cs = cells({'T': T, 'B1': post(down(2, l1)), 'B2': post(down(2, l2))})
        bad = sum(1 for c in cs if c['vals']['B1'] != c['vals']['T'] and c['vals']['B2'] != c['vals']['B1'])
        print('  lam1=%.3f lam2=%.3f violations=%d' % (float(l1), float(l2), bad))


if __name__ == '__main__':
    main()
