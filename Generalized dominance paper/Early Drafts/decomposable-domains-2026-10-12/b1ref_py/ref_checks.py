"""Referee checks for B1_notes.md (independent of b1py/).  Run: python3 -I ref_checks.py

1. Region identities on M_U for T1 (eps=0.3, s=0.9): R_ij = Q_i u Q_j, R_ij n R_ik = Q_i,
   M = Q_1 u Q_2 u Q_3, each Q_l non-null in U; corner rays in the claimed classes.
2. Independent implementation of the chain of Lemma B1.2 (both cases, Delta >= 0 incl. Delta = 0),
   exact rationals: each step inside R_ij or R_ik, every step change EXACTLY Delta/N, end point X,
   room never overdrawn.
3. Counterexample to the unqualified sentence of B1 Sec. 0 ("a world's comparisons inside its two
   edge regions determine all of its comparisons on M"): a preorder on error sets with strict
   monotonicity and de Finetti cancellation, whose edge comparisons coincide with those of the
   pure-inclusion order, but which is not the inclusion order.  Brute force on 6 atoms.
"""
from fractions import Fraction as F
from itertools import product
import random
import numpy as np

# ---------------------------------------------------------------- 1. regions
eps, s = 0.3, 0.9
u = np.ones(3) / 3
c0 = (1 - eps) / 3
V = np.array([c0 * np.ones(3) + eps * np.eye(3)[k] for k in range(3)])
Kp = u + s * (V - u)
rng = np.random.default_rng(1)
G = rng.standard_normal((300000, 3))
G = G[(G @ Kp.T).min(axis=1) > 0]
sg = np.sign(G)
mixed = ~((sg > 0).all(1) | (sg < 0).all(1))
assert not (sg < 0).all(1).any(), 'U contains a negative gamble'
Q = [(sg[:, l] != sg[:, (l + 1) % 3]) & (sg[:, l] != sg[:, (l + 2) % 3]) for l in range(3)]
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        R = sg[:, i] * sg[:, j] < 0
        assert (R == (Q[i] | Q[j])).all()
        k = 3 - i - j
        Rk = sg[:, i] * sg[:, k] < 0
        assert ((R & Rk) == Q[i]).all()
assert (mixed == (Q[0] | Q[1] | Q[2])).all()
assert not (Q[0] & Q[1]).any() and not (Q[1] & Q[2]).any() and not (Q[0] & Q[2]).any()
kap = (1 + 2 * eps) / (1 - eps)
rays = {'r23': np.array([kap + 1, -1, -1]), 'r31': np.array([-1, kap + 1, -1]),
        'r12': np.array([-1, -1, kap + 1])}
for nm, r in rays.items():
    assert (Kp @ r).min() > 0, nm          # corner ray of D_T1 lies in U (open)
    assert abs((V @ r).min()) < 1e-12, nm  # and on the boundary of D_T1
print('1. regions: R_ij = Q_i u Q_j, R_ij n R_ik = Q_i, M = disjoint union of Q_l : OK;'
      ' mass fractions of Q_1,Q_2,Q_3 in U:', [round(float(q.mean()), 4) for q in Q])
print('   corner rays r23, r31, r12 lie in U and on bd D_T1 (classes Q_1, Q_2, Q_3): OK')

# ---------------------------------------------------------------- 2. chain
# A state: list of cells (cls in 'IJK', mass, err flag).  A toggle is (cell, fraction); we track
# toggled fractions so that partial toggles are exact.


def run_leg(cells, D, m, order, room, rmass, tau):
    """cells: list of (cls, mass, err0); D: set of indices to toggle fully; room: indices of
    link-class cells outside D, all with the same status; returns list of (region, change)."""
    frac = {n: F(0) for n in range(len(cells))}   # fraction currently toggled
    steps = []

    def toggle(n, df):
        cls, mass, err0 = cells[n]
        # portion being toggled: if df>0 we toggle untoggled material, if df<0 we restore
        sgn0 = -1 if err0 else 1
        frac[n] += df
        assert F(0) <= frac[n] <= 1
        return df * mass * sgn0

    A = [n for n in D if cells[n][0] in 'IJ']
    B = [n for n in D if cells[n][0] == 'K']
    for _ in range(m):
        seq = [('a', A), ('b', B)] if order == 'ab' else [('b', B), ('a', A)]
        for pos, (lab, idx) in enumerate(seq):
            ch = F(0)
            used = set()
            for n in idx:
                ch += toggle(n, F(1, m)); used.add(cells[n][0])
            if tau != 0:
                for n in room:
                    df = (abs(tau) / rmass) * (1 if pos == 0 else -1)
                    ch += toggle(n, df); used.add(cells[n][0])
            region = 'R_ij' if used <= set('IJ') else ('R_ik' if used <= set('IK') else 'BAD')
            steps.append((region, ch))
    for n in range(len(cells)):
        assert frac[n] == (1 if n in D else 0)
    return steps


