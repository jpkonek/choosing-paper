"""PP61 exact simultaneous-inequality test (audit; REFEREE_round53 Thm A, Prop A'').

Requirement k: record r_k = rec(C_{a_k} -> X_k) refused at world i_k.  d_k = u^1_{i_k}(X_k) - u^1_{i_k}(C_{a_k})
is |g| times an atom-constant vector, so with w_p := int_p q|g| (any positive vector, q free per atom):
      q certifies all k   iff   exists w > 0 with  sum_p w_p d_k[p] < 0  for all k.
Gordan: infeasible iff exists alpha >= 0, alpha != 0 with sum_k alpha_k d_k[p] >= 0 for every atom p.
Because d_k is constant (per |g|) on each atom and vanishes off the atoms, such an alpha is a POINTWISE
certificate sum_k alpha_k d_k >= 0 a.e. -- an exact obstruction for every q and every tie-break (Prop A'').
All witnesses are verified in exact rational arithmetic.
"""
from fractions import Fraction as Fr
import numpy as np
from itertools import combinations


def dvec(inst, rec, i):
    d = {}
    for (p, x, y) in rec:
        at = inst.atoms[p]
        base = at.parent if at.role == 'minus' else p
        if at.sigma:
            continue                     # infinitesimal: irrelevant for strict base inequalities
        d[base] = d.get(base, 0) + at.phi[i][y] - at.phi[i][x]
    return d


def matrix(inst, reqs):
    """reqs: list of (rec, world).  Returns (atoms list, integer matrix rows = requirements)."""
    ds = [dvec(inst, r, i) for r, i in reqs]
    atoms = sorted(set(p for d in ds for p in d))
    col = {p: j for j, p in enumerate(atoms)}
    D = np.zeros((len(reqs), len(atoms)), dtype=np.int64)
    for k, d in enumerate(ds):
        for p, v in d.items():
            D[k, col[p]] = v
    return atoms, D


def verify_w(D, w):
    return all(w_ > 0 for w_ in w) and all(sum(Fr(int(D[k, j])) * w[j] for j in range(D.shape[1])) < 0 for k in range(D.shape[0]))


def verify_alpha(D, al):
    if not all(a >= 0 for a in al) or not any(a > 0 for a in al):
        return False
    return all(sum(al[k] * int(D[k, j]) for k in range(D.shape[0])) >= 0 for j in range(D.shape[1]))


def small_certificate(D, maxk=3):
    """search exact certificates with support <= maxk (pairs: ratio test; triples: LP on support)."""
    m = D.shape[0]
    for k in range(m):                    # a single row >= 0 pointwise
        if (D[k] >= 0).all() and (D[k] != 0).any() or (D[k] == 0).all():
            al = [Fr(0)] * m
            al[k] = Fr(1)
            if verify_alpha(D, al):
                return al
    for a, b in combinations(range(m), 2):
        lo, hi = Fr(0), None              # alpha = (1, t), t in [lo, hi]
        ok = True
        for j in range(D.shape[1]):
            x, y = int(D[a, j]), int(D[b, j])   # need x + t y >= 0
            if y > 0:
                lo = max(lo, Fr(-x, y))
            elif y < 0:
                bound = Fr(-x, y)
                hi = bound if hi is None else min(hi, bound)
            elif x < 0:
                ok = False
                break
        if ok and (hi is None or lo <= hi):
            al = [Fr(0)] * m
            al[a], al[b] = Fr(1), lo if lo > 0 or hi is None else lo
            if al[b] == 0 and hi is not None and hi > 0:
                al[b] = hi
            if verify_alpha(D, al):
                return al
    if maxk >= 3 and m <= 60:
        for t in combinations(range(m), 3):
            al = alpha_lp(D[list(t)])
            if al is not None:
                full = [Fr(0)] * m
                for idx, k in enumerate(t):
                    full[k] = al[idx]
                if verify_alpha(D, full):
                    return full
    return None


def alpha_lp(D):
    from scipy.optimize import linprog
    m, n = D.shape
    if m == 0:
        return None
    res = linprog(np.zeros(m), A_ub=-D.T.astype(float), b_ub=np.zeros(n), A_eq=np.ones((1, m)), b_eq=[1],
                  bounds=[(0, None)] * m, method='highs')
    if res.status != 0:
        return None
    x = res.x
    for den in (1, 2, 3, 4, 6, 12, 60, 840, 10 ** 4, 10 ** 6):
        al = [Fr(v).limit_denominator(den) if v > 1e-9 else Fr(0) for v in x]
        if verify_alpha(D, al):
            return al
    # exact re-solve on the support
    S = [k for k in range(m) if x[k] > 1e-9]
    sub = alpha_lp(D[S]) if len(S) < m else None
    if sub is not None:
        al = [Fr(0)] * m
        for idx, k in enumerate(S):
            al[k] = sub[idx]
        return al if verify_alpha(D, al) else None
    return None


def w_lp(D):
    from scipy.optimize import linprog
    m, n = D.shape
    if m == 0:
        return [Fr(1)] * n
    res = linprog(np.zeros(n), A_ub=D.astype(float), b_ub=-np.ones(m), bounds=[(1, None)] * n, method='highs')
    if res.status != 0:
        return None
    for den in (1, 10, 1000, 10 ** 6):
        w = [Fr(v).limit_denominator(den) for v in res.x]
        if verify_w(D, w):
            return w
    return None


def test(inst, reqs, want_small=True):
    """returns ('Q', w dict) or ('ALPHA', [(alpha, req)]) -- both exactly verified."""
    atoms, D = matrix(inst, reqs)
    w = w_lp(D)
    if w is not None:
        return 'Q', dict(zip(atoms, w))
    al = small_certificate(D) if want_small else None
    if al is None:
        al = alpha_lp(D)
    assert al is not None and verify_alpha(D, al), 'LP status inconsistent'
    return 'ALPHA', [(a, reqs[k]) for k, a in enumerate(al) if a > 0]
