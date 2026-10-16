"""C2: discrete concurrent-chart problem DCF(G,F) for CF(T1).

Unknowns: for every test gamble g in F a cell z[q,g] in {+,0,-} at every grid prior q in G.
Constraints (all NECESSARY for a solution of CF(T1) whose chart data hold exactly at the gambles of F):
 (CH) per g: the column z[.,g] is the cell pattern of max{0, c.q, c'.q} for some c, c' with
      sign c_i = sign g_i = -sign c'_i   (an LP in (c,c') once z is fixed; homogeneous, margin 1);
 (DC) per q: Acc(q) = {g : z=+} u {-g : z=-} is F-closed and coherent: no rejected h in +-F lies in
      posi(Acc(q)) + R^3_{>=0}, and no nonpositive gamble lies in posi(Acc(q)).  These are q-independent
      Horn clauses  (S => h)  and  (not all of S), generated lazily from LP duals;
 (TP) z[u,.] is the pattern of T1.
(DC) is exactly "there is a credal set K_q with P_{K_q}>0 on Acc(q) and <=0 on the rejected gambles".
"""
import numpy as np
from scipy.optimize import linprog, milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix, csr_matrix, vstack

E = np.eye(3)


def setup(eps):
    kap = (1 + 2 * eps) / (1 - eps)
    c0 = (1 - eps) / 3
    v = np.array([c0 * np.ones(3) + eps * E[k] for k in range(3)])
    s = kap + 1
    xp = (s + np.sqrt(s * s - 4)) / 2
    return kap, v, xp


def PT(g, v):
    """lower prevision of T1 (vertices v)"""
    return np.min(v @ g)


def corner(k, j, v):
    r = np.cross(v[k], v[j])
    t = 3 - k - j
    return r if r @ v[t] > 0 else -r


def facet_h(k, tau, v):
    """h(tau) on facet F_k between its two corner rays (i<j order of remaining indices)."""
    i, j = [l for l in range(3) if l != k]
    r0, r1 = corner(k, i, v), corner(k, j, v)
    return (1 - tau) * r0 + tau * r1


def mixed(g):
    return g.max() > 0 and g.min() < 0


def unit(g):
    return g / np.linalg.norm(g)


# ---------------------------------------------------------------- closure / coherence of an accepted set
def closure_check(A, H, tol=1e-9):
    """A: (n,3) accepted signed gambles; H: (k,3) rejected signed gambles.
    Returns (ok, clause). clause = ('sureloss', idxA) or ('imply', idxA, idxH).
    LP: max t s.t. m.a >= t (a in A), m.h <= 0, m in simplex."""
    n = len(A)
    # sure loss first: max t, m.a >= t
    def lp(extra=None):
        # vars m1,m2,m3,t ; minimise -t
        Aub = [np.r_[-a, 1.0] for a in A]
        if extra is not None:
            Aub.append(np.r_[extra, 0.0])
        Aub = np.array(Aub) if Aub else np.zeros((0, 4))
        bub = np.zeros(len(Aub))
        res = linprog([0, 0, 0, -1], A_ub=Aub, b_ub=bub, A_eq=[[1, 1, 1, 0]], b_eq=[1],
                      bounds=[(0, None)] * 3 + [(None, 1.0)], method='highs')
        return res
    if n == 0:
        return True, None
    res = lp()
    if -res.fun <= tol:
        lam = -res.ineqlin.marginals[:n]
        S = np.where(lam > 1e-9)[0]
        return False, ('sureloss', S)
    for hi, h in enumerate(H):
        res = lp(h)
        if res.status != 0 or -res.fun <= tol:
            if res.status != 0:   # infeasible: m.h<=0 impossible on simplex -> h>0 (not mixed): skip
                continue
            lam = -res.ineqlin.marginals[:n]
            S = np.where(lam > 1e-9)[0]
            return False, ('imply', S, hi)
    return True, None


