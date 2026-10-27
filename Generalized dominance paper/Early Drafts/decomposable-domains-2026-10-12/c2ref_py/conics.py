"""Referee check (independent of c2py): the gluing conics of C2 Lemma 4.2 / Prop 4.3.
Pencil vector written as H_k(q) = v_k x (C_k^T q), where c_k(h) = C_k h (writeup formulas for c_k), so
Q^k(q) = det(W q, v_k, C_k^T q).  Vertex b=2 (index 1), failing a=1 (index 0), c=3 (index 2), data x=x+.
kappa = x + 1/x - 1 (every eps in (0,1) <-> exactly one x>1).
Prints: the two quadratic forms; the common-line system through e_b and the coincidence system, solved with
x symbolic, and the list of x where the generic elimination could change (all polynomial pivots)."""
import sympy as sp

x = sp.Symbol('x', positive=True)
wa, wc, r = sp.symbols('wa wc r')
kap = x + 1/x - 1
eps = sp.simplify((kap - 1)/(kap + 2))
c0 = (1 - eps)/3
v = [sp.Matrix([c0 + (eps if i == k else 0) for i in range(3)]) for k in range(3)]
# C_k with c_k(h) = C_k h  (writeup Prop T1 normalisation, x1=x2=x3=x)
C = [sp.Matrix([[0, -x, -1], [0, x, 0], [0, 0, 1]]),
     sp.Matrix([[1, 0, 0], [-1, 0, -x], [0, 0, x]]),
     sp.Matrix([[x, 0, 0], [0, 1, 0], [-x, -1, 0]])]
q = sp.Matrix(sp.symbols('q1 q2 q3'))
W = sp.diag(wa, 1, wc)


def Qform(k):
    M = sp.Matrix.hstack(W*q, v[k], C[k].T*q)
    return sp.factor(sp.together(sp.expand(M.det())))


Qa, Qc = Qform(0), Qform(2)
Qa_n = sp.numer(sp.together(Qa)); Qc_n = sp.numer(sp.together(Qc))
print("Q^a numerator:", sp.factor(Qa_n))
print("Q^c numerator:", sp.factor(Qc_n))
e2 = {q[0]: 0, q[1]: 1, q[2]: 0}
print("Q^a(e_b), Q^c(e_b):", sp.simplify(Qa_n.subs(e2)), sp.simplify(Qc_n.subs(e2)))

# common line through e_b and D=(1,0,r):  B(e_b,D)=0 and Q(D)=0 for both forms
def polar(Qn, P1, P2):
    s = sp.Symbol('s')
    f = sp.expand(Qn.subs({q[i]: P1[i] + s*P2[i] for i in range(3)}))
    return sp.Poly(f, s).coeff_monomial(s)/2  # = B(P1,P2) since Q(P1)=0 here

E = [0, 1, 0]; D = [1, 0, r]
eqs = []
for Qn in (Qa_n, Qc_n):
    eqs.append(sp.factor(sp.expand(polar(Qn, E, D))))
    eqs.append(sp.factor(sp.expand(Qn.subs({q[0]: 1, q[1]: 0, q[2]: r}))))
print("\nCommon-line system (each must vanish):")
for e_ in eqs:
    print("   ", e_)
# solve with x symbolic
solII = sp.solve(eqs, [wa, wc, r], dict=True)
print("Common-line solutions (generic x):", [{k: sp.simplify(vv) for k, vv in s_.items()} for s_ in solII])

# coincidence: coefficient vectors proportional
mons = [q[0]**2, q[1]**2, q[2]**2, q[0]*q[1], q[0]*q[2], q[1]*q[2]]
Pa = sp.Poly(sp.expand(Qa_n), *q); Pc = sp.Poly(sp.expand(Qc_n), *q)
ca = [Pa.coeff_monomial(m) for m in mons]; cc = [Pc.coeff_monomial(m) for m in mons]
print("\ncoefficients Q^a:", [sp.factor(t) for t in ca])
print("coefficients Q^c:", [sp.factor(t) for t in cc])
minors = [sp.factor(sp.expand(ca[i]*cc[j] - ca[j]*cc[i])) for i in range(6) for j in range(i+1, 6)]
minors = [m for m in minors if m != 0]
solI = sp.solve(minors, [wa, wc], dict=True)
print("Coincidence solutions (generic x):", [{k: sp.simplify(vv) for k, vv in s_.items()} for s_ in solI])
