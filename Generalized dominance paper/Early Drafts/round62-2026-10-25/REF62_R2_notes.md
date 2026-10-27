# REF62-R2 — Referee report on the new results in REF62_fd_notes.md (25 Oct 2026)

Labels: PROVED (proved or re-derived here; not yet independently refereed) / CHECKED (exact rational computation) / CONJECTURE / NUMERICS.
Scripts are in `ref62r2py/`; run each with `python3 -I`:
- `r2_geom.py` → `r2_geom.out`: exact geometry and orthant-planarity;
- `r2_chart.py` → `r2_chart.out`: both charts, all prior supports, continuity;
- `r1_pmm.py` → `r1_pmm.out`: R1 sanity witness and the PMM upgrade.

## 0. Summary

Most of what REF62 adds holds up:
- **Lemma R0** is correct.
- **Theorem R1 (a)–(b)** are correct, with three small gaps that are easy to close. Part (a) says every g_ij is linear; part (b) says D_K must be orthant-planar.
- **Proposition R2** is correct, including boundary priors. Its proof sketch only argues one of the two inclusions; I supply the other (§3).
- **The n = 3 characterisation, both examples, and the O61 Thm B upgrade** are correct.

There is one real error and three smaller faults.

**The error.** R1's final clause says that if c is continuous then K is a normalised box, so that continuous certificate charts reach exactly the boxes. **This is false.** I give a continuous, regular, strictly sign-correct chart that meets the full certificate for every orthant-planar K, including the cyclic triangle and the non-box hexagon (§2.3; PROVED, CHECKED). The proof of step 4 silently assumes that the scalar factor λ is constant on each mixed orthant. The statement is true under that assumption, and that assumption holds for every continuous piecewise-linear chart (§2.4, PROVED).

**The smaller faults.**
- R2 is stated "on every U = D_{K′} with K′ ⊆ K". The four certificate conditions do hold there. But (LF) holds only when K′ ⊆ relint K, and (LF) is part of the coverage notion, so it must be named.
- The class R2 covers is exactly R10b §7's "cevian polygons". R10b had already isolated that class, its cyclic product condition and a non-box hexagon example, and had left coverage OPEN. R2 settles that open question; it should cite R10b §7 as its source.
- "The live distinction for triangles is general position" overstates. Triangles with one or two cevian edges are neither in general position nor orthant-planar, and they remain OPEN.

## 1. Verdict table

