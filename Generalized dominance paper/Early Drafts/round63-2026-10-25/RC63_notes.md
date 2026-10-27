# RC63: referee report on the composition theorem, the reach lemma and the orthant-map closure lemma

25 October 2026. Role: composition referee. Binding inputs: `AUDIT_r62_composition.md` §1 and `AUDIT_r63_decisions.md`.

Labels:
- **PROVED**: proved or re-derived here; not yet independently refereed.
- **CHECKED**: exact rational computation.
- **CONJECTURE**.
- **NUMERICS**.

Scripts are in `rc63py/`. Run each with `python3 -I` from that folder; each has a `.out` file.

| Script | What it checks |
|---|---|
| `geom.py` | exact helpers for n = 3 |
| `comp_check.py` | the pullback identity, guidance, monotonicity along 𝟙, and the exempt-point identity |
| `reach_search.py`, `ratio_lemma.py` | the reach lemma and the n = 3 count formula |
| `boundary_example.py` | a new n = 3 target whose exempt point is on an edge of the simplex |
| `n4_search.py` (NUMERICS), `n4_exact.py` (exact) | a new interior target in four worlds |
| `closure_check.py` | the closure lemma, plus a sanity check of the tie counterexample in AUDIT_r63 |

---

## 0. Summary

1. **The composition theorem is correct** (steps 1–7, with and without the exempt point).
   - There is no gap that needs repair. Two remarks:
   - The pullback identity holds exactly at every nonzero gamble, for any convention on the coordinate planes. The audit says only "almost everywhere".
   - The whole theorem follows in a few lines from a conjugacy (§2.8). The composed ranking *is* the veto–Brier ranking VB(L′,A), run on the pushed-forward measure ν = c₊μ. So every VB result transfers at once, including the exact list of undominated models.
2. **The reach lemma is correct.** I strengthen it in three ways (§3):
   - (a) it is symmetric in the two factors;
   - (b) it needs only (LF) for the composed target, not L′ ⊆ relint L;
   - (c) for n = 3 it becomes an exact formula.
3. **The closure lemma is correct** (§4).
4. **Main new finding (PROVED, CHECKED).** For three worlds and a target inside the open simplex, composition produces nothing new.
   - Every interior target L⋆K₀ has at most as many non-visible extreme points as L has.
   - So with a VB-type factor L, L⋆K₀ is already VB-type with at most one exempt point.
   - This rules out the CC63 task (a) "a target that is not VB-type" for n = 3 with interior factors.
   - In particular, no interior triangle with one or two edge lines through simplex vertices and two or more non-visible vertices is a composed target.
5. **The nearby reachable results** (consistent with keeping the aim and moving the setting):
   - (i) **n = 3, exempt point on an edge of the simplex.** The composed target has a whole edge ν(π\*⊙K₀) lying on the simplex boundary. It is outside both earlier classes (PROVED). Exact pentagon in §3.5 (CHECKED).
   - (ii) **n = 4, interior target.** An exact example of L⋆K₀ with three non-visible vertices and a facet normal with no zero coordinate (CHECKED). It is covered by the composition theorem, is not VB-type, and is not orthant-planar.
   - So composition does give genuinely new exactly covered targets, but not where the round expected (n = 3 interior).

## 1. Verdict table

