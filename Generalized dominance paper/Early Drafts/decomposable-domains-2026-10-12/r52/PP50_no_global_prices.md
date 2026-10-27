# PP50. No global prices: the four-posterior-model checkpoint, and what a continuum must do

23 October 2026. Task PP50 of Brief 52. One reader (me); not refereed.

**Labels.** PROVED: complete argument here, or a cited result. CHECKED: exact rational computation in `PP50_py/`; every such script ends ALL PASS. NUMERICS: a floating-point or MILP search that proposes something; no claim rests on it unless it is re-verified exactly. CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF52; AUDIT_round52, AUDIT_posterior_pairs and AUDIT_round52_answers (binding); PP42 (CG2, Thm 3.1, Thm 3.2, Prop 3.6); REFEREE_round50 (Thm R1, Lemma S); PP45 (Lemma 2.1, Lemma 2.3); PP46 (Lemma A0); PP47 (Lemma 1.3, Thm 4.1). Coordinator relays received during the task: PP49 (consolidated sufficiency, Theorem A; Theorem N; weak own-Bayes suffices; nearby triples are two-valued) and PP53 (an independent four-model certificate, the width budget, spectator constraints). I add no axioms. Extra hypotheses are named where they enter.

---

## 0. Verdict

1. **The checkpoint is met (Thm 2.1; CHECKED).** I take four nearby posterior models in a genuinely two-dimensional (convex) arrangement, with T among them:

     A = T,  B = C_(11,10,9.9),  C = C_(12,11,10),  D = C_(10,11,10.1).

   I give explicit fields, constant on each of the 30 realised advice types. All four models use the **uniform** supporting weight λ = u. The fields meet all four requirements:
   1. pointwise strict own-Bayes over all four advice values;
   2. nondegenerate CG2 intervals derived from the fields, for all 6 pairs at all 3 worlds;
   3. PP47 Thm 4.1 with strict slack for all 4 triples at all 3 worlds, so (TC) holds under zero-accepting gates;
   4. **no global constants at world 1.** Worlds 2 and 3 do have global constants.

   A gauge change (Lemma 1.2) turns the world-1 intervals into exactly the audit's pattern. In log₃ units, x_B − x_A, x_C − x_B, x_D − x_C and x_A − x_D are each forced to be at least 1, while both diagonal intervals contain [−10, 10].
2. **It persists all the way down to T (Thm 2.2; CHECKED).** The quadruple shrunk towards T by any factor t ∈ (0, 1] has the same 30 types, so **the same field table** works for every t. The cycle deficit stays fixed while the models converge to T.
3. **PP53's certificate is independently verified (§2.4; CHECKED).** My verifier finds PP53's realised types from the cells of the plane arrangement, not from the pair-ordering admissibility list, and gets the same 28 types. It confirms every claim: no global constants at worlds 1 and 2 (main certificate), or at world 1 (fixed-λ certificate). The two constructions agree on every structural feature.
4. **The proposed structural theorem ("own-Bayes plus CG2 force global prices") is false** for four models (Thm 2.1). So none of the three suspects (Bayes constraints, posterior geometry, universal acceptance) forces prices at this level. I prove instead what *does* restrict the phenomenon:
   - **(a) Orientation (Prop 3.1; PROVED).** A cycle can lack prices at world w only if, in one orientation, every edge X → Y has a disagreement at which Y's advice is worse at w. In the posterior family this fails exactly on edges that are **pure w-shifts**.
   - **(b) Witness rigidity (Prop 3.3; PROVED in the nearby regime; CHECKED).** For the natural transported fields λ_a = a, ℓ^a(h) − ℓ^a(S) = −h∘p (with p a credal witness), strict CG2 is impossible, and the only admissible constants are the posterior ratios. The escape therefore needs fields that are *not* of witness type.
5. **The continuous extension has a negative answer near T, for the posterior family in this architecture (§6; the decisive result).**
   - **PP51's kink certificate is independently confirmed** (CHECKED, `kink_check.out`, `kink_check_t10.out`). My code re-derives the cells, the two lone-answer cells, the forced orders and two-signedness, and I re-derive Thm 5.1's convexity argument.
   - **Theorem K (measure form; PROVED, with an exact box certificate).** At ε = 3/10, the kink is stable under moving its base point, perturbing its shape, and shrinking it by any factor in (0, 1/5]. This is certified uniformly on a box by an exact Descartes and coefficient-bound test (`kink_box.out`). Consequently:
     - every set G of gated posterior indices (own-Bayes gates, strict CG2, the closed triple test) meets a fixed neighbourhood U₀ of u in a **Lebesgue-null set**;
     - every selected non-perfect model must be gated (PP45 Lemma 2.3(b)), so **no selection whose image has positive measure near T is realisable**. In particular index = likelihood near T is not realisable, and neither is any 2-D patch, sector or positive-measure family through T;
     - this settles PP51's scale-invariance conjecture at u, in a stronger form.
   - **Kink-free gated families near T are therefore null.** Lines and tripods, which are kink-free by PP51, are examples. A 2-D index neighbourhood must be selected *onto* such a null set, as in PP45's tripod map.
   - **Source of the obstruction.** It is the posterior family's *wedge* answer regions near the corner rays of T's cone. They meet the closed triple test that the union architecture makes exact (Thm R1, PP47 Thm 4.1), and own-Bayes with triple-common constants (Lemma 6.1: every cell must be separable by a pattern-orthant plane in effective-weight space). So the culprit is **architecture plus posterior geometry**, not the axioms. Selective (non-union) acceptance, or a family with half-plane answer regions (PP51 §5.3(b)), escapes the hypotheses.
