# REF73b: exact LP check of CAm for R_g in MU73 sec 1.3 (three sup-balls, r=0.05).
# For each ball combination (k1,k2,k3) and c in {1,2}: is {x in B(k1), y in B(k2), z in B(k3), z >= (x+y)/c} nonempty?
# If so, minimise c*g_w(z)-g_w(x)-g_w(y) (linear on each ball) over the closed feasible set.
import itertools, numpy as np
from scipy.optimize import linprog
r=0.05
C={'a':np.array([-1.5,1.]),'b':np.array([1.,-1.5]),'n':np.array([-1.,-1.])}
s2={'a':3.,'b':1/3,'n':1.}
res=[]
for k1,k2,k3 in itertools.product(C,repeat=3):
  for c in (1,2):
    # variables x1,x2,y1,y2,z1,z2
    bounds=[(C[k1][0]-r,C[k1][0]+r),(C[k1][1]-r,C[k1][1]+r),(C[k2][0]-r,C[k2][0]+r),(C[k2][1]-r,C[k2][1]+r),(C[k3][0]-r,C[k3][0]+r),(C[k3][1]-r,C[k3][1]+r)]
    # z_i >= (x_i+y_i)/c  <=>  x_i + y_i - c z_i <= 0
    A=[[1,0,1,0,-c,0],[0,1,0,1,0,-c]]; b=[0,0]
    # feasibility with strict margin: maximise t s.t. x+y-cz+t<=0 -> check t>0
    A2=[row+[1] for row in A]; 
    f=linprog([0]*6+[-1],A_ub=A2,b_ub=b,bounds=bounds+[(None,1)])
    tmax=-f.fun
    if tmax<=1e-12: continue
    out=[]
    for w in (1,2):
      if w==1: obj=[-1,0,-1,0,c,0]
      else: obj=[0,-s2[k1],0,-s2[k2],0,c*s2[k3]]
      g=linprog(obj,A_ub=A,b_ub=b,bounds=bounds)
      out.append(g.fun)
    res.append(((k1,k2,k3,c),round(tmax,4),[round(v,4) for v in out]))
for x in res: print(x)
print("min world-2 over cross-ball combos:",min(v[2][1] for v in res if len(set(v[0][:3]))>1))
