"""refmap77: CHECK of PP77 Theorem 3.1 (exact refusal map of a same-ray second defender) against
PP76 Thm 1.1 (pointwise coupled rule, lib79.options), exact cells with radial halves.

Committed carriers: T, B = B_{3,t} (index (1,1,r)), inner/outer ray-3 members, ray-1 and ray-2 members.
Second defender B_tau = (1,1,s) with r < s < 1.  Splices X2 = T[S -> B], S from families
a, b, M, gen and random radially non-conic patterns.
Formula (Thm 3.1): K_C = L n {C != T};  P+ = S \ L(tau), P- = L(tau) \ S;
  Fav_w = {g in D : X2 strictly w-better than B_tau};  U_C = (P+ \ K_C) u (P- n K_C);
  C affected at w  <=>  U_C subset Fav_w;   mixed  <=>  affected and ((P+ n K_C) u (P- \ K_C)) n Fav_w != 0.
Run: python3 -I -B refmap77.py > refmap77.out   (from inside PP77_py)
"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP79_py'))
from lib79 import *

r = F(20, 21)
MODELS = {'T': post((1, 1, 1)), 'B': post((1, 1, r)),
          'R3in': post((1, 1, F(83, 84))), 'R3mid': post((1, 1, F(27, 28))), 'R3out': post((1, 1, F(9, 10))),
          'R1a': post((F(41, 42), 1, 1)), 'R1b': post((F(9, 10), 1, 1)),
          'R2a': post((1, F(41, 42), 1)), 'R2b': post((1, F(9, 10), 1))}
TAUS = [F(41, 42), F(55, 56), F(83, 84)]

def splices(At, rnd):
    L = [i for i, a in enumerate(At) if a['vals']['T'] != a['vals']['B']]
    fams = {}
    def mk(pred):
        return {i for i in L if pred(At[i])}
    fams['a'] = mk(lambda a: a['o'] in (0, 2) or a['half'] == 0)
    fams['b'] = mk(lambda a: a['o'] in (1, 2) or a['half'] == 0)
    fams['M'] = mk(lambda a: a['o'] in (0, 2) or (a['type'] == ('A', 1) and a['vals']['T'] == 'h' and a['half'] == 0))
    fams['gen'] = mk(lambda a: a['half'] == 0)
    fams['no1'] = mk(lambda a: a['o'] in (1, 2) and a['half'] == 0 or a['o'] == 2)
    fams['no2'] = mk(lambda a: a['o'] in (0, 2) and a['half'] == 0 or a['o'] == 2)
    fams['cov'] = mk(lambda a: a['o'] in (0, 2) or (a['vals']['R1b'] != a['vals']['T'] and a['half'] == 0))
    fams['cov2'] = mk(lambda a: a['o'] in (1, 2) or (a['vals']['R2b'] != a['vals']['T'] and a['half'] == 0))
    for j in range(40):
        dens = [rnd.random() for _ in range(3)]
        fams['rnd%d' % j] = {i for i in L if rnd.random() < dens[At[i]['o']]}
    return fams

def formula(At, Cn, w, S, Bt):
    Lset = {i for i, a in enumerate(At) if a['vals']['T'] != a['vals']['B']}
    K = {i for i in Lset if At[i]['vals'][Cn] != At[i]['vals']['T']}
    Ltau = {i for i, a in enumerate(At) if Bt[i] != a['vals']['T']}
    Pp, Pm = S - Ltau, Ltau - S
    X = lambda i: At[i]['vals']['B'] if i in S else At[i]['vals']['T']
    Fav = {i for i in Pp | Pm if lt(X(i), Bt[i], At[i]['h'], w)}
    U = (Pp - K) | (Pm & K)
    aff = U <= Fav
    mixed = aff and bool((((Pp & K) | (Pm - K)) & Fav))
    return aff, mixed

def run():
    rnd = random.Random(77)
    n = bad = 0
    tally = {}
    for s in TAUS:
        mods = dict(MODELS); mods['Bt'] = post((1, 1, s))
        At = atoms(mods)
        Bt = [a['vals']['Bt'] for a in At]
        for fam, S in splices(At, rnd).items():
            X = [a['vals']['B'] if i in S else a['vals']['T'] for i, a in enumerate(At)]
            if not (N1(At, Bt, X) and corr(At, 'T', Bt, X) and corr(At, 'B', Bt, X)):
                continue
            for Cn in MODELS:
                for w in range(3):
                    fam_ = family(At, Cn, None, None, w, Xvals=X, Bvals=Bt)
                    aff_c = fam_ is not None and any(f for o in fam_ for (v, f) in o)
                    mix_c = bool(mixed_available(At, Cn, w, Bt, X)) if aff_c else False
                    aff_f, mix_f = formula(At, Cn, w, S, Bt)
                    n += 1
                    if (aff_c, mix_c) != (aff_f, mix_f):
                        bad += 1
                        if bad <= 5: print('MISMATCH', s, fam, Cn, w + 1, (aff_c, mix_c), (aff_f, mix_f))
                    if mix_c:
                        key = (fam[:3] if fam.startswith('rnd') else fam, Cn, w + 1)
                        tally[key] = tally.get(key, 0) + 1
    print('carrier-world-splice-scale cases compared: %d ; mismatches: %d' % (n, bad))
    print('mixed refusals (family, carrier, world): count')
    for k in sorted(tally): print('  ', k, tally[k])
    assert bad == 0
    print('Theorem 3.1 formula = PP76 Thm 1.1 on every case: PASS')

if __name__ == '__main__':
    run()
