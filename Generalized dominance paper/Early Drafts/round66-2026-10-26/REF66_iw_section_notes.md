# REF66_iw: referee report on §7 "Infinitely many worlds" of *Universal coverage of coherent sets of desirable gambles (draft)*, and on the infinite-world text in the abstract, introduction and scope

26 October 2026. Referee: IW66a, acting for the lead. I read §7 (source lines 1097–1778), the abstract, the introduction, §9.1, §9.3, §9.4 and Lemma 6.1, which §7 invokes. I checked every proof by hand. I have now read `IW66b_notes.md`, as the lead's request required. Labels: PROVED / CHECKED / CONJECTURE.

## Verdict at the top

**§7 is mathematically sound.** Every theorem, proposition and lemma in it is correct as stated. All repairs requested by IW66a and IW66b have been made correctly; the omissions are deliberate and acceptable. The writer's five new additions are all CORRECT.

**Three sentences outside the formal results are false as written** and must be fixed:

1. **§9.4** says that every dominance relation is "a uniform Brier improvement". In infinite worlds this is false. Theorem 7.9(b) gives only pointwise improvement, and I give a counterexample (§2.1).
2. **The paragraph before Proposition 7.14** says that "in infinite dimensions the uniform version fails". This is false in general. I give an infinite-dimensional E in which uniform (LF) holds (§2.2). Proposition 7.14 itself, and the scope bullet, correctly restrict the claim to C(Ω).
3. **The abstract and the introduction** say that "precise and finitely generated targets are not covered on any one-sided domain". This needs "when E is infinite-dimensional". Remark 7.10 makes ℝⁿ a special case of §7, and there full-dimensional polytopes **are** covered. The abstract also omits full support, which every coverage claim needs.

**On the writer's flags:**
- **Flag 1.** The new definition of one-sidedness is the right one for §7. It is implied by §2's definition but not equivalent to it. §2's definition is unusable when null sets are asymmetric. Two sentences of justification should be added (§3).
- **Flag 2.** I supply an explicit pair of models whose dominance status differs between Ω and any countable norming Ω₀ (§2.3). The paragraph can then state a fact rather than "defined by different conditions".
- **Flag 3.** Stating the uniform-(LF) failure for C(Ω) only is correct and necessary. By §2.2 the restriction cannot be lifted to infinite-dimensional E in general.

## 1. Verdict per item

### 1.1 The writer's additions (requested items)

