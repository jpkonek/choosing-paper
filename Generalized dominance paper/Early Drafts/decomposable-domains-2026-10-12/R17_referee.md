# R17. Referee report on R14_notes.md §2 and R16_notes.md

13 October 2026. Independent referee; I wrote neither note. I read BRIEF.md, BRIEF2.md (with the 13 Oct
update), CCIBU.tex, AUDIT_ASSESSMENT.md, AUDIT_ASSESSMENT2.md, and for context R11, R13, R7, R9, plus
R2 (Fact 0) and R5 (Lemma 4.1). I re-derived each step. Verdicts: **CORRECT**, **CORRECT WITH REPAIR**
(the statement stands after a local fix, given here), **GAP** (a step is missing and not supplied here),
**FALSE** (as worded).

## 0. Verdict table

### R14 §2 (n ≥ 4)

| Item | Verdict | One-line reason |
|---|---|---|
| Lemma A0 (successive minimisation) | CORRECT | Iterated (PB); each stage is a decomposable domain |
| Lemma A1 (admissible lex sequence ⇒ unique coherent model) | CORRECT | Polynomial-sign argument, countable-union step, (IBU) at W(s_m)/\|W(s_m)\| ∈ int Δ |
| Lemma A2 (admissible W with F_W = {x}) | CORRECT | Proper separation (Rockafellar 11.3) from C₂ = {d_Z = 0, d_{Z^c} ≤ 0}; dichotomy checked |
| Termination ≤ 2n steps | CORRECT | ≤ dim R drops, ≤ n activations, and the appended u is counted (§1.3) |
| Theorem A (unique coherent realisation of efficient profiles, any n, no strict guidance) | CORRECT | A0 + A1 + A2 |
| Consequences (C), C_L = realisations of efficient profiles | CORRECT | |
| "Brief's form is too strong" example | CORRECT WITH REPAIR | Needs N_R(x) ∩ ℝⁿ₊ = ray(w). If R = F, then (w + e₁, u) works and no step lacks new weight |
| Prop B1 (Q-selection extends iff boundary fibres have least elements) | CORRECT | Both directions checked |
| B1, "for n = 3 this is automatic" | CORRECT WITH REPAIR | True on edges. At vertices Φ′_{e_i} is 2-dimensional, so a least element needs strict guidance (B3), as CCIBU uses |
| **Ex. B1′** (zonotope; Q-selection fails for n = 4) | **FALSE** as evidence for (IBU) systems | A finite-generator zonotope whose generators have mixed signs violates the *uniqueness* half of (IBU). Its realisability is not merely unchecked: it is impossible (§1.6). A zonoid repair restores the failure at the level of R. Coherence is still unchecked |
| Lemma B2 (Chebyshev: competitiveness, efficiency, localisation, uhc) | CORRECT | |
| Theorem C ((L) ⇒ continuous selection, (LA), (S), (C), any n) | CORRECT | Berge on each open face plus localisation |
| Lemma B3 (faces with constant y_j are points) | CORRECT | Iterated-exposed-face representation plus A0 and strict guidance |
| Lemma B4 | CORRECT | I is automatically non-empty and independent of the choice of m ∈ ri B(q) |
| Lemma B6 | CORRECT | Strict guidance is used only at extreme points |
| Prop B7 ((L) at vertices and on edges, any n, under strict guidance) | CORRECT (notational slip) | In the \|I\| = 1 case T is a single point, but not c_S. Read "T = {τ(q)}" |
| "Selection continuous on a neighbourhood of the 1-skeleton" | CORRECT | Follows from B2(ii) + B7. "(S) holds near the 1-skeleton" means continuity there; (S) itself is global |
| Prop B5 (R ⊂ ℝ⁴ with no (S)-selection at all) | CORRECT | Every step checked |

### R16

