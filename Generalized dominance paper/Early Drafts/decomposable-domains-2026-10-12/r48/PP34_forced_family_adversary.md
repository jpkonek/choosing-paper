# PP34. The forced-defence family: adversary's report

22 October 2026. Adversary's note for Brief 48 (task PP34). One reader (me); not refereed.

**Labels.** PROVED: complete argument here. CHECKED: exact finite computation (integer record algebra on cells; SAT with full (TC) through PP23 Lemma 1.1; LP realisability of cell patterns). Cells check bookkeeping and finite consistency only; they say nothing about (S) on the simplex, and a cell dominator is only one of the dominators the continuum allows. NUMERICS: none. CONJECTURE / OPEN: as stated.

**Scripts** (`r9/PP34_py/`; run `python3 -B <script>` inside the folder; outputs in `.out` files):

| Script | Content | Label |
|---|---|---|
| `lib34.py`, `geom34.py` | cell record algebra, P1/P2 encoding, T1's advice, LP realisability | library |
| `coordination_check.py` | Lemma 2.1 bookkeeping (2,214,657 configurations); blocked-world counts for four departure rules (Prop 5.2, Remark 5.3) | CHECKED |
| `seam_nonadditive_sat.py` | PP32's seam configuration without endorsement (T plus an all-A model on every edge), five cell sets | CHECKED |
| `argmax_sat.py`, `argmax_core.py` | the largest-loss rule imposed on all of T's departures, with full (TC); minimal core of the one failure | CHECKED |
| `forced_family_sat.py` | the forced family itself: T, V_1–V_3, selected patterns chosen by the solver, every Z with a selected dominator, 1-D edge KKM, direct (C), undominatedness; variants with maximal selection and with the silent-wedge dominators of §5.4 | CHECKED |

**Inputs.** Brief 48; AUDIT_round48_instructions (binding); PP30 (Theorem 3.1, Prop 4.2); REFEREE_round47; PP28 (separation lemma), PP29 (retreat split); PP32 (Lemmas 2.1–2.2, Theorem 3.1); AUDIT_completion (rules I–IV); AUDIT_selected_realizability §4 (support-sensitive obligations); REFEREE_Z_PP19 (Lemma H, Prop S); PP19 (Lemma 0.2, Lemma 5.0, Theorem 5); PP18 (Theorem Z); PP23 (Lemma 1.1, Theorem 2.1, undo Lemma 2.2); PP26 (Theorems V and M); LEAD_selection_count (Lemmas A, B, E). Axioms: Brief 48's and nothing else. Transitivity, absence of ties, continuity in measure and joint continuity are never used. Single-world ties and triangle completion are allowed throughout.

---

## 0. Verdict

**No obstruction found. The family has a precise freedom, and I can name it.**

I tried every lever in the brief. Each produces only *refusals*: verdicts that some world must withhold. A refusal hurts only when some selected model needs that world. I proved that the forced-defence family, together with all of its (IB) copies, reduces to **one** first-order condition of this kind (§3, the coordination condition (CC)). I then exhibit a joint rule that meets it (§5). Nothing I tried derives F1 or F2 from the axioms plus "T selected".

| Question | Answer | Where | Source of each failure met |
|---|---|---|---|
| Can the w-rule be refuted from T's side alone? | **No.** Any choice of accepting worlds among each departure's loss worlds is (TC)-consistent and makes T competitive against every rival that changes T only inside Sil(T). | Prop 2.3 (PROVED) | — |
| What do the forced defences force? | Exactly the padded-undo refusals of Lemma 2.1, in every context: a strict extension of PP30 Thm 3.1(b) to padded retreats. | Lemma 2.1, Cor 2.2 (PROVED; CHECKED) | axioms + T selected |
| Lever (IB): shared records | The refusals pass to every model that gives V_j's answers on the piece. When a selected edge model on [e_w, e_w′] does, V_j's verdict on every rival Z of the family is fully determined: refused at w, accepted at the other two worlds. | Props 3.1, 3.2 (PROVED) | axioms + T selected + an optional edge realiser |
| Lever: G versus G ∪ H, and j versus j′ | No conflict. On one-class pieces, every vertex is forced to the same world. Across nested pieces the only constraint is (CC). | Prop 3.3 (PROVED) | — |
| Lever: the dominators' own obligations | Edge dominators near e_j have guidance-trivial retreat defences on single-class pieces. Their two-class pieces fall under (CC). | Prop 4.1(f), §5 | — |
| Lever: KKM, 1-D edge KKM, sections | For each rival there is a selected dominator on [e_j, e_w], away from V_j's fibre. Nothing prevents dominators of shrinking pieces from creeping to e_j. | Props 4.1(d), 4.4 (PROVED) | sections are per rival |
| Lever: PP19 Theorem 5 / Prop S | **Vacuous here.** The copies of the dominations into T's context are strict guidance improvements of T at world j only, and Theorem 5 / Prop S need two worlds. | Prop 4.2 (PROVED) | — |
| Lever: PP18 Theorem Z | No correctness zone arises: the refusals are record-specific and leave other w-correcting records free. | Remark 4.5 | — |
| Joint rule: departures | The **largest-loss rule** accepts each departure from T's silence at the world with the largest ν-mass of errors, ties broken by a fixed priority. It never blocks any realiser at two worlds. Balanced additive rules (Ω) and tie-sharing rules do. | Prop 5.2 (PROVED); Remark 5.3 (CHECKED) | Ω's failure is from an optional comparison |
| Joint rule: dominators | **Silent-wedge dominators.** D(j,G,E) = V_j silenced on the wedge W_jw ∩ {θ_jw > τ}, i.e. D_[e_j, λ] with λ on [e_j, e_w], and τ = τ(G,E) chosen per rival. They never form a forbidden (P1) pair with any of T's departures. | Prop 5.4 (PROVED) | — |
| Cells | Satisfiable: PP32's seam configuration with no endorsement; the largest-loss rule with completion; V_1's whole family with selected dominators, 1-D edge KKM and direct (C), also with maximal selection and with the silent-wedge dominators forced. Two failures, both explained: "exact" largest-loss (completion must add acceptances), and cell artefacts in which the cells contain no dominator. | §6 (CHECKED) | |