| # | Item | Verdict | Notes |
|---|---|---|---|
| W1 | Proof of Lemma 7.1(c) (Ω̂, the embedding into C(Ω̂), representation of states by regular Borel probabilities) | **CORRECT** | Ω̂ is closed in the compact metrizable S. Isometry: \|ĥ\| ≤ ‖h‖ on S, with equality approached at evaluations. Order is preserved and reflected. L is well defined by injectivity, and L(ĥ) ≤ sup_Ω h = max_Ω̂ ĥ. The Hahn–Banach extension is dominated by f ↦ max f, so it is positive, and Riesz applies. Nit: L(1) = q(1) = 1 holds directly, since 1̂ = 1 ∈ Ê; the two-inequality argument is also valid. |
| W2 | General proof of Proposition 7.14 (no uniform tube on C(Ω), any K′ ⊆ K) | **CORRECT** | Infinitely many disjoint open V_j exist in an infinite metric space, and Σ k(V_j) ≤ 1, so k(V_j) → 0. P_S(b_j) = 0 because Ω∖V_j ≠ ∅. Then P_K(b_j) ≤ k(b_j), since k ∈ K′ ⊆ K, and ‖h_j‖ ≥ max h_j = 1 − P_K(b_j). The distance from h_j to h_j − k(h_j)1 ∉ U is k(h_j) ∈ [0, k(b_j)]. One implicit step: h_j ∈ ∂D_K needs P_K(h_j) = 0 ⇒ h_j ∈ ∂D_K. That is the converse of Lemma 7.2(b), and it is immediate from h_j + t1 ∈ D_K. Add "since h_j + t1 ∈ D_K for t > 0". |
| W3 | Example 7.4 and §7.8: C∪R differs from every D_Q on a non-null set | **CORRECT** | If q₀ ∈ Q, then P_Q(bω) ≤ q₀(bω) = 0 on R, so (C∪R)∖D_Q ⊇ R, with μ(R) = 1. Otherwise Q is closed and misses q₀, so Q ⊆ {q_s : s ≥ s₁} with s₁ = min Q > 0. On {a < 0, a + bs₁ > 0} we have b > 0, so a + bs > 0 for all s ≥ s₁. This set is open, nonempty (e.g. a = −1, b = 2/s₁) and non-null (Gaussian part), and it misses C∪R ⊆ {a ≥ 0}. I also re-checked the rest of Example 7.4: the states, P_S = min(a, a+b), μ(R) = 1, R ⊆ U∖C, guidance at every world, refusal of (∅,R), and that C∪R is a convex cone excluding 0 and containing {inf h > 0}. |
| W4 | Mutually singular admissible measures (§9.3) | **CORRECT** | Distinct g ∈ E₀ give disjoint lines g + ℝ1, by uniqueness of the decomposition h = (h − h(ω₀)1) + h(ω₀)1. So μ(L′) = Σ_k w_k·0 = 0 and μ ⊥ μ′. D_Q∖L′ is Borel (L′ is a countable union of closed lines), μ-a.e. equal to D_Q, and μ′-null. It is μ′-incoherent because every D_Q contains D_S, which is open and so μ′-non-null by (M3). Add "with K′ ⊆ Q", so that D_Q∖L′ is a model on U. |
| W5 | Remark 7.11 (order unit) | **CORRECT**, with one **wording GAP** | The transport is right. h ↦ h/e is an isomorphism with ‖h/e‖ ≤ ‖h‖/inf e and ‖h‖ ≤ ‖e‖‖h/e‖, so Ẽ is closed, separable and contains 1. It preserves signs, states, P_Q, (M1)–(M3), safety and C_U, and m_ω = e(ω)·m̃_ω. D_S is unchanged: inf h > 0 ⟺ inf h/e > 0. The dead-world claim is right: at ω₁ only the null record is accepted, so dominance is impossible. **Wording:** the dead-world space E = {(t,0)} *has* an order unit in the abstract sense, namely (1,0). So "Some order unit is needed" (remark) and "An order unit is needed" (scope bullet) do not describe what the example shows. The example shows only that a world at which every gamble vanishes is fatal. Repair: "Some condition of this kind is needed: if some world pays 0 on every gamble, … Whether a strictly positive element suffices without a positive lower bound (e.g. c₀ with e(n) = 1/n) is open." |

### 1.2 Repairs requested by IW66a

| IW66a item | Requested | Made? | Verdict |
|---|---|---|---|
| S3(a) | Σ w_k(1 + ‖g_k‖) < ∞ | Lemma 7.3 | CORRECT |
| S3(b) | Full-support argument via the linear homeomorphism Φ | Lemma 7.3 | CORRECT |
| S6 | Coherent-class lemma; note where full support is used | Lemma 7.2(d), Lemma 7.5(d), "Where the conditions are used" | CORRECT. Nit: in 7.5(d), "the converse is Lemma 7.2(a)" should be "K′ ⊆ Q gives P_Q ≤ P_{K′}". |
| B4 | Name the minimax theorem and check its hypotheses | Sion, with hypotheses and attainment stated | CORRECT |
| D2 | Cite Step A for P ≥ 0 on the removed part | Step D: "P(h) ≥ 0 by Step A" | CORRECT |
| P5 / B8 | Margin at every state | Theorem 7.7(i) | CORRECT |
| K4 | State which (LF) holds; relint fails; uniform unattainable; attribute D_K's undominatedness to protection | §7.6 opening, Proposition 7.12, the paragraph after it, Proposition 7.14, Proposition 7.15(a) | CORRECT, with **GAP G1** below |
| P1 | (LF) characterisation | Proposition 7.12 (forms 1 ⟺ 2; normal-cone form omitted) | CORRECT. I re-derived both directions. |
| P2 | Universal cover; K_⊥ = {0} ⇒ covered somewhere; K_⊥ ≠ {0} ⇒ never covered on a one-sided domain | Theorem 7.13 | CORRECT. In (b): s_J/(1 − 2^{−J}) ∈ K, convergence in norm, K norm-closed; strict positivity by density. |
| P3 | Coherent sets of desirable gambles = D_Q a.e. | Proposition 7.16 | CORRECT, with expository **GAP G4** |
| P4 | Order unit | Remark 7.11 | See W5 |
| L5/L6 | μ-relativity; finitely generated exclusion; order unit | §9.3, Theorem 7.13(c) | CORRECT |

