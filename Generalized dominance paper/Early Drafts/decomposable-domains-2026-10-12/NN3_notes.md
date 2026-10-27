# NN3 (round 42, BRIEF34). Referee of MM1 and MM2 under the audit's corrected scopes, and one four-judge test with smooth flat switch functions

18 Oct 2026. Independent referee. Rules of BRIEF13 and BRIEF34; all scope corrections of AUDIT_MM are adopted. Labels:
- **PROVED**: argument written or re-derived here line by line (one reader, me).
- **CHECKED**: exact computation in `nn3py/flat_design_check.py` → `nn3py/flat_design_check.out` (Fractions and sympy rationals; ends `ALL CHECKS PASSED`; run `python3 -I flat_design_check.py` inside `nn3py/`).
- **CONJECTURE**, **NUMERICS**: none used.

No assumption is added. Every hypothesis belongs to the result that states it. Setting: write-up §2; three worlds; μ standard Gaussian; T1 = D_K, K = (1−ε)u + εΔ, c₀ = (1−ε)/3, v_k = c₀𝟙 + εe_k; n judges per world, quorum q; a branch picks n−q+1 judges at each active world. "Switch value" σ_iv(g) := ℓ_iv(pair of g, silence) − ℓ_iv(pair of g, accept g only), for oriented g (MM1 §1.1; MM2's c_iv).

---

## 0. Verdicts

| Item | Verdict | Hypotheses actually used |
|---|---|---|
| MM1 Lemma 1.1 (switch-value reduction) + realisation | **Correct** | full domain; (b) uses that ∂D_K is null |
| MM1 Lemma 1.2 (QS ⇒ weak Bayes per branch), 1.3, 1.4 | **Correct** | Lyapunov, decomposability; weak only |
| MM1 Prop 2.1 (analytic judges) | **Correct as stated** (strict certificates in (a); weak Bayes ⇒ Σασ ≡ 0 in (b)) | K two-dimensional; analyticity of the branch's switch values near ONE point of the corner ray; no family |
| — new: Prop A below | closes the audit's weak-vs-strict gap **for analytic branches**: (QS) alone fails | as Prop 2.1, plus records near that point |
| MM1 Lemma 3.1 (pair-Helly) | **Correct** (two-generator cones only) | minor remark on distinct half-spaces |
| MM1 Prop 3.2 (proportional pairs) | **Correct modulo the FF2 Thm 4.1 import chain**; hypothesis can be weakened (§1.4) | GLOBAL proportionality on {+,0,−}; full domain; continuity; T1 selected |
| MM1 Thm 4.1 / Thm 4.2 (min-cell form) | **Correct, self-contained** | exact form σ = κ_iv(M_k)g_i on N ⊇ ∂D_T1; weak Bayes in all branches; continuity; triangle shape near T1 is DERIVED |
| MM1 Prop 5.1 (rank two) | **Correct with a one-line repair** (proportionality of switch values suffices for Prop 3.2) | dim R(C) ≤ 1 at one p; global rank-2 structure |
| MM2 Lemma 1.1 (branch form) | **Correct** | only \|F_i\| = n−q+1 |
| MM2 Thm 3.1 (alignment) | **Correct** | weak Bayes only |
| MM2 Lemma 3.2 (sign support) | **Correct with repair**: needs y_iv ≠ 0 on F | — |
| MM2 Lemma 3.3 (dimension ≥ 3) and the "≥ 8 supports" count | **Correct**; the count inherits the Lemma 3.2 repair | q ≥ 3 |
| MM2 Prop 4.1 (multi-site swap), Prop 4.3 (exhaustion) | **Correct**; the reading "local method exhausted" holds only when an aligned w_F is strictly signed off the boundary | atomlessness, decomposability |
| MM2 Cor 4.2 (generic judges fail at T1) | **Correct** | (QS) at T1's index; (LF) |
| MM2 Thm 5.1 (world-separable) | **Correct** on the full domain and on every decomposable domain with (LF) at T1 | weak Bayes at T1 for one mixture |
| MM2 Thm 6.4, Cor 6.5 (edge identities) | **Correct with a null-set repair**; a.e. plane, a.e. point, type c or d by imprecise/precise edge model | full domain; continuity on the closed edge |
| **Part B** (4 judges, q = 3, smooth flat) | MM1's analytic obstruction does **not** apply (PROVED). The smooth flat test design is nevertheless killed, by Thm 4.2 transported through a change of measure (PROVED) and independently by MM2's edge identities (PROVED; CHECKED). Shape change cannot help in that class. Genuinely heterogeneous flat designs: **open**, with new necessary conditions (Prop A(a), Cor A.2). | |

---

## 1. MM1

### 1.1 Switch-value reduction (Lemma 1.1, realisation, Lemmas 1.2–1.4). Correct.

- **Realisation.** For h_i > 0: σ(h) > 0, so ℓ(+) = −σ(h) < 0 = ℓ(0); σ(−h) < 0, so ℓ(−) = −σ(−h) > 0; ℓ(×) exceeds both. The order is + < 0 < − < ×, the world-i rank order. Symmetrically for h_i < 0. The envelope is at most sup|σ| + |h_i| + 1, Gaussian-integrable. ✓ (The same construction works for unbounded σ with an integrable envelope, e.g. MM1's degree-one monomials.)
- **(a).** Mixture values on the pair of g: 0 (silence), −Σασ(g) (accept g), −Σασ(−g) (accept −g), and × strictly worst for every nonzero α ≥ 0. Unique minimiser "accept g" ⟺ Σσ(g) > 0 and Σσ(g) > Σσ(−g); unique minimiser silence ⟺ Σσ(±g) < 0. ✓ Pointwise uniqueness a.e. ⟺ unique minimiser over models, by decomposability. ✓
- **(b).** P_K(g) > 0 ⇒ P_K(−g) = −P̄_K(g) ≤ −P_K(g) < 0. Silent pairs have P_K(±g) ≤ 0, and {P_K = 0} is null (LL1 Lemma 4.2a, refereed in MM3). ✓
- **(c)** weak version ✓. **Lemma 1.2** is the η = 0 case of LL2 Lemma 2.1 (refereed in MM3 §2.2): Lyapunov convexity, missing the open negative orthant because at most n − |F_i| = q − 1 judges could strictly prefer C_p, separation, pointwise form. ✓ It yields **weak** Bayes only.
- **Lemma 1.3** ✓. **Lemma 1.4** ✓: g = (1,1,−t) with t slightly above 2c₀/(c₀+ε) has v₃·g < 0, and −g has v₁·(−g) = −2c₀ − ε + c₀t < 0; so T1 is silent on an open set where accept is strictly better at worlds 1, 2.

### 1.2 Proposition 2.1 (real-analytic judges). Correct as stated.

Checked line by line.
- **Local picture.** At a point x₀ of a corner ray between facets with normals n₁ ≠ n₂ (both corners of K, i.e. with normal cones of positive angle), a neighbourhood of x₀ is covered by the two normal cones, so P_K(x₀ + y) = min(n₁·y, n₂·y) for small y. Outside cl D_K the pair is silent because P̄_K(x₀) > 0 when K spans the plane Σ = 1. ✓
- **Taylor step.** With Φ(x₀ + ty) = t^k P_k(y) + O(t^{k+1}) uniformly on |y| ≤ 1: P_k ≥ 0 on W, ≤ 0 off cl W. Even k: P_k = 0 on −W. Odd k: P_k = 0 on S = {n₁·y > 0 > n₂·y}, nonempty because n₁, n₂ are distinct points of the simplex, hence not parallel. ✓
- **Scope (audit correction 2 confirmed).** (a) concerns **strict** certificates; (b) says only that a **weak** Bayes mixture vanishes identically near the ray. The proof uses analyticity at one point x₀ of the ray, not along the ray, and nothing about any other selected model.

**The weak-versus-strict gap can be closed for analytic branches.** The following is new.

**Proposition A (PROVED).** Let C = C_p = D_K with K two-dimensional, x₀ a point of a corner ray of D_K, and F a branch at p. Let B be a ball around x₀ with B ∩ (−B) = ∅, inside the (LF) neighbourhood (automatic on the full domain), small enough that D_K ∩ B = (x₀ + W) ∩ B.

(a) *(C^∞ case.)* Suppose the σ_iv, (i,v) ∈ F, are C^∞ on B. Let β ∈ ℝ^F (any signs) satisfy β·σ_F ≥ 0 a.e. on B ∩ D_K and ≤ 0 a.e. on B ∖ cl D_K. Then β·σ_F is **flat** at x₀ (all derivatives vanish). In particular, under (QS) the weak-Bayes weight w_F of Lemma 1.2 has w_F·σ_F flat at x₀.

(b) *(Common factor times analytic.)* Suppose that on B, σ_iv = m·a_iv for all (i,v) ∈ F, where m is measurable, bounded, positive a.e. (common to the judges of F), and each a_iv is real-analytic on B. Then (NT_F) fails at p, so **(QS) fails at p**. No certificate, strict or weak, is involved.

*Proof.* (a) If β·σ_F were not flat, the Taylor argument of Prop 2.1 Step 2 applies verbatim to its lowest nonzero homogeneous term (it never uses the sign of β). (b) Put τ(g) := a_F(g) for g ∈ B ∩ D_K and τ(g) := −a_F(g) for g ∈ B ∖ cl D_K, and S := span a_F(B ∖ ∂D_K) ⊆ ℝ^F. S ≠ {0}, since σ_iv ≠ 0 a.e. and m > 0 a.e.
1. *The cone of τ-values is all of S.* Let V := τ(B ∖ ∂D_K). If cone(V) ≠ S, then (a convex cone dense in a subspace equals it) cl cone(V) ≠ S, so there is β ∈ S ∖ {0} with β·v ≥ 0 on V, i.e. β·a_F ≥ 0 on B ∩ D_K and ≤ 0 on B ∖ cl D_K. Prop 2.1's Taylor argument at x₀ gives β·a_F ≡ 0 near x₀, hence on the ball B by analyticity, hence β ⊥ S, so β = 0. Contradiction.
2. *A finite positively spanning set.* Choose points g₁, …, g_r ∈ B ∖ ∂D_K whose values τ(g_j) positively span S. Then 0 lies in the interior, relative to S, of co{τ(g_j)}; otherwise some nonzero β ∈ S has β·τ(g_j) ≥ 0 for all j.
3. *Averages.* Let B_j be disjoint balls of radius ρ around g_j, each on one side of ∂D_K, and u_j := ∫_{B_j} m τ dμ / ∫_{B_j} m dμ ∈ S. As ρ → 0, u_j → τ(g_j) (continuity of a, m ≥ 0 with positive integral). Relative interiority is stable under small perturbation inside S, so for small ρ, 0 = Σ_j θ_j u_j with all θ_j > 0.
4. *Exact record.* By Lyapunov's theorem for the atomless vector measure E ↦ (∫_E m τ dμ, ∫_E m dμ) on B_j, there is E_j ⊆ B_j with ∫_{E_j} m τ dμ = c θ_j u_j for any small c > 0. Let X switch C on E_j: accept g → silence if g_j ∈ D_K, silence → accept g otherwise. X is evaluable (full domain or (LF)), X ≠ C, and for (i,v) ∈ F, Δ_iv(p, X) = Σ_j ∫_{E_j} m τ_iv dμ = c Σ_j θ_j u_{j,iv} = 0. So Δ_iv ≤ 0 on all of F with X ≠ C: (NT_F) fails, and by MM2 Lemma 1.1 (QS) fails. ∎

**Corollary A.2 (PROVED).** If (QS) holds at p and C_p has a corner point x₀ as above, then some active world has at least q judges that are not real-analytic at x₀. (Otherwise pick n−q+1 analytic judges at every active world and apply Prop A(b) with m ≡ 1.) For T1 this must hold at every point of all three corner rays. For (n, q) = (7, 5): at least 5 of 7.

So the audit's correction 2 stands for MM1 as written, and Prop A supplies the missing argument for the analytic class. Prop A(b) does **not** extend to general C^∞ judges: F(x,y) = h(x)h(y) − h(−x) − h(−y) is a smooth strict certificate of a wedge (§4.1).

**Corollary 2.2, Lemma 2.3, Corollary 2.4.** Correct. The sweep p^{−1}⊙r₁₂ ∝ (−a, −b, c) at p ∝ (1/a, 1/b, (κ+1)/c) is right. Cor 2.2 concerns **the plain posterior family**, a construction choice: its moving corners are assumed, not derived. Under Prop A, Cor 2.2's last bullet and Cor 2.4 hold under (QS) alone, not only for certificates.

### 1.3 Lemma 3.1 (pair-Helly). Correct.

- Step 1: if X = σ₁^{P₁} ∩ σ₂^{P₂} were a ray, every triple intersection would lie in it, forcing that ray into all six world-3 cones. So every X is two-dimensional and all eight vectors of worlds 1, 2 lie in one plane L. The strict inequalities come from nondegenerate overlaps. ✓ *Remark.* The statement allows different half-spaces H_i. The interval argument still works: each world's rays span an arc < π, the two arcs overlap, so their union is an arc < 2π and admits one angular coordinate without wrap-around. In every application the half-space is common anyway (positive vectors).
- Step 2: cone(a₁,a₂) ∩ cone(a₁,a₃) = ray(a₁) for independent a₁, a₂, a₃; then z ∈ cone(a₂,a₃) contradicts independence. In the plane, [x(1),x(2)] ∩ [x(3),x(4)] ≠ ∅ forces x(2) = x(3). ✓
- Step 3 ✓. The lemma is about **two-generator** cones; Step 1's "non-ray intersection ⇒ common plane" fails for three generators (MM1 Remark 3.3 correctly declines). Remark 3.3's counting 2(n−q+1) ≤ n under 3q > 2n is right (checked n ≤ 5 by inspection; n ≥ 6 by 2q > 4n/3 ≥ n+2). The q = n−1 extension (pairs, n ≥ 4) is right.

### 1.4 Proposition 3.2 (proportional pairs) and its imports. Correct modulo the import chain; hypothesis weakens.

- Steps 1–2 ✓: in branch F* the weak-Bayes mixture equals Σ_i(α_iv + ρ_iα_iw)ℓ_iv up to advice-constant terms, with weights not all zero and supported in supp p.
- **Interface with FF2 Thm 4.1.** I checked that FF2 Steps 2–6 use exactly: W(q) ∩ Δ_{supp q} ≠ ∅ for every q (the Step 1 output); continuity in measure (Step 2); (H2) for the field (Step 4); T1 = C_{q₀} (Step 5); and the full domain (Step 6). Prop 3.2 supplies all of these with ℓ* = (ℓ_{1v₁}, ℓ_{2v₂}, ℓ_{3v₃}). Step 6 imports D1, BB2 Thm 6.1 and M3.7–3.8, each refereed once (GG3 item 8 records FF2 Thm 4.1 as correct modulo this chain). I did not re-referee those imports.
- **Repair/strengthening (PROVED).** Proportionality is needed only on {+, 0, −}, i.e. σ_iw = ρ_iσ_iv for both orientations of a.e. pair. Coherent C_p never gives ×, and for b = × every strictly guiding nonzero mixture already has β·(ℓ*(×) − ℓ*(a_{C_p})) > 0. So weak Bayes for ℓ* at all advices follows.
- **Scope.** The proportionality must be **global** (a.e. pair). Local proportionality, such as on pinned cells (Thm 4.1, Cor 4.3) or at the jets of one point, does not feed this chain: off the region the branch mixture depends on the ratio α_iv : α_iw, which may vary with p, so no fixed field ℓ* exists. MM1 does not make that inference in any theorem; the "quorum collapses to one field" sentences of MM1 §0 and §6 are readings and are local only.

### 1.5 Theorems 4.1 and 4.2 (min-cell form). Correct; self-contained.

- **Thm 4.1.** On a pinned cell the weak-Bayes inequalities give ω^Q·g = 0 on ∂D_K ∩ Q ∩ N. Since κ > 0 and α ≠ 0, ω^Q ≠ 0, so this piece is planar and ω^Q = d_Q n^Q with d_Q > 0. The normal n^Q lies in K: a minimiser m₀ at a relative-interior point of the piece satisfies m₀·g ≥ 0 on a planar neighbourhood with equality at the point, so m₀ ⊥ plane. If a cell carried pieces with two normals, the hypothesis would fail, so the theorem holds vacuously there. Reduction to Lemma 3.1 with generators A_i^{−1}κ_iv|_P > 0 ✓. A positive diagonal map preserves betweenness of rays ✓.
- **Thm 4.2.** Step 1 ✓, including: ∂D_K ∩ M_k ⊂ (ω^k)^⊥ at every boundary point (both sides lie in the open cell); walls carry no 2-D boundary piece (normal ∝ e_k − e_j ∉ ℝ₊K); n^k close to v_k because T1's facet with normal v_k is ∂D_T1 ∩ cl M_k (P_T1 = v_k·g on M_k); sides parallel to the simplex sides ⇒ K = {m ≥ c}. Step 3: from c_i d_k = λ_i z_i(k) (k ≠ i), d is fixed up to scale and c/t = β is fixed, so c is unique (and the judges must also satisfy d₁/d₂ = z₃(1)/z₃(2)). Step 4 (clopen) ✓; Lemma 1.3 at e₁ ✓.
- **Hypotheses actually used.** The exact form σ_iv = κ_iv(M_k)g_i on N ⊇ ∂D_T1∖{0} (audit correction 3: general finite fans are open); weak Bayes in all 216 branches at p near p₀ (from (QS)); continuity in measure on all of Δ; T1 selected; vertex models. **The triangle shape of nearby selected models is derived** (Step 1), not assumed. So within this class, credal sets that "round their corners" near T1 are excluded by the proof, not by an assumption.
- **Free extension (PROVED, §4.1 Lemma B.1).** Thm 4.2 holds verbatim for switch values m(g)κ_iv(M_k)g_i, with m bounded, even and positive a.e. (common to all judges), in particular for C^∞ flat m.

### 1.6 Proposition 5.1 (rank two). Correct with a one-line repair.

- (a) ✓. Σu_i = 0 on ∂C by continuity from both sides. If α_i· = 0, then at a boundary point with g_i < 0 < g_j, g_k (it exists, since P_K(−a,1,1) changes sign when K ⊂ int Δ) the other two components are ≥ 0 and vanish only if their weights vanish.
- (b) ✓ up to the last step. Each world's cone of switch values is pointed (its members have the sign of g_i), so all branches use r with one sign. π_i(r) then lies in all six pair cones in the coordinates (x, y) of V_i (generators in an open half-plane, pointed polyhedral cone), and the 1D Helly step gives σ_iw = ρσ_iv **as functions on all oriented g**. That is proportionality on {+,0,−}, which suffices by §1.4's strengthening. (As MM1 wrote it, "hence globally" for penalty differences at all advices, including ×, was not justified, and it is not needed.)
- **Scope (audit correction 1).** Only dim R(C) ≤ 1 at one interior selected model is excluded. The Remark after 5.1 is explicitly not a theorem; its last sentences use the plain-posterior sweep (an assumed family).

---

## 2. MM2

### 2.1 Branch form (Lemma 1.1). Correct.
|Q| + |F_i| ≥ q + n − q + 1 > n. ✓ It holds for every (n, q). For (7, 5): 35³ = 42 875 branches at full support.

### 2.2 Boundary alignment (Theorem 3.1). Correct; uses weak Bayes only.
On A′, (WB) at advice b gives w·f^{ab}_F ≥ 0 near y; on B′, (WB) at advice a gives −w·f^{ab}_F ≥ 0. Let r → 0. ✓ Gordan's alternative gives the restatement. ✓

**Lemma 3.2: repair.** The proof divides by |y_iv| > 0. A common essential value at a boundary point is an approximate limit at a point of a null set, and it can have zero entries even though the switch values are nonzero a.e. Examples: a continuous switch value vanishing at the point, or a flat judge (Part B). Add the hypothesis "y_iv ≠ 0 for (i,v) ∈ F". It holds, for instance, for switch values continuous and nonvanishing at the chosen facet points. With it, the proof is correct. The remark "≥ 8 extreme supports at T1" depends on the all-three-worlds conclusion and inherits the hypothesis.

### 2.3 Rigidity counting (Lemma 3.3). Correct.
A pointed cone in dimension ≤ 2 has ≤ 2 extreme rays, and each nonzero member's support contains one of their supports. The avoidance choices need n−q+1 ≤ n−1 (two worlds) and n−q+1 ≤ n−2, i.e. q ≥ 3 (one world). ✓ It holds for (7, 5) as well. The 27-branches-per-support count is right: a support meets each world in one judge (3 pairs) or two (1 pair).

### 2.4 Multi-site swap (Prop 4.1) and exhaustion (Prop 4.3). Correct.
- Prop 4.1: |Δ_iv − m z_iv| ≤ mrΛ < mζ/2. Disjointness holds because earlier sets have total measure < mΛ < μ(A_j)/2. ✓
- Prop 4.3: w·Δ_F is the integral of a strictly positive function over a non-null set. ✓
- **Reading.** "The local method is exhausted by Theorem 3.1" holds when some aligned w_F is strictly branch-Bayes off a null set near the boundary. When every aligned weight vanishes identically on an open set, local records can do more. Prop A(b) is exactly such a case, and there local records defeat (QS) **despite** alignment holding.
- **(R5) wording.** Correct as "every violator of (NT_F) has its change set inside the common tie set of all weak-Bayes weights of F". It is not "exactly" those records.

### 2.5 Generic judges at T1 (Cor 4.2). Correct.
Facet switch values at approximate-continuity points are common essential values: the two sides are half-spaces, and (LF) supplies accept and silence. Prop 4.1 then applies. Zero entries do no harm here.

### 2.6 World-separable judges (Thm 5.1). Correct on the full domain and on every decomposable domain with (LF) at T1.
Re-derived:
- The facet pieces of F₁ are h = (−(a+b), −a+(κ+1)b, (κ+1)a−b) with patterns (−,+,+), (−,−,+), (−,+,−).
- Each coordinate ranges over a full half-line on each piece (an open cone).
- Lemma 5.2 holds: the Cauchy equation is local, continuity holds, and the matching gives μ ∝ v.
- Slope matching: λ₁(c₀+ε) = λ₂c₀ (B₁⁻ on F₂'s piece (−,−,+)) and λ₂(c₀+ε) = λ₁c₀ (B₂⁻ on F₁'s piece (−,−,+)) give λ₁ = λ₂ = 0, and then λ₃ = 0.
- Constants vanish by the three F₁ equations and F₂'s (+,−,+).
- Only weak Bayes at T1 for one nonzero mixture is used. On a decomposable domain, Lemma 2.1 (Lyapunov + decomposability) produces that mixture from (QS), and (LF) supplies the facet switches. ✓

### 2.7 Edge identities (Thm 6.4, Cor 6.5). Correct with a null-set repair.
- (a) ✓. K ↦ D_K is a continuous injection from a compact space, hence a homeomorphism onto its image. Edge confinement (Lemma 6.2) and the vertex models give the sweep. α_p also sweeps (0,1) by the same IVT.
- (b) ✓. In Q_ij the boundary is Π_β. The other side is silence if α < β (since P̄ − P = (β−α)(g_i − g_j) > 0) and accept −g if α = β. *Remark:* in Q_ji the boundary is Π_α, not Π_β, so the two halves of one edge plane are generally reached at different indices; the symmetric statement (swap i, j) holds.
- (c) ✓ with a repair. To conclude that w has nonzero restrictions to both F_i and F_j, N must also contain the null set of approximate-continuity points whose approximate value has a zero entry. That set is null because the approximate value equals the function a.e. Fubini through the stated diffeomorphism then gives a.e. slices. The identity (6.1) itself is unaffected.
- **Scope (audit correction 5 confirmed).** The identity holds for a.e. s, at a.e. point of Π_s. The type is c or d according to whether K_{p_s} is imprecise or precise. The weight w = w(s, F) may vary with s. The judges must satisfy it with some type per plane. It does not identify one field across planes. Cor 6.5 needs the monotone-ratio hypothesis for **both** types; it does.
- **New observation used in Part B (PROVED).** Each corner ray of T1 lies in two edge regions: r₂₃ = (κ+1,−1,−1) ∈ Q₁₂ ∩ Q₁₃, r₃₁ ∈ Q₂₁ ∩ Q₂₃, r₁₂ ∈ Q₃₁ ∩ Q₃₂. The edge planes Π_s through a neighbourhood of r₂₃ contain the g₃- (resp. g₂-) direction and so cross the wall {g₂ = g₃}. Hence **the edge identities constrain the judges near T1's corners**, whatever the family does in the interior.

---

## 3. The four bridges

1. **Weak versus strict.**
   - Strict certification is used only in MM1 Prop 2.1(a), the "certified" checks (MM1 Part A, Thm 4.2 Part A) and Prop 4.3 / audit's sufficient certificate.
   - Everything else uses weak Bayes from (QS) only: MM1 Lemma 1.2, Thms 4.1–4.2, Props 3.2 and 5.1; MM2 Thm 3.1, Lemmas 3.2–3.3, Cor 4.2, Thms 5.1 and 6.4.
   - Prop A closes the gap for analytic branches (and common-factor-analytic branches): (QS) fails with no certificate assumption. For C^∞ branches it leaves only flatness.
2. **Local versus global proportionality.**
   - Lemma 3.1, Thm 4.1 and Cor 4.3 give proportionality on pinned cells (local).
   - Prop 3.2 needs it globally on {+,0,−} (§1.4).
   - Prop 5.1 gets global proportionality from the global rank-2 hypothesis.
   - Thm 4.2 never uses Prop 3.2.
   - No proved result passes from local to global proportionality.
3. **Arbitrary shapes versus moving corners.**
   - Assumed only in MM1 Cor 2.2 (plain posterior family, an explicit construction choice) and in readings (MM1 §6 "along every moving kink", the Remark after 5.1).
   - Derived in Thm 4.2 Step 1 (triangles near T1, from weak Bayes + min-cell form).
   - Not used in Prop 2.1, which concerns any selected model with a corner (in particular T1 itself), in Prop A, or in MM2. MM2 §6 uses forced edge shapes.
   - So the analytic exclusion at **T1** (Cor A.2) holds for every family, however its other members are shaped.
4. **Two versus three generators.**
   - Lemma 3.1, Thm 4.1, Thm 4.2, Cor 4.3 and Prop 5.1(b) are two-generator (n = 4, q = 3, or q = n−1) results.
   - Prop A, Cor A.2, MM2 Thms 3.1, 5.1, 6.4, Cor 4.2 and Lemma 3.3 are (n, q)-free (Lemma 3.3 needs q ≥ 3). They apply to 5-of-7 unchanged.

---

## 4. Part B: n = 4, q = 3, smooth flat switch functions

### 4.1 Results

**Lemma B.1 (common factor = change of measure; PROVED).** Let m be measurable, bounded, positive a.e. and even (m(g) = m(−g), so it is a function of the pair). Replacing every judge's penalty ℓ_iv by mℓ_iv and keeping μ gives the same L_iv on every model as keeping ℓ_iv and replacing μ by ν := mμ. So (QS), every branch test and every competitiveness statement are identical. MM1 Lemmas 1.1–1.4, Thms 4.1–4.2 and Prop A, and MM2 Thms 3.1, 5.1, 6.4, Props 4.1, 4.3, Cor 4.2 and Lemma 3.3, use μ only through: atomless; finite; same null sets as Lebesgue; integrability; continuity in measure (equivalent for μ and ν on coherent models, both being equivalent to Hausdorff convergence of credal sets by the compact-injective argument of §2.7). So they hold for ν.
*Proof.* ∫ mℓ dμ = ∫ ℓ dν. Strict guidance, integrability (∫|mℓ| dμ = ∫|ℓ| dν) and evenness of the pair indexing are preserved. ∎

*Consequence.* Smoothness of the judges is not an invariant of the problem. Any design whose switch values are smooth off finitely many planes can be made C^∞ by a common flat factor vanishing on those planes, with no change in (QS). Proposition 2.1 is the only MM1/MM2 exclusion whose hypothesis is not invariant in this way. Prop A(b) is its invariant form.

**The test design S (PROVED; CHECKED Part 1).** Put H(t) = e^{−1/t²} (t ≠ 0), H(0) = 0, and M(g) = H(g₁−g₂)H(g₂−g₃)H(g₃−g₁): C^∞, even, positive off the walls, flat on the walls. Let

  σ^S_iv(g) := M(g) κ_iv(M_k) g_i on M_k,

with MM1's Part A constants (κ*_i, κ*_i ± (c₀/2)τ_i, 2κ*_i). Then:
- σ^S is C^∞ on ℝ³∖{0} and flat at every point of T1's corner rays (they lie in the walls). It is strictly guiding a.e. and realised by integrable judges (MM1 realisation). So **neither Prop 2.1 nor Prop A(b) applies** at any corner: no judge is analytic there, and the factor in front of the cellwise part is not analytic.
- For each of the 216 branches there is α ≥ 0 with Σ_{F_i} α_iv κ_iv = κ*_i at every world (CHECKED for ε ∈ {1/10, 3/10, 1/2}; in fact for every ε by the pair structure). Hence Σ α σ^S = M·P_T1 (since P_T1 = v_k·g on M_k), and Σ α σ^S(−g) = M·P_T1(−g). By MM1 Lemma 1.1(b), **T1 is strictly certified in all 216 branches**, so (QS) holds at T1's index. MM2's alignment and Cor 4.2 are passed at T1, as they must be.
- The flatness is the C^∞ phenomenon of Prop A(a): every branch's combination M·P_T1 is flat at the corner points.

**Verdict on S and its families (PROVED).**
1. **Thm 4.2 kills S.** By Lemma B.1 (m = M), S under μ is the min-cell design under ν = Mμ, and Thm 4.2 holds for ν. So no coherent selection that is continuous in measure and passes through T1 satisfies (QS). Because Thm 4.2 Step 1 *derives* that selected models near T1 are triangles {m ≥ c}, **families whose credal sets change shape (rounded corners) are excluded too**: they cannot be weak Bayes in even one branch near T1. (Prop 3.2 also applies directly: κ*_i and 2κ*_i give a globally proportional pair at every world.)
2. **The edge identities kill S independently** (CHECKED Part 2). Take the branch (doubled pair {κ*, 2κ*} at world p, doubled pair at the other edge world) on the planes Π_s near the corner with positive coordinate p, crossing the wall between cells M_j and M_k. Identity (6.1) forces the cross-world ratio of switch magnitudes to be constant along Π_s. M cancels, so the ratio on cell M_l is κ*_p(l)/κ*_o(l) for type c, and (κ*_p(l) + κ*_p(p))/(κ*_o(l) + κ*_o(p)) for type d (−g lies in M_p). The two cells give different values for both types at all six (corner, edge) pairs, e.g. ε = 3/10: 7/16 vs 1 (c) and 1 vs 23/14 (d). In S these planes cross the wall for **every** s ∈ (0,1), so no continuous (QS) family exists on the closed edges, whether or not it passes through T1.
3. **General statement (PROVED; algebra CHECKED Part 3).** Let every judge's switch value be m(g)κ_iv(M_k)g_i on the edge regions Q_ij and on their antipodes (m as in Lemma B.1), and suppose T1 is weak Bayes in all 216 branches. By Thm 4.1(b) the doubled rays are then z_i(k) = (v_k)_i d_k/λ_i for some d, λ > 0. Let the (QS) family be continuous on the closed edges. Then:
   - **Type c fails identically.** The ratio difference has numerator ±3ελ.
   - **Type d requires d_p > d_j and d_p > d_k** at the corner whose positive coordinate is p. At corners +1 and +2 these give d₁ > d₂ and d₂ > d₁, a contradiction.

   So this whole class dies on the edges alone. For the narrower Thm 4.2 class (min-cell form only on N near ∂D_T1), the type-c identity still fails on the planes Π_s ∩ N near each corner (s near the corner's parameter). The edge models there must therefore be **precise** for a.e. such s. Type d involves σ at −g ∉ N and is not determined by that class.

### 4.2 Smooth flat designs not of common-factor form

The model function F(x,y) = h(x)h(y) − h(−x) − h(−y) (h(t) = e^{−1/t²} for t > 0, else 0) is C^∞, > 0 on {x, y > 0}, < 0 where x < 0 or y < 0, and 0 on the rest of the boundary (PROVED by inspection). Near T1's corner r₁₂, with L_k = v_k·g, put ρ > 0 smooth and

  u₃ = h(L₁)h(L₂) + ρ, u₁ = −h(−L₁) − ρ/2, u₂ = −h(−L₂) − ρ/2.

These are smooth, have the own-world signs in the orthant (−,−,+), and Σu_i = F(L₁, L₂) has exactly the sign of P_T1 there. So a smooth field strictly certifies T1 locally at a corner. This is not of common-factor-times-analytic form, and Prop 2.1 / Prop A(b) do not apply (PROVED).

For such genuinely heterogeneous flat designs, **no proved obstruction kills the class as a class**. The proved constraints they must meet are:
- every aligned branch combination is flat at every corner point of every selected model with a corner (Prop A(a));
- at T1's corner points, some world has ≥ q non-analytic judges (Cor A.2);
- alignment with nonzero-entry caveats (MM2 Thm 3.1, Lemma 3.2 repaired), and no strictly negative vector in the facet span (Cor 4.2);
- not (WS) (Thm 5.1);
- the edge identities, which reach T1's corners (§2.7 observation), with type c or d per plane;
- the exact nonstrict test (MM2 (R5)).

Whether all of these, together with (QS) along a shape-changing family, can be met is **open**. Nothing here is a construction.

**Part B verdict.**
- MM1's analytic obstruction fails to apply to smooth flat judges (PROVED, explicit design S certifying T1 in all 216 branches).
- The natural smooth flat test class (common flat factor × min-cell, shape-changing families allowed) is still killed, by Thm 4.2 through Lemma B.1 and independently by MM2's edge identities (PROVED; CHECKED).
- Smoothness bought nothing there: the flat factor is a change of measure.
- Escaping requires flatness that differs between the judges of a branch, in the sense of §4.2; that case is open.

---

## 5. Status table

| Item | Label |
|---|---|
| MM1 Lemmas 1.1–1.4 correct | PROVED |
| MM1 Prop 2.1 correct as stated (strict / weak-vanishing) | PROVED |
| Prop A(a) C^∞ flatness; Prop A(b) (QS) fails for common-factor × analytic branches near a corner | PROVED |
| Cor A.2: at each corner point of a selected model, some active world has ≥ q non-analytic judges | PROVED |
| MM1 Lemma 3.1 correct (two generators) | PROVED |
| MM1 Prop 3.2 correct modulo FF2 Thm 4.1 chain; proportionality on {+,0,−} suffices; global only | PROVED (interface checked; imports not re-refereed) |
| MM1 Thms 4.1, 4.2 correct; shape near T1 derived | PROVED |
| MM1 Prop 5.1 correct with repair | PROVED |
| MM2 Lemma 1.1, Thm 3.1, Lemma 3.3, Props 4.1, 4.3, Cor 4.2, Thm 5.1 correct | PROVED |
| MM2 Lemma 3.2 needs y_iv ≠ 0 on F | PROVED (repair) |
| MM2 Thm 6.4 needs zero-value null set in N; Q_ji half via α | PROVED (repair) |
| T1's corner rays lie in two edge regions each | PROVED |
| Lemma B.1 (common even factor = change of measure) | PROVED |
| Design S: C^∞, flat at corners, T1 certified in 216/216 branches | PROVED; CHECKED |
| S excluded by Thm 4.2 (via B.1), incl. shape-changing families | PROVED |
| S excluded by edge identities, both types | PROVED; CHECKED |
| Global min-cell × common factor with T1 weak Bayes: edge identities fail (type c identically; type d contradictory) | PROVED; CHECKED |
| Heterogeneous flat designs (§4.2) | open |

**Files.** `nn3py/flat_design_check.py` → `nn3py/flat_design_check.out`:
- Part 1: 216/216 branches give exactly M·P_T1 (ε = 1/10, 3/10, 1/2), plus 500 exact samples of P_T1 = v_k·g on M_k.
- Part 2: edge ratios for both types at all six (corner, edge) pairs.
- Part 3: symbolic type-c numerators and type-d solved conditions.
