# WA68: changes file for the definitive application paper

26 October 2026. Role: WA68 (BRIEF68).

## Deliverables
- `Coherence and accuracy for sets of desirable gambles.tex` and `.pdf`.
  - The title is the one the brief proposed.
  - Authors: Jason Konek and Catrin Campbell-Moore, as the brief requires. **The lead should flag this to the author.**
- Compilation: pdflatex, three passes.
  - No warnings, no undefined references, no overfull or underfull boxes.
- **Length: 24 pages.**
  - Main text: pp. 1–18.
  - Appendices A–D: pp. 19–24.
  - References: p. 24.

## Structure
| § | Content |
|---|---|
| 1 | Introduction: the repair theorem stated informally; the mechanism; the ranking; four scope qualifications (separable space with an order unit; models identified up to null sets; full support and how to drop it; some uniform repair, but not every dominance is uniform); achievement and limitation stated together; the veto–Brier contrast. |
| 2 | Setting: states (Lemma 2.1); measure and score (Lemma 2.2); models and coherence (Lemma 2.3); supporting states and the coherent hull (Lemma 2.4); changes, the test, joining (Def 2.5, Lemmas 2.6–2.7). |
| 3 | Minimax lemma (Lemma 3.1), with the explanation of fractional acceptance; Cors 3.2 (consistent case) and 3.3 (uniformly losing part). |
| 4 | Contraction (4.1), trimming (4.2), the change lemma (4.3), and Remark 4.4 (neither hypothesis can be dropped). |
| 5 | Repair theorem (Thm 5.1): both cases and the location clause; Remark 5.2. |
| 6 | The ranking: the plain rule (Def 6.1); its properties (Prop 6.2); the maximality characterisation (Prop 6.3); not transitive and not complete (Ex 6.4); dominance (Lemma 6.5, Props 6.6–6.7); the requirements and the main theorem (Thm 6.8), with full support and how to drop it. |
| 7 | Restricted domains: Cor 7.1, and examples of domains closed under coherent hulls. |
| 8 | Veto–Brier contamination example (Thm 8.1, Fig. 1), with the contrast. |
| 9 | Discussion: what is established; the third condition as an open question; scope; open questions. |
| A | Proofs of Lemmas 2.1–2.3. |
| B | Ex B.1 (dominance need not be uniform); Ex B.2 (μ{P_S = 0} = 0 is essential); Rem B.3 (replacing 𝟙 by an order unit). |
| C | One-sided domains (Prop C.1): exact local freedom; the finite-world form; K_⊥ ≠ {0} is excluded. |
| D | Proof of Thm 8.1: Lyapunov, Zorn, separation, uniqueness, coherence, target. |

## Map of results to sources and refereeing
Abbreviations:
- **OUT** = `OUT67_application_outline.md`.
- **UC** = `Universal coverage … (draft).tex`.
- **COV** = `Covering coherent sets … (draft).tex`.

