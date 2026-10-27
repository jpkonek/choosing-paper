# PP6. Allocation between selected models (Brief 38, Task B)

20 October 2026, night. Labels:
- **PROVED**: the full argument is given here. One reader (me); not refereed.
- **CHECKED**: an exact finite computation. The combinatorics are in exact rationals. Measures are closed-form solid angles evaluated in floating point, with error ≤ 1e-14 against margins ≥ 6e-7.
- **NUMERICS**: grid evidence with a positive margin, but no continuum certificate.
- **CONJECTURE**.

Scripts are in `PP6_py/` (run `python3 -I <script>` inside that folder; outputs are in `*.out`).

Setting: audit's family K_p = p + 3ε min_j p_j (Δ − u), C_p = D_{K_p}, for ε = 0.3 and 0.1. Problems are Gaussian on R³, and ν = μ × counting on the rank steps. For d = rec(C_p, C_q):
- a_i = ν(P_i) is the mass of steps C_q adds at world i;
- b_i = ν(Q_i) is the mass of steps it removes;
- Φ_i = 2a_i − b_i;
- W(d) is the set of worlds accepting C_p ⪯_i C_q.

I add no assumption to the programme.

---

## 0. Verdicts

1. **This subproblem is not obstructed.** A closed allocation passes all five requirements:

       W_add(d) = { i : ν(P_i) ≥ ν(Q_i) },  i.e.  i ∈ W(rec(C_p,C_q)) iff L_i(C_p) ≤ L_i(C_q),

   where L_i(X) = ν(U_i(X)) is world i's additive rank-step loss.
   - **Theorem 5 (PROVED, conditional on (AC)).** W_add satisfies all of the following: eligibility; guidance; all seven face obligations for every anchor; (TC); no selected model dominated; closed accepted sets; and (IB).
   - **(AC)** is the statement: no selected model is weakly additively Pareto-dominated by another.
     - W_add passes **if and only if** (AC) holds.
     - (AC) is PROVED at every boundary index.
     - In the interior it is NUMERICS: 11,476-point grids give a positive margin at ε = 0.1, 0.3 and 0.9.
   - **CHECKED.** W_add has 0 violations on all six grids, confirmed by an independent checker.
2. **Two exact identities (Lemma 1, PROVED).** Between regular models, a_i + b_i = M(d) is the same at all three worlds, and a_i − b_i = ΔL_i. Hence:
   - Φ_i = (M + 3ΔL_i)/2;
   - eligibility is ΔL_i ≥ −M/3;
   - guidance is ΔL_i = M.

   The whole subproblem therefore runs on the pair (ΔL(d), M(d)).
3. **Closed form (Lemma 2, PROVED; CHECKED to 2e-14).** L_i(C_p) = [2 per(conv(e_i ∪ K̂_p)) − per(K̂_p)] / 2π, with spherical perimeters (K̂_p is K_p projected radially onto the sphere).
4. **Anchors (Lemma 3, PROVED; CHECKED: 0 exceptions).** From an interior source, A(rec(C_p, C_q)) never meets ∂Δ. So the only face obligation is W ≠ ∅. Boundary anchors occur only for boundary sources.
5. **(IB) (CHECKED).** No two distinct ordered pairs on any grid have the same record.
   - This used an exact overlay test on all 54 mass-fingerprint coincidences, which were mirror pairs on the edges.
   - (IB) linking is therefore vacuous here. W_add is record-based in any case.
6. **Infinitesimal records (§2).**
   - **Shape lemma (Lemma 4, PROVED).** Under a direction-dependent rule, the directions accepted at one world near a chamber point are either contained in a closed half-circle (order type) or symmetric (reciprocal type). Nothing else is compatible with (TC) on small triangles.
   - **Consequences (PROVED).**
     - Uniform sticky slack fails (κ > 0 fails as soon as κ < max_v ℓ_i/m), and so does the whole eligible pool.
     - A world with guidance directions must be of order type.
     - If one world is inactive, the other two carry exactly opposite local orders. This is the selected-model form of PP4 Prop 3.2.
   - **NUMERICS (72-direction SAT).** At generic interior points and near u, every world must be of order type. Near e_1, one world may drop out.
