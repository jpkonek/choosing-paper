"""S4 NUMERICS. Example A of S4_notes.md: additive nested two-world system on the chain coordinate
x in [0,1] (mu-bar = Lebesgue in x), world 2 density 1, world 1 density theta(x) increasing.
(1) eta_1(P,1) for slabs P=[1/2-m,1/2): smallest eta with rho1(d_{1-eta}) >= rho1(P).
(2) MP-sharp check: omega_1(s) := min mu(A) s.t. rho1(A) >= rho1(c_s) (bathtub, discretised) equals 1 - tau(s),
    tau(s) := sup{t : rho1(d_t) >= rho1(c_s)}.
(3) the 'R3 holds next to an additive partner' modulus kappa(m) for world 2 density w(x)=|x-x0|^(-1/2).
Run: python3 -I rate_examples.py
"""
import numpy as np

def run(alpha):
    # theta=(1-x)^(-alpha); rho1(d_{1-e}) = e^(1-alpha)/(1-alpha), so eta1(P,1) = ((1-alpha) rho1(P))^(1/(1-alpha))
    print(f"--- world-1 density (1-x)^(-{alpha})")
    Th = lambda x: -(1-x)**(1-alpha)/(1-alpha)
    for m in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.001]:
        rP = Th(0.5) - Th(0.5-m)
        eta = ((1-alpha)*rP)**(1/(1-alpha))
        print(f"m={m:7.4f}  rho1(P)={rP:.3e}  eta1(P,1)={eta:.3e}  eta/m={eta/m:.3e}  log(eta)/log(m)={np.log(eta)/np.log(m):.2f}")

run(0.5)
run(0.9)

print("--- (2) MP-sharp: omega_1(s) vs 1 - tau(s), discretised, theta=(1-x)^(-1/2)")
n = 200000
x = (np.arange(n) + 0.5)/n
th = (1 - x)**-0.5
cum = np.cumsum(th)/n            # rho1(c_x)
tot = cum[-1]
order = np.argsort(-th)          # bathtub: heaviest cells first
cumb = np.cumsum(th[order])/n
for s in [0.05, 0.2, 0.5, 0.8]:
    target = cum[int(s*n)-1]
    k = np.searchsorted(cumb, target)        # number of cells needed
    omega = (k+1)/n
    # tau: largest t with rho1(d_t) >= rho1(c_s)
    tail = tot - np.concatenate([[0.0], cum])  # rho1(d_{i/n})
    idx = np.where(tail >= target)[0].max()
    tau = idx/n
    print(f"s={s:4.2f}  omega1={omega:.5f}  1-tau={1-tau:.5f}")

print("--- (3) kappa(m)=inf{rho2(B): mu(B)>=m} and sup_x rho2(slab_eta(x)), rho2=|x-0.3|^(-1/2)")
w = np.abs(x - 0.3)**-0.5
ws = np.sort(w)
cw = np.cumsum(ws)/n
cumw = np.concatenate([[0.0], np.cumsum(w)/n])
for m in [0.1, 0.01, 0.001]:
    kap = cw[int(m*n)-1]
    # smallest eta with sup_x rho2((x-eta,x+eta)) >= kappa
    def supslab(eta):
        k = max(1, int(2*eta*n))
        return np.max(cumw[k:] - cumw[:-k])
    lo, hi = 1e-7, 0.5
    for _ in range(60):
        mid = (lo+hi)/2
        if supslab(mid) >= kap: hi = mid
        else: lo = mid
    print(f"m={m:6.3f}  kappa={kap:.4e}  eta2(m)~{lo:.3e}  eta2/m={lo/m:.3e}")
