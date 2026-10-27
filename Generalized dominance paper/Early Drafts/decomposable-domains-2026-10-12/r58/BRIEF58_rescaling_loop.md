# Brief 58: mixed-class repair on the exact rescaling loop (24 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- **Audit, ALL BINDING:**
  - `AUDIT_round58.md` (organise by repair class; the forced pattern; mixed-class recurrence; success and failure criteria);
  - `AUDIT_round58_answers.md` (corrections; the exact rescaling loop; defence via a joint record-based relation; scope).
- **Corrections:** `DESIGN_MEMO.md` §8.25–§8.26, including the correction bullets at the end of each.
- **The posterior family, where the loop lives:**
  - `BRIEF52_posterior_gates.md` (C_a = D_{M_a}, M_a = {a∘p/(a·p) : p ∈ M}; the pair-ordering theorem);
  - `PP57_tie_completion.md` §4 (Lemma 4.1 pure likelihood shifts; Theorem Q);
  - `PP62_allocation_rule.md` (Theorem R, rule R₀; Theorem E, endorsement + closed sections fails at interior members with balanced member swaps; Cor E.2; Lemma S);
  - `PP56_kink_translation.md` §4 (Theorem L, balanced field u¹, condition (2V));
  - `PP63_allocation_adversary.md` (Lemma 3.1 single-world incomparability; Lemma 4.1 refusal spreading; Theorem J);
  - `PP66_two_neighbourhood.md` (local move);
  - `REFEREE_round53.md`, `REFEREE_round54.md` (scopes, (C⁺)).
- **Framework and module results:**
  - `PP64_extension_principle.md` (partial systems; Theorem 2.3) and `REFEREE_round55.md` (generalised trap; (H_acc));
  - `PP67_fill_family.md`, `PP68_fill_adversary.md`, `REFEREE_round56.md` (Theorem R: L₀ dominates all class-3 fills of N);
  - `PP69_two_direction.md`, `PP70_two_direction_adversary.md`, `PP71_recurrent_repair.md`: use only with the rescoping below;
  - `AUDIT_completion.md` (rules I–IV); `BRIEF54_refusal_allocation.md` (exact encodings); `LEAD_selection_count.md`; `PP59_hypotheses_ledger.md`.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; the full four-advice domain, with models modulo null sets.
- Ranks: correct 0 < silent 1 < wrong 2 < contradictory 3.
- T = T1 = D_M, with M = c·1 + εΔ and c = (1−ε)/3; ε = 3/10. T is at u.
- **Axioms:**
  - reflexivity; strict (G); (IB); (TC) only;
  - (S): coherent, undominated, competitive on supp p, closed fixed-rival sections;
  - (LA); global (C).
- **Do not:**
  - use approaches equivalent to the CPM realisation problem;
  - make ℓ^m proper.

## Rescoping of earlier results (audit, binding)
- PP70 Prop 1.5 (thin-fill repairs approach the source) holds only for in-family repairs on that curve.
- PP69's convergence assumes an additive certificate and a unique interior Bayes optimum. Neither is axiom-level.
- A repair's class does not determine the direction of its index.
- PP71 Thm 2.4 and Cor 2.5 (infinite chains, non-transitivity) need SAME-CLASS cycles and continuing silence.
- Off-curve accumulation is not a "two-dimensional sheet".
- **Score-patching exclusions (PP71 Props 2.6–2.7):** distinguish PRESERVING an entire score order from USING scores as witnesses for particular comparisons.