7. **Grids (§3, CHECKED).** On the e_1-, u- and whole-simplex grids at ε = 0.3 and 0.1, the problem is SAT and the backbone is small.
   - Every forced acceptance is a face obligation with only one eligible world. No refusal is forced.
   - Each of the 1,884 eligible sticky records (ΔL_i < 0) is acceptable in some allocation.
   - Strict 4-cycles at every world are realizable.
   - Audit's greedy rule fails on the e_1 grid. Its minimal core has two literals and is audit's mechanism, sited on the edge [e1,e3].
8. **What this does and does not decide (§4).** The selected-to-selected layer does not discriminate. It is passed by the additive rule, which FF2 Thm 4.1 excludes for the full system. Any obstruction must therefore come from records to non-selected rivals, coupled to this layer through mixed triples.

---

## 1. Setting and three exact facts

**Lemma 1 (PROVED; CHECKED on 100 random pairs to 8e-16).** Let X and Y be regular (no contradiction).
- Then a_i + b_i = M(d) := μ(A↔S) + μ(S↔B) + 2μ(A↔B) at every world.
- And a_i − b_i = L_i(Y) − L_i(X) =: ΔL_i.

*Proof.* On a changed problem, a regular change moves every world's rank by the same number of steps: A↔S and S↔B move by 1, and A↔B by 2. Unanimous problems are fixed or worsened the same way at all worlds. So |r_i(Y) − r_i(X)| is world-independent. The second identity is additivity of ν. ∎

Consequences for selected records:
- Φ_i ≥ 0 ⟺ ΔL_i ≥ −M/3.
- Guidance at i ⟺ b_i = 0 ⟺ ΔL_i = M.
- A strict improvement ⟺ ΔL_i = −M.
- Audit's count Σ_iΦ_i ≥ 0 reads ΣΔL_i ≥ −M.
- Both directions are eligible at i ⟺ |ΔL_i| ≤ M/3.

**Lemma 2 (perimeter formula; PROVED; CHECKED, 200 random (p, ε), max error 2.4e-14 against the cell computation).** Write v_1, v_2, v_3 for the vertices of K_p (v_k is the vertex towards e_k), θ for angles in R³, and {i, j, k} = {1, 2, 3}. Then

    L_i(C_p) = (1/π)[ θ(e_i,v_j) + θ(e_i,v_k) + ½θ(v_j,v_k) − ½θ(v_i,v_j) − ½θ(v_i,v_k) ].

*Proof.*
1. Count steps: r_i(g) = 1[some x ∈ K is on the wrong side for i] + 1[all of K is].
2. A plane g^⊥ puts some point of K on the opposite side from e_i iff it meets H_i := conv(e_i ∪ K). It puts all of K there iff it meets H_i and misses K.
3. Crofton on S²: the Gaussian measure of the planes meeting a convex spherical set equals its perimeter divided by 2π. So L_i = (2 per H_i − per K)/2π.
4. v_i lies inside conv(e_i, v_j, v_k). Its barycentric weights are s/(1 − w_i), (p_j − s/3)/(1 − w_i) and w_k/(1 − w_i), where s = 3ε min p and w = v_j; all are positive. Hence per H_i = θ(e_i,v_j) + θ(e_i,v_k) + θ(v_j,v_k). ∎

For ε = 0 this reduces to L_i = 2θ(p, e_i)/π.

**Lemma 3 (no boundary anchors from interior sources; PROVED; CHECKED: 0 of 4,284 interior-source records on the grids).** Let p be interior and q ≠ p. Then A(rec(C_p, C_q)) ∩ ∂Δ = ∅.

*Proof.*
1. A boundary r gives a precise C_r, which is never silent.
2. If K_p ⊄ K_q, some non-null set of lines meets K_p and misses K_q. There C_p is silent, so no precise C_r agrees with C_p on D.
3. If K_p ⊆ K_q, take r ∈ ∂Δ, so r ∉ K_p. For every direction n in the open arc where n·r > h_{K_p}(n), the lines with offsets in (h_{K_p}(n), min(n·r, h_{K_q}(n))) separate r from K_p and meet K_q. So they lie in D, and C_r disagrees with C_p on them. This set is non-null unless h_{K_q} = h_{K_p} on that open arc.
4. On the normal cone of each vertex v_k, h_{K_q} − h_{K_p} = n·(q − p + (s_q − s_p)(e_k − u)) is linear. Vanishing on an open sub-arc would make K_p and K_q share the vertex v_k, i.e. q − p = (s_p − s_q)(e_k − u).
5. This is impossible for 0 < ε < 1:
   - if the minimum coordinate of p is not k, then m(q) − m(p) ≤ (s_q − s_p)/3 < (s_q − s_p)/(3ε);
   - if it is k, then m(q) < m(p) while s_q > s_p.
   So s_q = s_p, hence q = p. ∎

