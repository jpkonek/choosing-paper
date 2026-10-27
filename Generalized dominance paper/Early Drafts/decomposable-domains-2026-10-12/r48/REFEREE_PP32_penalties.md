# Referee report on PP32 (the additive barrier), and what changes under general penalties (PP35)

22 October 2026. One referee (me). Labels: PROVED (full argument here), CHECKED (exact rational computation, script named), NUMERICS (floating point), CONJECTURE / OPEN. "Field" means a per-problem, per-world penalty. Scripts are in `r9/PP35_py/`. Run each with `python3 -I -B <script>`. Each writes a `.out` file and ends with ALL PASS.

## 0. Summary

**Part 1: PP32 as written (rank-linear endorsement).** Every claim is correct or correct after a small repair. Nothing is wrong inside its stated scope. All four scripts re-run with output identical to the `.out` files in the folder. Section 1 lists the repairs. Two of them matter:

- **Vocabulary.** In the project's language, "additive" means a general strictly guiding penalty: v3, eq. (local-penalties); *The Contamination Triangle*, §2. PP32 proves its results only for rank-linear fields, and several of its titles say "additive". Read with the project's meaning, Cor 3.3 ("additive endorsement forces precision") is false. A known additive (S)-system selects imprecise interior hexagons (§3.3).
- **FF2 comparison.** The remark that Cor 5.2 "is FF2 Thm 4.1's conclusion without continuity in measure" overstates the scope. FF2 Thm 4.1 covers every strictly guiding field. PP32 covers rank-linear fields only.

**Part 2: general penalties.** Write α_w = ℓ_w(silent) − ℓ_w(correct), β_w = ℓ_w(wrong) − ℓ_w(silent), and γ_w = ℓ_w(contra) − ℓ_w(wrong), all > 0.

**(a) Do Theorem 3.1 and Cor 3.3 extend?**
- **In general they fail** (PROVED, CHECKED).
  - Theorem 3.1: the field ℓ^T of §3.2 meets every hypothesis of Thm 3.1, with ℓ^T-endorsement in place of ρ-endorsement. Its conclusion fails: T1 is the exact unique u-Bayes model, and the edge Bayes models form a coherent edge selection with closed sections.
  - Cor 3.3: the normalised-box abstention field of *Coverage after Neutral Abstention*, eqs. (3)–(4), is a complete (S)-system satisfying all Brief-48 axioms. Its selected model at u is an interior hexagon.
- **They hold for a subclass** (Theorem A, PROVED). They extend verbatim when silence is weakly costlier than the geometric midpoint on the seam pieces:

    (H4)  α_1 α_2 ≥ β_1 β_2  a.e. where the edge model is silent.

  This class contains rank-linear fields (α = β) and every field with α_w ≥ β_w.
- **One local statement holds for every field** (Cor A′, PROVED). Every selected non-vertex edge model must have its silent window reach an end of the band J. So no precise edge model D_r with τ_r ∈ J can be selected. ℓ^T shows this is sharp.
- **The lead's diagnosis is half right.** Where an edge model *answers*, the edge sandwich does constrain exactly the ratios the majority fill uses: β_1 against α_2, and β_2 against α_1. The failure is on the edge model's own *silent window*. There, optimality of silence gives the inequalities in the wrong direction unless (H4) holds. It is not an "α+β versus α/β" mismatch.

