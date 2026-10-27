"""endorse77: PP77 Theorem 4.2 (forced u1-NON-endorsed acceptance behind the essential mixed refusal).

Part 1 (CHECKED membership; NUMERICS masses).  S in S_M (S = L1 u L3 u (lose-A2 n half 0)), same-ray
defender B_tau.  Z0 = B[(F \\ L(tau)) u (L1 \\ L(tau)) -> T];  Z1 = Z0 + (Y : S -> h), Y = off-D odd-3 cells
of type (A,3) where B is silent (a fraction of their mass).  Check: Z0, Z1 lie in B's world-1 refusal
family (PP76 Thm 1.1); Z0 is strictly reverse-guidance at 3; V-signs as predicted by Thm 4.2.
Part 2 (NUMERICS).  Every PP79 pool candidate B2 passing (N1) + both agreement obstructions on the S_M
splice: LP over B's world-1 refusal family (H-valued, atoms splittable):  t* = min max(V2, V3).
t* < 0 means: B must accept a rival with V_2 < 0 and V_3 < 0 at world 2 or 3 (or is defeated).
Run: python3 -I -B endorse77.py > endorse77.out
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'PP79_py'))
from lib77 import *
from scipy.optimize import linprog

r = F(20, 21)
T = post((1, 1, 1)); B = post((1, 1, r))

def in_family(At, Cn, w, Bv, X, Z):
    fam = family(At, Cn, None, None, w, Xvals=X, Bvals=Bv)
    if fam is None: return False
    strict = False
    for i, o in enumerate(fam):
        d = dict(o)
        if Z[i] not in d: return False
        strict = strict or d[Z[i]]
    return strict

def spliceM(At):
    X, F_ = [], set()
    for i, a in enumerate(At):
        t, b = a['vals']['T'], a['vals']['B']
        if t == b: X.append(t); continue
        loseA2 = (a['type'] == ('A', 1) and t == 'h' and b == 'S')
        inS = (a['o'] in (0, 2)) or (a['o'] == 1 and loseA2 and a['half'] == 0)
        if a['o'] == 1 and inS: F_.add(i)
        X.append(b if inS else t)
    return X, F_

def part1():
    print('[1] same-ray defenders on S_M: forced non-endorsed rival at B')
    for s in (F(41, 42), F(83, 84)):
        for R in (0.6, 1.8, 6.0):
            mods = {'T': T, 'B': B, 'Bt': post((1, 1, s))}
            At = atoms(mods); m = masses(mods, At, R=R)
            Bv = [a['vals']['B'] for a in At]; Bt = [a['vals']['Bt'] for a in At]; Tv = [a['vals']['T'] for a in At]
            X, Fs = spliceM(At)
            assert N1(At, Bt, X) and corr(At, 'T', Bt, X) and corr(At, 'B', Bt, X)
            D = {i for i in range(len(At)) if Bt[i] != X[i]}
            Lt = {i for i in range(len(At)) if Bt[i] != Tv[i]}
            Fo = {i for i in Fs if i not in Lt}
            L1o = {i for i, a in enumerate(At) if Tv[i] != Bv[i] and a['o'] == 0 and i not in Lt}
            f = sum(m[i] for i in Fo); q1 = sum(m[i] for i in L1o)
            Z0 = [Tv[i] if i in Fo | L1o else Bv[i] for i in range(len(At))]
            in1 = in_family(At, 'B', 0, Bt, X, Z0)
            rg3 = all(le(Z0[i], Bv[i], a['h'], 2) for i, a in enumerate(At)) and Z0 != Bv
            V0 = Vrec(At, m, Bv, Z0)
            Ycand = [i for i, a in enumerate(At) if i not in D and a['type'] == ('A', 2) and Bv[i] == 'S']
            ymax = sum(m[i] for i in Ycand)
            lo, hi = max(0.0, 2 * f - q1), (f + q1) / 2
            y = (lo + hi) / 2 if 2 * f >= q1 else 0.0
            lam = min(1.0, y / ymax) if ymax > 0 else 0.0
            Z1 = list(Z0)
            for i in Ycand: Z1[i] = 'h'
            in1b = in_family(At, 'B', 0, Bt, X, Z1)
            V1 = V0 + lam * (Vrec(At, m, Bv, Z1) - V0)
            print('  s=%s R=%.1f: f=%.5f q1=%.5f (f<q1: %s) | Z0 in fam1 %s, rev-guid at 3 %s, V(B->Z0)=%s'
                  % (s, R, f, q1, f < q1, in1, rg3, np.round(V0 / q1, 3)))
            print('      Z1 (y=%.5f, Y avail %.5f) in fam1 %s, V(B->Z1)/q1=%s  -> V2<0 and V3<0: %s'
                  % (y, ymax, in1b, np.round(V1 / q1, 3), bool(V1[1] < 0 and V1[2] < 0)))

def part2():
    from mixed79 import pool
    print('\n[2] PP79 pool on the S_M splice: LP min max(V2,V3) over B\'s world-1 refusal family')
    P = pool()
    n = neg = neg2 = 0; worst = []; tal = {}
    for name, K in P.items():
        mods = {'T': T, 'B': B, 'B2': K}
        At = atoms(mods)
        Bv2 = [a['vals']['B2'] for a in At]
        X, _ = spliceM(At)
        if not (N1(At, Bv2, X) and corr(At, 'T', Bv2, X) and corr(At, 'B', Bv2, X)): continue
        fam = family(At, 'B', None, None, 0, Xvals=X, Bvals=Bv2)
        if fam is None: continue
        m = masses(mods, At, n=120_000, R=1.2)
        Bv = [a['vals']['B'] for a in At]
        var = []  # (atom, value)
        for i, o in enumerate(fam):
            for v, sflag in o:
                if v in ('h', 'S') and Bv[i] in ('h', 'S'): var.append((i, v))
        nv = len(var)
        # objective: min t ; variables x_1..x_nv, t
        c = np.zeros(nv + 1); c[-1] = 1.0
        Vcol = np.zeros((3, nv))
        for j, (i, v) in enumerate(var):
            if v != Bv[i]:
                d = (1.0 if v == 'h' else 0.0) - (1.0 if Bv[i] == 'h' else 0.0)
                Vcol[:, j] = d * m[i] * unit(At[i])
        A_ub = np.zeros((2, nv + 1)); A_ub[0, :nv] = Vcol[1]; A_ub[1, :nv] = Vcol[2]; A_ub[:, -1] = -1
        atoms_used = sorted({i for i, _ in var})
        A_eq = np.zeros((len(atoms_used), nv + 1))
        for j, (i, v) in enumerate(var): A_eq[atoms_used.index(i), j] = 1.0
        ok_atoms = len(atoms_used) == len(At)
        if not ok_atoms: continue
        res = linprog(c, A_ub=A_ub, b_ub=np.zeros(2), A_eq=A_eq, b_eq=np.ones(len(atoms_used)),
                      bounds=[(0, 1)] * nv + [(None, None)], method='highs')
        n += 1
        tstar = res.x[-1] / max(m.sum(), 1e-12)
        cat = ''.join(ch for ch in name.split('(')[0] if not ch.isdigit())
        tal.setdefault(cat, [0, 0, 0])
        if tstar < -1e-6: neg += 1; tal[cat][0] += 1; continue
        # (ii) rivals refused at 1 AND at 3 (strictly reverse-guidance at 3, or in the world-3 family): min V2
        fam3 = family(At, 'B', None, None, 2, Xvals=X, Bvals=Bv2)
        best = None
        for mode in ('rg3', 'fam3'):
            if mode == 'fam3' and fam3 is None: continue
            keep = []
            for j, (i, v) in enumerate(var):
                if mode == 'rg3': okv = le(v, Bv[i], At[i]['h'], 2)
                else: okv = v in dict(fam3[i])
                if okv: keep.append(j)
            if len({var[j][0] for j in keep}) < len(At): continue
            c2 = np.zeros(nv); c2[keep] = Vcol[1, keep]
            bnds = [(0, 1) if j in set(keep) else (0, 0) for j in range(nv)]
            r2 = linprog(c2, A_eq=A_eq[:, :nv], b_eq=np.ones(len(atoms_used)), bounds=bnds, method='highs')
            if r2.status == 0:
                val = r2.fun / max(m.sum(), 1e-12)
                best = val if best is None else min(best, val)
        if best is not None and best < -1e-6: neg2 += 1; tal[cat][1] += 1
        else: worst.append((name, round(tstar, 5), best)); tal[cat][2] += 1
    print('  candidates evaluated %d' % n)
    print('  (i)  a world-1-refused rival with V2<0 and V3<0:                     %d' % neg)
    print('  (ii) otherwise, a rival refused at 1 and 3 with V2<0:                 %d' % neg2)
    print('  neither (endorsed alternatives possible as far as these tests go): %d' % len(worst))
    print('  by category [(i), (ii), neither]:', tal)
    print('  e.g.', worst[:8])
    from balanced79 import balanced_capable
    surv = [nm for nm, _, _ in worst if not balanced_capable(P[nm])]
    print('\n[3] exceptions of [2] that are ALSO free of balanced T-pieces (PP79 Cor A4 test): %d' % len(surv))
    print('  ', surv)
    return surv

if __name__ == '__main__':
    part1()
    part2()
