# R18: referee report on R15_notes.md (13 Oct 2026)

I did not write R15, and I assumed nothing in it was correct until I had checked it.

**What I read.**
- Setting: BRIEF.md, BRIEF2.md (including the 13 Oct update), CCIBU.tex.
- Context: R1 §§1–3 (Prop 2.1 table, Prop 2.5, Prop 3.1, Lemma 3.5); R4 (Thm A, Thm B, Prop G1); R8; R10a (Thm R, Thm M); R10b (Prop V, (1.1), Lemma FS, Lemma UVN, Prop L); R12.
- FA (device, read-only): §§10–10.2, i.e. (10.1) facet maps, (10.2) box with its witnesses, (10.3) ray equations.

Every step of R15 was re-derived by hand. Verdicts: **CORRECT** / **CORRECT WITH REPAIR** (the statement stands after a local fix, given here) / **GAP** / **FALSE**.

**Scripts.**
- Rerun: `raysys.py`, `facing_check.py`, `t1_box_cert.py`, `pstar_invariance.py`, `polygon_lambda.py`, `sanity_gauge.py`, `inspect_opt.py`, and `vertex_box.py 450 21`. The last reproduces `vbox_21.out` exactly.
- Added in `r18py/`:
  - `facing_indep.py`: my own parametrisation of the all-facing corner system and of the closed-form Λ, independent of `raysys`;
  - `survivors_lambda.py`: the vertex-limit Λ for all 33 coarse-survey survivors.

---

## 0. Verdict table

| Item | Verdict |
|---|---|
| (SH) setting, Q, (1.1), strict signs of c | CORRECT |
| Hypothesis (DF): definition and role | CORRECT as a hypothesis. CORRECT WITH REPAIR in the surrounding claims (§1 "not implied by the axioms"; "hold in every known covered system"; §0 "one first-order hypothesis") |
| Lemma C (clusters) | CORRECT |
| Thm 1(a) facet linearity | CORRECT. Uses concavity in **h** only, plus two-sidedness of (DF) |
| Thm 1(b) unique clusters | CORRECT |
| Thm 1(c) crossing rows, λ > 0 | CORRECT (the case Γ_k w = 0 is trivial and should be said) |
| Lemma 3.2 (nonsingularity) | CORRECT |
| Thm 1(d) corner proportionality | CORRECT. Concavity in h gives the upper bound at the corner; no concavity in q is used anywhere |
| §4 chart forms (|C_k| = 3, 2) | CORRECT |
| Lemma 4.1 (target prior drops out) | CORRECT |
| §4 parameter count / "rigid" / "at most two fixed points" | CORRECT WITH REPAIR (dimension count only; add "unless the composed Möbius map is the identity") |
| Thm 5.1 ((·,3,3)) | CORRECT ("genuine measurable ray lemma" should read "ray lemma under (DF)+(ND)") |
| Prop 5.2 (T1 corner system, two admissible solutions) | CORRECT |
| §0 item 3 "false … even for smooth fields" | CORRECT WITH REPAIR (needs the one-paragraph construction given below) |
| Prop 5.3 (what concavity adds) | CORRECT WITH REPAIR (the formula γ_k = f/(𝟙·m\*_k) is gauge-mixture-specific; the rank-one conclusion holds in general by the argument below) |
| Λ_{ab} definition and strict signs | CORRECT WITH REPAIR (the cited UVN(b) route needs (NA_w); a hypothesis-free route is given; the nondegeneracy Γ_k w ≠ 0 at the b-crossings must be stated outside the |C_k| ≥ 2 case) |
| Lemma 6.1 (vertex-limit box via Lemma FS) | CORRECT (with the repair in the previous row) |
| (NA_w): role and necessity; (FD) ⇒ (NA_w) | CORRECT |
| "All-facing" definition and the equivalent form v_k ∈ int conv{e_k, v_i, v_j} | CORRECT |
| T1 and every interior ε-contamination are all-facing and in general position | CORRECT |
| Thm 6.2 (main conditional no-go), Steps 1–6 | CORRECT |
| T1: box ⇔ 1/κ ≤ x² ≤ κ; x + 1/x ≤ √κ + 1/√κ < κ+1; explicit certificate | CORRECT |
| Remark on NOGO/FA | CORRECT as labelled (CONDITIONAL). FA (10.1)–(10.3) checked on device: they match |
| §8 hexagon / 9-gon slack values (0.25 / 0.421 / 0.442) | CORRECT (hexagon also by hand) |
| §8 "box met with equality only in non-general position" (general) | GAP (proved only for all-facing triangles; elsewhere it is Conjecture R15) |
| §7 numerics | Reproduced, with two minor misreports: the (2,2,2) minimum is 1.2187, not 1.124; the p\* grid has 66 points, not 105 |
| Conjecture R15 | Correctly labelled. The evidence supports it, but the inequality is sharp (inf Λ_max = 1, not attained), and Lemma 6.1 needs an extra nondegeneracy at 1-crossing facets for the (1,2,3) class |
| §3 Remarks / §9 (E1) side claims ("sign changes at most once"; "zero set is a line") | Not verified. They are unproved remarks and nothing depends on them |

