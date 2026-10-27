# REFEREE_round57. Referee report on PP69, PP70, PP71 (round 57) and on BRIEF58's structural facts

24 October 2026. Independent referee for round 58. I read BRIEF58, BRIEF57, AUDIT_round58 and its answers, LEAD_selection_count §1, AUDIT_completion, the PP59 ledger, DESIGN_MEMO §8.26 and its correction bullets, PP57 §4, BRIEF52 and AUDIT_posterior_pairs, PP68 §1, and REFEREE_round55 Prop G and REFEREE_round56 §1.7 where they were cited.

**Labels.**
- PROVED: I checked the argument, or I give one here.
- CHECKED: an exact computation I implemented myself, in `r9/REFEREE57_py/`. None of the authors' scripts is imported.
- NUMERICS / CONJECTURE: as usual.

**What I re-implemented.**
- **The round-57 curve and PP69's field** (`curve57.py`, `field57.py`). Exact rationals on 2,500 random problems.
- **Exact incoherence certificates** for 𝒲's off-arc Bayes acts (`offarc57.py`).
- **The rescaling loop on the posterior family** (`loop57.py`, `loop57b.py`). A complete chamber census, found by LP feasibility over every sign vector. This is a different method from PP71's face walk.
- **A SAT encoder of my own** (`sat57*.py`, using Glucose instead of CaDiCaL). With it I re-ran PP71's U₀ and V1 instances on my own census.

**Verdict scale:** correct / correct with repair / wrong. The audit's rescoping is applied throughout. For each result I state the hypotheses it actually uses.

---

## 0. Verdicts at a glance

