"""N1-N2 (NUMERICS): guidance along the exact loop, (2V), u1 increments of the three moves,
layer composition by odd world, and all pairwise pure-shift relations inside one loop."""
import numpy as np
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib73 import *

G = sample(2_000_000)
odd = classes(G)
h = np.sign(G.sum(1))
for a in [1.01, 1.03, 1.1, 1.17]:
    m = loop(a)
    X = [advice(G, mi) for mi in m]
    R = [ranks(G, x) for x in X]
    print(f'=== a = {a}:  m1 = {np.round(m[1],5)}, m2 = {np.round(m[2],5)}')
    # (2V): every answer has the sign of h on mixed points
    for i in range(3):
        bad = ((X[i] != 0) & (X[i] != h) & (odd >= 0)).sum()
        print(f'  (2V) member {i}: answers of sign -h on mixed points: {bad}')
    for (i, j, w) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        worse = (R[j][:, w] < R[i][:, w]).sum()   # new side strictly better at w
        strict = (R[j][:, w] > R[i][:, w]).sum()
        print(f'  move P{i}->P{j}: new side better at world {w+1} on {worse} pts, worse on {strict} pts (guidance: P{i} <=_{w+1} P{j})')
        lay = X[i] != X[j]
        comp = [int((lay & (odd == k)).sum()) for k in range(3)]
        V = Phi(G, X[j]) - Phi(G, X[i])
        print(f'     layer pts by odd world {comp};  V(P{i}->P{j}) = {np.round(V,5)} (sum {V.sum():+.1e})')
        # pointwise relation at the other two worlds
        for v in range(3):
            if v == w: continue
            bet = (R[j][:, v] < R[i][:, v]).sum(); wor = (R[j][:, v] > R[i][:, v]).sum()
            print(f'       world {v+1}: new better on {bet}, worse on {wor}  -> mixed: {bet>0 and wor>0}')
    tot = sum(Phi(G, X[j]) - Phi(G, X[i]) for (i, j) in [(0, 1), (1, 2), (2, 0)])
    print('  loop sum of V:', np.round(tot, 8))
