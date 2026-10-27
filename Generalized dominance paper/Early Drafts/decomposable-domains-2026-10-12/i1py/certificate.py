"""I1 Theorem 3 certificate (NUMERICS illustrating the proof; the proof itself is analytic).

Facet F_1 of T1 at p*=u, (PC) data x in {x+,x-}.  Middle window: facet lines through v_1 near
line(v_1,e_3) (x+) or near line(v_1,e_2) (x-), with e_1 on the - side.  They cross E1=[e1,e2] and
E2=[e3,e1].  mu1, mu2 = facet-1 Moebius maps (prob edge point -> prior edge point of its chord).
For q near u and three prior lines Lam_i = line(q, y_i), y_i in E1 (window), the forced supporting
lines of K_q are  L_i = line(z_i, pi_q(z_i)),  z_i = mu1^{-1}(y_i),
pi_q(z) = mu2^{-1}( line(q, mu1(z)) cap E2 ).
Certificate: write g2 = al g1 + be g3 + ga 1 (al,be>0); ga = g2(L1 cap L3).  ga>0 => no convex K_q.
We print ga at q = u + r n and u - r n (n normal to C_1, the chord of line(v_1,e_1)), and
pi_q(e1)-e1 (zero iff q in C_1)."""
import mpmath as mp
mp.mp.dps=40
def vec(*a): return mp.matrix([mp.mpf(t) for t in a])
def cross(a,b): return mp.matrix([a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]])
def dot(a,b): return sum(a[i]*b[i] for i in range(3))
E=[vec(1,0,0),vec(0,1,0),vec(0,0,1)]
def setup(eps,which):
    eps=mp.mpf(eps); kap=(1+2*eps)/(1-eps); c0=(1-eps)/3
    V=[mp.matrix([c0+(eps if i==k else 0) for i in range(3)]) for k in range(3)]
    s=kap+1; xp=(s+mp.sqrt(s*s-4))/2; x=xp if which=='+' else 1/xp
    return eps,kap,V,x
def c1(h,x):   # facet-1 chart vector (Contamination Triangle, Prop T1 normalisation)
    return mp.matrix([-(x*h[1]+h[2]),x*h[1],h[2]])
def pt(i,j,t): # (1-t)e_i + t e_j
    return (1-t)*E[i]+t*E[j]
def mu(i,j,t,V,x):   # facet-1 Moebius map on edge (i,j): prob t -> prior s
    z=pt(i,j,t); h=cross(z,V[0]); c=c1(h,x)
    return c[i]/(c[i]-c[j])
def mu_inv(i,j,s,V,x):
    # mu is Moebius in t: fit s=(a t+b)/(c t+1) exactly from 3 points, invert
    ts=[mp.mpf('0.2'),mp.mpf('0.5'),mp.mpf('0.8')]; ss=[mu(i,j,t,V,x) for t in ts]
    A=mp.matrix([[t,1,-t*s_] for t,s_ in zip(ts,ss)]); a,b,c=mp.lu_solve(A,mp.matrix(ss))
    return (s-b)/(a-c*s)
def line_edge(q,y,i,j):  # line(q,y) cap edge (i,j) -> parameter
    # solve (1-t)e_i+t e_j = q + l (y-q)
    A=mp.matrix([[E[j][k]-E[i][k], -(y[k]-q[k])] for k in range(3)])
    rhs=mp.matrix([q[k]-E[i][k] for k in range(3)])
    sol=mp.lu_solve(A[0:2,:],rhs[0:2]); return sol[0]
def L(q,y_s,V,x):
    """forced supporting line for Lam=line(q,y), y=pt(0,1,y_s) on E1; returns gamble g (oriented: e1 on - side)"""
    y=pt(0,1,y_s)
    z1=mu_inv(0,1,y_s,V,x)
    y2=line_edge(q,y,2,0)                 # prior crossing with E2=[e3,e1] (param from e3)
    z2=mu_inv(2,0,y2,V,x)
    g=cross(pt(0,1,z1),pt(2,0,z2))
    if g[0]>0: g=-g
    return g,(z1,y2,z2)
def gamma(q,ys,V,x):
    g1,_=L(q,ys[0],V,x); g2,_=L(q,ys[1],V,x); g3,_=L(q,ys[2],V,x)
    M=mp.matrix([[g1[k],g3[k],1] for k in range(3)])
    al,be,ga=mp.lu_solve(M,g2)
    return al,be,ga
if __name__=="__main__":
    for eps in ['0.05','0.3','0.6','0.9']:
        for w in ['+','-']:
            ep,kap,V,x=setup(eps,w)
            u=vec(1,1,1)/3
            # C_1: chord of line(v_1,e_1)
            h=cross(V[0],E[0]); Cn=c1(h,x)          # chord {Cn.q=0}
            n=Cn-sum(Cn)/3; n=n/mp.sqrt(dot(n,n))  # normal direction in 1-perp
            # window: chords near line(u,e3) (x+) cross E1 near midpoint; near line(u,e2) (x-) cross E1 near e2
            if w=='+': ys=[mp.mpf('0.52'),mp.mpf('0.54'),mp.mpf('0.56')]
            else:      ys=[mp.mpf('0.96'),mp.mpf('0.97'),mp.mpf('0.98')]
            out=[]
            for r in ['1e-3','1e-5']:
                r=mp.mpf(r)
                for sg in [1,-1]:
                    q=u+sg*r*n
                    al,be,ga=gamma(q,ys,V,x)
                    out.append(f"r={mp.nstr(r,2)} side={sg:+d}: al={mp.nstr(al,4)} be={mp.nstr(be,4)} ga/r={mp.nstr(ga/r,6)}")
            # window info at q=u
            _,(z1,y2,z2)=L(u,ys[1],V,x)
            print(f"eps={eps} x{w}={mp.nstr(x,6)}: window y1={mp.nstr(ys[1],3)} on [e1,e2], y2={mp.nstr(y2,4)} on [e3,e1] (from e3), z1={mp.nstr(z1,4)}, z2={mp.nstr(z2,4)}")
            for o in out: print("    ",o)
