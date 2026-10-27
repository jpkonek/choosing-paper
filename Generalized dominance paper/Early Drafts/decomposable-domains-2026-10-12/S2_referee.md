# S2 referee report: leading charges without nestedness, two-world chains, the tie remark (S2_notes.md)

Round 13 (BRIEF12), task (R4). Independent, adversarial reading of `S2_notes.md` in full, with the scripts in
`s2py/` (all three re-run; outputs reproduced). Read against the write-up §§2–3, §8.4(c), §8.5 (all parts),
`P4B_referee.md` §§1, 8 and `Q3_referee.md` §§3–4. Independent checks are in `s2ref_py/` (run with `python3 -I`).
Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. No assumption is added to the framework.

## 0. Verdicts

| Claim | Verdict |
|---|---|
| **S2.1** (leading charge of world i: 0 on M, or strictly positive on M; any n ≥ 2, no nestedness) | **CONFIRMED.** Every step re-derived (§1). Two simplifications: the carrier lemma is not needed; continuity is needed only to produce one two-sided generic index. |
| S2.1′(a) Thm E2 and Cor E2′ without (Nest) | **CONFIRMED** |
| S2.1′(a) Prop B2(b) without nesting | **CONFIRMED WITH REPAIR** (B2 is stated in chain coordinates; restate it without them, §2.2) |
| S2.1′(b) Thm Q36(a), (b) without (Nest_e) | **CONFIRMED.** (c), (d) still need (Nest_e). |
| S2.1′(c) Cor Q37 strengthened, and its contrapositive | **CONFIRMED** at the status of Thm M0closed(b); CHECKED where a complete world enters |
| Lemma PL | **CONFIRMED WITH REPAIR.** The coherence of X needs C ∈ C_L; only X′ is coherent from F ∈ C_L alone. |
| Cross-agreement (§3) | **CONFIRMED.** The additive gloss is imprecise: the true conclusion is stronger (§3.3). |
| **S2.2** (n = 2, a nonzero leading charge at either world ⇒ C_L is a chain) | **CONFIRMED** |
| S2.3 | **CONFIRMED** (immediate from S2.1, S2.2) |
| S2.0(a) | **CONFIRMED WITH REPAIR.** Wording: the result is "on one edge (or n = 2)" and "nested", not "any n" and "strictly nested". |
| S2.0(b) | **CONFIRMED** |
| S2.0(c) (three additive worlds: every edge selection nested) | **CONFIRMED WITH REPAIR.** Step 2 asserts an incoherent Lyapunov half-splice without proof (GAP). Repaired by a bounded splice. The whole proof simplifies and generalises (Prop R-S2.A, §4.3): it suffices that worlds i, j are additive and world k is complete. |
| Correction of the write-up's remark before Prop comonotone | **CONFIRMED WITH REPAIR** in scope: for n = 3, integral (density) penalties only; replacement text in §4.4 |
| S2.4 item 1 | **CONFIRMED WITH REPAIR** (P must lie in R_ij; X′ is automatically incoherent for bounded P ∪ Q) |
| S2.4 items 2–3 ("fan") | **CONFIRMED** when worlds i, j are additive (integral). **GAP** in general: the general case gives only Y ⪯_{i,j} C, Y ⋠_k C. |
| S2.4 item 4 (two-parameter family selected at interior indices) | **GAP:** heuristic, not derived |
| S2.4 item 5 | **CONFIRMED, strengthened:** strict (G) suffices, and no leading charge at world k is needed |
| §5 attempts, §7 | Failure reports and conjecture labels. Consistent with the above; no verdict needed. |

---

## 1. Theorem S2.1, step by step

**Definitions used.** As in the write-up before Thm Q36, a leading charge of world i on M is a *bounded* charge π ≥ 0 on U that vanishes on null sets and satisfies, for measurable A, B ⊆ M:
- (i) π(B∖A) > π(A∖B) ⇒ A ≤_i B;
- (ii) A ≤_i B ⇒ π(B∖A) ≥ π(A∖B).

Because π is finite and additive, (i) and (ii) read: π(A) < π(B) ⇒ A ≤_i B, and A ≤_i B ⇒ π(A) ≤ π(B). The theorem needs boundedness. It is part of the Q36 definition, and "charge" in §8.4 means a finite charge.

World orders are orders on error sets. Strict (G) and (IB) give this through N9.4: X ⪯_i Y iff E_iX ≤_i E_iY. All edge comparisons are between subsets of R_ij ⊆ M, so (i) and (ii) apply.