**(b) Can a single general field select an imprecise interior model, or T1 itself?**
- **Imprecise interior models: yes.** But this is **not new**. It is the normalised-box coverage already in *Coverage after Neutral Abstention* (eqs. (3)–(4)) and v3 `thm:general`, and the Contamination Triangle's "gauge mixtures cover hexagons and 9-gons arbitrarily close to T1".
- **T1: no.**
  - The obvious candidate fails. |g_w| densities with constant silence fractions produce normalised boxes, whose sides pass through simplex vertices. T1's sides do not, so no such box is T1 (PROVED).
  - T1's silent set *is* the abstention region of an additive rule at one weight: ℓ^T, and also DESIGN_MEMO §7's ℓ^m. But the induced family has an incoherent interior Bayes model (CHECKED, exact). So it is not an (S)-system.
  - No general additive (S)-system selects T1. This is already proved in the project:
    - *Contamination Triangle* Thm `main` / Cor `coverage` (refereed twice) for abstention-type (non-adjacent) fields;
    - Q4.2 / M3.10′ (CC3 referee; HH1 repair, valid under (TC)) for every strictly guiding field on the full domain;
    - FF2 Thm 4.1 under continuity in measure.
  - §4.3 gives a short independent proof for regular abstention fields, as a cross-check.

**So there is no major finding.** The positive half of the lead's suspicion is correct but already known. The negative half is correct for the local theorems (3.1, 3.3, 5.2). The conjecture PP32 was written to prove (Cor 3.2, T1 not single-field endorsable) remains true for general fields, but only by global arguments: interior coherence at other weights. PP32's local seam route cannot reach it.

---

## 1. Referee report on PP32, claim by claim

| Claim | Verdict | Notes |
|---|---|---|
| Lemma 1.1 | **correct with repair** | (i) Sharpness: "t′ = 1 − t + η, small η" needs t′ > 0. For t ∈ [1, β), take η ∈ (t−1, ε/c), which is non-empty exactly because t < β. (ii) and (iii) re-derived; c/(1−c) = c/(2c+ε) holds since 1 − c = 2c + ε. |
| Lemma 2.1 | correct | (i) uses that X ≺_w C means not C ⪯_w X (strict part). (ii) is fine, including m = e_3. |
| Lemma 2.2 (1-D edge KKM) | correct | S_1 ∪ S_2 = E, using Lemma B at the vertices. e_1 ∉ S_2 because D_r ≺_2 V_1 (D_r is 2-correct on W_12 ∩ {θ>τ_r}, equal elsewhere). For r ∉ K the threshold comparison at world 2 (or 1) re-derived. |
| Lemma 2.3 | correct | Lyapunov splice plus separation. Needs ρ_w integrable on Q, as stated. It holds verbatim for any field ℓ (used below). |
| Prop 2.4 | correct | κ = a/b, with a, b > 0 by the unique 1-correct minimiser when b = 0. The costs 2bρ_2, 2aρ_1, aρ_1+bρ_2 re-derived. |
| Cor 2.5 | correct | The intervals [s_n, i_n] nest. F(θ−) ≤ φ ≤ F(θ+) a.e. Level sets of θ are null. Uses closed sections for D_r for every r, which (S) supplies. |
| Theorem 3.1 | **correct** (improvable) | Every step re-derived. **Improvement:** (H3) can be weakened to "T is competitive on the support of its index (any non-empty set)". The fill is negative at *all three* worlds, so whichever world accepts it gives the contradiction. This removes the interior-index argument entirely. |
| Cor 3.2 | **correct with repair** | The list "not used: strict (G) at world 3" is right only with the weakened (H3) above. PP32's own derivation of (H3) uses strict (G) at the worlds of every edge. With the repair, Cor 3.2 needs strict (G) only at worlds 1 and 2, plus Lemma B at e_1, e_2. |
| Lemma 3.4 | correct | (i) The small rotation about x ∈ relint K is needed only when K is a segment parallel to the edge opposite e_k. (ii) The exclusion "e_k on the affine line of K" is exactly what transversality needs. |
| Cor 3.3 | **correct with repair; mislabelled** | The proof is right for rank-linear fields. Two repairs: (1) Title and wording must say *rank-linear*: for general strictly guiding fields the statement is false (§3.3). (2) The next sentence ("imprecise selected models can only sit on edges") needs the version for non-singleton K meeting int Δ. The same proof works, because x ∈ relint K ⊆ int Δ, and a convex K ⊆ ∂Δ lies in one edge. |
| Prop 4.1 | correct | Needs ρ integrable on Sil(T), an unbounded cone. Localising to bounded pieces costs nothing. |
| Example 4.2 | correct | |
| Example 4.3 | correct (as a local statement) | The added sentence "the argument is valid under null level sets of φ, ψ" is **not proved**. Label it CONJECTURE or delete it. |
| Theorem 5.1 | correct | (b): the swap values (y−x, ≤(Λ−δ)x−(Λ+δ)y) re-derived. λ_w > 0 comes from Prop 4.1, step 3. |
| Cor 5.2 | **correct; reading overstated** | The proof is correct, including the end cases τ_0 ∈ {α, β}. The sentence "this is FF2 Thm 4.1's conclusion … without continuity" is wrong in scope: FF2 covers all strictly guiding fields, Cor 5.2 only rank-linear ones. With 𝒩 = ∅ the field ℓ^T of §3.2 violates the general-field analogue. |
| §6.1 restrictions | correct | |
| §6.2, Prop 6.1 | correct | "Every threshold swap out of D_r is S_0-endorsed" is PROVED, not just a NUMERICS control: D_r is S_0-Bayes at (r_1, r_2). OPEN status agreed. |
| §6.3 lexicographic stacks | correct | Positive leading level, and positive later level after vanishing earlier levels: both re-derived. The claim that this "covers PP23's Ω-lex and PP25's L" was not checked by me (UNCLEAR). The region-dependent case is OPEN, agreed. |

