"""Exact verification, using only integer arithmetic and Python's standard library."""
from pathlib import Path
import json

root = Path(__file__).parent
data = json.loads((root / 'finite_order.json').read_text())
n, order = data['n'], data['order']
size = 1 << n
assert set(order) == set(range(size)) and len(order) == size
rank = {subset: k for k, subset in enumerate(order)}

for a in range(size):
    for b in range(size):
        if a != b and (a & b) == a:
            assert rank[a] < rank[b], ('inclusion', a, b)
        aa, bb = a & ~b, b & ~a
        assert (rank[a] <= rank[b]) == (rank[aa] <= rank[bb]), ('independence', a, b)

certificate = [(37, 2), (34, 13), (6, 48), (25, 38)]
assert all(rank[a] < rank[b] for a, b in certificate)
total = [sum(((b >> i) & 1) - ((a >> i) & 1) for a, b in certificate) for i in range(n)]
assert total == [-1, 0, 0, 0, 0, 0]

def thresholds(profile):
    return tuple(sum(1 << j for j, value in enumerate(profile) if value >= cutoff)
                 for cutoff in (3, 2, 1))

profiles = [tuple((x >> (2*j)) & 3 for j in range(n)) for x in range(4**n)]
keys = {x: tuple(rank[s] for s in thresholds(x)) for x in profiles}
assert len(set(keys.values())) == len(profiles)
for x in profiles:
    for j in range(n):
        if x[j] < 3:
            y = list(x); y[j] += 1
            assert keys[x] < keys[tuple(y)], ('rank monotonicity', x, tuple(y))

result = {'ordered_subset_pairs_verified': size**2,
          'rank_profiles_verified': len(profiles),
          'short_certificate': certificate, 'sum_difference': total}
(root / 'finite_order_certificate.json').write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
