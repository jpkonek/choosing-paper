# PP4. Triple-local certificates: an analytic screen

20 October 2026, Brief 37. Labels:
- **PROVED**: the full argument is given here (one reader, me; not refereed).
- **CHECKED**: an exact finite computation, with the script named.
- **CONJECTURE**.
- **NUMERICS**: none used.

Scripts are in `PP4_py/` (`python3 -I <script>` inside that folder; outputs are in `*.out`). All verdicts in the scripts use integers or `fractions.Fraction`; LP solutions are re-verified in exact rationals.

The axioms and setting are those of the brief and the gate note: the full four-advice domain, Gaussian problems, rank steps U_i(X), and records. (TC) means: A ⪯ B ⪯ C implies not C ≺ A, where ≺ is strict in the relation. (G) means strict (G) in FF2's sense: every pointwise weak world-i worsening is accepted, and no strict pointwise improvement is. I add no assumption to the programme. Hypotheses that belong to a single result (mass-based verdicts, monotone verdicts, scale-free verdicts) are stated in that result and define its class.

---

## 0. Verdicts

1. **Triple certificates are exactly (TC) (Theorem 1, PROVED; CHECKED on 1,494 configurations).**
   - Take any reflexive relation at one world that satisfies (G). On every three models, a strictly guiding additive certificate exists if and only if (TC) holds on those three models. (IB) is not used.
   - So audit's condition is not strictly stronger than (TC) on records. It is a restatement of (TC).
   - The lead's 4,210 certified triples are an instance of Theorem 1.
   - Without the weak half of (G), (TC) does not suffice: there are 72 counterexamples in the check, and every one of them violates (G).
2. **Every consequence of (TC) binds unchanged (§1.3).**
   - This covers Remark 10 (the triangle condition), S9 (anchoring), S8 (convexity), Screen C's exclusion of hysteresis, Screen B's exact (TC) condition, and P3 Prop 3.4.
   - S3 and FF2 Thm 4.1 are neither implied nor escaped, because each needs more structure than (TC).
   - FF2 Cor 4.3 and HH2 Cor 5.3 still bind as requirements: in any cover, some world's triple evaluators cannot be glued into one field.
3. **Two-point swaps (Theorem 2, PROVED; CHECKED).**
   - Write r(x,y) for the log-threshold of the swap "add at x, remove at y".
   - On the two-swap layer, (TC) says exactly three things:
     - (P) there is no hysteresis: r(x,y) + r(y,x) ≥ 0;
     - (T) Remark 10: every 3-cycle sum of r is ≥ 0;
     - (E) when a 3-cycle sum equals 0, the three pairs on that cycle are exactly reciprocal.
   - (P) is new: it is a second condition, separate from the triangle condition.
   - Nothing else is required. Longer cycles are free.
4. **k ≤ 3 locations: one potential; k = 4: not (Theorem 3, PROVED; sharpness CHECKED).**
   - Take verdicts on small records that are mass-based, scale-free, monotone and polyhedral. On any three locations, (TC) forces a single positive potential that endorses every accepted record on those locations.
   - On four locations this fails. Example E below is a (TC) world whose two-point swaps out of selected models form a strict 4-cycle, and no integrable positive field endorses it.
   - So **non-additivity is left for small records**, but only in three forms:
     - (N1) certificates on ≥ 4 locations;
     - (N2) infinite chains, as in the two-world gate;
     - (N3) verdicts outside Theorem 3's hypotheses.
5. **Three worlds near an interior target (§3, PROVED).**
   - Competitiveness on small records adds exact inequalities across worlds.
   - On a pair of lines of the same class, either the two majority worlds split the two orientations, or the covering world and the minority world are exactly reciprocal (Proposition 3.2).
   - If the minority world has strict spreads on its own class, the majority worlds must carry *opposite total orders* on that class (CHECKED: 6 of 64 patterns survive).
   - This is the two-world gate structure, carried by the majority worlds. S11 (PP2 Thm 6) constrains only the minority world's priority on its own class, so this is precisely the structure S11 leaves open.
   - Three-class records: some world must accept sticky 3-location records. Under Theorem 3, covering them is *triple-local Bayes*: there is a prior that depends on the three lines.
