"""Referee check: what happens at C2's candidate (I), W=(x,1,1/x)?  Factor both forms; test R along lines through e_b."""
import sympy as sp
exec(open('conics.py').read().split("# common line through")[0])
QaI = sp.factor(Qa_n.subs({wa: x, wc: 1/x})); QcI = sp.factor(Qc_n.subs({wa: x, wc: 1/x}))
print("Q^a at W_I:", QaI); print("Q^c at W_I:", QcI)
t, da, dc = sp.symbols('t da dc')
sub = {q[0]: t*da, q[1]: 1 - t*(da+dc), q[2]: t*dc}
for name, (A, B) in {'W_I': (x, 1/x), 'W_II': (kap, kap)}.items():
    PA = sp.Poly(sp.expand(sp.numer(sp.together(Qa_n.subs({wa: A, wc: B}).subs(sub)))), t)
    PC = sp.Poly(sp.expand(sp.numer(sp.together(Qc_n.subs({wa: A, wc: B}).subs(sub)))), t)
    La, Qa2, Lc, Qc2 = PA.coeff_monomial(t), PA.coeff_monomial(t**2), PC.coeff_monomial(t), PC.coeff_monomial(t**2)
    print(name, " La =", sp.factor(La), " Qa2 =", sp.factor(Qa2))
    print(name, " Lc =", sp.factor(Lc), " Qc2 =", sp.factor(Qc2))
    print(name, " R = Lc*Qa2-La*Qc2 =", sp.factor(sp.expand(Lc*Qa2 - La*Qc2)))
