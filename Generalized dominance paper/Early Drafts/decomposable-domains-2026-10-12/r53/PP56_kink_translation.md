# PP56. The kink certificate in the language of comparisons

23 October 2026. Task PP56 of Brief 53. One reader (me); not refereed. Worked independently of the parallel search agent. The coordinator's ledger PP59 arrived mid-task and is used in §2 and §5.

**Labels.**
- PROVED: a complete argument is given here.
- CHECKED: exact rational computation in `r9/PP56_py/`; every script ends ALL PASS.
- NUMERICS: none is used.
- CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF53; the binding audits (AUDIT_round53, _final, _ties, _transfer, AUDIT_section_topology, AUDIT_radial_transport); PP51 §5 (Thm 5.1); PP50 §6 (Lemma 6.1, Prop 6.2, Theorem K); PP52 (Thm 4.1, Prop 7.1, Conj 7.2); REFEREE_round50 (Thm R1, §1.2, Lemma S); AUDIT_completion; LEAD_selection_count; DESIGN_MEMO §8.15 (PP23 Ω, PP25 Thm A, the lead's balance identity); PP59 (ledger). No axiom is added. Extra hypotheses are named where they enter.

---

## 0. Verdict

1. **Translation (§2).** I split the kink certificate (PP51 Thm 5.1, run through PP50 Lemma 6.1 and REFEREE_round50 Thm R1) into twelve steps.
   - **Forced by the axioms alone (i):** the cell geometry; the identification, by exact (IB), of the R1 triangle's three links with *defences* of A, B and D against three hybrid rivals; and one genuine negative clause, the CG2-necessity triangle, which ends in a strict guidance link.
   - **Forced only by the gate architecture (ii):** every step that carries the contradiction:
     - which world accepts (additive acceptance);
     - that all three links are accepted at one world for suitable masses (Lyapunov plus linearity);
     - that reverses are refused (strict CG2, no other routes);
     - the effective-weight separability of Lemma 6.1;
     - the strictness hypothesis.
   - **Forced only by a further continuity assumption (iii):** no step. PP52 Thm 4.1 (closedness along changing-rival paths) is not used by the kink, and PP59 §5 records that it is vacuous on posterior pairs.

   So the outcome is the one the audit allowed: **the contradiction needs a field inequality, orthant separability of the two certificate cells in effective-weight space, for which no axiom-level comparison constraint has been established.**
2. **Direction (b) holds at a stated level, and more strongly than asked (Theorem L, PROVED; CHECKED).** Take one explicit relation Λ, the lexicographic order of a *balanced* strictly guiding field followed by its localisations to rational boxes.
   - It satisfies reflexivity, strict (G), (IB) and (TC). **Every world is a linear order, so there are no single-world ties at all.**
   - Every selected model is strictly better than every other model at some world. That gives defence on the full support, undominatedness, direct (C) for every model, and (LA).
   - This holds simultaneously for the kink triple **and for every posterior model in the test neighbourhood N_u**, against all measurable rivals.

   Hence **no certificate, finite or not, can be built from reflexivity, strict (G), (IB), (TC), the defence disjunctions, exact undominatedness and direct (C), with any cells, subdivisions or advice values.** This includes every SAFE clause in PP59.
3. **The kink is escaped without single-world ties (§4.2; CHECKED).** Λ uses exactly three departures from the gate architecture:
   - exact Bayes indifference of its first level on the disagreement region. This is PP51's stated residual gap; PP59 item (1) notes that DESIGN_MEMO §8.21 dropped it;
   - verdicts that are not closed along mass paths;
   - reverse comparisons whose old side has no coherent realiser.

   It does **not** use single-world ties. The audit's hypothesis, that the kink comes from prohibiting the indifferences (TC) allows, is not borne out at the level of the triple: the indifference that matters is at the level of the *field*, not of the relation.
4. **Where the strictness hypothesis bites (coordinator item 1; §2.3; CHECKED).** On the two certificate cells, Λ's first level makes A's two swap vectors exactly opposite, (−2, 1, 1) and (2, −1, −1). At equal masses the record (P⁺ ∪ P⁻: h → S) has level-1 value 0 at every world. The three treatments of that comparison differ:
   - a **closed** zero-accepting gate with that field makes the incoherent rival A[P⁺ ∪ P⁻ ↦ S] an **all-world** tie partner of T;
   - a strict gate leaves T **undefended**;
   - Λ decides it strictly at two worlds, with no tie.

   A tie at that comparison does not dissolve the contradiction inside closed gates. A non-closed tie-break does.
5. **Direction (a): any axiom-level kink must use sections (§5).**
   - **Prop 5.1 (PROVED).** Every relation of Λ's form has a non-closed fixed-rival section on any 2-D posterior neighbourhood. So Λ is not a solution of the module.
   - **Prop 5.2 (PROVED; CHECKED).** On the one-parameter family of two-cell rivals, closed and tie-free verdicts satisfy every clause (a "staircase"). So even a (iii)-level kink needs at least a two-parameter family of rivals.
   - Whether sections, entered through actual sequences (M6), yield an axiom-level contradiction near the kink is **OPEN**. §5.3 states the narrowest open question.

| Item | Result | Label |
|---|---|---|
| Step-by-step translation and classification | §2, Table 1 | PROVED (classification); geometry CHECKED |
| The strictness hypothesis as a comparison | §2.3 | PROVED; CHECKED |
| Balanced lexicographic relation Λ: all non-section axioms, linear orders, all of N_u | Thm L | PROVED |
| Λ on the kink's actual cells (2¹⁸ splice rivals; four-value instances; all triples) | §4.1 | CHECKED |
| Λ escapes without ties; mass-path discontinuity; gate-forbidden acceptances | §4.2 | CHECKED |
| No non-section certificate exists at any level | Cor 4.3 | PROVED |
| Λ-type relations have a non-closed section | Prop 5.1 | PROVED |
| Closed tie-free staircase on the two-cell path | Prop 5.2 | PROVED; CHECKED |
| Axiom-level kink using sections | §5.3 | OPEN |

---

## 1. Setting and what "translation" means

The setting is Brief 53's.
- Three worlds; problems g ∈ R³; Gaussian μ; the full four-advice domain; ranks: correct 0 < silent 1 < wrong 2 < contradictory 3.
- ε = 3/10. A = u (so C_A = T), B = (406, 421, 373)/1200, D = (406, 373, 421)/1200.
- `cells56.py` (CHECKED; it uses an unmodified copy of PP50's arrangement enumerator) finds 56 cells, 36 of them with disagreement. That is 18 up to the sign of g, all two-valued, as in PP50 §6.2.
- Notation:
  - **P⁺** ("above") is a bounded piece of the cell where A answers h alone, with h wrong only at world 1;
  - **P⁻** ("below") is a bounded piece of the cell where A answers alone, with h right only at world 1.

The exact encoding is AUDIT_round53_final's:
- the defence clause ⋁_{i ∈ supp a} [C_a ⪯_i X], with no defender chosen in advance;
- (TC) as reverse completion;
- undominatedness (⋀_i B_i) ⟹ (⋀_i A_i);
- direct (C), split between coherent and incoherent rivals;
- (IB) on every installed comparison.

**Local proxies (used throughout; exact (IB)).** Work with models that equal A outside finitely many bounded pieces. For a selected N ∈ {B, D}, put A^N := A[pieces ↦ N]. Then rec(N → N[E ↦ y]) = rec(A^N → A[pieces ↦ y′]), where y′ = y on E and N elsewhere. So N's defence, protection and direct-(C) clauses against every rival differing from N only on the pieces are *exactly* clauses for A^N inside the finite instance.

The rivals N[E ↦ y] with E ≠ ∅ bounded are incoherent: coherent models agreeing off a bounded set agree a.e. (AUDIT_completion §1). So the incoherent form of (C) applies.

---

## 2. The certificate, step by step

### 2.1 The dictionary

Three exact (IB) identifications carry everything that the axioms can say about the kink.

**(D1) Two-cell records.** On P⁺ ∪ P⁻, B and D both say S and A says h. Write X := A[P⁺ ∪ P⁻ ↦ S], a_w := [A ⪯_w X] and b_w := [X ⪯_w A]. By (IB):
- b_w = [B ⪯_w B[P⁺ ∪ P⁻ ↦ h]] = [D ⪯_w D[P⁺ ∪ P⁻ ↦ h]];
- a_w is B's (and D's) reverse variable.

The complete clause set on such a record is:

  ⋁a_w (A's defence),  ⋁b_w (B's and D's defences),  ¬⋀b_w (A's protection with (C)),  ¬⋀a_w (B's and D's protection with (C)).

When both pieces are non-null the record is mixed at every world, so strict (G) fixes nothing.

**(D2) The R1(ii) triangle.** REFEREE_round50 Thm R1(ii) uses three piece types:
- on P_ab ⊆ {A ≠ B}: X = A, Y = B, Z = A;
- on P_bd ⊆ {B ≠ D}: X = Y = B, Z = D;
- on P_da ⊆ {D ≠ A}: X = A, Y = Z = D.

By (IB) the triangle's links are three defence variables: [X ⪯_w Y] = [A ⪯_w R₁], [Y ⪯_w Z] = [B ⪯_w R₂] and [Z ⪯_w X] = [D ⪯_w R₃]. Here R₁ = A[P_ab ↦ B, P_da ↦ D], and R₂, R₃ are defined likewise.

(TC) then says: **if A, B and D all defend against R₁, R₂, R₃ at the same world w, then R₁ ⪯_w A, R₂ ⪯_w B and R₃ ⪯_w D.** These are three single-world ties between protected coherent models and incoherent hybrids. The axioms allow them unless they occur at all three worlds.

**(D3) The CG2-necessity triangle** (REFEREE_round50 §1.2). Put X = N, Y = N[D ↦ M] and Z = N[D₀ ↦ w-correct], with D₀ ⊆ D on the part where M is strictly w-better. Then Z ⪯_w X by guidance, and the reverse is a strict improvement. (TC) gives the genuinely axiom-level negative clause

  ¬([N ⪯_w N[D ↦ M]] ∧ [N[D ↦ M] ⪯_w Z]).

Its two variables are a defence variable of N and, by (IB), a defence variable of M.

### 2.2 Table 1: classification

(i) = forced by the axioms alone; (ii) = forced only by the gate architecture; (iii) = forced only by an extra continuity assumption.

| # | Step of the gate proof | In comparison language | Class |
|---|---|---|---|
| 1 | Cells; (K1) two lone-answer cells of opposite sign type; (K2) pair types; (K3) two-signedness | Facts about advice, independent of any ranking | (i), CHECKED (PP50 §6.2; `cells56.out`) |
| 2 | Every selected non-vertex model needs non-guidance acceptances of its own records (shell rival, PP52 Prop 7.1) | Defence disjunction + strict (G) | (i) |
| 2′ | ...and they come from *its own additive gate* | No counterpart | (ii) Gt, Ad |
| 3 | Own-Bayes: λ^N·Φ^N(r) > 0 for every record N realises | Only ⋁_w [N ⪯_w X]: *some* world, not a prescribed one | (ii) |
| 4 | Acceptance at w ⇔ Φ^N_w(r) ≥ 0 (R0) or > 0 (R) | Accepted masses form a closed (or open) half-space; the axioms put no shape on them | (ii) Ad; closedness alone would be (iii) |
| 5 | Reverse refusal: strict CG2 and no other acceptance routes | Axiom refusals come only from strict (G) and from protection (one refusing world per incoherent rival) | (ii) St, Gt |
| 6 | CG2 necessity (REFEREE §1.2) | Clause (D3) is (i); its premise, that both links are accepted, comes from positive gate values | clause (i); activation (ii) |
| 7a | R1(ii): the links are three gate acceptances | (D2): three defences, by exact (IB) | (i) |
| 7b | R1(ii): some masses make all three links accepted *at one world* | Needs Lyapunov plus linear acceptance (R1 proof, steps 3–4) | (ii) |
| 7c | R1(ii): the reverses are refused | The axioms allow them as single-world ties (D2) | (ii) St |
| 8 | Lemma 6.1: own-Bayes + closed triple test ⇔ orthant separability of every cell by effective weights ν^N = λ^N/c^N | Algebra on 3–7 | (ii) |
| 9 | Strictness: A's own-Bayes unique, or CG2 strict, on the two certificate cells | §2.3 | (ii) St |
| 10 | Thm 5.1 convexity: z^A between z^B and z^D cannot be cut on both sides | Geometry applied to 8 | (ii) in use |
| 11 | Theorem K: density points of the gated set give kink triples; every selected model is gated | No sections and no continuity are used; "every selected model is gated" is step 2′ | (ii) |
| 12 | PP52 Thm 4.1 (KKM along mass paths) | Not used by the kink; vacuous on selected posterior pairs (PP52 Cor 5.2; PP59 §5) | (iii), idle |

**Reading (PROVED).** Every implication that moves the argument towards a contradiction is in class (ii). The axiom-level content (1, 2, 6-clause, 7a) is a set of **disjunctions with free defending worlds** (D1, D2) and **negative 2-clauses** (D3). The kink turns them into a contradiction only by fixing, through an additive gate, *which* world defends: that is the field inequality in step 8.

### 2.3 Where strictness enters (coordinator item 1)

In Lemma 6.1's proof (step 3, PP51 Lemma 2.3) strictness makes the answerer's inequality strict on the certificate cells. In comparisons, it concerns A's verdicts on the two-cell records (D1) as the mass ratio m(P⁺) : m(P⁻) varies.
- At ratio 0 and ratio ∞ the verdicts are fixed by guidance: A defends at {1} and at {2, 3} respectively.
- Somewhere in between, the defending world must switch. Strictness guarantees that a gate does this with a strict verdict on both sides.
- In the tie case, the switching ratio carries a record whose gate value is 0.

**CHECKED (`kink56.out` (1)).** With Λ's first-level field u¹ the tie case is realised exactly:
- every certificate type is weakly separable with ν^A = ν^B = ν^D = (1, 1, 1), with every inequality an equality (`lex56.out`);
- the swap vectors of A on P⁺ and P⁻ are (−2, 1, 1) and (2, −1, −1);
- at equal masses X₁ := A[P⁺ ∪ P⁻ ↦ S] has level-1 value 0 at every world.

The three ways of treating that comparison:

| Rule on that comparison | [A ⪯_w X₁] | [X₁ ⪯_w A] | Outcome |
|---|---|---|---|
| zero-accepting union gate (R0), common field u¹ | all w | all w | all-world tie of T with incoherent X₁: violates (C) |
| strict gate (R), same field | no w | — | T undefended: violates (S) |
| Λ (non-closed tie-break) | w = 2, 3 | w = 1 | strict, no tie |

So a single-world tie at that comparison neither causes nor cures the kink. What the gate kink excludes is the field-level tie together with closedness. Breaking that tie with a later additive level, which is necessarily not closed along the mass path (§4.2), removes the contradiction.

---

## 3. The missing constraint, stated once

The gate proof's decisive inequality is PP50 Lemma 6.1 on the two certificate cells:

> there are ν^A, ν^B, ν^D > 0 and, for each cell, an orthant vector w with ν^A·w ≤ 0 ≤ ν^B·w, ν^D·w, strict for A.

Its comparison-level antecedent would be:

> A's defending world on every two-cell record (D1), and B's and D's on every pair-type record, is given by the sign of one linear functional of the record's masses, common to the triple at each world.

No axiom says this:
- (S) gives a disjunction;
- (TC) gives reverse completion;
- (IB) gives identifications only between equal records.

Theorem L below shows that no combination of these clauses can replace it.

---

## 4. Direction (b): a completion with no ties

### 4.1 The relation Λ

**Hypothesis (2V).** 𝒮 is a set of coherent models with all indices interior. On R(𝒮) := {g : the members of 𝒮 do not all give the same advice}, at a.e. g every member says either a common answer h(g) or S.

(2V) holds for the kink triple (CHECKED, `cells56.out`). It also holds for every posterior neighbourhood N_u small enough that u ∈ M_a for all a ∈ N_u: all answers then have the sign of u·g (PP51 §1; REFEREE_round50 §2.1).

**Level 0: a balanced field.** At a problem g with mixed signs, let x range over the two answers, and let Cor(x) and Wr(x) be the worlds where x is right and wrong. Put

  u¹_w(g, x) = −k_c|g| on Cor(x),  +k_r|g| on Wr(x);  u¹(g, S) = 0;  u¹_w(g, C) = (1 + max|k|)|g|,

with (k_c, k_r) chosen as follows:
- (|Wr|, |Cor|) if x = h(g) and g ∈ R. Then x and S are exactly indifferent at λ = (1, 1, 1).
- (2|Wr|, |Cor|) if x is the members' common advice off R. Then x is strictly λ-best.
- (|Wr|, 2|Cor|) otherwise. Then x is strictly λ-worse than S.

Off R with S as the common advice, both answers take the third row. At unanimous-sign g, put u¹_w = rank_w·|g|.

`lex56.py` (CHECKED) verifies on all 56 cells of the kink arrangement:
- strict guidance at every world over all four advice values;
- balance on R;
- strict λ-optimality of the common advice off R.

**Later levels.** Enumerate the open rational boxes B₁, B₂, …. Level q is 1_{B_q}·u¹.

**The relation.** For models X and Y and a level ℓ, write Δ^ℓ_w(X, Y) := ∫_{X≠Y} [u^ℓ_w(g, Y(g)) − u^ℓ_w(g, X(g))] dμ. Then

  X ⪯_w Y  iff  the sequence (Δ^ℓ_w(X, Y))_{ℓ ≥ 0} is lexicographically ≥ 0.

**Theorem L (PROVED).** Under (2V), Λ satisfies:
- reflexivity, strict (G), (IB) and (TC);
- **every world is a linear order on models modulo null sets** (no single-world ties);
- for every N ∈ 𝒮 and every X ≠ N there is a world w with N ≺_w X.

Hence every member of 𝒮 is defended on {1, 2, 3} against every measurable rival, is undominated, and has no all-world tie with any model. So direct (C) holds for every model, and (LA) holds when T ∈ 𝒮.

*Proof.*
1. **(IB).** Δ depends only on the record.
2. **Reflexivity and (TC).** Δ^ℓ(X, Z) = Δ^ℓ(X, Y) + Δ^ℓ(Y, Z) termwise. Lexicographically nonnegative sequences are closed under addition, and every sequence or its negative is lexicographically nonnegative. So each world is a total preorder, and a total preorder satisfies (TC).
3. **No ties.** If X ≠ Y on a non-null set E, then f := u¹_w(·, Y) − u¹_w(·, X) is nonzero a.e. on E, because ranks are injective a.e. and u¹ is strictly guiding. If every box integral of f vanished, f would vanish a.e., by the π–λ theorem. So some level is nonzero at every world.
4. **Strict (G).** A pointwise weak w-improvement that is strict somewhere has Δ⁰_w > 0.
5. **Protection.** Fix N ∈ 𝒮 and X ≠ N. Pointwise, λ·(u^ℓ(g, X(g)) − u^ℓ(g, N(g))) ≥ 0 at every level, since a localisation keeps a pointwise inequality. Let ℓ₀ be the first level at which the vector V := (Δ^{ℓ₀}_w(N, X))_w is nonzero; it exists by step 3. Then λ·V ≥ 0, V ≠ 0 and λ > 0, so V_w > 0 for some w. At that world all earlier levels vanish, so N ≺_w X. ∎

**Corollary 4.3 (PROVED).** Consider any finite or infinite set of clauses, on any cells and subdivisions and with any advice values, each following from reflexivity, strict (G), (IB), (TC), the defence disjunctions of the members of N_u, exact undominatedness or direct (C). Λ satisfies all of them. In particular this covers:
- PP59's SAFE entries 12 (point form), 13(a)(b), 14, 15, 16, 17 and 18, which are derived from these axioms together with T's defence;
- the kink's translated clauses (D1)–(D3).

So **no certificate without a section clause exists.**

*Origin.* Λ is the lead's balance identity and PP25 Theorem A (one indifferent first level, π-system tie-breaks; DESIGN_MEMO §8.15), extended from bounded rivals to all measurable rivals and applied to the kink module. The new content is the application: the kink has no axiom-level shadow outside sections.

**CHECKED (`instance56.out`).** Exact instances on the kink's actual cells: bounded pieces, rational masses (all verdicts are invariant under a common rescaling, so any small scale realises them), and the local proxies of §1.
- **I1.** All 18 disagreement cells with values {h, S}: 2¹⁸ = 262,144 rivals. Defence, strict protection and direct (C) hold for A, B and D, at two random mass vectors.
- **I2.** Six pieces, including P⁺ and P⁻, with all four advice values: 4,096 rivals. Same result.
- **I3.** Two 64-model instances, checked exhaustively: reflexivity; strict (G) on every pair; (IB) constant on all 729 and 2,197 record classes; (TC) on every ordered triple at every world; no single-world ties.

### 4.2 What Λ uses, and what it does not

**CHECKED (`kink56.out`).**

1. **No ties anywhere.** In particular, the R1(ii) triangle (D2) was evaluated over every triple of cells (A ≠ B, B ≠ D, D ≠ A), with three random mass vectors each, at every world: 12,672 instances. None had all three links accepted, and none had a single-world tie. The triangle is never formed. One link is simply refused, which a linear order can always do.
2. **Not closed along mass paths.** Take masses (t, 1) on (P⁺, P⁻). Then A ⪯₁ X_t for t = 1 − 1/n, n = 2, …, 10⁶, but not at t = 1. So the hypothesis of PP52 Thm 4.1 and of Lemma S fails, exactly at the field tie of §2.3.
3. **Acceptances the gates forbid.**
   - Of the 19,009 accepted reverse links in item 1, 5,181 have no old-side realiser among A, B and D.
   - In a six-piece instance, 2,803 of 6,048 accepted comparisons are non-guidance with no realiser in {A, B, D}. These are acceptances that a realiser-gated rule refuses.
4. **Field-level indifference.** This is the residual tie case of PP51 Thm 5.1 (§2.3).

**Answer to AUDIT_round53_final's four questions, at the level of the triple and of N_u without sections:**
- (1) No single-world tie is essential.
- (2) The reverse comparisons that abandon old-side realisers are those listed in item 3. They are needed for totality, not for any particular defence.
- (3) Refusals preserve protection automatically, because the protecting world is the first nonzero level's positive coordinate.
- (4) Everything holds for arbitrary measurable splits and all common-context copies, by Theorem L.

---

## 5. Direction (a): what an axiom-level kink would need

### 5.1 Λ fails sections

**Proposition 5.1 (PROVED).** Let N_u be a closed 2-D neighbourhood of u with connected interior V. Let a ↦ C_a be injective and continuous in measure on N_u, and let every C_a be silent on an open cone. Then for every relation of Λ's form (any field u¹ meeting §4.1's conditions, with levels localised on the rational boxes), some section {a ∈ V : C_a ⪯_w X} is not closed.

