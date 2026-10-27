"""C2 (round 15): NUMERICS for Theorem C2.1 (comonotone unanimity worlds, n = 2, M_U).

Run:  python3 -I ld_two_world.py
No proof depends on this script.  It discretises the mixed part M of U into x-cells
(x = chain coordinate of the coherent path C_s = D_[a's, b'+(1-b')s]), computes exact
Gaussian (= uniform angle) masses of the cells, and checks, on random and adversarial
test models, every property used in the proof:

  (a) C_s (cells with x < s) is exactly the world-1 error set of D_[a's, b'+(1-b')s]
      (geometric membership test at sample gambles of every cell);
  (b) competitiveness of every C_s on {1,2} (random X, and the exact fractional-knapsack
      worst case, which is what Lyapunov gives in the continuum);
  (c) every model X is weakly dominated by some C_s, strictly unless X = C_s;
  (d) sections {s : C_s <=_i X} are closed intervals [0,s1] and [s2,1], with s2 <= s1;
  (e) no leading density: for several candidate densities rho an explicit pair of regular
      models Y, Z with rho strictly favouring Y and Y not <=_1 Z;
  (f) negative control: a non-comonotone pair of members makes competitiveness fail.
"""
import math
import random

random.seed(20261015)

ALPHA, BETA = 0.35, 0.60          # K' = [alpha', beta'] in the weight t of world 2
NC = 400                           # x-cells per half (M^- and M^+)

# ---------------------------------------------------------------- geometry of M
def psi_of_ratio(r):
    """angle psi in (0,pi/2) with 1/(1+tan psi) = r"""
    return math.atan(1.0 / r - 1.0)

cells = []   # (half, k, mass, xmid)
for half in ('-', '+'):
    for k in range(NC):
        x0, x1 = k / NC, (k + 1) / NC
        if half == '-':     # sigma = alpha' x
            r0, r1 = ALPHA * x0 if x0 > 0 else 1e-15, ALPHA * x1
        else:               # tau = beta' + (1-beta') x
            r0, r1 = BETA + (1 - BETA) * x0, BETA + (1 - BETA) * x1
            if x1 == 1.0:
                r1 = 1 - 1e-15
        m = abs(psi_of_ratio(r0) - psi_of_ratio(r1)) / (2 * math.pi)
        cells.append((half, k, m, (x0 + x1) / 2))
MASS = [c[2] for c in cells]
XM = [c[3] for c in cells]
NCELL = len(cells)
N_PLUS_MASS = 0.25                 # the open quadrant g1, g2 > 0 (inside U)
MU_M = sum(MASS)

def gamble(half, x):
    """a gamble of M with chain coordinate x"""
    if half == '-':
        sig = ALPHA * x
        psi = psi_of_ratio(sig)
        return (-math.cos(psi), math.sin(psi))
    tau = BETA + (1 - BETA) * x
    psi = psi_of_ratio(tau)
    return (math.cos(psi), -math.sin(psi))

def accepted_by_interval(g, a, b):
    """g in D_[a,b] (t = weight of world 2): (1-t)g1 + t g2 > 0 for t in [a,b]"""
    return min((1 - a) * g[0] + a * g[1], (1 - b) * g[0] + b * g[1]) > 0

# ---------------------------------------------------------------- the worlds
F_MEMBERS = {'Fa': lambda x: 1.0 + x, 'Fb': lambda x: 1.0 + 3.0 * x * x}   # world 1
G_MEMBERS_ADD = {'G': lambda x: 1.0}                                         # world 2 additive
G_MEMBERS_INC = {'G1': lambda x: 1.0, 'G2': lambda x: 2.0 - x}               # world 2 incomplete
N_DENS = 1.0    # every member has density 1 on N_+ (any positive value works)

def wvec(f):
    return [f(XM[i]) * MASS[i] for i in range(NCELL)]

def chain(s):
    """fractional indicator of c_s = {x < s} on the cells"""
    v = []
    for (half, k, m, xm) in cells:
        x0, x1 = k / NC, (k + 1) / NC
        v.append(1.0 if s >= x1 else (0.0 if s <= x0 else (s - x0) * NC))
    return v

def dot(a, b):
    return sum(p * q for p, q in zip(a, b))

class System:
    def __init__(self, F, G):
        self.WF = {n: wvec(f) for n, f in F.items()}
        self.WG = {n: wvec(g) for n, g in G.items()}

    # a model X is (A, nmiss): A = fractional world-1 error indicator on M-cells,
    # nmiss = mu-mass of N_+ not accepted (both worlds err there)
    def le1(self, A1, n1, A2, n2):   # X1 <=_1 X2
        return all(dot(w, A1) + N_DENS * n1 <= dot(w, A2) + N_DENS * n2 + 1e-12
                   for w in self.WF.values())

    def le2(self, A1, n1, A2, n2):   # world-2 errors on M are M \ A
        return all(dot(w, [1 - a for a in A1]) + N_DENS * n1 <=
                   dot(w, [1 - a for a in A2]) + N_DENS * n2 + 1e-12
                   for w in self.WG.values())

