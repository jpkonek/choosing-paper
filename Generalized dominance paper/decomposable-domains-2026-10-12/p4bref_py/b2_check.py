# Prop B2 (P4) checks.  World 1 = lex(nu+, lambda), nu+ a right density at x0 with nu+(I) = 1.
# Then c_b <=_1 A depends only on (g, l) = (nu+(A), lambda(A)):
#   (g - f(b), l - b) >=_lex 0,  f(b) = nu+(c_b) = 1[b > x0].
# (a) sections are closed for every attainable (g,l);  (b) SP:
#   - if nu+ is {0,1}-valued (ultrafilter-type), nu = lambda + nu+ endorses every comparison: SP HOLDS;
#   - if nu+ takes arbitrarily small positive values on disjoint sets, SP fails (c_{x0} <=_1 A_j).
# (c) the repaired witness for B2(b): A = c_{x0} u (x0+h, 1) has nu+(A) = 0 and phi_1(A) = x0
#     (contradicting strict escape) for EVERY such nu+; P4's witness needs 0 < nu+(D) < 1.
from fractions import Fraction as Fr
x0 = Fr(2, 5)
def f(b): return 1 if b > x0 else 0
def le(b, g, l):
    d1 = g - f(b)
    return d1 > 0 or (d1 == 0 and l - b >= 0)
grid = [Fr(i, 200) for i in range(201)]
gs = [Fr(0), Fr(1, 7), Fr(1, 2), Fr(1)]
bad = 0
for g in gs:
    for l in grid:
        if l == 0 and g > 0: continue
        S = [b for b in grid if le(b, g, l)]
        e = max(S)
        # initial segment and closed: check S == grid up to e, and fine check just above e
        if S != [b for b in grid if b <= e]: bad += 1
        # exact supremum: candidates x0, l, 1 ; verify sup attained
        sup = max([b for b in [x0, l, Fr(1), Fr(0)] if le(b, g, l)] + [Fr(0)])
        above = sup + Fr(1, 10**9)
        if above <= 1 and le(above, g, l): bad += 1
print('(a) section shape violations (non-initial or non-closed):', bad)
# (b) ultrafilter-type nu+: g in {0,1}; nu = lambda + nu+ ; nu(c_b) = b + f(b)
viol = 0
for g in [Fr(0), Fr(1)]:
    for l in grid:
        for b in grid:
            if le(b, g, l) and l + g < b + f(b): viol += 1
print('(b) {0,1}-valued nu+: violations of (lambda+nu+)(A) >= (lambda+nu+)(c_b):', viol, '=> SP holds')
# diffuse nu+: comparisons c_{x0} <=_1 A_j with g_j = 2^-j, l_j = 2^-j  -> any endorsing nu has nu(c_x0) <= nu(A_j)
print('    diffuse nu+: c_x0 <=_1 A_j for g_j=2^-j:', all(le(x0, Fr(1, 2**j), Fr(1, 2**j)) for j in range(1, 30)))
# (c) repaired witness
h = Fr(1, 10)
g, l = Fr(0), x0 + (1 - x0 - h)
S = [b for b in grid if le(b, g, l)]
print('(c) A = c_x0 u (x0+h,1): nu+(A)=0, lambda(A)=', l, ', max section on grid =', max(S),
      '; phi_1(A) = x0 although A strictly contains c_x0')
