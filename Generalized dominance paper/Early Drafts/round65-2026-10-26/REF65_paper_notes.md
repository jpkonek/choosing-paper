# REF65_paper: referee report on the new proofs in "Covering coherent sets of desirable gambles" (draft of 26 Oct 2026)

Verdicts: CORRECT / GAP / ERROR. Every step of the items below was re-derived by hand. Exact checks are in `ref65paper_py/checks.py`, with output in `checks.out` (all PASS).

Line numbers refer to `Covering coherent sets of desirable gambles (draft).tex`. Result numbers are as in the compiled PDF.

- **Compilation.** An independent rebuild in `ref65paper_py/build/` (pdflatex, three passes) gives 57 pages, with 0 warnings, 0 overfull boxes and 0 underfull boxes. The PDF is byte-identical in size to the delivered one.
- **Diff of the veto lemmas.** The old and new drafts differ only in the class name (item 2).

## Status table

| # | Item | Verdict |
|---|---|---|
| 1 | Theorem 8.14 (convex error levels), scope and (G) | **CORRECT** |
| 2 | Lemmas 8.8–8.11 widened from 𝒱_B to 𝒱 | **CORRECT**. The proofs are verbatim; none uses the Brier form |
| 3 | Lemma 8.18 (collar lemma, simplified) | **CORRECT**. The single convex-combination estimate is valid at every point of relint F_k |
| 4 | Theorem 8.19(a), (b) and the concave-chart remark | **CORRECT**. One optional strengthening of the remark |
| 5 | Theorem 8.20 and Corollary 8.21 | **CORRECT** |
| 6 | Theorem 8.22 and Appendix A (Prop. A.1, Lemmas A.2–A.10) | **CORRECT**. One wording slip in Lemma A.4(iii), which does not affect the conclusion |
| 6/F3 | C62 Lemma 4.3 when u·c vanishes on an inner half-wall | **GAP in the refereed C62/REF62 proof**: real but closable. **The paper's route avoids it: CORRECT** |
| 7a | F2(a): Theorem 8.19(a), sign and convexity conditions only on U (a.e.) | Proof valid under the weaker hypothesis. **CORRECT** |
| 7b | F2(b): (Reg) only on the open mixed orthants | Proof valid. **CORRECT** |
| 7c | F2(c): Prop. A.1, fan only near ∂D_R∖{0} | Proof valid. **CORRECT** |
| 7d | (unflagged) Theorem 8.22(a) allows an arbitrary positive measurable scale, where DC63 had one scalar per cell | Proof valid. **CORRECT** |
| 8 | Lemma 8.1 and Corollary 8.5, with self-contained proofs | **CORRECT** |
| 9 | Global consistency | **ERROR (scope)** in four sentences: abstract l. 80; §8.4 l. 3470; §8.6 l. 3636–3637 and 3646–3648; open problem (9), l. 3705–3706. The conventions all pass |

There is no mathematical error in any new proof. The required changes are all scope statements.

---

## 1. Theorem 8.14 (convex error levels): CORRECT

**Hypotheses.**
- n = 3, U one-sided, K ⊆ relint Δ, D_K ⊆ U a.e., and (LF).
- The ranking is in 𝒱. (G) is part of Definition 8.7 ("The ranking is assumed to satisfy (G)"), so the REF64_bx 5a error is repaired.
- Convex error levels on an open convex G ⊇ U.
- The conclusion concerns "D_K undominated and the X_kj coherent", and so (via Lemma 8.10) covering and (GC). This matches O61 Theorem B together with the REF64_pc row 9 scope: (a) the interior pari-mutuel triangles, which are not all-crossing; (b) at least two all-crossing vertices.

**Steps checked.**
- **Preliminaries.** A ball lying a.e. in U lies in G: take a reflected pair y, 2x − y ∈ U ⊆ G and use convexity. Hence D_K ∪ (∂D_K∖{0}) ⊆ G, using the open set N of (LF).
- **Step 1.** Lyapunov's theorem on the veto-free models Y ⊆ N_v (integrable ℓ_k). D_K is not strictly dominated, because it pays no veto (Lemma 8.9). Separation gives π ∈ Δ. Then Γ ≤ 0 a.e. on D_K and Γ ≥ 0 a.e. on N_v∖D_K.
- **Step 2.** The ball of Lemma 8.11 lies in G. Continuity on the open sets B∩D_K and B∖C_K gives Γ(r) = 0, since v·(r − ε𝟙) = −ε. Density of relint F_v then gives Γ = 0 on F_v∖{0}.
- **Step 3.**
  - (i) The convex summands add up to 0, so each is affine on relint F_v.
  - (ii) ℓ_j = 0 on B∩{h_j = 0}, by Lemma 8.8 and continuity.
  - (iii) A vertex is exposed, so F_v contains an open piece of v^⊥. L is relatively open in the line V′ = v^⊥∩e_j^⊥, and e_j ∉ ℝv. An affine function vanishing on an interval of V′ is linear with kernel V′, hence equal to −κh_j.
  - (iv) The subgradient at r₀ ∈ L is orthogonal to e_j^⊥, so g = −κ′e_j and ℓ_j ≥ −κ′h_j on G. On F_v near r₀, where h_j takes both signs, κ′ = κ.
