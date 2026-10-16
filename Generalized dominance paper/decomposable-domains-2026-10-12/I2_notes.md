# I2: running the main chain globally with competing acceptances — the box returns as a precise collar, and the collar cannot be glued

14 Oct 2026 (round 10, impossibility side). Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Scripts: `i2py/`.
Notation as in *The Contamination Triangle.tex* §§4–5 (writeup): Ω = int Δ, P(q,g) = min_{K_q} m·g, facet gambles
h^k(τ), chord λ_τ, c_k(h) (PC data), H^±, N21.1′ (A_τ ⊆ H⁺_τ), Lemma R1, w′, w, ℓ′, ℓ, λ_b.

## 0. Outcome

**Claimed result (PROVED from the cited inputs; one input, R4 Prop D, is CHECKED).** There is no additive cover
of T1 (integral penalties; or bounded charges with interior minimisers) on any (LF) decomposable domain, for any
ε ∈ (0,1) and any interior target prior. Through Prop CF (⇐, CCIBU status) this says that CF(T1) has no solution.

The global chain, in one paragraph:
1. On the positive side of a facet chord, K_q can never straddle the facet line unless it is a singleton (Lemma 1).
2. So at every non-precise prior near a vertex e_b, the facet gambles of both b-crossing facets have exact
   half-plane behaviour, exactly as on the U-domain (Theorem 2).
3. Hence the failing box at e_b is not escaped by cuts at non-precise priors at all. It forces every prior in a
   neighbourhood of the failing edge near e_b to be **precise** (Theorem 3).
4. That precise collar is diagonal-projective, σ_w(q) = w⊙q/(w·q). Its d-lines then transport globally: every
   precise prior anywhere has K_q = {σ_w(q)}, with one w for all three vertices (Prop 4).
5. The crossing chord λ_b is non-precise, so between λ_b and the collar there are *transition points* at every
   small distance from e_b. At such a point the precise value must equal the apex Φ_b(q) of the two tangent lines
   singled out by the chord through q (Lemma 5).
6. Linearising σ_w = Φ_b at e_b gives one algebraic relation per vertex. The corner equation x + 1/x = κ+1 shows
   the three relations are inconsistent (Theorem 6).

This settles the brief's tasks as follows.
- **(2) The corner equation.** It survives exactly: it is local at p\*.
- **(2) The box.** It survives, but its conclusion is no longer an inequality on x. It becomes a structural
  statement: a precise collar exists along the failing edge.
- **(3) What closes the argument.** The new relation is the transition equation σ_w(q) = Φ_b(q) at the
  precise/non-precise interface. The referee's sector cap (C1) violates it, since det(I − Φ̂) = 1 − κ ≠ 0.
- **(4) Escaping configurations.** None survives.

## 1. Where charts can fail to be half-planes (task (1))

For a.e. g, the CF chart is the cell decomposition of max(0, c·q, c′·q). It differs from a half-plane only at
**adjacent** pairs (R4 Thm A). For every q in cl F(g) ∩ Ω, K_q ⊆ g^⊥: from the exact charts, P(q,±g) ≥ 0 on cl R(±g).
Hence adjacency at q needs dim K_q ≤ 1:
- if K_q is a segment, a single projective class of g is adjacent at q;
- if K_q is a point, a projective line of g is adjacent at q.

Near-facet gambles have half-plane charts wherever K_q ∩ K″ ≠ ∅ (Lemma B1 / raytransfer (c)). In particular this
holds on B₁ and near p\*.

The half-plane analysis at p\* (pivot chords, no sliding, slope–rotation, blow-up, projectivity, hence (PC), (NS)
and the crossing rows) is the local Thm TS and survives verbatim. Hence:

**Corner equation (PROVED, assembly).** Prop boxbridge (a), (b) use only (PC), (NS) and the local pivot facts. So
in every cover x₁ = x₂ = x₃ = x ∈ {x₊, x₋} with x + 1/x = κ + 1 (Prop T1, first part).

