import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hlib76 import *
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_t1_76.py')).read().split('random.seed(76)')[0].replace('if __name__ != "__main__": raise SystemExit', ''))
n = 3; allm = models(n); cnt = 0
for O in itertools.product(range(3), repeat=n):
    for B in allm:
        for X in allm:
            if B == X: continue
            for w in range(3):
                refs = coupled_refusals(O, B, X, w, allm)
                for C in allm:
                    brute = {apply(C, r) for r in refs if carries(C, r)}
                    f = formula(O, B, X, C, w)
                    if brute != f:
                        print('O', O, 'B', B, 'X', X, 'C', C, 'w', w, 'brute-f', brute - f, 'f-brute', f - brute); cnt += 1
                        if cnt > 5: raise SystemExit