| Item | Verdict | One-line reason |
|---|---|---|
| **Theorem A** (face-anchored transport) | CORRECT | Steps 1–4 checked. Strict guidance of ψ on the advice ranges of 𝔇 is a fourth hypothesis, stated in the preamble |
| — (T0) | CORRECT; necessary for (LF) and for Lemma IC's model in Step 3 | |
| — (A1) | CORRECT; used only in Step 1, to place Fact 0's C in 𝔇 | |
| — (A2) | CORRECT; weak half for Step 1 (and Step 3), strict half for the tie in Step 1 | |
| Remark (i): (AR) ⇔ anchored sandwich; countability automatic | CORRECT | R13 Prop S applies verbatim to anchored pairs |
| **Theorem LV** (blind additive faces) | CORRECT | (T0), (A1), (A2) and strict guidance checked. The error-only example is an instance (I checked that N′ exists) |
| **Prop P** (Puiseux prior) | CORRECT WITH REPAIR (minor) | The normalisation must be done inductively: changing p_k also changes o_{k+1}. Also, "degree one is not enough in general" is asserted without an example |
| **Prop V** | CORRECT as two one-way statements | §0 item 3's "iff" is overstated: (ii) needs an *interior exposing* β ∈ Σ_T, not just Σ_T ∩ N(π₀) ≠ ∅ |
| **Lemma NG** | CORRECT WITH REPAIR | False as worded when the second kind of advice in the advice range is ×, since × is worst at every world. Require two kinds of advice from {+, 0, −}. Both applications satisfy this |
| **Prop J** (a), (b), (c) | CORRECT | |
| **Prop RG** (CHECKED) | CORRECT WITH REPAIR, as a conditional | (R3) must mean *full support* of the push-forward of μ under g ↦ H_g. That reading is also what makes B^lex, hence Φ, injective, which the cited local FTPG needs. "Charts are open" must be replaced by "open half-planes"; U must be connected (point case); advice ranges with 3 or 4 kinds of advice need localisation. The ψ-density half of (R3) is never used |
| RG ⇒ "R11 §5 blow-up conjecture is FALSE (as reproduction)" | GAP (overstated) | Refuting the conjecture needs an actual (LA), (S), (C) lex system in regular position satisfying (R3). The note says it has not built one. (R2)'s injectivity also excludes non-injective reproductions. Correct reading: "no injective reproduction exists in any instance satisfying (R3)" |
| **Prop 3.3** ((AA) not derivable, not necessary) | CORRECT | Checked for n = 3, including (S) for the error-only system |
| (AR) ⇒ (AA) | CORRECT | |

---

## 1. R14 §2

### 1.1 Lemma A0: CORRECT
- ∫ v¹·ℓ(g, a_X) ≥ ∫ min_{A(g)} v¹·ℓ. A measurable pointwise minimiser exists (finite advice ranges). Equality holds iff X is a pointwise minimiser a.e.
- The models whose advice lies in A^{v¹} form a decomposable domain whose attainable set is exactly F¹ = argmin_R v¹·y. Induct.
- Signs of v^r are irrelevant, as claimed.

### 1.2 Lemma A1: CORRECT
- W admissible ⇒ W(s)_j = s^{r_j−1}(w^{r_j}_j + O(s)) > 0 for small s, where r_j is the first non-zero index. So W(s)/|W(s)| ∈ int Δ.
- For a, b ∈ A(g), W(s)·(ℓ(a) − ℓ(b)) is a polynomial in s. With finitely many pairs there is s₀(g) with argmin W(s)·ℓ = A^W(g) for s < s₀(g).
- Countable union: N ⊆ ⋃_M ⋂_{m≥M} N_m. If N is non-null, some N_m is non-null. The min-index and max-index pointwise W(s_m)-minimisers (defined on all of H) are two Bayes models differing on N_m. This contradicts (IBU).
- Convergence: the unique W(s_m)-Bayes model equals B^W at g for m ≥ M(g). Hence a.e. convergence, hence convergence in measure, and the coherent class is closed.
- Strict guidance is not used. Confirmed.

