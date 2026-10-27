# PP66. The two-neighbourhood rejection test: passed, by an explicit relation

23 October 2026. Diagnostic for Brief 55 (section "Two-neighbourhood rejection test"; AUDIT_round55_answers §1). One author; not refereed. No axiom added; the hypotheses used are listed in §6.

**Labels.** PROVED: complete argument here, or a cited result used within its stated hypotheses. CHECKED: exact integer computation in `r9/PP66_py/` (ends ALL PASS). CONJECTURE / OPEN: as stated. No NUMERICS are used for any claim.

---

## 0. Verdict

**Answer (a): the test is achievable (PROVED; CHECKED).** This includes the hardest case: a u¹-balanced swap, which is Theorem E's configuration, with any choice of the refusing world w, including the middle world m of the pair. Whether a = u or b = u makes no difference.

**The relation** (§2) is R₀ built on a perturbed balanced field ψ, followed by one single-world refusal surgery:
- **The field.** ψ := u¹ + φ_F. The perturbation φ_F is supported on the swap set F. It sums to zero over worlds and is asymmetric between the two worlds v, v′ ≠ w. It makes the swap record ψ-unbalanced with opposite signs at v and v′.
- **The surgery.** Refuse, at w only, every record within d-distance δ of r = rec(C_a, X) or of r⁻¹ = rec(C_b, Y).

Everything the test lists holds, on all records and all triangles:
- reflexivity, (IB), strict (G) and (TC);
- defence of every member of N against every measurable rival;
- protection of every member, so undominatedness and direct (C) hold too;
- the two reservations, which are open neighbourhoods of a and of b;
- the α = (1, 1) certificate, so no common reweighting certifies the pattern.

**Local shape, for the constructor.** On d-balls around the inverse pair:
- at w: r and r⁻¹ are incomparable (both refused);
- at v: the a-end is strictly preferred (C_p ≻_v X);
- at v′: the b-end is strictly preferred (C_q ≻_{v′} Y);
- outside the balls: ψ-additive.

**Pure-shift germs.** Members shifted from a toward e_w defend at v. Members shifted from b toward e_w defend at v′. For a balanced F these acceptances are u¹-unfavourable: they are exactly PP62 Cor E.2(i)'s literals. They are supplied by φ_F, not by u¹.

**Lemma S cascades terminate in one step.** At v the ψ-negative split link is refused. That link is u¹-favourable, as PP63's sharpened E.2(ii) requires. At w no triangle passes through the balls.

**What the test does reject (PROVED, §3).**
- Every allocation whose acceptances near the pair, at the two worlds other than w, are endorsed by a field whose h/S increments on F are world-symmetric outside the odd world. This includes every q·u¹ with a common weight q.
- The rejection holds when w = m. For u¹ itself it holds for every w (Theorem E).
- A d-robust version of the shape *must* defend the two ends at different worlds (Lemma T).

**What it cannot reject.** It does not reject proposals that handle swaps one at a time. Its rival is fixed before the relation is chosen, so it lies within the scope of PP61 Theorem C and PP63 Prop 4.6. To discriminate, the swap must be balanced for the proposal's own field (§5).

| Item | Result | Label |
|---|---|---|
| ψ = u¹ + φ_F keeps (U1), (U2); R₀^ψ satisfies Theorem R | Lemma 1 | PROVED |
| R₁ = R₀^ψ + one-world ball surgery passes the whole test | Theorem 2 | PROVED; CHECKED |
| Variant with Theorem L's Λ^ψ in place of R₀^ψ | Cor 2.1 | PROVED |
| World-symmetric endorsement fails at w = m (common q included) | Prop 3 | PROVED |
| No robust two-sided acceptance at one world | Lemma T | PROVED |
| Exact 4096-model instance: all clauses for w = 1, 2, 3 (ψ) and for w ≠ m (common q); controls fail as predicted | §4 | CHECKED |
| Whether every admissible field has balanced interior swaps | §5 | CONJECTURE |

---

## 1. Setting and the perturbed field

