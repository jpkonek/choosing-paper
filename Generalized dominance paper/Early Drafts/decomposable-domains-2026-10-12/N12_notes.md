# N12: the additive core on the U-domain — removing (DF) and (ND)

13 Oct 2026. Task: BRIEF6 part (B). Labels: **PROVED** (full proof here), **CHECKED** (verified, proof sketched),
**CONJECTURE**, **NUMERICS**. Citations: R15 (with the R18 repairs), R1 Prop 3.1, CONTAMINATION_NOGO (CN) §3.
Scripts: `n12py/`.

---

## 0. Outcome

**Verdict.** Not settled in full generality, but the gap is now much narrower and fully explicit.
- No realisation of T1 exists in any family whose facet support functions have one-sided directional derivatives at p\*
  that are continuous in the direction (hypothesis (DD), §4). This allows every kink with a continuous one-sided
  derivative: two-slope kinks, conical / piecewise-linear vertex motion, split "needle" vertices. **(DF) is removed.**
- The irregularity of the field c is irrelevant. Everything depends only on the credal family q ↦ K_q, which is
  automatically Hausdorff-continuous (§1).
- The vertex-limit box needs no regularity and no adjacency hypothesis (§2).
- The whole R15 contradiction depends on one geometric property: the **pivot chord map** of each facet is projective
  (§3). The remaining gap is exactly that property, for families with no directional derivatives (§7).
- No construction was found. Every kink mechanism examined is excluded (§§4–5).

Numbered claims:

**N12.1 (PROVED) Reduction.** On the U-domain (evaluable models: the measurable subsets of U = D_{K′}; see Setting
below), a realisation (R1)–(R2) is equivalent to a family
q ↦ K_q (q ∈ int Δ) with the following properties:
- K_q ⊇ K′ and K_{p\*} = T;
- K_q is Hausdorff-continuous;
- for a.e. g ∈ U, {q : P_{K_q}(g) > 0} is a.e. an open half-plane H(g) that respects the vertex signs of g.

The Bayes models at the vertices are automatically coherent. One may take p\* = u **globally**, by a projective
reindexing of the priors. Merely measurable c creates no extra freedom, because P(q,g) = P_{K_q}(g) is jointly
continuous whatever c is.

**N12.2 (PROVED) Chords and level chords.**
- For every g ∈ U there is a line ℓ with P(·,g) ≥ 0 on one closed side, P(·,g) ≤ 0 on the other, and P(·,g) = 0 on
  ℓ ∩ int Δ.
- P(q, g − c𝟙) = P(q,g) − c, so every level set of q ↦ P(q,g) is a straight chord, at every level
  c ∈ (min_i g_i, P_{K′}(g)).
- Charts are superadditive: H(g) ∩ H(g′) ⊆ H(g + g′) for a.e. pair (g, g′).

**N12.3 (PROVED) Regularity-free edge box.** Take a ≠ b and a.e. A, B ∈ U with A_a < 0 < A_b, B_b < 0 < B_a and
A_b B_a < |A_a||B_b|. Then H(A) ∩ H(B) does not meet the closed edge [e_a, e_b]. This contains R15 Lemma 6.1 and needs
neither (DF), (ND) nor (NA_w).

**N12.4 (PROVED) Pivot dichotomy and global tangency.** For h ∈ ∂D_T∖0, at least one of the following holds:
- some cluster chord of h passes through p\* (a *pivot chord*); then K_q touches the line L_h = {m·h = 0} for **every**
  q on that chord;
- P(·,h) ≡ 0 on a neighbourhood of p\*.

If the second case holds for an open arc of h in a facet F_k, then v_k ∈ K_q for all q near p\* (vertex pinning).

**N12.5 (PROVED) Reduction of R15 Thm 6.2 to two geometric hypotheses.**
- (PC) Every facet gamble has a unique cluster chord. That chord passes through p\*, and its normal is Γ_k h for one
  linear map Γ_k per facet.
- (NS) No sliding edges: the corner chords match.

Under (PC) and (NS), no all-facing general-position triangle is realisable. This covers T1 for every ε ∈ (0,1), and
every ε-contamination of an interior baseline. (DF), (ND) and (NA_w) are not needed.

**N12.6 (PROVED) Kinks are impossible.** Hypothesis (DD): for h ∈ relint F_k, the one-sided derivative
D(δ,h) = lim_{t↓0} P(p\*+tδ,h)/t exists for every δ, is continuous in δ, and takes both signs. Under (DD):
- (a) D(·,h) = α(h)[n(h)·δ]₊ − β(h)[n(h)·δ]₋ (two-slope form; from the level chords N12.2);
- (b) α(h)n(h) = Γ_k h with Γ_k linear, and β/α ≡ ρ_k is constant on each facet (from concavity in h; an
  "angular-momentum" argument);
- (c) hence (PC) and (NS) hold.

So T1 has **no** realisation under (DD) alone. (DD) is strictly weaker than (DF)+(ND): it permits kinks with
ρ_k ≠ 1 and a priori any continuous positively homogeneous first-order dependence.

