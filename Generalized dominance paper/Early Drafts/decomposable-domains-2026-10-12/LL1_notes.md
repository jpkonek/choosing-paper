# LL1 (round 40, BRIEF32). Quorum rankings: a mirror swap defeats every margin quorum, so the class satisfies (S) for no selection at all

18 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact rational computation, with a stated script in `ll1py/`.
- **NUMERICS**: none used.
- **CONJECTURE**.

Scripts: `ll1py/swap_check.py` → `swap_check.out`, `ll1py/tc_eta0.py` → `tc_eta0.out`. Run `python3 -I <script>.py` from inside `ll1py/`. All arithmetic is in Fractions. No assumption is added. Every extra hypothesis is a hypothesis of a stated result.

---

## 0. Outcome

**No cover exists in this class. The obstruction is complete, PROVED, and stronger than the brief anticipated.** No quorum ranking in the class satisfies (S) on the full domain with any selection whatever, continuous or not. This holds for every n, every q with 2q > n (or weighted quorums whose accepting coalitions pairwise intersect), every margin η ∈ (0,1) (it may depend on the world and on the judge), and every family of integrable, strictly guiding judges. So the class covers neither T1 nor any other coherent model.

1. **The mirror swap (Lemma 2.1; PROVED).** Take a selected model C, a point where its advice changes from a to b, and two small sets on either side of the change on which every judge's penalty difference ℓ(·,b) − ℓ(·,a) is nearly the same vector y. Swap the advice on these sets: a → b on one side and b → a on the other, with equal masses.
   - Every judge at every world sees the two changes cancel to first order. Its loss changes by o(size), while its d grows like 2·size·|y_iv|.
   - So **every** judge fails its margin test, at **every** world. C is comparable to the swapped model at no world, so it is not competitive on any set of worlds.
   - Heterogeneity of the judges cannot help. Each judge sees its own exact cancellation, because both swapped problems are the same problem type for that judge.
   - In the brief's language: the swap's (improvement, worsening) vector lies in the **intersection** of all C(n, n−q+1)^3 open failure regions, not merely in one of them (§5).
2. **Competitive models are totally disconnected (Theorem 3.1; PROVED).** Write Λ(f) for the vector of all judges' penalty differences on problem f. A model that is competitive on some nonempty set of worlds must be a locally constant function of Λ(f), off a null set. The set of such models, with the metric of convergence in measure, has no connected subset with more than one point.
   - Hence a selection that is continuous in measure and competitive at every index is **constant** (Corollary 3.2).
   - A constant selection cannot be competitive at two vertices, because C_{e_i} must be the world-i-perfect model.
3. **Closed sections force continuity (Lemma 4.1; PROVED).** If the sections are closed and the selected models are competitive, the selection has a closed graph in the measure topology. This uses 2q > n and integrable envelopes.
   - Coherent models form a compact set in measure, so the selection is continuous.
   - With item 2, this gives **Theorem 4.2: no ranking in the class satisfies (S)**.
   - The theorem uses neither (IB), nor (TC), nor 3q > 2n, nor anything about T1 or ε.
