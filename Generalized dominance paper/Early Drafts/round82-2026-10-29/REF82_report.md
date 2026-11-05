# REF82 referee report: rescaled-coverage.tex

## Results first

1. **Main claims are correct.** Section 7 proves (E), (A), (S) and (T) of LDG Definition 3.3 for 𝔏 = {L^M}, with almost coherent models as the coherent class. This holds under (M1), (M3) and (M5), with finitely many worlds. I checked every proof line by line and every constant, and found **no ERROR and no GAP** in the mathematics.

2. **Theorem 4.6 (cover rankings under (CC)) is correct.** (U) is used nowhere, and (M3) is not used either.
   - The constants are right: the thin-set constant C_μ, the face bound 2nC_μBq(T^c), κ = 2nC_μ(A+2B), and η₀ = 1/(nκ).

3. **The (CC) proof for the rescaled family (Proposition 5.3) is correct**, including the repaired step-1 witness.
   - The witnesses lie in W_ij but may lie on its boundary (g_j = 0).
   - The Setup paragraph moves each one to g − εe_j. That point lies in the open set U ⊆ W°_ij, which is non-null by (M3), and U ⊆ (D_{K_p} ∩ W_ij) ∖ D_{K_q}.
   - I checked all branches: step 1; step 2 with l = j; step 2 with j ∉ supp p; step 2 with ε > 0.

4. **The M = Δ obstruction, n ≥ 2.** Here (A1\*) is the note's world-by-world axiom, and (A1) is the application's axiom (guidance at every world).
   - **Under (A1\*) it is settled: TRUE for every n ≥ 2.** I independently verified the writer's witness X = (G₁ ∩ (G₂∪…∪G_n)) ∪ N for every nonempty S (proof below).
   - **Under (A1) it is FALSE for every n ≥ 2.** Some ranking satisfying (A1) satisfies (S), and even (T), with the assigned models c_p = D_{Δ_supp p}. A counterexample ranking is given below.
   - The note states the obstruction correctly with (A1\*). It should say explicitly that it fails under (A1) (findings M1 and M2).

5. **Numerical tests all agree with the note.** These cover (CC), the loss identity, the budget inequality, the thin-set lemma and the obstruction (scripts in `ref/`, details at the end).

**Verdict.** (E), (A), (S) and (T) are established for 𝔏 as stated, under (M1), (M3) and (M5) with Ω finite, with almost coherent models as the coherent class. All findings below are MINOR (presentation, scope, or unneeded hypotheses).

---

## The n ≥ 3 obstruction (brief item 4)

### (a) Under (A1\*): the obstruction holds for every n ≥ 2 (OK, Proposition 6.2 and Corollary 6.3)

**Setup.**
- The rescaled family of Δ has K_p = {F_p(m) : m ∈ Δ, p·m > 0} = Δ_{supp p}.
  - ⊆: every F_p(m) is supported in supp p.
  - ⊇: for x ∈ Δ_{supp p}, take m ∝ x_k/p_k on supp p and m = 0 elsewhere.
- So c_p = D_{Δ_supp p}. Under (M2), D_{Δ_S} ≈ G_S^+, since φ_{Δ_S}(g) = min_{k∈S} g_k.

**Notation.** Let P ≔ G₁ ∩ (G₂ ∪ … ∪ G_n), R ≔ {g₁ > 0, g_k ≤ 0 for all k ≥ 2}, N ≔ R ∩ {g₁ > 1} and X ≔ P ∪ N. Then G₁ = P ⊔ R and X ⊆ G₁.

**Criterion.** By (F5), X ≤_ω Y if and only if Y ∩ G_ω ⊆ X a.e. and X ∖ G_ω ⊆ Y a.e.

