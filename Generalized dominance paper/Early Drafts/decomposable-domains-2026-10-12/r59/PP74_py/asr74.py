"""asr74: exact cell-level test of PP74's ASR admissibility (U1)+(N1)+(U2) for H-repairs.

Own code; geometry conventions of PP75 geo75 (chart h1+h2+h3 = 1, T = D_M, v^a = (7,7,7)+9e_a).
A coherent model is given by a list of vertices K (positive 3-vectors, scale irrelevant):
D_K answers 'h' at h iff k.h > 0 for all k in K, '-h' iff all < 0, else 'S'.
Posterior C_m: K = {m o v^a}.  Vertex-wise rescaling C(m1,m2,m3): K = {m_a o v^a} (coherent, escape family).

Atoms are the open cells of the joint line arrangement of every model involved, so every model is
constant on every atom and all set conditions below are exact for rivals that are unions of atoms.
"""
import sys, os, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'PP75_py'))
from fractions import Fraction as F
from geo75 import COORD, cells as _cells, rank, htype

V = [(16, 7, 7), (7, 16, 7), (7, 7, 16)]

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
    assert all(x != 0 for x in vals), (K, h)
    return 'S'

def atoms(models):
    """models: dict name -> K.  Returns list of atoms {'h', 'vals'} on mixed problems only
    (unanimous problems: every interior model answers the positive gamble; omitted)."""
    L = []
    for K in models.values():
        L += lines(K)
    out = []
    for c in _cells([], extra_lines=L):
        h = c['pt']
        if any(x == 0 for x in h):
            continue
        t = htype(h)
        if t[0] == 'U':
            continue
        out.append({'h': h, 'type': t, 'vals': {n: ans(K, h) for n, K in models.items()}})
    return out

def ble(a, b, h, w): return rank(a, h, w) <= rank(b, h, w)
def blt(a, b, h, w): return rank(a, h, w) < rank(b, h, w)

def weakly_worse(At, P, Q, w):
    """P pointwise weakly w-worse than Q (P <|_w Q)"""
    return all(ble(a['vals'][Q], a['vals'][P], a['h'], w) for a in At)

def asr(At, X, B, committed):
    """ASR admissibility of defender B for rival X (both given as per-atom value lists).
    Returns dict: N1, U1 (per committed), affected {(C,w)}, anchors {(C,w): [v]}, ok."""
    n = len(At)
    H = [a['h'] for a in At]
    rep = {}
    rep['N1'] = all(any(blt(B[i], X[i], H[i], w) for i in range(n)) for w in range(3))
    U1 = {}
    for c, C in committed.items():
        D = [i for i in range(n) if C[i] != X[i]]
        U1[c] = (len(D) == 0) or any(B[i] != X[i] for i in D)
    rep['U1'] = U1
    aff, anc = [], {}
    for c, C in committed.items():
        for w in range(3):
            Smax = [i for i in range(n) if C[i] != B[i] and ble(X[i], C[i], H[i], w)]
            bet = [i for i in range(n) if blt(B[i], X[i], H[i], w)]
            if not Smax or not set(bet) <= set(Smax):
                continue
            # Y_S := B[S -> C] must differ from X for some admissible S (Bet <= S <= Smax)
            YS = lambda S: [C[i] if i in S else B[i] for i in range(n)]
            if YS(set(Smax)) == list(X) and YS(set(bet)) == list(X):
                continue
            aff.append((c, w))
            vs = [v for v in range(3) if v != w and all(ble(C[i], B[i], H[i], v) for i in range(n))]
            anc[(c, w)] = vs
    rep['affected'] = aff
    rep['anchors'] = anc
    rep['ok'] = rep['N1'] and all(U1.values()) and all(anc[k] for k in aff)
    return rep

def inH(At, m, base='T'):
    """model m in H relative to the atoms' R: answers only h/S and agrees with base where base is
    not in R (R = atoms where some member of the (2V) census differs from base)."""
    return all(a['vals'][m] in ('h', 'S') for a in At)
