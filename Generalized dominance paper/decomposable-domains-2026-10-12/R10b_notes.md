# R10b: obstruction attempt for the single-target additive problem (T1)

12 Oct 2026. Labels: **PROVED** (full proof written here), **CHECKED** (verified, proof sketched), **CONJECTURE**.
Citations: R1, R4 (with the repairs in R6, R8); PB = TRIANGLE_A0_A1_PROJECTIVE_BOUNDARY.md and FA = TRIANGLE_A0_A1_NOGO_FIXED_ANCHORS.md (device, CPM folder, read-only); NOGO = CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md; CSE = Conditional Shunning of Error.tex.
Script: `r10bpy/crossings.py` (classification check only; nothing below depends on it).

---

## 0. Outcome

A full impossibility proof for T1 was **not** obtained. The following hold under exactly the adopted conditions: additive rankings on a decomposable domain, strict (G), (LF) at the target only, conditions (i)–(iv) of BRIEF2, merely measurable charts, and, anywhere outside N, advice ranges that may be singletons (every evaluable model gives the same advice). They do **not** assume (H0), (H1), non-adjacency, or anything about Bayes models away from p* beyond what the axioms force.

1. **Vertex confinement (Prop V, PROVED, every n ≥ 3, every interior target).** (LF) plus coherence of the vertex Bayes models force B_{e_i} ⊆ {h_i > 0} a.e. Hence:
   * e_i ∈ K_{e_i};
   * p ↦ K_p is Hausdorff-continuous up to the vertices;
   * **acceptance (in effect) by every evaluable model can occur only for nonnegative gambles**.

   Consequences:
   * R4's escape "every evaluable model accepts deep inside D" (Remark B3) is closed.
   * (H0)_{U′} follows from non-adjacency.
   * FA's forbidden-support step, and hence the box step, holds on decomposable domains (Lemma FS).
2. **Uniform vertex neighbourhoods (Lemma UVN, PROVED).** This is the chart-level form of PB Lemma 3.1/Thm 3.2. It needs neither continuity nor non-adjacency.
3. **Locality barrier (Prop L, PROVED).** No contradiction can be derived from Bayes models at priors in any compact subset of int Δ together with (G), (LF) and the chart structure. The constant family K_q ≡ K is realisable there. So step (1) of the task cannot succeed alone: every obstruction must use interior priors accumulating at ∂Δ.
4. **Main local lemma (Lemma M, PROVED).** It concerns a facet crossing of D_K (§5). Inside any connected open set of priors that accept the inner side of the facet near the crossing, the boundary of the set of priors that also accept exterior points there consists of priors where the selection is **the single probability v** (the vertex of K owning the facet). This is the measurable, adjacency-tolerant form of PB Theorem 4.1 (exterior ratio).
5. **Two-vertex pinning is impossible (Theorem PL, PROVED).** Let K have two distinct vertices with crossings. Then there is no nonempty open set of priors on which K_q contains both vertices and stays inside their crossing wedges. In particular **K_q = K cannot hold on any open set (no plateau)**.
   * This holds for T1 for every ε ∈ (0,1), every interior triangle, interior segments, and ε-contamination of any interior baseline in every n ≥ 3.
   * It needs no (H0), no (H1), no non-adjacency, and no NOGO/PB/FA dependency.
6. **Strengthening (Cor PL2, PROVED).** Suppose exterior pairs near a facet are non-adjacent at the priors concerned. This holds, for example, if the advice ranges near ∂T are {+,0}, or if the selection is full-dimensional there. Then even **single-vertex pinning** on an open set is impossible.
7. **Scope.**
   * The obstruction mechanism is governed by **crossings**, not by "being a normalised box".
   * Normalised boxes have no crossings. So do some non-box polytopes, for example cevian hexagons that violate the box cyclic condition (explicit example in §7).
   * For n > 3 everything in items 1–6 transfers. FA's box/ray system does not transfer, and it is not needed in items 1–6.

**Remaining case for T1 (precise, §8).** T1 is open exactly in the "zero exterior ratio" regime: the selection leaves every two-vertex pinned configuration immediately near p*. In that regime the missing steps are measurable chart versions of PB §§5–6 and FA §§3–9. Adjacency (wedges) is allowed at priors away from p*.

---

## 1. Setting and notation

