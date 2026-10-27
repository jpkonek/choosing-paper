"""offarc70: Bayes acts of PP69's field at weights OFF the arc, and a coherence test (PP70 §2.7).
Independent implementation of PP69 §2.2's tables (patterns and thresholds from thr70/geom70).
For a weight lam, the Bayes act X_lam(g) = argmin_{A,B,S} lam.phi(g, .).
Coherence test on a sample: K* := {k in simplex : sig(g) k.g >= 0 for every answered sample g};
X is incoherent if K* is empty or some SILENT sample g0 has k.g0 of one strict sign on all of K*
(then every coherent model with X's answers answers at g0).  LP in floats: NUMERICS.
Control: on-arc weights p(theta) must pass (their Bayes act is C_theta, coherent).
Run: python3 -I -B offarc70.py > offarc70.out
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from geom70 import MV, M0, KN, KL0, cls, lab
from thr70 import thresholds, sgn_ans
import numpy as np
from scipy.optimize import linprog
random.seed(7071)


def delta(t):
    return 2 * (1 - t) / (2 + t)


def phi(g):
    """dict advice-label -> 3-vector (world 1,2,3), PP69 §2.2; labels 'A','B','S' relative to class."""
    o = cls(g)
    if o == 0:
        return None
    th = thresholds(g)
    aT = lab(sgn_ans(MV, g), g)
    t1 = th['R'][1] / 3 if 'R' in th else None
    t2 = None
    if 'J' in th:
        t2 = (1 + th['J'][1]) / 3
    if 'F' in th:
        t2 = (2 + th['F'][1]) / 3
    if o == 3:
        if aT == 'S':
            A, B = (-(1 - t2), -(1 - t2), 2 + t2), (1, 1, -1)
        elif aT == 'A':
            A, B = (-1, -1, 1), (1, 1, -1)
        else:
            A, B = (-(1 - t2), -(1 - t2), 2 + t2), (1 - t1, 1 - t1, -(2 + t1))
        return {'A': A, 'B': B}
    # classes 1, 2: build in class-1 coordinates (odd world first), then permute
    if aT == 'A' and t1 is None:
        a, b = (1, 2, 1), (1, 2, 1)
    elif aT == 'B':
        a, b = (3, 1, 1), (4, 1, 1)
    elif aT == 'A' and t2 is None:
        a, b = (1 + delta(t1), 1, 1), (1, 2, 1)
    elif aT == 'A':
        a, b = (1 + delta(t1), 1, 1), (1 + delta(t2), 1, 1)
    elif t2 is None:
        a, b = (3, 1, 1), (1, 2, 1)
    else:
        a, b = (3, 1, 1), (1 + delta(t2), 1, 1)
    A = (a[0], -a[1], -a[2]); B = (-b[0], b[1], b[2])
    if o == 2:                                     # odd world 2: swap worlds 1 and 2
        A = (A[1], A[0], A[2]); B = (B[1], B[0], B[2])
    return {'A': A, 'B': B}


def bayes(g, lam):
    o = cls(g)
    if o == 0:
        return 1 if g[0] > 0 else -1               # correct answer
    ph = phi(g)
    vals = {'S': 0.0, 'A': sum(l * float(x) for l, x in zip(lam, ph['A'])),
            'B': sum(l * float(x) for l, x in zip(lam, ph['B']))}
    best = min(vals, key=vals.get)
    if best == 'S':
        return 0
    sB = 1 if g[o - 1] > 0 else -1
    return sB if best == 'B' else -sB


def coherent_test(G, adv):
    ans = [(np.array([float(x) for x in g]), a) for g, a in zip(G, adv) if a != 0]
    sil = [np.array([float(x) for x in g]) for g, a in zip(G, adv) if a == 0]
    A_ub = np.array([-a * gg for gg, a in ans]) if ans else np.zeros((0, 3))
    b_ub = np.zeros(len(ans))
    eq = (np.ones((1, 3)), np.array([1.0]))
    r = linprog(np.zeros(3), A_ub=A_ub, b_ub=b_ub, A_eq=eq[0], b_eq=eq[1], bounds=[(0, 1)] * 3)
    if r.status != 0:
        return 'incoherent (no K)', None
    bad = 0
    for g0 in sil:
        lo = linprog(g0, A_ub=A_ub, b_ub=b_ub, A_eq=eq[0], b_eq=eq[1], bounds=[(0, 1)] * 3)
        hi = linprog(-g0, A_ub=A_ub, b_ub=b_ub, A_eq=eq[0], b_eq=eq[1], bounds=[(0, 1)] * 3)
        if lo.fun > 1e-7 or -hi.fun < -1e-7:
            bad += 1
    return ('coherent on sample' if bad == 0 else 'incoherent'), bad


if __name__ == '__main__':
    G = [tuple(Fr(random.randint(-300, 300), random.randint(1, 30)) for _ in range(3)) for _ in range(500)]
    G = [g for g in G if all(x != 0 for x in g) and g[0] + g[1] != 0]
    tests = [('arc theta=0 (T)', (1/3, 1/3, 1/3)), ('arc theta=0.5', (2.5/6, 2.5/6, 1/6)),
             ('arc theta=0.9', (2.9/6, 2.9/6, 0.2/6)),
             ('off arc (0.40,0.30,0.30)', (0.40, 0.30, 0.30)), ('off arc (0.45,0.35,0.20)', (0.45, 0.35, 0.20)),
             ('off arc (0.30,0.30,0.40)', (0.30, 0.30, 0.40)), ('off arc (0.60,0.20,0.20)', (0.6, 0.2, 0.2)),
             ('off arc (0.50,0.10,0.40)', (0.5, 0.1, 0.4))]
    for name, lam in tests:
        adv = [bayes(g, lam) for g in G]
        verdict, bad = coherent_test(G, adv)
        print('%-28s %-22s silent samples forced to answer: %s' % (name, verdict, bad))
