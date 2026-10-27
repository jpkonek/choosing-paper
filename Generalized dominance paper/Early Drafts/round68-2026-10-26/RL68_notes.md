# RL68: referee report on the definitive LDG manuscript

**Manuscript.** *Coherence, Dominance, and Generalized Loss*, file `Loss dominance generalized (definitive).tex` (22 pp.), read with `WL68_changes.md`.
**Date.** 26 October 2026.
**Referee.** RL68, independent.

**Method.**
- I read the manuscript from start to finish and re-derived every proof from the manuscript itself. I did not work from the source notes.
- I compared the hypotheses with v3.3 and with REF67_ldgo wherever the text was compressed.
- I recompiled the paper three times in `rl68_build/`.
- Scripts are in `rl68_py/`:
  - `checks.py` gives ALL PASS (output in `checks.out`);
  - `count71.py` is a coverage count for the Proposition 7.1 test.

**Labels.**
- PROVED: re-derived line by line here.
- CHECKED: exhaustive or numerical check in `rl68_py/` as well.

## Overall verdict

**The mathematics is correct.** I found no ERROR in any theorem, proposition, lemma or example. Every item that the changes file lists as new or not re-refereed is CORRECT. This includes:
- Proposition 7.1, which was PROVED and also CHECKED exhaustively on 40,000 random finite instances with a coarse change map (7,260 of them satisfy both hypotheses);
- the direct proof of Theorem 4.2;
- Example 4.4 and its claim that only compactness fails;
- the proof of Remark 3.7;
- Proposition 6.3(b);
- the verification in Example 6.4;
- the event-forecast paragraph;
- the randomisation lines.

**Compilation.** The paper compiles cleanly: no warnings, no undefined references, and no overfull or underfull boxes.

**Conventions.**
- No jargon and no old labels.
- No names on theorem-like environments.
- No commentary on earlier drafts.
- Standard dominance nomenclature.

**Structure.** The paper follows the three questions: §3 answers Q1, §§4–6 answer Q2, and §7 answers Q3. §7 states explicitly that the construction does not pass through Bayes choices or compact families.

**Required changes.** They concern **accuracy of framing in §7 and the abstract** and some small precision points. They are not about correctness. The most important is that §7 does not say that the content of Proposition 7.1 depends on how changes are individuated. It also states the companion's result without the companion's standing assumptions.

---

## 1. Verdicts, result by result