Hence the seven face obligations reduce to the following:
- interior sources: W ≠ ∅;
- edge sources: W ∩ supp p ≠ ∅, plus any further boundary anchors (computed exactly by LP; 390 records on the e_1 grid, 486 on the whole-simplex grid);
- vertex sources: guidance.

---

## 2. Infinitesimal displacement records (Approach 1)

### 2.1 First-order structure

Fix p with a unique minimum coordinate (a chamber point). For q = p + tv:
- ΔL = t ℓ(v) + o(t), with ℓ = dL(p) linear;
- M = t m(v) + o(t), with m a norm (m(−v) = m(v)). The record changes strips of lines at the three vertices of K_p, and |n·dv_k| enters symmetrically.

So the first-order eligibility region of world i is E_i = {ℓ_i ≥ −m/3}. It is the complement of an open arc F_i of length < π. Also:
- the guidance directions are G_i = {ℓ_i = m};
- the two-way band is B_i = {|ℓ_i| ≤ m/3};
- the additive half-circle is A_i = {ℓ_i ≥ 0}.

Angles are measured in the tangent basis (1,−1,0)/√2 (0°) and (1,1,−2)/√6 (90°). Towards e_1 is 30°, towards e_2 is 150°, towards e_3 is 270°. Values below are for ε = 0.3, from `t4_infinitesimal.py`, at 1° resolution.

| index p | F_1 (world 1 ineligible) | F_2 | F_3 | G_i (guidance) |
|---|---|---|---|---|
| (.5,.3,.2) generic | 324°–102° | 89°–224° | 198°–335° | none |
| (.9,.07,.03) near e_1 | 315°–78° | 88°–226° | 196°–337° | none |
| (.9,.05,.05) symmetric line | 311°–109° | 87°–226° | 194°–333° | world 1 at 210° only |
| (.35,.33,.32) near u | 327°–106° | 76°–214° | 204°–335° | none |
| u (one-sided from u) | 315°–105° | 75°–225° | 195°–345° | none |

**In words.**
- A world may accept a small displacement unless it heads within about ±70° of that world's own vertex, where the world improves by more than twice what it loses.
- Each two-way band B_i is two arcs of about 40° flanking A_i.
- Every direction lies in some F_i, so every small displacement is ineligible at some world. Adjacent F_j and F_k usually overlap, by up to 35°; there only the third world is eligible, and it is forced to accept. The overlap is empty only for F_1 and F_2 near e_1 off the symmetric line (§2.2).
- On the symmetric line near e_1, the direction away from e_1 (210°) is a pure world-1 worsening, which audit's §6 identified analytically. The direction towards e_1 is a pure world-1 improvement and lies deep inside F_1. This is the source of the diagnostic triple.

ε = 0.1 is qualitatively the same (`t4_infinitesimal_eps01.out`).

### 2.2 The shape lemma

Take a *direction-dependent* rule near p: for x and y near p, W(rec(C_x, C_y)) = W*(direction of y − x). Put S_i = {v : i ∈ W*(v)}. Say directions d_1, d_2, d_3 *span positively* if α_1d_1 + α_2d_2 + α_3d_3 = 0 for some α > 0.

**Lemma 4 (PROVED).**
- **(a)** (TC) at world i on small triangles holds iff S_i is *P-closed*: whenever d_1, d_2, d_3 ∈ S_i span positively, −d_1, −d_2, −d_3 ∈ S_i.
- **(b)** A closed P-closed set is either contained in a closed half-circle (*order type*) or symmetric, S_i = −S_i (*reciprocal type*). Conversely, both kinds are P-closed.

