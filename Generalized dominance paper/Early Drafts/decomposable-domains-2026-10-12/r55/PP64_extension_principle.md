# PP64. A commitment-based extension principle: definitions, the final-system theorem, and the first nontrivial extension

23 October 2026. Constructor, Brief 55. One author; not refereed. §1 was posted first as a draft for PP65. It is unchanged in substance; the refinements are marked [R]. Takes in the coordinator's relays of PP66 and of REFEREE_round54: its invariant (C⁺) and its sharpening of Cor E.2(ii).

**Labels.**
- PROVED: complete argument here, or a cited result used within its stated hypotheses.
- CHECKED: exact rational computation in `r9/PP64_py/geom64.py` on sample problems (output `geom64.out`, ends ALL PASS). Every CHECKED claim that is also stated as PROVED has its own proof; the check is a guard against slips.
- CONJECTURE / OPEN: as stated.

No axiom is added. Two design choices are named where they enter: the provisional selection Ĉ (§3) and the policy of refusing carrier-free records at the end (§2).

---

## 0. Verdict

1. **The partial system, invariant and operation are written down (§1).** Every clause of the invariant 𝓘 is *finitely refutable*. The one exception, "every refusal at a selected source is covered by a reservation", has permanent witnesses.
2. **Final system (Theorem 2.3; PROVED).** Take the union of any chain of partial systems satisfying 𝓘. Suppose every index is assigned and every record carried by a selected model is decided. Refuse the remaining records, which are carrier-free (Lemma 2.2). The result satisfies every axiom:
   - reflexivity, strict (G), (IB) and (TC);
   - (S), with closed sections;
   - (LA);
   - **global** (C).

   Moreover, the registered class P is exactly the class of undominated models.
   - **How global (C) is discharged.** Commitments only grow, so an all-world tie in the final relation consists of six acceptances that are present together at some stage, and rule IV registered the tie partner there. KKM then puts every undominated model in such a tie with a selected model.
   - The audit's caution about decreasing limits does not arise. Closed sections come from the reservations, not from a continuity argument at the limit.
3. **Extension lemma (§3).**
   - **Hypothesis H\*.** "Σ is tame along a provisional selection Ĉ". It has four checkable clauses: reservation compatibility; defence slack; copy-closure along Ĉ; closure-cleanliness.
   - **(A) Assignment is free (PROVED).** Under 𝓘 + H\*, assigning any index p with C_p := Ĉ_p needs no new reservation and preserves 𝓘 + H\*.
   - **(L) Limits (PROVED).** 𝓘 + H\* pass to unions of chains, provided each index's provisional value is revised only finitely often.
   - **(B) Settling a record.** This is reduced to an exact criterion (Prop 3.3; PROVED): the acceptance is closure-clean, **or** a copy-closed *spread system* of reservations with slack exists.
   - **What remains is Conjecture 3.4:** one of the two is always available, after co-design (a revision of Ĉ off the assigned set). Four failure configurations are named.
   - **Conditionally (PROVED):** stage-0 tameness together with Conjecture 3.4 gives T1 a full cover.
4. **First nontrivial extension (§4; PROVED, geometry CHECKED).** Rival X_E = T[E ↦ +] on edge {1, 2}; the defender is chosen jointly with its index.
   - **Forced for every edge defender D (Lemma 4.1).**
     - D is face-admissible, so it answers + on all of E.
     - Every world w ∈ {1, 2} at which D defends against X_E forces, by (TC), refusals at u of a whole family of *partial D-rivals* T[H′ ↦ D], each with a reservation.
   - **Joint choice criterion (Prop 4.2).** Choose D weakly 3-worse than T, for instance the −e₃ edge posterior at p = (½, ½, 0). Then:
     - T's induced obligations are all discharged by guidance at world 3;
     - D's refusal of X_E at 3 is forced by guidance.
   - **Σ₁ (Theorem 4.3).** It is explicit, satisfies 𝓘, and exhausts no face obligation.
   - **The switch (Prop 4.4).** It is forced strictly between u and p: there is an index whose model weakly dominates X_E at all three worlds.
   - **A new phenomenon: copy transport (Lemma 4.5).** By (IB), T's double refusal (1, 2) is carried along pure-shift rays to every later source on the ray. The {1, 2} edge is never reached, because face-admissible edge models answer on E (E-anchoring).
5. **Balanced swap as an adversarial instance (§5).** The step passes. It uses PP66's local move: the inverse pair is incomparable at w, and the ends are defended at v and v′. Theorems Q and E are respected exactly where they apply. The Lemma S splits are settled by refusing **carrier-free** links, which cost no slack.
6. **Two-neighbourhood test (§6).** The operation is not rejected. The sharper test, a rival balanced for the system's own commitments and chosen after them, is exactly Conjecture 3.4.
7. **Success criterion (§7). Partly met.**
   - The passage to the final system is PROVED.
   - Assignment of new defenders is PROVED free once tameness holds.
   - Handling the *next arbitrary rival* is reduced to the settling Conjecture 3.4, which is **not** proved. I do not claim more.

| Item | Result | Label |
|---|---|---|
| Partial system, invariant, operation | §1 | definitions |
| Unions preserve 𝓘 | Lemma 2.1 | PROVED |
| Carrier-free records may be refused at the end | Lemma 2.2 | PROVED |
| Final system: all axioms, global (C), P = undominated class | Thm 2.3 | PROVED |
| Assignment along a tame Ĉ is free | Prop 3.1 | PROVED |
| Tameness passes to limits (finite revision) | Prop 3.2 | PROVED |
| Exact criterion for settling a record | Prop 3.3 | PROVED |
| Settling always possible after co-design | Conj 3.4 | CONJECTURE |
| Conditional existence of a cover | Thm 3.5 | PROVED (conditional) |
| No fixed-oracle invariant | Remark 3.6 | PROVED given PP57 Thm Q |
| Edge defender: forced structure | Lemma 4.1 | PROVED |
| Edge posterior is weakly 3-worse than T | Lemma 4.2 | PROVED; CHECKED |
| Explicit Σ₁ satisfying 𝓘 | Thm 4.3 | PROVED |
| Switch: all-world weak dominator of X_E strictly between | Prop 4.4 | PROVED |
| Copy transport along pure-shift rays; E-anchoring | Lemma 4.5 | PROVED; CHECKED |
| Balanced-swap step | Prop 5.1 | PROVED (step level) |
| Guidance-spread slack lemma | Lemma 3.7 | PROVED |

