# C2 report: what survives when (S) and (T) are replaced by W (round 84)

Agent C2, 29 Oct 2026. Sources read: BRIEF84; ROUND83_overview (§0 first); LESSONS_H1–H5; the auditor's Handoff and Assessment (device, read-only); r82/appshort.tex; on the device, *The Contamination Triangle.tex* (§§2–5, the statement and status of Theorem gm, and §5's hypotheses), *Full Coverage by Homothetic Credal Families v3.tex* (Thm. 8 and its appendix, including the three-world compatibility lemma) and *Three Complete Rankings Cannot Cover.tex* (§§1–3). I also read the local copy of *Complete Rankings for Any Number of Worlds.tex* (main theorem and Remark rem:hyp), because the device dropped out during the session.

Labels: **PROVED** means a complete continuum proof is given here. **CHECKED** means I re-derived a cited argument or verified it by direct computation. **CONJECTURE**, **UNCLEAR** and **FAILS** have their usual meanings. Numerics were used for illustration only (§5.5); no claim rests on them.

---

## 0. Results first

| # | Question | Verdict |
|---|---|---|
| 1a | Complete integral ranking s_i = ∫_X ψ_i, ψ_i integrable, sign-respecting, otherwise arbitrary, satisfying W ⇒ every Bayes set {p·ψ > 0} (p ∈ Δ) is almost coherent, and tie sets are null at interior p | **PROVED** (Thm 1.1). W is used only through its conclusion that every incoherent model is dominated. |
| 1b | Hence T1 (indeed every all-facing triangle in general position, n = 3) is dominated under every such ranking | **PROVED** (Cor 1.3), via the refereed realisation theorem `thm:main`, not via gm verbatim. |
| 1c | Does gm apply verbatim? | **No** (CHECKED). gm assumes four-rank strict guidance (contradiction worst) and the original (S). Gamble-additive scores violate the first on the full domain. The realisation form of the theorem needs neither. |
| 1d | Converse: if tie sets are null at *every* p ∈ Δ, then W ⇔ all Bayes sets almost coherent | **PROVED** (Prop 1.4). |
| 2a | Intersection of finitely many integral judges; D_M undominated ⇒ D_M is Bayes for a nonnegative weight array Λ₀ on (judge, world) pairs | **PROVED** (Prop 2.1). |
| 2b | Under W, B_Λ is almost coherent for every Λ ≥ 0, Λ ≠ 0, with null ties if Λ ≫ 0 | **PROVED** (Prop 2.2). |
| 2c | Lead's conclusion (T1 cannot be protected) | **PROVED** whenever some supporting weight of D_M gives a world field c with null ties at every interior prior, in particular whenever Λ₀ ≫ 0 (Thm 2.3). |
| 2d | Lead's step "any incoherent Bayes set of φ is undominated under the intersection" | **FAILS** as a general inference when φ has zero weights: explicit example (Prop 2.4). Weak comparisons transfer to φ; strict ones do not. |
| 2e | Residual case: every supporting weight has a zero entry and c has a non-null tie set at some interior prior | **UNCLEAR**. It is the same loophole as 3d. |
| 3a | Lexicographic order with a pure commission layer first | **PROVED**: every undominated coherent model's credal set contains a vertex. V is undominated; T1 is dominated by V (Prop 3.2). |
| 3b | Lexicographic order with a strictly guided first layer ψ¹: a covered interior target is ψ¹-Bayes at an interior prior | **PROVED** (Prop 3.3). |
| 3c | Same, with null first-layer ties at every interior prior, under W ⇒ T1 dominated; box-first orders reach only the box family and satisfy W | **PROVED** (Thm 3.4). |
| 3d | First-layer tie sets that are non-null at some interior priors (a Lebesgue-null, nonempty set of priors) | **CONJECTURE/lead**. This is the only escape left for additive-based rankings. It is exactly the gap that Remark N20 of the Contamination Triangle note identifies. |
| 4a | Does the 11 Oct "V dominated for complete rankings" proof survive with W? | **No** (CHECKED). It uses closed *full* sections (T1), the face lemma, coherent edge selections and their competitiveness. W supplies none of these. Independence and guidance transfer without change. |
| 4b | Complete integral rankings under W, n ≥ 3: every coherent D_M whose credal set contains three vertices, V included, is dominated | **PROVED** (Thm 4.2), from Thm 1.1 and the three-world compatibility lemma of v3. |
| 4c | General complete (non-integral) rankings under W | **UNCLEAR**. |
| 5a | Under independence, dominance is a property of the change (A, R). The undominated models are exactly those to which no dominating change is available. | **PROVED** (Prop 5.1). |
| 5b | Generalised copy lemma: a dominating change is available to no undominated model | **PROVED** (Cor 5.2). |
| 5c | Incoherent X ⊇ T: every dominator removes a non-null part of X∖T. X ⊆ T: every dominator re-adds part of T∖X. Mixed case: one or the other. | **PROVED** (Cor 5.3). |
| 5d | Dominating changes are anti-guided at no world. If the excess E lies in {g_i > 0}, a dominator of T ∪ E keeping T must add gambles positive at i. | **PROVED** (Lemma 5.4). |
| 5e | A pure removal of R can dominate only if no undominated model contains R | **PROVED** (Cor 5.5). Box illustration CHECKED. |
| 5f | Assignment-containment test, generalising the audit's obstruction to every assignment and ranking: if every assigned weak dominator of an incoherent x ⊇ T contains x, W fails | **PROVED** (Prop 5.6). |
| 5g | The assignment must leave out part of every bounded excess and pick up part of every bounded deficit | **PROVED** (Cor 5.7). |

