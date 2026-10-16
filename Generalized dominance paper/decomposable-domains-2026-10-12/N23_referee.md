# N23: referee report on N21_notes.md (13 Oct 2026)

I did not write N21 and treated nothing in it as correct until I had re-derived it.

**Read.** BRIEF7; N21 in full; N15 in full; N18 and N20 in full (both refereed N15 as CORRECT with repairs); N14 §§2.3, 3,
5.2, 6; N12 §§2–3 (Lemma 2.1, Thm 2.4, Prop 2.5, Thm 3.1); R1 §§1–3 (Prop 2.1 table of charts for each advice range, Lemma 1.5, Props 2.4, 2.8,
3.1, Lemma 3.5); R4 in full (Thms A–C, §8 (K4), §9); R10b in full (Prop V, V1, V2, UVN, Lemmas D, M, P, Thm PL,
Cor PL2); R11 Lemma RS; R15 §§1–2 (Lemma C) and §6 (Lemma 6.1, Thm 6.2).

**Scripts.**
- Rerun: `n21py/lemmas_check.py` and `n21py/t1_lambda_per_vertex.py`. Output reproduced exactly: 0/908 sector
  violations; t-bounds 1.43e-3, 1.30e-3, 1.15e-3; incoherent at t = .25, .3, .35; every b has a failing box;
  Λ_{ab}Λ_{cb}/β² = 1.000000.
- New: `n23py/checks.py` (output in `n23py/checks.out`), six checks, listed in §10.

**Verdict scale.** CORRECT / CORRECT WITH REPAIR (local fix given here) / GAP / FALSE.

---

## 0. Summary

### 0.1 Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| §1 table of uses of non-adjacency (U-glob, U-box) | **CORRECT** | Both kinds checked. But the pinning step is only *partly* global: Cor PL2 can be run inside B₁ when the set contains p\*. N21 missed this; see §7 |
| **N21.1** quasi-concavity of q ↦ P(q,g), every decomposable domain, every g | **CORRECT** | Needs only (1.1) for good gambles, density of good gambles, and convexity of every chart in R1's table. Unanimous g″ > 0 is trivial |
| N21.1 Remark ("non-adjacency ⇔ adds quasi-convexity"; "exactly what survives") | **CORRECT WITH REPAIR** | "⇐" is false. The precise identity system with adjacent data for the advice range {+,0,−} is adjacent at every mixed pair, yet P(q,g) = q·g is affine (`checks.py` (4)). The correct equivalence is per good g at level 0: {P ≤ 0} convex ⇔ R(g) ∩ Ω is ∅, Ω or a half-plane ∩ Ω (no wedge in Ω) |
| N21.1′ (global inclusion A_τ ⊆ H⁺) | **CORRECT** | |
| **N21.2** (no −g acceptance and no d-face where K_q ∩ K″ ≠ ∅; ball B₁ with half-plane charts) | **CORRECT** | Steps 1–4 check. Hausdorff step re-derived. Small improvement: the statement holds pointwise in q for good g, so C need not be open or convex, and the null set does not depend on C |
| N21.3 (sector lemma) | **CORRECT** | The hypothesis "start in silence" is essential: 207 random segments go R(±g) → S → R(∓g) without a d-face (`checks.py` (5)) |
| **N21.4** ((TS) ⇒ N15 Thm 4.2, 4.3, §§5–6, (PC), (NS) on every (LF) domain) | **CORRECT** (two wording repairs) | Every edit re-derived. The genuinely new step, the negative vertex sign via c-clusters (item 5), is sound. Repairs: levels must lie in int N₀ (replacing I_g); the a.e. sets of N21.2 are uniform in C |
| N21.4 Remark (N12 Thm 3.1 items 3–5 transfer) | **CORRECT** | |
| **N21.5** (a) Lemma RS does not apply | **CORRECT** | C_{e_k} accepts −g on E (R1 Lemma 1.5) |
| N21.5 (b) deletion changes the Bayes family | **CORRECT** (wording) | "Loses the corresponding −g" should read: loses every −g with q ∈ R(−g), g ∈ E |
| N21.5 (c) n = 2 example | **CORRECT** | Data re-derived: concurrent lines, empty silence, (G) signs. Acceptance set {r < t} ∪ (0.4, 2t) for t ∈ (0.2, 0.4) (`checks.py` (6)) |
| N21.5 / §0 slogan "No WLOG reduction to two-element advice ranges (PROVED)" | **CORRECT WITH REPAIR** (scope) | What is proved is that the restriction route (Lemma RS, or naive deletion) fails. A general "no reduction exists" cannot be proved without an adjacent realisation, because any reduction would itself prove the theorem |
| §5 preamble (exactly one failing box per vertex; Λ_{ab}Λ_{cb} = β²) | **CORRECT** | Exact: sympy gives v_{ac}v_{ca}/(v_{aa}v_{cc}) − β² ≡ 0, and Λ ∈ {βx₊², β/x₊²} with βx₊² > 1 (`checks.py` (1)) |
| **N21.6** cut localisation (i)–(iv) | **CORRECT** | Steps 1–7 re-derived. The step-2 sign bookkeeping passes 12 962 random charts with 0 violations. The (iv) bound matches brute force and → 0 as η/δ → 1 (`checks.py` (2), (3)) |
| **N21.7** (a)–(d) | **CORRECT** (wording) | (a) should read "a.e. h with h_b > 0 that is not ≥ 0" (unanimous gambles are in B_q by convention). (d) is R4 (K4) with acceptance in the advice range from (a) |
| **N21.8** main theorem (a)–(c) | **CORRECT** | (a) N21.4 + N21.6 + N21.7; (b) is the contrapositive; (c) is N15 |
| N21.9 ((E5a) structure (i)–(iii)) | **CORRECT** | Proved as stated. The following paragraph ("silent on O … must cross a d-face") is heuristic. "Silent on O" holds only for h close enough to the facet relative to q, and fails where K_q = {v_k}. Label it CHECKED |
| (E5b) analysis (n_τ ≡ n; B accumulates only on [τ_i, τ_j]; pinned on λ ∩ B₁) | **CORRECT, but (E5b) is in fact impossible** | Referee Lemma R23.1 (§7) runs Cor PL2 on a *ball around p\**, where p\* itself supplies the pinned point (K_{p\*} = T ∋ v_k). So (E5b) dies, and (TS) reduces to its A-half |
| §0 item 6, last sentence ("…or must pin a vertex near p\* behind a wall of precise vertex priors") | **GAP in N21, closed here** | N21 produces no precise wall in case (E5b). After R23.2, (E5b) is excluded and the sentence holds |
| (E4′) "no argument local to the vertices can close (E4′)" | **CORRECT WITH REPAIR** (label) | The evidence is R4 §9's single identity cap (numerics plus a hand edge blow-up). That is not a proof. Label it CHECKED/NUMERICS |
| CONJECTURE N21; "silence cell reaches ∂Δ" | **CORRECT** (the small claim) | It is a recession-direction argument. The conjecture remains a conjecture |