4. **Exact illustration (CHECKED, `swap_check.out`).** Twelve heterogeneous, continuous, strictly guiding judges, η = 1/16. At boundary points of T1 and of two posterior models near u (one is FF2's index (167/500, 333/1000, 333/1000)), the point-evaluation swap has max_{iv} Δ_iv/d_iv ≈ 1.5·10⁻¹·s at offset s. All 12 judges fail for every offset s = 10⁻¹, …, 10⁻⁸.
5. **The nearby classes (§6).** Each natural relaxation fails one of the round's own requirements.
   - **η = 0, q < n:** (TC) fails. An exact example with n = 4, q = 3 is given (Proposition 6.1; PROVED, CHECKED `tc_eta0.out`).
   - **η = 0, q = n:** this is unanimity. Each judge then endorses every accepted comparison, so FF2 Cor 4.3 excludes it for continuous selections (imported status).
   - **Relative margins** (judge v supports iff Δ_v ≥ η·max_{v′}|Δ_{v′}|) are the **reachable nearby class**. They escape the swap. They keep reflexivity, (IB), (TC) for 3q > 2n, and closed sections. They keep strict (G) when the judges' stakes are within a factor κ of each other and η ≤ 1/κ. Their ties are exactly the world-neutral records (Proposition 6.2; PROVED).
   - In that class, competitiveness at p is **equivalent** to finitely many pointwise weak-Bayes conditions for guiding "virtual fields" (Proposition 6.3; PROVED). No single field is involved, so FF2 Thm 4.1 does not bind it as stated.
   - Direct (C) and admissibility are no longer automatic.
6. **Cycles.** No construction was produced, so there are no strict cycles of length ≥ 4 to report.

**Single most important open point.** In the relative-margin committee class, can heterogeneous judges and a continuous coherent selection through T1 satisfy, at every p, the finitely many virtual weak-Bayes conditions of Proposition 6.3? The selection must also make C_p strictly pointwise Bayes for some positive combination of all judges, which is the sufficient condition for (C) in Proposition 6.4. That combination may depend on p. This is the brief's quorum mechanism with the one feature removed that the mirror swap shows is fatal: a margin proportional to the gross change d.

---

## 1. Setting

Everything is as in the write-up §2, BRIEF32 and AUDIT_quorum.

- **Domain and advice.** We work on the full four-advice domain, with three worlds and the Gaussian μ, which is finite and non-atomic. Pairs are indexed by f ∈ H = {f_1 > 0}. The advice a_X(f) is one of + (accept f only), 0 (silence), − (accept −f only) and × (both). At world i the ranks are good < silence < bad < contradiction.
- **Judges.** At each world i there are judges v = 1, …, n with measurable penalties ℓ_iv(f, a). Each is strictly increasing in world-i rank for a.e. f, so all four values are distinct. Each has an integrable envelope.
  - L_iv(X) = ∫ ℓ_iv(f, a_X(f)) dμ;
  - d_iv(X,Y) = ∫ |ℓ_iv(f, a_Y) − ℓ_iv(f, a_X)| dμ;
  - Δ_iv(X,Y) := L_iv(Y) − L_iv(X).
- **Votes and acceptance.** Judge (i,v) supports X R_i Y iff Δ_iv(X,Y) ≥ η_iv d_iv(X,Y), with η_iv ∈ (0,1). (The brief's η and world-dependent η are special cases.) Each judge has a weight β_iv > 0. Accept X R_i Y iff the supporting weight at world i is at least q_i.
  - **(Q1)** q_i > 0.
  - **(Q2)** Any two accepting coalitions at a world intersect, i.e. 2q_i > Σ_v β_iv. This is the brief's 2q > n.
  - (TC) uses 3q > 2n, but no result below uses it.
- **Competitive.** A model C is competitive on S ⊆ {1,2,3}, S ≠ ∅, if every model X has some i ∈ S with C R_i X. Competitiveness against X = C is automatic.
- **(S).** This requires a map p ↦ C_p from Δ to coherent undominated models such that:
  - C_p is competitive on supp p;
  - {p : C_p R_i X} is closed for every world i and every model X.
- **Measure metric.** ϱ(X,Y) := μ{f ∈ H : a_X(f) ≠ a_Y(f)}.

For f ∈ H and advices a ≠ b put δ^{ab}(f) := (ℓ_iv(f,b) − ℓ_iv(f,a))_{i,v} ∈ ℝ^{3n}. By strict guidance, every entry is nonzero for a.e. f. Put

  Λ(f) := (ℓ_iv(f,a) − ℓ_iv(f,0))_{i,v; a ∈ {+,−,×}} ∈ ℝ^{9n},

and let Y** be the open set of vectors in ℝ^{9n} for which every entry of every pairwise difference y_b − y_a (a ≠ b, with y_0 := 0) is nonzero. Then δ^{ab} = Λ_b − Λ_a, and Λ(f) ∈ Y** for a.e. f.

For a measurable E and a measurable map Φ, the **essential range** R(Φ|E) is the set of y such that μ(E ∩ Φ^{-1}(B(y,r))) > 0 for every r > 0. It is closed, and Φ(f) ∈ R(Φ|E) for a.e. f ∈ E.

---

## 2. The mirror swap

**Lemma 2.1 (PROVED).** Let C be any model, let a ≠ b be advices, and put A := {f : a_C(f) = a} and B := {f : a_C(f) = b}. Suppose some y ∈ R(δ^{ab}|A) ∩ R(δ^{ab}|B) has all entries nonzero. Then there is a model X ≠ C such that, for every judge (i,v) at every world,

  Δ_iv(C, X) < η_iv d_iv(C, X).

So no judge supports C R_i X at any world. By (Q1), C R_i X fails at every world, and C is competitive on no nonempty set of worlds.

*Proof.*
1. **Choice of r.** Let η_* := min η_iv > 0 and y_* := min |y_iv| > 0. Choose 0 < r < η_* y_* / (1 + η_*).
2. **The two sets.** The sets A′ := A ∩ (δ^{ab})^{-1}(B(y,r)) and B′ := B ∩ (δ^{ab})^{-1}(B(y,r)), with max-norm balls, have positive measure. Since μ is non-atomic, pick E_A ⊆ A′ and E_B ⊆ B′ with μ(E_A) = μ(E_B) = m > 0. They are disjoint, because A ∩ B = ∅.
3. **The model.** Let X agree with C except that it gives advice b on E_A and a on E_B. Then X ≠ C, since ϱ(C,X) = 2m.
4. **Increments.** For each judge, the change on E_A is δ^{ab}_iv and the change on E_B is −δ^{ab}_iv. These are bounded there, so all integrals below are finite. Hence
   - Δ_iv(C,X) = ∫_{E_A} δ^{ab}_iv − ∫_{E_B} δ^{ab}_iv, and |Δ_iv(C,X)| < 2rm;
   - d_iv(C,X) = ∫_{E_A} |δ^{ab}_iv| + ∫_{E_B} |δ^{ab}_iv| > 2m(|y_iv| − r).

   The inequalities are strict because they hold strictly pointwise on sets of positive measure.
5. **Every judge fails.** By the choice of r, 2rm ≤ η_iv · 2m(|y_iv| − r). So Δ_iv(C,X) < η_iv d_iv(C,X). ∎

*Remarks.*
- **Same sign pattern.** If y is a common essential value, each world's entries of y have one sign. So the two swapped problem families have the same world-sign pattern, and the two changes have opposite signs at every world, judge by judge. Across a coordinate plane, by contrast, the world-i entries of δ^{ab} flip sign, and no common value with nonzero entries exists. This is why world-perfect models, such as C_{e_i}, are immune.
- **Dual form.** Fix a failing choice F and a dual weight w ≥ 0 supported on F (§5). The pointwise condition at the two sides reads Σ w(y − η|y|) ≥ 0 and Σ w(−y − η|y|) ≥ 0. Their sum is −2η Σ w|y| < 0. So no dual weight exists for any F, whatever the judges.
- **Exact illustration (CHECKED, `swap_check.py` → `swap_check.out`).**
  - The judges are four per world, with penalties ρ_iv(f)(r + r²/5), where r is the world-i rank and ρ_iv are four different positive rational functions of f.
  - At a relative-interior point h0 of a facet of C_p, for p = u, p = (167/500, 333/1000, 333/1000) and p = (2/5, 7/20, 1/4), the points h0 ± s·n (n the facet normal) lie on the accept and silence sides.
  - The point-evaluation swap gives max_{iv} Δ_iv/d_iv = 1.48·10⁻¹·s, 1.48·10⁻¹·s and 1.70·10⁻¹·s respectively. All 12 judges fail at η = 1/16 for every s ∈ {10⁻¹, …, 10⁻⁸}.
  - The script also checks that the 24 penalty differences at each pair of points are nonzero and have matching signs.
  - This is the integrand behind the lemma. The lemma itself is proved for genuine sets of positive measure.

---

## 3. Competitive models form a totally disconnected set

Let 𝒦 be the set of models (mod null sets) that are competitive on some nonempty set of worlds. Put G := R(Λ) ∩ Y**. It is locally compact, separable and σ-compact: G ∩ {|y| ≤ m, all relevant entries of magnitude ≥ 1/m} is compact. Moreover Λ^{-1}(G) is co-null.

**Theorem 3.1 (PROVED).**
- (a) For each C ∈ 𝒦 there is a locally constant function c : G → {+, 0, −, ×} with a_C = c ∘ Λ a.e.
- (b) Every connected subset of (𝒦, ϱ) is a single point.

*Proof.*
- **(a) Local constancy near each value.** Fix y ∈ G. Suppose that for every r > 0 two different advices both occur on non-null subsets of Λ^{-1}(B(y,r)). There are finitely many pairs of advices, so a single pair (a,b) occurs for all r. Then y ∈ R(Λ|A) ∩ R(Λ|B), where A, B are C's a- and b-regions. Since δ^{ab} = Λ_b − Λ_a is 2-Lipschitz in max norm, y^{ab} := y_b − y_a lies in R(δ^{ab}|A) ∩ R(δ^{ab}|B), and its entries are nonzero because y ∈ Y**. Lemma 2.1 then contradicts C ∈ 𝒦.
- **(a) Definition of c.** So there is r_y > 0 such that a_C is a.e. constant on Λ^{-1}(B(y, r_y)). This set has positive measure because y ∈ R(Λ). Let c(y) be that constant.
- **(a) c is locally constant.** If y′ ∈ G ∩ B(y, r_y/2), then Λ^{-1}(B(y′, r)) ⊆ Λ^{-1}(B(y, r_y)) for r ≤ r_y/2, and the smaller set is non-null. So c(y′) = c(y).
- **(a) a_C = c ∘ Λ.** G is Lindelöf, so countably many balls B(y_k, r_{y_k}) cover it. On each preimage a_C = c(y_k) = c ∘ Λ a.e. The union of the preimages is co-null.
- **(b) Countably many patterns on each compact.** Let Γ ⊆ 𝒦 be connected and let K ⊆ G be compact. For C ∈ Γ, the restriction c_C|_K is locally constant, so each of its four level sets is clopen in K.
  - A clopen subset of a compact metrizable space is a finite union of members of a fixed countable base. So K has countably many clopen subsets.
  - Hence c_C|_K lies in a countable set S_K.
- **(b) The patterns move continuously.** Put ν := Λ_*μ and d_K(c, c′) := ν(K ∩ {c ≠ c′}). Then d_K(c_C|_K, c_D|_K) ≤ ϱ(C, D). So C ↦ c_C|_K is continuous from Γ into the countable pseudometric space (S_K, d_K).
- **(b) The image is a point.** A countable pseudometric space has no connected subset of positive diameter. If d(x,x′) = D > 0, choose t ∈ (0, D) that is not a distance from x; then {z : d(x,z) < t} is clopen and separates x from x′. So all members of Γ agree a.e. on Λ^{-1}(K).
- **(b) Conclusion.** Exhaust G by countably many compacts. Then all members of Γ agree a.e. ∎

**Corollary 3.2 (PROVED).** Let P ⊆ Δ be connected, and let p ↦ C_p be continuous in measure on P with each C_p competitive on supp p. Then C_p is constant on P. In particular:
- (a) no selection continuous in measure on Δ is competitive at every index;
- (b) no path continuous in measure joins two different competitive models through competitive models.

*Proof.* The image of P is a connected subset of 𝒦, so it is a point by Theorem 3.1(b).
- (a) A constant selection would have C_{e_1} = C_{e_2}.
- At p = e_i, competitiveness on {i} forbids every world-i improvement. A world-i improvement X has Δ_iv(C,X) = −d_iv(C,X) < 0 for every judge, so no judge supports C R_i X.
- So C_{e_i} must be the world-i-perfect model: + on {f_i > 0} and − on {f_i < 0}, within H.
- The models for i = 1 and i = 2 differ on {f_1 > 0 > f_2}, which is non-null. ∎

*Remark (decomposable domains; PROVED).*
- **Rigidity.** On a decomposable domain with advice range A(f), append to Λ(f) the label A(f), one of 15 finite values. Then perform swaps only between problems with equal labels. Both advices used in a swap then lie in A(f) at both locations, and Lemma 2.1, Theorem 3.1 and Corollary 3.2 go through verbatim.
- **Vertices.** If (LF) holds at T1, a constant C must give, on a non-null set of mixed f near ∂D_{T1}, advice that is optimal at every world among {accept f, silence}. For mixed f no such advice exists. So Corollary 3.2(a) holds on every decomposable domain with (LF) at T1.
- **Scope.** Lemma 4.1 below is stated for the full domain only.

---

## 4. Closed sections force continuity; no ranking in the class satisfies (S)

**Lemma 4.1 (PROVED).** Assume (Q1), (Q2) and integrable envelopes. Let p ↦ C_p have closed sections, with each C_p competitive on supp p. Suppose p_k → p and C_{p_k} → C* in measure, where C* is a model that gives no contradictory advice on a non-null set. Then C* = C_p.

*Proof.*
1. **Continuity in measure.** Integrable envelopes make L_iv and d_iv(·,·) continuous in measure, by absolute continuity of the integral.
2. **C_p R_i C* at every world i.** Fix i. For a non-null E on which C* gives no ×, let X_E be C* with × on E.
   - Every world-i judge then has Δ_iv(C*, X_E) = d_iv(C*, X_E) > 0. By step 1, Δ_iv(C_{p_k}, X_E) − η_iv d_iv(C_{p_k}, X_E) → (1 − η_iv) d_iv(C*, X_E) > 0.
   - So for large k every world-i judge supports C_{p_k} R_i X_E, and p_k lies in the section {q : C_q R_i X_E}.
   - The section is closed, so C_p R_i X_E.
   - Let μ(E_m) → 0. Finitely many coalitions occur, so one accepting coalition J_i occurs infinitely often. Pass to the limit X_{E_m} → C*: every v ∈ J_i has Δ_iv(C_p, C*) ≥ η_iv d_iv(C_p, C*).
3. **C* R_i C_p at some world.** Competitiveness of C_{p_k} against X = C_p gives i_k ∈ supp p_k and an accepting coalition J′_k with Δ_iv(C_{p_k}, C_p) ≥ η_iv d_iv(C_{p_k}, C_p). Pass to a subsequence with constant (i, J′) and take limits: every v ∈ J′ has Δ_iv(C*, C_p) ≥ η_iv d_iv(C*, C_p).
4. **Conclusion.** By (Q2), some v ∈ J_i ∩ J′. Adding its two inequalities, with Δ(C*, C_p) = −Δ(C_p, C*) and d symmetric, gives 0 ≥ 2η_iv d_iv(C_p, C*). So d_iv(C_p, C*) = 0. Strict guidance makes |ℓ_iv(f, a) − ℓ_iv(f, b)| > 0 a.e. wherever a ≠ b, so C* = C_p a.e. ∎

**Lemma 4.2a (PROVED).** The coherent models form a compact subset of (models, ϱ).

*Proof.*
- The credal sets are compact in the Hausdorff metric (Blaschke).
- If K_k → K, then P_{K_k}(g) → P_K(g) for every g, since |P_K(g) − P_{K′}(g)| ≤ |g|·d_H(K, K′).
- So 1_{D_{K_k}}(±g) → 1_{D_K}(±g) off {P_K(g) = 0} ∪ {P_K(−g) = 0}.
- That set is null. If P_K(g) = 0 at a point g in the interior of the convex cone {P_K ≥ 0}, then concavity along the segment through g from 𝟙 (where P_K = 1) gives P_K(g) > 0. So {P_K = 0} ⊆ ∂{P_K ≥ 0}, which is null.
- By dominated convergence, K ↦ D_K is continuous in measure. The image of a compact set is compact, and every coherent model is some D_K. ∎

**Theorem 4.2 (PROVED).** On the full domain, no quorum ranking satisfying (Q1), (Q2) and integrable envelopes, with strictly guiding judges and margins η_iv ∈ (0,1), has a map p ↦ C_p into coherent models with closed sections and C_p competitive on supp p. In particular no such ranking satisfies (S). It covers neither T1 nor any coherent model.

*Proof.*
- **Closed graph.** Suppose p_k → p and C_{p_k} → C* in measure. By Lemma 4.2a, C* is coherent, so it gives no ×. Lemma 4.1 gives C* = C_p. So the graph is closed in Δ × 𝒞, where 𝒞 is compact.
- **Continuity.** A map into a compact metric space with closed graph is continuous.
- **Contradiction.** Corollary 3.2(a) then gives a contradiction. ∎

**What is and is not used.**
- **Used:**
  - non-atomicity and finiteness of μ;
  - strict guidance of every judge;
  - η_iv > 0;
  - competitiveness;
  - for Lemma 4.1: closed sections, (Q2) and integrable envelopes;
  - coherence, for compactness.
- **Not used:** (IB), (TC), 3q > 2n, admissibility, (C), (LF), anything about T1 or ε, and transitivity of any kind.
- **Barriers compared.** The obstruction is unrelated to FF2 Thm 4.1, which concerns endorsement by a single field. It concerns comparability: a positive margin makes the near-neutral records at the boundary of a moving coherent model comparable at no world. The audit's five-cycle certificate and its proofs of (G), (IB), (TC), no ties and closed sections all stand. They are simply never reached.

---

## 5. Relation to the brief's method

**Lemma 5.1 (exact reduction at a fixed p; PROVED).** Write z(X) := (Δ_iv(C_p, X), d_iv(C_p, X))_{i ∈ supp p, v}. For a choice F of failing coalitions (F_i with weight > Σ_v β_iv − q_i at each i ∈ supp p), let

  O_F := {z : Δ_iv − η_iv d_iv < 0 for all v ∈ F_i, i ∈ supp p}.

Then C_p is competitive on supp p iff, for every F, there is w ≥ 0, w ≠ 0, supported on F, with

  Σ_{(i,v) ∈ F} w_iv [δ_iv − η_iv |δ_iv|] ≥ 0,  δ := ℓ(f,b) − ℓ(f, a_{C_p}(f)),

for a.e. f and every advice b.

*Proof.*
- **Convexity.** The attainable set Z = {z(X)} is the Aumann integral of a finite-valued integrable correspondence over a non-atomic finite measure. So it is convex (Lyapunov; Aumann 1965).
- **Separation.** Competitiveness fails iff Z meets some O_F. O_F is a nonempty open convex cone: z with Δ = −1, d = 1 lies in it. So Z ∩ O_F = ∅ iff some nonzero y separates them. Polarity of the closed cone {Δ − ηd ≤ 0 on F} puts y in the cone of the defining functionals.
- **Pointwise form.** Switching to b on small sets turns the integral inequality into the pointwise one, and conversely. ∎

This is the brief's "convex attainable set avoids C(n, n−q+1)^3 open regions". Lemma 2.1 exhibits, for every moving coherent model, attainable points in **all** the regions at once. Equivalently, by the dual remark after Lemma 2.1, no dual weight exists for any F. The brief's hope was that the adversary must combine **different** sign types, so that heterogeneous judges cannot all see cancellation. But the swap uses **one** sign type on both sides of a single boundary, and so cancels for every judge separately.

---

## 6. The nearby classes

### 6.1 Margin zero

Take η = 0: judge v supports X R_i Y iff L_iv(X) ≤ L_iv(Y).
- Lemma 2.1 fails, because the swap's tiny increments now decide by their signs.
- Lemma 5.1 holds with η = 0. C_p is competitive iff, for every F, C_p is a pointwise weak Bayes model of the virtual field (ℓ_iv)_{(i,v) ∈ F} at some nonzero weight w ≥ 0 on F.

**Proposition 6.1 (PROVED; CHECKED `tc_eta0.out`).** Take η = 0, n = 4 and q = 3. Then (TC) can fail.

*Proof.*
- **The models.** Take three disjoint non-null cells on which accepting is good at world i, and a base model B accepting on all three. Let X, Y, Z be B made silent on the first, second and third cell respectively.
- **The masses.** Choose the judges' densities so that the masses m_v(c) = ∫_c (ℓ_v(0) − ℓ_v(+)) are (1,1,1), (1,2,3), (3,1,2) and (2,3,1). Any positive masses are attainable by strictly guiding judges: scale each judge's density on each cell.
- **Votes.** Then L_v(A) − L_v(B) = m_v(c_A) − m_v(c_B), and:
  - X R Y has votes {1,2,4};
  - Y R Z has votes {1,2,3};
  - Z R X has votes {1,3,4};
  - X R Z has only {1,2}.
- So X R Y, Y R Z and Z strictly R X: this is a Condorcet profile with one indifferent judge. ∎

At η = 1/16 the same profile accepts none of these edges, as the audit's counting argument requires (same output file). The counting argument needs every judge's support to be strict on non-identity records. At η = 0 a three-way-tied judge supports all three edges, and the count gives only 3q ≤ 2n + (q − 1), which permits a violation whenever q < n.

For q = n (unanimity), every accepted comparison at world i is endorsed by judge 1's field. So FF2 Cor 4.3 (PROVED modulo its import chain; GG3 repair) excludes covers with selections continuous in measure.

### 6.2 Relative margins: the reachable nearby class

For world i put M_i(X,Y) := max_v |Δ_iv(X,Y)|. Judge (i,v) supports X R_i Y iff

  Δ_iv(X,Y) ≥ η M_i(X,Y),  0 < η < 1;

accept with at least q votes. Here 2q > n is required for the stated tie property and 3q > 2n for (TC). Hypothesis **(H_κ)**: |ℓ_iv(f,b) − ℓ_iv(f,a)| ≥ κ^{-1} |ℓ_iv′(f,b) − ℓ_iv′(f,a)| for all v, v′, a, b and a.e. f.

**Proposition 6.2 (PROVED).**
- (a) The relation is reflexive and satisfies (IB).
- (b) Under (H_κ) with η ≤ 1/κ, strict (G) holds.
- (c) With 2q > n, X R_i Y and Y R_i X hold iff the record is **world-i-neutral**: Δ_iv(X,Y) = 0 for every v.
- (d) With 3q > 2n, (TC) holds.
- (e) For a selection continuous in measure, all sections are closed.
- (f) Lemma 2.1 does not apply. Every swap is decided by the signs of its increments, because the margin is scale-free in the increments.

*Proof.*
- (a) At the identity every Δ is 0 and M_i = 0. The rule depends only on the record.
- (b) **The improvement is accepted.** For a world-i guidance improvement from Y to X, every judge has Δ_iv(X,Y) = ∫|Δℓ_iv| > 0. By (H_κ), Δ_iv ≥ κ^{-1} Δ_iv′ for all v′, so Δ_iv ≥ ηM_i. All n judges support X R_i Y.
  - **The reverse is rejected.** Every Δ_iv(Y,X) < 0 ≤ ηM_i, so no judge supports Y R_i X.
- (c) A judge in two intersecting coalitions has Δ ≥ ηM_i and −Δ ≥ ηM_i. So M_i = 0. Conversely, if M_i = 0 every judge supports both directions.
- (d) **No judge supports all three edges.** Suppose a judge supports X R Y, Y R Z and Z R X. Its three increments are ≥ 0 and sum to 0, so each is 0. The margins then force M_i = 0 on all three edges. So all world-i judges are neutral on (X,Z), and X R_i Z holds with every vote, so Z ≺_i X is not strict.
  - **Counting.** Hence in a forbidden triangle each judge supports at most two edges. This gives 3q ≤ 2n, a contradiction.
- (e) The functions p ↦ Δ_iv(C_p, X) and p ↦ M_i(C_p, X) are continuous. Each vote condition is closed, and the acceptance set is a finite union of finite intersections of closed sets.
- (f) In the swap all Δ_iv and M_i are o(size). The rule compares them with each other, not with the size. ∎

**Proposition 6.3 (PROVED).** Fix p. A failing configuration consists of:
- for each i ∈ supp p, a set F_i of at least n − q + 1 judges;
- for each v ∈ F_i, a witness (v′, σ) with σ ∈ {±1}.

(Δ_iv < ηM_i iff Δ_iv < ησΔ_iv′ for some v′ and σ.) Then C_p is competitive on supp p iff, for every failing configuration, there are λ ≥ 0, not all zero, such that C_p is a pointwise weak Bayes model of the virtual field

  Σ_{i ∈ supp p} Σ_{v ∈ F_i} λ_iv (ℓ_iv − ησ_iv ℓ_{iv′_iv}).

Under (H_κ) with η ≤ 1/κ, each summand is world-i guiding.

*Proof.* As for Lemma 5.1, with O_config := {z ∈ ℝ^{3n} : z_iv − ησ z_iv′ < 0}. It is nonempty (z ≡ −1 works) and lies in the space of increments alone. Convexity of the attainable set, separation and Farkas give the weights. The pointwise form follows by switching on small sets. ∎

**Proposition 6.4 (PROVED).** In the relative-margin class, every model tied with C_p at all three worlds equals C_p, so direct (C) holds at C_p, if C_p is the strict pointwise Bayes model of some strictly positive combination Σ_{i,v} c_iv ℓ_iv. The combination may depend on p.

*Proof.* By Proposition 6.2(c), a tie at all worlds is a record with Δ_iv = 0 for all (i,v). Then Σ c_iv Δ_iv = 0. Strict pointwise Bayes forces a positive value for every non-identity record. ∎

*What remains open in the relative-margin class.* These are CONJECTURE-free statements of the gap.
- **Direct (C).** It is not automatic, since ties exist on world-neutral records. Without a condition like Proposition 6.4, a globally neutral incoherent X would be tied with C_p everywhere.
- **Admissibility.** It is not automatic either. If X dominates C_p, competitiveness yields only a world-neutral tie at one active world.
- **Competitiveness.** It requires the finitely many virtual weak-Bayes conditions of Proposition 6.3 at every p, for one fixed family of judges.
- **Barriers.** FF2 Thm 4.1 needs a single field. Here the endorsing combinations vary with p and with the configuration. Theorem 4.2 does not apply, by Proposition 6.2(f).
- Whether a single field can be extracted, for example a judge belonging to every accepting coalition, is the first thing to test. A single-crossing family of judges (losses on a segment ℓ_v = (1 − s_v)ℓ_A + s_vℓ_B) **would** have such a judge, the median, and so would be excluded by FF2 Cor 4.3. Genuine heterogeneity is necessary.

**CONJECTURE 6.5.** Any ranking whose world-i verdicts are a closed condition on finitely many additive statistics of the record, with no ties except on world-neutral records, has, along any competitive continuous selection, incoherent models tied with selected models at all worlds unless the selected models are strict Bayes models of positive combinations of those statistics' fields, as in Proposition 6.4. If true, Proposition 6.4's condition is the price of every finite-statistic rule, and the open point above is the general one for such rules.

---

## 7. Status table

| Item | Statement | Label |
|---|---|---|
| 2.1 | mirror swap: at a common essential value of δ^{ab} on both sides of C's a/b boundary, every judge at every world fails | PROVED |
| 2.1 illustration | 12 heterogeneous continuous judges, T1 and two posterior models near u, offsets 10⁻¹…10⁻⁸: all 12 fail | CHECKED (`swap_check.out`) |
| 3.1 | competitive models are locally constant functions of Λ; (𝒦, ϱ) is totally disconnected | PROVED |
| 3.2 | a selection continuous in measure and competitive on Δ is constant, hence impossible; also on decomposable domains with (LF) at T1 | PROVED |
| 4.1 | closed sections + competitiveness + (Q2) + integrable ⇒ closed graph in measure | PROVED |
| 4.2a | coherent models compact in measure | PROVED |
| 4.2 | no quorum ranking (any n, q with 2q > n, any η_iv ∈ (0,1), weighted) satisfies (S) on the full domain; no cover of T1 | PROVED |
| 5.1 | exact dual reduction of competitiveness at fixed p | PROVED |
| 6.1 | η = 0, n = 4, q = 3 violates (TC) | PROVED; CHECKED (`tc_eta0.out`) |
| 6.1 remark | η = 0, q = n excluded for continuous selections | FF2 Cor 4.3 (import chain; refereed in GG3) |
| 6.2 | relative-margin committees: reflexive, (IB), strict (G) under (H_κ), ties = world-neutral, (TC), closed sections; swap does not apply | PROVED |
| 6.3 | competitiveness ⟺ finitely many virtual weak-Bayes conditions | PROVED |
| 6.4 | strict Bayes for a positive combination ⇒ direct (C) at C_p | PROVED |
| 6.5 | finite-statistic rules need 6.4's condition | CONJECTURE |
| — | T1 cover by quorum rankings | **impossible** (Thm 4.2) |
| — | strict cycles of length ≥ 4 | none (no construction) |

## 8. Files (`ll1py/`)

- `swap_check.py` → `swap_check.out`: exact point-evaluation swaps at facet points of T1 and of C_p for p = (167/500, 333/1000, 333/1000) and (2/5, 7/20, 1/4), with twelve heterogeneous judges and η = 1/16. It checks the sign patterns and that all 12 judges fail.
- `tc_eta0.py` → `tc_eta0.out`: the Condorcet-plus-indifferent profile. It shows three (TC) violations at η = 0 and none at η = 1/16.