- **Step 4.** One slope per world. κ_j > 0 by Lemma 8.8 on U∩{h_j > 0}; this uses (G).
- **Step 5(a).**
  - The vertices are v^k with v^k_i = u_i for i ≠ k (check v^k ∈ K: 1 − Σ_{i≠k}u_i ≤ u_k ⇔ δ ≥ 0).
  - Lemma 4.16 gives F_{v^k} = cone{g^i : i ≠ k}.
  - Every world m ∈ supp π is crossing at some face through each ray g^i. This was checked for all (i, m) in `checks.py`.
  - det(u𝟙ᵀ − I) = 𝟙·u − 1 = δ: exact check PASS.
- **Step 5(b).** On F_v, Γ = −x·h = 0, and F_v spans v^⊥, so x ∈ ℝv. With x ≥ 0 and x ≠ 0 this forces v = w.
- **Remark after the theorem.** The Example 6.7 ranking lies in 𝒱 with G = ℝ³ (−min(h₁, 6h₁) is convex). At p, world 1 is anti-visible, so T is outside (b), and the remark is consistent.

**Flag F4 (optional widening).** The proof of (b) is dimension-free:
- Lemmas 8.8–8.11 and Proposition 2.10 are stated for general n.
- In Step 3(iii), V′ is (n−2)-dimensional in v^⊥, and the same argument applies.
- Steps 4 and 5(b) do not use n.

So (b) holds for every n ≥ 3, and I referee it as such. If the author wants the nearby stronger result, write "Let U … Suppose (a) n = 3 and K is a pari-mutuel model …; or (b) n ≥ 3 and K is a polytope with two vertices at each of which every world is crossing". No proof change is needed.

## 2. Lemmas 8.8–8.11 for 𝒱: CORRECT

- A diff of the block from Definition 8.7 to Theorem 8.12 between `w65build/draft_before_W65.tex` and the new draft shows that only "𝒱_B" became "𝒱" in the statements, plus the split of the definition. The proofs are byte-identical.
- I re-checked that no proof uses ℓ_k = −w h_k:
  - **Lemma 8.8** uses (G) and "ℓ_k ≠ 0 a.e. on Z_k".
  - **Lemma 8.9** uses Lyapunov's theorem and separation on (∫ℓ_k)_{W₀} and (∫φ_{k,κ_k}). Then ℓ_k > 0 a.e. on O′ by Lemma 8.8, and min_K m_{j₀} > 0.
  - **Lemma 8.10** uses only the signs of ℓ_j from Lemma 8.8.
  - **Lemma 8.11** uses Lemmas 8.8 and 8.9, coherence of X_kl and (LF).
- The standing hypotheses of §8.2 (one-sided U, K ⊆ relint Δ, (LF)) are unchanged.

## 3. Lemma 8.18 (collar lemma): CORRECT

**Setting.**
- The hypotheses used are (G), transitivity of ⪯_j, X undominated ⇒ coherent, (LF), and E∩D_R null.
- The case k = j holds because h_j > 0 on F_j∖{0} and E ⊆ {h_j < 0}.
- For k ≠ j, the box lemma (Lemma 8.17, re-checked) makes X = (U∖E)∩{h_k > 0} coherent, X = D_Q a.e.
- The two open sets D_R∩{h_k > 0} and N∩{h_k > 0, h_j > 0} lie a.e. in X, hence in D_Q. A ball inside their convex hull meets E only in a subset of X∩E = ∅, up to a null set.

**The estimate.**
- b = r_i + εr_j and b′ = b − η𝟙 satisfy b′_j, b′_k > 0 and v_k·b′ = −η.
- For p ∈ relint F_k: v_k·p = 0, v_l·p > 0 for l ≠ k, and p_k > 0.
- With A = (x − tb′)/(1 − t), the three displayed bounds are right:
  - v_k·A = (v_k·(x − p) + tη)/(1 − t);
  - v_l·A ≥ (2c − r|v_l|)/(1 − t);
  - A_k ≥ (2c − r)/(1 − t).
