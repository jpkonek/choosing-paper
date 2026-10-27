# PP49. The consolidated whole-simplex sufficiency theorem for posterior gates

23 October 2026. Task PP49 of Brief 52. One reader (me); not refereed.

**Labels.** PROVED: a complete argument is given here, or a cited result is named together with its refereeing status. CHECKED: an exact rational computation in `r9/PP49_py/posterior_checks.py` (its output ends ALL PASS). NUMERICS: none is used. CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF52. AUDIT_round52, AUDIT_posterior_pairs and AUDIT_round52_answers, which are binding. PP42 (Lemma 3.0, Thms 3.1, 3.2, Prop 3.5, Prop 5.2). REFEREE_round50 (Thm R1, the necessity of CG2 without the agreement region, Lemma S). PP47 (Lemma 1.2, Lemma 1.3, Cor 2.3, Thm 2.5, Thm 4.1). PP45 (Lemmas 2.1 and 2.3) and PP46 (Lemma A0, Thm D). LEAD_selection_count. AUDIT_completion (rules I–IV, F1/F2). REFEREE_PP32 §4.3. PP12 (Obs. 1, Thm E). DESIGN_MEMO §8.11, §8.20. Two further sources, for the necessary side only: *The Contamination Triangle* (r9/writeup; Thm `kkm`, Prop `necessary`, Thm `main`, Cor `coverage`), and FF2 Thm 4.1 / Cor 4.3 (refereed in GG3: "CORRECT, modulo its import chain").

**Ground rules kept.** I do not impose λ_a = a, rescaling invariance, or transported fields. Nothing is equivalent to the CPM realisation problem: no single field selects the family. I add no assumptions beyond the single hypotheses list of §2.

---

## 0. Result

### 0.1 The theorem

Fix the posterior selection a ↦ C_a = D_{M_a} on the **closed** simplex Δ, with M_a = {a∘p/(a·p) : p ∈ M} and M = c·1 + εΔ. Each index a ∈ Δ, boundary included, carries a field f^a = (f^a_1, f^a_2, f^a_3). At world w a record is accepted iff it is guidance, or some C_b (b ∈ Δ) equals the record's old side a.e. on its support and has gate value ≥ 0 at w. Assume (H0)–(H5) of §2. In words:
- (H0) the fields are strictly guiding;
- (H1) each C_a is weakly own-Bayes at a weight supported in supp a;
- (H2) every pair satisfies strict CG2 with positive constants;
- (H3) every triple satisfies the zero-accepting triangle condition;
- (H4) the field differences are L¹-continuous on Δ;
- (H5) there are no other acceptance routes.

**Theorem A (consolidated sufficiency; PROVED).** Under (H0)–(H5):
1. **Structural axioms.** Reflexivity, weak and strict (G), (IB) for every common-context copy, and (TC) all hold on the full measurable four-advice domain. Moreover, **two distinct models are never tied at any single world**.
2. **(S) on the whole simplex.** Every C_a is coherent and competitive on supp a. Every C_a is undominated in a strong sense: no Y ≠ C_a has Y ⪯_w C_a at every w ∈ supp λ_a. For every measurable rival X and every world w, the section A_w(X) = {a ∈ Δ : C_a ⪯_w X} is closed in Δ.
3. **(LA).** T1 = C_u is coherent and undominated.
4. **Direct (C), model by model.** For every model N, the only model tied with N at all three worlds is N itself. So no selected model is all-world tied with any other model, and the all-world tie partners of any coherent undominated model are coherent and undominated.
5. **Dominance.** For every measurable X there is a ∈ Δ with C_a ⪯_w X at all three worlds. If X is not one of the C_a, then C_a ≺_w X **at every world**. Hence:
   - the undominated models are exactly the C_a, and all of them are coherent;
   - every incoherent model, and every coherent model outside the family, is strictly dominated by a selected model;
   - the closure rules I–IV of AUDIT_completion add nothing, and neither F1 nor F2 occurs.

**Exactness (PROVED).**
- Under (H0), (H2), (H5) and zero-accepting gates, (TC) holds **iff** (H3) holds.
- (H1) is necessary for competitiveness (PP47 Lemma 1.2).
- The non-strict sandwich form of (H2) is necessary for (TC), for every pair of gated members, boundary members included (REFEREE_round50 §1.2).
- So the remaining gap between the hypotheses and the axioms is exactly the strictness in (H2) and the L¹-continuity in (H4). Both are stated precisely in §6.

