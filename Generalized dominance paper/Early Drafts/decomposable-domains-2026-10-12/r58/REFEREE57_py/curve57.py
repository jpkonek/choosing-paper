"""curve57: referee's own implementation of the round-57 curve C_theta and of PP69's field f (tables of PP69 §2.2).
theta in [0,1/3]: K_alpha = (1-alpha)M + alpha K_N (alpha = 3 theta); [1/3,2/3]: (1-beta)K_N + beta K_L0;
[2/3,1]: conv(v_t, M0).  min over a Minkowski combination = combination of mins.  Exact rationals.
"""
import sys
sys.path.insert(0, '.')
from rlib import *

v1, v2, v3 = VM
h12 = (F(1, 2), F(1, 2), F(0))
w1 = (F(16, 23), F(7, 23), F(0)); w2 = (F(7, 23), F(16, 23), F(0))   # M0 = projection of M from e3
KM = [v1, v2, v3]; KN = [v1, v2, v3, w1, w2]; KL0 = [v3, w1, w2]; M0 = [w1, w2]

def mn(K, h): return min(dot(k, h) for k in K)

def fmin(theta, h):
    """min over K_theta of k.h"""
    if theta <= F(1, 3):
        a = 3 * theta
        return (1 - a) * mn(KM, h) + a * mn(KN, h)
    if theta <= F(2, 3):
        b = 3 * theta - 1
        return (1 - b) * mn(KN, h) + b * mn(KL0, h)
    t = 3 * theta - 2
    vt = tuple((1 - t) * v3[i] + t * h12[i] for i in range(3))
    return min(dot(vt, h), mn(M0, h))

def advice(theta, g):
    k = cls(g)
    if k == 0: return 'C'
    m = majsign(g)
    hA = tuple(m * x for x in g); hB = tuple(-x for x in hA)
    if fmin(theta, hA) > 0: return 'A'
    if fmin(theta, hB) > 0: return 'B'
    return 'S'

def roots(h):
    """all theta where fmin(theta,h) crosses 0 (exact, segmentwise linear / min of two linears)"""
    out = []
    # R part: linear in theta on [0,1/3]
    a0, a1 = fmin(F(0), h), fmin(F(1, 3), h)
    if a0 != a1:
        r = -a0 / (a1 - a0) / 3
        if 0 <= r <= F(1, 3): out.append(r)
    b0, b1 = a1, fmin(F(2, 3), h)
    if b0 != b1:
        r = F(1, 3) + (-b0 / (b1 - b0)) / 3
        if F(1, 3) <= r <= F(2, 3): out.append(r)
    # F part: min(vt.h, mn(M0,h)), vt.h linear in t
    c0 = dot(v3, h); c1 = dot(h12, h)
    if c0 != c1:
        t = -c0 / (c1 - c0)
        if 0 <= t <= 1:
            th = F(2, 3) + t / 3
            if mn(M0, h) > 0 or True: out.append(th)
    return sorted(set(out))

def pattern(g):
    """list of (advice, start) along theta in [0,1]: change points exact"""
    k = cls(g)
    m = majsign(g)
    hA = tuple(m * x for x in g); hB = tuple(-x for x in hA)
    cand = sorted(set([F(0), F(1)] + roots(hA) + roots(hB)))
    # evaluate advice on each open interval between candidates (midpoints) and at endpoints
    seq = []
    pts = []
    for i in range(len(cand) - 1):
        pts.append(((cand[i] + cand[i + 1]) / 2, cand[i]))
    for mid, start in pts:
        a = advice(mid, g)
        if not seq or seq[-1][0] != a:
            seq.append((a, start))
    return seq

def thresholds(g):
    seq = pattern(g)
    return [a for a, _ in seq], [s for _, s in seq[1:]]

def delta(t): return 2 * (1 - t) / (2 + t)

def phi(g):
    """PP69 field (per unit |g|) at problem g: dict advice -> (phi1,phi2,phi3), with contradictory 'X'."""
    k = cls(g)
    if k == 0:
        return {'C': (F(-1),) * 3, 'W': (F(1),) * 3}
    if k == 2:
        gs = (g[1], g[0], g[2])     # sigma g is class 1
        ph = phi(gs)
        return {a: (v[1], v[0], v[2]) for a, v in ph.items()}
    advs, th = thresholds(g)
    pat = '>'.join(advs)
    if k == 3:
        if pat == 'S>A':
            t2 = th[0]; A = (-(1 - t2), -(1 - t2), 2 + t2); B = (F(1), F(1), F(-1))
        elif pat == 'A':
            A = (F(-1), F(-1), F(1)); B = (F(1), F(1), F(-1))
        elif pat == 'B>S>A':
            t1, t2 = th; A = (-(1 - t2), -(1 - t2), 2 + t2); B = (1 - t1, 1 - t1, -(2 + t1))
        else:
            raise ValueError('unexpected M3 pattern ' + pat)
    else:  # class 1: phi(A) = (a1,-a2,-a3), phi(B) = (-b1,b2,b3)
        if pat == 'A': a, b = (1, 2, 1), (1, 2, 1)
        elif pat == 'B': a, b = (3, 1, 1), (4, 1, 1)
        elif pat == 'A>S': a, b = (1 + delta(th[0]), 1, 1), (1, 2, 1)
        elif pat == 'A>S>B': a, b = (1 + delta(th[0]), 1, 1), (1 + delta(th[1]), 1, 1)
        elif pat == 'S': a, b = (3, 1, 1), (1, 2, 1)
        elif pat == 'S>B': a, b = (3, 1, 1), (1 + delta(th[0]), 1, 1)
        else:
            raise ValueError('unexpected M1 pattern ' + pat)
        a = tuple(F(x) for x in a); b = tuple(F(x) for x in b)
        A = (a[0], -a[1], -a[2]); B = (-b[0], b[1], b[2])
    S = (F(0),) * 3
    X = tuple(1 + max(A[i], B[i], S[i]) for i in range(3))
    return {'A': A, 'S': S, 'B': B, 'X': X}

def p(theta): return ((2 + theta) / 6, (2 + theta) / 6, (2 - 2 * theta) / 6)
