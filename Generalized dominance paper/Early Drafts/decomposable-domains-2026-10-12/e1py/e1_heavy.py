"""E1.4 (protection lemma instance) and E1.5 (inertness: sink-heavy reweighting) for T1. NUMERICS only.
Run: python3 -I e1_heavy.py"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from e1_common import *

rng = np.random.default_rng(5)
G = sample_U(rng, 300000)
T = in_DT(G)
COR = correct(G, T)


def rand_field(G):
    """random smooth positive multipliers"""
    A = rng.normal(size=(3, 3)); B = rng.normal(size=3)
    return 1.0 + 0.9 * np.sin(G @ A + B) ** 2


# ---- random admissible shadows: raise correct-world weights, lower error weights (T1 stays Bayes at u)
L = 4.0
fails = 0
nsh = 20
sink_err_before = 0
sink_err_after = 0
for r in range(nsh):
    Up = rand_field(G); Dn = 1.0 / rand_field(G)
    W = np.where(COR, L * Up, Dn)
    acc, tie = bayes(G, W, u)
    if not np.all(acc == T):
        fails += 1
    # sink for world 1: (+,-,-) gambles near the e1 ray, depth m: max(|g2|,|g3|) <= 2^-m g1
    # sample the sink directly (it has tiny measure)
    for m in range(3, 18):
        a = rng.uniform(0, 2.0 ** -m, size=(2000, 2))
        S = np.column_stack([np.ones(2000), -a[:, 0], -a[:, 1]])
        S /= np.linalg.norm(S, axis=1, keepdims=True)
        assert np.all(in_U(S)) and np.all(in_DT(S))            # T1 accepts: T1 is world-1-correct on the sink
        CS = correct(S, in_DT(S))
        WS = np.where(CS, L * rand_field(S), 1.0 / rand_field(S))
        # heavy reweighting at world 1: f = k (w2+w3)/w1 on depth m_k; here depth m -> k = m
        WSh = WS.copy(); WSh[:, 0] = WS[:, 0] * (1 + m * (WS[:, 1] + WS[:, 2]) / WS[:, 0])
        for _ in range(20):
            t = rng.dirichlet([0.3, 1, 1])
            accb, _ = bayes(S, WS, t)
            acch, _ = bayes(S, WSh, t)
            if m > 1 / t[0]:
                sink_err_after += int((~acch).sum())          # heavy shadow must be world-1-correct (accept) here
            sink_err_before += int((~accb).sum())
print(f"random admissible shadows: B_u != T1 in {fails}/{nsh}")
print(f"sink samples rejected (world-1 errors) by unweighted shadows over random t: {sink_err_before}")
print(f"sink samples at depth m > 1/t_1 rejected by the sink-heavy shadow: {sink_err_after} (must be 0)")

# heaviness keeps T1 Bayes at u on generic samples: raise world-1 weight on (+,-,-) gambles near the e1 ray
W = np.where(COR, L, 1.0)
near = (G[:, 0] > 0) & (G[:, 1] < 0) & (G[:, 2] < 0) & (np.maximum(-G[:, 1], -G[:, 2]) < 0.25 * G[:, 0])
Wh = W.copy(); Wh[near, 0] *= 1000.0
acc, tie = bayes(G, Wh, u)
print("heavy reweighting on a T1-correct region keeps B_u == T1:", bool(np.all(acc == T)), " region size:", int(near.sum()))

# ---- protection lemma (E1.4) instance: additive neighbours rho2, rho3; p in E_1(T1) arbitrarily deep, R in (+,-,-) n T1
rho2, rho3 = rand_field(G), rand_field(G)
E1T = ~COR[:, 0]
R = (G[:, 0] > 0) & (G[:, 1] < 0) & (G[:, 2] < 0) & T
print("R = (+,-,-) n T1 non-null (sample count):", int(R.sum()), "; E_1(T1) count:", int(E1T.sum()))
# world-2/3 change of toggling D = p u R, p a small subset of E_1(T1): R fixes worlds 2,3; p costs at most rho(p)
p = np.where(E1T)[0][:50]
d2 = -rho2[R].sum() + rho2[p].sum() * 1.0
d3 = -rho3[R].sum() + rho3[p].sum() * 1.0
print(f"toggling p u R changes rho2-error by {d2:.1f} and rho3-error by {d3:.1f} (both < 0: forced at world 1, delta = 1_R - 1_p)")
