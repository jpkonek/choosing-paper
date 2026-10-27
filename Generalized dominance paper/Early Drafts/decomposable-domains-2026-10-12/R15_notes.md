# R15: corner rays with merely measurable charts

13 Oct 2026. Labels as in BRIEF.md:
- **PROVED**: full proof written here.
- **CHECKED**: verified, with the proof sketched.
- **CONJECTURE**: not proved.
- **NUMERICS**: evidence only.

Citations:
- R1 (Lemma 3.5, Prop 3.1, table of Prop 2.1), R4 (Thm A, Thm B, Prop G1), R10a (Thm R, Thm M, Prop M′) and R10b (Prop V, Lemma FS, Lemma UVN, Lemma M, Thm PL), all with the repairs in R6, R8 and R12.
- CCIBU, which needs nothing at boundary priors.

Scripts are in `r15py/`.

---

## 0. Outcome

The decisive question is **not settled**. This round does three things:
- It finds the exact mechanism by which corner rays act on merely measurable charts.
- It shows that the R10a ray lemma does **not** generalise as a pure corner-ray statement.
- It proves a no-go for T1 under one first-order regularity hypothesis at p\*, using in addition a vertex-limit form of the box. The same no-go covers every ε-contamination triangle and, more generally, every "all-facing" triangle in general position.

1. **First-order corner calculus (Thm 1, PROVED).** Assume the hypotheses (DF) and (ND) below.
   - (DF) says that q ↦ P_{K_q}(h) is Gâteaux-differentiable at p\* for h in the relative interiors of the facets of D_T.
   - (ND) says that the derivative is not identically zero on any facet.

   Under (DF) and (ND), the merely measurable chart field has the following structure at p\*:
   - (a) the facet maps are linear;
   - (b) the essential cluster at each facet point is unique;
   - (c) each crossing gives a crossing row λ_{ik}e_i with λ_{ik} > 0;
   - (d) **corner proportionality**: Γ_k r ∝₊ Γ_j r at every corner ray r.

   Concavity of the chart representatives (R10a Thm R) is replaced by concavity of the **support function** h ↦ P_{K_q}(h). That concavity holds for every family. Corner proportionality (d) needs no corner hypothesis: concavity at the corner and the cluster separation of R10b (1.1) force it.
2. **The target prior is irrelevant at first order (Lemma 4.1, PROVED).** The substitution y = q/p\* (diagonal) carries every first-order constraint for (T, p\*) to the constraints for (T, u).
3. **The corner rays alone are consistent for T1 (Prop 5.2, PROVED).** For T1 the corner system is exactly FA (10.3) / R4 Prop G1, x + 1/x = κ + 1, with two positive solutions x₊ and x₋ = 1/x₊. Both satisfy every vertex sign condition.
   - The concave case adds the rank-one condition λ_{ik} = ξ_k α_i (one α per coordinate). That condition, and only that condition, makes the corner rays contradictory (this recovers Thm R).
   - So **"three corner constraints force p\*_i α_i = 0" is false for general measurable, or even smooth, fields**.
4. **A pure corner-ray no-go does exist for one class (Thm 5.1, PROVED).** If two vertices of T are each tangent from all three e_i (crossing distribution (·,3,3)), the corner between their facets cannot match. This holds under (DF) and (ND) alone: no box, no adjacency hypothesis.
5. **Vertex-limit box (Lemma 6.1, PROVED).** Use R10b Lemma FS at edge priors that converge to a vertex e_b, with witnesses near the two b-crossings. This gives six necessary inequalities Λ_{ab} ≤ 1, which are explicit in the first-order data. The hypothesis (NA_w) is needed: the witness pairs must be non-adjacent. It holds if every interior K_q is 2-dimensional.
6. **Main conditional theorem (Thm 6.2, PROVED).** Let T be an interior triangle in general position of **all-facing** type: each e_k sees one vertex of T in front of the opposite edge. This class contains T1 and every ε-contamination of an interior baseline. Then there is **no** strictly guiding additive realisation of D_T on a decomposable domain with:
   - (LF) at the target;
   - unique coherent interior Bayes models;
   - (DF) and (ND) at the target prior p\*;
   - (NA_w).

   This holds for **every** interior p\*. The proof is short: the box and the corners pinch every facet ratio to a vertex coordinate ratio, and this forces an edge line of T through a vertex of Δ.
   - For T1 alone: the box says 1/κ ≤ x² ≤ κ, which gives x + 1/x ≤ √κ + 1/√κ < κ + 1.
