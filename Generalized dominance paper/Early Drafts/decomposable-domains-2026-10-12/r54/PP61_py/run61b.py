"""PP61 run B: allocations beyond common reweighting, on the exact instance of run A.

E1  plain relational SAT solution: its source refusals -> LP; q or an exact alpha-certificate.
E2  forced single-world incomparability of every balanced (bal2) swap record r and its inverse r^-:
      OR_i ( r refused at i  AND  r^- refused at i ).        alpha = (1,1) for each such swap.
E3  forced non-straddling refusals (REFEREE_round53 6.1 table): r refused only inside {2,3} and r^-
    refused only inside {2,3} (no refusal at world 1 for either), on every Maj1/Min1 bal2 swap.
E4  mass-free hypothesis (MF-sig): records with the same set of (sign type, old, new) share verdicts.
E4' mass-free hypothesis (MF-class): records with the same set of (cell class, side, old, new) share verdicts.
For SAT outcomes the allocation is re-checked exactly (all clauses + full TC on every ordered triple)
and its source refusals go to the exact LP.  For UNSAT outcomes a minimal core is extracted.
"""
import sys, os, time, pickle
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from collections import Counter, defaultdict
import numpy as np
from geom61 import G3, G5, sig
from inst61 import Encoding, solve, check_assignment, VI
from run61a import build
import lp61


def get(label):
    fn = os.path.join(HERE, 'enc61_%s.pkl' % label)
    if os.path.exists(fn):
        with open(fn, 'rb') as f:
            return pickle.load(f)
    G = {'G3': G3, 'G5': G5}[label]
    kw = dict(max_bal2=4, max_bal3=2) if label == 'G3' else dict(max_bal2=2, max_bal3=1)
    inst, kinds = build(G, **kw)
    enc = Encoding(inst)
    with open(fn, 'wb') as f:
        pickle.dump((inst, kinds, enc), f)
    return inst, kinds, enc


def source_refusals(inst, enc, val):
    names, M = enc.mat['base']
    reqs = []
    for a, Sn in enumerate(names):
        if not inst.selected[Sn]:
            continue
        for b in range(len(names)):
            if a == b:
                continue
            r = M[a, b]
            for i in range(3):
                if not val[enc.v(r, i)]:
                    reqs.append((enc.recs[r], i, Sn, names[b]))
    return reqs


def lp_report(inst, reqs, tag):
    st, out = lp61.test(inst, [(r, i) for (r, i, S, X) in reqs])
    if st == 'Q':
        print('   [%s] LP: a common q certifies all %d source refusals (exact)' % (tag, len(reqs)))
    else:
        print('   [%s] LP: NO common q; exact alpha-certificate with support %d:' % (tag, len(out)))
        lab = {(r, i): (S, X) for (r, i, S, X) in reqs}
        for a, (r, i) in out:
            S, X = lab[(r, i)]
            print('        alpha=%s  : %s refuses %s at world %d' % (a, S, X, i + 1))
    return st, out


def bal_swaps(inst, kinds, only_kink=False):
    out = []
    for (n, a, b, F) in inst.swaps:
        if kinds.get((a, b, F)) != 'bal2':
            continue
        if only_kink:
            sg = sorted(sig(inst.atoms[p].ray) for p in F)
            if sg != ['Maj1', 'Min1']:
                continue
        out.append((n, a, b, F))
    return out


def rec_pair(inst, enc, n, a):
    names, M = enc.mat['base']
    ia, ix = names.index('S:' + a), names.index(n)
    return M[ia, ix], M[ix, ia]


def allocation_pattern(inst, kinds, enc, val, swaps):
    pat = Counter()
    for (n, a, b, F) in swaps:
        r, rb = rec_pair(inst, enc, n, a)
        Rr = ''.join(str(i + 1) for i in range(3) if not val[enc.v(r, i)])
        Rb = ''.join(str(i + 1) for i in range(3) if not val[enc.v(rb, i)])
        sg = '+'.join(sorted(sig(inst.atoms[p].ray) for p in F))
        pat[(sg, 'R(r)={%s}' % Rr, 'R(r-)={%s}' % Rb)] += 1
    return pat


