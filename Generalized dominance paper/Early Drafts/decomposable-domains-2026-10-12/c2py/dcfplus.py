"""DCF+: the discrete concurrent-chart problem with the facet-pencil constraints of the PC data, in witness form.

Unknowns
  * per generic test gamble g in F: chart data (c, c') with strict signs; cell z[q,g] in {+,0,-} at each grid prior;
  * per grid prior q: a credal set K_q given as the convex hull of WITNESS points (one witness per rejection
    requirement), so that no restriction on the shape of K_q is imposed (exact for finite data);
  * per (q, facet gamble h_k(tau)) with chi = c_k(h).q > 0: a side bit s (K_q in {m.h>=0} or in {m.h<=0}) [Lemma C].
Constraints
  (CH)  z[.,g] is the cell pattern of max{0, c.q, c'.q} (margin 1, |c|,|c'| <= Mc);
  (ACC) every witness m of K_q satisfies m.a >= delta for each accepted signed generic gamble a;
  (REJ) for each rejected signed generic gamble h there is a witness with m.h <= 0;
  (R1)  for facet gambles with chi < 0 there is a witness with m.h <= 0   (relaxes P<0 to P<=0);
  (C)   for facet gambles with chi > 0: all witnesses on the side chosen by s;
  (VF)  witnesses avoid the vertices: m_i <= 1 - dv;
  (TP)  at q = u the cells are those of T1 (K_u = T1).
Objective: maximise delta (strict acceptance margin); feasible iff delta* > 0.
Every constraint is necessary for a solution of CF(T1) coming from a cover with data x (PC), for good g,
up to: the vertex margin dv (VF is open in the continuum), the bound Mc on chart data, and the finite tau grid.
"""
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import coo_matrix
from dcf import setup, facet_h, PT
from pencil import cvec


