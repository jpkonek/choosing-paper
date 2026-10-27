# REF61 (positive side): referee report on the covering claims of P61, O61, F61 and E61

25 October 2026. Labels: PROVED (checked line by line here) / CHECKED (exact or symbolic check) / CONJECTURE / NUMERICS.
Referee scripts: `r61/ref61py/` (`thmD_pairs.py`, `ip_checks.py`, `geom_checks.py`, each with a `.out` file).
All sampling is atomic, so the numerics check algebraic identities only. Every convexity, Lyapunov or separation step was checked by hand.

## 0. Verdict table

| # | Claim | Verdict | Comment |
|---|---|---|---|
| 1 | P61 Thm A (the auditor's theorem): (G), (IB), transitivity, Lyapunov with 2n coordinates, Zorn, separation, uniqueness through monotonicity along **1**, coherence without polyhedrality, target protection, (C), (LF) | **CORRECT** | Every step re-derived (§1). |
| 2 | P61: converse to A11; convex one-sided U equals D_{K′} | CORRECT | |
| 3 | P61 Thm B(a)–(c): the undominated models are exactly X\*(W0,β,α) = D_{K(W0,β,α)} | **CORRECT** | Hypothesis "a model with a ≡ 0" is met by ∅. |
| 4 | P61 Thm B(d) = O61 Thm C: one free (exempt) point p ∈ Δ, including p ∈ ∂Δ | **CORRECT** | The two proofs are the same. |
| 5 | P61 Rem B′: sublinear vetoes add no targets | CORRECT for targets in relint Δ (the only use, in V6); GAP as a general statement | §2.3 |
| 6 | P61 Lemma V1: v ≠ e_j is visible from j iff h_j < 0 for every nonzero h ∈ F_v; the weak form in S1 is false | **CORRECT**; counterexample CHECKED | |
| 7 | P61 Lemma V2, Thm V: auditor's condition ⇔ uniform visibility ⇔ (iii-a)+(iii-b) | **CORRECT** | |
| 8 | P61 V3 (polytopes), V4 (smooth K ⊆ relint Δ), V5 (n = 2) | CORRECT | |
| 9 | P61 V6: for K ⊆ relint Δ, K is a VB-type target iff all but at most one extreme point is uniformly visible | **CORRECT** (within the stated class) | |
| 10 | P61 V7: reversed triangle, pari-mutuel models, boxes excluded from VB-type rankings | CORRECT (within the class) | |
| 11 | P61 D1: lower-dimensional K impossible on one-sided (LF) domains | CORRECT for μ with positive density (Gaussian). Minor GAP under bare (H2) | §2.5 |
| 12 | P61 D2, D3 | CORRECT | D3 proves only "exactly one zero"; see row 16. |
| 13 | IP classes "in": interior ε-contaminations, TV balls, belief functions with m(Ω) > 0 and positive singletons, strictly 2-monotone cores, strictly convex distortions, the PRI rule, smooth K, n = 2 | **CORRECT**; NUMERICS agree | |
| 14 | **IP class "in": constant-odds-ratio (COR)** | **ERROR (mislabel)** | The COR credal set is a density-ratio class, i.e. a normalised box, which P61 itself excludes (I6). I2 covers only the core of the COR *event* lower probability, which is a different, larger set. NUMERICS: 3 non-visible vertices at n = 3 and 10 at n = 4. |
| 15 | IP classes "out": pari-mutuel models, boxes | CORRECT (within the VB class) | |
| 16 | "ε-contaminations whose p has a zero coordinate are out (n ≥ 3)" | GAP (overstated), easily repaired | D3 proves the one-zero case. Repair for more zeros in §2.6. |
| 17 | P61 §7 nearby results: truncation hexagons, parallel bodies, one exact vertex | CORRECT | Trivial fix: the hexagon needs η < 1/10; η = 1/10 gives a triangle. d_H = η√(3/2) CHECKED. |
| 18 | O61 chamfered-triangle coverage (hexagon via Thm A; pentagon via Thm C) | **CORRECT for 0 < s ≤ 1/2**; GAP for s ∈ (1/2, 1) | For s > 1/2 the chords cross, so there is no chamfer. The Hausdorff-limit conclusion (s → 0) is unaffected. |
| 19 | F61 Thm D: radial simplices (T1, every interior ε-contamination, unequal ε_i allowed) covered on A_K | **CORRECT** | Case split, Lemma D1, coherence, (G), (IB), (C), (LF) and domain legitimacy all check. NUMERICS: 0 mismatches over 480 draws × 10⁵ pairs, with the pair-level minimisation done independently. |
| 20 | F61 side remark "A_K ⊇ D_{K′} for every K′ ⊆ K" | ERROR (minor, not load-bearing) | Explicit counterexample in §3.4. True when p ∈ K′. |
| 21 | E61 Prop 6.1: dense exact coverage | **CORRECT** | Now unconditional, since Thm A is refereed here. NUMERICS reproduced. |

Net assessment: every load-bearing positive theorem holds: Thm A, Thm B and C, Thm V and V6, Thm D, and Prop 6.1. There is one substantive error, the COR classification. The other gaps are scope or range qualifications.

---

## 1. P61 Theorem A, line by line (PROVED)

- **A1 (G).** h ∈ U and h_i ≥ 0 give v·h ≥ 0 for every v = (1−t)k + te_i. This uses k·h > 0 on K′, which is where h ∈ U is used. So φ_i = 0 on correct acceptances.
  - If X improves Y at i, then X∖Y ⊆ {h_i > 0} and Y∖X ⊆ {h_i < 0}.
  - So Δa ≤ 0 and Δb < 0, and the lexicographic order is strict. ✓
- **A2 (IB), A3 integrability.** ✓ (|v·h| ≤ max|h_j| for v ∈ Δ).
- **A4 Lyapunov.** There are finitely many (2n) integrable coordinates, and μ is non-atomic. ✓
- **A5 Zorn.** Ties at every world mean equal z, so ⪯ is a partial order on Z.
  - The chain is a decreasing net, and each a_ω is monotone along it, so the cluster point attains the infimum.
  - If the infimum equals a_ω(y^γ), the whole tail below y^γ has that value. Then b_ω is non-increasing on the tail, and the cluster point lies in the closure of the tail. ✓
- **A6 separation.** Prop lexbayes needs a model with a ≡ 0. D_K is one, and so is ∅.
  - The signs of λ and the β ≠ 0 argument are as in LDG.
  - Z′ is the range over X ⊆ N(W0), because φ ≥ 0. ✓
- **A7 uniqueness.** For v ≥ 0 with **1**·v = 1, φ(h + t**1**) = max(0, s − t) ≤ φ(h). So g strictly decreases along **1** at rate ≥ Σβ > 0.
  - {g = 0} is closed and meets each line h + ℝ**1** at most once, so Fubini makes it Lebesgue-null, hence μ-null. ✓
  - No polyhedrality is used.
- **A8 coherence.**
  - φ_ω(h) = sup over conv({0} ∪ A_ω) of (−v·h), so g = max over W of (−w·h). W is compact and every w ≥ 0 has **1**·w ≥ Σβ, so {g < 0} = D_Ŵ.
  - For ω ∈ W0, ψ_ω(h + t**1**) = ψ_ω(h) + t, so {φ_ω = 0} = D_{A_ω} a.e.
  - So X\* = D_{conv(K′ ∪ ⋃_{W0} A_ω ∪ Ŵ)}, which is coherent and contained in U because K\* ⊇ K′. ✓
- **A9 (W), (C).** A model tied at every world has the same z, so it is undominated, hence coherent. LDG Prop W(a) then applies. ✓
- **A10 target protection.**
  - a_i(D_K) = 0 because A_i ⊆ K.
  - A weak dominator Y has every a_i(Y) = 0, so Y ⊆ U ∩ ⋂D_{A_i} = D_K a.e.
  - For p ∈ K, Σp_i(b_i(Y) − b_i(D_K)) = ∫_{D_K∖Y} p·h > 0 unless D_K∖Y is null. That contradicts b_i(Y) ≤ b_i(D_K) for every i. ✓
- **A11 (LF).** Take 0 ≠ h ∈ ∂D_K. Then m ↦ m·h is non-constant on aff Δ with minimum 0 over K, so it is strictly positive on relint K ⊇ K′. ✓
  - Converse: if k′ ∈ K′ ∩ rel∂K, the boundary gamble h with k′·h = 0 lies on ∂U. Every neighbourhood of h meets the open complement of cl U, so (LF) fails. ✓
- **Convex-U remark.** This is the standard identity int C = {y·h > 0 for all y ∈ C\*∖0}. C\* ⊆ ℝⁿ₊ because D_K ⊇ int ℝⁿ₊. ✓

## 2. P61 Theorems B and V, and the IP classes

**2.1 Thm B (PROVED).**
- "Only these": A6–A8 use only the existence of some model with a ≡ 0.
- "All these": a weak dominator Y has a_ω(Y) = 0 on W0, b_ω(Y) ≤ b_ω(X\*) on W0, and a_ω(Y) ≤ a_ω(X\*) off W0. So J(Y) ≤ J(X\*), and uniqueness gives Y = X\*. ✓
- (d): with W0 = Ω and β = p, X\* = U ∩ ⋂D_{A_i} ∩ {p·h > 0} = D_{conv(K_0 ∪ {p})}. ✓
- O61 Thm C is word for word the same result. **CORRECT.**

**2.2 Visibility (PROVED).**
- V1 (⇒): (x + s(x − e_j))·h = −s h_j. This is positive because the point is in relint K and h ≠ 0 is non-constant on aff Δ. ✓
- V1 (⇐): separate the open ray from relint K inside aff Δ, then represent the affine separator by h ∈ ℝⁿ. ✓
- V2 is pure translation. ✓
- Thm V:
  - (ii)⇒(iii) uses the fact that k ∈ K_δ has full support, because relint K ⊆ relint Δ for full-dimensional K. ✓
  - (iii)⇒(ii) is a compactness cover. A vertex e_i ∈ cl ext K is extreme in K, so (iii-b) makes it isolated. ✓
- V6 (⇒): β̂ ∈ Ŵ ⊆ K and K ⊆ relint Δ force supp β = Ω = W0. ✓
- Tangent example CHECKED (`ip_checks.out` (4)):
  - The normals at v are (0, 1, −1) and (−1, .905, .429).
  - v is weakly visible from world 1 only, and strictly visible from no world. The ray LP agrees.

**2.3 Rem B′ scope.**
- For a sublinear veto φ_i = sup over B_i of (−v·h), the undominated set is conv(K′ ∪ ⋃_{W0} Â_ω ∪ normalise(β + Σα B_ω)).
- When W0 ≠ Ω, the last term depends on the radial shape of B_ω, not only on Â_ω. So "the same targets as VB(K′,Â)" is proved only when W0 = Ω.
- W0 = Ω is forced for targets in relint Δ, which is the only place B′ is used (V6). Elsewhere, state it as CONJECTURE.

**2.4 IP classes.**
- Lemma I0 ✓. Faces are cones of active h_A = 1_A − P̲(A)**1**.
- I1 ✓. I2 ✓: the strict marginal inequality applies strict supermodularity to the non-nested pair (C ∪ x, D).
- I3 ✓. I4 ✓: at n = 3 the PRI facets alternate upper/lower around the hexagon, so every vertex has one of each. I5 ✓. I6 ✓.
- NUMERICS (independent ray-LP test): TV balls at n = 4, 5 and random belief functions at n = 4, 5 have 0 non-visible vertices.
- **COR is an ERROR.**
  - Walley's constant-odds-ratio model has the density-ratio class {m : m_i/p_i ≤ k·m_j/p_j} as its credal set, with k = 1/(1−δ). That is the normalised box ν(p ⊙ [1,k]ⁿ).
  - Its lower probability on events is f∘p with f(x) = (1−δ)x/(1−δx). CHECKED: the minimum over the class equals f(p(A)) for every A.
  - But the core of f∘p is a different, larger polytope. None of the 6 (n = 3) or 24 (n = 4) core vertices is a vertex of the density-ratio class.
  - The COR credal set has 3 (n = 3) and 10 (n = 4) non-visible vertices, matching P61's own box counts. So it is **excluded** by V6.
  - **Repair:** replace "constant-odds-ratio" by "the 2-monotone envelope (core of the event lower probability) of a COR model", and move COR proper to the "out" list alongside boxes.

**2.5 D1 measure hypothesis.** The step "g ∈ U and −g ∈ U for a.e. g ∈ O" needs μ to charge both O and −O. Gaussian μ does, as does any μ with a positive density. Under bare absolute continuity, (LF) can hold vacuously where μ vanishes. Add "μ has a positive density" to D1.

**2.6 Repair for row 16 (p with several zeros, n ≥ 3).**
- *Case |supp p| ≥ 2.* The vertices v_i with i ∈ supp p all have support supp p. In the face {m_Z = 0}, where Z is the zero set of p, the extreme generators are normalisations of box corners β + Σ_{M′} α_ω e_ω. At most one corner has support supp p (the D3 count). So the target is not generated.
- *Case p = e_1.* Then v_i = ν(e_1 + a e_i), with a = ε/(1−ε), must come from Ŵ.
  - Generating v_2 and v_3 forces e_2 ∈ A_2 and e_3 ∈ A_3, with α_2λ_2 = α_3λ_3 = aβ_1.
  - So Ŵ also contains ν(β_1, aβ_1, aβ_1, …). Its first coordinate is 1/(1 + 2a) < 1 − ε, so it lies outside K.
- Hence the full claim holds (PROVED here).

**2.7 Nearby results.** d_H(K_η, K) = η√(3/2), CHECKED at η = .01, .05, .1. The hexagon range should be 0 < η < 1/10. N3 is ✓: adding v_1 leaves the normal cones at the four surviving hexagon vertices unchanged.

## 3. F61 Theorem D (radial simplices on A_K): CORRECT

**3.1 Ranking and axioms.**
- At world m the advice scores are: correct (0, −|s_m|); silent (0, 0); wrong (φ, +|s_m|); contradiction (φ of the wrong half, 2|s_m|).
- Level 1 is weakly monotone in the advice rank, and level 2 strictly. So strict (G) holds lexicographically on any domain.
- (IB) holds because both levels are integrals over problems.
- Lyapunov with finitely many actions per pair makes the range convex and compact.
- Lemma zorn applies.

**3.2 Coherence of minimisers (the case split, PROVED).** Prop lexbayes applies via the vacuous model. The pointwise rule on a pair is as follows.
- A contradiction costs Σβ_i·2|h_i| + (≥ 0) > 0, so it is never chosen.
- G(h) > 0 forces β·h > 0, hence G(−h) < 0. So at most one orientation is accepted. The accepted set is A_K ∩ ⋂_{W0} Z_i ∩ {G > 0}.
- {G = 0} is null: G is piecewise linear with non-negative, nonzero gradients β + Σα_m v_m.

Then:
- **(a) Two or more positive coordinates.**
  - Membership of A_K kills the indicator, so φ_m = [−v_m·h]_+ for every m.
  - The two sets then agree. When W0 = {k}, G > 0 forces h_k > 0, hence v_k·h ≥ 0. ✓
- **(b) Exactly one positive coordinate k.**
  - G > 0 forces k ∈ supp β ⊆ W0, so the indicator never enters G for m ∈ M (those m have h_m < 0).
  - The only discrepancy is the omitted constraint v_k·h ≥ 0.
  - When |W0| ≥ 2, Lemma D1 recovers it. Some i ∈ W0∖{k} has h_i < 0 and v_i·h ≥ 0, so (1−ε_i)p·h ≥ −ε_i h_i > 0, which gives v_k·h > 0.
  - When W0 = {k}, K\* omits v_k as well.
  - D1 never needs i ∈ supp β. ✓
- **(c) No positive coordinate.** Neither set accepts. ✓

NUMERICS (`thmD_pairs.out`) independently re-implement the pair-level minimisation over the four actions, including contradictions and the face constraint for each action. They use unequal ε_i, n = 3, 4, 5, and β supported on random subsets of W0. Result: 0 mismatches with A_K ∩ D_{K\*} over 480 draws × 10⁵ pairs, and no contradiction is ever chosen. F61's own script used equal ε and single acceptances only. This closes that gap.

**3.3 (iv), (v), (vi) and the domain.**
- **(iv)** ⋂Z_i ⊆ cl D_K, even without A_K: if some h_i < 0, then p·h > 0, so every v_k·h ≥ 0. A contradiction would need ±h ∈ cl D_K, which is null. The p-weighted Brier argument then gives Y = D_K. (0 violations on samples.) ✓
- **(v)** A tie at every world gives equal scores. Uniqueness then gives equality a.e. ✓
- **(vi)** p ∈ relint K, with positive barycentric weights λ_i ∝ p_i/ε_i. So r ∈ ∂D_K∖0 has r_i < 0 at its active facet, and p·r > 0. Hence v_k·h > 0 near r at every k with r_k ≥ 0, and a neighbourhood of r lies in A_K. ✓
- **Domain.** A_K is a Borel cone. The models are all measurable subsets of A_K, with pair menus determined by availability. This is closed under splicing and under limits in measure. ✓
- **Two definitions to state explicitly:**
  - Coherence on A is read as X = A ∩ D_Q. F61 §1 states this; it should be flagged to the author as a definition.
  - The domain depends on the target, exactly as U = D_{K′} does.
- Two-sidedness (vii) ✓ on the single-negative parts only. F61 itself notes that −h ∉ A_K near the two-negative parts.
- **n = 2:** A_K = ℝ², so Thm D gives full-domain coverage of intervals. This is consistent with F61 Cor A1.

**3.4 Side-remark error.** "A_K ⊇ D_{K′} for every K′ ⊆ K" is false.
- Take n = 3, p = u, ε = ½ and h = (1, 3, −10).
- Then v_1·h = −½, so h ∉ A_K: it has two positive coordinates.
- But k′·h = 0.425 > 0 for k′ = .97v_2 + .03p ∈ relint K. So h ∈ D_{K′} for a small ball K′ about k′.
- **Repair:** the claim holds whenever p ∈ K′, since then p·h > 0. Nothing in Thm D uses the claim.

## 4. O61 chamfers and E61 dense coverage

**O61 chamfers.**
- The identity v_1 − e_2 = (v_3 − v_1) + 3(v_2 − v_3) is CHECKED.
- From the cut point w = v_1 + s(v_3 − v_1), the direction w − e_2 points strictly inside both the facet m_2 ≤ 2/5 and the chord, by inward-normal signs. So w is strictly visible from world 2, and symmetrically for the other cut points.
- Two cuts on the same edge cross once s > 1/2. State the result for 0 < s ≤ 1/2. At s = 1/2 the result is the lower triangle, an ε-contamination, which is covered.
- The Thm C pentagon has the same range restriction.

**E61 Prop 6.1 (PROVED).**
- The supporting-line argument for K′_s ⊆ relint K_s is valid: x ∈ relint Δ gives c·x < max c_i, and the segment towards e_{i\*} stays in A_{i\*} for small t.
- The d_H bound is immediate.
- NUMERICS (`geom_checks.out`):
  - K_s is a hexagon at s = .5, .8, .9, .95, .99;
  - d_H = .0645, .0266, .0135, .0068, .0014, which matches E61 and stays below the bound;
  - K′_s ⊆ relint K_s;
  - every vertex is strictly visible.
- With Thm A refereed, the coverage claim is now unconditional. The proof needs only K full-dimensional, not K ⊆ relint Δ.

## 5. Points for the lead
1. Correct the COR entry; this is the only substantive error.
2. Restrict Rem B′ to W0 = Ω (or to targets in relint Δ), O61's chamfers to s ≤ 1/2, and N1 to η < 1/10. Add "positive density" to D1.
3. Replace D3's scope by §2.6 (all zero patterns, n ≥ 3).
4. Thm D is sound as stated, including unequal ε_i. Delete or repair the "A_K ⊇ D_{K′}" remark. State the definition of coherence on A_K explicitly in any write-up.
