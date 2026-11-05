# REF85: referee report on R85c, "the countable-selection construction without the integral score"

Referee REF85, 29 Oct 2026.

**Inputs read in full:**
- R85c_report.md, which is under review;
- BRIEF85, BRIEF85_REF, AUDIT_countable, AUDIT_obstruction83 and AUDIT_handoff;
- R85b_report;
- the relevant parts of app_long.tex: `def:hull`, `lem:states`, `lem:DQ`, `lem:identify`, `lem:hull`, `lem:guidedeverywhere`, `lem:contraction`, `lem:trim` and §repair;
- the relevant parts of appshort.tex: `lem:states`(b) and `lem:measurefacts`(c);
- ../r84/C1_report (Theorems 2–3) and ../r84/C2_report (Theorem 1.1, Proposition 1.4).

I re-derived every step below myself and did not take R85c's labels on trust. My scripts are in `r85/ref85/`, with their outputs saved as `out_*.txt`. They use only the box field ψ (or the Prop 12 field) and μ-masses. The payoff integral and the Brier score appear in none of them. The numerics are for exploration only: no verdict below rests on them, except where I say "exact LP".

**Labels**
- **ERROR**: a false statement or invalid step.
- **GAP**: a claim that is not proved as stated, though it may be true.
- **MINOR**: a wording, scope or presentation issue, or a sharpening.
- **OK**: checked and correct.

---

## 0. Summary

**I found no ERROR.** The mathematics that carries R85c's main claims is correct:
- Proposition 2;
- Theorem 3, both directions;
- Lemma 1 and Corollaries 4, 5 and 7;
- Proposition 6;
- Lemmas 8a and 8b, Theorem 8 and Corollary 9;
- Proposition 12 and Proposition 14;
- the reduction of Claim 9 to C1 Theorem 3, which I refereed and which is also correct.

Theorem 10, the infinite-world version, is written as a list of modifications. Each modification checks out, so it is a proof up to routine write-up (§6).

**Compliance with the author's rule: OK.**
- No ordinary payoff integral or Brier score is used as a ranking, a constraint or a proof device.
- R85c correctly removes the audit's buffer f_X(q) = ∫_X q(g)⁻dμ, which is an integral of gamble values. In its place R85c uses the violated mass F_Z(q) = μ(Z ∩ {q·g < 0}).
- `lem:trim`, `lem:contraction` and `lem:hull` contain no integrals of gambles.
- The scripts in c3py/ use ψ only. I checked them.
- One caution (MINOR-7): the general Theorem 11 class contains the payoff field ψ_ω = g_ω as a degenerate member. Any statement of "the class of box hull rankings" must therefore require l_ω < u_ω.

**Findings that need action:**

| # | Label | Location | Issue |
|---|---|---|---|
| G1 | GAP | §7, last bullet | "A coherence-free gate built from ψ alone would protect at most the Bayes family" is asserted without proof. |
| G2 | GAP | Thm 11 / brief item 6 | The transfer to general fields is proved only for finite Ω. No infinite-world transfer is stated or proved. |
| G3 | GAP | Thm 10 | This is a sketch. Three routine steps should be written out. |
| M1 | MINOR | Thm 3(ii), Cor 4, Thm 11 | The atomless hypothesis is unnecessary under (M2). |
| M2 | MINOR | Thm 11 | "By C2 Prop 1.4, (F) and (C) hold *exactly* when the complete ψ-ranking satisfies W" overstates C2. |
| M3 | MINOR | §6 bullet; Cor 5.1 | "By C1 Thm 2–3 only Bayes sets survive" holds for n = 2 only. For n ≥ 3 it is C1's conjecture R8. Likewise C2 Thm 4.2 is an n ≥ 3 result. |
| M4 | MINOR | §4 | The audit's §7 *inference* fails, as R85c says. In two worlds its *conclusion* nevertheless holds. |
| M5 | MINOR | Rem 13 | Lexicographic layers leave the protected class *unchanged*, not merely no larger. |
| M6 | MINOR | Thm 8 | The neighbourhood radii are tiny (10⁻⁶–10⁻⁸). This should be stated, as R85b did for the integral version. |
| M7 | MINOR | Cor 7 / Thm 11 | Two points of scope: (i) thin targets need nearly degenerate boxes; (ii) the payoff field is excluded only by requiring l < u. |
| M8 | MINOR | wording | "Upward closure" is ambiguous. Item 2d omits the vertex models. |

