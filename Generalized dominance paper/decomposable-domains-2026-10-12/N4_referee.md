# N4: referee report on the NSI_θ no-go notes N1, N2, N3

13 Oct 2026. Independent referee; I did not write N1–N3. Every step listed below was checked against
BRIEF.md, BRIEF2.md, BRIEF3.md and, where cited, R10b/R11. My own numerical checks are in `n4py/check.py`
(evidence only). I reran `n2py/geometry.py` and `n3py/thresholds.py`; their outputs match what the notes
report.

Verdicts: **CORRECT** / **CORRECT WITH REPAIR** (the conclusion holds but the statement or proof needs
the stated fix) / **GAP** (the conclusion is not established) / **FALSE**.

---

## 0. Bottom line

* **Under BRIEF3's definition (forced ties), "NSI_θ covers T1 for no θ > 0" STANDS for additive rankings
  on decomposable domains.** This covers both norms and every ε ∈ (0,1), and in fact ε-contamination of every
  interior baseline in every n ≥ 3. The class means additive penalties with integrable envelopes
  satisfying (LA), (S), (C), hence (IBU), with (LF) at the target.
* **Two independent complete proofs exist:**
  * N2 Cor C1 (via Thm B and Thm C);
  * N1 Thm 4.3 + Prop 4.4(d) + Lemma 4.2 + the explicit inequality θ₁(T1) < θ₀(T1) (Euclidean), or
    θ₀ = 1 (sup).
* N3 Thm ST gives a third proof under (NA). Its own proof yields more than N3 states (see §4).
* **Scope limits that must be stated with the conclusion:**
  * (i) It is proved only for additive (or, plausibly, countably sandwiched) rankings, not for general
    (IB) preorders.
  * (ii) It concerns the forced-tie reading of BRIEF3. Under a "ties permitted" reading the class contains
    all strict systems, and T1's status is the strict problem, which is still open.
  * (iii) NSI_θ systems form an added class, so T1's strict-guidance status is untouched.
* **Nothing is FALSE in a way that affects the T1 conclusion.** The non-CORRECT items are listed in §6.

---

## 1. Forced ties and ray transport

**Forced ties: N1 Lemma 1.2, N2 Lemma 0, N3 Lemma 1. CORRECT.**
* Let E ⊆ Band_i be measurable with good and 0 both in A(g) on E. The splices X (good on E) and Y
  (0 on E) are in M_L, because M_L is a decomposable domain (closed under splicing).
* In the coarse order of BRIEF3, X and Y lie in the same rank class at world i on every pair. So weak (G)
  gives both X ⪯_i Y and Y ⪯_i X.
* Additivity then gives ∫_E (ℓ_i(good) − ℓ_i(0)) dμ = 0 for every such E. Hence ℓ_i(good) = ℓ_i(0) a.e.
  on Band_i ∩ {both in the advice range}.
* The strict parts are R1 Lemma 1.1.
* Remarks:
  * The tie is forced only where both kinds of advice are in the advice range. Off N, singleton advice ranges impose nothing.
    Inside N, (LF) always supplies + and 0. All three notes use it only there.
  * The result depends on reading BRIEF3's "tied in the guidance order" literally. That reading is the
    text of BRIEF3.

**Pencil and ray transport: N1 Lemma 1.4, N2 Lemma 1. CORRECT. N3 §1(a): CORRECT under its stated
hypothesis.**
* Let h be band-i⁺. Then c_i(h) = 0, and d_i(h) > 0 because good vs bad is never tied.
* For advice range {+,0}:
  * R(h) = {c·p > 0} is a half-plane whose boundary line passes through δ_i.
  * Since c·((1−s)δ_i + sp) = s·c·p, acceptance is constant along every ray from δ_i.
* For advice range {+,0,−}:
  * R(h) = {c·p > 0} ∩ {d·p > 0}. This is a wedge with δ_i on the c-line and inside {d > 0}. It is
    star-shaped about δ_i, not a half-plane.
  * "Accepted at p" propagates to (δ_i, p], via d·q = (1−s)d_i + s·d·p and c′_i < 0.
  * "Silence at p" (c·p < 0) propagates to the whole ray.
  * Beyond p, away from δ_i, acceptance may switch to −h.
