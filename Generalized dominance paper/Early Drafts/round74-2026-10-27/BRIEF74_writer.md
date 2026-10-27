# Round 74 writer brief (WA74): the application paper, stripped to its formal core

Write ONLY in /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r74/.
Output: `core.tex` (compiles with pdflatex; keep the round-70 preamble, macros, title and authors from app_r70.tex), its PDF, and `WA74_changes.md` (what was kept, cut, renamed; label map old→new).

## Sources
- app_r70.tex: current manuscript (round 70). Reuse its setting, lemmas and proofs wherever they still apply.
- DPR73_report.md: the proof of Theorem D′. Apply REF73b_report.md's corrections; its §6 is the clean statement.
- REF73_report.md: an independent proof. Use it where clearer.
- MU73_report.md §2: margin triples, their existence (Lemma T), Lemma W.
- AUDITOR_guidance_1300.md: the auditor's instructions. Follow them.

## Author's instructions (binding)
- Strip the paper to the formal core and remove all exposition. The author will add exposition by hand.
  - No introduction, discussion, motivation, history, related work or "remarks".
  - The ONLY permitted prose explanation is a plain-English gloss of what each axiom means: one or two sentences per axiom.
- Every technical notion gets an explicit, numbered definition. A good undergraduate must be able to follow it.
  - Notions include: world, gamble, gamble space, state, credal set, D_Q, coherent model, the measure and its conditions, model (a.e.-class), change, guided, ranking, comparisons, ties, strict comparison, dominance, undominated, margin triples of both kinds, consolidation, admissibility.
- One explicit, numbered list of all axioms used anywhere, each with its plain-English gloss.
- Keep the results as streamlined as possible: short statements, and proofs complete but lean.
- No jargon ("certificate", "record", "safe", "dangerous", "route", "shelter"). No names on theorem environments. Use \coloneqq. Say "models". Use standard dominance terms. No commentary comparing versions.

## Required structure
1. **Setting and definitions.**
   - Ω any nonempty set; E ⊆ ℓ∞(Ω) a separable norm-closed subspace containing 𝟙; states; credal sets; D_Q; Lemma states (only the parts used).
   - The measure μ with (M1)–(M3). State precisely which results use which, and whether μ must be atomless or have a full-support atomless part.
   - Models modulo null sets; coherent models; the identification lemma.
   - The coherent hull, if used.
   - Changes; guided at ω; available to a model.
2. **Rankings and dominance.**
   - A ranking: one binary relation ⪰_ω on models per world.
   - Define ties and strict comparisons.
   - Define dominance exactly as in app_r70: weakly preferred at every world, strictly at some.
3. **Axioms.** One numbered list:
   - (A1) **Guidance.** If X ≠ Y a.e. and the change from Y to X is guided at every world, then X ≻_ω Y at every ω. This is the weakest form the theorem needs; it is implied by strict guidance.
   - (A2) **Three-model condition.** There are no A ⪰_ω B ⪰_ω C with C ≻_ω A.
   - (A3) **Transitivity through ties.**
   - (A4) **Consolidation**, in both forms (sum and midpoint), with the uniform-margin formulation of REF73b §6.
   - (A5) **Admissibility of a family 𝒦 of coherent models.** Each member is undominated.

   Plain-English gloss for each axiom. For (A4), state explicitly that equality of μ-masses fixes how much of each part is replaced.
4. **Main theorem (Theorem D′).** Assume (A1)–(A4), (M2), and that the atomless part of μ has full support. Then every incoherent model is dominated.
   - Organise the proof as the auditor asks: first preservation of undominatedness through ties (tie lemma; consolidations of undominated models are tied with them), then the geometric identification of coherent sets. Put measure-theoretic details in lemmas.
   - Do NOT claim that undominated models "cannot be consolidated".
   - Corollary: add (A5) for all coherent models ⇒ the undominated models are exactly the coherent ones; for a family 𝒦 ⇒ every member of 𝒦 is undominated and every incoherent model is dominated.
5. **The integral ranking (an example satisfying the axioms).**
   - Define m_ω and the rule of app_r70 Definition 6.1.
   - Proposition: under (M1)–(M3) with atomless μ, it satisfies (A1)–(A4), and (A5) for all coherent models.
   - Proof of (A4): a margin consolidation adds gambles in the coherent hull of what it removes, so no coherent model could make it, and it raises m_ω at every world.
   - Proof of (A3): there are no ties between distinct models.
   - Proof of (A5): reuse app_r70's protection proof (guidance-protection lemma).
   - Existence of such μ for every admissible Ω and E: reuse lem:measure and check that it is atomless. Do not claim nonemptiness for every fixed μ allowed by the theorem.
6. **Coherent dominators under the integral ranking.**
   - The repair theorem of app_r70 (Thm 5.1) and its consequence: every incoherent model is strictly dominated, at every world, by an undominated coherent model.
   - Keep its proof (minimax lemma, trimming), streamlined.
7. **Appendix: proofs of setting lemmas**, only those used.

## Cut entirely
- Introduction, discussion, scope, open questions.
- Maximality (Prop 6.3), the intransitivity example, the restricted-domain corollary, one-sided domains, veto–Brier and its appendix.
- Examples delimiting the main results (including the necessity of (M2) and (M3)), the "covers K" definition, and all remarks.

## Verification
Compile cleanly with no undefined references. Check that every symbol used is defined before use. Write WA74_changes.md. Final message: summary under 250 words, including page count.
