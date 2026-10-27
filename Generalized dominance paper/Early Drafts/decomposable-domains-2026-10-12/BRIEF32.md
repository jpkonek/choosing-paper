# Brief, round 40 (18 Oct 2026, 21:00): quorum rankings

Read FIRST: AUDIT_quorum.md (audit's construction, proofs and certificate) and AUDIT_quorum_summary.md.

## The class
- **Judges.** At each world i there are n judges v with integrable, strictly guiding additive losses ℓ_iv(h, a): strictly increasing in world-i rank, good < silence < bad < contradiction. Write
  - L_iv(X) = ∫ ℓ_iv(h, a_X(h)) dμ;
  - d_iv(X,Y) = ∫ |ℓ_iv(h, a_Y) − ℓ_iv(h, a_X)| dμ.
- **Votes.** Judge v supports X R_i Y iff L_iv(Y) − L_iv(X) ≥ η d_iv(X,Y), with 0 < η < 1.
- **Quorum.** Accept X R_i Y iff at least q judges support it. Audit's case is n = 4, q = 3.
- **Axioms of this round.** Reflexivity, strict (G), (IB), and **(TC) only** (three-model no-reversal).
  - Longer strict cycles ARE allowed. Audit's certificate has a strict 5-cycle.
  - This is the normative cost of the class. Report every longer cycle that a construction produces.
- **Unchanged.** (LA), (S) (closed sections for every model, competitiveness on supp p, every selected model undominated), direct (C), (LF) at T1, T1 undominated.

## Proved by audit (verify in LL3)
- (IB) holds.
- Strict (G) holds.
- There are no nontrivial ties, since 2q > n.
- (TC) holds, since a forbidden triangle needs 3q votes and each judge supports at most two of its edges. So 3q > 2n suffices, and n = 4, q = 3 gives 9 > 8.
- Sections are closed for any selection continuous in measure.
- Direct (C) is automatic.
- A coherent competitive selection is automatically undominated.
- **So a cover of T1 needs only:** a coherent selection, continuous in measure, through T1 and COMPETITIVE. That is, for every p and every measurable X ≠ C_p, some i ∈ supp p has ≥ q judges with L_iv(X) − L_iv(C_p) ≥ η d_iv(C_p, X).

## Observations to use (author's; verify)
1. **Per world, the SIGN of each judge's change on a problem is fixed by guidance.** Only magnitudes differ across judges.
   - So judge v's vote at world i on a record is the condition: improved mass ≤ ((1−η)/(1+η)) × worsened mass, both measured by v's density of |Δℓ|.
   - Competitiveness is a statement about every record mixing improvements and worsenings at every active world.
2. **The natural adversary: Bayes-neutral mixtures near T1's boundary.**
   - Combine small switches near T1's accept/silent and reject/silent boundaries of the three sign types, whose per-world change patterns are (+,−,−), (−,+,−) and (−,−,+).
   - The aim is that at EVERY world at least n − q + 1 judges see net change < η × gross.
   - With a continuum of problem types and Lyapunov purification, the adversary has many degrees of freedom. The judges' heterogeneity must defeat this in every branch.
   - Branches at full support: C(n, n−q+1)^3; this is 6^3 = 216 for n = 4, q = 3. Do NOT fix a defending coalition in advance.
3. **Generalisations allowed.** (n, q) with 3q > 2n (TC) and 2q > n (no ties); weighted quorums with the analogous weight conditions; η depending on the world.
4. **Barriers that may still bind.** These need neither (IB) nor transitivity.
   - FF2 Thm 4.1 (refereed in GG3, with its Cor 4.3 repair): no selection continuous in measure through T1 (T1 competitive) has every world's bounded-region comparisons out of selected models endorsed by one integrable strictly guiding field.
   - Q4.2 with HH1's repair: some world must fail to add up on its relevant comparisons.
   - HH2 Thm 5.1 / Cor 5.3, with audit's scope correction.

   A quorum cover must have comparisons OUT OF SELECTED (coherent) models that no single field endorses. Audit's certificate uses arbitrary models only.

## Read
- AUDIT_quorum.md, AUDIT_quorum_summary.md, BRIEF28.md, AUDIT_nontransitive.md;
- HH1_notes.md (dominance without transitivity; barrier survival), FF2_notes.md (Thm 4.1), GG3_notes.md (Part B repair of FF2 Cor 4.3), HH2_notes.md (Thm 5.1, Cor 5.3);
- JJ1_referee.md (compactness and margin techniques), II2_notes.md (Thm 2.1 compactness with disagreement size), KK3_notes.md (domain dichotomy);
- FF1_notes.md (plain posterior family; bets lemma; level lines);
- writeup/"The Contamination Triangle.tex" §2 (axioms, domains, advice ranks).

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it. Exact arithmetic for checks. A finite search is a diagnostic only; a positive result must cover every measurable competitor and every p.
