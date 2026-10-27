"""anchor59: independent re-run of PP74 Prop 5.2 / second74 (ASR anchoring fails for T--B splices).
Committed {T, B} with B = C_{(1,1,r)} (class 3) or C_{(r,1,1)} (class 1), r = 20/21; and {T, B3, B1} for the
defender--defender splices B3[S -> B1].  Rivals: splices Z1[S -> Z2], S a non-empty proper union of coarse
layer cells (cells of the Z1/Z2 arrangement inside {Z1 != Z2}).  Candidates B'': posterior grid, vertex-wise
single-world down-shifts, vertex-wise mixed rescalings (the same three families as PP74, generated here).
ASR admissibility: (N1) and (U1) for every committed model, and (U2): every committed C affected at some w has
an anchor v != w with B'' pointwise weakly v-worse than C.  'Affected at w' is computed from PP76 Theorem 1.1
with ALL copies (off-support part G2 allowed), and separately for the restricted family C[S -> B''] only.
Vectorised over splices with numpy; cells exact (Fractions)."""
import sys, os, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib59 import *
r = F(20, 21)


def candidates():
    out = {}
    g = [F(21, 20) ** e for e in range(-3, 4)]
    for a in g:
        for b in g:
            out[('P', a, b)] = post((a, b, F(1)))
    sh = [F(1), r, r * r, r ** 3]
    for k in range(3):
        for s in itertools.product(sh, repeat=3):
            if len(set(s)) == 1: continue
            out[('VW', k, s)] = vwise([down(k, x) for x in s])
    mix = [F(1), F(21, 20), r]
    for ms in itertools.product(itertools.product(mix, repeat=2), repeat=3):
        mm = tuple((p[0], p[1], F(1)) for p in ms)
        if len(set(mm)) == 1: continue
        out[('VM', mm)] = vwise(mm)
    return out


def ranks(vals, cor):
    """vals, cor: int arrays (..., n); rank 0 correct, 1 silent, 2 wrong"""
    return np.where(vals == cor, 0, np.where(vals == 0, 1, 2))


def run(committed, pair, label):
    Z1, Z2 = pair
    cand = candidates()
    base = cells(committed)
    key = lambda h: tuple(tuple(sum(F(k[i]) * h[i] for i in range(3)) > 0 for k in committed[z]) for z in pair)
    Lk = sorted({key(c['pt']) for c in base if c['vals'][Z1] != c['vals'][Z2]})
    n = len(Lk)
    Ss = [frozenset(c) for kk in range(1, n) for c in itertools.combinations(range(n), kk)]
    nS = len(Ss)
    Smat = np.array([[j in S for j in range(n)] for S in Ss])           # nS x n
    good = {'all': np.zeros(nS, bool), 'restricted': np.zeros(nS, bool)}
    n1u1 = np.zeros(nS, bool)
    seen = set()
    for name, K in cand.items():
        if tuple(K) in seen: continue
        seen.add(tuple(K))
        mods = dict(committed); mods['Bc'] = K
        cs = cells(mods)
        m = len(cs)
        cor = np.array([[1 if c['pt'][w] > 0 else -1 for c in cs] for w in range(3)])     # 3 x m
        idx = np.array([Lk.index(key(c['pt'])) if c['vals'][Z1] != c['vals'][Z2] else -1 for c in cs])
        com = {z: np.array([c['vals'][z] for c in cs]) for z in committed}
        Bv = np.array([c['vals']['Bc'] for c in cs])
        inS = np.zeros((nS, m), bool)
        lay = idx >= 0
        inS[:, lay] = Smat[:, idx[lay]]
        X = np.where(inS, com[Z2][None, :], com[Z1][None, :])                       # nS x m
        D = (Bv[None, :] != X)
        rB = np.stack([ranks(Bv, cor[w]) for w in range(3)])                        # 3 x m
        rX = np.stack([ranks(X, cor[w][None, :]) for w in range(3)])                # 3 x nS x m
        N1 = np.all([np.any(D & (rB[w][None, :] < rX[w]), axis=1) for w in range(3)], axis=0)
        U1 = np.ones(nS, bool)
        for z in committed:
            U1 &= np.any(D & (com[z][None, :] != X), axis=1)
        okS = N1 & U1 & np.any(D, axis=1)
        n1u1 |= okS
        for mode in ('all', 'restricted'):
            ok = okS.copy()
            for z in committed:
                C = com[z]
                rC = np.stack([ranks(C, cor[w]) for w in range(3)])
                for w in range(3):
                    bet = D & (rB[w][None, :] < rX[w])
                    cond = (C[None, :] != Bv[None, :]) & (rC[w][None, :] >= rX[w])
                    feas = ~np.any(bet & ~cond, axis=1)
                    strict = np.any(D & (rB[w][None, :] > rX[w]), axis=1) | np.any(D & cond & (rC[w][None, :] > rX[w]), axis=1)
                    if mode == 'all':
                        strict |= np.any(~D & (rC[w][None, :] > 0), axis=1)
                    else:
                        # restricted family: Y_S = B[S -> C] for S between bet and Smax; strictness = Y_S != X
                        Smax = (C[None, :] != Bv[None, :]) & (rC[w][None, :] >= rX[w])
                        for Sset in (bet, Smax):
                            Y = np.where(Sset, C[None, :], Bv[None, :])
                            strict |= np.any(Sset, axis=1) & np.any(Y != X, axis=1)
                    aff = feas & strict
                    anch = np.zeros(nS, bool)
                    for v in range(3):
                        if v == w: continue
                        if np.all(rB[v] >= rC[v]):
                            anch[:] = True
                    ok &= ~aff | anch
            good[mode] |= ok
    print('%s: distinct candidates %d, coarse layer cells %d, splices %d' % (label, len(seen), n, nS))
    print('   splices with a candidate passing N1 + U1: %d / %d' % (n1u1.sum(), nS))
    for mode in ('all', 'restricted'):
        print('   splices with an ASR-admissible (anchored) candidate [%s copies]: %d / %d' % (mode, good[mode].sum(), nS))
    sys.stdout.flush()


if __name__ == '__main__':
    T = post((1, 1, 1))
    job = sys.argv[1] if len(sys.argv) > 1 else 'ALL'
    if job in ('TB3', 'ALL'): run({'T': T, 'B': post(down(2, r))}, ('T', 'B'), 'T--B3 splices')
    if job in ('TB1', 'ALL'): run({'T': T, 'B': post(down(0, r))}, ('T', 'B'), 'T--B1 splices')
    if job in ('B3B1', 'ALL'): run({'T': T, 'B3': post(down(2, r)), 'B1': post(down(0, r))}, ('B3', 'B1'), 'B3--B1 splices')