7. **Why hexagons and 9-gons escape (§8).** In the (DF) + (NA_w) class, where all known covered polygons live, the triangle's first-order system is **rigid**: 3 unknowns, 3 corner equations. The box can then be met only with equality, and only in non-general position. For an N-gon the system has 2N − 6 free parameters.
   - The covered gauge-mixture polygons satisfy the box with slack: Λ = 0.25 for the hexagon and 0.42 / 0.44 for the 9-gons near T1.
   - For T1, Λ_max = x₊²/κ, for example 3.80 at ε = 0.3.
8. **NUMERICS for all general-position triangles.** Over about 1350 random triangles, every sign-admissible ray solution violates a vertex-limit box inequality. That is 900 solutions, in the (1,2,3) and (2,2,2) classes. The (0,3,3) class never has a solution, as Thm 5.1 says.
   - Optimising over triangles drives the minimum of Λ_max to 1⁺, and only as the triangle leaves general position.
   - **CONJECTURE R15**: Thm 6.2 holds for every interior triangle in general position.

**Exact remaining steps (§9).**
- (i) Remove (DF): handle kinked facets, sliding edges at corners, and first-order-flat facets.
- (ii) Remove (NA_w): this is the R4 adjacency residual near the vertices. It now requires degenerate K_p ⊆ h^⊥ ≈ line(e_b, v_k) on d-faces that separate the box witnesses from p\*.
- (iii) Prove CONJECTURE R15 for the (1,2,3) and non-facing (2,2,2) classes.

---

## 1. Setting and hypotheses

**Standing hypotheses (SH).**
- n = 3, with an additive strictly guiding system on a decomposable domain.
- For every q ∈ int Δ the Bayes model is a.e. unique and coherent: B_q ≈ D_{K_q}.
- T = conv{v_1, v_2, v_3} ⊆ int Δ is a triangle in general position: no edge line contains a vertex of Δ.
- D_T = B_{p\*} with p\* ∈ int Δ, and (LF) holds at D_T.
- By CCIBU these give (LA), (S), (C). By R10b Prop V the vertex models satisfy e_i ∈ K_{e_i}.

**Notation.**
- P(q, h) = P_{K_q}(h) = min_{m∈K_q} m·h. It is jointly continuous on int Δ × ℝ³ (R1 Prop 3.1). It is **concave and positively homogeneous in h** for each q.
- Facets of D_T: F_k = {h : h·v_k = 0, h·v_j ≥ 0 (j ≠ k)}, the normal cone of T at v_k.
- Corner (edge) rays: r_{kj} ∝ v_k × v_j, with r·v_l > 0. They correspond to the edges [v_k, v_j] of T.
- Coordinate i **crosses** on F_k if some w ∈ relint F_k has w_i = 0. Then w = w_{ik} ∝ v_k × e_i. Equivalently, line(v_k, e_i) supports T at v_k only. C_k denotes the set of crossing coordinates of F_k.
- General position gives exactly 6 crossings in total: each e_i has two tangent vertices. It also gives r_i ≠ 0 for every corner ray. The crossing distributions are (2,2,2), (1,2,3) and (0,3,3).
- Q is the convex neighbourhood of p\* from R1 Lemma 3.5. For a.e. g near ∂D_T, R(g) ∩ Q = {c(g)·q > 0} ∩ Q, and globally R(g) ⊆ {c(g)·q > 0}.
  - This uses the following facts. (LF) puts both + and 0 in the advice ranges near ∂D_T. For the advice range {+,0,−}, R = {c > 0, d > 0}. Near p\* there are no d-faces, because dim K_q = 2 there.
  - c(g) has the strict sign pattern of g.
- **Good** h: the representation above holds, and R10b (1.1) holds: P(·, h) ≥ 0 on cl R(h) and ≤ 0 off it. Good h form a co-null set.
- **Cluster set** Cl(h): the set of limits of ĉ(h_n) = c(h_n)/|c(h_n)| over good h_n → h. It is defined for **every** h.

**First-order hypotheses at p\*.**
- **(DF)** For each k and h ∈ relint F_k, q ↦ P(q, h) is Gâteaux-differentiable at p\*: P(p\* + tδ, h) = t γ_k(h)·δ + o(t) as t → 0 (both signs), for every δ ∈ 𝟙^⊥, with γ_k(h) ∈ (𝟙^⊥)\*.
- **(ND)** γ_k ≢ 0 on relint F_k, for each k.
- **(NA_w)** A.e. pair near the witness facet points used in §6 is non-adjacent. Then its chart is the full half-plane: R(g) ∩ int Δ = {c(g)·q > 0} ∩ int Δ (R1 table; R4 Thm A(ii)).
  - **(FD)** "dim K_q = 2 for all q ∈ int Δ" implies (NA_w), by R4 Thm B.

