"""lib79: exact cell model for PP79 (adversary, round 60).  Own code; Fractions only.

Chart h1+h2+h3 = 1 (PP75 convention).  A coherent model is D_K for a finite set K of positive
3-vectors: answer 'h' iff k.h > 0 for all k, '-h' iff k.h < 0 for all k, else 'S'.
T = D_M with vertices v^a = (7,7,7) + 9 e_a.  Posterior C_m: K = {m o v^a}.
Atoms = open cells of the joint line arrangement (coordinate lines + every vertex line of every
model involved), each split into two radial HALVES (index 0/1).  Every coherent model is constant on
a cell, so it takes the same value on both halves; a splice may take different values on the halves,
which is the exact finite shadow of a radially non-conic set.
"""
import sys, os, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'PP75_py'))
from fractions import Fraction as F
from geo75 import cells as _cells, htype, COORD

V = [(16, 7, 7), (7, 16, 7), (7, 7, 16)]
VALS = ('h', 'S', '-h')

def post(m):
    return [tuple(F(m[i]) * v[i] for i in range(3)) for v in V]

def vwise(ms):
    return [tuple(F(ms[a][i]) * V[a][i] for i in range(3)) for a in range(3)]

def lines(K):
    return [(k[0] - k[2], k[1] - k[2], k[2]) for k in K]

def ans(K, h):
    vals = [sum(k[i] * h[i] for i in range(3)) for k in K]
    if all(x > 0 for x in vals): return 'h'
    if all(x < 0 for x in vals): return '-h'
    return 'S'

def rank(a, h, w):
    if a == 'S': return 1
    if a == 'C': return 3
    if a == 'h': return 0 if h[w] > 0 else 2
    if a == '-h': return 0 if h[w] < 0 else 2
    raise ValueError(a)

def le(a, b, h, w):   # a weakly better than b at w
    return rank(a, h, w) <= rank(b, h, w)

def lt(a, b, h, w):   # a strictly better than b at w
    return rank(a, h, w) < rank(b, h, w)

def odd(h):
    t = htype(h)
    return t[1]

def atoms(models):
    """models: dict name -> K.  Atoms on mixed problems only (unanimous problems: every coherent
    model answers h there, correct at all worlds; they never enter a support)."""
    L = []
    for K in models.values():
        L += lines(K)
    out = []
    for ci, c in enumerate(_cells([], extra_lines=L)):
        h = c['pt']
        if any(x == 0 for x in h):
            continue
        t = htype(h)
        if t[0] == 'U':
            continue
        vals = {n: ans(K, h) for n, K in models.items()}
        for half in (0, 1):
            out.append({'h': h, 'type': t, 'o': t[1], 'cell': ci, 'half': half, 'vals': dict(vals)})
    return out

# ---------------------------------------------------------------- refusal families (PP76 Thm 1.1)
def options(C, B, X, h, w):
    """per-atom options for a rival Z of carrier C refused at w by the accepted record rec(B -> X):
    list of (value, strict_flag).  Theorem 1.1 of PP76, pointwise form."""
    opts = []
    if B != X:   # atom in D
        if le(X, B, h, w):            # stay Z = C: B weakly w-worse than X here
            opts.append((C, lt(X, B, h, w)))
        if C != B and le(X, C, h, w):  # take Z = B: C weakly w-worse than X here
            opts.append((B, lt(X, C, h, w)))
    else:
        opts.append((C, False))
        for n in VALS:
            if lt(n, C, h, w):
                opts.append((n, True))
    return opts

def family(At, Cn, Bn, Xn, w, Xvals=None, Bvals=None):
    """returns per-atom option lists, or None if some atom has none."""
    out = []
    for i, a in enumerate(At):
        C = a['vals'][Cn]
        B = Bvals[i] if Bvals is not None else a['vals'][Bn]
        X = Xvals[i] if Xvals is not None else a['vals'][Xn]
        o = options(C, B, X, a['h'], w)
        if not o:
            return None
        out.append(o)
    return out

def affected(At, Cn, w, Bvals, Xvals):
    fam = family(At, Cn, None, None, w, Xvals=Xvals, Bvals=Bvals)
    if fam is None: return False
    return any(s for o in fam for (v, s) in o)

def mixed_available(At, Cn, w, Bvals, Xvals):
    """is some refused rival at w (from this record) strictly w-WORSE than C somewhere?
    (then the refusal is mixed: the rival is also strictly w-better somewhere, by strictness, or
    it would contradict strict (G) -- we report both flags)"""
    fam = family(At, Cn, None, None, w, Xvals=Xvals, Bvals=Bvals)
    if fam is None: return None
    worse_atoms = [i for i, o in enumerate(fam)
                   if any(lt(At[i]['vals'][Cn], v, At[i]['h'], w) for (v, s) in o)]
    strict_atoms = [i for i, o in enumerate(fam) if any(s for (v, s) in o)]
    if not strict_atoms: return None   # not affected
    if not worse_atoms: return False
    # need a joint choice: worse somewhere and strict somewhere
    if any(i != j for i in worse_atoms for j in strict_atoms): return True
    i = worse_atoms[0]
    return any(s and lt(At[i]['vals'][Cn], v, At[i]['h'], w) for (v, s) in fam[i])

def N1(At, Bvals, Xvals):
    return all(any(lt(Bvals[i], Xvals[i], a['h'], w) for i, a in enumerate(At)) for w in range(3))

def corr(At, Zn, Bvals, Xvals):
    """generalised agreement obstruction (PP76 Lemma 1.3): committed Z must differ from X on a
    non-null part of D = {B != X}"""
    return any(Bvals[i] != Xvals[i] and a['vals'][Zn] != Xvals[i] for i, a in enumerate(At))
