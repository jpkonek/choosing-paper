# Checks for Section 8.1 (proper scores): exact arithmetic where possible.
from fractions import Fraction as Fr
import math, itertools
INF = math.inf

# 1. Flat proper score: lambda = Lebesgue on [0,1/3] u [2/3,1]
def s1(x):  # int_{[x,1)} (1-q) dlambda
    x = Fr(x)
    def I(a,b):  # int_a^b (1-q) dq
        return (b - b*b/2) - (a - a*a/2) if b > a else Fr(0)
    return I(max(x,Fr(0)),Fr(1,3)) + I(max(x,Fr(2,3)),Fr(1))
def s0(x):  # int_{[0,x)} q dlambda
    x = Fr(x)
    def I(a,b): return (b*b-a*a)/2 if b > a else Fr(0)
    return I(Fr(0),min(x,Fr(1,3))) + I(Fr(2,3),max(min(x,Fr(1)),Fr(2,3)))
assert s0(0)==0 and s1(1)==0
for x in [Fr(1,3),Fr(2,5),Fr(1,2),Fr(3,5),Fr(2,3)]:
    assert s0(x)==Fr(1,18) and s1(x)==Fr(1,18), x
# propriety on a rational grid: G_t(y) >= G_t(t)
grid=[Fr(i,60) for i in range(61)]
for t in grid:
    Gt=lambda y: t*s1(y)+(1-t)*s0(y)
    m=Gt(t)
    assert all(Gt(y)>=m for y in grid)
# tie: events E, Omega\E; worlds (E true) and (E false)
def L(f):
    a,b=f
    return (s1(a)+s0(b), s0(a)+s1(b))
assert L((Fr(2,5),Fr(2,5)))==L((Fr(2,5),Fr(3,5)))
print("flat score: proper, constant 1/18 on [1/3,2/3]; tie profile", L((Fr(2,5),Fr(2,5))))

# 2. Score infinite inside (0,1)
def t0(y): return y/(Fr(1,2)-y) if y<Fr(1,2) else INF
def t1(y): return (1-y)/(y-Fr(1,2)) if y>Fr(1,2) else INF
prof=lambda y:(t1(Fr(y)),t0(Fr(y)))   # worlds (E, not E)
print("infinite-inside score: profile 0.3", prof(Fr(3,10)), " profile 0", prof(0))
assert prof(Fr(3,10))==(INF,Fr(3,2)) and prof(0)==(INF,0)
# G_t = inf for 0<t<1 everywhere; G_0 = t0 min at 0, G_1 = t1 min at 1
for y in grid:
    assert t0(y)==INF or t1(y)==INF
    assert t0(y)>=0 and t1(y)>=0
assert t1(Fr(1))==0

# 3. SSK Example 4
def g0(x): return x*x if x<=Fr(1,2) else Fr(1,2)+x*x
def g1(x): return Fr(1,2)+(1-x)**2 if x<=Fr(1,2) else (1-x)**2
L4=lambda f:(g1(f[0])+g0(f[1]), g0(f[0])+g1(f[1]))
f=(Fr(1,2),Fr(3,10)); Lf=L4(f)
assert Lf==(Fr(84,100),Fr(124,100)), Lf
# grid search for weak dominators of f (step 1/400) plus exact proof in paper
N=400; dom=[]
for i in range(N+1):
    for j in range(N+1):
        g=(Fr(i,N),Fr(j,N)); Lg=L4(g)
        if Lg[0]<=Lf[0] and Lg[1]<=Lf[1] and g!=f: dom.append(g)
print("Ex4: weak dominators of (1/2,3/10) on 1/400 grid:", dom[:5])
assert not dom
# (0.6,0.7): no coherent weak dominator
m=(Fr(3,5),Fr(7,10)); Lm=L4(m)
assert Lm==(Fr(115,100),Fr(95,100))
bad=[r for r in [Fr(i,1000) for i in range(1001)] if L4((r,1-r))[0]<=Lm[0] and L4((r,1-r))[1]<=Lm[1]]
assert not bad
print("Ex4: (0.6,0.7) profile",Lm,"no coherent weak dominator on grid")
# sum of jumps is 1 everywhere (used in the paper's proof)
for g in [(Fr(i,7),Fr(j,9)) for i in range(8) for j in range(10)]+[(Fr(1,2),Fr(1,2))]:
    x,y=g
    B=(1-x)**2+x*x+(1-y)**2+y*y
    assert sum(L4(g))==1+B

