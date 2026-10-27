# MU73 sanity numerics (small). Gaussian mu on R^2 unless stated.
import numpy as np
rng=np.random.default_rng(73)
def ball(c,r,N):              # uniform in sup-norm ball, reweighted by Gaussian density (importance weights)
    P=c+r*(2*rng.random((N,2))-1); w=np.exp(-(P**2).sum(1)/2)/(2*np.pi)*(2*r)**2; return P,w
f2=lambda t: np.where(t>=0,2*t,t/2)          # auditor's distortion at world 2

print("== 1. Margin (set-wise) triples vs R_s' : x~a, y~b, z~a+b+delta*1 ==")
a=np.array([-1.5,1.]); b=np.array([1.,-1.5])
for kind,c in [("sum",1.),("mid",2.)]:
    for delta,r in [(0.2,0.02),(0.05,0.005)]:
        z0=(a+b)/c+delta
        # per unit of mass: split minus consolidated, with G3 of mass c*m; use product coupling
        X,_=ball(a,r,20000); Y,_=ball(b,r,20000); Z,_=ball(z0,r,20000)
        assert np.all(Z.min(0)[None,:]-(X.max(0)+Y.max(0))[None,:]/c>0)   # every z beats every (x+y)/c
        d1=np.mean(X[:,0])+np.mean(Y[:,0])-c*np.mean(Z[:,0])
        d2=np.mean(f2(X[:,1]))+np.mean(f2(Y[:,1]))-c*np.mean(f2(Z[:,1]))
        print(f"  {kind} delta={delta} r={r}: split increment per unit mass  world1={d1:+.4f}  world2={d2:+.4f}")

print("== 2. R0 / VB inequalities on random margin triples (Gaussian, product coupling) ==")
worst_m=np.inf; worst_veto=np.inf; worst_b=np.inf
p=np.array([.5,.5]); eps=.4
V=[(1-eps)*p+eps*np.eye(2)[i] for i in range(2)]
for _ in range(400):
    c=rng.choice([1.,2.]); x0=rng.normal(size=2)*1.5; y0=rng.normal(size=2)*1.5
    delta=rng.uniform(.05,.5); r=delta/8; z0=(x0+y0)/c+delta
    X,_=ball(x0,r,3000); Y,_=ball(y0,r,3000); Z,_=ball(z0,r,3000)
    # m(G3)-m(G1)-m(G2) per unit mass of G1 (G3 has mass c*m)
    dm=c*Z.mean(0)-X.mean(0)-Y.mean(0); worst_m=min(worst_m,dm.min())
    for v in V:   # VB veto a_i: consolidated minus split should be <=0 ; Brier b_i should drop
        veto=lambda H: np.maximum(-H@v,0).mean()
        worst_veto=min(worst_veto, veto(X)+veto(Y)-c*veto(Z))
    worst_b=min(worst_b,dm.min())
print(f"  min over trials of m-increment (consolidated - split), all worlds: {worst_m:.4f} (>0 expected)")
print(f"  min over trials of veto(split)-veto(consolidated): {worst_veto:.4f} (>=0 expected)")

print("== 3. Linearised type of the exact-triple PDE (2D): elliptic iff rho^-1/2 at x,y,x+y form a triangle ==")
rho=lambda h: np.exp(-(h**2).sum()/2)/(2*np.pi)
def typ(x,y,kind="sum"):
    al=rho(x)/rho(y)
    if kind=="sum": be=rho(x)/rho(x+y)
    else: be=8*rho(x)/rho((x+y)/2)
    t=be-1-al; disc=t*t-4*al
    return "elliptic" if disc<0 else ("parabolic" if disc==0 else "hyperbolic"), al, be
for x,y in [(a,b),(np.array([.3,.1]),np.array([.6,.2])),(np.array([1.,0.]),np.array([2.,0.])),(np.array([2.,.5]),np.array([.5,2.]))]:
    for kind in ["sum","mid"]:
        print("  ",x,y,kind,typ(x,y,kind)[0])
L=np.array([[np.cos(2*np.pi/3),-np.sin(2*np.pi/3)],[np.sin(2*np.pi/3),np.cos(2*np.pi/3)]])
print("  Lebesgue sum model L=R120: det L, det(I+L) =",round(np.linalg.det(L),12),round(np.linalg.det(np.eye(2)+L),12))
l1,l2=3+2*np.sqrt(2),3-2*np.sqrt(2); Lm=np.diag([l1,l2])
print("  Lebesgue midpoint model L=diag(3+-2sqrt2): det L, det((I+L)/2) =",round(np.linalg.det(Lm),12),round(np.linalg.det((np.eye(2)+Lm)/2),12))

print("== 4. Loss-averse kinked scores: Bayes set = D_Q for Q = normalised {p_w c_w : c_w in [a_w,b_w]} ==")
aw=np.array([1.,.7]); bw=np.array([2.,3.]); pw=np.array([.4,.6])
H=rng.normal(size=(200000,2))*3
F=(pw*(aw*np.maximum(H,0)-bw*np.maximum(-H,0))).sum(1)
ext=[pw*np.array([c1,c2]) for c1 in (aw[0],bw[0]) for c2 in (aw[1],bw[1])]
lower=np.min(np.stack([H@(e/e.sum()) for e in ext]),0)
print("  disagreements sign(F>0) vs sign(lower>0):",int(((F>0)!=(lower>0)).sum()),"of",len(H))

print("== 5. (M3) failure: mu on balls about a,b,n; X*=B(a)uB(b) ==")
n=np.array([-1.,-1.]); r=.05; cen={'a':a,'b':b,'n':n}
qs=np.linspace(0,1,100001); ok=[(q1*h[0]+(1-q1)*h[1]) for q1 in [0] for h in []]
both=[(q*(a[0]-r)+(1-q)*(a[1]-r)>0) and (q*(b[0]-r)+(1-q)*(b[1]-r)>0) for q in qs]
print("  any q in simplex positive on both balls (conservatively)?",any(both))
hits=[]
for k1 in cen:
  for k2 in cen:
    for c in (1.,2.):
      s=(cen[k1]+cen[k2])/c
      for k3 in cen:
        # z must exceed (x+y)/c at every world, all within radius r: need z-centre >= s-centre - 3r componentwise
        if np.all(cen[k3]-s>-3*r): hits.append((k1,k2,k3,c))
print("  support triples (x-ball,y-ball,z-ball,c) admitting a margin consolidation:",hits)
ca,cb=3.,1/3.
print("  Bayes values at centres (p=1/2): a:",.5*(a[0]+ca*a[1])," b:",.5*(b[0]+cb*b[1])," n:",.5*(n[0]+n[1]))
# worst-case check of every margin-consolidation constraint for R_g in the (M3)-failure example
g={'a':lambda h:(h[0],ca*h[1]),'b':lambda h:(h[0],cb*h[1]),'n':lambda h:(h[0],h[1])}
corners=lambda k:[cen[k]+r*np.array([s1,s2]) for s1 in(-1,1) for s2 in(-1,1)]
worst=np.inf
for (k1,k2,k3,c) in hits:
    for x in corners(k1):
        for y in corners(k2):
            for z in corners(k3):
                if np.all(z-(x+y)/c>0):
                    for w in (0,1):   # g linear on each ball, so corners give the extremes
                        worst=min(worst,c*g[k3](z)[w]-g[k1](x)[w]-g[k2](y)[w])
print("  min over constraints of [c*g(z)-g(x)-g(y)] (>=0 means R_g satisfies C3-set):",round(worst,4))
