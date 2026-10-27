# Brief 38: the allocation problem in three worlds (20 October 2026, night)

This is still the mechanism-design phase: short screening results, exact computations, short proofs. Each note should run to about 8 pages at most. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions.

## Read first
- `AUDIT_anchor_plan.md`: audit's plan. It covers the family K_p = p + 3ε min_j p_j (Δ − u), the anchor sets A(d), the seven face obligations, the eligible pool Φ_i = 2ν(P_i) − ν(Q_i), the greedy rule that fails, and its diagnostic triple near e_1.
- `DESIGN_MEMO.md` §8 (in particular §8.5 and §8.6).
- `PP4_triple_screen.md`: (TC) on swaps, the triangle condition, and opposite majority orders.
- `PP2_weakgate_obstruction.md` and `REFEREE_PP2.md`: the KKM mechanism behind S11.

## Lead's reading of the plan
1. With priority orders chosen per directed record, the gate imposes nothing: it passes exactly when the record is assigned. So the design is an *allocation* W(d) plus the verdicts Φ_i. (TC) is no longer automatic and must be imposed directly.
2. The reduction of the defence clause of (S) to seven closed face obligations is correct. For each record d and each face I that the anchor set A(d) meets, W(d) must meet I.
3. Closed sections follow if the accepted record sets R_i are closed and p ↦ rec(C_p, X) is continuous.

Axioms: reflexivity; strict (G); (IB); (TC) only; (S), meaning coherent selected models, each undominated, competitive on supp p, with closed sections; (LA); direct (C). Full four-advice domain, Gaussian measure on R³.

All paths are relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/.
