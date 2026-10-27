# PP69. A continuum of sources whose class-3 repairs stay inside the family: one relation, rival-dependent repairs, closed sections up to the edge

24 October 2026. Constructor, Brief 57. One author; not refereed. §1 was posted first as a draft for PP70 and is unchanged in substance. Takes in the coordinator's relay of REFEREE_round56 (items (1)–(6); see §4).

**Labels.**
- PROVED: complete argument here, or a cited result used within its hypotheses.
- CHECKED: exact rational computation in `r9/PP69_py/geom69.py` (output `geom69.out`, ALL PASS). Every CHECKED item that is also PROVED has its own proof; the check guards against slips.
- NUMERICS: `inst69.py` (floats, empirical Gaussian sample), evidence only.
- CONJECTURE / OPEN: as stated.

No axiom is added. One hypothesis is named: **(H_σ)** μ is invariant under the swap σ(g₁, g₂, g₃) = (g₂, g₁, g₃). This holds for the standard Gaussian used throughout.

---

## 0. Verdict

1. **The full milestone is not reached.** What is reached is the brief's partial target for **class-3 fills**, plus a class of splices, with no isolated indices anywhere:
   - **Sources:** the whole curve T →R→ N →J→ L₀ →F→ D\*, one coherent model C_θ at each index p(θ) = (1−θ)u + θh₁₂, θ ∈ [0, 1]. **The edge endpoint D\* at h₁₂ is included, and its sections are checked.**
   - **One relation:** a total relation 𝒲, additive at all three worlds, with no keys and no lexicographic levels (§2).
   - **Repairs:** rival-dependent and **inside the family**. The repair of a rival X is C_θ', with θ' the least index at which Φ₁(C_θ) = Φ₁(X).
2. **Theorem 3.1 (PROVED).** 𝒲 satisfies reflexivity, strict (G), (IB) with every copy, and (TC) on every triangle, for all measurable models. Every C_θ is:
   - defended against every measurable rival at a world of supp p(θ);
   - protected, with no all-world tie partner, so rule IV and direct (C) hold;
   - with closed fixed-rival sections along the whole closed arc, endpoint included.
3. **Theorem 3.3, the repair lemma (PROVED).** Let X ∉ 𝔽 with Φ₁(X) = Φ₂(X) ≤ Φ₁(T). Then C_θ' strictly dominates X, with θ' < 1: it ties with X at worlds 1 and 2 and is strictly better at world 3.
4. **What this covers (Cor 3.4, Prop 3.5; PROVED).**
   - Every class-3 majority fill of every source, in any measurable E. The repair index θ'(s, E) > s depends on the rival, and the repair is silent on part of E, so the path obstruction is respected. The comparisons are mixed at every world, checked world by world.
   - Every splice C_a[H ↦ C_b] between two sources whose disagreement set is swap-invariant on M₁ ∪ M₂ and arbitrary on M₃. This includes those T/N splices and every B-restoration N[H ↦ T] with H ⊆ R_B. The repair lies between a and b.
   - The step is genuinely repeatable: the same rule serves every source, including every repair.
5. **Sections and accumulation (Prop 3.6, Thm 3.7; PROVED).**
   - Reservations are rival-dependent open tubes; there are no fixed balls.
   - Every entailed kill clause whose literals lie on the arc has a refused literal, which is the strong form of (H_acc).
   - The dominators of each fixed class-3 fill form a compact subset of [0, 1). So no fixed rival is served by members accumulating at the edge, and PP68 §1(b) never triggers.
6. **Where the rest fails (§5).**
   - **(a) Axiom-level, given the symmetric choice (Prop 5.2).** In any relation invariant under the swap of worlds 1 and 2, no swap-invariant model repairs a class-1 or class-2 fill of a swap-invariant interior source. Since every member is swap-invariant and 𝒲 is swap-invariant, N's class-1 and class-2 fills cannot be repaired inside the family, nor can one-sided restorations (asymmetric T/N splices).
   - **(b) Certificate-level (Prop 5.3).** In any additive certificate, repairs of thin class-1 fills of C_s converge in measure to C_s and are asymmetric weak Bayes acts. So the registered class must accumulate at every member from off the symmetric line: it must be a two-dimensional Bayes sheet, a local version of the realisation problem.
   - (a) uses only (TC), strict (G), defence and the symmetry choice. To go further, either break the 1 ↔ 2 symmetry of the verdicts on the family itself, as Prop 5.1 says is needed, or build the two-dimensional sheet.

