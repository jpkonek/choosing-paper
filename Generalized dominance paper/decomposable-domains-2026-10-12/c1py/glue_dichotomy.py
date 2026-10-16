#!/usr/bin/env python3
"""
C1 round 15: glued credal worlds.  NUMERICS for Theorems C1.1-C1.4 of C1_notes.md.

Cell model of world i's mixed region M = Q_i u Q_j u Q_k:
  - finitely many cells per class, each of measure w_c;
  - densities constant on cells (so Lyapunov is exact: a fraction f of a cell
    realises f * (integral over the cell) for every density simultaneously);
  - Gamma_ij = conv{rho_1..rho_a}, densities > 0 on R_ij = Q_i u Q_j;
  - Gamma_ik = conv{sig_1..sig_b}, densities > 0 on R_ik = Q_i u Q_k.

Part A  (Thm C1.1, dichotomy): K1 := cone(Gamma_ij|Q_i), K2 := cone(Gamma_ik|Q_i).
        If K1 /\ K2 = {0}: build the explicit strict cycle Y < Y' <= Z <= Y.
        Else: produce nu in G (glued set) and check nu > 0 on every cell.
Part B  (Lemma C1.3, chain): random C, X with min_{nu in G} nu(delta) > 0;
        build the explicit round chain (exact rational arithmetic) and verify
        every step is inside one edge region, is weakly accepted by every
        generator of that region, respects the available masses, and ends at X.
Part C  (Prop C1.4, refinement): K1 != K2, K1 /\ K2 != {0}: an R_ij-internal
        comparison reached by a chain (so in the closure) that some rho_l strictly
        reverses: gluing refines the edge order.
All verdicts that matter are checked in exact Fractions; LPs (floats) only propose.
"""
import random
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog

RNG = random.Random(20261015)


def rfrac(lo=1, hi=9):
    return F(RNG.randint(lo, hi), RNG.randint(1, 4))


def make_instance(ni, nj, nk, a, b, mode="random"):
    """mode: 'random' | 'compatible' (K1 = K2) | 'disjoint' (try K1/\\K2={0})."""
    w = {('i', c): rfrac() for c in range(ni)}
    w.update({('j', c): rfrac() for c in range(nj)})
    w.update({('k', c): rfrac() for c in range(nk)})
    rho = []
    for _ in range(a):
        d = {}
        for c in range(ni):
            d[('i', c)] = rfrac()
        for c in range(nj):
            d[('j', c)] = rfrac()
        rho.append(d)
    sig = []
    for m in range(b):
        d = {}
        if mode == "compatible":
            # Q_i restriction = a positive combination of the rho restrictions
            lam = [rfrac(0, 3) for _ in range(a)]
            if sum(lam) == 0:
                lam[0] = F(1)
            for c in range(ni):
                d[('i', c)] = sum(lam[l] * rho[l][('i', c)] for l in range(a))
        elif mode == "disjoint":
            # Q_i restrictions concentrated on the 'other half' of the cells
            for c in range(ni):
                d[('i', c)] = rfrac(1, 2) if c < ni // 2 else rfrac(20, 40)
        else:
            for c in range(ni):
                d[('i', c)] = rfrac()
        for c in range(nk):
            d[('k', c)] = rfrac()
        sig.append(d)
    if mode == "compatible":
        # make K2 contain K1 too: add the rho_l|Q_i themselves as sigma restrictions
        for l in range(a):
            d = {('i', c): rho[l][('i', c)] for c in range(ni)}
            for c in range(nk):
                d[('k', c)] = rfrac()
            sig.append(d)
    if mode == "disjoint":
        for d in rho:
            for c in range(ni):
                d[('i', c)] = rfrac(20, 40) if c < ni // 2 else rfrac(1, 2)
    cells = {'i': [('i', c) for c in range(ni)], 'j': [('j', c) for c in range(nj)],
             'k': [('k', c) for c in range(nk)]}
    return dict(w=w, rho=rho, sig=sig, cells=cells)


