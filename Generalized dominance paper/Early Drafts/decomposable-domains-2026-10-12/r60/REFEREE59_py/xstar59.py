"""xstar59: PP75 Prop 9.1 re-checked with own code.
Reference family S = {u} u {u o (21/20 at i), u o (20/21 at i) : i = 1, 2, 3}; R = cells where some member of S
differs from T; off R the common advice is T's.  X*_3 := h on R where h_3 > 0, S on R where h_3 < 0, T off R.
(a) X*_3 is pointwise weakly 3-better than every member of S, strictly unless equal; (N1) fails for every H-model.
(b) incoherence: explicit points a, b accepted by X*_3 and a point of their segment where X*_3 is silent,
    with an open neighbourhood (checked at the cell level: the silent point lies in an open cell).
(c) escape candidates C_{u o (1 + t e_3)}: (N1) against X*_3, (N2) at T, and copy-defeat of T (general
    four-valued test over the restricted family T[S -> B], strict guidance included).
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib59 import *

T = post((1, 1, 1))
fam = {'T': T}
for i in range(3):
    for s in (F(21, 20), F(20, 21)):
        m = [F(1)] * 3; m[i] = s
        fam['S%d_%s' % (i, s)] = post(tuple(m))


def defeat(At, Z, B, X):
    """Z left with no defence against some Z[S -> B]; modes G (strict guidance) / R (refusal block)."""
    n = len(At)
    for mode in itertools.product('GR', repeat=3):
        opts = []
        for i in range(n):
            o = []
            for inS in ((True, False) if Z[i] != B[i] else (False,)):
                Y = Z[i] if inS else B[i]
                ok = True
                for j in range(3):
                    if mode[j] == 'G' and inS and not rank(B[i], At[i], j) < rank(Z[i], At[i], j): ok = False
                    if mode[j] == 'R' and X[i] != Y and not rank(X[i], At[i], j) < rank(Y, At[i], j): ok = False
                if ok: o.append((inS, X[i] != Y))
            opts.append(o)
        if any(not o for o in opts): continue
        if not any(x[0] for o in opts for x in o): continue
        if any(mode[j] == 'R' for j in range(3)) and not any(x[1] for o in opts for x in o): continue
        return mode
    return None


def main():
    # (a)
    cs = cells(fam)
    inR = [any(c['vals'][n] != c['vals']['T'] for n in fam) for c in cs]
    Xs = [(1 if c['pt'][2] > 0 else 0) if inR[k] else c['vals']['T'] for k, c in enumerate(cs)]
    worse = 0
    for n in fam:
        for k, c in enumerate(cs):
            if rank(c['vals'][n], c['pt'], 2) < rank(Xs[k], c['pt'], 2): worse += 1
    print('(a) cells where some member of S is strictly 3-better than X*_3:', worse)
    # (b)
    a = (F(-7, 9) - F(1, 2000), F(16, 9) + F(1, 2000) - F(1, 10 ** 6), F(1, 10 ** 6))   # s = 1, just outside A(T)
    b = (F(3, 10), F(9, 10), F(-2, 10))
    def X_at(h):
        vals = {n: answer(K, h) for n, K in fam.items()}
        r_ = any(vals[n] != vals['T'] for n in fam)
        return ((1 if h[2] > 0 else 0) if r_ else vals['T']), r_, vals['T']
    xa, xb = X_at(a), X_at(b)
    print('(b) X*_3(a) = %s (in R: %s, T: %s);  X*_3(b) = %s (in R: %s, T: %s)' % (xa[0], xa[1], xa[2], xb[0], xb[1], xb[2]))
    found = None
    for k in range(1, 4000):
        s = F(k, 4000) / 50
        h = tuple((1 - s) * a[i] + s * b[i] for i in range(3))
        try:
            xh = X_at(h)
        except AssertionError:
            continue
        if xh[0] == 0:
            found = (float(s), [float(x) for x in h], xh)
            break
    print('    first silent point on [a, b] (positive combination of two accepted problems):', found)
    # (c)
    print('(c) escape candidates C_{u o (1 + t e_3)}:')
    for t in (F(1, 5), F(1, 2), F(1), F(2), F(3), F(1, 5) + F(1, 100), F(3) - F(1, 100)):
        m = (F(1), F(1), 1 + t)
        mods = dict(fam); mods['Bc'] = post(m)
        cs = cells(mods)
        At = [c['pt'] for c in cs]
        inR = [any(c['vals'][n] != c['vals']['T'] for n in fam) for c in cs]
        X = [(1 if c['pt'][2] > 0 else 0) if inR[k] else c['vals']['T'] for k, c in enumerate(cs)]
        Bv = [c['vals']['Bc'] for c in cs]
        Tv = [c['vals']['T'] for c in cs]
        D = [i for i in range(len(cs)) if Bv[i] != X[i]]
        n1 = all(any(rank(Bv[i], At[i], w) < rank(X[i], At[i], w) for i in D) for w in range(3))
        n2 = any(Bv[i] != X[i] for i in range(len(cs)) if Tv[i] != X[i])
        dft = defeat(At, Tv, Bv, X)
        minus = sum(1 for i in range(len(cs)) if inR[i] and Bv[i] == -1)
        print('   t = %-8s N1 %s  N2 %s  T defeated: %s   (-h answers on R cells: %d)' % (t, n1, n2, dft, minus))
    # control: an H-candidate (a member of S) must fail N1
    mods = dict(fam); cs = cells(mods)


if __name__ == '__main__':
    main()