*Proof.*
- (a) For x, y = x + αd_1 and z = y + βd_2 with αd_1 + βd_2 + γd_3 = 0, (TC) on (x, y, z) requires the record x → z, whose direction is −d_3. Collinear triangles impose nothing, by a direct check of the two cases.
- (b) Suppose S is not in any closed half-circle and some d ∈ S has −d ∉ S. Then −d lies in a gap of S¹ ∖ S of length < π. The endpoints d_2 and d_3 of that gap lie in S, and −d is in the open cone they span. So d, d_2, d_3 span positively, and P-closedness puts −d in S, a contradiction. The converse is immediate. ∎

The other requirements become:
- coverage: ∪ S_i = S¹ (by Lemma 3, the only face obligation);
- undominatedness: ∩ S_i is symmetric;
- eligibility: S_i ⊆ E_i and G_i ⊆ S_i.

**Corollary 4.1 (PROVED).**
1. **Guidance forces order type.** If an exact guidance direction exists (G_i ≠ ∅), then S_i is of order type, because −G_i ⊆ F_i. This applies to world 1 on the symmetric line near e_1. (At generic points max_v ℓ_i/m reaches 1 at some worlds, so first-order guidance exists there, but no exact guidance at finite t. Nothing is forced by it.)
2. **Uniform sticky slack fails.** Let W_κ accept i iff ΔL_i ≥ −κM. If 0 < κ < max_v ℓ_i(v)/m(v), then S_i = {ℓ_i + κm ≥ 0} contains a closed half-circle with neighbourhoods of its endpoints, and it omits −v* for the maximiser v*. So it is neither type, and (TC) fails on a small triangle near p. The strict margins pass to finite t.
   - κ = 1/3 is the entire eligible pool, so the pool itself is not a (TC) allocation anywhere in the interior. The maximum ratio max_v ℓ_i/m is between 0.75 and 1 at the sample points.
   - CHECKED on the grids: 1,224–1,968 violations for κ = 1/3, and 21–102 for κ = 1/20. The only exception is the u grid at ε = 0.1, where the κ = 1/20 band happens to pass on the grid.
3. **Opposite orders.** If S_k = ∅ (world k accepts no small record; possible only if G_k = ∅), then S_i and S_j are complementary closed half-circles H and −H, with H ⊆ E_i and −H ⊆ E_j. Two subsets of closed half-circles cover S¹ only in this way.
   - This is PP4 Prop 3.2(b) transported to selected models: two worlds carry opposite total local orders.
   - The reciprocal branch of Prop 3.2(a) corresponds to reciprocal type here.
4. **Order type is locally an order.** If every S_i is of order type, S_i ⊆ H_i = {n_i·v ≥ 0}. Taking S_i = H_i works iff:
   - n_i ∈ N_i, the arc of normals whose open negative half-circle contains F_i (width π − |F_i| ≈ 40°); and
   - n_1, n_2, n_3 span positively, which gives coverage and makes ∩ S_i empty.

   The additive choice n_i = ∇ℓ_i is admissible iff dL(p) has a strictly positive normal λ (λ·dL = 0). NUMERICS: this holds at all 7,021 interior points of a 1/120 grid, with every component of λ at least 0.013 (normalised to sum 1). The smallest components occur near the edges.
   - Rotating n_i inside N_i is the only way a world can accept sticky small records (ℓ_i < 0). It costs refusals on the opposite side, which the other worlds must cover.

**NUMERICS (`t9_direction_sat.py`; 72 directions; exact first-order data).** I encoded eligibility, guidance, P-closedness, coverage and undominatedness as SAT.
- **SAT** at all 8 sample (p, ε).
- **Generic interior point, near u, and (.9, .051, .049) at ε = 0.1.** No world can be of reciprocal type or inactive: all three worlds must carry local orders.
- **Near e_1 off the symmetric line, (.9, .07, .03), both ε.** F_1 ∩ F_2 = ∅, and world 3 may be inactive or reciprocal. The other two then carry opposite orders.
- **(.9, .051, .049) at ε = 0.3.** The same holds with world 2.
- **Sticky directions.** Every sticky direction (7–12 per world) is acceptable in some solution.

### 2.3 Kinks, the vertex, edges

