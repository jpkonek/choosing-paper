# Brief, round 33 (17 Oct 2026): strict-slack threshold closure

Read FIRST: AUDIT_DD_slack.md (audit's note "DD1–DD3 Assessment – Strict Budget Slack", with its lemmas) and AUDIT_DD_summary.md.

## Corrections adopted
- **DD2's scope.** DD2's obstruction assumes that comparisons OUTSIDE the seed region stay within finite-seed additive envelopes. So the justified conclusion is only: bounded seeds cannot rescue a system that RETAINS additive structure outside them. Non-additivity need not be conic, and "surround T1's whole boundary" is conjectural.
- **Exact-budget thresholds are impossible.** The everywhere-contradictory model Z forces r_i(Z) = 0 at every world. DD1's frontier and Pexider/homothety results assumed Σ r_i = 1, so they do not constrain the viable construction.

## The construction to attack: STRICT BUDGET SLACK
- Thresholds: C_p ≼_i X ⟺ p_i ≥ r_i(X), with r(C_p) = p, and Σ_i r_i(X) < 1 whenever X is not selected. This is a proposed sufficient condition, not an axiom.
- Transitivity plus exact threshold sections give X ≼_i Y ⇒ r_i(X) ≥ r_i(Y).
- Consequences (audit's lemmas):
  - selected models are automatically protected;
  - every nonselected X is strictly dominated at every world, by C_p with p_i = r_i(X) + (1 − Σ_j r_j(X))/3;
  - competitiveness and closed sections follow from the threshold caps.
- **Closure process.**
  1. Choose initial strict-slack thresholds, with r(C_p) = p fixed.
  2. Install the guidance comparisons, the synchronized seeds, and every comparison required by the caps.
  3. Close under (IB) and transitivity.
  4. Wherever closure forces C_p ≼_i X with p_i < r_i(X), LOWER r_i(X) to the infimum of the forced coordinates, include that endpoint, and repeat.
- Thresholds only decrease, so strict slack for nonselected models survives, limit stages included.
- **Only two failure modes remain:**
  - (F1) a selected model's threshold drops below its prescribed coordinate;
  - (F2) closure produces a strict guidance reversal.
- Do NOT define the ranking by comparing threshold numbers. Keep the LEAST generated relations; incomparabilities are allowed.
- **Decisive theorem:** some initial strict-slack assignment has a closure with neither (F1) nor (F2).
- Keep non-additive comparisons FREE outside the seed cells. Build all three worlds jointly.

## Read
- AUDIT_DD_slack.md and AUDIT_DD_summary.md.
- DD1_notes.md: the patched family (bump placement bounds, necessary condition p¹₁ + p²₂ + p³₃ < 1, nine certificates, commuting squares).
- DD2_notes.md, DD3_referee.md.
- AUDIT_CC_seeds.md and AUDIT_CC_plan.md (synchronized seeds; the coupling warning).
- CC1_notes.md.
- AUDIT_nonlinear_programme.md (transition records).
- writeup §2.

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it.
