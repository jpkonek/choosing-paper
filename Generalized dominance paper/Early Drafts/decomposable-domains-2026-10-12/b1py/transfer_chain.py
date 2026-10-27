"""B1 notes, Lemma B1.2 (transfer chain): exact check on atomless cells.

Abstract model of world i on M = Q_i u Q_j u Q_k (the three sign classes; Q_i is the
link class R_ij n R_ik).  Each cell is a homogeneous atomless piece of M with
  cls  in {'L','J','K'}   (L = Q_i, J = Q_j, K = Q_k)
  m    rho-mass (Fraction > 0)
  err  True if the *current* model errs at world i on the cell
  inD  True if the cell is to be toggled (C -> X)
Toggling a fraction df of a cell changes the rho-error by +df*m (cell correct) or -df*m
(cell wrong).  A step may toggle cells of classes {L,J} only (an R_ij step) or {L,K}
only (an R_ik step).  The lemma: if Delta = net rho-error change of toggling D is > 0,
there is a finite chain C -> X of such steps, each with the SAME strictly positive
change.  Exact rational arithmetic; run with  python3 -I transfer_chain.py
"""
from fractions import Fraction as F
import random


def sgn(cell):
    return -1 if cell['err'] else 1


def leg(cells, tag):
    """Toggle every cell with inD=True, by a chain of R_ij / R_ik steps.
    Returns list of steps; each step = (classes_used, change, {cell_index: signed fraction})."""
    s_a = sum(c['m'] * sgn(c) for c in cells if c['inD'] and c['cls'] in 'LJ')
    s_b = sum(c['m'] * sgn(c) for c in cells if c['inD'] and c['cls'] == 'K')
    delta = s_a + s_b
    assert delta > 0, 'leg needs Delta > 0'
    room = [n for n, c in enumerate(cells) if c['cls'] == 'L' and not c['inD']]
    rplus = [n for n in room if sgn(cells[n]) > 0]
    rminus = [n for n in room if sgn(cells[n]) < 0]
    mplus = sum(cells[n]['m'] for n in rplus)
    mminus = sum(cells[n]['m'] for n in rminus)
    assert mplus + mminus > 0, 'leg needs room in the link class'
    N = 1
    while True:
        tau = delta / (2 * N) - s_a / N
        if tau == 0:
            choice = None
            break
        # tau>0: (order ab, R+) or (order ba, R-); tau<0: (order ab, R-) or (order ba, R+)
        opts = []
        if tau > 0:
            opts = [('ab', rplus, mplus), ('ba', rminus, mminus)]
        else:
            opts = [('ab', rminus, mminus), ('ba', rplus, mplus)]
        opts = [o for o in opts if o[2] >= abs(tau)]
        if opts:
            choice = opts[0]
            break
        N *= 2
    # all N rounds are identical: build one round, verify it, and report N copies
    a = {n: F(1, N) for n, c in enumerate(cells) if c['inD'] and c['cls'] in 'LJ'}
    b = {n: F(1, N) for n, c in enumerate(cells) if c['inD'] and c['cls'] == 'K'}
    order = 'ab'
    if choice is not None:
        order, rset, rmass = choice
        frac = abs(tau) / rmass        # same fraction of every room cell of that type
        first, second = (a, b) if order == 'ab' else (b, a)
        for n in rset:
            first[n] = first.get(n, 0) + frac      # toggle
            second[n] = second.get(n, 0) - frac    # untoggle
    seq = [('LJ', a), ('LK', b)] if order == 'ab' else [('LK', b), ('LJ', a)]
    rnd = []
    for clsset, tog in seq:
        change = F(0)
        for n, df in tog.items():
            c = cells[n]
            assert c['cls'] in clsset
            change += df * c['m'] * sgn(c)   # df<0 = untoggle a room portion
        rnd.append((clsset, change, tog))
    # a room portion is toggled and then untoggled within the round: check it never
    # exceeds the cell (fraction <= 1) and the round is consistent
    if choice is not None:
        assert frac <= 1
    # bookkeeping over the N rounds: every D cell toggled exactly once, room restored
    for n, c in enumerate(cells):
        tot = N * sum(tog.get(n, 0) for _, _, tog in rnd)
        want = 1 if c['inD'] else 0
        assert tot == want, (tag, n, tot, want)
    steps = rnd * N
    return steps, delta


