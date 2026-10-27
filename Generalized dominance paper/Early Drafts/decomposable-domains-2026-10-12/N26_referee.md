# N26 referee report

14 Oct 2026. I refereed N26_notes.md in full, together with n26py/warmup.py, against:
- LDG v2 §§1–3: preorder rankings, competitiveness, (LA), (S), (C), (I), thm:kkm;
- v3 §1: (G) and (IB) in eq. (independence);
- R2 (Fact 0, Lemma 1, Thm 7), R7 (T7, Lemma 7′, Thm 1′₂), N22, N24 (Prop R1), N9 and N25;
- the writeup's chain for Thm main (lem:signs to prop:T1).

Labels: **PROVED** (full proof here or verified line by line), **CHECKED** (verified, sketch), **CONJECTURE**,
**NUMERICS**. The referee script is n26ref_py/check_n26_1.py. It is independent of warmup.py: it uses the closed-form
Bayes path, the Gaussian-implied law of r, arbitrary and non-regular test models, exact lexicographic comparisons and
exact KKM points.

---

## 0. Verdicts

| Claim | Verdict |
|---|---|
| N26.1 two-world construction: every axiom; the incoherent t₀-minimisers are strictly dominated; target covered; genuine M0 | **CONFIRMED** (remark in §1.2 needs a wording repair; it is not used) |
| N26.2 / Lemma 2.1 (sections = primary sublevel sets) | **CONFIRMED** |
| N26.3 / Lemma 2.2 (multiplier normal form) | **CONFIRMED WITH REPAIR**: the summary sentences garble (c) |
| N26.4 / Lemma 2.3 (splice) | **CONFIRMED** |
| N26.5 / Thm 3.1, Cor 3.2 (no 2-dim faces; jump chords; no fans) | **CONFIRMED WITH REPAIR** (sign pattern is ±σ, not one σ). Valid for the 𝓛₂ˢ **primary** only |
| N26.6 / Thm 3.3, Cor 3.4 (rigidity; vertex-cutting chords) | **CONFIRMED WITH REPAIR** (face = translate of a fixed segment I·d, not [y⁻, y⁻+D]) |
| N26.7 / Thm 4.1, Cor 4.2 (p* ∉ E, dist > 0) | **CONFIRMED** (in 𝓛₂ˢ, ψ = primary) |
| Prop 4.3 | **CONFIRMED** as a conditional. Its single-pattern hypothesis is not automatic, and the proposition is moot in 𝓛₂ˢ |
| §4.3 edge box robust to null E | **CONFIRMED** (CHECKED) |
| Conjecture N26.R | **Correctly stated; identification essentially right but incomplete.** Sharpened by referee Prop R1 and Remarks R2–R3 (§4) |
| "Fans impossible / p* ∉ E for every supporting ψ on M_U" | **Not established, and not claimed by N26's proofs.** N25's "open" stands outside 𝓛₂ˢ (§3.3) |

---

## 1. N26.1: the n = 2 construction (CONFIRMED)

I re-derived every item by hand and re-checked it numerically.

**Data.**
- θ₊ is nondecreasing with range (0.2, 0.4) and a plateau at t₀ = 0.3 on [0.2, 0.3]. θ₋ is strictly increasing from 0.1
  to 0.9, with θ₋(0.625) = t₀. So ρ₁ = 1−θ and ρ₂ = θ lie in (0.1, 0.9), and both are bounded away from 0.
- Bayes rules: on the + side, accept iff θ₊ < p; on the − side, accept −g iff p < θ₋.
- Closed forms:
  - α_B = 0 on [0, 0.2], 2(p−0.2) on (0.2, 0.3], 0.3+2(p−0.3) on (0.3, 0.4), and ½ for p ≥ 0.4;
  - β_B = clip(½ + (p−0.1)/1.6).
- The only interior discontinuity is the jump of α_B at t₀, from 0.2 to 0.3. So E(ψ) = {t₀}, with tie set
  Z = {r ∈ [0.2, 0.3]}.
- Γ is a coordinatewise-nondecreasing continuous path from W₂ = C_{½} to W₁ = C_{3/2}, so u = α + β is a valid
  parameter. Strict monotonicity of U⁺ and V and the equivalences α(u) > r ⇔ u > U⁺(r), β(u) < r ⇔ u < V(r) follow from
  continuity of α, β (checked).
