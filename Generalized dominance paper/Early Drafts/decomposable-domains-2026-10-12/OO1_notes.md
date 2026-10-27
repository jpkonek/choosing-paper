# OO1 (round 43, BRIEF35). The negative side for finite quorum systems through T1: the exact fixed-field lemma, the proved implication, and how far the continuum of indices carries it

19 Oct 2026. Rules of BRIEF13 and BRIEF35. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named, with their recorded status.
- **CHECKED**: exact rational computation with a stated script in `oo1py/`.
- **NUMERICS**: none used.
- **CONJECTURE**: marked where offered. An **open** lemma is a precisely stated statement that is neither proved nor offered as likely.

Script (run `python3 -I rank3_pointed.py` from inside `oo1py/`; the output ends with `ALL CHECKS PASSED`):
- `rank3_pointed.py` → `rank3_pointed.out` (Remark 6.4: rank-three fixed-column data whose six pattern vectors are not positively dependent; all 42 875 five-of-seven branches).

Nothing in a proof rests on the script.

Setting: the write-up §2, AUDIT_LL, MM2 §1, NN2 §1. Three worlds; μ standard Gaussian; T1 = D_K, K = (1−ε)u + εΔ. At each world i there are n strictly guiding additive judges ℓ_iv (v ∈ J_i) with a common integrable envelope; quorum q; blocking size b := n − q + 1. No assumption is added: every extra hypothesis is a hypothesis of the result that states it.

---

## 0. Outcome

**Criterion (i) is NOT met.** I do not prove that no finite quorum system has a coherent selection, continuous in measure through T1, satisfying (QS).

**Criterion (ii) is met, in the following form.**

1. **The exact missing lemma (§2).** I state Lemma FF ("fixed factorised field"): every (QS) family through T1 admits ONE strictly guiding integrable additive field ℓ* = (ℓ*_1, ℓ*_2, ℓ*_3), built from the judges with problem-dependent nonnegative weights, and ONE weight t(p) ∈ Δ_{supp p} for each index, such that every selected model C_p is a pointwise weak ℓ*-Bayes model at t(p). Status: **open**.
   - It is exactly the input consumed by FF2 Theorem 4.1 Steps 2–6, and it is the weakest fixed-field statement of that form: ℓ* may mix the judges with weights depending on the problem h, and only weak Bayes is asked.
   - Logical honesty (Remark 2.3). Because Lemma FF's conclusion is contradictory, "a (QS) family exists ⇒ FF" is logically equivalent to the impossibility theorem. Its value is as the precise target of a fixed-field rigidity proof. That is why §§4–5 split it into sub-lemmas that are **not** individually equivalent to the theorem, and prove every link of the chain except two.
2. **The implication (Theorem 3.1, PROVED modulo the FF2 Theorem 4.1 Step 6 import chain: D1, BB2 Thm 6.1 with AUDIT_BB Lemma 2.0, M3.7–M3.8, each refereed once).** Lemma FF implies the impossibility theorem (Theorem T, §1) on the full domain, for every n and q (3q > 2n is not even used in this step).
3. **A concrete global sufficient form (Proposition 4.1, PROVED).** A blocking set at each world with constant-ratio proportional penalty differences on {+,0,−}, required **only on mixed problems**, implies Lemma FF. This contains MM1 Proposition 3.2 and NN2 Corollary 3.4.
4. **Boundary information suffices, if it is uniform (Theorem 5.4, PROVED).** This is the "continuum of indices" step the brief asked about.
   - Sweep (Lemma 5.1): every mixed problem h at which the switch maps are approximately continuous is an essential boundary point of C_p for interior indices p on both the acceptance side and the rejection side. At each such point a definite switch type is a common essential value, and the type is forced: accept/silence (c) or silence/reject (c′) unless C_p is precise along h, in which case accept/reject (d).
   - Consequently (Theorem 5.4): suppose the blocking-set proportionality holds, with p-independent sets and ratios, only at the switch type that the boundary actually exposes (hypothesis UB). Add a mild silence condition S0 for the problems whose every boundary is precise. Then Lemma FF follows. The proof needs a new device: on problems where only the accept/reject switch is exposed, the silence penalty is replaced by the midpoint of the two acceptance penalties (Lemma 5.3).
   - Uniformity across indices is automatic along linked boundaries (Proposition 5.5, PROVED): the ratios are properties of the judges at h, not of p. So, given per-index interior collapse (L1, which is NN2 Conjecture 6.4 with a fixed blocking set), UB reduces to a precise linking hypothesis (Link) on the family of boundaries.
5. **The chain, with statuses (§5.4):**

     (QS) family ⇒[L1: open] per-index collapse ⇒[+ Link: open; Prop 5.5 PROVED] UB ⇒[+ S0: open; Thm 5.4 PROVED] FF ⇒[Thm 3.1 PROVED mod FF2 chain] contradiction.

   The edge case of L1 is PROVED (NN1 Theorem 3.2, NN2 Theorem 4.1). On the edges, Link is exactly what NN2 Observation 5.1 shows to be missing: edge planes are pairwise disjoint, so nothing links them except interior boundaries.
6. **Neutral rivals in higher rank (§6).**
   - Proposition 6.1 (PROVED) gives a branch-restricted zero-sum record: a rival needs exact zero increments only on the branch's 3b coordinates.
   - Proposition 6.2 (PROVED) extends NN2 Proposition 6.3 from global fixed-column rank-two data to any branch whose own accepted switch values on six pattern sets span at most two dimensions.
   - Proposition 6.3 (PROVED) states the general mechanism. A neutral rival exists in branch F whenever the branch's switch values near some boundary points stay, on both sides, inside the span V_F of their boundary values. So (QS) requires **transverse variation** of the switch field off every selected boundary, in every branch whose boundary span is nonzero.
   - Rank three does not suffice for pattern counting (Remark 6.4, CHECKED). Fixed rank-three columns admit six pattern vectors that are not positively dependent, in all 42 875 branches. So Proposition 6.3 of NN2 does not extend by rank alone. The answer to the brief's question is: neutral rivals in rank ≥ 3 come from the absence of transverse variation (Proposition 6.3), not from rank.