**Net map.** Under W, every complete additive ranking, every finite intersection with a properly efficient target, and every lexicographic order with a tie-free first layer is excluded for T1. The same holds for every three-vertex target, V included. The one structural freedom that survives for additive building blocks is a **non-null indifference set of the first-level field at some interior prior**, resolved by a second criterion (§3.5, §2.5). The proof of `thm:main` does not cover that case: its hypothesis (BU) must hold at *every* interior prior. That freedom is the lead I would hand to C1. Beyond it, only genuinely non-additive or incomplete rules remain, and item 5 lists the necessary conditions they must meet.

---

## Standing facts

Throughout, Ω = {1,…,n}, μ is standard Gaussian on ℝⁿ (it has the same null sets as Lebesgue measure), and models are measurable sets modulo null sets. D_K = {g : min_{m∈K} m·g > 0} ∪ {g ≥ 0, g ≠ 0}. "Almost coherent" means equal a.e. to some D_K.

- **(F1)** {P_K = 0} is null (it meets each line parallel to 𝟙 once). D_{K₁} ∩ D_{K₂} = D_{co(K₁∪K₂)}, so a finite intersection of almost coherent models is almost coherent.
- **(F2) Limits.** If almost coherent X_m → X in measure, then X is almost coherent. *Proof.* Write X_m = D_{K_m}. By Hausdorff compactness, some subsequence has K_m → K. Then |P_{K_m}(g) − P_K(g)| ≤ ‖g‖_∞ d_H(K_m, K) → 0, so 1_{D_{K_m}} → 1_{D_K} off the null set {P_K = 0}. Hence X = D_K a.e. ∎
- **(F3) Cones are unbounded.** A scale-invariant set S of positive measure is not a.e. contained in a ball, since λ(S ∩ B(0,2R)) = 2ⁿ λ(S ∩ B(0,R)). Hence, for coherent C and non-null bounded E disjoint from C, both C ∪ E and C ∖ E' (E' ⊆ C non-null bounded) are incoherent: their difference from a cone would be a.e. a bounded difference of cones.
- **(F4) Lyapunov and separation.** Let Φ: ℝⁿ → ℝᵈ be integrable. Its range ℛ = {∫_X Φ dμ} is compact and convex. If y = ∫_Y Φ has no point of ℛ strictly above it in every coordinate, then there is λ ≥ 0, λ ≠ 0, with λ·y = max_ℛ λ·(·). Then Y ⊇ {λ·Φ > 0} and Y ∩ {λ·Φ < 0} is null: Y is *λ-Bayes*. If y is even Pareto-maximal, the same holds.
- **(F5) Change form of independence.** The brief's arbitrary-D independence makes each verdict at world i, in both directions, a function of the change (A, R) = (Y∖X, X∖Y). Proof: take D = A ∪ R and context F = X ∩ Y.

---

## 1. Complete additive rankings under W

Hypotheses (H1):
- ψ_i ∈ L¹(μ);
- ψ_i(g)·g_i > 0 for a.e. g (*sign-respecting*), with no homogeneity, concavity or continuity assumed;
- X ⪰_i Y iff s_i(X) ≥ s_i(Y), where s_i(X) = ∫_X ψ_i dμ.