| Item | Verdict | Notes / repair |
|---|---|---|
| Lemma 2.1 | CORRECT (PROVED) | — |
| **Lemma 2.2** (rescaling; lsc transfer, G) | CORRECT (PROVED), with two minor GAPs | (i) The transfer holds only **from L to L′**. The converse fails: take D = [0,1)∪[2,3], with f(t) = t on [0,1) and f(t) = t−1 on [2,3]. This f is continuous and strictly increasing, and f∘h is continuous while h is not lsc (CHECKED). Write "transfers from L to L′". (ii) The proof establishes "segment = D∩[0,b]" only after "If b∈D". Add: "if b∉D, the segment is D∩[0,b) = D∩[0,b]". (iii) **The lsc clause is used nowhere.** Ex 5.5 transfers only ranking-level hypotheses, and its "Thm 4.2 does not apply" argument works directly with the rescaled loss. The changes file is therefore wrong to say that the clause is used in Ex 5.5. Either delete the clause or keep it with the direction stated. |
| Lemma 2.3 | CORRECT (PROVED) | Includes the case π·L(c) = ∞. |
| Prop 3.1 | CORRECT (PROVED) | — |
| Ex 3.2 | CORRECT (PROVED) | — |
| Prop 3.3 | CORRECT (PROVED) | Uses transitivity only. |
| Ex 3.4 | CORRECT (PROVED) | — |
| Cor 3.5 | CORRECT (PROVED) | Never cited later (see §7 of this report). |
| Prop 3.6 | CORRECT (PROVED) | Wording: the last sentence nests "if every ranking satisfies closure under ties …" inside "With coherent admissibility". The proof needs coherent admissibility for "exactly the coherent ones". Make that explicit (see R2). |
| **Remark 3.7** (proof U) | CORRECT (PROVED) | Each step checked: U_L = M_L∩[C_L] by Prop 3.3. Both closure cases are covered: M_L closed under ∼ needs symmetry of ∼; C closed under ∼ gives [C] = C = ⋃C_L. Under reflexivity of preorder rankings, the case "∼ = equality ⇒ closure under ties" holds. The remark is never cited (§7). |
| Lemma 4.1 (KKM form) | CORRECT (PROVED) | The fixed-point map sends Δ_F to Δ_F, and d_ω is continuous because A_ω is compact and nonempty. |
| Fig. 1 | CORRECT | — |
| **Thm 4.2, direct proof (G)** | CORRECT (PROVED) | (a) A_ω is closed: it is all of Δ if L(m,ω) = ∞, and an lsc sublevel set otherwise. (b) Coverage follows from (i) and Lemma 2.3, with S = supp p ⊇ supp π. (c) KKM gives the dominator. (d) The final clause: a model tied in profile with some c ∈ C_L is undominated, so the added hypothesis is exactly closure under ties, and Prop 3.1(a) applies. The proof uses exactly the stated hypotheses. |
| Paragraph after Thm 4.2 | CORRECT | Minor: "Section 8.3 needs this freedom". Section 8.3 uses Thm 4.3; the witness on finite worlds is Ex 8.5. Cite Ex 8.5. |
| Fig. 2 | CORRECT | The caption is consistent. I reconstructed a score of the stated shape: s(1,x) = (1−x)² + ½·1{x<½} + ¼·1{x=½} and s(0,x) = x² + ½·1{x>½} + ¼·1{x=½}. It is strictly proper and reproduces L(m) = (1.15, 0.95), the three profile limits, the boxed corner and the non-closed set at world 2. However, **the paper never states SSK's score**, so readers cannot check the caption's numbers without SSK09 (R6). There are also layout collisions (R7). |
| Thm 4.3 | CORRECT (PROVED) | T_F and A_ω are closed. The finite intersection property holds via a linked G ⊇ ⋃F_i. Compactness is used without Hausdorff. |
| Finite-Ω reduction of Thm 4.3 to Thm 4.2 | CORRECT (PROVED) | Holds in both directions. |
| **Ex 4.4** ("only compactness fails", G) | CORRECT (PROVED; CHECKED, truncated) | The e_n are pairwise incomparable and C_L = {e_n}. Since L(e_n, n+1) = n+2 > 1, x is undominated. No two distinct models are tied. With Θ = ℕ discrete, (i) holds trivially. σ_F ≡ max F is constant, hence continuous. e_{max F} has loss 0 on F, so it is a Bayes model for every prior on F; in particular it is Bayes for p itself. The only failing hypothesis is compactness of ℕ. The bounded variant 3 − 1/n works (CHECKED). |
| Thm 5.1 | CORRECT (PROVED) | — |
| Cor 5.2 | CORRECT (PROVED) | — |
| Ex 5.3 | CORRECT (PROVED) | Holds whether or not a ⪯ a. |
| Ex 5.4 | CORRECT (PROVED; CHECKED, grid of 25 values of t) | Checked: reflexivity; the intransitivity witness; C_L; strict dominance of each x_q; every guarantee set; coverage, including the vertex cases; the open-fibre argument; and that c₀ and c₁ are the only models at least as good as every model at the respective worlds. |
| Ex 5.5, main part | CORRECT (PROVED; CHECKED) | The profile formula, the transfer of the Cor 5.2 hypotheses through Lemma 2.2 (ranking level), strict concavity on the arc, and the connectedness contradiction. |
| **Ex 5.5, randomisation lines (U)** | CORRECT (PROVED; CHECKED) | The arc is x² + y² = a², with x + y ≥ a and equality only at the endpoints. Incoherent profiles lie strictly above. The hull lies on or above the line x + y = a. The projection z − ((z₁+z₂−a)/2)(1,1) lies on the segment, because coordinates lie in [0,a] and a⁴ = 2 bounds the quadratic losses. No original profile lies at or below (a/2, a/2). |
| Thm 5.6 | CORRECT (PROVED) | — |
| Continuous special case; Thm 4.3 as a case; finite equivalence with Thm 5.1 | CORRECT (PROVED) | In the converse direction, it is implicit that A^Ω_ω(m) ≔ A_ω(m). Say so in three words. |
| Rem 5.7 | CORRECT (PROVED) | The cofinite topology is compact and singletons are closed. The Hausdorff variant via the one-point compactification is correct, and also correct when C_L is finite. |
| Rem 5.8 | CORRECT (PROVED) | — |
| "Guarantees on a finite set G" paragraph | CORRECT (PROVED) | Both non-inclusions are witnessed. Restricting to the face Δ_G preserves closedness, the guarantee and coverage. The Ex 4.4 instance is correct. |
| Rem 5.9 | CORRECT (PROVED) | The K-sets on copies are closed and give the guarantees. Continuous coverage holds in every case, including linked F with copies of one world only. The open-fibre and compactness contradiction uses only that the family contains a weak dominator of every c_t. The qualifier "that meets the hypotheses of Theorem 5.6" is present. |
| Thm 6.1 | CORRECT (PROVED) | Uses π·x with x ∈ (−∞,∞]. This is a finite sum, so it is well defined, but the notation was introduced only for [0,∞] values. Add "(defined in the same way)". |
| Uniform-dominance sentence after Thm 6.1 | CORRECT (PROVED) | — |
| Cor 6.2 | CORRECT (PROVED) | Attainment is via nested closed sublevel sets. |
| Prop 6.3 (⇔ and margin) | CORRECT (PROVED) | The g_n are lsc and increasing, with a positive limit or +∞, and compactness of Δ gives an empty {g_N ≤ 0}. The resulting c_p has finite losses with margin 1/N. |
| Prop 6.3(a) | CORRECT (PROVED) | — |
| **Prop 6.3(b) (U)** | CORRECT (PROVED) | (a) For interior q, V(q) < ∞ forces L(c_q) to be finite, so π ↦ π·L(c_q) is continuous. (b) p·L(c_q) → p·L(c_p) = V(p), because the losses are finite on supp p and continuous. (c) Choosing q within ε/2 then gives usc at p. |
| **Ex 6.4, verification (U)** | CORRECT (PROVED; CHECKED on a grid) | Checked: the Bayes models and V(p) = p₁p₂ + 1 − p₂ log p₂ (the p₁(1+p₂) + p₂² = 1 simplification); lsc of g₀ and g₁; L(m) = (¼, ∞); that m is Bayes for no prior; that (1,0) dominates m; that m has no strict dominator; and the failure of usc (V → 1 while V(δ₁) = 0). |
| **Prop 7.1 (U)** | CORRECT (PROVED; CHECKED, `checks.py`) | (a) Reflexivity, monotone scores, and no ties or cycles. (b) The change from c to a weak dominator is available to c, so it is accepted only as guidance, and protection gives m = c. (c)(i)⇒(ii): availability does not depend on the world. (c)(ii)⇒(i): strictness via (a), and membership in C_L via (b). Closure under ties holds. The stated hypotheses are exactly those used: protection for (b), both conditions for (c). The exhaustive test also confirms that "acyclic" fails without the first condition (2-cycles occur), which bears on R1(a). **Framing GAPs in the surrounding text: see R1.** |
| Prop 8.1 | CORRECT (PROVED) | V finite is now conditional on an incoherent model existing. Minor: the sentence on Pettigrew should say in one clause how his credence functions on subsets of Ω correspond to Δ, and that the convention 0·∞ = 0 is used. Otherwise "contains" is asserted without the translation that v3.3 gave. |
| **Event-forecast paragraph (U)** | CORRECT (PROVED) | (a) The reduction to τ(Ω) is valid: profiles, and all four dominance notions, agree. (b) As p ranges over Δ_{τ(Ω)}, the vectors c_p are exactly the coherent forecasts. (c) The expected loss is Σ_i G_{p(E_i)}(f_i). (d) Strict propriety gives finite unique minimisers, so V is finite, c_p is the unique Bayes model, and closure under ties holds. (e) Continuity of the [0,∞]-valued s gives continuous losses. (f) Thm 4.2 and Prop 6.3(b) then give uniform dominance. (g) The proper case: the normalisation and finiteness give V < ∞. SSK09 Lemma 5 is cited for the profile equality; I confirmed it independently via the supporting-line argument for the concave function t ↦ G_t(t) plus continuity. GAP (minor): "strictly proper" and "proper" for s are used but never defined. Add one clause each: "G_t has unique minimiser t" and "t minimises G_t". |
| Thm 8.2 | CORRECT (PROVED) | The mixture inequality is valid even when E_q L(q_n,·) might be infinite, since the first inequality forces it to be finite. D is lsc minus a finite usc function, so it is lsc, and it attains a positive minimum. |
| Lemma 8.3 | CORRECT (PROVED; CHECKED on random instances) | — |
| Prop 8.4 | CORRECT (PROVED) | The step order is correct (C_L = C first). Prop 3.3 suffices for the unique-minimiser clause, because closure was shown in step 1. |
| Ex 8.5 | CORRECT (PROVED; CHECKED) | — |
| Prop 8.6 | CORRECT (PROVED; identity CHECKED) | The step order has been fixed. |
| Prop 8.7 | CORRECT (PROVED; CHECKED) | Checked: the softmax bounds 1/7 < s_i < 3/5, the derivative bounds, 4ε < 8/175 and 2ε < 4/245, L₁(x*) < 49/144 + 1/250 < 9/25, max(L₁, L₂) > 9/25 on a 1/300 grid of Δ, and truth-directedness on 20,000 random moves. |
| Sentence on Joyce's Lemma 1* | CORRECT | b³ = (½,½,0) has s₁ = s₂ < 2/5 by symmetry, so both inequalities are reversed. |