**What it costs** (§7). The w-rule is non-additive (it has to be, by PP32) and *cross-world*: world w accepts a departure by comparing its own error mass with the other worlds' error masses. It must be mass-sensitive, by PP26 Theorems M and V. It must accept, by triangle completion, more than the single largest-loss world (cells). Near a silent edge model it must use that edge's worlds. At world j the dominators exchange an unbounded silent wedge for a bounded retreat. Lemma 0.2 then forces world j to rank every bounded retreat inside the wedge strictly above the rival. That is consistent, but it is an "infinitesimal wedge" verdict (Prop 5.6).

**What is not done.** This is not a construction. The joint rule is specified on departures from T's silence and on the family's dominations. A full relation must also make T competitive against rivals that change T's answers, make every dominator competitive against all of its own rivals, and close sections on the whole simplex. Those are exactly the parts of the original problem the family does not touch. The remaining danger is in (P2) triangles and in completion-forced acceptances that I could check only on cells (§8).

---

## 1. Setting and tools

Brief 48's setting: three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain, modulo null sets; ranks correct 0 < silent 1 < wrong 2 < contradictory 3. T = T1 = D_M with M = c·1 + εΔ, selected (hence at an interior index, Lemma E). Sil(T) is T's silent cone. On a class M_k (k the minority world) A is the majority answer and B the minority answer.

- **Error sets.** W_jw := {g : g_j g_w < 0} = M_j ∪ M_w. V_j is w-wrong exactly on W_jw. For advice a on a set H, write Wr_i(a) and Cor_i(a) for the points of H where a is i-wrong, resp. i-correct.
- **Departures.** A *departure* is a record d = (H, S → a) with H ⊆ Sil(T) and a regular (A or B) a.e. on H. T's competitiveness against T[H ↦ a] says exactly that Acc(d), the set of worlds accepting d, is nonempty. Its *loss worlds* are L(d) := {i : Wr_i(a) non-null}. By strict (G), Acc(d) ⊆ L(d). On mixed problems no answer is correct at all three worlds, so L(d) ≠ ∅.
- **The family.** For a vertex j and a bounded non-null G ⊆ Sil(T): r^j_G := (G, S → V_j). For w ∈ Acc(r^j_G) and non-null E ⊆ G: Z^w_{G,E} := V_j[G ↦ S, E ↦ w-correct], and R^j_G := V_j[G ↦ S].
- **(TC) on records.** PP23 Lemma 1.1: with weak guidance accepted, strict (G) and (TC) hold at i iff (P1) no two accepted mixed records compose to a pure i-improvement, and (P2) every accepted triangle of mixed records has its reverses accepted. (IB) makes verdicts functions of records.

---

## 2. What the forced defences force

**Lemma 2.1 (padded undo; PROVED; CHECKED in `coordination_check.py` A).** Uses (IB), strict (G), (TC). Let d = (H, S → a) be accepted at i, with H measurable (bounded or not). Let O ⊆ H with O ⊇ Wr_i(a), and let b be advice on O with values in {S, i-correct}. Suppose the record q := (O, a → b) is nontrivial and (H ∖ O) ∪ {b ≠ S} is non-null. Then q is refused at i, in every context.

