# PP32. The additive barrier: one field cannot serve both T1 and an edge

22 October 2026. One reader (me); not refereed.

**Labels.** PROVED: full proof here. CHECKED: exact rational computation. NUMERICS: floating-point illustration; no proof depends on it. CONJECTURE / OPEN: as stated.

**Scripts** (`r9/PP32_py/`; run `python3 -I -B <script>`; each writes a `.out` file; all end ALL PASS):

| Script | Content | Label |
|---|---|---|
| `seam_geometry.py` | band ranges α, β; the seam ray and its four sides are silent; τ_r ∈ J ⟺ [r, e_3] meets int M; four values of ε | CHECKED |
| `edge_covering.py` | the pointwise comparisons in Lemmas 2.1–2.2 (293 random pairs (K, r), 116,838 problems) | CHECKED |
| `union_escape.py` | Prop 6.1: T1 is Ω-Bayes and every precise edge model is S_0-Bayes | CHECKED |
| `seam_witness_mc.py` | the two explicit witnesses of Theorem 5.1, Gaussian Monte Carlo | NUMERICS |

**Inputs.** Brief 47; DESIGN_MEMO §8.16 (lead's conjecture); REFEREE_round46 (R46.0, R46.1 and the remark that the general-field case is open); AUDIT_selected_realizability §2 (S_0); PP18 Prop 4.3; PP30 (Thm 3.1, Prop 3.4); LEAD_selection_count (Lemma B). Nothing is assumed beyond Brief 47's axioms. Each result lists the axioms it uses.

---

## 0. Verdict

**The conjecture is true (PROVED).** It holds in a stronger, local form.

**Theorem 3.1, short form.** Suppose:
- strict (G) holds at worlds 1 and 2;
- the selection on the edge [e_1, e_2] is coherent and competitive, with closed sections for **one** rival, the precise model D_r with r = (1/2, 1/2, 0);
- T1 is competitive at all three worlds.

Then no positive densities ρ_1, ρ_2, ρ_3 can endorse both of the following:
- (i) the comparisons out of the edge models at worlds 1 and 2;
- (ii) T1's acceptances of majority fills of its own silence.

Endorsement is needed only for records supported in three small bounded pieces of Sil(T). No (IB), (TC), (C), (LA), undominatedness, or continuity is used.

**Status of the lead's sketch.**

| Step | Verdict |
|---|---|
| (a) T is balanced | **Correct** (Prop 4.1, with all λ_w > 0). Not needed for the contradiction; it is used for the second witness in Theorem 5.1. |
| (b) edge models are two-world Bayes | Correct for non-vertex models, and K ⊆ edge follows from strict (G) alone (Lemma 2.1). **Wrong:** "acceptance set = {ρ_2/ρ_1 < a/b} a.e." On the level set {ρ_2/ρ_1 = a/b} the model is unconstrained. Only a sandwich holds (Prop 2.4). |
| (c) four-quadrant clash in M_1 | **Not valid as stated.** Locally constant density ratios satisfy every local condition (Example 4.3). It is valid only if level sets are null. **Replaced** by a *seam* argument: one edge, and the plane g_3 = 0 instead of a second edge. The two sides of the seam lie in M_1 and M_2, whose balance identities push ρ_2/ρ_1 in opposite directions. |
| (d) thresholds inside the band | **PROVED** (Lemma 2.2, edge covering). Every point r of the edge lies in the credal set of some selected edge model, so the step cannot fail and no edge selection escapes. The proof uses 1-D KKM on the edge with rival D_r, strict (G) and Lemma B. |

**Restrictions (PROVED, §6.1).** The theorem survives restricting endorsement to:
- bounded records;
- annulus-supported records;
- records supported in Sil(T);
- all three restrictions at once;
- records in three arbitrarily chosen pieces of the required regions.

**Extensions (§§6.2–6.3).**
- **Lexicographic stacks** whose leading level is a positive density: excluded (PROVED).
- **Unions of finitely or countably many endorsing densities:** the proof does **not** extend. An explicit two-member family {Ω, S_0} satisfies every Bayes-level consequence (PROVED; CHECKED). Whether a real (S)-system exists this way is OPEN.
- **Lexicographic stacks whose leading level changes by region:** OPEN.

**Where non-additivity must live (Cor 5.2, PROVED).** Fix any positive field. Let 𝒩 be the part of Sil(T) where that field may fail. Then, for each edge {i, j}, 𝒩 must contain one of two sets (up to null sets):
- a whole *crossed cone* Sil(T) ∩ [(M_i ∩ {θ_ij > τ_0}) ∪ (M_j ∩ {θ_ij < τ_0})], for some τ_0 ∈ [α, β];
- the whole band Sil(T) ∩ M_k of the third class.

So non-additivity cannot be confined to:
- a null set;
- a bounded set;
- a neighbourhood of the coordinate planes.

FF2 Thm 4.1 reached this last conclusion only with continuity in measure.

**Two by-products (PROVED).**
- **Edge monotonicity (Cor 2.5).** Any single field that endorses the edge models must have ρ_j/ρ_i essentially nondecreasing in |g_j|/|g_i| on W_ij. This is the general-field form of R46.1. Ω violates it; S_0 satisfies it.
- **Additive endorsement forces precision (Cor 3.3).** Assume (S) with strict (G) at all worlds and a single endorsing field. Then every selected model with credal set K ⊆ int Δ is precise. This covers T1, refinements of T and PP20's coarsenings. It explains why the audit's S_0 works (everything selected is precise) and why nothing additive selects T1.

---

## 1. Setting and notation

Brief 47's setting:
- three worlds, with problems g ∈ R³ modulo sign and Gaussian μ;
- the full four-advice domain, with models taken modulo null sets;
- ranks r_w: correct 0, silent 1, wrong 2, contradictory 3;
- T = T1 = D_M, where M = c·1 + εΔ = {m ∈ Δ : m_w ≥ c} and c = (1−ε)/3.

D_K accepts g iff m·g > 0 for all m ∈ K. Strict (G) at w: a model pointwise no worse at w, and strictly better on a non-null set, is strictly preferred at w.

**Endorsement.** A positive density ρ_w *endorses* an accepted comparison N ⪯_w X if

  ∫ ρ_w (r_w(X) − r_w(N)) dμ ≥ 0.

This needs ρ_w to be integrable on {X ≠ N}.

**Edge coordinates.** Write W_12 = {g_1 g_2 < 0} = M_1 ∪ M_2 (up to null sets), θ := |g_2|/|g_1| on W_12, and φ := ρ_2/ρ_1.
- For r = (x, 1−x, 0), put τ_r = x/(1−x).
- For K = [k, k'] ⊆ [e_1, e_2] with first coordinates x_0 ≤ x_1, D_K on W_12 is:
  - 1-correct when θ < τ(x_0);
  - silent when τ(x_0) < θ < τ(x_1);
  - 2-correct when θ > τ(x_1).

  Off W_12 (on M_3 ∪ U), D_K gives the answer on which worlds 1 and 2 agree, which is correct at both. (Orient g with g_1 > 0 and check the sign of x g_1 + (1−x) g_2 in M_1 and in M_2.)

**The band and the seam.** Put α := c/(c+ε), β := (c+ε)/c = 1 + ε/c, and J := (α, β). For τ > 0 define

  O_1(τ) := Sil(T) ∩ M_1 ∩ {θ > τ},  O_2(τ) := Sil(T) ∩ M_2 ∩ {θ < τ}.

**Lemma 1.1 (PROVED; CHECKED in `seam_geometry.py`).**
- (i) θ < β on Sil(T) ∩ M_1, and θ > α on Sil(T) ∩ M_2. These bounds are sharp.
- (ii) For τ ∈ J the *seam ray* g*_τ = (1, −τ, 0) lies in the open cone Sil(T). Hence O_1(τ) and O_2(τ) are nonempty open cones, and so non-null.
- (iii) τ_r ∈ J iff the segment [r, e_3] meets int M, iff r_1, r_2 > c/(1−c).

*Proof.*
- (i) In M_1 write g = (1, −t, −t'). We have min_M m·g = c(1−t−t') − ε max(t, t') and max_M m·g = c(1−t−t') + ε, so T is silent iff c(1−t−t') < ε max(t,t') and c(t+t'−1) < ε. The second condition gives t < β. For each t ∈ (0, β), the point t' = 1 − t + η (small η > 0) is silent, so the bound is sharp. M_2 follows by the symmetry that swaps worlds 1 and 2, which sends θ to 1/θ.
- (ii) T is silent at g*_τ iff c(1−τ) < ετ and c(τ−1) < ε, i.e. iff τ ∈ J. The cone Sil(T) is open. Near g*_τ there are problems:
  - with g_3 < 0 (so in M_1) or g_3 > 0 (so in M_2);
  - with θ above or below τ.

  So all four combinations occur near g*_τ.
- (iii) A point (1−λ)r + λe_3 has all coordinates > c iff λ > c and (1−λ) min(r_1, r_2) > c. Such λ exists iff min(r_1, r_2) > c/(1−c) = c/(2c+ε). That is equivalent to τ_r ∈ J. ∎

The midpoint r = (1/2, 1/2, 0), with τ_r = 1, always qualifies. J is nonempty exactly because M has interior: the θ-ranges of T's silence on the two sides of the seam overlap. This overlap drives everything below.

---

## 2. Edge lemmas

Let E := [e_1, e_2], and let q ↦ C_q (q ∈ E) be the selection restricted to E.

**Lemma 2.1 (edge models live on the edge; PROVED).** Uses strict (G) at 1 and 2 and competitiveness on supp q = {1, 2}. Let q be in the open edge. Then:
- (i) C_q is correct at worlds 1 and 2 a.e. on M_3 ∪ U;
- (ii) if C_q = D_K is coherent, then K ⊆ E.

*Proof.*
- (i) On M_3 ∪ U, worlds 1 and 2 have the same correct answer. Suppose C_q is not correct on a non-null E′ ⊆ M_3 ∪ U. Then X := C_q[E′ → that answer] is pointwise weakly better at worlds 1 and 2, and strictly better on E′. Strict (G) refuses C_q ⪯_1 X and C_q ⪯_2 X, so C_q is not competitive.
- (ii) Suppose m ∈ K has m_3 > 0. On an open set of problems near (d, d, −1) with 0 < d < m_3/(m_1+m_2), we have m·g < 0, so D_K does not accept there. That set lies in M_3, which contradicts (i). (CHECKED, 2,000 instances.) ∎

**Lemma 2.2 (edge covering; PROVED; CHECKED).** Uses:
- strict (G) at worlds 1 and 2;
- coherent C_q, competitive on supp q;
- for one fixed r in the open edge, closed sets S_w := {q ∈ E : C_q ⪯_w D_r} for w = 1, 2.

Then there is q* in the open edge with C_{q*} ⪯_1 D_r and C_{q*} ⪯_2 D_r. Moreover C_{q*} = D_K with r ∈ K ⊆ E and K ≠ {e_1}, {e_2}.

In particular, **every point of the edge lies in the credal set of some selected edge model.**

*Proof.*
1. **The sections cover the edge.** Each q in the open edge lies in S_1 ∪ S_2 by competitiveness. The vertices give e_1 ∈ S_1 and e_2 ∈ S_2. Since E is connected and both sets are closed, they meet at some q*.
2. **q* is not a vertex.** By Lemma B, C_{e_1} = V_1. D_r is pointwise no worse than V_1 at world 2: it is 2-correct on W_12 ∩ {θ > τ_r}, where V_1 is 2-wrong, and equal to V_1 elsewhere. It is strictly better on a non-null cone. So strict (G) refuses V_1 ⪯_2 D_r, and the same holds at any index where C_q = V_1. Hence q* ≠ e_1 and C_{q*} ≠ V_1; symmetrically for V_2.
3. **K ⊆ E.** By Lemma 2.1, C_{q*} = D_K with K = [k, k'] ⊆ E.
4. **r ∈ K.** Suppose r ∉ K, say r_1 < x_0, so τ_r < τ(x_0). Then D_r is pointwise no worse than D_K at world 2:
   - both are 1-correct for θ < τ_r;
   - D_r is 2-correct on (τ_r, τ(x_1)), where D_K is 1-correct or silent;
   - they agree elsewhere.

   D_r is strictly better on the non-null cone τ_r < θ < τ(x_0), so strict (G) refuses C_{q*} ⪯_2 D_r. The case r_1 > x_1 is symmetric, at world 1. (CHECKED, `edge_covering.py`.) ∎

So the selection on each edge must realise every threshold. This is the 1-D KKM step the lead asked for, and it needs no endorsement.

**Lemma 2.3 (local Bayes from endorsement; PROVED).** Let N be a model, W a set of worlds, Q a measurable set, and ρ_w (w ∈ W) positive densities integrable on Q. Suppose:
- for every X equal to N off Q, some w ∈ W has N ⪯_w X;
- every such acceptance is ρ_w-endorsed.

Then some λ ∈ Δ_W makes N(g) a minimiser of a ↦ Σ_w λ_w ρ_w(g) r_w(g, a) for a.e. g ∈ Q.

*Proof.* Let V be the set of vectors v(X) := (∫_Q ρ_w (r_w(X) − r_w(N)) dμ)_{w ∈ W}.
1. **V is convex.** Given X, X′ and α ∈ [0,1], Lyapunov's theorem for the vector measure with densities (ρ_w Δr_w(X), ρ_w Δr_w(X′))_w gives E ⊆ Q carrying an α-fraction of both. Splice X on E with X′ on Q ∖ E. The result has vector α v(X) + (1−α) v(X′).
2. **Separation.** By hypothesis V misses the open negative orthant. A separating λ ≥ 0, λ ≠ 0, satisfies λ·v ≥ 0 on V.
3. **Pointwise.** If some answer were strictly cheaper than N's on a non-null subset of Q, replacing N's answer there would give λ·v < 0. ∎

**Proposition 2.4 (edge sandwich; PROVED).** Assume Lemma 2.2's hypotheses for r. Let P_1 ⊆ W_12 ∩ {θ > τ_r} and P_2 ⊆ W_12 ∩ {θ < τ_r} be non-null. Suppose ρ_1, ρ_2 > 0 are integrable on Q := P_1 ∪ P_2 and endorse, at worlds 1 and 2, every accepted comparison out of a model selected on the open edge against a rival equal to it off Q. Then there is κ ∈ (0, ∞) with

  φ ≥ κ a.e. on P_1, and φ ≤ κ a.e. on P_2.

*Proof.*
1. Take q* and C_{q*} = D_K, r ∈ K, from Lemma 2.2. Lemma 2.3 with W = {1, 2} gives weights (a, b).
2. **The answers on P_1 and P_2.** Because r ∈ K, D_K is silent or 2-correct on P_1, and silent or 1-correct on P_2.
3. **Both weights are positive.** If b = 0, the unique minimiser on Q is the 1-correct answer, which is false on P_1. So b > 0, and likewise a > 0.
4. **Costs on W_12.** The 1-correct answer costs 2bρ_2, the 2-correct answer costs 2aρ_1, silence costs aρ_1 + bρ_2, and contradiction costs 3(aρ_1 + bρ_2).
5. **The sandwich.** "2-correct or silent is optimal" means aρ_1 ≤ bρ_2, i.e. φ ≥ a/b. Symmetrically on P_2. Put κ := a/b. ∎

**Corollary 2.5 (edge monotonicity: the general-field form of R46.1; PROVED).** Suppose the endorsement of Prop 2.4 holds for all bounded records in W_12. Then for every τ > 0:

  ess sup_{W_12 ∩ {θ<τ}} φ ≤ ess inf_{W_12 ∩ {θ>τ}} φ.

Hence φ = F(θ) a.e. on W_12, for a nondecreasing F.

*Proof.*
1. **Exhaust by balls.** Apply Prop 2.4 to Q_n = W_12 ∩ B_n, with B_n balls exhausting R³. The admissible κ's form nonempty intervals [s_n, i_n], where s_n ↑ and i_n ↓. So s := lim s_n ≤ lim i_n.
2. **φ is a function of θ.** Take all rational τ. Then a.e. g satisfies F(θ(g)−) ≤ φ(g) ≤ F(θ(g)+). The level sets of θ are null, so φ(g) = F(θ(g)) at continuity points of F. ∎

Two consequences:
- **Ω** (φ = 1/2 on M_1, φ = 2 on M_2) violates the corollary at every τ. This recovers R46.1, here from closed sections for D_r.
- **S_0** (φ = θ) satisfies it.

So the edges alone do not force non-additivity. That matches the audit's §2 and the referee's remark that the general-field case was open.

---

## 3. The main theorem

**Theorem 3.1 (local additive barrier; PROVED).** Assume:
- (H1) strict (G) at worlds 1 and 2;
- (H2) on E, coherent C_q, competitive on supp q, and closed sections for the single rival D_r, where τ_r ∈ J (e.g. r = (1/2, 1/2, 0));
- (H3) T1 is competitive at all three worlds. This holds when T1 is selected: its index is then interior, because at an edge index {i, j}, filling Sil(T) ∩ M_k with the majority answer is a strict (G) improvement at both i and j.

Choose non-null pieces P_1 ⊆ O_1(τ_r), P_2 ⊆ O_2(τ_r) and P_3 ⊆ Sil(T) ∩ M_3. They may be bounded and arbitrarily small (Lemma 1.1). Let ρ_1, ρ_2, ρ_3 be positive and integrable on P := P_1 ∪ P_2 ∪ P_3. Then the following cannot both hold:
- (E-edge) every accepted comparison C_q ⪯_w X, with q in the open edge, w ∈ {1, 2} and X = C_q off P_1 ∪ P_2, is ρ_w-endorsed;
- (E-T) every accepted comparison T ⪯_w Y, where Y is a *majority fill* T[A → majority] with A ⊆ P, is ρ_w-endorsed.

*Proof.*
1. **The edge side.** By (E-edge) and Prop 2.4 there is κ with ρ_2 ≥ κρ_1 on P_1 and ρ_2 ≤ κρ_1 on P_2.
2. **Two pieces of equal world-1 weight.** ρ_1 μ is atomless, so there are non-null A_1 ⊆ P_1 and A_2 ⊆ P_2 with ρ_1(A_1) = ρ_1(A_2) =: m. (Here ρ(A) means ∫_A ρ dμ.) Then

   ρ_2(A_1) ≥ κm ≥ ρ_2(A_2).
3. **A small third piece.** Choose a non-null A_3 ⊆ P_3 with ρ_3(A_3) < ρ_3(A_1) + ρ_3(A_2).
4. **The rival.** Let Y := T[A_1 ∪ A_2 ∪ A_3 → majority]. T is silent on all three pieces. The majority answer changes the ranks as follows:

   | piece | class | Δ(r_1, r_2, r_3) |
   |---|---|---|
   | A_1 | M_1 | (+1, −1, −1) |
   | A_2 | M_2 | (−1, +1, −1) |
   | A_3 | M_3 | (−1, −1, +1) |

5. **Every world prefers T.** The ρ-values of T ⪯_w Y are:
   - world 1: ρ_1(A_1) − ρ_1(A_2) − ρ_1(A_3) = −ρ_1(A_3) < 0;
   - world 2: ρ_2(A_2) − ρ_2(A_1) − ρ_2(A_3) ≤ −ρ_2(A_3) < 0;
   - world 3: ρ_3(A_3) − ρ_3(A_1) − ρ_3(A_2) < 0.
6. **Contradiction.** By (H3), T ⪯_w Y holds at some w. By (E-T) its value is ≥ 0. ∎

**Corollary 3.2 (the lead's conjecture; PROVED).** Suppose:
- (S) holds with T1 selected (necessarily at an interior index);
- strict (G) holds;
- at each world w a single fixed positive integrable ρ_w weakly endorses every accepted comparison out of a selected model.

Then there is a contradiction. (All of Theorem 3.1's hypotheses hold. (IB) is not needed.)

**What is used, and what is not.**
- **Used:**
  - strict (G) at worlds 1 and 2 only;
  - Lemma B at e_1 and e_2;
  - closed sections for one rival on one edge;
  - competitiveness of T and of the edge models;
  - coherence of the edge models.
- **Not used:**
  - (IB), (TC), (LA), direct (C);
  - undominatedness;
  - strict (G) at world 3;
  - coherence of T (only T's silence pattern);
  - T's balance identity, PP18 Prop 4.3, which the lead's step (a) used;
  - any continuity.

**Lemma 3.4 (other targets; PROVED).** Let N = D_K with K ⊆ int Δ not a singleton. Then:
- (i) Sil(N) ∩ M_k is non-null for every k;
- (ii) for each vertex e_k not on the affine line of K (at least two vertices, or all three if K has interior), there is r on the opposite edge such that the seam ray of the line through e_k and r lies in Sil(N).

*Proof.*
- (i) Take x ∈ relint K. The line through x parallel to the edge opposite e_k separates e_k from the other two vertices. If necessary, rotate it slightly about x so that it strictly separates two points of K. Nearby lines give an open set of g ∈ Sil(N) ∩ M_k.
- (ii) Project x from e_k onto the opposite edge to get r. The line through e_k and r crosses K transversally at x, so its normal takes both signs on K. Sil(N) is open, so all four sides of the seam are present nearby, as in Lemma 1.1(ii). ∎

**Corollary 3.3 (additive endorsement forces precision; PROVED).** Assume:
- (S) with strict (G) at all three worlds;
- a single positive locally integrable field ρ endorses the accepted comparisons out of selected models (bounded records in Sil(N) suffice).

Then no model D_K with K ⊆ int Δ and K not a singleton is selected.

*Proof.* Lemma 2.1 rules out an edge index: Sil(N) ∩ M_k is non-null and N is not correct there. So N is competitive at all three worlds. Lemma 3.4 supplies the seam on a suitable edge. The proof of Theorem 3.1 then runs verbatim with N in place of T. ∎

So, in the class of single-field-endorsed systems, the audit's S_0 (all selected models precise) is not an accident: it is forced. Imprecise selected models can only sit on edges, where silence needs φ = κ on the silent wedge.

---

## 4. The lead's sketch, step by step

**(a) Prop 4.1 (balance; PROVED; PP18 Prop 4.3(b) with positivity added).** Suppose T is competitive at all worlds, and ρ endorses its accepted comparisons with rivals that differ from T only in Sil(T). Then there is λ with all λ_w > 0 and

  λ_k ρ_k = λ_i ρ_i + λ_j ρ_j a.e. on Sil(T) ∩ M_k.

*Proof.*
1. Lemma 2.3 with Q = Sil(T) gives λ.
2. On Sil(T) ∩ M_k, the majority answer costs 2λ_kρ_k, the minority answer costs 2(λ_iρ_i + λ_jρ_j), and silence costs their mean. Silence is optimal, so the two are equal.
3. If λ_k = 0, then λ_iρ_i + λ_jρ_j = 0 on a non-null set, which forces λ = 0. ∎

Consequence: put Λ := λ_1/λ_2. Then φ < Λ on Sil(T) ∩ M_1 and φ > Λ on Sil(T) ∩ M_2. The lead's "affine decreasing" relation ρ_3/ρ_1 = (λ_1 − λ_2 φ)/λ_3 on Sil(T) ∩ M_1 is correct.

**(b)** The correct parts:
- a non-vertex edge model is Bayes at (a, b, 0) with a, b > 0;
- its answers are functions of |g_1|/|g_2|. This needs only Lemma 2.1, not endorsement.

The incorrect part is the claim "acceptance set = {φ < a/b} a.e.". It fails whenever {φ = a/b} is non-null.

**Example 4.2.** Suppose φ ≡ κ on an open cone U_0 ⊆ W_12. Then the weights (κ, 1) make every non-contradictory answer optimal on U_0. So every D_K with K ⊆ E is Bayes there, whatever its threshold. Prop 2.4 is the correct replacement.

**(c) Example 4.3 (the four-quadrant clash fails locally; PROVED).** Take any point of the M_1 band and an open cone U_0 around it.
- On U_0, set ρ_1 = 1, ρ_2 = κ, ρ_3 = κ′.
- Take λ = (κ + κ′, 1, 1).

On U_0:
- T is balanced (silence, majority and minority all cost 2(κ+κ′));
- the [e_1,e_2]-model at weights (κ, 1) is indifferent;
- the [e_1,e_3]-model at weights (κ′, 1) is indifferent.

So all four quadrants are consistent, and no contradiction can come from M_1 alone.

The argument is valid under the extra hypothesis that φ and ψ have null level sets. Lemma 2.2 then supplies thresholds inside the band.

**Why the seam works where the quadrants do not.** In the lead's picture, both clashing regions lie in one class, under one balance identity. Across the seam g_3 = 0 the classes differ:
- **balance (Prop 4.1):** φ < Λ on the M_1 side and φ > Λ on the M_2 side;
- **edge sandwich (Prop 2.4):** φ is at least κ on the high-θ side, and at most κ on the low-θ side.

By Lemma 1.1, the M_1 side contains higher θ than the M_2 side. So the two requirements cross. Theorem 3.1 avoids Prop 4.1 altogether by testing T directly with a majority fill.

**(d) PROVED** by Lemma 2.2. "Inside the band" in the right sense means τ_r ∈ J, i.e. [r, e_3] meets int M. Every r is realised. This step cannot fail, so there are no escaping edge selections.

---

## 5. Explicit witnesses, and where the non-additivity sits

**Theorem 5.1 (two explicit witnesses; PROVED).** Use Theorem 3.1's setting, and let C := C_{q*} (from Lemma 2.2).
- **(a) If C is ρ-Bayes on P_1 ∪ P_2** (the edge models are "additive"): T accepts, at some world, a majority fill Y = T[A_1 ∪ A_2 ∪ A_3 → majority] (A_i ⊆ P_i) whose ρ-value is negative at every world. This is the proof of Theorem 3.1.
- **(b) If T is ρ-Bayes on P** (T is "additive", hence balanced by Prop 4.1): C accepts, at world 1 or 2, a *threshold swap*

    X = C[A_1 → 1-correct, A_2 → 2-correct], with A_i ⊆ P_i,

  whose ρ-value is negative at both worlds 1 and 2.

*Proof of (b).*
1. **Fix the answer types.** By Prop 4.1, φ < Λ on P_1 and φ > Λ on P_2. Choose non-null A_1 ⊆ P_1 on which C has one answer type (silent or 2-correct) and φ ≤ Λ − δ. Choose A_2 ⊆ P_2 on which C has one type (silent or 1-correct) and φ ≥ Λ + δ, with 0 < δ < Λ.
2. **The values.** Let c_i ∈ {1, 2} be the size of C's rank change on A_i. Put x := c_1ρ_1(A_1) and y := c_2ρ_1(A_2). Then:
   - world 1 value = y − x;
   - world 2 value = c_1ρ_2(A_1) − c_2ρ_2(A_2) ≤ (Λ−δ)x − (Λ+δ)y.
3. **Both negative.** By atomlessness, choose y < x < y(Λ+δ)/(Λ−δ). Both values are then negative.
4. **Contradiction.** C is competitive on {1, 2}, so it accepts X at world 1 or 2. ∎

NUMERICS (`seam_witness_mc.py`, ε = 3/10, small cones on each side of the seam ray (1, −1, 0) and around (1, 1, −2)):
- **Ω field (T balanced).** The swap out of D_{(1/2,1/2,0)} has values −0.00249 and −0.00249 at worlds 1 and 2, with standard errors about 0.00008.
- **S_0 field (edge monotone).** The majority fill out of T has values −0.00028, −0.00028 and −0.00028 at the three worlds, with standard errors about 0.00003.
- **Controls.** Each witness fails under the other field, as predicted:
  - under Ω, T's fill values sum to 0;
  - under S_0, the swap is never negative at both edge worlds.

**Corollary 5.2 (location; PROVED).** Fix a positive field ρ and a measurable 𝒩 ⊆ Sil(T). Suppose:
- (E-T) holds for majority fills supported in Sil(T) ∖ 𝒩;
- (E-edge) holds for rivals differing from the edge model only in W_12 ∩ Sil(T) ∖ 𝒩.

Then, up to null sets, either Sil(T) ∩ M_3 ⊆ 𝒩, or there is τ_0 ∈ [α, β] with

  X_12(τ_0) := Sil(T) ∩ [(M_1 ∩ {θ > τ_0}) ∪ (M_2 ∩ {θ < τ_0})] ⊆ 𝒩.

The same holds for each edge {i, j}, with θ_ij = |g_j|/|g_i| and the third class M_k.

*Proof.*
1. Suppose Sil(T) ∩ M_3 ⊄ 𝒩. By Theorem 3.1, for each τ ∈ J, O_1(τ) ⊆ 𝒩 or O_2(τ) ⊆ 𝒩.
2. The set A = {τ : O_1(τ) ⊆ 𝒩} is up-closed in J, and B = {τ : O_2(τ) ⊆ 𝒩} is down-closed. Since A ∪ B = J, put τ_0 := inf A.
3. Take countable unions over rational τ > τ_0 (for O_1) and over rational τ < τ_0 (for O_2). ∎

**Reading.**
- Every alternative in Cor 5.2 is a nonempty open cone of positive measure that reaches well inside the band.
- Relative to any one field, the non-additive part of the ranking must therefore fill, for each edge, a whole crossed cone at that edge's seam (or a whole class band). Which side carries it is a design choice, by Theorem 5.1.
- A fixed cone must be covered. Take τ_m := (α+β)/2. Every crossed cone X_12(τ_0) contains O_1(τ_m) (if τ_0 ≤ τ_m) or O_2(τ_m) (if τ_0 ≥ τ_m). So 𝒩 ⊇ O_1(τ_m), or 𝒩 ⊇ O_2(τ_m), or 𝒩 ⊇ Sil(T) ∩ M_3. These are three fixed open cones that depend only on ε.
- So the non-additive part is not bounded, not null, and not confined to a δ-neighbourhood of the coordinate planes or of ∂Sil(T), for any δ below a constant depending only on ε. This is FF2 Thm 4.1's conclusion for T1, now without continuity in measure.

**Remark.** P_3 can be any non-null subset of M_3 on which T is not correct at worlds 1 and 2. That includes Ans(T) ∩ M_3 where T gives the minority answer. Majority fills there also give slack at worlds 1 and 2. P_3 cannot be dropped:
- with λ_3 = 0 and φ ≡ Λ on P_1 ∪ P_2, T is Bayes on P_1 ∪ P_2;
- the edge model is then indifferent;
- so nothing on the seam alone is contradictory.

---

## 6. Restrictions and extensions

**6.1 Restrictions (PROVED).** Theorem 3.1 needs endorsement only for records supported in P_1 ∪ P_2 ∪ P_3. These pieces can be chosen bounded, inside an annulus, inside Sil(T), and away from the coordinate planes, all at once. So the theorem survives each of the following:
- endorsement restricted to bounded records;
- restricted to annulus-supported records (the referee's reading of "bounded");
- restricted to records supported in Sil(T);
- any intersection of these.

Lemma 2.1 (K ⊆ edge) uses strict (G), not endorsement, so the Sil(T) restriction costs nothing on the edge side.

Recommendation: state endorsement hypotheses locally ("records supported in P"). That is the form in which they bite.

**6.2 Unions of endorsers (several densities per world).** Hypothesis: each accepted N ⪯_w X is endorsed by *some* member of a family {ρ^n_w}.

- **What still follows.** Lemma 2.3 (in R^{W×n}) still makes each model Bayes for some nonnegative combination of members. The combination can depend on the model.
- **Why the proof does not extend.** Theorem 3.1 needs T's fills and the edge model's sandwich to be judged by the same field.

**Proposition 6.1 (Bayes-level escape; PROVED; CHECKED in `union_escape.py`).** Take the family {Ω_w, |g_w|} at each world. Then:
- T1 (indeed every regular model) is Ω-Bayes at u: on mixed problems all non-contradictory answers tie;
- every precise edge model D_r is S_0-Bayes at weights (r_1, r_2).

Moreover:
- every majority fill of T has Ω-values summing to 0, so it is Ω-endorsed at some world;
- every threshold swap out of D_r is S_0-endorsed at world 1 or 2 (NUMERICS control).

So every consequence used in §§2–5 holds. Whether an actual (S)-system with union endorsement exists is **OPEN**, and the same goes for countable families.

**What it would cost.** On each seam piece:
- the member under which the edge model is Bayes must fail to endorse some accepted majority fill of T (Theorem 5.1(a) applied to that member);
- the member endorsing T must be balanced there, so it fails some accepted swap out of the edge model (Theorem 5.1(b)).

Each world's relation restricted to P is then endorsed by no single field. Unions are the minimal non-additivity left open.

The natural single-formula candidate uses a density that depends on the old advice: Ω where the old side is silent, |g_w| where it answers. That is a transition-pricing rule (DESIGN_MEMO §2.C), and those screens apply to it first.

**6.3 Lexicographic stacks (PROVED / OPEN).** Suppose N ⪯_w X implies that (∫ρ^1_w Δr, ∫ρ^2_w Δr, …) ≥_lex 0.
- **Positive leading level.** If ρ^1_w > 0 a.e. on P, then lex ≥ 0 implies the first coordinate is ≥ 0. Theorem 3.1 applies to ρ^1, so these stacks are excluded (PROVED). This covers PP23's Ω-lex and PP25's L (R46.1's cases).
- **Positive later level.** More generally, suppose that for each w some level n_w vanishes, together with every earlier level, a.e. on P, while level n_w is positive a.e. on P. Then Theorem 3.1 applies to (ρ^{n_w}_w)_w (PROVED).
- **Region-dependent leading level (OPEN).** If the leading non-vanishing level differs between the pieces P_1, P_2, P_3 (e.g. level 1 lives on M_1 and level 2 on M_2), the proof does not apply. This is lexicographic-by-region with mass sensitivity. PP26 Theorem V excludes only its veto form.

---

## 7. Status and next steps

| Result | Status |
|---|---|
| Lemma 1.1 band/seam geometry | PROVED; CHECKED |
| Lemma 2.1 edge models on the edge (strict (G) only) | PROVED; CHECKED |
| Lemma 2.2 edge covering (step (d)) | PROVED; CHECKED |
| Lemma 2.3, Prop 2.4, Cor 2.5 (edge monotonicity; general-field R46.1) | PROVED |
| Theorem 3.1, Cor 3.2 (the conjecture), Lemma 3.4, Cor 3.3 (precision) | PROVED |
| Prop 4.1 (balance, λ > 0); Examples 4.2, 4.3 (lead's (b), (c) fail as stated) | PROVED |
| Theorem 5.1 witnesses; Cor 5.2 location | PROVED; witnesses NUMERICS-illustrated |
| §6.1 restrictions survive | PROVED |
| Unions of endorsers: Bayes-level escape | PROVED; CHECKED; full extension OPEN |
| Lex stacks: positive leading level excluded; region-dependent levels | PROVED / OPEN |

**Next steps (proposals).**
1. **Design consequence.** Any (S)-cover of T1 has to judge seam-straddling records non-additively.
   - These are majority fills out of T and threshold swaps out of edge models, inside a crossed cone at each seam.
   - The same is true for every other selected imprecise interior model (Cor 3.3).
   - The cleanest remaining additive-flavoured route is a two-field union (§6.2): a balanced field for records out of silent old sides, and an edge-monotone field for records out of answered old sides. It must first pass the transition-pricing screens (DESIGN_MEMO §5.C) and (IB). In particular, records out of an imprecise edge model's silent wedge coincide with records out of T there, so (IB) forces them to receive the same verdict.
2. **Unions with closed sections.** Test whether closed sections plus (TC) exclude the {Ω, S_0} union. This is the general-field question that remains open after this note.
