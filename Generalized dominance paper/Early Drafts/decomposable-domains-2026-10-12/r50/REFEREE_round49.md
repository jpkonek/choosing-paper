# Referee report, round 49: PP37, PP38, PP40, PP41

23 October 2026. Independent referee. I read BRIEF50_kernel_revision, AUDIT_round50, BRIEF49, AUDIT_completion (rules I–IV, F1/F2), LEAD_selection_count (Lemmas A, B, E), REFEREE_round48, and the four notes in full. I checked each listed claim line by line and edited no note. My scripts are in `r9/PP44_py/`. The authors' scripts were re-run from copies in `PP44_py/rerun/` (§5).

**Labels.** PROVED: complete argument, here or in the note, checked by me. CHECKED: exact finite computation. NUMERICS: sampling or LP on samples. CONJECTURE: unproved. "Unclear" means the argument has a gap I could neither close nor refute.

**Overall.** Most of the axiom-level results are correct. I found four substantive problems; the first and fourth are new.

1. **PP37 Thm 5.6, the surviving pattern: wrong.** Under the note's own hypotheses for Prop 5.2, the edge gate must be non-strict at both edge worlds. Then T is tied at all three worlds with the incoherent model T[O ↦ S] through the edge gate at w₀. That is F2. So within PP37's stated class, no uniform zero rule survives (§1.6; PROVED, CHECKED).
2. **PP38 Prop 5.2 is false.** PP40's counterexample is correct, and PP40's shadow repair (B3) is correct for triangles with exactly one bounded edge (§2.4).
3. **PP41 hypothesis (NA) is impossible as written (audit is right).** A local version repairs Prop 3.4′, and in fact follows from facts already proved about the kernel. But the proof also has a hidden single-realiser step, which must be stated as a hypothesis. Prop 2.8 inherits that hypothesis (§4.3).
4. **PP41 Prop 4.1(b) is false (audit is right).** I give an explicit all-world tie between T and an incoherent splice, through T's gate in one direction and a post-jump model's gate in the other. All of (I_Γ) holds (§4.4; PROVED, CHECKED). PP41's "null family" justification of a weaker (H_inst) is unsupported. A different argument (§4.5) shows conic splice records are never installed. A short case check handles step 1's non-conic record. Together they replace (H_inst) by a weaker hypothesis under the kernel.

---

## 0. Verdicts at a glance

| Note | Claim | Verdict |
|---|---|---|
| PP37 | Lemma 1.2 (levels 1 and 3/2) | correct (re-run identical) |
| PP37 | Thm 3.1 (universal competitiveness in Γ) | correct |
| PP37 | Thm 3.2 (localisation), Lemma 3.3 | correct |
| PP37 | Thm 4.1 (exact PP30 condition) | correct |
| PP37 | Prop 4.3 (explicit edge gate and family) | correct (CHECKED, re-run identical) |
| PP37 | Thm 5.1 (strict path gates impossible) | **correct with repair**: the world-3 test record of (T2) can fail to exist; a different test record works |
| PP37 | Prop 5.2 | correct under (H_path), (H_E). (H_E) is a restriction of design Γ, not a property of it. |
| PP37 | Prop 5.4 (junction inequality) | correct |
| PP37 | Prop 5.5 | correct. **(H5) is superfluous**: T alone realises a side of both directions. |
| PP37 | Thm 5.6, exclusions (S = ∅, 3 ∈ S, S = {1,2}) | correct under (H_path), (H4) |
| PP37 | Thm 5.6, survivor S = {w₀} "No F2" | **wrong** (counterexample, §1.6) |
| PP37 | Prop 6.1 (realised retreat kill), Cor 6.2 | correct |
| PP38 | Thm 3.1 (potential kernels) | correct |
| PP38 | Lemma 4.2 (coherence lemma) | correct (proof checked step by step; CHECKED, re-run identical) |
| PP38 | Cor 4.3 (registrable models: T, B_ij(t), V_k) | correct |
| PP38 | Thm 2.2 (no subordinate cone) | correct |
| PP38 | Prop 5.2 (interface) | **wrong** (PP40 Counterexample 1.2 confirmed) |
| PP38 | Thm 6.3 | (a) correct; (b) correct given (H_k), which is NUMERICS (re-run, §5) |
| PP40 | Prop 1.4 (shadow repair (B3)) | correct, for triangles with exactly one bounded edge |
| PP40 | Lemma 1.3 (shadow lemma) | correct. The range "(−∞, δ)" should be "[δ − M_v, δ)" (envelope bound). |
| PP40 | Lemma 2.1 (inheritance law), Cor 2.1a | correct (with C_{p₀} = T, as the note says) |
| PP40 | Lemma 2.5a, Prop 2.5 (k-inversion) | correct |
| PP40 | Prop 2.6 (edge-world ℓ-negative record; fourth residue family R4) | **correct with repair**: the signs must be strict *at the limit* t*, not along the sequence; boundary values of t* are not covered |
| PP40 | Prop 3.1 (splice Prop K), Cor 3.2 (zonoid criterion) | correct |
| PP40 | Thm 3.3 (a)–(d) (edge-rival dominator exclusions) | correct. (c)'s statement about near-vertex escapes is heuristic. |
| PP41 | Lemma 1.2 | correct (CHECKED, re-run) |
| PP41 | Thm 2.4 (no single-valuation jump), with Prop 2.3 | correct **under exactly** the kernel, (H_P), (H_inst), (V1)–(V3) |
| PP41 | Lemma 2.5 | correct |
| PP41 | Prop 2.8 | **correct with repair**: needs repaired Prop 3.4′ *and* a single-realiser hypothesis (R) for the post-jump models; unclear without (R) |
| PP41 | Prop 3.4′ | **correct with repair**: (NA) false; local replacement proved; hidden hypothesis (R) |
| PP41 | Prop 4.1 (a), (c) | correct |
| PP41 | Prop 4.1 (b) | **wrong** (counterexample, §4.4) |
| PP41 | Remark 2.6, "null family" | **unclear / unsupported**; keep (H_inst). A partial weakening is proved in §4.5. |