What the general domain changes is the global clause "chart = {c_k(h)·q > 0}". Only the one-sided global facts
N21.1′ and Lemma R1 were known. The next lemma recovers the missing direction at every non-precise prior.

## 2. No straddling on the positive side

**Lemma 1 (PROVED).** Let h ∈ relint F_k (k any facet) and q ∈ Ω with c_k(h)·q > 0. Then either K_q is a
singleton, or K_q ∩ h^⊥ = ∅. In fact K_q strictly straddles no g^⊥ with g in some ball B(h, r(q)).

*Proof.*
1. By Thm TS ((PC) near Σ), every cluster of normalised c(g), as good g → h, equals the normalised c_k(h). So for
   some r > 0, c(g)·q > 0 for every good g ∈ B(h,r): otherwise a sequence would give a cluster ≤ 0 at q.
2. For such g, q is not in the silence cell {c ≤ 0, c′ ≤ 0}. So q ∈ R(g), or q ∈ R(−g), or q ∈ F(g). These give
   min_{K_q} m·g > 0, or max < 0, or K_q ⊆ g^⊥. In no case does K_q strictly straddle g^⊥.
3. Strict straddling is open in g and good gambles are dense, so this holds for every g ∈ B(h,r).
4. If K_q ∋ m₀ ∈ h^⊥ and m₁ ≠ m₀ is another point of K_q, there are two cases:
   - if m₁·h > 0, take g = h − δ𝟙;
   - if m₁·h = 0, take g = h + δ((m₁ − m₀) − ((m₁ − m₀)·m₀)𝟙).
   For small δ, g strictly separates m₀ from m₁, which contradicts step 3. ∎

## 3. Positive state at non-precise priors near the vertices

For a facet F_k and q ∈ Ω let J_k(q) := {τ ∈ (0,1) : c_k(h(τ))·q > 0}. Since τ ↦ c_k(h(τ)) is affine, J_k(q) is an
interval, and its endpoint τ_∂(q) in (0,1), when it exists, is the parameter of the chord through q.

**Theorem 2 (PROVED).** Let K_q be non-singleton.
- (a) On J_k(q), either P(q,h(τ)) > 0 for every τ, or P(q,−h(τ)) > 0 for every τ.
- (b) Fix b and its two b-crossing facets F_a and F_c. There is a neighbourhood V of e_b such that every
  non-singleton q ∈ V is in the positive state of (a) for both F_a and F_c. Hence:
  - P(q,h) > 0 ⟺ c(h)·q > 0 for every h ∈ relint F_a ∪ relint F_c;
  - P(q, h_∂) = 0 for the facet gambles h^a_∂(q), h^c_∂(q) whose chords pass through q.

*Proof.*
- (a) By Lemma 1, the two open sets {τ : P(q,h(τ)) > 0} and {τ : P(q,−h(τ)) > 0} cover the interval J. By
  connectedness one of them is all of J.
- (b), choice of V. Choose τ\* with h^a(τ\*)_b > 0. Theorem pivot gives c_a(h(τ\*))·e_b > 0. Since K_q → {e_b},
  there is V with c_a(h(τ\*))·q > 0 and P(q,h(τ\*)) > 0 on V. The same holds for F_c.
- (b), the equivalence. For q ∈ V, τ\* ∈ J_a(q), so (a) gives the positive alternative on J_a(q). Off J,
  N21.1′ gives P ≤ 0.
- (b), the zero at the endpoint. At τ_∂, P(q,h_∂) ≤ 0 by N21.1′, and P(q,h_∂) ≥ 0 as the limit from inside J. ∎

## 4. The box returns as a precise collar

**Theorem 3 (PROVED).** Let x² > κ, so that the box fails at (a,b) (with x₋, use the transposition of the writeup).
There is s₀ > 0 such that every q₀ on the edge segment (e_b, e_b + s₀(e_a − e_b)] has a ball B(q₀, r) on which
every K_q (q ∈ Ω) is a singleton.

