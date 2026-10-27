"""PP76 check_defeat76 (CHECKED, exact): does counting ALL common-context copies (Theorem 1.1, with the
off-support part G2) defeat a committed source Z in cases where the restricted family of rivals
Z[S -> B] (PP75 (N3)/Theorem C; PP74 item 4) shows no defeat?  Defeat: some rival W of Z refused at
every world, by strict guidance or by a first-generation coupled refusal of one domination B <= X."""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hlib76 import *
n = 4; allm = models(n)
tot = d_full = d_restr = extra = 0; ex = None; ex0 = None
for O, Z in itertools.product(itertools.product(range(3), repeat=n), [(1,1,1,1),(1,1,1,0),(1,1,0,0)]):
    for B in allm:
        for X in allm:
            if B == X or any(strictly_worse(O, w, B, X) for w in range(3)): continue
            if not any(B[g] == Z[g] != X[g] for g in range(n)): continue    # Lemma 1.3 at Z
            forced = {w: {apply(Z, r) for r in coupled_refusals(O, B, X, w, allm) if carries(Z, r)} for w in range(3)}
            def defeated(W): return all(strictly_worse(O, w, Z, W) or W in forced[w] for w in range(3)) and W != Z
            full = [W for W in allm if defeated(W)]
            restr = [W for W in full if all(Z[g] == W[g] or B[g] == W[g] for g in range(n))]
            if full and ex0 is None: ex0 = (O, Z, B, X, full)
            tot += 1; d_full += bool(full); d_restr += bool(restr)
            if full and not restr:
                extra += 1
                if ex is None: ex = (O, Z, B, X, full[0])
print('dominations:', tot, ' Z defeated (all copies):', d_full, ' defeated by some Z[S->B]:', d_restr, ' defeats missed by the restricted family:', extra)
print('example (O, Z, B, X, defeating rival):', ex)
print('first defeat:', ex0)
