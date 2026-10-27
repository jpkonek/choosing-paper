"""REFEREE54: how far is PP61's V0 model (Cor E.2 configuration) from R0 with w0 = 3?
R0 is evaluated with PP61's own mass convention (F-halves unit mass, layer atoms equal infinitesimal mass);
records touching an atom of unspecified mass are skipped.  Counts (record, world) verdicts that differ."""
import os, pickle
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
for tag in ('V0', 'V1', 'test_R0e3'):
    D = pickle.load(open(os.path.join(HERE, ('corE2_%s.pkl' % tag if not tag.startswith('test') else 'corE2%s.pkl' % tag)), 'rb'))
    recs, val, PHI, W = D['recs'], D['val'], D['PHI'], D['W']
    diff, tot = Counter(), 0
    for r, rec in enumerate(recs):
        if not rec or any(W[p][0] is None for (p, x, y) in rec):
            continue
        V = [(sum(W[p][0] * (PHI[p][i][y] - PHI[p][i][x]) for (p, x, y) in rec),
              sum(W[p][1] * (PHI[p][i][y] - PHI[p][i][x]) for (p, x, y) in rec)) for i in range(3)]
        null = all(v == (0, 0) for v in V)
        for i in range(3):
            r0acc = (i != 2) if null else (V[i] >= (0, 0))
            acc = bool(val[3 * r + i + 1])
            tot += 1
            if acc != r0acc:
                diff[('acc' if acc else 'ref') + '-vs-R0-' + ('acc' if r0acc else 'ref') + ('-null' if null else '')] += 1
    print(tag, ': (record, world) verdicts compared', tot, '; departures from R0(w0=3):', dict(diff))
