# R9: referee report on R7_notes.md (round 9, 12 Oct 2026)

Scope: the items in the commission. I checked every step line by line against BRIEF.md. The checks covered three things:
- decomposable domains: every model built must have its advice in the advice ranges, or be a splice, inside M;
- (G) and (IB) are applied only inside M;
- (S) is used only as stated: competitive against M, with closed sections {p : C_p ⪯_i X} for X ∈ M.

Context read: R2, R5, R6 and R8. R6's repaired form of R2 Thm N is used: "int" means interior relative to aff Δ. No scripts were needed; every step is finite-dimensional convex analysis or a pointwise comparison, and all were redone by hand.

Verdict scale: CORRECT / CORRECT WITH REPAIR / GAP / FALSE.

---

## Summary table

| Item | Verdict |
|---|---|
| §1 class 𝓛₂ ((G) strict/weak, (IB), completeness) | CORRECT |
| §1 standing facts (L1), (Au), (PB), (Sp), (T7) | CORRECT |
| §1 primary supports, T_X, 𝔅_t, X ∈ 𝔅_t ⇔ t ∈ T_X | CORRECT |
| Lemma F | CORRECT |
| (F*) | CORRECT |
| Endpoint fibres are additive decomposable domains | CORRECT |
| **Lemma A** | CORRECT WITH REPAIR (a hypothesis is missing from the statement; every application satisfies it) |
| **Lemma SF**: non-ideal set relatively open; each non-ideal level gives an undominated Z₂ improvable at world 1 with the same primary; use of (T7) | CORRECT |
| **Corollary SF-L** | CORRECT |
| **Lemma BWC** | CORRECT |
| **Lemma 7′** | CORRECT |
| **Theorem 1′₂**, case (a0) | CORRECT (with Lemma A repaired) |
| case (a1): position bullets, sub-case R⁰ null (multipliers, splice) | CORRECT |
| case (a1), sub-case R⁰ non-null: (min,min), (max,max), (min,max), (max,min) | CORRECT |
| case (b): supports, no disjoint Θ's, θ₀ = 0, θ₀ ∈ (0,1) | CORRECT |
| case (c): world swap, Steps 0–5 | CORRECT WITH REPAIR (one sentence in Step 3 gives a wrong reason for a true conclusion) |
| case (c), branch t_A = 1 | CORRECT, but redundant: Step 5 already covers t_A = 1 |
| Invocations of R2 Lemma 1, Thm 7, Thm R | CORRECT |
| Invocations of R2 Thm N | CORRECT as special-case statements (n = 2, aff-Δ interior). The phrase "R2 Thm N forbids nesting" on faces is a misattribution; the tool is Lemma A (see below) |
| Remark 1 after the proof ("(S) enters only through (T7)") | CORRECT WITH REPAIR (wording) |
| Remark 3 / §5.1 (Ex. 4.3's face is incompatible with (S)) | CORRECT WITH REPAIR (needs "as a face 𝔅_t, t ∈ (0,1), of the system", plus (LA)) |
| §5.2 | CORRECT (pure convexity; (S) not even needed) |
| §5.3 | CORRECT (= case (a1), (min,max)) |
| §5.4 and §0 item 3: "the staircase lives only at vertices and edge endpoints" | FALSE as worded (counterexample below). TRUE for interior faces t ∈ (0,1), with a short proof R7 does not give (supplied below). Not used in the theorem |
| §5.5 | CORRECT (accurate summary of case (c)) |
| Corollaries 4.1, 4.2 | CORRECT |

**Bottom line.** Theorem 1′₂ is proved. None of the defects touches the logic of the proof. The two that need fixing in the text are Lemma A's statement and the §0.3/§5.4 narrative claim.

---

## §1. Setting and standing facts

**Class 𝓛₂.**
- Composite strict (G) holds. Suppose Y is pointwise at least as good as X at i, and strictly better on a non-null N. Off N the kinds of advice coincide, since distinct kinds of advice have distinct ranks off null sets. So P_i(Y) ≤ P_i(X). If equality holds, then φ_i agrees a.e. on N, so ψ_i is strictly lower a.e. on N, and S_i(Y) < S_i(X).
- Weak (G) holds similarly. (IB) holds because both levels are integrals.
- × is weakly worst for φ_i at both worlds, by weak guidance. This is used repeatedly below.

**(T7).** Per R2 Thm 7 and R6, (C) is not needed. The tie with a selected C_p (Fact 0(b)) is a tie in both levels, so improvability transfers from X to C_p.

**Primary supports.**
- 𝒫 is convex and compact. Aumann's theorem applies: the advice ranges are finite, the envelope is integrable, and μ is atomless.
- X ∈ U_L implies π(X) is weakly Pareto-minimal: a Y strictly lower in both primaries strictly beats X at both worlds.
- Separation gives T_X ≠ ∅. T_X is closed and convex.
- By (PB), X ∈ 𝔅_t ⇔ t ∈ T_X.
- On 𝔅_t, P_2 = c_t − κ_t P_1 with κ_t = t/(1−t).

**Lemma F: CORRECT.** For t ∈ (0,1), the t-sum argument forces both primary inequalities to be equalities. For t = 1, P_1(Y) ≤ min forces Y ∈ 𝔅_1. In (ii), P_2 need not be preserved, and R7 does not claim that it is.

**(F*): CORRECT.** By F(i), a dominator lies in the same fibre. With equal primaries, ⪯_i reduces to S_i.

**Endpoint fibres: CORRECT.**
- For t ∈ (0,1), 𝔅_t^± are the pointwise φ_1-min (or max) selections within the advice ranges of 𝔅_t, by (PB) applied on 𝔅_t.
- On those advice ranges φ_1 is constant, and then φ_2 is constant because the t-sum is constant and 1−t > 0. Composite strictness makes ψ_1 and ψ_2 strictly guiding there.
- "If J_t is a point then 𝔅_t is such a domain": if φ_1 were non-constant on the advice ranges of 𝔅_t on a non-null set, the pointwise φ_1-min and φ_1-max selections would give different values of P_1. Correct.

## Lemma A: CORRECT WITH REPAIR

**Defect.** The statement assumes only that (S_1, S_2) is strictly guiding on 𝔇, and that weak dominators of members of 𝔇 lie in 𝔇 with the same primaries. The first proof step ("A, B are (S_1,S_2)-Pareto in 𝔇") needs more. It needs every member of 𝔇 to have the same primaries as A, so that a Y ∈ 𝔇 that is S-better dominates A. Without that, a Y ∈ 𝔇 with lower S but higher P_1 does not dominate.

**Repair.** Add to the hypotheses: "φ_1 and φ_2 are a.e. constant on the advice ranges of 𝔇 (so P_1, P_2 are constant on 𝔇)". Every application satisfies this:
- case (a0): 𝔇 = 𝔅_{t₀} with J a point;
- case (a1), (min,min) and (max,max): 𝔇 = 𝔅^∓;
- case (b), θ₀ = 0: 𝔇 = 𝔅'' = argmin_𝔐 φ_2, where φ_1 is constant on the advice ranges of 𝔐 and φ_2 on those of 𝔅''.

**Rest of the proof, checked.**
- Sign patterns: c = (+,−) on R1 and c′ = (−,+) on R2. Both pairs of kinds of advice are in the advice ranges of 𝔇 because A, B ∈ 𝔇.
- The A and B inequalities.
- s_A ∈ (0,1]: s_A = 0 fails on R1. s_A ≠ 1: it fails on R2.
- s_B ∈ [0,1): s_B = 1 would need c_1 ≤ 0 on R1. s_B > 0: s_B = 0 fails on R2.
- R1 gives s_B ≤ s_A and R2 gives s_A ≤ s_B. Equality holds in all four inequalities a.e. on R.
- The (Sp) splice E lies in 𝔇 (a splice of 𝔇-members) and is a pointwise s*-minimiser.
- A weak dominator Y lies in 𝔇 with the same primaries. Strictness at one world would lower the s*-sum, because s* ∈ (0,1). So E ∈ U_L, and E is incoherent, contradicting (L1).

**Note.** Lemma A deliberately does not invoke R2 Thm N on 𝔇. That would require (LA), (S), (C) for the additive face system, through Lemma U, and those are not available. Lemma A uses (L1) of the global system instead. This is the right design. It also means that the sentences "R2 Thm N forbids nesting" in §0 item 3 and in the closing "Answer to R7" should cite Lemma A, not Thm N.

## Lemma SF: CORRECT

- **𝒦 and g_l.** 𝒦 is the Aumann integral of the advice-range correspondence of 𝔅_t, so it is convex and compact. g_l is the lower envelope of the convex compact projection to (P_1, S_l). So g_l is convex and finite on J, hence continuous on int J.
- **Relatively open.** The ideal set is the preimage of the closed set 𝒦 under the continuous map x ↦ (x, g_1(x), g_2(x)) on int J. So the non-ideal set N is relatively open in int J. This is convexity alone; (S) is not used here.
- **Z₂ is undominated.** By F(i), a weak dominator Y lies in F_t(x). From S_2(Y) ≤ g_2(x) we get S_2(Y) = g_2(x). The lexicographic choice of Z₂ then gives S_1(Y) ≥ S_1(Z₂), so no strict improvement exists. Z₂ ∈ U_L.
- **Improvable at world 1 with the same primary.** Z₁ ∈ 𝔅_t ⊆ M has P_1(Z₁) = x = P_1(Z₂). Non-ideality gives S_1(Z₁) = g_1(x) < S_1(Z₂). This matches the definition of "improvable at 1" in (T7) exactly.
- **Use of R2 Thm 7.** It is used in U_L form with world i = 1. The closed section used is {p : C_p ⪯_1 Z₁} with Z₁ ∈ M, so it stays within (S) as stated.
- **Conclusion.** N is countable and relatively open in an open interval, so N = ∅.

## Corollary SF-L: CORRECT

- Ideal level plus Pareto in the fibre (F*) means X attains both minima. Otherwise the ideal point would Pareto-improve on X.
- An interior point of the domain of the convex g_l has a finite subgradient −λ. Then S_1(Y) + λP_1(Y) ≥ g_1(P_1(Y)) + λP_1(Y) ≥ g_1(x) + λx = S_1(X) + λP_1(X) for all Y ∈ 𝔅_t. The same holds for S_2.
- The pointwise form follows from (PB) on 𝔅_t.
- Remark: the multipliers need not be unique. Every later argument works for an arbitrary choice from the subdifferential, and the multiplier comparisons in (a1) show that any choices coincide.

## Lemma BWC: CORRECT

- The ideal I exists by SF, lies in U_L by (F*), and SF-L applies to it.
- On Q, all kinds of advice in {+,0,−} in the advice range have equal φ_1, hence equal φ_2 (the t-sum is constant, and t ∈ (0,1)). So ψ_1 and ψ_2 are strict among them.
- If × is in the advice range of 𝔅_t, it must be φ-tied with the minimisers. Weak guidance makes both of its φ-values ≥, and the t-sum is equal, so it is ranked last by both ψ's.
- The two Lagrangians therefore select the world-1-best and the world-2-best advice in the advice range. These differ on mixed problems whenever at least two of {+,0,−} are present, because the two world orders are reverses. Contradiction on the non-null set Q.
- The single use (Step 2, Q = R2, {a,b} = {−,0}) has its hypothesis verified in Step 1.

## Lemma 7′: CORRECT

- A tie with a selected C_p means equality at all levels.
- Z ≺_i C_p, so p ∉ A_i(Z), which is closed by (S). On a neighbourhood V of p, C_q ⪯_i Z fails. If prefix(C_q) <_lex prefix(Z), then C_q ≺_i Z, which is impossible. So prefix(C_q) ≥_lex prefix(C_p), and p is a lexicographic local minimum.
- Countable-base injectivity: two values minimal on the same basic set are equal, because the lexicographic order on ℝ^{k−1} is total and antisymmetric.
- Any n. Only (S) and Fact 0(b), hence (LA), are used.

---

## Theorem 1′₂

**Notation and (A1)–(B2): CORRECT.**
- On R1 and R2 both kinds of advice are in the advice ranges of M, since A and B give them.
- Signs: d_1, d_2, e_1, e_2 ≥ 0 by weak guidance.
- The four inequalities are the pointwise t-minimality of A's and B's advice, checked one by one.
- Trichotomy (a)/(b)/(c): exhaustive. In (b) the intersection is {0} or {1}; it cannot be {0,1}, because then T_A = T_B = [0,1] and we are in (a).

### Case (a): CORRECT

- (A1) and (B1) at t₀ give d_2 = κd_1. (A2) and (B2) give e_2 = κe_1. On R⁰, equal φ_1 together with the equal t-sum gives equal φ_2. On R1⁺ we have d_1 > 0, and on R2⁺ we have e_1 > 0.
- **(a0).** J is a point, so 𝔅 is an additive face. Lemma A (repaired) applies, using F(i).
- **(a1) position bullets.** All six were checked.
  - A interior: on R⁰∩R1, the second Lagrangian strictly prefers the φ-tied 0 to +. On R⁰∩R2, the first prefers 0 to −.
  - B interior: on R⁰∩R1, the first prefers + to 0. On R⁰∩R2, the second prefers − to 0.
  - Endpoint bullets: each uses advice already in the advice range of 𝔅, namely the other model's advice, with strictly smaller or larger φ_1.
- **Sub-case R⁰ null.**
  - Each endpoint position kills R1⁺ or R2⁺, which are now all of R1 or R2. So both models are interior.
  - Multipliers:
    - on R1: σ_1 + λ_A d_1 ≥ 0 ≥ σ_1 + λ_B d_1, so λ_A ≥ λ_B;
    - on R2: τ_1 + λ_A e_1 ≤ 0 ≤ τ_1 + λ_B e_1, so λ_B ≥ λ_A;
    - μ follows the same way, with ψ_2(0) − ψ_2(+) on R1 and ψ_2(−) − ψ_2(0) on R2.
  - Equality forces ties on R. A and B agree off R, because the coherent pair differs exactly on R1 ∪ R2. So every splice is a pointwise minimiser of both Lagrangians and lies in 𝔅.
  - Undominatedness: by F(i), a dominator has the same P_1, and Lagrangian optimality then gives S_l(Y) ≥ S_l(E).
  - The (Sp) splice is incoherent. Contradiction with (L1). Correct.
- **Sub-case R⁰ non-null.** Both models are at endpoints. With int J ≠ ∅ the two endpoints are distinct.
  - (min,min) and (max,max): both models lie in 𝔅^∓. Weak dominators of members of 𝔅^∓ lie in 𝔅 (F(i)) at the same P_1, hence in 𝔅^∓. Lemma A applies.
  - (min,max): R2⁺ is null, so R2 = R2⁰.
    - For the ideal I at an interior level, I's advice on R2⁰ is not 0 (ψ_2 prefers −), not − (ψ_1 prefers 0), and not × (φ-tied and ψ_1-worst).
    - So it is +, and + is in the advice range of 𝔅 a.e. on R2⁰.
    - If φ_1(+) = φ_1(−), then φ_2 is also tied, and ψ_2 prefers −. So φ_1(+) ≠ φ_1(−), and weak guidance gives φ_1(+) < φ_1(0) = φ_1(−).
    - This contradicts A's pointwise φ_1-minimality on the non-null set R2. Correct.
  - (max,min): the mirror argument on R1⁰. I picks −, with φ_1(−) > φ_1(+), contradicting A's φ_1-maximality. Correct.

### Case (b): CORRECT

- World swap to t = 1: see case (c) for the symmetry check.
- On 𝔐 = 𝔅_1, φ_1 is constant on the advice ranges, ψ_1 is strictly guiding, and world 1 is S_1. By F(ii), dominators stay in 𝔐.
- Weak Pareto in (S_1, P_2): a Y that is strictly better in both coordinates is ≺_1 (same P_1, lower S_1) and ≺_2 (lower P_2).
- Supports exist by Aumann and separation. (PB) applies on 𝔐.
- The inequalities for A and B were checked. θ = 1 is excluded for both: τ > 0 for A and σ > 0 for B.
- **Disjoint Θ's are impossible.** In both orderings the larger θ is < 1, and the ratio chains are contradictory:
  - θ_A < θ_B via R1;
  - θ_B < θ_A via R2.
- **θ₀ = 0.** Then d_2 = e_2 = 0. 𝔅'' is an additive face; weak dominators stay in 𝔐 and then have P_2 ≤ min_𝔐 P_2. Lemma A (repaired) applies.
- **θ₀ ∈ (0,1).**
  - d_2 = θ₀σ/(1−θ₀) > 0 and e_2 > 0.
  - Weak dominators of members of 𝔅′ stay in 𝔅′ with equal S_1 and P_2, since θ₀ ∈ (0,1).
  - Interior P_2-levels:
    - A: the P_2-minimum excludes + on R1, and the P_2-maximum excludes − on R2;
    - B: the minimum excludes 0 on R2, and the maximum excludes 0 on R1.
  - In each case the competing advice is in the advice range of 𝔅′, because the other model gives it.
  - A subgradient of the convex lower envelope of {(P_2, S_2)} over 𝔅′ gives multipliers ν. R1 gives ν_A ≤ ν_B (d_2 > 0) and R2 gives ν_A ≥ ν_B (e_2 > 0). Ties follow.
  - The splice minimises S_2 + ν*P_2 over 𝔅′, so it is undominated and incoherent. Correct.
- The parenthetical "re-proves R2 Thm 6" is accurate in substance. With φ_1 ≡ 0, 𝔐 = M and the argument is R2 Thm 6 with the worlds swapped. No guidance of ψ_2 is used where φ_2 is strict.

### Case (c): CORRECT WITH REPAIR

- **World swap.** g′ = (−g_2, −g_1) maps mixed problems to mixed problems, + ↔ −, r ↦ 1−r and D_{[α,β]} ↦ D_{[1−β,1−α]}. It keeps A as the inner model, maps T ↦ 1−T, and preserves class 𝓛₂ (weak guidance and composite strictness are rank statements).
  - The map is orthogonal, so a standard Gaussian μ is invariant. For a non-isotropic Gaussian, the image system lives on the pushed-forward Gaussian. The proof uses only atomlessness and the positive radial density needed for (Sp), so nothing changes.
  - Disjoint closed intervals are ordered, so "T_B below T_A" can be assumed.
- **Step 0.** Both branches were checked: κ_A e_1 ≤ e_2 ≤ κ_B e_1 with κ_B < κ_A, and the t_A = 1 branch. Then t_A := min T_A > max T_B ≥ 0.
- **Step 1.**
  - The identity f(t) = f(t_A) + (t_A − t)(a+b) is correct.
  - For t < t_A, − is a t-minimiser in the advice range of M: 0 is φ-tied, + has f(t) ≥ 0 (if + is present), and × is weakly worse.
  - Any + that is a t-minimiser has a = b = 0.
  - So the advice range of 𝔅_t on R2 contains − and 0, and its {+,0,−} part is φ-tied.
- **Step 2.** BWC applies. J_t is a point, so 𝔅_t is an additive face.
- **Step 3.**
  - On R2, the S_2-minimiser picks − and the S_1-minimiser picks the world-1-best advice, which is not −.
  - W_t is undominated, by F(i) and the Z₂ argument.
  - W_t is improvable at world 1 with strict inequality: it picks − on the non-null set R2, where ψ_1 is strictly worse than 0, so S_1(W_t) > min S_1.
  - (T7) then makes {P_1(π_t)} countable.
  - Berge's theorem gives an upper hemicontinuous argmin; with singleton values it is continuous, so P_1(π_t) is constant.
  - **Repair, wording.** "Points of F_t with equal P_1 and t < 1 also have equal P_2" does not apply as written, because π_t and π_{t′} lie in different faces. The conclusion is still true. Let π_t = (x*, y) and π_{t′} = (x*, y′). t-optimality of π_t gives (1−t)y ≤ (1−t)y′, and t′-optimality of π_{t′} gives the reverse, so y = y′.
  - Closedness of T_{π*} then gives T_{π*} ⊇ [0, t_A].
- **Step 4.** T_X depends only on π(X). A t ∈ T_B ∩ (0, t_A) would force T_B = T_{π*} ∋ t_A. So T_B = {0}, and π(B) ≠ π*, since t_A ∈ T_{π*} ∖ T_B.
- **Step 5.**
  - π* is P_1-minimal on F_0: compare the small-t optimality of π* with any q ∈ F_0. Hence P_1(B) > P_1(π*).
  - B is weakly Pareto in (P_1, S_2) over 𝔅_0, where P_2 is constant, so a support θ exists.
  - θ = 1 is excluded by the π*-models, which lie in 𝔅_0.
  - θ < 1 is excluded on R2: − is φ-tied with B's 0, so it is in the advice range of 𝔅_0, and ψ_2(−) < ψ_2(0).
- **Branch t_A = 1.** Correct: θ = 0 is excluded by the π*-models, and θ > 0 by R2 blindness with ψ_1. But the branch is **redundant**. Steps 0–5 never use t_A < 1: Step 1 runs on (0,1) and Step 5 is independent of t_A. It can be deleted or kept as a remark.

### Invocations of R2 results: all CORRECT

- **R2 Lemma 1 (L1):** under (LA), (S), (C). The incoherent undominated splices in Lemma A, (a1) and (b) are the contradictions.
- **R2 Thm 7 (T7):** in SF (world 1, Z = Z₁ ∈ M) and in Step 3 (world 1, Z = the S_1-minimiser ∈ 𝔅_t ⊆ M).
- **R2 Thm R:** Corollary 4.1 uses the ⇐ direction. Its hypotheses (G), (IB), (LA), (S), (C) hold for 𝓛₂ systems (§1 above), and R6 found Thm R CORRECT.
- **R2 Thm N:** invoked only as "Theorem 1′₂ contains the additive case". With φ ≡ 0, every T_X = [0,1], case (a0) applies, and Lemma A gives R2 Prop N2. This is consistent with R6's repair, because R7 defines strict nesting as α_B < α_A ≤ β_A < β_B, i.e. K_A ⊂ int_{aff Δ} K_B. I checked that this equivalence is right, and that R6's counterexample pair [0,½] ⊂ [0,¾] is correctly excluded.
- **Misattribution:** see the note under Lemma A.

### Remark 1: CORRECT WITH REPAIR
"(S) enters only through (T7)" is inaccurate. (S) also enters through (L1): Fact 0's KKM step uses both the closed sections and competitiveness against M. Suggested replacement: "(S) enters through (L1) and (T7); (C) only through (L1)."

### Domain and (S) discipline
Every model constructed lies in M:
- Z₁, Z₂, I, W_t and the S_1-minimisers lie in faces 𝔅_t ⊆ M;
- the φ_1-extremal selections are models with advice in the advice ranges;
- the splices of A and B lie in M because it is a decomposable domain;
- the π*-models in 𝔅_0 are models with advice in the advice ranges.

(G) and (IB) are applied only to such models. Closed sections are used only with X ∈ M (Z₁, the S_1-minimisers, and inside Fact 0). (LF) plays no role. No all-model assumption was found.

---

## Part (A) claims (§0 items 2–3, §3 Remark 3, §5)

**§5.1 / Remark 3: CORRECT WITH REPAIR.**
- Checked. In Ex. 4.3, P_1 = ½(λ−λ′) = −P_2, so the configuration is the t = ½ face (κ = 1) with J = [−½, ½].
- On the fibre λ − λ′ = 2x, put s = λ + λ′. Then S_1 = −2s and S_2 = s, so g_1 and g_2 are attained at opposite ends of the s-range. Every interior level is non-ideal, so SF together with (T7) is contradicted.
- Repair: state the hypothesis precisely. The conclusion is "no (LA),(S),(C) 𝓛₂ system has the 4.3 configuration as a face 𝔅_t with t ∈ (0,1)". A system in which the 4.3 set sits inside M but is not a face is not addressed by SF; it is addressed by Theorem 1′₂, as far as nesting goes. Also, (S) fails only jointly with (LA), since (T7) uses Fact 0.

**§5.2: CORRECT.** A single non-ideal interior level would make the non-ideal set a singleton, which is not open. This is convexity only; (S) is not needed.

**§5.3: CORRECT.** It is case (a1) (min,max), as checked above.

**§5.4 and §0 item 3 ("the countable staircase lives only at vertices of the primary range and at endpoints of primary edges"): FALSE as worded.**

*Counterexample.*
- Take any additive strictly guiding (LA),(S),(C) system on a decomposable domain whose Bayes path has B_0 ≠ B_1, written in class 𝓛₂ as world 1 = lex(0, ℓ_1) and world 2 = lex(ℓ_2, 0). Here ℓ_2 is strictly guiding, so the composite is strict.
- Then 𝒫 = {0} × [a, b] with a < b. This is an edge, and F_1 = 𝒫.
- For s ∈ (0,1), B_s sits at an interior point of this edge. B_s is improvable at world 1 by B_1: equal P_1 = 0, smaller S_1 = L_1.
- So a continuum of improvable members fills the interior of a primary edge. (T7) is not violated, because all of them share the single world-1 primary level 0.

*What is true (repair, PROVED here).* For t ∈ (0,1), no member of U_L at an interior level x ∈ int J_t is improvable at either world.
- World 1. Let m(x) = min{S_1(Z) : Z ∈ M, P_1(Z) = x}. It is convex on the P_1-range of M, hence continuous on int J_t, which lies inside that range's interior. Let X ∈ U_L be at level x. By SF-L, S_1(X) = g_1(x). X is improvable at 1 iff m(x) < g_1(x). The set O = {x ∈ int J_t : m(x) < g_1(x)} is open, because m and g_1 are continuous. Each x ∈ O carries an ideal point in U_L that is improvable at 1, so O is countable by (T7). Hence O = ∅.
- World 2. The same argument works with P_2 = c_t − κ_t P_1, which is an affine bijection of levels.

So the correct statement is: on interior faces, improvable members occur only at J_t-endpoints and at vertices (faces where J_t is a point). On the boundary faces F_0 and F_1 they can fill the whole face, sharing one primary level of the corresponding world. In the proof these cases are handled by (b) and (c), not by Lemma A. The theorem does not use this claim.

**§5.5: CORRECT.** It is an accurate summary of case (c). Note that BWC flattens every face with t ∈ (0, t_A), not only the faces "strictly between" T_B and T_A.

**§0 item 2: CORRECT.**

**Corollaries 4.1 and 4.2: CORRECT.** Additive systems are in 𝓛₂ (take φ ≡ 0), so the "exactly the targets" equality holds on a fixed domain, and (LF) is a property of the domain.

---

## Requested edits to R7 (minimal)
1. Lemma A: add "φ_1 and φ_2 are a.e. constant on the advice ranges of 𝔇".
2. Case (c), Step 3: replace the "equal P_2" sentence with the two-line optimality argument.
3. Case (c): mark the t_A = 1 branch as redundant (Step 5 covers it).
4. Remark 1: say that (S) also enters through (L1).
5. §0 item 3, §5.4 and the closing paragraph:
   - restrict the staircase claim to interior faces t ∈ (0,1), and add the O-open argument above;
   - acknowledge boundary-face staircases;
   - cite Lemma A, not R2 Thm N, for "no nesting on additive faces".
6. §5.1 and Remark 3: say "as a face 𝔅_t, t ∈ (0,1)".
