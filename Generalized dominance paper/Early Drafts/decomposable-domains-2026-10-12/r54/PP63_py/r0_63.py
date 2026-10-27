"""PP63 s.6: exact check of PP62's draft rule R0 on PP56's exact instances (Fractions / integers).

R0(r) = {} if r empty; {w : V_w(r) < 0} if V(r) != 0; {w0} if r non-empty and V(r) = 0,
with V the level-0 (u1) value of the record (PP56 instance: sum_p m_p (phi_p(new) - phi_p(old))).
Masses are chosen so that NULL records exist (the kink's balanced swap: equal masses on Ep and Em),
otherwise the null clause is never exercised.
Checks over all ordered pairs / triples of instance models: reflexivity, strict (G), (IB) (by construction),
(TC) at every world, defence and protection (direct (C), undominatedness) for A and the proxies A^B, A^D.
Also: the number of null records, and that at u the pure e_{w0}-shift sequence gives a section failure
for the rival A[F -> S] (F the balanced swap) -- via Lemma 4.1 (strict w0-improvement), proved in the note.
"""
import os, sys, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP56_py'))
import numpy as np
from instance56 import Instance, DIS, ABOVE, BELOW
from cells56 import rank


def run(ids, vals, masses, w0=1):
    inst = Instance(ids, vals, masses)
    MODS = inst.models()
    n = len(MODS)
    lev = np.array([[inst.key(X, w)[0] for w in range(3)] for X in MODS], dtype=object)   # Phi_w(X)
    idx = {X: k for k, X in enumerate(MODS)}
    ACC = np.zeros((3, n, n), dtype=bool)
    nnull = 0
    for a, X in enumerate(MODS):
        for b, Y in enumerate(MODS):
            if a == b:
                ACC[:, a, b] = True
                continue
            Vv = [lev[b][w] - lev[a][w] for w in range(3)]
            if all(v == 0 for v in Vv):
                nnull += 1
                for w in range(3):
                    ACC[w, a, b] = (w != w0)
            else:
                for w in range(3):
                    ACC[w, a, b] = Vv[w] >= 0
    ok = True
    # strict (G)
    rk = np.array([[[rank(X[p], inst.g[p], w) for p in range(len(ids))] for X in MODS] for w in range(3)])
    for w in range(3):
        le = (rk[w][:, None, :] <= rk[w][None, :, :]).all(axis=2)
        ne = (rk[w][:, None, :] != rk[w][None, :, :]).any(axis=2)
        strict = le & ne
        ok &= bool((ACC[w] | ~strict).all()) and bool((~ACC[w].T | ~strict).all())
    # (TC)
    tcf = 0
    for w in range(3):
        M = ACC[w]
        for a in range(n):
            cyc = M[a][:, None] & M & M[:, a][None, :]
            good = M[:, a][:, None] & M.T & M[a][None, :]
            tcf += int((cyc & ~good).sum())
    ok &= tcf == 0
    # selected obligations (A and the proxies are coherent stand-ins; every other instance model is incoherent)
    dfn = prot = True
    for N in inst.base.values():
        a = idx[N]
        for b in range(n):
            if b == a:
                continue
            dfn &= bool(ACC[:, a, b].any())
            prot &= not bool(ACC[:, b, a].all())
    ok &= dfn and prot
    return ok, nnull, tcf, dfn, prot, n


if __name__ == '__main__':
    import random
    random.seed(62)
    ALL = True
    others = [i for i in range(len(DIS)) if i not in (ABOVE, BELOW)]
    for trial in range(4):
        ids = [ABOVE, BELOW] + random.sample(others, 4)
        masses = [7, 7] + [random.randint(1, 9) for _ in range(4)]     # equal |g|-mass on Ep, Em: balanced swap
        for w0 in range(3):
            ok, nn, tcf, dfn, prot, n = run(ids, ('P', 'S'), masses, w0)
            print(f'six pieces {ids}, values hS, masses {masses}, w0={w0+1}: models {n}, null records {nn}, '
                  f'TC failures {tcf}, defence {dfn}, protection {prot}: {"OK" if ok else "FAIL"}')
            ALL &= ok and nn > 0
    ids = [ABOVE, BELOW, others[0]]
    ok, nn, tcf, dfn, prot, n = run(ids, ('P', 'M', 'S', 'C'), [5, 5, 3], 1)
    print(f'three pieces, four values, w0=2: models {n}, null records {nn}, TC failures {tcf}, defence {dfn}, protection {prot}: {"OK" if ok else "FAIL"}')
    ALL &= ok
    print('R0 satisfies every non-section clause on these instances (null records exercised):', ALL)
    print('ALL PASS' if ALL else 'SOME FAIL')