---

## 1. PP37 (support-gated potentials)

### 1.1 Lemma 1.2, Thm 3.1, Thm 3.2, Lemma 3.3: correct

- **Lemma 1.2.** The orthant masses are 1/4 each. T and μ are permutation-invariant, which gives L⁰_w(T) = 1. For the edge models, I checked the pairing φ(g) = (g₁, g₂, −g₃). An edge model's answer on W₁₂ depends on θ alone, and its 1-correct category is {θ < m₁/m₂} on both M₁ and M₂. So the world-3 ranks pair to 2, W₁₂ contributes 1/2, and M₃ contributes 1.
- **Thm 3.1.** The full-support case uses Σ_w ρ_w δ_w ≥ 0 pointwise for records out of a coherent model. This holds because on U any change worsens, and contradiction costs 12 > 4. The edge case uses σ₁ = σ₂ on W₁₂ and A on M₃. Strict (G) needs strictly positive densities; it has them.
- **Lemma 3.3 / Thm 3.2.** Values are finite for unbounded records (bounded densities, finite μ), so they telescope around triangles. The symmetric zero rule accepts the reverse because the realiser of one side of the forward edge is the realiser of the other side of the reverse. At world 3 only the L-gate acts. Correct.

### 1.2 Thm 4.1 and Cor 4.2: correct

I re-derived E_w(y_{G,E}) = [σ_w(G^c) − σ_w(G^r)] − σ_w(E), counting E ∩ G^r as wrong → correct (−2). In (i) ⇒ (ii) the inequality uses a ≥ 0, which holds since σ/ρ > 0. A remark for Cor 4.2: in Γ, E is balanced on W₁₂, so every edge member is E-Bayes at (1/2, 1/2). The hypothesis is therefore automatic, with κ = 1.

### 1.3 Prop 4.3: correct

The ratio table σ_w/ρ_w ∈ {1/2, 1} is right. The sandwich fails exactly when τ₀ > α and τ₁ < β. The parametrised family is continuous at τ = α, β, β′, and each K(q) ∋ q. `edgegate37` re-run: 190/190, identical output.

### 1.4 Thm 5.1: correct with repair

Steps 1–3 are correct: level-n induction, π–λ, and Lemma A/E at the end. Step 2 uses the fact that a continuous function on a connected set with a local minimum at every point is constant. Proof: {f ≥ c} is open (local minima) and closed (continuity) for every c.

**Gap in (T2) at w = 3.** P = M₃ ∩ {C_{q₀} ≠ A} may be the set where C_{q₀} says B, which is 3-correct. This happens for every precise path model. Then no piece of P admits a 3-gain.

**Repair.** At w = 3 no E-gate acts. So run the construction with P′ := {C_{q₀} not 3-correct} ∩ (mixed problems). Put the gain inside B_m and a loss to contradiction outside it. Only the L-gate and guidance can accept the record, and both refuse it. At w ∈ {1, 2} the original P works: B and S on M₃ are 1- and 2-improvable, and the loss piece never moves to A, so no edge member realises the new side.

### 1.5 Props 5.2, 5.4, 5.5

- **Prop 5.2: correct under (H_path) and (H_E).** I checked the constancy argument. The strict world gives local minima, and (T1) gives lower semicontinuity at the other world. With λ₁b₁ + λ₂b₂ constant, both are continuous, hence constant on the component U adjacent to e₁. Then X = V₁[F ↦ 2-correct] kills closedness at e₁.
  - **Hidden assumption.** (H_E) is *not* a property of Γ as defined. Γ's clause 3 lets the L-gate of any full-support member realising the old side accept an edge member's record. (H_E) is a design restriction, and it should be stated in Γ's definition when Prop 5.2 is used.
- **Prop 5.4: correct.**
- **Prop 5.5: correct, and (H5) is superfluous (PROVED).** Γ's zero clause accepts when the realiser realises the old *or the new* side. Take X := T[A′ ↦ A, B′ ↦ B] with A′, B′ ⊆ Sil(T) ∩ M_k of equal mass. Per unit mass, S → A and S → B have opposite rank changes, so every Λ⁰_w is 0 (CHECKED, `f2_egate.out` (c), k = 1, 2, 3). T realises the old side of rec(T, X) and the new side of rec(X, T). With S = ∅, T ≈ X at every world, so rule IV gives F2. No member R is needed.