- So A ∈ D_R∩{h_k > 0}. This uses R = conv{v_l}, so v_l·A > 0 for all l gives A ∈ D_R.
- No case split on the sign of p_j is needed; this was the point to check.

**Exact test.** For all 6 ordered pairs (k, j), 40 rational points p, and 25 points x ∈ B(p, r) each, with t, c and r chosen exactly as in the proof: 6000/6000 give A ∈ D_R∩{h_k > 0}.

**Collar construction (l. 3122–3130).** C is open, lies a.e. in U, meets every E_t in a null set (Lindelöf), and accumulates at every p ∈ relint F_k. CORRECT.

## 4. Theorem 8.19 and the concave-chart remark: CORRECT

**Reduction.** In case (b), set φ_v = 0 for single-level views, σ_v = −c_v and O = U.
- U is automatically one-sided: if h, −h ∈ U, then 0 ∈ U and U, being open, contains −ε𝟙.
- N = U gives (LF).
- On N′ = (N ∪ D_R)∩O, continuity gives the closed sign conditions, and σ̃_v = 0 where h_j = 0.

**Step 0 (guidance).**
- In (a), the second level is strict, so X ≺_v Y for every view.
- In (b), finiteness and joint strict guidance give one view with a strict level.
- So (G) holds, and each ⪯_j is transitive.

**Step 1.**
- S₀ = ∅ in (a).
- In (b), the argument that σ_v ≥ 0 on U is correct: z = y + ε(y − x) ∈ D_R ⊆ U.
- E_v is a priority region:
  - The first level vanishes on M_{E_v}, and for v ∈ S₀ so does the second.
  - Y∩E_v non-null forces M ≺_v Y.
  - E_v∩D_R is null.
- All vetoes in W₀ and all σ_v with v ∈ S₀ vanish a.e. on D_R ∪ C.

**Step 2.**
- W₀′ ∪ P ≠ ∅.
- The domination argument is correct: views in S₀ tie (no further levels in (b), and S₀ = ∅ in (a)); views in W₀′ and P are strict.
- Separation (Rockafellar 11.3) applies. β ≠ 0, because the empty model would otherwise beat D_R.

**Step 3.** g̃(p) = 0 by squeezing between B_p∩D_R and B_p∖C_R ⊆ C.

**Step 4.**
- Each convex summand is affine on relint F_k.
- For v ∈ P (α_v > 0), φ̃_v vanishes on an open part of each face (h_j > 0), hence on the face.
- For v ∈ W₀′ (β_v > 0), the half-line relint F_k∩{h_j = 0} (s = 3t/2 on F_k = cone{r_i, r_j}) forces σ̃_v = −κ^{(k)}h_j. The constants agree via r_j, since (r_j)_j = −3.
- Exact values: σ̃(r_j) = 3κ and σ̃(r_i) = −2κ. CHECKED.

**Step 5.**
- The system is 3M_i − 2Σ_{j≠i}M_j = 0, with matrix 5I − 2J and eigenvalues {−1, 5} (CHECKED). So M = 0.
- Since β_vκ_v ≥ 0, each κ_v = 0.
- On F_j, σ̃_v is affine and vanishes on the two independent boundary rays, so it vanishes there.

**Step 6.**
- min_R m·(e₁ − e₂) = −1/5 (CHECKED), so the line through x ∈ D_R in direction e₁ − e₂ meets ∂D_R at two nonzero points. Convexity gives f ≤ 0 on D_R.
- f = 0 on D_R∩{h_j < 0}, which is nonempty (r_j + ε𝟙).
- The Step 1 argument gives f = 0 on D_R, so v ∈ S₀: a contradiction.

**Remark after the theorem (l. 3276–3283): CORRECT.**
- (C1) together with continuity of the concave c_j gives weak sign-correctness everywhere on U.
- (C1) gives joint strict guidance.
- (C1)–(C3) with Theorem 3.7 make the undominated models the coherent B_β, and (C4) makes D_R undominated. This contradicts (b).
- *Optional strengthening (nearby result).* The certificate is not needed. For a single-level chart ranking, (G) at world j forces c_j > 0 a.e. on U∩{h_j > 0} and c_j < 0 a.e. on U∩{h_j < 0}: take X = S ⊆ {h_j > 0}, Y = ∅, and the reverse. That is (C1), and it gives weak signs and joint strict guidance as above. So Theorem 8.19(b) gives directly: "no chart ranking with concave positively homogeneous components, on U as in (b), has D_R undominated and every undominated model coherent; in particular none covers R". This is strictly stronger than the remark's certificate statement and needs no new proof.