**Case S ∋ k for some k ≥ 2; take ω = 1.**
- X ∖ G₁ = ∅.
- Every g ∈ G_S^+ ∩ G₁ has g₁ > 0 and g_k > 0, so g ∈ P ⊆ X. Hence X ≤₁ G_S^+.
- X ≉ G_S^+:
  - If 1 ∉ S, the set G_S^+ ∩ {g₁ < 0} is nonempty, open and disjoint from X.
  - If 1 ∈ S, then N ∩ G_S^+ = ∅ (on N, g_k ≤ 0), and N contains the nonempty open set {g₁ > 1, g_k < 0 for all k ≥ 2}.

**Case S = {1}; take ω = 2.**
- G₁ ∩ G₂ ⊆ P ⊆ X, and X ∖ G₂ ⊆ G₁. Hence X ≤₂ G₁.
- G₁ ∖ X = R ∖ N contains the nonempty open set {0 < g₁ < 1, g_k < 0 for all k ≥ 2}. So X ≉ G₁.

**Conclusion.**
- In either case, (F5) gives μ(E_ω(G_S^+) ∖ E_ω(X)) = μ(X Δ G_S^+) > 0. (A1\*) then gives X ≺_ω Y for every Y ≈ G_S^+, so Y ⪯_ω X fails.
- So no assigned model weakly dominates X. This contradicts the common conclusion of LDG Theorem 2.2, Corollary 2.3 and Theorem 2.4.
- For n = 2 this reduces to the lead's example: R = W₁₂ and X ≈ D_Δ ∪ N.
- `ref/misc.py` part 3 confirms every inclusion and non-equivalence on samples, for n = 2, …, 6 and all S.

### (b) Under the application's (A1): the obstruction FAILS for every n ≥ 2

**The ranking.** Let G^{++} ≔ {g : g_k > 0 for all k} and G^{--} ≔ {g : g_k < 0 for all k}. Put

  ℓ(X) ≔ μ(G^{++} ∖ X) + μ(X ∩ G^{--}),  ι(X) ≔ 1 if X ≉ G_S^+ for every nonempty S, and ι(X) ≔ 0 otherwise,

and define X ⪯_ω Y ⇔ ℓ(X) + 3ι(X) ≤ ℓ(Y) + 3ι(Y), for every ω. This ranking evaluates every model.

**(A1).**
- Suppose X ≉ Y and the change from X to Y is guided at every world. Then A = Y ∖ X ⊆ G^{++} a.e. and B = X ∖ Y ⊆ G^{--} a.e.
- Hence ℓ(Y) = ℓ(X) − μ(A) − μ(B) = ℓ(X) − μ(X Δ Y) < ℓ(X).
- If ι(X) = 0, then ℓ(X) = 0, so no such Y exists.
- If ι(X) = 1, then ℓ(Y) + 3ι(Y) < ℓ(X) + 3. So Y ≺_ω X at every world.

**(S), via LDG Corollary 2.3.**
- ℓ(D_{Δ_S}) = 0 exactly:
  - G^{++} ⊆ D_{Δ_S}, since every g ∈ G^{++} has g ⪈ 0;
  - D_{Δ_S} ∩ G^{--} = ∅, since such g has min_{k∈S} g_k < 0 and is not ⪈ 0.
- So c_p ≔ D_{Δ_supp p} has loss 0, the minimum.
- Hence c_p ⪯_ω X for all X and ω, every set {p : c_p ⪯_ω X} equals Δ and is closed, and c_p is undominated and coherent.

**(T).**
- Every model with ι = 1 has loss ≥ 3 and is strictly beaten at every world by c_p. So U_L = C_L = {X : X ≈ G_S^+ for some S}.
- A model tied at every world with a member of C_L has loss 0, hence ι = 0, hence lies in C_L.

**What this shows.** The obstruction depends on the world-by-world strength of (A1\*), not on the reading of "guided". This is not a defect of the note's mathematics, but the author asked about (A1).

---

## Findings

