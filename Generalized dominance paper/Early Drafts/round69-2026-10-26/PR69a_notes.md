# PR69a: submission-readiness and copy-edit review of "Coherence and accuracy for sets of desirable gambles"

26 October 2026. Scope: interpretation and presentation only. This is not a new proof-check. Checklist = AUDIT_r69 point 5, as itemised in the PR69a brief.

**State after this review**
- **Files.** The `.tex` was edited (presentation only). It was recompiled with pdflatex ×3, output in `build/`, and the PDF was copied up.
- **Log.** No warnings, no undefined references, no overfull or underfull boxes.
- **Length.** 26 pages (unchanged).
- **Backups.** The pre-review versions are `PR69a_original_backup.tex` and `PR69a_original_backup.pdf`.
- **Page renders.** All 26 pages were rendered at 80 dpi and inspected (`png_pr69a/`; it now holds only the re-rendered p. 15).

---

## 1. Checklist with findings

### 1. Main theorem and contribution identifiable from the introduction?
**Yes.**
- The introduction names the repair theorem (Thm 5.1) as "our main result" and states (i) and (ii) informally.
- It then gives the ranking (Def 6.1) and the characterisation (Thm 6.8) as consequences.
- The paragraph "What this achieves, and what it does not" states the achievement and the limitation together. That limitation is that the ranking represents coherence but does not derive it from independently justified comparisons.

**Fixed.**
- Two labels clashed with "main result = Thm 5.1": the Plan called Thm 6.8 "the main theorem", and App B was titled "Examples delimiting the main theorem". The Plan now reads "characterises coherence as undominatedness (Theorem 6.8)", and App B is "Examples delimiting the main results".
- The intro used "covered" before it is defined. It now says "in the sense of the coverage requirements of Section 6.3".

### 2. Arbitrary worlds, separable gamble spaces, null-set identification, uniform versus strict improvement
**Consistent throughout.**
- **Scope of the gamble space.** "Any set of worlds, but E separable, closed, containing 𝟙 or an order unit" appears in:
  - the abstract;
  - intro Scope (1);
  - §2.1;
  - the statements of Thms 5.1 and 6.8;
  - §9.3, with all four uses of separability listed.
- **Thm 8.1** works in ℝⁿ.
- **Null-set identification** is stated in §2.3 and repeated inside Thms 5.1, 6.8 and 8.1.
- **Uniform versus strict.** Uniform improvement is "fixed margin at every state/world" in the abstract, intro (i), Thm 5.1(1), Thm 6.8(b) and §9.1. Uniform dominance is defined in §6.2, separately from strict dominance. Non-uniform strict dominance is flagged in:
  - intro Scope (4);
  - Thm 6.8(b);
  - the paragraph after Thm 6.8 ("with finitely many worlds they coincide");
  - Ex B.1.

**Small residues (statement wording, listed for sign-off and not applied).** Thm 6.8(d) says "equals it" and Prop 6.6 says "other than itself". Both mean "up to a.e.". This is harmless under the standing identification, but every other statement writes "a.e." explicitly.

### 3. Coherence modulo the measure made clear before "every incoherent model" is first used?
**Before: only partly.**
- The first uses were abstract ("every incoherent set") and intro ¶3 ("every incoherent model").
- The intro said models are identified up to null sets and that "the coherent models are exactly the sets D_Q (Lemma 2.3)". That reads as a theorem about Walley sets, not as the definition.
- The explicit "which sets count as incoherent depends on μ" came only later, in Scope (2).

**Fixed.**
- **Intro ¶1** now defines the notion before first use: a model is *coherent* if it agrees with some D_Q outside a μ-null set, and *incoherent* otherwise, and "throughout, 'incoherent' means incoherent modulo μ". The lemma citation is then attached to the correct claim: under (M2), coherent sets of desirable gambles give exactly the coherent models.
- **Abstract** now reads "every set that is incoherent modulo the measure can be replaced…".
- Both match the §2.3 definition verbatim in content. No mathematics changed.

