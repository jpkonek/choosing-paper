# UN65: sources and referee status for "Universal coverage by comparison deletion (draft)" (26 Oct 2026)

Files written (all in `r65/`):
- `Universal coverage by comparison deletion (draft).tex` and `.pdf`: 14 pages. It compiles cleanly with pdflatex under its own filename, with no undefined references and no overfull or underfull boxes.
- `un65py/add_example.py` and `.out`: an exact re-verification of Example 7.1. It uses `ref64es_py/xcone.py`, not `es64py/`.
- `un65build/`: build copies only.

Every result in the note is taken from a source that a referee report rated CORRECT, or is a direct consequence of such results. Nothing labelled CONJECTURE or NUMERICS is used.

## Map from results to sources

| Note | Content | Source | Referee status |
|---|---|---|---|
| §2.1 Lemma 2.1 | Facts about D_S. (b): the boundary is null, by the graph-over-𝟙^⊥ argument. (d): open sets a.e. inside D_S lie inside D_S | Paper §2: `lem:D` and `lem:open`. The proof of (b) is from WT65 C2(b) / REF65_hA a2. The proof of (d) is direct and replaces the citation of Rockafellar 6.3 | Paper refereed in REF64_paper / REF65_paper; WT65 C2 re-checked in REF65_hB H10 |
| §2.2, 𝒞_U description | 𝒞_U = {D_Q : K' ⊆ Q} | Paper §2; WT65 C1(b) | as above |
| §2.2 Lemma 2.2 | Q_B is a credal set ⊇ K'; B ⊆ hull(B) a.e.; hull(B) is the least coherent model containing B | ES64 §5 (definition); REF64_es E23 and §2.5; H65 Lemma 2.2(c) | REF64_es E23 CORRECT; REF65_hB H2 CORRECT; REF65_hA a2 CORRECT |
| §2.3–2.4 | Framework: reflexive relations with (TC), (FCC), dominance terminology, Brier loss and uniform dominance, (G), (IB), (GC), (C), (ID), (LF), (W), Definition 2.4 (cover) | Paper §2 (`def:dom`, requirements, `def:cover`); AUDIT_r64_decisions; FCC from AUDIT_nontransitive / REF64_es E3 | binding framework |
| Lemma 2.5(a),(b) | D_K ∈ ℳ_U ⟺ K' ⊆ K; (LF) ⟺ K' ⊆ relint K for full-dimensional K | Paper `lem:LF` (Lemma 4.5) and `lem:fulldim`(c),(d). Rockafellar Thm 11.6 is used directly (verified in round 64) | Paper refereed; REF65_hA §3.4 and REF65_hB §4 confirm its use here |
| Lemma 2.5(c) | Lower-dimensional K: (LF) fails on any domain with V ∩ (−V) null | Paper Prop 2.10 (`prop:lowdim`), first claim, in the simpler one-sided form. The essentially one-sided form is cited after Prop 6.3 | Paper refereed; REF65_hA f2/f4 |
| §3.1 Lemma 3.1 | Record relations satisfy (IB) | ES64 Lemma 1.1 | REF64_es E1 CORRECT |
| §3.2 Lemma 3.2 | Deletion lemma, stated for (FCC) and hence (TC) | ES64 Lemma 1.3 + REF64_es E3 (chain strengthening) | REF64_es E3 CORRECT |
| §3.3 Def 3.3 + existence of i(r) | Comparison-deleted Brier ranking CD(𝒩), for any n ≥ 2 | ES64 Def 3.1 | REF64_es E10 CORRECT (also notes validity on two-sided domains) |
| §4 Theorem 4.1(a)–(c) | Axioms; protection of 𝒩; (★) ⇒ domination (strict if the margin is strict) | ES64 Thm 3.2 | REF64_es E11–E14 CORRECT; §2.2–2.4 |
| Theorem 4.1(d),(e) | Necessity of (★); equivalence (★) ⟺ 𝒩-domination of everything outside 𝒩 | REF64_es §2.5 (referee result) | REF64_es E13; re-checked in REF65_hA §3(2) and REF65_hB §4 |
| Corollary 4.2 | Attack ⟺ hull-null; (ID) for CD(𝒞_U) ⟺ (H) | ES64 Cor 3.5 + REF64_es §2.5 | REF64_es E17 (converse added by the referee) |
| Lemma 4.3 | hull(B) = cone(B_d) + int ℝⁿ₊ | WT65 Lemma W1 (with Claim 0 and (2.1)) | Used and checked as CORRECT in REF65_hA d1 and REF65_hB H1/X4 |
| Corollary 4.4 | Density-point witness, r ≤ n | WT65 Cor W1′ (auditor's witness, AUDIT_r65_brief) | as above. The sharper bound r ≤ n−1 (WT65 W2) is **not** included |
| §5 Lemma 5.1 | Contraction lemma: q·x ≥ −cP(x) a.e. on X ⇒ q ∈ Q_X | REF65_hA §1, Lemma S | REF65_hA (full proof; 175 exact checks + LP numerics). Stated with complete proof, so used as instructed |
| Corollary 5.2 | Shrink invariance: hull(X∖N) = hull(X) for every N ⊆ D_{(1−τ)Q_X+τΔ} | REF65_hA §1, Corollary S | as above |
| Theorem 5.3 | (H), with a strict margin and N ⊆ hull(X∖N) | X65 Theorem H.1, in the streamlined form of REF65_hA §1: Step 1 is the minimax Step 1′; Step 2 is X65 Steps 2–3 with REF65_hA's choice μ(N₀∖N_τ) < μ(N₀∖X); Step 3 is Corollary 5.2, replacing X65 Steps 4–5. The idea of Step 1 (dominate from inside hull(X)) is due to H65 | REF65_hA: CORRECT. REF65_hB: CORRECT, recommends X65's proof. The acknowledgement crediting H65 was removed from the note at the lead's instruction, so the credit is recorded here only |
| Remark 5.4(a) | Hypotheses not used (regularity, pointedness, dim K', K' ⊆ relint Δ) | REF65_hA "hypotheses actually used"; REF65_hB headline 1 | CORRECT |
| Remark 5.4(b) | Explicit defender; λ* minimises a convex function | REF65_hA §1, after Step 1′ | — |
| Remark 5.4(c) | Every non-Bayes model on U is uniformly Brier-dominated by a Bayes act | ES64 Lemma 5.1; here it is Step 1 with G = U | REF64_es E22 CORRECT |
| Remark 5.4(d) | H65's Generation Lemma, stated without proof; the lineality hypothesis cannot be dropped; this route uses K' ⊆ relint Δ | H65 Lemma 2.3 and Theorem H, Steps 2–5 | REF65_hB H4 (CORRECT; lineality hypothesis necessary via X65 Example NP), H6, H9 |
| §6 Theorem 6.1 | Main theorem (a)–(e) | X65 Cor H.2 / H65 Cor H.2, with the scope repair "full-dimensional" | REF65_hA f1–f2 and §3; REF65_hB §4. FCC: REF64_es E3. Strict dominance with margin: REF65_hA §3(3) |
| Corollary 6.2 | Every full-dimensional K is covered on some domain (K' = {k₀}) | REF65_hA f3; REF65_hB §4 "Across domains" | CORRECT |
| Prop 6.3 + following paragraph | Lower-dimensional targets are not covered on one-sided domains; the stronger paper version; the Brier ranking covers precise models on the full domain; the two-sided analogue is open | Paper Prop 2.10, Cor 5.9; REF65_hA §6 (open question; Step 2 needs K' ≠ ∅; Q_B may be empty); REF64_es E10 | as cited |
| §7.1 | Universality is relative to U | AUDIT_r65_brief scope correction 2; REF65_hA f3 | — |
| §7.2 | Coherence-informed definition; representation, not independent justification; (ID) is not definitional; cross-world dependence | AUDIT_r65_brief "Decision"; AUDIT_r65_message; REF64_es §5.3(1),(2) | — |
| §7.3 (Tr), (Add) | Definitions; (Tr) ⇒ (Add); (IB)-form of (Add) | REF64_es §5.4 remarks; AD65 Lemma 1.1 and Prop 3.1 | REF65_ad items 1, 3 CORRECT |
| Example 7.1 | An exact failure of (Tr) and (Add) at world 1, for every 𝒩 ∋ D_K | REF64_es §5.3(3) (`ref64es_py/add_fail.py`) | CHECKED exactly by REF64_es; REF65_ad item 27 confirms that (Add) excludes Δ(𝒩). **Re-verified here** in exact rationals (`un65py/add_example.out`). The split parameter c = −19/100 is written as the linear form w = (76, −43, 157) |
| Lemma 3.2 (revised) | The deletion lemma now allows φ to take values in any totally ordered set, so that it applies to the lexicographic score in Remark 7.2 | ES64 Lemma 1.3; REF64_es §2.1 | the proof is unchanged |
| §7.3 Remark 7.2 + proof | LD(𝒩) (= R_lex(𝒩)): (a) (G), (IB), (FCC), (TC), (Add); (b) protection; (c) N ∈ 𝒩 dominates X ⟺ (★), and then dominates strictly; (d) for 𝒩 = 𝒞_U: (ID) ⟺ (H) **for this ranking only**, and by Theorem 5.3 a universal cover with the coverage set of Theorem 6.1(e). Transitivity is not claimed | AD65 Def 5.2, Thm 5.2 and Cor 5.3 | REF65_ad items 21–22 (CORRECT, line-by-line §4.2). The scope of the "only if" follows REF65_ad E1/item 23: the equivalence is stated for LD(𝒞_U) itself, and the remark says explicitly that it does not say every (Add)-ranking cover yields (H). Transitivity is not claimed (AD65 item 20: open) |
| §7.3 intro (revised) | The ⊔ notation; r(X,Z) = r(X,Y) ⊔ r(Y,Z) for non-overlapping steps; closure of Acc under ⊔ ⇒ (Add); the failure of (Add) is attributed to CD(𝒞_U), not to universal coverage | AD65 Lemma 1.1; REF64_es §5.4 | REF65_ad item 1 |
| Abstract (revised) | Adds that a lexicographic variant satisfies (Add) and is a universal cover | Remark 7.2 | — |
| §7.4 | Sub-relation of Brier, incomplete; coherent models can be uniformly Brier-dominated yet undominated | Theorem 6.1(a); REF64_es §5.1; ES64 Lemma 5.1 | as above |

## Not included (deliberately)

- WT65 W2 (n−1 removed points), the compactness tools C1–C3, the lower semicontinuity result C4, and examples C5–C6.
- X65 Theorem 2D (two worlds), Lemmas 4.1–4.3 and Example NP. Example NP is mentioned only implicitly, in Remark 5.4(d).
- H65's full proof. Only its Generation Lemma appears, without proof, in Remark 5.4(d).
- AD65 / REF65_ad material beyond §7.3 and Remark 7.2, e.g. Ex T, Ex V, Lemma 4.2 and the implication lattice.
- Labels and statuses of the project (PROVED / CHECKED), round numbers, and commentary on history.

## Flags

1. **Resolved (lead's change 1).** The R_lex remark has been added with its proof (Remark 7.2), and §7.3 and the abstract have been rephrased.
2. **Resolved (lead's change 2).** No project-internal labels remain in the .tex (checked by grep). The acknowledgement section has been removed.
3. **Example 7.1** rests on exact computer arithmetic, not a hand proof, and the note says so. It concerns one μ (density e^{−|h|₁}) and the reversed-triangle data.
4. **Generality of the standing assumption.** It is K' ⊆ Δ (nonempty, compact, convex), not K' ⊆ relint Δ.
   - Theorem H does not use relint (REF65_hA, REF65_hB).
   - The proofs of Theorem 4.1 and Remark 7.2 need only that U contains no h ≤ 0 and that coherent models contain int ℝⁿ₊.
   - Coverage forces K' ⊆ relint K anyway.
5. **Lemma 2.5(c)** is proved only for domains with V ∩ (−V) null. The paper's stronger "essentially one-sided" version is cited.
6. **Author block** is the name only.

---

# Revision after REF65_un (26 Oct 2026)

REF65_un found no mathematical error. Its required changes 1–9 have been made in place. The pre-revision source is backed up at `un65build/before_ref65un.tex`. The note recompiles cleanly to 14 pages: there are no warnings, no overfull or underfull boxes, and no undefined references.

| # | REF65_un item | Change |
|---|---|---|
| 1 | Abstract scope (ERROR) | The abstract now says "need not be transitive, and can violate disjoint additivity" |
| 2 | "Universal cover" undefined (GAP) | Added Definition 6.2: K is coverable on V if some ranking on ℳ_V covers it; a universal cover on V covers every K that is coverable on V. Added Corollary 6.3 with its two-line proof: CD(𝒞_U) covers K ⟺ K is coverable on U, so CD(𝒞_U) is a universal cover on U. Proposition 7.2(d) states the same for LD(𝒞_U). The abstract and §7.3 now use the defined term |
| 3 | Remark 5.4(d) (GAP) | Deleted. This removes the generation lemma and its unproved claims |
| 4 | Remark 7.2 → Proposition | The definition of LD(𝒩) is now prose before an unnamed Proposition 7.2. The lexicographic order is defined explicitly. Lemma 3.2 is now applied with φ := −Φ_i under ≥_lex, replacing "reverse lexicographic". The scoping sentences ("only if" concerns LD(𝒞_U) only; transitivity is not claimed) now follow the proof |
| 5 | (M) as a standing assumption | §2.1 now says "Throughout, μ satisfies (M)". The redundant "Assume (M)" has been removed from Theorems 5.3 and 6.1 |
| 6 | Remark 5.4(b) (minor GAP) | Added the density argument. A density point of N∖X is a density point of N. At a point of ∂N, a supporting half-space contains N, so the density there is at most 1/2. Hence such a point lies in N ⊆ hull(X∖N), and the witness follows from Lemma 4.3 and Carathéodory |
| 7 | Abstract "and nothing else" | The abstract now says that the reverse comparison on Brier ties is also deleted, and that deletions are by record and so apply in every context |
| 8 | Terminology | The (LF) gloss "that is, satisfies X ⊆ U a.e." is restored. A sentence after the definition of "one-sided" says how it differs from [KCM]'s "one-sided" (empty) and "essentially one-sided"; the note's condition lies between them. The introduction now says "covers a credal set K" |
| 9 | Small points | After Lemma 3.2, "real score" is now "score with values in a totally ordered set". Lemma 4.3 now has "(let s→∞)". §7.2 now reads "…represented as the undominated models of a ranking satisfying (G), (IB), (TC) and (FCC)…". After Theorem 6.1, a new sentence says that if K' meets ∂Δ no credal set is covered, although (a)–(d) still hold |

Numbering after the revision:
- Definition 6.2 and Corollary 6.3 are new.
- The old Corollary 6.2 is now Corollary 6.4.
- The old Proposition 6.3 is now Proposition 6.5.
- The old Remark 7.2 is now Proposition 7.2.

The source map in the table above is otherwise unchanged. The only further correction to it: Remark 5.4(d) has been removed.