**What is not achieved.** L1 is open in the interior (sum form). Link and S0 are open for general continuous coherent families. I have no proof and no counterexample for any of the three. I do not claim that the quorum class is nearly excluded.

**Use of hypotheses.** 3q > 2n is used only inside L1 (through NN2 Theorem 2.3). Theorem 3.1, Proposition 4.1, Theorem 5.4 and Proposition 5.5 hold for every (n, q). (IB), (TC), closed sections and absence of ties are not used. Continuity in measure is used in Theorem 3.1 (via FF2 Step 2) and in Lemma 5.1 (Hausdorff continuity of K_p). The full domain is used throughout §§3–5 (vertex models, availability of all advices, FF2 Step 6).

---

## 1. Setting and the target theorem

**Notation (MM2 §1).**
- Pairs are indexed by h ∈ H = {h_1 > 0}, with advice +, 0, −, ×.
- At each world i the judges ℓ_iv (v ∈ J_i, |J_i| = n) are measurable, strictly increasing in world-i rank for a.e. h, with ∫ max_{i,v,a} |ℓ_iv(h,a)| dμ < ∞.
- Δ_iv(p, X) := L_iv(X) − L_iv(C_p).
- (QS) at p: every model X ≠ C_p (mod null) has some i ∈ supp p at which at least q judges have Δ_iv(p, X) > 0.
- A branch at p is F = (F_i)_{i∈supp p} with F_i ⊆ J_i, |F_i| = b.
- Switch maps for a problem h:
  - c_iv(h) := ℓ_iv(h,0) − ℓ_iv(h,+);
  - c′_iv(h) := ℓ_iv(h,0) − ℓ_iv(h,−);
  - d_iv(h) := c_iv(h) − c′_iv(h) = ℓ_iv(h,−) − ℓ_iv(h,+).
  - By strict guidance, c_iv(h) and d_iv(h) have the strict sign of h_i, and c′_iv(h) has the strict sign of −h_i (write-up §2.4).
- A problem h is **mixed** if it has coordinates of both signs. Coordinate planes are null and are ignored.

**Imports used repeatedly (statuses as recorded).**
- MM2 Lemma 1.1 (branch form) and MM2 Lemma 2.1 (weak Bayes in every branch; Lyapunov convexity, FF2 Step 1 refereed in GG3 §8.1). These hold for every (n, q). For every p and branch F, (QS) at p gives w_F(p) ≥ 0, nonzero, supported in F, such that for a.e. h and every advice a:

    Σ_{(i,v)∈F} w_iv [ℓ_iv(h,a) − ℓ_iv(h, a_{C_p}(h))] ≥ 0.                         (WB)

- MM2 Theorem 3.1 (alignment): w_F(p)·y_F = 0 for every common essential value y of C_p.
- MM2 Lemma 6.1 (vertices: C_{e_i} = W_i) and MM2 Theorem 6.4 Step 1 (p ↦ K_p is Hausdorff-continuous for a coherent selection continuous in measure). Both are on the full domain.
- FF2 Theorem 4.1, Steps 2–6, with their import chain (Step 6: D1; BB2 Thm 6.1 with AUDIT_BB Lemma 2.0; M3.7–M3.8; each refereed once).

**Theorem T (the target; stated precisely).** Work on the full four-advice domain. Let n ≥ 1 and 1 ≤ q ≤ n with 3q > 2n. Let the judges be as above. Then there is no map p ↦ C_p on Δ such that:
- every C_p is coherent;
- the map is continuous in measure;
- T1 = C_{p₀} for some p₀ ∈ Δ;
- (QS) holds at every p ∈ Δ.

By the lifting lemma (AUDIT_LL, refereed in MM3), Theorem T is equivalent to the statement that no ranking in the shrinking-margin quorum class (judges as above, any such n, q) covers T1 with a selection continuous in measure. Theorem T is **not** proved here. Theorem 3.1 proves it under Lemma FF.

*Scope remark.* On a decomposable domain with (LF) at T1 one would replace FF2 Step 6 by the M3.10 chain, which needs (Av). That transfer is not checked here, so every result below is stated on the full domain.

---

## 2. The exact missing lemma

**Definition 2.1.** A **fixed field** is a triple ℓ* = (ℓ*_1, ℓ*_2, ℓ*_3) of measurable penalties on H × {+,0,−,×} such that:
- each ℓ*_i(h, ·) is strictly increasing in world-i rank for a.e. h;
- ∫ max_{i,a} |ℓ*_i(h,a)| dμ < ∞.

This is FF2's hypothesis (H2). A model C is a **pointwise weak ℓ*-Bayes model at t ∈ Δ** if, for a.e. h and every advice a,

  Σ_i t_i [ℓ*_i(h,a) − ℓ*_i(h, a_C(h))] ≥ 0.

**Lemma 2.2 (blends are fixed fields; PROVED).** Let λ_iv : H → [0, Λ] be measurable with Σ_v λ_iv(h) > 0 for a.e. h and each i. Then ℓ*_i := Σ_v λ_iv ℓ_iv is a fixed field.

*Proof.*
- **Guidance.** For a.e. h, every ℓ_iv(h,·) is strictly increasing in world-i rank. A nonnegative combination with positive total weight is strictly increasing too.
- **Envelope.** |ℓ*_i| ≤ Λ Σ_v |ℓ_iv| ≤ nΛ·max_{i,v,a}|ℓ_iv|, which is integrable. ∎

**Lemma FF (open).** Let the judges and a map p ↦ C_p satisfy all hypotheses listed in Theorem T. Then there exist:
- a fixed field ℓ*;
- a map t : Δ → Δ with supp t(p) ⊆ supp p for every p,

such that, for every p ∈ Δ, C_p is a pointwise weak ℓ*-Bayes model at t(p).

*Remarks 2.3.*
1. **What is and is not asked.**
   - No regularity of t is asked.
   - ℓ* need not be one of the judges, nor a blend with constant weights. In §§4–5 it is a blend, or a blend with a modified silence penalty.
   - At a vertex the condition is automatic. C_{e_i} = W_i (MM2 Lemma 6.1) is pointwise world-i optimal, so t(e_i) := e_i works for every fixed field.
