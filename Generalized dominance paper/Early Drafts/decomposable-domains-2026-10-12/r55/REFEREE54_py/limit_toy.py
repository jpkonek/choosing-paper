"""REFEREE54 section 4: an abstract decreasing chain whose stages all satisfy the axioms checked here
(reflexivity, (TC), defence and undominatedness and direct (C) of the selected member T, existential (C):
every incoherent model is dominated, and GLOBAL direct (C): every all-world weak dominator of a coherent
undominated model is coherent) while the limit (intersection) fails global direct (C).

Selection: partial, one assigned index (T at u), as in a BRIEF55 partial system.  Models are abstract
(records = ordered pairs, so (IB) is vacuous and no guidance pair exists).
Models: T, N, D, D2 coherent; X, Y_0..Y_K incoherent.
Stage n (n = 0..K) accepts, besides reflexivity:
  T <=_1 Z for every Z;   X <=_w N and N <=_w X (all w);   D <=_w X (all w);   D2 <=_w Y_j (all w, all j);
  Y_j <=_2 N, Y_j <=_3 N (all j);   Y_j <=_1 N  iff  j >= n.
Everything else is refused.  The limit is n = infinity (no Y_j <=_1 N).
Stage relations restricted to any finite set of models are those of the truncation, so checking stages
n = 0..K-1 with Y_0..Y_K present checks every stage of the infinite chain on those models.
"""
import itertools

K = 6
MODELS = ['T', 'N', 'D', 'D2', 'X'] + ['Y%d' % j for j in range(K + 1)]
COH = {'T', 'N', 'D', 'D2'}
SEL = {'T'}
W = (1, 2, 3)


def rel(n):
    acc = set()
    for z in MODELS:
        for w in W:
            acc.add((z, z, w))
        acc.add(('T', z, 1))
    for w in W:
        acc |= {('X', 'N', w), ('N', 'X', w), ('D', 'X', w)}
        for j in range(K + 1):
            acc.add(('D2', 'Y%d' % j, w))
            if w in (2, 3) or (n is not None and j >= n):
                acc.add(('Y%d' % j, 'N', w))
    return acc


def le(acc, a, b, w):
    return (a, b, w) in acc


def dominated(acc, m):
    for y in MODELS:
        if y == m:
            continue
        if all(le(acc, y, m, w) for w in W) and any(not le(acc, m, y, w) for w in W):
            return y
    return None


def check(acc):
    out = {}
    out['TC'] = all(not (le(acc, a, b, w) and le(acc, b, c, w) and le(acc, c, a, w))
                    or (le(acc, b, a, w) and le(acc, c, b, w) and le(acc, a, c, w))
                    for a, b, c in itertools.product(MODELS, repeat=3) for w in W)
    out['defence(T)'] = all(any(le(acc, 'T', z, w) for w in W) for z in MODELS)
    out['T undominated'] = dominated(acc, 'T') is None
    out['direct (C) for T'] = all(any(not le(acc, z, 'T', w) for w in W) for z in MODELS if z not in COH)
    out['existential (C)'] = all(dominated(acc, z) is not None for z in MODELS if z not in COH)
    und = [m for m in MODELS if m in COH and dominated(acc, m) is None]
    out['global direct (C)'] = all(z in COH for m in und for z in MODELS if all(le(acc, z, m, w) for w in W))
    # Rule IV of AUDIT_completion with P = coherent undominated models: tie partners of P are in P
    out['rule IV'] = all(z in und for m in und for z in MODELS
                         if all(le(acc, z, m, w) and le(acc, m, z, w) for w in W))
    return out, und


prev = None
allstages = True
for n in list(range(K)) + [None]:
    acc = rel(n)
    if prev is not None:
        assert acc <= prev, 'chain not decreasing'
    prev = acc
    res, und = check(acc)
    tag = 'stage %d' % n if n is not None else 'LIMIT  '
    print('%s: %s; coherent undominated: %s; N dominated by %s' % (tag, res, und, dominated(acc, 'N')))
    if n is not None:
        allstages &= all(res.values())
    else:
        lim = res
print('every stage passes every listed clause (incl. rule IV):', allstages)
print('limit: global direct (C) =', lim['global direct (C)'], '; existential (C) =', lim['existential (C)'],
      '; TC =', lim['TC'])