| Item | Result | Label |
|---|---|---|
| Curve: patterns, thresholds, 3-descending | Lemma 2.1 | PROVED; CHECKED |
| Pathwise-Bayes field, explicit | Lemma 2.2 | PROVED; CHECKED |
| 𝒲: axioms; defence, protection, (C⁺), closed sections | Thm 3.1 | PROVED |
| Continuity, symmetry, monotonicity of Φ along 𝔽 | Lemma 3.2 | PROVED |
| Repair lemma | Thm 3.3 | PROVED; NUMERICS |
| All class-3 fills of all sources, world-by-world status | Cor 3.4 | PROVED |
| Swap-invariant splices; T/N; B-restorations | Prop 3.5 | PROVED; NUMERICS |
| Dominators of a fixed fill avoid the edge | Prop 3.6 | PROVED |
| Commitment system, tubes, 𝓘, (H_acc) on the arc | Thm 3.7 | PROVED |
| Imported exclusions checked | §4 | PROVED (each) |
| Later members never repair 3-improvements; two directions | Prop 5.1 | PROVED |
| No symmetric repair of other-class fills in a symmetric relation | Prop 5.2 | PROVED |
| Additive certificates need a 2-D registered sheet | Prop 5.3 | PROVED |

---

## 1. The joint choice (posted first as DRAFT for PP70; unchanged in substance)

**Family.** One curve of coherent models, indexed along the whole closed segment from u to h₁₂ = (½, ½, 0):
- θ ∈ [0, ⅓]: C_θ = R_α, with α = 3θ and K_α = (1−α)M + αK_N (T → N);
- θ ∈ [⅓, ⅔]: C_θ = J_β, with β = 3θ − 1 and K = (1−β)K_N + βK_{L₀} (N → L₀);
- θ ∈ [⅔, 1]: C_θ = F_t, with t = 3θ − 2 and K = conv(v_t, M₀) (L₀ → D\*).

Index p(θ) := (1−θ)u + θh₁₂ = ((2+θ)/6, (2+θ)/6, (2−2θ)/6). So C_0 = T at u, C_⅓ = N, C_⅔ = L₀, and C_1 = D\* at h₁₂. Write 𝔽 := {C_θ : θ ∈ [0, 1]}.

**Relation.** One total relation 𝒲: X ⪯_w Y iff Φ_w(X) ≤ Φ_w(Y), where Φ_w(X) := ∫ f_w(g, X(g)) dμ, for the explicit field f of §2.

**Repair rule.** For X ∉ 𝔽 with Φ₁(X) = Φ₂(X) ≤ Φ₁(T):

  θ'(X) := min{θ ∈ [0, 1] : Φ₁(C_θ) = Φ₁(X)}.

Verdicts: a tie at worlds 1 and 2, and C_θ' ≺₃ X.

**Commitment scheme.**
- Commit guidance.
- Commit the whole 𝒲-row of every member: every record out of every C_θ, at every world.
- Reserve each committed refusal of (X, w) on a rival-dependent open tube (§3.4).

---

## 2. Construction

### 2.1 The curve

**Lemma 2.1 (PROVED; CHECKED, `geom69.out` C1–C2).**
- (a) For every g, θ ↦ C_θ(g) takes one of the following patterns:
  - (i) constant;
  - (ii) T(g) → S at τ₁(g) ∈ (0, ⅓];
  - (iii) S → D\*(g) at τ₂(g) ∈ (⅓, 1);
  - (iv) T(g) → S → D\*(g) at τ₁ < τ₂, with D\*(g) ≠ T(g).

  Pattern (ii) or (iv) occurs iff g ∈ L := {T ≠ N}. Pattern (iii) occurs iff T is silent at g and D\*(g) ≠ S.
- (b) **By class** (A majority, B minority; Lemma 1.2(b) of PP67):
  - on M₃: Q₃ = Sil(T) ∩ M₃ has S → A; R_B = L ∩ M₃ has B → S → A; the rest is constant A;
  - on M₁ (and symmetrically M₂): L ∩ M₁ has A → S, or A → S → B; Q₁ has S, or S → B; the rest is constant A or constant B;
  - unanimous problems are constant correct.
- (c) **The curve is 3-descending** (C_r ⊵₃ C_θ for r < θ) and 1-and-2-improving in the sense of Lemma 2.2(c).
- (d) The switching loci {g : τ_i(g) = θ} are null for every θ. Hence C_θₙ → C_θ a.e. whenever θₙ → θ.
- (e) Every member is swap-invariant: C_θ ∘ σ = C_θ, and τ_i ∘ σ = τ_i.

*Proof.*
- **Support functions add.** For Minkowski combinations, min_{K} k·g is the same combination of the minima.
  - On [0, ⅓] these minima are (1−α)h_M + αh_{K_N}. Since M ⊆ K_α ⊆ K_N, the R-part only withdraws answers, and only on L.
  - On [⅓, 1], K decreases from K_N to M₀: K_{L₀} ⊆ K_N, and v_t ∈ conv(v_s, h₁₂) ⊆ K_s for t > s. So answers are only added, and every K contains M₀. Hence every new answer is D\*'s answer.
- **No answer is ever revisited.** On L, D\* differs from T. So the answer added later is never T's.
- **Thresholds.** On the R-part, τ₁ = α\*/3 with α\* = h_M/(h_M − h_{K_N}), which is the unique root of a linear function. On the J- and F-parts, the first answer time is the root of a linear function in β, or in t through v_t·g.
- **(c).** On L, T is 3-correct; every added answer is D\*'s, and D\* ⊴₃ T (PP64 Lemma 4.2). This is also REFEREE_round56's confirmation of the audit's geometry, relay item (2).
- **(d).** At a switching time θ, g lies on the boundary of the dual cone of K_θ, which is null.
- **(e).** M, M₀, K_N, v₃ and h₁₂ are all swap-invariant. ∎