*Proof.*
1. **The level functions.** Put f^ℓ_w(a) := ∫ u^ℓ_w(g, C_a(g)) dμ. These are continuous on V, by dominated convergence (|u^ℓ| ≤ K|g|).
2. **Some level varies.** If every f^ℓ_w were constant on V, then for a ≠ b every box integral of u¹_w(·, C_b) − u¹_w(·, C_a) would vanish. That would give C_a = C_b a.e., contradicting injectivity.
3. **The first varying level.** Let ℓ* be the first level at which some f^{ℓ*}_w is not constant on V.
4. **A point that is not a local minimum.** A continuous function on a connected open set for which every point is a local minimum is constant: along a path, the set where the maximum is attained is open and closed. So there are a′ ∈ V and a_k → a′ with f^{ℓ*}_w(a_k) < f^{ℓ*}_w(a′).
5. **Two silent points.** Pick points x_I ≠ x_W in Sil(C_{a′}), off all box boundaries, and so close together that no box of index ≤ ℓ* separates them. Let q be the least index of a box containing exactly one of them. Then q > ℓ*. Relabel so that B_q ∋ x_I.
6. **The rival.** Let X equal C_{a′}, except:
   - on a small ball I around x_I, put the w-correct answer;
   - on a small ball W around x_W, put contradiction.

   Choose the balls' sizes so that the two level-0 contributions at w cancel. Then X agrees with C_{a′} at w on every level of index < q. At level q, X is strictly better. So C_{a′} ⋠_w X.
