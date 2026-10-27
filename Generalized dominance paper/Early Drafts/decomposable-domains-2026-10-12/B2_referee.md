# Referee report on B2_notes.md (round 15)

**Scope.** I checked Theorem B2.1 (Lemmas 1–11, Props 10 and 12) line by line against the write-up:
- §2: setting, decomposable domains, advice ranges, charts;
- §6: (TS), walls, Thm apex, vertexfree;
- §7: Thm gm, routes I1/I2/C2;
- §7.7: the M0 reduction, Lemma ball, Prop crosspin, Prop carrying, Thm M0closed.

I also checked:
- Prop 13 and Cor B2.2;
- the residual analyses (R2) and (p\* ∉ E);
- Remark 5.3, the claimed short proof on M_U;
- the §6 audit, against I1_notes/I1_referee and M0_referee.

**Scripts.**
- `b2py/` was rerun with `python3 -I`.
  - `geom_checks.out` reproduces byte-for-byte.
  - `random_triangles.py` cannot import its sibling module under `-I`, because `-I` drops the script directory from `sys.path`. I ran it through `b2ref_py/run_random.py`, which reports "300 random all-facing triangles; failures: none", identical to the original output.
- My own checks are in `b2ref_py/ref_checks.py` (output in `ref_checks.out`), items R1–R5. They are NUMERICS: no verdict below rests on them alone.

---

## 0. Verdict in brief

**Theorem B2.1 is CORRECT.**
- All three steps the author flagged hold:
  - Lemma 9 (arcs);
  - Lemma 7 (ball estimate for line ties, including uniformity in n);
  - Lemma 11 (v_i ∈ K^i).
- Two expository gaps need repair: Lemma 9 step 3 and Lemma 7's bookkeeping.
- The scope statement "every all-facing triangle in general position" is labelled CHECKED (NUMERICS). It can be upgraded to **PROVED**: every geometric input used (G1, G2, G4–G7) holds for every all-facing triangle, with short proofs (§2 below). All-facing already implies general position.

This is a genuinely new and clean result. On **every** decomposable domain (no (LF) needed), for every strictly guiding integral field with (γ) having D_T as a Bayes model at an interior x (T all-facing), every face model at x:
- is crossing-pinned;
- contains T;
- lies in the tangent hexagon.

Moreover, x carries no apex tie and no ±-tie. This is the general-domain version of Prop crosspin plus Remark midarc, and it deserves a place in the write-up.

| Item | Verdict |
|---|---|
| Lemma 1 (lexicographic limits; K^i exist, coherent) | CORRECT (two cosmetic repairs) |
| Lemma 2 (K1), (K2) | CORRECT |
| Lemma 3 (support) | CORRECT |
| Lemma 4 (own-vertex pinning, no ball lemma) | CORRECT |
| Lemma 5 (escape ⇒ e_c ∈ K^c) | CORRECT |
| Lemma 6 (propagation) | CORRECT |
| Lemma 7 (★ for line ties) | CORRECT; GAP (expository, fixable) in the bookkeeping of J_n and in the §2 wording "filled with line ties" |
| Lemma 8 (collapse) | CORRECT |
| Lemma 9 (no vertex collapse) | CORRECT; GAP (fixable) in the justification of step 3 |
| Prop 10 (= B2.1(b)) | CORRECT |
| Lemma 11 (T1 ⊆ K^i) | CORRECT (one simplification) |
| Prop 12 (= B2.1(c),(d)) | CORRECT |
| B2.1 for all all-facing T | CORRECT; upgrade CHECKED → PROVED (§2) |
| §2 tie anatomy (fan points countable; E ⊆ lines ∪ countable; vertex-segment rule) | CORRECT |
| Prop B2.0 (M0 reduction on decomposable domains) | GAP (documentation): plausible, but the general-domain "adds up" is a new definition and the transfer is asserted, not written |
| Cor B2.2 | CORRECT at the status of Prop B2.0 |
| Prop 13 (p\* ∈ E ⇒ (R2)) | CORRECT; GAP (notation: π⁺), WRONG word ("centre"), and G9 can be proved |
| Conjecture B2.R as stated | GAP / false without (LF): an explicit (γ)-field realises (R2) when (LF) is dropped (§6). Must be restated with (LF) |
| §5 diagnosis of why Prop carrying (d) does not transfer | CORRECT |
| §6 audit (route I1 robust off p\*) | GAP: the §0 summary overstates it. TSalways, Thm apex/cuts, vertexfree(i) and the every-q chart form are not audited, and they are inputs of route I1 |
| Remark 5.3 ("shorter proof of the p\* ∈ E half of M0closed(a)") | The proof is CORRECT as an *alternative* after one bridging step (GAP, fixable). The claim that it is *shorter* is WRONG |