**Chamber boundaries and u.** On the symmetric lines p_j = p_k = min, and at u, ℓ is piecewise linear in v (dm = min(v_j, v_k), resp. min_j v_j).
- Small triangles that straddle the kink use two or three different linear maps. Lemma 4 applies only within a chamber.
- At u the reversal of a record uses the chamber map of the far endpoint. So "direction-dependent" is not a well-posed reduction at u. The grids handle these points directly.
- Audit's triple a, b, c straddles the kink on p_2 = p_3. Its two links are records from bases in different chambers.

**Edges (PROVED).** Let p lie on [e2,e3].
- On M_2 ∪ M_3 regular changes have Δr_2 = −Δr_3. On M_1 and on unanimous problems, D_p is already best for worlds 2 and 3.
- So ΔL_2 + ΔL_3 ≥ 0 for every rival (edge count). M_1 changes near p have mass O(t²), so ℓ_2 + ℓ_3 ≡ 0 to first order.
- Hence some inward direction is first-order neutral for both worlds 2 and 3. (AC) at edge points is a second-order effect: at the midpoint, ΔL_2 = ΔL_3 = 0.971t² (ε = 0.3) and 0.716t² (ε = 0.1), in 50-digit arithmetic (`t10_edge_second_order.py`).

**Proposition 2.1 ((AC) at boundary indices; PROVED).** If p ∈ ∂Δ, no q ≠ p has L(q) ≤ L(p).

*Proof.* Take p ∈ [e2,e3] (vertices follow as special cases). If L_2(q) ≤ L_2(p) and L_3(q) ≤ L_3(p), the edge count forces equality and no M_1 or unanimous changes. Then:
- if q is interior, C_q is silent on a non-null set of M_1 lines through K_q, and D_p is A there, a contradiction;
- if q is on another edge and is not e_2 or e_3, D_q is B on the non-null set of M_1 lines that separate q from e_2 (or e_3), a contradiction;
- if q ∈ [e2,e3], then ΔL_2 = −ΔL_3 ≠ 0, because θ(·, e_2) is strictly monotone along the edge. ∎

For the vertex e_1: L_1(e_1) = 0, and only C_{e_1} has world-1 rank 0 almost everywhere.

**Near e_1.** Up to K_p's size, the picture is scale-invariant: K_p has size 3ε min(p_2, p_3), comparable to the distance from the edges.
- As p approaches the edges, both the margin min_v max_i ℓ_i/m and the second-order margin shrink, but they stay positive.
- The fine local grid at e_1 (h = 1/4000) gives a ratio margin of 0.0235 (ε = 0.3) and 0.0148 (ε = 0.1). At (.9, .05, .05) the margin is 0.206 (ε = 0.3) and 0.222 (ε = 0.1).

---

## 3. Grids (Approach 2; CHECKED)

**Grids.**
- **e_1 grid:** p = (1 − (j+k)/50, j/50, k/50) with j + k ≤ 6 (28 indices, edges and e_1 included), plus audit's a, b, c: 31 indices.
- **u grid:** (20 + a, 20 + b, 20 − a − b)/60 with |a|, |b|, |a + b| ≤ 3: 37 indices, including u and the chamber boundaries.
- **Whole simplex:** the 1/6 lattice, 28 indices, including all vertices and edges.

Every ordered pair has an exact record, built from a rational arrangement of 9 planes with exact signs. Each record yields Φ, the guidance and strict-improvement flags, and the exact faces met by A(d), via LP on cell rays.

**Encoding (`t6_sat.py`).**
- Hard clauses: eligibility, guidance, every face clause, (TC) on every ordered triple at every world, undominatedness, and (IB) links.
- Closedness cannot be imposed on a finite grid.
- Every record has min |Φ_i| ≥ 5.9e-7 away from guidance, so no verdict is borderline.

| grid, ε | idx | vars | TC clauses | SAT | forced accept (all = face clause with one eligible world) | forced refuse | sticky eligible acceptable | ΔL_i > 0 refusable |
|---|---|---|---|---|---|---|---|---|
| e_1, .3 | 31 | 2,790 | 80,910 | yes | 146 | 0 | 299/299 | 1,094/1,240 |
| e_1, .1 | 31 | 2,790 | 80,910 | yes | 162 | 0 | 291/291 | 1,077/1,239 |
| u, .3 | 37 | 3,996 | 139,860 | yes | 210 | 0 | 438/438 | 1,774/1,984 |
| u, .1 | 37 | 3,996 | 139,860 | yes | 204 | 0 | 449/449 | 1,774/1,978 |
| all, .3 | 28 | 2,268 | 58,968 | yes | 123 | 0 | 208/208 | 770/893 |
| all, .1 | 28 | 2,268 | 58,968 | yes | 129 | 0 | 199/199 | 762/891 |