def integ(dens, fn, w):
    """integral of a cell-function fn (value per unit mass = fraction) against dens."""
    return sum(dens[c] * fn.get(c, 0) * w[c] for c in fn if c in dens)


# ---------------------------------------------------------------- Part A
def glued_member(inst):
    """LP: lambda, mu >= 0, sum = 1, sum lam rho|Qi = sum mu sig|Qi.  Returns (lam, mu) or None."""
    rho, sig, Qi = inst['rho'], inst['sig'], inst['cells']['i']
    a, b = len(rho), len(sig)
    A_eq = []
    b_eq = []
    for c in Qi:
        A_eq.append([float(r[c]) for r in rho] + [-float(s[c]) for s in sig])
        b_eq.append(0.0)
    A_eq.append([1.0] * (a + b))
    b_eq.append(1.0)
    res = linprog(np.zeros(a + b), A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=[(0, None)] * (a + b), method="highs")
    if res.status != 0:
        return None
    return res.x[:a], res.x[a:]


def separate(inst):
    """LP: max s, h in [-1,1]^Qi, rho_l(h) >= s, sig_m(h) <= -s."""
    rho, sig, w, Qi = inst['rho'], inst['sig'], inst['w'], inst['cells']['i']
    n = len(Qi)
    # variables: h_1..h_n, s ; minimise -s
    c = np.zeros(n + 1)
    c[-1] = -1
    A, bb = [], []
    for r in rho:
        A.append([-float(r[q] * w[q]) for q in Qi] + [1.0])
        bb.append(0.0)
    for s_ in sig:
        A.append([float(s_[q] * w[q]) for q in Qi] + [1.0])
        bb.append(0.0)
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(bb),
                  bounds=[(-1, 1)] * n + [(None, 1)], method="highs")
    return res.x[:n], res.x[-1]


def part_A(trials=300):
    out = []
    n_cyc = n_pos = n_fail = 0
    for t in range(trials):
        mode = ["random", "disjoint", "compatible"][t % 3]
        ni = RNG.randint(2, 5)
        inst = make_instance(ni, RNG.randint(1, 3), RNG.randint(1, 3),
                             RNG.randint(1, 3), RNG.randint(1, 3), mode)
        w, rho, sig, Qi = inst['w'], inst['rho'], inst['sig'], inst['cells']['i']
        gm = glued_member(inst)
        if gm is None:
            h, s = separate(inst)
            if s <= 1e-9:
                n_fail += 1
                continue
            # exact: rationalise h, halve it (leave room), check strict separation exactly
            hq = {q: F(h[x]).limit_denominator(10**6) / 2 for x, q in enumerate(Qi)}
            A = {q: max(hq[q], F(0)) for q in Qi}            # fractions of cells (Z's error set)
            B = {q: max(-hq[q], F(0)) for q in Qi}           # Y's error set
            gapij = min(integ(r, A, w) - integ(r, B, w) for r in rho)
            gapik = min(integ(s_, B, w) - integ(s_, A, w) for s_ in sig)
            if gapij <= 0 or gapik <= 0:
                n_fail += 1
                continue
            # e: small piece of a cell, outside A u B (room: 1 - |h| >= 1/2)
            q0 = Qi[0]
            mx = max(r[q0] * w[q0] for r in rho)
            ef = min(F(1, 4), gapij / (2 * mx))
            e = {q0: ef}
            Yp = {q: B[q] + e.get(q, 0) for q in Qi}      # E(Y') = B u e
            ok = True
            ok &= ef > 0                                   # Y < Y' by strict (G)
            ok &= all(integ(r, Yp, w) <= integ(r, A, w) for r in rho)    # Y' <=_ij Z
            ok &= all(integ(s_, A, w) <= integ(s_, B, w) for s_ in sig)  # Z <=_ik Y
            ok &= all(B[q] + A[q] + e.get(q, 0) <= 1 for q in Qi)        # disjointness room
            if ok:
                n_cyc += 1
            else:
                n_fail += 1
        else:
            lam, mu = gm
            # nu = sum lam rho on R_ij, sum mu sig on R_ik ; check positivity on every cell
            pos = True
            for q in inst['cells']['i'] + inst['cells']['j']:
                pos &= sum(lam[l] * float(rho[l][q]) for l in range(len(rho))) > 0
            for q in inst['cells']['k']:
                pos &= sum(mu[m] * float(sig[m][q]) for m in range(len(sig))) > 0
            if pos:
                n_pos += 1
            else:
                n_fail += 1
    out.append(f"Part A: {trials} instances: strict cycle built and verified exactly: {n_cyc}; "
               f"glued strictly positive nu found: {n_pos}; neither: {n_fail}")
    return out


