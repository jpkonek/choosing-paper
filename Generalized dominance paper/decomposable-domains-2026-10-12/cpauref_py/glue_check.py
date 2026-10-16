"""CPaU referee: discrete sanity checks of the glue in Remark rem:CPaU (NUMERICS only).
(1) c_i(g) = rho_i(gbar)(lam_i(gbar,0) - lam_i(gbar,a_g)) has the strict sign of g_i.
(2) Lambda_i X = Lambda_i(W_i) + w_i 1_{E_i(X)}  (so a full-support state P_i gives an adding-up weight nu_i = P_i(w_i 1_.)).
(3) the p-Bayes models of the integral field over subsets of a finite sample of U are exactly B_p u S, S in Z_p.
Run: python3 -I glue_check.py
"""
import itertools, random
random.seed(7)
eps, s = 0.4, 0.5
u = [1/3]*3
T1 = [[(1-eps)/3 + eps*(k==j) for j in range(3)] for k in range(3)]
Kp = [[u[j] + s*(T1[k][j]-u[j]) for j in range(3)] for k in range(3)]
def P(K, g): return min(sum(m[j]*g[j] for j in range(3)) for m in K)
def inU(g): return P(Kp, g) > 0
def sample_U(n):
    out = []
    while len(out) < n:
        g = [random.gauss(0,1) for _ in range(3)]
        if inU(g): out.append(g)
        elif inU([-x for x in g]): out.append([-x for x in g])
    return out
# rank at world i of advice 'acc' (accept orientation g) vs '0': good < 0 < bad
def lam_table(g):
    # random bounded strictly rank-increasing penalties: values for good, none, bad
    t = []
    for i in range(3):
        a, b, c = sorted(random.uniform(-5, 5) for _ in range(3))
        while not (a < b < c): a, b, c = sorted(random.uniform(-5, 5) for _ in range(3))
        lam_acc = a if g[i] > 0 else c
        t.append((lam_acc, b))       # (lam_i(g, accept g), lam_i(g, none))
    return t
fails = 0
for trial in range(200):
    G = sample_U(9)
    L = [lam_table(g) for g in G]
    R = [[random.uniform(0.01, 3) for _ in range(3)] for g in G]
    c = [[R[k][i]*(L[k][i][1]-L[k][i][0]) for i in range(3)] for k in range(len(G))]
    # (1)
    for k, g in enumerate(G):
        for i in range(3):
            if (c[k][i] > 0) != (g[i] > 0): fails += 1
    # (2)
    w = [[abs(L[k][i][0]-L[k][i][1]) for i in range(3)] for k in range(len(G))]
    for X in itertools.product([0,1], repeat=len(G)):
        for i in range(3):
            for k, g in enumerate(G):
                lamX = L[k][i][0] if X[k] else L[k][i][1]
                ideal = 1 if g[i] > 0 else 0
                lamW = L[k][i][0] if ideal else L[k][i][1]
                err = 1 if X[k] != ideal else 0
                if abs(lamX - (lamW + w[k][i]*err)) > 1e-12: fails += 1
    # (3) with a planted tie
    p = [random.uniform(0.05,1) for _ in range(3)]; z = sum(p); p = [x/z for x in p]
    k0 = random.randrange(len(G))
    # rescale rho at k0 world 0 so that p.c(g_k0) = 0 (keeps strict sign since other coords fix it if possible)
    rest = sum(p[i]*c[k0][i] for i in (1,2))
    if (-rest/p[0] > 0) == (c[k0][0] > 0):
        c[k0][0] = -rest/p[0]
    def obj(X): return sum(p[i]*(sum((-c[k][i]) * X[k] for k in range(len(G)))) for i in range(3))
    vals = {X: obj(X) for X in itertools.product([0,1], repeat=len(G))}
    m = min(vals.values())
    Bp = tuple(1 if sum(p[i]*c[k][i] for i in range(3)) > 1e-12 else 0 for k in range(len(G)))
    Zp = [k for k in range(len(G)) if abs(sum(p[i]*c[k][i] for i in range(3))) <= 1e-12]
    for X, v in vals.items():
        isbayes = v <= m + 1e-9
        form = all(X[k] == Bp[k] for k in range(len(G)) if k not in Zp)
        if isbayes != form: fails += 1
print("trials 200, failures:", fails)
