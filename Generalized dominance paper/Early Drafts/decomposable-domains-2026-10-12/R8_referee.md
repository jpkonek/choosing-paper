# R8: referee report on R4 and R5 (round 9, 12 Oct 2026)

Scope: every PROVED or CHECKED item in R4_notes.md and R5_notes.md on the priority list. Each proof was checked line by line against BRIEF.md: decomposable domains, (G) and (IB) applied only inside M_L, and (LF) at the target only. R1, R2, R3 and R6 were read for context.

Sources opened:
- GD: v3 (labels thm:general, lem:local-independence, eq:independence, thm:additive-obstruction, lem:bayes-necessary); CCF (sec:cp, thm:SW, lem:Pd (i)–(iv)).
- CPM: CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md (§2).
- Device, read-only: CPM/TRIANGLE_A0_A1_NOGO_FIXED_ANCHORS.md (FA §§9–10) and CPM/TRIANGLE_A0_A1_PROJECTIVE_BOUNDARY.md (PB Lemma 3.1, Thm 3.2).

All three r4py scripts were rerun and reproduce the reported output. One referee script was added: `r8py/exE_fneg.py`.

Verdict scale: CORRECT / CORRECT WITH REPAIR / GAP / FALSE.

---

## Summary table

| Item | Verdict |
|---|---|
| R4 Thm A (adjacency dichotomy) | CORRECT ("any n" applies to (i)/(ii); the wedge clause is an n = 3 notion) |
| R4 Thm B | CORRECT |
| R4 Cor B1 | CORRECT |
| R4 Cor B2 (the reduction step) | CORRECT (one remark: charts are only identified on int Δ) |
| R4 Remark B3 | CORRECT WITH REPAIR (the parenthetical on the advice range {0} on U′∖cl D is false) |
| R4 Lemma S | CORRECT |
| R4 (H1⁺): openness of N′, extension of Thm B | CORRECT (homogeneity used tacitly) |
| R4 Thm C | CORRECT |
| R4 Lemma C2 | CORRECT |
| R4 Cor C3 | CORRECT (as a conditional) |
| R4 Prop D (CHECKED) | GAP: the dichotomy "constant or injective" is only illustrated by an example |
| R4 Prop F (CHECKED) | CORRECT given D's projective form. The "no precise ring" corollary needs "non-constant" |
| R4 Prop G1 | CORRECT |
| R4 Prop G2 (CONDITIONAL) | CORRECT as a conditional; matches FA §10.1 |
| R4 §9 item 4 (edge blow-up, CHECKED) | CORRECT |
| R4 Example E | CORRECT WITH REPAIR. The headline "(G) fails unless f ≡ 0" is FALSE as worded; the correct statement is "unless f ≤ 0, i.e. unless K_p ≡ {p}". The second bullet's derivation is invalid |
| R4 §8 (K1), (K2) | CORRECT |
| R4 §8 (K3) = transfer of B1 | CORRECT WITH REPAIR (positive case: acceptance of x⁻ near e_i needs a short measure argument) |
| R4 §8 (K4) = FA forbidden-support step | CORRECT (all-model domain, as stated) |
| R5 Lemma N1 | CORRECT ("same for b" uses the mirror pattern) |
| R5 Lemma TJ | CORRECT |
| R5 definition of "sandwiched" | CORRECT (consistent; covers unanimity of strictly guiding losses) |
| R5 Thm UN | CORRECT. Its "in particular K_A ⊂ int K_B" clause needs R6's repair (interior relative to aff Δ). The summary claim that UN "closes R2's uncountable unanimity case" needs one extra step, supplied below |
| R5 Lemma X | CORRECT |
| R5 Prop X2 (CHECKED) | CORRECT |
| R5 Lemma 4.1 | CORRECT |
| R5 Prop 4.2 | CORRECT |
| R5 Example 4.3 | CORRECT (arithmetic verified; 0 is undominated; no F-supporting prior) |
| R5 Lemma 4.4 | CORRECT |
| R5 Thm PC | CORRECT |
| R5 Thm UN′ | CORRECT |
| R5 Thm R_n (CHECKED) | CORRECT WITH REPAIR (the "Equivalently" diagram reformulation needs per-prior quantifiers; the boundary-tie gap is acknowledged) |