No use of (G) or (IB) outside M_L, and no silent all-model assumption. The only models built are evaluable models with advice in the advice ranges (B_q, D_{K_q}). Lemma FS is the decomposable-domain version.

---

## 1. Setting and hypothesis (DF)

**(SH).**
- R1 Lemma 3.5 gives R(g) ∩ Q = {c(g)·q > 0} ∩ Q for a.e. g ∈ U′ = D_{K′} ⊇ ∂D_T∖0.
- Globally, R(g) ⊆ {c·q > 0} whenever + and 0 are in the advice range. (LF) puts them there near ∂D_T (R10a §1 with the R12 shrink repair).
- c = ℓ(0) − ℓ(+) has the strict sign pattern of g by strict (G).
- R10b (1.1) holds for Fubini-good h.
- CCIBU supplies (LA), (S), (C). Its Lemma "efficient" makes the vertex models coherent, so R10b Prop V, V1 and Lemma FS are available.
- K_{p\*} = T, because D_T = B_{p\*} ≈ D_{K_{p\*}} and K ↦ D_K is injective. So P(p\*, h) = 0 on ∂D_T, which (DF) tacitly uses.

**(DF), role.** (DF) is the only bridge from p\* to the rest of the simplex. Its uses:
1. In Thm 1(a), two-sidedness gives D_{−δ} = −D_δ for the one-sided derivatives. Together with concavity of h ↦ P(q, h), this makes D_δ linear on each facet.
2. In Thm 1(b), it makes the essential cluster at each facet point unique, with zero line through p\*. That forces the crossing rows (c).
3. In Lemma 6.1, under (NA_w), a good gamble near a facet point has a *global* half-plane chart, whose normal converges to that unique cluster. This is how first-order data at p\* fix acceptance at edge priors near a vertex. The mechanism is legitimate.

(DF) is needed at every point of relint F_k, with no uniformity in h. It is not needed at the corner rays. Linearity in δ is part of the hypothesis and is used in (a) and (b). The statement is precise.

**Repairs to the surrounding claims.**
- §1 says "None of (DF), (ND), (NA_w) is implied by the axioms (§9)". Nothing in §9 proves independence. Replace with "not known to be implied".
- "All three hold in every known covered system" is verified, here and in R12, only for gauge mixtures. There:
  - (FD) holds;
  - (DF) holds because the normal cone of a vertex of S_{p\*} = Σ p\*_i M_i is the intersection of the summands' normal cones, so on relint facets the minimisers are unique and P(q, h) is differentiable in q.

  For the CSE boxes and the v19 LP realisations it was not checked. Say "in all gauge mixtures".
