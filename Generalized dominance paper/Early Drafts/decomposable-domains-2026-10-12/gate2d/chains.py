import itertools, random
from check import *

def chain_test(N, U, seed, nX, gate=True):
    ts, mass = make(N, U, seed)
    ctx = dict(N=N, U=U, mass=mass, K={1: keys(ts, N, U, 1), 2: keys(ts, N, U, 2)})
    models = list(itertools.product('PSMC', repeat=N+U))
    rnd = random.Random(seed)
    def acc(X, Y, w):
        if gate: return accept(X, Y, ctx, w, phi_sticky)
        # ungated version: same Phi on every mixed record
        if X == Y: return True
        UX, UY = indic(ranks(X, N, U, w)), indic(ranks(Y, N, U, w))
        on, off = UY - UX, UX - UY
        if not off: return True
        if not on: return False
        return phi_sticky(X, Y, w, on, off, ctx) >= 0
    viol = 0; weak = 0; ex = None
    Xs = rnd.sample(models, min(nX, len(models)))
    for w in (1, 2):
        succ = {}
        def S(X):
            if X not in succ: succ[X] = [Y for Y in models if Y != X and acc(X, Y, w)]
            return succ[X]
        for X in Xs:
            for Y in S(X):
                for Z in S(Y):
                    if Z == X: weak += 1; continue
                    if acc(Z, X, w):
                        weak += 1
                        if not acc(X, Z, w):
                            viol += 1
                            if ex is None: ex = (w, X, Y, Z)
    return dict(N=N, U=U, gate=gate, TC_violations=viol, weak_cycles=weak, example=ex)

if __name__ == '__main__':
    print(chain_test(3, 1, 5, 256, gate=True))
    print(chain_test(3, 1, 5, 256, gate=False))
    print(chain_test(4, 0, 7, 150, gate=True))
    print(chain_test(2, 2, 9, 256, gate=True))