### 1.3 Repairs requested by IW66b (its §10)

| # | Requested | Made? | Verdict |
|---|---|---|---|
| 1 | Domain lemma (c∞), (d∞) | Lemma 7.2(d), Lemma 7.5(d) | CORRECT |
| 2 | A2 for every B; safe ⟺ hull test | Lemma 7.5(b), Lemma 7.6 (including "applies to no D_Q at all") | CORRECT |
| 3 | Name the minimax theorem | Sion | CORRECT |
| 4 | Moment-weighted atoms; concentration on lines | Lemma 7.3 and the sentence after it | CORRECT |
| 5 | μ{P_S = 0} = 0 is essential | Example 7.4 and the sentence after Lemma 7.8 | CORRECT |
| 6 | Order unit; dead world; c₀ open | Remark 7.11 | CORRECT; wording as in W5 |
| 7 | Literal (LF); uniformity lost; characterisation; universality; strictly positive p in general E | All except general-E contamination (deliberately omitted) | CORRECT; omission acceptable, since contamination is stated only on C(Ω) |
| 8 | p without full support | Proposition 7.15(b),(c) | CORRECT. I re-derived (c): k′(g) = P_K(g) + ε(r(g) − min g), and equality forces g to be constant, hence 0. |
| 9 | Six scope items | §9.3 bullets; universality in §9.1 | CORRECT |
| — | Ω versus Ω₀ (F3) | "Worlds and norming sets" paragraph | CORRECT; see flag 2 and §2.3 |
| — | Atomless λ suffices, no density needed | Lemma 7.3 | CORRECT |

### 1.4 The rest of §7, re-checked line by line

| Result | Verdict | Notes |
|---|---|---|
| §7.1 set-up; Lemma 7.1(a),(b) | CORRECT | — |
| Lemma 7.2 (a)–(d) | CORRECT | conv(Q₁ ∪ Q₂) is compact as an image of Q₁ × Q₂ × [0,1]. Separation in (E*, w*) uses that its dual is E. |
| (M1)–(M3); Lemma 7.3 | CORRECT | The Fubini set {t = −P_Q(g)} is Borel because P_Q is continuous. |
| "Where the conditions are used" | CORRECT | Add: (M3) is also used for the one-sidedness of U (§7.6). |
| Lemma 7.5 (a)–(d) | CORRECT | — |
| Lemma 7.6 | CORRECT | — |
| Theorem 7.7, Steps A–D | CORRECT | Identical in substance to the refereed audit proof. Saddle step, uniqueness, choice of τ and contraction all re-checked. |
| Lemma 7.8 (a)–(c) | CORRECT | In (c), the points of (b) can be chosen inside Ω′ because inf_{Ω′} h_j = inf_Ω h_j. |
| Theorem 7.9, via Lemma 6.1 | CORRECT | (A1)–(A5) are verified correctly. (A2) uses D_S ⊆ C (Lemma 7.2(a)). (G) follows from 6.1(a). (b) follows from 6.1(a),(f). |
| "Worlds and norming sets" | CORRECT | See flag 2 (§2.3). |
| Remark 7.10 | CORRECT | — |
| §7.6: one-sidedness of U under (M3) | CORRECT | See flag 1 (§3). |
| Proposition 7.12 | CORRECT | (M2) is not needed. Harmless. |
| Paragraph after 7.12: "p is not an algebraic relative interior point of K" | **GAP G1** | No proof is given, and it is **false for finite Ω**, which the contamination subsection allows ("Ω a compact metric space"). It is true for every infinite Ω (PROVED, §2.4). Repair: "when Ω is infinite", plus one line of proof. |
| Theorem 7.13 (a)–(c) | CORRECT | (c) needs neither (M3) nor symmetric null sets under the new one-sidedness definition. |
| Paragraph before Proposition 7.14 | **ERROR (statement)** | See §2.2. |
| Proposition 7.15 (a)–(c) | CORRECT | In (b), (LF) fails because D_K ∈ M_U (p ∈ K) and P1(2) fails at k = p. |
| Proposition 7.16 | CORRECT, **GAP G4** (exposition) | The proof reuses the symbol φ for two functionals, and the order of claims is confusing. Also, D need not be Borel: D_{Q_D} ⊆ D ⊆ C_{Q_D}, so D is measurable for the completion of μ only. Say "μ-measurable (in the completion) and equal to D_{Q_D} a.e." |