### 2.2 The field

Put f_w(g, a) := |g|·φ_w(g, a), with φ(g, S) := 0. Write U_a(θ) := 3p(θ)·φ(g, a) = (2+θ)(φ₁ + φ₂)/2 + (1−θ)φ₃.

On **M₃**, take φ = (P, P, R) (so f₁ = f₂):

| pattern | A: (P_A, R_A) | B: (P_B, R_B) | U_A, U_B |
|---|---|---|---|
| S → A at τ₂ | (−(1−τ₂), 2+τ₂) | (1, −1) | 3(τ₂−θ), 1+2θ |
| A constant | (−1, 1) | (1, −1) | −1−2θ, 1+2θ |
| B → S → A | (−(1−τ₂), 2+τ₂) | (1−τ₁, −(2+τ₁)) | 3(τ₂−θ), 3(θ−τ₁) |

On **M₁**, with odd world 1 and vectors listed as (world 1, world 2, world 3), set φ(A) = (a₁, −a₂, −a₃) and φ(B) = (−b₁, b₂, b₃). Write δ(τ) := 2(1−τ)/(2+τ).

| pattern | a | b |
|---|---|---|
| A constant | (1, 2, 1) | (1, 2, 1) |
| B constant | (3, 1, 1) | (4, 1, 1) |
| A → S at τ₁ | (1+δ(τ₁), 1, 1) | (1, 2, 1) |
| A → S → B | (1+δ(τ₁), 1, 1) | (1+δ(τ₂), 1, 1) |
| S constant | (3, 1, 1) | (1, 2, 1) |
| S → B at τ₂ | (3, 1, 1) | (1+δ(τ₂), 1, 1) |

Then:
- U_A = 3(θ−τ₁)/(2+τ₁) in the A → S rows;
- U_B = 3(τ₂−θ)/(2+τ₂) in the → B rows;
- every other U is of fixed sign on [0, 1]: U_A ≤ −1 − θ/2 for "A constant"; U_A ≥ 1 + 2θ for a = (3, 1, 1); U_B ≥ 2 − θ/2 for b = (1, 2, 1); U_B ≤ −2 − 5θ/2 for b = (4, 1, 1).

On **M₂**, set φ(σg, a) := swap₁₂ φ(g, a). On **unanimous** problems, φ = (−1, −1, −1) for the correct answer and (1, 1, 1) for the wrong one. For contradictory advice X, φ_w(X) := 1 + max_a φ_w(a) at each world.

**Lemma 2.2 (PROVED; CHECKED, `geom69.out` C3–C6).**
- (a) f is measurable, |f| ≤ 6|g|, and f is strictly rank-monotone at every world and every g. Moreover f₁ = f₂ on M₃, and f is swap-equivariant: f_w(σg, a) = f_{σw}(g, a).
- (b) **Pathwise Bayes.** For a.e. g and every θ ∈ [0, 1] ∖ {τ₁(g), τ₂(g)}, C_θ(g) is the **unique** minimiser of p(θ)·f(g, ·) over the four advices. This includes θ = 0, which gives T, and θ = 1, which gives D\* with p(1)₃ = 0.
- (c) Every switch along the curve strictly lowers φ₁ + φ₂ and strictly raises φ₃.

*Proof.*
- **(a).** Read off the tables. All entries lie in [−3, 4], and the contradictory entry exceeds every other at every world. The signs give rank monotonicity: on M₃, P_A < 0 < P_B and R_B < 0 < R_A; on M₁, A is wrong only at world 1 and B is right only at world 1. τ_i are measurable by Lemma 2.1, and τ_i ∘ σ = τ_i gives equivariance.
- **(b).** Using the closed forms of U, the advice with the least U on each sub-interval is exactly the pattern of Lemma 2.1, with strict inequality off the thresholds. For example, in the B → S → A row: U_B < U_A iff θ < (τ₁+τ₂)/2, and both cross zero at τ₁ and τ₂. At θ = 0 and θ = 1 the inequalities are strict, because 0 < τ₁ and τ₂ < 1. Contradictory advice is never minimal.
- **(c).** Read off: P falls and R rises on M₃; on M₁, φ₁ + φ₂ goes δ(τ₁) → 0 → −δ(τ₂). ∎

**Definition 2.3.** X ⪯_w Y in 𝒲 iff Φ_w(X) ≤ Φ_w(Y), for w = 1, 2, 3. Φ is finite for every measurable model, since μ is Gaussian.

The field is a proof device, but here it **is** the module relation. It realises one curve only. It is not the CPM realisation problem, which requires coherent Bayes acts at every weight; off the arc, 𝒲's Bayes acts are not coherent and are not registered.

