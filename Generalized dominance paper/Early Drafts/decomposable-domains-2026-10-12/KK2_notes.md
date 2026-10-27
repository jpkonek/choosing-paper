# KK2. A complete proof of Theorem ccibu (closed choice from interior Bayes uniqueness, n = 3)

18 October 2026, round 39. The full LaTeX proof, ready for the paper, is in `KK2_ccibu.tex` in this folder. It compiles cleanly and is 7 pp. It uses no theorem names in theorem environments and writes definitions with `\coloneqq`. This note gives:
- the verdict;
- answers to the three audit points;
- a condensed proof;
- where each hypothesis and each domain property is used;
- a check of every use of ccibu.

No scripts. The argument is elementary, and no step depends on computation.

## 0. Verdict

**Theorem ccibu: PROVED as stated, with no added hypothesis.**

*Hypotheses:* n = 3; a decomposable domain; an additive ranking with integrable envelopes; penalties strictly increasing in world rank a.e.; and (BU): for every w in the open simplex, the w·L-minimiser is unique mod null sets and coherent.

*Conclusions:*
- (LA), (S), (C) hold.
- Every undominated model is coherent and is the only model with its loss profile.
- Also, C_L = U_L = {C_p : p ∈ Δ} for the explicit selection.

The CCIBU.tex argument is correct. I found no error in it; its boundary handling is right.

What was missing:
- **In the write-up's sketch:** the endpoint case of the edge face, and the countable-union persistence argument.
- **In both CCIBU.tex and the sketch:** proofs of the imported standard facts. These are: R is compact and convex; the coherent class is closed in measure; the pointwise Bayes characterisation. KK2 supplies all three with proofs.

One reader (this note). Previously: author-checked, plus N13's re-derivation of Lemmas 2–4.

## 1. The three audit points

**(i) Finite subgradients at endpoints. PROVED that none is needed.**

Relabel so the supporting weight is w = (w1, w2, 0) on an edge. Let:
- F = argmin_R w·y (a face of R);
- J = {y1 : y ∈ F} = [t−, t+];
- h(t) = min{y3 : y ∈ F, y1 = t} (convex on J).

An undominated x on F has x3 = h(x1). A finite subgradient is used **only** when t− < x1 < t+. There it always exists: the left difference quotients of a finite convex function are monotone and bounded by any right quotient. At an endpoint, h can have infinite slope (e.g. −√(t − t−)), so a support may be vertical (v3 = 0), and w + sv would stay on ∂Δ.

The endpoints are handled lexicographically instead:
- **x1 = t−:** levels (w, e1, e3), with w(s) = (w1 + s, w2, s²) > 0.
- **x1 = t+:** levels (w, e2, e3), with w(s) = (w1, w2 + s, s²) > 0. On F, y2 is strictly decreasing affine in y1.

The third level e3 gives exactly the condition x3 = h(endpoint). At vertices of Δ no subgradient is used.

**(ii) Uniqueness and coherence of directional (boundary) minimisers. PROVED (Lemma lex).**

Boundary Bayes sets M[A_w] are never claimed to be singletons. They can contain many models, including incoherent ones. What is unique is the **lexicographic** minimiser for levels (v⁰, v¹, v²) with w(s) = v⁰ + s v¹ + s² v² > 0 for 0 < s < s̄.

- *Persistence.* For each pair g there is σ(g) > 0 with argmin_{A(g)} w(s)·ℓ = Lex(g) for 0 < s < σ(g), since comparisons are signs of quadratics in s. A tie in Lex(g) persists for all s.
- *Uniqueness.* A non-null set of ties in Lex would, by a countable union over s = 1/m, give a non-null tie set at a single interior weight. That contradicts (BU), in its pointwise form (Lemma BUpoint).
- *Coherence.* The w(s_m)-Bayes models are unique and coherent. Their advice equals Lex(g) once s_m < σ(g), so they converge a.e., hence in measure, to the lexicographic model. The coherent class is closed in measure (Lemma cohclosed: Blaschke selection, plus D_K = {P_K > 0} a.e. because boundaries of convex cones are Lebesgue-null).

**How the selection is defined at boundary indices.**
- The selection index p is not the Bayes weight.
- For every p, x(p) is the Q_p-minimiser on R, with Q_p(y) = Σ p_i (y_i − a_i)² and a_i < min_R y_i.
- At an edge index, ties are broken by minimising the omitted coordinate.
- At a vertex index, x(e_i) is the profile of the unique world-i minimiser V_i.
- C_p is the unique model with profile x(p) (Lemma efficient). It is coherent because it is a lexicographic minimiser in one of Cases 1, 2, 3a–3c.

**(iii) Lower semicontinuity after the boundary tie-break. PROVED (Lemma lsc).**

