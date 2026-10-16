"""S2 numerics (2): the parallelogram lemma (PL) is an identity of exchanges.

On the U-domain a model is a subset of U; at world k the error set is E_k(X) = X sym-diff P_k with
P_k = {h in U : h_k > 0}, and by (G)+(IB) (N9.4 / Lemma vectorform) C <=_k X depends only on the
pair of difference sets (E_k C \ E_k X, E_k X \ E_k C).

PL: for models C, F and D contained in C sym-diff F, put X = C sym-diff D, X' = F sym-diff D. Then for
every world k:  (E_k C \ E_k X, E_k X \ E_k C) == (E_k X' \ E_k F, E_k F \ E_k X'),
so C <=_k X  iff  X' <=_k F, whatever the world orders are.

We check the set identity on random finite configurations with random sign patterns (n = 2, 3, 4).
"""
import random
random.seed(7)

def check(trials=20000):
    bad = 0
    for _ in range(trials):
        n = random.choice([2, 3, 4])
        N = random.randint(1, 30)
        signs = [[random.choice([-1, 1]) for _ in range(n)] for _ in range(N)]   # sign of h_k per cell
        P = [{g for g in range(N) if signs[g][k] > 0} for k in range(n)]
        C = {g for g in range(N) if random.random() < .5}
        F = {g for g in range(N) if random.random() < .5}
        diff = C ^ F
        D = {g for g in diff if random.random() < .5}
        X, Xp = C ^ D, F ^ D
        for k in range(n):
            E = lambda Y: Y ^ P[k]
            lhs = (E(C) - E(X), E(X) - E(C))
            rhs = (E(Xp) - E(F), E(F) - E(Xp))
            if lhs != rhs:
                bad += 1
    return bad

print('PL set identity violations in 20000 random configurations:', check())
