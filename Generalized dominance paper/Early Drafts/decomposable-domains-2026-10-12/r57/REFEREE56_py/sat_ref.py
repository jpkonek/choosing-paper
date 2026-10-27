"""sat_ref (REFEREE56): independent SAT re-derivation of PP68 §4 (Lemma 4.1, Lemma 4.2, Thm 4.3) and of the
path obstruction's (IB)+protection+(C) step, with a minimal encoding written from scratch (no lib68).

Encoded axiom instances ONLY (each is valid in the full measurable domain, so UNSAT transfers):
  weak/strict (G) for every ordered pair of the sub-universe (cells are non-null; different advice on a
  mixed cell always has different rank at every world);
  (IB): one Boolean per (record, world), a record being the tuple of (cell, old, new) on the support;
  (TC): for every ordered triple and world, X<=Y & Y<=Z & Z<=X  =>  the three reverses;
  defence of each SELECTED model on its support, against every other model of the sub-universe.
No protection, no direct (C) and no coherence declarations are used, except in test P (stated there).
Solver: Glucose4 (PP68 used CaDiCaL).
Run: python3 -I -B sat_ref.py > sat_ref.out
"""
import itertools
from pysat.solvers import Glucose4
W = (1, 2, 3)
ok = True
def chk(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)

def rank(c, a, w):
    if a == 'S': return 1
    corr = 'B' if c == w else 'A'
    return 0 if a == corr else 2

class Enc:
    def __init__(self, cells, models):
        self.cells = cells                    # list of (name, odd world)
        self.models = sorted(set(models)); self.v = {}; self.cl = []
    def rec(self, X, Y):
        return tuple((c, x, y) for (c, _), x, y in zip(self.cells, X, Y) if x != y)
    def var(self, r, w):
        return self.v.setdefault((r, w), len(self.v) + 1)
    def lit(self, X, Y, w): return self.var(self.rec(X, Y), w)
    def pw(self, X, Y, w):   # X pointwise no worse than Y at w
        return all(rank(k, x, w) <= rank(k, y, w) for (_, k), x, y in zip(self.cells, X, Y))
    def build(self, selected):
        for X, Y in itertools.permutations(self.models, 2):
            for w in W:
                if self.pw(X, Y, w):
                    self.cl += [[self.lit(X, Y, w)], [-self.lit(Y, X, w)]]
        for X, Y, Z in itertools.permutations(self.models, 3):
            for w in W:
                pre = [-self.lit(X, Y, w), -self.lit(Y, Z, w), -self.lit(Z, X, w)]
                for (P, Q) in ((Y, X), (Z, Y), (X, Z)):
                    self.cl.append(pre + [self.lit(P, Q, w)])
        for S_, supp in selected.items():
            for X in self.models:
                if X != S_: self.cl.append([self.lit(S_, X, w) for w in supp])
        return self
    def sat(self, assume, extra=()):
        s = Glucose4(bootstrap_with=self.cl + [list(c) for c in extra])
        r = s.solve(assumptions=list(assume)); s.delete(); return r

def put(cells, base, **kw):
    names = [c for c, _ in cells]; b = list(base)
    for k, v in kw.items(): b[names.index(k)] = v
    return tuple(b)

# ---------- Lemma 4.1 (agreement trap) ----------
cells = [('F', 3), ('Fp', 3), ('d1', 1), ('d2', 2)]   # F, F' in {Y = N} n Sil(Y) n M3; d1, d2: N != Y
N = ('S', 'S', 'S', 'S'); Y = ('S', 'S', 'B', 'B')
Z = put(cells, N, F='A'); YFp = put(cells, Y, Fp='A'); YFF = put(cells, Y, F='A', Fp='A')
e = Enc(cells, [N, Y, Z, YFp, YFF]).build({})
for w in (1, 2):
    chk('L4.1 w=%d: [Y <= N[F->A]] & [N <= Y[F\'->A]] UNSAT (TC+(G)+(IB) only)' % w,
        not e.sat([e.lit(Y, Z, w), e.lit(N, YFp, w)]))
    chk('L4.1 w=%d controls: each literal alone SAT' % w,
        e.sat([e.lit(Y, Z, w)]) and e.sat([e.lit(N, YFp, w)]))

# ---------- Lemma 4.2 (edge lemma) and (a) ----------
cells = [('F', 3), ('t3', 3), ('x1', 1), ('x2', 2)]
Cm = ('S', 'S', 'S', 'S')                       # C silent on F
for Bm, label in ((('S', 'S', 'B', 'B'), 'B mixed against C'), (('S', 'B', 'S', 'S'), 'B pointwise 3-better than C')):
    Yf = put(cells, Cm, F='A')
    e = Enc(cells, [Cm, Bm, Yf]).build({Cm: W})
    hyp = [e.lit(Bm, Yf, 1), e.lit(Bm, Yf, 2)]
    r1 = not e.sat(hyp + [e.lit(Cm, Bm, 1)]); r2 = not e.sat(hyp + [e.lit(Cm, Bm, 2)])
    r3 = not e.sat(hyp + [-e.lit(Cm, Bm, 3)])
    if label.startswith('B mixed'):
        chk('L4.2 (%s): B ->3 C forces C !<=1 B, C !<=2 B and C <=3 B' % label, r1 and r2 and r3 and e.sat(hyp))
    else:
        chk('L4.2(a) (%s): B ->3 C is UNSAT' % label, not e.sat(hyp))

