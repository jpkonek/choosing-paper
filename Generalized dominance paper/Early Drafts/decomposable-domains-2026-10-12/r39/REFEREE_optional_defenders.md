# Referee report: AUDIT_optional_defenders.md

21 October 2026. Adversarial referee, one reader. The context is PP5_diagnostic_and_repair.md, PP6_selected_allocation.md and AUDIT_anchor_plan.md.

**Labels**
- **PROVED**: the full argument is given here.
- **CHECKED**: exact rational enumeration over all pointwise change types, or an exhaustive finite check. LP cross-checks are in floating point and agree with the exact constants.
- **NUMERICS**: a scan of PP5's local selected models.
- **CONJECTURE**: as stated.

**Scripts** are in `REFEREE_OD_py/`. Run each as `python3 -I -B <script>`; each writes a `.out` file.

**Conventions** follow BRIEF36 and PP5:
- Ranks: good 0 < silent 1 < bad 2 < contradiction 3.
- On the minority class M_k, the majority worlds rank A, S, B as 0, 1, 2, and world k ranks them 2, 1, 0.
- δ_l = r_l(X) − r_l(C).
- Φ_l^κ = κν(P_l) − ν(Q_l), and b_l = ν(P_l) − ν(Q_l).

The integrand of Φ_l^κ is κδ_l⁺ − δ_l⁻ = ((κ−1)/2)|δ_l| + ((κ+1)/2)δ_l.

---

## 0. Verdict table

| item | verdict |
|---|---|
| Line 12: a nontrivial change alters the rank at every world | CONFIRMED (CHECKED: the four advices have distinct ranks at every world, so all 4·4·3 changes alter every rank) |
| Lemma 1 (pointwise efficiency) | CONFIRMED (CHECKED on all seven faces) |
| Theorem 2 (no uniquely compulsory mixed defence) and its "two legally available" consequence | CONFIRMED |
| Its application to every face obligation | CONFIRMED |
| Theorem 3, pointwise inequality | CONFIRMED. The coefficients are optimal. Only regularity of C is used. |
| Theorem 3, "two worlds with Φ³ ≥ 0" | CONFIRMED |
| Theorem 3, second-largest bound (κ−3)/4·μ(D) | CONFIRMED, and **sharp** (new) |
| Sharpness of 3: the example | CONFIRMED |
| Sharpness of 3: existence of sets in the silent regions | CONFIRMED (argument supplied, §2.4) |
| κ = 2 → 4 verdict vectors | CONFIRMED |
| Neighbourhood control: Lipschitz constant 15 and radii μ(D)/60, μ(D)/120 | CONFIRMED |
| Neighbourhood control: face-obligation claim for PP5 sticky records | CONFIRMED |
| Theorem 4 (symmetric thinning) | CONFIRMED (CHECKED exhaustively on 3 and 4 objects) |
| Theorem 4, record-based version | CONFIRMED, with two small remarks (§3.2) |
| Application to PP5 | CONFIRMED. Explicit admissible radius supplied (η′ < 0.00474), plus a NUMERICS scan showing no new violations at worlds 2 and 3 either. |
| §4 recommendations | CONFIRMED, with one sharpening: edges impose no reason to raise κ (§5) |
| **Edge version of Theorem 3** (new) | **PROVED and CHECKED** (§5) |
| **Vertex version** (new) | **PROVED and CHECKED** (§6) |

Nothing in the note is wrong.

The two substantive additions are:
- **A uniform dichotomy.** For κ ≥ 3 in the interior and κ ≥ 1 on an edge, every record either has two κ-eligible defenders, or its unique κ-eligible defender is additively safe with a sharp margin.
- **No forced sticky records on edges, for any κ ≥ 1.**

---

## 1. Section 1 of the audit

### 1.1 Lemma 1: CONFIRMED

