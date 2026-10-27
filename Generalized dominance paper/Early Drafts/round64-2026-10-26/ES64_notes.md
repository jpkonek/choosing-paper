# ES64 — Escape from the relational lemma: Brier with deliberate incomparability (25 Oct 2026)

Labels: **PROVED** (complete argument here; not refereed) / **CHECKED** (exact rational computation) / **CONJECTURE** / **NUMERICS** (finite search; a search that finds nothing proves nothing). Scripts are in `es64py/`; run each with `python3 -I <script>` from that folder. Each has an `.out` file.

Binding inputs: `BRIEF64.md` (role ES64) and `AUDIT_r64_decisions.md`. The framework is exactly the brief's:
- relations are reflexive, a.e.-equal models are tied, and only (TC) holds;
- strict (G) and (IB) are as in W62 §2;
- the cover requirements are global coherence, direct (C), target undominated, incoherent-model dominance and (LF).

Transitivity, completeness, (S), (B) and (W) are not assumed. (W) is obtained as a by-product.

---

## 0. Verdict in plain English

1. **The escape exists, and it is generic.** Start from plain Brier: world i ranks models by ∫_X h_i. Delete comparisons record by record, and never delete a guidance comparison. The resulting relation always satisfies reflexivity, strict (G), (IB) and (TC) (Lemma 1.3 and Theorem 3.2). The reason (TC) survives is short:
   - each world's relation is still contained in the Brier weak order;
   - the deletions are symmetric on Brier ties;
   - so a cycle of comparisons can never contain a strict step.

   No transitivity is needed and none is present: (TP) fails explicitly (§2.4).
2. **What to delete.** Choose the family 𝒩 of coherent models to be protected. For each N ∈ 𝒩, and each model Y that Brier-weakly-improves on N at every world, remove the single comparison "Y ⪯_i N" at one world i. By (IB) the same comparison is then removed in every context.
   - At that world, Y and N become **incomparable**. Nobody vetoes anything.
   - For the reversed triangle, the collar trade D_K ∪ P is Brier-better than D_K at every world. In the deletion relation it is incomparable with D_K at world 1, and strictly better than D_K at worlds 2 and 3. So D_K is undominated, without any priority region at any world (Prop 2.5).
3. **What this does to E61's machinery.** E61's priority-region lemmas (Lemma 3.1, Cor 3.2, Lemma 3.4) need (TP).
   - Under (TC) alone, a dominator of a box model must be **incomparable** with the worst R-avoiding model (Lemma 2.2).
   - The deletion relations realise exactly this pattern and have **no priority regions at all** (Prop 2.5).
   - So E61's broad impossibility (Cor 5.3), O61's Theorem A and IN63's Theorem C do not reach these relations. Each assumes transitive lexicographic or unanimity orders.
   - The lead's observation is confirmed: a *strong* priority region gives the box lemma from strict (G) alone (Lemma 2.1). But the axioms do not force strong priority regions to exist: the deletion relations have none.
4. **Reduction of the cover to one geometric condition (Theorem 3.2; PROVED).** The deletion relation built on 𝒩 has the following property: *its undominated models are exactly 𝒩, every other model is dominated by a member of 𝒩, and direct (C) and (W) hold*, provided condition (★) holds:

   > (★) Every model X ∉ 𝒩 has some N ∈ 𝒩 with ∫_N h ≥ ∫_X h coordinatewise (and not equal), whose change from X to N is not "attacked" by any member of 𝒩.

   Here a change (A, B), meaning "accept A instead of B", *attacks* a model N° if N° contains B and misses A.

   Hence **if D_K ∈ 𝒩 and (★) holds, K is covered**, with every requirement verified.
