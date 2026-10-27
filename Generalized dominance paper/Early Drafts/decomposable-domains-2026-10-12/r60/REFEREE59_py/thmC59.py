"""thmC59: independent exhaustive check of PP75 Theorem C (closed form of copy-defeat) on the abstract
two-valued H-atom model, plus checks of PP76 Cor 1.2(i)'s gloss and Prop 1.6 (exhaustion criterion).

Atom kind = (kind in {A, B}, odd world o, values (Z, B, X) in {0 = S, 1 = h}^3).
A_o: h right at the two worlds != o.  B_o: h right only at o.
Pattern of a move v -> v' = set of worlds at which v' is strictly better.
A configuration is the set of atom kinds that are non-null.  Measurable sets S may split an atom.

Brute-force defeat of Z (PP75's notion, 'the base rule included'): some S subset Delta(Z, B), non-null, such
that at every world j either
  guidance block:  Z[S -> B] strictly j-better than Z (pointwise on S), or
  refusal block:   X strictly j-better than Y_S := B[S -> Z] (pointwise on {X != Y_S}, which is non-null).
"""
import itertools, random

W3 = (0, 1, 2)


def better_set(kind, o, v_from, v_to):
    """worlds where v_to is strictly better than v_from (v_from != v_to)."""
    hset = frozenset(w for w in W3 if w != o) if kind == 'A' else frozenset([o])
    return hset if v_to == 1 else frozenset(W3) - hset


def brute_defeat(cfg):
    U = [a for a in cfg if a[2][0] != a[2][1]]           # Delta(Z, B)
    for st in itertools.product((0, 1, 2), repeat=len(U)):
        if not any(st):
            continue
        # pieces: (atom, inS)
        pieces = []
        for a in cfg:
            if a in U:
                s = st[U.index(a)]
                if s in (1, 2): pieces.append((a, True))
                if s in (0, 2): pieces.append((a, False))
            else:
                pieces.append((a, False))
        ok = True
        for j in W3:
            # guidance: on S, B better than Z at j
            g = all(j in better_set(a[0], a[1], a[2][0], a[2][1]) for (a, inS) in pieces if inS)
            # refusal: Y = Z on S, B elsewhere; on {X != Y} X better than Y at j
            diff = []
            for (a, inS) in pieces:
                Z, B, X = a[2]
                Y = Z if inS else B
                if X != Y:
                    diff.append(j in better_set(a[0], a[1], Y, X))
            rf = bool(diff) and all(diff)
            if not (g or rf):
                ok = False
                break
        if ok:
            return True
    return False


def closed_form(cfg):
    P1 = {better_set(a[0], a[1], a[2][0], a[2][1]) for a in cfg if a[2][0] != a[2][1] and a[2][0] == a[2][2]}
    P2 = {better_set(a[0], a[1], a[2][0], a[2][2]) for a in cfg if a[2][0] != a[2][2] and a[2][0] == a[2][1]}
    for k in W3:
        i, j = [w for w in W3 if w != k]
        nk, si, sj, sk = frozenset([i, j]), frozenset([i]), frozenset([j]), frozenset([k])
        Da = (nk in P1 and P1 <= {nk, si, sj} and all(k in p for p in P2)
              and (bool(P2) or bool(P1 & {si, sj})))
        Db = (bool(P1) and all(k in p for p in P1) and P2 <= {nk} and (bool(P2) or sk in P1))
        if Da or Db:
            return True
    return False


def n1(cfg):
    # B strictly better than X somewhere at every world
    return all(any(a[2][1] != a[2][2] and w in better_set(a[0], a[1], a[2][2], a[2][1]) for a in cfg) for w in W3)


def n1_closed(cfg):
    P1 = {better_set(a[0], a[1], a[2][0], a[2][1]) for a in cfg if a[2][0] != a[2][1] and a[2][0] == a[2][2]}
    P2 = {better_set(a[0], a[1], a[2][0], a[2][2]) for a in cfg if a[2][0] != a[2][2] and a[2][0] == a[2][1]}
    cov = set()
    for p in P1: cov |= p
    for p in P2: cov |= set(W3) - p
    return cov == set(W3)


def main():
    kinds = [(kd, o, v) for kd in 'AB' for o in W3 for v in itertools.product((0, 1), repeat=3)
             if not (v[0] == v[1] == v[2])]
    random.seed(59)
    tot = mis = mis_adm = adm = defeats = defeats_adm = n1mis = 0
    examples = []
    cfgs = []
    for size in (1, 2, 3, 4):
        cfgs += [frozenset(c) for c in itertools.combinations(kinds, size)]
    for _ in range(30000):
        cfgs.append(frozenset(random.sample(kinds, random.choice((5, 6, 7)))))
    for cfg in cfgs:
        tot += 1
        bd, cf = brute_defeat(cfg), closed_form(cfg)
        defeats += bd
        if n1(cfg) != n1_closed(cfg): n1mis += 1
        P2ne = any(a[2][0] != a[2][2] and a[2][0] == a[2][1] for a in cfg)
        isadm = n1(cfg) and P2ne
        adm += isadm; defeats_adm += bd and isadm
        if bd != cf:
            mis += 1
            if isadm:
                mis_adm += 1
                if len(examples) < 5: examples.append((sorted(cfg), bd, cf))
    print('configurations: %d (all subsets of size <= 4 of the %d kinds, plus 30000 random of size 5-7)' % (tot, len(kinds)))
    print('(N1) closed form mismatches: %d' % n1mis)
    print('defeats (brute force): %d ; closed-form mismatches over all configurations: %d' % (defeats, mis))
    print('configurations satisfying (N1) and (N2): %d ; defeats among them: %d ; mismatches: %d' % (adm, defeats_adm, mis_adm))
    for e in examples: print('  example:', e)


if __name__ == '__main__':
    main()
