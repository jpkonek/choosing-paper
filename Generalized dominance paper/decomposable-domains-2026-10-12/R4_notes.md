# R4: charts for the advice range {+,0,−} ("wedge" charts) and the residual case of T1

12 Oct 2026. Labels: **PROVED** (full proof written here), **CHECKED** (verified; proof sketched or relying on a cited classical theorem), **CONDITIONAL** (proved from cited files, which I did not fully re-verify), **CONJECTURE**.
Citations: R1/R2/R3 = round-1 notes in this folder; NOGO = CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md; PB = TRIANGLE_A0_A1_PROJECTIVE_BOUNDARY.md; FA = TRIANGLE_A0_A1_NOGO_FIXED_ANCHORS.md (all three device, CPM folder, read-only); v3 = Full Coverage by Homothetic Credal Families v3.
Scripts: `r4py/dichotomy.py`, `r4py/kinked_contamination.py`, `r4py/ray_box_cap.py`.

---

## 0. Outcome

Neither (a) nor (b) is settled in full. What is settled:

1. **Adjacency dichotomy (Thm A, PROVED).** For every pair with advice range {+,0,−}, either the accept-g and accept-(−g) regions are adjacent across a segment inside int Δ (the *d-face*), or both charts are exact half-planes on int Δ. R1's "wedge" (apex in int Δ) is a special case of adjacency. Pairs with advice range {+,−} are always adjacent.
2. **Adjacency forces degenerate credal sets (Thm B, PROVED).** For a.e. adjacent pair g, every interior prior p on the d-face has K_p ⊆ g^⊥. So K_p has dimension ≤ n−2 there.
   **Consequence (Cor B2):** R1 Thm 4.2 holds with its (H2) replaced by "a.e. pair meeting U' is non-adjacent". That holds whenever all interior K_p are full-dimensional. The domain condition (H0) is automatic on the all-model domain. So T1 has **no additive realisation with full-dimensional interior credal sets** (conditional on NOGO/PB/FA and (H1), exactly as in R1).
3. **Under continuity, adjacency forces precise credal sets (Thm C, PROVED).** Assume (H1⁺): the chart data for the advice range {+,0,−} are continuous off a closed null cone. Then every adjacent pair in U' has K_p a **singleton** along its whole d-face. The proof combines a new measure lemma with Hurewicz's dimension-lowering theorem. The measure lemma (Lemma S): pairwise disjoint segments lie on a null set of lines.
   Hence, under (H0)+(H1⁺)+NOGO, a T1 realisation must contain precise segments of priors.
   Further constraints:
   * apexes are not density points of the precise set (Lemma C2);
   * open precise regions are diagonal-projective or constant (Prop D, CHECKED);
   * such regions are one-sided as seen from any non-precise prior (Prop F).
4. **Where wedges would have to act (Prop G).** The ray equations alone force ξ₁=ξ₂=ξ₃∈{x₊,x₋} (PROVED). Both values violate the box at **every** pair of vertices (PROVED).
   Given the near-q* facet structure (CONDITIONAL), every box witness at every vertex must be cut by adjacent pairs, at priors converging to that vertex. Numerically, a precise identity "cap" near e₁ performs these cuts consistently: the apex distance from e₁ is O(t) (≈ 8.6·t at t = 0.0025), and the d-rays are pairwise disjoint (§9). So no local-at-the-vertex argument from Lemma S alone closes the case.
5. **The natural exact-wedge mechanism fails (Example E, PROVED).** Take contamination with ε/(1−ε) = (f·p)⁺. It produces exactly concurrent three-sector charts, with precise d-faces as Thm B predicts. But it satisfies (G) only if f ≡ 0.
6. **(H1) / Conjecture 4.3.** I recast the problem through the jointly continuous lower prevision P(q,h) = P_{K_q}(h) (the "K-world"). Several NOGO steps then transfer without (H1) (PROVED, §8):
   * PB's strict-sign theorem (B1), on non-adjacent pairs;
   * the interior-margin lemma B2;
   * FA's forbidden-support step (on the all-model domain).
   The remaining steps (PB §§4–6, FA §§3–9) are CONJECTURE.