### 1.5 Abstract, introduction and scope (infinite-world text)

| Location | Verdict | Repair |
|---|---|---|
| Abstract: "given a measure … with a finite first moment and null indifference boundaries" followed by "universal cover … covered credal sets characterised …" | **GAP G2** | Coverage, universality and the (LF) characterisation all need full support (M3). Add "and full support". |
| Abstract: "precise and finitely generated targets are not covered on any one-sided domain" | **ERROR (scope)** | It is false for finite-dimensional E, which includes the finite special case (Remark 7.10). Add "when the gamble space is infinite-dimensional". |
| Abstract: "contamination models (1−ε){p} + εS are covered" | GAP (minor) | Add "with ε > 0". ε = 0 is the precise case, which is not covered. |
| Introduction, paragraph on §7 | Same two points | Mention full support; add "when E is infinite-dimensional" to "precise and finitely generated targets". |
| §9.1 | CORRECT | Optionally note that "one-sided" in the last sentence is the §7 notion. |
| §9.3 bullets | CORRECT, except the order-unit bullet | See W5. "Local freedom is literal, not uniform" correctly says "on C(Ω) with Ω infinite". |
| §9.4: "every dominance relation a uniform Brier improvement" | **ERROR** | False for Theorem 7.9 (counterexample, §2.1). Repair: "a Brier improvement at every world, which is uniform when there are finitely many worlds; for the repair N of every incoherent model it is uniform in any case (Theorem 7.7(i))". |

## 2. Proofs supporting the verdicts (PROVED)

### 2.1 Dominance in §7 need not be uniform (refutes §9.4 as written)

**Setting.** Ω = (0,1] and E = {a + bω}, with states q_s(a + bω) = a + bs for s ∈ [0,1] (as in Example 7.4). Take K′ = {q_{1/2}}, so U = {a + b/2 > 0}, and let μ be the standard Gaussian on (a,b). Then μ satisfies (M1)–(M3). For (M2): {P_Q = 0} meets each line h + ℝ1 in one point, so it is Lebesgue-null by Fubini.

**Construction.** Write m(Y) = ∫_Y h dμ ∈ E ≅ ℝ².
- Choose a nonempty open ball V ⊆ U∖cl D_S, for example around (−1, 4).
- R_V ≔ {m(A₁) − m(B) : A₁ ⊔ B = V} = {∫_V f h dμ : −1 ≤ f ≤ 1}. This equality is Lyapunov's theorem applied to the nonatomic ℝ²-valued measure h dμ on V.
- R_V is convex and symmetric. Its support function λ ↦ ∫_V |λ·h| dμ is positive and continuous on the unit circle, so R_V contains a ball of some radius ρ > 0.
- Choose a small ball A₀ ⊆ D_S, disjoint from V, with ‖m(A₀)‖ < ρ/2. Put z ≔ (0, β) with 0 < β < ρ/2.
- Then z − m(A₀) ∈ R_V. Take the corresponding A₁, B ⊆ V and put A ≔ A₀ ∪ A₁.

**The record.** r ≔ (A, B) consists of disjoint Borel subsets of U, and m(r) = z, that is, m_ω(r) = βω. It is safe by Lemma 7.6: hull(B) ⊇ D_S ⊇ A₀ and μ(A₀) > 0.

**Conclusion.** With Y ≔ A and X ≔ B we have r(Y,X) = r. By Theorem 7.9(b), Y strictly dominates X. But inf_Ω(m_ω(Y) − m_ω(X)) = inf_{ω∈(0,1]} βω = 0. So dominance is not uniform. ∎