---

## 1. Proposition 2: structure of the ψ-hull ranking — OK

- **Independence (arbitrary-set form).** The verdict depends only on (A, B) = (Y∖X, X∖Y) modulo null sets.
  - The score difference is ∫_Aψ_ω − ∫_Bψ_ω.
  - Guidance and the hull clause depend only on (A, B).
  - Equality a.e. is preserved under common-context replacement, as in R85b §1.1.
- **World-by-world guidance.** Let a change be non-null and guided at ω. Then ψ_ω > 0 a.e. on A ⊆ {g_ω > 0} and ψ_ω < 0 a.e. on B ⊆ {g_ω < 0}, by sign-respect. So s_ω rises strictly and the comparison is accepted by the guidance clause. The reverse comparison would need s_ω to fall, so it is refused, and the preference is strict.
- **Ordering conditions.** Every accepted non-identity comparison strictly raises s_ω. This gives:
  - no ties between distinct models, hence transitivity through ties;
  - the three-model condition: a ⪰ b ⪰ c with c ≻ a would force s(c) > s(a) ≥ s(c).
- **Reflexivity** holds by the first clause.

Consolidation is not checked by R85c. The handoff does not require it.

## 2. Theorem 3: protection is exactly "C ⊆ B_r a.e. for some r" — OK (M1, M8)

**(i), the "if" direction.**
- Let Y dominate C. Then Y ≠ C, and every world strictly raises s_ω.
- The hull clause does not depend on ω, so the two cases are exhaustive.
- *Case A ⊆ H(B).*
  - B ⊆ C = D_Q gives H(B) ⊆ D_Q by `lem:hull`(c). This covers B null too, since H(∅) = D_S ⊆ D_Q.
  - So A ⊆ C, and since A ∩ C = ∅, A is null. Then s(B) ≪ 0 and B is non-null.
  - But r·ψ > 0 on B ⊆ B_r, so r·s(B) > 0. This contradicts r ≥ 0, r ≠ 0. OK.
- *Case A ⊄ H(B).* Every world must accept by guidance. Then `lem:guidedeverywhere` makes A and B null. OK.
- Hypothesis (C) is indeed not used.

**(ii), the "only if" direction.**
- *Lyapunov step.* R_C = {s(B) : B ⊆ C} is the range of a finite-dimensional non-atomic vector measure, so it is compact and convex.
- *Separation step.* If R_C misses the open orthant −ℝⁿ₊₊, a disjoint convex set and open convex set can be separated: there is λ ≠ 0 with λ·z ≥ λ·w for all z ∈ R_C and all w in the orthant.
  - Sending w = −te_i with t → ∞ gives λ ≥ 0.
  - Taking w → 0 and z = 0 gives c = 0.
  - Hence ∫_B λ·ψ ≥ 0 for every B ⊆ C, so λ·ψ ≥ 0 a.e. on C.
  - With N_r null for r = λ/Σλ, this gives C ⊆ B_r a.e., the excluded case. OK.
- *The pure removal.* C → C∖B adds nothing (A = ∅), so it is accepted at every world, and its reverse is refused. OK.

**M1 (the atomless hypothesis can be dropped).** Under (M2), atoms lie in D_S° ∪ (−D_S°) (appshort `lem:measurefacts`(c)). A coherent C = D_Q contains every positive atom and no negative atom. On a positive atom, λ·ψ > 0 for every λ ≥ 0 with λ ≠ 0.
- **Fix:** apply Lyapunov to the diffuse part μ_c restricted to C∖A_μ. The separation then gives λ·ψ ≥ 0 μ_c-a.e. on C, and the atoms in C satisfy it strictly. So (ii), the "only if" half of Cor 4, Prop 6 and the "exactly" of Thm 11 all hold under (M1)–(M3) without atomlessness.

**M8 (terminology).** "C ⊆ B_r" makes C a *sub-model* of a Bayes set, that is, a credal set *containing* K_r. "Upward closure" is right in credal sets but wrong in models.
- **Fix:** say "the coherent sub-models of ψ-Bayes sets (credal sets containing some K_r)".

**Exact check, n = 3** (`n3_exact.py`, exact LP). On each closed orthant ψ is linear. So "r·ψ ≥ 0 on cl D_Q" is an LP in r over the extreme rays of the pieces cl D_Q ∩ orthant. I used this test, which is independent of R85c's K_r ⊆ Q criterion, in §3.