### 1.3 Lemma A2 and termination: CORRECT
- C₁ ∩ ri C₂ = ∅ uses only that x is (strongly) efficient: a point there is y ∈ R with y_Z = x_Z and y_{Z^c} < x_{Z^c}, where Z^c ≠ ∅.
- Rockafellar 11.3 needs only ri C₁ ∩ ri C₂ = ∅. Since 0 ∈ C₁ ∩ C₂, both bounds are 0. Then ν_{Z^c} ≥ 0 and x ∈ argmin_{F^{k−1}} ν.
- Properness means not both sets lie in {ν = 0}. So either ν is non-constant on F^{k−1}, giving a proper face of strictly smaller dimension, or ν_{Z^c} ≠ 0, which with ν_{Z^c} ≥ 0 activates a new coordinate with positive weight. Admissibility is preserved.
- **Count.** Let a be the number of dimension drops (a ≤ dim R ≤ n) and b the number of activation-only steps.
  - Stop at Z = Ω: a + b ≤ 2n.
  - Stop at F = {x} with Z ≠ Ω: b ≤ n − 1, plus the appended u, so ≤ 2n.
  - The bound 2n is right.
- **Stop at Z = Ω.** A1 gives |A^W| = 1 a.e. A0 then makes F_W a single profile, which is x because x survives every step.
- **Theorem A.** Any realisation X of x has L(X) ∈ F_W. By A0 its advice lies in A^W, hence X = B^W a.e., which is coherent. CORRECT.
- **Consequences.**
  - (C) holds: tied ⇔ equal profile.
  - C_L = {realisations of efficient profiles}.
  - The vertex supports W = (e_i, u) are covered.
  - All correct.

### 1.4 The "brief's form is too strong" example: CORRECT WITH REPAIR
- The analysis at x = (a, ·, h(a)), with h(t) = −√(t − a), is right: no v with v₃ > 0 supports x on F.
- But if R = F, the in-plane minimising functionals at x are y₁ (plus multiples of w). So the sequence (w + e₁, u) is admissible, and both of its steps activate a new coordinate. The example therefore needs N_R(x) ∩ ℝ³₊ = ray(w), so that the first step is forced to be ∝ w.
- With that hypothesis added, every admissible sequence has a cutting step with zero weight on coordinate 3, as claimed.

### 1.5 Prop B1: CORRECT
- **Step 1.** The inequality Q_r(y_s) ≤ Q_r(z) (z ∈ Φ_p) is right. Upper hemicontinuity puts cluster points in Φ_p, and they minimise Q_r there. Q_r is strictly convex in y_{S^c} with y_S fixed, so the limit λ_r(p) is unique.
- **Step 2.**
  - Lower semicontinuity gives x(p) ≤ λ_r(p).
  - The S-coordinates: x(p)_S ≤ x*_S(p) together with monotonicity of the summands gives Q_p(x(p)) ≤ Q_p(x*). Uniqueness then gives equality, so x(p) ∈ Φ_p. The note compresses this into one sentence; it is fine.
  - For r = (1−η)e_j + ηu, λ_{r,j} → min_{Φ′_p} y_j because y_j − a_j > 0.
  - So x(p)_{S^c} is the ideal point of Φ′_p, and it lies in Φ′_p.
- **Converse.** Every x(q) lies in argmin Q_q (interior or boundary). Cluster points lie in Φ_p, hence are ≥ (x*_S, ℓ_p). The least element is efficient.
- (S) sections only at attainable levels: the attainable range of L_i is an interval, so the condition is equivalent to full lower semicontinuity.
- **Repair to the n = 3 remark.** At p = e_i, S^c has two coordinates and Φ′_{e_i} is the projection of argmin_R y_i, a planar set. It has a least element because it is a point under strict guidance (B3), which is what CCIBU uses. "Automatic" is true only at edge indices.

### 1.6 Ex. B1′: FALSE as an example relevant to (IBU) systems; repairable at the level of R

**The defect.** Under (IBU), every face of R exposed by an interior weight is a single point: two profiles in it would give two Bayes models at that weight (Lemma A0). In a zonotope R = Σ_k [0, γ_k], the face exposed by ν is Σ_{ν·γ_k = 0} [0, γ_k] + (vertex). Take δ¹ = (1, −1, 1, −2). Since δ¹ has both signs, δ¹^⊥ meets int ℝ⁴₊ in a relatively open subset of a hyperplane, e.g. ν = (1, 1.5, 1, 0.25). A generic such ν is orthogonal to no other generator. Its exposed face is a translate of [0, δ¹], which is not a point. So R violates (IBU)'s uniqueness clause.