**Edge facts.** Lemma Q34 is used correctly. It needs only strict (G) and competitiveness on supp p ⊆ {i, j}, and it gives:
- E_jC_p = R_ij ∖ E_iC_p;
- X_A := P_i off R_ij, with E_iX_A = A, is regular, and E_jX_A = R_ij ∖ A;
- X_A = C_p △ (A △ E_iC_p).

Also C_{e_i} = P_i (competitive on {i} against P_i, then strict (G)), and E_iC_{e_j} = R_ij. So m(e_i) = 0 and m(e_j) = π(R_ij). The function m(p) = π(E_iC_p) is well defined mod null because π vanishes on null sets.

**Small sets (no carrier needed).** Steps 1, 2 and 5 need, for every non-null E ⊆ M and every ε > 0, a non-null D ⊆ E with π(D) < ε.
- The note obtains D from a Yosida–Hewitt carrier. That is correct: for every ε there is a Z with μ(Z) < ε and σ(U∖Z) = 0, and π = ρμ off Z.
- A simpler argument suffices. Split E into k disjoint non-null pieces (μ is non-atomic). Some piece has π ≤ π(E)/k.
- So finite additivity of π creates no difficulty anywhere in S2.1.

**Step 1 (lower semicontinuity). Correct.**
- Fix p* with E_iC_{p*} non-null. If E_iC_{p*} is null, m(p*) = 0 and there is nothing to prove.
- Take D ⊆ E_iC_{p*} non-null with π(D) < ε, and put A := E_iC_{p*} ∖ D.
- Every edge index q with m(q) < π(A) has E_iC_q ≤_i A by (i), so q ∈ S_i(X_A).
- If such q accumulate at p*, the closed section S_i(X_A) contains p*. But X_A = C_{p*} △ D is strictly better at world i on D, so X_A ≺_i C_{p*} by strict (G). Contradiction.
- Uses: (i), closedness at world i, strict (G) at i. Competitiveness is not used.

**Step 2 (upper semicontinuity). Correct.**
- Suppose m(q_k) > m(q*) + η. Then π(R_ij ∖ E_iC_{q*}) > η, so that set is non-null.
- Take D in it, non-null, with π(D) < η, and put A := E_iC_{q*} ∪ D. Then π(A) < m(q_k), so by (ii) C_{q_k} ⋠_i X_A.
- m(q_k) > 0 forces q_k ≠ e_i, so j ∈ supp q_k. Competitiveness on supp q_k ⊆ {i, j} then gives C_{q_k} ⪯_j X_A. This step is valid, and it is the only use of competitiveness at non-vertex indices.
- Closedness of S_j(X_A) gives C_{q*} ⪯_j X_A. But E_jX_A = E_jC_{q*} ∖ D, so X_A ≺_j C_{q*} by strict (G) at world j. Contradiction.
- The case q* = e_i is covered: m(e_i) = 0, D ⊆ R_ij, E_jC_{e_i} = R_ij.

**Step 3 (generic levels). Correct.**
- m is continuous on the compact segment, so every v ∈ [0, π(R_ij)] is attained.
- A weak local max (min) value of m equals max_I m (min_I m) for some interval I with rational endpoints. So these values are countable, and (0, π(R_ij)) contains generic v.
- At any p with m(p) = v generic, p is neither a weak local max nor a weak local min. So every neighbourhood of p contains indices with m < v and indices with m > v. Such p are interior to the edge, since v ∉ {0, π(R_ij)}.

**Step 4 (optimality at both edge worlds). Correct.** Fix A ⊆ R_ij with π(A) = v.
- Indices with m < v lie in S_i(X_A) by (i).
- Indices with m > v lie in S_j(X_A), by (ii) and competitiveness, as in step 2.
- Both kinds accumulate at p, so closedness gives C_p ⪯_i X_A and C_p ⪯_j X_A.
- Only one generic index p is needed for step 5. Continuity serves only to produce it.

**Step 5 (π-null sets, "on either side"). Correct.** Let N′ ⊆ R_ij be non-null with π(N′) = 0. One of the two cases below holds, because N′ is non-null.
- If N′ ∩ E_iC_p is non-null: A := E_iC_p ∖ N′ has level v, and X_A ≺_i C_p.
- If N′ ∖ E_iC_p is non-null: A := E_iC_p ∪ N′ has level v, and E_jX_A = E_jC_p ∖ N′, so X_A ≺_j C_p.

