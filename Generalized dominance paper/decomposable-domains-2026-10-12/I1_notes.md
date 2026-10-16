# I1: the edges pin the c-lines, and the pinned c-lines cannot bound a convex K_q near p*

14 Oct 2026. Task: a GLOBAL compatibility argument for CF(T1). Labels: **PROVED** (full proof here, from the
cited inputs), **CHECKED** (verified, proof sketched), **CONJECTURE**, **NUMERICS**. Scripts: `i1py/`.
Notation as in *The Contamination Triangle.tex* §§2–5 (Ω = int Δ, P(q,g) = min_{K_q} m·g, facets F_k, corner
rays, crossings, chords λ_h, (TS), (PC), (NS), x_± with x + 1/x = κ + 1). Terminology as in TERMFIX_RULES.

---

## 0. Outcome

**Impossibility proved** (modulo the cited inputs, whose statuses are listed in §1).

**Theorem I1 (PROVED).** For every ε ∈ (0,1), no strictly guiding additive ranking with integral penalties covers
T1 on any decomposable domain with (LF). Consequently **CF(T1) has no solution** (this direction needs
Prop CF(⇐), i.e. it holds at the status of Thm CCIBU).

The global condition, in one sentence. Along every edge of Δ the limit credal sets are **pinned exactly** by the
facet chords coming from p* (Prop E). On the part of the edge where the box holds, this pins the chart line
c(g) = 0 of **every** gamble g crossing that edge, not only of facet gambles (Thm R). So the supporting lines of
K_q, for q near p*, are forced to be the lines line(μ₁⁻¹(y₁), μ₂⁻¹(y₂)) built from prior lines through q that end
at y₁, y₂ on two edges (Lemma S). In the "middle window" of a facet these forced lines are the joins of a
projectivity π_q between the two edges at e_k. They can bound a convex set on both sides of a certain chord C_k
only if π_q is a perspectivity, i.e. only if

  **(Diag)  C_k = line(p*, e_k):  the chord of the probability line through v_k and e_k passes through e_k.**

For the (PC) data of T1, (Diag) holds iff x = 1. The corner equation forces x = x_± ≠ 1. This is the
replacement for "projectivity + box" asked for in direction (b) of the brief:
- the edge maps supply the global projective structure;
- (Diag) is the replacement relation;
- it contradicts the corner equation directly, so **the box is not used**.

Where the pieces meet:
- *Interior:* K_u = T1, (PC) with x_±, and the facet chords through p*.
- *Edges:* edge confinement makes the limit sets one-dimensional, and Prop E then determines them exactly. Where
  the box fails (near the failing vertex of each edge) they are points; this is the sector-cap regime of C1.
- *Vertices:* μ fixes the endpoints because of the crossing rows. Admissibility of the window uses the
  non-failing ends near the vertices.
- *Crossing chords:* the window is chosen next to the crossing chord line(p*, e₃).

The contradiction itself appears at first order in |q − p*|, on one side of C_k. So the core cannot be glued to
the edges. The vertex caps are never reached.

What is new and what is imported:
- **New here:** Lemma 1 (strict signs), Lemma 2 (edge maps), Prop E, Thm R, Lemma S, Lemmas P and D, Lemma W,
  Theorem I1.
- **NUMERICS:** each step was validated end-to-end on a genuine CF solution (the normalised-box system, §9.1),
  where the predictions are exact.

---

## 1. Setting and cited inputs

A *cover*: a strictly guiding additive ranking (integral penalties) on a decomposable domain 𝓜 with (LF) at D_T,
satisfying (LA), (S), (C), covering D_T, T = T1. Its interior Bayes credal sets K_q (q ∈ Ω) are Hausdorff-continuous
and P is jointly continuous.

**Normalisations (PROVED).**
- *p\* = u.* Multiplying world i's penalties by D′_i > 0 gives a strictly guiding additive ranking on the same
  domain. Its q-Bayes model is the ν(D′q)-Bayes model of the original. It covers T1 at ν(D′⁻¹p\*). Choose D′ so
  that this point is u.
- *x = x₊.* Permuting worlds by σ = (1 2) maps covers of T1 to covers of T1 and fixes u. It sends the facet data
  x to 1/x (Contamination Triangle §4.6). Since x₋ = 1/x₊, we may take x = x₊.