**Scripts (re-run).** `seam_geometry`, `edge_covering`, `union_escape` and `seam_witness_mc` all end ALL PASS, and their outputs are byte-identical to the stored `.out` files (copies in `PP35_py/rerun_PP32/`). The Monte Carlo values match the note: swap −0.002485/−0.002489, fill ≈ −0.00028 at all three worlds. I read each script against its claim. `T_answer` uses min/max over M = c𝟙 + εΔ correctly, and `edge_covering` tests the right world in each case.

**Global recommendation for PP32.** Replace "additive" by "rank-linear" in the title, in §0 ("additive endorsement forces precision", "where non-additivity must live") and in §§5–7. Add a scope paragraph pointing to §§2–3 below.

---

## 2. Notation for general fields

On a mixed problem in class M_i (i the odd world), put s_j := |g_j|/|g_i| (j ≠ i); on W_12, θ = θ_12 = |g_2|/|g_1|. At weights λ, relative to the all-correct baseline, on M_1 with g = (+, −, −):
- accepting g (the minority answer) beats silence iff λ_1 α_1 > λ_2 β_2 + λ_3 β_3;
- accepting −g (the majority answer) beats silence iff λ_2 α_2 + λ_3 α_3 > λ_1 β_1.

Contradiction is never optimal, since γ > 0. The pair is **non-adjacent**, in the sense of the Contamination Triangle §2, iff these two half-planes do not overlap in int Δ. Comparing their intercepts on the two edges, that is iff α_1α_2 ≤ β_1β_2 and α_1α_3 ≤ β_1β_3. These are the *abstention* fields: silence is cheap.

Rank-linear fields (α = β) sit on the boundary. (H4) is the opposite inequality on the seam pair.

---

## 3. Question (a): Theorem 3.1 and Cor 3.3 under general penalties

### 3.1 What survives: Theorem A and Corollary A′

**Pointwise lemma (PROVED; CHECKED in `general_seam_algebra.py`, 200,000 random instances).** On W_12 at edge weights (a, b) with a, b > 0, let κ = a/b. The costs are:
- 1-correct: b(α_2+β_2);
- 2-correct: a(α_1+β_1);
- silence: aα_1 + bα_2.

Then:
- **(i)** If 2-correct is optimal, then α_2 ≥ κβ_1.
- **(ii)** If 1-correct is optimal, then β_2 ≤ κα_1.
- **(iii)** If silence is optimal, then aα_1 ≤ bβ_2 and bα_2 ≤ aβ_1. With (H4) this gives α_2 ≥ β_1β_2/α_1 ≥ κβ_1 and β_2 ≤ α_1α_2/β_1 ≤ κα_1, so (i) and (ii) hold at silent points too.
- **(iv)** Without (H4), silence can be optimal with α_2 < κβ_1 and β_2 > κα_1. The script prints a witness.