n ≥ 3. D = D_K is the target, with K ⊆ int Δ compact convex. (LF) holds with an open N ⊇ ∂D∖0. Shrink N so that N ∩ (−cl D) = ∅ and N contains no h ≤ 0. Then for every h ∈ N the advice range of the choice represented by h contains **accept h** and **neither** (no advice) (R1 Prop 2.5 and R6). So it is {+,0} or {+,0,−}, up to the irrelevant ×.

* Chart R(h): the set of priors at which accepting h is the unique minimiser (R1 Prop 2.1). It is relatively open and convex. For h ∈ N, c(h) := ℓ(h,0) − ℓ(h,+) has the strict sign pattern of h (R1 Lemma 1.1), and R(h) ⊆ {c(h)·p > 0}.
* K_q: interior Bayes credal sets, with B_q ≈ D_{K_q}. P(q,h) := min_{m∈K_q} m·h is jointly continuous on int Δ × ℝⁿ (R1 Prop 3.1).
* **Good h.** By Fubini, for a.e. h, {q ∈ int Δ: P(q,h) > 0} ≈ R(h) ∩ int Δ. For such h (both sets open):
  (1.1) P(·,h) ≥ 0 on cl R(h) ∩ int Δ, and P(·,h) ≤ 0 on int Δ ∖ cl R(h).
  Also, for good h, a.e. q ∈ R(h) has h ∈ D_{K_q}.
* **Open-convex facts used repeatedly.**
  * Two open convex sets that agree a.e. on an open convex set agree there.
  * If an open convex set contains a.e. point of an open convex set O, it contains O.
  * If D_{K_q} ⊇ U a.e. (U open), then D_{K_q} ⊇ U.
  * If, for a.e. q in an open set G, D_{K_q} ⊇ U⁺ (U⁺ open), then the same holds for every q ∈ G. Indeed P(q,·) ≥ 0 on U⁺ by continuity, and int cl D_{K_q} = D_{K_q}.
* **Facet, crossing, wedge.** Let v be a vertex of K whose normal cone is full-dimensional (any vertex of a polytope). Its facet is
  F_v = {h : v·h = 0, m·h ≥ 0 ∀ m ∈ K}, of dimension n−1.
  A **crossing** of v is a point w ∈ relint F_v with w_c = 0 for some world c.
  * Equivalently, coordinate c takes both strict signs on F_v.
  * Equivalently, some supporting hyperplane of K through the vertex e_c of Δ touches K only at v.
  * w is mixed, so w_j > 0 for some j.

  Fix a small ball U around w, bounded away from 0, with U ⊆ N, meeting no other facet. Put U⁺ = U ∩ D and U⁻ = U ∖ cl D. The **wedge** is
  W_v(U) := {m ∈ Δ : m·w″ ≥ 0 for all w″ ∈ F_v ∩ cl U},
  a cone in aff Δ with apex v, and K ⊆ W_v(U). Define:
  * Γ_v := {q ∈ int Δ : D_{K_q} ⊇ U⁺}. We have Γ_v ⊆ {q : K_q ⊆ W_v(U)} by continuity. Conversely {q : K_q ⊆ W_v(Ũ)} ⊆ Γ_v for a slightly larger concentric ball Ũ: write h ∈ U⁺ as h = w″ + (v·h)𝟙 with w″ ∈ v^⊥ ∩ Ũ ⊆ F_v, so m·h = m·w″ + v·h > 0;
  * α_v := {q ∈ Γ_v : D_{K_q} ∩ U⁻ = ∅}, which equals {q ∈ Γ_v : v ∈ K_q};
  * β_v := Γ_v ∖ α_v;
  * Z_v := {q ∈ int Δ : K_q = {v}}, which is relatively closed.

---

## 2. Vertex confinement

**Proposition V (PROVED; n ≥ 3, K ⊆ int Δ, (LF) at D_K).** For every world i, B_{e_i} ⊆ {h_i > 0} ∪ {h ≥ 0} a.e. Equivalently, D_{K_{e_i}} ⊆ {h_i > 0}, i.e. e_i ∈ K_{e_i}.

