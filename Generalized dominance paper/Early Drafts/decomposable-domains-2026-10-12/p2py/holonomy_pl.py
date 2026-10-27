#!/usr/bin/env python3
"""P2 / holonomy_pl.py  (NUMERICS; run with python3 -I)

Question: which rigidity in the additive chain for T1 is load-bearing?
The chain (writeup Sec. 4) produces, for each facet F_k, a facet map c_k : F_k -> 1^perp
(cluster-line normals) with
  (sign)    c_k(h) has the strict sign pattern of h on relint F_k (zeros exactly at crossings),
  (cross)   c_k(w_ik)_i = 0 at each crossing w_ik,
  (NS)      c_k(r) and c_j(r) positively proportional at each corner ray r = F_k cap F_j,
  (box)     for every ordered pair (a,b), A in relint F_k, B in relint F_k',
            A_a<0<A_b, B_b<0<B_a, A_b B_a < |A_a||B_b|:  c_k(A).q<=0 or c_k'(B).q<=0 on [e_a,e_b],
  (LIN)     c_k LINEAR on span F_k (projectivity, Cor PCNS) -- derived from coherence + pivot chords.
We test: (sign)+(cross)+(NS)+(box) with (LIN) replaced by "continuous, piecewise linear with one
break ray per facet", or with (LIN) dropped on one facet only.

Box test, exact reduction: with s_A = c_b/(c_b-c_a), s_B = -c_b/(c_a-c_b) (c = chart vector),
rho_A = A_b/|A_a|, sigma_B = |B_b|/B_a, the box holds iff  s_A <= s_B  whenever rho_A < sigma_B.
We sample facet points finely (grid) and report the box margin  min (s_B - s_A)  over admissible pairs.
"""
import sys
import numpy as np
from scipy.optimize import minimize

EPS = float(sys.argv[1]) if len(sys.argv) > 1 else 0.3
KAP = (1 + 2 * EPS) / (1 - EPS)
C0 = (1 - EPS) / 3
V = [C0 * np.ones(3) + EPS * np.eye(3)[k] for k in range(3)]
R12 = np.array([-1.0, -1.0, KAP + 1]); R23 = np.array([KAP + 1, -1.0, -1.0]); R31 = np.array([-1.0, KAP + 1, -1.0])
# facet k: crossing coordinates (i,j); 'i-end' corner (h_i<0 there) and 'j-end' corner
FAC = {0: dict(i=1, j=2, ri=R12, rj=R31),   # F_1: coords 2,3 cross; h_2<0 at r12, h_3<0 at r31
       1: dict(i=2, j=0, ri=R23, rj=R12),   # F_2: coords 3,1;      h_3<0 at r23, h_1<0 at r12
       2: dict(i=0, j=1, ri=R31, rj=R23)}   # F_3: coords 1,2;      h_1<0 at r31, h_2<0 at r23
for k, f in FAC.items():
    assert abs(V[k] @ f['ri']) < 1e-12 and abs(V[k] @ f['rj']) < 1e-12
    assert f['ri'][f['i']] < 0 and f['rj'][f['j']] < 0

def pt(k, tau):
    f = FAC[k]; return (1 - tau) * f['ri'] + tau * f['rj']

def cross_tau(k, coord):
    f = FAC[k]; a, b = f['ri'][coord], f['rj'][coord]; return a / (a - b)

def chart(k, h, P):
    """P[k] = (lamA, alA, beA, lamB, alB, beB, tb). Sector A (i-end): c_i = lamA h_i, c_j = alA h_i + beA h_j.
    Sector B (j-end): c_j = lamB h_j, c_i = alB h_i + beB h_j. Break ray b = pt(k,tb). c_k = -(c_i+c_j)."""
    f = FAC[k]; i, j = f['i'], f['j']
    lamA, alA, beA, lamB, alB, beB, tb = P[k]
    b = pt(k, tb)
    # which sector: h = lam*ri + mu*b with lam,mu>=0  <=>  sector A
    Mt = np.array([f['ri'][[i, j]], b[[i, j]]]).T
    lam, mu = np.linalg.solve(Mt, h[[i, j]])
    c = np.zeros(3)
    if lam >= -1e-12 and mu >= -1e-12:
        c[i] = lamA * h[i]; c[j] = alA * h[i] + beA * h[j]
    else:
        c[j] = lamB * h[j]; c[i] = alB * h[i] + beB * h[j]
    c[k] = -(c[i] + c[j])
    return c

