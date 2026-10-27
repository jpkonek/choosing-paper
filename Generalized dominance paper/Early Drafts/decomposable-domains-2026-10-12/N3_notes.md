# N3: a plateau target with NSI_θ vertex models (T1, three worlds)

13 Oct 2026. Labels as in BRIEF.md:
- **PROVED**: full proof written here, or a line-by-line transfer of a refereed proof, with every changed step written out.
- **CHECKED**: verified, with the proof sketched.
- **CONJECTURE**: not proved.
- **NUMERICS**: evidence only.

Citations: R1 (Lemmas 1.1–1.4, Prop 2.1, Prop 3.1), R4 (Thms A, B), R10b (§1 facts, (1.1), Lemma UVN, Lemmas D, M, P, Thm PL, Prop L), R12 (repairs), R14 Thm A (refereed CORRECT in R17), CCIBU.
Scripts are in `n3py/`.

---

## 0. Outcome

**The N3 strategy is impossible.** For T1, no additive system on a decomposable domain under NSI_θ can have:
- a Bayes model equal to T on an open set of interior priors (a "plateau"), together with
- a.e.-unique coherent interior Bayes models and (LF) at T.

This holds for every admissible θ, and needs no vertex or closed-choice condition. There is also no threshold to tune: the design fails for small θ and for large θ alike. NSI_θ does not weaken the no-plateau obstruction. Its exact ties actually *strengthen* it, by a new mechanism (cevian transport, §5).

1. **Exact ties (Lemma 1, PROVED).** Under NSI_θ, (G) forces ℓ_b(g,good) = ℓ_b(g,0) a.e. on the band. So the chart vector has c_b(h) = 0 *exactly* there. A band chart is therefore a cevian half-plane through e_b.
   - Consequence (Prop 2, PROVED): no NSI_θ system has a chart field with concave homogeneous components near ∂T. In particular the gauge mixtures (R10a Thm M) are not NSI_θ systems.
   - Strict-guidance systems are not NSI_θ systems either. NSI_θ is a different class, to be used alongside the strict systems.
2. **Closed choice under NSI_θ (Thm CC_θ, PROVED).** In three worlds, any additive NSI_θ system whose interior Bayes models are a.e. unique and coherent satisfies (LA), (S) and (C).
   - CCIBU's vertex rule fails here: the vertex face F_i can be 2-dimensional with no least element, and then no single value at e_i is lower semicontinuous.
   - The repair is a vertex blow-up selection.
   - This answers the brief's request to re-prove CCIBU's vertex step, and it is independent of T1.
3. **Admissibility ceiling (Prop A, PROVED).** If θ > θ_A(K) := inf{max_i h_i/‖h‖ : h ∈ ∂D_K∖0}, then D_K is not Bayes at any interior prior in any system with (LF). For T1:
   - θ_A = min{1, (1+2ε)/(2(1−ε))} in the sup norm;
   - θ_A = (1+2ε)/(√2·√(2(1−ε)²+(1+2ε)²)) in the Euclidean norm.
4. **Thm PL_θ (PROVED; unconditional).** R10b's no-plateau theorem survives NSI_θ whenever two vertices have θ-robust crossings.
   - The crossing argument (Lemma M) needs strictness at world c only at *one* facet point w₊ with (w₊)_c > θ‖w₊‖. That point can be chosen away from the crossing, outside the band.
   - For T1 this holds for every θ < θ_A (Prop S: facet midpoints are switch points).
   - So for T1 the only θ not covered is the single value θ = θ_A. In the sup norm with ε ≥ 1/4 even that value is inadmissible.
5. **Cevian transport (Thm ST, PROVED under non-adjacency (NA)).** This handles every admissible θ, including θ_A, and any norm.
   - A tie at world y near a y-crossing of a facet F_v makes the charts there cevians through e_y.
   - So the set of priors at which K_q keeps T's local facet near that crossing lies on **one line through e_y**.
   - With an open plateau this transports v ∈ K_q to priors next to e_y. There, strict y-guidance elsewhere on the same facet forces v ∉ K_q. Contradiction.
   - (NA) holds whenever the advice ranges near ∂T contain only two kinds of advice, or every interior K_q is 2-dimensional.