If p_m → p and x(p_m) → z, continuity of (q, y) ↦ Q_q(y) gives z ∈ M_p = argmin_R Q_p. Then:
- *Interior p:* M_p is a point.
- *Vertex p:* M_p = argmin_R y_i = {L(V_i)}, a point by (G).
- *Edge p:* (y_i, y_j) is constant on M_p by strict convexity, and z_k ≥ min_{M_p} y_k = x_k(p).

So every cluster point is ≥ x(p) coordinatewise, and each x_i is lsc. Hence the sections {p : C_p ⪯_i X} = {p : x_i(p) ≤ L_i(X)} are closed for **every** X ∈ M. The map x(·) need not be continuous; upper semicontinuity of x_k can fail at edges, which is harmless.

## 2. Condensed proof (lemma numbering as in `KK2_ccibu.tex`)

1. **Lemma pointwise (2.1).**
   - Every measurable selection s of A defines an evaluable model X_s, by (D).
   - X minimises v·L over M[A′] iff a_X ∈ argmin_{A′} v·ℓ a.e., for any v of any signs. The proof swaps in the measurable minimiser `first(argmin)`; the integrable envelope makes the difference integral finite.
   - Different advice on a non-null set gives different models.
2. **Lemma R (2.2). R = L(M) is compact and convex.**
   - Relaxed selections θ ∈ L^∞(μ)^4 form a weak-* compact convex Θ.
   - T(θ) = Σ_a ∫ θ(·, a) ℓ(·, a) is weak-* continuous, so T(Θ) is compact and convex and contains R.
   - An extreme point of Θ ∩ T⁻¹(y) (Krein–Milman) is {0,1}-valued. Otherwise, split a non-null set where two advices both have weight > 1/j into 4 non-null pieces (nonatomicity); 4 vectors in ℝ³ are dependent, so θ* is a midpoint.
   - This is Lyapunov's theorem in bang-bang form.
3. **Lemma cohclosed (2.3).** Coherent models are closed under convergence in measure.
4. **Lemma support (2.4).** An undominated x has a supporting w ∈ Δ, because R + [0,∞)³ is convex.
5. **Lemma BUpoint (3.1).** Under (BU), A_w(g) is a singleton a.e. for each interior w.
6. **Lemma lex (3.2).** Lexicographic minimisers are unique and coherent (see §1(ii)).
7. **Lemma vertex (3.3).** Under (G), ℓ_i(g,·) is injective on A(g), so V_i is the unique L_i-minimiser. It is coherent by Lemma lex with levels (e_i, 𝟏, 0).
8. **Lemma efficient (3.4).** An undominated x is lexicographic for:
   - (w, 0, 0) if w is interior;
   - (e_i, 𝟏, 0) at a vertex;
   - on an edge: (w, (−λ, 0, 1), 0) if t− < x1 < t+; (w, e1, e3) if x1 = t−; (w, e2, e3) if x1 = t+.
   Hence x has a unique realiser, and it is coherent. These cases exhaust Δ because n = 3.
9. **Lemma select (4.1).** x(p) is well defined and undominated, and no y ∈ R is strictly better on all of supp p (Q_p is strictly monotone in the supported coordinates on R).
10. **Lemma lsc (4.2)**, as in §1(iii).
11. **Theorem.**
    - C_p ∈ C_L gives (LA).
    - Competitiveness on supp p holds by step 9, since the world orders are complete.
    - Closed sections follow from step 10, giving (S).
    - (C) and the uniqueness of loss profiles follow from step 8.
    - Every undominated model equals some C_p, by KKM (write-up Thm kkm) and step 8.
12. **Remark reindex.** Every interior Bayes model is C_p for p_i ∝ w_i/(x_i − a_i).

## 3. What is used where (PROVED, by inspection of the proof)

| Property | Used in |
|---|---|
| (D): M is all measurable models with advice in A (follows from splice closure + closure in measure, write-up rem:advicerange / Hiai–Umegaki) | evaluability of selections; pointwise Bayes characterisation (splicing a minimiser in on a set); evaluability of the pure selection in Lemma R; the lexicographic model and the subdomains M[A^k] |
| splice closure alone | only through (D) |
| closure in measure alone | only through (D). The lexicographic model is evaluable directly by (D), and is also a limit of evaluable B_m |
| nonatomicity of μ | **Lemma R only** (convexity and closedness of R) |
| convexity of R ("Lyapunov convexity") | supporting weight (Lemma support); convexity of h (Case 3); uniqueness of x(p) and constancy of (y_i, y_j) on M_p (Lemma select); hence lsc; Remark reindex |
| compactness of R | existence of a_i, of min Q_p and of the fibre minima h(t); cluster points in Lemma lsc |
| integrable envelope | finite L; pointwise characterisation; weak-* continuity of T |
| μ finite, Lebesgue null sets, symmetric null sets | Lemma cohclosed (∂ of convex cones null; dominated convergence); Lemma lex(b); Lemma pointwise(c) |
| (BU) | Lemmas BUpoint and lex; Case 1 |
| (G) strict guidance | **Lemma vertex only**: Case 2 of Lemma efficient and the vertex indices of the selection. Cases 3b and 3c do **not** need (G) in this version; CCIBU.tex used (G) there |
| n = 3 | the case list of Lemma efficient; the one free coordinate in Lemma select(ii) |