*Proof.* Compare the optimal cost with the other two costs. For (i): a(α_1+β_1) ≤ aα_1+bα_2. For (ii): b(α_2+β_2) ≤ aα_1+bα_2. For (iii): combine the two silence inequalities with (H4). ∎

**Theorem A (general seam barrier; PROVED).**

*Hypotheses.*
- Strict (G) holds at worlds 1 and 2.
- The edge selection is coherent and competitive on supp q, and T is competitive on the support of its index.
- ℓ is a general field, integrable on the pieces below.
- C = D_K is a selected model at an open-edge index, with K ⊆ E and θ-thresholds τ_0 ≤ τ_1.
- P_1 ⊆ Sil(T) ∩ M_1 ∩ {θ > τ_0}, P_2 ⊆ Sil(T) ∩ M_2 ∩ {θ < τ_1} and P_3 ⊆ Sil(T) ∩ M_3 are non-null.
- On P_1, C is 2-correct, or silent with (H4). On P_2, C is 1-correct, or silent with (H4).

*Conclusion.* ℓ cannot endorse both of the following:
- every accepted comparison out of C at worlds 1 and 2 against rivals equal to C off P_1 ∪ P_2;
- every accepted majority fill of T supported in P_1 ∪ P_2 ∪ P_3.

*Proof.*
1. **Bayes weights.** Lemma 2.3 (any field) makes C pointwise (a, b)-Bayes on P_1 ∪ P_2.
2. **a, b > 0.** If b = 0, the unique minimiser is 1-correct. But C is not 1-correct on P_1, which is non-null. So b > 0, and likewise a > 0.
3. **The two inequalities.** The pointwise lemma gives α_2 ≥ κβ_1 a.e. on P_1 and β_2 ≤ κα_1 a.e. on P_2.
4. **The pieces.** By atomlessness choose A_1 ⊆ P_1 and A_2 ⊆ P_2 with ∫_{A_1}β_1 = ∫_{A_2}α_1 =: m. Choose A_3 ⊆ P_3 with ∫_{A_3}β_3 < ∫_{A_1∪A_2}α_3.
5. **The fill.** Fill all three pieces with the majority answer. The world values are:
   - world 1: m − m − ∫_{A_3}α_1 < 0;
   - world 2: −∫_{A_1}α_2 + ∫_{A_2}β_2 − ∫_{A_3}α_2 ≤ −κm + κm − ∫_{A_3}α_2 < 0;
   - world 3: < 0 by the choice of A_3.
6. **Contradiction.** T accepts the fill at some world of its support, and endorsement makes that value ≥ 0. ∎

(Finite instances: CHECKED in `general_seam_algebra.py`, part 4.)

**Corollary A (subclass; PROVED).** If (H4) holds a.e. on Sil(T) ∩ W_12 near a seam ray g*_τ with τ ∈ J, then PP32 Thm 3.1 holds verbatim for ℓ. Take C = C_{q*} with r ∈ K from Lemma 2.2, which uses no endorsement, and PP32's pieces. Similarly, if (H4) holds on each W_ij, then Cor 3.3 holds, by Lemma 3.4 plus Theorem A. This class includes rank-linear fields and every field with α_w ≥ β_w.

**Corollary A′ (every field; PROVED).** Under the hypotheses of Theorem A without (H4), let every comparison out of selected edge models, and T's fills, be ℓ-endorsed. Then every selected non-vertex edge model's silent window reaches an end of the band: τ_0 ≤ α or τ_1 ≥ β. Equivalently, K = [x_0, x_1] has x_0 ≤ d or x_1 ≥ 1−d, where d = c/(2c+ε) and (d, 1−d) is the shadow of int M from e_3.