**Setting.** The setting is BRIEF54 and PP62 §1.1:
- 𝒮₀ ⊇ N, with (2V);
- u¹ is PP56 §4.1's level-0 field, with properties (U1)–(U3) (PP62 §1.1);
- R is the disagreement region, so members agree off R and say h(g) or S on R;
- the record vector is V^f(rec(X, Y)) := Φ^f(Y) − Φ^f(X), with Φ^f(Z) := ∫ f(g, Z(g)) dμ;
- the record metric is d(ρ₁, ρ₂) := μ{ρ₁(g) ≠ ρ₂(g)} (PP63 §1);
- X ⪯_i Y ("X at least as good as Y at i") iff i ∉ R(rec(X, Y)).

**The test configuration.** Fix interior a, b ∈ N and a measurable non-null F ⊆ D_ab := {C_a ≠ C_b} ⊆ R. Put X := C_a[F ↦ C_b], Y := C_b[F ↦ C_a] and r := rec(C_a, X). By (IB), rec(C_b, Y) = r⁻¹.

Fix the world w, and write v, v′ for the other two worlds (in either order). Let F_w^± be the parts of F where X is strictly w-better or strictly w-worse than C_a. Every point of F is in one of them, because ranks are injective in the advice.

**Hypothesis (Mix_w).** μ(F_w⁺) > 0 and μ(F_w⁻) > 0.

For a u¹-balanced F (V(r) = 0), PP62 Cor 1.2 puts F on the odd-world-m points with c_m = 0. Both kinds of odd-world-m point then carry positive mass. One kind improves m and worsens the other two worlds; the other does the reverse. So **(Mix_w) holds for every w.**

**The perturbation.** For g ∈ F, let s(g) = +1 if C_a(g) = h(g) and C_b(g) = S, and s(g) = −1 in the opposite case. Define

  φ_F(g, h(g)) := −s(g)·(|g|/2)·(e_v − e_{v′})  for g ∈ F;  φ_F := 0 otherwise (other g, other values),
  ψ := u¹ + φ_F.

