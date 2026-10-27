# DD3. Referee report on AUDIT_CC_seeds.md / AUDIT_CC_plan.md §3, CC1_notes.md and CC2_notes.md

17 Oct 2026, round 32. This is an adversarial, independent reading. Every proof listed in the brief was re-derived line by
line, not read for plausibility. Labels for my own claims:
- **PROVED**: a full argument is given here (one reader: me);
- **CHECKED**: exact finite computation;
- **NUMERICS**: sampled; nothing rests on it.

Scripts are in `dd3ref_py/` (run `python3 -I <name>.py` inside it; outputs in `*.out`).

I also reran CC1's and CC2's scripts with `python3 -I`. `cc1py/seed_exact.py`, `cc1py/closure_check.py`,
`cc2py/geometry.py` and `cc2py/seed.py` all reproduce their stored outputs byte for byte.

---

## 0. Verdicts

| # | Item | Verdict |
|---|---|---|
| A1 | Audit: bundle matching of the seven regions | **CORRECT.** One unstated point is needed and holds: the cells lie in U and U ∩ −U = ∅, so the problems in the seven regions are pairwise distinct (§1.1) |
| A2 | Audit: disjoint-bundle seeds coexist; within a bundle two seeds never compose | **CORRECT** (PROVED; CHECKED cellwise, `bundle_relation.py`) |
| A3 | Audit: world-1 preorder with strict (G) and (IB) | **CORRECT.** The (IB) proof covers transports of composites. That is exactly what CC1's own proof of 1.1(b) lacks (see C2) |
| A4 | Audit: graph closed under convergence in measure | **CORRECT** |
| A5 | Audit: four-comparison certificate on every positive-measure set of bundles | **CORRECT** |
| A6 | Audit: the four seed bases, T1 included, are undominated with guidance orders at worlds 2 and 3 | **CORRECT** (CHECKED: incoming-seed blocking and the Pareto claim) |
| A7 | Audit: three-world system with (G), (IB), (LA), (C), (LF), lacking only (S) | **CORRECT** |
| A8 | Audit §3 (vetoes) and §4 (jumps, finite-image selections) | **CORRECT** |
| A9 | Plan §3: coupling warning, including the rearrangement contradiction | **CORRECT** (PROVED; CHECKED on a four-part model, `coupling.py`). One sharpening: only one direction of each rearrangement is needed |
| C1 | CC1 seed data: seven rational patterns, certificate, world-2/3 table | **CORRECT** (independently recomputed, CHECKED) |
| C1′ | CC1 §0/§1: "cells away from the coordinate planes" | **GAP (cosmetic), confirmed.** The closures of 5 of the 7 cells touch a coordinate plane; R_∅ touches all three (CHECKED by LP). The audit's shrinking repair fixes this, and nothing uses the claim |
| C2 | CC1 Thm 1.1(b): every composition contains ≤ 1 seed record; no strict reversal | **The statement is CORRECT. The proof has a GAP (fixable):** the chain argument does not reach (IB)-transports of composites. Explicit witness and one-paragraph fix in §2.2 |
| C3 | CC1 Lemma 2.0, Lemmas 2.1–2.3, invariant I, Thm 2.4 | **CORRECT.** Thm 2.4 is nearly tautological, as advertised |
| C4 | CC1 Thm 3.1 (a), (b) | **CORRECT** |
| C5 | CC1 Lemma 3.3, Lemma 3.4, Lemma 3.4′, Cor 3.5 | **CORRECT.** I re-derived the normal-cone computations |
| C6 | CC1 Thm 4.1, Lemma 4.2, applicability of the imported chain | **CORRECT** at the status of D1, M3.7(d), M3.8, Q4.1 (R1 each) and M3.9 = BB2 Thm 6.1. The status of BB2 Thm 6.1 can now be upgraded: CC3 found it CORRECT once AUDIT_BB's Lemma 2.0 is inserted |
| D1 | CC2 core: Thm 2.1, Props 2.2, 2.3 | **CORRECT** (re-derived; CHECKED independently, `cc2_core.py`). Cosmetic: in 2.3(b), "≤ 0" should be "< 0" |
| D2 | CC2 five-comparison corner seed (Prop 3.2), Lemmas 3.1, 3.3, 3.4 | **CORRECT** |
| D3 | CC2 valued worlds (Def 4.0), Thm 4.1, Lemma 4.3 | **CORRECT.** GAP (wording): the separable form (4.2) is forced only for shadow prices with \|θ\| below the richness bound. Lemma 4.3(c) gives exactly that, and no more |
| D4 | CC2 Lemmas 5.1–5.4 | **CORRECT.** Lemma 5.4's proof is a sketch, but it is sound |
| D5 | CC2 Lemma 5.5 | **CORRECT after a fix.** **GAP (fixable):** Step 5's multiplicative bound a₃ ≤ τ(1+ε₁)\|a₁\| does not follow. The derivable bound is additive, a₃ ≤ τ\|a₁\| + K′\|a\|², and Step 6 goes through with it unchanged (§3.4) |
| D6 | CC2 Thm 5.6 | (b) **CORRECT** (given D5's fix). (a) **GAP:** it holds only for **coherent** C, because Lemma 5.2 assumes C = D_K. The sentence after the theorem ("the only models competitive on Ω … are core Bayes models") overstates it: (b) carries a visibility hypothesis |
| D7 | CC2 Cor 5.7 | **CORRECT.** It is also **stronger than stated**: "middle arc" can be replaced by any point of ∂D_{T1} off the coordinate planes, and the facet-matching step is superfluous (§3.6) |
| D8 | CC2 §6, routes (L1)–(L5) | **GAP (fixable).** Read as the negations of 5.6/5.7's hypotheses, the list is complete up to two omissions: (i) W essentially dense near ∂D_{T1} without containing a neighbourhood; (ii) domains without chart infinity. (L1) is justified only by the strengthened 5.7 (§3.7) |

**No item is WRONG.** The two substantive fixes are C2 (record-class argument) and D5 (additive error). Neither touches a
mechanism.

---

## 1. The audit's synchronized seeds

### 1.1 Bundle matching (A1): CORRECT

The R_S are positive-measure subsets of small bounded neighbourhoods of the CC1 centres, all of equal Gaussian measure
m. The maps f_S: (0,1) → R_S are isomorphisms of atomless standard measure spaces with μ(f_S(A)) = m|A|.

One point is used but not stated: the seven regions must be disjoint **as sets of problems**, that is,
R_S ∩ −R_T = ∅. This is not automatic from the sign patterns. For example, −R_{14} has the sign pattern (−,+,−) of
R_{23}. It does hold, because every cell lies in U = D_{K′} and U ∩ −U = ∅.

The coupling is arbitrary, as the audit says. Nothing below needs an interpretation of it.

### 1.2 The finite relation (B) and Lemma 1 (A2, A3): CORRECT (PROVED; CHECKED)

Work on one bundle with world-1 ranks 0–3 per cell. The designated increment is j_S = 1 on the h₁ > 0 cells (12, 13,
14, 34) and j_S = 2 on the others.

Cellwise, d ≥ g_k means:
- on a cell S ∋ k: an upward crossing r_X < j_S ≤ r_Y;
- on a cell S ∌ k: a guidance move, or the single down-step j_S → j_S − 1.

So the bundle relation is the union R₀⁷ ∪ ⋃_k Π_S R_{k,S} of product relations. A composition of product relations is
the product of the cellwise compositions. Transitivity therefore reduces to three cellwise facts:
- R₀∘R₀ ⊆ R₀;
- R₀∘R_{k,S} ⊆ R_{k,S} and R_{k,S}∘R₀ ⊆ R_{k,S};
- for every k, l (k = l included), some cell S has R_{k,S}∘R_{l,S} = ∅. This is the cell {k,l}, where Y would need
  rank both ≥ j and < j.

All three are CHECKED (`bundle_relation.py`; a sampled 7-cell cross-check is NUMERICS, with 0 failures).

**Strict (G).** On every P_k cell, R_{k,S} forces a strict up-move. So no nonpositive, nonzero bundle record satisfies
(B).

**(IB).** The test depends on the record alone. So it holds for every accepted comparison, composites included.

**The measurable world** (a.e. t, with k allowed to depend on t, and guidance outside the seven regions). This inherits
transitivity fibre by fibre. A strict improvement on positive measure violates either (B) on a positive-measure set of
t, or the outside clause.

### 1.3 Lemma 2, closed graph (A4): CORRECT

The steps are:
- Pass to an a.e.-convergent subsequence. The seven measure-preserving maps carry null sets to null sets.
- Advice is four-valued, so it is eventually equal to its limit on every coordinate of a.e. bundle.
- (B) is a finite condition at each t, and the outside clause is pointwise.

The countable union of exceptional null sets is null.

### 1.4 Lemma 3, certificates at every scale (A5): CORRECT

On t ∈ A, the record of B_k → X_k^A is exactly g_k (CHECKED); elsewhere it is 0. The sum of the four records is −4 at
the designated increment of f_∅(A), and 0 elsewhere. So no strictly positive finitely additive ladder weight endorses
all four comparisons.

Also μ(X_k^A △ B_k) = 7m|A|.

The relation is not contained in any finite-seed envelope. So CC1 Thm 4.1 does not apply to it. This is CC1 §5,
escape 1.

### 1.5 Lemma 4, undominated bases (A6, A7): CORRECT (CHECKED)

Fix k and l. Take the cell {k,l} (any S ∋ k if k = l). On that cell B_k is world-1-correct, so its rank lies below j_S.
Hence d(Y, B_k; t) cannot cross j_S upwards, and every incoming comparison at world 1 is guidance. This is CHECKED for
all 16 pairs (k, l) from CC1's exact patterns.

At mixed sign patterns, +, 0 and − have pairwise incomparable three-world rank vectors. Ranks at any single world
separate all four advices (CHECKED). So Y ⪯_i B_k at all three worlds forces Y = B_k a.e.

The remaining properties:
- **(LA):** B_k ∈ C_L.
- **(C):** world 2 is antisymmetric mod null.
- **(LF):** this is a property of the full domain.

The system lacks only (S), as the audit says.

**Caution (not an error).** The seeds help competitiveness only at a C_p which, on a positive-measure set of bundles,
is world-1-correct on all three P_l cells of some l. Lyapunov-shrunk generic competitors still meet only the guidance
part of world 1. So the construction removes CC1's *finite-margin* obstacle. It does not yet show that Thm 3.1's
mechanism is defeated. That is the (S) question.

### 1.6 Audit §§3–4 (A8): CORRECT

**The veto argument** is correct as stated.

**Jumps.** C_{p_n} = A and closed sections give C_p ⪯_i A at every i. Undominatedness of A then forces ties at every
world.

**Finite image.** The tie-class preimages are finitely many, disjoint, closed and cover Δ. Connectedness leaves one
class. But C_{e_1} = P_1 ≺_1 P_2 = C_{e_2} by strict (G), a contradiction. This is CORRECT; it needs only (S) and (G).

### 1.7 The coupling warning (AUDIT_CC_plan §3) (A9): CORRECT

**Construction.** Let M carry B_k's pattern on part k of the bundles, for k = 1, …, 4. Let M′ apply seed k on part k.

**Step 1: M ⪯₁ M′ follows from the retained seeds alone.**
- B_k ⪯₁ X_k^{A_k} is transported by (IB) to base M_{k−1}, which agrees with B_k on R(A_k) because the parts are
  disjoint.
- Four such steps compose to M ⪯₁ M′.
- CHECKED: the four single-part steps are each accepted, and so is the direct comparison.

**Step 2: the advice distributions.**
- In each pair cell, the four parts' ranks form the same multiset before and after.
- In R_∅, every part strictly improves.
- CHECKED.

**Step 3: rearranging back.** A within-cell permutation of parts returns each pair cell to M's advice. Call the result
M″. Then rec(M, M″) is ≤ 0 and nonzero, and lives only in R_∅: a pure guidance improvement. CHECKED.

So M′ ⪯₁ M″ cannot be accepted, or transitivity contradicts strict (G).

**Sharpening.** The contradiction needs only the **one direction** M′ ⪯₁ M″ of the rearrangements. Weak acceptance
of rearrangements in all six pair cells is already fatal; full indifference is not needed.

**Why it bites additive pricing.** It cannot be a world-1 relation endorsed by any density that is constant on each
region, because such a density prices rearrangements at zero. This agrees with the certificate.

The design lesson in the plan (exchange whole bundle patterns; never rearrange components independently) is a correct
reading. It is a heuristic, not a theorem.

---

## 2. CC1

### 2.1 The seed (C1, C1′)

**Independent recomputation** (`cc1_seed_indep.py`, CHECKED). This was written without importing cc1py. It confirms:
- every vertex set sums to 1 and is positive;
- the seven acceptance patterns, with world-1 correctness equal to the cell index;
- strictness at the centres of every defining inequality, with my own witness choice;
- the bound |h_i| ≥ 0.15·max|h|;
- the record sum (0 on the six pair cells, −4 on R_∅);
- the world-2/3 improvement table exactly as printed.

**The closures of the cells as defined do reach the coordinate planes.** The LP minimum of |h_i|/‖h‖₁ is 0:
- for i = 3 on R_{12};
- for i = 2 on R_{13};
- for i = 1 on R_{14} and on R_{34};
- for all three coordinates on R_∅ (for instance, (0,1,1) is in its closure).

So §0's "away from the coordinate planes" is false for the cones themselves. It is harmless: the planes are null, the
cells are open, and no proof uses a uniform distance. Adopt the audit's repair (bounded neighbourhoods of the centres).

Cosmetic: the comment in `closure_check.py` says allowing shifted rank 3 on h₁ < 0 cells "can only remove paths". It
adds spurious states, which makes the check conservative.

### 2.2 Theorem 1.1(b) (C2): statement CORRECT, proof GAP (fixable)

The chain argument is correct for compositions of members of 𝒮 (guidance records, plus seed records and their
(IB)-transports). But the world-1 relation generated by 𝒮 must be closed under (IB) **again**, after composition.
**Transports of composites are not composites of members of 𝒮.**

**Witness (PROVED).**
1. Compose B_k → X_k (the seed) with a guidance step that raises the ranks on a non-null D ⊆ N_k back to B_k's. The
   composite record is g_k off D and 0 on D.
2. Transport it by (IB), replacing the common advice on D by × (rank 3).
3. Any 𝒮-chain realising the transported pair would need B_k's advice on all of R, including D. Guidance cannot lower
   rank 3 to B_k's rank there.

So this accepted comparison is outside the class that the proof analyses.

The same issue arises in the pure record calculus: the set of records of 𝒮-chains is not closed under record
composition.

**Fix (PROVED).** Use the record class
𝒞 := {r ≥ 0} ∪ ⋃_k {r: on R, d ≥ g_k in the sense of (B); off R, r ≥ 0}.
This is the audit's (B) with the whole of R as a single bundle.
- 𝒞 contains the generators.
- It is closed under composition: Lemma 1, with the cell {k,l} conflict.
- It is closed under (IB), because it is defined by records.
- It contains no strict reversal.

So the generated relation lies inside 𝒞. Theorem 1.1(b)'s conclusion and 1.1(c)'s rigidity (which in fact uses exactly
𝒞) then follow. Replace the chain proof, or append this paragraph. The exhaustive cell check remains a valid sanity
check of the chain statement.

### 2.3 Invariant I, Lemmas 2.0–2.3, Thm 2.4 (C3): CORRECT

**Lemma 2.0.** With the stated costs, Λ₁X_k − Λ₁B_k = g_k exactly. Let φ_{kl} = 1_{R_{kl}} + η′. The (P) estimate
2μ(R_{kl}) − 2η′μ(R) > (1+2η)(μ(R_{kl}) + η′μ(H)) holds for small η, η′. For k = l, use φ_{kj}.

**Lemma 2.1.**
- In the (g+𝒦) + (g′+𝒦) case, the (P)-witness contradicts |record| ≤ ω pointwise. So that case is vacuous.
- Strict (G) uses φ⁺ > 0 a.e. and the (E)-witness.

**Lemma 2.3.**
- q ↦ Λ_iC_q is L¹-continuous.
- Each set 𝒦_i and each g + 𝒦_i is L¹-closed on bounded records, because Ψ_i is bounded.
- There are finitely many seeds.

**Thm 2.4.**
- (a) (Prot) gives undominatedness and no global ties. thm:kkm then gives C_L = {C_q} and (C).
- (b) and (c) are definitional.

The theorem is close to tautological, as the note itself says. Nothing is hidden in it.

### 2.4 Theorem 3.1 (C4): CORRECT

**(a).**
- Lyapunov gives convexity and compactness of Z⁺: finitely many bounded integrands, finitely many advices, a
  nonatomic μ.
- 0 ∈ Z ∩ cl N, so the separating constant is 0.
- Localising to arbitrary D yields (WB) pointwise.
- Shrinking t·z⁺ ∈ Z⁺ defeats the cone at every world in J through the tuple member φ_i. It defeats every one of the
  finitely many seeds through their fixed (E)-witnesses, once t is small.

**(b).** Integrating (WB) along a_X gives Σ w_i(negative) ≥ 0 with w ≠ 0, a contradiction.

### 2.5 Lemmas 3.3, 3.4, 3.4′ and Cor 3.5 (C5): CORRECT

**Lemma 3.3.** At a.e. h the advice is eventually constant, so (WB) passes to the limit.

**Lemma 3.4.** I re-derived each step.
- **O(q) is nonempty.** Strictly separate q* from the compact convex set W(q). Since w − q* ∈ T, projecting the
  normal to T loses nothing.
- **Open graph.** This follows from upper hemicontinuity and compactness of W(q). Browder's theorem then gives a
  continuous selection.
- **Normal cones at a Brouwer fixed point.**
  - Interior: N_Δ(q) ∩ T = {0}.
  - Relative interior of the face q₃ = 0: −v = a𝟙 − b e₃ with 3a = b, so v = b(e₃ − u) with b > 0. Then
    v·(w₀ − q*) = −b q₃* < 0, using u·(w₀ − q*) = 0.
  - Vertex e₁: v = b₂(e₂ − u) + b₃(e₃ − u), and w₀ = e₁ gives −b₂q₂* − b₃q₃* < 0.

  All as claimed.

**Lemma 3.4′.** The face restriction keeps closed graph, convex values and nonemptiness, since Δ_{supp q} ⊆ F.

**Cor 3.5.**
- **Null ties.** If v_a − v_b ∥ 𝟙, there is no tie at all; otherwise the tie set is a line. Either way Fubini applies.
- **The tie clause.** The cases g+𝒦 / 𝒦 and g+𝒦 / g′+𝒦 are excluded by (E) and (P). So f_i ∈ 𝒦_i ∩ −𝒦_i, which
  gives equal ℓ^τ-loss. Hence T1 is also a minimiser, and minimisation is pointwise.

### 2.6 Theorem 4.1 and Lemma 4.2 (C6): CORRECT at the imports' status

**Lemma 4.2.**
- h* = (1,1,−t*) has v₃·h* = 0, while v₁·h* > 0 and v₂·h* > 0.
- For t slightly larger than t*, D_{T1} is silent. Indeed v₁·(−h) = c₀t − 2c₀ − ε < 0, and the gamble lies in
  U ∖ cl D_{T1}.
- "Accept h" is good at worlds 1 and 2, so (WB) fails there.
- At a vertex weight, D_{T1} would have to equal P₁.

**The chain.** It needs a field ℓ^τ with the following properties:
- non-degenerate (φ⁺ > 0 and λ strictly guiding, so no ladder-blind set);
- bounded, hence integral;
- (γ) and (γ₀) at **every** t (Cor 3.5, from Lemma 3.4′; Q4.1 needs the boundary weights);
- E null;
- D_{T1} Bayes at an interior w (Lemma 4.2).

I checked the hypotheses of D1, M3 §5 (standing data), M3.8, BB2 (H1)–(H4) and Q4.1. Each is met; none mentions
endorsers, fixed points or (S) of an additive ranking. CHECKED by reading.

**Status line.** CC1 lists M3.9 as "one reading, unrefereed". CC3 has since confirmed BB2 Thm 6.1 once AUDIT_BB's
Lemma 2.0 is inserted. Update the status accordingly.

---

## 3. CC2

### 3.1 The core (D1): CORRECT

**Thm 2.1.**
- The q-costs of +, 0 and − are λ₂q·h⁻, λ₁q·|h| and λ₂q·h⁺.
- So + beats 0 iff q·h⁺ − κq·h⁻ > 0, which is min_{t∈{1,κ}³}(q⊙t)·h > 0.
- κ ≥ 1 then also gives + over −.
- The cone over the cube [1,κ]³ is {s: s_i ≤ κs_j}. Diagonal scaling by q gives R(q) in both forms.

Independent checks (`cc2_core.py`), all CHECKED:
- 19 661 exact tests with a fresh sampler, including boundary q and κ = 1: 0 mismatches.
- For 200 random interior (q, κ), the vertex enumeration of the ratio polytope returns exactly the six normalised q⊙t.

Uniqueness gives undominatedness and (C). Continuity of q ↦ B_q in measure, including at the boundary (ties are null at
every q), gives closed sections.

**Prop 2.2.** max_{T1} m_i/m_j = (c₀+ε)/c₀ = κ(ε). On an edge, both sets are the same segment.

**Prop 2.3.**
- The six vertices are confirmed.
- r₁₂ lies on F₁ ∩ F₂, w₂₁ on F₁ ∩ {w₃·h = 0}, and w′₁₂ on F₂ ∩ {w₃·h = 0}; r₁₂ is strictly inside (CHECKED).
- The chart triangle is correct: κx + y = 1 meets x + y = 1/κ at (1/κ, 0). The apex (1/(κ+1), 1/(κ+1)) satisfies
  x + y ≥ 1/κ iff κ ≥ 1.
- Cosmetic: D_{T1} ∖ cl D_H requires w₃·h < 0, not ≤ 0. The difference is null.
- Cosmetic: geometry.py (D) checks an identity from an older "Theorem CC2.R". It is not the inequality
  u·a ≤ a₃(1−κ(x+y))/3 cited in §0. That inequality is one line: u·a = (a₃ − |a₁| − |a₂|)/3 together with the two edge
  bounds.

### 3.2 The corner seed and Lemmas 3.1–3.4 (D2): CORRECT

**Prop 3.2** is reproduced exactly. Chord separation works because the arc bulges away from the origin. The cell radius
5·10⁻⁷ is below margin/√2, which is enough.

**Lemma 3.1.** With a fixed base, each ladder coordinate has a fixed sign, so a certificate forces every δ_k ≤ 0, hence
δ_k = 0.

**Lemma 3.3.** This is a record-level argument on vectors. It does not have C2's chain issue.

**Lemma 3.4.** On Q₃ the world-1 and world-3 ladder changes are opposite. Integrating the certificate against ρ gives
the contradiction.

### 3.3 Valued worlds, Thm 4.1, Lemma 4.3 (D3): CORRECT

**Def 4.0.** The converse (V = 0 on A, −∞ off it) satisfies (V1) by transitivity.

**Thm 4.1.**
- If X ⪯_k C_p at every k, (V1) gives V_k(rec(C_p,X)) ≤ −V_k(rec(X,C_p)) ≤ 0, which contradicts (B).
- Closed sections follow from (U).
- The rest is thm:kkm.

**Lemma 4.3.**
- **(b):** the composite is the off-W record o ∪ o′.
- **(c):** the "symmetric" reverse inequality needs one more line. If w∘o′ ∈ A with ℓ(o′) = t′ < −m, richness gives an
  o in Z with ℓ(o) = −m ≥ t′, hence θ(w|Z) ≤ −m, contradicting |θ(w|Z)| < m. With that line it is CORRECT.
- **(d):** correct.

**Wording.** "(4.2) is forced" holds only for records whose off-W part lies in a rich region and whose shadow price is
below the richness bound. Large shadow prices may depend on the exchange region. Say so.

### 3.4 Lemma 5.5 (D5): GAP (fixable)

The E-step gives q^E₃|b₃| ≤ q^E₁b₁ + K_E|b|². Combined with b ≤ −a (Lemma 4.3(b)), this yields a₃ ≤ τ|a₁| + K′|b|².

**The multiplicative form does not follow.** Take a₁ = 0, so b₁ = 0. The inequalities then allow
0 < a₃ ≤ |b₃| ≤ K_E b₂²/q^E₃ with b₂ ≤ |a₂|. The derivable conclusion is a₃ = O(|a|²), not a₃ ≤ 0.

**Fix (PROVED).**
1. From the E-step, |b₃| ≲ b₁ + |b|². Hence |b| ≲ |a₁| + |a₂| + |b|², so |b| ≤ C|a| for small |b|.
2. So a₃ ≤ τ|a₁| + K′|a|², and likewise a₃ ≤ σ|a₂| + K′|a|².
3. Insert these into (5.1): [κ(q₁c_E + q₂c_F) − q₃]·a₃ ≤ K″|a|².
4. Step 6 then runs verbatim: |a| ≤ 2C_q a₃, so a₃ = 0 for small B.

The order of choices is unaffected: K′ and K″ depend only on E, F and η, which are fixed before B.

The other cases (0→+, 0→−, −→0) are the same computation.
- The reduction from + vs − to + vs 0 uses discrete convexity, λ₂ ≥ 2λ₁ ⟺ κ ≥ 1. This is correct.
- × never occurs in a model competitive on Ω, by strict (G). That case is unlisted, but it is trivial.

### 3.5 Theorem 5.6 (D6)

**(a)** cites Lemma 5.2, which assumes C = D_K. For an incoherent C whose off-W weight lies on ∂Δ, nothing is proved.
Lemma 5.5 needs q interior.
- Fix: restrict (a) to coherent C. This is all that 5.7 uses, and all that C_L needs.
- Alternatively, leave the incoherent boundary case open.

**(b)** is CORRECT given §3.4.
- g and g′ are linear and injective on each sign class, so an open piece of the boundary plane gives an open cone of
  values in q^⊥.
- At density points of the disagreement set, the core is strictly better (ties are null).

**Wording.** "So the only models competitive on Ω … are core Bayes models" omits (b)'s hypothesis. That hypothesis is
not automatic. In every sign class, B_q's accept/silent and silent/− boundaries are **chart-bounded** segments. For
example, on Q₃⁺ they are κ(q₁x + q₂y) = q₃ and q₁x + q₂y = κq₃. So a chart-bounded W can cover all of them. §0 item 4
states the result correctly ("somewhere visible off W").

**Lemma 5.4** is sound. The q-component of every record out of a q-optimal C is ≥ 0. The shells give first-order
⊥-parts with second-order q-parts. Convexity and the lifted point fill the paraboloid. The write-up should spell out how
the O(η) residual of the "opposite shells" point is absorbed, using the disc.

### 3.6 Corollary 5.7 (D7): CORRECT, and stronger than stated

The proof steps are sound:
- **Off-W weight:** Lemma 5.1 holds for every κ.
- **κ ≤ 1:** silence is never strictly optimal, since λ₂min(a,b) ≤ λ₂(a+b)/2 ≤ λ₁(a+b).
- **Boundary q:** Lemma 5.2 applies, since T1 is coherent.
- **Rigidity:** Thm 5.6(b) applies.
- **Contradiction:** for κ > 1 and q interior, R_κ(q) is a hexagon.

**Strengthening (PROVED).** Let G be any open set, off W mod null, that meets ∂D_{T1} ∖ 0 at a point off the
coordinate planes. Then T1 = B_q a.e. on G, and the boundaries of the two open cones coincide inside G. So B_q's
accept/silent boundary meets G in a sign class off the coordinate planes, which is exactly the hypothesis of
Thm 5.6(b).
- The facet-matching step, and with it the restriction to middle arcs, is therefore superfluous.
- Demonstration (CHECKED by sampling with exact arithmetic, `cc2_core.py` (S)): at a side-arc point of F₃, for three
  core values κ, an interior q matches T1 locally, with 0/3000 disagreements. Side arcs are not protected by a lack of
  local matching.

### 3.7 The §6 list (D8): GAP (fixable)

Read as the negations of the hypotheses of 5.6/5.7, the routes line up as follows:

| Route | Negates |
|---|---|
| (L2) | (H3) |
| (L3) | (H4) |
| (L4) | chart-boundedness |
| (L5) | (H1) |
| (L1) | the visibility hypothesis |

Two omissions and one mismatch:
1. **The negation of visibility is "essential density", not "contains a neighbourhood".** The negation of "W^c
   contains (mod null) an open set meeting ∂D_{T1}" is "W meets every open set near ∂D_{T1} in positive measure". A
   thin dense W, with W^c non-null near every boundary point but containing no open set, is not covered by (L1).
   - I expect Lemma 5.4 to extend to measurable Z, using density points of W^c along Σ. Then this route closes too.
     This is not proved; list it as open, or prove the extension.
2. **Domain.** Lemma 5.2 needs gambles at chart infinity, so §5 is a full-domain theorem. On M_U, or any domain without
   chart infinity, nothing is excluded. That is a route in its own right, distinct from (L4).
3. **(L1) and 5.7 as written.** As written, 5.7 excludes only W missing a piece of a *middle* arc. So (L1)'s
   "essentially all of ∂D_{T1}" is justified only by the strengthened corollary of §3.6. Adopt the strengthening; (L1)
   then becomes exact, up to item 1.

(L3)'s M_U clause depends on S21, as CC2 says. The two-veto sketch is labelled unproved, correctly.

---

## 4. Requested changes

1. **CC1 Thm 1.1(b):** replace the chain proof by the record class 𝒞 of §2.2, or append it.
2. **CC1 §0 and §1.1:** delete "away from the coordinate planes" for the cones, or adopt the audit's bounded
   neighbourhoods.
3. **CC1 §4 import list:** upgrade M3.9 to "BB2 Thm 6.1, confirmed with AUDIT_BB Lemma 2.0 (CC3)".
4. **CC2 Lemma 5.5, Step 5:** use the additive bound of §3.4.
5. **CC2 Thm 5.6:**
   - (a): restrict to coherent C;
   - delete the sentence "the only models … are core Bayes models", or add (b)'s hypothesis to it.
6. **CC2 Cor 5.7:** state it for any point of ∂D_{T1} off the coordinate planes, and drop the matching step.
7. **CC2 §6:**
   - add the thin-dense-W route and the domain route;
   - rephrase (L1) as essential density.
8. **CC2 Lemma 4.3:**
   - add the missing line in (c);
   - qualify "forced".
9. **AUDIT_CC_seeds §2:** add the line U ∩ −U = ∅ (problem-disjointness of the regions).
10. **Plan §3:** note that one direction of the rearrangements already suffices.
11. **Cosmetic:**
    - CC2 Prop 2.3(b): "< 0";
    - geometry.py (D) docstring;
    - closure_check.py comment.

## 5. Files (`dd3ref_py/`)

- `cc1_seed_indep.py` → `.out`: independent exact recomputation of CC1's seed, and the LP showing that the cell
  closures touch the coordinate planes.
- `bundle_relation.py` → `.out`: cellwise product-relation proof of transitivity, strict (G), the bundle certificate,
  Lemma 4's incoming-seed blocking, the Pareto claim, and the sampled 7-cell transitivity cross-check.
- `coupling.py` → `.out`: the four-part rearrangement contradiction.
- `cc2_core.py` → `.out`: Thm 2.1 with a fresh sampler, ratio-polytope vertices, the Γ₃ generators and hexagon, and the
  side-arc matching behind the 5.7 strengthening.