---

## 1. Definitions (posted as draft; [R] = refined)

### 1.1 Objects
- **Models and worlds.** Problems g are taken modulo sign, with Gaussian μ. Models are measurable four-advice maps modulo null sets. W = {1, 2, 3}.
- **Weak and strict betterness.** X is *weakly w-better* than Y if rank_w(X(g)) ≤ rank_w(Y(g)) a.e. It is *strictly* w-better if, in addition, the inequality is strict on a non-null set.
- **Records.** r = rec(X, Y) = (supp r = {X ≠ Y}, old = X|supp, new = Y|supp). Its inverse is r⁻¹ = rec(Y, X).
- **Carriers.** A model Z *carries* r if Z = old(r) a.e. on supp r. Then Z ⊕ r := Z[supp r ↦ new(r)], and rec(Z, Z ⊕ r) = r.
  - (IB) is built in: every verdict is a function of (record, world).
  - [R] A record is *carrier-free* (relative to a selection) if no selected model carries it.
- **Coherence and faces.** Coherent models are the D_K. C is *face-admissible at p* if C = D_K with K ⊆ Δ_{supp p}. This is necessary for competitiveness under strict (G) (AUDIT_section_topology §1).

### 1.2 Partial system Σ = (D, C, Acc, Ref, Res, P)
- **Assigned indices and models.** D ⊆ Δ, with u ∈ D. C: D → coherent face-admissible models, with C_u = T = T1. Committed models never change.
- **Committed verdicts.** Acc_w and Ref_w are disjoint sets of records. Every other (record, world) pair is UNASSIGNED; unassigned does not mean refused.
- **Reservations.** Res is a set of triples ρ = (U, X, w) with U ⊆ Δ open. Meaning: every C_q with q ∈ U, assigned now or later, satisfies C_q ⋠_w X.
- **Registration.** P is the set of registered models, which must be coherent and undominated.
- **Derived sets.**
  - Rz_q(X) := {w : ∃(U, X, w) ∈ Res with q ∈ U};
  - O_w(X) := ∪{U : (U, X, w) ∈ Res}, which is open;
  - F_w(X) := Δ ∖ O_w(X), which is closed.
- **Provisional data.** These are not part of Σ and are freely revisable: a provisional selection Ĉ (§3), intended worlds and intended radii.

### 1.3 Pending obligations, kept as explicit disjunctions
- **Def(p, X)** = ⋁_{w ∈ supp p} [C_p ⪯_w X], for every p (assigned or not) and every X. Its live disjuncts are supp p ∖ Rz_p(X).
- **Prot(N, X)**, for N ∈ P: ⋀_w [X ⪯_w N] ⇒ ⋀_w [N ⪯_w X].
- **DirC(N, X)**, for N ∈ P: an all-world tie with N ⇒ X is coherent, and then X ∈ P.
- **Face(p):** C_p is face-admissible.

### 1.4 The invariant 𝓘(Σ)
- **(I1)** Reflexivity and guidance are committed: ∅ ∈ Acc_w; every record whose old side is weakly w-better is in Acc_w; every record whose new side is strictly w-better is in Ref_w.
- **(I2)** (TC)-closure: if rec(A, B), rec(B, C) and rec(C, A) are all in Acc_w, so are their three inverses.
- **(I3)** Protection closure (rule III): N ∈ P and rec(X, N) ∈ Acc_w for every w ⇒ rec(N, X) ∈ Acc_w for every w.
- **(I4)** Registration of ties (rule IV): N ∈ P and X ≈ N by committed acceptances ⇒ X ∈ P.
- **(I5)** P consists of coherent models; T ∈ P; C(D) ⊆ P.
- **(I6)** Reservations are honoured: (U, X, w) ∈ Res and q ∈ D ∩ U ⇒ rec(C_q, X) ∈ Ref_w.
- **(I7)** Refusals are covered: q ∈ D and rec(C_q, X) ∈ Ref_w ⇒ w ∈ Rz_q(X). This applies to every assigned carrier of every refused record, that is, to all (IB) copies.
- **(I8)** KKM slack: for every X, (F₁(X), F₂(X), F₃(X)) is a closed KKM cover of Δ (Δ_J ⊆ ∪_{w∈J} F_w(X) for every face J). Equivalently, supp q ⊄ Rz_q(X) for all q and X.

For q ∈ D, (I6) and (I7) give Rz_q(X) = {w : rec(C_q, X) ∈ Ref_w}. So a selected source's section literals are refused **exactly** on its reserved worlds.

### 1.5 The extension operation
One step does one of the following:
- (a) ASSIGN a coherent face-admissible C at p ∉ D. The defender is an output: any coherent model may be chosen.
- (b) SETTLE an unassigned (r, w) as A or R.
- (c) RESERVE (U, X, w).
- (d) RESOLVE Def(p, X) by settling C_p ⪯_w X as A.

Then close the result:
1. **Reservations for new refusals.** Every new refusal at an assigned carrier receives a reservation (V, X′, w) with V ∋ p. This covers (IB) copies, and in case (a) also the reservations already in force at p. Every assigned q ∈ V then has its record refused. That record may have further carriers: this is the **copy cascade**.
2. **Closure.** Close under (I2)–(I4).
3. **Acceptance test.** Accept the step only if all of the following hold:
   - no record is both A and R;
   - there is no F1 (a forbidden guidance reverse) and no F2 (an incoherent registered model);
   - (I8) holds;
   - the **germ condition** holds: each new refusal of (X, w) at an assigned p has p ∉ cl(D ∩ {q : rec(C_q, X) ∈ Acc_w}).

---

## 2. Limits and the final system

