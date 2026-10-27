# PP57. Tie completion of the kink, and what closed sections do to it

23 October 2026. Task PP57 (constructor) of Brief 53. One author; not refereed. Takes in the coordinator's three mid-task messages: the PP59 ledger, PP56 (Theorem L, Prop 5.1), and REFEREE_round52 (Theorem K′).

**Labels.**
- PROVED: the argument is complete here, or it cites a named result together with its stated hypotheses.
- CHECKED: an exact rational computation in `r9/PP57_py/`.
- NUMERICS: none used.
- CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF53. The binding audits (AUDIT_round53, _section_topology, _transfer, _radial_transport, _ties, _final). PP49–PP52, PP21 (whose engine is reused unchanged except for one flag), AUDIT_completion, LEAD_selection_count, DESIGN_MEMO §8. Also PP59 (ledger), PP56 and REFEREE_round52. No axiom is added. Every extra hypothesis is named where it is used.

---

## 0. Verdict

1. **Gate acceptances cannot be completed by ties. The exact-tie case breaks protection instead (§2; PROVED).**
   - *Tie–pad lemma.* This is PP19 Thm 1 stated for an arbitrary tied pair. If X ~_w Y, then X ⋠_w W for every W that is strictly better than Y at w by guidance.
   - *Consequence.* A tie can sit only on a "knife-edge" comparison, one whose w-improving pads are all refused at w. A strictly positive gate link is never knife-edge. So an accepted kink triangle of strict gate links cannot be completed. This agrees with the referee's Theorem K′.
   - *The exact-tie case of PP51 Thm 5.1 (Prop 2.2).* Here the three effective constant vectors are collinear, and all three models are exactly indifferent a.e. on both certificate cells, with exactly opposite price vectors. A non-conic balanced silencing F then has zero gate value at every world, for A and for B. Under zero-accepting gates, A is all-world tied with the incoherent model A[F ↦ S], so direct (C) fails. Under strict gates, A is not defended against that model.
2. **Without sections, no single-world tie is essential (§3; CHECKED, agreeing with PP56 Thm L).**
   - I ran the audit's exact closure procedure on the kink's actual cells: rules I–IV, disjunctive defences for A, B and D, the audit's protection encoding, both certificate cells twin-split, and the value −h for pads.
   - It closes cleanly with ties allowed and with ties forbidden, under every world order tried. The closures are **inert**: no reverse comparison is ever installed. An independent verifier confirms them.
   - The rule behind these closures is a **priority of the "below" cell at world 1**. This is the cell-level shadow of PP56's lexicographic relation Λ.
3. **The decisive new result: sections turn the operative indifference into an incoherent all-world tie (§4, Theorem Q; PROVED).**
   - Suppose a relation accepts the strict part of some additive, strictly guiding first-level field Φ out of selected models. This is true of Λ and of any tie-breaking of Λ.
   - Suppose its fixed-rival sections are closed at a single member C_a.
   - Then C_a ⪯_w X at every world w for every X with Φ_w(C_a → X) = 0. The forcing sequences are **pure likelihood shifts** a∘(1 + t e_w), which make C_a strictly better at w. So these are actual section sequences with a fixed rival.
   - If some other member C_b disagrees with C_a on a non-conic set F whose Φ-increment is zero at all three worlds, then the incoherent model C_b[F ↦ C_a] is weakly no worse than C_b at all three worlds. Direct (C) fails.
   - For Λ, F is the kink's own balanced swap: equal |g|-mass on the "above" and "below" cells, between A = u and B (or D).
4. **What PP56 Prop 5.1's open section looks like, and why single-world ties do not help there (§4.3; PROVED).**
   - Take the balanced swap F and any world w. Exactly one of the following is open:
     - the section at u for the rival A[F ↦ S];
     - the section at B for the rival B[F ↦ h].
   - Closing the open one at w makes a tie at w. Every world has an open one, so closing all of them needs ties at all three worlds at once. That is precisely the forbidden incoherent all-world tie.
   - So single-world ties are not the lever. Sections force the tie at all three worlds simultaneously.