## Structural facts (binding; lead checked)
- **Forced pattern.** If B dominates a class-k fill of an interior selected C, then C ⋠_i B for i ≠ k (by (TC) + guidance + strict (G)) and C ⪯_k B (by C's defence). So one ordered pair (C, B) cannot repair fills of two classes, and a source with silence in all three classes needs at least three distinct repairers.
- **Agreement obstruction.** A proposed dominator cannot agree with the fill everywhere on its modified set ((IB) + protection + (C) + non-conicity). The repair's scale must depend on the rival.
- **No member of the round-57 curve dominates T's class-1 or class-2 fills.** New coherent models are necessary.
- **Mixed-class toy.** Losses (0,0,0), (−1,−1,2), (1,−2,1) realise the source-to-defender verdicts of a 3 → 1 → 2 cycle under transitive comparisons. This is consistency among SOURCES only, not a repair construction.

## The exact rescaling loop (audit, binding as the starting geometry)
- For a > 1, let d₃ = (a, a, a⁻²), d₁ = (a⁻², a, a) and d₂ = (a, a⁻², a), whose product is (1,1,1).
- Indices: m₀ = u, m₁ ∝ d₃, m₂ ∝ d₁∘d₃, m₃ ∝ d₂∘d₁∘d₃ = u.
- The scaled coherent models are the posterior models C_{m}.
- **By guidance (pure likelihood moves, PP57 Lemma 4.1 inverted):** C_{m₀} ⪯₃ C_{m₁}, C_{m₁} ⪯₁ C_{m₂} and C_{m₂} ⪯₂ C_{m₀}. These are exactly the defending acceptances the forced pattern requires for repairs of class 3, then class 1, then class 2.
- **NOT established:**
  - the refusals at the other two worlds;
  - the domination records (C_{m₁} dominating a class-3 fill of C_{m₀}, and so on);
  - their coexistence.
- **Freedoms to keep:**
  - the scale a (and the loop shape) chosen WITH the rival;
  - longer loops, branches, revisable candidate choices before commitment;
  - repairs outside the local family if necessary, with their obligations accounted for.

**Warning: the loop lives in the posterior neighbourhood of u.** Theorems Q and E constrain relations there.
- **Theorem Q:** containing the strict part of one additive field, together with a null member swap, is incompatible with closed sections.
- **Theorem E:** member acceptances endorsed by u¹, together with a balanced member swap at an interior member, are incompatible with closed sections.

Check whether their hypotheses apply to your relation; the loop members have member-to-member balanced swaps.

## Deliverable (audit, binding)
> Start with the exact rescaling loop. Choose its scale and the fill-domination records jointly. Establish ONE relation supporting a non-isolated family of such repairs, with universal defence, protection, all measurable copies, and closed fixed-rival sections. Permit additional branches and coherent defenders when the loop alone cannot handle a splice.

- **The relation is a joint RECORD-BASED relation.** Scores may witness particular comparisons. Using a score to supply EVERY favourable comparison is a substantial commitment, subject to the no-patching result. Different scores for different disagreements are allowed as a candidate, but (IB), (TC), protection and sections must be proved for the resulting rule. Closing each fixed-rival section does not make score gluing safe, because mixed triangles can draw comparisons from different pieces.
- **Defence obligations stay disjunctive.** Do not assign a defending world merely because a score favours it.
- **Universal defence.** EVERY installed coherent model is defended against EVERY measurable rival, jointly, and protected.
- **Sections:** the source indices are the constructed local family, including its accumulation points; rivals range over the full measurable domain. This is a local extension result, not full (S).
- **Domination** may be limited to the specified families:
  - fills of each loop member in all three classes, all measurable and arbitrarily small;
  - ALL measurable splices between installed models, especially consecutive loop members, with their common-context copies.
  - Keep T/N_k splices only if the N_k are retained. Do not register extra models just to enlarge the test.
  - Loop members need not dominate every splice themselves: new coherent defenders remain available.
- **Each proposed repair B(C, E) must address:**
  - overlapping and nested E;
  - all copies;
  - two repairs whose records compose;
  - a repair followed by a defence comparison;
  - the SAME rival compared with nearby selected sources.
- Propagate both acceptances and refusals of (TC). Unassigned is not refused.
- **Success:** one mixed-class measurable repair mechanism handling the rivals generated by its own defenders, with universal defence, protection, (IB), (TC) and closed sections on a non-isolated family.
- **Useful failure:** a proof that the mixed-class obligations themselves conflict, with no additive certificate, fixed successor, symmetry or guidance-worsening assumption doing the work.
- **Insufficient:** another finite cycle; another curve without its other-class rivals; another conditional theorem.

## Roles
- **Constructor (PP72):** the joint relation on the rescaling-loop family, with proofs.
- **Adversary (PP73):** first, two adjacent repair edges plus one splice; then a fixed rival approached along two branches, testing for an incoherent all-world tie in the limit; then Theorems Q and E on loop members' balanced swaps; then the rivals generated by the defenders.
- **Referee (REFEREE_round57):** PP69, PP70, PP71 under the rescoping above; the forced pattern; the curve exclusion; the rescaling loop's guidance claims.
