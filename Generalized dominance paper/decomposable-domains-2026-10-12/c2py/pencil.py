"""Per-prior admissibility of K_q under the facet-pencil constraints (PC data at p*=u):
  (R1)  c_k(h).q < 0  =>  P(q,h) < 0          (Lemma R1, writeup lem:R1N28)
  (C)   c_k(h).q > 0  =>  P(q,h) >= 0 or P(q,-h) >= 0   (Lemma C of C2_notes: no strict straddle)
for every facet gamble h = h_k(tau), tau in a grid.  K = conv(m_1..m_N), vertex-free (m_j,b <= 1-dv).
MILP per prior (HiGHS via scipy).  Optional extra linear objective/constraints for probing."""
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from dcf import setup, facet_h, E


def cvec(k, h, x):
    h1, h2, h3 = h
    if k == 0:
        return np.array([-(x * h2 + h3), x * h2, h3])
    if k == 1:
        return np.array([h1, -(h1 + x * h3), x * h3])
    return np.array([x * h1, h2, -(x * h1 + h2)])


def facet_rows(q, eps, x, ntau=80, tol=1e-12):
    kap, v, xp = setup(eps)
    rows = []   # (k, tau, h, chi)
    for k in range(3):
        # chi is affine in tau: find its root tau* and refine the grid geometrically around it
        h0, h1 = facet_h(k, 0.0, v), facet_h(k, 1.0, v)
        c0, c1 = cvec(k, h0, x) @ q, cvec(k, h1, x) @ q
        taus = list(np.linspace(0.0, 1.0, ntau + 2)[1:-1])
        if abs(c1 - c0) > 1e-15:
            ts = -c0 / (c1 - c0)
            for e in 10.0 ** -np.arange(2, 7):
                taus += [ts - e, ts + e]
        taus = sorted(t for t in taus if 0 < t < 1)
        for tau in taus:
            h = facet_h(k, tau, v)
            h = h / np.linalg.norm(h)
            chi = cvec(k, h, x) @ q
            rows.append((k, tau, h, chi))
    return rows


def admissible(q, eps, x, N=4, ntau=80, delta=None, dv=1e-3, extra=None, obj=None, time_limit=60):
    """extra(mvars_index_fn) -> list of (coef dict, lo, hi) linear constraints on vertex coordinates.
    obj: dict var->coef (minimise).  Returns (status, M (N,3) or None)."""
    rows = facet_rows(q, eps, x, ntau)
    scale = max(1e-12, min(q))           # natural length scale near a vertex
    if delta is None:
        delta = 0.0   # faithful relaxation of the strict inequality in (R1)
    # variables: m (N*3), then binaries
    nm = 3 * N
    cons, lo, hi = [], [], []
    nb = 0
    binmap = []
    def add(d, l, h):
        cons.append(d); lo.append(l); hi.append(h)
    for j in range(N):
        add({3 * j + i: 1.0 for i in range(3)}, 1, 1)
        for b in range(3):
            add({3 * j + b: 1.0}, -np.inf, 1 - dv)
    Mbig = 4.0
    for (k, tau, h, chi) in rows:
        if chi < -1e-13:
            # exists j: m_j.h <= -delta  : binaries y_j, sum y_j >= 1, m_j.h <= -delta + M(1-y_j)
            ys = list(range(nm + nb, nm + nb + N)); nb += N
            add({y: 1.0 for y in ys}, 1, np.inf)
            for j, y in enumerate(ys):
                d = {3 * j + i: h[i] for i in range(3)}; d[y] = Mbig
                add(d, -np.inf, -delta + Mbig)
        elif chi > 1e-13:
            s = nm + nb; nb += 1
            for j in range(N):
                d = {3 * j + i: h[i] for i in range(3)}; d[s] = -Mbig   # s=1 => m.h >= 0
                add(d, -Mbig, np.inf)
                d = {3 * j + i: h[i] for i in range(3)}; d[s] = -Mbig   # s=0 => m.h <= 0
                add(d, -np.inf, 0.0)
    if extra is not None:
        for (d, l, h_) in extra:
            add(d, l, h_)
    nv = nm + nb
    A = np.zeros((len(cons), nv))
    for r, d in enumerate(cons):
        for kk, val in d.items():
            A[r, kk] = val
    c = np.zeros(nv)
    if obj:
        for kk, val in obj.items():
            c[kk] = val
    integ = np.r_[np.zeros(nm), np.ones(nb)]
    lb = np.r_[np.zeros(nm), np.zeros(nb)]
    ub = np.r_[np.ones(nm), np.ones(nb)]
    res = milp(c, constraints=LinearConstraint(A, lo, hi), integrality=integ, bounds=Bounds(lb, ub),
               options={'time_limit': time_limit})
    if res.x is None:
        return res.status, None, res
    return res.status, res.x[:nm].reshape(N, 3), res