| # | Item | Verdict | Label |
|---|---|---|---|
| 1 | Step 1, pullback identity c⁻¹(D_Q) = D_{Q⋆K₀} for every compact convex Q ⊆ Δ | **CORRECT**, and stronger than stated: exact for every h ≠ 0, every boundary prior and every coordinate-plane convention | PROVED; CHECKED (0 mismatches in 151 898 gamble evaluations × 12 identities, about 1/3 of them on coordinate planes, every convention) |
| 2 | Step 2, guidance (veto counts only wrong acceptances; secondary score is strict) | CORRECT | PROVED; CHECKED (26 805 tests, 0 violations) |
| 3 | Step 3, integrability, Lyapunov in h-space, Zorn | CORRECT | PROVED |
| 4 | Step 4, separation transfers (common-zero model; VB minimiser is D_Q with Q ⊇ L′ in c-coordinates) | CORRECT | PROVED |
| 5 | Step 5, null sets pull back through the piecewise-linear map; uniqueness; global coherence; (C) | CORRECT | PROVED; monotonicity along 𝟙 CHECKED (5 000 tests) |
| 6 | Step 6, target protection, without and with the exempt point | CORRECT. Any p ∈ L works, not only p ∈ L′. | PROVED; exempt identity D_K = c⁻¹(D_{L_N}) ∩ {π\*·c > 0} CHECKED (0 mismatches, including π\* on ∂Δ) |
| 7 | Step 7, (LF) | CORRECT. L′ ⊆ relint L is sufficient. The exact condition is L′⋆K₀ ⊆ relint(L⋆K₀). | PROVED |
| 8 | "Taking K₀ uniform recovers VB" | CORRECT (c = identity when d_σ = 𝟙) | PROVED |
| 9 | Alternative proof by conjugacy to VB(L′,A) under ν = c₊μ | NEW | PROVED |
| 10 | Exact undominated family of the composed ranking: {D_{K(W0,β,α)⋆K₀}} | NEW (from P61 Thm B via item 9) | PROVED |
| 11 | Reach: extreme points of L⋆K₀ come from extreme points of both factors | CORRECT | PROVED |
| 12 | Reach: strict visibility preserved by q ↦ ν(q⊙m) | CORRECT | PROVED |
| 13 | Reach: non-visible extremes lie in ν(q\*⊙K₀) | CORRECT; strengthened to ν(q\*⊙ nonvis K₀) | PROVED; CHECKED (n = 3, 1 881 cases; n = 4 exact example) |
| 14 | Reach: reversed triangle not reachable | CORRECT; extended to the entire undominated family and to (LF)-only hypotheses | PROVED |
| 15 | Closure lemma for two orthant-diagonal maps | CORRECT (the maps also commute, and ⋆ is commutative) | PROVED; CHECKED (3 pairs, 0 mismatches) |
| 16 | **n = 3 count formula:** interior non-visible extremes of L⋆K₀ are exactly ⋃_i ν(M_i(L)⊙M_i(K₀)) | NEW | PROVED; CHECKED (3 200 random L × 4 K₀, 0 mismatches) |
| 17 | **n = 3, interior factors: L⋆K₀ is VB-type (≤ 1 exempt point) whenever L is** | NEW. Composition adds no interior n = 3 targets. | PROVED (polygonal L); CONJECTURE for non-polygonal L (uniform visibility) |
| 18 | n = 3, π\* in the relative interior of an edge of Δ: target outside VB-type and orthant-planar classes | NEW | PROVED; exact pentagon CHECKED |
| 19 | n = 4 interior composed target with 3 non-visible vertices, not orthant-planar | NEW | CHECKED (exact); search NUMERICS |
| 20 | AUDIT_r63 tie example (sanity check only, not my remit) | consistent | CHECKED |

---

## 2. The composition theorem, step by step

**Notation and hypotheses.**
- (H1) n finite worlds. Δ is the simplex and ν(x) := x/(𝟙·x).
- (H2) μ is Gaussian, or any finite measure absolutely continuous with respect to Lebesgue measure with a finite first moment.
- (K0) K₀ ⊆ relint Δ is compact, convex and orthant-planar. On each mixed orthant σ, D_{K₀} ∩ σ = {d_σ·h > 0} ∩ σ with d_σ ≫ 0. On the two pure orthants, d_σ ≫ 0 is arbitrary. The chart is c(h) := d_σ⊙h for h ∈ cl σ.
- (L) L = conv(L′ ∪ A₁ ∪ … ∪ A_n), or the same with one extra point π\* ∈ Δ. Here:
  - L′ is nonempty, compact and convex, with L′ ⊆ relint L;
  - each A_i ⊆ conv(L′ ∪ {e_i}) is compact;
  - L is full-dimensional.
- Put Q⋆K₀ := conv{ν(q⊙m) : q ∈ Q, m ∈ K₀}, K := L⋆K₀, K′ := L′⋆K₀ and U := D_{K′}.
- The scores are φ_i(h) := max(0, sup_{v∈A_i} −v·c(h)), a_i(X) := ∫_X φ_i dμ and b_i(X) := −∫_X c_i(h) dμ.

### 2.1 Step 1: the pullback identity (CORRECT, and exact)

