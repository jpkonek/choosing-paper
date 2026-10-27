# W65 — completing the covering paper: decisions, sources and flags (26 Oct 2026)

Labels: PROVED-ref (the proof follows a refereed source, re-proved in the paper) / PROVED-W65 (the result is refereed, but W65's write-up or organisation of the proof is new, so a referee should read it) / REMOVED.

## Deliverables

All files are in `r65/`.

- `Covering coherent sets of desirable gambles (draft).tex` and `.pdf`.
  - The PDF has 57 pages; the previous version had 44.
  - pdflatex (three passes) gives no warnings, no undefined references, no overfull boxes and no underfull boxes.
- `w65build/` holds the build files and backups:
  - `draft_before_W65.tex` and `.pdf`: the input versions;
  - `removed_block.tex`: the old §8.3, "Further exclusions, recorded without proof", as removed;
  - `new_block.tex` and `appendix.tex`: the inserted text.

Section map after the revision:

| § | Content |
|---|---|
| 8.1 | Veto–Brier rankings. Unchanged, apart from the two citation replacements below |
| 8.2 | Vetoes followed by an error level. Definition 8.7 now defines the class 𝒱 (vetoes, then a strict error level, with (G)) and the subclass 𝒱_B. Lemmas 8.8–8.11 are stated for 𝒱, with their proofs unchanged. Theorem 8.12 (𝒱_B) and Corollary 8.13 are unchanged. **New: Theorem 8.14 (convex error levels).** |
| 8.3 | **New:** unanimity rankings with convex vetoes and concave gains. Definition 8.15 (views, unanimity); Definition 8.16 (priority region); Lemma 8.17 (box lemma); Lemma 8.18 (collar lemma for R); the collar construction; **Theorem 8.19 (a), (b)**; a remark that concave single charts are excluded |
| 8.4 | **New:** single charts. The four-condition certificate (C1)–(C4) for general n; **Theorem 8.20** (regular certificate charts on domains ⊇ U₊ force orthant-planarity); **Corollary 8.21**; **Theorem 8.22** (piecewise-linear charts, three worlds; proof in Appendix A) |
| 8.5 | Composition, veto–box and chart rankings (old 8.4; now 8.23–8.27) |
| 8.6 | What the exclusions do and do not show. References updated |
| 9 | Open problems. (7) gains a sentence citing Corollary 8.21; new (9) on single charts on one-sided domains |
| App. A | **New:** proof of Theorem 8.22 (Proposition A.1, Lemmas A.2–A.10) |

The veto–box section (§6) is untouched. Nothing on the deletion construction or (H) was added.

## Task 1: the six exclusions of the old §8.3

| # | Old item | Decision | Where | Source → referee |
|---|---|---|---|---|
| 1 | Convex error levels: R, interior PMM triangles, polytopes with ≥ 2 all-crossing vertices | **PROVED** (PROVED-W65 write-up of a refereed proof) | Theorem 8.14 | O61 Thm B → ROUND61 impossibility referee CORRECT; PMM upgrade REF62_fd §3 → REF62_R2 row 24 CORRECT; scope REF64_pc row 9 and REF64_bx §5.2; (G) per REF64_bx 5a |
| 2 | Concave charts (E61 Cor 5.2) | **PROVED** (PROVED-W65) | Theorem 8.19(a) | E61 Cor 5.2, with Thm 5.1(b)(c), Lemma 3.4, Cor 3.2, Lemma 3.1 → ROUND61 CORRECT |
| 3 (first part) | Regular single charts with (DF), (ND) at π\* (R15 Thm 1 + A62 Cor 2.3; map x ↦ 3/2 − 1/x) | **REMOVED** | — | A62 Cor 2.3 → REF62_corner: "CORRECT, conditional on R15 Thm 1, Lemma 3.2 and R18's refereeing". R15 Thm 1 rests on R1 Prop 3.1, R10b UVN(a) and CCIBU, which are not among the round's sources; REF62_corner says it could not read CCIBU or R1 Prop 3.1. A self-contained proof cannot be assembled from refereed material. The nearby results that are proved are Theorem 8.20 (two-sided domains) and Theorem 8.22 (one-sided cones, PL and direction-continuous PL charts) |
| 3 (second part) | Full-domain regular certificate charts force orthant-planarity | **PROVED** (PROVED-W65) | Theorem 8.20, Corollary 8.21 | REF62_fd Thm R1(a)–(b), Lemma R0 and FD62 Lemma FD-3 → REF62_R2 rows 1–7 and 9 CORRECT, with its §2.2 closing the a.e. gaps. Row 8, R1(c) ("continuous ⇒ box"), is an ERROR and is **not** used |
| 4 | Continuous piecewise-linear charts (C62 Thm 4.1) | **PROVED** (PROVED-W65) | Theorem 8.22(b), App. A.5 (Lemma A.10), then Proposition A.1 | C62 Lemma 4.2 → REF62_corner CORRECT (needs (C2), (C3) on the segments (e_k, u]); the rest through the DC63 chain (row 5). See flag F3 |
| 5 | Direction-continuous PL charts with (C2) at π\* (DC63 Thm DC) | **PROVED** (PROVED-W65) | Theorem 8.22(a), App. A.1–A.4 | DC63 → REF63_neg: "CORRECT with (C2) at u". Also REF62_corner's repaired C62 Lemma 4.3 and C62 Lemma 2.2 (necessity of the kink condition) → REF62_corner CORRECT |
| 6 | Finite unanimity (IN63 Thm C) | **PROVED** (PROVED-W65) | Theorem 8.19(b) | IN63 Thm C → REF63_neg CORRECT; it uses E61 Lemma 3.4 and Cor 3.2 (ROUND61) |

### Notes on each decision

**(1) Theorem 8.14.**
- *Hypotheses.* A ranking in 𝒱 with convex error levels on an open convex G ⊇ U. U is one-sided, D_K ⊆ U a.e., and (LF) holds. D_K is undominated and the X_kj are coherent. The conclusion excludes:
  - (a) every pari-mutuel model in relint Δ₃, which is always a triangle; R is one case;
  - (b) every polytope in relint Δ₃ with two vertices at which every world is crossing.
- *Proof.* This is O61's steps 1–6, written out:
  - the prior Γ;
  - Γ = 0 on the faces;
  - affine summands;
  - crossing rows by a ball argument;
  - one slope per world, through an explicit subgradient argument;
  - (a) the ray matrix u𝟙ᵀ − I, with det = δ (matrix-determinant lemma);
  - (b) x ∈ ℝv and x ∈ ℝw.
- *Generalising Lemmas 8.8–8.11 from 𝒱_B to 𝒱.* Their proofs never used the Brier form (REF64_bx optional 6g). The text after the theorem keeps REF64_pc's scope remarks: PMM vertices are not all-crossing, and Example 6.7 lies in the class.

**(2) and (6) Theorem 8.19.**
- *One proof for both parts.* Following IN63 Thm C's structure, with S₀ empty in case (a).
- *What it uses:*
  - the box lemma (E61 Cor 3.2 via Lemma 3.1);
  - the collar lemma (E61 Lemma 3.4);
  - separation on models inside D_R ∪ C (IN63 step 2; this replaces E61's appeal to "LDG Prop lexbayes");
  - the face, circulant and chord steps of E61 Cor 5.2 and IN63 Thm C.
- *W65's own simplification.* Lemma 8.18 is proved by one convex-combination estimate valid at every point of relint F_k. E61's case split p_j > 0 versus p_j ≤ 0 is not needed. A referee should check it.
- *Remark.* After the theorem, a short remark excludes concave positively homogeneous single charts meeting the certificate, through (b) with one view per world.

**(3b) Theorem 8.20.**
- *Statement.* n ≥ 3, K ⊆ relint Δ, and U ⊇ U₊ a.e., where U₊ is the set of gambles with a positive coordinate. This is REF62_R2 row 9's observation that R0 and R1 use only gambles that are not ≤ 0. The certificate holds at every prior (REF62_R2 row 2).
- *Corollary 8.21.* With Theorem 2.9, this gives the item's original consequence for every domain that is not essentially one-sided.
- *The proof is W65's organisation:*
  - Step 0: the support restriction FD-3, plus the "sandwich" (2), which replaces the a.e. continuity argument of REF62_R2 §2.2;
  - Step 1: R0;
  - Step 2: an explicit inverse-function lemma, the F′ > 0 point of REF62_R2 row 4;
  - Steps 3–4: concavity of g and convexity of ψ, via strict epigraphs and hypographs;
  - Step 5: linearity;
  - Step 6: orthant-planarity.

**(4) and (5) Theorem 8.22 and Appendix A.**
- *Overall route.* Proposition A.1 is DC63's Theorem DC with (C2) at u. Part (b) (C62) is reduced to it through C62 Lemma 4.2 (Lemma A.10).
- *The chain:*
  - Lemma A.2: convexity test;
  - Lemma A.3: the kink test, i.e. the necessity half of C62 Lemma 2.2;
  - Lemma A.4: DC63 4.2-D(a)–(e), stated locally near ∂D_R;
  - Lemma A.5: the wall dichotomy;
  - Lemma A.6: DC63 4.3-D(a), local rescaling plus REF62's repaired C62 Lemma 4.3;
  - Lemma A.7: the junction lemma, DC63 4.3-D(b);
  - Lemma A.8: DC63 4.3-D(c);
  - Lemma A.9: crossing rows, DC63 4.4-D;
  - the corner system, with T³(x) = (3x − 10)/(10x − 12), giving 2a² − 3a + 2 = 0.

## Task 2: citations

| Citation | Where | Decision | Evidence |
|---|---|---|---|
| Rockafellar Thm 6.3 (ri cl C = ri C, cl ri C = cl C) | Lemma 2.3; standard-facts list (§2.1); Theorem 8.20 step 6; Lemma A.10 | **VERIFIED; kept** | Lecture notes `healy.econ.ohio-state.edu/kcb/Notes/SeparatingHyperplane.pdf`, Proposition 16, cite "Rockafellar [6, Theorem 6.3, p. 46]" for these relative-interior/closure identities. The notes `public.websites.umich.edu/~tborgers/Interiors.pdf` say their Proposition 4 ("cl(ri S) = cl S and ri(cl S) = ri S") "extends Theorem 6.3" of Rockafellar (1970) |
| Rockafellar Thm 11.3 (proper separation iff the relative interiors are disjoint) | Lemma 3.5; Lemma 4.13; Theorem 8.19, step 2 | **VERIFIED; kept** | "Revisiting Rockafellar's Theorem on Relative Interiors of Convex Graphs" (`par.nsf.gov/servlets/purl/10494605`; arXiv:2201.10689) states, before its Theorem 2.3, "Ω1 and Ω2 can be properly separated if and only if ri(Ω1) ∩ ri(Ω2) = ∅", citing [16, Theorem 11.3], where [16] is Rockafellar's *Convex Analysis* |
| Rockafellar Thm 13.2 (support functions) | Lemma 8.1 | **NOT VERIFIED → replaced** | Searched; no source quoting the number was found. Lemma 8.1 now proves directly that a finite sublinear φ equals max_{y∈B̃} y·h, with B̃ := {y : y·h ≤ φ(h) ∀h}. The proof uses the supporting hyperplane theorem (Rockafellar Thm 11.6, verified in round 64) on the epigraph, plus homogeneity |
| Schrijver §8.5 (minimal faces and vertices) | Corollary 8.5 | **NOT VERIFIED → replaced** | Searched; Google Books and archive.org give no section list for chapter 8. The vertex characterisation (vertex iff 𝟙 and the active g_f span ℝⁿ, iff v is the unique point of aff Δ satisfying the active equalities) is now proved in four lines in the proof of Corollary 8.5. Schrijver remains cited only for Cor 7.1a and 7.1h (verified in round 64) |

**Added without a number.** The standard-facts list in §2.1 now also cites Rockafellar, with no number, for "a convex function on an open convex set is continuous and has a subgradient at every point". Appendix A uses, without citation, the fact that a polyhedral convex set agrees near each of its points with that point plus its tangent cone.

## Other edits

- **Abstract.** It now lists the proved exclusion classes. "We record others without proof" is removed.
- **§8 opening.** The text now says that §8.3 concerns transitive unanimity rankings. The old reference to items (2) and (6) is removed.
- **§8.6.** It cites Theorem 8.14(a) and Corollary 8.21. The escape list now says "a chart outside the classes of Theorems 8.20 and 8.22 and of the remark after Theorem 8.19".
- **(TC) caveat.** The old §8.3 closing remark is kept after Theorem 8.19: the box lemma's step "Y ⪯_j X ⪯_j M ⇒ Y ⪯_j M" holds for unanimities, but (TC) does not imply it.
- **Date line.** Now "Draft, 26 October 2026".
- **Conventions, checked by grep:**
  - no optional names on theorem-like environments;
  - no `:=` or `=:` (only `\coloneqq` and `\eqqcolon`);
  - no commentary comparing drafts;
  - "models" throughout;
  - the dominance nomenclature is unchanged.

## Flags

- **F1. New write-ups need a referee.** None is a new theorem; each re-proves a refereed statement, but the text and some arguments are W65's:
  - Theorem 8.14: the subgradient step and the determinant;
  - Lemma 8.18: a simplified collar proof;
  - Theorem 8.19: the merged proof of (a) and (b);
  - Theorem 8.20: steps 0–4 reorganised;
  - all of Appendix A;
  - the concave-chart remark after Theorem 8.19.
- **F2. Hypotheses slightly weaker than the sources.** In each case the proof uses only what is stated, but strictly the stated theorem is a little stronger than the refereed one:
  - (a) Theorem 8.19(a) needs the sign conditions only on U, and convexity only up to a.e. agreement on U ∩ O. E61 assumes both on O.
  - (b) Theorem 8.20's (Reg) asks for local Lipschitz continuity on each open mixed orthant, after an a.e. modification. REF62_fd asks for it on each closed orthant. The bounds A ≤ c_l/h_l ≤ B are the same condition restated by homogeneity.
  - (c) Proposition A.1 asks the fan and direction field to cover only a conic neighbourhood of ∂D_R∖{0}. DC63 asks for a neighbourhood of cl D_K∖{0}. This is what makes the reduction of part (b) possible.
  - If strict fidelity to the sources is wanted, restate with the source hypotheses; no proof changes.
- **F3. Possible gap in the refereed proof of C62 Lemma 4.3 (item 4), closed in the paper.**
  - C62's proof, and REF62_corner's repair ("the kink test at q = u + tδ gives u·d_j ≤ 0"), assume that u·c > 0 along every inner half-wall at a facet point. Otherwise the zero set of q·c need not cross the wall near w.
  - A continuous PL field could in principle have u·c = 0 along an inner half-wall (a "valley"), and neither note treats that case.
  - The paper does not follow C62's route there. It reduces item (4) to the direction-continuous case, where DC63 Lemma 4.2-D(b) gives strict positivity inside D_R (Lemma A.4(ii); REF63_neg CORRECT). This excludes valleys.
  - A referee should confirm this reading.
- **F4. Theorem 8.14(b) is stated for n = 3, as before.** Its proof uses n = 3 only through the paper's previous scope; the argument of step 5(b) works for any n. The statement was not widened, because the general-n form was not explicitly refereed.
- **F5. Item 3's first part is gone.**
  - The paper no longer mentions (DF), (ND), Gâteaux differentiability or the map x ↦ 3/2 − 1/x.
  - New open problem (9) asks whether some chart on a one-sided domain meets the certificate for R. The text records what is now proved: concave components are impossible (remark after Theorem 8.19), and PL and direction-continuous PL charts are impossible (Theorem 8.22).
- **F6. Inherited from round 64 and unchanged.**
  - Second refereeing of Theorem BX (REF64_pc recommendation).
  - The W64 write-ups listed in W64_changes R7: Theorem 7.16(d), Proposition 8.27 (the contamination proposition, previously 8.18), Lemma 6.5, Corollary 7.9, Lemma 5.8, Corollary 8.25 (previously 8.16).
  - The second author's name, carried over from W62.
  - Ziegler is still cited without a number.
- **F7. Length.** The paper grew from 44 to 57 pages. Appendix A (about 6 pages) could move to supplementary material if the journal requires.

---

# Revision 2 (26 Oct 2026, after REF65_paper)

REF65_paper found no mathematical error in any new proof. All six of its required changes and the five recommended changes requested by the coordinator are made in place.

- Output: `Covering coherent sets of desirable gambles (draft).tex` and `.pdf`.
  - 57 pages.
  - pdflatex (three passes, clean auxiliary files): no warnings, no undefined references, no overfull or underfull boxes.
- Backup of the pre-revision source: `w65build/draft_before_rev2.tex`.

## Required changes

| # | Change | Done |
|---|---|---|
| 1 (S2) | §8.4 sentence before Theorem 8.22 | Now: "On open convex cones that contain C_R∖{0} and no nonzero h ≤ 0, charts that are continuous piecewise-linear, or direction-continuous piecewise-linear, near C_R∖{0} cannot meet the four-condition certificate for the reversed triangle." |
| 2 (S1) | Abstract | The chart items now read "…; composed, veto–box and chart rankings; and, for the certificate of single-chart coverage, regular charts on domains that are not essentially one-sided and continuous or direction-continuous piecewise-linear charts on one-sided cones." |
| 3 (S3) | §8.6, "lies in the scope of every exclusion above" | Replaced by the explicit list: Cor 8.5(a); Thm 8.12 with Cor 8.13; Thm 8.14(a); Thm 8.19 and the remark after it; Cor 8.21; Thm 8.22; Cors 8.24 and 8.25 |
| 4 (S4a) | §8.6 escape list | Now: "…or by being additive with a chart that does not meet the four-condition certificate (Theorems 8.20 and 8.22 concern the certificate, not coverage by chart rankings in general), or that meets it but lies outside the classes of those theorems." |
| 5 (S4b) | Open problem (9) | Now names the two classes: "cannot be continuous piecewise-linear or direction-continuous piecewise-linear near C_R∖{0}". It also records the strengthened concave-chart remark (item 9 below) |
| 6 | Lemma A.4(iii), rank-1 case | The constant-sign, constant-direction and 𝟙·δ = 0 statements are now made on int σ ∩ B(w, ρ_w) ⊆ V |

## Recommended changes

| # | Change | Done |
|---|---|---|
| 8 (F4) | Theorem 8.14 | Now "Let n ≥ 3 …; (a) n = 3 and K is a pari-mutuel model …; or (b) K is a polytope with two vertices at each of which every world is crossing". The proof is unchanged in substance. Step 3(iii) now says "hyperplane v^⊥", and V′ is the (n−2)-dimensional subspace v^⊥ ∩ e_j^⊥ ("an interval of the line" became "a nonempty relatively open subset"). Step 5(a) now begins "Here n = 3". Refereed for general n in REF65_paper §1. **Flag F4 is withdrawn.** |
| 9 | Remark after Theorem 8.19 | Strengthened to: no chart ranking with concave positively homogeneous components on U as in (b) that satisfies (G) has D_R undominated with every undominated model coherent; in particular none covers R. The proof: (G) applied to (S, ∅) and (∅, S) forces the strict signs a.e., so concavity gives weak signs everywhere and joint strict guidance; then Theorem 8.19(b) applies. No part of the certificate is needed |
| 10 | Open problem (7) | Now "no chart satisfying (Reg) meets the four-condition certificate for them there" |
| 11 | Appendix numbering clash | The appendix subsections are unnumbered (`\subsection*`). The two cross-references to them now name them ("the subsection 'Part (b)' below"; "until the end of the subsection 'The corner system'"). Lemma and proposition numbers A.1–A.10 are unchanged |
| 13 | Theorem 8.20, proof | Adds "(enlarging U by a null set if necessary)" after "we may assume" |

## Corrections to the first part of this file

- References to "App. A.1–A.4" and "App. A.5" in the Task 1 table mean the unnumbered appendix subsections "Two tests" through "The corner system", and "Part (b)".
- **F2 additions** (REF65_paper item 12):
  - (d) Theorem 8.22(a) allows an arbitrary positive measurable scale, where DC63 had one constant per cell. The proof only uses B_π, which depends only on δ by (Bdelta).
  - (e) One-sidedness of U is not used in Theorem 8.19(a) or Theorem 8.22, beyond D_R ⊆ U a.e., (LF), and V ⊆ U. REF65_paper rates F2(a)–(d) all CORRECT.
- **F3** is confirmed by REF65_paper §6. It is a real gap in the refereed C62/REF62 proof of Lemma 4.3, closable by inserting DC63 4.2-D(b). The paper's route avoids it.
  - **Round-log item (not a paper change):** results refereed "given C62 Thm 4.1 as repaired by REF62", for example IN63 Theorem S, inherit this one-line repair.

## Remaining flags

- F1: the W65 write-ups. These have now been refereed once, by REF65_paper.
- F5, F6 and F7 are unchanged.
