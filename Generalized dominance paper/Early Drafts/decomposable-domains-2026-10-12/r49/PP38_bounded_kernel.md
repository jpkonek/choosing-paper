# PP38. The bounded kernel: what it must do, a field that does it, and where the rest goes

22 October 2026. Task PP38 of Brief 49 (attack the kernel from a different angle). One reader (me); not refereed.

**Labels.** PROVED: complete argument here (or a cited refereed result, named). CHECKED: exact rational computation in `PP38_py/coherence_exact.py` (ALL PASS). NUMERICS: Gaussian Monte Carlo in `PP38_py/budget_mc.py`, `second_gen_mc.py`, `jump_gap_mc.py`; no proof depends on them. CONJECTURE / OPEN: as stated.

**Inputs.** Brief 49; AUDIT_round49_brief and AUDIT_round49_answers (binding); PP33 (Thm 3.1, Thm 5.1, Prop 8.2); PP34 (Lemma 2.1, (CC), Prop 5.2); PP36 (Prop K, Lemma E, Prop SD); PP30 (Thm 3.1); PP32 (Lemmas 2.1–2.3) and REFEREE_PP32_penalties (the field ℓ^T, Thm A, Cor A′); PP23, PP25 (Thm A, Thm B, Lemma 5); PP26 (Thms V, M, R); PP2 Thm 6; PP28 Lemma 6.2; AUDIT_completion (rules I–IV, F1/F2); AUDIT_selected_realizability §4; REFEREE_Z_PP19 (Lemma H); LEAD_selection_count (Lemmas A, B, E); REFEREE_round46 (R46.1); and the coordinator's relay of REFEREE_round48 (items (1)–(3), used in §2.4, §2.3 and §6). Only Brief 49's axioms are used; extra hypotheses are named where they enter.

---

## 0. Verdict

**The bounded kernel is not where the difficulty lives.** A single non-rank-linear field, used as a potential on bounded records only, meets every constraint that the axioms force on bounded records, for T, the vertex models, a complete edge selection, any path models, and any later defender that is Bayes for the field. It leaves room for dominations at all three worlds, and it passes every screen the brief lists. Its allocation of defence worlds is a fixed function of the record. So it survives closure and any growth of the registered family, for free.

The price is geometry, not verdicts. The field decides which coherent models can be registered: exactly its coherent Bayes models. For the field ℓ^T of REFEREE_PP32_penalties these are T, three one-parameter families of imprecise edge segments, and the vertices (PROVED). Precise non-vertex models cannot be registered under ℓ^T, and no potential kernel of any field can register a precise edge model in the band together with T. That second statement is PP35 Cor A′, now read as a statement about kernels.

What the kernel cannot do is then located exactly. It sits in the unbounded layer, at three named families of records. There the relation must accept unbounded records that the kernel's own field rejects:
- T's small fills;
- the post-jump defences on the path out of T's fibre;
- the forced rivals of edge models.

These are statements about the kernel's own field. I do not claim that the unbounded layer must be non-additive for every field (REFEREE_round48 item (3)).

| Question | Answer | Where | Label |
|---|---|---|---|
| Q1. Forced acceptances and refusals | A record-level list in three locations: inside Sil(T), at the seams, and in the edge models' own classes. One new screen: **no world may make a cone subordinate** (dual of PP26 Thm V and PP28 Lemma 6.2). | Thm 2.1, Thm 2.2, Lemma 2.3, Ex. 2.4 | PROVED |
| Q1, for potential kernels | Every item of Thm 2.1 reduces to one condition: **each registered model is Bayes for the field at a weight in its support**. (CC) then holds at every order; completion adds nothing. | Thm 3.1, Cor 3.2 | PROVED |
| Precise edge models | No potential kernel of any field registers a precise edge model with threshold in J together with T (Cor A′). Under ℓ^T no precise non-vertex model is registrable at all. | Cor 3.3, Cor 4.3 | PROVED |
| Q2. A rule with room | The ℓ^T potential on bounded records. Bounded room: T strictly dominates its mixed departures. Unbounded room: first-generation vertex rivals on PP30's balls are dominated by edge-segment models with **positive ℓ-value at all three worlds**. | §4, Prop 4.4 | PROVED; room at first generation NUMERICS |
| Tests | Departure–retreat pump, Thm V, Thm M, Thm R, PP2 Thm 6, R46.1, PP32/PP35 Thm A, Cor A′, Thm 2.2, Lemma 6.2: all passed. | Prop 4.5 | PROVED |
| Q3. Growing family, allocation after closure | Kernel + guidance + any set of **strictly ℓ-positive** unbounded acceptances is a closed system: (G), (IB), (TC), registered models undominated, closure inert, and Prop K never fires. So the recursion is free on that fragment. | Thm 5.1, Prop 5.3 | PROVED |
| Where it stops | (a) The selection must jump in measure at T's fibre. Post-jump models must defend against T[E ↦ A] at their edge's third world, by a record ℓ rejects. (b) Small fills of T: every registered dominator is ℓ-negative at some world. (c) A forced rival of the midpoint edge model has no ℓ-endorsed registered dominator. | Thm 6.2, 6.3, 6.5, Prop 6.6 | (a) PROVED + one NUMERICS hypothesis; (b) PROVED; (c) PROVED except one in-family inequality (NUMERICS) |
| Interface for the rest | Installed ℓ-negative records must be compensated at the worlds where they are ℓ-negative, and have no far inverses. Then no triangle with a bounded edge fails. | Prop 5.2 | PROVED |

**Is the kernel impossible?** No. The bounded kernel exists. The impossibilities found are of three kinds:
- chosen designs: balanced rules, rank-linear and (H4) fields, regional lexicographic rules, the exact largest-loss rule;
- one optional commitment: a single-field kernel together with precise in-band edge models;
- consequences of axioms plus the kernel choice: §6's three residues.

The classification is in §7.

---

## 1. Setting and the obligation form

