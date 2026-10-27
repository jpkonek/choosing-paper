# WL68: changes file for the definitive LDG

26 October 2026. Role: WL68 (BRIEF68).

## Deliverables
- `Loss dominance generalized (definitive).tex` and `Loss dominance generalized (definitive).pdf`.
- **Title.** The title inside the paper is v3.3's title, *Coherence, Dominance, and Generalized Loss*. I kept it because it is the authors' own and describes the paper. The filename is the one the brief requested. If the author wants a new title, the obvious candidate is *Coherence and Dominance under General Rankings*.
- **Authors.** Jason Konek and Catrin Campbell-Moore, as in v3.3. The lead should flag this to the author.
- **Length.** 22 pages (11pt, A4, 27 mm margins), against 43 for v3.3. There is no appendix.
- **Compilation.** Clean under pdflatex, run three times. There are no warnings, no undefined references, and no overfull or underfull boxes.

## Organisation (binding: AUDIT_r68 LDG structure)
| § | Content | Which question |
|---|---|---|
| 1 | Introduction. It states the three questions and the headline results informally. | — |
| 2 | Setting: dominance notions, loss rankings, Bayes models, lsc. Lemmas 2.1–2.3. | — |
| 3 | What follows once coherent undominated replacements exist: Prop 3.1, transitivity results, permissibility. | Q1 |
| 4 | Bayes choices with lsc losses. These lead: Thm 4.2 (finite worlds), Thm 4.3 (any worlds). Main Example 4.4. | Q2 |
| 5 | The general theorems: Thm 5.1 (finite worlds, KKM) and Thm 5.6 (local theorem, infinite worlds). Remarks on where their content lies. | Q2 |
| 6 | Margins, Bayes models, strict dominance. | Q2 |
| 7 | Constructing rankings: Prop 7.1, plus a pointer to the companion paper. | Q3 |
| 8 | Applications: proper scores; probabilism on arbitrary domains; conditional reports; the countable example; the Joyce foil. | — |
| 9 | Scope and open questions. | — |

**How the brief's points are implemented.**
- The application is not forced through LDG's sufficient conditions. §7 says explicitly that Prop 7.1 answers Q3 directly, that it does not pass through Bayes choices or compact families, and that nothing requires such a ranking to meet their hypotheses.
- The history of (S) and of certificates is not retold. There are no labels, and no "certificate", "record", "safe", "route" or "gate". I checked this by grepping the PDF text.
- The abstract compactness condition appears only in Remark 5.7(ii). That remark shows the condition is equivalent to the conclusion, using the cofinite topology; a single sentence adds the Hausdorff variant.
- The main example is Example 4.4, the transitive loss ranking. I placed it immediately after Thm 4.3. In that position it shows that compactness cannot be dropped from the Bayes-choice theorem. §5.2 then reuses it to show that guarantees on finite sets of worlds do not suffice without a compact family linking them.
- §7 states the philosophical achievement and the limitation together, following AUDIT point 3. The construction shows that the ranking requirements are compatible with coherence and can single it out exactly. It does not, by itself, derive coherence from independently justified comparisons.

## Result map
Status key:
- **R** = refereed source, proof copied or reworded.
- **A** = assembled from refereed parts with no new argument.
- **G** = minimal glue written here.
- **U** = listed in LDGO67 as "not re-refereed".