- V(r) = r + α_B(θ₋(r)−). It jumps at β₀ from 0.825 to 0.925, because β(u) = β₀ exactly on the plateau u ∈ [0.825, 0.925].
  NUMERICS reproduce 0.82482 → 0.92518.
- No strictly nested pair occurs in U_L (both coordinates move up), which is consistent with R7 Thm 1′₂.

**Axiom by axiom.**
- **Preorders**: complete preorders (lex pull-backs).
- **(G), strict**: two kinds of advice per problem in the advice range, with distinct world-i ranks, and ρ_i > 0. So a weak improvement gives
  E_i(X) ⊆ E_i(Y). Then either ψ_i(X) < ψ_i(Y), or E_i(X) = E_i(Y) a.e., which forces X = Y. A strict improvement on a
  non-null set gives ψ_i(X) < ψ_i(Y).
- **(IB), v3 form**: (D∩A)∪F versus (E∩A)∪F. Both levels are integrals of pointwise terms, so the difference vector
  (Δψ_i, ΔS_i) is ∫_A(…) and does not depend on F. A lex comparison depends only on the difference.
- **Lemma 1.1 / Cor 1.2** (Lagrangian form; non-improvability at both worlds): verified pointwise, including the
  endpoint cases u = ½, 3/2. The multipliers u and 3 − u are > 0, though the sign is not needed.
  NUMERICS: 0 mismatches over 401 values of u; a fractional-knapsack (exact) gap ≤ 2.3·10⁻¹⁶.
- **U_L = {C_u}**:
  - Every C_u is ψ-Bayes at an interior p. The endpoints are Bayes on (0, 0.1] and [0.9, 1). NUMERICS: 401/401.
  - Weak dominators have equal ψ, and then Cor 1.2 applies.
  - Every other model is dominated, by the weak-Pareto → Bayes argument (Lyapunov). At t₀ the bathtub comparison works
    because ρ₂/ρ₁ = t₀/(1−t₀) is constant on Z and U⁺ = r + β₀ there. Both secondaries then reduce to ±∫ r dν₁ up to
    equal-mass constants.
- **Incoherent t₀-minimisers**: strictly dominated at **both** worlds by the coherent model with the same ψ-profile.
  NUMERICS: 0/300 failures, after discarding trials that coincided with the coherent model.
- **(LA), (C)**: confirmed. A model tied with C_u weakly dominates it, so it equals C_u.
- **(S)**, with u(p) = ½ + p:
  - Competitiveness at interior p is equivalent to undominatedness, since the preorders are complete. At p = 1 and
    p = 0 the selections are the a.e.-unique ψ₁- and ψ₂-minimisers.
  - Sections: ψ₁(C_u) is continuous and strictly decreasing, and ψ₂(C_u) is continuous and strictly increasing. With
    non-improvability, {u : C_u ⪯₁ X} = [u_v, 3/2] and {u : C_u ⪯₂ X} = [½, u′_v].
  - These are closed for **every** X ∈ M_U. Nothing beyond the values (ψ_i(X), S_i(X)) is used, so incoherent and
    non-regular X are included.
  - NUMERICS: 300 arbitrary models, including fractional, random-set, non-regular and coherent-shaped ones. 0 section-
    shape failures, 0 covering failures. Exact KKM points (by bisection) always weakly dominate X, strictly unless
    X = C_p.
- **Index ≠ Bayes weight**: C_{u(0.3)} = C_{0.8} cuts the + side at 0.18, while the 0.3-face cuts in [0.2, 0.3].
  Confirmed.
- **(LF) and target**: T = D_[0.25, 0.625] = C_{0.875} lies on the plateau and is not a one-sided limit, so it is
  intermediate. ∂D_T ∖ 0 consists of the rays (3,−1) and (−3,5), both in the open half-plane U, so a small open N ⊆ U
  works. Confirmed.
- **Genuine M0**: each ψ_i endorses **every** comparison at world i, hence in particular the relevant ones (B coherent
  undominated, X regular). ψ has the BRIEF8 profile:
  - T is ψ-Bayes at the interior weight t₀;
  - there is a coherent Bayes model at every weight;
  - the Bayes model is unique off t₀;
  - E = {t₀} ≠ ∅.
  Nothing is cheap or vacuous.