*Claim (PROVED).* For every nonzero h, every convention choosing σ with h ∈ cl σ, and every nonzero q ≥ 0:

  q·c(h) > 0 ⟺ h ∈ D_{ν(q⊙K₀)}.

*Proof.*
- **Mixed σ.** REF62-R2 §3 proves D_{K₀} ∩ cl σ = {d_σ·x > 0} ∩ cl σ on the *closed* orthant. I re-checked both inclusions.
  - (⊆) Perturb x into σ along an s with d_σ·s < 0.
  - (⊇) Perturb along an s with m·s < 0.
  - Put x := q⊙h ∈ cl σ. If x ≠ 0, then q·c(h) = d_σ·x > 0 ⟺ x ∈ D_{K₀} ⟺ (q⊙m)·h > 0 for every m ∈ K₀.
  - If x = 0, that is supp q ∩ supp h = ∅, both sides are false.
- **Pure σ.** Both sides reduce to "supp q meets supp h" on the closed positive orthant. On the closed negative orthant both are false.
- Because h may sit on a coordinate plane and use either adjacent d_σ, the identity holds at every h ≠ 0. ∎

Hence, for every compact convex Q ⊆ Δ and every h ≠ 0:

  c(h) ∈ D_Q ⟺ h ∈ ⋂_{q∈Q} D_{ν(q⊙K₀)} = D_{S_Q} = D_{Q⋆K₀},

where S_Q := {ν(q⊙m)}.
- S_Q is compact, because q·m ≥ min_{K₀} min_i m_i > 0.
- D_S = D_{conv S} because the condition is linear.
- The audit's remark that coordinate-plane ambiguities form "a single null set" is true but unnecessary.

CHECKED in `comp_check.out`:
- Q = L (a VB triangle with an exempt point), Q = L′, and ten boundary and interior priors.
- 151 898 gamble evaluations, about 30% of them on one or two coordinate planes with all 8 conventions.
- 0 mismatches.

### 2.2 Step 2: guidance (CORRECT)

- c_i(h) has the sign of h_i because d_σ ≫ 0.
- For h ∈ U we have c(h) ∈ D_{L′} by Step 1, for every h ≠ 0.
- If h_i ≥ 0 and v = (1−t)k + te_i with k ∈ L′, then v·c(h) = (1−t)k·c(h) + t·c_i(h) ≥ 0. So φ_i(h) = 0.
- Strict (G): if X improves Y at i, the veto score does not rise. The secondary difference is −∫_{X∖Y} c_i + ∫_{Y∖X} c_i < 0, since both integrands have the right sign and XΔY is non-null.
- (IB) holds because all levels are integrals.

CHECKED: 26 805 pairs (h ∈ U, i with h_i ≥ 0), against every v ∈ A_i ∪ {e_i} ∪ vert L′. No violations.

### 2.3 Step 3: compact range (CORRECT)

- |c(h)|_∞ ≤ max_σ‖d_σ‖_∞ |h|, so the 2n integrands are dominated by a multiple of |h|.
- Lyapunov's theorem is used in h-space with the non-atomic μ. It needs nothing about c₊μ.
- LDG Lemma zorn then gives an undominated weak dominator for every model.

### 2.4 Step 4: separation (CORRECT)

The hypotheses of LDG Prop lexbayes hold:
- Z is convex.
- a_i ≥ 0.
- There is a **common-zero model**. D_K is one: for h ∈ D_K, c(h) ∈ D_L by Step 1, and A_i ⊆ L. The veto-free region c⁻¹(D_{L_N}) is another, with L_N := conv(L′ ∪ ⋃A_i).

So an undominated X\* minimises

  J(X) = ∫_X g dμ,  g(h) = G(c(h)),  G(x) := Σ_{ω∉W0} α_ω max(0, sup_{A_ω} −v·x) − β·x,

over X ⊆ U ∩ ⋂_{ω∈W0}{φ_ω = 0}, with β ≥ 0 nonzero and supported on W0.
- G is *literally* the VB integrand in c-coordinates.
- The constraint set is c⁻¹ of the VB constraint set N_c(W0) = D_{L′} ∩ ⋂_{W0}{ψ_ω ≥ 0}.
- In c-space the VB minimiser is N_c(W0) ∩ {G < 0} = D_Q a.e., with Q := conv(L′ ∪ ⋃_{W0} A_ω ∪ Ŵ) ⊇ L′.
- So the audit's "D_Q ∩ D_{L′}" is just D_Q.
- Ŵ may contain boundary priors when W0 ≠ Ω. Step 1 covers those.

