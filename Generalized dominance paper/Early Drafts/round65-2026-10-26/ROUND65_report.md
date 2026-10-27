# Round 65 report: (H) is proved; universal coverage by comparison deletion; (Add) assessed; covering paper completed

26 October 2026. Six agents: WT65 (auditor's tools), H65 (prover), X65 (adversary), AD65 ((Add) assessment), W65 (paper) and UN65 (note). Five referees: REF65_hA and REF65_hB (two independent refereeings of (H)), REF65_ad, and REF65_paper. Labels: PROVED (refereed once, unless stated) / CHECKED / CONJECTURE / NUMERICS. Notes are in this folder.

## 1. Headline: (H) is true (PROVED, refereed twice)

**Theorem H (X65 Thm H.1, refereed CORRECT by both REF65_hA and REF65_hB).**
- *Setting:*
  - n ≥ 1 worlds;
  - μ finite, absolutely continuous with respect to Lebesgue measure, with finite first moment;
  - K′ ⊆ Δ nonempty, compact and convex; U = D_{K′}.
- *Statement:* every incoherent measurable X ⊆ U has a coherent N with m(N) − m(X) ∈ int ℝⁿ₊ (strict in every coordinate) and μ((N∖X) ∩ hull(X∖N)) > 0.
- *Not needed:* pointedness, any condition on dim K′, K′ ⊆ relint Δ, X ⊇ int ℝⁿ₊, a continuous density.

**Proof (four steps).**
1. **Dominate from inside the hull.** Let G = hull(X) and P(h) = min_{q∈Q_X} q·h. Some Bayes act of G, N₀ = G ∩ {π·h > 0}, strictly dominates X in every coordinate.
   - This is ES64 Lemma 5.1 relativised to G; the idea is H65's.
   - REF65_hA gives a shorter minimax proof with no case split. It also turns finding π into a convex minimisation.
   - Every Bayes act of G is coherent, so an incoherent X is never one.
2. **Something is added.** N₀∖X is non-null, because k·h > 0 on U for k ∈ K′.
3. **Shrink uniformly.** N_τ := N₀ ∩ D_{(1−τ)Q_X + τΔ}. It is coherent, and its moment tends to m(N₀) as τ → 0, so the strict margin survives.
4. **Witness.**
   - Let a be a density point of N_τ∖X, and write a − (P(a) − δ)𝟙 = Σλ_j x_j + p′, with x_j ∈ X and p′ ≫ 0.
   - Superadditivity of P gives Σλ_j P(x_j) < δ.
   - Retained points satisfy q·x ≥ −((1−τ)/τ)P(x); removed points have q·x ≥ 0 ≥ that bound.
   - So every q ∈ Q_{X∖N_τ} has q·a ≥ P(a) − δ/τ > P(a)/2. A ball around a lies in hull(X∖N_τ).

**Strengthening (REF65_hA, Lemma S).** For every τ ∈ (0,1), hull(X∖N_τ) = hull(X). So the whole added part lies in the hull of the removed part. The proof is a contraction argument: if q ∈ Δ and q·x ≥ −c·P(x) a.e. on X, then q ∈ Q_X.

**Second proof (H65 Theorem H, refereed CORRECT by REF65_hB).**
- The defender is a hull Bayes act with at most 2n thin cuts.
- The Generation Lemma: every point of the defender is a combination of support points of X outside it, plus a positive vector.
- It uses K′ ⊆ relint Δ in its lineality step. X65's proof is shorter and recommended for publication.

**Corollary (H65 Cor H.1).** Defenders that beat X strictly in every coordinate always exist, and they form an open set. This answers WT65's open question.

**Why earlier searches failed (X65, CHECKED).** On the spike rival, 90 of 104 Bayes-act-of-U dominators fail to witness. That shape requires a defender sticking out of hull(X). Defenders inside the hull are certified. The failures came from one optional restriction: starting from Bayes acts of U.

**Adversarial checks (CHECKED exactly).** These illustrate the theorem; they are not part of its proof.
- REF65_hA: 25 rivals, including spikes, a deep hole with hull all of U, the boundary case, two non-pointed hulls and a comb.
- REF65_hB: 7 named and 36 random rivals.
- REF65_hB: 3,801 cases of Steps 4–5, with no failures. The bound P(a)/2 is essentially sharp (worst ratio 0.5016).
- Without the shrink, 1,554 of 3,288 cases fail. So the shrink is essential.

## 2. Universal coverage by comparison deletion (PROVED)

**Main theorem** (from Theorem H, ES64 Thm 3.2 / Cor 3.5, and REF64_es §2.5, all refereed). Fix U = D_{K′}. Comparison-deleted Brier Δ(all coherent models in U):
- satisfies reflexivity, a.e.-ties, strict (G), (IB), (TC) and finite-chain consistency;
- has as undominated models exactly the coherent models in U;
- makes every incoherent model dominated by a coherent undominated model; direct (C) and (W) hold;
- covers, in the binding sense including (LF), **exactly the full-dimensional K with K′ ⊆ relint K**. This needs Lemma LF(a)–(b) and Prop lowdim of the covering paper. X65's and ES64's "every K with K′ ⊆ relint K" omitted "full-dimensional".

Consequently:
- **Every full-dimensional credal set is covered on some domain,** for example with K′ a single point of relint K. This includes the reversed triangle, all interior pari-mutuel models, and every full-dimensional target on the earlier open lists.
- **Lower-dimensional targets are not covered by this result.** They need two-sided domains, where Step 2 fails. This is OPEN.

**Scope and limits (auditor's points, now settled facts).**
- "Universal" means one ranking per domain U, not one ranking for every target.
- The ranking is defined using coherence. It shows that coherence is representable through dominance under the agreed axioms. It does not give an independent accuracy-based justification of coherence.
- The ranking is not transitive and violates (Add). Each world's relation is a sub-relation of the Brier order.
- The axiom-level impossibility for the reversed triangle is refuted: the triangle is covered under the agreed framework.

**Write-up.** `Universal coverage by comparison deletion (draft).tex/.pdf` (UN65): 14 pages, self-contained, compiles cleanly. It contains the framework; the domain lemma; the deletion lemma; the reduction theorem; Theorem H with the minimax and contraction proofs; the main theorem with a definition of universal cover; and the lexicographic (Add)-satisfying variant LD as Proposition 7.2. Refereed by REF65_un: no mathematical error; all nine required presentation changes made.

## 3. The auditor's tools (WT65; used by H65 and X65)

**Density-point witness: CORRECT in both directions.**
- Sharper form: hull(B) = cone(B_d) + int ℝⁿ₊, with no closure needed.
- Under one-sidedness, n − 1 removed density points suffice (two in three worlds). This is sharp.
- ES64 Lemma 5.3's section-form test is valid only when Σb_j > 0.

**Compactness: CORRECT on 𝒦(K′).**
- The hull-overlap functional is lower semicontinuous, so witnessing is open in the defender.
- It is not upper semicontinuous: there are exact counterexamples in two and three worlds.

## 4. (Add) as a separate question (AD65; REF65_ad)

**Logical relations (PROVED; examples re-verified on the continuum by the referee).**
- Under (IB), transitivity = (Add) + cancellation.
- For complete relations, (TC) implies (Add).
- (Add) is independent of (IB), (TC), finite-chain consistency and (TP), jointly. REF65_ad supplied the two missing witnesses and repaired examples A and E for the continuum.

**Strengthened-framework branch (PROVED).**
- Pure guidance is transitive and protects every coherent model. So free protection comes from dropping completeness, not from dropping (Add).
- An (Add)-closed deletion relation R_lex(𝒩) satisfies all agreed axioms, (Add) and finite-chain consistency. It has the undominated set exactly 𝒩 iff (★).
- With Theorem H, **the universal cover therefore also exists under (G) + (IB) + (TC) + (Add).** This follows directly: REF65_ad refereed "R_lex(all coherent) is a universal cover iff (H)" as CORRECT, and (H) is now proved.
- The (Add)-closures of M1 and 𝒯 keep their conclusions. So (Add) excludes the round-64 relations, but none of what they were used to show.

**Corrections (REF65_ad).**
- "(G)+(IB)+(TC)+(Add) admits a universal cover iff (H)" was proved only in the "if" direction.
- The claim "incomparability under (Add) must be content-based and scale-free" is false. A Brier-threshold relation is transitive, satisfies (Add), and leaves small improvements unranked.
- Several normative sentences are assessments, not theorems.

**Side result (PROVED).** Call a ranking Brier-compatible when X ⪯_i Y implies m_i(X) ≥ m_i(Y). In any such ranking that leaves a non-Bayes model undominated, some world refuses arbitrarily small changes that improve Brier at every world.

**Assessment.** (Add) is a reasonable optional strengthening, but neither accuracy nor the agreed axioms imply it. Adopting it does not change the coverage answer.

## 5. Covering paper (W65; REF65_paper)

`Covering coherent sets of desirable gambles (draft).tex/.pdf`: 57 pages, compiles cleanly.

**Exclusions.** Five of the six exclusions recorded without proof are now proved in the paper:
- convex error levels (Thm 8.14, now for every n ≥ 3);
- concave charts and finite unanimity (Thm 8.19);
- full-domain regular charts force orthant-planarity (Thm 8.20, Cor 8.21);
- continuous and direction-continuous piecewise-linear charts, as certificate exclusions (Thm 8.22, Appendix A).

The first part of the regular-chart item (R15) is removed, because its source chain cannot be checked.

**Citations.**
- Rockafellar 6.3 and 11.3 are verified.
- Rockafellar 13.2 and Schrijver §8.5 are replaced by self-contained proofs.

**Referee result.** No mathematical error. Four over-broad scope sentences and one wording slip were fixed.

**Found while refereeing.** The refereed proof of C62 Lemma 4.3 has a real gap when u·c vanishes along an inner half-wall (an explicit "valley" example). The repair is to apply the strict-sign lemma (DC63 4.2-D(b)) first. The paper's route already does this. Results cited as "C62 Thm 4.1 as repaired by REF62", such as IN63 Theorem S, need this one-line insertion.

**Now inconsistent with §2.** The paper's open problem (1) (is every coherent model covered?) and the framing of its §8 exclusions predate Theorem H. They must be revised: the exclusions are about specific construction classes, and the universal question is now answered for full-dimensional targets on one-sided domains. This is not yet done.

## 6. Coverage map after round 65
- **Covered exactly:**
  - every full-dimensional credal set, by comparison-deleted Brier on a one-sided domain;
  - precise targets, on the full domain by plain Brier.
- **Covered by score-generated (complete, transitive, (Add)) rankings:**
  - the VB class;
  - class X (veto–box);
  - orthant-planar polygons and boxes;
  - composed targets.
- **Open:**
  - lower-dimensional, non-precise targets (two-sided domains);
  - whether a reasonable, coherence-independent (for example score-generated) ranking covers the reversed triangle and the other remaining targets;
  - the exact class reached by score-generated rankings.

## 7. Questions for the author
1. **Which question is now the main one?** The coverage question under the agreed axioms is answered for full-dimensional targets. The remaining substantive question is the auditor's distinction. What must a ranking satisfy to count as an *independent* accuracy-based justification, rather than a representation of coherence? Candidates include being score-generated (complete, transitive, (Add)), having each world's verdicts determined gamble by gamble, and not referring to coherence in their definition.
2. **Lower-dimensional targets.** Should the next round extend Theorem H to two-sided domains?
3. **The covering paper.** Should it now be reframed around Theorem H, with the score-generated constructions presented as "coverage by coherence-independent rankings", or should Theorem H get a separate short paper (the UN65 draft)?
