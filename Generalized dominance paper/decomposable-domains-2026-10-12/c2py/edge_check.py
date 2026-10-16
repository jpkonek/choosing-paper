"""Exact behaviour of the two pencil conditions for the conic-family map W_I=(x,1,1/x) (vertex b=2, a=1, c=3, x+)
along the failing edge q=(s,1-s,0) and just inside it: F_k(q) = (W q).H_k(q) (zero <=> sigma(q) on L^k(q)),
with the R1 orientation fixed numerically by comparing with an admissible precise point."""
import sympy as sp
e = sp.Rational(3,10); kap=(1+2*e)/(1-e); x=((kap+1)+sp.sqrt((kap+1)**2-4))/2
c0=(1-e)/3; v=[sp.Matrix([c0+(e if i==k else 0) for i in range(3)]) for k in range(3)]
def corner(k,j):
    r=v[k].cross(v[j]); t=3-k-j
    return r if (r.T*v[t])[0]>0 else -r
def cvec(k,h):
    h1,h2,h3=h
    if k==0: return sp.Matrix([-(x*h2+h3),x*h2,h3])
    if k==1: return sp.Matrix([h1,-(h1+x*h3),x*h3])
    return sp.Matrix([x*h1,h2,-(x*h1+h2)])
s,eta=sp.symbols('s eta',positive=True)
q=sp.Matrix([s,1-s-eta,eta])
def H(k):
    i,j=[l for l in range(3) if l!=k]; r0,r1=corner(k,i),corner(k,j)
    return (cvec(k,r1).T*q)[0]*r0-(cvec(k,r0).T*q)[0]*r1
for name,W in [('W_I=(x,1,1/x)',(x,1,1/x)),('W_II=(kappa,1,kappa)',(kap,1,kap))]:
    Wq=sp.Matrix([W[i]*q[i] for i in range(3)])
    for k,lab in [(0,'pencil a (F_1)'),(2,'pencil c (F_3)')]:
        Fk=sp.expand((Wq.T*H(k))[0])
        on_edge=sp.factor(sp.simplify(Fk.subs(eta,0)))
        d_eta=sp.factor(sp.simplify(sp.diff(Fk,eta).subs(eta,0)))
        print(name,lab,": F on edge =",on_edge,";  dF/deta at edge =",d_eta, "; at s=1/100:",sp.N(d_eta.subs(s,sp.Rational(1,100))))
