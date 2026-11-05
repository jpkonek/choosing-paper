# C1 report (round 84): commission-averse independent rankings under W

Agent C1, 29 Oct 2026. The payoff integral and Brier are used nowhere: not as rankings, not as constraints, not as assignment sources. The only scores used are sign-respecting commission-averse fields ψ, together with μ-masses.

---

## 0. Results first

**No construction for T1 was found.** The attempt produced one positive check and three structural results. Together they isolate the obstruction precisely.

| # | Result | Label |
|---|---|---|
| R1 | **Copy–KKM lemma.** Under independence, a dominating change is never available at any undominated model. So under W, the assigned dominator b of every incoherent x satisfies x ∉ [b∩T, b∪T]. | PROVED |
| R2 | **Endorsement theorem (n worlds).** Suppose the comparisons that assigned models win against incoherent rivals never lower some sign-respecting additive field ψ (integrable, with null Bayes boundaries). Then W forces three things. (a) Every assigned model is a ψ-Bayes set. (b) Every ψ-Bayes set is almost coherent. (c) The protected target T must satisfy a *straddling condition* NC(ψ,T). | PROVED |
| R3 | **Two-world theorem.** For n = 2, NC(ψ,T) holds only if T is itself a ψ-Bayes set. Protection by refusals therefore buys nothing for endorsed rankings. | PROVED |
| R4 | **Step 1, the audit pair.** A box-endorsed ranking satisfying W can protect T iff u₁u₂ = 9 l₁l₂. In that case T is the box Bayes set and T itself is X's dominator. T does not contain X. T dominates every rival in an explicit neighbourhood of X. W holds for all incoherent rivals. | PROVED |
| R5 | **Candidate A** (symmetric box, with refusals protecting T1, box assignment). All of the following hold: guidance, independence, the three-model condition, transitivity through ties, T1 undominated, and pointwise support defence. **W1–W3 fail for every assignment**: NC fails for every ρ tested with a = 0.1, 0.2, 0.3. | Properties PROVED. W failure CHECKED: rigorous reduction via R2, then exact-integral numerics. |
| R6 | **Candidate B** (lexicographic: commission first, or omission first). It leaves T1 dominated; in fact it leaves dominated every model that commits, respectively omits, at every world. | PROVED |
| R7 | **Candidate C** (T1's rescaled family as the assignment, maximal acceptance, one refusal world for T1 threats). Independence, guidance, T1 undominated and pointwise support defence hold. **The three-model condition and transitivity through ties FAIL** (three-patch counterexample). | PROVED |
| R8 | **Conjecture.** R3 holds for n = 3. With Theorem gm, this would exclude every endorsed ranking for T1 under W. | CONJECTURE (numerical support: R5) |

**Diagnosis (§6).** The obstruction is a squeeze, not a continuity problem.
- The ordering conditions come for free when acceptances are endorsed by a score. Every rule in the brief's candidate list is so endorsed, or is lexicographic.
- Endorsement plus W plus the copy lemma forces the target to be a Bayes set of the endorser. This is proved for n = 2 and conjectured for n = 3.
- Theorem gm then excludes T1, subject to C2's check that gm survives under W.

For endorsed rankings the obstruction is therefore axiom-level, once R8 is settled. For non-endorsed rankings it is construction-level. Only three escapes remain, listed in §6.

---

## 1. Setting and two tools

Ω = {1,…,n}; E = ℝⁿ; μ is standard Gaussian; models are measurable sets modulo null sets.

- **Changes.** The change X→Y adds Y∖X and removes X∖Y. It is *available at Z* if Z contains what is removed and misses what is added. It is guided, or anti-guided, at i in the usual sense.
- **Independence** in the brief's arbitrary-set form is equivalent to: the verdict "Y ⪰_i X" depends only on the change. (Proof: take D = XΔY, F = X∩Y, and G = the context of any other pair with the same change.)
- **Fields and scores.** For a field ψ = (ψ₁,…,ψₙ) write s_i(X) = ∫_X ψ_i dμ and B_r = {g : r·ψ(g) > 0} for r ∈ Δ.
- **Sign-respecting** means ψ_i(g)g_i > 0 for a.e. g.
- **(N)** means μ{r·ψ = 0} = 0 for every r ∈ Δ.
- **Representatives.** Each almost coherent model equals a.e. a unique open convex cone, its canonical representative. The boundary of a convex set is Lebesgue-null, and two open convex sets that agree a.e. are equal. Below, cl and int always refer to this representative.
- **The audit's T** is the sector (−τ, π/2+τ) with τ = arctan(1/3).
- **T1** = D_M with M = {m : m_i ≥ a}. Then T1 = {g : aΣg_i + (1−3a)min_k g_k > 0}.

**Density fact (F).** For every model Y and every ε > 0 there is an incoherent model x with ∫_{xΔY}|ψ| dμ < ε.

*Proof.* Let P be a small ball bounded away from 0. If Y and YΔP were both almost coherent, P would be a.e. equal to the symmetric difference of two cones, hence invariant under dilation modulo null sets. A bounded non-null set is not. So either Y or YΔP is incoherent. ∎

---

## 2. The copy–KKM lemma (R1), PROVED

**Lemma 1.** Assume independence. If Z is undominated and b dominates x, then the change x→b is not available at Z. Equivalently, it is not the case that b∩Z ⊆ x ⊆ b∪Z a.e.

*Proof.*
1. Suppose the change x→b, which adds b∖x and removes x∖b, is available at Z. Let Z' be the result of applying it to Z.
2. By independence, every comparison Z' ⪰_i Z has the same verdict as b ⪰_i x.
3. Every reverse comparison Z ⪰_i Z' has the same verdict as x ⪰_i b, because the reverse change is also common to both pairs.
4. Hence Z' dominates Z, a contradiction. ∎

**Corollary 1.** Assume independence and W, and let T be undominated.
- For each incoherent x, Theorem W gives p with b_p dominating x.
- By Lemma 1, x ∉ [b_p∩T, b_p∪T].
- In particular, if x ⊇ T then x∖T ⊄ b_p; and if x ⊆ T then b_p∩(T∖x) is non-null.

This is the audit's copy lemma, which is the case Z = T ⊆ x ⊆ b, applied to every undominated model at once.

---

## 3. The endorsement theorem (R2), PROVED

**Hypotheses.**
- ψ is sign-respecting, ∫|ψ| dμ < ∞, and (N) holds.
- The ranking satisfies W with assignment p ↦ b_p.
- **(E_ψ), endorsement at assigned models:** if x is incoherent and b_p ⪰_i x, then s_i(b_p) ≥ s_i(x).

Every subrelation of the ψ-score ranking satisfies (E_ψ).

**Theorem 2.**
- (a) For every p there is r ∈ Δ with supp r ⊆ supp p and b_p = B_r a.e.
- (b) Every B_r (r ∈ Δ) is almost coherent.
- (c) Assume also independence, and let T = D_M be almost coherent and undominated. Put P(T) = {r : s(B_r) ≥ s(T) componentwise}. Then:
  - (NC-i) every g ∈ T∖{0} lies in cl B_r for some r ∈ P(T);
  - (NC-ii) every g ∉ cl T lies outside int B_r for some r ∈ P(T).

  Equivalently, NC-ii says M ⊆ cl conv ⋃_{r∈P(T)} K_r, where B_r = D_{K_r}.

*Proof of (a).*
1. Let S = supp p, and let R ⊆ ℝⁿ be the range {s(Y)} over all models Y. R is compact and convex by Lyapunov's theorem, since μ is atomless.
2. Suppose some Y has s_i(Y) > s_i(b_p) for every i ∈ S. By (F) there is an incoherent x with the same strict inequalities.
3. By W2 some i ∈ S has p ∈ A_i(x). Then W1 gives b_p ⪰_i x, and (E_ψ) gives s_i(b_p) ≥ s_i(x). This is a contradiction.
4. So s(b_p), restricted to S, is weakly Pareto-maximal in the convex projection of R. Separation gives r ≥ 0, supported in S and nonzero, with r·s(b_p) = max_R r·s.
5. So b_p maximises ∫_Y r·ψ dμ. Hence b_p ⊇ {r·ψ > 0} and b_p ∩ {r·ψ < 0} is null. By (N), b_p = B_r a.e. ∎

*Proof of (b).*
1. B_r is the unique maximiser of r·s, by (N).
2. Suppose B_r were incoherent. Theorem W gives an assigned b_p dominating it.
3. By (E_ψ), s(b_p) ≥ s(B_r), so b_p also maximises r·s. Hence b_p = B_r a.e.
4. Then b_p and B_r are tied by reflexivity, so b_p does not dominate B_r. This is a contradiction. ∎

*Proof of (c), NC-i.*
1. Fix g ∈ T∖{0}. Let U_k be a non-null subset of T ∩ B(g, 1/k) bounded away from 0, and put x_k = T∖U_k. Each x_k is incoherent, by the dilation argument of (F).
2. By Corollary 1 and (a), there is r_k with B_{r_k} dominating x_k and μ(B_{r_k} ∩ U_k) > 0.
3. By (E_ψ) at the KKM point, s(B_{r_k}) ≥ s(x_k), and s(x_k) → s(T).
4. Pass to a subsequence with r_k → r*. By (N) and dominated convergence, B_{r_k} → B_{r*} in measure, and r ↦ s(B_r) is continuous. Hence r* ∈ P(T).
5. Suppose g ∉ cl B_{r*}. The representatives C_k of B_{r_k} are open convex cones containing (0,∞)ⁿ, and each contains a point h_k with h_k → g.
6. For small η, each C_k therefore contains {λh_k + (1−λ)e : 1−η < λ < 1, e ∈ (0,∞)ⁿ ∩ B(0,|g|)}. This set lies near g, outside cl B_{r*}, and has measure bounded below uniformly in k.
7. That contradicts B_{r_k} → B_{r*} in measure. ∎

*Proof of (c), NC-ii.*
1. Use x_k = T ∪ E_k, where E_k is a non-null subset of B(g, 1/k) ∖ cl T bounded away from 0. Here μ(E_k ∖ B_{r_k}) > 0.
2. Pick k_k ∈ E_k ∖ C_k. Since C_k is an open convex cone, there is a closed half-space through 0 that contains k_k and misses C_k.
3. If g ∈ int B_{r*}, that half-space captures a half-ball of fixed radius inside B_{r*}. Then μ(B_{r*} ∖ B_{r_k}) is bounded below, a contradiction.
4. **The duality.** If M ⊆ Q := cl conv ⋃K_r, a negative lower prevision under M gives a negative one under some K_r. Conversely, if m₀ ∈ M∖Q, separate it from Q and subtract a constant to obtain g with m₀·g < 0 < min_Q. ∎

**Remark.** No closedness of any section, and no ordering condition, is used. Pointwise support defence can hold while NC fails; Candidate A is an example. The theorem does not cover:
- endorsers with blind sets, where (N) fails;
- non-integrable (finitely additive) endorsers;
- rankings with no endorser at all.

---

## 4. Two worlds (R3, R4), PROVED

**Theorem 3.** Let n = 2, and assume the hypotheses of Theorem 2(c), with T an interior interval model, the sector (−A_T, π/2+B_T) with 0 < A_T, B_T. Then T = B_t a.e. for some t.

*Proof.*
1. **Sector structure.** By Theorem 2(b), each B_t, with t = r₁, is a.e. an open sector (−A(t), π/2+B(t)). Within the quadrant Q₊₋ (g₁ > 0 > g₂), the set B_t is increasing in t, because ψ₁ > 0 > ψ₂ there. So A is nondecreasing; symmetrically, B is nonincreasing.
2. **Monotonicity of scores.** Sign-respect and the Gaussian positivity of sectors give the following. s₁(sector(A,B)) is strictly increasing in A and strictly decreasing in B. s₂ is strictly decreasing in A and strictly increasing in B.
3. **Two limit points.** P(T) is compact, and B_{t_k} → B_t in measure forces the angles to converge. Apply NC-i at the directions −A_T + 1/k (inside T) to get t* ∈ P(T) with A(t*) ≥ A_T. Apply NC-ii at the directions −A_T − 1/k (outside T) to get t** ∈ P(T) with A(t**) ≤ A_T.
4. **Bounding B(t*) and B(t**).**
   - If B(t*) < B_T, then s₂(B_{t*}) ≤ s₂(A_T, B(t*)) < s₂(T), contradicting t* ∈ P(T). So B(t*) ≥ B_T.
   - Likewise, B(t**) > B_T would give s₁(B_{t**}) < s₁(T). So B(t**) ≤ B_T.
5. **Case t* ≤ t\*\*.** Monotonicity gives A(t*) = A_T. Then s₁(B_{t*}) − s₁(T) = ∫ψ₁ over the angles (π/2+B_T, π/2+B(t*)). This is ≤ 0, with equality only if B(t*) = B_T. So B_{t*} = T.
6. **Case t* > t\*\*.** Monotonicity gives B(t*) = B_T. The same argument applied to s₂ gives A(t*) = A_T, so B_{t*} = T. ∎

**Corollary 4 (boxes; the audit pair).** Take ψ_i = l_i g_i⁺ − u_i g_i⁻.
- Then tan A(t) = t l₁ / ((1−t)u₂) and tan B(t) = (1−t)l₂ / (t u₁). So tan A · tan B = l₁l₂/(u₁u₂) along the whole family.
- The audit's T has tan A_T = tan B_T = 1/3.
- So a box-endorsed ranking satisfying W with T undominated exists **iff u₁u₂ = 9 l₁l₂**. For the symmetric box this means ρ = u/l = 3.
- For ρ ≠ 3 no refusal pattern and no assignment works. Exact two-world formulas confirm this:
  - for ρ < 3, every model in P(T) accepts gambles just outside both rays of T;
  - for ρ > 3, every model in P(T) rejects gambles just inside both rays.

**Proposition 5 (Step 1 sanity check, ρ = 3, no refusals).**
1. **The dominator.** Let E = E_a ∪ E_b be the balls about (2,−1) and (−1,2), and m = μ(E_a) = μ(E_b), equal by the coordinate swap. Then ∫_E ψ₁ ≤ 2.1m + 3(−0.9)m = −0.6m, and the same bound holds for ψ₂ by symmetry. So **T ≻_i X at both worlds, by margin ≥ 0.6m**. X's dominator is T = b_{(½,½)}, and T ⊉ X.
2. **The neighbourhood.** Every model X' with ∫_{XΔX'}|ψ_i| < 0.6m for i = 1, 2 is strictly dominated by T.
3. **All incoherent rivals.** The box satisfies (S), so W holds with b_p = B_p.
4. **Rivals containing T.** By Corollary 1, for every incoherent X ⊇ T the W-dominator misses part of X∖T. For example, if E sits just below T's lower ray, the dominator is a B_p with p₁ slightly above ½, whose boundary cuts through E. ∎