5. **Local milestone: NOT achieved (§5).**
   - **The exact obstruction** is Theorem Q.
   - **It is not axiom-level.** It uses hypothesis (L0⁺): the strict part of an additive first level is accepted out of members.
   - **What survives is an axiom-level constraint.** Refusals at a member propagate to its w-improving likelihood shifts (Lemma 5.1).
   - **The resulting dilemma (§5).**
     - Λ-type lexicographic first levels fail sections (Theorem Q).
     - A single additive level that defends A, B and D on its own must be in the kink's tie case (Cor 4.4, conditional). Theorem Q then applies.
   - **What any successful rule must therefore have:** a first level that is neither lexicographic nor additive. Its strict preferences out of slightly improved members must sometimes be refused. §5 states this precisely as the target.

| Item | Result | Label |
|---|---|---|
| Tie–pad lemma (PP19 Thm 1 for any tied pair) | Lemma 2.1 | PROVED |
| Strict gate triangles cannot be tie-completed | Cor 2.1′ | PROVED |
| Exact-tie case of the kink inside gates: collinearity, opposite prices; (R0) incoherent all-world tie, (R) no defence | Prop 2.2 | PROVED (uses PP51 Lemmas 2.1, 2.3 and its CHECKED (K2)) |
| Closure engine on kink cells: clean with and without ties, inert | §3.1 | CHECKED |
| Extracted cell rule: the "below" cell has priority at world 1 | §3.2 | CHECKED (on the instance) |
| Pure likelihood shifts are strict w-improvements | Lemma 4.1 | PROVED; CHECKED (`shift57.out`) |
| Theorem Q: sections plus (L0⁺) plus a null non-conic piece give a direct-(C) failure | Thm 4.2 | PROVED |
| Λ-type relations: no tie-breaking closes sections | Cor 4.3 | PROVED |
| An additive level that defends A, B and D alone is in the tie case | Cor 4.4 | PROVED under strict (K2) for weak inequalities (otherwise CONJECTURE) |
| Open-section dichotomy per world | Prop 4.5 | PROVED |
| Refusals inherit along w-improving shifts | Lemma 5.1 | PROVED (axiom-level) |
| Existence of a rule with closed sections on N_u | — | OPEN |

---

## 1. Setting

This is BRIEF53's setting.
- Three worlds; Gaussian μ; the four-advice domain; ranks 0 < 1 < 2 < 3.
- T = D_M at ε = 3/10.
- Posterior family C_a = D_{M_a}, with index = likelihood, on a closed 2-D neighbourhood N_u of u containing the kink triple A = u, B = (406, 421, 373)/1200, D = (406, 373, 421)/1200.
- Every index is interior, so supp a = {1, 2, 3}.
- On the disagreement region the family is two-valued: each member says the common answer h(g) or S.

Encoding (audit, binding):
- **Defence:** ⋁_w [C_a ⪯_w X].
- **Undominatedness:** (⋀_w [X ⪯_w C_a]) ⇒ (⋀_w [C_a ⪯_w X]).
- **Direct (C):** an incoherent X must be refused at some world; a coherent X is refused somewhere or tied at all worlds.
- **Sections:** only through actual sequences with a fixed rival (M6 of PP59).

**The certificate cells** (CHECKED, `geom57.out`; 76 cells, 31 types):
- **Ep ("above")**: A answers h alone, h wrong only at world 1 (class Maj₁).
- **Em ("below")**: A answers h alone, h right only at world 1 (class Min₁).

B and D are silent on both cells.

---

## 2. The gate side: ties need knife-edges

**Lemma 2.1 (tie–pad lemma; PROVED).** Suppose X ⪯_w Y and Y ⪯_w X. Then:
- (a) X ⋠_w W for every W that is pointwise no worse than Y at w and strictly better on a non-null set;
- (b) U ⋠_w X for every U that is pointwise no better than Y at w and strictly worse on a non-null set.

The same holds with X and Y exchanged.

*Proof.*
- (a) Suppose X ⪯_w W. Then Y ⪯ X, X ⪯ W and W ⪯ Y, the last by guidance. (TC) gives Y ⪯_w W, which reverses a strict guidance comparison.
- (b) Suppose U ⪯_w X. Then X ⪯ Y, Y ⪯ U (guidance) and U ⪯ X. (TC) gives U ⪯_w Y, which again contradicts strict (G). ∎

