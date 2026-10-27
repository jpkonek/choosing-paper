"""PP61 geometry: sources, cell classes, atoms, exact pure-shift wedges, balanced field u^1.

Setting (BRIEF54): three worlds, eps = 3/10, T = D_M, posterior C_a = D_{M_a}.
Sources G (subset of N); N = conv{B, D, B', D'} with B' = 2u - B, D' = 2u - D (u interior).
(2V) on N: every coordinate of every a in N lies in [373, 427]/1200, ratio 373/427 > 0.7 = 3c,
so 1/a_i >= c * sum_j 1/a_j, i.e. u in M_a, so every C_a answers only with sign(u.g) (PROVED in note).

Cells: open cells of the central arrangement of all source planes + coordinate planes, with u.g > 0
(representative of each antipodal pair; models are odd).  Cells with the same (sign pattern, advice
tuple) are merged into one CLASS: every base model is constant on a class.

Atoms of a disagreement class K (K in R(G)):
   K.c1, K.c2 : two radial slabs of a compact angular core of one geometric cell of K
   K.r        : the rest of K (u.g > 0 side)
   K.n        : the antipodal class -K (ray -g)
Shift s = (a, w): a_t = a o (1 + t e_w).  sigma_s = {C_{a_t} != C_a}, split by class and value.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP56_py'))
from fractions import Fraction as Fr
from itertools import combinations
from pp50_lib_copy import cell_points, advice, mverts
from lex56 import phi_cell
from cells56 import rank

EPS = Fr(3, 10)
U = (Fr(1, 3),) * 3
B = (Fr(406, 1200), Fr(421, 1200), Fr(373, 1200))
D = (Fr(406, 1200), Fr(373, 1200), Fr(421, 1200))
Bp = tuple(2 * U[i] - B[i] for i in range(3))
Dp = tuple(2 * U[i] - D[i] for i in range(3))
G3 = {'u': U, 'B': B, 'D': D}
G5 = {'u': U, 'B': B, 'D': D, 'Bp': Bp, 'Dp': Dp}
VALS = ('P', 'M', 'S', 'C')
CODE = {1: 'P', -1: 'M', 0: 'S'}
TSTAR = Fr(1, 10 ** 5)


def check_2V(G):
    """u in M_a for every listed a and for the whole box [373,427]/1200 (sufficient condition)."""
    c = (1 - EPS) / 3
    ok = Fr(373, 427) >= 3 * c
    for a in G.values():
        inv = [1 / x for x in a]
        ok &= all(v >= c * sum(inv) for v in inv)
        ok &= all(Fr(373, 1200) <= x <= Fr(427, 1200) for x in a)
    return ok


_WEDGE = {}


def self_cname_tmp(geo, k):
    return geo.cname[k]


def sgnv(g):
    return tuple((x > 0) - (x < 0) for x in g)


def classes(G):
    """dict key -> ray, key = (sign pattern, advice tuple over sorted(G)); only u.g > 0, no zero coords."""
    seen = {}
    names = sorted(G)
    for g in cell_points(EPS, {k: list(v) for k, v in G.items()}):
        if any(x == 0 for x in g) or sum(g) <= 0:
            continue
        adv = tuple(CODE[advice(EPS, list(G[k]), g)] for k in names)
        seen.setdefault((sgnv(g), adv), tuple(g))
    return seen


def sig(g):
    """'Maj_j' (h=+g wrong only at j) or 'Min_j' (right only at j) or 'Una'."""
    neg = [w for w in range(3) if g[w] < 0]
    pos = [w for w in range(3) if g[w] > 0]
    if len(neg) == 1:
        return 'Maj%d' % (neg[0] + 1)
    if len(pos) == 1:
        return 'Min%d' % (pos[0] + 1)
    return 'Una'


def field(g):
    """Balanced u^1 field per |g| on R at ray g where the common answer is +g ('P').
    Returns dict value -> tuple over worlds (strictly guiding; P and S lambda-indifferent)."""
    return phi_cell(list(g), ('P', 'S'))


class Geometry:
    def __init__(self, G, tstar=TSTAR, slabs=None):
        self.G = G
        slabs = slabs or {}
        self.names = sorted(G)
        self.cls = classes(G)
        self.keys = sorted(self.cls)
        self.dis = [k for k in self.keys if len(set(k[1])) > 1]
        self.agr = [k for k in self.keys if len(set(k[1])) == 1]
        self.cname = {k: 'K%02d' % i for i, k in enumerate(self.keys)}
        self._wedge_cache = {}
        # atoms
        self.atoms = []          # list of (name, ray, class key, role)
        for k in self.dis:
            g = self.cls[k]
            for role in slabs.get(self_cname_tmp(self, k), ['c1', 'c2']) + ['r']:
                self.atoms.append((self.cname[k] + '.' + role, g, k, role))
            self.atoms.append((self.cname[k] + '.n', tuple(-x for x in g), k, 'n'))
        self.aidx = {a[0]: i for i, a in enumerate(self.atoms)}
        self.tstar = tstar

    def src_value(self, name, atom):
        """value of source `name` on base atom (P/M/S relative to the atom's ray)."""
        nm, g, k, role = atom
        v = k[1][self.names.index(name)]
        if role == 'n':
            return {'P': 'M', 'S': 'S'}[v]
        return v

    def source_model(self, name):
        return tuple(self.src_value(name, a) for a in self.atoms)

    def phi(self, atom_ray):
        """field per value at a ray (P = accept the ray, M = accept minus the ray)."""
        g = atom_ray
        if sum(g) > 0:
            return field(g)
        f = field(tuple(-x for x in g))   # at -g: 'M' here is the common answer +(-g)... relabel
        return {'P': f['M'], 'M': f['P'], 'S': f['S'], 'C': f['C']}

    # ---------------- pure shifts ----------------
    def shifted(self, name, w, t):
        a = self.G[name]
        b = [a[i] * (1 + (t if i == w else 0)) for i in range(3)]
        s = sum(b)
        return tuple(x / s for x in b)

    def shift_wedge(self, name, w):
        key = (tuple(sorted(self.G.items())), name, w, self.tstar)
        if key not in _WEDGE:
            _WEDGE[key] = self._shift_wedge(name, w)
        return _WEDGE[key]

    def _shift_wedge(self, name, w):
        """Exact sigma atoms of shift (name, w) at t = tstar, as a list of
        (class key, side '+'/'-', value of C_{a_t} relative to the side's ray).
        Also returns the stability certificate (chirotope constant on (0, tstar])."""
        t = self.tstar
        at = self.shifted(name, w, t)
        G2 = dict(self.G)
        G2['_t'] = at
        out = set()
        idx = self.names.index(name)
        for g in cell_points(EPS, {k: list(v) for k, v in G2.items()}):
            if any(x == 0 for x in g) or sum(g) <= 0:
                continue
            base = tuple(CODE[advice(EPS, list(self.G[k]), g)] for k in self.names)
            key = (sgnv(g), base)
            vt = CODE[advice(EPS, list(at), g)]
            if vt != base[idx]:
                assert key in self.cls
                out.add((key, '+', vt))
                out.add((key, '-', {'P': 'M', 'S': 'S'}[vt]))
        return sorted(out), self.stability(name, w)

    def stability(self, name, w):
        """PROOF device: the oriented matroid of all normals (base planes, coordinate planes,
        shifted planes m_j o a o (1 + t e_w)) is constant for t in (0, tstar]: no 3x3 determinant
        that is not identically zero has a root in (0, tstar]."""
        import sympy as sp
        T = sp.Symbol('t')
        base = []
        for nm in self.names:
            a = self.G[nm]
            for m in mverts(EPS):
                base.append([sp.Rational(m[j] * a[j]) for j in range(3)])
        base += [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        a = self.G[name]
        shifted = []
        for m in mverts(EPS):
            v = [sp.Rational(m[j] * a[j]) for j in range(3)]
            v[w] = v[w] * (1 + T)
            shifted.append(v)
        allv = [(v, False) for v in base] + [(v, True) for v in shifted]
        bad = 0
        nchecked = 0
        for (x, fx), (y, fy), (z, fz) in combinations(allv, 3):
            if not (fx or fy or fz):
                continue
            d = sp.expand(sp.Matrix([x, y, z]).det())
            if d == 0:
                continue
            p = sp.Poly(d, T)
            # strip powers of t
            while p.eval(0) == 0:
                p = sp.Poly(sp.cancel(p.as_expr() / T), T)
            nchecked += 1
            if p.count_roots(0, sp.Rational(self.tstar)) > 0:
                bad += 1
        return bad == 0, nchecked


if __name__ == '__main__':
    import time
    for label, G in (('G3', G3), ('G5', G5)):
        t0 = time.time()
        geo = Geometry(G)
        print(label, 'sources', geo.names, '(2V) on N:', check_2V(G))
        print('  classes (u.g>0):', len(geo.keys), ' disagreement:', len(geo.dis), ' atoms:', len(geo.atoms))
        ok_all = True
        for nm in geo.names:
            for w in range(3):
                wedge, (stab, nch) = geo.shift_wedge(nm, w)
                # Lemma 4.1: on every sigma atom C_{a_t} strictly better at w than C_a
                better = True
                for key, side, vt in wedge:
                    g = geo.cls[key] if side == '+' else tuple(-x for x in geo.cls[key])
                    va = key[1][geo.names.index(nm)]
                    if side == '-':
                        va = {'P': 'M', 'S': 'S'}[va]
                    better &= rank(vt, list(g), w) < rank(va, list(g), w)
                ok_all &= stab and better
                print('  shift (%s, e_%d): %d sigma atoms (incl. antipodes); chirotope stable on (0,t*]: %s (%d dets); strictly w-better on all: %s'
                      % (nm, w + 1, len(wedge), stab, nch, better))
        print(' ', label, 'ALL PASS' if ok_all else 'FAIL', '(%.1fs)' % (time.time() - t0))