**Not used:**
- (LF);
- any property of the target;
- that coherent models avoid ×;
- the indexing of pairs. Any measure-preserving re-indexing, e.g. JJ3's majority orientation, is harmless.

## 4. Check of every use (CHECKED: the hypotheses of ccibu are met in each; nothing extra is needed)

Since no hypothesis is added, each use is valid provided its object satisfies four things: integrable envelope, (G) on the whole advice range including × where × is present, a decomposable domain, and (BU). I checked each against its source text. I did not re-verify the sources' own derivations of (BU).

| Use | Envelope | (G) | (BU) | Verdict |
|---|---|---|---|---|
| **Prop CF(⇐) / Cor CFnone** (gm's reduction to CF(T1)) | per-pair rescaling, e.g. by 1/(1 + max\|ℓ\|), keeps the argmins | R1 Prop 2.1 (converse): c has the sign of g, c′ of −g, which is exactly (G) on {+,0,−} | "tie sets in ±∂D_{K_q}" (N28; not re-verified here) | OK. **Wording repair needed:** the text says "advice ranges {+,0,−}" but also "on the all-model domain". Either state the cover on the domain of models never giving ×, which is decomposable and satisfies (LF), or add ℓ_i(g,×) ≔ E(g) + 1. Then × is strictly worst, the envelope E + 1 is integrable, and × is never w-Bayes for any w ∈ Δ, so (BU) is unchanged. Either way ccibu applies |
| **Cor realisation** ("if" direction) | assumed | assumed | assumed | OK |
| **INTERSECTIONS transfer theorem** (ψ = Σ w_k L^k) | Σ w_k ‖h^k‖₁ < ∞ gives envelope Σ w_k h^k ∈ L¹ and a.e. absolute convergence | positive combination of strictly guiding penalties | Steps 3–4 | OK. D_K is Bayes at an interior p* (Step 6), so it is in C_ψ |
| **JJ3 Thm 5.1** (Φ′) | Prop 3.3 (δ ≤ E) | Prop 3.3, with × strictly worst by Lemma 1.1(b) | Prop 3.3 / Thm 2.1 | OK. T1 = B′_{w*} with w* interior, so it is in C_{Φ′} |
| **JJ2 Thm 5.5, alternative route** (Φ′) | stated | "strictly guiding and strict-best" | Lemmas 4.1, 4.3 | OK |
| CCIBU Cor sandwich; write-up M3 remark; branch E = ∅ of §M0 (ψ on M_U) | ρ_i ∈ L¹ | error penalty ρ_i > 0 on {+,0} | (γ) with E = ∅ | OK |

## 5. Consequences

1. **Status upgrades.** ccibu becomes PROVED (KK2; complete proof; one reader). Every result stated "at the status of Theorem ccibu" now holds at the status of its other inputs:
   - Prop CF(⇐), Cor CFnone, Cor realisation (if direction), Prop vertexfree for bare CF solutions, the C1 statement for CF solutions;
   - INTERSECTIONS (at gm's status);
   - JJ3 Thm 5.1 and JJ2 Thm 5.5 (modulo gm and their own lemmas);
   - the E = ∅ branch of §M0.
2. **JJ2's bypass is no longer needed for correctness.** Whether gm's routes use a cover only through Prop necessary is now a question of economy, not validity (KK1's task).
3. **Suggested replacements in the write-up.**
   - Replace the proof sketch of thm:ccibu by `KK2_ccibu.tex` §§2–5. Write-up labels used there: rem:advicerange, thm:kkm.
   - New status line: "proved (KK2; complete proof including the boundary cases; one reader). Earlier: author-checked (CCIBU.tex), Lemmas 2–4 re-derived in N13. Specific to three worlds."
   - Fix the × wording in Prop CF(⇐) as in §4.
4. **Scope.** Additive rankings, n = 3 (Remark ngeq4). Nothing is claimed for n ≥ 4, for (IB) preorders, or for weakened guidance. With weak guidance, Lemma vertex can fail: an e_i-face that is not a point has no coordinatewise-least element in general, which breaks lsc at vertex indices. Lemma efficient survives in Cases 3b and 3c.

## 6. Labels

- Theorem ccibu and all of its lemmas: **PROVED** (`KK2_ccibu.tex`).
- §3 usage table: **PROVED** by inspection.
- §4 hypothesis checks: **CHECKED** against the cited notes. Their internal derivations of (BU) were not re-verified.
- Remark ngeq4: an observation, not a claim.