**TC caveat (l. 3285–3288).** Accurate: transitivity is used only in Lemma 8.17, through Lemma 8.18.

## 5. Theorem 8.20 and Corollary 8.21: CORRECT

**Step 0.**
- Q ⊆ Δ_S, because a.e. h with h_s > 0 on S lies in U_+ ⊆ U and has π·c > 0. This uses (C1) on the positive orthant and the (Reg) bounds on the mixed orthants.
- The sandwich (eq:sandwich) is right: the first set is open and a.e. in D_Q; the last is an open null set, hence empty.

**Step 1.**
- For h ∈ Σ_ij, h ∈ D_{Q_θ} ⇔ ρ_ij > τ(θ), and π·c > 0 ⇔ f_ij > θ.
- The monotone-coupling argument gives f_ij = g_ij∘ρ_ij with g_ij nondecreasing.
- Local Lipschitz continuity follows along y(ρ), since −c_j ≥ A > 0 there.
- The bounds A/B·ρ ≤ g ≤ B/A·ρ hold.

**Step 2 (inverse lemma).**
- {H > y} = (F(y), ∞), {H < y} = (0, F_*(y)), and H∘F = H∘F_* = id.
- There is b with H′(b) ∈ (0, ∞), because H is absolutely continuous and not constant.
- F(y₀) = F_*(y₀) = b, and F′(y₀) = F_*′(y₀) = 1/H′(b). All correct.

**Step 3.**
- π·c = (−c_j)(a g_ij(s) + g_kj(t) − θ) (identity CHECKED).
- D_Q depends only on coordinates i, j, k (Q ⊆ Δ_{ijk}) and is a cone, so membership of h depends only on (s, t).
- S₁ = S₂: a square below a point of S₂∖S₁ gives an open set inside D_Q with π·c ≤ 0.
- The strict epigraph of φ_a is convex, so φ_a is convex. For fixed s and small a, θ − a g(s) > 0, so the extension F = 0 is never used in the limit.
- The limit −F′(θ)g_ij is convex, so g_ij is concave.

**Step 4.** Symmetric, with ψ_ij(S) = 1/g_ij(1/S) (identity CHECKED) and squares above. The strict hypograph is convex, so φ̂_a is concave on I_a = (0, S_a). In the limit, ψ_ij is convex. Since I_a increases to (0, ∞), the three-point concavity inequalities pass to the limit.

**Step 5.**
- Concavity and g(ε) > 0 give g(ρ)/ρ nonincreasing.
- Convexity and ψ(ε) → 0 give ψ(S)/S nondecreasing, that is, g(ρ)/ρ nondecreasing.
- So g = κρ.

**Step 6.**
- r_i = κ_ij r_j gives c = r_{j₀} d_σ ⊙ h.
- Two open convex sets that agree a.e. are equal (Rockafellar 6.3).
- Hence orthant-planarity in the sense of Definition 5.1.

**Remarks on Theorem 8.20.**
- (C2) is not used. Homogeneity of the modified c^σ is not needed either; Step 1 derives 0-homogeneity of f_ij.
- After the a.e. modification, c must be defined on all of σ. Since σ ⊆ U a.e., this is a harmless enlargement of U by a null set. A half-clause would make it explicit; optional.

**Corollary 8.21.**
- (C1) gives (SC), hence (G) by Lemma 3.2.
- B_{e_i} = U∩{h_i > 0} a.e., which is coherent by (C3).
- K ⊆ relint Δ meets no edge. Theorem 2.9 gives U_+ ⊆ U a.e.
- Theorem 8.20 then applies.
- The pari-mutuel example: the normals u_i𝟙 − e_i have no zero coordinate, so Lemma 5.5(d) applies (the models are full-dimensional). CORRECT.

## 6. Theorem 8.22 and Appendix A: CORRECT

**Normalisation (l. 3718).** B_π(π*⊙c) = B_{π⊙π*}(c). Neighbourhoods, (C1)–(C4) and the PL and direction-continuity structure are all preserved. CORRECT.

**Cells near a point.** T_σ ⊇ ℝw, because σ is a cone containing w. The tangent cones cover ℝ³ with disjoint interiors. CORRECT.

**Lemma A.2.** CORRECT: the convex hull of two balls contains a ball around each point of the open segment.

**Lemma A.3 (kink test).** CORRECT.
- q·c′ = max(f⁺, f⁻) on B.
- Independence uses f⁺ ≠ 0 on n^⊥ and q·d > 0.
- The witness values are q·c′(x₀ ± 2ηz) = η > 0 > −η = q·c′(x₀). CHECKED exactly on random instances.

