# LL3 (round 40, BRIEF32). Quorum rankings: verified foundations, the exact cycle/tie/TC conditions, and the escape question — quorum worlds CAN escape every single endorsing field out of coherent selected models, exactly when the judges are spread beyond a sharp threshold

18 Oct 2026. Rules of BRIEF13 and BRIEF32. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports keep their recorded status.
- **CHECKED**: exact rational computation with a stated script, or a step-by-step reading of a recorded result.
- **CONJECTURE**.
- **NUMERICS**: none used.

Scripts are in `ll3py/`; run `python3 -I <script>.py` from that folder. Outputs: `foundations.out`, `geometry.out`,
`certificate.out`. All verdicts use `fractions.Fraction`. Each script ends with `ALL CHECKS PASSED` / `ALL VERIFIED`.

No assumption is added. Every extra hypothesis below belongs to a stated result and is named there.

---

## 0. Outcome

**Part A (foundations).** All seven audit lemmas are correct (§2.1, PROVED). The audit's five-model certificate is correct
(§2.4, CHECKED). It also contains two strict **4-cycles** that the audit did not report, besides its 5-cycle.

The clean general statement uses the **Nakamura number** ν of the voting game: the least number of winning coalitions with
empty common intersection (ν = ∞ if some judge belongs to every winning coalition). For every winning family, every
margin η ∈ (0,1) (it may depend on the judge and on the world) and arbitrary strictly guiding integrable judges
(Theorem A, PROVED):
- no nontrivial ties can occur ⟺ the game is proper (no two disjoint winning coalitions) ⟺ ν ≥ 3;
- (TC) holds ⟺ ν ≥ 4;
- a strict k-cycle (of distinct models) can occur ⟺ the game is proper and k ≥ ν;
- ν = ∞ (a veto judge) ⟺ no cycles at all; then the veto judge's own loss endorses every accepted comparison.

For q-of-n quotas, ν = ⌈n/(n−q)⌉. So:
- no nontrivial ties ⟺ 2q > n;
- (TC) ⟺ 3q > 2n;
- strict k-cycles ⟺ k ≥ ⌈n/(n−q)⌉.

For n = 4, q = 3 this means strict 4-cycles and longer cycles occur, but 3-cycles never do. For weighted games, 2τ > W and
3τ > 2W are sufficient but not necessary. The exact condition is Nakamura's, and a proper game can still have ν = 3, as
weights (3,2,2,1,1) with threshold 6 show.

One consequence matters for the barriers (Prop A8, PROVED). In a quorum cover, T1 is automatically **selected**: it is
tied with a selected model, and nontrivial ties do not exist. So FF2 Thm 4.1 applies **verbatim** to every quorum cover
whose selection is continuous in measure. The "T1 merely tied" gaps of GG3 §8.2 and HH1 §2.3, §2.7 do not arise.

**Part B (escape). Answer: YES. A quorum world can escape every single endorsing field on comparisons out of coherent
selected models.** It can do so exactly when its judges are spread beyond a sharp threshold.

1. **Two coherent bases are needed, and two suffice (Lemma B0, PROVED).** Consider a finite family of accepted comparisons
   whose records have a pointwise worsening-free, non-null positive combination (a de Finetti/Motzkin certificate). Its
   base models must include two that **cross** at the world: each is better than the other on a non-null set. One base,
   or bases ordered pointwise at that world, never suffice. This is why the audit needed arbitrary intermediate models.
   Any two distinct plain-posterior models near u cross at every world (CHECKED, §3.5).
