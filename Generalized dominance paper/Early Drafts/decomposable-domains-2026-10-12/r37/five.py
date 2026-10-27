# Audit's five-region example, propagated by (IB) to every model on 5 regions
# (one penalty step per region, models = subsets = penalty sets; smaller is better).
import itertools
from scipy.optimize import linprog
R = range(5)
models = [frozenset(s) for k in range(6) for s in itertools.combinations(R, k)]
base = {'A':{0,4},'B':{1,4},'C':{2,4},'D':{3,4},'E':{0}}
strict_pairs = [('A','B'),('B','C'),('C','D'),('D','E'),('E','A')]
# record of (X,Y): (X minus Y, Y minus X); "X strictly better" records:
strict_recs = {(frozenset(base[a]-base[b]), frozenset(base[b]-base[a])) for a,b in strict_pairs}
def leq(X, Y):   # X no worse than Y
    if X <= Y: return True                     # guidance
    return (X - Y, Y - X) in strict_recs
def strict(X, Y): return leq(X, Y) and not leq(Y, X)
viol = 0; cert_fail = 0; ntrip = 0
for X, Y, Z in itertools.permutations(models, 3):
    if leq(X, Y) and leq(Y, Z) and strict(Z, X): viol += 1
for T in itertools.combinations(models, 3):
    cons = []  # rows a with a.w <= 0 (weak) or a.w <= -1 (strict)
    for X, Y in itertools.permutations(T, 2):
        if leq(X, Y):
            a = [(1 if r in X else 0) - (1 if r in Y else 0) for r in R]  # L(X)-L(Y) <= 0
            cons.append((a, strict(X, Y)))
    if not cons: continue
    ntrip += 1
    A = [a for a, s in cons]; b = [-1 if s else 0 for a, s in cons]
    res = linprog([0]*5, A_ub=A, b_ub=b, bounds=[(1, None)]*5)   # w >= 1 (strictly positive, scaled)
    if res.status != 0: cert_fail += 1
print("models", len(models), "TC violations", viol, "triples with comparisons", ntrip, "triples without certificate", cert_fail)
