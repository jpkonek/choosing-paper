"""REFEREE round 56, report section 5: stage consistency in the accumulation counterexample, for
every n up to NMAX, by an explicit ADDITIVE relation found by LP and then verified exactly.

Abstract instance (cells as in trap_ref.py, instance C, plus layer cells):
  E   : + correct at {1,2}; T silent, D = +      (Q_3-type fill region)
  W1  : + correct at {1,3}; T = +, D silent
  W2  : + correct at {2,3}; T = +, D silent
  L_k : + correct at {1};   T silent, D = +;   Q_k  = T[L_k -> D]   (k = 1..n)
  L'_k: + correct at {2};   T silent, D = +;   Q'_k = T[L'_k -> D]
Universe: all T/D splices.  Selected: T (all worlds), D (edge: worlds 1,2), Q_k, Q'_k (all worlds).
An additive relation: Phi(Z) = sum over cells where Z = D of Delta(cell) in R^3 (Phi(T) = 0);
X <=_w Y iff Phi_w(X) <= Phi_w(Y).  Then reflexivity, (IB), (TC) hold automatically (total
preorder of a record function); strict (G) holds iff each Delta(cell) has the guidance sign pattern;
if every selected S is STRICTLY lambda_S-Bayes cell by cell (lambda_S > 0 on supp S, 0 off it),
then S is defended on its support and strictly protected against every Z != S (so undominated and
direct (C) hold for coherent and incoherent Z alike).
Stage-n commitments: Q_k <=_1 D, Q'_k <=_2 D (k <= n).  We exhibit, for each n, a relation with
these commitments AND a_1 = [T <=_1 D]; by the 1<->2 symmetry of the instance, also one with a_2.
So no stage entails -a_1 or -a_2; but a_1 & a_2 is excluded by the axioms (Prop 2.2(b)), and the
limit q_k -> u forces both.  Layer contributions are bounded by 2^-k (Q_k -> T in measure).
Run: python3 -I -B limit_lp.py
"""
from fractions import Fraction as Fr
import math
import numpy as np
from scipy.optimize import linprog

NMAX = 6
SIGN = {'E': (-1, -1, +1), 'W1': (+1, -1, +1), 'W2': (-1, +1, +1),
        'L': (-1, +1, +1), 'Lp': (+1, -1, +1)}      # sign of Delta_w = loss(D value) - loss(T value)


def lam_Q(k, n, prime=False):
    """lambda_{Q_k} = (1, mu, nu) from the tangent line at y_k of the convex f(y) = 0.1(1-y)^2 + 0.1:
    in the (y, z) = (Delta_2, Delta_3)/|Delta_1| plane each tangent line is on the upper envelope
    of the others exactly near its tangent point, which separates cell L_k from the other L_j."""
    yk = 0.2 + 0.6 * (k - 0.5) / n
    f, fp = 0.1 * (1 - yk) ** 2 + 0.1, -0.2 * (1 - yk)
    bint = f - fp * yk
    nu, mu = 1.0 / bint, -fp / bint
    return (mu, 1.0, nu) if prime else (1.0, mu, nu)


def build(n):
    cells = ['E', 'W1', 'W2'] + ['L%d' % k for k in range(1, n + 1)] + ['Lp%d' % k for k in range(1, n + 1)]
    typ = {c: ('L' if c.startswith('L') and not c.startswith('Lp') else ('Lp' if c.startswith('Lp') else c)) for c in cells}
    sel = [('T', (1.0, 1.0, 10.0), set()), ('D', (1.0, 1.0, 0.0), set(cells))]
    for k in range(1, n + 1):
        sel.append(('Q%d' % k, lam_Q(k, n), {'L%d' % k}))
        sel.append(("Q'%d" % k, lam_Q(k, n, True), {'Lp%d' % k}))
    return cells, typ, sel