**Lemma A.4.**
- The opening paragraph uses (C4), (C2) at 𝟙 and (Bdelta). Then (i), (ii) (both midpoint constructions) and (v) are CORRECT. In (v), 0 ∉ V, since V is open and contains no nonzero h ≤ 0.
- (iii), rank-1 case: **wording slip (minor).**
  - "a has constant sign on the convex set int σ, where M_σh ≠ 0": the hypothesis gives M_σh ≠ 0 only on V∩int σ, and int σ need not lie in V.
  - Repair: replace "int σ" by "int σ∩B(w, ρ_w), which is convex and lies in V". Alternatively, note that 𝟙·p = 0 makes 𝟙·δ = 0 on V∩int σ whichever sign a takes there.
  - The conclusion is unaffected.
- (iv): CORRECT. Rank ≤ 1 together with (iii) gives a constant direction along w + ru, and v_k·(w + ru) ≠ 0 contradicts (ii).

**Runs and junctions (l. 3851–3865).** CORRECT.
- A non-regular point lies on a 2-face of some cell whose span is not v_k^⊥. That plane meets v_k^⊥ in a line, so there are finitely many junction rays.
- σ^±_I are locally constant on the connected run I.
- L_I ≠ 0 on I by (iii).

**Lemma A.5.** CORRECT (the midpoint trick forces λ = μ).

**Coordinates at a junction.**
- The angular description is right.
- σ₁ = σ⁺_{I₁}, σ_m = σ⁺_{I₂}, τ₁ = σ⁻_{I₁} and τ_{m′} = σ⁻_{I₂}.
- With n_j·u_j = 0, n_j·h = (n_j·e)·sin(θ_j − θ)/sin θ_j. So σ_j lies on the side n_j·h ≥ 0, and the outer side is analogous. Verified.

**Lemma A.6.** CORRECT.
- In the rescaling step, consecutive cells have rank 2 on P: off the facet by (iv), on the facet by hypothesis and the remark.
- The holonomy around w is 1, because M_σw ≠ 0.
- c′ is continuous and has the direction of δ everywhere on Y.
- In the kink test, a_j = 𝟙·M′_{σ_j}u_j > 0 **strictly**, because w + ru_j ∈ B_w∩D_R and Lemma A.4(ii) gives 𝟙·c′ > 0 there. The zero of q_t·c′ along the wall is therefore at r_t = O(t).
- The two consequences and the comparison are right; the telescoping sums at e use n_j·e > 0.

**Lemma A.7.** CORRECT.
- α > 0 and β > 0, both from (ii).
- The witness points satisfy q·M_τP₂ = c_tS(β + tγ′)/2 > 0 and q·M_τZ = −c_tS(β + tγ′)/8 < 0 (CHECKED exactly), and Z is the midpoint of P₁ and P₂ (CHECKED).
- σ_m ≠ τ₁, because a convex sector cannot span angles just below π and just below 2π.

**Lemma A.8.** CORRECT.
- Ranks never alternate.
- If all runs have rank 1, then p = 0, from two crossing coordinates and 𝟙·p = 0.
- If all have rank 2, continuity at junctions and at the boundary rays (which lie in V) applies.

**Lemma A.9.** CORRECT. δ_i(w_ik) = 0 by the sign change, and λ_ik > 0 by Lemma A.8 at w_jk.

**Corner system.** CHECKED directly at all three rays, not only by symmetry.
- The determinants are 3(3l₁₂l₁₃ − 2l₁₂l₂₃ − 2l₁₃l₃₂), 3(2l₁₃l₂₁ − 3l₂₁l₂₃ + 2l₂₃l₃₁) and −3(2l₁₂l₃₁ + 2l₂₁l₃₂ − 3l₃₁l₃₂). These are equivalent to a + 1/c, b + 1/a and c + 1/b each equal to 3/2.
- T³(x) = (3x − 10)/(10x − 12), which leads to 2x² − 3x + 2 = 0 with discriminant −7. CHECKED.

**Lemma A.10.** CORRECT.
- G is well defined, continuous, homogeneous and w-invariant.
- The claim (P agrees a.e. with an open convex cone T, so conv(P_H)∖P_H is null) is right. So is the dichotomy: Z is null, or Z contains a closed arc of length ≥ π.
- On the segment from e_l to 𝟙: Z(e_l) is null by (C1). Z(𝟙) contains an open semicircle, since v_l ∈ H∖{0}. Then s₀ > 0, the limit arc exists, and affinity in s gives a non-null tie at π(s₀), which contradicts (C2).
- The reduction V′ = {c ≠ 0} ⊇ ∂D_R∖{0} and δ = c/|c| fits Proposition A.1 exactly. This is where F2(c) is needed.