*Proof.* Take any X that is S on H. Put Y := X[H ↦ a] and W := Y[O ↦ b]. Then rec(X, Y) = d, so X ⪯_i Y. If q were accepted, then Y ⪯_i W. Now W differs from X only on (H ∖ O) ∪ {b ≠ S}. There W carries a (which is i-correct, because O contains all of Wr_i(a)) or b (which is i-correct). So W ≤_i X pointwise, strictly on a non-null set, and W ≺_i X by strict (G). That violates (TC). ∎

CHECKED: on all cell patterns with 1–5 pieces, every such composite d·q is a pure i-improvement (2,214,657 configurations).

**Corollary 2.2 (the vertex family exactly; PROVED).** Let w ∈ Acc(r^j_G). Then w ≠ j and G ∩ W_jw is non-null. At w, every record (O, V_j → b) is refused that satisfies all of:
- G ∩ W_jw ⊆ O ⊆ G;
- b ∈ {S, w-correct} on O;
- the record is nontrivial;
- (G ∖ O) ∪ {b ≠ S} is non-null.

In V_j's context: V_j ⋠_w V_j[O ↦ b]. Two special cases:
- O = G recovers PP30 Thm 3.1(b): the rivals Z^w_{G,E}.
- O ⊊ G with b ≡ S gives the **padded retreats**: V_j ⋠_w R^j_O whenever O contains every w-error of V_j in G and misses a non-null part of G.

The refusal is a genuine (non-guidance) constraint iff b = S on a non-null part of O ∖ W_jw. Otherwise the target is a pure w-improvement of V_j, and strict (G) refuses it anyway.

*Proof.* Lemma 2.1 with H = G and a = V_j|_G; Wr_w(V_j) = W_jw. ∎

**Proposition 2.3 (the w-rule alone is free; PROVED).** Uses PP23 Lemma 1.1 and Theorem 2.1. Choose any ∅ ≠ Acc(d) ⊆ L(d) for every departure d. Let each world accept weak guidance and its chosen departures. Then:
- reflexivity, strict (G), (IB) and (TC) hold;
- T is competitive against every rival that differs from T only inside Sil(T);
- no such rival dominates T.

*Proof.* An accepted departure has a loss at its world, so it is never a pure improvement there.
- (P1): two departures compose only on disjoint supports (the second needs old side S), to their union, which keeps a loss.
- (P2): the closing edge of a triangle of departures is a retreat, which is never accepted unless it is guidance.
- Competitiveness is the choice Acc(d) ≠ ∅.
- A dominator X of T with X = T off Sil(T) would need rec(X, T), a retreat from answers to silence, accepted at all three worlds. Here only guidance retreats are accepted, and no answer on a mixed problem is correct at all three worlds. ∎

**Consequence.** *No obstruction can come from T's forced defences alone, whatever the w-rule.* Every obstruction has to use some other accepted record: a selected model's defence, a domination, or a section.

---

## 3. Shared records: one record, one verdict

**Proposition 3.1 (realisers inherit the refusals; the coordination condition; PROVED).** Uses (IB) and Lemma 2.1. Let N be selected at q and give advice a a.e. on O ⊆ Sil(T). For each world i, call a record q* = (O, a → b) (with b as in Lemma 2.1) *blocked at i* if some departure d = (O ∪ F, S → a ⊕ c) is accepted at i, where:
- F is disjoint from O, and c is i-correct on F;
- F is empty only if b has an i-correct point.

Blocked records are refused at i in N's context too. So competitiveness of N against N[O ↦ b] needs:

  **(CC)** supp q ⊄ {blocked worlds of (O, a → b)}, for every such O and b.

(CC) is a necessary condition on the joint choice of departure verdicts and of the selected family.

*Proof.* Lemma 2.1 with H = O ∪ F and advice a ⊕ c. Its hypothesis O ⊇ Wr_i(a ⊕ c) holds because c makes no i-errors. Verdicts are per record, so the refusal holds in N's context. ∎

Vertex models satisfy (CC) for free: V_j's records of this kind are pure j-worsenings, accepted at j by guidance. The condition bites on edge and interior models. For edge models it is PP32's seam problem stated without additivity, and §5 solves it.