- §0 says the no-go holds "under one first-order regularity hypothesis at p\*". The theorem needs (DF) and (ND) at p\*, **and** (NA_w), a non-adjacency hypothesis on pairs near the six crossings at priors near the vertices. Item 6 lists all three, but the opening sentence understates them.

## 2. Lemma C and Theorem 1

**Lemma C. CORRECT.**
- For q ∈ A⁺(h): P(q, h_n) > 0, so q ∈ cl R(h_n) by (1.1), so ĉ(h_n)·q ≥ 0 because R(h_n) ⊆ {c·q > 0}.
- An open subset of a closed half-plane lies in the open half-plane, provided ĉ is non-constant on aff Δ.
- ĉ is non-constant because it has weak mixed signs, and ĉ ∝ 𝟙 would force ĉ = 0. The mirror argument handles A⁻.

**Thm 1(a). CORRECT.**
- For t > 0, φ_t = P(p\* + tδ, ·)/t is concave in h. This is concavity of the lower support function of K_{p\*+tδ}, valid for every family.
- For t < 0, φ_t is convex.
- Pointwise limits keep concavity and convexity respectively, so the limit is affine on the open 2-cone relint F_k ⊆ v_k^⊥. Positive homogeneity removes the constant.
- **Concavity of q ↦ P_{K_q}(·) is never used.** That map is not concave in general, and no step needs it.

**Thm 1(b). CORRECT.**
- Γ_k h·δ > 0 gives p\* ± tδ ∈ A^±(h), so ĉ·p\* = 0 and {Γ_k h·δ > 0} ⊆ {ĉ·δ > 0} on 𝟙^⊥.
- Two nonzero linear functionals on a 2-space with nested open half-planes are positively proportional.
- ℝ³ = 𝟙^⊥ ⊕ ℝp\* determines ĉ, and Cl(h) ≠ ∅ by density of good points and compactness.

**Thm 1(c). CORRECT.**
- If Γ_k w ≠ 0, uniqueness of the cluster and the two-sided weak signs give ĉ·e_i = 0. If Γ_k w = 0 the identity Γ_k w·(e_i − p\*) = 0 is trivial; the note should say so.
- v_k^⊥ ∩ e_i^⊥ = ℝw, so the functional is λ_{ik}h_i.
- Positivity: (ND) leaves a point h ∈ relint F_k with h_i > 0 off ker Γ_k. UVN(a) gives ĉ(h) ≥ 0 on V_i ∩ int Δ. A zero line through p\* and e_i would cut V_i, so ĉ·e_i > 0.

**Lemma 3.2. CORRECT.** Both cases are checked:
- If h₀ is not a crossing: e_i, e_{i′} and p\* would all lie on one line ℓ.
- If h₀ = w_{ik}: e_{i′} ∈ ℓ contradicts the strict positivity from (c).

**Thm 1(d). CORRECT.**
- Step 1 is a diagonal argument.
- Step 2 uses concavity **in h** along [r, h₀]: φ_t(x_θ) ≥ (1−θ)φ_t(r) + θφ_t(h₀). By linearity of Γ_k, limsup_{t↓0} φ_t(r) ≤ Γ_k r·δ for every θ.
- Step 3: two distinct unit vectors in p\*^⊥ admit δ with ĉ_k·δ < 0 < ĉ_j·δ. Then P(p\* + tδ, r) < 0, and Lemma C at r contradicts ĉ_j ∈ Cl(r).
- (DF) at r is not used.

**§4 forms. CORRECT.**
- c_k(h)·p\* = 0 and c_k(h)|_{𝟙^⊥} = Γ_k h.
- |C_k| = 3 gives μ_k ∝ v_k, i.e. c_k(h) = m_k h ⊙ v_k ⊘ p\* with m_k > 0.
- The |C_k| = 2 formula is correct.

