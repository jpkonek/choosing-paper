# Independent referee check of the separation-gated two-world construction.
# Written from the note's definitions, not from check.py.
# Exact arithmetic (Fractions). Run: python3 -I referee_check.py
import itertools, random, sys
from fractions import Fraction as F

ADV = 'PSMC'   # accept g, silent, accept -g, contradiction
R = {1: {'P': 0, 'S': 1, 'M': 2, 'C': 3},      # mixed cell, world 1
     2: {'P': 2, 'S': 1, 'M': 0, 'C': 3}}      # mixed cell, world 2
RU = {'P': 0, 'S': 1, 'M': 2, 'C': 3}          # unanimous cell ('P' = correct), both worlds

def piecewise(knots):
    # strictly increasing piecewise-linear map through the given knots (exact)
    def f(x):
        for (a, fa), (b, fb) in zip(knots, knots[1:]):
            if a <= x <= b:
                return fa + (fb - fa) * (x - a) / (b - a)
        raise ValueError
    def finv(y):
        for (a, fa), (b, fb) in zip(knots, knots[1:]):
            if fa <= y <= fb:
                return a + (b - a) * (y - fa) / (fb - fa)
        raise ValueError
    return f, finv

FAMILIES = {
    # the note's example: C_{1/2} = D_[1/3,2/3]
    'note': ([(F(0), F(0)), (F(1, 2), F(1, 3)), (F(1), F(1))],
             [(F(0), F(0)), (F(1, 2), F(2, 3)), (F(1), F(1))]),
    # a family that becomes precise (l = u) on [0.7, 0.8]
    'precise_band': ([(F(0), F(0)), (F(1, 2), F(1, 3)), (F(7, 10), F(7, 10)), (F(4, 5), F(3, 4)), (F(1), F(1))],
                     [(F(0), F(0)), (F(1, 2), F(2, 3)), (F(7, 10), F(7, 10)), (F(4, 5), F(3, 4)), (F(1), F(1))]),
    # deliberately INVALID (u decreasing on [1/2,7/10]): control showing the checker detects failures
    'invalid_control': ([(F(0), F(0)), (F(1, 2), F(1, 3)), (F(7, 10), F(3, 5)), (F(4, 5), F(7, 10)), (F(1), F(1))],
                        [(F(0), F(0)), (F(1, 2), F(2, 3)), (F(7, 10), F(3, 5)), (F(4, 5), F(7, 10)), (F(1), F(1))]),
    # wide imprecision
    'wide': ([(F(0), F(0)), (F(1, 2), F(1, 10)), (F(1), F(1))],
             [(F(0), F(0)), (F(1, 2), F(9, 10)), (F(1), F(1))]),
}

class Sys:
    def __init__(self, N, U, seed, fam='note', phi='note'):
        rnd = random.Random(seed)
        ts = set()
        while len(ts) < N:
            ts.add(F(rnd.randint(1, 999), 1000))
        self.ts = sorted(ts)
        self.N, self.U = N, U
        self.mass = [F(rnd.randint(1, 9)) for _ in range(N + U)]
        self.l, self.linv = piecewise(FAMILIES[fam][0])
        self.u, self.uinv = piecewise(FAMILIES[fam][1])
        self.phi = phi
        # tau: distinct values in (0,1) per cell
        tau = [F(rnd.randint(1, 10**6), 10**6 + 1) for _ in range(N + U)]
        self.K = {1: {}, 2: {}}
        for c in range(N + U):
            for j in (1, 2, 3):
                if c < N and j < 3:
                    t = self.ts[c]
                    self.K[1][(c, j)] = self.linv(t) if j == 1 else self.uinv(t)
                    self.K[2][(c, j)] = 1 - (self.uinv(t) if j == 1 else self.linv(t))
                else:
                    # -1 - tau, with a tiny j-offset to keep the finite keys distinct
                    v = -1 - tau[c] * F(9, 10) - F(j, 100 * (N + U + 3))
                    self.K[1][(c, j)] = v
                    self.K[2][(c, j)] = v
        self.models = list(itertools.product(ADV, repeat=N + U))
        self.Ucache = {1: {}, 2: {}}

    def rank(self, X, c, w):
        return R[w][X[c]] if c < self.N else RU[X[c]]

    def steps(self, X, w):
        d = self.Ucache[w]
        if X not in d:
            d[X] = frozenset((c, j) for c in range(self.N + self.U) for j in (1, 2, 3) if self.rank(X, c, w) >= j)
        return d[X]

    def nu(self, S):
        return sum((self.mass[c] for (c, j) in S), F(0))

    def Phi(self, on, off, w):
        if self.phi == 'note':          # Phi_i = 2 on_i - off_i at both worlds (the note)
            return 2 * self.nu(on) - self.nu(off)
        if self.phi == 'script':        # check.py: world 2 uses on - 2 off
            return 2 * self.nu(on) - self.nu(off) if w == 1 else self.nu(on) - 2 * self.nu(off)
        raise ValueError

    def accept(self, X, Y, w, gate=True):
        if X == Y:
            return True
        UX, UY = self.steps(X, w), self.steps(Y, w)
        on, off = UY - UX, UX - UY
        if not off:
            return True
        if not on:
            return False
        if gate:
            K = self.K[w]
            if max(K[e] for e in on) > min(K[e] for e in off):
                return False
        return self.Phi(on, off, w) >= 0

    def selected(self, p):
        l, u = self.l(p), self.u(p)
        X = ['P' if t < l else ('M' if t > u else 'S') for t in self.ts] + ['P'] * self.U
        return tuple(X)

    def critical_ps(self):
        ps = {F(0), F(1)}
        for t in self.ts:
            ps.add(self.linv(t)); ps.add(self.uinv(t))
        ps = sorted(ps)
        mids = [(a + b) / 2 for a, b in zip(ps, ps[1:])]
        return sorted(set(ps) | set(mids)) + [F(k, 64) for k in range(65)]


