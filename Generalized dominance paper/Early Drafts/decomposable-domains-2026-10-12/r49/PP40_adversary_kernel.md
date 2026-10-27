# PP40. Adversary on PP38's bounded kernel

23 October 2026. Task PP40 of Brief 49. One reader (me); not refereed.

**Labels.** PROVED: complete argument here. CHECKED: exact rational verification (`PP40_py/coherence_scan.py`, `pointwise_exact.py`, both ALL PASS). NUMERICS: Gaussian Monte Carlo (`jump_signs_mc.py`, `r3_window_mc.py`), using my own implementation of ℓ^T (`field40.py`), written from the definition and not copied from PP38's `field38.py`. No proof depends on NUMERICS unless stated. CONJECTURE / OPEN: as stated.

**Inputs.** Brief 49; AUDIT_round49_brief and AUDIT_round49_answers (binding); PP38 (the target); PP37 (Thm 5.1, Props 5.2–5.5, Thm 5.6); REFEREE_PP32_penalties (the field ℓ^T); REFEREE_round48; PP36 (Prop K, Lemma E); LEAD_selection_count (Lemmas A, B, E); AUDIT_completion (rules I–IV, F1/F2). I add no axioms. Every use of PP38's kernel is marked.

**Notation.**
- For a model M and a rival X, A(M, X) := {w : M ⪯_w X}.
- Φ_w(r) := L_w(new) − L_w(old) for the field ℓ^T. "ℓ-positive" means Φ_w > 0, and so on.
- Splice: C[S ↦ D] equals D on S and C elsewhere.
- At the jump: B_n := C_{p_n} ∈ B_ij(t_n), Δ_n := L(B_n) − L(T) ∈ R³, and k is the third world of the edge {i, j}. For bounded E ⊆ Sil(T) ∩ M_k put X_E := T[E ↦ A] and Y_E := B_n[E ↦ S].

---

## 0. Verdict

**The bounded kernel survives every test. PP38's completion does not, as stated.** Item by item:

1. **Kernel (item 1).**
   - **Correct:** Thm 3.1(ii), the coherence lemma (re-CHECKED by a blind method at 177 weights, including weights within 1/300 of u), Cor 4.3, and (CC) at every order on the fragment.
   - **Wrong as stated:** Prop 5.2, the interface for ℓ-negative records. It omits the case "ℓ-positive record + installed record". PP38's own Thm 6.3 triangle is a counterexample. Repaired here with a shadow condition (B3), and I show that the core of (B3) is necessary.
   - **Unbounded rivals: secured only on the fragment.** On the fragment, universal competitiveness against unbounded rivals is free (Prop 1.1: the maximal fragment is the ℓ^T preorder itself). But the milestone forces a jump (PP38 Thm 6.2), and at the jump the ℓ^T preorder fails closed sections at an edge world (Prop 2.3). So in the milestone, PP38 secures universal competitiveness **against bounded rivals only**. For unbounded rivals it is open for T, for the post-jump models, and for every model whose perturbations receive installed dominations.
2. **Jump (item 2).** PP37's tie obstruction does not reach the kernel: the kernel is non-strict, so Thm 5.1 does not apply, and it is unbalanced, so Prop 5.5 does not apply. PP37's junction inequality (Prop 5.4) does transfer to the unbounded layer, and it is exactly what fails at the jump. The jump forces more than PP38 lists:
   - an **inheritance law**: post-jump verdicts are eventually subsets of T's (Lemma 2.1);
   - a **k-inversion**: B_n's retreats Y_E are *strictly better than T at world k* in the relation, against a field gap of about 0.46 (Prop 2.5);
   - an **edge-world ℓ-negative record** at every jump, carried by B_n or **by T itself** (Prop 2.6). PP38 locates the residue only at world k.

   No all-world tie and no contradiction follows from sections, Lemma A and Lemma E. §2.7 states what survives.