## 3. Lemma 4.1 and §4 count

**Lemma 4.1. CORRECT.**
- ĉ := p\* ⊙ c maps p\*^⊥ onto 𝟙^⊥, with crossing rows λ ↦ μ = p\*λ.
- Proportionality and strict signs are preserved, and q ↦ (q/p\*)/Σ is a face-preserving bijection of Δ.
- Λ_{ab} is invariant: the factors p\*_b/p\*_a and p\*_a/p\*_b cancel between its two factors.
- `pstar_invariance.py` reproduces identical Λ_max (1.101393; and 3.797815 twice for T1) at five priors.
- The transfer is of the *first-order constraint system*, not of realisations. That is all the later arguments use.

**Count. CORRECT WITH REPAIR.**
- 4 entries per facet, minus 1 crossing condition per crossing, minus 1 scale per facet: 3 parameters against 3 corner equations.
- That is a dimension count. "At most two fixed points" needs "unless the composed Möbius map is the identity", and "rigid" should be "generically rigid".
- Nothing downstream depends on this: Thm 6.2 is proved directly.

## 4. §5

**Prop 5.2. CORRECT.** Recomputed by hand.
- T1 has v_k = b′𝟙 + εe_k with b′ = (1−ε)/3.
- F_1 = {h_1 = min, h·v_1 = 0}. On it h_1 < 0, and C_1 = {2, 3}.
- r_{12} = (−1, −1, κ+1) with κ = (1+2ε)/(1−ε).
- Normalising μ_{31} = 1 = μ_{12}: ĉ_1(r) = (a − (κ+1), −a, κ+1) and ĉ_2(r) = (−1, 1 − b(κ+1), b(κ+1)). Proportionality (positive factor 1/b) holds iff a + 1/b = κ+1.
- By R4 G1 (refereed CORRECT in R8), a = b = c ∈ {x₊, x₋}.
- The only non-crossing sign condition, evaluated at the two extreme rays of F_1, is 1/(κ+1) < a < κ+1. Both x₊ and x₋ = 1/x₊ satisfy it, because x₊ < κ+1.
- `raysys.py` reproduces x± to about 1e-14.

**§0 item 3 ("false even for smooth fields"). CORRECT WITH REPAIR.** What is proved is that the first-order corner system is consistent. To conclude that Thm R fails without concavity, one needs a field satisfying R10a's (i) and (ii). It exists:
- On F_k put f(h) = θ(h)c_k(h), where θ > 0 is continuous and chosen so that the pieces agree at the corners. Proportionality (d) makes this possible.
- Then Σp\*_i f_i = 0 on ∂D_T, and the sign conditions give (i).
- Two smooth functions on transversal planes that agree on their common line extend smoothly.

Add this paragraph.

**Prop 5.3. CORRECT WITH REPAIR.** "γ_k(h) = f(h)/(𝟙·m\*_k)" refers to the vertex of S_{p\*}, i.e. to gauge mixtures. For an arbitrary concave representative f with Σp\*_i f_i = 0 on ∂D_T, the rank-one conclusion holds as follows:
- f is linear on F_k (R10a Thm R, step 2).
- By (b), Γ_k h ∝₊ f(h)|_{𝟙^⊥} for each h.
- Γ_k is nonsingular (Lemma 3.2). Two linear maps on a 2-space that are pointwise positively proportional differ by a constant, so Γ_k = θ_k f|_{F_k}.
- Hence λ_{ik} = θ_k α_i.

For T1 this gives abc = 1 and α_1 + α_2 = (κ+1)α_3 cyclically, so κ = 1. That part is correct.

**Thm 5.1. CORRECT.**
- Lemma 3.2 gives Γ_k r, Γ_j r ≠ 0.
- r ⊙ v_k ∝ r ⊙ v_j with r_i ≠ 0 gives v_k = v_j.
- The numerics agree: no (0,3,3) solutions in any run.

