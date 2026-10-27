# WT65: check of the auditor's two tools (26 Oct 2026)

Labels: PROVED / CHECKED (exact computation) / NUMERICS. Scripts are in `wt65py/`.

## 0. Status table

| # | Item | Verdict | Notes |
|---|------|---------|-------|
| T1 | Density-point witness (AUDIT_r65_brief, "A finite geometric witness"), both directions | **CORRECT** | Both directions hold as stated, with r ≤ n. It sharpens to an exact formula, **hull(B) = cone(B_d) + int ℝⁿ₊**, with no closure (Lemma W1), and to **r ≤ n−1** (Lemma W2). |
| T1a | "every q ∈ Q_B is non-negative on each density point b_j" | CORRECT | Open half-space plus density one plus (M) (W1, Claim 0). |
| T1b | Margin η uniform in q | CORRECT | η = min_i p_i, because q ∈ Δ and q·b_j ≥ 0. |
| T1c | hull(B) = int C, C = cl cone(B_d ∪ ℝⁿ₊), when B_d is not closed | CORRECT | Needs Q_B = {q ∈ Δ : q·b ≥ 0 on B_d}, which uses the Lebesgue density theorem. W1 gives a direct separation proof that avoids the closure altogether. |
| T1d | Carathéodory step, and "absorbing nonnegative generators" | CORRECT | The absorbed generators add a vector in ℝⁿ₊, so strict positivity is kept. |
| T1e | Case r = 0 | CORRECT | r = 0 ⟺ A_d ∩ int ℝⁿ₊ ≠ ∅ ⟺ μ(A ∩ int ℝⁿ₊) > 0. This is ES64 Prop 5.4's case. |
| T1f | n or n+1 generators? | **n−1 suffice, and n−1 is sharp** (PROVED, CHECKED) | n+1 are never needed. n suffice for any B (conic Carathéodory). n−1 suffice once Q_B meets relint Δ, which always holds here since K' ⊆ Q_B. n−1 is attained for every n ≥ 2 and every K'. Without one-sidedness n can be needed. In three worlds: **two** removed density points suffice. |
| T2 | Compactness tool | **CORRECT** | All four checks pass (C1–C3). The defenders must range over Q ⊇ K'; nothing is lost, because D_Q ∩ U = D_{conv(Q∪K')}. |
| T2a | Null zero set via P_Q(h+t𝟙) = P_Q(h)+t | CORRECT | Z_Q is the graph of a continuous function over 𝟙^⊥, so it is Lebesgue-null and hence μ-null by (M). |
| T2b | Dominated convergence | CORRECT | Dominating function \|h\| (finite first moment). With dominating function 1 it also gives μ(D_{Q_k} △ D_Q) → 0. |
| T2c | Q ⊇ K' or all Q? | Q ⊇ K' | D_Q is a model (D_Q ⊆ U a.e.) iff K' ⊆ Q. Traces D_Q ∩ U of other credal sets are again of this form. |
| T2d | D_Q identified a.e. with the model | CORRECT | Q ↦ [D_Q] is a bijection onto the coherent models, and a homeomorphism (Hausdorff ↔ μ(·△·)). |
| T3 | Hull-overlap Φ_X(Q) := μ((D_Q∖X) ∩ hull(X∖D_Q)) | **Lower semicontinuous (PROVED); not upper semicontinuous (PROVED + CHECKED)** | Usc fails even inside the compact 𝒦_δ(X), with X incoherent and X ⊇ int ℝⁿ₊. There are explicit examples in two worlds (exact rationals) and three worlds (exact). The auditor's warning is correct and can be stated sharply: witnessing is an **open** condition on defenders, but not a **closed** one. |

## 1. Conventions

