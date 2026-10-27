# Referee report on PP2 (weak gate in three worlds, obstruction side)

20 October 2026. Adversarial referee. I read `PP2_weakgate_obstruction.md`, `BRIEF36_weakgate3.md`, `gate2d/Separation-Gated-Evaluators.tex` and the scripts in `PP2_py/`. I did not edit PP2. My only script is `REFEREE_PP2_py/lemma61_check.py`.

## Verdict in one paragraph

**Theorem 6 is correct.** I found no gap. Every step holds in the continuum, and the result is stronger than stated: two hypotheses can be weakened (see R1 below). It covers the strong gate, so the CONJECTURE after Proposition 9 is proved, within the note's setting. Theorem 1 and Propositions 2–5 are correct. The repairs are about wording and scope, plus one item in §4 that is wrong as stated: (E2) is not an escape route unless the tie is total. No label needs to be downgraded.

## Summary table

| Item | Verdict |
|---|---|
| Theorem 6, KKM step ("selected", not "tied") | CONFIRMED (one wording repair: cite KKM directly, not (★)) |
| Lemma 6.1 | CONFIRMED (holds in a stronger form: R1) |
| Lemma 6.2 (coherence places the models on [e1,e2] and [e1,e3]) | CONFIRMED |
| "Depends only on z_12 and only on z_13, hence constant on M_1" | CONFIRMED (the formal proof uses one threshold; the summary's "constant" claim also holds, with all thresholds) |
| The null-level-set contradiction; measure theory | CONFIRMED (null level sets can be weakened to "not essentially constant": R1) |
| Strict (G) at worlds 2 and 3 is enough | CONFIRMED (only the strict half of (G) is used) |
| Four-advice domain or contradiction used? | Neither is used. CONFIRMED |
| Covers the strong gate / proves the CONJECTURE | CONFIRMED WITH REPAIR (state why (H3) holds in Proposition 9's setting) |
| Lemma 0, KKM consequence (★) | CONFIRMED |
| Lemma 1, Theorem 1 | CONFIRMED |
| Level-offset refutation | CONFIRMED (summary wording repair) |
| Proposition 2 (a), (b) | CONFIRMED |
| Proposition 3 | CONFIRMED (minor: allow c_j = +∞) |
| Proposition 4 | CONFIRMED |
| Proposition 5 (a), (b) | CONFIRMED |
| §4 (E1) | CONFIRMED |
| §4 (E2) "an atom on M_i" | WRONG as stated; repaired in R1 and R2 (the tie must be total) |
| Labels PROVED / CHECKED / NUMERICS | CONFIRMED; stale theorem number in a script header |

## 1. Theorem 6, step by step

**Setting.** Accepting g is good at world i iff g_i > 0. On M_w (lines separating e_w from the other two vertices), the majority worlds rank A, S, B as 0, 1, 2 and world w ranks them 2, 1, 0. Regular models are determined by their ranks at any one world. Coherent models D_K are regular: they are never contradictory and are correct on unanimous problems, up to null sets.

### 1.1 KKM: is X_c really selected, or only tied with a selected model? — CONFIRMED

- (H4) gives, for each p, an i ∈ supp p with p ∈ A_i(X). That is exactly the KKM covering condition on every face, and the A_i(X) are closed. So some q has C_q ⪯_i X_c at all three worlds.
- Lemma 6.1 then gives **C_q = X_c**: equality of models up to null sets, not a tie. This is because:
  - at world 1, a pair C ≠ X can be accepted only by guidance or by the gate, and the proof refutes both;
  - at world 2, strict (G) refuses outright.
- No antisymmetry or direct (C) is needed, and no undominatedness.

**Wording repair.** Step 2 of the proof says "By (★) and Lemma 6.1". But (★), as stated in §0, presupposes that every world follows the ▷-rule, which Theorem 6 does not assume at worlds 2 and 3. The argument actually used is direct ("KKM gives q; Lemma 6.1 gives C_q = X_c") and is correct. The parenthesis "beating X at the worlds named in a lemma is enough" half-says this. Replace "(★)" by "KKM" in step 2.

### 1.2 Lemma 6.1 — CONFIRMED

- **Step 1.** If C has a higher world-1 rank than X_c at g ∈ M_1 ∪ M_2, then r(g) ≤ 1, because C is regular. Since k_1(g,j) ≥ c for j ≤ r(g), maximality forces k_1(g, r(g)+1) < c.
- **Step 2.** On a non-null set of such g, T^off_1(C,X_c) contains a non-null set with keys < c, so its essential infimum is < c. Every step in T^on_1 ⊆ U_1(X_c) has key ≥ c, so ess inf T^on ≥ c, or +∞ if T^on is null. Both the gate and guidance fail.
  - The inequality is strict in the *reverse* direction, so ties play no role.
  - Extra C-steps on M_3 only lower ess inf T^off, so they are harmless.
- **Step 3.** Otherwise r_1(C) ≤ r_1(X_c) a.e. on M_1 ∪ M_2. Worlds 1 and 2 are one minority and one majority on each of M_1 and M_2, so r_2 = 2 − r_1 there. On M_3, X_c has world-2 rank 0. So U_2(X_c) ⊆ U_2(C). If C ≠ X_c, the world-2 ranks differ on a non-null set, because regular models are determined by the ranks at one world. Strict (G) then refuses C ⪯_2 X_c.
- **X'_c.** The same argument with world 3 works: worlds 1 and 3 are opposite on M_1 ∪ M_3, and A on M_2 is world-3-best.

**Independent finite check** (`REFEREE_PP2_py/lemma61_check.py`). I wrote this from scratch, without PP2's library. World 2 obeys strict (G) only; PP2's `t5` gates world 2 with random keys, which is a weaker test of this lemma. World 1 refuses only the strict reverse order, and half the trials have tied keys. Result: 1,763,100 pairs (C, X_c) and (C, X'_c), no failures. CHECKED.

### 1.3 Lemma 6.2: coherence puts the models on the two edges — CONFIRMED

- Suppose m ∈ K has m_3 > 0. Then the M_3 lines passing strictly between m and [e1,e2] form an open set of lines, which is non-null. On them D_K is S or B, not A.
- So K ⊆ [e1,e2], say K = [a,b] in edge coordinates measured from e1.
- An M_1 line meets [e1,e2] only at z_12. The world-1 rank is:
  - 0 iff b < z_12;
  - 2 iff z_12 < a;
  - 1 otherwise.
- The equalities z_12 = a and z_12 = b hold only on null sets, because z_12 has a density.
- The density claim is correct. The map g ↦ (z_12, z_13) on the open orthant (−,+,+) is homogeneous of degree 0, and restricted to the sphere it is a diffeomorphism onto (0,1)². So the image of the uniform spherical measure has a positive continuous density.

### 1.4 "Depends only on z_12 and only on z_13, hence constant on M_1" — CONFIRMED

- **The formal proof (steps 3–5) uses one threshold c.** E = {k_1(·,1) ≥ c} ∩ M_1 = {z_12 ≤ y} = {z_13 ≤ y'} a.e., with y, y' ∈ (0,1). The difference of the two strips contains (0,y] × (y',1), which is non-null. Correct.
- **The summary's wording ("hence constant on M_1") is also right**, if every c is used. Each {k ≥ c} ∩ M_1 is then null or full, so k_1(·,1) is essentially constant on M_1.

### 1.5 Measure theory — CONFIRMED

- The map c ↦ μ{k_1(·,1) ≥ c} ∩ M_1 is continuous and nonincreasing, from μ(M_1) down to 0, when the level sets are null. So the value μ(M_1)/2 is attained.
- Essential infima are handled correctly. Lemma 6.1 needs only strict inequalities in the refusing direction.
- X_c is measurable whenever k_1 is.

### 1.6 Is strict (G) at worlds 2 and 3 enough? — CONFIRMED

Only the strict half is used: "if Y is a strict pointwise world-i improvement of X, then X ⋠_i Y". Nothing about k_2, k_3, Φ_2, Φ_3, (TC), (IB), (LA), (C), (LF) or undominatedness is used.

### 1.7 Four-advice domain or contradiction? — not used. CONFIRMED

Every model in the proof is regular. The theorem holds on any domain that contains the regular models X_c and X'_c and the selected models.

### 1.8 Covers the strong gate, and proves the CONJECTURE — CONFIRMED WITH REPAIR

- In Proposition 9's setting every k_i has null level sets. A non-null T^on then has ess inf < ess sup, so separation implies the weak gate, and (H2) holds.
- **Repair.** (H3) must also be checked in that setting, and PP2 does not say so. It holds automatically: any gate rule whose gate clause requires T^on to be non-null refuses X ⪯_i Y when Y is a strict pointwise improvement of X, because T^on is null and T^off is non-null. Add this sentence.
- **Scope.** The CONJECTURE is proved within the note's setting:
  - three worlds, Gaussian problems, coherent selections D_K;
  - (S) without undominatedness, i.e. competitive on supp p with closed sections;
  - a key at one world that is fixed.

  The question of whether (S) forces a two-dimensional image is indeed moot.

### 1.9 Counterexample attempt

I tried to break three steps:

- the KKM equality (a tie in place of equality);
- the edge placement (a K off the edge that still gives A a.e. on M_3);
- the strip step (atoms of k_1, or of the image of μ).

Each attempt failed for the reasons above. A sanity check of scope also passes:

- An additive world, such as an expected-loss world from the complete class story, violates (H2). So there is no clash with known positive results.
- A lexicographic world with a non-constant key is caught by Theorem 6. This is consistent with the two-world note, where M has one edge only.

## 2. R1 (strengthening, PROVED by the argument above): two hypotheses of Theorem 6 can be weakened

Theorem 6 holds with (H2) replaced by:

**(H2′)** At world 1, with a fixed key k_1:
- every pair (C, X) with C ≠ X, T^off_1 non-null and ess inf_{T^off} k_1 < ess inf_{T^on} k_1 is refused (ess inf over a null set is +∞); and
- k_1(·,1) is **not essentially constant** on M_1. Null level sets are not required.

*Proof.*
- Lemma 6.1 uses only the refusal in the strict reverse order (§1.2).
- If k_1(·,1) is not essentially constant on M_1, some c has 0 < μ(E) < μ(M_1), where E = {k_1(·,1) ≥ c} ∩ M_1. To see this, suppose every value is 0 or μ(M_1), and let c* be the supremum of the c with full value. Then k_1(·,1) ≥ c* and k_1(·,1) ≤ c* a.e.
- Then y > 0 and y' < 1, and step 5 runs unchanged. ∎

**Consequences.**
- (H2′) covers the strong gate with no assumption on level sets.
- It covers any rule that breaks essential-infimum ties by a secondary rule, since such a rule still refuses the strict reverse order.

## 3. R2 (rigidity; referee's sketch, which I believe PROVED): what a surviving fixed key must look like

Assume (H2′) without the non-constancy clause, together with (H3) and (H4). Then:

- k_1(·,1) equals a constant κ a.e. on **all** mixed problems, not just on M_1;
- min(k_1(·,2), κ) is a.e. constant on all mixed problems.

*Sketch.*
1. Theorem 6 (R1) gives k_1(·,1) = κ a.e. on M_1.
2. **For c > κ:** X_c has rank 0 on M_1, so K_c = {e1}. On M_2, D_{e1} is A, with world-1 rank 0, so k_1(·,1) < c a.e. on M_2.
3. **For c ≤ κ:** X_c has rank ≥ 1 on all of M_1, so e2 ∈ K_c, and {rank 2 on M_1} = {k_1(·,2) ≥ c} ∩ M_1 = {z_12 < a_c}. By the X'_c strip argument, this set is null or full, so a_c ∈ {0,1}.
   - Then K_c is either [e1,e2], giving S on M_2, or {e2}, giving B on M_2.
   - Either way k_1(·,1) ≥ c on M_2, and {k_1(·,2) ≥ c} ∩ M_2 is full exactly when it is full on M_1.
4. M_3 is handled the same way with X'_c. ∎

**Consequence for §4 (E2).** "Give k_i(·,1) an atom on M_i and decide the tie by a secondary rule" — **WRONG as stated.**
- A partial atom on M_1 is still killed by Theorem 6.
- A fixed world-1 primary key must be completely blind at level 1 across all mixed problems: one atom carrying the whole mixed level-1 layer.
- So all the content sits in the secondary rule. That rule, being record-based, is really an instance of (E1).

**Suggested rewrite of (E2).** "Ties: the primary key k_i(·,1) must be essentially constant on all mixed problems (R2); the ordering must come entirely from a record-based secondary rule, so (E2) reduces to (E1)." Screen S11 should be stated for record-chosen priorities only. For a fixed priority it is unsatisfiable unless the key is blind in the sense of R2.

## 4. The other items (briefly)

- **Lemma 0, (★): CONFIRMED.** One edge case: ▷ holds trivially when C = X. This is harmless.
- **Lemma 1: CONFIRMED.**
  - Step 2 is correct: on Δ every rank changes, the majority worlds one way and the minority the other, so Δ = ∪ G_i. Δ contains no unanimous problems, because both models are regular.
  - The pigeonhole step, and the "a.e. pair" use in step 6, are valid: take a.e. g in a non-null A and some g' in a non-null B′. Finitely many levels make the resulting set of C-steps non-null in I.
  - The conclusion a ≤ b fails the strict weak gate, so ties count as failures, correctly.
- **Theorem 1: CONFIRMED.**
  - The hypothesis gives Lemma 1's condition directly.
  - "A on every mixed problem" is incoherent: the three classes force K into [e2,e3] ∩ [e1,e3] ∩ [e1,e2] = ∅.
  - Remark: Theorem 1's key hypothesis makes k_1(·,1) non-constant on M_1. So Theorem 1's *impossibility* also follows from Theorem 6. Its stronger content is the mechanism: no regular model beats another at all three gates.
- **Level-offset refutation: CONFIRMED.**
  - World 2 gets guidance (A → S is a loss at both majority positions).
  - World 1 adds level-1 steps on E_3 (keys < 1) and removes level-2 steps on E_1 (keys > 10).
  - **Summary repair.** Summary item 2 says "A model dominates every rival...". This is domination at the gate level only (▷ at all three worlds), not domination under the verdicts. Say so.
- **Proposition 2: CONFIRMED.** I re-derived all six change types in (b), and the ψ_i bounds in (a). Both rivals are incoherent as claimed: B on all of M_3 forces K = {e3}, and then M_1 lines are A.
- **Proposition 3: CONFIRMED.** In the converse, if T^on_j is null then c_j = +∞, or any large finite c_j, works. This conflicts with "c ∈ R³" only cosmetically. The "protected below c" restatement is correct, including "sufficient up to ties".
- **Proposition 4: CONFIRMED.** Added steps are mixed regular steps that C lacks, so none is keyed below c_j. Atomlessness gives the disjoint pieces. The remark that contradiction rivals pass every weak gate is correct, provided the contradiction and unanimous keys lie strictly below the mixed keys, as under the brief's convention.
- **Proposition 5: CONFIRMED.**
  - (a): with threshold sets, any added step passes the gate. Otherwise X = C on M_1 ∪ M_2 and X is A-ward on M_3, which gives guidance at world 3.
  - (b): failing world 1 forces X to be a weak world-1 improvement. The P/Q bookkeeping is correct. M_1 changes only add losses at worlds 2 and 3, which helps those gates pass, so the "iff" holds up to ties.
- **Labels: CONFIRMED.**
  - PROVED is used only where there is a complete proof.
  - CHECKED and NUMERICS are used correctly, including "mixed directions, finite only".
  - Two cosmetic points: the header of `t5_edge_rigidity.py` says "Theorem 3" where it means Theorem 6, and the document numbers both a Lemma 1 and a Theorem 1.

## 5. What I recommend PP2 change (do not edit PP2; for the author)

1. In Theorem 6 step 2, write "KKM" in place of "(★)".
2. In §3, state R1. Optionally add R2 as a remark.
3. In the strong-gate consequence, add the sentence explaining why (H3) holds for any gate rule.
4. Rewrite (E2) as in §3 of this report.
5. Qualify "dominates" in summary item 2.
6. Fix the stale "Theorem 3" in `t5_edge_rigidity.py`.