6. **Regular continua in general (§4), for families with half-plane answer regions** such as PP51's proposed adjusted family. These are rigidity theorems for any 2-parameter patch of gated members whose fields are continuous in the index on each side of each member's own threshold (J), with continuous weights (Λ):
   - **Thm 4.1 (PROVED).** (TC) forces every *threshold jump* to be humble at every world.
   - **Thm 4.2 (PROVED).** Own-Bayes then forces all those jumps to vanish: every member is exactly indifferent at its own threshold. The checkpoint fields, mine and PP53's, are not restrictions of such a continuum. Side-profile continua cannot have strict CG2 (Cor 4.3).
   - **Thm 4.4 (PROVED under (J1)).** Intervals of nearby pairs collapse at first order onto a local price 1-form ζ.
   - So missing global prices in a regular continuum is a second-order (curvature) or finite-scale effect (Prop 4.5). The mechanism to try in a kink-free family is **depth-layered fields** (§4.4; CONJECTURE). That conjecture is **withdrawn for the posterior family near T** by Theorem K.
7. **Boundary behaviour (§5).**
   - Edges pointing at a vertex v are one-signed at v.
   - On the face {a_w = 0}, the forced weight support λ_w = 0 frees the world-w fields from Bayes, so Thm 4.2's squeeze does not act at world w there.
   - Near T, deficient four-model cycles exist at every scale (Thm 2.2), but kinks also exist at every scale (Theorem K). Any gated family near T must be null and kink-free.

| Item | Result | Label |
|---|---|---|
| Finite type reduction; gauge | Lemmas 1.1, 1.2 | PROVED |
| Four-model checkpoint, λ = u, no prices at world 1 | Thm 2.1 | CHECKED |
| Audit pattern via gauge | Cor 2.1′ | CHECKED |
| Same table for the whole shrinking family t ∈ (0, 1] | Thm 2.2 | CHECKED (exact oriented-matroid test) |
| PP53 certificate | §2.4 | CHECKED independently |
| Orientation condition; pure-shift edges | Prop 3.1, Cor 3.2 | PROVED; CHECKED (square) |
| Witness fields are rigid | Prop 3.3 | PROVED (nearby regime); CHECKED (grid class) |
| Humble jumps; vanishing jumps; side-profile continua fail strict CG2 | Thms 4.1, 4.2, Cor 4.3 | PROVED under (J), (Λ) |
| First-order collapse onto a 1-form ζ | Thm 4.4 | PROVED under (J1), (Λ) |
| Local exactness does not propagate | Prop 4.5 | PROVED |
| Depth-layered continuum | §4.4 | CONJECTURE (kink-free families only; withdrawn for posterior near T) |
| 3×3 grid refinement | §4.5 | NUMERICS (inconclusive) |
| PP51 kink certificate | §6.1 | CHECKED independently; argument re-proved |
| Exact triple reduction (effective-weight separability) | Lemma 6.1 | PROVED |
| Kink stable on a box × scales (0, 1/5] | Prop 6.2 | CHECKED (exact) |
| Gated posterior sets are null near u; no positive-measure selection near T | Thm K | PROVED |

---

## 1. Reduction to a finite problem

**Setting.** This is Brief 52's: three worlds, Gaussian μ, the four-advice domain, ranks 0 < 1 < 2 < 3, ε = 3/10, T = D_M, and the posterior family C_a = D_{M_a}. C_a accepts h iff (m_j∘a)·h > 0 for j = 1, 2, 3.

**Types.** For finitely many gated models, the advice of every model and the sign pattern of h are constant on each open cell of the central plane arrangement {n·g = 0}, n ∈ {m_j∘a_N} ∪ {e_1, e_2, e_3}. At a disagreement cell, normalise the answer to +h. The **type** is τ = (𝓗, 𝓢, Wr): the models answering h, the silent models, and the worlds where h is wrong. If the credal sets pairwise intersect, no cell carries both h and −h (PP49 Lemma 1.2), so the family is two-valued.

**Fields on a type.** On the cone of τ put ℓ^N_v(g, h) − ℓ^N_v(g, S) = ±m^N_v(τ)|g|₁, with + iff v ∈ Wr, and m^N_v(τ) > 0 constant. The values for −h and for contradiction are completed as in PP45 with a large constant K, so the field is strictly guiding and both are strictly worse than S.

For N's own advice, write the strict Bayes inequality at λ^N:
- answering models: Σ_{Wr} λ^N_v m^N_v < Σ_{Rt} λ^N_v m^N_v;
- silent models: the reverse.

**Intervals.** At world v, for κ_XY := c_X/c_Y:

  I_XY(v) = [ max_{τ: X errs at v} m^Y_v/m^X_v ,  min_{τ: Y errs at v} m^Y_v/m^X_v ]   (over τ in D_XY).

Here "X errs at v" means X's advice is the worse one at v.

**Lemma 1.1 (finite reduction; PROVED).** Suppose the following hold for a finite gated family with pairwise-intersecting credal sets and fields of the form above:
- (i) the strict Bayes inequalities hold at every type;
- (ii) every I_XY(v) that is bounded on both sides has lo < hi;
- (iii) for every triple and world, ∏ lo < 1 < ∏ hi around the triangle in both orientations.

Then the family satisfies (H0)–(H3) of PP49 on its own index set: strictly guiding integrable fields, strict own-Bayes, strict CG2 with positive constants, and (TC) under zero-accepting gates. Global constants exist at world v iff no cycle has ∏ hi < 1.