def continuity_fix(P):
    """Enforce continuity at the break: given lamA, alA, beA and lamB, solve alB, beB from
    c(b) equal on both sides (2 linear equations)."""
    Q = {}
    for k in range(3):
        f = FAC[k]; i, j = f['i'], f['j']
        lamA, alA, beA, lamB, _, _, tb = P[k]
        b = pt(k, tb)
        ci = lamA * b[i]; cj = alA * b[i] + beA * b[j]
        # side B: cj = lamB b_j must equal cj  -> fixes lamB ; ci = alB b_i + beB b_j -> one eq, two unknowns
        lamB = cj / b[j]
        # choose alB, beB with alB*b_i + beB*b_j = ci ; extra freedom kept as parameter 'alB'
        alB = P[k][4]; beB = (ci - alB * b[i]) / b[j]
        Q[k] = (lamA, alA, beA, lamB, alB, beB, tb)
    return Q

TAU = np.linspace(0, 1, 801)[1:-1]

def charts(k, tau, P):
    """vectorised: points and chart vectors on facet k at parameters tau"""
    f = FAC[k]; i, j = f['i'], f['j']
    lamA, alA, beA, lamB, alB, beB, tb = P[k]
    H = (1 - tau)[:, None] * f['ri'][None, :] + tau[:, None] * f['rj'][None, :]
    C = np.zeros_like(H)
    A = tau <= tb
    C[A, i] = lamA * H[A, i]; C[A, j] = alA * H[A, i] + beA * H[A, j]
    B = ~A
    C[B, j] = lamB * H[B, j]; C[B, i] = alB * H[B, i] + beB * H[B, j]
    C[:, k] = -(C[:, i] + C[:, j])
    return H, C

def sign_violation(P, tau=TAU):
    worst = 0.0
    for k in range(3):
        H, C = charts(k, tau, P)
        m = np.abs(H) > 1e-9
        worst = min(worst, (C * np.sign(H))[m].min())
    return worst  # <0 means violated

def ns_residual(P):
    res = []
    for (k, j, r) in [(0, 1, R12), (1, 2, R23), (2, 0, R31)]:
        a = chart(k, r * 1.0, P); b = chart(j, r * 1.0, P)
        # project to 1^perp coordinates
        a2 = a - a.mean(); b2 = b - b.mean()
        cr = a2[0] * b2[1] - a2[1] * b2[0]
        res.append(cr / (np.linalg.norm(a2) * np.linalg.norm(b2)))
        res.append(-min(0.0, a2 @ b2))
    return np.array(res)

def box_margin(P, tau=TAU):
    HC = [charts(k, tau, P) for k in range(3)]
    H = np.vstack([x[0] for x in HC]); C = np.vstack([x[1] for x in HC])
    K = np.concatenate([np.full(len(tau), k) for k in range(3)])
    worst = np.inf; arg = None
    for a in range(3):
        for b in range(3):
            if a == b: continue
            mA = (H[:, a] < 0) & (H[:, b] > 0) & (C[:, a] < 0) & (C[:, b] > 0)
            mB = (H[:, b] < 0) & (H[:, a] > 0) & (C[:, b] < 0) & (C[:, a] > 0)
            if not mA.any() or not mB.any(): continue
            rho = H[mA, b] / -H[mA, a]; sA = C[mA, b] / (C[mA, b] - C[mA, a])
            sig = -H[mB, b] / H[mB, a]; sB = -C[mB, b] / (C[mB, a] - C[mB, b])
            o = np.argsort(-sig); sig = sig[o]; sB = np.minimum.accumulate(sB[o])
            n = np.searchsorted(-sig, -rho, side='left')
            ok = n > 0
            if not ok.any(): continue
            marg = sB[n[ok] - 1] - sA[ok]
            t = np.argmin(marg)
            if marg[t] < worst:
                worst = marg[t]; arg = (a + 1, b + 1, int(K[mA][ok][t]) + 1, float(rho[ok][t]), float(sA[ok][t]))
    return worst, arg