def rand_model():
    kind = random.random()
    if kind < 0.4:
        A = [float(random.random() < 0.5) for _ in range(NCELL)]
    elif kind < 0.7:   # perturbed chain member
        s = random.random()
        A = chain(s)
        for _ in range(random.randint(1, 40)):
            i = random.randrange(NCELL)
            A[i] = 1.0 - A[i] if random.random() < 0.7 else random.random()
    else:              # band-structured
        A = [float(random.random() < XM[i] ** random.choice([0.3, 1, 3])) for i in range(NCELL)]
    nmiss = 0.0 if random.random() < 0.5 else random.random() * 0.05
    return A, nmiss

S_GRID = [j / 800 for j in range(801)]

def check_system(name, sysm, trials=400):
    print(f"=== system {name}: world 1 members {list(sysm.WF)}, world 2 members {list(sysm.WG)}")
    # (a) coherence of the chain: geometric test
    bad = 0
    for s in [0.0, 0.13, 0.5, 0.77, 1.0]:
        a, b = ALPHA * s, BETA + (1 - BETA) * s
        for (half, k, m, xm) in cells[::7]:
            for xx in (k / NC + 0.2 / NC, k / NC + 0.8 / NC):
                g = gamble(half, xx)
                acc = accepted_by_interval(g, a, b)
                err1 = (not acc) if g[0] > 0 else acc
                if err1 != (xx < s):
                    bad += 1
    print(f"(a) chain = error sets of D_[a's, b'+(1-b')s]: mismatches {bad}")
    # (b) competitiveness, random X
    fails = 0
    for _ in range(trials):
        A, nm = rand_model()
        for s in S_GRID[::20]:
            c = chain(s)
            if not (sysm.le1(c, 0.0, A, nm) or sysm.le2(c, 0.0, A, nm)):
                fails += 1
    print(f"(b) competitiveness failures over {trials} random X x 41 indices: {fails}")
    # (b') exact worst case: for each world-1 member f and world-2 member g, minimise f(A)
    # subject to g(A) >= g(c_s) + eps by fractional knapsack (ratio f/g ascending)
    worst = float('inf')
    for s in S_GRID[1:-1:25]:
        c = chain(s)
        for wf in sysm.WF.values():
            for wg in sysm.WG.values():
                target = dot(wg, c)
                order = sorted(range(NCELL), key=lambda i: wf[i] / wg[i])
                acc_g, acc_f = 0.0, 0.0
                for i in order:
                    take = min(1.0, (target - acc_g) / wg[i]) if acc_g < target else 0.0
                    acc_g += take * wg[i]
                    acc_f += take * wf[i]
                worst = min(worst, acc_f - dot(wf, c))
    print(f"(b') min over s, members of [min f(A) s.t. g(A) >= g(c_s)] - f(c_s): {worst:.3e} (>= 0 expected)")
    # (c),(d) domination and sections
    viol_sec, viol_dom, strict_ok = 0, 0, 0
    for _ in range(trials):
        A, nm = rand_model()
        S1 = [s for s in S_GRID[::4] if sysm.le1(chain(s), 0.0, A, nm)]
        S2 = [s for s in S_GRID[::4] if sysm.le2(chain(s), 0.0, A, nm)]
        # sections are intervals containing 0 resp. 1
        def is_interval(S, left):
            if not S:
                return False
            G = S_GRID[::4]
            idx = [G.index(s) for s in S]
            contiguous = idx == list(range(idx[0], idx[-1] + 1))
            return contiguous and ((idx[0] == 0) if left else (idx[-1] == len(G) - 1))
        if not (is_interval(S1, True) and is_interval(S2, False)):
            viol_sec += 1
        # exact section ends by bisection (s -> f(c_s) is continuous and monotone)
        lo, hi = 0.0, 1.0
        for _ in range(50):
            mid = (lo + hi) / 2
            if sysm.le1(chain(mid), 0.0, A, nm):
                lo = mid
            else:
                hi = mid
        s1 = lo
        lo, hi = 0.0, 1.0
        for _ in range(50):
            mid = (lo + hi) / 2
            if sysm.le2(chain(mid), 0.0, A, nm):
                hi = mid
            else:
                lo = mid
        s2 = hi
        if s2 > s1 + 1e-9:
            viol_dom += 1
            continue
        s = min(max((s1 + s2) / 2, s2), s1)
        c = chain(s)
        if not (sysm.le1(c, 0.0, A, nm) and sysm.le2(c, 0.0, A, nm)):
            # tolerance at a common end point
            s = s1
            c = chain(s)
        tied1 = sysm.le1(A, nm, c, 0.0)
        tied2 = sysm.le2(A, nm, c, 0.0)
        same = nm == 0 and max(abs(p - q) for p, q in zip(A, c)) < 1e-9
        if (tied1 and tied2) and not same:
            viol_dom += 1
        else:
            strict_ok += 1
    print(f"(d) section shape violations: {viol_sec};  (c) X not dominated by some C_s: {viol_dom}; "
          f"strictly dominated or equal: {strict_ok}/{trials}")

