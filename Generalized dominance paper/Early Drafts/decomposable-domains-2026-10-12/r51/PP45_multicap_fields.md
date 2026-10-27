# PP45. Compatible fields on the multicap family: the combined cut cannot sit beside T

23 October 2026. Task PP45 of Brief 51. One reader (me); not refereed.

**Labels.** PROVED: complete argument here, or a cited result that has been refereed (named). CHECKED: exact rational computation in `PP45_py/` (each script ends ALL PASS). NUMERICS: Gaussian Monte Carlo; no proof depends on it. CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF51; AUDIT_round51, AUDIT_multicap, AUDIT_round51_answers (binding); PP42 (design TWG, Lemma 3.0, Thms 3.1, 3.2, Lemma 4.1, Thm 4.3, Prop 5.2); PP43 Lemma 3.3 (contradiction shell); PP38 Thm 3.1(ii) (separation); AUDIT_completion; and the coordinator's relay of REFEREE_round50: CG2 necessity **without** the agreement-region hypothesis (under (R) and (R0)), Thm R1 (for two-valued families with (BR), the closed interval-triangle test is exactly (TC) under strict gates), Lemma S (closed sections for a compact gated family, conditions (S1)–(S4)), and the pointwise bound R_*. I add no axioms. Extra hypotheses are named where they enter.

---

## 0. Verdict

**Obstruction, at the first checkpoint. It comes from the gate-union architecture. It does not come from the strength of the compatibility test, and nothing here bears on the axioms.**

1. **The pair (T, combined cut) fails for every choice of fields and supporting weights (Thm 3.1; PROVED, CHECKED).** Let AB = C_(a,b,0) with a, b > 0. Suppose T and AB are both gated members of a gate union, T is a.e.-uniquely Bayes for its own field, and AB is universally competitive. Then at some world the CG2 sandwich for (T, AB) is empty. By the referee's form of PP42 Thm 3.1(c), (TC) fails at that world. The forbidden configuration is real: an accepted triangle whose missing reverse is a strict guidance reversal (§3.2; NUMERICS shows the records for one concrete field pair).
   - Triples play no role. CG3, the interval-triangle sums and the sufficient local-witness theorem are never used. The failure is in the pair condition, which is **necessary**.
   - The mechanism is a one-line inequality (Lemma 2.1). If CG2 holds at all three worlds, the CG2 constants, combined with the supporting weights, define a vector D ∈ R³. For both models to be own-Bayes at a disagreement point, some world where the cut answer is wrong must have a larger entry of D than some world where it is right. On the two corner bands of AB, the six answer families (Lemma 1.1) demand that **no** world carry the largest entry.
2. **What survives in the cube (Cor 3.2; PROVED, CHECKED).** Two members C_s, C_t can both be gated only if, going from s to t, at most one cut grows and at most one shrinks. With T present, the compatible members are exactly the **tripod**: single cuts at one vertex, {t e_i}. The box contains no compatible axis rectangle and no compatible C¹ surface. More generally, **no refinement of T whose credal set misses two vertices of M can be gated beside T** (Cor 3.3).
3. **So the combined cut cannot defend anything.** This includes the two-corner rival X = T[G_i ↦ C_s, G_j ↦ C_t] (§4). Any defender in a system containing T must pass the same pair test.
4. **The nearby result that is reachable: the tripod (Thm 5.1; PROVED, CHECKED).** One explicit formula gives jointly designed fields for T and all single caps at all three vertices, valid for every cut size t ∈ (0, δ] and every δ < ε/3. It delivers:
   - (i) unique Bayes with an explicit pointwise margin;
   - (ii) strict CG2 for every pair, with open intervals, and the strict triangle test for every triple;
   - (iii) field differences continuous in t with an integrable envelope, so Lemma S gives closed sections;
   - (iv) universal competitiveness, undominatedness and no all-world ties for every member;
   - (vi) an explicit continuous selection from a 2-D neighbourhood of T's index onto the tripod.

   This settles PP42 Prop 4.4(b) positively: caps at different vertices can be registered together once their fields change on each other's bands.

   **Two caveats.**
   - The construction is **witnessed**: one global set of constants works. By PP42 Thm 2.1 it is therefore a single-field realisation of the tripod at the bounded level, which is the route the ground rules treat as excluded (§6).
   - It does **not** deliver (v). NUMERICS finds most repair-class rivals undominated by tripod members, the two-corner rival included (§4).