**Lemma 2.1 (unions; PROVED).** The union of a chain (of any length) of partial systems satisfying 𝓘 satisfies 𝓘.

*Proof.*
- **(I1)–(I6) and (I8).** Each violation is witnessed by finitely many commitments. (I8) uses at most three reservations; the closures use at most six acceptances; (I6) uses one reservation and one assignment. These lie in a single stage, where the violation would already exist.
- **(I7).** Take a refusal and an assignment in the union. Both are present at some stage. There (I7) supplies a reservation, and reservations are permanent. ∎

**Lemma 2.2 (carrier-free completion; PROVED).** Let Σ satisfy 𝓘 with D = Δ, and suppose every record carried by some C_p is decided at every world. Refusing every undecided record at every world gives a total Σ̄ satisfying 𝓘.

*Proof.*
- **The new refusals are carrier-free.** If C_p carries r, then r = rec(C_p, C_p ⊕ r) is decided.
- **(I6), (I7).** Both concern only carried records, so they are unaffected.
- **(I1).** Weakly favourable records are already in Acc_w, so no new refusal is one of them.
- **(I2).** A (TC) violation needs three accepted links. Their inverses are already in Acc by (I2), so they are not among the new refusals.
- **(I3).** The required reverses are already in Acc by (I3).
- **(I8).** Unchanged. ∎

**Theorem 2.3 (final system; PROVED).** Let Σ̄ be total and satisfy 𝓘 (for instance, as produced by Lemma 2.2), and set X ⪯_w Y iff rec(X, Y) ∈ Acc_w. Then the relation satisfies reflexivity, strict (G), (IB), (TC), (S) on the closed simplex, (LA) and global (C). Moreover, P = C_L := {undominated models}, and all of them are coherent.

*Proof.*
- **Reflexivity, (G), (IB), (TC).** By (I1), by verdicts depending only on records, and by (I2) with disjointness of Acc and Ref.
- **(S): coherence and face-admissibility.** By construction and (I5).
- **(S): undominatedness.** If Y ⪯_w C_p for every w, then (I3) gives C_p ⪯_w Y for every w. So no domination is strict.
- **(S): competitiveness.** By (I8), some w ∈ supp p has w ∉ Rz_p(X). By (I7), rec(C_p, X) ∉ Ref_w. By totality it is in Acc_w.
- **(S): closed sections.** By (I6) and (I7), {p : C_p ⋠_w X} = O_w(X), which is open.
- **(LA).** T ∈ P.
- **Global (C).**
  - Fix any model N. The sets A_w(N) := {p : C_p ⪯_w N} = F_w(N) are closed. By competitiveness, every face Δ_J is covered by ∪_{w∈J} A_w(N).
  - By the KKM lemma there is a p with C_p ⪯_w N for every w.
  - If N is undominated, then N ⪯_w C_p at every w; otherwise C_p would dominate N. So N ≈ C_p, and (I4) gives N ∈ P.
  - Hence every undominated model is registered, so it is coherent by (I5). Conversely, members of P are undominated by (I3).
  - If N ∈ C_L and X ≈ N, then (I4) gives X ∈ P = C_L. ∎

**Remarks (the audit's limit cautions).**
1. **Increasing, not decreasing.** The audit's caution, that a coherent model may become undominated only at the limit, concerns *decreasing* refinement, where acceptances disappear. Here commitments only grow. The relevant positive facts are ties, which are six acceptances and so are witnessed at a stage. The undominated class is identified at the end by KKM (AUDIT_completion §5's registration mechanism), not by tracking undominatedness through the chain.
2. **Sections are closed by construction.** The refusal set of a fixed rival is a union of reservations. The [1/n, 1] → (0, 1] pathology cannot occur. A refusal at 0 needs a reservation, and the reservation would refuse at 1/n for large n, contradicting (I6) at the finite stage where both are present.
3. **Agreement with REFEREE_round54 §4.** [R]
   - (I3), (I4) and (I5) together are the referee's invariant (C⁺), with "registered" in place of "protected". Every all-world tie partner of a registered model is registered, coherent and, by (I3), undominated.
   - Global direct (C) is carried as an explicit obligation and discharged **only when D = Δ** (Theorem 2.3 needs a full selection for KKM). This matches the referee's finding: for *partial* systems, global (C) can fail at a limit even though every stage satisfies Rule IV (explicit counterexample, REFEREE_round54 §4).
   - The referee also confirms that committed, never-withdrawn reservations give open final refusal sets.
4. **What remains.** Everything therefore rests on *reaching* a chain whose union is total. That is the extension problem (§3).

---

## 3. The extension lemma

### 3.1 Tameness along a provisional selection

**Definition (H\*).** Let Ĉ be a coherent, face-admissible selection on Δ with Ĉ = C on D. [R] Continuity of Ĉ is not required; nothing below uses it. Σ is *tame along Ĉ* if the following four clauses hold.
- **(H1) Reservation compatibility.** For (U, X, w) ∈ Res and q ∈ U: Ĉ_q is not weakly w-better than X, and rec(Ĉ_q, X) ∉ Acc_w.
- **(H2) Slack.** For all q and X: supp q ⊄ Rz_q(X) ∪ {w : rec(Ĉ_q, X) ∈ Ref_w}.
- **(H3) Copy-closure.**
  - Let 𝓡_w := Ref_w ∪ {rec(Ĉ_q, X) : (U, X, w) ∈ Res, q ∈ U}. These are the records refused now or promised refused along Ĉ.
  - For every r ∈ 𝓡_w and every q′ such that Ĉ_{q′} carries r: w ∈ Rz_{q′}(Ĉ_{q′} ⊕ r).
- **(H4) Closure-cleanliness.** Register all of Ĉ(Δ), refuse 𝓡, and close under (I2)–(I4). The result has no F1, no F2 and no record in both Acc and Ref.

**Proposition 3.1 (assignment is free; PROVED).** Assume 𝓘 + H\*(Σ, Ĉ) and p ∉ D. Make the following assignment:
- set C_p := Ĉ_p and register it;
- commit Ref_w ∋ rec(C_p, X) for each w ∈ Rz_p(X);
- close.

