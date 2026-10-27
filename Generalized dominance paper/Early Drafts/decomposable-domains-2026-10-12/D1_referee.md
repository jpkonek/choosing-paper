# Referee report on D1_notes.md (round 15)

**What I checked.** I read Theorem D1 line by line: Lemmas D1.1–D1.6, the final surround step, Example D1.0, the K^i
structure, Corollary D1.7 and the §4 consequences. I checked them against:
- B2_notes and B2_referee: B2.1, Prop 13, §2 tie anatomy, Prop B2.0;
- the write-up: §2 (LF), §4.2 (UVN, Lemma PL2, Lemma nopin), §6 (Lemma quasiconcave, Lemma walls, Thm TSalways),
  §7.7 (Lemma quasilin, Prop crosspin, Prop carrying, Thm M0closed);
- R10b (Lemma D, Lemma M, Thm PL), and N28 Lemma 3.4 with N28_referee §3.3.

**Scripts.**
- I reran `d1py/` with `python3 -I` from `d1ref_py/`. Both `.out` files reproduce byte for byte. The scripts insert
  their own directory into `sys.path`, so `-I` does no harm here.
- My own checks are `d1ref_py/ref_checks.py`, with output in `ref_checks.out`:
  - R1: the bookkeeping of D1.5 (crossing, adjacent corner, sign at l): 0 failures over 6 values of ε;
  - R2: the Step-1 replacement inequality proposed in §5 below: 0 failures;
  - R3: finiteness of the hull constant of D1.4.

  These are NUMERICS. No verdict below rests on them.

---

## 0. Verdict in brief

**Theorem D1 is CORRECT.** The proof is complete once five fixable gaps are repaired. None of them touches the
mechanism.
- The two steps the author flagged hold:
  - Lemma D1.3, steps 2 and 4 (shell dichotomy; exclusion of d-ties);
  - Lemma D1.6, case (A) (the collar ball versus the ±σ′ pattern).
- The one substantive repair is in the transfer of Lemma M to a set E that is not closed (priority 5). R4 Thm B "off
  E" says nothing about d-faces that lie *on* an atom line (d-atoms), because every point of such a d-face is in E.
  A direct argument with the open chart R(−h) replaces it and is shorter (§5).
- **Conjecture B2.R under (LF) is PROVED as an additive statement.** It needs neither Prop B2.0 nor (β) and (δ). The
  hypotheses actually used are strict guidance, (γ), D_{T1} Bayes at an interior p\*, and (LF).
- **Corollary D1.7** is correct at the status of Prop B2.0, with a smaller dependency than the note states (§8).

| Item | Verdict |
|---|---|
| D1.1(a) coherence of D^δ_q at every q; continuity off E | CORRECT |
| D1.1(b) convexity of lex-accept sets; quasi-concavity | CORRECT |
| D1.1(c) UVN under (LF) | CORRECT (state "x ∈ N" in both clauses) |
| D1.1(d) one-sided limits at chord points | CORRECT; GAP (fixable): the definition of "generic" must also exclude pencil points; c′-ties are omitted in the proof |
| D1.1(e) face models at p\* | CORRECT |
| D1.2 cluster values are face models | CORRECT; but bullet 1 does not give "K^+(t) has interior" (see D1.3 step 2) |
| **D1.3 step 1** (shell levels tied or negated) | CORRECT |
| **D1.3 step 2** (dichotomy) | CORRECT after GAP (fixable): non-collinearity of K^+(t) must come from D1.2 bullet 3, not bullet 1 |
| D1.3 step 3 | CORRECT after a wording fix: "a.e. g in the shells", not "a.e. g ∈ G" |
| **D1.3 step 4** (exact zero; c-ties and d-ties ∝ b) | CORRECT |
| D1.3 steps 5–6 | CORRECT |
| D1.3 measure bookkeeping (arcs versus cones) | GAP (expository) |
| D1.4 ((TS_A) fails on F₁, F₂; use of (LF)) | CORRECT; GA and GB are elementary and should be proved, not cited as NUMERICS |
| D1.5 (pinned sets; choice of δ per crossing) | CORRECT (wording: p\* ∈ cl G, not p\* ∈ G) |
| D1.6 set-up, genericity, case Q ∉ E | CORRECT after GAP (fixable) in Step 1 of Lemma M (§5) |
| **D1.6 case (A)** | CORRECT |
| D1.6 case (B) | CORRECT (same Step-1 repair) |
| Final surround contradiction | CORRECT (d > 0 replaces relative closedness; generic segments suffice) |
| Example D1.0 and the K^i structure | CORRECT |
| "Gluing needs x_k + 1/x_{k+1} > κ+1 (CHECKED)" | Unsupported: no derivation or script in the note. Relabel as a remark. Not used |
| Cor D1.7 | CORRECT at the status of Prop B2.0; only (α\*), (γ), strict guidance and an integrable envelope are needed |
| §4 "only p\* ∉ E with E ≠ ∅ is left" | GAP (scope): the case E = ∅ also needs an argument (§9) |