7. **The sequence.** For each k, the first nonzero term of (Δ^ℓ_w(C_{a_k}, X))_ℓ is f^{ℓ*}_w(a′) − f^{ℓ*}_w(a_k) > 0. So C_{a_k} ⪯_w X.

The section contains every a_k and misses a′. ∎

So Λ is a solution of every module obligation except (S)'s section clause. **The kink's whole axiom-level weight, if any, must therefore pass through actual section sequences (M6).** This is consistent with PP25's remark that FF2 excludes Theorem A once (S) is imposed, but needs no whole-simplex hypothesis.

### 5.2 Closedness along one parameter is not enough

Parametrise the two-cell rivals by s ∈ [0, 2].
- On [0, 1], the S-swap on P⁺ grows to the full piece (masses (s, 1)).
- On [1, 2], the swap on P⁻ shrinks to nothing (masses (1, 2 − s)).

Write F_w := {s : A ⪯_w X_s} and G_w := {s : X_s ⪯_w A}. As s increases, X_s gets strictly better at world 1 and strictly worse at worlds 2 and 3, by guidance at every step. So (TC) through a guidance link gives:
- ¬(F₁(s′) ∧ G₁(s)) for s < s′;
- ¬(F_w(s) ∧ G_w(s′)) for s < s′ and w = 2, 3.