**N12.7 (CHECKED) Two further regularity classes reduce to (PC).**
- (a) *Polygonal families.* Suppose that, near p\*, K_q is a polygon whose vertex maps are local homeomorphisms on a
  punctured neighbourhood of p\*. Then the vertex maps are projective, by the local fundamental theorem of projective
  geometry, so (DF)+(ND) hold. Rank-one vertex maps are impossible on 2-crossing facets.
- (b) *Smooth dual charts, flat facets allowed.* Suppose the dual chart map Λ (tangent line ↦ chord) is C² near each
  facet segment, with nondegenerate transversal derivative. Then the chord map is a Möbius map. The proof is a
  second-order computation that needs **no** nondegeneracy of the q-derivative of P. So first-order-flat facets
  ((ND) failing) with a smooth dual chart are excluded.

**N12.8 (PROVED) Charges.** Let the penalties be charges ν_i = ν_i^c + ν_i^p (Yosida–Hewitt), each purely finitely
additive part carried by every neighbourhood of a closed null set S (for example S = ∂D_T, or any finite union of
seams). Then every Bayes model equals, a.e., the Bayes rule of the countably additive part. Such charges therefore
reduce to the integral case, and cannot create kinks. Charges carried near dense null sets are open (CONJECTURE N12.C2).

**N12.9 (NUMERICS) Two-slope data with a non-projective chord field violate concavity.**
- A linear program over all two-slope data (α, β) with a prescribed chord field n(τ) finds:
  - minimum violation exactly 0 when n is projective;
  - a violation of order h² whose scaled value converges to ≈ 3.5 > 0 when n is not projective.
- The second-order dual equation of N12.7(b) has only Möbius solutions (sympy check).

**Exact remaining gap (§7).**
- *Projective pivot conjecture N12.C1.* In any realisation, on each facet of T the clusters are unique pivot chords and
  the chord map is projective, with matching corners.
- Equivalently, the only realisations still possible are families with no continuous one-sided first-order behaviour at
  p\* on some facet: oscillating difference quotients, direction-discontinuous derivatives, or vertex pinning
  (N12.4, second case), together with sliding edges where (DD) fails.

---

## 1. Setting and reduction (N12.1)

**Setting.**
- K = T = T1 = (1−ε)u + εΔ, with vertices v_k.
- K′ = u + s(K − u) for some 0 < s < 1, and U = D_{K′}. U is an open convex cone containing cl D_T∖0, because K′ lies
  in the relative interior of T.
- c : U → ℝ³ is measurable and, for a.e. g, c_i(g) has the strict sign of g_i.
- B_q = {g ∈ U : q·c(g) > 0}.

**Requirements.**
- (R1) For every q ∈ int Δ: the tie set {g ∈ U : q·c(g) = 0} is μ-null, and B_q = D_{K_q} a.e. for a credal set K_q.
- (R2) K_{p\*} = T for some p\* ∈ int Δ.

Notation: P(q,g) := min_{m∈K_q} m·g.

**Lemma 1.1 (PROVED).**
- (a) K_q ⊇ K′.
- (b) The vertex Bayes models U ∩ {g_i > 0} = D_{conv(K′ ∪ {e_i})} are coherent.
- (c) K_q is unique for each q.

*Proof.*
- (a) D_{K_q} is an open convex cone that is a.e. contained in the open convex set U. So D_{K_q} ∖ cl U is open and
  null, hence empty. Openness then gives D_{K_q} ⊆ int cl U = U, and D_K ⊆ D_{K′} iff K ⊇ K′.
- (b) D_{K₁} ∩ D_{K₂} = D_{conv(K₁ ∪ K₂)}.
- (c) Open convex sets that agree a.e. are equal, and K ↦ D_K is injective. ∎

**Prop 1.2 (PROVED; = R1 Prop 3.1 in this domain).** q ↦ K_q is Hausdorff-continuous on int Δ, and P is jointly
continuous and 1-Lipschitz in g for the sup norm.

*Proof.*
- If q_n → q, then 1{q_n·c(g) > 0} → 1{q·c(g) > 0} off the null tie set of q.
- So D_{K_{q_n}} → D_{K_q} in Gaussian measure (dominated convergence).
- For closed convex cones with nonempty interior, local convergence in measure implies Hausdorff convergence of their
  traces on the sphere, and polar duality is continuous.
- Finally |P(q,g) − P(q′,g′)| ≤ ‖g − g′‖_∞ + ‖g‖ d_H(K_q, K_{q′}). ∎

**Prop 1.3 (PROVED; global form of R15 Lemma 4.1).** If (c, p\*) is a realisation, so is (c̃, u) with c̃ := p\* ⊙ c.

*Proof.*
- q̃·c̃(g) = (q̃ ⊙ p\*)·c(g), so B̃_{q̃} = B_{N(q̃⊙p\*)}. Here N is normalisation, a projective bijection of Δ that fixes
  the vertices.
- c̃ has the same sign pattern as c, ties and coherence transfer, and K̃_u = K_{p\*} = T. ∎