### 4. Optional construction properties versus requirements of the general argument
**Before: mostly right, but the acyclicity point was made only in §8, in one sentence.**
- Prop 6.2(b) already derived "every cycle consists of a.e.-equal models" as a separate bullet from "no ties".
- Requirement (1) in §6.3 already defined acyclicity as the chain condition only.
- Thm 8.1(a) already says "complete and transitive, hence acyclic".

**Fixed.**
- **§6.3.** A new paragraph after the requirement list says:
  - acyclicity in (1) is the chain condition only;
  - it is the appropriate consistency requirement;
  - it allows ties between distinct models and is satisfied by every total preorder;
  - the ranking's "every cycle consists of a.e.-equal models" follows from its no-ties property (Prop 6.2(b)) and is a special feature of the construction, not a requirement of coverage;
  - veto–Brier rankings tie distinct models.
- **§8.** The sentence now adds: "requiring every cycle to consist of a.e.-equal models would exclude rankings such as this one".
- **Intro.** It now glosses acyclicity as "no chain of weak comparisons ends in a strict reversal". It also says that no ties between distinct models is "a property that the general argument does not require".

**Other optional properties are correctly framed as optional.**
- The completeness and transitivity of veto–Brier appear as "ordering structure" in the §8 contrast and as "not needed" in the §8 opening.
- Disjoint additivity is listed as a property of the ranking, never as a requirement.
- The transitivity of veto–Brier is not used anywhere as a requirement.

### 5. Visual check of the PDF (all 26 pages)
- **Fixed.** Thm 6.8 broke "(M1)–" / "(M3)" across a line. It is now `\mbox{(M1)--(M3)}`. Re-rendered p. 15 is clean.
- **Fixed (proof notation).** Lemma 3.1 proof, "Minimax" step: "z ↦ min_S Φ(q,z)" had a free q. It now reads min_{q∈S} Φ(q,z).
- **Figure 1** (p. 17, contamination simplex): labels are legible and non-overlapping, the caption is accurate, and placement is fine.
- **Long displays** fit the text block: App D z(X), W, the Ex 6.4 bound, and the Thm 5.1 proof displays. No displayed equation is too wide.
- **Theorem statements** have no bad breaks after the fix: Thms 5.1, 6.8 and 8.1, Prop C.1, Cor 7.1.
- **No orphaned headings.**
  - p. 3 ends with roughly 6 lines of white space before §2 starts on p. 4. This is acceptable, and the journal will reflow it.
  - Ref [6] in the bibliography shows slightly stretched inter-word spacing, because of its short title-case line. This is cosmetic.

### 6. Bibliography, cross-references, companion title, metrizability proof
- **Cross-references.** All resolve.
  - §6.3 was given a label (`sec:undominated`).
  - The three pointers to "the requirements" now cite §6.3 rather than §6: intro "What this achieves", intro "The ranking", and §9.1.
  - The §8 acyclicity sentence also now cites §6.3.
  - Cor 7.1(c)'s reference to Thm 6.8(b)–(d) is still correct after the earlier relettering.
- **Konek PPR.** The entry reads "*Philosophy and Phenomenological Research*, forthcoming". It has no year, volume or pages, as required. The source still carries the comment `% year, volume, pages to be supplied by the author`. Remove that comment before submission.
- **Companion.** The entry is "Coherence and Dominance under General Rankings. Manuscript, 2026", and it matches the companion's `\title`. **For the lead:**
  - every other article title in this bibliography is in sentence case;
  - the companion cites this paper in sentence case;
  - so "Coherence and dominance under general rankings" would be house-consistent.
  - I did not change it, because Revision 3 item 6 asked for exact capitalisation. It is a one-line choice.
  - No reference to the old title "Generalized Loss" remains anywhere in this paper.
- **Other references.**
  - SSK, Mayo-Wilson–Wheeler, Schoenfield, Berger–Das, Pettigrew: details agree with RA68b's web-verified table.
  - Joyce 1998, Predd et al. 2009, Sion 1958, Lindenstrauss 1966, Lyapunov 1940, Rockafellar 1970, Walley 1991, Diestel–Uhl 1977: standard and correct as far as I know.
  - The Quaeghebeur chapter "Desirability", pp. 1–27 of Augustin et al. (Wiley, 2014), matches the usual citation. A quick search did not independently confirm the page range against the printed book.
  - The SSK one-sentence summary was flagged in WA68 for the author to confirm against SSK's theorem. That flag still stands.
