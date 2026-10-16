#!/usr/bin/env python3
"""P2 / nested_criterion.py (NUMERICS; run with python3 -I)

Checks the nestedness criterion of P2 Lemma 6.1:
  for credal sets M, M' with K' in their interiors and e_i not in M,
  E_i(D_M) is contained in E_i(D_M') (mod null)  iff
    (1) M subset conv(M' u {e_i})  and  (2) M' subset Sh_i(M) := {m in Delta : m in cone(M) - R_+ e_i},
  i.e. iff M and M' have the same two tangent lines from e_i and M' lies radially beyond M
  (both the near and the far boundary) on every ray from e_i.
Monte Carlo: sample gambles h in U = D_{K'} (Gaussian), compute membership in E_i, and compare
with the polygon test.  Also measures, inside a 2-parameter family of triangles near T1, how rare
nested pairs are.
"""
import numpy as np

rng = np.random.default_rng(3)
EPS, S = 0.3, 0.5
u = np.ones(3) / 3
V = np.array([(1 - EPS) * u + EPS * np.eye(3)[k] for k in range(3)])   # vertices of T1
KP = u + S * (V - u)                                                   # K'

def lower(M, H):           # M: (m,3) vertices, H: (N,3) gambles -> min_m m.h
    return (H @ M.T).min(axis=1)

def in_D(M, H):
    return lower(M, H) > 0

N = 400000
H = rng.normal(size=(N, 3))
H = H[lower(KP, H) > 0]                       # gambles of U (one orientation per pair)
mixed = (H.max(1) > 0) & (H.min(1) < 0)
H = H[mixed]

def err(M, i):
    X = in_D(M, H)
    good = H[:, i] > 0
    return (X & ~good) | (~X & good)

def contained(M, Mp, i, tol=2e-4):
    A, B = err(M, i), err(Mp, i)
    return (A & ~B).mean() < tol

def in_hull(P, M, eps=1e-9):
    # P points (k,3) in Delta; M vertices; test via LP-free method for small polygons: use scipy
    from scipy.optimize import linprog
    out = []
    for p in P:
        res = linprog(np.zeros(len(M)), A_eq=np.vstack([M.T, np.ones(len(M))]), b_eq=np.append(p, 1),
                      bounds=[(0, None)] * len(M), method='highs')
        out.append(res.status == 0)
    return np.all(out)

def in_shadow(P, M, i):
    # m in Sh_i(M) iff m = a*x - b*e_i (x in conv M, a>=0, b>=0), m in Delta
    from scipy.optimize import linprog
    e = np.eye(3)[i]
    out = []
    for p in P:
        k = len(M)
        # variables: lambda_1..k >=0 (a = sum lambda), b >= 0 ; p = sum lambda_j M_j - b e
        Aeq = np.hstack([M.T, -e[:, None]])
        res = linprog(np.zeros(k + 1), A_eq=Aeq, b_eq=p, bounds=[(0, None)] * (k + 1), method='highs')
        out.append(res.status == 0)
    return np.all(out)

def criterion(M, Mp, i):
    return in_hull(M, np.vstack([Mp, np.eye(3)[i]])) and in_shadow(Mp, M, i)

def push(M, i, t):
    """radial push away from e_i by factor along rays: m -> e_i + (1+t)(m - e_i), clipped into Delta
    (keeps the tangent lines from e_i)."""
    e = np.eye(3)[i]
    P = e + (1 + t) * (M - e)
    return P

if __name__ == '__main__':
    i = 0
    T = V.copy()
    tests = []
    # (a) radial push of T1 away from e_1 (same tangent lines): should be nested
    for t in [0.05, 0.1, 0.2]:
        Mp = push(T, i, t)
        if Mp.min() < 0: continue
        tests.append(("push T1 from e1 by %.2f" % t, T, Mp))
    # (b) homothety about u (different tangent lines): not nested either way
    for s in [0.95, 1.05]:
        tests.append(("homothety of T1 about u, s=%.2f" % s, T, u + s * (T - u)))
    # (c) conv(T1 u e_1)-type move toward e_1: E_1 shrinks
    tests.append(("T1 -> conv(T1, point toward e1)", np.vstack([T, (0.6 * T[0] + 0.4 * np.eye(3)[0])]), T))
    # (d) translation of T1 (generic): crossing
    tests.append(("translate T1 by (0.02,-0.01,-0.01)", T, T + np.array([0.02, -0.01, -0.01])))
    for name, M, Mp in tests:
        mc = contained(M, Mp, i); cr = criterion(M, Mp, i)
        mc2 = contained(Mp, M, i); cr2 = criterion(Mp, M, i)
        print(f"{name:45s}  E1(M)<=E1(M'): MC {mc!s:5} crit {cr!s:5} | E1(M')<=E1(M): MC {mc2!s:5} crit {cr2!s:5}")
    # (e) 2-parameter family near T1: translates T1 + (a, b, -a-b); count nested pairs at world 1
    grid = [(a, b) for a in np.linspace(-0.03, 0.03, 7) for b in np.linspace(-0.03, 0.03, 7)]
    fam = [T + np.array([a, b, -a - b]) for a, b in grid]
    nest = 0; tot = 0
    for x in range(len(fam)):
        for y in range(len(fam)):
            if x == y: continue
            tot += 1
            nest += criterion(fam[x], fam[y], i)
    print(f"translates of T1 (7x7 grid): nested ordered pairs at world 1: {nest} of {tot}")