**Cited inputs** (statuses as in the write-up's table):
- (C1) **Charts.**
  - By Cor TSalways(b), a.e. mixed pair has an advice range containing both acceptances. So its chart is of R1
    type {+,0,−} or {+,−}.
  - For {+,−} use the CF data (λd + e₀𝟙, (λ−1)d + e₀𝟙) (N28 Prop 5.1(⇒), confirmed).
  - For a.e. g there are c, c′ (d = c − c′) such that, with the **plane** cells
    W⁺(g) = {c>0, d>0}, W⁻(g) = {c′>0, d<0} and S(g) = {c≤0, c′≤0} (closed), for **every** q ∈ Ω:
    - P(q,g) > 0 ⟺ q ∈ W⁺;
    - P(q,−g) > 0 ⟺ q ∈ W⁻.
  - The every-q form is N28 Prop 5.1(⇒): "for good g, R(±g) and {P(·,±g)>0} are open, convex and a.e. equal,
    hence equal" (convexity by N21.1).
  - Hence on S(g) ∩ Ω, K_q meets ℓ_g := {m ∈ aff Δ : m·g = 0}, and P(·,g) ≤ 0 there.
- (C2) **(TS), (PC), (NS) at p\* = u.**
  - These hold by Cor TSalways(a): N28 Thm 3.5, one referee; Thm TS, refereed once in N23.
  - Crossing rows and corner equations follow (N12 Thm 3.1 items 3–5 under (TS), N21 §3 remark; refereed in N14).
  - Hence x₁ = x₂ = x₃ = x ∈ {x₊, x₋}, and the chord of h ∈ v_k^⊥ is {c_k(h)·q = 0}, where
    c₁(h) = (−(xh₂+h₃), xh₂, h₃), c₂(h) = (h₁, −(h₁+xh₃), xh₃), c₃(h) = (xh₁, h₂, −(xh₁+h₂)).
- (C3) **Unique clusters.**
  - For h in the normalised facet segment Σ with h ∈ relint F_k, and good g → h in N₀, c(g)/|c(g)| → c_k(h)/|c_k(h)|.
  - This is the last clause of Thm pivot in its B₁ form (Thm TS; N21.4 item 5). On B₁ the chart is
    {c(g)·q > 0} ∩ B₁ (Lemma B1). An affine function on aff Δ is determined, up to a positive factor, by its zero
    line and its positive side.
- (C4) **Edge confinement.** Every limit of K_q as q → q₀ ∈ relint[e_i,e_j] lies in [e_i,e_j]
  (Cor TSalways(c); N21.7(d), refereed in N23).

Nothing else is used: no regularity, no linear scaling, no hypothesis on the chart data beyond measurability.

---

## 2. Two elementary lemmas

**Lemma 1 (strict vertex signs; PROVED).** For x ∈ {x₊, x₋} and h ∈ relint F_k, the coordinate
sign c_k(h)_l equals sign h_l for every l with h_l ≠ 0. So every facet chord separates the vertices strictly, as ℓ_h does.

*Proof (k = 1; the others follow by cyclic symmetry).* Coordinates 2 and 3 hold by the crossing rows. For l = 1, use
h·v₁ = 0, i.e. c₀Σh = −εh₁, which gives h₂ + h₃ = κ|h₁|. Also h·v_j = ε(h_j − h₁) > 0.
- If h₂, h₃ ≥ 0, then xh₂ + h₃ > 0.
- If h₂ < 0: |h₂| < |h₁|, and xh₂ + h₃ = κ|h₁| + (x−1)h₂. This is > 0 for x ≤ 1. For x = x₊ it is
  ≥ (κ − x₊ + 1)|h₁| > 0, since x₊ < κ + 1.
- If h₃ < 0: xh₂ + h₃ = xκ|h₁| − (1−x)|h₃|. This is > 0 for x ≥ 1. For x = x₋ it is ≥ (x₋(κ+1) − 1)|h₁| > 0,
  since x₋ = 1/x₊ > 1/(κ+1).

So c₁(h)₁ = −(xh₂ + h₃) < 0 = sign h₁. ∎ (`t1_checks.out`: 0 violations; the corner equations hold.)

**Edge maps.** Let E = [e_i, e_j], with points (1−s)e_i + s e_j. Write t for probability parameters and s for prior
parameters. For z ∈ relint E there are exactly two tangent lines from z to T1. Exactly one has e_j on its positive
(T1) side; call it h_j(z). The other, h_i(z), has e_i on its positive side. Each is a facet gamble touching some
vertex v_k. Define μ_o(t) as the parameter of the point where its chord meets E (o ∈ {i, j}).

**Lemma 2 (PROVED).**
- (a) μ_i and μ_j are increasing homeomorphisms of [0,1] fixing 0 and 1.
- (b) Each is piecewise Möbius, with two pieces. On a piece where the touching vertex is v_k,
  μ_o(t) = E ∩ G_k(line(v_k, z(t))), where G_k : pencil(v_k) → pencil(p\*) is the projective map induced by Γ_k.
- (c) The Möbius extension of facet k's piece fixes the endpoint e_l of E whenever l ≠ k. It fixes e_k iff
  G_k(line(v_k,e_k)) = line(p\*,e_k).

*Proof.*
- (a), well-defined: by Lemma 1 the chord separates e_i from e_j strictly, so it meets relint E.
- (a), injective: the oriented chord determines the facet gamble. The chord normal n_h is strictly monotone on
  each facet (Thm pivot), continuous at corners (NS), and has n_h·(e_l − p\*) of sign h_l (Lemma 1). Going once
  round ∂D_T, h runs through the six mixed sign patterns once each, in cyclic order (Lemma signs). So n_h runs once
  round S¹ and is injective.
- (a), endpoints: as z → e_i, h_j(z) tends to the tangent from e_i, which is a crossing gamble of coordinate i.
  Its chord is line(p\*, e_i) (crossing rows), so μ_j → 0. The other endpoint is similar.
- (a), conclusion: a continuous injective map of [0,1] fixing 0 and 1 is an increasing homeomorphism.
- (b) The map is the composite of projective bijections E → pencil(v_k) → pencil(p\*) → E.
- (c) The line through v_k and e_l is a crossing line exactly when l ≠ k. Its chord is then line(p\*, e_l). ∎

For T1 on [e₁,e₂] (`symbolic_edges.out`), facet 3 gives s = tx/(tx − t + 1), which fixes both endpoints. Facet 1
fixes e₂ only, with s(0) = (x−1)/(2x−1). Facet 2 fixes e₁ only. With **c₀ = (1−ε)/3**, the pieces on
[e_a,e_b] are as follows:
- "+ toward e_b": F_a on [P_ac, e_b] and F_c on [e_a, P_ac];
- "+ toward e_a": F_b on [e_a, P_bc] and F_c on [P_bc, e_b];
- here P_ac = line(v_a,v_c) ∩ E lies at t = c₀ from e_a, and P_bc at t = 1 − c₀.

Put Z_o := μ_o⁻¹. Call q₀ ∈ relint E **non-failing** if Z_j(q₀) < Z_i(q₀), and write N_E for the open set of
non-failing points.

---

## 3. The edges are pinned exactly

**Proposition E (PROVED).** Let q₀ ∈ relint E, with s = s(q₀). Every limit K\* of K_q (q → q₀, q ∈ Ω) lies in E
and satisfies:
- (i) min K\* ≤ Z_j(s) and max K\* ≥ Z_i(s);
- (ii) K\* does not strictly straddle any probability point t ∈ (0, Z_j(s)) ∪ (Z_i(s), 1).

Hence:
- if q₀ ∈ N_E, every limit equals [Z_j(s), Z_i(s)], so K_q → [Z_j(s), Z_i(s)];
- if Z_j(s) > Z_i(s), every limit is a single point of [Z_i(s), Z_j(s)].

*Proof.*
1. K\* ⊂ E by (C4).
2. Fix t ∈ (0,1) and o = j. Let ĥ be the normalised h_j(z(t)). By Lemma 1, c_k(ĥ)·q₀ has the sign of s − μ_j(t).
   By (C3) the same sign holds for c(g)·q, for every good g near ĥ and every q ∈ Ω near q₀.
3. Case s > μ_j(t), i.e. t < Z_j(s). Then c(g)·q > 0, so q ∉ S(g): q lies in W⁺, W⁻ or the d-face, where
   K_q ⊂ ℓ_g. So K_q does not strictly straddle ℓ_g. If K\* strictly straddled t, then K_q would strictly straddle
   ℓ_g for q near q₀ along the sequence and g near ĥ. That is a contradiction.
4. Case t > Z_j(s). Then c(g)·q < 0, so q ∉ W⁺(g), and K_q meets the closed negative side of ℓ_g. In the limit
   K\* meets {≤ t}, so min K\* ≤ t. Taking the infimum over such t gives min K\* ≤ Z_j(s).
5. The case o = i is the mirror image.
6. Non-failing case. Suppose min K\* < Z_j. Then K\* strictly straddles points of (min K\*, Z_j), which (ii)
   forbids. So min K\* = Z_j, and likewise max K\* = Z_i. K\* is an interval.
7. Failing case. (0, Z_j) ∪ (Z_i, 1) = (0,1), so K\* straddles nothing and is a point. (i) places it in
   [Z_i, Z_j]. ∎

*Checks.*
- Failing ends: Prop E reproduces the known precise edge limits ωs with ω ∈ [κ/x, x] (R4 §9, N28_referee).
- Non-failing ends near a vertex: it gives [s/x, κxs], so the box value κx² ≷ 1 decides.
- Midpoint m₁₂ of [e₁,e₂] (the end of the crossing chord line(u, e₃)): it gives exactly the shadow of T1 from e₃,
  K\*(m₁₂) = [π₃(v₁), π₃(v₂)], with parameters (1−ε)/(2+ε) and (1+2ε)/(2+ε). This is non-failing for every ε
  and every x (crossing rows only).
- At ε = .3 with x₊, the non-failing set of each edge is s < 0.744, measured from the vertex where the box holds
  (`edgemaps.py`).

---

## 4. The pinned edges pin every c-line

**Theorem R (PROVED).** Let g satisfy (C1). Suppose ℓ_g meets relint E at the probability parameter t with e_o on
its positive side, and y := μ_o(t) ∈ N_E. Then the prior point y lies on the c-ray {c(g) = 0, c′(g) ≤ 0}: indeed
y ∈ cl W⁺(g) ∩ S(g). Symmetrically, the c′-line passes through μ_{o′}(t) (o′ the other end) when that point lies in
N_E.

*Proof (o = j).*
1. For priors q₀ ∈ E slightly beyond y toward e_j: Z_j(q₀) > t, so K\*(q₀) ⊂ (t, 1]. Hence K_q lies strictly on
   the positive side of ℓ_g for q ∈ Ω near q₀ (Prop E, convergence). So q ∈ W⁺(g).
2. For q₀ slightly before y: Z_j(q₀) < t < Z_i(q₀), using y ∈ N_E and continuity. So K_q strictly straddles ℓ_g,
   and q ∈ S(g).
3. Hence y ∈ cl W⁺ ∩ S ⊂ {c ≥ 0} ∩ {c ≤ 0, c′ ≤ 0}. ∎

**Lemma S (forced supporting lines; PROVED).** Let q ∈ Ω and let Λ ∋ q be an oriented line meeting two edges at
y₁ ∈ N_{E₁} and y₂ ∈ N_{E₂}, with e_{o_m} the end of E_m on the positive side of Λ. Put z_m := Z^{E_m}_{o_m}(y_m)
and L := line(z₁, z₂), oriented like Λ: the vertex partition is the same, because L crosses the same two edges.
Then min_{K_q} g_L·m = 0, i.e. L supports K_q and K_q lies on its closed positive side.

*Proof.*
1. For g near g_L, ℓ_g crosses E₁ and E₂ near z₁ and z₂ with the same orientations. Their μ-images lie near
   y₁, y₂ ∈ N (an open set).
2. By Thm R, for a.e. such g both μ-images lie on the c-ray of g. So the whole chord of the c-line inside Ω lies
   on the ray: the apex is not between them.
3. Points of that chord (except possibly the apex) lie in cl(W⁺ ∩ Ω) ∩ S. So P(·,g) = 0 on the chord.
4. Take such g_n → g_L. Their c-chords converge to Λ ∩ Ω (μ is continuous). Pick q_n on them with q_n → q. Then
   P(q,g_L) = lim P(q_n,g_n) = 0. ∎

---

## 5. The middle window, and the contradiction

Work on F₁; E₁ = [e₁,e₂] and E₂ = [e₃,e₁] meet at e₁. Let μ₁ be facet 1's Möbius map on E₁ ("+ toward e₂") and μ₂
facet 1's Möbius map on E₂ ("+ toward e₃"). Put h\* ∝ (0,1,−1), the probability line through v₁ and e₁, and let
C₁ := {c₁(h\*)·q = 0}, a line through u. Write a₁ := C₁ ∩ line E₁ and a₂ := C₁ ∩ line E₂ (projectively).
By Lemma 2(c), μ₁(e₁) = a₁ and μ₂(e₁) = a₂.

**Lemma W (an admissible window exists, for every ε; PROVED; x = x₊).** There are y⁽¹⁾ < y⁽²⁾ < y⁽³⁾ in relint E₁
near m₁₂, and a neighbourhood U of u, such that for every q ∈ U and every i:
- y⁽ⁱ⁾ ∈ N_{E₁}, and Z^{E₁}_2(y⁽ⁱ⁾) lies in facet 1's piece;
- line(q, y⁽ⁱ⁾) meets relint E₂ at a point of N_{E₂} whose Z^{E₂}_3-preimage lies in facet 1's piece.

*Proof.* All conditions are open, so it suffices to check them in the limit y → m₁₂, q = u.
1. On E₁: m₁₂ ∈ N_{E₁} (§3). Its preimage π₃(v₁), at t = (1−ε)/(2+ε), lies in facet 1's piece (c₀, 1), since
   (1−ε)/(2+ε) > (1−ε)/3.
2. On E₂: line(u, y) meets E₂ near e₃ for y on the appropriate side of m₁₂.
   - By cyclic symmetry, near e₃ the edge [e₃,e₁] behaves like [e₁,e₂] near e₁. There Z₂(s) = s/(x(1−s)+s) ~ s/x
     (facet 3) and Z₁(s) ~ κxs (facet 2, slope (1−ε)/(x(1+2ε))).
   - So N ⊃ (e₃, e₃ + δ₀) iff κx² > 1, which holds for x₊.
   - "+ toward e₃" on [e₃,e₁] near e₃ is supplied by F₁ on [0, 1 − c₀]. ∎

For q ∈ U let Λ_i(q) := line(q, y⁽ⁱ⁾) and z_i := μ₁⁻¹(y⁽ⁱ⁾), which does not depend on q. Let ρ_q : E₁ → E₂ be the
central projection from q, and put π_q := μ₂⁻¹ ∘ ρ_q ∘ μ₁, a projectivity between the lines E₁ and E₂. By Lemma S
the lines

  L_i(q) := line(z_i, π_q(z_i))   (i = 1, 2, 3)

support K_q from their positive sides, which contain e₂ and e₃.

**Lemma P (PROVED).**
- π_u is the perspectivity with centre v₁, and L_i(u) = line(v₁, z_i) are facet lines.
- If C₁ ∌ e₁, then π_q(e₁) = e₁ ⟺ q ∈ C₁.
- The map q ↦ π_q(e₁) has nonzero derivative transverse to C₁ at u.
- C₁ ∋ e₁ ⟺ x = 1.

*Proof.*
1. ρ_u follows chords through u. μ₁ and μ₂ are induced by the same pencil map G₁. So π_u(z) = line(v₁,z) ∩ E₂.
2. π_q(e₁) = μ₂⁻¹(line(q,a₁) ∩ E₂). This equals e₁ iff line(q,a₁) ∩ E₂ = a₂, iff q ∈ line(a₁,a₂) = C₁.
   (a₁ ≠ e₁ ≠ a₂ when C₁ ∌ e₁.)
3. Transversality: line(q,a₁) pivots about a₁ ∉ line E₂ (or moves parallel, if a₁ is at infinity). C₁ meets line
   E₂ transversally at a₂. μ₂⁻¹ is Möbius and finite at a₂.
4. Finally, c₁(h\*)₁ = −(x−1). ∎

**Lemma D (three-line determinant; PROVED).** Use affine coordinates (X,Y) on aff Δ with origin e₁ and axes E₁, E₂.
Write π(X) = (aX+b)/(cX+d). The line through (X,0) and (0,π(X)) has coefficients ℓ(X) = (1/X, 1/π(X), −1). For fixed
distinct X₁, X₂, X₃ ≠ 0 put D := det[ℓ(X₁); ℓ(X₂); ℓ(X₃)]. Then:
- D = 0 whenever b = 0 (perspectivities);
- ∂D/∂b at b = 0 equals (d/a²)(w₁−w₂)(w₂−w₃)(w₃−w₁), with w_i = 1/X_i. This is ≠ 0 when ad ≠ 0.

*Proof.*
1. At b = 0, ℓ(X_i) = w_iA + B with A = (1, d/a, 0) and B = (0, c/a, −1). So D = 0.
2. ∂_b ℓ(X_i) = p_i e_Y with p_i = −(cw_i + dw_i²)/a².
3. Expanding row by row with det[e_Y; A; B] = 1 gives Σ p₁(w₂−w₃) − p₂(w₁−w₃) + p₃(w₁−w₂).
4. The c-part cancels. The d-part is a Vandermonde determinant. ∎

**Theorem I1 (PROVED).** No cover of T1 exists, for any ε ∈ (0,1).

*Proof.*
1. Normalise p\* = u and x = x₊ (§1). Take the window of Lemma W.
2. *Base configuration.* At q = u the three supporting lines L_i(u) are facet lines through v₁ in increasing
   order. So g₂ = αg₁ + βg₃ with α, β > 0 and no 𝟙-component.
3. *Decomposition near u.* For q near u write g₂(q) = α(q)g₁(q) + β(q)g₃(q) + γ(q)𝟙, with α, β > 0 by continuity.
   Then γ(q) is the value of g₂ at X(q) := L₁ ∩ L₃, and γ = σ₀ · D(π_q), where σ₀ is a locally constant nonzero
   factor (orientations, and the normalisation of X).
4. *Sign change.* π_u is a perspectivity with ad ≠ 0: it is non-constant, and finite at 0 with value 0. By
   Lemma P, b(q) ∝ π_q(0) is nonzero off C₁ and changes sign across C₁ with nonzero derivative, because x₊ ≠ 1.
   By Lemma D, D(π_q) = b(q)(∂_bD + O(b)) changes sign too.
5. *Contradiction.* Pick q ∈ U on the side of C₁ where γ(q) > 0. By Lemma S, K_q ⊂ {g₁ ≥ 0} ∩ {g₃ ≥ 0}. So
   g₂ ≥ γ > 0 on K_q, whereas Lemma S also gives min_{K_q} g₂ = 0. ∎

**Corollary.**
- (a) Together with Cor TSalways(b), and since every cover has both acceptances in the advice range a.e., T1 has no
  additive cover on any (LF) decomposable domain. CONJECTURE N28 holds in its ranking form.
- (b) CF(T1) has no solution. This uses Prop CF(⇐) to import (C2)–(C4), so its status is that of Thm CCIBU.
  The imported proofs appear to use only the chart structure, but I have not re-verified them for bare CF families.
- (c) Bounded-charge penalties vanishing on null sets, given interior minimisers: the same proof (CHECKED). Every
  step uses charts and the every-q Bayes property, which hold there (Cor charges, N14 Thm C2).

---

## 6. What the argument says about the structure (interpretation)

- **The replacement for the box.** In the U-domain proof the box confronts the corner equation x + 1/x = κ + 1.
  Here (Diag) confronts it: in every middle window, the facet-k chord of line(v_k, e_k) must pass through e_k.
  - (Diag) says that the vertex map near v_k is the restriction of a projective map that **fixes the vertex e_k**.
  - With the crossing rows, which fix e_i and e_j, this makes it diagonal-projective, ψ_k(q) = ν(v_k ⊙ q/p\*).
  - That forces x = 1 for T1.
- **Why the known positive examples escape.**
  - The normalised-box systems (genuine CF solutions) have piecewise diagonal facet maps, so (Diag) holds.
  - Gauge-mixture polygons (R10a Thm M) do not have both acceptances in the advice range, so edge confinement and
    Prop E are unavailable.
  - T1 is the case where (NS) at the three corners of a triangle cannot be met with diagonal data
    (x = 1 gives 1 + 1 ≠ κ + 1).
- **Where the gluing fails.** The contradiction lives at first order near p\*, on one side of C₁. The failing ends
  of the edges (sector caps, C1) and the vertex layers are never needed: the window uses only the midpoint of one
  edge and the non-failing end of another.
- **Other targets (CONJECTURE).** Let T be any interior polygon whose covers have both acceptances a.e. Suppose
  some vertex v_k has an admissible middle window. Then every cover satisfies (Diag) at v_k. If true in general,
  this is a clean necessary condition for coverage on two-sided domains.

---

## 7. NUMERICS (sanity only; the proofs above do not depend on them)

| check | file | result |
|---|---|---|
| PC data: corner equations, vertex signs | `t1_checks.out` | NS holds; 0 sign violations |
| Edge maps exact (sympy) | `symbolic_edges.out` | facet 3 s = tx/(tx−t+1); facet 1 s(0) = (x−1)/(2x−1) |
| Non-failing sets per edge | `edgemaps.py` | one crossover per edge, e.g. s = 0.744 at ε = .3, x₊; the failing end is the failing-box vertex |
| **Validation on a genuine CF solution** (normalised boxes, λ = (1,1,1), η = (2,3,1.5)) | `sanity_box.out` | Prop E predicts every edge limit exactly (12/12). All forced lines touch the true K_q: \|min_K g·m\| ≤ 1.5e−15, LP gap ≤ 2e−15 at 5 priors |
| Full forced-line family for T1 near u (all admissible windows) | `t1_envelope.py` | LP gap/r ≈ 0.1–1.2, constant as r → 0, at ε ∈ {.05, .3, .6}, x± |
| Window by window | `middle_test.out` | outer windows (projective, fix the shared vertex): gap 0; middle window: gap 0 on one side of C₁ and > 0 on the other |
| Control x = 1 | `control_x1_middle.out` | middle-window gap 0 on both sides; x = 1.2 gives gaps |
| Three-line certificate | `certificate.out`, `cert_onC1.out`, `cert_admissible.out` | γ/r stable and of opposite signs across C₁ at ε ∈ {.05, .3, .6, .9}, x±; γ = 0 (1e−42) on C₁; windows admissible |

---

## 8. What a second reader should check first

1. **Prop E, step 3.** "c(g)·q > 0 ⇒ q ∉ S(g)" is applied to good g near the normalised facet gamble, at priors
   near an edge point far from p\*. It needs the unique-cluster convergence (C3) as **vectors in ℝ³**, not only as
   lines on B₁. I argue that an affine function on aff Δ is fixed by its zero line on B₁ and its sign, up to a
   positive factor.
2. **(C1), the every-q form.** For a.e. g and every q ∈ Ω, P(q,g) > 0 ⟺ q ∈ W⁺(g). Thm R and Lemma S need it at
   priors near the edges.
3. **Lemma S.** The c-ray must contain both pinned edge points, so that P(·,g) = 0 on the whole chord. This uses
   that both points lie in S(g), hence have c′ ≤ 0.
4. **Lemma W.** The window must sit in facet 1's pieces at both ends and in the non-failing parts. Both rest on
   the exact piece boundaries t = c₀ and t = 1 − c₀, and on the endpoint slopes 1/x and κx.
5. **Lemma 2(a), injectivity.** The degree-one argument for the chord-normal map.
6. **Normalisations.** World-reweighting moves p\* to u at the ranking level. σ = (1 2) swaps x₊ and x₋.

---

## 9. Files (`i1py/`)

`general.py` (edge maps, forced lines, LP gaps; box and T1 systems), `edgemaps.py`, `symbolic_edges.py`,
`sanity_box.py`, `t1_checks.py`, `t1_envelope.py`, `t1_where*.py`, `psi_maps.py`, `middle_test.py`,
`control_x1*.py`, `certificate.py`, `cert_onC1.py`, `cert_admissible.py`, and their `.out` files.
