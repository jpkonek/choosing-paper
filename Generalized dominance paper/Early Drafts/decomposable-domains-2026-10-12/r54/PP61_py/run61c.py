"""PP61 run C: the adaptive game (BRIEF54), exact.

State: sources G3 = {u, B, D}, all nine pure-shift germs, a swap family (singles for every pair, the
bal2/ovl/big families of (u,B) and (u,D)), pads; atom weights w = int q|g| over each atom.
The kink cells Ep (Maj1, u answers alone) and Em (Min1, u answers alone) carry the game: their core
slabs are split radially (atomlessness) whenever the adversary needs an exactly q-balanced piece.

Step n:
  (V1, revisable worlds)  Lambda_{w_n}: all clauses?  If not, perturb w_n generically and re-check.
                          Outcome (OK) = weights certify all source refusals AND relations hold.
  adversary              new swap X_n = C_u[P u Q' -> C_b], b alternating B, D, with P an EXISTING
                          Ep slab (overlap with earlier swaps) and Q' a NEW Em sub-slab with
                          int_{Q'} q|g| = int_P q|g|  (so X_n is q_n-balanced: Theorem Q's rival for q_n).
  (V2, frozen promises)  promises = every refusal of Lambda_{q_n} at a source record that existed before
                          X_n (the promised refusal neighbourhoods, worlds frozen).  For assignments
                          (i, j) = (refusing world of r_n, refusing world of r_n^-): exact LP (q or alpha)
                          and relational SAT with promises + the two refusals as unit clauses.
                          Classify (OK) / (W) / (R) / (W~R).
"""
import sys, os, time, random, pickle
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from collections import Counter
from fractions import Fraction as Fr
from geom61 import Geometry, G3, sig
from inst61 import Inst, Encoding, solve, check_assignment, lambda_assignment
from build61 import families
import lp61

random.seed(6161)


def kink_classes(geo):
    ep = [k for k in geo.dis if sig(geo.cls[k]) == 'Maj1' and k[1] == ('S', 'S', 'P')]
    em = [k for k in geo.dis if sig(geo.cls[k]) == 'Min1' and k[1] == ('S', 'S', 'P')]
    return geo.cname[ep[0]], geo.cname[em[0]]


class Game:
    def __init__(self):
        self.geo0 = Geometry(G3)
        self.EP, self.EM = kink_classes(self.geo0)
        self.slabs = {self.EP: ['c1', 'c2'], self.EM: ['c1', 'c2']}
        self.game_swaps = []          # (a, b, tuple of atom labels)
        self.w = None
        proto = Inst(self.geo0, [], pads=False)
        self.base_spec = []
        for (a, b) in (('B', 'u'), ('D', 'u'), ('B', 'D')):
            fam, L, V = families(proto, a, b, max_bal2=2 if 'u' in (a, b) else 0, max_bal3=0,
                                 overlaps='u' in (a, b))
            for kind, F in fam:
                labs = tuple(proto.atoms[p].label for p in F)
                for (x, y) in ((a, b), (b, a)):
                    self.base_spec.append((x, y, labs, kind))
        self.leaves = {}              # label -> list of current leaf labels

    def expand(self, lab):
        if lab not in self.leaves:
            return [lab]
        out = []
        for l in self.leaves[lab]:
            out += self.expand(l)
        return out

    def build(self):
        geo = Geometry(G3, slabs=self.slabs)
        proto = Inst(geo, [], pads=False)
        spec, kinds = [], {}
        for (x, y, labs, kind) in self.base_spec:
            F = tuple(sorted(proto.by_label[l] for lab in labs for l in self.expand(lab)))
            spec.append((x, y, F))
            kinds[(x, y, F)] = kind
        for (a, b, labs) in self.game_swaps:
            F = tuple(sorted(proto.by_label[l] for lab in labs for l in self.expand(lab)))
            for (x, y) in ((a, b), (b, a)):
                spec.append((x, y, F))
                kinds[(x, y, F)] = 'bal2'
        inst = Inst(geo, spec, pads=True, shifts=[(nm, w) for nm in geo.names for w in range(3)], kinds=kinds,
                    pad_kinds=())
        enc = Encoding(inst)
        return inst, kinds, enc

    def weights_for(self, inst):
        """inherit weights by label; unit weights at step 0."""
        if self.w is None:
            self.w = {a.label: 10 ** 6 for a in inst.atoms[:inst.nbase]}
        return {a.id: self.w[a.label] for a in inst.atoms[:inst.nbase]}

    def split(self, cls, slab, part):
        """radial split of slab cls.slab into (cls.slab+'a' with weight part, cls.slab+'b' with the rest)."""
        lab = cls + '.' + slab
        W = self.w.pop(lab)
        assert 0 < part < W
        i = self.slabs[cls].index(slab)
        self.slabs[cls][i:i + 1] = [slab + 'a', slab + 'b']
        self.w[lab + 'a'], self.w[lab + 'b'] = part, W - part
        self.leaves[lab] = [lab + 'a', lab + 'b']
        return lab + 'a'


def source_records(inst, enc):
    names, M = enc.mat['base']
    out = []
    for a, Sn in enumerate(names):
        if inst.selected[Sn]:
            for b in range(len(names)):
                if a != b:
                    out.append((Sn, names[b], M[a, b]))
    return out


