# OR64 — An ordinal collar argument under (TC) (25 Oct 2026)

Role: OR64 (main negative task, Brief 64). One author; nothing here is refereed.

Labels: **PROVED** (complete argument here) / **CHECKED** (exact computation; scripts in `or64py/`, run with `python3 -I`) / **CONJECTURE** / **NUMERICS** (none used).

Scripts:
- `or64py/geom.py` → `geom.out`: exact geometry of the reversed triangle, the collar centres, and one exact witness for the collar-hull step.
- `or64py/records.py` → `records.out`: finite-atom versions of the record calculus, of the counter-model M1, of the strict-priority repair, and of the diagnostic relation 𝒯. Every check is exhaustive over all model triples except where it says "random".

The proofs below are measure-theoretic and do not depend on the scripts. The atom checks are guards against slips.

---

## 0. Verdict in plain English

1. **E61's box lemma is false under (TC) for E61's own definition of a priority region (PROVED, explicit counter-model M1, §2.2).**
   - M1 has three worlds and two specially accepted records. It satisfies reflexivity, strict (G), (IB) and (TC).
   - World j has a priority region R in E61's sense. Yet the box model X_i = (U∖R) ∩ {h_i > 0} is dominated.
   - (TC) does not imply (TP).
2. **Two ordinal notions of priority restore the box lemma without transitivity (PROVED, §2.3).**
   - **Strong priority**: no model meeting R is ⪯_j any model avoiding R. With this, the box lemma needs strict (G) at i and nothing else (the lead's observation, confirmed).
   - **Strict priority**: M_R ≺_j Y for every Y meeting R. With this, the box lemma follows from (TC), and (TC) is genuinely needed (M1b).
   - E61's inclusion-veto corollary survives unchanged by a direct proof. E61's collar lemma survives for both ordinal notions.
   - Every priority region that E61, O61 and IN63 actually use (integral vetoes in lexicographic or unanimity orders, inclusion vetoes) is a strong priority region. So **no downstream theorem of rounds 61–63 is damaged**. What fails is only the claim that the box lemma holds at axiom level.
3. **The axioms do not force priority regions (PROVED, §2.6).** No strictly sign-correct single-level additive ranking has a strong or strict priority region, and normalised boxes are covered by such a ranking. A ranking that has vetoes is architecture.
4. **New necessary relational lemmas proved from the binding framework alone (criterion (C) met).**
   - **Record applicability and target transfer (Lemma T, §3.3).** By (IB), a record that witnesses a dominance applies to every context that matches it. So no dominance can move "away from" the target, or away from any undominated model.
     - Consequence, for every target: no incoherent model next to D_K is dominated by its coherent hull or by its coherent kernel. Dominators must cross the boundary.
     - If D_K itself dominates D_K ∪ P, then no undominated model contains P.
   - **Ordinal collar lemma (Lemma OC, §3.4).** Take any world j and any non-null set R of j-wrong gambles in the collar beyond the reversed triangle. Some coherent undominated model that accepts part of R dominates the dented box (U∖R) ∩ {h_i > 0}, for a suitable i ≠ j.
     - So world j accepts, at every world and in every matching context, a record that adds R-gambles while removing none.
     - **No world can veto any non-null part of the collar, in any relational form**: incomplete, non-transitive, non-additive, refusing only coherent intruders.
     - The proof uses the incoherent-model dominance requirement, not "undominated ⇒ coherent" through a box lemma. It is a strict generalisation of E61 Lemma 3.4.
5. **Where the ordinal argument stops (PROVED diagnostic, §3.5).** An explicit relation 𝒯 satisfies reflexivity, strict (G), (IB) and (TC); it is incomplete and not transitive. Under 𝒯:
   - D_K is undominated;
   - D_K strictly dominates every model that is not pointwise at least as good as D_K at some world;
   - no world accepts any collar trade.

   Its undominated models are exactly D_K and the *one-world improvements* of D_K.
   - So **the collar trade, as a rival, yields no ordinal contradiction**.
   - Any axiom-level proof must extract its contradiction from the required coherent dominators of incoherent one-world improvements, for example the dented boxes of Lemma OC.
6. **Conditional impossibility (criterion (B), PROVED, Theorem VA, §3.7).** Assume hypothesis (VA): every world's protection of the collar is a relational veto (VA1), and outside its veto region every world accepts collar trades that raise its own summed payoff (VA2). Then no cover of the reversed triangle exists.
   - This contains E61 Cor 5.3 and extends it to incomplete, non-transitive, non-additive orders.
   - (VA2) is the one acceptance hypothesis, and it is where a price enters. The argument has no other source of acceptances (diagnostic 𝒯).
   - This is a scoped result, **not** an axiom-level one.
7. **Criterion (A) is not achieved. Calibration (PROVED, §3.8):** an axiom-level impossibility for the reversed triangle would in particular settle negatively the open measurable-chart realisation problem of E61 §5 and O61 §7. That problem asks for strictly sign-correct integrable charts all of whose Bayes acts are coherent, with D_K a unique Bayes act. Such charts give complete, transitive (IB) rankings inside the binding framework. So (A) is at least as hard as a problem the project has left open since round 61.
8. **Architecture ledger (§4).** Each existing exclusion crosses into architecture at an identifiable step:
   - E61 Cor 5.3: the Brier comparison.
   - O61 Thm A: scalarising the target's error vector into one prior (Lemma 2 and step 2).
   - IN63 Thm C: Lyapunov plus separation into view weights, followed by supporting-face concavity analysis.
   - DC63 Thm DC and C62 Thm 4.1: a single numerical chart from the outset.
   - None of them uses (TP) outside a class where it holds automatically.

---

## 1. Framework, and the record calculus

Binding framework as in BRIEF64 / AUDIT_r64:
- Ω = {1,2,3}; μ has a positive density.
- Models are measurable X ⊆ U modulo null sets, on a decomposable U with (LF) at D_K.
- Each ⪯_w is reflexive, ties a.e.-equal models, and satisfies (TC): A ⪯ B, B ⪯ C ⇒ ¬(C ≺ A).
- Strict (G) and (IB) are as in W62 §2.

Notation:
- pos_w := {h_w > 0} and neg_w := {h_w < 0}. Hyperplanes are null.
- B_w := U ∩ pos_w is the world-w-best model.
- D_K is the open cone on r_j = 2·𝟙 − 5e_j; F_k := cl D_K ∩ v_k^⊥ = cone(r_i, r_j). F_k lies in pos_k and crosses h_i = 0 and h_j = 0 in its relative interior (CHECKED, `geom.out` §2).
- C = C_1 ∪ C_2 ∪ C_3 is E61's open collar, with C_k beyond relint F_k. Its depths δ_k(p) are shrunk if necessary so that C_k ⊆ pos_k ∩ U. This uses (LF) and h_k > 0 on F_k∖0.

**Records.** For models X, Y put rec(X,Y) := (X∖Y, Y∖X), a pair of disjoint sets. A record (A,N) *applies* to Z if N ⊆ Z and A ∩ Z = ∅ a.e. Its *result* is Z ⊕ (A,N) := (Z∖N) ∪ A, which is again a model by decomposability.

**Prop 1.1 (record form of (IB); PROVED).** (IB) holds iff for each w there is a set Acc_w of records with X ⪯_w Y ⟺ rec(X,Y) ∈ Acc_w.

*Proof.*
- (⇒) Take S = X△Y in (IB): X ⪯_w Y depends only on (X∩S, Y∩S) = rec(X,Y).
- (⇐) If X, Y and X′, Y′ agree off S with the same traces on S, then rec(X,Y) = rec(X′,Y′). ∎

In record terms:
- (G) says: every *guided* record (A,N) (A ⊆ pos_w, N ⊆ neg_w) lies in Acc_w, and the inverse (N,A) of a non-null guided record does not.
- Call a non-null (A,N) *anti-guided* at w if (N,A) is guided.

**Prop 1.2 (composition; PROVED, CHECKED `records.out` §0).**
- For models A, B, C, with r_1 = rec(A,B) = (P_1,N_1) and r_2 = rec(B,C) = (P_2,N_2): P_1 ∩ P_2 = N_1 ∩ N_2 = ∅, and

  rec(A,C) = r_1∘r_2 := ((P_1∖N_2) ∪ (P_2∖N_1), (N_1∖P_2) ∪ (N_2∖P_1)).

  Composition is commutative.
- Conversely, every pair with P_1 ∩ P_2 = N_1 ∩ N_2 = ∅ arises this way.
- So (TC) at w is the condition: for composable r_1, r_2 ∈ Acc_w, (r_1∘r_2)⁻¹ ∈ Acc_w ⇒ r_1∘r_2 ∈ Acc_w.

*Proof.*
- Classify points by membership vectors (a,b,c) ∈ {0,1}³: P_1 = {a=1,b=0}, N_1 = {a=0,b=1}, and so on. Direct bookkeeping gives the formula.
- For the converse, the sets N_1 ∪ P_2 and P_1 ∪ N_2 are disjoint, by disjointness of each record and composability. Take B := N_1 ∪ P_2, A := (B∖N_1) ∪ P_1 and C := (B∖P_2) ∪ N_2. Then rec(A,B) = r_1 and rec(B,C) = r_2. ∎

**Prop 1.3 (TC plus completeness is transitivity; PROVED).**

*Proof.* If ⪯ is complete, ¬(C ≺ A) means ¬(C ⪯ A) or A ⪯ C, and completeness turns ¬(C ⪯ A) into A ⪯ C. Hence (TC) gives A ⪯ B ⪯ C ⇒ A ⪯ C. The converse is trivial. ∎

So the only new freedom of the binding framework over total preorders is **incompleteness**.

**Prop 1.4 (what (TC) propagates; PROVED).**
- (a) If A ⪯ B and C ≺ A, then B ⋠ C. Strict comparisons propagate refusals forward.
- (b) If Y′ is pointwise at least as good as Y at w and Y ⪯_w X, then ¬(X ≺_w Y′). So an improvement of an accepted rival is accepted or incomparable, never strictly beaten.
- (c) A mere refusal Y ⋠ X propagates nothing. M1 (§2.2) is an example.
- (d) For a record r ∈ Acc_w and a guided g with r∘g defined, r∘g is never anti-guided at w.

  *Proof of (d).* r∘g keeps r's good parts P∩pos_w and N∩neg_w, and adds only good parts. It is anti-guided only if r is. So (TC) with one guided step never yields a contradiction. A (G)/(TC) contradiction needs **two non-guided accepted records** at one world whose composite is anti-guided.

---

## 2. Audit of E61 §3 under (TC)

### 2.1 What E61 uses
E61 Lemma 3.1 (pointwise-best) concatenates Y ⪯_j X* with X* ⪯_j M to obtain Y ⪯_j M. This is (TP).

It is used in:
- Cor 3.2 (box lemma), with X* = X_i := (U∖R) ∩ pos_i and M = M_R := (U∖R) ∩ neg_j;
- Cor 3.3, with X* = X_E.

Lemma 3.4 uses Cor 3.2 only to make X_i coherent. Cor 5.3, Thm 5.1, Cor 5.2 and IN63 Thm C use Lemma 3.4.

**E61's definition.** R ⊆ U ∩ neg_j is a priority region at j if no Y with μ(Y∩R) > 0 has Y ⪯_j M_R.

### 2.2 Question (i): the box lemma fails under (TC) for E61's definition

**Prop 2.1 (counter-model M1; PROVED).** Let {i,j,k} = {1,2,3}, and let U be any one-sided domain (for instance D_u, or D_{K′}) in which the following orthant pieces are non-null. Choose non-null measurable sets:
- E ⊆ U ∩ {h_i > 0, h_j < 0, h_k > 0};
- A ⊆ U ∩ {h_i < 0, h_j > 0, h_k > 0};
- B ⊆ U ∩ {h_i > 0, h_j > 0, h_k < 0}.

Put r_0 := (E ∪ A, B), and let R ⊆ U ∩ neg_j be any measurable set with E ⊆ R. Define:
- Acc_i := G_i ∪ {r_0};
- Acc_j := G_j ∪ {r_0};
- Acc_k := G_k,

where G_w is the set of guided records at w. Then:
- (a) all three relations are reflexive, tie a.e.-equal models, and satisfy (IB), strict (G) and (TC);
- (b) R is a priority region at j in E61's sense;
- (c) Y_0 := (X_i∖B) ∪ E ∪ A dominates X_i := (U∖R) ∩ pos_i, and μ(Y_0 ∩ R) ≥ μ(E) > 0.

So the conclusion of E61 Cor 3.2 fails. (TC) does not imply (TP): Y_0 ⪯_j X_i, and X_i is pointwise at least as good at j as M_R, yet Y_0 ⋠_j M_R.

*Proof.*
- **(IB).** By Prop 1.1 it is automatic.
- **Strict (G).** G_w ⊆ Acc_w. The inverse of a non-null guided record is never r_0:
  - at i, r_0⁻¹ = (B, E∪A) would need E ⊆ neg_i, but E ⊆ pos_i;
  - at j, it would need A ⊆ neg_j, but A ⊆ pos_j.
- **(TC) at k.** G_k is closed under composition.
- **(TC) at j.**
  - Composites of two guided records are guided.
  - r_0∘r_0 is defined only if E∪A = ∅.
  - Let g = (P_g, N_g) ∈ G_j with P_g ∩ (E∪A) = ∅. Since B ⊆ pos_j and N_g ⊆ neg_j, N_g ∩ B = ∅ is automatic. Then r := r_0∘g = ((E∖N_g) ∪ A ∪ (P_g∖B), (B∖P_g) ∪ (N_g∖E)), using A ∩ N_g = ∅.
  - r⁻¹ ∈ G_j would need A ⊆ neg_j, impossible since A is non-null in pos_j.
  - r⁻¹ = r_0 would need E ∪ A ⊆ (B∖P_g) ∪ (N_g∖E). But A is disjoint from B and from N_g. Impossible.
  - So r⁻¹ ∉ Acc_j, and (TC) holds.
- **(TC) at i.** The same computation with signs at i:
  - r = (E ∪ (A∖N_g) ∪ (P_g∖B), (B∖P_g) ∪ (N_g∖A)), using E ⊆ pos_i;
  - r⁻¹ ∈ G_i would need E ⊆ neg_i;
  - r⁻¹ = r_0 would need E ⊆ (B∖P_g) ∪ (N_g∖A), but E is disjoint from B and lies in pos_i, while N_g ⊆ neg_i. Impossible.
- **(b).**
  - Y ⪯_j M_R via G_j forces Y∖M_R ⊆ pos_j. But Y∩R ⊆ Y∖M_R lies in neg_j, so Y∩R is null.
  - Via r_0: rec(Y, M_R) = (E∪A, B) needs B ⊆ M_R ⊆ neg_j. But B is non-null in pos_j. Impossible.
- **(c).**
  - B ⊆ X_i, because B avoids R ⊆ neg_j. Also E∪A is disjoint from X_i, because E ⊆ R and A ⊆ neg_i.
  - So rec(Y_0, X_i) = r_0 ∈ Acc_i ∩ Acc_j.
  - At k, Y_0∖X_i = E∪A ⊆ pos_k and X_i∖Y_0 = B ⊆ neg_k, so Y_0 ≺_k X_i by strict (G). ∎

CHECKED on an 8-atom version (`records.out` §1): exhaustive (TC) over all 2⁸·³ triples, strict (G), random (IB) tests, priority, domination, and both incomparabilities. It finds 2788 non-transitive chains.

*Mechanism.* (IB) copies r_0 to every context that matches it. The copy to M_R is blocked because r_0 removes B, which is j-correct and lies in X_i but not in M_R. This is exactly the gap between "refused against M_R" and "refused against every R-avoiding model".

### 2.3 Question (ii): ordinal notions of priority that work

Call R ⊆ U ∩ neg_j:
- **strong priority at j** if μ(Y∩R) > 0 and μ(Z∩R) = 0 imply Y ⋠_j Z;
- **strict priority at j** if μ(Y∩R) > 0 implies M_R ≺_j Y.

Both imply E61's notion.

**Lemma 2.2 (box lemma, strong form; PROVED; uses strict (G) at i only).** If R is a strong priority region at j, then for every i ≠ j, X_i := (U∖R) ∩ pos_i is undominated.

*Proof.*
- Let Y weakly dominate X_i. From Y ⪯_j X_i, with X_i avoiding R, strong priority gives Y∩R null.
- Among models inside U∖R, X_i is pointwise at least as good at i as every other. If Y ≠ X_i a.e., strict (G) gives X_i ≺_i Y, contradicting Y ⪯_i X_i. ∎

No transitivity, no (TC) and no completeness is used.

**Lemma 2.3 (box lemma, strict form; PROVED; uses (TC) at j and strict (G) at i).** If R is a strict priority region at j, the same conclusion holds.

*Proof.*
- Let Y weakly dominate X_i. Then X_i ⪯_j M_R by weak (G), since X_i∖M_R ⊆ pos_j and M_R∖X_i ⊆ neg_j.
- If Y met R, strict priority would give M_R ≺_j Y. The chain Y ⪯_j X_i ⪯_j M_R then contradicts (TC).
- So Y ⊆ U∖R, and the pointwise argument of Lemma 2.2 finishes. ∎

**(TC) is needed in Lemma 2.3 (PROVED, CHECKED `records.out` §1b).** Add to Acc_j of M1 the records rec(M_R, Y) for all Y meeting R. Then:
- R becomes a strict priority region;
- Y_0 still dominates X_i;
- (TC) fails exactly on Y_0 ⪯_j X_i ⪯_j M_R ≺_j Y_0.

CHECKED (`records.out` §2): 468 random non-transitive systems were tested, each with R a strict priority region and each satisfying (G) and (TC). In none of them is X_i dominated.

**Prop 2.4 (E61 Cor 3.3 survives directly; PROVED).** Suppose j *inclusion-vetoes* R, that is, Y ⪯_j X ⇒ Y∩R ⊆ X∩R. For E ⊆ R, the model X_E := ((U∖R) ∪ E) ∩ pos_i is undominated.

*Proof.* A weak dominator Y has Y∩R ⊆ X_E∩R ⊆ E, by the veto applied to Y ⪯_j X_E itself. Then argue pointwise as in Lemma 2.2. ∎

The rest of E61's proof, the density-point argument as repaired by the round-61 referee, is unchanged. So inclusion vetoes are impossible for every target under the binding framework.

**Prop 2.5 (E61 Lemma 3.4 for ordinal priority; PROVED).** If R is a strong or strict priority region at some world j with μ(R∩D_K) = 0, then μ(R∩C) = 0.

*Proof.* E61's proof uses the order only through "X_i is undominated, hence coherent". Lemmas 2.2 and 2.3 supply this. The rest is geometry. An exact instance of the hull step is in `geom.out` §4: there x = (1−t)A + tB, with A ∈ D_K ∩ pos_1 and B ∈ U ∩ {h_1 > 0, h_2 > 0}, and x a 2-wrong point beyond F_1. ∎

Lemma OC (§3.4) is a stronger version.

**Prop 2.6 (the regions actually used are strong; PROVED).**
- (a) Let φ ≥ 0 be a leading integral veto in a lexicographic order, or in one view of a unanimity order, with R = {φ > 0}. Then R is strong. If μ(Y∩R) > 0 = μ(Z∩R), then ∫_Y φ > 0 = ∫_Z φ, so that view, and hence the world, strictly prefers Z, and Y ⋠ Z.
- (b) Unions over views of such regions are strong, for the same reason.
- (c) IN63's R_v = {φ_v > 0} ∪ {c_v < 0} for views with c_v ≤ 0 vanishing off R_v is strong. A Y meeting R_v loses at the first or the second level of view v against every Z avoiding R_v.
- (d) Inclusion-veto regions are strong.

E61's depth-leximax and Pareto vetoes were not re-checked.

**Consequence.** E61 Cor 5.3, Thm 5.1 and Cor 5.2, O61 Thms A and B (which never use Lemma 3.1), and IN63 Thm C are unaffected by the (TP) issue. Their classes are transitive anyway, and their priority regions are strong. Only the reading of Lemma 3.1 or Cor 3.2 as axiom-level statements is false.

### 2.4 Question (iii): are priority regions forced?

**Prop 2.7 (PROVED).** Let X ⪯_w Y ⟺ ∫_X f_w ≤ ∫_Y f_w, with f_w integrable, f_w < 0 a.e. on U ∩ pos_w, and f_w > 0 a.e. on U ∩ neg_w. Then no world has a non-null strong or strict priority region.

*Proof.* Let R ⊆ neg_j be non-null and G ⊆ U ∩ pos_j∖R be non-null.
- Pick E ⊆ R with 0 < ∫_E f_j < −∫_G f_j. This is possible by absolute continuity of the integral.
- Then Y := E ∪ G meets R and Y ≺_j ∅, while ∅ avoids R. So R is not strong.
- Also M_R ∪ E ∪ G ≺_j M_R, which contradicts strict priority. ∎

Normalised boxes are covered by the single-level box chart (FD62 Prop FD-B, refereed CORRECT), which is of this form. So **the binding requirements do not force priority regions in general**. "Some world vetoes the collar" is architecture.

For the reversed triangle, Lemma OC below shows that the requirements *forbid* every relational veto of any non-null part of the collar. Whether they force some veto elsewhere is open. I know no argument either way.

---

## 3. The ordinal argument

### 3.1 Rivals (item 1)
All rivals are measurable models in U. Here P_k ⊆ C_k denotes a piece beyond F_k, and R ⊆ C ∩ neg_j.
- (R1) **Collar models** D_K ∪ P, with P ⊆ U∖cl D_K. *Collar trade*: P = P_1 ∪ P_2 ∪ P_3, with P_k a small ball around c_k := m_k − δv_k, where m_k := r_i + r_j.
  - Each c_k is beyond F_k only, with sign pattern (+,−,−) up to permutation.
  - Σc_k = (2−δ)𝟙 (CHECKED, `geom.out` §3).
- (R2) **One-world collar models** D_K ∪ P with P ⊆ pos_w for one w. For example, a single piece P_w.
- (R3) **Dents** D_K∖P′, with P′ ⊆ D_K.
- (R4) **Dented boxes** X_i(R) := B_i∖R.
- (R5) **One-world improvements of D_K**: 𝓘_w := {(D_K∖N) ∪ A : N ⊆ D_K ∩ neg_w, A ⊆ (U∖D_K) ∩ pos_w}. This contains R2, B_w, and the R4 with R ⊆ C_i (for w = i).

### 3.2 Forced comparisons (item 2)
- (F1) **Guidance.** Guided records are accepted and their inverses refused (strict (G)).
- (F2) **World-best models (fact (a), PROVED).** B_w is undominated by strict (G) alone: any Y ≠ B_w a.e. has B_w ≺_w Y. So B_w is coherent, B_w = D_{Q_w} a.e.
- (F3) **Target protection (fact (b), PROVED; a disjunction over worlds).**
  - If Y is incoherent, then rec(Y, D_K) ∉ Acc_w for some w. Otherwise Y weakly dominates D_K; since D_K is undominated, Y would be tied with it at every world; direct (C) would then make Y coherent.
  - By (IB) this refusal holds in every context to which the record applies.
  - For Y = D_K ∪ P this is non-trivial **only if P meets pos_w for every w**. If P ⊆ neg_w, strict (G) already refuses at w. For the collar trade the refusing world is an unresolved disjunction w(P) ∈ {1,2,3}.
- (F4) **Required dominators (fact (c); a disjunction over credal sets and over the strict world).** Every incoherent X has a coherent undominated D_Q with rec(D_Q, X) ∈ ∩_w Acc_w and rec(X, D_Q) ∉ Acc_w for some w.
- (F5) **(TC) propagation.** Only as in Prop 1.4.
- (F6) **Direct (C).** All-world ties with coherent undominated models are coherent and undominated.

### 3.3 How (IB) transfers comparisons (item 4)

**Prop 3.1 (record applicability; PROVED).** Call (A,N) a *dominance record* if it lies in ∩_w Acc_w and its inverse is missing from some Acc_w. Then Z is dominated iff some dominance record applies to Z. The dominator is then Z ⊕ (A,N).

*Proof.* (⇒) rec(Y,Z) applies to Z. (⇐) By Prop 1.1, acceptance and refusal depend only on the record. ∎

**Lemma T (target transfer; PROVED; any target, any decomposable U).** Let C* be undominated, and let (A,N) be a record with A ∩ C* = ∅ and N ⊆ C* (it moves *away* from C*). Then:
- (a) (A,N) is not a dominance record;
- (b) if (A,N) ∈ ∩_w Acc_w, then C* ⊕ (A,N) is tied with C* at every world. If C* is coherent, C* ⊕ (A,N) is then coherent and undominated by direct (C).

*Proof.*
- (a) is Prop 3.1 applied to Z = C*.
- (b) (A,N) applies to C*, so C* ⊕ (A,N) ⪯_w C* for every w. Undominatedness forces the reverse comparisons. ∎

**Corollaries (PROVED).** Take C* = D_K. Let X be incoherent with dominator D_Q.
- (T1) If X = D_K ∪ P with P ∩ D_K = ∅, then μ(P∖D_Q) > 0. **No dominator of a collar model keeps the whole addition.** In particular D_K ∪ P is never dominated by a coherent superset, such as its coherent hull.
- (T2) If X = D_K∖P′ with P′ ⊆ D_K, then μ(D_Q ∩ P′) > 0. **No dent is dominated by a coherent subset**, such as its coherent kernel.
- (T3) If D_K dominates D_K ∪ P, then no undominated model contains P.
  - The dominance record (∅, P) applies to every Z ⊇ P.
  - The refusal of (P, ∅) at the strict world transfers by (IB), so the dominance is strict at that world.

These exclude, for every target, the cover mechanisms "dominate an incoherent model by its coherent completion" (outer or inner). They are not scoring arguments.

### 3.4 Required coherent dominators of dented boxes (item 3): the ordinal collar lemma

**Lemma OC (PROVED; reversed triangle; any decomposable U with (LF) at D_K).** Assume strict (G) and incoherent-model dominance. Let j be a world, i ≠ j, and R ⊆ U ∩ neg_j measurable with μ(R∩D_K) = 0 and μ(R∩C_i) > 0. Then X_i := (U∖R) ∩ pos_i is incoherent. Every coherent undominated D_Q that dominates it (one exists) satisfies:
- (a) μ(D_Q ∩ R ∩ pos_i) > 0. Hence Q ⊉ K, and if R ⊆ C_i then v_i ∉ Q.
- (b) D_Q ≠ D_K and D_Q ≠ B_i.
- (c) rec(D_Q, X_i) = (A,N) is a dominance record with μ(A∩R) > 0 and μ(N∩R) = 0. So world j, like every world, accepts a record that adds j-wrong gambles of R and removes none of R. By (IB) it accepts it in every context to which the record applies.

*Proof.*
1. **Incoherence.**
   - Suppose X_i = D_{Q′} a.e. Then X_i contains a.e. the open sets O_1 := D_K ∩ pos_i (since R misses D_K) and O_2 := U ∩ pos_i ∩ pos_j (since R ⊆ neg_j).
   - By W62 Lemma `lem:open`, O_1 ∪ O_2 ⊆ D_{Q′}. By convexity, conv(O_1 ∪ O_2) ⊆ D_{Q′}.
   - E61's collar geometry gives C_i ⊆ conv(O_1 ∪ O_2). It uses (LF) only; exact instance in `geom.out` §4.
   - Hence C_i ⊆ X_i a.e. But X_i ∩ R = ∅ and μ(R∩C_i) > 0. Contradiction.
2. **Existence.** Incoherent-model dominance supplies D_Q.
3. **(a).**
   - If μ(D_Q ∩ R ∩ pos_i) = 0, then D_Q∖X_i ⊆ neg_i a.e., because U ∩ pos_i∖X_i = R ∩ pos_i. Also X_i∖D_Q ⊆ pos_i.
   - So X_i is pointwise at least as good at i as D_Q, and differs from it (one is coherent, the other not). Strict (G) gives X_i ≺_i D_Q, contradicting D_Q ⪯_i X_i.
   - D_Q then contains gambles outside cl D_K, so Q ⊉ K. If those gambles lie beyond F_i, then v_i·h < 0 < q·h for all q ∈ Q, so v_i ∉ Q.
4. **(b).**
   - D_K ∩ R is null, so D_Q ≠ D_K by (a).
   - rec(B_i, X_i) = (R ∩ pos_i, ∅) adds only j-wrong gambles, so it is anti-guided at j and B_i ⋠_j X_i. Hence D_Q ≠ B_i.
5. **(c).** A = D_Q∖X_i ⊇ D_Q ∩ R ∩ pos_i, and N ⊆ X_i misses R. ∎

**Corollary OC (collar non-veto; PROVED).** For every world j and every non-null R ⊆ C ∩ neg_j:
- R meets some C_i with i ≠ j, because C_j ⊆ pos_j;
- some coherent undominated model meeting R ∩ pos_i dominates (U∖R) ∩ pos_i.

So:
- no non-null part of the collar is a strong priority region, a strict priority region, or (with (TP)) an E61 priority region at any world;
- more generally, no world j can refuse, against the dented box, every coherent undominated model that accepts R-gambles.

This is the transitivity-free, completeness-free and measurement-free form of E61 Lemma 3.4. Its hypothesis is weaker than E61's ("X_i is not dominated by a coherent undominated R-acceptor" instead of "X_i is undominated"), and it uses the dominance requirement rather than a box lemma.

**What the forced dominators look like (summary for item 3).**
- Dominators of collar models drop part of the addition (T1).
- Dominators of dents refill part of the dent (T2).
- Dominators of dented boxes are coherent undominated models, other than D_K and B_i, whose credal sets omit v_i and which accept collar gambles wrong at j (Lemma OC).

None of these is forced to be D_K, and none is forced to accept a collar trade against D_K.

### 3.5 Where the argument stops: the diagnostic relation 𝒯

Write IN := D_K and OUT := U∖D_K. Define, for each w,

  Acc_w := G_w ∪ T_w,  T_w := {(F,N) non-null : F ⊆ D_K, N ⊆ OUT, (F,N) not anti-guided at w}

("move toward the target, unless that is pointwise worse at w").

**Prop 3.5 (PROVED; CHECKED on a 9-atom version, `records.out` §3).** 𝒯 has the following properties.
- (a) It is reflexive, ties a.e.-equal models, and satisfies (IB), strict (G) and (TC). It is neither complete nor transitive.
- (b) D_K is undominated, and no model other than D_K is tied with it at every world.
- (c) D_K strictly dominates (≺ at every world) every model that is not pointwise at least as good as D_K at some world.
- (d) The undominated models are exactly D_K and the one-world improvements 𝓘 = ∪_w 𝓘_w.
- (e) No world accepts D_K ∪ P ⪯_w D_K for any P ⊆ OUT that meets neg_w for every w. In particular this holds for every collar trade, and D_K strictly dominates every such D_K ∪ P.

*Proof.*
1. **(a), (IB).** Automatic.
2. **(a), strict (G).** The inverse of a guided record is anti-guided, so it is not in T_w. It is not in G_w unless null.
3. **(a), (TC).**
   - G∘G ⊆ G.
   - Two composable records of T_w have no cancellations, since F ⊆ IN and N ⊆ OUT. Their composite (F_1∪F_2, N_1∪N_2) is anti-guided only if both are. So it lies in T_w.
   - For r = (F,N) ∈ T_w and composable g = (P_g,N_g) ∈ G_w, the composite is ((F∖N_g) ∪ (P_g∖N), (N∖P_g) ∪ (N_g∖F)).
     - If its inverse were in G_w, then N_g ⊆ F and P_g ⊆ N, and r would be anti-guided.
     - If its inverse were in T_w, then N ⊆ P_g and F ⊆ N_g, and again r would be anti-guided.
     - So the inverse is never accepted, and (TC) holds.
   - Non-transitivity: CHECKED, 626 260 chains A ⪯ B ⪯ C with A ⋠ C.
4. **(b).**
   - A record applying to D_K has N ⊆ IN and A ⊆ OUT. If it is in some T_w it is null.
   - So it lies in G_w for every w, hence it is Pareto-guided. It is then null, because D_K ⊇ U ∩ int ℝ³₊ and D_K ∩ ℝ³₋ = ∅.
5. **(c).**
   - rec(D_K, X) moves toward D_K. It is anti-guided at w exactly when X is pointwise at least as good as D_K at w.
   - rec(X, D_K) moves away from D_K, so it lies in no T_w, and in G_w only if X is pointwise at least as good at w.
6. **(d).**
   - Let X = (D_K∖N_X) ∪ A_X ∈ 𝓘_w, and let r = rec(Y,X) be accepted at every world.
   - At w, r ∈ T_w would make r anti-guided. So r ∈ G_w, which forces r = (A′ ⊆ OUT∖A_X, N″ ⊆ D_K ∩ neg_w∖N_X), a record moving away from D_K.
   - At every other world r must then be guided, so r is Pareto-guided and null.
   - Models outside 𝓘 are dominated by (c).
7. **(e).** Immediate from (c) and the definitions. ∎

**What 𝒯 shows (PROVED).**
- The axioms, together with the requirements on every model outside 𝓘 (target undominated, direct (C) at the target, and coherent undominated dominance of every incoherent model outside 𝓘), are jointly consistent with **every world refusing every collar trade**.
- So the collar trade by itself never produces an ordinal contradiction. "The collar trade improves Brier at every world" has no ordinal counterpart.
- 𝒯 fails only on 𝓘: its undominated set contains incoherent one-world improvements, for example D_K ∪ P_1 and the dented boxes of Lemma OC.
- **So any axiom-level proof must obtain its contradiction from the coherent dominators required by incoherent members of 𝓘.** These are the corner modifications and dented boxes of §3.4.

### 3.6 The possible final violations (item 5)
Under the binding framework a contradiction must take one of these forms:
- (V1) a dominance record applies to D_K;
- (V2) a dominance record applies to a required coherent dominator, or an incoherent model has no dominator;
- (V3) two non-guided accepted records at one world compose to an anti-guided record, or to a record whose inverse is accepted while it is refused (Prop 1.4(d));
- (V4) an incoherent model is tied at every world with a coherent undominated one;
- (V5) an accepted anti-guided record.

The forced data of §§3.2–3.4 produce none of these. 𝒯 realises (F1)–(F6) outside 𝓘.
- (V1) would need an incoherent X all of whose possible dominators move away from D_K. Lemma T shows these are excluded, not forced.
- (V3) would need two forced non-guided records that cancel each other's good parts at one world. The forced records of Lemma OC add j-wrong collar gambles at j while improving elsewhere. No pair of them was found to cancel, and I have no argument that one must.

**The argument stops here.**

### 3.7 Criterion (B): a conditional impossibility with the hypothesis named

**Hypothesis (VA) (ordinal "veto, then accept trades").** For each world j there is a measurable R_j ⊆ U ∩ neg_j with μ(R_j ∩ D_K) = 0 (the veto region; R_j = ∅ is allowed) such that:
- **(VA1) (relational veto).** For i ≠ j, no coherent undominated model D_Q with μ(D_Q ∩ R_j ∩ pos_i) > 0 dominates (U∖R_j) ∩ pos_i. This holds if R_j is strong priority, or strict priority, or E61-priority with (TP) at j.
- **(VA2) (acceptance of improving trades off the veto).** For every ε > 0 there is a measurable E_ε with μ(E_ε) < ε such that, for every j, every P ⊆ C∖(R_j ∪ E_ε) with ∫_P h_j dμ > 0 satisfies D_K ∪ P ⪯_j D_K.

**Theorem VA (PROVED; scoped, not axiom-level).** Under the binding framework and (VA), no ranking covers the reversed triangle.

*Proof.*
1. **The veto regions miss the collar.** By (VA1) and Lemma OC, μ(R_j ∩ C) = 0 for every j. If μ(R_j ∩ C_i) > 0 for some i ≠ j, Lemma OC produces exactly the dominator that (VA1) forbids. Also C_j ⊆ pos_j is disjoint from R_j.
2. **A collar trade.**
   - Fix δ small, so that c_k = m_k − δv_k ∈ C_k.
   - Choose radii ρ_k ≤ ρ with equal masses μ(B(c_k, ρ_k)) = m. This is possible since ρ ↦ μ(B(c,ρ)) is continuous and increasing from 0.
   - Since |h − c_k| ≤ ρ on B_k := B(c_k, ρ_k), we get ∫_{∪B_k} h dμ = m(Σc_k + O(ρ)) = m((2−δ)𝟙 + O(ρ)). This is ≥ γ𝟙 with γ > 0 for small ρ, and B_k ⊆ C_k.
   - Let M bound |h| on ∪B_k. Take ε < γ/M and P := ∪B_k∖E_ε. Then ∫_P h ≫ 0, and P ⊆ C∖(R_j ∪ E_ε) a.e. for every j.
3. **Incoherence.**
   - D_K ∪ P is incoherent. A cone D_Q ⊇ P a.e. contains tP′ for P′ := P ∩ D_Q, which is non-null, and every t > 0.
   - For t slightly larger than (|c_k|+ρ)/(|c_k|−ρ), the set tP′ is non-null, lies outside cl D_K (the complement of a cone is a cone), and misses ∪B_k. So D_Q ≠ D_K ∪ P a.e.
4. **Contradiction.** By (VA2), D_K ∪ P ⪯_j D_K for every j. This contradicts target-undominatedness together with direct (C) (F3). ∎

**Scope.**
- Theorem VA contains E61 Cor 5.3. In that class:
  - R_j is the union of the leading target-neutral veto regions over the views of world j, which is strong by Prop 2.6;
  - E_ε is the Yosida–Hewitt concentration set of the finitely additive levels;
  - every view is strictly better at Brier for P.
- It extends Cor 5.3 to incomplete, non-transitive, non-additive orders. The vetoes may be any relational structure satisfying (VA1).

**Why the extra hypothesis is needed by the argument.**
- (VA2) is the **only acceptance** in the proof. It is also the only place where a price, ∫_P h_j > 0, enters.
- Lemma OC uses (VA1) only to clear the collar.
- §3.5 shows that the binding framework's requirements outside 𝓘 are consistent with every world refusing every collar trade, so (VA2) cannot be derived from them.
- Whether it can be derived from the requirements inside 𝓘 is exactly criterion (A).

### 3.8 Criterion (A) is not achieved; calibration

**Prop K (PROVED).** Suppose there is a decomposable domain U with (LF) at D_K, and integrable f_1, f_2, f_3 on U with f_w < 0 a.e. on U ∩ pos_w and f_w > 0 a.e. on U ∩ neg_w, such that:
- (i) for every π ∈ Δ, every minimiser of Σ_w π_w ∫_X f_w over models X is coherent;
- (ii) D_K is the a.e.-unique minimiser for some π*.

Then the ranking X ⪯_w Y ⟺ ∫_X f_w ≤ ∫_Y f_w covers K under the binding framework.

*Proof.*
1. **Axioms.** (G) is strict by the sign conditions. (IB) holds because the relation is an integral of a record. The relation is complete and transitive, hence satisfies (TC).
2. **Score range.** By Lyapunov, the range Z of z(X) = (∫_X f_w)_w is compact and convex.
3. **Undominated models are coherent.** A Pareto-minimal z(X) is a boundary point of Z + ℝ³₊. A supporting π ≥ 0, normalised to π ∈ Δ, makes X a minimiser, so X is coherent by (i).
4. **Weak dominators.** For any X, minimise Σz over {z ∈ Z : z ≤ z(X)}. This gives an undominated weak dominator Y of X.
5. **Incoherent models are dominated.** If X is incoherent and Y does not dominate it, then z(X) = z(Y). So X is undominated, and hence coherent, a contradiction.
6. **Direct (C).** A model tied with a coherent undominated model has the same score, so it is undominated and coherent.
7. **Target.** A weak dominator of D_K is a π*-minimiser, so by (ii) it equals D_K a.e. ∎

**Consequence.**
- Criterion (A) for the reversed triangle implies that no strictly sign-correct measurable chart family has all Bayes acts coherent with D_K a unique Bayes act, on any (LF) domain.
- This is the tangency-relaxed CPM realisation problem. It is OPEN (E61 §5, §6; O61 §7; IN63 §9(i); DC63 §0 "open: non-PL fields").
- So (A) is at least as hard as that problem. Every negative result to date excludes only subclasses of such charts: concave, continuous PL, direction-continuous PL, regular, or finite-view concave.
- Conversely, a positive solution of the chart problem would refute (A) outright.

---

## 4. Architecture ledger for the existing exclusions

In the table, "framework" means the step is valid in the binding framework as stated or with OR64's repair; "architecture" means the step uses a structure the framework does not supply.

| Result | Steps that are framework-level | First step that is architecture | What that step uses |
|---|---|---|---|
| **E61 Cor 5.3** (view-unanimity; target-neutral vetoes; finitely additive levels; Brier) | (1) Leading vetoes give priority regions. Their regions are *strong* (Prop 2.6), so no (TP) is needed. (2) Lemma 3.4 holds for strong regions (Prop 2.5), and its relational core is Lemma OC. | (3) Lemma 3.6, and above all (4) "D_K ∪ P ties every veto and finitely additive level and is strictly better at Brier in every view". | The class itself (integral levels in views). The summed-payoff positivity ∫_P h ≫ 0 is turned into a preference at every world by an additive Brier level. In OR64 terms this is hypothesis (VA2). |
| **O61 Thm A** (𝒱_B: complete, transitive, lexicographic integral vetoes, then a common-weight Brier error) | Lemma 4 (collar forcing) is relational once Lemma 3 holds. The final ball contradiction is geometry. | Lemma 2 (the target pays no veto) and Thm A step 2: "D_K is not strictly dominated inside N, so some π ∈ Δ has D_K minimising −∫w π·h". | Lyapunov convexity of the score range and a supporting hyperplane, which scalarises the target's protection into one prior π. Lemmas 1 and 3 also use the numerical lexicographic levels (unique minimiser of b_j). |
| **IN63 Thm C** (finite unanimity; concave gains; convex vetoes, paid or not) | Step 1: R_v is a strong priority region (Prop 2.6(c)), and E61 Lemma 3.4 applies (Prop 2.5). | Step 2: Lyapunov plus separation, giving weights β, α with D_K maximising ∫g. | Scalarisation over views, then supporting-face analysis: concavity forces continuity and face-linearity (steps 3–5), and the circulant (step 6). |
| **DC63 Thm DC** (direction-continuous PL charts) | none | From the start: a single additive chart c meeting the four-condition certificate, with (C2) at u. | A common numerical representation, regular local charts (finite fan, direction continuity), and supporting-face and kink analysis near u. |
| **C62 Thm 4.1** (continuous PL charts) | none | From the start: as DC63, with value continuity. | As above, plus the corner-seam linear system. |
| **W62 Lemma `lem:dominance`** (W64's concern) | (W) and 𝒰 = 𝒞* | "If Y did not dominate X then by completeness X ⪯_i Y" | Completeness. In the binding framework this lemma is not needed, since incoherent-model dominance is a requirement. The W62 constructions are complete. |

**Summary.**
- The (TP) gap identified by the auditor is real at axiom level (M1), but harmless inside every published class.
- The decisive non-ordinal step is the same in every exclusion: some device (a Brier level, a scalarising prior, view weights, or a chart) converts the summed payoff of a collar trade into a preference. Ordinally that conversion has no basis (§3.5).

---

## 5. Success criteria, stated plainly

- **(A) Axiom-level impossibility: NOT achieved.** By Prop K it would settle an open chart problem. I do not conjecture either answer.
- **(B) Conditional impossibility: achieved (Theorem VA).**
  - The extra hypothesis (VA) is named: a relational veto (VA1) plus acceptance of improving collar trades off the veto (VA2).
  - (VA2) is the argument's only acceptance, and §3.5 shows that the framework's requirements outside the one-world improvements do not supply it.
  - This is a scoped result.
- **(C) New necessary relational lemmas: achieved.**
  - Lemma OC and Corollary OC: no world can veto any non-null part of the collar in any relational form. This excludes incomplete, non-transitive and non-additive collar vetoes, which no scoring result covers.
  - Lemma T and corollaries T1–T3, for every target: no hull or kernel dominance near the target; a target-dominated collar addition is contained in no undominated model.
  - Prop 3.5 (𝒯): the precise reduction of any remaining axiom-level proof to the one-world improvements 𝓘.

---

## 6. Suggested next step (not done)
The remaining axiom-level question is now a finite-looking local problem.

Can the incoherent one-world improvements in 𝓘_w be dominated by coherent undominated models, as Lemma OC requires for dented boxes, without either:
- producing a pair of non-guided accepted records at one world whose composite is anti-guided (V3), or
- making D_K or one of these dominators dominated (V1/V2)?

The natural test case is the three dented boxes B_i∖R with R a small ball in C_i ∩ neg_j at a crossing point of F_i, together with their required dominators (credal sets omitting v_i). ES64's record constructions are the right language for the positive side of the same question.

---

## 7. Files
| File | Content |
|---|---|
| `or64py/geom.py` / `geom.out` | rays, faces, crossings, face midpoints, collar centres (Σc_k = (2−δ)𝟙), exact hull witness for the collar step; ALL PASS |
| `or64py/records.py` / `records.out` | record composition; M1 (exhaustive (TC), strict (G), (IB) random, priority, domination); M1b ((TC) needed); 468 random non-transitive strict-priority systems; 𝒯 (exhaustive (TC); undominated set = {D_K} ∪ 𝓘; collar trades refused; Lemma T instance); ALL PASS |

---

## 8. Status table

| Item | Status |
|---|---|
| Prop 1.1 record form of (IB); Prop 1.2 composition formula, commutativity, (TC) in record form | PROVED; CHECKED |
| Prop 1.3 (TC) + completeness ⇔ transitivity | PROVED |
| Prop 1.4 (TC) propagates strict comparisons only; one guided step never gives a contradiction | PROVED |
| **Prop 2.1 M1: E61 priority region at j, yet the box model is dominated; (TC) ⇏ (TP)** | **PROVED; CHECKED (atoms)** |
| Lemma 2.2 box lemma for strong priority (strict (G) at i only) | PROVED |
| Lemma 2.3 box lemma for strict priority (needs (TC); M1b shows it is needed) | PROVED; CHECKED |
| Prop 2.4 E61 Cor 3.3 (inclusion vetoes) holds under the binding framework | PROVED |
| Prop 2.5 E61 Lemma 3.4 for strong or strict priority | PROVED; exact hull witness CHECKED |
| Prop 2.6 regions used in E61, O61, IN63 are strong, so their theorems are unaffected | PROVED (depth-leximax and Pareto vetoes not re-checked) |
| Prop 2.7 strictly sign-correct additive rankings have no priority regions; boxes covered without them | PROVED (coverage: FD62 Prop FD-B, refereed) |
| Facts (a), (b), (c) of the brief | PROVED; (b) non-trivial only when P meets every pos_w |
| Prop 3.1 record applicability; **Lemma T** target transfer; T1–T3 | PROVED |
| **Lemma OC / Cor OC: no relational veto of any non-null part of the collar; forced dominators of dented boxes (omit v_i, ≠ D_K, B_i)** | **PROVED** |
| **Prop 3.5 diagnostic 𝒯: all axioms; D_K undominated; undominated set = {D_K} ∪ 𝓘; every collar trade refused at every world** | **PROVED; CHECKED (atoms)** |
| Final-violation shapes V1–V5; none produced by the forced data | PROVED (classification); the "none" claim is relative to the forced data listed |
| **Theorem VA: no cover under the binding framework + (VA1) + (VA2)** (contains E61 Cor 5.3) | **PROVED (scoped, conditional)** |
| Prop K: (A) implies the negative answer to the open measurable-chart problem | PROVED |
| Architecture ledger (E61, O61, IN63, DC63, C62, W62 Lemma dominance) | PROVED (by inspection of the cited proofs) |
| Axiom-level impossibility for the reversed triangle (criterion (A)) | OPEN (not achieved) |
| Whether the requirements inside 𝓘 force an acceptance of a collar trade | OPEN |