**Overall verdict: CORRECT.** No step of N21's proved chain fails. The repairs are local or concern labels and scope.
N21's two named residuals reduce to one: **(E5b) is impossible** (§7, new). What remains open is (E5a), single-vertex
pinning near p\*, and (E4′), the near-all-orientation cut regime.

### 0.2 New results in this report (PROVED here; a second reader should check §7)

- **Lemma R23.1 (pinning on a ball around p\*).** Let F_k be a facet with a crossing τ_c ∈ (σ₁,σ₂), and let ρ ≤ r₁. If
  Ψ(·,σ₁) ≥ 0 and Ψ(·,σ₂) ≥ 0 on B(p\*,ρ), then v_k ∈ K_q and Ψ(q,·) ≡ 0 on [σ₁,σ₂] for every q ∈ B(p\*,ρ). In
  particular A_τ ∩ B(p\*,ρ) = ∅ for every τ ∈ [0,1].
- **Cor R23.2.** (E5b) cannot occur, on any (LF) decomposable domain. Hence (TS) ⇔ (TS_A): for every facet and every τ ∈ (0,1),
  p\* ∈ cl A_τ.
- **Prop R23.3 (refined (E5a)).** In (E5a) at τ, the whole convex set int(P_{τ_c−η} ∩ P_{τ_c+η}) ∩ B₁ is pinned for small η,
  and A_{τ_c} ∩ B₁ = ∅ at the crossing τ_c.
- **Cor R23.4 (unconditional, nearby result).** Every T1 realisation on an (LF) decomposable domain has, for a.e. mixed pair, an
  advice range containing acceptance of at least one orientation. So T1 has **no realisation on any (LF) decomposable domain on which a non-null set of mixed
  pairs has an advice range containing neither acceptance**. Moreover, if no evaluable model accepts the orientations in a non-null set of mixed orientations, then (TS) fails,
  and those orientations lie a.e. in {v_k·h ≤ 0} for every pinned facet k.

### 0.3 What is now proved for T1 on general (LF) decomposable domains

The full statement is §8. In brief: every realisation is in exactly one of two regimes.
- **(TS) holds.** Then the advice range of a.e. mixed pair contains both acceptances, all vertex models are precise, interior limits at edge
  priors are edge-confined, and every vertex carries the N21.6 cut structure. So the domain is "all-model on mixed pairs".
- **(TS) fails.** Then some facet has single-vertex pinning near p\* across a crossing, shielded by precise {v_k} priors.

On non-adjacent domains neither regime is possible (N15).

---

## 1. Setting and the table of uses (N21 §1)

- **Setting.** N₀ is a closed conic neighbourhood of ∂D_T ∖ 0 inside N, with P_{K″} > 0 on N₀.
  - It exists: P_{K″}(h) > 0 for 0 ≠ h ∈ ∂D_T, since m·h ≥ 0 on T, and a zero at an interior point of T would make h
    vanish on aff Δ, i.e. h = 0.
  - Compactness on the sphere then gives the neighbourhood.
  - Advice ranges on N are {+,0} or {+,0,−} (R10b §1). ✓
- **Table.** I re-checked each row against N15.
  - Lemma 2.1 uses global level chords (U-glob). Step 0 uses global half-planes. Step 4's negative sign uses
    λ⁺_τ ∩ Ω ⊆ P_τ globally. Lemma 4.1 uses Cor PL2 on int conv(G ∪ V_j), which leaves any ball at p\* (U-glob). The
    box bridge is (U-box).
  - Steps 2, 3, 5, Thm 4.3, §§5–6 are local.
  - The table is correct.