- (M): μ is a finite Borel measure with the same null sets as Lebesgue measure, and ∫|h| dμ < ∞. This is the paper's (M); "positive density" in ES64 is a special case.
- K' ⊆ relint Δ is nonempty, compact and convex, and U := D_{K'}.
- Credal sets are nonempty, closed and convex.
- D_S := {h : q·h > 0 ∀q ∈ S}, C_S := {h : q·h ≥ 0 ∀q ∈ S}, and P_S(h) := min_{q∈S} q·h.
- For measurable B: Q_B := {q ∈ Δ : q·h ≥ 0 for μ-a.e. h ∈ B}, and hull(B) := D_{Q_B}.
- E_d denotes the set of **Lebesgue** density-one points of E. It is unchanged when E is altered on a null set, and |E ∖ E_d| = 0 (Lebesgue density theorem).
- Under (M), μ(E ∩ V) > 0 for every ball V around a point of E_d.
- Every object in T1 (A_d, B_d, Q_B, hull(B), μ(A ∩ hull B)) is therefore invariant under null modifications of A and B. This settles the a.e. conventions.
- One could use μ-density points instead (Besicovitch differentiation). All statements below remain true, since they use only "μ(E ∩ V) > 0 for balls V around the point" and "a.e. point of E is a density point".

## 2. Tool 1: the density-point witness

**Claim 0 (PROVED).** If q ∈ Q_B and b ∈ B_d, then q·b ≥ 0.

*Proof.* Suppose q·b < 0. The open half-space {q·h < 0} contains a ball V around b. Since b ∈ B_d, |B ∩ V| > 0, so μ(B ∩ V) > 0 by (M). So q·h < 0 on a μ-non-null part of B, contradicting q ∈ Q_B. ∎

Conversely, if q ∈ Δ and q·b ≥ 0 on B_d, then q ∈ Q_B, because a.e. point of B lies in B_d. Hence
  **Q_B = {q ∈ Δ : q·b ≥ 0 for all b ∈ B_d}.**  (2.1)

**Lemma W1 (hull formula; PROVED).** For every measurable B ⊆ ℝⁿ,
  hull(B) = cone(B_d) + int ℝⁿ₊.
Here cone(·) is the set of finite non-negative combinations, with cone(∅) = {0}.

*Proof.* Write E := cone(B_d) + int ℝⁿ₊. E is convex, and open as a union of translates of an open set.

- (⊇) Let a = Σ_j λ_j b_j + p, with b_j ∈ B_d, λ_j ≥ 0 and p ≫ 0. For q ∈ Q_B, Claim 0 gives q·a ≥ q·p ≥ min_i p_i =: η > 0, since q ∈ Δ. This bound is uniform in q, so a ∈ D_{Q_B}. If Q_B = ∅, then D_∅ = ℝⁿ and there is nothing to prove.
- (⊆) Let a ∉ E. Separate the point a from the nonempty open convex set E: there is q ≠ 0 with q·a ≤ q·e for all e ∈ E.
  - q ≥ 0: if q_i < 0, then e = 𝟙 + s e_i ∈ E gives q·e → −∞ as s → ∞.
  - For b ∈ B_d and s, τ > 0, sb + τ𝟙 ∈ E. Letting τ → 0 gives q·a ≤ s q·b for every s > 0, so q·b ≥ 0. Taking s → 0 as well gives q·a ≤ 0.
  - Put q̂ := q/(𝟙·q) ∈ Δ. By (2.1), q̂ ∈ Q_B, and q̂·a ≤ 0. So a ∉ D_{Q_B}. ∎

*Remarks.*
1. W1 contains the auditor's "hull(B) = int C with C = cl cone(B_d ∪ ℝⁿ₊)". Both sides equal E (int C ⊆ D_{Q_B} by bipolarity and (2.1), and E ⊆ int C trivially). W1 shows that no closure is needed, so the question of B_d not being closed does not arise.
2. B_d may be replaced by any subset dense in B_d, e.g. B ∩ B_d, because the condition a − Σλ_j b_j ≫ 0 is open in (b_1, …, b_r) for fixed λ. Each b ∈ B_d is a limit of points of B ∩ B_d: every ball around b meets B in positive measure, and |B∖B_d| = 0.

**Corollary W1′ (the witness, both directions; PROVED).** Let A, B ⊆ ℝⁿ be measurable. The following are equivalent:
- (i) μ(A ∩ hull(B)) > 0;
- (ii) A_d ∩ hull(B) ≠ ∅;
- (iii) there are a ∈ A_d, b_1, …, b_r ∈ B_d and λ_j ≥ 0 with a − Σ_j λ_j b_j ∈ int ℝⁿ₊.