### 2.2 Uniform (LF) can hold in an infinite-dimensional E (refutes the paragraph before Proposition 7.14 as written)

**Setting.** Ω = {−1,1}^ℕ, an infinite compact metric space. r_n(ω) = ω_n. Put

  E ≔ {a + Σ a_n r_n : a ∈ ℝ, (a_n) ∈ ℓ¹}.

**Norm and order.** Choosing ω_n = sgn(a)·sgn(a_n) gives

  ‖a + Σ a_n r_n‖_∞ = |a| + Σ|a_n|, and inf = a − Σ|a_n|.

So E ≅ ℝ ⊕₁ ℓ¹ is closed, separable, infinite-dimensional, and contains 1.

**States.** The states are q_c(a + Σ a_n r_n) = a + Σ a_n c_n with sup|c_n| ≤ 1. Positivity is equivalent to a ≥ Σ|a_n| ⇒ a + Σ a_n c_n ≥ 0.

**Target and domain.** Take k₀ ≔ q₀ (the uniform product measure), K′ = {k₀}, U = {a > 0}, and K = S (or any contamination K = (1−ε){k₀} + εS).
- For K = S: ∂D_K∖{0} = {a = Σ|a_n| > 0}, where ‖h‖ = 2a, and dist(h, E∖U) = a. So the open ball of radius ½‖h‖ about h lies in U, and **uniform (LF) holds with δ = ½**.
- For the contamination K: P_K = a − εΣ|a_n|, and the relative distance is ε/(1+ε).

Also K_⊥ = {0}, so the target is covered (Theorem 7.13(a)).

**Consequence.** The failure of uniform (LF) is a property of C(Ω), not of infinite dimension. This answers flag 3: the restriction to C(Ω) is necessary. The paragraph before Proposition 7.14 should read: "…in finite dimensions it is automatically uniform; on E = C(Ω) with Ω infinite the uniform version fails (Proposition 7.14), although in other infinite-dimensional spaces it can hold." Optionally, add the example as a remark.

### 2.3 Flag 2: an explicit change of dominance status between Ω and Ω₀

**Setting.** Ω = [0,1] and E = span{1, ω, ω²} ≅ ℝ³. Take any countable Ω₀ ⊆ [0,1] with inf_{Ω₀} h = inf_Ω h for all h ∈ E, such as ℚ ∩ [0,1] or the set of Lemma 7.8(b). Pick ω\* ∈ [0,1]∖Ω₀. Take K′ = {Lebesgue mean}, so U = {a + b/2 + c/3 > 0}, and let μ be the standard Gaussian on the coefficients.

**Construction.** Exactly as in §2.1, now in ℝ³, with V a small ball around (−1, 4, 0) ∈ U∖cl D_S. This gives a safe record r = (A, B) with

  m(r) = β(ω − ω\*)², for small β > 0.

**Conclusion.** Put Y = A and X = B.
- With world set Ω₀: m_ω(r) > 0 at every ω ∈ Ω₀, so Y strictly dominates X (Lemma 6.1(a)).
- With world set Ω: m_{ω\*}(r) = 0 and r is non-null. So r is neither safe-accepted nor guidance at ω\*: guidance would force m_{ω\*}(r) > 0 by Lemma 7.8(a). Hence Y does not weakly dominate X.

So the two dominance relations differ, while the undominated sets coincide, as the paragraph proves. ∎

Suggested text: "…defines a different dominance relation: for E = span{1, ω, ω²} on [0,1], some safe record has moment β(ω − ω\*)² with ω\* ∉ Ω₀, so its models are ordered strictly at every world of Ω₀ but not at ω\*. Its undominated set is nevertheless the same."

### 2.4 G1: p is not in the algebraic relative interior of K when Ω is infinite

**Proof.** For k = (1−ε)p + εs, membership of p + t(p − k) in K requires s′ = (1+t)p − ts ≥ 0. So p is in the core of K only if every state s satisfies s ≤ C_s p for some constant C_s.
- If p({x}) = 0 for some x, then s = δ_x violates this.
- Otherwise Ω is countable and p has an atom at every point, with p_n → 0. Choose n_k with p_{n_k} ≤ 4^{−k} and put s = Σ 2^{−k} δ_{x_{n_k}}. Then s/p ≥ 2^k is unbounded.