**Candidates.**
- **W_add:** 0 violations on all six grids, confirmed by an independent checker (`t8_verify.py`: matrix-product (TC), faces, dominance; it does not use the clause list).
- **Audit's greedy rule** (source as witness): 234 and 259 violations on the e_1 grid; 0 on the u and whole-simplex grids.
- **Bands κ = 1/3 and 1/20:** violations as in Cor. 4.1(2).
- **Strict 4-cycles** p ≺_i q ≺_i r ≺_i s ≺_i p are realizable in a full solution at every world on every grid (`t7_structure.py`, re-verified by `t8_verify.py`). The layer does not force acyclicity.

**Minimal cores, in plain English.**
1. **Greedy, e_1 grid, ε = 0.3 and 0.1. Core size 2 (deletion-minimal).** Put a′ = (.94, 0, .06), b′ = (.94, .04, .02), c′ = (.96, 0, .04).
   - Greedy has world 1 accept a′ → b′ (Φ = (.0069, −.0217, .0596), ΔL/M = (−.22, −.71, .70)) and b′ → c′ (Φ = (.0066, .0562, −.0040), ΔL/M = (−.19, .90, −.42)).
   - Both a′ and c′ are precise points on the edge [e1,e3], and c′ is nearer e_1. So C_{c′} is a pointwise world-1 improvement of C_{a′}: guidance forces c′ ⪯_1 a′, and strict (G) forbids a′ ⪯_1 c′. (TC) then forbids accepting both links at world 1.
   - This is audit's mechanism (two sticky world-1 links composing to a strict world-1 improvement), now sited on an edge.
   - **Repair available:** both links are sticky at world 1 (ΔL_1 < 0). The first is additively accepted at world 3 (ΔL_3/M = .70) and the second at world 2 (ΔL_2/M = .90). W_add makes exactly this reassignment, which is audit's suggested coordinated reassignment.
2. **Band κ = 1/20, e_1 grid. Core size 4 (a single TC clause).**
   - At world 1: (.88,.02,.10) → (.90,.10,0) → (.90,0,.10) → (.88,.02,.10).
   - All three links pass the slack test. The chord (.88,.02,.10) → (.90,0,.10) improves world 1 by more than κM.
   - This is Lemma 4's mechanism: the accepted set of directions is longer than a half-circle but not symmetric.
3. **The full problem has no core on any grid.** No UNSAT was found. Per the brief, this is not proof of satisfiability; the satisfiability claim rests on Theorem 5.

---

## 4. Conclusion (Approach 3)

**Theorem 5 (PROVED, conditional on (AC)).** W_add, i ∈ W(d) iff ν(P_i) ≥ ν(Q_i), satisfies every requirement of Task B.
1. **Eligibility and guidance.** a_i ≥ b_i gives Φ_i ≥ a_i ≥ 0. Guidance (b_i = 0) is accepted, and strict improvements (a_i = 0 < b_i) are refused.
2. **(TC).** Each world's relation is the total preorder by L_i, which is transitive. Guidance lies inside it.
3. **Closedness.** {(p,q) : L_i(p) ≤ L_i(q)} is closed, because L_i is continuous on Δ by Lemma 2.
4. **(IB).** The verdict is a function of the record (a_i, b_i).
5. **Faces.**
   - Interior sources: only W ≠ ∅ is required (Lemma 3), which is (AC).
   - Edge anchors r ∈ [e_i, e_j]: the record is the same from C_r, and the edge count gives ΔL_i + ΔL_j ≥ 0, so one of the two worlds accepts.
   - Vertex anchors: guidance.
6. **Undominated.** q dominates p iff L(q) ≤ L(p) with L(q) ≠ L(p), which (AC) excludes. Ties at every world require L(q) = L(p), and both models are coherent. ∎

Conversely, if (AC) fails at (p, q), W_add leaves C_p dominated. So W_add passes **iff** (AC) holds.