*Proof.*
* **A boundary point with w_i = 0.** The set {h_i = 0}∖0 is connected because n ≥ 3. It contains e_j (j ≠ i), which lies in D. It contains −e_j, which does not lie in D. So it meets ∂D∖0 at some w. Since K ⊆ int Δ, w is mixed.
* **The vertex model near w.** Take a ball B ⊆ N around w.
  * For h ∈ B, accept-h and neither are both in the advice range.
  * At e_i, accepting h is good if h_i > 0. Then it is the unique best advice in the advice range, since 0 is silence and − or × is worse.
  * If h_i < 0, accepting h is bad and 0 is better.
  * By Lemma 1.5 (uniqueness at vertices), B_{e_i} ∩ B ≈ {h_i > 0} ∩ B.
* **Coherence.** B_{e_i} is coherent (BRIEF2 (ii)), so B_{e_i} ≈ D_{K_{e_i}} ∪ {h ≥ 0}. The sets D′ := D_{K_{e_i}} ∩ B and {h_i > 0} ∩ B are open, convex and a.e. equal, hence equal. So ∂D′ contains the disc {h_i = 0} ∩ B.
* **The cone lies in {h_i > 0}.** Suppose y ∈ D_{K_{e_i}} has y_i < 0 (the case y_i = 0 follows by openness). Take λ close to 1 and 0 < δ ≪ (1−λ)|y_i|. The point λ(w + δe_i) + (1−λ)y lies in B, has negative i-coordinate, and lies in D_{K_{e_i}} by convexity. Contradiction.
* **e_i ∈ K_{e_i}.** If e_i ∉ K_{e_i}, strictly separate them in aff Δ and extend the separating affine function linearly. This gives g with m·g > 0 on K_{e_i} and g_i < 0, i.e. g ∈ D_{K_{e_i}} ∖ {h_i > 0}. ∎

**Corollary V1 (acceptance by every evaluable model; PROVED).** Say that every evaluable model accepts *in effect* on a non-null set E if the only other advice in the advice range is ×, or there is none. Then E ⊆ {h ≥ 0} a.e.
* Such acceptance is chosen at every prior, in particular at every vertex. So E ⊆ ∩_i {h_i > 0} a.e.
* The same holds for advice range {−}, applied to −h.

**Corollary V2 (continuity at vertices; PROVED).** As q → e_i in Δ, B_q → B_{e_i} in L¹. Reason: the e_i-minimiser is a.e. unique with positive gap, and dominated convergence applies. Since K ↦ 1_{D_K} is a homeomorphism onto its image (R1 Prop 3.1), K_q → K_{e_i} in the Hausdorff metric, and K_{e_i} ∋ e_i.

**Remark V3 (adjacency near vertices; CHECKED).** Let adjacent pairs h_n have d-face points p_n → e_i. By R4 Thm B, K_{p_n} ⊆ h_n^⊥. By V2, dist(e_i, h_n^⊥ ∩ aff Δ) → 0, i.e. (h_n)_i/|h_n| → 0. So wedges can act near e_i only for pairs with h_i ≈ 0. This is consistent with the FA witnesses at e_1 (a_1 = −t x_3, b_1 ≈ t/x_2) and with R4 Prop G2.

**Corollary V4 ((H0) is not an extra hypothesis; PROVED).**
* On U′ = D_{K′} (R1 Prop 2.5), acceptance is in the advice range a.e. (R1 Prop 2.4, R8).
* By V1, advice ranges in which acceptance is the only advice (in effect) occur only on nonnegative gambles. On those, the chart Δ = {c·q > 0} has c > 0, so the NOGO strict signs hold.
* Hence the only advice ranges on U′ violating (H0) are {+,−}, and these are always adjacent (R4 Thm A).

So (H0)_{U′} is implied by (H2″)_{U′}. R4 Cor B2 becomes: *no realisation of T1 satisfies (H1) and has a.e. pair meeting U′ non-adjacent* (conditional on NOGO+PB+FA, as before). R1 Thm 4.2 no longer needs R4's (H0) repair. R4 Remark B3's "separate potential escape" is closed.

**Lemma FS (forbidden support on decomposable domains; PROVED).** Let q₀ ∈ Δ with S = supp q₀, let q_η → q₀ be interior priors, and let z′ have z′_s < 0 for every s ∈ S. Then z′ ∉ cl D_{K_{q_η}} for all small η.