*Proof.*
- Integrability and (BR): magnitudes are finitely many positive constants times |g|.
- Own-Bayes off the disagreement cells: each model's advice is coherent, so magnitudes concentrated on the worlds where it is better make it optimal.
- Strict CG2: (ii), with constants strictly inside each interval, gives strict inequalities a.e.
- (TC): (iii) is PP47 Thm 4.1(a) with slack, so no triple is tight and (b) is vacuous. Thm 4.1 is exact for two-valued families under (R0), (BR) and strict CG2 (PP49 Lemma 3.4(iii)).
- The last sentence: difference constraints on finitely many nodes are infeasible iff some cycle has negative total. ∎

**Lemma 1.2 (gauge; PROVED).** Replace N's world-w field by t_N·ℓ^N_w and λ^N_w by λ^N_w/t_N (then renormalise λ^N). This leaves every Bayes comparison unchanged and multiplies every world-w interval I_XY(w) by t_Y/t_X. Cycle products of interval endpoints are gauge-invariant.

So λ = u can always be assumed for interior weights, and only the **cycle deficit** ∏_cycle hi carries information.

*Proof.* λ^N_w·ℓ^N_w is unchanged, and ratios m^Y/m^X pick up t_Y/t_X. ∎

---

## 2. The checkpoint

### 2.1 The construction

Models (unnormalised likelihoods): A = (1, 1, 1) = T, B = (11/10, 1, 99/100), C = (12/10, 11/10, 1), D = (1, 11/10, 101/100). In log-likelihood coordinates, ABCD is a convex quadrilateral in cyclic order with T at a corner, and no edge is a pure shift (§3).

There are **30 realised disagreement types**, and no three-valued cell. The exact enumeration of arrangement cells is cross-checked by 200,000 random problems (`explore_types.out`, `rand_check_types.py`).

The field table (`checkpoint_fields.json`) has m^N_v(τ) = 3^{y^N_v(τ)} with integer exponents in [−20, 9], and λ = u for all four models. It has a transparent **side-profile** form, y^N_v(τ) = Φ^N_v + J_v(τ, side of N): one profile per side of the split, and one world scale per model.

**Theorem 2.1 (CHECKED, `verify_exact.out`).** With these fields:
- (V1) the 30 types are exactly the realised ones, and the family is two-valued;
- (V2) all 360 strict own-Bayes comparisons hold over all four advice values, including the completed −h and contradiction values. The agreement cells are handled separately;
- (V3) every interval is nondegenerate;
- (V4) the strict triple test holds for all 4 triples × 3 worlds × 2 orientations;
- (V5) world 1 admits no global constants, and worlds 2 and 3 do.

Derived intervals for log₃ κ_XY = x_X − x_Y:

| pair | world 1 | world 2 | world 3 |
|---|---|---|---|
| AB | [3, 8] | [−1, 1] | [−5, −3] |
| AC | [4, 9] | [0, 2] | [−12, −10] |
| AD | [−7, −6] | [4, 6] | [−4, −2] |
| BC | [−3, −2] | [0, 2] | [−8, −6] |
| BD | [−18, −13] | [4, 6] | [0, 2] |
| CD | [−19, −14] | [3, 5] | [7, 9] |

At world 1, around A → B → C → D → A, the upper bounds of x_A − x_B, x_B − x_C, x_C − x_D and x_D − x_A are 8, −2, −14 and 7. They sum to **−1**, so no global constants exist. Every triangle has slack. For example, in ABC, x_A − x_C must lie in [3, 8] + [−3, −2] = [0, 6] and also in [4, 9]; the overlap is [4, 6].