# ---------------------------------------------------------------- Part B
def random_states(inst, roomsign=None):
    """Per cell: masses (fractions of the cell) d+ (C right, X wrong), d- (C wrong, X right),
    s+ (outside D, both right), s- (outside D, both wrong).  Sum = 1."""
    st = {}
    for cls in 'ijk':
        for q in inst['cells'][cls]:
            x = [F(RNG.randint(0, 6)) for _ in range(4)]
            x[0] += RNG.randint(0, 6)
            if cls == 'i':
                if roomsign == '+':
                    x[3] = F(0); x[2] += 1
                elif roomsign == '-':
                    x[2] = F(0); x[3] += 1
                else:
                    x[2] += 1
            tot = sum(x)
            st[q] = [v / tot for v in x]
    return st


def delta_fn(st):
    return {q: v[0] - v[1] for q, v in st.items()}


def theta_G(inst, st):
    """min over normalised G of nu(delta) (LP)."""
    rho, sig, w, cells = inst['rho'], inst['sig'], inst['w'], inst['cells']
    dl = delta_fn(st)
    a, b = len(rho), len(sig)
    cost = []
    for r in rho:
        cost.append(float(sum(r[q] * dl[q] * w[q] for q in cells['j'] + cells['i'])))
    for s_ in sig:
        cost.append(float(sum(s_[q] * dl[q] * w[q] for q in cells['k'])))
    A_eq, b_eq = [], []
    for c in cells['i']:
        A_eq.append([float(r[c]) for r in rho] + [-float(s[c]) for s in sig])
        b_eq.append(0.0)
    A_eq.append([1.0] * (a + b))
    b_eq.append(1.0)
    res = linprog(np.array(cost), A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=[(0, None)] * (a + b), method="highs")
    return None if res.status != 0 else res.fun


def decompose(inst, st, first, second, Bnd=50.0):
    """LP: max eta, t on Q_i cells (per-unit-mass values), phi = delta on Q_first + t on Q_i
    accepted with margin eta by generators of the first region, psi = delta on Q_second +
    (delta - t) on Q_i by generators of the second region."""
    gens = {'j': inst['rho'], 'k': inst['sig']}
    w, cells = inst['w'], inst['cells']
    dl = delta_fn(st)
    Qi = cells['i']
    n = len(Qi)
    A, bb = [], []
    for g in gens[first]:
        # -(sum_{Qfirst} g dl w + sum_{Qi} g t w) + eta <= 0
        A.append([-float(g[q] * w[q]) for q in Qi] + [1.0])
        bb.append(float(sum(g[q] * dl[q] * w[q] for q in cells[first])))
    for g in gens[second]:
        # -(sum_{Qsecond} g dl w + sum_{Qi} g (dl - t) w) + eta <= 0
        A.append([float(g[q] * w[q]) for q in Qi] + [1.0])
        bb.append(float(sum(g[q] * dl[q] * w[q] for q in cells[second]) +
                        sum(g[q] * dl[q] * w[q] for q in Qi)))
    c = np.zeros(n + 1)
    c[-1] = -1
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(bb),
                  bounds=[(-Bnd, Bnd)] * n + [(None, 10)], method="highs")
    if res.status != 0:
        return None
    t = {q: F(res.x[x]).limit_denominator(10**6) for x, q in enumerate(Qi)}
    # exact margin
    m1 = min(sum(g[q] * dl[q] * w[q] for q in cells[first]) + sum(g[q] * t[q] * w[q] for q in Qi)
             for g in gens[first])
    m2 = min(sum(g[q] * dl[q] * w[q] for q in cells[second]) +
             sum(g[q] * (dl[q] - t[q]) * w[q] for q in Qi) for g in gens[second])
    return t, min(m1, m2)


