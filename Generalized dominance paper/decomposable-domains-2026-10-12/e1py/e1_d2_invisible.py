"""E1.6: D2's world 1 is invisible to the sink-heavy shadow. Cell model of the D2 chain (n equal-mass cells in the
chain coordinate x; the near-one clause proxied by 'delta >= 0 on the last block'). Exact integer arithmetic.
Checks: (a) every regular delta in K0 has sum_k w_k delta_k >= 0 for random nondecreasing w (heavy at the end),
together with the summation-by-parts identity; (b) the world-1 error set of the Bayes model of (w*lambda, lambda) is an
initial segment {x < x_t}, i.e. a chain model; (c) every comparison C_b <=_1 B'_t has delta = 0 on the last block,
while every generator-based delta (delta - g_* in K0) is >= 1 on its target in the last block.
NUMERICS only. Run: python3 -I e1_d2_invisible.py"""
import random

random.seed(3)
n, B = 64, 8                       # cells; last block = cells n-B..n-1


def in_K0(d):
    tail = 0
    for k in range(n - 1, -1, -1):
        tail += d[k]
        if tail < 0:
            return False
    return all(d[k] >= 0 for k in range(n - B, n))


def rand_K0():
    # random rightward transports plus free additions, kept ternary
    d = [0] * n
    for _ in range(random.randint(1, 12)):
        i = random.randrange(n - B)
        j = random.randrange(i + 1, n)
        if d[i] > -1 and d[j] < 1:
            d[i] -= 1; d[j] += 1
    for _ in range(random.randint(0, 4)):
        k = random.randrange(n)
        if d[k] < 1:
            d[k] += 1
    return d


def rand_w():
    w, cur = [], 1
    for k in range(n):
        cur += random.choice([0, 0, 1, 2]) + (50 if k >= n - B and random.random() < 0.5 else 0)
        w.append(cur)
    return w


bad_a = bad_id = tested = 0
for _ in range(20000):
    d = rand_K0()
    if not in_K0(d):
        continue
    tested += 1
    w = rand_w()
    lhs = sum(wk * dk for wk, dk in zip(w, d))
    tails = [sum(d[k:]) for k in range(n)]
    rhs = w[0] * tails[0] + sum(tails[k] * (w[k] - w[k - 1]) for k in range(1, n))
    bad_id += (lhs != rhs)
    bad_a += (lhs < 0)
print(f"(a) K0 elements tested: {tested}; negative weighted sums: {bad_a}; summation-by-parts mismatches: {bad_id}")

bad_b = bad_c = gen_bad = 0
for _ in range(3000):
    w = rand_w()
    t1 = random.randint(1, 50); t2 = random.randint(1, 200)       # weight t = (t1, t2) up to scale
    E1 = [k for k in range(n) if t1 * w[k] < t2]                   # world-1 errors of the Bayes model (ties excluded below)
    if any(t1 * w[k] == t2 for k in range(n)):
        continue
    if E1 != list(range(len(E1))):
        bad_b += 1
    # dominator comparison C_b <=_1 B'_t: delta = 1_{E1 B'_t} - 1_{c_b}, b < n - B (C_b correct on the last block)
    bcut = random.randrange(n - B)
    delta = [(1 if k in E1 else 0) - (1 if k < bcut else 0) for k in range(n)]
    if all(t1 * w[k] > t2 for k in range(n - B, n)):              # heavy enough at the end for this t
        if any(delta[k] != 0 for k in range(n - B, n)):
            bad_c += 1
    # generator-based delta: g_* = 1_Q - 1_P with P in the first half, Q a random non-empty subset of the last block
    P = random.sample(range(n // 2), 3); Q = random.sample(range(n - B, n), 2)
    g = [0] * n
    for k in P: g[k] -= 1
    for k in Q: g[k] += 1
    kap = rand_K0()
    s = [g[k] + kap[k] for k in range(n)]
    if all(x in (-1, 0, 1) for x in s) and any(s[k] < 1 for k in Q):
        gen_bad += 1
print(f"(b) Bayes error sets that are not initial segments: {bad_b}")
print(f"(c) dominator deltas nonzero on the last block (heavy case): {bad_c}; generator deltas not >= 1 on their target: {gen_bad}")
