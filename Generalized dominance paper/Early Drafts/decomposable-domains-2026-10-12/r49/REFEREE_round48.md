# Referee report, round 48: PP33, PP34, PP36

22 October 2026. Independent referee. I read Brief 48, AUDIT_round48_instructions, AUDIT_round49_brief, AUDIT_completion, PP19 Lemma 5.0 and Theorem 5, PP21 Lemma 2.3, PP25 Theorem A as refereed in REFEREE_round46, PP32 Lemma 2.1, and the three notes in full. I checked each listed claim line by line and did not edit any note. My scripts are in `r9/PP39_py/`: `pp39_checks.py` → `pp39_checks.out`, plus copies of the authors' scripts re-run under `PP39_py/rerun/` (§5).

**Labels.** PROVED: complete argument, here or in the note, checked by me. CHECKED: exact finite computation. NUMERICS: sampling. CONJECTURE: unproved.

**Overall.** The axiom-level results hold: PP33 Thm 3.1, PP34 Lemma 2.1 and Cor 2.2, PP36 Prop K, Lemma E, Lemma P1 and Prop SD. Under its stated scope, PP33 Theorem 5.1 is also correct. I found two substantive errors:
- **PP36's claim** that "one precise answerer at one defence world per dominator" is safe from Prop K is false. Counterexample: CHECKED, §3.4.
- **PP34 Prop 4.1(f)** is false as stated. Counterexample: CHECKED, §2.3.

Several further statements need repairs or narrower wording. I agree with all three of audit's corrections in AUDIT_round49_brief. I add one point to them: in PP33's relation, the registered defenders are not competitive even against each other (§1.3).

---

## 0. Verdicts at a glance

| Note | Claim | Verdict |
|---|---|---|
| PP33 | Thm 3.1 (ordinal refusal) | correct |
| PP33 | Cor 3.2 (budget) | correct **under its optional hypothesis**. The §0 and §9 tables should mark it as conditional. |
| PP33 | Cor 3.3 | **correct with repair**: it needs C coherent (Q not essentially bounded) as well as Cor 3.2's hypothesis |
| PP33 | Lemma 1.2(a) (not listed; used in §§4–6) | **correct with repair**: the Sil(T) witness fails for small ε (CHECKED); a replacement witness works |
| PP33 | Rule §4, Lemma 4.1, admissible interval, Prop 4.2 | correct |
| PP33 | Invariant (i)–(iv), Lemma 5.0 | correct |
| PP33 | Thm 5.1 (1) strict (G), (IB) | correct |
| PP33 | Thm 5.1 (2) (TC), incl. non-shadowing, mixed triangles across (G, E, j) | correct. It inherits PP25 Thm A's π-system repair (rational boxes suffice). |
| PP33 | Thm 5.1 (3) no ties; (4) members undominated, strict everywhere | correct |
| PP33 | Thm 5.1 (5) closure forces nothing | correct, with P = the member set |
| PP33 | Thm 5.1 (6) competitiveness | correct as stated (bounded rivals only). The relation fails (S) badly; see §1.3. |
| PP33 | Prop 6.1 | correct, and **relative to I only** (u ∉ I) |
| PP33 | Prop 8.2 | correct as stated. The gloss "the unbounded layer must be non-additive" is **not proved**. |
| PP33 | Backward rivals (Prop 8.1, shadows, Conj 8.3) | Prop 8.1 correct (uses L at j); shadow counts reproduced; "backward ray dominators exist" is **unclear** (only the budget is shown) |
| PP34 | Lemma 2.1, Cor 2.2 | correct (re-run: 2,214,657 configurations) |
| PP34 | Prop 2.3 | **correct with repair**: rivals with contradictory advice inside Sil(T) are not covered |
| PP34 | Props 3.1, 3.2 | correct |
| PP34 | Prop 3.3 | correct, with implicit hypotheses H, H′ ⊆ Q, and room in Q_i for (b′) |
| PP34 | (CC) | correct as a **necessary** condition. "The family reduces to (CC)" (§0) is overstated. |
| PP34 | Prop 4.1 (a)–(d) | correct |
| PP34 | Prop 4.1 (e) | **correct with repair** (the hypothesis must be on G, not G″). The "ends under any additive valuation" clause is unproved. |
| PP34 | Prop 4.1 (f) | **wrong** (CHECKED counterexample). Correct for single-answer pieces. |
| PP34 | Props 4.2, 4.3, 4.4 | correct. 4.2 needs a one-line clarification; 4.3's guidance step needs E ∩ W_jw null. |
| PP34 | Prop 5.2 | **correct with repair**: the literal hypothesis allows guidance acceptances, and then a record can be blocked at two worlds (CHECKED). Repaired form proved. Audit's caveat about completion acceptances stands. |
| PP34 | Prop 5.4 | correct; the ρ·r half of the proof needs repair |
| PP34 | Classification of failures | **partly overclaimed**: the two "cell artefact" rows are uninformative, not shown to be artefacts. The "exact" largest-loss UNSAT is a continuum-valid obstruction where the pieces are realisable. |
| PP36 | Lemma 1 | correct ("it never helps" is an unproved remark) |
| PP36 | Prop SD | correct ((a)–(c) checked by hand) |
| PP36 | Lemma E | correct |
| PP36 | Prop K, Cor K1 | correct (K1 needs D coherent, or D ≠ Z off G) |
| PP36 | Cor K2 | correct (uses (S) through KKM) |
| PP36 | Cor K3 | correct. The sentence extending it to "an edge model on [e_j, e_k]" needs "precise". |
| PP36 | Lemma P1 | correct |
| PP36 | Inference from P1: "one answerer at one defence world is Prop K-safe" (§0 item 4, (A) "PROVED", P4) | **wrong** (CHECKED counterexample, §3.4) |