* Both N1 and N2 state exactly this one-sided version, and the downstream proofs use only that.
* Minor wording repair: N2's sentence "a band-i⁺ chart is a union of rays from δ_i" is literally true only
  for advice range {+,0}. For advice range {+,0,−} read "star-shaped about δ_i".
* N3's "cevian half-plane" claim is made only for advice range {+,0} or under (NA), and is correct there.

---

## 2. N2

**Lemma 2 (vertex pull). CORRECT.**
* For a mixed x ∈ C_θ(i) with + in the advice range, c_i > 0 and d_i > c_i > 0 (since c′_i < 0). So δ_i satisfies the
  defining strict inequalities of R(x) for every advice range. × is never optimal.
* The measurable radius r(x) > 0 and the exhaustion E = ∪{r ≥ 1/k} give E′.

**Theorem B (band–hull obstruction; any n ≥ 3, any norm). CORRECT.** I checked every step:
* Step 1 needs a.e. uniqueness at p\*, (LF) inside U, c_i = 0 on U, and −U ∩ cl D = ∅. The last gives
  −h ∉ B_{p\*} a.e. and so licenses Lemma 1(b).
* Step 2 uses "an open convex set containing a.e. point of an open set contains it": separate a missing
  point and get a non-null exterior piece. The nonnegative orthant part of D_{K_q} does not meet U.
* Step 3 is an elementary estimate: m·y < −λ₀|m·x|/2.
* Only interior Bayes models are used, plus the target prior. The x (whose acceptance is in the advice range) need not be near w, which
  makes this stronger than N1's local version.

**Cor B1. CORRECT.** x = w′ − s𝟙 lies in N ∩ C_θ(i) with m·x = −s < 0, because m ∈ Δ.

**Theorem C (facet crossings). CORRECT** for θ ∈ (0,1), with the sup or Euclidean norm, n ≥ 3. The
θ ≥ 1 remark is also correct.
* The three cases are exhaustive.
* Case 1 reduces to Cor B1 by the intermediate value theorem on the connected set relint F_m.
* Case 2 is the positivity argument: c ≤ 0 with c_j < 0, so the point is rejected at every interior prior.
* Case 3:
  * Euclidean: a quadratic form vanishing on an open subset of m^⊥ vanishes on m^⊥, and m^⊥ ∩ e_i^⊥ ≠ 0.
  * Sup norm: a single minimising j₀ exists on an open subset, because {h_j = h_k} ∩ m^⊥ is a proper
    subspace when m ≫ 0. Then m ∝ e_i + θe_{j₀} is impossible.

**Cor C1 (ε-contamination of every interior baseline, every θ, both norms, n ≥ 3). CORRECT.**
* relint F_k = {v_k·h = 0, h_k < h_j ∀ j ≠ k} is right.
* The witnesses (a) and (b) are right algebraically. `n4py/check.py` §2 verifies them for 6000 random
  (p, ε, i, k) with n = 3, 4, 5, with 0 failures.
* K is full-dimensional, so −h ∉ cl D on relint F_k.
* `n4py/check.py` §3 also checks the case split of Thm C on a θ-grid for T1. Every θ falls into case 1 or
  case 2 on every (F_k, i) in both norms.

**Cor C2 (upright triangles, every θ). CORRECT.**
* The sign of (r_e)_i is the side of line(e) on which e_i lies.
* If i were positive on all three edge rays, then e_i ∈ K, which is impossible. So i changes sign on F_k
  or on F_j, and Thm C applies.
* The 87% figure is NUMERICS. I reproduced it: 17398 of 20000.

**Prop C3 (inverted triangles above θ_cap). GAP as a proof; immaterial.**
* The sketch does not establish the "exceptional configuration" list. In particular, "positivity near r
  forces the rest" is not argued.
* It is labelled CHECKED, but I would label it CONJECTURE. It is consistent with N1's finite exceptional
  set (see §5) and plays no role in T1.

**Theorem Z (θ < θ_cap(K) excluded; every interior full-dimensional K, any n ≥ 3, any norm). CORRECT.**
* Step 2 is the right compactness repair of Cor B1 for non-polytopes: contacts m_k → m\*, and
  m\* ∉ cap ⇒ some h ∈ C_θ(i) has m\*·h < 0.