| Paper | Outline | Source | Status |
|---|---|---|---|
| Lemma 2.1 (competitive vs strictly dominated) | 2.1 | v3.3 §1 | R |
| Lemma 2.2 (rescaling) | 2.2 | v3.3 Prop A.1 | R. Revision 2: the lsc-transfer clause is deleted, because nothing uses it. Ex 5.5 transfers only ranking-level hypotheses. The earlier claim that Ex 5.5 used the clause was wrong. |
| Lemma 2.3 (Bayes ⇒ competitive) | 2.3 | v3.3 Lemma A.2 | R |
| Prop 3.1 | 3.1 | v3.3 Prop 3.1 | R |
| Ex 3.2 | 3.2 | v3.3 Ex 3.2 | R |
| Prop 3.3 (preorder: undominated = tied with C_L) | 7.2 | v3.3 Prop 3.8 | R |
| Ex 3.4 | 7.3 | v3.3 Ex 3.9 | R |
| Cor 3.5 | 7.4 | v3.3 Cor 3.10, hypothesis restated | R (REF67_cc §4.2) |
| Prop 3.6 (permissibility) | 7.1 | v3.3 Prop 5.1 | R |
| Remark 3.7 (equivalence ∼) | 7.5 | v3.3 Prop 5.2 | **U** (proof copied; re-derived by me) |
| Lemma 4.1 (KKM), Fig 1 | 4.1 | v3.3 Lemma 3.3, Fig 1 | R |
| Thm 4.2 (finite worlds, Bayes choices, lsc) | 4.2 | v3.3 Cor 3.5 + Lemma A.2 | A (REF67_ldgo §1a). **Direct proof (G)**: inlines Cor 5.2 and Lemma 2.3 into one KKM argument. The content is identical to the outline's chain. |
| Fig 2 | Fig 2 | v3.3 Fig 2 | R; caption rewritten per REF67_ldgo rec. G ("no coherent model weakly dominates m") |
| Thm 4.3 (any worlds, compact family) | 5.1 | v3.3 Thm 3.6 / Cor 3.7 + Prop 2.4 + Lemma A.2 | A; the direct proof is v3.3's refereed one |
| Finite-Ω reduction of Thm 4.3 to Thm 4.2 | 5.1 | — | R (REF67_ldgo §1b: "holds in both directions") |
| **Ex 4.4 (main example)** | 5.6 | round 67 | R (REF67_ldgo §7a, PROVED and CHECKED). **G**: the sentence "every hypothesis of Thm 4.3 holds except compactness, with Θ = ℕ discrete, σ_F ≡ max F". This makes precise REF67_ldgo's statement that "the compact lsc family cannot be dropped". The bounded variant 3 − 1/n is from REF67_ldgo §7a. |
| Thm 5.1 (finite worlds, any ranking) | 4.3 | v3.3 Thm 3.4, restated | R |
| Cor 5.2 (closed competitive choice) | 4.4 | v3.3 Cor 3.5 / Prop 2.1 | R |
| Ex 5.3 | 4.5 | v3.3 Ex 2.3 | R |
| Ex 5.4 (two worlds, intransitive; Thm 5.1 applies, Cor 5.2 fails) | 4.7 | CC67 §2b; direct argument | R (REF67_cc §2; REF67_ldgo §7b CHECKED) |
| Ex 5.5 (rescaling; randomisation) | 4.6 | v3.3 Ex A.7, Prop A.8 | R; **the randomisation lines are U** (copied from A.8 and re-derived by me) |
| Thm 5.6 (local theorem) | 5.2 | CC67 §3.1 | R (REF67_cc §3; REF67_ldgo §2b) |
| Continuous special case; Thm 4.3 as a case; finite-Ω equivalence | 5.2 notes | CC67 §3.1–3.2 | R |
| Remark 5.7 (rival-dependent assignment; abstract compactness ⇔ conclusion; Hausdorff) | 5.3 + 5.4 merged | CC67 §1, §3.3 | R (REF67_cc §1; REF67_ldgo §4) |
| Remark 5.8 (vertex; hypotheses not implied by the conclusion) | 5.5 | REF67_cc §3 | R |
| Paragraph on "guarantees on a finite set G" (definition, two witnesses, implication from Thm 5.6, Ex 4.4 revisited) | definitional point | REF67_cc §3b | R (REF67_ldgo §4: both non-inclusions witnessed) |
| Remark 5.9 (closed comparison sets; Ex 5.4 with worlds copied) | 5.7 | R1 (REF67_cc §4.1), rewritten in the paper's own terms; CC67 §2 for the copies | R (REF67_ldgo §3; REF67_cc §2 checked the copies form). The qualifier "that meets the hypotheses of Thm 5.6" is included, per REF67_ldgo required change 2. |
| Thm 6.1 (margins) | 6.1 | v3.3 Thm A.4, with the compactness step written out | R |
| Cor 6.2 | 6.2 | v3.3 Cor A.3 | R; the attainment argument (nested closed sublevel sets) is written out, as REF67_ldgo §6 noted |
| Prop 6.3 (strict = Bayes for no prior; uniform) | 6.3 | v3.3 Cor A.5 + Prop A.9 | R; **the case (b) argument is U** (REF67_ldgo re-derived it) |
| Ex 6.4 (SSK09 Ex 2) | 6.4 | v3.3 Ex A.12 | R; **the verification paragraph is U** (CHECKED in REF67_ldgo misc.py) |
| **Prop 7.1 (constructing rankings)** | 9.1 | v3.3 Thm 3.13(a), (b), (d) and Rem 3.14, refereed by REF66_ldg | **U**: the compressed statement and proof are not re-refereed. I re-derived every step (see below). |
| Prop 8.1 (proper scores) | 8.1 | v3.3 §6.1 | R; "V finite" is made conditional on an incoherent model existing (REF67_ldgo change 7) |
| Event-forecast paragraph (Predd; SSK09 Thm 2, Concl. 3) | §8.1 | v3.3 §A.7 | **U**: rerouted through Thm 4.2 and Prop 6.3(b) on Δ_{τ(Ω)}. **G**: one clause saying that dominance relations agree on Ω and τ(Ω), and the explicit "no incoherent forecast is a Bayes model". |
| Thm 8.2 (probabilism, arbitrary Ω) | 8.2 | v3.3 Thm 6.1 | R. **G**: the zero credence function as the witness m′ ∉ C. |
| Lemma 8.3 | 8.3 | v3.3 Lemma 6.2 | R. The denominator is written as max(p(E_j), η), which is identical to v3.3's p(E_j) + max(η − p(E_j), 0). |
| Prop 8.4 (conditional reports) | 8.4 | v3.3 Prop 6.3 | R. Hypotheses renamed: block propriety; lsc along coherent systems. |
| Ex 8.5 | 8.5 | v3.3 Ex 6.4, condensed | R (CHECKED). Dropped: Lemma 8.3's explicit (u, v) formulas. |
| Prop 8.6 (countable example) | 8.6 | v3.3 Prop C.1 | R. The step order is fixed per REF67_ldgo: C_L = C first. |
| Prop 8.7 (Joyce foil) and the sentence locating the error | 9.2 | v3.3 Prop D.3; REF67_ldgo rec. D | R (CHECKED) |
| §9 Scope | Part 8 | — | Prose only. The wording "what depends only on the ranking" is restricted per REF67_ldgo change 5. |

