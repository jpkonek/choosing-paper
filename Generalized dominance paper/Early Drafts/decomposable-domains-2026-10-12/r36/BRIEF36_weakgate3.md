# Brief 36: the weak gate in three worlds (20 October 2026)

This is the mechanism-design phase. Deliver short screening results: exact finite examples, counterexamples, and short proofs. Do not deliver long theorem programmes. Keep each note under about 8 pages. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions beyond those stated. Plain English.

## Read first
- `gate2d/Separation-Gated-Evaluators.tex` (and its PDF): the two-world construction, the referee's repairs, audit's two extensions (Section "Two extensions found by audit"), Proposition 9 (strong gate in three worlds) and Remark 10 (triangle condition).
- `gate2d/REFEREE_gate2d.md` (referee report).
- `DESIGN_MEMO.md` §§1, 5–8: the screens S1–S10.
- The axioms are as in the note: reflexivity; strict (G); (IB); (TC) only (no transitivity); (S): coherent selected models, each undominated, competitive on supp p, with every section {p : C_p ⪯_i X} closed; (LA); direct (C); (LF). Full four-advice domain; ranks good 0 < silent 1 < bad 2 < contradictory 3.

## The weak gate
At world i, fix a key function k_i on rank steps (g, j) with null level sets. Contradiction steps (j = 3) and unanimous-problem steps get the lowest keys. A pair (X, Y) passes the weak gate at world i if T^on_i (steps Y adds) is non-null and ess inf over T^on_i of k_i < ess inf over T^off_i of k_i. World i accepts X ⪯_i Y iff X = Y, or T^off_i is null, or [the pair passes the weak gate and Φ_i(X,Y) ≥ 0]. No cycles, for any keys and any Φ_i (PROVED in the note).

## Three worlds
- Problems g ∈ R³ modulo sign, Gaussian measure, coherent models D_K for compact convex K in the 2-simplex.
- A selection p ↦ C_p over the 2-simplex. For screening, the target may be any interior imprecise credal set (a small triangle or hexagon is fine); the ε-contamination triangle T1 is the eventual target.
- Before gating, the sticky verdicts 2·on_i − off_i are never all negative out of a regular model (note, last paragraph of the audit section). So the issue is whether a world with a nonnegative verdict also passes its gate, with closed sections, and whether KKM dominators exist.

## Facts to use or test
- **KKM.** Closed covering sections force, for every model X, an index q with C_q ⪯_i X at all three worlds. Under the weak gate this needs, for each X not a pure worsening, some q such that at every world the lowest-key change between C_q and X is an added step (a loss for that world).
- **A shared problem order fails (check this; it is the lead's sketch, not proved).** Suppose all three worlds key steps by one common order of problems. Consider a regular rival X (no contradiction, correct on unanimous problems) whose bottom change is a regular change on a mixed problem. That change is a gain at some world, so no dominator passes all three gates. Make this precise, or refute it.
