"""S1 referee / patterns_ref.py -- independent re-derivation of Lemma S1.4 and a strengthening of S1.5(ii).

(1) The comparison tables of S1.4 are NOT hard-coded here.  World-1 error sets are built as sets of atoms
    {m, a, A-a, b, B-b, rest}; world-2 error sets are complements in M (regular models).  For each model pair the
    difference pair (P\\Q, Q\\P) is computed by set algebra and translated into a statement about the relation
    of a and b at that world (de Finetti cancellation).  Then competitiveness of C against X, of C' against Y and
    undominatedness of C, C' (X does not dominate C, Y does not dominate C') are imposed for every one of the
    4 x 4 relation patterns.
(2) Strengthening of S1.5(ii): a pattern (~,~) at (a,b) ties X_{a,b} with C AND Y_{a,b} with C' at both worlds,
    so (C) makes both coherent.  On a discretised crossing (A cut into k sigma-cells, B into k tau-cells, every
    subset enumerated) we count pairs (a,b) with X_{a,b} and Y_{a,b} both coherent: only the 4 corners
    (a in {0,A}, b in {0,B}).
Run: python3 -I patterns_ref.py
"""
import itertools

ATOMS = ('m', 'a', 'A-a', 'b', 'B-b', 'rest')
M = frozenset(ATOMS)
E1 = {
    'C':  frozenset({'m', 'b', 'B-b'}),          # m u B
    "C'": frozenset({'m', 'a', 'A-a'}),          # m u A
    'X':  frozenset({'m', 'a', 'B-b'}),          # m u a u (B\b)
    'Y':  frozenset({'m', 'A-a', 'b'}),          # m u (A\a) u b
}
E = {1: E1, 2: {k: M - v for k, v in E1.items()}}
RELS = ['<', '>', '~', '|']   # relation of a to b: a<b (a strictly better), a>b, tie, incomparable


def le_sets(P, Q, r):
    """P <=_i Q for error sets, given r = relation of {a} vs {b} at world i; via cancellation."""
    p, q = P - Q, Q - P
    if not p:                       # P\Q empty: P <= Q by monotonicity
        return True
    if not q:                       # Q\P empty, P\Q nonempty: strict (G) says Q < P
        return False
    assert p in ({'a'}, {'b'}) and q in ({'a'}, {'b'}) and p != q, (p, q)
    if p == {'a'}:                  # a <= b ?
        return r in ('<', '~')
    return r in ('>', '~')          # b <= a ?


def le(i, U, V, r):
    return le_sets(E[i][U], E[i][V], r)


def lt(i, U, V, r):
    return le(i, U, V, r) and not le(i, V, U, r)


def admissible(r1, r2):
    R = {1: r1, 2: r2}
    kC = le(1, 'C', 'X', R[1]) or le(2, 'C', 'X', R[2])
    kCp = le(1, "C'", 'Y', R[1]) or le(2, "C'", 'Y', R[2])
    domC = all(le(i, 'X', 'C', R[i]) for i in (1, 2)) and any(lt(i, 'X', 'C', R[i]) for i in (1, 2))
    domCp = all(le(i, 'Y', "C'", R[i]) for i in (1, 2)) and any(lt(i, 'Y', "C'", R[i]) for i in (1, 2))
    return kC and kCp and not domC and not domCp


def edge_admissible(r1, r2):
    R = {1: r1, 2: r2}
    return (le(1, 'C', 'X', R[1]) or le(2, 'C', 'X', R[2])) and \
           (le(1, "C'", 'Y', R[1]) or le(2, "C'", 'Y', R[2]))


ok = sorted((r1, r2) for r1, r2 in itertools.product(RELS, RELS) if admissible(r1, r2))
print("(1) admissible patterns (world1, world2):", ok)
assert set(ok) == {('<', '<'), ('>', '>'), ('~', '~'), ('~', '|'), ('|', '~')}
okE = sorted((r1, r2) for r1, r2 in itertools.product(RELS, RELS) if edge_admissible(r1, r2))
print("    competitiveness only (edge, no EU):", len(okE), okE)
assert len(okE) == 9

# tie transfer used in S1.5(~,~): pattern (~,~) => C ~ X and C' ~ Y at both worlds
for i in (1, 2):
    assert le(i, 'C', 'X', '~') and le(i, 'X', 'C', '~') and le(i, "C'", 'Y', '~') and le(i, 'Y', "C'", '~')
print("    (~,~) ties X with C and Y with C' at both worlds: True")

# (2) coherence of splices on a discretised crossing
k = 5
corners = 0
both = []
for amask in range(1 << k):
    for bmask in range(1 << k):
        a = [(amask >> t) & 1 for t in range(k)]          # A cells ordered by sigma increasing
        b = [(bmask >> t) & 1 for t in range(k)]          # B cells ordered by tau increasing
        initial = lambda v: all(v[t] >= v[t + 1] for t in range(k - 1))   # 1...10...0
        final = lambda v: all(v[t] <= v[t + 1] for t in range(k - 1))     # 0...01...1
        X_coh = initial(a) and final(b)     # m u a u (B\b): sigma-initial a, tau-final b
        Y_coh = final(a) and initial(b)     # m u (A\a) u b: sigma-final a, tau-initial b
        if X_coh and Y_coh:
            both.append((amask, bmask))
full = (1 << k) - 1
print("(2) pairs with X and Y both coherent:", both)
assert set(both) == {(0, 0), (0, full), (full, 0), (full, full)}
print("    => (~,~) only at (0,0) [X=C] and (A,B) [X=C'];  (0,B),(A,0) are excluded by strict (G).")
