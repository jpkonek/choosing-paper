"""I1 referee: independent numerical checks on T1 (own implementation, no import from i1py).

For each eps on a grid (and eps=1/7, where a2 is at infinity):
 (1) edge maps mu_o on every edge, both orientations: increasing homeomorphisms fixing 0,1 (Lemma 2(a));
     which facet supplies the tangent, and where the piece boundary is (expected c0 / 1-c0);
 (2) Prop E at m12: Z_2(m12)=(1-eps)/(2+eps), Z_1(m12)=(1+2eps)/(2+eps), non-failing;
 (3) the non-failing set of every edge (crossover points);
 (4) Lemma W window + Theorem I1 certificate, using the FULL piecewise maps (tangent selection +
     bisection, no Moebius fitting): gamma(q) on both sides of C1 at q=u +- r n, r=1e-4,1e-6,
     with all admissibility conditions checked at those q.
"""
import numpy as np
E=np.eye(3); u=np.ones(3)/3
def setup(eps):
    kap=(1+2*eps)/(1-eps); c0=(1-eps)/3
    V=[c0*np.ones(3)+eps*E[k] for k in range(3)]
    xp=((kap+1)+np.sqrt((kap+1)**2-4))/2
    return kap,c0,V,xp
def cvec(k,h,x):
    h1,h2,h3=h
    return [np.array([-(x*h2+h3),x*h2,h3]),np.array([h1,-(h1+x*h3),x*h3]),np.array([x*h1,h2,-(x*h1+h2)])][k]
def tangent(z,V,o,oth):
    """facet gamble through z tangent to T1 (T1 on + side) with h_o>0>h_oth; returns (k,h)"""
    res=[]
    for k in range(3):
        h=np.cross(z,V[k])
        vals=np.array([h@V[l] for l in range(3) if l!=k])
        if np.all(vals>=-1e-13): pass
        elif np.all(vals<=1e-13): h=-h
        else: continue
        if h[o]>0>h[oth]: res.append((k,h))
    return res
def mu(edge,o,t,V,x):
    i,j=edge; oth=j if o==i else i
    z=(1-t)*E[i]+t*E[j]
    r=tangent(z,V,o,oth)
    k,h=r[0]
    c=cvec(k,h,x)
    return c[i]/(c[i]-c[j]),k
def Zinv(edge,o,s,V,x,it=70):
    a,b=0.0,1.0
    for _ in range(it):
        m=(a+b)/2
        if mu(edge,o,m,V,x)[0]<s: a=m
        else: b=m
    return (a+b)/2
EDGES=[(0,1),(1,2),(2,0)]
def report(eps,x,V,c0,verbose=False):
    out=[]
    # (1) monotone / endpoints / pieces
    ts=np.linspace(1e-4,1-1e-4,2001)
    ok=True; pieces={}
    for ed in EDGES:
        for o in ed:
            vals=[mu(ed,o,t,V,x) for t in ts]
            m=np.array([v[0] for v in vals]); ks=np.array([v[1] for v in vals])
            ok&=bool(np.all(np.diff(m)>0)) and abs(m[0])<5e-2 and abs(m[-1]-1)<5e-2
            ch=np.where(np.diff(ks)!=0)[0]
            pieces[(ed,o)]=([int(ks[0])+1,int(ks[-1])+1],[round(ts[c],4) for c in ch])
    out.append(f"  monotone+endpoints all edges/orientations: {ok}")
    out.append(f"  pieces on E1=[e1,e2] toward e2 (facets, boundary t): {pieces[((0,1),1)]}  expected boundary c0={c0:.4f}")
    out.append(f"  pieces on E2=[e3,e1] toward e3 (t from e3): {pieces[((2,0),2)]}  expected boundary 1-c0={1-c0:.4f}")
    # (2) Prop E at m12
    Z2=Zinv((0,1),1,0.5,V,x); Z1=Zinv((0,1),0,0.5,V,x)
    out.append(f"  m12: Z2={Z2:.6f} (pred {(1-eps)/(2+eps):.6f}), Z1={Z1:.6f} (pred {(1+2*eps)/(2+eps):.6f}), nonfail={Z2<Z1}")
    # (3) crossover of Z_j - Z_i per edge
    for ed in EDGES:
        i,j=ed
        ss=np.r_[np.linspace(0.002,0.99,250),np.linspace(0.991,0.99995,60)]
        g=np.array([Zinv(ed,j,s0,V,x,40)-Zinv(ed,i,s0,V,x,40) for s0 in ss])
        cr=ss[np.where(np.diff(np.sign(g))!=0)[0]]
        out.append(f"  edge e{i+1}e{j+1}: Zj<Zi near s=0: {g[0]<0}; near s=1: {g[-1]<0}; crossovers {np.round(cr,3)}")
    return out
