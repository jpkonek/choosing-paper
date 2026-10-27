"""inst69: NUMERICS for PP69 Theorem 3.3 on an empirical, swap-symmetrised Gaussian sample.

The empirical measure has atoms, so Phi_1(C_theta) is a step function. The continuum member at the
crossing is emulated by splitting the switching atom group (an atom and its mirror) fractionally;
in the atomless Gaussian case this is the genuine member C_theta' (Lemma 3.2). Float arithmetic.
Tests:
  T1 Phi_1(C_theta) = Phi_2(C_theta) on a theta grid;
  T2 Phi_1 + Phi_2 non-increasing and Phi_3 non-decreasing along the curve;
  T3 class-3 fills (random, thin near the source's thresholds, maximal) of sources on a grid:
     the repair at theta' ties at worlds 1, 2 and is strictly better at world 3; the repair is
     silent on part of E (path obstruction respected);
  T4 swap-invariant splices C_a[H -> C_b] (H random, swap-closed): same, with theta' in [a, b];
  T5 (illustration of Props 5.1-5.3) class-1 fills and one-sided splices: no member on a fine
     grid dominates them.
Run: python3 -I -B inst69.py > inst69.out
"""
import random, math
import numpy as np
random.seed(691)
rng = np.random.default_rng(691)
c, e = 7/30, 0.3
MV = [tuple(c + (e if i == v else 0) for i in range(3)) for v in range(3)]
M0 = [(16/23, 7/23, 0.0), (7/23, 16/23, 0.0)]
h12 = (0.5, 0.5, 0.0); v3 = MV[2]
KN = MV + M0; KL0 = [v3] + M0
dot = lambda k, g: k[0]*g[0] + k[1]*g[1] + k[2]*g[2]
mn = lambda K, g, sg: min(sg * dot(k, g) for k in K)

def adv0(K, g):
    for sg in (1, -1):
        if mn(K, g, sg) > 0: return sg
    return 0

def cls(g):
    s = [1 if x > 0 else -1 for x in g]
    if s[0] == s[1] == s[2]: return 0
    for o in range(3):
        if s[(o+1) % 3] == s[(o+2) % 3]: return o + 1

def atom(g):
    T, N, D = adv0(MV, g), adv0(KN, g), adv0(M0, g)
    t1 = t2 = None
    if T != 0 and N == 0:
        hM, hN = mn(MV, g, T), mn(KN, g, T); t1 = hM / (hM - hN) / 3
    if N == 0 and D != 0:
        hN, hL = mn(KN, g, D), mn(KL0, g, D)
        if hL > 0: t2 = (1 + (-hN / (hL - hN))) / 3
        else:
            x0, x1 = D * dot(v3, g), D * dot(h12, g); t2 = (2 + (-x0 / (x1 - x0))) / 3
    o = cls(g); F = {0: np.zeros(3)}
    lab = lambda x: 'S' if x == 0 else ('U' if o == 0 else ('B' if x * g[o-1] > 0 else 'A'))
    if o == 0:
        cor = 1 if g[0] > 0 else -1; F[cor] = -np.ones(3); F[-cor] = np.ones(3)
    elif o == 3:
        A = 1 if g[0] > 0 else -1
        if lab(T) == 'S': PA, RA, PB, RB = -(1-t2), 2+t2, 1.0, -1.0
        elif lab(T) == 'A': PA, RA, PB, RB = -1.0, 1.0, 1.0, -1.0
        else: PA, RA, PB, RB = -(1-t2), 2+t2, 1-t1, -(2+t1)
        F[A] = np.array([PA, PA, RA]); F[-A] = np.array([PB, PB, RB])
    else:
        A = 1 if g[o % 2] > 0 else -1
        dl = lambda t: 2*(1-t)/(2+t)
        if lab(T) == 'A' and N != 0: a, b = (1, 2, 1), (1, 2, 1)
        elif lab(T) == 'B': a, b = (3, 1, 1), (4, 1, 1)
        elif lab(T) == 'A': a = (1+dl(t1), 1, 1); b = (1+dl(t2), 1, 1) if lab(D) == 'B' else (1, 2, 1)
        else: a = (3, 1, 1); b = (1+dl(t2), 1, 1) if lab(D) == 'B' else (1, 2, 1)
        pa = (a[0], -a[1], -a[2]); pb = (-b[0], b[1], b[2])
        pl = (lambda v: np.array(v, float)) if o == 1 else (lambda v: np.array((v[1], v[0], v[2]), float))
        F[A] = pl(pa); F[-A] = pl(pb)
    r = math.sqrt(sum(x*x for x in g))
    return dict(g=g, o=o, T=T, D=D, t1=t1, t2=t2, f={k: r*v for k, v in F.items()})

def advat(a, th):
    if a['t2'] is not None and th > a['t2']: return a['D']
    if a['t1'] is not None and th > a['t1']: return 0
    if a['t1'] is None and a['t2'] is not None: return 0
    return a['T']

n = 4000
raw = rng.standard_normal((n, 3))
atoms = []
for g in raw:
    g = tuple(float(x) for x in g)
    atoms.append(atom(g)); atoms.append(atom((g[1], g[0], g[2])))
W = 1.0 / len(atoms)
def Phi(model):            # model: list of advice per atom
    return W * sum(a['f'][x] for a, x in zip(atoms, model))
def member(th): return [advat(atoms[i - (i % 2)], th) for i in range(len(atoms))]
lam = lambda th: np.array([(2+th)/6, (2+th)/6, (2-2*th)/6])

ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name); ok &= bool(cond)

