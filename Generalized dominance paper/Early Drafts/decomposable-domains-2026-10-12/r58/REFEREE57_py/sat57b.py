"""sat57b: PP71's V1 splice test with its full rival universe (the 138 sampled consecutive splices, regenerated with
PP71's own sampling procedure, random.Random(71), on the identical cell order), using the referee's encoder.
Tests: (a) core requirements with all 138 splices present as rivals; (b) same without the cycle;
(c) which rivals matter: greedy removal of rival splices (not of requirements) keeping UNSAT."""
import sys, random
sys.path.insert(0, '.')
from sat57 import *

rnd = random.Random(71)
spl = []
for i in range(4):
    a, b = C[i], C[(i + 1) % 4]
    D = [j for j in range(nc) if a[j] != b[j]]
    seen = set()
    while len(seen) < min(40, 2 ** len(D) - 2):
        H = tuple(sorted(rnd.sample(D, rnd.randint(1, len(D) - 1))))
        seen.add(H)
    for H in sorted(seen):
        spl.append(tuple(b[j] if j in H else a[j] for j in range(nc)))
spl = [z for z in dict.fromkeys(spl) if z not in C and z != T]
core = [splice(i, H) for i, H in CORE]
print('regenerated splices:', len(spl), '; core inside:', all(z in spl for z in core))
allfills = [f for i in range(4) for f in FILLS[i]]
cyc = [(C[(i + 1) % 4], f) for i in range(4) for f in FILLS[i]]
base_models = C + [T] + allfills
E, r = run('(a) core requirements, all 138 splices present as rivals', base_models + spl, cyc, core)
run('(b) same, without the cycle', base_models + spl, [], core)
run('(c) all 138 dominated, no cycle', base_models + spl, [], spl)
if not r:
    # greedy: which rival splices (outside the core) are needed in the universe?
    riv = [z for z in spl if z not in core]
    k = 0
    while k < len(riv):
        trial = riv[:k] + riv[k + 1:]
        E2, r2 = run('   drop rival %d' % k, base_models + core + trial, cyc, core)
        if not r2: riv = trial
        else: k += 1
    print('rival splices needed besides the 11 core splices:', len(riv))
    for z in riv:
        for i in range(4):
            a, b = C[i], C[(i + 1) % 4]
            if all(z[j] in (a[j], b[j]) for j in range(nc)):
                print('   %s[H -> %s], H = %s' % (NAMES[i], NAMES[(i + 1) % 4], [cells[j][0] for j in range(nc) if z[j] != a[j]]))
                break
    run('final: core + needed rivals, with cycle', base_models + core + riv, cyc, core)
    run('final: core + needed rivals, without cycle', base_models + core + riv, [], core)