**Status of T1 (additive, decomposable or all-model domain, (LF)).**
* Impossible if the interior selection is full-dimensional, or more generally if a.e. pair meeting U' is non-adjacent, under (H0)+(H1). CONDITIONAL on NOGO.
* Under (H0)+(H1⁺), a realisation must use **precise d-faces**: segments of priors on which the selected model is a single probability, positioned to cut the box witnesses at all three vertices.
* No construction was found. Precise caps near the vertices are locally consistent. The global gluing (caps, apex curves, full-dimensional core) is the precise residual (§10).

Also found: R1 Thm 4.2 silently needs (H0), i.e. that on U' it is never the case that every evaluable model accepts h, or that every evaluable model gives no advice on h; see Remark B3. Acceptance by every evaluable model deep inside D is a separate potential escape, unrelated to wedges, on decomposable domains other than the all-model domain.

---

## 1. Setting and notation

As in BRIEF and R1 §§1–2. n=3 unless stated (§§2–3 hold for every n). For a pair g∈H with advice range ⊇{+,0,−} put (R1 Prop 2.1)
c = ℓ(g,0) − ℓ(g,+), c′ = ℓ(g,0) − ℓ(g,−), d = c − c′, α_g(p) = c·p, β_g(p) = c′·p.
* R(g) = {α>0, α>β}, R(−g) = {β>0, β>α}, S(g) = {α≤0, β≤0}.
* The chart is the cell decomposition of max{0, α_g, β_g}.
* By Lemma 1.1 of R1, c has the strict sign pattern of g and c′ that of −g. Hence d = c − c′ has the strict sign pattern of g, and |d_i| > max(|c_i|, |c′_i|) for every i (both P(g) and N(g)).
* For an orientation h whose acceptance is in the advice range, write c(h) for its acceptance-versus-silence vector: c(g)=c, c(−g)=c′.

**d-face.** F(g) = {p∈Δ : α_g(p)=β_g(p)>0} for the advice range {+,0,−}, and F(g) = {d·p=0}∩Δ for the advice range {+,−}. It is convex: a ray or segment of the d-line.
* K_p: for interior p, the credal set with B_p ≈ D_{K_p} (R1 Thm 2.2 (N2)). p ↦ K_p is Hausdorff-continuous on int Δ (R1 Prop 3.1).
* P(p,h) = min_{m∈K_p} m·h is jointly continuous on int Δ × ℝⁿ.
* Z = {p∈int Δ : dim K_p ≤ n−2}.
* Z_pt = {p∈int Δ : K_p a singleton} (relatively closed: diameter is continuous).
* ℓ_g = g^⊥ ∩ aff Δ is a line (n=3) in the *probability* plane. The d-line {d·p=0} lies in the *prior* plane. Both are lines in the same plane aff Δ but are different objects. g ↦ ℓ_g is injective on projective classes of non-unanimous g.

---

## 2. The adjacency dichotomy

**Theorem A (PROVED, any n).** Let g be mixed with advice range {+,0,−}. Exactly one of the following holds.
(i) *Adjacent:* F(g) ∩ int Δ ≠ ∅.
(ii) *Split:* R(g)∩int Δ = {α_g>0}∩int Δ, R(−g)∩int Δ = {β_g>0}∩int Δ, and {α_g>0}∩{β_g>0}∩int Δ = ∅.
A pair with advice range {+,−} and g mixed is always adjacent. R1's "wedge" (apex of the concurrent lines in int Δ, all three cells meeting int Δ) is adjacent.

*Proof.*
* The two cases are exclusive, since in (ii) F(g)∩int Δ ⊆ {α>0,β>0}∩int Δ = ∅.
* Suppose (i) fails. R(g) is relatively open and contains δ_i for i∈P(g) (vertex property, R1 §2), so it contains some y∈int Δ.
* Suppose x∈int Δ has α(x)>0 but x∉R(g). Then β(x)≥α(x). Equality would put x∈F(g), so β(x)>α(x).
* On the segment [x,y] ⊆ int Δ∩{α>0}, the affine function d=α−β is negative at x and positive at y. So it vanishes at some z with α(z)>0, i.e. z∈F(g)∩int Δ. Contradiction.
* Hence {α>0}∩int Δ ⊆ R(g). The reverse inclusion is trivial. The statement for R(−g) is symmetric.
* Disjointness of R(g) and R(−g) gives the last clause of (ii).
* For {+,−}, the d-line separates P(g)-vertices from N(g)-vertices (d has the strict sign of g), so it meets int Δ.
* For a wedge with apex a∈int Δ: α=β along the d-line, and the d-face is the half of the d-line on which this common value is positive. It starts at a, so it meets int Δ near a. ∎

