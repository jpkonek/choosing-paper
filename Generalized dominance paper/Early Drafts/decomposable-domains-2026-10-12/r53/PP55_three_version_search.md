# PP55. The kink module in three versions: exact finite search, and what it can and cannot see

23 October 2026. Task PP55 of Brief 53. One author; not refereed. It includes both of the coordinator's mid-task requests: ties exactly in the PP51 gap (with the PP59 ledger), and a section run.

**Labels.**
- PROVED: a complete argument is given here.
- CHECKED: an exact computation in `r9/PP55_py/`. SAT solutions are verified by an independent audit over the whole universe; field witnesses are verified in Fractions.
- NUMERICS: none is used for any claim. The LP and random search in `v3core55.py` only propose witnesses, which are then checked exactly.
- CONJECTURE / OPEN: as stated.

**Bottom line.**
- On every finite measurable instance, versions V1 and V2 are satisfiable, and V3 is not.
- So, in the audit's decision table, the kink is a **pricing (gate-architecture) obstruction**. Finite cells cannot even in principle show more (Prop F).
- Ties are not the lever. The PP51 tie gap closes inside the gate architecture (Theorem 5.1′). The only way a tied gate escapes the field-level certificate is by producing an exposure that direct (C) forbids (under (R0)), or by losing T's defence (under (R)).

---

## 0. Verdict