**Repair to the §1.2 remark** (CHECKED; the remark is not used). "w decreasing in r on each side" is not sufficient. A
world-1 weight wν₁ endorses all relevant world-1 comparisons iff each E₁(C_u) is a cheapest set of its ν₁-mass. That
holds iff w = F(U⁺) on the + side and w = F(V) on the − side, for **one** nonincreasing F. Then F is free on
(0.825, 0.925), the gap of V, and that is the jump at β₀. With F strictly decreasing and the analogous world-2 weight
G(U⁺), G(V) strictly increasing, the t₀-tie condition on Z reads F = G. It holds at most at one point. So the tie is
broken, as claimed.

**Scope.** In n = 2 every target is already covered (v3), so N26.1 is a mechanism demonstration and not a coverage
result. It does show the BRIEF8 anatomy (exceptional tie, intermediate coherent target, strict resolution of ψ-ties)
coexisting with closed competitive choice.

---

## 2. Mechanism lemmas N26.2–N26.4

- **Lemma 2.1: CONFIRMED.** The "iff lsc" direction is fine because levels outside J_i give empty or full sections.
- **Lemma 2.2: CONFIRMED.**
  - (a) g_i is convex and finite on the compact convex joint range (Lyapunov; integrable envelope), with ∂g_i(x) ≠ ∅ on
    int J_i. The supporting-line inequality plus (PB) gives pointwise minimality. The acceptance rule is the sign of
    s_i + λc_i.
  - (b) Two multipliers would force c_i = 0 on X △ X′.
  - (c) The T_i(λ) are disjoint and the measure is finite.

  **Repair.** The summary N26.3 ("a multiplier value … is taken at only countably many levels") and the §2 "Reading"
  ("only countably many levels can carry such a shared multiplier") misstate (c). What is proved is that the **set of
  multiplier values** λ_i(x), over levels x carrying two distinct non-improvable models, is countable. A single value
  can occur at a continuum of levels, wherever g_i is affine. Only the value-countability is used, in Thm 3.1 step 5 and
  Thm 3.3 step 3, so the proofs are unaffected.
- **Lemma 2.3: CONFIRMED.**
  - C and C′ agree off Z_{t₀}.
  - The splice X on A = D ∩ {|g| < R} is t₀-Bayes and pointwise minimises each σ_i + λ_iφ_i.
  - A weak dominator Y has ψ(Y) = ψ(X), by lex plus t₀ ∈ int Δ, and then S_i(Y) ≥ S_i(X). So nothing strictly
    improves X.
  - X △ C = A is bounded and non-null, and coherent models are cones, so X is incoherent. This contradicts R2 Lemma 1
    (LDG thm:kkm + (C)).
- **(T7)** (R2 Thm 7, U_L form) is valid here: it needs only (S) and real levels (R7 §1; R6: (C) not needed).

---

## 3. Three worlds: N26.5–N26.7

### 3.1 Verification (CONFIRMED in the class 𝓛₂ˢ on M_U, ψ := the primary)

- **Fact 3.0**: confirmed. A Pareto- or lex-minimum of the secondaries over the fibre is attained (Lyapunov range). Any
  weak dominator has equal ψ, so it lies in the fibre and is t₀-Bayes.
- **Thm 3.1**: confirmed, step by step.
  - In step 1 the level line {y_i = x} is a genuine line in the plane t₀·y = V(t₀), because t₀ ∦ e_i.
  - Step 2 uses genericity (T7) to get non-improvability, and Lemma 2.2(b) to get a singleton ∂g_i.
  - Step 5 is a pigeonhole: an uncountable G maps into a countable product.
  - The argument works for every n ≥ 3 (dim 𝔉 ≥ 2 ⇒ contradiction).
