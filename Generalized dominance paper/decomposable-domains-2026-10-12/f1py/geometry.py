# F1 (A): where is the far end x -> 1 of the D2 chain?  Host A = C2.1 path, host B = two-phase path.
# Exact formulas: for a mixed h = r(cos th, sin th), T(h) = h1/(h1-h2) = cos/(cos - sin); M+ = th in (th_b, 0),
# M- = th in (pi/2, th_a); T maps both increasingly onto (beta',1) and (0,alpha').
# Prints: membership of the two candidate end rays in U, the law of the uniformised x near 1 on M+ (host A: density
# bounded below; host B: zero), and truncated integrals of 1/(1-x) over the compact K_eta = {1<=|h|<=2, |th|<=eta}.
import math
al, be = 0.3, 0.6                      # K' = [alpha', beta'] (any values in (0,1) with al<=be)
T = lambda th: math.cos(th) / (math.cos(th) - math.sin(th))
th_b = math.atan2(be - 1, be)          # boundary ray (beta', beta'-1): T = beta'
th_a = math.atan2(1 - al, -al)         # boundary ray (-alpha', 1-alpha'): T = alpha'
P = lambda h: min((1 - t) * h[0] + t * h[1] for t in (al, be))   # P_{K'}(h)
print("T(th_b) =", round(T(th_b), 12), " T(th_a) =", round(T(th_a), 12))
print("P_K'((1,0)) =", P((1, 0)), "> 0 : ray (1,0) is in the open cone U")
print("P_K'((-al,1-al)) =", round(P((-al, 1 - al)), 15), ": ray (-alpha',1-alpha') is on dU")
# derivative bounds T'(th) = 1/(cos-sin)^2 on the closed ranges
def dT(th): return 1 / (math.cos(th) - math.sin(th)) ** 2
gp = [th_b + (0 - th_b) * k / 2000 for k in range(2001)]
gm = [math.pi / 2 + (th_a - math.pi / 2) * k / 2000 for k in range(2001)]
print("T' on [th_b,0]: [%.4f, %.4f];  on [pi/2,th_a]: [%.4f, %.4f]" % (min(map(dT, gp)), max(map(dT, gp)), min(map(dT, gm)), max(map(dT, gm))))
angM = (0 - th_b) + (th_a - math.pi / 2)  # angular size of M (lambda = angle / angM, radius independent)
def lam_xA_below(s):   # lambda{x_A < s}, host A: x_A = (T-be)/(1-be) on M+, T/al on M-
    Tp = be + (1 - be) * s; Tm = al * s
    thp = math.atan2(-(1 - Tp), Tp) if Tp < 1 else 0.0   # T(th)=Tp on M+  <=> tan th = 1 - 1/Tp
    thp = math.atan(1 - 1 / Tp)
    thm = math.pi + math.atan(1 - 1 / Tm) if Tm > 0 else math.pi / 2
    return ((thp - th_b) + (thm - math.pi / 2)) / angM
def lam_xB_below(s):   # host B: x_B = (T-be)/(2(1-be)) on M+, 1/2 + T/(2 al) on M-
    if s <= 0.5:
        Tp = be + (1 - be) * 2 * s; thp = math.atan(1 - 1 / Tp); return (thp - th_b) / angM
    Tm = al * (2 * s - 1); thm = math.pi + math.atan(1 - 1 / Tm) if Tm > 0 else math.pi / 2
    return ((0 - th_b) + (thm - math.pi / 2)) / angM
# check monotone, continuous, onto [0,1]
for name, F in (("A", lam_xA_below), ("B", lam_xB_below)):
    vals = [F(k / 1000) for k in range(1, 1000)]
    print("host %s: G(0+)=%.4f G(1-)=%.6f increasing=%s" % (name, vals[0], vals[-1], all(b >= a for a, b in zip(vals, vals[1:]))))
# x(th) on M+ near th = 0 (the ray (1,0)), host A and host B
def x_of_th_A(th):  # th in (th_b,0) on M+
    s = (T(th) - be) / (1 - be); return lam_xA_below(s)
def x_of_th_B(th):
    s = (T(th) - be) / (2 * (1 - be)); return lam_xB_below(s)
print("\n th(M+)      1-x_A(th)     (1-x_A)/|th|     x_B(th)")
for e in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5):
    th = -e
    print("%9.1e  %12.5e  %12.6f  %12.6f" % (th, 1 - x_of_th_A(th), (1 - x_of_th_A(th)) / e, x_of_th_B(th)))
print("=> host A: 1 - x ~ c|th| on M+ near the INTERIOR ray (1,0); host B: x stays at lambda(M+) < 1 there.")
# truncated integral of 1/(1-x) over K_eta (radial factor varpi for 1<=|h|<=2; angular density 1/(2 pi) of mu)
varpi = math.exp(-0.5) - math.exp(-2.0)
eta = 0.05
def trunc_int(xfun, cut):
    n = 200000; tot = 0.0
    for k in range(n):       # midpoint rule in th over [-eta, -cut)
        th = -eta + (eta - cut) * (k + 0.5) / n
        tot += 1 / (1 - xfun(th))
    return varpi / (2 * math.pi) * tot * (eta - cut) / n
print("\n cut     int_{K_eta, th<-cut} 1/(1-x_A) dmu     same for host B")
for cut in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
    print("%7.0e   %14.6f                      %10.6f" % (cut, trunc_int(x_of_th_A, cut), trunc_int(x_of_th_B, cut)))
print("=> host A: grows like log(1/cut) (not locally integrable on U); host B: bounded.")