Either case contradicts step 4. This is how strict (G) rules out π-null sets on either side: the generic model can neither contain nor avoid a non-null π-null set, because removing it is a strict world-i gain at no π-cost, and adding it is a strict world-j gain at no π-cost.

**Step 6 (linking).**
- Correct, and needed only for n ≥ 3. M = ⋃_{j≠i} R_ij mod null.
- R_ij ∩ R_ik contains a neighbourhood of e_i − η(e_j + e_k), which lies in U since K′ ⊆ Δ° is compact. So positivity on R_ij gives π(R_ik) > 0. Steps 1–5 on e_ik then give positivity on R_ik.
- Without linking one gets the dichotomy edge by edge. For n = 2, R_12 = M and the step is void.

**Conclusions.**
- Strict positivity on M forces ρ > 0 a.e. on M. If {ρ = 0} were non-null, removing a carrier of σ from it would leave a non-null π-null set.
- Endorsement follows from (ii).
- Adding up: the weight π + μ|_{N₊} is positive on non-null subsets of U = M ∪ N₊. Relevant comparisons have both error sets in M, because coherent and regular models are correct on N₊.

**Hypotheses actually used:**
- strict (G) at worlds i and j;
- (IB), through the normal form;
- competitiveness at the edge indices;
- closed sections at the edge indices, for the edge test models X_A only;
- for n ≥ 3, K′ ⊆ Δ°.

Not used: (C); (LA) beyond (S); nestedness; completeness; countable additivity; interior indices. The last is consistent with the locality barrier (Prop Q31), which concerns compact subsets of Δ°; the edges lie outside every such set.

**Consistency checks against refereed results.**
- Prop B2: lex(ν⁺, λ) has a nonzero leading charge vanishing on [0, x₀). B2(b) is the nested special case of S2.1.
- Thm N26.1: a full two-world system with a non-null primary tie. Its primaries have ρ_i > 0 a.e. and its undominated models form a monotone path, as S2.1 and S2.2 require.
- P4 Thm B3: in-order multi-level worlds cannot occur in a full system. This is again a special case.

No refereed construction contradicts S2.1.

**Verdict: CONFIRMED.** The proof is correct as written. With this report it has had two readers.

---

## 2. Consequences of S2.1

### 2.1 Thm E2 and Cor E2′ without (Nest): CONFIRMED

S2.1 with n = 2 is the conclusion of Thm E2 with (Nest), (K) and the chain removed. It uses strict (G), (IB) and (S) only.

Cor E2′ follows as before:
- the first level that is nonzero on M is a leading charge on M;
- strict (G) excludes all levels vanishing on M.

### 2.2 Prop B2(b) without nesting: CONFIRMED WITH REPAIR

B2 identifies M with [0,1] through the chain (c_b = [0,b)), and that identification presupposes nesting. Restated without it:

> **B2(b′).** Let n = 2, and let world 1 be lex(π, λ′), where π is a bounded charge, nonzero on M, that vanishes on a non-null subset of M, and λ′ is any strictly positive tie-breaker. Then no ranking with strict (G), (IB) and (S) has this world 1.

For instance, transport ν⁺ and λ to M by any measure isomorphism. This is S2.1, because π is a leading charge.

### 2.3 Thm Q36(a), (b) without (Nest_e): CONFIRMED

S2.1 is exactly Q36(a) with (Nest_e) removed, and (b) follows as in the write-up.

Q36(c) (complete worlds) and (d) (strict escape and Lemma T on R_ij) still use (Nest_e), through Prop Q35. The remark that "for a general acceptance cone positivity does not globalise" is unaffected.

### 2.4 Cor Q37 and its contrapositive: CONFIRMED

The proof of Cor Q37 goes through unchanged:
- (CP-a) worlds add up;
- leading-charge worlds have SP^reg_i by S2.1, for any selection with (S);
- complete worlds with (Nest_e) at e_i have SP^reg_i by Q36(c);
- so the ranking is (M0), which Thm M0closed(b) excludes.

Status: the status of M0closed(b), and CHECKED where a complete world enters.

Contrapositive, replacing (E-a)/(E-b) after Cor Q37. Every world of a cover of T₁ that does not add up:
- is not (CP-a), and has no leading charge nonzero on M (unconditionally); and
- either (E-a′) some edge family at e_i is not nested, or (E-b′) all are nested and the world is incomplete, with strict escape and Lemma T on every R_ij.