*Proof.*
* Take a ball B ⊆ {h_S < 0} around z′. For a.e. h ∈ B, acceptance is not in the advice range, or not every evaluable model accepts in effect (V1).
* In the second case, 0 or − is in the advice range. Both are strictly better than + at every world of S, so at q₀ acceptance is strictly suboptimal with a gap. Hence for a.e. h ∈ B, h ∉ B_{q_η} for small η, and μ(B ∩ B_{q_η}) → 0.
* If z′ ∈ cl D_{K_{q_η}}, then z′ + (open orthant) ⊆ D_{K_{q_η}}, since m·(z′ + x) ≥ min_i x_i > 0. That set occupies a fixed positive fraction of μ(B). ∎

This replaces FA §10.1's "strict signs at z′ = a+λb" and R4 (K4). It is valid on every decomposable domain under (LF). So the box (10.2) is derived from FA's facet maps without (H0). The facet maps themselves remain CONDITIONAL, as before.

---

## 3. Uniform vertex neighbourhoods

**Lemma UVN (PROVED; any n).** Let x ∈ N be mixed and let i be a world.
(a) If x_i > 0, there are a ball B₁ ∋ x and a relative neighbourhood V_i of e_i in Δ such that R(h) ⊇ V_i ∩ int Δ for a.e. h ∈ B₁, and P(q,h) > 0 for all q ∈ V_i ∩ int Δ and h ∈ B₁.
(b) If x_i < 0, there are B₁ and V_i with R(h) ∩ V_i = ∅ for a.e. h ∈ B₁, and P(q,h) < 0 for all q ∈ V_i ∩ int Δ and h ∈ B₁.

*Proof of (a).*
* Fix x⁻ < x coordinatewise, close to x, with x⁻_i > 0, and a ball B₀ ∋ x⁻ inside N ∩ {h_i > 0}.
* For a.e. h ∈ B₀, accept-h is in the advice range and is the strict minimiser at e_i. So it is the minimiser at every q within some r(h) > 0 of e_i. By dominated convergence, μ(B₀ ∖ D_{K_q}) → 0 as q → e_i.
* An open convex cone that misses x⁻ misses a half-ball of B₀ centred at x⁻. (Separate through 0: D ⊆ {ν·h > 0} with ν·x⁻ ≤ 0.) So x⁻ ∈ D_{K_q} for all interior q in some V_i.
* Upward closure gives P(q,h) > 0 for all h ≥ x⁻, in particular on a ball B₁ ∋ x.
* For good h ∈ B₁, the open convex set R(h) contains a.e. point of V_i ∩ int Δ (taking V_i convex), hence all of it.

*Proof of (b).* Mirror (a), using Lemma FS's argument at the vertex: not every evaluable model accepts in effect on {h_i < 0} (V1). Downward closure then shows that no h ≤ x⁺ is in D_{K_q}. ∎

R4 §8 (K3) obtained the negative case only on split pairs. It worked with the c-vector, which does not govern acceptance on adjacent pairs. At the level of charts no such restriction exists. Downstream steps should therefore be phrased with R(h), not with c-clusters.

---

## 4. The locality barrier

**Proposition L (PROVED).** Let Q ⊂ int Δ be compact and K ⊆ int Δ a credal set. There is an additive ranking on the all-model domain, so (LF) holds at D_K, with strictly (G)-ordered penalties, whose q-Bayes model is a.e. unique and equals D_K ∪ {h ≥ 0} for **every** q ∈ Q.

*Proof.* Use R1 Prop 2.1's converse: any measurable sign-respecting (c, c′) are realised by (G)-penalties. For a mixed pair g, choose the strict-sign vectors as follows:
* c (sign of g) with c·q > 0 on Q if g ∈ D, and c·q < 0 on Q otherwise;
* c′ (sign of −g) with c′·q > 0 on Q if −g ∈ D, and c′·q < 0 otherwise.

Such vectors exist because Q is a compact subset of int Δ: scale up the positive or the negative coordinates, measurably in g. Then on Q the three-sector chart gives "accept g" iff g ∈ D (d = c − c′ > 0 there), and silence if neither orientation is in D. Unanimous pairs get c > 0. There are no ties on Q. ∎

