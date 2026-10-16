# N26. Resolving exceptional ties lexicographically: a construction in two worlds, rigidity in three

14 Oct 2026. Task: BRIEF8, construction side. Step 1: an explicit ranking whose supporting additive assessment ψ has an
exceptional interior tie which the ranking resolves. Step 2: can the mechanism be placed where the T1 obstruction lives?
Labels: **PROVED** (full proof here), **CHECKED** (verified, proof imported or sketched), **CONJECTURE**, **NUMERICS**.
Script: `n26py/warmup.py` (NUMERICS only; no proof depends on it).

Imported, and used as stated: R2 Fact 0 (LDG thm:kkm), R2 Lemma 1 (U_L = C_L ⊆ coherent under (LA), (S), (C)), R2 Thm 7 in
R7's U_L form (T7), (PB) pointwise Bayes, Lyapunov/Aumann ranges, R2 Lemma U's splice fact (a bounded non-null symmetric
difference of two models is not a cone, so two such models are not both coherent), the writeup's Thm main (no realisation
of T1 on M_U), Lemma edgebox, and N24 Prop R1 (only its easy direction: p ∉ E ⇒ K continuous at p along int Δ ∖ E).

---

## 0. Outcome

**Verdict.** Step 1 succeeds in two worlds. Every axiom is verified, and the target can be the intermediate coherent
minimiser at the exceptional weighting. Step 2 fails inside the lexicographic class. In three worlds, closed sections
pin the tie-breaking multipliers, and an exceptional weighting can never carry the target. The mechanism is the same in
both cases: within each world, the tie-breaker must act as a Lagrangian. Two worlds leave the multiplier free along the
face. Three worlds fix it.

Class used throughout: **𝓛₂ˢ on M_U.** World i ranks by lex(ψ_i, S_i).
- ψ_i(X) = ν_i(E_i(X)) with ν_i = ρ_iμ and ρ_i > 0 a.e. on U. This is a strictly guiding error-weight integral.
- S_i(X) = ∫σ_i(g, a_X(g)) dμ has an integrable envelope and is otherwise arbitrary: any sign, not guiding.
- Each ψ_i is a supporting additive assessment: X ⪯_i Y ⇒ ψ_i(X) ≤ ψ_i(Y) for **all** comparisons. So every world adds
  up, which is BRIEF8's (M0).

**N26.1 (PROVED) Warm-up construction, n = 2, U-domain (evaluable models: the measurable subsets of U = D_{K′}) with (LF).** §1 gives explicit 𝓛₂ˢ data. Its
properties:
- strict (G), (IB), (LA), (S) with an explicit selection, (C), (LF);
- the primary ψ has exactly one exceptional interior weighting t₀ = 0.3. Its tie set Z (a non-null cone of mixed
  problems) carries a whole segment of ψ-Bayes profiles;
- at t₀, ψ ties coherent minimisers with incoherent splices. Every incoherent minimiser is strictly dominated at **both**
  worlds by the coherent minimiser with the same ψ-profile;
- the undominated set is a continuous monotone path of coherent models. It inserts the segment of coherent t₀-minimisers
  between the two one-sided Bayes limits;
- the selection is a linear reparametrisation of this path, so its index is not the ψ-Bayes weighting;
- the covered target T = D_[0.25, 0.625] has an interior credal set. It is an **intermediate** coherent ψ-minimiser at
  t₀, the n = 2 analogue of BRIEF8's "T1 at p* ∈ E".

**N26.2 (PROVED) Mechanism: Lagrangian tie-breakers, no staircase.** In N26.1 no selected model is improvable at any
world (improvable: some Z has the same primary and a smaller secondary). So R2 Thm 7 is vacuous, and the countable
staircase is never used. In general 𝓛₂, if every selected model is non-improvable, then the sections of (S) are exactly
the primary sublevel sets {q : ψ_i(C_q) ≤ ψ_i(X)} (Lemma 2.1). Closed choice then reduces to lower semicontinuity of
q ↦ ψ_i(C_q).

**N26.3 (PROVED) Multiplier normal form (any n, 𝓛₂ˢ on M_U, (LA), (S), (C)).** Fix a world i and a level x interior to
the range of ψ_i. Every undominated model at world-i level x that is not improvable at i minimises S_i + λψ_i
pointwise, for each λ ∈ Λ_i(x) := −∂g_i(x), where g_i(x) = min{S_i : ψ_i = x}. If two such models at the same level
differ on a non-null set D, then Λ_i(x) = {λ_i(x)} is a single point and D ⊆ T_i(λ_i(x)) := {s_i = −λc_i}. Distinct
multipliers give disjoint sets T_i. Hence a multiplier value shared by two distinct models at one level is taken at only
countably many levels (Lemma 2.2).

**N26.4 (PROVED) Splice lemma.** Let t₀ ∈ int Δ. Suppose two undominated t₀-face models, at different levels, share a
multiplier at **every** world. Then (LA), (S), (C) fail: a bounded splice of the two is undominated and incoherent
(Lemma 2.3). So resolving a face needs, for every pair of generic face models, a world whose multiplier separates them.
In N26.1 the separating multiplier is u itself, and it moves along the face.

**N26.5 (PROVED) No two-dimensional faces (n ≥ 3).** Under 𝓛₂ˢ on M_U with (LA), (S), (C), every interior ψ-Bayes face
has dimension ≤ 1 (Thm 3.1). In n = 3, therefore, every t₀ ∈ E(ψ) lies on a **jump chord**:
- the tie set at t₀ is Z_ℓ, the set of gambles whose chart line is one fixed chord ℓ ∋ t₀;
- every point of ℓ ∩ int Δ is exceptional, with the same tie set;
- distinct chords have disjoint tie sets and do not meet in int Δ, so there are at most countably many (Cor 3.2).
The isolated exceptional point (a "fan") is impossible.

