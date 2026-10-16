"""M0 referee, check 3 (sanity for Prop R, Steps A-B; elementary).
For T1 at several eps and random credal polygons K (containing K'), at each of the six crossings w (w_c=0):
 - if P_K(w)>0 then g1=w-s(1-e_c) has g1_c=0, P_T1(g1)<0<P_K(g1)  (a ball centred on {g_c=0} in D_K \ cl D_T1);
 - if P_K(w)<0 then g2=w+s(1-e_c) has g2_c=0, P_K(g2)<0<P_T1(g2) (a ball centred on {g_c=0} in D_T1 \ cl D_K);
 - along each facet, tau -> P_K(h(tau)) is concave, so zeros at both crossings force P_K<=0 on the corner portions.
"""
import numpy as np
rng=np.random.default_rng(3)
def PK(V,g): return (V@g).min()
bad=0; tests=0; conc_bad=0
for eps in [0.05,0.3,0.7,0.95]:
    c0=(1-eps)/3; T=np.array([c0*np.ones(3)+eps*np.eye(3)[k] for k in range(3)]); u=np.ones(3)/3
    Kp=u+0.5*(T-u); kap=(1+2*eps)/(1-eps)
    r12=np.array([-1,-1,kap+1.]); r23=np.array([kap+1,-1,-1.]); r31=np.array([-1,kap+1,-1.])
    F=[(r31,r12),(r12,r23),(r23,r31)]
    for trial in range(400):
        m=rng.dirichlet(np.ones(3),size=rng.integers(1,5))
        K=np.vstack([Kp,m])
        for k,(r,rp) in enumerate(F):
            ts=np.linspace(0,1,4001); H=(1-ts)[:,None]*r+ts[:,None]*rp
            phi=np.array([PK(K,h) for h in H])
            # concavity check on grid
            d2=phi[2:]-2*phi[1:-1]+phi[:-2]; conc_bad+= (d2>1e-9).any()
            for c in [i for i in range(3) if i!=k]:
                j=np.argmin(np.abs(H[:,c])); t0=ts[j]
                # exact crossing by linear interpolation
                a,b=r[c],rp[c]; tc=a/(a-b); w=(1-tc)*r+tc*rp
                pw=PK(K,w); s=1e-3*abs(pw) if pw!=0 else 0
                if pw>0:
                    g=w-s*(1-np.eye(3)[c]); tests+=1
                    bad+= not (abs(g[c])<1e-12 and PK(T,g)<0<PK(K,g))
                elif pw<0:
                    g=w+s*(1-np.eye(3)[c]); tests+=1
                    bad+= not (abs(g[c])<1e-12 and PK(K,g)<0<PK(T,g))
print(f"crossing-ball constructions tested: {tests}, failures: {bad}; non-concave facet profiles: {conc_bad}")
