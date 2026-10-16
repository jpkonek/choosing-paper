"""Second M0 referee: facet structure of hexagons around u (gauge-mixture examples, R10a)
and of random interior polygons; counts which triangle inputs of the p* in E branch fail.
Run: python3 -I hexagon_check.py"""
import numpy as np, importlib.util, sys, io, contextlib
spec = importlib.util.spec_from_file_location('gc', 'geometry_check.py')
gc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(gc)
u = np.ones(3) / 3
a = np.array([1, -1, 0]) / np.sqrt(2); b = np.array([1, 1, -2]) / np.sqrt(6)
for rot in [0.0, 0.2, np.pi / 6]:
    V = np.array([u + 0.15 * (np.cos(rot + k * np.pi / 3) * a + np.sin(rot + k * np.pi / 3) * b) for k in range(6)])
    gc.analyse(V, f'regular hexagon around u, rotation {rot:.3f}')
rng = np.random.default_rng(7)
stats = {'all_triangle_inputs': 0, 'some_corner_one_negative': 0, 'some_facet_without_2_relint_crossings': 0}
for _ in range(1000):
    m = rng.integers(4, 9)
    V = u + 0.2 * rng.normal(size=(m, 2)) @ np.vstack([a, b])
    if (V <= 0).any(): continue
    from scipy.spatial import ConvexHull
    V = V[ConvexHull(V @ np.vstack([a, b]).T).vertices]
    if len(V) < 4: stats['hull_is_triangle'] = stats.get('hull_is_triangle', 0) + 1; continue
    res, _ = gc.analyse(V, '', verbose=False)
    if res['two_cross_all'] and res['corner_two_neg']: stats['all_triangle_inputs'] += 1
    if not res['corner_two_neg']: stats['some_corner_one_negative'] += 1
    if not res['two_cross_all']: stats['some_facet_without_2_relint_crossings'] += 1
print('random interior polygons (hull with >= 4 vertices counted separately):', stats)
print('total relint crossings on the boundary cycle is always 6, so two per facet forces 3 facets')