*Proof.* Suppose instead α < τ_0 ≤ τ_1 < β. Take P_1 ⊆ O_1(τ_1), where C is 2-correct, and P_2 ⊆ O_2(τ_0), where C is 1-correct. Both are non-null by Lemma 1.1. Then apply Theorem A. ∎

**Consequences of Cor A′.** With Lemma 2.2, every r in the shadow lies in a selected K that reaches out of the shadow. In particular, no precise D_r with τ_r ∈ J is selected. The same statement holds for any imprecise interior selected N with its own band J_N (Lemma 3.4).

Cor A′ is sharp: ℓ^T below meets it with equality at t = 1. The box system (§3.3) also meets it. Its edge window at ratio t is [tλ_1/η_2, tη_1/λ_2], which can sit inside J_N = (λ_1/η_2, η_1/λ_2) only if t > 1 and t < 1 at once (CHECKED, `boxes_selection.py` (d)).

### 3.2 Theorem 3.1 fails for general fields: the field ℓ^T (PROVED; CHECKED in `ellT_counterexample.py`)

**The constants.** Put
- L := (c+ε)/c = β, so 1/L = α;
- d := 1/(1+L) = c/(2c+ε).

**The edge function.** Define

    F(θ) = θ/(2d) on (0, d];   1/2 + L(θ−d)/(2d) on [d, 1/L];   Lθ on [1/L, ∞),

and G(s) := 1/F(1/s). F is continuous and strictly increasing, with F(d) = 1/2 and F(1/L) = 1. The identity 1 − Ld = d makes the two formulas agree at 1/L.

**The field.** On M_i, with s_j = |g_j|/|g_i|:
- α_i = β_i = |g_i|;
- for j ≠ i: β_j = |g_i|F(s_j) and α_j = |g_i|G(s_j);
- γ_w = |g_w|.

On unanimous problems, α = β = γ = |g_w|. The envelope is integrable, since F(θ) ≤ 1 + Lθ and G(s) ≤ max(s/L, 2ds, 2).

**Facts.**
1. **Abstention (non-adjacent).** F(θ)F(1/θ) ≥ min(L², L(1+L)/2) > 1, so G < F. *Proof:* for θ ∈ [1/L, L] the product is L². For θ < 1/L it equals L·F(θ)/θ. On [d, 1/L], F(θ)/θ = L/(2d) + (1−L)/(2θ) is increasing, so the product is ≥ L/(2d) = L(1+L)/2 > 1. The case θ > L is symmetric.
2. **Edge consistency.** On M_2, β_2/α_1 = 1/G(1/θ) = F(θ). So on all of W_12, at edge weight ratio t = λ_1/λ_2:
   - the Bayes model is 1-correct iff F(θ) < t;
   - it is 2-correct iff G(θ) > t;
   - it is silent otherwise;
   - on M_3 ∪ U it gives the correct common answer.

   That is D_K with K the edge segment with thresholds F^{-1}(t) < G^{-1}(t): coherent, with null ties. So the edge selection q ↦ (Bayes model at q) is coherent and competitive, and p ↦ L_w(C_p) is continuous along the edge. Sections are therefore closed: (H1) and (H2) hold, with the ranking equal to ℓ^T itself. At t = 1, K = [(d,1−d,0), (1−d,d,0)], the shadow of M.
3. **T1 is the unique u-Bayes model.** On M_1 at u:
   - minority beats silence iff F(s_2) + F(s_3) < 1;
   - majority beats silence iff G(s_2) + G(s_3) > 1.

   Piecewise, the first holds iff s ∈ Q := {(c+ε)s_2 + cs_3 < c, cs_2 + (c+ε)s_3 < c}. That is exactly T1's acceptance of g: on [0,d]² the sum is (s_2+s_3)/(2d) < 1; on the mixed quadrant it reduces to Ls_2 + s_3 < 1.

   The second holds iff s_2 + s_3 > L. That is exactly T1's acceptance of −g, using G(s) = s/L for s ≤ L, and G > 1 for s > L.

   So T1 is competitive at every world: (H3) holds.
