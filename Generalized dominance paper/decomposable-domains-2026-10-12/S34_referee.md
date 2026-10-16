# S34. Referee report on S3_notes.md (R1, construction side) and S4_notes.md (R1–R3, exclusion side)

15 Oct 2026, round 13 (BRIEF12). Independent adversarial referee. Labels for my own results: **PROVED**,
**CHECKED**, **CONJECTURE**, **NUMERICS** (scripts in `s34ref_py/`, run with `python3 -I`; no verdict depends on them).
Verdicts per claim: CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG. Terminology as in termfix/TERMFIX_RULES.md
(U-domain M_U: a restriction of the class of evaluable models only). No assumption is added to the framework.

Read for this report: BRIEF12; write-up §§8.4(c), 8.5 (all parts, in particular (c), (e), (f)); P4B_referee §8 (DL,
DR, Lemma T, E2, E3); Q1_notes §§2, 6; Q12_referee §§1, 4–6; S3_notes, S4_notes, and their scripts `s3py/`, `s4py/`
(both re-run; outputs reproduce).

Notation as in S3/S4: (Nest), chain c_b, d_b = M∖c_b, slabs [s,t), μ̄, x(h), φ₁, φ₂, (K), 𝒰₁(Z) = {A : Z ≤₁ A},
τ(Z) = sup{t : Z ≤₁ d_t}, 𝒱_i (= S4's 𝓜_i) the endorsing probability charges on cut pairs.

---

## 0. Summary

| Claim | Verdict |
|---|---|
| S3.1 mirrored band ∪ translates: every axiom except closed sections, at both worlds; mirrored simple certificates; ¬SP^reg at both worlds | **CONFIRMED** (wording repair: "(Nest)" there means "C_L is the chain", since (Nest) includes (S)) |
| S3.2 exact section a+d+h−μ̄(F); closed only if the infimum is attained; ⇒ (QC₁) under closed world-1 sections | **CONFIRMED WITH REPAIR** ("⟺" holds for the test models D_{d,h} only; "min attained" should be "inf > 0"; half-open case when inf > 0 is not attained). Sufficiency is false in general (referee counterexample §2.3) |
| S3.3 packing lemma (a), (b) | **CONFIRMED** |
| S3.4 fibrewise route fails (K); general form for K ∪ translates | **CONFIRMED** (for the design stated; the other designs are correctly labelled failure reports) |
| Conjecture QC (S3.C1); "QC ⇒ ¬R1" | label **CONFIRMED** (CONJECTURE); implication **CONFIRMED** (it needs no minimax). Addition: QC₁ ⟺ QC₂ ⟺ "κ₁(c_s) > 0 for all s > 0" (PROVED here, §5.2). "Strictly stronger than ¬R1" should read "a priori stronger" |
| Theorem RATE (R3₁ ⟺ R3₂ ⟺ SR₁ ⟺ SR₂ ⟺ uniform forms ⟺ NDL) | **CONFIRMED** (every step re-derived) |
| §2.4 "doubly-light sequences give only favourable comparisons" | **CONFIRMED** as a statement about the listed comparisons; its rider "any exclusion must use closedness beyond Lemma T" is a heuristic, not PROVED |
| Corollary SR | **CONFIRMED** |
| Prop MP♯ (a)–(c) | **CONFIRMED**; (d) **CONFIRMED WITH REPAIR**: the correct bounds are ν(d_{τ(Z)}) ≤ inf_{A∈𝒰₁(Z)} ν(A) ≤ lim_{t↑τ(Z)} ν(d_t); the note's upper bound ν(d_{τ(Z)}) is unproved for finitely additive ν |
| Loop lemma | **CONFIRMED WITH REPAIR**: the proof uses "(K) at a cut in (s,t)", which is empty when t ≤ s; t ∈ (T(s), s] occurs, even in Example A (s > 3/4). Repaired by cancellation (§8.2) |
| Example A (all axioms via Thm witness; η₁(P,1) ≤ μ̄(P)²/2) | **CONFIRMED** |
| Prop LIN | **CONFIRMED WITH REPAIR**: proved as written for world 2 = μ̄; for a general SP weight ν₂ the certificate's averaging must be taken in ν₂ (or ν₂ ≤ Cμ̄ assumed) |
| Correction of write-up §8.5(f)(R3) ("would give Q1.C1") | **CONFIRMED: the sentence must be corrected**, and so must "common to (R1) and (R2)" and the Vitali clause (§9.3 gives the corrected text) |
| §5.1 "R1 is not a rate problem (PROVED observations)" | **GAP (overlabelled)**: what is shown is that no known argument uses uniformity over sources; "consistent with the mirrored-pair data" is not proved (no model). Relabel as observation |
| §5.2 LF cannot concentrate thin targets (world 2 = μ̄) | **CONFIRMED as stated** (for LF's slab-uniform mechanism), but the reading is misleading; the correct mechanism is §10.2 |
| Lemma UE and its consequences | **CONFIRMED** (inconclusive, as stated) |
| (W-a)–(W-d) | **CONFIRMED** ((W-a) with the MP♯(d) repair: modulus ν₂(d_{τ(Z)})) |
| Conjecture S4.1 (NDL always) | label **CONFIRMED** (CONJECTURE) |

**Net effect on the write-up.** (R1) is still open; nothing in S3 or S4 settles it either way. (R3) as a "missing
lemma" is dead: its qualitative form is a single joint property (NDL) that holds automatically in the setting of
Q1.C1, and the linear form that MP would need is false in general. Precise remaining forms in §12.

---

## 1. S3.1 — mirrored simple pairs without closed sections: CONFIRMED

Re-derived step by step.

- **(i) Strict (G), (IB).**
  - World 1 is Q1's world verbatim (Q1.1, confirmed in Q12_referee §1.1).
  - World 2 is its image under x ↦ 1−x with N₊ moved to the side that enters every condition (heads, x = −1). Under
    the map, d_{b₀} ↦ c_{1−b₀}, F′_j = A_j ∩ c_{b₀} ↦ a subset of d_{1−b₀}, heads ↦ tails. The key step of Q1.1
    (common negative part, compatibility s + t ≥ −1, no N₊ in the slab between x and a′ = 1−b₀) transports unchanged.
    CONFIRMED.
- **(ii) (K) for every model, from the two bands alone.**
  - For X = (A,N) and b ∈ (0,1): band₁ rejects 1_{A∪N} − 1_{c_b} iff, for some x₁ < b,
    μ̄([x₁,b)∖A) > μ̄(N) + μ̄(A ∩ d_b). (Tails at x ≥ b and on (1,2] are ≥ 0.)
  - band₂ rejects 1_{(M∖A)∪N} − 1_{d_b} iff, for some x₂ > b, μ̄([b,x₂) ∩ A) > μ̄(N) + μ̄(c_b∖A).
  - The chain of inequalities in the note closes into a contradiction. Correct.
- **(iii) (U).** The case split is correct:
  - N = ∅ from the conditions on (1,2], where the translates' tails vanish;
  - Q = ∅ from τ(b) = −μ̄(Q) in each case (b ≤ a is impossible for a translate, since τ_{δ₁}(a) ≤ 0 < μ̄(A_j));
  - then δ₂ = −1_P, so P = ∅ by (i).
  - The vertices follow from strict (G).
- **(iv) C_L = the selection, (LA), (C).**
  - The band sections are closed, nonempty initial and final segments: the defining tails are continuous and monotone
    in b, and b = 0 (resp. 1) is always in.
  - By (ii) they cover [0,1], so they meet at some b*. By (iii), every X ≠ C_{b*} is dominated by C_{b*}.
  - This is exactly the repair of Q12_referee §1.2. Correct.
- **(v) The mirrored certificates.**
  - c_a ≤₁ A_j and d_{b₀} ≤₂ F′_j ⊆ A_j are cut pairs at a and at b₀ respectively, so both are relevant.
  - Disjointness makes the family uniformly Cesàro-thin, and ¬SP^reg holds at both worlds. Correct.
- **(vi) Closed sections fail at both worlds.** Correct. A simpler witness than S3.2's is available:
  - **World 1.** For the regular model with E₁X ∩ M = d_a, c_b ≤₁ d_a via 𝒢₁(A_j) iff b ≤ 1 − μ̄(A_j), and via the
    band iff b ≤ 1 − a. So S₁(X) = [0,1): it contains every b < 1, and 1 ∉ S₁ by strict (G).
  - **World 2.** Mirror: S₂ of the model with E₂X ∩ M = c_{b₀} is (0,1].
  - This is the mechanism of S3.3(b), with Z = c_a.
  - NUMERICS `s34ref_py/s3_sections.py` (2): exact, dyadic family: end via A_j = 1 − μ̄(A_j) for j = 1..6; c₁ ≤₁ d_a
    is rejected.
  - NUMERICS `s34ref_py/s31_grid.py`: non-uniform disjoint family (24, 12, 6, 3, 1 cells; S3's own grid used equal
    measures, so it could not separate the section ends). (K): 0 failures and (U): 0 failures over 600 models × 95
    cuts. World-1 ends are n − |A_j|, and world-2 starts are |F′_j|, as predicted.

*Wording repair.* S3 §0 item 1 says "C_L = the selection (so (Nest))". (Nest) as defined in §8.4(c) includes (S).
S3.1 has the chain structure of (Nest) without (S), and that is what should be said.

---

## 2. S3.2 — sections of band ∪ translates worlds: CONFIRMED WITH REPAIR

### 2.1 What is correct

- **(a)** For D = [a,a+d) ∪ [1−h,1) with a+d+2h < 1, the function x + G_D(x) equals
  - a+d+h on [a,a+d],
  - x+h on [a+d,1−h],
  - 1 on [1−h,1].
  For F ∈ 𝓕_D, since G_F ≤ μ̄(F), the minimum of x + G_D − G_F is a+d+h − μ̄(F), attained at x = a. Re-derived
  piece by piece. The band end is d+h.
- **(c)** Every F with μ̄(F) ≤ h lies in 𝓕_D. Re-derived.
- **(d)** If inf_𝓕 μ̄(F) = 0, every such section is half-open. If all world-1 sections are closed, then
  inf_𝓕 μ̄(F) > 0, and every A ∈ 𝒰₁(Z) has μ̄(A) ≥ min(μ̄(Z), inf_𝓕 μ̄(F)), via τ(0) for the band and τ(a) for a
  translate. Hence (QC₁) holds, and (R1) is impossible, in this architecture with closed world-1 sections.
- The reading "the section sees F only through μ̄(F), so radial thinness does not help" is correct.
- So is the remark that "compact profiles" is the wrong test. ‖G_F‖_∞ = μ̄(F), so a thin family always has 0 as a
  limit profile. The operative condition is inf μ̄(F) > 0.

NUMERICS `s3_sections.py` (1): twelve random (d, h, F), exact rationals with bisection. The formula matches to
8·10⁻¹³, and the band end is d+h in every case.

### 2.2 Repairs

- **(b)** The note states only the cases "attained" and "0 and not attained". If inf_{𝓕_D} μ̄(F) = κ > 0 is not
  attained, the section is [0, a+d+h−κ), also half-open.
- **(d)** "κ := min_{F∈𝓕} μ̄(F) > 0 exists" is more than is proved. The test models give attainment only when
  members of measure close to κ lie in 𝓕_D for some admissible h, for instance when κ < (1−a)/2. What the argument
  proves, and what is used, is inf_𝓕 μ̄(F) > 0.
- **Heading of S3 §3 and §0 item 2** ("closedness ⟺ attained target measure", "closedness is exactly a measure
  bound"). The equivalence holds for the test models D_{d,h} only. In general the condition is **necessary, not
  sufficient**; see §2.3. Likewise S3 §6: "(QC) is what closedness gives *exactly* in S3.2" should read "(QC₁) is
  *implied* by closed world-1 sections in S3.2's class".

### 2.3 Counterexample to sufficiency (PROVED; NUMERICS `s3_sections.py` (3))

Take a = 0.3, F₀ = [0.99,1) (μ̄ = 0.01, the minimum), F_n = [0.5, 0.6 + 1/n) for n ≥ 5, and 𝓕 = {F₀} ∪ {F_n}. Let
D = [0.3,0.8).
- F₀ ∉ 𝓕_D, since G_D = 0 on [0.8,1).
- Each F_n ∈ 𝓕_D, with β_{F_n}(D) = 0.7 − 1/n.
- The band end is 0.5.

So S₁(X_D) = [0,0.7), which is open, although min μ̄(F) = 0.01 is attained. The exact computation agrees.

---

## 3. S3.3 — packing lemma: CONFIRMED

- **(a)** This is transitivity plus Lemma T₁: the radius form follows from the sequential form, and finitely many
  points are covered by P4B §8.2.
- **(b)** The note shows c_b∖W = Z and W∖c_b ⊇ [1−m_k,1) for b ∈ (s,1). For b ≤ s, W∖c_b ⊇ d_s, and the same chain
  works. So c_b ≤₁ W for every b < 1. Then (R5), or closedness at b = 1, gives M ≤₁ M∖Z, that is Z ≤₁ ∅. Correct.
- **"A band accepts A ≤₁ [1−μ̄(A),1)" for A ⊆ M.** The tails of 1_{[1−m,1)} − 1_A are ≥ 0. Correct.

---

## 4. S3.4 — fibrewise band ∪ translates fails (K): CONFIRMED

- **Fibre tails and heads at b ∓ ε.** These are −ε on the fibres Y′ and Y″. Correct.
- **Translates.** Integrating the fibre tails gives the global tail at a, which is μ̄(Q) − μ̄(P) = 0 < μ̄(A_j). The
  mirror computation at b₀ gives 0 < μ̄(F′_j). Correct.
- **General form.** Every translate member δ has ‖δ⁺‖₁ ≥ τ_δ(a) ≥ μ̄(F). So only cut pairs with
  μ̄(Q) < inf μ̄(F) are out of reach of the translates. (μ̄(P) + μ̄(Q) < inf is more than needed.) Correct.

NUMERICS `s34ref_py/s34_fibre.py`: 40 × 8 grid, 124 cut pairs, including pairs whose source lies in a row of some
A_j. (K) fails in all 124, and in each of them the *global* bands accept both comparisons. The failure is the fibrewise
restriction, as the note says.

The remaining designs in S3 §5 (lexicographic charge vectors, directed unions) are failure reports. They are correctly
labelled, and the CONJECTURE "such worlds satisfy SP^reg" is correctly labelled.

---

## 5. Conjecture QC and "QC ⇒ ¬R1"

### 5.1 Verdicts

- **"QC ⇒ ¬R1" is CONFIRMED** and needs no Sion. If 𝒜 ⊆ 𝒰₁(Z) is uniformly Cesàro-thin and f = Σλ_i 1_{A_i} has
  ‖f‖_∞ < ε, then min_i μ̄(A_i) ≤ μ̄(f) < ε. So κ₁(Z) = 0.
- **The CONJECTURE label is correct.**
- **Supporting facts, all correct:**
  - QC holds next to a uniformly absolutely continuous SP weight (Q1.6(a));
  - QC holds in S3.2's class with closed world-1 sections;
  - QC fails in S3.1.
- **Wording.** "(QC) is strictly stronger than ¬(R1)" should read "a priori stronger". No system with ¬R1 and ¬QC is
  exhibited. What is shown is only that the negations differ in form: vanishing measure versus Cesàro-thin.

### 5.2 Referee addition (PROVED): QC is one joint property, and reduces to segments

**Proposition QC-J.** Under (Nest) with every axiom, the following are equivalent:
- (QC₁);
- (QC₂);
- κ₁(c_s) > 0 for every s ∈ (0,1);
- κ₂(d_t) > 0 for every t ∈ (0,1).

Moreover, κ₁(Z) ≥ κ₁(c_{s₀(Z)}), and κ₁(c_s) ≥ κ₂(d_t) for every t ∈ [T(s),1).

*Proof.*
- If Z ≤₁ A_k with μ̄(A_k) → 0, MP(a), which needs no overlap condition, gives d_{b₀(Z)} ≤₂ A_k. That is ¬QC₂. The
  mirror gives ¬QC₂ ⇒ ¬QC₁.
- MP-loop gives 𝒰₁(Z) ⊆ 𝒰₁(c_{s₀}). Hence κ₁(Z) ≥ κ₁(c_{s₀}), and the segment form implies QC₁.
- The last inequality is MP♯(b): 𝒰₁(c_s) ⊆ 𝒰₂(d_t) for t ≥ T(s). ∎

So the relaxation of (R1) that S3 proposes attacking is itself a mirrored configuration. **(R1′) := ¬QC**: there are
s > 0 and A_k with μ̄(A_k) → 0 and c_s ≤₁ A_k for all k. Then automatically d_t ≤₂ A_k for every t ≥ T(s).

---

## 6. Theorem RATE: CONFIRMED

Every implication was re-derived.

- **Step A** (SR₁ ⇒ R3₁ᵘ).
  - Pass to a subsequence x_k → x̄; then the Q_k concentrate at x̄.
  - c_σ ≤₁ P_k, because S₁(P_k) = [0, φ₁(P_k)] is a closed initial segment containing σ.
  - Transitivity then contradicts Lemma T₁ for the fixed source c_σ.
- **Step B** (R3₂ ⇒ SR₁).
  - t_k ∉ S₁(P_k), so (K) gives d_{t_k} ≤₂ M∖P_k. Cancellation turns this into d_{t_k} ∩ P_k ≤₂ c_{t_k}∖P_k.
  - Then W_k = P_k ∩ d_g ≤₂ V_k, with μ̄(W_k) ≥ 2m/3.
  - V_k is non-null by strict (G), and V_k ⊆ c_{t_k}. This violates (R3₂) at gap g, x = 0.
- **The mirrors** ((R3₁) ⇒ (SR₂) and (SR₂) ⇒ (R3₂ᵘ)) were written out. They are exact.
- **Step D.**
  - "φ₂(W_k) → 1" uses Lemma T₂ at x = 0 for the fixed source d_{1−σ′}. Correct.
  - (K) at τ_k for the model with E₂ = W_k gives c_{τ_k} ∩ W_k ≤₁ d_{τ_k}∖W_k. Correct.
  - S_k = W_k ∩ c_{1−g} has μ̄ ≥ m/3, lies in [g, 1−g), and satisfies S_k ≤₁ R_k → 1 and S_k ≤₂ W_k ≤₂ V_k → 0.
- **Inputs used:** (K) at interior cuts, closed sections at regular models (B0 and Lemma T), strict (G), cancellation
  and transitivity. No (C) and no (LA) beyond N0. The "necessarily η < m/2" remark is right: take Q = P, a slab of
  width m.
- **Remarks (i), (iii).** Correct.
- **Wording.** "A rate in strict escape" means the rate at b = 0 only (SR_i). Rates of escape at interior b are not in
  the list.

**§2.4 (favourable comparisons only).** It is correct that the comparisons the definition and (K) produce are
favourable-direction cut pairs, which (U) does not forbid. The sentence "any exclusion must use closedness beyond
Lemma T; closedness used for a fixed source is exhausted by Lemma T" is a heuristic. Transitivity and sum closure
could still combine these comparisons with others. It should not carry the label PROVED (compare N2, whose rider has
the same status).

---

## 7. Corollary SR: CONFIRMED

- **Step 1.** A strictly positive charge has an a.e.-positive countably additive part. The reason is that a purely
  finitely additive charge is carried by sets of arbitrarily small measure, so it vanishes on some non-null set
  inside any non-null set. This is N19 Lemma R1.
- **κ(m) > 0.** The argument by μ̄{ρ < ε} → μ̄{ρ = 0} = 0 is correct.
- **Step 2.** It uses the relevant comparison C_{t_k} ⪯₂ X (E₂X = M∖P_k) in cut-pair form, which ν₂ ∈ 𝒱₂ endorses.
  The contradiction κ(m/2) ≤ ν₂(c_{t_k}) → 0 is exact.
- **Scope.** The hypothesis "ν₂(c_t) → 0 as t ↓ 0" is implied by uniform absolute continuity, so Cor. SR covers the
  whole setting of Q1.C1. It is not implied by SP^reg₂ alone (a purely finitely additive part may sit at 0⁺), and
  the note does not claim that.

---

## 8. MP♯ and the Loop lemma

### 8.1 MP♯: (a)–(c) CONFIRMED, (d) CONFIRMED WITH REPAIR

- **(b)** The proof is MP(a) with Lemma T₁ replaced by "t > τ(Z)". The endpoint t = τ(Z) is in by closedness of
  S₂(A). Correct.
- **(c)** Use A = d_{t′} with t < t′ < τ(Z) and strict (G). Correct.
- **(a)** τ(Z) < 1 by Lemma T₁. τ(Z) = 0 forces M ≤₂ Z, so Z = M. Correct.
- **(d) Repair.**
  - (b) includes t = τ(Z), so ν(d_{τ(Z)}) ≤ ν(A) for every A ∈ 𝒰₁(Z). This is stronger than the note's lower bound
    lim_{t↓τ} ν(d_t).
  - The test sets A = d_{t′} (t′ ↑ τ(Z)) give only inf ν(A) ≤ lim_{t′↑τ(Z)} ν(d_{t′}), which is ≥ ν(d_{τ(Z)}).
  - The note's upper bound ν(d_{τ(Z)}) would need Z ≤₁ d_{τ(Z)}, that is, attainment of the sup defining τ. That is
    not a section of a selected model, and nothing makes it closed.
  - Correct statement:

      **ν(d_{τ(Z)}) ≤ inf_{A∈𝒰₁(Z)} ν(A) ≤ lim_{t↑τ(Z)} ν(d_t).**

  - For μ̄ (or any countably additive ν) both bounds equal ν(d_{τ(Z)}). So inf μ̄(A) = 1 − τ(Z) stands.
- **Referee identity (PROVED, by monotonicity):** η₁(P,1) = 1 − τ(P). If P ≤₁ Q with Q ⊆ d_{1−η} non-null, then
  P ≤₁ d_{1−η}, and conversely Q = d_t is admissible. Hence, next to world 2 = μ̄,

      κ₁(P) = inf{μ̄(A) : P ≤₁ A} = η₁(P,1).

  So the QC quantity and the Lemma-T₁ radius at 1 coincide there.

NUMERICS `s34ref_py/s4_exampleA.py` (1), (4):
- the grid τ(c_s) agrees with the closed form T(s) = 1 − (1−√(1−s))² (Example A);
- 5000 random A with c_s ≤₁ A all have μ̄(A) ≥ 1 − T(s).

### 8.2 Loop lemma: CONFIRMED WITH REPAIR

*Gap.* The proof of S(t) ≤ s applies (K) "to the cut pair (c_s, d_t) at any cut in (s,t)". That needs s < t, and
t > T(s) does not imply t > s.

*Example (Example A itself).* In Example A, T(s) = 1 − (1−√(1−s))². This formula holds for t ≥ s and, by
cancellation, for t < s. So T(s) < s exactly when s > 3/4. For instance, T(0.8) = 0.694. NUMERICS (3): the interval
(T(s), s] is nonempty for s = 0.8, 0.9, 0.99.

*Repair (PROVED).* For all s, t ∈ (0,1): **c_s ≤₁ d_t or d_t ≤₂ c_s.**
- If s < t, this is (K) at a cut in (s,t).
- If t < s, cancellation turns c_s ≤₁ d_t into c_t ≤₁ d_s, and d_t ≤₂ c_s into d_s ≤₂ c_t. (K) applies to the cut
  pair (c_t, d_s) at a cut in (t,s).
- If s = t, use (K) at the cut s.

Hence t > T(s) ⇒ c_s ≰₁ d_t ⇒ d_t ≤₂ c_s ⇒ S(t) ≤ s. The two inclusions are MP♯(b) and its mirror, and they are
CONFIRMED (the mirror also holds at s′ = S(t), by closedness). The reading "the ping-pong never raises the exported
segment" stands.

---

## 9. Example A, Prop LIN, and the correction to §8.5(f)

### 9.1 Example A: CONFIRMED

- **The Bayes model.** At p (r = p₂/p₁), it errs at world 1 on h ∈ M exactly when θ(x(h)) < r. Tie sets are level
  sets of x, hence null. So the selection is C_{θ⁻¹(r)}, or C₀ = P₁ when r ≤ θ(0). It is coherent, on the path of
  §8.5(e), and continuous.
- **Thm witness applies.**
  - Integral penalties with an integrable envelope: θ ∈ L¹.
  - (W1): Bayes optimality.
  - (W2) and (W4): uniqueness at interior p; at e₁, ψ₁(X) = 0 forces X = P₁; e₂ is symmetric.
  - (W3): dominated convergence.
  So Example A is a successful system with every axiom, including closed sections for every model (ψ_i(C_p) is
  continuous in p) and C_L = the selection.
- **The radius.** η₁(P_m,1) = (ρ₁(P_m)/2)² ≤ m²/2. NUMERICS: η/m² = 0.4555, 0.4951, 0.4995 for m = 0.1, 0.01, 0.001.
- **The variants are right.** They give rate m^{1/(1−α)}: any power q > 1, not only q ≥ 2 as the note says. The
  slow logarithmic profile gives e^{−c/m}.

### 9.2 Prop LIN: CONFIRMED WITH REPAIR

As written, the proof compares the average **μ̄**(Q_il) ≤ ε/K with the lower bound **ν₂**(Q_il) ≥ c′·c·a/K. The two
match only for ν₂ = μ̄.

*Repair.* State Prop LIN for world 2 = μ̄. Alternatively, keep a general SP weight ν₂ with ν₂(d_t) ≥ c′(1−t), and
read the N4 certificate's averaging in ν₂, which is legitimate because integrating 1_{c_a} + Σλ_k(1_{Q_k} − 1_{P_k}) ≤ ε
against ν₂ is allowed. Or add ν₂ ≤ Cμ̄, with constant cc′a/C.

The N4 shape should be stated as a hypothesis: K sources with μ̄(P_i) = a/K, and targets with average μ̄ ≤ ε/K. With
that, the proof is exact, using η₁(P,1) = 1 − τ(P) and MP♯(b).

The reading "through MP, only a linear rate helps" is a statement about this route. It is fine as such.

### 9.3 The write-up's (R3) sentence: CORRECTION CONFIRMED, with a stronger reason

*Why the sentence is wrong.* By Cor. SR, qualitative (R3) is a **theorem** under the hypothesis of Q1.C1, namely
world 2 with a strictly positive, uniformly absolutely continuous endorsing charge. In that setting world 1 has no
simple certificate (Prop Q15), so R2's hypothesis holds there. Hence:
- "(R3) would give Q1.C1" is equivalent to an unproved claim of Q1.C1 itself;
- "with Theorem LF a Vitali-type argument for N17.B′ in two worlds" would also prove Q1.C1. It must be withdrawn for
  the same reason;
- "common to (R1) and (R2)" is not supported. In (R1) the sources are fixed, and Lemma T already gives their radii.

*Corrected item (proposed text for §8.5(f)):*

> **(R3)** *A rate in Lemma T.* For non-null $P\subseteq c_b$ and $x>b$, does the radius $\eta(P,x)$ of Lemma T$_1$
> admit a positive lower bound depending only on $\bar\mu(P)$ and $x-b$? This qualitative rate is equivalent to the
> same rate at world 2, to a uniform rate in strict escape at $b=0$ at either world, and to the absence of
> doubly-light sequences (sets of measure bounded below that world 1 ranks below sets concentrating at $1$ and world 2
> below sets concentrating at $0$) (\src{S4} Thm.~RATE). It holds whenever one world has a strictly positive
> endorsing charge vanishing at the far end of the chain, in particular next to an additive world with integrable
> density (\src{S4} Cor.~SR); so it does not give \src{Q1} Q1.C1, which is open in exactly that setting, and it does not
> by itself give a Vitali argument for N17.B$'$. Against the ratio certificates of N4, the route of
> Proposition~\ref{prop:MP} needs a rate linear in $\bar\mu(P)$, $\eta_1(P,1)\ge c\,\bar\mu(P)$ (\src{S4} Prop.~LIN);
> this fails in a system with every axiom and both worlds additive ($\eta_1(P,1)\le\bar\mu(P)^2/2$, \src{S4}
> Example~A), so it is not a consequence of the axioms and could only come from the failure of SP$^{\mathrm{reg}}$
> itself. No rate is known to bear on (R1), whose sources are fixed.

The opening of item (R3) ("the missing lemma common to (R1) and (R2)") should be deleted.

The closing paragraph of (f) ("pass the closedness test of Proposition Q13, which requires a compact family of target
profiles that a thin family cannot be") should also be updated: "in band ∪ translates worlds, closed world-1 sections
force inf μ̄(F) > 0 over the generating family, hence (QC) and no mirrored pair (\src{S3} Prop. S3.2)".

---

## 10. S4 §5 (the R1 failure report)

### 10.1 Verdicts

- **§5.1: GAP (overlabelled).** It is true that the mirrored-pair sources are fixed and that the known consequences
  of rates are lower bounds on φ_i. It is not proved that R3 is "irrelevant" or "consistent with the mirrored-pair
  data". That would need a model, or a proof that R3 has no consequence for auxiliary, varying sources generated
  inside an argument. Relabel as an observation.
- **§5.2: CONFIRMED as stated.**
  - With world 2 = μ̄, W ≤₂ Q iff μ̄(Q) ≥ μ̄(W) for disjoint sets. So T₂'s half-radius is μ̄(W)/2, LF's slab width is
    ≤ μ̄(W), and a cover of a spread set needs Σ μ̄(W_l) ≥ a.
  - The **reading is misleading**, however. In that very class, (K) itself concentrates thin targets: it forces
    P ≤₁ Q for every cut pair with μ̄(Q) > μ̄(P), which is the band on cut pairs, and that is how Q1.6(a) excludes
    simple certificates there.
  - So the obstruction is not "closedness is blind to the fibre". It is the blocking mechanism of §10.2.
- **Lemma UE: CONFIRMED.**
  - Steps 1–2 are correct. In step 3 the substitution is cancellation by the disjoint set B ∩ d_{x+κ}, not "sum
    closure", since L₂ = R₂ there. The step is correct.
  - Step 5's four pieces are pairwise disjoint. The final left-side monotonicity uses c_x∖(A∪A′∪B) ⊆ c_x∖B, which
    holds without assuming A_j ⊆ d_x.
  - The consequences (3-unions are thin; radii summable under iteration; the thin residue
    A ∩ d_{x+κ} ≤₂ [x,x+κ)∖A, by (K) at x+κ) are correct.
- **(W-a)–(W-d): CONFIRMED.** (W-a) should use the repaired modulus ν₂(d_{τ(Z)}). "Idempotent" in (W-c) means "does not
  raise the segment" (Loop lemma). It is not idempotence in the algebraic sense.
- **Conjecture S4.1:** the label is correct. By Cor. SR it holds next to any world with an end-vanishing SP weight.

### 10.2 Referee addition (PROVED): why (K) cannot transport the targets of a mirrored pair

Let Z be non-null, A ∈ 𝒰₁(Z), and t ≥ τ(Z). Then for every Q ⊆ d_t∖A, Q ≤₂ A ∩ c_t.

*Proof.* MP♯(b) gives d_t∖A ≤₂ A ∩ c_t. Monotonicity on the left finishes it. ∎

So on every cut pair (A ∩ c_t, Q) with Q ⊆ d_t∖A, (K) is already satisfied by world 2, in its favourable direction.
(K) never forces the world-1 packing A ∩ c_t ≤₁ Q, at any cut t ≥ τ(Z).

This holds in every system. It is exactly what packing needs, and exactly what S3.3 says no closed system can accept.
Next to world 2 = μ̄ it is harmless, since there every such A has μ̄(A) ≥ 1 − τ(Z), so the targets are fat. In a
mirrored pair it is the self-protection of the configuration: the world-2 half of the pair is precisely the statement
that blocks the world-1 transport.

A proof of ¬R1 must therefore produce world-1 packing of a thin A ∩ c_t from something other than (K) at cuts
t ≥ τ(Z). The remaining sources are:
- (K) at cuts below τ(Z), where it is not blocked;
- closedness at world 2 applied to non-segment sources.

---

## 11. Exact established statements after this round

These hold under (Nest) with every axiom: n = 2, strict (G), (IB), (LA), (S) with closed sections for every model,
and (C). One reader each beyond the authors unless noted.

1. **(RATE)** (S4 Thm. RATE, confirmed). The following are equivalent:
   - R3₁, R3₁ᵘ, SR₁;
   - R3₂, R3₂ᵘ, SR₂;
   - NDL: there are no S_k with inf μ̄(S_k) > 0, S_k ≤₁ R_k → 1 and S_k ≤₂ V_k → 0.

   If SR₁ fails at m, a doubly-light sequence exists with μ̄(S_k) ≥ m/3 and S_k ⊆ [m/3, 1−m/3).
2. **(SR)** If one world has a strictly positive endorsing charge vanishing at the far end of the chain (ν₂(c_t) → 0,
   or ν₁(d_t) → 0), then (1) holds. This covers every additive partner with integrable density, and the whole Q1.C1
   setting.
3. **(MP♯)**
   - For non-null Z and every A ∈ 𝒰₁(Z): d_t ≤₂ A for all t ∈ [τ(Z),1). This fails for some A ∈ 𝒰₁(Z) at every
     t < τ(Z).
   - For ν ∈ 𝒱₂: ν(d_{τ(Z)}) ≤ inf_{𝒰₁(Z)} ν ≤ lim_{t↑τ(Z)} ν(d_t).
   - η₁(Z,1) = 1 − τ(Z), and next to μ̄, κ₁(Z) = η₁(Z,1).
4. **(Loop)**
   - For all s, t ∈ (0,1): c_s ≤₁ d_t or d_t ≤₂ c_s.
   - For t > T(s): 𝒰₁(c_s) ⊆ 𝒰₂(d_t) ⊆ 𝒰₁(c_{s′}) for s′ ≤ S(t), and S(t) ≤ s.
5. **(QC-J)** QC₁ ⟺ QC₂ ⟺ κ₁(c_s) > 0 ∀s > 0 ⟺ κ₂(d_t) > 0 ∀t < 1. Also QC ⇒ ¬R1.
6. **(Block)** For A ∈ 𝒰₁(Z) and t ≥ τ(Z), world 2 accepts Q ≤₂ A ∩ c_t for every Q ⊆ d_t∖A (§10.2).
7. **(UE)** Uniform escape at x along a disjoint family raises the common segment by κ along disjoint 3-unions.
8. **(Example A)** There is a system with every axiom, both worlds additive (world 2 = μ̄), and η₁(P,1) ≤ μ̄(P)²/2.
   Hence no rate linear in μ̄(P) follows from the axioms. By variants, any polynomial order m^q (q > 1), and also
   e^{−c/m}, occurs.
9. **(LIN)** Next to world 2 = μ̄, a linear rate η₁(P,1) ≥ cμ̄(P) excludes N4 ratio certificates with ε < ca.
10. **(Without closedness, S3.1)** Every axiom except closed sections, at both worlds, is compatible with a mirrored
    simple pair through one disjoint family, with ¬SP^reg at both worlds. The non-closed sections are
    S₁(E₁ = d_a) = [0,1) and S₂(E₂ = c_{b₀}) = (0,1].
11. **(Architectures)**
    - In band ∪ translates worlds (generators 1_F − 1_{c_a}), closed world-1 sections imply inf_𝓕 μ̄(F) > 0, hence
      QC₁ and ¬R1 (S3.2). The converse is false (§2.3).
    - Fibrewise band ∪ translates violates (K) (S3.4).
    - Any world accepting right-packing of the targets of a simple certificate has a non-closed section (S3.3).

---

## 12. The precise remaining form of (R1)–(R3)

All under (Nest) with every axiom, closed sections for every model.

- **(R1) Mirrored simple pairs.** Are there s₀ ∈ (0,1) and a uniformly Cesàro-thin family 𝒜 with c_{s₀} ≤₁ A for all
  A ∈ 𝒜? This is equivalent to the original form by MP-loop. Then automatically d_t ≤₂ A for all t ≥ T(s₀) (MP♯).
  - **Weaker target:** ¬QC (R1′), the same with "μ̄(A_k) → 0" in place of "Cesàro-thin". It is implied by R1 and is
    also mirrored (QC-J). Excluding R1′ excludes R1.
  - **Known constraints on a construction:**
    - both worlds fail SP^reg, and neither is complete, (CP-a) or has a leading charge;
    - the targets do not concentrate (Lemma T);
    - no world packs its targets toward its far end (S3.3);
    - (K) at cuts ≥ T(s₀) cannot transport them (§10.2);
    - it does not lie in band ∪ translates with closed sections (S3.2) or in fibrewise band ∪ translates (S3.4);
    - dropping closedness at both worlds makes it realisable (S3.1).
  - **Any exclusion** must obtain world-1 packing of thin A ∩ c_t from (K) at cuts below T(s₀), or from world-2
    closedness at non-segment sources.
- **(R2) General certificates.** Unchanged: if neither world has a simple certificate, must both satisfy SP^reg? It is
  open even next to an additive world (Q1.C1).
  - New: the qualitative rate is available there (Cor. SR), so R2 must use the ¬SP certificate itself.
  - The only rate the MP route can use is linear (LIN), and it is not a consequence of the axioms (Example A).
- **(R3) — to be restated.** The "missing lemma" reading is withdrawn (§9.3). What remains is
  **CONJECTURE S4.1 (NDL in every system)**, equivalently qualitative R3 at either world. It is open only when
  neither world has an end-vanishing SP weight, and it is not known to bear on R1 or R2. The linear form
  (η₁(P,1) ≥ cμ̄(P)) is **false** in general (Example A).

---

## 13. Files (`s34ref_py/`, run with `python3 -I`)

- `s3_sections.py` (+ `.out`): exact rational section computations for band ∪ translates.
  - (1) S3.2 formula against bisection: 12 random cases, maximum error 8·10⁻¹³.
  - (2) The open-section witness E₁ = d_a with the dyadic family: ends 1 − μ̄(A_j), and c₁ ≤₁ d_a is rejected.
  - (3) The referee counterexample to sufficiency: min μ̄(F) attained, yet the section is [0,0.7).
- `s31_grid.py` (+ `.out`): S3.1 on a grid with a non-uniform disjoint family.
  - Nonpositive vectors are rejected.
  - (K): 0 failures and (U): 0 failures (600 models × 95 cuts).
  - World-1 and world-2 section ends match 1 − μ̄(A_j) and μ̄(F′_j).
- `s34_fibre.py` (+ `.out`): S3.4. (K) fails in all 124 cut pairs tested, while the global bands accept both
  comparisons in each.
- `s4_exampleA.py` (+ `.out`): Example A.
  - The closed form T(s), with T(s) < s for s > 3/4 (the Loop-lemma gap).
  - (K): 0 failures over 20,000 cut pairs.
  - MP♯ bathtub: 0 violations over 5000 sets.
  - η₁/m² → 1/2.
