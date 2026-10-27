"""Referee C12: independent checks for C1.1 (dichotomy), C1.3 step 1 (Farkas decomposition)
and C1.9 (finite G-obstruction alternative), on random cell models.  NUMERICS only.

Run: python3 -I ref_c1.py
"""
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(11)

def inst():
    ni, nj, nk = rng.integers(2, 6), rng.integers(1, 4), rng.integers(1, 4)
    a, b = rng.integers(1, 4), rng.integers(1, 4)
    w = rng.uniform(0.2, 2, ni + nj + nk)
    I = np.arange(ni); J = np.arange(ni, ni + nj); K = np.arange(ni + nj, ni + nj + nk)
    rho = np.zeros((a, len(w))); sig = np.zeros((b, len(w)))
    rho[:, np.r_[I, J]] = rng.uniform(0.1, 3, (a, ni + nj))
    sig[:, np.r_[I, K]] = rng.uniform(0.1, 3, (b, ni + nk))
    if rng.random() < 0.3:     # force an intersection
        lam = rng.uniform(0, 1, a)
        sig[0, I] = lam @ rho[:, I]
    return w, I, J, K, rho, sig

def G_constraints(w, I, rho, sig):
    a, b = len(rho), len(sig)
    Aeq = np.hstack([rho[:, I].T, -sig[:, I].T])            # sum lam rho|Qi = sum mu sig|Qi
    return Aeq, a, b

def nu_of(w, I, J, K, rho, sig, lam, mu):
    nu = np.zeros(len(w))
    nu[np.r_[I, J]] = (lam @ rho)[np.r_[I, J]]
    nu[K] = (mu @ sig)[K]
    return nu * w                                             # cell masses of nu

def G1_min(w, I, J, K, rho, sig, delta):
    """min nu(delta) over G_1 = {nu in G, nu(M) = 1}; None if G = {0}."""
    Aeq, a, b = G_constraints(w, I, rho, sig)
    # nu(v) is linear in (lam, mu): coefficient vectors
    cR = np.array([(rho[l] * w)[np.r_[I, J]] @ delta[np.r_[I, J]] for l in range(a)])
    cS = np.array([(sig[m] * w)[K] @ delta[K] for m in range(b)])
    mR = np.array([(rho[l] * w)[np.r_[I, J]].sum() for l in range(a)])
    mS = np.array([(sig[m] * w)[K].sum() for m in range(b)])
    A = np.vstack([Aeq, np.r_[mR, mS]]); beq = np.r_[np.zeros(len(I)), 1.0]
    r = linprog(np.r_[cR, cS], A_eq=A, b_eq=beq, bounds=[(0, None)] * (a + b), method="highs")
    return None if r.status != 0 else r.fun

def separating(w, I, rho, sig):
    n = len(I)
    A, bb = [], []
    for r_ in rho:
        A.append(np.r_[-(r_[I] * w[I]), 1.0]); bb.append(0)
    for s_ in sig:
        A.append(np.r_[(s_[I] * w[I]), 1.0]); bb.append(0)
    r = linprog(np.r_[np.zeros(n), -1.0], A_ub=np.array(A), b_ub=bb,
                bounds=[(-1, 1)] * n + [(None, 1)], method="highs")
    return r.x[-1]

def farkas_eta(w, I, J, K, rho, sig, delta):
    """max eta s.t. rho_l(delta 1_Qj + t) >= eta, sig_m(delta 1_{Qi u Qk} - t) >= eta, |t| <= 1e4."""
    n = len(I)
    A, bb = [], []
    for r_ in rho:
        A.append(np.r_[-(r_[I] * w[I]), 1.0]); bb.append((r_[J] * w[J]) @ delta[J])
    for s_ in sig:
        A.append(np.r_[(s_[I] * w[I]), 1.0]); bb.append((s_[np.r_[I, K]] * w[np.r_[I, K]]) @ delta[np.r_[I, K]])
    r = linprog(np.r_[np.zeros(n), -1.0], A_ub=np.array(A), b_ub=bb,
                bounds=[(-1e4, 1e4)] * n + [(None, 1)], method="highs")
    return r.x[-1] if r.status == 0 else -np.inf

