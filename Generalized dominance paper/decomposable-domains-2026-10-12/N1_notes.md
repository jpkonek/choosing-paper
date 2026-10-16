# N1: negligible-stakes indifference (NSI_θ): infrastructure and the triangle obstructions

13 Oct 2026. Labels as in BRIEF.md: **PROVED** (full proof written here), **CHECKED** (verified, proof
sketched), **CONJECTURE**. NUMERICS are evidence only. Scripts: `n1py/`.

Citations: R1 (Lemma 1.1–1.5, Prop 2.1, Thm 2.2, Prop 2.6, Prop 3.1), R10a (Thm V, Thm R, Thm M), R10b
(Prop V, Lemma FS, Lemma UVN, Lemma M, Thm PL), R14 (Thm A, Lemma B2, B4), R15 (Thm 1, Lemma 4.1,
Lemma 6.1, Thm 6.2), all as repaired in R6, R8, R12, R17, R18; CCIBU; LDG thm:kkm.

---

## 0. Outcome

**The answer to the author's question is negative, and the reason is structural rather than a matter of
θ being too small.** For additive systems on decomposable domains, NSI_θ adds no coverage of T1, of any interior
triangle, or (with the norms I checked) of any interior target, **for any θ**.

1. **Infrastructure carries over.** In additive form, (G) under NSI_θ *forces* ℓ_i(g,good) = ℓ_i(g,0) on band
   problems; it does not merely allow it (Lemma 1.2). The following carry over:
   - Interior Bayes uniqueness: R1 Lemma 1.4's splicing argument is unchanged (Prop 2.2).
   - The chart characterisation, with modified vertex charts (Thm 2.4).
   - Interiority of the target prior. This now has a two-line proof valid for every θ (Prop 2.3).
2. **Closed choice in three worlds, with no vertex condition (Thm 3.1, PROVED).**
   - In three worlds, an additive system with integrable envelopes whose interior Bayes models are unique and
     coherent (IBU) satisfies (LA), (S), (C). This holds under **any** guidance order, NSI_θ and Σ_T
     included.
   - The selection is R14's Chebyshev least-norm selection. Its vertex localisation repairs CCIBU's vertex
     step, so **no condition replaces "strict guidance at vertices"**: IBU alone suffices.
   - CCIBU's quadratic selection, by contrast, fails for NSI_θ systems with (LF) at an interior target
     whenever θ is below an explicit target-dependent value. For T1 at ε = 0.3 that value is 0.916
     (Prop 3.3).
3. **Chord pinning (Lemma 4.1, PROVED; any n ≥ 3, any θ > 0, any advice ranges compatible with (LF)).**
   - Suppose a facet point h′ of ∂D_T has 0 < h′_c < θ‖h′‖. Then the touching point m(h′) of T lies in K_q for
     **every** q on the half-chord (e_c, p\*].
   - Reason: world c is indifferent there, so the + vs 0 comparison has the same sign all along the chord.
4. **Acceptance needs a non-negligible winning stake (Lemma 4.2, PROVED).** Every h ∈ ∂D_T∖0 has a
   coordinate h_c ≥ θ‖h‖. Hence θ ≤ θ₁(T) := min_{h∈∂D_T} max_c h_c/‖h‖.
5. **Band no-go (Thm 4.3, PROVED; any n ≥ 3).**
   - If θ < θ₀(T) := max_c max_{h∈∂D_T} h_c/‖h‖, no additive NSI_θ system covers D_T. A non-degeneracy
     condition is needed; it is automatic when the relevant band edge lies inside a facet, and it holds for
     T1.
   - The contradiction: on the facet, chord pinning meets strict reward just past the band edge
     |h_c| = θ‖h‖. This is the brief's "crossings at the band edges replacing g_i = 0", made exact.
6. **No window (Thm 4.5).**
   - θ₁ < θ₀ always: PROVED for Euclidean and sup norms in n = 3; CHECKED for n ≥ 4.
   - So coverage would need θ₀ ≤ θ ≤ θ₁, which is impossible.
   - **For T1, every θ ∈ (0,1) fails, for either norm.** Euclidean values, with κ = (1+2ε)/(1−ε):
     θ₀(T1) = √((1+κ²)/(2+κ²)), between 0.816 and 1; θ₁(T1) = κ/√(2κ²+4), between 0.408 and 0.707.
     For the sup norm, θ₀ = 1 for every interior target.
   - **Answer to "how small can θ be": there is a target-dependent lower bound θ₀(T), and it is large**
     (θ₀(T1) ≥ √(2/3) for every ε). Above it, a second obstruction θ > θ₁(T) takes over.
7. **Triangle obstructions under NSI_θ (§5).**
   - Steps using strict reward for right answers at negligible stakes, near coordinate crossings, fail as
     stated. These are Thm V / Prop V, Thm 1(c), UVN(a) at crossings, Lemma M Step 4, and the A-witnesses of
     Lemma 6.1.
   - They survive with band edges replacing crossings, for θ below the facet values b_c(v).
   - Steps using strict penalty for wrong answers survive unchanged: FS, UVN(b), (a₋)_c ≤ 0, and the
     B-witnesses.
   - R10a Thm R becomes *stronger*: no concave chart representative exists for any θ > 0 and any target with
     a crossing.
   - R15's hypotheses (DF) + (ND) become *inconsistent* with NSI_θ, so Thm 6.2 is vacuous. Thm 4.3
     supersedes it.
8. **Nearby statement (Cor 4.6, CHECKED).** The same proof applies to *any* good~silence tie region Θ_c.
   - Near ∂D_T, a tie region at world c must contain the whole positive-c arc of ∂D_T or miss it.
   - Every boundary point needs a strictly rewarded positive coordinate.
   - So near the target boundary only world-wise (Σ_T-type) indifference is viable. For T1 not even that is
     viable: each positive-c arc contains points whose only positive coordinate is c.
   - Hence every tie-based weakening reduces T1 to strict guidance near ∂D_T. That is the original open
     problem, where all triangle obstructions apply unchanged.

**Recommendation (§6).** Do not pursue NSI_θ for coverage. The mirror weakening, "errors at negligible
stakes ~ silence", is not killed by the same argument on two-sided domains (advice range {+,0,−}). It is the only nearby
variant I could not close (§6.2, open).

---
## 1. Formalisation

### 1.1 The order

**Setting.** n ≥ 2 worlds. A binary problem is a pair {g, −g}, represented by g ∈ H. The kinds of advice
are +, 0, −, ×. At world i, "good" means accepting the orientation h ∈ {g, −g} with h_i > 0, and "bad"
means accepting the other one.

**Band.** Fix a norm ‖·‖ on ℝⁿ and θ ∈ (0,1). The pair is *in the i-band* if
- it is **mixed** (some coordinate positive and some negative), and
- |g_i| ≤ θ‖g‖.

The condition is invariant under g ↦ −g, so it is a property of the pair. Write Band_i for the set of such
pairs.

**Choice of norm.**
- With either the Euclidean norm or the sup norm, θ ≥ 1 puts every mixed pair in every band. That is
  total indifference on mixed problems, which is the D_Δ / Σ_Ω regime. So θ ∈ (0,1) throughout.
- All PROVED statements in §§1–5 hold for **every** norm, with the thresholds computed in that norm.
- The "no window" step (Thm 4.5) is PROVED for the Euclidean and sup norms in n = 3. For other norms it
  is a CONJECTURE.
- Numerical thresholds are given for both norms. The default is the Euclidean norm |·|.

