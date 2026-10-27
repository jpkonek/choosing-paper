# REF63-comp: referee report on the new reach results for the composition L⋆K₀ (RC63, CC63)

25 October 2026. Adversarial referee. Binding framework: BRIEF63, AUDIT_r62_composition §1, AUDIT_r63_decisions.

Labels:
- **PROVED**: proved or re-derived here; not yet independently refereed.
- **CHECKED**: exact integer or rational computation.
- **CONJECTURE**.
- **NUMERICS**: not used.

Scripts are in `ref63py/`. Each runs with `python3 -I <name>.py` and writes a matching `.out` file. The code is independent of `rc63py/` and `cc63py/`.
- Every hull is computed on integer generators of cone(K): facets by brute force over (n−1)-subsets, with integer cofactor normals.
- World types S, T, A and C are read off the incident facet normals, using P61 V1 and the O61 definitions.

| Script | What it checks |
|---|---|
| `cone.py` | exact cone hull, facets, edges, world types, cevian test |
| `n4_cc63_target.py` | the entire hull of CC63 §4.6 and of RC63 §3.6, the Theorem G prediction, facet classes |
| `n3_checks.py` | the ratio lemma (5 963 vertices); the formula ⋃ᵢν(Mᵢ(L)⊙Mᵢ(K₀)) on 2 000 compositions; the pentagon; the §6 triangles; T1 |
| `be_checks.py` | Theorem BE: 600 random n = 3 cases, and two n = 4 cases (S = {1,2} and S = {1,2,3}) |
| `hyp_checks.py` | the pullback identity on the §4.6 target; an explicit VB certificate for RC63's L; the §2.4 cyclic example; the tangent-cone step of Prop ZC for n = 3 to 6 |
| `gap_check.py` | CC63's two-pair gap vertex |
| `seg_k0.py`, `seg_search.py` | boundary targets built with a one-dimensional K₀ (tests CC63 §7, item 2) |

## 0. Bottom line

**No ERROR in any mathematical result.**
- Every claimed new covered target is outside the VB class in the right sense: at least two extreme points are not *strictly* visible, and P61 Cor V6 uses strict visibility.
- Every claimed new covered target meets the hypotheses of the composition theorem:
  - L is VB-type with at most one exempt point, and I exhibit explicit certificates;
  - K₀ is orthant-planar inside the open simplex;
  - (LF) holds.

There are several small GAPs and wording faults (all repaired below) and one factual slip, the T1 entry.

**Main points.**
1. **"Not VB-type" is established correctly, but not by non-visibility in O61's sense.**
   - In every n = 4 composed target the bad vertices are *tangential*. That is 5 of 5 in CC63 §4.6 and 3 of 3 in RC63 §3.6, each tangential from 1 to 3 worlds, and none non-visible in O61's strong sense (CHECKED).
   - So exclusion from the VB class rests on P61 Cor V6 (strict visibility), as CC63 says. It does *not* rest on O61 Theorem A.
   - RC63 calls these vertices "non-visible". That must read "not strictly visible", or it collides with O61's terminology.
   - Consequence: these targets are outside the VB *class*. Nothing shown here places them outside 𝒱_B. They sit in O61's "tangential gap".
