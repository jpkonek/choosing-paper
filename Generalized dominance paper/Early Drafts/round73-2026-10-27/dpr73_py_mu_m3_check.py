# Check: in MU73 sec 1.3 (mu = Lebesgue on three sup-balls), every margin triple
# has c*g_w(z) - g_w(x) - g_w(y) > 0 at both worlds (so R_g accepts every margin
# consolidation at both worlds, i.e. satisfies CAm).
import numpy as np, itertools
rng=np.random.default_rng(0)
r=0.05
C={'a':np.array([-1.5,1.]),'b':np.array([1.,-1.5]),'n':np.array([-1.,-1.])}
slope2={'a':3.,'b':1/3,'n':1.}
def g(w,h,k):
    return h[...,0] if w==1 else slope2[k]*h[...,1]
N=200000
worst={}
for (k1,k2,k3) in itertools.product(C,repeat=3):
  for c in (1,2):
    x=C[k1]+rng.uniform(-r,r,(N,2)); y=C[k2]+rng.uniform(-r,r,(N,2)); z=C[k3]+rng.uniform(-r,r,(N,2))
    ok=np.all(z-(x+y)/c>0,axis=1)
    if ok.sum()==0: continue
    for w in (1,2):
      v=c*g(w,z[ok],k3)-g(w,x[ok],k1)-g(w,y[ok],k2)
      worst[(k1,k2,k3,c,w)]=(ok.sum(),v.min())
for k,v in sorted(worst.items()): print(k,v)
print("all positive:",all(v[1]>0 for v in worst.values()))