So K_q ≡ K is consistent with everything the axioms say at priors in any compact Q ⊂ int Δ. Every obstruction must use interior priors accumulating at ∂Δ. In R1–R4 that was the box and B1; below it is UVN only. Theorem PL needs only interior priors (no boundary-prior condition and no vertex coherence), while Prop V needs vertex coherence.

---

## 5. The main local lemma and two-vertex pinning

Fix a vertex v with a crossing w (w_c = 0, and w_j > 0 for some j), and U as in §1, inside the UVN balls at w (for j) and at points w_± ∈ F_v ∩ U′ with (w_±)_c ≷ 0 (for c). Here U″ ⊂⊂ U′ ⊂⊂ U are concentric, and w_± ∈ U″.

**Lemma D (dichotomy; PROVED).** For q ∈ Γ_v exactly one of the following holds:
(α) D_{K_q} ∩ U = U⁺, and then v ∈ K_q;
(β) D_{K_q} contains an exterior collar {h ∈ U⁻ : dist(h, F_v ∩ cl U″) < δ(q)} for some δ(q) > 0.

β_v is open. For q ∈ α_v, P(q,h) < 0 for all h ∈ U⁻.

*Proof.*
* Suppose x ∈ D_{K_q} ∩ U⁻ and w′ ∈ F_v ∩ U′. Then z = w′ + ε(w′ − x) lies in U⁺ for small ε, since v·z = −ε v·x > 0. And w′ = (z + εx)/(1+ε) is a strict convex combination, so F_v ∩ U′ ⊆ D_{K_q}. Compactness gives the collar.
* In case (α), cl D_{K_q} ∩ U ⊆ cl U⁺, so h ∈ U⁻ gives h ∉ cl D_{K_q}, i.e. P(q,h) < 0.
* β_v is open by continuity of P(·,x).
* The identifications α ⇔ v ∈ K_q and Γ ⇔ K_q ⊆ W_v(U) are standard duality. ∎

**Lemma M (exterior-acceptance boundaries are precise; PROVED).** Let G ⊆ Γ_v be open and connected. Then every Q ∈ ∂_G β_v (= cl β_v ∩ G ∖ β_v) has K_Q = {v}.

*Proof.* Suppose Q ∈ ∂_Gβ_v and K_Q ≠ {v}. Then Q ∈ α_v, so v ∈ K_Q.

*Step 1: local non-adjacency.*
* Choose ρ > 0 and a ball B := B(Q, r₀) ⊆ G with K_p ⊄ B(v, ρ) for p ∈ B (Hausdorff continuity).
* For m ∈ W_v(U) and w′ ∈ F_v ∩ cl U′: m·w′ ≥ c₀|m − v|. (Write y = m − v ∈ 𝟙^⊥. Since y·(w′+z) ≥ 0 for z ∈ v^⊥ with |z| ≤ r, we get y·w′ ≥ r|P_{v^⊥}y| ≥ rc|y|, because 𝟙^⊥ ∩ ℝv = 0.)
* Let h ∈ U⁻ have nearest facet point w′ with |h − w′| < c₀ρ. Then ℓ_h ∩ W_v(U) ⊆ B(v, |h − w′|/c₀) ⊆ B(v, ρ).
* By R4 Thm B, a d-face point p ∈ B of an adjacent good h would have K_p ⊆ ℓ_h ∩ W_v(U), since p ∈ G ⊆ Γ_v. That is impossible.
* So the d-face misses B, and B ∩ {c(h) > 0} lies on one side of {d = 0}. Hence R(h) ∩ B ∈ {∅, B, {c(h) > 0} ∩ B}. Advice range {+,0} gives the same conclusion directly.

*Step 2: chart lines through Q.*
* Q ∉ cl R(h) for good h ∈ U⁻, by (1.1) and Lemma D (P(Q,h) < 0).
* Given η > 0, pick s ∈ β_v with |s − Q| < η. For good h ∈ U⁻ within δ(s) of F_v ∩ cl U″, P(·,h) > 0 near s. So R(h) meets B(s, η).
* Hence R(h) ∩ B = {c(h) > 0} ∩ B, and the line {c(h) = 0} is within 2η of Q.