**Proposition 3.2 (an edge realiser fixes the vertex's verdicts; PROVED).** Let {w, w′} be the two worlds other than j. Let G ⊆ Sil(T) ∩ (M_w ∪ M_w′) be bounded, and suppose a model selected on the open edge [e_w, e_w′] says A a.e. on G. Then for every w ∈ Acc(r^j_G) and every non-null E ⊆ G:
- V_j ⋠_w Z^w_{G,E};
- V_j ⪯_{w′} Z^w_{G,E};
- V_j ⪯_j Z^w_{G,E}.

So V_j's verdicts on the whole family over G are determined.

*Proof.* On M_w ∪ M_w′, j is a majority world, so V_j = A there, and the edge model N equals V_j on G. The first item is Cor 2.2. N is competitive on {w, w′} against N[G ↦ S, E ↦ w-correct], and it refuses at w by (IB). So it accepts at w′, and the copy into V_j's context gives the second item. The third is guidance. ∎

*Example.* PP30's two balls for V_1 (B+ ⊆ M_2, B− ⊆ M_3), with an edge model on [e_2, e_3] that says A on both balls. That model exists whenever its credal segment lies inside the band of each ball's class (PP32 Lemma 1.1). V_1 then accepts every Z at its non-refusing world.

**Proposition 3.3 (different vertices and nested pieces; PROVED).**
- **(a)** If G ⊆ M_k and j, j′ ≠ k, then r^j_G = r^{j′}_G = (G, S → A), and Acc = {k}: at the other two worlds A is correct, so strict (G) refuses. All vertices with the same record share the same world.
- **(b)** Suppose that on each edge a selected model says A a.e. on Q = Q_1 ∪ Q_2 ∪ Q_3, with Q_k ⊆ Sil(T) ∩ M_k (write H_k := H ∩ Q_k; k is the third world below). Let i ∈ Acc(H, S → A) and l ≠ i. Then l ∉ Acc(H′, S → A) whenever some O satisfies:
  - H_i ⊆ O ⊊ H and O ⊊ H′;
  - H′_l = O_l;
  - H′ ∖ O ⊆ Q_i ∪ Q_k.
- **(b′)** In mass coordinates, for a rule that picks one world α(h) from h = (ν(H_1), ν(H_2), ν(H_3)): if α(h) = i and α(h′) = l ≠ i, then it is not the case that h′_i > h_i and h′_l < h_l.

*Proof.*
- (a) Strict (G).
- (b) Lemma 2.1 at i refuses the retreat (O, A → S), because H ∖ O lies in classes where A is i-correct. Lemma 2.1 at l refuses the same retreat, through H′ ∖ O, which lies in classes where A is l-correct. The model on edge {i, l} that says A on O is then not competitive against N[O ↦ S].
- (b′) is (b) for sets chosen with the prescribed masses, which exist because μ is atomless: take O := H_i ∪ O_l with O_l ⊊ H_l of mass h′_l, and H′ := O ∪ (extra in Q_i) ∪ (anything in Q_k).

The largest-loss rule of §5 satisfies (b′). The balanced rule Ω does not (Remark 5.3). ∎

So nested pieces and different vertices interact only through (CC). The brief's suspicion, that the w-choices for G and G ∪ H might be forced apart, is right only in the sense of (b): it is a monotonicity condition, not a contradiction.

---

## 4. The dominators

Fix j, G, w ∈ Acc(r^j_G) and E, and write Z := Z^w_{G,E}, w′ := the third world, G″ := supp rec(V_j, Z).

**Proposition 4.1 (anatomy of a dominator; PROVED).** Let D be coherent with D ⪯_v Z at all v, strictly at one.
- **(a)** D ≠ V_j (PP30). D is strictly j-better than Z on a non-null part of G. Off G, Z = V_j is j-perfect; if D were no better on G, then Z ≤_j D pointwise, strictly on the cone {D ≠ V_j} ∖ G, and strict (G) would refuse D ⪯_j Z.
- **(b)** Let D′ := D[G ↦ Z|_G]. Then D′ ⋠_j D. Indeed Z ≤_j D′ pointwise (equal on G, and V_j off G), strictly. So D′ ⪯_j D ⪯_j Z ≺_j D′ would violate (TC).
- **(c)** If E ∩ W_jw is null, then T ⋠_j D: Z ≤_j T pointwise, strictly on (Sil(T) ∪ {T ≠ V_j}) ∖ G, so T ⪯_j D ⪯_j Z ≺_j T is excluded. T's defence against such a dominator is at w or w′.
- **(d) 1-D edge KKM.** The closed sections A_j(Z) and A_w(Z) cover the edge [e_j, e_w]:
  - e_j ∈ A_j(Z) by guidance;
  - e_j ∉ A_w(Z) by Cor 2.2;
  - e_w ∈ A_w(Z) by guidance.

  So some index q* ≠ e_j on that edge carries a selected C with C ⪯_j Z and C ⪯_w Z. If C is coherent it is D_K with K ⊆ [e_j, e_w] (PP32 Lemma 2.1), and K ≠ {e_j}.
- **(e) Inheritance.** If D = V_j a.e. on G″, then rec(D, D′) = rec(V_j, Z), so D ⋠_w D′. D′ is incoherent (Lemma H) and needs its own dominator D₂ ≠ D. The regress ends at the first dominator that differs from V_j on part of G″. It is not an obstruction: it is the general fact that every incoherent model needs a dominator. Under any additive valuation it must end (disjoint annuli of the wedge carry bounded total mass). Under (TC) alone I found no reason it must end, and none that it must not.
- **(f)** If D is an edge model on [e_j, e_w] and O is a piece of one class on which D answers, D's retreats from O are guidance at j or at w. D's answers there are j-correct, w-correct, or A on the third class (correct at both). So D's own forced defences bite only on two-class pieces, where (CC) applies.

**Proposition 4.2 (PP19 Theorem 5 and Prop S are vacuous here; PROVED).** Let Σ := supp rec(D, Z). Copying the domination into T's context gives P := T[Σ ↦ D] ⪯_v Q := T[Σ ↦ Z] at every v. Assume:
- {D ≠ V_j} meets Sil(T) ∩ M_w in a non-null set;
- {D ≠ V_j} meets {T = A} ∩ M_j in a non-null set.

Both hold for every edge model on [e_j, e_w] whose silent or w-correct wedge is {θ_jw > τ}, because θ_jw is unbounded on Sil(T) ∩ M_w (u^⊥ ⊆ Sil(T)). Then Q is a strict pointwise improvement of T at world j at most. Lemma 5.0 therefore applies only at j, where it yields T ⋠_j Y for a Y that strict (G) already refuses. Theorem 5 and Prop S need the domination at two worlds of strict pointwise improvement, so they give nothing.

*Proof.*
- **At w:** on the first set, Q = V_j = A, which is w-wrong, while T is silent.
- **At w′:** on the second set, Q = V_j = B, which is w′-wrong, while T says A, which is w′-correct.
- **At j:** Q = V_j is j-correct on the cone and S or w-correct on G. ∎

**Proposition 4.3 (the wedge sandwich at world j; PROVED).** If D ⪯_j Z, then Z ⋠_j W for every W ≺_j D (PP19 Lemma 0.2). In particular Z ⋠_j R^j_{G‴} for every bounded G‴ ⊆ {D not j-correct}. If G‴ ⊇ G ∖ E, guidance would accept Z ⪯_j R^j_{G‴}. So D is j-correct on a non-null part of G ∖ E, or E ∩ W_jw is non-null, consistently with 4.1(a).

**Proposition 4.4 (sections; PROVED).**
- For each fixed rival Z, Dom(Z) := ∩_v A_v(Z) is closed and misses F_{V_j}. So its distance from e_j is positive (PP30 4.2(c)).
- For G_n with μ(G_n) → 0, the dominator indices may accumulate at e_j. Each fixed Z_m is refused at w by all indices near e_j, and no fixed rival is inherited. This is PP19 Theorem 7 / Remark 7.1 with V_j in place of T.

Sections constrain each rival separately and never the family as a whole.

**Remark 4.5 (Theorem Z; PROVED).** Cor 2.2 refuses only records supported in the bounded set G. Theorem Z's improving comparisons C_p ⪯_w V_k[Q → w-correct] have unbounded support: C_p and V_k are distinct coherent models (V_k refuses its own strict w-improvement), so they differ on a non-null cone, which has non-null parts off every bounded Q. So none of Theorem Z's records is refused, and no correctness zone is created.

---

## 5. The exact freedom: a joint rule

### 5.1 What has to be chosen

By §§2–4, the family's first-order content is (CC), together with the dominations. Departures are chosen by the w-rule; dominations by the dominator rule. The two rules interact only through (P1) pairs (departure, domination), handled in Prop 5.4, and through (P2) triangles, which are not closed (§8).

### 5.2 The largest-loss rule

Fix a finite measure ν equivalent to μ (μ itself will do) and a priority order π on the worlds. For a departure d = (H, S → a), let ℓ_w(d) := ν(Wr_w(a)), and let α(d) be the π-first world maximising ℓ_w(d). Since a has errors on a mixed problem, max ℓ > 0, so α(d) ∈ L(d).

**Proposition 5.2 (single blocking; PROVED; CHECKED in `coordination_check.py` B).** Suppose every departure d is accepted at α(d) and at no other mixed world. Then every record (O, a → b) of Prop 3.1 is blocked at **at most one** world. Hence (CC) holds for every selected model whose support has at least two worlds. In particular, for the vertex family the rule sets w(j, G) := α(r^j_G) ≠ j.

*Proof.* Suppose the record is blocked at i through d_i and at l ≠ i through d_l. Their loss vectors are ℓ(O) + p and ℓ(O) + p′, with p_i = 0 and p′_l = 0: the padding is i-correct, resp. l-correct.
- α(d_i) = i gives ℓ_i(O) ≥ ℓ_l(O) + p_l ≥ ℓ_l(O), with equality only if i precedes l in π.
- α(d_l) = l gives ℓ_l(O) ≥ ℓ_i(O), with equality only if l precedes i.
- So ℓ_i(O) = ℓ_l(O), and each of i, l precedes the other. That is impossible. ∎

*Scope.* Prop 5.2 counts blocks caused by T's departures. On cells, triangle completion forces some departures to be accepted at a second world as well (`argmax_core.out`), so in a full relation the rule reads "at least α(d)". The cell runs with the rule in that form are all SAT. A continuum bound on the blocks caused by completion acceptances is OPEN (§8).

**Remark 5.3 (who fails; CHECKED in `coordination_check.py` B; PROVED by the examples).**
- **The balanced additive rule Ω** (accept S → A at i iff 2h_i ≥ h_j + h_k) blocks an edge model's retreat at both of its worlds. Example: class masses (0, 1, 1), blocked at worlds 2 and 3. This is R46.1 / PP32 in (CC) form, and it comes from an optional comparison (Ω's verdicts).
- **Largest-loss with ties shared** (accept at every maximising world) blocks two or three worlds at ties: loss vector (1, 1, 1).
- **The world-priority rule** (accept at the π-first loss world) also blocks at most one world. But it is mass-blind, so it falls under PP26 Theorems M and V once KKM dominators of Theorem V's rivals are required.