None of (DF), (ND), (NA_w) is implied by the axioms (§9). All three hold in every known covered system (gauge mixtures, R10a Thm M), and so do (SH).

---

## 2. Clusters (PROVED)

**Lemma C.** Under (SH), for every h near ∂D_T∖0 (not only good h) and every ĉ ∈ Cl(h):
- A⁺(h) := {q ∈ Q : P(q, h) > 0} ⊆ {ĉ·q > 0};
- A⁻(h) := {q ∈ Q : P(q, h) < 0} ⊆ {ĉ·q < 0};
- ĉ·q is a non-constant affine function on aff Δ.

*Proof.*
- Take q ∈ A⁺(h). By joint continuity P(q, h_n) > 0 for large n. By (1.1), q ∈ cl R(h_n), so ĉ(h_n)·q ≥ 0, and hence ĉ·q ≥ 0. A⁺(h) is open, so A⁺(h) ⊆ int{ĉ·q ≥ 0} = {ĉ·q > 0}.
- Take q ∈ A⁻(h). Then P(q, h_n) < 0, so q ∉ cl R(h_n) by (1.1), and ĉ(h_n)·q ≤ 0. Conclude as before.
- Non-constancy: h is mixed, so ĉ has weak signs with ĉ_i ≥ 0 ≥ ĉ_j for some i, j. Hence ĉ ∝ 𝟙 forces ĉ = 0, contradicting |ĉ| = 1. ∎

---

## 3. First-order corner calculus

**Theorem 1 (PROVED).** Assume (SH), (DF), (ND). For each k:

**(a) Facet linearity.** There is a linear map Γ_k : v_k^⊥ → (𝟙^⊥)\* with γ_k(h) = Γ_k h on relint F_k.

*Proof.*
- Fix δ. For t > 0, φ_t(h) = P(p\* + tδ, h)/t is concave in h. For t < 0 it is convex.
- Both converge on relint F_k to h ↦ γ_k(h)·δ. So the limit is concave and convex, hence affine on the open cone relint F_k ⊆ v_k^⊥.
- Positive homogeneity makes it linear. Linearity in δ is part of (DF). ∎

**(b) Unique clusters.** For h ∈ relint F_k with Γ_k h ≠ 0, Cl(h) = {ĉ_k(h)}. Here ĉ_k(h) is the unit vector with ĉ·p\* = 0 and ĉ|_{𝟙^⊥} ∝₊ Γ_k h. Note ℝ³ = 𝟙^⊥ ⊕ ℝp\*, and restriction is an isomorphism p\*^⊥ → (𝟙^⊥)\*.

*Proof.*
- If Γ_k h·δ > 0, then p\* + tδ ∈ A⁺(h) and p\* − tδ ∈ A⁻(h) for small t > 0.
- Lemma C gives ĉ·p\* ± t ĉ·δ ≷ 0. Let t ↓ 0: ĉ·p\* = 0 and ĉ·δ > 0.
- So {Γ_k h·δ > 0} ⊆ {ĉ·δ > 0}, i.e. ĉ|_{𝟙^⊥} ∝₊ Γ_k h. ∎

**(c) Crossing rows.** If i ∈ C_k, then Γ_k h·(e_i − p\*) = λ_{ik} h_i for all h ∈ v_k^⊥, with λ_{ik} > 0.

*Proof.*
- Take good sequences converging to w = w_{ik} from {h_i > 0} and from {h_i < 0}. Their clusters satisfy ĉ_i ≥ 0 and ĉ_i ≤ 0 respectively (strict sign patterns of c).
- By (b) the cluster is unique, so ĉ·e_i = 0. Since ĉ·p\* = 0, this gives Γ_k w·(e_i − p\*) = 0.
- The functional h ↦ Γ_k h·(e_i − p\*) on the plane v_k^⊥ vanishes on ℝw = v_k^⊥ ∩ e_i^⊥, so it equals λ_{ik}h_i.
- Positivity. For h ∈ relint F_k with h_i > 0, apply R10b UVN(a): R(h′) ⊇ V_i ∩ int Δ for a.e. h′ near h, and R(h′) ⊆ {c(h′)·q > 0}. So ĉ(h)·q ≥ 0 on V_i.
- The zero line of ĉ(h) passes through p\* ∈ int Δ. If it also passed through e_i, it would cut V_i. Hence ĉ·e_i > 0, i.e. λ_{ik} > 0. ∎

