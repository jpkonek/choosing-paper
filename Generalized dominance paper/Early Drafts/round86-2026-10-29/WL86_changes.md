# WL86 change log: ldg_countable.tex

Base: ldg_short.tex. Output: ldg_countable.tex and ldg_countable.pdf (7 pages, pdflatex, no errors, warnings, undefined references, or overfull/underfull boxes). The lead renames it on copying to `Coherence and Dominance under General Rankings - countable selection.tex` (GUIDANCE86 §2).

## Kept from ldg_short.tex
- Section 1 setting: Defs 1.1–1.6 and Lemma 1.7 (ties), with a one-sentence gloss after each definition. The sentence defining "transitive ranking" is dropped, because nothing uses it now. Def 1.1 now also says that reflexivity and continuity are not assumed. Def 1.4 says what "incoherent" means.
- The KKM lemma (Lemma 2.1), with its proof unchanged.
- The dominance principle (Def 3.1), Lemma 3.2, the three-ingredient overview, and the summary (P1)–(P3)/(C).
- Orientation: a ⪯_ω x means "a performs at least as well as x" throughout.

## Replaced (GUIDANCE86 §3)
- Defs 2.2–2.4: a countable family of assignments (Θ_j compact; b^j_θ; F_j(G) ⊇ G for every finite G, with t_{j,G} not necessarily continuous); witnesses (W1) comparison, (W2) compatibility and (W3) support coverage, with A indexed by G; exclusion of ties, universal over ⋂K_ω(x); and countable selection on I. The order of quantifiers is stated explicitly.
- Thm 2.5: the general compact theorem, with no coherence assumption. It gives weak dominance, and dominance when ties are excluded.
- Cor 2.6: the continuous-map / inverse-image sufficient case, which the application uses.
- Cor 2.7: the finite-world specialisation, proved by instantiating Thm 2.5.
- Lemma 2.8 and Cor 2.9: if the assigned models are in C_L and C_L is closed under ties, ties are excluded for x ∉ C_L.
- Def 3.3, with (E), (A), (S_σ) on M_L∖C and (T_σ). The paragraph on what is not assumed is updated, and the tie example is adapted to (T_σ).
- Thm 3.4 (now unnamed): (a) incoherent models are dominated; (b) U_L = C_L, with a note that this uses only (S_σ) and (T_σ) and needs no coherent assigned models; (c) the classification; (d) non-vacuity under (E).
- Cor 3.5: when the assigned models lie in C_L, under (T_σ) or closure under ties, incoherent models have dominators in C_L.
- Section 4: the paragraph on how countable selection relates to a single assignment, including the constant-assignment limitation and the no-converse disclaimer. Example 4.1 has two pairs and shows countable selection is strictly weaker than a single assignment. Example 4.2 has uncountably many pairs and shows dominance does not imply countable selection.
- One sentence cites the companion paper as verifying (S_σ) for its ranking. It cites no theorem numbers.

## Omitted (all still valid; can be reinstated)
- The old one-assignment Thm finite, Cor closed-choice, Thm local and old Cor coherent-assigned. All are special cases of Thm 2.5 and Cor 2.7 with a single assignment.
- The old (S)/(T) and the remark that KCM (A1)–(A4) can replace (S) and (T). GUIDANCE86 §9 removes (A1)–(A4) from the application.
- The subsection "Further conclusions under extra hypotheses" (Props conclusion, profiles, permissible). It is not in the brief's content list.
- The literature applications (ldg_full §8: proper scores, Nielsen, conditional reports, the countable example, Joyce) and their appendix. They rest on the Bayes-choice theorems, the margins section and examples that are absent from the short base, so they cannot be kept without being rewritten.

## Notes for the lead
- At 7 pages the draft is under the 10–12 target. No material was padded in. The abstract is left empty, as in the base.
- Numbering for WA86: Thm 2.5 is the general theorem, Cor 2.6 the inverse-image case, Lemma 2.8 the tie sufficiency, Cor 2.9 the coherent-assigned case, Def 3.3 the assumptions, Thm 3.4 the dominance argument and Cor 3.5 the coherent-dominator corollary.
- Labels: Thm 2.5, Cors 2.6/2.7/2.9/3.5, Lemma 2.8, Thm 3.4 and Examples 4.1/4.2 are PROVED in the draft, and re-derived here line by line. No GAP or ERROR was found.