### 2.5 Step 5: null sets and uniqueness (CORRECT)

- G(x + t𝟙) ≤ G(x) − tΣβ, so {G = 0} is closed and meets each line x + ℝ𝟙 at most once. By Fubini it is Lebesgue-null. CHECKED: 5 000 random (x, t, α, β), 0 failures.
- **Pullback of null sets through a map that is not globally linear.** On each open orthant σ, c is the invertible linear map diag(d_σ), and it maps σ *onto* σ. So c⁻¹(E) ∩ σ = diag(d_σ)⁻¹(E ∩ σ) is null whenever E is. There are finitely many orthants, and the coordinate planes are null.
- Discontinuity of c across the planes is irrelevant.
- Hence {g = 0} is μ-null and the minimiser is unique a.e.: X\* = c⁻¹(D_Q) = D_{Q⋆K₀} a.e.
- That model is coherent, because Q⋆K₀ is a nonempty compact convex subset of Δ, and it lies inside U because Q ⊇ L′.
- (C): a model tied at every world with X\* has the same score vector, so it is undominated, so it equals X\* a.e.

### 2.6 Step 6: target protection (CORRECT)

**Without an exempt point.**
- If Y ⪯ D_K at every world, then a_i(Y) = 0 for all i.
- So Y ⊆ U ∩ ⋂{φ_i = 0} = c⁻¹(D_{L′} ∩ ⋂D_{A_i}) = c⁻¹(D_L) = D_K a.e. The boundary {ψ_i = 0} is null and pulls back to a null set.
- For any p ∈ L (not only p ∈ L′), Σp_i(b_i(Y) − b_i(D_K)) = ∫_{D_K∖Y} p·c(h) dμ, which is > 0 unless D_K∖Y is null.

**With an exempt point.**
- D_L = D_{L_N} ∩ {π\*·x > 0}, so D_K = c⁻¹(D_{L_N}) ∩ {π\*·c > 0} (CHECKED with π\* interior and π\* on an edge).
- This is the a.e.-unique minimiser of Σπ\*_i b_i over the veto-free models. The tie set {π\*·c = 0} pulls back from a hyperplane, so it is null.
- So D_K is undominated, exactly as in O61 Thm C.

### 2.7 Step 7: (LF) (CORRECT)

- For fixed m ≫ 0, T_m(q) := ν(q⊙m) is a homeomorphism of Δ with inverse ν(·⊙m⁻¹). It maps relint Δ onto itself.
- q ∈ L′ ⊆ relint L, and relint L is open in aff Δ and contained in relint Δ. So T_m(relint L) is open and contained in K, hence in relint K.
- So K′ ⊆ relint K, because relint K is convex. P61 A11 then gives U ⊇ ∂D_K∖{0}.

**Remark (PROVED).** L′ ⊆ relint L is sufficient, not necessary. What (LF) needs is exactly K′ = L′⋆K₀ ⊆ relint K (P61 A11 and its converse). §3.2 uses this weaker form.

### 2.8 A shorter proof: conjugacy to VB (PROVED)

- c is a bijection of ℝⁿ minus the coordinate planes onto itself: each open orthant goes linearly onto itself.
- Let ν := c₊μ. It satisfies (H2):
  - it is finite;
  - it is absolutely continuous, because null sets pull back to null sets (§2.5);
  - it has a finite first moment, ∫|x| dν = ∫|c(h)| dμ < ∞.
- X ↦ c(X) is a bijection, modulo null sets, between the measurable X ⊆ U and the measurable Y ⊆ D_{L′}. It preserves:
  - every score: a_i(X) = ∫_{c(X)} max(0, sup −v·x) dν and b_i(X) = −∫_{c(X)} x_i dν;
  - the correctness of every acceptance at every world, since signs are preserved;
  - nullness.
