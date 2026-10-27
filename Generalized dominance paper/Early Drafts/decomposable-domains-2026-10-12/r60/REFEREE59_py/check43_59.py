"""check43_59: brute-force check of the record-level conditions of PP74 Theorem 4.3 on a finite sample of
the three-ray star, by an enumeration independent of PP74's proof.

Sample committed family G: T and pure down-shifts B_{k,lam} (m_k = lam) at several scales per ray.
Atoms: signatures (type, value of every sample model) of the cells of the joint arrangement.
Rival: X_E = T[E -> h], E a union of (parts of) atoms in Sil(T) cap A_3 cap L_3(lam_min); each signature
group may be wholly in E, outside E, or split (three states).
Defender: B = B_{3,lam} for every sample lam with E \ L(lam) non-null.

Checked, for every such (E, B):
 (N1)  B strictly better than X somewhere at every world;
 (U1)  no sample model equals X on D = {B != X};
 (d)   at the unfavourable world 3, for every triangle B' -> X' -> Y -> B' through a copy of d:
       - s = rec(X' -> Y) strict guidance and t carried by some C in G  =>  t strictly reverse-guidance;
       - t strict guidance and s carried by some C                      =>  s strictly reverse-guidance;
       - s carried by C1 and t carried by C2 (any C1, C2 in G)          =>  s or t strictly reverse-guidance.
   W and Y range over all FOUR advice values on every atom, and atoms may be split (measurable Y, W).
 (c)   for every ordered pair of sample dominations, X_{d1} != B_{d2} on a non-null part of D1 cap D2.
A 'bad' triangle exists iff every atom admits an allowed local choice and the required witnesses exist
(possibly on different parts of one atom); this is exact for unions of atoms with splitting.
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib59 import *

VALS = (1, 0, -1, 2)      # h, S, -h, contradictory (2 = contradictory)


def rk(v, o_type, w):
    # rank at world w of value v at an atom of type o_type = (('A'|'B'), odd)
    kind, o = o_type
    # sign of h_w: A_o -> h_o < 0, others > 0; B_o -> h_o > 0, others < 0
    hw_pos = (w != o) if kind == 'A' else (w == o)
    if v == 2:
        return 3
    if v == 0:
        return 1
    cor = 1 if hw_pos else -1
    return 0 if v == cor else 2


def main():
    T = post((1, 1, 1))
    lam3 = [F(20, 21), F(9, 10), F(4, 5)]
    lamo = [F(20, 21), F(17, 20)]
    models = {'T': T}
    for l in lam3:
        models['B3_%s' % l] = post(down(2, l))
    for k in (0, 1):
        for l in lamo:
            models['B%d_%s' % (k + 1, l)] = post(down(k, l))
    names = list(models)
    cs = cells(models)
    sig = {}
    for c in cs:
        t = htype(c['pt'])
        if t[0] == 'U':
            continue
        key = (t, tuple(c['vals'][n] for n in names))
        sig[key] = sig.get(key, 0.0) + solid(c['poly'])
    atoms = list(sig)
    assert all(v in (0, 1) for (_, vs) in atoms for v in vs), '2V violated'
    print('sample models:', len(names), ' atoms (signatures, mixed problems):', len(atoms))
    iT = names.index('T')
    big = names.index('B3_%s' % lam3[-1])
    cand = [a for a in atoms if a[0] == ('A', 2) and a[1][iT] == 0 and a[1][big] == 1]
    print('Sil(T) cap A_3 cap L_3(lam_min) signature groups:', len(cand))
    nE = nB = 0
    fails = {'N1': 0, 'U1': 0, 'd_ref': 0, 'd_cov': 0}
    doms = []
    for states in itertools.product((0, 1, 2), repeat=len(cand)):
        if not any(states):
            continue
        # build atom list with E-membership; split groups appear twice (in E / not in E)
        At = []
        for a in atoms:
            if a in cand:
                s = states[cand.index(a)]
                if s in (1, 2):
                    At.append((a[0], a[1], True))
                if s in (0, 2):
                    At.append((a[0], a[1], False))
            else:
                At.append((a[0], a[1], False))
        nE += 1
        Xv = [1 if inE else vs[iT] for (_, vs, inE) in At]
        for l in lam3:
            ib = names.index('B3_%s' % l)
            Bv = [vs[ib] for (_, vs, _) in At]
            # E \ L(lam) non-null: an E-atom where B silent
            if not any(inE and vs[ib] == 0 for (_, vs, inE) in At):
                continue
            nB += 1
            D = [i for i in range(len(At)) if Bv[i] != Xv[i]]
            ty = [a[0] for a in At]
            n1 = all(any(rk(Bv[i], ty[i], w) < rk(Xv[i], ty[i], w) for i in D) for w in range(3))
            if not n1:
                fails['N1'] += 1
            for C in range(len(names)):
                if all(At[i][1][C] == Xv[i] for i in D):
                    fails['U1'] += 1
            doms.append((frozenset(i for i in D), tuple(Xv), tuple(Bv), tuple((a[0], a[1]) for a in At)))
            w = 2
            Dset = set(D)

            def choices(i, mode, C1=None, C2=None):
                """allowed local (W, Y) choices at atom i; returns list of (sbad, tbad, snon, tnon)."""
                out = []
                Ws = VALS if i not in Dset else (None,)
                for W in Ws:
                    Bp = Bv[i] if i in Dset else W
                    Xp = Xv[i] if i in Dset else W
                    for Y in VALS:
                        sdiff, tdiff = (Xp != Y), (Y != Bp)
                        rX, rY, rB = rk(Xp, ty[i], w), rk(Y, ty[i], w), rk(Bp, ty[i], w)
                        if mode == 'Gs':          # s guidance: Y weakly w-worse than X'
                            if rY < rX: continue
                            if tdiff and At[i][1][C2] != Y: continue
                        elif mode == 'Gt':        # t guidance: B' weakly w-worse than Y
                            if rB < rY: continue
                            if sdiff and At[i][1][C1] != Xp: continue
                        else:                     # cover
                            if sdiff and At[i][1][C1] != Xp: continue
                            if tdiff and At[i][1][C2] != Y: continue
                        sbad = sdiff and not (rY < rX)      # s not strictly improving at this point
                        tbad = tdiff and not (rB < rY)
                        out.append((sbad, tbad, sdiff, tdiff))
                return out

            def bad(mode, C1=None, C2=None):
                ch = [choices(i, mode, C1, C2) for i in range(len(At))]
                if any(len(c) == 0 for c in ch):
                    return False
                any_ = lambda f: any(f(x) for c in ch for x in c)
                if mode == 'Gs':
                    return any_(lambda x: x[2]) and any_(lambda x: x[1])
                if mode == 'Gt':
                    return any_(lambda x: x[3]) and any_(lambda x: x[0])
                return any_(lambda x: x[0]) and any_(lambda x: x[1])
            for C in range(len(names)):
                if bad('Gs', C2=C) or bad('Gt', C1=C):
                    fails['d_ref'] += 1
            for C1 in range(len(names)):
                for C2 in range(len(names)):
                    if bad('cov', C1, C2):
                        fails['d_cov'] += 1
    print('rivals E (with split states):', nE, ' (E, defender) pairs:', nB)
    print('failures:', fails)
    # (c): consecutive dominations, over pairs sharing the same atom list (same E-split structure)
    bad_c = tot_c = 0
    for d1, d2 in itertools.product(doms, repeat=2):
        if d1[3] != d2[3]:
            continue
        tot_c += 1
        inter = d1[0] & d2[0]
        if not any(d1[1][i] != d2[2][i] for i in inter):
            bad_c += 1
    print('(c) checked on %d ordered pairs (same atom structure): violations %d' % (tot_c, bad_c))


if __name__ == '__main__':
    main()