## Unrefereed items (for the LDG manuscript referee)
Priority order:
1. **Prop 7.1, statement and proof** (outline item 1). I re-derived it:
   - (a) The null change is guided, so the relations are reflexive. An accepted non-null change raises the score on either branch.
   - (b) The change from c to a weak dominator is available to c, so it is accepted only as guidance. Protection then applies.
   - (c) (i) ⇒ (ii): whether a change is available does not depend on the world. (ii) ⇒ (i): strictness follows from (a), and (b) shows that every coherent model is undominated.

   The hypotheses are the ones REF67_ldgo §10 requires: protection for (b), both conditions for (c). **Terminology change:** the outline's "can be made to z" is now "available to z". The paper glosses it once as "no coherent model could make it", to match WA68's draft, which uses "could make" and "available".
2. ~~**Lemma 2.2, expanded proof of the lsc transfer (G).**~~ *Withdrawn in Revision 2: the clause and its proof are deleted.* v3.3 says only "a continuous increasing function of an lsc function is lsc". Since f_ω is defined only on a subset D of [0,∞], I added the argument: {t ∈ D : f_ω(t) ≤ a} = D ∩ [0,b], so {f_ω∘h ≤ a} = {h ≤ b}. The paper uses this only in Ex 5.5, where f(t) = t^{1/4} is defined on all of [0,∞].
3. **Thm 4.2, direct proof (G).** It is the outline's chain, Cor 4.4 + Lemma 2.3, written as one argument.
4. **Ex 4.4, "all hypotheses of Thm 4.3 except compactness" (G).** Θ = ℕ discrete; lsc trivial; σ_F constant, hence continuous; e_{max F} has loss 0 on F, hence is Bayes for every prior on F.
5. Remark 3.7's proof (U).
6. Prop 6.3 case (b) (U).
7. Ex 6.4 verification (U).
8. The event-forecast paragraph (U).
9. The randomisation lines in Ex 5.5 (U).

No other new mathematics was introduced. Prop 4.8 (v3.3 B.5–B.6, U) is **omitted**: it was optional, and it is the author's choice whether to add it. The reason for omitting it: Remark 5.8 already shows that the hypotheses are not implied by the conclusion, and including it would add 0.6 page of unrefereed text.