So "wedge" is the wrong invariant. What matters is **adjacency**: R(g) and R(−g) touching along a relatively open piece of hyperplane in int Δ. The apex may lie outside Δ. (Numerical check of the dichotomy on 4000 random charts: `dichotomy.py`, 0 violations.)

---

## 3. Adjacency forces degenerate credal sets

**Theorem B (PROVED, any n).** Assume (N1)–(N2) of R1 Thm 2.2 (i.e. (LA),(S),(C)). For a.e. pair g (advice range {+,0,−} or {+,−}):
K_p ⊆ g^⊥ for every p ∈ cl F(g) ∩ int Δ.
In particular dim K_p ≤ n−2 on F(g)∩int Δ.

*Proof.*
* For each interior p, B_p ≈ D_{K_p}, i.e. for a.e. orientation h, p∈R(h) ⇔ P(p,h)>0.
* Fubini on (p,h) (as in R1 Thm 3.2(ii)), applied to the orientations g and −g, gives a co-null set G of pairs such that, for g∈G,
  {p∈int Δ: P(p,g)>0} ≈ R(g)∩int Δ and {p: P(p,−g)>0} ≈ R(−g)∩int Δ (a.e. in p).
* Fix g∈G. P(·,g) is continuous and positive a.e. on the open set R(g)∩int Δ. Hence P(·,g) ≥ 0 on its closure in int Δ. Likewise P(·,−g) ≥ 0 on cl R(−g)∩int Δ.
* Every p∈F(g)∩int Δ lies in cl R(g)∩cl R(−g): moving off the d-line keeps α,β>0 and makes d>0 on one side, d<0 on the other.
* So min_{K_p} m·g ≥ 0 ≥ max_{K_p} m·g, i.e. K_p ⊆ g^⊥. Points of cl F(g)∩int Δ follow by continuity of K. ∎

**Corollary B1 (single-map form; PROVED).** Let V be a set of orientations. Assume:
* (H0)_V: for a.e. h∈V, both accepting h and silence are in the advice range of its pair;
* (H2″)_V: a.e. pair meeting V (as g or −g) is non-adjacent.

Then for a.e. h∈V, R(h)∩int Δ = {p·c(h)>0}∩int Δ with c(h) strictly sign-preserving. Hence for every interior q,
B_q ∩ V ≈ {h∈V : q·c(h) > 0}.
(H2″)_V holds for every V if dim K_q = n−1 for all q∈int Δ (by Thm B).

*Proof.* For the advice range {+,0} this is R1 Prop 2.1. Pairs with advice range {+,0,−} are split, by (H2″) and Thm A. The advice range {+,−} cannot occur on a non-null set meeting V, since they are always adjacent. ∎

**Corollary B2 (T1 without (H2); CONDITIONAL on NOGO+PB+FA as in R1 Thm 4.2).** R1 Thm 4.2 remains true with (H2) replaced by (H0)_{U′} + (H2″)_{U′}. In particular, no additive realisation of T1 on the all-model domain satisfies (H1) and has full-dimensional K_q at every interior q.

*Proof.* R1's proof uses (H2) only to obtain that charts of orientations in U′ are half-planes {c(h)·q>0} for every interior q, with c sign-preserving. Cor B1 supplies exactly this on U′. On the all-model domain every advice range contains {+,0,−} (× is never a minimiser), so (H0) holds. ∎

**Remark B3 (a gap in R1 Thm 4.2; CHECKED).** R1's (H2) still allows the advice range {+} on U′, where every evaluable model accepts (and {0}, where every evaluable model gives no advice, on U′∖cl D). Their charts are Δ or ∅, which are not of the form {c·q>0} with c sign-preserving, so NOGO's weak-sign axiom fails at those points.
* (LF) excludes the advice ranges {+} and {0} near ∂D∖0.
* But NOGO also uses strict signs deep inside D: FA §10.1, the forbidden-support step at z′≈a+λb ∈ cl D.
* Acceptance by every evaluable model (advice range {+}) near a+λb would void that step. So R1 Thm 4.2 needs (H0)_{U′} too.
* On general decomposable domains, acceptance by every evaluable model inside D (all K_q avoiding a fixed region) is a **separate potential escape** from the box, unrelated to wedges. It is not analysed here.

---