The largest-loss rule is the mass-sensitive representative.

**Proposition 5.3′ (silent edge models; PROVED for the shapes stated).** An edge model N on {x, y} can be silent only inside W_xy (PP32 Lemma 2.1). On W_xy every answer is wrong at x or at y, so every departure d inside N's silent region has a loss at x or at y. If α(d) = z ∉ {x, y}, N needs d accepted at x or y as well. **Amendment:** accept d also at x if a has B on a non-null part of supp d ∩ M_y, and otherwise at y. B on M_x or on M_y is z-wrong, so α(d) = z guarantees one of these cases. With this amendment:
- **(i)** No realiser on {x, z} or {y, z} is blocked by an amended acceptance. The record would need O ⊇ Wr_x(a), which contains B-points of M_y, and edge models on {x, z} say A on M_y.
- **(ii)** No realiser on {x, y} is blocked at its other world. A y-padded superset of O* ⊆ supp d has ℓ_y − ℓ_z ≤ ℓ_y(d) − ℓ_z(d) ≤ 0, with ties resolved towards z.
- **(iii)** The same record is never blocked at x by one amended departure and at y by another. Blocking at x forces a to have B on O* ∩ M_y, and that rules out the choice y for every amended departure containing O*.

Hence an edge realiser is blocked at most at one world. An interior realiser is blocked at most at two (one by α, by Prop 5.2, and one by the amendment, by (iii)), so it keeps a world. For (i) with y in place of x: the rule picks y only when there is no B on supp d ∩ M_y. Then α(d) = z forces B-points on supp d ∩ M_x, which edge models on {y, z} cannot realise.