## Other editorial decisions (beyond the outline)
- **Remarks 5.3 and 5.4 merged into Remark 5.7.** The metrizable variant is dropped, since it adds only a cardinality bound. The Hausdorff variant is kept in one sentence.
- **The relational variant of Example 5.6 is omitted.** The loss version is the main example.
- **SSK09 Example 1** appears only as a cited fact: an incoherent forecast is tied with a coherent one, so closure under ties fails. The outline's further claim, that Cor 4.4 applies after rescaling by e^t, is **not made**. I could not re-verify it within this round, and nothing depends on it.
- **Cor 6.2:** the optional weaker-hypothesis clause is omitted.
- **Lexicographic / Zorn method** (§9): one attribution sentence pointing to the companion paper. No claim is proved or asserted in LDG beyond attribution.
- **Open questions in §9:**
  - strict dominance in Thm 8.2 without bounded losses (Nielsen §4.2.1);
  - Joyce's framework for credences summing to more than one.

  The brief's "not this round" items (nonseparable spaces, no order unit, domain classifications) concern the application and are not stated in LDG.
- **Bibliography.** Added: de Finetti (1974) and Wald (1950), for one framing sentence in the introduction, and the companion paper. Dropped: CPMNote. SSSK is kept for the randomisation lines.

## Cross-paper flags
1. **LDG cites the companion paper for three things only:**
   - the intransitivity example on two-dimensional gambles;
   - the repair theorem, with a uniform margin, on an arbitrary set of worlds;
   - the use of the Zorn-lemma method for one structured construction.

   No LDG proof depends on the companion, and Prop 7.1 is proved in LDG. **The lead should confirm that WA68's manuscript carries the Zorn-lemma admissibility argument in its veto–Brier appendix**, as BRIEF68 requires. The §9 sentence points there.
2. **Terminology is aligned with WA68's draft as I found it in the folder:**
   - "available to", "could make";
   - "guided";
   - "models";
   - "not transitive".

   The checker should confirm the final versions still agree.
3. **Circularity: none.** The companion may cite LDG §3 and Prop 7.1. LDG uses the companion only as an example and for attribution.

## Revision 2 (after RL68 and RX68)

**Compilation.** Clean after three runs: no warnings, no undefined references, no overfull or underfull boxes. **22 pages.**

**RL68 required changes 1–8.**
1. **§7.**
   - (a) "Acyclic" is now conditional: "When guided changes improve the score, the ranking is acyclic (Prop 7.1(a))".
   - (b) A new paragraph explains how changes are individuated. With the finest individuation, coherent models are protected by definition and (c)(ii) reduces to plain score improvement. The construction has content only when changes are individuated coarsely and comparisons depend only on the change. "Its substantive mathematics is …" is reworded to "Its substance then lies in …".
   - (c) The introduction and §7 now state the companion's standing assumptions: a separable space of gambles containing the constants, a suitable measure on gambles (§7 adds "finite-moment and null-boundary conditions"), and models identified up to null sets. The wording is now "a change that no coherent model could make and that raises the score at every world by a uniform margin".
2. **Permissibility.**
   - Abstract and §1: "if every coherent model is undominated under some ranking".
   - Prop 3.5 (formerly 3.6), last sentence: "With coherent admissibility, every coherent model is permissible; if in addition every ranking satisfies closure under ties, the permissible models are exactly the coherent ones."
3. **Lemma 2.2.** The lsc clause is deleted. The table row above is corrected.
4. **Thm 6.1 and the finite equivalence.**
   - Thm 6.1 now says "with π·x defined as for losses".
   - The finite equivalence after Thm 5.6 adds "A^Ω_ω(m) ≔ A_ω(m)".
5. **Event forecasts.** "Proper" (each G_t is minimised at t) and "strictly proper" (t is the unique minimiser) are now defined. The s_i are proper "in the same sense".
6. **Fig. 2(b) and Pettigrew.**
   - The caption now states a score explicitly: s(1,x) = (1−x)² + ½·1{x<½} + ¼·1{x=½} and s(0,x) = x² + ½·1{x>½} + ¼·1{x=½}, summed over the events {1} and {2}. This is RL68's reconstruction. I checked that it is strictly proper and reproduces every number in the caption: (1.15, 0.95), the three profile limits, the boxed corner, and the non-closed set.
   - **Flag:** the caption calls it "a discontinuous strictly proper score of the kind in Example 4 of SSK09". It does not claim this is SSK's own formula, because I could not check that formula. The author may substitute SSK's own.
   - The Pettigrew sentence now says how credence functions on subsets correspond to Δ, and that expected losses use 0·∞ = 0.
