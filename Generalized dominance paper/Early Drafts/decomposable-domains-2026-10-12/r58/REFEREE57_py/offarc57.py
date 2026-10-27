"""offarc57: exact incoherence certificates for the Bayes acts X_lam of PP69's field at off-arc weights lam.
X_lam(g) = argmin_a lam.phi(g,a).  Certificate: problems g1, g2 with X_lam answering h1, h2 (strict argmin, all
vertex dot products non-zero, so X_lam is locally constant near them), and g' = c1 h1 + c2 h2 (c1,c2 > 0) at which
X_lam (strict argmin, locally constant) does NOT answer g'.  Any D_K answering h1, h2 on open dense subsets of
neighbourhoods answers c1 h1' + c2 h2' on an open dense subset of a neighbourhood of g' (min_K is superadditive),
so X_lam is not a.e. equal to any D_K: incoherent (PROVED given the certificate).  On-arc controls: none found.
"""
import sys, random
sys.path.insert(0, '.')
from rlib import *
from curve57 import *

ALLV = [v1, v2, v3, w1, w2, h12]
def generic(g):
    if cls(g) not in (1, 2, 3): return False
    if any(x == 0 for x in g): return False
    if any(dot(v, g) == 0 for v in ALLV): return False
    return True

def X(lam, g):
    ph = phi(g)
    U = {a: dot(lam, ph[a]) for a in ph}
    b = min(U.values())
    am = [a for a in U if U[a] == b]
    if len(am) != 1: return None
    a = am[0]
    if a in ('S', 'X'): return a
    m = majsign(g)
    s = m if a == 'A' else -m
    return ('ans', tuple(s * x for x in g))

def answers(lam, g, h):
    """does X_lam answer exactly the direction h at the problem g (= +-h)?"""
    r = X(lam, g)
    if r is None: return None
    return r != 'S' and r != 'X' and r[0] == 'ans' and all(r[1][i] * 1 == h[i] for i in range(3))

def search(lam, n=600, seed=1, combos=((1, 1), (1, 2), (2, 1), (1, 4), (4, 1))):
    rnd = random.Random(seed)
    ans = []
    while len(ans) < n:
        g = tuple(F(rnd.randint(-60, 60), rnd.randint(1, 9)) for _ in range(3))
        if not generic(g): continue
        r = X(lam, g)
        if r is None or r in ('S', 'X'): continue
        ans.append(r[1])
    for i in range(len(ans)):
        for j in range(i + 1, len(ans)):
            for c1, c2 in combos:
                gp = tuple(c1 * ans[i][k] + c2 * ans[j][k] for k in range(3))
                if not generic(gp): continue
                r = X(lam, gp)
                if r is None: continue
                if r in ('S', 'X') or r[1] != gp:
                    return (ans[i], ans[j], (c1, c2), gp, r)
    return None

tests = [('off', (F(2, 5), F(3, 10), F(3, 10))), ('off', (F(9, 20), F(7, 20), F(1, 5))),
         ('off', (F(3, 5), F(1, 5), F(1, 5))), ('off', (F(1, 2), F(1, 10), F(2, 5))),
         ('near', (F(2 + F(1, 2), 6) + F(1, 50), F(2 + F(1, 2), 6) - F(1, 50), F(1, 6))),
         ('near', (F(2 + F(3, 20), 6) + F(1, 50), F(2 + F(3, 20), 6) - F(1, 50), F(2 - F(3, 10), 6))),
         ('on', p(F(0))), ('on', p(F(1, 2))), ('on', p(F(17, 20)))]
for kind, lam in tests:
    assert sum(lam) == 1
    cert = search(lam, n=(600 if kind != 'on' else 150), combos=((1, 1), (1, 2), (2, 1)))
    print(kind, tuple(str(x) for x in lam), '->', 'CERTIFICATE' if cert else 'none found')
    if cert:
        h1, h2, cc, gp, r = cert
        print('     h1 =', tuple(str(x) for x in h1), ' h2 =', tuple(str(x) for x in h2), ' c =', cc)
        print('     g\' =', tuple(str(x) for x in gp), ' X_lam(g\') =', r if r in ('S', 'X') else ('answers', tuple(str(x) for x in r[1])))