In (iii), r ≤ n can always be arranged. If Q_B ∩ relint Δ ≠ ∅, which holds whenever B ⊆ U, then r ≤ n−1 can be arranged (Lemma W2). The points can be taken with a ∈ A ∩ A_d and b_j ∈ B ∩ B_d.

*Proof.*
- (i)⇒(ii): a.e. point of A ∩ hull(B) lies in A_d.
- (ii)⇒(i): hull(B) is open, because Q_B is compact and P_{Q_B} is continuous. A ball V around a ∈ A_d ∩ hull(B) lies in hull(B), and |A ∩ V| > 0.
- (ii)⟺(iii): this is W1.
- r ≤ n: reduce Σλ_j b_j to linearly independent b_j by the standard kernel step (Carathéodory), which leaves the sum unchanged.
- r ≤ n−1: Lemma W2.
- The choice of a and b_j: Remark 2 above, and the same density argument for a. ∎

The auditor's proof of necessity (choose η with a − 2η𝟙 ∈ C, approximate within η by c ∈ cone(B_d ∪ ℝⁿ₊), apply Carathéodory, absorb the ℝⁿ₊ generators) is also correct:
- write c = Σλ_j b_j + p with p ∈ ℝⁿ₊;
- then a − Σλ_j b_j = (a − c) + p ≥ a − c ≥ η𝟙 ≫ 0.

Absorbing p can only increase the residual, so strict positivity is kept. The sufficiency proof is also correct, and so is the uniformity of η (T1b). The auditor's count "at most n" is correct, but not sharp.

**Lemma W2 (n−1 removed points suffice; PROVED).** Let F ⊆ ℝⁿ be such that −e_i ∉ cone(F) for every i. If a ∈ cone(F) + int ℝⁿ₊, then a ∈ cone(F′) + int ℝⁿ₊ for some F′ ⊆ F with |F′| ≤ n−1.

The hypothesis holds for F = B_d whenever some q ∈ Q_B has full support, since then q·b ≥ 0 on cone(B_d) while q·(−e_i) < 0. In particular it holds for every B ⊆ U, because ∅ ≠ K' ⊆ Q_B and K' ⊆ relint Δ.

*Proof.*
- Let r be the least size of an F′ ⊆ F that works, and suppose r ≥ n. Take F′ = {b_1, …, b_r} with a − Σλ_j b_j ≫ 0.
- Minimality forces every λ_j > 0.
- Minimality also forces b_1, …, b_r to be linearly independent. Otherwise the kernel step removes one generator without changing Σλ_j b_j.
- So r = n, and M := [b_1 ⋯ b_n] is invertible.
- Put S := {ν ∈ ℝⁿ : Mν ≪ a}. Then S = ν₀ + D, with ν₀ := M⁻¹a and D := M⁻¹(−int ℝⁿ₊), an open convex cone. S ∩ ℝⁿ₊ ∋ λ.
- By minimality, S contains no point of ∂ℝⁿ₊: a point of S with ν ≥ 0 and some ν_j = 0 would use n−1 generators.
- S is convex, hence connected. It meets int ℝⁿ₊ and misses ∂ℝⁿ₊, so S ⊆ int ℝⁿ₊.
- For d ∈ D and τ > 0, ν₀ + τd ∈ S, so ν₀/τ + d ≫ 0. Letting τ → ∞ gives d ≥ 0. So D ⊆ ℝⁿ₊, and by continuity M⁻¹(−ℝⁿ₊) ⊆ ℝⁿ₊.
- Then ν := M⁻¹(−e_i) ≥ 0 and −e_i = Mν ∈ cone(F′) ⊆ cone(F). This is a contradiction. ∎

**Sharpness (PROVED; CHECKED in `generator_count.py`, part ii).** Fix n ≥ 2 and any K'. Put q_min := min{q_i : q ∈ K', i ≤ n} > 0, and take L > 1/q_min, s, ε > 0 with (n−2)s + 2ε < 1, and ρ < min(s, ε/2).