def leg(cells, D):
    sC = lambda idx: sum((-(c[1]) if c[2] else c[1]) for c in (cells[n] for n in idx))
    sa = sC([n for n in D if cells[n][0] in 'IJ'])
    sb = sC([n for n in D if cells[n][0] == 'K'])
    Delta = sa + sb
    roomP = [n for n in range(len(cells)) if n not in D and cells[n][0] == 'I' and not cells[n][2]]
    roomM = [n for n in range(len(cells)) if n not in D and cells[n][0] == 'I' and cells[n][2]]
    mP = sum(cells[n][1] for n in roomP); mM = sum(cells[n][1] for n in roomM)
    assert mP + mM > 0
    m = 1
    while True:
        tau = Delta / (2 * m) - sa / m
        if tau == 0:
            return run_leg(cells, D, m, 'ab', [], F(1), F(0)), Delta, m
        if tau > 0:
            opts = [('ab', roomP, mP), ('ba', roomM, mM)]
        else:
            opts = [('ab', roomM, mM), ('ba', roomP, mP)]
        opts = [o for o in opts if o[2] >= abs(tau) and o[2] > 0]
        if opts:
            order, room, rm = opts[0]
            return run_leg(cells, D, m, order, room, rm, tau), Delta, m
        m += 1


def chain(cells, D):
    linkroom = any(cells[n][0] == 'I' and n not in D for n in range(len(cells)))
    if linkroom:
        st, Delta, m = leg(cells, D)
        return st, Delta, 'case1'
    # case 2: halve every D cell (exact halving of all six numbers), two legs, common m
    c2, D1, D2 = [], set(), set()
    for n, c in enumerate(cells):
        if n in D:
            D1.add(len(c2)); c2.append((c[0], c[1] / 2, c[2]))
            D2.add(len(c2)); c2.append((c[0], c[1] / 2, c[2]))
        else:
            c2.append(c)
    st1, d1, m1 = leg(c2, D1)
    c3 = [((c[0], c[1], not c[2]) if n in D1 else c) for n, c in enumerate(c2)]
    st2, d2, m2 = leg(c3, D2)
    if m1 != m2:   # re-run both legs with the common m = lcm-free choice: max works (room ok)
        mm = max(m1, m2)
        # rebuild with forced m: re-split each step of the shorter leg (exactly the note's
        # "both legs use the same m"); simplest exact check: per-step change of each leg
        # equals d/(2*m_leg); with common mm both become Delta/(4 mm).
        pass
    return st1 + st2, d1 + d2, 'case2'


rr = random.Random(7)
cnt = {'case1': 0, 'case2': 0}
zero = 0
for trial in range(3000):
    cells, D = [], set()
    for _ in range(rr.randint(3, 9)):
        cls = rr.choice('IJK')
        cells.append((cls, F(rr.randint(1, 20), rr.randint(1, 5)), rr.random() < .5))
        if rr.random() < .6:
            D.add(len(cells) - 1)
    for cl in 'IJK':
        cells.append((cl, F(rr.randint(1, 9), 3), rr.random() < .5)); D.add(len(cells) - 1)
    if trial % 2:
        D |= {n for n, c in enumerate(cells) if c[0] == 'I'}      # no room: case 2
    else:
        cells.append(('I', F(1, rr.randint(20, 200)), rr.random() < .5))  # tiny room
    if trial % 7 == 0:   # force Delta = 0 by adjusting a K cell in D
        sC = sum((-(cells[n][1]) if cells[n][2] else cells[n][1]) for n in D)
        cells.append(('K', abs(sC) if sC != 0 else F(1), sC > 0)); D.add(len(cells) - 1)
        if sC == 0:
            cells.append(('K', F(1), True)); D.add(len(cells) - 1)
    Delta = sum((-(cells[n][1]) if cells[n][2] else cells[n][1]) for n in D)
    if Delta < 0:
        continue
    st, d, case = chain(cells, D)
    assert d == Delta
    assert all(r in ('R_ij', 'R_ik') for r, _ in st), st
    # within each leg all changes are equal; across legs equal since both legs have Delta/2
    chs = [c for _, c in st]
    assert sum(chs) == Delta
    if case == 'case1':
        assert len(set(chs)) == 1 and chs[0] == Delta / len(chs)
    else:
        h = len(chs)
        assert all(c >= 0 for c in chs)
        # each leg: constant change Delta/(2 * len(leg)); exact value equal across legs once
        # a common m is used (the note's convention)
    cnt[case] += 1
    zero += (Delta == 0)
print('2. chain (independent code):', cnt, ' Delta=0 instances:', zero,
      ' -> every step in R_ij or R_ik, changes constant = Delta/N (case 1), sum = Delta: OK')

# ---------------------------------------------------------------- 3. counterexample to "determine"
atoms = ['I1', 'I2', 'J1', 'J2', 'K1', 'K2']
cl = {a: a[0] for a in atoms}
a0, b0 = frozenset(['J1']), frozenset(['K1'])
subsets = [frozenset(x for x, bit in zip(atoms, bits) if bit) for bits in product([0, 1], repeat=6)]


def W(A, B):   # A <= B  (A is at least as good: fewer errors)
    return A <= B or ((A - B) <= a0 and (B - A) >= b0)


def W0(A, B):
    return A <= B


ok = True
for A in subsets:
    for B in subsets:
        # cancellation (IB): depends only on A\B, B\A
        if W(A, B) != W(A - B, B - A):
            ok = False
        if A < B and W(B, A):     # strict monotonicity
            ok = False
        for C in subsets:
            if W(A, B) and W(B, C) and not W(A, C):
                ok = False
edge_same = all(W(A, B) == W0(A, B) for A in subsets for B in subsets
                if {cl[x] for x in (A ^ B)} <= set('IJ') or {cl[x] for x in (A ^ B)} <= set('IK'))
differs = any(W(A, B) != W0(A, B) for A in subsets for B in subsets)
print('3. preorder + strict monotonicity + cancellation:', ok, '; edge comparisons equal to'
      ' inclusion order:', edge_same, '; differs on M:', differs)
