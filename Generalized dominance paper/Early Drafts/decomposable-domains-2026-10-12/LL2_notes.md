# LL2 (round 40, BRIEF32). Quorum rankings: the adversary wins for every judge configuration

18 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imported facts are named.
- **CHECKED**: exact rational computation with a stated script.
- **NUMERICS**: floating point or sampling. Nothing below rests on NUMERICS.
- **CONJECTURE**.

Scripts are in `ll2py/`. Run `python3 -I <script>.py` from inside that folder. Outputs are in `*.out`. Every verdict uses `fractions.Fraction`.

Setting and notation follow the write-up §2. The setting is three worlds, any ε ∈ (0,1), and either the full four-advice domain or a decomposable domain M with advice range A(h). μ is the standard Gaussian measure: finite and atomless. No assumption is added. Every extra hypothesis below is a hypothesis of a stated result.

---

## 0. Outcome

**The obstruction is PROVED, and it is stronger than the brief asked for.**
- No quorum system of the brief's class satisfies (S) with **any** selection, coherent or not, and for any target. This covers any n, any q ≤ n, weighted quorums with any threshold τ > 0, and margins η ∈ (0,1) that may depend on the world, the judge or the selected model.
- So no quorum system covers T1, on the full domain or on any decomposable domain with (LF) at T1.
- Of the brief's quorum conditions, only 2q > n is used, and only in variant (b). The condition 3q > 2n is not used.