This assignment needs **no new reservation**, and it satisfies 𝓘 + H\*(·, Ĉ).

*Proof.*
- **The new refusals are legitimate.** They lie in 𝓡. They are neither weak-guidance nor accepted, by (H1), and they are not accepted in the (H4)-closure.
- **(I6) at p.** By construction.
- **(I7).**
  - Every refused record carried by C_p is in 𝓡, so (H3) with q′ = p supplies the reservation.
  - Every *newly* refused record r = rec(Ĉ_p, X) is in 𝓡, so (H3) covers all of its other carriers, assigned or not.
- **(I2)–(I5).** The new closure is contained in the (H4)-closure, which is clean.
- **(I8) and (H2).** No reservation is added. A record newly in Ref_w and carried by Ĉ_q already had w ∈ Rz_q by (H3), so the set in (H2) does not grow.
- **(H1), (H3), (H4).** The (H4)-closure and 𝓡 are unchanged. ∎

**Proposition 3.2 (limits; PROVED).** Suppose that along a chain:
- every stage satisfies 𝓘 + H\*(Σ_α, Ĉ^α);
- each index's provisional value Ĉ^α_q changes only finitely often;
- changes are made only at unassigned indices.

Then the union satisfies 𝓘 + H\*(Σ_λ, Ĉ^λ), where Ĉ^λ is the eventual value.

*Proof.* (H1), (H2) and (H4) are finitely refutable, given the finitely many values Ĉ_q they mention. Take a stage at which those values have stabilised and the finitely many commitments are present. (H3) has permanent witnesses. ∎

So with tameness, defenders cost nothing to install. **All of the work is in settling records.**

### 3.2 Settling a record: the exact criterion

Fix an unassigned (r, w) that is carried by some Ĉ_q.

**Definition (spread system).** A *spread system* for (r, w) is a set 𝒱 of reservations at world w with the following properties.
- **(S1)** Every Ĉ-carrier q of r lies in some (V, Ĉ_q ⊕ r, w) ∈ 𝒱.
- **(S2)** Res ∪ 𝒱 satisfies (H3), with r added to Ref_w. This is the copy cascade, closed off.
- **(S3)** (H1) and (H2) hold for Res ∪ 𝒱.
- **(S4)** (H4) holds with the enlarged 𝓡.

**Proposition 3.3 (PROVED).** Under 𝓘 + H\*(Σ, Ĉ):
- (i) Accepting (r, w) preserves 𝓘 + H\* iff r ∉ 𝓡_w and the (H4)-closure with r added to Acc_w is clean. No reservation is needed.
- (ii) Refusing (r, w) preserves 𝓘 + H\* iff a spread system exists. In that case commit 𝒱 and refuse r together with the records rec(C_q, ·) at assigned q ∈ V.
- (iii) If r is carrier-free along Ĉ, (ii) holds with 𝒱 = ∅ whenever refusing r keeps (H4) clean. **Refusals of carrier-free records cost no slack.**

*Proof.*
- **(i).** Acceptances only add to the closure. (H1) needs r ∉ 𝓡_w, and (H4) needs cleanliness.
- **(ii).** Necessity: (I7) at future assignments, together with (H3), forces (S1) and (S2); (S3) and (S4) are clauses of H\*.
- Sufficiency: as in Prop 3.1.
- **(iii).** Immediate. ∎

**Four failure configurations (exact).** If (r, w) admits neither option, at least one of the following occurs.
- **(M1) Slack exhaustion.** Some Ĉ-carrier q of r, or some index forced by the cascade, has supp q ⊆ Rz_q(X′) ∪ R(r) ∪ {w}. Here R(r) is the set of worlds already refusing r and X′ is the corresponding copy rival.
- **(M2) Germ collision.** Every neighbourhood of a carrier q contains q′ with rec(Ĉ_{q′}, Ĉ_q ⊕ r) ∈ Acc_w, or with Ĉ_{q′} weakly w-better than Ĉ_q ⊕ r.
  - The second alternative cannot occur arbitrarily close to q when Ĉ is continuous in measure. That set is closed and misses q.
  - The first alternative can, because acceptance sets are arbitrary.
- **(M3) Unbounded cascade.** The copies are transported to a region where (M1) or (M2) holds. §4.5 shows that the transport is real.
- **(M4) Closure block of the acceptance.** Every acceptance conflict passes through a record in 𝓡. Concretely, one of the following holds:
  - a (TC) triangle whose reverse is in 𝓡;
  - rule III with a refused reverse;
  - rule IV registering an incoherent model.

**Conjecture 3.4 (settling lemma; CONJECTURE).** If Σ satisfies 𝓘 + H\*(Σ, Ĉ), then every Ĉ-carried unassigned (r, w) can be settled. This is allowed after a revision of Ĉ on an open set of unassigned indices, with every index revised only finitely often over the whole construction. The result satisfies 𝓘 + H\*(·, Ĉ′).

**Theorem 3.5 (conditional existence; PROVED given Conj 3.4 and stage-0 tameness).** Let Σ₀ be the system consisting of:
- T at u;
- (I1) committed;
- reservations for T's guidance refusals.

Suppose Σ₀ is tame along some Ĉ. Then, under Conjecture 3.4, there is a full system satisfying every axiom with T1 = C_u.

*Proof.*
1. Well-order Δ ∪ (records × W) in a type in which each item recurs cofinally often (continuum × continuum = continuum).
2. At each successor stage, do the following:
   - assign the next index by Prop 3.1;
   - or settle the next record if it is carried, by Conjecture 3.4.
3. At limit stages, use Prop 3.2.
4. At the end, apply Lemma 2.2 and Theorem 2.3. ∎

**Why H\* is substantive.** Each of its clauses is a property of (Σ, Ĉ), checkable without reference to future steps. Each is finitely refutable or has permanent witnesses. **None asserts that any completion exists.** In particular, H\* says nothing about the unassigned acceptances whose (TC) and protection consequences make up (M4). It is strictly weaker than "Σ is extendible": stage-0 tameness is compatible with every one of the round-54 constructions, including those that later fail. The content of Conjecture 3.4 is precisely that tameness can always be *maintained*.