No use of (G) or (IB) outside M_L was found in either note, and no silent all-model assumption. Details are in the last section.

---

## R4

### §1 notation
The sign facts check out. At i ∈ P(g), ℓ(+) < ℓ(0) < ℓ(−), so c_i > 0, c′_i < 0 and d_i = c_i + |c′_i|. At i ∈ N(g) the mirror holds. Hence |d_i| > max(|c_i|, |c′_i|).

R(g) = {c·p > 0, d·p > 0} is the unique-minimiser region. F(g) is a relatively open convex piece of the d-line.

### Theorem A: CORRECT
- Exclusivity holds.
- "Not (i) ⇒ (ii)":
  - y ∈ R(g) ∩ int Δ exists because R(g) is open and contains δ_i (vertex property).
  - For x ∈ int Δ with α(x) > 0 and x ∉ R(g), we get d(x) < 0, since d(x) = 0 would put x in F(g).
  - The segment [x, y] stays in the convex set {α > 0} ∩ int Δ, and d changes sign on it. The zero is a point of F(g) ∩ int Δ.
  - The mirror argument uses δ_j ∈ R(−g) for j ∈ N(g).
- {+, −}: d has the strict sign pattern of g, so the d-line separates vertices and meets int Δ.
- Wedge clause: α is not constant on the d-line unless the three lines coincide. R1's "apex" is a point only when n = 3, so the "any n" label applies to (i)/(ii) and not to the wedge sentence. Cosmetic.
- dichotomy.py rerun: {adj 2699, split 1301, viol 0}.

### Theorem B: CORRECT
- Fubini on (p, h) is legitimate: R(h) is defined by measurable data, and P is jointly continuous. Applying it to h and −h gives a co-null set of pairs.
- Positivity a.e. on the open set R(g) ∩ int Δ gives P(·, g) ≥ 0 on its closure.
- A point of F(g) ∩ int Δ is in cl R(g) ∩ cl R(−g). This needs d to be non-constant on aff Δ, which holds because d is mixed.
- Hence K_p ⊆ g^⊥, and the closure statement follows from Hausdorff continuity.
- dim ≤ n−2 holds because g is not ∝ 𝟙.

### Corollary B1: CORRECT
(H0) already excludes the advice range {+, −} and the singleton advice ranges. With (H2″), Thm A turns the charts for the advice range {+,0,−} into {c(h)·p > 0} on int Δ, and c(−g) = c′.

The uniform-in-q statement B_q ∩ V ≈ {q·c(h) > 0} follows because the exceptional set of h does not depend on q.

The last sentence (full-dimensional K ⇒ (H2″)) follows from Thm B.

### Corollary B2: reduction CORRECT (conditional on NOGO + PB + FA, as labelled)
Cor B1 supplies exactly what R1 Thm 4.2 took from (H2): half-plane charts with c sign-preserving on U′.

One remark. Cor B1 identifies charts only on int Δ. On ∂Δ a split chart can differ from {α > 0} only at the single point where the d-line meets each edge, since d·δ_i ≠ 0. The NOGO/PB/FA arguments evaluate maps only at interior priors (FA §10.1: "No map is evaluated at a boundary prior"; PB uses q_s ∈ int Δ). So this is harmless, but it should be said.

### Remark B3: CORRECT WITH REPAIR
- The main point is correct. (LF) excludes the advice ranges {+} and {0} near ∂D∖0, but FA §10.1's forbidden-support step works at z′ = a+λb, a sum of points on two different facets, so generically in int D. The advice range {+} (every evaluable model accepts) near z′ would void that step. Cor B2 therefore rightly adds (H0)_{U′}.
- Repair: drop the parenthetical about the advice range {0} on U′∖cl D. By R1 Prop 2.5, U′ ⊆ W a.e., and W ≈ Av∖{h ≤ 0} (Prop 2.4(i)). So acceptance is in the advice range at a.e. h ∈ U′, and the advice range {0} (every evaluable model gives no advice) cannot occur on a non-null subset of U′.

### Lemma S: CORRECT
- Classes: a rational τ crossing J transversally within len(J)/4 of its midpoint puts the 1/m-segment around x_J inside J.
- Law of sines: |x_J − z| ≤ δ/sin φ. If sin φ > mδ, then z lies in both J and J′.
- So |θ_J − θ_{J′}| ≤ (π/2)mδ, and r = x_J·n(θ_J) is Lipschitz too (τ is bounded).
- The image of a subset of a segment under a Lipschitz map has H¹ σ-finite, hence 2-dimensional measure zero (outer measure, so no measurability issue). Countably many classes.