2. **Obstruction (Theorem B1, PROVED).** Write r := (1−η)/(1+η). Suppose there are nonzero vectors y^S ≥ 0, one supported
   on each minimal winning S, such that for a.e. problem and every adjacent pair of advice ranks, the vector x of the
   judges' increments satisfies
   max_S Σ_v r_v y^S_v x_v ≤ min_S y^S·x.  (E)

   Then the field ℓ*(h, rank s) := Σ_{t<s} min_S y^S·x^t(h) is integrable and strictly guiding, and it endorses **every**
   accepted comparison. So the world adds up, and it satisfies FF2's (H3).

   For q-of-n quotas with common η, take y^S = 1_S. Then (E) reads r·(sum of the q largest increments) ≤ (sum of the q
   smallest). It holds whenever the judges' increments differ by a factor of at most
   **M\* = 1 + 2qη/((n−q)(1−η))**.

   For n = 4, q = 3, η = 1/16 (the audit's case) this gives M\* = 7/5. For η = 1/2 it gives M\* = 7.
3. **Sharpness and the certificate (Theorems B2, B3, PROVED; CHECKED).**
   - For every M > M\* there is a quorum world whose judges differ by a factor of at most M, and whose accepted
     comparisons out of **two coherent plain-posterior models A, B near T1** carry an explicit finite certificate. Every
     record is changed only inside two small boxes near ∂D_{T1}, inside a bounded log-ratio region.
   - The certificate defeats every strictly guiding penalty, integrable or not: the summed loss change is strictly
     negative. It also defeats every positive error weight, so it is an (M1) obstruction.
   - More generally (Theorem B3), for any game, any margins and any polyhedral cone K of allowed increment vectors:
     (E) on the generators of K ⟺ every world with increments in K has a common endorser ⟺ the comparisons out of two
     crossing coherent models never carry a certificate.
4. **The explicit instance (CHECKED, `certificate.out`, `geometry.out`).** World 1, n = 4, q = 3, η = 1/16, judges'
   increments in ratio ≤ 2, ε = 3/10.
   - A = C_{(17/50, 33/100, 33/100)} and B = C_{(33/100, 17/50, 33/100)}.
   - **Eight accepted comparisons**, four out of A and four out of B, each with exactly one dissenting judge.
   - Their records sum to a pure improvement: silence → good on eight pieces.
   - The same is CHECKED at all three worlds, for ε ∈ {1/20, 3/10, 1/2} and for indices within 10⁻⁶ of u.
   - The same world contains a **strict 4-cycle** (CHECKED). That is the normative cost.
5. **Consequence for the programme (Cor B4, PROVED modulo FF2's import chain).**
   - FF2 Thm 4.1 and Q4.2 (with HH1's repair) **do not exclude quorum covers**.
   - They impose one necessary condition: some world must violate (E) for every choice of y. For quotas, some world has a
     non-null set of problems on which r·top_q > bot_q for some adjacent increment, so the judges there differ by more
     than M\*.
   - The escape is cheap. It can sit on arbitrarily small cells next to ∂D_{T1}, out of any two crossing selected models.
     So these barriers say nothing further about quorum covers.
   - The decisive question is the competitiveness problem (the 216-branch system of BRIEF32). LL3 does not address it.

---

## 1. Setting and the vote condition

At world i, judge v has a strictly guiding loss ℓ_v(h, a) with integrable envelope. "Strictly guiding" means strictly
increasing in world-i rank: good (0) < silence (1) < bad (2) < contradiction (3). Write a_t(h) for the advice of rank t
at h, and x^t_v(h) := ℓ_v(h, a_{t+1}) − ℓ_v(h, a_t) > 0 (t = 0, 1, 2) for the adjacent increments.

For a record C → X put
- Q := {h : rank X(h) > rank C(h)} (worsening) and P := {rank X(h) < rank C(h)} (improvement);
- Δ_v(h) := |ℓ_v(h, a_X(h)) − ℓ_v(h, a_C(h))| = sum of the x^t_v between the two ranks;
- I_v := ∫_P Δ_v dμ and W_v := ∫_Q Δ_v dμ.

**Observation 1 of BRIEF32 (PROVED).** P and Q are the same for every judge, by guidance. Then L_v(X) − L_v(C) = W_v − I_v
and d_v(C, X) = W_v + I_v. So

  v supports C R X ⟺ W_v − I_v ≥ η(W_v + I_v) ⟺ I_v ≤ r W_v, with r := (1−η)/(1+η) ∈ (0,1).

With judge-dependent margins η_v, write r_v. A world is given by a monotone family 𝒲 of winning coalitions (q-of-n:
|S| ≥ q; weighted: Σ_S w_v ≥ τ). It accepts X R Y iff the supporters form a winning coalition.

---

## 2. Part A: foundations

### 2.1 The audit's lemmas (all PROVED; the class of BRIEF32 with any 𝒲 where stated)

- **A1 (IB, null invariance).** I_v and W_v depend only on the record. ✓
- **A2 (per-judge transitivity, new).** If v supports X R Y and Y R Z, then v supports X R Z.
  - L_v(Z) − L_v(X) = (L_v(Z) − L_v(Y)) + (L_v(Y) − L_v(X)) ≥ η(d_v(Y,Z) + d_v(X,Y)) ≥ η d_v(X,Z).
  - The last step is the triangle inequality for the L¹ distance d_v(X,Y) = ‖ℓ_v(·, a_X) − ℓ_v(·, a_Y)‖₁.
  - If X ≠ Y (mod null), support of X R Y forces L_v(X) < L_v(Y), because d_v(X,Y) > 0 by strict guidance.
  - So each judge's support relation is a partial order modulo null sets. The world aggregates n partial orders by a
    simple game.
- **A3 (strict (G)).** Let X be at least as good as Y a.e. at world i. Then P = ∅ for the record Y → X, so W_v = 0 for
  the record X → Y. Every judge has L_v(Y) − L_v(X) = d_v ≥ ηd_v, so X R Y.
  - If X is strictly better on a non-null set, then d_v > 0. Then L_v(X) − L_v(Y) = −d_v < ηd_v, so no judge supports
    Y R X.
  - Weak (G) with equal ranks a.e. means X = Y a.e., because distinct advices have distinct ranks. ✓
- **A4 (no nontrivial ties ⟸ 𝒲 proper; for quotas 2q > n).** For X ≠ Y no judge supports both directions, since that
  needs L_v(Y) − L_v(X) ≥ ηd_v > 0 and the reverse. So the two supporting coalitions are disjoint, and a proper game has
  no two disjoint winning coalitions. ✓
- **A5 (TC ⟸ ν ≥ 4; for quotas 3q > 2n).** Theorem A(b) below gives the general case. For the audit's case: a
  non-identity cycle X R Y R Z R X needs three winning coalitions, and by A2's strictness no judge is in all three.
  - Three q-sets with empty intersection need 3q ≤ 2n. So for 3q > 2n there is not even a cycle of acceptances.
  - Repeated models: X = Y gives X R Z and Z ≺ X, a contradiction. Y = Z gives X R Y and Y ≺ X, a contradiction.
    X = Z needs X ≺ X, which is impossible. ✓
- **A6 (closed sections, for every model X and any selection continuous in measure).**
  - |L_v(C_p) − L_v(C_{p′})| and |d_v(C_p, X) − d_v(C_{p′}, X)| are both ≤ 2∫_{diff(C_p, C_{p′})} env_v dμ. This tends to
    0 as μ(C_p Δ C_{p′}) → 0, by absolute continuity of the integral.
  - So F_v(p) := L_v(X) − L_v(C_p) − ηd_v(C_p, X) is continuous. The section is ∪_{S∈𝒲} ∩_{v∈S} {F_v ≥ 0}, a finite
    union of finite intersections of closed sets.
  - Where C_p = X, F_v(p) = 0 and the identity has all votes. This is the same continuous function, so nothing special
    happens there.
  - Non-injectivity of p ↦ C_p plays no role, since sections are preimages. ✓
- **A7 (direct (C); coherent competitive selections are undominated; proper 𝒲).**
  - X ≈ C at every world implies X = C (A4), so direct (C) holds.
  - Suppose Y dominates C_p. Then Y ≠ C_p, so by A4, Y R_i C_p and not C_p R_i Y at **every** world. This contradicts
    competitiveness of C_p on supp p. So C_p ∈ C_L, and (LA) holds. ✓

So, as the audit says, a cover of T1 on the full domain needs only a coherent selection, continuous in measure, through
T1, that is competitive. (LF) is trivial on the full domain.

**Prop A8 (T1 is automatically selected; PROVED).** Let every world have a proper game, and let a cover have (LA) and
(S). Then T1 = C_{q₀} for some q₀.
- *Proof.* T1 ∈ C_L is undominated. HH1 Prop 1(b) (arbitrary relations) gives T1 ≈ C_{q₀}, and A4 gives T1 = C_{q₀}
  mod null. ∎
- So FF2 Thm 4.1, with its hypothesis "T1 = C_{q₀}", applies verbatim to every quorum cover whose selection is continuous
  in measure. Its recorded status is CORRECT modulo D1, BB2 Thm 6.1 and M3.7–8, each refereed once (GG3 §8.1). The same
  holds for every barrier that HH1 lists as surviving "when T1 is selected" (Q3.25, CC2 Cor 5.7 under (TC)).

### 2.2 Theorem A (exact cycle, tie and TC conditions; PROVED; realisations CHECKED)

Let 𝒲 be any monotone family of winning coalitions with ∅ ∉ 𝒲. Let the margins η_v ∈ (0,1) be arbitrary, and let ν be
the Nakamura number of 𝒲. "For some fields" means for some strictly guiding integrable judges at this world.

- **(a)** Nontrivial ties occur for some fields ⟺ 𝒲 is not proper ⟺ ν = 2.
- **(b)** (TC) holds for all fields ⟺ ν ≥ 4.
- **(c)** For k ≥ 2, a cycle of acceptances A_0 R A_1 R … R A_{k−1} R A_0 with consecutive models distinct occurs for some
  fields ⟺ k ≥ ν. If 𝒲 is proper, the cycle can be taken strict (no reverse edge accepted) ⟺ k ≥ ν.
- **(d)** ν = ∞ (a veto judge v₀ in every winning coalition) ⟺ no acceptance cycle ever occurs. Then L_{v₀} endorses every
  accepted comparison: the world adds up and satisfies FF2's (H3), so such quorum worlds cannot escape.
- **(e)** For q-of-n quotas, ν = ⌈n/(n−q)⌉ if q < n, and ν = ∞ if q = n. Hence:
  - proper ⟺ 2q > n;
  - (TC) ⟺ 3q > 2n;
  - strict k-cycles ⟺ k ≥ ⌈n/(n−q)⌉.

  Sufficient weighted conditions: ν ≥ k + 1 if kτ > (k−1)W, where W = Σw_v. In particular properness if 2τ > W, and
  (TC) if 3τ > 2W.

*Proof.*
- **Necessity in (c).** The supporters S_0, …, S_{k−1} of the k edges are winning. A judge in all of them would have
  strictly increasing loss around the cycle (A2). So ∩S_j = ∅, and k ≥ ν.
- **Sufficiency in (c).** Take winning S_0, …, S_{k−1} with empty intersection: a Nakamura family, padded by repetition if
  k > ν. For each judge v pick j(v) with v ∉ S_{j(v)}.
  - Use k disjoint non-null cells F_0, …, F_{k−1}. Model A_m gives silence on F_m (where good advice is available) and
    good advice elsewhere.
  - Judge v has local loss equal to rank × density. Its F-masses are m_v(F_m) := r^{−((m − j(v) − 1) mod k)}.
  - Then judge v supports exactly the edges m ≠ j(v), with equality in the margin, and the reverse of edge j(v) only. So
    edge m has supporters ⊇ S_m (winning).
  - Its reverse has supporters G_m := {v : j(v) = m} ⊆ S_m^c. G_m is losing when 𝒲 is proper, since the complement of a
    winning coalition is then losing. So every edge is strict.
- **(a).** "⇐" by A4. "⇒": take S with S and S^c both winning. Two cells, with judges in S seeing cell a as cheap and
  judges in S^c seeing cell b as cheap (masses 1 and 1/r). Then X R Y and Y R X.
- **(b).** If ν ≥ 4, a forbidden triangle is a 3-cycle of acceptances, which (c) excludes. Repeated models are handled
  as in A5.
  - If ν ≤ 3, take three winning S_1, S_2, S_3 with empty intersection (repeat one if ν = 2). If S_1 ∩ S_2 is winning,
    then the three pairwise intersections are disjoint. Under properness two of them cannot both be winning, so after
    relabelling S_1 ∩ S_2 is losing. If 𝒲 is not proper, take S_3 = S_1, so S_1 ∩ S_2 = ∅.
  - Give the judges in S_1 ∩ S_2 the order X < Y < Z, those in S_2 ∩ S_3 the order Y < Z < X, those in S_3 ∩ S_1 the
    order Z < X < Y. Judges in only one S_j get one margin-steep pair and equal masses otherwise. Judges in no S_j get
    equal masses.
  - Then X R Y, Y R Z and Z R X, and the supporters of X R Z are exactly S_1 ∩ S_2, which is losing. So Z ≺ X, and (TC)
    fails.
- **(d).** "⇒": the veto judge supports every accepted non-identity edge and strictly increases along it. "⇐": if ν < ∞,
  then (c) with k = ν gives a cycle when 𝒲 is proper, and (a) gives a 2-cycle (a tie) when it is not.
- **(e).** A family of k q-sets has empty intersection iff the complements, each of size n − q, cover [n]. That is
  possible iff k(n−q) ≥ n. For weights, k winning coalitions with empty intersection give Σ_j w(S_j) ≤ (k−1)W, so
  kτ ≤ (k−1)W. ∎

**CHECKED (`foundations.out`).**
- ν = ⌈n/(n−q)⌉, properness ⟺ 2q > n, and ν ≥ 4 ⟺ 3q > 2n, by brute force for all n ≤ 8.
- Strict k-cycles realised exactly for k = ν, ν+1, ν+2 in six quota cases (η from 1/16 to 9/10) and three weighted games.
- Nontrivial ties realised for (n,q) = (4,2), (6,3), (5,2).
- Forbidden triangles realised for (n,q) = (3,2), (6,4), (5,3), (4,2), (9,6).
- Weighted examples: (3,2,2,1,1) with threshold 6 is proper with ν = 3. (2,1,1,1) with threshold 3 has ν = 3, and with
  threshold 4 it is collegial. (1,…,1) (7 judges) with threshold 5 has ν = 4.

This is Nakamura's theorem (K. Nakamura, *Int. J. Game Theory* 8 (1979) 55–61). Here it is applied to the margin partial
orders of A2, together with the realisability of every needed profile.

### 2.3 Margins that depend on the world or the judge

Nothing in A1–A8 or in Theorem A uses equality of the margins: replace r by r_v. Margins that depend on the world are
immaterial, since every statement is per world.

### 2.4 The audit's five-model certificate (CHECKED, `foundations.out` §1)

| model | A0 | A1 | A2 | A3 | A4 |
|---|---|---|---|---|---|
| judge losses | 5,5,5,5 | 1,6,6,6 | 2,1,7,7 | 3,2,1,8 | 4,4,4,4 |

- Each of A0 R A1, A1 R A2, A2 R A3, A3 R A4 is accepted by exactly three judges, with dissenters 1, 2, 3, 4
  respectively. A4 R A0 has four votes. Every reverse has at most one vote.
- No nontrivial ties occur among the five models. No (TC) violation occurs among any triple. The audit's claims hold.
- **Not reported by the audit:** the accepted set also contains A3 R A0 (judges 1, 2, 3) and A4 R A1 (judges 1, 2, 3).
  So there are strict **4-cycles** (A0, A1, A2, A3) and (A1, A2, A3, A4) as well as the 5-cycle. A strict 4-cycle is the
  shortest possible for (4,3) quorums, by Theorem A.

---

## 3. Part B: the escape question

### 3.1 What the barriers need

- **FF2 Thm 4.1 (H3).** One integrable strictly guiding penalty ℓ_i per world with ∫(ℓ_i(X) − ℓ_i(C_q)) dμ ≥ 0 whenever
  C_q ⪯_i X, i ∈ supp q, and X = C_q off some H_n. By Prop A8, this is the only hypothesis a quorum cover with a selection
  continuous in measure can fail. So FF2 Cor 4.3 says: **some world must have accepted comparisons out of selected
  models, supported in bounded regions, that no such penalty endorses.**
- **Q4.2 with HH1's repair.** Some world does not add up on relevant comparisons B ⪯_i X, with B ∈ C_L and X regular. By
  A7, every selected model is in C_L.

A **certificate** at world i is a finite family of accepted comparisons C^k R_i X^k with weights λ_k > 0 such that, at
a.e. h, the signed combination Σ_k λ_k(δ_{a_{X^k}(h)} − δ_{a_{C^k}(h)}) of advice ranks is first-order downward (every
upper tail sum ≤ 0), and nonzero on a non-null set.
- Then Σ_k λ_k ∫(ℓ(X^k) − ℓ(C^k)) dμ < 0 for **every** strictly guiding ℓ with finite integrals, so some comparison is
  not endorsed.
- For error indicators, the same certificate gives a positive combination of error-difference vectors that is ≤ 0 a.e.
  and not a.e. zero. That is an (M1) obstruction (write-up Def. addup), valid for every positive weight.

### 3.2 Lemma B0: one base never suffices; two crossing bases are needed (PROVED)

Let the base models C^1, …, C^m of a certificate at world i be ordered pointwise at world i: for each pair, one is at
least as good a.e. Then no certificate exists for any relation in which a pure improvement C R X (X strictly better
somewhere, nowhere worse) is never accepted. Strict (G) gives this, and every quorum world has strict (G) (A3).

*Proof.*
- Let C^m be a pointwise-worst base, and fix h. Every base's advice at h has rank ≤ ρ := rank C^m(h). So no move in the
  combination starts above ρ.
- The upper tail of the combination at level ρ+1 is therefore the total weight of moves ending above ρ. This must be
  ≤ 0, so no move ends above ρ.
- Every move out of C^m(h) that worsens ends above ρ. So no record out of C^m worsens anywhere, and each is a pure
  improvement, hence rejected. So no record out of C^m occurs.
- Induct on m. ∎

In particular, records all out of one coherent model never form a certificate. The audit's chain needed the arbitrary
intermediate models A1–A3 for exactly this reason.

### 3.3 Theorem B1 (a common endorser under the spread condition (E); PROVED)

Fix one world. Let 𝒲 be any winning family with minimal winning coalitions 𝒲_min, and let the margins be r_v. Suppose
there are vectors y^S ∈ ℝ^n_{≥0}, supported in S and nonzero, for S ∈ 𝒲_min, such that for a.e. h and t = 0, 1, 2:

  (E)  max_{S∈𝒲_min} Σ_v r_v y^S_v x^t_v(h) ≤ min_{S∈𝒲_min} y^S·x^t(h).

Put f(x) := min_S y^S·x and ℓ*(h, a_s(h)) := Σ_{t<s} f(x^t(h)). Then:
- ℓ* is measurable and strictly guiding;
- |ℓ*| ≤ (max_S ‖y^S‖_∞) Σ_v (ℓ_v(h,3) − ℓ_v(h,0)), so ℓ* has integrable envelope;
- L*(X) ≤ L*(Y) whenever X R Y, for **every** accepted comparison.

Consequently the world adds up, in the bounded countably additive sense, with density f(x^0) > 0 on the U-domain. It also
satisfies FF2's (H3) for every exhausting family.

*Proof.*
- Strict guidance: f(x) = min_S y^S·x > 0, since x ≫ 0 and each y^S ≥ 0 is nonzero.
- Let X R Y be accepted, with supporters containing some S₀ ∈ 𝒲_min, and use the notation of §1 for the record X → Y.
- f is a minimum of linear forms, so it is superadditive. Hence on P the ℓ*-increment satisfies
  Σ_t f(x^t) ≤ f(Δ) ≤ y^{S₀}·Δ.
- g(x) := max_S Σ_v r_v y^S_v x_v is a maximum of linear forms, so it is subadditive. Hence on Q the ℓ*-increment
  satisfies Σ_t f(x^t) ≥ Σ_t g(x^t) ≥ g(Δ) ≥ Σ_v r_v y^{S₀}_v Δ_v.
- So ∫_P Δ* ≤ Σ_{v∈S₀} y^{S₀}_v I_v ≤ Σ_v y^{S₀}_v r_v W_v ≤ ∫_Q Δ*. The middle step uses that each v ∈ S₀ supports the
  comparison, i.e. I_v ≤ r_v W_v.
- That is, L*(Y) − L*(X) = ∫_Q Δ* − ∫_P Δ* ≥ 0. ∎

**Corollary B1′ (quotas: the spread threshold; PROVED).** Let 𝒲 = {|S| ≥ q} with 2q > n and a common η. With y^S = 1_S,
(E) reads

  r·top_q(x) ≤ bot_q(x),

where top_q and bot_q are the sums of the q largest and the q smallest coordinates. It holds whenever
max_v x_v ≤ M\* min_v x_v, with

  **M\* := 1 + q(1−r)/((n−q)r) = 1 + 2qη/((n−q)(1−η)).**

*Proof.* Sort x ascending. Then top_q − bot_q = Σ_{j>q} x_j − Σ_{j≤n−q} x_j ≤ (n−q)(x_n − x_1)
≤ (n−q)(M\*−1)x_1 ≤ (n−q)(M\*−1)bot_q/q. So r·top_q ≤ r(1 + (n−q)(M\*−1)/q)bot_q = bot_q. ∎

Values:

| (n,q) | η = 1/16 | η = 1/3 | η = 1/2 | η = 9/10 |
|---|---|---|---|---|
| (4,3) | 7/5 | 4 | 7 | 55 |
| (5,4) | 23/15 | 5 | 9 | 73 |
| (7,5) | 4/3 | 7/2 | 6 | 46 |

These are CHECKED exact in `certificate.out` §B3, together with six other (n,q).

### 3.4 Sharpness: Theorems B2 and B3

**Theorem B2 (explicit certificate above M\*; PROVED, instances CHECKED).** Let 2q > n, a common η, and M > M\*.
- Let A, B be coherent models that **cross** at world i on open sets inside a bounded log-ratio region, i.e. both
  R_AB := {A good at i, B silent} and R_BA := {B good, A silent} contain open balls. The plain-posterior pairs of §3.5
  are examples.
- Then there is a quorum world i with judges' increments in K_M := {x ≫ 0 : x_v ≤ M x_w} and 2·C(n, n−q) accepted
  comparisons out of A and B whose records sum to a pointwise improvement.

*Construction.*
- **Types.** For each (n−q)-set D, let z_D := 𝟙 + (M−1)𝟙_D. Put N′ := C(q, n−q) and c := r(N′ + (M−1)C(q−1, n−q−1)).
  Then c/N′ = r(1 + (M−1)(n−q)/q) > 1 exactly when M > M\*. Pick b = 1 and a ∈ (N′, c].
- **Cells.** For each X ∈ {AB, BA} and each D, choose a ball N^X_D ⊆ R_X; the 2·C(n, n−q) balls are disjoint. Judge v
  has ℓ_v(h, a) = rank_i(h, a)·σ_v(h), with σ(h) = z_D on N^X_D and σ = 𝟙 elsewhere. These penalties are strictly
  guiding and bounded, with increments in K_M.
- **Type-level record R_D.** Improve mass a on type z_D, and worsen mass b on each type z_{D′} with D′ ∩ D = ∅.
  - Every v ∉ D (q judges) has I_v = a and W_v = b(N′ + (M−1)C(q−1, n−q−1)) = c·b/r. So I_v ≤ r W_v, and R_D is accepted.
  - Type z_{D′} is improved by R_{D′} (mass a) and worsened by the N′ records R_D with D ∩ D′ = ∅ (mass N′b < a).
- **Two copies.**
  - The A-copy of R_D is X^A_D := A, switched to good advice on a piece of N^{BA}_D of μ-mass s·a (A silent → good) and
    to silence on pieces Q^{AB}_{D,D′} ⊆ N^{AB}_{D′} of mass s·b (A good → silent).
  - The B-copy is symmetric.
  - Inside N^{AB}_{D′}, lay the pieces Q^{AB}_{D,D′} (total sN′b) inside the improvement piece of the B-copy of R_{D′}
    (mass sa), using an atomless parametrisation.
- **Pointwise net.** Each point carries at most one move silence → good and at most one move good → silent, and every
  point carrying the latter carries the former. So the net is worsening-free, with net improvement of μ-mass s(a − N′b)
  in each of the 2·C(n, n−q) balls.
- Every X^A_D equals A off the balls. It is regular, since only mixed problems change. ∎

For n = 4, q = 3 the construction is the 8-record certificate of §3.5. CHECKED: for 9 pairs (n,q) and 4 margins each,
at M = M\*·1001/1000, all records are accepted and the net is worsening-free and non-zero (`certificate.out` §B3).

**Theorem B3 (exact duality for polyhedral judge classes; PROVED).** Fix 𝒲, the margins r_v, and a cone K generated by
finitely many vectors z^1, …, z^m ≫ 0. The following are equivalent.
- (i) (E) holds on {z^1, …, z^m} (hence on K) for some nonzero y^S ≥ 0 supported in S, S ∈ 𝒲_min.
- (ii) Every quorum world (𝒲, r_v) whose adjacent increments lie in K a.e. has an integrable strictly guiding field
  endorsing all its accepted comparisons.
- (iii) For two coherent models A, B crossing at world i on open sets, no such world has a certificate made of
  comparisons out of A and B.

*Proof.*
- (i) ⇒ (ii) is Theorem B1. (E) is preserved by positive combinations: g is subadditive and f superadditive.
- (ii) ⇒ (iii): a certificate defeats every strictly guiding field (§3.1).
- (iii) ⇒ (i), contrapositive. Let T := {z^1, …, z^m}. For S ∈ 𝒲_min let
  Γ_S := {(α, β) ∈ ℝ^T_{≥0} × ℝ^T_{≥0} : Σ_z α_z z_v ≤ r_v Σ_z β_z z_v for all v ∈ S}
  (the type-level records accepted by the supporters S), and let V := Σ_S {β − α : (α, β) ∈ Γ_S}, a finitely generated
  cone.
  - **Stiemke alternative.** Consider the LP max 𝟙·s subject to v + s ≤ 0, 0 ≤ s ≤ 𝟙, v ∈ V. It is feasible and bounded.
    Its dual has value 0 iff some f ≥ 𝟙 has f·v ≥ 0 on V. So either V contains a nonzero v ≤ 0 (a type-level
    certificate) or some f ≫ 0 endorses V.
  - **Endorser gives (i).** If f ≫ 0 endorses V, Farkas' lemma on each Γ_S (the implication Au ≥ 0, u ≥ 0 ⇒ c·u ≥ 0 iff
    c ≥ Aᵀy for some y ≥ 0) gives y^S ≥ 0 on S with Σ_v r_v y^S_v z_v ≤ f_z ≤ y^S·z for every z ∈ T. This is (i), and
    y^S ≠ 0 since y^S·z ≥ f_z > 0.
  - **So if (i) fails, a type-level certificate exists.** It is realised out of A and B exactly as in Theorem B2: two
    copies, one ball per type and region, background σ = z^1. The world's increments lie in K. ∎

**Corollary B3′ (PROVED; both sides CHECKED).** For quotas with common η and K = K_M: (i) ⟺ M ≤ M\*.
- K_M is generated by the rays z_A = 𝟙 + (M−1)𝟙_A, ∅ ≠ A ⊊ [n]. On a ray the n−1 tight constraints x_v = M x_w,
  v ∈ A, w ∉ A, form a connected bipartite graph.
- The feasible families (y^S) form a convex set invariant under permutations of the judges. So if one exists, a
  symmetric one exists, which must be y^S = a𝟙_S.
- (E) on z_A then reads r(q + (M−1)min(q, |A|)) ≤ q + (M−1)max(0, |A| − (n−q)). The gap between the two sides is
  convex piecewise-linear in |A| with its minimum at |A| = n − q, where it gives M ≤ M\*.
- CHECKED: (E) at M = M\* on all rays, and failure at M\*·1001/1000, for the 36 cases of `certificate.out` §B3.

So **coherence of the bases gives no protection at all.** The threshold for comparisons out of two coherent models is
the same as for arbitrary comparisons.

### 3.5 The explicit certificate with geometric realisation (CHECKED)

Parameters: ε = 3/10, world 1, n = 4, q = 3, η = 1/16 (r = 15/17, M\* = 7/5), M = 2.

**Models.**
- A = C_{pA}, pA = (17/50, 33/100, 33/100); B = C_{pB}, pB = (33/100, 17/50, 33/100).
- Both are plain-posterior models near u: C_p = {g : p⊙g ∈ D_{T1}}, i.e. accept g iff c₀Σp_jg_j + ε·min_j p_jg_j > 0.
  They are selected in any cover that uses the plain posterior family.

**Regions** (`geometry.out`). The open sup-norm boxes of radius 59/300000 around the following centres lie in the stated
regions. The functions involved are 1-Lipschitz in sup norm, and the margins exceed the radius.
- R_AB box, centred at g_AB = (2393/9900, −529/2550, 2393/9900): A accepts (good at world 1), B is silent.
- R_BA box, centred at g_BA = (593/10200, 4193/9900, −529/2475): B accepts, A is silent.

Both boxes lie near ∂D_{T1}, have no zero coordinate, and lie in a bounded log-ratio region H_n. Split each into four
disjoint sub-boxes N^{AB}_w and N^{BA}_w, w = 1, …, 4.

**Judges.** ℓ_v(h, a) = rank_1(h, a)·σ_v(h), with σ_v = 2 on N^{AB}_w ∪ N^{BA}_w if v = w, and σ_v = 1 otherwise
(including off the boxes). So judges differ by a factor of at most 2.

**Pieces** (μ-masses in units s > 0 small). In N^{AB}_w, take disjoint Q^{AB}_{k,w} (k ≠ w) of mass 1 each and R^{AB}_w
of mass 1/4. Do the same in N^{BA}_w.

**The eight comparisons.**
- X^A_k := A with good advice on P^{BA}_k := ∪_{j≠k} Q^{BA}_{j,k} ∪ R^{BA}_k (mass 13/4), and silence on
  ∪_{w≠k} Q^{AB}_{k,w}.
- X^B_k := B with good advice on P^{AB}_k, and silence on ∪_{w≠k} Q^{BA}_{k,w}.
- Votes for A R X^A_k:
  - every v ≠ k has I_v = 13/4 and W_v = 4. Then W − I = 3/4 ≥ (1/16)(29/4), so v supports;
  - judge k has I = 13/2 and W = 3, so it dissents;
  - **accepted, 3 votes.** The same holds for B R X^B_k.
- **Net.** On every Q piece one record moves good → silence and another moves silence → good. Each R piece is improved
  once. So Σ_{8 records}(L(X) − L(base)) = −∫_{∪R}(ℓ(h, silence) − ℓ(h, good)) dμ < 0, for every strictly guiding ℓ.

CHECKED: `certificate.out` §B1 (votes, supporters, net) and `geometry.out` (regions).

**Robustness (CHECKED, `geometry.out`).**
- Both regions are realised, with explicit boxes, at **all three worlds**, for ε ∈ {1/20, 3/10, 1/2}, for
  pA = u + d(2,−1,−1) and pB = u + d(−1,2,−1) with d ∈ {1/300, 1/30000, 1/(3·10⁶)}.
- So the certificate can be placed at any world, out of selected models arbitrarily close to T1 = C_u, on cells next to
  ∂D_{T1} of arbitrarily small mass.
- Variant with η = 1/2, M = 8 > M\* = 7: also CHECKED (§B2).

### 3.6 Cycles in the escape world (the normative cost)

- **CHECKED (`certificate.out` §B4).** The world of §3.5 contains a strict 4-cycle Y_0 R Y_1 R Y_2 R Y_3 R Y_0. The Y_j
  have disjoint error sets made of pieces of types z_w and 𝟙. Judge v's losses are cyclic shifts of
  (1, 17/15, 289/225, 4913/3375), so each edge has 3 votes and each reverse has 1. No 3-cycle exists, by (TC).
- **Not determined.** Does every quorum world that escapes contain a strict cycle? With only the types z_w, the
  Condorcet construction needs M − 1 ≥ Σ_{p=1}^{3}(r^{−p} − 1). That is strictly more than M\* − 1 = 3(r^{−1} − 1). For
  M between the two thresholds I have neither a cycle nor a proof of acyclicity.

### 3.7 Consequences for quorum covers

**Corollary B4 (PROVED modulo FF2's import chain).** Let a cover of T1 have three quorum worlds, each with a proper game
and any margins, and a selection continuous in measure. Then at some world i, (E) fails for **every** family (y^S): the
set of problems where it fails for some adjacent increment is non-null. For quotas with common η_i: at some world, on a
non-null set, r_i·top_q(x) > bot_q(x), so there the judges' increments differ by a factor greater than M\*(n, q, η_i).

*Proof.* Otherwise each world has the field ℓ* of Theorem B1, endorsing all its comparisons. By Prop A8, T1 is selected,
so FF2 Thm 4.1 applies and gives a contradiction. ∎

**What this decides, and what it does not.**
- The barriers that survive without (IB) and transitivity (FF2 Thm 4.1, Q4.2 repaired) cannot exclude quorum covers.
  Theorems B2/B3 produce, at any world, out of any two crossing selected models near T1, accepted relevant comparisons
  that no single field endorses.
- The only constraint they leave is Corollary B4: judge spread above M\* at some world, on a non-null set. That costs
  nothing near small η (M\* = 7/5 for the audit's η = 1/16).
- The escape is confined to cells of arbitrarily small mass. So it is compatible with any behaviour elsewhere, but it is
  not shown to be compatible with competitiveness.
- Whether quorum covers exist is now entirely the competitiveness problem of BRIEF32, the 216-branch system, with fields
  spread beyond M\* somewhere. LL3 does not address it.
- HH2 Thm 5.1 / Cor 5.3 were not examined.

---

## 4. Status table

| # | Statement | Label |
|---|---|---|
| A1–A7 | audit's quorum lemmas (IB, strict G, no ties, TC, closed sections incl. C_p = X and non-injective, direct (C), undominatedness) | PROVED |
| A2 | per-judge transitivity; judges are margin partial orders | PROVED |
| A8 | T1 automatically selected; FF2 Thm 4.1 applies verbatim | PROVED |
| Thm A | ties ⟺ ν = 2; TC ⟺ ν ≥ 4; strict k-cycles ⟺ proper and k ≥ ν; collegial ⟺ acyclic and endorsed; ν = ⌈n/(n−q)⌉ | PROVED; realisations CHECKED |
| §2.4 | audit certificate correct; also strict 4-cycles (A0..A3), (A1..A4) | CHECKED |
| B0 | certificates need two bases crossing at the world | PROVED |
| B1, B1′ | common endorser ℓ* under (E); quotas: spread ≤ M\* = 1 + 2qη/((n−q)(1−η)) | PROVED |
| B2 | explicit certificate out of two coherent models for every M > M\* | PROVED; instances CHECKED |
| B3, B3′ | duality for polyhedral judge classes; sharpness of M\* | PROVED; both sides CHECKED (36 cases) |
| §3.5 | posterior pair, 8 records, η = 1/16, M = 2: escape at world 1; regions at all worlds, near u | CHECKED |
| §3.6 | strict 4-cycle in the escape world | CHECKED |
| §3.6 | does escape force a strict cycle? | open |
| B4 | quorum covers need spread > M\* (fails (E)) at some world | PROVED modulo D1, BB2 6.1, M3.7–8 |

## 5. Files (`ll3py/`)

- `quorum.py`: exact cell bookkeeping, voting, Nakamura numbers.
- `foundations.py` → `foundations.out`: §2 checks.
- `geometry.py` → `geometry.out`: regions R_AB, R_BA for posterior pairs, with explicit boxes.
- `certificate.py` → `certificate.out`: §3.4–3.6 checks.
