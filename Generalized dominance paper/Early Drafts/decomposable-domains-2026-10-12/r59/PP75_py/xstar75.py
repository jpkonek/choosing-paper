"""The j-ideal H-model X*_j (accept h on R iff h_j > 0; common advice off R) for a finite (2V)
family S (u and its six single shifts by 21/20), j = 3.
(a) every member of S, and every coherent model in H tested, fails N1 (X*_j >=_j it pointwise);
(b) X*_j is incoherent: explicit accepted points a, b whose positive combination is silent
    (on an open set);
(c) escape: posterior models beyond the neighbourhood, C_{(1,1,t)} (t >= 6/5) and C_{(1,1,t)}
    composed with small generic moves, pass N1, N2 and N3 with all copies for committed T."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import itertools
from geo75 import *

U = (F(1), F(1), F(1)); s = F(21, 20)
S = [U] + [tuple(s if i == k else F(1) for i in range(3)) for k in range(3)] \
        + [tuple(1 / s if i == k else F(1) for i in range(3)) for k in range(3)]
J = 2   # world 3

def in_R(h):
    return len(set(answer(m, h) for m in S)) > 1

def xstar(h):
    if in_R(h):
        return 'h' if h[J] > 0 else 'S'
    return answer(U, h)

# (a)
cs = cells(S)
atomsS = []
for ci, c in enumerate(cs):
    h = c['pt']
    v = {'X': xstar(h)}
    for i, m in enumerate(S): v['S%d' % i] = answer(m, h)
    atomsS.append({'cell': ci, 'h': h, 'vals': v})
ok_a = True
for i in range(len(S)):
    st = guidance_status(atomsS, 'X', 'S%d' % i, J)
    n1 = N1(atomsS, 'X', 'S%d' % i)[0]
    print('member', S[i], 'status of X* vs member at world 3:', st, '| N1 holds:', n1)
    if st != '>' or n1: ok_a = False
# (b) incoherence certificate
acc = [c['pt'] for c in cs if xstar(c['pt']) == 'h']
found = None
for a, b in itertools.combinations(acc, 2):
    for lam in (F(1, 4), F(1, 2), F(3, 4)):
        p = tuple(lam * a[i] + (1 - lam) * b[i] for i in range(3))
        if 0 in p: continue
        try:
            if xstar(p) == 'S':
                found = (a, b, lam, p); break
        except AssertionError:
            continue
    if found: break
print('incoherence certificate (a, b, lambda, silent combination):', found)
ok_b = found is not None
# (c) escape candidates
ok_c = True
for t in (F(6, 5), F(3, 2), F(2), F(4)):
    for pert in [(1, 1, 1), (F(101, 100), 1, 1), (1, F(101, 100), 1)]:
        Bm = tuple(F(pert[i]) * (t if i == J else F(1)) for i in range(3))
        cs2 = cells(S + [Bm])
        atoms = []
        for ci, c in enumerate(cs2):
            h = c['pt']
            atoms.append({'cell': ci, 'h': h, 'vals': {'X': xstar(h), 'T': answer(U, h), 'B': answer(Bm, h)}})
        rep = candidate_check(atoms, ['T'])
        outside = any(answer(Bm, a['h']) != answer(U, a['h']) and not in_R(a['h']) for a in atoms)
        print('B = C_%s: changes T outside R: %s | N1 %s N2 %s N3(T) %s -> candidate %s'
              % (tuple(str(x) for x in Bm), outside, rep['N1w'], rep['N2']['T'][0], rep['N3']['T'], rep['ok']))
        if not rep['ok']: ok_c = False
print('ALL PASS' if (ok_a and ok_b and ok_c) else 'FAIL', ok_a, ok_b, ok_c)