The endpoints are fixed by strict (G):
- at s = 0: F = {1}, G = {2, 3};
- at s = 2: F = {2, 3}, G = {1}.

**Proposition 5.2 (PROVED; CHECKED on a 97-point grid, `kink56.out` (3)).** The closed sets

  F₁ = [0, ½], F₂ = [½, 2], F₃ = [13⁄8, 2];  G₁ = [3⁄2, 2], G₂ = [0, 3⁄8], G₃ = [0, 3⁄2]

satisfy every clause of this family:
- **defences:** both covers hold;
- **protection with (C):** F₁ ∩ F₃ = ∅ and G₁ ∩ G₂ = ∅, so no point lies in all three F_w or in all three G_w;
- **no single-world tie:** F_w ∩ G_w = ∅ at each w;
- **(TC):** both families of clauses above hold, by interval comparison;
- the endpoint values.

So A's defending set runs {1} → {1, 2} → {2} → {2, 3} along the path, and the reverse runs {2, 3} → {3} → {1, 3} → {1}.

*Reading.* Closed verdicts on a one-parameter family give only pairwise coincidences (one-dimensional KKM), which the staircase absorbs. A (iii)-level kink would need a two-parameter rival family, where KKM forces triple coincidences, as in PP52 Thm 4.1. That theorem's pair-level form is vacuous for posterior pairs (PP52 Cor 5.2). For the kink cells:
- K(A, B) = {1, 3} (worlds 1 and 3 have pieces; world 2 has none);
- K(A, D) = {1, 2}.