**(AC) status.**
- PROVED at every boundary index (Prop. 2.1).
- NUMERICS in the interior:
  - grids of 11,476 indices: min_{q≠p} max_i ΔL_i/|q − p| = 0.0110 (ε = 0.3), 0.0080 (ε = 0.1), 0.0293 (ε = 0.9);
  - fine local grids at e_1, (.9,.05,.05), u and an edge midpoint: all positive;
  - the local normal is strictly positive at all 7,021 interior points tested.
- Two simpler proofs are unavailable:
  - L(Δ) is not a convex surface: λ(p)·L is not minimised at p near u (t3);
  - L_i is not quasi-convex for ε = 0.3 or 0.9 (t5).
- CONJECTURE: (AC) holds for all 0 < ε < 1. A certificate needs second-order control near the edges, where the first-order margin vanishes (§2.3).

**Is the subproblem obstructed? No.** Where it bites:
- **Greedy rules fail through one local pattern.** Near e_1 and along the edges at e_1, two sticky world-1 links compose to a strict world-1 improvement, via edge points or the symmetric line. Whatever allocation is used must send such links to the other worlds, where they are additively sound.
- **Uniform stickiness fails everywhere** (Cor. 4.1(2)). This includes "accept the whole eligible pool".
- **Each world must be locally order-like.** At generic interior points and near u, each world's acceptances among nearby selected models must lie in a closed half-plane of displacement directions. No world can be reciprocal or inactive there (NUMERICS).
  - Stickiness is possible only by rotating a world's local order, by up to about ±20° away from ∇L_i.
  - Near e_1 the opposite-orders branch (PP4 Prop 3.2(b)) becomes available.

**What this means for the full construction (no new assumption).**
- This layer cannot discriminate, because the additive rule passes it. FF2 Thm 4.1 excludes that rule for the full (S), since C_p is not additively competitive against non-selected rivals.
- The needed non-additivity must therefore live in records from C_p to non-selected rivals (splices). Two routes are available:
  - **Stickiness toward rivals that additively dominate C_p.** By Lemma 1, some such record must be accepted with ΔL_i < 0.
  - **Non-integrable local orders.** Rotated local orders n_i(p) whose direction field is not a gradient. This is a type-(N2)-like source that this layer permits; it is untested.
- **Next necessary test: mixed triples (C_q, C_p, X).** Here W_add, or a rotated variant, holds between C_q and C_p, and a sticky acceptance holds from C_p to X. (TC) then requires C_q ⪯_i X whenever X ⪯_i C_q. If W_add on selected pairs is combined with the sticky rival records that Lemma 1 forces, the triangle C_q ⪯ C_p ⪯ X with X ⪯ C_q is where an obstruction would have to appear.
  - The present harness extends directly: add spliced rivals near each line, as PP3 requires.

---

## 5. Files (`PP6_py/`)

| script → output | content | label |
|---|---|---|
| `geom.py` | exact-rational arrangement, solid angles, records, anchor faces (LP), losses, exact record-identity test | library |
| `lfast.py`, `lmp.py` | perimeter formula (numpy; mpmath at 50 digits) | Lemma 2 |
| `grids.py` → `rec_*.pkl` | the six exact record tables | CHECKED |
| `t1_additive_scan.py` → `.out` | (AC) and normal signs on an 861-point grid | NUMERICS |
| `t2_antichain.py`, `t2b_antichain_local.py` → `.out` | (AC) margins, global and local fine grids | NUMERICS |
| `t3_convexity.py`, `t5_quasiconvex.py` → `.out` | failure of convexity and quasi-convexity routes | NUMERICS |
| `t4_infinitesimal.py` → `t4_infinitesimal_eps0{1,3}.out` | arcs F_i, G_i, B_i, A_i by direction | CHECKED (first order by t = 2e-4) |
| `t6_sat.py` → `.out` | grid SAT, candidates, backbone | CHECKED |
| `t7_structure.py` → `.out` | forced-acceptance causes, 4-cycles, greedy minimal core | CHECKED |
| `t8_verify.py` → `.out` | independent checker | CHECKED |
| `t9_direction_sat.py` → `.out` | infinitesimal (72-direction) SAT: types per world | NUMERICS |
| `t10_edge_second_order.py` → `.out` | second-order neutrality at edges, 50 digits | CHECKED |
