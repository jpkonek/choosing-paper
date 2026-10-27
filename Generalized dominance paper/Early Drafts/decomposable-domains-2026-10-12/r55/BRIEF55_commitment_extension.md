# Brief 55: a commitment-based global extension principle (23 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- **Audit, ALL BINDING:**
  - `AUDIT_round55_direction.md` (change of direction: global compatibility is the central problem);
  - `AUDIT_round55_answers.md` (the formulation used below).
- **Definitions of the axioms:**
  - `LEAD_selection_count.md` §1 (definitions of (S), strict (G), all-world tie, undominated; Lemma B; the edge argument);
  - `AUDIT_completion.md` (closure rules I–IV; registered and protected models; how direct (C) is discharged globally);
  - `BRIEF54_refusal_allocation.md` (exact encodings of defence, undominatedness and direct (C)).
- **What round 54 established:** `DESIGN_MEMO.md` §8.23. Then, as needed:
  - `PP62_allocation_rule.md` (Theorems R, P, E; Cor E.2; Lemma S);
  - `PP63_allocation_adversary.md` (Lemma 3.1: single-world incomparability is safe; Lemma 4.1: refusal spreading; Theorem J; Prop 2.1: a false identification to avoid);
  - `PP61_joint_refusals.md` (Theorem C: finite or countable instances fixed in advance carry no obstruction);
  - `REFEREE_round53.md` (§6 alternative theorem and Prop A″; §7 ledger);
  - `PP57_tie_completion.md` §4 (Theorem Q).
- **Ledger:** `PP59_hypotheses_ledger.md`.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; the full four-advice domain, with models modulo null sets.
- Ranks: correct 0 < silent 1 < wrong 2 < contradictory 3.
- T = T1 = D_M, with M = c·1 + εΔ and c = (1−ε)/3; take ε = 3/10 where a number is needed.
- **Axioms:**
  - reflexivity; strict (G); (IB); (TC) only (single-world ties and incomparability allowed);
  - (S) on the WHOLE closed simplex Δ: coherent selected models, undominated, competitive on supp p, closed fixed-rival sections;
  - (LA); (C) globally.
- **Do not:**
  - use approaches equivalent to the CPM realisation problem;
  - make ℓ^m proper;
  - add lexicographic levels.

## The formulation (audit, binding)
**A partial system Σ consists of:**
- a fixed index simplex Δ with a partially assigned selection. Once C_p is committed it stays fixed. The target T is committed at a specified interior index; use u = (1/3, 1/3, 1/3) unless you justify otherwise.
- committed comparisons: records with a committed verdict at a world. Equal records are identified immediately ((IB)). Guidance is mandatory.
- **refusal reservations.** A committed refusal at (p, X, i) carries an open neighbourhood U ∋ p, and EVERY future assignment C_q with q ∈ U must satisfy C_q ⋠_i X. Reservations constrain indices whose models are not yet chosen.
- pending obligations, kept as explicit DISJUNCTIONS: defence of each committed model on its support; protection of T; undominatedness; direct (C); face restrictions. Obligations at unassigned indices are recorded and never deferred.
- **provisional choices** may be revised. **Commitments** (committed comparisons, committed models, reservations) may not.

**Unassigned is not refused.** Unknown comparisons stay unassigned, never defaulted to refusal or filled by an additive score.

**An extension step** may:
- assign a coherent model at an unassigned index (the DEFENDER IS AN OUTPUT; no cap, posterior or edge restriction unless derived);
- settle unassigned records;
- commit a refusal neighbourhood;
- resolve a defence obligation at an available world.

Before a step is accepted, check its consequences for existing commitments through (IB) copies, (TC) and closure rules I–IV.

**Final system and sections.** If every index and every comparison is eventually assigned and every refusal carries a reservation, then each fixed-rival refusal set is open, so sections are closed. This must be built into the invariant; it is not a final continuity argument.

**Limit cautions (audit):**
- A decreasing intersection of relations under a fixed selection preserves (G), (IB), (TC), closed sections, support defence (when it holds at every stage) and undominatedness of models protected at every stage.
- It does NOT automatically give global (C). A coherent model can become undominated only at the limit, with tie partners never constrained before. Stages that fail (C) are not repaired by the limit.
- "Each verdict changes only finitely often" does NOT give closed sections. Counterexample: [1/n, 1] → (0, 1].
- Transfinite constructions (using choice) are acceptable, but a well-ordering is only bookkeeping. The content must be the extension lemma, with a SUBSTANTIVE, checkable hypothesis (not "the partial system is extendible"), and the preservation argument.

## The first nontrivial extension (audit, binding)
> Starting with T and a small set of genuine commitments, introduce a rival that requires a new coherent defender. Choose that defender and its index jointly, establish its defence and protection obligations, and commit the refusal neighbourhoods needed at both T and the new defender, without exhausting any face-defence obligation.

**Default instance (lead's reading; replace it if you find a better one, and say why).** Take an edge {i, j} and a non-null set E where T is silent and worlds i and j agree. Let X_E := T[E ↦ that common answer].
- By strict (G), X_E ≺_i T and X_E ≺_j T, so T is not competitive at any index supported on {i, j} (LEAD Lemma, edge argument). An edge index needs a NEW defender.
- T's refusals T ⋠_i X_E and T ⋠_j X_E are forced. With reservations, every future C_q with q near u must refuse X_E at i and j, so near u the defence against X_E must come from the third world k.
- Somewhere between u and the edge the defending world must switch, with closed acceptance sets and open refusal sets. Determine the joint choice of defender and index, the reservations at T and at the new defender, and whether face-defence obligations survive.
- Then the adversarial instance: the balanced-swap configuration of Theorems Q and E, treated as an instance of this step.

## Two-neighbourhood rejection test (audit; small diagnostic only)
- Choose a non-conic swap between two interior selected models: X = C_a[F ↦ C_b] and Y = C_b[F ↦ C_a].
- Require the SAME world w to refuse C_p ⪯_w X throughout an open neighbourhood of a, and C_q ⪯_w Y throughout an open neighbourhood of b.
- At the centres these are inverse records, refused at one world, so no common reweighting certifies them (α = (1,1)).
- Keep universal defence, protection, (G), (IB) and (TC).
- Use it to REJECT extension proposals quickly. It is not a programme.

## Success criterion (audit)
Does the mechanism explain how to handle the next ARBITRARY rival without sacrificing earlier obligations, and how to pass to the final system? If it does not, it is another module, however elegant. Exclusions of further scoring architectures are not progress toward an impossibility result and should not be described that way.

## Roles
- **Constructor (PP64):** write down the partial-system definition, the invariant, the extension operation, the substantive hypothesis of the extension lemma, and the limit argument (including how global (C) is discharged) BEFORE large calculations. Then attempt the first nontrivial extension.
- **Adversary (PP65):** attack the operation at its first nontrivial extension with the existing swap, splice and guidance traps, reservations exhausting coherent models or defending worlds, and face obligations. Not another finite table.
- **Diagnostic (PP66):** the two-neighbourhood test; small.
- **Referee (REFEREE_round54):** the round-54 results and the decreasing-limit lemma with audit's qualifications.