| # | Label | Location | Finding and fix |
|---|---|---|---|
| M1 | MINOR | §2, sentence after Definition 2.7: "(A1\*) reads 'guided at ω' as a non-null reduction of the errors at ω." | Misleading. By Lemma 3.2 the two readings of "guided at ω" coincide under (M2). What separates (A1\*) from (A1) is the quantifier. **Replace with:** "By Lemma 3.2, under (M2) the hypothesis of (A1\*) at ω says exactly that the change from X to Y is non-null and guided at ω. So (A1\*) is the world-by-world form of (A1): it asks a change guided at a single world to make the model strictly better at that world. (A1) asks this only of changes guided at every world. Lemma 3.2 shows that (A1\*) implies (A1)." |
| M2 | MINOR (scope) | After Corollary 6.3 | Add a remark that the obstruction needs (A1\*): under (A1) alone, (S) and (T) can hold with c_p = D_{Δ_supp p}. Use the ranking ℓ + 3ι and its four-line proof from §(b) above. Without it, a reader of the brief (which says "under (A1)") may misread Corollary 6.3. |
| M3 | MINOR | Remark 5.2: "the analogous theorem with that monotonicity condition in place of (CC) does not apply to it" | Refers to a theorem not stated in the note, so the note is not self-contained here. **Replace with:** "Consider the condition (U): if p_i > q_i then ū_{K_p}(i) > ū_{K_q}(i). Under (M3), (U) implies (CC) by Lemma 3.6(b), since covers p ∈ 𝒫_i(X) and q ∈ 𝒫_j(X) satisfy ū_{K_p}(i) ≤ ū_{K_q}(i). The rescaled family need not satisfy (U), so (CC) is verified directly in Proposition 5.3." Keep the numbers, which I checked: p∗m = (0.12, 0, 0.39), q∗m = (0.09, 0.035, 0), 0.12/0.51 ≈ 0.235 < 0.72 = 0.09/0.125, and p₁ = 0.4 > 0.3 = q₁. |
| M4 | MINOR | Proposition 5.3 hypotheses: "Assume (M2) and (M3)." | (M2) is not used; only (M3) is. Change to "Assume (M3)." |
| M5 | MINOR | Theorem 4.6 and the line after it | (M3) is assumed and then said to be unused; I confirm it is unused. Either drop (M3) from the hypotheses or keep the sentence as is. Corollary 4.7 needs (M3) only through (CC) of particular families. Dropping it makes Theorem 4.6 cleaner. |
| M6 | MINOR | Remark 7.4 | Claims that (A2) and (A3) of the application hold, but never states them. **Add, in LDG's convention:** "(A2): there are no ω, X, Y, Z with X ⪯_ω Y, Y ⪯_ω Z and Z ≺_ω X. (A3): if Z and X are tied at ω and Y ⪯_ω Z, then Y ⪯_ω X." The one-line proofs given are correct. (A4) is correctly flagged as not checked. |
| M7 | MINOR | Definition 2.1 | It mixes LDG's definitions with two that LDG does not have: "strictly dominates at every world" and "competitive on S". Add: "The last two notions are not from [LDG]; they are used only as tools." |
| M8 | MINOR | Remark 4.8, first sentence | "The conditions hold only for almost coherence" is proved only for these rankings. **Replace with:** "For the rankings of this note, the conditions hold for almost coherence but not for coherence itself." The argument is correct: D_p ∪ {0} ≈ D_p is tied at every world with D_p ∈ 𝒞_L and violates (D1). |
| M9 | MINOR | Lemma 1.1(b): "(M1) is standard." | Add: "∫‖g‖_∞ dμ ≤ Σ_k ∫|g_k| dμ = n√(2/π)." |
| M10 | MINOR | Proposition 6.1, second sentence: "Under (M3), a model is ≈ D_{K^M_p} … iff it is ≈ D_{M′} …" | (M3) is not needed here, since the sentence follows from the first sentence alone. Only the "In particular" clause uses (M3), through Lemma 3.5. Move "Under (M3)" to that clause. |

---

## Item-by-item checks (all OK)