For finite Ω with p of full support, p **is** in relint K. So the paragraph must say "when Ω is infinite". ∎

## 3. Flag 1: the new definition of one-sidedness

**The definition (§7.6).** V is one-sided if there is no nonempty norm-open O with O ⊆ V a.e. and −O ⊆ V a.e.

**Is it what the proofs need? Yes.** Its only uses are these:
- **Theorem 7.13(c).** (LF) at D_K with 0 ≠ h ∈ K_⊥ yields N ⊆ V a.e. with N ⊇ Ball(h,ρ) ∪ Ball(−h,ρ). So O = Ball(h,ρ) and −O both lie in V a.e. No symmetry of null sets is used. The proof is CORRECT.
- **One-sidedness of U = D_{K′} under (M3).** By Lemma 7.5(d), O ⊆ U and −O ⊆ U, so O ⊆ U ∩ (−U) = ∅. CORRECT.

**Does it agree with the finite definition? No: it is implied by it, but strictly weaker.**
- *Implied (under Lebesgue null sets).* If O ⊆ V a.e. and −O ⊆ V a.e., then O ⊆ −V a.e. by symmetry, so μ(V ∩ (−V)) ≥ μ(O) > 0.
- *Not conversely.* In ℝⁿ, let F be a closed, symmetric, nowhere-dense set of positive Lebesgue measure (a symmetrised fat Cantor set), and put V = int ℝⁿ₊ ∪ F.
  - V ∩ (−V) ⊇ F is non-null, so V is not one-sided in §2's sense.
  - Suppose O is open with O ⊆ V a.e. Since F is nowhere dense, every nonempty open subset of O∖cl(int ℝⁿ₊) contains a non-null open set outside V. So O ⊆ cl ℝⁿ₊, and likewise −O ⊆ cl ℝⁿ₊, which forces O ⊆ {0}, so O = ∅.
  - Hence V is one-sided in §7's sense.

So in the finite special case, Theorem 7.13(c) **strengthens** Proposition lowdim. That is consistent, not contradictory.

**Is it the right notion? Yes. §2's definition is unusable under asymmetric null sets: it is not invariant under a.e.-modification of V.**
- Take μ from Lemma 7.3 with atomic ν and lines L = ∪(g_k + ℝ1), chosen so that −g_k ∉ {g_j}. This is possible since E₀ is uncountable when it is nonzero. Then L ∩ (−L) = ∅.
- V = L is a.e. equal to E, so M_V = M_E, the full two-sided domain. Yet μ(V ∩ (−V)) = 0, so V is "one-sided" in §2's sense.
- Under §7's definition V = L is not one-sided, because every open O satisfies O ⊆ L a.e.

**Repair (required, short).** After the definition, say:
- it depends only on the a.e.-class of V;
- in finite dimensions with (M) it is implied by §2's definition but is strictly weaker, so Theorem 7.13(c) extends Proposition lowdim;
- §2's definition cannot be used here because it is not invariant under a.e.-modification of V when μ's null sets are not symmetric (one-line example: V = L).

Optionally, call it "one-sided in the sense of this section" to avoid a clash with §2.

## 4. Ranked list of required changes