def no_leading(sysm):
    print("(e) no leading density for world 1: explicit rho-favoured comparisons that world 1 rejects")
    cands = {
        'Fa': [F_MEMBERS['Fa'](x) for x in XM],
        'Fb': [F_MEMBERS['Fb'](x) for x in XM],
        '(Fa+Fb)/2': [(F_MEMBERS['Fa'](x) + F_MEMBERS['Fb'](x)) / 2 for x in XM],
        'random': [0.5 + random.random() for _ in XM],
    }
    for name, rho in cands.items():
        found = None
        for wn, f in F_MEMBERS.items():
            ratio = [f(XM[i]) / rho[i] for i in range(NCELL)]
            i = min(range(NCELL), key=lambda j: ratio[j])
            j = max(range(NCELL), key=lambda j: ratio[j])
            if ratio[j] - ratio[i] < 1e-9:
                continue
            # P inside cell i, Q inside cell j (fractions), rho(P) = 1.05 rho(Q)
            q = 0.5
            rhoQ = q * rho[j] * MASS[j]
            p = 1.05 * rhoQ / (rho[i] * MASS[i])
            if p > 1:
                q *= 0.9 / p
                rhoQ = q * rho[j] * MASS[j]
                p = 1.05 * rhoQ / (rho[i] * MASS[i])
            fP = p * f(XM[i]) * MASS[i]
            fQ = q * f(XM[j]) * MASS[j]
            # Y errs on Q, Z errs on P; rho strictly favours Y; world 1 needs f(Q) <= f(P)
            if fQ > fP:
                found = (wn, i, j, p * rho[i] * MASS[i], rhoQ, fP, fQ)
                break
        if found:
            wn, i, j, rP, rQ, fP, fQ = found
            print(f"   rho={name:10s}: rho(P)={rP:.4e} > rho(Q)={rQ:.4e}, but member {wn}: "
                  f"f(Q)={fQ:.4e} > f(P)={fP:.4e}  => Y not <=_1 Z")
        else:
            print(f"   rho={name:10s}: NO violating pair found (unexpected)")

def negative_control():
    print("=== negative control: world 1 members Fa = 1+x and Fc = 2-x (not comonotone), world 2 = mu")
    F = {'Fa': F_MEMBERS['Fa'], 'Fc': lambda x: 2.0 - x}
    sysm = System(F, G_MEMBERS_ADD)
    fails = 0
    for s in S_GRID[1:-1:40]:
        c = chain(s)
        # swap: remove a slice just below s from c, add a slightly heavier (in mu) slice above s
        A = c[:]
        lo = sorted([i for i in range(NCELL) if XM[i] < s], key=lambda i: XM[i])[:3]
        hi = sorted([i for i in range(NCELL) if XM[i] > s], key=lambda i: -XM[i])[:3]
        if not lo or not hi:
            continue
        for i in lo:
            A[i] = 0.0
        mlo = sum(MASS[i] for i in lo)
        need = 1.02 * mlo
        for i in hi:
            take = min(1.0, need / MASS[i])
            A[i] = take
            need -= take * MASS[i]
            if need <= 0:
                break
        if not (sysm.le1(c, 0.0, A, 0.0) or sysm.le2(c, 0.0, A, 0.0)):
            fails += 1
    print(f"   competitiveness failures found at {fails} of the tested interior indices (> 0 expected)")

if __name__ == '__main__':
    print(f"K' = [{ALPHA}, {BETA}], {NCELL} x-cells, mu(M) = {MU_M:.6f}")
    sysA = System(F_MEMBERS, G_MEMBERS_ADD)
    check_system('C2.1(i): world 1 = unanimity{1+x, 1+3x^2}, world 2 additive (mu)', sysA)
    no_leading(sysA)
    sysB = System(F_MEMBERS, G_MEMBERS_INC)
    check_system('C2.1(ii): world 1 = unanimity{1+x, 1+3x^2}, world 2 = unanimity{1, 2-x}', sysB, trials=250)
    sysC = System({'Fa': lambda x: 1.0 + x, 'Fenvy': lambda x: 1.5 + x}, G_MEMBERS_ADD)
    check_system('C2.2 envy form: world 1 = unanimity{rho_a, rho_a + 0.5 rho_2}, world 2 = mu', sysC, trials=200)
    negative_control()
