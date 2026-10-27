# PP42. Removing the frozen kernel: per-model fields, triangle-local (TC), and the first repair that needs an excluded defender

23 October 2026. Task PP42 of Brief 50. One reader (me); not refereed.

**Labels.** PROVED: complete argument here (or a cited refereed or re-derived result, named). CHECKED: exact rational computation in `PP42_py/tc_local_witness.py` and `PP42_py/caps_exact.py` (both ALL PASS). NUMERICS: Gaussian Monte Carlo in `PP42_py/caps_mc.py`; no proof depends on it. CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF50, AUDIT_round50 and the milestone BRIEF49 (binding); AUDIT_round49_brief/answers; PP38 (kernel, Thm 3.1, Lemma 4.2, Cor 4.3, Thm 6.5); PP40 (shadow lemma, Lemma 2.1, Prop 2.3, K^S, Thm 3.3, Prop 3.4); PP41 (Thm 2.4 with its hypotheses, Γ_K, Prop 3.1); PP37 (gates, Lemma 3.3, Thms 5.1–5.6); PP33 Thm 3.1 (ordinal refusal); PP36 (Prop K, Lemma E); PP30 Thm 3.1; REFEREE_PP32_penalties (ℓ^T); REFEREE_round48; AUDIT_completion (rules I–IV, F1/F2); LEAD_selection_count (Lemmas A, B, E); and the coordinator's two relays (REFEREE_round49: F2 counterexamples in Γ and Γ_K; PP43: gate dominance Thm 2.1 and the no-additive-gate-jump Thm 3.4). Only Brief 50's axioms are used. Extra hypotheses are named where they enter.

---

## 0. Verdict

**The frozen kernel can be removed, and the first repair that PP38's kernel cannot make becomes possible.** But the milestone is not reached. Closed sections along the new path, cross-family compatibility and later generations remain open, and are stated exactly.