---

## 5. Three worlds: candidates for T1

### Candidate A: refusal-protected box (R5)

**Definition.**
- Fix ρ ≥ 1 and ψ_i = g_i⁺ − ρg_i⁻.
- A *threat* is a non-null change available at T1 that strictly raises every s_k.
- A T1-available change guided at every world is null: it could add only (+,+,+) gambles, which already lie in T1, and remove only (−,−,−) gambles, which T1 lacks. So for a threat d, the index j(d) := the least world at which d is not guided exists.
- **The rule.** Y ⪰_i X iff either Y = X a.e., or s_i(Y) > s_i(X) and the change X→Y is not a threat with j = i.
- **The assignment.** b_p = B_p.

**Properties.** All of the following are PROVED.
- *Independence:* the rule is a function of the change.
- *Guidance:* a guided non-null change strictly raises s_i and has j ≠ i; its reverse lowers s_i.
- *Three-model condition, and transitivity through ties:* every accepted non-null comparison strictly raises s_i. So a ⪰ b ⪰ c with c ≻ a would give s_i(c) > s_i(a) ≥ s_i(c). And ties hold only a.e.
- *T1 undominated:* any dominating change from T1 is a threat, and is refused at its j.
- *Pointwise support defence:*
  - If the change is not a threat, Bayes optimality gives a strictly improving world in supp p.
  - If it is a threat, it is refused at one world only. That leaves another support world when |supp p| ≥ 2. When p = e_k, the change to P_k is guided at k, so j ≠ k.