### 2.5 A further corollary (PROVED here, by inspection; one reader)

**Theorem LX's class is narrower than stated.** Take a lexicographic world (F_i, S_i) of Thm LX (on M_U, all axioms), with weakly signed primary c^F_i.
- Its primary π := |c^F_i|μ restricted to M is a leading charge of world i.
- By S2.1, either c^F_i = 0 a.e. on M, or c^F_i ≠ 0 a.e. on M.
- So "zeros allowed" can occur only in this all-or-nothing form on M.

This needs nothing beyond the hypotheses already stated for Thm LX.

---

## 3. Lemma PL, cross-agreement, and Theorem S2.2

### 3.1 Lemma PL: CONFIRMED WITH REPAIR

Let D ⊆ C△F, X = C△D and X′ = F△D.
- The set identity holds: E_kX = E_kC △ D, E_kX′ = E_kF △ D, and E_kF ∩ D = D ∖ E_kC.
- By de Finetti cancellation, C ⪯_k X iff (D ∩ E_kC) ≤_k (D ∖ E_kC) iff X′ ⪯_k F.
- The mirror statement F ⪯_k X′ ⟺ X ⪯_k C follows by exchanging C and F.

`s2ref_py/pl_orders.py` checks both equivalences, not just the set identity. It uses non-additive cancellative worlds (lexicographic with zero levels, and *incomplete* unanimity orders), n ∈ {2,3,4}, 20 000 trials: 0 violations. A control run with D not contained in C△F fails 13 607 times, so the hypothesis D ⊆ C△F is needed.

**Repair.** If F ∈ C_L and C ⪯_k X at every k, then:
- X′ ~_k F at every k, so X′ ∈ C_L by (C);
- C ~_k X at every k, by the mirror;
- X ∈ C_L only if, in addition, C ∈ C_L.

In every use C ∈ C_L, so nothing downstream changes.

### 3.2 Cross-agreement: CONFIRMED

With n = 2, crossing C, F ∈ C_L, P ⊆ A, Q ⊆ B and D = P ∪ Q:
- C ⪯_1 X iff Q ≤_1 P, and C ⪯_2 X iff P ≤_2 Q;
- X ⪯_1 C iff P ≤_1 Q, and X ⪯_2 C iff Q ≤_2 P;
- X′ is governed by PL.

All three bullets of the note follow:
- opposite strict orders make X dominate C, or X′ dominate F;
- a double tie makes both splices coherent through (C);
- under completeness, "one tie and one strict" makes X or X′ a dominator.

### 3.3 The additive gloss is imprecise

The note says that, in additive terms, cross-agreement forces ρ₂/ρ₁ to be constant on A ∪ B. In fact, if either world is additive with a density and both are complete, no crossing exists at all:
- take P ⊆ A and Q ⊆ B bounded, with ρ_1μ(P) = ρ_1μ(Q);
- they are tied at world 1, which cross-agreement forbids.

S2.2 supersedes this anyway.

### 3.4 Theorem S2.2: CONFIRMED

- **Step 2.** For n = 2, every regular X is X_{E_1X}. So the generic C(v) is optimal at both worlds among all regular X of level v. Every C_L member of level v is regular and undominated, hence tied with C(v). Fact 0 is not even needed.
- **Step 3.**
  - Prop lattice puts A and B in opposite halves.
  - Non-null P ⊆ A and Q ⊆ B with π(P) = π(Q) exist: take them off one carrier Z of the purely finitely additive part, where π = ρμ is non-atomic with ρ > 0 a.e. (S2.1).
  - X has level v, so C ⪯_1 X and C ⪯_2 X.
  - PL with F ∈ C_L gives X′ ∈ C_L.
  - X′ is incoherent: a middle band removed from an initial σ- (or τ-) set is not initial. The bounded-splice argument of §4.2 works equally well.
- **Step 4.**
  - Generic C(v), C(v′) are nested (step 3, applied with F = C(v′)) and are ordered by level (strict positivity), so the family is increasing.
  - For any F ∈ C_L of level v_F: π(Q_−(v_F)) ≥ sup v_n = v_F, by monotonicity alone, so no countable additivity is needed. Also Q_− ⊆ E_1F.
  - So E_1F ∖ Q_− is π-null, hence null.
  - Hence E_1F = Q_−(v_F), C_L is a chain, and (Nest) holds in the write-up's sense; Lemma N0 then applies.