**NSI_θ guidance order at world i** (rank classes, best first):
- on Band_i: {good, silence} < bad < ×;
- off Band_i, and on every unanimous pair: good < silence < bad < × (the original four-rank order).

So silence ties only with *good* advice. Bad advice is strictly worse than silence everywhere, and × is
strictly worst everywhere.

**(G_θ) on M_L.**
- (weak) If X is at least as good as Y in this order at world i on a.e. pair, then X ⪯_i Y.
- (strict) If, in addition, X is in a strictly better rank class on a non-null set, then X ≺_i Y.

Since swapping good and silence on band pairs is a weak improvement in both directions, (G_θ) **forces**
ties. It is not a weakening of (G) in the sense of an inclusion of axiom sets. As in the brief's
treatment of D_Δ and Σ_T, NSI_θ systems are an *additional admissible class*: a target counts as covered
if a strictly guiding system covers it **or** an NSI_θ system does. All other axioms are unchanged: decomposable
domains, (IB), (LA), (S), (C), (E), and (LF) at the target.

### 1.2 Additive form

**Lemma 1.2 (PROVED).** An additive ranking L_i(X) = ∫ ℓ_i(g, a_X(g)) dμ on a decomposable domain satisfies (G_θ)
at world i iff, for a.e. g and all a, b ∈ A(g) (the advice range of g):
- (i) ℓ_i(g,a) < ℓ_i(g,b) whenever a is in a strictly better NSI_θ class at i than b; and
- (ii) ℓ_i(g,good) = ℓ_i(g,0) whenever g ∈ Band_i and both are in A(g).

*Proof.*
- (i), and "if" for both parts: as in R1 Lemma 1.1.
- "Only if" for (ii): let E ⊆ Band_i ∩ {good, 0 ∈ A(g)} be measurable. Let X, Y ∈ M agree off E and give
  good, respectively silence, on E. Both are in M because M is a decomposable domain. Each is a weak improvement
  on the other, so L_i(X) = L_i(Y), i.e. ∫_E (ℓ_i(good) − ℓ_i(0)) dμ = 0.
- Since E is arbitrary, the integrand vanishes a.e. ∎

**Chart vectors.** As in R1 Prop 2.1, put c = ℓ(0) − ℓ(+), c′ = ℓ(0) − ℓ(−) and d = c − c′ = ℓ(−) − ℓ(+),
wherever the relevant kinds of advice are in the advice range. At a mixed pair g and world i, Lemma 1.2 gives:

| | g_i > θ‖g‖ | 0 < g_i ≤ θ‖g‖ | −θ‖g‖ ≤ g_i < 0 | g_i < −θ‖g‖ |
|---|---|---|---|---|
| c_i | > 0 | **= 0** | < 0 | < 0 |
| c′_i | < 0 | < 0 | **= 0** | > 0 |
| d_i | > 0 | > 0 | < 0 | < 0 |

So:
- c is weakly sign-preserving, with zeros exactly on the band coordinates where + is good;
- d remains **strictly** sign-preserving everywhere (good vs bad is never tied).

The table of charts for each advice range in R1 Prop 2.1 is otherwise unchanged:
- {+,0}: R(g) = {c·p > 0};
- {+,−}: R(g) = {d·p > 0};
- {+,0,−}: R(g) = {c·p > 0, d·p > 0} and R(−g) = {c′·p > 0, d·p < 0}.

**Lemma 1.3 (modified vertex property; PROVED).** Let h have advice range {+,0} or
{+,0,−} (so accepting h is in the advice range, but not every evaluable model accepts h). Then:
- δ_i ∈ R(h) if h_i > θ‖h‖;
- δ_i ∉ R(h) if 0 < h_i ≤ θ‖h‖, and in that case δ_i lies on the c-line, a tie;
- δ_i ∉ cl R(h) if h_i < 0.

*Proof.* Read off the table; d_i > 0 whenever h_i > 0. ∎

**Lemma 1.4 (radial invariance; PROVED).** Let h ∈ Band_c with h_c > 0 and both + and 0 in the advice range, and
let q = (1−s)e_c + s p with s ∈ (0,1]. Then:
- c(h)·q = s·c(h)·p;
- d(h)·q = (1−s)d_c + s·d(h)·p, with d_c > 0.

Hence for advice range {+,0} the + vs 0 decision is constant along every ray from e_c. For advice range {+,0,−}:
- "+ is the unique minimiser at p" propagates to all of (e_c, p];
- "+ loses to 0 at p" (c·p < 0) propagates to the whole ray.

*Proof.* c_c = 0 and d_c > 0 by the table. The minimiser conditions are the strict inequalities of R1
Prop 2.1, and both are preserved by these formulas. ∎

This is the mechanism behind everything in §4. It is also the exact sense in which the vertex e_c "does
not see" band problems.

## 2. Infrastructure under NSI_θ: additive systems on decomposable domains

### 2.1 Facts that need no guidance

**Prop 2.1 (PROVED).** Let L be additive with integrable envelopes and satisfy (G_θ) on a decomposable domain.
- (a) R1 Lemma 1.2 holds: Bayes models are exactly the pointwise minimisers.
- (b) R1 Lemma 1.3 holds: (LA) + (S) give a coherent p-Bayes model at every p; an undominated model is Bayes
  at some p; interior Bayes models are undominated.
- (c) The attainable set R is compact and convex.
- (d) LDG thm:kkm holds: (LA), (S), (C) imply U_L = C_L.

*Proof.* None of these uses (G). For LDG thm:kkm I re-read its proof: it uses (LA), (S) and (C) only,
through KKM on the sets A_ω = {p : c_p ⪯_ω m}. The other items are R1's proofs verbatim: splicing,
Lyapunov, and p_j > 0. ∎

### 2.2 Interior Bayes uniqueness

**Prop 2.2 (R1 Lemma 1.4 under NSI_θ; PROVED).** Assume (LA), (S), (C). For every interior p:
- (i) every p-Bayes model is coherent;
- (ii) the pointwise minimiser is a.e. unique.

*Proof.*
- (i): Prop 2.1(b), (d).
- (ii): R1's splicing argument goes through unchanged. Suppose two distinct kinds of advice both minimise on a
  non-null set. They differ in acceptance of g or of −g. This is still true for the tied pair (good, 0) at
  vertices; but the claim concerns interior p, and × is never an interior minimiser because it is strictly
  worst at every world. The splices X_F are evaluable models (the domain is closed under splicing) and all p-Bayes, hence all coherent by (i), hence
  all a.e. cones. Polar Fubini then gives the contradiction exactly as in R1.
- Strictness of (G) was never used. The only property of the kinds of advice used is that distinct kinds of advice in
  {+, 0, −} differ in acceptance. ∎

So in any n, under NSI_θ: (LA) + (S) + (C) ⇒ (IBU). (IBU) is the hypothesis "every interior w·L has an
a.e. unique minimiser, and it is coherent". The converse for n = 3 is Thm 3.1.

*Remark.* Interior ties are not forced by the band zeros. A tie between + and 0 at an interior p means
c·p = 0, and that set is null for a fixed p unless c ≡ 0 on a non-null set. c ≡ 0 is impossible on mixed
pairs, because c_j < 0 at every negative coordinate. If all positive coordinates of g are in the band,
then c ≤ 0 and c ≠ 0, so + loses at every interior prior. This is the content of Lemma 4.2.

### 2.3 The target prior is interior