| # | REF62 item | Verdict | Notes |
|---|---|---|---|
| 1 | Lemma R0: c_i/(−c_j) = g_ij(h_i/(−h_j)) a.e. on {h_i>0>h_j}, g_ij nondecreasing, independent of other coordinates | **CORRECT** (PROVED) | The quadrant threshold is τ = (1−t₀)/t₀, where t₀ = min_Q m_i; τ = ∞ when e_j ∈ Q. Countably many rationals give one null exceptional set. |
| 2 | R1 hypothesis remark "Interior priors a.e. plus limits suffice" | **GAP** (plausible; sketch only) | Hausdorff compactness of Q_π works, but only if {π·c = 0} is null at the limiting edge prior. That nullity is not inherited from interior priors. Either state it as a hypothesis or keep the all-π certificate. |
| 3 | R1 hypothesis "(R) holds for the round-62 continuous PL ansatz" | **GAP** | True if sign(c_j) = sign(h_j) holds *everywhere* off {h_j = 0}, not just a.e. A PL cell on which c_j vanishes along a boundary ray inside an open orthant (allowed by "a.e.") breaks the lower bound in (R). |
| 4 | R1 step 1 (g_ij concave) | **CORRECT** (re-derived) | Uses all levels t and ratios λ = π_i/π_k > 0. F = g_kj⁻¹ is differentiable with F′ > 0 at t = H(b) whenever H′(b) ∈ (0,∞), and such b exist because H is Lipschitz with H(0⁺) = 0 and H(∞) = ∞ under (R). Minor gap: the passage from a.e. to exact convexity of the slice. Closed in §2.2 by monotonicity. |
| 5 | R1 step 2 (φ_j convex, φ_j(0⁺) = 0) | **CORRECT** | This is the sublevel/hypograph version of step 1. The range of φ_k is (0,∞) by (R). |
| 6 | R1 step 3 (g_ij(ρ) = κ_ij ρ) | **CORRECT** | Concavity with g(0⁺) ≥ 0 makes g/ρ nonincreasing. Step 2 makes g/ρ nondecreasing. So g/ρ is constant. |
| 7 | R1 (a)–(b): c = λ(h)·d_σ⊙h on mixed σ; D_K orthant-planar | **CORRECT** (PROVED) | It also gives κ_ij independent of σ, so d_σ is determined by six numbers κ_ij (§2.1). |
| 8 | **R1 (c): "If c is continuous … K is a normalised box"**, and the consequences "continuous certificate charts reach exactly the normalised boxes", "extends F61 Thm A to non-convex charts", and row-13 wording "continuous ⇒ boxes, discontinuous ⇒ orthant-planar" | **ERROR** | Counterexample (§2.3): c(h) = ‖h‖₁·(d_σ⊙h)/‖d_σ⊙h‖₁ on mixed orthants, with a Lipschitz blend on the pure orthants. It is continuous, satisfies (R) and the full certificate, and has B_𝟙 = D_K for the cyclic triangle, which is not a box. CHECKED: 0 failures in 215 124 exact (π,h) tests, and continuity exact on 4 800 face points. **True version (PROVED, §2.4):** continuous **and** λ constant on each mixed orthant ⇒ box. Every continuous piecewise-linear chart on a finite conic partition has constant λ. |
| 9 | R1 consequences: T1 and the reversed triangle are not orthant-planar, so no regular chart meets the full-domain certificate; with FD-1, none does on any two-sided domain | **CORRECT** | CHECKED exactly: rays (−1,−1,5)/12 and (2,2,−3)/25 have no zero coordinate, and the exact deciding-vertex sets are empty on 3 mixed orthants each. The FD-1 step is fine because R0/R1 only use gambles that are not ≤ 0. Unaffected by row 8. |
| 10 | Prop R2: B_π = D_{ν(π⊙K)} for every nonzero π ≥ 0, including boundary priors | **CORRECT** (PROVED, §3) | Despite the discontinuity of c across coordinate planes. The key identity is D_K ∩ cl σ = {d_σ·x > 0} ∩ cl σ, applied to x = π⊙h ∈ cl σ∖0. REF62's sketch proves only "⊇". CHECKED: 0 mismatches over all 7 support patterns, with adversarial gambles near rays, faces and coordinate planes. Exact ties occur only on the predicted hyperplanes. |
| 11 | R2: d_σ ≫ 0 (implicit) | **GAP (closed)** | Automatic: ∂D_K ∩ σ is a nonempty relatively open piece of d_σ^⊥, so ±d_σ is an exposed normal, i.e. in cone K. |
| 12 | R2: null zero sets; at most one orientation positive; sign correctness; B_𝟙 = D_K | **CORRECT** | The zero set lies in finitely many hyperplanes (π⊙d_σ)·h = 0. h and −h cannot both lie in D_{π⊙K}. |
| 13 | R2 on one-sided U = D_{K′}, K′ ⊆ K: certificate conditions | **CORRECT** | U ∩ B_π = D_{conv(K′ ∪ ν(π⊙K))}, and U ∩ B_𝟙 = D_K. |
| 14 | R2 on U: (LF) | **GAP (scope)** | (LF) at D_K on U = D_{K′} holds iff K′ ⊆ relint K (P61 A11 and its converse). For K′ meeting rel∂K the certificate holds but (LF) fails. State the coverage claim for K′ ⊆ relint K. |
| 15 | n = 3: orthant-planar ⇔ every edge line of K passes through a vertex of Δ; at most 6 edges | **CORRECT** (PROVED, §4) | Also: an orthant-planar K ⊆ relint Δ is automatically a polygon. |
| 16 | "Boxes = such hexagons with trivial holonomy (Ceva-type product)" | **CORRECT** (precise form PROVED, §4) | An orthant-planar K is a normalised box iff κ₁₂κ₂₃κ₃₁ = κ₁₃κ₃₂κ₂₁. The log-linear system is a 6-cycle with rank 5. Non-degenerate boxes are hexagons. CHECKED on a box control: holonomy 1. |
| 17 | Non-box hexagon, holonomy 11/10 | **CORRECT** (CHECKED exactly) | Convex in the given order, orthant-planar, κ σ-independent, holonomy 11/10, vertex types ATT, AAS, TAT, SAA, TTA, ASA. Not VB-type: three vertices are not strictly visible. Same class as R10b §7's example. |
| 18 | Cyclic triangle conv{(1,4,2),(2,1,4),(4,2,1)}/7: genuinely orthant-planar | **CORRECT** (CHECKED exactly) | Rays (2,0,−1), (−1,2,0), (0,−1,2) (×1/7). Each mixed orthant has exactly one deciding vertex. K = {m₃ ≤ 2m₁, m₁ ≤ 2m₂, m₂ ≤ 2m₃}. Holonomy 1/8, so not a box. Types ATC, CAT, TCA. |
| 19 | Cyclic triangle genuinely not covered by earlier constructions | **CORRECT** (CHECKED against the listed constructions) | Not VB-type (no S at any vertex), nor exempt-point VB. Not a box. Not a contamination, PMM, belief-function core or interval: its edges are not parallel to sides of Δ, so it is not the core of any lower probability. Not a chamfer, and the dense approximation is only approximate. R10b §7 lists cevian polygons as OPEN. Consistent with R10b Thm PL: ν(π⊙K) contains two vertices of K only at π ∝ 𝟙 (hand check). |
| 20 | "Triangle outside 𝒱_B by O61 Thm A + Cor A(d)" | **CORRECT, conditional** | Applicability CHECKED: each vertex is tangential from exactly one world and A/C from the others. It relies on Cor A(d), which O61 calls a sketch and ROUND61 calls "repaired for n = 3 polytopes". I did not re-check that repair. |
| 21 | "R10a Thm R and E61 Cor 5.2 / O61 Thm B do not apply" | **CORRECT** | Thm R needs general position: each coordinate crosses on exactly one facet here, not two, and every ray has a zero coordinate. Whether some concave chart covers the cyclic triangle on a one-sided U is not settled. On the full domain, F61 Thm A says no. R10a's phrase "excluded for every triangle" (lines 160, 300) should read "every triangle in general position". |
| 22 | "Sharp-cornered triangle exactly covered; 'sharp corners' no obstruction" | **CORRECT** | |
| 23 | "The live distinction for triangles is general position" | **OVERSTATED** | Fully cevian triangles (three cevian edges) are covered. General-position triangles are excluded only from specific classes (R10a, R15, O61). Triangles with one or two cevian edges are OPEN. Label it a heuristic/CONJECTURE. |
| 24 | O61 Thm B upgrade to all interior n = 3 PMM triangles | **CORRECT** (PROVED; steps re-checked) | Vertex v^k: types A at k and C elsewhere. Ray r_i = u_i𝟙 − e_i lies on F_{v^j} and F_{v^k}. World i crosses on both, and worlds j, k on one each. det = u₁+u₂+u₃−1 = δ (sympy). CHECKED on 6 random exact instances. Steps 1–5 of O61 Thm B are generic, given non-visibility of every vertex. |