### F3: the "valley" in C62 Lemma 4.3

**Verdict.** It is a real GAP in the written C62 proof as repaired by REF62_corner. It is closable within C62's hypotheses. The paper's route does not depend on it and is CORRECT.

- **Where the gap is.**
  - C62's proof says, at q = u + tδ, that "f_q > 0 along W at distance ≫ t, so the zero set of f_q crosses W at distance O(t)". REF62's repair step 1 ("the kink test at q = u + tδ … gives u·d_j ≤ 0 for every inner half-wall") uses the same premise.
  - The premise needs u·c > 0 on the inner half-wall near w. (C4) and (C2) at u give u·c > 0 only a.e. on D_K, and a half-wall is null.
  - On a wall adjacent to a facet sector, u·c = αv_k·h > 0, so the premise holds there. But REF62 itself notes that middle sectors exist (`alpha_jump.out`). On a wall between two middle sectors, nothing in C62 or REF62 excludes u·c = 0.
- **The configuration is locally consistent with everything except (C3) near u** (`checks.py` §8). At w ∈ relint F₃:
  - Take g = 𝟙·c = min(r, |s|) for r > 0 and g = r for r < 0, in the coordinates h = (1+α)w + se + r𝟙, and c = (g/3)𝟙 + (1+α)p with p ∈ 𝟙^⊥∖{0}. This is continuous PL with c(w) = p ≠ 0. (C1) holds near w with w = (−1, −1, 4) and p = (−1, −1, 2). (C4) and (C2) at u hold locally.
  - The inner kinks have 𝟙·d_j = (−1, 2, −1). REF62's step 1 would assert that all are ≤ 0, which is false at the middle (valley) wall.
  - There q_t·c(w + ru) = tω·p for every r, so the kink test has no zero crossing at all.
  - The step therefore has no justification in this case.
- **Repair of the C62 proof.**
  - Insert the strict-sign lemma before the kink test: DC63 4.2-D(b), equivalently the paper's Lemma A.4(ii) applied to δ = c/|c|.
  - c(w) ≠ 0 by C62 Lemma 4.2, so c ≠ 0 near w and δ is continuous there.
  - Then u·c > 0 everywhere on D_K near w, so a_j > 0 and the O(t) crossing exists. Valleys are thus excluded by (C3) near u through the convexity test.
  - Statement and verdict of C62 Thm 4.1: unchanged. The proof verdict becomes "CORRECT WITH TWO REPAIRS".
  - Results refereed "given C62 Thm 4.1 as repaired by REF62" (e.g. IN63 Theorem S, REF63_neg) need the same one-line insertion. This should go in the round log.
- **The paper's route.**
  - Part (b) is reduced to Proposition A.1 by Lemma A.10.
  - Inside A.1, Lemma A.6 derives a_j > 0 from Lemma A.4(ii) explicitly (l. 3943–3945), and Lemma A.7 derives α, β > 0 the same way.
  - Lemma A.4(ii) (DC63 4.2-D(b), REF63_neg CORRECT) needs (C4), (C2) at 𝟙 and (C3) near 𝟙, all of which the paper assumes.
  - So W65's reading is right, and no change to the paper is needed.

## 7. Weaker hypotheses (flag F2 and one unflagged case)

- **(a) Theorem 8.19(a): CORRECT under the weaker hypothesis.**
  - The proof uses the sign conditions only in three places: in Step 0 (on X△Y ⊆ U), in the priority regions (subsets of U), and in the closed sign facts on N′. N′ is open and lies a.e. in U∩O; there an a.e. condition on U plus continuity of the convex representatives suffices.
  - Convexity is used only for σ̃_v and φ̃_v on O, and equality with σ_v and φ_v only a.e. on N′ ⊆ U∩O. In Step 6, the equality σ_v = σ̃_v is used a.e. on D_R ⊆ U∩O.
  - No restatement is needed.
  - Also unused: one-sidedness of U in (a). Only D_R ⊆ U a.e. and (LF) enter. It is harmless to keep.
- **(b) (Reg) on the open mixed orthants: CORRECT.**
  - Lipschitz continuity enters only through continuity of c on each open mixed orthant (the sandwich) and local Lipschitz continuity of g_ij along a curve inside one open mixed orthant (Step 2).
  - The bounds are used only on open mixed orthants.
  - Closed orthants are never used. No restatement is needed.