def linear_params(x):
    """Linear facet maps with crossing rates: F_1 (lam2,lam3)=(x1,1), F_2 (lam3,lam1)=(x2,1), F_3 (lam1,lam2)=(x3,1)."""
    P = {}
    for k in range(3):
        P[k] = (x[k], 0.0, 1.0, 1.0, x[k], 0.0, 0.5)
    return P


def unpack_global(z):
    P = {}
    for k in range(3):
        lamA, alA, beA, alB, tb = z[5 * k:5 * k + 5]
        ti, tj = cross_tau(k, FAC[k]['i']), cross_tau(k, FAC[k]['j'])
        tb = ti + (tj - ti) / (1 + np.exp(-tb))          # break strictly between the crossings
        P[k] = (np.exp(lamA), alA, np.exp(beA), 1.0, alB, 0.0, tb)
    return continuity_fix(P)


def polish(z):
    """Make NS exact: solve the three corner cross-product equations for the three alB's."""
    from scipy.optimize import fsolve
    idx = [3, 8, 13]
    def F(y):
        w = z.copy(); w[idx] = y
        return ns_residual(unpack_global(w))[0::2]
    y = fsolve(F, z[idx], xtol=1e-14)
    w = z.copy(); w[idx] = y
    return w


def obj(z):
    P = unpack_global(z)
    ns = ns_residual(P)
    sv = sign_violation(P, tau=np.linspace(0, 1, 161)[1:-1])
    bm, _ = box_margin(P, tau=np.linspace(0, 1, 161)[1:-1])
    return 50 * (ns ** 2).sum() + 50 * min(0, sv) ** 2 - min(bm, 0.05)


def report(z, label):
    P = unpack_global(z)
    print(f"\n{label}")
    print("  NS residual (max |cross|, max neg dot)", np.abs(ns_residual(P)).max())
    print("  sign check on 4000-pt grid (>=0 ok)", sign_violation(P, tau=np.linspace(0, 1, 4001)[1:-1]))
    bm, arg = box_margin(P, tau=np.linspace(0, 1, 4001)[1:-1])
    print("  box margin on 4000-pt grid (>=0 ok)", bm, "worst (a,b,facet,rho,sA):", arg)
    for k in range(3):
        print("  facet", k + 1, "(lamA, alA, beA, lamB, alB, beB, tb) =", np.round(P[k], 6))
    return P

if __name__ == '__main__':
    print(f"eps={EPS}  kappa={KAP:.6f}")
    # (1) linear case: corner solutions x+ and x-
    disc = (KAP + 1) ** 2 - 4
    for x in [((KAP + 1) + np.sqrt(disc)) / 2, ((KAP + 1) - np.sqrt(disc)) / 2]:
        P = linear_params([x, x, x])
        print(f"LINEAR x={x:.6f}: NS residual {np.abs(ns_residual(P)).max():.2e}, sign {sign_violation(P):.3e}, "
              f"box margin {box_margin(P)[0]:.4f}  (x^2/kappa={x*x/KAP:.4f})")

    rng = np.random.default_rng(1)
    best = None
    ntr = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    for trial in range(ntr):
        z0 = rng.normal(0, 0.7, 15)
        r = minimize(obj, z0, method='Nelder-Mead', options=dict(maxiter=6000, xatol=1e-9, fatol=1e-12))
        if best is None or r.fun < best.fun: best = r
    if best is not None:
        zb = polish(best.x)
        report(zb, "PIECEWISE LINEAR (one break per facet, strictly between its crossings), NS polished exactly:")
        np.save(__file__.replace('.py', '_best.npy'), zb)