5. **Pointwise Bayes estimate for PP42 Thm 4.3(a) (Prop 5.6; PROVED, CHECKED).** σ is the strict u-optimum on H_s whenever b + 3η + 3θ(s) < 1. The constant is exactly 3, from two monotonicity facts on the B-families. This also avoids the −σ ratio that drives the referee's R_* ≈ 8.45.
6. **Where to go next (§6).**
   - The type test does **not** block the edge: B_12(t) passes it for t ∈ {0.5, …, 2} (NUMERICS).
   - The test does pass single-vertex cuts of arbitrary **tilt**, which form a genuinely 2-dimensional family at each vertex (CHECKED on 187 sampled pairs).
   - I propose tilted single-vertex cuts as the replacement for combined cuts.

| Item | Result | Label |
|---|---|---|
| Strips carry exactly the three families; union-lemma advice | Lemma 1.1 | PROVED; CHECKED |
| Pair type lemma (any fields, any weights) | Lemma 2.1, Lemma 2.2 | PROVED |
| Universal competitiveness forces own weak Bayes; ungated non-perfect models fail | Lemma 2.3 | PROVED |
| (T, combined cut): empty CG2 sandwich ⇒ (TC) fails | Thm 3.1 | PROVED; CHECKED (200 random own-Bayes field draws per ε, all fail; controls pass) |
| Cube: compatible ⇔ ≤ 1 up and ≤ 1 down; with T only the tripod; no rectangle or C¹ surface | Cor 3.2 | PROVED; CHECKED (702 grid pairs) |
| Refinements missing two vertices are incompatible with T | Cor 3.3 | PROVED; CHECKED (300 random refinements) |
| Explicit forbidden triangle for one field pair | §3.2 | NUMERICS |
| Who can possibly dominate the two-corner rival in the tripod | Prop 4.1 | PROVED |
| Tripod fields: (i)–(iv), (vi) on the whole range t ∈ (0, δ], δ < ε/3 | Thm 5.1, Lemmas 5.2–5.4 | PROVED; CHECKED (73,124 exact checks) |
| PP42 Thm 4.3(a) pointwise | Prop 5.6 | PROVED; CHECKED (9,000 exact points) |
| Repair-class coverage by the tripod design | §4 | NUMERICS: mostly not covered |
| Edge models and tilted cuts pass the type test | §6 | NUMERICS / CHECKED samples; CONJECTURE in general |

---

## 1. Setting, bands and families

Brief 51's setting: three worlds; Gaussian μ; ranks 0 < 1 < 2 < 3 for correct, silent, wrong and contradictory advice; T = D_M with M = c·1 + εΔ, vertices m_i = c·1 + εe_i, c = (1−ε)/3, centre u. Take 0 < δ < ε/3 and K_s, C_s as in the brief. Write σ(g) := sign(Σg), the answer of every model whose credal set contains u.

**Bands and thresholds.** H_i := H_i(δ) is the *i-th corner band*. A problem g ∈ Sil(T) lies on band i when g's plane cuts off a corner of M at m_i alone. Let λ_j, λ_k ∈ (0, 1) be the fractions along the edges m_i → m_j and m_i → m_k at which the plane crosses. Its **threshold** is τ(g) := ε·max(λ_j, λ_k). Then the single cap K_i(t) answers σ at g iff τ(g) < t, and, by the union lemma, C_s(g) = σ iff τ(g) < s_i (up to null sets).

**Pattern.** At a band point, W(g) is the set of worlds where σ is wrong. The *families* on band i (j, k the other two worlds) are:
- A_i: W = {i} (the majority answer on M_i);
- B_j: W = {i, k}, so σ is right only at j (the minority answer on M_j);
- B_k: W = {i, j}.

**Lemma 1.1 (strips; PROVED; CHECKED `types_exact.out` (a), 50,393 exact checks).** For every 0 ≤ s < t ≤ δ and every i:
- on the strip H_i(t) ∖ H_i(s), σ is i-wrong, and the pattern is A_i, B_j or B_k;
- each of the three families meets the strip in a non-null set.

*Proof.* Normalise Σg = 1 and put κ₀ := c/ε. A plane crossing the two edges at λ_j, λ_k is given by

  g_i = −κ₀ − h,  g_j = −κ₀ + h(1/λ_j − 1),  g_k = −κ₀ + h(1/λ_k − 1),  h = (1 + 3κ₀)/(1/λ_j + 1/λ_k − 3).

To check this, note that m_i·g = −εh < 0, and the edge crossings are at λ_j and λ_k.
1. **σ is i-wrong.** g_i < 0 < Σg.
2. **The sign of g_j.** g_j > 0 iff (1 + 2κ₀)/λ_j − 1 > κ₀/λ_k, and symmetrically for g_k.
3. **The three families.** Fix τ ∈ (s, t), put λ_j := τ/ε and λ_k := ρτ/ε with ρ ∈ (0, 1].
   - At ρ = 1 both g_j and g_k are positive: family A_i.
   - For small ρ, g_j < 0 < g_k: family B_k.
   - Exchanging the roles of j and k gives B_j.

   The conditions are open, so each family contains an open set of (λ_j, λ_k), hence a non-null cone.
