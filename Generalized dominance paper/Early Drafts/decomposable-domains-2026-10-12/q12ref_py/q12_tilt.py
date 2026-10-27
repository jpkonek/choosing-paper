# New observation (Q12 ref, §N3): exponential-tilt first-order-dominance cones are nested in K, so their union
# is a legitimate cancellative strictly monotone world; but it accepts every cut pair with non-null target,
# and the section of A = c_x \ Z (Z left of x) is [0,x): open, exactly as Lemma DL predicts.
# Exact check on interval sets with a symbolic-free numeric tail test (high K, mpmath-free floats are enough
# for the sign pattern; we also report the smallest K that works for each b).
import math
def tail_ok(P, Q, K, grid=400):
    # delta = 1_Q - 1_P on [0,1]; tau_K(y) = int_{z>=y} e^{Kz} delta(z) dz >= 0 for all y?  (closed forms)
    def I(lo, hi, y):  # int_{max(lo,y)}^{hi} e^{Kz} dz
        l = max(lo, y)
        if l >= hi: return 0.0
        return (math.exp(K*hi) - math.exp(K*l))/K
    pts = sorted({0.0, 1.0} | {p for s in P+Q for p in s})
    return all(sum(I(lo, hi, y) for lo, hi in Q) - sum(I(lo, hi, y) for lo, hi in P) >= -1e-12*math.exp(K)
               for y in pts)
x, Z = 0.6, [(0.1, 0.3)]
for b in [0.5, 0.59, 0.599, 0.5999]:
    P, Q = Z, [(b, x)]                           # cut pair (Z, [b,x)) at cut b: c_b \ A = Z, A \ c_b = [b,x)
    K = next(k for k in range(1, 200000) if tail_ok(P, Q, k))
    print(f"b={b}: (Z,[b,x)) accepted from K={K} on; so b in S1(c_x minus Z)")
print("b = x: c_x \\ A = Z, A \\ c_x = empty: never accepted (strict (G)). Section [0,x) is open.")