---

## 1. Lemma D1.1

**(a) CORRECT.**
- A(g) is finite, and × is never tied (it is strictly worst at every world).
- Two advices with lexicographically equal losses have a difference vector v ∈ {±c, ±c′, ±d} with v·q = v·δ = 0. Then
  the line {v·q′ = 0} is the line through q in direction δ.
- "Generic δ" makes the set of g with a c-, c′- or d-line parallel to δ null. Each g lies in at most three of the
  sets N_δ, so only countably many δ are non-generic.
- The ray q + ℝ₊δ is parallel to no atom line, so it meets E in a countable set (B2 §2).
- Off E the Bayes model is coherent. It is a limit in measure of the coherent Bayes models at a.e. nearby point
  (B2_referee §1, Lemma 1, repair 2).
- So the limit along s_m ↓ 0 exists pointwise a.e. and is coherent.
- Hausdorff continuity of K at q ∉ E: every untied g keeps its strict optimum near q. The same holds for K^δ at
  q ∉ E.

**(b) CORRECT.**
- For a fixed oriented gamble and each competitor a, the set {q : + lex-beats a} is {q·v > 0} if δ·v < 0, and
  {q·v ≥ 0} if δ·v > 0. The case δ·v = 0 is null by genericity.
- So {q : g ∈ D^δ_q} is an intersection of at most three half-planes, each open or closed, and hence convex. The same
  holds for the orientation −g.
- The first half of Lemma quasilin(a) needs only D^δ_{q₁} ∩ D^δ_{q₂} ⊆ D^δ_q and coherence at every q. Both are now
  available.

**(c) CORRECT.**
- For each g the minimiser of q·ℓ tends to the strict world-l minimiser. The limit model is coherent as a limit in
  measure of the coherent D^δ_q.
- Clause x_l > 0: (LF) makes "accept" available on a ball around x, and it is world-l best there.
- Clause x_l < 0: silence is available by (LF), so the world-l best advice is never "accept".
  - Without x ∈ N a singleton range {+} would break this clause.
  - The statement should therefore read "x ∈ N" in both clauses.
- The strict sign comes from upward and downward closure, as written.

**(d) CORRECT; GAP (fixable).**
- *Definition of "generic".* E ⊆ (atom lines) ∪ (a countable set). The countable set contains two kinds of point
  (B2 §2):
  - fan (apex) points;
  - points whose pencil is charged by the non-atomic part of a line push-forward.

  At a point of the second kind, Z_t is **not** the set of gambles whose line is ℓ′. So "generic" must exclude both
  kinds. Since D1 uses only "a.e. t" and segments that avoid countably many points, the fix is free.
- *c′-ties.* The proof of the last clause lists c-ties and d-ties only. A c′-tie (silence against accepting −g) puts
  the accepted gamble −g in the symmetric difference, and −g has the pattern of c′ ∝ ±b′. Add this sentence. The
  conclusion "every accepted gamble in D_{K⁺} △ D_{K⁻} has pattern ±σ′" is then exact.
- *The rest.* For g tied at t with tie vector v ∝ ±b′:
  - q·v = (q − t)·v exactly;
  - the third advice is strictly worse near t;
  - so convergence is pointwise a.e., hence in measure, hence Hausdorff.

**(e) CORRECT.**

## 2. Lemma D1.2: CORRECT

- Every g ∉ Z_{p\*} keeps its strict optimum near p\*. On Z_{p\*} the advice is eventually in {+, 0} (B2.1(d)). A
  Hausdorff cluster value therefore has its advice in A\*_{p\*} a.e., so it is a face model and contains T1.
- Bullet 1 then follows by the diameter argument.
- Bullet 3 (convergence of K^±(t) along each half-ray of ℓ) is correct. Every gamble tied at t ∈ ℓ but not at p\* is
  eventually untied. One example is a d-atom on ℓ: there c·p\* = c′·p\* < 0, because B2.1(d) excludes d-ties at
  p\*.
