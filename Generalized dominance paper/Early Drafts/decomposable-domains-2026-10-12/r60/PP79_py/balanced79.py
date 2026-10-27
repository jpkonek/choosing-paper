"""balanced79: which coherent models N admit a u1-BALANCED non-conic record (F : T -> N), F inside
{N != T} (Theorem A3 / Cor A4 of PP79: under a u1-endorsed base sectioned along three down-shift
rays, every such record out of T is accepted at all three worlds, so a committed N of this kind is
weakly dominated by the incoherent N[F -> T]).

u1 per unit |g|-mass on a mixed cell (PP56 Section 4.1): answer h(g) on R: -|Wr| on Cor, +|Cor| on Wr
... in PP56's notation k_c = |Wr|, k_r = |Cor|; S: 0; -h ("otherwise"): k_c = |Wr|, k_r = 2|Cor|.
(All cells of {N != T} for the candidates below lie in the (2V) region R of the reference family when
N is a (2V) posterior; for other candidates the value is the R-row and the statement is a test of
flip structure only.)
A record (F : T -> N) restricted to cells c with |g|-masses x_c >= 0 has V = sum_c x_c (u1(N_c) - u1(T_c)).
Balanced-capable  <=>  0 = sum x_c v_c has a solution x >= 0, x != 0  (LP).
Radial halves make any such F non-conic.  Open cells contain compact pieces at positive distance from
the boundary of A(T), so the support can be kept off the thin layers of three interior ray carriers.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib79 import *
from mixed79 import pool, T, B, r
import numpy as np
from scipy.optimize import linprog

def u1(x, h):
    if x == 'S': return np.zeros(3)
    cor = [w for w in range(3) if rank(x, h, w) == 0]
    wr = [w for w in range(3) if rank(x, h, w) == 2]
    if x == 'h': kc, kr = len(wr), len(cor)
    else: kc, kr = len(wr), 2 * len(cor)
    v = np.zeros(3)
    for w in cor: v[w] = -kc
    for w in wr: v[w] = kr
    return v

def balanced_capable(K):
    At = atoms({'T': T, 'N': K})
    vecs = []
    for a in At:
        if a['half'] == 1: continue
        t, n = a['vals']['T'], a['vals']['N']
        if t != n:
            vecs.append(u1(n, a['h']) - u1(t, a['h']))
    if not vecs: return None
    A = np.array(vecs).T
    m = A.shape[1]
    A_eq = np.vstack([A, np.ones((1, m))]); b_eq = np.array([0, 0, 0, 1.0])
    res = linprog(np.zeros(m), A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * m, method='highs')
    return res.status == 0

if __name__ == '__main__':
    P = pool()
    groups = {}
    for name, K in P.items():
        g = name.split('(')[0].rstrip('0123456789')
        cap = balanced_capable(K)
        groups.setdefault(g, [0, 0, []])
        groups[g][0] += 1
        if cap: groups[g][1] += 1
        elif len(groups[g][2]) < 6: groups[g][2].append(name)
    for g, (n, c, ex) in groups.items():
        print('%-4s candidates %4d  balanced-capable %4d  examples NOT capable: %s' % (g, n, c, ex))
    # exact statements
    assert balanced_capable(B) is False
    for s in (F(83, 84), F(41, 42)):
        assert balanced_capable(post((1, 1, s))) is False
    assert balanced_capable(post((F(21, 20), F(441, 400), 1))) is True
    print('B and same-ray points: not capable; generic-order-type posterior (21/20, 441/400, 1): capable: PASS')
