"""REFEREE54: independent re-check of PP61 section 5.1 (the Cor E.2 configuration at u).

Input: the pickles written by corE2_rerun.py (a verbatim re-run of PP61's run61d.py that only saves its data).
Reused: model value vectors over exact atoms (rays), the selected/coherent/fixed flags, PP56's level-0 field PHI
(only for reporting u^1 signs), and the SAT verdict vector (through PP61's pair -> record matrix R).
Recomputed here: records (own), ranks (own), guidance, DEF, C/UND, SEC, (IB), TC on all ordered triples.
Also: the 13-clause V2 core, rebuilt from own records and brute-forced over its 12 variables (UNSAT; minimal).
"""
import sys, os, pickle, itertools
from collections import Counter, defaultdict
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
VALS = ('P', 'M', 'S', 'C')


def my_rank(v, g, w):
    if v == 'S':
        return 1
    if v == 'C':
        return 3
    s = g[w] if v == 'P' else -g[w]
    assert s != 0
    return 0 if s > 0 else 2


def check_model(fn):
    D = pickle.load(open(os.path.join(HERE, fn), 'rb'))
    names, vecs, flags, atoms, R, val = D['names'], D['vecs'], D['flags'], D['atoms'], D['R'], D['val']
    n = len(names)
    acc = lambda r, i: bool(val[3 * int(r) + i + 1])
    A = np.zeros((3, n, n), dtype=bool)
    for a in range(n):
        for b in range(n):
            for i in range(3):
                A[i, a, b] = acc(R[a, b], i)
    bad = Counter({k: 0 for k in ('REFL', 'G', 'DEF', 'UND', 'C', 'SEC', 'TC', 'EXTRA')})
    recs = {}
    ib = defaultdict(set)
    for a in range(n):
        for b in range(n):
            rec = tuple((p, vecs[a][p], vecs[b][p]) for p in range(len(atoms)) if vecs[a][p] != vecs[b][p])
            recs[a, b] = rec
            ib[rec].add(tuple(A[:, a, b]))
            if a == b or not rec:      # equal models under different names: reflexivity via (IB)
                bad['REFL'] += int(not A[:, a, b].all())
                continue
            for i in range(3):
                bt = [my_rank(VALS[x], atoms[p][1], i) < my_rank(VALS[y], atoms[p][1], i) for (p, x, y) in rec]
                if all(bt) and not (A[i, a, b] and not A[i, b, a]):
                    bad['G'] += 1
                if not any(bt) and not (not A[i, a, b] and A[i, b, a]):
                    bad['G'] += 1
    bad['IB'] = sum(1 for s in ib.values() if len(s) > 1)
    for a in range(n):
        if not flags[names[a]][1]:
            continue
        for b in range(n):
            if a == b:
                continue
            bad['DEF'] += int(not A[:, a, b].any())
            if flags[names[b]][0]:
                bad['UND'] += int(A[:, b, a].all() and not A[:, a, b].all())
            else:
                bad['C'] += int(A[:, b, a].all())
    iu = names.index('S:u')
    for t in [k for k, nm in enumerate(names) if nm.startswith('S:t')]:
        for b in range(n):
            if flags[names[b]][2] and b != iu:
                for i in range(3):
                    bad['SEC'] += int(A[i, t, b] and not A[i, iu, b])
    for i in range(3):
        Ai = A[i].astype(np.int32)
        bad['TC'] += int(((A[i] & ~A[i].T) & ((Ai @ Ai).T > 0)).sum())
    for tag, c in D['extra']:
        if not any((val[abs(l)] if l > 0 else not val[abs(l)]) for l in c):
            bad['EXTRA'] += 1
    # report the germ shape against the full balanced swap
    PHI, W = D['PHI'], D['W']
    ix = names.index('X:Ep.aEp.bEm.aEm.b')
    Rs = lambda a, b: ''.join(str(i + 1) for i in range(3) if not A[i, a, b]) or '-'
    print('[%s] R(C_u->X)={%s} R(X->C_u)={%s} R(C_B->Y)={%s}' % (D['tag'], Rs(iu, ix), Rs(ix, iu), Rs(names.index('S:B'), names.index('Y:Ep.aEp.bEm.aEm.b'))))
    for t in [k for k, nm in enumerate(names) if nm.startswith('S:t')]:
        rec = recs[t, ix]
        V = []
        for i in range(3):
            m1 = sum((W[p][1] or 0) * (PHI[p][i][y] - PHI[p][i][x]) for (p, x, y) in rec)
            m0 = sum((W[p][0] or 0) * (PHI[p][i][y] - PHI[p][i][x]) for (p, x, y) in rec)
            V.append((m0, m1))
        accw = [i + 1 for i in range(3) if A[i, t, ix]]
        unf = [i + 1 for i in range(3) if A[i, t, ix] and V[i] < (0, 0)]
        print('   %s: R={%s} accepted at %s, u1-unfavourable acceptances at %s' % (names[t], Rs(t, ix), accw, unf))
    print('   violations:', dict(bad), '->', 'PASS' if not any(bad.values()) else 'FAIL')
    return names, vecs, recs, A