- **(c) Proposition A.1, fan near ∂D_R∖{0} only: CORRECT.**
  - Every argument in A.2–A.9 and the corner system is local at points of ∂D_R∖{0}: the balls B_w, the junctions, F_k and the rays r_j.
  - (Bdelta) is used only on V′.
  - This weakening is what allows V′ = {c ≠ 0} in part (b). No restatement is needed.
- **(d) Unflagged: in Theorem 8.22(a), c need only be a positive measurable multiple of δ a.e.**
  - DC63 had one scalar per cell, so this is strictly more general.
  - Every step goes through B_π, which depends only on δ by (Bdelta).
  - CORRECT; worth one clause in W65_changes for transparency.
  - Also unused in Theorem 8.22: convexity and one-sidedness of U, beyond V ⊆ U (as DC63 noted). Harmless.

## 8. Lemma 8.1 and Corollary 8.5: CORRECT

**Lemma 8.1.**
- B̃ is closed, convex and bounded (y_i ≤ φ(e_i) and −y_i ≤ φ(−e_i)).
- The epigraph is closed with interior {t > φ}, and the supporting hyperplane is given by Rockafellar 11.6.
- s > 0: if s = 0, then y·h ≤ y·h₀ for all h, so y = 0.
- Scaling h ↦ λh gives y ∈ B̃, and λ → 0 gives y·h₀ ≥ φ(h₀). Hence φ is the support function of B̃.
- 0 ∈ B by strict separation and φ ≥ 0.
- B ⊆ V*, with cl V = {k·h ≥ 0 on K'', h_i ≥ 0} = Q*. Q = ℝ₊conv(K''∪{e_i}) is closed (the convex hull is compact and avoids 0). The bipolar theorem gives B ⊆ Q.
- The replacement of Rockafellar 13.2 is sound.

**Corollary 8.5.**
- *Vertex criterion.* The solutions of the active equalities form v + L with L = span(𝟙, active g_f)^⊥. If d ∈ L∖{0}, then v ± εd ∈ P. If L = {0}, the midpoint argument applies. Correct.
- *(a)* The span of 𝟙 and u_i𝟙 − e_i (i ∈ H) equals the span of 𝟙 and e_i (i ∈ H), so |H| ≥ n − 1 ≥ 2. The normals are negative exactly at i. Correct.
- *(b)*
  - K ⊆ relint Δ.
  - g^{ij} is negative exactly at i.
  - At w^H the active constraints are exactly those with i ∈ H and j ∉ H; the others are strict because k > 1.
  - Equalities force common ratios, hence a vertex.
  - |H| ≥ 2 gives non-visibility, and there are 2ⁿ − n − 2 such sets.
  - Exact vertex enumeration (`checks.py` §2): n = 3 gives 6 vertices, 3 not visible; n = 4 gives 14 vertices, 10 not visible. Both match.

## 9. Global consistency

**Conventions: PASS.**
- No optional names on theorem-like environments.
- No `:=` or `=:`.
- No commentary comparing drafts (grep for previous/earlier/now/no longer/recorded/without proof/replaced: only mathematical uses).
- "Models" is used throughout.
- No leftover (DF), (ND) or Gâteaux material.

**Pari-mutuel permissibility: PASS.**
- §8.6 ends: "nothing here says that pari-mutuel models are impermissible as coherent models".
- The introduction (l. 155–158) and the §8 opening (l. 2583) disclaim uncoverability.
- No sentence suggests impermissibility.

**Scope: four ERRORs, each a statement broader than what is proved.**

- **(S1) Abstract, l. 80: "and piecewise-linear single charts on one-sided cones".** Overstated in three ways:
  - Theorem 8.22 excludes only *continuous* or *direction-continuous* PL charts. Charts that jump, for example at the corner rays, are not excluded; DC63 §6 records this as open.
  - It excludes them only from the *four-condition certificate*, not from coverage by chart rankings (l. 3306–3307 say so).
  - It applies only to R.

  Likewise "regular single charts …" is a certificate exclusion.