| Item | Verdict | Exact scope (short) |
|---|---|---|
| PP69 𝒲, Lemmas 2.1–2.2 | correct (CHECKED independently) | additive field on one curve; each C_θ is the unique pointwise Bayes act at p(θ) |
| PP69 Thm 3.1 | correct | all measurable models; sections closed **along the arc** |
| PP69 Lemma 3.2, Thm 3.3, Cor 3.4 | correct | in 𝒲, with (H_σ); not axiom-level |
| PP69 Prop 3.5 | correct, but one remark is vacuous | swap-invariant H only; the remark on REFEREE_round56's P_w family applies to no splice |
| PP69 Prop 3.6 | correct | in 𝒲 |
| PP69 Thm 3.7 | **correct with repair** | (I8) fails at e₁ and e₂ with the uncapped radius at θ = 1; capping it repairs the proof |
| PP69 Prop 5.1 | correct (typo in (a)) | (a) needs the curve's world-3 descent |
| PP69 Prop 5.2 | correct | (TC), strict (G), a swap-invariant relation, and swap-invariant C and B |
| PP69 Prop 5.3 | correct with repair (PP70's margin) | **additive certificates only**; the "sheet" is a reading |
| PP70 Lemma 1.1, Thm 1.2 | correct | **this curve** (ranks monotone along the parameter); the memo's "any curve" overstates |
| PP70 Prop 1.3 | correct with rescoping | core lemma general (= forced pattern); the direction corollaries need a family ordered pointwise at world 3 |
| PP70 Prop 1.5 | correct with repair | in-family repairs on this curve; (a) and (d) only for sources on the F-segment (L₀ included) |
| PP70 Props 1.6–1.9 | correct | as stated, with the hypotheses listed in §2 |
| PP70 Prop 2.1 | correct (an error in PP69 found) | PP69's radius rule at θ = 1 |
| PP70 Props 2.2–2.7 | correct | relative to PP69's committed rows (choice-level); 2.6 is a sketch |
| PP70 §2.7, off-arc incoherence | NUMERICS → **PROVED at five weights** (exact certificates) | not proved for every off-arc weight |
| PP71 Lemma 2.1, Prop 2.2, Lemma 2.3 | correct | Prop 2.2: uniform same-class cycles under (DK) |
| PP71 Thm 2.4, Cor 2.5 | correct with rescoping | same-class steps (more precisely, a world differing from every step's class); Cor 2.5 also needs continuing silence |
| PP71 Props 2.6–2.7 | correct; readings rescoped | they exclude **preserving** a whole score order, not scores used as **witnesses** |
| PP71 SAT 4-cycle; 2-cycle UNSAT; 3-cycle SAT | correct (reproduced) | cell sub-universes; SAT is evidence only |
| PP71 splice "11-splice core" UNSAT | **correct with repair** | the UNSAT also needs ≥ 10 further splices present as rivals; the 11 alone are SAT |
| PP71 Lemmas 5.1–5.2 | correct | closed sections, continuous indices, uncountable parameter set |
| BRIEF58 forced pattern and consequence | correct | interior C; only B ⪯_i Y at i ≠ k is needed |
| BRIEF58 curve exclusion | correct; strict (G) alone suffices | any model pointwise weakly 3-worse than T |
| BRIEF58 toy vectors | correct (CHECKED) | sources only; also compatible with all guidance among the actual loop models |
| BRIEF58 loop guidance claims | correct (PROVED; CHECKED exactly at four scales) | each is a **strict** guidance comparison; the forced refusals are guidance-compatible |

No result was found wrong outright. Two items are wrong **as stated** and are repaired below: PP69 Theorem 3.7 at the endpoint, and the description of PP71's splice core. Several readings are narrower than the round-57 memo says.

---

## 1. PP69

### 1.1 The relation 𝒲 (Lemmas 2.1, 2.2; Def. 2.3) — correct

**Re-implementation (`curve57.py`).** I built the curve directly from the definitions. Minima over Minkowski combinations were computed as combinations of minima. M₀ = [(16,7,0)/23, (7,16,0)/23]. On each segment the change points of the advice were computed exactly. The field was coded straight from PP69's tables. Mirror problems in M₂ were obtained through σ.

**Results (`field57.out`).** All checks pass, with 0 failures on 2,500 problems and 1,141 switches:
- The patterns are exactly the 15 (class, pattern) types listed in Lemma 2.1(b).
- Each problem changes advice at most twice. Ranks are monotone in θ at every world, and non-decreasing at world 3, so the curve descends at world 3.
- Advice is swap-invariant.
- φ is strictly rank-monotone at every world.
- f₁ = f₂ on M₃, and f is swap-equivariant.
- **C_θ is the unique minimiser of p(θ)·φ(g, ·)** on a 1/48 grid, at θ = 0 and θ = 1, and at every threshold ± 10⁻⁶.
- Every switch lowers φ₁ + φ₂ and raises φ₃.

By hand I re-derived every closed form of U in §2.2. Two remarks:
- The bound "U_A ≤ −1 − θ/2" for "A constant" on M₁ is loose. The exact value is −2 + θ/2, which is ≤ −1 − θ/2 on [0, 1]. This is harmless.
- |f| ≤ 4|g| in fact holds; the stated 6|g| is also fine.

**Hypotheses.** 𝒲 needs only ∫|g| dμ < ∞. Equal values Φ₁ = Φ₂ on swap-invariant models need (H_σ).

### 1.2 Theorem 3.1 — correct

- (i) A total additive preorder with a strictly rank-monotone integrand gives reflexivity, strict (G), (IB) (verdicts depend on records only) and (TC) (transitivity).
- (ii)–(iv) follow from a.e. uniqueness of the pointwise argmin. For a fixed θ, the switching loci are null. At θ = 1 uniqueness still holds, because τ₂ < 1.
- (v) θ ↦ Φ_w(C_θ) is continuous (a.e. convergence and dominated convergence), so A_w(X) is closed **in [0, 1]**. That is all (v) claims.

### 1.3 Lemma 3.2, Theorem 3.3, Corollary 3.4 — correct

**Theorem 3.3** uses exactly the following:
- X is measurable, with Φ₁(X) = Φ₂(X) ≤ Φ₁(T) and X ∉ 𝔽;
- (H_σ);
- Bayes optimality at p(θ′), together with p₁ = p₂ and Lemma 3.2(c) (which excludes θ′ = 1).

PP70's one-line proof is the same argument. It is a theorem about 𝒲, not about the axioms.

**Corollary 3.4(a)–(c)** are correct. I re-checked:
- the record identity rec(C_s, Z) = rec(Y, C_θ′) in (b);
- the world-3 mixing argument in (c), which uses the tie at world 1;
- that every advice change on a mixed problem changes the rank at every world, which is what (c) needs at worlds 1 and 2.

**Corollary 3.4(d)** is honestly labelled. **A remark for PP70 §2.7(c)**, which asserts that Φ₁ decreases *strictly* on the strength of a 12-bin check. Twelve bins do not cover every sub-interval. Strictness on every (θ₁, θ₂) does follow from a short argument:
- each threshold is a continuous function on an open set where its pattern holds;
- so any problem whose threshold lies in (θ₁, θ₂) has a non-null neighbourhood with the same property;
- it is therefore enough that threshold values are dense in [0, 1].

The sampled ranges in `field57.out` support density:
- R-part: (0.002, 0.333);
- class-1/2 S→B: (0.338, 0.913);
- second thresholds: up to 0.997.

A full proof needs the elementary boundary limits (τ → 0, ⅓, 1 at the faces of the relevant cones). I label it a sketch, not PROVED. Only "earliest is redundant" and s\* = s depend on it.

### 1.4 Proposition 3.5 — correct, with one sentence to delete

- The equality Φ₁(Z) = Φ₂(Z) needs (H_σ), with H ∩ (M₁ ∪ M₂) swap-invariant.
- The range Φ₁(C_b) ≤ Φ₁(Z) ≤ Φ₁(C_a) holds because every complete forward change lowers φ₁ + φ₂ (CHECKED).

**PP70 Prop 2.3 is correct.** Put P₁ = R_B ∪ (L ∩ M₁), from REFEREE_round56's definition of P_w. Any H ⊇ P₁ that is swap-invariant on M₁ ∪ M₂ contains L. So PP69's remark that the referee's non-vacuous Prop 7.1 splices "are repaired here whenever H is swap-invariant" applies to no splice, and should be deleted. Those splices are class-2 (or class-1) fills of N.

### 1.5 Proposition 3.6 — correct. Theorem 3.7 — correct with repair

**Prop 3.6.** D\* = A a.e. on M₃, and D\* ⊴₃ Y with D\* ≠ Y. So 1 ∉ Dom(Y).

**Theorem 3.7(a) is wrong as stated (PP70 Prop 2.1 is right).** At θ = 1, PP69 drops the boundary term from r(1). Take X = V₁ and w = 1:
- A₁(V₁) = ∅, since V₁ is strictly 1-better than every model;
- so r(1) = ∞ and U₁(V₁) = Δ;
- then Rz_{e₁}(V₁) ⊇ {1} = supp e₁, and (I8) fails.

The same holds at e₂.

**Repair.** Cap r(1) at ½·dist(h₁₂, ∂Δ ∖ (e₁, e₂)), or at any smaller positive constant. The rest of the proof then holds. I checked the nearest-point estimate:
- if q ∈ B(p(θ₀), r(θ₀)) and θ\* is the arc point nearest q, then |p(θ\*) − p(θ₀)| ≤ 2|q − p(θ₀)| < dist(p(θ₀), p(A_w(X)));
- so θ\* refuses X at w;
- the arc meets the edge only at h₁₂, perpendicularly, so h₁₂ is the nearest arc point to every edge point near it.

**The price of the cap** is PP70 Prop 2.2 (the edge squeeze). That is a bequest, not an error.

### 1.6 Section 4 (imports) — correct, one reason inaccurate

PP70 §2.6 is right that 𝒲 satisfies (L0⁺) out of members. The correct reason Theorem Q does not bite is different from PP69's:
- Q(i)'s sequence needs **selected pure likelihood shifts** C_{a∘(1+t_k e_w)} of a member. The arc contains no posterior shifts.
- Q(ii)'s mechanism, a non-null non-conic swap with zero increments at all three worlds, is excluded by uniqueness, as PP69 says.

The other import checks are correct.

### 1.7 Propositions 5.1–5.3

**Prop 5.1 — correct, with a typo.** In (a), "C_s ⪯₃ C_θ for θ ≤ s is guidance" should read **θ ≥ s**: later members are pointwise 3-worse. The conclusion is right. A later C_θ satisfies C_θ ⊴₃ C_s ⊴₃ Y strictly, so strict (G) refuses C_θ ⪯₃ Y. Part (a) needs the curve's world-3 descent. Part (b) is the general forced pattern (§4.1).

**Prop 5.2 — correct.** Exact hypotheses:
- (TC), weak and strict (G);
- a relation invariant under σ (with μ σ-invariant, so that X ↦ X∘σ acts on models modulo null sets);
- C and B swap-invariant;
- C defended against B at a world of {1, 2, 3};
- F ⊆ Sil(C) ∩ M₁ non-null.

No additivity, registration or (IB) is used.

**Prop 5.3 — correct with repair; scope confirmed: additive certificates only.**
- (a) needs one additive, strictly monotone, integrable field that decides B_n ⪯_w Y_n at every world, with C_s its a.e.-unique λ_s-Bayes act. The proof needs PP70's margin e(g) > 0 a.e. (a.e.-uniqueness of the Bayes act is equivalent to pointwise uniqueness a.e.).
- (b) needs the **same** field to decide every comparison out of B_n, because defence against every bounded rival is then a supporting-hyperplane condition (Lyapunov). This is PP38 Thm 3.1(ii), an architecture fact; it is NOT SAFE in the sense of the ledger, entry 21.
- (c) needs the certificate and the B_n to be swap-invariant.

What is proved:
- B_n → C_s in measure;
- B_n is weakly λ_n-Bayes, with limit weights at which C_s is weakly Bayes;
- in 𝒲 itself, λ_n is off the arc, since on the arc uniqueness gives B_n = C_θ, which Prop 5.2 forbids.

**"Two-dimensional sheet" is a reading**, and is withdrawn as the audit says. Nothing in 5.3 is axiom-level.

---

## 2. PP70

### 2.1 Lemma 1.1 and Theorem 1.2 — correct, for this curve

Lemma 1.1(a)–(d) agree with my implementation. Lemma 1.1(e) (τ ≥ 9/16 on R_B, in F-units) is consistent with it: my sampled minimum of the second R_B threshold is θ = 0.8598, that is, t = 0.579.

**Theorem 1.2** uses exactly two facts:
- for a.e. g and every w, s ↦ rank_w C_s(g) is monotone (Lemma 1.1(b));
- C_{s_n} → C_s a.e.

Its conclusions follow: G⁺ is a closed interval, G⁻ ∪ {C_s = X} is an interval, and the two are disjoint. Consequence (ii) holds for any coherent C_s. DESIGN_MEMO §8.26's "**along any** non-isolated curve" overstates this. The theorem is for this curve, or any family with per-problem monotone ranks.

### 2.2 Proposition 1.3 (direction lemma) — correct with rescoping

The **core statement** is general:
- C is selected at an interior index;
- Y = C[E ↦ A_k] is a class-k fill;
- B satisfies B ⪯_i Y at both i ≠ k.

Then C ⋠_i B for i ≠ k, and C ⪯_k B. This is BRIEF58's forced pattern (§4.1). Corollary (a), distinct dominators for distinct classes, is general.

**Corollaries (b)–(c), "the class fixes the direction", hold only on families whose members are pointwise weakly ordered at world 3 along the parameter.** That is true on the round-57 curve.
- (c) is really about **any** model pointwise weakly 3-worse than T.
- (b) fails to transfer elsewhere. On the rescaling loop, consecutive members are 3-ordered on one edge only, and 3-mixed on the other two (`loop57.out`). So a class-1 repair there is neither "earlier" nor "later" in any 3-order.

This is exactly the audit's "the class does not determine the direction of the index". Corollary (d) is relative to PP67's (C3) choice.

### 2.3 Propositions 1.4 and 1.5 — correct; 1.5 needs its scope repaired

**Prop 1.4** is correct. Hypotheses: a selection on the curve with closed sections; an interior source C_s; a class-3 fill of it.

**Prop 1.5** needs repair.
- **(a)** is conditional on fills E ⊆ Sil(C_s) ∩ M₃ whose first-answer thresholds lie in (s, s + η). That hypothesis can be met only when s lies on the **F-segment** (s ∈ [2, 3) in PP70's index, L₀ included).
  - For R- and J-segment sources, every class-3 silent problem first gets an answer on the F-segment (index ≥ 2; ≥ 2 + 9/16 on R_B).
  - So nothing in Prop 1.4(b) or 1.5(a) forces their repairs to approach the source.
  - In 𝒲 they do approach it (Cor 3.4(d)), but that is 𝒲's choice.
  - PP70's sentence "the in-family repairs of the thin fills of every source accumulate at that source" should be restricted to F-segment sources. PP70 already restricts the J-segment, but forgets the R-segment.
- **(b)** and **(c)** concern in-family R_α-repairs only.
- **(d)** ("fixed balls are impossible") inherits (a)'s scope: in-family repairs of thin fills of F-segment sources (and in-family splice repairs at u, from (b)).

As the audit says, none of (a)–(d) is axiom-level: a repair from outside the family escapes them all.

### 2.4 Propositions 1.6–1.9 — correct

- **Prop 1.6.** I re-derived the record, and the strict-(G) form of the path obstruction.
- **Prop 1.7.** I re-derived the record rec(R_α, Z_H) and exclusions (i)–(iv) cell by cell.
  - (ii) needs N registered and protected, (C), and H ∖ L_α non-conic.
  - Hence the first inequality in (b) (α > ess inf σ|_E) needs (L ∖ E) ∖ L_α non-conic. It may fail for conic E.
- **Prop 1.8.** I re-derived the records in (a)–(d). The two-band identity rec(R_α, Z_H) = rec(R_{α′}, R_x) holds.
- **Prop 1.9.** Correct. It uses: strict (G); (TC); C_t ⋠₃ Y (because C_t = A on E); C_t's defence at 1 or 2; and G_w ∖ E a non-null *proper* part of the opposite band, so that r_w stays mixed. The kill is the cycle C_t ⪯_w Y ⪯_w Z_w ⪯_w C_t, with Y ⊵_w Z_w strictly.

### 2.5 Propositions 2.1–2.7 and §2.7: what is proved, and what is numerics

**Prop 2.1 — correct.** See §1.5. It is a genuine error in PP69.

**Prop 2.2 — correct, PROVED, relative to PP69's committed rows (choice-level).**
- (a) Kill-A: C_θ ⪯₁ D, C_θ ⪯₂ D and the class-3 fill Y ≺_{1,2} C_θ give D ⋠_{1,2} Y, for an edge D with supp {1, 2}. With Φ₁(C_θ) ↓ Φ₁(D\*), this gives min(Φ₁, Φ₂)(D) ≤ Φ₁(D\*).
- The swap-invariant case uses Lemma 3.2(c).
- (d): I re-derived the sign computation. Equal-mass class-1 and class-2 S→B pieces lower both Φ₁ and Φ₂ by δ per unit.

**Prop 2.3** — correct (§1.4).

**Prop 2.4** — correct as a reading.

**Prop 2.5 — correct.** PP68 Thm 1.1(iii) transfers to C_s's fills: its proof uses only guidance between nested fills, (TC) and domination. Interior points of Dom(Y_E) persist for nearby nested E″ ⊊ E ⊊ E′, because Φ is continuous in measure.

**Prop 2.6** — correct as a sketch; the o(1) bookkeeping is not written out. It concerns PP69's ½-radius rule only.

**Prop 2.7** — correct, PROVED for PP69's field. My per-switch check confirms that the drop in Φ₁ (= Φ₂) is at most half the rise in Φ₃, on all 1,141 switches. Whether an axiom-level version exists stays OPEN, as PP70 says.

**§2.7(a), incoherent off-arc Bayes acts: upgraded from NUMERICS to PROVED at five weights (`offarc57.out`).**

*The certificate.* Let X_λ be the pointwise argmin of λ·φ. I search for two problems g₁ and g₂, and a third problem g′ = c₁h₁ + c₂h₂, such that:
- X_λ answers h₁ = ±g₁ and h₂ = ±g₂;
- X_λ is silent at g′, with c₁, c₂ > 0;
- each of the three points is generic: no coordinate and no vertex dot product (v_i, w_j, h₁₂) is zero, and the argmin is strict.

*Why it proves incoherence.* At a generic point the pattern is locally constant and the thresholds are continuous, so X_λ is locally constant near all three points. Suppose X_λ = D_K a.e. Then:
- D_K answers h on open dense subsets of neighbourhoods U₁ and U₂;
- since min_K is superadditive, D_K answers on an open dense subset of c₁U₁ + c₂U₂, which is a neighbourhood of g′;
- but X_λ is silent there. Contradiction.

So X_λ is incoherent modulo null sets. It is undominated in 𝒲, because it is the unique λ-Bayes act, so **global (C) fails in 𝒲 (PROVED)** at these weights:
- the four weights PP70 tested: (2/5, 3/10, 3/10), (9/20, 7/20, 1/5), (3/5, 1/5, 1/5) and (1/2, 1/10, 2/5);
- the near-arc weight p(3/20) + (1/50)(1, −1, 0).

*Controls and limits.*
- None of the three on-arc weights (θ = 0, ½, 17/20) yields a certificate, as it must not.
- At p(½) + (1/50)(1, −1, 0) none was found, matching PP70's report.
- Incoherence at every off-arc weight, or near the arc in general, remains NUMERICS/CONJECTURE.

PP70's inference — every extension to D = Δ must deviate from 𝒲 on records that no arc member carries — is correct. It now rests on these certificates, as well as on Theorem gm.

**§2.7(b)–(c).** Correct, with the strictness caveat of §1.3. The CONJECTURE (no coherent repair of thin other-class fills **in 𝒲**) remains a conjecture.

---

## 3. PP71

### 3.1 Structure results

**Lemma 2.1 — correct.** Hypotheses:
- C_i is registered (protected), with (C) for its tie partners;
- C_j dominates the fills C_i[E ↦ A] for **bounded** non-null E ⊆ {C_j = A} ∩ Sil(C_i) ∩ M₃;
- the Lebesgue measure class, for Lemma H.

**Prop 2.2 — correct under (DK)**, for **uniform same-class** cycles, in which every bounded class-3 fill of each member is dominated by the next. I checked:
- step 1 (density of strict silence);
- step 2 (the open convex A-region cannot meet Sil(C_i));
- step 3 (with g_t = (1, 1, −t)).

**It does not apply to mixed-class loops.** In the rescaling loop, C_{m₁} is a down-shift of T at world 3, so its class-3 A-region strictly contains T's. That is allowed there, because the edge C_{m₀} → C_{m₁} is the only class-3 edge.

**Lemma 2.3 — correct.** The dichotomy holds separately for each diagonal.

### 3.2 Theorem 2.4 and Corollary 2.5 — correct with rescoping

**Theorem 2.4** uses only weak and strict (G) and (TC), for a cycle in which each C_{i+1} satisfies C_{i+1} ⪯_w Y_i for a class-k_i fill Y_i of C_i. Its exact content is this:

> **For every world w that differs from every step's class k_i, ⪯_w is not transitive on {C_i, Y_i}.**

For PP71's same-class cycles (every k_i = 3) this means worlds 1 and 2. For the mixed cycle 3 → 1 → 2, no world qualifies, and the theorem says nothing.

Indeed I checked that transitive orders realise the mixed cycle even with one fill per step. Put each Y_i just below its source at the two worlds other than k_i, and just above its dominator at world k_i. At world 3 this gives C₀ ⪯ Y₂ ≺ C₂ ⪯ Y₁ ≺ C₁ ⪯ Y₀, consistent with all required verdicts. This is an abstract-level remark only: it ignores the pointwise guidance between different steps' fills.

**Corollary 2.5.**
- (a) needs: 𝒮 finite; every member has non-null class-3 silence; every class-3 fill of every member is dominated by a member. (Then every vertex has an out-edge, so there is a same-class cycle.)
- (b) needs transitivity at worlds 1 and 2, **and continuing silence**: every model reached along the chain has non-null class-3 silence, otherwise the chain may stop.
- The closing claim ("no additive certificate supports a fill-closed system with uniform generations") also needs PP67 Prop 7.4's hypothesis: every generation is silent on one fixed E₀.

Both rescopings are as the audit states.

### 3.3 Propositions 2.6–2.7 — correct; readings rescoped

**Prop 2.6** assumes that ⪯_w **contains the entire order** {X ⪯ Y : Φ(X) ≤ Φ(Y)}, for all pairs including rival–rival pairs. Its proof uses Φ-order links Y ⪯ Z and Z ⪯ X between arbitrary models. So it excludes **preserving a whole score order** and then patching it. It does **not** exclude:
- using a score as a **witness** for particular comparisons, for example defence rows out of registered models only;
- member-specific scores.

**Prop 2.7** assumes that ⪯_w **is**, for all pairs, the sign of an integral of a pointwise skew comparison of world-w ranks. The proof (three-part rank rotation) is correct.

**The reading** "Bayes-act defences are unavailable in a recurrent system" is proved only in this form: one common score per world, supplying every favourable comparison out of every member of a **same-class** cycle. The edge-lemma refusals then force the score to fall strictly all the way round.

For mixed-class cycles even that form fails. One score per world supplies every source-to-defender verdict of 3 → 1 → 2 (the toy vectors, §4.3).

### 3.4 The cell SAT results — reproduced; the core needs a repaired description

**Census.** My complete LP sign-vector census of the arrangement for (C₁, …, C₄, T) gives:
- 43 open chambers;
- **exactly PP71's 23 V1 cells** (C₁ … C₄, T);
- **exactly its 25 U₀ cells** (C₁ … C₄, with bounded pieces);
- 46 fills per model.

My encoder has the same clause types as PP71's, but its own code:
- weak and strict (G);
- one variable per (record, world) for (IB);
- lazy (TC), with a final check on all ordered triples;
- defence of selected models against every model;
- rule III;
- (C) clauses *added* for every non-selected model in SAT runs (strongest SAT), and *dropped* in UNSAT runs (strongest UNSAT).

**Results (`sat57c.out`, `sat57.out`).**
- U₀ 4-cycle: SAT, with (C) on. The forced verdicts are exactly R, R, A on each edge.
- U₀ 2-cycle: UNSAT, with (C) off.
- U₀ 3-cycle: SAT.
- V1 4-cycle with T present: SAT.
- V1 2-cycle: UNSAT. V1 3-cycle: SAT.

All agree with PP71. SAT remains evidence only.

**Splice core (`sat57.out`, `sat57b.out`).**
- With the universe = the five models, all their fills, and **only the 11 core splices**, the problem "4-cycle + each core splice dominated by one of T, C₁, …, C₄" is **SAT**.
- I regenerated PP71's 138 sampled splices with its own procedure (random.Random(71), identical cell order); all 11 core splices are among them.
- With all 138 present as rivals, the core requirements are **UNSAT**, and SAT without the cycle. This reproduces PP71.
- Greedy minimisation of the **rivals** (keeping the 11 requirements) leaves 10 further splices that must be present. Their defence obligations, (IB) records and triangles are what close the contradiction. The 21-splice universe is UNSAT with the cycle and SAT without it.

**Repair of the statement.** "An 11-splice core is UNSAT" should read: *11 domination requirements, in a universe that also contains at least 10 further splices as rivals, is UNSAT (no coherence labelling; rule III only; whole-region conic cells; weak domination).* It remains a full-domain fact, since defence against every measurable rival is an axiom. Its content is: these four models plus T cannot both close the cycle and dominate those 11 splices. It concerns this example only.

### 3.5 Lemmas 5.1–5.2 — correct

**Lemma 5.1.** Hypotheses:
- a selection with closed fixed-rival sections in index space;
- interior indices p_i(s), continuous in s;
- at each s, C_{i+1}(s) dominates some class-3 fill of C_i(s), which gives the edge-lemma refusals.

The pinning conclusion C_i(s′) ⪯₃ C_{i+1}(s) also needs C_i(s′) to defend at a world of full support.

**Lemma 5.2** needs S uncountable. Its proof is right: some S_n = {r ≥ 1/n} is uncountable, so it has two points within 1/n of each other.

I did not re-run the two-cycle census-stability check. It stays CHECKED at six pairs and CONJECTURE elsewhere, as PP71 labels it.

---

## 4. BRIEF58's structural facts

### 4.1 The forced pattern and its consequence — correct

**Exact hypotheses.**
- C is selected at an index whose support contains all three worlds.
- E ⊆ Sil(C) ∩ M_k is non-null, and Y = C[E ↦ A_k] (A_k is correct at both i ≠ k).
- B is any measurable model with B ⪯_i Y at both i ≠ k. Full domination is not needed.

**Proof.**
- Weak (G) gives Y ⪯_i C. Strict (G) gives C ⋠_i Y.
- If C ⪯_i B, then C ⪯_i B ⪯_i Y ⪯_i C is an accepted triangle with a refused reverse, against (TC). So C ⋠_i B for i ≠ k.
- C's defence against B then gives C ⪯_k B.

**Consequence.** If B served fills of classes k ≠ k′ of the same C, then C would refuse B at {i ≠ k} ∪ {i ≠ k′} = {1, 2, 3}, and C would be undefended. So the class-1, class-2 and class-3 repairers of a source that is silent in all three classes are pairwise distinct. (One B may still serve many fills of one class.)

At an edge source (supp {i, j}, with k ∉ supp), the same refusals leave C undefended. That is PP70's Kill-A.

### 4.2 No round-57 curve member dominates T's class-1/2 fills — correct, and (TC) is not needed

Every curve member satisfies C_θ ⊴₃ T pointwise: Lemma 2.1(c), CHECKED in `field57.out`. Let Y = T[E ↦ A_k] with E ⊆ Sil(T) ∩ M_k, k ∈ {1, 2}.
- On E, Y is 3-correct, while every member is silent or 3-wrong there.
- Off E, Y = T ⊵₃ C_θ.

So Y ⊵₃ C_θ strictly, and **strict (G) alone** refuses C_θ ⪯₃ Y.

The statement holds verbatim for **every** model pointwise weakly 3-worse than T. It also covers every fill of T on Sil(T) whose new answer is 3-correct, including class-3 minority (B) fills. Breaking the 1 ↔ 2 symmetry cannot help, as the audit says.

### 4.3 The mixed-class toy — correct (CHECKED, `loop57.out`)

With loss vectors (0, 0, 0), (−1, −1, 2) and (1, −2, 1) and X ⪯_w Y ⟺ ℓ_w(X) ≤ ℓ_w(Y), every required verdict holds:
- for 3 → 1 → 2: the refusals at the two non-designated worlds and the acceptance at the designated one;
- the three world orders are C₁ < C₀ < C₂, C₂ < C₁ < C₀ and C₀ < C₂ < C₁.

**Added check.** These orders are compatible with **all pointwise guidance among the three actual loop models**. The only guidance relations among them are the three strict designated-world ones of §4.4, and the toy orders respect them. So the source-level consistency survives the real geometry.

It is still consistency among sources only, as BRIEF58 says. Fixed score gaps cannot handle arbitrarily small fills.

### 4.4 The rescaling loop's guidance claims — correct

**Geometry.** Put s = a⁻³ ∈ (0, 1). Then:
- m₁ ∝ (1, 1, s);
- m₂ ∝ (s, 1, s) ∝ (1, a³, 1);
- m₂/m₁ ∝ (s, 1, 1);
- m₀/m₂ ∝ (1, s, 1).

So each move is a **pure single-world down-shift**: at world 3, then world 1, then world 2. In particular m₂ is itself the pure world-2 up-shift u∘(1 + (a³ − 1)e₂).

**Proof (PP57 Lemma 4.1, re-proved).** For interior a, b = a∘(1 + t e_w) and any compact M in the open simplex:
- for every vertex, Σ b_i p_i h_i = Σ a_i p_i h_i + t a_w p_w h_w;
- so C_b gains only w-correct acceptances and loses only w-wrong ones;
- hence C_b ⊵_w C_a pointwise, strictly on a non-null cone.

Applied to the three moves this gives C_{m₀} ⊵₃ C_{m₁}, C_{m₁} ⊵₁ C_{m₂} and C_{m₂} ⊵₂ C_{m₀}. Weak (G) then gives the three claimed acceptances.

**CHECKED (exact, complete census; 58 chambers at each scale s ∈ {1/2, 4/5, 19/20, 99/100}).**
- Each of the three is a **strict** pointwise improvement at its designated world.
- At the two other worlds, every consecutive pair is **pointwise mixed**.
- Lemma 4.1 also passed at 36 random (a, t, w): 1,224 chamber comparisons, 0 violations.

**Consequences for the constructor (PROVED; not in BRIEF58).**
1. **The reverses are forced refusals by strict (G):** C_{m₁} ⋠₃ C_{m₀}, C_{m₂} ⋠₁ C_{m₁}, C_{m₀} ⋠₂ C_{m₂}. Together with the forced pattern, each pair's defences are pinned. For example, C_{m₁} must defend against C_{m₀} at world 1 or world 2.
2. **The forced-pattern refusals are not excluded by guidance**, because the other-world statuses are mixed. At chamber level (`loop57b.out`), each edge's source has 9 silent chambers of the edge's class. Single-chamber fills on 7 of them pass the pointwise prerequisites (neither the agreement obstruction nor strict (G) excludes them). The other 2 lie inside the defender's A-region, where the agreement obstruction applies (for bounded parts). The whole-silence fill passes on all three edges. This is not a domination proof.
3. **A warning on Theorem Q.** For a non-isolated family of scales a ↓ 1, the indices m₂(a) are exactly Theorem Q(i)'s pure-shift sequence u∘(1 + t_k e₂), and m₁(a) is the pure world-3 down-shift ray. So if the relation contains (L0⁺)-type strict acceptances out of these members at world 2, Q(i) applies at u with closed sections. Any balanced non-conic member swap then triggers Q(ii). The constructor must avoid (L0⁺) on these rays, or show that no such swap exists.

**Not established, as BRIEF58 says:**
- the other-world refusals as commitments;
- the domination records;
- their coexistence;
- defence against every rival.

---

## 5. Exact statements to carry into round 58

1. **Forced pattern** (§4.1): interior C; B ⪯_i Y at i ≠ k ⇒ C ⋠_i B (i ≠ k) and C ⪯_k B. Axiom-level.
2. **Direction:** only on families ordered pointwise at world 3. Not on the loop.
3. **Accumulation (PP70 Prop 1.5):** in-family repairs on the round-57 curve, F-segment sources. Not axiom-level.
4. **Recurrence (PP71 Thm 2.4):** non-transitivity only at worlds differing from every step's class. Empty for 3 → 1 → 2.
5. **No patching (PP71 Prop 2.6):** applies to relations containing a whole fine score order. Scores as witnesses are not excluded.
6. **Additive repairs (PP69 Prop 5.3):** additive certificates; convergence in measure plus weakly-Bayes repairers. No sheet.
7. **𝒲 is a module relation only:** global (C) fails in 𝒲 (PROVED at five weights). PP69 Theorem 3.7 needs the cap at θ = 1.
8. **PP71's splice obstruction** needs its rival set.

---

## 6. Scripts (`r9/REFEREE57_py/`; run `python3 -I -B <script>` inside the folder)

| Script → output | Content | Label |
|---|---|---|
| `rlib.py` | exact D_K advice, classes, ranks; complete chamber census by LP over all sign vectors, with exact verification; posterior images | — |
| `loop57.py` → `loop57.out` | rescaling loop at s = 1/2, 4/5, 19/20, 99/100: pointwise status per pair and world; forced-pattern compatibility; Lemma 4.1 at random shifts; toy vectors | CHECKED |
| `loop57b.py` → `loop57b.out` | loop edges: chamber-level fill prerequisites (agreement, strict (G)) | CHECKED |
| `curve57.py` | own implementation of the round-57 curve and of PP69's field | — |
| `field57.py` → `field57.out` | Lemma 2.1 patterns, ≤ 2 changes, monotone ranks, 3-descent, swap; φ rank-monotone, f₁ = f₂ on M₃, equivariance; unique argmin on grid and at thresholds; switch signs; PP70 Prop 2.7 ratio; threshold ranges | CHECKED (ranges: NUMERICS) |
| `offarc57.py` → `offarc57.out` | exact incoherence certificates for X_λ at five off-arc weights; on-arc controls | CHECKED (→ PROVED via §2.5) |
| `sat57.py` → `sat57.out` | V1 census (identical 23 cells); 4-cycle with T SAT; 2-cycle UNSAT; 3-cycle SAT; core with only its 11 splices SAT | CHECKED |
| `sat57b.py` → `sat57b.out` | PP71's 138 splices regenerated; core UNSAT with them as rivals, SAT without the cycle; 10 further rivals needed; 21-splice universe UNSAT / SAT without the cycle (about 3 min) | CHECKED |
| `sat57c.py` → `sat57c.out` | U₀ (25 cells, 46 fills each): 4-cycle SAT with (C) on and edge pattern forced; 2-cycle UNSAT; 3-cycle SAT | CHECKED |