**N26.6 (PROVED) Jump chords are rigid (n = 3).** On a jump chord, the ψ-Bayes face is the same set of models at every
point of ℓ ∩ int Δ: no chart of a gamble outside Z_ℓ crosses ℓ inside Δ (Thm 3.3). Consequently (Cor 3.4):
- the chord's endpoints lie in the relative interiors of two edges, so ℓ cuts off a vertex;
- every face model is Bayes at both endpoints, and its credal set meets both of those edges.

**N26.7 (PROVED) The target never sits at an exceptional weighting (n = 3).** Assume 𝓛₂ˢ on M_U with (LA), (S), (C), and
T = D_K ∈ C_L with K ⊆ int Δ. Then every interior weighting p at which T is ψ-Bayes satisfies p ∉ E(ψ). Moreover
dist(p, E(ψ)) > 0 when p is T's (unique) Bayes weighting and K_q → K as q → p (Thm 4.1, Cor 4.2). For T1 this excludes
BRIEF8's configuration p* ∈ E, intermediate or extreme, for the whole class. A sharper fact for any jump-chord field:
T1 could only be the *accepting* extreme of a segment face, never intermediate (Prop 4.3).

**N26.8 Step 2 assessment: what is left of the route for 𝓛₂ˢ and T1.**
- By N26.5–N26.7 and Thm main, a cover of T1 needs E(ψ) ≠ ∅. E(ψ) must be a countable union of rigid, vertex-cutting,
  non-crossing chords at positive distance from p*.
- Placing exceptional weightings along the box's edge approaches does nothing. Lemma edgebox needs only E(ψ) null
  (CHECKED, §4.3).
- So the only open question for this class is whether N15's chain survives (BU) failing on such chords away from p*.
  The local part runs in a ball around p* free of E (N26.7). The global inputs to re-check are Lemma levels and Lemma
  nopin/PL2 (CONJECTURE N26.R, §4.4).
- The n = 2 warm-up shows the exclusion in N26.7 is genuinely three-world. In two worlds the frontier's level sets are
  points, so nothing pins the multipliers.

**Scope.** N26.3–N26.7 are for two-level lexicographic rankings with additive levels, a strictly guiding primary, and
the U-domain. General (IB) preorders, three or more levels, and two-sided domains (advice range {+,0,−}) are not covered
(§5).

---

## 1. Step 1: the two-world construction (N26.1)

### 1.1 Data
- **Worlds and problems.** n = 2. Problems are g with g₁ > 0. Unanimous problems have g₂ > 0. Mixed problems have
  g₂ < 0, and r(g) := −g₂/(g₁ − g₂) ∈ (0,1). The Gaussian μ gives r a distribution with a positive continuous density on
  (0,1).
- **Coherent models.** A coherent model is D_[α,β] (0 ≤ α ≤ β ≤ 1). It accepts unanimous g, accepts g iff r < α, and
  accepts −g iff r > β.
- **Domain M_U.** Take K′ = {½}, U = D_{K′}. The advice range is {+,0} on unanimous g and on mixed g with r < ½ (g ∈ U), and {−,0} on mixed
  g with r > ½ (−g ∈ U). An evaluable model is a triple: A ⊆ {r < ½} (accept g), B ⊆ {r > ½} (accept −g), W ⊆ unanimous (accept). Coherent
  members are C_{α,β} := D_[α,β] with α ≤ ½ ≤ β. M_U is a decomposable domain.
- **Primary ψ.** Error weights ρ₁ = 1 − θ(r), ρ₂ = θ(r) on mixed problems, and ρ₁ = ρ₂ = 1 on unanimous ones, with
  ψ_i(X) = ∫_{E_i(X)} ρ_i dμ. On the + side (r < ½) silence errs at world 1 and acceptance errs at world 2. On the − side
  acceptance of −g errs at 1 and silence errs at 2. On unanimous problems silence errs at both. θ is fixed by:
  - + side: θ₊(r) = 0.2 + 0.5r on (0, 0.2]; θ₊ = t₀ := 0.3 on [r₁, r₂] = [0.2, 0.3]; θ₊(r) = 0.3 + 0.5(r − 0.3) on [0.3, ½);
  - − side: θ₋(r) = 0.1 + 1.6(r − ½) on (½, 1). It is strictly increasing from 0.1 to 0.9, with θ₋(β₀) = t₀ at β₀ = 0.625.
  All weights are bounded and > 0.
- **ψ-Bayes models** at p ∈ [0,1] (p = weight of world 1). Pointwise:
  - accept g on the + side iff p > θ₊(r);
  - accept −g on the − side iff p < θ₋(r);
  - always accept unanimous g.
  So the Bayes model is C_{α_B(p), β_B(p)}, with α_B(p) = sup{r < ½ : θ₊(r) < p} (0 if empty) and β_B(p) = inf{r > ½ :
  θ₋(r) > p} (1 if empty). It is a.e. unique at every p ≠ t₀, since off the plateau the tie sets {θ = p} are single
  r-values, and the vertices are unique by strict guidance.
- **The exceptional weighting.** E(ψ) = {t₀}. The tie set is Z := {mixed g : r ∈ [r₁, r₂]}, a non-null cone. α_B jumps
  from r₁ to r₂ at t₀; β_B is continuous, with β_B(t₀) = β₀. The t₀-Bayes models are (A, B, W) with
  W = all, B = {r > β₀}, A = {r < r₁} ∪ A_Z, A_Z ⊆ Z arbitrary.
  - A_Z = Z ∩ {r < α} with α ∈ [r₁, r₂]: coherent.
  - A_Z bounded non-null: incoherent.
- **The path Γ.** Let Γ be the closure of {(α_B(p), β_B(p)) : p ≠ t₀} together with the segment {(α, β₀) : r₁ ≤ α ≤ r₂}.
  - Γ is a continuous path from (0, ½) to (½, 1), with both coordinates nondecreasing.
  - u := α + β is strictly increasing along Γ. Distinct points of a coordinatewise-monotone path have distinct sums.
  - So Γ = {(α(u), β(u)) : u ∈ [½, 3/2]} with α, β continuous and nondecreasing. Write C_u := C_{α(u), β(u)}.
