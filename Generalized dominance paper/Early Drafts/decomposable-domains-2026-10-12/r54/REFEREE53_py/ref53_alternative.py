"""REFEREE round 54: the simultaneous-inequality alternative (AUDIT_round54_test §2), checked on finite-atom
instances.  LPs (scipy) only PROPOSE a weight q or a certificate alpha; every claim is then verified exactly in
Fractions.  On finitely many atoms the theorem is Gordan's alternative; the continuum proof is in the report.

 (1) The audit's swap example: increments (-2,1,1) on E+, (2,-1,-1) on E-.  Forward record refused at world 1
     and reverse record refused at world 2: feasible (explicit q).  Both at world 1: alpha = (1,1).
 (2) A cyclic triple d1 = f1 - f2, d2 = f2 - f3, d3 = f3 - f1: every pair is q-feasible, the triple is not
     (alpha = (1,1,1)).  So the obstruction is not pairwise.
 (3) 400 random integer instances (m records, n atoms): each is classified, and the q or the alpha is verified
     exactly.  Exactly one alternative holds in every instance.
"""
import random
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import linprog

random.seed(54)
FAIL = []


def check(c, msg):
    if not c:
        FAIL.append(msg)
        print('FAIL:', msg)


def rat(x, den=10 ** 6):
    return Fr(x).limit_denominator(den)


def verify_q(mass, d, q):
    return all(q_j > 0 for q_j in q) and all(sum(m * qj * dk for m, qj, dk in zip(mass, q, row)) < 0 for row in d)


def verify_alpha(d, alpha):
    if any(a < 0 for a in alpha) or all(a == 0 for a in alpha):
        return False
    n = len(d[0])
    return all(sum(alpha[k] * d[k][j] for k in range(len(d))) >= 0 for j in range(n))


def solve(mass, d):
    """Return ('q', q) or ('alpha', alpha), exactly verified, or ('?', None)."""
    m, n = len(d), len(mass)
    # q-LP: q_j in [1, 1e4], sum_j mass_j q_j d_kj <= -1
    A = np.array([[float(mass[j] * d[k][j]) for j in range(n)] for k in range(m)])
    r = linprog(np.zeros(n), A_ub=A, b_ub=-np.ones(m), bounds=[(1, 1e4)] * n, method='highs')
    if r.status == 0:
        for den in (10 ** 3, 10 ** 6, 10 ** 9):
            q = [rat(x, den) for x in r.x]
            q = [max(x, Fr(1)) for x in q]
            if verify_q(mass, d, q):
                return 'q', q
    # alpha-LP: alpha >= 0, sum alpha = 1, sum_k alpha_k d_kj >= 0 for all j
    Aa = -np.array([[float(d[k][j]) for k in range(m)] for j in range(n)])
    r2 = linprog(np.zeros(m), A_ub=Aa, b_ub=np.zeros(n), A_eq=np.ones((1, m)), b_eq=[1.0],
                 bounds=[(0, None)] * m, method='highs')
    if r2.status == 0:
        for den in (10, 100, 1000, 10 ** 4, 10 ** 6):
            al = [rat(x, den) for x in r2.x]
            if verify_alpha(d, al):
                return 'alpha', al
    return '?', None


# (1) swap example: atoms E+ and E-, unit masses; per-unit level-0 increments of A -> A[F -> S]
inc = {'E+': (-2, 1, 1), 'E-': (2, -1, -1)}
mass = [Fr(1), Fr(1)]
fwd = lambda w: [inc['E+'][w], inc['E-'][w]]            # d for "A refuses A[F->S] at w"
rev = lambda w: [-inc['E+'][w], -inc['E-'][w]]          # d for "B refuses B[F->h] at w" (inverse record)
k1, s1 = solve(mass, [fwd(0), rev(1)])
print('(1) forward refused at world 1, reverse at world 2:', k1, [str(x) for x in s1])
check(k1 == 'q', 'swap example different worlds feasible')
k2, s2 = solve(mass, [fwd(0), rev(0)])
print('    forward and reverse both refused at world 1:', k2, [str(x) for x in s2])
check(k2 == 'alpha' and verify_alpha([fwd(0), rev(0)], [Fr(1), Fr(1)]), 'same-world infeasible, alpha=(1,1)')
# all 9 world assignments
tab = {}
for w in range(3):
    for v in range(3):
        tab[(w + 1, v + 1)] = solve(mass, [fwd(w), rev(v)])[0]
print('    all assignments (forward world, reverse world) -> outcome:', tab)
# expected: feasible iff the two requirements need the same sign of z = q(E+) - q(E-)
for (w, v), out in tab.items():
    sf = -1 if inc['E+'][w - 1] < 0 else 1  # forward needs z * inc_E+ < 0 ... sign of z required
    need_f = 1 if inc['E+'][w - 1] < 0 else -1
    need_r = 1 if -inc['E+'][v - 1] < 0 else -1
    check((out == 'q') == (need_f == need_r), f'swap table {(w, v)}')

# (2) cyclic triple on 3 atoms
f = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]   # f_i = indicator of atom i
dcyc = [[f[0][j] - f[1][j] for j in range(3)], [f[1][j] - f[2][j] for j in range(3)],
        [f[2][j] - f[0][j] for j in range(3)]]
mass3 = [Fr(1), Fr(2), Fr(3)]
pair_ok = all(solve(mass3, [dcyc[i], dcyc[j]])[0] == 'q' for i in range(3) for j in range(i + 1, 3))
kt, st = solve(mass3, dcyc)
print('(2) cyclic triple: every pair feasible:', pair_ok, '; triple:', kt, [str(x) for x in st])
check(pair_ok and kt == 'alpha', 'cyclic triple')

# (3) random instances
counts = {'q': 0, 'alpha': 0, '?': 0}
for _ in range(400):
    m, n = random.randint(2, 5), random.randint(2, 6)
    massr = [Fr(random.randint(1, 5)) for _ in range(n)]
    d = [[random.randint(-4, 4) for _ in range(n)] for _ in range(m)]
    kind, sol = solve(massr, d)
    counts[kind] += 1
    if kind == 'q':  # the alternative must then fail: no alpha (check by the easy direction on the q found)
        pass
    if kind == 'alpha':
        # exactly verified certificate; the easy direction then rules out every q
        pass
check(counts['?'] == 0, 'every random instance classified exactly')
print('(3) random instances: q-feasible', counts['q'], ' alpha-certified', counts['alpha'], ' unresolved', counts['?'])
print('ALL PASS' if not FAIL else f'{len(FAIL)} FAILURES')
