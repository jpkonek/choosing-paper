"""Search finite independent orders with no strictly positive additive weak extension."""
import numpy as np
from scipy.optimize import linprog
import random, json, time
from pathlib import Path

rng=random.Random(77219)
n=6
bits=np.array([[(s>>i)&1 for i in range(n)] for s in range(1<<n)])
full=(1<<n)-1
out=Path(__file__).parent
start=time.time()

def flippable(order):
    rank=np.empty(1<<n,dtype=int)
    rank[order]=np.arange(1<<n)
    candidates=set()
    for a,b in zip(order,order[1:]):
        a,b=int(a&~b),int(b&~a)
        # The previous simultaneous assignment uses the original a,b.
        if a and b:
            candidates.add((a,b))
    valid=[]
    for a,b in candidates:
        rest=full^(a|b)
        c=rest
        pairs=[]
        while True:
            if rank[b|c]!=rank[a|c]+1:
                break
            pairs.append((int(rank[a|c]),int(rank[b|c])))
            if not c:
                valid.append((a,b,pairs))
                break
            c=(c-1)&rest
    return valid

def margin(order):
    # w dot (later-earlier) >= 0 and every w_i >= delta.
    diffs=bits[order[1:]]-bits[order[:-1]]
    A=np.zeros((len(diffs)+n,n+1))
    A[:len(diffs),:n]=-diffs
    A[len(diffs):,:n]=-np.eye(n)
    A[len(diffs):,-1]=1
    eq=np.zeros((1,n+1)); eq[0,:n]=1
    return linprog([0]*n+[-1],A_ub=A,b_ub=np.zeros(len(A)),
                   A_eq=eq,b_eq=[1],bounds=[(0,None)]*(n+1),method='highs')

for restart in range(40):
    w=np.array([rng.random() for _ in range(n)])
    order=list(np.argsort(bits@w))
    last=None
    for step in range(4000):
        moves=flippable(order)
        if len(moves)>1:
            moves=[m for m in moves if (m[1],m[0])!=last] or moves
        a,b,pairs=rng.choice(moves)
        for i,j in pairs: order[i],order[j]=order[j],order[i]
        last=(a,b)
        res=margin(order)
        if not res.success or res.x[-1]<1e-9:
            data={'n':n,'order':list(map(int,order)),'success':res.success,
                  'margin':float(res.x[-1]) if res.success else None,
                  'weights':res.x.tolist() if res.success else None}
            (out/'finite_order.json').write_text(json.dumps(data,indent=2))
            print('FOUND',restart,step,time.time()-start,data,flush=True)
            raise SystemExit
    print('restart',restart,'seconds',round(time.time()-start,1),flush=True)
print('No witness found')