**Remark 3.6 (no fixed-oracle invariant; PROVED, given PP57 Theorem Q and PP63 §4.6).** One could try the hypothesis "Σ agrees with some reweighted Λ_q along the posterior selection". It fails at every total Σ whose selection is the posterior family near u:
- a total Σ agreeing with Λ_q *is* Λ_q;
- Λ_q has a q-balanced interior swap (PP63 §4.6);
- Theorem Q then forbids closed sections together with (C).

So no hypothesis of this kind can be preserved up to the final system. Hypotheses of finite consistency are preserved, but they are vacuous (PP61 Theorem C). This is why H\* is local and record-based rather than witness-based.

**Lemma 3.7 (guidance-spread slack; PROVED).** Let Ĉ be face-admissible and continuous in measure. For a model Y, put W_w(Y) := {q : Y weakly w-better than Ĉ_q}, which is closed. For each pair (q, Y) with Y strictly w-better than Ĉ_q, put J_q := {w′ : q ∈ W_{w′}(Y)}, and choose a reservation ball of radius

  r(q, Y, w) < min{ ¼·dist(q, ∪_{w′∉J_q} W_{w′}(Y)), dist(q, Δ_{J_q}), dist(q, {q″ : Ĉ_{q″} weakly w-better than Y}) }.

With these radii, the guidance reservations satisfy (H1) and (H2).

*Proof.*
- **Positive radii.** Two facts are needed.
  - **Pareto lemma.** A face-admissible D_K cannot be weakly improved at every world of its face unless the change is null. At each g, either g_J has a uniform sign and every J-world is correct, or the advice is correct at some J-world, or the advice is S and g_J is mixed. In every case any change worsens some J-world.
  - Hence J_q ⊉ supp q, so q ∉ Δ_{J_q}. The other two sets are closed by continuity and miss q.
- **Slack.**
  - Suppose q′ is reserved at every world of supp q′ = J. Then for each w ∈ J, q′ lies in the ball around some q_w.
  - Let q\* be the q_w with the largest radius. For any other w′ ∈ J we have |q\* − q_{w′}| < 2r\*. If w′ ∉ J_{q\*}, then |q\* − q_{w′}| ≥ dist(q\*, W_{w′}) ≥ 4r\*, which is impossible.
  - So J ⊆ J_{q\*}, and q′ ∈ Δ_J ⊆ Δ_{J_{q\*}}. This contradicts |q′ − q\*| < dist(q\*, Δ_{J_{q\*}}).
- **(H1).** By the third term of the minimum. ∎

**Stage-0 tameness is OPEN.** Lemma 3.7 gives (H1) and (H2) for the guidance reservations. The copy-closure (H3) of guidance spreads along the posterior selection is not proved: the cascade of §4.5 applies to them too.

---

## 4. The first nontrivial extension

**Setting.**
- Edge {i, j} = {1, 2}, third world k = 3.
- Let E be a bounded non-null set near the ray of g₀ = (1, 1, −2), at positive angular distance from T's answer boundary. On E, T is silent and worlds 1 and 2 agree (CHECKED).
- X_E := T[E ↦ +]. It is incoherent (non-conic; Lemma H).
- rec(T, X_E) = (E : S → +). Strict (G) puts it in Ref₁ and Ref₂ (I1). Weak (G) puts it in Acc₃: X_E is 3-worse on E.

Start from Σ₀:
- T at u, (I1), and reservations for all of T's guidance refusals. Lemma 3.7 radii are used with Ĉ = the posterior family; with only T assigned, the simple rule "balls inside the open simplex" already gives (I8), since |W_g| ≤ 2 by the Pareto lemma.
- In particular, (U_E, X_E, 1) and (U_E, X_E, 2) are in Res₀. U_E is chosen inside Σ_E := {a : C_a silent on E} (open, containing u).

**Lemma 4.1 (forced structure for any edge defender; PROVED).** Let D be selected at p in the open edge {1, 2} in some extension satisfying 𝓘.

(a) D = D_K with K ⊆ Δ_{12}. D answers + on all of E, since m₁g₁ + m₂g₂ > 0. Hence:
- rec(D, X_E) = rec(D, T) restricted to F′ := D(D, T) ∖ E;
- D's defence against X_E is its defence against T, read off E.

(b) Suppose D ⪯_w X_E is accepted for some w ∈ {1, 2}. Then (TC) forces T ⋠_w T[H′ ↦ D] for every measurable H′ with (P_w ∖ E) ⊆ H′ ⊆ D(T, D) for which the triangle is non-degenerate. Here P_w := {D strictly w-better than T}. The case H′ = D(T, D) gives T ⋠_w D. Each of these is a refusal at u and needs a reservation there.

*Proof.*
- **(a).** Face-admissibility is necessary for competitiveness (AUDIT_section_topology §1). The rest is direct computation.
- **(b), the case H′ = D(T, D).**
  - The triangle D → X_E → T → D at w has two accepted links: D ⪯_w X_E (given) and X_E ⪯_w T (weak (G): T is worse on E).
  - If T ⪯_w D were also accepted, (TC) would demand T ⪯_w X_E, which is refused by strict (G).
- **(b), general H′.** Put Z := T[D(T, D) ∖ H′ ↦ D], so that rec(Z, D) = (H′ : T → D) = rec(T, T[H′ ↦ D]).
  - The condition P_w ∖ E ⊆ H′ means that Z's D-part lies in {D strictly w-worse than T} ∪ E. On E, Z is + or S while X_E is +.
  - So X_E is weakly w-better than Z, and X_E ⪯_w Z is accepted by (I1).
  - With D ⪯_w X_E, the triangle D → X_E → Z → D has two accepted links.
  - Its reverse Z ⪯_w X_E is refused by strict (G) whenever Z ≠ X_E. That is the non-degeneracy condition.
  - So rec(Z, D) must be refused. T carries it.
