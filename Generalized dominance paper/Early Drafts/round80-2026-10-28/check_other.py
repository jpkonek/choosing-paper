# Checks for Sections 8.2, 8.3 and 8.5
from fractions import Fraction as Fr
import math, itertools, random
INF=math.inf
random.seed(1)

# --- 8.2 lifted SSK Example 2 on Omega={1,2}; credence c=(e,a,b,W) on (empty,{1},{2},Omega)
def g0(y): return 0.0 if y==0 else 1+y
def g1(y): return INF if y==0 else y-math.log(y)
def L(c):
    e,a,b,W=c; r=e*e+(1-W)**2
    return ((1-a)**2+g0(b)+r, a*a+g1(b)+r)
def E(t,c):  # prior (t,1-t), 0*inf=0
    l=L(c); return sum(w*x for w,x in ((t,l[0]),(1-t,l[1])) if w>0)
grid=[i/40 for i in range(41)]
for t in grid:
    q=(0,t,1-t,1); Vq=E(t,q); assert Vq<INF
    for _ in range(400):
        m=tuple(random.random() for _ in range(4))
        if random.random()<0.3: m=(m[0],m[1],0.0,m[3])
        assert E(t,m)>Vq-1e-12
m=(0,0.5,0,1); print("lifted: L(m)=",L(m)," L(delta1)=",L((0,1,0,1)))
assert L(m)==(0.25,INF) and L((0,1,0,1))==(0.0,INF)

# --- 8.3 Nielsen 2021: Omega={1,2,3}, cells {1},{2,3}; credence functions on all 8 subsets
W=[1,2,3]; subsets=[frozenset(s) for r in range(4) for s in itertools.combinations(W,r)]
def cf(p): return {A:sum(p[w-1] for w in A) for A in subsets}
def brier(c,w): return sum(((1 if w in A else 0)-c[A])**2 for A in subsets)
def logs(c,w):
    tot=0.0
    for A in subsets:
        x=c[A] if w in A else 1-c[A]
        tot+= INF if x<=0 else -math.log(x)
    return tot
v1,v2=cf((1,0,0)),cf((0,1,0))
print("Brier J_1(v1), J_1(v2):",brier(v1,1),brier(v2,1))
assert brier(v1,1)==0 and brier(v2,1)==4
c=cf((0,0.5,0.5)); cond=cf((0,0.5,0.5))  # plan on cell {2,3}
def prof(J,plan1):
    return tuple(J(c,w)+J(plan1 if w==1 else cond,w) for w in W)
zero={A:0.0 for A in subsets}
for plan in (v2,v1,zero):
    print("log profile:",prof(logs,plan))
assert prof(logs,v2)==prof(logs,v1)==prof(logs,zero)

# --- 8.5 Joyce
# (a) two-cell tie example
def LT(x): return ((1-x[0]+x[1])**2,(1+x[0]-x[1])**2)
for _ in range(2000):
    x=(Fr(random.randint(0,100),100),Fr(random.randint(0,100),100)); d=x[0]-x[1]
    assert LT(x)==LT(((1+d)/2,(1-d)/2))
# truth-directedness at world 1 (truth (1,0)): increasing x1 or decreasing x2 strictly lowers L1
for _ in range(2000):
    x=[random.random(),random.random()]; y=[random.uniform(x[0],1),random.uniform(0,x[1])]
    if y!=x: assert LT(y)[0]<LT(x)[0]
print("tie example: every credence tied with a coherent one; L(0,0)=",LT((0,0)))

# (b) additive example, general N
def addL(x,N):
    def s1(b): return 3*(1-b)**2+2*(N-1)*(1-b)
    def s0(b): return 3*b*b+2*b
    return [s1(x[w])+sum(s0(x[n]) for n in range(N) if n!=w) for w in range(N)]
def bayes(p,N): return [min(max(((2*N+6)*pn-2)/Fr(6),Fr(0)),Fr(1)) for pn in p]
for N in (3,4,5,7):
    # truth-directed: derivative signs
    # coherent b is the unique Bayes model for (6b+2)/(2N+6)
    for _ in range(200):
        r=[random.randint(0,20) for _ in range(N)]; s=sum(r) or 1; b=[Fr(x,s) for x in r]
        if sum(b)!=1: continue
        p=[(6*bn+2)/(2*N+6) for bn in b]; assert sum(p)==1 and min(p)>0 and bayes(p,N)==b
    pa=[Fr(1,2),Fr(1,2)]+[Fr(0)]*(N-2); xa=bayes(pa,N)
    assert sum(xa)>1
    # exact check that x_a minimises expected loss under pa among a random sample
    ea=lambda x: sum(w*l for w,l in zip(pa,addL(x,N)))
    for _ in range(300):
        y=[Fr(random.randint(0,60),60) for _ in range(N)]
        if y!=xa: assert ea(y)>ea(xa)
    # ties between constant credences 1/(2N) and 3/(2N)
    u=[Fr(3,2*N)]*N; v=[Fr(1,2*N)]*N
    assert addL(u,N)==addL(v,N)
    print("N=%d: x_a="%N,[str(t) for t in xa]," tie profile",str(addL(u,N)[0]))
# coherent margin for N=3
N=3; xa=bayes([Fr(1,2),Fr(1,2),0],3); La=addL(xa,3)
best=min(max(l-la for l,la in list(zip(addL([Fr(i,200),Fr(j,200),Fr(200-i-j,200)],3),La))[:2]) for i in range(201) for j in range(201-i))
print("N=3 L(x_a)=",[str(t) for t in La]," min over coherent of max_{w=1,2} excess:",best)

# (c) prop:joyce loss: permutation invariance
def LJ(x):
    z=[math.exp(t) for t in x]; S=sum(z); eps=1/250
    return [(1-zi/S)**2+eps*(sum(x)-1)**2 for zi in z]
for _ in range(1000):
    x=[random.random() for _ in range(3)]; perm=random.choice(list(itertools.permutations(range(3))))
    y=[x[perm[i]] for i in range(3)]
    assert all(abs(LJ(y)[i]-LJ(x)[perm[i]])<1e-14 for i in range(3))
print("prop:joyce: L(1,1,0)=",LJ([1,1,0])," L(1/2,1/2,0)=",LJ([.5,.5,0]))