### (H1⁺), openness of N′, extension of Thm B: CORRECT
- The continuous representative has weak signs. Still, d ≠ 0 and d is non-constant on aff Δ: c = c′ would force c = c′ = 0, contradicting normalisation, and d ∝ 𝟙 is impossible with weak mixed signs. So the d-line is a genuine line and F is lower semicontinuous. As in R1's (H1), the zero-coordinate set can be added to S.
- Tacit point: working in the 2-dimensional projective space of pairs (Thm C) uses that chart data are degree-0 homogeneous. This holds a.e. because interior Bayes models are cones (B_p ≈ D_{K_p}). It then holds everywhere on U′∖S by continuity, since S is a cone. In any case, working in ℝ³ gives fibres of dimension ≤ 1, and Hurewicz still yields dim ϑ(D) ≥ 2.

### Theorem C: CORRECT
- N″ is open: diam K_p is continuous and F is lower semicontinuous.
- Fibres of ϑ are countable:
  - g ↦ ℓ_g = g^⊥ ∩ aff Δ is injective on projective classes (the line spans g^⊥), and g, g′ ∈ H are never antipodal.
  - So the sets F(g)∖Z_pt for g in one fibre are pairwise disjoint, nonempty, relatively open subsets of one line.
- Hurewicz's closed-map inequality applies to compact metric D (Engelking 1.12.4).
- A 2-dimensional subset of a 2-manifold has interior (Hurewicz–Wallman IV.3).
- The family J_L is pairwise disjoint by the same ℓ-argument, so Lemma S makes Λ null. Contradiction.
- Theorem C needs Thm B at **every** g ∈ D; the extension paragraph provides this.

### Lemma C2: CORRECT
- On int S(g), P(·, g) ≤ 0 ≤ P̄(·, g) for a.e. g, by Fubini and continuity.
- At precise points this gives σ(p)·g = 0, where σ is continuous on the relatively closed set Z_pt.
- Fubini then gives λ(Z_pt ∩ int S(g)) = 0.
- The density-point corollary uses a sector of positive angle.

### Corollary C3: CORRECT (conditional)
- If N′ = ∅, then (H2″)_{U′} holds a.e., because a.e. pair has actual chart = continuous representative.
- (H1⁺) gives (H1) after adding the closed null cone {c = 0} to S. Then Cor B2 applies.
- Otherwise Thm C applies.
- "No non-degenerate segment in Z_pt ⇒ no realisation" holds because F(g) ∩ int Δ is a nonempty relatively open subset of a line.

### Proposition D (CHECKED): GAP
1. **The dichotomy step is unproved.** "(G)-signs exclude non-injective degenerate maps" is supported only by one example (σ depending on p₁ alone). Non-constant non-injective σ is not excluded: a 1-dimensional image, folds, or partial plateaus.
   - The pattern argument can be made to work when σ(O) is a curve whose fibres are segments. For each m ∈ σ(O), every h ⊥ m shares one d-line, so d_h ∝ ±d(m). But m^⊥ (m > 0) meets all 6 mixed orthants, while ±d(m) and its small perturbations realise at most 4 patterns.
   - No general argument is given.
2. **Injective case: essentially right, but one step is missing.** To apply the local fundamental theorem one needs σ^{-1}(ℓ_h) ∩ O ⊆ L_h (up to the degenerate silence set) for an open set of h. This follows from invariance of domain: σ is open, so σ(R(h) ∩ O) ⊆ {m·h > 0} strictly. That point should be written. The diagonal step (Aᵀ(e_i × x))_i = det(e_i, x, Ae_i) = 0 for x in an open set ⇒ Ae_i ∥ e_i is correct.
3. **Repair:** state D for σ injective on O (or a local homeomorphism). Leave "non-constant ⇒ injective" as a CONJECTURE, or prove it.

