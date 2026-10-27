# AX72 numerical checks (exact where possible; floats elsewhere)
import numpy as np
from fractions import Fraction as Fr
np.random.seed(0)

def fk(t):   # auditor's kinked f
    return 2*t if t>=0 else t/2
def fodd(t): # odd, slope 1 on [-1,1], slope 2 outside
    return t if abs(t)<=1 else 2*t-np.sign(t)
def fsin(t): # superadditive, not homogeneous
    return 2*t-abs(np.sin(t))
def gcav(t): # concave, kink at 1, not homogeneous
    return t if t<=1 else (1+t)/2

print("== 1. R_s' : X*={h1+f(h2)>0}")
a=(Fr(-3,2),Fr(1)); b=(Fr(1),Fr(-3,2))
F=lambda h: h[0]+ (2*h[1] if h[1]>=0 else h[1]/2)
print(" F(a),F(b),F(a+b) =",F(a),F(b),F((a[0]+b[0],a[1]+b[1])))

print("== 2. C1 counterexample: common kinked f, p=(1/2,1/2)")
F2=lambda h: fk(h[0])+fk(h[1])
a=(-3.5,1.0); b=(1.0,-3.5)
print(" F(a),F(b),F(a+b) =",F2(a),F2(b),F2((a[0]+b[0],a[1]+b[1])))

print("== 3. C1+C2 counterexample: odd f, p=(2/3,1/3)")
F3=lambda h: 2*fodd(h[0])+fodd(h[1])
h=(-2.0,3.6); print(" F(h)=",F3(h)," F(h/4)=",F3((h[0]/4,h[1]/4)))
# oddness and sign
ts=np.linspace(-5,5,2001); print(" odd:",np.allclose([fodd(-t) for t in ts],[-fodd(t) for t in ts]))

print("== 4. C3a counterexample f=2t-|sin t|")
xs=np.random.uniform(-20,20,(200000,2))
sup=[fsin(x+y)-fsin(x)-fsin(y) for x,y in xs]
print(" min superadditivity gap:",min(sup))
r=[fsin(t)/t for t in np.linspace(-30,30,60001) if abs(t)>1e-9]
print(" weight range f(t)/t:",min(r),max(r))
print(" increasing:",np.all(np.diff([fsin(t) for t in np.linspace(-30,30,60001)])>0))
F4=lambda h: fsin(h[0])+fsin(h[1])
h=(np.pi+0.3,-np.pi); print(" F(h)=",F4(h)," F(h/2)=",F4((h[0]/2,h[1]/2)))

print("== 5. C3b counterexample g concave, kink at 1")
F5=lambda h: gcav(h[0])+gcav(h[1])
h=(-1.0,1.01); print(" F(h)=",F5(h)," F(10h)=",F5((10*h[0],10*h[1])))
mid=[2*gcav((x+y)/2)-gcav(x)-gcav(y) for x,y in xs]; print(" min midpoint-concavity gap:",min(mid))
sa=[gcav(x+y)-gcav(x)-gcav(y) for x,y in xs]; print(" min superadditivity gap (expected <0):",min(sa))

print("== 6. R0 violates C2 (symmetric mu): A = balls at (2,-1),(-1,2)")
q1=np.array([.8,.2]); q2=np.array([.2,.8])
for v in [(2,-1),(-1,2)]:
    v=np.array(v); print("  P_Q(v)=",min(q1@v,q2@v))
# -A inconsistent: need q with q.(-2,1)>=0 and q.(1,-2)>=0
ps=np.linspace(0,1,100001); ok=[(p*-2+(1-p)*1>=0) and (p*1+(1-p)*-2>=0) for p in ps]; print("  -A consistent?",any(ok))
