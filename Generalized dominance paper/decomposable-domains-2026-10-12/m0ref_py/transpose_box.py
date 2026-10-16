"""M0 referee, independent check 1.
(a) sympy: facet data of the transposed field c^sigma(g)=sigma c(sigma g), sigma=(1 2), is (1/x2, 1/x1, 1/x3).
(b) brute-force box search (dense tau grid, own code) vs the product criterion
    certificate  <=>  some x_k x_{k+1} > kappa  or  some x_k x_{k+1} < 1/kappa   (k cyclic).
"""
import sympy as sp, numpy as np, itertools
h1,h2,h3,x1,x2,x3=sp.symbols('h1 h2 h3 x1 x2 x3',positive=True)
def c(k,h,x):
    a,b,cc=h
    if k==1: return sp.Matrix([-(x[0]*b+cc),x[0]*b,cc])
    if k==2: return sp.Matrix([a,-(a+x[1]*cc),x[1]*cc])
    return sp.Matrix([x[2]*a,b,-(x[2]*a+b)])
X=(x1,x2,x3); P=sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])
h=sp.Matrix([h1,h2,h3])
# sigma F2 = F1, sigma F1 = F2, sigma F3 = F3
cs={1:P*c(2,list(P*h),X), 2:P*c(1,list(P*h),X), 3:P*c(3,list(P*h),X)}
Y=(1/x2,1/x1,1/x3)
for k in (1,2,3):
    ratio=[sp.simplify(cs[k][i]/c(k,list(h),Y)[i]) for i in range(3)]
    print('facet',k,'c^sigma / c(1/x2,1/x1,1/x3) =',ratio)

# (b)
def setup(eps):
    kap=(1+2*eps)/(1-eps)
    r12=np.array([-1,-1,kap+1.]); r23=np.array([kap+1,-1,-1.]); r31=np.array([-1,kap+1,-1.])
    return kap,{0:(r31,r12),1:(r12,r23),2:(r23,r31)}
def cv(k,H,x):
    a,b,cc=H[:,0],H[:,1],H[:,2]
    if k==0: return np.stack([-(x[0]*b+cc),x[0]*b,cc],1)
    if k==1: return np.stack([a,-(a+x[1]*cc),x[1]*cc],1)
    return np.stack([x[2]*a,b,-(x[2]*a+b)],1)
def brute(x,eps,nt=4001,ns=801):
    kap,F=setup(eps); t=np.linspace(1e-6,1-1e-6,nt)
    HH={k:(1-t)[:,None]*F[k][0]+t[:,None]*F[k][1] for k in range(3)}
    CC={k:cv(k,HH[k],x) for k in range(3)}
    s=np.concatenate([np.linspace(1e-6,1e-2,200),np.linspace(1e-2,1-1e-2,ns),1-np.linspace(1e-6,1e-2,200)])
    best=-np.inf
    for a,b in itertools.permutations(range(3),2):
        q=np.zeros((len(s),3)); q[:,a]=1-s; q[:,b]=s
        S={}
        for k in range(3):
            H=HH[k]; C=CC[k]
            mA=(H[:,a]<0)&(H[:,b]>0); RA=np.where(mA,-H[:,a]/np.where(mA,H[:,b],1),0)
            pos=(C@q.T)>0
            S[('A',k)]=np.where(pos,RA[:,None],0).max(0)
            mB=(H[:,b]<0)&(H[:,a]>0); RB=np.where(mB,-H[:,b]/np.where(mB,H[:,a],1),0)
            S[('B',k)]=np.where(pos,RB[:,None],0).max(0)
        for k in range(3):
            for kk in range(3):
                pr=S[('A',k)]*S[('B',kk)]
                if pr.max()>0: best=max(best,np.log(pr.max()))
    return best
def pred(x,kap):
    p=[x[0]*x[1],x[1]*x[2],x[2]*x[0]]
    return max(max(np.log(v/kap),np.log(1/(kap*v))) for v in p)
rng=np.random.default_rng(7); agree=0; n=0; worst=0
for eps in [0.1,0.3,0.7]:
    kap=(1+2*eps)/(1-eps)
    for _ in range(25):
        x=np.exp(rng.uniform(-1.2,1.2,3)*np.log(kap)*0.8)
        b=brute(x,eps); p=pred(x,kap); n+=1
        if abs(p)>0.02: agree+= (np.sign(b)==np.sign(p))
        else: agree+=1
        worst=max(worst,abs(b-p))
print(f'(b) sign agreement brute vs product criterion: {agree}/{n}; max |brute-pred| = {worst:.3g}')
