# Round 84 summary (29 Oct 2026): commission-averse independent rankings under W

Sources: C1_report.md (construction) and C2_report.md (theory map). Neither report has been refereed. No integral payoff or Brier score is used anywhere.

## Setting
- Worlds: finitely many.
- Measure: standard Gaussian.
- Domain: every measurable model.
- Axioms in force: world-by-world guidance; independence in the arbitrary-set form; the three-model condition; transitivity through ties.
- Selection: W, with one assignment for all rivals.
- Target: one target protected per ranking.

## What was proved

**1. Independence makes dominance a property of the change** (C2 Prop 5.1; C1 Lemma 1).
- A dominating change can be applied to no undominated model.
- Under W, therefore, the assigned dominator b of an incoherent x must leave x outside [b∩T, b∪T].
- If x adds a bounded set E to T, b must leave out part of E. If x removes a bounded set from T, b must restore part of it.

**2. Complete additive rankings under W.**
- Take world scores ∫_X ψ_i, with ψ_i integrable and sign-respecting, and nothing else assumed.
- W then forces every Bayes set {p·ψ > 0} to be almost coherent.
- Consequences:
  - the contamination triangle T1, and every triangle in general position, is dominated;
  - for n ≥ 3, every target whose credal set contains three vertices is dominated, the vacuous model included.

  The exclusion of T1 goes through the refereed realisation theorem in *The Contamination Triangle*, not through Theorem gm as stated.

**3. Endorsed rankings** (C1 Thm 2). Suppose the comparisons that assigned models win are never against a sign-respecting additive field ψ (integrable, with null indifference sets).
- Then W forces every assigned model to be a ψ-Bayes set, and every ψ-Bayes set to be almost coherent.
- The protected target must also satisfy a "straddling" condition.
- **With two worlds**, that condition forces the target to be a ψ-Bayes set itself. So refusing comparisons buys nothing.
- **Audit's two-world pair.** A box-endorsed ranking protects T exactly when u₁u₂ = 9 l₁l₂. Then T is X's dominator, and it beats a whole neighbourhood of X.

**4. Intersections and lexicographic orders** (C2).
- *Intersections:* excluded for T1 whenever the target has a strictly positive supporting weight.
- *Commission-first lexicographic orders:* every undominated coherent model has a vertex in its credal set.
- *Lexicographic orders whose first layer has null indifference sets at every interior prior:* excluded for T1.

**5. Failed candidates for T1** (C1).
- *Box with refusals:* W fails numerically at a = 0.1, 0.2 and 0.3. The scores are computed exactly; only the grid search is numerical.
- *Lexicographic orders:* fail.
- *T1's rescaled family as the assignment, with maximal acceptance:* breaks the three-model condition, by an explicit three-patch counterexample.

## Open
- **R8:** the two-world straddling theorem should extend to three worlds. If it does, every endorsed ranking is excluded for T1 under W.
- **The one structural escape left for additive building blocks.** This is a first-level field whose indifference set is non-null at some interior prior, with a second criterion settling those ties. C2 and C1 identify the same gap: "blind-set" endorsers, as in the earlier D2 and VB constructions.
- **Other escapes:**
  - finitely additive or non-integrable endorsers;
  - rankings with no endorser at all, whose ordering conditions hold only because the relevant compositions cannot be realised.
- **The vacuous model.** The 11 Oct theorem does not survive under W. For general complete rankings that are not integral, the question is open.

## Reachable now
Under endorsement and W:
- **Two worlds:** every interior interval, via boxes.
- **Three worlds:** rescaled boxes and the near-triangle polygons, assuming R8.

## Decision needed from the author
Are blind-set (lexicographic, non-null-tie first layer) rankings acceptable in principle? They keep strict world-by-world guidance if the second layer is strictly guided. But some gambles are then ignored at the first level at some priors.