### §1: measure conditions (Lemma 1.1)

**(a) (M5) ⇒ atomless and (M5) ⇒ (M2).**
- Atoms: apply (M5) with a ≡ t(g₀) and b ≡ 0.
- (M2): φ_K(g) = φ_K(h(g)) + t(g), and a = −φ_K is continuous.

**(b) Gaussian μ.**
- Cov(t, h_k) = 1/n − 1/n = 0, and the variables are jointly normal, so t and h are independent.
- t ~ N(0, 1/n) has density at most √(n/2π). So c_μ = √(n/2π).

**(c) The application's existence measure (appshort Lemma 4.3).**
- The construction matches appshort with E = ℝⁿ.
- h(g+s𝟙) = h(g) and t(g+s𝟙) = t(g)+s. Tonelli then gives c_μ = 1/√(2π).
- (M1): bound ∫|s| dλ = √(2/π).
- (M3): Φ is a linear homeomorphism from E₀ × ℝ onto ℝⁿ, and (g_k) is dense in E₀.

**C_μ.** It is finite, since ‖h‖_∞ ≤ 2‖g‖_∞. The application's (M3) (full support of the diffuse part) reduces to plain full support because μ is atomless.

### §3: ranking-free facts
- **(F1)–(F5):** OK, including E_i(X) ∖ E_i(Y) = ((Y∩G_i) ∖ X) ∪ ((X∖G_i) ∖ Y).
- **Lemma 3.2:** OK. It uses {g_ω = 0} = {φ_{{e_ω}} = 0}, which is null.
- **Lemma 3.3 (error-minimality):** OK. D contains no g ≤ 0, by (D1), (D2) and (D4).
- **Lemma 3.4:** OK.
  - Separation: w·c = 0 from y = 0 and y = 2c, and m = w/Σw_k ∈ M.
  - Sufficiency: x = g − ε𝟙 lies in the closure C, x′ ∈ D is near x, and g − x′ ≫ 0.
  - Measurability holds under (M2).
- **Lemma 3.5:** OK.
- **Lemma 3.6:** OK.
  - (a) is direct.
  - (b): the lower-probability witness e_i − s𝟙 lies in W°_ij; the upper-probability witness s𝟙 − e_i lies in W°_ji.

### §4: the cover-ranking theorem

**Lemma 4.2 (thin sets).**
- For δ ≤ ½: ‖g‖ ≤ 2‖h‖ + |t + φ_K(h)|. This gives (1−δ)|t + φ_K(h)| ≤ 2δ‖h‖, hence |t + φ_K(h)| ≤ 4δ‖h‖.
- (M5) with a = −φ_K and b = 4δ‖·‖_∞ gives the bound 8c_μδ∫‖h‖ ≤ C_μδ.
- For δ > ½ the bound is trivial, since C_μ ≥ 2.
- The symmetric-difference bound follows from (F2), (F4) and (M2).

**Lemma 4.3 (faces).**
- ε = Bq(T^c), and m(T^c) ≤ ε for every m ∈ K_q.
- Both inclusions give min_{k∈T} |g_k| ≤ 2ε‖g‖_∞. Lemma 4.2 with K = {e_k} and δ = 2ε, then a union over |T| ≤ n sets, gives 2nC_μBq(T^c).
- The case ε > ½ is trivial.

**Lemma 4.4 (attainment and closedness).** OK. The maps p ↦ μ(E_i(X) ∖ E_i(D_p)) and p ↦ μ(E_i(D_p) ∖ E_i(X)) are Lipschitz with constant C_μA. 𝒫_i(X) is a zero set, hence compact.

**Lemma 4.5 (budget).**
- Identity (1) is OK. (CC) applied to (p^k, p^j) gives p^k_k ≤ p^j_k.
- The bound ‖p^i − p^j‖₁ ≤ 2ρ is OK.
- The case split in (ii) is exhaustive up to the null sets E_i(X) ∖ E_i(D_{p^i}).
- s_j ≤ 2(n−1)C_μAρ + 4nC_μBρ ≤ κρ.