**Prop 1.4 (PROVED, equivalence).** Write (★) for: a.e. g has an open half-plane H(g) with
- e_i ∈ H(g) if g_i > 0,
- e_i ∉ cl H(g) if g_i < 0,
- {q ∈ int Δ : P(q,g) > 0} = H(g) ∩ int Δ a.e.

A realisation yields a family K_q as in N12.1 satisfying (★), with H(g) = {q·c(g) > 0}. Conversely, given such a family
with null ties, let c(g) be the normal of H(g), normalised (measurable by evaluation on a countable dense set of priors).
Its Bayes models are the D_{K_q}.

**Consequence.** Any discontinuity of c (dense, non-closed, as in CN §3) has no effect beyond K_q. The CN regularisation
issue and the "closure vs pointwise rejection" issue disappear on this domain. All regularity questions are about
q ↦ K_q at p\*.

## 2. Chords, box, pivots

**Lemma 2.1 (weak chords; PROVED).**
- (a) For a.e. g ∈ U:
  - P(·,g) ≥ 0 on cl H(g) ∩ int Δ;
  - P(·,g) ≤ 0 on int Δ ∖ H(g);
  - P(·,g) = 0 on the chord ℓ(g) = ∂H(g) ∩ int Δ;
  - {q : P(q,g) = 0} is null.
- (b) For **every** mixed g ∈ U, and every limit ℓ of chords ℓ(g_n) along good g_n → g (a *cluster chord*), with the
  limiting orientation:
  - P(·,g) ≥ 0 on the closed positive side;
  - P(·,g) ≤ 0 on the closed negative side;
  - P(·,g) = 0 on ℓ ∩ int Δ;
  - e_i lies in the closed positive side if g_i > 0, and in the closed negative side if g_i < 0.
  Cluster chords exist, because chords separate vertices, so they meet Δ and lie in a compact space.

*Proof.*
- (a) For each q, {g : P(q,g) = 0} ⊆ ∂D_{K_q} ∪ {nonneg. boundary}, which is null. By Fubini, the set
  {(q,g) : P = 0} is null, so the tie set is null for a.e. g.
- Fix such a g. The open set {P > 0} is a.e. equal to H, so {P > 0} ∖ cl H is open and null, hence empty. Openness then
  gives {P > 0} ⊆ H. Similarly {P < 0} ⊆ int Δ ∖ cl H.
- Hence P ≥ 0 on H and P ≤ 0 off cl H. By continuity in q, P ≥ 0 on cl H, P ≤ 0 on the closed complement, and P = 0 on ℓ.
- (b) Joint continuity (Prop 1.2) passes these properties to limits. ∎

**Lemma 2.2 (level chords; PROVED).**
- m·𝟙 = 1 on Δ, so P(q, g − c𝟙) = P(q,g) − c.
- For c ∈ (min_i g_i, P_{K′}(g)), the gamble g − c𝟙 lies in U and is mixed.
- So Lemma 2.1(b) gives, for every such level c, a line ℓ_c with P(·,g) ≥ c on one closed side and ≤ c on the other. ∎

**Lemma 2.3 (superadditivity; PROVED).** For a.e. (g, g′) ∈ U², H(g) ∩ H(g′) ∩ int Δ ⊆ H(g + g′). The right side is ∅
when g + g′ ∉ U.

*Proof.*
- P(q, g + g′) ≥ P(q,g) + P(q,g′) > 0 for a.e. q ∈ H(g) ∩ H(g′).
- By Fubini, g + g′ is good for a.e. pair. So H(g) ∩ H(g′) is a.e. contained in H(g + g′), and an open set a.e.
  contained in an open half-plane is contained in it.
- If g + g′ ∉ U, then P(q, g + g′) ≤ 0 for all q, because K_q ⊇ K′. ∎

(Lemma 2.3 is stated for the a.e. pairs only; Theorem 2.4 applies the same argument directly.)

**Theorem 2.4 (edge box; PROVED).** Let a ≠ b. For a.e. pair (A, B) with A_a < 0 < A_b, B_b < 0 < B_a and
A_b B_a < |A_a||B_b|, H(A) ∩ H(B) ∩ [e_a, e_b] = ∅.

*Proof.*
- The inequality gives an open interval of λ > 0 with (A + λB)_a < 0 and (A + λB)_b < 0. For a.e. (A, B, λ), A + λB is
  good (Fubini).
- By Lemma 2.3 (with H(λB) = H(B)), O := H(A) ∩ H(B) ∩ int Δ ⊆ H(A + λB).
- Suppose q₀ ∈ [e_a, e_b] ∩ H(A) ∩ H(B). The open set H(A) ∩ H(B) contains a neighbourhood of q₀, so O accumulates at
  q₀ and q₀ ∈ cl H(A + λB).
- But e_a and e_b lie in the open half-plane aff Δ ∖ cl H(A + λB), by the strict signs, and so does q₀ ∈ [e_a, e_b].
  Contradiction. ∎