- So **the composed ranking on M_U is isomorphic to VB(L′,A) on M_{D_{L′}} under ν.**
- P61 Thms A and B and O61 Thm C apply verbatim. Undominated models are exactly the c⁻¹(D_{K(W0,β,α)}) = D_{K(W0,β,α)⋆K₀}. The target D_L is undominated. Strict (G), (IB) and (C) transfer.
- Only (LF) needs a separate argument, §2.7, because c is not a homeomorphism of ℝⁿ.

**Remark.** The theorem holds for every positive rescaling d_σ ↦ λ_σ d_σ of the chart. The targets do not change; the rankings do (AUDIT_r62 §0 on direction invariance).

---

## 3. The reach lemma and what composition actually reaches

### 3.1 The audit's statements (CORRECT)

- **Extreme points come from extreme points.** Use bilinearity of (q,m) ↦ q⊙m. If q = Σλ_j q_j, then ν(q⊙m) = Σ_j [λ_j (q_j·m)/(q·m)] ν(q_j⊙m), and the weights are positive and sum to 1. Do the same in m. Extremality forces equality.
- **Visibility is preserved.** T_m maps lines through e_j to lines through e_j, preserving order along them. It also maps relint L into relint K (§2.7). So a ray from e_j through q into relint L becomes a ray from e_j through T_m q into relint K.
- **Where the non-visible extreme points sit.** Let x be a non-visible extreme point and take a representation x = ν(q⊙m) with both factors extreme. Then q is non-visible, so q = q\*.
- **Equality case.** If every extreme point is non-visible, then ext K ⊆ ν(q\*⊙K₀) ⊆ K. Since ν(q\*⊙K₀) is convex (a projective image of a convex set), K = ν(q\*⊙K₀).
  - That set is orthant-planar, with deciding vectors d_σ⊙q\*.
  - It is full-dimensional, so q\* is interior.
  - The reversed triangle has three non-visible vertices (P61 V7) and is not orthant-planar (REF62-R2 row 9). So it is excluded.

### 3.2 Strengthenings (PROVED)

**(a) Symmetric form.** Assume K₀ is full-dimensional. If x = ν(q⊙m) ∈ relint Δ and m is visible in K₀ from j, then x is visible in K from j: apply T_q, a homeomorphism of relint Δ because q ≫ 0, to the visibility ray of m. Hence:

  the interior non-visible extreme points of L⋆K₀ lie in {ν(q⊙m) : q ∈ nonvis ext L, m ∈ nonvis ext K₀}.

CHECKED on the n = 4 example: all 3 non-visible vertices of K have the form ν(q\*⊙m) with m non-visible in the box.

**(b) Only (LF) is needed, not L′ ⊆ relint L.** Let Q := conv(L′ ∪ ⋃A_i ∪ {β̂}) and suppose K′ = L′⋆K₀ ⊆ relint(Q⋆K₀). Every extreme point x = ν(q⊙m) with q extreme in Q falls into one of these cases:
- q ∈ L′: impossible, since then x ∈ K′ ⊆ relint K;
- q ∈ A_i with q = (1−t)k + te_i, 0 < t < 1: then x lies strictly between T_m k ∈ relint K and e_i, so it is visible from i;
- q = e_i: then x = e_i;
- q = β̂: then x ∈ ν(β̂⊙K₀).

**(c) The whole undominated family.** By §2.8 the undominated models are the D_{K(W0,β,α)⋆K₀}. If such a target lies inside relint Δ, then supp β = Ω, because ν(β̂⊙m) ∈ K has support supp β. So W0 = Ω and Ŵ = {β̂}, and (b) applies.

**Consequence.** No composed ranking (L′, A, K₀ orthant-planar) has the reversed triangle as an undominated target with (LF), on any U-domain of this form, in any number of worlds.

### 3.3 n = 3: an exact count (PROVED, CHECKED)

**Lemma N3.** Let n = 3. Let K be compact, convex and full-dimensional, and let x ∈ K ∩ relint Δ be an extreme point. Then x is non-visible iff, for some i, x minimises both ratios m_i/m_j (j ≠ i) over K. Write M_i(K) for the set of such points.
- Each M_i(K) has at most one point.
- The M_i(K) are pairwise disjoint.

