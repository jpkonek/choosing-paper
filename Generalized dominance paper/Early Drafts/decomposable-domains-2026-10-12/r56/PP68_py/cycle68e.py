"""cycle68e: explain the core of cycle68d by forced literals."""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cycle68c.py')).read()
exec(src.split("for name, h in")[0])
Zf = fill(N, ['P1', 'P2', 't3']); Yf = fill(Y, ['P1', 'P2', 't3']); Xf = fill(T, ['P1', 'P2'])
b = [I.lit(Y, Zf, 1), I.lit(Y, Zf, 2)]
nm = {T: 'T', N: 'N*', Y: 'Y', Zf: 'Zfull', Yf: 'Yfull', Xf: 'Xfull'}
print('under Y <=_{1,2} Zfull:')
for a in nm:
    for c in nm:
        if a != c:
            f = [I.forced(a, c, w, b) for w in W]
            if any(x in 'AR' for x in f):
                print('   %-6s <=_w %-6s %s' % (nm[a], nm[c], f))
print('T <=_1 Yfull with b:', I.sat(b + [I.lit(T, Yf, 1)]), '; T <=_2 Yfull with b:', I.sat(b + [I.lit(T, Yf, 2)]))
print('both:', I.sat(b + [I.lit(T, Yf, 1), I.lit(T, Yf, 2)]))