*Step 3: both sides of the crossing give the same limit.*
* Take good h₊ⁿ → w₊ and h₋ⁿ → w₋ in U⁻. Pass to subsequences with ĉ(h±ⁿ) → a±. Then a±·Q = 0, and a± is not ∝ 𝟙.
* Put H± = {a± · p > 0}.
* (i) For q ∈ H₊ ∩ B, a neighbourhood of q lies in R(h₊ⁿ) for large n. A.e. point of that neighbourhood accepts h₊ⁿ ∈ U⁻, i.e. lies in β_v. So H₊ ∩ B ⊆ cl β_v.
* (ii) For q ∈ β_v ∩ B, P(q, h₋ⁿ) > 0 for large n. So q ∈ cl R(h₋ⁿ) ∩ B ⊆ {c(h₋ⁿ) ≥ 0}, and therefore a₋·q ≥ 0.
* Hence H₊ ∩ B ⊆ cl H₋. Both boundary lines pass through Q, so a₊ = λa₋ with λ > 0, as vectors (affine functionals on aff Δ correspond bijectively to linear functionals on ℝⁿ).

*Step 4: contradiction.*
* (a₋)_c ≤ 0, because c(h₋ⁿ)_c < 0 pointwise by strict (G) at world c.
* By UVN(a) at w₊, R(h₊ⁿ) ⊇ V_c ∩ int Δ. So H₊ ⊇ V_c ∩ int Δ.
* If a₊·e_c = 0, the boundary line through e_c and the interior point Q would cut V_c ∩ int Δ. So a₊·e_c > 0, i.e. (a₊)_c > 0. Contradiction. ∎

Lemma M is the measurable, adjacency-tolerant replacement for PB Thm 4.1 ("d_{F,j} > 0 is impossible"). Strict (G) is used only at worlds c and j (UVN), and Thm B at interior priors.

**Lemma P (precise points propagate; PROVED).** Let v ≠ v′ be vertices with crossings. Let O be a nonempty open set with O ⊆ Γ_{v′} ∩ α_{v′} ∖ Z_{v′}, and let A ∈ Z_v ∩ int Δ. Then for every o ∈ O the segment [o, A) meets Z_{v′}.

*Proof.*
* Near A, K_q ≈ {v}. Moreover v·h ≥ c|h| on cl U⁺_{v′}, and v·h > 0 for exterior h near the crossing of v′ (only v′ is active on relint F_{v′}).
* So a ball B_A ⊆ Γ_{v′} ∩ β_{v′}.
* For a.e. h ∈ U⁺_{v′}, R(h) ⊇ O ∪ B_A. Hence G′ := int conv(O ∪ B_A) ⊆ Γ_{v′} (§1), and G′ ⊇ [o, A].
* By Lemma M on G′, o ∉ cl β_{v′}: otherwise o ∈ ∂β_{v′} and K_o = {v′}. Also A ∈ β_{v′}, which is open.
* The first t with q(t) ∈ cl β_{v′} lies in (0, 1). The point q(t) is in ∂_{G′}β_{v′}, so K_{q(t)} = {v′} by Lemma M. ∎

**Theorem PL (two-vertex pinning is impossible; PROVED).** Assume the axioms with (LF) at D_K, K ⊆ int Δ, n ≥ 3, and let v ≠ v′ be vertices of K that both have crossings, with balls U_v and U_{v′} chosen as above. Then there is no nonempty open set O ⊆ int Δ such that, for all q ∈ O:
* v, v′ ∈ K_q, and
* D_{K_q} ⊇ U⁺_v ∪ U⁺_{v′}, i.e. O ⊆ Γ_v ∩ Γ_{v′}.

The second condition holds whenever K_q ⊆ W_v(Ũ_v) ∩ W_{v′}(Ũ_{v′}) (§1).

**Corollary.** No open set of priors has K_q = K (no plateau). This applies to T1 (all ε ∈ (0,1)), every interior triangle, every interior segment, and ε-contamination of every interior baseline in every n ≥ 3.

*Proof.*
* O ⊆ Γ_v ∩ α_v ∖ Z_v, and the same for v′, since K_q ∋ v, v′ is not a singleton.
* UVN(a) at w (coordinate j with w_j > 0) gives V_j ∩ int Δ ⊆ Γ_v ∩ β_v. Then G := int conv(O ∪ V_j) ⊆ Γ_v.
* Along a segment from o ∈ O to e′ ∈ V_j, the first point of cl β_v is a point A ∈ Z_v (as in Lemma P).
* On [o, A], let A₁ be the point of the closed set Z_v ∪ Z_{v′} nearest o (A₁ ≠ o).
* If A₁ ∈ Z_v, Lemma P gives a point of Z_{v′} on [o, A₁). If A₁ ∈ Z_{v′}, Lemma P with the roles swapped gives a point of Z_v on [o, A₁). Both contradict the choice of A₁. ∎