dich = {'G>0 only': 0, 'sep only': 0, 'both': 0, 'neither': 0}
fk = {'agree': 0, 'disagree': 0, 'skipped(boundary)': 0}
c19 = {'common nu': 0, 'obstruction': 0, 'both': 0, 'neither': 0}
for trial in range(400):
    w, I, J, K, rho, sig = inst()
    g = G1_min(w, I, J, K, rho, sig, np.zeros(len(w)))
    s = separating(w, I, rho, sig)
    key = ('G>0 only' if s <= 1e-9 else 'both') if g is not None else ('sep only' if s > 1e-9 else 'neither')
    dich[key] += 1
    if g is None:
        continue
    for _ in range(5):
        delta = rng.choice([-1.0, 0.0, 1.0], len(w)) * rng.uniform(0, 1, len(w))
        th = G1_min(w, I, J, K, rho, sig, delta)
        eta = farkas_eta(w, I, J, K, rho, sig, delta)
        if abs(th) < 1e-7:
            fk['skipped(boundary)'] += 1
        elif (th > 0) == (eta > 1e-9):
            fk['agree'] += 1
        else:
            fk['disagree'] += 1
    # C1.9: finite family of deltas
    D = [rng.choice([-1.0, 0.0, 1.0], len(w)) * rng.uniform(0, 1, len(w)) for _ in range(rng.integers(2, 5))]
    Aeq, a, b = G_constraints(w, I, rho, sig)
    mR = np.array([(rho[l] * w)[np.r_[I, J]].sum() for l in range(a)])
    mS = np.array([(sig[m] * w)[K].sum() for m in range(b)])
    def coef(delta):
        return np.r_[[(rho[l] * w)[np.r_[I, J]] @ delta[np.r_[I, J]] for l in range(a)],
                     [(sig[m] * w)[K] @ delta[K] for m in range(b)]]
    C = np.array([coef(d) for d in D])
    # common nu in G_1 with nu(delta_s) >= 0 for all s
    r1 = linprog(np.zeros(a + b), A_ub=-C, b_ub=np.zeros(len(D)),
                 A_eq=np.vstack([Aeq, np.r_[mR, mS]]), b_eq=np.r_[np.zeros(len(I)), 1.0],
                 bounds=[(0, None)] * (a + b), method="highs")
    common = r1.status == 0
    # obstruction: c in simplex with max_{G_1} sum c_s nu(delta_s) < 0.  LP dual form:
    # min_c max_nu = value; compute via: min z s.t. for all nu in G_1 ... use vertex enumeration-free
    # formulation: max_{G_1} (c^T C)x is an LP; minimise over c by LP duality:
    # max {(C^T c).x : Aeq x = 0, m.x = 1, x >= 0} = min {y : Aeq^T u + m y >= C^T c}
    nI = len(I); nD = len(D)
    # variables: c (nD), u (nI), y (1); minimise y
    A_ub = np.hstack([C.T, -Aeq.T, -np.r_[mR, mS][:, None]])
    r2 = linprog(np.r_[np.zeros(nD + nI), 1.0], A_ub=A_ub, b_ub=np.zeros(a + b),
                 A_eq=np.r_[np.ones(nD), np.zeros(nI + 1)][None, :], b_eq=[1.0],
                 bounds=[(0, None)] * nD + [(None, None)] * (nI + 1), method="highs")
    obstr = r2.status == 0 and r2.fun < -1e-9
    c19[('both' if obstr else 'common nu') if common else ('obstruction' if obstr else 'neither')] += 1
print("C1.1 dichotomy (G != 0  XOR  separating h):", dich)
print("C1.3 step 1 (theta > 0  <=>  Farkas decomposition with eta > 0):", fk)
print("C1.9 (common endorsing nu in G_1  XOR  finite obstruction):", c19)
