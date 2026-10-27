# C62 — Constructor notes: signed piecewise-linear fields for the reversed triangle (25 Oct 2026)

Labels: **PROVED** (full proof here, not refereed) / **CHECKED** (exact computation, rational arithmetic or exact symbolic) / **CONJECTURE** / **NUMERICS**. Scripts in `c62py/` with `.out` files. Plain English first, then proofs.

---

## 0. Verdict

1. **Positive control passes (CHECKED).** Three normalised boxes, with the box field c_j(h) = min(l_j h_j, u_j h_j) on U = D_{K'}, pass the exact all-priors checker: conditions 1–4 hold for every prior π ≥ 0 (`box_control.out`). The checker also rejects the obvious bad fields (`negative_controls.out`). So the test does not import an extra requirement.
2. **The lead's reformulation of condition 3 is correct, with one strictness clause (PROVED, Lemma 2.1).** For continuous c, "every B_π is a coherent cone" is equivalent to the pairwise condition c(h+k) ∈ cone(e_1, e_2, e_3, c(h), c(k)) for all h, k ∈ U, plus: no prior that accepts both h and k is exactly indifferent to h+k. I did not use it for the search. I used an equivalent local form for piecewise-linear fields, a "kink test" on cell walls (Lemma 2.2), which reduces the all-priors check to finitely many exact linear programmes and a finite connectivity check.
3. **No explicit field was found, and none exists in the main ansatz (PROVED, Theorem 4.1).** Take any one-sided U ⊇ cl D_K∖0, so any choice of K'. No positively homogeneous c that is continuous and piecewise linear on a finite conic partition near ∂D_K∖0 satisfies conditions 1–4 for the reversed triangle. Adding cones does not help. The proof uses condition 3 only at priors near the target prior π* and on the three segments [e_k, π*].
4. **The seam that fails is the three corner rays r_j = 2·𝟙 − 5e_j.**
   - Local convexity near π* forces c to be linear on each facet of D_K (Lemma 4.3).
   - The sign seams where each facet crosses two coordinate planes force crossing rows c_i = λ_{ik} h_i (Lemma 4.4).
   - Continuity at the three corners then gives a 6×6 homogeneous linear system of full rank (CHECKED). So all λ = 0, and c vanishes on ∂D_K. Lemma 4.2 shows that is impossible.
   - Even if only directions must match at the corners (c may be rescaled by different factors on different cells), the corner system x + y = 3/2, 1/y + z = 3/2, 1/z + 1/x = 3/2 has no real solution (CHECKED). Its only solutions are 3/4 ± i√7/4.
5. **The most promising relaxations were examined.**
   - *Different K':* irrelevant. Every step is local at ∂D_K.
   - *More cones:* irrelevant. Lemma 4.3 excludes every wall through a facet point.
   - *Discontinuity across walls:* reduces to a "pinned" facet (a facet held fixed for an open set of priors), which R10b Cor PL2 excludes in this one-sided setting. This is a detailed sketch (CONJECTURE, §6.1).
   - *Two-level designs:* complete orders with a veto first and a piecewise-linear signed second level fail by the same corner seam when the target pays no veto (PROVED given E61 Thm 5.1 and Lemma 3.4; §6.3). Complete orders where the target pays a veto are already excluded by S3.
   - *What survives:* (i) incomplete (unanimity) orders whose effective charts are only weakly sign-correct, through vetoes the target pays (E61 §4.1(c)); (ii) genuinely irregular fields, with non-Lipschitz or measurable behaviour at the facets or corner rays (§6.2); (iii) orders that are not additive. These are limits of the signed-field ansatz only, not an impossibility theorem for coverage.
6. **Coordination with R15 (lead's message, §7).**
   - Our certificate gives R15's (SH) and (NA_w) automatically; (ND) is automatic for piecewise-linear fields.
   - (DF) can fail for piecewise-linear fields, namely when π*·c has a kink across a facet. Theorem 4.1 does not need it.
   - No hypothesis of R15 Lemma 6.1 or R10b Lemma FS involves (S) or closed choice.
   - **Λ is undefined for the reversed triangle**: its corner-ray system has no real solution, so it is excluded before any box inequality is needed. Under R15's own hypotheses (DF), (ND) this is a pure corner-ray no-go, like R15 Thm 5.1. The reversed triangle behaves like the (·,3,3) class, not like the random (2,2,2) triangles in R15's survey.

**Explicit candidate field: none.** The continuous piecewise-linear ansatz is provably empty for this target.

---

## 1. Setting and named hypotheses

- Three worlds. K = {m ∈ Δ : m_i ≤ 2/5}, with vertices v_1 = (1,2,2)/5 and permutations. Then D_K = {h : v_k·h > 0, k = 1,2,3} = {P > 0}.
  - The rays of D_K are r_j = 2·𝟙 − 5e_j, with v_k·r_j = δ_{kj} (`seam_system.py` checks it).
  - Facet F_k = cl D_K ∩ v_k^⊥ = cone(r_i, r_j) for {i,j,k} = {1,2,3}.
- **(U)** U is an open convex cone containing cl D_K∖0 and containing no h ≤ 0. Example: U = D_{K'} with K' compact convex in relint K. For the cross-section below we also take u ∈ K'.
- **Field.** c : U → ℝ³ is positively homogeneous and integrable. World i maximises ∫_X c_i. For a prior π ≥ 0, π ≠ 0, put f_π := π·c and B_π := U ∩ {f_π > 0}.
- **Certificate (auditor §4):**
  - (C1) sign(c_i) = sign(h_i) a.e. on U;
  - (C2) {f_π = 0} is null for every π;
  - (C3) every B_π is a.e. equal to a globally coherent cone D_{Q_π};
  - (C4) B_{π*} = D_K a.e. for some π* > 0.
- **(PL)** There is a finite polyhedral fan (finitely many polyhedral cones) covering a neighbourhood of cl D_K∖0, and on each cone σ, c(h) = M_σ h. "Continuous PL" means the pieces agree on shared faces.
- **Normalisation.** Replacing c_i by π*_i c_i preserves (C1)–(C4) and (PL), and turns π* into u. So π* = u from now on.
- **Cross-section.** Since u ∈ K', every h ∈ U has Σh > 0. In the plane {Σh = 1}, U becomes an open convex polygon U₂, the fan becomes a polygonal subdivision, and c is affine on each cell. D_K becomes the triangle T = {h_k < 2 for k = 1,2,3}, whose edge F_k is the line h_k = 2.

---

## 2. Condition 3: the pairwise and local forms

**Lemma 2.1 (lead's reformulation; PROVED).** Let c be continuous on U with the strict sign pattern of h (the continuous version of (C1)). For h, k ∈ U put a = c(h), b = c(k), d = c(h+k), and A := {π ≥ 0 : π·a > 0, π·b > 0}.

(a) The implication "π ∈ A ⇒ π·d > 0" holds iff A = ∅, or d ∈ C_{ab} := cone(e_1, e_2, e_3, a, b) and A ∩ d^⊥ = ∅.

(b) In particular it holds if d = s + αa + βb with s ≥ 0, α, β ≥ 0 and α + β > 0. When the only representations have α = β = 0, so that d = s ≥ 0, it holds iff π·s > 0 on A.

(c) (C3) holds for every π iff the implication in (a) holds for every pair h, k ∈ U. Then B_π = D_{Q_π}, where Q_π is the normalised dual cone of B_π.

*Proof.*
- (a) Suppose A ≠ ∅. Then cl A = Ā := {π ≥ 0 : π·a ≥ 0, π·b ≥ 0}: every point of the convex set Ā is a limit along a segment to a point of A.
  - The implication gives π·d ≥ 0 on Ā. By Farkas, d lies in the dual of Ā, which is the finitely generated, hence closed, cone C_{ab}.
  - The strict part is the implication itself on A.
  - Conversely, if d ∈ C_{ab} then π·d ≥ 0 on A, and strictness is the stated extra clause.
- (b) If α + β > 0, then π·d ≥ α π·a + β π·b > 0 on A.
- (c) "⇐": B_π is open (c is continuous), closed under positive scaling (homogeneity), and closed under addition (the pairwise condition). So it is an open convex cone.
  - It contains int ℝ³₊, since there c > 0 by the strict signs. It contains no h ≤ 0, since B_π ⊆ U.
  - An open convex cone C ≠ ℝ³ equals {h : q·h > 0 for all q ∈ C\*∖0}. C ⊇ int ℝ³₊ gives C\* ⊆ ℝ³₊.
  - So C = D_{Q_π} with Q_π := C\* ∩ Δ.
  - "⇒": a coherent cone is closed under addition. ∎

*Remarks.*
- The strictness clause matters only on a boundary configuration (d ≥ 0 with zeros). For continuous fields with strict signs it never binds at interior pairs, because there d has the strict pattern of h+k.
- The lead's "plus openness/continuity details" are exactly (c). For merely measurable c the a.e. version needs a separate density argument, which I do not need.
- Concave c (c(h+k) ≥ c(h) + c(k)) is the case α = β = 1. That is the box field.
- The dual view is the same statement: {π : h ∈ D_{Q_π}} = {π : π·c(h) > 0}.

**Lemma 2.2 (local kink criterion for continuous PL fields; PROVED).**
- *Kink vector.* Let e = [a, b] be an interior edge of the cross-section subdivision, between cells σ and τ. Let n_e be the plane through 0 and e, oriented positive on σ. Continuity gives M_σ − M_τ = d_e n_eᵀ for a unique d_e ∈ ℝ³.
  - Locally f_π = min(f_σ, f_τ) (a concave kink) iff π·d_e ≤ 0.
- *Statement.* Suppose (C1) and (C2) hold, and for every interior edge e:
  - (K) π·d_e ≤ 0 for all π in the closure of {π ∈ relint Δ : (π·c(a))(π·c(b)) < 0}.

  Suppose also that for every generic π (π·c(v) ≠ 0 at every vertex v) the closed set S_π := cl U₂ ∩ {f_π ≥ 0} is connected. Then (C3) holds for every π.
- *Necessity.* Conversely, (K) is necessary.

*Proof.*
- **Generic π.** S_π is closed and connected. It is locally convex at every point:
  - inside a cell it is a half-plane intersected with cl U₂;
  - at a crossing of an edge it is {min(f_σ, f_τ) ≥ 0}, by (K);
  - vertices carry f_π ≠ 0;
  - points of ∂U₂ inside boundary edges are cl U₂ intersected with a half-plane.

  By the Tietze–Nakajima theorem (a closed, connected, locally convex subset of ℝⁿ is convex), S_π is convex. B_π differs from int S_π ∩ U₂ only inside {f_π = 0}, which is null by (C2). So B_π is a.e. convex. Lemma 2.1(c) and the argument of Lemma 2.3 make it a.e. coherent.
- **Necessity of (K).** If π·d_e > 0 at a point where the zero set crosses e, then f_π = max(f_σ, f_τ) there. The set {f_π > 0} is locally a union of two half-planes with distinct boundary lines. Its convex hull contains an open wedge where f_π < 0, so no convex set agrees with B_π a.e. ∎

**Lemma 2.3 (generic priors suffice; PROVED).** Suppose B_π is convex for a dense set of priors, and (C2) holds for all π. Then B_π is a.e. equal to the open convex cone conv(B_π) for every π.

*Proof.*
- Take h, k ∈ B_π. For generic π′ near π, h, k ∈ B_{π′}, so π′·c(h+k) > 0. Letting π′ → π gives f_π(h+k) ≥ 0.
- So B_π + B_π ⊆ B_π ∪ Z_π, where Z_π = {f_π = 0} is closed and null.
- Induction: every point x of the open set B_π + B_π is a limit of points of B_π, since Z_π is null and closed. So sums of three or more terms also land in B_π ∪ Z_π, by the same limit.
- Hence conv(B_π) ⊆ B_π ∪ Z_π. ∎

**The exact checker** (`checker.py`) implements Lemmas 2.2–2.3 in rational arithmetic.
- (C1), (C4) and (C2) are vertex tests.
- (K) is one 2-D vertex-enumeration LP per kinked edge and orientation.
- Connectivity is tested at one representative prior for every 2-cell of the line arrangement {π : π·c(v) = 0} in the prior simplex. Inside a cell, the sign vector at all vertices, and hence the combinatorics, is constant. Representatives are offset midpoints of arrangement segments, with an exact safe offset.

This is a finite exact argument for all π ≥ 0, not a grid.

---

## 3. Positive control (CHECKED, `box_control.out`)

- **Set-up.** Normalised box K = ν(∏_j [l_j, u_j]) with u ∈ K. Take K′ = u + ½(K − u) and c_j(h) = min(l_j h_j, u_j h_j).
- **Partition.** The coordinate planes and the 8 corner planes.
- **Theory.** Kinks occur only across h_j = 0, with d = (l_j − u_j)e_j ≤ 0, so (K) holds for every prior. Also π·c(h) = min over π⊙Q of q·h, so B_π = U ∩ D_{ν(π⊙Q)}.

| Box | Cells | Kinked edges | (C1) | (C2) | (C4) | (K) | Connectivity (priors tested) | Result |
|---|---|---|---|---|---|---|---|---|
| l = (1,1,1), u = (2,2,2) (constant odds ratio, k = 2) | 28 | 15 | OK | OK | OK | OK | OK (1236) | CERTIFIED |
| l = (1,1,1), u = (2,3,5) | 34 | 16 | OK | OK | OK | OK | OK (1711) | CERTIFIED |
| l = (2,1,3), u = (5,4,4) | 35 | 17 | OK | OK | OK | OK | OK (1643) | CERTIFIED |

**Negative controls (CHECKED, `negative_controls.out`).**
- N1: the convex box field max(l_j h_j, u_j h_j) fails (K) on 12 edges, at the vertex priors e_j.
- N2: a reversed-triangle field satisfies the linear conditions (C1), (C2), (C4) exactly. It was found by LP and rounded to rationals, on a partition by coordinate planes, facet planes and medians (54 triangles). It fails (K) on 65 of 72 edges.
  - One witness is on the facet edge r_3–(2,0,−1) at π = u itself: π·d = 1043/11250 > 0. This is the "α ≤ β" facet condition of §4 failing.

So the checker accepts the known construction and rejects bad ones.

---

## 4. Main result: the continuous PL ansatz cannot cover the reversed triangle

**Theorem 4.1 (PROVED).** Assume (U) and (PL) with c continuous near cl D_K∖0, and (C1) and (C4) with π* = u. Assume also that (C2) and (C3) hold for all π in a neighbourhood N of u and on the three segments (e_k, u]. This is a contradiction. So no continuous PL field, on any finite conic partition and with any K′, carries the certificate for the reversed triangle.

The proof has four steps. First, from (C4) and continuity: f_u ≥ 0 on cl D_K, f_u ≤ 0 off D_K, and f_u = 0 on ∂D_K. On a cell σ adjacent to relint F_k from inside, f_u(h) = α_σ v_k·h with α_σ > 0, because f_u is linear and positive on σ ∩ D_K. From outside, f_u(h) = β_σ v_k·h with β_σ > 0.

**Lemma 4.2 (c does not vanish on ∂D_K∖0; PROVED).** Let w ∈ ∂D_K∖0, and let k be a coordinate with w_k > 0. Every boundary point has one: h_k > 0 on F_k.

*Proof.*
- Suppose c(w) = 0. For small x, c(w + x) = G(x) := M_σ x on each cell σ at w. So near w, B_π is w + P_π with P_π := {π·G > 0}, a cone.
- If B_π is a.e. convex then P_π is a.e. a convex cone: either full (up to a null set) or of angle ≤ π.
- Along π(s) = (1 − s)e_k + su, let Z(s) be the set of unit directions with π(s)·G ≤ 0.
  - At s = 0, Z is null, since G_k = c_k(w + ·) > 0 a.e.
  - At s = 1, Z is a closed arc of length ≥ π, because w ∈ ∂D_K.
- Let s₀ := inf{s : Z(s) non-null}.
  - G is continuous, and each non-null Z(s) contains an arc of length ≥ π. By uniform convergence, π(s₀)·G ≤ 0 on an arc of length ≥ π.
  - If Z(s₀) were null, that is a contradiction.
  - Otherwise s₀ > 0, and π(s)·G > 0 a.e. for s < s₀. Linearity in s then forces π(s₀)·G = 0 on that arc. That is a non-null tie at π(s₀), contradicting (C2). ∎

**Lemma 4.3 (facet linearity: no wall may pass through a facet point; PROVED).** For each k there is a linear map M_k on v_k^⊥ with c = M_k on cl F_k∖0.

*Proof.*
- **Set-up.** Fix w ∈ relint F_k. In the cross-section, the cells at w are sectors bounded by rays from w: the two facet rays, plus inner half-walls inside T and outer half-walls outside.
- **An inner half-wall has kink d with d·u = 0.** Let W be an inner half-wall between sectors σ and τ, with kink d. Continuity of f_u = α v_k·h across W, where v_k·h > 0, gives α_σ = α_τ. Hence d·u = 0.
- **Its kink is κ c(w).** Take q = u + tδ with δ·c(w) < 0 and t > 0 small.
  - Then f_q(w) < 0, while f_q > 0 along W at distance ≫ t. So the zero set of f_q crosses W at distance O(t) from w.
  - The kink coefficient there is q·d = tδ·d. By the necessity part of Lemma 2.2 and (C3) at q ∈ N, δ·d ≤ 0.
  - This holds for every δ with δ·c(w) < 0. By Lemma 4.2, c(w) ≠ 0, so d = κ c(w) with κ ≥ 0.
- **Outer half-walls.** Symmetrically, where f_q(w) > 0 the zero set lies outside, and every outer half-wall has kink d′ = −κ′ c(w) with κ′ ≥ 0.
- **Comparing the two sides.** Let σ₁, τ₁ be the inner and outer sectors on facet side 1 at w, and σ₂, τ₂ those on side 2.
  - Continuity along the facet gives (M_{σ₁} − M_{σ₂})|_{v_k^⊥} = (M_{τ₁} − M_{τ₂})|_{v_k^⊥}.
  - The left side is Σ κ_j c(w)(n_j·h), summed over the inner half-walls. The right side is −Σ κ′_j c(w)(n′_j·h), over the outer ones.
  - Each orienting functional n_j and n′_j vanishes on w and is positive on facet side 1.
  - Evaluating on side 1 gives (Σ κ_j a_j + Σ κ′_j b_j) c(w) = 0 with a_j, b_j > 0. So every κ = κ′ = 0.
- **Conclusion.** No wall through w carries a kink, apart from the facet plane itself. So c|_{v_k^⊥} is linear near every relint point. relint F_k is connected, so it is linear on all of F_k. ∎

**Lemma 4.4 (crossing rows; PROVED).** On F_k, for i ≠ k, c_i = λ_{ik} h_i with λ_{ik} ≥ 0, and c_k = −Σ_{i≠k} λ_{ik} h_i.

*Proof.*
- On F_k = cone(r_i, r_j), both h_i and h_j change sign. Concretely, on F_3 = {(−3s+2t, 2s−3t, 2s+2t)}, h_2 = 0 at t/s = 2/3 and h_1 = 0 at t/s = 3/2. So each facet has two crossing rays w_{ik} with h_i = 0.
- By continuity and (C1), c_i(w_{ik}) = 0. A linear functional on the plane v_k^⊥ that vanishes on ℝw_{ik} is a multiple of h_i.
- The sign of the multiple comes from (C1).
- f_u = 0 on F_k gives the last row. ∎

**Proof of Theorem 4.1.**
- c is continuous at the corner rays, so M_a r_j = M_b r_j for the two facets F_a, F_b through r_j.
- With Lemma 4.4 this is 9 linear equations in the six λ_{ik}. The system has rank 6 (CHECKED, `seam_system.out` (a)). Done by hand:
  - corner r_3 gives λ_{31} = λ_{32} and 3λ_{31} = 2(λ_{12} + λ_{21});
  - cyclically, λ_{ik} = μ_i (one value per coordinate);
  - so 3μ_3 = 2(μ_1 + μ_2), 3μ_1 = 2(μ_2 + μ_3), 3μ_2 = 2(μ_3 + μ_1);
  - summing gives 3Σμ = 4Σμ, so μ = 0.
- Hence c = 0 on ∂D_K, contradicting Lemma 4.2. ∎

**Corollary 4.5 (only directions match; CHECKED).** Allow different positive constants on different cells. B_π depends only on the direction of c(h), and then only proportionality holds at the corners: c_{F_a}(r_j) = κ_j c_{F_b}(r_j).
- Put x = λ_{21}/λ_{31}, y = λ_{12}/λ_{32}, z = λ_{23}/λ_{13}. The corners give x + y = 3/2, 1/y + z = 3/2, 1/z + 1/x = 3/2.
- The only solutions are complex: x = 3/4 ∓ i√7/4 and y = z = 3/4 ± i√7/4 (`seam_system.out` (b)).
- Equivalently, y ↦ 3/2 − 1/y is an elliptic Möbius map (trace 3/2 < 2, rotation angle arccos(3/4) ≈ 41.4°) whose cube is not the identity.
- The sign windows (c_k ≥ 0 on F_k, i.e. each ratio in [2/3, 3/2]) are not even needed.

**The exact seam constraint.** Each corner ray r_j is where the two facet maps meet. Each facet map is pinned to the form "λ h_i on the two crossing coordinates, minus their sum on the third". The three corner seams are then inconsistent. The constraint is first-order at the target prior: it uses only priors near u, plus the segments [e_k, u] in Lemma 4.2. It is independent of the partition, of K′, and of the field away from ∂D_K.

**What this shows, and what it does not.**
- It excludes the continuous PL signed-field ansatz for the reversed triangle with the auditor's certificate.
- It does not exclude non-additive orders, incomplete orders, or irregular measurable fields (§6.2).
- It does not exclude certificates that allow non-unique Bayes acts at boundary priors; Theorem 4.1 uses only interior priors.
- It also explains the contrast with R10b Prop L. That result realises K_q ≡ K near p\* only with charts that are discontinuous across every facet (a plateau). Continuity rules plateaus out locally; Theorem PL rules them out globally.

---

## 5. Why the box passes and the reversed triangle fails (consistency check)

- Normalised boxes have no facet crossings: their facets lie on cevians (R10b §7). So Lemma 4.4 imposes nothing, and nothing pins the corner seams.
- The reversed triangle has two crossings on every facet (non-facing (2,2,2)). The six crossing rows over-determine the three corner seams.
- This is the same mechanism as R15's rigidity count (3 unknowns, 3 corner equations for any triangle). Here the equations have no real solution at all.

---

## 6. Relaxations

### 6.1 Discontinuous PL fields (CONJECTURE; detailed sketch)

*Claim.* Theorem 4.1 persists for PL fields that may jump across walls.

*Sketch.* A jump across a wall W through a facet point or corner ray, between cells σ and τ, makes the boundary of B_q run along W between the zeros y_s and y_t of the two side functions. Local convexity then needs the configuration "where one side changes sign, the other side is negative".
- **Inner walls.** For q = u + tδ near u, both side functions increase inward. So y_s = y_t is needed for every δ. That means c_σ/α_σ = c_τ/α_τ on W at the facet point or corner: normalised direction continuity. The same holds for outer walls with β.
- **The facet plane itself as a jump wall.**
  - Either the directions match (unpinned), or u·c_in > 0 > u·c_out on a facet segment (pinned).
  - A pinned segment cannot end at a relint point. Where it ends, the boundary of B_q steps between the facet and an O(t)-displaced line with a concave corner, for either sign of δ.
  - So the whole facet is pinned for an open set of priors near u, including its crossings. That is single-vertex pinning on an open set, which R10b Cor PL2 excludes. Its hypothesis "advice ranges {+,0} near ∂T" holds on a one-sided U.
- **Cells whose map vanishes at the point.** These are excluded as in Lemma 4.2, or by the same zero-crossing comparison.
- **Unpinned case.** The normalised facet field is continuous and linear (the argument of Lemma 4.3), and corner proportionality holds by the inner-wedge comparison. Corollary 4.5 then gives the contradiction.

The case analysis is written only in outline; it should be refereed before use.

### 6.2 Smooth and irregular fields (CONJECTURE, with a partial argument)

- **Smooth case.** Let the field be C² along the facets, with one-sided transversal slopes 0 < α, β < ∞ of f_u.
  - The first-order displacement of ∂B_q at a facet point is −tψ(δ·c), where ψ(y) = y/α for y < 0 and y/β for y > 0.
  - Convexity for ±δ forces α ≤ β, and c″ = κc with κ ≥ 0 for the normalisation α ≡ 1. The second representative c/β must satisfy the opposite condition.
  - Both have |·|²θ′ constant, so β is constant and κ = 0. The facet direction map is projective-linear, and Corollary 4.5 applies.
- **Steep fields.** If α or β is infinite (non-Lipschitz direction fields), a second-order computation shows that the junction between an O(t) side and an O(t²) side is non-convex either way.
- **What remains.** Measurable or non-uniform fields at the facets or corner rays escape these arguments.

### 6.3 Two-level complete designs (PROVED given E61 Thm 5.1, Lemma 3.4 and S3)

*Claim.* Let world j rank lexicographically: first a veto ∫φ_j (φ_j ≥ 0, vanishing on {h_j > 0}), then a signed level ∫c_j with c_j strictly sign-correct and continuous PL near ∂D_K. Suppose the target pays no veto. Then the ranking does not cover K.

*Proof.*
- E61 Thm 5.1 makes D_K the β-Bayes act of Σβ_j c_j on N = U ∖ ∪{φ_j > 0}, with β > 0. A zero β_j would reject gambles such as 5e_j − Σ_{i≠j} e_i, which lie in D_K.
- It also makes every null-tie t-Bayes act on N coherent.
- By E61 Lemma 3.4, N contains D_K and an open collar beyond every facet relint.
- Lemmas 4.2–4.4 use only these neighbourhoods, together with the inner wedge at each corner, which lies in D_K ⊆ N.
- So Theorem 4.1 applies to the field (β_j c_j). ∎

This extends O61 Thm A (Brier second level) to any PL signed second level. Complete orders in which the target pays a veto are excluded by S3 (cited). The remaining two-level gap is E61 §4.1(c): incomplete (unanimity) orders with target-paid vetoes. There the effective chart is only weakly sign-correct, and Lemma 4.2's strict-sign step fails.

### 6.4 What a cover would need

By the above, an additive or finite-view cover of the reversed triangle must have, at the target prior, at least one of:
- (i) a corner seam where the normalised facet maps do not match. This needs irregular fields (§6.2).
- (ii) a pinned facet. Excluded by R10b Cor PL2 here.
- (iii) effective charts that are only weakly sign-correct near ∂D_K. That means target-paid vetoes under incomplete orders.

**My recommendation is (iii).** It is the only branch not excluded by a proved statement, and it keeps the auditor's architecture (finite statistics, compact range, separation). Concretely, look for unanimity worlds whose leading level is a veto the target pays near the corner rays, so that the corner seams are switched off, with a strictly sign-correct second level. Thm 5.1's converse would then require the effective chart to vanish on neighbourhoods of the corners. Lemma 4.2's argument does not apply there, because the strict sign of c_k fails.

---

## 7. Answers to the lead's R15 questions

**(1) Hypotheses.**
- *R15 Lemma 6.1* needs (SH), (DF), (ND) and (NA_w).
  - (SH): additive strictly guiding system on a decomposable domain; a.e.-unique coherent Bayes models at every interior prior; general-position triangle target equal to B_{p\*} with p\* interior; (LF).
  - (S) and (C) appear in (SH) only as consequences (via CCIBU), not as assumptions. No closed-choice condition is used.
- *R10b Lemma FS* needs (LF), a decomposable domain, and Prop V/V1 (vertex coherence). It uses neither (S) nor closed choice.
- *Our certificate supplies all of (SH).*
  - Interior Bayes acts are unique by (C2) and coherent by (C3).
  - The reversed triangle is in general position: no line m_i = 2/5 contains a vertex of Δ.
  - (LF) holds because U is open and contains cl D_K∖0.
- *(NA_w) is automatic.* On a one-sided U the advice ranges are {+,0}, so every chart is the full half-plane {c(g)·q > 0}.
- *(ND) is automatic for PL fields.* P(u + tδ, h) = tδ·c(h)/α or /β, which is not identically 0.
- *(DF) can fail for PL fields.* It holds at h ∈ relint F_k iff α = β, i.e. f_u has no kink across F_k. Theorem 4.1 bypasses (DF): Lemmas 4.2–4.4 derive facet linearity, crossing rows and corner continuity directly.

**(2) Λ for the reversed triangle.** Undefined. The corner-ray system has no real solution: x + y = 3/2 and its cyclic versions. So there is no sign-admissible ray solution on which to evaluate the box.
- Under R15's hypotheses this is a no-go from Thm 1 alone, without the box or (NA_w), analogous to R15 Thm 5.1.
- It is consistent with CONJECTURE R15 and settles the reversed triangle within R15's (DF)+(ND) class.

**(3) Scope and redirect.**
- *Excluded:* every continuous PL single-level field (PROVED); fields meeting R15's (DF)+(ND) (via R15 Thm 1 plus Corollary 4.5); and complete veto-then-PL designs (§6.3).
- *Not a cheap escape:* failure of (DF) in the PL class. It does not escape, since Theorem 4.1 holds without it.
- *Excluded here too:* failure of (NA_w) is impossible on a one-sided U, and pinning is excluded by R10b Cor PL2.
- *Cheapest surviving escape:* §6.4(iii).
- *Positive control kept:* the box passes (§3).

---

## 8. Status table

| Item | Status |
|---|---|
| Lemma 2.1: lead's quasi-superadditivity reformulation, with strictness clause (continuous fields) | PROVED |
| Lemma 2.2: local kink criterion + connectivity ⇒ (C3) for all π (Tietze–Nakajima) | PROVED |
| Lemma 2.3: generic priors suffice | PROVED |
| Exact checker (all priors, rational) | implemented; CHECKED on controls |
| Box positive control: 3 boxes certified for all priors | CHECKED |
| Negative controls N1, N2 rejected with witnesses | CHECKED |
| Lemma 4.2: c ≠ 0 on ∂D_K∖0 | PROVED |
| Lemma 4.3: no kinked wall through a facet point; facet maps linear | PROVED |
| Lemma 4.4: crossing rows | PROVED |
| **Theorem 4.1: no continuous PL field (any partition, any K′) carries the certificate for the reversed triangle** | **PROVED** |
| Corner system rank 6 (continuity version) | CHECKED (sympy) |
| Corollary 4.5: direction-only corner system has no real solution (3/4 ± i√7/4) | CHECKED (sympy) |
| §6.1 discontinuous PL fields reduce to pinning (excluded by R10b Cor PL2) | CONJECTURE (detailed sketch) |
| §6.2 C² fields with finite slopes: facet maps projective-linear, hence excluded | CONJECTURE (argument sketched) |
| §6.3 complete veto-then-PL-signed designs, target paying no veto: not covering | PROVED given E61 Thm 5.1, Lemma 3.4 |
| R15 for the reversed triangle: no sign-admissible ray solution; Λ undefined | CHECKED |
| Surviving escape: incomplete orders with target-paid vetoes (weak effective charts) | open |
| Explicit covering field for the reversed triangle | none found; none exists in the continuous PL class |

## 9. Files (`c62py/`)

| File | Content |
|---|---|
| `checker.py` | exact all-priors certificate checker (Lemmas 2.2–2.3) |
| `box_control.py` / `.out` | positive control, three boxes |
| `negative_controls.py` / `.out` | N1 convex box field, N2 LP-built reversed-triangle field |
| `seam_system.py` / `.out` | corner-seam systems (continuity and proportionality), Möbius check |
