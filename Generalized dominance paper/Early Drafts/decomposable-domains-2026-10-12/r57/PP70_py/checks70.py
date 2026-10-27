"""checks70: SAT checks of PP70 §1 lemmas on abstract cell instances (lib70; sub-universe principle).
K1 direction lemma, class 1: a model 3-worse than C cannot dominate (at 2,3) a class-1 fill of C.  UNSAT
K2 one model cannot serve a class-1 and a class-2 fill of the same interior source.              UNSAT
K3 two-band splice: R_a cannot dominate Z_H, H = L_a u (L_x \\ L_a'), a < a' < x.                  UNSAT
   control: same instance without the commitment                                                  SAT
K4 generalised trap transferred to a later member C_t that is A on the fill set:
   r1@1 alone SAT, r2@2 alone SAT, both UNSAT; r_w is carried by the source C_s.
K5 Kill-A: C_s <=_1 C_t and C_s <=_2 C_t jointly UNSAT when C_t gains A on Sil(C_s) in class 3; each alone SAT.
K6 edge model D with C <=_1 D and C <=_2 D is undefended against a class-3 fill of C (Prop 2.2).   UNSAT
K7 a member record refused at 1 and 2 has no selected edge carrier (Prop 2.3).                    UNSAT
Run: python3 -I -B checks70.py > checks70.out
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib70 import Inst, W

ok = True


def rep(name, got, want):
    global ok
    good = (got == want)
    ok &= good
    print('%-62s %-5s (expected %s) %s' % (name, 'SAT' if got else 'UNSAT', 'SAT' if want else 'UNSAT',
                                           'ok' if good else 'FAIL'))


# ---------- K1, K2: source C silent on bands; later model B answers 3-wrong on bands
cells = [('f1', 1), ('f2', 2), ('b1', 1), ('b2', 2), ('b3', 3)]
I = Inst(cells, [])
C = I.m(f1='S', f2='S', b1='S', b2='S', b3='S')
B = I.m(C, b1='B', b2='B', b3='A')                     # later member: 3-worse than C
Y1 = I.m(C, f1='A')                                     # class-1 fill
Y2 = I.m(C, f2='A')                                     # class-2 fill
I = Inst(cells, [C, B, Y1, Y2]).build({C: W, B: W}, [C, B], {Y1, Y2})
rep('K1 later B dominates class-1 fill of C (worlds 2,3)', I.sat([I.L(B, Y1, 2), I.L(B, Y1, 3)]), False)
Bx = I.m(C, b1='B', b2='B', b3='B')                     # an arbitrary model: mixed against C at every world
I2 = Inst(cells, [C, Bx, Y1, Y2]).build({C: W, Bx: W}, [C, Bx], {Y1, Y2})
rep('K2 one model serves class-1 fill (2,3) and class-2 fill (1,3)',
    I2.sat([I2.L(Bx, Y1, 2), I2.L(Bx, Y1, 3), I2.L(Bx, Y2, 1), I2.L(Bx, Y2, 3)]), False)
rep('K2 control: class-1 fill only', I2.sat([I2.L(Bx, Y1, 2), I2.L(Bx, Y1, 3)]), True)

# ---------- K3: splices between T and N, four sigma-bands, three class parts each
cells = []
for b in range(1, 5):
    cells += [('rb%d' % b, 3), ('l1_%d' % b, 1), ('l2_%d' % b, 2)]
Tv = {('rb', 3): 'B', ('l1_', 1): 'A', ('l2_', 2): 'A'}


def Rcut(k):           # silent on bands 1..k (L_alpha for the k-th cut), T's answer elsewhere
    d = {}
    for b in range(1, 5):
        d['rb%d' % b] = 'S' if b <= k else 'B'
        d['l1_%d' % b] = 'S' if b <= k else 'A'
        d['l2_%d' % b] = 'S' if b <= k else 'A'
    return tuple(d[c] for c, _ in cells)


T, Ra, Rap, Rx, N = Rcut(0), Rcut(1), Rcut(2), Rcut(3), Rcut(4)
Zd = {}
for b in range(1, 5):
    sil = b in (1, 3)
    Zd['rb%d' % b] = 'S' if sil else 'B'
    Zd['l1_%d' % b] = 'S' if sil else 'A'
    Zd['l2_%d' % b] = 'S' if sil else 'A'
ZH = tuple(Zd[c] for c, _ in cells)
I3 = Inst(cells, [T, Ra, Rap, Rx, N, ZH]).build({M: W for M in (T, Ra, Rap, Rx, N)}, [T, Ra, Rap, Rx, N], {ZH})
rep('K3 control: five members, two-band splice, no commitment', I3.sat(), True)
rep('K3 R_a dominates Z_H, H = L_a u (L_x minus L_a\')', I3.sat([I3.L(Ra, ZH, w) for w in W]), False)
print('    record identity rec(R_a,Z_H) == rec(R_a\',R_x):', I3.rec(Ra, ZH) == I3.rec(Rap, Rx))

# ---------- K4: generalised trap at a later member that answers A on the fill set
cells = [('e', 3), ('m3', 3), ('m1a', 1), ('m1b', 1), ('m2a', 2), ('m2b', 2)]
I = Inst(cells, [])
Cs = I.m(e='S', m3='S', m1a='S', m1b='S', m2a='S', m2b='S')
Ct = I.m(e='A', m3='A', m1a='B', m1b='B', m2a='B', m2b='B')
Y = I.m(Cs, e='A')
Z1 = I.m(Cs, e='A', m2a='B')            # G_1 = E u m2a  (C_t strictly 1-worse on m2a)
Z2 = I.m(Cs, e='A', m1a='B')            # G_2 = E u m1a
S1c = I.m(Cs, m3='A', m1a='B', m1b='B', m2b='B')    # C_s (+) r_1 : C_s carries r_1
S2c = I.m(Cs, m3='A', m1b='B', m2a='B', m2b='B')
I4 = Inst(cells, [Cs, Ct, Y, Z1, Z2, S1c, S2c]).build({Cs: W, Ct: W}, [Cs, Ct], {Y, Z1, Z2})
r1, r2 = I4.L(Z1, Ct, 1), I4.L(Z2, Ct, 2)
print('    carriers: rec(C_s, C_s+r_1) == rec(Z_1, C_t):', I4.rec(Cs, S1c) == I4.rec(Z1, Ct),
      '; rec(C_s, C_s+r_2) == rec(Z_2, C_t):', I4.rec(Cs, S2c) == I4.rec(Z2, Ct))
print('    r_1 mixed at 1 and 2:', I4.gstat(I4.rec(Z1, Ct), 1) == 0 and I4.gstat(I4.rec(Z1, Ct), 2) == 0,
      '; C_t refuses Y at 3 by strict (G):', I4.gstat(I4.rec(Ct, Y), 3) == -1)
rep('K4 base', I4.sat(), True)
rep('K4 r_1 accepted at 1', I4.sat([r1]), True)
rep('K4 r_2 accepted at 2', I4.sat([r2]), True)
rep('K4 r_1 at 1 and r_2 at 2 (C_t undefended against Y)', I4.sat([r1, r2]), False)

# ---------- K5: Kill-A
I5 = Inst(cells, [Cs, Ct, Y]).build({Cs: W, Ct: W}, [Cs, Ct], {Y})
rep('K5 C_s <=_1 C_t alone', I5.sat([I5.L(Cs, Ct, 1)]), True)
rep('K5 C_s <=_2 C_t alone', I5.sat([I5.L(Cs, Ct, 2)]), True)
rep('K5 C_s <=_1 C_t and C_s <=_2 C_t', I5.sat([I5.L(Cs, Ct, 1), I5.L(Cs, Ct, 2)]), False)

# ---------- K6: an open-edge model D (support {1,2}) is undefended against a class-3 fill of C
#            once C <=_1 D and C <=_2 D are both accepted (signed propagation, any source C)
cells = [('e', 3), ('q', 3), ('b1', 1), ('b2', 2)]
I = Inst(cells, [])
C = I.m(e='S', q='S', b1='S', b2='S')
D = I.m(e='A', q='A', b1='B', b2='B')         # edge-type model, A on class 3, mixed against C at 1 and 2
Yf = I.m(C, e='A')
I6 = Inst(cells, [C, D, Yf]).build({C: W, D: (1, 2)}, [C, D], {Yf})
rep('K6 C <=_1 D alone', I6.sat([I6.L(C, D, 1)]), True)
rep('K6 C <=_1 D and C <=_2 D (D undefended against the fill)', I6.sat([I6.L(C, D, 1), I6.L(C, D, 2)]), False)

# ---------- K7: a record out of a member refused at 1 and 2 bans every edge carrier (IB + competitiveness)
cells = [('p1', 1), ('p2', 2), ('x', 3)]
I = Inst(cells, [])
L0 = I.m(p1='S', p2='S', x='S')
L0P = I.m(L0, p1='B', p2='B')
DK = I.m(p1='S', p2='S', x='A')              # wide edge model: silent on both band parts
DKP = I.m(DK, p1='B', p2='B')
I7 = Inst(cells, [L0, L0P, DK, DKP]).build({L0: W, DK: (1, 2)}, [L0, DK], set())
print('    rec(L0, L0[P->B]) == rec(D_K, D_K[P->B]):', I7.rec(L0, L0P) == I7.rec(DK, DKP))
rep('K7 control: no commitment', I7.sat(), True)
rep('K7 L0 refuses L0[P->B] at 1 and 2 (W-row) with D_K selected on the edge',
    I7.sat([-I7.L(L0, L0P, 1), -I7.L(L0, L0P, 2)]), False)
print('ALL PASS' if ok else 'SOME FAIL')
