"""S1 / patterns.py  --  exhaustive check of the case analysis in Lemma S1.2 (crossing agreement).

Two crossing members C, C' of C_L with world-1 error sets m u B and m u A.
For a subset a of A and b of B, the splice X = m u a u (B \ b) and the splice Y = m u (A \ a) u b satisfy
(cancellation, E_2 = M \ E_1 on M):
    C  <=_1 X  iff  b <=_1 a        X <=_1 C  iff  a <=_1 b
    C  <=_2 X  iff  a <=_2 b        X <=_2 C  iff  b <=_2 a
    C' <=_1 Y  iff  a <=_1 b        Y <=_1 C' iff  b <=_1 a
    C' <=_2 Y  iff  b <=_2 a        Y <=_2 C' iff  a <=_2 b
Here 'a <=_i b' means: world i ranks the error set a no worse than b.

Constraints used:
  (K_C)  competitiveness of C  against X:  (b <=_1 a) or (a <=_2 b)
  (K_C') competitiveness of C' against Y:  (a <=_1 b) or (b <=_2 a)
  (U_C)  X does not dominate C
  (U_C') Y does not dominate C'
A relation between a and b at one world is one of '<' (a strictly better), '>' (b strictly better),
'~' (tie), '|' (incomparable).
Expected output: the admissible patterns are exactly (<,<), (>,>), (~,~), (~,|), (|,~).
Run: python3 -I patterns.py
"""
import itertools

RELS = ['<', '>', '~', '|']

def le(rel):      # a <= b
    return rel in ('<', '~')

def ge(rel):      # b <= a
    return rel in ('>', '~')

def lt(rel):      # a < b strictly
    return rel == '<'

def gt(rel):      # b < a strictly
    return rel == '>'

def admissible(r1, r2):
    K_C = ge(r1) or le(r2)
    K_Cp = le(r1) or ge(r2)
    # X dominates C: X <=_1 C (a<=_1 b) and X <=_2 C (b<=_2 a), one strict (a<_1 b or b<_2 a)
    X_dom = le(r1) and ge(r2) and (lt(r1) or gt(r2))
    # Y dominates C': Y <=_1 C' (b<=_1 a) and Y <=_2 C' (a<=_2 b), one strict
    Y_dom = ge(r1) and le(r2) and (gt(r1) or lt(r2))
    return K_C and K_Cp and not X_dom and not Y_dom

ok = [(r1, r2) for r1, r2 in itertools.product(RELS, RELS) if admissible(r1, r2)]
print("admissible (world1, world2) patterns:", ok)
assert set(ok) == {('<', '<'), ('>', '>'), ('~', '~'), ('~', '|'), ('|', '~')}

# Edge version: only competitiveness (no two-world undominatedness).
ok_edge = [(r1, r2) for r1, r2 in itertools.product(RELS, RELS)
           if (ge(r1) or le(r2)) and (le(r1) or ge(r2))]
print("edge version (competitiveness only):", ok_edge)
print("excluded on edges:", sorted(set(itertools.product(RELS, RELS)) - set(ok_edge)))