| Run | Level 0 | Level 1 | Level 2 | Every finite level | Label |
|---|---|---|---|---|---|
| V1: axioms, ties allowed | SAT | SAT | SAT | SAT (Prop F) | CHECKED; PROVED |
| V2: V1, no single-world ties | SAT | SAT | SAT | SAT (Prop F) | CHECKED; PROVED |
| V2 + realiser gating (coherent realiser, or selected realiser) | SAT | SAT | SAT | SAT (Prop F′) | CHECKED; PROVED |
| V3: V2 + own-Bayes fields, CG2, triangle test (PP51) | UNSAT | UNSAT | UNSAT | UNSAT | PROVED (Thm 5.1, mechanically checked core) |
| V3 with ties in the certificate cells (PP51's gap) | UNSAT | UNSAT | UNSAT | UNSAT | PROVED (Thm 5.1′, under (H*)) |
| V1 + section clauses from finite instances | SAT | SAT | SAT | SAT (Prop SR) | PROVED |
| V1/V2 + any PP59 SAFE derived clauses | SAT | SAT | SAT | SAT (Cor F″) | PROVED |

1. **The audit's decision table.** Only V3 fails, so the obstruction is pricing. This is the strongest finite-level answer possible. By Prop F, *no* finite instance of V1 or V2 can be UNSAT, whatever the cells, pieces, rivals or selected interior coherent models. This agrees with PP56's Theorem L (continuum, without sections), which reached it independently.
2. **The V3 core (§4).** It has 10 constraint groups on 4 cells:
   - the two lone-answer cells U ("above") and L ("below");
   - one pair-type cell for (A, B), on which A and D answer, B is silent and h is right at {1, 3};
   - one for (A, D), on which A and B answer, D is silent and h is right at {1, 2}.

   Minimality is CHECKED: each one-group deletion has an exact rational witness.
3. **The comparison pattern behind the SAT runs (§5).** The solver's solutions are *defence-only*:
   - every non-guidance acceptance is a selected model's defence of its own record (a coherent, indeed selected, realiser);
   - nothing is completed;
   - V2 needs no tie;
   - protection is carried by default refusals.

   So, at finite level, none of the following is needed: ties, acceptances without an old-side coherent realiser, or abandoning realiser gating. What the gate architecture adds, and what fails, is **additive pricing of the defence choices across U and L**.
4. **Ties exactly in the gap (§6).**
   - At field level, the configuration "A, B and D all exactly indifferent on U and L" exists. There is an exact witness: collinear effective weights, with separating vectors on U and L that are exactly opposite.
   - In comparison language it forces A ⪯_w A[E ↦ S] at every world for a bounded E ⊆ U ∪ L. In V1 that is UNSAT, with a 4-clause core: (IB), B's undominatedness (3 clauses) and T's direct (C).
   - Every single-world tie on a U ∪ L record is SAT in V1, record by record.
   - Ties on nested U ∪ L records at the same world cannot all be taken at once: that is UNSAT at level 1, with a one-TC-clause core closing on strict (G), which is the audit's transitivity constraint.
5. **Sections (§7).**
   - In V1 and V2 no non-guidance verdict is ever forced (Prop F with two priority orders).
   - Section clauses obtained from actual sequences can therefore only transport guidance verdicts, or the pigeonhole form of the defence disjunction. Both are implied at the limit index by its own clauses (Prop SR).
   - So a section run built from finite instances cannot create UNSAT. An axiom-level kink, if one exists, must prove acceptance along a sequence by a non-finitary argument over a two-parameter family of rivals, as PP56 Prop 5.2 already indicates.

---

## 1. The finite measurable model

**Geometry (CHECKED, `geom55.py`, `pieces55.py`).**
- ε = 3/10. The models are A = u, B = (406, 421, 373)/1200 and D = (406, 373, 421)/1200.
- The planes are the 9 planes (a∘m_v)^⊥, the planes e_w^⊥ and (1,1,1)^⊥.
- This gives 76 open cones modulo sign, each with an exact rational interior point. 32 of them are disagreement cells.
- Cell 56 = U: A alone answers, wrong only at world 1. Its interior point is PP51's "above" point.
- Cell 59 = L: A alone answers, right only at world 1. Its interior point is PP51's "below" point.
- Every cell is an open cone, so it has positive Gaussian measure.

**Pieces.**
- *Radial halves.* These are cell ∩ {|g| < r*} and cell ∩ {|g| > r*}, where r* is the χ₃ median. Each half has exactly half the cell's mass. Radial pieces are not cones.
- *Angular halves.* These are cell ∩ {±n·g > 0}, with n = g₀ × v.
  - For U, n = (0, 756973/1296000000, −2384389/2160000000). For L, n = (0, −11939/1536000, 11939/1536000).
  - Both normals have mixed signs.
  - g₀ ± δn lie in the cell, on opposite sides of n^⊥ (exact, `pieces55.out`).

**Levels.**

| Level | Active pieces | Alphabet | Universe |
|---|---|---|---|
| 0 | U, L, AB3 (55), AB13 (62), AD2 (63), AD12 (68), whole | P, S, N | 3⁶ × 3 = 2,187 models |
| 1 | U, L in radial halves; the other four whole | P, S, N on U, L; P, S elsewhere | 3⁴·2⁴ × 3 = 3,888 |
| 2 | U, L in radial × angular quarters; cells 62, 68 whole (the V3 core cells) | P, S | 2¹⁰ × 3 = 3,072 |

On every non-active cell a model equals one of A, B, D (its "outside label"). So A, B and D themselves belong to every universe.

**Coherence is exact (PROVED).** Suppose a coherent D_K (K nonempty, closed, convex, inside the simplex) is a.e. constant on every cell of a central arrangement.
- Its answer cone is the interior of the dual cone K*, whose boundary lies in the arrangement planes. So K* is polyhedral with facet normals among the plane normals, and K = conv(S) for a nonempty set S of the 13 normals. All 13 normals are nonnegative.
- The resulting catalogue has 742 patterns (exhaustive over 2¹³ subsets). It contains A, B and D.
- A model that differs between two radial pieces of one cell is not conic, hence incoherent.
- A model that differs across an angular split is incoherent, because a mixed-sign normal is not p for any p in the simplex.
- A model that is contradictory on part of a cell is incoherent.

In every universe exactly 3 models are coherent: A, B and D.

**Records and (IB) (CHECKED).** A record is the pair's support, with old and new advice there. Two pairs share a variable iff they agree piecewise on active pieces and have the same ordered outside labels. The outside part is exact: different ordered label pairs have different supports (an assertion in `inst55.py`). Records are never identified by mass.

---

## 2. Encoding (`sat55.py`); every clause carries its source label

- One boolean per (record, world). (IB) is therefore built in, for reverses and all common-context copies alike.
- **G+ / G− (strict (G)).** A record that is a weak worsening at w is the constant TRUE. A nontrivial pure improvement is FALSE. Identical pairs are reflexive TRUE.
- **TC.** For each accepted triangle X→Y→Z→X at w: (a ∧ b ∧ c) ⇒ each reverse. This is the implication itself, not "no triangles".
- **DEF.** ⋁_{i∈supp a}[C_a ⪯_i X] for each selected C_a and each rival X. All selected indices are interior. The defending world is not fixed.
- **UND.** (B₁ ∧ B₂ ∧ B₃) ⇒ A_j for j = 1, 2, 3, using all three worlds.
- **DCI / DCC.** Direct (C). For an incoherent X: ¬(B₁ ∧ B₂ ∧ B₃). For a coherent X: (B₁ ∧ B₂ ∧ B₃) ⇒ A_j. DCC is identical to UND and is labelled separately.
- **TIE (V2 only).** ¬[X ⪯_w Y] ∨ ¬[Y ⪯_w X] for distinct X, Y.
- **REAL (variant, not an axiom).** Refuse every non-guidance record whose old side has no coherent realiser in the catalogue, or (stronger) no selected realiser.

**Laziness, soundly.** TC and TIE are generated lazily:
1. Solve.
2. Build the full relation: solver values, plus guidance verdicts for records without variables.
3. Find every violated triangle or tie in the **whole** universe, by Boolean matrix products.
4. Add those clauses and repeat.

At termination every family holds over the whole universe. `sat55.audit` re-checks each family from the definitions: reflexivity, G+, G−, (IB) consistency, TC, DEF, UND, DCI and ties. All audits report 0 violations. Unknown coherence never arises, because classification is exact.

**Sizes** (V2, by label):

| Level | DEF | UND | DCI | TC | TIE | Variables |
|---|---|---|---|---|---|---|
| 0 | 6,094 | 18,282 | 6,088 | 1,643,646 | 7,533 | 38,544 |
| 1 | 10,936 | 32,808 | 10,930 | 2,087,280 | 7,881 | 67,590 |
| 2 | 8,919 | 26,757 | 8,913 | 3,353,226 | 324 | 42,768 |

At level 0 there are 823,543 distinct records.

---

## 3. Why V1 and V2 are satisfiable at every finite level

**Proposition F (PROVED; CHECKED).** Fix any finite partition into positive-measure pieces, any universe of piecewise-constant models, and any set of selected coherent models with interior indices. Fix any priority order of the pieces. Define:

> X ⪯_w Y iff X = Y, or at the first piece where X and Y differ, X's advice has smaller rank at w.

Then every V1 and V2 clause holds.

*Proof.*
1. **Structure.** Each ⪯_w is the lexicographic order of rank vectors, a strict linear order plus reflexivity.
2. **(IB).** The verdict depends only on the record's first piece and the advice there.
3. **Strict (G).** A pure improvement is better on its first piece.
4. **(TC).** There are no directed 3-cycles of distinct models.
5. **No ties.** Distinct models never tie.
6. **Protection.** A coherent model D_K, K ≠ ∅, is *locally Pareto* on every piece. It is never contradictory. It answers where h is right at all worlds. Elsewhere h, S and −h are pairwise incomparable across worlds. So on the deciding piece some world prefers C_a, and that world also refuses X ⪯ C_a. This gives DEF, UND, DCI and DCC. ∎

*Checked:* audits with 0 violations for random orders, and for outside-cells-first orders, at levels 0–2 (`run55_L*.out`, `sections55_L*.out`).

**Proposition F′ (PROVED).** Delete from Prop F's relation every non-guidance acceptance whose old side has no selected realiser. All clauses still hold, and V2 + REAL is SAT.
- *(TC).* A subset of a linear order has no 3-cycles, and guidance is contained in the order.
- *DEF.* It uses only C_a's own records, which C_a realises.
- *UND and DCI.* These only become easier with fewer acceptances. ∎

**Corollary F″ (the PP59 SAFE clauses add nothing at finite level; PROVED).** Every SAFE entry of the PP59 ledger is a finite derivation from reflexivity, strict (G), (IB), (TC), defence, undominatedness and direct (C). This covers PP18 Lemma Z0, PP19 Thms 1 (point form), 4(a)(b) and 5, Prop S, PP30 Thm 3.1, PP33 Thm 3.1, Prop K / K^S and Lemma E's inner step. Each derivation uses finitely many auxiliary models built on finitely many measurable sets: Y = T[D_Y ↦ C], N[H ↦ C], C[S ↦ D], fills on E ⊆ G, and so on.
- Refine the pieces so that those sets are unions of pieces.
- Prop F on the refined partition satisfies every axiom instance there, so it satisfies every derived clause.
- Restricted to the coarser universe it is again a Prop F relation: order the coarse pieces by their earliest refined sub-piece.

So V1 or V2 plus any finite set of SAFE clauses is SAT on every finite instance. For this reason I did not add them as separate clause families. Their effect on the SAT/UNSAT question is nil. The sequence forms are treated in §7.

**Scope of Prop F.** It is a finite-atom device. In the continuum a "first piece" exists only for a countable region priority, and within a region some atomless rule is still needed. Region priority is the device that PP26 Thm V and Cor 2.2 show fails whole-simplex (S). PP56 Theorem L gives the continuum analogue (Λ), and PP56 Prop 5.1 shows how its sections fail. So finite SAT in V1 and V2 is **uninformative about the continuum by construction**. That is the audit's warning, now proved.

---

## 4. V3: the exact core and its continuum interpretation

**System (`v3core55.py`).**
- I use PP50 Lemma 6.1's exact form of PP51's constraints: own-Bayes fields on cells, CG2, and the closed triangle test with the triple's common positive constants.
- Unknowns: effective weights ν^N > 0 and, per disagreement cell c, a vector w_c in the open orthant O_s.
- Constraints: ν^H·w_c < 0 for answerers and ν^Q·w_c > 0 for silent models.
- Group (SEP, N, c) is model N's inequality on cell c.
- Subdividing a cell changes nothing, because the constraints are pointwise. So V3's status is the same at every level.

**UNSAT certificate (PROVED; mechanically checked).** The argument is PP51 Thm 5.1, which the checker verifies in three parts:
- **(K1)** U and L with all of (SEP, A/B/D, U/L).
- **(K2)** The strict pair inequalities max_W r > min_R r, with r = log ν^A/ν^X, derived from included cells. Over all 13 weak orders, these force z^B₂ ≥ z^A₂ ≥ z^D₂.
- **The convexity step.**

The pair inequality is a two-line lemma. If max_W r ≤ log κ ≤ min_R r, then ν^X·w ≤ ν^A·w/κ, which contradicts the two strict signs. It needs only one of the two groups to be strict.

**Deletion-minimal core: 10 groups (CHECKED).**

| Cell | Advice of A, B, D | h right at | Groups | Role |
|---|---|---|---|---|
| 56 = U | P, S, S | {2, 3} | A, B, D | above: ℓ(z^A) > θ ≥ max ℓ(z^B), ℓ(z^D) |
| 59 = L | P, S, S | {1} | A, B, D | below: ℓ′(z^A) < θ′ ≤ min ℓ′(z^B), ℓ′(z^D) |
| 62 | P, S, P | {1, 3} | A, B | AB inequality: max(r₁, r₃) > r₂ |
| 68 | P, P, S | {1, 2} | A, D | AD inequality: max(r₁, r₂) > r₃ |

- U and L also supply the AB and AD inequalities for W = {2, 3}, R = {1} and W = {1}, R = {2, 3}.
- With cells 62 and 68 these force r^{AB}₁ > r^{AB}₂ and r^{AD}₂ > r^{AD}₁, which is betweenness in coordinate 2.
- Each of the 10 one-group deletions has an exact rational witness: ν, w and all strict signs checked in Fractions (`v3core55.out` (3)).

**Continuum interpretation.**
- *Sets:* any non-null pieces of the four open cones above. The certificate is pointwise, so it survives arbitrary measurable splits.
- *Records:* the selected models' own h ↔ S moves on those sets.
- *Axioms:* the only axiom-level ingredient is (TC). It enters through the gate union, as CG2 and common triple constants (Thm R1-type triangles). Everything else is architecture:
  - per-model additive fields;
  - own-Bayes margins;
  - union acceptance.

  In V1 and V2 none of these links is forced (§7). That is the precise sense in which the kink is pricing.

---

## 5. The comparison pattern of the SAT runs (V1/V2 against V3)

These are the solver's canonical solutions. The solver's default polarity is "refuse", so a solution accepts only what the clauses demand.

| Level | Accepted non-guidance records | Of which: no coherent realiser | No selected realiser | Single-world ties (V1) | Ties (V2) |
|---|---|---|---|---|---|
| 0 | 6,092 (≤ 6,094 defence obligations) | 0 | 0 | 0 | 0 |
| 1 | 10,886 (≤ 10,936) | 0 | 0 | 2,376 (22 with a selected model) | 0 |
| 2 | 8,694 (≤ 8,919) | 0 | 0 | 4 (2 with a selected model) | 0 |

- **Which single-world ties are used.** None is needed. At levels 1 and 2 the V1 solver happened to use some, for example A ~₂ A[U_out ∪ L ↦ S]. V2 removes all of them with the same acceptances.
- **Which acceptances lack an old-side coherent realiser.** None. Every non-guidance acceptance is a selected model's own defence record: a *defence-only* relation. No completion, registration or tie is required. This is PP21's inert pattern, now with three selected models defended against every rival in the universe.
- **Which refusals carry protection.** Against incoherent rivals, protection is overwhelmingly by refusal at all three worlds:

  | Level 0 | Rivals refused at 3 worlds | at 2 worlds | at 1 world |
  |---|---|---|---|
  | against A | 2,071 | 107 | 6 |
  | against B and D (each) | 1,952 | 223 | 9 |

  - Only 48 rivals (level 0) or 96 (level 2) are protected solely by strict-(G) refusals. All the others need at least one non-guidance refusal. In the gate architecture that refusal would come from every realiser's gate refusing; here it is a default.
  - The two coherent rivals of each selected model (the other two selected models) are refused at exactly 2 worlds.

**The rule behind it.** At finite level the defence-world choice is free per record (Prop F with any priority). What V3 adds is that the choice must be the sign of a *linear* functional of the record, the same functional for all of a model's records, and compatible across models through CG2. On U ∪ L no such functional exists (§4).

So the pattern the axioms permit and the architecture forbids is this: **a defence choice on records straddling U and L that is not the sign of one additive functional**. Prop F's priority between the two cells is one example. Its continuum version is a discontinuity of verdicts along rival mass paths that move mass between U and L. That is exactly PP52's changing-rival closedness, which is not (S).

---

## 6. Ties exactly in PP51's gap (coordinator's request; PP59 ledger)

**Lemma 6.0 (the reduction tolerates weak CG2; PROVED).** Apply PP50 Lemma 6.1 (⇒) with *non-strict* CG2:
- Each answerer keeps its own (weak or strict) Bayes inequality with ẑ, because only terms favourable to it change.
- Each silent model keeps its own, by humility.

So strictness in the separability form is model by model. Strict CG2 is never needed.

**Theorem 5.1′ (PROVED).** Take the kink triple in the gate-union architecture of V3 (zero rule (R0) or (R)), with:
- weak own-Bayes allowed for all three models on U ∪ L;
- non-strict CG2;
- the closed triangle test with positive constants;
- (H*): on the cells other than U and L, B and D are a.e.-uniquely own-Bayes.

Then the configuration is impossible.

*Proof.*
1. **K2 survives.** The pair inequalities from the cells off U ∪ L still force z^B₂ ≥ z^A₂ ≥ z^D₂ (CHECKED, `v3ties55.out`).
2. **The case analysis.** Run the convexity step with S on [z^B, z^D] and S₂ = z^A₂, at any point of U and any point of L, and check at which inequalities equality is possible.
   - If S₃ < z^A₃, then ℓ′(S) < ℓ′(z^A) ≤ θ′ ≤ min(ℓ′(z^B), ℓ′(z^D)) ≤ ℓ′(S). This is a contradiction even with every tie allowed.
   - So S₃ ≥ z^A₃. Then ℓ(S) ≥ ℓ(z^A) ≥ θ ≥ max(ℓ(z^B), ℓ(z^D)) ≥ ℓ(S), so every step is an equality, and S = z^A. Either:
     - (i) z^A = z^B or z^A = z^D, so r^{AB} or r^{AD} is constant, contradicting a strict pair inequality from (H*); or
     - (ii) z^A lies in the open segment, and A, B, D are all exactly indifferent at that point of U.
   - Feeding S = z^A into L gives ℓ′(z^A) ≤ θ′ ≤ min ≤ ℓ′(z^A): all three are exactly indifferent at that point of L.
   - Any point of U or L with a strict inequality gives a contradiction, so (ii) holds a.e. on U ∪ L.
3. **The common field.** By Lemma 6.0 and the ties:
   - the rescaled fields of A, B, D coincide with ẑ on U ∪ L, since for silent B, termwise humility plus a zero sum forces equality;
   - s∘ẑ is parallel to a single vector w* on U and to −w* on L, since it is orthogonal to the plane spanned by the three ν's.
4. **A zero-value record.** Choose a bounded E_U ⊆ U and E_L ⊆ L with masses that make the signed integrals cancel. Then Φ^N_w(E : h → S) = 0 at every world, for N = A, B, D.
5. **Under (R0).** T's gate accepts T ⪯_w X := T[E ↦ S] at every w. Then:
   - by (IB) this is the record B[E ↦ h] → B;
   - B's undominatedness gives B ⪯_w B[E ↦ h] at every w;
   - by (IB) again, X ⪯_w T at every w;
   - so T is all-world tied with X. X is incoherent, because E_U is bounded (Lemma H). Direct (C) fails.
6. **Under (R).** No gate accepts T → X at any world: A's value is 0, B and D are silent on E, and guidance refuses a mixed record. So T has no defence. ∎

**The field level alone does not exclude it (CHECKED, `v3ties55.out`).** "A, B, D all weak on U and L, every other cell strict" has an exact witness on all 32 cells. In it:
- ν^A, ν^B, ν^D are collinear in the z-plane;
- ν·w = 0 for all three models on U and on L;
- w_U + w_L = 0.

So step 5 or 6 is genuinely needed.

The intermediate variants are also settled at field level:
- *T alone tied:* UNSAT by the checker (the chain stays strict through B and D).
- *T with B, or T with D:* UNSAT by step 2(i).

**V1 explores exactly those ties (CHECKED, `ties55_L0.out`, `ties55_L1.out`, `coretest55.out`).** Rivals X = A[E ↦ v], with E a union of pieces of U and L meeting both, and v ∈ {S, N}:

| Forced pattern | Level 0 (2 rivals) | Level 1 (18 rivals) |
|---|---|---|
| t1: single-world tie A ~_w X, each w | SAT (6/6) | SAT (54/54) |
| t1 jointly on every such X at a fixed w | SAT | **UNSAT** at each w (see below) |
| t2: A ⪯_w X at every w (the tied gate's zero-value acceptance), v = S | **UNSAT** | **UNSAT** (9/9) |
| t2 with v = N | SAT | SAT (9/9) |
| t3: all-world tie | UNSAT (DCI) | UNSAT (18/18) |
| t4: t2 plus reverses at two worlds | UNSAT if v = S; SAT if v = N | as level 0 (27 UNSAT, 27 SAT) |

The joint-tie failure at level 1 is the audit's "A ∼ B, B ∼ C ⇒ A, C not strictly ordered", found by the solver. Its clause core (`coretest55b.out`) is one TC clause plus strict (G). For example, at world 1:
- the ties A ~₁ A[U_in ∪ L_in ↦ S] and A ~₁ A[U_in ∪ L ↦ S];
- the (IB) copy of the first;
- the strict guidance link A ⪯₁ A[L_out ↦ S].

These close an accepted triangle whose completion would reverse strict guidance. So ties on nested U ∪ L records cannot all be taken at once. Each one alone is free.

The level-0 clause core of t2 has 4 clauses:
- UND(B, B[U ∪ L ↦ P], w) for w = 1, 2, 3;
- DCI(A, A[U ∪ L ↦ S]).

The chain is (IB), then B's undominatedness, then (IB), then T's direct (C). This is the relational content of step 5. It is the exposure of PP19 Lemma 0.4 / PP18 Lemma Z0 (SAFE in PP59).

It bites exactly when the silenced set lies where B or D is silent. With v = N there is no selected model to expose, and the tie survives.

**Reading.** In comparison language the tie the gap needs is "T accepts its own silencing of U ∪ L at every world". The axioms forbid it through B's protection, with no gate involved. Single-world ties on those records are harmless and V1 allows them, but they do not help: V2 is SAT without them.

---

## 7. Sections (coordinator's request)

**Proposition B (no forced verdicts; PROVED; CHECKED).** In V1 and V2, at any finite level, every non-guidance literal [X ⪯_w Y] is unforced.
- The record is mixed at w, so it has a piece where X is better at w and one where X is worse.
- Prop F with either piece first gives two solutions that disagree on the literal.
- `sections55.py` audits Prop F for random and outside-first orders and confirms the two witness pieces for every literal on a selected model's record.

**Proposition SR (section clauses from finite instances are redundant; PROVED).** Let a_k → a in the selected interior family, with a fixed rival X.
- **(a) Guidance acceptances.** If C_{a_k} ⪯_w X holds by guidance for all k, then C_a ⪯_w X by guidance. Along a subsequence C_{a_k} → C_a a.e., and the pointwise rank inequality passes to the limit.
- **(b) The pigeonhole form.** By pigeonhole, some world w accepts for infinitely many k, so (S) gives ⋁_{w∈W∞}[C_a ⪯_w X]. Here W∞ is the set of worlds not refused by strict (G) for infinitely many k.
  - If X is a pure improvement of C_{a_k} at w for all large k, the same limit argument makes it a pure improvement of C_a at w.
  - So W∞ contains C_a's own available worlds, and the clause is implied by C_a's DEF.
- **(c) Nothing else.** By Prop B, nothing else is forced, and under M6 sections enter only through proved acceptances. So no section clause derived from finite instances changes the status of V1 or V2. V1 + SEC is SAT at every level. ∎

**What a section-based kink would need.** It would need acceptance along a sequence, with a fixed rival, proved by an argument that no finite instance supplies:
- an infinite family of rivals used simultaneously;
- a two-parameter interaction, as PP56 Prop 5.2 requires;
- or continuity beyond (S) (PP52 Thm 4.1, which is COND-Ct+).

I did not find such an argument. I make no claim either way: OPEN.

---

## 8. Scope: what is omitted

1. **Sections.** Not encoded as clauses (Brief 53); §7 shows that their finite shadows are redundant. The continuum section question remains open.
2. **Rivals beyond the cell algebra.**
   - Only piecewise-constant models on the stated pieces appear.
   - Non-active cells take one of the three selected models' advice.
   - The alphabet is restricted (P, S, N; P, S at level 2).
   - Contradictory advice appears only in coherence classification.
   - No selected models beyond A, B and D. Prop F covers any additional interior posterior models, so adding them cannot change V1 or V2.

   For UNSAT this is sound, since restriction weakens. For SAT it means only a candidate, but Prop F supplies SAT on *every* finite universe anyway.
3. **Masses.** Never used in V1 or V2. Verdicts on equal-mass records are independent variables. V3 uses only pointwise field inequalities, so masses do not enter its certificate. Theorem 5.1′ step 4 uses the existence of a cancelling mass ratio (non-atomicity), which is continuum reasoning.
4. **Global (C).** "Every incoherent model is dominated" is existential and not encoded. Prop F's relations leave many incoherent undominated models; in a full system they are removed only through (S) and KKM.
5. **(C) for coherent models other than the selected ones**, and their defences, are not checked (recorded scope).
6. **V3's triangle test.** V3 imports the closed triangle test with positive constants, as PP51 does. Under (R0) with ties its necessity is not established (REFEREE_round50: only the pair sandwich is). Theorem 5.1′ is therefore a statement about PP51's architecture.

---

## 9. Next step

Since only pricing fails at finite level, the decisive object is a **non-additive defence choice on records straddling U and L, with closed fixed-rival sections**. Concretely:
- take PP56's Λ, which is lexicographic across levels, and replace its box tie-breaks on the U/L interaction by a two-parameter rule;
- check the fixed-rival section condition over a 2-D posterior neighbourhood directly, by the actual-sequence method of M6;
- keep in mind that by Theorem 5.1′ no tie-based repair inside gate unions exists, so the rule must leave closed additive gates.

---

## 10. Scripts (`r9/PP55_py/`; run `python3 -B <script> [level] > <out>` inside the folder)

| Script | Content | Label |
|---|---|---|
| `geom55.py` | exact cells (76), advice, ranks, complete coherent catalogue (742) | library |
| `pieces55.py` | angular-split normals mixed-sign; both sides nonempty; ALL PASS | CHECKED |
| `inst55.py`, `levels55.py` | pieces, universes, exact record identification, coherence | library |
| `sat55.py` | labelled clauses, lazy TC/TIE, `audit`, Prop F relations, clause cores | library |
| `run55.py` | V1, V2, V2+REAL (both kinds), Prop F audit, patterns; `run55_L{0,1,2}.out` | CHECKED |
| `v3core55.py` | V3 certificate checker, deletion-minimal core, exact witnesses for minimality, tie variants | PROVED + CHECKED |
| `v3ties55.py` | K2 from cells off U ∪ L; exact all-tie field witness | CHECKED |
| `ties55.py`, `coretest55.py`, `coretest55b.py` | V1 tie experiments (t1–t4, joint); the 4-clause exposure core; the joint-tie TC core | CHECKED |
| `sections55.py` | Prop F under arbitrary priority orders; Prop B witnesses | CHECKED |
| `gates55.py` | z3 encodings of V3. Not used for any claim: z3's nonlinear solver did not finish | — |