def minimal_core(enc, extra, tcs, budget=400):
    """deletion-based minimal unsatisfiable subset over (enc.clauses + extra + tcs), via selectors."""
    from pysat.solvers import Solver
    allc = list(enc.clauses) + list(extra) + list(tcs)
    top = enc.nvars + 10 ** 6
    sel = list(range(top + 1, top + 1 + len(allc)))
    S = Solver(name='cadical153')
    for s_, (tag, c) in zip(sel, allc):
        S.add_clause(list(c) + [-s_])
    assert not S.solve(assumptions=sel)
    core = set(S.get_core())
    core = [s_ for s_ in sel if s_ in core]
    i = 0
    calls = 0
    while i < len(core) and calls < budget:
        trial = core[:i] + core[i + 1:]
        calls += 1
        if not S.solve(assumptions=trial):
            c2 = set(S.get_core())
            core = [s_ for s_ in trial if s_ in c2]
        else:
            i += 1
    S.delete()
    return [allc[s_ - top - 1] for s_ in core], calls < budget


def describe_lit(enc, inst, l):
    r, i = divmod(abs(l) - 1, 3)
    rec = enc.recs[r]
    body = ','.join('%s:%s>%s' % (inst.atoms[p].label, 'PMSC'[x], 'PMSC'[y]) for (p, x, y) in rec)
    return '%s[%s @w%d]' % ('' if l > 0 else 'NOT ', body, i + 1)


LOCAL = {}


def local_units(inst, enc, lv, models):
    """unit clauses fixing every record NOT touching `models` (names of base swaps) to Lambda_w's verdict.
    Sound for SAT answers (a SAT solution is re-checked on all clauses); an UNSAT answer is then only
    'no solution agreeing with Lambda_w off the pattern' and is reported as such."""
    rel = set(models)
    free = set()
    for label, (names, M) in enc.mat.items():
        idx = [k for k, n in enumerate(names) if n in rel or any(n.endswith('|' + m) for m in rel)
               or any(n.startswith('PAD:' + m + ':') for m in rel)]
        for k in idx:
            free.update(M[k, :].tolist())
            free.update(M[:, k].tolist())
    units = []
    for r in range(len(enc.recs)):
        if r in free:
            continue
        for i in range(3):
            v = enc.v(r, i)
            units.append(('LOCAL', (v if lv[v] else -v,)))
    return units, len(free)