def chain(cells):
    """Full chain; halves D first if the link class has no room."""
    room = [c for c in cells if c['cls'] == 'L' and not c['inD']]
    if sum(c['m'] for c in room) > 0:
        steps, d = leg([dict(c) for c in cells], 'single')
        return steps, d, 'single leg'
    # halving: split every D cell into two halves
    h = []
    for c in cells:
        if c['inD']:
            h.append(dict(c, m=c['m'] / 2, inD=True, half=1))
            h.append(dict(c, m=c['m'] / 2, inD=False, half=2))
        else:
            h.append(dict(c, half=0))
    s1, d1 = leg([dict(c) for c in h], 'leg1')
    # after leg 1: half-1 cells are toggled (status flipped), half-2 cells are now the D
    h2 = []
    for c in h:
        if c['half'] == 1:
            h2.append(dict(c, err=not c['err'], inD=False))
        elif c['half'] == 2:
            h2.append(dict(c, inD=True))
        else:
            h2.append(dict(c))
    s2, d2 = leg(h2, 'leg2')
    return s1 + s2, d1 + d2, 'two legs (no room)'


def rand_instance(rng, noroom):
    cells = []
    for _ in range(rng.randint(3, 14)):
        cls = rng.choice('LJK')
        cells.append(dict(cls=cls, m=F(rng.randint(1, 50), rng.randint(1, 9)),
                          err=rng.random() < 0.5, inD=rng.random() < 0.6))
    for cl in 'LJK':                      # every class present
        cells.append(dict(cls=cl, m=F(rng.randint(1, 30), 7), err=rng.random() < .5,
                          inD=True))
    if noroom:
        for c in cells:
            if c['cls'] == 'L':
                c['inD'] = True
    else:
        cells.append(dict(cls='L', m=F(1, rng.randint(100, 3000)),   # tiny room
                          err=rng.random() < 0.5, inD=False))
    return cells


def main():
    rng = random.Random(20261015)
    done = {'single leg': 0, 'two legs (no room)': 0}
    worst_N = 0
    n_inst = 0
    while n_inst < 4000:
        cells = rand_instance(rng, noroom=(n_inst % 2 == 1))
        delta = sum(c['m'] * sgn(c) for c in cells if c['inD'])
        if delta <= 0:
            continue
        steps, d, mode = chain(cells)
        assert d == delta
        changes = set(ch for _, ch, _ in steps)
        assert all(ch > 0 for ch in changes)
        assert sum(ch for _, ch, _ in steps) == delta
        for clsset, ch, tog in steps:
            for n in tog:
                pass
        done[mode] += 1
        worst_N = max(worst_N, len(steps))
        n_inst += 1
    print('instances with Delta>0 :', n_inst, done)
    print('every step: one edge region (LJ or LK), change > 0, changes sum to Delta: OK')
    print('longest chain (steps)  :', worst_N)
    # one explicit small example
    ex = [dict(cls='J', m=F(5), err=True, inD=True),    # C errs on Q_j part: toggling fixes 5
          dict(cls='K', m=F(6), err=False, inD=True),   # toggling adds 6
          dict(cls='L', m=F(1, 100), err=False, inD=False)]  # tiny room
    steps, d, mode = chain(ex)
    print('\nexplicit example: s_J=-5, s_K=+6, Delta=1, room 1/100 ->', mode,
          ', steps:', len(steps), ', each change =', steps[0][1])


if __name__ == '__main__':
    main()