def main(steps=4):
    g = Game()
    log = []
    for n in range(steps + 1):
        t0 = time.time()
        inst, kinds, enc = g.build()
        w = g.weights_for(inst)
        print('\n=== step %d: base models %d, swaps %d, atoms %d, records %d  (%.0fs)' % (
            n, len(inst.base_models), len(inst.swaps), len(inst.atoms), len(enc.recs), time.time() - t0))
        val = lambda_assignment(enc, w)
        bad = check_assignment(enc, val)
        print('  V1: Lambda_{q_n} with the inherited weights: violated clauses', dict(Counter(t.split(':')[0] for t in bad)))
        for t in [t for t in bad if t.startswith('SEC')][:3]:
            print('      ', t)
        # V2 on the newest swap (step >= 1): frozen promises = refusals of Lambda_{q_n} on pre-existing records
        if n >= 1:
            a, b, labs = g.game_swaps[-1]
            names, M = enc.mat['base']
 
            F = tuple(sorted(inst.by_label[l] for lab in labs for l in g.expand(lab)))
            xn = [nm for (nm, x, y, FF) in inst.swaps if x == a and y == b and FF == F][0]
            ia, ix = names.index('S:' + a), names.index(xn)
            r, rb = M[ia, ix], M[ix, ia]
            z = [sum(w[p] * (inst.atoms[p].phi[i][y] - inst.atoms[p].phi[i][x]) for (p, x, y) in enc.recs[r]) for i in range(3)]
            print('  adversary swap %s : u^1 q_n-value of r_n = %s (balanced: %s)' % (xn, z, z == [0, 0, 0]))
            newrecs = set()
            for (Sn, Xn, rr) in source_records(inst, enc):
                if Xn == xn or (Xn.startswith('X:') and Xn.split(':')[2] == xn.split(':')[2]):
                    newrecs.add(rr)
            promises = []
            for (Sn, Xn, rr) in source_records(inst, enc):
                if rr in newrecs or rr in (r, rb):
                    continue
                for i in range(3):
                    if not val[enc.v(rr, i)]:
                        promises.append((rr, i))
            promises = sorted(set(promises))
            print('  V2: %d frozen promised refusals' % len(promises))
            res = {}
            for (i, j) in ((0, 1), (1, 0), (0, 0), (1, 2), (1, 1)):
                reqs = [(enc.recs[rr], k) for (rr, k) in promises] + [(enc.recs[r], i), (enc.recs[rb], j)]
                st, out = lp61.test(inst, reqs)
                extra = [('PROMISE', (-enc.v(rr, k),)) for (rr, k) in promises] + \
                        [('NEW', (-enc.v(r, i),)), ('NEW', (-enc.v(rb, j),))]
                sst, sval, tcs = solve(enc, extra=extra, phases=[v if val[v] else -v for v in range(1, enc.nvars + 1)])
                if sst == 'SAT':
                    assert not check_assignment(enc, sval, extra)
                cls = {('Q', 'SAT'): '(OK)', ('ALPHA', 'SAT'): '(W~R)', ('ALPHA', 'UNSAT'): '(W)+(R)', ('Q', 'UNSAT'): '(R)'}[(st, sst)]
                cert = '' if st == 'Q' else ' alpha support %d: %s' % (len(out), [(str(a_), 'w%d' % (k + 1), 'new' if rq in (enc.recs[r], enc.recs[rb]) else 'old') for a_, (rq, k) in out][:4])
                print('    r_n refused at %d, r_n^- refused at %d : LP %s, SAT %s -> %s%s' % (i + 1, j + 1, st, sst, cls, cert))
                res[(i, j)] = (st, sst, cls)
            log.append(dict(step=n, swap=xn, z=z, V2=res))
        # V1 repair: generic perturbation of the inherited weights
        if bad:
            for attempt in range(5):
                w2 = {p: 1000 * v + random.randint(1, v) for p, v in w.items()}
                val2 = lambda_assignment(enc, w2)
                bad2 = check_assignment(enc, val2)
                if not bad2:
                    break
            rel = max(abs(w2[p] / 1000 - w[p]) / w[p] for p in w)
            print('  V1: generic perturbation (max relative change %.1e): violated clauses %d -> (OK)' % (rel, len(bad2)))
            assert not bad2
            for p, v in w2.items():
                g.w[inst.atoms[p].label] = v
            w = w2
        else:
            print('  V1: (OK) without change')
        if n == steps:
            break
        # adversary move
        P = g.EP + '.' + g.slabs[g.EP][0]
        Q = max((g.EM + '.' + s for s in g.slabs[g.EM]), key=lambda l: g.w[l])
        wp, wq = g.w[P], g.w[Q]
        if wq > wp:
            Qa = g.split(g.EM, Q.split('.')[1], wp)
            labs = (P, Qa)
        else:
            Pa = g.split(g.EP, P.split('.')[1], wq)
            labs = (Pa, Q)
        b = 'B' if n % 2 == 0 else 'D'
        g.game_swaps.append(('u', b, labs))
        print('  adversary: new q_n-balanced swap u -> %s on %s' % (b, labs))
    with open(os.path.join(HERE, 'run61c.pkl'), 'wb') as f:
        pickle.dump(log, f)


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4)