**Unanimous over I.** Let K be supported on I and g unanimous over I. Then p·g has a definite sign, up to coordinate-null sets, so D_K gives the correct advice at every world of I. Any other advice has rank ≥ 1 there.

**Mixed over I.**
- Regular changes: worlds of opposite orientation get δ of opposite sign. Since I contains both orientations, some world of I gets worse.
- A change to contradiction: rank 3 exceeds every regular rank.
- D_K is never contradictory, because K ≠ ∅.

`r1_interior.py` §1 enumerates every coherent-old change on each of the seven faces and finds 0 failures. The enumeration covers 12, 24 and 30 change types for |I| = 1, 2 and 3.

### 1.2 Theorem 2: CONFIRMED

Suppose ν(Q_i) > 0. Then on the non-null set where X improves world i, Lemma 1 gives a worsening world in I∖{i} at each point. With finitely many worlds, some j ≠ i receives a non-null part, so ν(P_j) > 0.

The consequence "no guidance in I ⇒ at least two worlds of I have ν(P) > 0" follows:
- If no world of I has ν(P) > 0, Lemma 1 forces X = C a.e., which is guidance.
- If exactly one world has ν(P) > 0, Theorem 2 gives guidance at that world.

"Legally available" is right under strict (G). A record with ν(P_l) > 0 and ν(Q_l) > 0 is neither compulsory nor forbidden.

The face application is correct. For q ∈ A(d) ∩ Δ_I, splicing realises d from C_q, and K_q is supported on supp q ⊆ I. For a boundary q it is the singleton {q}.

The remark about PP5 Prop 4.3 is correct. There, worlds 2 and 3 have ν(P) = sm > 0 and ν(Q) = (1+s)m > 0.

---

## 2. Section 2 of the audit: Theorem 3

### 2.1 Pointwise inequality: CONFIRMED (PROVED; CHECKED)

The audit's case split is complete:
- **Regular → regular on a mixed problem.** |δ| = a at all three worlds, the two majority δ's are equal, and the minority δ is opposite. So Σδ = ±a.
- **New advice contradictory.**
- **Unanimous problems.** All δ ≥ 1.

The bound (κ−1)a + ((κ+1)/2)Σδ ≥ ((κ−3)/2)a ≥ (κ−3)/2 needs κ ≥ 3 in the last step.

**CHECKED.**
- 900 exact checks: 30 change types × 6 world orders × κ ∈ {3, 7/2, 4, 10, 100}, with 0 violations.
- LHS − RHS is affine in κ, nonnegative at κ = 3, and has slope ≥ 0. So it holds for all κ ≥ 3.
- The audit's 540 = 30 × 6 × 3 is reproduced.

**Necessity of κ ≥ 3.** For κ = 2, 5/2 and 29/10, the minimum pointwise slack is −1/2, −1/4 and −1/20. The negative cases are A↔B changes, with a = 2.

**Optimal coefficients (CHECKED by LP).** Over all (α, γ) with Φ_j + Φ_k + α b_i ≥ γ μ(D), the optimum is α = (κ+1)/2 and γ = (κ−3)/2, for κ = 3, 3.5, 4 and 6.

By hand: the a = 1 constraints are γ ≤ α − 2 (minority improves; i is the minority) and γ ≤ κ − 1 − α (i is a majority world that improves). These meet at α = (κ+1)/2.

**Remark: what the proof uses.** It uses only that C is *regular*: never contradictory, and correct on unanimous problems. It does not use the support of K. So Theorem 3 also holds for edge- and vertex-supported C, but there it says nothing about which worlds of I are eligible (see §5).

### 2.2 Consequences: CONFIRMED

- **κ = 3.** For each i, Φ_j + Φ_k ≥ −2b_i ≥ 0. So no world can be the sole eligible one. Since Φ^κ is nondecreasing in κ, the two eligible worlds remain eligible for every κ ≥ 3.
- **κ > 3.** Take i = argmax Φ. Only b_i ≤ 0 is needed.