6. **NUMERICS.** For T1, θ_PL = θ_A in both norms, at 7 values of ε, matching the formulas to 5 digits. Over 3000–5000 random interior triangles:
   - every triangle has ≥ 2 switching vertices (so θ_PL ≥ θ_A);
   - θ_strip > θ_A, except where θ_A = 1 in the sup norm, where nothing is admissible.

**Net.** Under NSI_θ, a plateau is impossible for T1 at every θ:
- unconditionally for θ ≠ θ_A;
- at θ = θ_A, under (NA).

The answer to "how small can θ be" is that no θ works. Small θ fails by PL_θ (Lemma M is relocated off the crossing). Large θ fails by admissibility. The ties that NSI_θ adds create a new rigidity (Thm ST) that applies even to non-plateau strategies (Cor ST2).

---

## 1. Additive systems under NSI_θ

Fix a norm ‖·‖ on ℝ³. The band of world b is β_b = {g mixed : |g_b| ≤ θ‖g‖}. For an orientation h, accepting h is:
- *good-tied* at b if 0 < h_b ≤ θ‖h‖;
- *strictly good* at b if h_b > θ‖h‖;
- *bad* at b if h_b < 0.

Charts and notation are as in R1 §2: c = ℓ(0) − ℓ(+), c′ = ℓ(0) − ℓ(−), d = c − c′, and R(h) is the chart of h.

**Lemma 1 (exact ties; PROVED).** (G) under NSI_θ holds on a decomposable domain iff, for each b and a.e. g, the following hold on A(g):
- ℓ_b(g,·) is weakly increasing in the coarse world-b order and strictly increasing across its classes;
- ℓ_b(g,good) = ℓ_b(g,0) a.e. on β_b, wherever both kinds of advice are in the advice range.

Hence c_b(h) = 0 if accepting h is good-tied at b, c_b(h) > 0 if it is strictly good, and c_b(h) < 0 if it is bad. On unanimous problems everything is strict.

*Proof.* Let E ⊆ β_b be non-null with good, 0 ∈ A(g) on E. The splices X (good on E) and Y (0 on E), equal elsewhere, each weakly improve on the other in the coarse order. So L_b(X) = L_b(Y), i.e. ∫_E(ℓ_b(good) − ℓ_b(0)) dμ = 0 for every such E. Hence the integrand vanishes a.e. The strict half is R1 Lemma 1.1 verbatim. ∎

**Consequences.**
- (a) *Band charts are cevians.* Let the advice ranges be {+,0}, or non-adjacent in the sense of R4 Thm A. If accepting h is good-tied at y, strictly good at x, and bad at k, then
  R(h) ∩ int Δ = {c_x p_x + c_k p_k > 0} = {p_x/p_k > ρ(h)}, with ρ(h) = |c_k|/c_x.
  This is a half-plane bounded by a line through e_y, and it does not depend on p_y.