- **Secondaries, built from Γ.**
  - U⁺(r) := inf{u : α(u) > r} on (0, ½) is strictly increasing, and α(u) > r ⇔ u > U⁺(r).
  - V(r) := sup{u : β(u) < r} on (½, 1) is strictly increasing, and β(u) < r ⇔ u < V(r).
  - V jumps at β₀, from r₁ + β₀ to r₂ + β₀. This is how the − side "remembers" the plateau.

  Writing A_X, B_X for X's accepted mixed sets,

  S₁(X) = ∫_{A_X} U⁺(r) ρ₁ dμ − ∫_{B_X} V(r) ρ₁ dμ,  S₂(X) = ∫_{A_X} (U⁺(r) − 3) ρ₂ dμ + ∫_{B_X} (3 − V(r)) ρ₂ dμ.

  Both integrands are bounded (|U⁺|, |V| ≤ 3/2).
- **Ranking.** X ⪯_i Y iff (ψ_i(X), S_i(X)) ≤_lex (ψ_i(Y), S_i(Y)).
- **Selection.** u(p) := ½ + p, p ∈ [0,1], and C_p := C_{u(p)}.

### 1.2 Verification

**Lemma 1.1 (Lagrangian form; PROVED).** For every u ∈ [½, 3/2], C_u is the a.e.-unique pointwise minimiser over the
advice ranges of both S₁ + uψ₁ and S₂ + (3 − u)ψ₂.

*Proof.* Compare, pointwise, the cost of each kind of advice under S₁ + uψ₁:
- unanimous: accept 0, silence uρ₁ > 0;
- + side: accept U⁺(r)ρ₁, silence uρ₁. Accept iff U⁺(r) < u iff r < α(u);
- − side: accept −g at (−V(r) + u)ρ₁, silence 0. Accept iff u < V(r) iff r > β(u).

The ties {U⁺ = u} and {V = u} are at most single r-values, hence null. For S₂ + (3 − u)ψ₂:
- unanimous: silence costs (3 − u)ρ₂ > 0;
- + side: accept costs (U⁺ − 3 + 3 − u)ρ₂ = (U⁺ − u)ρ₂. Accept iff r < α(u);
- − side: accept −g costs (3 − V)ρ₂, silence (3 − u)ρ₂. Accept iff V(r) > u iff r > β(u). ∎

**Corollary 1.2 (non-improvability; PROVED).** Let Z ∈ M with ψ₁(Z) = ψ₁(C_u). Then S₁(Z) ≥ S₁(C_u), with equality iff
Z = C_u a.e. The same holds at world 2.

*Proof.* By (PB) and Lemma 1.1, S₁(Z) + uψ₁(Z) ≥ S₁(C_u) + uψ₁(C_u), with equality iff Z is a pointwise minimiser, i.e.
Z = C_u. ∎

**(G) (PROVED).**
- Weak: if X is a.e. at least as good as Y at world i, then the error indicator inequality gives ψ_i(X) ≤ ψ_i(Y).
- If ψ_i(X) = ψ_i(Y), then E_i(X) = E_i(Y) a.e. (ρ_i > 0). On two-element advice ranges distinct kinds of advice have distinct world-i
  ranks, so X = Y and the lex values agree.
- Strict improvement on a non-null set gives ψ_i(X) < ψ_i(Y), hence X ≺_i Y.

**(IB) (PROVED).** Both levels are integrals of pointwise terms. Replacing common advice shifts ψ_i and S_i of both models
by the same amounts. A lex comparison of two vectors depends only on their difference.

**Preorders.** Lex orders on ℝ² pulled back are complete preorders.

**U_L = {C_u : u ∈ [½, 3/2]} (PROVED).**
- *Each C_u is undominated.*
  - C_u is ψ-Bayes at some interior p. The endpoints are Bayes for p ∈ (0, 0.1] and for p ∈ [0.9, 1); the plateau models
    are Bayes at t₀.
  - Let Y ⪯_i C_u at both worlds. Then ψ_i(Y) ≤ ψ_i(C_u), and p interior gives ψ(Y) = ψ(C_u).
  - Then S₁(Y) ≤ S₁(C_u), so Cor 1.2 gives Y = C_u.
- *Every other model is dominated.*
  - An undominated X is weakly ψ-Pareto, since a model better at both primaries is lex-better at both worlds. The range
    of ψ is compact and convex (Lyapunov), so X is ψ-Bayes at some p ∈ [0,1].
  - If p ≠ t₀, the Bayes model is unique, and X = C_{u(B)} for the corresponding path point.
  - If p = t₀, then X = (A, {r > β₀}, all) with A = {r < r₁} ∪ A_Z. Put m := ν₁(A_Z), and let α ∈ [r₁, r₂] satisfy
    ν₁(Z ∩ {r < α}) = m. Let Y := C_{α + β₀}.
  - On Z, ρ₂/ρ₁ = t₀/(1 − t₀) is constant, so ψ(Y) = ψ(X).
  - On Z, U⁺(r) = r + β₀. Hence S₁(X) − S₁(Y) = ∫_{A_Z}(r + β₀)dν₁ − ∫_{Z∩{r<α}}(r + β₀)dν₁ ≥ 0, with equality iff
    A_Z = Z ∩ {r < α} a.e. This is the bathtub principle: equal ν₁-mass, and r has an atomless law under ν₁.
  - Likewise S₂(X) − S₂(Y) = (t₀/(1−t₀))[∫_{A_Z} r dν₁ − ∫_{Z∩{r<α}} r dν₁] ≥ 0, with the same equality case.
  - So unless X = Y, Y ≺₁ X and Y ≺₂ X.

