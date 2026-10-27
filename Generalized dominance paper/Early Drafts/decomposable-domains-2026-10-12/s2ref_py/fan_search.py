"""S2 referee check (2): crossing tie-splits on an edge whose two worlds i, j are additive.

Finite face model (S2.0(a)): on the tie face Z of the edge weight s0, rho_j = kappa*rho_i, so every split of Z
with the same rho_i-level has the same (psi_i, psi_j). Cells c = 0..m-1 of equal rho_i-mass. A split S
(cells where the model errs at world i) at level |S|. World k: toggling cell c from model Y's advice changes
Y's world-k error weight by +w(c) if Y is k-correct at c, -w(c) if k-wrong (one weight vector per 'judge').
  * complete k  : additive (one judge) or lexicographic (two judges, lex);
  * incomplete k: unanimity of two judges.
C, F are face splits that CROSS (neither contains the other). Requirements tested exhaustively over all
balanced exchanges T (|T cap S| = |T \\ S|, T nonempty) from C and from F:
  (U)  no exchange strictly improves at world k while tying i, j (undominatedness inside the face);
  (NT) no exchange ties at every world (otherwise (C) is violated by a bounded, hence incoherent, splice).
Referee's claim (PROVED in S2_referee.md, Prop. R-S2.A): with k complete, no crossing pair passes (U)+(NT).
With k incomplete, crossing pairs passing (U)+(NT) exist (the 'fan' of S2.4 is locally consistent).
"""
import itertools, random
random.seed(5)

def delta(T, S, kc, judges):
    # change of world-k error weight per judge when toggling T from the split S; kc[c]: model C k-correct at c
    return tuple(sum(w[c] * (1 if kc[c] else -1) for c in T) for w in judges)

def le_k(kind, d):          # is X <=_k Y given d = weight(X) - weight(Y) per judge ?
    if kind == 'unan':
        return all(x <= 1e-12 for x in d)
    for x in d:             # 'add' (one judge) or 'lex'
        if abs(x) > 1e-12:
            return x < 0
    return True

def ok_model(S, kc, judges, kind, m):
    inside, outside = sorted(S), [c for c in range(m) if c not in S]
    for r in range(1, min(len(inside), len(outside)) + 1):
        for Q in itertools.combinations(inside, r):
            for P in itertools.combinations(outside, r):
                d = delta(P + Q, S, kc, judges)
                X_le_Y = le_k(kind, d); Y_le_X = le_k(kind, tuple(-x for x in d))
                if X_le_Y and Y_le_X:
                    return False            # tie at every world: (NT) fails
                if X_le_Y and not Y_le_X:
                    return False            # X strictly better at k, tied at i, j: (U) fails
    return True

def search(kind, trials=3000):
    found = 0
    for _ in range(trials):
        m = random.randint(3, 6)
        nj = 1 if kind == 'add' else 2
        judges = [[random.uniform(.1, 2) for _ in range(m)] for _ in range(nj)]
        kcC = [random.random() < .5 for _ in range(m)]                     # C's world-k correctness
        SC = frozenset(c for c in range(m) if random.random() < .5)
        SF = frozenset(c for c in range(m) if random.random() < .5)
        if SC <= SF or SF <= SC:
            continue
        kcF = [kcC[c] ^ ((c in SC) != (c in SF)) for c in range(m)]     # differing advice flips correctness
        if ok_model(SC, kcC, judges, kind, m) and ok_model(SF, kcF, judges, kind, m):
            found += 1
            if found == 1:
                ex = (m, sorted(SC), sorted(SF), kcC, [[round(x, 3) for x in w] for w in judges])
    return found, (ex if found else None)

for kind in ['add', 'lex', 'unan']:
    f, ex = search(kind)
    print(f'world k = {kind:4s}: crossing pairs passing (U)+(NT) among random trials: {f}')
    if ex:
        print('   example (m, S_C, S_F, C k-correct per cell, judges):', ex)

# Item 5 of S2.4 (referee's strengthening: strict (G) alone suffices): in every surviving crossing pair,
# C is world-k-wrong on ALL of A = S_F \ S_C or on ALL of B = S_C \ S_F (and likewise for F).
def item5(trials=3000):
    viol = tot = 0
    for _ in range(trials):
        m = random.randint(3, 6)
        judges = [[random.uniform(.1, 2) for _ in range(m)] for _ in range(2)]
        kcC = [random.random() < .5 for _ in range(m)]
        SC = frozenset(c for c in range(m) if random.random() < .5)
        SF = frozenset(c for c in range(m) if random.random() < .5)
        if SC <= SF or SF <= SC:
            continue
        kcF = [kcC[c] ^ ((c in SC) != (c in SF)) for c in range(m)]
        if ok_model(SC, kcC, judges, 'unan', m) and ok_model(SF, kcF, judges, 'unan', m):
            tot += 1
            A, B = SF - SC, SC - SF
            for kc in (kcC, kcF):
                if not (all(not kc[c] for c in A) or all(not kc[c] for c in B)):
                    viol += 1
    return tot, viol
print('item 5 check (unanimity world k): surviving crossing pairs, violations of item 5:', item5())