**Lemma 1 (PROVED).**
- (i) Σ_i ψ_i(g, x) = Σ_i u¹_i(g, x) for every g and every advice value x. So (U2) holds for ψ: every member is pointwise (1, 1, 1)-Bayes.
- (ii) |ψ| ≤ K_ψ|g| with K_ψ := K + 1, and ψ_i is strictly increasing in the i-rank at every g, over all four values. This is (U1).
- (iii) V^ψ(r) = V(r) + Θ(e_v − e_{v′}), where Θ := ½∫_F |g| dμ > 0.
- (iv) R₀^ψ (PP62's rule with ψ in place of u¹, any w₀) satisfies every conclusion of PP62 Theorem R, on all records and all triangles: (IB), reflexivity, strict (G), (TC), defence of every member against every rival, and protection.

*Proof.*
- **(i).** φ_F(g, x) is a multiple of e_v − e_{v′}, whose coordinates sum to zero.
- **(ii).** Only the value h on F moves, by at most |g|/2 per coordinate. By PP56's formula, on R the value h is at distance at least |g| from each of its rank neighbours, at every world:
  - at a Wr = {o} point:
    - at a correct world: h = −|g| and S = 0;
    - at o: h = 2|g|, S = 0 and C ≥ 3|g|;
  - at a Cor = {o} point:
    - at o: h = −2|g| and S = 0;
    - at a wrong world: h = |g|, S = 0 and C ≥ 5|g|.

  So every strict rank inequality survives. The bound on |ψ| is immediate.
- **(iii).** At g ∈ F the record r moves h → S if s = +1, contributing φ(S) − φ(h) = +(|g|/2)(e_v − e_{v′}). It moves S → h if s = −1, contributing φ(h) − φ(S) = +(|g|/2)(e_v − e_{v′}). Integrate over F.
- **(iv).** PP62's proof of Theorem R uses only three things: (U1) (steps 2–3), additivity of V (step 4) and (U2) (step 5). All three hold for ψ by (i) and (ii). ∎

**Continuity of V^ψ in d (PROVED).** Suppose d(ρ, ρ′) < δ, with disagreement set E. Each coordinate of V^ψ(ρ) − V^ψ(ρ′) is an integral over E of four terms, each bounded by K_ψ|g|. So

  |V^ψ_i(ρ) − V^ψ_i(ρ′)| ≤ 4K_ψ ∫_E |g| dμ ≤ 4K_ψ σ √δ,  with σ² := ∫|g|² dμ,

by Cauchy–Schwarz.

---

## 2. The relation and the theorem

**Hypothesis (Sgn).** V^ψ_v(r) > 0 > V^ψ_{v′}(r). By Lemma 1(iii) this means V_v(r) > −Θ and V_{v′}(r) < Θ.
- It holds whenever F is u¹-balanced, for every w (since V(r) = 0).
- It holds whenever V_v(r) > 0 > V_{v′}(r) already; then one can even take φ_F = 0, i.e. ψ = u¹.

**Choice of δ.** Take δ > 0 with:
- δ < min(μ(F_w⁺), μ(F_w⁻));
- 4K_ψσ√δ < κ := min(V^ψ_v(r), −V^ψ_{v′}(r)).

Put 𝒰 := B_δ(r) ∪ B_δ(r⁻¹), a set of records. By the isometry of inversion (PP63 Lemma 1.1(a)), 𝒰⁻¹ = 𝒰.

**The relation R₁.** For every ordered record ρ of measurable four-advice models:

  R₁(ρ) := R₀^ψ(ρ) ∪ ({w} if ρ ∈ 𝒰).

Nothing is unassigned.

**Theorem 2 (PROVED).** Assume (2V) on 𝒮₀ ⊇ N, (Mix_w) and (Sgn). Then R₁ satisfies the following.
1. Reflexivity and (IB) on every record, including reverses and all common-context copies.
2. Strict (G) on every record at every world.
3. (TC) on every triangle of measurable models.
4. **Universal defence.** For every p ∈ N and every measurable Z ≠ C_p, R₁(rec(C_p, Z)) ≠ {1, 2, 3}.
5. **Protection.** For every p ∈ N and every Z ≠ C_p, R₁(rec(Z, C_p)) ≠ ∅. Hence undominatedness holds (vacuously), and direct (C) holds for coherent and incoherent Z alike. In particular T = C_u is protected.
6. **Reservations.** Put U_a := {p ∈ N : μ(C_p ≠ C_a) < δ} and U_b := {q ∈ N : μ(C_q ≠ C_b) < δ}. These are open neighbourhoods of a and b, with:
   - C_p ⋠_w X for all p ∈ U_a;
   - C_q ⋠_w Y for all q ∈ U_b.

   More strongly, the refusal holds for every model within d < δ of C_a, or of C_b, so it also binds any future defender assigned there.
7. **α-certificate.** For any field u and any bounded q ≥ q₀ > 0:
   - the w-increments of the two centre refusals are d and −d pointwise;
   - so α = (1, 1) shows that no common q makes both ∫ q·d < 0 and ∫ q·(−d) < 0;
   - by Prop A″ (REFEREE_round53), no Λ_q has both refusals open.
8. **Centre verdicts.**
   - R₁(r) ⊇ {w, v′} and v ∉ R₁(r);
   - R₁(r⁻¹) ⊇ {w, v} and v′ ∉ R₁(r⁻¹).

   So C_a ≻_v X, C_b ≻_{v′} Y, and the pair is incomparable at w.

*Proof.*
- **1.** R₁ is a function of the record. The empty record is not in 𝒰, because d(∅, r) = μ(F) > δ.
- **Robust mixing.** Let ρ ∈ B_δ(r). It agrees with r off a set E with μ(E) < δ. On F_w⁺ ∖ E and on F_w⁻ ∖ E, which are both non-null, its new side is strictly w-better and strictly w-worse respectively. The same holds on B_δ(r⁻¹), with the roles exchanged. So **no record in 𝒰 is weakly w-one-sided.**
- **2.** Off 𝒰, and at worlds other than w, R₁ = R₀^ψ, which satisfies strict (G) by Lemma 1(iv). On 𝒰 at w, strict (G) imposes nothing, because those records are mixed at w. Adding refusals never removes a (G)-refusal.
- **3.** Take a triangle accepted under R₁ at a world k.
  - If k ≠ w, R₁ agrees with R₀^ψ at k, and Theorem R(TC) gives the reverses.
  - If k = w, each link is accepted by R₀^ψ and lies outside 𝒰. Theorem R(TC) gives each reverse accepted by R₀^ψ. Each reverse is the inverse of a link outside 𝒰, so it lies outside 𝒰, because 𝒰 is inverse-closed. So it is still accepted.

  This is PP63 Lemma 3.1(a), with base R₀^ψ.
- **4.** Off 𝒰 this is Theorem R for R₀^ψ.
  - If ρ ∈ B_δ(r), then V^ψ_v(ρ) > V^ψ_v(r) − κ ≥ 0 by continuity in d. So V^ψ(ρ) ≠ 0, v ∉ R₀^ψ(ρ), and v ≠ w. Hence ρ is accepted at v.
  - If ρ ∈ B_δ(r⁻¹), then V^ψ_{v′}(ρ) > −V^ψ_{v′}(r) − κ ≥ 0, so ρ is accepted at v′.

  This holds for every record in 𝒰, not only for those whose old side is a member. That is PP63 Lemma 3.1(b) with full slack.
- **5.** R₁ refuses everything R₀^ψ refuses, and Theorem R gives protection for R₀^ψ.
- **6.** μ(C_p ≠ C_a) is continuous in p, by continuity in measure of p ↦ C_p (PP49 Lemma 1.1), so U_a is open. Moreover d(rec(Z, X), r) ≤ μ(Z ≠ C_a) for every model Z, because X is fixed (PP63 Lemma 1.1(b)). So rec(C_p, X) ∈ B_δ(r), and w ∈ R₁. The same argument applies at b, since rec(C_b, Y) = r⁻¹.
- **7.** rec(C_b, Y) is the inverse of r. Its w-increment is −d pointwise, and the rest is the alternative theorem.
- **8.** By (Sgn), V^ψ_{v′}(r) < 0 and V^ψ_v(r) > 0. So R₀^ψ refuses r at v′ and refuses r⁻¹ at v, and accepts r at v and r⁻¹ at v′. Surgery adds w to both. ∎

**Corollary 2.1 (Theorem L variant; PROVED).** Replace R₀^ψ by Λ^ψ: PP56's lexicographic relation with first level ψ and box localisations as later levels. Theorem L holds for ψ, since its proof uses only strict guiding, (U2)-balance and additivity. Λ^ψ is a total preorder at each world, so it satisfies (TC).

On 𝒰, the level-0 coordinate V^ψ_v (or V^ψ_{v′}) is strictly positive, so Λ^ψ accepts there. Steps 1–8 go through verbatim. The resulting relation has no ties anywhere, and incomparability only at w on 𝒰.

**Pure-shift germs and splits (PROVED).** Let a_t := a∘(1 + te_w) and b_t := b∘(1 + te_w), for small t. Both lie in U_a and U_b.
- **Germ out of a.** V^ψ(rec(C_{a_t}, X)) = V^ψ(r) + Γ^ψ(a, a_t), and Γ^ψ → 0. So the defence of C_{a_t} against X comes from v.
  - Its u¹-value at v is V_v(r) + Γ_v(a, a_t).
  - For a balanced F this is Γ_v(a, a_t) < 0: exactly at a = u (PP62 Lemma 1.3(b)); under (H_Γ) elsewhere.
  - So this is PP62 Cor E.2(i)'s u¹-unfavourable acceptance. It is made ψ-favourable by φ_F.
- **Germ out of b.** C_{b_t} defends Y at v′, where it is again u¹-unfavourable.
- **Lemma S splits.** For an accepted shifted record and a split Z, the two split links have ψ-values at v summing to −V^ψ_v < 0. So R₀^ψ refuses one of them, which is the u¹-favourable link PP63 §6.3 says must be refused. No further acceptance is created, so the cascade stops. At w every record of 𝒰 is refused in both directions, so no accepted triangle at w passes through 𝒰.

**Does a = u or b = u matter?** No. Nothing in Theorem 2 uses the position of a or b. T = C_u's protection is clause 5. The only u-specific input is the exactness of "u¹-unfavourable" in the germ remark: Lemma 1.3(b) is PROVED at u and is only NUMERICS elsewhere. The construction does not need that remark.

---

## 3. What the test does reject

**Prop 3 (world-symmetric endorsement fails at w = m; PROVED).** Let F be u¹-balanced, so that it lies on odd-world-m points (PP62 Cor 1.2), and take w = m. Let f be any field with (U1)–(U2) whose h/S increment f(g, S) − f(g, h) is a multiple of ε_m at a.e. g ∈ F. This includes f = q·u¹ for every bounded q ≥ q₀ > 0.

Then no allocation satisfies all of the following:
- defence of every C_p (p near a) against X and of every C_q (q near b) against Y;
- the test's two reservations at m;
- **f-endorsement** at the worlds ≠ m of the acceptances of rec(C_p, X) and rec(C_q, Y), for p near a and q near b;
- when F is f-balanced (the case c = 0 below), also (H_Γ) for f at a.

*Proof.*
- V^f(r) = c·ε_m for some scalar c, so its two non-m coordinates are equal, to c.
- If c > 0, endorsement forbids accepting r⁻¹ at either non-m world, and m is refused. So C_b is undefended.
- If c < 0, C_a is undefended in the same way.
- If c = 0, F is f-balanced, and PP62 Theorem E (with Ψ = f) gives the contradiction. Its openness step is the reservation at a, and its refusing world is w = m, so neither direct (C) nor a closed section is needed. Theorem E is unconditional for f = u¹ at a = u. ∎

So **a common reweighting cannot serve as the base at w = m**, and the world-asymmetric φ_F is exactly what is needed. For w ≠ m a common q suffices: the non-w coordinates of c·ε_m are −2c and c, which have opposite signs once c ≠ 0 (CHECKED, §4). For u¹ itself every w fails, by Theorem E (CHECKED as a control).

**Lemma T (no robust two-sided acceptance at one world; PROVED, axiom-level, using strict (G) and (TC) only).** Suppose X′ ⪯_k Y′ is accepted, and E is a non-null subset of {Y′ strictly k-better than X′} ∩ supp rec(X′, Y′). Then

  Y′ ⪯_k X′[E ↦ Y′] is refused.

The record of that comparison is rec(X′, Y′)⁻¹ restricted off E, which lies within d = μ(E) of rec(X′, Y′)⁻¹. Hence **no world accepts both a record ρ that is mixed at k and every record in a d-ball around ρ⁻¹.**

*Proof.* Put Z := X′[E ↦ Y′]. Then Z is pointwise weakly k-better than X′, strictly on E. So strict (G) accepts Z ⪯_k X′ and refuses X′ ⪯_k Z. If Y′ ⪯_k Z were also accepted, the cycle X′ → Y′ → Z → X′ would be accepted at k. (TC) would then demand X′ ⪯_k Z. Contradiction. ∎

**Consequence.** Suppose a solution defends the a-end ball and the b-end ball each by a single world (a d-robust shape, which is what a reusable extension step wants). Then by Lemma T those two worlds are distinct, so they are v and v′. **Theorem 2's local shape is therefore the only d-robust one.** It cannot be replaced by a tie at a single non-w world.

---

## 4. Exact check (CHECKED, `PP66_py/two_nbhd66.py` → `two_nbhd66.out`, ALL PASS, about 105 s)

**The instance.** Worlds are indexed 0–2. Take m = 0, max world p = 1 and min world n = 2 of log(b/a); this is the u → B pattern, re-indexed. The twelve atoms take the values {h, S}, and their integer masses equal their |g|-weights:
- **F:** Wr = {m} pieces of masses 4 and 6, and Cor = {m} pieces of masses 5 and 5. Here a answers and b is silent, so F is u¹-balanced.
- **Two further D_ab atoms:** a Cor = {p} atom (b answers) and a Cor = {n} atom (b silent). These make X ≠ C_b.
- **The two shift layers** of a_t and b_t toward e_w, three unit atoms each, with PP62 Lemma 1.3's composition. One layer atom lies in D_ab, as is generic by PP63 Prop 2.1.

Models: all 4,096 assignments. Members: C_a, C_{a_t}, C_b and C_{b_t}. δ = 3.5, which exceeds each layer's mass, so the shifted records lie in 𝒰.

**What is checked exhaustively:**
- (U1) and (U2) for each field;
- reflexivity, and strict (G) on all 16.8M ordered pairs at every world;
- (TC) on all 6.9·10¹⁰ ordered triples at every world, by one integer matrix product per world;
- defence and protection of the four members against all models;
- the four reservations;
- α = (1, 1).

(IB) holds by construction (the verdict is a function of the record) and was re-verified on 2·10⁵ random pairs.

| Run | Outcome |
|---|---|
| ψ base + surgery, w = 0 (= m), 1, 2 | **all clauses hold**. Centre verdicts R(r) = {w, v′} and R(r⁻¹) = {w, v}, as Theorem 2.8 states. The u¹-value of rec(C_{a_t}, X) is ∈ O_w; it is accepted at v (Cor E.2(i) realised). |
| common q (3 on one Wr-piece), w = 1, 2 (≠ m) | all clauses hold |
| Control 1: u¹ base + surgery, every w | C_{a_t} undefended against X and C_{b_t} against Y (Theorem E) |
| Control 2: common q base, w = m | C_b undefended against Y (Prop 3) |
| Control 3: ψ base without surgery | the w-refusals are absent (additive base: no same-world inverse refusals) |

**A finite-margin note.** With q = 2 the q-imbalance (4) was smaller than the record vector can move inside a ball of radius 3.5 through the mass-2 atoms. Defence then failed at w = 2. That is the finite form of the condition 4K_ψσ√δ < κ. The theorem chooses δ after κ, and q = 3 restores the margin.

---

## 5. Reading for the constructor and the adversary

1. **The test does not reject this shape, so it is weaker than intended.** It fixes the swap before the relation is chosen. Then a perturbation of the field supported on F, plus one inverse-closed ball surgery, always passes. This is Theorem C's lesson (PP61 Cor C.5, PP63 Prop 4.6) seen at the level of relations, not weights.
2. **What R₁ does not do.** R₁ still has R₀^ψ's section failures at every ψ-null record out of an interior member (PP62 Theorem P, which holds verbatim for ψ). Swaps disjoint from F that are u¹-balanced are also ψ-balanced. So the shape is a local patch, one swap at a time. Theorem 2 makes no claim about sections elsewhere.
3. **The reusable mechanism.** For a swap record r that is not ψ-balanced, choose w so that the two other coordinates of V^ψ(r) have strictly opposite signs. That is always possible when V^ψ(r) ≠ 0 and Σ_i V^ψ_i = 0, and it is the condition for adding the reservation at w with no loss of defence. Then refuse a ball around {r, r⁻¹} at w.
   - **Balls at one world combine.** Lemma 3.1 allows any inverse-closed, section-open union at a world, and each ball keeps its own slack at v or v′.
   - **Balls at different worlds may overlap.** A record lying in balls refused at two different worlds needs the third world to accept it. With ψ-margins this is a finite, checkable condition, but I have not analysed it (OPEN).
   - **Several perturbations φ_F can be added,** provided their sum stays within the |g|/2 rank-gap bound pointwise.

   **The first binding constraint is ψ-balanced swaps.** On those, V^ψ(r) = 0 and Theorem E (for ψ) bites.
4. **A sharper test (suggestion).** Run the two-neighbourhood test on a swap balanced for the proposal's own field, chosen after the proposal. Equivalently, require the proposal to state its field ψ, and then test a ψ-balanced F.
5. **CONJECTURE.** Every field with (U1)–(U2) on a genuinely 2-D N has a ψ-balanced non-conic member swap between interior members. If so, the shape of Theorem 2 cannot be globalised by changing the field, and a global rule must use acceptances not endorsed by any single field on some balanced swaps. Cor E.2 and Prop 4.6 already point that way.

   Evidence for the conjecture: on D_ab the h/S increments of any admissible ψ lie in the zero-sum plane, and a balanced F exists unless they all lie in an open half-plane. Theorem J and Prop 5.3 (PP63) show that 2-D families make such half-plane configurations hard to sustain. This is not proved.

---

## 6. Exactly what is used

- **Results imported within their stated hypotheses:**
  - (2V) on 𝒮₀ ⊇ N, and PP56's u¹ with (U1)–(U2), with the explicit rank gaps of PP56 §4.1;
  - continuity in measure of p ↦ C_p (PP49 Lemma 1.1), and PP63 Lemma 1.1;
  - PP62 Theorem R's proof structure;
  - PP63 Lemma 3.1, which I re-proved in-line in steps 2–4;
  - μ Gaussian, so that σ < ∞.
- **Test-specific hypotheses:** (Mix_w) and (Sgn). Both are automatic for u¹-balanced F, for every w.
- **Not used:** completeness, (LA), closed sections anywhere except the two reservations, (H_Γ), any lexicographic level beyond Cor 2.1's optional variant, and properness of ℓ^m.
  - Non-conicity of F is not needed. It only makes X and Y incoherent, and direct (C) holds for every rival anyway.
  - Prop 3 additionally uses PP62 Theorem E (with (H_Γ) for f when c = 0 and f ≠ u¹ or a ≠ u).