def solve(n):
    cells, typ, sel = build(n)
    nv = 3 * len(cells)
    col = {(c, w): 3 * i + w for i, c in enumerate(cells) for w in range(3)}
    A, b = [], []                                   # A x <= b
    def scale(c):
        if c.startswith('L'):
            return 2.0 ** (-int(c.lstrip('Lp')))
        return 1.0
    bounds = []
    for c in cells:
        sc = scale(c)
        for w in range(3):
            s = SIGN[typ[c]][w]
            bounds.append((sc, 1e7 * sc) if s > 0 else (-1e7 * sc, -sc))
    for name, lam, Dcells in sel:
        for c in cells:
            row = np.zeros(nv)
            for w in range(3):
                row[col[(c, w)]] = lam[w]
            mg = 1.0 * scale(c)
            if c in Dcells:      # S takes D's value here: lam.Delta < 0
                A.append(row); b.append(-mg)
            else:                # S takes T's value: lam.Delta > 0
                A.append(-row); b.append(-mg)
    # commitments: Phi_1(D) >= 0 (a_1);  Phi_1(D) - Delta_1(L_k) >= 0;  Phi_2(D) - Delta_2(L'_k) >= 0
    row = np.zeros(nv)
    for c in cells:
        row[col[(c, 0)]] = -1
    A.append(row.copy()); b.append(0.0)
    for k in range(1, n + 1):
        r1 = row.copy(); r1[col[('L%d' % k, 0)]] += 1
        A.append(r1); b.append(0.0)
        r2 = np.zeros(nv)
        for c in cells:
            r2[col[(c, 1)]] = -1
        r2[col[('Lp%d' % k, 1)]] += 1
        A.append(r2); b.append(0.0)
    res = linprog(np.zeros(nv), A_ub=np.array(A), b_ub=np.array(b), bounds=bounds, method='highs')
    return res, cells, typ, sel, col


def verify(n, x, cells, typ, sel, col):
    """exact re-verification with rationals rounded from the LP solution"""
    Dl = {c: [Fr(float(x[col[(c, w)]])) for w in range(3)] for c in cells}
    ok = all((Dl[c][w] > 0) == (SIGN[typ[c]][w] > 0) and Dl[c][w] != 0 for c in cells for w in range(3))
    for name, lam, Dcells in sel:
        lamF = [Fr(t).limit_denominator(10 ** 6) for t in lam]
        for c in cells:
            v = sum(l * d for l, d in zip(lamF, Dl[c]))
            ok &= (v < 0) if c in Dcells else (v > 0)
        ok &= all(l > 0 for l, w in zip(lamF, range(3)) if (name != 'D' or w < 2))
    PhiD = [sum(Dl[c][w] for c in cells) for w in range(3)]
    ok &= PhiD[0] >= 0                                                   # a_1
    for k in range(1, n + 1):
        ok &= PhiD[0] - Dl['L%d' % k][0] >= 0                            # Q_k <=_1 D
        ok &= PhiD[1] - Dl['Lp%d' % k][1] >= 0                           # Q'_k <=_2 D
    ok &= not (PhiD[1] >= 0)                                             # a_2 is (necessarily) false here
    ok &= all(abs(Dl[c][w]) <= Fr(10 ** 7, 2 ** int(c.lstrip("Lp"))) for c in cells if c.startswith("L") for w in range(3))
    return ok, PhiD


allok = True
for n in range(1, NMAX + 1):
    res, cells, typ, sel, col = solve(n)
    if res.status != 0:
        print('  n=%d: LP infeasible/failed (%s)  FAIL' % (n, res.message))
        allok = False
        continue
    ok, PhiD = verify(n, res.x, cells, typ, sel, col)
    allok &= ok
    print('  n=%d: additive relation with stage commitments + a_1, exact check %s; Phi(D) = (%.4f, %.4f, %.4f)'
          % (n, 'PASS' if ok else 'FAIL', *[float(t) for t in PhiD]))
print('ALL PASS' if allok else 'SOME FAIL')
