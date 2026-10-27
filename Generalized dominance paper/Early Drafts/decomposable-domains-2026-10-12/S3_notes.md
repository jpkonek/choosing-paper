# S3. Mirrored simple pairs (R1): construction side

15 Oct 2026, round 13 (BRIEF12, task (R1), construction side). Labels: **PROVED** (full proof here), **CHECKED**
(complete up to a cited result or a routine verification sketched here), **CONJECTURE**, **NUMERICS** (scripts in
`s3py/`, run with `python3 -I`; no proof depends on them). No assumption is added to the framework. Terminology as in
termfix/TERMFIX_RULES.md: M_U is the class of evaluable models D ⊆ U = D_{K′}; this restricts only which models are
evaluated.

---

## 0. Outcome

**No construction of (R1).** I did not find a two-world nested system with every axiom (closed sections for every
model) and a non-null Z with Z ≤₁ A for all A in a uniformly Cesàro-thin family.

**What was obtained.**

1. **S3.1 (PROVED). (R1) holds if closed sections are dropped at both worlds.** A mirrored "band ∪ translates"
   system has strict (G), (IB), (LA), competitiveness, undominatedness, no tie partners, (C), C_L = the selection
   (so (Nest)), (LF) at every interior C_b, and mirrored simple certificates through one disjoint family:
   c_a ≤₁ A_j and d_{b₀} ≤₂ A_j for all j. Both worlds fail SP^reg. This realises the "ping-pong" of Q1 §4 D and
   Prop N2, which was neither realised nor refuted before. Only closed sections fail, at both worlds.