*Proof.*
- F_x lies in the plane x^⊥. Because x ≫ 0, that plane contains no nonzero h ≥ 0 and no nonzero h ≤ 0. Let H_j := {h_j ≥ 0}.
- Every nonzero point of x^⊥ lies in one or two of the H_j.
- F_x is pointed. A single ray cannot meet all three H_j, so a non-visible x has a 2-dimensional F_x with extreme rays a and b. By V1, x is non-visible iff F_x meets every H_j, iff a and b together meet every H_j.
- Walk around the six sign sectors of x^⊥. Since F_x is an arc shorter than π, it then contains a whole closed "one-plus" sector, of sign pattern (+,−,−) up to permutation.
- That sector is bounded by two rays with h_i > 0: one with h_j = 0, h_k < 0, and one with h_k = 0, h_j < 0.
- The first ray lies in F_x iff m_i h_i + m_k h_k ≥ 0 on K with equality at x, iff x minimises m_i/m_k. The second likewise gives m_i/m_j.
- Uniqueness: the two minimiser sets lie on distinct lines through e_j and through e_k.
- Disjointness: minimising both m_i/m_j and m_j/m_i would make the ratio constant on K. ∎

CHECKED (`ratio_lemma.out`): 16 087 vertices of random polygons, compared with the P61 V3 normal-cone test. 0 mismatches.

**Decoupling.** For K = L⋆K₀ and x = ν(q⊙m) ∈ relint Δ, the ratio of ν(q′⊙m′) is (q′_i/q′_k)(m′_i/m′_k). Generators equal to e_j impose no constraint. So x ∈ M_i(K) iff q ∈ M_i(L) and m ∈ M_i(K₀). Hence:

  **ext K ∩ relint Δ ∩ nonvis = ⋃_i ν(M_i(L) ⊙ M_i(K₀)),  and so N(L⋆K₀) ≤ min(N(L), N(K₀)),**

where N counts the non-visible extreme points inside relint Δ.

CHECKED (`ratio_lemma.out`): the formula has 0 mismatches over 3 200 random polygons L, with 0 to 3 non-visible vertices, against 4 factors K₀ (cyclic triangles with t = 2 and t = 3, the holonomy-11/10 hexagon, a box). The histogram (N(L), N(L⋆K₀)) is always diagonal.

### 3.4 Consequence for n = 3 (PROVED)

**Corollary.** Let n = 3 and let L be a VB-type polygon with at most one non-visible vertex. Suppose L ∩ ∂Δ consists only of vertices of Δ; this is automatic unless π\* ∈ ∂Δ, because points of A_i other than e_i are interior. Then L⋆K₀ has at most one non-visible extreme point, and it is a polygon. So it is already in the VB class with one exempt point (P61 V6, O61 Thm C).

**Composition therefore adds no new n = 3 targets inside the open simplex.** In particular:
- For CC63(a) with n = 3 and interior factors, "at least two non-strictly-visible extreme points" is impossible.
- For CC63(c): an interior triangle with one or two cevian edges is a composed target only if at most one of its vertices is non-visible, and it is then already covered.

For non-polygonal L the pointwise count still holds. Uniform visibility of the remaining extreme points is not checked, so that case is a CONJECTURE.

### 3.5 Nearby result 1: exempt point on an edge of the simplex (PROVED; CHECKED)

Let π\* lie in the relative interior of the edge {m₃ = 0} of Δ, and let K₀ be full-dimensional.

**The face on that edge.**
- The only points of L with m₃ = 0 are π\* and possibly e₁, e₂.
- So K ∩ {m₃ = 0} is ν(π\*⊙K₀) together with possibly e₁, e₂.
- ν(π\*⊙K₀) = {ν(π\*₁m₁, π\*₂m₂, 0)} is a nondegenerate segment, because m₁/m₂ is not constant on K₀.
- So K has two extreme points with support exactly {1,2}.

**Not VB-type.** No VB(K′,A) with K′ ⊆ relint Δ has such an undominated target. Look at the generators of K(W0,β,α) on {m₃ = 0} with support exactly {1,2}:
- K′ gives none.
- A_ω gives only e_ω.
- Ŵ gives at most one, ν(β + αλe_ω), because no v_ω may carry a K′-component and β₃ = 0.

By P61 B′, sublinear vetoes add nothing. The target is also not orthant-planar, because R2's class lies in relint Δ.

**Covered.** Yes, by the composition theorem: O61 Thm C allows π\* ∈ ∂Δ, and Steps 1 and 7 are unaffected.

