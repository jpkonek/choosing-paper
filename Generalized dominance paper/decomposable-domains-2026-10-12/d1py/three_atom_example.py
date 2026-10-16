"""D1 Example D1.0 (NUMERICS): the referee's one-atom field (B2_referee §6) extended to three corner atoms
with the symmetry of T1.  Domain WITHOUT (LF): advice range {+,0} on G_k, {0,-} on -G_k, singleton elsewhere.
Checks:
 E1  every gamble of G_k has the corner pattern of r_k (so the G_k are disjoint and c = b_k is strictly guiding);
 E2  for every subset S of atoms, D_T1 minus the union of G_k (k in S) equals D_{co(T1 u {m_k : k in S})}
     on random gambles (so every Bayes model, at every q, is coherent: (gamma) holds with E = three chords);
 E3  b_k . u = 0, the b_k positively span 1^perp, so T1 is an interior point of the zonotope face at u;
 E4  the world-i-best u-Bayes models K^i (lexicographic limits toward e_i) and T1 subset K^i subset co(T1 u e_i);
 E5  (LF) is what fails: the vertex model at e_2 contains v_1, so the middle-arc gamble of F_1 is not
     strictly accepted near e_2 (UVN fails), unlike on any (LF) domain.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from itertools import combinations
from t1geom import T1, kappa, corner_ray, P, tangent_point, E, facet_param

rng = np.random.default_rng(11)
out = []
for eps in [0.05, 0.2, 0.3, 0.6, 0.9]:
    V = T1(eps); u = np.ones(3) / 3
    # corners: atom k=(i,j) at corner ray r_ij, cap beyond edge [v_i,v_j], outer point o_ij
    atoms = [(0, 1), (1, 2), (2, 0)]
    m = {}; pat = {}; b = {}
    for (i, j) in atoms:
        o = tangent_point(V, i, j, eps)
        mid = 0.5 * (V[i] + V[j])
        m[(i, j)] = mid + 0.5 * (o - mid)               # a point in int cap_ij
        r = corner_ray(V, i, j)
        pat[(i, j)] = np.sign(r)
        bb = np.where(pat[(i, j)] > 0, 2.0, -1.0)       # (-1,-1,2)-type, b.u = 0
        b[(i, j)] = bb
    # E1
    bad1 = 0; cnt = {a: 0 for a in atoms}
    for _ in range(200000):
        g = rng.normal(size=3)
        if P(V, g) <= 0:
            continue
        for a in atoms:
            K = V + [m[a]]
            if P(K, g) < 0:          # g in G_a  (T1 accepts, K_a strictly rejects)
                cnt[a] += 1
                if not np.all(np.sign(g) == pat[a]):
                    bad1 += 1
    # E2
    bad2 = 0; n2 = 0
    for S in [s for r_ in range(4) for s in combinations(atoms, r_)]:
        K = V + [m[a] for a in S]
        for _ in range(20000):
            g = rng.normal(size=3)
            inG = any(P(V, g) > 0 and P(V + [m[a]], g) < 0 for a in S)
            lhs = (P(V, g) > 0) and not inG
            rhs = P(K, g) > 0
            # ignore boundary cases (null)
            if abs(P(K, g)) < 1e-12:
                continue
            n2 += 1
            if lhs != rhs:
                bad2 += 1
    # E3
    B = np.array([b[a] for a in atoms])
    ok3 = np.allclose(B @ u, 0) and np.allclose(B.sum(0), 0)
    # E4
    K4 = []
    for i in range(3):
        th = E[i] - u
        rejected = [a for a in atoms if th @ b[a] < 0]
        K4.append((i, [a for a in rejected]))
    # E5: vertex model at e_2 (index 1): accept G_a iff b_a[1] > 0
    rej2 = [a for a in atoms if b[a][1] < 0]
    K2 = V + [m[a] for a in rej2]
    h, r0, r1 = facet_param(V, 0)
    # middle arc of F_1: find tau with h2,h3>0
    taus = np.linspace(0, 1, 2001); mids = [t for t in taus if h(t)[1] > 0 and h(t)[2] > 0]
    hm = h(mids[len(mids) // 2])
    P2 = P(K2, hm)
    out.append(f"eps={eps}: E1 atom counts {list(cnt.values())}, pattern violations {bad1}; "
               f"E2 coherence mismatches {bad2}/{n2}; E3 b.u=0 & sum b=0: {ok3}; "
               f"E4 K^i rejects atoms {[(i, len(r)) for i, r in K4]}; "
               f"E5 P_(K^(2))(middle-arc gamble of F_1) = {P2:.2e} (UVN would need >0)")
print("\n".join(out))
