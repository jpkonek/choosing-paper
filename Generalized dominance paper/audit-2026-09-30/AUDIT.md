# Audit and revision, 30 September 2026

Revised `Loss Dominance Generalized.tex` in place and rebuilt its PDF. Compared the draft with `CPMs/outputs/complete-class-research/kkm-calibration-v8.tex`. The original source and PDF are saved here as `manuscript-before.tex` and `manuscript-before.pdf`; `revision.diff` records the changes. The v8 source was not edited.

## Main findings and changes

1. **The new (A) has a different quantifier from the old (A).** The new condition is collective: for every coherent model there exists an applicable loss under which it is undominated. It does not entail admissibility of every coherent model for a fixed loss. The local inclusion is now `K_L ⊆ U_{R_L}`, supplied by the definition in (LA), not by (A). The fixed-loss proofs use (LA); (E) and (A) enter the family-level rationality argument.

   A simple check: take one world, two coherent models, and two losses with values `(0,1)` and `(1,0)`. Each model is undominated for one loss and dominated for the other. (A) holds, although no individual loss vindicates both coherent models. In particular, a model outside C_L need not be incoherent.

2. **C_L is the full coherent admissible class, not an arbitrarily selected family.** With the new definition, C_L equals C intersected with U_L. Its admissibility is built into its definition; the additional requirement in (LA) is nonemptiness. The chosen models in (S) and the compact family in (T) must belong to that class. Their profiles need not be stipulated to exhaust K_L: the theorem establishes that they do. Application-specific coherent classes remain independently specified and their admissibility is proved, rather than assumed by calling them C_L.

3. **Profile identification needs a separate assumption.** Added (I) in the opening: C_L is closed under equal profiles within M_L. Because any model sharing an undominated profile is undominated, this is equivalent to requiring such a model to be coherent. It does not require injectivity of the loss map. Without (I), the theorem identifies undominated profiles, and incoherent models can still tie those profiles. The exact conclusion under (I) is U_L = C_L, with domination of every member of M_L outside C_L.

4. **The dominance argument is now visible before Section 2.1.** The opening describes how choice conditions give coherent weak dominators, identification gives domination outside C_L, and (E)/(A) combine those local results across reasonable losses. It states the normative premise separately. Section 6 proves this argument rather than introducing evaluation domains and repeating their axioms for the first time.

5. **Equivalence requires careful coverage.** Section 6 retains the more general conclusion up to an equivalence relation. Under profile identification up to equivalence, the permissible class is the union of M_L intersected with [C_L]. Equality with [C] requires coverage of equivalent models, not just coherent representatives. This follows from (A) if evaluability preserves equivalence, or if coherence itself preserves equivalence. Otherwise it remains an additional condition.

   This extra requirement is not implied by (E). For example, take coherent models c,d and a noncoherent m equivalent to c but not d. One loss evaluates only c. Another evaluates d,m, assigning losses 0,1 at a single world. Both losses satisfy the local choice and equivalence-identification conditions. (E) and (A) hold, but m is evaluated only by the loss under which it is dominated. It is not covered by the permissible union.

6. **Applications require full admissibility where they previously assumed the old (A).** Proper-score, probabilism, conditional-report, and countable examples establish C_L = C. The Joyce subprobability proposition requires this stronger condition explicitly: replacing its old (A) merely by the new (LA) would weaken its assumption incorrectly, since its competitor-dependent construction can visit any point of the coherent simplex. The discussion of countably many conditional cells now says that full coherent admissibility can fail, rather than claiming that the new definition of C_L fails.

7. **Deleted material left an orphaned appendix.** The new draft had removed the integrated error-loss and vertex-tie applications from v8 but retained the appendix proving the deleted vertex-tie proposition. Its references to that proposition, the regret identity, and the tie condition had no definitions. Removed that appendix and the remaining reference to its deleted application, preserving the deletion of the main applications. Its original contents remain in the saved source and v8.

## Mathematical review

The fixed-loss KKM covering proof, the finite-intersection compactness argument, Bayes existence, the margin theorem, and the strict-dominance argument retain their mathematical structure. All competitors and Bayes minimisations are now over M_L. Chosen models are in C_L. The notation R, K, U_R, and V is explicitly retained as an abbreviation for the corresponding loss-indexed objects when L is fixed.

The distinction between dominance, strict dominance, and uniform dominance is retained. The margin discussion still limits the simple expected-gap characterisation of uniform dominance to finite loss profiles; the appendix handles infinite losses separately for finite state spaces. The proofs' uses of support-restricted sums and possible infinite losses were checked.

The conditional construction, rescaling/randomisation example, selection obstruction, ray-bounds construction, countable example, and the internal calculations in the Joyce counterexample were reviewed. No additional change to their mathematical conclusions was required. The audit did not independently reverify all bibliographic attributions against the external publications; the literature comparisons already present were retained.

## Validation

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` succeeds.
- Final PDF: 23 pages.
- No unresolved references or citations, duplicate labels, or overfull/underfull box warnings in the final build.
- Source-level label/reference check passes.
- All pages rendered and visually inspected for layout; the opening, theorems, and rewritten rationality section retain the manuscript's existing typesetting.
