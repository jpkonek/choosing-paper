# Loss Dominance Generalized v3.1: changes from v3

25 October 2026. v3 is unchanged. v3.1 adds four things and fixes one sentence.

1. **Defending-world form of (B)** (Prop 2.2, PROVED). (B) holds iff there are:
   - one map u from the simplex to C_L, the same for every rival; and
   - for each rival m, defending worlds d_m(p) in supp p, such that the closure of each set {p : d_m(p) = ω} lies inside {p : u_p ⪯_ω m}.
   
   Only the chosen defences must survive limits. Other comparisons may jump, and refusal sets need not be open. A limit index need not itself be defended at ω, and ω may lie outside its support.
2. **The conclusion (W) as a stated objective** (§3.1, Prop 3.1, Example 3.2). (W) says every model is weakly dominated by a member of C_L.
   - (W) with (LA) and (C) gives U_L = C_L. This is a two-line deduction.
   - The permissibility argument needs weak dominators only for *incoherent* models. Example 3.2 (an infinite descending chain of coherent models) shows that (W) is strictly stronger than that. This scoping follows the auditor's remark.
3. **A second route: admissibility** (§3.5, Lemma 3.11, Prop 3.12).
   - **Lemma 3.11 (Zorn).** If the world orders are lexicographic in finitely many numbers and the set of score vectors is compact, every model is weakly dominated by an undominated model. Any number of worlds.
   - **Prop 3.12 (separation).** Two levels, finitely many worlds, convex score set, and a model scoring 0 at every leading level. Then every undominated model minimises a weighting in which second-level weights sit only at worlds whose leading level is 0.
   - With non-atomic splicing (Lyapunov's theorem), this reduces dominance to checking the minimisers. The route needs no certificates and no closed sections.
4. **Hypothesis table** extended to the new results.
5. **Fix:** the three-world example concerns "a continuum of loss profiles on finitely many worlds", not "a finite set".

## Application outside the paper (project result, refereed once)
**Theorem VB** (see `VB_dominance_note.md`). In the veto–Brier ranking on the U-domain:
- every model is weakly dominated by an undominated model;
- the undominated models are exactly the polyhedral lexicographic-Bayes minimisers, and they are coherent.

Together with L3 Thm 3.3, every incoherent model is dominated by a coherent undominated model, and T1 is undominated. **So T1 is covered on the U-domain**, under strict (G), (IB), (LA) (meaning C_L = coherent ∩ undominated), (LF) and (C). (S) fails for VB; that is no longer an obstacle.

Open, for the author:
- whether the U-domain suffices, or the full four-advice domain is required;
- the role of lexicographic rankings;
- the exact reading of (LA) in L3.