2. **"Not orthant-planar" is proved for the interior targets,** by Lemma O1 (correct) plus a facet normal with three or more nonzero coordinates.
   - For the boundary targets (Theorem BE, RC63's pentagon) both authors argue only "R2's class lies in relint Δ". That is true, but it holds by definition.
   - I supply a robust certificate:
     - n = 3: every Theorem BE target has a non-cevian edge (PROVED).
     - n = 4: both test cases have many facets with three or more nonzero coordinates (CHECKED).
   - So these targets stay outside any natural extension of R2 to the boundary.
3. **T1 in CC63 §7 item 1 is a slip (CONFIRMED).**
   - T1 is the interior ε-contamination with p = ū and ε = 3/10. Its vertex types are CCS, CSC and SCC: all three are strictly visible (CHECKED).
   - So T1 is covered by VB (L3 Thm 3.3; VB_dominance_note; P61 Thm A).
   - Delete it from the list of unreached targets.
4. **RC63's CONJECTURE (row 17, non-polygonal L) is now PROVED,** by the uniform-visibility argument in §3.3. The n = 3 statement "composition adds no interior targets" holds for every compact convex VB-type L.
5. **Sharper n = 3 count (PROVED).** If K₀ is full-dimensional, then N(L⋆K₀) = N(L) exactly, not merely ≤ min(N(L), N(K₀)). My 2 000 compositions show only diagonal entries (CHECKED).

## 1. Verdict table

| # | Item | Verdict | Label |
|---|---|---|---|
| R8 | RC63 §2.8: conjugacy. The composed ranking is VB(L′,A) on ν = c₊μ, and the undominated family is exactly {D_{K(W0,β,α)⋆K₀}} | **CORRECT** | PROVED |
| R10 | RC63 §3.2: strengthened reach. (a) symmetric form; (b) only (LF) is needed; (c) the whole undominated family; reversed triangle excluded | **CORRECT**, with two wording GAPs: (a) needs K₀ full-dimensional (stated there, but not repeated in Summary 2); "in any number of worlds" should be the general statement in §2.2 | PROVED |
| R12 | RC63 §3.3: Lemma N3 and the n = 3 decoupling formula | **CORRECT**, with a GAP (scope): Mᵢ(L) must be restricted to relint Δ, and K must be full-dimensional | PROVED; CHECKED (5 963 vertices, 0 mismatches; 2 000 compositions, 0 mismatches) |
| R12+ | Sharpening N(L⋆K₀) = N(L) for full-dimensional K₀ | NEW | PROVED; CHECKED |
| R13 | RC63 §3.4: n = 3 interior composition adds no new targets | **CORRECT**. The CONJECTURE for non-polygonal L is closed. | PROVED (all compact convex L) |
| R14 | RC63 §3.5: boundary-exempt pentagon | **CORRECT**. The pentagon is exact, there are two extreme points of support {1,2}, and L′ ⊆ relint L. | CHECKED |
| R14′ | Its "not orthant-planar" reason (R2 lies in relint Δ) | **GAP (definitional only).** Repaired: 3 of 5 edges are non-cevian, and Lemma O1's edge argument is valid for boundary K. | PROVED; CHECKED |
| R15 | RC63 §3.6: n = 4 instance | **CORRECT**: 31 vertices, 32 facets, 61 edges; 3 bad vertices; 6 facets with all coordinates nonzero; 20 facets with ≥ 3 nonzero; 23 non-cevian edges | CHECKED |
| R15′ | Its wording "3 vertices are non-visible" | **GAP (terminology).** They are TAAT, TTAT and TATT, so "not strictly visible". The V6 exclusion is unaffected. | CHECKED |
| R15″ | Composition hypotheses for R15 | Satisfied. Explicit certificate: L′ = conv{v + (v − e_j)/100}, A_j = {v}, π\* = the CCCC vertex. | CHECKED |
| C1 | CC63 Theorem N3 (n = 3, interior π\*) | **CORRECT** for full-dimensional L and K₀. GAP (scope): "L of any dimension" uses "VB-type", which is undefined for lower-dimensional L. Lemma A needs K₀ full-dimensional; RC63's formula covers lower-dimensional K₀. | PROVED |
| C1a | CC63 Lemmas A and B | **CORRECT**. In Lemma B's ATC case, the attribution of "by convexity" matches only one orientation; the conclusion holds in both. | PROVED |
| C2 | CC63 Lemma O1 (orthant-planar ⇒ cevian edges ⇒ two-term facets, any n) | **CORRECT** | PROVED |
| C3 | Lemma R (ratio patterns decouple), Lemma TP (two-pair rule) | **CORRECT** | PROVED |
| C4 | Theorem G and acyclicity feasibility | **CORRECT**. Wording GAP: in (G1), "equivalently ū ∈ L and …" needs ū ∈ L, which (G2) supplies. K must be full-dimensional for TP. | PROVED |
| C5 | Lemma NP (a box factor transfers the facets of L) | **CORRECT** | PROVED; CHECKED (all 6 facets of L appear in K) |
| C6 | Theorem F (box family, n ≥ 4): covered, ≥ 2^{n−1} − n bad vertices, not orthant-planar | **CORRECT**. Hypotheses verified. (F-d) is *automatic* for CC63's explicit family (PROVED here). | PROVED |
| C7 | Explicit n = 4 target, §4.6 | **CORRECT** in every listed detail: 32 vertices, 63 edges, 33 facets; the 5 bad vertices as listed; facet split 12 / 15 / 6 by number of nonzero coordinates; 24 non-cevian edges; Theorem G prediction exact; pullback identity holds | CHECKED (6 000 gambles, a third on coordinate planes, 0 mismatches) |
| C8 | Theorem BE (any n ≥ 3): covered, not VB-type, not orthant-planar | **CORRECT**, with (iv) a GAP (definitional only) as in R14′. For n = 3 a non-cevian edge always exists (PROVED). Wording in (iii): "λ ∈ {0,1}" should read "extreme points need λ ∈ {0,1}". | PROVED; CHECKED (600 n = 3 cases; n = 4 with \|S\| = 2 and 3) |
| C9 | Prop ZC: contaminations whose p has exactly one zero are never composed targets | **CORRECT**. Scope: p with two or more zeros is not treated (all vertices then lie on ∂Δ). | PROVED; CHECKED (800 tangent-cone cases, n = 3 to 6) |
| C10 | Lemma NC (cevian corners) | **CORRECT** | PROVED |
| C11 | n = 3 triangle criterion (vertex-region lemma; two cevian edges never; one cevian edge iff the angle criterion) | **CORRECT** for *interior* triangles. §0 item 5 omits "interior". | PROVED; CHECKED (the three named examples reproduce their types) |
| C12 | §7 item 1: T1 listed as unreached | **ERROR (slip).** T1 is covered by VB. | CHECKED |
| C13 | §7 item 2, bullet 2 (an interior corner with fewer than two cevian rays is not reached unless the target is VB-type) | **CORRECT for n = 3**, but the cited proof (Lemma NC) covers only dim K₀ ≥ 2. GAP repaired in §3.6 for dim K₀ = 1. | PROVED; CHECKED (256 cases, 0 counterexamples) |
| C14 | §4.7 two-pair gap example | **CORRECT**: ATTT; incident normals as stated; that K has only 1 bad vertex | CHECKED |
| C15 | Silhouette decoupling | **CORRECT** | PROVED |

## 2. RC63

### 2.1 Conjugacy (R8): CORRECT

- Off the coordinate planes, c maps each open orthant linearly and bijectively onto itself.
- Null sets pull back to null sets, so ν = c₊μ is absolutely continuous. It has a finite first moment because |c(h)| ≤ max‖d_σ‖_∞ |h|.
- X ↦ c(X) is a bijection, modulo null sets, between M_U and M_{D_{L′}}. Here U = c⁻¹(D_{L′}) exactly, by Step 1.
- Under this bijection:
  - a_i(X) = ∫_{c(X)} max(0, sup_{A_i} −v·x) dν and b_i(X) = −∫_{c(X)} x_i dν;
  - correctness at world i is preserved, because sign c_i = sign h_i;
  - pointwise improvement, splicing and nullness are all preserved.
- So strict (G), (IB), transitivity, (C) and the whole undominated set transfer from P61 Thm A and B and O61 Thm C.
- The undominated models are c⁻¹(D_{K(W0,β,α)}). By the pullback identity for compact convex Q (boundary priors allowed) these are D_{K(W0,β,α)⋆K₀}. They are coherent, because Q⋆K₀ is compact, convex and inside Δ.
- (LF) is the one thing not transported, since c is not a homeomorphism. §2.7 handles it.

### 2.2 Strengthened reach (R10): CORRECT

- **(a) Symmetric form.** T_q is a homeomorphism of relint Δ (q ≫ 0) that fixes e_j and maps lines through e_j to lines through e_j. If K₀ is full-dimensional, T_q(relint K₀) is open and contained in K, hence in relint K. So visibility of m transfers to x = ν(q⊙m). The lemma needs K₀ full-dimensional; for a segment K₀, relint K₀ is not open.
- **(b) Only (LF) is needed.** The case analysis (q ∈ L′, q ∈ A_i, q = e_i, q = β̂) is complete. Points q ∈ A_i with 0 < t < 1 give x on the open segment (T_m k, e_i) with T_m k ∈ K′ ⊆ relint K. That is uniform visibility, not just pointwise.
- **(c) The whole undominated family.** β̂ ∈ Ŵ (take every v_ω = 0), so ν(β̂⊙m) ∈ K has support supp β. K ⊆ relint Δ then forces W0 = Ω and Ŵ = {β̂}.
- **"In any number of worlds."** The reversed triangle is a three-world object. The general statement proved is:

  *no K ⊆ relint Δ that is not orthant-planar, and none of whose extreme points is strictly visible, is an undominated (LF) target of any composed ranking.*

  This includes every pari-mutuel model with n ≥ 3, since its facet normals have n nonzero coordinates.

### 2.3 Ratio lemma and decoupling (R12): CORRECT, with a scope GAP

- **The proof.** F_x ⊆ x^⊥ contains no nonzero h ≥ 0, and it is a pointed arc. The six-sector walk shows that meeting all three {h_j ≥ 0} forces a whole closed one-plus sector. Its two boundary rays are the two-term normals (i→j) and (i→k). The converse is immediate.
- **"Non-visible" there means "not strictly visible"** (P61 V1). That is the sense V6 needs.
- **Scope.**
  - The formula ext K ∩ relint Δ ∩ nonvis = ⋃ᵢ ν(Mᵢ(L)⊙Mᵢ(K₀)) needs Mᵢ(L) restricted to relint Δ. Mᵢ(L) can be a boundary point when π\* ∈ ∂Δ.
  - Ratios should be read in the cross-multiplied form r mᵢ − m_j ≥ 0, so that points e_k ∈ L are handled. RC63's "generators equal to e_j impose no constraint" says this informally.
- **Sharpening (PROVED).** If K₀ ⊆ relint Δ₃ is full-dimensional and orthant-planar, then by CC63 Lemma A(iv) each Mᵢ(K₀) is a single point, for every i. The formula then gives:

  **N(L⋆K₀) = N(L)** (counting interior non-strictly-visible extreme points).

  CHECKED: the (N(L), N(L⋆K₀)) histogram over 2 000 compositions is (0,0) 180, (1,1) 476, (2,2) 968, (3,3) 376.

### 2.4 n = 3 interior: no new targets (R13): CORRECT, now for every L

**Lemma U (PROVED, any n).** Let L be VB-type with exempt point π\*, and K₀ orthant-planar inside relint Δ. Then:
- every extreme point of L⋆K₀ outside the polytope ν(π\*⊙K₀) is *uniformly* visible;
- the extreme points inside ν(π\*⊙K₀) are among its finitely many vertices.

So L⋆K₀ ⊆ relint Δ is VB-type iff at most one extreme point is not strictly visible.

*Proof.*
- K₀ is a polytope: on each mixed orthant cl D_{K₀} is a half-space, the pure orthants are trivial, so cl D_{K₀} is polyhedral and so is its dual.
- Every extreme point x of L⋆K₀ is ν(q⊙m) with q ∈ ext L ⊆ L′ ∪ ⋃A_j ∪ {π\*}.
  - q ∈ L′ is impossible, since x would lie in relint K.
  - If q ∈ A_j, then x ∈ [ν(k⊙m), e_j] with ν(k⊙m) ∈ L′⋆K₀. That set is a compact subset of relint K, hence inside some K_δ.
  - If q = π\*, then x is a vertex of ν(π\*⊙K₀). There are finitely many, so pointwise strict visibility gives a common δ. ∎

With the n = 3 count, this closes RC63's CONJECTURE for non-polygonal L. It is also the argument CC63 F3 sketches.

### 2.5 Pentagon (R14): CORRECT

CHECKED, with my own hull:
- the vertices are (1/6,1/6,2/3), (1/5,4/5,0), (1/13,8/13,4/13), (1/15,4/5,2/15) and (2/3,1/3,0);
- L's types are CCC (π\*), CCS and ASC, so L is VB-type with exempt π\*;
- the two extreme points with support {1,2} are (1/5,4/5,0) and (2/3,1/3,0);
- edges 2 and 4 of the five are cevian.

**Not VB-type.** The P61 Thm B generator count is right. Ŵ ∩ Φ_S = ν({β + Σ_{ω∈M} s_ω e_ω : 0 ≤ s_ω ≤ α_ω}), with M ⊆ S∖W0 and supp β ⊆ W0. This is a projective image of a box. Its only corner with support exactly S is M′ = S∖supp β, so there is at most one extreme point of support S.

**Not orthant-planar.** RC63 gives only the definitional reason. Lemma O1's edge argument also works for boundary K, because ∂D_K never meets an open pure orthant. The pentagon has non-cevian edges, so it is not orthant-planar in any extended sense either.

### 2.6 n = 4 instance (R15): CORRECT, with a terminology GAP

CHECKED:
- L has exactly one non-strictly-visible vertex, (7/20, 17/125, 79/1000, 87/200), of type CCCC.
- K has 31 vertices, 61 edges and 32 facets.
- K has exactly 3 bad vertices, of types TAAT, TTAT and TATT, all from the CCCC vertex of L.
- K has 6 facets with no zero coordinate, 20 with at least three nonzero coordinates, and 23 non-cevian edges.

The certificate for the composition theorem: L′ = conv{v + (v − e_j)/100} lies strictly inside L (CHECKED), A_j = {v}, and π\* is the CCCC vertex.

## 3. CC63

### 3.1 Theorem N3, Lemmas A and B (C1, C1a): CORRECT

**Lemma A.**
- The G-cones are root cones: active facet (i→j) gives w⊙(r eᵢ − e_j) = w_j(eᵢ − e_j).
- In log-ratio coordinates the normal fan tiles 𝟙^⊥.
- Arcs are shorter than π, so they are 60° or 120°, and contain at most one A-gap. Each A-gap lies in exactly one arc.
- So K₀ has exactly 3 bad vertices, one for each A-world. CHECKED: all K₀ in `n3_checks` have 3 bad vertices.

**Lemma B.**
- K ⊇ K₀ (since ū ∈ L), so a bad vertex of K is bad in K₀.
- In the ATC case (A at k₁, T at k₂, C at l):
  - the T-world k₂ forces the boundary root e_{k₁} − e_l directly;
  - the C-world l supplies y = s(e_{k₁}−e_l) + t(e_l−e_{k₂}) with t ≥ s;
  - adding (t − s)(e_{k₁}−e_l) gives e_{k₁} − e_{k₂}.
- So D contains both roots and L ⊆ M_{k₁}. The other orientation is symmetric. Correct.

**N3.** Two bad vertices with distinct A-worlds force q_a = q_{a′} on L, which contradicts full-dimensionality.

**Scope.** "L of any dimension" should be dropped, or "VB-type" defined for lower-dimensional L. The composition theorem itself assumes L is full-dimensional.

CHECKED, §2.4 cyclic example:
- L's types are ACC (ū), CAS, CSA and SCC;
- K has 7 vertices, and its only bad vertex is (1/7,4/7,2/7), of type ATC;
- K has 4 non-cevian edges.

### 3.2 Lemma O1 (C2): CORRECT

**Edges.**
- If an edge is not cevian, then {a,b}^⊥ lies in no coordinate hyperplane.
- The relint of the edge's normal cone has dimension n − 2 and is open in {a,b}^⊥. So it contains an h with no zero coordinate, in a mixed orthant.
- Near h, ∂D_K = {min(a·h′, b·h′) = 0}, which uses two distinct hyperplanes.

**Facets.** At a vertex, n − 2 independent cevian edges put n − 2 simplex vertices into the facet's affine hull. So the facet normal has at most two nonzero coordinates.

A facet normal is unique up to positive scaling, so "has three or more nonzero coordinates" is a well-defined certificate.

### 3.3 Two-pair rule, Theorem G, feasibility (C3, C4): CORRECT

- **Lemma TP.** g = r eᵢ − e_j ∈ F_x has g_k ≥ 0 for every k ≠ j. Two pairs with different heads cover every world.
- **Theorem G.**
  - Support: r qᵢ mᵢ − q_j m_j ≥ q_j(r mᵢ − m_j) ≥ 0.
  - Extremality: equality forces q = ū by (G2), so the face of K is a face of K₀ containing w.
- **Feasibility.**
  - A directed cycle in the union of pairs forces equal coordinates on all of L, so L is not full-dimensional.
  - An acyclic union has a linear extension, and its open chamber satisfies all the strict inequalities.
- CHECKED: on §4.6, the rule "pairs i→j with i < j, at least two distinct heads" predicts exactly the 5 bad vertices.

### 3.4 Lemma NP and Theorem F (C5, C6): CORRECT

- **Lemma NP.** Each term grows or shrinks so that Σ qᵢηᵢxᵢ/x\*ᵢ ≥ Σ qᵢηᵢ ≥ 0. The equality set contains T_{m\*}(facet of L), which has dimension n − 2.
- **Theorem F, conclusion 2.**
  - R(ν(x);K₀) = Lo(x) × H(x) for a box corner.
  - (F-c) gives (G1) and (G2), with ū ∈ L.
  - |H| ≥ 2 gives (G3).
  - The count of such corners is 2^{n−1} − 1 − (n − 1) = 2^{n−1} − n.

**Hypotheses for the explicit family, verified.**
- vⱼ ∈ int M_a exactly when ε < min_{b≠a} (p₀_a − p₀_b)/(1 + p₀_a − p₀_b).
- Σ := conv{vⱼ} = (1−ε)p₀ + εΔ contains p₀ in its relative interior. So L′ = {p₀} ⊆ relint L, Aⱼ = {vⱼ} ⊆ [p₀, eⱼ], and π\* = ū.
- K₀ = ν([α,β]) ⊆ relint Δ is orthant-planar, with chart c_j(h) = α_j h_j⁺ − β_j h_j⁻.
- (LF) holds, because L′ ⊆ relint L.

**(F-d) is automatic for this family (PROVED).**
- Σ ⊆ int M_a, so ū ∉ Σ.
- Some facet of Σ has ū strictly on its inner side. That facet stays a facet of L.
- Its normal eₖ − (1−ε)p₀ₖ𝟙 has all n coordinates nonzero.

So the family needs no CHECKED step.

### 3.5 The explicit target, §4.6 (C7): CORRECT

CHECKED in `n4_cc63_target.out`:
- 32 vertices, 63 edges and 33 facets (Euler characteristic 2).
- Bad vertices: the box corners (1,1,2,2), (1,2,1,2), (1,2,2,1), (1,2,2,2) and (2,1,2,2), with types AATT, ATAT, ATTA, ATTT and TATT. All are tangential; none is non-visible in O61's strong sense.
- Facets: 12 two-term, 15 three-term and 6 four-term, with the four-term normals exactly as listed.
- 24 non-cevian edges.
- Pullback identity {c(h) ∈ D_L} = D_K: 0 mismatches over 6 000 integer gambles (a third on coordinate planes), with 34 exact ties that agree.
- K′ = ν(p₀⊙K₀) lies strictly inside every facet of K.

**Verdicts.**
- Not VB-type: five non-strictly-visible vertices, by V6.
- Not orthant-planar: by O1.
- Covered: by the composition theorem, with every hypothesis verified.

### 3.6 Theorem BE, Prop ZC, Lemma NC, §7 (C8–C13)

**Theorem BE (CORRECT).**
- (ii): L ∩ Φ_S = {π\*}, so K ∩ Φ_S = ν(π\*⊙K₀). This has dimension |S| − 1 ≥ 1 because K₀ is full-dimensional and the coordinate projection is open.
- (iii): by the generator count in §2.5.
- CHECKED:
  - n = 3: 600 out of 600 random cases have exactly two extreme points of support S, equal to the endpoints of ν(π\*⊙K₀).
  - n = 4, S = {1,2}: 2 such points; 16 facets with at least three nonzero coordinates; 21 non-cevian edges.
  - n = 4, S = {1,2,3}: 6 such points, equal to ext ν(π\*⊙K₀); 19 facets with at least three nonzero coordinates; 22 non-cevian edges.

**Repair of (iv) for n = 3 (PROVED).** Every Theorem BE target in three worlds has a non-cevian edge, so it is not orthant-planar even in an extended, boundary sense.
- Suppose every edge is cevian. The edges at the two boundary vertices x± ∈ Φ_{12} other than the boundary edge must lie on line(x±, e₃).
- Then K ⊆ {r⁻m₂ ≤ m₁ ≤ r⁺m₂}, with r± = (π\*₁/π\*₂)·(extreme values of m₁/m₂ on K₀).
- L is full-dimensional, so some q ∈ L has q₁/q₂ ≠ π\*₁/π\*₂. Then ν(q⊙m±) violates one of the two bounds.
- CHECKED: 600 of 600 random cases have a non-cevian edge.
- For n ≥ 4 the general statement is open. Both test cases are certified (CHECKED).

**Prop ZC (CORRECT).**
- dim K₀ = 0: the composition is a projective image of a VB target, and P61 D3 excludes K.
- dim K₀ ≥ 2: Lemma NC requires two independent cevian directions at the interior vertex v_k. Only v_k − e_k is available (CHECKED exactly, n = 3 to 6).
- dim K₀ = 1: the face {m_k = 0} would be a single point, since K₀ lies on a line through e_k.
- Scope: p with two or more zeros is not covered. D3 does not cover it either.

**Lemma NC (CORRECT).** The copy ν(q⊙K₀) is a projective diagonal image of K₀, so its edges are cevian. At a vertex of a d-polytope there are at least d independent edges.

**§7, item 2, bullet 2.** For dim K₀ = 1 Lemma NC gives only one cevian ray, so the stated proof is incomplete. The claim is still true for n = 3 (PROVED):
- Take an interior vertex x = ν(q⊙m). Here q ∈ Aᵢ, so x − eᵢ ∈ int T_x.
- If the copy's line passes through e_l with l ≠ i, there are two cevian lines.
- If l = i: a non-VB target needs a boundary segment of support exactly S = {a,b}, so l ∈ S and i = a.
- For any y in that segment with y_a > 0, y − x has a negative coefficient on e_c − x in the basis {e_b − x, e_c − x}.
- The convex tangent wedge contains both x − e_a and y − x, so it contains e_b − x or e_c − x. That is a second cevian line.
- CHECKED: 256 non-VB boundary targets built with a segment K₀, and 0 interior vertices with fewer than two cevian lines.

**§7, item 1 (T1): ERROR (slip).** T1 has types CCS, CSC and SCC, so all its vertices are strictly visible and it is covered by VB. Replace the list with: "the reversed triangle, every triangle with exactly two cevian edges, every one-cevian triangle failing the angle criterion, …". The 63% figure from O61 also already excludes the visible cases.

**§0 item 5 and §6.** The phrase "a triangle is a composed target iff VB-type" should say *interior* triangle.

CHECKED, the §6 examples:

| Example | Types | Cevian edges | Bad vertices |
|---|---|---|---|
| two-cevian | SAA, CCT, CTC | 2 | 2 |
| one-cevian, covered | CSC, SCA, CCT | 1 | 1 |
| one-cevian, open | CCC, SCA, CAT | 1 | 2 |

## 4. Did each composed target meet the composition theorem's hypotheses?

| Target | L VB-type, at most one exempt point | K₀ orthant-planar in relint Δ | (LF): L′⋆K₀ ⊆ relint K |
|---|---|---|---|
| RC63 pentagon | yes (CCS, ASC visible; π\* on an edge) | cyclic triangle | yes |
| RC63 n = 4 | yes (explicit certificate, §2.6) | box | yes, by Step 7 |
| CC63 §4.6 | yes (L′ = {p₀}, Aⱼ = {vⱼ}, π\* = ū) | [1,2]⁴ box | yes (CHECKED strictly inside) |
| Theorem F family | yes (§3.4) | any box with α ≪ β | yes |
| Theorem BE family | yes (contamination simplex plus π\*; (BE) holds) | any full-dimensional K₀ | yes |

## 5. Recommended text changes

1. **RC63.**
   - "non-visible" → "not strictly visible" throughout §3. Add that the n = 4 bad vertices are tangential, so O61 Theorem A does not apply to them.
   - Row 17: replace CONJECTURE with PROVED (Lemma U).
   - Add N(L⋆K₀) = N(L) for full-dimensional K₀.
   - Restrict Mᵢ to relint Δ.
2. **CC63.**
   - Delete T1 from §7 item 1.
   - Say "interior triangle" in §0 item 5.
   - Theorem N3: L and K₀ full-dimensional, or cite RC63 for lower-dimensional K₀.
   - (G1): drop "equivalently", or add ū ∈ L.
   - BE (iii) wording.
   - Add the non-cevian-edge certificate to BE (iv) for n = 3.
   - Supply the dim K₀ = 1 argument in §7 item 2.
   - Note that (F-d) is automatic for the explicit family.
3. **Paper (W63 / LDG and the covering note).** State clearly that the new targets are outside the VB class, not outside 𝒱_B. Whether some single-chart 𝒱_B ranking reaches them is untouched (O61's tangential gap).
