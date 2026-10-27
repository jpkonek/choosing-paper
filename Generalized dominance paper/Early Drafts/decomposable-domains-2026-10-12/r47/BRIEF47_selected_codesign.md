# Brief 47: selected-family co-design with incoherence certificates (22 October 2026)

Push for a breakthrough. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- `AUDIT_selected_realizability.md` (audit's note: the additive edge benchmark; the support-sensitive record obligation lemma §4; the co-design problem §5).
- `AUDIT_answers47.md` (audit's answers to the lead's questions; binding guidance for this round).
- `PP23_local_rule.md` §§2–4 (departures; Ω; Lemma 4.3 non-realizability; Lemma 4.4; Theorem 4.5 room reduction; Props 4.6–4.7 and the padding construction; Conjecture 4.9).
- `REFEREE_round46.md` §2.5 (the repaired Props 4.6–4.7: hypotheses P1–P3, steep padding lines, padding mass) and R46.1.
- `AUDIT_completion.md` (closure rules I–IV: copies, triangle completion, protection, tie propagation; failures F1/F2).
- `LEAD_selection_count.md`, `PP18_source_field.md` (Theorem Z), `REFEREE_Z_PP19.md` (Lemma H), `PP19_sections_near_T.md`, `DESIGN_MEMO.md` §8.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain, models modulo null sets. Ranks correct 0 < silent 1 < wrong 2 < contradictory 3. Classes M_1, M_2, M_3 (M_k: world k is the minority sign); U = unanimous problems.
- T = T1 = D_M, M = c·1 + εΔ, c = (1−ε)/3.
- Axioms: reflexivity; strict (G); (IB); (TC) only (equivalently: every accepted triangle has all three reverses); (S): coherent selected C_p on the whole simplex, each undominated, competitive on supp p, every section {p : C_p ⪯_i X} closed for each fixed X; (LA); direct (C). No continuity in measure, no joint continuity, no measurability of verdicts beyond what (IB) and the models give.
- Do not use approaches equivalent to the CPM realisation problem. Do not make ℓ^m proper.

## The exact defence obligation (audit §4)
For a record r = (D, a → b), let P(r) = {p : C_p = a a.e. on D} and A(r) = the set of worlds accepting r. The defence part of (S) is equivalent to: A(r) ∩ supp(p) ≠ ∅ for every r and every p ∈ P(r). Records whose old side is realised only by unselected coherent models carry NO defence obligation. But optional records can still be FORCED by (TC) triangle completion, protection of selected models, (IB) copies, or closed sections.

## Binding guidance from audit's answers
- Leave the geometry near T open. Do not assume continuous motion of credal boundaries, plateaus with jumps, or precise boundary models. Closed sections constrain jumps: if constant models C approach a boundary index p, then C_p ⪯_i C at every world, so C_p and C tie at all worlds when C is undominated.
- A pointwise "sweep" of boundaries does not imply that one selected model realises a two-set pattern (audit's counterexample, path K_t = (1−t)M + t{e_1}, with g = (1,−3/2,−1/2) and h = (1,−1/2,−3/2)).
- In the padding test, what matters is preventing the offending pair from being accepted at the SAME world while all genuine obligations are met. Check ALL decompositions of the repair's reverse, not just Prop 4.7's split.
- T dominates its own inverted rivals: T ⪯_i T·d at every world, for inverted d supported in T's silence.
- Additive comparisons are allowed wherever they help. Do not irrevocably freeze an additive order.
- Unselected coherent models may be dominated, but not through an inverted-departure record (its worse endpoint is incoherent).
- A partial family is acceptable as a construction step only if its index domain and values are explicit, every obligation it generates is included, new defenders are registered and checked, closure cannot force the offending comparisons, and the sections verified are stated precisely. The desired result is a mechanism that keeps working as the family grows.
