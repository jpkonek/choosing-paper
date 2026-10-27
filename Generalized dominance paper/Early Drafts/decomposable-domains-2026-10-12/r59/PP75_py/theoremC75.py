"""Theorem C (closed form) versus the brute-force atom checker, on random H-type rivals.
For committed Z, candidate B, rival X (all two-valued h/S on the mixed cells):
  P1 = patterns of Z -> B on Delta(Z,B) \ Delta(Z,X)   (B's moves not shared by X)
  P2 = patterns of Z -> X on Delta(Z,X) \ Delta(Z,B)   (X's moves not made by B)
Closed forms:  N1  <=>  U P1  u  U{comp(p) : p in P2} = {1,2,3}
               N2  <=>  P2 nonempty
               Z defeated (coupled refusals with all copies, incl. the base rule)  <=>  exists k:
                 (Da_k) {!=k} in P1, P1 subset {{!=k},{i},{j}}, k in every p of P2,
                        and (P2 nonempty or P1 meets {{i},{j}});   or
                 (Db_k) P1 nonempty, every p in P1 contains k, P2 subset {{!=k}},
                        and (P2 nonempty or {k} in P1)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import random, itertools
from geo75 import *

random.seed(7575)
W = frozenset(range(3))
def comp(p): return W - p

def closed_forms(atoms, Z, X='X', B='B'):
    P1, P2 = set(), set()
    for a in atoms:
        h, z, b, x = a['h'], a['vals'][Z], a['vals'][B], a['vals'][X]
        if z != b and z == x: P1.add(pattern(z, b, h))
        if z != x and z == b: P2.add(pattern(z, x, h))
    cov = set()
    for p in P1: cov |= p
    for p in P2: cov |= comp(p)
    n1 = (cov == set(W))
    n2 = len(P2) > 0
    dfe = False
    for k in range(3):
        i, j = [w for w in range(3) if w != k]
        nk = frozenset([i, j]); si, sj = frozenset([i]), frozenset([j])
        if nk in P1 and P1 <= {nk, si, sj} and all(k in p for p in P2) and (P2 or (P1 & {si, sj})):
            dfe = True
        if P1 and all(k in p for p in P1) and P2 <= {nk} and (P2 or frozenset([k]) in P1):
            dfe = True
    return n1, n2, dfe, P1, P2

def rnd_model(sp):
    return tuple(F(random.randint(1000 - sp, 1000 + sp), 1000) for _ in range(3))

if __name__ == "__main__":
    tot = mism = 0; ndef = 0
    for trial in range(400):
        Zm, Bm = rnd_model(120), rnd_model(120)
        if random.random() < 0.3:   # single shifts of B relative to Z
            k = random.randrange(3); f = random.choice([F(11, 10), F(10, 11)])
            Bm = tuple(Zm[i] * (f if i == k else 1) for i in range(3))
        extra = [rnd_model(120)] if random.random() < 0.5 else []
        cs = cells([Zm, Bm] + extra)
        atoms = []
        mode = random.choice(['near', 'free'])
        for ci, c in enumerate(cs):
            h = c['pt']
            if htype(h)[0] == 'U':
                atoms.append({'cell': ci, 'h': h, 'vals': {'Z': 'h', 'B': 'h', 'X': 'h'}}); continue
            z, b = answer(Zm, h), answer(Bm, h)
            if mode == 'near' and len(set([z, b] + [answer(e, h) for e in extra])) == 1 and random.random() < 0.8:
                xs = [z]
            else:
                r = random.random()
                xs = ['h'] if r < 0.35 else (['S'] if r < 0.7 else ['h', 'S'])
            for xv in xs:
                atoms.append({'cell': ci, 'h': h, 'vals': {'Z': z, 'B': b, 'X': xv}})
        n1b = N1(atoms)[0]
        n2b = N2(atoms, 'Z')[0]
        dfb = defeated(atoms, 'Z') is not None
        n1, n2, dfe, P1, P2 = closed_forms(atoms, 'Z')
        tot += 1; ndef += dfb
        if (n1b, n2b, dfb) != (n1, n2, dfe):
            mism += 1
            print('MISMATCH', (n1b, n2b, dfb), (n1, n2, dfe), sorted(map(pname, P1)), sorted(map(pname, P2)))
    print('random configurations', tot, 'defeated', ndef, 'mismatches', mism)
    print('ALL PASS' if mism == 0 else 'FAIL')
