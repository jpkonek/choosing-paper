# M2. (NC) is not needed next to two leading worlds: the forced fixed point

16 Oct 2026, round 20 (BRIEF17; BRIEF13 rules). Labels: **PROVED** (full proof here, from results the write-up or
refereed notes mark proved, each named), **CHECKED**, **CONJECTURE**, **NUMERICS** (`m2py/`, run with `python3 -I`
from inside it; no proof rests on it). No assumption is added. Notation: write-up §§2–3 (axioms, M_U, regular
models, relevant comparisons, Def. addup), L4 §§1–2 (ν ∈ ba₊(M)³, t·ν, Gap_t, d_t, c^ν, Lemma L4.0, Thm L4.1, (B1)),
K2 §§1–2 (vector form (1.1), divisibility, Thm K2.1, Prop K2.2), K3 §§1–2 (𝒩(𝔊), K3.1(a)–(c)), B1 §1 (leading
density, Lemma B1.0). World 1 is the world under study; n ≥ 2 worlds unless stated.

---

## 0. Outcome

**(NC) is neither proved nor refuted in general, and no world failing (NC) was constructed. What is PROVED is the
nearby result that matters for L4: next to two partner worlds with leading densities, L4's fixed point exists with
no hypothesis at all on the third world. In that class strongly (M1) worlds are inside L4's reach.**

The leading-density condition on the partners is (RL) below. Additive worlds with integrable densities satisfy it.

**Theorem M2.6 (PROVED).** Assume (H_U), and that worlds 2 and 3 satisfy (RL) with densities ρ₂, ρ₃ > 0 a.e. on M.
Assume nothing about world 1 beyond strict (G) and (IB). Then there is ρ₁ ∈ L¹(M), ρ₁ ≥ 0, such that
c := (ρ₁σ₁, ρ₂σ₂, ρ₃σ₃) satisfies L4's standing hypotheses (B1):
- (γ₀): d_t(c) = 0 at every t ∈ Δ;
- T1 = B_{p*} ∪ S with S ⊆ Z_{p*}, where either p* ∈ Δ°, or p* = e₁ and ρ₁ = 0 a.e. on E₁(T1) ∩ M.

Two consequences follow.
- If ρ₁ can be taken > 0 a.e. on M, (H_U) is contradictory (M0closed(a)).
- Otherwise L4.9 applies. A cover forces configuration (I₂)/(I₃) or (V), with the blind set Λ♮ defined below.
  This Λ♮ is contained in L4's blind set Λ₁ whenever world 1 satisfies (NC).

**The mechanism.**
- L4.1 used an endorser of *all* relevant world-1 comparisons, and that is (NC).
- Here the endorser is taken from a smaller family 𝔉𝔏: the comparisons that competitiveness **forces** next to the
  partner worlds, together with their **closed-section limits**.
- Every member of 𝔉𝔏 is divisible (Lemma M2.2). So K2.1 and Hahn–Banach give an endorser φ, with no hypothesis on
  world 1 (Cor. M2.3).
- A modified KKM argument (Thm M2.4) shows that φ already makes the gap vanish. It runs the KKM lemma so that the
  dominator's world-1 comparison is a limit of forced ones.
- Separation gives admissibility of T1 (Prop. M2.5).
- Rigid comparisons, where K2.1 says nothing, are never used.
- This is the brief's "limiting/compactness argument using closed sections". It is applied to the forced family
  rather than to rigid comparisons, and it closes the family under limits instead of proving (NC).

**The single obstruction left by the argument (§6).** The forced KKM needs (RL-1) at every partner world:
competitiveness failing at a partner j must give a ψ_j-strict improvement. Without that, the world-1 comparison
supplied by competitiveness can be rigid.
- So a world failing (NC) can matter for T1 only if one of its two partners fails (RL).
- There, and in the general three-world case, L4.1 still needs (NC). It needs it only on the dominance-and-target
  family 𝔇_k ∪ 𝔗_k (Prop. M2.7).

