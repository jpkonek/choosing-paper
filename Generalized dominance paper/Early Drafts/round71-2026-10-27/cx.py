from fractions import Fraction as F
from itertools import permutations
W=[0,1,2]
def u(x,y,z):  # coordinate x:1, y:-1, z:10
    v=[0,0,0]; v[x]=1; v[y]=-1; v[z]=10; return v
atoms={p:u(*p) for p in permutations(W)}
tot=[sum(a[i] for a in atoms.values()) for i in W]
print("total",tot)
for x in W:
  for (y,z) in [(a,b) for a in W for b in W if len({x,a,b})==3]:
    w={p:F(0) for p in atoms}
    w[(x,y,z)]=F(1); w[(y,x,z)]=F(19,20); w[(z,y,x)]=F(1)
    s=[sum(w[p]*atoms[p][i] for p in atoms) for i in W]
    t=[tot[i]-s[i] for i in W]
    print(x,(y,z),"s",s,"t",t, "ok" if s[x]>0 and t[x]>0 and min(s)<=0 and min(t)<=0 else "FAIL")