## 4. Under continuity, adjacency forces precise d-faces

**Lemma S (disjoint segments carry a null set of lines; PROVED).** Let 𝒥 be any family of pairwise disjoint non-degenerate segments in ℝ². Then the set of lines containing a member of 𝒥 has Lebesgue measure 0 in the (θ,r)-parametrisation of lines.

*Proof.*
* *Classes.* For m∈ℕ and a segment τ with rational endpoints, let 𝒥(m,τ) consist of those J that:
  * meet τ in a single point x_J;
  * contain the closed segment of half-length 1/m centred at x_J.
  Every J lies in some class: take 1/m < (length J)/4 and a short rational τ crossing J transversally near its midpoint.
* *Lipschitz directions.* Fix a class. For J≠J′ in it, x_J≠x_{J′} (disjointness). Let δ = |x_J−x_{J′}| and let φ be the angle between their lines.
  * If φ>0, the lines meet at z, and the law of sines gives |x_J−z|, |x_{J′}−z| ≤ δ/sin φ.
  * If sin φ > mδ, then z lies in both J and J′, contradicting disjointness.
  * Hence sin φ ≤ mδ, so φ ≤ (π/2)mδ. The direction θ_J is therefore a Lipschitz function of x_J on X = {x_J} ⊆ τ.
* *Null image.* The line of J has coordinates (θ_J, x_J·n(θ_J)), a Lipschitz image of a subset of a segment. Its 2-dimensional measure is 0. Countably many classes. ∎

**Hypothesis (H1⁺).** There is a relatively closed null cone S ⊂ U′ such that, a.e. on U′∖S:
* the advice range is {+,0,−} (ignoring ×, as in R1 Prop 2.1);
* the chart data (c_g,c′_g)/‖(c_g,c′_g)‖ agree with a function continuous on U′∖S.

(H1⁺) is the analogue of (H1) for the advice range {+,0,−}, and it implies (H1) on the split pairs. A version with advice range {+,0} or {0,−} on some components is analogous.

Under (H1⁺), N′ := {g∈U′∖S : F(g)∩int Δ≠∅} is open (F(g) is lower semicontinuous in g). Thm B extends from a.e. g to every g∈N′:
* take good g_k→g and p_k∈F(g_k) with p_k→p;
* K_{p_k}⊆g_k^⊥, so K_p⊆g^⊥ by Hausdorff continuity.

**Theorem C (PROVED, n=3).** Assume (LA),(S),(C) and (H1⁺). For every g∈N′, K_p is a singleton for every p∈F(g)∩int Δ. That is, F(g)∩int Δ ⊆ Z_pt.

*Proof.*
* Let N″ = {g∈N′ : F(g)∩int Δ ⊄ Z_pt}. It is open: non-singleton is an open condition on p, and F is lower semicontinuous. Suppose N″≠∅ and let D⊂N″ be a closed disc in the (2-dimensional) projective space of pairs.
* Let ϑ: D → 𝓛 send g to its d-line {d_g·p=0}. This is a genuine line, because d_g has strict mixed signs. ϑ is continuous, since d is.
* *Fibres are countable.* Suppose g≠g′ have the same d-line L. A common non-singleton point p∈F(g)∩F(g′) would satisfy K_p ⊆ ℓ_g∩ℓ_{g′}, which is a point because ℓ_g≠ℓ_{g′}. So the non-singleton parts of the faces, F(g)∖Z_pt, are pairwise disjoint relatively open nonempty subsets of L. A line carries only countably many of them.
* *Dimension count.* ϑ is closed (D compact), and a countable compact set has dimension 0. Hurewicz's theorem for closed maps (dim D ≤ dim ϑ(D) + sup dim fibres; Hurewicz–Wallman VI.7, Engelking 1.12.4) gives dim ϑ(D) ≥ 2. A subset of the 2-manifold 𝓛 of dimension 2 has nonempty interior (Menger–Urysohn; Hurewicz–Wallman IV.3). So ϑ(D) contains an open set Λ of lines.
* *Contradiction.* For each L∈Λ choose g_L with ϑ(g_L)=L and an open sub-segment J_L ⊆ F(g_L)∖Z_pt. The J_L are pairwise disjoint: a common point would be non-singleton yet lie in K ⊆ ℓ_{g_L}∩ℓ_{g_{L′}}, a point. By Lemma S, Λ is null. Contradiction. ∎

