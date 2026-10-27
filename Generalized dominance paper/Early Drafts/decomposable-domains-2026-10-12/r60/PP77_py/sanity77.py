"""sanity77: V(T -> B_{3,t}) ~ p(-1,-1,2), alpha/beta ~ 2 (NUMERICS)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib77 import *
T = post((1, 1, 1)); B = post((1, 1, F(20, 21)))
mods = {'T': T, 'B': B}
At = atoms(mods); m = masses(mods, At, n=400_000)
Tv = [a['vals']['T'] for a in At]; Bv = [a['vals']['B'] for a in At]
print('V(T->B) =', Vrec(At, m, Tv, Bv))
al = sum(m[i] for i, a in enumerate(At) if Tv[i] != Bv[i] and a['o'] == 2)
be = [sum(m[i] for i, a in enumerate(At) if Tv[i] != Bv[i] and a['o'] == o) for o in (0, 1)]
print('alpha', al, 'beta', be, 'alpha/beta', al / be[0])