PP19 Thm 1 is the special case Y = T, X = C_p. In record form, a tie on r = rec(X → Y) at w forbids at w every **improving pad** of r: the new side improved at w on any extra non-null set, inside or outside the support.

**Corollary 2.1′ (PROVED).** Suppose a link of an accepted triangle at w is *w-robust*: some strict improving pad of it is also accepted at w. Then completing that triangle is F1.

In gate unions, a link with strictly positive gate value is w-robust, because gate values are integrals and change continuously under small pads. PP51 Thm 5.1 with REFEREE_round50 Thm R1(ii) produces, for the kink, an accepted triangle of three such links. So **keeping gate acceptances, the kink has no tie completion.** This is the referee's Theorem K′, reached by a different route.

**Proposition 2.2 (the exact-tie case of the kink inside gates; PROVED).** Take PP51's setting with its gap hypothesis: weak own-Bayes for A, and CG2 non-strict on the two certificate cells. Use the triple constants ω^N, with z^N as in PP51 Thm 5.1, and assume the CHECKED strict (K2) orders z^B_2 > z^A_2 > z^D_2. Suppose the configuration survives. Then:
- (i) z^A lies on the segment [z^B, z^D];
- (ii) at a.e. point of Ep ∪ Em, Q^A = Q^B = Q^D = P(g) at every world;
- (iii) σ∘P(g) = κ(g)ν on Ep and −κ′(g)ν on Em, for one fixed vector ν ∈ O(−,+,+) orthogonal to every ω^N.

Hence, for any non-conic F = F⁺ ∪ F⁻ with F⁺ ⊆ Ep, F⁻ ⊆ Em and ∫_{F⁺} κ = ∫_{F⁻} κ′:
- the gate values Φ^A_w(F : h → S) and Φ^B_w(F : S → h) vanish at every world;
- under (R0), A is all-world tied with the incoherent A[F ↦ S], so direct (C) fails;
- under (R), neither guidance nor any of the triple's gates accepts A's record at any world. So within the triple, A is undefended against it. (In a 2-D family, other gated members that answer on F would also have to be checked.)

*Proof.*
1. **The two forms.** PP51 Lemma 2.3 (⇒, weak form) at g⁺ ∈ Ep and g⁻ ∈ Em gives positive linear forms ℓ, ℓ′ with ℓ(z^A) ≥ θ ≥ ℓ(z^B), ℓ(z^D) and ℓ′(z^A) ≤ θ′ ≤ ℓ′(z^B), ℓ′(z^D).
2. **The segment point.** Let S ∈ [z^B, z^D] have S_2 = z^A_2.
   - If S_3 < z^A_3, then ℓ′(S) < ℓ′(z^A) ≤ θ′ ≤ ℓ′(S), a contradiction. So S_3 ≥ z^A_3.
   - Then ℓ(S) ≥ ℓ(z^A) ≥ θ ≥ ℓ(S). So S = z^A, and every inequality is an equality, at both points.
3. **Pointwise equalities.** Lemma 2.3's chain σ·(P∘ω^N) ≷ σ·E^N is termwise. With ω^N > 0 (two-signedness K3), equality forces Q^N_w = P_w for all three models and all w.
4. **The vector ν.** Each n(g) = σ∘P(g) is orthogonal to the three ω^N. These span a plane, since the z^N are collinear and distinct. So n(g) ∈ ℝν, and its sign pattern fixes the orientation on each cell.
5. **Gate values.** Φ^A_w(F) = ω^A_w ν_w (∫_{F⁺} κ − ∫_{F⁻} κ′) = 0, and likewise for B. A[F ↦ S] differs from A on a non-conic set, so it is incoherent (Lemma H). ∎

So the "operative freedom" the referee identified, exact indifference on both cells, **comes with a ready-made incoherent all-world tie partner** inside the gate architecture. Λ escapes this because its later levels break the tie (PP56). Section 4 shows that closed sections remove that escape.

---

## 3. Axiom level without sections: a different completion, with no ties

### 3.1 Exact closure runs (CHECKED; `run57a.out`, `verify57.py`)