---

## 1. Theorem B2.1, step by step

Throughout, x = p\* ∈ Δ°, A\*(g) = A\*_x(g), "face model" is as in B2 §1, and D_{T1} is x-Bayes. By strict guidance:
- × is never in A\*(g), since D_{T1} ∈ M gives a non-× element of A(g), and × is strictly worst at every world;
- for mixed g, the advices +, 0, − have pairwise distinct world-i ranks whenever g_i ≠ 0.

### Lemma 1: CORRECT

**The lexicographic minimiser.** For each g, A(g) has at most 4 elements. Hence for s < s₀(g) the minimisers of (x+sθ)·ℓ over A(g) are the lexicographic minimisers of (x·ℓ, θ·ℓ).

**Ties occur along at most three directions.** For a ≠ b in A\*(g), ℓ(a) − ℓ(b) is not a multiple of 𝟙:
- it is strictly signed and mixed, since x·(ℓ(a) − ℓ(b)) = 0 with x interior;
- so its restriction to 𝟙^⊥ is nonzero, and {θ : θ·(ℓ(a) − ℓ(b)) = 0} is a line in 𝟙^⊥.

So the lexicographic minimiser is unique for a.e. (θ, g).

**Coherence of D^θ.**
- Polar Fubini at x applied to (γ): for a.e. θ, the Bayes models at x + sθ are unique and coherent for a.e. s.
- Along such s_m ↓ 0 they converge pointwise a.e. to D^θ, hence in measure (μ is finite).
- So D^θ is coherent (R1 Prop 3.1).

**Coherence of D^i.**
- On A\*(g), θ_i·ℓ = ℓ_i − x·ℓ = ℓ_i − const, and ℓ_i has a *strict* minimiser on A\*(g).
- So for each g, D^θ(g) = D^i(g) for all θ in a g-dependent neighbourhood of θ_i.
- Along generic θ_m → θ_i this is pointwise a.e. convergence, so D^i is coherent.

**Cosmetic repairs.**
1. Membership D^i ∈ M follows from Remark advicerange: D^i is a measurable selection of A, and A\*_x is measurable because ℓ is. It does not follow from closure in measure.
2. The brief's reading, "limits along the segments from p\* to the vertices", is also valid, but needs one more fact than Lemma 1 uses:
   - On a general domain every tie line has the form {c·q = 0}, {c′·q = 0} or {d·q = 0} with a strictly signed normal. So no tie line contains a vertex, and each meets (x, e_i) in at most one point.
   - By §2's E ⊆ (countable union of lines) ∪ (countable set), E ∩ (x, e_i) is countable.
   - Off E the Bayes model is coherent: it is a limit in measure of generic Bayes models, since the ties at q are null.
   - Hence D^i = lim_{s↓0} Bayes(x + sθ_i) directly.

   Either route is fine. Lemma 1's route (θ → θ_i) is self-contained and should be kept.

### Lemma 2: CORRECT
- **(K1).** If T1 accepts g and g_i > 0, then + ∈ A\* is world-i best, so D^i accepts. Then P_{C_i}(g) = min(P_{T1}(g), g_i), so D_{T1} ∩ {g_i > 0} = D_{C_i}. Finally, D_{K^i} ⊇ D_{C_i} a.e. implies K^i ⊆ C_i, by an open-set separation.
- **(K2).** If T1 is silent on g, then 0 ∈ A\*. If g_i > 0, the world-i best element is + or 0, never −.