- **Aliprantis–Border.** It is gone entirely: there is no citation and no leftover comment.
- **Metrizability proof (App A, Lemma 2.1(a)): correct.** The steps are:
  1. (h_n) is dense in the unit ball, which exists because E is separable.
  2. Each term of d is weak-* continuous on S×S and bounded by 2·2⁻ⁿ, so d is weak-* continuous.
  3. d(q,r)=0 gives q=r on a dense subset of the ball, hence on E by norm continuity and scaling.
  4. So id: (S, w*) → (S, d) is a continuous bijection from a compact space onto a metric (Hausdorff) space, and hence a homeomorphism.
  
  This differs slightly from the audit's sketch, which uses "convergence on the dense sequence extends by uniform boundedness". Both are valid, and the compact-to-Hausdorff route is complete as written. The facts that d is a metric (symmetry, triangle inequality) are left implicit; they are obvious.

### 7. Authorship
- **Not changed.**
  - The author block is "Jason Konek and Catrin Campbell-Moore", with pdfauthor the same and the date "October 2026".
  - The form is identical to the companion's.
- **For the author.** Per the audit, this needs Jason's confirmation and agreement with Catrin.
  - Authorship of the earlier note does not settle it.
  - RX68 records that the source draft of this paper's core ("Universal coverage …") listed Jason alone.

---

## 2. Fixes applied (presentation only)
1. **Abstract.** "every incoherent set" → "every set that is incoherent modulo the measure".
2. **Intro ¶1.** It now defines coherent and incoherent models modulo μ before first use. Lemma 2.3 is now cited for the correct claim: coherent sets of desirable gambles give exactly the coherent models under (M2).
3. **Intro "The ranking", acyclicity.** Acyclicity is glossed as the chain condition. "No ties between distinct models" is marked as a property the general argument does not require.
4. **Intro "The ranking", coverage.** "Covered" is tied to the coverage requirements of §6.3.
5. **Intro "What this achieves" and §9.1.** The pointer to the requirements is now §6.3 instead of §6.
6. **Plan.** "derives the ranking and the main theorem" → "derives the ranking and characterises coherence as undominatedness (Theorem 6.8)".
7. **§6.3.** Added `\label{sec:undominated}`, plus a new expository paragraph on acyclicity:
   - it is the chain condition only;
   - it is the appropriate consistency requirement;
   - it allows ties and is met by total preorders;
   - "every cycle consists of a.e.-equal models" is a special feature of Def 6.1's ranking, via no ties;
   - veto–Brier rankings tie distinct models.

   The claim "every total preorder satisfies it" is a one-line triviality: transitivity gives A₀ ⪯ A_k, which excludes A_k ≺ A₀. Thm 8.1(a) already uses it.
8. **§8.** The acyclicity sentence now cites §6.3 and adds that requiring cycles to consist of a.e.-equal models would exclude veto–Brier rankings.
9. **Thm 6.8.** `\mbox{(M1)--(M3)}` prevents the line break after the en dash. This is typographic only.
10. **Lemma 3.1 proof.** `\min_S\Phi(q,z)` → `\min_{q\in S}\Phi(q,z)`. This is notation only: the bound variable was previously free.
11. **§9.3.** "Some condition of the second kind is needed" → "Some condition like the second, a gamble bounded below by a positive constant, is needed". The old phrase was an unclear referent.
12. **App B title.** "Examples delimiting the main theorem" → "Examples delimiting the main results". Ex B.1 delimits Thm 6.8(b) and Ex B.2 delimits Prop 6.6.

## 3. Requires sign-off (not applied)
1. **Thm 6.8(d).** Change "a model tied with a coherent model at any one world equals it" to "… equals it a.e.". This is consistent with how every other statement is phrased, and there is no mathematical change under the standing identification.
2. **Prop 6.6** (and Thm 6.8(d), first clause). Optionally change "no weak dominator other than itself" to "no weak dominator not a.e. equal to it". The same remark as in item 1 applies, and it is optional.
3. **Companion bibliography entry.** Choose sentence case ("Coherence and dominance under general rankings") for house consistency, or keep title case as instructed in Revision 3. This is the lead's call.
4. **Author's items, outside my remit.**
   - Authorship (§1.7 above).
   - The final Konek PPR details, or keeping "forthcoming".
   - Confirming the SSK summary sentence.
   - Removing the Konek-entry source comment before submission.

