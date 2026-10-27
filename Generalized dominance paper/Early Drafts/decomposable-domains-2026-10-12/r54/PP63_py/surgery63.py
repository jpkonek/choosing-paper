"""PP63 Lemma 3.1 (refusal surgery), checked exhaustively on an exact finite instance.

Base relation: PP56's Lambda on six pieces of the kink cells (Ep, Em + 4 others), values {h, S}
(64 models; PP56 instance56.Instance, unchanged).  Selected obligations for A, A^B, A^D (PP56 local proxies).
For many random records r and worlds i with r, r^{-1} not weakly i-favourable for their old sides:
  (a) refuse {r, r^-1} at i  -> check reflexivity, strict (G), (IB), (TC) on all ordered triples,
      undominatedness / direct (C) for the proxies; defence holds iff the prediction of Lemma 3.1(b);
  (b) control: refuse r alone at i (not inverse-closed) -> count (TC) failures.
"""
import os, sys, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP56_py'))
from instance56 import Instance, DIS, ABOVE, BELOW
from cells56 import rank

random.seed(63)
ids = [ABOVE, BELOW] + random.sample([i for i in range(len(DIS)) if i not in (ABOVE, BELOW)], 4)
inst = Instance(ids, ('P', 'S'), [random.randint(1, 50) for _ in ids])
MODS = inst.models()
W = range(3)
LEVEL = int(sys.argv[1]) if len(sys.argv) > 1 else 0
K = {X: [inst.key(X, w)[:1] if LEVEL == 1 else inst.key(X, w) for w in W] for X in MODS}


def rec(X, Y):
    return tuple((p, X[p], Y[p]) for p in range(len(X)) if X[p] != Y[p])


def inv(r):
    return tuple((p, b, a) for (p, a, b) in r)


BASE = {}
for X in MODS:
    for Y in MODS:
        BASE[rec(X, Y)] = tuple(K[X][w] <= K[Y][w] for w in W)

SEL = list(inst.base.values())     # A, A^B, A^D as proxies (all coherent stand-ins; rivals incoherent unless equal)


def weakly_fav(r, i):
    """old side pointwise no worse at i on the record."""
    return all(rank(a, inst.g[p], i) <= rank(b, inst.g[p], i) for (p, a, b) in r)


def check(V):
    acc = lambda X, Y, w: True if X == Y else V[rec(X, Y)][w]
    ok_g = ok_tc = ok_prot = True
    for X in MODS:
        for Y in MODS:
            if X == Y:
                continue
            for w in W:
                rx = [rank(X[p], inst.g[p], w) for p in range(6)]
                ry = [rank(Y[p], inst.g[p], w) for p in range(6)]
                if all(a <= b for a, b in zip(rx, ry)):
                    ok_g &= acc(X, Y, w) and not acc(Y, X, w)
    import numpy as np
    n = len(MODS)
    tcfail = 0
    for w in W:
        Mx = np.array([[acc(MODS[a], MODS[b], w) for b in range(n)] for a in range(n)], dtype=bool)
        for a in range(n):
            cyc = Mx[a][:, None] & Mx & Mx[:, a][None, :]
            good = Mx[:, a][:, None] & Mx.T & Mx[a][None, :]
            tcfail += int((cyc & ~good).sum())
    defence = True
    for N in SEL:
        for X in MODS:
            if X == N:
                continue
            defence &= any(acc(N, X, w) for w in W)
            if all(acc(X, N, w) for w in W):          # undominatedness, then (C): X != N is incoherent
                ok_prot = False
    return ok_g, tcfail, ok_prot, defence


ok0 = check(BASE)
print('base', 'Lambda (all levels)' if LEVEL == 0 else 'level-1 only (ties)', ': strict (G)', ok0[0], ' TC failures', ok0[1], ' protection', ok0[2], ' defence', ok0[3])
ALL = ok0[0] and ok0[1] == 0
BASEPROT, BASEDEF = ok0[2], ok0[3]
recs = [r for r in BASE if r]
trials = 0
ctrl_fail = 0
pred_ok = True
while trials < 60:
    r = random.choice(recs)
    i = random.randrange(3)
    if weakly_fav(r, i) or weakly_fav(inv(r), i):
        continue
    if LEVEL == 1 and not (BASE[r][i] and BASE[inv(r)][i]):
        continue          # control base: use records tied at i
    trials += 1
    V = dict(BASE)
    for s in (r, inv(r)):
        V[s] = tuple(False if w == i else V[s][w] for w in W)
    g, tc, prot, dfn = check(V)
    # prediction of Lemma 3.1(b): defence survives iff each realised record in U keeps a world != i
    realised = lambda s: any(rec(N, tuple(N[p] if all(q != p for (q, _, _) in s) else [b for (q, a, b) in s if q == p][0]
                                            for p in range(6))) == s for N in SEL)
    pred = all(any(BASE[s][w] for w in W if w != i) for s in (r, inv(r)) if realised(s))
    pred_ok &= (pred == dfn) if BASEDEF else True
    ALL &= g and tc == 0 and (prot or not BASEPROT)
    V2 = dict(BASE)
    V2[r] = tuple(False if w == i else V2[r][w] for w in W)
    ctrl_fail += check(V2)[1] > 0
print('surgery trials (r, r^-1 refused at i):', trials, ' all: strict (G), (TC), protection preserved:', ALL)
print('defence survives exactly as Lemma 3.1(b) predicts:', pred_ok)
print('control (refuse r alone, not inverse-closed): trials with a (TC) failure:', ctrl_fail, 'of', trials)
print('ALL PASS' if ALL and pred_ok and (LEVEL == 0 or ctrl_fail > 0) else 'SOME FAIL')
