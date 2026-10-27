"""thr70: exact switching thresholds along the curve, by region (PP70 §1).

For each sampled g we compute exactly:
  sigma(g) in (0,1]  : R_a gives T's answer iff a < sigma          (g in L = {T != N})
  beta(g)  in (0,1)  : J_b answers iff b > beta                     (g in {N = S, L0 answers})
  tau(g)   in (0,1)  : F_t answers iff t > tau                      (g in {L0 = S, D* answers})
and report, per region (class, from->to), the range of thresholds and the 12-bin coverage.
Regions are sampled by rejection from a large exact sample, plus targeted samples
for the thin J region (g with g3 large of the minority sign).
Run: python3 -I -B thr70.py > thr70.out
"""
from fractions import Fraction as Fr
import random, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom70 import MV, M0, KN, KL0, v3, h12, dot, mn, cls, lab
random.seed(7070)


def sgn_ans(K, g):
    for sg in (1, -1):
        if mn(K, g, sg) > 0:
            return sg
    return 0


def thresholds(g):
    out = {}
    aT, aN, aL = sgn_ans(MV, g), sgn_ans(KN, g), sgn_ans(KL0, g)
    aD = sgn_ans(M0, g)
    if aT != 0 and aN == 0:          # R segment: T answers, N silent
        sg = aT
        a, b = mn(MV, g, sg), mn(KN, g, sg)
        out['R'] = (lab(sg, g), a / (a - b))
    if aN == 0 and aL != 0:          # J segment
        sg = aL
        b, cc = mn(KN, g, sg), mn(KL0, g, sg)
        out['J'] = (lab(sg, g), b / (b - cc))
    if aL == 0 and aD != 0:          # F segment: v_t.g crosses 0
        sg = aD
        x0, x1 = sg * dot(v3, g), sg * dot(h12, g)
        if x0 <= 0 < x1:
            out['F'] = (lab(sg, g), -x0 / (x1 - x0))
    return out


def rnd():
    return tuple(Fr(random.randint(-600, 600), random.randint(1, 60)) for _ in range(3))


if __name__ == '__main__':
    G = [rnd() for _ in range(60000)]
    # targeted: thin J region lies near M1 with g1>0>g2,g3 and 16g1+7g2 ~ 0
    for _ in range(40000):
        g1 = Fr(random.randint(1, 400), 40)
        g2 = -g1 * Fr(random.randint(2000, 2400), 1000)       # g2/g1 in [-2.4,-2.0] ~ -16/7
        g3 = -Fr(random.randint(1, 4000), 40)
        G.append((g1, g2, g3)); G.append((g2, g1, g3))
    G = [g for g in G if all(x != 0 for x in g)]
    data = {}
    for g in G:
        o = cls(g)
        for segn, (l, th) in thresholds(g).items():
            data.setdefault((segn, o, l), []).append(th)
    ok = True
    for k in sorted(data):
        v = data[k]
        bins = sorted(set(min(11, int(x * 12)) for x in v))
        full = bins == list(range(12))
        print(k, 'n=%d min=%.4f max=%.4f' % (len(v), float(min(v)), float(max(v))),
              'all 12 bins' if full else 'bins %s' % bins)
        ok &= all(0 < x <= 1 for x in v)
    print('thresholds in (0,1]:', ok)
    # R_B points: all later answered A on F?
    rb = [g for g in G if cls(g) == 3 and sgn_ans(MV, g) != 0 and lab(sgn_ans(MV, g), g) == 'B']
    rbF = [thresholds(g).get('F') for g in rb]
    print('R_B samples %d; with an F threshold: %d; F-threshold range on R_B: %s' % (
        len(rb), sum(1 for x in rbF if x), (float(min(x[1] for x in rbF if x)), float(max(x[1] for x in rbF if x)))))
    print('ALL PASS' if ok else 'SOME FAIL')
