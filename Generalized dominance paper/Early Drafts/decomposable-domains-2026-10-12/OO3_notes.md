# OO3 (round 43, BRIEF35): consolidation notes for "Quorum Rankings and the Contamination Triangle"

19 Oct 2026. Deliverables:
- `OO3_quorum.tex`, compiled to `OO3_quorum.pdf` (25 pages; pdflatex, no errors, no overfull boxes).
- One script, `oo3py/ex51_patterns.py` → `oo3py/ex51_patterns.out` (exact integers; used for Remark 12.2).
- `oo3py/png/`: page renders, for inspection only.

No assumption is added. The audit's corrected scopes (AUDIT_LL, AUDIT_MM, AUDIT_NN; BRIEF33–35) and every referee repair (MM3, NN3) are applied in the .tex and marked "repair" or "scope" there. Every recorded `.out` cited in the note ends with `ALL CHECKS PASSED` (rechecked today).

The inconsistencies between notes are listed below. They are **not** silently resolved. Where the .tex had to pick a formulation, it says which one it uses and why.

## A. Inconsistencies between notes (substantive)

1. **Zero entries of common essential values.**
   - NN3 §2.2 shows that a common essential value can have zero entries, even though switch values are nonzero a.e. It therefore repairs MM2 Lemma 3.2 by adding the hypothesis y_iv ≠ 0 on F.
   - NN1 Theorem 3.2, Step 1 (and Cor 3.3), written in the same round, asserts "by strict guidance every entry y_iv is nonzero". It also uses ψ := evaluation at y⁰, which needs positivity of every |y⁰_iv|. So NN1's proof needs the same repair.
   - NN2 §4.1 imports MM2 Lemma 3.2 "verbatim", together with the "≥ 13 extreme supports" count. That import inherits the repair.
   - NN2 Theorem 4.1 itself is fine: its null set N₁ excludes approximate value 0.
   - *In the .tex:* Theorem 9.2(a) is stated on N* (values with all relevant entries nonzero), with an explicit flag. Lemma 6.6 carries the hypothesis. Not otherwise resolved.

2. **The edge-case hypothesis of the collapse (|S| = 2).**
   - NN2 (remark after Thm 2.3) says that with only 2q > n, Steps 1–4 give coincidence at *one* world, and that 3q > 2n is needed to propagate.
   - NN1 Lemma 2.1 (two colours) gives coincidence at *both* worlds, with a common point, under 2q > n alone. NN1 Thm 3.2 accordingly claims edge collapse for every quota with 2q > n. NN2 Thm 4.1 states the plane-wise edge collapse under 3q > 2n.
   - These are not contradictory, because NN2's conclusion (b) is stronger. But NN2's remark understates the two-world case. The .tex states both, with their own hypotheses (Remark 8.4).

3. **The headline scope of the fixed-margin exclusion.**
   - LL2 §0 says that no quorum system satisfies (S), with any selection, for "any q ≤ n". LL1 §0 says (S) fails "for no selection at all, continuous or not".
   - The proved scope (LL2 Cor 5.2; MM3 §2.4; AUDIT_LL) is narrower. For continuous selections the exclusion holds for every q. For closed sections (which is what (S) asks) it holds only for proper games (2q > n), and LL1 Thm 4.2 needs coherent selections on the full domain.
   - The .tex uses the corrected scope (Theorem 4.4 (i)/(ii)).

4. **What the audit's remark on NN1 Example 5.1 refers to.**
   - AUDIT_NN_summary says the example's "simplest realisation actually fails" the exact test. No note read for OO3 proves this for Example 5.1 specifically, and the audit names no realisation.
   - The nearest written result is NN2 Prop 6.3 (fixed-column rank-two data fail (QS) near T1). It requires all six mixed sign patterns.
   - OO3 checked exactly that the Example 5.1 columns realise all six mixed patterns and no pure one (`oo3py/ex51_patterns.out`). So Prop 6.3 applies to fixed-column realisations of those data.
   - The identification of the audit's remark with this argument is OO3's own, and it is labelled so (Remark 12.2).

