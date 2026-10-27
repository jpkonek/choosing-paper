# Q2 §5.1: world-1 error sets of coherent members D_[alpha,beta] (K' = [al0,be0] subset of [alpha,beta]) of M_U, n = 2.
# Gamble g=(g1,g2); prior weight t on world 2; D_K accepts g iff (1-t)g1 + t g2 > 0 for all t in K.
# World-1 error: g1>0 and not accepted, or g1<0 and accepted. Claim: E1 = {g in M-: sigma<alpha} u {g in M+: tau<=beta}.
import random
random.seed(3)
def acc(g, K): return all((1-t)*g[0] + t*g[1] > 0 for t in K)
bad = 0; tested = 0
for _ in range(200000):
    al0 = random.uniform(0.05, 0.5); be0 = random.uniform(al0, 0.95)
    al = random.uniform(0, al0); be = random.uniform(be0, 1)
    g = (random.uniform(-1, 1), random.uniform(-1, 1))
    if not acc(g, (al0, be0)): continue                      # g must lie in U = D_K'
    if g[0]*g[1] >= 0: continue                               # mixed problems only
    tested += 1
    err = (g[0] > 0 and not acc(g, (al, be))) or (g[0] < 0 and acc(g, (al, be)))
    if g[0] > 0:
        tau = g[0]/(g[0]-g[1]); pred = tau <= be; assert tau > be0
    else:
        sig = -g[0]/(g[1]-g[0]); pred = sig < al; assert sig < al0
    bad += (err != pred)
print("mixed gambles of U tested:", tested, " mismatches with the lattice formula:", bad)
