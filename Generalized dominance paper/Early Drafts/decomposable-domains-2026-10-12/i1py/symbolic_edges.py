"""Exact edge maps for T1 (p*=u, PC data with parameter x, kappa=(1+2eps)/(1-eps)).
On edge [e1,e2], probability point z=(1-t,t,0) (t from e1), prior point (1-s,s,0).
For each facet k: Moebius map t -> s (chord of the facet-k line through z)."""
import sympy as sp
eps,x,t,s=sp.symbols('epsilon x t s',positive=True)
c0=(1-eps)/3
E=sp.eye(3)
V=[sp.Matrix([c0,c0,c0])+eps*E[:,k] for k in range(3)]
def cvec(k,h):
    h1,h2,h3=h
    if k==0: return sp.Matrix([-(x*h2+h3),x*h2,h3])
    if k==1: return sp.Matrix([h1,-(h1+x*h3),x*h3])
    return sp.Matrix([x*h1,h2,-(x*h1+h2)])
z=sp.Matrix([1-t,t,0])
mob={}
for k in range(3):
    h=z.cross(V[k])
    c=cvec(k,h)
    sk=sp.simplify(c[0]/(c[0]-c[1]))
    mob[k]=sk
    print(f"facet {k+1}: s = {sp.factor(sk)}")
    # value at t=0, t=1/2, t=1 and derivative at 0
    print("    s(0)=",sp.simplify(sk.subs(t,0))," s(1)=",sp.simplify(sk.subs(t,1)), " ds/dt(0)=",sp.factor(sp.diff(sk,t).subs(t,0))," ds/dt(1)=",sp.factor(sp.diff(sk,t).subs(t,1)))