## 3. Lemma 1; Corollaries 4, 5 and 7 — OK

- **Lemma 1.** The identity p·ψ(g) = min_{v∈Bx}(p·v)(k_v·g) holds coordinatewise. Since p·v > 0, sign(p·ψ) = sign(P_{K_p}). This also holds at boundary p, where K_p ⊆ Δ_{supp p}.
  - Monte Carlo check: 0 sign disagreements over 20 random full boxes × 2·10⁵ gambles.
- **Corollary 4.** The "if" direction is Thm 3(i).
  - For the converse: strictly separate k ∈ K_r∖Q and shift by 𝟙 to obtain g with k·g < 0 < P_Q(g).
  - Continuity of P_Q and P_{K_r} gives a ball in D_Q∖D_{K_r}, which has positive measure under full support. OK.
- **Corollary 5.2 (the audit's T).** I re-derived K_r = [r/(r+ρ(1−r)), ρr/(ρr+1−r)] ⊆ [¼, ¾] ⇔ ρ/(3+ρ) ≤ r ≤ 3/(3+ρ). Such an r exists iff ρ ≤ 3, and at ρ = 3 only r = ½ works. OK.
  - Exact cross-check (`n2_protection.py`): an LP over 4000 angular cells searches for a fractional pure removal of T. It finds none for ρ ∈ {1.5, 2, 2.9, 3}.
  - It finds a strictly improving removal for ρ = 3.1 (gain 3.1·10⁻⁵) and for ρ = 4 (2.4·10⁻³).
  - The same LP agrees with the K_r ⊆ Q criterion on all 36 test cases (narrow, precise interior, vertex, vacuous, and touching a vertex).
- **Corollary 5.3 (T1).** The worst coordinate of K_r is r_i/(r_i + ρ(1−r_i)). Summing the constraints gives ρ ≤ (1−a)/(2a), with r = u when that holds. OK.
  - The extreme-ray LP threshold is ρ* = 4.500000, 2.000000 and 1.166667 for a = 0.1, 0.2 and 0.3, matching (1−a)/(2a).
  - The K_r-in-M LP slack changes sign at exactly the same ρ.
  - At a = 0.2 and ρ = 2, the protecting prior is r = (⅓, ⅓, ⅓).
- **Corollary 7 (coverage).**
  - "If": for the vertex case, K_{e_i} = {e_i}. For the face case, the box [1, 1+κ]ⁿ gives |k_ω − r_ω| ≤ κ r_ω.
  - "Only if": for |supp r| ≥ 2, K_r contains the image of an open box under a diagonal homeomorphism followed by normalisation. Normalisation ℝ^F₊₊ → relint Δ_F is an open map, so K_r has nonempty relative interior. OK.
  - The characterisation in the brief ("Q contains a vertex, or Q ∩ Δ_F has nonempty interior relative to aff Δ_F for some face with |F| ≥ 2") is correct.
  - **Exact n = 3 check** (`n3_exact.py`). For each of the following, I took the best of four small symmetric boxes and 300 random full boxes. All ten verdicts match Cor 7:
    - interior triangle: covered;
    - generic interior segment: not covered;
    - segment pointing at a vertex (on q₁ = q₂, not containing e₃): not covered;
    - segment on an edge: covered;
    - segment from a vertex inward: covered;
    - precise interior point: not covered;
    - precise point on an edge: not covered;
    - vertex point: covered;
    - segment from an edge point to the interior: not covered;
    - vacuous model: covered.
  - In the uncovered cases the best LP value is about −2·10⁻⁴. It tends to 0⁻ only as κ → 0, that is, only in the limit of the excluded payoff field (see M7).

**M7 (scope).**
- (i) The protecting box for a target whose relative interior has radius η needs u/l − 1 ≲ η. So thin targets are reached only by nearly degenerate boxes.
- (ii) Theorem 11's class contains ψ = g, whose hull ranking protects every coherent model.
- **Fix:** define the box class with l_ω < u_ω for every ω, and say explicitly that its closure contains the payoff field, which is excluded.

**M8 (wording).** Item 2d of the summary table says "in two worlds this is every non-precise interval". The vertex models D_{e_i} are also covered (§3 of R85c says so).
- **Fix:** say "all coherent models except the precise interior ones".

## 4. Proposition 6 — OK, with a sharpening

The proof is correct.
- Under continuity and full support, protection gives r·ψ ≥ 0 on the closure of the open set {P_Q > 0}.
- That closure contains ±h when Q ⊆ h^⊥.
- Strict commission-aversion then gives a contradiction.

The construction of h with no zero coordinate for a non-vertex precise p is also right: only one value of t fails.

**Sharpening (useful for R85c's open item O1).** For a precise interior p, the same argument shows something stronger. Any continuous field (not necessarily commission-averse) whose hull ranking protects D_p must have r·ψ(h) ≥ 0 and r·ψ(−h) ≥ 0 on the **whole hyperplane** p^⊥. Under weak commission-aversion this forces r·ψ ≡ 0 on p^⊥.
- In two worlds p^⊥ is a single pair of rays, which is exactly what Prop 12 achieves.
- For n ≥ 3 an analogue must make the r-aggregate field commission-neutral on an (n−1)-dimensional subspace, not just on one pair of rays.
- This is a necessary condition, and the n ≥ 3 search should start from it.

## 5. The selection argument (Theorem 8, Corollary 9, Lemmas 8a and 8b) — OK (M4, M6)

Each step was checked against the cited lemmas.

- **The gap γ > 0 (Lemma 8a).**
  - X ⊆ G a.e. by `lem:hull`(b) and (M2).
  - For each p, the maximisers of Z ↦ ∫_Z p·ψ over Z ⊆ G are G ∩ B_p up to the null set N_p.
  - G ∩ B_p = D_{conv(Q∪K_p)} is coherent, so the bracket is positive for every p.
  - The bracket is continuous in p: (p·ψ)⁺ is continuous in p for every g, and dominated by ‖ψ‖.
  - Δ is compact. OK.
  - Uniqueness of the Bayes act comes from null ties, not from strict propriety. This answers R85b's worry.
- **The inconsistent case (Lemma 8b).**
  - h is concave and continuous. It is negative everywhere, because h(q) = 0 would give X ⊆ B_q = D_{K_q} a.e., which is consistent.
  - The right derivative toward e_ω is ∫_{L₀}(ψ_ω − q₀·ψ). The difference quotients are dominated by 2‖ψ‖, and N_{q₀} is null.
  - Maximality gives s_ω(L₀) ≤ h(q₀) at every ω. The same holds toward any p ∈ Δ, giving p·s(L₀) ≤ h(q₀).
  - X₊ ⊆ B_{q₀} gives K_{q₀} ⊆ Q_{X₊}, so X₊ is consistent.
  - The bound γ ≥ −h(q₀) follows from ∫_G(p·ψ)⁺ ≥ p·s(X₊). OK.
- **The buffer.**
  - Q_τ = (1−τ)Q + τΔ ⊇ Q, and it decreases as τ ↓ 0.
  - P_{Q_τ} = (1−τ)P_Q + τ min_ω, so G_τ ↑ G exactly (the nonnegative gambles lie in every G_τ), and e_τ → 0.
  - Here, unlike in the audit, Q_τ is the trimming set itself, so no compactness lemma is needed. OK.
  - The buffer replaces f_X by a measure of violated mass: F_Z is continuous by (M2) and dominated convergence, vanishes exactly on Q_Z, and satisfies |F_Z − F_{Z′}| ≤ μ(Z△Z′). OK.
- **Trimming.** `lem:trim` applies with X := X₊ and N := X₊ ∩ G_τ ⊆ D_{Q_τ}, giving Q_R = Q. OK.
- **The robust hull inclusion.**
  - (1−τ)q + τΔ = {q′ ∈ Δ : q′ ≥ (1−τ)q} is a relative neighbourhood of q, so Q ⊆ int Q_τ.
  - With a = min_K F_R > 0 and μ(Z△X₊) ≤ μ(Y△X) ≤ ρ(X,Y): Q_{Z∖G_τ} ∩ K = ∅, so H(Z∖G_τ) ⊇ G_τ.
  - H is increasing in its argument, which gives H(Y∖G_τ) ⊇ G_τ.
  - The hull chain b_p∖Y ⊆ G_τ ⊆ H(Y∖G_τ) ⊆ H(Y∖b_p) has the monotonicity in the right direction. OK.
- **The uniform margin.** p·s(b_p) = ∫_{G_τ}(p·ψ)⁺ ≥ ∫_G(p·ψ)⁺ − e_τ, and |p·s(Y) − p·s(X)| ≤ ρ(X,Y). The gap exceeds γ/2 for ρ(X,Y) < r_X = min(γ/4, a/2). OK.
- **Closed witnessing sets, support coverage and KKM.**
  - p ↦ 1_{B_p} is continuous in measure because N_p is null for every p ∈ Δ, including the boundary. So the K_ω(Y) are closed.
  - The weighted inequality gives support coverage.
  - KKM gives p*. The strict gains exclude an all-world tie. OK.
- **The dominators are coherent and protected.** b_{p*} = D_{conv(Q_τ∪K_{p*})} is coherent and lies inside B_{p*}, so it is undominated by Thm 3(i). OK.
  - Consistency check: no *protected* coherent model can lie in a ball of radius r_X. If one did, G_τ ⊆ H(Y∖G_τ) ⊆ Y would give r·s(Y) ≥ r·s(b_r), against the gap. The proof is therefore self-consistent.
- **The repaired inconsistent case.** The hull clause is obtained through the consistent part X₊ and trimming, not through inconsistency of the removed part. This is valid.
  - R85c's counterexample to the audit's inference is correct: two patches near (1, −0.7) and (−0.7, 1) with ρ = 2 are consistent (supporting interval about [0.433, 0.567]), yet have negative box score at both worlds (`n2_protection.py` (F)).
- **The countable subcover.** X ↦ 1_X is an isometry into L¹((1+‖ψ‖)dμ), which is separable. That space has the same null sets as μ, since the weight is ≥ 1. A subspace of a separable metric space is Lindelöf, so countably many balls suffice. OK.
- **One remark.** Dominance of each incoherent X already follows from Theorem 8 with Y = X. The countable collection matters only for the structural condition.

**M4 (the audit's §7 conclusion survives in two worlds).** R85c labels the audit's §7 "FAILS verbatim". That is correct for the *inference*. But in n = 2 the audit's *conclusion* ("Y∖U is inconsistent") is true for every field satisfying (F) and (C). Proof (mine):
1. Suppose L₀ is consistent, with Q_{L₀} = [c, d].
2. X is inconsistent and K_{q₀} ⊆ Q_{X₊}, so K_{q₀} ∩ [c, d] = ∅. Say K_{q₀} lies below c.
3. Almost every g ∈ L₀ then has q·g < 0 for some q < c and c·g ≥ 0. So q ↦ q·g is increasing, and g₁ > 0.
4. Hence s₁(L₀) > 0, which contradicts s₁(L₀) ≤ h(q₀) < 0.
5. Robustness: min_Δ F_{L₀} > 0, and μ((Y∖U)△L₀) ≤ μ(Y△X).

A random search over 734 inconsistent two-world configurations found no consistent L₀, which is consistent with this argument (`out_n2_inconsistent.txt`). For n ≥ 3 the question is open.
- **Fix:** say "the inference fails; the conclusion holds for n = 2 and is open for n ≥ 3; the repair makes the question moot".

**M6 (tiny neighbourhoods).** I computed the radii exactly for the audit pair, using exact cap masses (`n2_radius.py`):

| ρ | γ | a | r_X |
|---|---|---|---|
| 1.5 | 1.13·10⁻² | 1.37·10⁻⁵ | 6.8·10⁻⁶ |
| 2 | 4.48·10⁻³ | 3.30·10⁻⁶ | 1.6·10⁻⁶ |
| 3 | 4.11·10⁻⁴ | 3.6·10⁻⁸ | 1.8·10⁻⁸ |

- **Fix:** state that the neighbourhoods exist but are microscopic, so only countability, not size, is being claimed.

**Numerical checks of Theorem 8** (exploration only):
- *Two worlds, X = T ∪ E* (`n2_selection.py`).
  - For ρ = 1.5, 2 and 3, the minimum over p of p·(s(b_p) − s(X)) is at least γ − e_τ.
  - The KKM points are p* = 0.4515, 0.5 and 0.5, with all-world gains 1.11·10⁻², 4.48·10⁻³ and 4.11·10⁻⁴.
  - The hull clause holds: Q(X∖b) = [0.3578, 0.6423] lies inside b's interval.
  - At ρ = 3 the dominator is T itself. This matches R85c's table.
  - Perturbations Y inside r_X, and perturbations 100 times larger, all pass with the same assignment.
- *Two worlds, inconsistent rivals* (`n2_inconsistent.py`). I tested T∪N, T∪P1∪P2 and P1∪P2 for ρ = 2 and 3.
  - s_ω(L₀) ≤ h(q₀) holds, with equality in the extremal cases.
  - The bound γ ≥ −h(q₀) holds up to quadrature error of about 3·10⁻⁴ relative, in cases where it is an equality analytically.
  - The dominators beat X at both worlds, and the hull clause holds.
- *Three worlds, X = T1 ∪ three balls* (`n3_selection.py`, Monte Carlo with 1.5·10⁶ samples).
  - At ρ = 1.5 the KKM point is the uniform prior, with gains (0.0180, 0.0179, 0.0177).
  - At ρ = 2 the gains are (0.0062, 0.0063, 0.0065).
  - In both cases the gains exceed γ/2, and the hull clause holds: Q(X∖b) ⊆ conv(Q_τ ∪ K_p), checked by LP.
- *Three worlds, X = T1 ∪ N* (`n3_lemma8b.py`). The interior maximiser is q₀ = (0.285, 0.285, 0.429). The values s_ω(L₀) = h(q₀) agree to 2·10⁻⁷, and all directional derivatives are ≤ 0.

## 6. Theorems 10 and 11: infinite worlds and transfer — OK as mathematics; G2, G3

**Theorem 10.** I checked each modification.
- E′, the closed sublattice generated by E, is separable: rational lattice-linear expressions in a dense sequence suffice, because the lattice operations are norm-continuous. So S′ is compact and metrizable.
- ψ is u-Lipschitz from E to E′, so m_ψ is a genuine Bochner integral of ψ(g), not of g.
- q∘ψ is superadditive (φ(x) = lx⁺ − ux⁻ is concave and positively homogeneous) and continuous. So B_q is an open convex cone containing E₊₊ and missing {sup g ≤ 0}.
  - appshort `lem:states`(b) then gives B_q = {P_{K_q} > 0}.
  - q∘ψ(g + t𝟙) ≥ q∘ψ(g) + lt puts the tie set inside cl B_q∖B_q ⊆ {P_{K_q} = 0}, which is null.
- Theorem 3(i) holds: m_ψ(B) ≤ 0 pointwise and r is positive.
- Lemma 8b's bound holds uniformly, since m_ψ(L₀) ≤ h(q₀)𝟙.
- The buffer Q_ε (the closed convex hull of the ε-neighbourhood) works:
  - ∩_ε Q_ε = Q by separation and compactness;
  - Q_ε ⊇ (1−λ)Q + λS, by uniform continuity on the compact set S×S×[0,1];
  - so `lem:trim` applies.
- F_Z is weak-* continuous on the metrizable S.
- The audit's §3 hypotheses hold with Θ = S′ and θ_F(p) = Σp_ωδ_ω.

So the sketch is a proof.

**G3 (write-up).** Three steps should be written out:
- (a) P_{Q_ε} ↑ P_Q pointwise, hence G_ε ↑ G and e_ε → 0. This needs the compactness argument of R85b §2.2.
- (b) Strong measurability of g ↦ ψ(g) into E′. This follows from continuity and separability.
- (c) The statement restricts to world-independent (l, u). It extends verbatim to 0 < inf l_ω ≤ sup u_ω < ∞, and should say so.

**G2 (the transfer is finite-world only).** Theorem 11 is stated for §§2–4, that is, for finite Ω, and its proof is correct there.
- (F) gives null ties, hence closed witnessing sets.
- (C) gives coherence of G ∩ B_p and consistency of X₊.
- The buffer and trimming do not involve ψ.

The brief asks for "every field with null ties and coherent Bayes sets" in the infinite-world setting too. That is not proved.
- **Fix:** add the hypotheses Theorem 10 actually uses:
  - (F∞): ψ: E → E′ is norm-continuous with ‖ψ(g)‖ ≤ c‖g‖, E′ is a separable sublattice, and each q∘ψ is superadditive, positively homogeneous and ≥ l·inf g on E₊₊;
  - null tie sets.

  Alternatively, restrict Theorem 11 explicitly to finite Ω. Theorem 3(ii) in infinite worlds stays UNCLEAR, as R85c says.

**M2.** C2 Prop 1.4 assumes null ties at *every* p. C2 Thm 1.1 gives null ties from W only at *interior* p.
- **Fix:** say "given null ties at every p ∈ Δ, (C) holds iff the complete ψ-ranking satisfies W".

## 7. Proposition 12: precise targets in two worlds — OK

I re-derived the proof and checked it numerically (`n2_prop12.py`, with β = 0.5).
- **Properties of the field.**
  - It is continuous: the largest jump between neighbouring directions on a grid of 2·10⁵ directions is 1.1·10⁻⁴, consistent with continuity.
  - It is sign-respecting, with loss weights in [1, 1+β].
  - It is weakly commission-averse everywhere, and strictly so off the rays g₂ = −g₁.
- **The sector map.** F(x) = x/κ(x) is strictly increasing, since κ − xκ′ = 1 − β + β(ln x − 1)² > 0. It maps (0,∞) onto (0,∞).
- **The Bayes sets.** They are sectors with x₀y₀ ≥ 1, so they are convex and coherent. The tie sets are rays, hence null.
  - x₀y₀ = 1 only at r = ½: for example 2.23 at r₁ = 0.2 and 1.69 at r₁ = 0.35.
  - With centre c, the protected precise model is q₁ = 1/(1+c). For c = 0.6 this is q₁ = 0.625.
- **Pure-removal LP.** For the centred field (c = 1), the target half-plane D_{½} admits no improving removal, while D_{0.4} and D_{0.6} are dominated, with gain 2.0·10⁻⁴.

**Constraints.**
- World-by-world guidance and independence follow from (F) via Prop 2.
- The full domain is kept.
- No loss profile is imposed, and no payoff integral is used: ψ = g only on a null set of rays.
- Selection holds by Theorem 11.
- Cross-coordinate dependence of ψ_ω on g_{−ω} is not forbidden by the handoff.

**Coverage in two worlds.** By §4 above, the field must be r-neutral on p^⊥, and it is. R85c's claim "every coherent model in two worlds is protected by some commission-averse hull ranking" is correct, provided "commission-averse" means weakly so for the Prop 12 member.

## 8. Proposition 14: the hull clause in posi form — OK

- **ess(B).** B∖ess(B) is null (by separability), and Q_B is determined by ess(B) (by continuity of q).
- **The cone.** K = cone(ess B) + E₊. Then K + E₊₊ = int K = int cl K, since K is convex with nonempty interior.
- **The closure.** Hahn–Banach gives cl K = {P_{Q_B} ≥ 0}, or E if Q_B = ∅. Its interior is D°_{Q_B}, which equals H(B) up to the null set {P_{Q_B} = 0}. OK.
- One can replace ess(B) by any conull subset of B, by perturbing within the margin ε.
- R85c's conceptual reading is accurate: the clause uses the axioms D2–D4 but not the class of coherent models.

**G1.** "A coherence-free gate built from ψ alone would protect at most the Bayes family" is not proved. Only one gate, F(B) = ∩{B_r : B ⊆ B_r}, is discussed, and even for that gate it is not shown that T1 is dominated.
- **Fix:** label it CONJECTURE, or prove it for that gate. To prove it, exhibit for ρ < 2 a change from T1 that adds A ⊆ F(B)∖T1, removes B, and raises every s_ω.

The "largest gate" bullet is a sound informal remark, but it is not a theorem. Label it REMARK.

## 9. Remark 13: lexicographic layers and intersections — OK (M5)

**M5.** The protected class of the lexicographic ranking is not merely "smaller or equal": it is **equal** to that of R_H^{ψ¹}.
- Let C ⊆ B¹_r. Any non-null pure removal B ⊆ C has r·s¹(B) > 0, so some world has s¹_ω(B) > 0. The removal is refused there at the first layer.
- Changes outside the hull clause are guided-only, and hence null.
- So the dominators b_p remain *undominated* under the lexicographic ranking as well.
- **Fix:** state equality.

**Intersections.** The intermediate-box reduction is correct: Λ·Ψ = Σ_ω p_ω(l̄_ω g_ω⁺ − ū_ω g_ω⁻), where (l̄, ū) are convex combinations of the judges' boxes. So intersections reach no target beyond Cor 7.

## 10. Claim 9 and C1 Theorem 3 (refereed) — OK (M3)

**C1 Theorem 2.**
- **(a).** By density fact (F), a strict improvement at the support of b_p can be approximated by an incoherent rival. W1, W2 and endorsement then give a contradiction. So s(b_p) is weakly Pareto-maximal; by Lyapunov and separation, b_p = B_r. OK.
- **(b).** If B_r were incoherent, its W-dominator would also maximise r·s, so it would equal B_r a.e. Reflexivity then contradicts dominance. OK.
- **(c), NC-i.** The copy lemma gives μ(B_{r_k} ∩ U_k) > 0. Pass to a limit r* ∈ P(T); the open-cone neighbourhoods have measure bounded below uniformly in k, which contradicts convergence in measure. OK.
- **(c), NC-ii.** A supporting half-space through 0 captures a half-ball of fixed radius in int B_{r*}. OK.

**C1 Theorem 3.** I checked each step.
- A(t) is nondecreasing and B(t) nonincreasing, by sign-respect in Q₊₋ and Q₋₊.
- s₁ and s₂ are strictly monotone in the sector angles.
- NC-i and NC-ii give t* and t** with A(t*) ≥ A_T ≥ A(t**).
- The two s-inequalities give B(t*) ≥ B_T ≥ B(t**).
- Both orderings of t* and t** force B_{t*} = T. OK.
- **MINOR:** "interior interval model" should state A_T + B_T ≤ π/2, and should state that μ has positive density on sectors (Gaussian).

**Numerical sanity check** (ρ = 2, `n2_protection.py` (B)):
- P(T) = {t : s(B_t) ≥ s(T)} = [0.492, 0.508].
- Every K_t in P(T) lies inside (0.25, 0.75), so NC-ii fails, as C1 Cor 4 predicts.
- tan A · tan B = 0.25 = 1/ρ² along the whole Bayes family, while T has 1/9.

**Claim 9.** R_H^ψ satisfies (E_ψ), since every accepted comparison raises s_i. It is independent, and for 1 < ρ < 3 it protects T (Cor 5), which is not a box Bayes set. So by C1 Thm 3 no single assignment satisfies W, while Cor 9 gives the countable condition. **The separation of W from the countable condition, using a commission-averse score, is established.**

**M3.** R85c §6 says "under W, any box-endorsed ranking, by C1 Thm 2–3, only Bayes sets survive". This is proved for n = 2 only; for n ≥ 3 it is C1's conjecture R8. Likewise, Cor 5.1 cites C2 Thm 4.2, which is an n ≥ 3, complete-integral result.
- **Fix:** add these qualifiers.

---

## 11. Verdict

**1. Is every incoherent model dominated under each box hull ranking? Yes.**
- **Finite worlds.** For every full box (l_ω < u_ω) and every μ satisfying (M1) and (M2) (Gaussian included):
  - each incoherent model is dominated, at every world, by a coherent model D_{conv(Q_τ∪K_p)} that is itself undominated;
  - the countable selection condition holds;
  - the margin is γ/2 on a ρ-ball, which is microscopic (M6).
  - Atomlessness is not needed (M1).
- **Infinite worlds.** The same holds for boxes with constant (l, u), and by the same proof for 0 < inf l ≤ sup u < ∞, on any separable E containing 𝟙, using S′. This is a proof modulo the write-up items in G3.

**2. Which coherent models are covered by the class of box hull rankings? Exactly the following.**
- **The criterion (finite n, full-support μ).** D_Q is covered iff Q contains a vertex, or Q ∩ Δ_F has nonempty interior relative to aff Δ_F for some face with |F| ≥ 2.
- **Two worlds.** Every coherent model is covered except the precise interior ones.
- **Three worlds.** The covered models include:
  - every full-dimensional credal set, including T1;
  - every set touching a vertex;
  - every set that is a full segment inside an edge.
- **Not covered by any full box.** Every precise non-vertex model, and every lower-dimensional credal set that contains no vertex and is not full-dimensional in any face. Examples are interior segments, including those pointing at a vertex, and points in the interior of an edge.

**Nearby results that are available now:**
- **Boxes give a dense class.** The covered class is Hausdorff-dense among credal sets, since any Q can be thickened.
- **Two worlds, full coverage.** Adding R85c's Prop 12 fields gives family-level admissibility of every coherent model.
- **The n ≥ 3 gap.** Closing it needs fields whose r-aggregate is commission-neutral on a whole subspace (§4); this is a necessary condition.

**R85c's main claims stand.** Before anything goes to the author, R85c should make the fixes listed above:
- G1: label the coherence-free-gate claim a conjecture;
- G2: restrict Theorem 11 to finite Ω, or add (F∞);
- G3: write out the Theorem 10 steps;
- M1–M8: the qualifiers and wording.