def acyclic(S, w, gate=True):
    # Kahn's algorithm on the accepted non-identity relation
    idx = {X: n for n, X in enumerate(S.models)}
    succ = [[] for _ in S.models]
    indeg = [0] * len(S.models)
    for X in S.models:
        for Y in S.models:
            if X != Y and S.accept(X, Y, w, gate):
                succ[idx[X]].append(idx[Y]); indeg[idx[Y]] += 1
    q = [n for n in range(len(S.models)) if indeg[n] == 0]
    seen = 0
    while q:
        n = q.pop(); seen += 1
        for m in succ[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                q.append(m)
    return seen == len(S.models), sum(len(s) for s in succ)


def tc_violations(S, w, gate):
    # count (X,Y,Z) with X<=Y<=Z and Z strictly below X
    acc = {}
    M = S.models
    for X in M:
        for Y in M:
            acc[(X, Y)] = S.accept(X, Y, w, gate)
    succ = {X: [Y for Y in M if acc[(X, Y)]] for X in M}
    v = 0; ex = None
    for X in M:
        for Y in succ[X]:
            for Z in succ[Y]:
                if acc[(Z, X)] and not acc[(X, Z)]:
                    v += 1
                    if ex is None: ex = (X, Y, Z)
    return v, ex


def system_checks(S):
    out = {}
    M = S.models
    ps = S.critical_ps()
    sel = {p: S.selected(p) for p in ps}
    selset = set(sel.values())
    comp_fail = []; dom_sel = []; sect_fail = []; addit_fail = []
    for p in ps:
        C = sel[p]
        for X in M:
            a = {w: S.accept(C, X, w) for w in (1, 2)}
            # section identity: C_p <=_w X iff Phi_w(C_p,X) >= 0
            for w in (1, 2):
                UC, UX = S.steps(C, w), S.steps(X, w)
                ph = S.Phi(UX - UC, UC - UX, w)
                if a[w] != (ph >= 0):
                    sect_fail.append((p, X, w))
                # Prop 5(a): additive nu acceptance implies acceptance
                if S.nu(UX) >= S.nu(UC) and not a[w]:
                    addit_fail.append((p, X, w))
            ok = a[1] if p == 1 else (a[2] if p == 0 else (a[1] or a[2]))
            if not ok:
                comp_fail.append((p, X))
            if X != C and S.accept(X, C, 1) and S.accept(X, C, 2):
                dom_sel.append((p, X))
    # every non-selected model strictly dominated at both worlds by some selected
    undominated_rest = []
    for X in M:
        if X in selset:
            continue
        if not any(S.accept(C, X, 1) and not S.accept(X, C, 1) and S.accept(C, X, 2) and not S.accept(X, C, 2)
                   for C in selset):
            undominated_rest.append(X)
    # strict (G) on all pairs
    g_fail = 0
    for X in M:
        for Y in M:
            for w in (1, 2):
                rX = [S.rank(X, c, w) for c in range(S.N + S.U)]
                rY = [S.rank(Y, c, w) for c in range(S.N + S.U)]
                if all(a <= b for a, b in zip(rY, rX)):
                    if not S.accept(Y, X, w): g_fail += 1
                    if rY != rX and S.accept(X, Y, w): g_fail += 1
    out.update(n_selected=len(selset), comp_fail=len(comp_fail), comp_ex=comp_fail[:3],
               dom_selected=len(dom_sel), section_identity_fail=len(sect_fail),
               additive_not_accepted=len(addit_fail), undominated_nonselected=len(undominated_rest),
               undom_ex=undominated_rest[:3], strictG_fail=g_fail)
    return out


if __name__ == '__main__':
    configs = [(3, 1), (2, 2), (4, 0), (1, 3), (3, 2)]
    runs = [(f, 'note') for f in ('note', 'precise_band', 'wide')] + [('note', 'script'), ('invalid_control', 'note')]
    for fam, phi in runs:
        if True:
            for (N, U) in configs:
                for seed in (1, 2, 3, 4, 5):
                    S = Sys(N, U, seed, fam, phi)
                    ac = {w: acyclic(S, w)[0] for w in (1, 2)}
                    res = system_checks(S)
                    print(fam, phi, (N, U), seed, 'ts=', [str(t) for t in S.ts],
                          'acyclic=', ac, res, flush=True)