**Instance.**
- Atoms: one representative cell per type (31 types), with Ep and Em twin-split into non-conic halves. That gives 33 atoms.
- Coherence: PP21's exact polygon test. Twin-splitting models are incoherent.
- Rivals: A, B or D, changed arbitrarily on the four twin atoms with values in {h, −h, S}. That gives 243 rivals.
- Obligations: defence of each of A, B and D against every rival, kept **disjunctive** (DFS over worlds).
- Protection: P = {A, B, D} with rules III and IV, so an incoherent all-world tie partner is F2.
- No-ties mode adds F3: an installed record whose reverse is accepted at the same world.

**Result.**

| mode | world orders | outcome | installed records / world | ties | reverses installed by rule II |
|---|---|---|---|---|---|
| ties allowed | 123, 231, 312 | clean | 485 / 115 / 0 (cyclically) | 0 | 0 |
| ties forbidden | 123, 231, 312 | clean | same | 0 | 0 |

`verify57.py` re-derives (G), (TC) (PP21 Lemma 2.1's pair criterion, coded independently), defence and protection from the definitions: 0 errors in both modes.

A larger window adds the pair cells B_13 and D_12 (values {h, S}; 972 rivals; greedy, `run57b_2.out`). It also closes cleanly with ties allowed and with ties forbidden: 0 stuck obligations, 0 ties, |P| = 3, re-verified with 0 errors. Records per world are 2264 / 348 / 6.

### 3.2 The rule behind the table (CHECKED; `rule57a.out`)

I tested statements of the form "a record whose part on region R is a non-null weak w-worsening is accepted at w":

| R | world 1 | world 2 | world 3 |
|---|---|---|---|
| Em ("below") | **holds** (351 records, 0 exceptions) | fails (33/135) | fails (123/135) |
| Ep ("above") | fails | fails | fails |

So the clean completion is: **at world 1, keeping A's below-cell answers outweighs any amount of above-cell change.** A defends every mixed silencing of Ep ∪ Em at world 1. B and D defend the corresponding answering moves at world 2 (or 3), where A's reverse is refused.

This is a mass-free priority, the cell shadow of a lexicographic first level. It is exactly Λ's behaviour at the field tie of PP56 §2.3. Λ is the measurable version, with balanced level 0 and box tie-breaks (PP56 Thm L: every non-section clause holds on all of N_u, for all measurable rivals, with no ties).

### 3.3 The audit's four questions, without sections

1. **Essential single-world ties:** none. The clean closures use no ties, and the no-ties runs are clean (here and PP56 Thm L).
2. **Reverse comparisons that abandon old-side realisers:** none in the cell closures, which are inert. In Λ they arise only from totality (PP56 §4.2).
3. **Refusals that preserve protection:** in the cell closures, A's reverse is refused at world 1 and B's/D's at world 2. In Λ, the protecting world is the positive coordinate of the first nonzero level.
4. **Arbitrary splits and common-context copies:** yes for Λ (Thm L).

**Sections change all four answers (§4).**

---

## 4. Sections: Theorem Q

**Hypothesis (L0⁺).** For each world w there is an integrable, strictly guiding field ℓ_w (|ℓ_w(g, x)| ≤ K|g|, strictly increasing in the w-rank). With Φ_w(X → Y) := ∫ [ℓ_w(g, Y(g)) − ℓ_w(g, X(g))] dμ, the relation satisfies

  C_b ⪯_w Y whenever Φ_w(C_b → Y) > 0, for selected C_b.

Λ satisfies (L0⁺) with ℓ = its level 0, and so does every relation obtained from Λ by changing only how level-0 ties are broken. Nothing else about the relation is assumed: no transitivity, no completeness, no gates.

**Lemma 4.1 (pure likelihood shifts; PROVED; CHECKED `shift57.out`).** For interior a and t > 0, put b = a∘(1 + t e_w), normalised. Then C_b is pointwise no worse than C_a at w. It is strictly better on a non-null set.

*Proof.*
- For each vertex m_v, Σ_i b_i m_{v,i} h_i = Σ_i a_i m_{v,i} h_i + t a_w m_{v,w} h_w (up to the positive normalisation), so the sign changes only in the direction of sign(h_w).
- Where h_w > 0, C_b answers wherever C_a does, so it only gains w-correct answers.
- Where h_w < 0, it only loses w-wrong answers.
- The boundary planes move, so the change set is a non-null cone.

`shift57.out` confirms, for a ∈ {A, B, D}, w = 1, 2, 3 and t = 1/1000, exactly 0 cells where C_b is w-worse and 12 where it is strictly w-better. ∎

**Theorem 4.2 (Q; PROVED).** Assume (L0⁺). Let a be interior in N_u, and suppose the fixed-rival sections at a are closed.
- (i) For every world w and every model X with Φ_w(C_a → X) ≥ 0, C_a ⪯_w X.
- (ii) Suppose another selected C_b and a non-null set F ⊆ {C_a ≠ C_b}, not a.e. a cone, have Φ_w(F : C_a → C_b) = 0 for w = 1, 2, 3. Then the incoherent model Y := C_b[F ↦ C_a] satisfies Y ⪯_w C_b at every world. So direct (C) fails for C_b.

*Proof.*
- (i) Take b_k = a∘(1 + t_k e_w), with t_k ↓ 0. By Lemma 4.1 and strict guiding, Φ_w(C_{b_k} → C_a) > 0, and additivity of the integral gives Φ_w(C_{b_k} → X) = Φ_w(C_{b_k} → C_a) + Φ_w(C_a → X) > 0. By (L0⁺), C_{b_k} ⪯_w X for every k, with the same rival X throughout. The closed section {a′ : C_{a′} ⪯_w X} contains a.
- (ii) Put X := C_a[F ↦ C_b]. Then Φ_w(C_a → X) = 0 at every w, so by (i), C_a ⪯_w X at all three worlds. By (IB), rec(C_a → X) = (F : C_a → C_b) = rec(Y → C_b). So Y ⪯_w C_b at every world. Y differs from the coherent C_b exactly on F, which is non-conic, so Y is incoherent (Lemma H). ∎

Only one member's sections are used. Neither single-world ties nor (TC) enter.

**Corollary 4.3 (Λ cannot be repaired by changing its tie-breaks; PROVED).** Every relation that agrees with Λ's level-0 strict verdicts out of members, with any tie-breaking at all, fails closed sections or direct (C).
- Take F = F⁺ ∪ F⁻ with F⁺ ⊆ Ep and F⁻ ⊆ Em radial slabs of equal |g|-mass (atomless).
- Λ's level-0 increments of h → S are (−2, 1, 1)|g| on Ep and (2, −1, −1)|g| on Em (CHECKED, `shift57.out` (2)). So Φ(F : A → B) = 0 at every world.
- Apply Theorem Q at a = u: the incoherent B[F ↦ h] is weakly no worse than B at every world.
- Applying it at a = B gives the same failure for A, with A[F ↦ S].

**Corollary 4.4 (any additive level that defends the triple alone; PROVED under the stated hypothesis).** Suppose the relation is sandwiched: {Φ_w > 0} ⊆ R_w ⊆ {Φ_w ≥ 0} on comparisons out of members, for one additive field Φ. Then:
- defence makes each of A, B and D weakly λ-Bayes for Φ (PP42 Thm 2.1 "⇒", confirmed in REFEREE_round50 §1.1);
- a single field is a gate system with a common field and CG2 holding with equality.

If the strict (K2) orders also hold for the effective weights, then Prop 2.2's steps 1–4 apply. They give opposite price vectors on Ep and Em, hence a null non-conic F, hence Theorem Q.

**OPEN:** whether strict (K2) persists when CG2 holds only with equality. If it fails, a degenerate case z^B = z^A has to be handled separately.

### 4.3 What PP56 Prop 5.1's open section looks like

**Proposition 4.5 (PROVED).** Let R be Λ, or any relation satisfying (L0⁺) whose worlds are linear orders with no ties (as Λ's are). Fix the balanced swap F and a world w. Then exactly one of the following holds:
- (α) A ⋠_w A[F ↦ S], and the section at u for this rival is open: it contains every pure shift u∘(1 + t e_w);
- (β) B ⋠_w B[F ↦ h], and the section at B for that rival is open, in the same way.

*Proof.*
- The two records are mutual inverses: (F : h → S) and (F : S → h). A linear order without ties accepts exactly one of them at w.
- Theorem Q(i)'s sequence accepts at every shift on both sides.
- So at w the refused side is open. ∎

**Answer to the coordinator.** The open section sits on the kink's own balanced swap of the two certificate cells, along the pure likelihood shift toward e_w. A single-world tie at w closes the section at w and only there. Every world has one open section, so closing them all is an all-world tie between A (or B) and an incoherent swap. **Single-world ties do not help: the section limit demands the tie at all three worlds at once.** The comparisons forced along the way all have coherent old-side realisers (A on one side, B on the other), so abandoning realisers plays no role in this failure.

Neither does rule (TC)-completion help. Theorem Q uses no (TC) step, so no reverse or tie rule elsewhere can undo it. A repair has to **refuse** some of (L0⁺)'s strict acceptances out of shifted members.

---

## 5. The measurable construction attempt, and the obstruction

**Target (audit).** A relation on N_u with (G), (IB), actual (TC), defence, undominatedness, direct (C) and closed fixed-rival sections, against all measurable rivals. The local milestone. **Status: not achieved.**

**What I tried, in order.**
1. **Gate union with tie completion.** It fails by Cor 2.1′; in the tie case by Prop 2.2.
2. **The cell rule of §3.2 (absolute priority of Em at world 1), extended measurably.** On cells, masses are invisible, so the rule must be given a mass dependence before it means anything measurably. The two canonical choices are:
   - additive (finite relative weights), which is a first-level field and falls under Cor 4.4 and Theorem Q;
   - lexicographic, which is Λ's form and falls under Cor 4.3.

   I did not settle whether a mass-free region priority meets (L0⁺) along the pure-shift sequences. Its section behaviour is OPEN. (I first tried the segment u → B at world 2. That attempt is invalid, because the extracted rule has no Em-priority at world 2: `rule57a.out`.)
3. **Λ with modified tie-breaks**, as the coordinator asked. It fails by Cor 4.3, whatever the tie-breaks.
4. **Closing Λ's sections by adding the limit acceptances** (the minimal section-closing modification). By Theorem Q(i) this adds exactly the level-0-null comparisons out of every member at every world. That yields the incoherent all-world tie of Q(ii).
   - Note on (TC) for this modification (PROVED): every triangle of the modified relation has all its links level-0-null. Level-0 increments are additive and nonnegative on every accepted link, so they sum to zero. So no strict guidance link ever lies on such a triangle, and completion never produces F1.
   - So the modification fails at protection only, never at (TC). This is the precise sense in which the obstruction is direct (C), not transitivity.

**Is the obstruction axiom-level? No.**
- Theorem Q needs (L0⁺) on the shift sequences.
- The axioms alone do not force C_{b_k} ⪯_w X, because defence is disjunctive and the record rec(C_{b_k} → X) is mixed at every world.
- What the axioms do force is the following.

**Lemma 5.1 (refusals inherit along improving shifts; PROVED, axiom-level).** With closed sections, if C_a ⋠_w X, then C_{a∘(1+t e_w)} ⋠_w X for all small t > 0, although these members are strict w-improvements of C_a (Lemma 4.1).

*Proof.* A section's complement is open in N_u. ∎

**The resulting dilemma, stated precisely.**

A rule with closed sections must satisfy: whenever a member refuses X at w, slightly w-improved members also refuse X at w. Two natural kinds of first level conflict with this.
- **Lexicographic first levels (Λ and its tie-breaks).** Improvement at level 0 always wins. Sections fail (Cor 4.3, Prop 4.5).
- **Purely additive levels that defend the members by themselves.** They are pushed by the kink into its tie case. Then (L0⁺) and Theorem Q give an incoherent all-world tie (Cor 4.4, conditional on strict (K2)). Strict uniqueness is excluded by PP51 Thm 5.1 / Theorem K′.

So any successful rule needs a first level that is **neither**: it must refuse some comparisons out of w-improved members that its own first-level increments favour. One way to say this is that verdicts must depend on the rival's improvement relative to the member, in a way that is not additive across the shift wedge and the rival's own change.

**Nearby reachable aims** (per the standing preference to move the aim rather than stop at the impossibility):
- **(a) The axiom-level form of Theorem Q.** Replace (L0⁺) by its consequence actually needed: acceptance at w along the pure-shift sequence for the single rival C_a[F ↦ C_b]. Then ask, with PP56 §5.3's question, whether the non-section clauses force that acceptance for a **two-parameter** family of balanced swaps. Prop 5.2 of PP56 shows one parameter is not enough. Theorem Q identifies the right rivals and the right sequences: pure shifts, and the Ep/Em balanced swap.
- **(b) A first level that is null on no non-conic piece of any member pair.** Theorem Q(ii) then has nothing to bite on, and Q(i) is harmless. For additive levels this means strict pairwise Bayes separation of every member pair. By Cor 4.4 that is excluded on the kink triple for a single field. Per-pair separating fields are the gate architecture again. So (b) needs a **non-additive** level whose null set contains no member-to-member swap. **CONJECTURE (target):** such a level can be built from per-member strict fields combined by a rule that is closed along pure shifts. It need not be closed along arbitrary mass paths (PP52 Thm 4.1's extra hypothesis, which the referee confirms is not an axiom).
- **(c) A one-parameter milestone.** On a segment through u avoiding one of B and D (so the pair has no balanced piece), Theorem Q(ii) is vacuous. The milestone may be reachable there, but it is not the audit's 2-D target.

---

## 6. The four questions, with sections

| Question | Without sections | With closed sections |
|---|---|---|
| 1. Essential single-world ties | none (§3; PP56 Thm L) | single-world ties are **insufficient**: the forced limit acceptances tie A (or B) with an incoherent swap at **all three** worlds (Prop 4.5) |
| 2. Reverses that abandon old-side realisers | none needed (inert closures); Λ's are for totality only | irrelevant: the forced comparisons all have coherent realisers (A, B) |
| 3. Refusals that keep protection elsewhere | the first nonzero level's positive world (Λ); world 1 versus world 2 (cells) | none can, for the balanced swap under (L0⁺): each world's refusal sits on an open section |
| 4. Survive measurable splits and common-context copies | yes (Thm L) | no: Theorem Q uses one measurable non-conic split and one (IB) identification |

Referee note (2) does not affect these results: the local construction theorem is not used. Note (5) does not either: radial transport is not used.

---

## 7. Scripts (`r9/PP57_py/`; run `python3 -I -B <script>` inside the folder)

| Script | Content | Label |
|---|---|---|
| `geom57.py` | exact cells of the kink triple (PP51's enumerator `post51.py`, copied unchanged) | CHECKED |
| `space57.py` | 33-atom instance: Ep/Em twin-split; exact coherence (PP21 `cells.is_coherent`) | library |
| `engine21.py` | PP21 closure engine, unchanged except an optional no-ties failure F3 | library |
| `search57.py` | disjunctive-defence DFS and greedy search over worlds | library |
| `run57a.py` → `run57a.out` | §3.1: ties allowed / forbidden × three world orders, all clean; re-verified | CHECKED |
| `verify57.py` | independent check of (G), (TC) pair criterion, defence, protection | library |
| `analyse57a*.py`, `rule57.py` → `rule57a.out` | §3.2: rule extraction | CHECKED |
| `run57b.py` → `run57b_2.out` | larger window with pair cells B_13, D_12 (greedy): clean in both modes, 0 ties, re-verified | CHECKED |
| `shift57.py` → `shift57.out` | Lemma 4.1 for a ∈ {A, B, D}, w = 1, 2, 3; Λ's level-0 increments on Ep, Em | CHECKED, ALL PASS |

**Most important next step.** Do aim (a). Fix the balanced swap rivals C_a[F ↦ C_b] for a 2-parameter family of pairs near (u, B) and the pure-shift sequences. Then test, with the closure engine extended by explicit M6 section clauses, whether the non-section axioms force acceptance along those sequences. A yes is the first axiom-level obstruction in the module. A no gives the shape of the non-additive first level needed for aim (b).