5. **The universal choice.** Take 𝒩 = *all* coherent models. Then (★) becomes a single condition (H) on the moment map and the coherent hull: every incoherent X has a coherent N with ∫_N h ≥ ∫_X h (not equal) such that N∖X meets hull(X∖N) in positive measure.
   - **If (H) holds, the binding framework admits a universal cover.** Every coherent model is undominated, and every incoherent model is dominated by a coherent one. This holds for every target K with K' ⊆ relint K, the reversed triangle included.
   - (H) is **CONJECTURE**.
     - *Proved:* the first step, that a Bayes act strictly dominates any incoherent model, in all coordinates (Lemma 5.1). Also proved: (H) when X misses part of the positive orthant (Prop 5.4).
     - *Exact certificates (CHECKED):* every collar rival D_K ∪ P with P inside three thin boxes beyond the face midpoints, provided P has mass in the box corners (Prop 5.6; this includes E61's collar trades); and two unions of Bayes acts (T1), where every strict Bayes dominator found was certified.
     - *Random search (NUMERICS, §5.5):* holes and bumps. 17 of 30 random rivals were certified exactly. The other 13 are search failures, not counter-instances.
6. **The minimal choice fails.** Take 𝒩 = Bayes acts ∪ {D_K}. Then (★) fails at the bump rival D_K ∪ P: every strict Bayes dominator found on the grid contains P (CHECKED on a grid, Prop 3.4). This matches the ordinal Lemma 4.3, valid in *every* cover: the defender of D_K ∪ P must drop part of P. So more coherent models must be protected; the universal choice protects them all.
7. **Ordinal lemmas valid in every cover under the binding framework (§4; PROVED).** These are offered to OR64. They concern collar refusal (some world refuses "add P" in every context), protection transfer (non-invertibility of defence records) and bump defenders.
   - The deletion relations satisfy all three, so none of them, alone or together, yields a contradiction.
   - **Any axiom-level impossibility for the reversed triangle must refute (★) for every 𝒩 ∋ D_K, and in particular must exhibit an incoherent model violating (H).**

**Deliverable reached.** This is level (2) of the brief, in a strong form:
- the mechanism satisfies the axioms everywhere (PROVED);
- the target, and every coherent model, is protected against *every* rival (PROVED);
- global coherence and incoherent-model dominance are reduced exactly to (H), which is proved or certified on the classes listed.

**What remains to globalise is exactly (H)** (or (★) for some smaller family 𝒩 ∋ D_K). This is not a full cover, and I do not claim one.

---

## 1. Record calculus (PROVED)

Notation:
- Models are measurable X ⊆ U, modulo μ-null sets.
- The **record** of the ordered pair (X, Y) is r(X, Y) := (X∖Y, Y∖X), a pair of disjoint sets modulo null sets. It reads: "X accepts A = X∖Y where Y accepts B = Y∖X". Its inverse is r⁻¹ := (B, A).
- A record (A, B) **attacks** a model Z if B ⊆ Z and A ∩ Z = ∅ (a.e.). Then Z ⊕ r := (Z∖B) ∪ A satisfies r(Z ⊕ r, Z) = r.

**Lemma 1.1 ((IB) = record relations).**
- A relation satisfies (IB) if X ⪯_i Y ⟺ r(X, Y) ∈ Acc_i for a set Acc_i of records.
- Conversely, every (IB) relation is of this form.
- Reflexivity is (∅, ∅) ∈ Acc_i. Ties of a.e.-equal models hold because records are taken modulo null sets.

*Proof.*
- **Record relations satisfy (IB).** Take S, X, Y, X′, Y′ as in W62 (IB). Then X∖Y = (X∩S)∖(Y∩S) = X′∖Y′, and the same holds for Y∖X.
- **(IB) relations are record relations.** Take S := X△Y. Then (IB) says that X ⪯_i Y depends only on (X∩S, Y∩S) = r(X, Y). ∎

**Lemma 1.2 ((TC) as 3-cycle closure).** (TC) at world i is equivalent to the following: whenever X ⪯ Y ⪯ Z ⪯ X, all three reverse comparisons hold too.

*Proof.*
- ¬(Z ≺ X) means: Z ⋠ X, or X ⪯ Z.
- So (TC) says that X ⪯ Y ⪯ Z together with Z ⪯ X forces X ⪯ Z.
- Rotating the cycle gives the other two reverses. ∎

**Lemma 1.3 (deletion lemma).** Let φ be any real function on models, and let ⪯ be a relation such that:
- (a) X ⪯ Y implies φ(X) ≤ φ(Y);
- (b) if X ⪯ Y and φ(X) = φ(Y), then Y ⪯ X.

Then ⪯ satisfies (TC).

*Proof.*
- By (b), X ≺ Y implies φ(X) < φ(Y).
- Suppose A ⪯ B ⪯ C. Then φ(A) ≤ φ(C).
- So C ≺ A, which would need φ(C) < φ(A), is impossible. ∎

So **any sub-relation of a weak order that is symmetric on its ties satisfies (TC).** Deleting comparisons from a complete transitive score order, while keeping deletions symmetric on score ties, never breaks (TC). This is the brief's "deliberately missing comparison" in its simplest exact form.

---

## 2. E61's priority machinery under (TC): what survives, what fails

Fix worlds j ≠ i and a non-null R ⊆ U ∩ {h_j < 0}. Put M_R := (U∖R) ∩ {h_j < 0} and X_i := (U∖R) ∩ {h_i > 0}.

**Lemma 2.1 (strong priority gives the box lemma without transitivity; PROVED).**
- Say R is a *strong priority region* at j if no Y with μ(Y∩R) > 0 has Y ⪯_j Z for any Z with μ(Z∩R) = 0.
- Then X_i is undominated. Only strict (G) at world i is used.

*Proof.*
- Let Y weakly dominate X_i. Then Y ⪯_j X_i, and X_i avoids R, so μ(Y∩R) = 0.
- If Y ≠ X_i a.e., then X_i∖Y ⊆ {h_i > 0} and Y∖X_i ⊆ (U∖R) ∩ {h_i < 0} a.e.
- Strict (G) gives X_i ≺_i Y, contradicting Y ⪯_i X_i. ∎

This confirms the lead's observation. (TC) is not even needed.

**Lemma 2.2 (what (TC) gives for E61's weak priority; PROVED).**
- Suppose R is a priority region in E61's sense: no Y meeting R is ⪯_j M_R.
- If Y ⪯_j X_i with μ(Y∩R) > 0, then Y and M_R are **incomparable** at j.

*Proof.*
- X_i is pointwise j-better than M_R, so X_i ⪯_j M_R by (G) and reflexivity.
- (TC) applied to Y ⪯_j X_i ⪯_j M_R gives ¬(M_R ≺_j Y).
- Since Y ⋠_j M_R, this forces M_R ⋠_j Y. ∎

So E61 Lemma 3.1 and Cor 3.2 fail without (TP) exactly when the dominator of X_i is incomparable with M_R at j. §2.4 exhibits this.

**Lemma 2.3 (a pure-guidance world kills every target; PROVED).**
- Suppose some world j accepts only guidance comparisons: X ⪯_j Y iff X∖Y ⊆ {h_j > 0} and Y∖X ⊆ {h_j < 0} a.e.
- Then every R ⊆ U∩{h_j<0} is a strong priority region.
- Take R a small ball in U∩{h_j<0, h_i>0}, non-empty when U ⊇ cl D_K∖0 with K ⊆ relint Δ. Then X_i has a hole, so it is incoherent and undominated. No target is covered.

*Proof.*
- Strong priority: if Y meets R and Z avoids R, then Y∖Z ⊇ Y∩R ⊆ {h_j < 0}, so Y ⋠_j Z.
- Incoherence of X_i is E61 Cor 3.3's convexity argument. ∎

So every world must accept some non-guidance comparisons that add j-wrong gambles. This is the only "veto-type" conclusion I can extract from the axioms alone.

**2.4 Diagnostic: (TP) fails in the deletion relation; Lemma 3.1's mechanism is absent (CHECKED, `collar.py`).**
- Take the deletion relation of §3 with 𝒩 = all coherent models, N := D_{Q_t} (Q_t = (1−t)K + tu, t = 3/23) and P₁ the thin box beyond the midpoint of face F_{v_1}.
- Three facts hold:
  - N ⪯₁ D_K ∪ P₁ holds. The record is Brier-accepted (m(N) − m(D_K∪P₁) = (0.00249, 0.0360, 0.0360), exact) and attacks no coherent model (Prop 5.6).
  - D_K ∪ P₁ ⪯₁ D_K holds by guidance (P₁ ⊆ {h₁ > 0}, CHECKED).
  - N ⪯₁ D_K is deleted, because its record attacks D_K and m(N) − m(D_K) = 0.0288·(1,1,1) ≫ 0. So N and D_K are incomparable at world 1.
- This is a (TP) failure: a comparison composed with a guidance comparison is not accepted.
- Status: CHECKED given Theorem 3.2's construction, which is PROVED.

**Prop 2.5 (no priority regions in deletion relations; PROVED).** In the deletion relation of §3, for any family 𝒩 of coherent models, no non-null R ⊆ U∩{h_j<0} is a priority region at j, even in E61's weak sense.

*Proof.*
- Take E ⊆ R non-null with μ(E) small, and put Y := ((U∖R) ∩ {h_j>0}) ∪ E.
- The record r(Y, M_R) = (A, B) has A ⊇ U ∩ int ℝ³₊ and B = M_R.
- It is Brier-strict at j for small E: m_j(A) − m_j(B) ≥ ∫_{(U∖R)∩{h_j>0}} h_j + ∫_{M_R}|h_j| − ∫_E|h_j| > 0.
- It attacks no coherent model: every coherent model contains int ℝ³₊, which A meets. So it is not deleted, and its tie-inverse clause does not apply because the comparison is strict.
- Hence Y ⪯_j M_R with μ(Y∩R) > 0. ∎

**Consequences for the existing exclusions.** The relevant ledger point is where each exclusion first uses transitivity, or a transitive lexicographic or unanimity architecture.
- E61 Cor 5.3 and Thm 5.1 use priority regions via (TP) (Lemma 3.1), and view-unanimity.
- O61 Thm A uses complete, transitive veto-then-Brier orders.
- IN63 Thm C uses unanimity of finitely many views, which is transitive, and E61 Lemma 3.4.
- C62 and DC63 use single charts.

The deletion relations are neither transitive nor view-generated, so none of these applies. I have not re-audited each proof line by line; that is OR64's ledger task.

---

## 3. The deletion construction and the reduction theorem

**Setting.**
- Finitely many worlds; three for the reversed triangle.
- μ is a finite measure with a positive density and finite first moment. The scripts use the density e^{−|h|₁}, for which cone moments are exact rationals.
- U := D_{K'}, with K' ⊆ relint K compact convex. U is one-sided, U ∩ (−ℝ³₊) = ∅, U ⊇ int ℝ³₊, and (LF) holds at D_K.
- Coherent models are the D_Q, a.e., with K' ⊆ Q.
- Write m(X) := ∫_X h dμ ∈ ℝ³. Write ℬ := {N_π := U ∩ {π·h > 0} : π ∈ Δ} for the Bayes acts, all of which are coherent.

**Definition 3.1 (deletion relation Δ(𝒩)).** Let 𝒩 be a family of coherent models.
- **Brier records.** Br_i := {(A,B) : m_i(A) ≥ m_i(B)}.
- **Guidance records.** G_i := {(A,B) : A ⊆ {h_i>0}, B ⊆ {h_i<0} a.e.}.
- **The records to delete.** 𝓡 := {r = (A,B) non-null : m(A) ≥ m(B) coordinatewise, and r attacks some N ∈ 𝒩}.
- **The deletion world.** For r ∈ 𝓡, let i(r) be the least i with m_i(A) > m_i(B) and r ∉ G_i. If there is none, let i(r) be the least i with r ∉ G_i. Such an i exists:
  - if r ∈ G_i for every i, then A ⊆ int ℝ³₊ and B ⊆ U ∩ (−int ℝ³₊) = ∅ a.e.;
  - since A ∩ N = ∅ and N ⊇ int ℝ³₊, A is null too, so r would be null.
- **Deleted and accepted records.** Del_i := {r ∈ 𝓡 : i(r) = i} ∪ {r⁻¹ : r ∈ 𝓡, i(r) = i, m_i(A) = m_i(B)}, and Acc_i := Br_i ∖ Del_i.
- **The relation.** X ⪯_i Y :⟺ r(X,Y) ∈ Acc_i.

**Which comparisons are missing, and why (TC) holds.**
- *Missing.* For each N ∈ 𝒩 and each Y ≠ N with m(Y) ≥ m(N), the comparison Y ⪯_i N is removed at exactly one world, i = i(r(Y,N)). By (IB) the same record is removed in every context.
  - If Brier ties at that world, the reverse N ⪯_i Y is removed too.
  - Nothing else is removed. Guidance comparisons are never removed.
  - At world i the pair (Y, N) becomes incomparable.
- *(TC).* By Lemma 1.3 with φ_i = −m_i (Brier error up to a constant): Acc_i ⊆ Br_i, and Acc_i is symmetric on Brier ties. The symmetry is checked in (d) of the proof below.

**Theorem 3.2 (reduction theorem; PROVED).** Δ(𝒩) satisfies reflexivity, a.e.-ties, strict (G), (IB) and (TC). Moreover:
- (i) every N ∈ 𝒩 has no weak dominator other than itself;
- (ii) assume (★): every model X ∉ 𝒩 has some N ∈ 𝒩 with m(N) ≥ m(X), m(N) ≠ m(X), and r(N,X) = (N∖X, X∖N) attacking no member of 𝒩. Then every X ∉ 𝒩 is dominated by a member of 𝒩;
- (iii) under (★): the undominated models are exactly 𝒩, so global coherence holds; direct (C) holds in the strong form "a model tied at every world with N ∈ 𝒩 equals N"; (W) holds; and every incoherent model is dominated by a coherent undominated model;
- (iv) if moreover D_K ∈ 𝒩, the ranking covers K in the sense of BRIEF64. (LF) is a property of U.

*Proof.*
- **(a) Reflexivity and a.e.-ties.** The null record is never deleted, because 𝓡 consists of non-null records and the inverse of a non-null record is non-null. Records are taken modulo null sets.
- **(b) (IB).** Lemma 1.1.
- **(c) Strict (G).**
  - Let r ∈ G_i be non-null. Then m_i(A) > m_i(B), so r ∈ Br_i and r⁻¹ ∉ Br_i.
  - r is not deleted at i in either way:
    - not because r ∈ 𝓡 with i(r) = i, since i(r) is never a world where r ∈ G_i;
    - not as a tie-inverse, since tie-inverses are ties at i while r is strict.
  - So X ≺_i Y.
- **(d) (TC).** Lemma 1.3. Symmetry on ties: let r ∈ Acc_i with m_i(A) = m_i(B), and suppose r⁻¹ ∉ Acc_i. Since r⁻¹ ∈ Br_i, we have r⁻¹ ∈ Del_i. Either way r is deleted too:
  - if r⁻¹ ∈ 𝓡 with i(r⁻¹) = i, it is a tie at i, so its inverse r is deleted;
  - if r⁻¹ = s⁻¹ with s = r ∈ 𝓡 and i(r) = i, then r ∈ Del_i.

  Both contradict r ∈ Acc_i.
- **(i)** Let Y ⪯_i N for all i, with Y ≠ N. Then m(Y) ≥ m(N), and r(Y,N) attacks N, so r(Y,N) ∈ 𝓡 and is deleted at i(r). Contradiction.
- **(ii)** Let d := r(N,X).
  - d ∉ 𝓡, because it attacks no member of 𝒩.
  - d is not a deleted tie-inverse: that would need r(X,N) ∈ 𝓡, hence m(X) ≥ m(N), hence m(X) = m(N), which is excluded.
  - d ∈ Br_i for every i, so d ∈ Acc_i for every i.
  - For some j, m_j(N) > m_j(X), so r(X,N) ∉ Br_j and X ⋠_j N.
  - So N dominates X.
- **(iii)** From (i) and (ii). Members of 𝒩 are undominated by (i).
- **(iv)** Immediate. ∎

**Lemma 3.3 (Bayes acts never block a defence; PROVED).** If r = (A,B) has m(A) − m(B) ∈ ℝ³₊∖0, then r attacks no Bayes act.

*Proof.*
- If r attacked N_π, then Z := N_π ⊕ r would have m(Z) ≥ m(N_π), not equal.
- Hence π·m(Z) ≥ π·m(N_π) = max over all models.
- So Z also maximises, and by uniqueness of the maximiser ({π·h = 0} is null) Z = N_π a.e. Then r is null, a contradiction. ∎

So for 𝒩 = ℬ ∪ 𝒩′, the only possible blockers are members of 𝒩′.

**Prop 3.4 (the minimal family ℬ ∪ {D_K} is not enough).**
- Take X₁ := D_K ∪ P₁, with P₁ the box beyond the midpoint of F_{v_1} (δ = λ = 1/10, `geom.piece_beyond`).
- *CHECKED on a grid, exact at each grid point (`bump.out`):* on the 1/60 grid, 102 priors π give m(N_π) − m(X₁) ≫ 0. Every one of these N_π contains P₁, so r(N_π, X₁) = (N_π∖X₁, D_K∖N_π) attacks D_K.
- D_K itself does not dominate X₁: m(D_K) − m(X₁) = −m(P₁) = (−0.0263, +0.0072, +0.0072).
- *What the grid check suggests:* within ℬ ∪ {D_K}, X₁ has no admissible defender. This is not proved off the grid. It agrees with the necessary Lemma 4.3.
- *Background (`pi_dk.out`):* the strict Bayes dominators of D_K itself have every π_k ≥ 0.267 on the 1/30 grid, against 1/5 at the vertices of K.

**Corollary 3.5 (universal family; PROVED given (H)).** Let 𝒩 = all coherent models. If (H) holds, every coherent model is undominated, every incoherent model is dominated by a coherent model, and Δ(𝒩) covers every K with K' ⊆ relint K. That includes the reversed triangle.

*Proof.*
- A coherent N° containing X∖N a.e. contains hull(X∖N). So if (N∖X) ∩ hull(X∖N) is non-null, r(N,X) attacks no coherent model, and (★) holds.
- Apply Theorem 3.2. ∎

---

## 4. Necessary ordinal lemmas, valid in every cover (PROVED; offered to OR64)

Assume a cover of K under the binding framework. Write C* for the coherent undominated models.

**Lemma 4.1 (protection transfer).**
- Let N ∈ C* dominate X, with record r = r(N,X).
- Let N° ∈ C* be attacked by r, and suppose r is accepted at every world (it is, since N ⪯_i X for all i).
- Then N° ⊕ r weakly dominates N°. Hence N° ⊕ r is tied with N° at every world, and is coherent and undominated.
- In particular, if N° ⊕ r is incoherent, this configuration is impossible: **defence records may not attack members of C* unless the attacked copy is again coherent.**

*Proof.*
- r ∈ Acc_i for all i, and (IB) gives N° ⊕ r ⪯_i N° for every i.
- N° is undominated, so N° ⪯_i N° ⊕ r for every i, which is a tie.
- Direct (C) then gives N° ⊕ r ∈ C*. ∎

**Lemma 4.2 (collar refusal).**
- Let P ∩ D_K = ∅ with D_K ∪ P incoherent.
- Then some world i has ¬(D_K∪P ⪯_i D_K). By (IB), the record (P, ∅) is refused at i in every context.
- Necessarily P ⊄ {h_i > 0} a.e.

*Proof.*
- If D_K ∪ P ⪯_i D_K held at every i, then either D_K is dominated, or D_K ∪ P is tied with D_K at every world and so coherent by direct (C). Both are excluded.
- If P ⊆ {h_i > 0}, strict (G) forces the comparison at i. ∎

**Lemma 4.3 (the bump defender).**
- Let N ∈ C* dominate D_K ∪ P, with P ∩ cl D_K = ∅ non-null.
- Then either μ(P∖N) > 0, or N∖P is coherent, undominated and tied with D_K at every world.

*Proof.*
- If P ⊆ N, then r(N, D_K∪P) = (N∖(D_K∪P), D_K∖N) attacks D_K.
- Lemma 4.1 then gives D_K ⊕ r = N∖P ∈ C*, tied with D_K. ∎

**Remark (scope).**
- The deletion relations Δ(𝒩) satisfy all three lemmas:
  - Lemma 4.2: (P, ∅) is refused at world i(r);
  - Lemma 4.3: the defender in Prop 5.6 drops part of P.
- So these lemmas, combined with (G) and (TC), cannot by themselves give a contradiction.
- The only remaining handle for an impossibility proof is the *existence* part: (★) for every 𝒩 ∋ D_K, in particular (H). A refutation of (H) is a concrete, checkable target for OR64.

---

## 5. Toward (H)

**(H).** Every incoherent X has a coherent N with m(N) ≥ m(X), m(N) ≠ m(X), and μ((N∖X) ∩ hull(X∖N)) > 0.

Here hull(B) := D_{Q_B} with Q_B := {q ∈ Δ : q·h ≥ 0 for a.e. h ∈ B}: the smallest coherent model containing B a.e. It exists and lies in U, because K' ⊆ Q_B.

**Lemma 5.1 (strict Bayes dominator; PROVED).** If X is not a Bayes act a.e., some π ∈ Δ has m(N_π) − m(X) ∈ int ℝ³₊.

*Proof.*
- **Setup.** ℳ := {m(Y)} is convex and compact (Lyapunov) and full-dimensional.
- **The interior case.** If m(X) ∈ int ℳ, then m(X) + ε𝟙 ∈ ℳ for some ε > 0.
  - A maximiser z of Σz over ℳ ∩ (m(X) + ε𝟙 + ℝ³₊) is Pareto-maximal in ℳ.
  - Separating z + int ℝ³₊ from ℳ gives λ ∈ ℝ³₊∖0 with z ∈ argmax λ·ℳ.
  - The maximiser is unique a.e. because {λ·h = 0} is null. So z = m(N_{λ/Σλ}).
- **The boundary case.** If m(X) ∈ ∂ℳ, every outer normal ν ≠ 0 at m(X) makes X the a.e.-unique maximiser of ν·m, so X = U ∩ {ν·h > 0}.
  - If some normal had ν ≥ 0, X would be a Bayes act. So the normal cone N_ℳ satisfies N_ℳ ∩ ℝ³₊ = {0}.
  - N_ℳ is pointed, because ℳ is full-dimensional. So K₁ := conv(N_ℳ ∩ {|ν|₁ = 1}) is compact, convex, misses 0 and misses ℝ³₊.
  - Separating K₁ from ℝ³₊ gives d ≥ 0 with d·ν < 0 on K₁. Then d + ζ𝟙 ≫ 0, for small ζ, still has d·ν < 0 on N_ℳ∖0, so it is in the interior of the tangent cone.
  - So m(X) + t(d+ζ𝟙) ∈ int ℳ for small t > 0, and the interior case applies. ∎

**Lemma 5.2 (hull facts; PROVED).**
- hull(B) ⊇ int ℝ³₊.
- hull(B) ⊇ int cone(B_d ∪ ℝ³₊), where B_d is the set of density points of B.
- In particular, hull(B) ⊇ b + ℝ_{>0}𝟙 for b ∈ B_d. Coherent models are closed upward along 𝟙.

*Proof.* By bipolarity, cl cone(B_d ∪ ℝ³₊) = C_{Q_B}, and its interior is D_{Q_B} (W62 Lemma D, open). ∎

**Lemma 5.3 (point certificate; PROVED).** Suppose:
- a is an interior point of N∖X;
- b₁, …, b_r are density points of X∖N;
- a − Σλ_k b_k ∈ int ℝ³₊ for some λ_k ≥ 0.

Then μ((N∖X) ∩ hull(X∖N)) > 0.

For cones, in the section Σh = 1, the last condition is equivalent to a ∈ int conv{b₁, …, b_r, e₁, e₂, e₃}. This is the test used by the scripts.

*Proof.* The condition is open in a, so a small ball around a lies in N∖X and in int cone(nbhd(b_k) ∪ ℝ³₊) ⊆ hull(X∖N) by Lemma 5.2. ∎

**Prop 5.4 (H) when X misses part of the positive orthant; PROVED.**
- If μ(int ℝ³₊ ∖ X) > 0, take N_π from Lemma 5.1.
- Then N_π∖X ⊇ int ℝ³₊∖X, which is non-null and contained in every hull. ∎

**Prop 5.6 (exact certificate for a class of collar rivals; PROVED with CHECKED inequalities, `prop56.py`).**
- **Data.**
  - B_k: the thin box beyond the midpoint of face F_{v_k}, with depth 0 < −v_k·h < s(h)/10 and lateral |(v_i−v_j)·h| < s(h)/10, where s := (v_i+v_j)·h. Each box lies in U.
  - N := D_{Q_t} with t = 3/23.
  - C := ∪_k C_k^±: the polyhedral corner cones of the boxes, with lateral ∈ ±[0.096, 0.1) and depth ∈ [0.07, 0.09].
- **Claim.** For every measurable P ⊆ B₁∪B₂∪B₃ with μ(P∩C) > 0, the rival X := D_K ∪ P satisfies (H), with N as the coherent defender.

*Proof.*
- **Brier part, for every measurable P in the boxes.**
  - On B_k we have h_k > 0 and h_j < 0 (exact: the wrong-sign parts have mass 0).
  - So m_k(N) − m_k(X) = m_k(N∖D_K) − m_k(P∩B_k) − Σ_{j≠k} m_k(P∩B_j) ≥ m_k(N∖D_K) − m_k(B_k).
  - This equals 0.0024928 > 0 exactly, for each k by symmetry.
- **Hull part.**
  - For a density point p of P ∩ C₁⁺ put y(p) := p + (s(p)/9)(e₃ + (e₁+e₂)/1000). This is linear in p.
  - At the four extreme rays of C₁⁺, exact checks give all of the following, hence on the whole cone:
    - C₁⁺ ∩ N = ∅;
    - y ∈ N;
    - v₁·y < 0, so y ∉ D_K;
    - y lies outside B₁ laterally;
    - v₂·y > 0 and v₃·y > 0, so y ∉ B₂ ∪ B₃.
  - Then Lemma 5.3 applies with a = y(p) and b = p.
  - C₁⁻ is checked the same way with e₂. The other faces follow by the permutation symmetry of the configuration: K, K′, u, μ, the boxes and Q_t are all symmetric. ∎
- The class contains every collar trade of E61 type built from these boxes, for example P = B₁∪B₂∪B₃, where m(P) = 0.01182·(1,1,1) ≫ 0 (`collar.out`).
- *Consequence.*
  - For each such rival the record (P, ∅) is deleted only at world 1.
  - D_K ∪ P is strictly Brier-worse than N at every world, and the comparison is kept, so it is dominated by the coherent N.
  - N is itself undominated (Thm 3.2(i)).

**5.5 Further evidence for (H).**
- **(i) Exact certificates (CHECKED, `t1c.out`).** Two unions of Bayes acts X = N_{p₁} ∪ N_{p₂}, whose lines meet at c ∈ U:
  - (p₁, p₂) = ((1/5, 13/40, 19/40), (1/5, 1/8, 27/40)): 6 of 6 sampled strict Bayes dominators certified;
  - (p₁, p₂) = ((3/8, 3/8, 1/4), (1/4, 19/40, 11/40)): 5 of 5 certified.

  Part of the mechanism is general:
  - *PROVED, by Lemma 3.3:* any strict Bayes dominator N_q must exclude part of *both* lobes N_{p₁}∖N_{p₂} and N_{p₂}∖N_{p₁}. Otherwise X∖N_q ⊆ N_{p₁}, say, and r(N_q, X) would attack the Bayes act N_{p₁}.
  - *Observed in every certified instance, not proved in general:* the line of N_q passes just beyond c, and the triangle (c, c₁, c₂) lies in hull(X∖N_q) by the chord argument (the boundary of X is concave at c).

  The best slacks are tiny (4·10⁻⁴ and 4·10⁻⁵), so this is a sharp test.
- **(ii) Random holes and bumps (NUMERICS, `hunt3.out`).**
  - The rivals are Bayes act minus a conic hole, Bayes act plus a conic bump, and deep holes.
  - Defenders tried: Bayes acts, Bayes acts cut by a second half-space, and thin cuts along the faces of U (q′ near a vertex of K′). The last are needed for deep holes, as predicted by Lemma 5.2's "shadow" geometry.
  - Seed 5, 10 rivals of each kind (`hunt3.out`). Certified, exactly: deep holes 4/10, holes 7/10, bumps 6/10.
  - The remaining 13 cases are of two kinds:
    - 5 cases: the local search found no strict Bayes dominator, although one exists by Lemma 5.1;
    - 8 cases: a dominator was found, with slack between 3·10⁻⁷ and 1.2·10⁻⁴, but no certificate within the restricted defender family (one Bayes act, at most one extra cut) and the 9 000 sample points.
  - These are search failures. They are not shown to violate (H), and they are not evidence for it either.
  - The certified cases include holes, bumps and deep holes. The deep holes needed the U-face cuts, as predicted.
- **(iii) Mechanism.** In every certified case the defender "cuts through" X at a defect, in one of two ways:
  - it removes a little of X on the far side of a point a ∉ X, as seen from the positive orthant (Lemma 5.2);
  - it adds a, paid for by Brier slack. The slack exists because a Bayes act strictly dominates X (Lemma 5.1).

  A proof of (H) needs a uniform version: a non-convexity witness of X near the boundary of some strict Bayes dominator, or near the faces of U, at a cost below the slack. The two delicate configurations are deep holes far from every face, and defects of size comparable to the slack. I have not closed this.

**CONJECTURE H.** (H) holds for every incoherent model, for every μ with a positive continuous density and finite first moment, and every U = D_{K'} with K' ⊆ relint Δ.

**What remains to globalise, exactly:**
- (H) for all incoherent X; or
- (★) for some smaller family 𝒩 ∋ D_K, in which case the coherent models outside 𝒩 must also be dominated (Thm 3.2(ii)).

Everything else in the cover is PROVED (Theorem 3.2).

---

## 6. Remarks for the author

1. **Target independence.** With 𝒩 = all coherent models the mechanism protects every coherent model at once. If (H) holds, the binding framework therefore has a *universal* complete-class property: the undominated models are exactly the coherent ones. The reversed triangle is then not special.
   - The author may want to decide whether this is intended. Deleting exactly the comparisons that would dominate a coherent model is legitimate under (TC). It is the "incomparability, rather than more elaborate prices" that AUDIT_r64 §3 anticipated.
   - If such relations are to be excluded, a further axiom is needed. Two candidates:
     - (TP), which E61 used;
     - a closure condition on the accepted records, such as "if r is accepted at i and r′ is pointwise at least as good as r at i, then r′ is accepted".

     Both are transitivity-like. Lemma 1.3 shows that (TC) alone cannot exclude deletions.
2. **What the negative side must do.** Under (TC) alone, an impossibility proof for the reversed triangle must produce, for every family 𝒩 ∋ D_K of coherent models, a rival with no un-attacked Brier-dominating defender in 𝒩.
   - The proof must also apply to rankings not built on Brier. Theorem 3.2 is only a sufficient construction.
   - In particular, the existence part of the cover, not the protection part, is where any obstruction must live. Protection is free: Theorem 3.2(i) holds for every 𝒩, with no condition.
3. **Other base scores.** Lemma 1.3 applies to any complete score order with strict (G); veto–Brier orders are an example. Only an order whose undominated models are all coherent is useful as a base, because deletion only enlarges the undominated set. Brier is the natural base: its undominated models are the Bayes acts.

---

## 7. Status table

| Item | Status |
|---|---|
| Lemma 1.1 (IB) ⟺ record relations | PROVED |
| Lemma 1.2 (TC) ⟺ 3-cycle reversal closure | PROVED |
| **Lemma 1.3 deletion lemma: sub-relations of a weak order that are symmetric on ties satisfy (TC)** | **PROVED** |
| Lemma 2.1 strong priority region ⇒ box model undominated, using strict (G) only (lead's observation) | PROVED |
| Lemma 2.2 under (TC), E61-type priority ⇒ the box dominator is incomparable with M_R | PROVED |
| Lemma 2.3 a pure-guidance world ⇒ no cover of any target | PROVED |
| §2.4 explicit (TP) failure in a deletion relation (E61 Lemma 3.1 mechanism absent) | CHECKED |
| **Prop 2.5 deletion relations have no priority region at any world** (E61 Cor 3.2, Lemma 3.4, Cor 5.3 inapplicable) | **PROVED** |
| **Thm 3.2 reduction: Δ(𝒩) satisfies all axioms; members of 𝒩 have no weak dominators; (★) ⇒ undominated = 𝒩, direct (C), (W), incoherent dominance; D_K ∈ 𝒩 ⇒ cover** | **PROVED** |
| Lemma 3.3 Bayes acts are never attacked by strictly improving records | PROVED |
| Prop 3.4 𝒩 = ℬ∪{D_K}: X₁ = D_K∪P₁ has no admissible Bayes defender (102/102 grid dominators contain P₁) | CHECKED on grid; general claim NUMERICS |
| Cor 3.5 (H) ⇒ universal cover (every coherent model undominated; every K with K′ ⊆ relint K covered) | PROVED given (H) |
| Lemma 4.1 protection transfer (defence records may not attack C* incoherently) | PROVED |
| Lemma 4.2 collar refusal at some world, in every context, by a world where P has wrong part | PROVED |
| Lemma 4.3 the defender of D_K∪P drops part of P (or gives a coherent tie) | PROVED |
| Lemma 5.1 every non-Bayes model is strictly dominated (all coordinates) by a Bayes act | PROVED |
| Lemma 5.2 hull facts (positive orthant; cones; upward along 𝟙) | PROVED |
| Lemma 5.3 point certificate for the hull condition | PROVED |
| Prop 5.4 (H) when X misses part of the positive orthant | PROVED |
| **Prop 5.6 (H) for all D_K∪P, P ⊆ B₁∪B₂∪B₃ measurable with mass in the box corners; includes E61-type collar trades** | **PROVED (exact inequalities CHECKED)** |
| §5.5(i) T1 unions of Bayes acts: all sampled strict dominators certified (6/6, 5/5) | CHECKED (instances) |
| §5.5(ii) random holes, bumps, deep holes: 17/30 certified exactly; 13 search failures (5 with no dominator found, 8 with no certificate in the restricted family); no violation of (H) shown | NUMERICS (each certificate CHECKED) |
| **CONJECTURE H** (universal) | CONJECTURE |
| Full cover of the reversed triangle under the binding framework | open; reduced exactly to (H), or to (★) for some 𝒩 ∋ D_K |

## 8. Files (`es64py/`)

| File | Content |
|---|---|
| `cones.py` | exact moments of polyhedral cones under e^{−\|h\|₁} (orthant clipping, simplicial formula \|det\|·Σg) |
| `geom.py` | reversed triangle, U = D_{K′}, boxes beyond faces |
| `pi_dk.py` / `.out` | Bayes acts strictly dominating D_K (min π_k = 0.267) |
| `bump.py` / `.out` | X₁ = D_K∪P₁: all strict Bayes dominators contain P₁; defender D_{Q_t} with exact certificate |
| `collar.py` / `.out` | collar trade; deletion at world 1; explicit (TP) failure |
| `prop56.py` / `.out` | Prop 5.6 exact inequalities |
| `t1.py`, `t1gap.py`, `t1b.py`, `t1c.py` / `t1c.out` | unions of two Bayes acts; exact certificates |
| `hunt.py`, `hunt2.py`, `hunt3.py` / `hunt3.out` | random searches (NUMERICS); `hunt3` is the final version |