**Corollary (PROVED, from S2.2).** In a two-world system satisfying every axiom in which *either* world has a nonzero leading charge, (Nest) holds. So all of §8.4(c) and §8.5(c) applies unconditionally, including LF, IS, MP, N1, N2 and Prop Q15. For example, if world 2 is additive, world 1 has no simple certificate and no fixed-source star certificate.

So the open two-world class "without a nonzero leading charge" no longer needs (Nest) as a hypothesis.

---

## 4. S2.0 and the write-up's tie remark

### 4.1 S2.0(a), (b)

**(a): CONFIRMED WITH REPAIR (wording).**
- The proof is for the two worlds of one edge, or for n = 2, with weights (1−t, t). There Bayes sets at t < t′ satisfy {r ≤ t} ⊆ {r < t′}: nested, and *strictly* only if {t < r < t′} is non-null.
- The table's "(any n) … at distinct weights strictly nested" is false read literally for interior weights when n ≥ 3. There nested pairs have codimension 2 (Lemma nested).
- Restate as: "on one edge (or n = 2), Bayes error sets at distinct weights are nested, for every tie-break."

**(b): CONFIRMED.**
- Every t₀-Bayes model at an interior t₀ is undominated, since a dominator would lower the weighted sum.
- Fact 0 and (C) then force each t₀-Bayes model to be coherent.
- Hence Z_{t₀} is a cone mod null, being a difference of coherent cones.
- A bounded (radial) split of Z_{t₀} is t₀-Bayes and not a cone. Contradiction.

### 4.2 S2.0(c): CONFIRMED WITH REPAIR

**Step 1 is correct.**
- Competitive on {i, j} means no X is strictly better at both worlds, so the profile is weakly Pareto-minimal in the attainable set.
- The attainable set is convex and compact by Lyapunov, so there is a supporting weight (1−s, s).
- By (a), a crossing forces one common s ∈ (0,1). (s = 0 or 1 gives P_i or P_j, which cross nothing.) The pair then differs only on Z_s, where ρ_j = κρ_i.

**Step 2 (same level) has a GAP.**
- The claim is that a Lyapunov half-splice for the vector measure (ρ_i, signed ρ_k) is "incoherent and tied". Tied: yes.
- Incoherent: not justified. Lyapunov produces *some* set with half of each coordinate, and it may be a cone, i.e. coherent.

**Step 3 (bathtub) is correct as written.**
- Each model is ψ_k-minimal among splits of Z at its level, and the bathtub form follows.
- A crossing forces A ∪ B ⊆ {f = λ}, and an equal-mass exchange there is tied at all three worlds.
- Incoherence is again asserted ("choose X incoherent"). It is easy here: see the repair.

**Repair: bounded splices.**
- Coherent models and P_i are cones mod null, so A = E_iF ∖ E_iC and B = E_iC ∖ E_iF are cones. Each non-null cone meets the unit ball W in a non-null set.
- Take non-null P ⊆ A ∩ W and Q ⊆ B ∩ W with ρ_iμ(P) = ρ_iμ(Q).
- Then P ∪ Q is non-null and bounded, hence not a cone. So C△(P∪Q) and F△(P∪Q) are not cones, i.e. they are incoherent.
- In the bathtub step, P, Q ⊆ {f = λ} also give ψ_k-equality. So steps 2 and 3 merge: at equal levels, both models are bathtub minimisers with the same λ, and A ∪ B ⊆ {f = λ} again.
- In fact the bathtub is not needed at all; see 4.3.

### 4.3 Proposition R-S2.A (new; PROVED here, one reader): edge nestedness from additive edge worlds and a complete third world

> **Prop R-S2.A.** Let n = 3, on M_U (any K′ ⊆ Δ°), with a ranking satisfying strict (G), (IB), (S) and (C). Let worlds i and j be additive with integral penalties (ψ_l(X) = ∫_{E_lX} ρ_l dμ, with ρ_l > 0 a.e. and integrable). Let C, F ∈ C_L both be competitive on {i, j}; for instance C = C_p and F = C_{p′} with p, p′ ∈ e_ij.
> (a) If world k is complete, C and F are nested at world i. Hence **(Nest_e) holds on e_ij**.
> (b) In general, if C and F cross, then:
>   - A ∪ B ⊆ Z_s for one s ∈ (0,1);
>   - for every non-null bounded P ⊆ A, Q ⊆ B with ρ_iμ(P) = ρ_iμ(Q), the model C and X := C△(P∪Q) are incomparable at world k, and so are F and X′ := F△(P∪Q).
> (c) If world k has a nonzero leading charge π_k, a crossing additionally needs:
>   - the countably additive density of π_k proportional to ρ_i on A ∪ B (a.e.);
>   - C world-k-correct a.e. on one of A, B and world-k-wrong a.e. on the other.

