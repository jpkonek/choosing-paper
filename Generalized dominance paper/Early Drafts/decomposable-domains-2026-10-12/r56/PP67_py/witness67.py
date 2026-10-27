# PP67: (1) exact per-type feasibility of the witness field; (2) an exhaustive finite instance of the witness W.
# Run: python3 -I -B witness67.py > witness67.out
from fractions import Fraction as Fr
import itertools
import numpy as np
ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name); ok &= bool(cond)
nu = Fr(1, 2)
LAM = {'T': (1, 1, 1), 'N': (1, 1, nu), 'D': (1, 1, 0)}
# per-type vectors in the order (w, w', o): a = f(A) - f(S), b = f(B) - f(S); A correct at w, w', wrong at o.
# class M3 (o = world 3): world order (1, 2, 3).  class M1 (o = world 1): stored as (w1, w2, w3) directly.
def vecM3(aw, ao, bw, bo):   # a = (-aw1,-aw2,+ao), b = (+bw1,+bw2,-bo)
    return ((-aw[0], -aw[1], ao), (bw[0], bw[1], -bo))
def vecM1(ao, aw, bo, bw):   # odd world 1: a = (+ao, -aw2, -aw3), b = (-bo, +bw2, +bw3)
    return ((ao, -aw[0], -aw[1]), (-bo, bw[0], bw[1]))
TYPES = {
  ('M3', 'SSA'): vecM3((1, 1), 5, (1, 1), 1),
  ('M3', 'AAA'): vecM3((1, 1), 1, (1, 1), 1),
  ('M3', 'BSA'): vecM3((1, 1), 10, (1, 1), Fr(5, 2)),
  ('M1', 'SSS'): vecM1(3, (1, 1), 1, (2, 1)),
  ('M1', 'SSB'): vecM1(3, (1, 1), Fr(3, 2), (1, 2)),
  ('M1', 'AAA'): vecM1(1, (2, 1), 1, (1, 1)),
  ('M1', 'ASS'): vecM1(3, (1, 3), 1, (2, 1)),
  ('M1', 'ASB'): vecM1(3, (1, 3), Fr(3, 2), (1, 2)),
  ('M1', 'BBB'): vecM1(2, (1, 1), 3, (1, 1)),
}
def swap12(v): return (v[1], v[0], v[2])
for t in [t for t in TYPES if t[0] == 'M1']:          # class M2 = class M1 with worlds 1, 2 exchanged
    a, b = TYPES[t]; TYPES[('M2', t[1])] = (swap12(a), swap12(b))
def argmin(lam, a, b):
    vals = {'S': 0, 'A': sum(l*x for l, x in zip(lam, a)), 'B': sum(l*x for l, x in zip(lam, b))}
    m = min(vals.values()); win = [k for k, v in vals.items() if v == m]
    return win[0] if len(win) == 1 else None
def odd(cl): return {'M1': 0, 'M2': 1, 'M3': 2}[cl]
good = True
for (cl, ty), (a, b) in TYPES.items():
    o = odd(cl)
    # rank monotonicity: at non-odd worlds A < S < B; at the odd world B < S < A (contradictory is put above all)
    for w in range(3):
        good &= (a[w] < 0 < b[w]) if w != o else (b[w] < 0 < a[w])
    for k, M in zip(ty, 'TND'):
        good &= argmin(LAM[M], a, b) == k
chk("per-type field: ranks monotone; T, N, D* are the UNIQUE argmins of lam_T=(1,1,1), lam_N=(1,1,1/2), lam_D=(1,1,0) on all 15 types", good)

# ---------- exhaustive finite instance ----------
# atoms: (class, type, mass, in_E0-label)
W = 40
atoms = [('M3','BSA',W,None), ('M3','SSA',1,'e1'), ('M3','SSA',2,'e2'), ('M3','SSA',1,None),
         ('M1','SSB',1,None), ('M1','ASS',1,None), ('M1','ASB',1,None), ('M1','SSS',1,None),
         ('M2','SSB',1,None), ('M2','ASS',1,None), ('M2','ASB',1,None), ('M2','AAA',1,None)]
n = len(atoms); VAL = 'ASB'
F = np.zeros((n, 3, 3), dtype=float)   # F[atom, value(A,S,B), world]
for i, (cl, ty, m, _) in enumerate(atoms):
    a, b = TYPES[(cl, ty)]
    for w in range(3):
        F[i, 0, w] = m*float(a[w]); F[i, 1, w] = 0.0; F[i, 2, w] = m*float(b[w])
E0 = [i for i, at in enumerate(atoms) if at[3]]
mods = np.array(list(itertools.product(range(3), repeat=n)), dtype=np.int8)   # 3^12 models
Phi = np.zeros((len(mods), 3))
for i in range(n): Phi += F[i, mods[:, i], :]
kap = np.zeros(len(mods))                  # world-3 first key: mass of 3-wrong (A on M3) answers on E0
for i in E0: kap += (mods[:, i] == 0) * atoms[i][2]
def idx(vals): return int(sum(v * 3**(n-1-k) for k, v in enumerate(vals)))
def model(name):
    return [ {'T':0,'N':1,'D':2}[name] and None for _ in range(n)]