## 2. Hypotheses, and dependence on deleted material

- **The proofs use exactly the stated hypotheses.** I checked every compressed or restated item: Cor 3.5 (transitivity only), Prop 3.6, Thm 4.2, Thm 4.3, Prop 6.3 (which states the Θ = Δ identification), Prop 7.1, Prop 8.1, and Prop 8.4 (whose hypotheses were renamed). The only mismatches are of scope, not of logic:
  - Lemma 2.2's lsc clause is unused (R3).
  - Abstract and Prop 3.6: the permissibility claims need coherent admissibility (R2).
- **No proof depends on material deleted from v3.3.** Every internal reference resolves to a result in the manuscript. External dependencies:
  - SSK09 Ex 1, Ex 2, Ex 4 and Lemma 5;
  - SSSK Thm 1;
  - Nielsen Prop 1 and Lemmas 1 and 3;
  - SSK14 Thm 2.

  Of these, only Fig. 2(b) leaves the reader unable to verify a claim without the cited paper (R6).
- The changes file says that "the lsc transfer is used in Ex 5.5". That is inaccurate (R3).

## 3. Structure

- **The three questions are reflected in the organisation:** §3 (Q1), §§4–6 (Q2), §7 (Q3). The introduction announces them, and §7 says that Prop 7.1 "answers the third question directly. It does not pass through Bayes choices or compact families, and nothing requires a ranking built in this way to meet their hypotheses." This satisfies AUDIT point 2. The history of (S) is not retold.
- **§7 states the achievement and the limitation together**, as AUDIT point 3 requires. On what the construction achieves and leaves open, however, §7 is **incomplete in three places** (R1):
  1. "The ranking is acyclic, but in general it is not transitive". Acyclicity needs the first condition ("guided changes improve the score"); without it, 2-cycles occur (CHECKED).
  2. Nothing is said about how changes are individuated. The proposition allows any assignment of changes to ordered pairs. If every ordered pair is its own change (the finest individuation), then "available to no coherent model" just means "made from an incoherent model". Coherent models are then protected by fiat, and (c)(ii) reduces to plain score improvement at every world. v3.3's Remark 3.14 made exactly this point. Without it, the sentence "Its substantive mathematics is the existence of the improvements in (c)(ii)" overstates the general proposition. The content comes from a coarse individuation, as in the companion: a change is what is added and what is removed, so comparisons depend only on the change, and "available" is a genuine restriction.
  3. The companion's result is described as holding "on an arbitrary set of worlds", in both the introduction and §7, without the companion's own standing qualifications. The companion's abstract states them prominently:
     - a separable space of gambles containing the constants;
     - a measure on gambles (full support in the headline);
     - models identified up to null sets.

     AUDIT requires these qualifications in statements and introductions, so the description of the companion should not drop them.