Such a ranking is complete at each world, so reflexivity, the three-model condition and transitivity through ties hold. Independence holds because s_i(Y) − s_i(X) = ∫_A ψ_i − ∫_R ψ_i. World-by-world guidance holds, and for integral rankings it is *equivalent* to sign-respect. Write B_p = {p·ψ > 0} and N_p = {p·ψ = 0}. The p-Bayes models, the maximisers of p·s, are exactly the sets B_p ∪ Z with Z ⊆ N_p.

**Theorem 1.1 (PROVED).** Assume (H1), and assume that every incoherent model is dominated. This holds in particular if W1–W3 hold for some common assignment, by Theorem W. Then:
- (a) for every interior p, N_p is null and B_p is the a.e.-unique p-Bayes model, which is almost coherent;
- (b) for every p ∈ Δ, B_p is almost coherent, and its credal set lies in Δ_{supp p};
- (c) every undominated model is p-Bayes for some p ∈ Δ, and equals B_p if p is interior.

*Proof.*

(a) *Interior Bayes models are undominated.* Let p be interior and let Y be p-Bayes. Suppose Z dominates Y. Then s(Z) ≥ s(Y) with strict inequality in some coordinate, and p ≫ 0 gives p·s(Z) > p·s(Y) = max, which is absurd. So every p-Bayes model is undominated and, by hypothesis, almost coherent.

*Ties are null.* Suppose N_p were non-null. Choose R with Z := N_p ∩ B(0,R) non-null. Then B_p and B_p ∪ Z are both almost coherent, so Z is a.e. a difference of cones, which contradicts (F3). Hence N_p is null.

(b) *Vertices.* For p = e_k, B_{e_k} = {g_k > 0} a.e., which is coherent.

*Boundary points.* Let p ∈ ∂Δ be any other boundary point, and let r be interior.
- *Path limits.* Put q_t = (1−t)p + t r for t ∈ (0,1]. Off N_p, sign(q_t·ψ) → sign(p·ψ). On N_p, q_t·ψ = t r·ψ for every t. So 1_{B_{q_t}} converges pointwise to the indicator of L_r := B_p ∪ (N_p ∩ {r·ψ > 0}), except on the set N_p ∩ {r·ψ = 0}.
- *The exceptional set is null for a.e. r.* For each g ∈ N_p with ψ(g) ≠ 0, the vector ψ(g) is not parallel to 𝟙 (otherwise p·ψ(g) ≠ 0). So {r : r·ψ(g) = 0} is a proper affine subspace of aff Δ. By Fubini on (r, g), the set N_p ∩ {r·ψ = 0} is null for a.e. r.
- *Limits are coherent.* For such r, dominated convergence and (F2) make L_r almost coherent. Let good r_m → e_k. Then 1_{L_{r_m}} converges, off the null set {g_k = 0}, to the indicator of C_k := B_p ∪ (N_p ∩ {g_k > 0}), so C_k is almost coherent.
- *Intersection.* On {g ≫ 0} we have p·ψ > 0, so N_p ∩ {g ≫ 0} = ∅. Hence ⋂_k C_k = B_p, which is almost coherent by (F1).

Finally, B_p ⊇ {g_i > 0 ∀ i ∈ supp p}, which forces K ⊆ Δ_{supp p}.

(c) An undominated Y has s(Y) Pareto-maximal in the range, so (F4) gives λ ∈ Δ with Y λ-Bayes. Part (a) does the rest. ∎

**Remark 1.2 (CHECKED): gm's exact hypotheses.** Theorem `thm:gm` (*The Contamination Triangle*, §5) assumes all of the following:
- a strictly guiding additive ranking with integral penalties and integrable envelopes;
- a decomposable domain with (LF) at D_{T1};
- (LA), (S) in its original closed-choice form, and (C);
- coverage of T1.

Here "strictly guiding" refers to the four-rank order good ≺ silence ≺ bad ≺ contradictory. A gamble-additive score gives contradictory advice the value good + bad, which is strictly better than bad. So gm's (G) fails on the full domain, and (S) is not available under W. gm therefore does **not** apply verbatim.

The same note's `thm:main`, refereed twice, needs only a *realisation* (`def:realisation`). This is a measurable c: U → ℝ³ on U = D_{K'}, with K' ⊆ relint T, such that:
- each c_i has the strict sign of g_i a.e.;
- **(BU)** for every interior q, {g ∈ U : q·c = 0} is null and {g ∈ U : q·c > 0} = D_{K_q} a.e.;
- **(TP)** K_{p*} = T.