2. **S3.2 (PROVED). In this architecture, closedness is exactly a measure bound on the targets.** Take any world 1
   of the form band ∪ ⋃_{F∈𝓕} 𝒢(F) (Q1's form, any family 𝓕, any world 2). For the test models
   D_{d,h} = [a,a+d) ∪ [1−h,1),
   S₁(X_{D_{d,h}}) = [0, a+d+h − inf{μ̄(F) : F ∈ 𝓕, G_F ≤ G_D}].
   So the section is closed iff that infimum is attained. Hence: **all world-1 sections closed ⟹
   min_{F∈𝓕} μ̄(F) = κ > 0 ⟹ inf{μ̄(A) : Z ≤₁ A} > 0 for every non-null Z.** That rules out (R1). Q1.3's example is
   one instance (β_{A_j} = a+d+h − μ̄(A_j), which matches the numbers there exactly). The formula sees only μ̄(F), so
   thinness in the radial direction does not help.
3. **S3.3 (PROVED). Packing lemma.** In any system satisfying (H): if Z ≤₁ A, then A ≰₁ Q for every Q inside the
   Lemma-T₁ neighbourhood of 1 (or of any finite set of points) for Z. If a world accepts "right-packing"
   A ≤₁ [1−μ̄(A),1) for members of 𝒰₁(Z) of arbitrarily small measure, then one application of the limit rule (R5)
   produces outcome (a), Z ≤₁ ∅. This is the mechanism behind every failure in Q1, N3 and S3.1–S3.2. A band (any
   unanimity over x-increasing densities) always accepts right-packing.
4. **S3.4 (PROVED). The radial route fails at (K).** Take worlds of the form "fibrewise band ∪ translates by
   generators with a fat negative part" (the transverse design the brief suggested). They leave small cut pairs
   that cross fibres decided by neither world. Translates can decide only cut pairs that carry positive mass at least
   min_F μ̄(F), so small cut pairs must be decided by the cones, and fibrewise cones are not jointly complete on them.
5. **What the failures suggest (CONJECTURE S3.C1, for the exclusion side).** (QC) For every non-null Z,
   κ₁(Z) := inf{μ̄(A) : Z ≤₁ A} > 0, and the mirror statement for world 2.
   - (QC) implies ¬(R1) (PROVED, §4).
   - (QC) is what closedness gives exactly in the architecture of S3.2.
   - (QC) fails in S3.1, where closedness is dropped.
   - (QC) is proved when the partner world has a strictly positive, uniformly absolutely continuous endorsing charge
     (Q1.6(a)).
   - A proof in general needs exactly the missing quantitative ingredient: a way to turn "Z ≤₁ A with μ̄(A) small"
     into "Z ≤₁ Q with Q concentrated near finitely many points". That is a packing step, which by S3.3 is the only
     way closedness has ever been seen to bite.

---

## 1. Setting (recalled)

(Nest), n = 2, as in write-up §8.4(c), §8.5(c).
- M is the set of mixed problems of U, with the chain c_b (μ̄(c_b) = b), d_b = M ∖ c_b and slabs [s,t) = c_t ∖ c_s.
  N₊ is the set of nonnegative problems of U.
- x(h) := inf{b : h ∈ c_b} on M; its image measure is Lebesgue measure on [0,1].
- A model X is (A, N), with A = E₁X ∩ M and N ⊆ N₊ the unaccepted nonnegative problems. Then E₁X = A ∪ N and
  E₂X = (M ∖ A) ∪ N.
- World i is a monotone, cancellative order ≤_i on world-i error sets. Equivalently it is an acceptance set 𝒜_i of
  {−1,0,1}-valued δ = 1_{worse} − 1_{better} that contains every δ ≥ 0, contains no nonzero δ ≤ 0, and is closed
  under sums that stay {−1,0,1}-valued (N17.1(a), N9.4).

The axioms in cut form (Lemma cutform, Q1.0):
- **(K)** For every model (A, N) and every b ∈ (0,1): c_b ≤₁ A ∪ N or d_b ≤₂ (M∖A) ∪ N.
- **(U)** No model other than C_b has both A ∪ N ≤₁ c_b and (M∖A) ∪ N ≤₂ d_b. This gives undominatedness and no tie
  partners.
- **(Cl)** For every W ⊆ U:
  - {b : c_b ≤₁ W} is closed. It is an initial segment, so this says: c_b ≤₁ W for all b < β implies c_β ≤₁ W.
  - Mirror for world 2 with final segments.
  - This is the limit rule (R5) restricted to the selection (Thm R5).

---

## 2. S3.1: mirrored simple pairs with every axiom except closed sections (PROVED)

### 2.1 The system

*Problem side.* As in Q1 §2.1:
- n = 2, K′ = [k₁,k₂] ⊂ (0,1).
- The coherent path C_b = D_{[α(t),β(t)]}, reparametrised so that μ̄(c_b) = b.
- The selection is p ↦ C_{b(p₂)}.
- Every interior C_b has a credal set strictly larger than K′ on both sides, so (LF) holds at it with N = U.

*Parameters.*
- Fix 0 < a < b₀ < 1.
- Fix a family 𝒜 = {A_j} of pairwise disjoint non-null subsets of d_a with A_j ∩ c_{b₀} non-null. For example,
  take the dyadic family of Q1.3 inside [a,1) and keep the members that meet [a,b₀).
- Put F′_j := A_j ∩ c_{b₀}.

*Tails and heads.* For δ put:
- τ_δ(x) := ∫_{x(h)≥x} δ dμ̄ (world 1; N₊ placed at x = 2, so it enters every tail with x ≤ 2);
- η_δ(x) := ∫_{x(h)≤x} δ dμ̄ (world 2; N₊ placed at x = −1, so it enters every head with x ≥ −1).

*World 1.* This is Q1's world 1 verbatim:
- band₁ = {τ_δ ≥ 0 on [0,2]};
- 𝒢₁(A_j) = {τ_δ ≥ τ_{g_j} on [0,2]}, with g_j = 1_{A_j} − 1_{c_a};
- 𝒜₁ = band₁ ∪ ⋃_j 𝒢₁(A_j).

*World 2.* This is the mirror image under x ↦ 1 − x:
- band₂ = {η_δ ≥ 0 on [−1,1]};
- 𝒢₂(F′_j) = {η_δ ≥ η_{g′_j} on [−1,1]}, with g′_j = 1_{F′_j} − 1_{d_{b₀}};
- 𝒜₂ = band₂ ∪ ⋃_j 𝒢₂(F′_j).

### 2.2 Claims

**(i) Both worlds have strict (G) and (IB).**
- World 1 is Q1.1.
- World 2 is Q1.1 transported by x ↦ 1 − x. Under this map:
  - d_{b₀} becomes the initial segment c_{1−b₀};
  - F′_j becomes a subset of d_{1−b₀};
  - heads become tails;
  - N₊ is still on the side that enters every condition.
- The key step of Q1.1 (common negative part and compatibility s + t ≥ −1) is unchanged.

**(ii) (K) for every model.** It is already supplied by the two bands. Let X = (A, N) and b ∈ (0,1). Suppose both
fail.
- If band₁ rejects 1_{A∪N} − 1_{c_b}, then for some x₁ < b we have μ̄(N) + μ̄(A ∩ [x₁,1)) < b − x₁. Hence
  μ̄([x₁,b) ∖ A) > μ̄(N) + μ̄(A ∩ d_b).
  (The conditions at x ≥ b and on (1,2] hold automatically.)
- If band₂ rejects 1_{(M∖A)∪N} − 1_{d_b}, then for some x₂ > b we have μ̄(N) + μ̄([0,x₂) ∖ A) < x₂ − b. Hence
  μ̄([b,x₂) ∩ A) > μ̄(N) + μ̄(c_b ∖ A).
- Combining the two:
  μ̄([x₁,b)∖A) > μ̄(N) + μ̄(A∩d_b) ≥ μ̄(N) + μ̄(A∩[b,x₂)) > 2μ̄(N) + μ̄(c_b∖A) ≥ μ̄([x₁,b)∖A).
  This is a contradiction.

**(iii) (U): no dominating or tied model.** Suppose X = (A, N) has δ₁ := 1_{c_b} − 1_{A∪N} ∈ 𝒜₁ and
δ₂ := 1_{d_b} − 1_{(M∖A)∪N} ∈ 𝒜₂.
- On (1,2], τ_{δ₁} = −μ̄(N), while every condition there requires a value ≥ 0. So N = ∅.
- Put P = c_b ∖ A and Q = A ∖ c_b. Then δ₁ = 1_P − 1_Q.
  - If δ₁ ∈ band₁, then τ(b) = −μ̄(Q) ≥ 0, so Q = ∅.
  - If δ₁ ∈ 𝒢₁(A_j) and b ≤ a, then δ₁ ≤ 0 on d_a, so τ_{δ₁}(a) ≤ 0 < μ̄(A_j). This is impossible.
  - If δ₁ ∈ 𝒢₁(A_j) and b > a, then −μ̄(Q) = τ_{δ₁}(b) ≥ G_{A_j}(b) ≥ 0, so Q = ∅.
- With Q = ∅, δ₂ = −1_P is nonpositive and accepted at world 2, so P = ∅ by (i).
- So X = C_b. (Vertices: P₁ and P₂ are the unique world-best models.)

**(iv) C_L = the selection, (LA), (C).** Fact 0 cannot be cited, because sections are not closed. The direct
argument of the Q12 repair works instead.
- Fix X. The band sections are closed:
  - {b : 1_{E₁X} − 1_{c_b} ∈ band₁} = [0, β₁(X)], since the defining inequalities are continuous in b;
  - {b : … ∈ band₂} = [β₂(X), 1], likewise.
- By (ii) these two sets cover [0,1], so some b* has C_{b*} ⪯₁ X and C_{b*} ⪯₂ X.
- By (iii) X ≠ C_{b*} is dominated. So the undominated models are exactly the selected ones, C_L is the selection,
  (LA) holds, and (C) holds vacuously.

**(v) Mirrored simple certificates, uniformly Cesàro-thin.**
- g_j ∈ 𝒢₁(A_j), so c_a ≤₁ A_j: this is C_a ⪯₁ X_j with E₁X_j = A_j.
- g′_j ∈ 𝒢₂(F′_j), so d_{b₀} ≤₂ F′_j ⊆ A_j, and hence d_{b₀} ≤₂ A_j by monotonicity. Both are relevant
  comparisons.
- The A_j are pairwise disjoint, so the family is uniformly Cesàro-thin: the averages (1/J)Σ_{j≤J} 1_{A_j} have sup
  norm 1/J.
- Every ν ∈ 𝒱₁ has ν(c_a) ≤ inf_j ν(A_j) = 0, and every ν ∈ 𝒱₂ has ν(d_{b₀}) ≤ inf_j ν(F′_j) = 0.
- So ¬SP^reg holds at **both** worlds, in mirror image, with the **same** targets. This is exactly the
  configuration of (R1) and Props N1, N2.

**(vi) What fails.** Closed sections fail at both worlds (§3). Everything else above holds for every model.

NUMERICS `s3py/mirror_pair.py` (+ `.out`). Setting: a 128-cell grid in x, one N₊ cell, a = 1/4, b₀ = 3/4, and
8 disjoint spread A_j. Results:
- the generators are accepted;
- 1500 compatible pairs of random members per world: every sum is accepted;
- 4000 random nonpositive vectors: none is accepted;
- 400 random models at all 127 interior cuts: 0 failures of (K) and 0 failures of (U);
- the world-1 section ends for D = [a,a+d) ∪ [1−h,1) are 52/128 = a + d + h − μ̄(A_j) (μ̄(A_j) = 3/32 for every
  j), against the band value 32/128. This agrees with S3.2.

---

## 3. S3.2: closedness ⟺ attained target measure, in band ∪ translates worlds (PROVED)

**Proposition S3.2.** Let world 1 be band₁ ∪ ⋃_{F∈𝓕} 𝒢₁(F) as in Q1, with any family 𝓕 of non-null subsets of d_a,
and let world 2 be arbitrary. Let 0 < d, h with a + d + h < 1 − h. Put D := [a,a+d) ∪ [1−h,1), let X_D be regular
with E₁X_D ∩ M = D, and put 𝓕_D := {F ∈ 𝓕 : G_F ≤ G_D on [a,1]}. Then:
- (a) for F ∈ 𝓕_D, β_F(D) = a + d + h − μ̄(F); for F ∉ 𝓕_D the contribution is empty; the band contributes
  [0, d+h];
- (b) S₁(X_D) = [0, a + d + h − inf_{F∈𝓕_D} μ̄(F)] if the infimum is attained, and [0, a + d + h) if it is 0 and
  not attained;
- (c) 𝓕_D contains every F with μ̄(F) ≤ h;
- (d) consequently, if inf_{F∈𝓕} μ̄(F) = 0, then S₁(X_{D_{d,h}}) is not closed for every admissible (d, h). If every
  world-1 section is closed, then κ := min_{F∈𝓕} μ̄(F) > 0 exists, and every A with Z ≤₁ A satisfies
  μ̄(A) ≥ min(μ̄(Z), κ).

*Proof.*
- (a) Q1.3 gives β_F(D) = min(1, min_{x∈[a,1]} (x + G_D(x) − G_F(x))) for F ∈ 𝓕_D. The function x + G_D(x) takes
  these values:
  - a + d + h on [a, a+d];
  - x + h on [a+d, 1−h];
  - 1 on [1−h, 1].
  Also G_F(x) ≤ G_F(a) = μ̄(F) for x ≥ a. So the minimum is a + d + h − μ̄(F), attained at x = a, and it is ≤ 1.
  The band value is min(μ̄(D), a + d + h) = d + h.
- (b) S₁ is the union of the band part and the sets [0, β_F]. Every β_F < a + d + h, and β_F > d + h once
  μ̄(F) < a.
- (c) Check G_F ≤ G_D piece by piece:
  - on [a, a+d], G_D ≥ h ≥ μ̄(F) ≥ G_F;
  - on [a+d, 1−h], G_D = h ≥ μ̄(F);
  - on [1−h, 1], G_D(x) = 1 − x ≥ μ̄(F ∩ d_x) = G_F(x).
- (d) The first claim follows from (b) and (c), because members of arbitrarily small measure lie in 𝓕_D. If every
  section is closed, the infimum over 𝓕 is attained at some non-null F, so it is positive. For the bound on μ̄(A):
  - if Z ≤₁ A through the band, τ(0) ≥ 0 gives μ̄(A) ≥ μ̄(Z) (on M);
  - if through 𝒢₁(F), the condition at x = a gives μ̄(A ∩ d_a) ≥ μ̄(F) + μ̄(Z ∩ d_a) ≥ κ. ∎

*Readings.*
- Q1.3 is the instance 𝓕 = dyadic family: μ̄(A_j) = 0.7·2^{−j}, so β = 0.5 − 0.0875 = 0.4125, 0.45625, …. This
  agrees with q13_sections.out to all printed digits.
- The section depends on F only through μ̄(F). Making the targets thin in the radial (transverse) direction changes
  nothing, because any uniformly Cesàro-thin family has inf μ̄(A) = 0 (take ν = μ̄ in N1(b)).
- The brief suggested finding a thin family whose profiles {G_F} are compact. That is impossible:
  ‖G_F‖_∞ = μ̄(F), so 0 is always a limit point. The real requirement is attainment, which thinness excludes.
- The same computation applies to world 2 of S3.1 by mirror symmetry. With
  D′ = (1−a′−d, 1−a′] ∪ (0, h] and a′ := 1 − b₀, S₂(X_{D′}) is a half-open final segment.

---

## 4. S3.3: the packing lemma and its one-step (R5) reversal (PROVED)

Assume (Nest), strict (G), (IB), (K) and closed sections at regular models (no (C) or (LA) needed).

**Lemma S3.3.**
- (a) Let Z be non-null and let η = η(Z) be the radius of Lemma T₁ at x = 1. If Z ≤₁ A, then A ≰₁ Q for every
  non-null Q ⊆ d_{1−η}. The same holds with d_{1−η} replaced by the union of the Lemma-T₁ neighbourhoods of any
  finite set of points. Mirror for world 2 with W = d_{b₀}, using Lemma T₂ near 0.
- (b) Drop the closedness assumption and keep only (G) and (IB). Suppose Z ⊆ c_s with s < 1, and suppose there are
  A_k with Z ≤₁ A_k ≤₁ [1−m_k, 1), m_k → 0. Then one application of (R5) to the model W := M ∖ Z installs
  Z ≤₁ ∅, which is outcome (a) of the exact consistency test.

*Proof.*
- (a) By transitivity Z ≤₁ Q, which Lemma T₁ excludes.
- (b) Take b ∈ (s, 1) and k with 1 − m_k > b. Then
  - c_b ∖ W = Z ∩ c_b, and W ∖ c_b = d_b ∖ Z ⊇ [1−m_k, 1);
  - Z ∩ c_b ≤₁ Z ≤₁ [1−m_k, 1) ≤₁ d_b ∖ Z, by monotonicity and transitivity;
  - so c_b ≤₁ W for every b < 1.
  (R5) at b = 1 installs M ≤₁ M ∖ Z, which by cancellation is Z ≤₁ ∅. ∎

*Use.*
- A band (unanimity over x-increasing densities) accepts A ≤₁ [1−μ̄(A), 1): the tails of 1_{[1−m,1)} − 1_A are
  ≥ 0 when m = μ̄(A).
- So a world containing a band admits no simple certificate whose targets have vanishing measure. This covers Q1,
  S3.1 and S3.2.
- The tilt world N3 is the same mechanism with the targets packed into a slab (Lemma DL).
- **Any construction of (R1) needs both worlds to refuse packing of their thin targets, toward 1 at world 1 and
  toward 0 at world 2, while staying jointly complete on cut pairs (K).**

---

## 5. S3.4: the transverse (radial) route fails at (K) (PROVED for the design tried)

Identify M with [0,1]_x × [0,1]_y (chain coordinate × radial coordinate; this is an isomorphism of measure algebras
that preserves the chain). The brief's idea was to block packing by making the cones fibrewise:
- world 1 = fband₁ ∪ ⋃_j (g_j + fband₁), where fband₁ = {δ : τ_{δ(·,y)} ≥ 0 for a.e. y} (and A_j = [a,1) × Y_j
  with the Y_j disjoint);
- world 2 = the mirror image, with fband₂ (heads) and translates by g′_j.

Fibrewise cones never move mass across fibres, so they never accept right-packing of A_j. Lemma S3.3 is avoided.

**Claim S3.4.** (K) fails. Fix b ∈ (a, b₀), disjoint Y′, Y″ of equal positive measure, and ε > 0 with
a < b − ε and b + ε < b₀. Put P := [b−ε, b) × Y′ and Q := [b, b+ε) × Y″, so that μ̄(P) = μ̄(Q). Let X be the regular
model with E₁X ∩ M = (c_b ∖ P) ∪ Q. Then neither world accepts its competitive comparison.

*Proof.*
- 1_Q − 1_P ∉ fband₁: on fibres y ∈ Y′ the tail at b − ε is −ε < 0.
- 1_P − 1_Q ∉ fband₂: on fibres y ∈ Y″ the head at b + ε is −ε < 0.
- 1_Q − 1_P ∉ g_j + fband₁: integrating the fibre tails over y, membership would give the global tail condition
  τ_{1_Q−1_P}(a) ≥ τ_{g_j}(a) = μ̄(A_j). But τ_{1_Q−1_P}(a) = μ̄(Q) − μ̄(P) = 0, because P, Q ⊆ d_a.
- 1_P − 1_Q ∉ g′_j + fband₂: the mirror computation at x = b₀ requires η ≥ η_{g′_j}(b₀) = μ̄(F′_j) > 0. But
  η_{1_P−1_Q}(b₀) = μ̄(P) − μ̄(Q) = 0, because P, Q ⊆ c_{b₀}.
- So C_b ⋠₁ X and C_b ⋠₂ X: C_b is not competitive. ∎

*General form (PROVED by the same computation).* In any world of the form K ∪ ⋃_F (g_F + K), with K contained in
the global band cone (tails, or heads at world 2) and generators g_F = 1_F − 1_{c_a} (or 1_F − 1_{d_{b₀}}), every
translate member δ has ‖δ⁺‖₁ ≥ μ̄(F). So cut pairs with μ̄(P) + μ̄(Q) < inf_F μ̄(F) can be decided only by the cones.
Then:
- if inf_F μ̄(F) > 0, the cones must be jointly complete on small cut pairs, and fibrewise cones are not;
- if inf_F μ̄(F) = 0 (thin families), translates can decide arbitrarily small pairs, but S3.2 shows that sections
  then fail to close whenever K contains the band, and S3.3 shows the same for any K that packs.

I found no cone that is jointly complete on cut pairs with its mirror partner and contains no packing moves. The
global bands are jointly complete (S3.1(ii)) and pack. Fibrewise bands do not pack, and they are not jointly complete.
Intermediate classes I tried also fail one side or the other, each with a two-cell counterexample of the S3.4 kind:
- "unanimity over densities f(x)g(y) with f monotone" is again fibrewise;
- "first-order dominance after a measure-preserving fibre rearrangement" packs.
These are failure reports, not theorems.

*Other designs tried (failure reports, not proved in general).*
- **Unanimity over lexicographic charge vectors.** Each member's leading level endorses every world-i acceptance. So
  under ¬SP all leading levels vanish on c_a. A W = d_{a/2} section is then an intersection of sections [0, β_θ)
  that are open at the point β_θ where θ's leading level runs out (the Thm E2 mechanism). It is closed only if some
  member closes strictly below every open end. In every concrete family I tried this regresses without end. CONJECTURE:
  such worlds satisfy SP^reg under (Nest) with (K).
- **Directed unions of closed cones** (the tilt type). Every section is a union of closed initial segments, and it
  is closed iff its supremum is attained. For W = c_x ∖ Z the supremum is attained only by a member that already
  packs (N3, S3.3).

---

## 6. The quantitative statement suggested for the exclusion side

**(QC_i) CONJECTURE S3.C1.** Under (Nest) and every axiom with closed sections for every model, for every non-null Z:
- κ₁(Z) := inf{μ̄(A) : Z ≤₁ A} > 0;
- κ₂(W) := inf{μ̄(A) : W ≤₂ A} > 0.

Status:
- **(QC₁) ⟹ ¬(R1) (PROVED).** A uniformly Cesàro-thin 𝒜 has inf_A ν(A) = 0 for every charge (N1(b)), in particular
  for ν = μ̄. So 𝒜 ⊆ 𝒰₁(Z) would give κ₁(Z) = 0.
- (QC) is strictly stronger than ¬(R1). Targets of vanishing measure that are nested (with a free filter) are not
  Cesàro-thin.
- (QC₁) holds in every band ∪ translates world with closed sections (S3.2(d)), and in every system whose world 2 has
  a strictly positive, uniformly absolutely continuous endorsing charge (Q1.6(a)).
- (QC) fails at both worlds in S3.1, where only closedness is missing. So (QC) is exactly where closedness must bite.
- (QC) is equivalent to: no non-null Z is ≤₁ a sequence of sets of vanishing measure. This is the measure analogue
  of Lemma T, which handles sets shrinking to finitely many points of the chain. Lemma T is proved by packing the
  targets with DR and then dropping them with DL. A proof of (QC) needs a packing step for spread targets: from
  "Z ≤₁ A with μ̄(A) < κ" derive "Z ≤₁ Q ∪ R with Q in a fixed neighbourhood of finitely many points and μ̄(R) small".
  That is the "uniform DR" of P4B §8.5 in measure form, and the rate of (R3) is the natural route to it.
- By S3.3, no system can accept the packing itself. A proof must therefore get the packing from (K) at cuts near 1,
  where world 2 must accept d_t ≤₂ A (MP(a)), together with closedness at world 2.

---

## 7. Status table

| Item | Status |
|---|---|
| S3.1 mirrored band ∪ translates: every axiom except closed sections, (Nest), mirrored simple certificates, ¬SP at both worlds | PROVED; NUMERICS `mirror_pair.py` |
| S3.2 exact sections β_F = a+d+h−μ̄(F); closedness ⟺ min μ̄(F) attained ⟹ (QC) | PROVED |
| S3.3 packing lemma; one (R5) step gives outcome (a) | PROVED |
| S3.4 fibrewise (radial) design fails (K); general form for K ∪ translates | PROVED (design tried); other designs failure reports |
| unanimity of lexicographic charges / directed unions | failure reports; CONJECTURE (SP^reg) |
| S3.C1 (QC) | CONJECTURE; (QC) ⟹ ¬(R1) PROVED |
| (R1) | open; no construction |

*Axioms.* S3.1 verifies, for **every** evaluable model: strict (G), (IB), (LA), competitiveness, undominatedness, no
tie partners, (C), C_L = the selection, (LF) at interior C_b. It fails exactly closed sections, at both worlds (S3.2
and its mirror). S3.3(a) uses Lemma T (closed sections, (K), strict (G)); S3.3(b) uses only (G), (IB) and (R5).
**No assumption is added to the framework.**

## 8. Files (`s3py/`, run with `python3 -I`)

- `mirror_pair.py` (+ `.out`): the S3.1 system on a 128-cell grid. It checks the generators, sum-closure (1500 pairs
  per world), exclusion of nonpositive vectors (4000), (K) and (U) (400 models × 127 cuts), and the world-1 section
  ends against S3.2. No proof depends on it.