---

## 1. PP33 (joint rule)

### 1.1 Theorem 3.1 and its corollaries

**Theorem 3.1: correct.**
- On Q ∖ H, B_H = N <_v C, because ranks at one world are injective.
- Q ∖ H is non-null because Q is not essentially bounded and H is bounded.
- So B_H ≺_v C by strict (G), and C ⪯_v Y ⪯_v B_H would break (TC).
- The theorem uses strict (G) and (TC) only. Reflexivity is not used.

**Applicability to vertex rivals: correct.** V_j is j-perfect, and a coherent C ≠ V_j disagrees with it on a non-null cone (Lemma H).

**Cor 3.2: correct under its hypothesis.**
- The hypothesis is needed only for the records rec(Y, B_H).
- Dominated convergence applies because ρ_v and the ranks are bounded and μ is finite.
- I re-derived the budget formula. Since w ∉ {j}, only E ∩ G_j and E ∩ G_w carry j-wrong w-correct answers.
- Audit is right that the hypothesis is optional, so neither the budget nor Cor 3.3 constrains a construction that does not adopt it. The §0 table states this; the §9 status table does not. It should.

**Cor 3.3: correct with repair.**
- The step μ{C ≠ V_j} ≤ L_j(C) ≤ L_j(Z) uses Theorem 3.1, which needs Q unbounded.
- For an incoherent C with bounded Q, Cor 3.2's hypothesis allows C ⪯_j Z together with L_j(C) > L_j(Z) (a tie, not a contradiction).
- Add "coherent", which is the case of interest.

**§2's "direction is forced": overclaimed.** (IB) makes the *set* of accepting worlds a function of the record. It does not stop a designer from choosing the rule on such records with the available dominators in view. Theorem 3.1 links w and K. It does not order them.

**Lemma 1.2(a): correct with repair.**
- The Sil(T) witness (−α, −2, 3) needs c(1 − α) < 2ε. With ε = 3/10, as in the scripts, it always holds. With ε = 1/10 it fails for 60 of 99 values of t, and with ε = 1/20 for 86 of 99 (CHECKED (1)).
- Replacement: g = (−α, −K, K + 1 + α) with α = t/(3(1 − t)) and K > c/ε. Then Σg = 1, s0_1(g) = t and g ∈ Sil(T) for every ε. This is the template already used for (c).

### 1.2 The rule and the invariant (§§4–5)