Wording: this is a ray lemma under (DF)+(ND), not a "genuine measurable" one.

## 5. The box (Lemma 6.1)

**Definition of Λ_{ab}.**
- In the plane h_b = 0, D_T contains e_a and e_c in its interior, so its two boundary rays lie in opposite open quadrants.
- These rays are the two b-crossings, on the two distinct tangent-vertex facets.

**Strict signs: CORRECT WITH REPAIR.** The note derives them "as in (c), using UVN(a) and UVN(b)".
- c_k(w)_a > 0 follows from UVN(a) exactly as in (c).
- For c_{k′}(w′)_a < 0, UVN(b) only says R(h) ∩ V_a = ∅. That bounds R(h), not c(h), unless the chart is a full half-plane, i.e. under (NA_w). Since Lemma 6.1 assumes (NA_w) the route is valid, but there is a hypothesis-free route:
  - if Γ_{k′}w′ ≠ 0, the unique cluster at the b-crossing w′ has ĉ·e_b = 0 and ĉ·p\* = 0, so its zero line is line(p\*, e_b), which does not contain e_a;
  - the weak sign ĉ_a ≤ 0 then becomes strict.
- **Nondegeneracy must be stated.** Λ needs Γ_k w ≠ 0 at both b-crossings.
  - This is automatic when |C_k| ≥ 2 (Lemma 3.2), so it holds throughout Thm 6.2.
  - It is **not** automatic for the 1-crossing facet of a (1,2,3) triangle: a rank-one Γ_k with kernel at its crossing is not excluded. This matters for Conjecture R15 and the (1,2,3) numerics only.

**Proof steps. CORRECT.**
1. Step 1: c_{k′}(A)·q₀ = s c_a + (1−s)λ_{bk′}A_b. The acceptance threshold is as stated.
2. Step 2: the mirror computation.
3. Step 3: the product of the two ratio bounds is *exactly* s-independent at first order; the (1−s)/s factors cancel. The limit s → 0 is needed only to send A → w′ and B → w. A λ with (A+λB)_a, (A+λB)_b < 0 exists iff (|A_a|/A_b)(|B_b|/B_a) > 1.
4. Step 4:
   - Cl(A) = {ĉ(A)} gives uniform convergence ĉ(h′) → ĉ(A) over good h′ → A.
   - (NA_w) makes each R(h′) ∩ int Δ the full half-plane, so for all interior q near q₀ (where ĉ(A)·q₀ > 0), a.e. h′ in a ball around A lies in B_q ≈ D_{K_q}.
   - The open convex cone then contains the ball, so A ∈ D_{K_q}.
5. Step 5: R10b Lemma FS with S = {a, b} (refereed CORRECT in R12; valid on decomposable domains under (LF) and vertex coherence).

**Role of (NA_w). CORRECT.**
- Without non-adjacency, a d-face between the region near p\* and q₀ can cut the witness charts. This is exactly R4 Prop G2's mechanism. So the hypothesis is genuinely used, and it is localised correctly (pairs near the six crossings, at interior priors near q₀).
- (FD) ⇒ (NA_w) by R4 Thm B, together with Thm A(ii), the R1 table, and (LF) excluding the advice ranges {+}, {−}, {0} and {+,−}.
- §9 (E4)'s identification of the escape is right: d-face priors with K_p ⊆ h^⊥ ≈ line(e_b, v_k). Its clause "impossible near e_b unless K_{e_b} ⊆ line(e_b, v_k)" holds only for d-faces that accumulate at e_b (V2 continuity). Read it that way.

**FA cross-check.**
- FA (10.1) has M_1g = (−(g_2 + x_1g_3), g_2, x_1g_3), so FA's x_k equals R15's (a, b, c) inverted (x_1 = 1/a, x_3 = 1/c).
- FA's box 1/κ ≤ x_i x_j ≤ κ is then equivalent to R15's six inequalities Λ ≤ 1.
- FA's witnesses also sit at q₀ = (1, t, 0) with t → 0, a vertex limit.