**Lemma 3.2 (PROVED).** If |C_k| ≥ 2, then (ND) on F_k implies that Γ_k is nonsingular.

*Proof.*
- Suppose rank Γ_k = 1 with kernel ℝh₀. All clusters on relint F_k∖ℝh₀ have one common zero line ℓ ∋ p\*.
- If h₀ is not a crossing, the two crossings put e_i and e_{i′} on ℓ. Together with p\* ∈ int Δ, that is impossible.
- If h₀ = w_{ik}, the other crossing puts e_{i′} ∈ ℓ. Then ĉ·e_{i′} = 0 at points with h_{i′} > 0, contradicting the strict sign obtained in (c). ∎

**(d) Corner proportionality.** Let r = r_{kj}. If Γ_k r ≠ 0 ≠ Γ_j r (for example both facets have ≥ 2 crossings), then Γ_k r = κ Γ_j r with κ > 0.

*Proof.*
1. *Both facet limits are clusters at r.* As h → r in relint F_k, ĉ_k(h) → ĉ_k(r) (the normalised Γ_k r with ĉ·p\* = 0). A diagonal argument puts ĉ_k(r) ∈ Cl(r). Likewise ĉ_j(r) ∈ Cl(r).
2. *Upper bound at the corner.* Take h₀ ∈ relint F_k and x_θ = (1 − θ)r + θh₀. Concavity of φ_t (t > 0) gives
   φ_t(r) ≤ [φ_t(x_θ) − θφ_t(h₀)]/(1 − θ) → Γ_k r·δ.
   So limsup_{t↓0} P(p\* + tδ, r)/t ≤ min(Γ_k r·δ, Γ_j r·δ).
3. *Conclusion.* Suppose ĉ_k(r) ≠ ĉ_j(r). Both lie in the 2-dimensional space p\*^⊥, so some δ ∈ 𝟙^⊥ has ĉ_k·δ < 0 < ĉ_j·δ.
   - By Step 2, P(p\* + tδ, r) < 0 for small t > 0, i.e. p\* + tδ ∈ A⁻(r).
   - Lemma C with ĉ_j ∈ Cl(r) then gives ĉ_j·δ < 0. Contradiction. ∎

**Remarks.**
- No uniformity of the o(t) in h is assumed. In particular (DF) is not assumed at the corner rays.
- Without (DF), Step 2 is unavailable, and two distinct clusters at r are not excluded. That configuration is a **sliding edge**: P(q, r) = 0 on two open side wedges at p\*, so K_q keeps an edge on the fixed line r^⊥ and slides past v_k (§9).
- Without two-sidedness, the argument of (a) gives only that the sign of γ along a facet changes at most once (monotone line fields), not linearity.

---

## 4. The ray system; the target prior drops out

**First-order chart forms.** Put c_k(h)_i := Γ_k h·(e_i − p\*). For q ∈ Δ, the first-order chart line of a facet gamble h ∈ F_k is {q : Σ_i q_i c_k(h)_i = 0}. This line passes through p\*. By (b) it is the line of the unique cluster at h, a global line.

From Σ_i p\*_i(e_i − p\*) = 0, with μ_{ik} := p\*_i λ_{ik}:
- |C_k| = 3: c_k(h) = m_k (h ⊙ v_k ⊘ p\*), with m_k > 0. The facet map is diagonal-projective.
- |C_k| = 2, C_k = {i, i′}, third coordinate l:
  - c_k(h)_i = λ_{ik}h_i and c_k(h)_{i′} = λ_{i′k}h_{i′};
  - c_k(h)_l = −(μ_{ik}h_i + μ_{i′k}h_{i′})/p\*_l.
- |C_k| = 1 or 0: the remaining entries are free, subject to the sign conditions.

**Lemma 4.1 (diagonal invariance; PROVED).** Write y = q/p\* and ĉ_i = p\*_i c_k(h)_i. Then Σ q_i c_k(h)_i = Σ y_i ĉ_i, and the ĉ are the p\* = u forms with λ replaced by μ. The following transfer verbatim between (T, p\*) and (T, u), because q ↦ y/Σy is a face-preserving bijection of Δ and only signs and proportionality enter:
- the corner conditions (proportionality is invariant under diagonal scaling);
- the vertex sign conditions;
- the acceptance signs at every prior, including edge priors.