grid = [k/60 for k in range(61)]
P = {th: Phi(member(th)) for th in grid}
chk("T1 Phi_1 = Phi_2 along the curve (max dev %.2e)" % max(abs(P[t][0]-P[t][1]) for t in grid),
    all(abs(P[t][0]-P[t][1]) < 1e-9 for t in grid))
chk("T2 Phi_1+Phi_2 non-increasing, Phi_3 non-decreasing",
    all(P[grid[i+1]][0]+P[grid[i+1]][1] <= P[grid[i]][0]+P[grid[i]][1]+1e-12 and P[grid[i+1]][2] >= P[grid[i]][2]-1e-12 for i in range(60)))

# events after s: groups of atoms switching at the same time
events = {}
for i in range(0, len(atoms), 2):
    a = atoms[i]
    for t in (a['t1'], a['t2']):
        if t is not None: events.setdefault(t, []).extend([i, i+1])
evt = sorted(events)

def repair(s, target1, model_s):
    """walk the curve from s; find theta' and fractional split with Phi_1 = target1; return (theta', Phi)."""
    th, cur = s, list(model_s)
    ph = Phi(cur)
    if ph[0] <= target1 + 1e-15: return s, ph, cur, None
    for t in evt:
        if t <= s: continue
        grp = events[t]
        new = list(cur)
        for i in grp: new[i] = advat(atoms[i - (i % 2)], t + 1e-13)
        d = W * sum(atoms[i]['f'][new[i]] - atoms[i]['f'][cur[i]] for i in grp)
        if ph[0] + d[0] <= target1:
            rho = (target1 - ph[0]) / d[0]
            return t, ph + rho * d, new, (grp, rho)
        cur, ph = new, ph + d
    return None

fails, worst, n3, silent_part = 0, 1e9, 0, True
srcs = [k/12 for k in range(12)]
for s in srcs:
    Cs = member(s); Ps = Phi(Cs)
    E0 = [i for i, a in enumerate(atoms) if a['o'] == 3 and Cs[i] == 0]
    tests = []
    for p in (0.05, 0.3, 0.7):
        tests.append([i for i in E0 if random.random() < p])
    thin = sorted(E0, key=lambda i: atoms[i]['t2'])[:5]
    tests += [thin, E0]
    for E in tests:
        if not E: continue
        Y = list(Cs)
        for i in E:
            a = atoms[i]; Y[i] = 1 if a['g'][0] > 0 else -1
        PY = Phi(Y)
        res = repair(s, PY[0], Cs)
        n3 += 1
        if res is None: fails += 1; continue
        tp, Pr, newm, split = res
        gap = PY[2] - Pr[2]
        worst = min(worst, gap)
        if not (abs(Pr[0]-PY[0]) < 1e-12 and abs(Pr[1]-PY[1]) < 1e-12 and gap > 0): fails += 1
        silent_part &= any(atoms[i]['t2'] > tp for i in E) or (split is not None and any(i in split[0] for i in E))
chk("T3 %d class-3 fills of 12 sources: repair ties at 1,2 and is strictly better at 3 (min margin %.2e)" % (n3, worst), fails == 0)
chk("T3' every repair is silent on part of its fill set", silent_part)

fails4, n4, inrange = 0, 0, True
for (a_, b_) in [(0.0, 1/3), (0.05, 0.6), (0.2, 0.9), (1/3, 2/3), (0.5, 0.95)]:
    Ca, Cb = member(a_), member(b_)
    diff = [i for i in range(0, len(atoms), 2) if Ca[i] != Cb[i]]
    for p in (0.1, 0.5, 0.9):
        H = [i for i in diff if random.random() < p]
        H = H + [i + 1 for i in H]                 # mirror atoms: swap-closed H
        Z = list(Ca)
        for i in H: Z[i] = Cb[i]
        PZ = Phi(Z); n4 += 1
        res = repair(a_, PZ[0], Ca)
        if res is None: fails4 += 1; continue
        tp, Pr, _, _ = res
        inrange &= a_ <= tp <= b_ + 1e-12
        if not (abs(Pr[1]-PZ[1]) < 1e-12 and Pr[2] < PZ[2]): fails4 += 1
chk("T4 %d swap-invariant splices dominated by a member between the two sources" % n4, fails4 == 0 and inrange)

# T5 illustration: class-1 fills and one-sided splices are dominated by no grid member
fine = [k/600 for k in range(601)]
PF = [Phi(member(t)) for t in fine]
cnt5, dom5 = 0, 0
for s in (0.1, 0.4, 0.8):
    Cs = member(s)
    Q1 = [i for i, a in enumerate(atoms) if a['o'] == 1 and Cs[i] == 0]
    for p in (0.1, 0.5):
        Y = list(Cs)
        for i in Q1:
            if random.random() < p:
                Y[i] = 1 if atoms[i]['g'][1] > 0 else -1
        PY = Phi(Y); cnt5 += 1
        dom5 += any(all(PF[k][w] <= PY[w] for w in range(3)) for k in range(601))
for (a_, b_) in [(0.0, 1/3), (0.2, 0.9)]:
    Ca, Cb = member(a_), member(b_)
    H = [i for i in range(len(atoms)) if Ca[i] != Cb[i] and atoms[i]['o'] == 1]
    Z = list(Ca)
    for i in H: Z[i] = Cb[i]
    PZ = Phi(Z); cnt5 += 1
    dom5 += any(all(PF[k][w] <= PZ[w] for w in range(3)) for k in range(601))
chk("T5 (illustration) %d class-1 fills / one-sided splices: dominated by no member on a 1/600 grid" % cnt5, dom5 == 0)
print("ALL PASS" if ok else "SOME FAIL")