**The (κ−3)/4 bound is sharp (new; CHECKED).**
- Put silence → majority changes on M_1, M_2, M_3 with masses 1/2, 1/4, 1/4.
- Then b = (0, −1/2, −1/2) and Φ^κ = ((κ−1)/2, (κ−3)/4, (κ−3)/4)·μ(D).
- The second-largest value equals the bound exactly. This is the audit's own family at s = 1/2.
- LP over all 30 types confirms that the minimum is (κ−3)/4 for κ = 3.5, 4 and 6.
- With strict b < 0 the bound is an infimum, approached as s → 1/2⁺.

**Strengthening (PROVED; threshold CHECKED by LP).** The hypothesis b ≤ 0 can be dropped. With i = argmax Φ:

    second-largest Φ^κ ≥ ½[ ((κ−3)/2) μ(D) − ((κ+1)/2) b_i ].

Equivalently, for κ ≥ 3:

> **Interior dichotomy.** Every record out of a regular model either has two κ-eligible worlds, or its unique κ-eligible world i has **b_i > ((κ−3)/(κ+1)) μ(D)**.

The LP minimum of max_l b_l over records with two weakly ineligible worlds is exactly (κ−3)/(κ+1): 1/9, 1/5 and 3/7 at κ = 3.5, 4 and 6.

So for κ ≥ 3 a *forced* acceptance (a unique eligible defender) is never sticky. For κ = 3 the margin degenerates to b_i > 0. This is the precise sense in which κ ≥ 3 removes PP5 Prop 4.3.

### 2.3 Sharpness example: CONFIRMED (CHECKED)

The audit's formulas are correct:
- b = ((1−2s)m, −m, −m);
- Φ_1 = (κ−2s)m;
- Φ_2 = Φ_3 = ((κ−1)s − 1)m.

For κ ∈ [2, 3), the interval (1/2, min(κ/2, 1/(κ−1))) equals (1/2, 1/(κ−1)), which is nonempty exactly when κ < 3. At the midpoints for κ = 2, 9/4, 5/2, 11/4 and 29/10, there is exactly one eligible world in every case (`r1_interior.out` §3).

The phrase "among those giving the counting guarantee" is accurate. For κ < 2 even coverage fails: equal masses give Φ = (κ−2)(1, 1, 1)m < 0. The pointwise minimum of ΣΦ^κ is exactly κ − 2 (CHECKED).

So the thresholds are:
- **2** for interior coverage by the pool;
- **3** for two defenders, and equivalently for "no forced sticky record".

Both are sharp.

### 2.4 Existence of the sets in silent regions: CONFIRMED (PROVED)

1. For interior p, K_p = p + 3ε min(p)(Δ − u) is a triangle with nonempty interior, because min p > 0 and ε > 0.
2. Through any interior point x of Δ, the line parallel to the edge opposite e_k separates e_k from the other two vertices. Nearby lines through nearby points of int K_p do the same.
3. So the set of M_k lines meeting int K_p is a nonempty open set of planes, which has positive Gaussian measure. C_p is silent on all of it.
4. μ is atomless, so subsets of every smaller prescribed mass exist.
5. p ∈ A(d) trivially, so these records really are obligations.

### 2.5 The κ = 2 → 4 vectors: CONFIRMED (CHECKED)

At s = 3/4 the vectors are (1/2, −1/4, −1/4)m and (5/2, 5/4, 5/4)m.

The PP5 t7 instance is consistent with this: m₂/m₁ = 6.3958/8.5277 = 0.75.

"No longer forced by that first link" is the correct, limited claim. If the first link is accepted at world 2 or 3 instead, Prop 4.4 transfers the return quarantine to that world. This is a shift, not an elimination; the audit does not claim more.

Enlarging κ is harmless for existence, because E^2 ⊆ E^κ:
- every κ = 2 allocation remains admissible;
- strict improvements still have Φ^κ = −ν(Q) < 0.

