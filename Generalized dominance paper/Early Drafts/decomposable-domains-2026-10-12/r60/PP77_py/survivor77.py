"""survivor77: the single pool candidate that escapes both endorse77 [2] and PP79 Cor A4 (T+520):
its vertex set, and PP79 bal2_79 (O4: two-ray-carried null records under PP78's base B)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP79_py'))
from mixed79 import pool
from bal2_79 import attack
P = pool()
K = P['T+520']
print('T+520 vertices:', [tuple(str(x) for x in k) for k in K])
h = attack(K, 'T+520')
print('fatal two-ray configurations under PP78 base (O4):', len(h), h[:6])
