# NN2 (round 42, BRIEF34). Five-of-seven committees: the blocking-cone collapse extends to every blocking size; where it reaches, and where it does not

18 Oct 2026. Rules of BRIEF13 and BRIEF34; the scope corrections of AUDIT_MM are adopted. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named, with their recorded status.
- **CHECKED**: exact rational computation with a stated script in `nn2py/`.
- **NUMERICS**: none used.
- **CONJECTURE**: marked where offered.

Scripts (run `python3 -I <script>.py` from inside `nn2py/`; each output ends with `ALL CHECKS PASSED`):
- `collapse_check.py` → `collapse_check.out` (Theorem 2.3 and Lemma 2.1; exhaustive one-dimensional parts, random exact instances in ℝ⁴ and ℝ⁵ with exact failure certificates);
- `sumform_escape.py` → `sumform_escape.out` (the rank-two sum-form configuration of §6).

Nothing in a proof rests on a script.

Setting: the write-up §2; three worlds; μ standard Gaussian; T1 = D_K, K = (1−ε)u + εΔ, c₀ = (1−ε)/3, v_k = c₀𝟙 + εe_k. At each world i there are n strictly guiding integrable additive judges ℓ_iv (v ∈ J_i, |J_i| = n) and the quorum is q. Write **b := n − q + 1** for the blocking size. For BRIEF34, n = 7, q = 5, b = 3, and a full-support branch is a choice of a 3-set F_i ⊆ J_i at each world: C(7,3)³ = 42 875 branches. (QS), branches and (NT_F) are as in AUDIT_LL and MM2 §1. No assumption is added; every extra hypothesis is a hypothesis of the result that states it.

The one arithmetic fact used throughout:

  3q > 2n  ⟺  n − 2b + 2 ≥ b,                                                    (0.1)

since n − 2b + 2 − b = 3q − 2n − 1. For (n,q) = (7,5): n − 2b + 2 = 3 = b.

---

## 0. Outcome

**Answer to the adversarial question.** MM1's two-generator collapse **does extend** to blocking cones with any number b of generators, in every dimension, for every (n,q) with 3q > 2n and with at least two active worlds (Theorem 2.3, PROVED; CHECKED on exact instances). The audit's reason for hoping otherwise was that MM1's *proof* (a non-ray intersection forces a common plane) fails for three generators. That is true, but the *statement* survives by a different proof: project to a generic line, apply the one-dimensional two-family Helly property, and use a depth count in which the inequality 3q > 2n appears exactly. So **there is no escaping three-generator cone configuration** in any geometry where MM1's collapse was formulated, that is, wherever the branch representations of a selected model share a common linear parameter. Deliverable (b) as posed is therefore impossible, and the obstruction (a) holds in those classes.

What is PROVED:

1. **Collapse (Theorem 2.3).** Take finitely many vectors, n per world, in a common open half-space of a finite-dimensional space. Suppose that every choice of one b-generator cone per active world has a nonzero common point. Then there is a single ray z such that, at every world, at least n − 2b + 2 (≥ b) of the vectors lie on z, every b-cone of every world contains z, and z is the only ray carrying b vectors at any world. For b = 2 this recovers MM1 Lemma 3.1 (c), and it is new for b ≥ 3, answering MM1 Remark 3.3.
2. **Five-of-seven versions of MM1's exclusions (§3).** These hold for every (n,q) with 3q > 2n:
   - cellwise-linear judges on any finite fan collapse to one field on the pinned cells (Corollary 3.1, extending MM1 Thm 4.1);
   - **min-cell judges: (QS) fails for every coherent selection that is continuous in measure and passes through T1** (Corollary 3.2, extending MM1 Thm 4.2, self-contained);
   - near T1, general fans give plain posteriors on the T1-pinned cells (Corollary 3.3, extending MM1 Cor 4.3);
   - rank-two worlds with dim R(C) ≤ 1 fail (Corollary 3.4, extending MM1 Prop 5.1(b));
   - proportional blocking sets at every world fail (MM1 Prop 3.2, restated with a scope remark on the advice ×).
   - T1 **alone** still passes (QS) in the min-cell class for 5-of-7, with all 42 875 branches strictly certified and no two of the four off-ray judges proportional (Remark 3.5). So the isolation, not the single model, is what fails.
3. **MM2 re-derived for branch size 3 (§4).** The branch reformulation, weak Bayes, alignment, the sign lemma, the generic-judge failure, the world-separable failure and the edge identities hold verbatim. The annihilator bound stays dim W_p ≥ 3, and at T1 at least 13 extreme supports are needed (by counting). **New (Theorem 4.1):** applying Theorem 2.3 to MM2's edge identities shows that on almost every edge plane Π_s, at least n − 2b + 2 judges at each of the two edge worlds have switch magnitudes proportional, along the whole plane, to one common function. Consequently (Corollary 4.2), (QS) fails on the full domain whenever, near some edge, every triple of same-world judges contains a pair whose switch ratio varies with the off-edge payoff. This is a within-world condition. It holds for generic smooth judges and does not involve the target. The n = 4, q = 3 version, with pairs, is also new.
4. **The bridges asked for (§5).**
   - *Weak versus strict.* Every result in §§2–4 uses only weak certificates, through Lemma 1.2 of MM1 and MM2's alignment. In the classes of §3, guidance forbids a weak certificate from vanishing on a pinned piece, so no strictness is needed. The vanishing-certificate loophole of AUDIT_MM point 2 lives only in the sum form of §6.
   - *Local versus global.* §3 needs proportionality only on pinned cells; Corollary 3.2 never uses global proportionality. Theorem 4.1 gives plane-wise proportionality with constants depending on the plane, which does **not** feed Proposition 3.2 (an explicit gap, stated).
   - *Shapes.* No result assumes moving corners. Corollary 3.2 *derives* polygonal shapes with corners on the walls from cellwise linearity. On the edges the shapes are forced (MM2 Lemma 6.2). In the interior, with general judges, shapes are free, and nothing here constrains rounded corners.