### Proposition F (CHECKED, given D): CORRECT given D's projective form; corollary over-stated
- The argument is correct:
  - every line L′ near L is L_h for a unique pair h = v/w (componentwise);
  - for good h the two sides near o₁ and o₂ lie a.e. in R(h) and R(−h), so these chord pieces lie in cl F(h);
  - convexity of F(h) carries the chord across to a point p′ near p_f;
  - Fubini over (point, direction) gives two good lines through a.e. p′, so K_{p′} is a singleton;
  - continuity of diam K transfers this to p_f.
- Because F needs D's projective form, it inherits D's gap.
- The sentence "there is no precise boundary ring around a full-dimensional core" holds only for **non-constant** σ. A constant precise region (K_p ≡ {m₀}) is untouched by F: its charts are one-sided on O, and its d-faces are null in h.

### Proposition G1: CORRECT
- x₂ = T³(x₂), with T the Möbius map of [[s, −1], [1, 0]], s = κ+1 > 2. T is hyperbolic with multiplier μ² ≠ 1, so T³ ≠ id has exactly T's two fixed points.
- x₊ > √κ because (κ+1) − (√κ + 1/√κ) = (κ+1)(1 − 1/√κ) > 0, and x + 1/x is increasing on (1, ∞).
- Matches FA:
  - box (10.2): 1/κ ≤ x_i x_j ≤ κ;
  - rays (10.3): identical equations;
  - κ = 1 + ε/b_i with b_i = (1−ε)/3, i.e. κ = 1 + 3ε/(1−ε) (NOGO §2, eq. (2.1)).
- G1 is consistent with, and sharper than, FA's own conclusion (box + (10.3) ⇒ x ≡ 1 ⇒ κ = 1).
- Minor numerical misreport: ray_box_cap.py's grid scan finds only x₊ for ε ≥ 0.2. Its residual filter discards the repelling fixed point x₋. §9 item 3's sentence "Only x₊ and x₋ solve T³x = x (grid scan)" overstates the scan. The theorem itself is proved.

### Proposition G2 (CONDITIONAL): CORRECT as a conditional
- FA §10.1 was checked:
  - the witnesses a ∈ F₃ and b ∈ F₂ at q₀ = (1, t, 0) and q_η = (1, t, η);
  - a+λb has negative coordinates 1 and 2, which is exactly supp q₀;
  - "If q·M_F w > 0 ... w ∈ C_q" is FA's (9.3)-based fact, used as "α_h(q_η) > 0 for h → a from D".
- Under a split chart, α_h(q_η) > 0 forces acceptance a.e. near a. A non-null set of adjacent pairs near a (or near b) follows.
- The caveat on B1 is appropriate.

### §9 item 4 (edge blow-up, CHECKED): CORRECT
I recomputed it. With h = (tz, κ, −1), M₃h = (tz, x₃κ, −(tz + x₃κ)) and p = e₁ + ty, one gets p·M₃h = t[z + x₃κ(y₂ − y₃)] + O(t²). The same holds for M₂.

The thresholds ω ≤ x₃ and ω ≥ κ/x₂ follow from R(h) ⊆ {α > 0}. The witnesses rescale to z = −κx₃ and z = κ/x₂. Both are cut iff ω ∈ [κ/x₂, x₃], which is nonempty iff x₂x₃ ≥ κ. This is first order in t, as stated.

### Example E: CORRECT WITH REPAIR (the headline is FALSE as worded)
- Correct parts:
  - P_{K_p}(h) = (1−ε)[p·h + (f·p)⁺ m];
  - d = (M + |m|) p·h;
  - both case analyses for R(h) and for R(−h) (I redid them);
  - concurrency at {p·h = 0 = f·p};
  - d-face ⊆ {f·p < 0} (precise).
- **Error.** The (G) test is applied to the particular vectors c = M(h + mf) and c′ = −|m|(h + Mf). The chart determines (c, c′) only where the corresponding boundary line is visible in Δ.
  - At i ∈ N(h) the sign of c_i is invisible: δ_i already lies in R(−h).
  - The second bullet (h_i → 0⁻ ⇒ f_i ≥ 0) is therefore not a valid deduction.
  - Counterexample to the stated conclusion: f = (−1, −1, −1). Then (f·p)⁺ ≡ 0, so K_p ≡ {p}, the precise identity model. This is (G)-realisable (c = h, c′ = −h). Yet f ≠ 0, and R4's (c, c′) test flags 100% of mixed h (`r8py/exE_fneg.py`).
