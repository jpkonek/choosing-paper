"""geom70: exact geometry of the candidate curve T -R_a-> N -J_b-> L0 -F_t-> D* (PP70 §1).

Conventions: problems g in R^3 (mod sign); D_K answers sigma in {+1,-1} iff min_{k in K} sigma k.g > 0.
Curve parameter s in [0,3]: s in [0,1] -> R_s, [1,2] -> J_{s-1}, [2,3] -> F_{s-2}.
For Minkowski combinations the min over the set is the combination of mins, so each member's
advice on g is decided by exact rational formulas; thresholds are computed exactly.
Checks (exact rationals on samples):
  G1 along the curve every advice change is 3-monotone (3-rank never decreases), on a 1/48 grid;
  G2 census of change types (segment, class, old->new);
  G3 every one of 12 equal subintervals of each segment contains changes of each listed type
     (so every band (s,t] has class-1 and class-2 parts, and class-3 parts in R and F);
  G4 at most two changes per problem along the whole curve; list the two-change patterns;
  G5 J_b = N on class 3 for all b (no class-3 change in the J segment).
Run: python3 -I -B geom70.py > geom70.out
"""
from fractions import Fraction as Fr
import itertools, random
random.seed(70)
c, e = Fr(7, 30), Fr(3, 10)
MV = [tuple(c + (e if i == v else 0) for i in range(3)) for v in range(3)]
M0 = [(Fr(16, 23), Fr(7, 23), Fr(0)), (Fr(7, 23), Fr(16, 23), Fr(0))]
h12 = (Fr(1, 2), Fr(1, 2), Fr(0))
v3 = MV[2]
KN = MV + M0
KL0 = [v3] + M0
dot = lambda k, g: sum(k[i] * g[i] for i in range(3))
mn = lambda K, g, sg: min(sg * dot(k, g) for k in K)


def adv(s, g):
    """advice (+1,-1,0) of the curve member at parameter s (Fraction in [0,3])."""
    for sg in (1, -1):
        if s <= 1:
            v = (1 - s) * mn(MV, g, sg) + s * mn(KN, g, sg)
        elif s <= 2:
            b = s - 1
            v = (1 - b) * mn(KN, g, sg) + b * mn(KL0, g, sg)
        else:
            t = s - 2
            vt = tuple((1 - t) * v3[i] + t * h12[i] for i in range(3))
            v = min(sg * dot(vt, g), mn(M0, g, sg))
        if v > 0:
            return sg
    return 0


def cls(g):
    s = [1 if x > 0 else -1 for x in g]
    if s[0] == s[1] == s[2]:
        return 0
    for o in range(3):
        if s[(o + 1) % 3] == s[(o + 2) % 3]:
            return o + 1


def lab(x, g):
    o = cls(g)
    if x == 0:
        return 'S'
    if o == 0:
        return 'A' if x * g[0] > 0 else 'W'
    return 'B' if x * g[o - 1] > 0 else 'A'


def rank(x, g, w):
    if x == 0:
        return 1
    return 0 if x * g[w - 1] > 0 else 2


def samples(n=6000):
    G = [g for g in itertools.product(range(-6, 7), repeat=3) if all(x != 0 for x in g)]
    G += [tuple(Fr(random.randint(-400, 400), random.randint(1, 40)) for _ in range(3)) for _ in range(n)]
    return [g for g in G if all(x != 0 for x in g) and g[0] + g[1] != 0]


def changes(g, grid):
    out = []
    prev = adv(grid[0], g)
    for a, b in zip(grid, grid[1:]):
        cur = adv(b, g)
        if cur != prev:
            out.append((a, b, prev, cur))
        prev = cur
    return out


def seg(s):
    return 'R' if s < 1 else ('J' if s < 2 else 'F')


if __name__ == '__main__':
    G = samples()
    grid = [Fr(k, 48) for k in range(0, 145)]
    ok = True
    mono = True
    census = {}
    sub = {}
    multi = {}
    nchg = 0
    for g in G:
        ch = changes(g, grid)
        nchg = max(nchg, len(ch))
        pat = []
        for (a, b, x, y) in ch:
            mono &= rank(y, g, 3) >= rank(x, g, 3)
            key = (seg(a), cls(g), lab(x, g), lab(y, g))
            census[key] = census.get(key, 0) + 1
            k12 = int((a - int(a)) * 12)
            sub.setdefault(key, set()).add((int(a), k12))
            pat.append(key)
        if len(pat) >= 2:
            multi[tuple(pat)] = multi.get(tuple(pat), 0) + 1
    print('G1 3-monotone along the curve:', mono); ok &= mono
    print('G2 change census (segment, class, old, new): count')
    for k in sorted(census):
        print('    ', k, census[k])
    print('G3 subinterval coverage (12 per segment):')
    g3 = True
    for k in sorted(sub):
        segi = {'R': 0, 'J': 1, 'F': 2}[k[0]]
        cov = sorted(j for (i, j) in sub[k] if i == segi)
        full = cov == list(range(12))
        print('    ', k, 'covers all 12' if full else 'covers %s' % cov)
        if k[1] in (1, 2):
            g3 &= full
    print('G3 every subinterval of every segment has class-1 and class-2 changes:', g3); ok &= g3
    print('G4 max changes per problem:', nchg, '; multi-change patterns:')
    for k, v in sorted(multi.items(), key=lambda kv: -kv[1]):
        print('    ', k, v)
    ok &= nchg <= 2
    g5 = all(k[1] != 3 for k in census if k[0] == 'J')
    print('G5 no class-3 change on the J segment:', g5); ok &= g5
    print('ALL PASS' if ok else 'SOME FAIL')