## Revision after VER86 (coordinator points (a)–(d))
- (a) Def 2.2(iii) now says "including G = ∅". It notes that F_j(∅) := {ω_0}, for a fixed world, is one admissible choice, and that F_j(G) must be nonempty so that Δ_{F_j(G)} is nonempty.
- (b) Def 2.2(ii) now requires explicitly that the assigned models b^j_θ belong to M_L.
- (c) Def 3.3 now treats (S_σ) and (T_σ) as conditions on a single ranking; a family satisfies them if every member does. Thm 3.4 is restated so that each part carries exactly the hypotheses it uses:
  - (a) for a single L with (S_σ) and (T_σ): every incoherent model is dominated, and U_L = C_L. This uses no (A), no (E) and no coherent assigned models.
  - (b) (S_σ) and (T_σ) give: incoherent models are irrational.
  - (c) (A) gives: coherent models are permissible.
  - (d) (A), (S_σ) and (T_σ) give the partition, without (E).
  - (e) (E), (S_σ) and (T_σ) give dominance under at least one ranking. This is the only use of (E).
  
  The note after the theorem says this. Cor 3.5 is now stated for a single ranking (assigned models in C_L, plus (T_σ) or closure under ties) and then lifted to families.
- (d) Other LDG-side VER86 remarks: none needed further changes. The tie clause was already universal over ⋂K_ω (item 7). The construction already used every finite G, not a sequence of them (item 7). The companion-paper sentence already names the almost coherent models as the coherent class (item 9). The remaining VER86 items concern the application.
- Rebuild is clean, still 7 pages.

### Numbering
No result number changed: Thm 2.5, Cor 2.6, Cor 2.7, Lemma 2.8, Cor 2.9, Def 3.3, Thm 3.4, Cor 3.5 and Examples 4.1/4.2 are as before. **The part letters of Thm 3.4 changed:**

| Content | Old part | New part |
|---|---|---|
| incoherent models dominated | (a) | (a) |
| U_L = C_L | (b) | (a) |
| incoherent models irrational | (c) | (b) |
| coherent models permissible | (c) | (c) |
| partition into permissible and irrational | (c) | (d) |
| non-vacuity under (E) | (d) | (e) |

## After REF86
Before editing, I saved the previous file as ldg_countable_v1.tex. REF86 reported no ERROR and no GAP. I applied the LDG-side MINOR findings as follows, using its replacement text.
- L1: the remark after Lemma 1.7 now names 𝒜 := {a}.
- L2: the Brouwer map in Lemma 2.1 is renamed Φ, so that it no longer clashes with the finite set G.
- L3: Theorem 2.5 now assumes only a fixed countable family of assignments and one x ∈ M_L with witnesses at index j. This is weaker than before, so every citation of it remains valid.
- Corollary 2.7: x and j are now bound in the conclusion ("for every x ∈ I and its index j").
- Lemma 3.2: the proof of the second sentence is completed (an evaluating L exists, and irrationality gives a dominator under it).
- L4: (T_σ) now uses Definition 2.4's "with exclusion of ties" wording for the same family. The hypothesis of Corollary 3.5 is reworded the same way.
- L7: the §4 "is replaced by" sentences are rewritten as a comparison of two conditions defined in the paper. I added one qualifier for exactness: the single-assignment side has assigned models in C_L, citing Lemma 2.8. Without it, "weaker" would not be literally true. "instead specifies" now reads "specifies".
- L5: "would be empty" now reads "would add nothing to dominance itself".
- L8: not applied. The abstract stays empty, as the coordinator instructed.

The build is clean: no errors, warnings, undefined references, or overfull or underfull boxes. It is 7 pages. **No result number or part letter changed.** Theorem 2.5, Corollaries 2.6/2.7/2.9/3.5, Lemma 2.8, Definitions 2.2–2.4/3.1/3.3, Theorem 3.4(a)–(e) and Examples 4.1/4.2 all keep their numbers.