- **(S2) §8.4, l. 3470: "On one-sided domains, piecewise-linear charts cannot meet the four-condition certificate for the reversed triangle."** Same over-breadth. In addition, the theorem's domains are open convex cones containing C_R∖{0} and no nonzero h ≤ 0, not all one-sided domains.
- **(S3) §8.6, l. 3636–3637: "The reversed triangle … lies in the scope of every exclusion above."** False. R is not in the scope of:
  - Theorem 8.14(b): at each v_k, world k is anti-visible;
  - Corollary 8.5(b) (not a density-ratio class) or 8.5(c);
  - Proposition 8.6 and Proposition 8.27 (R is not a contamination);
  - Corollary 8.26 (R's edge lines m_i = 2/5 are not cevian).
- **(S4) §8.6, l. 3646–3648 (escape list) and open problem (9), l. 3705–3706.**
  - The escape list "a chart outside the classes of Theorems 8.20 and 8.22 and of the remark after Theorem 8.19" suggests that charts inside those classes cannot cover. Theorems 8.20 and 8.22 exclude only the certificate. A chart ranking with non-null ties (failing (C2)) is not covered by them. The concave case is excluded outright by Theorem 8.19(b); see item 4.
  - Open problem (9), "cannot be piecewise linear, continuous or direction-continuous", reads as "cannot be continuous". It should name the two PL classes.

**Minor.**
- Open problem (7), l. 3697–3698: "no regular chart meeting the four-condition certificate covers them there" is vacuous in form, since such charts do not exist.
- Appendix numbering: subsections A.4 ("The corner system") and A.5 ("Part (b)") share numbers with Lemmas A.4 and A.5. W65_changes itself writes "App. A.5 (Lemma A.10)". Use unnumbered subsections, or refer to them only by name.

---

## Ranked list of required changes

1. **(S2) §8.4, l. 3470.** Replace with: "On open convex cones that contain C_R∖{0} and no nonzero h ≤ 0, charts that are continuous piecewise-linear, or direction-continuous piecewise-linear, near C_R∖{0} cannot meet the four-condition certificate for the reversed triangle."
2. **(S1) Abstract, l. 79–81.** Replace "regular single charts on domains that are not essentially one-sided, and piecewise-linear single charts on one-sided cones" with: "and, for the certificate of single-chart coverage, regular charts on domains that are not essentially one-sided and continuous or direction-continuous piecewise-linear charts on one-sided cones". Optionally add "for the reversed triangle and other pari-mutuel models" after "exclusions".
3. **(S3) §8.6, l. 3636–3637.** Replace "and lies in the scope of every exclusion above" with: "The exclusions that apply to it are Corollary 8.5(a), Theorem 8.12 with Corollary 8.13, Theorem 8.14(a), Theorem 8.19 and the remark after it, Corollary 8.21, Theorem 8.22, and Corollaries 8.24 and 8.25."
4. **(S4a) §8.6, l. 3646–3648.** Replace "or by being additive with a chart outside the classes of Theorems 8.20 and 8.22 and of the remark after Theorem 8.19" with: "or by being additive with a chart that does not meet the four-condition certificate (Theorems 8.20 and 8.22 concern the certificate, not coverage by chart rankings in general), or that meets it but lies outside the classes of those theorems".
5. **(S4b) Open problem (9), l. 3705–3706.** Replace "cannot be piecewise linear, continuous or direction-continuous" with "cannot be continuous piecewise-linear or direction-continuous piecewise-linear near C_R∖{0}".
6. **Lemma A.4(iii), l. 3836.** Replace "constant sign on the convex set int σ" with "constant sign on the convex set int σ∩B(w, ρ_w) ⊆ V". In the next line, read "δ ≡ p/|p| on int σ∩B(w, ρ_w)" and "𝟙·δ = 0 on int σ∩B(w, ρ_w)".

### Recommended (not required)

7. **Record F3 in the round log.** C62 Lemma 4.3 (REF62_corner: CORRECT WITH REPAIR) needs a second repair: the strict-sign step (DC63 4.2-D(b)) before the kink test, to exclude valleys on middle inner half-walls. Results that cite "C62 Thm 4.1 as repaired by REF62" inherit this one-line fix. The paper is unaffected.
8. **F4.** State Theorem 8.14(b) for every n ≥ 3. The proof is verbatim and was refereed here for general n.
9. **Strengthen the remark after Theorem 8.19.** No chart ranking with concave positively homogeneous components, on U as in (b), covers R or even has D_R undominated with (GC). (G) gives (C1), and Theorem 8.19(b) applies without (C2)–(C4). Open problem (9) can then say this.
10. **Open problem (7).** Write "no chart satisfying (Reg) meets the four-condition certificate for them there".
11. **Appendix subsection numbering clash.** Make the subsections unnumbered.
12. **W65_changes.** Add the unflagged generalisation 7(d) (arbitrary measurable scale in Theorem 8.22(a)) to F2, and note that one-sidedness of U is unused in Theorems 8.19(a) and 8.22.
13. **Theorem 8.20, proof l. 3326.** Add "(enlarging U by a null set if necessary)" after "we may assume c = c^σ on every mixed orthant".

## Files
- `ref65paper_py/checks.py` and `checks.out`: exact checks (sympy and fractions). All PASS.
- `ref65paper_py/build/`: an independent clean compile (p.tex is a copy of the draft).