# ---------------------------------------------------------------- MILP
class DCF:
    def __init__(self, G, F, fixed, M=1e3):
        """G: (nq,3) priors, F: (ng,3) gambles (mixed, generic), fixed: dict q-index -> array of cells
        (+1,0,-1) per g (e.g. target prior)."""
        self.G, self.F, self.fixed, self.M = np.asarray(G), np.asarray(F), fixed, M
        self.nq, self.ng = len(G), len(F)
        self.clauses = []   # list of (pos_literals, neg_literals) over signed-acceptance vars, q-independent

    # variable layout: per g: c(3), c'(3) ; per (q,g): zp, z0, zm
    def vidx(self):
        ng, nq = self.ng, self.nq
        self.nc = 6 * ng
        self.nz = 3 * ng * nq
        return self.nc + self.nz

    def z(self, q, g, k):  # k=0 '+',1 '0',2 '-'
        return self.nc + 3 * (q * self.ng + g) + k

    def acc_var(self, q, sg):
        """signed gamble index sg in [0,2ng): sg<ng -> +g, else -g ; returns var index of 'accepted'"""
        if sg < self.ng:
            return self.z(q, sg, 0)
        return self.z(q, sg - self.ng, 2)

    def build(self):
        nv = self.vidx()
        G, F, M = self.G, self.F, self.M
        rows, lo, hi = [], [], []

        def add(coefs, l, h):
            rows.append(coefs); lo.append(l); hi.append(h)
        for gi, g in enumerate(F):
            s = np.sign(g)
            # sign constraints: s_i c_i >= 1 ; -s_i c'_i >= 1
            for i in range(3):
                add({6 * gi + i: s[i]}, 1, np.inf)
                add({6 * gi + 3 + i: -s[i]}, 1, np.inf)
            for qi, q in enumerate(G):
                zp, z0, zm = self.z(qi, gi, 0), self.z(qi, gi, 1), self.z(qi, gi, 2)
                add({zp: 1, z0: 1, zm: 1}, 1, 1)
                cq = {6 * gi + i: q[i] for i in range(3)}
                cpq = {6 * gi + 3 + i: q[i] for i in range(3)}
                # zp => c.q >= 1 and c.q - c'.q >= 1
                d = dict(cq); d[zp] = -M; add(d, 1 - M, np.inf)
                d = dict(cq); [d.__setitem__(k, d.get(k, 0) - v) for k, v in cpq.items()]; d[zp] = -M
                add(d, 1 - M, np.inf)
                # zm => c'.q >= 1 and c'.q - c.q >= 1
                d = dict(cpq); d[zm] = -M; add(d, 1 - M, np.inf)
                d = dict(cpq); [d.__setitem__(k, d.get(k, 0) - v) for k, v in cq.items()]; d[zm] = -M
                add(d, 1 - M, np.inf)
                # z0 => c.q <= 0, c'.q <= 0
                d = dict(cq); d[z0] = M; add(d, -np.inf, M)
                d = dict(cpq); d[z0] = M; add(d, -np.inf, M)
        self.base_rows = (rows, lo, hi)
        lb = np.r_[-M * np.ones(self.nc), np.zeros(self.nz)]
        ub = np.r_[M * np.ones(self.nc), np.ones(self.nz)]
        for qi, cells in self.fixed.items():
            for gi, cell in enumerate(cells):
                k = {1: 0, 0: 1, -1: 2}[int(cell)]
                lb[self.z(qi, gi, k)] = 1
        self.lb, self.ub = lb, ub

    def clause_rows(self):
        rows, lo, hi = [], [], []
        for (S, H) in self.clauses:     # not(all S accepted and H not accepted): sum(1-acc_S)+acc_H >= 1
            for qi in range(self.nq):
                d = {}
                for sg in S:
                    d[self.acc_var(qi, sg)] = d.get(self.acc_var(qi, sg), 0) - 1
                for sg in H:
                    d[self.acc_var(qi, sg)] = d.get(self.acc_var(qi, sg), 0) + 1
                rows.append(d); lo.append(1 - len(S)); hi.append(np.inf)
        return rows, lo, hi

    def solve(self, time_limit=600, verbose=False):
        nv = self.nc + self.nz
        r1, l1, h1 = self.base_rows
        r2, l2, h2 = self.clause_rows()
        R = r1 + r2
        A = lil_matrix((len(R), nv))
        for k, d in enumerate(R):
            for j, val in d.items():
                A[k, j] = val
        cons = LinearConstraint(csr_matrix(A), np.array(l1 + l2), np.array(h1 + h2))
        integ = np.r_[np.zeros(self.nc), np.ones(self.nz)]
        res = milp(np.zeros(nv), constraints=cons, integrality=integ, bounds=Bounds(self.lb, self.ub),
                   options={'time_limit': time_limit, 'disp': verbose})
        return res

    def cells(self, x):
        Z = np.zeros((self.nq, self.ng), int)
        for qi in range(self.nq):
            for gi in range(self.ng):
                k = np.argmax([x[self.z(qi, gi, j)] for j in range(3)])
                Z[qi, gi] = [1, 0, -1][k]
        return Z

    def signed(self):
        return np.vstack([self.F, -self.F])

    def check_closure(self, Z, maxadd=100000):
        SF = self.signed()
        added = 0
        for qi in range(self.nq):
            accs = [gi for gi in range(self.ng) if Z[qi, gi] == 1] + \
                   [self.ng + gi for gi in range(self.ng) if Z[qi, gi] == -1]
            rej = [sg for sg in range(2 * self.ng) if sg not in accs]
            while True:
                ok, cl = closure_check(SF[accs], SF[rej])
                if ok:
                    break
                if cl[0] == 'sureloss':
                    S = [accs[i] for i in cl[1]]
                    newc = (tuple(sorted(S)), ())
                    # remove one to continue scanning this q
                    if newc not in self.clauses:
                        self.clauses.append(newc); added += 1
                    break
                S = [accs[i] for i in cl[1]]
                h = rej[cl[2]]
                newc = (tuple(sorted(S)), (h,))
                if newc not in self.clauses:
                    self.clauses.append(newc); added += 1
                rej = [r for r in rej if r != h]
                if added >= maxadd:
                    return added
        return added

    def run(self, rounds=50, time_limit=600, log=print):
        self.build()
        for it in range(rounds):
            res = self.solve(time_limit)
            if res.x is None:
                log(f"round {it}: MILP status {res.status} ({res.message}); clauses {len(self.clauses)}")
                return None, res
            Z = self.cells(res.x)
            added = self.check_closure(Z)
            log(f"round {it}: feasible chart assignment; new closure clauses {added}; total {len(self.clauses)}")
            if added == 0:
                return Z, res
        return None, None