def core_check():
    D = pickle.load(open(os.path.join(HERE, 'corE2_V0.pkl'), 'rb'))
    names, vecs, atoms = D['names'], D['vecs'], D['atoms']
    idx = {nm: k for k, nm in enumerate(names)}
    rec = lambda a, b: tuple((p, vecs[a][p], vecs[b][p]) for p in range(len(atoms)) if vecs[a][p] != vecs[b][p])
    iu, iB = idx['S:u'], idx['S:B']
    ixp, iyp = idx['X:Ep.aEm.a'], idx['Y:Ep.aEm.a']
    # (IB): rec(Y' -> C_B) equals rec(C_u -> X')
    same = rec(iyp, iB) == rec(iu, ixp)
    # coarse-scale shifted members t00, t10, t20 (shift e1, e2, e3)
    T = [idx['S:t00'], idx['S:t10'], idx['S:t20']]
    # u^1 signs of rec(C_{u_t^w} -> X') with the layer weighted by eps (equal per layer atom), F weighted 1
    PHI, W = D['PHI'], D['W']
    signs = []
    for w, t in enumerate(T):
        r = rec(t, ixp)
        V = [(sum((W[p][0] or 0) * (PHI[p][i][y] - PHI[p][i][x]) for (p, x, y) in r),
              sum((W[p][1] or 0) * (PHI[p][i][y] - PHI[p][i][x]) for (p, x, y) in r)) for i in range(3)]
        signs.append(V)
    endorsed_neg = all(signs[w][v] < (0, 0) for w in range(3) for v in range(3) if v != w)
    # variables: r[i] = [C_u <=_i X'] (= [Y' <=_i C_B] by IB), s[w][i] = [C_{u_t^w} <=_i X']
    def clauses():
        cl = [('C', [(('r', i), False) for i in range(3)])]
        for w in range(3):
            cl.append(('DEF%d' % w, [(('s', w, i), True) for i in range(3)]))
            cl.append(('SEC%d' % w, [(('s', w, w), False), (('r', w), True)]))
            for v in range(3):
                if v != w:
                    cl.append(('END%d%d' % (w, v), [(('s', w, v), False)]))
        return cl
    CL = clauses()
    vars_ = sorted({lit for _, c in CL for lit, _ in c})
    def sat(cls):
        for bits in itertools.product((False, True), repeat=len(vars_)):
            asg = dict(zip(vars_, bits))
            if all(any(asg[l] == pos for l, pos in c) for _, c in cls):
                return True
        return False
    unsat = not sat(CL)
    minimal = all(sat(CL[:k] + CL[k + 1:]) for k in range(len(CL)))
    print('[V2 core] %d clauses over %d variables; (IB) rec(Y\'->C_B) = rec(C_u->X\'): %s; END units have V_v < 0 at v != w: %s; UNSAT: %s; minimal: %s'
          % (len(CL), len(vars_), same, endorsed_neg, unsat, minimal))
    return same and endorsed_neg and unsat and minimal


if __name__ == '__main__':
    ok = True
    for fn in ('corE2_V0.pkl', 'corE2_V1.pkl'):
        check_model(fn)
    print('core re-check:', 'PASS' if core_check() else 'FAIL')