- **Other Z.** More generally, the same argument forces Z ⋠_w D for every Z strictly w-worse than X_E. Those Z that are not {T, D}-valued give records carried by neither T nor D. They are committed as refusals without reservations, since (I7) concerns assigned carriers only. ∎

**Lemma 4.2 (the −e₃ edge posterior; PROVED, CHECKED).** Let D := D_{M_p} with M_p = {(m₁, m₂, 0)/(m₁ + m₂) : m ∈ M}, p = (½, ½, 0), so K = [(16, 7, 0), (7, 16, 0)]/23. Then D is weakly 3-worse than T everywhere and strictly 3-worse on an open cone.

*Proof.* Take any g.
- **T answers s with s correct at 3.** D cannot be 3-better.
- **T is silent.** If D answers s, then for the m ∈ M with s(m·g) ≤ 0 we get s·m₃g₃ = s(m·g) − s(m₁g₁ + m₂g₂) < 0. So s is wrong at 3, and D is not 3-better.
- **T answers s with s wrong at 3.** Then s(m₁g₁ + m₂g₂) = s(m·g) − s·m₃g₃ > 0, so D answers s too.
- **Strictness.** At g = (−1, −1, 10), T says + (correct at 3) and D says −.

CHECKED on 22,744 samples, together with mixedness at worlds 1 and 2:
- at (−1, −1, 10), D is better than T at 1;
- at (2, −1, 2), D is worse than T at 1. ∎

**Prop 4.2 (joint choice criterion; PROVED).** Suppose the edge defender D is weakly 3-worse than T (as in Lemma 4.2). Then:
- (i) every partial D-rival T[H′ ↦ D] of Lemma 4.1(b) is weakly 3-worse than T, so T ⪯₃ T[H′ ↦ D] is guidance. All of T's (TC)-induced defence obligations are discharged at world 3, with no new non-guidance acceptance at u;
- (ii) D ⋠₃ X_E and D ⋠₃ T are forced by strict (G), because F′ contains the open cone of Lemma 4.2 and that cone is disjoint from E;
- (iii) T ⪯₃ D holds by guidance.

For a general edge defender (for example D = V₁, which defends at 1 by guidance), (i) fails. T must then defend against T[H′ ↦ V₁] by **non-guidance** acceptances at 2 or 3. So the joint choice that minimises new non-guidance commitments at u is **index on the edge, defender weakly k-worse than T.** This is derived, not imposed: it is the condition under which Lemma 4.1(b)'s obligations close by guidance.

**Theorem 4.3 (Σ₁; PROVED).** Let D be as in Lemma 4.2 at p = (½, ½, 0). Let Σ₁ be the closure of Σ₀ with the following added.
- **Assignment.** C_p := D, with D ∈ P.
- **Defence commitments.** D ⪯₁ X_E and D ⪯₁ T. These are D's defences against X_E and against T. [Both 1 and 2 are possible; one world suffices.]
- **Forced refusals at u.** T ⋠₁ T[H′ ↦ D] for all H′ as in Lemma 4.1(b), each with a reservation (U_{H′}, ·, 1) inside the open simplex.
- **Forced refusals at p.** D ⋠₃ X_E and D ⋠₃ T, with reservations V₃ ∋ p.
- **D's guidance refusals.** Reservations as in Lemma 3.7, with all balls around p disjoint from all balls around u.

Then Σ₁ satisfies 𝓘, and no face-defence obligation is exhausted.

*Proof.* Only u and p are assigned.

**(I2).**
- At world 1 the only non-guidance acceptances are D ⪯₁ X_E and D ⪯₁ T.
- A triangle with exactly one non-guidance link would make that link a weak improvement: its rank changes are minus those of two guidance links (PP21 Lemma 2.1). Both links are mixed at 1 (Lemma 4.2), so no such triangle exists.
- Every triangle containing both links has a third link T ⪯₁ X_E or T ⪯₁ D, and both are refused.
- Every triangle with two accepted links and a refused reverse has had its third link refused. This is Lemma 4.1(b), and it also covers the links D ⪯₁ T, T ⪯₁ Z, Z ⪯₁ D: the Z that are weakly 1-worse than T are among those strictly 1-worse than X_E, or equal T.
- So no triangle has three accepted links, and (I2) holds vacuously beyond guidance.

**(I3) and (I4).**
- If X ⪯_w T at every w by committed acceptances, these are guidance, so X is weakly better at all worlds. By the Pareto lemma, X = T.
- The same holds for D on {1, 2}: every committed acceptance into D is guidance.

**(I6) and (I7).**
- T and D carry each other's refused records only trivially, because D ≠ T on D(T, D).
- Every refusal at u or p has its ball.

**(I8), rival by rival.** Every reservation centred at u lies in the open simplex, and every reservation centred at p is a small ball around p.
- **X_E.** Reserved {1, 2} near u, so world 3 is free. Reserved {3} near p, so worlds 1 and 2 are free, on the edge as well.
- **D and the partial rivals.** Reserved {1} near u; worlds 2 and 3 are free.
- **T as a rival.** Reserved {3} near p; worlds 1 and 2 are free.
- **Guidance rivals.** Lemma 3.7. Each rival's balls around u and around p are disjoint.

At p itself: D ⪯₁ X_E, D ⪯₁ T, and guidance at 1 or 2 (Pareto) for every other rival. ∎

**Prop 4.4 (the switch; PROVED).** In every total extension of Σ₁:
- (i) A_w(X_E) := {q : C_q ⪯_w X_E} are closed and form a KKM cover. A₁ ∪ A₂ misses U_E, A₃ misses V₃, and p ∈ A₁. Hence there is q\* with C_{q\*} ⪯_w X_E for every w, so C_{q\*} weakly dominates X_E at all worlds. Moreover, q\* ∉ U_E ∪ V₃.
- (ii) C_{q\*} ≠ T, and C_{q\*} is strictly 1-better (or 2-better) than T somewhere off E. Otherwise strict (G) would refuse C_{q\*} ⪯_{1/2} X_E.
- (iii) Along the −e₃ ray a_s = (1, 1, s) (normalised), C_{a_s} answers + at g₀ iff s < 7/16 (CHECKED). Every member weakly 3-worse than T that answers + on all of E refuses X_E at 3 by guidance. So, if the selection follows this ray, the switch lies in s ∈ [7/16 + O(diam E), 1 − rad U_E]:
  - acceptance at 3 holds on a closed set reaching down to the switch;
  - acceptance at 1 holds on a closed set reaching up to it;
  - both refusal sets are open.