*Proof.*
1. By 4.2 step 1, a crossing gives one common s ∈ (0,1) with A ∪ B ⊆ Z_s, where ρ_j = κρ_i.
2. Take P and Q as in the repair above. Then:
   - ψ_i(X) − ψ_i(C) = ρ_iμ(P) − ρ_iμ(Q) = 0;
   - ψ_j(X) − ψ_j(C) = κ(ρ_iμ(Q) − ρ_iμ(P)) = 0.
   So X ~_i C and X ~_j C.
3. If C ⪯_k X: by PL, X′ ⪯_l F at all three worlds. F is undominated, so X′ ~ F everywhere, and X′ ∈ C_L by (C). But X′ is not a cone. Contradiction.
4. If X ⪯_k C:
   - strictly: X dominates C ∈ C_L;
   - with a tie: X ~ C everywhere, so X ∈ C_L by (C), but X is not a cone.
   Contradiction either way.
5. So C and X are incomparable at k. The F-side follows by PL. This is (b), and (a) follows since a complete world has no incomparable pairs.
6. For (c):
   - with P, Q off one carrier of π_k, (i) and (ii) turn π_k(E_kX) ≠ π_k(E_kC) into a strict comparison, which steps 3 and 4 exclude;
   - so ∫_{P∪Q} ε_C ρ^{π_k} dμ = 0 for all such balanced P, Q, where ε_C = ±1 according as C is k-correct or k-wrong;
   - varying P within A ∖ Z and Q within B ∖ Z shows that ε_C ρ^{π_k}/ρ_i equals a constant a on A and −a on B;
   - a ≠ 0, because ρ^{π_k} > 0 a.e. by S2.1. ∎

*Remarks.*
- The proof uses neither closed sections, nor generic levels, nor the bathtub, nor K′. Only competitiveness on the edge, (C), and PL enter.
- S2.0(c) (all three worlds additive) is the special case "world k additive", which is complete.
- The two-world analogue (both worlds additive, every axiom): C_L has no crossing pair, since the bounded exchange is tied at both worlds. This covers S2.0(b) in the form "crossings need a tie face, and a tie face kills (C)".

NUMERICS: `s2ref_py/fan_search.py` uses finite face models with exhaustive balanced exchanges.

| World k | Crossing pairs passing undominatedness at both models and "no all-world tie" |
|---|---|
| additive (complete) | 0 |
| lexicographic (complete) | 0 |
| unanimity of two weights (incomplete) | 50 of 3000 random trials; example printed |

In all 66 surviving pairs of a second run, the model is world-k-wrong on all of A or all of B (item 5 of S2.4, §5).

### 4.4 The write-up's remark (before Prop comonotone)

The remark says (Nest_e) "can fail at exceptional edge weights where a non-null tie set is split in crossing ways".

- **For edge selections of a system satisfying the axioms:** wrong, whenever:
  - all worlds are additive with integral penalties (S2.0(c), repaired);
  - the two edge worlds are additive and the third is complete (R-S2.A);
  - n = 2 and either world has a nonzero leading charge (S2.2; additive worlds with bounded-charge penalties included).
- **For the family of Bayes face models:** correct.
- **Scope:** for n = 3 the exclusion is proved only for integral (density) penalties at the edge worlds. With purely finitely additive charge penalties, Lyapunov and the Bayes-support step are not available. This scope restriction must accompany the correction.

Suggested replacement text:

> (Nest$_e$) holds for edge selections that are Bayes for additive edge systems with null ties. A non-null tie set of the edge worlds cannot be split in crossing ways by an edge selection of a system satisfying the axioms if the two edge worlds are additive with integral penalties and the third world is complete (in particular, if all worlds are additive), nor, in two worlds, if either world has a nonzero leading charge. A crossing tie-split would require the third world to be incomplete, with C and C△(P∪Q) incomparable there for every bounded balanced exchange. Whether this can happen is open.

---

## 5. S2.4 (three-world anatomy)

**Transfer.** S2.1 is stated for every n, and its steps 1–4 are edge statements. So:
- m is continuous on e_ij;
- generic edge-selected models are optimal at worlds i and j among edge test models of their level.