### Lemma 3: CORRECT
A linear functional on e_c^⊥ that is ≥ 0 on an open set and vanishes at an interior point vanishes identically. So m₀ ∝ e_c.

### Lemma 4: CORRECT (no ball lemma, as claimed)
- **Case P_{K^c}(w) > 0.**
  - P̄_{T1}(w) > 0 because w ∈ relint F_k, so w·v_j > 0 for j ≠ k.
  - On the ball around g₁ := w − s(𝟙 − e_c), T1 is silent and K^c accepts. So {+, 0} ⊆ A\*.
  - On the part of the ball with g_c < 0, world c ranks 0 above +, so D^c cannot accept.
- **Case P_{K^c}(w) < 0.** Symmetric. Here + is world-c best on the part with g_c > 0, so D^c would accept there.

### Lemma 5: CORRECT
On the ball of Lemma 4 (built for K), A\* ⊇ {+, a} with a ≠ +. So D^c accepts exactly on the g_c > 0 half. Continuity of P_{K^c} gives P_{K^c} = 0 on the trace of the ball in e_c^⊥, and Lemma 3 applies.

### Lemma 6: CORRECT
- The witness g₀ = (g_a = 0, g_b ≫ 0, g_c = −1) works for every T ⊆ Δ°, since min_T m_b > 0.
- On B_a, |A\*| ≥ 2 and + ∈ A\*. So D^a accepts iff g_a > 0, and Lemma 3 gives e_a ∈ K^a.

### Lemma 7: CORRECT; GAP (expository)
I re-derived Prop F steps 1–4 for line ties on two-sided domains.

1. **Charts are exact half-planes near x.** For a c-tie at x, d·x = c·x − c′·x > 0.
   - On B(x, 1/n), the chart of the tied gamble h_t := g − t𝟙 is {c(h_t)·q > 0} ∩ B(x, 1/n) whenever d(h_t) > 0 on that ball.
   - If − ∉ A(h_t), the chart is {c·q > 0} globally.
   - So the J_n device is right.
2. **Nesting.** For t < t′, R(h_{t′}) ⊆ R(h_t) holds for a.e. q, by coherence of the Bayes model at a.e. q. Two half-planes in B(x, 1/n) whose boundary lines pass through the centre x and which are nested a.e. are equal.
3. **Cliff and (★).** These go through verbatim, because:
   - P(q, ·) is 1-Lipschitz in the sup norm;
   - the cliff needs only "q ∉ chart ⇒ P(q, h_t) ≤ 0" for a.e. q.