**The chain.**
1. **Exact reduction (Lemma 2.1, PROVED).** C is competitive on S exactly when, for every choice of blocking coalitions (the brief's C(n, n−q+1)^|S| branches), C is a pointwise weak Bayes model of a **distorted** mixture of that branch's judges.
   - "Distorted" means each judge's local change Δ is replaced by Δ − η|Δ|.
   - This is the brief's 216-branch test made exact, by Lyapunov and separation.
   - The obstruction needs only **one** branch: all judges.
2. **Gap lemma (Lemma 3.1, PROVED; sharp, CHECKED).** If two models are distorted-Bayes at mixture weights α and α′ with the same support, and every ratio α′_iv/α_iv lies in (1/κ, κ) with κ = (1+η)/(1−η), then the two models are equal a.e.
   - The proof is one line: add the two pointwise conditions on the set where the models disagree.
   - Heterogeneity of the judges plays no role. Lemma 3.2 allows one world with no margin at all.
3. **Countability (Proposition 4.1, PROVED).** By compactness of the finite-dimensional weight simplex, **at most countably many models are competitive on any nonempty set of worlds**.
4. **Theorem 5.1 (PROVED).** A countable-valued selection through the two distinct vertex models W_1, W_2 cannot be continuous in measure, because the image of the connected simplex would be connected. Nor can it have closed sections when there are no nontrivial ties: its level sets would then be closed, and Sierpiński's theorem applies.
5. **The explicit adversary (Proposition 6.1, PROVED; illustration CHECKED at T1).** This is the brief's Bayes-neutral mixture, made exact.
   - Take a point of a model's boundary where every judge is approximately continuous.
   - Move equal tiny masses across the boundary in opposite directions.
   - Every judge at every world then sees net change ≈ 0 and gross change > 0. All judges fail, whatever their heterogeneity, because they all see the same two problem types in mirror image.
   - Hence the boundary of any competitive coherent model must lie inside the judges' (null) set of approximate discontinuity. The proof in step 2 removes the need for any regularity.
6. **The FF2 route (Proposition 7.1, PROVED; CHECKED).** The sum of the judges endorses every accepted comparison exactly when 2qη + (n−q)[(1+η)/M − (1−η)M] ≥ 0. Here M bounds the pointwise judge-to-judge ratio.
   - Under that condition, FF2 Theorem 4.1 already applies, modulo FF2's import chain.
   - Heterogeneity M > M*(n,q,η) escapes FF2, but not Theorem 5.1, which needs no import chain at all.
7. **What survives (§8, PROVED).** Theorem 5.1 needs uniformly *linear* margins at small scale for one blocking family at every world but at most one. So a surviving quorum system must have at least **two worlds** at each of which at least **q judges** (weight ≥ τ) have **sublinear** margins: liminf_{s↓0} ψ_iv(s)/s = 0.
   - Such systems keep every elementary property the audit proved: (IB), strict (G), (TC), no ties, closed sections, direct (C), and automatic undominatedness (Proposition 8.2).
   - In them, small records impose: for every blocking branch, C_q is a pointwise weak (undistorted) Bayes model of some nonnegative mixture of that branch's judges (Proposition 8.3).

**Does the argument use (IB), (TC) or closed sections?**
- (IB): never. (TC): never, and neither is 3q > 2n.
- Closed sections: only in variant (b) of Theorem 5.1. There they serve as the substitute for continuity in measure, together with reflexivity and no nontrivial ties (from 2q > n). Variant (a) uses continuity in measure and none of these.
- Also unused: coherence of selected models, T1 (except that (LF) at T1 makes W_1 ≠ W_2), transitivity, (C) and (LA).

**Single most important open point.** In the surviving class (sublinear margins at two or more worlds), can a coherent selection, continuous in measure and through T1, be pointwise weakly Bayes for a judge mixture inside every blocking branch at every q? This is Proposition 8.3's necessary condition. FF2 Theorem 4.1 excludes it when one mixture can be fixed for all q; with mixtures varying in q it is open.

---

## 1. The class

**Judges.** For each world i there is a finite set J_i of judges. Judge v has a measurable penalty ℓ_iv(h,a), a ∈ A(h), with integrable envelope, and it is strictly increasing in world-i rank on A(h) for a.e. h. For models C, X write:
- Δ_iv(h; a→b) := ℓ_iv(h,b) − ℓ_iv(h,a);
- N_iv(C,X) := ∫ Δ_iv(h; a_C(h)→a_X(h)) dμ = L_iv(X) − L_iv(C);
- G_iv(C,X) := ∫ |Δ_iv(h; a_C(h)→a_X(h))| dμ = d_iv(C,X).

Off the coordinate planes, which are null, the four advices have four distinct world-i ranks. So for a.e. h and a ≠ b in A(h), Δ_iv(h; a→b) ≠ 0 for every i and v, and the sign of Δ_iv(h; a→b) does not depend on v. In particular G_iv(C,X) > 0 whenever X ≠ C.

**The endorsement hypothesis (E_i).** Let 𝒞 ⊆ M be a class of models (below, the selected models). World i satisfies (E_i) with **blocking family** B_i ⊆ J_i and margin η_i ∈ [0,1) if the following holds.
- For every C ∈ 𝒞 there is s_0(C) ∈ (0, ∞].
- For every evaluable X ≠ C with G_iv(C,X) ≤ s_0(C) for all v ∈ B_i, if
  N_iv(C,X) < η_i G_iv(C,X) for every v ∈ B_i,
  then not C ⪯_i X.

In words: a comparison out of C that every judge of B_i fails to support with margin η_i is not accepted, at least for small records.

**Instances (PROVED, immediate).**
- (i) **The brief's class.** Take B_i = J_i, η_i = η (or η depending on i), s_0 = ∞. If every judge has N < ηG, nobody supports the comparison, and q ≥ 1 votes are needed.
- (ii) **Weighted quorums.** Accept if the supporters' weight is at least τ > 0. Take B_i = J_i again. Any B_i whose complement has weight < τ also works.
- (iii) **Judge-dependent margins.** Each judge has a margin function ψ_iv, and supports iff N_iv ≥ ψ_iv(G_iv). Suppose there are η, s_0 > 0 and a blocking family B_i with ψ_iv(s) ≥ ηs for all s ≤ s_0 and v ∈ B_i. In the quorum case a blocking family is any set of n−q+1 judges.
- (iv) **Margins depending on the selected model.** Margins η_i(C) > 0 are allowed; see Remark 4.2.

With η_i = 0, (E_i) says that every accepted comparison out of C is weakly endorsed (N ≥ 0) by at least one judge of B_i.

---

## 2. The exact reduction

For an index set I_S := ⊔_{i∈S} B_i, let Σ_S be the set of nonnegative, nonzero vectors α on I_S normalised to sum 1. Say that C is **distorted-Bayes at α** if for a.e. h and every b ∈ A(h):

  Σ_{(i,v)∈I_S} α_iv [Δ_iv(h; a_C(h)→b) − η_i |Δ_iv(h; a_C(h)→b)|] ≥ 0.   (DB)

**Lemma 2.1 (PROVED).** Let S ≠ ∅, let every i ∈ S satisfy (E_i), and let C ∈ 𝒞 be competitive on S. Then C is distorted-Bayes at some α ∈ Σ_S.

Conversely, take the brief's class, with global linear margins and s_0 = ∞, and let C be any model. If for every choice of B_i ⊆ J_i with |B_i| = n−q+1 (i ∈ S) the model C is distorted-Bayes at some α supported on ⊔B_i, then C is competitive on S. So the 216-branch test is exact.

*Proof.*
1. **The attainable set.** For evaluable X put z_iv(X) := N_iv(C,X) − η_i G_iv(C,X) = ∫ f_iv(h, a_X(h)) dμ, where f_iv(h,b) := Δ_iv(h; a_C(h)→b) − η_i|Δ_iv(h; a_C(h)→b)|. Each |f_iv| is bounded by twice the envelope, so it is integrable.
   - Z := {z(X) : X ∈ M} ⊆ ℝ^{I_S} is convex. Given X, Y and t ∈ [0,1], Lyapunov's theorem for the atomless finite-dimensional vector measure E ↦ (∫_E f(h,a_X), ∫_E f(h,a_Y)) gives E_t with both coordinates equal to t times their totals. The splice of X on E_t with Y off E_t is evaluable (decomposability) and has z = t z(X) + (1−t) z(Y). This is FF2 Step 1, refereed in GG3 §8.1.
   - 0 = z(C) ∈ Z.
2. **No point of Z in the open negative orthant.** Suppose z(X) < 0 componentwise.
   - Apply Lyapunov to E ↦ (∫_E Δ_iv, ∫_E |Δ_iv|)_{(i,v)∈I_S} on the disagreement set of C and X. For each t ∈ (0,1) this gives a splice X_t with N_iv(C,X_t) = tN_iv(C,X) and G_iv(C,X_t) = tG_iv(C,X) for all (i,v) ∈ I_S.
   - For small t, G_iv(C,X_t) ≤ s_0(C), and N_iv(C,X_t) − η_iG_iv(C,X_t) = t z_iv(X) < 0.
   - By (E_i), not C ⪯_i X_t at every i ∈ S. Since X_t ≠ C, this contradicts competitiveness.
3. **Separation.** Separate the convex set Z from the open convex cone {z < 0}. This gives α ≠ 0 and c with α·z ≥ c ≥ α·y for all z ∈ Z and y < 0. The supremum of α·y over y < 0 is finite only if α ≥ 0, and it is then 0. So α ≥ 0 and α·z ≥ 0 on Z. Normalise α into Σ_S.
4. **Pointwise.** The set P := {h : α·f(h,b) < 0 for some b ∈ A(h)} is measurable. If it were non-null, choose b(h) measurably on P (first admissible advice in a fixed order), and let X be C with advice b on P. Then α·z(X) = ∫_P α·f(h,b(h)) dμ < 0, a contradiction. So (DB) holds.
5. **Converse.** Suppose C is not competitive on S. Then some X has, at each i ∈ S, fewer than q supporters. So at least n−q+1 judges fail, and we choose B_i among them; thus z_iv(X) < 0 for all (i,v) ∈ ⊔B_i. Integrating (DB) at b = a_X(h) gives α·z(X) ≥ 0, which is impossible. ∎

*Remark 2.2.* The judges at world i share the sign of each local change, so Σ_v α_iv(Δ_iv − η|Δ_iv|) is the distortion of the single field m_i := Σ_v α_iv ℓ_iv. Thus (DB) says that C is weakly Bayes, with margin, for the field m = (m_1, m_2, m_3), with world weights absorbed. Lemma 3.1 does not need this remark.

---

## 3. The gap lemmas

Below, α and α′ are nonnegative, nonzero vectors on a common finite index set I := ⊔_i B_i. Both may have zeros. Pointwise conditions for different models are compared on their common co-null set.

**Lemma 3.1 (PROVED).** Suppose η_i ≥ η > 0 at every world, and put κ := (1+η)/(1−η). Let C be distorted-Bayes at α and C′ at α′, and suppose:
- supp α = supp α′;
- α′_iv/α_iv ∈ (1/κ, κ) on the support.

Then C = C′ a.e.

*Proof.*
1. Let E := {h : a_C(h) ≠ a_{C′}(h)}, and suppose μ(E) > 0. For a.e. h ∈ E put a := a_C(h), b := a_{C′}(h) ∈ A(h) and Δ_iv := Δ_iv(h; a→b), which is nonzero for every (i,v).
2. C's condition (DB) at b, and C′'s at a, read:
   - Σ α_iv(Δ_iv − η_i|Δ_iv|) ≥ 0;
   - Σ α′_iv(−Δ_iv − η_i|Δ_iv|) ≥ 0.
3. Adding them gives Σ(α_iv − α′_iv)Δ_iv ≥ Σ η_i(α_iv + α′_iv)|Δ_iv|.
4. The ratio condition is equivalent to |α_iv − α′_iv| < η(α_iv + α′_iv) ≤ η_i(α_iv + α′_iv) on the support. Both sides vanish off the support. The support is nonempty and every |Δ_iv| > 0.
5. Hence Σ(α−α′)Δ ≤ Σ|α−α′||Δ| < Σ η_i(α+α′)|Δ|, a contradiction. ∎

*Sharpness (CHECKED, `gap_check.py` Part A).*
- 16 000 random exact instances satisfy the strict inequality.
- With ratios exactly 1/κ and κ, one two-world problem satisfies both conditions with equality, for η = 1/16, 1/4, 1/2. So the open ratio interval cannot be closed.

**Lemma 3.2 (PROVED; one world without margin).** Suppose η_1 ≥ 0 is arbitrary and η_i ≥ η > 0 for every other world i. Choose ρ > 1 with (ρ−1)(ρ²+1) < η(1 + 1/ρ); for example ρ = 1 + η/4. If C is distorted-Bayes at α, C′ at α′, supp α = supp α′, and α′_iv/α_iv ∈ [1/ρ, ρ] on the support, then C = C′ a.e.

*Proof.*
1. **Setup.** Use the notation of Lemma 3.1 on E. Let s_i be the common sign of Δ_iv at world i, and put A_i := Σ_v α_iv|Δ_iv| and A′_i := Σ_v α′_iv|Δ_iv|. Then A′_i ∈ [A_i/ρ, ρA_i], and Σ_i A_i > 0.
2. **The two conditions.** Taking the worst case η_1 = 0:
   - (C) Σ_i (s_i − η_i)A_i ≥ 0;
   - (C′) Σ_i (−s_i − η_i)A′_i ≥ 0.
3. **World 1 is controlled by the others.** Put R := Σ_{i≠1} A_i.
   - If s_1 = +, (C′) gives A′_1 ≤ Σ_{i≠1} A′_i ≤ ρR, so A_1 ≤ ρ²R.
   - If s_1 = −, (C) gives A_1 ≤ R.
   - In both cases A_1 ≤ ρ²R, so R > 0.
4. **Adding.** (C) + (C′) gives Σ_i s_i(A_i − A′_i) ≥ η(R + R′) ≥ η(1 + 1/ρ)R. But |A_i − A′_i| ≤ (ρ−1)A_i, so the left side is at most (ρ−1)(1+ρ²)R. This contradicts the choice of ρ. ∎

*Checks (CHECKED, `gap_check.py` Part B).*
- Exact random instances with ρ = 1 + η/4 never satisfy both conditions.
- **The lemma fails with two free worlds:** A = (N, N, 1), A′ = (N, N+2, 1), signs (+, −, +) and η_3 = 1/4 satisfy both conditions, with ratio 1 + 2/N → 1.

This explains the survivor condition of §8. It is not evidence for a cover.

---

## 4. Competitive models are countable

**Proposition 4.1 (PROVED).** Suppose every world satisfies (E_i) on 𝒞, with margins η_i ≥ η > 0 at all worlds but at most one. Then the models C ∈ 𝒞 that are competitive on at least one nonempty set of worlds form a countable set, modulo null sets.

*Proof.*
1. **Each such C has a weight.** By Lemma 2.1, C is distorted-Bayes at some α ∈ Σ_S, extended by zero to I; (DB) does not change. Let Σ be the set of nonnegative, nonzero vectors on I with sum 1, and fix ρ as in Lemma 3.2. If no world is free, any 1 < ρ < κ works instead, by Lemma 3.1.
2. **Compact pieces.** For nonempty P ⊆ I and m ≥ 1, let K_{P,m} := {α ∈ Σ : supp α = P, α_iv ≥ 1/m on P}. It is compact, and the sets K_{P,m} exhaust Σ.
3. **Finite covers.** For α° ∈ K_{P,m}, let B(α°) := {α : supp α = P, α_iv/α°_iv ∈ (ρ^{−1/2}, ρ^{1/2})}. Its trace on K_{P,m} is relatively open, and any two of its members have ratios in [1/ρ, ρ]. By compactness, finitely many B(α°) cover K_{P,m}.
4. **One model per ball.** By Lemma 3.2 (or 3.1), all models distorted-Bayes at weights in one B(α°) coincide.
5. **Counting.** So finitely many models have a weight in K_{P,m}, and countably many in all. ∎

*Remark 4.2 (PROVED).* If the margin depends on the model, η_i = η_i(C) > 0, apply the proof to {C : min_i η_i(C) ≥ 1/k} for each k. Lemma 3.1 needs only min(η(C), η(C′)) ≥ η. The union of these countable sets is countable.

---

## 5. The theorem

Let W_i denote the world-i best evaluable model, which has the pointwise best world-i advice in A(h). It exists and is measurable, since A(h) is finite and measurable.

**Lemma 5.0 (PROVED).** Suppose world i satisfies (E_i) on 𝒞 with any η_i ≥ 0, and C ∈ 𝒞 is competitive on {i}. Then C = W_i a.e.

Moreover, W_1 ≠ W_2 on the full domain and on every decomposable domain with (LF) at T1.

*Proof.*
1. **C = W_i.** Suppose C ≠ W_i. On the record C → W_i every world-i judge has Δ ≤ 0 pointwise, with strict inequality on the disagreement set. So N_iv = −G_iv < 0 ≤ η_iG_iv.
   - Lyapunov scaling, as in Lemma 2.1 step 2, gives arbitrarily small sub-records with the same property.
   - (E_i) rejects them, so C is not competitive on {i}.
2. **W_1 ≠ W_2 under (LF).**
   - The corner ray r_23 = (κ+1, −1, −1) lies in ∂D_{T1}∖{0}, so the open set of (LF) contains a ball around it.
   - On that ball, h_1 > 0 > h_2, and for a.e. pair the advice range contains "accept h" and silence.
   - "Accept h" is good, rank 0, at world 1. So W_1 accepts h.
   - It is bad at world 2, where silence is better. So W_2 does not accept h. ∎

**Theorem 5.1 (PROVED).** Let M be the full domain or any decomposable domain. Let ⪯_1, ⪯_2, ⪯_3 be any relations on M, and let p ↦ C_p ∈ M (p ∈ Δ) be a selection competitive on supp p for every p, with 𝒞 := {C_p}. Assume:
- every world satisfies (E_i) on 𝒞, with margins η_i ≥ η > 0 at all worlds but at most one;
- W_1 ≠ W_2.

Then:
- **(a)** the selection is not continuous in measure;
- **(b)** if each ⪯_i is reflexive on 𝒞 and has no nontrivial ties on 𝒞 (C ⪯_i C′ and C′ ⪯_i C imply C = C′), then some section {p : C_p ⪯_i C_{p′}} is not closed.

In particular, (S) fails for every ranking with these properties, whatever the target and whether or not the selected models are coherent.

*Proof.*
1. **Countably many values.** By Proposition 4.1, the set {C_p : p ∈ Δ} is countable. By Lemma 5.0, it contains W_1 = C_{e_1} and W_2 = C_{e_2}, which are distinct.
2. **(a).** If the selection were continuous in measure, its image would be a connected subset of the metric space (models mod null, μ(X △ Y)). It is countable and has two points, which is impossible. For x_0 := W_1, choose r ∈ (0, μ(W_1 △ W_2)) that is not a value of μ(x_0 △ ·). Then {x : μ(x_0 △ x) < r} is a nontrivial clopen subset of the image.
3. **(b), level sets closed.** Write P_k := {p : C_p = Y_k} for the distinct values Y_k. Let p* ∈ cl P_k and Y := C_{p*}.
   - For each i, the section {p : C_p ⪯_i Y_k} is closed and contains P_k, by reflexivity. So it contains p*, and Y ⪯_i Y_k at every world.
   - If Y ≠ Y_k, the absence of nontrivial ties gives "not Y_k ⪯_i Y" at every world.
   - But Y_k = C_p for some p ∈ P_k is competitive on supp p ≠ ∅, so Y_k ⪯_i Y at some i. This is a contradiction, so p* ∈ P_k.
4. **(b), conclusion.** Δ is a continuum partitioned into countably many pairwise disjoint nonempty closed sets P_k. By Sierpiński's theorem there is only one such set, contradicting W_1 ≠ W_2. ∎

**Corollary 5.2 (PROVED).** No quorum system satisfies (S), and so none covers T1, on the full domain or on any decomposable domain with (LF) at T1. This holds for:
- n judges per world, integrable strictly guiding additive losses, margin η ∈ (0,1) (possibly world- or judge-dependent), and any quorum 1 ≤ q ≤ n;
- weighted quorums with any threshold τ > 0;
- margin functions ψ_iv with ψ_iv(s) ≥ ηs near 0 for n−q+1 judges at every world but at most one.

Variant (a) excludes selections continuous in measure for every q. Variant (b) excludes selections with closed sections whenever 2q > n (weighted: 2τ > total weight).

*Proof.* Instances (i)–(iii) of §1 give (E_i). Reflexivity holds because the identity record has n votes. 2q > n gives no nontrivial ties, as the audit shows. Lemma 5.0 gives W_1 ≠ W_2. ∎

*Remarks.*
- With 2q ≤ n, variant (b) needs a separate argument. It is not given here, and is not needed for the brief's class.
- The theorem holds for any finite number of worlds (at least 2) with W_1 ≠ W_2. It is not specific to T1, which is used only to supply W_1 ≠ W_2 via (LF).
- It also excludes **single-judge η-margin rankings** (n = 1) and **unanimity** (q = n). So the obstruction comes from the linear margin at small scale combined with finitely many judges. Aggregation is not the cause.

---

## 6. The explicit adversary: the mirror swap

This is the brief's "Bayes-neutral mixture near T1's boundary", in a form that defeats every judge at once.

**Proposition 6.1 (PROVED).** Let C be a model, h_0 a point, and a ≠ b advices. Put P_a := {a_C = a} and P_b := {a_C = b}, and assume:
- **(i)** both P_a and P_b have positive lower density at h_0, and b ∈ A(h) on P_a and a ∈ A(h) on P_b near h_0 (the full domain, or an (LF) region);
- **(ii)** for each judge (i,v) of a finite family 𝒥, the switch map f_iv(h) := Δ_iv(h; a→b) has a finite nonzero approximate limit δ_iv at h_0.

Then for every η > 0 and s > 0 there is a model X that differs from C only on a set of measure < s inside any prescribed ball around h_0, such that every judge of 𝒥 has N_iv(C,X) < η G_iv(C,X). Hence, if 𝒥 ⊇ ⊔B_i, C is competitive on no nonempty set of worlds in any ranking with (E_i) at every world.

*Proof.*
1. Let θ := η/3 < η/(1+η). The set of h with |f_iv(h) − δ_iv| > θ|δ_iv| for some (i,v) ∈ 𝒥 has density 0 at h_0.
2. For small r, remove it from P_a ∩ B_r(h_0) and from P_b ∩ B_r(h_0). Since μ is atomless, choose subsets A′ and B′ of equal measure m > 0 inside what remains.
3. Let X be C with b on A′ and a on B′. On B′ the change is b→a, with Δ = −f_iv.
4. So N_iv = ∫_{A′}f_iv − ∫_{B′}f_iv, which gives |N_iv| ≤ 2θm|δ_iv|. Also G_iv ≥ 2(1−θ)m|δ_iv|.
5. Hence N_iv < ηG_iv. Taking m small makes the record small, and (E_i) rejects it at every world. ∎

*Reading.* Each judge sees the same problem types in mirror image, so heterogeneity across judges is irrelevant. Only each judge's own local continuity matters. Lyapunov purification is not needed here; it is needed only in §2 to make the converse test exact.

**Corollary 6.2 (PROVED).** Suppose a coherent D_K is competitive on some nonempty set of worlds, in a ranking with (E_i) at every world, on a domain where accept and silence are available near ∂D_K. Then at every mixed point h_0 ∈ ∂D_K∖{0} off the coordinate planes, some switch map h ↦ Δ_iv(h; + → 0) with (i,v) ∈ ⊔B_i fails to have a finite nonzero approximate limit.

*Proof.* Near such h_0, D_K accepts on the convex side, which has positive lower density, and is silent on the other side, which contains a half-space through h_0. Apply Proposition 6.1. ∎

So the boundary of every competitive coherent model lies inside one fixed null set: the judges' approximate-discontinuity set. This holds in particular for T1 itself.

T1 alone can therefore be defended, but only by judges that jump across ∂D_{T1}. Lemma 3.1 is what turns "every selected boundary must sit on the jump set" into a global contradiction, with no regularity assumed.

*Illustration (CHECKED, `swap_T1.py` → `swap_T1.out`).*
- Setting: ε = 3/10, h_0 = r_12 + r_31 = (−2, 16/7, 16/7) ∈ relint F_1, and four judges per world with polynomial densities. The densities are deliberately heterogeneous, with scales 1, 1000, 1/1000 and 37/3.
- The two-point surrogate has equal masses at h_0 ± t v_1. T1 accepts at h_0 + t v_1 and is silent at h_0 − t v_1.
- At t = 1/1000, every judge at every world fails for η = 1/16, 1/4, 1/2 and 9/10, with max N/G ≈ 4·10⁻³.
- At t = 1/10, the configuration is too coarse for η ≤ 1/4. This is as expected: the swap needs local continuity at the scale of the record.

---

## 7. The FF2/HH2 route, and exactly when it applies

**Proposition 7.1 (PROVED; CHECKED).** Fix a world, the quorum rule with n, q and margin η, and suppose a pointwise ratio bound |Δ_v| ≤ M|Δ_w| holds for all judges v, w (a.e., all switches). Then the sum field Σ_v ℓ_v endorses every accepted comparison, Σ_v N_v ≥ 0, for every such configuration iff

  2qη + (n−q)[(1+η)/M − (1−η)M] ≥ 0,  i.e. M ≤ M* := [qη + √(q²η² + (n−q)²(1−η²))] / ((n−q)(1−η)).

*Proof.*
1. **Sufficiency.** Write W_v and I_v for the worsened and improved masses, so N_v = W_v − I_v. Supporters w ∈ Q (|Q| ≥ q) have I_w ≤ θW_w, where θ = (1−η)/(1+η).
   - The common sign and the ratio bound give W_v ≥ W_w/M and I_v ≤ MI_w for every non-supporter v and every w ∈ Q. Average over w ∈ Q.
   - Then Σ_v N_v ≥ Σ_{w∈Q} W_w [1 + (n−q)/(qM) − θ(1 + (n−q)M/q)], which is ≥ 0 iff the displayed inequality holds. (Taking |Q| = q is the worst case.)
2. **Necessity.** Take q identical supporters with I = θW, and n−q non-supporters with magnitudes ×1/M on the worsening set and ×M on the improving set. This configuration is realisable: the ratios lie in [1/M, M] pointwise. The comparison is accepted, and the sum equals W[q(1−θ) + (n−q)(1/M − Mθ)].

*Checks (CHECKED, `endorse_check.py` → `endorse_check.out`).*
- n = 4, q = 3: M* ≈ 1.2832 for η = 1/16, 2.6330 for η = 1/4, and 6.4641 for η = 1/2.
- The worst case just above M* is accepted with three votes and has negative sum.
- Random exact records with ratio ≤ M* show no accepted comparison with negative sum.

*Consequences.*
- When M ≤ M* at every world, (H3) of FF2 Theorem 4.1 holds with ℓ_i := Σ_v ℓ_iv, an integrable strictly guiding field. So FF2 excludes coherent continuous selections through T1, modulo its import chain (D1, BB2 Thm 6.1, M3.7–3.8).
- Heterogeneity M > M* escapes this route, and the audit's certificate is of that kind.
- HH2 Thm 5.1 needs (Loc_i), whose sub-records may change the supporting coalition. I did not verify (Loc_i) for heterogeneous quorums, and it is not needed.
- **Theorem 5.1 supersedes all three routes for this class.** It needs no import chain, no coherence, no T1 and no bound on heterogeneity.

---

## 8. What survives: the exact boundary of the obstruction

**Proposition 8.1 (PROVED; restatement of the hypotheses).** In the quorum class with margin functions ψ_iv(s) (support iff N ≥ ψ_iv(G)), the hypotheses of Theorem 5.1 hold unless at least **two** worlds each have no blocking family of uniformly linear judges. That means at least q judges (weighted: weight ≥ τ) with liminf_{s↓0} ψ_iv(s)/s = 0. A judge with ψ(s) ≥ ηs on [0, s_0] for some η, s_0 > 0 counts as linear.

So a constructor must put sublinear margins on a quorum of judges at two or more worlds. Lemma 3.2's two-free-world failure (§3) shows that the gap mechanism does not extend there.

**Proposition 8.2 (PROVED).** Let ψ_iv be continuous with 0 < ψ_iv(s) ≤ s for s > 0, and use 2q > n and 3q > 2n. For example, take ψ(s) = ηs²/(1+s). Then every property the audit proved remains:
- (IB): N and G depend only on the record.
- Strict (G): a strict pointwise improvement has N = G ≥ ψ(G) in one direction and N = −G < 0 < ψ(G) in the other.
- No nontrivial ties: two quorums share a judge, and ψ > 0.
- (TC): a supporter strictly lowers its own loss on each supported edge between distinct models, so it supports at most two edges of a triangle. A forbidden triangle needs 3q votes, more than the 2n available.
- Closed sections for selections continuous in measure: L_iv(C_p), d_iv(C_p, X) and ψ are continuous.
- Direct (C), and undominatedness of competitive selected models: these follow from no ties, as in the audit.

**Proposition 8.3 (PROVED).** In the class of Proposition 8.2, let C be competitive on S. Then for every branch (V_i)_{i∈S} with |V_i| = n−q+1, C is a pointwise weak Bayes model of a nonnegative nonzero mixture of the judges in ⊔V_i. This is (DB) with all η_i = 0.

*Proof.* Lemma 2.1 with η_i = 0. Step 2 there needs only that a judge with N < 0 does not support, which holds since ψ ≥ 0; no smallness is needed. ∎

*Remarks.*
- **The constructor's target.** Choose n integrable strictly guiding fields per world and a coherent family C_q, continuous in measure and through T1, such that for every q and every branch, C_q is pointwise weakly Bayes for some mixture inside the branch. Competitiveness against large records is a further requirement, because ψ is only sublinear near 0.
- **Unanimity is excluded.** For q = n the branch is one judge per world, which is a fixed field. FF2 Theorem 4.1 applies with ℓ_i := ℓ_{i,v} for any judge v: unanimity gives N ≥ ψ ≥ 0, which is (H3). This is PROVED modulo FF2's import chain.
- For q < n each branch has at least two judges, and the mixture may vary with q. FF2's Step 4, the property (γ) for one fixed field, then has no counterpart. That is the open point of §0.

---

## 9. What is used

| Result | Used | Not used |
|---|---|---|
| Lemma 2.1 | Lyapunov (atomless μ, integrable envelopes), decomposability, (E_i), competitiveness | (IB), (TC), transitivity, closed sections, coherence, T1 |
| Lemmas 3.1, 3.2 | strict guidance (Δ ≠ 0), pointwise (DB) | judges' signs (3.1), any regularity of the judges |
| Prop 4.1 | finitely many judges, compactness of the simplex | continuity of the selection |
| Thm 5.1(a) | continuity in measure, W_1 ≠ W_2 | closed sections, 2q > n, 3q > 2n |
| Thm 5.1(b) | closed sections at selected models, reflexivity, no nontrivial ties (2q > n), Sierpiński | continuity, 3q > 2n |
| Prop 6.1 | approximate continuity at one boundary point | Lyapunov, the selection |
| Prop 7.1 | pointwise ratio bound | — |

---

## 10. Status and files

| Item | Statement | Label |
|---|---|---|
| 2.1 | competitiveness ⇔ distorted weak Bayes for every blocking branch (⇒ for any (E)-ranking; ⇔ in the brief's class) | PROVED |
| 3.1 | gap lemma; the ratio interval (1/κ, κ) is sharp | PROVED; sharpness CHECKED |
| 3.2 | gap lemma with one margin-free world; fails with two | PROVED; failure CHECKED |
| 4.1, 4.2 | competitive models are countable | PROVED |
| 5.0 | vertex selections are the world-best models; W_1 ≠ W_2 under (LF) | PROVED |
| 5.1 | no continuous, or closed-section, competitive selection in any linear-margin system | PROVED |
| 5.2 | no quorum system satisfies (S); none covers T1 (full domain, every decomposable (LF) domain) | PROVED |
| 6.1, 6.2 | mirror swap defeats every judge; competitive coherent boundaries lie in the judges' jump set | PROVED; T1 illustration CHECKED |
| 7.1 | exact sum-field endorsement condition; FF2 then applies | PROVED; CHECKED |
| 8.1–8.3 | survivors need sublinear margins on a quorum at ≥ 2 worlds; they keep the audit's properties; their small-record condition | PROVED |
| — | whether a sublinear-margin quorum system covers T1 | open |

**Files (`ll2py/`).**
- `gap_check.py` → `gap_check.out`: Lemma 3.1 random exact tests and sharpness; Lemma 3.2 tests; the two-free-world failure family.
- `swap_T1.py` → `swap_T1.out`: the mirror swap at T1's facet F_1 with heterogeneous judges.
- `endorse_check.py` → `endorse_check.out`: Proposition 7.1, the threshold M* and its worst case.
