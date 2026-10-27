"""PP76 hlib76: exact finite model of the H-class (two states per point).
Atoms g = 0..n-1, each with an odd world o[g] in {0,1,2}.  An H-model is a tuple of states in {0,1};
state 1 is better at the odd world o[g] and worse at the two other worlds (PP62 (1.1): every h <-> S
change at a point of R improves its odd world and worsens the other two, or the reverse).
A record is (support, old values, new values); (IB) = verdicts depend on the record only.
"""
import itertools

def better(o, w, x, y):
    """is state x strictly better than state y at world w, at an atom with odd world o"""
    if x == y: return False
    return (x > y) if w == o else (x < y)

def weakly_worse(O, w, Y, X):
    """Y pointwise weakly w-worse than X"""
    return all(not better(O[g], w, Y[g], X[g]) for g in range(len(O)))

def strictly_worse(O, w, Y, X):
    return weakly_worse(O, w, Y, X) and Y != X

def rec(X, Y):
    return tuple((g, X[g], Y[g]) for g in range(len(X)) if X[g] != Y[g])

def models(n):
    return list(itertools.product((0, 1), repeat=n))

def carries(C, r):
    return all(C[g] == a for g, a, b in r)

def apply(C, r):
    Z = list(C)
    for g, a, b in r: Z[g] = b
    return tuple(Z)

def coupled_refusals(O, B, X, w, allm):
    """all records refused at w by the coupled rule from the accepted domination record rec(B->X),
    over ALL common-context copies (B',X') and all Y strictly w-worse than X'."""
    n = len(O); D = [g for g in range(n) if B[g] != X[g]]; out = set()
    for Zc in allm:
        Bp = tuple(B[g] if g in D else Zc[g] for g in range(n))
        Xp = tuple(X[g] if g in D else Zc[g] for g in range(n))
        if Zc != tuple(Zc[g] for g in range(n)): pass
        for Y in allm:
            if strictly_worse(O, w, Y, Xp):
                out.add(rec(Y, Bp))
    return out