4. **Uniformity in n (author's flag): no problem.**
   - The line L(g) does not depend on n: every J_n uses the same line, since J_n ↑ J.
   - The threshold in (★) does not depend on n either.
   - Fix a concentric sub-ball B′ ⊂ B of radius r − δ′. Every fibre meeting B′ has |J(g)| ≥ 2δ′ (a.e. point of the fibre in B is tied), so it lies in G_n := {|J_n| ≥ δ′} for some n. The G_n increase to a full-measure set of fibres.
   - Any two fibres at distance < δ′ lie in a common G_N, so (★) at level N gives L(g) = L(g′).
   - A function on a full-measure subset of a connected open set of fibres that is constant on pairs at distance < δ′ is constant, by chaining.
5. **Conclusion.** An oriented line in aff Δ fixes c up to a positive factor, because aff Δ spans ℝ³. Since c has the strict sign pattern of g, the whole sub-ball has one sign pattern. A ball centred on {g_j = 0} has both signs of g_j.

**Repairs.**
- (a) Write J_n with "good" levels and essential inf/sup, as in Prop F step 3. Add the four-line uniformity argument above.
- (b) §2 point 1 and the end of Lemma 7 say "no ball … is filled with line ties". Lemma 7 proves this only for a ball filled with line ties *of one type*. That is all B2 uses: Lemma 8 and Prop 13(iii) use c-ties.
  - The mixed-type statement is plausible. Nesting across types forces c′-levels below the c/d-levels on a fibre, and all share one line. But it is not proved.
  - Either restrict the wording to one type, or add that argument.

### Lemma 8: CORRECT
- C_i ∩ ∂Δ = {e_i} holds for every T ⊆ Δ°.
- On S, A\* = {+, 0} exactly: + from T1, 0 from D^i's silence, and − excluded because it would be world-i better.
- The ball in S centred on {g_j = 0} exists for every compact co(T1 ∪ {m\*}) ⊆ Δ°: the triangle co(e_i, e_j, p) collapses onto the edge [e_i, e_j] as p → e_i.
- Lemma 7 then applies to c-ties.

### Lemma 9: CORRECT; GAP in the step-3 justification
- **Step 1.** Correct: D^a = D_{e_a} accepts g iff g_a > 0.
- **Step 2.** Correct. My checks:
  - Apex tie: R₋ = {θ·c′ > 0} ∩ {θ·d < 0}, which has angle ≤ π.
  - S = {θ·c ≤ 0, θ·c′ ≤ 0}: if c|_{𝟙^⊥} ∥ c′|_{𝟙^⊥}, then c − λc′ ∈ ℝ𝟙 and ⊥ x, so c = λc′ with λ < 0, and S is a line (null). Otherwise S has angle < π.
  - At θ_b, c_b and c′_b have opposite signs, so S contains no vertex direction.
  - d-tie: R₋ is the half-plane {θ·d < 0}, and S = ∅.
  - NUMERICS R2: 2982 random apex data, no failure.
- **Step 3.** |A_a| ≥ π is correct:
  - For θ with K(θ) ⊆ {m_a < 1 − ε}, D^θ rejects *every* g in a fixed open set N_ε near e_a − (1 − ε/2)𝟙, uniformly in such K.
  - Fubini then gives, for a.e. g ∈ N_ε, {K(θ) ⊆ {m_a < 1 − ε}} ⊆ R₋(g) mod null.
  - The increasing union over ε has measure ≤ π.

  The sentence "R₋(g_ε) ∋ θ_b, θ_c, so A_a misses G_bc and neighbourhoods of θ_b, θ_c" infers a *lower* bound on the complement of A_a from an *upper* bound. As written it does not follow.

  **Correct argument.**
  - For any g with g_a > 0 > g_b, g_c and generic θ ∈ R₋(g), D^θ rejects g. If this happens on a non-null set of such g, then K(θ) lies strictly on the negative side of ℓ_g, and e_a ∉ K(θ), because e_a·g = g_a > 0.
  - R₋(g) is an open convex cone containing θ_b and θ_c, hence containing the closed short arc [θ_b, θ_c] (which has angle < π) together with a g-dependent neighbourhood of it.
  - By Fubini over (θ, g) on the non-null orthant {g_a > 0 > g_b, g_c}, A_a misses the arc G_bc and a fixed neighbourhood of θ_b and of θ_c, mod null.
  - Equivalently, use the accept cells R₊(g) of gambles with g_a < 0 < g_b, g_c.

  Also replace "for one good g_ε" by "for a.e. g in N_ε". A single gamble's membership in a model is meaningless.
- **Steps 4–5.** Correct as written.
  - A_a ∪ A_b misses a neighbourhood of θ_c, so |A_a ∩ A_b| > 0, and A_a ∩ A_b ⊆ G_ab.
  - On A_a ∩ A_b and A_b ∩ A_c, D^θ is silent on every g with g_a, g_c > 0 > g_b. So S(g) meets two gaps in positive measure for a.e. such g, which is impossible for an arc that avoids the three vertex directions.

  The measurability of A_a should be stated: e_a ∈ K(θ) iff μ{g_a < 0, D^θ(g) = +} = 0, which is Tonelli-measurable.

### Prop 10: CORRECT
- The chain 5 ⇒ 6 ⇒ 8 ⇒ contradiction with 9 is valid.
- P_K(w) = 0 means K ⊆ {m·w ≥ 0}, touching the line.
- Concavity along h(τ) gives the arc signs.

### Lemma 11: CORRECT
- **Vertices v_k, k ≠ i.** On the corner portion of F_k where h_i > 0, P_{K^i} ≥ P_{C_i} = 0 and P_{K^i} ≤ 0 already give P_{K^i} ≡ 0 on an *open* arc; concavity is not needed. Lemma 3, run in v_k^⊥ (positive homogeneity turns the arc into an open cone of v_k^⊥), gives v_k ∈ K^i.
- **Vertex v_i (author's flag).** Correct. K^i ⊆ W_i (Prop 10), which is pointed, and e_i lies strictly in the opposite wedge. If v_i ∉ K^i:
  - a line f = 0 through v_i meeting W_i only at v_i has f ≥ δ > 0 on the compact K^i, and f(e_i) < 0;
  - the lines f = η with 0 < η < δ straddle T1 (f(v_i) = 0 < η < f(v_j));
  - so on an open set of gambles g ≈ f − η, K^i accepts g, g_i < 0, and T1 is silent, against (K2).
- **G10 remark.** This step is genuinely needed: (K1) and pinning alone do not suffice (NUMERICS G10 confirmed).

### Prop 12: CORRECT
- **Containment.** If every line through int T1 meets the closed convex K, then T1 ⊆ K, by strictly separating a point of int T1 ∖ K and translating the separating line through it.
- **No ±-ties.** T1 ⊆ K^i ∩ K^j gives D_{K^i} ∪ D_{K^j} ⊆ D_{T1}, so T1 would accept both g and −g.

### Conclusion (d) and the hypotheses
Conclusion (d) needs no extra hypothesis, since × ∉ A\*. B2.1 uses none of: (LF), (S), (C), (β), (δ), integrability beyond the definition of A\*. Only strict guidance, (γ) and D_T ∈ M are used.

---

## 2. Upgrade: B2.1 holds for every all-facing triangle (PROVED, not just CHECKED)

Let T = co{v_1, v_2, v_3} be all-facing: v_k = α e_k + β v_i + γ v_j with α, β, γ > 0.

- **(i) Corner-ray patterns.** Let f be the affine function vanishing on line(v_k, v_j), with f(v_i) > 0. Then:
  - 0 = f(v_k) = α′f(e_k) + β′f(v_i) gives f(e_k) < 0;
  - 0 = f(v_j) = α″f(e_j) + γ″f(v_i) gives f(e_j) < 0;
  - f(e_i) > 0, since f > 0 somewhere in Δ°.

  So r_{kj} has pattern (i: +, j: −, k: −). In particular no edge line of T contains a vertex of Δ, so **all-facing implies general position**.
- **(ii) Facet structure (G1, G2).** For h ∈ F_k: 0 = h·v_k = α h_k + β h·v_i + γ h·v_j with h·v_i, h·v_j ≥ 0, not both 0, so h_k < 0. By (i), along F_k from r_{kj} to r_{ki}:
  - coordinate i goes from + to −;
  - coordinate j goes from − to +.

  Each crosses exactly once in relint F_k, at distinct points, because h ≤ 0 is impossible on ∂D_T. The crossing line {m·w = 0} contains v_k and e_c (G2).
- **(iii) G5.** By (ii), e_k is strictly negative on both crossings of F_k, so it lies strictly in the opposite wedge. The wedge W_k is pointed, because line(v_k, e_i) ≠ line(v_k, e_j).
- **(iv) G6 is automatic.** The side of τ_i on which h_i > 0 always contains a whole corner portion of F_k.
- **(v) G4 and G7.** These hold for every T ⊆ Δ° (§1, Lemmas 6 and 8).
- **NUMERICS R1.** 3000 random all-facing triangles (wider sampling than `random_triangles.py`): no failure of (i)–(iii).

**Fix.** Replace "CHECKED (NUMERICS: 300 random triangles)" by "PROVED", citing (i)–(v). G3, G8 and G9 (hexagon and caps) are used only in Prop 13 and remain T1-specific.

---

## 3. §2 tie anatomy: CORRECT
- **Fan points countable.** Each g has at most one apex, and a finite measure has countably many atoms.
- **E ⊆ (countable union of atom lines) ∪ (countable set).** Correct, by the pencil argument on the three push-forwards g ↦ {c·q = 0}, {c′·q = 0}, {d·q = 0} plus apex atoms. Two distinct pencils share one dual point, and the non-atomic part charges countably many pencils.
- **Vertex-segment rule.** Correct, by the two displayed computations.
- **§3 (design of the fan).** The claimed "structure such a fan must have" (K a boundary point along d-rays; boundary curve met once by a.e. line) is not proved in the note. It is superseded by B2.1(d) and should be deleted or labelled heuristic.

---

## 4. Prop B2.0 and Cor B2.2

- **B2.0: GAP (documentation).** The general-domain definition of "adds up" (bounded strictly guiding λ_i; ν_i positive on problems with non-singleton advice range; relevant comparisons with regular X) is new.
  - N13 Prop B is indeed stated on a decomposable domain M, for (CP-a) with (FS^c).
  - Its (γ) proof (ties on the hyperplane p·w = 0 with w strictly signed) transfers verbatim.
  - Its (β) proof needs the splices X_m to be regular, so that only relevant comparisons are invoked. That is fine because Bayes models are regular under strict guidance, but it is the N19 Prop R3(a) step and must be written for the new definition.
  - Its (α) cites N11 Cor 3.2(d), which is for (CP-a); for adding up, (α) must be re-derived from T1 ∈ C_L.

  The write-up §7.7 status says explicitly that rankings that add up on general domains "have not been examined", so B2.0 must not be imported silently. **Fix:** write out (α) and (β) for the general-domain definition, or state B2.0 as CHECKED with this list of steps to do.
- **Cor B2.2: CORRECT** at the status of B2.0. The claim that the ties at p\* are exactly the oriented c-ties D_{T1} ∖ D_{K♭} follows from Prop 12, since T1 accepts every {+, 0} tie. Note that B2.2 does need B2.0, while B2.1 does not.

---

## 5. Prop 13: CORRECT, with repairs

- **(i)** CORRECT.
  - Every tie contains 0 (B2.1(d)).
  - D♭ = ∩_m D^{θ_m} a.e. over a countable dense set of generic θ: on a {+, 0}-tie, θ·c takes both signs on 𝟙^⊥, because c is mixed and c·x = 0.
  - A countable intersection of coherent open cones is convex, hence a.e. equal to its interior, which is D_K for K = cl co ∪K_m.
- **(ii)** CORRECT.
- **(iii)** CORRECT.
  - **G9 can be proved for T1.** o₁₂ = (κ, κ, 1)/(2κ + 1) lies strictly inside (v₁, e₂) and (v₂, e₁): its m₂-coordinate (1 + 2ε)/(3 + 3ε) exceeds c₀ = (1 − ε)/3 (NUMERICS R3 confirms).
  - Let g be affine and T1-positive with g(m) < 0 for some m ∈ cap₁₂ = co(v₁, v₂, o₁₂). Then g(o₁₂) < 0. Going from v₁ (positive) through o₁₂ (negative) to e₂ gives g(e₂) < 0, and likewise g(e₁) < 0. Then g(e₃) > 0. So the pattern is (−, −, +).
  - **Structure.** The tie set D_{T1} ∖ cl D_{K♭} is open, and its components correspond one-to-one to the caps that K♭ enters. Each component is connected because all the sets {P_{T1} > 0, m·g < 0}, m ∈ cap, contain points near r₁₂ + s𝟙. Different caps give disjoint components, because their patterns differ.
  - So **the ties at p\* are at most three full corner c-atoms, one per entered cap, and the face is a zonotope with at most three generators.** This is a clean structural statement and should be stated as such.
- **(iv)** P_K ≡ 0 on α ∪ α′ for every face model at p\* that accepts G: CORRECT. But the note then writes "π⁺ := P_K", while Prop carrying uses π⁺ for P_{K⁺(t)} at chord points t ∈ ℓ°, not at p\* (which may lie on several chords). **Fix:** call the quantity at p\* something else, and when applying Prop carrying (d) on M_U, add the bridge used in the proof of Thm M0closed:
  - if π⁺(h) > 0, then by N25 Thm 4.1(d) h − s𝟙 has a neighbourhood in G ⊆ D_{K_δ}, so P_{K_δ}(h) > 0;
  - hence P_{K_δ} ≤ 0 on α forces π⁺ ≤ 0, and with π⁺ ≥ 0 (carrying (c)) π⁺ ≡ 0.
- **"T1 intermediate only with one atom at each corner": CORRECT; "centre": WRONG.**
  - The generators are positive multiples of −b_k, and no two corner normals are antiparallel. So the all-accept point T1 is a non-extreme point of the face iff the normals positively span p\*^⊥ (which needs three atoms).
  - It is then *interior* to the zonotope, but it is its *centre* only when Σ_k ∫_{G_k} c dμ = 0 (example R5). Replace "at its centre" by "in its interior".
- **"That is the only place an N26.1-type ordinal tie-breaking could still matter."** Heuristic. When T1 is a vertex of the face, (R2) is not closed either. Label it as such.

---

## 6. Residual (R2) and Conjecture B2.R

**The diagnosis of §5 is correct.** On a two-sided domain:
- a c-tie of g persists along the chord L only while c′(g)·q < 0;
- beyond the apex, − is the unique minimiser;
- d-atoms with d ∝ ±b can add tied levels on L.

So Prop carrying (d)'s frozen support along the whole chord is not available.

**B2.R as stated ("(R2) is empty") is false unless (LF) is assumed.** Explicit example (NUMERICS R4 confirms the pattern claim):
- **Data.** Take m ∈ int cap₁₂, K₀ := co(T1 ∪ {m}), G := D_{T1} ∖ cl D_{K₀}. By the G9 argument above, every g ∈ G has pattern (−, −, +).
- **Domain.** A(g) = {+, 0} for g ∈ G (and {0, −} for −g ∈ G). Elsewhere A(g) is the singleton advice of D_{T1}. This is decomposable by Remark advicerange.
- **Penalties.** On G, ℓ(g, +) = 0 and ℓ(g, 0) = b := (−1, −1, 2): strictly guiding, bounded. On singleton problems the penalties are irrelevant.
- **Bayes models.** D_{T1} if q·b > 0, D_{K₀} if q·b < 0, ties on E = {q·b = 0} ∋ u. So (γ) holds, and so do (β) and (δ). D_{T1} is Bayes at u ∈ E.
- **What it realises.** Every hypothesis of B2.1 holds, every conclusion of B2.1 holds (face models: T1 ⊆ K ⊆ K₀ ⊆ 𝒲), and the configuration is exactly (R2) with one full corner atom.
- **What fails.** Only (LF), and of course (C) for ψ as a ranking. (C) is irrelevant for a supporting assessment, whose ties the original ranking breaks.

**Consequences.**
- (R2) cannot be closed by any argument local at p\*, nor by (α\*), (β), (γ), (δ). The closing must use (LF) globally, as on M_U, where UVN supplies vertex neighbourhoods.
- **Fix.** Restate B2.R as: *under (LF) at D_{T1} (and (β), (δ)), (R2) is empty.*

**A nearby target worth trying.** Prop carrying (d) should transfer verbatim if two conditions hold:
- for a.e. g in the carrying atom G, the apex lies outside Δ°, i.e. c′(g)·q < 0 on L ∩ Δ° (automatic if − ∉ A(g));
- no other tie gambles have chart lines on L.

Under these conditions the remaining inputs are:
- the two-sided form of N25 Thm 4.1(e) (frozen support) on L;
- UVN from (LF) (accepting h is in the advice range near ∂D_{T1}, so world-l ideals accept the middle-arc gamble).

That would close (R2) on every domain that is one-sided along the carrying shells. It isolates the genuinely two-sided case as the residual. I have not checked N25 Thm 4.1(e) in this setting: CONJECTURE.

---

## 7. Residual (p\* ∉ E) and the §6 audit

- **Table entries.** The entries for Thm TS (needs E ∩ B₁ = ∅), Prop edgelimits / Prop clines (limits through q ∉ E), and Lemma forcedlines / Lemma window (P = 0 at chord points off E, joint continuity at one window point q ∉ E) are a reasonable reading.
  - For forced lines one needs points of the chords {c(g_n)·q = 0} off E converging to the window point. That holds because a line that is not an atom line meets E in a countable set.
- **The §0 sentence is overstated.** "Route I1 survives every exceptional set that stays away from p\* (CHECKED audit, §6)" is not what §6 establishes. Route I1's inputs, per Table gmdeps (rows marked "all"), include several items §6 does not audit:
  - Thm TSalways and its walls 𝒲_{m₀}, 𝒜_b, which are defined through K_q at *every* q;
  - Thm cuts and Thm apex, through Cor TSalways(b),(c) and vertexfree(i);
  - the every-q chart form of Prop CF(⇒), which I1_referee §2 shows can be weakened to the a.e.-q form *plus Hausdorff continuity of K_q near the edges*. Hausdorff continuity fails at points of E, and nothing keeps E away from the edges.

  Moreover, the supporting assessment ψ satisfies (α)–(δ), not (LA), (S), (C). §6 audits only the uses of (BU), not uses of Prop necessary(b)–(c) beyond what (β), (δ) supply.
- **Fix.** Replace the §0 sentence by: "Route I1 survives an exceptional set E with p\* ∉ cl E, *conditionally on* (TS), edge confinement and K_q → {e_b} for (γ)-fields (Thm TSalways, Thm cuts/apex, Prop vertexfree(i): not audited)."
- **Further remark.** The quasi-linearity of tie-breaking families (Lemma quasilin), which carried Prop chainchords on M_U, is not available on two-sided domains. Its quasi-convexity half uses B^A_q ⊆ B^A_{q₁} ∪ B^A_{q₂}, which needs half-plane charts. Wedge charts give quasi-concavity (Lemma quasiconcave) but not that inclusion. This is the first thing a two-sided Prop chainchords must replace.

---

## 8. Remark 5.3 (short proof on M_U)

- **The argument: CORRECT as an alternative proof**, once the bridge of §5(iv) is added.
  - On M_U, K ⊇ K′ excludes K^a = {e_a}, so Lemma 9 is not needed.
  - Lemmas 1–8, 11 and Props 10, 12, 13 hold.
  - Prop carrying (c), (d) then close the case.
- **"Shorter": WRONG.** The existing p\* ∈ E proof is Prop crosspin (one ball-lemma application), Prop carrying (a)–(d), and a five-line final step. The B2 route:
  - still uses the ball lemma (in Lemma 8, and in Prop 13(iii), which is carrying (b));
  - still uses frozen support (carrying (c)), carrying (d), and N25 Thm 4.1(d) for the bridge;
  - adds Lemmas 1, 2, 4–6, 8, 11 and Prop 12.

  It is longer, and not independent.
- **What is new on M_U.** An alternative proof of Remark midarc (K ⊇ T1 for every face model), via the lexicographic limits K^i and (K2) instead of sector convexity.
- **Fix.** Say "an alternative proof, sharing the ball lemma and Prop carrying (c), (d)".

---

## 9. Recommended additions to the write-up

1. **Theorem (face models at a target weighting; general decomposable domains).** B2.1 for every all-facing T, with the §2 proofs of the geometric inputs. Status: proved, one reading (this report). Place it in §6 next to Prop crosspin. It is the two-sided generalisation of Prop crosspin and of Remark midarc, and it closes the "fan design" for (γ)-fields on every decomposable domain.
2. **Corollary (tie anatomy at p\*, T1).** The ties at p\* are exactly D_{T1} ∖ D_{K♭} (oriented), at most three full corner c-atoms, one per cap entered by K♭. The face is a zonotope with T1 at its all-accept point, which is interior iff the normals positively span. Status: proved for T1 (G9 proved in §5 above); for the ranking reading, at the status of Prop B2.0.
3. **Residual list (§8.5).**
   - Record (R2) *under (LF)*, with the example of §6 showing that (LF) is indispensable.
   - Record (p\* ∉ E) with the conditional statement of §7.
