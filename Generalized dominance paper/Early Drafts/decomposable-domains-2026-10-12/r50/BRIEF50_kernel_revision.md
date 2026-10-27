# Brief 50: revise the bounded kernel together with the defenders (23 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- `AUDIT_round50.md`: audit's assessment and instructions. BINDING.
- `BRIEF49_recursive_milestone.md` (the milestone; still binding), `AUDIT_round49_brief.md`, `AUDIT_round49_answers.md`.
- `PP38_bounded_kernel.md` (kernel ℓ^T; Thm 3.1: kernel acceptance forces registered models to be ℓ^T-Bayes, so only T, B_ij(t), V_k), `PP40_adversary_kernel.md` (shadow condition; jump facts; splice Prop K), `PP41_kernel_completion.md` (Thm 2.4 and its exact hypotheses; gates), `PP37_recursive_milestone.md` (support-gated potentials; ties against sections; iso-level), `PP33_joint_rule.md` (Thm 3.1: ORDINAL refusal; the budget of Cor 3.2 is optional), `PP36_joint_rule_search.md` (Prop K), `REFEREE_round48.md`, `REFEREE_PP32_penalties.md`, `PP30_surgery.md` (Thm 3.1: forced silence-defences), `AUDIT_completion.md` (closure rules I–IV; F1/F2), `LEAD_selection_count.md`, `DESIGN_MEMO.md` §8.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain, models modulo null sets. Ranks correct 0 < silent 1 < wrong 2 < contradictory 3. Classes M_1, M_2, M_3; U unanimous.
- T = T1 = D_M, M = c·1 + εΔ; Sil(T) = T's silent set.
- Axioms: reflexivity; strict (G); (IB); (TC) only (accepted triangles need all reverses); (S): coherent selected models, undominated, competitive on supp p, fixed-rival sections closed; (LA); direct (C). Single-world ties and compositions allowed. No continuity in measure of the selected models.
- Do not use approaches equivalent to the CPM realisation problem. Do not make ℓ^m proper.

## Audit's corrections to the lead's round-49 summary
- "The jump is the crux" holds only AFTER fixing PP38's kernel. The kernel's restriction to ℓ^T-Bayes models is what forces the jump and the shortage of dominators.
- PP41 Thm 2.4 holds only under its exact hypotheses: the kernel, a post-jump family matching the milestone edge, the installed-record restriction, and the valuation assumptions.
- PP41's hypothesis (NA) is impossible as written. Values of bounded records are uniformly bounded by an integrable envelope, so they cannot fill an open half-space. Prop 3.4′ and Prop 2.8's dependence on it are unresolved.
- PP41 Prop 4.1(b) does not give direct (C) for a union of gates: other gates can accept the reverse comparisons.
- Any refusal is a GLOBAL verdict on a disagreement record. State the aggregation rule across gates explicitly.
