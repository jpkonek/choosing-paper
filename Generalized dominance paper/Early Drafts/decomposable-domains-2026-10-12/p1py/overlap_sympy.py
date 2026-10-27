"""P1 CHECK (sympy): (1) pivot-normal parameters at the corner r31 from the two facet maps; overlap <=> x3+1/x1>k+1.
(2) mid-facet arc on F1: continuity of the normal across an arc forces b1/a1 = rho_b/rho_a > 1.
(3) Lemma P1.1 algebra on random samples (sanity)."""
import sympy as sp, random
k,x1,x3,a,b,ra,rb=sp.symbols('kappa x1 x3 a b rho_a rho_b',positive=True)
r31=sp.Matrix([-1,k+1,-1])
c1=lambda h,x: sp.Matrix([-(x*h[1]+h[2]),x*h[1],h[2]])
c3=lambda h,x: sp.Matrix([x*h[0],h[1],-(x*h[0]+h[1])])
t=lambda n: sp.simplify(-n[0]/(-n[0]-n[2]))       # param of (-,+,-) normals: 0 at (0,1,-1), 1 at (-1,1,0)
t3=t(c3(r31,x3)); t1=t(c1(r31,x1))
print("t3 =",t3,"  t1 =",t1)
print("t3-t1 =",sp.factor(sp.simplify(t3-t1)), " ; equals (x3+1/x1-(k+1))/(k+1):",
      sp.simplify(t3-t1-(x3+1/x1-(k+1))/(k+1))==0)
# (2) on F1 middle (h2,h3>0): normal param u=h3/(x h2+h3) with rho=h3/h2 -> u=rho/(x+rho)
u=lambda rho,x: rho/(x+rho)
print("arc continuity u_A(rho_a)=u_B(rho_b) <=> b/a = rho_b/rho_a :",
      sp.simplify(sp.solve(sp.Eq(u(ra,a),u(rb,b)),b)[0]-a*rb/ra)==0)
# (3) Lemma P1.1: no positive solution of x_k+1/x_{k+1}>=K+1, 1/K<=x_k x_{k+1}<=K
random.seed(0); bad=0
for _ in range(200000):
    K=1+random.random()*20; x=[10**random.uniform(-3,3) for _ in range(3)]
    ok=all(x[i]+1/x[(i+1)%3]>=K+1 and 1/K<=x[i]*x[(i+1)%3]<=K for i in range(3))
    bad+=ok
print("random samples satisfying the system (expect 0):",bad)