**(LA), (C) (PROVED).**
- C_L = U_L ∩ coherent = {C_u} ≠ ∅.
- If Y is tied with C_u at both worlds, then Y weakly dominates C_u, so Y = C_u by the first bullet above. Hence (C).

**(S) (PROVED).**
- *Competitiveness.*
  - For p ∈ (0,1), complete preorders make competitiveness on {1,2} equivalent to not being strictly dominated, which
    holds.
  - p = 1: C_p = C_{3/2} = (all of + side, ∅, all) = W₁, the a.e.-unique ψ₁-minimiser. So C_p ⪯₁ X for every X.
  - p = 0: likewise C_{½} = W₂.
- *Closed sections.* Fix X ∈ M.
  - u ↦ ψ₁(C_u) is continuous and strictly decreasing: α and β are continuous and nondecreasing with α + β strictly
    increasing, and r has a positive density.
  - Let v := ψ₁(X). If v > ψ₁(C_{½}), then {u : C_u ⪯₁ X} = [½, 3/2]. Otherwise there is a unique u_v with
    ψ₁(C_{u_v}) = v, and {u : C_u ⪯₁ X} = (u_v, 3/2] ∪ {u_v : S₁(C_{u_v}) ≤ S₁(X)}. By Cor 1.2 this is [u_v, 3/2].
  - World 2 is symmetric, with ψ₂(C_u) strictly increasing, giving [½, u′_v].
  - {p : C_p ⪯_i X} is the preimage of a closed set under the continuous u(·), hence closed. This holds for every X ∈ M.
- *Not Bayes for the index.* C_p is not ψ-Bayes for p in general. For example, C_{u(0.3)} = C_{0.8}, while the
  0.3-Bayes face is {C_u : u ∈ [0.825, 0.925]}.

**(LF) and the target (PROVED).**
- T := C_{0.25 + β₀} = D_[0.25, 0.625] lies on the plateau segment, so T ∈ C_L.
- Its credal set [0.25, 0.625] contains K′ = {½} in its relative interior.
- ∂D_T ∖ 0 consists of the rays r = 0.25 (orientation g ∈ U) and r = 0.625 (orientation −g ∈ U). A small open cone
  N ⊆ U around them has advice ranges containing "accept h" and silence. So (LF) holds.
- T is a coherent ψ-minimiser at t₀ that is neither one-sided limit C_{r₁+β₀}, C_{r₂+β₀}: it is intermediate.

**Adding up and the exceptional tie (PROVED).**
- ψ_i endorses every comparison of world i.
- At t₀, ψ ties T with incoherent splices (A_Z = Z ∩ {r < 0.25} altered on a bounded non-null set). The ranking
  dominates them, strictly at both worlds, which is BRIEF8's anatomy (N22 Prop 4.1).
- *Remark (CHECKED, sketch; not needed).* ψ is, up to scale, the only additive assessment endorsing **all** comparisons,
  since lex orders force proportionality to the primary. For the *relevant* comparisons only (B coherent undominated),
  other weights are admissible. A world-1 weight w(r)ν₁ is admissible when w is decreasing in r on each side, and it may
  jump at β₀. Such weights can break the tie at t₀. This is consistent with R2 Thm R (n = 2: U_L is always additively
  realisable). So in n = 2 the exceptional tie is a feature of ψ, not of every supporting assessment.

NUMERICS (`n26py/warmup.py`, 4000 bins per side):
- LP gap S_i(C_u) − min{S_i : ψ_i = ψ_i(C_u)} ≤ 2·10⁻¹⁵ at 25 path points and both worlds;
- 200/200 random incoherent t₀-face models are strictly dominated by the coherent model with the same profile;
- ψ₁(C_u) is monotone decreasing and ψ₂(C_u) monotone increasing along the path.

**Why it works.** The face at t₀ has a continuum of primary levels, so Thm 7 forbids improvable models there. Each face
model must therefore be a one-world Lagrangian minimiser (N26.3). Off Z, all face models agree. They can still have
*different* multipliers u, because off Z the pointwise constraint on the multiplier is an interval: the jump of V at β₀
has length r₂ − r₁. The multiplier slides across that interval as the face is traversed.

---

## 2. General lemmas for 𝓛₂ˢ on M_U (N26.2–N26.4)

**Notation.**
- On M_U an evaluable model is X ⊆ U, with two kinds of advice per problem in the advice range (+, 0).
- c_i(g) := φ_i(g,0) − φ_i(g,+), where φ_i is the pointwise primary penalty. Then c_i = ±ρ_i ≠ 0, with the strict sign
  of g_i.
- s_i(g) := σ_i(g,0) − σ_i(g,+). Put κ_i := −s_i/c_i.
- The range J_i := ψ_i(M_U) is a compact interval.
- g_i(x) := min{S_i(Z) : ψ_i(Z) = x} is attained, finite and convex on J_i, because the joint range of (ψ_i, S_i) is
  compact and convex (Lyapunov). ∂g_i(x) ≠ ∅ for x ∈ int J_i.
- Improvable at i: some Z ∈ M has ψ_i(Z) = ψ_i(X) and S_i(Z) < S_i(X).
- (T7): C_i := {ψ_i(X) : X ∈ U_L improvable at i} is countable. A level x is *generic at i* if x ∉ C_i. Every
  undominated model at a generic level is non-improvable at i.

**Lemma 2.1 (sections; PROVED, any n, any 𝓛₂).** If C_q is non-improvable at i, then {q : C_q ⪯_i X} =
{q : ψ_i(C_q) ≤ ψ_i(X)}. If this holds for all q, the section is closed for every X iff q ↦ ψ_i(C_q) is lower
semicontinuous.

*Proof.* If ψ_i(C_q) = ψ_i(X), non-improvability gives S_i(C_q) ≤ S_i(X), so C_q ⪯_i X. The other cases are by
definition. Sublevel sets of all levels are closed iff the function is lsc. ∎