---

## 3. The milestone for class 3

### 3.1 Axioms and the registered family

**Theorem 3.1 (PROVED).**
- (i) 𝒲 is reflexive, satisfies (IB) for every record (so every copy at every carrier), strict (G) at every world, and (TC) on every triangle, for all measurable models.
- (ii) For every θ and every model X, p(θ)·Φ(C_θ) ≤ p(θ)·Φ(X), with equality iff X = C_θ a.e.
- (iii) **Defence.** For every θ and every X there is w ∈ supp p(θ) with C_θ ⪯_w X. For θ < 1, supp p(θ) = {1, 2, 3}; for θ = 1 it is {1, 2}.
- (iv) **Protection and (C⁺).** If X ⪯_w C_θ at every w, then X = C_θ a.e. So each C_θ is undominated, its only all-world tie partner is itself, and rules III and IV hold for the registered set P = 𝔽.
- (v) **Closed sections.** For every fixed X and w, A_w(X) := {θ : C_θ ⪯_w X} is closed in [0, 1], and p(A_w(X)) is closed in Δ.

*Proof.*
- **(i).** Each world is a total preorder. Φ_w(Y) − Φ_w(X) is the integral over supp rec(X, Y) of the new values minus the old, so verdicts are functions of records. Strict monotonicity of f_w gives strict (G).
- **(ii).** Integrate Lemma 2.2(b). The integrand of the difference is ≥ 0 a.e., and > 0 wherever X ≠ C_θ, off a null set.
- **(iii).** Apply (ii). The weights in p(θ) are positive exactly on supp p(θ).
- **(iv).** Φ(X) ≤ Φ(C_θ) coordinatewise gives p(θ)·Φ(X) ≤ p(θ)·Φ(C_θ), so X = C_θ by (ii).
- **(v).** θ ↦ Φ_w(C_θ) is continuous by Lemma 2.1(d) and dominated convergence (|f| ≤ 6|g|). The map p is a homeomorphism onto a compact arc. ∎

**Lemma 3.2 (PROVED).**
- (a) Φ₁(C_θ) = Φ₂(C_θ) for every θ.
- (b) θ ↦ Φ₁(C_θ) is continuous and non-increasing, and θ ↦ Φ₃(C_θ) is non-decreasing.
- (c) Φ₁(C_1) = min{Φ₁(X) : Φ₁(X) = Φ₂(X)}, attained only at D\*.

*Proof.*
- **(a).** By (H_σ), Lemma 2.2(a) and C_θ ∘ σ = C_θ: Φ₁(X) = Φ₂(X ∘ σ).
- **(b).** Lemma 2.2(c) gives the change of Φ₁ + Φ₂ = 2Φ₁, and of Φ₃.
- **(c).** Apply Theorem 3.1(ii) at θ = 1, where p(1) = (½, ½, 0). ∎

### 3.2 The repair lemma

**Theorem 3.3 (PROVED; NUMERICS `inst69.out` T3–T4).** Let X ∉ 𝔽, with Φ₁(X) = Φ₂(X) ≤ Φ₁(T). Put

  θ' := min{θ ∈ [0, 1] : Φ₁(C_θ) = Φ₁(X)}.

Then:
- θ' exists, and θ' < 1;
- C_θ' ⪯_w X and X ⪯_w C_θ' for w = 1, 2;
- C_θ' ≺₃ X.

So C_θ' strictly dominates X in 𝒲.

*Proof.*
- **Existence.** The set of such θ is closed. It is non-empty by the intermediate value theorem: Φ₁(C_0) = Φ₁(T) ≥ Φ₁(X) ≥ Φ₁(C_1), by Lemma 3.2.
- **The verdicts.** By Theorem 3.1(ii) at p(θ'), using the equal first two coordinates,

  p₃(θ')·(Φ₃(C_θ') − Φ₃(X)) ≤ 0,

  with equality iff X = C_θ', which is excluded since X ∉ 𝔽.
- **θ' < 1.** If θ' = 1, then Φ₁(X) = Φ₁(D\*), and Lemma 3.2(c) forces X = D\* ∈ 𝔽.
- Hence p₃(θ') > 0 and Φ₃(C_θ') < Φ₃(X). ∎