So a two-parameter argument would have to mix B-pieces and D-pieces. The hybrid M it produces is not protected. I tried the obvious continuation, adding the (TC) clauses through A^B and A^D, and it yields no contradiction.

### 5.3 Status of direction (a)

- **No certificate without sections (PROVED, Cor 4.3).**
- **With sections:** OPEN. The narrowest form of the question is:

  > For a closed 2-D posterior neighbourhood N_u, is there an actual sequence a_k → a with a fixed rival X, acceptance forced at every a_k by the non-section clauses, such that the forced limit acceptance at a contradicts the non-section clauses at a?

  Prop 5.1 shows that Λ fails exactly here, so this is where a certificate would have to bite.
- **Kink geometry is irrelevant until then.** Theorem L does not use the kink cells, so an axiom-level obstruction, if one exists, is not specific to the kink triple. It would be a statement about sections over a 2-D posterior family.

**CONJECTURE 5.3 (stated as a target, not supported by evidence here).** Under closedness along mass paths of each selected model's own verdicts (PP52 Thm 4.1's hypothesis), together with the axioms, the kink triple is not completable. Prop 5.2 shows that such a proof must use at least three piece types, with records realised by two different selected models.

---

## 6. What this changes

1. **The kink is architectural, in the precise sense the audit allowed.** Its contradiction lives in steps 3–5 and 7b–10 of Table 1, all class (ii). Theorem L shows that the axioms, with sections removed, are satisfiable on the whole test neighbourhood with no ties at all.
2. **Ties are not the lever.** Allowing single-world ties enlarges the space, but the triple can be completed without them. The real lever is a *field-level* indifference, broken non-closedly. Any construction that keeps verdicts closed along mass paths must look elsewhere. Prop 5.2 shows that one-parameter closed staircases are available, so the place to look is two-parameter interactions.
3. **The remaining difficulty is one clause.** Everything except fixed-rival sections is solved simultaneously for N_u by Λ. Prop 5.1 shows how Λ's sections break: at the first non-constant level of a ↦ U^ℓ(C_a). A constructive next step would be a non-closed relation in which every member's verdict functions are locally constant on all levels that decide comparisons against a fixed rival. Prop 5.1 says box tie-breaks cannot provide this, but it does not exclude other tie-breaking families.