**Lemma 2.2 (multiplier normal form; PROVED).** Let x ∈ int J_i, and let X be non-improvable at i with ψ_i(X) = x.
- (a) For every μ ∈ ∂g_i(x), X minimises S_i − μψ_i over M, hence pointwise. Put λ := −μ. On {c_i > 0}, X accepts iff
  κ_i < λ; on {c_i < 0}, iff κ_i > λ; except on T_i(λ) := {κ_i = λ}.
- (b) If X′ is another such model at the same level and μ(X △ X′) > 0, then ∂g_i(x) is a single point, and
  X △ X′ ⊆ T_i(λ_i(x)).
- (c) T_i(λ) ∩ T_i(λ′) = ∅ for λ ≠ λ′. Hence {λ_i(x) : x is a level carrying two non-improvable models that differ on a
  non-null set} is countable.

*Proof.*
- (a) For any Z ∈ M, S_i(Z) ≥ g_i(ψ_i(Z)) ≥ g_i(x) + μ(ψ_i(Z) − x), and S_i(X) = g_i(x). Then (PB) gives pointwise
  minimality. The acceptance rule follows by comparing (σ_i + λφ_i)(+) with (σ_i + λφ_i)(0), i.e. by the sign of
  s_i + λc_i.
- (b) On X △ X′ both kinds of advice are pointwise minimisers for every λ ∈ −∂g_i(x), so s_i + λc_i = 0 there. Two values of λ
  would force c_i = 0 on a non-null set, which is excluded.
- (c) On T_i(λ) ∩ T_i(λ′) we have (λ − λ′)c_i = 0. By (b) each listed value has a non-null T_i. Pairwise disjoint
  non-null sets in a finite measure space are countably many. ∎

**Lemma 2.3 (splice; PROVED, any n).** Let t₀ ∈ int Δ, and let C ≠ C′ be undominated ψ-t₀-Bayes models. Suppose that for
each world i, both minimise S_i + λ_iψ_i over M, for a common λ_i. Then (LA), (S), (C) fail.

*Proof.*
- C and C′ agree off the t₀-tie set (pointwise uniqueness there), and D := C △ C′ is non-null.
- Take R with A := D ∩ {|g| < R} non-null, and let X be C switched to C′ on A.
- X is t₀-Bayes, since both kinds of advice are t₀-minimisers on D. For each i, X pointwise minimises σ_i + λ_iφ_i, since both
  kinds of advice are minimisers on D.
- *X is undominated.* Suppose Y ⪯_i X for every i. Lex gives ψ_i(Y) ≤ ψ_i(X), and t₀ interior gives ψ(Y) = ψ(X). Then
  S_i(Y) = S_i(Y) + λ_iψ_i(Y) − λ_iψ_i(X) ≥ S_i(X), so Y is nowhere strictly better.
- C is coherent (R2 Lemma 1), and X △ C = A is bounded and non-null, so X is incoherent.
- An undominated incoherent model contradicts R2 Lemma 1. ∎

**Reading.**
- *Lemma 2.3 is the obstruction.* A face is resolved only if the multipliers separate every two generic face models at
  some world.
- *Lemma 2.2 is the pinning mechanism.* As soon as a level is shared by two different non-improvable models, its
  multiplier is unique. Only countably many levels can carry such a shared multiplier with distinct values.
- *Two worlds versus three.* In n = 2 the Pareto frontier is a curve, levels are generically single points, and nothing
  pins. In n = 3 it is a surface, and level sets are curves.

---

## 3. Three worlds: faces of the primary (N26.5, N26.6)

Standing **(H𝓛)**: n = 3, 𝓛₂ˢ on M_U, (LA), (S), (C). Let t₀ ∈ int Δ, let Z_{t₀} := {g : t₀·c(g) = 0}, and let
𝔉 := {ψ(X) : X t₀-Bayes}. Fix a t₀-Bayes model B₀. Then

 𝔉 = ψ(B₀) + {∫_A w dμ : A ⊆ Z_{t₀}},  with w(g) = ∓c(g), the sign set by B₀'s advice.

This is the range of a non-atomic vector measure, so it is compact and convex. Every coordinate y_i is non-constant on
𝔉 when 𝔉 is not a point, because w_i ≠ 0 a.e. on Z_{t₀}.

**Fact 3.0 (every face point is carried; PROVED).** For y ∈ 𝔉, the fibre {X t₀-Bayes : ψ(X) = y} contains an undominated
model C^y, coherent by R2 Lemma 1.

*Proof.*
- The joint range {(∫_A w, ∫_A δσ) : A ⊆ Z} is compact and convex (Lyapunov). So the secondary profiles over the fibre
  form a compact set, and a lexicographic minimum of (S₁, S₂, S₃) is attained.
- A weak dominator Y has ψ(Y) ≤ y, hence ψ(Y) = y (t₀ interior). So Y lies in the fibre and cannot be strictly better.
  ∎

**Theorem 3.1 (no 2-dimensional face; PROVED).** Under (H𝓛), dim 𝔉 ≤ 1 for every t₀ ∈ int Δ.

*Proof.* Suppose dim 𝔉 = 2.
1. For each i and each x ∈ (min_𝔉 y_i, max_𝔉 y_i), the chord 𝔉 ∩ {y_i = x} is a nondegenerate segment.
2. If x is generic at i, any two points y ≠ y′ of that chord give non-improvable models C^y, C^{y′} at world-i level x.
   They differ on a non-null set, since their profiles differ. x ∈ int J_i. By Lemma 2.2(b), ∂g_i(x) is a singleton.
3. By Lemma 2.2(c), the values λ_i(x), x generic, form a countable set Λ_i.
4. Let G be the set of y ∈ relint 𝔉 with y_i generic for i = 1, 2, 3. G is 𝔉 minus countably many lines, hence
   uncountable.
