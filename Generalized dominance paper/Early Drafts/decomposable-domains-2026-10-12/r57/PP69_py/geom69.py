"""geom69: exact checks for PP69 (curve, thresholds, the pathwise-Bayes field).

Curve parameter theta in [0,1]:
  [0,1/3]  R_alpha, alpha = 3 theta,     K = (1-alpha) M + alpha K_N
  [1/3,2/3] J_beta,  beta = 3 theta - 1, K = (1-beta) K_N + beta K_L0
  [2/3,1]  F_t,     t = 3 theta - 2,     K = conv(v_t, M0), v_t = (1-t) v3 + t h12
Index p(theta) = (1-theta) u + theta h12, i.e. lambda_theta = ((2+theta)/6, (2+theta)/6, (2-2theta)/6).

Checks (exact rationals):
  C1  per-problem advice pattern along the curve equals the predicted one
      (constant; x->S at tau1 in (0,1/3]; S->y at tau2 in (1/3,1); x->S->y), on a dense theta grid
      and at tau +- 1e-6;
  C2  pattern census by class, with A/B labels (majority/minority);
  C3  field phi(g, .) of PP69 §2 is strictly rank-monotone at every world;
  C4  C_theta(g) is the UNIQUE argmin of lambda_theta . phi(g, .) over {+,-,S,X} at every grid theta
      different from the thresholds, including theta = 0 and theta = 1;
  C5  phi_1 = phi_2 on class M3; swap-equivariance phi(sigma g) = swap phi(g) and tau(sigma g) = tau(g);
  C6  every forward switch strictly decreases phi_1 + phi_2 and strictly increases phi_3
      (used in Lemma 3.2 and Prop 3.5).
Run: python3 -I -B geom69.py > geom69.out
"""
from fractions import Fraction as Fr
import itertools, random
random.seed(69)
c, e = Fr(7, 30), Fr(3, 10)
MV = [tuple(c + (e if i == v else 0) for i in range(3)) for v in range(3)]
M0 = [(Fr(16, 23), Fr(7, 23), Fr(0)), (Fr(7, 23), Fr(16, 23), Fr(0))]
h12 = (Fr(1, 2), Fr(1, 2), Fr(0))
v3 = MV[2]
KN = MV + M0
KL0 = [v3] + M0
dot = lambda k, g: sum(k[i] * g[i] for i in range(3))
mn = lambda K, g, sg: min(sg * dot(k, g) for k in K)
TH1, TH2 = Fr(1, 3), Fr(2, 3)


def val(theta, g, sg):
    """min over K_theta of sg*k.g (support-function form; exact)."""
    if theta <= TH1:
        a = 3 * theta
        return (1 - a) * mn(MV, g, sg) + a * mn(KN, g, sg)
    if theta <= TH2:
        b = 3 * theta - 1
        return (1 - b) * mn(KN, g, sg) + b * mn(KL0, g, sg)
    t = 3 * theta - 2
    vt = tuple((1 - t) * v3[i] + t * h12[i] for i in range(3))
    return min(sg * dot(vt, g), mn(M0, g, sg))


def adv(theta, g):
    for sg in (1, -1):
        if val(theta, g, sg) > 0:
            return sg
    return 0


def thresholds(g):
    """exact (tau1, tau2) or None; tau1 = R-silencing time, tau2 = first answer time on [1/3,1]."""
    T, N, D = adv(Fr(0), g), adv(TH1, g), adv(Fr(1), g)
    tau1 = tau2 = None
    if T != 0 and N == 0:
        sg = T
        hM, hN = mn(MV, g, sg), mn(KN, g, sg)          # hM > 0 >= hN
        a = hM / (hM - hN)
        tau1 = a / 3
    if N == 0 and D != 0:
        sg = D
        hN, hL = mn(KN, g, sg), mn(KL0, g, sg)
        if hL > 0:
            b = -hN / (hL - hN)
            tau2 = (1 + b) / 3
        else:
            x0, x1 = sg * dot(v3, g), sg * dot(h12, g)   # x0 <= 0 < x1
            t = -x0 / (x1 - x0)
            tau2 = (2 + t) / 3
    return T, N, D, tau1, tau2


def cls(g):
    s = [1 if x > 0 else -1 for x in g]
    if s[0] == s[1] == s[2]:
        return 0
    for o in range(3):
        if s[(o + 1) % 3] == s[(o + 2) % 3]:
            return o + 1


def lab(x, g):
    """A (majority), B (minority), S, or U (unanimous correct)."""
    o = cls(g)
    if x == 0:
        return 'S'
    if o == 0:
        return 'U' if x * g[0] > 0 else 'Uwrong'
    return 'B' if x * g[o - 1] > 0 else 'A'


def rank(x, g, w):  # x in {1,-1,0,'X'}
    if x == 'X':
        return 3
    if x == 0:
        return 1
    return 0 if x * g[w] > 0 else 2


