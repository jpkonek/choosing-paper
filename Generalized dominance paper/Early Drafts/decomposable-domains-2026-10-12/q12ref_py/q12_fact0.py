# Q1.2 repair check: Fact 0 (Thm kkm) needs closed sections at BOTH worlds, which attempt A lacks.
# Direct replacement: for any model X=(A,N), b2 := clip(mu(A)-mu(N),0,1) lies in S1(X) (band part) and in S2(X).
# Also: undominatedness / no tie partner of each C_b, tested on random X (band + exotic family).
from fractions import Fraction as Fr
import random
random.seed(7)
def tau_at(terms, x): return sum(c*max(Fr(0), hi - max(lo, x)) for c, lo, hi in terms if hi > x)
def nonneg(terms, ref=None):
    pts = {Fr(0), Fr(1), Fr(2)}
    for _, lo, hi in terms + (ref or []): pts |= {lo, hi}
    return all(tau_at(terms, p) - (tau_at(ref, p) if ref else 0) >= 0 for p in pts if 0 <= p <= 2)
a = Fr(3,10); Ngrid = 40; w = Fr(1, Ngrid)
fam = [[(a + k*Fr(7,10)/12 + j*Fr(7,10)/(12*6), a + k*Fr(7,10)/12 + (j+1)*Fr(7,10)/(12*6)) for k in range(12)] for j in range(6)]
def gF(F): return [(Fr(1), lo, hi) for lo, hi in F] + [(Fr(-1), Fr(0), a)]
def acc(terms): return nonneg(terms) or any(nonneg(terms, gF(F)) for F in fam)
def rand_X():
    A = [(k*w, (k+1)*w) for k in range(Ngrid) if random.random() < random.random()]
    n = Fr(random.randrange(0, 8), 20) if random.random() < 0.5 else Fr(0)
    return A, n
bad0 = 0; badU = 0; T = 0
for _ in range(400):
    A, n = rand_X(); muA = sum(hi-lo for lo, hi in A)
    b2 = min(Fr(1), max(Fr(0), muA - n))
    E1X = [(Fr(1), lo, hi) for lo, hi in A] + ([(Fr(1), Fr(1), 1+n)] if n else [])
    in1 = acc(E1X + [(Fr(-1), Fr(0), b2)])          # C_b2 <=_1 X
    in2 = (1 - b2) <= (1 - muA) + n                 # psi2(C_b2) <= psi2(X)
    T += 1
    if not (in1 and in2): bad0 += 1
    # undominatedness of C_b at random grid b: X <=_1 C_b and X <=_2 C_b  ==> X = C_b
    b = Fr(random.randrange(1, Ngrid), Ngrid)
    d1 = [(Fr(1), Fr(0), b)] + [(-c, lo, hi) for c, lo, hi in E1X]   # 1_{c_b} - 1_{E1 X}
    x_le_1 = acc(d1); x_le_2 = (1 - muA) + n <= 1 - b
    isCb = (n == 0) and sorted(A) == [(k*w, (k+1)*w) for k in range(int(b*Ngrid))]
    if x_le_1 and x_le_2 and not isCb: badU += 1
print("random models:", T, " b2 in S1 and S2 fails:", bad0, " C_b dominated/tied by other model:", badU)