6. **What survives (§4).** A local rate scheme Σ_loc meets (P), (T) and (E) on every triangle, and the covering inequalities of Proposition 3.1 (two-location records and three-class records). Its non-additivity is of type (N2).
   - With gates as the implementation of the orders, it fails on same-class records over three lines whose key ranges nest, wherever selected models realise that pattern (PP1 Prop 2's mechanism). So the orders must follow the geometry of the lines, or be replaced by monotone rates; Proposition 3.4 gives the exact condition in that case.
   - What is not designed: the verdict on mixed records with many locations (clause D).
   - §4 lists exactly what must be proved for (S) and for undominatedness.

---

## 1. Triple certificates and (TC)

### 1.1 Definitions

- Fix a world i and write U(X) := U_i(X) for the step set.
- A **certificate** for three models X, Y, Z is an integrable f > 0 a.e. on rank steps, with F(U) := ∫_{U(U)} f dν, such that:
  - U ⪯ V implies F(U) ≤ F(V);
  - U ≺ V implies F(U) < F(V);

  for all U, V in {X, Y, Z}. This is audit's "strictly guiding additive evaluator that supports every comparison among the three and preserves strictness": a strictly guiding additive loss at world i is exactly a positive weight on rank steps.
- The **type** of a step s is the triple t(s) = (1_{s∈U(X)}, 1_{s∈U(Y)}, 1_{s∈U(Z)}) ∈ {0,1}³. Let T be the set of non-constant types carried by a non-null set of steps.
- F(U) − F(V) = Σ_{t∈T} c_t (t_U − t_V), where c_t is the f-mass of the steps of type t. As f ranges over integrable a.e.-positive functions, (c_t) ranges over all of (0,∞)^T, because ν is finite. **So a certificate exists if and only if a finite linear system in c > 0 is feasible.**

### 1.2 Theorem 1

**Theorem 1 (PROVED).** Let ⪯ be a reflexive relation satisfying (G) at world i. For any three pairwise distinct models, a certificate exists if and only if (TC) holds on them. Hence "every triple has a certificate" is equivalent to (TC).

*Proof.* Certificate ⇒ (TC) is immediate: X ⪯ Y ⪯ Z ≺ X would give F(X) ≤ F(Y) ≤ F(Z) < F(X).

For the converse, suppose no certificate exists. By Motzkin's transposition theorem there are λ_{UV} ≥ 0 on the accepted ordered pairs (U ⪯ V) such that the following holds. Put κ := Σ λ_{UV}(e_U − e_V) ∈ ℝ³, so that Σκ = 0. Then κ·t ≥ 0 for every t ∈ T, and either κ·t > 0 for some t ∈ T, or λ_{UV} > 0 on some strict pair.

1. **Lemma A.** If κ·t = 0 on T, then κ = 0.
   - The non-constant types fall into three complementary classes: {100, 011}, {010, 101} and {001, 110}. On each class, κ·t vanishes iff κ_X = 0, κ_Y = 0, κ_Z = 0 respectively.
   - X ≠ Y needs class 1 or class 2 to be present; X ≠ Z needs class 1 or 3; Y ≠ Z needs class 2 or 3. So at least two classes are present, two coordinates of κ vanish, and Σκ = 0 gives the third.
2. **Case κ = 0.** Then λ is a circulation with λ > 0 on a strict pair. It decomposes into cycles, and the strict pair lies on one of them.
   - A 2-cycle U ⪯ V ⪯ U contains no strict pair.
   - So there is a 3-cycle U ⪯ V ⪯ W ⪯ U with one link strict, say W ≺ U. That violates (TC).
3. **Case κ ≠ 0** (so κ·t > 0 somewhere, by Lemma A).
   - **Lemma B.** Every source–sink pair (P, N), with κ_P > 0 > κ_N, has U(N) ⊆ U(P).
     - If N is the only negative entry, a type with t_N = 1 needs t_P = 1 for every P with κ_P > 0.
     - If the negative entries are N and N′, a type with t_P = 0 needs t_N = t_{N′} = 0.
   - Distinct models have distinct world-i step sets, because ranks determine advice. So N is a strict pointwise improvement of P.
   - The flow λ decomposes into paths from sources to sinks (plus cycles), so there is an accepted path from some P to some N.
     - If the path has length 1, then P ⪯ N, which strict (G) forbids.
     - If it has length 2, P ⪯ M ⪯ N, then (G) gives N ≺ P, which violates (TC). ∎

**CHECKED (`t1_triple_vs_tc.py`).** I enumerated every type set T with pairwise distinct models and every relation on three models.
- With (G): 1,494 configurations, of which 1,170 satisfy (TC). Every one of the 1,170 has an exact certificate, and no configuration that violates (TC) has one.
- Control, with strict (G) only: there are 72 configurations that satisfy (TC) and have no certificate. In each of them, a strict pointwise improvement X ⊂ Z is left incomparable. The weak half of (G) would install X ⪯ Z, and (TC) would then fail.

**Remark 1.1.** Certificates on k ≥ 4 models are strictly stronger than (TC).
- The strict 4-cycle of Example E (§2.3) has no certificate on its four models.
- Audit's 5-region example has no certificate on its five models: it would need w₄ ≤ 0.
- The rest of this note shows that this gap is the whole room left by (TC).

### 1.3 What binds anyway

| Screen | Uses | Binds on triple-certificate rules? |
|---|---|---|
| Remark 10 (triangle condition) | (TC), (IB), double crossing | **Yes, verbatim.** It is sharpened by (P) and (E) in Theorem 2. Double crossing near an interior target is CHECKED in §2.4 |
| S9 (anchoring collapse, P3 Thm 3.2) | (IB), strict (G), (TC) | **Yes, verbatim.** Triple certificates do not prevent anchors. A rule that judges every record containing some pattern by one additive score collapses near there to that score, *globally* on small records |
| S8 (convexity) | (TC) | **Yes.** Theorem 3 is a local strengthening: on ≤ 3 locations even non-convex monotone rules are endorsed |
| Screen C (hysteresis), Screen B ((TC) condition), P3 Prop 3.4 (orientation sign-consistency), HH2 Lemma 1.4 (no two accepted records compose to a strict improvement) | (TC) | **Yes.** (P) in Theorem 2 is Screen C's two-problem swap in rate form |
| S3 (finite-statistics collapse) | finitely many fixed additive judges in quorum form; no (TC) | **Not implied, not excluded.** Triple evaluators vary with the triple; nothing makes them a finite committee. If an implementation draws them from a finite list by quorum, S3 applies to it |
| FF2 Thm 4.1, HH2 Thm 5.1 | one field ℓ endorsing (or satisfying (Loc) for) local comparisons out of selected models | **Not implied.** Their contrapositives (FF2 Cor 4.3, HH2 Cor 5.3) bind as **requirements**: some world's triple evaluators cannot be glued into one integrable strictly guiding field, and that world fails (Loc) for every ℓ. By Theorem 3 the failure cannot sit on ≤ 3 locations (under its hypotheses) |
| S10, S11 | gates with fixed keys | Do not apply (no gate is assumed). §3 shows that a gate-like structure is forced on the majority worlds, and §4 lists the S11-type check |

---

## 2. Small swaps at one world

### 2.1 Setting

- Fix a world. A **location** is a non-null set R_x of world-i rank steps, all at one level. Different locations are disjoint.
- An **x→y swap** is a record whose added steps lie in R_x and whose removed steps lie in R_y, both non-null, with x ≠ y. Write m_x and m_y for the two masses.
- **Rule S (swap-only).**
  - Accept identity and guidance.
  - Accept an x→y swap iff m_x ≥ ρ(x,y) m_y, with ρ(x,y) ∈ (0, ∞]; ∞ means "never".
  - Refuse everything else.
- Write r := log ρ.
- Rule S is (IB) and satisfies strict (G).
- It is the scale-free form of Remark 10: ρ < 1 is the sticky direction and ρ > 1 a spread.

### 2.2 The exact content of (TC) on swaps

**Lemma 2.1 (no hysteresis; PROVED).** (TC) implies r(x,y) + r(y,x) ≥ 0.

*Proof.* Suppose ρ_xy ρ_yx < 1.
- Let X have b-steps of masses β and β′ and lack some a-steps of mass α.
- First link: X → Y adds those a-steps and removes all the b-steps. It is accepted when α ≥ ρ_xy (β + β′).
- Second link: Y → Z re-adds the β b-steps and removes the α a-steps. It is accepted when β ≥ ρ_yx α.
- Both hold for small β′ > 0.
- Z is X without the β′ steps, a strict improvement. So Z ≺ X by (G), and X ⪯ Y ⪯ Z.
- If the a- and b-sets are chosen inside steps where some selected model has the b-steps and not the a-steps, and some other selected model has the reverse, both links are records out of selected models. Pair crossing suffices. ∎

**Lemma 2.2 (triangle; PROVED; Remark 10 with the equality case).** Take three locations a, b, c and the local models W₁ (steps on b, c), W₂ (on c, a) and W₃ (on a, b). Then (TC) and (P) imply:
- (T) ρ_ab ρ_bc ρ_ca ≥ 1;
- (E) if ρ_ab ρ_bc ρ_ca = 1, then ρ_ab ρ_ba = ρ_bc ρ_cb = ρ_ca ρ_ac = 1;

and the same for the other orientation.

*Proof.* The forward links W₁ ⪯ W₂ ⪯ W₃ ⪯ W₁ hold iff α ≥ ρ_ab β, β ≥ ρ_bc γ and γ ≥ ρ_ca α. (TC) then requires every reverse link, for example W₁ ⪯ W₃, i.e. α ≥ ρ_ac γ.
- If the product is < 1, the forward set is open and non-empty. Over that set, α/γ reaches down to ρ_ab ρ_bc, so ρ_ac ≤ ρ_ab ρ_bc and ρ_ac ρ_ca ≤ P_f < 1, contrary to (P).
- If the product is 1, the forward set is the ray of equalities. There α/γ = ρ_ab ρ_bc = 1/ρ_ca, so ρ_ac ρ_ca ≤ 1, and (P) gives equality. ∎

**Theorem 2 (PROVED).** Rule S satisfies (TC) if and only if (P), (T) and (E) hold for all distinct locations.

*Proof of sufficiency.* Take X ⪯ Y ⪯ Z and Z ⪯ X; I show X ⪯ Z. Classify steps by their type (x, y, z) ∈ {0,1}³.
- **Guidance, then guidance.** Z ⪯ X forces Z = X.
- **Swap a→b, then guidance.** Z ⪯ X can only be a swap that adds (100) ⊆ R_b and removes (011) ∪ (001) ⊆ R_a. X ⪯ Z then has masses (m_a^{011} + m_a^{001}, m_b^{100}). These dominate the first link's (m_a^{011}, m_b^{100} + m_b^{101}), so X ⪯ Z by monotonicity of the thresholds.
- **Guidance, then swap.** Symmetric.
- **Swap a→b, then swap c→d.** The cancelled types (010) and (101) force a = d and b = c respectively. List the cases in which the composite X → Z is a single swap:
  - (i) a = c, b = d, no cancellation: the sum of two accepted a→b records, which is accepted because each threshold set is a convex cone;
  - (ii) a = d, b = c: either a pure improvement, which Lemma 2.1's pump excludes under (P), or a smaller a→b swap whose acceptance follows from (P);
  - (iii) a = d, b ≠ c with (101) and (110) null, or b = c, a ≠ d with (010) and (011) null: exactly the triangle of Lemma 2.2, and (T), (E) give the reverse link.

  In every other configuration the composite adds, or removes, in two locations. Z ⪯ X is then itself a two-location record, which rule S refuses. ∎

**CHECKED (`t2_two_swap_tc.py`).** Four locations, three atoms each with masses 1, 2, 4, so 4,096 models. All 4,096³ triples were checked by a boolean matrix product, in integer arithmetic.

| rates | rule S: (TC) violations | rule M: (TC) violations | cycle with ρ-product < 1 |
|---|---|---|---|
| **E**: ρ = ½ on a→b→c→d→a, 2 on the reverse, 8 on diagonals | **0** | **0** | (a,b,c,d), product 1/16 |
| C1: triangle abc negative | 35,184 | 60,784 | (a,b,c) |
| C2: pair ab negative | 9,472 | 30,016 | (a,b) |
| C3: triangle product 1, pairs not reciprocal (violates E) | 3,072 | 3,072 | none |
| C4: triangle product 1, pairs reciprocal | 0 | 0 | none |
| C5: sticky everywhere, ρ = ½ (Remark 10) | 96,456 | 581,832 | (a,b) |
| C6: spread everywhere, ρ = 2 | 0 | 0 | none |

Rule M is a monotone closure of rule S. Removals stay inside one location y; additions may be anywhere, and those in some single location x ≠ y must pay. It is CHECKED here; its continuum (TC) is CONJECTURE (the case analysis is longer).

### 2.3 Endorsement: three locations yes, four locations no

**Corollary 2.3 (PROVED).** Take finitely many locations. The accepted swaps of rule S are endorsed by a location-constant potential w > 0 iff r has no negative cycle (difference constraints log w_y − log w_x ≤ r(x,y)). (TC) excludes negative cycles of length 2 and 3 only. In particular, any three locations are always endorsed.

**Example E (PROVED; CHECKED).** Take four locations with ρ = ½ around a→b→c→d→a, ρ = 2 on the reverse links, and ρ = 8 on the diagonals.
- Every pair sum is ≥ 0, and every 3-cycle sum is ≥ log 2 in both orientations, so (TC) holds by Theorem 2.
- The 4-cycle sum is −4 log 2.
- **No integrable f > 0 endorses it.** Take Lebesgue points a₀, …, d₀ of f in the four locations and small balls around them, with mass ratio ½ on each forward link. Endorsement gives f(b₀) ≤ ½ f(a₀), f(c₀) ≤ ½ f(b₀), f(d₀) ≤ ½ f(c₀) and f(a₀) ≤ ½ f(d₀), so f(a₀) ≤ f(a₀)/16.
- Finitely additive weights are handled as in the gate note (Yosida–Hewitt).
- Near any interior target the four swaps are records out of selected models (§2.4). So **(TC) does not force a single potential on two-point swaps out of selected models.**

**Theorem 3 (PROVED).** Let d ≤ 3 locations be given at world i, and consider the *pure* records on them: records whose changes inside each location are all additions or all removals. Each has a net vector v ∈ ℝ^d (+mass added or −mass removed). Assume:
- the verdict on pure records depends only on v (mass-based);
- the accepted set A is a cone (scale-free);
- A is monotone: v ∈ A and v′ ≥ v imply v′ ∈ A;
- A is a finite union of closed polyhedral cones.

Then (TC) and strict (G) give w ∈ ℝ^d, w > 0, with w·v ≥ 0 for every v ∈ A.

*Proof.*
1. **Duality.** Let K := cone(A), which is polyhedral and hence closed. If K ∩ (−ℝ^d_+) = {0}, separation of the dual cone from the open orthant gives w > 0 on K.
2. **Carathéodory.** Otherwise some u ≤ 0, u ≠ 0, equals v₁ + … + v_m with v_k ∈ A and m ≤ d ≤ 3.
3. **m = 1.** Strict (G) is violated.
4. **m = 2.** Realise X →v₁ Y →v₂ Z as a chain whose composite is pure with net v₁ + v₂. In each location, cancel on the same steps when the signs are opposite; scale the masses down so they fit. Then Z is a strict improvement of X with X ⪯ Y ⪯ Z, contrary to (TC).
5. **m = 3.** Put s := v₁ + v₂. Then −s = v₃ − u ≥ v₃, so −s ∈ A. The chain X ⪯ Y ⪯ Z with Z ⪯ X forces s ∈ A by (TC). Now s + v₃ = u is the case m = 2. ∎

**Sharpness (CHECKED).** Example E under the monotone rule M has no (TC) violation on cells, and has no positive potential. For d = 4, Carathéodory allows four-term certificates, and TC excludes only those with at most three terms.

**Reading.** On small records, (TC) is "no Motzkin certificate with at most three terms". Triple certificates of models (Theorem 1) and endorsement on three locations (Theorem 3) are two faces of this. What remains:
- **(N1)** certificates on ≥ 4 locations (Example E);
- **(N2)** infinite chains with no finite certificate. The two-world gate is the model case: sticky along a dense order with refusals, so that any potential must halve along unbounded chains;
- **(N3)** rules outside Theorem 3's hypotheses. These include non-monotone ones (gates are not monotone: an added high-key step can break the gate), scale-dependent ones (HH2 §6) and non-polyhedral ones.

**Lemma 2.4 (pumps for 3-location records; PROVED).** Suppose a world accepts the pure record (+α at a; −β at b, −γ at c) with γ > 0. Then (TC) forces it to refuse every b→a swap with masses (β′, α) and β′ ≤ β. In rate form, r(b,a) > log(β/α).

*Proof.* The second link would compose with the first to the pure improvement "−γ at c, −(β − β′) at b". ∎

So a world that accepts sticky 3-location records (β, γ ≥ α) must keep a strict spread, or a refusal, on the swaps back.

**Remark 2.5 (PROVED).** If r is continuous at the diagonal, so that r(x,y) → r̄(x₀) as x, y → x₀, then (P) gives r̄ ≥ 0. Sticky behaviour is therefore excluded at small separation. Negative rates, and with them type-(N1) cycles, must link locations bounded apart.

### 2.4 Crossing near an interior target (CHECKED, `t3_crossing.py`)

- I took six lines near u = (1/3, 1/3, 1/3) (four of class M_1, one each of M_2 and M_3) and 1,639 rational indices in the disc |p − u| ≤ 1/5.
- **Precise family D_{p}.** All 30 ordered pairs of world-1 step locations on distinct lines are realised. That is, for each pair some selected model has the second step and not the first. So every triple is doubly crossing, and Remark 10, Lemma 2.1 and Example E apply to records out of selected models.
- **Translates D_{K_p}, K_p = p + (1/10)(T − u).** All same-level pairs are realised. The 16 missing ordered pairs are of the form "level 1 absent on one line, level 2 present on another": these need K_p decided opposite ways on two lines (PP1's crossed pairs), which the window does not reach.
- For every ordered pair (P, Q) of the four M_1 lines, some selected model is A on P and S on Q. This is the hypothesis of Proposition 3.2.

---

## 3. Three worlds near an interior target: what covering adds

**Record types.** On a problem in M_w, a regular change moves the two majority worlds by d steps and the minority world w by −d. For changes A ↔ S:
- the majority worlds' steps are at level 1;
- the minority world's steps are at level 2.

**Proposition 3.1 (covering inequalities; PROVED from competitiveness on {1,2,3}).** Let p be interior and assume scale-free thresholds on the two-swap records below.
- **(C-same)** Let P, Q ∈ M_w, and let C_p be A on P and S on Q. The rival is S on P and A on Q.
  - Majority worlds j, k see the swap (+P1, −Q1).
  - World w sees (+Q2, −P2).
  - Covering for all mass ratios is: min(r_j, r_k)(P1, Q1) + r_w(Q2, P2) ≤ 0.
- **(C-diff)** Let P ∈ M_u and Q ∈ M_v with u ≠ v, C_p silent on both, and the rival A on both.
  - World u sees (+P2, −Q1).
  - World v sees (+Q2, −P1).
  - The third world sees a pure improvement.
  - Covering is: r_u(P2, Q1) + r_v(Q2, P1) ≤ 0.
  - The reverse record (both lines moved towards the minority) is pure worsening at the third world, so guidance covers it. Each world may therefore refuse it.
- **(Three-class)** Let P_w ⊆ M_w for w = 1, 2, 3, with C_p silent on all three (this needs int K_p ≠ ∅). The rival is A on subsets of masses m_w.
  - World i sees (+m_i at P_i2; −m_j at P_j1, −m_k at P_k1).
  - Some world accepts for every m. The count Σ off ≤ 2 Σ on of the gate note shows that 2·on − off ≥ 0 at the maximising world suffices, and that some sticky acceptance is necessary when the masses are balanced, because then off_i = 2 on_i at every world.

**Proposition 3.2 (dichotomy on same-class pairs; PROVED).** Let P, Q ∈ M_w be realised in both orientations (CHECKED in §2.4).
- **(a) Same world on both orientations.** If one majority world j attains the minimum in (C-same) for both orientations, then summing the two inequalities and applying (P) at worlds j and w gives r_j(P1,Q1) + r_j(Q1,P1) = 0 and r_w(P2,Q2) + r_w(Q2,P2) = 0. Both worlds are then *exactly reciprocal* on the pair.
- **(b) Strict minority spread forces opposite orders.** Suppose world w's pair sums on its own class are ≥ s > 0 on a finite set of lines, all of whose pairs are realised both ways.
  - Then every pair is split: one majority world covers each orientation.
  - The orientations covered by world j contain no 3-cycle. On such a cycle, r_j would sum to at most −(the reverse cycle sum of r_w), and that sum is > 0 by (T) and (E) at w. This would contradict (T) at j.
  - So world j's covered orientations form a **total order** on the lines ("add earlier, remove later"), and world k's form the **reverse order**.
- **CHECKED (`t4_split.py`).** For three lines with r_w ≡ 1, exactly 6 of the 64 assignments are feasible: the 6 orders. Each has an exact rational solution, and each infeasible one has an exact certificate. With r_w ≡ 0, 36 are feasible.

**Reading.** Locally, this is the two-world gate on each class, carried by its two majority worlds, with opposite priorities. The gate keys l⁻¹, u⁻¹ and 1 − u⁻¹, 1 − l⁻¹ have the same structure.

**Relation to S11.** PP2 Thm 6 needs a priority on M_w that is used at **two** edges at e_w, where the prioritising world is opposite in rank to another world. Only the minority world w meets that condition (with j on [e_w, e_j], and with k on [e_w, e_k]).
- A majority world j is opposite in rank on M_w only to w, so its order on M_w enters a Lemma 6.1-type construction at the single edge [e_w, e_j].
- So the structure forced here (two-sided spreads at the minority world, orders at the majority worlds) is the one S11 leaves open.
- Whether a weaker edge argument couples world j's order (through z_wj) with world k's reverse order (through z_wk) is the first check in §4. If both orders were fixed, and each had to make the edge threshold models selected, the strip argument would make them constant.

**Proposition 3.3 (triple-local Bayes; PROVED).** Assume Theorem 3's hypotheses at each world on the three locations of a three-class record. Then each world i has a potential (a_i, b_ij, b_ik) > 0 on its locations (P_i2, P_j1, P_k1) that endorses its accepted records.
- By Motzkin, covering gives y ∈ Δ with y_j a_j ≥ Σ_{i≠j} y_i b_ij for j = 1, 2, 3. In words: at prior y, silence weakly beats A on each of the three lines, under the triple's potentials.
- The potentials and y may depend on the triple (P₁, P₂, P₃).
- Suppose instead each world had one potential on all its locations. Then the sets of admissible y would be closed and convex, and every finite family of them would intersect. So all of them would intersect: C_p would be weak Bayes, and FF2 Steps 2–6 would exclude the system.
- **Hence the imprecision of C_p must be carried by the non-gluing of the triple potentials at some world: (N1) or (N2).**

**Proposition 3.4 (three same-class lines; PROVED).** Let x, y, z ∈ M_w. Suppose every mixed A/S pattern on {x, y, z} is realised by some selected model near p, and assume Theorem 3's hypotheses at each world on the three locations. Let w_j, w_k (level 1) and w_w (level 2) be the endorsing potentials. Then covering forces **w_w ∈ cone(w_j, w_k)**.

*Proof.* Otherwise Farkas gives v with w_j·v < 0, w_k·v < 0 and w_w·v > 0. Such a v is mixed, since it cannot be ≥ 0 or ≤ 0. The record "A→S where v > 0, S→A where v < 0", with masses |v|, is then refused at all three worlds. ∎

**What realisability excludes.** If y separates x from z near the target, the pattern "A on y, S on x and z" needs a convex K_p that meets x and z but misses y, which is impossible. So which patterns are realised depends on the geometry of the lines, and Proposition 3.4 must be applied pattern by pattern.

---

## 4. What survives, and what must be proved

### 4.1 The local scheme Σ_loc (records on at most three locations near the target)

At world i, classify each changed step as *own-class* (its problem is in M_i) or *foreign* (in M_j or M_k).

| record at world i | verdict | why |
|---|---|---|
| own-class swap (both sets in M_i) | spread: accept iff on ≥ 2·off, in both orientations | Prop 3.2(b) needs s > 0. Ratios in (½, 2) are accepted in neither direction, and the majority worlds cover them |
| foreign swap within one class M_w | weak gate along κ_w^{(i)}, sticky: accept iff 2·on ≥ off. The other majority world of M_w uses −κ_w | Prop 3.2(b): opposite orders; (C-same) holds with equality |
| foreign swap across two classes | refuse | a third world covers it by guidance (§3, (C-diff) remark) |
| own-class adds, foreign removes (C-diff, three-class) | sticky: accept iff 2·on ≥ off | (C-diff): (−log 2) + (−log 2) ≤ 0. Three-class: the count gives a winner |
| foreign adds, own-class removes | refuse | Lemma 2.4 requires refusal or a strict spread; guidance covers it at a third world |

The following are checked by hand against §§2–3.
- (P), (T) and (E) hold on every triangle. Every triangle with a refused edge passes. The all-finite triangles are own-class spreads (cycle sum 3 log 2) or foreign same-class gates (acyclic).
- Every covering inequality of Proposition 3.1 holds. PP1 Prop 2's full-reversal records are also covered when R and Q each sit on one line: the minority spread covers ratios ≥ 2, and whichever majority world has the right order covers the rest.
- **Gap (PROVED, by the same computation).** Take a same-class record on three lines whose κ-ranges *nest*. At the majority worlds it adds on Q and removes on R₁ ∪ R₂, with κ(R₁) < κ(Q) < κ(R₂). Then it fails the weak gate at both majority worlds, because −κ reverses but does not un-nest. Only the minority spread covers it, and only at ratios μ(R) ≥ 2μ(Q). So where such a pattern ("A on Q, S on R₁ and R₂") is realised, the gate implementation of the orders fails. This is PP1 Prop 2(a)'s mechanism.
  - The way out is to choose κ_w compatible with the geometry. CONJECTURE: if κ orders lines by where they cross K, a line lying between two others in κ separates them near the target, and the nested pattern is not realised (Prop 3.4, last paragraph).
  - Alternatively, replace the gates by monotone rates. Proposition 3.4 then applies.
- Non-additivity is of type (N2): sticky rates along dense orders κ_w at the majority worlds. So FF2 Cor 4.3 and HH2 Cor 5.3 are met formally.
- No clause judges every record that contains a fixed pattern by one additive score, so S9 has no anchor.

**What Σ_loc is not.** It is verified only on two-location records and on three-class records, not on every record with three locations (see the gap above). It is not yet a rule. It does not say how to judge a record that mixes several clause types, or that spreads over many locations (clause D). (S) needs such records to be covered too. This is the design question left open.

### 4.2 Exact list of what must be proved for a three-world construction built on Σ_loc

0. **Same-class records on three or more lines.** Choose κ_w so that nested patterns are never realised (geometric orders), or use monotone rates satisfying w_w ∈ cone(w_j, w_k) on every realised triple (Proposition 3.4). Then check the result on PP1's exact cells.
1. **(TC) globally.** On all triples, not just on ≤ 3 locations: no pumps across clauses. Lemma 2.4 is the template. The gate note's no-cycle lemma covers each gated clause separately but no longer covers their union.
2. **Clause D.** A verdict for records that mix own-class and foreign changes, several classes and many locations. It must:
   - (i) reduce to Σ_loc on the records of §4.1;
   - (ii) keep (TC);
   - (iii) cover every record out of C_p at some world in supp p.

   The three-world count Σ off ≤ 2Σ on gives a sticky winner before any admissibility restriction. The obligation is that the winner's record passes that world's admissibility condition.
3. **Support clause (competitiveness on supp p).**
   - Interior indices: items 2(iii), together with R1 (rivals with contradiction or unanimous errors).
   - Edges: selected models on [e_i, e_j] must have K_p ⊆ [e_i, e_j] (PP1 §6). Covering there uses two worlds, so on M_k the inequality of Proposition 3.1 must hold with only those worlds.
   - Vertices.
4. **Closed sections.** A_i(X) = {p : C_p ⪯_i X} must be closed for every X. The specific risks:
   - **Clause switching.** As p moves, the class pattern of rec(C_p, X) changes when a boundary of C_p crosses the changed set. The clause applied must not jump in the excluded direction.
   - **The gated clauses.** As in PP1 §6, at boundary problems the order κ_w must not undercut. The test on finite cells is PP1's split-model harness.
   - **Two-sided spreads.** These are thresholds of continuous masses, so they are closed.
5. **KKM dominators** (necessary). Every X needs q with C_q ⪯_i X at all three worlds. The following must be checked explicitly:
   - incoherent regular rivals (e.g. "A on every mixed problem");
   - PP2's tripod models;
   - PP1 §4's local rivals with Σψ ≥ 1;
   - the edge threshold models of PP2 Lemma 6.1, rebuilt from κ_w at the majority worlds.

   This is where the S11-type question of §3 is settled. Does world j's order on M_w have to make edge-[e_w, e_j] models selected, with threshold sets {z_wj ≤ y}? And world k's reverse order, with {z_wk ≤ y}? If both, the strip argument forces κ_w to be constant, and κ_w must then be record-chosen (PP2 (E1)).
6. **Undominatedness.** It is not automatic. PP1 Lemma U used antisymmetry, but (TC)-direct worlds may have ties and cycles.
   - It must be shown that no X ≠ C_p has X ⪯_i C_p at all three worlds.
   - In Σ_loc, each covering clause has its reverse refused or spread at the covering world. Same-class reverses are refused by the gated majority world, and cross-class reverses by the refusal rows. It remains to show this for clause D.
   - Direct (C): every tie with a selected model must be with a coherent model. (P) with strict inequality makes ties boundary-only on two-point swaps.
7. **Non-additivity in the required sense.** The aim is to show that, along the family near T1, no integrable strictly guiding field satisfies (Loc) at the majority worlds. This is the gate note's Prop 4(b), transported to the orders κ_w.

**Suggested first experiment.** PP1's exact cell harness with Σ_loc as the verdict and the orders κ_w as SAT unknowns:
- competitiveness;
- dominators, including split models;
- (TC) by matrix product, as in `t2`.

This would test items 1, 3 and 5 at once, on 6–8 lines with crossed pairs and edge-hugging lines (PP2's warning).

---

## 5. Files (`PP4_py/`)

| script | content | label |
|---|---|---|
| `t1_triple_vs_tc.py` → `.out` | Theorem 1: all type sets and relations on three models; the control without weak (G) | CHECKED |
| `t2_two_swap_tc.py` → `.out` | Theorem 2 and Example E: exhaustive (TC) on 4,096 models; rules S and M; controls C1–C6; negative-cycle certificates | CHECKED |
| `t3_crossing.py` → `.out` | Double crossing near the centre for precise and translate families; same-class orientations | CHECKED |
| `t4_split.py` → `.out` | Proposition 3.2(b): 6 of 64 orientation patterns, exact solutions and certificates | CHECKED |