- **Caution.** Bullet 1 does **not** imply that K^+(t) is two-dimensional. A segment of length > 2η lies in no η-ball.
  See D1.3 step 2.

## 3. Lemma D1.3 (author's priority 1)

**Measure bookkeeping: GAP (expository).**
- α₀ is a one-dimensional arc, and the shells over it form a μ-null surface. So every "a.e. h ∈ α₀, a.e. s" statement
  is vacuous as written.
- **Fix.** Work on the two-dimensional cone ℝ₊α₀. The map (h, s) ↦ h + s𝟙 is a diffeomorphism onto an open set,
  since 𝟙 is transversal to ∂D_{T1}. By positive homogeneity (s_{λh} = λs_h, P(λh) = λP(h)) every conclusion for λh
  is the conclusion for h. So "a.e. h" means a.e. τ.
- Likewise, step 4 proves P^+ = 0 for **a.e.** h ∈ A_t. Continuity in h then gives it on the closure of the essential
  part of A_t. Step 5 needs only a set of positive length.

**Step 1: CORRECT.**
- On a shell, c ∝₊ b gives c·t = 0.
- If c′·t < 0, the gamble is a c-tie. K^+ accepts it (δ·c > 0) and K^− is silent (δ·c < 0).
- If c′·t > 0, then − beats 0 (c′·t > 0) and beats + (d·t = −c′·t < 0), so both models negate.
- If − ∉ A, the gamble is a c-tie.
- Apexes at a non-fan t are null.

**Step 2: CORRECT after a GAP.**
- The algebra is right. Accepted levels are s > −P, negated levels are s < −P̄. If both occur in (0, s_h), the silent
  interval [−P̄, −P] lies inside (0, s_h). Step 1 makes that interval null, so P = P̄ on h, and K^+(t) lies in a line.
- **The justification "K^+(t) has interior by D1.2" is wrong as cited** (§2 above).
- **Fix.** Use D1.2 bullet 3: K^+(t) → K^+_\* ⊇ T1 in the Hausdorff metric. So for t near p\*, K^+(t) contains points
  m_i within any prescribed distance of v₁, v₂, v₃, and these are affinely independent. Hence K^+(t) lies in no line.
  This holds for every h at once, so the dichotomy holds for a.e. h ∈ α₀.

**Step 3: CORRECT after a wording fix.**
- "For a.e. g ∈ G, c′(g)·p\* < 0" is false for the oriented atom G as a whole. G is the set of gambles whose
  c-direction is b, and it may contain gambles with c′·p\* > 0, which are negated at p\*.
- What is true, and all that is used: a.e. **shell** gamble is tied at p\*, hence a {+,0} c-tie by B2.1(d), so
  c′·p\* < 0 for it.
- Dominated convergence then works as written. Entirely negated shells carry levels of total length
  ≥ inf_{α₀} s_h > 0, so their measure tends to 0.

**Step 4: CORRECT. This is the delicate step, and it holds.**
- Take h ∈ A_t with P^+(h) > 0.
  - The levels s ∈ (−ε, 0) are accepted by K^+.
  - K^− is silent on the whole shell, because every shell level is a c-tie at t when h ∈ A_t. So −P^−(h) ≥ s_h > 0,
    and K^− does not accept those levels.
  - They therefore lie in D_{K⁺} ∖ D_{K⁻} ⊆ Z_t (D1.1(d)).
  - For + to win the lexicographic order over a′ ∈ {0, −} with δ·b > 0, the tie vector (c, resp. d) must be ∝ **+b**,
    as the note says.
- *c ∝ b.* At p\* we have c·p\* = 0. Three cases:
  - a {+,0} tie, which needs T1 to accept f_s, but P_{T1}(f_s) = s < 0;
  - − strictly optimal, which needs T1 to negate, i.e. s < −P̄_{T1}(h) ≤ −2c₁;
  - an apex, which is null.

  All three are impossible for s ∈ (−c₁, 0). (The note's phrase "Z_{p\*} ∩ (h + ℝ𝟙) = S_h" is exact only on levels
  s > −P̄_{T1}(h). That is the only range used.)
- *d ∝ b.* K^− (δ·d < 0) picks −, so P̄^−(t,h) < −s < c₁. But P̄^−(t,h) ≥ P̄_{T1}(h) − ‖h‖·d_H(K^−(t), K^−_\*)
  ≥ 2c₁ − o(1), uniformly on the compact α₀. This holds on both half-rays of ℓ, because both one-sided limits are face
  models containing T1.