**W1–W3 fail** (CHECKED).
1. Candidate A satisfies (E_ψ), and ψ satisfies (N). So by Theorem 2 *every* assignment satisfying W would satisfy NC(ψ,T1).
2. I computed s(B_r) and s(T1) exactly, as Gaussian moments of polyhedral cones: ∫_C g dμ = (2π)^{−3/2} Σ_facets (angle × inward normal), validated against Monte Carlo.
3. I then tested NC on a grid in Δ (spacing 1/90 for a = 0.2, 1/60 otherwise) and on 3·10⁵ random directions.

| a | ρ tested | violation |
|---|---|---|
| 0.2 | 1.5, 2, 2.5 | non-T1 gambles accepted by all of P(T1), e.g. direction (−0.67, 1, 1); margin up to 0.17 |
| 0.2 | 2.5, 3, 4, 6, 10 | T1 gambles rejected by all of P(T1), e.g. (−0.245, 1, −0.251), a two-loss gamble at T1's ridge; margin up to 0.19 |
| 0.1 | 2, 4, 8, 12, 20 | failure every time; the failing gamble for ρ ≥ 8 is (1, −0.105, −0.111) |
| 0.3 | 1.2, 1.5, 2.33, 3, 5 | failure every time |

For 2 ≤ ρ ≤ 4 (a = 0.2), P(T1) contains no grid point other than u.

