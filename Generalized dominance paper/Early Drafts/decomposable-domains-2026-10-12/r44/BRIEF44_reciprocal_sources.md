# Brief 44: reciprocal source protection and (S) (22 October 2026)

This round aims at a construction or an exact obstruction. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; if you need one, name it as a hypothesis. Keep each note under about 10 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- `AUDIT_six_source.md`: audit's new note. Main results are sections 9–14 (three-source and six-source extensions, reciprocal source defences, non-endorsement at every world). Audit's finite checks: `AUDIT_reciprocal_py/`.
- `LEAD_selection_count.md`: lead's lemmas on how many selected models (S) needs (not yet refereed).
- `DESIGN_MEMO.md` §8 (especially §8.5 on S10/S11, §8.10 on J1, §8.11 the rescaled family and Theorem E, §8.12 the guard construction and Theorems B and O).
- As needed: `PP15_guard_changing.md`, `PP16_selection_architecture.md`, `REFEREE_guard.md`, `PP2_weakgate_obstruction.md`, `PP12_equivariance.md`, `gate2d/Separation-Gated-Evaluators.tex`.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ (only its null sets matter); full four-advice domain, models modulo null sets. Ranks good 0 < silent 1 < bad 2 < contradictory 3.
- Target T = T1 = D_M, M = c·1 + εΔ, c = (1−ε)/3, 0 < ε < 1.
- Axioms: reflexivity; strict (G); (IB) (verdicts depend only on the disagreement record, so whole record classes are accepted or refused together); (TC) only: A ⪯ B ⪯ C implies not C ≺ A (no transitivity); (S): coherent selected C_p, each undominated, competitive on supp p (for every X some w ∈ supp p has C_p ⪯_w X), and every section {p : C_p ⪯_w X} closed for each fixed X; (LA); direct (C).
- Do not use approaches equivalent to the CPM realisation problem. Do not make ℓ^m proper.

## What is known (check what you use)
- Fixed priority keys with weak gates fail in three worlds (PP2 Thm 6, refereed). J1: nested-window selections cannot have closed accepted-record sets in the rival argument. The rescaled (posterior) family is one diagonal orbit; equivariant rankings fail (Theorem E, rival Λ). The guard construction with T selected is closed off (Theorems B, O).
- No (TC) engine has failed on (TC) itself. Every failure so far has been in (S): defence (competitiveness) and KKM dominators.
- Audit §1: if X is strictly better than T at world i by guidance and C dominates X, then T ⪯_i C is impossible. So the dominator of a rival that helps worlds 1 and 2 must be beaten by T at world 3.
- Lead (LEAD_selection_count.md): (S) cannot be met with finitely many selected models; with no all-world ties it needs uncountably many, each fibre closed; private witness sets of audit's kind can protect only countably many sources.