**Theorem N (no global prices; PROVED modulo FF2's import chain).** Every solution of (H0)–(H5) has a world at which no global witness exists: no single integrable, strictly guiding field endorses every accepted comparison out of every selected model. Under a uniform-gap condition (UG), this means: at that world no single set of compatibility constants is consistent for all members. If global witnesses existed at all three worlds, every C_a would be a Bayes model of one field U, at the explicit weight μ_a ∝ λ_a/c_a. FF2 Thm 4.1 excludes that for every strictly guiding integrable field on the full domain, and the Contamination Triangle Cor `coverage` excludes it for non-adjacent fields. So **any solution must lack global prices** at some world (§7).

### 0.2 What changes relative to earlier statements

- **Uniqueness is not needed.** Once pairs are strict, weak own-Bayes suffices. Strictness lives in (H2): every nontrivial accepted record has a refused reverse (Lemma 3.2). That one fact delivers undominatedness, direct (C) and the strictness of every domination. PP42 Thm 3.2 assumed a.e.-uniqueness; PP47 Thm 2.5 shows what goes wrong without strict pairs.
- **The posterior family is not two-valued.** Triples such as (T, V_1, V_2), or (T, C_{(.8,.1,.1)}, C_{(.1,.8,.1)}), give three different answers on a non-null set (CHECKED (A1)). So PP47 Thm 4.1, which is a two-valued test, cannot be the whole-simplex triple hypothesis. (H3) is the exact triangle condition. Lemma 3.4 gives a field-level criterion for it that:
  - is per orientation;
  - covers three-valued points;
  - reduces to PP47 Thm 4.1 on two-valued triples and contains PP42's strict CG3.
- **Triples whose posterior credal sets pairwise overlap are two-valued** (Lemma 1.2). That includes all sufficiently close interior triples. So PP47 Thm 4.1 is exactly the local test, and the three-valued form matters for far triples and for boundary members.
- **Boundary.** Every index carries a gate. The gate of V_w at world w is redundant, because guidance already accepts all its records. Every other boundary gate is needed so that the realisers form a compact family, and it must satisfy (H2)–(H4).
- **The pair-ordering theorem extends to boundary pairs**, in extended reals (Prop 5.2; PROVED; CHECKED (B)).

| Item | Result | Label |
|---|---|---|
| Posterior family continuous in measure on closed Δ; vertices V_i; faces | Lemma 1.1 | PROVED |
| Overlapping posteriors never give opposite answers; three-valued triples exist | Lemma 1.2 | PROVED; CHECKED (A) |
| Vertex gate at own world redundant | Lemma 3.1 | PROVED |
| No ties at any world; strict links | Lemma 3.2 | PROVED |
| Strict potentials for ≤ 2 gates | Lemma 3.3 | PROVED |
| Field-level criteria for (H3); reconciliation of PP42 and PP47 | Lemma 3.4, §3.3 | PROVED |
| Theorem A (1)–(5); exactness | §4 | PROVED |
| Section lemma by F_w(X) projection; boundary limits | Prop 4.3 | PROVED |
| Boundary checklist; boundary pair-ordering | §5, Prop 5.2 | PROVED; CHECKED (B) |
| Necessity and gaps | §6 | PROVED / OPEN as stated |
| No global prices; single-field reduction | Thm N, Cor 7.4 | PROVED modulo FF2's chain |

---

## 1. Setting and one set of conventions

**Problems and models.**
- Ω = R³ with the Gaussian measure μ. Problems are taken modulo sign.
- The advice set is A = {+, 0, −, ×}: accept g, silence, accept −g, contradiction.
- r_w is the world-w rank: correct 0 < silent 1 < wrong 2 < contradictory 3. It is injective on A, for a.e. g.
- A model is a measurable map Ω → A, taken modulo null sets.
- The record of Y → X is rec(Y, X) = (S, Y|_S, X|_S), with support S := {Y ≠ X}. Y is its **old side**.

**Fields and values.**
- A field f^a assigns to each world w a measurable f^a_w : Ω × A → R.
- δ^a_w(g; x→y) := f^a_w(g, y) − f^a_w(g, x).
- The gate value of a record is Φ^a_w(Y → X) := ∫_S δ^a_w(g; Y(g) → X(g)) dμ.

**Realisers and pair notation.**
- C_b **realises** rec(Y, X) if C_b = Y a.e. on S.
- D_ab := {C_a ≠ C_b}. On D_ab, put φ^a_ab := δ^a_w(C_a → C_b) and φ^b_ab := δ^b_w(C_a → C_b). Both value the *move C_a → C_b*. By strict guidance both have the sign of r_w(C_b) − r_w(C_a).
- This is PP42's (f^N, f^M) with N = C_a and M = C_b. It is also PP45's e^N, e^M, and PP47's interval I_ab written in log-constants.

**Acceptance rule (R0, gate union).** Y ⪯_w X iff
- **(G)** r_w(X) ≥ r_w(Y) a.e. on S; or
- **(R0)** some b ∈ Δ has C_b realising rec(Y, X) and Φ^b_w(Y → X) ≥ 0.

This is the rule of Lemma S and of PP47 Thm 4.1. I use the zero-accepting rule throughout, never the strict rule (R). A refusal is global: guidance and every realiser refuse.

**Axioms** (BRIEF52):
- reflexivity, strict (G), (IB), and (TC) only. (TC) says: if A ⪯ B ⪯ C then not C ≺ A; equivalently, every accepted triangle has its reverses.
- (S) on the whole simplex, (LA), and direct (C).
- Single-world ties and compositions are allowed.
- Undominated: no Y with Y ⪯_w N at every w and Y ≺_w N at some w.

**The family.**
- By PP12 Obs. 1 (PROVED, CHECKED there), C_a(g) = T1(a∘g) for every a ∈ Δ, boundary included.
- T1 accepts h iff m_i·h > 0 for i = 1, 2, 3, where the m_i = c·1 + εe_i are the vertices of M. It accepts −h iff m_i·h < 0 for all i, and is silent otherwise.

**Lemma 1.1 (the family on the closed simplex; PROVED).**
- (a) a ↦ C_a is continuous in measure on Δ.
- (b) C_{e_i} = V_i, the model correct at world i a.e.
- (c) For a in the relative interior of a face F_S (S = supp a), M_a lies in the relative interior of F_S, and C_a depends on g only through (g_i)_{i∈S}.
- (d) a ↦ C_a is injective.

*Proof.*
- (a) C_a(g) is determined by the signs of the three numbers (m_i∘a)·g. Each depends continuously on a. Since m_i > 0 and a ≠ 0, each m_i∘a ≠ 0, so each zero set {g : (m_i∘a)·g = 0} is a null plane. So for a.e. g and every a_n → a, C_{a_n}(g) = C_a(g) eventually. Dominated convergence then gives μ{C_{a_n} ≠ C_a} → 0.
- (b) For a = e_i, (m_j∘e_i)·g = (c + ε·[j = i])·g_i, which has the sign of g_i.
- (c) (a∘p)_i = 0 exactly for i ∉ S, and p > 0 on M.
- (d) Different faces give disjoint credal sets. Within a face, max_{q∈M_a} q_i/q_j = (a_i/a_j) max_{p∈M} p_i/p_j (AUDIT_posterior_pairs §1), so M_a determines a. And D_K determines K. ∎

**Lemma 1.2 (two-valued and three-valued triples; PROVED; CHECKED (A)).**
- (a) Two coherent models D_K and D_{K'} give opposite answers on a non-null set iff K ∩ K' = ∅. So if M_a, M_b, M_c pairwise intersect, the triple is two-valued: D_abc := {C_a, C_b, C_c pairwise distinct} is null.
- (b) Three-valued triples exist in the posterior family. One example, at ε = 3/10: at g = (1, −1, 1/10), T1 is silent, C_{(.8,.1,.1)} accepts g and C_{(.1,.8,.1)} accepts −g. All margins are strict, so the set is open and non-null. (T, V_1, V_2) is three-valued at the same g.

*Proof of (a).* Accepting g and −g requires min_K m·g > 0 > max_{K'} m·g, which is impossible if K ∩ K' ≠ ∅. Conversely, disjoint compact convex sets are strictly separated by an open cone of gambles.
- If a, b are interior and close to each other, then M_b is Hausdorff-close to M_a (Lemma 1.1 and AUDIT_posterior_pairs §1). M_a has nonempty relative interior, so the two sets intersect.
- CHECKED (A2): 3,000 overlapping nearby pairs gave no opposite answer. ∎

So PP47 Thm 4.1 applies exactly to the *local* triples. The whole-simplex hypothesis needs three-valued points. This is the first convention to reconcile (§3.3).

---

## 2. The single list of hypotheses

**(H0) Fields.** For every a ∈ Δ and every w:
- f^a_w is measurable;
- f^a_w(g, ·) is strictly increasing in r_w, for a.e. g.

**(H1) Own-Bayes, weak and pointwise.** For every a ∈ Δ there is λ_a ∈ Δ with supp λ_a ⊆ supp a, such that for a.e. g, C_a(g) minimises x ↦ Σ_w λ_{a,w} f^a_w(g, x) over all four advice values.
- λ_a need not equal a, need not depend continuously on a, and need not be unique.
- **No uniqueness of the minimiser is required.**
- At a vertex, λ_{e_i} = e_i, and (H1) holds for every strictly guiding field.

**(H2) Strict pairs.** Fix a world w and distinct indices a, b, neither equal to e_w. There are constants κ, κ′ ∈ (0, ∞), which may depend on (a, b, w), such that

  κ·φ^a_ab < κ′·φ^b_ab  a.e. on D_ab.

- For a two-signed move this is the strict sandwich ess sup_{φ^a<0} φ^b/φ^a < … < ess inf_{φ^a>0} φ^b/φ^a, with strict pointwise inequalities. That is PP42's strict CG2 and PP47's "strict CG2 a.e.".
- For a one-signed move it is a bounded-ratio condition.
- Pairs that contain e_w at world w are exempt (Lemma 3.1).

**(H3) Triangle condition (zero-accepting, exact).** Fix a world w and an ordered triple (a, b, c) of distinct indices, none equal to e_w. Then there is no nontrivial triangle of models X, Y, Z with all three of:
- C_a realising rec(X, Y), with Φ^a_w(X → Y) ≥ 0;
- C_b realising rec(Y, Z), with Φ^b_w(Y → Z) ≥ 0;
- C_c realising rec(Z, X), with Φ^c_w(Z → X) ≥ 0.

(H3) involves only three fields and three models. Lemma 3.4 gives field-level criteria:
- PP42's strict CG3, which covers three-valued points;
- a per-orientation constant criterion, which covers three-valued points;
- PP47 Thm 4.1, which is exact on two-valued triples.

**(H4) Continuity.**
- **(a)** a ↦ C_a is continuous in measure on Δ. This is automatic by Lemma 1.1.
- **(b)** For every w and every x, y ∈ A, the map a ↦ δ^a_w(·; x→y) is continuous from Δ into L¹(μ). In particular every gate value is finite. At (e_w, w), (b) can be dropped (Remark 4.4).
- **(c)** (Used only in §7.) A common integrable envelope: |δ^a_w(g; x→y)| ≤ E(g) for all a, w, x, y, with E ∈ L¹(μ). By dominated convergence, (c) together with pointwise convergence implies (b).

**(H5) No other routes.** Acceptance is exactly (G) ∪ (R0), with realisers ranging over all of Δ. There is no kernel, no installed record and no gate outside the family.

*Not assumed:*
- (BR);
- PP42's hypothesis (U);
- uniqueness in (H1);
- λ_a = a;
- invariance;
- transported fields;
- any lower bound on interval widths;
- global constants;
- the pair-ordering certificate D = log(a/b).

---

## 3. Tools

### 3.1 Redundancy, strict links, potentials

**Lemma 3.1 (the vertex gate at its own world is redundant; PROVED).** Any record accepted at world w through the gate of V_w is a weak w-worsening, so guidance accepts it.

*Proof.* Its old side equals V_w on the support, and V_w has w-rank 0 a.e. ∎

Consequently, in every proof below, a link accepted through (e_w, w) is treated as a guidance link. This is why (H2) and (H3) exempt e_w at world w. The vertex gates at the *other* worlds are not redundant (§5).

**Lemma 3.2 (strict links: no ties at any world; PROVED).** Assume (H0), (H2) and (H5). If a nontrivial record P → Q is accepted at w, then its reverse Q → P is refused at w. Hence:
- two distinct models never tie at any world;
- the relation at each world is antisymmetric.

*Proof.* Let S be the support of the record; it is non-null.
1. **P → Q by guidance.** Q is strictly w-worse than P at every point of S.
   - The reverse is not guidance.
   - Any realiser M of Q has Φ^M_w(Q → P) < 0, because the integrand is negative on S by strict guidance.
2. **P → Q through a gate a, with C_a = P on S.** If a = e_w, step 1 applies (Lemma 3.1). Otherwise:
   - **Reverse by guidance.** Then P → Q is a nontrivial weak improvement, so Φ^a_w(P → Q) < 0. This contradicts the acceptance.
   - **Reverse through a gate b, with C_b = Q on S.** Then S ⊆ D_ab, and on S the move P → Q is the move C_a → C_b. If b = e_w, guidance refuses the forward record, so that case cannot occur. Otherwise (H2) gives κ′∫_S φ^b_ab > κ∫_S φ^a_ab = κΦ^a_w(P → Q) ≥ 0. So Φ^b_w(Q → P) = −∫_S φ^b_ab < 0, and gate b refuses. ∎

This is PP47 Lemma 1.3. The proof covers every realiser of the whole simplex, boundary members included.

**Lemma 3.3 (strict potentials for at most two gates; PROVED, the strict form of PP42 Lemma 3.0).** Fix w and a set F of at most two indices, none equal to e_w. Assume (H0), (H2) and (H4)(b). Then there are constants c_N > 0 (N ∈ F) and a measurable U : Ω × A → R with the following properties:
- U is weakly increasing in r_w;
- |U| is bounded by a finite sum of L¹ functions;
- for a.e. g, every N ∈ F and every x ≠ C_N(g): U(g, x) − U(g, C_N(g)) > c_N·δ^N_w(g; C_N(g) → x).

*Proof.* For |F| = 2, take (c_a, c_b) := (κ, κ′) from (H2); for |F| = 1 take c = 1.

At a fixed g, build a graph on the four advice values:
- gate edges C_N(g) → x (x ≠ C_N(g)) of weight c_N δ^N;
- monotone edges x → y of weight 0 whenever r_w(y) > r_w(x).

A potential with strict gate inequalities exists iff every cycle that contains a gate edge has strictly negative weight. (Add a slack η(g) > 0, smaller than the least |weight| of such simple cycles divided by 8, and take longest paths from a root.) Take any such cycle:
1. **Shortcut.** Replace each gate edge C_N(g) → x, together with the monotone chain x → … → z that follows it, by the single gate edge C_N(g) → z. Since ℓ^N is strictly increasing and r(z) > r(x), the weight strictly increases whenever the chain is nonempty.
2. **What remains.** A closed walk of gate edges between old values. Old values occur at most twice, so this walk consists of self-loops of weight 0, and, where C_a(g) ≠ C_b(g), of 2-cycles of weight c_aφ^a_ab − c_bφ^b_ab < 0.
3. **Strict negativity.** If only self-loops remain, every chain was nonempty (gate edges go to x ≠ C_N(g)), so the original weight was strictly below 0. Otherwise some 2-cycle with negative weight remains.
4. **Measurability and bounds.** These are as in PP42 Lemma 3.0. ∎

### 3.2 The triangle condition and its field-level criteria

Fix w and an ordered triple o = (a, b, c) of distinct indices, none equal to e_w. Write A = C_a(g), B = C_b(g), C = C_c(g). A triangle as in (H3) is, pointwise, a configuration (X(g), Y(g), Z(g)) with three constraints: X = A where X ≠ Y; Y = B where Y ≠ Z; Z = C where Z ≠ X. Enumerating the cases, the nonzero pointwise link vectors (δ^a(X → Y), δ^b(Y → Z), δ^c(Z → X)) are exactly:
- P_ab(g) = (φ^a_ab, −φ^b_ab, 0), when A ≠ B;
- P_bc(g) = (0, φ^b_bc, −φ^c_bc), when B ≠ C;
- P_ca(g) = (φ^a_ac, 0, −φ^c_ac), when A ≠ C;
- Q_o(g) = (δ^a(A→B), δ^b(B→C), δ^c(C→A)), when A, B, C are pairwise distinct.

Write V_o(g) for this set. A configuration is nontrivial at g iff its vector is nonzero, by strict guidance. So (H3) for o says: there is no measurable selection v(g) ∈ {0} ∪ V_o(g), nonzero on a non-null set, with ∫v ≥ 0 componentwise.

**Lemma 3.4 (field-level criteria for (H3); PROVED).**
- **(i) Constant criterion, per orientation.** Suppose there is κ ∈ (0, ∞)³ with:
  - κ·v ≤ 0 for every v ∈ V_o(g), for a.e. g;
  - no measurable selection v(g) ∈ {0} ∪ Z_o(g), nonzero on a non-null set, has ∫v = 0. Here Z_o(g) := {v ∈ V_o(g) : κ·v = 0}.

  Then (H3) holds for o.
- **(ii) PP42's strict CG3 implies (i).** Suppose one triple of constants gives a strict potential for {a, b, c}, so all old-value 2- and 3-cycles are strictly negative a.e. Then κ·v < 0 for every v ∈ V_o(g), so Z_o is empty and (i) holds, for both orientations.
- **(iii) PP47 Thm 4.1 is (i) on two-valued triples.** Suppose D_abc is null and (H2) holds. Then condition (i) holds for o iff the following two conditions hold, and these are PP47 Thm 4.1's (a) and (b):
  - (a) there is κ > 0 satisfying the three closed pair inequalities κ_aφ^a ≤ κ_bφ^b and the two cyclic analogues;
  - (b) no κ as in (a) has all three pair-equality sets non-null, with orientations whose rays sum to zero with positive weights (the "tight triple with all extremes attained").

  Given (BR), PP47 also proves that (TC) is equivalent to (a) and (b). So on two-valued triples the criterion is exact.

*Proof.*
- **(i)** Take a nontrivial o-triangle with ℓ := ∫v ≥ 0. Then κ·ℓ ≥ 0 and κ·ℓ = ∫κ·v ≤ 0, so κ·v = 0 a.e. and v ∈ {0} ∪ Z_o a.e. Since κ > 0 and ℓ ≥ 0 with κ·ℓ = 0, we get ℓ = 0. This contradicts the second clause.
- **(ii)** Telescoping at g gives Σ (link weights) < Σ (U-differences) = 0 at every nontrivial configuration.
- **(iii)** V_o(g) contains only the P-vectors, and κ·P_ab ≤ 0 ⟺ κ_aφ^a_ab ≤ κ_bφ^b_ab. So the first clause of (i) is the closed test (a).
  - The zero vectors of a pair lie on the line spanned by (κ_b, −κ_a, 0), or its cyclic analogues. (H2) makes each pair's equality set one-signed: equality of the ratio on non-null parts of both sign regions would contradict the strict sandwich. So each pair contributes one ray.
  - The three rays are pairwise independent and satisfy one positive linear relation, κ_c(κ_b, −κ_a, 0) + κ_a(0, κ_c, −κ_b) + κ_b(−κ_c, 0, κ_a) = 0.
  - So a nontrivial zero selection with ∫ = 0 exists iff all three equality sets are non-null and their rays are those of that relation. By non-atomicity the masses can then be matched, as in PP47's Ex1. That is the negation of (b). ∎

### 3.3 Reconciliation of PP42 Thms 3.1/3.2 and PP47 Thm 4.1

| Point | PP42 Thm 3.1/3.2 | PP47 Thm 4.1, Lemma 1.3 | This note |
|---|---|---|---|
| Acceptance | (R); (R0) only with strict CG | (R0) | (R0) throughout (Lemma S needs it) |
| Gated models | non-vertex members; vertices ungated | all family members | every a ∈ Δ; (e_w, w) redundant (Lemma 3.1) |
| Pair condition | CG2 with positive constants; strict for (R0) | strict CG2 a.e. plus (BR) | (H2): strict, positive constants; no (BR) |
| Triple condition | CG3: one κ for both orientations, plus 3-cycles on D_123 | two-valued: closed test plus no attained tight triple | (H3) exact; criterion (i) per orientation, three-valued points included; contains both (Lemma 3.4) |
| Bayes | a.e.-unique, λ_N ∈ Δ_{s(N)} | weak Bayes forced (L1.2); Thm 2.5 shows weak Bayes plus non-strict CG2 gives F2 | weak suffices given (H2) |
| Ties | no all-world tie for members | no tie at any world | no tie at any world, for all models |
| Closure | (d) needs the triple condition (referee) | — | rules I–IV inert (§4.5) |
| Sections | path, Prop 5.2 / Lemma S | Lemma S | F_w(X) projection on closed Δ (Prop 4.3) |

The sign conventions agree:
- PP42's (f^N, f^M) is (φ^a_ab, φ^b_ab) with N = C_a and M = C_b.
- PP47's I_NM is the set of feasible log(κ_a/κ_b).
- PP45's D_w = −log(κ_wλ^M_w/λ^N_w).

---

## 4. Proof of Theorem A

### 4.1 Reflexivity, (G), (IB)

- **Reflexivity.** A trivial record is guidance.
- **Weak (G).** This is guidance.
- **Strict (G).** Suppose Y is pointwise no worse than X at w and strictly better on a non-null set. Then on S = {Y ≠ X} it is strictly better everywhere, since ranks are injective. The reverse X ⪯_w Y is not guidance, and every realiser b of X gives Φ^b_w(X → Y) < 0 by (H0).
- **(IB).** Both clauses of the acceptance rule depend only on (S, Y|_S, X|_S): the guidance inequality, the realiser condition and the integral. So all common-context copies share one verdict.

### 4.2 (TC)

Take an accepted triangle X ⪯_w Y ⪯_w Z ⪯_w X. Choose a reason for each link. Reclassify links through (e_w, w) as guidance (Lemma 3.1). Let F be the set of gate indices used.
- **Case |F| ≤ 2.** Take U from Lemma 3.3 and put 𝒰(r) := ∫_{supp r} [U(new) − U(old)]. These integrals are finite by (H4)(b).
  - A guidance link has 𝒰 ≥ 0.
  - A gate link through N with non-null support has 𝒰 > c_N Φ^N_w ≥ 0.
  - The three values telescope to 0, so no link is a nontrivial gate link.
  - All the links are then weak worsenings whose rank increments sum to 0 pointwise. So every increment is 0, and the triangle is trivial.
- **Case |F| = 3.** Every link is a gate link through three distinct indices, none equal to e_w. (H3) says the triangle is trivial.

So **every accepted triangle is trivial**, X = Y = Z, and (TC) holds: A ⪯ B ⪯ C ⪯ A forces A = C, and then A ⪯ C by reflexivity. No transitivity is claimed, and none is needed. The argument applies to arbitrary measurable models, so it covers all common-context copies.

**Exactness.** Suppose (H3) fails for some triple. Then a nontrivial accepted triangle exists. By Lemma 3.2 its reverses are refused, so (TC) fails. Hence, given (H0), (H2) and (H5), (TC) ⟺ (H3). ∎

### 4.3 (S)

**Coherence.** C_a = D_{M_a}.

**Competitiveness on supp a.** Let X ≠ C_a. By (H1), λ_a·Φ^a(C_a → X) = ∫ Σ_w λ_{a,w} δ^a_w(C_a → X) ≥ 0, since the integrand is pointwise ≥ 0 and integrable by (H4)(b). So some w ∈ supp λ_a ⊆ supp a has Φ^a_w(C_a → X) ≥ 0. C_a realises its own record, and (R0) accepts it.
- For a vertex this is guidance at world i.
- For an edge index it is a world of the edge.

**Undominatedness, strong form.** Let Y ≠ C_a and suppose Y ⪯_w C_a at some w ∈ supp λ_a. I show Φ^a_w(C_a → Y) < 0.
- **Guidance.** C_a → Y is a nontrivial weak improvement at w, so its value is negative by (H0).
- **Gate b.** C_b = Y on S ⊆ D_ab, and −∫_S φ^b_ab = Φ^b_w(Y → C_a) ≥ 0.
  - If b = e_w, this is the guidance case.
  - Otherwise (H2) gives κ∫_S φ^a_ab < κ′∫_S φ^b_ab ≤ 0.

If this holds at every w ∈ supp λ_a, then λ_a·Φ^a(C_a → Y) < 0, which contradicts (H1). So no Y ≠ C_a is weakly no worse than C_a at all worlds of supp λ_a. In particular C_a is undominated. Only weak Bayes was used.

**Closed sections.** See Prop 4.3.

**Proposition 4.3 (sections by projection; PROVED).** Assume (H0), (H4)(a)–(b) and (H5). Fix a measurable X and a world w. Write S_a := {C_a ≠ X}. Define:
- G_w(X) := {a ∈ Δ : r_w(X) ≥ r_w(C_a) a.e.};
- F_w(X) := {(a, b) ∈ Δ × Δ : C_b = C_a a.e. on S_a, and Φ^b_w(C_a → X) ≥ 0}.

Then G_w(X) and F_w(X) are closed. Since Δ is compact, the projection π_1(F_w(X)) is closed. Hence A_w(X) = G_w(X) ∪ π_1(F_w(X)) is closed.

*Proof.* Let a_n → a and b_n → b. Put E_n := {C_{a_n} ≠ C_a}; then μ(E_n) → 0 by (H4)(a), and S_{a_n} Δ S_a ⊆ E_n.
1. **Guidance.** Along a subsequence, C_{a_n}(g) = C_a(g) eventually, for a.e. g, because there are four values and convergence is in measure. The pointwise inequality passes to the limit.
2. **Realisation passes to the limit.**
   μ(S_a ∩ {C_b ≠ C_a}) ≤ μ{C_b ≠ C_{b_n}} + μ(S_a ∩ {C_{b_n} ≠ C_{a_n}}) + μ(E_n).
   The middle term is at most μ(S_{a_n} ∩ {C_{b_n} ≠ C_{a_n}}) + μ(E_n) = μ(E_n). All three terms tend to 0.
3. **Values pass to the limit.** Write h_n(g) := δ^{b_n}_w(g; C_{a_n}(g) → X(g)) and h(g) := δ^b_w(g; C_a(g) → X(g)). Both vanish off S_{a_n} and S_a respectively. Then
   |h_n − h| ≤ Σ_{x,y} |δ^{b_n}_w(x→y) − δ^b_w(x→y)| + 1_{E_n}·2 max_{x,y} |δ^b_w(x→y)|.
   The first term tends to 0 in L¹ by (H4)(b). The second tends to 0 by absolute continuity of a single integrable function. So Φ^{b_n}_w(C_{a_n} → X) → Φ^b_w(C_a → X), and the limit is ≥ 0.
4. **Projection.** Any sequence in π_1(F_w(X)) lifts to a sequence in F_w(X) whose b-coordinates have a convergent subsequence. ∎

This is the audit's F_i(X) argument. It handles **changing realisers along a converging sequence**, including realisers that converge to edge and vertex indices: Δ is closed and every boundary index carries a gate.

**Remark 4.4 (at (e_w, w) no field is needed).** Suppose b_n → e_w at world w. Then the limit record has old side V_w on S_a, so it is a weak w-worsening, and guidance accepts it. So (H4)(b) at (e_w, w) can be dropped, by splitting F_w(X) into the closed sets {b = e_w} and {b ≠ e_w}.

**Inheritance at the boundary.** If a_n → a ∈ ∂Δ and C_{a_n} ⪯_w X for every n, then C_a ⪯_w X. For a = e_i and w ≠ i, the limit acceptance is carried by a limit realiser's gate. For a = e_i and w = i it is guidance. Lemma 1.1 supplies the convergence in measure at every boundary point.

### 4.4 (LA) and direct (C)

- **(LA).** C_u = T1 is coherent and undominated (§4.3).
- **Direct (C).** By Lemma 3.2, distinct models never tie at any single world, so a model tied with N at all worlds equals N. This is the model-by-model form, and it holds for every model, selected or not.

### 4.5 Dominance, the undominated class, and closure

**Dominance (KKM).** Fix X. The sets A_1(X), A_2(X), A_3(X) are closed (Prop 4.3). For every face Δ_S and every p ∈ Δ_S, competitiveness gives some w ∈ supp p ⊆ S with p ∈ A_w(X). So Δ_S ⊆ ∪_{w∈S} A_w(X). By the KKM lemma, ∩_w A_w(X) ≠ ∅: there is a with C_a ⪯_w X at every w. This is LDG Thm `kkm` / Contamination Triangle Thm `kkm`; no transitivity is used.
- If X ≠ C_a, Lemma 3.2 refuses every reverse, so C_a ≺_w X at every w.

**The undominated class.** Let N be undominated and take a as above. Then C_a ≺_w N cannot hold at any w, so N ⪯_w C_a at every w. That is an all-world tie, so N = C_a. So the undominated models are exactly the selected models, and all are coherent.

**Closure (AUDIT_completion rules I–IV, with P := {C_a}).**
- Rule I is (IB).
- Rule II has no premise, since every accepted triangle is trivial.
- Rule III: X ⪯_i N at every i forces X = N, by the strong undominatedness of §4.3.
- Rule IV: there are no ties.
- F1 is excluded by strict (G), and F2 by direct (C).

So the extension theorem of AUDIT_completion applies with P equal to the image. ∎

**Consequence for repairs.** Under (H0)–(H5), every rival is dominated, strictly at every world, by some C_a. No explicit repair has to be constructed. A proposed rival can only serve as an adversarial test: if some X is not dominated, one of (H0)–(H5) is false.

---

## 5. Boundary checklist

**5.1 Supports.**
- (H1) asks for λ_a ∈ Δ_{supp a}.
- An edge index a with supp a = {j, k} defends only at j or k. This is how it meets PP12 Lemma 3.1(b)'s rival Λ, which is a strict world-l improvement of every edge model.
- A vertex defends at its own world by guidance.
- The weights are free. λ_a = a is not imposed, and λ_a can jump.
- When λ_{a,l} = 0, the world-l field drops out of (H1) (PP42 Prop 3.6). It remains constrained by (H2)–(H4).

**5.2 Which gates exist, and why.**
- **V_w at world w** is redundant (Lemma 3.1).
- **V_i at worlds j ≠ i.** This gate is needed. Suppose interior realisers b_n → e_i accept rec(C_{a_n}, X) at world j. Then the limit is carried only by V_i's world-j gate, since guidance need not hold. So V_i's world-j field must be the L¹ limit of nearby fields (H4)(b), and it must satisfy (H2)–(H3) at world j with every other member.
- **Edge models.** An edge model must be gated at its support worlds: an ungated non-perfect selected model is not competitive (PP45 Lemma 2.3(b), shell rival). Its off-support gate at world l is needed for compactness, exactly as for V_i.
- I do not claim these gates are necessary for every possible design. They are what makes the realiser family compact, which is what Prop 4.3 uses.

**5.3 Pairs and triples with boundary members.**
- (H2) and (H3) must hold for them, except where e_w appears at world w.
- **Necessity.** The non-strict sandwich is necessary for (TC) for any two members gated at w (REFEREE_round50 §1.2; its proof uses only that the improving member is not w-correct where it improves). (H3) is necessary given (H2) (§4.2).
- **Examples.**
  - (e_i, e_j) at world k is a two-signed pair.
  - (a, e_i) at world i is exempt.
  - (u, e_1, e_2) at world 3 is a three-valued triple (Lemma 1.2(b)), so PP47 Thm 4.1 does not apply to it and Lemma 3.4(i) is the criterion.

**5.4 Compactness and limits.**
- Δ is compact, and every index is gated.
- Prop 4.3 covers fixed-rival limits approaching an edge or a vertex, with the realisers converging anywhere in Δ.

**5.5 The pair-ordering theorem at the boundary.** The audit noted that the logarithmic proof needs positive a and b. The theorem survives in extended reals.

**Proposition 5.2 (boundary pair ordering; PROVED; CHECKED (B): 16,370 exact disagreements over interior, edge and vertex indices, no violation).** Let a, b ∈ Δ. Put r_i := b_i/a_i ∈ [0, ∞], with x/0 := ∞ for x > 0. Let Z := {i : a_i = b_i = 0}. At a disagreement of C_a and C_b, let W and R be the worlds where C_b is worse and better respectively, and put W′ := W ∖ Z and R′ := R ∖ Z. Then W′ and R′ are nonempty, and

  min_{i∈W′} r_i < max_{j∈R′} r_j.

Equivalently, D := log(a/b) ∈ [−∞, ∞] satisfies max_{W′} D > min_{R′} D.

*Proof.*
**Case 1: silence (or −h) becomes h.** Here W = {h_i < 0} and R = {h_i > 0}. C_a does not accept h, so some p ∈ M has Σp_ia_ih_i ≤ 0. C_b accepts h, so Σp_ib_ih_i > 0 for every p ∈ M.
- **R′ is nonempty.** Otherwise Σp b h = Σ_{W′} p_ib_ih_i ≤ 0.
- **W′ is nonempty.** Otherwise a = 0 on R′ as well (from Σp a h ≤ 0 and p > 0), so a = 0 everywhere, which is impossible.
- **The degenerate orders.** If max_{R′} r = ∞ = min_{W′} r, then again a = 0 on R′ ∪ W′ ∪ Z. If min_{W′} r = 0 ≥ max_{R′} r, then b = 0 on R′ and Σp b h ≤ 0.
- **The main case.** Otherwise choose a finite k > 0 with max_{R′} r ≤ k ≤ min_{W′} r. Then b_ih_i ≤ ka_ih_i term by term, so Σp b h ≤ kΣp a h ≤ 0, a contradiction.

**Case 2: h becomes silence.** Here W = {h_i > 0} and R = {h_i < 0}. The same bookkeeping applies with k ∈ [0, ∞) and Σp b h ≥ kΣp a h > 0.
- At k = 0, positivity comes from some b_i > 0 on W′, since p > 0 on M.

**Case 3: opposite answers.** Apply Case 1 to the newly accepted orientation. ∎

**Reading.** At the level of advice geometry, PP45's type test is not blocked by any boundary pair, vertex pairs included. This is a necessary condition for (H1) and (H2), not a construction. Following the audit, the constants are not frozen to a/b.

---

## 6. Necessity, and the exact gaps

| Hypothesis | Necessary in the gate union? | Source |
|---|---|---|
| (H0) | essentially: a gate that rates a nontrivial pure w-improvement ≥ 0 accepts it under (R0), which violates strict (G). So each field must be strictly guiding on every move its gate can be asked to judge | strict (G) |
| (H1) weak own-Bayes | **yes**, for every gated selected member, at a weight in Δ_{supp a} | PP45 Lemma 2.3, PP47 Lemma 1.2 (shell rival) |
| (H2) | the **non-strict** sandwich is necessary for (TC), for every gated pair, boundary pairs included | REFEREE_round50 §1.2 |
| (H3) | necessary for (TC), given (H2) | §4.2 |
| (H4)(a) | weak form forced: the selection must converge to T at T's index | PP47 Cor 2.3 |
| (H4)(b) | not known to be necessary; it is the sufficient condition of Lemma S | OPEN |
| (H5) | definitional for the architecture | — |

**Gap 1 (strictness in (H2)).** Suppose the sandwich holds but the bound κ is attained on non-null parts of both sign regions of φ^a. Then a set D balancing the two parts has ∫_Dφ^a = ∫_Dφ^b = 0. Both directions of C_a → C_a[D ↦ C_b] are then accepted at w: a single-world tie, which the axioms allow.
- If such D can be aligned at every world, the result is an all-world tie with an incoherent model, so F2 (PP47 Thm 2.5).
- So strictness is sufficient but not necessary. The exact condition — no simultaneous zero-balancing set at all three worlds, plus (TC) after the ties are completed — is **OPEN**.

**Gap 2 (positive constants for one-signed pairs).** Lemma 3.2 and undominatedness need only the sandwich with κ ∈ [0, ∞]. Lemma 3.3 uses positive constants, which for one-signed pairs is a bounded-ratio condition. Whether unbounded-ratio one-signed pairs can break (TC) is **OPEN**. It is minor: such pairs never yield an acceptance in the improving direction.

**Gap 3 (necessity of positive κ in Lemma 3.4(i) at three-valued points).** The referee's per-orientation question is open in the same form. Criterion (i) is sufficient. On two-valued triples it is exact (PP47, under (BR)). On three-valued triples, separation gives only κ ≥ 0, κ ≠ 0. **OPEN.**

---

## 7. No global prices

**Definition 7.1.**
- A **global witness at world w** is a measurable U_w : Ω × A → R with an integrable envelope, strictly increasing in r_w a.e., together with constants c_a ∈ (0, c̄] (a ∈ Δ ∖ {e_w}), such that for every such a, a.e. g and every x:
  U_w(g, x) − U_w(g, C_a(g)) ≥ c_a δ^a_w(g; C_a(g) → x).
- An **integrated global witness** requires only this: C_a ⪯_w X implies ∫[U_w(X) − U_w(C_a)] ≥ 0, for every a and every X.
- **Global prices** are constants c_a, one for each member, satisfying every pair inequality c_aφ^a_ab ≤ c_bφ^b_ab and every 3-cycle inequality on D_abc.

**Lemma 7.2 (witness ⟺ prices; PROVED).**
- **(a) A global witness gives global prices.** On D_ab: c_aφ^a_ab ≤ U(C_b) − U(C_a) ≤ c_bφ^b_ab. The 3-cycles follow by telescoping. Every global witness is an integrated one: guidance links have ∫ ≥ 0 because U is increasing, and gate links have ∫ ≥ c_bΦ^b ≥ 0.
- **(b) Prices give an integrated witness.** Assume (H4)(b)–(c). Let Q ⊆ Δ be countable and dense, with prices c on Q bounded by c̄. Assume the **uniform gap (UG)**: there is a measurable γ > 0, with γ ≤ E, such that c_a[f^a_w(g, y) − f^a_w(g, x)] ≥ γ(g) whenever r_w(y) > r_w(x), for all a ∈ Q. Then an integrated global witness exists at w.
  - A sufficient condition for (UG): c is bounded below on Q, and the rank gaps of f^a are bounded below uniformly in a. That holds, for instance, if a ↦ f^a(g, ·) is pointwise continuous on the compact Δ.

*Proof of (b).*
1. **The graph at g.** Gate edges y → x carry W(y, x) := sup{c_bδ^b(y→x) : b ∈ Q, C_b(g) = y}, a countable supremum. Monotone edges carry weight γ/4.
2. **Shortcuts.** By (UG), each gate edge followed by at most three monotone edges is beaten by the gate edge to the endpoint: the loss is at least γ − 3γ/4.
3. **Old-value cycles.** The old-value 2- and 3-cycles are suprema over countably many tuples of price inequalities, so they are ≤ 0 a.e.
4. **The potential.** Longest paths give U, strictly increasing (steps ≥ γ/4), with 0 ≤ U ≤ 3(c̄E + γ). It dominates every gate in Q pointwise.
5. **Gates outside Q.** For b ∉ Q take b_n ∈ Q with b_n → b. On S ∩ {C_{b_n} = C_b} the pointwise inequality for b_n applies. Hence
   ∫_S [U(X) − U(C_b)] ≥ c_{b_n}∫_S δ^{b_n}(C_b → X) − ∫_{{C_{b_n} ≠ C_b}} (2·3(c̄E + γ) + c̄E).
   The second term tends to 0. The first tends to c*Φ^b_w ≥ 0 by (H4)(b), along a subsequence with c_{b_n} → c* ∈ [0, c̄].
6. **Guidance and (e_w, w)** are endorsed because U is increasing. ∎

**Theorem N (no global witness at some world; PROVED modulo FF2 Thm 4.1's import chain).** Assume (H0)–(H5), with (H4)(c). Then at some world w there is no integrated global witness. In particular, at that world there are no global prices satisfying (UG) on any countable dense set.

*Proof.* FF2 Thm 4.1's hypotheses hold for the selection a ↦ C_a:
- (H1) of FF2: the selection is coherent, continuous in measure (Lemma 1.1), competitive on supp a (§4.3), and has T1 = C_u.

If every world had an integrated global witness U_w, then U = (U_1, U_2, U_3) would satisfy FF2's (H2) and (H3), with H_n = Ω. FF2 Cor 4.3 says this is impossible. That corollary was refereed in GG3 as "CORRECT AS STATED", at the status of its import chain: D1, BB2 Thm 6.1 and M3.7–M3.8, each refereed once. ∎

**Corollary 7.3 (global witnesses would make every C_a Bayes for one field; PROVED).** Suppose global witnesses (U_w, c_{·,w}) exist at all three worlds. For a non-vertex index put μ_a ∝ (λ_{a,w}/c_{a,w})_w; then μ_a ∈ Δ_{supp a}. Pointwise,

  Σ_w μ_{a,w}[U_w(x) − U_w(C_a)] ≥ (normalisation)·Σ_w λ_{a,w}δ^a_w(C_a → x) ≥ 0.

So C_a is a pointwise μ_a-Bayes model of the single field U, and an a.e.-unique one when (H1) holds strictly. The vertex models are trivially U-Bayes at e_i. So a ↦ C_a would be a coherent, competitive selection, continuous in measure, of Bayes models of **one** strictly guiding integrable field, through T1.
- FF2 Thm 4.1 excludes this on the full domain, for every such field.
- Contamination Triangle Thm `main` / Cor `coverage` exclude it for non-adjacent fields (refereed twice).
- REFEREE_PP32 §4.3 Prop B excludes it for regular abstention fields. ∎

**Corollary 7.4 (any solution lacks global prices).** Every solution of the field-design problem (H0)–(H5) must, at some world, use the **triple-locality** of (H3). Prices consistent on every triple must fail to be consistent on some larger family, or fail (UG).
- This is the audit's target pattern: x_B − x_A, x_C − x_B, x_D − x_C, x_A − x_D ∈ [1, 2], with the diagonals in [−4, 4].
- Every triple is feasible with slack (for example 0, 1.5, 3 along two consecutive cycle edges). The four together are not, since summing the cycle gives 0 ≥ 4.
- Theorem A uses only triples, so it is compatible with this pattern. Theorem N says that some such pattern **must** occur in any solution. PP42 Prop 3.5(c) and REFEREE Prop R2 give finite and continuum instances.

---

## 8. What is open

1. **The field-design problem itself (OPEN).** Do fields satisfying (H0)–(H5) exist on the whole simplex for the posterior family?
   - Theorem A reduces coverage of T1 to this problem.
   - Theorem N says any solution has no global prices at some world.
   - PP46 Thm D (the star) satisfies (H0)–(H3), with (H4)(b) on its own compact index set. So the architecture is consistent locally. That design, however, is globally witnessed.
2. **Gaps 1–3 of §6**: the exact strictness needed, one-signed pairs, and positive κ at three-valued points.
3. **(H4)(b)** is sufficient for sections. Whether discontinuous fields can still give closed sections is OPEN.
4. **Weak witnesses.** Theorem N needs a strictly guiding witness, which (UG) supplies. Whether a global witness that is only weakly guiding is also excluded is OPEN: FF2's Step 4 and its import chain use strictness.
5. **FF2's import chain** limits Theorem N's status. Theorem A does not depend on it.

---

## 9. Scripts

`r9/PP49_py/posterior_checks.py`. Run `python3 -I -B posterior_checks.py > posterior_checks.out` inside the folder. It uses Fractions only, and the output ends ALL PASS.
- **(A1)** The three-valued triple at ε = 3/10, with strict margins.
- **(A2)** 3,000 overlapping nearby pairs: no opposite answers.
- **(B)** Prop 5.2 on 16,370 disagreements between interior, edge and vertex indices: both W′ and R′ nonempty, and the extended-real inequality holds in every case.

**Most important next step.** Attack the four-posterior-model checkpoint (the audit's second deliverable) with the criteria of this note, at the world where Theorem N says prices must fail:
- the pair conditions (H2) and the per-orientation triple criterion of Lemma 3.4(i);
- triples containing a far member, which can be three-valued (Lemma 1.2(b));
- the target: triple-consistent but globally inconsistent constants.