**Prop 2.3 (PROVED; any n ≥ 2; any θ, indeed any guidance order in which bad is strictly worse than
silence at every world).** Let D_K ∈ C_L with K ⊆ int Δ, and assume (LF) at D_K. Then every p\* at which
D_K is Bayes is interior.

*Proof.*
- Let S = supp p\* ≠ Ω. Put g(t) = −1_S + t·1_{S^c}. Then P_K(g(t)) changes sign, because m(S^c) > 0 on K.
  So there is g₀ ∈ ∂D_K∖0 with (g₀)_S < 0.
- Every h near g₀ has h_S < 0, and by (LF) silence is in its advice range. Accepting h is strictly worse than
  silence at every world of S, so at p\* accepting h is never a minimiser.
- But a non-null part of that neighbourhood lies in D_K, and D_K is p\*-Bayes. Contradiction. ∎

This is shorter than R1 Prop 2.6. It uses only strict *penalty* of wrong answers, which NSI_θ keeps.

### 2.4 Chart characterisation

**Theorem 2.4 (R1 Thm 2.2 under NSI_θ; PROVED).**

**(N) Necessity.** Assume (LA), (S), (C). Then:
- (N1), (N2) hold verbatim (Prop 2.2).
- (N3_θ) At e_i: off Band_i the e_i-Bayes advice is a.e. unique and is the best advice in the advice range at
  world i. On G_i := Band_i ∩ {good and 0 both in the advice range} it may be either good or silence.
  - The world-i minimising face is F_i := argmin_R y_i = x⁰ + {∫_E δ dμ : E ⊆ G_i}, with
    δ(g) = ℓ(g, good_i) − ℓ(g, 0) and δ_i = 0.
  - Every Pareto-efficient point of F_i has a **unique** realisation, and it is coherent. This holds under
    (IBU), by R14 Thm A with the admissible sequence (e_i, w), w = (0, α, β), α, β > 0. Strict guidance
    is not needed (R17 §1.3).
  - Inefficient e_i-Bayes models may be incoherent.
- (N4) holds verbatim.

**(S) Sufficiency (n = 3).** (IBU) alone implies (LA), (S), (C), as well as (G_θ) and (IB) (Thm 3.1). No
condition at boundary priors or at vertices is needed. This replaces R1 Thm 2.2(S), which assumed
uniqueness at all p ∈ Δ.

**(T)** holds verbatim, and p\* is interior by Prop 2.3.

**The charts themselves.**
- R1 Prop 2.1's table holds with the vertex property of Lemma 1.3.
- The "vertex-respecting half-space" chart becomes: an open half-plane that contains δ_i for every
  out-of-band positive coordinate, has δ_i **on its boundary line** for every in-band positive coordinate,
  and has every δ_j with a negative coordinate outside its closure.
- A pair whose positive coordinates are all in band has R(g) ∩ int Δ = ∅. So it is accepted at no
  interior prior. ∎

**Modified Prop V / Thm V (vertex anchoring).** See §5, item V.

## 3. Closed choice in three worlds: the vertex step repaired

Notation is as in R14:
- R is the attainable set and a_i < min_R y_i.
- For q ∈ Δ, f_q(y) = max_i q_i(y_i − a_i), t\*(q) = min_R f_q, and B(q) = argmin_R f_q.
- σ(B) is the least-norm point argmin_{y∈B} Σ(y_i − a_i)², and x(q) := σ(B(q)).
- F_i = argmin_R y_i and m_i = min_R y_i.

**Theorem 3.1 (PROVED; n = 3; any guidance order).** Let L be additive on a decomposable domain, with integrable
envelopes, and assume (IBU). Then:
- every coordinate of q ↦ x(q) is lower semicontinuous on Δ;
- each x(q) is efficient and supp(q)-competitive, with a unique coherent realisation C_q.

Hence (LA), (S), (C) hold. (G) and (IB), for whatever guidance order the penalties respect, hold because
the rankings are additive. In particular the theorem covers NSI_θ, Σ_T, and strict guidance.

*Proof.*

*Step 1: efficiency, competitiveness, realisation.*
- x(q) is efficient and supp(q)-competitive by R14 Lemma B2(i). That proof uses neither guidance nor
  interiority of q (R17 §1.7).
- Uniqueness and coherence of the realisation is R14 Thm A, which uses (IBU) only.

*Step 2: active sets.*
- For q ∈ Δ put c_i(q) = a_i + t\*(q)/q_i for i ∈ supp q. Let m ∈ ri B(q) and I(q) = {i ∈ supp q : m_i = c_i}.
  I(q) is non-empty and independent of m.
- By R14 Lemma B4(i), which is pure convexity, y_I = c_I for every y ∈ B(q).
- Since B(q) = R ∩ {y_j ≤ c_j, j ∈ supp q}, there are three cases:
  - |I| = |supp q|: B(q) is a point if supp q = Ω. If supp q has two elements, B(q) is the segment
    R ∩ {y_S = c_S}.
  - |I| = 2 < |supp q| = 3: B(q) = R ∩ {y_I = c_I, y_k ≤ c_k}, a segment in direction e_k.
  - |I| = 1, I = {i}: the minimality argument of R14 B4(ii) (no guidance used) gives m_i = min_R y_i. So
    B(q) ⊆ F_i, and B(q) = F_i ∩ {y_l ≤ c_l(q), l ∈ supp q∖i}.
- In the first two cases B(q) is a point or a segment parallel to a coordinate axis, so it has a
  coordinatewise **least element**, and then σ(B(q)) is that least element.

*Step 3: the vertex regime V_i.* Let
 V_i := {q ∈ Δ : ∃ y ∈ F_i with q_l(y_l − a_l) < q_i(m_i − a_i) for all l ∈ supp q∖{i}}.
- q ∈ V_i iff I(q) = {i}.
  - "If": the witness y has f_q(y) = q_i(m_i − a_i) ≤ f_q(z) for every z ∈ R, since z_i ≥ m_i. So y ∈ B(q)
    with the inactive inequalities strict, which places i alone in the active set of ri B(q).
  - "Only if": a relative-interior point m of B(q) is such a witness.
- V_i is relatively open in Δ. The inequalities are strict and continuous in q. A coordinate l ∉ supp q
  enters with q′_l small, so q′_l(y_l − a_l) is small.
- e_i ∈ V_i (the condition is vacuous), and the V_i are pairwise disjoint.
- On V_i, B(q) = {y ∈ F_i : g_l(q,y) := q_l(y_l − a_l) − q_i(m_i − a_i) ≤ 0, l ≠ i}. Here F_i is compact
  and convex, and the g_l are jointly continuous and convex in y, with a Slater point at each q ∈ V_i.
- So q ↦ B(q) is Hausdorff-continuous on V_i:
  - lower hemicontinuity: Slater plus convexity (move a point slightly toward the Slater point);
  - upper hemicontinuity: closed graph.
- By Berge with a strictly convex objective, σ∘B is continuous on V_i.

*Step 4: lower semicontinuity everywhere.*
- At q ∈ ∪V_i, x is continuous (Step 3, V_i open).
- At q ∉ ∪V_i, B(q) has a least element ℓ(q) = x(q) (Step 2). Let q_m → q.
  - Every cluster point z of x(q_m) lies in B(q), by upper hemicontinuity of B (R14 Lemma B2(iii); Berge
    on the fixed compact R).
  - Hence z ≥ ℓ(q) = x(q) coordinatewise.
- So every coordinate of x is lower semicontinuous.

