# Second referee report: Thm TSalways and its satellites (14 Oct 2026)

I wrote none of N21, N23, N28, R10b or their referee reports. Every step listed below was re-derived from the
statements of the cited lemmas, not from the first referees' reports. I read them only afterwards, to compare.

**Read.**
- BRIEF9; writeup §§2–5 (*The Contamination Triangle.tex*).
- N28_notes in full; N28_referee in full.
- N21_notes in full; N23_referee in full; R10b_notes in full.
- R12_referee (summary table); CHECK_REPORT §1.
- I1_notes, I2_notes and C2_notes in full, for their uses of these inputs.

**Scripts.** `ts2ref_py/checks.py`, with output in `checks.out`. All NUMERICS are sanity checks only, and every verdict
rests on the hand derivations.

**Scale.** CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG.

---

## 0. Verdicts

| # | Item | Verdict |
|---|---|---|
| 1 | **Thm TSalways** (N28 Prop 3.1, Lemmas 3.2–3.4, Thm 3.5) | **CONFIRMED** |
| 1a | N21.9 (i)–(iii) (walls of an A-failure) | CONFIRMED |
| 1b | Thm N21.4 = writeup Thm TS (items 1–5 re-derived; items 6–8 spot-checked) | CONFIRMED |
| 1c | R10b Lemma UVN, Lemma D, Lemma M, Cor PL2, Lemma P, Thm PL | CONFIRMED (R12's wording repair: β_v is *relatively* open in Γ_v) |
| 1d | Lemma R23.1, Cor R23.2 | CONFIRMED |
| 1e | N21.1, N21.1′, N21.2 (Lemma B1, pointwise form), Lemmas 2.1–2.4 (walls) | CONFIRMED |
| 2 | Cor TSalways (b), (c): both acceptances in the advice range a.e.; K_q → {e_b}; edge confinement (N21.6, N21.7, N21.8(b)) | **CONFIRMED** |
| 3a | Thm cuts (N21.6) | **CONFIRMED** |
| 3b | Thm apex (N28 Thm 4.1): a\* = e_b | **CONFIRMED WITH REPAIR** (the sentence on competition, §3.3) |
| 4a | Lemma R1 (chords separate Ω globally) | **CONFIRMED** (this is the second reading) |
| 4b | Prop vertexfree (i)–(iv) | **CONFIRMED** (one unsupported sentence elsewhere in §5.3 of the writeup, §4.3) |
| 5 | N28 Prop 5.1 (⇒), in the every-q chart form used by I1 | **CONFIRMED WITH REPAIR** (citation and measurability, §5) |

**No GAP and nothing WRONG** was found in any proved statement.

There are two overclaims in the writeup's prose, and one caveat on how the cluster clause may be used:
- **Overclaim.** The sentence "competition … at a positive distance from ∂Δ is impossible" appears in Thm apex, in the intro
  and in §5.3 (E4′). It is not proved: only the *cut* d-faces of Thm cuts are shown to go to ∂Δ.
- **Overclaim.** §5.3 says the non-precise layer pokes "beyond both ℓ and ℓ′ on the chord". This is not proved, since on λ_b only
  ≤ 0 is known. C2 Cor 3.3 asserts the opposite.
- **Caveat.** The vector-level cluster clause (I1's (C3)) is proved only at relative-interior facet gambles, not at
  corner rays.

None of these affects any use made by I1, I2 or C2 (§6).

---

## 1. Thm TSalways

### 1.1 Inputs, re-derived

**N21.1 (quasi-concavity, every g).**
- Take P(q_i,g) > c and pick c′ ∈ (c, min P(q_i,g)). Choose good g″ → g − c′𝟙.
- By (1.1), q_i ∈ cl R(g″). The set cl R(g″) is convex, because every chart in R1's table is convex.
- By (1.1) again, P(·,g″) ≥ 0 on [q₁,q₂]. Passing to the limit gives P(·,g) ≥ c′ on [q₁,q₂].
- (1.1) itself: {P > 0} is open and a.e. equal to R. So {P > 0} ∖ cl R is open and null, hence empty; and P ≥ 0 on cl R
  by continuity.
- No N₀ and no goodness of g itself is needed. ✓
- N21.1′ follows from convexity of A_τ. ✓

**N21.2 / Lemma B1 (pointwise).** For good g ∈ N₀ and any q with K_q ∩ K″ ≠ ∅:
- P(q,−g) < 0, so q ∉ cl R(−g) by (1.1);
- Thm B on cl F(g): F(g) ⊆ cl R(g) ∩ cl R(−g), so P(q,±g) ≥ 0 there and K_q ⊆ g^⊥, which is impossible here;
- hence {c > 0} ⇒ d > 0.

The exceptional g-set does not depend on q. ✓

**R10b.**
- *UVN.*
  - (a) Dominated convergence at e_i gives x⁻ ∈ D_{K_q} near e_i. The half-ball bound has uniform Gaussian mass. Upward
    closure then gives P(q,h) > 0 for **all** h ∈ B₁ and **all** q ∈ V_i ∩ Ω.
  - (b) Use downward closure, with an orthant fraction of a ball centred at x⁺. ✓
- *Lemma D.* The identifications α = {v ∈ K_q} and Γ ⇔ K_q ⊆ W_v(U) were re-derived, with the gamble w′ − t𝟙 for v ∉ K_q
  and the estimate m·w′ ≥ c₀|m − v|. β is relatively open in Γ. ✓
- *Lemma M.*
  - Step 1: d-face points of h with |h − w′| < c₀ρ force K_p ⊆ B(v,ρ).
  - Steps 2–3: the chart lines of h± pass through Q; H₊ ∩ B ⊆ cl(β ∩ B) ⊆ cl H₋; hence a₊ = λa₋ with λ > 0.
  - Step 4: (a₋)_c ≤ 0, while UVN(a) at w₊ forces a₊ ≥ 0 on V_c ∩ Ω. A zero at e_c would make the line through e_c and
    Q cut V_c, so (a₊)_c > 0.
  - Sequences only; no continuity in g. ✓
- *Cor PL2* is Lemma M with Step 1 replaced by the no-d-face hypothesis. ✓
- *Lemma P.* Near A ∈ Z_v, K_q ≈ {v}, and v·h > 0 on all of U_{v′}, so a ball B_A ⊆ Γ_{v′} ∩ β_{v′}. Lemma M on
  int conv(O ∪ B_A) then applies, and the first point of cl β on [o,A) is a Z_{v′} point. ✓
- *Thm PL.* Take the nearest point A₁ of Z_v ∪ Z_{v′} on [o,A]. Lemma P, with the roles chosen by which set A₁ lies in,
  gives a nearer point. Shrinking U_v or U_{v′} only enlarges Γ and leaves α, β and Z unchanged. ✓

**N21.4 (Thm TS).**
- *Item 1.* The local straight levels of Lemma levels hold on B₁, with levels |t| < c̄ ((N1)–(N2)).
  - {f ≤ t} ∩ B₁ = ∩_{t′∈(t,t+η)} Π⁻_{t′} ∩ B₁, using "f ≥ t′ on Π⁺_{t′}".
  - Complementary convex sets in B₁ are separated by a line. ✓
- *Item 2.* Under (TS) at τ, the two lines through p\* do not cross in B₁, so they coincide. ✓
- *Items 3–4* use only the A-half.
  - Betweenness: n_σ ≠ −n_{σ′}, because A_σ ∩ A_{σ′} ⊇ V_j ∩ Ω and A ⊆ H⁺ globally.
  - The jump double-wedge W ∪ −W lies in the convex set Z_{τ₀} ∩ B₁, so Z_{τ₀} contains a neighbourhood of p\*,
    contradicting p\* ∈ cl A_{τ₀}. ✓
- *Item 5 (c-clusters).* Take q ∈ A_τ ∩ B₁. Then P(q,g_m) > 0 for large m, so q ∈ cl R(g_m) ⊆ {c(g_m) ≥ 0}, and ĉ·q ≥ 0.
  Symmetrically on B_τ. So the line of ĉ is λ_τ, with the same positive side.
  - ĉ is not ∝ 𝟙, because its weak signs are mixed.
  - So ĉ·e_l ≤ 0 whenever h(τ)_l < 0. This holds for **every** good sequence and every cluster. ✓
- *Items 6–8* (no sliding, rotation, regularity, blow-up, projectivity).
  - Spot-checked: every step uses only B₁, levels |t| < c̄, anchors with ξ < r₁/2, and the cap lemma at single priors.
  - This is the N15 chain, refereed twice, localised. ✓

**R23.1, R23.2.**
- R23.1, step 1: K_q lies in the wedge {m·h(σ₁) ≥ 0, m·h(σ₂) ≥ 0}, which is contained in W_{v_k}(Ũ), so q ∈ Γ.
- Step 2: Lemma B1 on B ⊆ B₁ excludes d-faces.
- Steps 3–4: PL2 applies on the ball, and p\* ∈ α because v_k ∈ T.
- R23.2: n is constant, by continuity and concavity (also when n_{τ₁} = −n_{τ₀}).
  - Accumulation of B at τ < τ_i would give n·(e_i − p\*) ≤ 0 by c-clusters, against > 0 from V_i ⊆ A_τ for τ > τ_i.
  - Then R23.1 on [τ′, τ‴] ∋ τ_i contradicts p\* ∈ cl A_{τ_i}. ✓

**N21.9.**
- G = int({Ψ_{σ₁} ≥ 0} ∩ {Ψ_{σ₂} ≥ 0}) is convex with nonempty interior (UVN at the shared positive coordinate). So
  p\* ∈ cl G.
- On O, an interior zero of a concave function that is ≥ 0 gives Ψ(q,·) ≡ 0 on [σ₁,σ₂], hence v_k ∈ K_q.
- int conv(O ∪ V_j) ⊆ Γ: for good h ∈ U⁺, the open convex R(h) contains a.e. point of O and of V_j ∩ Ω, hence their
  hull. Then use Fubini and the open-cone fact.
- On [o,v], the first point of cl β (which may be o itself) lies in ∂_{G′}β, so it is a {v_k} prior.
- So **every** segment from O to V_j ∩ Ω meets the **single global** set Z_{v_k}.
- The Option 1/2 bookkeeping (j = l = the shared coordinate) checks against Lemma signs. ✓

### 1.2 The cascade

- **Prop 3.1.**
  - Step 2 needs (TS) only at τ₁ on F_i, and its conclusion refutes that, so there is no circularity.
  - Step 3: if n·(e_l − p\*) = 0, one edge direction at e_l has negative slope, since otherwise e_l would minimise n·x
    over Δ and p\* could not be interior.
  - Step 5: n·(x − p\*) ≤ (1−t)δ − tb, so t < δ/(δ+b) and |x − p\*| ≤ δ(1 + 2/b). Here v, and hence b, is fixed before δ.
  - Step 6: Q ∈ Z_{v_m} ⊆ A^i_{τ₁} ⊆ H⁺ (Lemma 2.4, i ≠ m), and dist(p\*, Z_{v_m}) > 0.
  - **CONFIRMED.** (`checks.py` (7): 0 violations of the estimate.)
- **Lemma 3.2.** R23.1 puts B(p\*,ρ) in Γ_{v_l} ∩ α_{v_l}. Then O ∩ B(p\*,ρ) is open, nonempty and lies in
  Γ_{v_m} ∩ Γ_{v_l} with v_m, v_l ∈ K_q, which contradicts PL. **CONFIRMED.**
- **Lemma 3.3.** No β-straddle of τ_x and none of τ_y give the three cases. The Option endpoints τ₀ = τ_x and τ₀ = τ_y
  are admissible. **CONFIRMED.**
- **Lemma 3.4.**
  - |Q_i − p\*| ≤ δ + √2 t_i, so t_i ≥ (d−δ)/√2.
  - 0 ∈ int conv{e_i − p\*} is an open condition.
  - The weights λ_i/t_i give p\* ∈ conv{Q_i}.
  - **CONFIRMED.** (`checks.py` (6): 2998 trials, 0 failures of either the bound or the conclusion.)
- **Thm 3.5.**
  - Step 1 is R23.2; step 2 is Lemma signs; step 3 is Lemma 3.3.
  - Step 4 applies Lemma 3.4 with (a,b,c) = (m,n,l), Z = Z_{v_l} and Z′ = Z_{v_m}; p\* ∉ Z ∪ Z′ because T is not a
    singleton.
  - Step 5: Lemma 2.4 with i = n, and convexity of A^n_τ ∌ p\* (N21.1, which holds for every g).
  - **CONFIRMED.**

**Quantifier audit.**
- *"For every q" (true pointwise).* (TS), A_τ, B_τ and Z_{m₀} are pointwise sets. (1.1), Lemma B1, Lemma 2.3 and UVN's
  P-clause hold for every q.
- *"For a.e. g" (only through good gambles).* Good gambles enter only as approximants (N21.1, the c-clusters, Lemma M)
  or as a.e. choices (UVN's chart clause).
- *Specific gambles* (h(τ), w\*\*, 𝟙 − e_b, m₀ − m + t𝟙) are used only through P, which is defined for every g.
- *Continuity.* No continuity of c(·) in g is used anywhere; every limit is a cluster along a sequence.
- *Chart shape.* Half-plane charts are used only on B₁ (Lemma B1) or after Lemma M Step 1 has excluded d-faces in a
  ball. Global statements use only convexity of charts (quasi-concavity), so they tolerate three-ray charts.

---

## 2. Cor TSalways (b), (c)

The chain is (TS) ⇒ (PC), (NS) ⇒ x ∈ {x₊, x₋} ⇒ a failing box at every b ⇒ N21.6 at every b ⇒ N21.7. Checks:
- *Failing box at every b.* With x₊² > κ, i.e. x₊ > √κ (from x + 1/x = κ + 1 > √κ + 1/√κ), and transposition for x₋,
  each b has exactly one failing a. (`checks.py` (3): x₊²/κ ∈ [1.90, 29.96] and x₋²κ < 1.)
- *N21.7(a).*
  - B_{q_m} ∈ 𝓜, so its accepted set lies in Av ∪ {h ≥ 0} a.e.
  - K_{q_m} → {e_b} gives 1_{D_{K_{q_m}}} → 1_{h_b>0} in L¹(μ): P_{K_m} → h_b uniformly on bounded sets, and
    {h_b = 0} is null.
- *(b).* Every mixed g and −g has a positive coordinate. ✓
- *(c).* K_{e_b} = {e_b} by coherence of B_{e_b} ≈ {h_b > 0}. Then V2 gives K_q → {e_b}.
- *Edge confinement.* Take h = (1,1,−M) at a prior with support {a,b}. Accepting it is in the advice range by (a), and it
  is strictly best at q₀ with a margin. Dominated convergence gives m_a + m_b ≥ M m_c for every M, so m_c = 0. ✓

**CONFIRMED.** One dependency note follows.

**Dependency note.** (b) and (c) rest on N21.6, whose Step 1 uses the **chart-form edge box** (N14 §2.3). That box was
re-derived here: on O = R(A′) ∩ R(B′) ∩ Ω near q₀, P(·, A′+λB′) > 0, which contradicts Lemma FS at q₀.

So I1's statement that "**the box is not used**" holds only for I1's new argument. Its inputs (C1) and (C4) come
through Cor TSalways (b), (c), and those use the failing box (via N21.6). This is not a gap, but I1 §0 should say so.

---

## 3. Thm cuts, Thm apex

### 3.1 Thm cuts (N21.6): CONFIRMED

Steps 1–7 were re-derived.
- *Margins.* c(g)·q₀ > 0 for good g near A_s. This follows from **vector** cluster uniqueness:
  - an affine function on aff Δ is the restriction of a unique linear functional on ℝ³;
  - so the zero line on B₁ plus the positive side fixes ĉ.
- *Product-null argument.* It gives one family in which a.e. member has q₀ ∉ R(g).
- *Step 2.* The A-case and B-case sign tables are correct.
- *Step 3.* The apex lies in Ω, by the B₁ contradiction with R(−g).
- *Step 4.* The apex lies outside B₁, by Thm B together with K_q ⊇ K″.
- *Step 5.* z\* ≠ e_a, by V2 and Prop V.
- *Step 7.* The test gambles give t ≤ (η−δ)/(η(1 − v_{k\*,b})), which tends to 0.

**Statement repair (cosmetic).** The hypotheses "(PC), (NS)" must be read as including the cluster clause of (PC) and
Lemma B1 (N₀, K″, r₁). These hold in the setting where the theorem is used.

### 3.2 Thm apex (N28 Thm 4.1): mathematics CONFIRMED

- *Step 1.* By Fact 4.0′, P(q,w\*\*) = t·v_{k\*}·w\*\* ≥ 0 on [a\*,z\*] ∩ Ω. (`checks.py` (1): min v_{k\*}·w\*\* = 0.108 > 0.)
- *Step 2.* (a\*, z\*] ⊆ H⁻ (open). The triangle conv(I ∪ {q₁}) carries P = 0 and meets B₁ ∖ λ_b, which contradicts
  Z ∩ B₁ = λ_b ∩ B₁.
- *Step 3.*
  - On [x,a\*] ⊆ λ_b ∩ Ω, P ≥ 0 by convexity and P ≤ 0 by N21.1′. So P(a\*,w\*\*) = 0 and e_b ∈ K_{a\*}.
  - Separating a\* from the open convex C_b ∋ p\* gives φ < 0 on (a\*, e_b].
  - The d-faces pass through B(y,r), which contradicts Lemma 2.3 (pointwise for good g_m, with (g_m)_b ≠ 0).
  - ✓
- *Orientation.* `checks.py` (2): for x± and every b, both b-crossing chords are line(u,e_b), with the strict
  orientations used (0/60 violations).

### 3.3 Repair: "competition at a positive distance from ∂Δ is impossible"

The writeup states this in Thm apex, in the intro (l. 65: "competition … can occur only in neighbourhoods of the vertices
that shrink to the vertices") and in §5.3 (E4′). BRIEF9 repeats it.

**What is proved** is narrower: for every sequence of cut gambles as in Thm cuts,
- a_m → e_b;
- the d-faces (a_m, z_m) converge into ∂Δ: to {e_b} in the A-case, and to [e_b, z\*] in the B-case.

**Why the broader claim is not proved.** Nothing excludes an adjacent pair, far from ∂D_T, with d-face points at some
fixed interior q. Such a q needs only dim K_q ≤ 1 with K_q ⊆ g^⊥. The constraints proved so far forbid that only on B₁
and on the crossing chords (non-precise, but possibly segments).

**Repair.** Replace the sentence by "the cut d-faces of Thm cuts converge into ∂Δ, with apexes at e_b".

**Verdict.** CONFIRMED WITH REPAIR. No proof in N28, I1, I2 or C2 uses the broad form (§6).

---

## 4. Lemma R1 and Prop vertexfree

### 4.1 Lemma R1: CONFIRMED (second reading)

1. Suppose q₁ ∈ H⁻ ∩ Ω has P(q₁, h(τ)) ≥ 0.
2. The convex set {P ≥ 0} then contains conv(λ_τ ∩ B(p\*,r₁/2) ∪ {q₁}) ⊆ Ω ∖ H⁺.
3. On that set P ≤ 0 (N21.1′), so P = 0 there.
4. The segment [p\*, q₁] lies in it and leaves λ_τ inside B₁, which contradicts Z_τ ∩ B₁ = λ_τ ∩ B₁ (TS).

This holds for every all-facing T in general position.

### 4.2 Prop vertexfree: CONFIRMED

- **(i)** We have φ(y) = Σ y_i φ(e_i) = 0 with y_i > 0 and φ(e_a), φ(e_c) ≥ 0 (as limits).
  - If φ(e_b) = 0, then φ ≡ 0 on aff Δ, which is impossible.
  - So φ(e_b) < 0. The apexes a_m ∈ Ω converge to e_b (Thm apex, which needs a failing box at b, true for every b of T1).
    This contradicts Lemma 2.3.
- **(ii), (iii)** follow from Lemma R1 and Fact 4.0.
  - Fact 4.0 was re-derived (αγ(w′_c w_a − |w′_a||w_c|) ≤ 0, with the bracket > 0 from int T).
  - LP check: max(1 − m_b) = 0 (`checks.py` (1)).
  - Distinctness of the two points uses (i).
- **(iv)** A singleton on λ_b must be e_b, which (i) excludes.

### 4.3 A related sentence that is not supported

§5.3 of the writeup, and BRIEF9, describe the non-precise layer as "poking … beyond both ℓ and ℓ′ **on the chord**".

- On λ_b, Lemma R1 gives only P(q,w′) ≤ 0 and P(q,w) ≤ 0. Strictness holds only on the open sides.
- So "beyond both on the chord" is unproved.
- C2 Cor 3.3 claims that on λ_b, K_q stays inside the tangent wedge, touching ℓ′ and ℓ.
- No proved statement conflicts with C2 here. The §5.3 bullet should be corrected to "meets both ℓ′ and ℓ (≤ 0); strictly
  beyond ℓ′ on the open e_a-side and beyond ℓ on the open e_c-side".

---

## 5. Prop 5.1 (⇒), every-q form: CONFIRMED WITH REPAIR

**Derivation.** For each interior q:
- the g-section of {(q,g) : 1[q ∈ R(g)] ≠ 1[P(q,g) > 0]} is null, because of a.e. uniqueness of the q-Bayes model at
  **every** q (Prop necessary (a)) and B_q ≈ D_{K_q} ∪ {h ≥ 0};
- × is never a minimiser when anything else is in the advice range (strict (G)).

Then:
- Fubini gives a co-null set of g whose q-sections are null.
- For such g, R(g) ∩ Ω and {P(·,g) > 0} are open, convex (N21.1) and a.e. equal, hence equal (cl A = cl B and int cl = id
  for open convex sets). This holds **at every q**.
- With both acceptances in the advice range (Cor TSalways(b)):
  - {+,0,−} charts are {c > max(0,c′)} and {c′ > max(0,c)}, with the penalty c and c′;
  - {+,−} charts take the data (λd + e₀𝟙, (λ−1)d + e₀𝟙). `checks.py` (5): strict signs and identical cells, 0
    violations.
- Consequences for I1 (C1):
  - on cl W⁺(g) ∩ cl W⁻(g), K_q ⊆ g^⊥;
  - on S(g), K_q meets ℓ_g.
  - ✓

**Repairs.**
1. *Hausdorff continuity on a general decomposable domain.* Cite R1 Prop 3.1 (L¹-continuity of q ↦ B_q, then the
   homeomorphism K ↦ 1_{D_K}). Do not cite Prop reduction, which is stated for U-domain realisations.
2. *The good set.* State that it is the intersection of the co-null sets for g and for −g. Also state joint
   measurability of (q,g) ↦ 1[q ∈ R(g)]; it holds because c, c′ and A(·) are measurable in g, so Fubini applies.
3. *Non-uniqueness of CF data.* CF data are not unique: the apex of the three rays may lie outside Ω. Downstream uses of a
   *specific* c(g) (I1 Prop E, Thm R, Lemma S; I2 Lemma 1; C2 Lemma 3.1) are legitimate. For g in the collar N₀ the
   advice range contains silence, so c is the penalty vector.
   - On B₁, the chart line of c is fixed up to positive scale by R(g) ∩ B₁ = {c·q > 0} ∩ B₁. That is what (C3) concerns.
   - For bare CF solutions, Prop CF (⇐) builds penalties from the given data, so the same reading applies.

---

## 6. Consequences for I1, I2, C2

I found no gap. No use made by I1, I2 or C2 is invalidated. Specific points:

**I1**
- **(C1)** CONFIRMED in exactly the stated every-q form (§5).
- **(C2)** CONFIRMED (Thm TSalways).
- **(C3)** CONFIRMED as vector convergence, for every good sequence g → h with h in the normalised facet segment of
  relint F_k.
  - Caveat: it is **not** proved at corner rays, where Thm pivot covers only τ ∈ (0,1) and (TS) is not asserted.
  - In Prop E, ĥ = h_j(z(t)) is a corner ray at the two piece boundaries t = c₀ and t = 1 − c₀. Those finitely many t
    must be excluded.
  - This is harmless: (ii) "strictly straddles t" is open in t, and (i) is an inf/sup over t.
- **(C4)** CONFIRMED.
- §0's "the box is not used" should read "not used beyond the inputs", because (C1) and (C4) rest on N21.6, whose Step 1
  is the chart-form box.
- I did not referee I1's own steps.

**I2**
- Inputs used: Thm TSalways ((TS), (PC), (NS), edge confinement, K → e_b), the cluster clause for **every** good g → h
  (I2's check-first item 1), N21.1′, and Prop vertexfree (i), (iii).
- All are CONFIRMED.
- The phrase "competition (cuts) at non-precise priors cannot escape" is I2's own claim (its Theorem 3). It does not rest
  on the overclaim of §3.3.

**C2**
- Inputs used: Prop CF(⇒), Cor TSalways, crossing rows, N21.1′, Prop vertexfree (i), (iv), Fact 4.0. All are CONFIRMED.
- Lemma 3.1 step 4 is the cluster clause at relint facet gambles. ✓
- C2 Cor 3.3 contradicts only the unproved §5.3 bullet (§4.3), not any proved input.

**Status upgrade for the writeup.** Each of these now has two independent readings:
- Thm TSalways, Cor TSalways, Thm cuts, Thm apex (with the wording repair), Lemma R1, Prop vertexfree and Prop CF(⇒);
- their inputs N21.4, N21.9, R10b UVN/M/PL and R23.1/R23.2.

Prop CF(⇐) and Thm CCIBU were not in scope.

---

## 7. Files

`ts2ref_py/checks.py` and `checks.out`. All results below are NUMERICS:
1. Fact 4.0 LP (max 0) and Fact 4.0′ (min 0.108).
2. Chord orientations (0/60).
3. x₊²/κ > 1 and x₋²κ < 1.
4. Lemma signs (0 violations).
5. {+,−} → CF conversion (0).
6. Surround lemma (0/2998).
7. Prop 3.1 estimate (0/20 000).
8. Lemma 2.1 gamble (0).