CONFIRMED.

**Item 1: CONFIRMED WITH REPAIR.**
- X = C△(P∪Q) must be an edge test model, so P must lie in R_ij. Q ⊆ E_iC ⊆ R_ij automatically.
- So either take F competitive on {i, j} (an edge model), or intersect P with R_ij. The note's "F ∈ C_L" is too loose.
- The hypothesis "X′ incoherent" is automatic for bounded P ∪ Q (4.2).
- With that, PL plus step 4 plus (C) give C ⋠_k X, as claimed.

**Items 2–3 ("fan"): CONFIRMED for additive edge worlds; GAP in general.**
- *Additive edge worlds* (integral penalties). R-S2.A(b) gives the fan: X is tied with C at i and j and incomparable with C at k. Fact 0 then gives a selected Y with Y ⪯ X everywhere. As argued in item 2, Y ~_{i,j} C (a strict improvement at i or j would beat C's (1−s, s)-Bayes value), and Y, C are incomparable at k. This is the fan: two non-tied C_L members tied at i, j. The note's restriction "in the cases built here" is the needed hypothesis.
- *In general* (worlds i, j not additive), what follows is only:
  - C ⪯_i X and C ⪯_j X (step 4);
  - C ⋠_k X (item 1);
  - a selected Y ⪯ X everywhere with Y ⋠_k C.
- Y may be strictly better than C at i or j, and strictly worse at k, without contradiction. Then C and Y are neither tied at i, j nor incomparable at k. So "Hence C_L contains, at level v, at least two non-tied coherent members that are tied at worlds i and j and incomparable at world k" is not derived. "At level v" is not derived either; (ii) gives only π(E_iY) ≤ v.
- If world k is complete, the general conclusion is: X ≺_k C, and C ≺_i X or C ≺_j X.

**Item 4: GAP (heuristic).**
- "A crossing on a continuum of levels needs fans at a continuum of levels in one tie face" conflates pairs at different faces: S2.0(a) puts each crossing pair in *its own* face Z_s.
- "A two-parameter family in C_L, selected at interior indices" is not derived. Nothing shows that the fan partner Y is not edge-selected.
- Read it as a heuristic description, not as PROVED.

**Item 5: CONFIRMED, strengthened.** The world-k leading charge is not needed.
- If C is world-k-correct on non-null parts of both A and B, take P, Q there (non-null, in R_ij, π(P) = π(Q)).
- Then C ≺_k X by strict (G) alone, and C ⪯_i X, C ⪯_j X by step 4.
- PL then gives X′ ⪯ F everywhere, strictly at k, so F is dominated. Incoherence is not even needed.

Corrected item 5 (PROVED): a crossing between a generic edge-selected C and an edge model F ∈ C_L requires C to be world-k-wrong a.e. on A or a.e. on B. NUMERICS: `fan_search.py`, 66 surviving pairs, 0 violations.

---

## 6. Remaining parts of the note

- **§5 (a)–(d).** These are failure reports.
  - (a) is S2.0(b).
  - (b) is a special case of S2.2.
  - (c), the half-vanishing leading charge, is excluded by S2.1 step 5. The intermediate "forced anatomy" (Z-path and so on) was derived before S2.1 and is moot. I did not re-check it, and it should not be cited.
  - (d), the exact test with R5, is a remark without a computation, and is labelled as such.
- **§7.** "Q2.N holds in general (two worlds)" is correctly labelled CONJECTURE. The remark that a real-valued "level" with (i), (ii) would suffice is accurate: S2.1 and S2.2 use nothing else.
- **§8 (write-up changes).** Agreed, with the repairs above.
  - B2(b) restated (§2.2).
  - PL's last sentence (§3.1).
  - S2.0(a) wording and S2.0(c) incoherence (§4.1–4.2).
  - The scope of the tie-remark correction (§4.4).
  - S2.4 items 2–5 (§5).
  - Add R-S2.A, the LX-class corollary (§2.5), and the S2.2 corollary that part (c) applies unconditionally in the leading-charge class (§3.4).

---

## 7. Exact established statements (after this report)

1. **Thm S2.1 (PROVED; two readers).**
   - *Hypotheses:* n ≥ 2; M_U with K′ ⊆ Δ°; strict (G), (IB) and (S); π a bounded charge ≥ 0 on U, vanishing on null sets, that is a leading charge of world i on M.
   - *Conclusion:* either π(M) = 0, or π(D) > 0 for every non-null D ⊆ M.
   - *In the second case:* the countably additive density of π is > 0 a.e. on M; π endorses every world-i comparison between subsets of M; and world i adds up (SP^reg_i).
   - *Proof uses:* edge indices at e_i only; closed sections at edge test models; competitiveness on edges; strict (G) at the two edge worlds; for n ≥ 3, linking.
2. **Thm E2 and Cor E2′ (n = 2): PROVED without (Nest).** **Thm Q36(a), (b): PROVED without (Nest_e).** **B2(b′) (§2.2): PROVED.**
3. **Cor Q37 (at the status of Thm M0closed(b); CHECKED where a complete world enters).**
   - *Hypothesis:* (H_U); every world is (CP-a), or has a leading charge nonzero on M, or is complete with (Nest_e) on both edges at e_i.
   - *Conclusion:* T₁ is not covered.
   - *Contrapositive:* as in §2.4.
4. **Lemma PL (PROVED, any n).**
   - *Hypotheses:* D ⊆ C△F, X = C△D, X′ = F△D.
   - *Conclusion:* C ⪯_k X ⟺ X′ ⪯_k F and F ⪯_k X′ ⟺ X ⪯_k C, at every world.
   - *If F ∈ C_L and C ⪯_k X at every world:* X′ ∈ C_L, and C ~ X at every world. If also C ∈ C_L, then X ∈ C_L.
5. **Thm S2.2 (PROVED).**
   - *Hypotheses:* n = 2; every axiom; some world has a nonzero leading charge on M.
   - *Conclusion:* {E_1C : C ∈ C_L} is a chain, each member determined a.e. by its π-level. Hence (Nest) holds and all nested two-world results apply.
6. **S2.0(a) (PROVED).** On one edge (or n = 2), additive Bayes error sets at distinct weights are nested, for every tie-break.
7. **S2.0(b) (PROVED).** n = 2: a purely additive system with all axioms has null tie sets at every interior weight.
8. **Prop R-S2.A (PROVED here; one reader), including S2.0(c).**
   - *Hypotheses:* n = 3; strict (G), (IB), (S) and (C); worlds i, j additive with integral penalties; C, F ∈ C_L competitive on {i, j}.
   - *If world k is complete:* (Nest_e) holds on e_ij.
   - *Otherwise:* crossings need incomparability at k for every bounded balanced exchange, and, if world k has a nonzero leading charge, also the proportionality and sign conditions of R-S2.A(c).
9. **S2.4 (PROVED parts).**
   - *Transfer:* m is continuous on e_ij, and generic edge-selected models are optimal at worlds i and j among edge test models of their level.
   - *Item 1:* P ⊆ R_ij; X′ is automatically incoherent for bounded P ∪ Q.
   - *Item 5:* strengthened, under strict (G) alone.
   - *Items 2–3:* hold for additive (integral) edge worlds.
   - *Item 4:* not proved.
10. **(R4) status.**
    - *Two worlds:* Conj Q2.N is PROVED when some world has a nonzero leading charge (including additive worlds of either kind, and lexicographic worlds with a charge first level). It is open when neither world has one: the open SP^reg class.
    - *Edges in three worlds:* (Nest_e) is PROVED in the cases of item 8. It is open otherwise. It remains load-bearing only for complete worlds (Q36(c) via Prop Q35(5)) and for general acceptance cones; for leading-charge worlds it is no longer needed (S2.1).

---

## 8. Files (`s2ref_py/`)

- `pl_orders.py`, `.out`: PL as an equivalence of comparisons. Additive, lexicographic (zero levels allowed) and incomplete unanimity worlds; n ∈ {2,3,4}; 20 000 trials; 0 violations. The control with D ⊄ C△F fails 13 607 times. (NUMERICS)
- `fan_search.py`, `.out`: finite tie faces with exhaustive balanced exchanges.
  - Crossing pairs that are undominated at both models with no all-world tie: none when world k is additive or lexicographic (complete), consistent with R-S2.A(a); 50 when world k is an incomplete unanimity order (example printed).
  - Item 5 holds in all 66 surviving pairs of the second run. (NUMERICS)
- The `s2py/` scripts (`additive_tie`, `face_np`, `pl_identity`) were re-run and their outputs reproduced. They check set identities and finite tie faces only, and they bear on S2.0 and PL, not on S2.1 or S2.2.