## 2. Theorem R1

### 2.1 What R0 already gives

R0 says the threshold for each ordered pair (i,j) does not depend on the other coordinates. So in R1(a), κ_ij = d_σ,i/d_σ,j is **the same for every mixed σ with σ_i = + and σ_j = −**.
- For n = 3 the six numbers κ_ij determine every d_σ up to scale.
- Across a face {h_m = 0} between two mixed orthants, d_σ and d_σ′ are proportional off coordinate m.
- CHECKED: κ is σ-independent for the hexagon, the cyclic triangle and the box (`r2_geom.out`).

This is what makes the continuous chart of §2.3 possible: the *direction* field of d_σ⊙h is already continuous across mixed–mixed faces.

### 2.2 Closing the a.e. gaps (PROVED)

**g_ij is continuous and determined everywhere.** Under (R), f = c_i/(−c_j) is continuous on the open quadrant, and f = g∘ρ a.e. Suppose f(h) < α < f(h′) at two points with ρ(h) = ρ(h′). Then two open neighbourhoods have ρ-images overlapping in an interval I. Since ρ is a submersion, g < α a.e. on I and g > α a.e. on I, a contradiction. So g∘ρ = f everywhere, with g continuous.

**The slices are exactly convex.** In step 1, O := {λG(a) + H(b) > t} is open and agrees a.e. with an open convex set C, with O ⊆ C. The complement C∖O = C ∩ {λG + H ≤ t} is a down-set, because G and H are nondecreasing. If it had a point, it would contain a small open box inside C, which has positive measure. So O = C. Step 2 is the same argument.

### 2.3 Counterexample to R1(c) (PROVED; CHECKED in `r2_chart.out`, chart B)