**Theorem 4.6.**
- **Step 1:** OK. Each term of the budget sum is ≥ 0 and the sum is ≤ 1, so each L(X,i) lies in [0,1]. In the equality case, ρ = 0 forces all p^i to be equal and all s_i to be 0.
- **(a):** OK, in all three cover cases.
- **(b):** OK.
- **(c):** OK, since L(Y,i) < 1 forces i ∈ T(Y).
- **(d):** OK.
- **(e):** OK, since each 1 − L(X,i) ≥ q_i and the q_i sum to 1.
- **(f):** OK.
- **(g):** OK, since Σa_i < 1 makes q_i > a_i ≥ 1 − L(X,i), including for i ∉ T(X).

**Corollary 4.7 (i)–(v):** OK against LDG.
- 𝒞_L = 𝒞 ∩ 𝒰_L.
- The hypotheses of Corollary 2.3 come from Theorem 4.6(c) and (d), with c_p ∈ 𝒞_L for every p.
- Closure under ties comes from (a) and (e).

### §5: the rescaled family

**Proposition 5.1.**
- (i): F_p(m_λ) = (1−θ)F_p(m) + θF_p(m′), with θ(λ) = λ(p·m′)/((1−λ)p·m + λp·m′). By the intermediate value theorem, F_p maps [m, m′] onto [F_p(m), F_p(m′)], so K_p is convex.
- Sign identity: F_p(m)·g = m·(p∗g)/(p·m), with p·m ≥ δ > 0. This is valid for boundary p too.
- (ii) (Lip): the coordinate identity is OK, and ‖F_p(m) − F_q(m)‖₁ ≤ |(q−p)·m|/(q·m) + Σ_k m_k|p_k − q_k|/(q·m) ≤ 2‖p−q‖₁/δ. Pairing the images of the same m gives the Hausdorff bound.
- (iii) (Dom): B = 1/δ.

**Proposition 5.3: (CC).**
- **Step 1:** p∗g = e_i, so φ_M(e_i) ≥ δ. And m·(q∗g) ≤ q_i/p_i − sq_lδ < 0.
- **Step 2:** h^s vanishes off S = supp p (ε = 0 when j ∉ S). Hence p∗g^s = h^s and, by Step 1, q∗g^s = d∗h^s.
  - The sign of g^s_j is right in all three cases: j = l; l ≠ j ∈ S; j ∉ S.
  - s* is attained and s* ≥ δ/2.
  - φ_M(h^s) ≥ δ(s* − s).
  - f(s*) = (d_i − d_l)m\*_i + ε(d_l − d_j)m\*_j ≤ −(d_l − d_i)δ + ε(d_l + d_j) < 0.
- **Step 3:** OK.

**Corollary 5.4:** κ = 8nC_μ/δ. OK.

### §6: targets touching the boundary

**Proposition 6.1 (which models the rescaled families reach).**
- The characterisation matches the brief: "all members of M′ have the same support" is equivalent to "M′ ⊆ relint Δ_S".
- For the converse construction: p∗m = ((1−ε)/|S|)·m′ and p·m = (1−ε)/|S|.

**Example 6.4 (M = conv{e₁, e₂, u}).**
- F_p(u) = p, so K_p = conv{e₁, e₂, p}.
- D_{K_p} ⊆ (G₁ ∩ G₂) ∪ {g ⪈ 0}, and X ∖ G₁ ⊆ {g₁ = 0}, which is null.
- So X ≤₁ D_{K_p} and X ≤₂ D_{K_q} for all interior p, q, and (CC) fails.