**Corollary 3.4 (every class-3 fill of every source; PROVED).** Fix s ∈ [0, 1] and a non-null measurable E ⊆ Sil(C_s) ∩ M₃. Put Y := C_s[E ↦ A]. Then:
- (a) If Y ∈ 𝔽, Y is coherent and registered and needs no repair. Otherwise Theorem 3.3 applies, with θ'(s, E) ∈ (s, 1).
- (b) C_θ' is silent on a non-null part of E, so the audit's path obstruction is respected.
- (c) **World by world**, rec(C_θ', Y) is mixed at worlds 1, 2 and 3, so none of the three verdicts is guidance:
  - at worlds 1 and 2 it is a non-guidance tie;
  - at world 3 it is a non-guidance strict acceptance, with Y ⋠₃ C_θ'.
- (d) **Repeatable step.** C_θ' is itself a source, and its class-3 fills are repaired by the same rule at θ'' > θ'. As μ(E) → 0, θ'(s, E) → s\* := max{θ : Φ₁(C_θ) = Φ₁(C_s)}. Here s\* = s whenever every band (s, s+δ) carries non-null switches (CHECKED for twelfth-bands in PP70 G3; for all bands, CONJECTURE). In that case repairs accumulate at every source, as PP70 Prop 1.5 says they must.

*Proof.*
- **(a), the hypotheses of Theorem 3.3.** f₁ = f₂ on M₃, so Φ₁(Y) − Φ₁(C_s) = Φ₂(Y) − Φ₂(C_s) < 0, by strict (G), since A is 1-correct. Together with Lemma 3.2(a), Φ₁(Y) = Φ₂(Y) < Φ₁(C_s) ≤ Φ₁(T). Since Φ₁(C_θ) ≥ Φ₁(C_s) > Φ₁(Y) for θ ≤ s, θ' > s.
- **(b).** Suppose C_θ' = A a.e. on E, and put Z := C_θ'[E ↦ S]. Then rec(C_s, Z) = rec(Y, C_θ'), both supported off E with old side C_s. So Φ(Z) − Φ(C_s) = Φ(C_θ') − Φ(Y), which is (0, 0, < 0). Then Z dominates C_s, contradicting Theorem 3.1(iv).
- **(c), world 3.** C_θ' is 3-better on the part of E given by (b). It is also 3-worse somewhere off E. Otherwise C_θ' would differ from Y only on E ∩ {C_θ' = S}, where it is strictly 1-worse, and then Φ₁(C_θ') > Φ₁(Y), contradicting the tie. Off E, every difference is a forward change from C_s, which is 3-worsening (Lemma 2.1(c)).
- **(c), worlds 1 and 2.** If C_θ' were pointwise weakly 1-better or 1-worse than Y, it would be so strictly, since the two differ (by (b)). Strict monotonicity of f₁ would then break the tie. World 2 is the same.
- **(d).** Φ₁(Y) → Φ₁(C_s) from below, and θ ↦ Φ₁(C_θ) is continuous and non-increasing. ∎

**Prop 3.5 (splices; PROVED; NUMERICS T4).** Let 0 ≤ a < b ≤ 1 and let H ⊆ {C_a ≠ C_b} be measurable, with H ∩ (M₁ ∪ M₂) swap-invariant. Put Z := C_a[H ↦ C_b]. If Z ∉ 𝔽, Theorem 3.3 applies, and θ'(Z) ∈ [a, b].

In particular this covers:
- every T/N splice T[H ↦ N] = N[L∖H ↦ T] with H ∩ (M₁ ∪ M₂) swap-invariant;
- every B-restoration N[H ↦ T] with H ⊆ R_B;
- every splice of a source with its own repair of that kind.

*Proof.*
- **Equal first two coordinates.** On M₃, f₁ = f₂. On the swap-invariant part, change variables g ↦ σg using (H_σ). So Φ₁(Z) = Φ₂(Z).
- **The range.** Each problem in H makes a complete forward change from C_a(g) to C_b(g). Each such change lowers φ₁ + φ₂ (Lemma 2.2(c)). So Φ₁(C_b) ≤ Φ₁(Z) ≤ Φ₁(C_a), and the intermediate value theorem on [a, b] places θ' there. ∎

Two remarks.
- **The guidance status of a splice repair depends on the splice.** At worlds 1 and 2 the tie forces mixing, by the argument of Cor 3.4(c). At world 3 the strict verdict can be a guidance acceptance, when C_θ' ⊵₃ Z. This agrees with PP70 Prop 1.7.
- **REFEREE_round56 caution (3)** says that R_α can be pointwise worse at world 2 than an incoherent Z_H. Our repair index is not the audit's σ-window choice. It is fixed by Φ₁-equality, which builds in worlds 1 and 2.
- The splices of the referee's item (4) (H ⊇ P_w for one world w) **are** repaired here whenever H is swap-invariant on M₁ ∪ M₂: they get new dominators, members strictly between a and b.

### 3.3 Fixed rivals do not run to the edge

**Prop 3.6 (PROVED).** For a class-3 fill Y ∉ 𝔽 of C_s as in Cor 3.4, the dominator set Dom(Y) := {θ : C_θ ⪯_w Y for all w} is a compact subset of [0, 1).

*Proof.*
- Dom(Y) is an intersection of sections, so it is closed (Theorem 3.1(v)).
- D\* = A a.e. on M₃, so D\* = Y on E. Off E, D\* ⊴₃ C_s (Lemma 2.1(c)). So D\* ⊴₃ Y, and D\* ≠ Y since Y ∉ 𝔽.
- Strict (G) gives D\* ⋠₃ Y. So 1 ∉ Dom(Y). ∎

Hence the hypothesis of PP68 §1(b), the same fixed rival served by later dominators that accumulate on the edge, never holds. Including the endpoint costs nothing for class-3 fills. D\* has no class-3 fills, because it answers a.e. on M₃.

### 3.4 The commitment system and its sections

**Tubes.** Fix a rival X and a world w. Put R := [0, 1] ∖ A_w(X), which is open by Theorem 3.1(v). For θ ∈ R let

  r(θ) := ½·min{dist(p(θ), p(A_w(X))), dist(p(θ), ∂Δ)} for θ < 1,

and drop the second term for θ = 1. Then

  U_w(X) := ⋃_{θ∈R} B(p(θ), r(θ)) ∩ Δ.

The radii depend on X and w, and shrink to 0 at the boundary of the section. There are no fixed balls.

**Theorem 3.7 (PROVED).** Let Σ consist of:
- D := p([0, 1]), with C_{p(θ)} := C_θ and P := 𝔽;
- Acc_w and Ref_w := 𝒲's verdicts on every record carried by a member, at every world, together with guidance;
- Res := {(U_w(X), X, w)}.

Then:
- (a) Σ satisfies PP64's invariant (I1)–(I8) and the germ condition.
- (b) **(H_acc), strong form, on the arc.** Every negative clause entailed by Σ and the ground clauses whose literals all lie at arc indices has a literal that is committed refused, with a reservation.
- (c) Σ's signed closure on the arc is contained in 𝒲. So it is contradiction-free and contains every repair verdict of §3.2.
- (d) (I9) adds nothing: accepted index sets are closed.

*Proof.*
- **(a).**
  - (I1)–(I5) are Theorem 3.1(i), (iv), together with totality.
  - (I6): if q = p(θ) ∈ U_w(X), the ball containing it is centred at a refusing θ₀ with |p(θ) − p(θ₀)| < r(θ₀) < dist(p(θ₀), p(A_w(X))). So θ ∉ A_w(X), and the refusal is committed.
  - (I7) holds because every refusal of every member, including every (IB) copy, is a refusal of some (X, w) at some θ ∈ R.
  - (I8): let q ∈ Δ and let θ\* be the index of the arc point nearest q. If q ∈ U_w(X), then by the same estimate θ\* refuses X at w. So Rz_q(X) is contained in C_θ\*'s refusal worlds, and these miss a defence world (Theorem 3.1(iii)). That world lies in supp q: tubes around θ < 1 avoid ∂Δ, so edge points q lie only in tubes around θ = 1, where D\* defends at 1 or 2.
  - The germ condition is the openness of R.
- **(b).** 𝒲 is a total relation satisfying every ground clause at arc indices. A clause entailed at those indices holds in 𝒲, so one of its literals is false in 𝒲. That literal is committed refused, by construction.
- **(c).** Same argument.
- **(d).** By Theorem 3.1(v). ∎

The nearest-point selection Ĉ_q := C_θ\*(q) is reservation-compatible on every tube (PP64 (H1)), by the (I8) estimate. It is provisional only.

**Bequest, and what is open.**
- Committed rows transmit through (IB) to every future carrier, by PP67 §8.5. 𝒲 shows that all these copies are jointly satisfiable.
- Every index off the arc is unassigned. This includes the rest of the edge, where PP65 Prop 3.2 needs infinitely many values.
- Tubes around θ = 1 bind edge indices near h₁₂: future edge models there must refuse X at w whenever D\* does.
- (H_acc) for clauses with literals at future carriers (PP67 (O2)) is OPEN.

**On "one relation".** 𝒲 has undominated incoherent models off the arc: the Bayes acts at off-arc weights. So it is the **module** relation, not a full cover. That is consistent with every full-cover exclusion (§4). Global (C) is established in PP64's sense for the registered class, through (I3)–(I5); its full form is discharged only at D = Δ, by PP64 Thm 2.3.

---

## 4. Imported exclusions and relays, checked against their hypotheses

- **Theorem Q (PP57 Thm 4.2).**
  - Its hypothesis (L0⁺) is a Λ-type lexicographic first level on a posterior neighbourhood. That fails here.
  - Its mechanism is a non-null non-conic F ⊆ {C_a ≠ C_b} with zero increments at all three worlds. That cannot exist here: C_a[F ↦ C_b] would tie C_a in Φ, and Theorem 3.1(ii) forces F to be null.
- **Theorem E (PP62).** It needs a member swap balanced for the endorsing field. The same argument excludes one.
- **Theorem J (PP63).** It concerns additive kernels with negative (h, S) two-cycles defending a **two-dimensional** posterior neighbourhood. 𝔽 is one-dimensional, and the referee notes that one-parameter families escape.
- **J1 (PP11)** concerns closedness in the rival argument, which is not required.
- **PP67 Prop 7.3 (non-Archimedean world 3).** Its hypothesis is a uniform dominator. Here N_E → C_s in measure (Cor 3.4(d)), which is exactly its escape clause (d).
- **PP67 Prop 7.4.** It needs every generation silent on one fixed E₀ (relay item (5)). Our generations answer on parts of each earlier fill. The bound is respected, not contradicted.
- **Path obstruction.** Respected: Cor 3.4(b).
- **PP68 Lemma 4.2 (edge lemma).** It holds in 𝒲: C_s ⋠₁,₂ C_θ' and C_s ⪯₃ C_θ'.
- **PP68 Thm 4.3.** 𝔽 is linearly ordered, so there are no 2- or 3-cycles.
- **PP68 Thm 4.4.** Its chain is realised as a continuum, and no convergence of iterated parameters is used.
- **PP68 Prop 1.3 (sharing).** It needs one model serving every subset of a fixed E₀. Nested fills here have distinct repairs, since their Φ₁ differ.
- **PP68 Prop 2.1 (tie plateaus).** There are no fixed balls.
- **PP68 §1(b).** Excluded by Prop 3.6. Relay (5) adds that it needs E_m non-conic; Prop 3.6 does not need that.
- **REFEREE_round55 trap ¬a₁ ∨ ¬a₂.** It holds: Φ₁(D\*) < Φ₁(T), so T ⋠₁ D\* and T ⋠₂ D\*.
- **Full-cover exclusions (single fields; PP32 Thm 3.1; REFEREE_PP32 Thm A and Cor A′; M0 and intersections).** Each needs a whole-simplex selection or a selection on the whole edge. Only one edge index is assigned here. Cor A′ binds any later extension along the edge that keeps 𝒲, so such an extension must change the relation.
- **REFEREE_round56 Theorem R** (L₀ dominates every class-3 fill of N, in a certificate consistent with PP67). It is compatible with this note but not used. Here N's class-3 fills are repaired by curve members between N and D\*, at rival-dependent indices. In 𝒲, L₀ = C_⅔ dominates exactly those fills Y with Φ(C_⅔) ≤ Φ(Y).

---

## 5. Where the rest fails, and at what level

Rivals still in scope:
- N's class-1 and class-2 fills, which include the restorations N[H ↦ T] with H ⊆ L ∩ (M₁ ∪ M₂);
- one-sided T/N splices;
- the other-class fills of every source.

**Prop 5.1 (two directions; PROVED; agrees with PP70 Prop 1.3).** Let the relation satisfy the axioms, and let r < s.
- (a) C_s ⪯₃ C_θ for θ ≤ s is guidance. Hence no later member C_θ (θ > s) is ⪯₃ any strict pointwise 3-improvement of C_s; in particular it is ⪯₃ none of C_s's class-1 or class-2 fills.
- (b) If C_r repairs a class-1 fill of C_s, then C_s ⋠₂ C_r and C_s ⋠₃ C_r, so C_s ⪯₁ C_r. For class 2, swap 1 and 2.

*Proof.* (TC) with the strict guidance link Y ≺_w C_s (A₁ is 2- and 3-correct on M₁). Then C_s ⪯_w B ⪯_w Y ⪯_w C_s is a forbidden cycle. ∎

**Prop 5.2 (no symmetric repair in a symmetric relation; PROVED).** Suppose:
- the relation satisfies (TC) and strict (G) and is swap-invariant (X ⪯_w Y ⟺ X∘σ ⪯_{σw} Y∘σ);
- C is a swap-invariant model defended against B at a world of {1, 2, 3};
- B is swap-invariant.

Then B dominates no class-1 fill Y = C[F ↦ A] (F ⊆ Sil(C) ∩ M₁ non-null), and no class-2 fill.

*Proof.*
- As in Prop 5.1, C ⋠₂ B and C ⋠₃ B.
- Swap invariance, with C∘σ = C and B∘σ = B, turns C ⋠₂ B into C ⋠₁ B.
- So C is undefended against B. ∎

**Consequences.**
- 𝒲 is swap-invariant (Lemma 2.2(a) and (H_σ)), and every member of 𝔽 is swap-invariant. So **no member of 𝔽 repairs an other-class fill of a member, in 𝒲 or in any swap-invariant relation**. The restorations are among these fills.
- **Level.** This is axiom-level given two choices: the symmetric family and a symmetric relation. It is not axiom-level outright.
- **What an in-family repair needs.** A source C_s must accept an earlier C_r at world 1 and refuse it at world 2 (C_r repairs class 1), and the reverse for another C_{r′}. So the verdicts among the symmetric members themselves must break the symmetry between worlds 1 and 2.
- One-sided splices out of T are not covered by Prop 5.2. In 𝒲, no member dominates them (NUMERICS T5).

**Prop 5.3 (additive certificates need a two-dimensional registered class; PROVED).** Let 𝒲′ be any certificate additive at all worlds with an integrable, strictly monotone field. Let C_s be the a.e.-unique λ_s-Bayes act, λ_s > 0. Let Y_n := C_s[F_n ↦ A] with F_n ⊆ Sil(C_s) ∩ M₁ and μ(F_n) → 0, and let B_n be registered models dominating Y_n. Then:
- (a) B_n → C_s in measure.
- (b) Each B_n is weakly λ_n-Bayes for some λ_n (PP38 Thm 3.1(ii), applied to the module). Every limit point λ\* of (λ_n) is a weight for which C_s is weakly Bayes.
- (c) If 𝒲′ and the B_n are swap-invariant, Prop 5.2 is contradicted. So in a swap-invariant certificate the B_n are asymmetric, and so are their mirrors B_n∘σ, which repair the class-2 fills.

*Proof.*
- **(a).** λ_s·Φ(B_n) ≤ λ_s·Φ(Y_n) → λ_s·Φ(C_s). The excess is the integral of a function that is ≥ 0 a.e. and > 0 a.e. on {B_n ≠ C_s}. So μ({B_n ≠ C_s} ∩ {excess > δ}) → 0 for every δ > 0, which is convergence in measure.
- **(b).** Defence against every bounded rival gives a supporting hyperplane of the convex risk set (Lyapunov) at Φ(B_n). Pass to the limit in λ_n·Φ(B_n) ≤ λ_n·Φ(X).
- **(c).** Immediate. ∎

So any additive device that repairs every class-1 fill of every source registers asymmetric Bayes acts accumulating at every member. The registered class is then a two-dimensional sheet around the arc, which is a local, two-dimensional instance of the realisation problem that the brief forbids as an approach.

The barrier for N's other-class fills therefore has two layers:
- **(i) choice level:** symmetry (Prop 5.2);
- **(ii) certificate level:** additivity (Prop 5.3).

Neither is a conflict among the axioms.

**Remark (not pursued; CONJECTURE).** Fresh class-1 and class-2 fills, with F ⊆ Q_k, can probably be repaired by PP67-style keyed models T ∧ D\*_k at isolated indices, with keys κ_k on Q_k. Every member is silent or k-correct on Q_k, so the keys vanish on 𝔽 and sections stay closed. A per-type check is needed: on M₃ the two keyed models must agree with a symmetric extrapolation of the field. Even if it works, the repairs lie outside the family, and restorations stay unrepaired. So it would not meet the brief's criterion.

---

## 6. What to do next

**Option A (smallest step).** Keep 𝔽, T and 𝒲's class-3 verdicts. Add a **σ-breaking** layer on M₁ ∪ M₂ only:
- earlier members serve the class-1 fills and restorations of later members at world 1;
- other earlier members serve class 2 at world 2;
- following Prop 5.1(b), choose the alternation as a function of the rival, not of the index, so that no section alternates.

The test is whether this layer can keep closed sections. It cannot be additive (Prop 5.3), so it must be a genuinely non-additive verdict pattern, of the shape PP61's Cor E.2 model already shows locally.

**Option B.** A two-dimensional Bayes sheet around the arc, with the M₃-part of the advice depending on λ₃ only. The obstruction to watch is that a coherent D_K whose M₃-answers move must change M₁ ∪ M₂ answers: for k ∈ Δ, D_{conv(M ∪ {k})} keeps all of T's answers on M₁ ∪ M₂ iff k ∈ A := {k₁, k₂ ≥ 7/30; k₁, k₂ ≤ (16/7)k₃; k₁ ≤ (16/7)k₂; k₂ ≤ (16/7)k₁}. This is PROVED by testing k·g against the extreme rays of T's closed answer cones on M₁ and M₂. Since A is bounded away from the edge (k₃ ≥ 49/480), every family that approaches the edge silences some of T's other-class answers, and so creates restorations.

---

## 7. Records and obligations that remain unassigned

1. **Indices:** all of Δ off the arc p([0, 1]).
2. **Rows:** the rows of rivals, that is, rival–rival records not carried by members.
3. **Dominators:**
   - other-class fills of every source (§5);
   - one-sided splices;
   - fills of splices.
4. **(H_acc):** clauses with literals at future carriers.
5. **Bequest:** the (IB) copies of all committed member rows, at future carriers; and the tube constraints near h₁₂ on the edge.

---

## 8. Scripts (`r9/PP69_py/`; run `python3 -I -B <script>` in that folder)

| Script → output | Content | Label |
|---|---|---|
| `geom69.py` → `geom69.out` | Exact rationals on 7,703 problems: curve patterns and exact thresholds (C1); census (C2); rank monotonicity of φ (C3); C_θ is the unique argmin of p(θ)·φ on a 1/96 grid and at thresholds ± 10⁻⁶, θ ∈ [0, 1] (C4); f₁ = f₂ on M₃ and swap-equivariance (C5); forward switches lower φ₁ + φ₂ and raise φ₃ (C6). ALL PASS, about 4 min | CHECKED |
| `inst69.py` → `inst69.out` | Empirical swap-symmetrised Gaussian sample with 8,000 atoms, the crossing atom pair split fractionally (T1–T5): Φ₁ = Φ₂; monotonicity; 60 class-3 fills of 12 sources repaired (ties at 1, 2, strict at 3) and silent on part of E; 15 swap-invariant splices repaired between their ends; class-1 fills and one-sided splices dominated by no member. ALL PASS, about 5 s | NUMERICS |