**Exact example** (`boundary_example.out`).
- K₀ is the cyclic triangle.
- L = conv{(1/2,1/2,0), (1/5,2/5,2/5), (1/5,3/5,1/5)}. The second vertex is visible from world 3 and the third from world 2.
- L′ = conv{points v + (v − e_j)/10, centre} ⊆ relint L.
- K is the pentagon with vertices (1/15,4/5,2/15), (1/13,8/13,4/13), (1/6,1/6,2/3), (2/3,1/3,0), (1/5,4/5,0).
- K′ ⊆ relint K.
- The pullback and exempt identities have 0 mismatches over 98 534 evaluations, including coordinate planes.

### 3.6 Nearby result 2: n = 4, interior (CHECKED exactly; search NUMERICS)

**Search** (`n4_search.out`). L is random with at most one non-visible vertex, and K₀ = ν([1,2]×[1,3]×[1,5/2]×[1,9/5]) is a normalised box, which is orthant-planar. In 83 accepted trials (12 with N(L) = 0, 71 with N(L) = 1), N(L⋆K₀) ranged up to 5 when N(L) = 1.

**Exact instance** (`n4_exact.out`).
- L = ν of (151,246,200,403), (192,406,172,229), (211,202,432,154), (350,136,79,435), (340,254,230,176).
  - L lies inside relint Δ.
  - Exactly one vertex is non-visible, so L is VB + exempt by V6.
- K = L⋆K₀ has 31 vertices and 32 facets, and lies inside the open simplex.
- **3 vertices are non-visible**, so K is not VB-type by V6.
- 6 facet normals have no zero coordinate. Each is then an extreme ray of cl D_K inside an open orthant, which rules out planarity there. So K is **not orthant-planar**.
- By the composition theorem K is exactly covered on U = D_{L′⋆K₀}.

**So** the composition class strictly enlarges the covered union in four worlds. The n = 3 collapse in §3.4 is special to three worlds: there the three "avoidance sectors" of the log-ratio chart partition the circle. Whether partially cevian or general-position *triangles* (n = 3) can be reached by any composition is answered negatively above for interior factors.

---

## 4. Orthant-map closure lemma (CORRECT; PROVED, CHECKED)

- c maps each closed orthant into itself, so e(c(h)) = a_σ⊙d_σ⊙h = c(e(h)), and the vectors a_σ⊙d_σ are ≫ 0.
- By Step 1 with Q = K_e, the composite's B_𝟙 is c⁻¹(D_{K_e}) = D_{K_e⋆K_c}. On σ it equals {(a_σ⊙d_σ)·h > 0}.
- So K_e⋆K_c ⊆ relint Δ is orthant-planar, with deciding vectors a_σ⊙d_σ, and the composite is R2's chart for it.
- ⋆ is commutative, so the composition is symmetric.

CHECKED (`closure_check.out`): cyclic⋆hexagon, cyclic⋆cyclic and hexagon⋆box are all orthant-planar, every edge line passes through a simplex vertex, and commutativity and B_𝟙 = D_P have 0 mismatches.

---

## 5. Points for the other roles and for the paper

- **CC63.** For n = 3 with interior factors, task (a) cannot succeed (§3.4). Use n ≥ 4 (§3.6, an exact instance is available) or an exempt point on ∂Δ (§3.5). For (b), §3.3 gives the n = 3 geometry exactly. For n ≥ 4, a geometric description of the non-visible points of L⋆K₀ is OPEN; the symmetric reach in §3.2(a) is a necessary condition.
- **W63.** State the theorem with the conjugacy proof (§2.8), the exact pullback (§2.1), and (LF) in the form L′⋆K₀ ⊆ relint(L⋆K₀). Do not claim new interior n = 3 targets.
- **Coverage map.**
  - New covered targets: composed targets in n ≥ 4, and n = 3 targets with a face ν(π\*⊙K₀) on an edge of Δ.
  - The reversed triangle remains excluded from every composed ranking (§3.2(c)). This is an exclusion of one construction, not of coverage.
- **Possible test case** (not settled here). Zero-support ε-contaminations are excluded from VB (P61 D3) and touch ∂Δ along a face. Whether they arise as composed targets in the sense of §3.5 is unchecked.