1. **What a kernel revision can and cannot be (Thm 2.1, PROVED).** Call an additive integrable strictly guiding functional U_w a *witness* at world w if U_w ≥ 0 on every accepted bounded record. Under any aggregation with a witness at every world, the registrable models are exactly the coherent U-Bayes models. This covers PP38's kernel, every revised single field, and PP43's gate dominance. So *any* witnessed revision only swaps ℓ^T for another field U. The registered family is then a partial single-field realisation, which is the route the ground rules exclude. For the first recursive repair (T's fills) a witnessed design needs coherent U-Bayes models that converge to T in measure, at weights accumulating on T's Bayes weights (Prop 2.3, PROVED). ℓ^T has none (PP38 Lemma 4.2). That is exactly why T's fills failed in PP38.
2. **The replacement: one field per registered model, aggregated by union, with a pairwise and a triple compatibility condition (§3).** Each registered model N carries its own integrable strictly guiding field ℓ^N. A record is accepted at w iff it is guidance, or some registered model that realises its old side rates it positively. There is no common bounded kernel. T keeps ℓ^T, so all of T's own verdicts are unchanged.
   - **(TC) is triangle-local (Thm 3.1, PROVED; CHECKED).** (TC) holds if every pair of gates satisfies a ratio sandwich (CG2) and every triple admits common constants (CG3). CG2 is also necessary, and CG3 is necessary in a weak form. Every accepted triangle uses at most three gates, so a local witness built for those three suffices. **No global witness is needed** (Prop 3.5, PROVED): the cap path of §4 admits none, so Thm 2.1's Bayes restriction does not apply to it.
   - **Members (Thm 3.2, PROVED).** Under CG2 alone: universal competitiveness through the member's own gate, against every measurable rival; undominatedness; no all-world tie with any other model, so direct (C) holds for members; strictness of every gate-endorsed domination; closure rules II–IV inert, F1/F2 absent, all common-context copies included. Registering a new member never removes a defence.
   - **The referee's F2 counterexamples violate CG2 (Prop 3.4, PROVED; CHECKED).** So CG2 is exactly what the union needed (coordinator item 1). PP43's Thm 3.4 needs a uniform kernel Bayes margin over T. Here there is no common bounded part, and the margins vanish (§5).
3. **The first recursive repair that needs an excluded model: T's fills (§4).** The defenders are *vertex caps*: refinements C^v_s = D_K with K = M ∩ {m_v ≤ c + ε − s}. PP41 Prop 3.1 shows ℓ^T cannot register them.
   - **Cap lemma (Lemma 4.1, PROVED; CHECKED; NUMERICS).** ℓ^T rates a small cap worse than T at v and better than T at both other worlds. The cap's own v-errors are one-signed: at v it is pointwise worse than T.
   - **One fill, one excluded defender (Thm 4.2, PROVED).** Take any fill X = T[G ↦ N] with Φ^T_v(T → X) > 0 for some v, and G away from the m_v-boundary strip of Sil(T). A cap C with its own field (ℓ^T, with C's own v-errors discounted on its disagreement cone) dominates X. The module {T, V_1, V_2, V_3, C} satisfies everything in Thm 3.2, including closure and the shadow condition. The bounded verdicts that change are exactly C's ℓ^T-kill records, and they are named.
   - **A continuous path out of T's fibre (Thm 4.3, PROVED).** The whole one-parameter family s ↦ C^v_s, s ∈ (0, s_0], with humble fields, satisfies strict CG2 and CG3. It is continuous in measure and tends to T, so **no jump is forced**. It dominates every sufficiently small fill whose largest ℓ^T-loss is at world v, except fills hugging the m_v-strip at a scale finer than their size. It admits no global witness.
4. **Where it stops (§5).** Three results are PROVED:
   - (a) With every gate accepting zero-valued records (allowed by strict CG), fixed-rival sections are closed along the whole cap path, for every measurable rival and through every realiser's gate. This includes inheritance at T's index (Prop 5.2).
   - (b) Any family in which one member eventually dominates every fixed fill of a vanishing sequence cannot have closed sections.
   - (c) Within this implementation, caps cut at different vertices violate CG2.

   Open: extending the path to the edge, cross-family fields, generation 2 (fills by caps' own answers, caps' forced rivals) and the rest of the repair class.

| Item | Result | Label |
|---|---|---|
| Any witnessed revision = single-field realisation; T-fills need near-T U-Bayes models | Thm 2.1, Prop 2.3 | PROVED |
| Pointwise local witness exists iff no positive gate 2-/3-cycle | Lemma 3.0 | PROVED; CHECKED (a) |
| (TC) ⇔ CG2 for pairs + CG3 for triples; strict versions allow zero-acceptance | Thm 3.1 | PROVED; CHECKED (b) |
| Members: competitive, undominated, tie-free, strict dominations, closure inert, monotone registration | Thm 3.2 | PROVED |
| Endorsement lemma (generalised PP33 Thm 3.1); free at worlds off the support | Lemma 3.3, Prop 3.6 | PROVED |
| Referee/PP43 F2 pairs violate CG2 | Prop 3.4 | PROVED; CHECKED (d) |
| Triangle-consistent, globally inconsistent constants | Prop 3.5 | PROVED; CHECKED (c) |
| Cap geometry and ℓ^T signs | Lemma 4.1 | PROVED; CHECKED; NUMERICS |
| One excluded defender repairs one fill, with closure | Thm 4.2 | PROVED; NUMERICS illustration |
| Continuous cap path: (TC), members, coverage of small fills, no global witness | Thm 4.3 | PROVED |
| Amplification limited by CG3; cross-vertex caps incompatible in this implementation | Prop 4.4 | PROVED |
| Closed sections on the cap path (incl. inheritance at T); eventual-domination families fail sections | Props 5.2, 5.1 | PROVED (5.1 under (U)) |
| Reaching the edge; cross-family caps; generation 2; rest of the repair class | §5.3 | OPEN |

---

## 1. Setting and the aggregation rule

Brief 50's setting:
- three worlds; problems g ∈ R³ modulo sign; Gaussian μ; the full four-advice domain; models modulo null sets;
- ranks correct 0 < silent 1 < wrong 2 < contradictory 3; classes M_1, M_2, M_3 and U; on M_k, A is the majority answer and B the minority answer;
- T = D_M with M = c·1 + εΔ, whose vertices are m_i = c·1 + εe_i; Sil(T) is T's silent cone;
- ℓ^T is the field of REFEREE_PP32 §3.2. T is its a.e.-unique u-Bayes model. On ∂Sil(T), T's answer and silence tie at u (REFEREE_PP32 §3.2, Fact 3).

**Fields and values.** A *field* ℓ assigns to each problem, world and advice a penalty ℓ_w(g, a). It is strictly increasing in the w-rank and has an integrable envelope. For a record r = (D, a → b), put Φ^ℓ_w(r) := ∫_D [ℓ_w(g, b(g)) − ℓ_w(g, a(g))] dμ. A model N *realises* r if N = a a.e. on D.

**Design TWG (triangle-witnessed gates).** Each registered coherent model N, other than the vertex models, carries a field ℓ^N. The vertex models carry no field. At world w a record r is accepted iff:
- **(G)** r is a weak w-worsening (guidance); or
- **(R)** some registered N realises r and Φ^{ℓ^N}_w(r) > 0. Under the *zero variant* **(R0)**, ≥ 0 suffices.

Every other record is refused at w.

**Aggregation rule (audit item 6).** The verdict is the union over guidance and all realisers' gates. A refusal is therefore global: it means guidance and *every* realiser's gate refuse. Each clause depends only on the record and the registered family, so all common-context copies receive one verdict, and (IB) holds.

**Bounded records.** These have no separate kernel. A bounded record realised by no member is accepted only by guidance. No member's defence uses such records (Thm 3.2(a)), so dropping the old kernel's acceptances of them costs nothing.

**(BR) Bounded ratios.** For any two gated members, the ratios of their increments on their disagreement set are bounded above and below by positive constants. All fields constructed below satisfy (BR).

Write Φ^N := Φ^{ℓ^N}, D_{NM} := {N ≠ M}, and s(N) for the support of N's index.

---

## 2. Witnesses: what a kernel revision with one additive witness is

**Theorem 2.1 (witness theorem; PROVED).** Suppose that at each world w there is an additive integrable functional U_w, strictly guiding on bounded records, with U_w(r) ≥ 0 for every accepted bounded record r. Then:
- (a) a model N is competitive against every bounded rival on s iff N is pointwise λ-Bayes for U at some λ ∈ Δ_s;
- (b) in the maximal U-preorder (accept r at w iff U_w(r) ≥ 0, bounded or not), every a.e.-unique U-Bayes member is universally competitive, undominated and tie-free, and closure is inert;
- (c) sections in the maximal preorder are closed iff p ↦ U_w(C_p) is lower semicontinuous;
- (d) PP43's gate dominance is a witnessed design, with witness U.

*Proof.*
- (a) ⇐: λ·U(N → X) ≥ 0 gives a world of supp λ with U_w ≥ 0. ⇒: this is PP38 Thm 3.1(ii)'s Lyapunov–separation argument (PP32 Lemma 2.3 on balls). It uses only that every accepted record has U_w ≥ 0.
- (b), (c): PP40 Prop 1.1, with U in place of ℓ^T.
- (d): PP43 Thm 2.1, step 1. ∎

**Corollary 2.2 (classification; PROVED).** Under a witness, "making defender and bounded verdicts both variables" (audit item 1) means choosing U together with the family. The ℓ^T-bounded comparisons responsible for excluding a candidate C are exactly its *kill set*: the bounded records out of C with U_w < 0 at every w ∈ s(C). By (a), this set is empty iff C is U-Bayes. No reassignment of verdicts inside one witness can admit C; only a change of U can, and that changes the whole family. A witnessed design therefore *is* a single-field realisation of its registered family. Classification: an **optional commitment ("one witness")** whose completion is the CPM-type realisation route that the ground rules exclude.

**Proposition 2.3 (T's fills under a witness; PROVED).** Let T be the a.e.-unique λ_T-Bayes model of the witness U, and let Λ_T := {λ : T is λ-Bayes for U}. Let X_n = T[G_n ↦ N_n] be fills with μ(G_n) → 0, and let C_n be registered dominators. Then:
- C_n ≠ T and C_n → T in measure;
- every limit of C_n's Bayes weights λ_n lies in Λ_T;
- writing C_n = D_{K_n}, the credal sets satisfy K_n → M in the Hausdorff metric.

*Proof.*
1. **The excess.** U(C_n) ≤ U(X_n) componentwise, so λ_T·(U(C_n) − U(T)) ≤ λ_T·(U(X_n) − U(T)) → 0. Put e(g, a) := Σ_w λ_{T,w}(U_w(g, a) − U_w(g, T(g))). It is > 0 for a ≠ T(g), a.e., by uniqueness. With only four advice values, m(g) := min_{a ≠ T(g)} e(g, a) > 0 a.e. Then μ{C_n ≠ T, m > η} ≤ η⁻¹ ∫ e(g, C_n(g)) dμ → 0 for each η > 0, and μ{m ≤ η} → 0 as η → 0. So C_n → T in measure.
2. **The weights.** Pass to an a.e.-convergent subsequence. Pointwise optimality at λ_n passes to the limit weight, so T is λ-Bayes there.
3. **The credal sets.** Suppose some k ∈ K_n stays at distance ≥ r from M. Then D_{K_n} is silent on a fixed non-null cone of Ans(T): the problems whose planes separate k from M. Suppose instead that some point of M stays at distance ≥ r from K_n. Then D_{K_n} answers on a fixed non-null cone of Sil(T). By compactness, both contradict C_n → T. ∎

Under ℓ^T, no coherent Bayes model other than T exists near u (PP38 Lemma 4.2, CHECKED down to 1/300 of u). This is PP38 Thm 6.5's isolation in its general form. **So the T-fill is the first repair that needs an excluded model, namely refinements K_n → M**, and no witnessed design can supply such models without becoming a local realisation at T. §§3–4 therefore drop the single witness.

---

## 3. Gate unions: (TC), members, endorsement

### 3.1 Compatibility conditions

Fix gated members N ≠ M and a world w. On D_{NM} put
- f^N_w(g) := ℓ^N_w(g, M(g)) − ℓ^N_w(g, N(g));
- f^M_w(g) := ℓ^M_w(g, M(g)) − ℓ^M_w(g, N(g)).

These are the two fields' values of the move N → M. Both have the sign of r_w(M(g)) − r_w(N(g)).

- **(CG2)_w(N, M):** there are constants c_N, c_M > 0 with c_N f^N_w ≤ c_M f^M_w a.e. on D_{NM}.
  - Equivalently (the *sandwich*): ess sup of f^M/f^N over {f^N < 0} ≤ ess inf of f^M/f^N over {f^N > 0}.
  - The condition is symmetric in N and M. It is vacuous when the move is one-signed at w on D_{NM}, given (BR).
- **(CG3)_w(N_1, N_2, N_3):** there are c_1, c_2, c_3 > 0 such that:
  - each pair satisfies (CG2) with these constants;
  - on D_{123} := {N_1, N_2, N_3 pairwise distinct}, for both cyclic orders (i, k, m),

      c_i δ^i(N_i → N_k) + c_k δ^k(N_k → N_m) + c_m δ^m(N_m → N_i) ≤ 0,

    where δ^i(a → b) := ℓ^{N_i}_w(g, b) − ℓ^{N_i}_w(g, a).
- **Strict versions:** all inequalities hold strictly a.e.

**Lemma 3.0 (pointwise local witness; PROVED; CHECKED (a), 6,000/6,000).** Let F be a set of at most three gated members whose constants satisfy (CG2) and (CG3) at w. Then there is a measurable U(g, ·), weakly increasing in the w-rank, with

  U(g, b) − U(g, N(g)) ≥ c_N δ^N(N(g) → b)  for all N ∈ F and all advice b,

and with an integrable envelope. Under the strict versions the inequality is strict for b ≠ N(g).

*Proof.*
1. **The graph.** At g, form the graph on the four advice values. Gate edges run N(g) → b with weight c_N δ^N. Monotone edges of weight 0 run x → y whenever r_w(y) ≥ r_w(x). A potential exists iff the graph has no positive cycle.
2. **Shortcut.** In any cycle, replace a gate edge x → y followed by a monotone chain y → … → z (where z is the source of the next gate edge) by the single gate edge x → z. Its weight is no smaller, because δ^N is increasing in rank and r_w(z) ≥ r_w(y).
3. **Reduction.** So a positive cycle yields a positive cycle of gate edges between old values. A cycle of length ≥ 4 on at most 3 old values contains a positive simple 2- or 3-cycle. Those cycles are exactly what CG2 and CG3 exclude.
4. **Measurability and integrability.** Take U(g, a) := the longest-path value from a fixed root. It is a finite max of measurable sums, bounded by Σ_N c_N times the envelope.
5. **Strict case.** The cycles are strictly negative, so a small slack can be added to every gate edge. ∎

**Theorem 3.1 (triangle-local (TC); PROVED).**
- **(a)** If (CG2)_w holds for all pairs and (CG3)_w for all triples of gated members, then under (R) at w there is no nontrivial accepted triangle. With guidance, this gives reflexivity, strict (G), (IB) and (TC), for all copies.
- **(b)** The same holds under (R0) for those gates whose CG2/CG3 constraints are strict.
- **(c) Necessity.** Suppose (CG2)_w(N, M) fails, and N = M fails to be w-correct on a non-null part of {N = M}. Then (TC) fails at w.

*Proof.*
- **(a), (b).**
  1. Take an accepted triangle r_1, r_2, r_3 (X ⪯ Y ⪯ Z ⪯ X). For each link choose one reason: guidance, or a gate N_i. Let F be the set of chosen gates, so |F| ≤ 3, and take U from Lemma 3.0.
  2. Put 𝒰(r) := ∫_{supp r} [U(g, new) − U(g, old)]. A gate link through N has old side N on its support, so 𝒰 ≥ c_N Φ^N_w > 0 under (R), and 𝒰 > c_N·Φ^N_w ≥ 0 under strict (R0). A guidance link has 𝒰 ≥ 0, by monotonicity.
  3. The three 𝒰-values telescope to 0 pointwise. So no link is a gate link, and all three are weak worsenings. Their rank changes sum to 0 pointwise, so all are 0. Ranks are injective, so the links are trivial.
  4. Strict (G): a nontrivial pure w-improvement is not guidance, and every field rates it negative.
- **(c).** The sandwich fails, so by Lyapunov (bounded parts of D_{NM} suffice) there is a bounded D ⊆ D_{NM} with ∫_D f^N > 0 > ∫_D f^M (CHECKED (b), 4,000/4,000 atom sets). Take a bounded F ⊆ {N = M} where they are not w-correct.
  - r_1 := (D, N → M) is accepted through N.
  - r_2 := (D, M → N) ∪ (F, N → w-correct) has M as a realiser, with value −∫_D f^M − α(F) > 0 for small F.
  - The composite is a pure w-improvement of N, accepted by neither route.
  - The three models form an accepted triangle whose reverse is a strict guidance reversal, so (TC) fails. ∎

**(d) Weak necessity of CG3 (PROVED).** Suppose (TC) holds at w. Build triangles with X = N_1, Y = N_2, Z = N_3 on D_{123}, and with pair swaps on bounded parts of D_{12}, D_{23}, D_{31}. Every link is then realised. Lyapunov and separation give c ∈ [0, ∞)³ ∖ {0} satisfying the CG3 inequalities for one orientation. CG3 asks for c > 0 for both orientations; the gap is the degenerate case of a zero constant.

### 3.2 Members

**Theorem 3.2 (members; PROVED).** Assume (CG2) for every pair of gated members, and that each gated member N is the a.e.-unique λ_N-Bayes model of ℓ^N with λ_N ∈ Δ_{s(N)}. Then, under (R), and under (R0) wherever the strict versions hold:
- **(a) Universal competitiveness.** N is competitive against every measurable rival on s(N), through its own gate. V_k is competitive at k by guidance.
- **(b) Undominatedness.** No model Y ≠ N satisfies Y ⪯_w N at every w. Hence no member has an all-world tie, and direct (C) holds for members.
- **(c) Strictness.** If C's gate passes C ⪯_w Z, then Z ⋠_w C.
- **(d) Closure.** Rules II–IV of AUDIT_completion add nothing given Thm 3.1. F1 and F2 do not occur. The extension theorem of AUDIT_completion §3 applies.
- **(e) Monotone registration.** Registering a new member removes no acceptance. Its only new obligations are CG2/CG3 for pairs and triples containing it. Existing fields are untouched.

*Proof.*
- **(a)** λ_N·Φ^N(N → X) > 0 for X ≠ N, so some w ∈ s(N) has Φ^N_w > 0, and N realises the record.
- **(b)** Suppose rec(Y, N), with support D, is accepted at w.
  - By guidance: then Φ^N_w(N → Y) ≤ 0.
  - Through a realiser M of Y on D: M ≠ N and D ⊆ D_{MN}. CG2(M, N) gives c_N ∫_D f^N ≥ c_M ∫_D f^M = c_M Φ^M_w(Y → N) ≥ 0, so again Φ^N_w(N → Y) ≤ 0.
  - Since this holds at every w, λ_N·Φ^N(N → Y) ≤ 0, so Y = N by uniqueness.
- **(c)** The same computation with C in place of N gives Φ^C_w(C → Z) ≤ 0 for any accepted reverse.
- **(d)** Rule II has no premise, by Thm 3.1. Rules III and IV have none, by (b). F1 is excluded by strict (G), and F2 by (b).
- **(e)** Acceptances are a union over gates. ∎

**Ordinal refusals and shadows (audit item 2).** Suppose C ⪯_v Y is accepted. PP33 Thm 3.1's refusal of Y ⪯_v Q, for every strict v-improvement Q of C, is a (TC) consequence, so Thm 3.1 delivers it. PP40's shadow condition (B3) is the same statement for installed records. TWG installs no records: every domination is endorsed by the dominator's own gate. I use the ordinal refusal directly, and no numerical budget.

**Lemma 3.3 (endorsement; PROVED).** Let C, M be gated, and let Z = M·z, with z bounded, supported in {C = M}, and a weak w-improvement of M. Suppose C's gate passes C ⪯_w Z. Then M's own field rates C above M at w: Φ^M_w(D_{CM} ∖ supp z: C → M) > 0. In particular, at a world where C is pointwise w-worse than M on D_{CM}, no gate can pass it.

*Proof.*
1. Φ^C_w(C → Z) = Φ^C_w(D′: C → M) + Φ^C_w(z), where D′ := D_{CM} ∖ supp z. The second term is < 0, so Φ^C_w(D′: C → M) > 0.
2. CG2 then gives c_M Φ^M_w(D′: C → M) ≥ c_C Φ^C_w(D′: C → M) > 0. ∎

This is PP33 Thm 3.1 in TWG form. The endorsement is required of the *repaired model's own field*, not of one common field.

**Proposition 3.6 (endorsement is free off the support; PROVED).** If λ_{M,w} = 0, then replacing ℓ^M_w by any strictly guiding integrable field leaves M's Bayes property unchanged. So Lemma 3.3's requirement at w ∉ s(M) is constrained only by CG2/CG3 with the other members.

*Example.* For an edge model N = B_12(t), world 3 is off the support. PP40 Thm 3.3 says the dominations of N's forced rivals must be ℓ^T-negative at world 3, and so must be installed. In TWG they need only N's own world-3 field, which is free up to CG2/CG3. Whether those can be met along the whole edge is OPEN (§5.3).

### 3.3 The referee's counterexamples and PP43

**Proposition 3.4 (PROVED; CHECKED (d)).** The F2 configurations of REFEREE_round49 §4.4 and PP43 Prop 2.2 have V^T_w(T → X) > 0 and V^B_w(T → X) < 0 at every world, where X = T[S ↦ B]. Lemma 3.3's computation shows that CG2(T, B) forbids exactly this: it would need V^B_w(T → X) ≥ κ_w V^T_w(T → X) > 0. With the referee's numbers the two vectors are (3.01, 2.78, 6.43) and (−2.91, −6.10, −2.45) (CHECKED (d)). **The F2 failures come from unions without CG2, not from the zero rule.** This answers coordinator item 1. TWG's fields are integrable throughout, with no tail functionals, and direct (C) for the aggregate is Thm 3.2(b).

**Proposition 3.5 (no global witness is needed; PROVED; CHECKED (c)).**
- (i) Suppose some U and positive constants c_N satisfy U ≥ c_N ℓ^N on N-realised moves, for all N. Then the difference constraints log c_N − log c_M ∈ (sandwich interval) are globally consistent. Conversely, globally consistent constants give such a U, by Lemma 3.0 applied at once to all gates that are old sides at g.
- (ii) Thm 3.1 needs only consistency on triples. CHECKED (c) gives four gates whose triples are all consistent while the whole system is not.
- (iii) The cap path of Thm 4.3 is globally inconsistent at world v: see the proof there. Hence Thm 2.1's Bayes restriction does not apply to it, and TWG is not a single-field realisation.

**PP43 Thm 3.4 does not transfer.** PP43 Lemma 3.1 holds verbatim with own gates: closed sections at p_0 give limsup_n Φ^{B_n}_w(B_n → T) ≤ 0 at every w. Own-Bayes gives only μ_n·Φ^{B_n}(B_n → T) > 0. The two are compatible iff the own margins tend to 0. PP43's killer X_n* needs a *uniform* margin h_0 > 0, which came from the common kernel's Bayes property. In TWG no common bounded part exists. The caps of §4 have margins tending to 0 by construction (Prop 5.2).

---

## 4. The first recursive repair that needs an excluded defender: T's fills

### 4.1 Vertex caps

Fix a world v and s ∈ (0, 2ε/3). Put

  K^v_s := M ∩ {m_v ≤ c + ε − s},  C^v_s := D_{K^v_s},  H_s := {C^v_s ≠ T}.

K^v_s is M with a small corner cut off at the vertex m_v, by a cut parallel to the opposite side. These are refinements of T. PP41 Prop 3.1 shows they are not registrable under PP38's kernel, so PP37's Conjecture 7.1 candidates were excluded.

**Lemma 4.1 (caps; PROVED; (i)–(iii) CHECKED in `caps_exact.out`; (iv) NUMERICS in `caps_mc.out`).**
- **(i)** H_s ⊆ Sil(T). It is a non-null open cone (up to null sets), increasing in s and continuous in measure in s. ∩_{s>0} H_s is null.
- **(ii)** On H_s, the cap's answer σ is v-wrong: σ·g_v < 0.
- **(iii)** H_s meets the three families attached to m_v in non-null sets: A on M_v, and B on M_j for both j ≠ v. Consequently:
  - at world v the cap is pointwise worse than T on H_s;
  - at each w ≠ v the move T → C is **mixed**: it gains on the A-family and on the B-family of M_w, and loses on the B-family of the third world.
- **(iv)** Let Φ(s) := Φ^{ℓ^T}(T → C^v_s) and d(g) := ℓ^T(g, σ) − ℓ^T(g, S). Then:
  - Φ_v(s) > 0;
  - Φ_w(s) = Φ_{w′}(s) for the two worlds w, w′ ≠ v;
  - θ(s) := ess sup over H_s of (u·d)/d_v tends to 0 as s → 0;
  - hence Φ_w(s) ≤ −(1 − 3θ(s))Φ_v(s)/2 < 0 for w ≠ v, once θ(s) < 1/3.

  NUMERICS at ε = 0.3, v = 3: Φ(ε/40) = (−9.8, −9.6, +19.6)·10⁻⁴, with u·Φ/Φ_v falling from 0.030 to 0.004 as s goes from ε/5 to ε/40.

*Proof.*
- **(i)** D_K answers, with M's answer, wherever D_M answers. So C ≠ T only where T is silent and K is unanimous. These are the problems whose plane misses K but meets M: an open cone. Nestedness: K^v_s decreases in s. The cone is non-null by (iii). The planes missing every K^v_s but meeting M pass through m_v, so their union is null.
- **(ii)** A plane that meets M only inside the cut corner separates m_v from K. Since s < 2ε/3, the centre u = (c + ε/3)·1 lies in K. So σ(u·g) > 0 and σ(m_v·g) < 0. Since u·g = Σg/3 and m_v·g = cΣg + εg_v, this gives σg_v < −(c/ε)σΣg < 0.
- **(iii)** Each family's boundary arc on ∂Sil(T) consists of problems whose plane supports M at m_v. (On M_j, j ≠ v, one side of T's B-region is the m_v-side; on M_v, T's A-region is bounded by m_v·g = 0.) Shift such a plane slightly into M. It then cuts off a small triangle at m_v and misses K, so H_s contains a non-null part of Sil(T) next to each arc. The signs per family give the consequences.
- **(iv)**
  - Φ_v > 0 by (ii).
  - Symmetry: the transposition of the two non-v coordinates preserves μ, ℓ^T, M and K, hence T and C, and exchanges w and w′.
  - θ(s) → 0: if g ∈ H_s, its plane meets M only inside a cap of diameter O(s). So ĝ lies within O(s) of the arcs Γ_v of (iii). On Γ_v, σ and silence tie at u (REFEREE_PP32 §3.2, Fact 3), so u·d = 0 there. d/|g| is continuous on each class closure. d_v/|g| is bounded below near Γ_v: d_v = β_v = |g_v| on the A-arc of M_v, and β_v = |g_j|F(s_v) with s_v ≥ d on the m_v-side of M_j.
  - The last bullet: 3u·Φ ≤ 3θΦ_v and Φ_w = Φ_{w′} give 2Φ_w = 3u·Φ − Φ_v ≤ −(1 − 3θ)Φ_v. ∎

### 4.2 One fill, one excluded defender

**The cap's own field.** For a ≥ 1 and b ∈ (0, 1/2], let ℓ^C equal ℓ^T off H_s. On H_s, multiply ℓ^T's world-v penalties by b and its penalties at the two other worlds by a. In words: **the cap discounts its own v-errors on its disagreement cone.**

**Theorem 4.2 (PROVED).** Let X = T[G ↦ N] be a fill: G ⊆ Sil(T) bounded and non-null, N a registered model answering a.e. on G. N = V_j gives the vertex fills, and any N in the repair class is allowed. Suppose that for some v:
- **(F1)** x := Φ^T_v(T → X) > 0;
- **(F2)** G ∩ H_s is null, for some s with θ(s) < 1/6.

Put C := C^v_s. Choose b < min(1/2, x/Φ_v(s)) and a > max(1, max_{w≠v} (−Φ^T_w(T → X))/(−Φ_w(s))). Then:
- **(a)** C is the a.e.-unique u-Bayes model of ℓ^C, so it is registrable at any interior index.
- **(b)** C's own gate passes C ⪯_w X at every w, so C strictly dominates X (Thm 3.2(c)).
- **(c)** The module 𝒫 = {T, V_1, V_2, V_3, C}, with gates ℓ^T, ℓ^C and none, satisfies CG2 and CG3 under (R). So Theorems 3.1(a) and 3.2 hold for it: (TC) with all copies, universal competitiveness, undominatedness, no ties, direct (C) for members, rules I–IV inert, no F1/F2.
- **(d) Which verdicts change** (audit item 1):
  - T's gate is unchanged. The V_k are unchanged. Records realised by both T and C live off H_s, where ℓ^C = ℓ^T, so their verdicts are unchanged.
  - The only new acceptances are records realised by C alone. Among them are records in C's **ℓ^T-kill set**: bounded records out of C refused by ℓ^T at all three worlds. This set is nonempty because C is not ℓ^T-Bayes (Thm 2.1(a); PP41 Prop 3.1).
  - A typical kill record is a partial retreat (H_0, σ → S) with H_0 ⊆ H_s bounded, combined with a small trade along T's tie plane elsewhere. ℓ^T rates it negative at every world. C's gate rates its retreat part at world v by bΦ^T_v instead of Φ^T_v, so it accepts the record at v.
  - The old kernel's acceptances of bounded records realised by no member are gone. No defence used them.

*Proof.*
- **(a)**
  - Off H_s: ℓ^C = ℓ^T and C = T, which is the unique u-optimum.
  - On H_s, σ against silence: the u-value of σ − S under ℓ^C is (1/3)[b·d_v + a(d_w + d_{w′})] = (1/3)[b·d_v + a(3u·d − d_v)] ≤ (d_v/3)[b − a(1 − 3θ)] < 0, since a(1 − 3θ) > 1/2 ≥ b.
  - On H_s, silence against the opposite answer −σ: let d′ := ℓ^T(−σ) − ℓ^T(S). Under ℓ^T at u, silence strictly beats −σ on Sil(T), so u·d′ > 0. Also d′_v = −α_v, because −σ is v-correct. So d′_w + d′_{w′} > α_v, and the ℓ^C-value is (1/3)[−bα_v + a(d′_w + d′_{w′})] > (1/3)(a − b)α_v > 0.
  - Contradiction is costlier than silence at every world.
  - So σ is the strict optimum, with null ties.
- **(b)**
  - rec(C, X) = (H_s: σ → S) ∪ (G: S → N), and the two pieces are disjoint by (F2).
  - At w ≠ v: Φ^C_w = −aΦ_w(s) + Φ^T_w(T → X) > 0, by the choice of a.
  - At v: Φ^C_v = −bΦ_v(s) + x > 0, by the choice of b.
- **(c)** For the move T → C on H_s:
  - at v it is one-signed: f^T = d_v and f^C = b·d_v, so c_T ≤ b·c_C works;
  - at w ≠ v, f^C = a·f^T exactly, so c_T = a·c_C works.

  CG3 is vacuous with two gates. Thm 3.2's hypotheses hold by (a).
- **(d)** Read off the definition of ℓ^C. ∎

**NUMERICS** (`caps_mc.out` (b), (c); ε = 0.3, v = 3, s = ε/20, a = 1, b = 0.001). The cap answer is the strict u-optimum at all 9,571 sampled points of H. Take the fill X = T[ball((1, −0.6, −0.6), 0.05) ↦ V_1], with Φ^T(T → X) = (−1.4, 1.9, 1.9)·10⁻⁵. Then Φ^C(C → X) = (1.99·10⁻³, 1.98·10⁻³, 1.5·10⁻⁵), which is positive at every world.

So **the excluded defender can be registered by changing the bounded verdicts on its own records only, and the repair survives closure.** In the module, this holds with all common-context copies, rules I–IV and the shadow condition (Thm 3.1 gives (TC) outright).

### 4.3 A continuous path out of T's fibre

**Humble fields.** Fix v, s_0 with θ(s_0) < 1/18, b ∈ (0, 1/6) and η > 0. For s ∈ (0, s_0], let ℓ^{C_s} equal ℓ^T off H_s. On H_s:
- world v is multiplied by b;
- at w ≠ v, the penalties are multiplied by (1 + η) where σ is w-wrong and by (1 − η) where σ is w-correct.

C_s over-weights its own errors and under-weights its own gains relative to T. Let R be a (BR) bound for (∫_{P_w}β + ∫_{Q_w}α)/Φ_v(s), uniform in s ≤ s_0, where P_w and Q_w are the w-wrong and w-correct parts of H_s. Choose ηR < 1/36.

**Theorem 4.3 (the cap path; PROVED).** Let 𝒫_v := {T, V_1, V_2, V_3} ∪ {C_s : 0 < s ≤ s_0}, with C_s at the indices of a path q: [0, s_0] → int Δ, q(0) = p_T. Then:
- **(a)** Each C_s is the a.e.-unique u-Bayes model of ℓ^{C_s}. The path s ↦ C_s is continuous in measure, and C_s → T as s → 0. **There is no jump.**
- **(b)** Strict CG2 holds for every pair and strict CG3 for every triple. So Thm 3.1(b) holds with the zero variant (R0) at every gate, and Thm 3.2 holds for every member.
- **(c)** There are no globally consistent positive constants at world v. So 𝒫_v has no global witness of the rescaled-gate form (Prop 3.5(i), (iii)), and Thm 2.1's Bayes restriction does not apply to it.
- **(d) Coverage.** Let X = T[G ↦ N] be a fill, v a world maximising Φ^T_·(T → X), x := Φ^T_v(T → X) and y := max_{w≠v} (−Φ^T_w(T → X))⁺. Then x > y/2. X is strictly dominated by C_s through C_s's gate whenever G ∩ H_s is null and 3y < Φ_v(s) < x/b. That interval is nonempty because b < 1/6. In particular, every fill with 3y < Φ_v(s_0), and with G ∩ H_s null for some s satisfying 3y < Φ_v(s) < x/b, is dominated.

*Proof.*
- **(a)**
  - Bayes is as in Thm 4.2(a). The (1 ± η) factors change the u-values on H_s by at most ηR·d_v, which the margins absorb. The opposite answer keeps a strictly positive margin near Γ_v: the field is non-adjacent, G < F.
  - Continuity: Lemma 4.1(i).
- **(b)**
  - **Pair (T, C_s), move S → σ on H_s.** At v: f^C = b·f^T > 0, so any c_T < b·c_C works. At w ≠ v: f^C/f^T = 1 + η on the w-wrong part and 1 − η on the w-correct part, so any c_T/c_C ∈ (1 − η, 1 + η) works, strictly.
  - **Pair (C_s, C_{s′}), s < s′.** The disagreement set is H_{s′} ∖ H_s, where C_s = T has field ℓ^T. The constraints are the same, with C_s in place of T.
  - **Triples.** All members take values in {S, σ} at each point (nested caps answer alike), so D_{123} is empty. At w ≠ v, equal constants work. At v, take c increasing geometrically along the triple.
  - **Vertices** carry no gate.
- **(c)** For s < s″ < s′, the world-v constraints are c_s < b·c_{s″} < b²·c_{s′}. Between any two caps lie arbitrarily many others, so c_s < b^k·c_{s′} for every k. Hence c_s ≤ 0.
- **(d)**
  - x > y/2: Σ_w Φ^T_w(T → X) > 0, because T is the unique u-Bayes model, and x is the largest of the three values.
  - Domination is as in Thm 4.2(b), with C_s's self-margin at w ≠ v equal to −Φ^{C_s}_w(T → C_s) ≥ (1/2 − 3θ/2 − ηR)Φ_v(s) ≥ (1/2 − 1/12 − 1/36)Φ_v(s) > Φ_v(s)/3.
  - The interval: Φ_v(s) is continuous with Φ_v(0+) = 0 (Lemma 4.1(i)), so the intermediate value theorem gives s. ∎

**What is not covered.** The uncovered fills are those whose G meets H_s for every admissible s. These hug the m_v-arcs at a scale finer than their ℓ^T-size. They include **T's fills by the caps' own answers**, G ⊆ H_{s′}: the first generation-2 repair. Such fills have a positive world v′ whose arcs they avoid. Dominating them needs caps cut at another vertex, and Prop 4.4(b) shows that this implementation cannot register those.

**Proposition 4.4 (limits of this implementation; PROVED).**
- **(a) Amplification is limited by CG3.** Give nested caps C_n, C_m (s_n < s_m) fields that multiply the worlds w ≠ v on their cones by a_n, a_m exactly. Then CG2 is tight, with constant ratios a_m (for T and C_m, and for C_n and C_m on H_m ∖ H_n) and a_n (for T and C_n). CG3 for (T, C_n, C_m) then forces a_n = 1. With humble ratios (a_corr ≤ a_wrong), it forces a^n_corr ≤ a^m_wrong / a^m_corr.
- **(b) Caps at different vertices conflict.** Take C^v_s and C^{v′}_{s′}, v ≠ v′, with Thm 4.3's fields, and look at world v.
  - On H^{v′} ∖ H^v both fields equal ℓ^T·(1 ± η), and the move is mixed (Lemma 4.1(iii) for v′). So c/c′ ∈ (1/(1 + η), 1/(1 − η)).
  - On H^v ∖ H^{v′} the move σ^v → S has f = −b·β_v for C^v and −β_v for C^{v′}. CG2 needs c′ ≤ b·c.
  - These are incompatible for b < 1 − η.

  Repairing this needs C^{v′}'s field on H^v to discount C^v's v-errors too, and to stay silent there by re-weighting elsewhere. **OPEN; CONJECTURE: possible**, since C^{v′}'s field on H^v is constrained only by CG2/CG3 and its own Bayes property.

---

## 5. Sections

**Proposition 5.1 (eventual domination is incompatible with closed sections; PROVED under CG2 and (U)).**
- **Setting.** Let X_k = T[G_k ↦ N_k] be fills with μ(G_k) → 0, none dominated by T. Let registered models C_n sit at indices q_n → q*. Suppose each X_k is dominated by C_n for all n ≥ n(k).
- **(U)** The realisers M used satisfy sup_M (c_M/c_T)·∫_{G_k} env(ℓ^M) → 0.
- **Conclusion.** Some fixed-rival section is not closed.

*Proof.*
1. If all sections are closed, C* := C_{q*} ⪯_w X_k for all w and k.
2. Fix w and k, and let D := {C* ≠ T} ∖ G_k.
   - If the acceptance is by guidance, then T ≥_w C* on D.
   - If it is through a realiser M (possibly C* itself), then M = C* ≠ T on D. CG2(M, T) gives c_T Φ^T_w(D: M → T) ≥ c_M Φ^M_w(D: M → T) > −c_M ∫_{G_k} env(ℓ^M).
3. In both cases Φ^T_w(T → C*) ≤ o(1) as k → ∞, at every w. So λ_T·Φ^T(T → C*) ≤ 0, and C* = T by uniqueness.
4. But T does not dominate X_k. ∎

So dominators of small fills must be **locally finite**: each fixed fill is dominated by members from only a bounded part of the path. Thm 4.3 meets this. For fixed X, the condition Φ_v(s) > 3y fails as s → 0.

**Proposition 5.2 (closed sections on the cap path; PROVED).** In Thm 4.3, with (R0) at every gate and every measurable rival X, each set A_w(X) ∩ q([0, s_0]) is closed. In particular, inheritance at T's index holds: if C_{s_n} ⪯_w X with s_n → 0, then T ⪯_w X. This is the condition PP40 Lemma 2.1 requires, and the own margins tend to 0, as PP43 Lemma 3.1 requires.

*Proof.*
1. Let s_n → s* (s* = 0 gives T), with rec(C_{s_n}, X) accepted at w through guidance or through a realiser C_{s′_n} (C_0 := T).
2. **The realisers converge.** Pass to s′_n → s′. C_{s′_n} = C_{s_n} a.e. on S_n := {C_{s_n} ≠ X}. Since the models converge in measure and take four values, 1_{S_n} → 1_{S*} in measure. So C_{s′} = C_{s*} a.e. on S*: C_{s′} realises rec(C_{s*}, X).
3. **The values converge.** The fields differ only on cones of vanishing measure difference and are bounded by 2·env(ℓ^T). By dominated convergence, Φ^{C_{s′_n}}_w(rec(C_{s_n}, X)) → Φ^{C_{s′}}_w(rec(C_{s*}, X)). The limit is ≥ 0, so (R0) accepts.
4. **Guidance** passes to the limit a.e.
5. **Only these routes exist.** The vertex models carry no gate, and there are no installed records. ∎

Thm 4.3 with Prop 5.2 gives **a connected index path out of T's index** with:
- universal competitiveness of every member against every measurable rival;
- (TC) for all copies;
- undominatedness, and direct (C) for members;
- inert closure;
- closed fixed-rival sections for every measurable rival, relative to the path;
- strict domination of every small fill satisfying Thm 4.3(d).

It contains no jump and needs no installed records.

### 5.3 What is open, exactly

1. **Reaching the edge.** The path stops at a small cap C_{s_0} at an interior index. Continuing it to an edge model while keeping strict CG2/CG3 with every member is OPEN. Endorsement at world 3 is free for edge models (Prop 3.6), and that is the route I would try first.
2. **Cross-family caps** (Prop 4.4(b)). Needed for generation-2 fills, by the caps' own answers, and for fills hugging the m_v-arcs.
3. **The rest of the repair class.** This round does not treat:
   - the vertex rivals' dominators;
   - the forward and backward forced rivals of the caps (by PP30 Thm 3.1 every cap has them);
   - the edge models' forced rivals.

   Lemma 3.3 and Prop 3.6 state what each requires: endorsement by the repaired model's own field, which is free off its support.
4. **Generations.** Thm 3.2(e) makes registration monotone. Every later generation reduces to finding fields that satisfy CG2/CG3 with the members already registered.

---

## 6. Classification, and the audit's instructions

| Obstruction met | Source | Label |
|---|---|---|
| Bayes restriction to ℓ^T's family; T isolated, so T-fills unrepairable | **optional commitment: one witness** (PP38's kernel, any single revised field, PP43's dominance). Completing it is a single-field realisation. | PROVED (Thm 2.1, Prop 2.3) |
| Union of gates without CG2 gives F2 (referee) | chosen design | PROVED (Prop 3.4) |
| PP43 Thm 3.4 (no additive-gate jump) | the common bounded kernel's uniform margin | does not apply in TWG (§3.3) |
| Amplified nested caps | chosen implementation (tight proportional fields) | PROVED (Prop 4.4(a)) |
| Caps at different vertices | chosen implementation (base fields off own cones) | PROVED (Prop 4.4(b)) |
| Eventual domination of all small fills | **axioms + milestone** (closed sections, strict (G), T's uniqueness) under CG2 | PROVED (Prop 5.1) |

Nothing found is an axiom-level impossibility of the milestone.

**Audit instructions.**
1. **Defender and bounded verdicts as variables.** Cor 2.2 names the responsible comparisons: the defender's kill set under the field. Thm 4.2(d) reassigns exactly those, through the defender's own gate, keeping every existing defence (Thm 3.2(e)). The caps are not ℓ^T-Bayes, and they are registered.
2. **Ordinal refusal.** PP33 Thm 3.1 is used as a (TC) consequence, through Thm 3.1. No budget is imposed.
3. **Milestone kept.** Universal competitiveness is proved for every member against every measurable rival (Thm 3.2(a)). Sections are proved for every rival on the path (Prop 5.2). The edge is not reached, and this is stated.
4. **First recursive repair.** T's fills are handled (Thms 4.2, 4.3), including closure, all copies and the shadow condition. Generation-2 fills and the midpoint edge rival are reduced to stated conditions (Prop 4.4(b), Prop 3.6).
5. **No continuity imposed.** The path happens to be continuous. Closed sections were proved, not assumed.
6. **Aggregation.** The rule is the union over guidance and realisers' gates. (TC), undominatedness and direct (C) are proved for the aggregate (Thms 3.1, 3.2).

---

## 7. Status and scripts

| Result | Label |
|---|---|
| Thm 2.1, Cor 2.2, Prop 2.3 | PROVED |
| Lemma 3.0, Thm 3.1 (a)–(c), (d) weak form | PROVED; CHECKED (a), (b) |
| Thm 3.2, Lemma 3.3, Prop 3.6 | PROVED |
| Prop 3.4 | PROVED; CHECKED (d) |
| Prop 3.5 | PROVED; CHECKED (c) |
| Lemma 4.1 | PROVED; (i)–(iii) CHECKED; (iv) NUMERICS |
| Thm 4.2, Thm 4.3, Prop 4.4 | PROVED; Thm 4.2 NUMERICS illustration |
| Props 5.1, 5.2 | PROVED (5.1 under (U)) |
| Cross-family caps; reaching the edge; the rest of the repair class; generations | OPEN; Prop 4.4(b) CONJECTURE |

**Scripts** (`r9/PP42_py/`; run `python3 -I -B <script> > <script>.out` inside the folder):

| Script | Content | Label |
|---|---|---|
| `tc_local_witness.py` → `.out` | (a) Lemma 3.0 against Bellman–Ford, 6,000 instances; (b) sandwich ⇔ no P1 mixture, 4,000 atom sets; (c) the 4-cycle (triples consistent, global inconsistent); (d) the referee's F2 pair violates CG2. ALL PASS | CHECKED |
| `caps_exact.py` → `.out` | Lemma 4.1(i)–(iii): 11,314 disagreement points over ε ∈ {1/10, 3/10}, v = 1, 2, 3, two cut sizes; T silent, answer v-wrong, the three families, swap symmetry. ALL PASS | CHECKED |
| `caps_mc.py` → `.out` | Lemma 4.1(iv) signs and θ; cap Bayes under its own field; one fill dominated (Thm 4.2) | NUMERICS |
| `field40.py` | PP40's independent implementation of ℓ^T (copied) | library |

**Most important next step.** Extend the cap path to the edge [e_1, e_2], keeping strict CG2/CG3 along the way. Edge models' world-3 fields are free (Prop 3.6), which is exactly the freedom PP40's R3 lacked. Then attack Prop 4.4(b) with non-base fields on other caps' cones.
