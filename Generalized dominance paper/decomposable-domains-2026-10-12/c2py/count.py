import numpy as np
from families import gambles
from horn import clauses
F, tags, v = gambles(0.3, taus=(0.25, 0.5, 0.75), shifts=(-0.01, 0.01), box=True)
SF = np.vstack([F, -F])
cl = clauses(SF)
print(len(F), len(cl), sum(1 for c in cl if len(c[0]) == 1), sum(1 for c in cl if len(c[1]) == 0))
