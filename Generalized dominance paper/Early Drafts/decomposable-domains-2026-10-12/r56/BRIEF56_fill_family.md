# Brief 56: explicit co-design for a whole measurable family of fills (23 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- **Audit, ALL BINDING:**
  - `AUDIT_round56.md` (assessment of round 55; signed propagation; accumulation; this round's target);
  - `AUDIT_round55_direction.md`, `AUDIT_round55_answers.md` (the commitment-based formulation).
- **The framework:** `PP64_extension_principle.md`:
  - §1 definitions and invariant 𝓘;
  - Lemma 2.1, Lemma 2.2, Theorem 2.3 (final system);
  - §3 tameness and the settling criterion;
  - §4 the first extension.
- **What is forced:** `PP65_extension_adversary.md`:
  - §2: Lemma 2.1 (edge models equal X_E on E); Prop 2.2 (T's refusals are uniform in E on P_i); Prop 2.3 (the pinned edge defender); Prop 2.4 (the new dominator's forced properties); §2.5 (the switch);
  - §4: Prop 4.1 (the guidance trap); Prop 4.2 (accumulation); Prop 4.3 (revisions).
- **Background:**
  - `PP66_two_neighbourhood.md` (local move; Lemma T);
  - `REFEREE_round54.md` §4 (decreasing-limit lemma; (C⁺));
  - `AUDIT_completion.md` (closure rules I–IV);
  - `LEAD_selection_count.md` (definitions; Lemmas A, B, E);
  - `PP29_forced_realisation.md` (Lemma 3.3);
  - `PP36_joint_rule_search.md` (Lemma E, Prop K);
  - `PP59_hypotheses_ledger.md`;
  - `DESIGN_MEMO.md` §8.23–8.24.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; the full four-advice domain, with models modulo null sets.
- Ranks: correct 0 < silent 1 < wrong 2 < contradictory 3.
- T = T1 = D_M, with M = c·1 + εΔ and c = (1−ε)/3; ε = 3/10 where a number is needed. T is committed at u.
- **Axioms:**
  - reflexivity; strict (G); (IB); (TC) only;
  - (S) on the whole closed simplex: coherent, undominated, competitive on supp p, closed fixed-rival sections;
  - (LA); global (C).
- **Do not:**
  - use approaches equivalent to the CPM realisation problem;
  - make ℓ^m proper;
  - add lexicographic levels;
  - restrict defenders to a family in advance. Any family must be DERIVED.

## Audit's corrections to round 55 (binding)
- PP64's final-system theorem stands only once every index is assigned and every required verdict is settled.
- "The first extension works" overstates what was done. Only a PARTIAL edge defence exists. The off-edge dominator of X_E was shown NECESSARY (by KKM) but was never CONSTRUCTED with its comparisons and reservations, and tameness of the first extension is unproved. So not even one repeatable step has been demonstrated.
- **Signed propagation.** The guidance trap (PP65 Prop 4.1) is caught by propagating forced REFUSALS as well as acceptances. Write a_i = [T ⪯_i D] and b_i = [D ⪯_i X], with D the edge model and X the fill.
  - Guidance and (TC) give ¬a_1 ∨ ¬b_1 and ¬a_2 ∨ ¬b_2.
  - Edge defence gives b_1 ∨ b_2.
  - Hence ¬a_1 ∨ ¬a_2. Once a_1 is accepted, b_1 is refused, b_2 accepted and a_2 refused.
  
  **Invariant requirement:** keep the unresolved defence disjunctions, and propagate BOTH acceptances and refusals forced by (TC), guidance, protection, undominatedness, direct (C) and those disjunctions.
- **Accumulation.** Acceptances at finitely many q_n → p are harmless at each finite stage, but their union forces acceptance at p (closed sections), and that new acceptance can interact with other commitments.
  - PP64's chain-union lemma does NOT settle a strengthened invariant that includes these limit acceptances. Consistency after topological closure at limit stages needs its own proof.
  - At an UNASSIGNED p, a forced limit acceptance is a constraint on whatever coherent model is eventually assigned there. Do not substitute the current provisional model.
- **Revisions.** PP65 Prop 4.3's countability of revisions assumes each revision changes a set with non-empty interior. A dense assigned set blocks further CONTINUOUS revisions, not arbitrary revisions of a discontinuous provisional selection.

## The target of round 56 (audit, binding)
- Fix a region E₀ of T's silence where worlds 1 and 2 agree (so k = 3), with A their common correct answer. Consider X_E := T[E ↦ A] for ALL measurable E ⊆ E₀: arbitrarily small, nested, overlapping and non-conic.
- **Construct, uniformly in E and jointly:**
  - coherent dominators N_E, with explicit formulas or explicit choice rules;
  - their indices p(E);
  - the edge defenders (PP65 Prop 2.3 pins their verdict pattern);
  - the necessary defences and refusals, as signed commitments;
  - reservations that SURVIVE ACCUMULATION, for example as E_n shrink or p(E_n) accumulate.
- **Include the forced rivals that the new defenders generate**, so the difficulty is not just moved elsewhere. For example:
  - fills and partial silencings relative to N_E (N_E[E′ ↦ S], N_E[E′ ↦ A]);
  - T/N_E splices (Prop K);
  - swaps between N_E and N_{E′} for overlapping E, E′;
  - comparisons X_E versus N_{E′};
  - all their (IB) copies.
- **Do not invoke KKM to conclude that a dominator exists. EXHIBIT how to choose it**, and prove that the choices coexist under signed logical closure and closed sections.
- **Success** means a uniform, genuinely recursive co-design operation on a continuum of rivals. A conditional theorem of the form "if every step succeeds, we obtain coverage" does not count.
- State plainly which records remain unassigned at the end of the module.

## Roles
- **Constructor (PP67).** Explicit E ↦ (N_E, p(E), edge defenders, signed commitments, reservations), with proofs:
  - coherence and undominatedness of each N_E;
  - domination of X_E;
  - defence and protection;
  - closed sections, through reservations in index space;
  - (TC) under signed closure;
  - consistency after limit closure.
  
  Also cover the forced rivals of the new defenders.
- **Adversary (PP68).** Attack the same construction:
  - overlapping fills;
  - a SEQUENCE of fills chosen after earlier commitments;
  - accumulation of p(E_n);
  - the forced rivals of the new defenders;
  - signed-closure conflicts, including the guidance trap generalised.
  
  A bare finite module is insufficient.
- **Referee (REFEREE_round55).** PP64 Lemma 2.1, Lemma 2.2, Theorem 2.3 and §4; PP65 Props 2.1–2.4, 4.1–4.3, 5.1; PP66; audit's signed-propagation derivation and revision correction.