**NUMERICS** (`pstar_invariance.py`): Λ_max is identical to 6 digits across five p\*, for a random triangle and for T1. ∎

**Parameter count.**
- Each facet map has 4 entries. There are 6 crossing conditions and 3 facet scales, leaving 3 projective parameters.
- There are 3 corner equations.
- So the system is **rigid** for every triangle. For (2,2,2) it is a composition of three Möbius relations around the cycle, which has at most two fixed points.

---

## 5. What the corner rays do and do not give

**Theorem 5.1 ((·,3,3) triangles; PROVED).**
- Statement: if two vertices v_k, v_j of T are each tangent from all three e_i, then (SH), (DF), (ND) are inconsistent. No box and no adjacency hypothesis is needed.
- Proof: by (c), c_k(r) ∝ r ⊙ v_k ⊘ p\* and c_j(r) ∝ r ⊙ v_j ⊘ p\* at r = r_{kj}. By (d) they are proportional. Since r_i ≠ 0, this forces v_k ∝ v_j, hence v_k = v_j. ∎
- (A singular Γ_k is excluded by Lemma 3.2.) This is the one class where a genuine measurable "ray lemma" holds.

**Proposition 5.2 (T1: corner rays are satisfiable; PROVED).**
- Statement:
  - T1 has crossing distribution (2,2,2), with C_k = {i ≠ k}.
  - Write a = λ_{21}/λ_{31}, b = λ_{32}/λ_{12}, c = λ_{13}/λ_{23} (in μ-form for general p\*).
  - Theorem 1 reduces to a + 1/b = b + 1/c = c + 1/a = κ + 1, with κ = 1 + 3ε/(1 − ε). These are FA (10.3) / R4 G1.
  - By R4 G1 the only positive solutions are a = b = c = x₊ or a = b = c = x₋ = 1/x₊, where x + 1/x = κ + 1.
  - Both satisfy every vertex sign condition (sign c_k(h)·e_i = sign h_i on F_k).
- Proof:
  - The corner r_{12} = (−1, −1, κ + 1) has (c_1(r), c_2(r)) proportional iff (1/(κ+1))(a + 1/b) = 1. The other two corners follow by cyclic symmetry.
  - The only non-crossing sign condition is at e_1 on F_1, and similarly for the other facets. It reads 1/(κ+1) < a < κ + 1, and x₊, x₋ satisfy it.
  - `raysys.py` reproduces a = x₊ and a = x₋ to 1e-14. ∎

**Proposition 5.3 (what concavity adds; PROVED).**
- For a concave representative f (R10a Thm R), γ_k(h) = f(h)/(𝟙·m\*_k). Here m\*_k is the vertex of S_{p\*} over v_k. Hence λ_{ik} = ξ_k α_i, with one α per coordinate.
- For a triangle this rank-one condition is one extra equation. For T1 it is abc = 1, and then α_1 + α_2 = (κ+1)α_3 (cyclically), which forces κ = 1.
- **Consequence:** the R10a contradiction comes from the rank-one structure, not from the corner rays. The corner rays allow x₊ and x₋. Any measurable no-go for (2,2,2) triangles must use more than the data at p\*. Given Prop L, it must use priors accumulating at ∂Δ.

---

## 6. The vertex-limit box and the main theorem

**Λ values.** For an ordered pair (a, b), let w (with w_a > 0, on facet k) and w′ (with w′_a < 0, on facet k′) be the two b-crossings. In the plane h_b = 0, D_T is a convex cone containing the open positive quadrant, so its two boundary rays have opposite a-signs. Define

 Λ_{ab} := [c_k(w)_a / (λ_{bk} w_a)] · [λ_{bk′} |w′_a| / |c_{k′}(w′)_a|].

The strict signs c_k(w)_a > 0 > c_{k′}(w′)_a follow as in (c), using UVN(a) and UVN(b).

**Lemma 6.1 (vertex-limit box; PROVED under (SH), (DF), (ND), (NA_w)).** Λ_{ab} ≤ 1 for all a ≠ b.

*Proof.*
1. *Accepted witnesses near w′.* Let q₀ = s e_a + (1 − s)e_b. On F_{k′} near w′, a facet gamble A with A_b > 0 has c·q₀ = s c_a + (1 − s)λ_{bk′}A_b. It is accepted (c·q₀ > 0) once A_b > s|c_{k′}(w′)_a|(1 + η)/((1 − s)λ_{bk′}). So accepted A exist with
   |A_a|/A_b → |w′_a|(1 − s)λ_{bk′}/(s|c_{k′}(w′)_a|(1 + η)).