### 1.6 Thm 5.6: the exclusions are correct; the survivor fails (counterexample)

**Exclusions.** S = ∅ is excluded by Prop 5.5 (with or without (H5)). 3 ∈ S is excluded by Prop 5.3 against Prop 5.4 (a₃ ≡ 1 < 3/2). S = {1, 2} is excluded because then a₃ is constant. All correct under (H_path) and (H4).

**The survivor's claim "No F2: zero records are refused at w₀, so no all-world tie passes through an L-gate" is wrong.** It overlooks the E-gate, which also acts at w₀ ∈ {1, 2}. Under the hypotheses the note uses for Props 5.2–5.5 (status table: (H_path), (H4), (H5), (H_E)), Prop 5.2 forces the E-gate to be **non-strict at both edge worlds**, and in particular at w₀.

**Counterexample (PROVED; CHECKED in `f2_egate.out` (a), (b)).** Take w₀ = 1 (w₀ = 2 is symmetric, using M₂).
- **The pieces.** Let D be any non-vertex edge member, for instance Prop 4.3's segment with θ-thresholds (α, 1). Take bounded non-null O_A ⊆ M₁ ∩ {T = A} ∩ {D = A} and O_B ⊆ M₁ ∩ {T = B} ∩ {D = B}, with μ(O_A) = μ(O_B) and σ(O_A) = σ(O_B). Two linear constraints can be met by atomlessness. Witnesses with strict margins: `f2_egate.out` (b).
- **The record.** Put X := T[O_A ∪ O_B ↦ S], which is incoherent (Lemma H). On M₁, A → S changes the ranks by (−1, +1, +1) and B → S by (+1, −1, −1), and ρ = (2, 1, 1) is constant there. So rec(T, X) has L-value 0 at every world and E-value 0 at worlds 1 and 2, for **any** balanced E.
- **World 1.** The L-gate is strict there and refuses. The E-gate is symmetric, and D realises the old side of rec(T, X) and the new side of rec(X, T). So T ⪯₁ X and X ⪯₁ T.
- **Worlds 2 and 3.** These are not in S, so the L-gate is symmetric, and T realises a side in each direction.
- **Conclusion.** T ≈ X at all three worlds, and rule IV registers the incoherent X: F2.

**Consequence.** Within PP37's class (one balanced L per full-support member, one balanced E per edge member, a uniform zero rule per world), and with (H_path), (H4) and (H_E), *no* zero-rule pattern survives. The only escapes are:
- drop (H_E), so that Prop 5.2 no longer forces E to be symmetric, and make E strict at w₀ (Thm 3.1 allows strict at one edge world). Whether that avoids F2 is OPEN: I found records with Λ⁰₁ > 0 > E₁, so cross-gate L/E ties at w₀ are not excluded automatically; or
- restrict the E-gate's zero clause, for example to records whose sides are realised by no full-support member.

The §0 and §9 tables should be corrected.

### 1.7 Prop 6.1, Cor 6.2: correct

W is well defined. R ⪯_j W is a nontrivial j-worsening because P ∖ Q is non-null. rec(W, C) is realised by C₂: C₂ = V_j on Q and C₂ = S on G′. Its value is ≥ φ_j(Q) − φ_j(G′), since S → anything gains at most 1. W ⪯_j R is a pure j-improvement, so (TC) fails. The proof needs C ⪯_j R only at world j, not domination. Cor 6.2 follows, since {T = V_j} ∩ G′ = ∅.

### 1.8 Hypotheses

- **(H_path)** is the natural domain choice.
- **(H4)** excludes path members that are A a.e. on M₃. Under PP38's kernel every post-jump model B₁₂(t) is such a member, so PP37's §5 and PP38/PP41's jump analyses work in disjoint regimes. This should be said.
- **(H5)** is unnecessary (§1.5).
- **(H_E)** is a design restriction (§1.5), and it is what kills the survivor (§1.6).

---

## 2. PP38 (bounded kernel)

### 2.1 Thm 3.1: correct

- **(i)** Each triangle has either all edges bounded or at least two unbounded edges. At this stage the unbounded edges are guidance, so they have Φ ≥ 0 with equality only if trivial.
- **(ii)** This uses PP32 Lemma 2.3 on balls and compactness of the nested Λ_n, which gives weights in the closed face.
- **Hidden scope.** (ii) "⇒" assumes that bounded records are accepted only by the kernel and guidance. Every later design keeps this; it should be stated.

### 2.2 Lemma 4.2 (coherence lemma) and Cor 4.3: correct

I checked every step:
- F(1/L) = 1, using Ld = 1 − d.
- The slopes of F⁻¹ are 2d, 2d/L, 1/L. Its kink at 1/2 is concave and its kink at 1 is convex.
- In the case y₀ = 1, the one-sided slopes −λ_j/(2dλ_k) < −2dλ_j/λ_k follow from 4d² < 1.
- In the case y₀ = 1/2, G(s) = s/L on (0, L], so G⁻¹ is linear near 1/2, and the convex kink of G at L has slopes 1/L and 1/(2dL).
- The midpoint argument is correct, with ball radii r/4 and r/2.
- Only λ_i > λ_j and λ_k > 0 are used; "λ_j minimal" is not needed.