Remark N20 of the note stresses that (BU) is needed at *every* interior q.

**Corollary 1.3 (PROVED).** Let n = 3, and let M be an all-facing triangle in general position. This includes T1 = {m : m_i ≥ a} for every 0 < a < 1/3, which is the ε-contamination with ε = 1 − 3a. Then D_M is dominated under every ranking satisfying (H1) and W.

*Proof.* Suppose D_M is undominated. By 1.1(c), D_M is p*-Bayes for some p*. A boundary p* is impossible, since it would put M in a face (1.1(b)). So p* is interior and D_M = B_{p*}. Fix K' ⊆ relint M and U = D_{K'} ⊇ D_M, and put c := ψ|_U.
- *(BU).* For interior q, the tie set lies inside N_q, which is null by 1.1(a). Also {g ∈ U : q·c > 0} = B_q ∩ U = D_{co(K_q ∪ K')} a.e., by (F1).
- *(TP).* B_{p*} ∩ U = D_M.

So c is a realisation of M at p*, which `thm:main` excludes. ∎

**Proposition 1.4 (PROVED): converse under null ties.** Assume (H1) and that N_p is null for *every* p ∈ Δ. Then W holds if and only if every B_p is almost coherent.

*Proof.* (⇒) is 1.1. (⇐) is the Handoff's box argument, written out in general.
- *Continuity.* If q_m → p, then 1_{B_{q_m}} → 1_{B_p} off N_p, so p ↦ s(B_p) is continuous by dominated convergence.
- *Strict defence.* Let x be incoherent. Then x ≠ B_p, which is the unique p-Bayes model, so p·(s(B_p) − s(x)) > 0. Hence some i ∈ supp p has s_i(B_p) > s_i(x).
- *Conclusion.* The strict sections O_i(x) = {p : s_i(B_p) > s_i(x)} are open and cover supports. Handoff §4.1 then gives W1–W3 with b_p = B_p. ∎

So for complete integral rankings, the whole question under W is coherence of the Bayes family. T1 and every three-vertex target (§4) are out. Per H3 §3, polygons arbitrarily close to T1 (hexagons and 9-gons from gauge mixtures) are reached additively; I have not re-checked that. Since (S) and (T) imply W, any such construction that satisfies them meets W. That is the nearby reachable result in this class.

---

## 2. Intersections of additive rankings

Setting: a finite set J of judges, each with fields ψ^k_i satisfying (H1). The intersection relation is X ⪰_i Y iff s^k_i(X) ≥ s^k_i(Y) for all k. It is reflexive and transitive, hence satisfies the three-model condition and transitivity through ties. It is independent (F5) and world-by-world guided, since every judge is strictly guided. Write:
- S(X) = (s^k_i(X))_{k,i} ∈ ℝ^{J×Ω} and Ψ = (ψ^k_i);
- for Λ ≥ 0, Λ ≠ 0: F_Λ = Λ·Ψ, B_Λ = {F_Λ > 0} and N_Λ = {F_Λ = 0}.

**Proposition 2.1 (PROVED).** Y is undominated under the intersection if and only if S(Y) is Pareto-maximal in the range. Domination is exactly S(Z) ≥ S(Y) with S(Z) ≠ S(Y). Hence an undominated Y is Λ₀-Bayes for some Λ₀ ≥ 0, Λ₀ ≠ 0, by (F4). If Y = D_M with M ⊆ int Δ, then every world carries positive weight: p_i := Σ_k λ⁰_{k,i} > 0. Otherwise B_{Λ₀} ⊇ {g_j > 0 ∀ j ≠ i}, which would push M into a face.

**Proposition 2.2 (PROVED).** Suppose every incoherent model is dominated under the intersection, for instance under W. Then:
- for Λ ≫ 0, N_Λ is null and B_Λ is almost coherent;
- for every Λ ≥ 0 with Λ ≠ 0, B_Λ is almost coherent.

*Proof.*
- *Λ ≫ 0.* Every Λ-Bayes model is undominated: a dominator Z has S(Z) ≥ S(Y) with S(Z) ≠ S(Y), so Λ·S(Z) > Λ·S(Y). The argument of 1.1(a) then applies verbatim.
- *Λ ≥ 0, Λ ≠ 0.* Repeat the argument of 1.1(b) in the orthant of ℝ^{J×Ω}. Approach Λ along Λ + tΓ with Γ ≫ 0 generic; Fubini over Γ works because Ψ(g) ≠ 0 a.e. Then let Γ tend to the unit weight on (k, i), which gives B_Λ ∪ (N_Λ ∩ {g_i > 0}). Finally intersect over i, using that F_Λ > 0 on {g ≫ 0}. ∎

**Theorem 2.3 (PROVED): the lead's conclusion, rigorous version.** Let n = 3 and M be as in Cor 1.3. Let D_M be undominated under an intersection satisfying W, and let Λ₀ be any supporting weight. Put c_i := Σ_k λ⁰_{k,i} ψ^k_i. If {q·c = 0} is null for every interior q, a contradiction follows. In particular this holds whenever D_M is properly efficient, that is, whenever some supporting weight satisfies Λ₀ ≫ 0.

*Proof.*
- *c is admissible.* c is sign-respecting by Prop 2.1 and integrable.
- *Bayes sets of c.* q·c = F_{Λ(q)} with Λ(q)_{k,i} = q_i λ⁰_{k,i}, so {q·c > 0} = B_{Λ(q)}, which is almost coherent by 2.2 for every q.
- *The target.* Ties at u are null, so D_M (which is Λ₀-Bayes) equals B_{Λ₀} = {u·c > 0}.
- *Realisation.* Restricting c to U gives a realisation of M at u, as in Cor 1.3, which is a contradiction. If Λ₀ ≫ 0, then Λ(q) ≫ 0 for interior q, and the ties are null by 2.2. ∎

**Proposition 2.4 (FAILS: the sketch's middle step).** The step "the mixture ranking contains the intersection's comparisons, so every incoherent Bayes set of φ is undominated under the intersection" is invalid when φ gives some judge-world pairs zero weight. Weak comparisons transfer to φ, but strict ones do not.

*Example*, n = 3:
- *The two judges.* Judge 1 has ψ¹_i(g) = w_i sign(g_i) with w = (1,1,2). Judge 2 is a box score with ψ²_i = g_i⁺ − 2g_i⁻.
- *Ties of φ.* Let φ be judge 1 alone, at prior u. Then u·φ = 0 exactly on the non-null set N = {g₁,g₂ > 0 > g₃} ∪ {g₁,g₂ < 0 < g₃}.
- *An incoherent φ-Bayes set.* Let Z be a small ball about (1,1,−1) and put Y = B ∪ Z, where B = {u·φ > 0}. Y is φ-Bayes. It is incoherent, because it contains neighbourhoods of (1,−5,1) and (−5,1,1) but not of their sum.
- *Its dominator.* Let Z' be a ball about (2,2,−½) inside the same orthant, with μ(Z') = μ(Z). Judge-1 scores depend only on mass per sign pattern, so they agree. Judge 2 is strictly better at every world when the radius of Z is small. So Y' = B ∪ Z' dominates Y under the intersection.

**2.5 Residual (UNCLEAR).** A counterexample to the *conclusion* needs all of the following:
- every supporting weight of S(D_M) has a zero entry at some judge-world pair, while every world is still represented;
- the associated field c has a non-null tie set at some interior prior; by Fubini the set of such priors is Lebesgue-null;
- D_M is then a *lexicographic* Bayes set (Λ₀ first, then a second weight on N_{Λ₀}), not a realisation.

This is §3's loophole again. I found no argument excluding it, and no example. Infinite families are UNCLEAR: Pareto-maximal points need not have supporting functionals in ℝ^ℕ. The dense-mixture device of H3 item 11 only shows that the intersection's undominated class contains that of φ⁺, a mixture with all weights positive, whose Bayes sets are coherent under W by Thm 1.1.

---

## 3. Lexicographic combinations

Layers: s^r_i = ∫ψ^r_i with ψ^r_i ∈ L¹ and r = 1,…,m. At world i, compare (s¹_i, …, s^m_i) lexicographically.

**Proposition 3.1 (PROVED).** Suppose each ψ^r_i is weakly sign-respecting (ψ^r_i·g_i ≥ 0) and, for a.e. g, some layer has ψ^r_i(g) ≠ 0. Then each world order is a complete preorder that is independent and world-by-world guided. A guided non-null change raises every layer weakly and some layer strictly.

**Proposition 3.2 (PROVED): pure commission first.** Let ψ¹_i vanish on {g_i > 0} and be negative on {g_i < 0}, for example −w_i(g) g_i⁻, with any later layers. Then:
- V = D_Δ has first layer 0, the maximum, at every world. So it dominates every model with positive commission at every world.
- V itself is undominated. A rival tying V's first layer at a world must lie in the nonnegative orthant, so its omission there is at least V's.
- D_K has zero commission at world i if and only if e_i ∈ K. Hence every undominated coherent model has a vertex in its credal set, and T1 is dominated by V.

A pure omission-first order similarly leaves only the vertex models D_{e_i} among coherent undominated models.

**Proposition 3.3 (PROVED).** Let ψ¹ be strictly sign-respecting. If some Z has s¹_i(Z) > s¹_i(Y) at every i, then Z dominates Y. So an undominated Y has s¹(Y) weakly Pareto-maximal, and (F4) makes Y ψ¹-Bayes at some p. For an interior target D_M the prior p is interior, since a boundary p would put M in a face.

**Theorem 3.4 (PROVED).** Let ψ¹ be strictly sign-respecting with null tie sets N¹_q at every interior q, and assume W. Then:
- (i) every interior B¹_q is undominated, hence almost coherent;
- (ii) for n = 3, every M as in Cor 1.3 is dominated;
- (iii) if ψ¹ is a box field l g⁺ − u g⁻ (0 < l ≤ u), whose ties are null at every p ∈ Δ, the undominated class is exactly the rescaled box family, and W holds.

*Proof.*
- (i) A dominator Z of B¹_q satisfies s¹(Z) ≥ s¹(B¹_q). It is therefore q-Bayes, and uniqueness gives Z = B¹_q a.e.
- (ii) By 3.3, D_M = B¹_{p*}, and ψ¹|_U is a realisation; apply `thm:main`.
- (iii) Undominated models are first-layer Bayes and hence unique, so the class is the box family. For incoherent x, the first-layer strict sections are open and cover supports, as in Prop 1.4. Handoff §4.1 then gives W, with strict first-layer defence at the KKM point. ∎

**3.5 The loophole (CONJECTURE/lead).** Exclusion fails only if the set Q_bad of interior q with non-null N¹_q is nonempty; by 3.4 it must be. By Fubini over q, Q_bad is always Lebesgue-null.
- *What happens at q ∈ Q_bad.* The lexicographic order picks, inside the tie fibre, second-layer Pareto-maximal sets B¹_q ∪ Z. Under W these must be almost coherent. Explicitly, they are sets B ∪ (N ∩ {r·ψ² + η·ψ¹ > 0}), with r ≥ 0 and η a Lagrange multiplier for the fibre constraint.
- *How T1 could appear.* T1 = B¹_{p*} ∪ Z₀ with Z₀ ⊆ N¹_{p*} can then be protected as a second-layer selection that is not a limit of neighbouring Bayes sets.
- *Why `thm:main` is silent.* (BU) fails at the priors in Q_bad, which is exactly the situation of Remark N20.

Whether such a field exists with every Bayes set coherent, and with W holding, is open. That would need a tie fan of gambles whose chart lines all pass through p*, together with coherent second-layer selections. This is the one additive-based route the record does not close, so I recommend that C1 screen it first.

---

## 4. The vacuous model

**4.1 Dependency check (CHECKED).** I read *Three Complete Rankings Cannot Cover* (TCR) §§1–3 on the device, and the local copy of *Complete Rankings for Any Number of Worlds* (CRAN), including `thm:main` and Remark `rem:hyp`(e).

What transfers:
- The arbitrary-set independence implies their (IB′) on regular models.
- On regular models, world-by-world guidance coincides with their strict four-rank (G).

What does not: (S) is used through
- (T1): closedness of the *full* section {p : C_p ⪯_k Y}, combined with completeness, to make Y ≺_k C_p persist near p*. This drives the "complement of Σ is open" step of the no-saturated-cut theorem;
- (T2);
- the face lemma, in particular C_{e_i} = D_i;
- coherent *edge selections* with thresholds (α, β);
- FSE's Theorems 56 and 64 and Corollary 31.

What W gives instead:
- A W-version of (T2) does hold. If x is incoherent and x ≻_w b_{p*}, then p* ∉ A_w(x), so W2 and closedness give b_p ⪰_v x near p* on the open edge.
- (T1) has no W-analogue. A_k(Y) is only a closed subset of the section.
- The b_p need not be coherent, and need not lie in a face.

So the proof does not survive.

**Theorem 4.2 (PROVED).** Let n ≥ 3 and assume (H1) and W. Every coherent D_M whose credal set contains three vertices is dominated; in particular V is.

*Proof.*
1. Suppose D_M is undominated, with e_i, e_j, e_k ∈ M. By Thm 1.1(c), D_M is p⁰-Bayes, and M ⊆ Δ_{supp p⁰} forces p⁰_i, p⁰_j, p⁰_k > 0.
2. Thm 1.1(b) gives coherent B_p with K_p ⊆ Δ_{supp p} for every p. So the hypothesis of the three-world compatibility lemma (v3, `lem:three-world`, which I re-read) holds with D_{K_p} = B_p. Its first part gives ψ_i/(−ψ_j) = F_ij(g_i/(−g_j)) a.e. on {g_i > 0 > g_j}, independently of the other coordinates. Its second part gives sup F_ij = ∞.
3. Now take g with g_i > 0 > g_j and every other coordinate positive. D_M rejects g (since e_j ∈ M), so p⁰·ψ(g) ≤ 0. The terms at the other worlds are positive (k among them), so F_ij < p⁰_j/p⁰_i on a set that is non-null for every ratio interval.
4. Hence F_ij is bounded (F_ij ≤ p⁰_j/p⁰_i), which is a contradiction. ∎

**4.3 (UNCLEAR).** For complete rankings that are not integral, nothing in the record shows that V is dominated under W. The missing tool is a substitute for (T1), that is, openness of the complement of the strict sections.

There is a further gap. Complete independent worlds are comparative probabilities on error sets, but additivity needs fineness. Fineness was derived *from* closed sections (CCF, FSE), and W does not give that derivation. So V, and three-vertex targets in general, still require either incompleteness or a complete non-fine order. Nothing found here forbids V under W for such rankings.

---

## 5. The copy lemma, generalised

Only independence (F5) is used in 5.1–5.3. Reflexivity and guidance enter in 5.4–5.6.

**Proposition 5.1 (PROVED).** Whether Y dominates X depends only on the change (A, R) = (Y∖X, X∖Y): it requires every Y ⪰_i X and the failure of some X ⪰_i Y, and both are functions of the change. Let 𝒟 be the set of *dominating changes*. A change is *available* to Z if R ⊆ Z and A ∩ Z is null. Then:
- X is dominated if and only if some change in 𝒟 is available to X;
- consequently, the undominated models are exactly those to which no change in 𝒟 is available.

*Proof.* If (A, R) ∈ 𝒟 is available to Z, then Z' = (Z∖R) ∪ A differs from Z by exactly (A, R), so Z' dominates Z. The converse is immediate. ∎

**Corollary 5.2 (PROVED): generalised copy lemma.** If T is undominated, then no dominating change is available to T. The audit's lemma is the special case R = ∅, T ⊆ X, A = B∖X.

**Corollary 5.3 (PROVED).** Let T be undominated and let Y dominate X via (A, R).
- If X ⊇ T: A ∩ T = ∅ automatically, so μ(R∖T) > 0. **Every dominator removes a non-null part of the excess X∖T**, and Y ⊉ X. When X is incoherent and Y ⊇ X, this is the audit's contradiction.
- If X ⊆ T: R ⊆ T automatically, so **every dominator re-adds a non-null part of T∖X**.
- If X = (T∖F) ∪ E, with F ⊆ T and E ∩ T = ∅: either μ(R ∩ E) > 0 or μ(A ∩ F) > 0.
- If a whole class 𝒰 is undominated, the change must be unavailable to every member of 𝒰. With 𝒰 = all almost coherent models this is H5's "coherent-availability blocking".

**Lemma 5.4 (PROVED): dominating changes are never anti-guided.** If A ⊆ {g_i < 0} and R ⊆ {g_i > 0}, the change being non-null, then the reverse change is guided at i. So X ≻_i Y, and Y ⪰_i X fails.

*Consequence.* Let E ⊆ {g_i > 0} ∖ T be non-null and bounded, and let X = T ∪ E, which is incoherent by (F3). Every dominator that removes nothing from T must add a non-null set of gambles positive at i (outside T ∪ E). Otherwise, if A ⊆ {g_i < 0} and R ⊆ E ⊆ {g_i > 0}, the change is anti-guided at i. So a pure removal can dominate T ∪ E only if the removed excess is not inside a single half-space {g_i > 0}. In the audit's pair, each ball separately is positive at one world, so only the removal of *both* balls can work as a pure removal. At each world, that removal deletes one correct and one wrong acceptance, so the world order must weigh the wrong acceptance (commission) at least as heavily as the correct one: commission aversion in its minimal form.

**Corollary 5.5 (PROVED, with a CHECKED illustration).** A pure removal of R can be dominating only if no undominated model contains R. If it were dominating, it would be available to that model.

*Box illustration.* Take the box score l = 1, u = ρ, in two worlds. The rescaled boxes K_p = [p₁/(p₁+ρp₂), ρp₁/(ρp₁+p₂)] contain the directions of both ball centres only if ρp₂/2 < p₁ < 2p₂/ρ, which is possible only if ρ < 2.
- For ρ = 3, T = K_u and no undominated box contains both balls.
- Removing both balls raises both box scores. Per unit mass at world 1 the gain is at least 3·0.9 − 2.1 = 0.6, using exchange symmetry. So T dominates X.
- Monte Carlo (4·10⁶ samples) agrees: for ρ = 3 both score changes from the removal are positive. For ρ = 1.5, priors p₁ ∈ (0.455, 0.545) give boxes containing both balls, and the removal lowers both scores.

**Proposition 5.6 (PROVED): assignment-containment test.** This generalises the audit's obstruction to *every* ranking and assignment, with no score consistency needed. Let T be undominated and x ⊇ T incoherent. Suppose every assigned b_p with b_p ⪰_i x at all i satisfies b_p ⊇ x a.e. Then W fails for x.

*Proof.* Suppose W holds. KKM gives p̄ with b_{p̄} weakly dominating x, and W3 makes the domination strict. Two cases:
- b_{p̄} = x a.e.: reflexivity makes them tied at every world, contradicting W3;
- otherwise T ⊆ x ⊊ b_{p̄}, contradicting the copy lemma. ∎

**Corollary 5.7 (PROVED).** If W holds and T is undominated:
- for every bounded non-null E disjoint from T, some assigned b_p weakly dominating T ∪ E has μ(E∖b_p) > 0;
- for every bounded non-null F ⊆ T, some assigned b_p weakly dominating T∖F has μ(F ∩ b_p) > 0.

So if T is not assigned, the assigned family must straddle ∂T at every scale. It must leave out part of every small excess and contain part of every small deficit. With the strict-defence route (Handoff §4.1) the b_p are coherent cones, so each such b_p excludes a whole cone of directions through part of E.

**5.8 Necessary conditions for a ranking in which T1 is undominated and every incoherent model near T1 is dominated.** Gathering §§1–5:
- **(N1)** The world orders are not complete integral orders (Cor 1.3).
- **(N2)** If they are finite intersections of integral judges, T1 is not properly efficient, and the field c of every supporting weight has a non-null interior tie set (Thm 2.3).
- **(N3)** If they are lexicographic with a strictly guided first layer, that layer has non-null ties at some interior prior (Thm 3.4).
- **(N4)** Dominating changes for T1 ∪ E remove part of E. They are anti-guided nowhere. When E lies in one half-space {g_i > 0}, they add gambles positive at i or remove gambles of T1 negative at i. And they are unavailable to every undominated model (5.3–5.5).
- **(N5)** The common assignment passes the containment test (5.6) and straddles ∂T1 (5.7).
- **(N6)** No whole-model test may decide verdicts: v3 Prop. 1 and round 82 apply unchanged. By 5.1, a valid rule can be written as a set 𝒟 of changes, plus the per-world acceptance sets V(A, R) ⊆ Ω from which the ordering conditions must be checked.

---

## 6. Hand-off to C1 (nearby reachable results)

1. **The tie-fan loophole (§3.5, §2.5).** This is the only additive-based route that the record does not close. Build a strictly guided first-layer field with a non-null indifference set at the target prior p*: a fan of gambles whose chart lines pass through p*. Resolve the fan by a commission-averse second layer. Test this first on the audit pair, where it is not needed but must not break, and then on T1.
2. **Approximate coverage.** If only approximate coverage is wanted, complete additive rankings under W reach exactly the coherent-Bayes families (Prop 1.4). Per H3, these include polygons arbitrarily close to T1.
3. **Genuinely non-additive or incomplete rules.** These must satisfy (N4)–(N6).