2. *Accepted witnesses near w.* On F_k near w, accepted B with B_b < 0 exist with |B_b|/B_a up to ≈ s c_k(w)_a/((1 − s)λ_{bk}w_a).
3. *The certificate.* As s, η → 0, the product (|A_a|/A_b)(|B_b|/B_a) tends to Λ_{ab}. If Λ_{ab} > 1, then for small s some λ > 0 makes (A + λB)_a < 0 and (A + λB)_b < 0.
4. *A and B are accepted at nearby interior priors.* By (b), good h′ near A have ĉ(h′) near ĉ(A). By (NA_w), R(h′) ∩ int Δ = {c(h′)·q > 0}. So for interior q near q₀, a.e. h′ in a ball around A lies in B_q ≈ D_{K_q}, and openness and convexity give A ∈ D_{K_q}. Likewise B.
5. *Contradiction.* So A + λB ∈ D_{K_q} for interior q → q₀, which contradicts R10b Lemma FS (supp q₀ = {a, b}). ∎

**All-facing triangles.**
- *Definition.* T has crossing distribution (2,2,2), labelled so that C_k = {i ≠ k}, and h_k < 0 on F_k for every k. Equivalently, v_k ∈ int conv{e_k, v_i, v_j}: e_k sees v_k in front of the opposite edge.
- *Contamination triangles are of this type.* For T = (1 − ε)p₀ + εΔ with p₀ interior, the edges are parallel to those of Δ, so T is in general position. The line e_k v_k passes through p₀ ∈ int T, so v_k faces e_k.

**Theorem 6.2 (PROVED).** Let T be an all-facing triangle in general position and p\* ∈ int Δ. Then (SH), (DF), (ND), (NA_w) are inconsistent. In particular this holds for T1 (every ε ∈ (0,1)) and for every ε-contamination of an interior baseline.

*Proof.*
1. *Setting up.* Work in μ-form (Lemma 4.1). Each facet has two crossings, so each Γ_k is nonsingular (Lemma 3.2). Write ρ_k(i:j) = μ_{ik}/μ_{jk}.
2. *The corner equation.* Consider the corner r = r_{ac} with third vertex b. Facing gives r_a, r_c < 0 < r_b. Put A = −r_c/r_b > 0 and B = −r_a/r_b > 0, and s = ρ_a(b:c), t = ρ_c(a:b). Corner proportionality (d), written out in the (a, b, c) components, is
   (6.1) A/s + B t = 1.
   Also r ⊥ v_a and r ⊥ v_c give
   (6.2) v_{aa}B + v_{ac}A = v_{ab} and v_{ca}B + v_{cc}A = v_{cb}.
3. *The box for this corner.* The b-crossings lie on F_a (with w′_a < 0, since h_a < 0 on F_a) and on F_c. A direct computation from §4 gives
   Λ_{ab} = st·v_{ac}/v_{aa} and Λ_{cb} = (v_{ca}/v_{cc})/(st).
   (`facing_check.py` agrees with the general Λ to 1e-14.)
   So Lemma 6.1 gives v_{ca}/v_{cc} ≤ st ≤ v_{aa}/v_{ac}.
4. *Intervals for s and t.* By (6.1), st = (s − A)/B and t = (1 − A/s)/B are both increasing in s. With (6.2), the box becomes
   (6.3) v_{cb}/v_{cc} ≤ ρ_a(b:c) ≤ v_{ab}/v_{ac},
   (6.4) v_{ca}/v_{cb} ≤ ρ_c(a:b) ≤ v_{aa}/v_{ab}.
   (The upper ends correspond to Λ_{ab} = 1 and the lower ends to Λ_{cb} = 1. If L > U the box is empty, which is an immediate contradiction.)
5. *Pinching.* Apply (6.4) to the other corner of facet a, namely r_{ab}, with the roles (a, c, b) ↦ (b, a, c). Its t-variable is ρ_a(b:c), so it gives ρ_a(b:c) ∈ [v_{ab}/v_{ac}, v_{bb}/v_{bc}]. Together with (6.3), ρ_a(b:c) = v_{ab}/v_{ac} for every facet a.
6. *Contradiction.* Then s = A + B·v_{aa}/v_{ac} attains the upper end, and (6.1) gives t = v_{aa}/v_{ab}. But step 5 applied to facet c gives t = ρ_c(a:b) = v_{ca}/v_{cb}. So v_{aa}v_{cb} = v_{ab}v_{ca}. That says det(v_a, v_c, e_c) = 0, i.e. e_c lies on line(v_a, v_c), contradicting general position. ∎