**Cor 4.3.** Uniqueness of the Bayes model at boundary weights holds:
- on M₃ at λ₃ = 0, A costs 0;
- on W₁₂ the ties lie on rays.

`coherence_exact` re-run: identical, ALL PASS.

### 2.3 Thm 2.2 (no subordinate cone): correct

- Step 1 needs T's competitiveness against T[G ↦ V_j] and w ≠ j.
- Step 2 is PP30 Thm 3.1(b): T's departure composed with V_j → w-correct is a pure w-improvement.
- In step 4, H ∩ G = ∅ because G ⊆ R, and the record is bounded.
- In step 5, the e_j-triangles shrinking to e_j force K = {e_j}.

The final clause is right: lines with small e_j-triangles miss M, so they lie in Ans(T) ⊆ R^c when R ⊆ Sil(T).

### 2.4 Prop 5.2: wrong; PP40's repair is correct

**PP40 Counterexample 1.2 is valid (PROVED).**
- Let r = rec(C, Z) be installed at v with Φ_v(r) = −δ, and put Q := Z[F ↦ contradiction] with ∫_F(increase) < δ.
- Then g = rec(Q, C) is unbounded with Φ_v(g) = δ − ∫_F(increase) > 0. PP38 Thm 5.1 allows any such record in 𝒢_v.
- The triangle C ⪯ Z ⪯ Q ⪯ C is accepted. Its bounded edge Z → Q is strict guidance, so the reverse Q ⪯_v Z is refused.
- (B1) and (B2) hold, so Prop 5.2 fails. PP38's own Thm 6.3 "Consequence" is an instance.

**PP40 Prop 1.4 (shadow condition (B3)) is correct (PROVED).** In a triangle with exactly one bounded edge, the two unbounded edges have mutually inverse far parts. Case by case:

| Pair of unbounded edges | Outcome |
|---|---|
| (guidance, guidance) | trivial far part, impossible |
| (guidance, 𝒢), (𝒢, 𝒢) | Φ-sum > 0, impossible |
| (guidance, installed) | (B1), or a positive Φ-sum |
| (installed, installed) | (B2) |
| (𝒢, installed) | (B3) |

Since (B3) as worded covers every ℓ-positive unbounded record, it also covers guidance records. That is consistent: by (B1), the inverse of an installed far part is never a weak worsening.

**Scope.** (B3) is sufficient. Lemma 1.3 shows only its core is necessary: the inverse-far-part records rec(Q, C) with Q a bounded perturbation of Z and value in (0, δ).

**Small correction to Lemma 1.3.** Values of bounded perturbations are bounded by the envelope M_v = ∫(α+β+γ)_v dμ ≈ 2.7 at ε = 3/10 (`na_local.out` (3)). So the forbidden values fill [δ − M_v, δ), not (−∞, δ). Triangles with three unbounded edges remain open, as both notes say.

### 2.5 Thm 6.3: correct

- **(a)** Inheritance and strict (G) remove i and j eventually, and competitiveness at an interior index leaves k.
- **(b)** Φ_k(rec(B_n, X)) = L_k(T) + β_k(E) − L_k(B_n) < 0, given (H_k).
- **(H_k)** is NUMERICS. `jump_gap_mc` re-run: §5.

---

## 3. PP40 (adversary)

### 3.1 Inheritance law (Lemma 2.1): correct

A_w(X) is closed relative to I, and p₀ ∉ A_w(X) whenever T ⋠_w X. Nonemptiness comes from competitiveness at the interior p_n. The note correctly replaces T by C_{p₀} when installed records create a tie. That replacement matters because (TC) does not give transitivity, so A(C_{p₀}, ·) and A(T, ·) can differ.

### 3.2 k-inversion (Prop 2.5): correct

- **Splice identity.** rec(D, C[S ↦ D]) = ({D ≠ C} ∖ S, D → C) = rec(D[S ↦ C], C). With D = B_n, C = T, S = E, the two splices are X_E and Y_E, because B_n = A on E ⊆ M_k.
- **(a)** The triangle T ⪯ Y_{E′} ⪯ Y_{E₀} ⪯ T has middle edge A ↦ S removed on E′ ∖ E₀, which is k-guidance. Its reverse is a pure k-improvement, so T ⋠_k Y_{E′}.
- **(b) and (c)** follow as stated.
- **Field comparison.** Φ_k(Y_{E′} → T) = −Δ_{n,k} + β_k(E′), so the field ranks the pair the other way, by about 0.46 (`jump_signs_mc` re-run, §5).

### 3.3 Edge-world ℓ-negative record at every jump (Prop 2.6, R4): correct with repair

The argument needs a **fixed** F (case (a)) or E′ (case (b)) chosen *before* n ≥ N(X). So the signs must be strict at the limit t* = lim t_n, by continuity of t ↦ Δ_w(t), not merely for each n.

