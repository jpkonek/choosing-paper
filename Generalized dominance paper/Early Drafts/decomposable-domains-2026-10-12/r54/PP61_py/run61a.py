"""PP61 run A: build the exact instance, validate the clause generator against Lambda_w.

(1) For random generic atom weights w, Lambda_w (PP56 relation, field w*u^1, atom localisations)
    satisfies EVERY clause generated (G, DEF, UND, C, SEC, TC on all ordered triples).  This is the
    finite form of Prop F (and a test of the encoder: Theorem L guarantees the non-section clauses).
(2) For unit weights (the u^1-balanced masses) Lambda_1 violates some SEC clause, on a balanced swap:
    Theorem Q / PP57 Prop 4.5 reproduced on the instance.
(3) The plain relational SAT problem (with lazy TC) is solved; the solution is re-checked exactly.
"""
import sys, os, time, random, pickle
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fractions import Fraction as Fr
from geom61 import Geometry, G3, G5
from inst61 import Inst, Encoding, solve, check_assignment, lambda_assignment
from build61 import swap_spec


def build(G, shifts='all', pairs=None, **kw):
    geo = Geometry(G)
    proto = Inst(geo, [], pads=False)
    if pairs is None:
        pairs = [(a, b) for a in geo.names for b in geo.names if a < b]
    spec, kinds = swap_spec(proto, pairs, **kw)
    sh = [(nm, w) for nm in geo.names for w in range(3)] if shifts == 'all' else shifts
    inst = Inst(geo, spec, pads=True, shifts=sh, kinds=kinds)
    return inst, kinds


if __name__ == '__main__':
    label = sys.argv[1] if len(sys.argv) > 1 else 'G3'
    G = {'G3': G3, 'G5': G5}[label]
    t0 = time.time()
    kw = dict(max_bal2=4, max_bal3=2) if label == 'G3' else dict(max_bal2=2, max_bal3=1)
    inst, kinds = build(G, **kw)
    enc = Encoding(inst)
    print('[%s] base models %d (sources %d, swaps %d), shifts %d, atoms %d, records %d, vars %d, clauses %d  (%.0fs)' % (
        label, len(inst.base_models), len(inst.geo.names), len(inst.swaps), len(inst.subs), len(inst.atoms),
        len(enc.recs), enc.nvars, len(enc.clauses), time.time() - t0))
    from collections import Counter
    print('   swap kinds:', Counter(kinds[(a, b, F)] for (n, a, b, F) in inst.swaps))
    print('   clause kinds:', Counter(t.split(':')[0] for t, c in enc.clauses))
    ALL = True
    # (1) generic Lambda_w
    random.seed(61)
    for trial in range(0 if 'skipL' in sys.argv else 3):
        w = {p: random.randint(10 ** 6, 10 ** 9) for p in range(inst.nbase)}
        val = lambda_assignment(enc, w)
        bad = check_assignment(enc, val)
        print('(1.%d) Lambda_w, random w: violated clauses: %d %s' % (trial, len(bad), bad[:3]))
        ALL &= not bad
    # (2) unit weights
    if 'skipL' in sys.argv:
        bad1 = ['SEC']
    w1 = {p: 1 for p in range(inst.nbase)}
    if 'skipL' not in sys.argv:
        val1 = lambda_assignment(enc, w1)
        bad1 = check_assignment(enc, val1)
    kinds_bad = Counter(t.split(':')[0] for t in bad1)
    print('(2) Lambda_1 (unit masses): violated clauses by kind:', dict(kinds_bad))
    secb = [t for t in bad1 if t.startswith('SEC')]
    for t in secb[:6]:
        print('     ', t)
    ALL &= bool(secb) and set(kinds_bad) == {'SEC'}
    # (3) plain SAT
    t1 = time.time()
    st, val, tcs = solve(enc, verbose=False)
    print('(3) plain relational SAT:', st, ' TC clauses generated:', len(tcs), ' (%.0fs)' % (time.time() - t1))
    if st == 'SAT':
        bad = check_assignment(enc, val)
        print('    exact re-check of all clauses incl. full TC: violations', len(bad))
        ALL &= not bad
    with open(os.path.join(HERE, 'run61a_%s.pkl' % label), 'wb') as f:
        pickle.dump(dict(val=val, tcs=tcs), f)
    print('ALL PASS' if ALL else 'SOME FAIL', '(%.0fs)' % (time.time() - t0))