*Step 5: (S) and (C).*
- {p : C_p ⪯_i X} = {p : x_i(p) ≤ L_i(X)}, which is closed by Step 4.
- Competitiveness on supp p is Step 1.
- (C) holds because tied profiles have the same unique realisation (R14 Thm A).
- (LA) holds because each C_q is coherent and undominated. ∎

**What replaces "strict guidance at vertices".** Nothing beyond (IBU).
- CCIBU needed argmin_R y_i to be a point. Chebyshev localisation instead makes the selection constant,
  equal to σ(F_i), on the open set V_i ∋ e_i. So interior indices approaching e_i from different
  directions do not produce different cluster points.
- On an edge (e_i, e_j) near e_i, the selection slides continuously through σ(F_i ∩ {y_j ≤ c_j(q)}) to
  the y_j-minimal point of F_i. This is the "lexicographic tie-break" the brief suggested, produced
  automatically.

**Corollary 3.2.** R14 §1 point 4 flagged the three-world Σ_T case as breaking exactly at vertex
selections. That gap is closed: Thm 3.1 applies to Σ_T systems verbatim.

For n ≥ 4 the R14 residual remains: (L) on open faces of dimension ≥ 2. Without strict guidance it is
worse, because the Prop B5 oscillating-fibre geometry is no longer excluded by Lemma B3.