Not covered: OPEN, but satisfied on all cells tested (§6).
- one-class pieces on which two edges are silent;
- silent regions of different edges overlapping inside one class.

### 5.4 The dominator rule: silent wedges

For w = α(r^j_G), let Wd(τ) := W_jw ∩ {|g_w| > τ|g_j|}, and define

  D(j, G, E) := V_j[Wd(τ) ↦ S] = D_[e_j, λ_τ],

where λ_τ ∈ (e_j, e_w] is the point with threshold τ, and τ = τ(G, E) is chosen per rival with Wd(τ) ∩ G null. (This needs ess sup_G θ_jw < ∞, true for PP30's balls; for general G see §8.) The credal set is genuinely variable: it is the segment from the vertex to a rival-dependent point. Each such D is coherent. It may be selected on the edge [e_j, e_w], on the segment q ↦ D_[e_j, q].

**Proposition 5.4 (dominations never meet T's departures in (P1); PROVED).** Let ρ := rec(D, Z) be accepted at all three worlds, and let r be any departure, with r accepted at α(r) or at any world. Neither r·ρ nor ρ·r is a nontrivial pure improvement at a world where r is accepted.

*Proof.* The support of ρ is Wd ∪ G″. On Wd, ρ is S → V_j. On G″, ρ is V_j → Z.
- **r·ρ.** It composes only if r's new side equals D on its overlap with Σ. Since D = S on Wd, r misses Wd. The composite contains S → V_j on Wd:
  - this is a w-worsening (Wd ⊆ W_jw);
  - it is a w′-worsening on Wd ∩ M_j, which is non-null (V_j = B there);
  - so the composite can be a pure improvement only at j.

  At j, every part must improve. Hence r ⊇ G ∖ E with new side V_j there, E ∩ W_jw is null, and r's remaining new side is j-correct. Then r has no j-loss, so it is never accepted at j.
- **ρ·r.** It requires r's old side S to sit where Z is silent and D is not, so supp r ⊆ G ∖ E. The composite contains S → V_j on Wd, so again only j is possible. At j the parts V_j → c on supp r cannot improve on the j-correct V_j. ∎

**Proposition 5.5 (closed sections for the wedge family; PROVED, conditional on a threshold form).** Suppose the verdicts of D_[e_j, λ_τ] against a fixed rival X are monotone in τ at each world, with closed threshold sets. Then the sections of the segment selection near e_j are closed.
- For X = Z^w_{G,E}: A_w(Z) = {τ ≤ τ_w(Z)} misses τ = ∞ (that is e_j), as Cor 2.2 requires.
- A_j(Z) = {τ ≥ τ_j(Z)} contains e_j, as guidance requires.
- Dominators of Z exist on the segment iff τ_j(Z) ≤ τ_w(Z) (and the w′ verdict agrees).

Illustration: value the wedge part of rec(D, Z) with |g|-weights, so that its j-cost is of order τ⁻² and its w-gain of order τ⁻¹. Then τ_j ≤ τ_w holds whenever Z's forced w-advantage Δ_w(Z) is at most a constant times the square root of its j-cost Δ_j(Z). In particular it holds for all sufficiently small pieces, because Δ_w(Z) ≤ C·Δ_j(Z): every change of Z on G″ is a j-worsening. The monotone threshold form is a design choice, not forced.

**Proposition 5.6 (the cost at world j; PROVED).** By Prop 4.3, world j must rank every bounded retreat R^j_{G‴} with G‴ ⊆ Wd(τ) strictly above Z. As G shrinks, τ(G, E) → ∞ is allowed (Prop 4.4). World j then treats ever thinner wedges as no worse than ever smaller retreats. This is consistent with |g_j|-weights on the wedge records (the wedge's j-mass decays like τ⁻²). It is not a statement about T's region.

---

## 6. Cell checks (CHECKED)

All runs use exact integer record algebra, strict (G), (IB), and full (TC) through P1/P2 over all composable pairs (up to 15 million P2 triangles per world).

| Run | Content | Result |
|---|---|---|
| `seam_nonadditive_sat` | T silent on all pieces, competitive and undominated; the model that says A everywhere selected on all three edges (H_A), competitive on each edge pair, undominated. Classes (1,2,3), (1,1,2,3), (1,1,2,2), (1,1,2,2,3), (1,1,1,2,3). | SAT in all five. PP32's seam barrier is about endorsement, not about (TC). The solver's witness is a class-priority rule, which is mass-blind (PP26 Theorem M); see the next row for a mass-sensitive one. |
| `argmax_sat`, "at least" | the largest-loss rule imposed on all of T's departures (A and B answers), plus H_A; six class/mass sets up to five pieces | SAT in all six |
| `argmax_sat`, "exact" (refused at every other mixed world) | same | SAT in four, **UNSAT in two** (classes (1,1,2,2,3)). Minimal core (`argmax_core.out`, six items): the edge-12 and edge-23 obligations, the rule's verdicts on four departures, among them a three-way tie. Completion must add acceptances. Prop 5.2 holds as stated, but in a full relation the rule is "at least α(d)". |
| `forced_family_sat`, layout ab, V_1's family, 1-D edge KKM (`ff_ab_v1_edgeKKM.out`) | 7 rivals R, Z (G ∈ {a, b, a∪b}, all E, w = 2, 3); the selected set chosen by the solver among the 11 cell-coherent patterns; direct (C); undominatedness | SAT. T accepts a at w = 2, b and a∪b at w = 3. The dominator of all seven is V_1 with A on the cone cell, an edge-12 / edge-13 model. |
| same with maximal selection (`…_maxsel.out`) | every cell-coherent pattern selected on every face where it is realisable: competitive there and undominated (PP29's "sel" load) | SAT |
| same with silent-wedge dominators forced (`…_wedge.out`) | the dominator of every R, Z of V_1 must be V_1[c ↦ S] (§5.4) | SAT |
| layouts ad, bd (second cone cell d; 27 cell-coherent patterns), V_1's family, edge KKM; plain / maximal selection / wedge forced (`ff_ad_v1_*`, `ff_bd_v1_*`) | | SAT in all six |
| layout ab, all incoherent cell models need cell dominators (`ff_ab_all_edgeKKM.out`) | | UNSAT. **Artefact**: a continuum dominator need not be cell-measurable. |
| layouts ab, ad, bd, all three vertex families (`ff_*_family_edgeKKM*.out`) | | UNSAT; minimal core R_2 (resp. R_3) alone. **Artefact, PROVED by enumeration of the cell-coherent patterns.** By exposure (PP19 Lemma 0.4 with N = T), R_2's dominator must differ from R_2 at a cell where T does. It must be B on a (otherwise it is a pure 2-worsening). Every remaining cell-coherent pattern is then a pure 3-worsening of R_2. The continuum dominator uses a cone in W_23 that these five cells do not contain. |

So, on every cell set where the vertex's dominators can exist at all, the whole family closes under the full axioms:
- including 1-D edge KKM and direct (C);
- including maximal selection;
- with the silent-wedge dominators of §5.4 forced.

On the cells where it fails, the failure is the absence of a dominator, which is a property of the cells and not of the axioms.

---

## 7. Classification and costs

| Lever tried | Outcome | Classification |
|---|---|---|
| (IB) transfer of r^j_G to X, to V_j and to defenders | refusals only (Lemma 2.1, Prop 3.1) | axioms + T selected; harmful only via (CC) |
| Edge realiser of V_j on seam pieces | V_j's verdicts determined (Prop 3.2) | axioms + T selected + the optional selected edge model |
| j versus j′, G versus G ∪ H | same world on one-class pieces; monotonicity (b′) | axioms + T selected |
| Ω as the w-rule | double blocking | optional comparison |
| Shared-tie largest loss | double blocking at ties | optional comparison |
| "Exact" largest loss | UNSAT on 5 cells | optional comparison (completion needs more acceptances) |
| Dominator chain (inheritance) | no contradiction; ends under any additive valuation | — |
| PP19 Theorem 5 / Prop S on dominator copies | vacuous (one world) | — |
| Sections, KKM, edge KKM | rival-wise only; creeping allowed | — |
| Theorem Z | no zone | — |
| All three vertex families on 5 cells | UNSAT | chosen geometry (cell artefact, proved) |

**Costs of the surviving rule.**
1. **Non-additive and cross-world.** α compares world w's error mass with the others'. This is unavoidable for any single positive field (PP32 Thm 3.1, Cor 3.3), and Ω fails (CC).
2. **Mass-sensitive.** Mass-blind alternatives exist at first order (world priority, the cell SAT witnesses), but PP26 Theorems M and V exclude them under (S).
3. **Completion acceptances.** The rule cannot be exact. Which extra acceptances completion forces, and whether they ever double-block, is checked only on cells.
4. **Support-aware near silent edge models** (Prop 5.3′). The one-class double-silent case is open.
5. **The wedge verdict at world j** (Prop 5.6). Accepting unbounded silent wedges against bounded retreats is non-S_0 only through the family's forced verdicts at w. At j it can be S_0-like.
6. **Wedges must miss G.** This holds when G's θ_jw-range is bounded. A G whose directions approach the plane g_j = 0 inside W_jw needs a dominator whose wedge meets G; there D = S = Z off E. Its (P1) analysis is the same with E ∩ Wd in place of E, but I did not complete it.

---

## 8. What remains open, and the next adversarial test

1. **(P2) triangles mixing departures, completion acceptances and wedge dominations.** Prop 5.4 is (P1) only. The cells pass. A continuum argument would have to control triangles with one bounded edge and two unbounded wedge edges (PP23 Lemma 1.2: such triangles have 0, 2 or 3 unbounded edges).
2. **One-class pieces silent for two edge models** (Prop 5.3′). On M_x, edges {x,y} and {x,z} can both be silent. A departure with B everywhere there must be accepted at y and at z. I checked that no realiser of B on M_x exists on {y,z} (Lemma 2.1 of PP32), which removes the obvious clash, but not the general case.
3. **Registration of the wedge dominators.** D_[e_j, λ] must be undominated and competitive on its support against every rival, not only against the records of §5. On cells this holds (maximal-selection runs). In the continuum it is OPEN.
4. **T's rivals that change T's answers** (outside Sil(T)), and the dominators' competitiveness against all of their rivals. These are outside the family. Prop 2.3 says the family adds nothing to them, but the full relation must handle them.
5. **The strongest remaining test.** Take PP30's two balls for V_1, the largest-loss world w, the silent wedge on [e_1, e_w], and an edge model on [e_2, e_3] that says A on both balls (Prop 3.2). Then check every (P2) triangle among:
   - the domination;
   - the edge model's forced acceptance at w′;
   - T's departures on the balls and on the wedge's silent part;
   - the completion acceptances.

   It is a finite list of record shapes and could be done exactly.

**For the record.** The family's content is Lemma 2.1 plus (IB). Through Prop 3.1 it turns into one condition, (CC), on how departures from T's silence are distributed over worlds relative to the selected family's supports. PP32 is the statement that no additive distribution meets (CC) at the seams. Prop 5.2 is the statement that a mass-sensitive, cross-world distribution does. That is the freedom: it lives in **how a departure's world is chosen**, not in which dominator is chosen. Silent-wedge dominators stay out of the departures' way (Prop 5.4).