**Lemma C2 (precise points avoid silence; PROVED).** For a.e. pair g, λ(Z_pt ∩ int S(g)) = 0. Hence, for a.e. adjacent pair whose silence cell has positive angle, the apex (if interior) is not a Lebesgue density point of Z_pt.

*Proof.*
* As in Thm B, for a.e. g we have P(·,g) ≤ 0 ≤ P̄(·,g) on int S(g)∩int Δ.
* At p∈Z_pt with K_p={σ(p)}, this says σ(p)·g = 0.
* For each p, the set {g: σ(p)·g=0} is null. By Fubini, for a.e. g the set {p∈Z_pt: σ(p)·g=0} is null.
* A density point at the apex would give positive measure inside the silence sector. ∎

**Corollary C3 (CONDITIONAL on NOGO as in Cor B2).** Under (H0)_{U′} and (H1⁺), a T1 realisation must have a nonempty **open** set N′⊆U′ of adjacent pairs, and every d-face of a pair in N′ consists of precise priors.
In particular, if Z_pt contains no non-degenerate segment, then T1 has no realisation.

*Proof.* If N′=∅, then (H2″)_{U′} holds, and (H1⁺) implies (H1); apply Cor B2. Otherwise apply Thm C. ∎

---

## 5. Open precise regions

**Proposition D (CHECKED; relies on the local fundamental theorem of projective geometry).** Let O⊆int Δ be open and connected with K_p = {σ(p)} on O. Then σ is constant on O, or σ(p) = w⊙p/(w·p) on O for some w>0.

*Sketch.*
* By Fubini, for a.e. h, {p∈O : σ(p)·h=0} is null. So silence meets O in a null set, and inside O the chart is of d-type: σ(p)·h ≷ 0 on the two sides of L_h∩O.
* By continuity, σ maps L_h∩O into ℓ_h for a.e. h, hence for all h for which ℓ_h crosses σ(O).
* (G)-signs exclude non-injective degenerate maps. For example, if σ(p) depends on p₁ only, all d-lines are {p₁=c}. Every h with ℓ_h through a fixed interior point of σ(O) would then share one d-sign pattern, but the lines through an interior point realise every mixed pattern.
* A continuous injective map of a planar domain sending segments into lines is projective (classical, local form).
* Its d-vectors d_h ∝ Aᵀh must have the strict sign of h for every h whose ℓ_h passes through a point of σ(O). As in R1's "diagonal" observation (taking h ∝ e_i×x for x∈σ(O)), this forces each column of A to be ∝ e_i, i.e. A diagonal. ∎