- **Lemma 4.1: correct.** Off {s0_j > m}, N is j-wrong and Z's differing advice is S or the j-answer.
- **Admissible set: correct.**
  - (E) is open, because the cost 2∫_{W_j(m,d)} ρ_j is continuous and increasing in d.
  - d ↦ μ({Z ≠ N} ∩ {s0_j > d}) is right-continuous and non-increasing, so (X) also holds on an interval (m, d_X).
  - δ* > 0 follows by continuity of measure and Lemma 4.1.
- **Well-definedness.** Z does not determine (G, E, w): points of E where N is already w-correct are invisible. But (E) and (X) depend only on (Z, N), and N is the unique coherent model equal to Z off a bounded set. So K(Z) is a function of Z. Prop 6.1 uses this; it should be stated.
- **Invariant and Lemma 5.0: correct.**
  - (ii) holds on W ∩ M_j, where C says A and N says B. This set is a non-null cone, so (ii) survives removal of every bounded set: the "B1 reading" required in REFEREE_round46 §3.
  - (iii) is Lemma 1.1.

### 1.3 Theorem 5.1

**(1) Strict (G) and (IB): correct.**
- Unbounded weak worsenings are accepted by guidance, bounded ones by L.
- A 𝒢-record is not a pure j-improvement by (i), and not a pure a- or b-improvement by (ii).

**(2) (TC): correct.** I checked every case.
- **One bounded edge.** (Guid, Guid) is trivial. (Guid, 𝒢) contradicts (ii) at the non-vertex worlds and the first-level sum at j. (𝒢, 𝒢) contradicts (B2): same family, far parts all run non-j → j; across families, W_j ∩ M_j ∩ W_k = ∅ by Lemma 1.2(b).
- **Three unbounded edges with at most one 𝒢 link:** pointwise cancellation.
- **Two or three 𝒢 links.**
  - Consecutive links meet on far supports only where N_1 = C_2.
  - **Shadow-freeness is correct.** Within a family, N_1 gives the j-answer (s0_j > m_1) while C_2 gives the non-j answer (s0_j < d_2). Across families the overlap lies in M_l, where N_1 says A and C_2 says B.
  - With three 𝒢 links, ℓ_1 cannot cancel on its far support. With two 𝒢 links and one guidance link, both 𝒢 links are forced to world j of one family, and then the first levels sum to > 0.
- **Mixed triangles across (G, E, j) and shared records** are covered, because the relation is record-based and the argument runs over arbitrary copies.
- The 0-unbounded case is L's (TC). It inherits PP25 Thm A's repair: the countable family of boxes must be a π-system. Rational boxes are one.

**(3) No ties: correct.** L has none, by the π-system repair. Guidance with 𝒢 is excluded by (i)/(ii), and 𝒢 with 𝒢 by (B2). Direct (C) is then vacuous.

**(4) Undominatedness: correct.** The landing argument is complete.
- Conic disagreement gives M = N on all of W.
- Only R_j(x) with x ≤ m agree with N on W. T is silent on W ∩ Sil(T); other families say A on W ∩ M_j.
- The two cases G ∖ E non-null and E = G (which uses (X)) exclude the remaining candidates.
- Strictness at every world then follows from (3).

**(5) Closure: correct**, with P = 𝓜. Rule III has no premise by (4), rule IV none by (3), F1 is excluded by (1), and F2 cannot occur.

**(6) Competitiveness: correct as stated**, but the stated scope is narrow. Brief 48 item 3 asks that each new defender's comparisons with T and with the other defenders be handled. Theorem 5.1 handles them only for consistency, not for (S):
- T ⪯_w R_j(s) holds at no world (audit).
- **R_1(m) ⋠_w V_1 at every world**, and likewise for any two members of a ray.
  - rec(R_1(m), V_1) is supported on the wedge W_1(0, m), so it is unbounded.
  - It is a pure 1-improvement, and it is mixed at worlds 2 and 3 (CHECKED (5)).
  - It is not a 𝒢-record. Its support is exactly the wedge W_1(0, m), and its new side V_1 is never silent. Every installed record's support has a non-null part off its wedge: where Z is silent, or, if E = G, the set guaranteed by (X).
  - So a selected ray model is not competitive against the vertex model on its own ray.

