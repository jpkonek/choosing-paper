"""S34 referee: independent grid check of S3.1 with a NON-uniform disjoint family (measures 24,12,6,3,1 cells),
so that the section ends differ across j (S3's own grid used equal measures). Integer units: cell mass 1, N cell mass WN.
World 1 tails (N at x=2), world 2 heads (N at x=-1); band U translates by g_j = 1_{A_j} - 1_{c_a}, g'_j = 1_{A_j cap c_b0} - 1_{d_b0}.
Checks: (K) and (U) for 600 random models at all interior cuts; nonpositive vectors rejected; world-1 section of
E_1 X = d_a ends at n - |A_j| via A_j (referee formula 1 - mu(A_j)); world-2 section of E_2 X = c_b0 starts at |F'_j|.
Run: python3 -I s31_grid.py"""
import random
import numpy as np
random.seed(3)
n, WN = 96, 4
ia, ib0 = 24, 72
cells = list(range(ia, n)); random.shuffle(cells)
sizes = [24, 12, 6, 3, 1]
A, p = [], 0
for s in sizes:
    A.append(sorted(cells[p:p + s])); p += s
# make sure each A_j meets c_b0
for j in range(len(A)):
    if not any(k < ib0 for k in A[j]):
        A[j][0] = next(k for k in range(ia, ib0) if all(k not in B for B in A))
def vec(pos=(), neg=(), N=0):
    d = np.zeros(n + 1, int)
    for k in pos: d[k] += 1
    for k in neg: d[k] -= 1
    d[n] = N; return d
def tails(d):
    t = np.cumsum(d[:n][::-1])[::-1] + d[n] * WN
    return np.concatenate([t, [d[n] * WN, d[n]]])
def heads(d):
    h = np.cumsum(d[:n]) + d[n] * WN
    return np.concatenate([[d[n] * WN], h, [d[n]]])
G1 = [tails(vec(pos=A[j], neg=range(ia))) for j in range(len(A))]
G2 = [heads(vec(pos=[k for k in A[j] if k < ib0], neg=range(ib0, n))) for j in range(len(A))]
acc1 = lambda d: (tails(d) >= 0).all() or any((tails(d) >= g).all() for g in G1)
acc2 = lambda d: (heads(d) >= 0).all() or any((heads(d) >= g).all() for g in G2)
bad = sum(1 for _ in range(5000) if (lambda d: d.any() and (acc1(d) or acc2(d)))(np.array([random.choice([-1, 0, 0]) for _ in range(n + 1)])))
print("nonpositive nonzero vectors accepted:", bad)
Kf = Uf = 0
for _ in range(600):
    q = random.random()
    S = {k for k in range(n) if random.random() < q}
    if random.random() < 0.5:
        b = random.randrange(1, n); S = set(range(b)) ^ {k for k in range(n) if random.random() < 0.04}
    Nn = 1 if random.random() < 0.2 else 0
    for b in range(1, n):
        x1 = vec(pos=S, neg=range(b), N=Nn)
        x2 = vec(pos=[k for k in range(n) if k not in S], neg=range(b, n), N=Nn)
        if not (acc1(x1) or acc2(x2)): Kf += 1
        if not (S == set(range(b)) and Nn == 0) and acc1(-x1) and acc2(-x2): Uf += 1
print("(K) failures:", Kf, " (U) failures:", Uf)
# sections
E = range(ia, n)
for j in range(len(A)):
    end = max(b for b in range(n + 1) if (tails(vec(pos=[k for k in E if k >= b], neg=[k for k in range(b) if k < ia])) >= G1[j]).all())
    print(f"  world 1, E_1 = d_a, via A_{j}: |A_j|={len(A[j])}, section end {end} cells, predicted n-|A_j| = {n-len(A[j])}")
for j in range(len(A)):
    Fp = len([k for k in A[j] if k < ib0])
    # E_2 X = c_b0 ; C_t <=_2 X iff 1_{E2X \ d_t} - 1_{d_t \ E2X} accepted
    st = min(t for t in range(n + 1) if (heads(vec(pos=[k for k in range(ib0) if k < t], neg=[k for k in range(t, n) if k >= ib0])) >= G2[j]).all())
    print(f"  world 2, E_2 = c_b0, via F'_{j}: |F'_j|={Fp}, section start {st} cells, predicted |F'_j| = {Fp}")
print("So with an infinite disjoint family the two sections are [0,1) and (0,1]: open at both worlds (mirror).")
