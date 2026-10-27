"""N3 (NUMERICS; the statements are PROVED in PP73 sec.2): fill-splice identities of one exact loop.
For the edge P_i ->(k) P_{i+1} with predecessor P_{i-1}:
 S_k := Sil(P_i) & M_k & {P_i != P_{i-1}}.  Claims: (a) on S_k, P_{i-1} = A (so the class-k fill of P_i on
 E subset S_k is the splice P_i[E -> P_{i-1}]); (b) on S_k the repairer P_{i+1} = A (agreement obstruction).
Also: mass of S_k and of the remaining silent class-k region."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib73 import *

G = sample(2_000_000)
odd = classes(G); A = majority(G)
for a in [1.01, 1.05, 1.17]:
    P = [advice(G, mi) for mi in loop(a)]
    print(f'=== a = {a}')
    for (i, k) in [(0, 2), (1, 0), (2, 1)]:      # P0 class 3 -> P1, P1 class 1 -> P2, P2 class 2 -> P0
        prev, nxt = P[(i - 1) % 3], P[(i + 1) % 3]
        sil = (P[i] == 0) & (odd == k)
        S = sil & (P[i] != prev)
        print(f'  source P{i}, class {k+1}: |Sil&M_k| = {sil.sum()}, |S_k| = {S.sum()}; '
              f'pred = A on S_k: {(prev[S] == A[S]).mean():.4f}; repairer P{(i+1)%3} = A on S_k: {(nxt[S] == A[S]).mean():.4f}; '
              f'repairer = A on rest of Sil&M_k: {(nxt[sil & ~S] == A[sil & ~S]).mean():.4f}')