**Remark (relation to R15 Lemma 6.1).**
- Write σ(A) for the point where ℓ(A) crosses the edge (a,b). Theorem 2.4 says σ(A) ≤ σ(B), in the orientation in which
  H(A) contains e_b and H(B) contains e_a.
- R15 obtained this only via (DF), (NA_w) and R10b Lemma FS. Here the edge model needs neither.

**Prop 2.5 (pivot dichotomy, tangency, pinning; PROVED).** Let h ∈ ∂D_T∖0, so P(u,h) = 0 (taking p\* = u).
- (a) Either some cluster chord of h passes through p\*, or P(·,h) ≡ 0 on a neighbourhood of p\*.
- (b) If ℓ is a pivot chord, then for every q ∈ ℓ ∩ int Δ, P(q,h) = 0: K_q lies in {m·h ≥ 0} and touches
  L_h = {m : m·h = 0}. On the open positive side of ℓ, P(·,h) ≥ 0; on the open negative side, K_q meets {m·h ≤ 0}.
- (c) Suppose P(·,h) ≡ 0 near p\* for every h in an open arc A ⊆ relint F_k. Then v_k ∈ K_q for all q near p\*.

*Proof.*
- (a) B_{p\*} = D_T a.e. So good g ∈ D_T have p\* ∈ H(g), and good g ∉ cl D_T have p\* ∉ cl H(g).
  - Near h both sets have positive measure. This gives clusters ℓ⁺, with p\* in the closed positive side, and ℓ⁻, with
    p\* in the closed negative side.
  - If neither passes through p\*, Lemma 2.1(b) gives P(·,h) ≥ 0 and P(·,h) ≤ 0 on a neighbourhood of p\*.
- (b) Lemma 2.1(b).
- (c) For q near p\*, K_q ⊆ ∩_{h∈A} {m·h ≥ 0}, a wedge W at v_k, and K_q meets every L_h with h ∈ A.
  - For h interior to A, L_h ∩ W = {v_k}. ∎

**Prop 2.6 (monotone pivot chords; PROVED).** Let h, h′ ∈ relint F_k have pivot chords with normals n, n′, not
antipodal. Then any pivot chord of h + h′ has its normal in cone(n, n′). Hence, where pivots exist, the chord map
h ↦ n(h) is monotone along each facet.

*Proof.*
- On the open sector S = {n·(q − p\*) > 0, n′·(q − p\*) > 0}, P(q, h + h′) ≥ P(q,h) + P(q,h′) ≥ 0.
- So by Lemma 2.1(b), S is disjoint from the open negative side of every cluster chord ℓ″ of h + h′.
- If ℓ″ passes through p\*, this forces S ⊆ closed positive side of ℓ″, i.e. n″ ∈ cone(n, n′). ∎

## 3. What the R15 contradiction really uses (N12.5)

**Hypothesis (PC) (projective pivot chords).** For each facet F_k of D_T there is a linear map
Γ_k : v_k^⊥ → (𝟙^⊥)\* such that, for every h ∈ relint F_k:
- Γ_k h ≠ 0;
- Cl(h) consists of the single line ℓ_h = {q : Γ_k h·(q − p\*) = 0};
- ℓ_h has the positive side {Γ_k h·(q − p\*) > 0}.

**Hypothesis (NS) (no sliding edge).** At each corner ray r = r_{kj}, Γ_k r ∝₊ Γ_j r. (Γ_k extends linearly to the
closed facet.)

**Theorem 3.1 (PROVED).** Assume (R1), (R2), (PC) and (NS), with T an all-facing triangle in general position (R15 §6).
This includes T1 for every ε ∈ (0,1). Then there is a contradiction, at every interior p\*.

*Proof.* I check that each step of R15/R18 used only (PC) and (NS), plus regularity-free facts proved in §2.