* The estimate x_i − θ‖x‖ ≥ s(h_i − θ‖h‖) is the triangle inequality.
* Step 3 checks out:
  * C_θ(l) ∩ B is convex and misses ∂D, so it lies in D or in the complement of cl D.
  * Some l recurs along a shrinking sequence of balls.
  * The local-to-global segment argument gives μ ∈ cap_θ(l).
* The formulas for cap_θ(i) are correct:
  * Euclidean: half-angle arcsin θ about e_i, the dual of the round cone of half-angle arccos θ;
  * sup norm: m_i ≥ 1/(1+θ), obtained by dualising the generators (θ, ±1, ±1).
* θ_cap(T1) is correct: sup 2(1−ε)/(1+2ε); Euclidean 0.774 / 0.526 / 0.249 / 0.050 at ε = 0.05 / 0.3 /
  0.6 / 0.9 (rerun).

**"General principle" (§7). CORRECT WITH REPAIR.**
* The precise, proved content is the tie-region version of Thm B. It goes through verbatim, since Lemma 1
  needs c_i = 0 on a ball around w and Lemma 2 needs c_i > 0 at x. Stated precisely: an obstruction
  arises when
  * a target-boundary point w lies in int R_i (the tie region at world i), with −w ∉ cl D, and
  * a contact m of w is cut (m·x < 0) by an x in int({h_i > 0} ∖ R_i) whose acceptance is in the advice range.
* Σ_T escapes *this* mechanism, because it has no strict side at worlds of T. That is all that is shown.
* Two overstatements need repair:
  * (a) "Any partial indifference within a world is harmful" holds only when the tie/strict interface
    meets the target boundary in the configuration above. A tie region bounded away from ∂D does
    nothing to that target.
  * (b) "Total indifference at a world is not harmful" is false as a general statement. The positivity
    obstruction (Thm C case 2; N1 Lemma 4.2; N1 Cor 4.6(ii)) still applies. For T1, Σ_T with any T ∋ c
    fails, because ∂D_{T1} has points whose only positive coordinate is c.
* Restate both as "this obstruction requires an interface; Σ_T avoids it but not positivity".

---

## 3. N1

**Lemma 4.1 (chord pinning). CORRECT.** This is the same mechanism as N2 Thm B, Step 1.
* The touching step is right: P_{K_q}(h′) = 0, then local-to-global, then
  m ∈ (cl D_K)\* ∩ Δ = K.

**Lemma 4.2 (θ ≤ θ₁). CORRECT.** It is identical to N3 Prop A and N2 Thm C case 2.

**UVN_θ. CORRECT.** It is R10b UVN(a) with the ball B₀ inside {h_c > θ‖h‖}. Dominated convergence and the
half-ball argument are unchanged.

**Theorem 4.3 (band no-go under (B1), (B2)). CORRECT.**
* For x = h₀ + tk, β(x) > 0 for small t by the definition of the one-sided derivative.
* Then m₀ ∈ K_q along the chord (K_q is closed), and m₀·x < 0 contradicts UVN_θ near e_c.
* Remark: (B2) holds whenever m₀ ∉ cap_θ(c). Take k ∈ C_θ(c) with m₀·k < 0; superadditivity of β gives
  β′(h₀; k) ≥ β(k) > 0.
* In the Euclidean norm, (B2) fails iff m₀ ∝ e_c − θĥ₀. That vector lies on the boundary of
  cap_θ(c): its angle with e_c is arcsin θ. So N1's exceptional θ-values are always ≥ θ_cap(K),
  consistent with N2 Thm Z.

**Prop 4.4.**
* (a) **CORRECT.** Smooth points are dense in the relatively open band arc, and the contacts converge on
  a subsequence.
* (b) **CORRECT.** By a Gordan alternative, (B2) fails iff m₀ = λ(e_c − θĥ₀); with m₀ = v this forces
  θ = R_{v,c} = |π_{v^⊥}e_c|.
* (c) **CORRECT.** The superdifferential argument in the sup norm forces h₀ ∝ (θ, −1, −1).
* (d) **CORRECT.**
  * Euclidean: follow F_k from its c-zero toward the foot of e_c. The first band-edge point lies in
    relint F_k, and θ < R = θ₀.
  * Sup norm: (θ, −1, −1) ∈ v_k^⊥ would need θ = 2 + ε/a > 1.