def run_chain(inst, st, verbose=False):
    """Build and verify the chain of Lemma C1.3.  Returns (ok, nsteps, info)."""
    w, cells = inst['w'], inst['cells']
    gens = {'j': inst['rho'], 'k': inst['sig']}
    Qi = cells['i']
    # which region gets u (an up-piece of D): second region must contain it
    upk = [q for q in cells['k'] + Qi if st[q][0] > 0]
    upj = [q for q in cells['j'] if st[q][0] > 0]
    if upk:
        first, second, uq = 'j', 'k', upk[0]
    elif upj:
        first, second, uq = 'k', 'j', upj[0]
    else:
        return False, 0, "no up-piece"
    dec = decompose(inst, st, first, second)
    if dec is None or dec[1] <= 0:
        return False, 0, "no strict decomposition"
    t, eta = dec
    dl = delta_fn(st)
    # u: fraction of cell uq inside its d+ part, second-generators(u) <= eta/4
    gmax = max(g[uq] * w[uq] for g in gens[second])
    uf = min(st[uq][0] / 2, eta / (4 * gmax))
    # psi' = psi - 1_u keeps margin >= 3 eta / 4 ; delta' = delta - 1_u
    # room sign
    roomplus = all(st[q][2] > 0 for q in Qi)
    roomminus = all(st[q][3] > 0 for q in Qi)
    if not (roomplus or roomminus):
        return False, 0, "no room in some Q_i cell"
    mode = '+' if roomplus else '-'
    roomcap = {q: (st[q][2] if mode == '+' else st[q][3]) for q in Qi}
    # delta' on Q_i (u removed if uq in Q_i)
    dlp = dict(dl)
    dlp[uq] = dl[uq] - uf
    # per-round transfer tau_q = (t_q - delta'_q)/m  (per unit mass of cell q)
    # remark: if uq in Q_i, psi' = delta'_Qi - t, phi uses t: tau uses delta' on Q_i.
    tau1 = {q: t[q] - dlp[q] for q in Qi}
    # choose m: |tau_q| <= roomcap_q / 2 and second-gens(y) <= second-gens(u)
    m = 1
    while True:
        ok_room = all(abs(tau1[q]) / m <= roomcap[q] / 2 for q in Qi)
        if mode == '+':
            yv = {q: max(-tau1[q], F(0)) / m for q in Qi}
        else:
            yv = {q: max(tau1[q], F(0)) / m for q in Qi}
        ok_def = all(sum(g[q] * yv[q] * w[q] for q in Qi) <= g[uq] * uf * w[uq] for g in gens[second])
        if ok_room and ok_def:
            break
        m *= 2
        if m > 2**20:
            return False, 0, "m too large"
    # equal pieces of D (cell model: equal fractions), u kept aside
    dplus = {q: st[q][0] for q in st}
    dplus_main = dict(dplus)
    dplus_main[uq] -= uf
    dminus = {q: st[q][1] for q in st}
    # state counters
    err = {q: st[q][1] + st[q][3] for q in st}      # C's error mass fraction per cell
    target = {q: st[q][0] + st[q][3] for q in st}   # X's
    raised = {q: F(0) for q in Qi}                  # transfer mass currently toggled
    steps = []

    def step(region, changes):
        # changes: dict cell -> change of error fraction ; check region & acceptance & bounds
        allowed = set(cells[region] + Qi)
        for q, d in changes.items():
            if q not in allowed:
                return False
        for g in gens[region]:
            if sum(g[q] * d * w[q] for q, d in changes.items()) < 0:
                return False
        for q, d in changes.items():
            err[q] += d
            if err[q] < 0 or err[q] > 1:
                return False
        steps.append(region)
        return True

    if mode == '+':
        x = {q: max(tau1[q], F(0)) / m for q in Qi}
        y = {q: max(-tau1[q], F(0)) / m for q in Qi}
        # S_0: raise y
        if not step(second, {q: y[q] for q in Qi}):
            return False, 0, "S0"
        for r in range(1, m + 1):
            ch = {}
            for q in cells[first] + Qi:
                ch[q] = ch.get(q, 0) + (dplus_main[q] - dminus[q]) / m
            for q in Qi:
                ch[q] += x[q] - y[q]
            if not step(first, ch):
                return False, 0, f"F{r}"
            ch = {}
            for q in cells[second]:
                ch[q] = (dplus_main[q] - dminus[q]) / m
            for q in Qi:
                ch[q] = ch.get(q, 0) - x[q] + (y[q] if r < m else 0)
            if r == m:
                ch[uq] = ch.get(uq, 0) + uf
            if not step(second, ch):
                return False, 0, f"S{r}"
    else:
        xp = {q: max(-tau1[q], F(0)) / m for q in Qi}   # lowered at F, raised at S
        yp = {q: max(tau1[q], F(0)) / m for q in Qi}    # lowered at S_{r-1}, raised at F_r
        ch = {q: -yp[q] for q in Qi}
        ch[uq] = ch.get(uq, 0) + uf
        if not step(second, ch):
            return False, 0, "S0-"
        for r in range(1, m + 1):
            ch = {}
            for q in cells[first] + Qi:
                ch[q] = ch.get(q, 0) + (dplus_main[q] - dminus[q]) / m
            for q in Qi:
                ch[q] += -xp[q] + yp[q]
            if not step(first, ch):
                return False, 0, f"F{r}-"
            ch = {}
            for q in cells[second]:
                ch[q] = (dplus_main[q] - dminus[q]) / m
            for q in Qi:
                ch[q] = ch.get(q, 0) + xp[q] - (yp[q] if r < m else 0)
            if not step(second, ch):
                return False, 0, f"S{r}-"
    if any(err[q] != target[q] for q in st):
        return False, len(steps), "endpoint mismatch " + str(
            {q: float(err[q] - target[q]) for q in st if err[q] != target[q]})
    return True, len(steps), f"mode {mode}, first {first}, m={m}, eta={float(eta):.3g}"


