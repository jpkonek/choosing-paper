from fractions import Fraction as F
from itertools import product
import random
random.seed(1)
K=4
models=list(product([0,1],repeat=K))   # error indicator per region (binary, error / no error)
def le(mp,mm,X,Y):  # X at least as accurate as Y
    add=sum(mp[k] for k in range(K) if Y[k] and not X[k])
    rem=sum(mm[k] for k in range(K) if X[k] and not Y[k])
    return add>=rem
def tc_viol(mp,mm):
    for X in models:
        for Y in models:
            if not le(mp,mm,X,Y): continue
            for Z in models:
                if le(mp,mm,Y,Z) and le(mp,mm,Z,X) and not le(mp,mm,X,Z): return (X,Y,Z)
    return None
def transitive(mp,mm):
    return all(le(mp,mm,X,Z) for X in models for Y in models for Z in models if le(mp,mm,X,Y) and le(mp,mm,Y,Z))
def intersection_equal(mp,mm):
    # compare with: for all nu with mp<=nu<=mm, nu(E_Y)>=nu(E_X); worst case nu=mp on additions, mm on removals -> same; check by vertices
    for X in models:
        for Y in models:
            ok=all(sum(nu[k]*(Y[k]-X[k]) for k in range(K))>=0 for nu in product(*[(mp[k],mm[k]) for k in range(K)]))
            if ok!=le(mp,mm,X,Y): return False
    return True
cautious=sticky=0; cv=sv=0; tr=ie=0
for trial in range(300):
    mm=[F(random.randint(1,6)) for _ in range(K)]
    if trial%2==0:
        mp=[F(random.randint(1,int(m))) for m in mm]   # mp <= mm : cautious
        cautious+=1
        if tc_viol(mp,mm) is None: cv+=1
        if transitive(mp,mm): tr+=1
        if intersection_equal(mp,mm): ie+=1
    else:
        mp=list(mm); j=random.randrange(K); mp[j]=mm[j]+random.randint(1,4)  # sticky on one region
        sticky+=1
        if tc_viol(mp,mm) is not None: sv+=1
print('cautious (mu+<=mu-): trials',cautious,'TC holds',cv,'transitive',tr,'= intersection of band',ie)
print('sticky on one region: trials',sticky,'TC violated',sv)
# explicit sticky counterexample: regions P,Q,R ; mu- =1, mu+ =2
mp=[F(2)]*3+[F(1)]; mm=[F(1)]*4
X=(0,1,1,0); Y=(1,0,1,0); Z=(0,0,0,0)
# with K=4 regions: P=0,Q=1,R=2
X=(0,1,1,0); Y=(1,0,1,0); Z=(0,1,0,0)
print('explicit:', le(mp,mm,X,Y), le(mp,mm,Y,Z), le(mp,mm,Z,X), not le(mp,mm,X,Z))