- **Missed refinement.** Cor PL2 itself is local: it needs only the absence of d-faces on G. What is global in N15 Lemma
  4.1 is the *α-exclusion*, which needs a β-point (from V_j). When G is a ball around p\*, the pinned point is p\* itself
  and the β-point can be local. This is §7.

---

## 2. N21.1, N21.1′ and the remark

**N21.1. CORRECT.**
1. *Shift.* c′ ∈ (c, min P(q_i,g)) gives P(q_i, g′) > 0 for g′ = g − c′𝟙.
2. *Approximation.* Good gambles are co-null, hence dense, so good g″ → g′ exist. Joint continuity keeps
   P(q_i,g″) > 0.
3. *Chart.* (1.1) gives q_i ∈ cl R(g″). This also shows R(g″) ≠ ∅: if no evaluable model accepted g″, (1.1) would give
   P ≤ 0 everywhere.
   - Every chart in R1's table is convex: Δ, ∅, {c>0}, {d>0}, {c>0,d>0} and {c′>0,d<0}. So cl R(g″) is convex and
     contains [q₁,q₂]. Then P(·,g″) ≥ 0 on it.
   - If g″ > 0, then P(·,g″) > 0 everywhere and the claim is trivial.
4. *Limit.* Let g″ → g′. Then P ≥ c′ > c on [q₁,q₂]. The ≥-version follows by intersection.
5. *Hypotheses.* (LF) and U′ are not used, so the lemma holds for every g ∈ ℝ³. ✓

**N21.1′. CORRECT.** If x ∈ A_τ with n·(x − p\*) < 0, the segment from x to y ∈ H⁺ ∩ B₁, with y close to λ and to p\*,
contains points of B₁ ∖ H⁺. Convexity of A_τ (N21.1) puts them in A_τ, which is a contradiction.

**Remark. CORRECT WITH REPAIR.**
- *What is right.*
  - Non-adjacency ⇒ quasi-convexity at the levels c ∈ I_g (N15 Lemma 2.1).
  - A *wedge* chart for a good g, i.e. both constraints active in Ω, ⇒ {P(·,g) ≤ 0} is not convex. Reason:
    {P > 0} = R(g) ∩ Ω minus a closed null set, and the convex hull of the complement of a wedge with apex in Ω covers
    part of the wedge.
- *What is wrong.* Adjacency does not imply failure of quasi-convexity.
  - Counterexample: the precise identity system K_q = {q} with data d = κg, c′ = −θg + e₀𝟙, c = (κ−θ)g + e₀𝟙, where
    0 < θ < κ and e₀ is small. These have the strict (G) signs.
  - The charts are exactly {q·g ≷ 0} and the silence cell is empty. On the d-line {q·g = 0} we have α = β = e₀ > 0, so
    every mixed pair is adjacent.
  - Yet P(q,g) = q·g is affine.
  - `checks.py` (4): 0 sign violations, 0 chart mismatches, all 1 508 mixed pairs adjacent.
- *Repair.* Replace "⇔" by: "for good g, {P(·,g) ≤ 0} is convex iff R(g) ∩ Ω is ∅, Ω or Ω ∩ (half-plane). Non-adjacency
  (R4 Thm A(ii)) is sufficient, not necessary."
- This does not affect any proof in N21.

---

## 3. N21.2 and N21.3

**N21.2. CORRECT.**
1. *No −g acceptance.* If m ∈ K_q ∩ K″, then m·g > 0, so P(q,−g) < 0. By (1.1) for the good orientation −g, q ∉ cl R(−g).
2. *No d-face.* This is Thm B: K_p ⊆ g^⊥ is incompatible with m·g > 0.
3. *Half-plane chart.* {α>0, d<0} ⊆ R(−g), since β = α − d > α > 0. And {α>0, d=0} = F(g). So α > 0 ⇒ d > 0 on C.
4. *The ball.* K″ + B(0,ρ) ∩ 𝟙^⊥ ⊆ T, and a point x ∈ K″ ∖ K_q is strictly separated by a unit n. Then
   x + ρ′n ∈ T (ρ′ < ρ) has distance > ρ′ from K_q. So d_H(K_q,T) < ρ′ forces K_q ⊇ K″. Continuity at p\* gives B₁. ✓
- *Improvement.* Steps 1–3 are pointwise in q for good g (step 1 via (1.1), not via Fubini on C). So the conclusion holds
  on the relatively closed set {q : K_q ∩ K″ ≠ ∅}, with the exceptional null set of g independent of C.

**N21.3. CORRECT.**
- S(g) = {α ≤ 0, β ≤ 0} is convex.
- At a sign change of d along the segment, α = β there. Either the common value is > 0, which is F(g), or it is ≤ 0,
  which is S(g), excluded after leaving S.
- The hypothesis "start in silence" is essential: `checks.py` (5) finds 207 segments not starting in S that pass
  R(±g) → S → R(∓g).
- This matters for the heuristic after N21.9 (§7.4).

---

## 4. Theorem N21.4

All items re-derived. The notation is as in N15. "Local Lemma 2.1" means N15 Lemma 2.1 on B₁, at levels c with
h − c𝟙 ∈ int N₀.

