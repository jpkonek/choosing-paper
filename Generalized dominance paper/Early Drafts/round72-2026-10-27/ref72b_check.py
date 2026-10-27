# REF72b quick numeric sanity checks (NUMERICS only)
import numpy as np
fk=lambda t: 2*t if t>=0 else t/2              # auditor kink
F1=lambda h: fk(h[0])+fk(h[1])                 # E1
print("E1 a,b,a+b:",F1((-3.5,1)),F1((1,-3.5)),F1((-2.5,-2.5)))
f2=lambda t: t if abs(t)<=1 else 2*t-np.sign(t) # E2
F2=lambda h: 2*f2(h[0])+f2(h[1])
print("E2 h, h/4:",F2((-2,3.6)),F2((-0.5,0.9)))
f4=lambda t: 2*t-abs(np.sin(t))
print("E4 h, h/2:",f4(np.pi+0.3)+f4(-np.pi), f4((np.pi+0.3)/2)+f4(-np.pi/2))
r=np.random.default_rng(1); x=r.normal(size=10**6)*5; y=r.normal(size=10**6)*5
print("E4 superadd min gap:",(f4(x+y)-f4(x)-f4(y)).min())
g5=lambda t: min(t,(1+t)/2)
print("E5 h,10h:",g5(-1)+g5(1.01), g5(-10)+g5(10.1))
# C1 violation for R_{s'}: removing B1 (mass 1.1m at (-1,-1.2)) and B2 (mass m at (1,.9))
m=1.0; B=[((-1,-1.2),1.1*m),((1,0.9),m)]
print("C1: world1 incr",-sum(w*c[0] for c,w in B)," world2 incr",-sum(w*fk(c[1]) for c,w in B))
# C2 dual: Q=conv{(.8,.2),(.2,.8)}, A about (2,-1),(-1,2)
for c in [(2,-1),(-1,2)]: print("P_Q at",c,min(.8*c[0]+.2*c[1],.2*c[0]+.8*c[1]))
# Main thm sign table check: on R1, S1 etc. world-1 and world-2 signs of adding/removing
