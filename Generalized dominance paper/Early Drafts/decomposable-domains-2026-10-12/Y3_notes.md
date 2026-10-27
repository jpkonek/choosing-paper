# Y3 — An actual reservation plan at a vertex: a single vertex carries no obstruction, even with T1 ∈ C_L

16 Oct 2026, round 27, Milestone 3 of BRIEF19. Labels:
- **PROVED**: full proof here, not refereed;
- **CHECKED**: exact rational arithmetic on stated samples;
- **CONJECTURE**;
- **NUMERICS**: sampling only; nothing depends on it.

Scripts are in `y3py/`. Run each with `python3 -I <script>` from inside `y3py/`; outputs are in the matching `.out` files. No assumption is added. Every extra hypothesis below is a hypothesis of the result that states it.

**Read:** BRIEF19, AUDIT_X123, X1 (plan-based compactness criterion, Thm X1.3.3, Cor X1.3.5), X2 (X2.2, X2.5–X2.9), L3 (L3.1, L3.4), T1n (T1n.1), P1 Part I (P1.15–P1.18), write-up §2, §4 (single-vertex pinning), §8 (Prop Q31).

**Notation.** As in the write-up §2:
- worlds 1, 2, 3; the vertex is e₁;
- c₀ = (1−ε)/3, λ = ε/c₀, A := 1+λ;
- T1 = conv{v_k}, with v_k = c₀(𝟙 + λe_k);
- for p ∈ Δ and a set M ⊆ ℝ³_{>0}, write ν(p⊙M) for the normalised image {ν(p⊙m) : m ∈ M};
- the posterior family is K_p = ν(p⊙T1) (X2.5).

Domain: the full two-sided domain, where every measurable model is evaluable. (LF) at T1 holds there trivially.

---

## 0. Outcome

**1. An actual vertex plan exists, and it is compatible with T1 (Theorem Y3.2, PROVED; pointwise lemmas CHECKED).**

The data:
- the vertex neighbourhood N := {p ∈ Δ : A(p₂+p₃) ≤ η′p₁}, a closed neighbourhood of e₁ in Δ that contains both edges through e₁ near e₁. The constants η′ < η < 1/(A+1) are explicit;
- the selection Σ_p := D_{ν(p⊙B₁)}, with box B₁ := {1}×[1,A]×[1,A]. It is precise at e₁ (Σ_{e₁} = {g₁>0}, as L3.1 forces) and edge-supported on both edges. Add Σ_u := T1 as an isolated index;
- the competitors 𝒳 := **all measurable models**;
- an explicit additive strictly guiding field Ψ⁽¹⁾ on the full domain;
- the explicit plan V(p,i,X) := N ∩ B(p, (Ψ_i(Σ_p) − Ψ_i(X))/Λ) whenever Ψ_i(Σ_p) > Ψ_i(X), with Λ = 16√(6/π)·A². At the isolated index, V(u,i,X) := {u}.

The world orders of Ψ⁽¹⁾ satisfy, simultaneously:
- global strict (G) and (IB);
- for every p ∈ N ∪ {u} and every measurable X: (K) (competitiveness on supp p), (R4) (protection), (Csel), and the plan clauses (sections closed relative to N ∪ {u});
- **T1 ∈ C_L**, and (LF) at T1.

So the whole theory Θ_Σ|_{N∪{u}} ∪ Plan(V) ∪ {T1 ∈ C_L} is satisfiable, and **every finite fragment is satisfiable with that same plan**. This covers fragments with thin near-plane competitors and fragments comparing selected models at different indices (Cor. Y3.3).

**2. Answer to the obstruction branch of the milestone: there is no single-vertex obstruction to T1.**
- No argument that uses selection indices only in N, together with u, global (G), (IB), T1 ∈ C_L and (LF), can exclude T1 (Cor. Y3.4).
- This already holds within additive rankings.
- The "decisive vertex obstruction for every selection with the forced vertex behaviour" does not exist.

This is the vertex analogue, on the full domain, of the interior locality barrier Prop Q31.