5. **Readings stronger than the theorems (MM1).**
   - The phrase "the quorum collapses to one field" in MM1 §0 and §6 is local (pinned cells). It is not the global proportionality that Prop 3.2 needs (NN3 §1.4).
   - MM1 Prop 5.1(b) says "hence globally" for penalty differences at all advices, including ×. This was unjustified and is not needed (NN3 repair: proportionality on {+,0,−} suffices).
   - The .tex states the repaired versions.

6. **MM2 §7 (R5), "exactly".**
   - MM2 says the gap between alignment and (NT_F) consists "exactly" of records whose change set lies in the common tie set of all weak-Bayes weights.
   - NN3 §2.4 corrects this: every violator lies in that set, but the set does not characterise the violators. The .tex uses NN3's wording.

7. **Bounds in the lifting lemma.**
   - AUDIT_LL and BRIEF33 state 0 < ψ(s) ≤ s, but the construction gives ψ ≤ s/2.
   - MM3 R2 and the transfer of Theorem A use ψ(s) < s, or ψ ≤ cs with c < 1. MM3's clean statement uses ψ ≤ s/2, and the .tex adopts it.
   - The setting also changes: "full measurable menu domain" (AUDIT_LL) becomes "decomposable domain" (MM3 repair), since menu terminology was retired in the write-up.

## B. Inconsistencies of notation or emphasis (no mathematical conflict)

8. **Two different thresholds, both written M\*.** LL2 Prop 7.1 gives M\* ≈ 1.2832 for (4,3), η = 1/16: the threshold for the **sum** field to endorse. LL3 Cor B1′ gives M\* = 7/5: the threshold for the min-of-sums field ℓ\* and for every endorser. MM3 §3.2 confirms consistency. BRIEF and LL3 Cor B4 use LL3's. The .tex keeps LL3's and adds a warning.
9. **"No escaping configuration" versus "the escape is real".**
   - NN2 §0 says that no three-generator cone configuration escapes (intersection form), so that "deliverable (b) as posed is impossible".
   - NN1 §0, and NN2 §6 itself, exhibit escaping configurations in **sum** form.
   - The two claims are consistent once intersection form and sum form are distinguished. The .tex keeps them apart (Sections 8 and 12).
10. **The audit's five-model example.** AUDIT_quorum reports a strict 5-cycle and states that the triples satisfy (TC). LL3 §2.4 finds two additional strict 4-cycles that the audit did not report. This is an omission, not a contradiction.
11. **LL3 Thm A(b), realisation wording.** "One margin-steep pair and equal masses otherwise" is ambiguous: one reading makes an S₂-only judge support X R Z. MM3 §3.3 gives explicit masses, and the .tex states the repaired masses.
12. **MM1 Thm 4.2 Part A (T1-only design).**
    - MM1 labels it "CHECKED (exact), hence PROVED", with checks for ε ∈ {1/10, 3/10, 1/2} only. NN3 §4.1 says it holds for every ε by the pair structure.
    - The .tex states it for every ε, citing that argument: every pair cone contains κ\*_i.
13. **"Self-contained".** MM1 Thm 4.2, and NN1 Cor 4.3 / NN2 Cor 3.2 after it, are called self-contained. That means no FF2 import. Step 1 does still use the write-up's equivalence of measure-closeness and Hausdorff-closeness for coherent models (write-up Prop reduction(b), R1 Prop 3.1).
14. **NN1 Thm 4.1 (interior collapse under (B)).** It is written with k = 3 for (7,5). NN1 does not state a general (n,q) version, so the .tex restricts it to (7,5).

## C. Status caveats recorded in the .tex (so they are not lost)

- **Not refereed line by line:**
  - NN1 and NN2 in full. AUDIT_NN gave a focused review only: NN2 §2, §§5–6, and the NN1 statements. The collapse theorem was judged to "appear sound".
  - MM3's own observations R1–R3.
  - NN3's Prop A, Cor A.2, Lemma B.1 and Part B.
  - LL3 Prop A8, Lemma B0 and Cor B4.
- **Imports.** Prop 10.1 (proportional blocking sets), Prop 10.11(b) (rank two) and Cor 7.4 rest on the FF2 Thm 4.1 import chain (D1, BB2 Thm 6.1, M3.7–3.8, each refereed once).
- **Construction hierarchy (BRIEF35).** Only level (b) has been reached: T1 alone. NN1 Ex 5.1 and NN2 Prop 6.1 are level (a).