*Proof.*
1. Take the box certificate of Prop T1: A ∈ relint F_a and B ∈ relint F_c with the ratio condition and
   c_a(A)·q₀ > 0, c_c(B)·q₀ > 0. It exists for every small s.
2. The set W = {c_a(A) > 0, c_c(B) > 0} is open and contains q₀, and the non-singleton priors form an open set.
3. Suppose non-singleton q_n → q₀. On W ∩ V, Theorem 2 gives P(q_n,A) > 0 and P(q_n,B) > 0. So
   P(q_n, A+λB) > 0, by superadditivity, for λ chosen with (A+λB)_a < 0 and (A+λB)_b < 0.
4. But edge confinement (Cor TSalways(c)) puts every limit of K_q at q₀ inside Δ_{ab}, where m·(A+λB) ≤ −δ < 0.
   So P(q_n, A+λB) < 0 for large n, a contradiction. ∎

This is the U-domain box argument with no chart transport. Competition (cuts) at non-precise priors cannot escape
it. Only precise priors can escape, and they must fill a collar U_b. The union of the balls around a segment is
connected.

## 5. Every precise prior follows one diagonal-projective map

**Prop 4 (PROVED, given R4 Prop D, which is CHECKED).**
- (a) On U_b, K_q = {σ_w(q)} with σ_w(q) := w⊙q/(w·q) for some w > 0.
- (b) For a.e. g with σ_w^{-1}(g^⊥) ∩ U_b ≠ ∅, the d-vector is d(g) ∝₊ w⊙g. Hence R(g) ⊆ {σ_w(q)·g > 0} on all
  of Ω.
- (c) Every precise prior q ∈ Ω has K_q = {σ_w(q)}, with the same w at all three vertices.

*Proof.*
- (a) R4 Prop D gives a constant or diagonal-projective map. A constant map would equal e_b, since U_b accumulates
  at e_b. That is excluded by Prop vertexfree (i).
- (b) Inside U_b, R(±g) = {±σ_w·g > 0} exactly (exact charts at precise priors). So the common boundary
  {(w⊙g)·q = 0} ∩ U_b, a segment, lies on the d-line, and the orientation matches. Since R(g) = {c > 0, d > 0},
  the inclusion holds globally.
- (c) Let K_{q′} = {σ′}.
  - For g as in (b), σ′·g > 0 ⇒ σ_w(q′)·g ≥ 0. This holds a.e., and then for all such g by openness.
  - Fix m₀ ∈ σ_w(U_b) and use all g ⊥ m₀. This forces σ_w(q′) ∈ m₀ + ℝ₊(σ′ − m₀).
  - Taking two m₀ in general position gives σ_w(q′) = σ′.
  - Applying this with the collars at two vertices shows their weights are proportional. ∎

## 6. Transition points and the contradiction

**Lemma 5 (PROVED).** Let q ∈ V be a singleton prior that is a limit of non-singleton priors. Then
K_q = {Φ_b(q)}, where Φ_b(q) := ℓ_{h^a_∂(q)} ∩ ℓ_{h^c_∂(q)}. This is the intersection of the zero lines of the two
b-crossing-facet gambles whose chords pass through q, and it is constant along chords.

*Proof.* Theorem 2(b) gives P(q_n, h_∂(q_n)) = 0 for both facets. Pass to the limit, using joint continuity of P
and continuity of h_∂. A singleton lying on two distinct lines is their intersection point. ∎

**Existence (PROVED).** λ_b ∩ Ω is non-precise (Prop vertexfree (iii)), and the collar U_b is precise. Take any
arc of radius r < ρ around e_b, inside the closed sector between λ_b and the failing edge. The non-precise set is open, and its component on the arc that
contains the λ_b end is a half-open interval. The far endpoint of that interval is precise and is a limit of
non-precise priors, so it is a transition point q_r. So transition points exist at
every small radius.