The mixed-sign property that R14 cites as making R compatible with B3 is exactly what makes it incompatible with (IBU). Indeed δ¹ ⊥ w = (1,1,0,0) forces δ¹₁ = −δ¹₂, so δ¹ has mixed signs. The same holds for any finite-generator construction of this type. More generally, under (IBU) the normal fan of a polytopal R cannot place an edge normal cone inside int ℝⁿ₊. So polytopal attainable sets are essentially excluded. "Realising it by a field with (IBU) has not been checked" should read "is impossible".

**Repair (CHECKED at the level of R).** Replace the δ-part by a zonoid D = {∫ f(d) d dν(d) : 0 ≤ f ≤ 1} with generators d = (α, −α, β, γ):
- α > 0 and β, γ ≠ 0;
- ν has a density on a relatively open subset of w^⊥ (3-dimensional), with (β/α, γ/α) jointly non-degenerate (e.g. independent);
- the ζ-part is likewise diffuse in ℝ⁴, with all coordinates non-zero and w·ζ ≠ 0.

Then:
- **Interior-exposed faces are points.** For interior ν′, ν′ restricted to w^⊥ is non-zero (ν′ is not ∝ w), so ν′^⊥ ∩ w^⊥ is ν-null. The same holds for the ζ-part.
- **Compatible with B3.** All generator coordinates are non-zero.
- **Strict guidance signs.** Generators of every mixed sign pattern arise from problems in the corresponding orthants.
- **F_w = D + (pt).** Over y₁ = c ∈ (0, ∫α), the fibre's min-y₃ point is attained only by f = 1{β/α < λ} and its min-y₄ point only by f = 1{γ/α < λ′}. These indicators differ on a non-null set, so the fibre (a 2-dimensional convex set in (y₃, y₄)) has no least element.
- For an open arc of edge indices, x*_S(p) lies over such c, so by B1 the Q-selection fails (S).

So "the quadratic selection does not extend" survives at the level of R, for an R compatible with B3 and with the uniqueness half of (IBU). Coherence of the interior Bayes family, the other half of (IBU), is not verified for any such R. **Answer to the commission's question:** the failure of the quadratic selection for n = 4 is not established for any (IBU) system. The given example is not one. A repaired R-level example exists; its realisation is open.

### 1.7 Lemma B2: CORRECT
- **(i)** Off S the terms vanish and on S they are positive, so z_S < y_S strictly gives f_q(z) < f_q(y). Efficiency of σ: y′ ≤ σ forces y′ ∈ B(q) and ‖y′ − a‖ ≤ ‖σ − a‖, with equality only at σ. B(q) is convex, so σ is unique.
- **(ii)** On U: every S-term is ≥ (b_i/2)(min_R y_i − a_i) ≥ 2τ, and every off-S term is < τ. So f_q = |q_S|·f_{π(q)} on R. U is a neighbourhood of b because the off-S conditions hold strictly at b.
- **(iii)** Berge.
- **Note.** Near a vertex e_i, x is constant: x(q) = σ(argmin_R y_i).

### 1.8 Theorem C: CORRECT
- On relint Δ_S, B is continuous with compact convex values. Berge with a strictly convex objective makes σ∘B single-valued and upper hemicontinuous, hence continuous.
- At b, x = (x|_{relint Δ_S})∘π on U, with π continuous and π(b) = b.
- Efficiency, supp-competitiveness (B2(i)) and unique coherent realisation (Theorem A) give (LA).
- Continuous profiles give closed sections, hence (S). (C) is Theorem A.

### 1.9 Lemmas B3, B4, B6, Prop B7: CORRECT
- **B3.**
  - Every face of a compact convex set is a face of a proper exposed face: a relative-interior point of F lies in some exposed face G, so F ⊆ G. Hence F = F_V for some finite sequence V.
  - On a non-null set where |A^V| ≥ 2, the models with pointwise ℓ_j-min and ℓ_j-max advice in A^V have different L_j. All four kinds of advice have distinct world-j ranks a.e., since g_j = 0 is null.
  - The pullback to R_S is a face of R.