The two-loss failures sit exactly where the rescaled family's charts are wedges, not half-planes: these are the gambles with two negative coordinates. Scripts: `r84/c1py/exact_box.py`, `nc_exact.py`, `two_world.py`.

### Candidate B: lexicographic (R6), PROVED

**Definition.** At world i, compare the net new commission mass μ(A∩N_i) − μ(B∩N_i) first, and the net new omission mass second. Here A is the added set and B the removed set.

**Properties.** It is a complete preorder (lexicographic order on (μ(X∩N_i), μ(P_i∖X))). It is independent and guided.

**Failure.**
1. Let X be any model with μ(X∩N_k) > 0 for every k. Removing non-null R_k ⊆ X∩N_k for every k strictly lowers commission at every world, so X is dominated.
2. T1 commits at every world, so T1 is dominated.
3. Omission-first is symmetric: adding pieces of P_k∖X dominates any model that omits at every world.

### Candidate C: rescaled-family assignment with maximal acceptance (R7)

**Definition.**
- b_p = {g : p∗g ∈ T1}, the rescaled family; b_{e_i} = P_i and b_u = T1.
- For a change d, let I(d) be the set of worlds where d is accepted. It contains every world except:
  - the worlds where d is anti-guided;
  - when d is a non-null T1-available change with no anti-guided world, the least non-guided world.

