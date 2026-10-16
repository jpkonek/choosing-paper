"""I1 referee: independent symbolic checks (sympy).
(a) Lemma 1 on F_1 (endpoint test of the affine function x h2 + h3 along the facet segment).
(b) Facet-1 Moebius maps on E1=[e1,e2] and E2=[e3,e1]; mu1(e1)=a1=C1 cap E1, mu2(e1)=a2=C1 cap E2.
(c) Lemma P(4): c1(h*) for h*=(0,1,-1).
(d) Lemma D: det of three lines through (X_i,0),(0,pi(X_i)); D|_{b=0}=0 and d_b D at b=0.
(e) gamma vs D: value of line-2 functional at L1 cap L3 is det/(cross-term).
"""
import sympy as sp
eps,x,t,s=sp.symbols('epsilon x t s',real=True)
kap=(1+2*eps)/(1-eps); c0=(1-eps)/3
v=[sp.Matrix([c0+(eps if i==k else 0) for i in range(3)]) for k in range(3)]
e=[sp.Matrix([1 if i==k else 0 for i in range(3)]) for k in range(3)]
def c1(h): return sp.Matrix([-(x*h[1]+h[2]),x*h[1],h[2]])
# (a) facet segment of F_1 between corner rays r31=(-1,k+1,-1) and r12=(-1,-1,k+1)
r31=sp.Matrix([-1,kap+1,-1]); r12=sp.Matrix([-1,-1,kap+1])
print("(a) r31.v1, r31.v3 =",sp.simplify(r31.dot(v[0])),sp.simplify(r31.dot(v[2])),"; r12.v1, r12.v2 =",sp.simplify(r12.dot(v[0])),sp.simplify(r12.dot(v[1])))
for name,r in [('r31',r31),('r12',r12)]:
    print("    x h2+h3 at",name,"=",sp.simplify(x*r[1]+r[2]))
print("    => -c1_1>0 on the whole closed segment iff 1/(k+1) < x < k+1 (affine in tau); x+- satisfy x+1/x=k+1 so both hold.")
# (b) facet-1 Moebius maps
def mu_edge(i,j,tt):
    z=(1-tt)*e[i]+tt*e[j]; h=z.cross(v[0]); c=c1(h)
    return sp.simplify(c[i]/(c[i]-c[j]))
m1=mu_edge(0,1,t)   # E1, t from e1, s from e1
m2=mu_edge(2,0,t)   # E2, t from e3, s from e3
print("(b) facet-1 map on E1 (from e1): s =",sp.factor(m1))
print("    s(0)=",sp.simplify(m1.subs(t,0)),"  s(1)=",sp.simplify(m1.subs(t,1)))
print("    facet-1 map on E2 (from e3): s =",sp.factor(m2))
print("    s(0)=",sp.simplify(m2.subs(t,0)),"  s(1)=",sp.simplify(m2.subs(t,1)))
hstar=sp.Matrix([0,1,-1])
print("    h*.v1 =",sp.simplify(hstar.dot(v[0])),"; h*.v2 =",sp.simplify(hstar.dot(v[1])),"; h*.v3 =",sp.simplify(hstar.dot(v[2])),"(h* not a facet gamble: line(v1,e1) cuts T1)")
C=c1(hstar)
print("(c) c1(h*) =",list(C),"; c1(h*).e1 =",C[0],"  => C1 contains e1 iff x=1")
# C1 cap E1, C1 cap E2
a1=sp.solve(sp.Eq(C[0]*(1-s)+C[1]*s,0),s)[0]
a2=sp.solve(sp.Eq(C[2]*(1-s)+C[0]*s,0),s)[0]   # E2 from e3: (1-s)e3+s e1
print("    a1 (param on E1 from e1) =",sp.simplify(a1),"  mu1(e1)-a1 =",sp.simplify(m1.subs(t,0)-a1))
print("    a2 (param on E2 from e3) =",sp.simplify(a2),"  mu2(e1)-a2 =",sp.simplify(m2.subs(t,1)-a2),"(a2 infinite iff x=2, i.e. eps=1/7 for x+)")
# (d) Lemma D
a,b,cc,d=sp.symbols('a b c d'); X=sp.symbols('X1:4')
pi=lambda XX:(a*XX+b)/(cc*XX+d)
rows=[[1/XX,1/pi(XX),-1] for XX in X]
D=sp.Matrix(rows).det()
print("(d) D at b=0:",sp.simplify(D.subs(b,0)))
dD=sp.simplify(sp.diff(D,b).subs(b,0))
w=[1/XX for XX in X]
target=d/a**2*(w[0]-w[1])*(w[1]-w[2])*(w[2]-w[0])
print("    d_b D at b=0 minus (d/a^2)(w1-w2)(w2-w3)(w3-w1) =",sp.simplify(dD-target))
# (e) gamma vs D: lines l_i=(A_i,B_i,C_i) meaning A X + B Y + C = 0. P=l1 x l3 (homog); l2.P = det(l1,l2,l3) up to sign
l=[sp.Matrix(r) for r in rows]
P=l[0].cross(l[2])
print("(e) l2.(l1 x l3) + det(l1,l2,l3) =",sp.simplify(l[1].dot(P)+sp.Matrix.hstack(l[0],l[1],l[2]).T.det()), " (so gamma = -D/P_3 times orientation/normalisation factors; P_3 != 0 iff L1,L3 not parallel)")
# corner equation and x+-
xp=((kap+1)+sp.sqrt((kap+1)**2-4))/2
for ev in [sp.Rational(1,100),sp.Rational(1,7),sp.Rational(3,10),sp.Rational(99,100)]:
    xv=xp.subs(eps,ev); kv=kap.subs(eps,ev)
    print(f"    eps={ev}: x+={sp.N(xv,8)}, kappa={sp.N(kv,8)}, 1<x+<k+1: {bool(1<xv<kv+1)}, kx+^2>1: {bool(kv*xv**2>1)}")
