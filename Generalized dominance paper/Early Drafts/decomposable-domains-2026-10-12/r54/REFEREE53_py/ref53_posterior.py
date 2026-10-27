"""REFEREE round 54 (file REFEREE_round53.md): independent exact checks of the posterior-family facts that
PP56 Theorem L and PP57 Theorem Q rely on.  Written from scratch (no import from PP5x_py).

Setting: three worlds, eps = 3/10, c = (1-eps)/3, M = c*1 + eps*Simplex with vertices m_v = c*1 + eps*e_v.
Posterior model C_a (likelihood a): at problem g, s_v = sum_i a_i m_{v,i} g_i (v = 1,2,3);
answer + if all s_v > 0, answer - if all s_v < 0, silent otherwise.  Answers 'P' (+) and 'M' (-), 'S', 'C'.
Rank at world w: correct 0 < S 1 < wrong 2 < C 3, where + is correct at w iff g_w > 0.

Checks (exact Fractions, random rational problems and indices):
 (A) (2V) region: if normalise(1/a) has every coordinate >= c (i.e. u in M_a) then every answer of C_a has the
     sign of g_1+g_2+g_3.  Also: outside that region a counterexample exists (so the condition is not idle).
 (B) Balanced field u1 built from its PP56 definition for a finite sampled family S (A, B, D + random members
     of the (2V) region): strict guidance at every world over all four values; every member pointwise
     lambda-Bayes at lambda = (1,1,1); h and S exactly tied on R; common advice strictly best off R.
 (C) Lemma 4.1 (pure shifts b = a o (1 + t e_w)): rank_w(C_b(g)) <= rank_w(C_a(g)) at every sampled g, strict
     somewhere; and count points where C_a answers (wrongly at w) and C_b falls silent (the wording
     'C_b answers wherever C_a does' is then false although the conclusion holds).
 (D) Increments of h -> S under u1 on the certificate cells Ep (A alone, h wrong only at world 1) and Em
     (A alone, h right only at world 1): (-2,1,1)|g| and (2,-1,-1)|g| per unit |g| (here |g| factor omitted).
"""
import random
from fractions import Fraction as Fr

random.seed(20261023)
EPS = Fr(3, 10)
C0 = (1 - EPS) / 3
VERT = [tuple(C0 + (EPS if i == v else 0) for i in range(3)) for v in range(3)]
U = (Fr(1, 3),) * 3
B = (Fr(406, 1200), Fr(421, 1200), Fr(373, 1200))
D = (Fr(406, 1200), Fr(373, 1200), Fr(421, 1200))
VALS = ('P', 'M', 'S', 'C')
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print('FAIL:', msg)


def advice(a, g):
    s = [sum(a[i] * m[i] * g[i] for i in range(3)) for m in VERT]
    if all(x > 0 for x in s):
        return 'P'
    if all(x < 0 for x in s):
        return 'M'
    return 'S'


def rank(x, g, w):
    if x == 'S':
        return 1
    if x == 'C':
        return 3
    correct = (g[w] > 0) == (x == 'P')
    return 0 if correct else 2


def in_2V_region(a):
    inv = [1 / x for x in a]
    z = sum(inv)
    return all(v / z >= C0 for v in inv)


def rand_g():
    return tuple(Fr(random.randint(-999, 999), random.randint(1, 50)) for _ in range(3))


def rand_index(radius):
    while True:
        a = tuple(Fr(1, 3) + Fr(random.randint(-1000, 1000), 1000) * radius for _ in range(3))
        if min(a) <= 0:
            continue
        z = sum(a)
        return tuple(x / z for x in a)


def u1(g, x, family_adv):
    """PP56 level 0 per unit |g| (the |g| factor is common and omitted).  family_adv = set of advice of S at g."""
    pos = [w for w in range(3) if g[w] > 0]
    neg = [w for w in range(3) if g[w] < 0]
    if not pos or not neg:  # unanimous sign
        return tuple(rank(x, g, w) for w in range(3))
    if x == 'S':
        return (0, 0, 0)
    vals = {}
    inR = len(family_adv) > 1
    hset = family_adv - {'S'}
    for y in ('P', 'M'):
        cor, wr = (pos, neg) if y == 'P' else (neg, pos)
        if inR and y in hset:
            kc, kr = len(wr), len(cor)
        elif (not inR) and family_adv == {y}:
            kc, kr = 2 * len(wr), len(cor)
        else:
            kc, kr = len(wr), 2 * len(cor)
        vals[y] = tuple(-kc if w in cor else kr for w in range(3))
    top = 1 + max(abs(t) for y in vals for t in vals[y])
    if x == 'C':
        return (top, top, top)
    return vals[x]


# (A) the (2V) region
print('(A) (2V) region: B, D in region:', in_2V_region(B), in_2V_region(D))
check(in_2V_region(B) and in_2V_region(D) and in_2V_region(U), 'B, D, u in (2V) region')
n_ok = n_tested = 0
for _ in range(400):
    a = rand_index(Fr(1, 8))
    if not in_2V_region(a):
        continue
    for _ in range(60):
        g = rand_g()
        if sum(g) == 0:
            continue
        x = advice(a, g)
        n_tested += 1
        if x != 'S':
            ok = (x == 'P') == (sum(g) > 0)
            n_ok += ok
            check(ok, f'(2V) answer sign a={a} g={g}')
