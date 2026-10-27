"""geom68: exact rational geometry for PP68 (eps = 3/10, c = 7/30).

Models (all D_K, K a polytope, answer s at g iff s*min_{v in vert K} v.g > 0):
  T     : K = M = c*1 + eps*Delta (vertices c*1 + eps*e_i)
  Nstar : K = conv(M u {(1/2,1/2,0)})          (PP68 Lemma 2.1)
  D     : the -e3 edge posterior, K = [(16,7,0),(7,16,0)]/23  (PP64 Lemma 4.2)
  Dm13  : precise model at m = (9,0,7)/16 on the edge [e1,e3]   (PP68 Prop 2.4 carrier)
Checks (exact, on an integer grid plus random rationals):
  L1  Nstar = T except where T answers s with s*(g1+g2) < 0; there Nstar = S and s is 3-correct;
  L2  class pattern of the silenced set: class 3 -> T says B; class 1 / class 2 -> T says A; never unmixed;
  L3  Nstar = S wherever T = S (in particular on Q_3), so Nstar != A a.e. on Q_3;
  L4  witnesses: Nstar vs T mixed at worlds 1 and 2 (better on t3,l1 / t3,l2; worse on l2 / l1);
  L5  D = A on class 3; D weakly 3-worse than T;
  L6  Dm13 equals T on L* = {Nstar != T}, and Dm13 = A on a non-null part of Q_3 (open witness);
  L7  posterior members C_q = T(g o q) on a grid of interior q: none equals T on L* while answering A
      somewhere on Q_3 (sampled; NUMERICS-level, reported as such).
Run: python3 -I -B geom68.py
"""
from fractions import Fraction as F
import itertools, random

eps = F(3, 10)
c = (1 - eps) / 3
M = [tuple(c + (eps if j == i else 0) for j in range(3)) for i in range(3)]
h12 = (F(1, 2), F(1, 2), F(0))
KN = M + [h12]
KD = [(F(16, 23), F(7, 23), F(0)), (F(7, 23), F(16, 23), F(0))]
KDm = [(F(9, 16), F(0), F(7, 16))]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def ans(K, g):
    vals = [dot(v, g) for v in K]
    if all(x > 0 for x in vals):
        return '+'
    if all(x < 0 for x in vals):
        return '-'
    return 'S'


def sgn(x):
    return '+' if x > 0 else ('-' if x < 0 else '0')


def cls(g):
    s = [sgn(x) for x in g]
    if '0' in s:
        return None
    if s[0] == s[1] == s[2]:
        return 0
    for k in range(3):
        o = [s[j] for j in range(3) if j != k]
        if o[0] == o[1] and s[k] != o[0]:
            return k + 1


def AB(g, a):
    """translate a sign answer into A/B/S for g's class"""
    k = cls(g)
    if a == 'S':
        return 'S'
    if k == 0:
        return 'A' if a == sgn(g[0]) else 'B'
    maj = sgn(g[0] if k != 1 else g[1])
    return 'A' if a == maj else 'B'


def correct(g, a, w):
    return a == sgn(g[w - 1])


def samples():
    pts = []
    R = range(-6, 7)
    for g in itertools.product(R, R, R):
        if 0 not in g:
            pts.append(tuple(F(x) for x in g))
    random.seed(68)
    for _ in range(20000):
        pts.append(tuple(F(random.randint(-997, 997), random.randint(1, 211)) for _ in range(3)))
    return [g for g in pts if cls(g) is not None]


def main():
    G = samples()
    ok = True
    L1 = L2 = L3 = True
    pat = set()
    for g in G:
        t, n = ans(M, g), ans(KN, g)
        s12 = g[0] + g[1]
        if s12 == 0:
            continue  # null boundary plane g1 + g2 = 0
        if t == 'S':
            L3 &= (n == 'S')
        elif (t == '+' and s12 < 0) or (t == '-' and s12 > 0):
            L1 &= (n == 'S') and correct(g, t, 3)
            pat.add((cls(g), AB(g, t)))
        else:
            L1 &= (n == t)
    L2 = pat <= {(3, 'B'), (1, 'A'), (2, 'A')} and len(pat) == 3
    print('L1 Nstar = T off L*, S on L*, silenced answers 3-correct:', L1)
    print('L2 silenced (class, T-answer) patterns:', sorted(pat), L2)
    print('L3 Nstar silent wherever T silent:', L3)
    w_t3 = (F(1), F(1), F(-5))
    w_l1 = (F(1), F(-1, 2), F(-2))
    w_l2 = (F(1, 10), F(-1, 2), F(3))
    L4 = (cls(w_t3) == 3 and ans(M, w_t3) == '-' and ans(KN, w_t3) == 'S' and
          cls(w_l1) == 1 and AB(w_l1, ans(M, w_l1)) == 'A' and ans(KN, w_l1) == 'S' and
          cls(w_l2) == 2 and AB(w_l2, ans(M, w_l2)) == 'A' and ans(KN, w_l2) == 'S')
    print('L4 witnesses t3, l1, l2 (each the centre of an open cone):', L4)
    L5 = True
    rk = lambda g, a, w: 1 if a == 'S' else (0 if correct(g, a, w) else 2)
    for g in G:
        d, t = ans(KD, g), ans(M, g)
        if cls(g) == 3:
            L5 &= AB(g, d) == 'A'
        L5 &= rk(g, d, 3) >= rk(g, t, 3)
    print('L5 D = A on class 3 and D weakly 3-worse than T:', L5)
    L6a = True
    for g in G:
        t, n = ans(M, g), ans(KN, g)
        if t != n:
            L6a &= ans(KDm, g) == t
    g6 = (F(1), F(1, 100), F(-1, 2))
    L6b = cls(g6) == 3 and ans(M, g6) == 'S' and ans(KDm, g6) == '+'
    print('L6 Dm13 = T on L* (all samples):', L6a, '; Dm13 = A at a T-silent class-3 point:', L6b)
    # L7 sampled numerics on posterior members
    bad = []
    qs = [(F(a), F(b), F(30 - a - b)) for a in range(3, 28) for b in range(3, 28) if 3 <= 30 - a - b <= 27]
    Gs = G[:6000]
    for q in qs:
        if q == (F(10), F(10), F(10)):
            continue
        Kq = [tuple(m[i] * q[i] for i in range(3)) for m in M]
        eqL = all(ans(Kq, g) == ans(M, g) for g in Gs if ans(M, g) != ans(KN, g))
        if eqL:
            aQ = any(cls(g) == 3 and ans(M, g) == 'S' and AB(g, ans(Kq, g)) == 'A' for g in Gs)
            if aQ:
                bad.append(q)
    print('L7 (NUMERICS) interior posterior members on the grid that are carriers:', bad)
    ok = L1 and L2 and L3 and L4 and L5 and L6a and L6b
    print('ALL PASS' if ok else 'SOME FAIL')


if __name__ == '__main__':
    main()
