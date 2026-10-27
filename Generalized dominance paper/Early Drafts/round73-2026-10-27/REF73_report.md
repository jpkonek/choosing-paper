# REF73: referee report on PRO73 (§§1, 2, 5, 6) and MU73 (§§2.3–2.5)

27 Oct 2026. Hand proofs, plus one small script: `ref73_py/check.py`. Labels: PROVED / CHECKED / WRONG / UNCLEAR. "Fixed" means the statement is right but the written argument has a gap, and the repair is given below.

## Verdicts

| # | Claim | Verdict |
|---|---|---|
| 1a | PRO73 Lemma LT (local exact triples, Gaussian on Rⁿ, n ≥ 2, non-collinear x, y) | **CHECKED.** The construction and both Jacobian identities are right. An independent numerical check, n = 3 sum, has error 4·10⁻¹⁰. |
| 1b | PRO73 Lemma D (density lemma) | **PROVED.** |
| 1c | PRO73 Theorem S | **PROVED after one fix.** Claim 2 ("perturb collinear x, y to x + δ, y − δ") fails when y = −x. That case needs a separate two-line argument (§1.3). |
| 1d | PRO73 "C3.7(ii) complete" | **PROVED**, for Gaussian μ on Rⁿ with exact triples. |
| 2a | PRO73 Theorem D, steps 1–4 and 6 | **PROVED.** |
| 2b | PRO73 Theorem D, step 5 | **Conclusion right; justification WRONG as written; fixed.** "X′ agrees with X near w and d" is false in general: T and S are arbitrary measurable bijections, so the restricted G₂, G₃ can sit anywhere. The repair (§2.2) uses only facts already in the proof. X′ is a legitimate consolidation (CHECKED). |
| 2c | "Within 𝓡, (CA) implies (C3)" | **PROVED.** |
| 3a | PRO73 Proposition GC: R_GC is in 𝓡, transitive, satisfies (CA), (G) | **PROVED.** |
| 3b | GC protection of every coherent model, two worlds | **PROVED.** The coefficients are right for 0 < a ≤ b < 1. The edge cases are right in substance, but the printed formulas contain 1/a and 1/(1 − b), which are undefined at a = 0 and b = 1. A single formula with no edge cases is given in §3.2. Q = S really does need the two-case argument. |
| 4a | MU73 C3m definition, chain-union preservation | **CHECKED.** |
| 4b | MU73 Lemma W (witness characterisation; general Ω, separable E, (M2) + (M3)) | **PROVED.** |
| 4c | MU73 Lemma T (margin triples exist for atomless μ whenever W_c is non-null) | **PROVED.** |
| 4d | MU73 C3.7(ii) for C3m | **PROVED.** Only (G) and C3m are used; (SC) is not needed. With atoms, the G_i must avoid the atoms (one line). |
| 4e | R0 (Def. 6.1) satisfies C3m; so does veto–Brier on U | **PROVED.** In fact R0 satisfies more: every margin consolidation is accepted at every world (§4.4). |
| 4f | R_{s'} violates C3m (MU73 §2.5(i)) | **CHECKED** (increments recomputed by hand: −δ / +1.5 − δ/2 for c = 1, −2δ / +1.5 − δ for c = 2). |
| 4g | MU73 §2.3 aside: "C3p strict contains C3m" | **UNCLEAR as stated** for uncountable Ω, and irrelevant. With "≥" it is CHECKED for countable Ω (§4.1). |

**New result (§5, PROVED by the referee, not yet refereed).** PRO73's Theorem D carries over to the margin form in the paper's general setting:
- **Hypotheses.** (G) + (SC) + (CAm) + (TT), with (M2), (M3) and μ atomless. Here (CAm) means: the consolidation by a margin triple is at least as good at every world.
- **Conclusion.** Every incoherent model is dominated.
- **What it avoids.** Density points, Gaussian structure, and exact triples.
- **Nonempty for every Ω.** R0 belongs to this class. It satisfies (TT) vacuously, because it has no ties between distinct models. So the nonemptiness question of PRO73 item 11 disappears for the margin form.
- **Contrast with exact (CA).** R0 does not satisfy PRO73's exact (CA), because an exact consolidation leaves m unchanged and R0 refuses it.

---

## 1. PRO73 §1–2: Lemma LT, Lemma D, Theorem S

### 1.1 Lemma LT: CHECKED

Write μ = γ_P ⊗ γ_⊥.

**T preserves μ.** T acts on P by (r, φ) ↦ (τ(r), φ + θ(r, h_⊥)) and is the identity on h_⊥. Its Jacobian is block-triangular, with determinant ττ′/r. The condition ρ(Th)|det DT| = ρ(h) reduces to ττ′e^{−τ²/2} = re^{−r²/2}. Integrating gives e^{−τ²/2} = e^{−r²/2} + C. τ does not depend on h_⊥, so letting θ depend on h_⊥ is harmless. ✓

**Sum case.**
- Rotation-equivariance of T_P gives h_P + T_P(h_P) = e^{iφ}(r + τe^{iθ}). So S_P(r, φ) = (σ(r), φ + β(r)) with σ = |r + τe^{iθ}|.
- S(h) = (S_P, 2h_⊥) has Jacobian determinant 2^m σσ′/r.
- The identity ρ(Sh)|det DS| = ρ(h) becomes σσ′e^{−σ²/2} = 2^{−m}e^{3|h_⊥|²/2} re^{−r²/2}. This gives the stated λ. ✓

**Midpoint case.** S_*(μ|G₁) = ½μ|G₃ means μ(S(A)) = 2μ(A). With S_⊥ = id, this gives λ = 2. ✓

**θ is explicit.** cos θ = (σ² − r² − τ²)/(2rτ). It is smooth near r₀ exactly when |x|, |y| and |s| form a strict triangle. Choose the sign of θ so that T(x) = y.

**Injectivity.** τ is strictly increasing, and the map is a rotation on each circle (S also scales h_⊥). ✓

**Independent check.** `ref73_py/check.py` builds the n = 3 sum construction from scratch. T(x) = y and S(x) = x + y hold exactly. The maximum error of the two Jacobian identities over 200 points is 3.6·10⁻¹⁰.

### 1.2 Lemma D: PROVED

The midpoint factor is harmless: μ(B ∩ S⁻¹X) = ½μ(S(B) ∩ X) ≤ μ(B(s, Lr) ∩ X). Gaussian density points are Lebesgue density points, since the density is bounded above and below on compact sets. The restriction of an exact triple is again an exact triple. ✓

### 1.3 Theorem S: PROVED, after one fix

**Claim 1 is correct.**
- For sums, y′ = s′ − x′ ranges over a ball of radius r inside B(y, 2r). For midpoints it lies inside B(y, 3r).
- So the fraction of good x′ tends to 1, uniformly in s′.
- Pairs with x′ collinear with s′ form a null set. Here s′ ≠ 0 for small r, because s ≠ 0 by non-collinearity.

**Gap in Claim 2.** Take collinear x, y ∈ K. The perturbed pair x + δ, y − δ is non-collinear for generic δ, except when y = −x. Then x + δ and −(x + δ) are always collinear, and the sum and the midpoint are both 0. Without this case, midpoint-convexity and so Claim 3 are not established. For example, x, −x ∈ K would put 0 ∈ K.

**Fix.** K never contains both x and −x.
- Suppose it does. Pick d ∈ D_S not in span(x); this is possible because n ≥ 2 and D_S is open.
- For small ε, u = x + εd and v = −x − 2εd lie in K, because K is open.
- They are non-collinear. If a(x + εd) = x + 2εd, then a = 1 and a = 2.
- Claim 1 (sum) gives u + v = −εd ∈ K, contradicting K ∩ (−D_S) = ∅.

So every collinear pair in K has x + y ≠ 0, and the perturbation argument applies.

**The rest is correct.**
- Claim 3: open and midpoint-convex implies convex; tx for t ≥ 1 by sums and convexity; tx for t < 1 by the stated trick; and 0 ∉ K.
- Claim 4: X̃ ⊆ cl K via x + εd, and ∂K is Lebesgue-null.
- Conclusion: Lemma `lem:identify`(b), then (M2).

### 1.4 C3.7(ii) "complete": PROVED (Gaussian on Rⁿ, exact C3)

The guided rival gives Y ≻_ω X at every ω, which already contradicts a defence X ≻_ω Y; (SC) is not needed. Theorem S does the rest.

---

## 2. PRO73 §5: Theorem D

### 2.1 Steps 1–4 and 6: PROVED

- **Step 2.** (TT) gives Y ⪰ X. At the world where Y ≻ Z, the comparison X ⪰ Y would give the chain Z ⪰ X ⪰ Y together with Y ≻ Z, which (SC) forbids. ✓
- **Step 3.** (CA), undominatedness, and step 2. ✓
- **Step 4.** The consolidated model misses G₂ ⊆ D_S, which is non-null. So it is dominated by step 1, contradicting step 3. ✓
- **Step 6.** Theorem S. ✓

### 2.2 Step 5: conclusion right, justification wrong as written

**Legitimacy of the restricted triple: CHECKED.**
- Restrict G₁ to G₁^ρ = G₁ ∩ B(x₀, ρ), and put G₂^ρ = T(G₁^ρ) and G₃^ρ = S(G₁^ρ).
- For A ⊆ G₁, T_*(μ|G₁)(T(A)) = μ(A), because T is a bijection. So the pushforward identities restrict. The same holds for S.
- This needs T(A) to be measurable. That is automatic for Borel bijections between Borel sets (Lusin–Souslin), and the definition of a matched triple should say "bimeasurable".
- G₁^ρ ∪ G₂^ρ ⊆ X and G₃^ρ ∩ X is null. So X′ is a consolidation of X. ✓

**What is wrong.** "w and d = z − w are density points of X′, since X′ agrees with X near them."
- T and S are arbitrary measurable bijections. So G₂^ρ ⊆ X and G₃^ρ can lie in any neighbourhood of w or of d.
- Example: G₂^ρ may be a small set of positive density at d. Then d is not a density point of X′.
- "w a density point of X" is also not enough: w could be a density point of G₂^ρ.

**Repair.**
1. *z = x₀ is a density point of E∖X′.*
   - For ε < ρ, X′ ∩ B(x₀, ε) ⊆ (X∖G₁) ∪ G₃^ρ, and both sets are disjoint from G₁.
   - x₀ is a density point of G₁, so X′ has density 0 at x₀. ✓
   - The original sentence states this correctly, but gives no reason for it.
2. *Choose w as a density point of G₁, not of X,* with 3ρ < |w − x₀| < 5ρ, x₀ − w ∈ D_S, and w not collinear with x₀.
   - The set {w : 3ρ < |w − x₀| < 5ρ, x₀ − w ∈ D_S} is a fixed fraction of B(x₀, 5ρ).
   - G₁ has density 1 at x₀, so for small ρ a positive-measure set of such w lies in G₁.
   - Since G₁∖B(x₀, ρ) ⊆ X′ (G₁ is disjoint from G₂ ⊇ G₂^ρ and from G₃), w is a density point of X′.
3. *d = x₀ − w ∈ D_S is a density point of X′,* because X′ is undominated (step 3), hence contains D_S a.e. (step 1), and D_S is open.
4. *w and d are non-collinear,* since w is not collinear with z = w + d. Lemma D then gives a sum triple for X′ with G₂ ⊆ B(d, Lr) ⊆ D_S, and step 4 applies. ✓

With this repair, Theorem D is **PROVED** (Gaussian μ on Rⁿ, exact triples).

### 2.3 Remarks: PROVED

- **(CA) implies (C3) within 𝓡.** Suppose Z ⪰ … ⪰ Z′ with a strict link X_i ≻ X_{i+1}. Close the cycle with Z′ ⪰ Z, from (CA), and start it at X_{i+1}. This is a chain from X_{i+1} to X_i with X_i ≻ X_{i+1}, which (SC) forbids. ✓ The same argument shows that (CAm) implies (C3m).
- **Closure under ties.** It follows from step 2 and Theorem D. ✓
- **Item 9's implications.** Completeness and (SC) give transitivity. Completeness and (C3) give (CA). ✓
- **Not refereed:** item 9's "CHECKED" score computation, items 4, 5 and 8, and the open items 10 and 11.

---

## 3. PRO73 §6: Proposition GC (two worlds)

### 3.1 Membership, transitivity, (CA), (G): PROVED

- **(R), (I).** The verdict depends only on (1_A − 1_B)μ. ✓
- **Transitivity.** cone_ω is closed under addition. Transitivity gives (SC) and (TT). ✓
- **(CA).** It holds by definition. ✓
- **(G).**
  - Each generator has ∫h_ω dν ≥ 0.
  - Consolidation generators give exactly 0:
    - sums: ∫_{G₁}[S(h) − h − T(h)]_ω dμ = 0;
    - midpoints: ∫_{G₃}h_ω dμ = 2∫_{G₁}S(h)_ω dμ = ∫_{G₁}h_ω dμ + ∫_{G₂}h_ω dμ.
  - The reverse of a non-null guided change has ∫h_ω dν < 0, because μ{h_ω = 0} = 0. ✓

### 3.2 Protection: PROVED. Simpler coefficients

**Positivity on cone_ω.** f_ω(t) = min(c₊t, c₋t) with c₋ ≥ c₊ ≥ 0 is concave and positively homogeneous, hence superadditive and midpoint-concave (2f((a + b)/2) ≥ f(a) + f(b)). So ∫f_ω(h_ω)dν ≥ 0 on each generator of cone_ω. A weak dominator gives one decomposition per world. Adding the two inequalities gives ∫F dν ≥ 0, which is legitimate. ✓

**Coefficients for 0 < a ≤ b < 1.** In the mixed quadrant (h₁ > 0, h₂ < 0), min_t [th₁ + (1 − t)h₂] is attained at t = a. In the other mixed quadrant it is attained at t = b. PRO73's coefficients give sign(F) = sign(ah₁ + (1 − a)h₂) and sign(F) = sign(bh₁ + (1 − b)h₂) respectively. The constraints c₋ ≥ c₊ reduce to (1 − b)/b ≤ s ≤ (1 − a)/a. ✓

**Edge cases.** As printed, c₋² = (1 − a)/a and c₋¹ = sb/(1 − b) are undefined at a = 0 and b = 1. The remark "the corresponding c₊ is 0" is right after rescaling: for a = 0 take c₊¹ = 0, and for b = 1 take c₊² = 0. I checked both by hand.

**Cleaner choice (suggested replacement).** Use one formula for every Q ≠ S:

  F(h) = a·h₁⁺ − b·h₁⁻ + (1 − b)·h₂⁺ − (1 − a)·h₂⁻.

- The constraints hold automatically: b ≥ a at world 1, and 1 − a ≥ 1 − b at world 2.
- Signs by quadrant:
  - both positive: F > 0 unless (a, b) = (0, 1);
  - both negative: F < 0;
  - h₁ > 0 > h₂: sign(ah₁ + (1 − a)h₂);
  - h₁ < 0 < h₂: sign(bh₁ + (1 − b)h₂).
- So {F > 0} = D_Q and {F < 0} = E∖cl D_Q, up to null rays.
- NUMERICS: 0 sign mismatches over 27 credal sets (including a = 0, b = 1, a = b, and a = b ∈ {0, 1}) at 4·10⁵ Gaussian points.
- This F is MU73's loss-averse form (a_ω ≤ b_ω), which is a nice link between the two reports.

**Q = S.** Here F ≡ 0 on D_S (numerically confirmed), so no single separable F separates D_S. PRO73's two cases are correct:
- if A is non-null, use F = −Σh_ω⁻;
- otherwise, use F = h₁ on ν = −1_Bμ. ✓

**Weak dominators.** A weak dominator Y gives ∫F dν = ∫_A F − ∫_B F < 0 whenever Y ≠ D_Q a.e. So Y = D_Q. ✓

**Not refereed:** item 11 (n ≥ 3). A separable F has a Bayes set D_Q only for "box" credal sets, so the difficulty is real for exact (CA). For the margin form it disappears (§5).

---

## 4. MU73 §§2.3–2.5

### 4.1 Definitions: CHECKED

- **C3m.** The definition is clear.
- **Chain unions.**
  - A forbidden chain has finitely many links, so all of them lie in one stage.
  - A link that is strict in the union is strict in that stage too, because the reverse is absent from the union.
- **The C3p aside.** The margin condition is required μ⊗³-a.e. on the product, but a pairing graph is μ⊗³-null. So "any isomorphisms pair a margin triple" does not follow directly.
  - For countable Ω the weak form holds: per world, ess inf_{G₃} z(ω) ≥ (ess sup_{G₁} x(ω) + ess sup_{G₂} y(ω))/c, so S(h) ≥ (h + T(h))/c a.e. along any pairing.
  - So "C3p(≥) implies C3m" is CHECKED for countable Ω and UNCLEAR for uncountable Ω.
  - Nothing else depends on this aside. Drop it from the paper.

### 4.2 Lemma W: PROVED

**(⇒).** By superadditivity, P_Q(z) ≥ P_Q((x + y)/c) + P_S(z − (x + y)/c) > 0. ✓

**(⇐), step by step.**
- **Step 1.** Lindelöf applies to the open set V in a separable metric space.
  - Take z ∈ supp(μ|(U_k∖X)) ∩ (U_k∖X); such z exist for a.e. point of U_k∖X.
  - With 3δ = inf(z − (x_k + y_k)/c), balls of radius δ/2 keep a margin of at least 1.5δ.
  - μ(X ∩ B(x_k)), μ(X ∩ B(y_k)) and μ(B(z)∖X) are all positive. ✓
- **Step 2.** x ∈ cl(x + D_S). ✓
- **Step 3.** For v ∈ V and a ball B about v, B ∩ V is open and nonempty, so it has positive measure by (M3), and it lies in X a.e. So v ∈ X⁺.
  - D_S ⊆ V: take x = y = d − ε𝟙 with c = 2. ✓
- **Step 4.** λv = λ(v − η𝟙) + (1 − λ)ε𝟙 with ε = λη/(1 − λ). ✓
- **Step 5.** {sup h < 0} is open in the sup norm. ✓
- **Step 6.** cl V ⊆ C_K and D_K ⊆ V, so cl V∖V ⊆ {P_K = 0}, which is null by (M2). ✓

### 4.3 Lemma T and the C3m theorem: PROVED

**Lemma T.**
- Sup-norm balls of radius δ/8 have diameter δ/4.
- The margin is at least δ − (δ/4)(1 + 2/c), which is δ/4 for c = 1 and δ/2 for c = 2.
- Fubini gives the three positive masses.
- Sierpiński's theorem (μ atomless) gives masses m, m and cm. Disjointness of G₁ and G₂ is secured by m ≤ ½ min μ(X ∩ B_i).
- The margin then holds for every triple, not just almost every. ✓

**C3.7(ii) for C3m.**
- Step 1 does not need (SC): Y ≻_ω X at every ω already contradicts any X ≻_ω Y.
- Step 2 combines Lemma W, Lemma T and a single-link application of C3m. ✓

**Atoms (§1.2).** By (M2), atoms lie in D_S ∪ {sup h < 0}. If inf a ≤ 0 ≤ sup a, some state q has q(a) = 0, by connectedness of S. So X agrees with every coherent model on atoms. One addition is needed: the G_i must be taken in the complement of the countable set of atoms, so that μ-masses equal μ_c-masses. ✓

### 4.4 R0 and veto–Brier satisfy C3m: PROVED

**The coupling π.** π = (μ|G₁ ⊗ μ|G₂ ⊗ μ|G₃)/(cm²) has total mass m and marginals μ|G₁, μ|G₂ and μ|G₃/c. ✓

**R0.** m_ω(Z′) − m_ω(Z) = c∫[z − (x + y)/c](ω) dπ > 0 at every ω. Along any chain in R0, m_ω is non-increasing, and strictly decreasing at every non-null step. ✓

**Veto–Brier.**
- v_i ≥ 0 and cz ≥ x + y give c[−v_i·z]⁺ ≤ [−v_i·x]⁺ + [−v_i·y]⁺. So a_i does not rise.
- b_i strictly falls.
- Each world's order is a total preorder, so no strict chain returns from Z′ up to Z. ✓

**Stronger: R0 satisfies (CAm).**
- The consolidation change removes B = G₁ ∪ G₂ and adds G₃.
- For a.e. z ∈ G₃, take a margin partner pair (x, y) at which P_{Q_B}(x) > 0 and P_{Q_B}(y) > 0. Lemma `lem:hull`(b) and (M2) make this hold for a.e. x and a.e. y in B.
- Superadditivity and monotonicity give P_{Q_B}(z) ≥ (P_{Q_B}(x) + P_{Q_B}(y))/c > 0.
- So G₃ ⊆ hull(B) a.e., and by Lemma `lem:test` no coherent model could make the change.
- Its m-increment is positive at every world. So clause (ii) of Def. 6.1 accepts it at every world. ✓

---

## 5. Nearby result: Theorem D in the margin form, general setting (PROVED by the referee; needs refereeing)

**Theorem D_m.**
- **Setting.** Ω arbitrary, E separable, (M2) and (M3), μ atomless. With atoms, assume instead that the atomless part has full support, as in §4.3.
- **Axioms.** Let the ranking satisfy (G), (SC), (TT) and
  - **(CAm)** for every margin triple, every Z ⊇ G₁ ∪ G₂ with Z ∩ G₃ null, and every ω, Z′ ⪰_ω Z.
- **Conclusion.** Every incoherent model is dominated.

*Proof.* Let X be undominated. PRO73 steps 1–3 hold verbatim, since they use no geometry:
- X ⊇ D_S a.e. and X ∩ {sup h < 0} is null;
- every margin consolidation of X is undominated.

1. **Lemma U.** If X is undominated, there are no x ∈ X⁺ and z ∈ (E∖X)⁺ with z − x ∈ D_S.
   - Otherwise put d = (z − x)/2, so inf d = 2δ > 0.
   - Take sup-norm balls of radius ρ < δ/2 about x, d and z. Then μ(X ∩ B(x)) > 0 by definition of X⁺. Also μ(X ∩ B(d)) > 0, because B(d) ⊆ D_S ⊆ X a.e. and (M3) holds. Finally μ(B(z)∖X) > 0.
   - The margin is inf(z′ − x′ − d′) ≥ 2δ − 3ρ > 0.
   - Sierpiński gives a sum margin triple with G₂ ⊆ D_S.
   - Its consolidation is undominated (step 3) but misses a non-null part of D_S, so it is dominated (step 1). Contradiction.
   - **Consequence:** X⁺ + D_S ⊆ X a.e.
2. **Choosing a triple.** Suppose X is incoherent.
   - Lemma W gives c and a point (x₀, y₀, z₀) with x₀, y₀ ∈ X⁺, z₀ ∈ (E∖X)⁺ and z₀ − (x₀ + y₀)/c ∈ D_S.
   - Fix a small η > 0 and put x₁ = x₀ + η𝟙.
   - By step 1, x₀ + D_S ⊆ X a.e.; with (M3), this gives x₁ ∈ X⁺. The margin survives if η is small.
   - Build a margin triple with G₁ ⊆ X ∩ B(x₁, ρ), G₂ ⊆ X ∩ B(y₀, ρ) and G₃ ⊆ B(z₀, ρ)∖X, with ρ ≪ η.
   - Its consolidation X′ is undominated (step 3).
3. **Finding a bad pair for X′.**
   - Pick t ∈ (η/8, η/2) with ‖x₀ + t𝟙 − y₀‖ > 2ρ. The excluded t form an interval of length at most 4ρ. Put x = x₀ + t𝟙.
   - A small neighbourhood of x lies in x₀ + D_S. It avoids G₁ (distance at least η/2 − ρ) and G₂. So it lies in X′ a.e. and has positive measure by (M3). Hence x ∈ X′⁺.
   - Any z ∈ supp(μ|G₁) lies in (E∖X′)⁺, because G₁ ∩ X′ = ∅.
   - Then inf(z − x) ≥ η − t − ρ > 0. This contradicts step 1 applied to the undominated X′. ∎

**Nonemptiness.**
- R0 ∈ 𝓡 satisfies (CAm) (§4.4).
- R0 satisfies (TT) vacuously: distinct models are never tied (Prop. `prop:structure`(b)), so Z ~ X means Z = X a.e.
- Veto–Brier on U satisfies (CAm) and (TT) (total preorders, Z′ strictly better), for consolidations inside U.
- A score-free witness: R_GC rebuilt with margin consolidation generators is also in 𝓡 for two worlds, with any μ satisfying (M1) and (M2). Margin generators have ∫h_ω dν > 0, and f_ω is non-decreasing, so c·f(z_ω) ≥ f(x_ω + y_ω) ≥ f(x_ω) + f(y_ω). The protection proof of §3.2 is unchanged.

**What this means for the programme.**
- PRO73's recommendation, (CA) + (TT) in place of maximality, works better in the margin form:
  - it holds in the paper's general setting;
  - it is satisfied by the manuscript's own ranking for every Ω;
  - it needs no Gaussian or exact-triple machinery.
- Exact (CA) excludes R0. An exact consolidation leaves m unchanged, so R0 refuses it.
- **Recommendation.** State the dominance theorem with (CAm) + (TT).
- The maximality question (PRO73 item 10) is untouched.

## Corrections to carry into the round summary

1. **Theorem S, Claim 2.** Add the antipodal case (§1.3).
2. **Theorem D, step 5.**
   - Choose w as a density point of G₁, not of X.
   - Justify the density at d by "X′ is undominated, so X′ ⊇ D_S".
   - Justify the density at z by "disjointness from G₁".
   - Add "bimeasurable" to the definition of a matched triple.
3. **GC.** Replace the coefficients by F = a h₁⁺ − b h₁⁻ + (1 − b)h₂⁺ − (1 − a)h₂⁻, and keep the two-case argument for Q = S.
4. **MU73.** Drop or qualify the "C3p strict contains C3m" aside. Note that atoms must be excluded from the G_i.
5. **Adopt Theorem D_m (§5)** after it is refereed.

## Files

- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/REF73_report.md`
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/ref73_py/check.py`: sign check of the unified GC functional against D_Q, and an independent n = 3 check of LT for sums.
