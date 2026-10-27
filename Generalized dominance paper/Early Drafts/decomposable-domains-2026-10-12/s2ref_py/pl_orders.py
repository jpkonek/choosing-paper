"""S2 referee check (1): the parallelogram lemma at the level of ORDERS, for non-additive cancellative worlds.

Finite stand-in for M_U: cells g = 0..N-1, sign pattern of h per cell, P_k = {h_k > 0}, E_k(Y) = Y ^ P_k.
World orders tested (all strictly monotone and de Finetti-cancellative on error sets):
  'add'  : additive, random positive weights (complete);
  'lex'  : lexicographic in 2-3 random charges with zeros allowed, last level strictly positive (complete);
  'unan' : unanimity over 2-3 random positive weight vectors (INCOMPLETE).
Order on error sets: A <= B iff the (cancelled) difference pair (A\\B, B\\A) is accepted.
Checks, for random C, F and D subset of C^F, X = C^D, X' = F^D, every world:
  (PL)  C <=_k X  <=>  X' <=_k F      and   (PL*)  F <=_k X'  <=>  X <=_k C.
Control: with D NOT contained in C^F the equivalence can fail (hypothesis is needed).
"""
import random
random.seed(11)

def make_order(kind, N):
    if kind == 'add':
        w = [random.uniform(.1, 2) for _ in range(N)]
        return lambda A, B: sum(w[g] for g in A) <= sum(w[g] for g in B) + 1e-12
    if kind == 'lex':
        L = random.randint(2, 3)
        lv = [[random.choice([0, 0, random.uniform(.1, 2)]) for _ in range(N)] for _ in range(L - 1)]
        lv.append([random.uniform(.1, 2) for _ in range(N)])
        def le(A, B):
            for w in lv:
                a, b = sum(w[g] for g in A), sum(w[g] for g in B)
                if abs(a - b) > 1e-12:
                    return a < b
            return True
        return le
    if kind == 'unan':
        W = [[random.uniform(.1, 2) for _ in range(N)] for _ in range(random.randint(2, 3))]
        return lambda A, B: all(sum(w[g] for g in A) <= sum(w[g] for g in B) + 1e-12 for w in W)

def run(trials=20000, inside=True):
    bad = 0
    for _ in range(trials):
        n = random.choice([2, 3, 4]); N = random.randint(1, 12)
        signs = [[random.choice([-1, 1]) for _ in range(n)] for _ in range(N)]
        P = [{g for g in range(N) if signs[g][k] > 0} for k in range(n)]
        orders = [make_order(random.choice(['add', 'lex', 'unan']), N) for _ in range(n)]
        C = {g for g in range(N) if random.random() < .5}
        F = {g for g in range(N) if random.random() < .5}
        pool = (C ^ F) if inside else set(range(N))
        D = {g for g in pool if random.random() < .5}
        X, Xp = C ^ D, F ^ D
        for k in range(n):
            E = lambda Y: Y ^ P[k]
            le = lambda Y, Z: orders[k](E(Y) - E(Z), E(Z) - E(Y))   # cancellation form
            if le(C, X) != le(Xp, F) or le(F, Xp) != le(X, C):
                bad += 1
                break
    return bad

print('PL/PL* violations, D inside C^F, 20000 trials (add/lex/unan worlds):', run(inside=True))
print('control, D unrestricted (should be > 0):', run(inside=False))
