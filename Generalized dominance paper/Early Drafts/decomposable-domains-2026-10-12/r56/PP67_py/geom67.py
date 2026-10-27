# PP67 geometric checks (exact rationals on sample problems).
# Run: python3 -I -B geom67.py > geom67.out
from fractions import Fraction as Fr
import itertools, random
random.seed(67)
c, e = Fr(7,30), Fr(3,10)
MV = [tuple(c + (e if i==v else 0) for i in range(3)) for v in range(3)]      # vertices of M
M0 = [(Fr(16,23), Fr(7,23), Fr(0)), (Fr(7,23), Fr(16,23), Fr(0))]             # edge projection of M from e3
def adv(K, g):
    s = [sum(k[i]*g[i] for i in range(3)) for k in K]
    if all(x > 0 for x in s): return 1
    if all(x < 0 for x in s): return -1
    return 0
def rank(x, g, w):
    if x == 0: return 1
    return 0 if x*g[w] > 0 else 2
T, Dst, N = MV, M0, MV + M0          # N = D_{conv(M u M0)}
G = [g for g in itertools.product(range(-7,8), repeat=3) if all(x != 0 for x in g)]
G += [tuple(Fr(random.randint(-500,500), random.randint(1,70)) for _ in range(3)) for _ in range(25000)]
G = [g for g in G if all(x != 0 for x in g)]
ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name); ok &= bool(cond)
def cls(g):                      # odd world (0-based) of a mixed g, or None if unanimous
    s = [1 if x > 0 else -1 for x in g]
    if s[0] == s[1] == s[2]: return None
    for o in range(3):
        if s[(o+1)%3] == s[(o+2)%3]: return o
def lab(x, g, o):                # A = majority answer, B = minority, S
    if x == 0: return 'S'
    return 'B' if x*g[o] > 0 else 'A'
# 0. M0 is the radial projection of M from e3
chk("M0 = projection of M's vertices 1,2 from e3",
    all(tuple(v[i]/(v[0]+v[1]) for i in range(2)) == m[:2] for v, m in zip(MV[:2], M0)))
# 1. N = T meet D*
chk("N = T ^ D* (keep common answer, else S) on %d samples" % len(G),
    all(adv(N,g) == (adv(T,g) if adv(T,g) == adv(Dst,g) else 0) for g in G))
# 2. D* answers A on all of M3; D* and N weakly 3-worse than T; N silent on Sil(T)
chk("D* = A on every M3 sample", all(lab(adv(Dst,g),g,2) == 'A' for g in G if cls(g) == 2))
chk("D* never strictly 3-better than T", all(rank(adv(Dst,g),g,2) >= rank(adv(T,g),g,2) for g in G))
chk("N never strictly 3-better than T", all(rank(adv(N,g),g,2) >= rank(adv(T,g),g,2) for g in G))
chk("N silent wherever T is silent", all(adv(N,g) == 0 for g in G if adv(T,g) == 0))
chk("N never strictly 3-better than... D* is weakly 3-worse than N", all(rank(adv(Dst,g),g,2) >= rank(adv(N,g),g,2) for g in G))
# 3. region R_B = M3 & {T = B}: N = S, D* = A there (gains for N, D* at worlds 1 and 2)
RB = [g for g in G if cls(g) == 2 and lab(adv(T,g),g,2) == 'B']
chk("R_B non-empty (%d samples), N = S and D* = A on it" % len(RB),
    RB and all(adv(N,g) == 0 and lab(adv(Dst,g),g,2) == 'A' for g in RB))
gw = (-1,-1,10)
chk("witness g = (-1,-1,10): class M3, T = B, N = S, D* = A", cls(gw) == 2 and lab(adv(T,gw),gw,2) == "B" and adv(N,gw) == 0 and lab(adv(Dst,gw),gw,2) == "A")
# 4. type census of (T, N, D*) by class
allowed = {2: {('S','S','A'), ('A','A','A'), ('B','S','A')},
           0: {('S','S','S'), ('S','S','B'), ('A','A','A'), ('A','S','S'), ('A','S','B'), ('B','B','B')},
           1: {('S','S','S'), ('S','S','B'), ('A','A','A'), ('A','S','S'), ('A','S','B'), ('B','B','B')}}
seen = {0: set(), 1: set(), 2: set()}
good = True
for g in G:
    o = cls(g)
    if o is None:
        good &= adv(T,g) == adv(N,g) == adv(Dst,g) != 0; continue
    t = (lab(adv(T,g),g,o), lab(adv(N,g),g,o), lab(adv(Dst,g),g,o))
    seen[o].add(t); good &= t in allowed[o]
chk("unanimous points: all three answer; every mixed triple is an allowed type", good)
for o in range(3): print("   class o=%d types seen: %s" % (o+1, sorted(seen[o])))
# 5. N is the most silent coherent model weakly 3-worse than T:
#    a point m of the simplex keeps all of T's 3-wrong answers iff m in conv(M u M0).
H = [(MV[0],MV[2]), (MV[2],MV[1]), (MV[1],M0[1]), (M0[1],M0[0]), (M0[0],MV[0])]  # hull boundary, some orientation
def side(p, q, m): return (q[0]-p[0])*(m[1]-p[1]) - (q[1]-p[1])*(m[0]-p[0])
sg = [side(p, q, MV[2] if q != MV[2] and p != MV[2] else M0[0]) for p, q in H]
def inside(m): return all(side(p,q,m)*s >= 0 for (p,q), s in zip(H, sg))
W3 = [g for g in G if adv(T,g) != 0 and rank(adv(T,g),g,2) == 2]          # T's 3-wrong answers
bad_in, miss_out, nout = 0, 0, 0
for _ in range(400):
    a, b = Fr(random.randint(0,200),200), Fr(random.randint(0,200),200)
    if a + b > 1: a, b = 1-a, 1-b
    m = (a, b, 1-a-b)
    keeps = all(adv([m], g) == adv(T, g) for g in W3)
    if inside(m): bad_in += (not keeps)
    else:
        nout += 1; miss_out += keeps
chk("every sampled m in conv(M u M0) keeps all T's 3-wrong answers", bad_in == 0)
print("   sampled m outside the hull: %d; of these keeping all 3-wrong answers on the samples: %d" % (nout, miss_out))
chk("(sample-level) outside points drop some 3-wrong answer, up to boundary slack", miss_out <= nout // 20)
print("ALL PASS" if ok else "SOME FAIL")