print(f'    points tested {n_tested}; answers all have the sign of sum(g): {not FAIL}')
# counterexample outside the region
found = None
for _ in range(20000):
    a = rand_index(Fr(9, 10))
    if in_2V_region(a):
        continue
    g = rand_g()
    if sum(g) == 0:
        continue
    x = advice(a, g)
    if x != 'S' and ((x == 'P') != (sum(g) > 0)):
        found = (a, g, x)
        break
print('    outside the region, an answer against sign(sum g) exists:', found is not None,
      '' if found is None else f'a={tuple(map(str, found[0]))}')
check(found is not None, 'region condition not idle')

# (B) balanced field on a finite sampled family
fam = [U, B, D] + [a for a in (rand_index(Fr(1, 10)) for _ in range(40)) if in_2V_region(a)]
print('(B) family size', len(fam))
nR = nOff = 0
for _ in range(3000):
    g = rand_g()
    if sum(g) == 0 or 0 in g:
        continue
    adv = [advice(a, g) for a in fam]
    fa = set(adv)
    check(not ({'P', 'M'} <= fa), 'two-valued')
    field = {x: u1(g, x, fa) for x in VALS}
    for w in range(3):
        order = sorted(VALS, key=lambda x: rank(x, g, w))
        check(all(field[order[i]][w] < field[order[i + 1]][w] for i in range(3)), f'strict guidance g={g} w={w}')
    L = {x: sum(field[x]) for x in VALS}
    best = min(L.values())
    for x in adv:
        check(L[x] == best, f'member not lambda-Bayes at g={g}')
    if len(fa) > 1:
        nR += 1
        h = (fa - {'S'}).pop()
        check(L[h] == L['S'] == 0, 'balance on R')
        check(all(L[y] > 0 for y in VALS if y not in (h, 'S')), 'others strictly worse on R')
    else:
        nOff += 1
        v = next(iter(fa))
        check(all(L[y] > L[v] for y in VALS if y != v), 'strict optimality off R')
print(f'    points on R: {nR}, off R: {nOff}; strict guidance, lambda-Bayes members, balance: {not FAIL}')

# (C) Lemma 4.1
viol = strict = wording = 0
for _ in range(300):
    a = rand_index(Fr(1, 12))
    if not in_2V_region(a):
        continue
    w = random.randrange(3)
    t = Fr(random.randint(1, 100), 1000)
    b = tuple(a[i] * (1 + (t if i == w else 0)) for i in range(3))
    for _ in range(80):
        g = rand_g()
        if 0 in g or sum(g) == 0:
            continue
        xa, xb = advice(a, g), advice(b, g)
        ra, rb = rank(xa, g, w), rank(xb, g, w)
        viol += rb > ra
        strict += rb < ra
        wording += (xa != 'S' and xb == 'S')
check(viol == 0, 'Lemma 4.1 monotonicity')
check(strict > 0, 'Lemma 4.1 strictness somewhere')
print(f'(C) Lemma 4.1: w-worsenings found {viol}; strict w-improvements {strict}; '
      f'points where C_a answers but C_b is silent (wording repair needed): {wording}')
check(wording > 0, 'wording counterexample expected')

# (D) increments on Ep / Em for the triple family
trip = [U, B, D]
ep = em = None
for _ in range(200000):
    g = rand_g()
    if 0 in g or sum(g) <= 0:
        continue
    adv = [advice(a, g) for a in trip]
    if adv == ['P', 'S', 'S']:
        wr = tuple(w for w in range(3) if rank('P', g, w) == 2)
        if wr == (0,) and ep is None:
            ep = g
        if wr == (1, 2) and em is None:
            em = g
    if ep and em:
        break
if em is None:   # Em is a thin cell: perturb around the diagonal direction (1, -x, -x) found by bisection
    for i in range(2000, 4000):
        x = Fr(i, 10000)
        for dj in range(-40, 41):
            g = (Fr(1), -x, -x - Fr(dj, 1000000))
            if sum(g) > 0 and [advice(a, g) for a in trip] == ['P', 'S', 'S']:
                em = g
                break
        if em is not None:
            break
check(ep is not None and em is not None, 'found Ep and Em points')
for nm, g in (('Ep', ep), ('Em', em)):
    fa = {advice(a, g) for a in trip}
    inc = tuple(u1(g, 'S', fa)[w] - u1(g, 'P', fa)[w] for w in range(3))
    print(f'(D) {nm} point {tuple(map(str, g))}: increment h->S per |g| = {inc}')
    check(inc == ((-2, 1, 1) if nm == 'Ep' else (2, -1, -1)), f'increment on {nm}')

print('ALL PASS' if not FAIL else f'{len(FAIL)} FAILURES')