- (b) *Vertex property, weakened.* R(h) contains δ_i for every i at which accepting h is strictly good. Good-tied vertices lie on ∂R(h). Bad vertices lie outside cl R(h).
- (c) *What survives unchanged.* R1 Lemma 1.4 and Prop 3.1 and R10b (1.1) use only interior Bayes uniqueness and coherence (IBU). R4 Thms A and B use only chart geometry and IBU, not strict signs (re-read: Thm B's proof uses only that p ∈ F(g) lies in cl R(g) ∩ cl R(−g)). All of these hold under NSI_θ with IBU.
- (d) *UVN(a) holds* at x ∈ N, x mixed, whenever accepting x is **strictly** good at i. The proof of R10b is verbatim with B₀ ⊆ N ∩ {h_i > θ‖h‖}, which is an open condition at x. UVN(a) fails, as stated, when x_i ∈ (0, θ‖x‖].

**Proposition 2 (no concave chart fields; PROVED).** Let V be an open connected set of orientations, and let f_b be concave on a convex open W ⊇ V with sign(f_b) = sign(c_b) a.e. on V. Suppose V contains a non-null set of h with 0 < h_b < θ‖h‖ and a point with h_b > θ‖h‖. Then this is impossible.

*Proof.* Lemma 1 gives f_b = 0 on an open set O ⊆ V and f_b(z) > 0 at some z ∈ V (by continuity, near a point where c_b > 0). On a line through a point of O and z, a concave function that is zero on an interval and positive beyond it violates concavity at the end of the interval. ∎

This applies near every crossing of ∂T. So gauge mixtures (concave f_i on all of ℝ³) and the v19 concave CPM realisations are never NSI_θ systems. In particular, the earlier positive constructions (precise targets, boxes, hexagons, 9-gons) are not automatically available under NSI_θ.

**Remark.** The precise family K_p = {p} needs c(h) ∝ h, which is not NSI-admissible. So NSI_θ is a *different* class of systems from the strict ones, not a superset. Under the author's "accepted alongside" reading, a target counts as covered if either class covers it.

---

## 2. Closed choice under NSI_θ (the CCIBU vertex step)

**Theorem CC_θ (PROVED, n = 3).** Take additive penalties with integrable envelopes on a decomposable domain, satisfying (G) under NSI_θ (Lemma 1). Assume (IBU): for every w ∈ int Δ, the w-Bayes minimiser is a.e. unique and coherent. Then (LA), (S) and (C) hold, and every undominated model is coherent and is the only model with its profile.

*Proof.*

**(C) and coherence.** R14 Thm A (refereed CORRECT in R17, §0 table) shows, for any n and without strict guidance, that every efficient profile x ∈ R has exactly one realising model and that this model is coherent. Its proof uses IBU and the lexicographic perturbation only. This gives (C) as in CCIBU.

**Why CCIBU's vertex rule fails.** Let F_i = argmin_R y_i. Under NSI_θ, F_i is the Aumann integral of the {good, 0} choices over the world-i band, so it can be 2-dimensional. If band problems exist with g_j > θ‖g‖ and g_k < 0, then good and silence are ordered oppositely at j and at k. F_i then has no least element in (y_j, y_k).

For q = (1−s)e_i + s r (r ∈ conv{e_j, e_k}), the Q_q-minimisers converge to
x̂(e_i, r) := argmin_{F_i} G_r, where G_r(y) = r_j(y_j−a_j)² + r_k(y_k−a_k)².
(Proof below. NUMERICS: `n3py/blowup_check.py` shows distinct limits for r = (.9,.1), (.5,.5), (.1,.9).)

So a single value at e_i is lower semicontinuous only if it is ≤ every such limit, i.e. only if F_i has a least element (R14 Prop B1).

**Blow-up.** Let Δ̂ be Δ with each vertex e_i replaced by the arc Θ_i = {(e_i, r) : r ∈ conv{e_j,e_k}}. Interior or edge points q → e_i converge to (e_i, r) when their directions (q − q_i e_i)/(1−q_i) → r. Δ̂ is homeomorphic to the truncated triangle Δ_δ = {p : p_i ≤ 1−δ ∀ i}, via a face-preserving homeomorphism ψ: Δ_δ → Δ̂ that takes the cut segment {p_i = 1−δ} onto Θ_i by its direction coordinate r.

Define x̂ on Δ̂ as follows:
- interior q: the unique minimiser of Q_q (as in CCIBU);
- relint edge: CCIBU's edge rule;
- (e_i, r) with r ∈ relint conv{e_j, e_k}: the unique minimiser of G_r over F_i (G_r is strictly convex in (y_j, y_k), and y_i is constant on F_i);
- (e_i, e_j): minimise y_j over F_i, then minimise y_k.

**Each x̂ is efficient.** At arc points, a weak improvement z must have z_i = x̂_i, so z ∈ F_i. It must then lower G_r, or, at the endpoint, keep y_j and lower y_k. Both contradict the definition. Interior and edge cases are as in CCIBU.

**x̂ is lower semicontinuous on Δ̂.** Interior and edge points are as in CCIBU's Lemma lsc. Strict guidance is used there only at vertices, as R14 notes.

At (e_i, r), take q_m = (1−s_m)e_i + s_m r_m → (e_i, r), interior or on an edge, with minimisers x_m → z.
- Since Q_{q_m}(y) = (1−s_m)(y_i−a_i)² + s_m G_{r_m}(y), and y*_i ≤ x_{m,i} for every y* ∈ F_i, minimality gives G_{r_m}(x_m) ≤ G_{r_m}(y*). Also, in the limit, z_i ≤ y*_i, so z ∈ F_i.
- Hence z minimises G_r over F_i. For r in the relative interior this gives z = x̂(e_i,r).
- For r = e_j: z_j = x̂_j, and z_k ≥ x̂_k by the secondary rule. Edge sequences on [e_i, e_j] fall in this case, by the same inequality with r_m = e_j.
- Sequences of arc points are handled by continuity of G in r.

**The selection.** Let ρ: Δ → Δ_δ be the identity on Δ_δ. On the corner triangle N_i = {p_i ≥ 1−δ} put
ρ(p) = (1−δ)e_i + δ[λe_j + (1−λ)e_k], with λ = (δ + p_j − p_k)/(2δ).
This is continuous, λ ∈ [0,1], and it agrees with the identity on {p_i = 1−δ}.

Put σ = ψ∘ρ and C_p = the realisation of x̂(σ(p)).
- σ is continuous, so x̂∘σ is lower semicontinuous. This is exactly closedness of {p : C_p ⪯_m X}.
- supp σ(p) ⊆ supp p, where an arc point at e_i has support {i}. So C_p is supp(p)-competitive. Arc values have y_i = min y_i, so they are competitive on every S ∋ i. Competitiveness on S implies competitiveness on every S′ ⊇ S.
- Every value is efficient, hence undominated and coherent. So (LA) and (S) hold. ∎

Vertex models are now a *chosen* point of the frontier arc of F_i, namely x̂(σ(e_i)) = x̂(e_i, ½(e_j + e_k)). Vertex Bayes models are generally not unique.

---

## 3. The proposed design and the admissibility ceiling

The proposed design (N3) is a system on a decomposable domain with K_q = K = T1 on a compact Q ⊂ int Δ with nonempty interior (Prop L shows this is consistent locally). Near ∂Δ it would interpolate to vertex models that exploit NSI_θ. A natural choice is V_b = (1−δ)e_b + δΔ with δ/(1−δ) ≤ θ (sup norm). That model accepts h_b > θ‖h‖, rejects h_b < 0, and is free on the band; I checked it is coherent and consistent with the best advice in the advice range on N.

Sections 3–5 show that no such design can exist: the interior Bayes family is already inconsistent. Vertex coherence and closed choice are never reached.

**Proposition A (admissibility; PROVED).** Let K ⊆ int Δ with (LF) at D_K. Suppose some mixed h₀ ∈ ∂D_K∖0 has max_i (h₀)_i < θ‖h₀‖. Then D_K is not Bayes at any interior prior.

*Proof.*
- Near h₀ there is an open set E ⊆ D_K ∩ N on which every positive coordinate is good-tied.
- So c ≤ 0 there, with c_k < 0 for some k. Then R(h) ⊆ {c·p > 0} has empty intersection with int Δ. This holds for advice ranges {+,0} and {+,0,−}; (LF) puts + and 0 in the advice range.
- So no interior Bayes model accepts E ⊆ D_K. ∎

Hence the admissible range is θ ≤ θ_A(K) := inf_{∂D_K∖0} max_i h_i/‖h‖.

**T1.** The facet of vertex v_k is F_k: v_k·h = 0. Normalise h_k = −a with a = (1−ε)/3 and b = a + ε = (1+2ε)/3. On relint F_k:
- h_x + h_y = b, and h_x, h_y > −a;
- the leader switches at the midpoint s_k = (−a, b/2, b/2).

So θ_A = (b/2)/‖s_k‖:
- sup norm: min{1, (1+2ε)/(2(1−ε))}. For ε < 1/4 this lies in (1/2, 1); for ε ≥ 1/4 it is 1, and θ = 1 itself is inadmissible.
- Euclidean norm: (1+2ε)/(√2·√(2(1−ε)²+(1+2ε)²)), between 1/√6 and 1/√2.

(PROVED. In the sup norm, a mixed h ∈ D with one negative coordinate −a needs h_x + h_y > b. With two negatives the positive coordinate exceeds b. NUMERICS confirm both norms: `thresholds.py`.)

---

## 4. Theorem PL_θ: the crossing argument moves off the crossing

**Definition.** A vertex v of K is *θ-robust* if there are:
- a coordinate c;
- a coordinate j ≠ c;
- a compact connected set A ⊆ relint F_v containing a point with h_c < 0 and a point w₊ with (w₊)_c > θ‖w₊‖,

such that h_j > θ‖h‖ on A. Let θ_PL(K) be the supremum of θ for which K has two θ-robust vertices.

**Theorem PL_θ (PROVED).** Take an additive system on a decomposable domain under NSI_θ with IBU and (LF) at D_K, K ⊆ int Δ, n ≥ 3. If v ≠ v′ are θ-robust, then the conclusion of R10b Thm PL holds with U_v, U_{v′} taken as tubes around A_v, A_{v′}. In particular there is no open set of priors with K_q = K.

*Proof (changes to R10b, step by step).*
- **Tubes.** Replace the small ball U around the crossing by a tube U ⊆ N around A, meeting no other facet. Lemma D's collar argument needs only w′ ∈ F_v ∩ U″ and x ∈ U⁻: z = w′ + ε(w′−x) is close to w′, and v·z = −εv·x > 0. So Lemma D holds on tubes (R12: β_v is relatively open in Γ_v).
- **Lemma M.**
  - Step 1 (the estimate m·w′ ≥ c₀|m−v| on compact pieces of F_v, and R4 Thm B) is unchanged.
  - Steps 2–3 are unchanged, with w± ∈ A ∩ U″, (w₋)_c < 0, and w₊ as in the definition.
  - Step 4: (a₋)_c ≤ 0 because accepting h₋ is *bad* at c, which is still strict. (a₊)_c > 0 by UVN(a) at w₊, which applies because accepting is *strictly* good at c there (§1(d)).
- **Theorem PL.**
  - UVN(a) at every point of cl U (strict at j, by compactness) gives V_j ∩ int Δ ⊆ Γ_v ∩ β_v.
  - The open-convex fact gives G = int conv(O ∪ V_j) ⊆ Γ_v.
  - Lemma P uses only the definitions, Lemma M, and the positivity of v on cl U_{v′}⁺ (compact in relint F_{v′}).
  - The nearest-point argument is verbatim.
- No other step uses strictness. ∎

**Proposition S (switching vertices are robust below θ_A; PROVED).** Suppose that on relint F_v there are:
- a c-crossing w⁰;
- a point s with h_c(s) = h_j(s) = max_i h_i(s);
- j the largest coordinate on the arc [w⁰, s] ⊆ relint F_v.

Then v is θ-robust for every θ < θ_A.

*Proof.* On [w⁰, s], h_j = max_i h_i ≥ θ_A‖h‖ > θ‖h‖. At s, h_c = h_j > θ‖h‖. Extend the arc slightly past w⁰ (by continuity) to get a point with h_c < 0. ∎

**T1.** On F_k, w⁰ = (−a, 0, b) is the x-crossing, s = s_k, and y leads on [w⁰, s_k]. So all three vertices switch, and θ_PL(T1) ≥ θ_A(T1). Since θ ≤ θ_A is necessary (Prop A), **no plateau exists for any θ < θ_A**. The case θ = θ_A is the only one left; there s_k lies on the band boundary of both x and y. For general triangles, NUMERICS (`switching.py`, 5000 triangles) found no triangle with fewer than 2 switching vertices. CONJECTURE: every interior triangle has ≥ 2.

---

## 5. Cevian transport: the NSI ties themselves obstruct the plateau

**Theorem ST (PROVED under (NA)).** Assume the following:
- an additive NSI_θ system with IBU and (LF) at D_K, K ⊆ int Δ, n = 3;
- U ⊆ N is a tube around a compact piece A ⊂ relint F_v such that on cl U, h_y ∈ (0, θ‖h‖), h_x > θ‖h‖ and h_k < 0;
- (NA): a.e. pair meeting U is non-adjacent (R4 Thm A, split);
- some w₊ ∈ relint F_v has (w₊)_y > θ‖w₊‖.

Then Π_U := {q ∈ int Δ : D_{K_q} ∩ U = U⁺} lies on a single line through e_y. In particular, no open set of priors keeps the target facet near A, and there is no plateau.

*Proof.*
1. By §1(a), for a.e. h ∈ U, R(h) ∩ int Δ = {p_x/p_k > ρ(h)}.
2. Suppose q₁, q₂ ∈ Π_U with ratios r₁ < r₂ (where r = p_x/p_k). Fubini at the two priors gives:
   - for a.e. h ∈ U⁺: q₁, q₂ ∈ R(h), so ρ(h) < r₁;
   - for a.e. h ∈ U⁻: q₁, q₂ ∉ R(h), so ρ(h) ≥ r₂.
3. Hence every p in the cevian strip S = {r₁ < p_x/p_k < r₂} satisfies B_p ∩ U ≈ U⁺.
4. By the open-convex facts (R10b §1), D_{K_p} ⊇ U⁺ and D_{K_p} ∩ U⁻ = ∅. Then v ∈ K_p: otherwise separate to get g ∈ D_{K_p} with v·g < 0. For w ∈ A, the point w + δg lies in U⁻ ∩ (cl D_{K_p} + D_{K_p}) ⊆ U⁻ ∩ D_{K_p}, a contradiction.
5. S is a cone with apex e_y, so it meets every neighbourhood V_y of e_y.
6. UVN(a) at an exterior point x near w₊ (strictly good at y) gives x ∈ D_{K_q} for q ∈ V_y ∩ int Δ. Since v·x < 0, this means v ∉ K_q, contradicting step 4 on S ∩ V_y.
7. Hence Π_U has a single ratio. For an open set, take two points of it with distinct ratios. ∎

**T1, all admissible θ.** Take v = v_k and A near the y-crossing (−a, b, 0) of F_k, on its side where h_y > 0:
- y is good-tied there, for any θ > 0;
- x is strictly good there, with ratio b/max(a,b) = 1 > θ in the sup norm and b/√(a²+b²) > 1/√2 > θ_A in the Euclidean norm;
- k is bad.

For w₊, take a point near the corner F_k ∩ F_x, where y is the only positive coordinate. Its ratio is 1 (sup norm) or ≥ 0.816 > θ_A (Euclidean).

Hence, **under (NA), no plateau for T1 exists at any admissible θ, including θ = θ_A**. Admissibility itself forces the existence of w₊: near that corner y is the only positive coordinate, so it must be strictly good.

NUMERICS (`strip_threshold.py`, 3000 random triangles): θ_strip > θ_A in the Euclidean norm, with minimum gap 0.094. In the sup norm θ_strip ≥ θ_A, with equality only when θ_A = 1, where no θ is admissible.

**Corollary ST1 (any tie rule).** The proof uses only two things:
- an exact tie at y on an open piece of F_v next to a y-crossing;
- strictness at y somewhere on the same facet.

Admissibility supplies the second. So every NSI-type rule (good ~ silence for small positive stakes, strict for leading stakes, any norm or stake measure) excludes plateaus for T1 under (NA).

**Corollary ST2 (beyond plateaus).** In any NSI_θ realisation of T1 under (NA), the set of interior priors that keep T's local facet near each tied crossing piece lies on the line through e_y and p*. This is a rigidity constraint for non-plateau strategies too: it is stronger than strict guidance's Lemma M, which only constrains the boundary of β_v.

**Without (NA).** CHECKED (sketch): along a segment of S from Q towards e_y, the first prior with v ∉ K_q has K_q = {v}. The reason is that adjacency points p′ have K_{p′} ⊆ h^⊥ (Thm B), which is incompatible with v ∈ K_{p′} because v·h > 0. A Hausdorff limit then gives K ⊆ W_v ∩ h₀^⊥ = {v}. But exterior rejection on S itself needs (NA). So the case θ = θ_A without (NA) is open.

---

## 6. Answers to the task

**(1) Validity.** No valid system has Bayes model T on an open set:
- unconditionally for θ < θ_A (Thm PL_θ with Prop S);
- under (NA) for every admissible θ (Thm ST);
- for θ > θ_A, T is never Bayes (Prop A).

Every proposed design breaks at the interior priors: IBU together with coherence fails somewhere in the cevian strips. The breakdown occurs before vertex coherence or closed choice can be checked. Closed choice is not the bottleneck: Thm CC_θ provides it for every IBU system.

(LF) at T and (C) are not reached; (C) holds automatically whenever IBU holds (R14 Thm A).

**(2) θ.** The design fails for every θ > 0, and no threshold rescues it. The relevant constants are θ_PL(K) ≥ θ_A(K) and θ_strip(K) > θ_A(K) (T1 proved; triangles NUMERICS). For T1:
- θ_A = min{1, (1+2ε)/(2(1−ε))} in the sup norm;
- θ_A = (1+2ε)/(√2·√(2(1−ε)²+(1+2ε)²)) in the Euclidean norm.

The norm changes these constants but no conclusion.

---

## 7. Remarks and open items

- **Why the author's heuristic fails.** NSI_θ removes strictness exactly at the crossings. Lemma M only needs strictness at one point on the positive side of the facet, and for every admissible θ such a point exists (it is the switch point). Worse, the exact ties make band charts independent of p_y, which transports pinning along cevians to the vertex.
- **What would be needed** for a plateau to survive: ties at y on all of F_v ∩ {h_y > 0}. That contradicts admissibility near the corner F_v ∩ F_x. So for triangles with crossing facets, no tie rule built on good ~ silence gives a plateau under (NA).
- **Nearby reachable direction.** The plateau route is closed. NSI_θ realisations of T1, if any exist, must have K_q leave T immediately, with the pinned sets on single cevians (Cor ST2). Thm CC_θ supplies closed choice for any such family. The open question is IBU coherence in that regime; that belongs to N1/N2. Prop 2 shows the known concave constructions cannot be reused there.
- **Open.**
  - θ = θ_A without (NA).
  - Whether every interior triangle has two switching vertices (NUMERICS: yes).
  - n ≥ 4: Thm ST and PL_θ transfer (cevians become planes through e_y); Thm CC_θ does not.

## Scripts (n3py/)

- `thresholds.py`: θ_A and θ_PL for T1 (7 values of ε, both norms; they match the formulas) and for random triangles. The coarse grid misreports thin triangles; refinement removes the apparent gaps (`window_fine.py`, `window_one.py`).
- `switching.py`: counts switching vertices; every random triangle has ≥ 2 (5000 sampled).
- `strip_threshold.py`: θ_strip versus θ_A.
- `blowup_check.py`: directional vertex limits on a synthetic attainable set with a 2-dimensional bottom face.
