"""exh59b: is the restricted family Z[S -> B] complete for single-domination defeat (strict guidance counted)?
Independent of PP76's check_defeat76: own brute force over all copies (exh59.forced)."""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exh59 import *
random.seed(77)
n = 4; models = list(itertools.product((0, 1), repeat=n))
tot = dfull = drest = 0
for Kt in itertools.product([(kd, o) for kd in 'AB' for o in range(3)], repeat=n):
    if random.random() > 0.05: continue
    K = list(Kt); T = tuple(random.choice((0, 1)) for _ in range(n))
    for B in models:
        for X in models:
            if B == X or any(sworse(K, w, B, X) for w in range(3)): continue
            if not any(B[g] == T[g] != X[g] for g in range(n)): continue
            R = refused_rivals(K, T, B, X, models)
            full = [Z for Z in models if Z != T and all(sworse(K, w, T, Z) or Z in R[w] for w in range(3))]
            rest = [Z for Z in full if all(Z[g] in (T[g], B[g]) for g in range(n))]
            tot += 1; dfull += bool(full); drest += bool(rest)
print('single dominations: %d ; T defeated (all copies): %d ; defeated by some T[S -> B]: %d' % (tot, dfull, drest))