- **B4.**
  - I ≠ ∅ automatically, since f_q(m) = t*.
  - I is the same for every m ∈ ri B(q).
  - (ii): moving from m toward any z with z_i < m_i lowers f_q, so m_i = min_R y_i. B(q) ⊆ argmin_R y_i, which is a point by B3.
- **B6.**
  - Extreme points of R_S give singleton fibres (B3). Upper hemicontinuity at a singleton gives Hausdorff continuity.
  - At relative-interior points of an edge G: y′ = (1−t)y + t·y_e gives lower hemicontinuity uniformly in y, since |y′ − y| ≤ t·diam R.
  - Strict guidance is used only in the first case.
- **B7.**
  - On an edge, T = argmin_{R_S} f_q is a singleton: if |I| = 1, by B4(ii) applied to R_S; if |I| = 2, then T ⊆ {c_S}.
  - **Notational slip.** "T ⊆ {c_S}" and "c_S(q) ∈ Eff(R_S)" are right only in the |I| = 2 case. In general write T = {τ(q)}.
  - τ is continuous (singleton-valued and upper hemicontinuous), τ(q) ∈ Eff(R_S) (B2(i) on R_S), and B(q) = Φ(τ(q)) is continuous by B6. So (L) holds on edges. Vertices are trivial.
  - Only strict guidance at the two worlds of S is used.
- **Neighbourhood of the 1-skeleton.** For q ∈ U(b) with |supp b| ≤ 2, x = x∘π near q, and x|_{relint Δ_S} is continuous at π(q). So x is continuous on an open neighbourhood of the 1-skeleton. CORRECT. "(S) holds on a neighbourhood" should read "the selection is continuous on a neighbourhood".

### 1.10 Prop B5: CORRECT
- **R_S.** R_S = conv γ([0,1]). Its weakly efficient set is the arc: a chord point (ε, 1−ε) is beaten by γ(θ′) when 2θ′ − θ′² > ε² and θ′ < ε.
- **Fibres.** Every γ(θ) is exposed, so fibres are faces of R, equal to conv of cl K over γ(θ). That is a point for θ ≠ θ₀, and [A, B] at θ₀, since cl K adds every cluster value of σ.
- **Obstruction.**
  - Competitiveness puts x_S(p) on Γ on relint E, and pins the two vertices.
  - x₁ = φ^{−1}(x₂) is upper semicontinuous; with lower semicontinuity, x₁ is continuous on E.
  - p* exists and lies in (0,1). The attaining indices converge to p*: any cluster point p̄ ≤ p* has x₁(p̄) = θ₀, so p̄ = p*.
  - The limits (γ(θ₀), A) and (γ(θ₀), B) together with lower semicontinuity force x₃(p*), x₄(p*) ≤ 0, but x₃ + x₄ = 1 on the fibre.
- **Scope.** Correctly stated: the fibre over γ(θ₀) violates B3. The Σ_T realisability is labelled CONJECTURE.

---

## 2. R16

### 2.1 Theorem A: CORRECT

**Step 1.**
- Fact 0(a) on M (R2) gives C ∈ C_L with C ⪯_i B. (A1) puts C in 𝔇; (A2) gives ψ(C) ≤ ψ(B).
- Since w is interior, ψ(C) = ψ(B). The strict half of (A2) excludes C ≺_i B, so C ~_i B at every world.
- (C) gives B ∈ C_L.

**Step 2.** The radial splice. 𝔇 is closed under splicing, and (PB) holds on 𝔇.

**Step 3.**
- T ∈ 𝔇 by (T0). Lemma IC gives competitiveness against M ⊇ 𝔇. The contrapositive of the weak half of (A2) with C = T then excludes a coordinatewise ψ-improvement.
- Aumann convexity plus separation gives w_T ∈ Δ.
- For supp w_T = S ≠ Ω: IC's g₀ exists because K ⊆ int Δ. With V ⊆ N′ (and −V ⊆ N′ if −g₀ ∈ ∂T; otherwise −V ∩ T = ∅ after shrinking), X △ T ⊆ N′, so X ∈ 𝔇. Strict guidance on the advice ranges of 𝔇 gives ψ_i(X) < ψ_i(T) for i ∈ S.