5. The map y ↦ (λ₁(y₁), λ₂(y₂), λ₃(y₃)) ∈ Λ₁ × Λ₂ × Λ₃ has countable range. So some two points y ≠ y′ of G share all
   three multipliers.
6. By Lemma 2.2(a), C^y and C^{y′} both minimise S_i + λ_iψ_i for each i. Lemma 2.3 gives a contradiction. ∎

**Corollary 3.2 (jump chords; PROVED).** Let t₀ ∈ E(ψ) under (H𝓛). Then:
- (a) There is d ∈ ℝ³ with t₀·d = 0 such that Z_{t₀} = Z_ℓ := {g ∈ U : c(g) ∈ ℝd} a.e. Every g ∈ Z_ℓ has chart line
  ℓ := {q ∈ int Δ : q·d = 0}. All g ∈ Z_ℓ have one sign pattern (that of ±d), because c(g) has the strict sign of g.
- (b) For every q ∈ ℓ, Z_q = Z_ℓ. In particular ℓ ⊆ E(ψ).
- (c) Distinct jump chords have disjoint tie sets and do not meet in int Δ. There are countably many, and E(ψ) is their
  union.

*Proof.*
- (a) The face is a segment (Thm 3.1, and not a point since Z_{t₀} is non-null and w ≠ 0). So w(g) ∈ ℝd a.e. on
  Z_{t₀}; otherwise the range of the vector measure would be 2-dimensional.
- (b) Z_q ⊇ Z_ℓ is non-null, so q ∈ E. By (a) at q, Z_q is single-direction, and that direction must be d.
- (c) A gamble has one chart line. If two chords met at q, then Z_q would contain two directions, contradicting (a) at
  q. Countability follows from disjointness of non-null sets. ∎

For q ∈ ℓ put B⁻_q := the q-Bayes model rejecting Z_ℓ. It is unique a.e. because the ties off Z_ℓ are null. The face is
𝔉_q = [y⁻(q), y⁻(q) + D], with y⁻(q) := ψ(B⁻_q) and D := −∫_{Z_ℓ} c dμ. Note that D does not depend on q. The map
q ↦ B⁻_q is continuous in measure along ℓ (dominated convergence; ties off Z_ℓ are null at every q ∈ ℓ).

**Theorem 3.3 (rigidity; PROVED).** Under (H𝓛), q ↦ B⁻_q is constant a.e. on ℓ ∩ int Δ. Equivalently, for a.e. g ∉ Z_ℓ,
the sign of q·c(g) is constant on ℓ ∩ int Δ.

*Proof.* If B⁻ were not locally constant everywhere on the connected chord, there would be q ∈ ℓ and q′_m → q in ℓ with
B⁻_{q′_m} ≠ B⁻_q.

*Step 1: faces at different points are not collinear.* Suppose 𝔉_{q′} ⊆ L, the line containing 𝔉_q.
- The support plane {q·y = min} contains the nondegenerate segment 𝔉_q, hence L, hence 𝔉_{q′}.
- So 𝔉_{q′} ⊆ argmin_R q·y = 𝔉_q, and by symmetry the faces are equal.
- Then B⁻_{q′} is q-Bayes, hence equal to B⁻_q off Z_ℓ. So B⁻_{q′} ≠ B⁻_q forces y⁻(q′) ∉ y⁻(q) + ℝD.

*Step 2: generic face levels at q are shared.*
- Let x ∈ (y⁻_i(q), y⁻_i(q) + D_i) be generic at i, with face point y ∈ 𝔉_q, y_i = x.
- By continuity, for large m the level x lies in the open i-range of 𝔉_{q′_m}, at a face point y′.
- y′ ≠ y, by Step 1 (the faces are translates of [0, D]).
- The undominated models C^y and C^{y′} (Fact 3.0) are non-improvable at i and differ. So Lemma 2.2(b) applies:
  ∂g_i(x) is a singleton, and by Lemma 2.2(c) the values λ_i(x) over generic face levels of 𝔉_q form a countable set Λ_i.

*Step 3: splice.*
- The s ∈ (0,1) with all coordinates of y⁻(q) + sD generic are cocountable. Recall D_i ≠ 0, so each level is hit by at
  most one s.
- s ↦ (λ_i(y⁻_i(q) + sD_i))_i has countable range. So two such s ≠ s′ share all three multipliers.
- Their models C, C′ are both q-Bayes. Lemma 2.3 at t₀ = q gives a contradiction.

*Equivalence.* Constancy of B⁻_q on ℓ means that for each q, sign(q·c(g)) = sign(q₁·c(g)) for a.e. g ∉ Z_ℓ. By Fubini on
(g, q) ∈ U × ℓ, for a.e. g this holds for a.e. q ∈ ℓ. q·c(g) is affine in q, so the sign is constant on the open
chord. ∎

**Corollary 3.4 (shape of a rigid chord; PROVED).** Under (H𝓛), let ℓ be a jump chord with endpoints q₀, q₁ ∈ ∂Δ. Then:
- (a) every t-Bayes model for t ∈ ℓ ∩ int Δ (the same set for all t) is q₀- and q₁-Bayes;
- (b) q₀ and q₁ lie in the relative interiors of edges;
- (c) if q₀ ∈ relint[e_a, e_b], every coherent face model D_K has K ∩ [e_a, e_b] ≠ ∅. So ℓ cuts off the vertex common to
  its two edges, and the face models' credal sets meet both of those edges.

*Proof.*
- (a) Rigidity makes the set of t-Bayes models independent of t ∈ ℓ. Pass to the limit t → q₀ in t·ψ(X) ≤ t·ψ(Y).
- (b) If q₀ = e_a, every face model would be the unique e_a-minimiser W_a. But the two face extremes differ on Z_ℓ.
- (c) At q₀ = (s, 1−s, 0)-type weights with s ∈ (0,1), g with g_a, g_b < 0 has q₀·c(g) < 0, so a q₀-Bayes model rejects
  a.e. such g ∈ U. If m_c ≥ δ > 0 on K, then D_K ⊆ U contains a neighbourhood of (−1, −1, M) for large M, a contradiction.
  The two endpoints are on different edges, since ℓ passes through int Δ and is not an edge. Both edges share the vertex
  that ℓ separates from the other two. ∎