- **Repair (representation-free).**
  - The vertex property needs R(h) to contain a neighbourhood of δ_i for i ∈ P(h).
  - Near δ_i, P ∝ h_i + f_i⁺ m. If f_i > 0, this is < 0 for 0 < h_i < f_i|m|, which is a non-null set of h.
  - Hence f_i ≤ 0 for every i, i.e. (f·p)⁺ ≡ 0 on Δ and K_p ≡ {p}.
  - Correct statement: "the family is (G)-realisable iff f ≤ 0, iff K_p ≡ {p}."
  - The moral (only the precise model survives) is unchanged.

### §8 (K1): CORRECT
- Under (H0) + non-adjacency on U′, for h ∈ U′∖Bad: good h_k → h have half-plane charts.
- A limit in measure of normalised half-planes is {v·p > 0} ∩ int Δ.
- The limit normal is determined, because the good charts' lines cross int Δ, so ĉ is continuous relative to U′∖Bad.
- The sign claims follow from continuity of P.

### §8 (K2): CORRECT
- Forward: q′·v ≥ 0 on a neighbourhood of an interior q forces q·v > 0, because an affine function with an interior local minimum 0 on aff Δ vanishes identically, and |v| = 1.
- Converse: compactness of U(w) gives q·ĉ > 0 on B(w, r)∖Bad, hence P(q, ·) ≥ 0 on a dense subset of the ball, hence on the ball. Since int{P ≥ 0} = {P > 0} ⊆ D_{K_q}, the claim follows.

### §8 (K3) (PB Lemma 3.1, Thm 3.2 → B1): CORRECT WITH REPAIR
Checked against PB Lemma 3.1.

- **Positive case.** "x⁻ accepted near e_i by the vertex property and openness of R(x⁻)" cannot be taken literally: charts are defined only for a.e. h. Repair:
  - For a small ball N around x⁻ (with h_i > 0 and acceptance in the advice range on N), dominated convergence gives μ(N ∖ D_{K_q}) → 0 as q → e_i, because each R(h) is open and contains δ_i.
  - A convex cone containing all but a small fraction of a ball contains its centre, indeed a smaller ball. So x⁻ ∈ D_{K_{q_s}} for small s.
  - The rest uses only R(g_n) ⊆ {α > 0}, so it holds for adjacent g_n too: {α < 0} is open and misses R(g_n), so P(q_s, g_n) ≤ 0 by Fubini and continuity. That part is right.
  - That acceptance is in the advice range near x⁻ needs (H0) or the all-model domain. §8 assumes (H0).
- **Negative case.** Correct on split pairs. One implicit step: "P(q_s, ·) ≤ 0 near x⁺ ⇒ x⁺ ∉ C_{q_s}" uses P(q, x⁺ + δ𝟙) = P(q, x⁺) + δ.

### §8 (K4): CORRECT (all-model domain)
- At q₀, accepting h with h_S > 0 is strictly best. R(h) is open, so h ∈ B_{q_η} for small η. This holds for a.e. h and every η, since the q_η form a countable family.
- Hence every limit point K* ⊆ Δ_S, and max_{K_{q_η}} m·z < 0 uniformly near z′ (Hausdorff compactness).
- This matches FA's forbidden-support observation with S = supp q₀ = {1, 2}.
- On a decomposable domain it needs + in the advice range for a.e. h with h_S > 0. R4 restricts it to the all-model domain correctly.

---

## R5

### Lemma N1: CORRECT
- The tie-transfer of competitiveness and the unchanged sections are correct.
- Interiority for a: σ = − exactly on supp a; silencing A on R_σ is a strict improvement at every world of supp a.
- "Same for b" is the **mirror** argument, not the same one: take σ = + exactly on supp b and switch B to A's acceptance on R_σ. This works.

### Lemma TJ: CORRECT
- Lyapunov halving and m(S₀) = m(S₁) = ½m(Z) = 0 check out.
- (C) puts both splices in C_L.
- Both ray cases were rechecked. Positive radial density makes ρ^< and ρ^≥ non-null.