## 6. All-facing triangles and Theorem 6.2

**Definition. CORRECT.**
- h_k < 0 on F_k∖0 ⟺ e_k − v_k ∈ −int(tangent cone of T at v_k). Equivalently, the ray from e_k through v_k enters int T. Equivalently, v_k is a strictly positive combination of e_k, v_i, v_j.
- The condition implies C_k = {i ≠ k}, since each coordinate crosses on exactly two facets.

**Contamination. CORRECT.**
- For T = (1−ε)p₀ + εΔ, the edge line through v_i, v_j has k-coordinate (1−ε)p₀_k > 0, so it misses e_i and e_j.
- Hitting e_k would need (1−ε)(p₀_i + p₀_j) + ε = 0, which is impossible. So T is in general position.
- v_k ∈ (p₀, e_k) with p₀ ∈ int T, so T is all-facing. T1 is the case p₀ = u.

**Thm 6.2. CORRECT.** Every step was recomputed.
- (6.1): ĉ_a(r) = (A − s, s, −A) and ĉ_c(r) = (−tB, 1, tB − 1) in (a, b, c) coordinates. They are proportional, with positive factor s, iff A/s + Bt = 1.
- (6.2): r ⊥ v_a and r ⊥ v_c.
- Λ_{ab} = st·v_{ac}/v_{aa} and Λ_{cb} = (v_{ca}/v_{cc})/(st). These use |w′_a|/w′_c = v_{ac}/v_{aa} on F_a and |w′_c|/w′_a = v_{ca}/v_{cc} on F_c.
- (6.3) and (6.4) follow from monotonicity in s and (6.2).
- Pinching: (6.4) for the triple (b, c, a), at corner r_{ab}, gives ρ_a(b:c) ≥ v_{ab}/v_{ac}. (6.3) gives ≤. All-facing is invariant under relabelling, so this is legitimate.
- Step 6: t = v_{aa}/v_{ab} = v_{ca}/v_{cb}, i.e. the minor v_{aa}v_{cb} − v_{ab}v_{ca} = ±det(v_a, v_c, e_c) = 0. That puts e_c on line(v_a, v_c), contradicting general position.
- Labelling collision: the corner constants A, B clash with the witness names A, B of Lemma 6.1. Cosmetic.

**Independent numerical check (`r18py/facing_indep.py`, own code).**
- 2029 all-facing general-position triangles: half contamination triangles with random baseline and ε, half random.
- 971 had one sign-admissible solution and 1057 had two.
- min Λ_max = 1.186; none ≤ 1.

**T1. CORRECT.**
- v_{13}/v_{11} = b′/(b′+ε) = 1/κ, so Λ_{12} = ac/κ. With a = b = c = x the six values are x²/κ and 1/(κx²).
- The box gives x² ∈ [1/κ, κ], hence x + 1/x ≤ √κ + 1/√κ.
- With y = √κ: (κ+1) − (y + 1/y) = (y−1)(y²+1)/y > 0 for ε > 0.
- The explicit certificate was verified:
  - A ∈ F_1 and B ∈ F_3 (facet equations checked);
  - acceptance thresholds s < xη/(1+2xη) and ζ < xs/(1−s);
  - feasibility η < βζ(1+η), which in the limit needs βx² > 1.
- x₊²/κ = 1.90, 2.34, 3.80, 7.31, 29.96 at ε = .05, .1, .3, .6, .9 (recomputed).

## 7. §8 and the numerics

- **Gauge polygons.**
  - Hexagon by hand: the b-crossing is w = (4, 0, −1), with f_a(w) = u·w = −w_c, so f_a(w)/w_a = 1/4; w′ = (−1, 0, 4) gives factor 1. So Λ = 1/4.
  - `polygon_lambda.py` reproduces 0.25 / 0.4211 / 0.4417, and `sanity_gauge.py` reproduces 0 violations.
  - This is a genuine sanity check: a reversed inequality would fail on these realised systems.