def forced_line(q,y,V,x):
    """Lemma S for Lam=line(q, Y), Y=(1-y)e1+y e2 on E1, second crossing on E2=[e3,e1].
    returns oriented gamble g (e2,e3 on + side) and admissibility data"""
    Y=(1-y)*E[0]+y*E[1]
    d=Y-q
    # q + l d on E2 : second coordinate zero
    l=-q[1]/d[1]; P=q+l*d; y2=P[0]       # param from e3 toward e1 is first coordinate
    adm={}
    # orientation: e2 positive on E1 -> o=1 ; e3 positive on E2 -> o=2
    z1=Zinv((0,1),1,y,V,x); z2=Zinv((2,0),2,y2,V,x)
    adm['y1_nonfail']=z1<Zinv((0,1),0,y,V,x)
    adm['y2_nonfail']=Zinv((2,0),0,y2,V,x)<z2   # edge (i,j)=(e3,e1): nonfail iff Z_{e1}<Z_{e3}
    adm['facet1_at_z1']=mu((0,1),1,z1,V,x)[1]==0
    adm['facet1_at_z2']=mu((2,0),2,z2,V,x)[1]==0
    adm['y2_in_relint']=0<y2<1 and abs(P[2]+P[0]-1)<1e-12
    Z1=(1-z1)*E[0]+z1*E[1]; Z2=(1-y2*0)*0+(1-z2)*E[2]+z2*E[0]
    g=np.cross(Z1,Z2)
    if g@E[1]<0: g=-g
    adm['e3_pos']=g@E[2]>0 and g@E[0]<0
    return g,adm,(z1,y2,z2)
def gamma(q,ys,V,x):
    G=[];A=True
    for y in ys:
        g,adm,_=forced_line(q,y,V,x); G.append(g); A&=all(adm.values())
    M=np.c_[G[0],G[2],np.ones(3)]
    al,be,ga=np.linalg.solve(M,G[1])
    return al,be,ga,A
if __name__=="__main__":
    grid=[0.005,0.02,0.05,1/7,0.2,0.3,0.45,0.6,0.75,0.9,0.97,0.995]
    for eps in grid:
        kap,c0,V,xp=setup(eps); x=xp
        print(f"eps={eps:.4f} kappa={kap:.4f} x+={x:.5f}")
        for line in report(eps,x,V,c0): print(line)
        C=cvec(0,np.array([0,1,-1.0]),x); n=C-C.mean(); n/=np.linalg.norm(n)
        print(f"  C1 normal n={np.round(n,4)}, C1.u={C@u:.1e}, C1.e1={C[0]:.4f}")
        for dy in [0.01,0.003]:
            ys=[0.5+dy,0.5+2*dy,0.5+3*dy]
            res=[]
            for r in [1e-4,1e-6]:
                for sg in [1,-1]:
                    al,be,ga,A=gamma(u+sg*r*n,ys,V,x)
                    res.append(f"r={r:.0e},{'+' if sg>0 else '-'}: al={al:.3f} be={be:.3f} ga/r={ga/r:+.4e} adm={A}")
            fl=forced_line(u,ys[1],V,x); res.append(f"adm flags at u (middle line): {fl[1]}  (z1,y2,z2)={np.round(fl[2],4)}")
            print(f"  window y={np.round(ys,3)}:"); [print("     ",z) for z in res]
