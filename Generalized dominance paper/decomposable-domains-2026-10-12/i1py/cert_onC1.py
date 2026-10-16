"""gamma vanishes for q on C_1 (perspective case) and pi_q(e1) = e1 there; check a1=mu1(e1) != e1."""
import mpmath as mp
from certificate import *
for eps in ['0.3','0.05']:
  for w in ['+','-']:
    ep,kap,V,x=setup(eps,w); u=vec(1,1,1)/3
    h=cross(V[0],E[0]); Cn=c1(h,x)
    # a direction along C_1 in aff: t = Cn x 1 projected
    tdir=cross(Cn,vec(1,1,1)); tdir=tdir/mp.sqrt(dot(tdir,tdir))
    n=Cn-sum(Cn)/3; n=n/mp.sqrt(dot(n,n))
    ys=[mp.mpf('0.52'),mp.mpf('0.54'),mp.mpf('0.56')] if w=='+' else [mp.mpf('0.96'),mp.mpf('0.97'),mp.mpf('0.98')]
    a1=mu(0,1,mp.mpf(0),V,x)   # prior image of e1 on E1 (s from e1)
    for name,q in [('on C1',u+mp.mpf('1e-3')*tdir),('off C1 +',u+mp.mpf('1e-3')*n),('off C1 -',u-mp.mpf('1e-3')*n)]:
        al,be,ga=gamma(q,ys,V,x)
        # pi_q(e1): line(q, a1-point) cap E2, then mu2^{-1}
        A1=pt(0,1,a1); y2=line_edge(q,A1,2,0); pe=mu_inv(2,0,y2,V,x)
        print(f"eps={eps} x{w}: a1=mu1(e1) at s={mp.nstr(a1,6)} (e1 is s=0); {name}: gamma={mp.nstr(ga,5)}  pi_q(e1) param on [e3,e1] from e3 = {mp.nstr(pe,12)} (e1 is 1)")