For the corollary: a plateau K_q = K satisfies the hypothesis trivially, since D_K ⊇ U⁺_v ∪ U⁺_{v′}. More generally, suppose each q ∈ O has K_q ∋ v, v′ and K_q ⊆ W_v(Ũ_q) ∩ W_{v′}(Ũ′_q) for some balls (depending on q). Since the sets {q : K_q ⊆ W(Ũ_{1/m})} are relatively closed, Baire gives an open subset with uniform balls, so the theorem applies.

**Corollary PL2 (single-vertex pinning; PROVED).** Let G ⊆ Γ_v be open and connected, and suppose a.e. h ∈ U⁻ has no d-face meeting G. Then G ⊆ α_v or G ⊆ β_v. The hypothesis holds if the advice ranges on U⁻ are {+,0}, or if dim K_q = n−1 on G (Thm B). In particular, if moreover O ⊆ int α_v ∩ Γ_v is open and G = int conv(O ∪ V_j) satisfies the hypothesis, we get a contradiction.

*Proof.* In Lemma M, Step 1 is the only place where K_Q ≠ {v} was used. ∎

So, with full-dimensional selections or advice ranges {+,0} near ∂T, no vertex of K can be pinned on any open set.

---

## 6. What the corners and facets of T1 impose (task item 3)

* **Facets are the active structure.** Each facet crossing makes the inner side of the facet accepted on a region of priors containing a cone from any pinned region to a vertex neighbourhood. It forces the switch to exterior acceptance to happen only through priors whose selection is exactly the vertex probability (Lemma M). Two such vertices are incompatible with any open pinned set (Theorem PL).
* **Corners (rays of D) enter only through FA's ray matching.** That step is not used here.
* **Is the triangle's structure incompatible with affine charts per problem?**
  * Locally at (p*, ∂T), no: Prop L shows that the facet and corner structure is compatible with affine-diagram charts at priors in any compact subset of int Δ.
  * Combined with UVN at the vertices, yes in the pinned regime (Theorem PL).
* **The unpinned regime is not decided.** There, every neighbourhood of p* contains priors where K_q has moved off a vertex.

---

## 7. Scope: other targets, and n > 3

**Crossing criterion (n = 3; PROVED).**
* A vertex v has a crossing iff its two edge normals have strictly opposite signs in some coordinate.
* As the edge normal goes once round, it crosses the six coordinate walls. A wall is crossed either along an edge lying on a cevian (a line m_b = ρm_a through a vertex of Δ) or at a vertex, and in the latter case that vertex has a crossing.
* Consequences:
  * Every interior triangle has ≥ 2 crossing vertices.
    * An edge normal lies on at most one wall: two zero coordinates would put the edge on ∂Δ. So at most 3 of the 6 transitions sit on edges, and at least 3 sit at vertices.
    * A vertex's normal cone is an arc of angle < π. It can contain at most 3 of the 6 wall rays, because rays k and k+3 are opposite.
    * Suppose a single vertex hosted every vertex transition. Then it hosts exactly 3, the 3 edges lie on 3 consecutive wall rays, and that vertex's arc spans 4 gaps, i.e. more than π. This is impossible.
    * (20 000 random triangles: 0 exceptions, `r10bpy/crossings.py`.)
  * T1 has 3 crossing vertices, each with 2 crossings.
  * Normalised boxes (CSE, all worlds anchored) are cevian hexagons with **no** crossings. Theorem PL says nothing about them, consistent with their positive coverage.