3. **Residues (item 3).** I prove a splice form of Prop K (Prop 3.1). Every registered model must defend against every splice C[S ↦ D] of every dominator C. Consequences:
   - **PP38's proposed dominators for the edge models' forced rivals are excluded.** T, V_1, V_2, V_3 and B_13, B_23 away from the vertices cannot dominate small forced rivals of B_12(1). The only clean survivors are B_12(t) with t → 1 (|t − 1| ≲ 0.005 on PP38's ball). These must be ℓ-endorsed at worlds 1 and 2 and installed at world 3 (Thm 3.3).
   - **Fills.** V_j never dominates T's j-fills (PP36 Lemma E(ii), now with a second proof), and T ⋠_j C for every dominator C of a j-fill. A zonoid criterion decides the rest (Prop 3.4).
   - **No forced F1/F2** for the three families together. An F1 is forced only if the ℓ-positive layer keeps the shadows of installed records.

| Item | Finding | Label |
|---|---|---|
| 1 | Thm 3.1(ii), Lemma 4.2, Cor 4.3, (CC) on the fragment correct | PROVED (re-derived); Lemma 4.2 CHECKED independently |
| 1 | Maximal fragment = ℓ^T preorder; universal competitiveness free there; sections ⇔ lower semicontinuity of p ↦ L_w(C_p) | PROVED |
| 1 | PP38 Prop 5.2 false as stated; repaired with (B3); shadow lemma | PROVED |
| 2 | Inheritance Lemma 2.1; no post-jump model near p_0 dominates anything T does not | PROVED |
| 2 | ℓ^T preorder breaks sections at the jump (junction inequality, margin h_0 > 0) | PROVED; h_0 ≈ 0.086 NUMERICS |
| 2 | Splice identity; k-inversion Y_E ≺_k T; T ⋠_k (dominators of Y_E) | PROVED |
| 2 | Edge-world ℓ-negative record at every jump (B_n's or T's) | PROVED given signs; sign map NUMERICS |
| 3 | Splice Prop K (K^S); zonoid form under the kernel | PROVED |
| 3 | R3 localisation: forced rivals of B_12(1) dominated only by B_12(t), t → 1 (or models near V_1, V_2 at extra cost) | PROVED; window NUMERICS |
| 3 | Fills: V_j excluded; T ⋠_j C; survivors' criterion | PROVED |
| 3 | Joint installation of R1–R3 (+ R4, T's own) | OPEN; no F1/F2 forced |

---

## 1. The kernel

### 1.1 What holds (re-derived)

- **Thm 3.1(ii).** Correct. For bounded rivals the only acceptances are the kernel's and guidance's, and guidance records have Φ ≥ 0. The Lyapunov/separation step (PP32 Lemma 2.3) needs only integrability on balls. The nested compact sets Λ_n give λ in the **closed** face Δ_s, so interior-index models may be Bayes at boundary weights (this is how B_ij(t) and V_k enter Cor 4.3).
- **Lemma 4.2 (coherence lemma).** I re-checked it by a method that does not use the proof's kinks. For each weight and each class M_i, I computed the B- and A-boundary functions by bisection on a blind grid of 3,200 triples. I searched for any failure of concavity of b or convexity of a, and verified every hit exactly in rationals: two problems with the same strict-margin Bayes answer whose midpoint has a different unique answer.
  - **CHECKED:** witnesses at all 171 interior weights of denominator 20, and at six weights within 1/30 or 1/300 of u, for ε ∈ {3/10, 1/10}.
  - **CHECKED:** no witness at u.
  - Near u the witness sits at the A-kink s_j ≈ L, as the proof predicts for y_0 near 1/2.
  - The proof's one-line non-adjacency step (B and A never both beat silence) holds because G < F (REFEREE_PP32 §3.2, Fact 1).
- **Cor 4.3** follows. **Uniqueness at boundary weights:** at edge weights the ties lie on threshold rays, and at vertices the Bayes model is the perfect model.
- **(CC) at every order.** Correct on the fragment. B1 is the computation Φ_i(O, S → a) ≥ α_i(F) > 0. B2 holds because N is Bayes at an edge weight with both coordinates positive, so its retreat cannot be ℓ-negative at both edge worlds. Once ℓ-negative records are installed, (CC) survives **iff** no bounded reverse is installed by rule II, i.e. iff the repaired Prop 1.4 below holds.

### 1.2 Unbounded rivals

**Proposition 1.1 (the maximal fragment; PROVED).** Accept a record r at w iff Φ_w(r) ≥ 0, bounded or not. Call this the ℓ^T preorder.
- (a) It satisfies reflexivity, strict (G), (IB) and (TC): it is a total preorder per world.
- (b) Every a.e.-unique ℓ-Bayes model N (in particular every registered model of Cor 4.3) is competitive against **every measurable rival** on supp λ_N ⊆ s(N). N is undominated, and N has no all-world tie with any other model. So F1 and F2 cannot occur, and rules I–IV are inert.
- (c) For a selection on the index domain I, all fixed-rival sections are closed **iff** p ↦ L_w(C_p) is lower semicontinuous on I at every w.

*Proof.*
- (a) Φ_w is additive and record-based, and strict (G) follows from positive penalties.
- (b) For any Y ≠ N, Σ_w λ_{N,w} Φ_w(rec(N, Y)) = ∫ Σ_w λ_{N,w}(ℓ_w(Y) − ℓ_w(N)) dμ > 0 by uniqueness. So some w ∈ supp λ_N has Φ_w > 0. An all-world tie N ≈ Y forces this sum to be 0, hence Y = N.
- (c) A_w(X) = {p : L_w(C_p) ≤ L_w(X)}. As X varies, L_w(X) takes every value in [0, sup] (Lyapunov). Closed sublevel sets at every level is exactly lower semicontinuity. ∎

So on the fragment, PP38's "closed system" can be taken maximal, and then universal competitiveness is free (PP38 states it only for bounded rivals). **The milestone breaks this.** The jump is forced (PP38 Thm 6.2, re-checked), and at the jump lower semicontinuity fails at an edge world (Prop 2.3). Any working completion must therefore:
- **refuse** some ℓ-positive records of the post-jump models at an edge world;
- **accept** ℓ-negative ones elsewhere (§2).

Once records are refused, universal competitiveness against unbounded rivals is no longer automatic for anyone whose defence used them. PP38 gives no replacement. **Verdict on item 1, last question: only bounded rivals are secured.**

### 1.3 PP38 Prop 5.2 is false as stated

Prop 5.2 claims that (B1) compensation and (B2) no mutually inverse installed far parts exclude every failing triangle with exactly one bounded edge. The proof handles the pairs of unbounded edges (guidance, guidance), (guidance, 𝒢), (𝒢, 𝒢), (guidance, installed) and (installed, installed). It omits **(𝒢, installed)**: an ℓ-positive record together with an ℓ-negative installed one.

**Counterexample 1.2 (PROVED).** Let r = rec(C, Z) be installed at v with Φ_v(r) = −δ < 0, compensated, and the only installed record. Then (B1) and (B2) hold. Put Q := Z[F ↦ contradiction] with F bounded and ∫_F (penalty increase) < δ. Then g := rec(Q, C) is unbounded with Φ_v(g) = δ − ∫_F (…) > 0, so Thm 5.1 allows g ∈ 𝒢_v. The triangle C ⪯_v Z ⪯_v Q ⪯_v C is accepted, its bounded edge is a strict guidance step, and the reverse Q ⪯_v Z is refused. (TC) fails, and rule II would install the reverse: **F1**.

PP38's own Thm 6.3 triangle (B_n, X, X[F ↦ contradiction]) is this instance, so the note contradicts itself.

**Lemma 1.3 (shadow lemma; PROVED; axioms only).** Let C ⪯_v Z be accepted. Let Q be any model with Z ⪯_v Q accepted and Q ⪯_v Z refused. Then Q ⪯_v C must be refused. (Proof: otherwise the triangle C, Z, Q lacks a reverse.) Under the kernel, when Q is a bounded perturbation of Z, the records rec(Q, C) forbidden this way have ℓ-values filling (−∞, δ). So every installed record with deficit δ forbids the ℓ-positive records with inverse far part and value in (0, δ).

**Proposition 1.4 (repaired interface; PROVED).** Add to (B1) and (B2):

**(B3)** at each world v, no accepted ℓ-positive unbounded record has far part inverse to the far part of a record installed at v.

Then no accepted triangle with exactly one bounded edge fails (TC).

*Proof.* The remaining pair (𝒢, installed) needs far(g) = far(r)⁻¹, which (B3) excludes. The other pairs are as in PP38, with one gloss on (guidance, guidance): two weak worsenings with inverse far parts have identical ranks there, because ranks are injective at a world, so the far part is trivial. ∎

By Lemma 1.3, (B3) is not optional in its core range. Its cost is exactly a set of refused ℓ-positive records: shadows. §3 shows whose defences fall in them.

---

## 2. The jump

Setting: PP38 Thm 6.2. p_0 ∈ Φ_T ∩ P is a boundary point. It is interior by Lemma E and exists by Lemma A. Take p_n → p_0 with C_{p_n} not tied to T and C_{p_0} = T. The equality C_{p_0} = T holds in the kernel fragment, where registered models have no ties. If installed records create a tie, replace T by C_{p_0} throughout.

### 2.1 Inheritance

**Lemma 2.1 (PROVED; axioms + milestone).** For every measurable rival X there is N(X) such that ∅ ≠ A(B_n, X) ⊆ A(T, X) for all n ≥ N(X).

*Proof.* If T ⋠_w X, then p_0 ∉ A_w(X). This set is closed, so it misses a neighbourhood of p_0. Nonemptiness is competitiveness on supp p_n = {1, 2, 3}, since p_n is interior near p_0. ∎

**Corollary 2.1a (PROVED).** If T does not dominate X, then for n ≥ N(X) no B_n dominates X. So **every repair-class rival that T fails to dominate gets no dominator from the post-jump models near p_0**: not T's fills, not B_n's own retreats (§2.5), not vertex rivals.

### 2.2 The margin

**Lemma 2.2 (PROVED; NUMERICS for values).** Put h(t) := Σ_w λ_w(t)(L_w(T) − L_w(B_ij(t))). Then inf_{t ∈ [0, ∞]} h(t) =: h_0 > 0.

*Proof.* h(t) > 0 by uniqueness of the λ(t)-Bayes model, since T ≠ B_ij(t) on Sil(T) ∩ M_k. t ↦ L_w(B_ij(t)) is continuous: the thresholds F⁻¹(t) and G⁻¹(t) are continuous, the disagreement wedges vanish, and the envelope is integrable. As t → ∞ or 0, B → V_i or V_j and h → L_i(T) − L_i(V_i) = L_i(T) > 0 (or the same at j). So h is a positive continuous function on [0, ∞]. ∎

NUMERICS (`jump_signs_mc.out`): h_0 = 0.101, 0.086, 0.063, 0.012 for ε = 0.1, 0.3, 0.5, 0.9, attained at t = 1.

### 2.3 Transfer of PP37's obstruction

| PP37 result | In PP38's setting | Why |
|---|---|---|
| Thm 5.1 (strict zero rule impossible) | does not apply to the kernel | K_ℓ accepts Φ = 0 at every world (symmetric zero rule) |
| Prop 5.5 (symmetric everywhere ⇒ F2) | **blocked** (PROVED) | a bounded all-world tie needs Φ_w(T → X) = 0 at every w, but Σ_w Φ_w(T → X) > 0 for X ≠ T (unique u-Bayes) |
| Props 5.2/5.3 (regularity, iso-level) | no iso-level constraint on the kernel | the kernel is not shared balanced levels; the analogue is Lemma 2.1 |
| **Prop 5.4 (junction inequality)** | **applies to the unbounded layer**: Prop 2.3 | — |

**Proposition 2.3 (no field-monotone edge layer at the jump; PROVED).** Suppose that for all large n, every record out of B_n with Φ_w > 0 is accepted at w, for both w ∈ {i, j}. Then sections are not closed at p_0.

*Proof.*
1. By Lemma 2.2, max_{w ∈ {i,j}} (L_w(T) − L_w(B_n)) ≥ h(t_n) ≥ h_0.
2. Pass to a subsequence on which the maximum is at one world w.
3. Let X := T[F ↦ w-correct] with F ⊆ Sil(T) ∩ M_w bounded and α_w(F) < h_0. Then Φ_w(rec(B_n, X)) = L_w(T) − α_w(F) − L_w(B_n) > 0, so every B_n accepts X at w.
4. Closedness gives T ⪯_w X. But X is a pure w-improvement of T. ∎

In the language of Prop 1.1(c): **the jump is a failure of lower semicontinuity of the loss profile at an edge world.** B_n is ℓ-better than T there by at least h_0. PP38's world-k residue is the *consequence* of repairing this by refusals: once i and j are refused, competitiveness pushes B_n to k.

### 2.4 Which edge models can sit at the jump

**Proposition 2.4 (PROVED; CHECKED (a)).**
- **(i)** B_ij(1) is pointwise no better than T at world k, and strictly worse on Sil(T) ∩ M_k. Hence B_ij(1) ≠ B_n for n ≥ N(X_E): at k it refuses X_E by strict (G), and at i and j by Lemma 2.1.
- **(ii)** For t ≠ 1, B_ij(t) is strictly k-better than T on a non-null cone R_t. This is the compensation that (B1) needs, and its mass → 0 as t → 1.

*Proof of (i)* (edge 12, k = 3). On M_1 (chart s_2, s_3):
- B_12(1) says B iff s_2 < 1/L, S iff 1/L ≤ s_2 ≤ L, and A iff s_2 > L.
- T says B only on Q ⊆ {s_2 < 1/L}, and A where s_2 + s_3 > L (which includes s_2 > L).

So wherever B_12(1) has rank 1 or 0 at world 3, T has rank ≤ that. M_2 is symmetric. On M_3, B_12(1) says A, which is 3-wrong. ∎

CHECKED (`pointwise_exact.out`): 19,900 rational problems, strict on all 2,563 samples in Sil(T) ∩ M_3. Exact R_t witnesses for t ∈ {1/2, 9/10, 11/10, 2}. NUMERICS: μ(R_t) = 0 at t = 1, 3.9·10⁻⁴ at t = 0.9, 1.9·10⁻² at t = 2.

### 2.5 The splice identity and the k-inversion

**Lemma 2.5a (splice identity; PROVED, (IB)).** For any models D, C and any set S,

  rec(D, C[S ↦ D]) = rec(D[S ↦ C], C) = ({D ≠ C} ∖ S, D → C).

So D ⪯_w C[S ↦ D] and D[S ↦ C] ⪯_w C are one verdict.

Apply this with D = B_n, C = T, S = E: **B_n ⪯_k X_E is the same record as Y_E ⪯_k T**, since B_n = A on E and T is silent there.

**Proposition 2.5 (k-inversion; PROVED; axioms + milestone).** Let E_0 ⊊ E′ ⊆ Sil(T) ∩ M_k be bounded, with E′ ∖ E_0 non-null, and let n ≥ max(N(X_{E_0}), N(X_{E′})). Then:
- **(a)** Y_{E′} ⪯_k T and T ⋠_k Y_{E′}, so **Y_{E′} ≺_k T**;
- **(b)** T ⋠_k D for every D with D ⪯_k Y_{E′}, in particular for every dominator of Y_{E′};
- **(c)** T must defend against Y_{E′} at i or j. By Lemma 2.5a, T ⪯_w Y_{E′} ⟺ X_{E′} ⪯_w B_n. Since B_n ⋠_w X_{E′} (Lemma 2.1), T's defence world w ∈ {i, j} gives X_{E′} ≺_w B_n.

*Proof.*
- (a) Y_{E′} ⪯_k T is the copy of the forced B_n ⪯_k X_{E′} (PP38 Thm 6.3(a)). If T ⪯_k Y_{E′}, then T ⪯_k Y_{E′} ⪯_k Y_{E_0} ⪯_k T. The middle step is guidance: Y_{E_0} has A, which is k-wrong, on E′ ∖ E_0. The last step is the copy of B_n ⪯_k X_{E_0}. The reverse Y_{E_0} ⪯_k Y_{E′} is a strict guidance reversal, so (TC) fails.
- (b) D ⪯_k Y_{E′} ⪯_k T ⪯_k D would need the reverse T ⪯_k Y_{E′}, which (a) refuses.
- (c) is Lemma 2.5a with Lemma 2.1. ∎

**Reading.** At world k the relation ranks B_n's retreat strictly above T. The field says the opposite, by Δ_{n,k} − β_k(E′) ≥ 0.46 − β_k(E′) (NUMERICS: Δ_3 ≥ 0.463 on every t, my implementation; PP38 reports ≥ 0.44 after 4 s.e.). On the pair (B_n, X_{E′}) the relation and the field disagree at two worlds whenever T's defence world w has Δ_{n,w} < 0.

### 2.6 The residue is not confined to world k

**Proposition 2.6 (PROVED given strict signs of Δ_{n,i}, Δ_{n,j}; NUMERICS for which case occurs).** For n large, at least one of the following holds.
- **(a) B_n carries it.** If Δ_{n,w} > 0 for some w ∈ {i, j}: for F ⊆ Sil(T) ∩ M_w bounded with β_w(F) < Δ_{n,w}, the rival T[F ↦ A] satisfies A(T, ·) = {w}: Φ_w = β_w(F), and the other two values are −α < 0, since A is correct at the other worlds. So B_n ⪯_w T[F ↦ A] is forced (Lemma 2.1), with Φ_w = β_w(F) − Δ_{n,w} < 0.
- **(b) T carries it.** If Δ_{n,i} < 0 and Δ_{n,j} < 0: T's forced defence against Y_{E′} (Prop 2.5(c)) is at i or j, with Φ_w(T → Y_{E′}) = Δ_{n,w} + α_w(E′) < 0 for E′ small. So **a registered model's own defence must go against the field.**

NUMERICS (`jump_signs_mc.out`, ε = 0.3, 4 s.e.): the double-loss set I_2 = {t : Δ_1 < 0, Δ_2 < 0} spans t ∈ [0.65, 1.55]. It contains t = 1 for every ε tested (ε = 0.1: [0.70, 1.40]; ε = 0.5: [0.60, 1.70]; ε = 0.9: [0.50, 1.80]). Outside I_2, case (a) applies.

So whatever t* = lim t_n is, the jump needs an ℓ-negative record at an edge world as well as PP38's at k. Case (b) is a **fourth residue family (R4): T's own defences**. It is absent from PP38's list and occurs iff t* ∈ I_2. Choosing t* ∉ I_2 avoids R4 but not (a). That choice is a *chosen geometry*.

### 2.7 Tie or contradiction?

I found neither. Attempts:
- (i) Triangles among T, B_n and bounded perturbations of T need an acceptance into B_n from an unregistered model. Such acceptances can be refused, and guidance never forces them for t ≠ 1 (R_t is a cone).
- (ii) Triangles T ⪯_w B_n ⪯_w X ⪯_w T force only Φ_w(T → X) = 0 and then B_n ≈_w T. Since Σ_w Φ_w(T → X) > 0, B_n can always pick another world of A(T, X).
- (iii) Diagonal subsequences give ∅ ≠ A(B_n, B_m) ⊆ A(T, B_m) ⊊ {1, 2, 3} for m < n. This is consistent.
- (iv) Lemma A and Lemma E are used only to place p_0, and Lemma B to exclude vertex models.

**CONJECTURE 2.7.** The constraints of §§2.1–2.6, together with (TC) and (B1)–(B3), are jointly satisfiable at one jump for a fixed edge family. I have no proof. The surviving freedom is stated in §5.

---

## 3. The residue records

### 3.1 A splice form of Prop K

**Proposition 3.1 (K^S; PROVED; (IB), (TC), and D's universal competitiveness).** Let D be registered, C any model, S any set, and Z a rival with C ⪯_i Z and Z ≺_i D[S ↦ C]. Then D ⋠_i C[S ↦ D].

*Proof.* By Lemma 2.5a, D ⪯_i C[S ↦ D] is the verdict D[S ↦ C] ⪯_i C. The triangle D[S ↦ C] ⪯_i C ⪯_i Z ⪯_i D[S ↦ C] then lacks the reverse D[S ↦ C] ⪯_i Z. ∎

PP36 Prop K is the case S = ∅. In addition, D ⋠_i C[S ↦ D] whenever C[S ↦ D] ≺_i D by strict (G), i.e. on the set G(C, D) := {i : C ≤_i D pointwise}.

**Corollary 3.2 (kernel form: a zonoid criterion; PROVED).** Let Z = D·z be a bounded perturbation of D with value vector z := Φ(D → Z), and let C ⪯_v Z for every v ∈ s(D) (for instance a dominator). Put d(S) := Φ(D → D[S ↦ C]) for bounded S disjoint from supp z. D can remain competitive against every splice C[S ↦ D] only if, for every bounded S, some v ∈ s(D) ∖ G(C, D) has d_v(S) ≤ z_v.
- If a single world v survives, the condition is ∫(ℓ_v(C) − ℓ_v(D))⁺ dμ ≤ z_v.
- **Sufficient:** C is μ-Bayes for some μ ∈ Δ_{s(D) ∖ G(C,D)} with μ·z ≥ 0 (then μ·d(S) ≤ 0 ≤ μ·z).

*Proof.* Under the kernel, Z ≺_v D[S ↦ C] iff Φ_v(Z → D[S ↦ C]) = d_v(S) − z_v > 0. ∎

This is the audit's "actual simultaneous allocation" requirement, made concrete. A dominator must leave each registered model a defence world not only against itself (Prop K) but **against each of its splices into that model**. One dominator serving several rivals of D must leave a world for each S against the union of their kill sets.

### 3.2 R3: the edge models' forced rivals

Let N = B_12(1) (s = {1, 2}). Let Z′ = N[G′ ↦ S, E′ ↦ B] with E′ ⊆ G′ ⊆ Sil(T) ∩ M_3 bounded, so z_1, z_2 > 0 and z_3 < 0.

**Theorem 3.3 (localisation; PROVED, for registered geometry under the ℓ^T kernel and N universally competitive).**
- **(a) T is excluded.** Take P_1 ⊆ M_1 ∩ {1/L < s_2 ≤ γL, s_2/L + G(s_3) > 1}, where N = S and T = A, and P_2 its mirror in M_2, with equal |g|-mass m (γ < 1). Each change S → A costs N at its own world (+|g|) and gains at the other (−|g|·s/L ≥ −γ|g|). So d(P_1 ∪ P_2) ≥ m(1 − γ)(1, 1). If z_1, z_2 < m(1 − γ), worlds 1 and 2 are both killed, and N is not competitive against T[P_1 ∪ P_2 ↦ N]. So **T dominates no small forced rival of N.**
- **(b) V_1, V_2 are excluded.** V_1 ≤_1 N pointwise, so G(V_1, N) = {1}. On W_12 every change N → V_1 is a 2-worsening, so the condition is L_2(V_1) ≤ L_2(Z′). This fails unless z_2 ≥ L_2(V_1) − L_2(N) ≈ 0.72 (NUMERICS). V_2 is symmetric.
- **(c) V_3, B_13(s), B_23(s) are excluded for small Z′.** Each says S or B on a non-null Q_s ⊆ M_3, where N says A. Every change there costs N at worlds 1 and 2, so d(Q_s) > 0 coordinatewise, and a small Z′ is killed. The threshold κ(s) is positive and bounded below on compact ranges of s. But κ(s) → 0 as B_13(s) → V_1 or B_23(s) → V_2. Near the vertices, these models escape K^S only by making **N** accept ℓ-negative defences against their splices: L_1(B_13(s)) ≈ L_1(V_1) < L_1(N).
- **(d) The B_12 family.** For t > 1, B_12(t) ≤_1 N pointwise: its 1-correct region grows and its 2-correct region shrinks. So world 2 must survive for every S, which forces **L_2(B_12(t)) ≤ L_2(Z′)**. World 1 is automatically ℓ-positive. So **the domination is ℓ-endorsed at both edge worlds**, and admissible t form a window around 1 that shrinks to {1} with Z′. t < 1 is the mirror case. t = 1 is N itself, which refuses Z′ at 3.

*Proof.* (a)–(d) are Prop 3.1 and Cor 3.2 with the stated sets. In (d), d_2 ≥ 0 pointwise on the wedge (opposite rank changes on W_12, strictly guiding field), so sup_S d_2(S) = L_2(B_12(t)) − L_2(N). ∎

NUMERICS (`r3_window_mc.out`; PP38's ball, centre (1, 1, −1.9), radius 0.2, E′ = G′):
- z = (7.5, 7.5, −10.5)·10⁻⁴;
- admissible t: 1.002 yes, 1.005 no; 0.995 yes, 0.980 no;
- for every admissible t, L_3(B_12(t)) − L_3(Z′) ≈ +1.1·10⁻³ > 0, so **the domination must be installed, ℓ-negative, at world 3**;
- census: B_12(t) ≤_1 N pointwise (t > 1) on 2·10⁶ samples.

**Consequence for PP38 §8 item 1.** It proposes "T and the B_13/B_23 families" as the natural dominators of Z′. T is excluded outright. B_13 and B_23 are excluded except arbitrarily near V_1 and V_2, where they create a new N-side residue. The clean freedom is an edge-local repair: Z′ is dominated by B_12(t_{Z′}), with t_{Z′} → 1, installed at world 3. Whether this recursion closes along the edge (each B_12(t)'s forced rivals dominated by B_12(t′) with t′ near t) is **CONJECTURE 3.3′**.

### 3.3 R2: T's fills

Let X = T[G ↦ V_j] with G ⊆ Sil(T) ∩ M_j small, so z = (−α_j(G) at j, +β_w(G) at w ≠ j).

**Proposition 3.4 (PROVED).**
- **(a)** T ⋠_j C for every dominator C (Prop K: X ≺_j T).
- **(b)** V_j is not a dominator. G(V_j, T) = {j}. Choose S ⊆ (Sil(T) ∩ M_j) ∖ G near the A-boundary, where F is large, with ∫_S |g_j| < ∫_G |g_j| but ∫_S |g_j|F(s_w) > ∫_G |g_j|F(s_w) for both w ≠ j (the ratio of F between the two boundaries is about 5 at ε = 0.3). Then d(S) > z at every world. This is PP36 Lemma E(ii), now also forced by K^S.
- **(c)** A μ-Bayes C with μ_j < 1 passes Cor 3.2 whenever μ·z ≥ 0. For μ supported off j (edge models B_ww′ opposite j) this always holds.
- **(d)** Each dominator's served fills must leave T a world for every splice. One C serving fills of all three classes kills T's defence against C itself (S = ∅): T ⋠_j C for each j.

So R2 is not obstructed. Its survivors are mainly edge models whose edge avoids j. By PP38 Thm 6.5 they are ℓ-negative somewhere, and by Lemma 1.3 each such installed record strips T's ℓ-positive defences, at that world, against the dominator's splices.

### 3.4 Installing R1–R4 together

The constraints any joint installation must meet:
- **(TC) interface:** (B1), (B2), (B3) (Prop 1.4). (B3) forbids the shadows.
  - At the jump, the shadows are T's ℓ-positive k-defences against B_n-splices; this is what produces Prop 2.5.
  - For fills, they are T's defences against dominator splices (Prop 3.4).
  - For R3, they fall on N's records at world 3, which is outside N's support, so they are harmless.
- **Sections at p_0:** Lemma 2.1 for every rival. In particular, dominators of rivals T does not dominate come from away from p_0 (Cor 2.1a).
- **K^S** for every registered model, every dominator, and every splice (Prop 3.1), including *new* defenders, retroactively, as in PP37 Cor 6.3.
- **(IB) identities** (Lemma 2.5a). Every installed domination of a splice of a registered model is simultaneously a defence verdict of that model.

**F1/F2.**
- F1 is forced exactly when an ℓ-positive record in a shadow is kept (Counterexample 1.2).
- F2 would need an all-world tie with an incoherent model. In the kernel no bounded all-world tie exists (§2.3). Unbounded ties arise only through installed records in both directions, which (B2) excludes.
- I found no configuration of R1–R4 that forces F1 or F2 once shadows are refused. **OPEN.**

---

## 4. Classification

| Failure | Source | Label |
|---|---|---|
| Prop 5.2 as stated | an error in PP38 (missing case); repaired by (B3) | PROVED |
| Maximal (field-monotone) unbounded layer breaks sections at the jump | **axioms + milestone** (closed sections, strict (G), a path to an edge) given the **optional commitment** "single-field bounded kernel", which fixes the registrable geometry (Cor 4.3) and so forces the jump (Thm 6.2) | PROVED |
| Inheritance; post-jump models near p_0 dominate nothing T does not | axioms + milestone | PROVED |
| k-inversion Y_E ≺_k T; T ⋠_k dominators of Y_E | axioms + milestone, given that the post-jump models say A on a non-null part of Sil(T) ∩ M_k (true for every edge-family model: the kernel's geometry) | PROVED |
| Edge-world ℓ-negative record at every jump | kernel field (optional commitment); case (b), T's own, is **chosen geometry** (t* ∈ I_2) | PROVED; signs NUMERICS |
| B_12(1) never at the jump | axioms + milestone + ℓ^T geometry | PROVED |
| T, V_1, V_2, V_3, B_13, B_23 (off the vertices) cannot dominate small forced rivals of B_12(1) | **axioms** (K^S, strict (G)) + universal competitiveness of N + the kernel's verdicts on bounded records | PROVED |
| R3 dominations ℓ-negative at world 3 | the kernel field | NUMERICS |
| V_j cannot dominate T's j-fills | axioms (PP36 Lemma E(ii); K^S) | PROVED |

Nothing above makes the bounded kernel impossible. The milestone fails PP38's *completion* at two named places: (i) the unbounded layer at the jump and (ii) the dominator supply. Both are now constrained much more tightly than PP38 states.

---

## 5. The freedom that survives, and the next step

**Surviving freedom (all tests above).** Fix the ℓ^T bounded kernel. A completion of the milestone may choose, and must choose:
1. **At the jump.**
   - A limit edge parameter t* ≠ 1.
   - For each rival X, eventual post-jump verdicts that are a nonempty subset of T's verdict set A(T, X).
   - Refusals of the ℓ-positive records forbidden by Prop 2.3 and Lemma 1.3.
   - The k-inversion of Prop 2.5.
   - The edge-world ℓ-negative records of Prop 2.6: B_n's if t* ∉ I_2, T's if t* ∈ I_2.
2. **For R3.** Dominators B_12(t) inside the window L_{w*}(B_12(t)) ≤ L_{w*}(Z′), with w* = 2 if t > 1 and w* = 1 if t < 1. They are ℓ-endorsed at 1 and 2 and installed at 3. Alternatively, near-vertex B_13 or B_23 dominators, paid for by ℓ-negative defences of N.
3. **For R2.** Dominators passing Cor 3.2 (for example, edge models opposite j), installed where ℓ-negative, with T's shadowed defences moved to other worlds.
4. **Throughout.** (B1)–(B3) and K^S for every registered model.

**Most important next step.** Test CONJECTURE 3.3′ first. It is one edge family, one world (3) of installation, no T-shadow, and a one-parameter recursion t → t′. If the edge family closes under its own forced rivals with world-3 installs satisfying (B2), R3 is solved for all generations. Then return to the jump, and choose t* ∉ I_2 so that T carries no residue.

---

## 6. Status and scripts

| Result | Label |
|---|---|
| §1.1 re-derivations; Lemma 4.2 independent check | PROVED; CHECKED |
| Prop 1.1 (maximal fragment); Counterexample 1.2; Lemma 1.3; Prop 1.4 | PROVED |
| Lemma 2.1, Cor 2.1a, Lemma 2.2, Prop 2.3, Prop 2.4, Lemma 2.5a, Prop 2.5 | PROVED; h_0 and μ(R_t) NUMERICS; Prop 2.4(i) CHECKED |
| Prop 2.6 | PROVED given signs; I_2 NUMERICS |
| Conj 2.7, Conj 3.3′; joint installation §3.4 | CONJECTURE / OPEN |
| Prop 3.1, Cor 3.2, Thm 3.3 (a)–(d), Prop 3.4 | PROVED; R3 window and world-3 sign NUMERICS |

**Scripts** (`r9/PP40_py/`; run `python3 -I -B <script> > <script>.out` inside the folder):

| Script | Content | Label |
|---|---|---|
| `field40.py` | independent implementation of ℓ^T, T, the Bayes models and the edge family | library |
| `coherence_scan.py` → `.out` | blind non-convexity search with exact verification: 177/177 weights ≠ u incoherent (ε = 3/10, 1/10), none at u. ALL PASS | CHECKED |
| `pointwise_exact.py` → `.out` | B_12(1) ≥_3 T pointwise (19,900 problems); exact R_t witnesses for t ≠ 1; jump sign facts. ALL PASS | CHECKED |
| `jump_signs_mc.py` → `.out` | Δ_w(t) for 50 values of t and four ε; h(t) and h_0; I_2; μ(R_t); u-Bayes = T sanity check (0 mismatches) | NUMERICS |
| `r3_window_mc.py` → `.out` | Theorem 3.3(d): pointwise census, admissible window on PP38's ball, world-3 sign | NUMERICS |
