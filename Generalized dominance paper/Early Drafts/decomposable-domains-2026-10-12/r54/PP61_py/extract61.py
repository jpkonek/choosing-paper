"""PP61: extract the allocation pattern of a saved SAT solution (E2_<label>.pkl) on the balanced swaps.

For each balanced swap X = C_a[F -> C_b] (and its copy Y = C_b[F -> C_a]):
  R(r)  with r  = rec(C_a -> X)   (= rec(Y -> C_b))
  R(r-) with r- = rec(X -> C_a)   (= rec(C_b -> Y))
  for each pure shift (a, e_w): R(rec(C_{a_t} -> X));  for each shift (b, e_w): R(rec(C_{b_t} -> Y)).
Also counts, over ALL base records with a selected old side, the worlds of single-world incomparability
(both directions refused) and single-world ties (both accepted).
"""
import sys, os, pickle
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from collections import Counter
from geom61 import sig
from run61b import get, bal_swaps


def R(enc, val, r):
    return ''.join(str(i + 1) for i in range(3) if not val[enc.v(r, i)]) or '-'


def main(label='G3', fn='E2'):
    inst, kinds, enc = get(label)
    with open(os.path.join(HERE, '%s_%s.pkl' % (fn, label)), 'rb') as f:
        val = pickle.load(f)
    names, M = enc.mat['base']
    rows = Counter()
    for (n, a, b, F) in bal_swaps(inst, kinds):
        ia, ix = names.index('S:' + a), names.index(n)
        r, rb = M[ia, ix], M[ix, ia]
        sg = '+'.join(sorted(sig(inst.atoms[p].ray) for p in F))
        sh = []
        for w in range(3):
            S = inst.subs[(a, w)]
            nm, Ms = enc.mat[(a, w)]
            it, jx = nm.index(S['tname']), nm.index(n)
            sh.append(R(enc, val, Ms[it, jx]))
        # reverse record r- = rec(C_b -> Y): shifts at b against the copy Y
        yname = [m for (m, x, y, FF) in inst.swaps if x == b and y == a and FF == F][0]
        shb = []
        for w in range(3):
            S = inst.subs[(b, w)]
            nm, Ms = enc.mat[(b, w)]
            it, jy = nm.index(S['tname']), nm.index(yname)
            shb.append(R(enc, val, Ms[it, jy]))
        rows[(sg, a + '>' + b, R(enc, val, r), R(enc, val, rb), '/'.join(sh), '/'.join(shb))] += 1
    print('balanced swaps: (types, pair, R(r), R(r-), R at shifts of a in e1/e2/e3, R(r-) at shifts of b)')
    for k, c in sorted(rows.items()):
        print('  ', k, 'x', c)
    inc, tie = Counter(), Counter()
    for a_, Sn in enumerate(names):
        if not inst.selected[Sn]:
            continue
        for b_ in range(len(names)):
            if a_ == b_:
                continue
            r, rb = M[a_, b_], M[b_, a_]
            for i in range(3):
                x, y = val[enc.v(r, i)], val[enc.v(rb, i)]
                if not x and not y:
                    inc[i + 1] += 1
                if x and y:
                    tie[i + 1] += 1
    print('source-vs-rival pairs: single-world incomparabilities by world', dict(inc), '; single-world ties by world', dict(tie))


if __name__ == '__main__':
    main(*(sys.argv[1:] or []))