- (iv) Direct (C) at q\*: X_E is incoherent, so some world must refuse rec(X_E, C_{q\*}). On the ray, rec(X_E, C_{q\*}) = (E : + → S) ⊔ (L : T → C_{q\*}). Its carriers must answer + on E and agree with T on L. No member of the ray does both, so the refusal is carrier-free and costs no slack (Prop 3.3(iii)).

*Proof.* (i) is KKM. The rest follows from Lemmas 4.1–4.2, the computation at g₀, and monotonicity along pure-shift rays (Lemma 4.5(a)). ∎

**Lemma 4.5 (copy transport and E-anchoring; PROVED, CHECKED).**

(a) Along a pure-shift ray a_s = u∘(1 + t e_w), every vertex sum Σ_i a_i m_{v,i} g_i changes with slope of the same sign (that of g_w). So each g's advice moves monotonically along the ray, through at most − → S → + or the reverse. (CHECKED for −e₃ and −e₂.)

(b) Let q′ ∈ U_E lie on such a ray, and let z lie further along it. Then C_z carries rec(C_{q′}, X_E) provided:
- C_z is silent on E; and
- no problem of L_{q′} := {C_{q′} ≠ T} changes advice a second time between q′ and z.

The copy rival is X_z := X_E[L_z ∖ L_{q′} ↦ C_z]. Since rec(C_{q′}, X_E) is refused at 1 and 2 (q′ ∈ U_E), **C_z must refuse X_z at 1 and 2 and accept it at 3.** C_z needs its own reservation, which is a cascade (M3).

CHECKED:
- −e₃ ray: q′ = (1, 1, 9/10), z = (1, 1, s) for s ∈ [1/2, 17/20]. 0 failures in 1,184 layer checks. The carry stops at s ≈ 7/16, where C_z starts answering on E.
- −e₂ ray: q′ = (1, 9/10, 1), z for s ∈ [3/10, 17/20]. 0 failures. At s = 1/4 it breaks by a second change (+ → S → −); the edge model (1, 0, 1) does not carry the record.

(c) **E-anchoring.** No face-admissible model on the edge {1, 2} carries any record whose support meets E in a non-null set on which the old advice is S. So the transported double refusals (1, 2) **never reach the edge where world 3 is unavailable.** On the edges {1, 3} and {2, 3}, world 3 lies in the support.

*Proof.*
- (a) is the PP57 Lemma 4.1 computation.
- (b): along the ray each g changes at most as in (a). On L_{q′} the first change happened before q′, so C_z = C_{q′} there under the no-second-change proviso. On E both are silent.
- (c): such models answer + on E. ∎

**What the first extension shows.**
- The defender and its index are chosen jointly by a derived criterion (Prop 4.2).
- Reservations are committed at both T and D, and slack survives on every face (Thm 4.3).
- The switch is forced, closed on the acceptance side and open on the refusal side (Prop 4.4).
- **Reservations at T are not local.** By (IB), every later source on a pure-shift ray through U_E inherits a double refusal (Lemma 4.5). Its defence is pushed to world 3 on a large region. The edge {1, 2} is protected only because its models answer on E.

This is the concrete form of (H3), and of the cascade (M3) in Conjecture 3.4.

---

## 5. The balanced-swap configuration as an adversarial instance

**Configuration.** Use PP57/PP62's configuration:
- a = u and b = B interior, posterior members;
- F ⊆ D_{uB} balanced and non-conic, so (Mix_w) holds for every world (PP66 §1);
- X := T[F ↦ C_B] and Y := C_B[F ↦ T];
- r_F := rec(T, X) = rec(Y, C_B), with r_F⁻¹ = rec(C_B, Y) = rec(X, T).

The step assigns C_B at B and settles r_F and r_F⁻¹. Following PP66's local shape, it uses three distinct worlds w, v, v′:
- **Verdicts.**
  - r_F ∈ Ref_w ∩ Ref_{v′} ∩ Acc_v;
  - r_F⁻¹ ∈ Ref_w ∩ Ref_v ∩ Acc_{v′}.
- **Reservations.**
  - (U, X, w) and (U, X, v′) around u;
  - (U_B, Y, w) and (U_B, Y, v) around B.

**Prop 5.1 (PROVED at step level).** For balls with U ∌ B and U_B ∌ u, chosen inside the open simplex, the step preserves 𝓘. Moreover:

- (i) **Defence and protection at both ends.** T defends against X at v; C_B defends against Y at v′. C_B is protected against Y (r_F refused at w and v′). T is protected against X (r_F⁻¹ refused at w and v).
- (ii) **(I8).** Near u, rival X has only v free. Near B, rival Y has only v′ free. Both points are interior, so (I8) holds.
- (iii) **Theorem Q is respected where it applies.**
  - Pure shifts u_t^w and u_t^{v′} lie in U. When assigned, they must refuse X at w and at v′ respectively.
  - By PP62 Lemma 1.3, V_w(rec(C_{u_t^w}, X)) = Γ_w(u, u_t^w) > 0. So the system refuses **strictly u¹-favourable** comparisons out of selected models near u, and does not contain {V > 0}.
  - These refusals are legitimate: by (Mix), C_{u_t} is not weakly better than X at any world.
- (iv) **Theorem E is respected where it applies.**
  - The only free world for u_t^w in U is v. So C_{u_t^w} ⪯_v X is accepted on assignment, with V_v = Γ_v < 0. This is exactly PP62 Cor E.2(i).
  - So acceptances near u are not confined to u¹-endorsed ones.
