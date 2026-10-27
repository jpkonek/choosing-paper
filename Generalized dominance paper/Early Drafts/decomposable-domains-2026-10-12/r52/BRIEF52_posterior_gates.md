# Brief 52: the posterior family, whole simplex, and no global prices (23 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- `AUDIT_round52.md`, `AUDIT_posterior_pairs.md` (the posterior family; the pair-ordering theorem), `AUDIT_round52_answers.md`. ALL BINDING.
- Gate architecture and tools:
  - `PP42_kernel_revision.md` (per-model fields; CG2, CG3; Thm 3.2);
  - `REFEREE_round50.md` (Thm R1; Lemma S, the section lemma; repairs);
  - `PP47_multicap_adversary.md` (Thm 4.1, the zero-accepting (TC) test under strict CG2; Thm 2.5);
  - `PP45_multicap_fields.md` and `PP46_multicap_computation.md` (Lemma 2.1 / A0: the pair Bayes + CG2 condition gives one vector D; the combined-cut obstruction; the star fields).
- Background:
  - `LEAD_selection_count.md` (Lemmas A, B, E; Theorem C);
  - `AUDIT_completion.md` (closure rules I–IV; F1/F2);
  - `REFEREE_PP32_penalties.md` (single general fields cannot select T1: Contamination Triangle main theorem, Q4.2);
  - `PP12_equivariance.md` (Theorem E; rival Λ);
  - `DESIGN_MEMO.md` §8.11, §8.20.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain, models modulo null sets. Ranks correct 0 < silent 1 < wrong 2 < contradictory 3.
- T = T1 = D_M, M = c·1 + εΔ, c = (1−ε)/3.
- **Posterior family.** For a ∈ Δ, M_a = {a∘p/(a·p) : p ∈ M}, C_a = D_{M_a}. C_u = T; C_{e_i} = V_i; boundary indices give models on the corresponding face.
- **Pair-ordering theorem.** For interior a, b, the single vector D = log(a/b) certifies every disagreement.
- Axioms: reflexivity; strict (G); (IB); (TC) only; (S) on the whole simplex (coherent selected models, undominated, competitive on supp p, fixed-rival sections closed); (LA); direct (C). Single-world ties and compositions allowed.
- Do not use approaches equivalent to the CPM realisation problem. Do not make ℓ^m proper.

## Binding commitments for this attempt (audit)
- **Selection.** Index = likelihood: a ↦ C_a on the whole simplex, boundary included.
- **What is not imposed.**
  - λ_a = a is NOT imposed; supporting weights are separate.
  - No rescaling invariance of the rankings.
  - Fields need not be transported copies of T's field.
- **Failures.** Report a failure as a failure of this architecture and family, not of co-design generally.
- **Repairs.** If the consolidated reduction holds, KKM plus the dominance theorem supply dominators, and explicit repairs are only adversarial tests.
- **Sections.** For a fixed rival X, let F_i(X) = {(a, b) : C_b agrees with C_a wherever C_a ≠ X, and Φ_i^b(C_a, X) ≥ 0}. With continuity in measure, L¹-continuous fields and a common envelope, F_i(X) is closed. Projecting over the compact realiser parameter b gives a closed section. This handles changing realisers along a sequence.
- **Interval widths.** Do NOT require a uniform lower bound on interval widths. The decisive target is gates whose pair constraints are feasible on every triple but INFEASIBLE on some larger finite collection, so that there are no global prices.
  - Abstract pattern: x_B − x_A, x_C − x_B, x_D − x_C, x_A − x_D each in [1, 2], with the diagonals in [−4, 4].
  - Every triple is feasible with slack; the four together are not.
- **Boundary from the outset.** Test edge-support competitiveness, fixed-rival limits approaching an edge and a vertex, and compactness of the realisers.
