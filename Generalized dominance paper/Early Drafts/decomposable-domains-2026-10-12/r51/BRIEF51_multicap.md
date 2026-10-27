# Brief 51: compatible fields on the multicap family (23 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- `AUDIT_round51.md`, `AUDIT_multicap.md` (the family K_s; the union lemma; the interval criterion; repairs to PP42), `AUDIT_round51_answers.md`. ALL BINDING.
- `PP42_kernel_revision.md` (per-model fields; aggregation "accept iff guidance or some realiser's gate rates positively"; Thm 3.1 (CG2, CG3); Thm 3.2; caps; the section argument; Props 4.4, 5.1, 5.2) and `PP42_py/`.
- `PP43_two_gate_test.md` (gate dominance; Thm 3.4: no Bayes margin over T near T's fibre), `REFEREE_round49.md`, `PP40_adversary_kernel.md`, `PP33_joint_rule.md` (ordinal refusal), `PP36_joint_rule_search.md` (Prop K), `PP30_surgery.md` (forced silence-defences), `AUDIT_completion.md` (closure rules I–IV; F1/F2), `BRIEF49_recursive_milestone.md` (the milestone), `DESIGN_MEMO.md` §8.18–8.19.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain, models modulo null sets. Ranks correct 0 < silent 1 < wrong 2 < contradictory 3. Classes M_1, M_2, M_3; U unanimous.
- T = T1 = D_M, M = c·1 + εΔ, c = (1−ε)/3. Family: for 0 < δ < ε/3 and s ∈ [0, δ]³, K_s = M ∩ {m_i ≤ c + ε − s_i}, C_s = D_{K_s}, C_0 = T. H_i(t) = where the single cut at i differs from T. Union lemma: {C_s ≠ T} = H_1(s_1) ⊔ H_2(s_2) ⊔ H_3(s_3).
- Axioms: reflexivity; strict (G); (IB); (TC) only; (S) (coherent selected models, undominated, competitive on supp p, fixed-rival sections closed); (LA); direct (C). Single-world ties and compositions allowed. No continuity in measure of selected models is assumed.
- Do not use approaches equivalent to the CPM realisation problem. Do not make ℓ^m proper.

## Binding answers from audit
1. **Index map.** Construct fields on the parameter box, and propose an explicit selection from a 2-D neighbourhood of T's index into the box. Check closed sections there for EVERY measurable rival. Do not build in a directional interpretation: the index is not a Bayes weight. If compatibility makes every gated cube member undominated, those members belong to the actual undominated class even if the selection misses them; keep that visible.
2. **T's field may change.** Preserve T's model and the axioms, not ℓ^T's verdicts. T's field is the s = 0 member of the jointly designed family. Continuity is required of the fields' advice-cost DIFFERENCES, with an integrable bound sufficient for the section proof.
3. **Additive gates first.** A failed pair or triple should first prompt changes to:
   - the fields on other corner bands;
   - the supporting weights;
   - the defender or the selected subfamily;
   - the strength of the sufficient compatibility test.
   
   Failure of strict CG3 does not prove failure of (TC): check whether the offending records actually form a forbidden configuration. A lexicographic branch is allowed only as a separately labelled branch with its own proofs.
4. **Supporting weights λ_s vary freely** (distinct from the index p). For an interior index any probability weight is allowed, including boundary weights. There is no required direction. Positive rescaling of a world's whole field preserves the gate's verdicts: normalise with it.
5. **Repair class.** Fills, retreats and improved retreats for all members in scope, on arbitrary bounded measurable sets including arbitrarily small ones. Explicit domination is required only for nontrivial incoherent modifications. Also include a simultaneous two-corner modification X = T[G_i ↦ C_s, G_j ↦ C_t], with disjoint G_i, G_j in different corner bands. Vertex rivals and the edge are deferred. Universal competitiveness of every registered member against ALL measurable rivals is NOT deferred.

## Common first checkpoint (all agents)
T, two single caps (cuts at vertices i ≠ j), and their combined cut, with the simultaneous two-corner rival included. Then the eight-model box. The deliverable is a formula or extension mechanism valid for an open range of cut sizes, not feasible fields at sampled models. If it fails, say whether the obstruction comes from:
- the axioms;
- the gate-union architecture;
- the stronger sufficient compatibility test.