## 4. Scope and open questions

§9 is accurate:
- "One ranking at a time";
- the sufficiency of the conditions, with Remarks 5.7 and 5.8;
- the corrected statement of "what depends only on the ranking", which names completeness via Lemma 2.3 and numerical values for §6;
- the Zorn sentence, including "then shows that undominated models are coherent".

Both open questions are genuine. Not stating the application paper's "not this round" items in LDG is acceptable, since they concern the application.

## 5. Cross-paper dependence

- **No circularity.**
  - LDG uses the companion (`Coherence and accuracy for sets of desirable gambles.tex`, current folder version) only for illustration and attribution: the 2-D intransitivity example, the repair theorem, and the Zorn method.
  - The companion does **not cite LDG at all**: its bibliography has no LDG entry, and it proves its own protection result (Prop "protect", which goes through a countable Ω₀) and its own strict-dominance characterisation.
  - Prop 7.1 is proved in LDG.
- **Consistency.**
  - The companion's ranking matches Prop 7.1's construction.
  - "Could make", "available", "guided" and "not transitive" (alongside "intransitive") agree.
  - The companion's example on ℝ² (two worlds) matches LDG's description.
  - The companion's veto–Brier appendix carries the Zorn step (Step 4 of the proof of Thm vb), so LDG's §9 attribution is supported.
  - The companion's "uniformly dominates" (strict, with inf of score gain > 0) is the score-side analogue of LDG's loss definition. This is consistent.