- For j = 1, …, n−1, put b_j := L e_n − e_j + s Σ_{k∉{j,n}} e_k.
- Put a := Σ_j b_j + ε𝟙, A := ball(a, ρ), and B := ∪_j ball(b_j, ρ).

Then:
- q·b_j ≥ L q_n − q_j > 0 on K', and q·a > 0 on K', so for small ρ, A, B ⊆ U.
- A and B are disjoint.
- a − Σ_j b_j = ε𝟙, so μ(A ∩ hull B) > 0.

But for i < n:
- every a′ ∈ A has a′_i ≤ −1 + (n−2)s + ε + ρ < 0;
- every point of ball(b_k, ρ) with k ≠ i has i-th coordinate > 0.

So any witness must use a point of each of the n−1 balls. Hence n−1 is attained. In three worlds, two removed points are needed in general and always suffice.

**Control (CHECKED, part iii).** Without the hypothesis of W2, n can be needed: take F = {−e_1, …, −e_n} and a = −½𝟙. This cannot occur for B ⊆ U.

**Random stress test (CHECKED, part i).** There were 1400 random adversarial instances with n = 2…5. In each, F consists of n generators in C_{K'} near ∂C_{K'}, and a = Σλb + small slack. In every instance a representation with ≤ n−1 generators was found and verified in exact rationals; none needed n. Only positive LP answers are used, each re-verified exactly.

**Remark (section form of ES64 Lemma 5.3).** The test "a ∈ int conv{b̃_1, …, b̃_r, ẽ_1, …, ẽ_n}" in a section {k̄·h = 1} is equivalent to (iii), but only when k̄·b_j > 0 and k̄·a > 0. This holds for k̄ ∈ relint K' with K' full-dimensional (paper, Lemma fulldim(c)). The section Σh = 1 used by ES64's scripts needs 𝟙/n ∈ K', or a direct check that Σb_j > 0. The conic form (iii) has no such proviso, and it is the one to use in proofs.

## 3. Tool 2: compactness

**Lemma C1 (the parameter space; PROVED).** Let 𝒦(K') := {Q credal : K' ⊆ Q}, with the Hausdorff metric d_H.