Brief 49's setting:
- three worlds; problems g ∈ R³ modulo sign; Gaussian μ; the full four-advice domain; models modulo null sets;
- ranks correct 0 < silent 1 < wrong 2 < contradictory 3;
- classes M_1, M_2, M_3 (M_k: world k is the minority world) and U;
- on M_k, A is the majority answer and B the minority answer;
- T = T1 = D_M with M = c·1 + εΔ; Sil(T) is T's silent cone; θ_ij = |g_j|/|g_i| on W_ij := M_i ∪ M_j;
- the band J = (α, β) with α = c/(c+ε), β = (c+ε)/c (PP32 Lemma 1.1).

**Records and obligations.** A record r = (D, a → b) is bounded if D is essentially bounded. A(r) is the set of worlds accepting r. For a registered model N with assigned support s(N), the support-defence part of competitiveness is (AUDIT_selected_realizability §4):

  **(Ob)** A(r) ∩ s(N) ≠ ∅ for every record r whose old side N realises (N = a a.e. on D).

Against bounded rivals, (Ob) concerns bounded records only. This is the job of the bounded kernel. Vertex models have s = {j} and are j-perfect, so their (Ob) is guidance. Interior-index models (T, path models, any defender at an interior index) have s = {1, 2, 3}. Edge models on [e_1, e_2] have s = {1, 2}.

**Forced refusals.** By PP23 Lemma 1.1, strict (G) and (TC) hold at world i iff:
- (P1) no two accepted records compose to a nontrivial pure i-improvement;
- (P2) every accepted triangle has its reverses.

---

## 2. Q1: what every bounded rule must do

### 2.1 The list

**Theorem 2.1 (forced acceptances and refusals; PROVED).** Use (IB), strict (G) and (TC). Register T, V_1, V_2, V_3, a complete edge selection on [e_1, e_2], and path models, all universally competitive on their supports. Require explicit dominators for the vertex rivals. Then every bounded-record rule satisfies the following.

