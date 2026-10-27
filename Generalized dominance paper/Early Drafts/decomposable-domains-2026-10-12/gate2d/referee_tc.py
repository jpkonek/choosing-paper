# Ungated vs gated (TC) violation counts, note's Phi vs check.py's Phi, on the chains.py configuration.
import sys
sys.path.insert(0, '.')
from fractions import Fraction as F
import check, chains
from referee_check import Sys, tc_violations
# 1) reproduce the note's 730,964 with check.py's own Phi (world 2 = on - 2 off)
print('chains.py as shipped (script Phi):', chains.chain_test(3, 1, 5, 256, gate=False)['TC_violations'])
# 2) same cells with the note's Phi (2 on - off at both worlds)
def phi_note(X, Y, w, on, off, ctx):
    m = lambda S: sum(ctx['mass'][c] for (c, j) in S)
    return 2*m(on) - m(off)
check.phi_sticky = phi_note
chains.phi_sticky = phi_note
r = chains.chain_test(3, 1, 5, 256, gate=False)
print('chains.py with note Phi, ungated:', r['TC_violations'])
r = chains.chain_test(3, 1, 5, 256, gate=True)
print('chains.py with note Phi, gated:', r['TC_violations'], r['weak_cycles'])
# 3) per world, my implementation
for phi in ('note', 'script'):
    S = Sys(3, 1, 5, 'note', phi)
    for w in (1, 2):
        print('referee', phi, 'world', w, 'ungated', tc_violations(S, w, False)[0], 'gated', tc_violations(S, w, True)[0])
