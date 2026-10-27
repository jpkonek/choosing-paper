"""exh59: PP76 Cor 1.2 / Cor 1.4 / Prop 1.6 re-checked on an independent two-valued H-atom model,
with strict-guidance refusals COUNTED in the notion of defeat (a source cannot defend at w against a rival
that is strictly w-better: strict (G)).

Atoms g = 0..n-1 with odd world o[g] and kind A/B.  Two values: 1 = h, 0 = S.
First-generation refusals of an accepted record rec(B -> X) at w are computed by brute force over every
common-context copy (B', X') and every Y strictly w-worse than X' (records rec(Y -> B') carried by T).
"""
import itertools, random, sys
random.seed(5959)


def better(kind, o, w, x, y):
    """x strictly better than y at world w (x != y)"""
    if x == y: return False
    hgood = (w != o) if kind == 'A' else (w == o)
    return (x == 1) == hgood


def sworse(K, w, Y, X):
    """Y strictly w-worse than X: pointwise weakly worse, different somewhere"""
    return Y != X and all(not better(K[g][0], K[g][1], w, Y[g], X[g]) for g in range(len(K)))


def forced(K, B, X, w, models):
    n = len(K); D = [g for g in range(n) if B[g] != X[g]]
    out = set()
    for Wc in models:
        Bp = tuple(B[g] if g in D else Wc[g] for g in range(n))
        Xp = tuple(X[g] if g in D else Wc[g] for g in range(n))
        for Y in models:
            if sworse(K, w, Y, Xp):
                out.add(tuple((g, Y[g], Bp[g]) for g in range(n) if Y[g] != Bp[g]))
    return out


def refused_rivals(K, T, B, X, models):
    res = {}
    for w in range(3):
        R = set()
        for r in forced(K, B, X, w, models):
            if all(T[g] == a for g, a, b in r):
                Z = list(T)
                for g, a, b in r: Z[g] = b
                R.add(tuple(Z))
        res[w] = R
    return res


def up(K, T, g, i):
    return better(K[g][0], K[g][1], i, 1 - T[g], T[g])


def crit(K, T, doms, guidance):
    """Prop 1.6 (guidance=False) and its repair (guidance=True)."""
    n = len(K); data = []
    for (B, X) in doms:
        U = {g for g in range(n) if B[g] == T[g] != X[g]}
        L = {g for g in range(n) if B[g] != T[g] == X[g]}
        Wd = {i for i in range(3) if U and all(up(K, T, g, i) for g in U)}
        data.append((U, L, Wd))
    opts = list(range(len(doms))) + (['g'] if guidance else [])
    for sig in itertools.product(opts, repeat=3):
        if any(s != 'g' and i not in data[s][2] for i, s in enumerate(sig)): continue
        G0 = set()
        for i, s in enumerate(sig):
            if s != 'g': G0 |= {g for g in data[s][1] if up(K, T, g, i)}
        Om = set(range(n))
        for i, s in enumerate(sig):
            if s == 'g':
                Om &= {g for g in range(n) if up(K, T, g, i)}
            else:
                Om -= data[s][0]
                Om -= {g for g in range(n) if not up(K, T, g, i) and g not in data[s][1]}
        if G0 <= Om and (G0 or (guidance and Om)):
            return True
    return False


def main():
    n = 4
    models = list(itertools.product((0, 1), repeat=n))
    single_tot = single_def = single_def_noG = 0
    pair_tot = mis_old = mis_new = pd = 0
    ex = None
    for Kt in itertools.product([(kd, o) for kd in 'AB' for o in range(3)], repeat=n):
        K = list(Kt)
        if random.random() > 0.08: continue
        T = tuple(random.choice((0, 1)) for _ in range(n))
        adm = [(B, X) for B in models for X in models if B != X
               and not any(sworse(K, w, B, X) for w in range(3))
               and any(B[g] == T[g] != X[g] for g in range(n))]
        if not adm: continue
        cache = {d: refused_rivals(K, T, d[0], d[1], models) for d in adm}
        def defeated(ds, withG=True):
            for Z in models:
                if Z == T: continue
                if all((withG and sworse(K, w, T, Z)) or any(Z in cache[d][w] for d in ds) for w in range(3)):
                    return True
            return False
        for d in adm:
            single_tot += 1
            a = defeated([d]); b = defeated([d], False)
            single_def += a; single_def_noG += b
            if a and ex is None: ex = (K, T, d)
        for _ in range(60):
            d1, d2 = random.sample(adm, 2)
            pair_tot += 1
            bf = defeated([d1, d2]); pd += bf
            if crit(K, T, [d1, d2], False) != bf: mis_old += 1
            if crit(K, T, [d1, d2], True) != bf: mis_new += 1
    print('single admissible acceptances: %d ; T defeated counting strict guidance: %d ; by coupled refusals alone: %d'
          % (single_tot, single_def, single_def_noG))
    print('first single-acceptance defeat (atoms (kind, odd), T, (B, X)):', ex)
    print('pairs: %d ; T defeated (with guidance): %d ; Prop 1.6 as stated disagrees: %d ; repaired criterion disagrees: %d'
          % (pair_tot, pd, mis_old, mis_new))


if __name__ == '__main__':
    main()
