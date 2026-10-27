# REF71: exact checks for L4. Atoms u_{xyz}: coord x=1, y=-1, z=10.
from fractions import Fraction as F
from itertools import permutations
W=[0,1,2]
def u(x,y,z):
    v=[0,0,0]; v[x]=1; v[y]=-1; v[z]=10; return v
atoms={p:u(*p) for p in permutations(W)}
tot=[sum(a[i] for a in atoms.values()) for i in W]
print("d(r) =",tot)
# whole-ball split (lambda=1): s = {xyz, yxz, zyx}, t = the other three
for x in W:
  for y in W:
    if y==x: continue
    z=3-x-y
    S=[(x,y,z),(y,x,z),(z,y,x)]
    s=[sum(atoms[p][i] for p in S) for i in W]
    t=[tot[i]-s[i] for i in W]
    # each piece is 3 unit-mass balls; radius eps perturbs each coord by <= 3*eps
    margin=min(s[x],t[x],-min(s),-min(t))
    print("x",x,"y",y,"s",s,"t",t,"margin",margin,"robust for eps <",F(margin,3))
# lambda-range for the lead's split: s = xyz + lam*yxz + zyx
import sympy as sp
lam=sp.symbols('lam')
x,y,z=0,1,2
s=[atoms[(x,y,z)][i]+lam*atoms[(y,x,z)][i]+atoms[(z,y,x)][i] for i in W]
t=[tot[i]-s[i] for i in W]
print("s(lam)",s,"t(lam)",t)
print("conditions: s_x>0, t_x>0, s_y<0 (lam<2), t_z<0 (lam>9/10) -> lam in (9/10,1]")
