# Brief 57: two-direction, rival-sensitive repairs on a non-isolated family (24 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- **Audit, ALL BINDING:**
  - `AUDIT_round57.md` (assessment of round 56; the path obstruction; guidance closure is optional);
  - `AUDIT_round57_two_direction.md` (fill repairs F_t with thresholds τ; retreat repairs R_α with thresholds σ; the vacuity correction);
  - `AUDIT_round57_answers.md` (answers that fix this round's scope and criterion).
- **Starting module:**
  - `PP67_fill_family.md` (T, N = D_{K_N}, K_N = conv(M ∪ M₀), D* = D_{M₀} at (½, ½, 0); signed closure; certificate Theorem 4.1);
  - `PP68_fill_adversary.md` (forced structure §1; checks §2; L₀ = D_{conv(v₃, M₀)}; edge lemma and cycle results §4).
  - Read both with the corrections in `DESIGN_MEMO.md` §8.25 (end of section).
- **Framework:**
  - `PP64_extension_principle.md` (partial systems; invariant; Lemma 2.1; Theorem 2.3);
  - `REFEREE_round55.md` (generalised trap; accumulation counterexample; (H_acc) theorem);
  - `REFEREE_round54.md` §4 ((C⁺));
  - `AUDIT_completion.md` (rules I–IV);
  - `BRIEF54_refusal_allocation.md` (exact encodings);
  - `LEAD_selection_count.md`;
  - `PP59_hypotheses_ledger.md`.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; the full four-advice domain, with models modulo null sets.
- Ranks: correct 0 < silent 1 < wrong 2 < contradictory 3.
- T = T1 = D_M, with M = c·1 + εΔ and c = (1−ε)/3; ε = 3/10, so v₃ = (7, 7, 16)/30.
- **Axioms:**
  - reflexivity; strict (G); (IB); (TC) only;
  - (S) on the whole closed simplex: coherent, undominated, competitive on supp p, closed fixed-rival sections;
  - (LA); global (C).
- **Do not:**
  - use approaches equivalent to the CPM realisation problem;
  - make ℓ^m proper.
- Additive or lexicographic PROOF DEVICES are allowed. Every imported exclusion (Theorems Q, E, J, Prop 7.4, …) must be checked against its exact hypotheses before it is used. A certificate without closed sections can establish consistency of commitments, but not the sections of the constructed system.

## Corrections from audit (binding)
- **Keeping the present N keeps T ⪯₃ N as guidance.** Guidance status is fixed by the two models' advice. What is dropped is the requirement that EVERY FUTURE repair be guidance-worse at its designated world.
- **Bridge.** R₁ = N but F₀ = L₀ ≠ N. Use J_β = D_{(1−β)K_N + βK_{L₀}}, 0 ≤ β ≤ 1, where K_{L₀} = conv(v₃, M₀) ⊆ K_N. The candidate curve is T →(R_α)→ N →(J_β)→ L₀ →(F_t)→ D*, with
  - K_α = (1−α)M + αK_N, R_α = D_{K_α};
  - F_t = D_{conv(v_t, M₀)}, v_t = (1−t)v₃ + t(½, ½, 0).
  
  This is GEOMETRY ONLY. No defence or domination follows from it.
- **Splices.** For L = {T ≠ N}: N[H ↦ T] = T[L∖H ↦ N]. Retreats and restorations are ONE family; handle all measurable subsets of L once.
- **"Every repair is mixed at every world" is unchecked.** Verify gains and losses world by world for each rival class.
- **Path obstruction.** A fixed later member cannot dominate a fill on which it agrees with the fill everywhere ((IB) + protection + (C) + non-conicity). Repairs must depend on the rival.
- **PP67 Prop 7.1, retreat half: vacuous** (P₁ ∪ P₂ = L). The fill half stands.
- **PP68 Prop 4.7(b): wrong** (reversed comparison). PP68 §1(b) stands under its hypothesis: the same fixed rival served by later dominators.
- **Increasing parameters need not converge to 1** without a further argument.

## Audit's candidate windows (binding as candidates, not as architecture)
- **Fill repairs (class 3).** For a fill Y_E = N[E ↦ majority] with E inside the common silence of N and F₀:
  - each problem g has a switching threshold τ(g) ∈ (0, 1), with F_t silent before it and answering after it;
  - choose t from the distribution of τ on the actual E. For example, a t between its quartiles answers on at least a quarter of E and is silent on at least a quarter.
  - Keep the WHOLE window available while checking relational constraints.
  - Recurrence: for fills of F_s the thresholds exceed s.
- **Splice repairs.** For Z_H = T[H ↦ S], H ⊆ L:
  - R_α has thresholds σ(g) on L;
  - if Z_H is incoherent, some α restores T's answer on a non-null part of H and withdraws it on a non-null part of L∖H. Otherwise H is a threshold cut.
- **Other classes.** The F_t window addresses class-3 fills only. Fills of N in classes 1 and 2 may need different coherent candidates.

## Target: a successful extension milestone (audit, binding)
**Theorem to aim for.** For every source in a specified NON-ISOLATED family and every rival in the stated measurable classes, there is an admissible repair in the family, and all those choices coexist in ONE relation (or one partial commitment system) such that:
- every registered model (T, all repairs, all selected models in the family) is defended against EVERY measurable rival, is protected, and has CLOSED FIXED-RIVAL SECTIONS along its assigned indices;
- each chosen repair dominates its rival;
- (G), (IB) with all copies, (TC) and global (C) hold for the registered models, together with signed closure;
- mixed triangles combining a fill repair and a splice repair are handled.

**Further requirements:**
- **Joint choice:** one system of repair parameters and verdicts. NOT a relation supporting every parameter in the windows.
- **Rival classes:**
  - N's fills in ALL THREE classes;
  - all measurable T/N splices;
  - the cross-class and common-context copies generated by installed comparisons;
  - plus the analogous rivals of the new sources, for ONE genuinely repeatable step: every source in the non-isolated family, not just N.
- **Revisable:** everything optional from round 56, including N, its index, D*'s edge placement, mutual-defence commitments and reservation choices. Use RIVAL-DEPENDENT reservation neighbourhoods; do not keep fixed balls unless the tie plateaus they force are wanted. Preserve T at u and the axioms.
- **Endpoint.** Index placement is chosen jointly with the relation; the segment from u to (½, ½, 0) is one candidate. If the family includes the edge endpoint, its sections must be checked there. Otherwise label the result an INTERIOR construction and leave endpoint extension open.
- **Partial success:** the same simultaneous theorem for fills alone or splices alone, with a non-isolated source family, all measurable rivals in that class, and genuine section proofs. Finite model collections, isolated indices, or separate relations for separate rivals fall short.

## Roles
- **Constructor (PP69):** the joint choice and relation, with proofs, aiming at the milestone.
- **Adversary (PP70):** mixed fill/splice triangles; (IB) copies; fixed-rival sections along the non-isolated family, including where rival-dependent reservations meet; defence against every measurable rival at the new sources; other-class fills; signed-closure traps, generalised; accumulation. Attacks must be uniform or adaptive, not a finite table.
- **Alternative (PP71):** recurrent repair among four or more coherent models. Repairs RETURN to previously used models through non-guidance comparisons, while handling entire measurable rival families. A four-cycle among selected models alone is not informative. Keep the effort moderate.
- **Referee (REFEREE_round56):** PP67, PP68, and audit's geometric claims (path obstruction, vacuity, thresholds τ and σ, quartile window, splice identity, bridge J_β, recurrence of thresholds).