| | Statement | Label |
|---|---|---|
| M2.1 | q ↦ ψ_j(C_q) is lower semicontinuous at every (RL) world with closed sections | PROVED |
| M2.2 | forced pairs and their closed-section limits are accepted at world 1 and divisible | PROVED |
| M2.3 | 𝒩(𝔉𝔏) ≠ ∅ with no hypothesis on world 1; a maximal-support element exists | PROVED |
| M2.4 | forced KKM: every φ ∈ 𝒩(𝔉𝔏) has Gap_t ≡ 0, so c^φ has (γ₀) (any n, any target) | PROVED; NUMERICS |
| M2.5 | T1 is c^φ-Bayes at some p* ∈ Δ°, or p* = e₁ with ρ₁ = 0 on E₁(T1) ∩ M | PROVED; NUMERICS |
| M2.6 | L4's (B1) without (NC) next to two (RL) worlds; contradiction if Λ♮ is null, else L4.9's dichotomy | PROVED (L4.9 itself is unrefereed) |
| M2.7 | in general L4.1 needs (NC) only on 𝔇_k ∪ 𝔗_k | PROVED (by inspection of L4.1) |
| Q_M2 | does some full system have a world failing (NC)? does it matter for T1 when both partners are (RL)? | first open; second answered **no** by M2.6 |

---

## 1. Setting and definitions

Standing hypotheses for §§1–3:
- n ≥ 2, any K′ ⊆ Δ°, U = D_{K′}, M_U;
- a ranking with strict (G) and (IB) at every world, (LA), and (S): a selection p ↦ C_p ∈ C_L, competitive on
  supp p, with closed sections {p : C_p ⪯_i X} for every i and every X ∈ M_U.

(C) is not used in §§1–3. ψ_j(X) := ∫_{E_jX ∩ M} ρ_j dμ.

**(RL) at world j ≠ 1.** World j has a density ρ_j ∈ L¹(M), ρ_j > 0 a.e., such that for every C ∈ C_L and every
regular X:
- **(RL-1)** ψ_j(C) < ψ_j(X) ⇒ C ⪯_j X;
- **(RL-2)** C ⪯_j X ⇒ ψ_j(C) ≤ ψ_j(X).