**Proved properties.**
- Independence, reflexivity and guidance hold.
- T1 is undominated, since every non-null change from T1 is refused somewhere.
- **Face lemma.** If supp p ⊆ J and x→b_p is anti-guided at every world of J, the change is null. (p∗g ≤ 0 with p∗g ≠ 0 forces g ∉ b_p; p∗g ≥ 0 with p∗g ≠ 0 forces g ∈ b_p.)
- Hence pointwise support defence holds for every rival, and no score is used anywhere. This is a genuinely non-endorsed rule.

**Failure: the three-model condition and transitivity through ties.**
1. At world 1, take disjoint patches g₁ near (1,1,1) (in T1, g₁ > 0), n₁ near (−1,−2,−2) (outside T1, g₁ < 0) and n₂ near (−1,3,−3) (g₁ < 0). Let Z₀ miss all three.
2. Put x = Z₀, z = Z₀ ∪ g₁ ∪ n₁ and y = Z₀ ∪ n₂.
3. x→z is mixed at world 1 and unavailable at T1 in either direction, so z ~₁ x.
4. z→y is mixed at world 1 (removing n₁ helps) and not T1-available, so y ⪰₁ z.
5. But x→y only adds n₂, so it is anti-guided, and x ≻₁ y.
6. This breaks transitivity through ties. Taking (a, b, c) = (y, z, x) breaks the three-model condition.

*The general lesson.* Without a score, a mixed change must be one of three things:
- **oriented**, which needs a score;
- **tied**, and then ties must stay neutral under any later worsening, which this rule violates;
- **incomparable**, which removes the defences W needs.

---

## 6. The obstruction, and what remains

1. **For endorsed rankings it is axiom-level (n = 2 proved; n = 3 conjectured).**
   - Under independence, world-by-world guidance and W, endorsement by any integrable sign-respecting field with null Bayes boundaries forces the protected target to be one of that field's Bayes sets. All of those Bayes sets are then almost coherent.
   - The brief's threshold, region-dependent and cross-coordinate additive rules all fall in this class, as do refusal-protected boxes and smooth context-robust (intersection-over-contexts) versions of non-additive scores.
   - With Theorem gm, if C2 confirms it survives under W, R8 would exclude T1 for the whole class.
   - So under W, endorsed rankings reach the same targets as under (S): W's extra freedoms (an unassigned target, dominated or incoherent assigned models) are inert here.
2. **Otherwise it is construction-level.** Nothing excludes:
   - **blind-set endorsers**, where (N) fails; the record's D2 and VB constructions used such sets;
   - **non-integrable endorsers**, where Lyapunov fails;
   - **rankings with no endorser at all.**

   Such rankings must satisfy the ordering conditions without one. Those conditions constrain only *realisable* compositions. So a successful rule must have accepted changes whose formal nonnegative combinations are anti-guided, with all such combinations non-realisable (for example, because they add the same gamble twice). Candidate C shows that the naive version breaks the conditions.
3. **Nearby reachable results.**
   - In two worlds, Corollary 4 shows boxes are exactly what W can do with endorsed rankings. They cover every interior interval.
   - In three worlds, the W-reachable targets under endorsement are, conditional on R8, the coherent Bayes families of additive fields: rescaled boxes, and the gauge-mixture polygons near T1 from the record.
4. **Recommended next round.**
   - (i) Prove or refute R8. NC's dual form (M ⊆ cl conv ⋃K_r, together with T ⊆ ⋃ cl B_r over r ∈ P(T)) is the natural handle.
   - (ii) Decide whether blind-set or finitely additive rankings are acceptable before anyone builds one.
