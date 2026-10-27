# PP64 geometric checks for the first extension (exact rationals on sample problems).
from fractions import Fraction as Fr
import itertools, random
random.seed(64)
c, e = Fr(7,30), Fr(3,10)
MV = [tuple(c + (e if i==v else 0) for i in range(3)) for v in range(3)]   # vertices of M
def advice(Kverts, g):
    s = [sum(k[i]*g[i] for i in range(3)) for k in Kverts]
    if all(x>0 for x in s): return 1
    if all(x<0 for x in s): return -1
    return 0
def post(a):  # posterior credal vertices (unnormalised is fine for signs)
    return [tuple(a[i]*m[i] for i in range(3)) for m in MV]
def rank(x, g, w):
    if x == 0: return 1
    return 0 if x*g[w] > 0 else 2
T = MV
D = post((1,1,0))          # edge posterior at p=(1/2,1/2,0): K=[(16,7,0),(7,16,0)]/23
G = [g for g in itertools.product(range(-7,8), repeat=3) if all(x!=0 for x in g)]
G += [tuple(Fr(random.randint(-400,400),random.randint(1,60)) or Fr(1) for _ in range(3)) for _ in range(20000)]
G = [g for g in G if all(x!=0 for x in g)]
ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ")+name); ok &= bool(cond)
# 1. D weakly 3-worse than T everywhere; strictly somewhere
worse3 = [g for g in G if rank(advice(D,g),g,2) > rank(advice(T,g),g,2)]
better3 = [g for g in G if rank(advice(D,g),g,2) < rank(advice(T,g),g,2)]
chk("D never strictly 3-better than T (%d samples)" % len(G), not better3)
chk("D strictly 3-worse than T on %d samples" % len(worse3), len(worse3) > 0)
# 2. world 1 (and 2): mixed
b1 = [g for g in G if rank(advice(D,g),g,0) < rank(advice(T,g),g,0)]
w1 = [g for g in G if rank(advice(D,g),g,0) > rank(advice(T,g),g,0)]
chk("D vs T mixed at world 1 (%d better, %d worse)" % (len(b1),len(w1)), b1 and w1)
g = (-1,-1,10); chk("witness (-1,-1,10): T=+, D=-", advice(T,g)==1 and advice(D,g)==-1)
g = (2,-1,2);   chk("witness (2,-1,2): T=+, D=S", advice(T,g)==1 and advice(D,g)==0)
# 3. g0 = (1,1,-2): T silent, D answers +, threshold 7/16 on the -e3 ray
g0 = (1,1,-2)
chk("T silent at g0, D answers + at g0", advice(T,g0)==0 and advice(D,g0)==1)
chk("C_(1,1,s) answers + at g0 iff s<7/16", all((advice(post((1,1,s)),g0)==1) == (s < Fr(7,16))
      for s in [Fr(k,64) for k in range(1,64)]))
# 4. -e2 ray: silent at g0 down to the edge {1,3}
chk("C_(1,s,1) silent at g0 for s in (0,1], and edge model (1,0,1) silent",
    all(advice(post((1,s,1)),g0)==0 for s in [Fr(k,64) for k in range(0,65)]))
# 5. Pareto lemma: no sample point where some advice is weakly better at all supp worlds and differs
def pareto_ok(K, supp):
    for g in G[:4000]:
        a0 = advice(K,g)
        for x in (1,-1,0):
            if x==a0: continue
            if all(rank(x,g,w) <= rank(a0,g,w) for w in supp): return False
    return True
chk("Pareto: T on {1,2,3}", pareto_ok(T,(0,1,2)))
chk("Pareto: D on {1,2}", pareto_ok(D,(0,1)))
chk("Pareto: posterior (3,1,1) on {1,2,3}", pareto_ok(post((3,1,1)),(0,1,2)))
# 6. along pure-shift rays (-e3 and -e2 from u) each problem changes monotonically: + side never re-entered
def mono(ray):
    ss = [Fr(k,40) for k in range(40,-1,-1)]
    for g in G[:6000]:
        seq = [advice(post(ray(s)),g) for s in ss]
        # sums move in one direction: allowed patterns are monotone sequences in {-1,0,1}
        if not (all(x<=y for x,y in zip(seq,seq[1:])) or all(x>=y for x,y in zip(seq,seq[1:]))): return False
    return True
chk("monotone advice along -e3 ray", mono(lambda s:(1,1,s)))
chk("monotone advice along -e2 ray", mono(lambda s:(1,s,1)))
# 7. ray carriers: q'=(1,1,9/10); z=(1,1,s), s in (7/16+,9/10): C_z = C_q' on L_q'={C_q'!=T}
def carriers(ray, d, svals, E):
    q = post(ray(d)); bad = 0; n = 0
    for s in svals:
        z = post(ray(s))
        for g in G[:6000]:
            if advice(q,g) != advice(T,g):
                n += 1
                if advice(z,g) != advice(q,g): bad += 1
        if any(advice(z,gE) != 0 for gE in E): bad += 1
    return bad, n
E = [(Fr(1)+Fr(i,20), Fr(1)+Fr(j,20), Fr(-2)+Fr(k,20)) for i in (-1,0,1) for j in (-1,0,1) for k in (-1,0,1)]
chk("E sample is T-silent with g1,g2>0>g3", all(advice(T,x)==0 and x[0]>0 and x[1]>0 and x[2]<0 for x in E))
bad,n = carriers(lambda s:(1,1,s), Fr(9,10), [Fr(k,20) for k in range(10,18)], E)
chk("-e3 ray: z=(1,1,s), s in [1/2,17/20] carries rec(C_q',X_E), q'=(1,1,9/10) (%d layer checks, %d bad)"%(n,bad), bad==0)
bad,n = carriers(lambda s:(1,s,1), Fr(9,10), [Fr(k,20) for k in range(6,18)], E)
chk("-e2 ray: z=(1,s,1), s in [3/10,17/20] carries rec(C_q',X_E), q'=(1,9/10,1) (%d checks, %d bad)"%(n,bad), bad==0)
# beyond: the carry breaks by a SECOND change (+ -> S -> -) on the layer L_q' (2V fails far from u)
q = post((1,Fr(9,10),1)); L = [g for g in G[:6000] if advice(q,g)!=advice(T,g)]
br = [g for g in L if advice(post((1,Fr(1,4),1)),g)!=advice(q,g)]
chk("-e2 ray: at s=1/4 the carry breaks (%d layer points), always by a second change T:+-> q':S -> z:- or mirror"%len(br),
    br and all(advice(T,g)==-advice(post((1,Fr(1,4),1)),g)!=0 and advice(q,g)==0 for g in br))
chk("edge {1,3} model (1,0,1) does NOT carry it", any(advice(post((1,0,1)),g)!=advice(q,g) for g in L))
print("ALL PASS" if ok else "SOME FAIL")