- No (LF) is used here, as the remark says.

**Steps 5–6: CORRECT.**
- A concave γ_t that vanishes on a set of positive length is ≤ 0 everywhere, by Lemma caps(a). It vanishes on the
  interval co(A_t), because {γ_t ≥ 0} is convex.
- Lemma 3, run in v₁^⊥, gives v₁ ∈ K^+(t).
- Step 6 uses the same δ, hence the same K^+(t), on α′ ⊂ F₂.
- Steps 3 and 4 hold uniformly for t ∈ ℓ ∩ B(p\*, r₀) on both sides, so r₀ can be chosen once.

## 4. Lemma D1.4: CORRECT (how (LF) is used)

- (LF) enters only through D1.1(c), applied to middle-arc gambles of F₁ (positive at worlds 2 and 3). These lie on
  ∂D_{T1} ⊆ N.
- The argument runs:
  - x ∉ E with P(x,g) > 0 gives P^δ(x,g) > 0;
  - convexity gives co({x} ∪ V₂′ ∪ V₃′) ⊆ C;
  - that hull meets the half-ray R⁺ of ℓ in an open interval starting within C₀|x − p\*| of p\*;
  - at a.e. t of that interval, K^δ_t = K^+(t), and D1.3 gives P^+ ≤ 0 on F₁, a contradiction.
- **GA and GB need no NUMERICS.**
  - GA: b·e₂ < 0 < b·e₃, so ℓ hits relint[e₂, e₃] at L = λe₂ + (1−λ)e₃. Then L − p\* = λ(e₂ − p\*) + (1−λ)(e₃ − p\*),
    which lies in the open wedge.
  - GB: if R⁺ makes angle ≥ θ with both wedge edges, then for |x − p\*| and the radii of V₂′, V₃′ small, the wedge at x
    spanned by e₂′ − x and e₃′ − x still contains the direction of R⁺ with margin θ/2. So C₀ ≤ 2/sin(θ/2), which is
    finite (R3).
- F₂ with the half-ray R⁻ is symmetric.

## 5. Lemma D1.5 (priority 4) and Lemma D1.6 (priorities 2 and 5)

**D1.5: CORRECT.**
- *Choice of δ.* The corner portion adjacent to the crossing contains no other corner (R1 confirms the corners: r₁₂
  for w₂₁, r₃₁ for w₃₁, r₂₃ for w₃₂). So at most one atom can cover σ_i there, and a generic δ with δ·b_k > 0
  exists.
- *P^δ(p\*, h(σ_i)) = 0.* "≤" holds because K^δ_{p\*} ⊇ T1. For "≥":
  - on the middle arc it is crossing pinning (B2.1(b));
  - on the corner portion, either P_{K♭}(h(σ_i)) = 0, and D_{K^δ} ⊇ D_{K♭} gives "≥";
  - or h(σ_i) lies under a carrying arc and the shells are accepted.
- *(i)* This is the wedge argument of Lemma nopin. It uses P = P^δ at q ∉ E.
- *(ii)* A concave function that is ≥ 0 at σ₁ and σ₂ and ≤ 0 at the interior point τ_m is ≡ 0 on [σ₁, σ₂].
- *Wording.* p\* lies in {P^δ ≥ 0 at σ₁ and σ₂}, not in its interior G. The note then correctly uses p\* ∈ cl G.

**D1.6, set-up and genericity: CORRECT.**
- O ∩ cl β = ∅.
- y ∈ β for y ∉ E, by UVN at w for world l.
- [o, y] ⊆ G by convexity.
- A.e. segment avoids the countably many non-generic points, is transversal to the countably many atom lines, and
  meets E countably.

**Lemma M off E (priority 5): GAP (fixable), in Step 1, in both case Q ∉ E and case (B).**
- Step 1 must show that a near-facet good h ∈ U⁻ has no d-face in B(Q, r).
- The note invokes "R4 Thm B off E": K_p ⊆ h^⊥ for p ∈ cl F(h) ∖ E. That is correct where it applies. But if h
  belongs to a **d-atom** whose line ℓ″ crosses B, then F(h) ⊆ ℓ″ ⊆ E, and cl F(h) ∖ E contains at most the
  endpoints. So R4 Thm B is silent.
- Nothing excludes such d-atoms near Q: E may be dense, and B2 §5 names d-atoms explicitly.