- **§8 item 3. GAP as a general claim.** "The box can be met with equality only in non-general position" is proved only for all-facing triangles (Thm 6.2). For the (1,2,3) and non-facing (2,2,2) classes it is Conjecture R15. Item 2 (why polygons escape) is a heuristic and should be labelled so.
- **§7 table.**
  - Random survey: 1340 triangles passed the filter (446 + 447 + 447). (1,2,3): 562 solutions, min Λ_max = 1.0045, reproduced. (2,2,2): 336 solutions, but the min Λ_max in the three output files is **1.2187** (seeds 21/22/23: 1.2263 / 1.3887 / 1.2187), not 1.124.
  - The T1 p\*-scan grid has **66** points, not 105. Its result (always two solutions, both violating the box) is reproduced.
  - Coarse survivors: I computed the vertex-limit Λ_max for all 33 (`r18py/survivors_lambda.py`). All exceed 1 (min 1.0041). This confirms the note's verdict that they are sampling artefacts. (margins.out's 0.9996 is a grid underestimate of the sup.)
  - Optimiser: `inspect_opt.py` shows the minimisers are (1,2,3) triangles with three Λ's ≈ 1 and normalised |det| down to 4e−5. That is consistent with the note.
- **Conjecture R15.** Correctly labelled. Caveats the note should state:
  1. inf Λ_max = 1 over general-position triangles, not attained, so any proof must be sharp. The (2,2,2) margin (≥ 1.19 in both my all-facing sample and theirs) is much larger than the (1,2,3) margin (≥ 1.004).
  2. For (1,2,3), Lemma 6.1 needs the nondegeneracy Γ_k w ≠ 0 at the 1-crossing facet. The solver normalises |t| = 1 and would not detect a singular branch.
  3. The numerics test only the first-order constraint system. They say nothing about the escapes (E1)–(E4).

## 8. Requested edits, in priority order

1. §0 opening and item 6: state that the no-go is conditional on (DF), (ND) **and** (NA_w) (or (FD)), not on "one first-order hypothesis".
2. Lemma 6.1: add "Γ_k w ≠ 0 at both b-crossings (automatic if |C_k| ≥ 2)". Replace the UVN(b) justification of c_{k′}(w′)_a < 0 by the line(p\*, e_b) argument, or note that it uses (NA_w).
3. §8 item 3: restrict "met with equality only in non-general position" to the all-facing class, or cite Conjecture R15.
4. §7: correct the (2,2,2) minimum (1.2187) and the grid size (66).
5. Prop 5.3: replace the gauge-specific formula by Γ_k = θ_k f|_{F_k} with the nonsingularity argument.
6. §0 item 3 / Prop 5.2: add the smooth-field construction, or say "the first-order corner system is consistent".
7. §1: "not known to be implied"; "hold in all gauge mixtures".
8. §4: "generically rigid"; Möbius "unless identity". Thm 5.1: drop "genuine measurable".
9. Thm 1(c): add the trivial Γ_k w = 0 case. §6: rename the corner constants A, B.
10. Mark the §3 remark "sign changes at most once" and §9 (E1)'s "zero set is a line" as unproved heuristics.

**Net assessment.** The mathematics of R15 is sound. Theorem 1, Lemma 4.1, Prop 5.2, Thm 5.1, Lemma 6.1 and Thm 6.2 are correct as stated under their hypotheses, with only local repairs. The main theorem is a genuine conditional no-go for T1 and for every all-facing general-position triangle (all interior ε-contaminations included), at every interior p\*.

Its value is bounded by three hypotheses that are not derived:
- (DF), in particular oddness in δ;
- (ND);
- (NA_w).

Deriving these is the open problem, exactly as §9 states.
