# Referee report on F1_notes.md and F2_notes.md

15 Oct 2026. Adversarial reading against D2_notes, D2_referee, D2_referee2, E1_notes, C2_notes §1, B3_notes and
B3_referee, and the write-up §§2–3, §7.7 and §8.5 (Def. addup, part (c) preamble, Thm S22, Cor MC, Cor SR, Prop MP♯,
Prop lattice, Thm D21, Prop D2sigma, Conj sigmaB). The quoted round-report lines were checked in the project doc
`coverage-on-decomposable-domains-round-report`.

Scripts:
- All five author scripts were rerun with `python3 -I` (`f1py/geometry.py`, `rounding.py`, `d2prime_cell.py`;
  `f2py/f2_d2_geometry.py`, `f2_ends_T1.py`). Each output is byte-identical to the stored `.out`. The reruns are in
  `f12ref_py/*.rerun`.
- My independent check is `f12ref_py/ref_geometry.py` (output in `.out`).

No verdict rests on numerics.

## 0. Verdicts

| Item | Verdict |
|---|---|
| F1 (A): geometry of D2's far end (two rays; R₊(1,0) interior to U, R₊(−α′,1−α′) on ∂U); 1/(1−x) not locally integrable on U | **CORRECT** |
| F1 §2.1: readings (E1), (E2) have property (R); (E4) trivialises conj:sigmaB via \|h\|^{−2} | **CORRECT** |
| Theorem F1.2 (chain monotonicity of σ-finite endorsers next to an additive world) | **CORRECT** |
| Theorem F1.3 (D2: σ-finite endorsers are φ(x)λ with ∫^1 φ = ∞; none finite on compact subsets of U; non-σ-finite endorsers exist) | **CORRECT** |
| conj:sigmaB is false as written (n = 2, D2) | **CORRECT**. F1.3 and F2.4 agree; F1.3 is the more general of the two |
| Prop. F2.4 (the same refutation by a D2-specific route) | **CORRECT** |
| Theorem F1.4, Corollary F1.5 | **CORRECT**. The last sentence of F1.5 is a necessary condition only (§3) |
| Lemma F1.5′ (design for D2′) | **CORRECT** |
| Lemmas F1.6a, F1.6b, Theorem F1.6 (D2′_A and D2′_B are full systems; world 1 fails SP^reg, type (M2)) | **CORRECT**. One wording point (§4.4) |
| Lemma F1.7 | **CORRECT**. One parenthetical claim is unproved (§4.5) |
| Theorem F1.8 (blow-up exactly at the chain's far end; D2′_A has no endorser finite on compact subsets of U; D2′_B satisfies conj:sigmaB) | **CORRECT** |
| Remark F1.9 ("any endorser under (R) finite on K_η violates the certificate") | **GAP (fixable)**: it cites F1.2(a), which needs σ-finiteness. The fix is in §4.6 |
| F1 §5 (equivalence; impossibility in the D2 architecture; Conj. F1.C, F1.C′) | **CORRECT** as labelled. A caution on the evidence for F1.C′ is in §4.7 |
| F2 §1.1 (definitions; base = eventually 0 at every end) | **CORRECT** |
| F2 table, rows E1.1, E1.2, E1.3(b), E1.4, E1.5, E1.5-scope, E1.6, §2.4 | **CORRECT** |
| F2 row E1.3(a), "integrability relaxed to a.e. finiteness"; same hypothesis in F2.2 and F2.3 | **GAP (fixable)**: the relaxation fails under the total-cost reading (§5.2) |
| F2 "E1 location claim WRONG / unproved" | **CORRECT** in substance. "Unproved, and the proved constraint admits ∂U" is the accurate wording (§5.3) |
| Props F2.1, F2.2, Cor. F2.3 (where ends can sit) | **CORRECT**, subject to the §5.2 caveat. F2.2 imports Hausdorff convergence (R1 Prop 3.1): CHECKED, not re-proved |
| F2 §2 (E1.4 and E1.5 at ∂U) | **CORRECT** |
| F2 §3 (B3) | **CORRECT** (consistent with B3_referee) |
| F2 §4.1, one-sentence statements | Starthere sentence, σ-finite sentence and exclusions sentence: **CORRECT**. Ends sentence: **GAP** (missing hypotheses). B3 sentence: **GAP** (one-directional). See §5.6 |
| F2 §4.2 | **CORRECT** |
| F2 §4.3, open route | **GAP**: item 5 is attributed to "world i", but E1.1 gives an unendorsed comparison at *some* world, and under (H_U) this is automatic (§5.7). (R-a), (R-b) and the nearby conjecture: **CORRECT** as labelled |

Net assessment:
- Nothing is WRONG at theorem level.
- The refutation of conj:sigmaB is solid. Two independent routes give it (F1.2 + F1.1(c); F2.4 (A)–(E)), and I re-derive it a third way analytically in §1.
- The D2′ systems re-derive axiom by axiom.

## 1. Priority 1: claim (A) and the geometry (CORRECT)

**Error sets from the C2.1 parametrisation.**
- On M⁻ (h₁ < 0 < h₂), m_t·h increases in t, so h ∈ D_{[l,r]} iff T(h) < l. A world-1 error there is an acceptance.
- On M⁺ (h₁ > 0 > h₂), m_t·h decreases in t, so h ∈ D_{[l,r]} iff T(h) > r. A world-1 error there is a rejection.
- Hence E₁ ∩ M = {M⁻ : T < l} ∪ {M⁺ : T ≤ r}. This agrees with write-up Prop. lattice (σ = T on M⁻, τ = T on M⁺).
- With K_s = [α′s, β′+(1−β′)s], the last points to enter E₁ are T ↑ 1 on M⁺ (direction (1,0)) and T ↑ α′ on M⁻ (the
  ray (1−α′)h₁ + α′h₂ = 0, i.e. R₊(−α′, 1−α′)).
- P_{K′}(1,0) = 1 − β′ > 0, so R₊(1,0) is interior to U. P_{K′}(−α′, 1−α′) = (1−α′)(−α′) + α′(1−α′) = 0, so the
  second ray lies on ∂U.

`ref_geometry.py` (1)–(2) checks this by brute force: 31 626 mixed samples, 0 mismatches between "world-1 error of
D_{K_s}" and {x_A ≤ s}, and x_A → 1 at both rays.

**Rate.**
- T′(θ) = (cos θ − sin θ)^{−2}, which equals 1 at θ = 0, so 1 − T ≈ |θ| on M⁺.
- The uniform coordinate is x = G(x_A) with G′(1) = [(1−β′)/T′(0) + α′/T′(θ_α)]/|M|_ang.
- Hence (1−x)/|θ| → G′(1)/(1−β′). For α′ = 0.3 and β′ = 0.6 this is **2.3095**, which matches F1's numerical value 2.309.
- The near-unanimous share of the levels x → 1 is (1−β′)/T′(0) divided by the bracket: **0.4361**, which matches F2's 0.437.

So ∫ dθ/|θ| = ∞ on every K_η, and Lemma F1.1(c)(d) is right. The density bound in F1.1(c) is correct: the angle is
uniform and independent of the radius under λ, dx/dθ ≤ D, and T′ ∈ [1/2, 1] on the closed arcs.

Host B's far end is ∂U only. On M⁺ the raw coordinate is below ½, so x < λ(M⁺) < 1 there (`ref_geometry.py` (6)).

The write-up sentence "blows up only as x→1, that is, near the boundary ray of U on the side of e₂, and is bounded on
every closed subcone of U" (status of conj:sigmaB, and D2_referee2 §3.3) is **false**, exactly as both notes say.

## 2. Priority 2: F1.2, F1.3, (R), F2.4

### 2.1 Readings (CORRECT)

- (E1) has (R) trivially.
- (E2) has (R) by the displayed decomposition.
- "∫δ dν ≥ 0 whenever defined" also has (R): if ν(E₁X) < ∞ then ν(δ⁺) < ∞, the integral is defined, and it gives
  ν(δ⁻) ≤ ν(δ⁺).
- (E4) trivialises the conjecture:
  - E₁B is a cone for coherent B.
  - Under ρ = |h|^{−2}, a non-null cone has mass ∫₀^∞ r^{−1}e^{−r²/2} dr · (angle) = ∞.
  - 0 ∉ U, so ρ is locally integrable on U.
  - So every constraint under (E4) is vacuous or trivial.

The reading of conj:sigmaB is (E1), the reading of Prop. D2sigma, so the refutation applies to the conjecture as
intended.

### 2.2 Theorem F1.2 (CORRECT)

- **Inputs.**
  - (Nest) by Cor. MC(a). World 2 is additive with integrable density, so (MC) holds.
  - The chain c_b with μ(c_b) = bμ(M), from write-up part (c).
  - A coordinate x with c_b = {x < b} mod null. Put x := inf{b ∈ ℚ : h ∈ c_b}. Then {x < b} = ⋃_{b′<b} c_{b′} ⊆ c_b
    with equal mass.
  - (K) for every regular model (Lemma N0).
- **(a)** The construction is valid. P′_n ∪ Q has finite ν-mass because ρ ≤ n there. (K) applies because
  ν₂(Q) > ν₂(c_b ∖ P′_n). Then (R) applies. It needs ν₂(d_b) > 0, i.e. b < 1. ✓
- **(b)**
  - Non-atomicity gives P ⊆ A and Q ⊆ B with ν₂(Q) = (1+ε)ν₂(P) (shrink P first).
  - ν(E₁X) ≤ ν(c_b) + c₁ν₂(Q) < ∞, and finite subtraction gives ν(P) ≤ ν(Q).
  - This contradicts c₂ν₂(P) < ν(P) and ν(Q) ≤ c₁(1+ε)ν₂(P) < c₂ν₂(P). ✓
  - Passing from "ess sup_{c_b} ≤ F(b) := ess inf_{d_b}" at rational b to ρ = F(x⁺) a.e. is correct: F has countably
    many jumps, and x_*λ is Lebesgue measure. ✓
  - Remark: transitivity is not used; only (K) and (R) are.
- **(c)** ν|_M + ν₂|_{N₊} is bounded, countably additive and positive on non-null sets. Relevant comparisons see only
  M, and (R) applies with finite values. ✓

### 2.3 Theorem F1.3 and the refutation (CORRECT)

- (1) follows from F1.2(b), F1.2(c) with D2.1 step 7, and F1.1(c) with g = φ. The M⁻ statement uses the M⁻ half of
  F1.1(c). ✓
- (2) holds because local finiteness on the σ-compact set U gives σ-finiteness. ✓
- (3) holds by Prop. D2sigma. ✓
- (4) ν_t = λ|_{c_t} + ∞·λ|_{d_t} works. I re-derived the case split:
  - if δ⁺ meets d_t, the cost is ∞ on the right;
  - otherwise δ⁺ ⊆ c_t forces b < t, so E₁X ⊆ c_t, where ν_t = λ;
  - a generator-type δ has δ⁺ ⊇ Q_g near 1, which meets d_t;
  - so δ ∈ 𝒦₀ and λ(δ⁻) ≤ λ(δ⁺). ✓

**Conclusion.** conj:sigmaB ("ρ_i locally integrable on U", n ≥ 2) is **false**, with D2 as an n = 2 counterexample
under (E1) and (E2).

### 2.4 Cross-check with F2.4 (agreement; CORRECT)

F2.4 reaches the same conclusion at R₊(1,0) under (E1).

| Step of F2.4 | Method | Check |
|---|---|---|
| (A) ν(c_b) < ∞ | Uses 𝒦₀ membership of 1_{A′} − 1_B directly, a D2-specific substitute for (K) | Tails ≥ 0 because λ(A′) = λ(B) and A′ ⊆ d_b ✓ |
| (B) monotonicity | Uses cuts strictly between x′ and x″ | ✓ |
| (C) | Is D2.1 step 7 with finite ν(c_a) | ✓ |
| (D), (E) | Coincide with F1.2(b) and F1.1(c) | ✓ |

Differences:
- F1.3 is strictly more general: any reading with (R), plus the ∂U ray.
- F2.4 is self-contained inside D2.
- Neither uses the other.

## 3. Priority 3: F1.4 and F1.5 (CORRECT)

- **Tools.**
  - (i) Shrinking, (iii) chaining and (iv) disjoint sums are ternary-sum closures. Each sum is checked to be
    ternary: P ∩ Q = ∅, and R ⊆ d_{b₀} is disjoint from c_{b₀}.
  - (ii) is (K) at b₀ against the regular model with E₁ = (c_{b₀} ∖ Q) ∪ R.
- **Rounding.**
  - P(cover ≥ cλ(S)/2) ≥ c/2 = 0.316, since Y ≤ λ(S) and E[Y] ≥ cλ(S).
  - P(cost ≤ 4Γ) ≥ 3/4.
  - The joint probability is ≥ 0.066 > 0 (`ref_geometry.py` (5)). Capping w_k at 1 keeps the cover. ✓
- **Export.** ν₂(R) ≤ 4Γ + η < ν₂(d_{b₀}) when 4Γ < ν₂(d_{b₀})/2, so the disjoint R_i fit. ✓
- **Lower bound.**
  - s_m = inf{φ₁(P) : μ̄(P) ≥ m} > 0 by (SR₁), which holds by Cor. SR next to an additive world.
  - φ₁(Z) is attained and sections are initial segments, so c_{s_m} ≤₁ Z ≤₁ R.
  - Prop. MP♯(a),(b) give t* < 1 and d_{t*} ≤₂ R, i.e. ν₂(R) ≥ ν₂(d_{t*}) > 0.
  - θ depends only on (S, b₀). ✓
- A certificate whose sources overlap its targets reduces to the disjoint case with weights scaled by (1−ε)^{−1}.
  This is harmless.

**F1.5.**
- l(b) and r(b) are nondecreasing by Prop. lattice and nestedness. λ(d_b) → 0 forces r → 1 and l → α′.
- On K ∩ M⁺, T ≤ 1/(1+c). On cl(K ∩ M⁻) ⊆ U, T ≤ T₀ < α′ by compactness. ✓
- The last sentence ("must use targets accumulating at R₊(1,0)") is **necessary only**. On host B, or any chain with
  r(b) = 1 at some b < 1, every compact K ⊂ U has K ∩ M inside some c_{b₀}, so no compact-target certificate exists
  at all. F1.9 shows that host A realises it.

The scope sentence ("with both worlds non-additive the literal (C) is open") is accurate. F1.4 uses Cor. SR at world 2.

## 4. Priority 4: D2′_A and D2′_B

### 4.1 Design (Lemma F1.5′; CORRECT)

- **(D1′)**
  - Host A: x is increasing in T on each arc. So z < z₀ (T near β′) gives small x, and y ≥ y₀ (T near α′) gives x
    near 1.
  - Host B: x(M⁺) < λ(M⁺) < x(M⁻).
- **(D2′)**
  - On M⁻, y and x are increasing functions of T that tend to 1 together, so {x ≥ t} ⊇ M⁻ ∩ {y ∈ B′_m} for large m.
  - The product structure λ = λ(M⁻) × (radial mass ϖ) × Leb(y) holds because the angle is independent of the radius.
  - Projective-plane incidences and the independence of the digit levels give Leb(Ŷ_g ∩ Ŷ_{g′}) > 0. ✓
- **(D3), (D4′)** are as in D2.
  - (q_n+1)/L_n = 0.40, 0.237, 0.120 and 0.062 for n = 1, …, 4 (q = 5, 17, 67, 257).
  - These are below 2^{1−n} and tend to 0. ✓
- **Bounded away from zero.** On cl(S ∪ W) both coordinates are bounded away from 0, by the ∂U rays and the cut-offs
  z₀, y₀.

### 4.2 Lemma F1.6a: strict (G), (IB), transitivity (CORRECT)

The key observation, used throughout, is that **P_g ∩ W = ∅, so g_* = 1_{Q_g} on all of W**, not only on {x ≥ a}.
With it, the cases go through as follows.
- **(F).** P_g ∩ {x ≥ t} = ∅ for t ≥ a.
- **Strict (G).**
  - A base δ ≤ 0 has ∫_M δ = τ_δ(0) ≥ 0, so δ = 0.
  - A generator-branch δ ≤ 0 would be ≥ 1 on Q_g ∩ W ∩ {x ≥ t*}, which is non-null.
- **Sums.**
  - D ≥ 0 on 𝒜₁ by R⁻.
  - Mixed R⁺/R⁰ sums use (F).
  - Base + base and base + generator stay in the cone or its translate.
  - Generator + generator gives σ ≥ 2 on Q_g ∩ Q_{g′} ∩ W ∩ {x ≥ max b*}, which is non-null by (D2′). Impossible.

So 𝒜₁ is closed under ternary sums, and the vector form gives a preorder with (IB).

### 4.3 Lemma F1.6b: closed sections for every model (CORRECT)

- **(i)** Same as D2.4(i). R⁺ does not see the W-clause.
- **(ii) B₀.** For b < 1, δ_b = 1_A ≥ 0 on {x ≥ b}, so the W-clause holds with b* = b. Monotonicity of t + λ(A∩{x≥t})
  gives B₀ = [0, λ(A)].
- **(ii) B_g.**
  - The W-clause with large b* reads "Q_g ∩ {x ≥ t} ⊆ A a.e. for some t". The clause is monotone in b*, so
    "some b*" is equivalent to "all large b*", and the clause depends on A only.
  - The tail clause is (b−t)⁺ ≤ u_g(t), with τ_{g_*}(t) = λ(Q_g∩{x≥t}) − λ(P_g∩{x≥t}).
  - Bounds: b ≤ λ(A)+λ(P_g)−λ(Q_g) at t = 0. At t = a, b ≤ 1 − λ(Q_g), using Q_g ⊆ W ⊆ d_a.
  - The initial-segment and closedness arguments are as in D2.
- **Union.** It is closed by (D3). Every b_k → s eventually lies in some B_g with λ(P_g) > (s − β₀)/2, there are
  finitely many such g, and one of them repeats. ✓

### 4.4 Theorem F1.6 (CORRECT)

- **(K) for every model.** For N_X null, 1_Q − 1_P is ≥ 0 on all of {x ≥ b}, hence on W ∩ {x ≥ b}. ✓
- **Vertices.** By (G). ✓
- **World-2 sections.** C_b ⪯₂ X iff b ≥ λ(A) − λ(N_X), which is closed. ✓
- **Step 4 (no weak domination).**
  - b = 1 is handled separately.
  - For b < 1, δ′ − g_* ≤ −1 on Q_g ∩ {x ≥ max(b, b*)} ⊆ W, which is non-null. So only the base branch is possible,
    which forces Q null, and then λ(P) ≤ 0. ✓
- **Step 5 (strict domination of every X ≠ C_b).**
  - Regular X: take b = λ(A). C_b ⪯₂ X holds with equality, and C_b ⪯₁ X holds by B₀. If X ⪯₁ C_b as well, step 4
    gives X = C_b.
  - Non-regular X: take b = max(0, λ(A) − λ(N_X)). Then b ≤ λ(A) ≤ a + λ(A∩d_a) ≤ ψ(a), so C_b ⪯₁ X, and R⁻ gives
    X ⋠₁ C_b.
  - So U_L = C_L = {C_b}, and (C) and (LA) hold. ✓
- **(LF).** Host B's K_b = [0, r] or [l, 1] contains K′ in its relative interior. This includes K_{1/2} = [0,1],
  whose boundary rays R₊(1,0) and R₊(0,1) lie in U. ✓
- **Steps 7–8.**
  - The certificate is relevant, since g_* − g_* = 0.
  - (M2): every relevant δ has D = 0. Generator terms are excluded on W ∩ {x ≥ max} by (D2′), so f ∈ 𝒦₀^W, and
    f ≤ 0 forces f = 0. ✓
- **Wording.** "Every non-additive ingredient lies in one compact subset of ℝ² ∖ {0}" overstates. World 1's base order
  is tail dominance in x, an incomplete, non-additive order acting on all of M. What is confined is the generators
  (sources and targets) and the protected set. Say "every generator and the protected set".

`d2prime_cell.py` was rerun and its output is byte-identical: 0 failures in every listed test, and 3 expected failures
for the W-only-heavy ρ. `ref_geometry.py` (4) independently reproduces the coupling failure in the continuum on host A.
- At b = 0.99, take P ⊂ c_b ∩ M⁻ and Q ⊂ d_b ∩ M⁺ with λ(P) = 0.00224 < λ(Q) = 0.00438. (K) then forces C_b ⪯₁ X.
- The density 1/(1−x) on M⁻ and 1 on M⁺ gives ν(P) = 0.188 > ν(Q) = 0.004, so it does not endorse this comparison.

### 4.5 Lemma F1.7 (CORRECT)

- **(a)**
  - δ⁻ ⊆ c_b with b < 1, and φ is right-continuous and nondecreasing, so ∫δ⁻φ ≤ φ(b) < ∞.
  - Tonelli on δ^± separately gives ∫δφ = φ(0)τ_δ(0) + ∫τ_δ dφ ≥ 0.
  - This needs no near-end positivity of δ, so the W-restriction is harmless. ✓
- **(b)** The blockwise construction of φ is correct. Each m with a_{j,m} > 0 contributes ≥ 1, and (D2′) with g = g′
  gives infinitely many such m. ✓
- **Unproved parenthetical.** §5's "(which transitivity forces in that architecture)" is not proved.
  - Sum closure constrains only pairs whose sum is ternary.
  - F1.7(b) uses only the g = g′ case of (D2′).
  - Fix: delete the parenthetical, or prove it.

### 4.6 Theorem F1.8 and Remark F1.9

- **F1.8 (CORRECT).**
  - (1) holds by step 7 under (R).
  - (2) follows from F1.2 + F1.1(c). Host A blows up at the interior ray although no trade reaches it.
  - On host B, K ∩ M ⊆ c_{b₀} for compact K ⊂ U (F1.1(d)). So ν_φ of F1.7(b), with λ on N₊ and ρ₂ ≡ 1, is
    positive and locally integrable on U. **conj:sigmaB holds in D2′_B**, a full system whose world 1 fails SP^reg.
  - So the failure of conj:sigmaB depends on the host (the selection), as F1 says.
  - (3) ν_t carries over verbatim.
- **F1.9: GAP (fixable).** The claim covers every endorser under (R) that is finite on K_η. Under (E1), the step
  ν(c_a) < ∞ cites F1.2(a), which assumes σ-finiteness. **Fix** (uses only (K) and (R)):
  1. Choose η so that K_η ∩ M ⊆ d_a. This is needed anyway for W′ ⊆ d_a.
  2. Put κ := λ(K_η ∩ M) > 0, and pick 0 = b₀ < b₁ < … < b_N = a with steps < κ.
  3. If ν(c_{b_j}) < ∞, take Q ⊆ K_η ∩ M with λ(Q) > b_{j+1} − b_j, and the regular X with
     E₁X = c_{b_j} ∪ Q.
  4. (K) at b_{j+1} gives C_{b_{j+1}} ⪯₁ X, and (R) gives ν(c_{b_{j+1}}) ≤ ν(c_{b_j}) + ν(K_η) < ∞.
  5. By induction, ν(c_a) < ∞. The certificate then gives ν(S) ≤ εν(K_η ∩ M) for every ε.

  Under (E2) no fix is needed.

### 4.7 F1 §5 and the conjectures

- **Equivalence (CORRECT).** By F1.2, next to an additive world, an endorser finite on compact subsets of M exists iff
  a σ-finite endorser exists.
- **Caution on F1.C′** ("locally integrable on M").
  - Its evidence is two-world only. In two worlds next to an additive world, F1.2 places every blow-up at the far end
    of the chain. That end is always R₊(1,0) and/or ∂U, and never interior to M. So F1.C′ is automatic there whenever
    a σ-finite endorser exists.
  - In three worlds without (Nest_e), F2 §1.4 leaves ends shrinking to interior rays of M, or to the T1-correct side of
    ∂D_{T1}, unexcluded. Exactly there F1.C′ would fail if endorsers must blow up at ends.
  - So the claim in F1 §2.4 that F1.C′ "still serves the localisation route" is contingent on an F2.3-type location
    result, i.e. on (Nest_e). Say so.

## 5. Priority 5: F2

### 5.1 Hypotheses extracted for E1.1–E1.6 (CORRECT)

I re-derived each row. Notes:
- **E1.1.**
  - (a) needs no integrability (M0closed(a)).
  - (b) uses finite ψ: B_t is the a.e.-unique pointwise minimiser.
  - The "Which worlds" GAP is real. Admissibility of (ν_i, aρ_j, bρ_k) needs aρ_j/(bρ_k) bounded below on {T1 correct
    only at j}, and symmetrically. If ess inf ρ_j/ρ_k = 0 there, no constants work.
- **E1.4.** It is location-free. ρ_if_i is integrable (Σ2^{−r}Σl^{−2}). The margin computation needs only that T1 is
  eventually correct at world i on each end.
- **E1.5.** Step 1's base comparison T1 ⪯_k Y and step 2's (h) computation never use where the ends are, nor E1.3.
  F2 is right.
- **E1.6.** It is two-world. "D2.C does not bear on T1" is overstated, as F2 says.

### 5.2 GAP: "integrability relaxed to a.e. finiteness" (E1.3(a) row, F2.2, F2.3)

- **The problem.**
  - Under the total-cost reading (E1), an a.e.-finite ρ_k may have ρ_kμ(E_kT1) = ∞, resp. ρ₂μ(E₂C_p) = ∞.
  - Then the comparison T1 ⪯_k X (resp. C_p ⪯₂ X) compares ∞ with ∞ and is endorsed vacuously.
  - So "T1 ⋠_k X by endorsement" fails.
- **The fix.** Either state the endorsement in cancellation form (E2), where ρ(R) > ρ(p) with both finite gives
  non-endorsement, or add ρ_kμ(E_kT1) < ∞ (resp. ρ₂μ(E₂C_p) < ∞ for p ∈ e₁₂).
- **Scope.** Under integrability (E1's original setting) there is nothing to fix.

### 5.3 Where ends sit: F2.1–F2.3 (CORRECT, with the §5.2 caveat)

- **F2.1.** cl D_{T1} ∖ 0 ⊆ U, so P_{K′} has a positive minimum on cl D_{T1} ∩ S². Rejection is world-i-correct where
  h_i < 0. ✓
- **F2.2 (first claim).**
  - X = C_p △ (p ∪ R) strictly improves world 2.
  - Competitiveness on {1,2} gives C_p ⪯₁ X with δ = 1_R − 1_p.
  - This δ is −1 at every depth and its positive part avoids the deep ends.
  - Contradiction with end-protection. ✓
- **F2.2 (second claim).**
  - Given K_p → co(K′ ∪ {e₂}) (imported), P_{K_p} is |h|-Lipschitz in the Hausdorff distance.
  - This gives d_b ⊆ {m₂ < η|·|} near e₂. ✓
- **F2.3.** I re-derived the sign-class bookkeeping:
  - Q₁ = (+,−,−) ∪ (−,+,+) feels both edges;
  - (+,−,+) and (−,+,−) lie in Q₂ ⊆ R₁₂;
  - (+,+,−) and (−,−,+) lie in Q₃ ⊆ R₁₃;
  - in the h₁ < 0 classes, small h₂ (or h₃) with the other coordinates ≤ 0 is incompatible with U, which forces
    proximity to ∂U. ✓
- **Wording.** E1's "these are the near-unanimous limits" is **unproved, and the proved constraint (E1.3(a)) also
  admits ∂U ∩ {h_i < 0}**. That is the accurate wording of F2's "WRONG".
  - "False as a characterisation" is fair only in this sense: no three-world protected world with a ∂U end is
    constructed.
  - The two-world D2′_B does have its whole protected end at ∂U (F1.8), which corroborates F2.

### 5.4 F2 §2 (E1.4 and E1.5 at ∂U; CORRECT)

- At ∂U ∩ {h_i < 0}, E1.4 applies with no hypothesis on the other worlds.
- E1.5 applies iff its joint hypotheses hold.
- No result shows a three-world D2 installation meets them.
- F2.4 does not touch E1.5, since E1.5 concerns base-only endorsers and E1.6 provides one in two worlds.

### 5.5 F2 §3 (B3; CORRECT)

Consistent with B3_referee:
- B3.2 holds in its corrected form ("a total world of a cover that does not add up is not AR");
- B3.C is one-directional and open.

The round-report line "must be incomplete (as reworded by the referee)" is indeed in the project round report, and it
overstates.

### 5.6 F2 §4.1, the replacement sentences

- **starthere sentence: CORRECT.**
  - Under end-protection, "non-end-positive relevant comparisons" equals E1.5's base (F2 §1.1).
  - "Jointly heavy" correctly carries (h)'s dependence on the other densities.
- **Ends sentence: GAP.**
  - "Under (Nest_e) on both edges they lie at …" omits F2.2's further hypotheses: densities at worlds 2 and 3,
    positive and a.e. finite (with the §5.2 reading), endorsing the edge comparisons.
  - "Automatic at ∂U ∩ {h_i < 0}" should read "automatic for ends that eventually lie in a collar of ∂U inside
    {h_i < 0}". An end approaching ∂U ∩ {h_i = 0} is not covered.
- **B3 sentence: GAP (wording).** "That it cannot be total at all is Conjecture B3.C" should read "would follow from
  Conjecture B3.C". B3.C plus B3.2 implies it; the converse is not claimed (B3_referee, "Equivalently" is WRONG).
- **σ-finite sentence: CORRECT.** I recommend it name the sharper target F1.C′, which in two worlds next to an
  additive world is equivalent to σ-finiteness (F1 §5). It should also record that conj:sigmaB itself holds in D2′_B.
  - *Reading.* A failure of local integrability on U is a property of the selection, not of the non-adding-up
    mechanism.
- **Exclusions sentence: CORRECT.** "Nothing proved fixes where protection sits" is in mild tension with F2.3. Prefer
  "nothing proved confines protection to near-unanimous limits; under (Nest_e) and F2.2's hypotheses it lies there or
  at ∂U ∩ {h_i < 0}".

### 5.7 F2 §4.3, the open route

**GAP in item 5.**
- **The defect.** F2 lists item 5 among the properties of "a world i". E1.1(b) yields an unendorsed dominator
  comparison at *some* world j, which may depend on ν and t. Moreover, under (H_U), E1.1(a),(b) make item 5 automatic
  for every admissible integrable ν. So item 5 is not a restriction on world i.
- **Restatement.** For every admissible integrable ν, the set of t at which some world's dominator comparison is
  ν-unendorsed is non-null; this is automatic under (H_U).
  - At an end-protected world whose ends are eventually T1-correct, with ν replaced by its E1.4 reweighting, any
    unendorsed comparison at that world is a base comparison.
  - The constraint on world i is then that its base comparisons into the E1.4-reweighted Bayes models cannot all be
    ν′-endorsed. This is a constraint only when the failures must sit at world i, for instance when the other worlds'
    comparisons are all endorsed by ν′.
- **The rest.** (R-a), (R-b), "also not covered" and the nearby conjecture are accurately labelled. In the
  conjecture, the "Lyapunov-free admissibility step" is indeed the missing piece. E1.1(b)'s pointwise-minimiser
  argument additionally needs ψ-differences on C △ B_t to be finite. They are, if ρ is integrable off the deep ends
  and both models agree deep in the ends.

## 6. Requested changes

1. **F1.9.** Replace the citation of F1.2(a) by the stepwise (K) argument of §4.6, or restrict the claim to σ-finite
   endorsers or to (E2).
2. **F1 §5.** Delete "(which transitivity forces in that architecture)", or prove it.
3. **F1.6.** Change "every non-additive ingredient" to "every generator source and target, and the protected set".
4. **F1 §2.4 / F1.C′.** Add that its use for T1 is contingent on an F2.3-type location of ends, i.e. on (Nest_e).
5. **F1.5.** Mark the last sentence as a necessary condition only. On host-B-type chains no compact-target
   certificate exists.
6. **F2 (E1.3(a) row, F2.2, F2.3).** State the endorsement in cancellation form, or require finite total cost out of
   T1 (resp. C_p).
7. **F2 §4.1.** Repair the ends sentence and the B3 sentence as in §5.6. Optionally add F1.C′ and D2′_B to the
   σ-finite sentence.
8. **F2 §4.3.** Restate item 5 as in §5.7.
9. **Write-up.** Adopt both notes' list:
   - mark conj:sigmaB as false (n = 2, D2) and correct its status sentence;
   - correct D2_referee2 §3.3;
   - change the Intro, summary and table "open" entries;
   - remove the "near-unanimous limits only" sentences of §8.5(f),(g);
   - in Prop. D2sigma's Reading, name both end rays.

## 7. Files

- `f12ref_py/ref_geometry.py` (+ `.out`) checks:
  - (1) the error-set formula, by brute force from the C2.1 parametrisation;
  - (2) the end rays and their location relative to U;
  - (3) the analytic slope 2.3095 and share 0.4361;
  - (4) the continuum coupling counterexample to a W-only-heavy density on host A;
  - (5) the F1.4 rounding constants;
  - (6) host B's ends.
- `f12ref_py/*.rerun` hold the reruns of all author scripts, each byte-identical to the stored outputs.
