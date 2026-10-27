from fractions import Fraction as F
from itertools import product, combinations
# --- 1. geometry: advice of D_K for K=[l,u] on g=(1-t,-t)
def advice(l,u,t):
    # accept g iff min_{p in K}(p-t)>0 iff l>t ; accept -g iff u<t
    if l>t: return 'g'
    if u<t: return 'b'   # accepts -g: bad at world 1
    return 's'
A=(F(1,4),F(3,4)); B=(F(2,5),F(3,5))
ts={'a':F(30,100),'b':F(35,100),'c':F(65,100),'d':F(70,100),'e':F(72,100)}
for r,t in ts.items():
    print(r,t,'A:',advice(*A,t),'B:',advice(*B,t))
# check each patch interval of half-width 1/100 stays in the same advice zone
for r,t in ts.items():
    for tt in (t-F(1,100),t+F(1,100)):
        assert advice(*A,tt)==advice(*A,t) and advice(*B,tt)==advice(*B,t),(r,tt)
print('patch zones stable for half-width 1/100')
# --- 2. ranks
R1={'g':0,'s':1,'b':2,'x':3}   # world 1: accepting g good
R2={'g':2,'s':1,'b':0,'x':3}   # world 2 reversed; contradiction worst
P='abcde'
LIC=[ {'a':('s','g'),'c':('s','b')},          # base A-type: rival gains a, loses c
      {'b':('g','s'),'c':('b','s')},          # base B-type
      {'b':('s','g'),'d':('s','b')},
      {'a':('g','s'),'d':('b','s'),'e':('b','s')} ]
# certificate: sum of rank changes (rival-base) at world 1 over the four licences
tot={r:0 for r in P}
for L in LIC:
    for r,(o,n) in L.items(): tot[r]+=R1[n]-R1[o]
print('net world-1 rank change of the four records:',tot)
# --- 3. relation on finite abstraction (whole patches), advice in g,s,b,x
models=list(product('gsbx',repeat=5))
idx={m:i for i,m in enumerate(models)}
def rec(Y,X):  # record from base Y to rival X
    return {P[k]:(Y[k],X[k]) for k in range(5) if Y[k]!=X[k]}
def lic(Y,X):
    r=rec(Y,X); return any(r==L for L in LIC)
def le1(Y,X): # Y no worse than X at world 1
    return all(R1[Y[k]]<=R1[X[k]] for k in range(5)) or lic(Y,X)
def le2(Y,X):
    return all(R2[Y[k]]<=R2[X[k]] for k in range(5))
succ1=[[j for j,X in enumerate(models) if le1(Y,X)] for Y in models]
S1=[set(s) for s in succ1]
# strict G
bad=0
for i,Y in enumerate(models):
    for j in succ1[i]:
        X=models[j]
        if i!=j and all(R1[Y[k]]<=R1[X[k]] for k in range(5)) and i in S1[j]: bad+=1
print('strict-G violations:',bad)
ties=sum(1 for i in range(len(models)) for j in succ1[i] if j!=i and i in S1[j])
print('nontrivial ties at world 1:',ties)
# TC: Y0<=Y1<=Y2 and Y2<Y0 (Y2<=Y0, not Y0<=Y2)
viol=0
for i0 in range(len(models)):
    for i1 in succ1[i0]:
        for i2 in succ1[i1]:
            if i0 in S1[i2] and i2 not in S1[i0]: viol+=1
print('TC violations at world 1:',viol)
# strict cycle through the four licences
A0=tuple('ssss'+'b')  # base silent on a..d, bad on e  (A-like on a..d)
# undominated: A (all s) and B (g,g,b,b,b)
Am=tuple('sssss'); Bm=tuple('ggbbb')
def dominated(Z):
    for X in models:
        if X==Z: continue
        if le1(X,Z) and le2(X,Z) and (not le1(Z,X) or not le2(Z,X)): return X
    return None
print('A dominated by:',dominated(Am),' B dominated by:',dominated(Bm))
# the four rivals: who defends
rivals=[('A',Am,{'a':'g','c':'b'}),('B',Bm,{'b':'s','c':'s'}),('A',Am,{'b':'g','d':'b'}),('B',Bm,{'a':'s','d':'s','e':'s'})]
for name,base,ch in rivals:
    X=list(base)
    for r,v in ch.items(): X[P.index(r)]=v
    X=tuple(X)
    print(name,'vs',''.join(X),' w1 defends:',le1(base,X),' w2 defends:',le2(base,X),' w2 comparable either way:',le2(base,X) or le2(X,base))
# local potentials for every 3 licence types: strict inequalities
cons=[lambda w:w['c']>w['a'],lambda w:w['b']>w['c'],lambda w:w['d']>w['b'],lambda w:w['a']>w['d']+w['e']]
W={(0,1,2):dict(a=1,c=2,b=3,d=4,e=1),(1,2,3):dict(c=1,b=2,d=3,e=1,a=5),(0,2,3):dict(b=1,d=2,e=1,a=4,c=5),(0,1,3):dict(d=1,e=1,a=3,c=4,b=5)}
for S,w in W.items():
    assert all(cons[k](w) for k in S); print('licences',[k+1 for k in S],'strictly endorsed by',w)
print('all four simultaneously endorsable (weak)?  impossible: chain gives w_a>=w_a+w_e')
# --- 4. explicit strict cycle and shortest strict cycle length
chain=[tuple('sgsss'[0:0]+'ssssb')]
Y=list('sgssb')  # a s, b g, c s, d s, e b
seq=[tuple(Y)]
for L in LIC:
    Z=list(seq[-1])
    for r,(o,n) in L.items():
        assert Z[P.index(r)]==o; Z[P.index(r)]=n
    seq.append(tuple(Z))
print('chain:',[''.join(s) for s in seq])
for k in range(4): assert le1(seq[k],seq[k+1])
print('last strictly better than first by guidance:', le1(seq[4],seq[0]) and not le1(seq[0],seq[4]))
# shortest strict cycle via search over lengths 2..5
import collections
def has_strict_cycle(maxlen):
    N=len(models)
    for L_ in range(2,maxlen+1):
        found=False
        # cycle Y0<=Y1<=...<=Y_{L-1}<=Y0 with at least one strict edge
        for i0 in range(N):
            frontier={(i0,False)}
            for step in range(L_-1):
                nf=set()
                for (i,s) in frontier:
                    for j in succ1[i]:
                        if j==i: continue
                        nf.add((j, s or (i not in S1[j])))
                frontier=nf
            for (i,s) in frontier:
                if i0 in S1[i] and i!=i0 and (s or (i not in S1[i0])): return L_
    return None
print('shortest strict cycle length at world 1:',has_strict_cycle(5))
# --- 5. defence allocation over all rivals to A in the abstraction
cnt=collections.Counter()
for X in models:
    if X==Am: continue
    d1=le1(Am,X); d2=le2(Am,X)
    cnt[(d1,d2)]+=1
print('rivals to A: (world1 defends, world2 defends) counts:',dict(cnt))