**Proposition 6.5 (the homothetic family).**
- Λ < 1 < V for non-singleton M, λ ∈ (0,1), and Σr = 1.
- θ(r) = 1, since r_k − d_k = ℓ_k ≥ 0. So K_r = M.
- The identity (1−λ)p̲_{K_p} + λp̄_{K_p} = p holds, where p̲_{K_p} and p̄_{K_p} are the lower and upper probabilities of K_p.
- (Dom) holds with B = 1/λ.
- (Lip) holds with A = 1 + 2/δ_M. A = 1 + 1/δ_M also works, since ‖p−q‖_∞ ≤ ½‖p−q‖₁ on Δ.
- (CC) follows from Lemma 3.6(b) and the identity above. The singleton case is OK.

### §7: the class 𝔏 and the LDG conditions
- **Restatements:** Theorem 2.2, Corollary 2.3, Definitions 3.1 and 3.3 and Theorem 3.4 of ldgshort.tex are restated faithfully. The numbering is correct.
- **(E):** OK.
- **(A):** OK. X ≈ D ≈ D_M = D_{K^M_{p_M}}, which lies in 𝒞_{L^M}.
- **(S):** OK, via Corollary 2.3, with c_p = D_{K^M_p} ∈ 𝒞_{L^M}.
- **(T):** OK.
- **(A1) against appshort Definitions 2.1 and 2.2:** OK. "X ≠ Y" there means not equal a.e. Because L^M is invariant under null modification (Theorem 4.6(a)), the relations are also well defined on the application's a.e.-classes of models.

### Style
- **Jargon:** a case-insensitive search for certificate, record, safe, route, dangerous and shelter finds nothing.
- **Lemmas and theorems are unnamed.** The only bracketed arguments are citations, and named definitions are allowed.
- **\coloneqq is used throughout;** there is no `:=`.
- **Compilation is clean:** no warnings, no overfull boxes, no "??" in the PDF (14 pages).
- **Self-contained,** except for M3 and M6.

---

## Numerical tests (scripts in ref/)

**`ref/cc_witness.py`** runs the note's exact (CC) witnesses.
- Inputs: M is the convex hull of 1 to 4 random interior points; p and q have random zero coordinates; n = 2, …, 6.
- Over 2 seeds, it tested 244,421 cases with p_i > q_i and found 0 failures.
- Branches covered: step 1 (167k cases); step 2 with l = j (24.9k); step 2 with j ∉ S (10.8k); step 2 with ε > 0 (41.7k).
- In every case it checked that g ∈ W_ij with φ_M(p∗g) > 0 > φ_M(q∗g), and that the shifted point g − εe_j lies in W°_ij with the same strict signs.

**`ref/mc_loss.py`** uses Gaussian μ, n = 3, 2×10⁵ samples, a grid of mesh 1/20 on Δ, and the theorem's own η = 1/(2nκ).
- Families: 2 random interior rescaled families, and the homothetic families of conv{e₁, e₂, u} and of Δ.
- **Loss identity** L(D_{K_q}, i) = 1 − q_i: 160 checks, 0 failures.
- **(CC)** between all empirical covers of 240 test models (unions, intersections and flips): 0 failures.
- **Budget inequality:** the sum is ≤ 1 throughout. Equality occurred only when X coincides on the sample with some D_p, as Step 1 predicts.
- **Constant κ:** max s_j/ρ ≈ 0.50, against κ ≥ 421.

**`ref/misc.py`**
- **(CC) by direct Monte Carlo:** 2,568 cases with n = 2, …, 5 and p_i > q_i + 0.02.
  - One case showed zero empirical mass for (D_p ∩ W_ij) ∖ D_q.
  - `ref/cc_zero_case.py` resampled that case with heavy tails. The mass is positive (about 10⁻⁴), and the witnesses have g_i ≈ 700 because p_i = 0.024. This agrees with the proof.
- **Thin-set lemma:** max of μ{|φ_K| ≤ δ‖g‖_∞}/(C_μδ) ≈ 0.39, so the bound (ratio ≤ 1) holds.
- **Obstruction witness:** verified for n = 2, …, 6 and every nonempty S.