### 2.6 Neighbourhood control: CONFIRMED

**Lipschitz constant.** The integrand of Φ^4 depends only on the record's (old, new) label at the problem, and δ ∈ [−3, 3]. So the integrand lies in [−3, 12] (0 off D). Labels differ on a set of mass ρ, so the Lipschitz constant is ≤ 15.

In general:
- Φ^κ is 3(κ+1)-Lipschitz;
- b is 6-Lipschitz;
- μ(D) is 1-Lipschitz.

**Radii.** μ(D)/4 − 15r > 0 for r < μ(D)/60. At r = μ(D)/120 the remaining margin is μ(D)/8, half of μ(D)/4.

**Face obligations.**
- For Prop 4.3 records every changed old label is S, so the silent-old mass s(d) equals μ(D).
- If ρ(d′, d) < μ(D), then d′ keeps silent-old mass ≥ μ(D) − ρ > 0. A precise boundary C_q is silent only on a null set, so A(d′) ∩ ∂Δ = ∅.
- The radius μ(D)/60 is far inside this.
- So on the ball the only obligation is W ≠ ∅, and either margin-bearing world discharges it.

**Remark.** Theorem 3 itself needs no neighbourhood. It holds for *every* record in H₁₂₃, because each such record is realised out of a coherent C_q. The ball is needed only to keep the hypothesis b ≤ 0, or more weakly the dichotomy's alternative, and the absence of boundary anchors.

---

## 3. Section 3 of the audit: symmetric thinning

### 3.1 Theorem 4: CONFIRMED (PROVED; CHECKED)

Take a violation of R′: x ⪯′ y ⪯′ z, z ⪯′ x, and not x ⪯′ z.
- Since z ⪯′ x survives, the pair {x, z} was not deleted. So "not x ⪯ z" already held in R.
- The premises lie in R′ ⊆ R.

So it was an old violation. Repeated objects cause no trouble, and deleting {x, x} would only remove premises.

**CHECKED (`r4_thinning.py`).**
- 3 objects: all 64 relations × 8 masks, giving 512 cases. Symmetric deletion creates 0 new violations. One-sided deletion creates new violations in 18 cases.
- 4 objects: 4,096 relations × 64 masks, giving 262,144 cases. Symmetric deletion creates 0 new violations; one-sided deletion creates them in 32,796 cases.

### 3.2 Record-based version: CONFIRMED

- **Pair-level thinning.** rev(rec(X, Y)) = rec(Y, X), so O = rev(O) deletes unordered model pairs. Theorem 4 then applies to the whole relation, rivals included.
- **(IB).** R_i ∖ O is still a set of records.
- **Closedness.** A closed set minus an open set is closed. rev is a ρ-isometry, since swapping labels preserves "labels differ". So B(d, r) ∪ B(rev d, r) is open and symmetric. Numerically the maximum |Δρ| was 1.7e−17 on 40 sampled pairs.
- **(G).** It requires only O ∩ Guid_i = ∅ at the thinned world. The phrase "in both directions" is automatic once O = rev(O).

Two remarks:
- **(a)** The identity record must not lie in O, or reflexivity fails. This is covered because identity is guidance.
- **(b)** Thinning preserves neither the defence clause nor protection of selected models. The audit says so, and §3.3 supplies the receiving worlds.

### 3.3 Application to PP5: CONFIRMED (radius supplied; NUMERICS added)

The diagnosis is correct. PP5 §3.3's new triples close because the reverse acceptance, for example C_b ⪯₁ C_a, becomes strict. By Theorem 4, every one of PP5's 2, 7 and 25 "new" world-1 pairs disappears under symmetric deletion.

PP5 §4.1 (N1) already drew the qualitative lesson. The audit adds the global guarantee.

**Eligibility of the four receiving directions.** These are from PP5's certified masses, with κ = 2 and Lipschitz constant 9:

| record | receiving world | Φ | Φ/9 | world-1 guidance distance ν/3 | silent-old mass |
|---|---|---|---|---|---|
| d_ab | 3 | 0.049523 | 0.005503 | ν(Q₁)/3 = 0.004969 | 0.024259 |
| rev d_ab | 2 | 0.046977 | 0.005220 | ν(P₁)/3 = 0.005582 | 0.006763 |
| d_bc | 2 | 0.048116 | 0.005346 | ν(Q₁)/3 = 0.005778 | 0.007062 |
| rev d_bc | 3 | 0.048290 | 0.005366 | ν(P₁)/3 = **0.004742** | 0.023917 |

So the following symmetric repair is admissible for any common radius **η′ < 0.00474**: remove the open balls B(d, η′) ∪ B(rev d, η′) from R₁, and add the closed balls at the receiving worlds. The binding constraint is avoiding world-1 guidance near rev d_bc.

All four reverse and forward directions are also additively safe at their receiving worlds, with add > 0.0207. So AF would accept them there anyway.

**NUMERICS (`r3_symmetric_repair.py`, PP5's 227-model local scan, η ∈ {0.001, 0.0025, 0.005}).**
- Both "add at the receiving world" and "add only where no other world accepts" give:
  - 0 new violating pairs at every world, including worlds 2 and 3;
  - W ≠ ∅ on every pair;
  - 0 dominated selected models;
  - eligibility at every receiving world;
  - no world-1 guidance removed.
- The diagnostic triple is gone. The unrelated greedy violations remain (7,996, or 7,983 at η = 0.005). The repair is local, as the audit says.
- This covers selected models only. Rivals, and the receiving worlds against rivals, are untested.

---

## 4. Section 4 of the audit: recommendations

All four points are CONFIRMED and consistent with PP6:
- Strict 4-cycles are realisable (PP6 §3).
- PP6 Lemma 4 forces only *local* half-plane (order-type) structure, not a global potential.

One sharpening follows from §5. The case for κ = 4 is an interior one. On edges, any κ ≥ 1 already gives coverage, and it already rules out forced sticky acceptances. No finite κ gives two edge defenders unconditionally, so raising κ further buys nothing there.

---

## 5. Edge version of Theorem 3 (new)

**Setting.**
- C = D_K is coherent with K ⊂ Δ_{ij}. K may be a segment (imprecise) or a point (precise; audit's family at boundary indices).
- X is an arbitrary measurable four-advice rival, d = rec(C, X), D is the changed set, and κ ≥ 1.
- k is the third world.

For d ∈ H_{ij}, the edge obligation is W(d) ∩ {i, j} ≠ ∅. World k cannot discharge it. Every record of H_{ij} is realised in this setting by splicing onto a compatible C_q with q ∈ Δ_{ij}. So the results below hold on all of H_{ij}, with no neighbourhood argument.

**Pointwise structure (PROVED; CHECKED: 24 imprecise and 18 precise change types).**
- **(P1)** On unanimous problems and on M_k, which are exactly the problems unanimous within I, C is correct for i and j. Every change has δ_i, δ_j ≥ 1.
- **(P2)** On M_i ∪ M_j:
  - a regular → regular change has δ_j = −δ_i and |δ_i| = a ∈ {1, 2};
  - a change to contradiction has δ_i, δ_j ≥ 1.
- Hence δ_i + δ_j ≥ 0 everywhere. Equality holds exactly on regular changes in M_i ∪ M_j, the set D_reg, and the sum is ≥ 2 elsewhere.

### Theorem E (PROVED; CHECKED). For κ ≥ 1:

    (E0)  b_i + b_j ≥ 2 μ(D ∖ D_reg) ≥ 0                    (edge count)
    (E1)  Φ_i^κ + Φ_j^κ ≥ (κ−1) μ(D)
    (E2)  Φ_j^κ + ((κ+1)/2) b_i ≥ ((κ−1)/2) μ(D),   and the same with i and j exchanged.

**Proof.**
- On D_reg, the (E2) integrand is ((κ−1)/2)a + ((κ+1)/2)δ_j − ((κ+1)/2)δ_j = ((κ−1)/2)a.
- Elsewhere it is ≥ κ + (κ+1)/2.
- For (E1), the integrand is (κ−1)a on D_reg and ≥ 2κ elsewhere.
- Integrate. ∎

**Sharpness (CHECKED).**
- **(E1) and (E2): equality.** Take balanced A→S and B→S changes on M_i, which are available for precise edge models. Equality holds for every κ.
- **(E2): optimal pair.** The LP optimum over all (α, γ) with Φ_j + α b_i ≥ γ μ(D) is (α, γ) = ((κ+1)/2, (κ−1)/2), for κ = 1.5, 2, 3, 4 and 8. This holds for both the imprecise and the precise type sets.
- **By hand.** The a = 1 constraints are γ ≤ κ − α and γ ≤ α − 1.

### Corollaries (PROVED; thresholds CHECKED by LP)

**E-a. Coverage.** For every κ ≥ 1, some world of {i, j} is κ-eligible, with margin max(Φ_i, Φ_j) ≥ ((κ−1)/2) μ(D).
- κ ≥ 1 is necessary. For κ < 1, balanced regular changes give Φ_i = Φ_j = (κ−1)/2 · μ(D) < 0.
- At κ = 1 the pool is the additive pool, and coverage is the edge count.

**E-b. Two defenders with margin.**

    min(Φ_i^κ, Φ_j^κ) ≥ ((κ−1)/2) μ(D) − ((κ+1)/2) max(b_i, b_j).

So both edge worlds are κ-eligible whenever **max(b_i, b_j) < ((κ−1)/(κ+1)) μ(D)**.
- The threshold is exact: the LP minimum of Φ_j given b_i, b_j ≤ β equals the formula at every β tested, including both sides of the threshold.
- **The literal analogue of Theorem 3's hypothesis is degenerate here.** By (E0), b_i, b_j ≤ 0 forces b_i = b_j = 0 and D = D_reg. Both worlds are then eligible for every κ ≥ 1, with margin exactly ((κ−1)/2) μ(D). In this case Φ_l = (κ−1)ν(P_l) and ν(P_i) = ν(P_j) = ½∫|δ_i| ≥ μ(D)/2.

**E-c. No κ guarantees two eligible edge defenders unconditionally, even when neither world is guidance.**
- *Example.* Take a precise C_p, p in the open edge. Let X = C_p, except: silence on a subset of M_i where C_p says A (mass m, improving i), and silence on a subset of M_i where C_p says B (mass m/(2κ), worsening i).
- Then ν(P_i), ν(Q_i), ν(P_j), ν(Q_j) > 0, so neither world is guidance and both are legally available (Theorem 2).
- But Φ_i^κ = −m/2 < 0 for every κ. This was checked exactly up to κ = 10⁶.

**E-d. Unique edge defenders are additively safe.** If Φ_j^κ < 0, then by (E2) with i and j exchanged:

    b_i > ((κ−1)/(κ+1)) μ(D).

- Sharp, with ≥ attained at Φ_j = 0: masses 1/(κ+1) and κ/(κ+1) give b_i = 1/3 at κ = 2 and 3/5 at κ = 4.
- So for every κ ≥ 1 there is **no forced sticky record at an edge obligation**. Every acceptance forced by the pool there is additively safe, by a margin proportional to μ(D), and AF's additive branch already makes it.
- The PP5 Prop 4.4 return of such a forced edge acceptance satisfies b_i(return) ≤ −b_i(first link) < 0. So it is strictly additively unsafe at that world.
- *CONJECTURE (not checked).* An additive core with a sticky branch confined to H₁₂₃ quarantines these returns automatically.

**E-e. Guidance cases ("non-guidance alternative").**
- If one edge world, say j, is guidance (ν(Q_j) = 0), the obligation is discharged compulsorily by (G), and no pool choice is involved.
- No alternative is guaranteed. A→S on M_i alone gives guidance at j and a *strict improvement* at i, so i is even forbidden. None is needed.
- If neither world is guidance, both are legally available (Theorem 2). E-a to E-d give exactly what the κ-pool adds.

**Answer to the brief's question.**
- Two eligible defenders on an edge are guaranteed for no κ unconditionally. They are guaranteed for every κ > 1 under the sharp condition max(b_i, b_j) < ((κ−1)/(κ+1)) μ(D).
- "At least one alternative to a forced sticky acceptance" is not needed on edges for any κ ≥ 1, because a uniquely eligible edge defender is never sticky (E-d).

---

## 6. Vertex version (PROVED; CHECKED: 12 change types)

For K = {e_i}, C is correct for world i on every problem. So every change has δ_i ≥ 1. Hence:
- ν(Q_i) = 0 (guidance);
- b_i = ν(P_i) ≥ μ(D);
- Φ_i^κ ≥ κ μ(D).

The vertex obligation is discharged by (G) for any κ > 0. Other worlds can be strict improvements, for example B→A on M_i with δ = (2, −2, −2), and they are irrelevant. There is nothing to optimise at a vertex.

---

## 7. Summary of sharp thresholds

| face | pool covers the obligation | two eligible defenders in I | unique eligible defender |
|---|---|---|---|
| interior (I = {1,2,3}) | κ ≥ 2; ΣΦ ≥ (κ−2)μ(D) | κ ≥ 3 under b ≤ 0, with second-largest margin (κ−3)/4·μ(D); more generally when b_top < ((κ−3)/(κ+1))μ(D) | for κ ≥ 3, additively safe: b > ((κ−3)/(κ+1))μ(D). Forced sticky records exist for every κ ∈ [2, 3). |
| edge (I = {i,j}) | κ ≥ 1; max Φ ≥ ((κ−1)/2)μ(D) | never unconditionally; iff-type threshold max b < ((κ−1)/(κ+1))μ(D) | for every κ ≥ 1, b > ((κ−1)/(κ+1))μ(D) |
| vertex | guidance | — | guidance, b ≥ μ(D) |

All constants are sharp.

κ = 4 gives:
- interior: margin μ(D)/4 for two defenders under b ≤ 0, and an additive margin of μ(D)/5 for a unique defender;
- edges: an additive margin of 3μ(D)/5.

Lipschitz constants for transporting any of these to ρ-balls are 3(κ+1) for Φ^κ, 6 for b and 1 for μ(D).

**Still open, and untouched by this note:**
- (TC) at the receiving worlds against rivals;
- direct (C);
- a closed, record-based return quarantine for interior forced records when κ < 3, or a proof that κ ≥ 3 removes the need for one globally;
- a full cover of T1.

---

## 8. Files (`REFEREE_OD_py/`)

| script → output | content | label |
|---|---|---|
| `common.py` | exact rank and change-type enumeration (four advices; coherent old advice by face; precise or imprecise) | library |
| `r1_interior.py` → `.out` | line 12; Lemma 1 on all faces; Theorem 3 pointwise (900 checks); optimal coefficients; sharpness of 3; κ < 2; second-largest sharpness; interior dichotomy threshold | CHECKED (LP cross-checks float) |
| `r2_edge_vertex.py` → `.out` | Theorem E (E0–E2), optimal constants, E-b/E-d thresholds, E-c counterexample, κ < 1, vertex | CHECKED |
| `r3_symmetric_repair.py` → `.out` | symmetric PP5 repair on the 227-model scan; ρ-isometry of rev | NUMERICS |
| `r4_thinning.py` → `.out` | Theorem 4 exhaustively on 3 and 4 objects, against one-sided deletion | CHECKED |