---

## 4. Step 2: the target and the T1 obstruction (N26.7, N26.8)

### 4.1 The target is never at an exceptional weighting

**Theorem 4.1 (PROVED).** Assume (H𝓛) and T = D_K ∈ C_L with K ⊆ int Δ. Then T is ψ-Bayes at some interior p, and every
such p lies outside E(ψ).

*Proof.*
1. *T is ψ-Bayes at an interior weight.*
   - T is undominated, hence weakly ψ-Pareto, hence ψ-Bayes at some p ∈ Δ (Lyapunov, separation).
   - If p = e_a, then T = W_a, which is false: T rejects the non-null set U ∖ cl D_T ∩ {h_a > 0}.
   - If supp p = {a, b}, silence T on T ∩ {h_a < 0, h_b < 0}. This set is non-null because K ⊆ int Δ, and the resulting
     model is in M_U. The change lowers ψ_a and ψ_b strictly, contradicting p-Bayes.
2. *p ∉ E(ψ).* If p ∈ E(ψ), then by Cor 3.2 p lies on a jump chord ℓ. By Thm 3.3 and Cor 3.4(a), T is q₀-Bayes at an
   endpoint q₀ ∈ relint[e_a, e_b]. By Cor 3.4(c), K meets [e_a, e_b], contradicting K ⊆ int Δ. ∎

**Corollary 4.2 (E stays away from the target; PROVED).** Under Thm 4.1's hypotheses, suppose T is ψ-Bayes at p and K_q → K
(Hausdorff) as q → p along int Δ ∖ E(ψ). This holds whenever p ∉ E: N24 Prop R1's easy direction, i.e. N12 Prop 1.2's
argument. Then dist(p, E(ψ)) > 0.

*Proof.*
- Suppose jump chords ℓ_m pass through q_m → p.
- Each face extreme of ℓ_m is a limit of bulk K_{q′} with q′ ∉ E arbitrarily close to q_m: it is a one-sided limit,
  as in N22 §4.
- By Cor 3.4(c) its credal set meets ∂Δ. So bulk K_{q′_m}, with q′_m → p, stays at Hausdorff distance at least
  dist(K, ∂Δ) − o(1) from K.
- This contradicts K_{q′_m} → K. ∎

**Consequence for T1 (PROVED, assembling).** Suppose an 𝓛₂ˢ ranking on M_U satisfies (G), (IB), (LA), (S), (C) and
covers T1. Then:
- E(ψ) ≠ ∅. Otherwise, at every interior q the unique ψ-Bayes model is lex-undominated, hence coherent, and T1 is Bayes
  at an interior p*. That is a realisation, which Thm main excludes.
- E(ψ) is a countable union of rigid, vertex-cutting, non-crossing chords (Cor 3.2, Thm 3.3, Cor 3.4).
- p* ∉ E(ψ), and indeed dist(p*, E(ψ)) > 0 (Thm 4.1, Cor 4.2).

So BRIEF8's suggestion "T1 itself at an exceptional weighting, as an intermediate coherent minimiser" is impossible in
this class, and so is T1 as an extreme. The n = 2 construction (N26.1) shows that the corresponding configuration *is*
possible in two worlds. The exclusion therefore rests on the three-world multiplier pinning of §3.

### 4.2 A direct reason T1 cannot be intermediate (any field with a jump chord at p*)

**Prop 4.3 (PROVED).** Let ψ be any strictly guiding error-weight field on M_U. Suppose the tie set at p* has the
single-chart form Z_ℓ (one sign pattern σ), the face extremes D_{K_±} are coherent, and T1 is a face model. Then
D_{K₊} = T1. Hence T1 is the accepting extreme, and D_{K₋} = T1 ∖ R with R confined near one corner ray, of sign
pattern σ = sign(r_{ki}).

*Proof.*
- *The accepting extreme is T1.* D_{K₊} ⊇ T1 ⊇ D_{K₋}, and both differences lie in Z_ℓ.
  - If D_{K₊} ≠ T1, then K₊ ⊊ T1, so K₊ misses a vertex v_k.
  - Every h ∈ relint F_k then has P_{K₊}(h) > 0, so D_{K₊} ∖ T1 contains points next to all of relint F_k.
  - These carry the three sign patterns of Lemma signs, contradicting a single σ.
- *Shape of the other extreme.* For R := T1 ∖ D_{K₋}, the boundary trace {h ∈ ∂D_{T1} : P_{K₋}(h) < 0} is a union of
  sets {h ∈ F_k : h·(m − v_k) < 0}, m ∈ K₋ ∖ T1.
  - Each such set is an end-interval of the facet, since h(τ)·δ is affine in τ.
  - A single pattern forces it inside one corner-ray region. ∎

### 4.3 Exceptional weightings along the edge approaches do not affect the box (CHECKED)

Lemma edgebox's proof uses three things:
- the half-plane chart of a.e. good gamble (Fubini over q ∉ E);
- superadditivity of P(q, ·) = P_{K_q} at a.e. q in O = H(A) ∩ H(B) ∩ int Δ;
- the fact that q₀ ∈ cl O.

It never uses Bayes uniqueness at a specified weight. Its conclusion is valid for every field with E(ψ) Lebesgue-null.
In fact it gives the slightly stronger form [e_a, e_b] ∩ cl(H(A) ∩ H(B) ∩ int Δ) = ∅.

Prop boxbridge(c) needs only uniqueness of the cluster lines of A and B, which comes from the analysis at p*. So placing
exceptional weightings on the edge approaches cannot disable the box. Only the derivation of (PC), (NS) at p* matters,
and by Cor 4.2 that happens in a ball free of E.