4. **No other pattern.** g_i < 0 always, and Σg > 0 excludes the pattern {1, 2, 3}. ∎

---

## 2. The pair type lemma

For gated N, M and g ∈ D_NM := {N ≠ M}, write e^X_w(g) := ℓ^X_w(g, M(g)) − ℓ^X_w(g, N(g)) for X = N, M (PP42's f^N, f^M). Let W(g) be the worlds where M(g) has the higher rank and R(g) the others. Both fields are strictly guiding, so e^X_w > 0 on W(g) and < 0 on R(g).

CG2 at w, in the exact form of REFEREE_round50 (the sandwich), says there is κ_w ∈ [0, ∞] with κ_w|e^N_w| ≤ |e^M_w| on {w ∈ W} and |e^M_w| ≤ κ_w|e^N_w| on {w ∈ R}, a.e. on D_NM. With positive constants, κ_w = c^N_w/c^M_w.

**Lemma 2.1 (type lemma; PROVED).** Assume:
- CG2 holds at all three worlds;
- N and M have interior supporting weights λ^N, λ^M;
- at a.e. g ∈ D_NM, N strictly prefers N(g) to M(g) at λ^N under ℓ^N, and M weakly prefers M(g) to N(g) at λ^M under ℓ^M.

Put D_w := −log(κ_w λ^M_w/λ^N_w) ∈ [−∞, ∞]. Then for a.e. g ∈ D_NM,

  max_{w ∈ W(g)} D_w > min_{r ∈ R(g)} D_r.   (★)

*Proof.* Fix such a g. Put a_w := λ^N_w|e^N_w| and b_w := λ^M_w|e^M_w|.
1. **What the hypotheses say.** N strict gives Σ_W a − Σ_R a > 0. M weak gives Σ_W b − Σ_R b ≤ 0. CG2 gives b_w ≥ e^{−D_w} a_w on W and b_r ≤ e^{−D_r} a_r on R.
2. **D is finite where it matters.** Because the weights are interior and a, b > 0, D_w > −∞ for w ∈ W and D_r < ∞ for r ∈ R.
3. **Contradiction.** Suppose max_W D ≤ min_R D, and take a finite m between them. Then

     Σ_W b − Σ_R b ≥ e^{−m}(Σ_W a − Σ_R a) > 0.

   This contradicts M's weak preference. ∎

*Remarks.*
- Positive rescaling of a world's whole field, and the choice of λ, only shift D. That is the normalisation freedom the audit allows, and it is used up in D.
- Lemma 2.1 uses nothing about the *form* of the fields. It covers any additive strictly guiding fields, including ones that change on bands where the model is silent.

**Lemma 2.2 (order form; PROVED).** (★) is a finite set of strict inequalities, so its solution set is open, and only the order of D matters. For a refinement point, where M answers σ and N = T is silent:
- pattern A_w says "w is not at the bottom";
- pattern B_r (σ right only at r) says "r is not at the top".

When N answers σ and M is silent, the two readings swap: A_w says "w is not at the top", and B_r says "r is not at the bottom".

**Lemma 2.3 (own Bayes is forced; PROVED).** In a gate union (guidance, or a realiser's gate under (R) or (R0)), let N be competitive on supp p against every measurable rival.
- (a) If N carries a gate, it is weakly λ-Bayes for its own field at some λ ∈ Δ_supp p.
- (b) If N carries no gate, it is perfect at some world of supp p.

*Proof.*
- (a) If not, PP38 Thm 3.1(ii) (Lyapunov and separation; the direction "competitive ⇒ Bayes" that the audit confirmed for PP42 Thm 2.1) gives a bounded X with Φ^N_w(N → X) < −η₀ at every w ∈ supp p. Add a thin shell on which X says contradiction, with envelope below η₀/2 (PP43 Lemma 3.3).
  - Any coherent model ≠ N differs from N on a non-null cone, which meets the shell. So only N realises the old side.
  - N's gate value is negative at every w ∈ supp p.
  - The record is not a weak w-worsening at any such w, since then Φ^N_w ≥ 0.

  So N is refused at every world of its support.
- (b) Make X equal N except for the shell and, at each w ∈ supp p, a small set on which X is w-correct and N is not. Only N realises the record, N has no gate, and guidance refuses at every w. ∎

Every multicap member answers like T on Ans(T). T gives, on M_w, the minority answer, which is right only at w. With λ_w = 0 that answer is strictly worse than silence, so **every gated multicap member has an interior supporting weight**. Boundary weights, which the audit allows, cannot occur here.

---

## 3. The obstruction

### 3.1 The theorem

**Theorem 3.1 (PROVED; CHECKED `pair_obstruction_exact.out`).** Let 0 < a, b ≤ δ and AB := C_(a,b,0). Consider any gate union, under (R) or (R0), in which:
- T and AB are gated members;
- T is a.e.-uniquely λ^T-Bayes for ℓ^T;
- AB is universally competitive on its support.

Then for every choice of the two fields and weights, the CG2 sandwich for (T, AB) fails at some world. Hence (TC) fails at that world.

*Proof.*
1. **Own Bayes.** By Lemma 2.3(a) and the remark after it, AB is weakly own-Bayes at an interior λ^AB.
2. **Disagreement set.** D_{T,AB} = H_1(a) ⊔ H_2(b), where AB answers σ and T is silent.
3. **Apply the type lemma.** Suppose CG2 held at all three worlds. Apply Lemma 2.1 with N = T and M = AB. By Lemma 1.1, all six families occur on non-null sets. Among them are B_2 and B_3 on band 1, and B_1 on band 2.
4. **Contradiction.** By Lemma 2.2, worlds 1, 2 and 3 are all excluded from the top of D. That is impossible.
5. **Conclusion.** So CG2 fails at some world w. By PP42 Thm 3.1(c), in the referee's form without the agreement-region hypothesis, valid under (R) and (R0), (TC) fails at w. ∎

**CHECKED.** At ε ∈ {1/10, 3/10}, exact points of all six families are taken. Random positive magnitudes are drawn for each world and point (that is, arbitrary fields), together with random interior weights, conditioned on T strictly and AB weakly own-Bayes. All 200 draws per ε have an empty sandwich at some world. Controls: constructive fields with all three sandwiches non-empty exist for (T, A) and for (A, B), as Cor 3.2 predicts.

### 3.2 The forbidden configuration

The brief asks whether the offending records actually form a forbidden configuration. They do, and for every fields:
1. **The bounded set.** At the failing world w, take a bounded D ⊆ H_1(a) ∪ H_2(b) with ∫_D e^T_w > 0 > ∫_D e^AB_w (Lyapunov). Take a bounded F ⊆ Sil(T) off the bands.
2. **The two models.** Put X := T[D ↦ AB] and Y := T[F ↦ w-correct].
3. **The three links.**
   - T ⪯_w X: T's gate accepts.
   - X ⪯_w Y: AB realises the old side (AB = T on F) and rates it −∫_D e^AB_w − α^AB_w(F) > 0 for small F.
   - Y ⪯_w T: guidance accepts.
4. **The missing reverse.** (TC) then needs T ⪯_w Y. That is a strict w-improvement, which every gate rates negatively and strict (G) refuses.

**NUMERICS** (`forbidden_triangle_mc.out`). Setting: ε = 0.3, a = b = ε/8, T with ℓ^T, AB with PP42's humble field on both cuts (b = 0.1, η = 0.02), w = 1. Results:
- Φ^T_1(D: T → AB) = +5.06·10⁻³;
- AB's gate value of X → Y is +3.56·10⁻³.

The configuration is present.

### 3.3 Consequences in the cube and beyond

**Corollary 3.2 (PROVED; CHECKED `types_exact.out` (b), 702 grid pairs per ε, plus the checkpoint pairs).** Let C_s and C_t be gated, each a.e.-uniquely own-Bayes. Lemma 2.1 can hold only if, from s to t, **at most one coordinate goes up and at most one goes down**. Consequently:
- **(a) The four-model checkpoint.** (T, A), (T, B), (A, B), (A, AB) and (B, AB) pass. (T, AB) fails.
- **(b) With T, only the tripod.** If T is gated, every compatible member has at most one non-zero cut: it lies in the **tripod** {t e_i : 0 ≤ t ≤ δ, i = 1, 2, 3}.
- **(c) No 2-D compatible family.** No compatible family contains an axis rectangle {s, s + αe_i, s + βe_j, s + αe_i + βe_j}, and none contains a C¹ immersed surface.

*Proof.* There are two cases.
- **Two ups, i and j.** On the strips of bands i and j, C_t answers σ and C_s is silent. Band i supplies B_j and B_k ("not top"), and band j supplies B_i. No world can be on top. Two downs is the same case with s and t exchanged.
- **One up i, one down j.** The constraints are "top = i" (band i) and "bottom = j" (band j, with the reversed readings). These are compatible.

Then:
- (b) is the case s = 0.
- (c), the rectangle: its diagonal pair has two ups.
- (c), the surface: every tangent vector must have a zero coordinate, since a vector with three non-zero coordinates has two of one sign. A 2-dimensional subspace inside the union of the coordinate planes is one of them, and {v_i = 0} contains a vector with two positive coordinates. Along that direction, nearby pairs have two ups. ∎

**Corollary 3.3 (PROVED; CHECKED `types_exact.out` (c), 300 random tilted refinements).** Let K ⊆ M be compact and convex and miss two vertices m_i, m_j of M. Then D_K cannot be gated beside T, with T a.e.-uniquely own-Bayes and D_K universally competitive.

*Proof.* K is closed and m_i ∉ K. So every plane cutting off a small enough corner at m_i, of any orientation, misses K. D_K answers σ there and T is silent. As the depth tends to 0 at a fixed edge ratio, the pattern is fixed by the ratio (Lemma 1.1, step 2), so all three families at m_i occur. The same holds at m_j. Then B_1, B_2 and B_3 all occur, and Lemma 2.2 leaves no top. ∎

Refinements missing exactly one vertex pass the test (necessary condition only).

### 3.4 Classification

| Used | Not used |
|---|---|
| Additive fields, one per gated model; acceptance = guidance or some realiser's gate (union), under (R) or (R0) | CG3; the triple interval sums; PP42's sufficient local-witness theorem |
| (TC), strict (G), reflexivity (through CG2 necessity) | (S), sections, (LA), (C), any coverage obligation |
| T a.e.-uniquely own-Bayes (requirement (i); Thm 3.2(b) needs it for undominatedness) | any special form of the fields; any restriction on bands where a model is silent |
| AB universally competitive (forces own weak Bayes, Lemma 2.3) | any choice of supporting weights (absorbed into D) |

So the obstruction belongs to the **gate-union architecture**, together with T's uniqueness. It is not a failure of the stronger sufficient compatibility test: CG2 is necessary, and Thm R1 makes the whole interval test exact here. No conclusion about the axioms follows.

Two loopholes stay open, and I flag them without pursuing them:
- **T not unique.** If T merely *ties* σ and silence on all six families, (★) becomes non-strict and D = 0 is admissible. T is then not a.e.-unique, and requirement (i) fails.
- **Other architectures.** A lexicographic or non-additive gate, or an aggregation other than the union, falls outside Lemma 2.1. Any such branch needs its own proofs (audit item 3).

---

## 4. Consequences for the repair class

**The combined cut cannot be registered beside T** (Thm 3.1), so it cannot defend anything. Any defender of any rival in a system containing T must pass Lemma 2.2 against T. That excludes every refinement missing two vertices (Cor 3.3).

**Proposition 4.1 (two-corner rival in the tripod; PROVED).** Let X = T[G_i ↦ σ, G_j ↦ σ], with bounded non-null G_i ⊆ H_i ∩ A_i and G_j ⊆ H_j ∩ A_j. On both pieces σ is right at k, at j on G_i, and at i on G_j. Then none of the following is accepted at all three worlds by any route:
- T, which is refused at k, because T → X is a pure k-improvement;
- any cap at k;
- any cap at i whose cut contains G_i, which is refused at i;
- any cap at j whose cut contains G_j.

So a tripod dominator of X, if one exists, is a cap at i or j whose cut does not contain that vertex's piece.

*Proof.*
- **Caps at k.** The record consists of the cap's own σ → S (a k-improvement on band k) plus S → σ on G_i ∪ G_j (k-improvements). It is a pure k-improvement.
- **Caps at i containing G_i.** The record is (H_i(t) ∖ G_i: σ → S) ∪ (G_j: S → σ). Both parts are i-improvements.
- **The verdict.** Every strictly guiding field rates a pure w-improvement negatively, and guidance refuses it. ∎

**NUMERICS (`tripod_repairs_mc.out`; the design of §5, ε = 0.3, 1.5·10⁶ samples, every member tested through every route).** These are dominated:
- a deep A_1-fill of T by cap answers (by one small cap at vertex 1);
- a shallow retreat of C_1(δ) (by C_1(0.975δ)).

These are **not** dominated by any tripod member:
- deep B-family fills;
- fills hugging the arc;
- all four two-corner rivals tested (deep and shallow, two size ratios);
- deep retreats.

**Assessment (CONJECTURE).** The residue is structural. Near a cap C_{i,t} the tripod is 1-dimensional. Small retreats and fills perturb the three world-values in a 3-parameter range of directions. Defenders near C_{i,t} therefore have to come from a 2-parameter family, the dimension of the weight simplex. The type test excludes combined cuts for that role. It allows single-vertex cuts of variable tilt (§6).

---

## 5. The reachable construction: the tripod

### 5.1 The formula

Fix ε ∈ (0, 1), δ ∈ (0, ε/3) and c := 1/4. Put φ(t) := t/(2δ) ∈ [0, 1/2].

**Member points.** Each member has a point in R³:
- μ^T := (1, 1, 1);
- μ^{i,t} := 1 − φ(t)e_i for the cap C_{i,t} := C_{te_i}, t ∈ (0, δ].

**Separating vectors.** At a band point g on band i, with q := 1 − φ(τ(g)) and ζ := φ(τ(g))/2, define n(g) = |g|·n̂, with n̂_i = 1 and:
- A_i: n̂_j = n̂_k = −q/2;
- B_j: n̂_j = −(q + ζ), n̂_k = ζ;
- B_k: n̂_k = −(q + ζ), n̂_j = ζ.

The sign of n_w is + exactly at the worlds where σ is wrong.

**Margins and humility factors.** Let m̂^s(g) := |n̂·μ^s|.
- A member that answers σ at g (a "σ-sayer") gets H^s_w = 1 + c·m̂^s at worlds where σ is wrong and 1 − c·m̂^s where it is right. It is humble.
- A member that is silent at g (an "S-sayer") gets the reverse.

**The fields.** Every member uses ℓ^T off the bands. On the bands, at each world, member s has the σ-versus-silence magnitude m^s_w := |n_w| μ^s_w H^s_w. Its full field is:
- at a σ-wrong world: ℓ(−σ) = 0, ℓ(S) = m, ℓ(σ) = 2m, ℓ(contradiction) = 2m + Λ;
- at a σ-right world: ℓ(σ) = 0, ℓ(S) = m, ℓ(−σ) = m + 2Λ, ℓ(contradiction) = m + 3Λ;
- where Λ := Σ_w m^s_w.

All fields are strictly guiding with envelope 15|g|. Every member's supporting weight is λ = u; positive rescaling of a world's field is absorbed into the constants. The CG2 constants are **global**: c^s_w := 1/μ^s_w.

### 5.2 Bayes, compatibility and regularity

**Lemma 5.2 (pointwise Bayes; PROVED; CHECKED (A1)).** Every member is the a.e.-unique u-Bayes model of its field, with pointwise margin

  |cost(σ) − cost(S)| ≥ (3/8)·|n(g)·μ^s| on the bands.

*Proof.*
1. **Off the bands.** Every member equals T and uses ℓ^T, of which T is the a.e.-unique u-Bayes model.
2. **σ against silence on the bands.** Up to the factor 3, cost(σ) − cost(S) = Σ_w n_w μ_w H_w = n·μ ± c·m̂ Σ_w |n_w|μ_w. The sign is + for σ-sayers and − for S-sayers, and Σ_w |n̂_w| ≤ 5/2. The value is n·μ = −|g|m̂ for σ-sayers and +|g|m̂ for S-sayers.
3. **Which members are σ-sayers.** n̂·μ^{i,t} = φ(τ) − φ(t). This is negative exactly when t > τ, that is, exactly where C_{i,t} answers σ.
4. **The other members are silent with margin.** On band i:
   - T: n̂·μ^T = φ(τ) > 0;
   - caps at j: n̂·μ^{j,t′} = φ(τ) + q·φ(t′)/2 on A_i, φ(τ) + (q + ζ)φ(t′) on B_j, and φ(τ) − ζφ(t′) ≥ (3/4)φ(τ) on B_k;
   - caps at k: symmetric.
5. **The margin.** Hence the margin is ≥ m̂|g|(1 − 5c/2) = (3/8)m̂|g|.
6. **−σ and contradiction.** They are strictly worse: −σ costs at least 2Λ − Λ > 0 more than silence, and contradiction more again. ∎

**Lemma 5.3 (strict CG2 with global constants; PROVED; CHECKED (A2)–(A4)).** Let P be a σ-sayer and Q an S-sayer at g. Write s_PQ(g) := m̂^P + m̂^Q. With c^s = 1/μ^s, the scaled magnitudes are |n_w|H^s_w, and:
- their ratio is ≥ 1 + c·s_PQ at σ-wrong worlds;
- it is ≤ 1/(1 + c·s_PQ) at σ-right worlds.

Moreover, s_PQ is bounded below on D_PQ by a constant depending only on the pair:
- φ(t) − φ(t′) for C_{i,t}, C_{i,t′} with t > t′;
- φ(t) for (C_{i,t}, T);
- (3/4)·min(φ(t), φ(t′)) for C_{i,t}, C_{j,t′}.

Member-to-member magnitude ratios lie in [3/10, 10/3], so (BR) holds.

*Proof.*
1. **The ratio bounds** follow from (1 + ca)/(1 − cb) ≥ 1 + c(a + b) and (1 − ca)/(1 + cb) ≤ 1/(1 + c(a + b)).
2. **The pair bound.** s_PQ = n̂·(μ^Q − μ^P), which is computed in step 4 of Lemma 5.2's proof. For instance, for cross pairs on band i: φ(t) − n̂_jφ(t′) ≥ φ(t) − ζφ(t′) ≥ (3/4)φ(t), since τ < t. ∎

So every pair has an **open** CG2 interval around the global constants, at every world. Every triple then satisfies the strict triangle test, with the three differences of the global constants summing to 0. CG3's three-value clause is vacuous: members take only the values σ and S on the bands and agree off them.

**Lemma 5.4 (regularity; PROVED; CHECKED (A5)).** At each fixed g, every advice-cost difference of C_{i,t} is continuous in t on [0, δ], **including at the switch t = τ(g)**, and is bounded by 15|g|. Here C_{i,0} = T, for each i.

*Proof.* μ^{i,t} and m̂ are continuous in t. At the switch m̂ = 0, so H = 1 from both sides. Dominated convergence then gives L¹-continuity. ∎

### 5.3 The theorem

**Theorem 5.1 (the tripod; PROVED).** Let 𝒯 := {T} ∪ {C_{i,t} : i = 1, 2, 3, 0 < t ≤ δ}, with the fields above, the vertex models V_k carrying no gate, and (R0) at every gate. Then:
- **(i)** Lemma 5.2 holds.
- **(ii)** (TC) holds for all common-context copies. This follows from PP42 Thm 3.1(b) with the strict constants of Lemma 5.3, and is consistent with Thm R1.
- **(iii)** Lemma S applies with Θ = the tripod. The tripod is compact, being three segments glued at T:
  - (S1) holds by the union lemma and continuity of H_i(t) in measure;
  - (S2) holds by Lemma 5.4;
  - (S4) holds because there are no other routes.
- **(iv)** By PP42 Thm 3.2, with the referee's correction that (d) also needs the triple condition, which holds: every member is competitive against **every measurable rival** through its own gate at some world, and is undominated. No member has an all-world tie, dominations are strict, and closure rules II–IV are inert.
- **(vi) Selection.** Write q := p − p_T. On N_r := {‖q‖_∞ < r} ⊆ int Δ, put t_i(p) := min(δ, K₀·(q_i − max_{j≠i} q_j)⁺). Select C_{i,t_i(p)} for the unique i with t_i(p) > 0, and T otherwise.
  - The map is continuous into the tripod: whenever the arg-max changes, every t_i is 0.
  - So (S3) holds, and Lemma S gives closed fixed-rival sections on N_r for every measurable rival, including inheritance at T's index.
  - All selected models are interior-index members, competitive on full support.
  - No directional reading is intended. Any continuous surjection would do.
- **Undominated members.** Every member of 𝒯 is undominated, whether or not the selection reaches it. For K₀r ≥ δ the selection reaches all of them.

*Scope.* Every ε ∈ (0, 1), every δ < ε/3, and the whole range of cut sizes t ∈ (0, δ] at all three vertices. This is the open-range formula the brief asks for, but for the tripod, not the box.

### 5.4 PP42's own cap path, pointwise

**Proposition 5.6 (PROVED; CHECKED `tripod_exact.out` (B), 9,000 exact points at ε ∈ {1/10, 3/10, 1/2}).** Take PP42's humble field on H_s: world v multiplied by b; worlds w ≠ v by 1 + η where σ is wrong and 1 − η where it is right. At every g ∈ H_s, in units of u-weighted cost:

  3[ℓ(σ) − ℓ(S)] ≤ d_v(b − 1 + 3η + 3θ(s)),
  3[ℓ(−σ) − ℓ(S)] ≥ (1 − b − 3η)α_v + 3(1 − η)u·d′ > 0.

So σ is the strict u-optimum whenever b + 3η + 3θ(s) < 1.

*Proof.* The key fact is that on B_j-points of H_v one has g_v < g_k < 0, so s_v > s_k. Since F and G are non-decreasing, β_k ≤ β_v and α_k ≤ α_v.
1. **σ against silence.** Σ_{w≠v}|d_w| equals d_v − 3u·d on A_v and d_v + 2β_k − 3u·d on B_j. Both are ≤ 3d_v − 3u·d. Insert this into 3[ℓ(σ) − ℓ(S)] = b·d_v + Σ_{w≠v} d_w + ηΣ_{w≠v}|d_w|, using Σ_{w≠v} d_w = 3u·d − d_v.
2. **−σ against silence.** Σ_{w≠v}|d′_w| = Σ_{w≠v} d′_w + 2α_k ≤ 3α_v + 3u·d′, and Σ_{w≠v} d′_w = 3u·d′ + α_v. ∎

The checks found max Σ_{w≠v}|d_w|/d_v ≈ 2.98. The ratio Σ_{w≠v}|d′_w|/α_v reaches 8.48, which matches the referee's R_*; the bound above never divides by α_v alone.

---

## 6. What this leaves, and the proposal

1. **The tripod is witnessed.** Its global constants give, by PP42 Prop 3.5(i), a single U ≥ c^s ℓ^s on every member's realised moves, and Thm 2.1 then makes the tripod a single-field realisation at the bounded level. I report it because it settles compatibility in the cube exactly: the only obstruction is the type test. It is not offered as the continuation route.
   - **A non-witnessed strict variant is OPEN.** Adding PP42's world-i chain (a discount b < 1 on each cap's own cut) needs log(1/b) to fit inside the CG2 slack, at world i, of every cap at another vertex. In this design that slack, on the B_k-points of band j for the pair (C_{i,t}, C_{j,s}), is at most c·φ(s), which tends to 0 as s → 0.
   - So small caps at the other vertices squeeze the chain out. Whether this is forced for every design, that is, whether near T strict TWG compatibility across vertices forces a witness, is a **CONJECTURE** worth testing. If true, the gate union would not escape realisation in any multi-vertex family.
2. **Coverage (requirement (v)) is not delivered** (§4). That needs defenders from a 2-parameter family near each cap.
3. **Tilted single-vertex cuts pass the type test** (CHECKED `types_exact.out` (d)). All sampled pairs passed:
   - 60 nested pairs;
   - 67 crossing pairs at one vertex, including strongly different tilts;
   - 60 pairs at different vertices.

   *Heuristic.* For crossing cuts at one vertex, the two exclusive regions split the edge ratio at a single threshold. One region carries {A_i, B_j} and the other {A_i, B_k}, or all three on one side and one family on the other. Each case admits an order.
   - **CONJECTURE.** All single-vertex refinements are pairwise type-compatible with each other and with T.
   - They form a **2-dimensional** family (depth × tilt) at each vertex, which is what the residue of §4 calls for, and what the box could not supply.
4. **The edge is not blocked by the type test** (NUMERICS `edge_types_mc.out`). For B_12(t), t ∈ {0.5, 0.9, 1, 1.1, 2}, the test passes both with an interior weight and with λ_3 = 0. At t = 1 the dangerous patterns "worse only at world 1" or "only at world 2" do not occur, and I checked this analytically on M_1. This is a necessary condition only.

**Proposed next round.**
- Replace the multicap box by the **fan**: T plus tilted single-vertex cuts at all three vertices.
- Design joint fields on it: the §5 formula, with member points now depending on depth and tilt.
- Test whether the fan dominates retreats and arc-hugging fills of caps.
- Settle the witness question of item 1, since it decides whether a TWG continuation can avoid realisation at all.

---

## 7. Status and scripts

| Result | Label |
|---|---|
| Lemma 1.1 | PROVED; CHECKED |
| Lemmas 2.1–2.3 | PROVED |
| Thm 3.1, Cor 3.2, Cor 3.3 | PROVED; CHECKED |
| §3.2 forbidden configuration (concrete) | NUMERICS (general form PROVED) |
| Prop 4.1 | PROVED |
| Thm 5.1, Lemmas 5.2–5.4 | PROVED; CHECKED |
| Prop 5.6 | PROVED; CHECKED |
| Repair-class coverage by the tripod design | NUMERICS: not covered |
| Witness forced near T; fan pairwise compatible; edge compatible | CONJECTURE (samples CHECKED / NUMERICS) |

Scripts are in `r9/PP45_py/`. Run `python3 -I -B <script> > <script>.out` inside the folder.

| Script | Content | Label |
|---|---|---|
| `pp45_lib.py` | exact geometry: bands, thresholds, patterns, corner points, union-lemma advice, order test | library |
| `types_exact.py` | (a) Lemma 1.1, 50,393 checks; (b) Cor 3.2 on 702 grid pairs and the checkpoint; (c) Cor 3.3, 300 refinements; (d) tilted-cut pairs. ALL PASS | CHECKED |
| `pair_obstruction_exact.py` | Thm 3.1 against 2 × 200 random own-Bayes field draws; constructive controls for (T, A), (A, B). ALL PASS | CHECKED |
| `tripod_exact.py` | (A) Thm 5.1 design: Bayes, margin, strict CG2, pair bounds, (BR), switch continuity, 73,124 checks; (B) Prop 5.6. ALL PASS | CHECKED |
| `forbidden_triangle_mc.py` | the three records of §3.2 for one field pair | NUMERICS |
| `tripod_repairs_mc.py` | repair-class rivals against the tripod, every route | NUMERICS |
| `edge_types_mc.py` | type test for T against B_12(t) | NUMERICS |
