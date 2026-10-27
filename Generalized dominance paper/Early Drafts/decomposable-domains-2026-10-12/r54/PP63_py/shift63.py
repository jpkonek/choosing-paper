"""PP63 s.2: exact (IB) identification of shifted records (Fractions only).

For a source a, a target b, a swap set F inside D_ab = {C_a != C_b}, and a pure shift
a_t = a o (1 + t e_w) (t > 0) or a o (1 - t e_w), write sigma = {C_{a_t} != C_a}.
Two-valued records are pairs (P, Q): P = silenced (old answers h, new silent),
Q = answered (old silent, new answers h).  Claims checked cell by cell:
  (i)  rec(C_{a_t} -> C_a[F -> C_b]) = (F+ u sig+, F- u sig-)          when F cap sigma = 0;
  (ii) rec(C_b[F u sigma -> C_{a_t}] -> C_b) = (F+ u (sig+ \\ A_b), F- u (sig- cap A_b));
  (iii) the two coincide  iff  sigma cap D_ab = 0.
Here F+ = F cap (A_a \\ A_b), F- = F cap (A_b \\ A_a), sig+ = A_{a_t} \\ A_a, sig- = A_a \\ A_{a_t}.
Cells are those of the joint arrangement of {a, b, a_t} (PP51 enumerator, unchanged).
We take F = every D_ab cell not meeting sigma (the largest admissible F at cell level).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP57_py'))
from fractions import Fraction as Fr
from post51 import cells, advice

EPS = Fr(3, 10)
MOD = {'A': (Fr(1, 3),) * 3, 'B': (Fr(406, 1200), Fr(421, 1200), Fr(373, 1200)),
       'D': (Fr(406, 1200), Fr(373, 1200), Fr(421, 1200))}


def shift(a, w, t):
    return tuple(a[i] * (1 + (t if i == w else 0)) for i in range(3))


def rec(old, new):
    """old, new: dict cell -> 1 (answer) / 0 (silent).  Returns (P, Q) as frozensets of cells."""
    P = frozenset(k for k in old if old[k] == 1 and new[k] == 0)
    Q = frozenset(k for k in old if old[k] == 0 and new[k] == 1)
    return P, Q


def run():
    ok = True
    rows = []
    for an, bn in (('A', 'B'), ('A', 'D'), ('B', 'A'), ('D', 'A'), ('B', 'D'), ('D', 'B')):
        a, b = MOD[an], MOD[bn]
        for w in range(3):
            for sgn in (1, -1):
                t = Fr(sgn, 1000)
                at = shift(a, w, t)
                G = cells(EPS, [a, b, at])
                Ca = {g: advice(EPS, a, g) for g in G}
                Cb = {g: advice(EPS, b, g) for g in G}
                Ct = {g: advice(EPS, at, g) for g in G}
                assert all(v in (0, 1) for d in (Ca, Cb, Ct) for v in d.values())
                sig = {g for g in G if Ct[g] != Ca[g]}
                Dab = {g for g in G if Ca[g] != Cb[g]}
                F = Dab - sig
                X = {g: (Cb[g] if g in F else Ca[g]) for g in G}            # C_a[F -> C_b]
                Y = {g: (Ct[g] if (g in F or g in sig) else Cb[g]) for g in G}  # C_b[F u sig -> C_{a_t}]
                r1 = rec(Ct, X)
                r2 = rec(Y, Cb)
                Fp = {g for g in F if Ca[g] == 1}
                Fm = {g for g in F if Ca[g] == 0}
                sp = {g for g in sig if Ct[g] == 1}
                sm = {g for g in sig if Ct[g] == 0}
                c1 = r1 == (frozenset(Fp | sp), frozenset(Fm | sm))
                c2 = r2 == (frozenset(Fp | {g for g in sp if Cb[g] == 0}), frozenset(Fm | {g for g in sm if Cb[g] == 1}))
                inter = sig & Dab
                c3 = (r1 == r2) == (len(inter) == 0)
                ok &= c1 and c2 and c3
                # guidance status of the shift record s = rec(C_{a_t} -> C_a) at each world
                gw = []
                for v in range(3):
                    better = worse = 0
                    for g in sig:
                        rt = 1 if Ct[g] == 0 else (0 if g[v] > 0 else 2)
                        ra = 1 if Ca[g] == 0 else (0 if g[v] > 0 else 2)
                        better += rt < ra
                        worse += rt > ra
                    gw.append('G+' if worse == 0 else ('G-' if better == 0 else 'mix'))
                rows.append((an, bn, w + 1, sgn, len(sig), len(Dab), len(inter), r1 == r2, gw, c1 and c2 and c3))
    return ok, rows


if __name__ == '__main__':
    ok, rows = run()
    print('a  b  w  dir  |sigma| |D_ab| |sigma cap D_ab|  identity(i)=(ii)?  shift record per world  checks')
    for r in rows:
        print(f'{r[0]}  {r[1]}  {r[2]}  {"+" if r[3] > 0 else "-"}    {r[4]:4d}   {r[5]:4d}     {r[6]:4d}            {str(r[7]):5s}            {r[8]}   {r[9]}')
    print('formulas (i), (ii) and the criterion (iii) hold in every case:', ok)
    print('ALL PASS' if ok else 'SOME FAIL')
