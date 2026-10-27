"""defeat77: refinement of PP79's pigeonhole (D1).  PP77 Prop 6.1: same-ray dominations d_a (S_a splice,
scale tau_a) and d_b (S_b splice, scale tau_b), tau_a < tau_b, jointly defeat B via the reversion rival
B[(F_a \\ L(tau_a)) u (F_b \\ L(tau_b)) -> T] iff F_a n (L(tau_b) \\ L(tau_a)) is null.  So DISJOINT SCALES ARE
NOT ENOUGH; scale tau_a must be a right-increase point of F_a.  Exact cells; defeat search = PP79 defeat79."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP79_py'))
from lib79 import *
from defeat79 import defeated, admissible
from mixed79 import T, B, r

def run():
    sa, sb = F(41, 42), F(27, 28)          # index (1,1,s): s_a > s_b  <=>  tau_a < tau_b
    At = atoms({'T': T, 'B': B, 'Ba': post((1, 1, sa)), 'Bb': post((1, 1, sb))})
    Ba = [a['vals']['Ba'] for a in At]; Bb = [a['vals']['Bb'] for a in At]
    def X_of(fam, gap):
        X = []
        for a in At:
            t, b = a['vals']['T'], a['vals']['B']
            if t == b: X.append(t); continue
            o = a['o']; inLa = a['vals']['Ba'] != t; inLb = a['vals']['Bb'] != t
            if fam == 'a':
                if o in (0, 2): inS = True
                elif gap: inS = (inLa or not inLb) and a['half'] == 0   # F_a avoids L(tau_b) minus L(tau_a)
                else: inS = a['half'] == 0
            else:
                inS = (o in (1, 2)) or a['half'] == 0
            X.append(b if inS else t)
        return X
    for gap in (False, True):
        Xa, Xb = X_of('a', gap), X_of('b', False)
        adm = (admissible(At, Ba, Xa), admissible(At, Bb, Xb))
        w = defeated(At, 'B', [(Ba, Xa), (Bb, Xb)])
        print('F_a avoids the shell L(tau_b)\\L(tau_a): %-5s admissible=%s  B defeated: %s' % (gap, adm, w))
    print('expected: defeated only when F_a avoids the shell (Prop 6.1)')

run()