4. **Endorsement.** ℓ^T endorses every accepted comparison, because the ranking *is* ℓ^T. So (E-edge) and (E-T) hold on any pieces, and the conclusion of Thm 3.1 fails. This is consistent with Cor A′: for t ≤ 1, τ_0 = F^{-1}(t) ≤ α; for t ≥ 1, τ_1 = G^{-1}(t) ≥ β.
5. **ℓ^T is not an (S)-system.** At p = (200, 800, 1)/1001 the p-Bayes model is incoherent. Take two M_1 gambles, with s_3 = 1/L ∓ 1/(4L) and s_2 just inside the acceptance boundary. Both are accepted with strict margins, and their midpoint is strictly not accepted. The cause is that F has a concave kink at 1/L.

   Strict margins persist on neighbourhoods. The midpoints of two full-measure subsets of two balls cover the open midpoint ball, so no D_K agrees a.e. with this Bayes model. By *Contamination Triangle* Prop. `necessary`(a), interior Bayes models of an additive (S),(C),(LA) system are unique and coherent. So no (S)-selection exists for ℓ^T.

   (CHECKED for ε ∈ {1/10, 3/10, 1/2, 9/10}. Checks (b) and (c) cover about 24,000 random rational problems at u and about 19,000 at edge weights.)

**Why the local route breaks.** ℓ^T's edge models are silent on the whole seam band at t = 1. There, silence-optimality gives G ≤ κ ≤ F, the reverse of what the fill needs. Prop 2.4's sandwich is available only where edge models answer.

### 3.3 Cor 3.3 fails for general fields: normalised boxes (known; CHECKED in our setting)

Take *Coverage after Neutral Abstention*, eqs. (3)–(4):
- mixed problems: α_w = λ_w|g_w| and β_w = η_w|g_w|, with 0 < λ_w < η_w;
- contradiction 2(λ_w+η_w)|g_w|;
- unanimous problems: 0, |g_w|, 2|g_w|, 4|g_w|.

At every p ∈ Δ, the pointwise minimiser is unique a.e. and equals D_{K_p}, with K_p = {normalise(p ⊙ a) : a_w ∈ [λ_w, η_w]}. CHECKED with λ = (1,1,2) and η = (2,3,3): 23,871 (p, g) pairs at interior, edge and vertex p. K_u is a hexagon in int Δ, with six extreme points listed in `boxes_selection.out`.

By v3 `thm:general`, this gives (LA), (S) with continuous sections, (C), (G) and (IB). Transitivity gives (TC), and reflexivity is trivial. So every Brief-48 axiom holds, and an imprecise interior model is selected. (H4) fails everywhere, since α_iα_j < β_iβ_j. Corollary A′ is respected (§3.1).

### 3.4 The other PP32 corollaries under general fields

- **Cor 5.2 (location).** It does not extend: ℓ^T with 𝒩 = ∅ satisfies its premises.
- **Cor 2.5 (edge monotonicity).** The analogue holds where edge models answer: Theorem A gives α_2/β_1 ≥ κ and β_2/α_1 ≤ κ on the respective sides. On edge-silent windows nothing is forced.
- **Cor 3.2 (T1 not single-field endorsable) for general fields.** This is true by global results already in the project, not by PP32's route:
  - Q4.2 with HH1's repair (CC3 referee: "no ranking whose worlds all add up covers T1", ladder endorsers ν^s, ν^w, i.e. separate α and β; survives under (TC) per HH1);
  - FF2 Thm 4.1 (any strictly guiding field, with continuity in measure).

  One caveat: Q4.2 endorses relevant comparisons out of all of C_L, while PP32 endorses comparisons out of selected models only. I have not checked whether HH1's repaired proof needs the larger family (OPEN for me).

---

## 4. Question (b): an imprecise interior model, and T1 itself

### 4.1 Imprecise interior models: yes, and already known

