# Q1 attempt A (n = 2): world 1 = band U union_F G(F), g_F = 1_F - 1_{[0,a)}.
# Discretised check of (i) sum-closure inside C = {-1,0,1}^N, (ii) sign conditions,
# (iii) the exact non-closed section of Prop Q1.3. Exact rationals; run with python3 -I.
from fractions import Fraction as Fr
import random
N = 60                      # bins of [0,1], width 1/N
a_idx = 18                  # a = 0.3
w = Fr(1, N)
def tails(d):               # tau_d(x_k) = sum_{l>=k} d_l * w, k = 0..N (tau(1)=0)
    t = [Fr(0)]*(N+1)
    for k in range(N-1, -1, -1): t[k] = t[k+1] + d[k]*w
    return t
def band(d): return all(v >= 0 for v in tails(d))
def gF(F): return [(-1 if k < a_idx else 0) + (1 if k in F else 0) for k in range(N)]
random.seed(1)
# a family of 'spread' exotic sets F_j inside [a,1]: every 6th bin offset j (disjoint)
Fam = [set(range(a_idx + j, N, 6)) for j in range(6)]
TF = [tails(gF(F)) for F in Fam]
def inG(d, i): t = tails(d); return all(t[k] >= TF[i][k] for k in range(N+1))
def acc(d): return band(d) or any(inG(d, i) for i in range(len(Fam)))
def rand_member(S=None):
    # random element of G(F_i): 1_F - 1_S (S inside [0,a)), then random band moves keeping C-valued
    i = random.randrange(len(Fam))
    if S is None: S = set(k for k in range(a_idx) if random.random() < 0.5)
    d = [(1 if k in Fam[i] else 0) - (1 if k in S else 0) for k in range(N)]
    for _ in range(random.randrange(0, 12)):
        k = random.randrange(N); 
        if d[k] < 1 and random.random() < 0.5: d[k] += 1          # add a nonnegative vector
        else:                                                     # move a -1 to the left
            l = random.randrange(0, k+1)
            if d[k] == -1 and d[l] == 0: d[k], d[l] = 0, -1
    assert acc(d); return d
viol = 0; tested = 0
for _ in range(4000):
    S = set(k for k in range(a_idx) if random.random() < 0.5)
    s = rand_member(S); t = rand_member(set(range(a_idx)) - S)
    if random.random() < 0.3:          # pair an exotic member with a band member
        t = [0]*N; t[random.randrange(N)] = 1
    u = [x+y for x, y in zip(s, t)]
    if all(-1 <= v <= 1 for v in u):
        tested += 1
        if not acc(u): viol += 1
print("sum-closure: compatible pairs tested", tested, "violations", viol)
# sign condition: no nonpositive nonzero vector is accepted (random ones)
bad = 0
for _ in range(3000):
    d = [-(random.random() < 0.3) for _ in range(N)]
    if any(d) and acc(d): bad += 1
print("nonpositive nonzero accepted:", bad)
# exact section of A = [a,a+d) u [1-h,1) for the exotic family F_j = spread with density 1/m on [a,1]
def beta_F(GD, GF, xs):   # max b with GD(x)-GF(x) >= (b-x)_+ for x>=a, requires GD>=GF
    if any(GD(x) < GF(x) for x in xs): return None
    return min(1, min(x + GD(x) - GF(x) for x in xs))
a, d, h = Fr(3,10), Fr(1,10), Fr(1,10)
xs = [a + Fr(k, 1000)*(1-a) for k in range(1001)]
GD = lambda x: max(Fr(0), a+d-x) + min(h, 1-x)
out = []
for m in [2, 5, 10, 100, 1000]:
    GF = lambda x, m=m: (1-x)/m          # tail profile of a set of density 1/m on [a,1]
    out.append((m, beta_F(GD, GF, xs)))
print("beta_F(A) for F of density 1/m:", [(m, None if b is None else float(b)) for m, b in out])
print("sup = min(x+G_D(x)) =", float(min(x + GD(x) for x in xs)), "(not attained); band value =", float(d+h))
