"""Referee check of Lemma D2.2's combinatorics: PG(2,q) lines pairwise meet in one point, each point on q+1
lines, multiplicity of the chosen K*L lines <= q+1, and the (D4) bound (q+1)/L_n -> 0 with q_n >= 4^n.
Run: python3 -I design_check.py"""
import itertools
from fractions import Fraction as Fr
def pg2(q):
    pts, seen = [], set()
    for v in itertools.product(range(q), repeat=3):
        if v == (0,0,0): continue
        c = next(t for t in v if t); inv = pow(c, q-2, q)
        w = tuple((inv*t) % q for t in v)
        if w not in seen: seen.add(w); pts.append(w)
    idx = {p:i for i,p in enumerate(pts)}
    return pts, [frozenset(idx[p] for p in pts if sum(x*y for x,y in zip(l,p)) % q == 0) for l in pts]
bad = 0
for q in [2,3,5,7,11,13,17]:
    pts, lines = pg2(q)
    Pi = len(pts); assert Pi == q*q+q+1
    ok1 = all(len(l) == q+1 for l in lines)
    ok2 = all(len(l & m) == 1 for l, m in itertools.combinations(lines, 2))
    ok3 = all(sum(p in l for l in lines) == q+1 for p in range(Pi))
    print('q', q, 'Pi', Pi, 'lines have q+1 pts', ok1, 'pairwise meet in 1 pt', ok2, 'each pt on q+1 lines', ok3)
    bad += (not (ok1 and ok2 and ok3))
def isprime(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n % i == 0: return False
        i += 1
    return True
for n in range(1, 12):
    q = 4**n
    while not isprime(q): q += 1
    Pi = q*q+q+1; Kn = 2**n; Ln = Pi // Kn
    bound = Fr(q+1, Ln); claimed = Fr(2*(q+1)*2**n, q*q)
    print('n', n, 'q_n', q, 'L_n', Ln, '(q+1)/L_n = %.3e' % float(bound), '<= 2(q+1)2^n/q^2:', bound <= claimed,
          ' K_n L_n <= Pi_n:', Kn*Ln <= Pi)
    bad += (bound > claimed) or (Kn*Ln > Pi)
print('TOTAL FAILURES', bad)
