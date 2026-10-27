# A62 — Adversary notes, round 62 (25 Oct 2026)

Labels: PROVED (proof here, not refereed) / CHECKED (verified exactly or by a short hand argument) / CONJECTURE / NUMERICS.
Scripts: `a62py/` (each with a `.out` file). Everything is exact (sympy or `Fraction`) unless marked NUMERICS.

Target: K = {m ∈ Δ_3 : m_i ≤ 2/5}, vertices v_1 = (1,2,2)/5 and permutations. D_K = {h : v_k·h > 0 ∀k}, rays r_j = 2·𝟙 − 5e_j (r_1 = (−3,2,2)), faces F_k = {v_k·h = 0} ∩ cl D_K = cone(r_i, r_j). On F_k: h_k > 0 (world k anti-visible); h_i, h_j each change sign in relint F_k (both cross). Crossing points on F_3: (−1,0,2) (h_2 = 0) and (0,−1,2) (h_1 = 0). Domain U = D_{K'}, K' ⊆ relint K compact convex; then cl D_K∖0 ⊆ U and U ⊇ ℝ³₊∖0.

Ranking class (auditor §4): world i maximises ∫_X c_i, c positively homogeneous, sign(c_i) = sign(h_i) a.e. on U. Certificate: (1) sign correctness; (2) null ties of π·c for every nonzero π ≥ 0; (3) every B_π := U ∩ {π·c > 0} globally coherent; (4) B_{π*} = D_K for some π* > 0.

**Normalisation used throughout.** Replacing c_i by π*_i c_i changes nothing (B_π is reparametrised), so π* = u = (1,1,1). Write g := c_1 + c_2 + c_3, so (4) says B_u = U ∩ {g > 0} = D_K a.e.

---

## 0. Summary

1. **(a) The lead's reformulation is correct after three repairs (Thm A, PROVED).** For c continuous off a closed null cone, and given (2): condition (3) for all π ⟺ for all h, k (and h+k) off that cone **that some prior accepts jointly**, c(h+k) ∈ ℝ³₊ + ℝ₊c(h) + ℝ₊c(k). The weak (non-strict, Farkas) form is the right one; the strict form is sufficient, not necessary. The restriction "jointly accepted" matters only for degenerate boundary pairs. Under (1), "coherent" is the same as "essentially convex", including at boundary priors.
2. **Priority item from the lead: R15 already excludes the reversed triangle, without the box (PROVED, given refereed R15 Thm 1 and Lemma 3.2).** The R15 corner system for K has **no real solution** at any interior target prior. The cyclic Möbius map is x ↦ 3/2 − 1/x: elliptic (trace 3/2, det 1), rotation angle arccos(3/4), which is not a multiple of 120°. So Λ is never reached. Scope: any additive (single-level) realisation with (SH), (DF), (ND) at p*. (NA_w) is not needed, and no step uses (S). For signed fields, (DF) means exactly "g has no kink across the faces". The constructor's `seam_system.py` reached the same elliptic map independently.
3. **(b)+(c) New exclusions inside the auditor's ansatz.**
   - **Thm A62-1 (PROVED).** No **continuous piecewise-linear** field, on any finite polyhedral fan and with any K', satisfies (1), (2) at u, (3) on a neighbourhood of u, and (4). This covers the kinked (non-(DF)) case that R15 leaves open. The box control passes every step.
   - **Thm A62-1′ (PROVED, under stated regularity).** The same holds for continuous fields whose kink ratio θ = λ^out/λ^in is **constant** along each face. This includes every C¹ field (θ = 1), hence smooth local-prior charts. The only alternative is c ≡ 0 on ∂D_K.
   - **Thms A62-2 and A62-3 (PROVED under nondegeneracy).** Fields that **jump** across a face, and fields **vanishing on the faces**, fail under the stated nondegeneracy. Two new lemmas do the work: an exclusivity lemma and a segment lemma.
   - **Exact witnesses** (π, h, k) with π·c(h) > 0, π·c(k) > 0, π·c(h+k) < 0, all strict and all three gambles in D_K (so valid for every K'), for:
     - a continuous PL local-prior chart, at a prior within 1/40 of u;
     - E61's discontinuous lower-prevision chart, at (1,2,3)/6.
   - Exact failure witnesses for:
     - pari-mutuel-affine (PMA): (1) fails on every U; exactly the priors with min π̂_i ≤ 1/6 have incoherent B_π;
     - max-repaired PMA: (4) fails;
     - box mixtures: every B_π is a box, so (4) fails.
4. **(d) What survives (precise).** A single-level signed field covering K must have one of the following:
   - (S1) a **continuous field whose kink ratio θ(y) ≥ 1 varies along some face**. Then g is not PL and not C¹ near that face;
   - (S2) degenerate first-order data on a face (outside the nondegeneracy hypotheses of A62-2/3);
   - (S3) a non-PL discontinuity at the corner rays (a "sliding edge", R15's E2);
   - (S4) no one-sided limits at the faces.

   I found no candidate that survives my own tests, and I do not claim impossibility outside the classes excluded above.

---

## 1. (a) The quasi-superadditivity reformulation

Notation: for a, b ∈ ℝ³ put P(a,b) := {π ≥ 0 : π·a > 0, π·b > 0} and P̄(a,b) := {π ≥ 0 : π·a ≥ 0, π·b ≥ 0}. Farkas for polyhedral cones: (P̄)* = ℝ³₊ + ℝ₊a + ℝ₊b =: Cone(a,b), always closed.

**Lemma 1.1 (coherence = essential convexity; PROVED).** Assume (1). For every nonzero π ≥ 0, B_π is globally coherent (a.e. equal to some D_Q, Q ⊆ Δ closed convex) iff B_π is a.e. equal to a convex set.
*Proof.*
- For h ∈ int ℝ³₊ (⊆ U), a.e. such h has c(h) > 0, so π·c(h) > 0. Hence B_π ⊇ int ℝ³₊ a.e.
- B_π ⊆ U contains no h ≤ 0.
- If B_π ≐ C with C convex, then O := int cl C is an open convex cone with O ≐ B_π, O ⊇ int ℝ³₊ and O ⊆ cl U pointed. So O = {h : q·h > 0 ∀ q ∈ O*∖0} = D_Q with Q := O* ∩ Δ ⊆ Δ (because O* ⊆ ℝ³₊), and K' ⊆ Q.
- The converse is trivial. ∎

So the brief's worry that "Bayes sets miss positive gambles near the boundary" arises only when (1) fails (e.g. PMA, §6.1). Under (1) it cannot happen, at boundary priors included.

**Theorem A (exact reformulation; PROVED).** Let E be a closed null cone (e.g. the walls of a PL fan) with c continuous on U∖E, and assume (2). Then the following are equivalent:
- (i) (3) holds for every nonzero π ≥ 0;
- (ii) (weak QSA) for all h, k ∈ U with h, k, h+k ∉ E and P(c(h), c(k)) ≠ ∅: c(h+k) ∈ Cone(c(h), c(k)).

*Proof.* (ii) ⇔ "π·c(h+k) ≥ 0 for all π ∈ P(a,b)". When P ≠ ∅, cl P = P̄; then Farkas applies.
- **(i)⇒(ii).**
  - Let π ∈ P(a,b). B_π∖E is open and ≐ C_π, an open convex cone (Lemma 1.1).
  - Balls N_h, N_k ⊆ B_π∖E are a.e. inside C_π, hence inside it (an open convex set containing a.e. point of a ball contains the ball).
  - So h+k ∈ C_π with a ball around it, and that ball lies a.e. in B_π.
  - Continuity at h+k gives π·c(h+k) ≥ 0.
- **(ii)⇒(i).**
  - Let O := {z : z + V ⊆ B_π a.e. for some ball V ∋ 0}. O is open, O ⊆ B_π a.e., and B_π∖E ⊆ O, so O ≐ B_π.
  - Let x, y ∈ O, t ∈ (0,1) and z = tx + (1−t)y. For a.e. small u: x+u, y+u ∈ B_π∖E and z+u ∉ E.
  - π accepts positive multiples of both, so (ii) and homogeneity give π·c(z+u) ≥ 0. By (2), z+u ∈ B_π for a.e. u.
  - So z ∈ O, and O is a convex cone. ∎

**Corrections to the brief's statement.**
- **Restriction to jointly accepted pairs.** The unrestricted "for all h, k" is formally stronger. If P̄ = {0}, Cone = ℝ³, so nothing is lost. If P = ∅ but P̄ ∋ π₀ ≠ 0 (a "boundary-prior pair", e.g. c(h) ∝ (1,−1,−1), c(k) ∝ (−1,1,−1), π₀ = (1,1,0)), the condition π₀·c(h+k) ≥ 0 follows from (i) by perturbing h to h′ with π₀·c(h′) > 0 and passing to the limit, whenever such h′ (or k′) exist nearby. Otherwise it is not implied by the argument (CHECKED).
- **Strictness.** The strict form (π·c(h+k) > 0) is sufficient, not necessary. It fails only on the null tie set.
- **Null sets.** For merely measurable c, pointwise QSA is not necessary, because c can be altered on null sets. Theorem A is stated for the version of c that is continuous off E.
- **Discontinuous fields.** (ii) must be imposed at continuity triples, and (2) is essential in (ii)⇒(i).
- **Boundary priors.** π = e_i gives B = U ∩ {h_i > 0}, coherent automatically. Edge priors are genuinely constrained and are included in (ii).
- **Concave c** (box) satisfies (ii) with coefficients 1 (c(h+k) ≥ c(h) + c(k)), as the brief says (CHECKED).

**Dual view (CHECKED).** For each h, A(h) := {π : h ∈ D_{Q_π}} must be an open half-plane of Δ. Equivalently, both A(h) and Δ∖A(h) are convex.
- The field is then determined up to a positive scalar per h by the edge thresholds, and the interior condition is collinearity of those thresholds.
- Only the direction of c(h) matters, so c ↦ s(h)c with s > 0 measurable preserves everything.
- A generator family Q_π = conv{X_m π} has the half-plane property iff for each h one generator binds coordinatewise. That is exactly a concave field c(h) = min_m X_m^T h, which E61 Cor 5.2 excludes for K.

---

## 2. Priority item: R15 / R10b and the reversed triangle

### 2.1 Which hypotheses R15 Thm 1 uses; is (S) used?
- (SH) as stated lists "(LA), (S), (C) by CCIBU" as **consequences**. R18 checked the proofs: Lemma C, Thm 1(a)–(d) and Lemma 3.2 use only:
  - (1.1), which is Fubini plus B_q ≈ D_{K_q} at interior q;
  - joint continuity of P (R1 Prop 3.1, from a.e.-unique Bayes acts and dominated convergence);
  - (DF) and (ND) at p*;
  - UVN(a) at vertex neighbourhoods (strict guidance at e_i, (LF), dominated convergence).
- No step uses (S). Vertex coherence (Prop V) enters only Lemma FS, UVN(b) and the box. These are **not needed** below.
- **For single-level signed fields**, (SH) holds whenever the certificate (1)–(4) holds:
  - the chart is R(h) = {c(h)·q > 0} exactly;
  - advice ranges are {+, 0} on one-sided U, so no adjacency arises and (NA_w) is automatic;
  - B_q are a.e. unique and coherent by (2)–(3).

### 2.2 The corner system for K (PROVED given R15 Thm 1(c),(d) and Lemma 3.2)
- **Crossings.** Crossing sets C_k = {i ≠ k} for every k (`raysys_exact.out`). Every facet has two crossings, so Γ_k is nonsingular (Lemma 3.2), and every crossing row λ_{ik} is nonzero.
- **Facet maps** in μ-form (Lemma 4.1): c_k(h)_i = λ_{ik}h_i for i ≠ k, and c_k(h)_k = −Σ_{i≠k} μ_{ik}h_i / p*_k.
- **Corner proportionality** c_k(r) ∝ c_j(r), normalised by one λ per facet, gives **only the complex solutions** λ = 3/4 ± (√7/4)i at p* = u. Exact solutions at p* = (1/6,1/3,1/2) and (3/10,3/10,2/5) are likewise non-real (sympy).
- **Hand form.**
  - At corner r_3 = (2,2,−3), shared by F_1 and F_2 (common crossing coordinate 3), proportionality reads 2x + 2y = 3. Here x is F_1's coefficient ratio (coordinate 2 : coordinate 3) and y is F_2's ratio (coordinate 1 : coordinate 3).
  - Cyclically, the three corners compose x ↦ 1/(3/2 − x) three times. The matrix [[0,1],[−1,3/2]] has trace 3/2 and det 1, so it is elliptic, with rotation angle arccos(3/4) ≈ 41.41°.
  - Its cube is not ± the identity (T³ = [[3/8,−5/4],[5/4,−3/2]] for the conjugate form x ↦ 3/2 − 1/x). So there is no real fixed point: the corner system is inconsistent over ℝ, not just over ℝ₊.
- **Positive control.** The same code on T1 (ε = 3/10) returns exactly R15 Prop 5.2's two positive solutions 23/14 ± 3√37/14, i.e. x₊ = 2.946 and x₋ = 0.339.

**Corollary 2.3 (PROVED, conditional only on the refereed R15 Thm 1 + Lemma 3.2).** For the reversed triangle and every interior p*, no additive strictly guiding realisation satisfies (SH), (DF) and (ND) at p*. No box, no (NA_w), no boundary priors and no (S) are used. So Λ_{ab} is never defined: there is no real ray solution to evaluate it at. The reversed triangle behaves like R15's (·,3,3) class (a pure corner no-go), although its crossing distribution is the non-facing (2,2,2).

**NUMERICS (`raysurvey*.out`).**
- Random triangles: 10 non-facing (2,2,2) triangles. None has a positive ray solution; 8 have no real solution at all. The single all-facing (2,2,2) triangle found has positive solutions, as R15 says.
- Upper-probability triangles {m_i ≤ b_i} (80 random b): none has a positive solution; 70 have no real solution.
- **CONJECTURE A62-NF:** for every non-facing (2,2,2) triangle in general position, the corner system has no positive solution. Each corner gives the linear relation x r_c + y r_a = |r_b| between ratios of adjacent facets, so the cycle is a composition of maps x ↦ r_a/(|r_b| − r_c x). A proof would bound the composed trace.

### 2.3 Translation of (DF), (ND) for signed fields (CHECKED)
- Let y ∈ relint F_k, q = u + tδ, and n with v_k·n = 1. Let g have one-sided normal slopes λ^in(y), λ^out(y). Then P(u + tδ, y)/t → ρ_y(δ·c(y)), where ρ_y(s) = s/λ^out for s > 0 and s/λ^in for s < 0 (this is the blow-up of §3, using that P(q,·) has normal slope → 1).
- So **(DF) ⟺ λ^in = λ^out on the faces (θ ≡ 1, no kink)**, and **(ND) ⟺ c ≢ 0 on each face**.
- Continuous PL fields generically have kinks, so they lie in R15's escape (E1). Theorem A62-1 closes that escape for PL, and A62-1′ for constant θ.

### 2.4 Two-level designs (veto + additive secondary) (CHECKED, argument sketch)
- E61 Thm 5.1 reduces any finite-view cover to a single-level chart σ̂ on N ⊇ D_K ∪ C, all of whose null-tie Bayes acts are coherent. The collar C contains full neighbourhoods of relint faces.
- R15 Thm 1 is local. It uses gambles in small balls around relint facet points, limits along facets to the corner rays (Lemma C needs only facet sequences h_n → r inside N), priors near p*, and UVN(a) at vertex priors.
- So Cor 2.3 applies to the reduced system whenever σ̂ is **strictly** sign-correct near the faces (E61 5.1(a) gives only weak signs) and satisfies (DF), (ND) at the separating prior.
- The thinning of the collar at the rays does not obstruct Thm 1(d) as written. It does mean that two-level designs naturally live in the "pinned/sliding edge" regime (E2), which is the place to look for an escape.

---

## 3. (b) Necessary conditions near the faces and rays

Standing assumptions: (1)–(4) with π* = u. Coordinates near y ∈ relint F_k: h = y + s n, with y in the face plane and v_k·n = 1, so s = v_k·h (s > 0 inside). "Inner/outer" refer to s > 0 / s < 0.

**N0 (g on the faces; PROVED for continuous c).** g = 0 on ∂D_K∖0. Indeed g > 0 a.e. on D_K and g ≤ 0 a.e. on U∖cl D_K, and ∂D_K∖0 ⊆ U. So c(F_k) ⊆ Π := 𝟙^⊥. By continuity, c_k ≥ 0 on F_k, and c_i has the weak sign of h_i there.
- *Box:* ✓ (g = min_{q∈Q} q·h vanishes on ∂D_Q).

**N1 (face QSA ⇒ monotone rotation; PROVED for continuous c).** For h, k ∈ F_k, Cone(c(h), c(k)) ∩ Π = ℝ₊c(h) + ℝ₊c(k), and P ≠ ∅ unless c(h) and c(k) are antiparallel. So Theorem A gives c(h+k) ∈ ℝ₊c(h) + ℝ₊c(k).
- Consequently the direction of c rotates monotonically along each face, and winds exactly once around Π as y runs once around ∂D_K. The sign sectors are visited in the order (−,+,+) → (−,−,+) → (+,−,+) → (+,−,−) → (+,+,−) → (−,+,−).
- At the crossing points the direction is fixed: c(−1,0,2) ∝ (−1,0,1) and c(0,−1,2) ∝ (0,−1,1) on F_3 (cyclically on the other faces).
- *Box:* ✓, trivially (no crossings).

**N2 (first-order convexity at u; PROVED for c continuous and Lipschitz near the faces, with g = λ^{in/out}(y)s + o(s) uniformly on compacts, λ^{in/out} > 0 continuous).**
- Statement: for every w ∈ ℝ³, the function φ_w(y) := −ρ_y(w·c(y)) is convex on relint F_k, where ρ_y(s) = s/λ^out(y) for s > 0 and s/λ^in(y) for s < 0.
- *Proof.*
  - For π = u + εw, G_ε(y,s) := g + ε w·c is strictly increasing in s for small ε. So locally B_π = {s > f_ε(y)}, and f_ε is convex because B_π ≐ an open convex cone (and the two coincide here).
  - f_ε(y)/ε → −ρ_y(w·c(y)), uniformly on compacts.
  - Limits of convex functions are convex. ∎
- λ^{in/out} > 0 follows from (2) at u for PL fields; it is an assumption otherwise.
- *Box:* ✓. c is linear on each face and θ = 1 (g = w·h on both sides of each face, inside one orthant), so φ_w is linear.

**N3 (kink direction; PROVED under N2's hypotheses).** If c(y) ≠ 0 and the direction of c rotates strictly through y, then θ(y) := λ^out(y)/λ^in(y) ≥ 1. That is, g is concave across the face: it is steeper outside than inside.
- *Proof.* Take w ⊥ c(y) with w·c changing sign at y. The convexity of φ_w at y compares slopes −(w·c)′ and −θ(w·c)′, which gives (θ − 1)(w·c)′ ≥ 0 on both sides. ∎
- *Box:* θ = 1 ✓.

**N4 (constant kink ⇒ linear normalised field; PROVED).** If θ is constant on F_k, put ĉ := c/λ^out. Then on F_k either ĉ ≡ 0, or ĉ is linear with ĉ_i = κ_i h_i for both crossing worlds i ≠ k, and ĉ_k = −ĉ_i − ĉ_j.
- *Proof.*
  1. **Locally linear where nonzero.** Near y₀ with ĉ(y₀) ≠ 0, take w in an open set with w·ĉ > 0 on a small conic neighbourhood V. Then φ_w = −w·ĉ is convex, and φ_{−w} = θ⁻¹·w·ĉ is convex, so w·ĉ is linear on V for an open set of w. Hence ĉ is linear on each component of {ĉ ≠ 0}.
  2. **No zero arc next to a nonzero arc.** At such a junction φ_w is 0 on one side and −ρ̂(t·w·a) on the other. Convexity for all w forces a = 0.
  3. **No isolated zero.** At an isolated zero ray, convexity for all w forces the two adjacent directions to be antiparallel: a′ = −μa. On F_3 both have third coordinate ≥ 0 (N0), so a = (x,−x,0). The middle arc (h_1, h_2 < 0) then forces x = 0.
  4. **Signs on a linear face.** A linear ĉ_i with the weak sign of h_i on a face where h_i changes sign equals κ_i h_i, with κ_i ≥ 0. ∎

**N5 (ray matching; PROVED for continuous c; CHECKED (sketch) for PL c with discontinuities at the rays, via the step lemma below).** At each ray r, the facet limits satisfy ĉ_{F}(r) ∝₊ ĉ_{F′}(r).
- **Step lemma (PROVED).** In the rescaled cross-section at r, the limit acceptance set is ∪_S S ∩ {ℓ_S·x > −w·c_S(r)} over the cells S around r. It must be convex for every w. At each wall between two cells, the two threshold lines must meet the wall at the same point. Otherwise the boundary contains a segment of the wall with accepted points on both sides of the wall's line, which contradicts convexity.
- An inner cell with g_S(r) > 0 is impossible when some adjacent face is displaced inwards (w with w·c_F(r) < 0).
- Chaining the walls between the two face-adjacent cells gives ρ_2(w·c^{(2)}(r)) = κ ρ_3(w·c^{(3)}(r)) on an open set of w. Hence the directions are proportional.
- *Box:* ✓ (c continuous).

**N6 (exclusivity lemma; PROVED; any measurable c).** Fix π and a face F_k. Say y ∈ relint F_k is:
- Y₁(π) if a.e. point of a small inner half-ball is in B_π and a.e. point of the outer half-ball is not;
- Y₂(π) if a.e. point of a full ball is in B_π;
- Y₃(π) if only the outer half-ball is accepted.

If B_π is essentially convex, then Y₃(π) = ∅, and Y₁(π) ≠ ∅ implies Y₂(π) = ∅.
- *Proof.*
  - A Y₁ point makes the face plane a supporting plane of the open convex cone C_π ≐ B_π, so C_π ⊆ {v_k·h > 0}. A Y₂ point then lies inside C_π but on that plane, which is a contradiction.
  - For Y₃, the supporting plane gives C_π ⊆ {v_k·h < 0}, which misses 𝟙 ∈ C_π. ∎
- *Box:* ✓ (vacuous: the box has no Y₁ points except at π = u).

**N7 (segment lemma; PROVED).** Suppose that along a segment π_t = (1−t)u + tπ′:
- every y in a set Y ⊆ relint F_k passes strictly from Y₁ (t < t*(y)) to Y₂ (t > t*(y));
- the inner side stays accepted throughout.

Then t* is constant on Y (by N6). If this holds for all π′ in an open set, the outer first-order data at Y are collinear: c^out(y) ∝₊ n (jump case), or d^out(y) ∝₊ n (vanishing case, c = s d^out + o(s)).
- *Proof.* The lines {π : π·c^out(y) = 0} must pass through a common point of every such segment, so they coincide. ∎

---

## 4. Theorems excluding classes of signed fields

**Theorem A62-1 (continuous PL; PROVED).**
- **Statement.** Let K be the reversed triangle and K' ⊆ relint K any compact convex set. Let c be continuous on U and linear on each cell of a finite polyhedral conic fan. Then c cannot satisfy all of:
  - (1) strict sign correctness a.e.;
  - (2) at π = u only;
  - (3) for all π in some neighbourhood of u;
  - (4).
- **Proof.**
  1. **Normal slopes are constant on each face.** On an inner cell σ adjacent to F_k, g = λ_σ(v_k·h). Here λ_σ > 0 by (2) at u: λ_σ = 0 would make g ≡ 0 on an open set. Continuity of g across a wall that meets relint F_k transversally forces equal λ on both sides. So λ^in_k and λ^out_k are constant on F_k, and N2 applies with constant θ_k.
  2. **Linear or vanishing.** By N4, on each face ĉ is either linear with crossing rows κ, or ≡ 0.
  3. **Linear faces contradict the rays.** Continuity at r_1, r_2, r_3 gives the system 2κ_2 = 3κ_1 − 2κ_3 and cyclic, in ĉ-units with λ constant. Its only solution is κ = 0. In direction-only form it is the elliptic Möbius system of §2.2, with no real solution. A face with some κ = 0 forces a wrong sign at a ray (e.g. ĉ = (0, κ_2h_2, −κ_2h_2) gives ĉ_3(r_1) < 0) or vanishes, and a vanishing face forces its neighbours to vanish at the shared ray. So **c ≡ 0 on ∂D_K**.
  4. **Vanishing contradicts strict signs.** On an inner cell σ adjacent to F_k, c = (v_k·h) d_σ. Continuity across transversal walls makes d_σ the same on the whole inner layer. But a crossing world i takes both signs of h_i on that layer while c_i = (v_k·h)d_i has one sign. That contradicts strict sign correctness on an open set. ∎
- **Box control:** steps 1–2 hold. No crossing world exists, so steps 3–4 never start. C62's `box_control.out` independently certifies boxes under the same checker conditions.
- **Exact illustration:** §5.3.

**Theorem A62-1′ (constant kink ratio; PROVED under N2's hypotheses + λ^{in/out} extending positively to the rays).** If θ_k is constant on each face and c is continuous, then c ≡ 0 on ∂D_K∖0 (steps 2–3 above, with ĉ = c/λ^out).
- In particular, every C¹ field with ∂_n g ≠ 0 on the faces (θ ≡ 1) is excluded, unless it vanishes on the faces. This includes smooth local-prior charts c_j = q_j(h)h_j with q continuous and in relint Δ on ∂D_K. (This is the signed-field form of Cor 2.3, by an independent route.)

**Theorem A62-2 (jump across a face; PROVED).**
- **Hypotheses.** c has uniform one-sided limits c^in, c^out, continuous on relint F_k, with g^in > 0 > g^out there and (ND) c_k^in, c_k^out > 0. Then (3) fails along [u, e_k].
- **Proof.**
  - Along π_t = (1−t)u + te_k the inner side stays accepted.
  - The outer side switches on at t*(y) = −g^out/(c_k^out − g^out) ∈ (0,1).
  - N7 gives c^out(y) ∝₊ n on all of relint F_k, using the open set of π′ = (1−η)e_k + ηw′ with w′ near u.
  - The crossing worlds force n_i = n_j = 0, so n ∝ e_k. Then g^out = n_k σ > 0, a contradiction. ∎
- **Mixed and one-sided jumps (CHECKED: case-analysis sketch under (ND), not a full proof; refereeing needed).** Suppose different sub-arcs of a face carry different types: g^in > 0 = g^out, g^in = 0 > g^out, or continuous. Each mixture is excluded by N6 plus the same collinearity mechanism (details: one Y₁ point forbids any outward displacement on the same face, so the outward data must be collinear, contradicting the crossing signs). If the sketch is right, **every finite-fan PL field with (ND) one-sided limits is excluded** (status: CHECKED, not PROVED):
  - continuous across the faces: A62-1 (with N5 for discontinuities at the rays);
  - jumping: this theorem.

**Theorem A62-3 (fields vanishing on a face; PROVED).**
- **Hypotheses.** c = s d^±(y) + o(s) near relint F_k, with d^± continuous and nondegenerate: u·d^{in/out} > 0, d_k^in > 0 > d_k^out, and d_i^out ≠ 0 off the crossing rays for the crossing worlds i. Then (3) fails along [u, e_k].
- **Proof.** As in A62-2, using the transition t*(y) = λ^out/(λ^out − d_k^out). N7 then gives d^out ∝ n, while d_i^out must change sign at the crossing ray. ∎
- For PL c this is automatic once c ≡ 0 on F_k (A62-1, step 4 is the continuous special case).

---

## 5. (c) Attacks on named candidate families (exact witnesses; `witnesses.out`, `attack_plchart*.out`)

Every witness below uses strict inequalities at continuity points. So it persists on open neighbourhoods of h, k and h+k and cannot be repaired on null sets. Given the gambles, B_π contains balls around h and k and misses a ball around h+k, so B_π is not essentially convex.

### 5.1 Pari-mutuel-affine c = (6/5)h − (1/5)(max h)𝟙 (CHECKED)
- u·c = 3P(h), so B_u = D_K. Every B_π is convex (a superlevel set of a concave function).
- **(1) fails on every U:** h = (1,10,10) ≥ 0 has c(h) = (−4/5, 10, 10).
- **Incoherent Bayes sets at interior priors.** π·c(e_i) = (6π_i − Σπ)/5, so B_π contains all positive gambles **iff min_i π_i/Σπ > 1/6** (exact criterion). For example, π = (1,2,9)/12 rejects the positive gamble (1, 1/100, 1/100): π·c = −89/1000.

### 5.2 Max-repaired PMA (CHECKED)
- Definition: c_i = max((6/5)h_i − M/5, h_i/10) if h_i > 0, else (6/5)h_i − M/5. This is sign-correct, but discontinuous on {h_i = 0}.
- **(4) fails.** Take h_δ = (1/10, −1−δ, 9/5) with δ = 1/10, 1/100, 1/1000. Then v_3·h_δ < 0, so h_δ is outside D_K, yet g(h_δ) = 13/100, 119/500, 311/1250 > 0.
- h_δ → (1/10, −1, 9/5) ∈ relint F_3, so h_δ ∈ U for every admissible K' once δ is small.
- Mechanism: the repair raises c_1 exactly in the band 0 < h_1 < M/6, which meets every crossing face.

### 5.3 Continuous PL local-prior chart (CHECKED; illustrates A62-1)
- **Construction.** Fan of the six planes h_i = 0 and h_i = h_j: 14 rays, 24 simplicial cells. At each ray, c_j = v_{k,j} r_j with k = argmax r (smallest index on ties); interpolate linearly.
- Exactly: strictly sign-correct, and g = min_k v_k·h. So (1) and (4) hold, and (DF) holds too (θ = 1).
- **Witness at π = u + (1/40)(−3,2,1) = (31/120, 23/60, 43/120):**
  - h = (−7/5, −24, 267/5): π·c = 7/3000 > 0;
  - k = (8/5, −129/5, 264/5): π·c = 19/750 > 0;
  - h+k = (1/5, −249/5, 531/5): π·c = −1/3000 < 0.

  All three are in D_K (v_3·h = 13/25, 22/25, 7/5 respectively).
- A second witness at π = (1/30, 8/15, 13/30) is in `attack_plchart.out`.
- The failure sits at the crossing point (0,−1,2) of F_3. There c_1 has slope 1/5 for h_1 > 0 and 2/5 for h_1 < 0, so c is not linear on F_3, exactly as A62-1 step 2 predicts.

### 5.4 E61 lower-prevision chart (discontinuous) (CHECKED)
At π = (1,2,3)/6, with no argmax ties at any of the three points:
- h = (89/50, 171/100, −69/50): π·c = 17/1500;
- k = (9/100, 127/100, −41/100): π·c = 13/1500;
- h+k = (187/100, 149/50, −179/100): π·c = −13/375.

All three are in D_K. This gives an exact form of E61 §5's numerical failure.

### 5.5 Mixtures of box rules (PROVED)
- Σ_m a_m min(l^m_j h_j, u^m_j h_j) = min(L_j h_j, U_j h_j), with L = Σa_m l^m and U = Σa_m u^m: the Minkowski sum of boxes is a box. Exact check on 500 random instances.
- So every B_π is a normalised-box cone D_{π⊙Q}, and (4) fails. Every face of a box cone lies in a closed orthant, whereas F_3 of D_K crosses h_1 = 0.

### 5.6 Smooth local-prior charts and other C¹ fields (PROVED via A62-1′ and Cor 2.3)
If they are nondegenerate on the faces, they are excluded.

---

## 6. (d) The design space that survives

For single-level signed fields (the auditor's ranking class) on any U = D_{K'}, a cover of the reversed triangle must have, on at least one face, one of the following:
- **(S1) Variable kink.**
  - What: c is continuous and nonzero on the face, and the kink ratio θ(y) = λ^out/λ^in is **non-constant**, with θ ≥ 1 wherever c rotates (N3).
  - Consequences:
    - g is neither PL nor C¹ across that face;
    - by N2 the normalised curve must satisfy "w·c/λ^out concave and w·c/λ^in convex for all w ∈ W₊(V)", locally on every small arc V;
    - at crossings the directions are fixed (N1);
    - at the rays the directions must match (N5);
    - so, by §2.2, **the face maps cannot be projectively linear**: the variable θ must bend the direction curve.
  - Status: this is the only regular continuous route left. I have no candidate. Whether N2 + N5 can be met at all is open; near u it is locally unconstrained (CHECKED by the slope computation in N3).
- **(S2) Degenerate first-order data.**
  - c ≡ 0 on a face with transverse data violating A62-3's nondegeneracy: higher-order vanishing, d_i^out ≡ 0 on an arc, or u·d^out = 0.
  - Or jumps where a one-sided limit of the anti-visible coordinate vanishes (c_k^out ≡ 0), outside A62-2's (ND).
- **(S3) Non-PL behaviour at the corner rays.** Non-unique clusters at r (R15's "sliding edge" E2) with c discontinuous there in a way not covered by the PL step lemma (N5).
- **(S4) No one-sided limits** at the faces (oscillating fields), or fields that are not Lipschitz near the faces.
- **Outside the certificate.** Rankings with non-null ties at boundary priors, where only the auditor's sandwich holds, are not tested here.

**What any constructor must check first (cheap filters, all exact):**
1. g = 0 on ∂D_K;
2. the directions at the six crossing points and the three rays;
3. θ ≥ 1 and non-constant on some face;
4. the failure mechanism of §5.3: no "convex kink" of w·c across a wall meeting a face, for w ⊥ c(crossing point);
5. the segment test N7 along [u, e_k].

---

## 7. Status table

| Item | Status |
|---|---|
| Lemma 1.1: under (1), coherent ⟺ essentially convex (all π ≥ 0, boundary included) | PROVED |
| Thm A: (3) ∀π ⟺ weak QSA on jointly accepted pairs (c continuous off a closed null cone, with (2)) | PROVED |
| Brief's version: strict form only sufficient; "all pairs" needs the joint-acceptance restriction (boundary-prior pairs) | CHECKED |
| R15 Thm 1 / Lemma 3.2: no use of (S); vertex coherence not needed; (SH) holds for certified signed fields; (NA_w) automatic | CHECKED |
| **Cor 2.3: reversed triangle, any interior p\*: R15 corner system has no real solution (elliptic Möbius, angle arccos 3/4); no box needed** | **PROVED** (given refereed R15 Thm 1) |
| Positive control: same code returns T1's x± = 23/14 ± 3√37/14 | CHECKED |
| Non-facing (2,2,2) triangles: no positive corner solution (90/90 sampled) | NUMERICS; CONJECTURE A62-NF |
| For signed fields: (DF) ⟺ no kink across faces (θ ≡ 1); (ND) ⟺ c ≢ 0 on faces | CHECKED |
| Two-level veto + secondary designs fall under Cor 2.3 if the E61-reduced chart is strict, (DF), (ND) | CHECKED (sketch) |
| N0–N3 necessary conditions; box control passes each | PROVED |
| N4 constant kink ⇒ linear or zero on faces | PROVED |
| N5 ray matching: continuous | PROVED |
| N5 ray matching: discontinuous PL | CHECKED (sketch) |
| N6 exclusivity lemma; N7 segment lemma | PROVED |
| **Thm A62-1: no continuous PL field (any fan, any K') satisfies (1), (2)@u, (3) near u, (4)** | **PROVED** |
| Thm A62-1′: constant kink ratio (incl. C¹) ⇒ c ≡ 0 on ∂D_K | PROVED (stated regularity) |
| Thm A62-2: two-sided jump across a face with (ND) | PROVED |
| Mixed/one-sided jumps ⇒ all (ND) finite-fan PL fields excluded | CHECKED (sketch; referee needed) |
| Thm A62-3: face-vanishing with nondegenerate transverse data | PROVED |
| PMA: (1) fails on every U; B_π coherent iff min π̂ > 1/6 | CHECKED (exact) |
| Max-repaired PMA: (4) fails | CHECKED (exact) |
| Continuous PL local-prior chart: explicit incoherent Bayes set within 1/40 of u | CHECKED (exact) |
| E61 chart: tie-free exact witness at (1,2,3)/6 | CHECKED (exact) |
| Box mixtures are boxes | PROVED |
| Surviving space S1–S4; no surviving candidate found | statement; existence open |

**Scope warning.** Everything negative here concerns the stated classes of single-level signed fields (and, conditionally, E61-reduced two-level designs) under the stated regularity. None of it is an impossibility claim for coverage of the reversed triangle by arbitrary rankings, nor by fields in S1–S4.