7. **Fig. 2 layout.** Panel (b) is shifted right by 0.55 cm. The "weakly dominates m" label is moved clear of the curve and the dashed lines. The "(1,1)" label is now above its point, and the "L(m)" label in (b) is below right. Checked visually at 200 dpi.
8. **Small items.**
   - \coloneqq is now used in every example set-up: Ex 3.2, 3.4, 5.3, 5.5 and 6.4, Ex 8.5 (including L_i), §8.5, and Prop 8.7.
   - After Thm 4.2, the text now cites Ex 8.5 for "this freedom is needed".
   - In §1, "neither ingredient mentions dominance" is qualified with "apart from the requirement that the assigned models be undominated, which is the other half of the argument". The same qualification is added in §9.

**RL68 optional cuts (as instructed).**
- Cor 3.5 (strict-dominance transfer) and Remark 3.7 (equivalence ∼) are deleted. Neither was cited. The §3.2 preamble now reads "Transitivity enters only through the following result", and §1 says "Only one of these consequences uses transitivity".
- Remark 5.9 is now argued on the two-world Ex 5.4 itself, since Thm 5.6 applies there through the finite equivalence. The copied-worlds construction is reduced to one sentence.
- The parenthetical "undominated on G vs on Ω" is dropped.
- The eight-model example is **not** added.

**RX68 LDG items.**
- **R-L1.**
  - §7: "So, of the consequences in Section 3, those that use no order properties apply; the dominance conclusion itself comes from Proposition 7.1(c), not from Section 5."
  - §9: "In every application of Section 8 …".
- **R-L3.** "Coverage" in Thm 5.1(ii) and Thm 5.6 2(b) is renamed **"every prior is served at a world it charges"**. Elsewhere it is "the serving condition": Cor 5.2 proof, Cor 5.2 preamble, Ex 5.4, Rem 5.8, and the finite-G paragraph. "Open cover" and "covered" in the Fig. 1 caption are unchanged. A grep of the PDF finds no "coverage".
- **R-L4.** The end of §7 now includes the companion's maximality statement and the caveat. The third requirement "restricts individual comparisons at individual worlds, and it is stronger than coherent admissibility, which asks only that coherent models remain undominated; its independent justification is open." §9 "Open questions" adds whether that requirement can be justified independently or weakened while preserving the companion's results.
- **R-L5.** "The ranking requirements" is replaced by an explicit list: "a ranking can accept every guided comparison, accept comparisons between distinct models only when they raise the score, be closed under ties, and still have exactly the coherent models as its undominated models".
- **R-L6.** Ex 5.4 now says "losses (t, 1−t) … (2, 2)" and "the loss of m at ω".
- **R-L7.** "Tied at ω" is defined in §2.
- **Guidance wording.** §7 now says "a set of changes said to be *guided at ω* (by the truth there)". "Guided at ω" and "guided at every world" are used throughout. The introduction says "the changes guided at each world".

**Companion title.** The companion is named by its title, *Coherence and accuracy for sets of desirable gambles*, at its first mention in §1 and again in §7.

**Renumbering.** Removing Cor 3.5 and Rem 3.7 renumbers §3: the permissibility proposition is now Prop 3.5. Later numbers are unchanged: Thm 4.2, 4.3; Ex 4.4; Thm 5.1, 5.6; Prop 7.1, and so on.

**New or unrefereed text in Revision 2.** All of it is prose, except one item:
- Fig. 2(b)'s explicit score (checked by RL68 and by me).
- The individuation paragraph (RL68's suggested text, lightly edited).
- The R-L4 caveat (RX68's text).
- The one-sentence copied-worlds claim. Its proof was refereed (REF67_cc §2; RL68 checked the copies form).

## Revision 3 (lead)
- §7: replaced 'coherent models are then protected by definition' with 'every score improvement of an incoherent model is then accepted' (RL68 second round S1).