2. **Logical status.** By Theorem 3.1, the conclusion of Lemma FF is inconsistent with the hypotheses of Theorem T. So "hypotheses of T ⇒ FF" is logically equivalent to Theorem T, as any lemma whose conclusion is fed into a contradiction must be.
   - Its content is the **route**: Theorem T would follow from a fixed-field rigidity statement for the quorum family.
   - For that reason §5 splits it into sub-lemmas L1, Link and S0, none of which is known to be equivalent to Theorem T, and proves every implication between them.
3. **Why this form is exact for the downstream exclusion.** FF2 Theorem 4.1 Step 1 produces, from competitiveness and local endorsement, exactly this conclusion for the field of (H2): W(q) ∩ Δ_{supp q} ≠ ∅ for every q. Steps 2–6 use nothing else about the ranking (FF2 §4, "What is and is not used").
   - Two weaker kinds of structure are not consumed. One is weak Bayes at fields that depend on p: NN2 Observation 5.1 shows that this is what plane-wise proportionality gives. The other is weak Bayes on a subset of indices: Step 3's covering argument uses every index, including the edges.
   - MM1 Proposition 3.2 and NN2 Corollary 3.4 reach FF2 through exactly this conclusion (Proposition 4.1 below).

---

## 3. The implication

**Theorem 3.1 (PROVED modulo FF2 Theorem 4.1 Step 6's import chain: D1; BB2 Thm 6.1 with AUDIT_BB Lemma 2.0; M3.7–M3.8; each refereed once).** Work on the full domain. Let p ↦ C_p be a map of coherent models, continuous in measure on Δ, with T1 = C_{p₀}. Suppose there are a fixed field ℓ* and t : Δ → Δ with supp t(p) ⊆ supp p such that C_p is a pointwise weak ℓ*-Bayes model at t(p) for every p. Then there is a contradiction.

In particular, Lemma FF implies Theorem T, for every n and q.

*Proof.* Put W(p) := {w ∈ Δ : C_p is a pointwise weak ℓ*-Bayes model at w}. By hypothesis t(p) ∈ W(p) ∩ Δ_{supp p}. This is verbatim the conclusion of FF2 Theorem 4.1 Step 1 for the field ℓ := ℓ*. I check that each later step uses only this, continuity in measure, coherence of the C_p, T1 = C_{p₀} and (H2) for ℓ*.

1. **Step 2 (closed graph).**
   - W(p) is closed and convex. For each of countably many w_m → w in W(p), the defining inequalities hold off a null set N_m. Off ∪N_m, which is null, they pass to the limit, and they are linear in w.
   - Let p_m → p and w_m ∈ W(p_m), w_m → w. Continuity in measure gives μ(C_{p_m} △ C_p) → 0. Since the advice takes four values, a subsequence has a_{C_{p_m}}(h) = a_{C_p}(h) eventually, for a.e. h. On the co-null set where this holds and all inequalities hold, the inequality at (p_m, w_m) becomes the inequality at (p, w) in the limit. So w ∈ W(p).
   - No property of the ranking is used.
2. **Step 3 (covering).** It uses that W has closed graph with nonempty compact convex values, and that W(q) ∩ Δ_{supp q} ≠ ∅ at the boundary fixed point q (FF2 Step 3, items 4–5). Both hold. Conclusion: every w* ∈ int Δ lies in W(q) for some q.
3. **Step 4 (property (γ)).** It uses only (H2) for ℓ*: for a.e. h and a ≠ b, ℓ*(h,a) − ℓ*(h,b) is either not proportional to 𝟙 or of strict constant sign. By Fubini, for a.e. w ∈ int Δ the w-Bayes model of ℓ* is a.e. unique. By Step 3 it is C_q for some q, hence coherent.
4. **Step 5 (T1 is weak Bayes at an interior weight).**
   - Some w ∈ W(p₀) exists.
   - If w_3 = 0 with w_1, w_2 > 0: on the open set of gambles near (1, 1, −t) with t slightly above 2c₀/(c₀+ε), T1 is silent, and "accept" is strictly better at worlds 1 and 2 for ℓ* (strict guidance). That contradicts weak Bayes.
   - If w = e_1: T1 accepts a non-null set of g with g_1 < 0 (for example near the facet piece of F_1 with pattern (−,+,+)). There world 1 strictly prefers silence, which contradicts weak Bayes.
   - The other cases follow by symmetry, so w ∈ int Δ.
5. **Step 6 (the field contradiction).** ℓ* is a strictly guiding integral field with (γ), and D_{T1} is ℓ*-Bayes at an interior weight. On the full domain (LF) at D_{T1} and (Av) hold. D1, BB2 Thm 6.1 and M3.7–M3.8 then give the contradiction, exactly as in FF2 Step 6. Their standing data are properties of the field, not of a ranking.

Theorem T: under its hypotheses, Lemma FF would supply ℓ* and t, and the above gives a contradiction. ∎

*Remarks.*
- **What Theorem 3.1 does not use.** It does not use (QS), and it does not use n, q or 3q > 2n. Those enter only through the derivation of FF (§§4–5). Coherence of the selected models is used in Step 4.
- **What is not covered.** A selection that is not continuous in measure escapes Step 2, as in FF2.

---

## 4. A concrete global sufficient form

**Hypothesis (R) (global proportional blocking sets on mixed problems).** There are:
- b-sets B_i ⊆ J_i (i = 1, 2, 3);
- designated judges v_i ∈ B_i;
- constants ρ_iv > 0 (v ∈ B_i), with ρ_{iv_i} = 1;

such that, for a.e. mixed h, every i, every v ∈ B_i and all a, a′ ∈ {+, 0, −}:

  ℓ_iv(h,a) − ℓ_iv(h,a′) = ρ_iv [ℓ_{iv_i}(h,a) − ℓ_{iv_i}(h,a′)].

Equivalently, c_iv = ρ_iv c_{iv_i} and c′_iv = ρ_iv c′_{iv_i} a.e. on mixed problems; then d follows, since d = c − c′.

**Proposition 4.1 (PROVED).** Assume the hypotheses of Theorem T, except that 3q > 2n is not needed, and assume (R). Then Lemma FF holds with:
- ℓ*_i := ℓ_{iv_i}, a fixed field by Lemma 2.2;
- t(e_i) := e_i at the vertices;
- t(p) := T(p)/Σ_i T_i(p) at the other indices, where T_i(p) := Σ_{v∈B_i} w_iv(p) ρ_iv for i ∈ supp p and T_i(p) := 0 otherwise. Here w(p) is a weight given by (WB) at p for the branch (B_i)_{i∈supp p}.

Consequently (Theorem 3.1), (R) excludes every (QS) family through T1, modulo the FF2 Step 6 chain.

*Proof.*
1. **Vertices.** Remark 2.3(1).
2. **Normalisation is possible.** For |supp p| ≥ 2, w(p) ≥ 0 is nonzero and ρ > 0, so T(p) ≥ 0 is nonzero and supported in supp p.
3. **Mixed h, advice in {+,0,−}.** Let h be mixed, outside the null sets of (R) and of (WB) at p. Put a₀ := a_{C_p}(h). This is not ×, since a coherent model never accepts both g and −g (write-up §2). For a ∈ {+, 0, −}, (R) gives

     Σ_i Σ_{v∈B_i} w_iv [ℓ_iv(h,a) − ℓ_iv(h,a₀)] = Σ_i T_i(p) [ℓ*_i(h,a) − ℓ*_i(h,a₀)].

   The left side is ≥ 0 by (WB), and positive scaling preserves the sign.
4. **The advice ×.** It is strictly worst for every ℓ*_i, so Σ_i t_i [ℓ*_i(h,×) − ℓ*_i(h,a₀)] > 0.
5. **Unanimous h.** If all coordinates of h share a sign, a coherent model gives the advice that is best at every world: it accepts the orientation that is positive everywhere. So the inequality holds termwise. ∎

*Remarks.*
- **MM1 Proposition 3.2 is the special case** in which (R) holds on all problems, not just mixed ones. NN2 Corollary 3.4 reaches it as well. So the exclusions of proportional judges are instances of Theorem 3.1.
- **(R) is global.** NN2 Observation 5.1 shows that the constants cannot simply be read off the edge results, which give constants depending on the plane. Section 5 shows what the continuum of indices does give.

---

## 5. What the continuum of indices gives: sweep, exposed types, a midpoint field, propagation

Throughout this section the full domain is used, together with the hypotheses of Theorem T. 3q > 2n is not used.

**Definitions.**
- G is the set of h ∈ H, off the coordinate planes, at which every coordinate of c, c′ and d is approximately continuous, with approximate value equal to its value, and every value is nonzero. G is co-null, by a.e. approximate continuity of measurable functions and strict guidance.
- We use the representative D_{K_p} of C_p. Its advice at the pair h is + if P_{K_p}(h) > 0, − if P̄_{K_p}(h) < 0 (here P̄_K(h) = max_K m·h = −P_K(−h)), and 0 otherwise.
- For mixed h put A₊(h) := {p ∈ Δ : P_{K_p}(h) > 0} and A₋(h) := {p ∈ Δ : P̄_{K_p}(h) < 0}.
- Let ∂₊(h) and ∂₋(h) be the boundaries of A₊(h) ∩ int Δ and A₋(h) ∩ int Δ, taken **relative to int Δ**.
- A switch type τ ∈ {c, c′, d} is **exposed by C_p at h** if both of its advice sets have positive upper density at h. The advice sets are accept/silence for c, silence/reject for c′, and accept/reject for d. For h ∈ G, τ(h) is then a common essential value of C_p (MM2 §1, basic source), so MM2 Theorem 3.1 applies to it.
- C_p is **precise along h** if K_p = {m} with m·h = 0.

**Lemma 5.1 (sweep and exposed types; PROVED).** Let h ∈ G be mixed.
- (a) A₊(h) and A₋(h) are disjoint, nonempty and relatively open in Δ. Both ∂₊(h) and ∂₋(h) are nonempty.
- (b) Let p ∈ ∂₊(h). Then P_{K_p}(h) = 0, and:
  - if C_p is precise along h, C_p exposes d at h;
  - if K_p ⊆ h^⊥ and K_p is not a singleton, C_p exposes c, c′ and d at h;
  - otherwise (P̄_{K_p}(h) > 0), C_p exposes c at h.
- (c) Statement (b) holds for p ∈ ∂₋(h) with P̄_{K_p}(h) = 0, and with c′ in place of c in its last case.
- (d) Every p ∈ Δ at which C_p is precise along h exposes d at h.

*Proof.*
1. **(a).**
   - p ↦ K_p is Hausdorff-continuous (MM2 Theorem 6.4 Step 1, valid on all of Δ). Also |P_K(h) − P_{K′}(h)| ≤ d_H(K, K′)|h|, and likewise for P̄. So both are continuous in p, and A± are relatively open. They are disjoint because P ≤ P̄.
   - h has coordinates h_i > 0 and h_k < 0. By MM2 Lemma 6.1 and injectivity of K ↦ D_K, K_{e_i} = {e_i} and K_{e_k} = {e_k}. So P_{K_{e_i}}(h) = h_i > 0 and P̄_{K_{e_k}}(h) = h_k < 0.
   - By continuity, A₊ ∩ int Δ and A₋ ∩ int Δ are nonempty. They are disjoint relatively open subsets of the connected set int Δ, so neither is relatively closed, and each has nonempty relative boundary.
2. **(b): the value at h.** p ∉ A₊ (an open set does not contain its boundary points), and p is a limit of points of A₊. So P_{K_p}(h) = 0. Write K := K_p and P := P_K.
3. **The accept set has positive density at h.** P is concave and positively homogeneous, so superadditive: P(h + x) ≥ P(h) + P(x) = P(x). For x ∈ B(δ𝟙, δ/2) we have P(x) ≥ δ − δ/2 > 0, since |m·y| ≤ |y| for m ∈ Δ. So the balls B(h + δ𝟙, δ/2), 0 < δ < δ₀, lie in the accept set. Their union has positive lower density at h, because it contains a truncated open cone with vertex h.
4. **The non-accept side.** Choose m₀ ∈ K with m₀·h = 0. The half-space {g : m₀·g < 0} lies in {P < 0}, and it has density 1/2 at h. Three cases:
   - **P̄(h) > 0.** By continuity P̄ > 0 near h, so near h that half-space is silent. Accept and silence both have positive density, so c is exposed.
   - **P̄(h) = 0.** Then K ⊆ h^⊥, and for g = h + x we have P(g) = min_K m·x and P̄(g) = max_K m·x.
     - If K = {m}, the accept set {m·x > 0} and the reject set {m·x < 0} are half-spaces. So d is exposed.
     - If K contains m ≠ m′, these are linearly independent (distinct points of Δ). So some x₀ has m·x₀ > 0 > m′·x₀. Then the silence set h + {x : min_K m·x < 0 < max_K m·x} contains an open cone with vertex h. The accept set contains h + ℝ_{>0}𝟙 (an open cone around it), and the reject set contains h − ℝ_{>0}𝟙 (likewise). All three sets have positive density, so all three types are exposed.
5. **(c).** P̄_K(h) = 0 iff P_K(−h) = 0. Apply steps 2–4 to the orientation −h, with "accept −h" in place of "accept h". The switch between silence and "accept −h" is c′.
6. **(d).** This is the singleton case of step 4, which used nothing about p beyond precision along h. ∎

**Corollary 5.2 (PROVED).** Let h ∈ G be mixed. Exactly one of the following holds.
- (i) The types exposed at h by interior indices include at least two of c, c′, d.
- (ii) Every p ∈ ∂₊(h) ∪ ∂₋(h) is precise along h. In this case interior indices expose d at h.

Write E_d for the set of mixed h ∈ G in case (ii).

*Proof.*
- If some p ∈ ∂₊ is not precise along h, it exposes c (Lemma 5.1(b)). If some p′ ∈ ∂₋ is not precise along h, it exposes c′.
- If both exist, case (i) holds. If exactly one exists, the other boundary is nonempty (Lemma 5.1(a)) and consists of precise indices, which expose d. So again (i) holds.
- If neither exists, (ii) holds. ∎

**Hypothesis (UB) (uniform boundary proportionality, type-wise).** There are B_i, v_i and ρ_iv as in (R), and a co-null set G′ ⊆ G, such that the following holds for every p ∈ Δ with |supp p| ≥ 2, every mixed h ∈ G′, every type τ exposed by C_p at h, every i ∈ supp p and every v ∈ B_i:

  τ_iv(h) = ρ_iv τ_{iv_i}(h).

So proportionality is asked **only on what each selected boundary exposes**, at the worlds that are active there, with constants independent of p.

**Hypothesis (S0).** For a.e. h ∈ E_d: every p ∈ Δ at which C_p is silent at h is precise along h.

**Lemma 5.3 (midpoint silence; PROVED).** Let ℓ̂ be a fixed field and E ⊆ H measurable. Define ℓ̃ := ℓ̂, except that ℓ̃_i(h,0) := ½(ℓ̂_i(h,+) + ℓ̂_i(h,−)) for h ∈ E. Then:
- ℓ̃ is a fixed field;
- for h ∈ E, t ∈ ℝ³_{≥0} ∖ {0} and d̂(h) := (ℓ̂_i(h,−) − ℓ̂_i(h,+))_i, the advice + is weakly t-optimal for ℓ̃ at h iff t·d̂(h) ≥ 0, the advice − iff t·d̂(h) ≤ 0, and the advice 0 iff t·d̂(h) = 0.

*Proof.*
- **Guidance.** In world-i rank, silence lies strictly between + and − (whichever sign h_i has), and the midpoint lies strictly between ℓ̂_i(h,+) and ℓ̂_i(h,−). The advice × is unchanged and remains strictly worst.
- **Envelope.** |ℓ̃| ≤ max_a |ℓ̂|.
- **Differences.** For h ∈ E:
  - ℓ̃(0) − ℓ̃(+) = d̂/2 and ℓ̃(−) − ℓ̃(+) = d̂;
  - ℓ̃(+) − ℓ̃(0) = −d̂/2 and ℓ̃(−) − ℓ̃(0) = d̂/2;
  - ℓ̃(+) − ℓ̃(−) = −d̂ and ℓ̃(0) − ℓ̃(−) = −d̂/2.

  Pairing each with t gives the three criteria. The advice × is strictly worse than every advice for t ≥ 0, t ≠ 0. ∎

**Theorem 5.4 (PROVED).** Assume the hypotheses of Theorem T (3q > 2n is not needed), (UB) and (S0). Then Lemma FF holds. Explicitly:
- **The field.** Let ℓ̂_i := ℓ_{iv_i}, and let E be the measurable set of mixed h at which c_iv(h) ≠ ρ_iv c_{iv_i}(h) or c′_iv(h) ≠ ρ_iv c′_{iv_i}(h) for some i and some v ∈ B_i. Let ℓ* := ℓ̃ be the midpoint modification of ℓ̂ on E (Lemma 5.3).
- **The weights.** t(e_i) := e_i at the vertices, and t(p) := T(p)/ΣT(p) at the other indices, with T as in Proposition 4.1.

Consequently, (UB) and (S0) together exclude every (QS) family through T1 (Theorem 3.1), modulo the FF2 Step 6 chain.

*Proof.*
1. **Where proportionality holds.** Let h ∈ G′ be mixed. Interior indices have all three worlds active, so (UB) applies there at every world.
   - If h ∉ E_d, then by Corollary 5.2(i) two of c, c′, d are ρ-proportional at h at every world. Since d = c − c′, with the same constants, the third is ρ-proportional too. So h ∉ E.
   - If h ∈ E_d, then by Corollary 5.2(ii), d is exposed at some interior index, so d is ρ-proportional at h.
   - Hence, up to a null set: d_iv = ρ_iv d̂_i on all mixed problems, where d̂ is formed from ℓ̂; and E ⊆ E_d.
2. **Mixed h ∉ E.** All differences among {+, 0, −} are ρ-proportional at h, and ℓ* = ℓ̂ there. Steps 3–4 of the proof of Proposition 4.1 apply verbatim.
3. **Mixed h ∈ E: the setup.** Then h ∈ E_d and d is ρ-proportional. Fix p with |supp p| ≥ 2, and let w := w(p) be the branch weight. For a.e. such h:
   - **C_p accepts h.** (WB) with alternative "−" gives Σ_{F} w_iv d_iv(h) = T(p)·d̂(h) ≥ 0.
   - **C_p rejects h.** (WB) with alternative "+" gives −T(p)·d̂(h) ≥ 0.
   - **C_p is silent at h.** By (S0), C_p is precise along h. By Lemma 5.1(d), it exposes d at h. By MM2 Theorem 3.1, w·d_F(h) = 0, so T(p)·d̂(h) = 0.
4. **Mixed h ∈ E: the conclusion.** By Lemma 5.3, in each case the advice of C_p is weakly T(p)-optimal for ℓ*, hence weakly t(p)-optimal. At vertices, C_{e_i} = W_i is never silent at a mixed h and is pointwise world-i optimal.
5. **Unanimous h.** ℓ* = ℓ̂ there, since E consists of mixed problems, and the argument of Proposition 4.1 step 5 applies.
6. **Null sets.** For each fixed p, the exceptional sets are: the complement of G′; the null set in (S0); the null set of (WB) at p; and the set where C_p differs from D_{K_p}. Their union is null. So the weak Bayes inequality holds for a.e. h, for each p.
7. **The field is fixed.** ℓ̂ is a fixed field by Lemma 2.2, and so is ℓ* by Lemma 5.3. ∎

*Why the midpoint is needed.* On E_d the boundaries expose only the accept/reject switch. So nothing in the boundary data constrains the silence penalties of the blocking set. Lemma 5.3 replaces them by a silence penalty that is exactly half-way, for which the d-information alone decides optimality at every index. Without it, (UB) would have to demand proportionality of switch types that no boundary exposes.

**Hypothesis L1(B) (per-index collapse with a fixed blocking set).** For every p ∈ Δ with |supp p| ≥ 2 there are constants ρ_iv(p) > 0 (i ∈ supp p, v ∈ B_i, ρ_{iv_i}(p) = 1) such that, for every mixed h ∈ G and every type τ exposed by C_p at h, τ_iv(h) = ρ_iv(p) τ_{iv_i}(h).

Status of L1(B):
- At edge indices, the collapse is PROVED, with p-dependent coincident sets Z_i(p) of size ≥ 2q − n ≥ b. This is NN1 Theorem 3.2, on N(C_p), which contains every exposed value at points of G. Requiring B_i ⊆ Z_i(p) for all p is part of L1(B).
- At interior indices, L1(B) is the conclusion of NN2 Theorem 2.3 whenever the boundary data of C_p have common-parameter form. So it is NN2 Conjecture 6.4 with a fixed blocking set. It is **open**.

**Hypothesis Link.** Write p ≍ p′ if some mixed h ∈ G and some type τ are exposed at h by both C_p and C_{p′}. Then for every p ∈ Δ with |supp p| ≥ 2 and every interior p′, there is a chain p = p₀ ≍ p₁ ≍ … ≍ p_m = p′ with p₁, …, p_m interior.

**Proposition 5.5 (PROVED).** L1(B) and Link imply (UB), with G′ := G and ρ_iv := ρ_iv(p*) for any interior p*.

*Proof.*
1. **One link.** If p ≍ p′ through (h, τ) and i ∈ supp p ∩ supp p′, then ρ_iv(p) = τ_iv(h)/τ_{iv_i}(h) = ρ_iv(p′). The denominator is nonzero since h ∈ G.
2. **Along a chain.** Interior indices have every world active. So along a chain from p to p* with interior intermediate indices, every consecutive pair shares world i whenever i ∈ supp p. Hence ρ_iv(p) = ρ_iv(p*).
3. **Conclusion.** L1(B) with these constants is (UB). ∎

*Remarks 5.6.*
1. **The constants are properties of the judges.** Proposition 5.5 is the open-and-closed propagation principle asked for in AUDIT_NN point 4, in the only form I can prove. At a shared point h, the ratio τ_iv(h)/τ_{iv_i}(h) is a value of the judges, so it cannot depend on which selected model exposes h. Agreement then propagates along linked boundaries.
2. **Edges and Observation 5.1.**
   - For different s, the edge planes Π_s are pairwise disjoint, and on each open edge C_{p_s} exposes points of Π_s only (MM2 Theorem 6.4(b)).
   - So no two edge indices are ≍-linked through the regions Q_ij directly. The plane-dependent constants γ_v(s) of NN2 Theorem 4.1 (Observation 5.1) are exactly the failure of Link among edge indices.
   - Proposition 5.5 says what would repair it. Suppose an interior selected boundary that satisfies L1 meets Π_s and Π_{s′} at G-points, where the same type is exposed as by the edge models. Then γ(s) = γ(s′).
3. **The measure-theoretic content of Link.**
   - Two selected boundaries typically meet along finitely many rays, a null set, which may miss G. So Link is delicate for merely measurable judges.
   - If the switch maps are continuous on the open mixed orthants (AUDIT_MM's smooth flat judges are of this kind), then G contains every mixed point off the coordinate planes. Link then becomes a geometric property of the family {∂D_{K_p}} alone.
   - I do not know whether every family as in Theorem T has this property. A topological argument from the sweep alone does not suffice. A separator of e₃ from [e₁, e₂] and a separator of e₁ from [e₂, e₃] can be disjoint in Δ, so sets ∂₊(h), ∂₊(h′) of different patterns need not meet. Link is **open**.
4. **The chain, with statuses.**

     (QS) family through T1
       ⇒ [L1(B): open in the interior; PROVED on edges, but with p-dependent Z(p)]
     per-index collapse
       ⇒ [+ Link: open; Prop 5.5 PROVED]
     (UB)
       ⇒ [+ S0: open; Thm 5.4 PROVED]
     Lemma FF
       ⇒ [Thm 3.1 PROVED mod FF2 Step 6 chain]
     contradiction.

   Also (R) ⇒ FF (Proposition 4.1, PROVED), and (R) ⇒ (UB) and (S0) trivially, since (R) gives every type proportional on mixed problems.

**Observation 5.7 (alignment along the whole family does not force L1; PROVED from NN2 Proposition 6.1, CHECKED there).**
- **The data.** Take NN2 Proposition 6.1's columns (seven per world, rank two), with a measurable β : (mixed gambles) → ℝ² in the pattern cones A_{s(g)}. Put σ_iv(g) := ⟨a_iv, β(g)⟩ on all mixed gambles.
- **Alignment holds everywhere in the interior.** Every interior selected model, of any coherent family whatever, satisfies MM2's alignment condition in all 42 875 branches. The reason is that one fixed w_F annihilates every value of σ_F.
- **No collapse.** No two judges of a world are proportional.
- **Consequence.** The alignment conditions at all interior indices together, however the boundaries sweep, do not imply L1. Any proof of L1 must use the exact nonstrict test, not alignment along the family.
- **Where these data fail.** They fail the exact test at T1 and at nearby models (NN2 Proposition 6.3). Proposition 6.3 below also applies to them whenever, in some branch F, the boundary values span the image {(⟨a_iv, β⟩)_{(i,v)∈F} : β ∈ ℝ²}, because all values lie in that image. So they are not a counterexample to Theorem T.

---

## 6. Neutral rivals beyond rank two

Fix p, write C := C_p, and let F be a branch at p. For a problem h and an advice b, put s^b_F(h) := (ℓ_iv(h,b) − ℓ_iv(h,a_C(h)))_{(i,v)∈F}.

**Proposition 6.1 (branch-restricted rivals; PROVED).**
- **Hypotheses.** Let E_1, …, E_m be pairwise disjoint non-null sets of problems. On each E_k let b_k(h) ≠ a_C(h) be a measurable choice of advice, with s_k := s^{b_k}_F bounded on E_k. Put x_k := ∫_{E_k} s_k dμ. Suppose some θ ≥ 0, θ ≠ 0, has Σ_k θ_k x_k ≤ 0 componentwise.
- **Conclusion.** (NT_F) fails, so (QS) fails at p.

*Proof.*
1. **A convex range.** On E := ∪E_k put s := s_k on E_k. The vector measure A ↦ (∫_A s dμ, μ(A)) on subsets of E is finite-dimensional and atomless, so its range is convex (Lyapunov). It contains (0, 0) and every (x_k, μ(E_k)).
2. **A good subset.** With τ := θ/Σθ, it therefore contains (Σ_k τ_k x_k, Σ_k τ_k μ(E_k)). So there is A ⊆ E with ∫_A s ≤ 0 and μ(A) > 0.
3. **The rival.** Let X be C with advice b_k on A ∩ E_k. It is evaluable on the full domain, X ≠ C, and Δ_F(X) = ∫_A s ≤ 0. By MM2 Lemma 1.1, (QS) fails. ∎

Compared with NN2 Lemma 6.2:
- only the 3b branch coordinates must vanish, or merely be ≤ 0, instead of all 3n judges;
- any alternative advice may be used, not only silence.

**Proposition 6.2 (branch rank two; PROVED).**
- **Hypotheses.** For an oriented gamble g write σ(g) for the accept-to-silence switch (MM1 §1.1). Suppose that for each of the six mixed patterns s, C accepts a non-null set E_s of oriented gambles of pattern s. Suppose also that σ_F(g) ∈ V a.e. on ∪_s E_s, for a linear subspace V ⊆ ℝ^F with dim V ≤ 2.
- **Conclusion.** (QS) fails at p.

*Proof.*
1. **One vector per pattern.** Shrink each E_s so that σ_F is bounded on it, and put x_s := ∫_{E_s} σ_F. Then x_s ∈ V, since V is a closed subspace. Also x_s ∈ O_s := {z ∈ ℝ^F : sgn z_iv = s_i for all (i,v) ∈ F}, since each strict sign integrates to a strict sign.
2. **The pattern cones in V.** The sets O_s ∩ V are nonempty, open and convex in V, pairwise disjoint, and O_{−s} = −O_s. None contains 0.
3. **dim V = 2.** A line through 0 is two open rays plus 0. A ray lies in at most one O_s, since the O_s are disjoint cones. So at most two O_s ∩ V can be nonempty if dim V ≤ 1, but there are six.
4. **No closed half-plane contains the six vectors.** Suppose f ∈ V* ∖ {0} had f(x_s) ≥ 0 for every s.
   - O_s ∩ V contains x_s, with f ≥ 0, and −x_{−s}, with f ≤ 0.
   - Being connected, it meets ker f. By the ray count of step 3, at most two of the six sets do. Contradiction.
5. **Conclusion.** So 0 is in the interior of conv{x_s} in V, and Σ_s θ_s x_s = 0 for some θ > 0. Proposition 6.1, with silence on the E_s, applies. ∎

This extends NN2 Proposition 6.3. There, all 3n judges had to be fixed-column rank two on an open set. Here it is enough that one branch's 3b judges have rank at most two on the accepted gambles used, which may lie anywhere.

**Proposition 6.3 (transverse variation is necessary; PROVED).**
- **Hypotheses.**
  - Let h_1, …, h_k ∈ G be basic sources of common essential values y¹, …, y^k of C, of types τ_1, …, τ_k (MM2 §1).
  - Put V_F := span{y¹_F, …, y^k_F} ≠ {0}.
  - Suppose each h_j has a neighbourhood U_j such that τ_{j,F}(h) ∈ V_F for a.e. h ∈ U_j, on both advice sets of the type τ_j.
- **Conclusion.** (QS) fails at p.

*Proof.*
1. **A margin.** Y := {±y^j_F} is symmetric and spans V_F, so 0 is interior to conv Y in V_F. Choose δ > 0 with max_{y∈Y} f(y) ≥ δ for every f ∈ V_F* of dual norm 1, and fix 0 < r < δ.
2. **The sets.** For each j, choose non-null sets A_j and B_j inside U_j, on the two advice sets of τ_j (call the advices a_j and b_j), with |τ_j − y^j| < r on them. Choose all 2k sets pairwise disjoint, one after another, using atomlessness, as in MM2 Proposition 4.1 step 2.
   - On A_j, the switch a_j → b_j has F-values τ_{j,F}.
   - On B_j, the switch b_j → a_j has F-values −τ_{j,F}.
   - Both lie in V_F a.e.
3. **Averages.** u_j := μ(A_j)^{−1}∫_{A_j} τ_{j,F} and u′_j := −μ(B_j)^{−1}∫_{B_j} τ_{j,F} lie in V_F, within r of y^j_F and of −y^j_F respectively.
4. **0 lies in their hull.** Suppose not. Strict separation in V_F gives a unit f with f < 0 on all u_j, u′_j. But max_Y f ≥ δ, and each u differs from its y by less than r < δ, so some u has f(u) > 0. Contradiction.
5. **Conclusion.** So a nontrivial nonnegative combination of the exact integrals ∫_{A_j}, ∫_{B_j} is 0, and Proposition 6.1 applies. ∎

*Reading.*
- **Alignment (MM2 Thm 3.1) needs w_F ⊥ V_F.** A switch field that, near boundary points, varies only inside the span of its own boundary values gives a neutral rival. So (QS) requires, in every branch, that the near-boundary switch values leave V_F on non-null sets, with the transverse components signed so as to defeat every such combination. This is MM2's (R5) second-order condition in its exact form.
- **The vanishing certificates are covered.** If a whole branch mixture vanishes identically near the boundary (AUDIT_MM point 2), then the branch values lie in w_F^⊥ there. Proposition 6.3 applies as soon as they do not leave the span of the boundary values.

**Remark 6.4 (rank three does not suffice for pattern counting; CHECKED, `rank3_pointed.out`).**
- **The columns.** Take n = 7 and, with k = −3, …, 3,

    a_iv := e_i + (k/50 + k²/400) e_{i+1} − (k/50) e_{i+2} ∈ ℚ³.

  No two columns of one world are proportional.
- **The pattern vectors.** For each mixed pattern s, let x_s ∈ ℚ³ have entries 10 where s_i = + and −1 where s_i = −. Then:
  - sgn⟨a_iv, x_s⟩ = s_i for all 21 judges and all six patterns;
  - ⟨(1,1,1), x_s⟩ ∈ {8, 19}, which is > 0 for every s. So the six vectors are **not** positively dependent;
  - in each of the 42 875 branches, the F-restricted vectors have rank 3.
- **Meaning.** With fixed rank-three columns, accepted values confined near these x_s escape the mechanism of NN2 Proposition 6.3 and of Proposition 6.2. Rank alone does not produce neutral rivals.
- **What it is not.** This is not a (QS) model. Nothing about boundaries, the second-order test or a family is checked. Proposition 6.3 still applies whenever the near-boundary values stay in the span of the boundary values.
- **Answer to the brief's question.** In rank ≥ 3, the mechanism of the exact nonstrict test is positive dependence (or a nonpositive combination) among exactly attainable branch integrals (Proposition 6.1). Propositions 6.2–6.3 give sufficient conditions for it. Rank or sign patterns alone do not produce it.

---

## 7. Status

| Item | Statement | Label |
|---|---|---|
| T | no (QS) family through T1, full domain, 3q > 2n | **open** (criterion (i) not met) |
| FF | the fixed factorised field exists for every (QS) family through T1 | **open** (the exact missing lemma; logically equivalent to T, Remark 2.3(2)) |
| 2.2 | blends of judges are fixed fields | PROVED |
| 3.1 | FF ⇒ T (any n, q; no use of (QS) beyond FF) | PROVED modulo FF2 Step 6 chain (D1; BB2 Thm 6.1 + AUDIT_BB 2.0; M3.7–M3.8; each refereed once) |
| 4.1 | (R) on mixed problems ⇒ FF | PROVED |
| 5.1 | sweep: every mixed h ∈ G lies on interior boundaries on both sides; exposed type c / c′, or d exactly at indices precise along h | PROVED |
| 5.2 | at each mixed h ∈ G: ≥ 2 types exposed, or every interior boundary index is precise along h (E_d) | PROVED |
| 5.3 | midpoint silence keeps a fixed field and reduces optimality to the sign of t·d̂ | PROVED |
| 5.4 | (UB) + (S0) ⇒ FF | PROVED |
| 5.5 | L1(B) + Link ⇒ (UB) | PROVED |
| 5.7 | alignment at all interior indices does not imply L1 | PROVED (from NN2 6.1, CHECKED there) |
| L1(B) | per-index collapse with a fixed blocking set | edges: collapse PROVED (NN1 3.2) with p-dependent sets; interior **open** (NN2 Conj 6.4) |
| Link | chain-linking of selected boundaries through G-points | **open** |
| S0 | silence at E_d problems only at indices precise along h | **open** |
| 6.1 | branch-restricted rivals (≤ 0 on 3b coordinates suffices) | PROVED |
| 6.2 | one branch of rank ≤ 2 on six accepted pattern sets ⇒ (QS) fails | PROVED |
| 6.3 | no transverse variation near boundary points ⇒ (QS) fails | PROVED |
| 6.4 | rank-three columns with non-positively-dependent pattern vectors, all 42 875 branches of rank 3 | CHECKED |

**Hypotheses used.**
- 3q > 2n: only inside L1, through NN2 Theorem 2.3.
- Continuity in measure: Theorem 3.1 (FF2 Step 2) and Lemma 5.1 (Hausdorff continuity of K_p).
- Full domain: throughout.
- Coherence of the selected models: Theorem 3.1 Step 4, Lemma 5.1 and Proposition 4.1.
- (IB), (TC), closed sections, absence of ties: none.

**Where a proof of Theorem T must now act.**
- **L1 in the interior.** The sum form must be converted to common-parameter form at each interior index. By Observation 5.7, this must use the exact test, and by Proposition 6.3 the relevant information is the transverse variation of the switch field off ∂C_p.
- **Link.** Gluing along a continuous family of convex cones.
- **S0.** A side condition on problems all of whose selected boundaries are precise.

Everything downstream of these three statements is proved here, modulo the FF2 import chain.

**Files.** `oo1py/rank3_pointed.py` → `oo1py/rank3_pointed.out` (Remark 6.4; exact `fractions.Fraction`; ends with ALL CHECKS PASSED).
