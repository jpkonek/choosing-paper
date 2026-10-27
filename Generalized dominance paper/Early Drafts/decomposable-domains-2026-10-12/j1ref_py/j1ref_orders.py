"""J1 referee, combinatorics of Theorem R.2 (PROVED in J1_referee.md; this script only enumerates).
For every digraph G on {0,1,2} with a directed cycle, compute the minimum number of arrows that must
be misaligned for a configuration with conflict digraph G to escape Theorem R.2:
  an order (k1,k2,k3) is aligned if every FORWARD arrow (earlier -> later) is aligned and,
  when k2 has arrows to both k1 and k3, condition (B) holds.
Two readings of (B): 'B fails' (worst case: an order whose middle vertex has out-degree 2 never helps)
and 'B holds'. Run: python3 -I j1ref_orders.py
"""
from itertools import combinations, permutations

V = (0, 1, 2)
ARCS = [(a, b) for a in V for b in V if a != b]


def has_cycle(A):
    S = set(A)
    if any((b, a) in S for (a, b) in S):
        return True
    return {(0, 1), (1, 2), (2, 0)} <= S or {(0, 2), (2, 1), (1, 0)} <= S


def min_mis(A, B_fails):
    A = list(A)
    best = None
    for r in range(len(A) + 1):
        for Mis in combinations(A, r):
            ok = True  # survives = every order is non-aligned
            for o in permutations(V):
                pos = {v: i for i, v in enumerate(o)}
                fwd = [e for e in A if pos[e[0]] < pos[e[1]]]
                k1, k2, k3 = o
                Bbad = B_fails and (k2, k1) in A and (k2, k3) in A
                if not (any(e in Mis for e in fwd) or Bbad):
                    ok = False
                    break
            if ok:
                return r, Mis
    return best


seen = set()
rows = []
for r in range(2, 7):
    for A in combinations(ARCS, r):
        if not has_cycle(A):
            continue
        # canonical form up to relabelling
        canon = min(tuple(sorted((p[a], p[b]) for a, b in A)) for p in
                    [dict(zip(V, q)) for q in permutations(V)])
        if canon in seen:
            continue
        seen.add(canon)
        mf = min_mis(canon, True)
        mh = min_mis(canon, False)
        rows.append((len(canon), canon, mf[0], mh[0], mf[1]))
for n, A, mf, mh, wit in rows:
    print(f"|A|={n} arcs={A}  min misaligned to survive: B-fails {mf}, B-holds {mh}; witness {wit}")


# ---- all minimal surviving misaligned sets, and test of the characterisation
# "Mis survives  <=>  Mis contains a directed cycle of G"   (B-holds reading)
def survives(A, Mis, B_fails):
    for o in permutations(V):
        pos = {v: i for i, v in enumerate(o)}
        fwd = [e for e in A if pos[e[0]] < pos[e[1]]]
        k1, k2, k3 = o
        Bbad = B_fails and (k2, k1) in A and (k2, k3) in A
        if not (any(e in Mis for e in fwd) or Bbad):
            return False
    return True


print("\ncharacterisation test (B-holds): survives <=> Mis contains a directed cycle")
bad = 0
for n, A, *_ in rows:
    for r in range(len(A) + 1):
        for Mis in combinations(A, r):
            if survives(A, set(Mis), False) != has_cycle(Mis):
                bad += 1
                print("  counterexample", A, Mis)
print("  mismatches:", bad)
print("\nB-fails reading: minimal surviving sets")
for n, A, *_ in rows:
    mins = []
    for r in range(len(A) + 1):
        for Mis in combinations(A, r):
            if survives(A, set(Mis), True) and not any(set(x) <= set(Mis) for x in mins):
                mins.append(Mis)
    print(f"  {A}: {mins}")