1. **Local straight levels. CORRECT WITH REPAIR (wording).**
   - For good g ∈ int N₀, R(g) ∩ B₁ = {c(g)·q > 0} ∩ B₁ (N21.2), and {P(·,g) > 0} ≈ R(g) ∩ Ω. So N12 Lemma 2.1(a),(b)
     hold on B₁. A cluster line that misses B₁ gives the cases ∅/B₁.
   - N15 Lemma 2.1, Steps 2–6, run in the convex set B₁. The level interval I_g must be replaced by
     {c : g − c𝟙 ∈ int N₀}, which contains [−c₀, c₀] for facet gambles.
   - Lemma 2.3 holds with r₁. It uses only that {f > c} ∩ B₁ and {f < c} ∩ B₁ are half-planes not meeting λ ∩ B₁ (in
     N20's weakened form).
2. **(TS) replaces Steps 0, 1, 5. CORRECT.**
   - (TS) makes A_τ ∩ B₁ and B_τ ∩ B₁ proper and nonempty, so both are half-planes.
   - p\* ∉ A_τ ∪ B_τ and p\* ∈ cl A_τ ∩ cl B_τ put p\* on both boundary lines. Two lines through p\* that do not cross in
     B₁ coincide.
   - Global A_τ ⊆ H⁺_τ follows from N21.1′. With UVN (adjacency-tolerant, R10b §3) this gives n_τ·(e_l − p\*) > 0 when
     h(τ)_l > 0.
3. **Step 2. CORRECT.**
   - n_σ ≠ −n_{σ′}: A_σ ∩ A_{σ′} ⊇ V_j ∩ Ω (or V_i ∩ Ω) is nonempty, and A ⊆ H⁺ globally.
   - The wedge inclusion near p\* plus Farkas gives betweenness.
   - The open half-circle is {n : n·(e_j − p\*) > 0} on (0,τ_j), from item 2.
   - Gluing on the overlap needs non-constancy (N18 R-a), which is item 5. It is independent of Steps 2–3.
4. **Step 3. CORRECT.**
   - Z_{τ₀} ∩ B₁ = {Ψ ≥ 0} ∩ {Ψ ≤ 0} ∩ B₁. The first set is convex by N21.1, the second by local Lemma 2.1.
   - The jump double-wedge then gives a neighbourhood of p\* inside Z_{τ₀}, contradicting p\* ∈ cl A_{τ₀}.
   - Only the A-half of (TS) is used. This matters in §7.
5. **Step 4 via c-clusters. CORRECT.**
   - R15 Lemma C runs on B₁. q ∈ A⁺ gives q ∈ cl R(g_m) ∩ B₁ ⊆ cl{c(g_m) > 0}. q ∈ A⁻ gives q ∉ cl R(g_m).
     Non-constancy of ĉ follows from the weak mixed signs.
   - Two complementary open half-discs of λ_τ, contained in opposite open sides of the ĉ-line, force that line to be
     λ_τ with the same orientation.
   - c(g_m)_i < 0 gives ĉ·e_i ≤ 0, i.e. n_τ·(e_i − p\*) ≤ 0. Only a weak inequality is obtained, but it suffices:
     - under constancy λ_τ ≡ λ (from the cap lemma, as written), the A-side gives n·(e_i − p\*) > 0 on one side of τ_i;
     - the c-cluster gives ≤ 0 on the other side.
   - Continuity of n then gives λ_{τ_i} = line(p\*, e_i).
   - This is the one new argument, and it is sound.
6. **Thm 4.3. CORRECT.**
   - r ∈ int N₀ (a corner ray), so Z(·,r) ∩ B₁ is convex.
   - The test prior q ∈ B with q ∈ A^k_τ and n^k(0+)·(q − p\*) < 0 exists by strict monotonicity. The cap lemma at q is
     local.
7. **§5 and 8. §6. CORRECT.**
   - Anchors with ξ < r₁/2, Lemma 2.3 at radius r₁, Lemma 5.2 and Prop 5.3(a) are all local.
   - The blow-ups are at p\*.
   - N12 Lemma 4.3's "n nowhere locally constant" is item 5.
   - The N18/N20 repairs (τ₀ ∈ int J; the affine-patching lemma) carry over.

**Conclusion.** Under (TS), N15 Thm 4.2 holds on B₁: Z_τ ∩ B₁ = λ_τ ∩ B₁, unique clusters, a continuous strictly monotone
chord map, and crossing values. So do Thm 4.3, Lemma 5.1, Prop 5.3 and §6. This gives (PC) and (NS) on every (LF) decomposable
domain. The **Remark** (N12 Thm 3.1 items 3–5) is CORRECT: these items use only c-clusters at p\*, which item 5 supplies.

---

## 5. Proposition N21.5

- **(a) CORRECT.** On E, (−g)_k > 0, so accepting −g is the world-k best advice in the advice range. The e_k-minimiser gives that
  advice (R1 Lemma 1.5), so C_{e_k} ∉ M′. Lemma RS needs C_p ∈ M′ for all p.
- **(b) CORRECT (wording).** On E the chart becomes {α > 0}. So B′_q gains g for q ∈ {α>0, d ≤ 0} = (R(−g) ∩ {α>0}) ∪ F(g).
  It loses −g for **every** q ∈ R(−g), including those with α ≤ 0, where the pair falls silent.
- **(c) CORRECT.**
  - With α = 0 at t = r/2 and d = 0 at t = r, we have α(r) > 0. So β(r) = α(r) > 0, and the c′-threshold s exceeds r.
    Silence is {t ≤ r/2} ∩ {t ≥ s} = ∅, and the system is the identity. (G) signs hold.
  - After restriction, the accepted r-set at t ∈ (0.2, 0.4) is {r < t} ∪ (0.4, 2t). That set is not an initial
    segment, so it is incoherent (`checks.py` (6)).
- **Scope repair.**
  - What is proved: the restriction route fails (Lemma RS is inapplicable, and naive deletion can destroy (R1)).
  - What is not proved: that no reduction to a non-adjacent domain exists. Any such reduction plus N15 would *prove* the
    theorem, so non-existence could only be shown by an adjacent realisation.
  - Rephrase the §0 slogan as "Lemma RS gives no WLOG reduction to two-element advice ranges".

---

## 6. §5: N21.6, N21.7, N21.8

**Preamble. CORRECT.**
- Λ_{ab}Λ_{cb} = st·(v_{ac}/v_{aa})·(v_{ca}/v_{cc})/(st) = v_{ac}v_{ca}/(v_{aa}v_{cc}). For T1 this is
  ((1−ε)/(1+2ε))² = β² exactly (sympy).
- With R15's per-pair values Λ ∈ {βx², β/x²} and x₊² > κ = 1/β (R4 G1), each b has exactly one a with Λ_{ab} > 1, at
  both x₊ and x₋ = 1/x₊. Exact, and confirmed for ε ∈ {.01, …, .99}.

**N21.6. CORRECT.**
1. *Step 1.*
   - The chart-form box (N14 §2.3) gives, for a.e. (A′,B′) in the product of witness balls (signs and ratio are open
     conditions), q₀ ∉ R(A′) ∩ R(B′).
   - X × Y null forces X or Y null. So one family has q₀ ∉ R(g) for a.e. member.
   - α_g(q₀) > 0 by the margins: unique clusters (N21.4) give ĉ(g) → ĉ(A_s) uniformly. α is affine, so convergence on
     B₁ is convergence at q₀.
   - On N there is no advice that every evaluable model gives. Advice range {+,0} would give q₀ ∈ R(g). So the advice range is {+,0,−} and d(q₀) ≤ 0.
2. *Step 2.* Every inequality checks:
   - A-case: σ ∈ (q₀, e_a), z ∈ (e_b, q₀];
   - B-case: σ ∈ (e_b, q₀), z ∈ [q₀, e_a);
   - d(σ) < 0 and α(z) > 0, z ∈ cl(F(g) ∩ Ω).
   - `checks.py` (2): 12 962 admissible random charts, 0 violations.
3. *Step 3.*
   - If the d-line misses {α = 0} in Ω, then d < 0 on the convex set {α ≤ 0} ∩ Ω (it contains points near V⁻, where
     α, d < 0).
   - The α-line meets B₁ for small s, and d < 0 on it. So nearby points with α > 0 lie in R(−g) ∩ B₁, contradicting
     N21.2.
   - The d-line and α-line are distinct, since α(z) > 0 = d(z).
4. *Step 4.* d ≥ 0 on α-line ∩ B₁ (N21.2, closure). d ≠ 0 there, because the apex lies outside B₁ (Thm B closure
   clause versus K_q ⊇ K″). d(σ) < 0. So a ∈ (σ, B₁).
5. *Step 5.*
   - λ_{w\*} = line(p\*, e_b) is transversal to the edge at e_b, so σ_m → e_b.
   - A-case: |z_m − e_b| ≤ s_m.
   - z\* ≠ e_a: otherwise V2 and Thm B at d-face points near e_a would give K_{e_a} ⊆ line(e_b, v_{k\*}), contradicting
     e_a ∈ K_{e_a} (Prop V).
6. *Step 6.* (w\*)^⊥ ∩ aff Δ = line(e_b, v_{k\*}), since w\*·e_b = 0 = w\*·v_{k\*}. Hausdorff continuity applies along
   d-face points. ✓
7. *Step 7.*
   - The test gambles lie in N, with h_b = η − δ > 0, h·v_{k\*} = −δ + ηv_{k\*,b} < 0 for η ↓ δ, and h_a > 0 in the
     B-case.
   - z\* = e_b: Lemma 1.5 plus vertex coherence and V2.
   - z\* in the relative interior of the edge: R1 Prop 2.8 on non-null subsets of shrinking balls.
   - The bound t ≤ (η − δ)/(η(1 − v_{k\*,b})) matches brute force at η/δ ∈ {1.5, 1.1, 1.01, 1.001} (`checks.py` (3)).
     N21's own script fixed η/δ = 1.001 and so did not show the limit.
   - So K\* = {e_b}.

**N21.7. CORRECT** (wording in (a)).
- (a) uses L¹-continuity of K ↦ 1_{D_K} at {e_b}, where {h_b = 0} is null. Since B_q contains the unanimous gambles by
  convention, the conclusion is {h_b > 0} ⊆ Av ∪ {h ≥ 0} a.e. (Av: the orientations whose acceptance is in the advice range.)
- (b) a mixed g and −g each have a positive coordinate, and every b has a failing box.
- (c) B_{e_b} ≈ {h_b > 0}.
- (d) R4 (K4) needs exactly that acceptance of a.e. h with h_S > 0 is in the advice range.

**N21.8. CORRECT.**
- (a) N21.4 ⇒ (PC), (NS) ⇒ R15 algebra (x ∈ {x₊, x₋}) ⇒ N21.6, N21.7 at every b.
- (b) is the contrapositive.
- (c) is N15.9(a).
- Hypotheses to state explicitly:
  - (R1) at every interior prior, which gives Hausdorff continuity (N20 §8);
  - Prop V and V2 (vertex coherence is forced, R1 Lemma 1.5).
- The scope remark (general all-facing T: acceptance in the advice range for one world) is CORRECT.

---

## 7. The residuals (N21 §6), and new results

### 7.1 Lemma R23.1 (pinning on a ball around p\*; PROVED here)

**Statement.** Work on any (LF) decomposable domain with (R1), (R2). Let F_k have a crossing τ_c ∈ (σ₁,σ₂) ⊆ [0,1], and let
0 < ρ ≤ r₁. Suppose Ψ(·,σ₁) ≥ 0 and Ψ(·,σ₂) ≥ 0 on B := B(p\*,ρ). Then for every q ∈ B:
- v_k ∈ K_q;
- Ψ(q,·) ≡ 0 on [σ₁,σ₂], and Ψ(q,·) ≤ 0 on [0,1].

**Proof.**
1. *B ⊆ Γ.* Concavity gives Ψ ≥ 0 on B × [σ₁,σ₂]. Take R10b's ball U around w = h(τ_c) so small that:
   - F_k ∩ cl Ũ ⊆ cone h([σ₁,σ₂]);
   - U ⊆ int N₀;
   - R10b's UVN conditions hold (shrinking is harmless; N18 §1.5, N20 §3).

   Homogeneity then gives K_q ⊆ W_{v_k}(Ũ), so B ⊆ Γ_{v_k} (R10b §1).
2. *No d-faces.* B ⊆ B₁, so by N21.2 no good h ∈ U⁻ has a d-face meeting B.
3. *Dichotomy.* Cor PL2 (valid for any open connected G ⊆ Γ_v; N18 §1.5, N20 §3) gives B ⊆ α_{v_k} or B ⊆ β_{v_k}.
4. *p\* ∈ α.* K_{p\*} = T ∋ v_k, and p\* ∈ B. So B ⊆ α, i.e. v_k ∈ K_q on B.
5. *Values.* v_k ∈ K_q gives Ψ(q,τ) ≤ v_k·h(τ) = 0 for all τ ∈ [0,1]. Equality on [σ₁,σ₂] follows from step 1. ∎

**Why this is new.** N15 Lemma 4.1 and N21 apply Cor PL2 to sets G with p\* ∉ G, and must find the α-point far away
(V_j), which leaves B₁. When the set is a ball at p\*, the α-point is p\* itself and nothing leaves B₁.

### 7.2 Corollary R23.2: (E5b) is impossible (PROVED here)

**Setup.** Assume, on a facet F_k, that p\* ∈ cl A_τ for every τ ∈ (0,1) and p\* ∉ cl B_{τ₀} for some τ₀.

1. *A-structure only.* N21.4 items 1–4 use only the A-half of (TS). They give:
   - A_τ ∩ B₁ = H⁺_τ ∩ B₁ with p\* ∈ ∂H⁺_τ, and A_τ ⊆ H⁺_τ globally;
   - n_τ monotone on (0,τ_j) and on (τ_i,1);
   - n_τ continuous on (0,1).
2. *n is constant.*
   - Let D⁻ := B(p\*,ρ₀) ∩ {n_{τ₀}·(q − p\*) < 0}, with ρ₀ ≤ min(r₁, dist(p\*, B_{τ₀})). Then D⁻ ⊆ Z_{τ₀}.
   - If n_{τ₁} ≠ n_{τ₀} for some τ₁, pick q ∈ A_{τ₁} ∩ D⁻.
   - Concavity gives Ψ(q,τ) > 0 strictly between τ₀ and τ₁. So n_τ·(q − p\*) > 0 there, and continuity at τ₀ gives
     n_{τ₀}·(q − p\*) ≥ 0, a contradiction.
   - So n_τ ≡ n on (0,1). (N21's CHECKED claim; this is a complete proof.)
3. *B fails outside [τ_i, τ_j].*
   - For τ < τ_i: if B_τ accumulated at p\*, the c-cluster argument (N21.4 item 5) would give n·(e_i − p\*) ≤ 0, while
     V_i ⊆ A_τ ⊆ H⁺ for τ > τ_i gives > 0.
   - Likewise for τ > τ_j, with j. (N21's PROVED claim; checked.)
4. *A ball where both values are ≥ 0.* Pick τ′ < τ_i and τ‴ > τ_j, and ρ := min(ρ(τ′), ρ(τ‴), r₁). Then Ψ(·,τ′) and
   Ψ(·,τ‴) are ≥ 0 on B(p\*,ρ), because B_{τ′} and B_{τ‴} miss it.
5. *Contradiction.* Lemma R23.1 with σ₁ = τ′, σ₂ = τ‴ and crossing τ_i gives A_{τ_i} ∩ B(p\*,ρ) = ∅. This contradicts
   p\* ∈ cl A_{τ_i}. ∎

**Consequences.**
- (TS) ⇔ (TS_A): on each facet, the A-half implies the B-half.
- Failure of (TS) means (E5a) on some facet.

### 7.3 Prop R23.3: refined (E5a) (PROVED here)

**Setup.** In (E5a) at τ, N21.9 gives σ₁ < τ < σ₂, a crossing τ_c ∈ (σ₁,σ₂), and an open pinned set
O ⊆ G := int(P_{σ₁} ∩ P_{σ₂}).

**Statement.**
- For 0 < η ≤ η₀ (with [τ_c ± η₀] ⊆ [σ₁,σ₂]), the convex open set G_η := int(P_{τ_c−η} ∩ P_{τ_c+η}) ∩ B₁ satisfies:
  - G_η ⊇ O;
  - G_η ⊆ Γ_{v_k}(U_η);
  - G_η has no d-faces.

  Cor PL2 then gives G_η ⊆ α. So Ψ(q,·) ≡ 0 on [τ_c ± η] for q ∈ G_η.
- Hence A_{τ_c} ∩ B₁ = ∅: a point of A_{τ_c} ∩ B₁ lies in some G_η by joint continuity, and pinned points have
  Ψ(·,τ_c) ≤ 0.
- Also A_{τ_c−η} ∩ A_{τ_c+η} ∩ B₁ = ∅.

**Sub-cases.**
- If moreover B fails at two parameters straddling τ_c, Lemma R23.1 gives pinning on a whole ball around p\*.
- So (E5a) splits into a **ball-pinned** case and a **thin** case, where the pinned set has p\* on its boundary.

**Why neither case closes locally.** Ball pinning of a single vertex is consistent with every constraint at priors in B₁
(compare Prop L). Theorem PL excludes only *two* vertices pinned on a common open set, so at most one facet can be
ball-pinned on a given ball. Excluding (E5a) needs the walls of §7.4, at priors where K_q ∩ K″ = ∅.

### 7.4 N21.9 and the wall heuristic

- (i)–(iii) are CORRECT as proved:
  - concavity forces Ψ(q,·) ≡ 0 on [σ₁,σ₂] from an interior zero;
  - the wedge argument gives v_k ∈ K_q;
  - Lemma M on int conv(O ∪ V_j), which lies in Γ by chart convexity, is adjacency-tolerant;
  - precise Q gives {v_k·h > 0} ⊆ Av ∪ {h ≥ 0}.
- The paragraph "each exterior h near the crossing is silent on O … along (Q, e) it must cross a d-face" holds only in
  a qualified form:
  - At o ∈ O, h is rejected (v_k ∈ K_o). −h is rejected iff some m ∈ K_o has m·h ≥ 0. By the Lemma M step 1 estimate,
    m·h ≥ c₀|m − v_k| − |h − w′|, so this holds once |h − w′| ≤ c₀·max_{m∈K_o}|m − v_k|, and it fails if
    K_o = {v_k}. So "silent" needs K_o ≠ {v_k} and h close to the facet relative to o.
  - With o ∈ S(h), N21.3 then gives the d-face crossing on (Q,e).
  - Without o ∈ S(h), §3 shows the passage can avoid F(h).
  - Label: CHECKED.

### 7.5 Cor R23.4: acceptance of at least one orientation is in the advice range (PROVED here)

**Statement.** In every T1 realisation on an (LF) decomposable domain, the advice range of a.e. mixed pair contains acceptance of at least one orientation.

**Proof.**
- If (TS) holds: N21.7(b).
- If not: R23.2 gives (E5a) on some F_k. N21.9(ii)–(iii) give an interior Q with K_Q = {v_k}, so {v_k·h > 0} ⊆ Av a.e.
  For a.e. mixed g, exactly one of ±g has v_k·(±g) > 0. ∎

**Corollaries.**
- No realisation exists on (LF) domains with a non-null set of mixed pairs whose advice range is ⊆ {0, ×} (in particular, mixed pairs on which every evaluable model gives no advice).
- If no evaluable model accepts the orientations in a non-null set of mixed orientations, then (TS) fails, and these orientations lie a.e. in
  {v_k·h ≤ 0} for every pinned k.

### 7.6 (E4′)

- The description is CORRECT given N21.6–N21.7.
- "No argument local to the vertices can close (E4′)" rests on R4 §9: one identity cap at ε = 0.2, numerics plus a hand
  edge blow-up. Label it NUMERICS/CHECKED.
- The case a\* ∈ Ω (apex at finite distance on the crossing chord) is not covered by that evidence. There, N21.6(iii)
  gives K_{a\*} ⊆ line(e_b, v_{k\*}) at an interior prior on λ_{w\*}. It may be the more promising place to look for a
  contradiction.

---

## 8. What is now proved for T1 on general decomposable domains with (LF)

**Hypotheses** (labelled ★ below):
- a strictly guiding additive system on a decomposable domain M;
- integral penalties, or bounded charges vanishing on null sets given interior Bayes minimisers (N14 Thm C2);
- (LF) at T1 (any ε ∈ (0,1));
- (R1) at every interior prior;
- (R2) at an interior p\*.

**Theorem (N15 + N21 + N23; PROVED).** Under ★:

1. **Local structure (every M).**
   - q ↦ P(q,g) is quasi-concave on Ω for every g.
   - On B₁ = B(p\*, r₁), where K_q ⊇ K″, near-facet gambles have no d-faces and no acceptance of −g. Their charts are
     half-planes.
2. **Dichotomy.** Exactly one of the following holds.
   - **(I) (TS) holds**, equivalently (TS_A). Then:
     - (PC) and (NS) hold;
     - the advice range of a.e. mixed pair contains both acceptances;
     - K_{e_b} = {e_b} for every b;
     - interior limits at edge priors lie in the edge face;
     - at every vertex b the failing box is cut by d-faces F(g_m) ∩ Ω = (a_m, z_m), with a_m → a\* ∈ [e_b,p\*] ∖ B₁,
       z_m → z\* ∈ [e_b,e_a), K_q ⊆ line(e_b, v_{k\*}) on [a\*,z\*] ∩ Ω, and K_{q_m} → {e_b}.
   - **(II) (TS) fails.** Then some facet F_k is pinned:
     - an open convex G with p\* ∈ cl G on which v_k ∈ K_q and Ψ_k(q,·) ≡ 0 on an arc around a crossing τ_c;
     - A_{τ_c} ∩ B₁ = ∅;
     - every segment from G to V_l contains an interior Q with K_Q = {v_k};
     - {v_k·h > 0} ⊆ Av a.e.
3. **Non-existence.** There is no realisation on M if any of the following holds:
   - (a) a.e. pair meeting U′ is non-adjacent (N15; e.g. the U-domain, whose evaluable models are the measurable subsets of U = D_{K′}; two-element advice ranges near ∂T; full-dimensional K_q);
   - (b) M satisfies (TS) and a non-null set of mixed pairs has an advice range lacking one acceptance (N21.8);
   - (c) a non-null set of mixed pairs has an advice range containing neither acceptance (R23.4, new);
   - (d) every facet satisfies (TS_A), and a non-null set of mixed pairs has an advice range lacking one acceptance (R23.2 + N21.8, new
     formulation without the B-half).

The same holds for every all-facing triangle in general position, with "every b" in (I) replaced by the worlds b that
have a failing box.

**Open (precise).**
- **(E5a)** on domains where the advice range of a.e. mixed pair contains acceptance of at least one orientation: single-vertex pinning near p\* across a
  crossing, ball-pinned or thin, shielded by precise {v_k} walls outside B₁.
- **(E4′)** on domains where the advice range of a.e. mixed pair contains both acceptances (the all-model domain in particular).

**CONJECTURE N21 (now: (E5a) and (E4′) do not occur)** is unrefuted. No construction is known.

**Nearby targets suggested by this round.**
1. *Ball-pinned (E5a).* B(p\*,ρ) ⊆ {v_k ∈ K_q}. Combine with (I) or (II) on the other two facets: two ball-pinned facets
   are excluded by Theorem PL. So the case reduces to one pinned facet plus two (TS_A) facets, a three-way finite
   configuration.
2. *(E4′) with a\* ∈ Ω.* At an interior prior on the crossing chord, K ⊆ line(e_b, v_{k\*}) is a precise-type
   degeneracy. Test it against N21.1 (quasi-concavity), whose superlevel sets must be convex along the whole chord
   λ_{w\*}.

---

## 9. Requested edits to N21

1. §2 Remark: replace "⇔" with the per-g wedge criterion of §2; cite the adjacent identity counterexample.
2. N21.2: state it pointwise for good g on {K_q ∩ K″ ≠ ∅}, with the null set independent of C.
3. N21.4 item 1: replace I_g by {c : h − c𝟙 ∈ int N₀}.
4. N21.5 and §0 item 4: change the slogan to "Lemma RS gives no WLOG reduction". Fix the wording of (b).
5. N21.7(a): add "∪ {h ≥ 0}".
6. N21.9: relabel the paragraph after the proof as CHECKED, adding the proximity condition and the o ∈ S(h) requirement.
7. §6 (E5b): replace with R23.2, i.e. (E5b) is impossible. Then §0 item 6's last sentence becomes true.
8. §6 (E4′): relabel "no argument local to the vertices can close (E4′)" as NUMERICS/CHECKED.
9. N21.8: list (R1) at every interior q, Prop V and V2 among the hypotheses explicitly.
10. `lemmas_check.py` (2): vary η/δ so that the → 0 claim is visible.

---

## 10. Files (`n23py/`)

| File | What | Result |
|---|---|---|
| `checks.py` (1) | Exact Λ product for T1; βx₊² versus 1 | difference ≡ 0 (sympy); βx₊² ∈ [1.37, 300] > 1 and β/x₊² < 1 for ε ∈ [.01, .99] |
| (2) | N21.6 step-2 bookkeeping on random (G)-sign charts for the advice range {+,0,−} with α(q₀) > 0 ≥ d(q₀) | 12 962 charts, 0 violations |
| (3) | N21.6(iv): brute-force admissible t on line(e_b, v_k) versus formula, η/δ → 1 | agreement to 1e-5; t_max = 0.476 → 0.0014 (ε = .1) |
| (4) | Precise identity system with adjacent data | strict signs, charts = identity, empty silence, all 1 508 pairs adjacent; P affine ⇒ quasi-convex |
| (5) | N21.3 hypothesis check | 207 segments R(±g) → S → R(∓g) not starting in S |
| (6) | N21.5(c) exact acceptance sets | incoherent at t = .25, .3, .35; coherent at .15, .5 |
| `checks.out` | output of the above | |

All numerics are sanity checks. The verdicts rest on the hand derivations in §§2–7. Lemma R23.1 and Cor R23.2 are new
and are proofs, not numerics. They use only refereed tools (Cor PL2 on arbitrary open connected G ⊆ Γ_v; N21.2; N21.4
items 1–5), but a second reader should check them before they are relied on.