- **One inconsistency of emphasis:** the missing qualifiers (R1(c)).

## 6. Conventions

- **Jargon and labels.** No "certificate", "record", "safe", "route", "gate" or "realiser", and no labels (S), (B), (GI) and so on. I grepped the PDF text.
- **Theorem-like environments.** None carries a name.
- **Earlier drafts.** No commentary on them.
- **Dominance nomenclature.** Standard. The footnote mapping to SSK and Joyce is helpful.
- **The word "models".** Used throughout, with "credence" and "forecast" only inside applications.
- **\coloneqq.** It is used for most definitions, but the example set-ups are inconsistent. Ex 4.4, Ex 5.4 and Prop 8.6 use "≔", while the following use "=" for definitions:
  - Ex 3.2, Ex 3.4, Ex 5.3 (M_L = …, C = …);
  - Ex 5.5 (M_L, C, L₁, L₂);
  - Ex 6.4 (Ω, M_L, C);
  - Ex 8.5 (Ω, E_j, M_L, L_i);
  - §8.5 (Ω, M_L, C);
  - Prop 8.7 (N = 3).

  This is minor (R8).
- **Compilation.** Clean, 22 pages.

## 7. Clarity and length

**Inessential or unused** (optional cuts, about ⅔ page in total):
- Lemma 2.2's lsc clause (R3).
- Cor 3.5: never cited, and its only role is noted in the §3.2 preamble. Keep it only if the authors want the strict-dominance transfer for preorders.
- Remark 3.7: never cited. The companion defines models as null-set classes and does not use it. Keep it as a short remark or cut it.
- Remark 5.9's copied-worlds construction: its last sentence already says that the argument works with two worlds. The copies add only that the phenomenon persists on infinite Ω. That could be one sentence instead of eight lines.
- The parenthetical on "undominated on G versus on Ω" in the guarantees paragraph.

