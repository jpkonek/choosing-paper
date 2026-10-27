"""layer74: u1 layer masses along the pure down-shift ray of world 3 at u (NUMERICS: exact cells, float solid angles).
For a standard Gaussian, |g| and g/|g| are independent, so the |g|-mass of a cone is proportional to its solid
angle; we report masses in solid-angle units.  For B_t = C_{u o (3 -> r^j)}:
  alpha = odd-3 layer mass, beta1/beta2 = odd-1/odd-2 layer masses, p = alpha + beta (PP73 Lemma 1.4: beta1 = beta2),
  and the ratio beta/p used in PP74 Lemma 5.3 (window non-empty iff beta(t) >= 2 theta e at the lower end)."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'PP75_py'))
from asr74 import post, lines, ans
from geo75 import cells as _cells, htype
from fractions import Fraction as F

def solid(poly):
    P = [(float(x), float(y), 1 - float(x) - float(y)) for (x, y) in poly]
    cx = sum(p[0] for p in P) / len(P); cy = sum(p[1] for p in P) / len(P); c = (cx, cy, 1 - cx - cy)
    def dot(a, b): return sum(x * y for x, y in zip(a, b))
    def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
    def nrm(a): return math.sqrt(dot(a, a))
    tot = 0.0
    for i in range(len(P)):
        a, b = P[i], P[(i + 1) % len(P)]
        num = abs(dot(c, cross(a, b)))
        den = nrm(c)*nrm(a)*nrm(b) + dot(c, a)*nrm(b) + dot(c, b)*nrm(a) + dot(a, b)*nrm(c)
        tot += 2 * math.atan2(num, den)
    return tot

def main():
  r = F(20, 21)
  T = post((1, 1, 1))
  for j in (1, 2, 3, 4, 6):
    B = post((1, 1, r ** j))
    L = lines(T) + lines(B)
    m = {1: 0.0, 2: 0.0, 3: 0.0}
    for c in _cells([], extra_lines=L):
        h = c['pt']
        if any(x == 0 for x in h): continue
        t = htype(h)
        if t[0] == 'U': continue
        if ans(T, h) != ans(B, h):
            m[t[1] + 1] += solid(c['poly'])
    p = m[3] + m[1]
    print('scale r^%d: alpha=%.5f beta1=%.5f beta2=%.5f  p=%.5f  beta/p=%.3f' % (j, m[3], m[1], m[2], p, m[1] / p))

if __name__ == '__main__':
    main()