**Fix (verified; it also removes the dependence on R4 Thm B).**
- Let h ∈ U⁻ be good, with nearest facet point w′ and |h − w′| < c₀ρ.
- If R(−h) ∩ B ≠ ∅, this set is open, so it has a point q ∉ E with P(q, −h) > 0. Hence K_q ⊆ {m·h < 0}.
- Also K_q ⊆ W_v(U), since q ∈ G ∖ E ⊆ Γ_v.
- For m ∈ W_v(U), m·h ≥ m·w′ − |h − w′| ≥ c₀|m − v| − |h − w′|. So K_q ⊆ B(v, |h − w′|/c₀) ⊆ B(v, ρ), against the
  choice of B.
- Hence R(−h) ∩ B = ∅. Then B ∩ {c > 0} ∩ {d < 0} ⊆ R(−h) is empty, and R(h) ∩ B = {c > 0} ∩ B, which is exactly the
  conclusion of Step 1.
- R2 checks the inequality on samples: 0 failures.

**The other steps survive E.**
- Step 2 uses continuity at Q in case Q ∉ E, or at the β-points s ∉ E.
- Step 3(i) uses a.e. points.
- Step 3(ii) uses q ∈ β, which is off E.
- Step 4 uses strict signs and UVN at w₊.

**Case Q ∉ E: CORRECT after the fix.**
- Q ∉ β: otherwise continuity at Q puts off-E points of [o, Q) into β.
- So v ∈ K_Q, and Lemma M gives K_Q = {v}.

**Case (A): CORRECT (priority 2).**
- K^o ⊆ W_v(U) is a closed condition. Lemma D is pure duality and applies to the limit set K^o, giving an exterior
  collar in D_{K^o}.
- v ∈ K^s gives D_{K^s} ∩ U⁻ = ∅.
- The ball around w − s(𝟙 − e_c) has center in {g_c = 0} and lies in the collar, since P_{T1} = v·(·) near w gives
  v·(w − s(𝟙 − e_c)) = −s(1 − v_c) < 0.
- Its two half-balls are non-null, with patterns that differ in coordinate c only. At most one of them is ±σ′, so the
  other contradicts D1.1(d), with the c′-tie sentence added.

**Case (B): CORRECT.**
- K^s and K^o both contain v.
- If either equals {v}, nearby off-E points of the segment are in {K ⊆ B(v, η)}.
- Otherwise Steps 1–4 run on a full ball:
  - Step 1 needs K_p ⊄ B(v, ρ) on B ∖ E. This follows because both one-sided limits have a point at distance ≥ 2ρ
    from v, and "⊄ B(v, ρ)" is preserved in the limit.
  - Step 2 needs P(·, h) < 0 on both sides, which holds because v ∈ K^s ∩ K^o.

## 6. The final surround contradiction: CORRECT

- d = dist(p\*, 𝒵 ∪ 𝒵′) ≥ r > 0 by D1.2. The proof of N28 Lemma 3.4 uses only d > 0, not relative closedness.
- The proof chooses one segment per vertex with o_i ∈ O_i ∩ B(p\*, δ) and v_i ∈ V_i ∩ B(e_i, δ). Each O_i is open with
  p\* ∈ cl O_i, so these pairs have positive measure, and the a.e. statement of D1.6 suffices.
- The index pattern matches Lemma 3.4: 𝒵 toward V₂ and V₃, 𝒵′ toward V₁.
- For h³ ∈ relint F₃: v₁·h³, v₂·h³ > 0. Fix η before applying D1.2 and D1.6. Then 𝒵 ∪ 𝒵′ ⊆ C₃, which is convex, while
  P^δ(p\*, h³) ≤ P_{T1}(h³) = 0.
- **Remark.** The cascade of Thm TSalways (Prop 3.1, Lemmas 3.2–3.3) is not needed. D1.4 pins F₁ and F₂ directly,
  which gives walls toward all three vertices. This is a genuinely simpler surround than N28's.

## 7. Example D1.0, K^i, step (3): CORRECT, one unsupported label

- **Example D1.0.**
  - D_{T1} ∖ G_k ≈ D_{T1} ∩ D_{co(T1 ∪ {m_k})} mod null, and D_{K₁} ∩ D_{K₂} = D_{co(K₁ ∪ K₂)}. This proves E2
    exactly.
  - The G_k are disjoint, by their patterns (B2_referee G9).
  - Σb_k = 0 with pairwise non-parallel b_k, so T1 is interior to the zonotope (B2_referee §5).
  - In E5, K^{(2)} = co(T1 ∪ {m₁₂, m₂₃}), and its minimum on a middle-arc gamble of F₁ is attained at v₁ (= 0). So UVN
    fails, as claimed.
  - Reproduced.
