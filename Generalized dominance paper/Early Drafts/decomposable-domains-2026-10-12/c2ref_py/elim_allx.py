"""Referee check: hand elimination of the common-line system for EVERY x>1 (no exceptional set).
Also: the forms Q^a, Q^c are never proportional for w>0 (q1^2, q3^2 coefficients), and the C2 candidate (I)
shares only a line NOT through e_b.  Then repeat the exact solve at all three vertices via cyclic relabelling,
and at the x_- data via the transposition (1 2), at several rational x (sanity)."""
import sympy as sp
src = open('conics.py').read().split("solII = ")[0]
exec(src)
E1, E2, E3, E4 = [sp.numer(sp.together(e_)) for e_ in eqs]
# r = 0 branch
print("r=0 branch:", sp.solve([E1.subs(r, 0), E2.subs(r, 0), E3.subs(r, 0)], [wa, wc], dict=True))
# r != 0: E1, E3 linear in (wa, wc)
lin = sp.solve([E1, E3], [wa, wc], dict=True)[0]
print("from E1,E3: wa =", sp.factor(lin[wa]), "; wc =", sp.factor(lin[wc]))
print("E2 residual:", sp.factor(sp.together(E2.subs(lin))))
print("E4 residual:", sp.factor(sp.together(E4.subs(lin))))
# positivity of wa, wc forces 0<r<1 ; the residual factor then gives r = 1/x
print("check at r=1/x: wa, wc =", sp.simplify(lin[wa].subs(r, 1/x)), sp.simplify(lin[wc].subs(r, 1/x)), " kappa =", sp.simplify(kap))
