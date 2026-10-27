"""cycle68d: minimal core of H2 + H3 (cycle68c)."""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cycle68c.py')).read()
exec(src.split("for name, h in")[0])
core = H2 + H3
i = 0
while i < len(core):
    t = core[:i] + core[i + 1:]
    if not I.sat(t):
        core = t
    else:
        i += 1
inv = {v: k for k, v in I.var.items()}
for l in core:
    r, w = inv[l]
    print('accept at w=%d: %s' % (w, ' '.join('%s:%s->%s' % x for x in r)))