# 4. SSK Example 5
def h0(x): return x*x if x<=Fr(1,2) else Fr(1)
def h1(x): return Fr(1,2)+(1-x)**2 if x<=Fr(1,2) else Fr(0)
L5=lambda f:(h1(f[0])+h0(f[1]), h0(f[0])+h1(f[1]))
assert L5((Fr(1,2),Fr(7,10)))==(Fr(7,4),Fr(1,4))
# Bayes for prior (1/2,1/2): expected loss 1, V = 1
Vhalf=min(Fr(1,2)*h1(y)+Fr(1,2)*h0(y) for y in grid)*2
assert Vhalf==1 and sum(L5((Fr(1,2),Fr(7,10))))/2==1
assert L5((Fr(0),Fr(1)))==L5((Fr(0),Fr(7,10)))==(Fr(5,2),0)
print("Ex5: (1/2,7/10) profile (7/4,1/4) Bayes for (1/2,1/2); (0,1),(0,7/10) tied at (5/2,0)")

# 5. SSK Example 6 with g1(1/2)=1/4
def k0(x): return Fr(0) if x<Fr(1,2) else x*x
def k1(x): return Fr(1,2) if x<Fr(1,2) else (1-x)**2
# constituents C1=A1&A2, C2=A1&~A2, C3=~A1&A2, C4=A3; truth (A1,A2,A3)
truth=[(1,1,0),(1,0,0),(0,1,0),(0,0,1)]
def L6(q):
    out=[]
    for t in truth:
        tot=0
        for i in range(3):
            w=2 if i==2 else 1
            tot+=w*(k1(q[i]) if t[i] else k0(q[i]))
        out.append(tot)
    return out
assert L6((Fr(1,2),)*3)==[1,1,1,1] and L6((0,0,0))==[1,Fr(1,2),Fr(1,2),1]
print("Ex6: (1/2,1/2,1/2) ->",L6((Fr(1,2),)*3)," (0,0,0) ->",L6((0,0,0)))

# 6. SSK conditional forecasts, Brier, worlds A1B, A2B, B\(A1uA2), B^c
def LC(x,y):
    return ((1-x)**2+y*y, x*x+(1-y)**2, x*x+y*y, 0)
print("cond:",LC(Fr(9,10),Fr(7,10)),LC(Fr(3,5),Fr(2,5)))
assert LC(Fr(9,10),Fr(7,10))==(Fr(1,2),Fr(9,10),Fr(13,10),0)
assert LC(Fr(3,5),Fr(2,5))==(Fr(8,25),Fr(18,25),Fr(13,25),0)

# 7. Pettigrew enhanced log score, W={1,2}, F = (empty,{1},{2},W)
sets=[(),(1,),(2,),(1,2)]
def Lstar(c,i):
    tot=0.0
    for X,cx in zip(sets,c):
        if i in X: tot+= (INF if cx==0 else -math.log(cx))
        tot+=cx
    return tot
c=(0,0,0.5,1)
print("Pettigrew: L*(c)=",Lstar(c,1),Lstar(c,2)," L*(delta2)=",Lstar((0,0,1,1),1),Lstar((0,0,1,1),2))
# divergence D(p,c)=p.L*(c)-p.L*(p) for p=(t,1-t)
def D(t):
    p=(0,t,1-t,1)
    def E(x): return sum(w*Lstar(x,i) for w,i in ((t,1),(1-t,2)) if w>0)
    return E(c)-E(p)
assert D(0.0)<0.2 and all(D(t)==INF for t in [1e-9,0.1,0.5,1.0])
eps=0.1; pe=(0,eps,1-eps,1)
assert Lstar(pe,1)<INF and Lstar(pe,2)<Lstar(c,2)
print("projection is delta2 (D=%.4f), p_eps=(0.1,0.9) strictly dominates c"%D(0.0))