def run_pattern(inst, kinds, enc, extra, tag, seed_tc=(), phases=None):
    """Relational SAT for a pattern.  In local-repair mode, records not touching the pattern are first
    fixed to Lambda_w; whenever an UNSAT core contains such a fixing unit, those records are released
    and the problem is re-solved (core-guided relaxation).  The final answer is therefore exact:
    SAT (re-checked on every clause) or UNSAT with a core free of fixing units (a genuine core)."""
    t = time.time()
    units = []
    if tag.split()[0] in LOCAL:
        units, nf = LOCAL[tag.split()[0]]
        print('   [local repair start: %d free records; others fixed to Lambda_w, released on demand]' % nf)
    tcs_all = list(seed_tc)
    released = 0
    for it in range(400):
        ex = list(extra) + units
        st, val, tcs = solve(enc, extra=ex, seed_tc=tcs_all, phases=phases, verbose=False,
                             solver_name=os.environ.get('PP61_SOLVER', 'cadical153'))
        tcs_all = tcs
        if st != 'UNSAT':
            break
        core, minimal = minimal_core(enc, ex, tcs_all)
        loc = set(c for tg, c in core if tg == 'LOCAL')
        if not loc:
            break
        # release every record whose fixing unit occurs in the core
        rel = set((abs(c[0]) - 1) // 3 for c in loc)
        before = len(units)
        units = [u for u in units if (abs(u[1][0]) - 1) // 3 not in rel]
        released += len(rel)
    print('[%s] relational SAT: %s  (TC clauses %d, released %d records, %.0fs)' % (tag, st, len(tcs_all), released, time.time() - t))
    if st == 'SAT':
        bad = check_assignment(enc, val, extra)
        print('   exact re-check (all clauses, pattern clauses, full TC on all ordered triples): violations %d' % len(bad))
        return st, val, tcs_all, bad
    if st == 'UNSAT':
        print('   minimal unsatisfiable core (%s): %d clauses, none of them a fixing unit' % ('minimal' if minimal else 'reduced', len(core)))
        for tg, c in core:
            print('     %-50s %s' % (tg[:50], ' OR '.join(describe_lit(enc, inst, l) for l in c)[:500]))
        return st, core, tcs_all, None
    return st, None, tcs_all, None


if __name__ == '__main__':
    label = sys.argv[1] if len(sys.argv) > 1 else 'G3'
    which = sys.argv[2] if len(sys.argv) > 2 else 'E1,E2,E3,E4,E4c'
    inst, kinds, enc = get(label)
    print('[%s] records %d, clauses %d' % (label, len(enc.recs), len(enc.clauses)))
    seed = ()
    pa = os.path.join(HERE, 'run61a_%s.pkl' % label)
    if os.path.exists(pa):
        with open(pa, 'rb') as f:
            seed = pickle.load(f)['tcs']
    nxt = [enc.nvars + 1]

    def aux():
        nxt[0] += 1
        return nxt[0] - 1

    import random
    from inst61 import lambda_assignment
    random.seed(7)
    wgen = {p: random.randint(10 ** 6, 10 ** 9) for p in range(inst.nbase)}
    lv = lambda_assignment(enc, wgen)
    phases = [v if lv[v] else -v for v in range(1, enc.nvars + 1)]
    print('phase seed: Lambda_w for a generic w (an additive allocation); patterns force departures from it')
    swaps = bal_swaps(inst, kinds)
    kink = bal_swaps(inst, kinds, only_kink=True)
    print('balanced (bal2) swaps:', len(swaps), ' of kink type Maj1+Min1:', len(kink))
    if 'E1' in which:
        st, val, tcs, bad = run_pattern(inst, kinds, enc, [], 'E1 plain', seed, phases)
        if st == 'SAT':
            lp_report(inst, source_refusals(inst, enc, val), 'E1')
            for k, c in sorted(allocation_pattern(inst, kinds, enc, val, swaps).items()):
                print('     pattern', k, 'x', c)
    if 'E2' in which:
        extra = []
        for (n, a, b, F) in swaps:
            r, rb = rec_pair(inst, enc, n, a)
            ys = [aux() for i in range(3)]
            extra.append(('E2:%s' % n, tuple(ys)))
            for i in range(3):
                extra.append(('E2:%s' % n, (-ys[i], -enc.v(r, i))))
                extra.append(('E2:%s' % n, (-ys[i], -enc.v(rb, i))))
        st, val, tcs, bad = run_pattern(inst, kinds, enc, extra, 'E2 incomparability on every bal2 swap', seed, phases)
        if st == 'SAT':
            lp_report(inst, source_refusals(inst, enc, val), 'E2')
            for k, c in sorted(allocation_pattern(inst, kinds, enc, val, swaps).items()):
                print('     pattern', k, 'x', c)
            with open(os.path.join(HERE, 'E2_%s.pkl' % label), 'wb') as f:
                pickle.dump(val, f)
    if 'E3' in which:
        extra = []
        for (n, a, b, F) in kink:
            r, rb = rec_pair(inst, enc, n, a)
            extra.append(('E3:%s' % n, (enc.v(r, 0),)))       # r accepted at world 1
            extra.append(('E3:%s' % n, (enc.v(rb, 0),)))      # r^- accepted at world 1
        if os.environ.get('PP61_LOCAL'):
            ms = [n for (n, a, b, F) in kink] + [m for (n, a, b, F) in kink for (m, x, y, FF) in inst.swaps if x == b and y == a and FF == F]
            LOCAL['E3'] = local_units(inst, enc, lv, ms)
        st, val, tcs, bad = run_pattern(inst, kinds, enc, extra, 'E3 non-straddling on kink-type bal2', seed, phases)
        if st == 'SAT':
            lp_report(inst, source_refusals(inst, enc, val), 'E3')
            for k, c in sorted(allocation_pattern(inst, kinds, enc, val, kink).items()):
                print('     pattern', k, 'x', c)
    if 'E5' in which:
        # overlapping kink swaps u -> B with inconsistent mass orientations (no inverse pair involved)
        geo = inst.geo
        # B answers, u (and D) silent: u -> B is S -> h, increments (2,-1,-1) on EP (Maj1), (-2,1,1) on EM (Min1)
        EP = [geo.cname[k] for k in geo.dis if sig(geo.cls[k]) == 'Maj1' and k[1] == ('P', 'S', 'S')][0]
        EM = [geo.cname[k] for k in geo.dis if sig(geo.cls[k]) == 'Min1' and k[1] == ('P', 'S', 'S')][0]
        def swp(labs):
            F = tuple(sorted(inst.by_label[l] for l in labs))
            n = [m for (m, x, y, FF) in inst.swaps if x == 'u' and y == 'B' and FF == F][0]
            return n
        cases = {
            # refused at 1 <=> Q(EM part) > Q(EP part);  refused at {2,3} <=> Q(EP part) > Q(EM part)
            'E5a': [((EP + '.c1', EM + '.c1', EM + '.c2'), (1, 2)), ((EP + '.c1', EM + '.c2'), (0,))],
            'E5b': [((EP + '.c1', EM + '.c1'), (1, 2)), ((EP + '.c1', EP + '.c2', EM + '.c1'), (0,))],
        }
        for tg, req in cases.items():
            extra = []
            for labs, i in req:
                n = swp(labs)
                r, rb = rec_pair(inst, enc, n, 'u')
                # forward record refused at i ONLY (accepted at the other worlds), reverse unconstrained
                for k in range(3):
                    extra.append(('%s:%s' % (tg, n), (-enc.v(r, k),) if k in i else (enc.v(r, k),)))
                print('   %s requirement: R(rec(C_u -> %s)) = %s exactly' % (tg, n, [k + 1 for k in i]))
            if os.environ.get('PP61_LOCAL'):
                ms = []
                for labs, i in req:
                    n = swp(labs)
                    ms.append(n)
                    F = tuple(sorted(inst.by_label[l] for l in labs))
                    ms += [m for (m, x, y, FF) in inst.swaps if x == 'B' and y == 'u' and FF == F]
                LOCAL[tg] = local_units(inst, enc, lv, ms)
            st, val, tcs, bad = run_pattern(inst, kinds, enc, extra, tg + ' overlapping orientations', seed, phases)
            reqs = []
            for labs, i in req:
                n = swp(labs)
                r, rb = rec_pair(inst, enc, n, 'u')
                for k in i:
                    reqs.append((enc.recs[r], k, 'S:u', n))
            lp_report(inst, reqs, tg + ' (the two prescribed refusals alone)')
            if st == 'SAT':
                lp_report(inst, source_refusals(inst, enc, val), tg + ' (whole allocation)')
    if 'E6' in which:
        # uniform rule candidate: EVERY swap record that is mixed at world 3, and its inverse, refused at world 3
        names, M = enc.mat['base']
        extra = []
        cnt = 0
        for (n, a, b, F) in inst.swaps:
            r, rb = rec_pair(inst, enc, n, a)
            if inst.guidance(enc.recs[r], 2) == 0:
                extra.append(('E6:%s' % n, (-enc.v(r, 2),)))
                extra.append(('E6:%s' % n, (-enc.v(rb, 2),)))
                cnt += 1
        print('[E6] swaps mixed at world 3 (both directions forced refused at 3):', cnt, 'of', len(inst.swaps))
        st, val, tcs, bad = run_pattern(inst, kinds, enc, extra, 'E6 uniform incomparability at world 3', seed, phases)
        if st == 'SAT':
            lp_report(inst, source_refusals(inst, enc, val), 'E6')
            for k, c in sorted(allocation_pattern(inst, kinds, enc, val, swaps).items()):
                print('     pattern', k, 'x', c)
            with open(os.path.join(HERE, 'E6_%s.pkl' % label), 'wb') as f:
                pickle.dump(val, f)
    for mode, tg in (('sig', 'E4'), ('class', 'E4c')):
        if tg not in which.split(','):
            continue
        groups = defaultdict(list)
        for rid, rec in enumerate(enc.recs):
            if rec:
                groups[inst.rtype(rec, mode)].append(rid)
        extra = []
        for ty, rs in groups.items():
            for r1, r2 in zip(rs, rs[1:]):
                for i in range(3):
                    extra.append(('MF-%s' % mode, (-enc.v(r1, i), enc.v(r2, i))))
                    extra.append(('MF-%s' % mode, (enc.v(r1, i), -enc.v(r2, i))))
        print('[%s] mass-free hypothesis (%s): %d record types for %d records' % (tg, mode, len(groups), len(enc.recs)))
        st, res, tcs, bad = run_pattern(inst, kinds, enc, extra, '%s mass-free (%s)' % (tg, mode), seed, phases)
        if st == 'SAT':
            lp_report(inst, source_refusals(inst, enc, res), tg)
            for k, c in sorted(allocation_pattern(inst, kinds, enc, res, swaps).items()):
                print('     pattern', k, 'x', c)