- **K^i.** The world-i-best advice on G_k is + iff (b_k)_i > 0, so K^i rejects exactly the two atoms with
  (b_k)_i < 0. Correct.
- **"x_k + 1/x_{k+1} > κ+1 (CHECKED in this round by the sector computation)".** There is no derivation in the note
  and no script in `d1py/`. It is not used. Label it as a heuristic remark, or supply the computation.

## 8. Corollary D1.7 and its dependence on Prop B2.0

- **CORRECT at the status of Prop B2.0**, which B2_referee §4 rated GAP (documentation). Theorem D1 uses only:
  - strict guidance of ψ;
  - an integrable envelope;
  - (γ);
  - D_{T1} ψ-Bayes at an interior p\*;
  - (LF), inherited from the ranking's domain, which ψ shares.
- So of B2.0 only three items are needed:
  - (α\*);
  - (γ);
  - **ρ_i > 0 a.e. on problems with non-singleton advice range.** This is the general-domain N19 Lemma R1, without
    which ψ is not strictly guiding. It should be added to B2_referee's to-do list for B2.0.
- (β) and (δ), and with them the regular-splice step of N13 Prop B, are **not** needed. The status line can say so.
- **B2.R.** The restated conjecture "(R2) empty under (LF)" is proved by D1 as an additive theorem. It does **not**
  depend on B2.0, nor on the "(β), (δ)" that B2_referee attached to the restatement.
- "Ordinal tie-breaking at p\* is vacuous": correct at the same status. It applies at every interior weighting at
  which D_{T1} is ψ-Bayes.

## 9. §4 consequences

- "General-domain half of Thm M0closed(a)'s p\* ∈ E branch": correct, under (LF).
  - "Independent of Prop carrying" is also correct. On M_U, D1 uses B2.1, Prop 13 (ball lemma), R10b and N28, not
    frozen support.
- **"Only the branch p\* ∉ E with E ≠ ∅ is left": GAP (scope).**
  - If E(ψ) = ∅, then ψ has (BU) everywhere, but Theorem gm is stated for rankings with (LA), (S), (C).
  - Applying it to ψ needs either Thm ccibu (author-checked only), or an audit that the routes of Thm gm use nothing
    beyond (BU), (TP), (LF), (β), (δ). B2_referee §7 notes that Prop necessary(b)–(c) are used.
  - State the E = ∅ case at that status.
- **"D1.6 shows TSalways's walls cross every chord".**
  - D1.6 does show that the wall step (Lemma M at chord points) crosses chords. That holds given an open convex G with
    G ∖ E ⊆ Γ_v and a pinned O.
  - TSalways also uses Prop 3.1 (local chain on B₁) and Lemma 3.2 (Thm PL, R23.1 at p\* ∈ cl O). These need (BU)
    near p\*.
  - The proposal is correctly labelled CONJECTURE. Narrow the sentence accordingly.

## 10. Required changes (summary)

1. D1.1(d): define generic t to avoid fan points **and** charged-pencil points; add c′-ties to the proof. D1.1(c):
   "x ∈ N" in both clauses.
2. D1.3: do the bookkeeping on the cone ℝ₊α₀. Step 2: get non-collinearity from K^+(t) → K^+_\* ⊇ T1. Step 3: "a.e.
   shell gamble". Step 4: "P^+ = 0 a.e. on A_t, then continuity".
3. D1.4: replace NUMERICS GA and GB by the one-line proofs of §4.
4. D1.5: "p\* ∈ cl G".
5. D1.6 (both cases): replace "R4 Thm B applies off E" by the open-chart argument of §5.
6. Final step: cite N28 Lemma 3.4's proof with d > 0, and note that generic segments suffice.
7. §2: relabel the gluing inequality.
8. Cor D1.7: list the precise B2.0 imports ((α\*), (γ), ρ_i > 0), and state that B2.R is proved independently of
   B2.0.
9. §4: the E = ∅ caveat; narrow the TSalways sentence.

**Status after repairs.** Theorem D1, and B2.R under (LF): PROVED, one reading (this report). Cor D1.7: at the status
of Prop B2.0, with the reduced import list.