**Proposition F (one-sidedness; CHECKED, given Prop D's projective form).** Let O be as in D with σ non-constant, and let p_f∈int Δ with K_{p_f} not a singleton. Then no line through p_f meets O on both sides of p_f.

*Proof.*
* Suppose a line L through p_f meets O at o₁, o₂ on opposite sides of p_f. Lines L′ near L still meet O near o₁ and o₂ and pass near p_f.
* Each such L′ is L_h for a unique h (σ is a projective bijection), and a.e. L′ corresponds to a.e. h.
* For such h, by Fubini and Thm B, the two sides of L_h∩O lie a.e. in R(h) and R(−h). So L_h∩O ⊆ cl F(h).
* F(h) is convex, so it contains the whole chord between the two pieces, including a point p′ near p_f. Thm B gives K_{p′} ⊆ ℓ_h.
* By Fubini over the pencils through p′, for a.e. p′ near p_f two distinct such h exist. So K_{p′} is a singleton. By continuity K_{p_f} is a singleton. Contradiction. ∎

So precise open regions cannot surround non-precise ones. In particular there is no precise boundary "ring" around a full-dimensional core. Precise "caps" near individual vertices are not excluded.

---

## 6. T1: where adjacency would have to act

Symmetric NOGO coordinates: κ = 1+3ε/(1−ε). The realising prior can be moved to u by output rescaling (NOGO §2), so all κ_i are equal for T1.

**Proposition G1 (PROVED).** The three ray equations FA (10.3), x₃+1/x₂ = x₁+1/x₃ = x₂+1/x₁ = κ+1, have exactly two positive solutions:
x₁=x₂=x₃=x₊ and x₁=x₂=x₃=x₋=1/x₊, where x₊+1/x₊ = κ+1 and x₊>1.
Moreover x₊² > κ and x₋² < 1/κ. So **both violate the box** (10.2), at every pair of vertices: the upper box for x₊, the lower box for x₋.

*Proof.*
* x₃=T(x₂), x₁=T(x₃), x₂=T(x₁) with T(x) = s−1/x, s=κ+1>2. So x₂ = T³(x₂).
* T is the Möbius map of the matrix [[s,−1],[1,0]], which has trace s>2 and determinant 1. It is hyperbolic, so T³ has the same two fixed points as T. Positivity propagates.
* x+1/x is increasing on (1,∞), and x₊+1/x₊ = κ+1 > √κ+1/√κ. Hence x₊>√κ. The lower case follows from x₋=1/x₊. ∎

So, unlike the CPM case, the ray system itself does not single out ξ=1; only the boundary-prior box does. (Numerical confirmation: `ray_box_cap.py`, e.g. ε=0.2: κ=1.75, x₊²=5.38.)

**Proposition G2 (CONDITIONAL on the conclusions of PB §§3–6 and FA §§3–9 holding for the realisation: facet maps (10.1) and ray matching).** For every vertex e_k and all small t>0:
* every neighbourhood of the FA §10.1 witness a(t) (or of b(t)) contains a non-null set of adjacent pairs;
* each of these separates the witness prior q_η ≈ e_k + O(t) from part of its own accept-region, although α_h(q_η)>0.
Under (H1⁺) these pairs form an open set with precise d-faces (Thm C). Those d-faces separate q_η, which lies within O(t) of e_k, from points of R(h).

*Proof.*
* By G1, a box inequality fails at the pair of vertices used at e_k.
* FA §10.1: if a and b both lay in C_{q_η}, so would a+λb. But a+λb is excluded at q_η: on the all-model domain via §8 (K4), and under (H0)+(H1) via the strict signs of Φ.
* So, say, a∉C_{q_η}. A whole neighbourhood of a is then outside D_{K_{q_η}}. Yet interior points h→a have α_h(q_η)>0 by (9.3).
* By Thm A such h are adjacent; split pairs would have R(h)∩int Δ = {α_h>0}. ∎

**Caveat.** The near-q* chain itself uses priors far from q* (B1 via PB Lemma 3.1; PB Thm 4.1's Q = q*+d e_j). §8 shows B1 survives on split pairs, but adjacent pairs near vertices could in principle also disturb B1. G2 is therefore stated conditionally.

**Local consistency of vertex caps (numerical evidence, §9).** Let K_p = {p} on a cap near e₁ (identity precise model), and use the facet map M₃ with ξ=x₊.
* The apex of a(t) lies at distance ≈ 8.6·t from e₁ (t = 0.0025…0.08). The d-ray ends on edge e₁e₂ at τ ≈ 2.3t, beyond q₀ at τ ≈ t.
* The d-rays of the facet family are pairwise disjoint: they lie on the pencil of lines through the vertex v₃ of K.
* At edge level (x₊ case), a precise edge model of slope ω = w₂/w₁ is compatible with the facet α's iff ω ∈ [κ/x₂, x₃]. That interval is nonempty exactly when the upper box fails, and such an edge model then rejects both witnesses (CHECKED; blow-up computation in §9, item 4).

So no contradiction arises locally at a vertex. Note also that Lemma S does not bite on the facet family, since it is a 1-parameter pencil.

---

## 7. Example E: the natural exact-wedge mechanism and its failure

**Example E (PROVED).** Let f∈ℝ³ (an affine function on Δ) and K_p = (1−ε(p))p + ε(p)Δ with ε/(1−ε) = (f·p)⁺. For mixed h, let m = min h < 0 < M = max h.

*Exact three-sector charts.* P_{K_p}(h) ∝ p·h + (f·p)⁺m. Put
α = M p·(h+mf), β = −|m| p·(h+Mf), d = α−β = (M+|m|) p·h.
Then
* R(h) = {α>0, α>β}: in {f·p>0}, α<d·M/(M+|m|) so α>0 ⇒ d>0; in {f·p≤0}, d>0 ⇒ α>0;
* R(−h) = {β>0, β>α} (similarly);
* silence = {α≤0, β≤0}.
The three lines are concurrent at {p·h=0=f·p}, on the kink line. The d-face lies in the precise layer {f·p≤0}, exactly as Thm B requires. Numerically (`kinked_contamination.py`) the charts agree with this formula at 100% of non-tie grid points.

*(G) fails unless f=0.* (G) needs c = M(h+mf) to have the sign of h and c′ = −|m|(h+Mf) the sign of −h, for all mixed h.
* For h_i→0⁺ this forces m f_i ≥ 0, i.e. f_i ≤ 0.
* For h_i→0⁻ with i not the minimiser, it forces m f_i ≤ 0, i.e. f_i ≥ 0.
* Hence f=0, the precise model.

This is R1 Thm 4.1's (NAL) obstruction reappearing on the contaminated side. The kink mechanism produces wedges for free, but the (G)-signs of the α-vector are global conditions at all vertices, not just where α is active.

---

## 8. (H1) and Conjecture 4.3: the K-world dictionary

Work with the jointly continuous P(q,h) = P_{K_q}(h), C_q := cl D_{K_q}, and Bad as in R1 Thm 3.2. Assume (H0) and non-adjacency on U′, so ĉ := c/‖c‖ is defined a.e. on U′.

**(K1) PROVED (R1 Thm 3.2 refined).**
* For every h∉Bad, R̃(h) = {P(·,h)>0} is a.e. a half-plane H(h). Proof: limit in measure of half-planes along good h_k→h.
* ĉ is continuous on U′∖Bad in the relative topology.
* P(·,h) ≥ 0 on cl H(h) and ≤ 0 on int Δ∖H(h).

**(K2) Essential clusters; B2 transfers (PROVED).** Put U(w) = ∩_r cl{ĉ(h): h∈B(w,r)∖Bad}.
* *Forward.* If w∈D_{K_q}, every v∈U(w) has q·v>0. Proof: w∈D_{K_{q′}} for q′ near q, so q′·ĉ(h_n) ≥ 0 eventually along h_n→w. Hence q′·v ≥ 0 on a neighbourhood of q, which forces q·v>0.
* *Converse.* If q·v>0 for all v∈U(w), then P(q,·) ≥ 0 on a neighbourhood N of w (density of U′∖Bad and continuity of P). So w∈int cl D_{K_q} = D_{K_q}.

**(K3) PB Lemma 3.1 and Thm 3.2 (B1) transfer (PROVED).**
* *Positive case, valid even with adjacent pairs.*
  * x⁻ is accepted near e_i by the vertex property and openness of R(x⁻). No α-reasoning is needed.
  * So g_n ≥ x⁻ gives g_n∈D_{K_{q_s}}, i.e. P(q_s,g_n)>0.
  * But q_s·ĉ(g_n)<0 forces P(q_s,g_n) ≤ 0 by (K1).
* *Negative case, on split pairs.*
  * q_s·ĉ(g_n)>0 gives P(q_s,g_n) ≥ 0, so g_n∈C_{q_s}, and upper closure gives x⁺∈C_{q_s}.
  * Choose x⁺∉Bad with ĉ continuous at x⁺. Then q_s·ĉ<0 on a neighbourhood of x⁺, so P(q_s,·) ≤ 0 there and x⁺∉C_{q_s}.
* Thm 3.2 then follows as in PB.
* The negative case is exactly where adjacency enters: with an adjacent pair, g_n can be rejected at q_s although α_{g_n}(q_s)>0.

**(K4) Forbidden support on the all-model domain (PROVED).**
* Let q_η→q₀ with supp q₀=S. Let K* be any Hausdorff limit point of K_{q_η}.
* For a.e. h with h_S>0, accepting h is strictly best at q₀ and hence at q_η for small η. So D_{K*} ⊇ {h_S>0} a.e., i.e. K*⊆Δ_S.
* So for z′ with z′_S<0, max_{K_{q_η}} m·z′ < 0 uniformly near z′ for small η.
* This replaces NOGO's use of strict signs of Φ at z′ in FA §10.1, without (H1).

**Conjecture 4.3′.** The remaining steps transfer with Φ-clusters replaced by essential clusters U(·) and interior membership used throughout (as FA §8 already does). These are PB §§4–6 (exterior ratio law, unique facet trace, interior clusters) and FA §§3–9 (anchors, seeds, pinning, pencil test). Status: CONJECTURE. In my reading every use of continuity of Φ in those sections has the form "a neighbourhood with positive (negative) scalarisation", which (K1)–(K2) supply; but I have not re-verified the 60 KB chain line by line.

---

## 9. Numerical evidence (evidence only)

1. `dichotomy.py`: 4000 random sign-respecting (c,c′). 2699 adjacent, 1301 split. In every split case, R(g)={α>0} and R(−g)={β>0} on a 120-grid of int Δ. 0 violations.
2. `kinked_contamination.py` (f=(−1,2,2)):
   * chart agreement with Example E's concurrent formula: 1.000 on non-tie grid points;
   * every sampled d-face lies in the precise layer;
   * (G)-sign violation for 100% of sampled mixed h (expected, since f≠0).
3. `ray_box_cap.py`:
   * ray/box data for ε ∈ {.05, .2, .5, .8}: x₊² ∈ {2.20, 5.38, 22.96, 193.99}, against κ ∈ {1.16, 1.75, 4, 13}. Only x₊ and x₋=1/x₊ solve T³x=x (grid scan).
   * Identity cap at e₁ (ε=0.2, ξ=x₊):
     * |A(t)−e₁|/t rises from 5.29 to 8.61 as t decreases from 0.08 to 0.0025, i.e. the apex distance is O(t);
     * α(q₀) = 0 to machine precision;
     * d(q₀) < 0, so −a is accepted at q₀ and the cut works;
     * the d-ray endpoint lies at τ/t ≈ 2.3 > 1;
     * 0 crossings among d-rays.
4. Edge blow-up (hand computation, CHECKED; consistent with item 3).
   * Set p = e₁+t y and h = (tz, v). The facet maps give α_∞ = z + x₃κ(y₂−y₃) for the F₃-family v=(κ,−1), and α_∞ = x₂z + κ(y₃−y₂) for the F₂-family v=(−1,κ).
   * A precise edge model σ(q₀) ∝ (1, ωt, 0) at y*=(1,0) accepts (tz,κ,−1) iff z+κω>0, and (tz,−1,κ) iff z−ω>0.
   * R(h)⊆{α_h>0} for all z forces ω ≤ x₃ and ω ≥ κ/x₂.
   * At the FA witnesses, a is accepted iff ω > x₃ and b iff ω < κ/x₂. So for ω∈[κ/x₂, x₃], which is nonempty iff x₂x₃ ≥ κ, both witnesses are cut, consistently.

---

## 10. Answer to (a)/(b) and the precise residual

**(b), what is proved.** Wedge charts (advice range {+,0,−}) can rescue T1 only through **adjacency**, and adjacency costs degeneracy of the selection:
* K_p ⊆ g^⊥ on the d-face (Thm B);
* K_p a singleton under continuity (Thm C).

Hence:
* full-dimensional selections are excluded, given (H0)+(H1)+NOGO (Cor B2);
* under (H1⁺), selections whose precise locus contains no segment are excluded (Cor C3).

**(a), status.** No realisation was constructed.
* The one exact-wedge mechanism found (Example E) fails (G).
* Any realisation must have the structure below (under (H0)+(H1⁺); the vertex statements are CONDITIONAL on the near-q* chain).

**Residual R4 (open).** Does there exist an additive realisation of T1 with the following structure?
* A full-dimensional core around p*, where charts are split.
* An open set N′⊆U′ of adjacent pairs with precise d-faces. Their apexes are not density points of the precise set, and their silence sectors avoid its density points.
* Near each vertex e_k, d-faces that cut every FA §10.1 witness for all small t, within O(t) of e_k.
* Open precise regions that are diagonal-projective caps (Prop D), one-sided with respect to the core (Prop F).
* Measurable (G)-sign-respecting α,β data with the facet maps M_F (ξ ≡ x₊ or ξ ≡ x₋) near p*.

**CONJECTURE R4.** No such realisation exists. Equivalently, under (H0), a.e. pair meeting U′ is non-adjacent in any additive realisation of T1. Evidence:
* the global sign constraints (Example E);
* one-sidedness (Prop F);
* every apex of the cut pairs would have to sit on the boundary of a precise cap accumulating at each vertex, and Lemma C2 forbids it from being a density point of the cap.

The decisive missing step is a global argument tying the apex curves Γ_k (boundaries of the vertex caps) to the full-dimensional core. Prop F alone does not suffice for small caps.

**Separately open.**
* (H1)/(H1⁺) removal (Conjecture 4.3′).
* Advice ranges {+} or {0} (advice that every evaluable model gives) on domains other than the all-model domain (Remark B3).