* **Not a dividing line at "normalised box".** Cevian hexagons
  K = {m : m_b ≤ r_{ab} m_a} with r₁₂r₂₃r₃₁ ≠ r₂₁r₃₂r₁₃
  are not normalised boxes (boxes have r_{ab} = u_b/l_a, which forces equality of the two cyclic products). Yet they have no crossings. Example: r₁₂ = 2, r₂₃ = 2, r₃₁ = 3, r₂₁ = 2, r₃₂ = 2, r₁₃ = 1.5. The products are 12 versus 6. All six constraints are active (a hexagon), and there are no crossings (`r10bpy/crossings.py`).
  * Polygons whose non-cevian wall transitions all sit at a single vertex (exactly one crossing vertex) are also outside Theorem PL.
  * For both classes coverage is **open**: neither the CSE positive results nor these obstructions reach them.

**n > 3 (PROVED where stated).**
* Prop V, V1, V2, V4, Lemma FS, UVN, Prop L, Lemmas D, M, P, Theorem PL and Cor PL2 are written for general n. They use:
  * the n-free results R1 Prop 3.1, R1 Lemmas 1.1, 1.4, 1.5 and R4 Thm B;
  * connectivity of {h_i = 0}∖0 (n ≥ 3);
  * hyperplanes in place of lines in Lemma M.
* For ε-contamination of an interior baseline in ℝⁿ, every F_k has crossings in every coordinate x ≠ k. Take h_k = −1, h_x = 0 and the remaining coordinates equal and positive. Then relint holds (h_l > h_k for l ≠ k), and h_x can be perturbed to either sign. So Theorem PL holds there.
* FA's box/ray system (10.2)–(10.3) is three-state-specific. The full NOGO chain is **not** claimed for n > 3, as NOGO §1 already says.

---

## 8. The precise remaining case for T1

**Status.** T1 is not shown impossible. Any additive realisation on a decomposable domain must satisfy the following (all PROVED, without (H0), (H1), or non-adjacency):
* For every pair of vertices v ≠ v′ of K, the pinned set {q : v, v′ ∈ K_q, q ∈ Γ_v ∩ Γ_{v′}} is relatively closed with empty interior, and contains p*. In particular K_q ≠ K on every open set.
* For every vertex v, crossing (w, c), and j with w_j > 0, on the cone C := int conv({p*} ∪ V_j) ⊆ Γ_v:
  * either C ⊆ β_v (exterior acceptance immediately in every direction towards e_j: PB's "zero exterior ratio" regime),
  * or C meets Z_v (a prior selecting exactly the probability v).
* If the advice ranges near ∂T are {+,0}, or the selection is full-dimensional off p*, the second alternative and every single-vertex pinning are excluded (Cor PL2).
* Acceptance by every evaluable model (in effect) occurs only for nonnegative gambles. The selection is continuous up to the vertices, with e_i ∈ K_{e_i}. The box step holds on decomposable domains.

**Remaining case (open).** This is a realisation in the zero-exterior-ratio regime. Ruling it out needs measurable, chart-level versions of:
* PB §5–6: uniqueness of the exterior and interior limit half-planes at facet points, using essential clusters of R(h) along cones of approach directions instead of sequences of Φ-values;
* FA §§3–9: fixed anchors, seeds, envelope pinning, pencil test, giving the facet maps M_F;
* FA §10.2: ray matching.

With those, the box (now unconditional via Lemma FS) and Prop G1 of R4 finish the proof. Adjacency must still be tolerated at priors away from p*, i.e. the d-face wedges of R4 Prop G2 near the vertices. By Remark V3 these only occur for pairs with h_k ≈ 0 near e_k.

**CONJECTURE R10b.** The chart-level versions above hold, with every "cluster" replaced by limits of charts R(h) over sets of positive measure. Every use of continuity of Φ in PB/FA has the form "a neighbourhood with positive (negative) scalarisation". In chart form this is supplied by (1.1), UVN and Lemma D. Lemma M shows the template works for PB Thm 4.1.

---

## 9. Corrections to earlier notes

* **R1 §4.2(c) / R4 Remark B3.** Plateaus at p* are now excluded unconditionally (Theorem PL), not only under (H1)–(H2) via PB. Acceptance by every evaluable model inside D is excluded by V1.
* **R4 Cor B2.** Drop (H0) (V4).
* **R4 §8 (K3).** The negative case holds at chart level for adjacent pairs too (UVN(b)). The restriction to split pairs concerned c-clusters only.
* **R4 Prop G2.** Its decomposable-domain branch no longer needs (H0) (Lemma FS).
* **Task step (1)** as literally posed (only priors near p*) cannot succeed (Prop L).