§3.3. The lead's reading ("cheaper silence makes imprecise models additive-Bayes") is right: these are exactly the abstention fields, β > α. But it is the project's existing positive result:
- v3 `thm:general`;
- *Coverage after Neutral Abstention* eqs. (3)–(4);
- START HERE: "Covered: … normalized boxes; gauge-mixture polygons (incl. polygons arbitrarily close to T1)".

It is not a new finding.

### 4.2 The obvious T1 candidate

- **|g_w| densities with constant silence fractions** (α_w = λ_w|g_w|, β_w = η_w|g_w|). The Bayes model at every index is a normalised box (PROVED, §3.3). Each side of a normalised box lies on a line q_i/q_j = constant, which passes through the third simplex vertex. T1's sides lie on lines q_w = c, which pass through no simplex vertex. So **no index gives Sil(T1)** (PROVED).
- **Ratio-dependent silence penalties.** These can make Sil(T1) the abstention region at one weight. ℓ^T does it at u (§3.2), and so does DESIGN_MEMO §7's ℓ^m (π_i(x) = −x_i q_i(x)/m_i), for any interior M. So **T1's silent set is the abstention region of an additive rule** (PROVED, CHECKED).
- **The induced selection.** It does **not** satisfy (S): the interior Bayes model at p = (200, 800, 1)/1001 is incoherent (§3.2, item 5). The closed-section, vertex and edge clauses do hold for ℓ^T on the boundary of Δ (§3.2, item 2; Lemma B is automatic). The failure is interior coherence at weights other than u.

### 4.3 No single general additive field gives an (S)-system through T1

The project proves this as follows:
- **Abstention fields:** *Contamination Triangle* Thm `main` / Cor `coverage` (refereed twice). It applies on every decomposable domain non-adjacent near T, hence on the full domain for abstention fields.
- **Every strictly guiding field, full domain:** Q4.2 / M3.10′ ((Av) holds on the full domain; status per CC3 referee, M3.9 refereed once).

For a cross-check, here is a short proof in PP32's setting.

**Proposition B (PROVED).**

*Hypotheses.*
- The ranking is a general additive field on the full domain with (LA), (S) and (C), and covers T1.
- **(N)** The field is non-adjacent.
- **(Reg)** The six edge functions F_ij (defined below) are continuous, strictly increasing, and have inverses with a point of positive derivative.

*Conclusion.* Contradiction.

*Proof.*
1. **Coherent Bayes models everywhere.** By *Contamination Triangle* Prop. `necessary`, every interior Bayes model is unique and coherent, and T1 = B_{λ*} with λ* ∈ int Δ. Under (Reg) the edge Bayes models are unique and coherent too.
2. **Edge functions.** Coherence on edge {i,j}, as in §3.2 item 2, forces β_j/α_i = F_ij(θ_ij) a.e. on W_ij, with the same function on M_i and M_j. Put G_ji(x) := 1/F_ij(1/x). On M_j, α_i/β_j = G_ji(s_i).
3. **Concavity.** Take interior weights λ = (η, λ_2, λ_3) with η → 0. Coherence of B_λ makes the M_2-majority region {ηG_21(s_1) + λ_3G_23(s_3) > λ_2} convex. It has the form {s_3 > b(s_1)} with b(s_1) = G_23^{-1}((λ_2 − ηG_21(s_1))/λ_3), and convexity means b is convex. To first order in η, b = const − η·D·G_21/λ_3 with D > 0 by (Reg). So G_21 is concave on (0,∞). Being positive, G_21(x)/x is nonincreasing, i.e. F_12(θ)/θ is nonincreasing.
4. **A lower bound from T1's majority answers.** On M_2, T1 does not accept the majority answer when s_1 + s_3 < L. So λ*_1/F_12(θ_12) ≤ λ*_2 for every θ_12 > 1/L (take s_3 small). With step 3, for θ ≤ 1/L < θ′ we get F_12(θ)/θ ≥ F_12(θ′)/θ′ ≥ λ*_1/(λ*_2θ′). Letting θ′ ↓ 1/L gives F_12(θ) ≥ Lθλ*_1/λ*_2 on (0, 1/L]. Likewise F_13(θ) ≥ Lθλ*_1/λ*_3 there.
5. **Contradiction with T1's minority answers.** On M_1, T1 accepts g for s ∈ Q, so λ*_1 ≥ λ*_2F_12(s_2) + λ*_3F_13(s_3) ≥ Lλ*_1(s_2+s_3). That forces s_2 + s_3 ≤ 1/L on Q. But (d−δ, d−δ) ∈ Q, and 2d > 1/L ⟺ 2(c+ε) > 2c+ε. ∎