- **Cor 3.2**: confirmed. A one-dimensional range of a non-atomic vector measure forces w ∈ ℝd a.e.
  **Repair.** "All g ∈ Z_ℓ have one sign pattern" is not proved and is false in general. c(g) ∈ ℝd only gives
  sign(g) ∈ {σ, −σ}, σ = sign d. Both occur in U: for instance (1, 1, −0.5) and (−0.4, −0.4, 1). So Z_ℓ = G⁺ ∪ G⁻, the
  union of two oriented atoms (N25.3's notion).
- **Thm 3.3**: confirmed after the matching repair.
  - With G± both present, B⁻_q (silent on Z_ℓ) is a face point but not an extreme. The face is 𝔉_q = y⁻(q) + I·d with a
    **fixed** compact interval I ∋ 0, I = [−∫_{G⁺}|c|, ∫_{G⁻}|c|] in units of d. The claimed form [y⁻, y⁻+D] is wrong
    in general.
  - Steps 1–3 only use "faces at points of ℓ are translates of one segment in direction d, with d_i ≠ 0". So they go
    through verbatim, parametrising by s ∈ int I.
  - Continuity of B⁻ along ℓ holds because Z_q = Z_ℓ at every q ∈ ℓ.
  - In step 2 the second model at level x comes from q′_m. Lemma 2.2(b) does not need the two models to be Bayes at the
    same weight.
  - Step 3 is the splice at q.
- **Cor 3.4**: confirmed.
  - (b) A face at a vertex would be the unique W_a, but the extremes differ on Z_ℓ.
  - (c) If K ∩ [e_a, e_b] = ∅, then D_K ∩ {g_a, g_b < 0} contains a neighbourhood of (−1, −1, M), which a q₀-Bayes model
    rejects.
- **Thm 4.1**: confirmed. Step 1 (T is Bayes at an interior p) is a correct direct argument. Step 2 is Cor 3.4(c).
- **Cor 4.2**: confirmed.
  - The face extremes on a chord through q_m are one-sided limits of bulk Bayes models, even with other chords nearby:
    off Z_{ℓ_m} the signs at q_m are a.e. strict, and on Z_{ℓ_m} the sign is fixed by the side.
  - The extremes are coherent (singleton fibres, Fact 3.0; or as limits in measure of coherent models).
  - Measure convergence of cones gives Hausdorff convergence (R1 Prop 3.1).
  - The import of N24 Prop R1(a)/(b) is legitimate here, because the unique Bayes model off E is undominated, hence
    coherent.
- **"Consequence for T1"**: confirmed. E = ∅ would make the primary a realisation in the sense of def:realisation
  (strict signs, (BU) at every interior q, (TP)), which Thm main excludes.
- **Prop 4.3**: confirmed as stated. Three patterns on relint F_k (lem:signs) cannot fit in one pattern, nor in {±σ}.
  But its single-σ hypothesis is not implied by Cor 3.2 (see the repair). The proposition is moot in 𝓛₂ˢ, because
  Thm 4.1 already excludes p* ∈ E.

### 3.2 Do N26.5–N26.7 use the lexicographic structure, or only ψ? (Priority 3)

They use the lexicographic structure essentially, at four points:
1. "undominated ⇒ weakly ψ-Pareto" and the identification "lex tie ⇔ equal (ψ_i, S_i)";
2. (T7), which is lex-specific (local minima of the primary along the selection);
3. Lemma 2.2: the multiplier comes from the convex value function of the **additive secondary**;
4. Lemma 2.3: the splice is undominated *because* it is a pointwise Lagrangian minimiser of an **additive secondary**.

Point 4 is the decisive one. For a general (IB) preorder ranking in M0 there is no analogue: a dominator of the splice
need not be comparable to it through any supporting assessment. The comparisons "C_p ⪯_i X" with X incoherent are not
relevant comparisons, so ψ says nothing about them.

The results are also about **one particular** supporting assessment, the primary. Other supporting assessments of the
same ranking can have different exceptional sets. In n = 2 the §1.2 remark (repaired) gives one with E = ∅. Nothing in
N26 constrains E(ψ′) for those.

### 3.3 Adjudication with N25

N25 works under (H25), a general preorder ranking with (M0), and with ψ the integral part of the endorsing charges.
There, fan points and p* ∈ E are open (N25 R-a, R-c). N26 excludes both **only** for 𝓛₂ˢ with ψ = primary. There is no
conflict:
- **"Isolated exceptional points (fans) are impossible"** is PROVED for 𝓛₂ˢ primaries (Thm 3.1). It is **not** a fact
  about every supporting assessment on M_U. For bare strictly guiding fields it is false (N25.1 lists fans; e.g. put
  c(g) := g − (x·g)𝟙 on a small non-null cone of gambles with g_i ≠ 0, where |x·g| is small enough to keep strict
  signs). For supporting assessments of general M0 rankings it is open.
- **"p* ∉ E"** is PROVED for 𝓛₂ˢ primaries (Thm 4.1). It is open in general (N25.10, R-a).
- N25.8 gives "a.e.-ideal" tie-breaking at 2-dimensional faces without lex structure. It is the general-ranking analogue
  of Lemma 2.2(a) at generic levels. What has no general analogue is the splice (Lemma 2.3) that turns countably many
  multipliers into an undominated incoherent model. That is exactly why N26's exclusion does not lift.
- **For BRIEF8 within 𝓛₂ˢ.** One may choose ψ := primary. It is in N25's cone 𝒩 and endorses all comparisons, so (E_ψ)
  holds. Then N25's R-a and R-c are excluded, and only R-b-type configurations (rigid chords, p* ∉ cl E) remain.

---

## 4. Conjecture N26.R (Priority 4)

### 4.1 Is it stated correctly?

Yes, as a conditional, read as follows:
- "(BU) off a countable union of rigid chords" means E(ψ) = ⋃ chords with p* ∉ cl E (Cor 4.2);
- Thm pivot's "Z_τ = λ_τ ∩ int Δ" is read off E.

The "if so" implication is right:
- edgebox needs only E null (§4.3, confirmed);
- the T1 algebra is field-free;
- the two symmetry reductions stay inside the class:
  - p* → u is a per-world positive rescaling of the primaries, which leaves each lex order unchanged and maps chords to
    chords;
  - the 1↔2 transposition gives an 𝓛₂ˢ ranking covering σ(T1) = T1.

### 4.2 Is "Lemma levels and Lemma nopin/PL2 are the only global steps" correct?

Essentially yes, with three corrections.

- **(a) Lemma chords is global too.** It is the base of Lemma levels, the cluster-line paragraph of Thm pivot, and
  boxbridge(c). It survives off E, with the same proof (CHECKED):
  - K is Hausdorff-continuous on Ω° := int Δ ∖ E (N24 R1(a)), and Ω° is dense of full measure;
  - an open subset of Ω° that is a.e. inside an open half-plane is inside it;
  - cluster lines pass to the limit at q ∈ Ω° by Lipschitz continuity in g and relative continuity in q.
- **(b) Lemma levels survives off E (referee, PROVED).**
  - The proof's two convexity steps show conv{f > t} ∩ Ω° ⊆ {f > t} and conv{f ≤ t} ∩ Ω° ⊆ {f ≤ t}. Use triangles: the
    three vertices lie in one open side Π^±_{t′}.
  - So the two convex hulls meet only inside the null set E. A convex set of measure zero has empty interior, so a
    line L separates them.
  - {f > t} is relatively open in Ω°, and Ω° is dense on both sides of L. So L ∩ Ω° ⊆ {f ≤ t}, and
    {f > t} = Ω° ∩ int L⁺.
  - Thm pivot Steps 0, 2–5 and the cluster-line paragraph use levels and caps pointwise off E. A line through p* meets
    E in a countable set, since chords avoid p*. So they survive.
- **(c) The genuine obstruction is PL2's clopen argument, and it is sharper than "each side separately".**
  - Every chord is a full chord of Δ, so it **disconnects** int Δ.
  - Every chord separates p* from at least one vertex, because a line through int Δ missing p* leaves some vertex on
    the far side.
  - So the convex sets G = int(P_{σ₁} ∩ P_{σ₂}) and int co(G ∪ V_j) used in Thm pivot Step 1 and Lemma nopin are cut by
    a chord whenever it separates p* from the relevant vertex.
  - Chords may also accumulate (countably many, summable masses, non-crossing, vertex-cutting), so cl E ∖ E can be
    nonempty away from p*.
  - N26's evidence (b) does not address gluing across a chord or accumulation.

### 4.3 Referee Prop R1 (PROVED): the pivot theorem alone kills the chords

**Proposition R1.**
- Assume (H𝓛), and let T1 ∈ C_L be ψ-Bayes at p* (ψ the primary).
- Suppose the conclusion of Thm pivot holds for the primary's field c on the middle range of each facet F_k. That is,
  for τ ∈ [τ_i, τ_j]:
  - h(τ) has a unique (oriented) cluster line λ_τ ∋ p*;
  - τ ↦ λ_τ is continuous;
  - λ_{τ_i} = lin(p*, e_i) and λ_{τ_j} = lin(p*, e_j).

Then E(ψ) = ∅. With Thm main, no 𝓛₂ˢ ranking on M_U covers T1.

*Proof.*
1. *The lines λ_τ sweep the arc of partition {k} | {i, j}.* For τ ∈ (τ_i, τ_j), h(τ) has pattern h_i, h_j > 0 > h_k
   (lem:signs). By lem:chords(b) in the limit, e_i, e_j ∈ Π⁺ and e_k ∈ Π⁻. The lines through p* with this property form
   the closed arc of directions between lin(p*, e_i) and lin(p*, e_j) that avoids lin(p*, e_k). By continuity and the
   endpoint values, the λ_τ sweep this whole arc (intermediate value theorem).
2. *All directions are swept.* The three arcs, for k = 1, 2, 3, cover all directions through p*.
3. *A pivot line crosses each chord.* Let ℓ be a rigid chord. p* ∉ ℓ by Thm 4.1. Take x ∈ ℓ ∩ int Δ. Some λ_τ equals
   lin(p*, x), and it crosses ℓ transversally at x.
4. *Nearby charts cross ℓ.* Uniqueness of the cluster line means that normalised c(g) → a for good g → h(τ). So for g in
   a small ball B around h(τ), the chart lines cross ℓ transversally inside int Δ. Such g are not in Z_ℓ, because their
   charts are not ℓ.
5. *Contradiction.* B ∩ U is non-null, since cl D_{T1} ∖ 0 ⊆ U. Step 4 then contradicts Thm 3.3 (rigidity). So there
   are no chords, and E = ∅ by Cor 3.2(c). ∎

**Consequence.** N26.R needs re-proof of Thm pivot (cluster-line part) only. Thm nosliding, Cor PCNS and boxbridge need
no re-check under chords: once pivot holds, chords cannot exist, and Thm main applies verbatim.

### 4.4 Referee Remarks R2–R3 (CHECKED, sketch; not PROVED): where exactly PL2 can fail

- **R2.**
  - PL2 and nopin only use the 𝒰-trace q ↦ B_q ∩ 𝒰, for a small ball 𝒰 around a point w of a crossing ray (w may be
    chosen anywhere on that ray), and charts of gambles in 𝒰.
  - Suppose μ(Z_ℓ ∩ 𝒰) = 0 for every rigid chord ℓ. Then the trace is continuous in measure on **all** of int Δ, chord
    points included. The two one-sided extremes agree on 𝒰, so α_v, β_v and Γ_v are well defined at chord points via
    either extreme. Lemma D (β_v open), the collar argument and UVN then go through.
  - So PL2/nopin, and with them Thm pivot and Prop R1, survive.
- **R3 (sharpened residual, CONJECTURE N26.R′).** In 𝓛₂ˢ on M_U, a cover of T1 needs rigid chords whose tie sets
  accumulate, in measure, at every point of some crossing ray of ∂D_{T1}. That is: for every ball 𝒰 around such a
  point, some chord has μ(Z_ℓ ∩ 𝒰) > 0.

  Such chords cannot pass through p*. Their gambles near the crossing would have cluster lines ≠ lin(p*, e_c), and
  pivot forbids that, but only once pivot is known. The residual is therefore a circularity to be broken locally at the
  crossing rays. It is not a global gluing problem.

---

## 5. Scope of what is established

- **PROVED (n = 2):** an explicit 𝓛₂ˢ system on the U-domain (evaluable models: the measurable subsets of U = D_{K′}) with (LF), strict (G), (IB), (LA),
  (S) (explicit non-Bayes selection, closed sections for every model), (C) and M0. Its primary has an exceptional
  interior tie, resolved strictly at both worlds, and an intermediate coherent minimiser is covered. This shows that
  the BRIEF8 mechanism is consistent with closed choice. In n = 2 it adds no coverage.
- **PROVED (n ≥ 3, n = 3 for chords; 𝓛₂ˢ on M_U, ψ = the primary):**
  - no 2-dimensional interior faces, hence no fans;
  - E(primary) is a countable union of non-crossing, rigid, vertex-cutting chords;
  - interior targets are never at exceptional weightings, and dist(p*, E) > 0.
  Repairs: ±σ patterns, fixed-segment faces, and the wording of Lemma 2.2(c).
- **PROVED (referee):** Lemma levels and lem:chords survive off a null E. Prop R1: pivot ⇒ E(primary) = ∅.
- **Open:**
  - N26.R, reduced to Thm pivot under chords, and further (R2, sketch) to non-accumulation of chord tie sets at the
    crossing rays;
  - m ≥ 3 lex levels, advice range {+,0,−}, weakly guiding primaries;
  - every non-lexicographic M0 ranking, where fans and p* ∈ E remain open exactly as N25 says;
  - BRIEF8's second question and its two repairs.
