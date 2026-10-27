# ADD71: 4-atom example (worlds x,y,z = coords 0,1,2). Point-mass idealisation, mass 1 per atom.
# s = {sig1, sig2}, t = {tau1, tau2}; all atoms lie outside D_S, so adding any subset is available to D_S.
# Check: s,t in P_x, not dangerous; s+t dangerous and not guided at x;
# s is x-safe: no x-guided g built from the remaining atoms (add atoms with h_x>0, remove atoms with h_x<0,
# fractions in [0,1]; removal availability over-approximated) makes s+g positive at all worlds. Same for t.
from fractions import Fraction as F
from scipy.optimize import linprog
sig1=(-1,-1,5); sig2=(4,-1,1); tau1=(-1,5,-1); tau2=(4,1,-1)
add=lambda *v:[sum(c) for c in zip(*v)]
s=add(sig1,sig2); t=add(tau1,tau2); st=add(s,t)
print("d(s)",s,"d(t)",t,"d(s+t)",st)
assert s[0]>0 and t[0]>0 and min(s)<=0 and min(t)<=0 and min(st)>0
assert sig1[0]<0 and tau1[0]<0   # adding them is not guided at x
def best_rescue(base, others):
    # variables: f_i in [0,1] for each other atom (sign +1 add if h_x>0, -1 remove if h_x<0), m free; maximise m
    cols=[]
    for a in others:
        sgn= 1 if a[0]>0 else -1
        cols.append([sgn*c for c in a])
    n=len(cols)
    c=[0]*n+[-1]
    A=[]; b=[]
    for k in range(3):   # m - base_k - sum f_i col_i[k] <= 0
        A.append([-col[k] for col in cols]+[1]); b.append(base[k])
    r=linprog(c,A_ub=A,b_ub=b,bounds=[(0,1)]*n+[(None,None)])
    return -r.fun, r.x
print("best min-coordinate after x-guided rescue of s:",best_rescue(s,[tau1,tau2]))
print("best min-coordinate after x-guided rescue of t:",best_rescue(t,[sig1,sig2]))