1. *Prior.* Take p\* = u (Prop 1.3).
2. *Chart forms.* Let c_k(h) be the vector with c_k(h)·p\* = 0 and restriction Γ_k h on 𝟙^⊥. Then ℓ_h = {c_k(h)·q = 0}.
3. *Crossing rows* (R15 Thm 1(c)).
   - At a crossing w = w_{ik} ∈ relint F_k, the unique cluster ℓ_w is a limit of good chords from {h_i > 0} and from
     {h_i < 0}. By Lemma 2.1(b), e_i lies on both closed sides, so e_i ∈ ℓ_w and c_k(w)·e_i = 0.
   - Hence c_k(h)_i = λ_{ik} h_i on v_k^⊥.
   - Weak vertex signs (Lemma 2.1(b)) give λ_{ik} ≥ 0.
   - If λ_{ik} = 0, every ℓ_h would pass through e_i. Then the chord of the other crossing w_{i′k} would contain p\*, e_i
     and e_{i′}, which are not collinear. So λ_{ik} > 0.
   - (R15's UVN route is not needed.)
4. *Nonsingularity* (R15 Lemma 3.2). If Γ_k has rank 1, all chords on relint F_k coincide, contradicting the two
   distinct crossing chords. (In T1 every facet has two crossings.)
5. *Corner equations.* These are (NS), written in the R15 §4 forms. In Thm 6.2 they are (6.1).
6. *Box.* Let A ∈ relint F_{k′} near w′ and B ∈ relint F_k near w be as in R15 Lemma 6.1, steps 1–2, with
   σ(A) > σ(B), i.e. their pivot chords cross the open edge in the wrong order.
   - By uniqueness of clusters, good A′ and B′ in small balls have chords uniformly close to ℓ_A and ℓ_B. So
     H(A′) ∩ H(B′) still meets the open edge (a,b).
   - The ratio condition A_b B_a < |A_a||B_b| is open.
   - This contradicts Theorem 2.4 on a set of pairs of positive measure.
   - Hence R15 steps 1–3, which compute σ from c_k(·) alone, give Λ_{ab} ≤ 1. Strict signs and the nondegeneracy
     Γ_k w ≠ 0 at b-crossings hold by items 3–4 (R18 §5 repair).
7. *Conclusion.* R15 Thm 6.2 steps 1–6 are algebra in the quantities ρ_k(i:j) = μ_{ik}/μ_{jk} and the vertices of T.
   With items 3–6 they give e_c ∈ line(v_a, v_c), contradicting general position. For T1 directly:
   x + 1/x = κ + 1 together with x² ∈ [1/κ, κ] is impossible. ∎

**Remark.**
- Theorem 3.1 uses no derivative of P, no (ND), no (NA_w) and no Lemma FS. Every first-order hypothesis in R15 enters
  only through (PC) and (NS).
- The magnitudes of P never matter, only the chord lines. That is why kinks of the form "same chord, different slopes"
  are harmless (§4).

## 4. Kinks: (DD) implies (PC) and (NS) (N12.6)

**Hypothesis (DD).** For each k and each h ∈ relint F_k:
- D(δ,h) := lim_{t↓0} P(p\*+tδ, h)/t exists in ℝ for all δ ∈ 𝟙^⊥;
- δ ↦ D(δ,h) is continuous;
- D(·,h) takes both signs.

Remarks on (DD):
- (DF)+(ND) imply (DD): the derivative is then a nonzero linear function, which is continuous and two-signed.
- One-sided derivatives along rays are allowed to depend nonlinearly on δ. This is the "kink" class E1 of R15 §9.

**Lemma 4.1 (two-slope form; PROVED).** Under (DD), there are α, β > 0 and a unit n ∈ 𝟙^⊥ such that
D(δ,h) = α[n·δ]₊ − β[n·δ]₋.

*Proof.* Write D = D(·,h). D is positively homogeneous of degree 1 and continuous, with D(0) = 0.

1. *Level chords at each scale.* Fix s ∈ ℝ. For small t > 0, Lemma 2.2 applied to the level ts gives a closed half-plane
   E_t ⊆ aff Δ such that P(·,h) ≥ ts on E_t and P(·,h) ≤ ts on the closure of its complement.
   - Write the rescaled half-planes (E_t − p\*)/t = {ν_t·δ ≥ c_t}, with |ν_t| = 1 and c_t ∈ [−∞, ∞].
   - Pass to a subsequence with (ν_t, c_t) → (ν, c).
2. *Separation by a line.* If D(δ) > s, then P(p\*+tδ, h) > ts for small t, so ν_t·δ ≥ c_t. In the limit, ν·δ ≥ c.
   Symmetrically, D(δ) < s gives ν·δ ≤ c.
3. *Positive levels.* Take s > 0.
   - Both {D > s} and {D < s} are nonempty: homogeneity scales up a point where D > 0, and 0 ∈ {D < s}. So c is finite,
     and c ≥ 0 because 0 ∈ {D < s}.
   - Both sets are open (D is continuous). So {D > s} ⊆ {ν·δ > c} and {D < s} ⊆ {ν·δ < c}.
   - Hence D = s on the line L_s := {ν·δ = c}. Since D(0) = 0 ≠ s, c > 0.
4. *The level lines are parallel scalings.* For 0 < s < s′, L_s and L_{s′} are disjoint, hence parallel.
   - Homogeneity puts (s′/s)L_s inside {D = s′}.
   - If (s′/s)L_s ≠ L_{s′}, the two side structures force one of two things:
     - D ≡ s′ on an open strip that avoids 0; but homogeneity moves the strip onto overlapping strips with different
       values;
     - or D ≥ s′ on all of ℝ², contradicting D(0) = 0.
   - So L_s = sL_1, and D(δ) = α n·δ on {n·δ > 0}, where L_1 = {n·δ = 1/α}.
5. *Negative levels.* The same argument at s < 0 gives D(δ) = β n′·δ on {n′·δ < 0}.
6. *The two normals agree.* The open half-planes {n·δ > 0} = {D > 0} and {n′·δ < 0} = {D < 0} are disjoint, and both
   have boundary through 0. Disjoint half-planes of this kind are complementary, so n′ = n. ∎

**Lemma 4.2 (unique clusters; PROVED).** If D(·,h) has the two-slope form, then
Cl(h) = {p\* + n(h)^⊥}, oriented by n(h).

*Proof.* Let ℓ ∈ Cl(h).
- If n·δ > 0, then P(p\*+tδ, h) > 0 for small t. By Lemma 2.1(b), p\*+tδ lies in the open positive side of ℓ.
- If n·δ < 0, the point lies in the open negative side.
- Letting t → 0 puts p\* ∈ ℓ, and the inclusions fix ℓ's normal as n. ∎

**Lemma 4.3 (concavity forces projectivity; PROVED).**
- Fix a facet F_k and an affine section h(τ) = h₀ + τh₁, τ ∈ I (open interval) of relint F_k.
- Put a(τ) = α n and b(τ) = β n, evaluated at h(τ).

Assume (DD) on F_k, and that n is not constant on I (this is automatic in T1; see below). Then a is affine and β/α ≡ ρ_k
is constant. Hence a(h) = Γ_k h with Γ_k linear.

*Proof.*
1. *Concavity in τ.* For each δ, f_δ(τ) := D(δ, h(τ)) is a pointwise limit of the concave functions
   τ ↦ P(p\*+tδ, h(τ))/t. So f_δ is concave, hence continuous.
2. *Continuity of n, α, β.*
   - Suppose n(τ_m) → n\* ≠ n(τ₀). Pick δ with n\*·δ > 0 > n(τ₀)·δ. Then f_δ(τ_m) > 0 for large m, but
     f_δ(τ₀) = −β|n(τ₀)·δ| < 0. This contradicts continuity. So n is continuous.
   - Then δ = n(τ₀) gives continuity of α near τ₀, and δ = −n(τ₀) gives continuity of β.
3. *Second derivatives lie along n.* Fix τ₀ and a small interval J ∋ τ₀ with n(J) inside an arc of length < π/2.
   Let C_J = {δ : n(τ)·δ > 0 for all τ ∈ J}, an open cone.
   - For δ ∈ C_J, a·δ = f_δ is concave on J. For δ ∈ −C_J, b·δ = f_δ is concave on J.
   - Choosing a basis in C_J shows that a and b are locally Lipschitz, with vector-measure second derivatives
     satisfying a″·δ ≤ 0 and b″·δ ≥ 0 for all δ ∈ C_J. So a″ ∈ −C_J\* and b″ ∈ C_J\*, where
     C_J\* = cl cone{n(τ) : τ ∈ J}.
   - Run over rational intervals J and use continuity of n: the polar densities satisfy a″ = −n m_a and b″ = n m_b,
     with m_a, m_b ≥ 0 Radon measures.
4. *Conserved quantities.* d(a × a′) = a′ × a′ dτ + a × da′ = −(a × n) m_a = 0. This uses the product rule for a
   continuous BV factor (a is Lipschitz).
   - So a × a′ ≡ L_a is constant on I, and likewise b × b′ ≡ L_b.
   - Since α ≥ c > 0 locally, n = a/α is Lipschitz, and a × a′ = α² ω, b × b′ = β² ω, with ω = n × n′.
5. *Conclusion.*
   - If L_a = 0, then ω = 0 a.e., so n is constant, contrary to assumption.
   - Otherwise ω ≠ 0 a.e., and (β/α)² = L_b/L_a is constant. So b = ρa with ρ constant.
   - Then (m_b + ρm_a)n = b″ − ρa″ = 0, so m_a = m_b = 0 and a is affine on I.
   - Positive homogeneity, D(δ, λh) = λD(δ,h) hence a(λh) = λa(h), extends a to a linear map on span F_k = v_k^⊥. ∎

**Non-constancy in T1.** Each facet F_k contains two crossings w_{ik} and w_{jk} in its relative interior. By Lemma 4.2
and step 3 of the proof of Theorem 3.1, their chords are line(p\*, e_i) and line(p\*, e_j). These are distinct, so n is
not constant.

**Lemma 4.4 ((DD) implies (NS); PROVED).** This is R15 Thm 1(d), whose proof goes through as follows.
- *Upper bound at the corner.* Concavity in h gives
  limsup_{t↓0} P(p\*+tδ, r)/t ≤ D_k(δ, r) := [Γ_k r·δ]₊ − ρ_k[Γ_k r·δ]₋.
  This is the limit of D(δ,·) along F_k (concavity bound along [r, h₀], then θ → 0, using continuity of the two-slope
  formula). The same bound holds for j.
- *The facet-j limit chord is a cluster at r.* The chords ℓ_h (h ∈ F_j, h → r) converge to the line
  p\* + (Γ_j r)^⊥. By a diagonal argument this line is a cluster chord at r.
- *Matching.* If Γ_k r and Γ_j r were not positively proportional, choose δ with Γ_k r·δ < 0 < Γ_j r·δ.
  - Then P(p\*+tδ, r) < 0 for small t.
  - Lemma 2.1(b) then puts p\*+tδ in the open negative side of that cluster chord, i.e. Γ_j r·δ < 0. Contradiction.
  - (Γ_k r ≠ 0 by item 4 of the proof of Theorem 3.1.) ∎

**Theorem 4.5 (PROVED).** Under (R1), (R2) and (DD) at p\* on the three facets, no all-facing general-position triangle
is realisable on the U-domain. In particular T1 is not realisable, for any ε.

*Proof.* Lemmas 4.1–4.4 give (PC) and (NS). Apply Theorem 3.1. ∎

**What this excludes concretely (CHECKED: each instance satisfies (DD)).**
- Two-slope kinks along the chord (ρ_k ≠ 1). These are allowed but harmless.
- Conical first-order motion K_{p\*+tδ} = T + tW(δ) + o(t), with W positively homogeneous and continuous. Here
  D(δ,h) = h·W_k(δ). Lemma 4.1 forces W_k(−δ) ∥ W_k(δ) and parallel level lines, and Lemma 4.3 then forces W_k to be
  linear on chord directions. In particular piecewise-linear vertex motion with seams along rays from p\* is excluded.
- Split vertices ("needles"): two or more vertices of K_q collapsing to v_k as q → p\*, each with a continuous conical
  first-order motion. Then D(δ,h) = min_j h·W_j(δ). This is continuous, so Lemma 4.1 applies: the needle must be
  radial, and its chord field is projective.

## 5. Beyond directional derivatives (N12.7; CHECKED)

**5.1 Polygonal families.** Suppose that on a punctured neighbourhood N∖{p\*}, K_q is a polygon whose vertex near v_k,
v_k(q), is a local homeomorphism.
- Take q₀ ∈ N∖{p\*} and an open set G of gambles g whose minimiser on K_{q₀} is v_k(q₀).
- For g near G, the level chords of P(·,g) near q₀ are v_k^{-1}(lines) (Lemma 2.2). This is an open set of lines.
- By the local fundamental theorem of projective geometry (a continuous injective map of a planar domain sending
  collinear triples to collinear triples is projective), v_k is projective near q₀.
- Projective maps that agree on open sets coincide, so v_k is a single projective map on the connected set N∖{p\*}. It
  extends continuously, hence projectively, to p\*. So (DF) and (ND) hold, and Theorem 4.5 applies.

Two further cases:
- *Vertex splitting with projective pieces* P₁ ≠ P₂ requires the chords of P₁ and P₂ to coincide for every h ∈ F_k.
  That forces P₂ to be a perspective image of P₁ from v_k, which is again two-slope and radial.
- *Rank-one vertex maps* v_k = γ∘φ give all facet gambles the same chord {φ = φ(p\*)}. This is impossible with two
  crossings.

**5.2 Smooth dual charts (flat facets allowed).**
- Dualise: points of the dual m-plane are lines L = {m·g = c}. The map Λ(L) = (chord of L)\* sends the tangent-line
  curve C_q of K_q (a convex curve, convex toward the polar interior, which is the same side for all q near p\*) into
  the pencil q\*.
- Λ maps the facet segment F_k\* ⊆ C_{p\*} into the line p\*\*. Choose coordinates in which p\*\* = {y = 0} and
  Λ^{-1}(x, y) = (X, Y), with Y(x, 0) = 0 and X(x, 0) = s(x). Projectivity of the chord map means s is Möbius.
- Lines through (x₀, 0) with slope m correspond to priors on the chord ψ(x₀); m = 0 corresponds to p\*. Both signs of
  m occur.
- Assume Λ^{-1} is C² near F_k\* with w(x) := Y_y(x, 0) ≠ 0. To first order in m, the signed curvature of
  Λ^{-1}(line) is m·{s′[(x−x₀)w]″ − s″[(x−x₀)w]′}.
- Convexity on the same side for both signs of m forces the braces to vanish for all x and x₀. That is the pair
  s′w″ = s″w′ and 2s′w′ = s″w.
- With A = s″/s′ this gives A′ = A²/2, so A = −2/(x + C) or A = 0. Hence s = D − K/(x + C), a Möbius map.
  (`ode_check.py` confirms that the residual vanishes for Möbius s and does not vanish for s = x + x³.)

This hypothesis does not involve the q-derivative of P. It therefore excludes first-order-flat facets (P = o(t))
whenever the dual chart is C² and transversally nondegenerate. Status: CHECKED. The curvature expansion was done by
hand and checked symbolically, but not written to journal standard.

## 6. Finitely additive penalties (N12.8)

**Setting.**
- Loss at world i: L_i(X) = ν_i(E_i(X)), where E_i(X) = X △ (U ∩ {g_i > 0}) and ν_i is a bounded charge on the
  measurable sets of U that vanishes on μ-null sets.
- Yosida–Hewitt: ν_i = ν_i^c + ν_i^p, with ν_i^c countably additive (density ℓ_i) and ν_i^p purely finitely additive.
- Strict (G) on improvement sets away from S is seen only by ν^c. Hence ℓ_i > 0 a.e. off S (*).

**Prop 6.1 (PROVED).** Suppose each ν_i^p is carried by every neighbourhood of a closed μ-null set S, i.e.
|ν_i^p|(U ∖ N_η(S)) = 0 for every η > 0. Let X be a Bayes model at an interior q, i.e. a minimiser of
Σ_i q_i L_i over the domain, and assume the countably additive Bayes rule R_q := {g ∈ U : q·c(g) > 0}, with
c_i := ℓ_i-differences, has null ties. Then X = R_q a.e.

*Proof.*
- Suppose μ(Y) > 0 for Y := (X △ R_q) ∖ N_η(S) and some η.
- Let X′ agree with R_q on Y and with X elsewhere. X′ is in the domain, which is closed under splicing.
- The purely finitely additive terms do not change, because Y avoids N_η(S).
- The countably additive term strictly decreases, by ∫_Y |q·c| dμ > 0. This contradicts minimality.
- Hence X = R_q a.e. off every N_η(S), and therefore a.e., because ∩_η N_η(S) = S is null. ∎

**Consequence.** Charges concentrated near ∂D_T, or near finitely many seams, change nothing. Requirements (R1) and (R2)
become requirements on the countably additive field c, and Theorem 4.5 and the open gap apply verbatim. A purely
finitely additive part therefore cannot "mimic a kink" in this regime.

**CONJECTURE N12.C2.** The same holds for arbitrary purely finitely additive parts. These can be carried by sets that
are dense near every point, where the splice argument fails.

Status of the reduction: if a Bayes minimiser exists, its restriction to any open set disjoint from the carrier
coincides with R_q. Not proved in general.

## 7. The exact remaining gap

Combining §§2–4, a realisation of T1 must fail (PC) or (NS) on some facet or corner of T. By Theorem 4.5 it must
therefore fail (DD) there. By Prop 2.5 and Lemma 2.1, the failure has one of exactly these forms:

- **(G1) Pivot degeneracy / vertex pinning.** For h in an open arc of F_k, P(·,h) ≡ 0 near p\*. Then v_k ∈ K_q for all
  q near p\* (Prop 2.5(c)).
  - The plateau theorems (R10b Thm PL, N3 PL_θ) exclude K_q = T on open sets, not the pinning of a single vertex.
  - Not excluded here.
- **(G2) Non-unique clusters**, or **(G3) a non-projective pivot chord map**, on a facet where D(·,h) fails to exist or
  to be continuous. In that case:
  - P(p\*+tδ, h)/t oscillates as t ↓ 0, or depends discontinuously on δ;
  - the chord map ψ_k : relint F_k → pencil(p\*) is still monotone (Prop 2.6), passes through line(p\*, e_i) at the
    crossings, and keeps K_q tangent to L_h along each whole chord (Prop 2.5(b)).
- **(G4) Sliding edge at a corner** (two distinct limit chords), in the same non-(DD) setting.

**CONJECTURE N12.C1 (projective pivot lemma).** In every realisation on the U-domain, (PC) and (NS) hold
at p\*. By Theorem 3.1 this would give the full additive core (B) for T1 with merely measurable c.

Evidence for N12.C1:
- It holds in every regularity class examined: (DD); polygonal families; C² dual charts.
- The obstruction is second-order and two-sided (§5.2): chords through p\* must bend consistently for priors on both
  sides of p\*. This uses only convexity of the C_q, and suggests a synthetic proof via three-curve convexity
  inequalities.
- NUMERICS (§8): within two-slope data the projective class is exactly the feasible one.

Suggested route to prove N12.C1:
- Use the scaling-invariant compact set of blow-up limits of P(p\*+t·, ·)/m(t), with m(t) the facet sup-rate.
- Lemma 2.2 makes each blow-up a ridge function φ_h(n(h)·δ); this part is PROVED by the argument of Lemma 4.1 with
  homogeneity dropped, provided K_q is Lipschitz at p\*.
- Lemma 4.3 needs only the slopes of φ_h at 0. The missing piece is an argument that some blow-up in the compact
  scaling-orbit closure has one-sided slopes at 0, for example a minimal or recurrent element of the scaling flow.

No construction is in sight: every kink mechanism one can write down with continuous first-order data is excluded, and
the residual classes (G1)–(G4) are oscillatory or pinned.

## 8. Numerics and files (`n12py/`)

| File | What | Result |
|---|---|---|
| `ode_check.py` | sympy: the §5.2 second-order condition | only Möbius s survive (residual 0); s = x + x³ gives residual 3(1−6x²)/√(3x²+1) ≠ 0 |
| `twoslope_lp.py` | LP: given a chord field n(τ), search over all two-slope data α, β ∈ [1, 50] for concavity of τ ↦ D(δ, h(τ)) for 180 directions δ | projective n: violation 0. Non-projective (θ = θ_proj + ε sin²(πτ), ε = .05, .2, .5; linear angle): violation > 0 |
| `twoslope_scaling.py` | grid refinement (N = 21, 41, 81) | violation/h² = 3.38, 3.47, 3.50: a genuine continuum second-derivative defect, as Lemma 4.3 predicts |

NUMERICS only; Lemma 4.3 is the proof.