def mk(which):
    return [VAL.index(at[1][{'T':0,'N':1,'D':2}[which]]) for at in atoms]
T, N, D = mk('T'), mk('N'), mk('D')
iT, iN, iD = idx(T), idx(N), idx(D)
def leq(i, j, w):      # model i at least as good as model j at world w (loss order; lexicographic key at world 3)
    if w < 2: return Phi[i, w] <= Phi[j, w] + 1e-9
    if kap[i] != kap[j]: return kap[i] < kap[j]
    return Phi[i, 2] <= Phi[j, 2] + 1e-9
def leq_all(i, w):     # vector over all models: model i <=_w each model
    if w < 2: return Phi[i, w] <= Phi[:, w] + 1e-9
    return (kap[i] < kap) | ((kap[i] == kap) & (Phi[i, 2] <= Phi[:, 2] + 1e-9))
def geq_all(i, w):     # each model <=_w model i
    if w < 2: return Phi[:, w] <= Phi[i, w] + 1e-9
    return (kap < kap[i]) | ((kap == kap[i]) & (Phi[:, 2] <= Phi[i, 2] + 1e-9))
for nm, i, supp in (('T', iT, (0,1,2)), ('N', iN, (0,1,2)), ('D*', iD, (0,1))):
    dom = np.ones(len(mods), bool)
    for w in supp: dom &= geq_all(i, w)
    dom &= ~(np.arange(len(mods)) == i)
    chk("%s: no other model is <= it at every world of its support (unique Bayes => protection, direct (C))" % nm, not dom.any())
    if nm == 'D*':
        d3 = geq_all(i, 0) & geq_all(i, 1) & geq_all(i, 2); d3[i] = False
        chk("D*: no other model <= it at all three worlds", not d3.any())
    defd = np.zeros(len(mods), bool)
    for w in supp: defd |= leq_all(i, w)
    chk("%s: defended against all %d models at a world of its support" % (nm, len(mods)), defd.all())
def X(Es):   # T filled with A on the listed E0 atoms
    v = list(T)
    for i in Es: v[i] = 0
    return idx(v)
def Y(Es):
    v = list(N)
    for i in Es: v[i] = 0
    return idx(v)
Efam = [[E0[0]], [E0[1]], E0]
c = True
for Es in Efam:
    x, y = X(Es), Y(Es)
    c &= all(leq(iN, x, w) for w in range(3))                       # N dominates X_E (weakly) ...
    c &= not leq(x, iN, 2)                                          # ... strictly at 3
    c &= leq(iD, x, 0) and leq(iD, x, 1) and not leq(iD, x, 2)      # edge pattern
    c &= not leq(iT, x, 0) and not leq(iT, x, 1) and leq(iT, x, 2)  # guidance at T
    c &= leq(iD, y, 0) and leq(iD, y, 1)                            # D* defends against N's fills at 1, 2
    c &= not leq(iN, y, 0) and not leq(iN, y, 1) and leq(iN, y, 2)  # N's fills: guidance
    c &= not leq(iT, y, 0) and not leq(iT, y, 1)                    # T cannot dominate N's fills
for Es in Efam[:2]:
    x = X(Es)
    c &= not leq(x, iN, 0) and not leq(x, iN, 1)                     # forced (E0 \ E non-null)
    c &= not leq(x, iD, 0) and not leq(x, iD, 1) and leq(x, iD, 2)   # PP65 Prop 2.3(c)
c &= all(leq(iN, iT, w) and leq(iD, iT, w) and leq(iD, iN, w) for w in (0, 1))
c &= not leq(iT, iN, 0) and not leq(iT, iN, 1) and leq(iT, iN, 2) and not leq(iN, iT, 2)
c &= not leq(iT, iD, 0) and not leq(iT, iD, 1) and leq(iT, iD, 2) and not leq(iD, iN, 2)
chk("all module commitments and the listed forced literals hold in W (E = e1, e2, e1 u e2)", c)
# (G) on a random sample of pairs, at every world (strict)
rng = np.random.default_rng(67); g_ok = True
rank = {0: {0: 0, 1: 1, 2: 2}, 2: {0: 2, 1: 1, 2: 0}}   # value A,S,B -> rank at a non-odd world / at the odd world
def rk(i, val, w): return rank[2 if w == odd(atoms[i][0]) else 0][val]
for _ in range(20000):
    i, j = rng.integers(len(mods), size=2)
    for w in range(3):
        ri = [rk(k, mods[i, k], w) for k in range(n)]; rj = [rk(k, mods[j, k], w) for k in range(n)]
        if all(p <= q for p, q in zip(ri, rj)):
            g_ok &= leq(i, j, w)
            if ri != rj: g_ok &= not leq(j, i, w)
chk("strict (G) on 20,000 random pairs at every world", g_ok)
print("ALL PASS" if ok else "SOME FAIL")
