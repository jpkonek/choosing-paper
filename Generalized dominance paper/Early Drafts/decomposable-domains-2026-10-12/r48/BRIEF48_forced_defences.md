# Brief 48: forced defences and their replacement dominators, built jointly (22 October 2026)

Aim: a repeatable extension rule that survives adding its own defenders, with a proved invariant. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- `AUDIT_round48_instructions.md` (audit's assessment of round 47 and its instructions; binding).
- `PP30_surgery.md` (Theorem 3.1: the forced defence; Prop 4.2: displaced dominators), `REFEREE_round47.md`.
- `PP28_selected_codesign.md` (separation lemma; certificates on a base; growth rule), `PP29_forced_realisation.md` (retreat split).
- `PP32_additive_barrier.md` (local additive barrier; rank-linear endorsement).
- `AUDIT_completion.md` (closure rules I–IV; F1/F2), `AUDIT_selected_realizability.md` §4 (support-sensitive obligations), `REFEREE_Z_PP19.md` (Lemma H, Prop S), `PP19_sections_near_T.md` (compensation, Theorem 5), `LEAD_selection_count.md`, `DESIGN_MEMO.md` §8.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain, models modulo null sets. Ranks correct 0 < silent 1 < wrong 2 < contradictory 3. Classes M_1, M_2, M_3; U unanimous.
- T = T1 = D_M, M = c·1 + εΔ. Sil(T) = T's silent set.
- Axioms: reflexivity; strict (G); (IB); (TC) only; (S) on the whole simplex (coherent selected C_p, undominated, competitive on supp p, closed fixed-rival sections); (LA); direct (C). No continuity in measure, no joint continuity. Single-world ties allowed.
- Do not use approaches equivalent to the CPM realisation problem. Do not make ℓ^m proper.

## The family (audit; from PP30 Theorem 3.1)
Fix a precise model D_p (start with the vertex models V_1, V_2, V_3) and a bounded measurable G ⊆ Sil(T).
- X := T[G ↦ D_p]. T must defend against X at some world w.
- (IB) then forces R := D_p[G ↦ silence] ⪯_w D_p.
- For non-null E ⊆ G let Z := R with the w-correct answer restored on E. Guidance and (TC) force D_p ⋠_w Z.
- Z is incoherent (Lemma H), so it needs a coherent dominator D_K with D_K ⪯_i Z at every world, while T stays undominated.

## Requirements (audit)
1. Choose the defence world w and the replacement credal set K jointly, by a rule. K genuinely variable.
2. Cover the whole measurable family: all three vertex models, arbitrary admissible G, arbitrarily small E.
3. Register every new defender. Handle its comparisons with T, with other defenders and with their rivals. Check shared disagreement records and mixed triangles across different (G, E).
4. Include sections. State where each new defender is selected and prove the relevant fixed-rival sections closed. Label relative closedness on a partial index domain as such.
5. The fields Ω and |g_w| are optional witnesses only. Freeze neither. Do not require T to dominate every inverted departure; keep only the certificate comparisons actually needed.