*(A) Inside Sil(T).*
- **A1 (forced acceptance, set-valued).** Every bounded departure d = (H, S → a) with H ⊆ Sil(T) and a regular is accepted at some world of its loss set L(d) = {i : a is i-wrong on a non-null part of H}. It is never forced to one specified non-guidance world by T alone: any nonempty choice inside L(d) is (TC)-consistent (PP34 Prop 2.3, with REFEREE_round48's repair that rivals with contradictions are excluded).
- **A2 (padded-undo refusal).** If d is accepted at i, then every record (O, a → b) is refused at i, in every context, whenever:
  - Wr_i(a) ⊆ O ⊆ H;
  - b ∈ {S, i-correct} on O;
  - the record is nontrivial;
  - (H ∖ O) ∪ {b ≠ S} is non-null.

  (PP34 Lemma 2.1.) PP30 Thm 3.1(b) is the case O = H: N ⋠_w N[G ↦ S, E ↦ w-correct] for every model N with N = a on G.
- **A3 (vertex-world refusal).** If C dominates a vertex rival Z = V_j[G ↦ S, E ↦ w-correct], then world j refuses every bounded record Z → V_j[H ↦ C], for every bounded H ⊆ {C ≠ V_j} (PP33 Thm 3.1: V_j is j-perfect, so C has no j-compensation). The same holds for any member N and any dominator C without v-compensation relative to N (PP25 Lemma 5).

*(B) At the seams.* Let N be a registered edge model on [e_1, e_2], and O ⊆ Sil(T) bounded with N = a on O. For i ∈ {1, 2}, an *i-padding* is a non-null bounded F ⊆ Sil(T) ∖ O with advice c that is i-correct on F.
- **B1 (seam blocking).** If T's departure (O ∪ F, S → a ⊕ c) is accepted at i for some i-padding, then N's retreat (O, a → S) is refused at i. (This is A2 with H = O ∪ F and Wr_i(a ⊕ c) = Wr_i(a) ⊆ O.)
- **B2 (coordination (CC)).** For every such O, the following two cannot both hold:
  - some 1-padded departure is accepted at 1;
  - some 2-padded departure is accepted at 2.
- **B3 (forced single-world acceptance).** If one of them holds, say at i, then N's retreat (O, a → S) is accepted at the other edge world.
- **B4 (the seam selector).** Suppose N's window [τ_0, τ_1] lies inside J. Take O = O_1 ∪ O_2 with O_1 ⊆ Sil(T) ∩ M_1 ∩ {θ_12 > τ_1} (N = A) and O_2 ⊆ Sil(T) ∩ M_2 ∩ {θ_12 < τ_0} (N = A). Both are non-null (PP32 Lemma 1.1). Every M_3-padding F ⊆ Sil(T) ∩ M_3 with A is both a 1-padding and a 2-padding. So there is σ_N(O) ∈ {1, 2} such that every departure (O ∪ F, S → A) with F ⊆ Sil(T) ∩ M_3 is accepted at world 3 or at σ_N(O), and never at the other edge world.

*(C) In the edge models' own classes.*
- **C1.** On M_3 every record out of an edge model is a weak worsening at 1 and at 2, so it is guidance (Lemma 2.3).
- **C2.** On W_12 = M_1 ∪ M_2, worlds 1 and 2 have exactly opposite rank changes for regular advice (Lemma 2.3). Hence a record out of an edge model is non-guidance at both edge worlds iff its W_12-part has a 1-gain and a 2-gain. Call such a record *two-sided*. Its two gains may lie in one class, because an edge model can give both answers on a one-class piece of Sil(T); this is REFEREE_round48's correction of PP34 Prop 4.1(f). Only two-sided records carry edge obligations: each must be accepted at 1 or at 2.
- **C3 (edge covering).** Every point of [e_1, e_2] lies in the credal set of some selected edge model (PP32 Lemma 2.2). So B4 binds unless every selected window reaches an end of J.

*(D) Vertices and path models.*
- **D1.** Vertex models add only guidance.
- **D2.** Interior path models need A(r) ≠ ∅ for every bounded record out of them. Any bounded record out of a regular model has a loss at some world, so this is never contradicted by strict (G) alone.

*Proof.* Each item was proved where cited. The new parts are the bookkeeping in B1–B4 and C1–C2.
- B3 is (Ob) with s(N) = {1, 2}.
- B4: the departure has loss worlds {1, 2, 3}: A is 1-wrong on O_1, 2-wrong on O_2 and 3-wrong on F. It is accepted at some world. If it is accepted at an edge world, B2 fixes which one across all M_3-paddings.
- C1 and C2 are Lemma 2.3. ∎

**Lemma 2.3 (own-class identities; PROVED; CHECKED (d)).** On M_1 and on M_2, r_1 + r_2 = 2 for A, S and B. So δ_1 = −δ_2 pointwise for records between regular models supported in W_12. On M_3, A is correct at worlds 1 and 2, so every change away from A is a weak worsening at both.

*Proof.* On M_1 the ranks (r_1, r_2, r_3) are A (2, 0, 0), S (1, 1, 1), B (0, 2, 2). On M_2 they are A (0, 2, 0), S (1, 1, 1), B (2, 0, 2). ∎

### 2.2 A new screen: no subordinate cones

Call world j **R-subordinate**, for a measurable cone R, if it accepts every bounded record whose restriction to R^c is a nontrivial weak j-worsening, whatever happens on R. A lexicographic rule whose leading level is a strictly guiding functional of the R^c-part is R-subordinate.

**Theorem 2.2 (no subordinate cone; PROVED).** Use reflexivity, strict (G), (IB), (TC), T competitive, and coherent dominators for the vertex rivals of V_j. Let R be a cone such that:
- (a) R ∩ Sil(T) is non-null;
- (b) R misses the corner of M_j: for every δ > 0, R^c ∩ M_j contains a non-null set of problems whose M_j-line has its e_j-triangle inside the δ-ball around e_j.

Then world j is not R-subordinate. (b) holds for every R ⊆ Sil(T), and for every R ⊆ M_i ∪ M_k.

*Proof.*
1. **The rival.** Take a bounded non-null G ⊆ R ∩ Sil(T). T accepts (G, S → V_j) at some w; w ≠ j, since the record is a pure j-improvement. Put Z := V_j[G ↦ S, E ↦ w-correct] with E = G.
2. **Its dominator.** Let C be its coherent dominator. C ≠ V_j, because V_j ⋠_w Z (PP30 Thm 3.1(b)). So Q := {C ≠ V_j} is a non-null cone (Lemma H).
3. **The refused records.** C has no j-compensation, so by PP33 Thm 3.1, Z ⋠_j V_j[H ↦ C] for every bounded H ⊆ Q.
4. **Q lies in R.** Suppose Q ∖ R is non-null, and take a bounded non-null H ⊆ Q ∖ R. The record rec(Z, V_j[H ↦ C]) is bounded. Its R^c-part is (H, V_j → C), because G ⊆ R; this is a nontrivial weak j-worsening. R-subordination accepts it at j, a contradiction. So Q ⊆ R, that is, C = V_j a.e. on R^c.
5. **C is V_j.** By (b), C = D_K says B on a non-null set of lines whose e_j-triangles shrink to e_j. D_K says B on a line only if K lies strictly inside its e_j-triangle. So K = {e_j} and C = V_j, a contradiction.

For R ⊆ Sil(T), the lines with small e_j-triangles miss M, so they lie in Ans(T). ∎

**What it excludes.**
- PP32 §6.3's OPEN case (a lexicographic stack whose leading level is blind on a region), whenever the blind region meets Sil(T) and misses the corner.
- Every "Ans(T)-first" lexicographic rule (R = Sil(T)), at every world.
- Any rule that uses Sil(T)-records only as tie-breaks.

PP26 Thm V and PP28 Lemma 6.2 exclude the opposite extreme, a dominant region. Together they say that every world must trade cones against their complements at bounded rates in both directions. A potential does this; a gate or a regional lexicographic rule does not.

### 2.3 What is not forced

- The departure verdicts themselves are free (A1).
- Single-world ties are free.
- Which world a two-sided edge record uses is free, subject to B2–B4.

Nothing in Theorem 2.1 forces non-additivity unless the edge selection contains a window strictly inside J (C3 with B4); see Cor 3.3.

### 2.4 Test case from REFEREE_round48: C = D_λ, λ = (1/2, 1/2, 0)

C is precise, with threshold θ_12 = 1 ∈ J.
- **The balls.** C gives B (1-correct) on G_1 ⊆ Sil(T) ∩ M_1 ∩ {θ_12 < 1}, and B (2-correct) on G_2 ⊆ Sil(T) ∩ M_2 ∩ {θ_12 > 1}. Both sets are non-null near the seam rays.
- **T's departures.** (G_1, S → B) is a pure worsening at 2 and at 3, so it is accepted there by guidance. Symmetrically, (G_2, S → B) is accepted at 1 and at 3.
- **The rivals.** Z_1 := C[G_1 ↦ S, E_1 ↦ 2-correct] is a pure 2-improvement of C. Strict (G) refuses C ⪯_2 Z_1, and guidance accepts C ⪯_1 Z_1. Symmetrically, Z_2 := C[G_2 ↦ S, E_2 ↦ 1-correct] gives C ⋠_1 Z_2 and C ⪯_2 Z_2.
- **Forced at the dominator level (Prop K).** Let N_1 and N_2 be dominators of Z_1 and Z_2. Then C ⋠_2 N_1 and C ⋠_1 N_2. So competitiveness on {1, 2} forces C ⪯_1 N_1 and C ⪯_2 N_2, and **N_1 ≠ N_2**.
- **At the seam.** C's window is the single point 1 ∈ J, so B4 binds with σ_C.
- **Under any potential kernel** C cannot be registered together with T (Cor 3.3).

---

## 3. Potential kernels

Let ℓ be a **strictly guiding integrable field**: per problem and world, penalties 0 < α_w (silent − correct), β_w (wrong − silent), γ_w (contradiction − wrong), positive a.e., with an integrable envelope. Put L_w(X) := ∫ ℓ_w(g, X(g)) dμ, and for a record r put Φ_w(r) := L_w(new) − L_w(old), which is finite for every record.

**The kernel K_ℓ.** A bounded record r is accepted at w iff Φ_w(r) ≥ 0. Unbounded records are not decided by the kernel; at this stage only guidance is accepted among them.

**Theorem 3.1 (potential kernels; PROVED).**
- (i) K_ℓ plus guidance satisfies reflexivity, strict (G), (IB) and (TC) on bounded records. Single-world ties occur exactly on Φ_w = 0.
- (ii) A model N is competitive against every bounded rival at worlds in s iff N is pointwise λ-Bayes for ℓ for some λ ∈ Δ_s, that is, N(g) minimises Σ_w λ_w ℓ_w(g, ·) a.e.
- (iii) Suppose every registered model is the a.e.-unique λ_N-Bayes model for its λ_N. Then rules III and IV of AUDIT_completion add nothing to bounded records. The allocation A(r) = {w : Φ_w(r) ≥ 0} is a function of the record alone. It is independent of the registered family and unchanged by closure.

*Proof.*
- (i) Φ_w is additive under composition of copies, so each world is a total preorder on bounded-equivalence classes. Around an accepted triangle the values sum to 0 and are each ≥ 0, so each is 0, and the reverses are accepted. A nontrivial pure w-improvement has Φ_w < 0, since the penalties are strictly positive.
- (ii) ⇐: Σ_w λ_w Φ_w(r) = ∫ Σ_w λ_w (ℓ_w(new) − ℓ_w(old)) dμ ≥ 0, so some w ∈ supp λ has Φ_w(r) ≥ 0.
  ⇒: Apply PP32 Lemma 2.3 on the balls B_n. It needs only integrability, and holds for any field (REFEREE_PP32_penalties). It gives a nonempty closed set Λ_n ⊆ Δ_s of weights for which N is Bayes on B_n. The Λ_n decrease, so some λ lies in all of them.
- (iii) Let X be a bounded perturbation of a registered N with Φ_w(rec(X, N)) ≥ 0 at every w. Then Σ λ_{N,w} Φ_w(rec(X, N)) ≥ 0. Uniqueness gives Σ λ_{N,w} Φ_w(rec(N, X)) > 0 unless X = N, a contradiction. So rule III has no bounded premise. Rule IV needs Φ_w = 0 at all w, which gives X = N in the same way. ∎

**Corollary 3.2 (Theorem 2.1 under potentials; PROVED).** If every registered model is Bayes at a weight in its support, every item of Theorem 2.1 holds at once:
- A1 holds because T is Bayes.
- A2, B1 and B2 are (TC) consequences, and (i) gives (TC).
- B3 and the edge obligations hold by (ii).
- A3 becomes a budget: for every bounded H ⊆ {C ≠ V_j}, Φ_j(rec(Z, V_j[H ↦ C])) < 0. This holds if L_j(C) < L_j(Z) (PP33 Cor 3.2 with ℓ in place of L).

In particular, (CC) holds **at every order**, including triangle completions. The audit's worry about PP34's largest-loss rule (completion acceptances that break the blocking bound) cannot arise: K_ℓ is already closed. This also bypasses REFEREE_round48's finding that the exact largest-loss rule fails on cells.

**Corollary 3.3 (precise edge models; PROVED).** Under any potential kernel, at any ℓ, no edge model whose window lies strictly inside J can be registered together with T. Every accepted bounded comparison out of T and out of the edge models is ℓ-endorsed (Φ ≥ 0), so PP35 Cor A′ applies. In particular C = D_{(1/2,1/2,0)} of §2.4 is excluded.

This is an **optional-commitment** obstruction (single field) combined with a **chosen geometry** (precise in-band edge models). A rule that registers precise in-band edge models must satisfy B4 with a σ_N that no field endorses. I give no such rule (OPEN).

**Proposition 3.4 (room; PROVED).**
- **Balanced fields have no room.** Call ℓ balanced if, for some λ ∈ int Δ, the sum Σ_w λ_w ℓ_w(g, a) does not depend on the regular advice a on mixed g (PP23's Ω and PP25's L, with λ = u). Then no bounded record between regular models is accepted at all three worlds with a refused reverse: the λ-combination of its Φ-values is 0.
- **Non-balanced fields have room.** If T is the unique λ_T-Bayes model, bounded rivals Y of T with Φ_w(rec(T, Y)) ≥ 0 at all three worlds exist as soon as the field is not balanced on Sil(T). Prop 4.4 gives an explicit one.

*Proof.* The first part is the balance computation of PP23 Prop 3.2, with λ in place of u. The second is Prop 4.4. ∎

---

## 4. The ℓ^T kernel

**The field** (REFEREE_PP32_penalties §3.2). Put L := β = (c+ε)/c and d := 1/(1+L). Define

  F(θ) = θ/(2d) on (0, d];  1/2 + L(θ − d)/(2d) on [d, 1/L];  Lθ on [1/L, ∞),  and G(s) := 1/F(1/s).

On M_k, with s_j = |g_j|/|g_k|:
- α_k = β_k = γ_k = |g_k|;
- for j ≠ k: α_j = |g_k| G(s_j), β_j = |g_k| F(s_j) and γ_j = |g_j|.

On U, α = β = γ = |g_w|. The field is strictly guiding and integrable. It is non-adjacent (G < F), so it is an abstention field, and it is not rank-linear.

**Lemma 4.1 (PROVED in REFEREE_PP32_penalties §3.2; re-CHECKED (a), (b)).**
- T is the a.e.-unique u-Bayes model.
- At the edge weight (t/(1+t), 1/(1+t), 0), the a.e.-unique Bayes model is B_12(t) := D_{K(t)}, where K(t) ⊆ [e_1, e_2] is the segment with θ_12-thresholds F⁻¹(t) < G⁻¹(t). It is never precise.
- The same holds on the other edges (B_13, B_23) by symmetry. At e_k the Bayes model is V_k.

**Lemma 4.2 (coherence lemma; PROVED; CHECKED (c) at all 90 interior grid weights of denominator 15 other than u, for ε ∈ {1/10, 3/10, 1/2, 9/10}).** For every interior λ ≠ u, every λ-Bayes model of ℓ^T is incoherent.

*Proof.*
1. **Setup.** Let i be a world with λ_i maximal, j one with λ_j minimal (so λ_j < λ_i), and k the third world. On M_i write g = (g_i, g_j, g_k) = (1, −s_j, −s_k) with s > 0. The chart is affine, so cones correspond to subsets of the (s_j, s_k)-quadrant.
2. **What coherence requires.** For any D_K, the set where it accepts g (the minority answer B) is {m_j s_j + m_k s_k < m_i for all m ∈ K}, which is convex. The set where it accepts −g (the answer A) is {m_j s_j + m_k s_k > m_i for all m ∈ K}, also convex.
3. **The Bayes regions.** Up to null sets (tie curves), the Bayes model's B-region is {λ_j F(s_j) + λ_k F(s_k) < λ_i} = {s_k < b(s_j)}, with b(s) := F⁻¹(y(s)) and y(s) := (λ_i − λ_j F(s))/λ_k. Its A-region is {λ_j G(s_j) + λ_k G(s_k) > λ_i} = {s_k > a(s_j)}, with a(s) := G⁻¹(z(s)) and z(s) := (λ_i − λ_j G(s))/λ_k. These follow from the costs: B costs λ_j(α_j + β_j) + λ_k(α_k + β_k), S costs Σ λ_w α_w, and A costs 2λ_i.
4. **The kinks of F.** F is convex on [0, 1/L], with slopes 1/(2d) < L/(2d). It has a concave kink at 1/L, where the slope drops from L/(2d) to L (because 2d < 1). F⁻¹ has slopes 2d, 2d/L, 1/L: a concave kink at 1/2 and a convex kink at 1.
5. **Case y_0 := y(1/L) = (λ_i − λ_j)/λ_k ≠ 1/2.** The point s_j = 1/L is in the domain, since F(1/L) = 1 < λ_i/λ_j, and b(1/L) > 0. The function y has a convex kink at 1/L.
   - If y_0 is not a kink of F⁻¹, then b = F⁻¹∘y has a convex kink there.
   - If y_0 = 1, the one-sided slopes are b′(1/L−) = −λ_j/(2dλ_k) and b′(1/L+) = −2dλ_j/λ_k. Since 4d² < 1, b′(1/L−) < b′(1/L+), so the kink is again convex.

   In both cases b is not concave near 1/L. So the open hypograph {s_k < b(s_j)} is not convex.
6. **Case y_0 = 1/2.** Use the A-region at s_j = L, where G(L) = 1 < λ_i/λ_j and z(L) = y_0 = 1/2. G has a convex kink at L: its slope rises from 1/L to 1/(2dL). So z has a concave kink there. G⁻¹(z) = Lz is linear near z = 1/2. So a has a concave kink at L, and the epigraph {s_k > a(s_j)} is not convex.
7. **From a non-convex region to incoherence.** There are two points of the region whose midpoint lies outside it, all three with strict margins. Take small balls B_1, B_2 around the two points. Suppose a convex set contains a.e. point of B_1 ∪ B_2. Then it contains every point of the ball of midpoints, because for each such point q the set of p ∈ B_1 with p and 2q − p both inside has positive measure. But the Bayes model gives a different answer on the midpoint ball. So it agrees a.e. with no D_K. ∎

**Corollary 4.3 (the registered geometry; PROVED).** Under the ℓ^T kernel the registrable models are exactly:
- T (interior indices);
- B_ij(t) for any edge {i, j} and t ∈ (0, ∞): at interior indices, and at indices on their own edge;
- V_k.

So no precise non-vertex model can be registered under ℓ^T: neither PP33's rays, nor the precise edge models of PP30's Ans(T)-kept geometry. The complete edge selection is q ↦ B_12(q_1/q_2), which is continuous in measure, with C_{e_k} = V_k.

*Proof.* Thm 3.1(ii), Lemmas 4.1 and 4.2, and uniqueness at u and at boundary weights. ∎

**Proposition 4.4 (room; PROVED; CHECKED (e); NUMERICS).**
- **(a) Bounded room.** Let E, E′ ⊆ Sil(T) ∩ M_1 be small balls around nearby points. The record T → T[E ↦ B, E′ ↦ A] has, per unit mass:
  - −α_1 on E and +β_1 on E′ at world 1;
  - +β_j on E and −α_j on E′ at worlds j = 2, 3.

  Here α_1 = β_1 = |g_1| and β_j − α_j = |g_1|(F − G)(s_j) > 0. Choose μ(E) slightly smaller than μ(E′), with ∫_E |g_1| < ∫_{E′} |g_1|. Then all three values are positive, so T strictly dominates this incoherent rival. CHECKED: values (0.01, 0.817, 0.826) on two atoms.
- **(b) Unbounded room at the first generation (NUMERICS, `budget_mc.out`).** Take PP30's balls for V_1 (ε = 3/10, radius 0.05).
  - T's departure (G, S → V_1) has Φ = (−3, +8, +8)·10⁻⁶, so it is accepted at worlds 2 and 3.
  - For both Z_2 and Z_3, the edge-segment models B_12(t) and B_13(t) with t ≥ 480 satisfy the budget at world 1: ΔL_1(C) ≈ 4·10⁻⁶ < 8.9·10⁻⁶.
  - They are compensated at worlds 2 and 3: they are strictly better there on masses ≈ 1.5·10⁻³ and 7.6·10⁻⁴.
  - **rec(C, Z) has positive ℓ-value at all three worlds**, for example (+5·10⁻⁶, +3.5·10⁻³, +9.1·10⁻⁴).

  So the kernel's own field dominates these rivals, and no shadow analysis is needed (Thm 5.1). The mechanism is the vertex geometry: near e_1 the world-1 cost of the wedge is second order in its angle, while the gains at worlds 2 and 3 are first order. This is PP34's "infinitesimal wedge" observation in additive form.

**Proposition 4.5 (the brief's screens; PROVED).**

| Screen | Outcome for K_{ℓ^T} |
|---|---|
| Departure–retreat pump (PP25 Lemma 3) | Impossible: a potential never composes two accepted records into a pure improvement. |
| PP26 Thm V (no veto region) and Thm M (mass-blind) | No veto: every regional improvement is outweighed by enough loss elsewhere. Verdicts are mass-sensitive. |
| PP26 Thm R (linear region-constant weights collapse to additive endorsement) | Not in class R_w: the weights depend on the ratios s_j, not on the region. Its conclusion (endorsement) holds trivially, so it is not an obstruction to an additive kernel. |
| PP2 Thm 6 (fixed-key gates) | Hypothesis (H2) fails: no world uses a gate. |
| R46.1 (balanced rules fail at the edges) | ℓ^T is not balanced, and the edge selection is not vertex-valued. |
| PP32 Thm 3.1 (rank-linear), PP35 Thm A ((H4) fields) | ℓ^T is neither. (H4) fails on the edge-silent windows. |
| PP35 Cor A′ (every field) | Met: the windows reach the band ends, with equality at t = 1. |
| Thm 2.2 here, PP28 Lemma 6.2 | No subordinate and no dominant cone: the field is positive everywhere. |
| PP30 Thm 3.1 (forced silence-defences) | Automatic: N[G ↦ S] ⪯_w N at every w with Φ_w(G, S → N) ≥ 0, and T's Bayes property supplies one such w. |

---

## 5. Q3: growing families and allocations after closure

**Theorem 5.1 (the ℓ-positive fragment is closed; PROVED).** Take any family 𝒫 of registered models, each an a.e.-unique ℓ-Bayes model at a weight in its support. At each world w, let the relation consist of:
- weak guidance;
- the kernel K_ℓ on bounded records;
- any set 𝒢_w of unbounded records with **Φ_w > 0**, together with all their copies.

Then:
1. reflexivity, strict (G), (IB) and (TC) hold;
2. every member of 𝒫 is competitive against every bounded rival on its support, and is undominated;
3. no two distinct members are tied at all worlds;
4. rules I–IV of AUDIT_completion add nothing, and F1 and F2 do not occur;
5. Prop K (PP36) never removes a defence world.

*Proof.*
- 1: every accepted record has Φ_w ≥ 0, with Φ_w = 0 only for bounded kernel records (whose reverses are then accepted) or for trivial guidance. An accepted triangle has Φ_w-values summing to 0, so all its links are Φ_w = 0 kernel records and their reverses are accepted. Strict (G) and (IB) are as in Thm 3.1.
- 2: competitiveness is Thm 3.1(ii). If C ⪯_w N at all w, then Φ_w(rec(C, N)) ≥ 0 for all w, so Σ λ_{N,w} Φ_w(rec(C, N)) ≥ 0. Uniqueness gives C = N.
- 3: as in 2.
- 4: II is 1; III and IV are 2 and 3. F1 would be an accepted record with Φ < 0, and none exists.
- 5: Prop K needs N ⪯_i Z, Z ≺_i D and D ⪯_i N. In the fragment the first and third have Φ_i ≥ 0, so Φ_i(rec(D, Z)) ≥ 0. But Z is pointwise strictly i-better than D, so Φ_i(rec(D, Z)) < 0. ∎

So, on the fragment, the audit's allocation requirement is met in the strongest form. Each defence world is a fixed function of the record. It holds simultaneously for every registered model, and it holds after closure, for every number of generations. The question for Q3 is therefore not the allocation but the **supply**: does every repair-class rival have an ℓ-positive registered dominator? §6 answers no, for three families.

**Proposition 5.2 (interface for records the field rejects; PROVED).** Add to the fragment unbounded records r installed at worlds where Φ_v(r) < 0. Suppose:
- (B1) every such r is compensated at those worlds (its far part is not a weak v-improvement);
- (B2) no two installed records have mutually inverse far parts.

Then no accepted triangle with exactly one bounded edge fails (TC).

*Proof.* Use PP25 Thm B with the triangle lemma. In the case (guidance, installed r), r's far part is a weak improvement, which contradicts (B1) if Φ_v(r) < 0. It contradicts strict positivity if Φ_v(r) > 0: the three Φ_v-values would then sum to more than 0, as in PP33 Thm 5.1, item 2. ∎

Triangles with three unbounded edges remain the unbounded layer's problem: shadows, PP25 Lemma 6.

**Proposition 5.3 (where Prop K can bite; PROVED).** For registered D and N, the worlds Prop K removes are contained in

  {i : N serves some installed Z with Φ_i(rec(N, Z)) < 0}.

(Proof: Thm 5.1(5).) This refines PP36's pair-dependent defence worlds: only the installed records that the field rejects create pair-dependent constraints. It is consistent with REFEREE_round48's counterexample to PP36's "one answerer per dominator is Prop K-safe", because that construction uses non-field acceptances.

---

## 6. Where the residue goes

Fix the ℓ^T kernel (ε ∈ (0, 1)).

**Lemma 6.1 (PROVED).** Every model selected at an interior index of the milestone domain is T, some B_ij(t), or some V_k (Cor 4.3).

**Theorem 6.2 (forced jump; PROVED).** Let P be the path from p_T to the edge, and p_0 a boundary point of Φ_T ∩ P in P. Such a point exists: Φ_T is closed (LEAD Lemma A) and lies in the open simplex (Lemma E). Let p_n → p_0 in P with C_{p_n} ≠ T. Then:
- eventually every C_{p_n} lies in one family B_ij(·), along a subsequence;
- μ{C_{p_n} ≠ T} ≥ μ(Sil(T) ∩ M_k) > 0, where k is the third world.

So the selection is discontinuous in measure at p_0. This answers FF2's open point for this kernel: a jump is forced.

*Proof.*
- **Not a vertex model.** If C_{p_n} = V_k infinitely often, closed sections for the rival V_k give T ⪯_w V_k at every w. V_k is undominated, so T ≈ V_k at all worlds, against Lemma B.
- **So an edge family.** By Lemma 6.1, eventually C_{p_n} ∈ ∪ B_ij, and a subsequence stays in one family.
- **The measure gap.** B_ij(t) says A on all of M_k, where T is silent on Sil(T) ∩ M_k. ∎

**Theorem 6.3 (post-jump defences; PROVED, with one NUMERICS hypothesis).** In the setting of Theorem 6.2, let B_n := C_{p_n} ∈ B_ij(·). Let X := T[E ↦ A] with E ⊆ Sil(T) ∩ M_k bounded and non-null.
- **(a) Forced acceptance (PROVED).** For all large n, B_n ⪯_k X and B_n ⋠_i X, B_n ⋠_j X. Indeed X ≺_i T and X ≺_j T by strict (G), so closed sections at p_0 forbid B_n ⪯_i X and B_n ⪯_j X for infinitely many n. Competitiveness on full support leaves world k.
- **(b) The field rejects it.** Assume (H_k): inf_t (L_k(B_ij(t)) − L_k(T)) > 0. NUMERICS (`jump_gap_mc.out`): the margin, less 4 standard errors, is at least 0.44 for each ε ∈ {0.1, 0.3, 0.5, 0.9}, uniformly over 61 values t ∈ [10⁻³, 10³]; it is about 0.46 at ε = 0.3, t = 1. Choose E with ∫_E β_k smaller than that margin. Then Φ_k(rec(B_n, X)) = L_k(T) + ∫_E β_k − L_k(B_n) < 0. So world k must accept an unbounded record that ℓ rejects.
- **Consequence (PROVED, given (b)).** World k cannot accept all ℓ-nonnegative unbounded records. This is the analogue of PP33 Prop 8.2: Q := X[F ↦ contradiction] gives the accepted triangle B_n ⪯ X ⪯ Q ⪯ B_n, whose missing reverse Q ⪯ X is a strict guidance reversal.

**Lemma 6.4 (T is isolated in loss space; PROVED; NUMERICS (5)).** Put

  3c_3 := 3·min_k ∫_{Sil(T) ∩ M_k} (|g_k|/3)(1 − G(s_i) − G(s_j)) dμ > 0.

Then every registered C ≠ T satisfies Σ_w (L_w(C) − L_w(T)) ≥ 3c_3.

*Proof.* Σ_w (L_w(C) − L_w(T)) = 3∫(cost_u(C) − cost_u(T)) dμ, and the integrand is ≥ 0 because T is u-Bayes. Every C in Cor 4.3 other than T says A on Sil(T) ∩ M_k for some k: the third world of its edge, or any k ≠ k′ for V_{k′}. There the u-excess of A over silence is (1/3)(β_k − α_i − α_j) = (|g_k|/3)(1 − G(s_i) − G(s_j)). This is positive a.e., because T's A-region on M_k is exactly {G(s_i) + G(s_j) > 1}. Numerically, the sums are 0.29 for B_12(1) and 0.98 for V_k. ∎

**Theorem 6.5 (T's small fills; PROVED).** Let X = T[G ↦ V_j] with G ⊆ Sil(T) ∩ M_j bounded, and Σ_w Φ_w(G, S → V_j) < 3c_3 (true for small μ(G)). Then:
- X is incoherent (Lemma H);
- T does not dominate X: S → B on M_j is a strict j-improvement, so T ⋠_j X;
- every registered C ≠ T that dominates X accepts, at some world, a record with Φ_v(rec(C, X)) < 0.

*Proof of the last item.* Σ_v (L_v(X) − L_v(C)) = Σ_v Φ_v(G, S → V_j) − Σ_v (L_v(C) − L_v(T)) < 3c_3 − 3c_3 = 0. ∎

So T's fills, which the audit puts in the repair class, are never dominated inside the ℓ-positive fragment. Their dominations must be installed records of the kind in Prop 5.2.

**Proposition 6.6 (second generation: a forced rival of an edge model).** Let N = B_12(1), the edge segment over the shadow of M; it is the edge model whose window is exactly J. Let G′ ⊆ Sil(T) ∩ M_3 be bounded, where N = A. T's departure (G′, S → A) is a pure improvement at worlds 1 and 2, so it is accepted only at 3. By PP33 Prop 2.1(f), N ⋠_3 Z′ for Z′ = N[G′ ↦ S, E′ ↦ B]. Z′ is incoherent and lies in the repair class ("edge models' forced rivals").
- **(a) PROVED.** Every registered C outside the family B_12(·) has, at world 1 or 2, a loss exceeding N's by a uniform amount. The reason: N is the a.e.-unique (1/2, 1/2, 0)-Bayes model, and each such C differs from N on a fixed set where N is strictly optimal. For B_13 and V_1 that set is M_2 ∩ {θ_12 > β}; for B_23 and V_2 it is M_1 ∩ {θ_12 < α}; for T and V_3 it is Sil(T) ∩ M_3. So for small G′ none of them is an ℓ-positive dominator of Z′.
- **(b) In the family (NUMERICS, `second_gen_mc.out`).** L_3(B_12(t)) ≥ L_3(N) for all t. The value is symmetric under t ↦ 1/t and smallest at t = 1. But Z′ is strictly better than N at world 3. So no B_12(t) is an ℓ-positive dominator either. Ball radius 0.2 around (1, 1, −1.9), mass 2.6·10⁻⁴; ΔL(Z′) = (+7.0, +7.0, −9.8)·10⁻⁴ for E′ = G′, and (+1.1, +1.1, −4.9)·10⁻⁴ for E′ = ∅. The script reports min over each family's grid of max_v (ΔL_v(C) − ΔL_v(Z′)):
  - +0.086 (T), +0.73 (V_k), +0.55 (B_13, B_23), and +6·10⁻⁴ to +1.0·10⁻³ (B_12; in-family s.e. ≈ 5·10⁻⁵);
  - at N = B_12(2) the in-family gap is +5·10⁻⁴; extrapolating linearly along the family's tangent direction still leaves a gap of ≈ +3·10⁻⁴.

  The in-family check is a finite grid (±5% around t_0, plus 30 log-spaced values), so (b) is NUMERICS for these two N and this ball only.

So the recursion leaves the ℓ-positive fragment at the **second generation**, at the edge models' own forced rivals. The vertex rivals stay inside it because the frontier of registered loss vectors has a corner at each vertex, where the world-j cost is second order. Along the edge, the frontier is smooth, and a forced rival is Pareto-dominated only if its change happens to lie in the frontier's tangent cone.

**Summary of the residue.** Under the ℓ^T kernel the following need installed unbounded records with Φ < 0 at some world:
- post-jump defences against T[E ↦ A] (Thm 6.3, at world k);
- dominations of T's small fills (Thm 6.5);
- dominations of edge models' forced rivals (Prop 6.6).

Prop 5.2 is the exact (TC) interface for these with the kernel. Their mutual (TC), (B2) and shadow-freeness, and the far layer that gives competitiveness against unbounded rivals at those worlds, are the open part. Following REFEREE_round48 item (3), I state these as "rejected by the kernel's field", not as "endorsed by no field".

---

## 7. Classification

| Obstruction | Source | Label |
|---|---|---|
| Balanced kernels (Ω, L): no room; fail at the edges | chosen design (Prop 3.4; R46.1) | PROVED |
| Rank-linear or (H4) single-field kernels with T | chosen design (PP32, PP35 Thm A) | PROVED |
| Any single-field kernel with a precise in-band edge model | **optional commitment** (one field) plus **chosen geometry** (precise edge window in J) (Cor 3.3) | PROVED |
| Regional lexicographic kernels (subordinate cone) | chosen design (Thm 2.2) | PROVED |
| Exact largest-loss rule | chosen design (REFEREE_round48; completion acceptances) | CHECKED there |
| Precise non-vertex defenders under ℓ^T | chosen design: the field fixes the registrable geometry (Cor 4.3) | PROVED |
| Jump at T's fibre; post-jump defences rejected by ℓ at k | **axioms** (closed sections, strict (G), competitiveness, Lemmas A, B, E) plus the kernel (Thms 6.2, 6.3) | PROVED; (H_k) NUMERICS |
| T's small fills not ℓ-dominated | **axioms** plus the kernel (Thm 6.5) | PROVED |
| Edge models' forced rivals not ℓ-dominated | axioms plus the kernel (Prop 6.6) | PROVED except (b), which is NUMERICS |

None of these is an impossibility of the kernel. They are the places where the unbounded layer must depart from the kernel's field.

---

## 8. What remains, and the next step

1. **The ℓ-negative layer.** Install the residue records (§6) with compensation (B1) and no far inverses (B2), and decide the shadows among them. Prop 5.2 makes the kernel side automatic. The first test is Prop 6.6's Z′. Its natural dominators are T and the B_13/B_23 families, whose records are ℓ-negative at world 1 or 2 and compensated there.
2. **The jump.** Design the unbounded verdicts at p_0. Thm 6.3 says exactly what they must do: refuse B_n ⪯_i X and B_n ⪯_j X, and accept B_n ⪯_k X against ℓ. Whether this can be done with all sections at p_0 closed is OPEN. It is now a statement about one fixed rival family and one edge family.
3. **Other fields.** Is there a field whose coherent Bayes set contains a curve from T's weight into the interior (no jump)? Prop B of REFEREE_PP32_penalties forbids it near a whole edge, not along a curve. OPEN.
4. **Precise in-band edge models.** These need a non-field σ_N (B4). OPEN. Thm 2.2 and PP28 Lemma 6.2 forbid both lexicographic shortcuts.

**Most important next step.** Run the recursive milestone with the ℓ^T kernel fixed. Do all dominations that can be ℓ-positive that way (Thm 5.1 makes them free). Then spend the whole design effort on the three residue families, starting with Prop 6.6.

---

## 9. Status and scripts

| Result | Label |
|---|---|
| Thm 2.1 (forced list), Lemma 2.3, Ex. 2.4 | PROVED; Lemma 2.3 CHECKED |
| Thm 2.2 (no subordinate cone) | PROVED |
| Thm 3.1, Cor 3.2, Cor 3.3, Prop 3.4 | PROVED |
| Lemma 4.1 | PROVED (REFEREE_PP32_penalties); re-CHECKED |
| Lemma 4.2 (coherence lemma), Cor 4.3 | PROVED; CHECKED |
| Prop 4.4 (a) bounded room | PROVED; CHECKED |
| Prop 4.4 (b) first-generation ℓ-positive dominations | NUMERICS |
| Prop 4.5 (screens) | PROVED |
| Thm 5.1, Prop 5.2, Prop 5.3 | PROVED |
| Thm 6.2, Thm 6.3(a), Lemma 6.4, Thm 6.5, Prop 6.6(a) | PROVED |
| Thm 6.3(b) hypothesis (H_k), Prop 6.6(b) | NUMERICS |
| §8 items 1–4 | OPEN |

**Scripts** (`r9/PP38_py/`; run `python3 -I -B <script> > <script>.out` inside the folder):

| Script | Content | Label |
|---|---|---|
| `coherence_exact.py` → `.out` | (a) T = unique u-Bayes; (b) edge Bayes = segment D_{K(t)}; (c) Lemma 4.2 witnesses at 90 grid weights × 4 values of ε (B-kink and A-kink cases); (d) Lemma 2.3; (e) Prop 4.4(a). ALL PASS. | CHECKED |
| `field38.py` | vectorised ℓ^T, ranks, Bayes, T, V_j | library |
| `budget_mc.py` → `.out` | PP30's balls: Φ(d), the rivals Z_2 and Z_3, B_1x(t) dominators (budget, compensation, ℓ-values at all worlds), the jump margin, isolation sums | NUMERICS |
| `second_gen_mc.py` → `.out` | Prop 6.6: the forced rival Z′ of B_12(t_0); best ℓ-domination gap per registered family | NUMERICS |
| `jump_gap_mc.py` → `.out` | (H_k) for four values of ε (min margin 0.44 after 4 s.e.); also the edge-world margin min_{w=1,2}(L_w(B) − L_w(T)) < 0 for every t | NUMERICS |