**Reading.** T1's minority region bulges past the chord that its majority region fixes. Coherence at nearby weights forces the minority region to sit under that chord: F(θ)/θ nonincreasing. Normalised boxes sit exactly on the chord (F = kθ), which is why they are covered and T1 is not.

### 4.4 Reconciliation with earlier project statements

| Earlier statement | Consistent? |
|---|---|
| DESIGN_MEMO §7: "in any number of worlds an imprecise model is never competitive for I_λ" | Yes. I_λ is the error-set loss: silence costs half of wrong, so it is rank-linear with density |g_i|. Ties are null, so Bayes models are precise. The remark is specific to I_λ. Balanced rank-linear fields (Ω) do make T1 Bayes (PP32 Prop 4.1), and abstention fields make boxes Bayes. |
| DESIGN_MEMO §7 Proposal 3, ℓ^m | Yes. A general additive field with D_M as m-Bayes at one weight: the same phenomenon as ℓ^T. Single-index realisability was never the obstacle. |
| v3 Thm `additive-obstruction` | Covers only targets containing three simplex vertices. No conflict. |
| CNA eqs (3)–(4); START HERE "covered: normalized boxes, gauge-mixture polygons" | This is (b)'s positive half. |
| Contamination Triangle Thm `main` / Cor `coverage`; FF2 Thm 4.1; Q4.2 / M3.10′ | These are (b)'s negative half for T1. FF2 and Q4.2 already use general (ladder) fields. PP32's rank-linear local results are a different, weaker-hypothesis line, and §3.2 shows that this line cannot be extended to general fields. |
| AUDIT_selected_realizability §2 (S_0 is an additive (S)-system) | Yes. S_0 is rank-linear, and every selected model in it is precise (PP32 Cor 3.3). |
| kkm-calibration notes | Not reachable from this session (project docs only; not in r9 or on disk). Not reconciled. |

---

## 5. Recommendations

1. Retitle PP32 and its §0 bullets as **rank-linear**. Add one paragraph:
   - Thm 3.1, Cor 3.3 and Cor 5.2 hold for fields with (H4) (Theorem A);
   - they fail for abstention fields (ℓ^T, boxes);
   - the general-field form of Cor 3.2 rests on Q4.2 / FF2, not on the seam.
2. Adopt the weakened (H3) ("T competitive on the support of its index"). It is free and it removes the strict-(G)-at-world-3 dependence.
3. For Brief 48's design work, read Cor A′ this way. Any additive-flavoured piece of a T1 cover that is judged by one general field must use edge models that are imprecise and reach beyond the shadow of M. Precise edge models in the shadow are excluded for *every* single field, not just rank-linear ones.

## Scripts (`r9/PP35_py/`)

| Script | Content | Label |
|---|---|---|
| `boxes_selection.py` | normalised-box field: Bayes = D_{K_p} at all p; K_u a hexagon; (H4) fails; Cor A′ check | CHECKED |
| `ellT_counterexample.py` | ℓ^T: G < F; T1 = unique u-Bayes; coherent edge Bayes models; Cor A′ sharpness; incoherent interior Bayes model | CHECKED |
| `general_seam_algebra.py` | pointwise lemma of Theorem A; (H4) witness; finite fills | CHECKED |
| `rerun_PP32/*.out` | outputs of PP32's four scripts, re-run (identical) | CHECKED / NUMERICS as in PP32 |