def phi(g):
    """PP69 field: dict advice -> (phi_1, phi_2, phi_3); f = |g| * phi."""
    o = cls(g)
    T, N, D, t1, t2 = thresholds(g)
    out = {0: (Fr(0),) * 3}
    if o == 0:
        cor = 1 if g[0] > 0 else -1
        out[cor] = (Fr(-1),) * 3
        out[-cor] = (Fr(1),) * 3
    elif o == 3:
        A = 1 if g[0] > 0 else -1      # majority sign (worlds 1,2)
        B = -A
        lT = lab(T, g)
        if lT == 'S':                       # S -> A at t2
            PA, RA = -(1 - t2), 2 + t2
            PB, RB = Fr(1), Fr(-1)
        elif lT == 'A':                     # A throughout
            PA, RA, PB, RB = Fr(-1), Fr(1), Fr(1), Fr(-1)
        else:                               # B -> S (t1) -> A (t2)
            PA, RA = -(1 - t2), 2 + t2
            PB, RB = 1 - t1, -(2 + t1)
        out[A] = (PA, PA, RA)
        out[B] = (PB, PB, RB)
    else:
        # class 1 or 2: odd world o; vector (odd, other12, world3)
        A = 1 if g[(o % 2)] > 0 else -1     # majority sign = sign of the other of worlds 1,2 (and of world 3)
        B = -A
        lT, lD = lab(T, g), lab(D, g)
        def dl(t):
            return 2 * (1 - t) / (2 + t)
        if lT == 'A' and N != 0:             # A constant
            a, b = (1, 2, 1), (1, 2, 1)
        elif lT == 'B':                      # B constant
            a, b = (3, 1, 1), (4, 1, 1)
        elif lT == 'A':                      # A -> S (t1) [-> B (t2)]
            a = (1 + dl(t1), 1, 1)
            b = (1 + dl(t2), 1, 1) if lD == 'B' else (1, 2, 1)
        else:                                # T silent: S [-> B]
            a = (3, 1, 1)
            b = (1 + dl(t2), 1, 1) if lD == 'B' else (1, 2, 1)
        pa = (Fr(a[0]), -Fr(a[1]), -Fr(a[2]))   # (odd, other, w3): A wrong at odd, right elsewhere
        pb = (-Fr(b[0]), Fr(b[1]), Fr(b[2]))
        def place(v):
            return (v[0], v[1], v[2]) if o == 1 else (v[1], v[0], v[2])
        out[A] = place(pa)
        out[B] = place(pb)
    mx = [max(out[k][w] for k in out) + 1 for w in range(3)]
    out['X'] = tuple(mx)
    return out


def lam(theta):
    return ((2 + theta) / 6, (2 + theta) / 6, (2 - 2 * theta) / 6)


ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok &= bool(cond)


G = [g for g in itertools.product(range(-6, 7), repeat=3) if all(x != 0 for x in g)]
G += [tuple(Fr(random.randint(-400, 400), random.randint(1, 60)) for _ in range(3)) for _ in range(6000)]
G = [g for g in G if all(x != 0 for x in g)]
grid = [Fr(k, 96) for k in range(97)]
eps = Fr(1, 10**6)

c1 = c3 = c4 = c5 = c6 = True
census = {}
for g in G:
    T, N, D, t1, t2 = thresholds(g)
    o = cls(g)
    # C1 predicted advice
    def pred(th):
        if t1 is not None and th > t1 and (t2 is None or th < t2):
            return 0
        if t1 is None and t2 is not None and th < t2:
            return 0
        if t2 is not None and th > t2:
            return D
        return T if t1 is None or th < t1 else 0
    pts = list(grid)
    for t in (t1, t2):
        if t is not None:
            pts += [t - eps, t + eps]
            c1 &= (Fr(0) < t < 1)
    if t1 is not None: c1 &= t1 <= TH1
    if t2 is not None: c1 &= t2 > TH1
    for th in pts:
        if 0 <= th <= 1 and th not in (t1, t2):
            c1 &= adv(th, g) == pred(th)
    key = (o, lab(T, g), 'S' if t1 is not None else '-', lab(D, g) if t2 is not None else '-')
    census[key] = census.get(key, 0) + 1
    # C3 rank monotone
    F = phi(g)
    for w in range(3):
        order = sorted(F.keys(), key=lambda a: rank(a, g, w))
        rks = [rank(a, g, w) for a in order]
        vals = [F[a][w] for a in order]
        c3 &= all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)) and len(set(rks)) == len(rks)
    # C4 unique argmin
    for th in pts:
        if 0 <= th <= 1 and th not in (t1, t2):
            L = lam(th)
            sc = {a: sum(L[w] * F[a][w] for w in range(3)) for a in F}
            best = min(sc.values())
            arg = [a for a in sc if sc[a] == best]
            c4 &= (arg == [adv(th, g)])
    # C5 symmetry
    sg = (g[1], g[0], g[2])
    if o == 3:
        c5 &= all(F[a][0] == F[a][1] for a in F)
    Ts = thresholds(sg)
    c5 &= (Ts[3], Ts[4]) == (t1, t2)
    Fs = phi(sg)
    c5 &= all(Fs[a] == (F[a][1], F[a][0], F[a][2]) for a in F)
    # C6 forward switches: phi1+phi2 strictly down, phi3 strictly up
    seq = [T]
    if t1 is not None: seq.append(0)
    if t2 is not None: seq.append(D)
    for x, y in zip(seq, seq[1:]):
        c6 &= (F[y][0] + F[y][1] < F[x][0] + F[x][1]) and (F[y][2] > F[x][2])

chk("C1 advice along the curve = predicted pattern; 0 < tau1 <= 1/3 < tau2 < 1 (%d problems)" % len(G), c1)
print("C2 pattern census (class, T, R-silenced?, final answer if added): ")
for k in sorted(census, key=str):
    print("    ", k, census[k])
chk("C3 field strictly rank-monotone at every world", c3)
chk("C4 C_theta = unique argmin of lambda_theta.phi on grid + thresholds +- 1e-6, theta in [0,1]", c4)
chk("C5 phi_1 = phi_2 on M3; swap-equivariance of phi and of the thresholds", c5)
chk("C6 every forward switch lowers phi1+phi2 and raises phi3 strictly", c6)
print("ALL PASS" if ok else "SOME FAIL")