**Step 4.**
- CCIBU needs only three worlds, strict guidance and envelopes on the advice ranges of 𝔇, and (IBU) over 𝔇 (Steps 1–2). 𝔇 is a decomposable domain, so its standing facts hold.
- CCIBU's Remark puts T, the unique w_T-Bayes model, into C_ψ.
- (LF) at T is (T0).

**The hypotheses.**
- (T0), (A1) and (A2) are exactly what is used, and each is used.
- Strict guidance of ψ on the advice ranges of 𝔇 is a fourth, independent hypothesis. It is used in Step 3 and in CCIBU.
- n = 3 enters only through CCIBU. With R14 Theorem C, the same proof runs in any n once (L) holds for ψ on 𝔇.

**Remark (i).** (AR) is (A2) with 𝔇 = M. "(AR) ⇔ anchored sandwich": ⇒ take Θ = {ψ_i}; ⇐ R13 Prop S's density argument works pair by pair, so it applies to anchored pairs, and then aggregation gives (A2). CORRECT.

### 2.2 Theorem LV: CORRECT
- **(F1) equivalence.** Min/max selections. For m = 2 and Ω_ℓ = Ω, "upper profile constant on 𝔅_τ" ⇔ F_τ = {π(T)} ⇔ τ exposes π(T). Correct.
- **(T0).**
  - Pairs where R and T differ meet N′ ∪ (−N′).
  - On those pairs, (F2) makes the advice range of 𝔇 equal to A(g), since all upper levels tie.
  - (LF) for L puts R in M.
- **(A1).** The iteration is right. Each stage uses τ^k > 0 on Ω_ℓ, and (PB) on the previous stage domain, where X attains the minimum.
- **(A2).** Equal upper profiles on 𝔇 reduce lex comparisons to L^m. For sandwiched worlds, (W) and (R) on a dense countable subfamily give the same.
- **Strict guidance on the advice ranges of 𝔇.** Composite strictness with tied upper levels.
- **Example 1 (error-only).**
  - τ = u exposes 0 ∈ 𝒫 = {(f,f,f)}.
  - T ∈ 𝔅_u, since coherent models never err on Q.
  - N′ exists: for K ⊆ int Δ, ∂T∖{0} consists of strictly mixed gambles. Its trace on the sphere is compact and disjoint from ±(closed orthant). So a conic N′ ⊆ N avoiding Q ∪ (−Q) exists, and there φ¹ ≡ 0 on A(g).

### 2.3 Prop P: CORRECT WITH (minor) REPAIR
- **Expansion and level 0.** Correct.
- **Level 1.** The identity t·φ² + μ·φ¹ ≡ c₁(g) holds pointwise on the advice ranges of 𝔅^{(2)}, not only after integration, because those advice ranges are the pointwise argmin.
- **Level k ≥ 2.** On the advice ranges of 𝔅^{(k)}, o_k = Σ_i c^{(k)}_i(φ²_i − λ_i·φ¹) + const(g), with c^{(k)} ≥ 0. Each bracket is minimised by a_X pointwise ((PB) on 𝔅_t), so X ∈ 𝔅^{(k+1)}.
- **Pointwise F-optimality.** p·Λ(g,b) − p·Λ(g,a_X) = Σ_k ε^k(o_k(b) − o_k(a_X)) ∈ ℝ[[ε]], whose first non-zero coefficient is positive.
- **Integration.** R5 Lemma 4.1 applies. The coefficients (p_i, εp_i) are finitely many elements of F, and Hahn's finite-dimensional lex basis handles infinite series coefficients.
- **Uniqueness.** Prop LX's F-clause; p_i = t_i + O(ε) > 0.
- **Repair: normalisation.** Adding βt to p_k changes o_k by βt·φ¹, which is constant on the advice ranges of 𝔅^{(k)} for k ≥ 1. But it also changes o_{k+1} by βt·φ² ≡ β(c₁ − μ·φ¹), which is *not* constant. So the sentence "can be imposed without changing any 𝔅^{(k)}" is false for a posteriori normalisation. It is correct if each p_k is normalised *before* p_{k+1} is defined, because the level-(k+1) construction works for any p_k. Alternatively, drop the normalisation: positive F-rescaling does not change the Bayes set.
- **Unsupported remark.** "A degree-one prior t + εμ is not enough in general" (§0 item 3) is asserted with no example. Note that all o_k are functionals of the 2n-vector of level differences. A finite-degree prior may well suffice; the note correctly does not claim it either way in §2.2, but the summary should not assert the negative.

