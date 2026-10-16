# S3 NUMERICS: the mirrored band+exotic system of S3 Prop S3.1 on a cell grid (exact integers).
# x-cells 0..n-1 of mass 1/n (chain coordinate, c_b = cells < b*n), plus one nonnegative-problem cell N of mass wN.
# World 1: tails from the right, N counted in every tail (placed at x=2).  World 2: heads from the left, N in every head.
# W1 accepts d iff tau_d >= 0 (band1) or tau_d >= tau_{g_j} for some j, g_j = 1_{A_j} - 1_{c_a}.
# W2 accepts d iff eta_d >= 0 (band2) or eta_d >= eta_{h_j} for some j, h_j = 1_{A_j cap c_b0} - 1_{d_b0}.
# Vectors: d[0..n-1] cell values in {-1,0,1}, d[n] value on N.  Integer units: cell mass 1, N mass WN.
import random
random.seed(7)
n, WN = 128, 5
ia, ib0 = 32, 96                      # a = 1/4, b0 = 3/4
m = 8                                 # A_j = cells k >= ia with k % m == j : disjoint, spread over d_a
A = [[k for k in range(ia, n) if k % m == j] for j in range(m)]
def vec(pos=(), neg=(), N=0):
    d = [0]*(n+1)
    for k in pos: d[k] += 1
    for k in neg: d[k] -= 1
    d[n] = N; return d
def tails(d):   # tau at x = k/n for k=0..n, plus the (1,2] condition, all in integer units
    t, out = d[n]*WN, []
    for k in range(n-1, -1, -1):
        t += d[k]; out.append(t)
    return out[::-1] + [d[n]*WN] + [d[n]]          # last entry: sign of N part
def heads(d):
    h, out = d[n]*WN, [d[n]*WN]
    for k in range(n):
        h += d[k]; out.append(h)
    return out + [d[n]]
G1 = [tails(vec(pos=A[j], neg=range(ia))) for j in range(m)]
G2 = [heads(vec(pos=[k for k in A[j] if k < ib0], neg=range(ib0, n))) for j in range(m)]
def ge(u, v): return all(x >= y for x, y in zip(u, v))
Z1 = [0]*(n+3)
def acc1(d):
    t = tails(d); return ge(t, Z1) or any(ge(t, g) for g in G1)
def acc2(d):
    h = heads(d); return ge(h, Z1) or any(ge(h, g) for g in G2)
def comp(s, t): return all(-1 <= x+y <= 1 for x, y in zip(s, t))
add = lambda s, t: [x+y for x, y in zip(s, t)]
# (0) generators
assert all(acc1(vec(pos=A[j], neg=range(ia))) for j in range(m))
assert all(acc2(vec(pos=[k for k in A[j] if k < ib0], neg=range(ib0, n))) for j in range(m))
print("generators c_a <=1 A_j and d_b0 <=2 A_j cap c_b0 accepted: OK")
# (1) sum closure on random members obtained from generators by random admissible moves
def random_member(world):
    j = random.randrange(m)
    if world == 1: d = vec(pos=A[j], neg=range(ia))
    else: d = vec(pos=[k for k in A[j] if k < ib0], neg=range(ib0, n))
    if random.random() < 0.3: d = [0]*(n+1)
    acc = acc1 if world == 1 else acc2
    for _ in range(random.randrange(1, 60)):      # random single-cell changes, kept only if still accepted
        e = d[:]; k = random.randrange(n+1); e[k] = random.choice([-1, 0, 1])
        if acc(e): d = e
    return d
for world, acc in ((1, acc1), (2, acc2)):
    tested = bad = 0
    while tested < 1500:
        s, t = random_member(world), random_member(world)
        if not comp(s, t): continue
        tested += 1
        if not acc(add(s, t)): bad += 1
    print(f"world {world}: {tested} compatible pairs of members, sums not accepted: {bad}")
# (2) no nonzero nonpositive accepted
bad = 0
for _ in range(4000):
    d = [random.choice([-1, 0, 0]) for _ in range(n+1)]
    if any(d) and (acc1(d) or acc2(d)): bad += 1
print("nonpositive nonzero vectors accepted:", bad)
# (3) (K) and (4) (U) for random models (A, N) at every interior cut
def model():
    p = random.random(); Aset = {k for k in range(n) if random.random() < p}
    if random.random() < 0.5:   # perturbations of a chain member
        b = random.randrange(1, n); Aset = set(range(b)) ^ {k for k in range(n) if random.random() < 0.05}
    return Aset, (1 if random.random() < 0.2 else 0)
Kfail = Ufail = 0
for _ in range(400):
    Aset, Nn = model()
    for b in range(1, n):
        x1 = vec(pos=[k for k in Aset], neg=range(b), N=Nn)                      # 1_{E1 X} - 1_{c_b}
        x2 = vec(pos=[k for k in range(n) if k not in Aset], neg=range(b, n), N=Nn)  # 1_{E2 X} - 1_{d_b}
        if not (acc1(x1) or acc2(x2)): Kfail += 1
        trivial = (Aset == set(range(b)) and Nn == 0)
        if not trivial and acc1([-v for v in x1]) and acc2([-v for v in x2]): Ufail += 1
print("(K) failures:", Kfail, "  (U) failures (dominating or tied models):", Ufail)
# (5) world-1 sections of D = [a, a+d) u [1-h, 1): largest accepted cut per exotic generator (Q1.3 mechanism)
idd, ih = 16, 16
D = list(range(ia, ia+idd)) + list(range(n-ih, n))
def sec1(gidx=None):
    best = -1
    for b in range(0, n+1):
        t = tails(vec(pos=D, neg=range(b)))
        ok = ge(t, Z1) if gidx is None else ge(t, G1[gidx])
        if ok: best = b
    return best
print("world-1 section ends (cells; a+d+h =", ia+idd+ih, "): band", sec1(), " exotic j:", [sec1(j) for j in range(m)])