Let K be any orthant-planar target with deciding vectors d_σ (n = 3). Define:
- **Mixed orthant σ:** c(h) := ‖h‖₁ · (d_σ⊙h)/‖d_σ⊙h‖₁, i.e. λ(h) = ‖h‖₁/‖d_σ⊙h‖₁.
- **Pure orthant s ∈ {+𝟙, −𝟙}:** c_l(h) := h_l·w_l(h), with
  - w_l = (|h_a| f^{(b)}_l + |h_b| f^{(a)}_l)/(|h_a| + |h_b|), where {a,b} = {1,2,3}∖{l};
  - f^{(m)}_l(h) := ‖h‖₁ d^{(m)}_l/‖d^{(m)}⊙h‖₁;
  - d^{(m)} is the deciding vector of the mixed orthant across {h_m = 0}.

Checks:
- **Continuity.** Across a mixed–mixed face, d_σ⊙h and d_σ′⊙h are positive multiples of each other (§2.1), so the normalised formulas agree. Across a mixed–pure face {h_m = 0}, w_l = f^{(m)}_l, which is the mixed value. On the l-axis, f^{(a)}_l = f^{(b)}_l = 1, so the blend is continuous. CHECKED: 0/4 800 exact face mismatches, and all 6 axis limits agree.
- **(R).** Every piece is Lipschitz: on the l-axis, f^{(a)} − f^{(b)} = O(|h_a| + |h_b|). Also c_j/h_j ∈ [min d/max d, max d/min d] on mixed orthants, and similarly on pure ones.
- **Certificate.** c is strictly sign-correct. On mixed orthants, π·c = λ(h)·(π⊙d_σ)·h with λ > 0, so B_π is *identical* to R2's: B_π = D_{ν(π⊙K)} for all π ≥ 0. Zero sets are null. B_𝟙 = D_K.
- **Conclusion.** For the cyclic triangle (holonomy 1/8) and the hexagon (11/10), K is not a box. CHECKED: 0 mismatches in 215 124 and 285 348 exact (π,h) tests. λ is visibly non-constant, e.g. 3 versus 21/8 on (+,+,−).

**General principle (PROVED).** Replacing c by λ(h)c with any positive 0-homogeneous λ leaves every Bayes set {π·c > 0} unchanged. So the certificate sees only the direction field of c. Continuity of c is then equivalent to continuity of that direction field. The value-matching seams of the round-62 continuous-PL ansatz are strictly stronger than continuity. They are the "projective factors ξ_F" of R10a's comparison remark, set to 1.

### 2.4 The correct statement of R1(c) (PROVED)

**Claim.** If c is continuous at the 2n axis rays and λ is constant on each mixed orthant, then K is a normalised box.
- The ray s·e_l lies in cl σ for every mixed σ with σ_l = s.
- Continuity there gives λ_σ d_σ,l = C_l^s for all such σ.
- So d_σ ∝ (l_j if σ_j = +, u_j if σ_j = −), and convexity of B_𝟙 forces l ≤ u.
- This needs only continuity at the axis rays. No holonomy argument is needed.

**Continuous PL charts have constant λ.** On a full-dimensional cell τ ⊆ σ we have c = M_τh = λ(h)d_σ⊙h. For l ≠ l′, (m_l·h)·h_{l′}d_{l′} = (m_{l′}·h)·h_l d_l is a polynomial identity on τ. By unique factorisation, m_l·h = βh_l, so λ is constant on τ. Values match across interior walls, where c ≠ 0. So λ is constant on σ.

**Corrected row 13.** *Full domain, certificate, regular charts: the reachable targets are exactly the orthant-planar ones, continuous or not. Continuous piecewise-linear (more generally, orthant-linear) charts reach exactly the normalised boxes.*

## 3. Prop R2 at boundary priors (PROVED)

Let σ be a mixed orthant, and recall D_K ∩ σ = {d_σ·h > 0} ∩ σ with d_σ ≫ 0.

**Identity.** D_K ∩ cl σ = {d_σ·x > 0} ∩ cl σ.
- **(⊆)** Let x ∈ D_K ∩ cl σ and suppose d_σ·x ≤ 0. Choose s ∈ σ with d_σ·s < 0. This is possible because σ is mixed and d_σ ≫ 0. For small ε, y = x + εs lies in σ ∩ D_K, since D_K is open, but d_σ·y < 0. Contradiction.
- **(⊇)** Let x ∈ cl σ with d_σ·x > 0, and suppose x ∉ D_K. Pick m ∈ K with m·x ≤ 0 and s ∈ σ with m·s < 0. Then y = x + εs lies in σ, has d_σ·y > 0, and has m·y < 0. Contradiction.