### 2.4 Prop V: CORRECT (statements); summary wording repair
- **(i)** st(p) exists, since p is a finite F-vector in a field containing ℝ. Taking standard parts gives st(p) ∈ N(π₀). On 𝔅⁰, p·(S(Y) − S(T)) ≥ 0, and the infinitesimal argument gives st(p) ∈ Σ_T. Correct, with no positivity used.
- **(ii)** Correct. Interiority of β is what makes T *the* (unique) lex-Bayes model via Prop LX.
- **Repair.** These give "T ∈ lex family ⇒ Σ_T ∩ N(π₀) ≠ ∅" and "Σ_T contains an interior β exposing π₀ ⇒ T ∈ lex family". The intermediate case is undecided: Σ_T meets N(π₀) only at non-exposing or boundary β, where an F-prior β + εγ might still work. §0 item 3's "iff" must be weakened, as the status table already does.

### 2.5 Lemma NG: CORRECT WITH REPAIR
- **Defect.** On mixed g the orders are + < 0 < − < × or − < 0 < + < ×. × is worst at *every* world. If the advice range of 𝔅_t is {a_T, ×}, then a_T is world-best at all worlds and strictly guiding ψ_i are consistent with T. The claim "two distinct kinds of advice are ranked in opposite orders by some pair of worlds" fails for pairs containing ×.
- **Repair.** Assume the advice range of 𝔅_t contains, besides T's advice (never ×, since T is coherent), another kind of advice from {+, 0, −}. On {+, 0, −} the two world orders on a mixed problem are exact reverses, so the proof goes through.
- **Applications.** Both bullets satisfy the repaired hypothesis. (LF) near ∂T puts the switch of acceptance of g in the advice range, so near ∂T the advice range contains at least two of {+, 0, −}. Under blindness, ψ_i = φ²_i + const is strictly guiding on those advice ranges, so T cannot be multi-Lagrangian. That contradicts SF_n in the regular position.

### 2.6 Prop J: CORRECT
- **(a)** The gap/envelope argument: 2|w − w₀|₁H(g) < γ(g) keeps the minimiser. Pointwise a.e. uniqueness at w₀ follows from Bayes uniqueness.
- **(b)** The surjectivity argument for θ is right. θ·π_r ≤ θ·y on F_t follows from the two Bayes inequalities. Cluster points lie in argmin_{F_t} θ (respectively argmax), which are disjoint because θ is non-constant on F_t. P is continuous in measure.
- **(c)** Immediate. Φ(t) ∈ int Δ is required and is stated.

### 2.7 Prop RG: CORRECT WITH REPAIR (as a conditional theorem); its consequence is overstated

I checked the skeleton and the repairs below, with the local FTPG taken as cited.

**Step 1.**
- B^lex is continuous at p iff Z(p) is null, which is the definition of p ∉ P*.
- B^ψ is continuous (J(a)) and injective, hence an embedding on compacta. (R2) puts the image of U∖P* in B^ψ(K) with K compact, so Φ is continuous.

**Step 2.** Repair the wording. The lex accept-set is {p·Δ¹ > 0} ∪ (part of H_g), and the ψ accept-set is similar; neither is open. Use the open half-planes instead:
- Fubini on (p, g) (joint measurability is fine) gives, for a.e. g, that "lex accepts at p" ⇔ "ψ accepts at Φ(p)" for λ-a.e. p.
- Hence the open sets {p·Δ¹ > 0} ∩ Φ^{−1}(L_g^−) and {p·Δ¹ < 0} ∩ Φ^{−1}(L_g^+) are null, hence empty.
- Then Φ(H_g ∩ (U∖P*)) ⊆ L_g, exactly as argued.
- With 3 or 4 kinds of advice in the advice range, the same argument applies on the portions of H_g where exactly two kinds of advice compete. This should be said.