No mathematical statement or proof was altered beyond item 10 of §2, which is notation only.

## Lead edits after PR69a
- Thm 6.8(d): 'equals it' -> 'equals it a.e.'.
- Companion bibliography title set in sentence case, matching the other entries.

## Framing check (dominance proved, not assumed)

The mathematics already proves dominance: Prop 6.6 shows coherent models are undominated, and Thm 5.1 with Prop 6.7 shows every incoherent model is uniformly dominated by an undominated coherent one; Thm 6.8 assembles these. No result assumes a dominance property. The fixes are wording only.

1. **§6.3, cover definition.** The sentence "The requirements we adopt for an accuracy ranking …" is replaced by a short paragraph that sorts the conditions into kinds:
   - (1) constrains the ranking: strict guidance, independence, acyclicity;
   - (6) constrains the domain (local freedom);
   - (2)–(5) are *the dominance property*: what a covering ranking must achieve, not what it is assumed to satisfy.

   It then says: "For the ranking of Definition 6.1 no condition is assumed; Theorem 6.8 proves all six." The list of conditions is unchanged.
2. **Introduction.** A new paragraph, "Dominance is proved, not assumed", follows "The ranking":
   - nothing in the definition presupposes that incoherent models are dominated or that undominated models are coherent;
   - protection (Prop 6.6) keeps coherent models undominated;
   - the repair theorem supplies a coherent replacement accepted as strictly better at every world;
   - together these give the dominance property (Thm 6.8);
   - one sentence says this bypasses the usual route, in which coherent models are assigned to priors, the comparisons guaranteed at each prior must form closed sets, and a covering lemma of Knaster–Kuratowski–Mazurkiewicz type is applied.

   No labels are used.
3. **Assumption-like phrasing rephrased.**
   - **Intro, "The ranking":** "in the sense of the coverage requirements of Section 6.3" → "in the sense of Section 6.3".
   - **Intro, "What this achieves":** "the requirements we adopt for accuracy rankings … are compatible with coherence" → "a ranking meeting the constraints we impose on accuracy rankings can achieve the coverage property of Section 6.3 for every credal set".
   - **§9.1:** "the requirements of Section 6.3 are compatible with coherence and can represent it exactly" → "the conditions of Section 6.3 can all be met, with undominatedness singling out exactly the coherent models".
   - **§9.1, companion pointer:** adds "here their existence is proved directly, not assumed".
   - **Abstract:** "As a consequence, and without assuming any dominance property, one ranking …".
4. **Checked and left unchanged.**
   - Cor 7.1(d), "every ranking on U that covers K needs both conditions": these are conditions of the definition, not assumptions.
   - Thm 6.8 proof, which says "Requirement (k) holds by …"; it already reads as proofs of each condition.
   - Thm 8.1, which proves each condition for veto–Brier.
   - §9.2, the coherent-admissibility discussion.

**Requires sign-off:** none. No mathematical statement or proof was changed.

**Build:** pdflatex ×3 in `r69/build/`; clean (no warnings, undefined references, overfull or underfull boxes); PDF copied to `r69/`. 26 pages.

## Companion description updated (LDG restructure)
- §9.1, the companion paragraph (formerly l. 1237), now follows LDG's new order.
  - LDG first derives the dominance property from independently checkable conditions. This uses a Knaster–Kuratowski–Mazurkiewicz argument on finite sets of worlds that needs only closed sets of guaranteed comparisons, plus a compactness step.
  - It then records what follows from that property.
  - Finally, it reduces the construction of rankings to the existence of specific improvements, which Thm 5.1 supplies here.
- That is the only description of LDG in the paper.
- The intro's "Dominance is proved, not assumed" paragraph describes the usual route, not LDG's structure. It is consistent with the new description and is unchanged.
- No mathematical change. Clean rebuild in `r69/build/`, 26 pages.
