"""PP63 s.6.5: an exact counterexample to openness for R0 inside PP62's own module N = N_u u N_B.

a := u o (1 - s e_2) (normalised), s = 1/100: an interior point of the lobe N_u (PP62 Lemma 3.1; see note).
Claim: C_a has a balanced member swap with B, i.e. the {a, B} arrangement has non-null cells of BOTH kinds
  Ep-type: odd world 1, Wr = {1}, C_a answers, C_B silent  (silencing improves world 1: c_1 > 0)
  Em-type: odd world 1, Cor = {1}, C_a answers, C_B silent (silencing worsens world 1: c_1 < 0)
and world 1 is the strictly middle coordinate of log(B/a) (PP62 Cor 1.2).
Then F = F+ u F- (equal |g|-mass, non-conic) has V(F : a -> B) = 0, X := C_a[F -> C_B] is a null rival of a,
and PP63 Prop 6.1 gives a non-closed section at a for X at w0 = 2 (a o (1 + t e_2) stays in N_u for t < s).
Also: u itself is not interior to N_u (pure +e_2 shifts of u lower Phi_2 and leave N_u) -- proved in the note.
Exact cells: PP51 enumerator (PP57_py/post51.py, unchanged).
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP57_py'))
from fractions import Fraction as Fr
from post51 import cells, advice

EPS = Fr(3, 10)
U = (Fr(1, 3),) * 3
B = (Fr(406, 1200), Fr(421, 1200), Fr(373, 1200))


def norm(a):
    s = sum(a)
    return tuple(x / s for x in a)


ok = True
for s in (Fr(1, 100), Fr(1, 1000)):
    a = norm((U[0], U[1] * (1 - s), U[2]))
    c = (1 - EPS) / 3
    for p in (a, B):            # (2V): u in M_p
        inv = [1 / x for x in p]
        ok &= min(x / sum(inv) for x in inv) >= c
    d = [math.log(B[i] / a[i]) for i in range(3)]
    order = sorted(range(3), key=lambda i: d[i])
    middle = order[1]
    kinds = {'Ep': 0, 'Em': 0}
    for g in cells(EPS, [a, B]):
        xa, xb = advice(EPS, a, g), advice(EPS, B, g)
        assert xa in (0, 1) and xb in (0, 1)
        if not (xa == 1 and xb == 0):
            continue
        cor = [w for w in range(3) if g[w] > 0]
        wr = [w for w in range(3) if g[w] < 0]
        if wr == [0]:
            kinds['Ep'] += 1
        if cor == [0]:
            kinds['Em'] += 1
    print(f's = {s}: a = {[str(x) for x in a]}; log(B/a) = {[round(x, 5) for x in d]}, middle world = {middle + 1}; '
          f'cells (a answers, B silent): Ep-type {kinds["Ep"]}, Em-type {kinds["Em"]}')
    ok &= middle == 0 and kinds['Ep'] > 0 and kinds['Em'] > 0
print('balanced member swaps between the interior lobe point a and B exist (both orientations, middle world 1):', ok)
print('ALL PASS' if ok else 'SOME FAIL')