5. **Where the collapse does not reach (§6).** With three active worlds and general judges, the boundary relation is a **sum**: u₁ + u₂ + u₃ = 0 on ∂C, with u_i in the branch cone of world i. It is not a common point of cones.
   - The combinatorial collapse genuinely fails in sum form. An exact rank-two configuration satisfies all 42 875 branch positive-dependence conditions and realises all six mixed sign patterns, with no two judges proportional at any world (Proposition 6.1, CHECKED). This is the explicit escaping configuration.
   - But it does **not** survive the exact nonstrict test. Any fixed-column rank-two boundary data, near any model whose accepted region carries all six mixed patterns (T1 and every model near it), admit a non-null *zero-sum record*: a change on which every judge's increment is exactly 0. So (QS) fails (Proposition 6.3, PROVED). The gap between the combinatorial and the exact test is the weak/strict gap made concrete.

**Use of (IB), (TC), closed sections: none is used anywhere.** Only the numerical inequality 3q > 2n enters (Theorem 2.3's propagation step; (0.1)). This is the inequality behind (TC)'s counting proof, but (TC) itself is not used. Continuity in measure of the selection is used in Corollary 3.2 (clopen step) and in §4 (edge sweep). Absence of ties is not used.

**Single most important open point.** Interior, three active worlds, general judges: along a continuous family through T1, does the exact nonstrict test force the boundary data into common-parameter (intersection) form, so that Theorem 2.3 applies? Or is there sum-form data of rank ≥ 3 that passes the exact test along a moving family with no proportional blocking sets? §6.4 states the target precisely. It is the only place left where the extra freedom of 5-of-7 could act.

---

## 1. Setting and the abstract blocking-cone problem

**Branches.** At p, a branch is F = ⊔_{i∈supp p} F_i with F_i ⊆ J_i and |F_i| = b. MM2 Lemma 1.1 (PROVED there for any n, q) gives: (QS) at p ⟺ (NT_F) for every branch F. MM2 Lemma 2.1 (any branch size) gives: (QS) at p ⇒ for every branch, C_p is a pointwise **weak** Bayes model of a nonnegative nonzero mixture of F's judges. Neither uses 3q > 2n.

**The abstract problem.** Let V be a finite-dimensional real vector space and φ ∈ V* a linear functional. Let S be a finite set of worlds with |S| ≥ 2, and for each i ∈ S let a_i1, …, a_in ∈ V with φ(a_iv) > 0. For T ⊆ {1, …, n} with |T| = b put

  σ_i^T := cone{a_iv : v ∈ T}.

The **colourful hypothesis** is:

  (H_b)  for every choice (T_i)_{i∈S} of b-sets, ⋂_{i∈S} σ_i^{T_i} ≠ {0}.

MM1 Lemma 3.1 is the case b = 2, n = 4, |S| = 3. Its hypothesis allows a separate half-space per world, but its proof (Step 1, "the open half-plane L ∩ H") uses a common one. In every application below a common φ is available. Corollaries 3.1–3.3 use positive vectors with φ = sum of coordinates. Theorem 4.1 uses point evaluation of positive functions. Corollary 3.4 uses a pointed cone in a plane.

---

## 2. The collapse theorem

**Lemma 2.1 (depth count; PROVED; CHECKED `collapse_check.out` Part 3).** Let a_1, …, a_n ∈ V with φ(a_v) > 0, let 1 ≤ b ≤ n, and let z ≠ 0 lie in cone{a_v : v ∈ T} for every b-set T. Then at most 2b − 2 of the a_v fail to be positive multiples of z. Hence at least n − 2b + 2 are positive multiples of z.

*Proof.*
1. **z lies in φ's half-space.** z is a nonzero nonnegative combination of vectors with φ > 0, so φ(z) > 0. A vector a_v that is not a positive multiple of z is not in ℝz: a nonpositive multiple would have φ ≤ 0.
2. **A generic functional vanishing on z.** Let Z := {ψ ∈ V* : ψ(z) = 0}. For each a_v ∉ ℝz, the set {ψ ∈ Z : ψ(a_v) = 0} is a proper subspace of Z, since some functional vanishes on z but not on a_v. A finite union of proper subspaces does not cover Z. So there is ψ ∈ Z with ψ(a_v) ≠ 0 for every a_v not on the ray of z.
3. **No b same-sign vectors.** Suppose b such vectors had ψ(a_v) > 0, forming a b-set T. Write z = Σ_{v∈T} λ_v a_v with λ ≥ 0. Then 0 = ψ(z) = Σ λ_v ψ(a_v), so λ = 0 and z = 0, a contradiction. The same holds for ψ < 0.
4. **Count.** So at most b − 1 off-ray vectors are positive and at most b − 1 are negative. ∎

**Lemma 2.2 (two families of intervals; PROVED).** Let 𝓘 and 𝓙 be finite nonempty families of compact intervals in ℝ with I ∩ J ≠ ∅ for all I ∈ 𝓘 and J ∈ 𝓙. Then all members of 𝓘, or all members of 𝓙, share a point.

*Proof.* Let λ be the largest left endpoint in 𝓘 ∪ 𝓙, attained by K, and ρ the smallest right endpoint, attained by K′.
- If λ ≤ ρ, every interval contains [λ, ρ].
- If λ > ρ, then K ∩ K′ = ∅, so K and K′ belong to the same family, say 𝓘. Every J ∈ 𝓙 meets K, so its right end is ≥ λ. It also meets K′, so its left end is ≤ ρ. Hence every J ∈ 𝓙 contains [ρ, λ]. ∎

**Theorem 2.3 (blocking-cone collapse; PROVED; CHECKED `collapse_check.out` Parts 1–2).** In the abstract setting of §1, assume n ≥ 3b − 2 (for b = n − q + 1 this is 3q > 2n, by (0.1)) and (H_b). Then there is z ∈ V ∖ {0} such that:
- (a) at every world i ∈ S, at least n − 2b + 2 (≥ b) of the a_iv are positive multiples of z;
- (b) z ∈ σ_i^T for every i ∈ S and every b-set T;
- (c) at every world, the ray of z is the only ray containing b or more of the a_iv.

Conversely, (b) implies (H_b).

*Proof.*
1. **A generic line.** Put â := a/φ(a), so φ(â) = 1, and â_iv = â_iw iff a_iv, a_iw are positively proportional. The set of f ∈ V* with f(â_iv) = f(â_iw) for some world i and some non-proportional pair (v,w) is a finite union of proper subspaces. Choose f outside it. Then, within one world, equal f-values occur only for positively proportional vectors.
2. **Intervals.** For x ∈ σ_i^T ∖ {0}, x̂ := x/φ(x) is a convex combination of the â_iv (v ∈ T). So f(x̂) lies in the compact interval I_i^T := [min_{v∈T} f(â_iv), max_{v∈T} f(â_iv)].
3. **One world has a common point.** Fix two distinct worlds i, j ∈ S. For any b-sets T_i, T_j, choose b-sets at the other worlds arbitrarily. (H_b) gives x ≠ 0 in all the chosen cones, so f(x̂) ∈ I_i^{T_i} ∩ I_j^{T_j}. By Lemma 2.2 one of the two families, say world i's, has a common point t.
4. **The middle values coincide.** Let y₁ ≤ … ≤ y_n be the values f(â_iv). The b smallest give the interval [y₁, y_b] and the b largest give [y_{n−b+1}, y_n], so y_{n−b+1} ≤ t ≤ y_b. Since n − b + 1 ≥ b (from n ≥ 3b − 2 ≥ 2b − 1), this forces y_b = y_{b+1} = … = y_{n−b+1}. These are n − 2b + 2 equal values. By step 1, the corresponding a_iv are positive multiples of one vector z.
5. **Propagation to the other worlds.** By (0.1), n − 2b + 2 ≥ b. Choose a b-set T* of these vectors, so σ_i^{T*} = ℝ₊z. Let k ≠ i and let T be any b-set. Take T* at i, T at k, and arbitrary b-sets elsewhere. (H_b) gives a nonzero point of ℝ₊z ∩ σ_k^T, so z ∈ σ_k^T. This proves (b) at every k ≠ i.
6. **Back to world i.** Lemma 2.1 at a world k ≠ i gives at least n − 2b + 2 ≥ b of its vectors on ℝ₊z. Running step 5 with the roles of i and k exchanged gives z ∈ σ_i^T for every T. This proves (b) at every world, and Lemma 2.1 then gives (a).
7. **(c).** Suppose b vectors at world i lay on a ray z′ ≠ z. As in Lemma 2.1, choose ψ ∈ V* with ψ(z) = 0, ψ(z′) ≠ 0, and ψ nonzero on every vector off the ray of z. Then those b vectors have one ψ-sign, so their cone misses z. This contradicts (b).
8. **Converse.** Under (b), z is a common nonzero point of every colourful choice. ∎

*Remarks.*
- **The role of 3q > 2n.** Steps 1–4 need only n ≥ 2b − 1, which is 2q > n (since 2b − 1 ≤ n ⟺ n + 1 ≤ 2q). They give n − 2b + 2 proportional vectors at **one** world. The propagation in steps 5–6 needs those to form a blocking set, which is exactly 3q > 2n. So the user's (TC) inequality is precisely what turns a one-world degeneracy into a global collapse.
- **No dimension or world-number restriction.** The proof works in every dim V and with |S| ≥ 2. In particular it covers edges (|S| = 2), which MM1 Lemma 3.1 did not.
- **Sharpness.** (H_b) holds for the configurations {z, z, z, z ± u, z ± w} at every world (positive multiples allowed), for any u, w with all vectors in φ's half-space (`collapse_check.out` Part 2d). After a one-vector perturbation it fails, with an exact certificate (Part 2e). The certificates in Parts 2a–2c and 2e are exactly the objects of steps 1–4: a rational f and two b-sets at two worlds whose f-intervals are disjoint, which proves that the corresponding cones meet only at 0.
- **For b = 2, n = 4.** Theorem 2.3 gives MM1 Lemma 3.1 (c). It also gives (a) and (b): at every world two vectors lie on z, and the other two have opposite ψ-signs for every generic ψ ∈ z^⊥. So their classes modulo z are negatively proportional, which means coplanarity with z in the middle. MM1's proof was specific to two generators; this one is not.

---

## 3. Consequences: MM1's exclusions hold for every (n,q) with 3q > 2n

In MM1's settings below, "all branches" means all C(n,b)^{|supp p|} branches. MM1's Lemmas 1.1–1.4 hold verbatim for any (n,q):
- Lemma 1.2 is MM2 Lemma 2.1 for any branch size;
- Lemma 1.3 uses only that every world-i judge strictly prefers W_i;
- Lemma 1.4 uses Lemma 1.2 on an edge branch.

**Corollary 3.1 (MM1 Theorem 4.1 for 3q > 2n; PROVED).**
- **Setting and hypotheses.** Those of MM1 Theorem 4.1: cellwise-linear judges σ_iv(g) = κ_iv(Q)g_i on Q ∩ N, κ_iv(Q) > 0; C = D_K with K ⊆ int Δ two-dimensional and ∂D_K∖{0} ⊆ N; C is weak Bayes for a branch mixture in all C(n,b)³ branches.
- **Conclusion.**
  - (a) At each world i, at least n − 2b + 2 (≥ b) judges have κ_iv|_{P(C)} positively proportional to one vector z_i ∈ ℝ^{P(C)}_{>0}. The ray of z_i is the only ray of ℝ^{P(C)} that carries b or more of the vectors κ_iv|_{P(C)}.
  - (b) There are λ ∈ ℝ³_{>0} and d ∈ ℝ^{P(C)}_{>0} with n^Q_i d_Q = λ_i z_i(Q) for all Q ∈ P(C) and all i.

*Proof.*
1. **Steps 1–4 of MM1's proof hold verbatim.** They treat one branch at a time and use only guidance (κ > 0) and weak Bayes. They give, for every branch, a vector d^F ∈ ℝ^{P(C)}_{>0} with A_i d^F ∈ cone{κ_iv|_{P(C)} : v ∈ F_i} at every world, where A_i := diag(n^Q_i)_Q.
2. **Apply Theorem 2.3.** Put a_iv := A_i^{−1}κ_iv|_{P(C)}. These are positive vectors, so take φ := sum of coordinates. Then d^F ∈ ⋂_i cone{a_iv : v ∈ F_i}, which is (H_b) with |S| = 3. Theorem 2.3 gives a positive vector z (it is a positive multiple of positive vectors).
3. **Transfer back.** Put z_i := A_i z. The linear bijection A_i maps rays to rays, so Theorem 2.3 (a) and (c) give (a). Taking d := z and λ := 𝟙 gives A_i d = z_i, which is (b). ∎

**Corollary 3.2 (MM1 Theorem 4.2 for 3q > 2n; PROVED, self-contained).**
- **Hypotheses.** Every judge is cellwise linear on the three min-cells M_k := {g_k < g_j, j ≠ k} on some open cone N ⊇ ∂D_{T1}∖{0}. The judges are arbitrary strictly guiding integrable judges off N. 3q > 2n.
- **Conclusion.** No coherent selection p ↦ C_p that is continuous in measure on Δ with T1 = C_{p₀} satisfies (QS). Already the per-branch weak Bayes condition fails.

*Proof.* Follow MM1's proof of Theorem 4.2.
1. **Step 1 (classification near T1).** Verbatim: it uses Theorem 4.1 Steps 1–4 for one branch.
2. **Step 2.** Use Corollary 3.1 with P = {M₁, M₂, M₃}, which is the same set of cells for every C near T1. By Corollary 3.1 (a), the ray of z_i is the unique ray of ℝ³ carrying b or more of the fixed vectors κ_iv|_P. So z_i depends on the judges only. This was the one point where MM1 used the doubled-middle structure of n = 4.
3. **Steps 3–4.** The uniqueness of the triangle model of the fixed field (z_i)_i, and the clopen argument with MM1 Lemmas 1.3–1.4, hold verbatim. ∎

**Corollary 3.3 (MM1 Corollary 4.3 for 3q > 2n; PROVED).** Take cellwise-linear judges on any finite fan with N ⊇ ∂D_{T1}∖{0}, and suppose (QS) holds at an interior p₀ with C_{p₀} = T1. Then for p near p₀ there is μ(p) ∈ ℝ³_{>0} such that, on every cell pinned by T1, ∂C_p is the boundary plane of the plain posterior C_μ.

*Proof.* MM1's Steps 1, 2 and 4 hold verbatim. Step 3 changes as follows.
1. **At C_p.** Corollary 3.1 gives at least b judges at world i proportional on P(C_p) ⊇ P(T1). They stay proportional after restriction to P(T1).
2. **At T1.** By Corollary 3.1 (a), applied with P(T1), there is exactly one ray carrying b or more of the restricted vectors.
3. **Conclusion.** So C_p and T1 use the same z_i on P(T1), and Step 4 applies. ∎

**Proposition 3.2 restated (MM1 Proposition 3.2; PROVED modulo FF2 Theorem 4.1 Steps 2–6 and their import chain, as recorded in MM1).** Suppose every world i has b judges whose penalty differences among the advices {+, 0, −} are positively proportional with constant ratios. Then no coherent selection that is continuous in measure on Δ and passes through T1 satisfies (QS).

*Scope remark on ×.* MM1 assumes proportionality for all advices. That is not needed.
- In MM1's Step 2 take ℓ*_i := ℓ_{iv_i}, including its own values at ×.
- The weak Bayes inequality at advice × holds for **every** nonnegative nonzero mixture, because × is strictly worst for every judge and a coherent C_p never advises ×.
- So the output of FF2 Step 1 holds for ℓ* as soon as the proportionality holds on {+, 0, −}.

**Corollary 3.4 (MM1 Proposition 5.1(b) for 3q > 2n; PROVED modulo Proposition 3.2).** In MM1's rank-two setting (σ_iv ∈ V_i := span(b_i1, b_i2) on ℝ³∖{0}), if dim R(C) ≤ 1 at some interior selected C, then (QS) fails for every coherent selection that is continuous in measure and passes through T1.

*Proof.*
1. **One representing vector.** As in MM1, every branch uses the same r spanning R(C), with π_i(r) in every b-cone of world i. The sign is fixed because world i's cone is pointed: its generators have the strict sign of g_i.
2. **Proportional judges.** A pointed finitely generated cone in V_i lies in an open half-plane. Lemma 2.1 in V_i then gives at least n − 2b + 2 ≥ b judges proportional to π_i(r) as elements of V_i, hence proportional as functions.
3. **Proportional penalty differences.** Proportional switch values give proportional c, c′ = σ(−·) and d = c − c′, which are the penalty differences among {+, 0, −}. Proposition 3.2 applies at every world. ∎

**Remark 3.5 (T1 alone still passes for 5-of-7, with heterogeneous judges; PROVED).** Take min-cell judges with A_i := diag((v_k)_i)_k and κ*_i := A_i𝟙 = (c₀ + εδ_ik)_k. Let τ_i := e_{i+1} − e_{i+2} and τ′_i := e_i − ½(e_{i+1} + e_{i+2}). Fix 0 < δ < c₀.
- **The judges at world i:** κ*_i, 2κ*_i, 3κ*_i, κ*_i ± δτ_i and κ*_i ± δτ′_i. All are positive.
- **Every branch is certified with d = 𝟙.** The vectors a_iv = A_i^{−1}κ_iv are 𝟙, 2·𝟙, 3·𝟙 and 𝟙 ± δA_i^{−1}τ_i, 𝟙 ± δA_i^{−1}τ′_i. Every 3-set either contains a multiple of 𝟙 or, having at least three of the four off-ray vectors, contains an antipodal pair 𝟙 ± x, whose midpoint is 𝟙. So 𝟙 ∈ cone(a_{F_i}) for every F_i.
- **Strictness.** The branch mixture then has switch value d_k v_k·g = P_{T1}(g) on M_k, so T1 is strictly certified in all 42 875 branches (MM1 Lemma 1.1(b)). This proves (QS) at T1 against every X.
- **No further proportionality.** span(κ*_i, τ′_i) = span(𝟙, e_i) does not contain τ_i. τ′_i = (3/2)e_i − ½𝟙 is not proportional to κ*_i. Hence no two of the four off-ray judges are proportional.
- **Whole-space choice.** The judges are taken cellwise linear on all of ℝ³, not only on N. The class allows this, and it makes P_{T1} = v_k·g hold on the whole cell M_k (MM1 Part 0), which the strictness step uses.
- **So isolation is the obstruction.** By Corollary 3.2, no family extends this. The isolation, not the single model, is what fails.

**Reading of §3.** Wherever a selected model's branch representations share a common linear parameter (the vector d of the cellwise-linear classes, or the relation space R(C) when it is a line), the branch structure collapses to a single field for every (n,q) with 3q > 2n. The extra freedom of 5-of-7 is invisible there, exactly as the 3-of-4 freedom was. No explicit escaping cone configuration exists in these geometries (Theorem 2.3 (b)).

---

## 4. MM2 re-derived for branch size 3; edge proportionality

**4.1 What carries over verbatim (PROVED; MM2's proofs).** MM2 Lemma 1.1, Lemma 2.1, Theorem 3.1, Lemma 3.2, Proposition 4.1, Corollary 4.2, Proposition 4.3, Theorem 5.1 and Lemma 5.2, Lemmas 6.1–6.3 and Theorem 6.4 use only |F_i| = n − q + 1, or nothing about n and q at all (MM2 §9). For 5-of-7:
- **Branches.** There are 42 875 at full support and C(7,3)² = 1 225 on an edge.
- **Dimension bound (MM2 Lemma 3.3).** dim W_p ≥ 3 still holds. Step 3 needs b ≤ n − 2, which is 3 ≤ 5.
- **Extreme supports at T1.** By MM2 Lemma 3.2, every support meets all three worlds. A support with s_i ≥ 1 judges at world i lies in ∏_i C(n − s_i, b − s_i) ≤ C(6,2)³ = 3 375 branches. Since 42 875/3 375 > 12, the cone W_p ∩ ℝ^{J}_+ needs at least 13 distinct extreme supports (PROVED by counting).
- **Edge identities (MM2 Theorem 6.4).** For a.e. s and each of the 1 225 edge branches (F_i, F_j), some w ≥ 0 with nonzero restrictions to F_i and F_j satisfies

    Σ_{v∈F_i} w_iv |τ_{s,iv}(g)| = Σ_{u∈F_j} w_ju |τ_{s,ju}(g)|  for every g ∈ Π_s ∖ N.   (4.1)

**Theorem 4.1 (edge proportionality; PROVED).**
- **Hypotheses.** Full domain; 3q > 2n; p ↦ C_p a coherent selection, continuous in measure on the closed edge [e_i, e_j], with (QS) at every point of the edge. Notation as in MM2 Theorem 6.4.
- **Conclusion.** For a.e. s ∈ (0,1) there are:
  - a null set N_s ⊆ Π_s (for two-dimensional measure);
  - a function z_s : Π_s ∖ N_s → (0, ∞);
  - sets I_s ⊆ J_i and I′_s ⊆ J_j, each with at least n − 2b + 2 (≥ b) elements;
  - constants γ_v(s) > 0;

  such that

    |τ_{s,iv}(g)| = γ_v(s) z_s(g)  (v ∈ I_s),   |τ_{s,ju}(g)| = γ_u(s) z_s(g)  (u ∈ I′_s),   for every g ∈ Π_s ∖ N_s.

  Moreover, for every b-set T ⊆ J_i, z_s is a nonnegative combination of the |τ_{s,iv}| (v ∈ T) on Π_s ∖ N_s, and likewise at world j.
- **In words.** On almost every edge plane, n − 2b + 2 judges at each edge world have switch magnitudes proportional to one common function along the whole plane, for all values of the off-edge payoff. For 5-of-7 this means three judges per edge world; for 3-of-4, two.

*Proof.*
1. **A good null set.** Let N₁ ⊆ Q_ij be the set where some switch map c_iv, d_iv, c_ju, d_ju is not approximately continuous, or has approximate value 0.
   - At a.e. point a measurable function is approximately continuous with approximate value equal to its value.
   - The values are nonzero a.e. by strict guidance.
   - So N₁ is null. MM2's Fubini step (Theorem 6.4, step 4) gives N_s := N₁ ∩ Π_s 2-null for a.e. s.
2. **The identities hold together.** Discard also the null sets of s on which (4.1) fails for one of the finitely many branches. For each remaining s, (4.1) holds on Π_s ∖ N_s for all 1 225 branches, with the switch type τ_s fixed by the model C_{p_s} (MM2 Theorem 6.4 (b)), hence common to all branches.
3. **Set up Theorem 2.3.**
   - Let V be the span of the 2n functions |τ_{s,iv}|, |τ_{s,ju}| on Π_s ∖ N_s. It has dimension at most 2n.
   - Fix g₀ ∈ Π_s ∖ N_s and put φ(f) := f(g₀). This is linear on V and positive on all 2n generators.
   - By (4.1), the common value Σ_{F_i} w|τ_{s,i}| lies in cone{|τ_{s,iv}| : v ∈ F_i} ∩ cone{|τ_{s,ju}| : u ∈ F_j}. It is nonzero, being positive at g₀.
   - This is (H_b) with S = {i, j}.
4. **Conclude.** Theorem 2.3 gives z_s ∈ V with the stated properties. z_s is a positive multiple of a positive function, so it is positive. ∎

*Remarks.*
- **Selection-independence.** As in MM2, the planes are forced, not designed: every continuous coherent (QS) selection has these edge boundaries (MM2 Theorem 6.4 (a)). So Theorem 4.1 is a condition on the judges alone, given only that such a selection exists.
- **A fixed triple on many planes.** There are finitely many candidate sets, so a fixed pair (I, I′) serves for a set of s of positive measure. On the union of those planes, |τ_iv|/|τ_iw| (v, w ∈ I) is a function of s, that is, of g_j/g_i, alone.

**Corollary 4.2 (PROVED).** Assume 3q > 2n, the full domain, and an open set U ⊆ Q_ij on which every c and d switch map is continuous. Suppose that for τ ∈ {c, d} and **every** b-set T ⊆ J_i (or every b-set T ⊆ J_j) there are v, w ∈ T such that |τ_iv|/|τ_iw| is non-constant on every segment in U parallel to the g_k-axis. Then no coherent selection that is continuous in measure on Δ satisfies (QS) everywhere, whether or not it passes through T1.

*Proof.*
1. **Planes through U.** For s in a nonempty open interval, Π_s ∩ U is a nonempty open subset of Π_s. It contains segments parallel to the g_k-axis, because Π_s contains that direction. Continuity gives N₁ ∩ U = ∅.
2. **Proportional judges on the plane.** Choose such an s for which Theorem 4.1 holds. It gives at least n − 2b + 2 ≥ b judges at world i, and at world j, with mutually proportional |τ_s| on Π_s ∩ U.
3. **Contradiction.** Any b of them form a b-set whose pairwise ratios are constant on such a segment, contrary to the hypothesis. ∎

*Comparison with MM2 Corollary 6.5.*
- MM2 needed every world-i/world-j ratio to be monotone in g_k. That is a cross-world condition, and constant ratios such as "world-i judges ignore g_k" escape only one side of it.
- Corollary 4.2 is a **within-world** condition, which holds for generic smooth judges.
- A design passing the edges must have, near every edge and for both switch types, a b-set of same-world judges whose magnitudes are proportional along every edge plane.
- For n = 4, q = 3 this already strengthens MM2 (pairs in place of triples).

---

## 5. The three bridges

### 5.1 Weak versus strict certification

- **Every result of §§2–4 uses weak certificates only.**
  - The inputs are MM2 Lemma 2.1 (weak Bayes in every branch) and MM2 Theorem 3.1/6.4 (alignment), which need weak Bayes only.
  - Strict certification is used only in the *positive* Remark 3.5.
- **Why no strictness is needed in §3 (PROVED).** In the cellwise-linear classes, a weak certificate α of a branch cannot vanish on any open subset of a pinned cell.
  - On Q its switch value is ω^Q·g, with ω^Q_i = Σ_{v∈F_i} α_iv κ_iv(Q).
  - ω^Q·g ≡ 0 on an open set forces ω^Q = 0. Since κ > 0, that forces α = 0.
  - So the degenerate "weak mixture vanishing near a corner" of AUDIT_MM point 2 cannot occur there. MM1 Theorem 4.1 Step 3 already used this, and Corollary 3.1 inherits it.
- **Edges.** On the edges, Theorem 4.1 uses (4.1) only *on* the planes Π_s. It needs no information off them, so a certificate that vanishes off Π_s is covered.
- **Where vanishing certificates matter.** Only in the sum form of §6, where switch values of different worlds can cancel identically. There the gap between weak and exact is decisive in both directions:
  - Proposition 6.1 passes every weak/alignment condition;
  - Proposition 6.3 shows that the same data fail the exact test.

### 5.2 Local versus global proportionality

- **Corollaries 3.1–3.3** produce proportionality **only on the pinned cells**. Corollary 3.2 nevertheless excludes (QS), because near T1 the selected models are determined by their pinned cells (MM1 Thm 4.2 Step 1). Global proportionality is never used.
- **Proposition 3.2** needs **global** proportionality with a constant ratio. Its proof feeds one fixed field into FF2 Theorem 4.1.
- **Theorem 4.1** gives a third, intermediate kind: proportionality along each edge plane, with constants γ_v(s) that may depend on the plane.

**Observation 5.1 (the gap is real; PROVED).** Plane-wise proportionality does not give the hypothesis of Proposition 3.2.
- **Example.** Let ℓ_iv be strictly guiding and integrable, let ρ : (−∞, 0) → [1, 2] be measurable and non-constant, and put ℓ_iw(h,a) := ρ(h_j/h_i) ℓ_iv(h,a) on Q_ij (and ℓ_iw := ℓ_iv elsewhere).
  - ℓ_iw is strictly guiding with an integrable envelope.
  - Its penalty differences are proportional to those of ℓ_iv with the constant ratio ρ(−(1−s)/s) on each plane Π_s.
  - They are not proportional with a constant ratio on Q_ij.
- **Effect on the branch mixture.** A branch mixture α_vℓ_iv + α_wℓ_iw = (α_v + α_wρ(h_j/h_i))ℓ_iv is a single field reweighted by a function of h. The reweighting depends on p through α.
- **Consequence.** FF2 Theorem 4.1 Steps 2–4 (closed graph, covering, (γ)) need one field fixed in p, and they get no input from this. Turning Theorem 4.1 into a global exclusion therefore needs an argument that the constants γ_v(s) cannot depend on s. I do not have one.

### 5.3 Arbitrary selected shapes versus moving corners

- **No result here assumes moving or persistent corners.**
  - Corollary 3.2 *derives* the shape of every selected model near T1 from cellwise linearity. On a pinned cell the weak Bayes mixture is linear and vanishes on the boundary piece, so the piece is planar. A cell cannot contain two facets. Hence nearby models are polygons with corner rays on cell walls (MM1 Thm 4.2 Step 1, valid for any b).
  - Rounding a corner is impossible in that class, because it would need infinitely many cells or non-linear judges.
  - On the edges, shapes are forced by (QS) itself (MM2 Lemma 6.2: K_p is a segment of the edge).
- **What is not covered.** In the interior, with judges that are not cellwise linear (or are cellwise linear on a fan with cells not pinned by T1), the selected models may round their corners immediately away from T1. None of the results above constrains them there except through MM2's alignment.
- **The analytic obstruction.** MM1 Proposition 2.1 (analytic judges, at a corner of the selected model) applies only at models that have corners. It is not used here.

---

## 6. Where the collapse does not reach: three active worlds in sum form

### 6.1 The sum form

At an interior p, MM2 Theorem 3.1 gives the following for every branch F. With u_i := Σ_{v∈F_i} w_iv σ_iv (approximate values on ∂C_p),

  u₁ + u₂ + u₃ = 0 at every common essential boundary point.                        (6.1)

This is a **sum** relation, not a common point of cones. It becomes one in exactly two situations:
- **Edges.** With two worlds, u_i = −u_j, which is §4.
- **Cellwise-linear judges.** u_i(g) = ω_i g_i on a planar piece, and (6.1) forces ω ∝ n^Q, so all worlds share the parameter d. That is §3.

In MM1's rank-two language, (6.1) says (u_i) ∈ R(C). Theorem 2.3 needs the cones to be pulled back to one common space. That happens when R(C) is a line (Corollary 3.4), not in general.

### 6.2 An exact escaping configuration in sum form

**Proposition 6.1 (CHECKED, `sumform_escape.out`).** Let d₁ = (1, −2), d₂ = (2, 1), d₃ = (−2, 1), and for world i put

  a_iv := d_i + (k/20) d_i^⊥,  k = −3, …, 3,  where (x, y)^⊥ := (−y, x)

(seven vectors per world, listed in the output). Then:
- (i) no two a_iv at one world are proportional;
- (ii) every choice of one vector per world (343 choices) is positively dependent with all three weights positive. Hence each of the 42 875 branches F has an explicit w ≥ 0 supported in F, nonzero at all three worlds, with Σ_F w_iv a_iv = 0;
- (iii) for each of the six mixed sign patterns s there is an explicit β_s ∈ ℚ² with sgn⟨a_iv, β_s⟩ = s_i for every judge. For example, s = (+, −, +) is realised by β_s = (−12, −12). No β realises a pure pattern.

**Consequence (PROVED from the CHECKED facts).** Let N be an open set of mixed gambles, and let β : N → ℝ² be any measurable map with β(g) ∈ A_{s(g)}, where

  A_s := {β : sgn⟨a_iv, β⟩ = s_i for all i, v}

and s(g) is the sign pattern of g. Put σ_iv(g) := ⟨a_iv, β(g)⟩ on N, and extend arbitrarily off N by MM1's realisation lemma. Then:
- the switch values are strictly guiding on N;
- every one of the 42 875 branches satisfies (6.1), indeed Σ_F wσ ≡ 0 on N, for every model whose boundary lies in N;
- no two judges are proportional on N.

So the sum-form analogue of Theorem 2.3 is **false**: (6.1) for all branches does not force proportional blocking sets. This is the explicit configuration escaping the collapse that the brief asked for.

### 6.3 But it fails the exact test

**Lemma 6.2 (zero-sum records; PROVED).** Let C be a model, and let E_1, …, E_m be pairwise disjoint non-null sets of oriented gambles. Suppose each E_k is accepted by C ("accept g only"), silence is available on each E_k (full domain, or (LF)), and the accept-to-silence switch vector σ(g) = (ℓ_iv(g, 0) − ℓ_iv(g, accept g))_{i,v} is bounded on each E_k. Suppose further that the vectors x_k := ∫_{E_k} σ dμ satisfy Σ_k θ_k x_k = 0 for some θ ≥ 0, θ ≠ 0. Then (QS) fails at every p with C_p = C.

*Proof.*
1. **A zero-sum set.** By Lyapunov's theorem for the atomless vector measure E ↦ (∫_E σ dμ, μ(E)) on ⋃E_k, the range is convex. It contains each (x_k, μ(E_k)), hence (0, Σ_k t_k μ(E_k)) with t_k := θ_k/Σθ. So some E ⊆ ⋃E_k has μ(E) > 0 and ∫_E σ = 0.
2. **The record.** Let X be C with silence on the pairs of E. These pairs are distinct, since C accepts g only. Then Δ_iv(p, X) = ∫_E σ_iv = 0 for every judge at every world.
3. **Conclusion.** X ≠ C, and no judge strictly prefers C_p, so (QS) fails. ∎

**Proposition 6.3 (fixed-column rank-two data fail exactly; PROVED).**
- **Hypotheses.** Let N be an open set of mixed gambles, let a_iv ∈ ℝ² be **any** fixed vectors, and let β : N → ℝ² be measurable with ⟨a_iv, β(g)⟩ = ℓ_iv(g, 0) − ℓ_iv(g, accept g) for a.e. g ∈ N. Let C be a model that, for each of the six mixed patterns s, accepts a non-null set of g ∈ N with pattern s, with silence available there.
- **Conclusion.** (QS) fails at every p with C_p = C.
- **Scope.** This applies to T1, and to every D_K with K Hausdorff-close to T1, whenever N contains a neighbourhood of ∂D_{T1}∖{0}. Each facet piece has an accepted side carrying its pattern, all six patterns occur (MM2 §5), and the pieces persist under small perturbation. In particular, the configuration of Proposition 6.1 cannot carry T1 or any model near it.

*Proof.*
1. **The pattern cones.** Strict guidance gives β(g) ∈ A_{s(g)} a.e. on N. The A_s are open convex cones, pairwise disjoint, with A_{−s} = −A_s.
2. **One vector per pattern.** For each s choose a bounded non-null accepted E_s ⊆ N of pattern s with |β| ≤ M on E_s. Then x_s := ∫_{E_s} β lies in A_s, because each defining strict inequality integrates to a strict inequality.
3. **Claim: the six x_s lie in no closed half-plane {⟨f, ·⟩ ≥ 0}, f ≠ 0.**
   - Suppose they did. Then A_s meets {⟨f, ·⟩ ≥ 0} through x_s, and also {⟨f, ·⟩ ≤ 0} through −x_{−s} ∈ −A_{−s} = A_s.
   - A_s is connected and open, so it meets the line f^⊥.
   - The line f^⊥ is two rays, and each ray lies in at most one of the disjoint A_s. So at most two of the six cones meet it, which is a contradiction.
4. **Positive dependence.** A finite set lying in no closed half-plane has 0 in the interior of its convex hull. So Σ θ_s x_s = 0 with θ > 0.
5. **Conclude.** ∫_{E_s} σ_iv = ⟨a_iv, x_s⟩, so Σθ_s ∫_{E_s} σ = 0. Lemma 6.2 applies. ∎

*Remarks.*
- **What the proof uses.** No branches, certificates, continuity of the selection or properties of the columns. It is a pure rank count: six pattern cones cannot all avoid one line in ℝ².
- **Why certificates vanish here.** At a model whose boundary pieces in N carry all six patterns, each with both sides present, every weak certificate restricted to N has the form ⟨r, β⟩ with r = Σ_F w a. If r ≠ 0, weak Bayes would need A_s to meet r^⊥ for all six s, which is impossible by step 3. So r = 0: in rank two every weak certificate vanishes identically on N. Proposition 6.1's alignment is exactly of that degenerate kind, and the exact test then detects the zero-sum record.
- **Rank k.** The same argument works for data σ = Cβ with β ∈ ℝ^k. (QS) fails whenever the accepted integrals ∫_{E_s} β positively span ℝ^k. This can be avoided only if the accepted pattern cones in ℝ^k are not "balanced". For k ≥ 3 they need not be, so Proposition 6.3 does **not** extend automatically.

### 6.4 What remains

The target, stated without added assumptions, is this. Find 3n strictly guiding integrable judges and a coherent selection, continuous in measure through T1 (with W_i at the vertices and edge segments on the edges), such that:
- **(T1) Edges.** The edge planes satisfy (4.1) and hence Theorem 4.1: a b-set of proportional judges per edge world on almost every plane, with switch types fixed per plane.
- **(T2) Alignment.** At every interior selected model, every one of the 42 875 branches satisfies (6.1).
- **(T3) Exactness.** The exact nonstrict test (NT_F) holds. In particular, no zero-sum record exists (Lemma 6.2). Where a weak certificate vanishes, the second-order records near boundary points must also be blocked (MM2 §7 (R5)).
- **(T4) No collapse.** The interior boundary data are **not** of common-parameter form. Otherwise Theorem 2.3, with Proposition 3.2 or the argument of Corollary 3.2, applies.

Propositions 6.1–6.3 show that (T2) and (T4) are compatible, and that rank two is too small for (T3).

**CONJECTURE 6.4.** Along a continuous family through T1, (T3) forces the interior boundary data, branch by branch, into common-parameter form, and hence into collapse by Theorem 2.3. The evidence:
- rank two forces vanishing certificates and then zero-sum records;
- in the cellwise-linear classes the common parameter is automatic;
- on the edges it is automatic.

Settling this would decide (QS) through T1 for every (n,q) with 3q > 2n.

---

## 7. Status table

| Item | Statement | Label |
|---|---|---|
| 2.1 | depth count: a point in all b-cones of one world ⇒ ≥ n − 2b + 2 vectors on its ray | PROVED; CHECKED (Part 3) |
| 2.2 | two families of intervals, all cross pairs meeting ⇒ one family has a common point | PROVED |
| 2.3 | blocking-cone collapse, any b, any dimension, ≥ 2 worlds, 3q > 2n | PROVED; CHECKED (1D exhaustive; exact certificates in ℝ⁴, ℝ⁵) |
| 3.1 | cellwise-linear, any finite fan: all-branch weak Bayes ⇒ single field on pinned cells | PROVED |
| 3.2 | min-cell judges: (QS) fails through T1 for every continuous coherent selection, all 3q > 2n | PROVED (self-contained) |
| 3.3 | general fans near T1: plain posteriors on T1-pinned cells | PROVED |
| 3.2 (MM1) | proportional blocking sets at every world ⇒ (QS) fails; proportionality on {+,0,−} suffices | PROVED modulo FF2 Thm 4.1 imports |
| 3.4 | rank-two worlds with dim R(C) ≤ 1 ⇒ (QS) fails | PROVED modulo 3.2 (MM1) |
| 3.5 | T1 alone passes (QS) for 5-of-7, 42 875 branches strictly certified, heterogeneous judges | PROVED |
| 4.1 (list) | MM2's branch reformulation, alignment, sign lemma, generic and separable failures, edge identities for b = 3; dim W_p ≥ 3; ≥ 13 extreme supports at T1 | PROVED (MM2's proofs; counting) |
| 4.1 | edge proportionality on a.e. edge plane | PROVED |
| 4.2 | within-world non-constant ratios near an edge ⇒ no continuous (QS) selection | PROVED |
| 5.1 | plane-wise proportionality does not give Prop 3.2's hypothesis | PROVED (example) |
| 6.1 | sum-form escaping configuration: all 42 875 branches, no proportional judges, six patterns | CHECKED |
| 6.2 | zero-sum records defeat (QS) | PROVED |
| 6.3 | fixed-column rank-two data fail (QS) at T1 and nearby models | PROVED |
| 6.4 | the exact test forces common-parameter form along families | CONJECTURE |
| — | (QS) for 5-of-7 through T1 with arbitrary judges | **open** |

**Hypotheses used.**
- (IB), (TC), closed sections, absence of ties: none, anywhere.
- 3q > 2n: Theorem 2.3 step 5 and everything built on it.
- Continuity in measure: Corollary 3.2 and §4.
- Full domain: §4 (as in MM2 §6) and Proposition 6.3 (silence available on E).
- Coherence of selected models: §§3–4.

**Files (`nn2py/`).**
- `collapse_check.py` → `collapse_check.out`:
  - Part 1: one-dimensional exhaustive checks of Theorem 2.3: two worlds with values in {0..3} (14 400 configurations); three worlds with values in {0,1,2} (46 656). In both, the hypothesis holds iff the middle triples coincide at a common value.
  - Part 2: random exact instances in ℝ⁴ and ℝ⁵ (generic; one world collapsed; collapsed on distinct rays; one-vector perturbations), each with an exact projection certificate of failure; and common-ray configurations, verified to have z in all 3 × 35 triple cones.
  - Part 3: the depth count.
- `sumform_escape.py` → `sumform_escape.out`: Proposition 6.1 (columns, 343 triples, 42 875 branches, six realising β_s, no pure pattern) and, as an auxiliary fact not used in any proof, open half-planes containing the 14 columns of each pair of worlds.