**(R3) must be read as full support.** The Step-2 conclusion holds only for g in a co-null set G₀ produced by Fubini. The density step needs {H_g : g ∈ G₀} to be dense. For an *arbitrary* co-null G₀ this is equivalent to the push-forward of μ under g ↦ H_g having full support on the lines meeting U. With that reading:
- every open set of lines carries positive mass;
- so any two points of U∖P* are separated by a non-null set of chart lines;
- so B^lex, and hence Φ, is injective.

**Step 3.** The cited local FTPG (Shiffman, Enseign. Math. 41 (1995)) requires an *injective* map; I could not retrieve the exact statement to confirm the attribution. Injectivity of Φ is exactly what the full-support reading supplies. The "segments into lines" form is equivalent on connected pieces: overlapping segments share infinitely many image points.

**Step 4.**
- Needs U∖{t} connected (take U a disc).
- The projective map P is a homeomorphism of ℝP², and its values near t lie in the compact K ⊂ int Δ. So P(t) ∈ K and Φ extends continuously. J(c) then gives the contradiction. Correct.

**Step 5.**
- Lines crossing ℓ form an open set of lines, and full support makes chart lines dense in it.
- π_L(H_g) and π_R(H_g) both equal L_g, so σ = π_R^{−1}π_L fixes a dense, hence (by continuity) open, set of lines. So σ = id.
- Then π_L = π_R on ℓ, and the one-sided limits coincide, contradicting the jump on G_ℓ. Correct.

**Unused hypothesis.** The ψ-density half of (R3) is never used.

**The consequence is overstated (GAP).** §0 item 4(c) and the status row say R11 §5's conjecture is "FALSE as a reproduction statement under richness". RG proves: *in any instance satisfying (R1)–(R3), there is no injective reproduction.* To make the conjecture false, an (LA), (S), (C) two-level lex system is needed with an interior target in the regular position satisfying (R3). §2.6 itself says this has not been verified. Moreover, (R2) excludes reproducing fields whose interior family is non-injective, and §0 omits (R2). Correct statement: "under (R2)–(R3) no blow-up reproduction exists; whether (R3) instances exist is open."

### 2.8 Prop 3.3: CORRECT
- In three worlds the error-only system's selection p ↦ D_p is unique and continuous at every p: a boundary tie p·g = 0 is a hyperplane in g-space, hence null.
- So (LA), (S), (C), strict (G), (IB) and (LF) on the all-model domain hold. C_L = {D_p}.
- The (AA) witnesses are right:
  - D_{p′} ≺₁ D_p by L₁;
  - X_s (D_{p′} with bad advice on s-measure of Q) has F(X_s) = s > 0, so D_p ≺₁ X_s;
  - X_s → D_{p′} in measure.
- (AR) ⇒ (AA): continuity of ψ_i in measure. Correct.
- The reduction holds because L_i itself vindicates every precise interior target. So (AA) is neither derivable nor necessary.

---

## 3. Summary of required changes

1. **R14 Ex. B1′.**
   - State that a finite-generator zonotope with mixed-sign generators violates (IBU) uniqueness.
   - Replace it by the zonoid of §1.6 (R-level failure of the Q-selection, (IBU)-uniqueness and B3 compatible).
   - Keep "coherent realisation unverified".
   - The claim "the quadratic selection fails for n ≥ 4 under (IBU)" is not established for any system.
2. **R14 B1.** "Automatic for n = 3" only at edges; at vertices it needs strict guidance.
3. **R14 B7.** Write T = {τ(q)}.
4. **R14 §2.1 example.** Add N_R(x) ∩ ℝⁿ₊ = ray(w).
5. **R16 Lemma NG.** Require a second kind of advice from {+, 0, −}.
6. **R16 Prop P.** Inductive normalisation. Delete or support "degree one not enough".
7. **R16 Prop V.** Replace "iff" in §0.
8. **R16 Prop RG.**
   - (R3) means full support of the chart-line distribution.
   - Use open half-planes.
   - U connected.
   - Localise for advice ranges with 3–4 kinds of advice.
   - Confirm the FTPG citation's injectivity hypothesis.
   - Downgrade "R11 §5 conjecture FALSE" to "no injective reproduction in (R3) instances; existence of such instances open".