**T1 in one line.**
- Λ_{12} = βac with β = (1 − ε)/(1 + 2ε) = 1/κ, so the box is 1/κ ≤ x² ≤ κ. This is exactly FA (10.2).
- The box then gives x + 1/x ≤ √κ + 1/√κ < κ + 1 (equivalently (1 − √κ)(κ + 1) < 0), contradicting x + 1/x = κ + 1.
- Explicit certificate for x₊:
  - edge prior q₀ = (s, 1 − s, 0);
  - A = (−β(1 + η), η, 1) ∈ F_1, accepted for s < xη/(1 + 2xη);
  - B = (1, −ζ, −β(1 − ζ)) ∈ F_3, accepted for ζ < xs/(1 − s);
  - A + λB < 0 on {1, 2} is possible iff η < βζ(1 + η). As η → 0 this needs βx² > 1, i.e. x₊² > κ, which holds since x₊ > 1.
  - For x₋, use the mirror certificate near e_1, which needs x₋² < 1/κ.
- Numerical values of x₊²/κ: 1.90, 2.34, 3.80, 7.31, 29.96 at ε = 0.05, 0.1, 0.3, 0.6, 0.9 (`t1_box_cert.py`, `vertex_box.py`).

**Remark (relation to NOGO).** Theorem 6.2's algebra (6.1)–(6.3) uses only:
- facet maps with crossing rows;
- corner matching;
- the box.

FA derives these for continuous CPMs without (DF). If FA's derivation is valid for general triangles (it is stated only for contamination), the pinching argument extends NOGO from contamination triangles to all all-facing triangles. This is CONDITIONAL on FA, which was not re-read.

---

## 7. Numerics (evidence only)

| Test | Result |
|---|---|
| Box test on realised gauge mixtures (hexagon, two 9-gons near T1) | 0 violations (`sanity_gauge.py`); Λ_{ab} = 0.25 / 0.421 / 0.442 for all (a,b) (`polygon_lambda.py`) |
| T1, ε ∈ {.1, .3, .6}, p\* on a 105-point grid (ε = .3) | always exactly 2 sign-admissible solutions (x₊, x₋); both violate the box (`t1_pstar_scan.py`) |
| ~1350 random general-position triangles, Λ_max over sign-admissible solutions (`vertex_box.py`, 3 seeds) | (1,2,3): 562 solutions, min Λ_max = 1.0045, none ≤ 1. (2,2,2): 336 solutions, min Λ_max = 1.124, none ≤ 1. (0,3,3): no solutions (Thm 5.1) |
| Nelder–Mead minimisation of Λ_max over triangles, 6 completed runs over 3 seeds (`minimise_lambda.py`) | converges to 1.0001–1.0003; minimisers have min normalised \|det(v_k, v_j, e_i)\| ≤ 2e−4, i.e. they approach non-general position |
| Coarse box test (`survey.py`) | 33 apparent (1,2,3) survivors. Refining three of them (`margins.py`, `refine.py`) gave certificates 1.018, 1.103, 1.149 > 1, at priors within 0.01–0.03 of a vertex. The coarse survivors are sampling artefacts; the vertex-limit Λ is the right statistic. These survivors also passed an interior coherence test on facet gambles (`coherence_test.py`) |

---

## 8. Why hexagons and 9-gons escape

1. **Rigidity count.** For an N-gon target, the first-order system has 3N projective facet parameters. It has at most 6 crossing conditions (fewer if an edge lies on a cevian) and N corner equations. That leaves ≥ 2N − 6 free parameters: 0 for triangles, 6 for hexagons, 12 for 9-gons. The triangle is the only polygon whose corner system is rigid.
2. **Where the pinching uses the triangle.**
   - In Thm 6.2 each facet a has exactly two corners, shared with the only two other facets. The two b-crossings sit on the two facets that meet at the corner opposite v_b.
   - So the box for b and the corner equation (6.1) involve the same two facet ratios. Facet a's two corners then give opposite one-sided bounds that meet at v_{ab}/v_{ac}.
   - In a hexagon or 9-gon, the two b-crossings are on non-adjacent facets. Intermediate facets have ≤ 1 crossing, and their free rows absorb the corner equations, so no pinching occurs. This is the first-order version of R10a's remark that "some edge ray is adjacent only to non-crossing facets".