- **Repaired statement (PROVED).** Suppose t_n → t* ∈ [0, ∞], and either Δ_w(t*) > 0 for some w ∈ {i, j}, or Δ_i(t*) < 0 and Δ_j(t*) < 0. Then case (a) or case (b), respectively, holds for all large n.
- **Vertex limits.** At t* ∈ {0, ∞} one edge coordinate is positive (Δ_j → L_j(V_i) − L_j(T) > 0), so (a) applies.
- **Not covered.** t* on the zero set of Δ_i or Δ_j with the other ≤ 0. This includes the two endpoints of I₂ (NUMERICS: ≈ 0.65 and 1.55 at ε = 0.3). There, Δ_{n,w} → 0 and neither F nor E′ can be fixed.
- **The note's label** "PROVED given strict signs of Δ_{n,i}, Δ_{n,j}" should read "given strict signs at t*".
- **R4 (T's own ℓ-negative defence)** is correct for t* in the interior of I₂, including t* = 1. As a limit point, t* = 1 is not excluded by Prop 2.4(i), which excludes only B_n = B_ij(1).

### 3.4 Splice form of Prop K (Prop 3.1) and Cor 3.2: correct

**Prop 3.1.** By the splice identity, D ⪯_i C[S ↦ D] is the verdict D[S ↦ C] ⪯_i C. The triangle D[S ↦ C] → C → Z → D[S ↦ C] then lacks its reverse. Only (IB) and (TC) are used; D's competitiveness is not used in the proof.

**Cor 3.2.**
- Z vs D[S ↦ C] is bounded with value d(S) − z, and the kernel makes Z ≺_v D[S ↦ C] iff d_v(S) > z_v.
- Worlds in G(C, D) are removed by strict (G), provided {C ≠ D} ∖ S is non-null. That holds for bounded S and coherent C ≠ D.
- The sufficient condition is right: μ·d(S) ≤ 0 ≤ μ·z.
- The single-world formula should exclude supp z from the integral; this is minor.

### 3.5 Edge-rival dominator exclusions (Thm 3.3): correct

- **(a)** I checked the region P₁: N = S for 1/L < s₂ ≤ γL, and T = A iff s₂/L + G(s₃) > 1, using G(s) = s/L on (0, L]. Each S → A change costs +|g₁| at world 1 and gains G(s₂)|g₁| ≤ γ|g₁| at world 2. So d ≥ m(1 − γ)(1, 1), and small z₁, z₂ are killed. The killed rival is T[P₁ ∪ P₂ ↦ N], as stated.
- **(b)** sup_S d₂(S) = L₂(V₁) − L₂(N), because V₁ → N agrees on M₃ and U and is a 2-worsening on W₁₂. Correct.
- **(c)** B₁₃(s) says B on a non-null part of M₃, since its m₃ > 0. Every change from A there costs at worlds 1 and 2. Correct. The sentence about near-vertex models "escaping only by" ℓ-negative defences of N is heuristic, not proved.
- **(d)** Correct: d₂ ≥ 0 pointwise, by opposite rank changes on W₁₂.
- **Window.** `r3_window_mc` re-run: §5.

---

## 4. PP41 (kernel completion)

### 4.1 Lemma 1.2 and Lemma 2.2: correct

Lemma 1.2(b) was checked by hand:
- on M₁, T says B only where F(s₂) < 1, i.e. s₂ < 1/L;
- T says A wherever s₂ > L.

In Lemma 1.2(c), the region {s₁ + s₃ > L} equals T's A-region on M₂, because G(s) = s/L on (0, L] and G > 1 beyond L.

Lemma 2.2 is correct. It uses (V3) on rec(C_{q_m}, X), which is unbounded unless C_{q_m} = C_q.

### 4.2 Prop 2.3, Thm 2.4, Lemma 2.5: correct under exactly their hypotheses

**Prop 2.3.**
- **Step 1** uses (H_inst) essentially. rec(B_n, X_E) is a sub-record of rec(B_n, T), so it is not installed, and (V3) gives V₃ ≥ 0.
- **Step 7.** The separation is between a compact convex range containing 0 and the open positive quadrant, which gives μ ∈ Δ₁₂. μ = e₁ would contradict Lemma 1.2(c).

**Thm 2.4.**
- λ·a ≡ 0 and μ·a ≡ 0 follow from a(D ∖ S) = −a(S).
- If λ and μ are not parallel, the density lies on a line, but it must carry the sign patterns (−,−,+) on Sil(T) ∩ M₃ and (+,−,−) or (−,+,−) on R_{t*}. No line does.
- If they are parallel, λ₃ = 0 and λ·density < 0 on Sil(T) ∩ M₃.

**Exact hypothesis list** (the audit's correction is right). The theorem needs all of:
- PP38's kernel;
- a complete edge with every edge index in I;
- (H_P);
- (H_inst);
- (V1)–(V3), including that every positive-value unbounded record realised by a registered model is accepted;
- angular densities, for continuity in t and for the measure a.

It does not cover a post-jump family other than the edge's own (Remark 2.6), or kernels other than ℓ^T.

**Lemma 2.5** is a two-line linear inequality and is correct.

### 4.3 Audit objection 1: (NA), Prop 3.4′ and Prop 2.8

**(NA) is impossible as written (PROVED).** Every record r satisfies |Φ_w(r)| ≤ E_w := ∫(α+β+γ)_w dμ (E_w ≈ 2.7 at ε = 0.3; `na_local.out` (3)). Π^C-values of tail perturbations are bounded by the integral of the angular density. Bounded sets cannot fill open half-spaces.

**A local version repairs the half-space step, and it needs no new assumption on Φ.** Write K_Φ(C) for the closed convex cone generated by the essential range of the normalised pointwise change vectors d(g, a) = ℓ(g, a) − ℓ(g, C(g)), a ≠ C(g). Define K_Π(C) likewise from Π^C's angular density. The dual cone K_Φ(C)* is the set of signed weights y at which C is pointwise y-Bayes.

**Lemma R1 (corner vectors; PROVED).** For every model C, K_Φ(C)* ⊆ R³_{≥0}.

*Proof.* On M_w near its corner (s_i, s_j → 0), changing to contradiction gives d/|g_w| with w-entry ≥ 1 and other entries ≤ G(s)+F(s)+s → 0. So y·d ≥ 0 forces y_w ≥ 0. ∎

So if C is Φ-Bayes at exactly one weight λ ∈ Δ, then K_Φ(C)* = R₊λ and K_Φ(C) = {x : λ·x ≥ 0}. This holds for every model of Cor 4.3:
- T at u: by Lemma 4.2, and uniqueness at boundary weights;
- B_ij(t) at its edge weight: the corner of M_k forces y_k = 0, and the thresholds fix the ratio;
- V_k at e_k.

**Lemma R2 (local attainability; PROVED).** Let K be K_Φ(C) or K_Π(C), and let p ∈ ri K. Then there is s₀ > 0 such that, for every s ∈ (0, s₀], s·p is the value of a perturbation of C:
- a bounded one, for K_Φ;
- a change on a cone of directions, for K_Π, which may then be truncated outside any ball without changing its Π-value.

*Proof.*
1. **Finitely many generators.** p ∈ ri cone(F) for a finite set F of essential directions. Take a small simplex around p in ri K.
2. **Approximating pieces.** For each f ∈ F, take disjoint non-null bounded pieces A_f, with one advice change each, whose change vectors are within η of f. Let p_f be the value of the change on A_f. For small η, p = Σ c_f p_f with all c_f > 0. The p_f stay in span K, because the essential range lies in K.
3. **Scaling.** The value map on subsets of A_f is a non-atomic vector measure, so its range contains the segment [0, p_f]. Choose A′_f ⊆ A_f with value s·c_f·p_f, for s ≤ 1/max c_f. ∎

NUMERICS (`na_local.out`) for T, B₁₂(1/2) and B₁₂(2), with 18,000 sampled change vectors each:
- the sampled dual cone deviates from the Bayes ray by at most 0.0014;
- 30/30 random targets with λ·x/|x| ∈ [0.02, 0.5] lie in the sampled cone (LP certificates).

**Prop 3.4R (repair of Prop 3.4′; PROVED).** Let C be registered in Γ_K and Φ-Bayes at exactly one weight λ, as every model of Cor 4.3 is. Suppose C is **not** Π^C-Bayes at λ. Then there is an unbounded rival X with V^C_w(C → X) < 0 at every world, so C's own gate refuses X everywhere.

If moreover

**(R)** no other registered member's gate passes rec(C, X) at any world, and rec(C, X) is not a copy of an installed record,

then C is not competitive against X.

*Proof.*
1. **The cones add to R³.** λ ∉ K_Π* gives K_Φ* ∩ K_Π* = R₊λ ∩ K_Π* = {0}. So the convex cone K_Φ + K_Π has trivial dual, is dense, and equals R³.
2. **Decomposition.** By Rockafellar Cor 6.6.2, ri(K_Φ + K_Π) = int K_Φ + ri K_Π. So −(1, 1, 1) = φ + v with φ ∈ int K_Φ and v ∈ ri K_Π.
3. **The perturbations.** By Lemma R2 take, for one small s:
   - b bounded inside B_{R₀}, with Φ(b) = sφ;
   - c on a cone outside B_R (R > R₀), with Π^C(c) = sv.
4. **Values.** Then V^C(C → C·b·c) = −s(1, 1, 1) + Φ(c), and |Φ(c)| ≤ ∫_{|g|>R}(α+β+γ) → 0.
5. **Other routes.** Guidance refuses, because V^C is strictly guiding. The kernel does not apply, because the record is unbounded. Everything else is (R). ∎

This is stronger than Prop 3.4′, since it does not need "Π^C-Bayes only at λ′". But (R) is a genuine hidden assumption of PP41's step 4 ("for generic b and c no other gate realises its old side"):
- once the edge family is registered, every region on which B₁₂(t) has a given answer is shared with B₁₂(s) for s near t, apart from null rays;
- T shares {B_n = T}.

So "for generic b and c" is false whenever a continuum of members is registered. The honest reading is: **own-gate competitiveness, as used in Prop 4.1(a), forces common weights.**

**Prop 2.8: correct with repair.** Its step 1 is Prop 3.4R applied to B_n, so it holds under (R) for the post-jump models, together with the stated convergence of densities. Steps 2–4 are correct: (J_B) in the limit gives V^T(B* → T) ≤ 0 with equality at 3, and μ*_{1,2} > 0 forces V^T(B* → T) = 0, which contradicts strict u-optimality of T.

Without (R), I could not complete the argument. A version holds if every member realising the old side of the test record has a valuation within s/2 of V^{B_n} on it; this is plausible when all valuations converge together, but it is not shown. **Verdict: unclear without (R).**

### 4.4 Audit objection 2: Prop 4.1(b) is false

**Claim (b).** "No C has an all-world tie with an incoherent model through gates or the kernel; direct (C) can fail only through installed records." Its proof treats only ties whose two directions both go through C's own gate. In that case both directions need V^C_w = 0 at every w (C realises only the new side of rec(X, C)), so λ_C·V^C = 0 forces X = C. That part is right.

**Counterexample (PROVED; CHECKED in `cross_gate_tie.out`).** Take ε = 3/10 and t = 1/2. Let B := B₁₂(t) be registered at an interior index, as a post-jump model is, so its gate acts at all three worlds.

1. **Four cones of D_t = {T ≠ B}.** Witnesses with strict margins, and the rank change of T → B on each:

   | Cone | T → B | Rank change T → B |
   |---|---|---|
   | (i) Sil(T) ∩ M₃ | S → A | (−1, −1, +1) |
   | (ii) R_t ⊆ Sil(T) ∩ M₁ | S → A | (+1, −1, −1) |
   | (iii) M₂, T = A | A → B | (+2, −2, +2) |
   | (iv) Sil(T) ∩ M₁, θ < F⁻¹(t) | S → B | (−1, +1, +1) |

2. **Tail fields.** Take rank-linear angular fields with nonnegative coefficients, which are therefore weakly guiding:
   - π^T: (1, 0, 1) on (iii), (1, 1, 0) on (iv), 0 elsewhere;
   - π^B: (1, 1, 0) on (i), (0, 1, 1) on (ii), 0 elsewhere.

   T is π^T-Bayes at u, and B is π^B-Bayes at μ = (t, 1, 0)/(1 + t), against all four advice options (CHECKED). (I2) asks for C to be the a.e.-*unique* Π^C-Bayes model. To get that, add ηψ to both fields, with ψ the angular restriction of ℓ^T. T and B are the unique ψ-Bayes models at u and μ, ψ is strictly guiding, and for small η the signs in step 3 are unchanged. So (I1)–(I3) hold for V^T = Φ + KΠ^T and V^B = Φ + KΠ^B.
3. **Tail values.** With unit angular weights, Π^T(T → B) = (1, 1, 2) and Π^B(B → T) = (1, 2, 1). Both are strictly positive at every world.
4. **The tie.** Choose K > max_w E_w / 1, for example K = 2.96 (NUMERICS for E_w; the existence of K is exact). Let S := D_t ∖ (unit ball) and X := T[S ↦ B], which is incoherent (Lemma H).
   - V^T_w(T → X) = Φ_w + K·Π^T_w > 0 at every w, so T's gate gives T ⪯_w X.
   - rec(X, T) has old side B on S, which B realises, and V^B_w(X → T) = −Φ_w + K·Π^B_w > 0 at every w. So B's gate gives X ⪯_w T.
   - Hence T ≈ X at all three worlds, and rule IV registers X: **F2, with no installed record and no refusal.**

**Valid conclusion.** In Γ_K, an all-world tie of a member C with X ≠ C needs, at some world, a direction passed by a gate other than C's (or an installed copy). Direct (C) in Γ_K therefore needs a cross-gate compatibility condition. A necessary one: for members C ≠ C′ and conic S ⊆ {C ≠ C′}, the vectors V^C(C → C[S ↦ C′]) and V^{C′}(C → C[S ↦ C′]) must not lie in the open positive and open negative orthants respectively.

This is the audit's point exactly: the relation is a **union** of gates, so any refusal or protection must be checked against every gate that realises a side.

### 4.5 The "null family" claim (Remark 2.6)

**The claim is unsupported.** No measure on the family of splice sets is defined. And the claim does not address what Thm 2.4 actually needs.

**A different argument does part of the job (PROVED).** Weaken (H_inst) to:

**(H_inst′)** installed records are dominations rec(C, Z) of *incoherent* rivals Z, each a bounded perturbation of a registered model.

Then:
- **Conic records are never installed.** Suppose an installed record were a copy of (S, T → B*) or its inverse, for a cone S. Then Z = C[S ↦ B*] (C = T on S) would be conic. Being a bounded perturbation of a conic registered Y, it would equal Y a.e. (homogeneity), so Z would be coherent: a contradiction. This covers every splice record used in Prop 2.3 step 7 and Thm 2.4.
- **Step 1's record needs more.** Step 1's record rec(B_n, X_E) is not conic. A copy of it installed as rec(C, Z) forces C = B_n a.e. on D_n := {B_n ≠ T}, and Y = C[D_n ↦ T] registered.
  - If C = B_n, then Z = X_E, and B_n dominating X_E contradicts inheritance for n ≥ N(X_E).
  - If C ≠ B_n, C must be another kernel-registrable model agreeing with B_n on all of D_n. None does. With cones (iii) and (iv) of §4.4 taken at t_n (both non-null for every t, by Lemma 1.2(c)):
    - T differs on D_n by definition;
    - B₁₃(s) and V₁ say A on cone (iii), where B_n = B;
    - B₂₃(s), V₂ and V₃ say A on cone (iv), where B_n = B;
    - B₁₂(s), s ≠ t_n, differs from B_n on a threshold wedge. At fixed θ in that wedge, T says A for large s₃, so the wedge meets D_n non-nully.

    (PROVED, sketch.)

So, under the kernel and (H_P), Thm 2.4 holds with (H_inst′) in place of (H_inst). Until this is written out in the note, keep (H_inst) explicit, as the audit says.

---

## 5. Scripts re-run (`PP44_py/rerun/`, copies of the authors' scripts; outputs compared with the originals)

All 13 authors' scripts ran to completion. Every output is **byte-identical** to the authors' `.out` (all scripts are seeded).

`twofield_lp.py` first failed in my copy, because it imports `field38` by a relative path to `../PP38_py`. With a symlink it reproduced exactly; this is not a defect in the original folder.

| Script | Time | Key output re-confirmed |
|---|---|---|
| PP37 `levels37`, `edgegate37` | 98 s, 26 s | balance identity; 190/190 edge models, Thm 4.1 condition = band predicate |
| PP38 `coherence_exact` | 2 s | Lemma 4.2 witnesses at 90 weights × 4 ε; ALL PASS |
| PP38 `budget_mc`, `second_gen_mc` | 54 s, 183 s | Prop 4.4(b); Prop 6.6 gaps (NUMERICS) |
| PP38 `jump_gap_mc` | 126 s | (H_k): min_t [L₃(B) − L₃(T) − 4 s.e.] ≥ 0.443 for all four ε |
| PP40 `coherence_scan`, `pointwise_exact` | 56 s, 3 s | 177/177 weights incoherent, none at u; B₁₂(1) ≥₃ T pointwise; ALL PASS |
| PP40 `jump_signs_mc` | 109 s | h₀ = 0.101, 0.086, 0.063, 0.012; I₂ on the **t-grid** ≈ [0.65, 1.55] at ε = 0.3. The endpoints are grid-resolution only, which matters for §3.3. |
| PP40 `r3_window_mc` | 19 s | admissible at t = 0.995 and 1.002, not at 0.980 and 1.005; L₃(B) − L₃(Z′) ≈ +1.1·10⁻³ (world-3 ℓ-negative) |
| PP41 `exact41` | 5 s | Lemma 1.2 (a)–(d); ALL PASS |
| PP41 `twofield_lp` 4000 | 6 s | two-world iso infeasible at 21 values of t; world-3 alone feasible for t ≠ 1 |

**New scripts** (`PP44_py/`; run `python3 -I -B <script> > <script>.out` inside the folder):

| Script | Content | Label |
|---|---|---|
| `f2_egate.py` → `.out` | (a) the record T → T[O_A ∪ O_B ↦ S] has zero L-value at all worlds and zero E-value at worlds 1, 2 for any balanced E; (b) witness points of M₁ ∩ {T = D = A} and M₁ ∩ {T = D = B} for a Prop 4.3 edge member; (c) Prop 5.5 without (H5). ALL PASS | CHECKED |
| `cross_gate_tie.py` → `.out` | Prop 4.1(b) counterexample: cones (i)–(iv) with witnesses and rank patterns; π^T, π^B weakly guiding and Bayes at u and μ; Π^T(T → B) = (1,1,2), Π^B(B → T) = (1,2,1); MC envelope and Φ(T → B₁₂(1/2)) = (0.053, −0.183, 0.507); a valid K | CHECKED + NUMERICS |
| `na_local.py` → `.out` | envelope bound (NA impossible); sampled dual cones of T, B₁₂(1/2), B₁₂(2) equal the Bayes ray to 1.4·10⁻³; cone-membership certificates | NUMERICS |

---

## 6. What this means for round 50

1. **PP37's Γ.** It loses its last surviving zero-rule pattern under its own hypotheses (§1.6). PP37's realiser-gated design and PP41's Γ_K share one defect, a union of gates with symmetric zero clauses, and both §1.6 and §4.4 are instances of it. Any revised design must state the aggregation across gates and check ties *across* gates. This supports the audit's instruction.
2. **The kernel.** The kernel's restriction to ℓ^T-Bayes models is what makes Prop 3.4R bite: each registered model has a *unique* Φ-Bayes weight, so its own gate is forced to share that weight. Revising the bounded kernel, as the audit recommends, changes K_Φ(C) and hence this constraint.
3. **Nearby reachable results.** In place of (NA), use Lemma R2 together with uniqueness of the Φ-Bayes weight, both proved. In place of "for generic b and c", use (R), or restate Prop 3.4′ as an own-gate statement. In place of the "null family", use (H_inst′) together with the step-1 lemma of §4.5.