### Sandwiched (definition) and Theorem UN: CORRECT
- Step 0: N1's interiority argument does not depend on which alternative of N1 holds.
- Step 1: the attainable set of a pairing vector is convex and compact (Aumann, integrable envelope). Separation gives p ≥ 0.
- Step 2: the strict sign of c in each pairing is where strict guidance of every θ_i is used.
- Steps 3–5: Step 4's use of (R) at j and (W) elsewhere, with p^{θ*} interior, is correct. E ∈ M because it is a splice.
- (IB) is not used; only strict (G) is used, in Step 0.
- **Repair 1:** "In particular no D_{K_A}, D_{K_B} ∈ U_L with K_A ⊂ int K_B" inherits R2 Thm N's sufficiency clause, which R6 found FALSE as worded (n = 2, K_A = [0, ½], K_B = [0, ¾]). Read int relative to aff Δ.
- **Repair 2 (summary claim).** "Closes R2's uncountable unanimity case" is not immediate. R2 Prop 5's families have only *weakly* guiding members, and UN needs every θ strictly guiding (Step 2's strict inequality and interiority both fail with weak signs). Fix:
  - By the essential-union argument (BA's corollary; on decomposable domains, strictness on A(g) suffices), strict (G) of the unanimity ranking yields a countable subfamily with ψ_i = Σ c_k L^{θ_k} strictly guiding.
  - Then Θ′_i = {θ + ψ_i : θ ∈ Θ_i} sandwiches ⪯_i: (W) holds because weak inequalities add, (R) holds because θ strict and ψ_i weak give a strict sum, and every member is strictly guiding.
  - So UN does cover R2's open case, but this step must be written.

### Lemma X: CORRECT
I verified:
- Y = X_{C∪W} and A = X_{C∪U} with C = R1∖U;
- the (IB) context removal (X_{C∪W}, X_{C∪U} versus X_W, X_U agree off C and coincide on U ∪ W);
- the orientations of q₁ and q₂;
- for (★B), B = X_{C′∪W} and B′ = X_{C′∪U} with C′ = R2∖W.

The complete-ranking reformulation is correct.

### Proposition X2 (CHECKED): CORRECT
- CCF §5 (sec:cp: definition of "fine", lem:cp), thm:SW and lem:Pd (i), (ii), (iv) exist and say what is used. q₁, q₂ are comparative probabilities on R by (G) and (IB) inside M.
- Both splitting cases were checked:
  - a < 1: θ ∈ (a, min(b, 1));
  - a ≥ 1: θ′ ∈ (1/b, 1/a), shrinking U.
  - Each violates (★B); the reverse inequality violates (★A).
- Finite additivity gives P₂ = κP₁ (null pieces have P = 0 by (ii)).

### Lemma 4.1: CORRECT
- A finite-dimensional ordered real vector space inside F is lexicographic in a suitable basis (Hahn/Hausner–Wendel).
- The h_t are real integrable combinations of the f_r.
- The integrated lexicographic sign argument and the strictness clause are correct.
- The "⇔ pointwise minimiser" remark needs measurable selection of F-minimisers. This is fine: the comparison is a lexicographic condition on finitely many real measurable functions.

### Proposition 4.2: CORRECT
- Steps 2 and 4 are pure ordered-field algebra; infinitesimal p_j > 0 is enough.
- Step 3 uses 4.1.
- The hypothesis covers A and B through Step 0.

### Example 4.3: CORRECT
- λx + λ′y = (½(λ−λ′) − 2ε(λ+λ′), −½(λ−λ′) + ε(λ+λ′)).
  - For real λ ≠ λ′ the standard parts are nonzero with opposite signs.
  - For λ = λ′ = s > 0 the point is (−4εs, 2εs).
  - So 0 is undominated in K.
- Supports, with p·(λx + λ′y) linear in the vertices:
  - x needs t(1 − 3ε) ≥ ½ − ε, i.e. t ≥ (½−ε)/(1−3ε) > ½;
  - y needs t(1 + 3ε) ≤ ½ + ε, i.e. t ≤ (½+ε)/(1+3ε) < ½;
  - so no F-prior supports K at 0.
- The infinitesimal crossing interval is λ ∈ (½ + ε, ½ + 2ε).
- Guidance signs are legitimate: on P_x the switch is silence → accept with g bad at world 1 and good at world 2.
- 0 is also competitive, so it falsifies "competitive ⇒ F-Bayes".
- As R5 says, no full (S)/(C) system is built around it.

### Lemma 4.4: CORRECT
- Field form of (★):
  - (★A) ⇔ ¬[γ₁(U) < δ₁(W) ∧ γ₂(U) > δ₂(W)];
  - (★B) ⇔ ¬[γ₁(U) > δ₁(W) ∧ γ₂(U) < δ₂(W)].
- Exact Lyapunov splitting of the finitely many coefficient measures is valid.
- In the case st a < 1, a real θ ∈ (st a, min(st b, 1)) gives a < θ < b in F, because the gaps are standard. The case st a ≥ 1 shrinks U. Both violate (★B).

### Theorem PC: CORRECT
- The pairwise inequality:
  - p_B,i > 0 on P and p_A,j > 0 on N are forced;
  - r_j = ∞ is handled;
  - p_A − c·p_B has signs (−) on P and (+) on N, so (p_A − c·p_B)·w < 0. Contradiction.
- AllPat ⇒ p_A = p_B = p interior ⇒ A = B by Lemma U, which needs (LA), (S), (C); these are assumed.

### Theorem UN′: CORRECT
- Step 0 with patterns:
  - for a, use τ = − exactly on supp a and switch A to b;
  - for b, use τ = + exactly on supp b and switch B to a.
- Step 2 is PC's u-argument, applied in each pairing.
- The splice is on Z′ ∩ {|g| < 1} with Z′ = {a_A ≠ a_B}, a non-null cone because A and B are coherent.

### Theorem R_n (CHECKED): CORRECT WITH REPAIR
- (a) is correct. R1 Thm 2.2(S), with uniqueness at every p and coherent π(p) ∈ U_L, gives (LA), (S), (C), and U_add = {B_p} = π(Δ) = U_L.
  - A unique Bayes model is undominated even at boundary p: a weak dominator would be p-Bayes.
- (b) is correct at interior priors and vertices. The boundary-tie gap is honestly flagged. Note also that "onto U_L" can fail for members Bayes only at tied boundary priors; this is part of the same gap.
- **Repair:** the "Equivalently" reformulation ("for a.e. g the partition p ↦ a_{π(p)}(g) is a vertex-respecting diagram") is ill-posed as written. a_{π(p)}(g) is defined only mod null sets in g, separately for each of uncountably many p. A field of diagrams yields agreement with π(p) for a.e. p, not for every p. State the condition per prior: there is a measurable field of sign-respecting (c, c′) whose minimiser at each p ∈ Δ is a.e. unique and a.e. equal to π(p). Its converse also needs a measurable choice of (c, c′) where a boundary line is invisible in Δ.

---

## Citations

Verified:
- FA (device): §9 eq. (9.3); §10 (10.1) facet maps, §10.1 box (10.2), witnesses and forbidden-support observation, §10.2 rays (10.3), output rescaling.
- PB (device): Lemma 3.1 (x⁻, x⁺, q_s), Thm 3.2.
- NOGO §2: κ_i = 1 + ε/b_i, facet maps (2.2), output rescaling.
- CCF: sec:cp, lem:cp, thm:SW, lem:Pd. "CCF §5" is correct numbering, since the file has no introduction section.
- v3 labels: thm:general, lem:local-independence, eq:independence, lem:bayes-necessary.
- R1, R2 and R3 cross-references (R3 Lemma 2.1 = §2.1 constant-level lemma).

Inherited issue: R5 repeats R2 Thm N's sufficiency clause without R6's repair (see UN above).

## Domain flags
- No instance of (G) or (IB) applied outside M_L. Every model built in R5 is a splice or a model with advice in the advice ranges, inside M: N1's silencing, UN's E, Lemma X's Y and B′, TJ's E_S, UN′'s switches, and 4.4's W_θ.
- R4 (K4) and Cor B2's last sentence are explicitly all-model, which is legitimate.
- R4 (K3)'s positive case and G2's decomposable-domain branch need acceptance to be in the advice range near x⁻ and z′. That is (H0), which R4 assumes, and Remark B3 correctly flags the need for it.
- No silent all-model assumption found.

## Scripts
- r4py/dichotomy.py, kinked_contamination.py and ray_box_cap.py reproduce the reported numbers.
- New: `r8py/exE_fneg.py` shows that R4's (c, c′) sign test rejects the precise model, f = (−1, −1, −1).