1. **(ERROR) §9.4.** Replace "every dominance relation a uniform Brier improvement" by "every dominance relation a Brier improvement at every world, uniform when Ω is finite; the repair N of Theorem 7.7 improves uniformly in every case". Counterexample: §2.1.
2. **(ERROR) Paragraph before Proposition 7.14.** "in infinite dimensions the uniform version fails" → "on C(Ω) with Ω infinite the uniform version fails (Proposition 7.14); in other infinite-dimensional spaces it can hold". Optionally add the ℝ ⊕₁ ℓ¹ example of §2.2.
3. **(ERROR, scope) Abstract and introduction.** "precise and finitely generated targets are not covered on any one-sided domain" → add "when the space of gambles is infinite-dimensional". Also add full support of the measure (G2), and "ε > 0" for contamination.
4. **(GAP, flag 1) §7.6.** Add the three sentences of §3: a.e.-invariance; strictly weaker than §2 (so 7.13(c) extends Proposition lowdim); why §2's definition fails under asymmetric null sets.
5. **(GAP G1) Paragraph after Proposition 7.12.** "p is not an algebraic relative interior point of K" → add "when Ω is infinite", with the one-line proof of §2.4.
6. **(flag 2) "Worlds and norming sets".** Replace "defined by different conditions" with the explicit example of §2.3 (two sentences).
7. **(wording, W5) Remark 7.11 and the §9.3 bullet "An order unit is needed".** The dead-world space has an abstract order unit. Rephrase as in W5 and keep the open question.
8. **(GAP G4) Proposition 7.16.** Reorder the proof and rename the second φ. State that D is μ-measurable (in the completion), since D need not be Borel.
9. **(minor)** Proposition 7.14: add "since h_j + t1 ∈ D_K for t > 0". Lemma 7.5(d): fix the citation for "the converse". W4: add "K′ ⊆ Q". "Where the conditions are used": add the one-sidedness of U to the uses of (M3). Lemma 7.1(c): note L(1) = q(1) directly (optional).

With 1–6 made, I would accept §7 and the infinite-world text for publication. None of the changes affects a theorem, proposition or lemma statement in §7.

## Third round (Revision 3)

I checked every changed passage in the source of Revision 3 against the required changes in §4.

| # | Required change | Verdict |
|---|---|---|
| 1 | §9.4: dominance is a Brier improvement at every world, uniform when Ω is finite; the repair N improves uniformly in every case | MADE, CORRECT |
| 2 | Before Proposition 7.14: the failure is restricted to C(Ω), with "in other infinite-dimensional spaces it can hold" | MADE, CORRECT. Leaving out the ℝ ⊕₁ ℓ¹ example is acceptable. |
| 3 | Abstract and introduction: full support (for the coverage results); ε > 0 and "on C(Ω)" for contamination; "when the space of gambles is infinite-dimensional" | MADE, CORRECT |
| 4 | §7.6 one-sidedness: a.e.-invariance; implied by §2's definition but strictly weaker (int ℝⁿ₊ ∪ F); failure of §2's definition under asymmetric null sets (the union L of lines) | MADE, CORRECT. The fat-Cantor argument (O ⊆ cl ℝⁿ₊ ∩ −cl ℝⁿ₊ = {0}) and the L example (no −g_k is a g_j, which also excludes g_k = 0) are written correctly. |
| 5 | Relative interior: "when Ω is infinite", with a proof | MADE, CORRECT. The identity p + t(p − k) = (1−ε)p + ε((1+t)p − ts) is right. For ε > 0 the representation in K is unique, so membership in K ⟺ s ≤ ((1+t)/t)p. Both cases are right: an atomless point gives δ_x; in the purely atomic case, s{x_{n_k}}/p{x_{n_k}} ≥ 2^k. |
| 6 | Norming-set example | MADE, CORRECT. Optional wording: choose A₀ first, then A₁ with m(A₁) − m(V∖A₁) = β(ω − ω\*)² − m(A₀), so that the order of choices is explicit. Optionally give an instance of V, e.g. a ball about −1 + 4ω, which lies in U∖cl D_S. |
| 7 | Order-unit wording: "Some condition of this kind is needed", with the c₀ question open; scope bullet renamed "The constants" | MADE, CORRECT |
| 8 | Proposition 7.16: proof in five steps, ψ renamed; D measurable for the completion of μ | MADE, CORRECT |
| 9 | Minor items: ∂D_K step in Proposition 7.14; citation in Lemma 7.5(d); Q ⊇ K′ in §9.3; (M3) and the one-sidedness of U; L(1) = q(1) in Lemma 7.1(c) | MADE, CORRECT |

**Verdict.** All nine required changes are made correctly. The writer's write-ups of my three examples (one-sidedness in §7.6, the norming-set example, and the relative-interior proof) are correct. No theorem, proposition or lemma statement in §7 changed, apart from the added measurability clause in Proposition 7.16, which is correct. **§7 and the infinite-world text are acceptable.** The only remaining point is the optional wording in item 6.
