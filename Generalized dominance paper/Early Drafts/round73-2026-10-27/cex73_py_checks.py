import numpy as np
rng=np.random.default_rng(0)
# Staircase X = {h : exists k in Z with h1 > -2^k and h2 > 2^k}
def inX(h):
    h1,h2=h
    if h2<=0: return False
    if h1>0: return True
    # need k with 2^k < h2 and 2^k < -h1... i.e. -2^k < h1 means 2^k > -h1
    # condition: exists k: -h1 < 2^k < h2
    lo,hi=-h1,h2
    if lo>=hi: return False
    k=np.floor(np.log2(hi))
    return 2.0**k>lo or 2.0**(k-1)>lo
# 1. pair in X with sum outside
d=0.02
x=np.array([-1+d,1+2*d]); y=np.array([-0.5+2*d,0.5+d])
print("x in X",inX(x),"y in X",inX(y),"x+y in X",inX(x+y),"x+y=",x+y)
# 2. upward closed, halving-closed, X+X misses Q--  (random tests)
bad_up=bad_half=bad_qmm=0
pts=rng.normal(size=(200000,2))*2
P=[p for p in pts if inX(p)]
P=np.array(P)
for i in range(50000):
    a=P[rng.integers(len(P))]; b=P[rng.integers(len(P))]; q=np.abs(rng.normal(size=2))
    if not inX(a+q): bad_up+=1
    if not inX(a/2+q/2): bad_half+=1
    s=a+b
    if s[0]<0 and s[1]<0: bad_qmm+=1
print("upward fails",bad_up,"half+pos fails",bad_half,"sum in Q-- ",bad_qmm)
# 3. X not a cone: (−1.5,1.6) in X? scale
z=np.array([-1.2,1.3]); print("z",inX(z),"1.5z",inX(1.5*z))
# 4. Prop B feasibility: reflex removal with loss-averse s (c<=d)
for (c1,d1,c2,d2) in [(1,1,1,1),(1,3,1,2),(0.5,4,0.2,5)]:
    a=np.array([-2,1.]); b=np.array([1,-2.])  # reflex pair (|a1||b2|=4 > a2 b1=1)
    lo=c1*b[0]/(d1*abs(a[0])); hi=d2*abs(b[1])/(c2*a[1])
    print("c,d",(c1,d1,c2,d2),"mass ratio window",lo,hi,"feasible",lo<hi)