**Application.** For h ∈ σ and π ≥ 0 nonzero, x = π⊙h ∈ cl σ∖0 and π·c(h) = d_σ·x. So π·c(h) > 0 ⇔ π⊙h ∈ D_K ⇔ h ∈ D_{π⊙K}. On the pure orthants both sides agree trivially. Hence B_π = D_{ν(π⊙K)} a.e. for every nonzero π ≥ 0.

The discontinuity of c across coordinate planes is irrelevant, because the argument runs orthant by orthant on h. A boundary prior moves x = π⊙h onto ∂σ, never h itself.

## 4. n = 3 geometry (PROVED)

**Rays and edges.** The extreme ray of cl D_K for an edge [v,w] of K is v×w. It lies on {h_l = 0} iff e_l ∈ span(v,w), i.e. iff the edge line passes through e_l.

**No ray in a pure orthant.** Rays satisfy min_K m·r = 0, so none lies in an open pure orthant.

**Necessity.** If a ray lies in an open mixed orthant, two facets with distinct normals meet inside σ, so σ is not planar.

**Sufficiency.** Work on the sphere, in a mixed triangle T. P = cl D_K ∩ T is convex. It contains the side of T on which the closed positive (or negative) orthant lies, since cl ℝ³₊∖0 ⊆ D_K, and it omits the opposite vertex. Its boundary in int T is therefore one connected arc. With no polygon vertex in int T, that arc lies in one great circle, so D_K ∩ σ is a half-space intersected with σ.

**At most 6 edges.** Each edge line is a supporting line through one of the three external points e_l, and each such point has exactly two supporting lines.

**A polygon automatically.** An orthant-planar K ⊆ relint Δ is a polygon: ∂D_K is covered by at most 6 planar pieces, because coordinate planes cannot carry 2-dimensional pieces of ∂D_K when K ⊆ relint Δ.

**Box criterion.** κ_ij = l_i/u_j is a log-linear system on the 6-cycle l₁–u₂–l₃–u₁–l₂–u₃. It is solvable iff the holonomy equals 1, and then D_K and D_box agree on every orthant.

**Family.** The cyclic triangles {m₃ ≤ tm₁, m₁ ≤ tm₂, m₂ ≤ tm₃}, t > 1, are all orthant-planar with holonomy t⁻³ (CHECKED for t = 3/2, 2, 3).

## 5. Sanity check of R1's mechanism (CHECKED, `r1_pmm.out`)

Take c_i = h_i|h_i|/‖h‖₁. This chart is regular and strictly sign-correct, with g_ij(ρ) = ρ², which is not linear.
- At every edge prior, B_π = {√π_i h_i + √π_j h_j > 0} is coherent: 0/20 000 mismatches. So R0 alone forces nothing.
- At π = 𝟙 the Bayes set is not convex. Take h = (−5/2, −1, 7/2) and k = (−4, 7, −5). Then Σπ_i h_i|h_i| = 5 for h and 8 for k, but −17/2 for h + k.
- This matches R1, which needs full-support priors in steps 1–2.

## 6. Corrections to REF62

- **§0 and §2, R1 conclusion, and the "Consequences" bullet.** Replace "If c is continuous … K is a normalised box" and "continuous certificate charts reach exactly the normalised boxes" with the §2.4 statement. Add the §2.3 counterexample.
- **§4 row 13.** Use the corrected text in §2.4.
- **R2.** Add "d_σ ≫ 0 (automatic)". Add the (⊆) half of the proof. Restrict (LF) to K′ ⊆ relint K. Remove "the chart is discontinuous" as a reason that R10a, E61 and O61 do not apply: a continuous chart also works, and the real reasons are non-general position and non-convexity. Cite R10b §7 (cevian polygons, cyclic condition, coverage OPEN there) as the class R2 now settles positively.
- **"Live distinction is general position."** Relabel it CONJECTURE. Partially cevian triangles are OPEN.
- **R1 hypotheses.** Either drop "interior priors a.e. plus limits suffice" or add nullity of ties at edge priors. Replace "(R) holds for the ansatz" with "(R) holds for continuous PL charts that are sign-correct everywhere off the coordinate planes".

## 7. Implication for round 62

The certificate depends only on the direction field of c (§2.3). An exclusion of the *continuous piecewise-linear* ansatz on one-sided U, with values matching on seams, therefore says nothing about continuous charts in general. The natural relaxation is piecewise-linear directions with a free positive scalar per cell: projective matching across seams.
- On the full domain this relaxation still yields only orthant-planar targets (R1(a)–(b)), so T1 and the reversed triangle stay excluded there for regular charts.
- On one-sided U, R1 does not apply.