- (v) **The Lemma S splits are settled cheaply.** [R, after REFEREE_round54 §2.6]
  - Take such an unfavourable acceptance, with X₀ := C_{u_t}. Take E′ inside {X strictly v-better than X₀}, small, and put Z := X₀[E′ ↦ X].
  - Then Z ⪯_v X₀ is guidance-accepted and X₀ ⪯_v Z is guidance-refused. So (TC) forces the refusal of the **specific** link X ⪯_v Z, as the referee's sharpening of Cor E.2(ii) says.
  - Its record is rec(X, Z) = ((F ∪ σ_t) ∖ E′ : X → X₀). Its carriers must equal C_B on F ∖ E′ and T on σ_t ∖ E′. By PP63 Prop 2.1 this is special position, so the record is generically **carrier-free**.
  - Hence the forced refusal costs no slack (Prop 3.3(iii)). This is PP66's "one-step termination" in this framework.
  - The other link, rec(Z, X₀) = (E′ : X → X₀), is carried by T when E′ ⊆ σ_t. Under the referee's choice of E′ it is guidance-accepted, so no reservation at u is ever needed for it.
- (vi) **The two ends use different defending worlds** (v at the a-end, v′ at the b-end), as PP66 Lemma T requires for any d-robust version.

*Proof.* The checks of Theorem 4.3 apply with these rivals. The (TC) status of the inverse pair at w is PP63 Lemma 3.1, applied to the two committed records and their inverses only. ∎

**Where the adversary bites.** All of the above holds for a swap *fixed before* the commitments. The dangerous instance is chosen *after* Σ. For example, the adversary waits until shifted members u_{t_n}^w (t_n → 0) have committed acceptances of rec(C_{u_{t_n}}, X′) at every world, for some later rival X′ = T[F′ ↦ C_{B′}]. Then every refusal of r_{F′} at u meets the germ condition's obstruction (M2), and acceptance at all worlds violates C_{B′}'s protection (M4).

In this framework the defence is ordering-independent but not automatic:
- **Commitments only happen in steps.** Those shifted members' records with X′ are not committed until (X′, ·) is processed, or until they are forced by closure.
- **The (M2) configuration arises only if earlier settlements *chose* acceptance at all worlds on a sequence converging to u.**

Conjecture 3.4 asserts that a settling choice avoiding this always exists. It is not proved.

---

## 6. The two-neighbourhood rejection test on the operation

**The configuration.** In the test configuration, the step of §5 with v, v′ replaced by the test's requirements does the following:
- refuse r at w with (U_a, X, w);
- refuse r⁻¹ at w with (U_b, Y, w);
- defend the a-end at v and the b-end at v′ (PP66's shape);
- settle the Lemma S links by carrier-free refusals.

**Result: the operation is not rejected.** This step preserves 𝓘 (Prop 5.1 with general interior a, b). PP66 independently exhibits a total relation of this local shape satisfying every clause (PP66 Theorem 2).

**What the test is not able to show.** Nothing in the operation uses a common reweighting, so the α = (1, 1) obstruction does not apply. As PP66 notes, the swap in the test is fixed in advance. The sharper version is a swap balanced for the system's *own* accumulated commitments and chosen after them. That is exactly the (M2)/(M4) configuration of §5, and hence Conjecture 3.4. **My operation passes the stated test but has not been subjected to the sharper one.**

---

## 7. Assessment against the success criterion

**What the mechanism does explain.**
- **Passage to the final system (PROVED).** Theorem 2.3 gives all axioms, including global (C) and closed sections. No continuity argument is needed at the limit, and arbitrary transfinite chains are allowed.
- **Installing new coherent defenders (PROVED, under tameness).** The defender is any coherent face-admissible model, chosen as a provisional value. Assignment needs no new reservation and costs no slack (Prop 3.1). Co-design means revising the provisional selection off the assigned set (Prop 3.2).
- **The first nontrivial extension, explicitly (PROVED).**
  - a derived joint-choice criterion;
  - reservations at both T and the defender;
  - surviving face obligations;
  - a forced, closed switch.
- **Theorems Q and E respected** at the adversarial balanced swap; refusals of carrier-free records cost nothing.

**What it does not explain.**
- **The next arbitrary rival.** Its records must be settled one by one. Prop 3.3 says exactly when a settlement is possible. Conjecture 3.4, that one always is, is **unproved**. The candidate obstructions are:
  - (M2) germ collisions at accumulation points of earlier acceptances, which the adversary's after-the-fact balanced swap targets;
  - (M3) copy transport, which really carries refusals far from where they were committed (Lemma 4.5).
- **Stage-0 tameness.** The copy-closure of the guidance spreads along a provisional selection is not proved.
- **A settling policy.** The mechanism does not specify one that provably avoids (M2). The two greedy policies are excluded where Theorems Q and E apply: "accept unless closure forbids" if its acceptances near u contain all strictly u¹-favourable comparisons, and "refuse unless defence forbids" if its acceptances are u¹-endorsed. A successful policy must sit between the envelopes, as round 54 found.

**By the audit's standard, then,** this is a global framework with a proved limit theorem and a proved free-assignment lemma. The settling lemma is still missing. If Conjecture 3.4 were proved, Theorem 3.5 would give coverage. The most promising handle on it is that refusals of carrier-free records are free, so (M4) can usually be broken without spending slack. The real enemy is (M2), and an attack on Conjecture 3.4 should start there.

---

## 8. Scripts (`r9/PP64_py/`; run `python3 -I -B geom64.py > geom64.out` inside the folder)

`geom64.py` uses exact rationals on 22,744 sample problems (an integer grid plus random rationals). It checks:
- D (the −e₃ edge posterior) is weakly 3-worse than T, with witness cones;
- D and T are mixed at world 1;
- g₀ = (1, 1, −2) is T-silent and has the 7/16 threshold;
- the −e₂ ray is silent at g₀ down to the edge;
- the Pareto lemma holds for T, D and one posterior;
- advice is monotone along the −e₃ and −e₂ rays;
- copy transport along both rays, and its breakdown by second change.

Ends ALL PASS.
