"""REFEREE54: the alpha-certificates of PP61 section 4.2 / 6, re-derived pointwise.

A refusal requirement "S refuses S <=_i X" has increment d(g) = u1_i(g, X(g)) - u1_i(g, S(g)); a common weight q
certifies it iff int q d < 0.  alpha >= 0, alpha != 0 with sum alpha_k d_k >= 0 a.e. excludes every q.
On the instance every d is |g| times an integer vector per atom, so the pointwise test is a per-atom test.
The u^1 increments are taken from PP56's field (atom.phi) AND recomputed from the closed formula on R
(phi(h) - phi(S) = -|Wr| at Cor worlds, +|Cor| at Wr worlds), and the two are compared.
"""
import sys, os, pickle
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
P61 = os.path.join(HERE, '..', 'PP61_py')
sys.path.insert(0, P61)
sys.path.insert(0, os.path.join(HERE, '..', 'PP56_py'))
import inst61  # noqa: F401
VALS = ('P', 'M', 'S', 'C')

inst, kinds, enc = pickle.load(open(os.path.join(P61, 'enc61_G3.pkl'), 'rb'))
val = pickle.load(open(os.path.join(P61, 'E2_G3.pkl'), 'rb'))
names0, M0 = enc.mat['base']


def own_incr(p, x, y):
    """closed-form u^1 increment for an h/S change on a mixed-sign atom (None if not of that kind)."""
    g = inst.atoms[p].ray
    vx, vy = VALS[x], VALS[y]
    if {vx, vy} not in ({'P', 'S'}, {'M', 'S'}):
        return None
    h = 'P' if 'P' in (vx, vy) else 'M'
    sgn = [(1 if gw > 0 else -1) * (1 if h == 'P' else -1) for gw in g]
    cor = [w for w in range(3) if sgn[w] > 0]
    wr = [w for w in range(3) if sgn[w] < 0]
    if not cor or not wr:
        return None
    v = [(-len(wr) if w in cor else len(cor)) for w in range(3)]   # phi(h) - phi(S)
    return tuple(v) if vy == h else tuple(-t for t in v)


def incr(Sname, Xname):
    a, b = names0.index(Sname), names0.index(Xname)
    xs, xx = inst.models[Sname], inst.models[Xname]
    out = {}
    for p in range(inst.nbase):
        if xs[p] != xx[p]:
            at = inst.atoms[p]
            d = tuple(at.phi[w][xx[p]] - at.phi[w][xs[p]] for w in range(3))
            own = own_incr(p, xs[p], xx[p])
            assert own is None or own == d, (at.label, own, d)
            out[at.label] = d
    return out, M0[a, b]


def refused(r, i):
    return not val[3 * int(r) + i + 1]


ok = True
# A1 (E2): C_B refuses B[K09.c1 u K11.c1 -> D] at worlds 1 and 3; alpha = (1, 2)
d, r = incr('S:B', 'X:B>D:K09.c1,K11.c1')
s = {k: v[0] + 2 * v[2] for k, v in d.items()}
print('A1 increments', d, '; d1 + 2 d3 per atom', s, '; E2 refuses at 1 and 3:', refused(r, 0) and refused(r, 2))
ok &= all(x == 0 for x in s.values()) and refused(r, 0) and refused(r, 2)
# A4: u refuses u[K10.c1 u K17.c1 u K17.c2 -> B] at world 2 and u[K10.c1 u K17.c2 -> B] at world 1; alpha = (1, 1/2)
d1, _ = incr('S:u', 'X:u>B:K10.c1,K17.c1,K17.c2')
d2, _ = incr('S:u', 'X:u>B:K10.c1,K17.c2')
labs = sorted(set(d1) | set(d2))
comb = {k: d1.get(k, (0, 0, 0))[1] + Fr(1, 2) * d2.get(k, (0, 0, 0))[0] for k in labs}
print('A4 increments', d1, d2, '; d2(r1) + 1/2 d1(r2) per atom', {k: str(v) for k, v in comb.items()})
ok &= all(v >= 0 for v in comb.values()) and any(v != 0 for v in comb.values()) or all(v == 0 for v in comb.values())
# inverse pair at one world: alpha = (1, 1) on any balanced swap (d(r^-) = -d(r) pointwise by (IB))
d, r = incr('S:u', 'X:u>B:K13.c1,K20.c1') if 'X:u>B:K13.c1,K20.c1' in inst.models else (None, None)
print('inverse-pair certificate is the identity d(r) + d(r^-) = 0 (record reversal); nothing to compute')
print('ALPHA RE-CHECK:', 'PASS' if ok else 'FAIL')