- (a) 𝒦(K') is compact.
  - The nonempty compact subsets of the compact metric space Δ form a compact space (Blaschke / Hausdorff).
  - Convexity is preserved under d_H-limits. Given x, y ∈ Q, pick x_k, y_k ∈ Q_k with x_k → x and y_k → y. Then (1−t)x_k + t y_k ∈ Q_k, and its distance to Q tends to 0.
  - K' ⊆ Q_k for all k implies K' ⊆ Q, since d(x, Q) ≤ d_H(Q_k, Q) for x ∈ K'.
- (b) Q ↦ [D_Q] is a bijection of 𝒦(K') onto the coherent models on U (classes mod null sets).
  - A coherent model is D_Q a.e. for a unique credal Q (paper, Lemma open).
  - D_Q ⊆ U a.e. ⟺ D_Q ⊆ D_{K'} (Lemma open, with O = D_Q) ⟺ K' ⊆ Q (Lemma D(c)).
  - So the defenders **must** range over Q ⊇ K'. A D_Q with Q ⊉ K' is not a model.
- (c) Nothing is lost by this restriction. For every credal Q, D_Q ∩ U = D_{Q∪K'} = D_{conv(Q∪K')} by Lemma D(a), and conv(Q∪K') ∈ 𝒦(K').

**Lemma C2 (continuity; PROVED).**
- (a) |P_Q(h) − P_{Q′}(h)| ≤ d_H(Q, Q′)·|h|.
  - Given q ∈ Q, pick q′ ∈ Q′ with |q − q′| ≤ d_H. Then P_{Q′}(h) ≤ q′·h ≤ q·h + d_H|h|. Minimise over q and use symmetry.
  - So P_{Q_k} → P_Q uniformly on bounded sets.
- (b) Z_Q := {P_Q = 0} = ∂D_Q is μ-null.
  - Since q·𝟙 = 1 on Δ, P_Q(y + t𝟙) = P_Q(y) + t.
  - In the coordinates h = y + t𝟙 with y ∈ 𝟙^⊥ (a linear isomorphism), Z_Q = {(y, −P_Q(y))} is the graph of a continuous function. Each fibre is one point, so Z_Q is Lebesgue-null by Fubini, and μ-null by (M).
- (c) If Q_k → Q in 𝒦(K'), then 1_{D_{Q_k}} → 1_{D_Q} pointwise off Z_Q, by (a). Dominated convergence, with dominating functions |h| (finite first moment) and 1 (μ finite), gives:
  - m(D_{Q_k}) → m(D_Q);
  - μ(D_{Q_k} △ D_Q) → 0.

  Quantitatively, |m(D_Q) − m(D_{Q′})| ≤ ∫_{\{|P_Q(h)| ≤ d_H(Q,Q′)|h|\}} |h| dμ.
- (d) The map Q ↦ [D_Q] is continuous and injective from the compact space (𝒦(K'), d_H) into (models, μ(·△·)). It is therefore a homeomorphism onto its image, so "compact" means the same in both topologies.

**Corollary C3 (PROVED).** For a model X and δ ≥ 0, put 𝒦_δ(X) := {Q ∈ 𝒦(K') : m(D_Q) − m(X) ≥ δ𝟙}. It is compact, being the preimage of a closed set under a continuous map on a compact space.

If X is incoherent, then it is not a.e. a Bayes act, because N_π = U ∩ {π·h > 0} = D_{conv(K'∪{π})} is coherent. ES64 Lemma 5.1 then gives π with m(N_π) − m(X) ≫ 0. So 𝒦_δ(X) ≠ ∅ for δ := min_i (m(N_π) − m(X))_i > 0.

*Caveat.* The set of eligible defenders in (H) is 𝒮(X) := {Q : m(D_Q) ≥ m(X), m(D_Q) ≠ m(X)}. It is a compact set minus a closed set, so it is not compact in general. It is also larger than ∪_{δ>0} 𝒦_δ(X): it includes defenders that tie X in some coordinate. A proof or refutation of (H) that works only in ∪_{δ>0} 𝒦_δ(X) does not cover these.

## 4. The hull-overlap functional: what holds and what fails

For a model X and Q ∈ 𝒦(K'), put Φ_X(Q) := μ((D_Q∖X) ∩ hull(X∖D_Q)). Then (H) for X says: Φ_X > 0 somewhere on 𝒮(X).

**Prop C4 (Φ_X is lower semicontinuous; PROVED).** Let Q_k → Q. Put A := D_Q∖X, B := X∖D_Q, H := hull(B), and define A_k, B_k, H_k in the same way.

1. *H ⊆ liminf H_k pointwise.*
   - Let a ∈ H. By W1′, a − Σλ_j b_j ≫ 0 with b_j ∈ B_d.
   - Put T := {b ∈ B_d : P_Q(b) < 0}. T is dense in B_d: B ⊆ {P_Q ≤ 0}, and a.e. point of B is in B_d ∖ Z_Q.
   - By openness, we may take every b_j ∈ T.
   - For b ∈ T, choose a ball V ∋ b with P_Q ≤ −c < 0 on V. By C2(a), P_{Q_k} < 0 on V for large k. Then V ∩ D_{Q_k} = ∅ = V ∩ D_Q, so V ∩ B_k = V ∩ X = V ∩ B. Hence b ∈ (B_k)_d.
   - So for large k, all b_j lie in (B_k)_d, and a ∈ H_k by W1.
2. μ(A △ A_k) ≤ μ(D_Q △ D_{Q_k}) → 0, by C2(c).
3. By Fatou and step 1, liminf μ(A ∩ H_k) ≥ μ(A ∩ H). So liminf Φ_X(Q_k) ≥ liminf μ(A ∩ H_k) − lim μ(A∖A_k) ≥ Φ_X(Q). ∎

**Consequences (PROVED).**
- (a) {Q : Φ_X(Q) > 0} is open in 𝒦(K'). With C2, W^≫(X) := {Q : m(D_Q) − m(X) ≫ 0, Φ_X(Q) > 0} is open. A witnessing defender with a strict margin in every coordinate is robust: every nearby defender also witnesses.
- (b) Polytope defenders suffice whenever W^≫(X) ≠ ∅.
  - Polytopes are dense in 𝒦(K'). Outer-approximate Q by a finite intersection P₀ of half-spaces with Q ⊆ P₀ ⊆ Q + εB, and put P := P₀ ∩ Δ ⊇ K'.
  - This does not cover witnesses in 𝒮(X) that tie X in some coordinate.
- (c) Φ_X attains its infimum on each compact 𝒦_δ(X). It need not attain its supremum (see below). Maximising Φ_X needs a separate argument, as the auditor says.

**Failure of upper semicontinuity: precise statement.** There exist an incoherent X ⊇ int ℝⁿ₊ (so Prop 5.4 does not apply), δ > 0, and Q_k → Q, all in 𝒦_δ(X), with Φ_X(Q_k) ≥ c > 0 for all k but Φ_X(Q) = 0.

The mechanism: X∖D_{Q_k} is a sliver of measure → 0 along ∂D_Q. Its hull does not shrink with it. Hull is not continuous in the removed set, only lsc in the defender (Prop C4).

**Example C5 (two worlds; PROVED, every number CHECKED exactly in `hull_jump_2d.py`).** Take μ with density e^{−|h|₁}. Write credal sets as intervals of p = q_1.

- *Data.*
  - K' = [1/4, 3/4], so U = int cone((3,−1), (−1,3)).
  - Q = [1/8, 7/8], so D_Q = int cone((7,−1), (−1,7)).
  - G₋ := int cone((1,0), (14,−1)) and G₊ := int cone((0,1), (−1,14)).
  - X := D_Q ∖ cl(G₋ ∪ G₊).
- *X is admissible as a rival.*
  - X ⊆ U and X ⊇ int ℝ²₊.
  - X is incoherent: each g ∈ G₋ is a midpoint of two points of X, so any convex cone containing X a.e. contains the non-null G₋, which X misses.
- *Moments.* m(G₋) = (29/225, −1/225), m(G₊) = (−1/225, 29/225), and m(D_Q) − m(X) = (28/225)(1,1).
- *At the limit.* Φ_X(Q) = 0: X ⊆ D_Q, so B = ∅ and hull(B) = int ℝ²₊, which misses G₋ ∪ G₊.
- *Along the sequence.* Q_ε := [1/8 − ε, 7/8] ⊇ K' for 0 < ε ≤ 1/32, with d_H(Q_ε, Q) = ε√2 → 0.
  - B_ε = X∖D_{Q_ε} = int cone((7+8ε, −1+8ε), (7,−1)), with μ(B_ε) = ε → 0.
  - Q_{B_ε} = [1/8, 1], so hull(B_ε) = int cone((7,−1), (0,1)). This set is independent of ε, and contains G₋.
  - A_ε = G₋ ∪ G₊.
  - So **Φ_X(Q_ε) = μ(G₋) = 1/15 for every ε ∈ (0, 1/32]**, while Φ_X(Q) = 0.
  - The margins are m(D_{Q_ε}) − m(X) = (28/225 − ε(14+8ε)/8, 28/225 + ε(2−8ε)/8) ≥ (1/20)𝟙 for ε ≤ 1/32. So all Q_ε and Q lie in 𝒦_{1/20}(X).

**Example C6 (three worlds; PROVED, CHECKED exactly in `hull_jump_3d.py`).** Take any permutation-symmetric μ satisfying (M); the script uses e^{−|h|₁}.

- *Data.*
  - Q = conv{v₁, v₂, v₃}, with v₁ = (3/5, 1/5, 1/5) and permutations, and any K' ⊆ Q in relint Δ (e.g. K' = {𝟙/3}).
  - G₁ := int cone((−1,3,3), (−1,6,3), (−1,3,6)). G₂ and G₃ are its images under the transpositions (12) and (13). G := G₁ ∪ G₂ ∪ G₃.
  - X := D_Q ∖ cl G.
- *Facts.*
  - cl G∖0 ⊆ D_Q, since every v_i·generator > 0.
  - X ⊇ int ℝ³₊, since G_j ⊆ {h_j < 0}.
  - X is incoherent. Each g ∈ G₁ lies on a segment in direction e₁ between a point of int ℝ³₊ and a point of D_Q with h₁ ∈ (−(g₂+g₃)/3, −min(g₂,g₃)/3), and both lie in X. Here cl G₁ ⊆ {−3h₁ ≤ min(h₂,h₃)}.
  - By symmetry, m(G) = c𝟙 with c = ∫_{G₁} 𝟙·h dμ > 0. Exactly, c = 729/24500.
  - Φ_X(Q) = 0, as in C5.
- *Along the sequence.* Put Q_ε := conv(Q ∪ {v₁ + εd}) with d = (1, −½, −½), so d_H(Q_ε, Q) → 0 and D_{Q_ε} = D_Q ∩ {q_ε·h > 0}.
  - For ε < 3/20, q_ε > 0 on the generators of G₁. The same holds for G₂ and G₃ (checked), so A_ε = G and B_ε = D_Q ∩ {q_ε·h ≤ 0}.
  - b_ε := (−2,3,3) + ε𝟙 lies in the open set D_Q ∩ {q_ε·h < 0} ∖ cl G, so it is a density point of B_ε.
  - Each generator g of G₁ satisfies g − ¾ b_ε ≫ 0 for ε < 2/3, so cl G₁∖0 ⊆ cone(b_ε) + int ℝ³₊ ⊆ hull(B_ε) by W1.
  - Hence **Φ_X(Q_ε) ≥ μ(G₁) = 9/700** for all ε < 3/20, while Φ_X(Q) = 0.
  - The margin m(D_{Q_ε}) − m(X) = m(G) − m(B_ε) → c𝟙 by C2. It is ≥ (c/4)𝟙 exactly at ε = 1/100, 1/200, 1/400, 1/1000 and 10⁻⁶, and for all small ε by continuity.

Both examples have Φ jumping **down** at the limit, which is the direction lsc allows. By Prop C4 the opposite jump (Φ_X(Q_k) → 0 while Φ_X(Q) > 0) is impossible.

## 5. What H65 and X65 may use

- **W1 / W1′ / W2 (PROVED).** For B ⊆ U:
  - hull(B) = cone(B_d) + int ℝⁿ₊ = ∪_{|F|≤n−1, F⊆B∩B_d} (cone F + int ℝⁿ₊);
  - (H) for X ⟺ some Q ∈ 𝒮(X) and a ∈ (D_Q∖X)_d have a − Σ_{j≤n−1} λ_j b_j ≫ 0 with b_j ∈ (X∖D_Q)_d. In three worlds, two removed points suffice.
- **C1–C3 (PROVED).** Compactness of 𝒦_δ(X), continuity of moments and of μ(·△·), and the restriction to Q ⊇ K' is without loss.
- **C4 (PROVED).** Witnessing is an open condition on defenders. Strict all-coordinate witnesses are stable under perturbation, and can be taken polyhedral.
- **C5/C6 (PROVED).** Witnessing is not closed, even inside 𝒦_δ(X). A counterexample cannot be obtained by taking a limit of near-witnesses. A proof cannot pick a maximiser of Φ_X by compactness alone. A limit argument on defenders does not transfer witnessing to the limit.
- **Open, flagged.** Whether a witness in 𝒮(X) that ties X in some coordinate can always be replaced by one with a strict margin in every coordinate. If so, (H) reduces to W^≫(X) ≠ ∅, which is an open condition.

## 6. Files (`wt65py/`)

- `generator_count.py` / `.out`: the random stress test of W2 (exact verification), the sharpness family for n = 2…6, and the control without one-sidedness.
- `hull_jump_2d.py` / `.out`: Example C5, exact rationals.
- `hull_jump_3d.py` / `.out`: Example C6, exact. It uses `../es64py/cones.py` for the exact cone moments.