Which worlds satisfy it:
- (RL-2) says that ρ_jμ endorses every relevant comparison (L4.9's "adds up", with a countably additive weight).
- (RL-1) adds that every ψ_j-strict worsening of a member of C_L is accepted.
- A leading density on M (B1 Def.) satisfies (RL-1) by (L1) and (RL-2) by Lemma B1.0. Additive worlds with integrable
  densities, and lexicographic refinements of them, are examples.

**Pairs.** All pairs (C, X) below have C ∈ C_L and X regular, so they are relevant comparisons at world 1, with vector
δ = 1_{E₁X} − 1_{E₁C} (which vanishes on N₊). Assume every world j ≠ 1 satisfies (RL).
- **Forced pair.** There is S ⊆ Ω with 1 ∈ S such that C is competitive on S and ψ_j(X) < ψ_j(C) for every
  j ∈ S ∖ {1}. Examples:
  - C = C_q with S = supp q ∋ 1 (K2's forced comparisons, with the leading property replaced by (RL));
  - C = T1 with S = Ω, since T1 is competitive on Ω by Lemma IC (R11, refereed in R13).
- **Limit pair.** C = C_{q*}, and there are q_m → q* with constant support S ∋ 1 such that
  ψ_j(X) < L_j := lim inf_m ψ_j(C_{q_m}) for every j ∈ S ∖ {1}. A forced pair (C_q, X) with S = supp q is a limit
  pair (constant sequence).
- **𝔉𝔏** is the set of vectors of forced pairs and limit pairs. **ℳ** := {μ|_U} ∪ {ρ_jμ|_{A_{1j}∩M},
  ρ_jμ|_{R_{1j}} : j ≠ 1}, a finite family of atomless finite measures ≪ μ (K2 (1.1) notation).

---

## 2. The forced family has an endorser, whatever world 1 is

**Lemma M2.1 (lower semicontinuity; PROVED).** If world j satisfies (RL), then q ↦ ψ_j(C_q) is lower semicontinuous on Δ.

*Proof.*
- Let q_m → q with ψ_j(C_{q_m}) ≤ s for all m, and let η > 0 with s + η ≤ ρ_j(M).
- Toggling subsets of M off the regular model P_j (ψ_j(P_j) = 0) gives, by Lyapunov, a regular Y with
  ψ_j(Y) = s + η.
- (RL-1) gives C_{q_m} ⪯_j Y for every m. The closed section gives C_q ⪯_j Y, and (RL-2) gives ψ_j(C_q) ≤ s + η.
- Let η ↓ 0. (If s ≥ ρ_j(M) there is nothing to prove.) ∎

**Lemma M2.2 (PROVED).** Let every world j ≠ 1 satisfy (RL). Every forced pair and every limit pair (C, X) has
C ⪯₁ X, and its vector δ is divisible with respect to ℳ (K2 Def.).

*Proof.*
1. **Forced pairs are accepted.**
   - For j ∈ S ∖ {1}, (RL-2) and ψ_j(X) < ψ_j(C) give C ⋠_j X.
   - Competitiveness of C on S leaves C ⪯₁ X.
2. **Limit pairs are accepted.**
   - For each j ∈ S ∖ {1}, eventually ψ_j(C_{q_m}) > ψ_j(X), because ψ_j(X) < L_j.
   - So (C_{q_m}, X) is forced through S for all large m, and C_{q_m} ⪯₁ X by step 1.
   - The section {q : C_q ⪯₁ X} is closed, so C_{q*} ⪯₁ X.
3. **Sub-moves.** Let δ′ satisfy δ′^± ⊆ δ^± with the common fraction f ∈ (0,1] in every m ∈ ℳ.
   - Let X′ be the regular model with E₁X′ = E₁C △ supp δ′.
   - By K2 (1.1), applied to the measures ρ_jμ|_{A_{1j}} and ρ_jμ|_{R_{1j}} on δ′⁺ and δ′⁻ separately,
     ψ_j(X′) = (1 − f)ψ_j(C) + fψ_j(X) for every j ≠ 1.
4. **Divisibility.**
   - *Forced pair.* ψ_j(X′) − ψ_j(C) = f(ψ_j(X) − ψ_j(C)) < 0 for j ∈ S ∖ {1}. So (C, X′) is forced, and accepted
     by step 1.
   - *Limit pair.* By Lemma M2.1, ψ_j(C_{q*}) ≤ L_j. So ψ_j(X′) ≤ (1 − f)L_j + fψ_j(X) < L_j for j ∈ S ∖ {1}. Thus
     (C_{q*}, X′) is again a limit pair along the same sequence, and is accepted by step 2.
   - Either way δ′ ∈ 𝒜₁. ∎

**Corollary M2.3 (PROVED).** Let every world j ≠ 1 satisfy (RL). Then:
- no nonnegative combination of members of 𝔉𝔏 is ≤ 0 a.e. and < 0 on a non-null set;
- 𝒩(𝔉𝔏) ≠ ∅: there is a finitely additive probability φ on M, vanishing on null sets, with φ(δ) ≥ 0 for every
  δ ∈ 𝔉𝔏;
- there is φ* ∈ 𝒩(𝔉𝔏) whose countably additive density is positive exactly off a set Λ♮ that is minimal mod null.

These hold with no hypothesis on world 1 beyond strict (G) and (IB).

*Proof.*
- The first claim is K2.1 (refereed CORRECT), applied to accepted divisible vectors (Lemma M2.2).
- In particular (NC_{𝔉𝔏}) holds. K3.1(a), whose proof is written for any family 𝔊, gives 𝒩(𝔉𝔏) ≠ ∅.
- 𝒩(𝔉𝔏) is convex and norm-closed. So fact (F2) of K3.1(c) applies verbatim, and gives φ*. ∎

*Remark.*
- 𝔉𝔏 ⊆ 𝔚₁. So 𝒩(𝔚₁) ⊆ 𝒩(𝔉𝔏), and Λ♮ is contained in L4's blind set Λ₁ whenever world 1 satisfies (NC).
- A world-1 certificate of any kind, (M1) or strongly (M1), must contain a member of 𝔚₁ ∖ 𝔉𝔏 (K2.2′ sharpened to
  limit pairs).

---

## 3. The forced KKM: the gap of the forced shadow vanishes

**Theorem M2.4 (PROVED; any n ≥ 2, any target).** Let every world j ≠ 1 satisfy (RL), and let φ ∈ 𝒩(𝔉𝔏). Put
ν := (φ, ρ₂μ, …, ρ_nμ). Then:
- Gap_t(ν) = 0 for every t ∈ Δ, and the coherent infimum is approached by selected models;
- consequently (Lemma L4.0) d_t(c^ν) = 0 for every t ∈ Δ, where c^ν = (ρ₁σ₁, ρ₂σ₂, …) and ρ₁ is the countably
  additive density of φ. This is property (γ₀).

*Proof.* Fix t ∈ Δ, a regular B, and η > 0. We find a selected C with t·ν(C) ≤ t·ν(B) + O(η).

0. **Perturbations B_±.**
   - Let φ = ρ₁μ + π, and let D_m be the localizing family of π (K3.1(b): μ(D_m) → 0 and π(M ∖ D_m) ≤ 2^{−m}).
   - Let Q^{(1)} := {h ∈ M : σ_j(h) = −σ₁(h) for all j ≠ 1}. It is non-null: it contains a neighbourhood of
     (L, −1, …, −1) ∈ U for large L, since min_{K′} m₁ > 0.
   - Choose a non-null W ⊆ Q^{(1)} ∖ D_m, for m large, with μ(W), ρ₁μ(W) and every ρ_jμ(W) below η.
   - Let B₋ (resp. B₊) equal B off W, and on W take the side of the worlds j ≠ 1 (resp. of world 1). Both are regular.
   - On W all worlds j ≠ 1 agree, so ψ_j(B₊) − ψ_j(B₋) = ρ_j(W) ∈ (0, η] for every j ≠ 1.
   - Every coordinate of ν(B_±) is within η + 2^{−m} of that of ν(B).
1. **KKM sets.**
   - For j ≠ 1, let F_j := {q : C_q ⪯_j B₊}. These are closed by (S).
   - Let O := {q : 1 ∈ supp q and C_q ⋠_j B₊ for every j ∈ supp q ∖ {1}}, and F₁ := cl O.
   - *Covering.* Competitiveness of C_q on supp q against B₊ gives i ∈ supp q with C_q ⪯_i B₊.
     - If i can be taken ≠ 1, then q ∈ F_i.
     - Otherwise 1 ∈ supp q and q ∈ O ⊆ F₁.
   - So every q lies in ⋃_{i ∈ supp q} F_i. The KKM lemma gives q* ∈ ⋂_i F_i. (This is Theorem kkm's argument with
     F₁ replaced by cl O.)
2. **Worlds j ≠ 1.** C_{q*} ⪯_j B₊ is relevant, so (RL-2) gives ψ_j(C_{q*}) ≤ ψ_j(B₊) ≤ ψ_j(B) + η.
3. **World 1.**
   - Take q_m ∈ O with q_m → q* and constant support S ∋ 1.
   - For j ∈ S ∖ {1}, C_{q_m} ⋠_j B₊. The contrapositive of (RL-1) gives ψ_j(C_{q_m}) ≥ ψ_j(B₊) > ψ_j(B₋).
   - Hence L_j ≥ ψ_j(B₊) > ψ_j(B₋), so (C_{q*}, B₋) is a limit pair.
   - φ ∈ 𝒩(𝔉𝔏) gives φ(E₁C_{q*}) ≤ φ(E₁B₋) ≤ φ(E₁B) + ρ₁μ(W) + π(W) ≤ φ(E₁B) + η + 2^{−m}.
   - (If S = {1}, then q_m = e₁ = q* and C_{q*} = P₁, with φ(E₁P₁) = 0.)
4. **Conclusion.**
   - t·ν(C_{q*}) ≤ t·ν(B) + O(η + 2^{−m}). Since C_{q*} is coherent, inf_coh t·ν ≤ inf_reg t·ν, so Gap_t(ν) ≤ 0.
   - Gap_t(ν) ≥ 0 always.
   - Lemma L4.0 (Gap_t(ν) ≥ d_t(c^ν) for every ν ∈ ba₊(M)^n; its proof is written for three worlds and uses nothing
     else) gives d_t(c^ν) = 0. ∎

*Reading.*
- Theorem kkm produces a dominator C_{q*} with C_{q*} ⪯₁ B. In L4.1 that comparison had to be endorsed, which is
  where (NC) entered.
- Here the world-1 KKM set is cl O instead of the section {C_q ⪯₁ B}. On O, competitiveness fails at every partner
  in the support. (RL-1) turns that failure into a ψ-strict improvement, so the world-1 comparison is **forced**.
  At the limit point, closed sections keep it accepted.
- Lemma M2.2 shows that these limit comparisons are still divisible, so K2.1 controls them.
- No rigid comparison is ever needed.

NUMERICS (`m2py/m2_checks.py` (B); an additive Brier system on M_U(T1), ε = 0.3, s = 0.9, 4·10⁴ gambles, grid 1/60,
40 random t with 1%-perturbed Bayes B). The grid version uses Sperner labels in place of the KKM sets.
- 0 covering or Sperner failures.
- Forced endorsement on O: max (ψ₁(C_q) − ψ₁(B₋)) = −3.2·10⁻².
- Best vertex of a fully labelled triangle: t·ψ(C) − t·ψ(B) ≤ 5.8·10⁻³, against a scale of 0.45 (grid
  discretisation).

---

## 4. Admissibility of T1 by separation

**Proposition M2.5 (PROVED).** Assume (H_U), let worlds 2 and 3 satisfy (RL) with ρ₂, ρ₃ > 0, let φ ∈ 𝒩(𝔉𝔏), and let
ρ₁ be its countably additive density. Then there is p* ∈ Δ with p*·c ≥ 0 a.e. on D_{T1} ∩ M and ≤ 0 a.e. on
M ∖ D_{T1}, i.e. T1 = B_{p*} ∪ S with S ⊆ Z_{p*}. Moreover p* ∈ Δ°, or p* = e₁ and ρ₁ = 0 a.e. on E₁(T1) ∩ M.

*Proof.*
1. **Localizing π.** Let D_m be as in M2.4. For a measurable W ⊆ M ∖ D_m, put Y_W := T1 △ W (regular) and
   δ_W := 1_{E₁Y_W} − 1_{E₁T1}.
   - If ψ_j(Y_W) < ψ_j(T1) for j = 2, 3, then (T1, Y_W) is forced (S = Ω), so φ(δ_W) ≥ 0.
   - δ_W = 0 on D_{m′} for every m′ ≥ m, so |π(δ_W)| ≤ 2^{−m′}. Hence ∫ρ₁δ_W dμ ≥ 0, exactly as in L4.1 step 3.
2. **Separation.**
   - Let χ := +1 on D_{T1} and −1 off it. Then v(W) := (∫ρ₁δ_W, ψ₂(Y_W) − ψ₂(T1), ψ₃(Y_W) − ψ₃(T1)) = ∫_W χ c dμ,
     with c = (ρ_iσ_i)_i.
   - Its range over W ⊆ M ∖ D_m is convex (Lyapunov) and contains 0.
   - By step 1 it misses the open negative orthant. Separation gives w^m ∈ Δ with w^m·v(W) ≥ 0 for all such W.
   - Hence χ w^m·c ≥ 0 a.e. on M ∖ D_m.
3. **Limit.** Let p* be a limit point of (w^m). Since D_m decreases to a null set, χ p*·c ≥ 0 a.e. on M.
4. **Interior.** This is H1.1 step 4, which uses only ρ₂, ρ₃ > 0.
   - If p*₃ = 0 and p*₂ > 0, then on (−,−,+) ∩ D_{T1} (non-null), p*·c = −p*₁ρ₁ − p*₂ρ₂ < 0. Contradiction.
   - Symmetrically, using (−,+,−) ∩ D_{T1}: p*₂ = 0 and p*₃ > 0 is excluded.
   - On (+,−,−) ∩ D_{T1}, p*₁ = 0 gives −p*₂ρ₂ − p*₃ρ₃ < 0. Contradiction.
   - So p* ∈ Δ° or p* = e₁. At e₁ the condition reads χσ₁ρ₁ ≥ 0, i.e. ρ₁ = 0 a.e. on E₁(T1) ∩ M. ∎

H1.1 is not needed: only (2,3)-strict improvements of T1 are used, and separation against the open orthant handles
them.

NUMERICS (`m2py/m2_checks.py` (A)). The LP max{s : χ w·c ≥ s|c|₁ on samples, w ∈ Δ} recovers the separating weight.
- Facet-switching field (T1 = B_u):
  - w* = u to 10⁻⁵, margin ≈ +10⁻⁵ (ε = 0.3, s = 0.9);
  - the same at ε = 0.2, s = 0.6.
- Brier field: margin −0.13 and −0.09 (T1 is not Brier-Bayes).

---

## 5. The main theorem and what it closes

**Theorem M2.6 (PROVED).** This is the statement in §0.

*Proof.*
- Take φ = φ* from Cor. M2.3, and ρ₁ its density.
- Thm M2.4 gives (γ₀) for c. Since c ≠ 0 a.e. on M (ρ₂ > 0), L4.1.2's directional-limit argument, which uses only
  (γ₀), makes every B_q, q ∈ Δ°, coherent.
- Prop. M2.5 gives T1 = B_{p*} ∪ S, with p* ∈ Δ° or the vertex case.
- These are exactly the hypotheses (B1) of L4 §4 with Λ₁ := Λ♮. L4 derives K3.7(β), (β′) and K3_referee (Q1) from
  them using only (γ) and ρ₂, ρ₃ > 0.
- If Λ♮ is null, c is strictly signed and p* ∈ Δ°, so M0closed(a) gives a contradiction.
- Otherwise L4.9 (for p* ∈ Δ°) and §6 of L4 (for p* = e₁) give (I₂)/(I₃) or (V). ∎

**What this closes.**
- L4 §4 covered "worlds 2, 3 add up and world 1 satisfies (NC)". M2.6 covers "worlds 2, 3 satisfy (RL) and world 1
  is arbitrary".
- In particular, the case the brief singled out (a strongly (M1) world 1, failing (NC)) is no longer outside the
  fixed-point argument when its partners are (RL). It meets the same fate as every other third world: blindness of
  the forced-limit endorsers on a set Λ♮ in configuration (I) or (V).
- Even for (NC) worlds, M2.6 is sharper: Λ♮ ⊆ Λ₁.
- If L1's Theorem L1 holds (unrefereed; Q_A "no" for weak fields with p* ∈ Δ°), only the vertex configuration (V)
  survives in this class.

**The branch "construct a world violating (NC), then aim it at T1"** was not carried out. M2.6 shows that this
branch would not by itself defeat the fixed point:
- Next to two (RL) partners, any third world, (NC) or not, leaves the forced shadow φ* undefeated (Gap ≡ 0).
- φ* is admissible for T1.
- φ* is degenerate only through Λ♮.
- So a world failing (NC) helps a T1 cover only if at least one of its partners fails (RL), or through Λ♮ exactly as
  in L4.9.

---

## 6. What remains of (NC), and the single obstruction

**Proposition M2.7 (PROVED, by inspection of L4.1's proof).** In Theorem L4.1, the hypothesis (NC) at world k can be
replaced by (NC_{𝔇_k ∪ 𝔗_k}), where:
- 𝔇_k := {1_{E_kX} − 1_{E_kC} : C selected, X regular, C ⪯_i X at every i} (the dominance pairs of Theorem kkm);
- 𝔗_k := {1_{E_kY} − 1_{E_kT1} : T1 ⪯_k Y, Y regular}.

L4.1 step 1 endorses only kkm dominance pairs. Step 3 endorses only T1's out-comparisons. Steps 2 and 4 use no
endorsement. Separately:
- 𝔗_k alone always satisfies (NC⁺) (one base; N17.3 Lemma 3.1);
- 𝔉𝔏 always satisfies (NC⁺) next to (RL) partners (M2.3).

Only the union with 𝔇_k is in question.

**The single obstruction.** Theorem M2.4 needs (RL-1) at every partner in exactly one place, step 3: from
C_{q_m} ⋠_j B₊ it must conclude ψ_j(C_{q_m}) > ψ_j(B₋).
- If partner j only adds up (RL-2 without RL-1), the failure of competitiveness at j carries no ψ_j-information.
- The comparison C_{q_m} ⪯₁ B₊ that competitiveness hands to world 1 is then an arbitrary relevant comparison,
  possibly rigid. K2.1 does not reach it.
- Equivalently, the residual of L4 is now this: a world failing (NC_{𝔇 ∪ 𝔗}) one of whose partners is not (RL), for
  instance an incomplete partner (a unanimity of several densities).
- Nothing here shows that such worlds exist, or that they do not.

**Why no proof of (NC) itself was found (a reading, CHECKED).**
- Strict (G), (IB) and sum-closure alone do not exclude uniformly negative certificates. N17.7's fine world has
  Σg_i = −1.
- Coherence of the bases does not exclude them either. The world-1 error sets of P₂, P₃ ∈ C_L already cover M twice
  on Q₁ and once elsewhere.
- So a proof must use (S) or (C) on the rigid comparisons themselves. K2.1–K2.2 and M2.2 reach only divisible ones.

---

## 7. Dependencies and files

**Used.**
- Theorem K2.1 and the vector form (1.1) of K2 (refereed CORRECT).
- K3.1(a)–(c), with fact (F2) (refereed CORRECT).
- Lemma B1.0.
- Lemma IC (R11, refereed R13).
- Theorem kkm's KKM lemma.
- Lemma L4.0 and L4.1.2's directional-limit argument (L4; under referee).
- H1.1 step 4 (positivity part only).
- M0closed(a).
- L4.9 and L4 §6, for the consequence only (unrefereed).
- Lyapunov's convexity theorem; separation of convex sets in ℝ³.

**Not used:** (NC) at world 1, any localized endorser of world 1, K3.5's patch, H1.2, N13 Prop. B, (C) in §§1–3.

**Not yet refereed.** Points a referee should check, in order of risk:
1. Thm M2.4 step 3. The constant-support subsequence, and the limit pair's margin L_j ≥ ψ_j(B₊) > ψ_j(B₋).
2. Lemma M2.2 step 4 (limit pairs). The sub-move pair is again a limit pair along the same sequence; this uses
   Lemma M2.1.
3. Prop. M2.5 step 1. The π-part vanishes because δ_W = 0 on every D_{m′}, m′ ≥ m.
4. That L4's (B1) consequences (K3.7(β), (β′), (Q1)) need nothing beyond (γ₀) and ρ₂, ρ₃ > 0. This is quoted from L4.

`m2py/` (run with `python3 -I m2_checks.py` from inside it; output in `m2_checks.out`):
- (A) the separation LP of Prop. M2.5 on the facet-switching and Brier fields;
- (B) the forced KKM of Thm M2.4 on an additive Brier system (grid/Sperner version).