* **GAP (scope):** §0 item 5 and §6.1 ("every interior target with dim K = 2 … outside a finite exceptional
  set E(K)") are proved only for polytopes. For curved K, finiteness of the set of θ at which (B2) fails
  at every available band-edge point is not shown. N2 Thm Z covers θ < θ_cap for every K. The residual
  range for non-polytopes is θ ∈ [θ_cap, θ₀) with (B2) failing.

**Theorem 4.5 (no window).**
* Euclidean, n = 3: **CORRECT.**
  * The local identification D_K = C₁ near h¹ uses Lemma 4.2 and invariance of domain on the curve
    Γ ∩ S².
  * Following ∂C₁ gives either a reflex junction with ∂C₃ (θ < 1/√2) or D_K = C₁ (θ ≥ 1/√2,
    contradicted by e₂). The tangency at θ = 1/√2 is handled.
  * It holds for general convex K, not only polytopes.
* Sup norm: **CORRECT WITH REPAIR.**
  * The stated consequence "θ₁(K) < θ₀(K)" is **false** in the sup norm. For T1 with ε ≥ 1/4,
    θ₀ = θ₁ = 1; random sup-norm triangles also attain θ₀ − θ₁ = 0 (`n4py/check.py` §4).
  * Correct statement: no θ ∈ (0,1) satisfies θ₀ ≤ θ ≤ θ₁. In the sup norm this is trivial, since
    θ₀ = 1 for every interior K (that claim is correct: take h = e_c − t₀(𝟙 − e_c) with
    min_K m_c ≤ 1/2).
  * §0 item 6's "θ₁ < θ₀ always … sup norms" should be amended accordingly.
  * Nothing downstream changes, because θ ≥ 1 is excluded separately.
* n ≥ 4: a sketch only, correctly labelled CHECKED.

**T1 formulas. CORRECT** in both norms. With κ = (1+2ε)/(1−ε):
* Euclidean:
  * θ₀ = √((1+κ²)/(2+κ²)), attained at the foot of e_c on v_k^⊥. That foot lies in relint F_k, since
    h_k = −ab/|v|² < h_j = −a²/|v|².
  * θ₁ = κ/√(2κ²+4), attained at the facet midpoint. On F_k the function max(h_x, h_y)/‖h‖ is minimal at
    the midpoint, not at the corner.
* Sup norm: θ₀ = 1 and θ₁ = min(1, κ/2).
* The inequality θ₁ < θ₀ (Euclidean) is equivalent to κ² < 2 + 2κ², which always holds.
* Numerics agree to grid accuracy (`n4py/check.py` §1).

**Thm 3.1 (closed choice from IBU, any guidance order, Chebyshev selection). CORRECT,** modulo the
cited R14 Lemma B2(i), B4 and Thm A (refereed CORRECT in R17).
* Efficiency: a least-norm point of the Chebyshev argmin, with y − a > 0 on R. Competitiveness on
  supp q is immediate.
* Active-set trichotomy: in |I| ≥ 2 cases B(q) is a point or an axis-parallel segment, so a least element
  exists and equals σ(B(q)).
* V_i is open. B is Hausdorff-continuous on V_i by Slater plus closed graph. Berge applies with a strictly
  convex objective.
* Lower semicontinuity off ∪V_i follows from upper hemicontinuity and the least element.
* Wording repair: the selection is constant (= σ(F_i)) only on the smaller neighbourhood of e_i where the
  constraints y_l ≤ c_l(q) are inactive on F_i. This happens because c_l(q) → ∞ as q → e_i. On the rest
  of V_i it is only continuous. The proof uses only continuity.

**Prop 3.3 (CCIBU quadratic selection fails). CORRECT.** For T1 at ε = 0.3, 0.916 = b/√(a²+b²) with
w = (0, b, −a) ∈ F_k.

**Precise targets (§6.1, "even precise interior targets are not NSI_θ-covered"). GAP (unsupported).**
* Lemma 4.1 needs U ∩ (−cl D_K) = ∅. For K = {p\*}, Γ = p\*^⊥∖0 = −Γ, so every boundary point
  violates it.
* N1's remark about the precise *family* K_p ≡ {p} does not exclude a precise *target*.
* N2 §6 correctly lists precise targets as open. N1 should be corrected to "open".

---

## 4. N3

**Prop A (θ_A ceiling). CORRECT.**
* θ_A(K) equals N1's θ₁(K).
* The T1 closed forms are correct:
  * sup: min{1, (1+2ε)/(2(1−ε))};
  * Euclidean: (1+2ε)/(√2·√(2(1−ε)²+(1+2ε)²)).
* The Euclidean form equals κ/√(2κ²+4). The rerun matches to 5 digits at seven values of ε.

**Thm PL_θ. CORRECT** (transfer).
* I checked against R10b §5 the steps that use strictness:
  * Lemma M Step 4 needs (a₋)_c ≤ 0, which is strict penalty and kept.
  * It also needs (a₊)_c > 0 via UVN(a) at w₊, which needs (w₊)_c > θ‖w₊‖ and is supplied by
    θ-robustness.
  * Thm PL needs UVN(a) at world j on cl U, supplied by h_j > θ‖h‖ on A.
* Lemma D's collar argument works on tubes that meet no other facet, since D_K = {v·h > 0} locally there.
* Steps 1–3 use R4 Thm B, i.e. d, which is still strict.
* Prop S is CORRECT, and its T1 application is correct (y leads on [w⁰, s_k]).
* The random-triangle statements are NUMERICS/CONJECTURE. My rerun of `n3py/thresholds.py` shows
  coarse-grid cases with θ_PL < θ_A (33 in sup, 43 in Euclidean). N3 attributes these to grid
  artefacts, which I did not verify.
* This does not affect T1, and PL_θ is superseded by N1 Thm 4.3 and N2 Cor C1, which need no plateau.

**Thm ST (cevian transport, under (NA)). CORRECT; conclusion understated.**
* With a *single* prior q₁ ∈ Π_U, the signs of ρ(h) − r₁ are fixed a.e. on U⁺ and on U⁻. So every prior
  on the whole cevian through e_y and q₁ lies in Π_U.
* Steps 4–6 then give a contradiction near e_y. Hence **Π_U = ∅**.
* Since p\* ∈ Π_U whenever D_K = B_{p\*}, Thm ST already shows that T1 is not Bayes at any interior prior
  (under (NA)), not merely that it has no plateau. Cor ST2 is therefore vacuous.
* (NA) can be removed by the one-sided transport of N1 Lemma 1.4 / N2 Lemma 1. That is exactly N2 Cor B1
  applied to F_v. So the open item "θ = θ_A without (NA)" is closed by N2.

**Prop 2 (no concave chart fields). CORRECT.** A concave function that vanishes on an interval and is
positive beyond it is impossible.

**Thm CC_θ (closed choice via vertex blow-up). CORRECT,** modulo CCIBU's interior and edge lsc lemmas and
R14 Thm A.
* ρ is continuous and agrees with the identity on {p_i = 1−δ}, where λ = p_j/δ.
* ρ maps N_i onto the cut segment, which ψ sends to the arc Θ_i (support {i}). So
  supp σ(p) ⊆ supp p. Competitiveness on smaller supports is the stronger property, so the direction is
  right.
* The arc limits are correct. G_{r_m}(x_m) ≤ G_{r_m}(y\*) follows from x_{m,i} ≥ m_i. The relint
  limit is unique by strict convexity. At the endpoint, the lexicographic rule gives lsc.
* Arc values are efficient.

**Consistency of the two closed-choice results.**
* They agree. N1 uses the Chebyshev selection, which is locally constant at vertices. N3 uses CCIBU's
  quadratic selection plus blow-up.
* N3's "no single value at e_i is lsc" refers to CCIBU's interior quadratic selection, and agrees with
  N1 Prop 3.3.
* Neither selection is needed for the T1 no-go.

---

## 5. Consistency between the notes

* **Thresholds agree.**
  * N1's θ₁ is the same quantity as N3's θ_A, with identical closed forms in both norms.
  * N2's θ_cap is a different and smaller quantity. In the Euclidean norm on 586 random interior
    triangles, max(θ_cap − θ₀) = −0.19. For T1, θ_cap < θ₀ at every ε checked.
  * N1 excludes θ < θ₀ (given (B2)) and θ > θ₁. N2 Thm Z excludes θ < θ_cap with no (B2), for every K,
    every n ≥ 3 and every norm. N2 Cor C1 excludes every θ for contamination targets.
  * N1's exceptional values satisfy θ ≥ θ_cap (§3, remark on Thm 4.3), so the two results interlock.
* **T1 verdicts agree:** every θ is excluded, in both norms, by N1 and by N2. N3 agrees, and after the
  §4 strengthening it gives the same full exclusion under (NA).
* **One disagreement:** precise targets (N1 says "not covered", N2 says "open"). N2 is right; see §3.
* **Minor:** N1's no-window statement is false in the sup norm as written (§3). Nothing depends on it.

**Use of priors and models outside the axioms. None found in the main results.**
* The no-go arguments use only the following:
  * interior Bayes models B_q (pointwise minimisers over the advice ranges, so they lie in M_L), with a.e. uniqueness and
    coherence from (IBU). (IBU) follows from (LA), (S), (C) by R1 Lemma 1.4 / N1 Prop 2.2, and BRIEF2
    requires it in any case;
  * the target prior p\*, which is interior by N1 Prop 2.3 (CORRECT; it uses strict penalty only);
  * (LF) advice ranges inside N.
* No boundary-prior Bayes model, no vertex model, no selection, and no imported regularity ((DF), (NA),
  (H0), (H1)) enters N1 Thm 4.3, N2 Thm B/C/Z, or Cor C1.
* N3 Thm ST uses (NA) as an explicit, removable hypothesis.
* Vertex models appear only in N1 V_θ (not used) and in N3's design (§3), which is a hypothetical, not
  an argument.

**Ordinal extension (not claimed by the notes; my assessment).**
* The no-go uses only (IBU), an interior target prior, and the sign and tie pattern of an additive field.
* R11 Lemma K and Thm W(a) use (W) and (R) and no guidance. Thm W(d) uses strictness only for a strict
  *penalty* step, which NSI_θ keeps. The aggregate ψ inherits the forced ties through (W).
* So the transfer to countably sandwiched NSI_θ systems looks routine, but it is not written.
  CONJECTURE (likely). General (IB) preorders: open.

---

## 6. Items that are not CORRECT

| Item | Verdict | Repair or comment |
|---|---|---|
| N2 Lemma 1 wording ("union of rays") | CORRECT WITH REPAIR | For advice range {+,0,−}: star-shaped about δ_i; proof unaffected |
| N2 §7 "general principle" | CORRECT WITH REPAIR | Interface harmful only when it meets ∂D as in Thm B; Σ_T escapes Thm B but not positivity (fails for T1) |
| N2 Prop C3 | GAP (sketch) | Relabel CONJECTURE; immaterial |
| N1 §0.5 / §6.1, finite E(K) for every dim-2 interior K | GAP | Proved for polytopes only; curved K open on [θ_cap, θ₀) |
| N1 Thm 4.5, "θ₁ < θ₀" in the sup norm | CORRECT WITH REPAIR (statement false as written) | θ₀ = θ₁ = 1 occurs (T1, ε ≥ 1/4); restate as "no θ ∈ (0,1) in [θ₀, θ₁]" |
| N1 §6.1, precise targets "not covered" | GAP (unsupported) | Lemma 4.1 fails for K = {p\*}; status open (as N2 says) |
| N1 Thm 3.1 remark "constant on V_i" | CORRECT WITH REPAIR | Constant only near e_i; continuous on V_i |
| N3 Thm ST / Cor ST2 | CORRECT, understated | One prior suffices: Π_U = ∅, so T1 is not Bayes at all under (NA); (NA) removable via N2 |
| N3 random-triangle claims (θ_PL ≥ θ_A, etc.) | NUMERICS only | Rerun shows coarse-grid exceptions; not verified as artefacts |

Everything else asked about is **CORRECT**:
* N1 Lemma 1.2, Lemma 1.4, Lemma 4.1, Lemma 4.2, UVN_θ, Thm 4.3, Prop 4.4, the T1 formulas, Thm 3.1,
  Prop 3.3, Prop 2.3;
* N2 Lemma 0, Lemma 1, Lemma 2, Thm B, Cor B1, Thm C, Cor C1, Cor C2, Thm Z;
* N3 Lemma 1, Prop A, Prop 2, Thm PL_θ, Prop S, Thm CC_θ.

## 7. Files

* `n4py/check.py`: independent checks.
  * §1: T1 θ₀, θ₁, θ_cap in both norms against the closed forms.
  * §2: Cor C1 witnesses, n = 3, 4, 5.
  * §3: Thm C case coverage on a θ-grid.
  * §4: random triangles (θ₀ − θ₁, θ_cap − θ₀).
