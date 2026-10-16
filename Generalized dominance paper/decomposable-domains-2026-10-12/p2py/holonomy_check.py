#!/usr/bin/env python3
"""P2 / holonomy_check.py (NUMERICS): independent brute-force check of the box condition for a saved
solution: random A, B on all facets, q0 on a grid of each closed edge; reports violations and the
minimum over admissible pairs of max_q0 min(cA.q0, cB.q0) (must be <= 0).  Also re-checks the linear case.
Usage: python3 -I holonomy_check.py eps file.npy mode   (mode: pl | onekink<m>)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import holonomy_pl as H

def load(fname, mode):
    z = np.load(fname)
    if mode == 'pl':
        return H.unpack_global(z)
    m = int(mode[-1]) - 1
    sys.argv = [sys.argv[0], str(H.EPS), str(m)]
    import importlib, holonomy_onekink as O
    O.M = m
    return O.unpack(z)

def worst_box(P, n=200000, seed=0):
    rng = np.random.default_rng(seed)
    q = np.linspace(0, 1, 401)
    worst = -np.inf; wit = None; nviol = 0
    for a in range(3):
        for b in range(3):
            if a == b: continue
            ka = rng.integers(0, 3, n); ta = rng.random(n); kb = rng.integers(0, 3, n); tb = rng.random(n)
            for idx in range(n):
                A = H.pt(ka[idx], ta[idx]); B = H.pt(kb[idx], tb[idx])
                if not (A[a] < 0 < A[b] and B[b] < 0 < B[a] and A[b] * B[a] < -A[a] * -B[b]): continue
                cA = H.chart(ka[idx], A, P); cB = H.chart(kb[idx], B, P)
                vA = q * cA[a] + (1 - q) * cA[b]; vB = q * cB[a] + (1 - q) * cB[b]
                v = np.minimum(vA / np.abs(cA).max(), vB / np.abs(cB).max()).max()
                if v > worst: worst = v; wit = (a + 1, b + 1, ka[idx] + 1, ta[idx], kb[idx] + 1, tb[idx])
                if v > 1e-12: nviol += 1
    return worst, nviol, wit

if __name__ == '__main__':
    fname, mode = sys.argv[2], sys.argv[3]
    P = load(fname, mode)
    w, nv, wit = worst_box(P, n=int(sys.argv[4]) if len(sys.argv) > 4 else 20000)
    print(f"{fname}: max over admissible sampled pairs of max_q min(cA.q, cB.q) (normalised) = {w:.3e}; violations: {nv}; at {wit}")
    x = ((H.KAP + 1) + np.sqrt((H.KAP + 1) ** 2 - 4)) / 2
    w, nv, wit = worst_box(H.linear_params([x, x, x]), n=int(sys.argv[4]) if len(sys.argv) > 4 else 20000)
    print(f"linear x+ : max = {w:.3e}; violations: {nv}; at {wit}")