class DCFPlus:
    def __init__(self, eps, x, G, F, ntau=12, dv=1e-3, Mc=1e3, refine=(1e-2, 1e-3), pencil=True):
        self.pencil = pencil
        self.eps, self.x, self.G, self.F = eps, x, np.asarray(G), np.asarray(F)
        kap, v, xp = setup(eps)
        self.v = v
        self.u = np.ones(3) / 3
        self.ntau, self.dv, self.Mc, self.refine = ntau, dv, Mc, refine
        self.nq, self.ng = len(G), len(F)
        self.iu = [i for i in range(self.nq) if np.allclose(self.G[i], self.u)]
        self.target = np.array([1 if PT(g, v) > 0 else (-1 if PT(-g, v) > 0 else 0) for g in self.F])

    def facet_list(self, q):
        rows = []
        for k in range(3):
            h0, h1 = facet_h(k, 0.0, self.v), facet_h(k, 1.0, self.v)
            c0, c1 = cvec(k, h0, self.x) @ q, cvec(k, h1, self.x) @ q
            taus = list(np.linspace(0, 1, self.ntau + 2)[1:-1])
            if abs(c1 - c0) > 1e-15:
                ts = -c0 / (c1 - c0)
                for e in self.refine:
                    taus += [ts - e, ts + e]
            for tau in sorted(t for t in taus if 0 < t < 1):
                h = facet_h(k, tau, self.v); h = h / np.linalg.norm(h)
                rows.append((k, tau, h, cvec(k, h, self.x) @ q))
        return rows

    def build(self):
        self.var = 0
        lb, ub, integ = [], [], []

        def newvar(l, u_, integer=False):
            i = self.var; self.var += 1
            lb.append(l); ub.append(u_); integ.append(1 if integer else 0)
            return i
        R, C, V, LO, HI = [], [], [], [], []
        self.nrow = 0

        def addrow(d, l, h):
            for j, val in d.items():
                R.append(self.nrow); C.append(j); V.append(val)
            LO.append(l); HI.append(h); self.nrow += 1
        Mc = self.Mc
        delta = newvar(0, 1.0)
        self.delta = delta
        cv = {}
        for gi, g in enumerate(self.F):
            s = np.sign(g)
            cv[gi] = [newvar(-Mc, Mc) for _ in range(6)]
            for i in range(3):
                addrow({cv[gi][i]: s[i]}, 1, np.inf)
                addrow({cv[gi][3 + i]: -s[i]}, 1, np.inf)
        self.cv = cv
        z = {}
        Mz = 10 * Mc
        for qi, q in enumerate(self.G):
            for gi in range(self.ng):
                if qi in self.iu:
                    t = self.target[gi]
                    zz = [newvar(1 if t == 1 else 0, 1 if t == 1 else 0, True),
                          newvar(1 if t == 0 else 0, 1 if t == 0 else 0, True),
                          newvar(1 if t == -1 else 0, 1 if t == -1 else 0, True)]
                else:
                    zz = [newvar(0, 1, True) for _ in range(3)]
                z[qi, gi] = zz
                zp, z0, zm = zz
                addrow({zp: 1, z0: 1, zm: 1}, 1, 1)
                c = cv[gi][:3]; cp = cv[gi][3:]
                d = {c[i]: q[i] for i in range(3)}; d[zp] = -Mz; addrow(d, 1 - Mz, np.inf)
                d = {c[i]: q[i] for i in range(3)}
                for i in range(3): d[cp[i]] = d.get(cp[i], 0) - q[i]
                d[zp] = -Mz; addrow(d, 1 - Mz, np.inf)
                d = {cp[i]: q[i] for i in range(3)}; d[zm] = -Mz; addrow(d, 1 - Mz, np.inf)
                d = {cp[i]: q[i] for i in range(3)}
                for i in range(3): d[c[i]] = d.get(c[i], 0) - q[i]
                d[zm] = -Mz; addrow(d, 1 - Mz, np.inf)
                d = {c[i]: q[i] for i in range(3)}; d[z0] = Mz; addrow(d, -np.inf, Mz)
                d = {cp[i]: q[i] for i in range(3)}; d[z0] = Mz; addrow(d, -np.inf, Mz)
        self.z = z
        # credal sets via witnesses (skip q = u: K_u = T1 is consistent with the fixed target cells)
        SF = np.vstack([self.F, -self.F])
        Mw = 2.0
        self.wit = {}
        self.sbits = {}
        for qi, q in enumerate(self.G):
            if qi in self.iu:
                continue
            fac = self.facet_list(q) if self.pencil else []
            acc = [z[qi, gi][0] for gi in range(self.ng)] + [z[qi, gi][2] for gi in range(self.ng)]
            reqs = []   # (vector h, activation var or None, kind)
            for si in range(2 * self.ng):
                reqs.append((SF[si], acc[si], 'gen'))       # witness needed iff acc = 0
            sb = []
            for (k, tau, h, chi) in fac:
                if chi < -1e-13:
                    reqs.append((h, None, 'R1'))
                elif chi > 1e-13:
                    sb.append((newvar(0, 1, True), h, k, tau))
            self.sbits[qi] = sb
            W = []
            for (h, a, kind) in reqs:
                m = [newvar(0, 1) for _ in range(3)]
                W.append(m)
                addrow({m[i]: 1.0 for i in range(3)}, 1, 1)
                for i in range(3):
                    addrow({m[i]: 1.0}, -np.inf, 1 - self.dv)
                if kind == 'gen':      # a = 0 (rejected) => m.h <= 0
                    d = {m[i]: h[i] for i in range(3)}; d[a] = -Mw; addrow(d, -np.inf, 0)
                else:
                    addrow({m[i]: h[i] for i in range(3)}, -np.inf, 0)
            self.wit[qi] = W
            for m in W:
                for si in range(2 * self.ng):      # accepted => m.a >= delta
                    a = SF[si]
                    d = {m[i]: a[i] for i in range(3)}; d[delta] = -1; d[acc[si]] = -Mw
                    addrow(d, -Mw, np.inf)
                for (s, h, k, tau) in sb:
                    d = {m[i]: h[i] for i in range(3)}; d[s] = -Mw; addrow(d, -Mw, np.inf)   # s=1 => m.h>=0
                    d = {m[i]: h[i] for i in range(3)}; d[s] = -Mw; addrow(d, -np.inf, 0)   # s=0 => m.h<=0
        self.A = coo_matrix((V, (R, C)), shape=(self.nrow, self.var)).tocsr()
        self.lo, self.hi = np.array(LO), np.array(HI)
        self.lb, self.ub, self.integ = np.array(lb, float), np.array(ub, float), np.array(integ)

    def solve(self, time_limit=600, disp=False):
        c = np.zeros(self.var); c[self.delta] = -1.0
        res = milp(c, constraints=LinearConstraint(self.A, self.lo, self.hi), integrality=self.integ,
                   bounds=Bounds(self.lb, self.ub), options={'time_limit': time_limit, 'disp': disp})
        return res

    def cells(self, x):
        Z = np.zeros((self.nq, self.ng), int)
        for (qi, gi), zz in self.z.items():
            Z[qi, gi] = [1, 0, -1][int(np.argmax([x[j] for j in zz]))]
        return Z

    def credal(self, x, qi):
        return np.array([[x[j] for j in m] for m in self.wit[qi]])