**Essential but missing:**
- The individuation point in §7 (R1(b)).
- The companion's qualifiers (R1(c)).
- The SSK Example 4 score, one line, for Fig. 2(b) (R6).
- Definitions of "proper" and "strictly proper" for event scores (R5).

**Optional addition.** A self-contained five-line illustration of Prop 7.1 would let readers see a coarse change structure without the companion. v3.3's eight-model set-valued example is refereed and would serve.

**Figure 2 layout (R7).**
- Panel (a)'s x-axis label "L(·,1)" runs into panel (b)'s vertical axis.
- "weakly dominates m" sits on the dashed line and the curve.
- In (b), the label "(1,1)" is struck through by the dotted line.

Increasing (b)'s xshift by about 0.5 cm and nudging the two labels fixes all three.

---

## 8. Ranked list of required changes

1. **§7 framing (accuracy of what the construction achieves).**
   - (a) Replace "The ranking is acyclic" with "When guided changes improve the score, the ranking is acyclic (Proposition 7.1(a))".
   - (b) Add two sentences on individuation. Suggested text: *"The proposition places no constraint on how changes are individuated. If every ordered pair of models is its own change, a change is available to a coherent model exactly when it starts from one; coherent models are then protected by definition, and (c)(ii) asks only for a coherent model with a better score at every world. The construction has content when changes are individuated coarsely, so that one change is available to many models — in the companion paper, by the gambles added and removed — and the comparison of two models at a world depends only on the change between them."* Adjust "Its substantive mathematics is …" accordingly.
   - (c) In the introduction (¶ "How can suitable rankings be constructed?") and in §7, state the companion's result with its standing assumptions: "for a separable space of gambles containing the constants, a suitable measure on gambles, and models identified up to null sets". Also write "a coherent replacement reached by a change that no coherent model could make, which raises the score at every world by a uniform margin". Avoid "an improvement … available to no coherent model".
2. **Permissibility wording.**
   - Abstract: "…and, if every coherent model is undominated under some ranking, the rationally permissible models are exactly the coherent ones".
   - Prop 3.6, last sentence: "With coherent admissibility, every coherent model is permissible; if in addition every ranking satisfies closure under ties, the permissible models are exactly the coherent ones."
3. **Lemma 2.2.** Either delete the unused lsc clause, or state that it transfers from L to L′ (the converse fails) and add the b ∉ D case to the proof. Correct the changes file, which says the clause is used in Ex 5.5.
4. **Thm 6.1.** Say that π·x is defined as before for x with values in (−∞,∞]. In the finite equivalence after Thm 5.6, add "A^Ω_ω(m) ≔ A_ω(m)".
5. **Event forecasts.** Define "strictly proper" (each G_t has the unique minimiser t) and "proper" (t minimises G_t) for s and s_i.
6. **Fig. 2(b) self-containment.** State SSK09 Example 4's score in one line in the caption or text. A score of the form above reproduces every number in the caption, but the authors should quote SSK's own. Add one clause to the Pettigrew sentence on the correspondence of credence functions on subsets with Δ, and on 0·∞ = 0.
7. **Fig. 2 layout.** Fix the three label collisions.
8. **Small items.**
   - Use \coloneqq consistently in the example set-ups listed in §6.
   - After Thm 4.2, cite Ex 8.5 for "needs this freedom".
   - In the introduction, qualify "Neither ingredient mentions dominance" with: apart from the requirement that assigned models be undominated, which is the other half of the argument.