**Prop 3.3 (CCIBU's quadratic selection fails under NSI_θ; PROVED).** Let n = 3, let D_K have (LF) and
K ⊆ int Δ.
- The plane {h_i = 0} meets ∂D_K∖0 in two rays, w ∈ (0,+,−) and w′ ∈ (0,−,+) in the (i, j, k) coordinates.
  The cone D_K ∩ {h_i = 0} contains e_j and e_k, so its boundary rays lie in opposite open quadrants.
- Suppose w_j > θ‖w‖ or w′_k > θ‖w′‖. For example, for the Euclidean norm and T1 this holds whenever
  θ < (b′+ε)/√(b′² + (b′+ε)²), where b′ = (1−ε)/3; that is 0.916 at ε = 0.3.
- Then the projection Φ′_{e_i} of F_i to the two omitted coordinates has no least element.
- By R14 Prop B1, with the R17 repair at vertices, the CCIBU selection then violates (S) at e_i.

*Proof.*
- Φ′_{e_i} = x⁰_{jk} + {∫_E (δ_j, δ_k) dμ : E ⊆ G_i}, with signs:
  - δ_l < 0 iff good_i is good and out of band at l;
  - δ_l = 0 iff good_i is good and in band at l;
  - δ_l > 0 iff good_i is bad at l.
- y_j is minimised by E ⊇ {δ_j < 0} with E ∩ {δ_j > 0} = ∅, and y_k likewise. A least element exists iff
  {δ_j < 0 < δ_k} ∪ {δ_k < 0 < δ_j} is null.
- Say w_j > θ‖w‖. Near w, inside N, both good_i and 0 are in the advice range.
- The orientations with h_i ∈ (0, θ‖h‖), h_j > θ‖h‖ and h_k < 0 form a non-null set there. On it
  δ_j < 0 < δ_k.
- The case w′_k > θ‖w′‖ is symmetric. ∎

## 4. The new obstructions: chord pinning and the band no-go

### 4.0 Standing hypotheses

**(H_θ).**
- n ≥ 3, θ ∈ (0,1), any norm.
- An additive NSI_θ system (Lemma 1.2) on a decomposable domain with integrable envelopes, satisfying (LA), (S),
  (C). By Prop 2.2 this gives (IBU); in n = 3 it is equivalent to (IBU) by Thm 3.1.
- A target D_K ∈ C_L with K ⊆ int Δ and dim K = n−1, and (LF) at D_K with neighbourhood N.
- D_K is Bayes at p\*, which is interior by Prop 2.3, so D_K ≈ B_{p\*}.

**Notation.**
- Γ = ∂D_K ∖ 0. Every point of Γ is mixed, because K ⊆ int Δ.
- φ_c(h) = h_c/‖h‖.
- T(h) = argmin_{m∈K} m·h is the touching set. h ∈ Γ is *smooth* if T(h) is a single point m(h).
  Smooth points are dense in Γ: a convex cone's boundary is differentiable a.e.
- Shrink N so that N ∩ (−cl D_K) = ∅. This is possible because dim K = n−1 (R10a §1, R12).

### 4.1 Chord pinning

**Lemma 4.1 (chord pinning; PROVED under (H_θ)).** Let h′ ∈ Γ with 0 < h′_c < θ‖h′‖. Then for every
q ∈ (e_c, p\*]:
- K_q ∩ T(h′) ≠ ∅;
- if h′ is smooth, m(h′) ∈ K_q.

In particular, for a polytope K and h′ in the relative interior of the facet F_v, the vertex v lies in
K_q along the whole half-chord.

*Proof.*
1. *Choosing U.* Take a convex open ball U ∋ h′ with U ⊆ N, every point of U mixed, U ⊆ {0 < h_c < θ‖h‖},
   and U ∩ (−cl D_K) = ∅. Then for a.e. h ∈ U, + and 0 are in the advice range, and c(h)_c = 0 (Lemma 1.2).
2. *Points of D_K ∩ U.* For a.e. such h, + is the unique p\*-minimiser, since B_{p\*} ≈ D_K and the
   minimiser is unique (IBU). So c·p\* > 0, and also d·p\* > 0 if − is in the advice range. By Lemma 1.4, + is the
   unique minimiser at every q ∈ (e_c, p\*].
3. *Points of U ∖ cl D_K.* For a.e. such h, neither h nor −h is in D_K, so the p\*-minimiser is 0. Hence
   c·p\* < 0, using that ties are null at p\*. By Lemma 1.4, c·q < 0 at every q on the ray, so + is not a
   minimiser.
4. *Agreement on U.* So B_q ∩ U ≈ D_K ∩ U. By (IBU), B_q ≈ D_{K_q} up to nonnegative gambles, which do not
   meet U. Hence D_{K_q} ∩ U and D_K ∩ U are a.e.-equal open convex sets, and therefore equal.
5. *Touching.* P_{K_q}(h′) = 0, because h′ ∈ ∂(D_K ∩ U). Take m ∈ argmin_{K_q} m·h′.
   - P_{K_q} ≤ m·(·) everywhere, so m·h > 0 on D_K ∩ U, and therefore m·h ≥ 0 on cl D_K ∩ U.
   - Since cl D_K is a convex cone and m·h′ = 0: for y ∈ cl D_K and small t, h′ + t(y − h′) ∈ cl D_K ∩ U,
     which gives m·y ≥ 0.
   - So m lies in (cl D_K)\* ∩ Δ = K, and m·h′ = 0. That is, m ∈ T(h′). ∎

**Why this is new.** Under strict guidance, Lemma 1.4 fails: c_c > 0 tilts the + vs 0 comparison toward
acceptance as q → e_c. NSI_θ removes exactly that tilt on band problems. The target's local boundary
structure is then frozen along a whole segment of priors ending at a vertex of Δ. This is the
"plateau"/pinning phenomenon of R10b, but on a segment, and **forced** by the axioms rather than assumed.

### 4.2 Acceptance needs a winning stake

**Lemma 4.2 (W; PROVED under (H_θ)).** Every h ∈ Γ has max_c φ_c(h) ≥ θ. Moreover a.e. h ∈ D_K ∩ N has
max_c φ_c(h) > θ. Hence θ ≤ θ₁(K) := min_{h∈Γ} max_c φ_c(h).

*Proof.*
- Let h ∈ D_K ∩ N be mixed with every positive coordinate in band. Then c(h) ≤ 0, with c_j < 0 at every
  negative j (table, §1.2). So c·p\* < 0, and + is not a p\*-minimiser, since 0 is in the advice range by (LF).
- So such h form a null subset of D_K ∩ N. The condition "every positive coordinate is in band" is open,
  so if some h ∈ Γ had max_c φ_c(h) < θ, a non-null piece of D_K ∩ N near h would consist of such points.
  Contradiction. ∎

### 4.3 The band no-go

**UVN_θ (R10b Lemma UVN(a) under NSI_θ; PROVED).** Let x ∈ N be mixed with x_c > θ‖x‖. Then there is a
relative neighbourhood V of e_c with x ∈ D_{K_q} for every interior q ∈ V.

*Proof.* This is R10b's proof with one change.
- Choose x⁻ < x, close to x, with x⁻_c > θ‖x⁻‖, and a ball B₀ ∋ x⁻ inside N ∩ {h_c > θ‖h‖}.
- For a.e. h ∈ B₀, + is in a strictly better NSI_θ class at c than 0, −, × (good, out of band), so it is
  the strict ℓ_c-minimiser. The gap argument and dominated convergence give μ(B₀ ∖ B_q) → 0 as q → e_c.
- The half-ball argument puts x⁻ ∈ D_{K_q}, and upward closure gives x ∈ D_{K_q}. ∎

**Theorem 4.3 (band no-go; PROVED).** Assume (H_θ). Suppose there are a world c and a pair (h₀, m₀) such
that:
- (B1) h₀ ∈ Γ, h₀_c = θ‖h₀‖, and h₀ = lim h′_k for smooth h′_k ∈ Γ with 0 < (h′_k)_c < θ‖h′_k‖ and
  m(h′_k) → m₀;
- (B2) (non-degeneracy) some k ∈ ℝⁿ has m₀·k < 0 and β′(h₀; k) > 0, where β(h) := h_c − θ‖h‖ (concave)
  and β′ denotes the one-sided directional derivative.

Then **no such system exists**: D_K is not covered by any additive NSI_θ system.

*Proof.*
1. By Lemma 4.1, m(h′_k) ∈ K_q for all q ∈ (e_c, p\*]. K_q is closed, so m₀ ∈ K_q. Also m₀·h₀ = 0.
2. Put x = h₀ + tk with t > 0 small. Then x ∈ N, x is mixed, β(x) > 0, and m₀·x = t·m₀·k < 0.
3. By UVN_θ, x ∈ D_{K_q} for interior q in a neighbourhood V of e_c. The half-chord (e_c, p\*] meets V.
4. At such q, P_{K_q}(x) ≤ m₀·x < 0. Contradiction. ∎

The priors used all lie on one segment ending at e_c. No edge prior, no vertex model, no regularity
(DF)/(NA), and no box is needed. This is consistent with R10b Prop L: the priors accumulate at e_c ∈ ∂Δ.

**Prop 4.4 (when (B1), (B2) hold).** Let θ₀(K) := max_c max_{h∈Γ} φ_c(h).

(a) **PROVED.** If θ < θ₀(K), (B1) holds for some c.
- Pick c and h\* ∈ Γ with φ_c(h\*) > θ. The set {h_c = 0} ∩ Γ ≠ ∅ (n ≥ 3; R10b Prop V, first step).
- Γ ∩ S^{n−1} is a topological (n−2)-sphere, hence connected. Take a path in it from a zero of φ_c to h\*.
  Let h₀ be the first point on the path with φ_c ≥ θ, and let the path start at the last zero before h₀.
- Between that zero and h₀, φ_c ∈ (0, θ). Smooth points are dense there, and a subsequence of touching
  points converges.

(b) **PROVED.** Let K be a polytope, n = 3, and use the Euclidean norm.
- On the facet arc F_v (a great-circle arc), φ_c(h(t)) = R_{v,c} cos(t − τ), with R_{v,c} := |π_{v^⊥}e_c|.
  So for θ ≠ R_{v,c}, the level θ is crossed transversally.
- Suppose (B2) fails at h₀. Then m₀ = λ(e_c − θĥ₀) with λ > 0 (the alternative to the existence of k,
  since ∂β(h₀) = {e_c − θĥ₀}). If h₀ ∈ relint F_v, then m₀ = v.
- With v·ĥ₀ = 0, this forces ĥ₀ ∝ π_{v^⊥}e_c and θ = R_{v,c}. At a corner h₀, m₀ is the strip-side
  vertex, and the same identity results.
- Hence (B2) holds for every θ < θ₀(K) outside the finite set E(K) := {R_{v,c}}.

(c) **PROVED (sup norm, n = 3, polytope).** ∂‖·‖_∞ at h₀ is conv{sgn(h₀_j)e_j : |h₀_j| = ‖h₀‖}, with
j ≠ c because h₀_c = θ‖h₀‖ < ‖h₀‖.
- (B2) fails only if m₀ ∈ int Δ is a positive multiple of e_c − θΣα_j sgn(h₀_j)e_j.
- That requires both j ≠ c to have h₀_j = −‖h₀‖, i.e. h₀ ∝ (θ, −1, −1) up to order, together with m₀ the
  matching vertex.
- This is again a finite exceptional set of θ.

(d) **T1 (PROVED; numerics confirm).**
- *Euclidean.* For θ < θ₀(T1), every first band-edge point lies in a facet relative interior, with
  θ < R_{v,c} there. So (B2) holds. (`n1py/t1_arcs.py`: about 400 endpoints for each ε ∈ {.05, .3, .6},
  none at a corner.)
- *Sup norm.* h₀ ∝ (θ, −1, −1) on F_2 would need θ = (2b′+ε)/b′ > 1. So (B2) holds for every θ < 1.

### 4.4 No window

Thm 4.3 excludes θ < θ₀(K) (outside E(K)), and Lemma 4.2 excludes θ > θ₁(K). Since θ₁(K) ≤ θ₀(K) always,
any surviving θ must satisfy max_c φ_c ≡ θ on Γ (or be exceptional).

**Theorem 4.5 (PROVED; n = 3; Euclidean or sup norm).** No credal K ⊆ int Δ with dim K = 2 has
max_c φ_c ≡ θ on Γ in a way compatible with Lemma 4.2. Hence θ₁(K) < θ₀(K), and **no θ ∈ (0,1) outside
E(K) admits additive NSI_θ coverage of D_K.**

*Proof (Euclidean).* Suppose φ_c ≤ θ on Γ for every c, together with Lemma 4.2. Let
C_c = {h : h_c > θ|h|}, a round convex cone of half-angle α = arccos θ about e_c.
1. *Starting point.* The arc cos t·e₁ + sin t·e₂, for t ∈ (−π/2, 0), starts in D_K, at e₁, and leaves cl D_K
   before reaching −e₂. Its exit point h¹ ∈ Γ has φ₁ = max_c φ_c, since φ₂ < 0 = φ₃. So φ₁(h¹) = θ.
2. *Locally D_K = C₁.* Near h¹, φ₂ < 0 and φ₃ ≈ 0 < θ. By Lemma 4.2, a.e. point of D_K near h¹ has φ₁ > θ.
   So locally D_K ⊆ C₁, and Γ ⊆ {φ₁ = θ} = ∂C₁. Being open and relatively closed in C₁ near h¹, D_K agrees
   with C₁ locally.
3. *Following ∂C₁.* Follow Γ along the circle ∂C₁ ∩ S², which is parametrised by
   θe₁ + √(1−θ²)(cos s·e₂ + sin s·e₃), starting from s = π.
   - If θ < 1/√2: φ₃ = √(1−θ²) sin s reaches θ at some s₁. Past that point ∂C₁ enters C₃, where φ₃ > θ, so
     Γ must leave ∂C₁ there and continue on ∂C₃. By step 2 applied at both sides, D_K is locally C₁ ∪ C₃
     near the junction ray. The two circles cross transversally, so this union has a reflex edge, and D_K
     is not convex.
   - If θ ≥ 1/√2: φ₂, φ₃ ≤ √(1−θ²) ≤ θ on ∂C₁, with equality only at tangency points, where the same
     reflex/pinch argument applies. So Γ is all of ∂C₁ and D_K = C₁. But e₂ ∈ D_K and φ₁(e₂) = 0. ∎

*Sup norm.* The same argument applies with C_c = {h_c > θ|h_j| for all j ≠ c}.
- The exit point is h¹ ∝ (θ, −1, 0).
- Along the face h₁ = −θh₂ of C₁, φ₃ = h₃/‖h‖ reaches θ at (θ, −1, θ). The face normals (1, θ, 0) and
  (0, θ, 1) differ, so the union is non-convex.
- Going the other way, one passes the convex edge (θ, −1, −1) of C₁ and then meets C₂ in the same way.
- Otherwise D_K = C₁, which is again impossible. ∎

*n ≥ 4 (CHECKED, sketch).* Lemma 4.1, Lemma 4.2, UVN_θ, Thm 4.3 and Prop 4.4(a) are dimension-free. The
window argument runs the same way in the 2-plane spanned by e₁, e₂, then follows ∂C₁ within the 3-space
spanned by e₁, e₂, e_j. A full write-up of the junction step for general n is not attempted.

**Corollary (T1 and the threshold question; PROVED).** Put κ = (1+2ε)/(1−ε) and b′ = (1−ε)/3.
- *Euclidean.*
  - θ₀(T1) = √((1+κ²)/(2+κ²)). It is attained at the foot of e_c on v_k^⊥ (k ≠ c), which lies in
    relint F_k. As ε increases from 0 to 1 it rises from √(2/3) ≈ 0.816 to 1: 0.858, 0.928, 0.984 at
    ε = .1, .3, .6.
  - θ₁(T1) = κ/√(2κ²+4). It is attained at h ∝ (κ/2, κ/2, −1) ∈ relint F_3. It rises from 1/√6 ≈ 0.408
    to 1/√2: 0.485, 0.601, 0.685 at ε = .1, .3, .6.
  - θ₁ < θ₀ ⟺ κ² < 2 + 2κ², which always holds.
  - Every θ < θ₀ is excluded by Thm 4.3 (no exceptional values for T1), and every θ > θ₁ by Lemma 4.2.
    **So no θ ∈ (0,1) works.**
- *Sup norm.*
  - θ₀ = 1 for every interior K: take h = e_c − t(𝟙 − e_c) at its boundary value t₀ = min_K m_c/(1−m_c),
    which is ≤ 1 for some c, since some m_c ≤ 1/2.
  - So Thm 4.3 alone excludes every θ < 1, for every interior target satisfying (B2), T1 included.
  - θ₁(T1) = min(1, κ/2).
- NUMERICS (`n1py/thresholds.py`, `n1py/rand_check.py`).
  - The formulas match to 4 digits.
  - Over 391 random interior triangles (Euclidean): min θ₀ = 0.912, max θ₁ = 0.660. So the excluded
    ranges overlap with a margin of at least 0.338.

**Answer to (c)(2).** There is a target-dependent threshold θ₀(T) below which the obstruction persists. It
is the largest normalised positive stake on the target's boundary, and for T1 it is at least √(2/3) for
every ε. Above θ₁(T) a second obstruction takes over. For T1, and every interior triangle tested, the two
ranges cover (0,1).

### 4.5 Arbitrary tie regions (the nearby statement)

**Cor 4.6 (CHECKED).** Replace the band by any measurable family of tie regions: at world c, good ~
silence on Θ_c (a set of mixed pairs), and the order is strict elsewhere. Assume each Θ_c equals the
closure of its interior up to a null set.

The proofs of Lemmas 1.2, 1.4, 4.1, 4.2 and of UVN_θ, Thm 4.3 go through with:
- "0 < h_c < θ‖h‖" replaced by "h_c > 0 and h ∈ int Θ_c";
- "h_c > θ‖h‖" replaced by "h_c > 0 and h ∉ cl Θ_c".

Consequences, near Γ:
- (i) For each c, the positive-c part of Γ cannot contain both interior points of Θ_c and points of its
  exterior that are adjacent to them along Γ, apart from non-degenerate exceptions. So, up to such
  exceptions, Θ_c ⊇ a neighbourhood of Γ ∩ {h_c > 0}, or Θ_c misses one. That is, near the boundary the
  ties are world-wise, i.e. of Σ_T type.
- (ii) Every h ∈ Γ needs a positive coordinate outside the tied worlds.

For T1, every positive-c arc Γ ∩ {h_c > 0} contains points whose only positive coordinate is c (the foot
points of §4.4). So no world can be tied near Γ, and **any tie-based weakening leaves T1 with strict
guidance on a neighbourhood of Γ.** That is the original open problem; §5 shows its obstructions are
unaffected.

*Consistency checks.*
- With Θ_c = all mixed pairs, i.e. Σ_{{c}}, (ii) says that no boundary point of the target may have c as
  its only positive coordinate. That means K touches the face {m_c = 0}, which matches the shape of the
  Σ_T closures in CSE.
- With all worlds tied, nothing mixed near Γ can be accepted, which is the D_Δ exception.

*Remark (dim K < n−1, e.g. T3).* Lemma 4.1 needs only h′ ∉ −cl D_K. That fails only for h′ ⊥ K, a
nowhere-dense set of directions in Γ, so Thm 4.3 extends with h′_k chosen off it. CHECKED.

---

## 5. Triangle obstructions under NSI_θ, item by item (small θ > 0)

**Two kinds of strictness.**
- "Strict reward" means c_c > 0 for h_c > 0: the right answer beats silence. NSI_θ removes it on
  0 < h_c ≤ θ‖h‖.
- "Strict penalty" means c_c < 0 for h_c < 0, and d strict: the wrong answer is worse than silence or the
  right answer. NSI_θ keeps it.

Below, b_c(v) := sup_{h∈relint F_v} φ_c(h). For T1, b_c(v_k) = θ₀(T1) for every crossing pair (k, c).

| Item | Status under NSI_θ | Step that used strict reward at negligible stakes |
|---|---|---|
| **R10a Thm V / R10b Prop V** (e_i ∈ K_{e_i}) | **FAILS as stated.** Survives in modified form V_θ (PROVED, below): dist(e_i, K_{e_i}) ≤ C·θ | Prop V: B_{e_i} ∩ B ≈ {h_i > 0} on a ball B around the crossing w (w_i = 0). Thm V: h^θ = h⁰ + θk with tiny positive h_i is accepted. On Band_i the vertex model may be silent |
| R10a Cor V1 / R10b Cor V1 (every evaluable model accepts h only if h ≥ 0) | Modified (PROVED): every evaluable model accepts h only if min_i h_i ≥ −C′θ‖h‖ | via V_θ |
| **R10b Lemma FS** | **Survives** for z′ with z′_S < 0. Needs either a ball inside N, or margin z′_s < −C′θ‖z′‖ to exclude that every evaluable model accepts z′ (V1_θ) | none: it uses strict *penalty* |
| R10b Lemma UVN(a) | Survives with the **band edge replacing the crossing**: x_c > θ‖x‖ (UVN_θ, §4.3) | the vertex strict minimiser for h_c > 0 |
| R10b Lemma UVN(b) | **Survives unchanged** for x ∈ N, where 0 is in the advice range. Elsewhere it needs a C′θ margin | none (strict penalty) |
| R10b Lemma D, Lemma P (geometry) | Survive unchanged | none |
| **R10b Lemma M** | Survives in modified form M_θ for θ < b_c(v) (CHECKED). Take w₊ ∈ relint F_v with (w₊)_c > θ‖w₊‖, and replace U by a convex tube in N around the facet segment [w₋, w₊] meeting no other facet. Steps 1–3 are unchanged (R4 Thm B uses only d, which is still strict). Step 4 uses UVN_θ at w₊ and (a₋)_c ≤ 0 (strict penalty) | Step 4, UVN(a) at w₊ near the crossing (w₊ → w) |
| **R10b Thm PL** | Survives for pairs v ≠ v′ with θ < b_c(v) and θ < b_{c′}(v′); for T1, for θ < θ₀(T1). CHECKED. Superseded by Thm 4.3 | via Lemma M and UVN(a) at w_j > 0 |
| **R10a Thm R** (ray lemma, concave charts) | **Strengthened** (PROVED, Thm R_θ below): for every θ > 0 and every target with a crossing, no concave sign-respecting representative exists. No corner rays are needed | Step 3: "f_i has the sign of h_i near the zero line on a crossing facet" |
| R10a Thm M (gauge mixtures) | Gauge mixtures violate (G_θ): f_i > 0 on band-positive h. Any NSI_θ variant would need f_i = 0 there, which Thm R_θ forbids | — |
| **R15 Thm 1 (a), (b), (d)** | Survive (they use no guidance) | — |
| **R15 Thm 1 (c)** (crossing rows, λ > 0) | **FAILS.** Replaced by the flatness Lemma 5.1 (PROVED): crossing facets are first-order flat. So **(DF) + (ND) are inconsistent with NSI_θ** | two-sided clusters at the crossing; λ > 0 via UVN(a) at h_i > 0 near the crossing |
| R15 Lemma 3.2, Thm 5.1, Prop 5.2, 5.3 | Vacuous (they presuppose (c)) | — |
| R15 Lemma 4.1 (p\* drops out) | Survives (no guidance) | — |
| **R15 Lemma 6.1** (vertex-limit box) | The **mechanism survives** (CHECKED): FS at edge priors near e_b, with **A-witnesses restricted to A_b > θ‖A‖**, beyond the b-band edge of F_{k′}. B-witnesses are unchanged (strict penalty). The quantitative Λ_{ab} ≤ 1 needs (DF), which is inconsistent with NSI_θ, so the box has no first-order content | the threshold A_b > s|c_a|/((1−s)λ_{bk′}) → 0 as s → 0, i.e. reward λ_{bk′}A_b > 0 for arbitrarily small A_b. Under NSI_θ, c_b(A) = 0 for A_b ≤ θ‖A‖, so c·q₀ = s·c_a(A) < 0 and A is never accepted |
| **R15 Thm 6.2** (all-facing no-go) | **Vacuously true** (hypotheses inconsistent). Superseded by Thm 4.3, which needs no (DF), (ND), (NA_w), box, or corner rays | via (c) and Lemma 6.1 |

**V_θ (PROVED; Euclidean norm).** Let w ∈ Γ with w_i = 0 and |w| = 1, and let B(w, r) ⊆ N. Assume
θ < r/4. Then every coherent e_i-Bayes model D_{K_{e_i}} has a point m₀ ∈ K_{e_i} with
 |m₀ − e_i| ≤ (1+√2)(2 + 4/r)·θ.

*Proof.*
1. At e_i, h ∈ N with h_i < 0 is strictly rejected (strict penalty). Hence P := P_{K_{e_i}} ≤ 0 on
   N ∩ {h_i < 0}, and by continuity P ≤ 0 on Π := {h_i = 0} ∩ B(w, r/2).
2. For h ∈ Π, h + 2θe_i ∈ N is out of band (2θ > θ√(1 + 4θ²)), so it is strictly accepted. Hence
   P(h + 2θe_i) ≥ 0, and so P(h) ≥ −2θ.
3. Let m₀ ∈ argmin_{K_{e_i}} m·w, and let u ⊥ w be a unit vector in e_i^⊥. Then m₀·(w ± (r/2)u) ≥ −2θ and
   m₀·w = P(w) ∈ [−2θ, 0]. So |m₀·u| ≤ 4θ/r.
4. Hence the projection of m₀ onto e_i^⊥ = span{w, u} has length ≤ 2θ + 4θ/r. Since m₀ ∈ Δ,
   1 − (m₀)_i ≤ √2·|π m₀|, and the bound follows. ∎

The order θ cannot be improved to e_i ∈ K_{e_i}. Locally, K = conv{(1−δ)e_i + δe_j, (1−δ)e_i + δe_k}
with δ ≈ θ/2 meets both constraints near w but excludes e_i. CHECKED.

**Thm R_θ (PROVED).** Let K ⊆ int Δ, n = 3, and suppose some vertex v_k has a crossing in coordinate i.
Then no family f₁, f₂, f₃, concave and positively homogeneous on a neighbourhood of cl D_K∖0, satisfies
both of the following:
- (i_θ) on Γ, f_i > 0 where h_i > θ‖h‖, f_i = 0 where 0 < h_i ≤ θ‖h‖, f_i < 0 where h_i < 0;
- (ii) Σ_i p\*_i f_i = 0 on Γ.

*Proof.*
- By R10a Thm R Step 2, f_i is linear on F_k.
- The band strip {0 < h_i < θ‖h‖} ∩ relint F_k is open in v_k^⊥ and non-empty, because there is a
  crossing. f_i vanishes on it, so f_i ≡ 0 on F_k.
- But f_i < 0 on the non-empty open part {h_i < 0} ∩ relint F_k. ∎
- Strictness of the negative sign for an a.e.-signed representative follows from concavity, by R12's
  repair of Cor R1. This holds for every θ > 0, with no condition on corners or p\*.

**Lemma 5.1 (flat crossing facets; PROVED).** Assume R15's (SH) with NSI_θ in place of strict guidance,
and (DF) at p\*. Let coordinate c cross on F_k. Then:
- Γ_k h·(e_c − p\*) = 0 for all h ∈ v_k^⊥;
- moreover Γ_k ≡ 0 (first-order flat), if either θ < b_c(v_k), or (NA_w) holds near the negative part
  {h_c < 0} ∩ relint F_k.

*Proof.*
1. *Band strip.* On the band strip, c(h)_c = 0 a.e. So every cluster has ĉ_c = 0. By R15 Thm 1(b), which
   uses no guidance, the unique cluster is ∝ Γ_k h with ĉ·p\* = 0. Hence Γ_k h·(e_c − p\*) = 0 on an open
   subset of the plane v_k^⊥. By linearity (Thm 1(a)) it vanishes on all of v_k^⊥.
2. *Consequence.* So for every h ∈ relint F_k with Γ_k h ≠ 0, the cluster's zero line is line(p\*, e_c).
3. *Case θ < b_c(v_k).* For h with h_c > θ‖h‖, UVN_θ gives ĉ·q ≥ 0 on a neighbourhood V_c of e_c. That
   neighbourhood straddles line(p\*, e_c), which is a contradiction unless Γ_k h = 0.
4. *Case (NA_w).* For h with h_c < 0, UVN(b) with full half-plane charts gives ĉ·q ≤ 0 on V_c, with the
   same contradiction.
5. In either case Γ_k vanishes on an open set, hence identically. ∎

So under NSI_θ, any realisation of any target with a crossing must be **non-differentiable or
first-order flat at p\*** on every crossing facet. This is R15's escape (E1)/(E3), now forced.
Thm 4.3 shows that it does not help either.

---

## 6. Assessment

### 6.1 Answers

**(c)(1) Can NSI_θ deliver coverage of T1 or of interior triangles?**
- **No, for additive systems on decomposable domains.** The proof is complete for T1 and both norms, for all
  θ ∈ (0,1): Thm 4.3 with Prop 4.4(d), Lemma 4.2, and the T1 corollary.
- For every interior target with dim K = 2 in three worlds (Euclidean or sup norm), the same holds outside
  a finite exceptional set E(K) of θ-values where band edges are degenerate (Thm 4.3, 4.5).
- Even precise interior targets are not NSI_θ-covered. They stay covered by strict systems, since NSI_θ
  systems are an *added* class.
- Under NSI_θ, every one of the triangle obstructions either survives in a band-edge form or becomes
  vacuous (§5). But they are no longer needed.

**(c)(2) How small can θ be?** There is no "small θ" regime that helps.
- The no-go threshold θ₀(T) is the largest normalised positive stake on the target boundary. For T1 it is
  ≥ √(2/3) ≈ 0.816 at every ε (0.928 at ε = 0.3).
- For θ < θ₀(T) the chord pinning lemma meets strict reward just past the band edge (Thm 4.3).
- For θ > θ₁(T) (0.601 at ε = 0.3), Lemma 4.2 kills acceptance near the target boundary.
- The intervals overlap for T1, and for all 391 sampled triangles.
- The author's ideal, "for every θ > 0 every coherent target is covered", is false for all interior
  targets in three worlds under the norms checked.

**Ordinal (IB) preorders.**
- Lemma 4.1 and Lemma 4.2 are additive arguments: they compare + and 0 through prior-weighted sums.
- If the R11/R13 sandwich reduction extends to NSI_θ, the no-go transfers to sandwiched ordinal NSI_θ
  systems. That needs sandwiching penalties that respect the forced ties of Lemma 1.2 (CONJECTURE).
- For general (IB) preorders it is open.

### 6.2 Nearby results and leads (per the project preference: what is reachable)

1. **Theorem 3.1 is a genuine positive by-product.** In three worlds, closed choice follows from (IBU)
   alone, for every guidance order. This closes the vertex gap for Σ_T systems that R14 flagged
   (Cor 3.2).
2. **What the obstruction says about any tie-based weakening (Cor 4.6).** Near ∂D_T, ties must be
   world-wise (Σ_T-type), and each boundary point needs a strictly rewarded positive coordinate. For T1
   this forces strict guidance on a neighbourhood of ∂D_T. **So no good~silence weakening, stake-based or
   otherwise, can change the status of T1.** The decisive question remains the strict-guidance
   single-target problem of BRIEF2, with R15's residual (DF)/(ND)/(NA_w) escapes.
3. **The mirror weakening NSE_θ** ("bad ~ silence when the stake is negligible") is the one nearby
   variant not closed here. Findings (CHECKED, sketches):
   - Chord pinning holds on the *negative* band strip when the advice ranges there are {+,0}. Then UVN(a), which
     needs no band because reward is still strict, gives a contradiction for **every** θ > 0, whenever the
     target has a crossing.
   - With advice range {+,0,−} on the negative strip, the identity d·q = (1−s)d_c + s·d·p\* has
     d_c < 0. So pinning holds only on a sub-segment [s₀, 1] away from e_c, and the argument does not
     close.
   - A Lemma 4.2 analogue requires every h ∈ Γ to have a coordinate h_j < −θ‖h‖. That holds for T1 when
     θ ≲ 0.34 at ε = 0.3, the value at the foot points; the minimum over Γ was not computed.
   - The R15 flatness argument (Lemma 5.1) also applies, so NSE_θ realisations must be non-smooth at p\*.
   - Whether an NSE_θ realisation of T1 on a two-sided domain exists is open. I would not prioritise it: it trades
     strict penalty for strict reward and still has to beat the corner/box mechanism.

---

## 7. Status table

| Claim | Label |
|---|---|
| Lemma 1.2: (G_θ) for additive rankings ⇔ strict on classes and **forced** ℓ_i(good) = ℓ_i(0) on band | PROVED |
| Lemma 1.3 (modified vertex property); Lemma 1.4 (radial invariance) | PROVED |
| Prop 2.1: Bayes / Lyapunov / thm:kkm facts need no guidance | PROVED (thm:kkm re-read) |
| Prop 2.2: R1 Lemma 1.4 (interior uniqueness, splicing) under NSI_θ | PROVED |
| Prop 2.3: target prior interior, any θ (strict penalty only) | PROVED |
| Thm 2.4: chart characterisation under NSI_θ | PROVED |
| Thm 3.1: n = 3, (IBU) ⇒ (LA), (S), (C), any guidance order (Chebyshev selection) | PROVED |
| Cor 3.2: closes R14's Σ_T vertex gap (n = 3) | PROVED |
| Prop 3.3: CCIBU's quadratic selection fails under NSI_θ (explicit θ-range) | PROVED |
| Lemma 4.1: chord pinning | PROVED |
| Lemma 4.2: θ ≤ θ₁(K) | PROVED |
| UVN_θ | PROVED |
| Thm 4.3: band no-go under (B1), (B2) | PROVED |
| Prop 4.4: (B1) for θ < θ₀; (B2) outside finite E(K) (polytopes, Euclidean or sup norm); T1 has no exceptions | PROVED (T1 also NUMERICS) |
| Thm 4.5: no window (n = 3; Euclidean, sup) | PROVED |
| Thm 4.5 for n ≥ 4; other norms | CHECKED (sketch) / CONJECTURE |
| T1 formulas θ₀ = √((1+κ²)/(2+κ²)), θ₁ = κ/√(2κ²+4) (Euclidean); θ₀ = 1, θ₁ = min(1, κ/2) (sup) | PROVED (NUMERICS agree) |
| Cor 4.6: arbitrary tie regions, Σ_T-type near ∂D_T; T1 forces strict guidance near ∂D_T | CHECKED |
| V_θ: dist(e_i, K_{e_i}) = O(θ) | PROVED (sharpness of order: CHECKED) |
| Thm R_θ (no concave representative, any θ > 0) | PROVED |
| Lemma 5.1: (DF) ⇒ crossing facets flat; (DF) + (ND) inconsistent | PROVED |
| Lemma M_θ, Thm PL for θ < b_c(v); Lemma 6.1 mechanism with band-edge witnesses | CHECKED |
| Ordinal / sandwiched transfer | CONJECTURE |
| NSE_θ (mirror) | open; partial claims CHECKED |

## 8. Files (`n1py/`)

| File | Purpose |
|---|---|
| `thresholds.py` | θ₀, θ₁ (and an auxiliary edge-prior threshold, superseded by Prop 2.3) for T1 at both norms; the random part is slow, see the next row |
| `rand_check.py` | θ₀ vs θ₁ over random interior triangles (both norms) |
| `t1_arcs.py` | location of T1's band-edge endpoints (facet relint vs corner) |