**Corollary 2.1′ (the audit's pattern; CHECKED, `gauge_pattern.out`, `verify_exact_gauged.out`).** Multiply all exponents by 4 and apply the gauge φ = (0, −33, −26, 29) on world 1. The weights become λ^N ∝ (3^{−φ_N}, 1, 1), which are interior. World-1 intervals for x_X − x_Y become:
- AB [−21, −1];
- BC [−5, −1];
- CD [−21, −1];
- AD [1, 5];
- diagonals AC and BD: [−10, 10].

So x_B − x_A ≥ 1, x_C − x_B ≥ 1, x_D − x_C ≥ 1 and x_A − x_D ≥ 1, with both diagonals free in [−10, 10]. This is the audit's abstract pattern, realised by actual fields, advice changes and Bayes conditions. Re-verified: ALL PASS.

### 2.2 How it works: pins on own-error discounts

For each cycle edge X → Y, one **pin type** supplies the decisive upper bound: a cell where Y's advice is worse at world 1. At three of the four pins, Y's world-1 penalty is set well below X's. That is an *own-error discount*, and it helps the Bayes inequality of both models.

The pin for B → C has type 𝓗 = {B}, 𝓢 = {A, C, D}, Wr = {2, 3}, so h is right only at world 1:
- y^B = (1, 0, 0): B answers h, since 3 > 1 + 1;
- y^C = (−1, 0, −8): C stays silent on world 2's strength, since 1 + 3^{−8} > 1/3;
- the world-1 ratio m^C_1/m^B_1 = 3^{−2} gives hi_BC = −2.

The pins C → D and D → A work the same way, with jump e₁ = −3.

The pin for A → B instead uses a **humble** world-1 jump, e₁ = +8. The large upper bound it pays (8) is what keeps triangles ABC and ABD feasible. The diagonals absorb the rest: their intervals are wide because every type separating A from C, or B from D, is humble at world 1.

The Bayes cost of the humble types is paid by the model scales Φ^N_v. These are effective weights, and in tropical terms they decide which world dominates each model's Bayes sum. **Nothing in the posterior geometry ties a pin to the other pairs it touches**, beyond the per-type pair conditions of PP45 Lemma 2.1.

### 2.3 The checkpoint survives shrinking towards T

**Theorem 2.2 (CHECKED, `scale_matroid.out`, `scale_check.out`).** Put a_N(t) := 1 + t(a_N − 1) for t ∈ (0, 1]. All 455 determinants of triples of the 15 plane normals are cubic polynomials in t. None vanishes identically, and none has a root in (0, 1] (Descartes' rule after t = 1/(1 + x), with p(1) ≠ 0). So the oriented matroid, the cells and the type set are constant on (0, 1]. Since Lemma 1.1's conditions depend only on the type table, **checkpoint_fields.json works for every t**. `scale_check` re-runs the full verifier at t ∈ {1, 1/2, 1/4, 1/10, 1/100, 1/1000}: ALL PASS every time.

The models converge to T, while the world-1 deficit stays at 3^{−1}. With λ = u and one common field (say ℓ^T) on all agreement cells, the fields converge to ℓ^T in L¹, because the disagreement cells shrink. The selection converges to T, as PP47 Cor 2.3 requires. So a deficient cycle can sit **arbitrarily close to T**, at a fixed deficit. §4 explains why this is a fact about isolated quadruples and not about a regular continuum.

### 2.4 Independent verification of PP53's certificate

`convert_pp53.py` reads both PP53 solutions (P = acceptors, R = correct worlds; magnitudes taken as the exact binary values of exp(φ), as PP53 does). It converts them to my table format and runs my verifier unchanged. That verifier recomputes the realised types from the arrangement cells, independently of PP53's pair-ordering admissibility list.

**Result (CHECKED, `convert_pp53.out`).** Both certificates realise exactly 28 types, are two-valued, and pass (V2)–(V4).
- Main certificate: no global constants at worlds 1 and 2; constants exist at world 3.
- λ = index certificate: no global constants at world 1 only.

The world-1 cycle product is e^{−0.2} = 0.8187, as PP53 states.

**Agreement.** Both constructions are type-wise constant, use pins on own-error discounts, keep wide diagonals, and are scale-free. Mine uses λ = u, integer powers of 3, and a different quadrilateral.

---

## 3. What does, and does not, restrict the phenomenon

**Proposition 3.1 (orientation; PROVED).** Suppose a k-cycle lacks global constants at w. Then, in one orientation, every edge X → Y has a disagreement type at which Y errs at w.

*Proof.* Infeasibility of difference constraints is witnessed by a cycle of finite upper bounds. An upper bound on x_X − x_Y at w comes only from Y-err types. ∎

**Corollary 3.2 (pure shifts; PROVED; CHECKED).** Let b/a have r_u = r_{u′} ≤ r_w, where r = b/a: a pure shift towards world w. Then C_b's advice is never worse at w than C_a's. By the pair-ordering theorem a W ∋ w needs min_W r < max_R r, which fails for every W ∋ w. So such an edge can enter a deficient cycle only in the orientation from b to a.

In the "square" configuration A, (1.1, 1, 1), (1.1, 1.1, 1), (1, 1.1, 1), the edges AB and DC are pure world-1 shifts in opposite orientations. The MILP reports no Y-err type at world 1 for either orientation. Worlds 1 and 2 are therefore excluded, and world 3 is feasible (`milp_search.out`).

**Proposition 3.3 (witness fields are rigid; PROVED in the nearby regime; CHECKED).** Consider **witness fields**: λ_N = a_N and ℓ^N_v(g, h) − ℓ^N_v(g, S) = −h_v p_v(g, N), with p(g, N) ∈ M; when N is silent, p(g, N) must lie in W_N(g) = {p ∈ M : (a_N∘p)·h < 0}.

These are the natural transported fields. Bayes is automatic for every index, because λ_N·(ℓ(h) − ℓ(S)) = −(a_N∘p)·h. But for nearby interior X ≠ Y, strict CG2 fails at some world, and the only admissible constants are κ = 1, the posterior ratios.

*Proof.*
1. **The setting.** In the nearby (facet) regime, h-sayers form a half-plane of indices whose normal ω sweeps every direction. The half-circle of directions where X is ahead of Y meets open parts of two A-sectors, A_i and A_j.
2. **The witness is forced.** At a problem just inside Y's silence near facet i, W_Y(g) shrinks to the binding vertex. So p(g, Y) → m_i, and p_i(Y) → c + ε ≥ p_i(X).
3. **The lower bound.** There h is wrong at i, and X answers h, so X errs at i. This forces lo_XY(i) ≥ 0.
4. **The upper bound.** Near Y's threshold in the A_j part of facet j, p(g, Y) → m_j, so p_i(Y) → c ≤ p_i(X). There h is right at i, and the silent Y errs, which forces hi_XY(i) ≤ 0.
5. **Conclusion.** lo ≥ 0 ≥ hi. ∎

CHECKED (`witness_probe.out`): for the checkpoint models, with witnesses on an exact grid of M, the witness class admits CG2 intervals only with zero width. With margin 10⁻³ it is infeasible even when no cycle is demanded; with margin 0 it is feasible.

*Reading.* Prop 3.3 is the precise form of the intuition that "posterior geometry forces prices". It is true for fields whose Bayes margins are delivered by a credal witness. It is false in general (Thm 2.1), because general fields can price worlds far outside the ratio range of M. The checkpoint's ratios reach 3^{±20}.

**The deficit budget.** If a cycle has ∏ hi = e^{−Γ}, each diagonal interval must have width at least Γ, by the two triangles containing it. This is PP53's width budget (Lemma 3.4) restricted to the cycle itself. In Thm 2.1, Γ = log 3 and the diagonal widths are 5 log 3 and 5 log 3.

---

## 4. The continuum

**Scope.** By Theorem K (§6), no posterior patch near T can be gated at all. This section is therefore about the route left open by PP51 §5.3(b): 2-parameter families of coherent models whose answer regions are **half-planes in index space** (hypothesis (L) below). The posterior family satisfies (L) only near facets, and that is all the proofs use. The theorems tell such a family what its fields must look like.

Let 𝒫 be an open 2-parameter patch of gated members, with fields f^N. Write F_v(g, N) := log m^N_v(g) for the log gap between h and S at problems where N's credal set is near-binding at one facet (the linear regime). There, the h-sayers at g form a half-plane {N : ω·N > s}, bounded by the threshold line L_g.

**Hypotheses.**
- **(L)** On a non-null set of problems with normals ω in every direction, the h-sayers of 𝒫 form a half-plane {N : ω·N > s}. The family is two-valued on 𝒫.
- **(J)** For a.e. disagreement problem g, N ↦ F_v(g, N) extends continuously from each side of L_g up to L_g, locally uniformly in (g, N). The **threshold jump** is j_v(g, N₀) := F_v(err side) − F_v(right side) at N₀ ∈ L_g.
- **(Λ)** N ↦ λ_N is continuous and interior.
- **(J1)** (J) together with ∇_N F_v continuous on each closed side, jointly in (g, N).

These are regularity choices, not axioms. (S2) asks only for L¹-continuity, which (J) implies (with an envelope) but does not require.

**Theorem 4.1 (TC forces humble jumps; PROVED).** Under (J) and two-valuedness, j_v ≥ 0 at every world v, at every point of the threshold set.

*Proof.*
1. **A negative neighbourhood.** Suppose j_v(g₁, N₀) < −2η. By (J), j_v < −η on a neighbourhood: normals in an arc of width α > 0, and lines and crossing points near (g₁, N₀).
2. **Pins.** A pair X → Y straddling such a line, with Y on the side erring at v, has ρ = F_v(g, Y) − F_v(g, X) = j_v + o(1). This happens iff d·ω̃ < 0, where d = Y − X and ω̃ = sign(ω_v)ω. So hi_XY(v) ≤ −η + o(1).
3. **The directions.** The directions d pinned by some normal in the arc form an open arc of length 180° + α. It contains three directions that positively span the plane.
4. **The triangle.** A tiny triangle near N₀ with these edge directions has all three edges crossed by such lines, in the cycle orientation. So Σ log hi ≤ −3η + o(1) < 0.
5. **Conclusion.** The closed cycle test fails. For a two-valued triple with (BR) that test is necessary for (TC) (Thm R1; PP47 Thm 4.1(a)). ∎

**Theorem 4.2 (threshold indifference; PROVED).** Under (J), (Λ), own-Bayes and (TC), j_v(g, N₀) = 0 at every world, and N₀ is exactly indifferent between h and S at g, under both one-sided fields.

*Proof.* Let X → N₀ from the answering side and Y → N₀ from the silent side. By (J), (Λ) and a countable dense set of approximants, the weak Bayes inequalities pass to the limit. Write λ = λ_{N₀} and y^h, y^S for the one-sided limits.

Theorem 4.1 gives y^S ≤ y^h on Wr and y^S ≥ y^h on Rt. Hence

  Σ_{Wr} λ e^{y^S} ≤ Σ_{Wr} λ e^{y^h} ≤ Σ_{Rt} λ e^{y^h} ≤ Σ_{Rt} λ e^{y^S} ≤ Σ_{Wr} λ e^{y^S}.

All of these are equalities. With λ interior, y^h = y^S at every world. ∎

**Corollary 4.3 (PROVED).**
- (a) In such a continuum, own-Bayes margins vanish at each member's own threshold, so strict pointwise Bayes is impossible there. Weak Bayes, which PP49 shows suffices, is what survives.
- (b) The checkpoint fields of Thm 2.1, and PP53's, jump at the members' own thresholds. So they are not the restriction of any patch satisfying (J) and (Λ).
- (c) Suppose a patch uses **side-profile fields**, F_v(g, N) = Φ_v(N) + J_v(g, side), with Φ continuous. Then every ratio across a split equals Φ_v(Y) − Φ_v(X), so every CG2 interval is a single point and strict CG2 fails. This settles negatively PP46's open question of "open two-sided intervals with continuous designs", for this class.

**Theorem 4.4 (first-order collapse; PROVED under (J1), (Λ)).** For every X ∈ 𝒫 and direction d, the world-v interval for (X, X + td) has width o(t) and centre t c_v(X; d) + o(t). Here c_v(X; d) is the derivative of F_v(g_d, ·) at X along d, where g_d is the problem whose threshold line passes through X in direction d. Moreover c_v(X; ·) is linear:

  k_{X, X+td}(v) = t ζ_v(X)·d + o(t), with ζ_v a 1-form on 𝒫.

*Proof.*
1. **Values near the boundary direction.** A line g with normal ω near ω_d (ω_d ⊥ d) crosses the segment at a fraction θ of its length. Since the jump is zero (Thm 4.2), ρ/t lies in conv{∇F^h·d, ∇F^S·d} + o(1). Lines on the two sides of ω_d have the same sign of ω_v and opposite signs of ω·d: one side is X-err, the other Y-err.
2. **Collapse.** Both sides attain values near the whole segment conv{…} at g_d. Nonemptiness of the interval forces that segment to be a point, the tangential derivative, so the width is o(t).
3. **Linearity.** TC on tiny triangles t d₁, t d₂, t d₃ with Σ d_i = 0 gives Σ c(X; d_i) = 0. Together with homogeneity and c(−d) = −c(d), this makes c(X; ·) additive, hence linear. ∎

So a regular continuum is **locally priced at first order**, by ζ. Small cycles have deficit O(r²): curvature of ζ against second-order widths.

**Proposition 4.5 (local exactness does not propagate; PROVED).** In any gated family, (TC) on a triangle (X, Y, Z) says only that I_XZ meets I_XY + I_YZ. Along a chain X = N₀, N₁, …, N_n = Z with I_{N_{k−1}N_k} ≈ {0}, it says that I_{XN_k} meets I_{XN_{k−1}} up to o(1), for each k. That allows far-pair intervals to drift. So a 4-cycle of far members can be deficient while every short pair is locally exact.

*Proof.* The closed cycle test for a triple is exactly the intersection statement; nothing else links the triple. ∎

### 4.4 The proposed continuous mechanism for kink-free families: depth-layered fields (CONJECTURE)

**Status.** For the posterior family near T this conjecture is **false**: Theorem K excludes every gated posterior patch, whatever the fields. It is stated for families satisfying (L) everywhere, which are kink-free because their answer regions are never wedges.

Theorems 4.1–4.4 say exactly what such a continuum must look like. The checkpoint's type structure is transported from the members' own thresholds to **fixed depths**:

  F_v(g, N) = Φ_v(N) + P_v(g, δ(g, N)), where δ(g, N) := ω·N − s is the signed depth of N from L_g.

Here P_v(g, ·) is continuous at δ = 0, with h and S tied at δ = 0 for N's own weights (Thm 4.2). P_v may jump at finitely many depths ±δ_k. Those jumps are harmless in L¹, since for each N the set of g at which N sits exactly at depth δ_k is null.

For a pair at separation comparable to δ_k, the CG2 ratios P_v(g, δ_Y) − P_v(g, δ_X) sample the layers. Those layers play the part of the checkpoint's "types". Close pairs see only the continuous core, so they are locally exact, as Thm 4.4 requires. Far pairs straddle layers and can carry the deficient pins, as Prop 4.5 permits.

**CONJECTURE 4.6.** For a coherent 2-parameter family through T satisfying (L) (half-plane answer regions), there are δ₁ > 0 and depth-layered fields on a neighbourhood of T, with the following properties:
- weakly own-Bayes, strictly at every depth ≠ 0;
- strict CG2 for all pairs;
- (TC) for all triples, with the spectator constraints of PP53 holding vacuously, since the patch is two-valued;
- L¹-continuous, as Lemma S needs;
- some 4-cycle at separation ≈ δ₁ has no global constants at world 1.

What must still be checked is exactly the following:
- (i) Bayes for every member at every depth, which is a separation condition on the effective weights e^{Φ(N)} along each line;
- (ii) the width budget: every member F must have widths to the deficient cycle summing to at least Γ. By Thm 4.4 that is impossible for F near a cycle vertex unless the other three pairs are wide, which far pairs in the layer regime can be;
- (iii) the triangle test for triples straddling different layers.

**Two further PROVED negatives, which delimit the conjecture.**
- Witness-type cores (Prop 3.3) and side-profile cores (Cor 4.3(c)) cannot be used.
- Translation-invariant designs, with P independent of the offset s and Φ the same at every world, give intervals centred at ζ = 0 to first order. That contradicts the pair-ordering requirement of PP45 Lemma 2.1, which needs θ to have the order of Δ. So Φ must carry the posterior tilt world by world, and P must depend on position.

### 4.5 Discrete refinement test (NUMERICS)

A 3 × 3 grid of nine posterior models spanning the checkpoint quadrilateral has 101 types and is two-valued (CHECKED). I demanded a deficient corner 4-cycle at world 1.
- Under the side-profile ansatz, with humble fields at worlds 2 and 3, the MILP is **infeasible**.
- The general type-wise MILP is **also infeasible** (`grid3_free.log`).

Both searches impose Bayes in the sufficient dominant-world form, so infeasibility is **inconclusive**. PP51 §6 makes the same point about this relaxation. The grid carries **no** PP51 kink certificate on any of its 84 triples (`kink_scan_grid3.out`, CHECKED). Whether nine-member refinements of a deficient quadrilateral admit (TC) together with a deficient corner cycle is OPEN.

---

## 5. Boundary behaviour

1. **Pure-shift edges (Cor 3.2).** Along a direction pointing straight at vertex v (r_u = r_{u′} < r_v), every pair is one-signed at v. Such edges cannot carry a world-v pin in that orientation. Near vertex v, the members are separated almost purely along these directions, so world-v pins become scarce. The vertex gate V_v is exempt at v (PP49 Lemma 3.1).
2. **The face {a_w = 0}.** The weight support is forced, λ_w = 0 (PP49 (H1); PP53 "support equality is forced"). So world-w fields of face members are free of Bayes (PP42 Prop 3.6). Theorem 4.2's chain then does not act at world w: jumps there need only be humble (Thm 4.1). The other two worlds are still squeezed.

   Prices at world w are therefore cheapest to break **on or near the edge opposite vertex w**. Breaking them there is constrained only by Thm 4.1 and the triangle test. This is the natural place to put Theorem N's deficient world (CONJECTURE: a deficient world-w cycle can be placed in a collar of that edge).
3. **Approaching T.** There are two competing scale-free facts at u:
   - deficient four-model cycles exist at every scale, with one field table and fields converging to ℓ^T in L¹ (Thm 2.2);
   - kink triples exist at every scale, uniformly near u (Prop 6.2).

   So a gated family near T must be a **null, kink-free** set, such as PP51's lines and tripods. A deficient cycle can sit inside such a set only if the set contains four points in a two-dimensional (non-collinear) arrangement. Whether a kink-free null set through T can contain the checkpoint pattern **and** be defended under the selection is the remaining question (§6.4).

   In a (J)-regular family satisfying (L), the deficit of cycles of size r around T comes either from ζ's curvature, so it is O(r²), or from layers at a fixed depth δ₁, so it is absent below scale δ₁.
4. **Compactness of realisers.** In the depth-layered mechanism, realisers are the members themselves, indexed by a compact parameter set, as in Lemma S. The finitely many layer depths make (S2) a matter of dominated convergence. This is untested.

---

## 6. The kink obstruction: independent check, and the measure theorem

### 6.1 The exact triple reduction

**Lemma 6.1 (PROVED).** Let (X, Y, Z) be a two-valued triple of gated models. The triple admits own-Bayes fields (weak, or strict as required) and constants passing the closed triple test at every world **iff** there are effective weights ν^N ∈ (0, ∞)³ with the following property. For every realised type (𝓗, 𝓢, Wr), there is w in the open orthant O_s (w_v > 0 on Wr, w_v < 0 off Wr) with ν^H·w ≤ 0 for all H ∈ 𝓗 and ν^Q·w ≥ 0 for all Q ∈ 𝓢, with strict inequality where Bayes is strict.

*Proof.*
1. **(⇒) Substitution.** Let c^N_v be the triple's common constants at world v. Put m̃^N_v := c^N_v m^N_v and ν^N_v := λ^N_v / c^N_v. Closed CG2 with these constants says the erring side's m̃ is at least the right side's, at every world, for every cross pair.
2. **(⇒) One common vector.** On a type, let ẑ be min over H of m̃^H on Wr and max over H of m̃^H off Wr. Every H still satisfies its Bayes inequality with ẑ in place of m̃^H, because only terms that help H changed. Every Q satisfies its inequality with ẑ, because humility puts m̃^Q below ẑ on Wr and above ẑ off Wr. Then w := s∘ẑ works.
3. **(⇐)** Set every model's field on the type equal to |w|/c, with constants c ≡ 1. ∎

PP51's Lemma 2.3 and Thm 5.1 are statements about this reduction. Theorem 5.1's proof is a two-cell convexity argument in the coordinates z^N = (ν^N_j/ν^N_i, ν^N_k/ν^N_i). I re-derived it line by line, including the "silent alone" variant, which needs strictness at one inequality. It is correct as stated.

### 6.2 Independent check of the instance (CHECKED, `kink_check.out`, `kink_check_t10.out`)

For A = u, B = (406, 421, 373)/1200, D = (406, 373, 421)/1200 at ε = 3/10, my arrangement code (not PP51's) finds the following:
- 18 disagreement cells, all two-valued;
- **(K1)** a cell where A alone answers with Wr = {1}, and one where A alone answers with Wr = {2, 3};
- **(K2)** the worse-sets of (A, B) are {1}, {1, 3}, {2, 3}, {3}, whose only admissible order of log(ν^A/ν^B) is 3 > 1 > 2. Those of (A, D) are {1}, {1, 2}, {2}, {2, 3}, whose only admissible order of log(ν^A/ν^D) is 2 > 1 > 3. No tied vector is admissible;
- **(K3)** every pair is two-signed at every world.

Together these give z^B_2 ≥ z^A_2 ≥ z^D_2, and Thm 5.1 applies. The same certificate holds at scale t = 1/10. The full certificate search over all odd models, lone worlds, coordinates and modes (`kink_scan_grid.py`) recovers it as (A, i = 1, j = 2, answering). On my checkpoint quadruple it finds no kink.

### 6.3 Stability, and the measure theorem

**Proposition 6.2 (CHECKED, `kink_box.out`, exact).** Use the chart a ↦ (a₁/a₃ − 1, a₂/a₃ − 1). Let the base be a₀ = (1 + x₁, 1 + x₂, 1), with shape perturbations p, q ∈ R² and scale s ∈ (0, 1/5]. Put

  A = a₀,  B = a₀∘(1 + s(β + p − 1)),  D = a₀∘(1 + s(δ + q − 1)),

with β = 3(406, 421, 373)/1200 and δ = 3(406, 373, 421)/1200. For |x|, |p|, |q| ≤ 10⁻⁵, every such triple carries the kink certificate.

*Method.* There are 220 determinants of triples of the 12 plane normals. Each is a polynomial in (x, p, q, s). After s = (1/5)·τ and τ = 1/(1 + X), each Descartes coefficient (in X) is bounded away from 0 on the box by an exact coefficient-sum bound, and the signs show no change at the centre. So no determinant vanishes on the box × (0, 1/5]. The oriented matroid, the cells and the certificate are therefore those of the checked instance at s = 1/10.

A caution: at the centre, one determinant changes sign at s = 400/1259, so the range must stop below that. PP51's instance at s = 1 has a different cell structure, but it is also a kink.

**Theorem K (PROVED).** Use ε = 3/10 and the gate-union architecture: own-Bayes gates, strict CG2 a.e. for every gated pair, and the closed triple test at every world for every gated triple, as (TC) requires. Let U₀ = {|x| < 10⁻⁵}. Then:
- (a) every set G of gated posterior indices has |G ∩ U₀| = 0 (Lebesgue measure in the chart);
- (b) every selected model that is not perfect at some world is gated (PP45 Lemma 2.3(b)). So the set of selected posterior models near T is null. In particular no selection a ↦ C_a whose image near T has positive measure, such as index = likelihood, a 2-D patch or a sector at T, is realisable in this architecture.

*Proof of (a).*
1. Suppose |G ∩ U₀| > 0 and take a₀ ∈ G ∩ U₀ that is a Lebesgue density point of G.
2. For small s, the sets B_s := {a₀∘(1 + s(β + p − 1)) : |p| ≤ 10⁻⁵} and D_s (similarly, with q) are affine images of the p- and q-boxes. They lie inside the ball of radius 0.2s about a₀ and occupy a fixed positive fraction of it.
3. By density, G meets both, giving B ∈ G ∩ B_s and D ∈ G ∩ D_s.
4. By Prop 6.2, (a₀, B, D) is a kink triple. PP51 Thm 5.1 then says the gated triple has no fields passing the closed triple test, so (TC) fails. ∎

*Classification.* The obstruction belongs to the **architecture plus the posterior geometry**:
- the union of additive own-Bayes gates makes the closed triple test exact (Thm R1, PP47 Thm 4.1);
- Lemma 6.1 turns that test into linear separability in effective-weight space;
- the posterior family's answer regions near the corner rays of T's cone are wedges, which are not linearly separable on both sides of the lone world.

No axiom is involved. Theorem K is consistent with PP49's Theorem A (whose hypotheses it shows cannot all hold near T) and with Theorem N.

### 6.4 What remains

- **Kink-free 2-D families through T do not exist** in this architecture, in the strong sense that every gated posterior family is null near T. The coordinator's question (b) has a negative answer.
- What is left is the null route: a kink-free null gated set through T (lines, tripods, or possibly fractal sets) onto which a continuous selection maps a 2-D index neighbourhood. That set must carry:
  - a deficient cycle at some world (Theorem N), which needs four gated points in a two-dimensional arrangement, as in the checkpoint;
  - defences of every rival.
- **Evidence for the null route (CHECKED, `kink_scan_tripod.out`).** Take the tripod made of the three segments from u to the checkpoint corners B, C, D, sampled at 1/3, 2/3 and 1 (10 models, 120 triples). It carries no kink certificate. Thm 5.1 is only a sufficient obstruction, so this is evidence, not feasibility. Still, the checkpoint quadruple is compatible with a kink-free null gated set through T.
- Two exits change the hypotheses:
  - selective (non-union) acceptance, under which the closed triple test is no longer forced;
  - a family with half-plane answer regions, PP51 §5.3(b), to which §4 applies.

---

## 7. Status and scripts

| Result | Label |
|---|---|
| Lemmas 1.1, 1.2 | PROVED |
| Thm 2.1, Cor 2.1′ | CHECKED |
| Thm 2.2 | CHECKED (exact) |
| PP53 certificate | CHECKED (independent) |
| Prop 3.1, Cor 3.2 | PROVED; square case CHECKED |
| Prop 3.3 | PROVED (nearby regime); CHECKED (grid witnesses) |
| Thms 4.1, 4.2, Cor 4.3 | PROVED under (J), (Λ) |
| Thm 4.4 | PROVED under (J1), (Λ) |
| Prop 4.5 | PROVED |
| Conjecture 4.6 (depth-layered continuum, half-plane families only); face-collar placement | CONJECTURE |
| Lemma 6.1 | PROVED |
| PP51 kink instance; re-derivation of Thm 5.1 | CHECKED; PROVED |
| Prop 6.2 (box × scales) | CHECKED (exact) |
| Theorem K | PROVED |
| 3×3 grid | NUMERICS |

**Scripts** (`r9/PP50_py/`; run `python3 -I -B <script> > <script>.out` inside the folder):

| Script | Content | Label |
|---|---|---|
| `pp50_lib.py` | exact arrangement cells and types for posterior models | library |
| `verify_exact.py` | (V1)–(V5) for any table: exact types, full four-advice Bayes, intervals, Thm 4.1 triples, Floyd–Warshall prices | CHECKED, ALL PASS |
| `checkpoint_fields.json`, `_gauged.json`; `gauge_pattern.py` | the Thm 2.1 table; the audit-pattern gauge | CHECKED |
| `scale_matroid.py`, `scale_check.py` | Thm 2.2 | CHECKED |
| `convert_pp53.py` | independent re-verification of PP53 | CHECKED |
| `explore_types.py`, `rand_check_types.py` | type lists for three configurations; sampling cross-check | CHECKED |
| `kink_check.py` | §6.2: independent PP51 instance check (K0)–(K3), at scales 1 and 1/10 (the optional `numerics` effective-weight search is slow and was not used) | CHECKED, ALL PASS |
| `kink_box.py` | Prop 6.2: exact box and scale certificate | CHECKED, ALL PASS |
| `kink_scan_grid.py` | kink certificates on all triples of a model set (checkpoint: none; 3×3 grid: none) | CHECKED |
| `milp_search.py`, `explore_ansatz.py`, `construct_checkpoint.py`, `witness_search.py`, `witness_probe.py`, `grid_search.py` | MILP proposals (dominant-world Bayes, base-3 exponents); witness class; grid | NUMERICS (proposals only) |

**Most important next step.** Settle the null route.
1. **Gated set.** Gate exactly the tripod 𝒯 = ⋃_N [u, a_N] through the checkpoint corners, with fields on a fine sample of 𝒯. Use the exact triple reduction (Lemma 6.1) for every triple, together with the checkpoint's world-1 deficit.
2. **Selection.** Map a 2-D index neighbourhood onto 𝒯 continuously, as PP45 does for its tripod.
3. **Test.** Check that every rival is dominated by some member of 𝒯. Lemma S then gives closed sections. PP49 Theorem A's KKM dominance step has to be re-checked for a non-injective selection.

If the tripod with a deficient world-1 cycle is infeasible at the field level, Lemma 6.1's separability gives a dual certificate. That certificate would be the next structural theorem.

(Conjecture 4.6 stays relevant only for families with half-plane answer regions.)