def part_B(trials=150):
    out = []
    n_ok = n_neg = n_skip = n_bad = 0
    nsteps = []
    bad = []
    for tr in range(trials):
        mode = ["random", "compatible"][tr % 2]
        inst = make_instance(RNG.randint(2, 4), RNG.randint(1, 3), RNG.randint(1, 3),
                             RNG.randint(1, 3), RNG.randint(1, 3), mode)
        if glued_member(inst) is None:
            n_skip += 1
            continue
        rs = [None, '+', '-'][tr % 3]
        st = random_states(inst, rs)
        th = theta_G(inst, st)
        if th is None:
            n_skip += 1
            continue
        if th <= 1e-7:
            n_neg += 1
            continue
        ok, ns, info = run_chain(inst, st)
        if ok:
            n_ok += 1
            nsteps.append(ns)
        else:
            n_bad += 1
            bad.append(info)
    out.append(f"Part B: {trials} instances; G={{0}} or LP issue (skipped): {n_skip}; "
               f"not G-strict (no chain claimed): {n_neg}; G-strict: {n_ok + n_bad}, "
               f"chain built and verified exactly: {n_ok}, failed: {n_bad} {bad[:5]}")
    if nsteps:
        out.append(f"        chain lengths: min {min(nsteps)}, median {sorted(nsteps)[len(nsteps)//2]}, max {max(nsteps)}")
    return out


