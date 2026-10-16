"""K2.1 check (NUMERICS/CHECKED): the piece-assignment of the Divisibility Theorem.

Random certificates on finitely many cells: integer weights n_k, cell values d_k(c) in {-1,0,1},
with sum_k n_k d_k(c) <= 0 for every cell and < 0 for some cell.
Each cell is split into N equal pieces (N = max_c sum_{k: d_k(c)=-1} n_k).
Negatives: generator k gets n_k distinct pieces of each cell where d_k = -1.
Positives: generator k gets n_k distinct pieces, chosen among pieces already assigned
to negatives of other generators, in each cell where d_k = +1.
We verify: (i) every piece is +1 for at most one k and -1 for at most one k
(pairwise disjoint gains, pairwise disjoint losses: the chaining lemma applies);
(ii) the sum of the piece-vectors is <= 0 on every piece and < 0 on some piece;
(iii) piece-vector k uses the same fraction n_k/N of every cell of its support.
Exact integer arithmetic; run with python3 -I.
"""
import random

def random_certificate(rng, ncells, ngen):
    while True:
        d = [[rng.choice((-1, 0, 0, 1)) for _ in range(ncells)] for _ in range(ngen)]
        n = [rng.randint(1, 4) for _ in range(ngen)]
        ok = True
        strict = False
        for c in range(ncells):
            s = sum(n[k] * d[k][c] for k in range(ngen))
            if s > 0:
                ok = False
                break
            if s < 0:
                strict = True
        if ok and strict and all(any(x != 0 for x in row) for row in d):
            return d, n

def assign(d, n):
    ngen, ncells = len(d), len(d[0])
    N = max(sum(n[k] for k in range(ngen) if d[k][c] == -1) for c in range(ncells))
    pos = {k: {} for k in range(ngen)}
    neg = {k: {} for k in range(ngen)}
    for c in range(ncells):
        nxt = 0
        owners = []  # piece index -> negative owner
        for k in range(ngen):
            if d[k][c] == -1:
                neg[k][c] = list(range(nxt, nxt + n[k]))
                owners += [k] * n[k]
                nxt += n[k]
        assert nxt <= N
        free = 0
        for k in range(ngen):
            if d[k][c] == 1:
                chosen = []
                while len(chosen) < n[k]:
                    assert free < nxt, "certificate inequality violated"
                    assert owners[free] != k
                    chosen.append(free)
                    free += 1
                pos[k][c] = chosen
    return N, pos, neg

def verify(d, n, N, pos, neg):
    ngen, ncells = len(d), len(d[0])
    some_neg = False
    for c in range(ncells):
        val = [0] * N
        pcount = [0] * N
        ncount = [0] * N
        for k in range(ngen):
            for p in pos[k].get(c, []):
                val[p] += 1
                pcount[p] += 1
            for p in neg[k].get(c, []):
                val[p] -= 1
                ncount[p] += 1
            # fraction check
            if d[k][c] == 1:
                assert len(pos[k][c]) == n[k]
            if d[k][c] == -1:
                assert len(neg[k][c]) == n[k]
        assert max(pcount) <= 1 and max(ncount) <= 1
        assert max(val) <= 0
        if min(val) < 0:
            some_neg = True
    assert some_neg
    return True

def main():
    rng = random.Random(20261015)
    trials = 0
    for _ in range(3000):
        ncells = rng.randint(2, 7)
        ngen = rng.randint(2, 6)
        d, n = random_certificate(rng, ncells, ngen)
        N, pos, neg = assign(d, n)
        verify(d, n, N, pos, neg)
        trials += 1
    print("divisibility piece-assignment: %d random certificates, 0 failures" % trials)

if __name__ == "__main__":
    main()