**Theorem 6 (PROVED).** Every cover gives a contradiction.

*Proof.*
1. By Prop 4(c) and Lemma 5, G_b(q) := σ_w(q) − Φ_b(q) vanishes at every q_r. G_b is real-analytic near e_b,
   with G_b(e_b) = 0.
2. Blow up at b = 2, with (a,c) = (1,3), p\* = u and x = x₊. Write q = e₂ + t(y₁, ·, y₃) and
   m = e₂ + t(μ₁, ·, μ₃). The chord conditions are
   - xζ + κ(y₃ − y₁) = 0 on F₁, with h = (−1, tζ, κ − tζ);
   - ζ′ + xκ(y₁ − y₃) = 0 on F₃, with h = (κ − tζ′, tζ′, −1).

   The tangent lines are ζ + κμ₃ − μ₁ = 0 and ζ′ + κμ₁ − μ₃ = 0. This gives
   Φ̂y = (y₁ − y₃)v with v = κ/(1−κ²)·(1/x − κx, κ/x − x), so v₁, v₃ > 0. Also σ̂_w y = (ω_a y₁, ω_c y₃), with
   ω_a = w₁/w₂ and ω_c = w₃/w₂. (`i2py/transition.py` checks the expansion against the exact Φ at t = 10⁻⁶.)
3. DG = diag(ω_a, ω_c) − v(1, −1) has det = ω_aω_c + ω_a v₃ − ω_c v₁. Its kernel is not the λ_b direction or
   the edge direction.
4. So the zeros q_r, which approach e_b inside the closed sector, force the following relation:
   (R_b) det = 0 with kernel inside the open sector, i.e. 1/ω_c = G(ω_a) := (v₁ − ω_a)/(v₃ω_a), 0 < ω_a < v₁.
5. By the cyclic symmetry of T1 and x₊, the three vertices give r₂ = G(r₁), r₃ = G(r₂), r₁ = G(r₃), where
   r₁ = w₁/w₂, r₂ = w₂/w₃, r₃ = w₃/w₁, and r₁r₂r₃ = 1.
6. G is Möbius with matrix [[−1, v₁], [v₃, 0]]. Its eigenvalues are real, of opposite sign and of unequal modulus,
   so G³ has only G's fixed points. Hence r₁ = r₂ = r₃ = 1, which needs v₁ − v₃ = 1.
7. But v₁ − v₃ = κ(x + 1/x)/(1+κ) = κ, by the **corner equation**. Since κ > 1, this is a contradiction.
8. The x₋ case follows by transposition. Prop diag (a) transports the conclusion to any p\*. ∎

- **NUMERICS (`i2py/three_vertices.out`).** Over a grid of w, the quantity min over the sector of |G_b|/r, maximised
  over the three vertices b, stays ≥ 0.06 at ε ∈ {.05, .3, .6, .9}.
- **NUMERICS.** For the identity cap (C1), det = 1 − κ, so C1 cannot meet any non-precise prior at its boundary.
  The C1 sector boundary has only one family tight, not both.

## 7. Dependencies and what a second reader must check

**Inputs used.**
- Thm TSalways ((TS), (PC), (NS), edge confinement, K → e_b), one referee.
- Thm TS (cluster uniqueness near Σ, pivot vertex signs).
- N21.1′.
- Prop vertexfree (i), (iii), one referee.
- Prop T1 (corner equation, box certificate).
- R4 Prop D, CHECKED. It is the only non-PROVED input. It is used to identify σ on U_b; the rest needs only that
  σ is C¹ with diagonal derivative at e_b.

**Check first.**
1. Lemma 1 step 1: cluster uniqueness is needed for every good g → h, not only for those used in Thm TS.
2. Theorem 2(b): the choice of V must be uniform for both facets.
3. Prop 4(b): the d-line identification uses only exact charts at precise priors.
4. Theorem 6: cyclic transport of the blow-up to e₃ and e₁. `three_vertices.py` recomputes it exactly at all three
   vertices.