**3. The posterior candidate at the vertex (Props Y3.5–Y3.7, PROVED/CHECKED).**
- **(a) The posterior edge families are jointly realisable.** One additive system, the cube box ν(p⊙[1,A]³) (an R10a box cover), has Bayes family equal to the posterior on **all of ∂Δ**: all three edges and all three vertices, with one triple of orders. This settles the compatibility part of Milestone 2 for the posterior edge families. In that system T1 is dominated.
- **(b) Box rigidity at a vertex (Prop Y3.7(a)).** Suppose an additive field has a box family ν(p⊙B) as its p-Bayes models on a neighbourhood of e₁, and T1 ∈ C_L, with T1 Bayes at w\*. Then w\*⊙B ∝ B₁. So the cube (the posterior's edges at e₁) is **incompatible with T1** in any additive vertex plan (Cor. Y3.6). The finite certificate is two families of near-plane gambles at the crossings of coordinate 1 on F₂ and F₃.
- **(c) Two box vertices are incompatible (Prop Y3.7(b)).** No additive field carries T1-compatible box plans at two vertices. The conflict sits at gambles near the third coordinate axis. So within box plans, the additive obstruction to T1 needs at least two vertices.
- **(d) The posterior selection itself is not additive near e₁.** For p ∈ int Δ ∩ N, the posterior is not the p-Bayes family of any additive field (Remark Y3.8, PROVED). A vertex plan for the posterior selection would need a non-additive interior system near e₁, which is Milestone 1's open problem localised. I did not construct one, and I found no certificate against one.

**Nearby result (project preference).** The literal target, a plan for the posterior selection on a vertex neighbourhood, is out of reach for the reason in 3(d). The reachable nearby results are 1 and 3(a). Either:
- keep T1 ∈ C_L and accept one-sided edges at e₁ (odds intervals [r/A, r]); or
- keep the posterior edges and lose T1, within additive plans.

Whether a non-box or non-additive vertex plan can have both is the precise open question Q_Y3 (§6).

---

## 1. Additive fields in acceptance-vector form

On the full domain, write each pair through either of its orientations g ∈ ℝ³. An additive field that is non-adjacent where it matters is given by a measurable map g ↦ m(g) ∈ ℝ³_{>0}. Its **acceptance vector** is n(g) := m(g)⊙g, which has the strict sign pattern of g.

For the pair {h, −h} (h ∈ H) put:
- ℓ(h,S) = 0;
- ℓ(h,M) = −n(h), the cost of accepting h;
- ℓ(h,O) = −n(−h);
- ℓ_i(h,×) = 2A|h| for every i.

**Lemma Y3.1 (PROVED).**
- **(a) Guidance.** If 0 < m ≤ A coordinatewise, the field is strictly guiding, with integrable envelope 2A|h|.
  - At a world with h_i > 0: ℓ_i(M) = −m_i(h)h_i < 0 = ℓ_i(S) < ℓ_i(O) = m_i(−h)h_i < 2A|h|.
  - With h_i < 0 the roles of M and O swap.
  - On unanimous pairs, M is correct at every world, with the same inequalities.
- **(b) Bayes models.** At a weight w with w·n(h) and w·n(−h) not both positive, the w-Bayes advice is:
  - M iff w·n(h) > 0;
  - O iff w·n(−h) > 0;
  - S otherwise.
- **(c) Box families.** For a box B = ∏[α_j, β_j] ⊆ ℝ³_{>0}, let corner_B(g) have coordinate α_j where g_j > 0 and β_j where g_j < 0.
  - With m(g) := corner_B(g), the w-Bayes model is D_{ν(w⊙B)} for **every** w ∈ Δ.
  - It is a.e. unique, and continuous in measure in w.
  - The family is coherent, precise at the vertices, and edge-supported.
- **(d) Axioms from uniqueness.** At any weight w where the Bayes model Σ_w is a.e. unique, Σ_w is competitive on supp w and undominated. Every model tied with Σ_w at all worlds equals Σ_w.
- **(e) Closed sections.** If w ↦ Σ_w is continuous in measure on a set W, then each section {w ∈ W : Ψ_i(Σ_w) ≤ Ψ_i(X)} is closed relative to W.

*Proof.*
- (a), (b): the inequalities are read off the definitions. A pointwise minimiser of w·ℓ(h,·) is the Bayes advice (write-up §2.4, R1 Lemma 1.2).
- (c):
  - min_{m∈B} m·z over z = w⊙g is attained at corner_B(g) whatever w is, because the signs of z are those of g. So (w⊙corner_B(g))·g > 0 ⟺ P_{ν(w⊙B)}(g) > 0.
  - Ties lie on finitely many hyperplanes in g, which are null.
  - ν(w⊙B) is the image of a convex set under a projective map of the positive cone, so it is convex.
  - At w = e_k it is {e_k}. If w_l = 0, it lies in {m_l = 0}.
  - Continuity in measure follows by dominated convergence.
- (d): if L_i(X) < L_i(Σ_w) for every i ∈ supp w, then w·L(X) < w·L(Σ_w). If X ⪯_i Σ_w at every world, then X is w-Bayes, hence X = Σ_w a.e.
- (e): dominated convergence. ∎

---

## 2. The vertex plan

**The field Ψ⁽¹⁾.** Fix η ∈ (0, 1/(A+1)), for instance η = 1/(2(A+1)), and η′ ∈ (0, η). Put

  Γ_η := {g : |g₁| ≤ η·max(|g₂|, |g₃|)}, a closed double wedge around the plane g₁ = 0.

For each g define:
- m(g) := corner_{B₁}(g) = (1, m₂, m₃), with m_j = 1 if g_j > 0 and m_j = A if g_j < 0, when g ∈ Γ_η;
- m(g) := 𝟙 + λe_{k(g)} = v_{k(g)}/c₀, with k(g) := argmin_k v_k·g (the active vertex of T1 at g; ties are null), when g ∉ Γ_η.

So Ψ⁽¹⁾ is the B₁ box field in a wedge around the plane g₁ = 0, and the "posterior field with attribution frozen at u" (X2.6 at p = u) everywhere else.

**Lemma Y3.3a (corner agreement at u; PROVED, CHECKED).** For g ∈ Γ_η with η < 1/(A+1),

  sign(corner_{B₁}(g)·g) = sign(P_{T1}(g)).

So the B₁ decision at u and the T1 decision agree on Γ_η.

*Proof.* Write M := max(|g₂|, |g₃|). Then P_{T1}(g) has the sign of min(τ₁, τ₂, τ₃), with τ_k := (𝟙+λe_k)·g.
- **g₂, g₃ > 0.**
  - The corner is (1,1,1), with value ≥ M − ηM > 0.
  - Every τ_k ≥ M − AηM > 0.
  - Both accept.
- **g₂, g₃ < 0.**
  - Corner value ≤ ηM − AM < 0.
  - τ₁ ≤ AηM − M < 0.
  - Both reject.
- **g₂ > 0 > g₃** (the reverse case is symmetric).
  - The corner is (1,1,A), with value b = g₁ + g₂ + Ag₃ = τ₃.
  - τ₂ − τ₃ = (A−1)(g₂ − g₃) > 0, and τ₁ − τ₃ = (A−1)(g₁ + |g₃|).
  - If g₁ ≥ −|g₃|, then min τ = τ₃ = b exactly.
  - Otherwise |g₃| < |g₁| ≤ ηM, so M = g₂. Then τ₁ ≥ M(1 − (A+1)η) > 0 and b ≥ M(1 − (A+1)η) > 0. Both accept. ∎

CHECKED (`y3_vertex_box.out`, part (a)): about 3700 gambles per ε ∈ {1/20, 1/10, 3/10, 1/2, 4/5}, including adversarial samples, with **0 mismatches**.

Negative control (`y3_controls.out`): with η = 1.6/(A+1) there are mismatches, so the bound on η is not slack.

**Lemma Y3.3b (the field near e₁ is exactly the B₁ family; PROVED, CHECKED).** For w ∈ N and every gamble g,

  sign(w·n(g)) = sign P_{ν(w⊙B₁)}(g).

*Proof.*
- **g ∈ Γ_η.** n(g) is the B₁ corner vector, so Lemma Y3.1(c) applies.
- **g ∉ Γ_η.** Then |g₁| > ηM, and for 1 ≤ m ≤ A,

  |w₂m₂g₂ + w₃m₃g₃| ≤ A(w₂+w₃)M ≤ η′w₁M < w₁|g₁| ≤ w₁m₁|g₁|.

  So both the field and every corner of B₁ give the sign of g₁. ∎

CHECKED (part (b)): 6000 (w, g) samples per ε, with w on both edges, in the interior and at e₁: **0 mismatches**. Part (c): the field at u equals the T1 decision for all sampled g, **0 mismatches**.

**Lemma Y3.3c (reservation radii; PROVED).** For p, q ∈ N and every world i,

  |Ψ_i(Σ_p) − Ψ_i(Σ_q)| ≤ Λ|p − q|,  Λ := 16√(6/π)·A² ≈ 22.1·A².

*Proof.*
- **Which pairs can change.** Off Γ_η the advice is constant on N (Lemma Y3.3b), and unanimous pairs never change. A pair can change only if some orientation g ∈ Γ_η has sign(p·n(g)) ≠ sign(q·n(g)).
- **The slab.** Then |(p⊙m_σ)·g| ≤ |p−q|·A|g|, where m_σ is one of the four B₁ corners. Since m_σ ≥ 𝟙, |p⊙m_σ| ≥ |p| ≥ 1/√3. So |ê·ĝ| ≤ A√3|p−q|, with ê the unit vector of p⊙m_σ.
- **Cost per pair.** Such a pair changes ℓ_i by at most |n_i(h)| + |n_i(−h)| ≤ 2A|h|.
- **Gaussian estimate.** For standard Gaussian g, ĝ is uniform on S² and independent of |g|, and ê·ĝ is uniform on [−1, 1]. So

  ∫ |g|·1{|ê·ĝ| ≤ θ} dμ = E|g|·θ = 2√(2/π)·θ.

- **Total.** Summing over the four corners gives

  |ΔΨ_i| ≤ 4·2A·2√(2/π)·A√3|p−q|. ∎

NUMERICS (`y3_lip.out`): the empirical worst ratio is 0.5–3.0, against the bound Λ ≈ 39–354.

**Theorem Y3.2 (vertex reservation plan with T1 ∈ C_L; PROVED).**

Let Ψ⁽¹⁾, N, Σ_p = D_{ν(p⊙B₁)} (p ∈ N), Σ_u := T1 and V be as in §0. Then:
1. **(Global.)** Ψ⁽¹⁾ is an additive ranking on the full domain with integrable envelope. It satisfies strict (G) and (IB). Its u-Bayes model is T1, a.e. uniquely. Hence T1 is coherent and undominated, so T1 ∈ C_L and (LA) holds. A model tied with T1 at every world equals T1. (LF) at T1 holds.
2. **(Vertex selection.)** For p ∈ N, Σ_p is the a.e.-unique p-Bayes model. It is coherent, with:
   - Σ_{e₁} = {g₁ > 0}, as L3.1 forces;
   - K_p ⊆ [e₁, e_j] on the edges, as X2.2(a) forces;
   - K_p → {e₁}, as X2.2(d) forces.
3. **(All local clauses, against every measurable X.)** For every p ∈ N ∪ {u}:
   - (K): Σ_p is competitive on supp p;
   - (R4): Σ_p is undominated;
   - (Csel): no model other than Σ_p ties it at every world;
   - closed sections: {p ∈ N ∪ {u} : Σ_p ⪯_i X} is closed in N ∪ {u}.
4. **(The plan.)** The plan is the one in §0. If Σ_p ⋠_i X, then Σ_q ⋠_i X for every q ∈ V(p,i,X), and V(p,i,X) ∋ p is relatively open. The maximal plan V^max(p,i,X) = {q ∈ N : Ψ_i(Σ_q) > Ψ_i(X)} also works.
5. **(Finitary form.)** Define the assignment x_{i,r} := [Ψ_i(r) ≥ 0], with Ψ_i(r) the world-i value of the record r. It satisfies the clauses below; by Prop X1.3.2, so does every finite subset of them:
   - every clause (Bg), (N), (Σ) of Θ;
   - (K), (R4), (Csel) at all p ∈ N ∪ {u} and all X;
   - Plan(V);
   - the protection clauses of T1.

*Proof.*
- (1):
  - Lemma Y3.1(a) gives strict (G), and additivity gives (IB).
  - By Lemma Y3.3a off Γ_η, and by the definition of m on Γ_η, the field decision at u equals D_{T1}'s.
  - Ties at u lie on finitely many hyperplanes. So T1 is the a.e.-unique u-Bayes model, and Lemma Y3.1(d) applies at w = u.
- (2): Lemma Y3.3b and Lemma Y3.1(c).
- (3): Lemma Y3.1(d) at each p ∈ N, and at u. Continuity in measure on N (Lemma Y3.1(c)) gives closedness via Lemma Y3.1(e). The point u is isolated in N ∪ {u}.
- (4): by Lemma Y3.3c, q ∈ V(p,i,X) gives Ψ_i(Σ_q) ≥ Ψ_i(Σ_p) − Λ|q−p| > Ψ_i(X).
- (5): every clause listed is a true statement about the preorders of Ψ⁽¹⁾. ∎

**Corollary Y3.3 (the fragments the milestone names; PROVED).** Take any finite fragment: finitely many competitors X₁, …, X_n (arbitrary measurable models) and finitely many indices p₁, …, p_m ∈ N ∪ {u}, together with all the clauses of Θ and Plan(V) that mention them. It is satisfied by the restriction of the assignment in Thm Y3.2(5). The fixed plan V is used for every fragment and is never shrunk. In particular:
- **Thin competitors.** Suppose X differs from Σ_p only on a wedge W_θ of angular width θ at a coordinate plane, and X ≺_i Σ_p. Its reservation radius (Ψ_i(Σ_p) − Ψ_i(X))/Λ is fixed by (p, i, X) alone. It is small but positive.
  - NUMERICS: margins of about 6·10⁻⁴, 3·10⁻⁵ and 4·10⁻⁷ at θ = 10⁻¹, 10⁻², 10⁻³, for world-1 corrections at the plane h₁ = 0.
  - Adding finer competitors adds new reservations. It never changes old ones. This is exactly the failure mode the audit warned about ("choosing smaller reservations afresh"), and it is absent here.
- **Selected models at different indices.** For X = Σ_q, the plan clause reads: Ψ_i(Σ_p) > Ψ_i(Σ_q) ⇒ Ψ_i(Σ_{p′}) > Ψ_i(Σ_q) for |p′−p| < (Ψ_i(Σ_p) − Ψ_i(Σ_q))/Λ.
- **Vertex-forced records (X2.2(c)).** For a cone P ⊆ Q₁ (a closed cone inside the open region Q₁) and F ⊆ E₁(Σ_p), world 1 accepts ρ_p(F) = (F → 1-correct; P: O → S) whenever

  Λ|p − e₁| ≤ ∫_P |n₁(−h)| dμ  (for p ∈ N with Σ_p at O on P, which holds near e₁).

  Silencing P costs world 1 exactly ∫_P |n₁(−h)| dμ. Correcting F gains at most Ψ₁(Σ_p) − Ψ₁(B¹) ≤ Λ|p−e₁|, since B¹ = Σ_{e₁} corrects every world-1 error and every per-pair gain is ≥ 0. So "a far silence outweighs any correction of C_p's errors" (X2.9) holds with an explicit neighbourhood N_P. Ψ⁽¹⁾ is not G′-invariant, so X2.9 does not apply to it.

**Corollary Y3.4 (vertex locality barrier on the full domain; PROVED).** Take the full two-sided domain. Consider the premises:
- global strict (G) and (IB);
- T1 ∈ C_L (hence (LA)) and (LF) at T1;
- at every index p ∈ N ∪ {u}: competitiveness on supp p, closedness relative to N ∪ {u} of every section {p : C_p ⪯_i X}, and (C) for models tied with C_p.

These premises have a model (Thm Y3.2). So no derivation of a contradiction from them exists. An exclusion of T1 must use selection indices outside N ∪ {u}, for every vertex neighbourhood of the form above. By symmetry the same holds at e₂ and e₃ separately, with boxes B₂ = [1,A]×{1}×[1,A] and B₃.

As in Prop Q31, global consequences of (S), such as Theorem kkm, count as using all indices. The ranking Ψ⁽¹⁾ has no global closed selection: by Thm gm, no additive ranking covers T1.

---

## 3. The posterior's edges at e₁

**Proposition Y3.5 (the cube system realises the posterior on ∂Δ; PROVED, CHECKED).** Let Ψ^□ be the box field of the cube [1,A]³ (Lemma Y3.1(c)). Its acceptance vectors are those of X2.6's field with the caution cost charged to **both** majority worlds: on Q_o,

  O iff w·h + λΣ_{j≠o}w_jh_j < 0,  M iff w·h + λw_oh_o > 0.

Then:
- **(a) A successful system on all of Δ.** Ψ^□ satisfies strict (G), (IB) and (C); every Bayes model is coherent; competitiveness, protection and closed sections hold for every measurable model. This is the R10a box cover for the box [1,A]³, written out.
- **(b) It equals the posterior on ∂Δ.** For every p ∈ ∂Δ, ν(p⊙[1,A]³) = K_p = ν(p⊙T1). On an edge (p_l = 0) both equal the odds interval between ν(Ap_i, p_j, 0) and ν(p_i, Ap_j, 0); at the vertices both are precise.
- **(c) Hence the three posterior edge families are jointly realisable.** One triple of world orders carries them, so each world's two edge appearances are one order, and compositions across edges are compositions in that order. This is the compatibility asked for in Milestone 2, for the posterior edges.
- **(d) What it costs.** In the interior, ν(p⊙cube) is the hexagon conv(K_p ∪ {ν(p⊙((A)𝟙 − λe_k))}) ⊋ K_p. At u, it is a hexagon ⊋ T1, so T1 is dominated: Cor. Y3.6 below, or directly by Thm gm.

*Proof.* (a) Lemma Y3.1. (b) On the edge p₃ = 0, the six corners of the cube collapse onto the two points listed, and the posterior's three points lie on that segment with its two ends. (d) Direct. ∎

CHECKED (`y3_cube.out`):
- cube decision = double-attribution formula: 0 mismatches of about 6000 pairs per ε;
- cube = posterior at boundary p: 0 mismatches;
- interior: 1–2% of pairs differ.

NUMERICS: as p → e₁, the difference set concentrates at the plane h₁ = 0. Its mass is 2·10⁻², 7·10⁻³, 1.3·10⁻³ and 2.6·10⁻⁴ at r = 0.2, 0.05, 0.01, 0.002, and the median |h₁|/|h| on it is 0.66, 0.15, 0.027, 0.0055. This is the audit's interior-locality phenomenon, seen at the vertex.

**Proposition Y3.7 (box rigidity at a vertex; PROVED, CHECKED).**

Let Ψ be any strictly guiding additive ranking on the full domain, with integrable envelope. Let N be a relative neighbourhood of e₁ in Δ. Suppose that for every p in a dense subset of N, the box model D_{ν(p⊙B)} is a p-Bayes model of Ψ, for a box B = ∏[α_j, β_j] that is not a single point. ("The natural plan for the box selection.")

- **(a)** If T1 ∈ C_Ψ, then T1 is w\*-Bayes for some w\* ∈ Δ, and w\*⊙B = K·B₁ for some K > 0. That is, α₁ = β₁, α₂w₂\* = α₃w₃\* = α₁w₁\*, and β_j = Aα_j for j = 2, 3.
- **(b)** Suppose moreover that D_{ν(p⊙B′)} is p-Bayes for p in a neighbourhood of e₂, for a box B′, and T1 ∈ C_Ψ. Contradiction. So at most one vertex carries a T1-compatible box plan in one additive field.

*Proof.*

**Step 0 (T1 is Bayes).** In an additive ranking on a decomposable domain, the set R := {L(X) − L(T1) : X} is the Aumann integral of a finite-valued correspondence over a non-atomic measure, so it is convex (Richter/Aumann).
- Undominated means R misses −ℝ³_{≥0} ∖ {0}.
- Separating R from the open negative orthant gives w\* ≥ 0, w\* ≠ 0, with w\*·r ≥ 0 on R.
- So T1 is w\*-Bayes: its advice minimises w\*·ℓ(h,·) for a.e. h.

**Step 1 (pinning).** Let D ⊆ N be countable and dense among the weights where the box model is Bayes. For a.e. pair, the box advice is a p-minimiser for every p ∈ D.
- Fix such a pair, with an orientation g whose box acceptance line ℓ_g := {p : (p⊙corner_B(g))·g = 0} meets the interior of N.
- On D, the field's acceptance gain (ℓ(S) − ℓ(accept g))·p is ≥ 0 on one side of ℓ_g and ≤ 0 on the other. This uses non-adjacency of the box family near ℓ_g: −g is not accepted near ℓ_g ∩ int N, because on ℓ_g

  (p⊙corner(−g))·(−g) = −Σ_j p_j(β_j − α_j)|g_j| < 0

  for interior p, since B is not a point.
- The gain is affine in p. So it vanishes on ℓ_g ∩ N and is a positive multiple of p·(corner_B(g)⊙g). It is not identically zero, because of strict (G).

**Step 2 (crossing families at e₁).** Small-|g₁| gambles have box lines through N.
- *Family (−,+,−):* g = (−a, 1, −c), with a > 0 small and c near 1/A.
  - Here T1 accepts g iff c < (1−a)/A, and is silent beyond: T1 never accepts −g there, since P_{T1}(a, −1, c) = c₀(a−1+c) − ε < 0.
  - Since T1 is w\*-Bayes, the affine function c ↦ w\*·((β₁, α₂, β₃)⊙g) changes sign at c = (1−a)/A, for a.e. small a.
  - Hence −β₁aw₁ + α₂w₂ − β₃(1−a)w₃/A ≡ 0, which gives β₁w₁ = α₂w₂ = β₃w₃/A. (If w₃ = 0 there is no sign change at all: contradiction.)
- *Family (+,+,−):* g = (a, 1, −c), with corner (α₁, α₂, β₃) and T1 boundary c = (1+a)/A. This gives α₁w₁ = α₂w₂ = β₃w₃/A.
- *The mirror families* (−,−,+) and (+,−,+) give β₁w₁ = α₃w₃ = β₂w₂/A and α₁w₁ = α₃w₃ = β₂w₂/A.
- So (a) holds with K = α₁w₁.

**Step 3 (proof of (b)).** By (a) at e₁ and at e₂, w\* is the same point. (a) determines w\* from B, and from B′.
- Take g = (x, −y, 1) with 0 < x ≪ y ≪ 1.
- In w\*-normalised coordinates, the e₁ plan pins the acceptance vector to (1, A, 1)⊙g, and the e₂ plan pins it to (1, 1, 1)⊙g.
- Both lines cross the interiors of the respective neighbourhoods on an open set of such g. The vectors are not proportional, since A ≠ 1 and y ≠ 0. A single field vector cannot be both. ∎

CHECKED:
- `y3_twobox.out`: an explicit rational g in both wedges Γ_η; points of N₁ and of N₂ on both sides of the respective lines; n₁ × n₂ ≠ 0.
- `y3_cube.out`, part (4): the (−,+,−) pinning forces w\* = (1, A, A) for the cube, and the (+,+,−) family then mismatches T1. For example, at ε = 1/10 and a = 1/100 the field's zero is at c = 1209/1600 and T1's at c = 303/400.

**Corollary Y3.6 (PROVED).** No additive ranking whose p-Bayes models near e₁ are the cube models has T1 ∈ C_L; the cube is the box extension of the posterior's edge models. The reason is that α₁ = 1 ≠ A = β₁. The certificate is finite in kind: two one-parameter families of near-plane gambles at the crossings (0, A, −1) and (0, −1, A) of coordinate 1 on the facets F₃ and F₂.

Remarks.
- Together, Y3.2 and Y3.7(a) say that the T1-compatible additive box plans at e₁ are exactly the B₁ plan, up to the reparametrisation p ↦ ν(p⊘w\*).
- Their edge models are the one-sided odds intervals [r/A, r] (r = p₁/p_j), which contain the precise p. The posterior's are [r/A, rA].
- So within box plans, T1 pins the vertex behaviour to first order at the crossings of coordinate 1. This is the full-domain, single-vertex shadow of the write-up's §4.2 pinning.

**Remark Y3.8 (the posterior near e₁ is not additive; PROVED).** Let U ⊆ int Δ be open; U ⊆ N ∖ ∂Δ is allowed. No additive strictly guiding field has the posterior C_p as a p-Bayes model for p in a dense subset of U.

*Proof.*
- **Kink pairs.** For each p ∈ U there is a pair h_p ∈ Q₁ whose posterior O-region in p-space is a wedge with apex p and angle < π, with only S around it. Take p₂b = p₃c and p₁a = (2+λ)p₂b. The map p ↦ h_p is a smooth bijection onto a two-parameter family, so the pairs whose apex lies in U form a cone of positive measure.
- **Convexity.** For an additive field, the S-region {p·c ≤ 0, p·c′ ≤ 0} is convex. Choose p₁, p₂ ∈ S (dense) whose segment crosses the wedge.
- **Contradiction.** Linearity forces p·c′ ≤ 0 on an open set of the wedge, where O must be a minimiser. So p·c′ = 0 on an open set, c′ = 0, and strict (G) fails. ∎

So the natural (additive, identity-parametrised) plan for the posterior selection near e₁ fails. Additive orders in which C_p is competitive because it is Bayes at a *different* weight w(p) are not excluded by this proof (CONJECTURE: they are excluded too, by a local fundamental-theorem-of-projective-geometry argument). Either way, a vertex plan for the posterior selection needs genuinely new local orders near e₁.

---

## 4. What this changes for T1

1. **The vertex is not where T1 dies, taken alone (Cor. Y3.4).**
   - The audit asked for an actual plan that survives arbitrarily fine fragments with fixed reservations. Theorem Y3.2 gives one for all measurable competitors, with T1 ∈ C_L and (LF).
   - With Prop Q31 (interior compact sets, on M_U), every one-region argument is now blocked at the level of index-local premises.
2. **Where an additive obstruction lives, within box plans.**
   - It needs at least two vertices. The conflict is at gambles near the third coordinate axis, where both vertex plans pin the same line (Prop Y3.7(b)).
   - This matches the write-up's Thm gm, whose proof uses vertex neighbourhoods of several worlds (Lemma UVN for the crossing coordinate and a second world j in Lemma nopin).
3. **For the posterior candidate.**
   - Its edges at e₁ are additively compatible with each other and with all three edges (Prop Y3.5).
   - They are additively incompatible with T1 in box form (Cor. Y3.6). They are compatible in the one-sided form [r/A, r].
   - Any cover keeping the posterior edges at e₁ must have non-box near-vertex Bayes structure, or non-additive local orders (with T1 ∈ C_L).
4. **For X1's programme.** The plan of Thm Y3.2 satisfies uniform rejection (Cor X1.3.5) with explicit radii. It is a legitimate first block for a shared-plan construction.
   - It cannot be extended additively to a second vertex in box form (Y3.7(b)).
   - The next construction must therefore change, between the vertices, either the box structure or additivity. This is the content of Milestones 1–2.

---

## 5. Where I stopped

- **Posterior selection at the vertex.** I did not construct a non-additive local system for the posterior near e₁ with interior indices (Remark Y3.8 shows one is needed), and I found no certificate against one. X2.9 rules out the invariant one only.
- **Posterior edges with T1 ∈ C_L and non-box interior.** Open: Q_Y3 below.
- **Pointwise feasibility (CHECKED at one point, `y3_pencil.out`).**
  - The T1 pencil constraints alone are pointwise satisfiable with the posterior edges. Take (s,t) = (1/50, 1/100) in the blow-up coordinates p = (1, s, t)/norm, with A = 3/2.
  - For the F₂-crossing pencil, both the posterior triangle and the cube hexagon meet the required tangency exactly, at their shared vertex (sA, t).
  - For the F₃-crossing pencil, the required tangent value −0.006734 lies strictly between the posterior's (−0.008919) and the cube's (−0.006712).
  - The obstruction to *homogeneous* families (K′(σs, σt) = σK′(s, t)) is PROVED: homogeneity forces straight level lines to be parallel, hence Minkowski families sP + tQ, hence boxes, and then Y3.7(a) applies.
- **Two vertices, general families.** I proved incompatibility only for boxes (Y3.7(b)). For general coherent closed vertex families it is open. CONJECTURE Y3.C: no additive field with T1 ∈ C_L has closed competitive coherent selections near two vertices. It would localise Thm gm to two vertices.

## 6. Open question

**Q_Y3.** Is there a ranking on the full domain, additive or not, with T1 ∈ C_L and a vertex plan at e₁ whose edge selections at e₁ are the posterior's, the odds intervals [r/A, rA]?

- For additive rankings, in the blow-up coordinates p = (1, s, t)/norm, k = (1, k₂, k₃), the question becomes exact. Find compact convex K′(s,t) ⊆ ℝ²_{≥0} on [0, δ]² with:
  - edges K′(s,0) = [s/A, sA]×{0} and K′(0,t) = {0}×[t/A, tA];
  - every support function (s,t) ↦ σ_{K′(s,t)}(−y) has straight level lines;
  - at the T1 levels Ac − 1 (for y = (1, −c)) and Ac′ − 1 (for y = (−c′, 1)), the level lines pass through (1, 1).
- Box (homogeneous) families fail (Y3.6). Pointwise the constraints are feasible.
- A yes answer would keep the posterior candidate's edges. A no answer would make "posterior edges at a vertex" a decisive obstruction for additive local plans, and would leave only non-additive orders for the posterior.

## 7. Status

| Item | Status |
|---|---|
| Y3.1 acceptance-vector form; box fields; axioms from Bayes uniqueness | PROVED |
| Y3.3a B₁-corner = T1 decision on Γ_η (η < 1/(A+1)) | PROVED; CHECKED (0 mismatches; control fails above 1/(A+1)) |
| Y3.3b field Ψ⁽¹⁾ = B₁ family on N, all gambles | PROVED; CHECKED |
| Y3.3c Lipschitz bound Λ = 16√(6/π)A² ⇒ explicit reservation radii | PROVED; NUMERICS |
| **Y3.2 vertex plan at e₁: all measurable competitors, explicit plan, T1 ∈ C_L, (LF); every finite fragment satisfiable with the same plan** | **PROVED** |
| Y3.3 thin competitors, cross-index comparisons, X2.2(c) records with explicit N_P | PROVED; NUMERICS for margins |
| **Y3.4 no single-vertex obstruction to T1 (vertex locality barrier)** | **PROVED** |
| Y3.5 cube system = posterior on all of ∂Δ (joint posterior edges); hexagon interior; T1 dominated | PROVED; CHECKED |
| Y3.7(a) T1-compatible box plans at a vertex are exactly B₁ (up to reparametrisation) | PROVED; CHECKED |
| Y3.6 cube/posterior-edge box plan incompatible with T1 (additive) | PROVED; CHECKED |
| Y3.7(b) no additive field with T1-compatible box plans at two vertices | PROVED; CHECKED |
| Y3.8 posterior on an open interior set has no additive realisation (identity parametrisation) | PROVED |
| Plan for the posterior selection itself near e₁ | not obtained (needs non-additive interior orders) |
| Y3.C two-vertex additive incompatibility for general families | CONJECTURE |
| Q_Y3 posterior edges at a vertex with T1 ∈ C_L | open |

**Referee priorities.**
1. Lemma Y3.3a, the case g₂ > 0 > g₃.
2. Lemma Y3.3b, the bound off Γ_η.
3. Prop Y3.7, Step 1. Pinning needs the box line to meet int N and the other acceptance to be far, which is non-adjacency of the box family.
4. The convexity of R in Step 0, via the Aumann integral over a non-atomic measure.

## 8. Files (`y3py/`)

- `y3common.py`: exact helpers.
- `y3_vertex_box.py` / `.out`: Lemmas Y3.3a, Y3.3b; field at u and at e₁ (CHECKED).
- `y3_controls.py` / `.out`: η above 1/(A+1); the cube and {1}×[1/A, A]² boxes fail at u (negative controls).
- `y3_cube.py` / `.out`: cube = double attribution; cube = posterior on ∂Δ; NUMERICS of the interior difference near e₁; algebra of Cor. Y3.6.
- `y3_twobox.py` / `.out`: Prop Y3.7(b) witness.
- `y3_lip.py` / `.out`: NUMERICS for the Lipschitz radius and the thin-competitor margins.
- `y3_pencil.py` / `.out`: the pointwise pencil feasibility for Q_Y3 (§5).
