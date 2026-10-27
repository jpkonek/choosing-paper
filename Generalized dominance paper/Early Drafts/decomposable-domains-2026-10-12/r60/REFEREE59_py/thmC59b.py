"""thmC59b: classify the configurations where PP75 Theorem C's closed form and brute force disagree."""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thmC59 import *
kinds = [(kd, o, v) for kd in 'AB' for o in W3 for v in itertools.product((0, 1), repeat=3) if not (v[0] == v[1] == v[2])]
cnt = {}; ex = {}
for size in (1, 2, 3):
    for c in itertools.combinations(kinds, size):
        cfg = frozenset(c)
        bd, cf = brute_defeat(cfg), closed_form(cfg)
        if bd == cf: continue
        P2ne = any(a[2][0] != a[2][2] and a[2][0] == a[2][1] for a in cfg)
        key = ('N1' if n1(cfg) else 'notN1', 'N2' if P2ne else 'notN2', 'brute' if bd else 'closed')
        cnt[key] = cnt.get(key, 0) + 1
        ex.setdefault(key, sorted(cfg))
for k in sorted(cnt): print(k, cnt[k], ' e.g.', ex[k])