**Recommended, not required.** Make the optional cuts in §7 (Cor 3.5 and Remark 3.7 if they are not wanted; compress Remark 5.9's copies; drop the parenthetical). Optionally, add v3.3's eight-model example as a short illustration of Prop 7.1.

**Bottom line.** After R1–R3, which are text-level, the manuscript is ready. No mathematical repair is needed.

---

## Second round: check of Revision 2 (26 October 2026)

**What I checked.**
- I re-read the revised `Loss dominance generalized (definitive).tex` in full.
- I recompiled it three times (`rl68_build/ldg2.*`). The compile is clean: no warnings, no undefined references, no overfull or underfull boxes. It is 22 pages.
- I grepped the PDF text and rendered Figure 2 at 150 dpi.

**Verdict.** Every required change R1–R8 has been made, and made correctly. No new mathematical issue arises. One sentence in the new §7 paragraph needs a precision fix (S1 below). The fault is in the wording I suggested, which the authors adopted.

### Required changes R1–R8
| # | Status | Notes |
|---|---|---|
| R1(a) acyclicity | DONE, correct | "When guided changes improve the score, the ranking is acyclic (Proposition 7.1(a))". |
| R1(b) individuation | DONE; one precision fix needed (S1) | The paragraph is accurate except for one clause. |
| R1(c) companion assumptions | DONE, correct | Stated in both §1 and §7. I checked them against the companion. "Finite-moment" is its (M1), and "null-boundary" is its (M2). Full support (M3) is correctly not listed, because the companion says only (M1) and (M2) are needed for the repair theorem. The wording "through a change that no coherent model could make and that raises the score at every world by a uniform margin" is accurate. |
| R2 permissibility | DONE, correct | Abstract, §1, and the last sentence of Prop 3.5. |
| R3 Lemma 2.2 | DONE | The lsc clause is deleted. The remaining one-line proof is complete. |
| R4 | DONE | Thm 6.1 now says "π·x defined as for losses". The finite equivalence after Thm 5.6 now includes A^Ω_ω(m) ≔ A_ω(m). |
| R5 | DONE, correct | "Proper" and "strictly proper" are defined through G_t. The s_i are proper "in the same sense". The finiteness argument is unchanged and still valid. |
| R6 | DONE, correct | The Pettigrew sentence now gives the correspondence with Δ and the 0·∞ = 0 convention. The Fig. 2(b) score is checked below. |
| R7 | DONE | Panel (b) is shifted, the labels are moved, and nothing collides with an axis. One cosmetic residue remains: the dashed vertical line through L(m) still crosses the second "1" of the "(1,1)" label. Moving that label to `above left` fixes it. Optional. |
| R8 | DONE | \coloneqq is now used in every example set-up I listed, including the L_i of Ex 8.5, §8.5 and N ≔ 3. Ex 8.5 is cited for "this freedom is needed". The "neither ingredient mentions dominance" qualifier appears in §1 and §9. |

### The new §7 text
- **Acyclicity condition.** Correct.
- **Individuation paragraph.** Correct, apart from S1.
  - "available to a coherent model exactly when it starts from one" is correct for the finest individuation.
  - "(c)(ii) asks only for a coherent model with a better score at every world" is correct. A guided non-null change raises the score under (a)'s hypothesis, and an unguided change from an incoherent model is then always unavailable.
  - **S1 (required, one clause).** The clause "coherent models are then protected by definition" is not specific to the finest individuation. In every individuation, the change from a coherent c is available to c, so c can be weakly dominated only through changes guided at every world (this is the proof of Prop 7.1(b)). The clause can also be misread as saying that the protection hypothesis of (b) holds automatically, which is false: a change from c could be guided at every world. What is specific to the finest case is that **every score improvement of an incoherent model is accepted**. Suggested replacement for the sentence: *"If every ordered pair of distinct models is its own change, a change is available to a coherent model exactly when it starts from one; every score improvement of an incoherent model is then accepted, and (c)(ii) asks only for a coherent model with a better score at every world."*
- **Companion's assumptions.** Correct (see R1(c)).
- **Listed ranking requirements.** Correct. The four listed properties are delivered by Prop 7.1(a)–(c) together with the companion's repair theorem: every guided comparison accepted, comparisons between distinct models accepted only when they raise the score, closure under ties, and exactly the coherent models undominated.
- **Maximality statement.** Correct. It matches the companion's Prop "maximal". I re-verified it:
  - Let R satisfy the three properties, and let x R y with x ≠ y. Then the score strictly rises. If the change is available to a coherent model, the third property makes it guided; otherwise it is unavailable and improving. Either way it is accepted by the ranking.
  - Conversely, the ranking satisfies all three properties. The second holds because guided non-null changes raise the score, which the companion proves.
  - Comparisons of a model with itself are covered by the null change.
- **Caveat on the third condition.** Correct. It is stated at the end of §7 and repeated as an open question in §9, consistent with BRIEF68's addition (point 5).
- **Placement of the dominance conclusion.** "The dominance conclusion itself comes from Proposition 7.1(c), not from Section 5" is accurate.

### The renamed condition: "every prior is served at a world it charges"
- **Named form.** Used in Thm 5.1(ii) and Thm 5.6 2(b).
- **Short form, "the serving condition".** Used in the proof of Cor 5.2, the sentence before Ex 5.3, Ex 5.4, Rem 5.8 and the finite-G paragraph. The paragraph after Thm 5.6 uses the full phrase.
- **No stray "coverage".** The PDF contains none. The remaining "cover" and "covered" are ordinary topology (open covers, Fig. 1, Ex 5.5, Rem 5.9).
- **Minor, optional.** "The serving condition" is first used in the proof of Cor 5.2 without being introduced. Add "(the serving condition)" after the name in Thm 5.1(ii).
- **No change needed.** "Serve against every rival" (§1, after Thm 5.1, Rem 5.7) is related but distinct usage, and it reads naturally.

### Fig. 2(b)
The caption now states s(1,x) = (1−x)² + ½·1{x<½} + ¼·1{x=½} and s(0,x) = x² + ½·1{x>½} + ¼·1{x=½}, with loss s(1,f_i) + s(0,f_j) at world i, where j ≠ i. This is exactly my reconstruction, and the world/event pairing is correct. I re-verified each claim:
- m = (0.6, 0.7) has profile (0.16 + 0.49 + ½, 0.09 + 0.36 + ½) = (1.15, 0.95).
- For p₁ > ½, the profile is (2p₂², 1 + 2p₁²), which tends to (0.5, 1.5). At (½,½) it is (1,1). For p₁ < ½ it is (1 + 2p₂², 2p₁²), which tends to (1.5, 0.5).
- The score is strictly proper. For t > ½, every y ≠ t has strictly larger Brier part, and its penalty is t/2, ¼ or (1−t)/2, each at least (1−t)/2. The case t < ½ is symmetric, and at t = ½ the penalty is constant.
- No coherent model weakly dominates m. The world-2 losses are at least 1 on one side and at the centre, and the world-1 losses exceed 1.5 on the other side.
- The set at world 2 contains every p with p₁ < ½ (loss < 0.5) but not (½,½) (loss 1 > 0.95).
- The boxed corner (0.5, 0.5) is the liminf of the profiles.
- The drawn curves match these formulas, including L(c_{δ₁}) = (0,3).
- Calling it a score "of the kind in Example 4 of SSK09" is appropriately hedged.

### Other Revision 2 changes
- **Deletions.** Cor 3.5 and Rem 3.7 are gone, and nothing references them. Renumbering is consistent: Prop 3.5 is permissibility.
- **§3 wording.** "Only one of these consequences uses transitivity" and "Transitivity enters only through the following result" are accurate. Prop 3.5(c) uses transitivity only through Prop 3.3.
- **Rem 5.9.** It is now argued on Ex 5.4 directly. Thm 5.6 applies there by the finite equivalence, and the open-fibre and compactness argument is unchanged and correct. The one-sentence copied-worlds claim was checked in round 1.
- **"Tied at ω".** Now defined in §2. Its use in Prop 7.1(a) is now formally covered.
- **Ex 5.4.** Its numbers are now called "losses", but the relation is not the loss ranking because of the exceptions. The text says this explicitly ("accept every comparison … except"), so it is fine.

### Remaining actions
1. **S1 (required).** Replace the clause "coherent models are then protected by definition" as above.
2. **Optional.** Add "(the serving condition)" in Thm 5.1(ii), and move the "(1,1)" label in Fig. 2(b).

With S1 made, I recommend the manuscript as final.