### 4.4 What remains for 𝓛₂ˢ: rigid chords away from p*

Where does N15's chain use (BU) at weights outside a small ball B(p*, r) ⊆ int Δ ∖ E?
- (i) **Lemma levels**: global half-plane form of {P(·, g) > t} on int Δ, via cluster lines of g − t′𝟙 and joint
  continuity. It is used in Thm pivot Step 0 and in Lemma sandwich, with radius r₀ = dist(p*, ∂Δ).
- (ii) **Lemma nopin**: the set int co(G ∪ V_j) reaches the vertex neighbourhoods V_j, and Lemma PL2's clopen argument
  runs on it. Rigid chords cut off vertices, so they can cross this set.
- (iii) Lemma UVN: as q → e_l along int Δ ∖ E. Unaffected (dominated convergence off a null set).
- (iv) Box: unaffected (§4.3).

Across a rigid chord, q ↦ K_q jumps from K₋ to K₊ ⊆ K₋. Only gambles whose minimiser over K₋ lies in K₋ ∖ K₊ see the
jump, and no other chart crosses the chord.

**CONJECTURE N26.R.** The conclusions of Thm pivot, Thm nosliding and Cor PCNS hold under (BU) on a neighbourhood of p*
and off a countable union of rigid chords. If so, then with N26.7 no 𝓛₂ˢ ranking on M_U covers T1.

Evidence:
- (a) Every local step runs on B(p*, r) once Lemma sandwich is used with r in place of r₀. The constants r₀/(r₀ ± |y|)
  change but remain finite.
- (b) The two global steps (i) and (ii) use straight-level and clopen arguments. A jump along a chord that no other chart
  crosses plausibly preserves them on each side separately.

Not proved. Whether rigid chords can exist at all in a system with (S) is also open. On a rigid chord the face's levels
may be singly occupied: the face's normal cone runs from q₀ to q₁ ∈ ∂Δ, and nearby frontier points have non-positive
normals. In that case the n = 2 mechanism of §1 could resolve it.

---

## 5. Scope, and what does not transfer

- **Class.** All of §§2–4 assumes:
  - two lexicographic levels;
  - additive levels;
  - a strictly guiding primary (error weights > 0);
  - the U-domain, so that two-element advice ranges give the scalar κ_i.

  These enter only through (T7), (PB), Lyapunov ranges and Lemma 2.2.
  - *m levels (CONJECTURE).* R7 Lemma 7′ gives a depth-k staircase, and Lemma 2.2 should iterate level by level (the
    multiplier at depth k is pinned by shared depth-(k−1) fibres).
  - *Advice range {+,0,−}.* κ_i becomes a pair of ratios, and Lemma 2.2(b) still forces ties. Thm 3.1's use of Lemma 2.3 is
    unchanged. Not checked.
  - *Weakly guiding primaries* (c_i = 0 allowed) break Lemma 2.2(b), since ties with c_i = 0 do not pin λ. This is the
    N9.9 zero-pattern class, and it is not covered.
- **Supporting assessments other than the primary.** BRIEF8's ψ (N13 Prop B / N22 Thm 2.1) may differ from the primary.
  For 𝓛₂ˢ the primary is a supporting assessment satisfying (α)–(δ), so the main theorem already forces E(primary) ≠ ∅,
  and §§3–4 describe that set. Nothing here says other assessments must have ties. In n = 2 they need not (§1.2 remark).
- **General (IB) preorders.** The multiplier argument needs real-valued levels and Lagrange duality. For non-lexicographic
  rankings that add up (M0) without being lexicographic, the BRIEF8 question is untouched by this note.
- **BRIEF8's second question and the two repairs** (N₀ conic vs arbitrary N; permitted ties) are not addressed.

---

## 6. Status

| Claim | Status | Where |
|---|---|---|
| N26.1 two-world 𝓛₂ˢ system: (G), (IB), (LA), (S) explicit, (C), (LF); E(ψ) = {t₀}; ties resolved; intermediate target covered | PROVED | §1 |
| Lagrangian form / non-improvability of every selected model in N26.1 | PROVED; NUMERICS gap ≤ 2·10⁻¹⁵ | Lemma 1.1, Cor 1.2 |
| ψ is the only assessment endorsing all comparisons; other relevant-comparison assessments can break the tie (n = 2) | CHECKED (sketch) | §1.2 remark |
| Lemma 2.1: non-improvable selection ⇒ sections = primary sublevel sets | PROVED | §2 |
| Lemma 2.2: multiplier normal form, uniqueness when levels are shared, countability | PROVED | §2 |
| Lemma 2.3: common multipliers on one face ⇒ undominated incoherent splice | PROVED | §2 |
| Thm 3.1: no 2-dimensional interior ψ-faces (any n ≥ 3) | PROVED | §3 |
| Cor 3.2: E(ψ) = countable union of non-crossing jump chords with single-chart tie sets (n = 3) | PROVED | §3 |
| Thm 3.3: jump chords are rigid; Cor 3.4: they cut off a vertex, and face credal sets meet both edges | PROVED | §3 |
| Thm 4.1: interior targets are never at exceptional weightings; Cor 4.2: positive distance | PROVED | §4.1 |
| T1 cover in 𝓛₂ˢ ⇒ E ≠ ∅, rigid chords only, p* ∉ cl E | PROVED (uses Thm main) | §4.1 |
| Prop 4.3: with a single-chart tie set at p*, T1 is the accepting extreme, never intermediate | PROVED | §4.2 |
| Edge box robust to null E | CHECKED | §4.3 |
| N26.R: N15's chain survives rigid chords away from p* (⇒ no 𝓛₂ˢ cover of T1) | CONJECTURE | §4.4 |
| Extensions to m levels, advice range {+,0,−} | CONJECTURE / not checked | §5 |