| Manuscript | Source | Refereed by |
|---|---|---|
| Lemma 2.1(a)–(f) | OUT Lemma 1.1; UC Lemmas states, envelopes, normingE(b) | IW66a, IW66b, REF66_iw; REF67_out C1. **Glue:** the clause ∂D_Q = {P_Q = 0} (two lines, from UC envelopes(b)). |
| Lemma 2.2 | OUT Lemma 1.2 and §1.5; UC Lemma measure, Lemma D(b) | IW66a, IW66b, REF66_iw; RF67b row 21 |
| Lemma 2.3(a),(b) | OUT Lemma 1.3; UC Prop cdg | IW66a, IW66b, REF66_iw; REF67_out C5–C6. **Glue:** the instance μ = δ_𝟙 + δ_{−𝟙} illustrates the refereed remark (RF67b row 19) that every D_Q is a.e. D_S when μ is carried by D_S ∪ (−D_S). |
| Lemma 2.4(a)–(d) | OUT Lemma 1.4(a)–(d),(f); (e) folded into Cor 3.3(b) | RF67a S5; RF67b row 1, §3.3; REF67_out C7–C8 |
| Def 2.5, Lemma 2.6 (test) | OUT Lemma 5.1 | SR66, IW66b; RF67a S5; RF67b G1; REF67_out H4 |
| Lemma 2.7 (joining) | UC Lemma record(b), Lemma safe(c) | earlier rounds (SR66) |
| Lemma 3.1 (minimax) | OUT Lemma 2.1; UC Thm Hinf Step B | IW66a/b; RF67a P1–P4; RF67b rows 2–3; REF67_out C9 |
| Cor 3.2 | OUT Cor 2.2 | RF67a T1; RF67b row 7; REF67_out C10 |
| Cor 3.3 | OUT Cor 2.3 | RF67a P1–P6; RF67b §2.1, §3.3; REF67_out C11 |
| Lemmas 4.1–4.2 | OUT Lemmas 3.1–3.2; UC Lemma contraction, Prop shrink | REF65_hA; IW66a D1–D2; REF67_out C12–C13 |
| Lemma 4.3 | OUT Lemma 3.3(a) | RF67b Prop R; REF67_out C14 |
| Remark 4.4, second part | OUT Remark 3.4, family and n = 2 example | REF67_out U2–U3, §2.1 |
| Remark 4.4, first part | **NEW** (see below) | — |
| Thm 5.1 | OUT Thm 4.1, both cases. The inconsistent case uses region hull(X₊). μ(N∖X) > 0 is proved from Lemma 4.3 and Lemma 2.6, which is OUT Lemma 3.3(c) inlined. | RF67a, RF67b; REF67_out C17–C19, U5, §2.2 |
| Remark 5.2 | OUT Part 4 remarks | RF67a T6, B4; REF67_out C19 |
| Def 6.1, Prop 6.2 | OUT Def 5.2, Prop 5.3 | SR66; IW66a/b; RF67a E5–E6; RF67b row 15; REF67_out C21 |
| The sentence that the guidance-only relation has every property of Prop 6.2 | **Glue** | — |
| **Prop 6.3 (maximality)** | **NEW** (brief, author's addition 3); proof verified below | — |
| Ex 6.4 | UC Example tr, moved to the full domain ℝ² | UC example refereed in earlier rounds. **Glue:** the move uses Lemma 2.6 with B consistent; the argument is unchanged. |
| Lemma 6.5 | OUT Lemma 5.4, with Ω′ = Ω | RF67a E1–E4; RF67b §3.1 |
| Props 6.6–6.7 | OUT Props 5.5–5.6 | RF67a; RF67b row 15; REF67_out C23. **Glue:** (i)⇒(iv) is argued directly, as in the protection proof, instead of through OUT 5.4's "non-null ⇒ closed". |
| Thm 6.8 | OUT Thm 5.7 (a)–(d),(f), headline with (M3) | RF67a S2–S4; RF67b rows 15–19; REF67_out C24 |
| Requirements list (§6.3) | UC/COV Def cover, in words. Local freedom is stated as "an open set containing ∂D_K∖{0} lies in U a.e." | The equivalence with the original form is RF67a §2.4 (test with D_K ∪ O). |
| Cor 7.1 and examples | OUT Cor 6.1 and examples (E; D_{K′}; U ⊇ {sup h > 0}; D_{K′} ∪ F) | RF67a C3, §2.4; RF67b §3.5; REF67_out C27, U4 |
| Thm 8.1 | COV Cor contam with s = 0 (K′ = {p}, A_i = {v_i}), an instance of COV Thm cover | Round 61: P61 Thm A; REF61 rows 1–3; VB_dominance_note (refereed once). REF67_out V2 asked for exactly this form. |
| Thm 8.1(b), the clause "K* contains p and some v_i" | Read off Step 7 (W₀ ≠ ∅) | Glue |
| §8 contrast, "U itself is dominated" | Also in VB_dominance_note, setting paragraph | **Glue:** from Thm 8.1(b) and Lemma 2.3(a) |
| App A | OUT and UC proofs, as above | as above |
| Ex B.1 | OUT Ex 5.8 (gain βω on (0,1]) | REF66_iw §2.1; RF67a. **Glue in the write-up:** it follows the construction in UC "Worlds and norming sets" (Lyapunov ball, plus A₀ ⊆ D_S), adapted to the target gain (0, β) on the full domain. |
| Ex B.2 | UC Example PS, on the full domain | earlier rounds; RF67a E1; RF67b row 14 |
| Rem B.3 | OUT Remark 1.6; UC Remark orderunit | IW66b §7.1; REF66_iw W5; RF67a H2; RF67b row 22 |
| Prop C.1(a),(c) | OUT Cor 6.2(a),(c); UC Prop inf-LF, Thm inf-cover(c) | IW66a P1–P2; IW66b §6.2; REF66_iw; REF67_out C28 |
| Prop C.1(b) | OUT Cor 6.2(b); UC Lemma LF(b) | note Lemma LF(b); REF67_out C29 |
| App D | COV Lemmas axioms, lyap, zorn, sep, unique, coh, Remark direct, Lemma LF(a); P61 A1–A11 | REF61 §1 (every step re-derived). Specialised to A_i = {v_i}. |
| §9.2: property (3) implies coherent admissibility | **Glue** (one line, reusing the proof of Prop 6.6) | — |
| §9.3: mutually singular measures | UC §Scope "Dependence on μ" | **Glue:** the construction of disjoint dense sets D₀ and D₀ + x₀, with x₀ ∉ D₀ − D₀ |
| §9.3: reweighting sentence | OUT Remark 1.5 | REF67_out U1 |

## New mathematics, all of it elementary

1. **Prop 6.3 (maximality).** Proof checked.
   - **The ranking has properties (1)–(3).**
     - (1) holds by clause (i).
     - (2): a non-null guided change has increment ∫_A |h(ω)| + ∫_B |h(ω)|. The integrand is positive a.e. on the non-null set A ∪ B, so the increment is positive. Clause (ii) changes are positive by definition. (M2) is not needed.
     - (3) holds because clause (ii) applies only to changes that no coherent model could make.
   - **It is the largest such relation.** Let R satisfy (1)–(3), and suppose X R Y.
     - If X = Y a.e., the change is null, hence guided, so it is in the ranking.
     - Otherwise the increment is positive by (2).
     - If some coherent model could make the change, it is guided by (3).
     - If not, clause (ii) applies.
   - The lead's check is correct as stated.
2. **The guidance-only relation.** It has every property of Prop 6.2, by the same proof. This is the brief's "these properties alone do not characterise it".
3. **Remark 4.4, first part.** A score gain at every world does not suffice without the hull inclusion.
   - Setting: ℝ² with standard Gaussian μ; X = ∅; N = W ∪ W′, where W is the ball of radius ½ about (3,−1) and W′ is its mirror image.
   - Both coordinates of m(N) equal ∫_W (h₁+h₂) > 0.
   - D_Δ misses N, so D_Δ could make the change.
   - This replaces OUT's unproved remark that "the gain alone is not enough".
4. **§9.2.** Property (3) implies that coherent models have no weak dominator other than themselves.
5. **The minor glue listed in the table.** Ex 6.4 moved to ℝ²; the Ex B.1 write-up; disjoint lines in §9.3; the instance δ_𝟙 + δ_{−𝟙}; ∂D_Q = {P_Q = 0}; the direct (i)⇒(iv) in Prop 6.7.

Nothing else is new. No unrefereed result from the outline is used:
- The nonseparable sketch is omitted. It appears only as an open question.

## Cut or demoted (relative to OUT)
- **Dropped:**
  - OUT Lemma 3.3(b), the uniform-gain version without (M2). (M2) is standing.
  - "World sets" (dependence of dominance on Ω versus Ω₀).
  - Uniform local freedom and Prop tube.
  - Cor 6.2(d) (contamination on C(Ω)).
  - Cor 6.3(b)–(e), including (LF) on V₀ and the geometric density-point test.
  - The half-space alternative in the inconsistent case.
  - The countable-union remark.
  - The visibility class, its figure and its catalogue (per the audit).
- **Inlined:**
  - OUT Lemma 3.3(c), into the proof of Thm 5.1.
  - Lemma 1.4(e), into Cor 3.3(b).
- **Moved to appendices:**
  - the one-sided classification (App C, short);
  - the delimiting examples (App B).

## Flags for the lead
1. **Authors.** The author block lists Konek and Campbell-Moore, as the brief requires.
2. **Example 6.4.** I used UC's Example tr, moved to ℝ². I did not use RF67b's ℝ² example, whose positive increment (0.0145) is a numerical quadrature.
   - In Example tr, the increment bound is exact (> 1.075δ).
   - It also gives incompleteness directly.
   - **The referees should confirm the move.** It uses the full-domain test with B consistent; no other change.
3. **Thm 8.1** is the case s = 0 of COV Cor contam, on the domain {p·h > 0}.
   - Its proof was specialised and checked step by step against P61/REF61.
   - It does not depend on LDG. App D carries Lyapunov, Zorn and separation in full.
4. **Bibliographic details to check:**
   - Aliprantis–Border Thm 6.30, for weak-* metrizability of the dual ball;
   - the page range of the Quaeghebeur chapter (1–27).
5. **No cross-citation of LDG,** so there is no dependence in either direction.
   - If the lead wants a pointer, add one sentence in §9.1 once WL68's title is fixed.
6. **Models are completion-measurable sets modulo null sets,** not Borel sets.
   - This makes Walley-coherent sets literally models.
   - Every notion is class-invariant, so nothing changes.
7. **The referees should re-check every glue item and Prop 6.3,** per BRIEF68's verification phase.

---

# Revision 2 (after RA68a, RA68b, RX68; lead's instructions 1–15)

**Compile:** pdflatex ×3; no warnings, undefined references, overfull or underfull boxes. **Length: 26 pages** (was 24; +1 related work, +scope inside statements, +§2.3 second role of (M2), +§9 rewrite).

## Changes made
1. **Acyclicity** (RA68b #1, RA68a #6). Cover requirement (1) now defines acyclicity as the chain clause only. Prop 6.2(b): "every cycle consists of a.e.-equal models" is a separate bullet derived from "no ties". Thm 8.1(a): "complete and transitive, hence acyclic". §8 now notes that veto–Brier ties distinct models (Lyapunov halving) and that this is why acyclicity is the chain clause.
2. **"In general incomplete and intransitive"** in abstract, intro (×2), §8 (×2). Ex 6.4 now opens "The ranking need not be transitive or complete."
3. **Coherence framing** (RA68b #3). Abstract, intro ¶1 and §2.3: coherent sets are represented by credal sets only up to their boundary; identification holds modulo μ under (M2). Lemma 2.3 split: (b) the sandwich D_{K_D} ⊆ D ⊆ C_{K_D} without (M2), a.e. equality under (M2); (c) the Walley version. App A proof annotated (Steps 1–4 use no (M2)). §2.3 adds (M2)'s second role with RA68b's ℝ² ray example (Gaussian + law of (θ,−θ)); §9.3 restates both roles.
4. **Scope in statements.** Thms 5.1, 6.8 and 8.1 now carry their hypotheses, E separable/closed/containing 𝟙 (or order unit), and identification modulo μ. Thm 6.8(b) carries the uniformity caveat (Ex B.1). Thm 6.8 gains (c): every model is weakly dominated by an undominated coherent model (RX68 R-A5); old (c),(d) are now (d),(e); Cor 7.1(c) references updated.
5. **Protection and (M2).** Intro ("protected by the rule together with the null-boundary condition"), §9.1, §9.2 ("Under (M2), property (3) implies it", citing Lemma 6.5).
6. **§9.1** now points to Cor 7.1(d) for restricted domains instead of "the same holds".
7. **Veto–Brier contrast** scoped to "some genuinely imprecise targets" / "interior contamination" (abstract, intro, §8). Added the same-domain comparison: on U = D_{p} the ranking of Def 6.1 covers K and every full-dimensional credal set (nonempty interior relative to aff Δ) with p in its relative interior (Cor 7.1(d), Prop C.1(a),(b)).
8. **Related work** paragraph "Accuracy for imprecise credences" in §1 (SSK 2012 and others), positioning the paper; "requirements usually placed" → "the requirements we adopt", with Joyce (truth-directedness) and Pettigrew (additivity) cited in §6.3.
9. **Remark 4.4**: second part now uses the incoherent variant B ∩ {‖h‖ > 1}, with a proof of incoherence; first part's W′ described as the image under exchange of coordinates (the ball about (−1,3)), with exchange-invariance of μ stated.
10. **Terms.** "Available" defined in Def 2.5 and the intro; "available from" removed. "route" → "follows the classical argument from undominatedness to coherence". "Admissible measures" → "measures satisfying (M1)–(M3)". "The universal ranking" removed (now "the ranking of Definition 6.1"). Intro scope (1) "not covered" → "our results do not apply to it"; §6.3 "models available" → "models allowed".
11. **De facto names.** Italic run-in titles removed from Rem 4.4, Ex B.1, Ex B.2, Rem B.3 (now plain first sentences); item labels in Thm 5.1 and Prop 6.2 made parenthetical, not italic.
12. **Wording.** Lyapunov sentence now requires non-atomic μ ("in general, and in infinite dimensions, it need not be"). After Def 6.1: "Whether some coherent model could make the change does not depend on ω". The garbled sentence after Prop 6.3 replaced by the sharper form: ⪯_ω is already the largest relation with (2) and (3); (1) is automatic; no assumption beyond (M1). Intro and §9.1 describe Prop 6.3 in this two-condition form.
13. **Minor.** Abstract: "one minimax lemma, once for consistent sets and twice for inconsistent ones"; "characterised exactly by dominance in a ranking built from an accuracy score". Ex B.2 exponential variable renamed θ. §9.3 lists all four uses of separability. Uniform dominance: "the margin is measured by the score". §6.3: models on U "contained in U a.e. (we use a representative inside U)". Thm 5.1(3): "a fixed minimiser q*". After Thm 6.8: concrete loss without (M3) (δ_𝟙 + δ_{−𝟙}: one coherent model). §9.2: coherent admissibility phrased as in families of rankings. "Represent it exactly" used in intro and §9.1. Author block now `Jason Konek and Catrin Campbell-Moore`, date "October 2026", pdftitle/pdfauthor set (RX68 R-A10).
14. **Companion pointer** (§9.1): one non-load-bearing paragraph citing Konek and Campbell-Moore, *Coherence, dominance, and generalized loss* (manuscript, 2026); "the proofs in the present paper are self-contained".
15. **A–B Thm 6.30** kept, with LaTeX comment `% theorem number to be checked against the printed edition`.

## New text not yet refereed
- **Related-work paragraph** (§1, "Accuracy for imprecise credences"), including the one-sentence summary of SSK 2012: "under natural conditions, no real-valued scoring rule for imprecise forecasts is strictly proper". **The author should confirm this summary against SSK's exact theorem.**
- §2.3 paragraph on the second role of (M2) (RA68b's example, checked by RA68b by hand; my write-up not re-refereed).
- §8 sentence that veto–Brier ties distinct models (Lyapunov halving; RA68b's observation, write-up mine).
- §8 same-domain comparison sentence (RA68b's suggestion; it combines Cor 7.1(d) and Prop C.1(a),(b)).
- Remark 4.4 incoherence proof for X = D_Δ ∪ B′ (REF67_out U2 / RA68a / RA68b checked the instance; this proof text is mine).
- Prop 6.3 sharpening sentence (RA68a's observation).
- Thm 6.8(c) and its one-line proof; sentence after Thm 6.8 on what is lost without (M3) (RA68b's suggestion).
- Lemma 2.3(b) split (sandwich without (M2)): read off the existing proof, Steps 1–4.

## Citations added — flags
- Seidenfeld, Schervish, Kadane, IJAR 53:1248–1261 (2012): confident.
- Pettigrew, *Accuracy and the Laws of Credence*, OUP 2016: confident.
- Schoenfield, Noûs 51:667–685 (2017): fairly confident; check pages.
- Mayo-Wilson and Wheeler, PPR 93:55–78 (2016): fairly confident; check pages.
- Berger and Das, Noûs 54:666–703 (2020): **check volume and pages**.
- Konek, "Epistemic conservativity and imprecise credence", PPR 2019: **volume and pages omitted; author to supply**.
- Companion: title as given by the lead ("Coherence, dominance, and generalized loss"); must match WL68's final title.

---

# Revision 3 (RA68b second round, D1–D5; lead's instructions)

Compile: pdflatex ×3, clean (no warnings, undefined references, overfull or underfull boxes). **Length: 26 pages.**

1. **Same-domain sentence (§8, D1):** now "every full-dimensional credal set K′ (one with nonempty interior relative to aff Δ) with p ∈ relint K′". Change item 7 of Revision 2 corrected to match.
2. **Konek reference (D2):** "Philosophy and Phenomenological Research, forthcoming", with no year, volume or pages; LaTeX comment `% year, volume, pages to be supplied by the author`.
3. **SSK summary (D3):** "no continuous real-valued scoring rule for imprecise forecasts is strictly proper, relative to decision rules that reduce to expected-utility maximisation for precise credences, although strictly proper lexicographic scores exist."
4. **Tie sentence (§8, D4):** added that Σ p_i b_i(Y) = −∫_Y p·h dμ < 0, so z(Y) ≠ 0 and z(T) = z(Y∖T) = z(Y)/2 ≠ 0; both sets are non-null, hence distinct models.
5. **(M2) example (§2.3, D5):** now says D = D_Q also holds up to null sets of the Gaussian part γ, and Lemma 2.3(a) is applied with μ replaced by γ, which satisfies (M3).
6. **Companion title** capitalised exactly: "Coherence, Dominance, and Generalized Loss".

New text not yet refereed: only the wording of items 3–5 above, each following RA68b's recommended text.
