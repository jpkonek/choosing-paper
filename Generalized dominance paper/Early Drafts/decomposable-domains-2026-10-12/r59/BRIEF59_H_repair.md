# Brief 59: repairing incoherent arrangements in the equal-loss class H (24 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- **Audit, ALL BINDING:**
  - `AUDIT_round59.md` (the H diagnosis; the proof gap; the coupled refusal rule; the round's object);
  - `AUDIT_round59_rescaling.md` (rescaling inequalities; candidate defenders; the escape clause);
  - `AUDIT_round59_answers.md` (answers and revised defaults; the zero-sum obstruction; the boxed deliverable).
- **Corrections:** `DESIGN_MEMO.md` §8.27, including its correction bullets.
- **Round 58:** `PP72_rescaling_loop.md`, `PP73_loop_adversary.md`, `REFEREE_round57.md`.
- **Posterior and balanced-field background:**
  - `BRIEF52_posterior_gates.md`;
  - `PP56_kink_translation.md` §4 (u¹, condition (2V), the set R);
  - `PP57_tie_completion.md` §4 (Theorem Q);
  - `PP62_allocation_rule.md` (Theorem E, Cor E.2, Lemma S);
  - `PP66_two_neighbourhood.md`.
- **Framework:**
  - `PP64_extension_principle.md` (partial systems; Theorem 2.3) and `REFEREE_round55.md` (generalised trap; (H_acc));
  - `REFEREE_round54.md` §4 ((C⁺));
  - `AUDIT_completion.md` (rules I–IV); `BRIEF54_refusal_allocation.md` (exact encodings); `LEAD_selection_count.md`; `PP59_hypotheses_ledger.md`.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; the full four-advice domain, with models modulo null sets.
- Ranks: correct 0 < silent 1 < wrong 2 < contradictory 3.
- T = T1 = D_M, with M = c·1 + εΔ, c = (1−ε)/3 and ε = 3/10; vertices v^1, v^2, v^3 of M. T is committed at u.
- **Axioms:**
  - reflexivity; strict (G); (IB); (TC) only;
  - (S): coherent selected models, undominated, competitive on supp p, closed fixed-rival sections;
  - (LA); global (C).
- **Do not:**
  - use approaches equivalent to the CPM realisation problem;
  - make ℓ^m proper.
- **Posterior models.** C_m = D_{M_m}. **Rescaling inequalities:** g ∈ C_m iff Σ_i m_i v_i^α g_i > 0 for α = 1, 2, 3, which is linear in m. Composition is exact: rescaling C_m by b gives C_{m∘b}. This transports geometry and guidance; it does NOT transport verdicts or section proofs.

## The object (audit, binding)
- **H.** Let R be the region where nearby posterior models disagree; off R their common advice is fixed. Let H be the measurable models that give only the common answer h or silence on R and the common advice off R.
  - Every H-model has the same minimal total balanced loss, so no rule of the form "accept iff a zero-sum score is non-negative" can strictly dominate within H (the zero-sum obstruction).
  - The construction must distinguish coherent from incoherent ARRANGEMENTS of advice within H.
- **Representation.** Records in H may be written as error sets: errors removed and errors added, with common errors cancelling. Do NOT assume finite cancellation, additive closure or transitivity. N9.4's "de Finetti cancellation" (A ≤_i B ⟺ A∖B ≤_i B∖A) is just (IB). The record-based formulation stays primary.
- **H is a local test domain, not the old U-domain problem.** Import old results (M0closed, L4, R21, D2/T2n recipes) only individually, with their hypotheses checked. "Blind endorsers are necessary" is not a construction principle.
- **The separating principle concerns COHERENT COMPLETION of advice**, not distance from a threshold or a perturbed score.
  - Compatibility sets: P(X) := {m : C_m agrees with X a.e. on R}, and partial compatibility sets P(X; S) for specified S ⊆ R. Their defining inequalities are explicit.
  - P(X) = ∅ means "not represented by this posterior family", not "incoherent".
  - These sets do not define a ranking. The question is whether incompatible requirements can guide the choice of defender and its necessary refusals.
- **Coupled refusal rule (PROVED by audit; lead checked).** If B ⪯_i X is installed and X ≺_i Y by strict guidance, then Y ⋠_i B (otherwise (TC) demands Y ⪯_i X). Apply this to ALL common-context copies, and say at once how each affected selected source keeps a defence against B.
- **Protection.** Protect T and the coherent models the construction actually needs. Do NOT register every posterior model. Distinguish candidates from committed undominated models. Other coherent models may be dominated.
- **Indices.** Choose them jointly with the relation. Likelihood indexing is a candidate, not a constraint; a posterior parameter describes a model, while a selection index fixes its defence support. The construction must eventually supply a genuine selection with closed fixed-rival sections, and "no section obligation" for committed defenders is NOT allowed. An unsuccessful likelihood-indexed attempt is not a failure of the model family.
- **Scores** are optional witnesses only. Do not keep score-favourable acceptances or a fixed-world ban on null acceptances as invariants unless they are independently necessary.

## Deliverable (audit, binding)
**An operation whose output is:**
- a defender B;
- the required acceptances;
- the required refusals;
- the surviving defence options.

**It must preserve every existing obligation** after:
- common-context copying;
- (TC) with signed propagation;
- section closure, including closure followed by copying (the PP72 gap).

**Further requirements:**
- **Test class:** every incoherent measurable splice X = C[A ↦ D] between committed coherent models, including pure-answer fills, and ultimately every incoherent H-model. Domination is required only when X is incoherent.
- **Works twice:** the second application must handle incoherent measurable splices between a source and its new defender, and between newly committed defenders, with their copies, uniformly over measurable splice sets.
- **Freedom:** different rivals may get different defenders, and competing candidates need not all be installed. Choose defenders according to which joint defence options survive, not by a fixed score, a nearest-model rule or a predetermined path.
- **Escape clause:** if the rescaled candidate set becomes empty, identify the incompatible advice requirements and decide whether ANY coherent credal set satisfies them. That separates posterior geometry from axiom-level obstruction.
- **Insufficient:** extending the two-ray family while leaving pure-answer splices untouched; finite SAT alone (by PP61 Thm C it settles nothing).

## Roles (work CONCURRENTLY; neither half may assume the other will follow)
- **Geometer (PP75):** an explicit CANDIDATE CORRESPONDENCE X ↦ {admissible m}, from compatibility and partial-compatibility sets, the agreement obstruction, and guidance-level necessary conditions implied by coupled refusals. Prove its necessary conditions, describe it for pure-answer fills and for splices between posterior models, and report emptiness cases with the escape-clause analysis.
- **Constructor (PP74):** the operation and the relation. Which additional conditions make a candidate usable, and one record-based rule implementing the operation twice, with proofs of preserved obligations, including section closure followed by copying.
- **Adversary (PP76):** coupled refusals across copies; defence exhaustion at affected sources; section closure followed by copying; the second application; balanced swaps (Theorems Q and E) where their hypotheses hold.
- **Referee (REFEREE_round58):**
  - PP72 Theorem 6.2, especially the section-then-copy step; its Props 3.2 and 4.1; the SAT runs;
  - audit's H argument and zero-sum obstruction;
  - PP73's fill–splice identity and tie-rule conditions (ρ1)–(ρ3);
  - the rescaling inequalities and composition.