3. **Same regularity class.**
   - The gauge-mixture polygons satisfy (DF), (ND), (FD), and they satisfy the box with slack (Λ ≤ 0.45).
   - Within this class, triangles differ from them only through rigidity plus the box. The box can be met with equality only in non-general position. Then a crossing migrates to an edge and the distribution changes.
4. **Not through the corner rays alone** (Prop 5.2). Exception: (·,3,3) triangles (Thm 5.1).

---

## 9. What escapes, and the exact remaining steps

A T1 realisation, or one for any all-facing triangle, must violate (DF), (ND) or (NA_w). Each escape is described precisely below.

- **(E1) Kinked facets.** One-sided derivatives with g_{−δ} ≠ −g_δ.
  - Concavity then gives only monotone facet line fields (§3 remark).
  - The chart structure forces the zero set of P(·, h) near p\* to be a line through p\*, so the kink is a jump in the transverse slope across that line.
- **(E2) Sliding edges.** Clusters at a corner ray are not unique, and P(q, r) = 0 on two open wedges at p\*. K_q keeps an edge on the fixed edge line of T and slides it past a vertex.
  - This is excluded by (DF) + (ND) on the adjacent facets (Thm 1(d)).
  - Otherwise it is open. An "edge-pinning" analogue of R10b Thm PL / Lemma M would close it. Corner rays have no crossings (r_i ≠ 0), so Lemma M's Step 3 does not transfer directly.
- **(E3) First-order flat facets.** Γ_k = 0: v_k stays to first order. Thm PL excludes exact pinning on open sets, not o(t) pinning.
- **(E4) Adjacency at the box witnesses.** This is the R4 residual, now localised.
  - The witnesses are gambles near the b-crossings w ∈ F_k, at edge priors near e_b. This matches R10b Remark V3: h_b ≈ 0.
  - To cut their charts, a d-face must separate q₀ from the region {c·q > 0} near p\*. By R4 Thm B, the d-face priors carry K_p ⊆ h^⊥ ≈ line(e_b, v_k): degenerate credal sets on lines through e_b and the tangent vertex.
  - This must happen for at least one witness family of every pair (a, b) with Λ_{ab} > 1.
  - It is impossible under (FD). It is also impossible near e_b itself unless K_{e_b} ⊆ line(e_b, v_k).

**Cleanest statement of the remaining problem for T1.** Assume an additive realisation exists (SH). Then, at the target prior p\*, at least one of the following holds:
- some facet support function q ↦ P_{K_q}(h) is not Gâteaux-differentiable or is first-order flat;
- or some interior Bayes credal set on a d-face of a near-crossing witness pair is degenerate, as in (E4).

**Next steps, in order of expected payoff.**
1. Prove (DF) along blow-up subsequences. Lipschitz control of q ↦ K_q would give blow-up limits G(δ, h) that are concave in h on facets. What is missing is oddness in δ, and Lemma C supplies only the sign structure. A plausible route is to apply Lemma C at p\* ± tδ simultaneously, together with Thm PL to rule out one-sided pinning.
2. Exclude (E4) by combining R4 Thm B with Hausdorff continuity: degenerate K_p on lines through e_b at priors between e_b and p\*, for both crossings of every b.
3. Extend the pinching proof of Thm 6.2 to the (1,2,3) and non-facing (2,2,2) classes (CONJECTURE R15). The numerics say the margin is positive but can be small (Λ_max ≥ 1.0045 in the sample).

---

## 10. Files (`r15py/`)

| File | Purpose |
|---|---|
| `raysys.py` | first-order ray-system solver for any triangle and p\*; sign test; edge box test |
| `vertex_box.py` | closed-form vertex-limit Λ_{ab}; random survey |
| `facing_check.py` | closed-form Λ in the all-facing class vs code |
| `t1_box_cert.py`, `t1_pstar_scan.py` | T1 certificates; p\* scan |
| `pstar_invariance.py` | Lemma 4.1 check |
| `polygon_lambda.py`, `sanity_gauge.py` | gauge-mixture polygons (consistency of the box test) |
| `survey.py`, `coherence_test.py`, `margins.py`, `refine.py` | coarse survey; interior coherence test; refinement of apparent survivors |
| `minimise_lambda.py`, `inspect_opt.py` | search for counterexamples to CONJECTURE R15 |