# ---------------------------------------------------------------- Part C
def part_C(trials=60):
    out = []
    found = 0
    tried = 0
    example = None
    for tr in range(trials):
        inst = make_instance(3, 2, 2, 2, 2, "random")
        if glued_member(inst) is None:
            continue
        tried += 1
        rho, sig, w, cells = inst['rho'], inst['sig'], inst['w'], inst['cells']
        Qi, Qj = cells['i'], cells['j']
        # find delta on R_ij (fractions in [-1/2,1/2]) and t on Q_i: max s with
        # rho_l(delta_Qj + t) >= s, sig_m(delta_Qi - t) >= s, rho_l0(delta) <= -s
        for l0 in range(len(rho)):
            cellsR = Qj + Qi
            nR, nI = len(cellsR), len(Qi)
            # vars: delta (nR), t (nI), s
            A, bb = [], []
            for r in rho:
                row = [0.0] * (nR + nI + 1)
                for x, q in enumerate(cellsR):
                    if q[0] == 'j':
                        row[x] = -float(r[q] * w[q])
                for x, q in enumerate(Qi):
                    row[nR + x] = -float(r[q] * w[q])
                row[-1] = 1.0
                A.append(row); bb.append(0.0)
            for s_ in sig:
                row = [0.0] * (nR + nI + 1)
                for x, q in enumerate(cellsR):
                    if q[0] == 'i':
                        row[x] = -float(s_[q] * w[q])
                for x, q in enumerate(Qi):
                    row[nR + x] = float(s_[q] * w[q])
                row[-1] = 1.0
                A.append(row); bb.append(0.0)
            row = [0.0] * (nR + nI + 1)
            for x, q in enumerate(cellsR):
                row[x] = float(rho[l0][q] * w[q])
            row[-1] = 1.0
            A.append(row); bb.append(0.0)
            c = np.zeros(nR + nI + 1); c[-1] = -1
            res = linprog(c, A_ub=np.array(A), b_ub=np.array(bb),
                          bounds=[(-0.5, 0.5)] * nR + [(-20, 20)] * nI + [(None, 1)], method="highs")
            if res.status != 0 or res.x[-1] <= 1e-6:
                continue
            dvals = {q: F(res.x[x]).limit_denominator(10**5) for x, q in enumerate(cellsR)}
            # states: d+ = max(delta,0), d- = max(-delta,0), room s+ = rest (C right)
            st = {}
            for q in cellsR:
                dp, dm = max(dvals[q], F(0)), max(-dvals[q], F(0))
                st[q] = [dp, dm, 1 - dp - dm, F(0)]
            for q in cells['k']:
                st[q] = [F(0), F(0), F(1), F(0)]
            dl = delta_fn(st)
            rev = integ(rho[l0], dl, w)   # rho_l0(E_X) - rho_l0(E_C)
            if rev >= 0:
                continue
            ok, ns, info = run_chain(inst, st)
            if ok:
                found += 1
                if example is None:
                    example = (float(rev), ns, info,
                               [float(integ(r, dl, w)) for r in rho])
                break
    out.append(f"Part C: {tried} intersecting instances; found R_ij-internal comparison C <= X "
               f"in the glued closure (explicit chain verified) that some rho_l strictly reverses: {found}")
    if example:
        out.append(f"        example: rho_l(E_X)-rho_l(E_C) over generators = "
                   f"{[round(v, 4) for v in example[3]]}; chain: {example[1]} steps, {example[2]}")
    return out


if __name__ == "__main__":
    lines = []
    lines += part_A()
    lines += part_B()
    lines += part_C()
    print("\n".join(lines))