# ---------- Thm 4.3: 2-cycle and 3-cycle ----------
# cells: P (class 3, all silent), t3 (class 3: T = B, the others S), y1 (class 1: Y = B, others S)
cells = [('P', 3), ('t3', 3), ('y1', 1), ('y2', 2), ('a1', 1)]   # a1: Y gives the 3-correct A (as D_[v3,h12] does)
T = ('S', 'B', 'S', 'S', 'S'); Ns = ('S', 'S', 'S', 'S', 'S'); Yc = ('S', 'S', 'B', 'B', 'A')
fill = lambda X: put(cells, X, P='A')
mods = [T, Ns, Yc, fill(T), fill(Ns), fill(Yc)]
e = Enc(cells, mods).build({T: W, Ns: W, Yc: W})
serve = lambda B, C: [e.lit(B, fill(C), 1), e.lit(B, fill(C), 2)]
h1, h2, h3 = serve(Ns, T), serve(Yc, Ns), serve(T, Yc)
chk('T4.3 3-cycle N* ->3 T, Y ->3 N*, T ->3 Y (T pointwise strictly 3-better than N*): UNSAT',
    not e.sat(h1 + h2 + h3))
chk('T4.3 controls: h1+h2 SAT, h1+h3 SAT; h2+h3 already UNSAT (N* <=3 Y <=3 T closes with the guidance '
    'link T <=3 N*, so h1 is not needed: agrees with PP68 cycle68c.out "H2+H3 UNSAT")',
    e.sat(h1 + h2) and e.sat(h1 + h3) and not e.sat(h2 + h3))
chk('T4.3 2-cycle N* ->3 T ->3 N* UNSAT (T strictly 3-better than N*)', not e.sat(h1 + serve(T, Ns)))
# 2-cycle between two mixed models forces a world-3 tie
cells2 = [('P', 3), ('m1', 1), ('m2', 2), ('n1', 1), ('n2', 2)]
B2 = ('S', 'B', 'B', 'S', 'S'); C2 = ('S', 'S', 'S', 'B', 'B')
f2 = lambda X: put(cells2, X, P='A')
e2 = Enc(cells2, [B2, C2, f2(B2), f2(C2)]).build({B2: W, C2: W})
hh = [e2.lit(B2, f2(C2), 1), e2.lit(B2, f2(C2), 2), e2.lit(C2, f2(B2), 1), e2.lit(C2, f2(B2), 2)]
chk('T4.3 2-cycle of mixed models: SAT, and forces the world-3 tie B ~3 C',
    e2.sat(hh) and not e2.sat(hh + [-e2.lit(B2, C2, 3)]) and not e2.sat(hh + [-e2.lit(C2, B2, 3)]))

# ---------- P: the path obstruction's step (IB) + protection + (C) ----------
# C_s silent on E; C_t = majority A on E; they differ also on a cell u.  Z := C_t[E -> S] has
# rec(Z, C_s) = rec(C_t, X) for X := C_s[E -> A].  If C_t <=_w X at every w then Z <=_w C_s at every w,
# so protection of C_s gives the reverses and (C) would register the incoherent Z.  We encode protection +
# (C) for the single registered model C_s as the clause "not (Z <=_w C_s for all w)" for Z declared
# incoherent (Z differs from the coherent C_t on a bounded non-conic set, Lemma H).
cellsP = [('E', 3), ('u1', 1), ('u2', 2), ('u3', 3)]
Cs = ('S', 'S', 'S', 'S'); Ct = ('A', 'B', 'B', 'B'); X = ('A', 'S', 'S', 'S'); Zp = ('S', 'B', 'B', 'B')
eP = Enc(cellsP, [Cs, Ct, X, Zp]).build({Cs: W, Ct: W})
chk('P  records: rec(C_t, X) == rec(Z, C_s)', eP.rec(Ct, X) == eP.rec(Zp, Cs))
prot = [[-eP.lit(Zp, Cs, w) for w in W]]
chk('P  C_t dominating X (all worlds) is UNSAT with protection+(C) of C_s; SAT without it',
    (not eP.sat([eP.lit(Ct, X, w) for w in W], prot)) and eP.sat([eP.lit(Ct, X, w) for w in W]))
print('ALL PASS' if ok else 'SOME FAIL')