None of this contradicts the note, which lists unbounded competitiveness as missing (§8.2). But it shows how far the relation is from an (S)-system: **a family closed under the repair rule, whose members do not defend against each other.** Audit's sentence ("closed under the proposed repair operation is not yet a family whose members can all satisfy (S)") applies already to pairs of members, before any rival is considered.

**Hidden assumptions.**
- Transitivity: not used.
- "No ties" and "strict at every world" are *outputs* of this relation, not assumptions. But the proofs of (4) and (5) depend on them, so a redesign that admits ties (as audit's round-49 item 5 permits) must re-prove (4) and (5).
- Continuity of the selection: not used.
- Universal coverage: not claimed. Only the forward class is covered.

### 1.4 Prop 6.1: correct, relative only

Each piece checks out:
- bounded acceptances occur at at most one s, because two distinct ray models disagree on a cone;
- the guidance part, together with the bounded weak worsenings, is the closed set {s : R_j(s) ≤_w X a.e.};
- 𝒢-copies occur at at most two s: the index of K(X), and the supremum of X's far non-j set;
- other families cannot supply the old model (Lemma 1.2(c)).

The rays are clopen in I and p_T is isolated. As audit notes, u (the common limit of the rays) and the edges are omitted, so the proposition does not test the junctions where closedness is hardest.

### 1.5 Prop 8.2: correct as stated; the gloss is not proved

**The proof is right.**
- Q = Z[F ↦ contradiction] gives Z ⪯_v Q by guidance.
- Q ⪯_v C holds by the extended potential.
- C ⪯_v Z holds in 𝒢.
- The reverse C ⪯_v Q has Φ_v^{(1)} < 0 and contradictory new-side points, so nothing accepts it.
- Balance gives every installed record a world with Φ_v^{(1)} < 0. Balance applies because G ⊆ Sil(T) contains no U-points, so C and Z are regular and agree on U.

**What it shows.** The proof uses only that every unbounded record with Φ_v^{(1)} > 0 is accepted at v. So it excludes exactly the ρ-potential extension. It does not show that "the unbounded layer must be non-additive":
- An unbounded layer with a different positive density Ψ_v escapes this triangle whenever Ψ_v(r) ≥ 0 for every installed r.
- Balance is a property of ρ, not of Ψ.
- Whether such a Ψ can coexist with L's bounded verdicts in mixed triangles is untested.

**Nearby correct statement:** "at each world v, any unbounded layer that accepts every record positive for some additive potential Ψ_v must have Ψ_v ≥ 0 on every installed record."

### 1.6 Backward rivals

- **Prop 8.1: correct.** It uses Cor 3.2's hypothesis at j, which L satisfies.
  - The general form also holds: under L, any dominator with unbounded Q and no j-compensation relative to N satisfies L_j(C) ≤ L_j(Z) ≤ L_j(N) ≤ L_j(C). Hence C = N, which refuses Z.
- **The backward class is non-empty for every member R_j(m) with m > 0.**
  - Take G ⊆ W_j(0, m) ∩ Sil(T), which is non-null by Lemma 1.2(a). The record is accepted at j by guidance.
  - Z = N[G ↦ j-correct] is then a pure j-improvement of N.
  - So every registered non-vertex member has forced rivals without a dominator. PP33 says this; the §0 phrase "survives its own defenders" should carry "forward class" every time it is used.
- **Shadow counts: reproduced exactly** (816 and 261).
- **"Backward ray dominators exist" (§0): unclear.** The note shows only that some R_j(x) meets the j-budget and is compensated. That it can be installed without breaking (TC) is exactly what is open. Conj 8.3 is fairly labelled.

---

## 2. PP34 (adversary)

### 2.1 §2

- **Lemma 2.1: correct.** O ⊇ Wr_i(a) makes W i-correct wherever it differs from X. Re-run: 2,214,657 configurations, all PASS.
- **Cor 2.2: correct**, including the criterion for when the refusal is genuine: b = S on a non-null part of O ∖ W_jw. The record is never a weak w-worsening, because it changes on G ∩ W_jw.
- **Prop 2.3: correct with repair.**
  - "Departure" is defined with *regular* advice. A rival T[H₁ ↦ contradiction, H₂ ↦ A] with H₂ ⊆ M_1 ∪ M_2 is mixed at all three worlds and is not a departure. So in the relation of Prop 2.3, T does not defend against it. The claim "competitive against every rival that differs from T only inside Sil(T)" is therefore false as stated.
  - Repair: allow advice in {A, B, contradiction} and let L(d) be the worlds at which some piece has rank > 1. The (P1) argument (disjoint union keeps a loss) and the (P2) argument (no triangle of departures) go through unchanged. I checked that three departures cannot close a triangle: on supp d₁ the middle model is non-S, which forces the third to be both S and non-S.

### 2.2 §3

- **Prop 3.1: correct.** "F is empty" should read "F is null". (CC) is necessary.
- **§0's claim** that the family "reduces to one first-order condition (CC)" is overstated. Lemma 2.1 also refuses records that are domination records at world j: Prop 4.3 is an instance. §5.1 states this correctly ("(CC), together with the dominations").
- **Prop 3.2: correct.** The edge model equals V_j on G. It refuses at w by (IB), so it must accept at w′, and the copy goes to V_j.
- **Prop 3.3: correct.**
  - (a) is strict (G).
  - (b) needs H, H′ ⊆ Q, implicitly; the condition H′ ∖ O ⊆ Q_i ∪ Q_k is then equivalent to H′_l ⊆ O.
  - (b′) needs Q_i ∖ H_i to have mass at least h′_i − h_i, and Q_k enough room as well.
  - The largest-loss rule satisfies (b′): h′_l < h_l ≤ h_i < h′_i ≤ h′_l is impossible. Ω does not, e.g. h = (0, 1, 1) and h′ = (0, 1 + δ, 1 − δ) with δ ≤ 1/3.

### 2.3 §4: the dominators

**(a)–(d): correct.**
- (d) uses closed sections and competitiveness on the whole edge, and PP32 Lemma 2.1(ii) for K ⊆ edge.
- q* may be e_w. That is consistent with the statement.

**(e): correct with repair.**
- rec(D, D′) = rec(V_j, Z) needs D = V_j a.e. on **G**, not only on G″. On G ∖ G″ = E ∖ W_jw, Z = V_j, so any point where D ≠ V_j enters rec(D, D′).
- For edge models on [e_j, e_w] the two hypotheses coincide, because {D ≠ V_j} ⊆ W_jw. For interior D they do not.
- "Under any additive valuation it must end" has no proof: unclear.

**(f): wrong as stated.**
- An edge model on [e_j, e_w] can give both answers on a one-class piece of Sil(T). Its retreat is then mixed at both of its worlds, so it is not guidance at either.
- CHECKED (4): D = D_{(1/2, 1/2, 0)}, both points in M_1 ∩ Sil(T). D says B at (−1, 1/2, 1/2) and A at (−3/2, 2, 1/2). The rank changes of D → S are (+1, −1) at world 1 and (−1, +1) at world 2.
- **Repair:** "on a one-class piece on which D gives a single answer". Mixed-answer pieces are genuine trades and fall under (CC). The §5 conclusion that edge dominators' own forced defences bite only on two-class pieces must widen to "two-class or mixed-answer pieces".

**Prop 4.2: correct, with a clarification.**
- Lemma 5.0's hypothesis compares X = Q with C = P on E ⊇ {Q ≠ T}, not Q with T.
- At w, on the first set, Q = A while P = D ∈ {S, B}. At w′, on the second set, Q = B while P = D ∈ {S, A}. So Q is not ≤ P there, and Lemma 5.0 fails at w and w′ for this copy.
- The note compares Q with T instead. The conclusion survives because D ≠ V_j at those points.
- Scope: only the copy into T's context is shown to be inert.

**Prop 4.3: correct.**
- R^j_{G‴} ≺_j D by strict (G).
- But guidance accepts Z ⪯_j R^j_{G‴} only when, in addition, E ∩ W_jw is null. The concluding disjunction is right once the step is written in that order.

**Prop 4.4: correct.**

### 2.4 §5: the joint rule

**Prop 5.2: correct with repair.**
- The hypothesis "accepted at α(d) and at no other *mixed* world" lets guidance accept d at other worlds. A record can then be blocked at two worlds.
- Example (CHECKED (3)): one piece of M_1 with a = B and b = A. The departure (O, S → B) is a weak worsening at worlds 2 and 3, so it is accepted at both by guidance, and q is blocked at both.
- The proof only treats blocks of the form α(d_i) = i.
- **Repaired statement (PROVED; CHECKED exhaustively on 1,176 configurations):** a record is blocked at most at one world at which q is not a pure improvement. If d_i is accepted at i by guidance, then F is null and a is i-wrong on O. Any second block then forces a to be wrong at two worlds a.e. on O, so a = B on O ⊆ M_k, and q is a pure improvement at both blocked worlds.
- **(CC) still follows for supports of size ≥ 2:** a model giving B on M_k has k in its support (PP32 Lemma 2.1(i)), and q is a weak k-worsening.

**Audit's caveat stands, and I sharpen it.**
- Prop 5.2 bounds blocking only for the exact rule.
- The exact rule is UNSAT in two of six cell configurations. I re-ran `argmax_core`: the minimal core is identical.
- The core is not a cell artefact. Its six items are continuum constraints on genuine measurable records: competitiveness of an all-A model on edges 12 and 23, plus four verdicts. A cell refutation is therefore a continuum refutation wherever the five pieces can be realised with such edge models (PP32 Lemma 1.1 bands; plausible for these masses, not checked by me).
- So Prop 5.2 is a statement about a relation that cannot be completed in those configurations. The bound for the "at least α(d)" form, after completion acceptances, is open, as audit says.

**Prop 5.4: correct; the proof of the ρ·r half needs repair.**
- The proof says the composition requires supp r ⊆ G ∖ E. That is false: r may also act off Σ, where the context is free.
- The conclusion survives. The composite contains S → V_j on Wd, which is a w-worsening and a w′-worsening on Wd ∩ M_j. At j it is a pure improvement only if E ∩ W_jw is null, r covers G ∖ E with new side V_j, and r's other parts go S → j-correct. Then r is a pure j-improvement, and strict (G) refuses it at j.
- Scope:
  - it covers (P1) only;
  - it needs ess sup_G θ_jw < ∞, so arbitrary admissible G is not covered (the note says so);
  - it does not show that the dominations rec(D, Z) themselves can be accepted at all three worlds.

### 2.5 Classification of failures

- **Ω, and shared ties (double blocking) — optional comparisons:** correct.
- **Exact largest-loss — optional comparison:** correct, with the sharpening in §2.4.
- **"All three vertex families on 5 cells — chosen geometry (cell artefact, PROVED)": overclaimed.**
  - What is proved is that no cell-coherent pattern can dominate R_2.
  - That a continuum dominator of R_2 exists and meets the remaining obligations is asserted, not shown.
  - Label: *uninformative*, not "artefact". The same applies to `ff_ab_all` ("a continuum dominator need not be cell-measurable").
- **Re-runs:** `ff_ab_v1_edgeKKM` (SAT) and `ff_ab_family_edgeKKM` (UNSAT, minimal core R_2) reproduced exactly.

---

## 3. PP36 (joint search)

### 3.1 Lemma 1: correct

V_j's answers per class are as stated, so guidance at k holds iff G ∩ M_l is null. "A mixed world on top of a guidance world never helps" is an unproved remark. It is plausible for V_j's records: any model silent on G whose competitiveness would need the extra world already contains a guidance world in its support. Label it as a remark.

### 3.2 Prop SD: correct

I checked (a)–(c) of PP21 Lemma 2.3 by hand.
- **(a) No requested record is a weak improvement.**
  - rec(T, Z) worsens at i ≠ j on Sil(T) ∩ M_i ∖ G, a non-null cone minus a bounded set.
  - It worsens at j on E′.
- **(b) Compositions.**
  - Two fills compose only on disjoint supports. Their inverse composite is guidance only if both fills are pure improvements, which (a) excludes.
  - A fill composes with rec(T, Z₂) only if G₁ ⊆ G₂ ∖ E₂. The inverse composite is then guidance at no world: at w′ ≠ j₂ it improves on V_{j₂}'s w′-errors in Sil(T) ∖ G₂, and at j₂ it improves on E₂′.
  - Two rec(T, Z) never compose, because Sil(T) ∖ (G₁ ∪ G₂) is non-null.
  - rec(T, V_j) composes with nothing.
- **(c) Rule III.** Only the rec(T, Z) are accepted at all worlds. They cannot end at T, V_j (excluded on E′) or V_i (excluded on Sil(T) ∖ G).
- **Strictness:** rec(Z, T) is mixed at w.

### 3.3 Lemma E, Prop K, Cors K1–K3, Lemma P1

**Lemma E: correct.**
- (i) The splice D[G′ ↦ C] ties C at all worlds, so it would be registered (F2). For C = V_j, R is j-perfect off G′, which gives F1.
- (ii) is the same argument with T in place of C.

**Prop K: correct.**
- Z ≤_i D holds off G, on G ∖ E and on E.
- Strictness comes from D ≠ Z and injective ranks. Then (TC) applies.

**Cor K1: correct.** It needs D coherent, or D ≠ Z off G. For D = Z, Prop K does not apply and the argument gives nothing.

**Cor K2: correct.** N_i comes from KKM under (S). Prop K at i ∈ s shows that the N_i are not all equal.

**Cor K3: correct.** Both cases check out:
- off the median, the disagreement wedge meets u^⊥ ∖ {0} ⊆ Sil(T) in a sector;
- on the median, the planes meet in a line of u^⊥, and every neighbourhood of that line meets the wedge.

The §5 sentence "the same holds for any dominator serving two vertex families against an edge model on [e_j, e_k]" needs "precise" (or "erring inside Sil(T) at j and at k"). A vertex-anchored edge set [e_j, μ] is never j-wrong.

**Lemma P1: correct.**
- The lune argument places ±g* in one closed quadrant pair, so g* ∥ e_{i″}.
- Then both functionals depend only on (g_i, g_{i′}) and agree where g_i g_{i′} > 0.

### 3.4 The inference after Lemma P1: wrong

**The claim.** §0 item 4, (A) ("PROVED Prop K-safe for precise selections") and P4 ("for precise answerers and precise D, |κ| ≤ 1") assert that a dominator serving the rivals of one precise answerer C at one defence world kills at most one world of every precise D. For D = C this rests on the remark that "one model must not dominate C's own Z's at every world of C's support".

**Why it fails.** A Z built at a guidance world of C's record is pointwise better than C at *every* guidance world of that record, not only at the defence world. Different Z's served by the same N can therefore kill different worlds of C.

**Counterexample (CHECKED (2), exact; on balls of radius 1/20, at 802 sampled points, for ε = 3/10 and ε = 1/20).**
- C = D_λ with λ = (1/2, 1/2, 0). It is selected on the open edge [e_1, e_2], so its support is {1, 2}.
- G₁ is a ball around (−1, 2, −1.1) ⊆ Sil(T) ∩ M_2. G₂ is a ball around (2, −1, −1.1) ⊆ Sil(T) ∩ M_1. C says the minority answer B on both.
- Both records (G_k, S → B) are weak 3-worsenings, so T defends at w = 3 by guidance.
- Let Z_k = C[G_k ↦ A], the 3-correct answer. Then:
  - Z₁ ≺_1 C pointwise (on M_2, A is 1-correct and B is 1-wrong);
  - Z₂ ≺_2 C pointwise.
- A single dominator N(C, 3) of both gives C ⋠_1 N and C ⋠_2 N, by Prop K with D = C.
- So C is not competitive against N on its support.

**Repair.** Index each dominator by the answerer and by a world i₀ ∈ supp C at which none of its Z's is pointwise better than C. Equivalently, split C's own Z's by the set {i : Z ≺_i C}. For D ≠ C, Lemma P1 still gives |κ(N, D)| ≤ 1. The stage-0 runs are unaffected, because their answerers were vertex models.

**Alternative (B), not on my list.** I checked that genuine Z's served by T cannot kill a vertex-containing D at its vertex world. On E′, D would have to be j-wrong. Retreats can kill such D where D is silent, but under (B) T does not serve retreats.

---

## 4. Hidden assumptions

| Assumption | PP33 | PP34 | PP36 |
|---|---|---|---|
| Transitivity | not used | not used | not used |
| No single-world ties | holds in its relation as a *result*; (4)–(5) depend on it | not assumed | not assumed (the engine completes triangles) |
| Continuity of the selection | not used; sections only relative to I | not used; Prop 5.5 assumes a monotone threshold form (stated) | not modelled |
| Strict repairs at every world | a result of (3)+(4), not an assumption | not assumed (4.1 uses strictness at one world) | not assumed |
| Universal coverage | forward class only; the backward class is non-empty and uncovered | Prop 2.3 only for regular advice; 5.4 only for G of bounded θ-range; 4.1(f) only for single-answer pieces | "T dominates all genuine Z" is refuted by Cor K2/K3; "one answerer, one world" fails (§3.4) |
| Optional additive comparisons | L on bounded records (PP32: cannot survive edge selections); Cor 3.2's budget | none required; Ω used only as a foil | none |

---

## 5. Scripts

**Mine:** `PP39_py/pp39_checks.py` → `pp39_checks.out`, ALL PASS, under 1 s.
- (1) Lemma 1.2(a) witness failure and repair. CHECKED.
- (2) The §3.4 counterexample. CHECKED.
- (3) Prop 5.2 with guidance blocks: max 2 blocked worlds, max 1 at non-pure-improvement worlds. CHECKED.
- (4) Prop 4.1(f) counterexample. CHECKED.
- (5) rec(R_1(m), V_1) is a pure 1-improvement and mixed at worlds 2 and 3, on 831 wedge points. CHECKED (a sampled sign census).

**Re-runs** (copies in `PP39_py/rerun/`; `PP39_py/PP21_py` is a link for PP36's imports):

| Script | Result |
|---|---|
| PP33 `geometry_exact.py` | ALL PASS; output identical |
| PP33 `budget_mc.py` | identical (fixed seed) |
| PP34 `coordination_check.py` | identical: Part A 2,214,657 configurations; Part B as reported |
| PP34 `argmax_core.py 00112 12122` | identical six-item core |
| PP34 `forced_family_sat.py family edgeKKM v1` | SAT; identical |
| PP34 `forced_family_sat.py family layout=ab edgeKKM` | UNSAT, core R_2; identical |
| PP36 `verify36.py 100` | engine agreement 100/100; 0 violations |
| PP36 `exp_kill.py ref single,samedir bits0` | identical base (126 defences, 336 self-dominations). My pool was larger (2,283 models; arguments for the original not recorded). Agreement 6,712/6,712; characterisation exact; precise non-vertex survivors 0/283, as reported. |

---

## 6. Assessment and nearby reachable results

1. **PP33.** The durable content is:
   - Theorem 3.1, an axiom-level refusal at uncompensated worlds;
   - the shadow-free (TC) template of Theorem 5.1, which is the right proof pattern for any family of nested-wedge dominations.

   The relation is not a base for (S). Its members fail competitiveness against each other (§1.3), and its bounded layer must change (PP32; AUDIT_round49 item 2). The nearby target is to keep the invariant (i)–(iv) and shadow-freeness as *conditions on installed records* and to drop L.
   - At j, Theorem 3.1 requires endorsement only of the specific bounded records rec(Y, B_H), not of a potential.
   - At a and b, Prop 8.2 in its corrected form says only that any additive acceptor used there must be ≥ 0 on installed records.
2. **PP34.** Lemma 2.1 and Prop 3.1 are the correct general form of the forced refusals. Prop 5.2 in its repaired form is a first-stage bound. The open question is the one audit names: whether completion-forced acceptances double-block. My sharpening makes this urgent, because the exact rule is refuted in the continuum on realisable configurations.
3. **PP36.** Prop K, Lemma P1 and Lemma E are solid tools. The proposed invariant (P4) is the right *shape*, matching audit's pair-dependent defence worlds. But its claimed proof for precise answerers fails at D = C. With the repair in §3.4, the invariant becomes: for each pair (D, N), the worlds killed by N's served rivals miss a world of supp D, with the answerer's own Z's partitioned by their improvement sets. This is a sound, checkable target, and it is exactly the bookkeeping audit asks round 49 to carry through closure.
