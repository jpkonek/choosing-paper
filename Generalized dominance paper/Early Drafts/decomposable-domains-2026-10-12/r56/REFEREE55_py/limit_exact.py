"""REFEREE round 56, report section 5 (supersedes the exploratory limit_lp.py): every finite stage
of the accumulation counterexample is consistent, by an EXPLICIT additive relation, exact rationals.

Abstract instance (instance C of trap_ref.py plus layers):
  E    : + correct at {1,2}; T silent, D = +
  W1   : + correct at {1,3}; T = +, D silent
  W2   : + correct at {2,3}; T = +, D silent
  L_k  : + correct at {1};   T silent, D = +;  Q_k  = T[L_k -> D]   (k = 1..n)
  L'_k : + correct at {2};   T silent, D = +;  Q'_k = T[L'_k -> D]
Universe: all T/D splices.  Selected: T (worlds 1,2,3), D (edge: worlds 1,2), Q_k, Q'_k (1,2,3).
Additive relation: Phi(Z) = sum over cells where Z takes D's value of Delta(cell); X <=_w Y iff
Phi_w(X) <= Phi_w(Y).  Reflexivity, (IB), (TC) are automatic (a total preorder of a record function);
strict (G) <=> sign pattern of each Delta(cell); a selected S that is strictly lambda_S-Bayes in every
cell (lambda_S > 0 exactly on supp S) is defended on supp S and strictly protected (so undominated,
and direct (C) holds against coherent and incoherent rivals alike).
Explicit values (delta = 1/100, eps = 1/(100 n^2), kappa = 1, zeta = 1/10, eps_k = k eps,
z_k = zeta + kappa eps_k^2):
  Delta(L_k)  = (-1, 1 - eps_k, z_k),      Delta(L'_k) = (1 - eps_k, -1, z_k)
  lambda(Q_k) = (1, mu_k, nu_k), lambda(Q'_k) = (mu_k, 1, nu_k), with
     nu_k = 1 / (2 kappa eps_k (1 - eps_k) + z_k + kappa eps^2 / 2),  mu_k = 2 kappa eps_k nu_k
     (tangent-line separation on the strictly convex curve z = zeta + kappa e^2)
  Delta(E) = (-delta, -delta, 1),  Delta(W1) = (p, -(p + delta), 1),  Delta(W2) = (-(1 + delta), 1, 1),
     p = 1 + 2 delta + 2 sum_k eps_k   (so Phi_1(D) = sum_k eps_k > 0)
  lambda(T) = (1, 1, 10), lambda(D) = (1, 1, 0).
Stage-n commitments Q_k <=_1 D and Q'_k <=_2 D, and a_1 = [T <=_1 D] (strictly: Phi_1(D) > 0); the mirror relation (1 <-> 2, L <-> L', W1 <-> W2) gives a_2 instead.
Run: python3 -I -B limit_exact.py
"""
from fractions import Fraction as Fr

SIGN = {'E': (-1, -1, 1), 'W1': (1, -1, 1), 'W2': (-1, 1, 1), 'L': (-1, 1, 1), 'Lp': (1, -1, 1)}


def stage(n, tail=0, masses=False):
    """tail > 0: also add the cells L_k, L'_k for k = n+1..n+tail (present in the domain, no member
    selected there yet); masses=True: every layer cell's Delta is scaled by its mass 2^-k and the base
    cells use delta = 2^-n / 100 (so the witness is compatible with Q_k -> T in measure)."""
    delta = Fr(1, 100 * 2 ** n) if masses else Fr(1, 100)
    eps, kappa, zeta = Fr(1, 100 * (n + tail) ** 2), Fr(1), Fr(1, 10)
    Dl, typ, sel = {}, {}, []
    wt = (lambda k: Fr(1, 2 ** k)) if masses else (lambda k: Fr(1))
    K = n + tail
    sum1 = sum(wt(k) * (-1 + (1 - k * eps)) for k in range(1, K + 1)) * 2     # layer contribution to Phi_1
    p = 1 + 2 * delta - sum1
    Dl['E'], Dl['W1'], Dl['W2'] = (-delta, -delta, Fr(1)), (p, -(p + delta), Fr(1)), (-(1 + delta), Fr(1), Fr(1))
    typ.update(E='E', W1='W1', W2='W2')
    sel += [('T', (Fr(1), Fr(1), Fr(10)), set()), ('D', (Fr(1), Fr(1), Fr(0)), None)]
    for k in range(1, K + 1):
        ek = k * eps
        zk = zeta + kappa * ek ** 2
        Dl['L%d' % k], typ['L%d' % k] = tuple(wt(k) * t for t in (Fr(-1), 1 - ek, zk)), 'L'
        Dl['Lp%d' % k], typ['Lp%d' % k] = tuple(wt(k) * t for t in (1 - ek, Fr(-1), zk)), 'Lp'
        if k <= n:
            nu = 1 / (2 * kappa * ek * (1 - ek) + zk + kappa * eps ** 2 / 2)
            mu = 2 * kappa * ek * nu
            sel += [('Q%d' % k, (Fr(1), mu, nu), {'L%d' % k}), ("Q'%d" % k, (mu, Fr(1), nu), {'Lp%d' % k})]
    cells = list(Dl)
    sel[1] = ('D', sel[1][1], set(cells))
    return n, cells, Dl, typ, sel


def check(n, cells, Dl, typ, sel):
    ok = all((Dl[c][w] > 0) == (SIGN[typ[c]][w] > 0) and Dl[c][w] != 0 for c in cells for w in range(3))
    for name, lam, Dcells in sel:
        for c in cells:
            v = sum(l * d for l, d in zip(lam, Dl[c]))
            ok &= (v < 0) if c in Dcells else (v > 0)
        sup = (0, 1) if name == 'D' else (0, 1, 2)
        ok &= all(lam[w] > 0 for w in sup) and all(lam[w] == 0 for w in range(3) if w not in sup)
    Phi = [sum(Dl[c][w] for c in cells) for w in range(3)]
    ok &= Phi[0] >= 0                                                    # a_1: T <=_1 D
    for k in range(1, n + 1):
        ok &= Phi[0] - Dl['L%d' % k][0] >= 0                             # Q_k <=_1 D
        ok &= Phi[1] - Dl['Lp%d' % k][1] >= 0                            # Q'_k <=_2 D
    # consequences that must hold in any such relation: a_2 false, and D defends X_E = T[E->D] at 2
    XE = Dl['E']
    ok &= Phi[1] < 0                                                     # T !<=_2 D
    ok &= not (XE[0] >= Phi[0]) and (XE[1] >= Phi[1])                    # D !<=_1 X_E, D <=_2 X_E
    return ok, Phi


allok = True
for n in list(range(1, 31)) + [50, 100]:
    ok, Phi = check(*stage(n))
    allok &= ok
    if n <= 3 or n in (10, 30, 50, 100):
        print('  n=%3d: explicit additive relation, all axiom clauses + stage commitments + a_1: %s   Phi(D) = (%s, %.5f, %.3f)'
              % (n, 'PASS' if ok else 'FAIL', Phi[0], float(Phi[1]), float(Phi[2])))
print('  n = 1..30, 50, 100 checked exactly (unit layer weights, layer cells k <= n only)')
okm = True
for n in range(1, 13):
    ok, Phi = check(*stage(n, tail=12, masses=True))
    okm &= ok
print('  with masses 2^-k on layers, delta = 2^-n/100, and 12 further unoccupied layer cells per world:'
      ' n = 1..12 %s' % ('PASS' if okm else 'FAIL'))
allok &= okm
print('ALL PASS' if allok else 'SOME FAIL')