---

## 7. Scripts (`r9/PP56_py/`; run `python3 -I -B <script> > <script>.out` inside the folder)

| Script | Content | Label |
|---|---|---|
| `pp50_lib_copy.py` | unmodified copy of PP50's exact arrangement enumerator | library |
| `cells56.py` | all 56 cells of the kink arrangement; 36 with disagreement; two-valued | CHECKED |
| `lex56.py` | Λ's level-0 field; strict guidance, balance on R, strict optimality off R on every cell; tie case of Lemma 6.1 with ν = (1, 1, 1) | CHECKED, ALL PASS |
| `instance56.py` | exact local-proxy instances I1–I3: 2¹⁸ splice rivals; four-value rivals; exhaustive axiom check (reflexivity, strict (G), (IB), (TC), no ties, defence, protection, direct (C)) | CHECKED, ALL PASS (about 20 s) |
| `kink56.py` | §2.3 table (R0, R, Λ on X₁); §4.2 mass path; Prop 5.2 staircase on a grid; R1(ii) triangles over all cell triples; counts of realiser-free acceptances | CHECKED, ALL PASS |

**Most important next step.** Attack §5.3 directly. Take two indices a_k → a in N_u, a fixed rival concentrated near the moving boundary between C_{a_k} and C_a, and the clauses of Cor 4.3. Ask whether every relation satisfying those clauses must, like Λ, accept along the sequence and refuse at the limit. A yes would give the first axiom-level obstruction in the module. A no would give the first candidate whose sections are closed, and it should be extracted as a rule, not a table.
