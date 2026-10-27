# IN63 — Incomplete branch: finite-view unanimity rankings aimed at the reversed triangle (25 Oct 2026)

Labels: **PROVED** (proof written here, not yet refereed) / **CHECKED** (exact rational or symbolic computation) / **CONJECTURE** / **NUMERICS**. Scripts are in `in63py/`, each with a `.out` file. Binding inputs: `AUDIT_r63_decisions.md` (the corrected incomplete-order task, and the counterexample showing that strictly sign-correct views can have non-null weighted ties) and `AUDIT_r62_composition.md` §2.

Target throughout: K = {m ∈ Δ₃ : m_i ≤ 2/5}, with vertices v₁ = (1,2,2)/5 and its permutations.
- D_K = {h : v_k·h > 0 for every k}.
- Its rays are r_j = 2·𝟙 − 5e_j.
- Its faces are F_k = cone(r_i, r_j).
- In the cross-section Σh = 1, D_K is the triangle T = {h_k < 2}, and face F_k is the line h_k = 2.

---

## 0. Summary in plain English

**What was asked.** Build a small unanimity ranking, with finitely many integrated views at each world, that is aimed at the reversed triangle. Prove that undominated weak dominators exist by compactness. Locate a supporting face that contains the target, and say which view weights vanish on it. Show how the views that get zero weight remove the incoherent minimisers on that face. Then check the entire efficient set.

**What I did.**

1. **A general toolkit for finite-view unanimity rankings (PROVED, §§2–3).**
   - *Existence.* Undominated weak dominators exist by compactness (§2).
   - *Strictly positive weights.* A minimiser for weights that are strictly positive on every view is always efficient. So any non-null tie at such weights produces an incoherent efficient model (the slab lemma, E2).
   - *Free-sign lemma (E3).* On a supporting face with weight λ¹, the further selections inside the tie region use weights that must be positive on the views omitted by λ¹. On the views that λ¹ uses, however, they may take **either sign**. This is the precise way in which "omitted views eliminate incoherent minimisers": they can only do so if the used views stay harmless under weights of either sign.
   - *Rank-deficiency lemma (E4).* If, on a non-null set, the field takes values in a subspace that contains no nonzero non-negative vector, then that set is tied at some strictly positive weight. That is fatal.

2. **Concave views are dead, whatever the faces (Theorem C, PROVED, §4).** This covers any finite number of unanimity views at each world, of two kinds:
   - single-level views with concave, positively homogeneous, merely *weakly* sign-correct gains;
   - two-level lexicographic views, consisting of a convex veto (paid by the target or not) followed by such a gain.

   For every such ranking, either some undominated model is incoherent or the reversed triangle is dominated. Non-null ties, supporting faces on the boundary of the weight simplex, and omitted views do not help. This strengthens E61 Cor 5.2, which needed strictly sign-correct second levels. In particular, the audit's "paid vetoes" candidate is excluded whenever the vetoes are convex and the second levels concave.

3. **Two further quick exclusions (PROVED, §5).**
   - Any number of orthant-diagonal views (the composition-theorem charts) never makes the reversed triangle efficient.
   - Fields with a constant direction on some region of a mixed orthant are impossible for every target.

4. **One-level resolution reduces to the refereed corner-seam theorem (Theorem S, PROVED given C62 Thm 4.1, §6).** Suppose the views are continuous and piecewise linear, and the target's whole boundary is settled at a single level of the lexicographic face chain, with full freedom at that level. Then the views aggregate into a three-world chart that meets C62's hypotheses, so it fails.

5. **The one genuine escape I found, and how far it goes (§7).**
   - *The escape.* Settle the three corners **one level later than the faces.* Small corner "caps" are tied at the first level. The C62 corner-seam system then disappears: it is replaced by a direction-matching condition at the six cut points, and that condition **has real positive solutions** (CHECKED). An exact one: cut at p = 1/4, crossing coefficients all equal to 1, cap direction κ = (1,1,−2).
   - *What it forces.* The used views must be rank-one on each cap (PROVED). A **rotation lemma** (PROVED) then forces those views to enter each face parallel to κ. Under face linearity this makes them vanish on the faces, which is the pinned branch.
   - *Status.* That the cap mechanism is excluded for continuous piecewise-linear fields is a CONJECTURE with a proof outline. The open steps are named.

6. **An explicit six-view system that runs every step of the corrected task (§8, CHECKED).**
   - Each world has two views:
     - A_j, a "cap" chart: E61's lower-prevision chart away from the caps, and the direction κ^(k) times Σh on cap k;
     - B_j, Brier, regraded by depth on the caps.
   - (1) Compactness gives undominated weak dominators.
   - (2) The target lies on the face with weights λ¹ = (1,1,1 | 0,0,0). The Brier weights vanish there, and the tie region is exactly the three caps.
   - (3) The omitted Brier views reduce the face's minimisers to strips parallel to the cuts. All of these are coherent, and the target is the unique lexicographic maximiser.
   - (4) **But the entire efficient set contains incoherent models.** Two exact witnesses are given, both at strictly positive weights:
     - E61's lower-prevision failure, at (1,2,3 | ε,ε,ε);
     - the rotation failure at a cut point, at (11/10, 9/10, 1 | ε,ε,ε).
   - (5) A variant with plain Brier views on the caps also fails on the target's own face, through the free-sign lemma (exact witness).

**Bottom line.**
- No cover was found.
- Every finite-view design I could formulate fails, and each failure is a theorem or an exact witness.
- Three escapes are not excluded:
  - fields that are not piecewise linear, or are discontinuous near ∂D_K;
  - face-resolution patterns other than "everything at one level" and "corner caps at the second level" (for example, tie regions reaching outside D_K);
  - non-additive or non-view orders.

### Status table

| Item | Status |
|---|---|
| §2 Undominated weak dominators (single-level views; lexicographic views via VB Step 1) | PROVED |
| E1 Strictly positive-weight maximisers are efficient; admissible lexicographic maximisers are efficient | PROVED |
| E2 Slab lemma: a non-null tie at strictly positive weights gives an incoherent efficient model | PROVED |
| E3 Free-sign lemma (nested faces: used coordinates free, omitted ones strictly positive) | PROVED |
| E4 Rank-deficiency lemma (Gordan) | PROVED |
| E5 Efficient set invariant under c ↦ s(h)c, s > 0 (for admissible lexicographic maximisers; in full, given the lexicographic separation theorem) | PROVED / PROVED given cited theorem |
| E6 Almost-everywhere limits of coherent cones are coherent | PROVED |
| **Thm C: concave single-level views, and convex-veto/concave two-level lexicographic views, at any faces, ties and paid vetoes, cannot cover K** | **PROVED** (uses refereed E61 Lemma 3.4) |
| Prop 5.1: orthant-diagonal views (any number, any faces) never make D_K efficient | PROVED |
| Cor 5.2: piecewise-constant direction fields impossible for every target; rank-one caps impossible | PROVED |
| **Thm S: continuous piecewise-linear views with one-level resolution cannot cover K** | **PROVED given C62 Thm 4.1** (refereed CORRECT after repair) |
| §7.2 Cut-point direction system has real positive solutions (symmetric family p ∈ [1/4, 2/3); exact point p = 1/4, x = 1) | CHECKED (sympy); non-symmetric: NUMERICS |
| §7.3 Forced local cap structure (used views rank-one on caps; omitted views lowered) | PROVED (local, hypotheses K1–K4) |
| §7.4 Rotation lemma | PROVED (rank-one case) |
| §7.5 Consequence: used views vanish on face middles (given face linearity) | PROVED |
| §7.5 The whole cap mechanism is excluded for continuous piecewise-linear fields | CONJECTURE (outline; needs the multi-view transfer of REF62 §4(b)) |
| §8 Σ_cap: target efficient on the face λ¹; face selections are strips (coherent) | CHECKED + PROVED |
| §8 Σ_cap: incoherent efficient models at strictly positive weights (two witnesses) | CHECKED (exact) |
| §8 Plain-Brier variant: incoherent efficient model on the target's own face | CHECKED (exact) |
| A cover of the reversed triangle by finite-view rankings | open |

---

## 1. Setting and named hypotheses

**Worlds and domain.**
- There are three worlds.
- The domain is one-sided: U = D_{K'} with K' = (u + K)/2, so U₂ = {h_k < 11/3} in the cross-section. Every result below holds for any open convex one-sided cone U ⊇ cl D_K∖0 with no h ≤ 0.
- Models are measurable X ⊆ U modulo μ-null sets. Here μ is Gaussian, or any absolutely continuous measure with finite first moment.
- The domain is decomposable, and (LF) holds at D_K, because U is open and contains cl D_K∖0.

**Views.**
- World j carries a finite set 𝒱_j of views. The set of all views is 𝒱 = ⊔_j 𝒱_j, with |𝒱| = V, and j(v) denotes the world of view v.
- A single-level view v has an integrable, positively homogeneous gain field c_v : U → ℝ, and z_v(X) := ∫_X c_v dμ (larger is better).
- A two-level lexicographic view has a veto φ_v ≥ 0 that vanishes on {h_{j(v)} > 0}, followed by a gain c_v. It compares (−∫φ_v, ∫c_v) lexicographically.

**Ordering at each world.** X ⪰_j Y iff every view at j weakly prefers X. This is the unanimity order: incomplete and transitive.

**Named hypotheses.**
- **(WS) weak sign-correctness.** c_v ≥ 0 where h_{j(v)} > 0, and c_v ≤ 0 where h_{j(v)} < 0.
- **(SG) strict guidance.** For each j, a.e. on {h_j ≠ 0}, some view at j is nonzero.

  Together these give strict (G). Integrated record comparisons give (IB).

**Dominance.** Weak dominance means weakly better at every view of every world. Domination additionally requires strict improvement at some view. An undominated model is called *efficient*.

**Success criterion (audit).**
- (i) Every efficient model is coherent, meaning a.e. equal to D_Q ∩ U for a credal set Q.
- (ii) D_K is efficient.
- (iii) Strict (G), (IB), (C), (LF).

---

## 2. Existence of undominated weak dominators (PROVED)

**Single-level views.**
- Let Z := {z(X) : X ⊆ U} ⊆ ℝ^V. Each z_v is the integral of an integrable function over X, and μ is non-atomic. By Lyapunov's theorem, Z is compact and convex.
- Weak dominance of X by Y is exactly z(Y) ≥ z(X) coordinatewise. The views serve as proof coordinates only; the physical worlds are not re-indexed.
- Fix X. The set D := {z ∈ Z : z ≥ z(X)} is compact and non-empty. Take z* ∈ argmax_D Σ_v z_v.
- If some z' ∈ Z dominated z*, then z' ∈ D and Σz' > Σz*, a contradiction.
- So any model realising z* is an undominated weak dominator of X. ∎

**Lexicographic views.** Use the 2V coordinates (−∫φ_v, ∫c_v). Weak dominance is the product of the views' lexicographic orders. The chain/Zorn argument of `VB_dominance_note.md` Step 1 applies verbatim: compactness supplies lower bounds for chains, coordinate by coordinate, along tails. This is the audit's AUDIT_r62 §2 remark, made explicit.

---

## 3. Structure of the efficient set (single-level views)

Write c = (c_v)_v : U → ℝ^V. For λ ∈ ℝ^V put
- B_λ := U ∩ {λ·c > 0},
- T_λ := U ∩ {λ·c = 0}.

**E1 (PROVED).**
- (a) If λ ≫ 0 (every coordinate strictly positive), every maximiser of λ·z over Z is efficient. This includes every model B_λ ∪ S with S ⊆ T_λ.
- (b) Call a sequence λ¹, …, λ^r *admissible* if:
  - λ¹ ≥ 0;
  - for each ℓ, λ^ℓ ≥ 0 on Z_{ℓ−1} := {v : λ¹_v = … = λ^{ℓ−1}_v = 0}, with arbitrary signs elsewhere.

  Let F₀ := Z and F_ℓ := argmax_{F_{ℓ−1}} λ^ℓ. Every z ∈ F_{r−1} that maximises over F_{r−1} some μ with μ_{Z_{r−1}} ≫ 0 is efficient.

*Proof.*
- (a) is the standard fact: a dominator would strictly increase λ·z.
- (b), constructing a positive representative. Choose s_{r−1} ≪ s_{r−2} ≪ … ≪ s₁ large, so that μ' := μ + Σ_{i<r} s_i λ^i ≫ 0. This is possible because:
  - coordinates first used at level i are positive in λ^i;
  - coordinates in Z_{r−1} are positive in μ.
- (b), maximising. Each λ^i (i < r) is constant on F_{r−1}. So z maximises μ' over F_{r−1}, and by (a) it is Pareto-maximal within F_{r−1}.
- (b), climbing the chain. Suppose Y dominates z. Then λ¹ ≥ 0 gives z(Y) ∈ F₁. Next, λ² + sλ¹ ≥ 0 for large s gives z(Y) ∈ F₂, and so on. Hence z(Y) ∈ F_{r−1}, a contradiction. ∎

**E2 slab lemma (PROVED).** If λ ≫ 0 and T_λ is non-null, some efficient model is incoherent.

*Proof.*
- By E1(a), every B_λ ∪ S with S ⊆ T_λ is efficient.
- Take a density point p ≠ 0 of T_λ, and a small cube Q at p in which T_λ has density > 1 − η.
- Split Q along a direction e into three slabs Q₋, Q₀, Q₊, and let S := (T_λ∖Q) ∪ (T_λ∩(Q₋ ∪ Q₊)).
- Suppose B_λ ∪ S were a.e. a convex set C. Then C contains all but measure 2η|Q| of Q₋ ∪ Q₊.
- For x in the core of Q₀, the pairs (y, 2x − y) with y ∈ Q₋ and 2x − y ∈ Q₊ form a set of measure ≥ c|Q|. For η small, some pair lies in C × C, so x ∈ C.
- So C contains the core of Q₀. But (B_λ ∪ S) ∩ Q₀ ⊆ Q₀∖T_λ has measure ≤ η|Q|. Contradiction. ∎

**E3 free-sign lemma (PROVED).** Let λ¹ ≥ 0 support an efficient model X*, with tie region T := T_{λ¹}. For every μ with μ_v > 0 for all v ∉ supp λ¹, and arbitrary signs on supp λ¹:
- (a) every maximiser of μ·∫_S c over S ⊆ T, joined to B_{λ¹}, is efficient;
- (b) if T ∩ {μ·c = 0} is non-null, some efficient model is incoherent.

The same holds at any depth of an admissible chain, with Z_{r−1} in place of 𝒱∖supp λ¹.

*Proof.*
- (a) is E1(b) with r = 2.
- (b): μ' := μ + sλ¹ ≫ 0 has the same maximisers on F₁, and E2's argument runs inside T. ∎

*Meaning.* On a face, the omitted views (zero weight in λ¹) can remove incoherent tie-selections. But every view used by λ¹ re-enters with arbitrary sign. So the used views must be harmless on T under weights of either sign. Rank-one behaviour along a direction orthogonal to λ¹ is harmless; anything else generically is not (§8, witness W1).

**E4 rank-deficiency lemma (PROVED).** Suppose c(E) ⊆ L for a non-null E and a linear subspace L ⊆ ℝ^V with L ∩ ℝ^V_+ = {0}. Then some efficient model is incoherent.

*Proof.* By Gordan's alternative there is λ ≫ 0 with λ ⊥ L. Then E ⊆ T_λ; apply E2. ∎

**E5 rescaling (PROVED, with a caveat).** The lexicographic maximiser of an admissible chain is determined by the signs of λ^ℓ·c(h), level by level. So the set of admissible lexicographic maximisers with null final ties is unchanged by c ↦ s(h)c, for any measurable s > 0.

That every efficient model is such a maximiser is the lexicographic separation theorem (Martínez-Legaz–Singer, *Lexicographical separation in ℝⁿ*, Linear Algebra Appl. 1987; citation to be verified). I do not use it in any theorem below.

So, as for single charts, only the **direction field** h ↦ c(h)/|c(h)| matters for coverage. The rankings themselves differ.

**E6 (PROVED).** If 1_{C_n} → 1_A a.e. with each C_n a convex cone, then A is a.e. equal to liminf C_n = ∪_m ∩_{n≥m} C_n. That set is an increasing union of convex cones, hence convex.

---

## 4. Theorem C: concave views cannot cover the reversed triangle, whatever the faces

**Theorem C (PROVED).** Take the setting of §1, with (WS) and (SG). Each world carries finitely many views of either type:
- single-level, with gain c_v concave and positively homogeneous on U;
- two-level lexicographic, with a convex, positively homogeneous veto φ_v ≥ 0 vanishing on {h_{j(v)} > 0}, paid by the target or not, followed by such a c_v.

If every undominated model is coherent, then D_K is dominated.

Non-null ties, boundary weights and omitted views are all allowed. No strict sign-correctness and no uniqueness are assumed.

*Proof.*

1. **Discarding views that vanish on D_K.**
   - Single-level views are lexicographic views with φ_v ≡ 0. Let W₀ be the set of views whose veto vanishes a.e. on D_K. Let S₀ ⊆ W₀ be those whose gain c_v also vanishes a.e. on D_K.
   - For v ∈ S₀, c_v is concave and zero on the open cone D_K, so c_v ≤ 0 everywhere. By (WS), c_v = 0 on {h_{j(v)} > 0}.
   - Put R_v := {φ_v > 0} ∪ {c_v < 0} ⊆ {h_{j(v)} < 0}. This is a priority region at j(v) in E61's sense. Any Y meeting R_v in a non-null set is strictly worse in view v than M_{R_v} := (U∖R_v) ∩ {h_{j(v)} < 0}, on which both levels vanish.
   - R_v does not meet D_K. By the refereed collar lemma (E61 Lemma 3.4, which needs the box lemma and hence "every undominated model coherent"), R_v misses a.e. the open collar C beyond the relative interiors of the three faces.
   - The same lemma applied to {φ_v > 0} shows that every veto in W₀ vanishes a.e. on D_K ∪ C.

2. **Restricting and separating.** Restrict to models Y ⊆ D_K ∪ C. These are legitimate models by (LF).
   - On them, every view in S₀ is identically 0 at both levels, and every veto in W₀ is 0. Put W₀' := W₀∖S₀, and let P be the views whose veto D_K pays.
   - Suppose some such Y were strictly better than D_K in c_v for all v ∈ W₀' and in φ_v for all v ∈ P. Then Y would dominate D_K. (If W₀' ∪ P = ∅, all views vanish on D_K, and (SG) fails at D_K.)
   - The range over Y ⊆ D_K ∪ C is compact and convex (Lyapunov). Separating it from the open cone of such improvements (VB note Step 2) gives β ≥ 0 on W₀' and α ≥ 0 on P, not both zero. With them, D_K maximises ∫_Y g over Y ⊆ D_K ∪ C, where

     g := Σ_{W₀'} β_v c_v − Σ_P α_v φ_v.

   - **β ≠ 0.** If β = 0, D_K would minimise Σα_v∫φ_v. But the empty model scores 0, while D_K pays a positive veto.
   - So g ≥ 0 a.e. on D_K and g ≤ 0 a.e. on C.

3. **g vanishes on ∂D_K∖0.**
   - g is concave on the open convex cone U, hence continuous.
   - Every relative-interior face point is a limit of points of D_K and of C. So g = 0 on the relative interiors of the faces, and by continuity on ∂D_K∖0.

4. **Each summand is linear on each face.** On a face F, the summands β_v c_v and −α_v φ_v are concave and add up to 0. Each is therefore also convex there, hence linear on F.

5. **Crossing rows.**
   - On a face that crosses h_j = 0 (F_i and F_k, for i, k ≠ j), (WS) and linearity force c_v = κ_v^F h_j for each view v at world j, with κ ≥ 0.
   - A veto must also vanish where h_j > 0, so it is identically 0 on every face.
   - At the ray r_j, where (r_j)_j = −3, the coefficients from the two crossing faces coincide.
   - On the anti-visible face F_j, c_v is linear with c_v(r_i) = c_v(r_k) = 2κ_v.

6. **The circulant.**
   - Put M_j := Σ_{v∈𝒱_j} β_v κ_v.
   - g = 0 at r_i and r_k on F_j gives −3M_i + 2(M_j + M_k) = 0 for each i.
   - The circulant (−3, 2, 2) is nonsingular (eigenvalues 1, −5, −5). So M = 0 and κ_v = 0 whenever β_v > 0.
   - Hence every summand vanishes on ∂D_K∖0.

7. **Each summand vanishes on D_K.**
   - Take a summand f (concave, zero on ∂D_K∖0). Every point of D_K lies on a chord with ends in ∂D_K∖0, so f ≥ 0 on D_K.
   - By (WS), f ≤ 0 on the non-empty open set D_K ∩ {h_{j(v)} < 0}, so f = 0 there.
   - A concave function that is ≥ 0 on a convex set and 0 on an open subset of it vanishes identically on that set. So f ≡ 0 on D_K.

8. **Contradiction.** For α_v > 0 this says φ_v ≡ 0 on D_K, so v is not paid. For β_v > 0 it says c_v ≡ 0 on D_K, so v ∈ S₀. Both contradict the choice of W₀' and P. ∎

**Corollaries.**
- (i) The audit's paid-veto candidate fails: unanimity of Brier views and target-paid convex vetoes, with any number of views and any face structure.
- (ii) It also fails with box secondaries or VB-type concave secondaries.
- (iii) It fails with "flat weighted combinations" of concave views. On D_K such a combination forces every summand to be linear and then zero (step 2 of the face argument).

So a cover needs **non-concave** views. This is consistent with AUDIT_r63's counterexample, whose c₂ is not concave.

---

## 5. Two quick exclusions

**Prop 5.1 (orthant-diagonal views; PROVED).** Suppose every view is orthant-diagonal: c_v(h) = d_{σ,v} h_{j(v)} on each open orthant σ, with d_{σ,v} ≥ 0. Assume (SG), any number of views, and any faces. Then D_K is dominated.

*Proof.*
- Let σ₃ = (+,+,−). There D_K ∩ σ₃ = σ₃ ∩ {v₁·h > 0, v₂·h > 0} is not a.e. a half-space of σ₃.
- On σ₃, scores depend on S ⊆ σ₃ only through the moment m(S) := ∫_S h dμ, via z = M_σ m.
- The moment zonoid 𝓜 := {m(S) : S ⊆ σ₃} has boundary points m({w·h > 0} ∩ σ₃) only. Each supporting face is a singleton, because {w·h = 0} is null.
- So m(D_K ∩ σ₃) ∈ int 𝓜, and some S has m(S) = m(D_K ∩ σ₃) + ε𝟙.
- Then M_σ(ε𝟙) = ε(d_{σ,v})_v ≥ 0, and it is nonzero by (SG). So (D_K∖σ₃) ∪ S dominates D_K. ∎

The same argument shows something more general. If all views are linear on a cell σ, D_K ∩ σ is not a half-space, and M_σ d ∈ ℝ^V_+∖0 for some d, then D_K is dominated. So the corners r_j must lie on cell walls. Composing any number of orthant-diagonal views does not reach the reversed triangle. This is consistent with the orthant-map closure lemma of AUDIT_r63.

**Cor 5.2 (PROVED from E4).**
- (a) **Constant direction (any target).** Suppose c has constant direction κ on a non-null set E in a mixed orthant. By (WS), κ has entries of both signs. Then span{κ} ∩ ℝ^V_+ = {0}, and E4 applies. So piecewise-constant direction fields are impossible, for every target.
- (b) **Rank-one caps.** A cap on which the whole field is ∝ κ, with κ of mixed sign, is impossible. This is used in §7.

---

## 6. Theorem S: one-level resolution reduces to the corner seam

**Theorem S (PROVED, given C62 Thm 4.1, refereed CORRECT after repair).** Assume single-level views satisfying (WS) and (SG), each continuous and piecewise linear on a finite fan near cl D_K∖0. Suppose D_K is the lexicographic maximiser of an admissible chain λ¹, …, λ^r such that:
- (i) the final tie region T_{r−1} contains an open conic O ⊇ ∂D_K∖0;
- (ii) λ^r_v > 0 for all v ∈ Z_{r−1}.

The case r = 1 is λ* ≫ 0 with null ties. Then some efficient model is incoherent.

*Proof.*
1. **The aggregated chart.** By E1(b), λ^r has a strictly positive representative ν. Define C_j := Σ_{v∈𝒱_j} ν_v c_v.
   - C is continuous and piecewise linear.
   - It is strictly sign-correct a.e., by (SG) and ν ≫ 0.
2. **Coherent local Bayes sets.** Fix π ∈ ℝ³_{++} and let μ_π := (π_{j(v)}ν_v)_v.
   - μ_π has strictly positive coordinates on Z_{r−1}.
   - By E1(b) and E3 at depth r, every maximiser over F_{r−1} is efficient. By E2 its ties in T_{r−1} are null.
   - On O it coincides with {π·C > 0}.
   - So for every π ≫ 0, the set {π·C > 0} is locally convex near ∂D_K, with null ties.
3. **The target.** At π = 𝟙 the set is D_K.
4. **Applying C62.** These are C62 (C1)–(C4) near u, on the segments (e_k, u], and locally near ∂D_K∖0. C62's proof (Lemmas 4.2–4.4 and the corner continuity) is local to ∂D_K, so Thm 4.1 applies. ∎

**Scope.** This excludes, for continuous piecewise-linear views, every design whose whole boundary is settled at one level, with full freedom at that level.

**What escapes.** Designs in which different parts of ∂D_K are settled at **different** levels of the face chain. §7 studies the natural one.

---

## 7. The corner-cap mechanism: an escape from the corner seam, and why it closes

### 7.1 Design idea

- Cut each corner r_k off D_K by a straight cut [a, a'] lying inside D_K, giving a cap C_k ⊂ D_K. The rest is a hexagon H.
- At level 1, the weight λ¹ (support R; omitted views Z := 𝒱∖R) satisfies:
  - λ¹·c ≡ 0 on the caps;
  - λ¹·c > 0 on H;
  - λ¹·c < 0 on U∖cl D_K.
- At level 2, the omitted views accept the caps.
- So the face middles are settled at level 1, and the corners at level 2.
- The hexagon's corners are the cut points. The corner rays r_k lie inside tied regions, so C62's corner continuity at r_k never enters.

### 7.2 First order: the corner seam is replaced by a solvable cut-point system (CHECKED)

- Level-1 analysis on the face middles, with perturbations λ¹ + δ, gives face-linear crossing rows for the aggregated used views, exactly as in C62. On face F_k:
  - C_i = M^k_i h_i and C_j = M^k_j h_j for the crossing worlds;
  - C_k = −(C_i + C_j).
- At a cut point a, the cap's all-or-nothing behaviour (§7.3) forces the values from the two faces at the same corner to be parallel: C^{F_a}(a) ∥ C^{F_b}(a'). This replaces C62's corner condition at r_k.
- **At p = 0 (cuts at the corner).** This is C62 Cor 4.5's system, with only complex solutions 3/4 ± i√7/4 (re-CHECKED, `capcut.out`).
- **Cyclically symmetric cuts a = r_c + p r_b.** The condition is 3px² − 2px + 3p − 2x² + 3x − 2 = 0. This is solvable over the reals iff −32p² + 36p − 7 ≥ 0, i.e. p ∈ [1/4, 7/8]. Cut validity (the cap contains no crossing point) needs p < 2/3, and the positivity condition holds. CHECKED (`capcut_sym.out`).
- **Exact point p = 1/4, x = 1.**
  - Cut points: (2,1,−2) and (1,2,−2), i.e. the cut is h₃ = −2 in the cross-section.
  - The face maps C = h − (Σh)e_k (all crossing coefficients 1) take the same value κ^(3) = (1,1,−2) at both cut points.
  - Equivalently, the diagonal charts d^(1) = (1/2,1,1) and d^(2) = (1,1/2,1), which are ∝ v₁ and v₂ and are E61's lower-prevision pieces, agree with κ^(3) at the cut points. CHECKED.
- **Non-symmetric cuts.** Least squares over random cut positions in [0, 2/3)⁶ finds real positive solutions in 3356 of 4000 trials. NUMERICS (`capcut_search.out`).

So the C62/A62 corner obstruction is specific to settling the corner at the same level as the faces.

### 7.3 Forced local structure of a cap (PROVED, local)

**Hypotheses.**
- **(K1)** λ¹·c ≡ 0 on the open cap C ⊂ D_K. C is bounded by the cut segment [a, a'] ⊂ D_K and by two face portions.
- **(K2)** λ¹·c > 0 on the H-side cells next to the cut, and it tends to 0 at the cut (continuity).
- **(K3)** λ¹·c < 0, with nonzero slope, on the cells just outside the cap's face portions.
- **(K4)** c is continuous and piecewise linear near cl C∖0.

The perturbations used are λ¹ + sδ + ε𝟙, with ε ≪ s. Here δ_R is arbitrary and δ_Z ≥ 0. These weights are strictly positive, so their Bayes sets are efficient (E1) and must be coherent.

**(a) On the cut, all used views are mutually proportional, and so is every pair of views of opposite sign.**
- If not, some admissible δ makes δ·c change sign at an interior point x of the cut.
- Near x, the accepted set is then:
  - on one side of x, the H side minus an O(s) layer;
  - on the other side, H plus the part of the cap where δ·c > 0. That part's boundary leaves the cut at x at a fixed angle.
- This gives a reflex angle at x that does not shrink as s → 0. Not convex.

**(b) Hence c_R = τκ_R on C, with τ ≥ 0.**
- Here κ_R is the common direction of c_R on the cut (assumed nonzero; the degenerate case c_R = 0 on the cut is the pinned cut).
- If δ_R·κ_R < 0, the cap is rejected near the cut. A convex accepted set containing ℝ³₊ ⊂ H then rejects the whole cap.
- So δ_R·c_R ≤ 0 on C whenever δ_R·κ_R < 0, which forces c_R(h) ∈ ℝ₊κ_R.

**(c) The omitted views on the cap.**
- Then c_Z = τκ_Z − ζ with ζ ≥ 0. This is Farkas over the admissible cone {δ_Z ≥ 0}.
- If ζ ≡ 0, the whole field is rank one on C, which Cor 5.2(b) excludes.
- So the omitted views must be "lowered" by a depth term ζ, and the cap's accepted parts are sublevel sets of λ_Z·ζ/τ. These must be strips on the H side; in practice ζ/τ increases with depth.

**(d) Normal derivative across the cut.** Let D be the derivative of c across the cut into H. Then D ∈ ℝ₊κ̃ + ℝ^V_+, where κ̃ is the cap direction. Otherwise some λ ≫ 0 would accept the cap while rejecting H next to the cut.

### 7.4 Rotation lemma (PROVED, rank-one case)

**Hypotheses.** Let a be a cut point on face F_k, and assume (K1)–(K4) and (b). In addition:
- **(H1)** On the face-middle side M of a, the boundary is a level-1 null tie: λ¹·c > 0 inside and < 0 outside, with outer slope β_M > 0.
- **(H3')** Some μ with μ_Z ≫ 0 has μ·c > 0 on cl C∖0 near a. For example, the level-2 weight that accepts the cap.

Let τ_R := ∂_t c_R(a) be the derivative along F_k into M.

**Conclusion.** τ_R ∈ ℝκ_R.

*Proof.*
1. **The perturbation.** Suppose δ ⊥ κ_R with δ·τ_R > 0. Put λ_η := λ¹ + η(δ, 0) + η²μ + η³𝟙. This is strictly positive for small η, so its Bayes set is efficient.
2. **On the cap.** λ_η·c = η²μ·c + O(η³) > 0 near a, so the cap is accepted.
3. **Just outside the cap's face portion.** There λ¹·c = −β_P·dist, and δ·c_R vanishes on that face portion (c_R ∝ κ_R there). So the accepted layer has thickness O(η²).
4. **Just outside the face middle.** At w(t) = a + t·e (t > 0), λ_η·c(w(t)) = ηtδ·τ_R + O(η²). So the accepted region reaches out to distance ≈ ηtδ·τ_R/β_M.
5. **The non-convex triple.** Take:
   - p := w(−t₁) slightly inside the cap (accepted);
   - q := w(t₁) + (ηt₁δ·τ_R/2β_M)·n (accepted).

   Their midpoint lies at outward distance Θ(η) over a. There λ_η·c ≈ −β·Θ(η) + O(η²) < 0, using δ·c_R(a) = 0. So the midpoint is rejected.
6. **Conclusion.** This is an incoherent efficient model. So δ·τ_R ≤ 0 for every δ ⊥ κ_R. Applying the same to −δ gives δ·τ_R = 0, i.e. τ_R ∈ ℝκ_R. ∎

An exact instance is witness W3 in §8: α = (11/10, 9/10, 1) ⊥ κ^(3), with τ_R = (0,−1,1) ∉ ℝκ.

### 7.5 Consequences

**Cor 7.1 (PROVED).** Suppose c_R is linear along F_k from a through both crossing points, which is face linearity, the multi-view analogue of C62 Lemma 4.3 on the middle. Then c_R = κ_R·f with f affine.
- Every used view at a crossing world i with κ_v ≠ 0 vanishes at the crossing point h_i = 0.
- If both crossing worlds have such views, f ≡ 0, so **c_R ≡ 0 on the face middle** (the pinned branch).
- Otherwise, every used view of some crossing world vanishes on the cap.

**CONJECTURE 7.2 (outline).** The cap mechanism is excluded for continuous piecewise-linear fields. On the pinned branch:
- REF62 §4(b)'s switching argument transfers. Along λ¹ + sπ' (π' on the used views, plus ε on the omitted ones), the outer cells beyond a pinned face middle switch on at times fixed by their data.
- Unequal times give genuine non-convexity.
- Equal times for an open set of π' force proportional data. The crossing worlds then force the common direction onto world-k views, contradicting rejection outside at λ¹.

**Steps still to be refereed.**
- the multi-view transfer of C62 Lemma 4.2 / 4.3 (face linearity and c_R ≠ 0) on the middles;
- the transfer of REF62 §4(b);
- the degenerate sub-case in which a crossing world's used views vanish on a cap.

---

## 8. An explicit six-view system Σ_cap: the corrected task step by step (CHECKED, `sigma_cap.out`)

**Geometry (cross-section Σh = 1).**
- Caps: C_k := T ∩ {h_k < −2}. Cap C₃ has vertices r₃ = (2,2,−3), (2,1,−2) and (1,2,−2), and lies in the orthant (+,+,−).
- Hexagon: H' := T∖∪cl C_k.
- U = D_{K'} with K' = (u + K)/2.

**Views at world j.**
- **A_j:**
  - off the caps, E61's lower-prevision chart (5/2)·v_{k(h),j}·h_j, with k(h) = argmin_l v_l·h;
  - on C_k, A = (Σh)(𝟙 − 3e_k). For k = 3 this is the direction κ^(3) = (1,1,−2).
- **B_j:**
  - off the caps, Brier h_j;
  - on C_k, B_k = h_k + Σh and B_i = Σh for i ≠ k. This is the depth-lowered form of §7.3(c), with ζ_k = depth.

All views are sign-correct, and A alone is strictly sign-correct, so strict (G) holds.
- (IB) holds because views are integrals.
- Transitivity holds because the orders are unanimity orders.
- (LF) holds because U ⊇ cl D_K∖0.

**Step 1 (compactness).** Undominated weak dominators exist, by §2.

**Step 2 (supporting face).**
- λ¹ = (1,1,1 | 0,0,0). **The Brier weights vanish.**
- u·A = (5/2)·min_k v_k·h off the caps. This is > 0 on H' and < 0 off D_K, and it is ≡ 0 on the caps.
- So the tie region is exactly the three caps. CHECKED at sample points.

**Step 3 (omitted views on the face).**
- The face's minimisers are H' ∪ S for arbitrary S ⊆ caps, so incoherent ones abound.
- With μ_B ≫ 0 and μ_A arbitrary, which is exactly the free-sign family of E3, on C₃:

  μ·c = (μ_A·κ^(3) + μ_{B1} + μ_{B2} + μ_{B3})Σh + μ_{B3}h₃.

- So the efficient selections are strips {h₃ > t·Σh} parallel to the cut (CHECKED: 0 mismatches in about 10⁴ random (μ, point) tests; also immediate from the displayed formula). H' ∪ strips = T ∩ {h_k > t_k} is coherent.
- At level 2, (0,0,0 | 1,1,1) gives 3Σh + h_k > 0 on each open cap. So D_K is the **unique** lexicographic maximiser, hence efficient by E1(b), and (C) holds at D_K.
- **The omitted views do eliminate every incoherent minimiser on this face.**

**Step 4 (the entire efficient set): failure.** Both witnesses are robust, with all inequalities strict.
- **W2, at λ = (1,2,3 | ε,ε,ε), ε = 10⁻⁶ (strictly positive weights, so efficient by E1).**
  - x = (1001/1000, 1, −3/4) and y = (1, 13/10, −3/4) are accepted, with λ·c ≈ 0.2505 and 0.0500.
  - Their midpoint m = (2001/2000, 23/20, −3/4) is rejected, with λ·c ≈ −0.0995.
  - The signs are stable on a 10⁻⁵ grid and for ε ∈ {0, 10⁻³}.
  - This is E61's lower-prevision defect, untouched by the caps.
- **W3, the rotation lemma, at λ = (11/10, 9/10, 1 | ε,ε,ε), ε = 10⁻⁴ (α ⊥ κ^(3)).**
  - p = (1999/1000, 2081/2000, −4079/2000), inside C₃, is accepted.
  - q = (401/200, 383/400, −157/80), just beyond the middle of F₁, is accepted.
  - Their midpoint (1001/500, 999/1000, −2001/1000) is rejected.

**Step 5 (variant with plain Brier on the caps): failure on the target's own face (W1, `freesign_witness.out`).**
- μ = (−4,0,0 | 3,1,1) has strictly positive representative μ + 5λ¹ = (1,5,5,3,1,1). By E3 its face selection H' ∪ (C₃ ∩ {h₁ > 3/2}) ∪ … is efficient.
- p = (17/10, 3/2, −11/5) and q = (1, 39/20, −39/20) are accepted.
- Their midpoint (27/20, 69/40, −83/40) is rejected.
- So with plain Brier on the caps, the omitted views do **not** eliminate the incoherent minimisers: the used views A re-enter with a negative weight.

**Diagnosis.**
- Σ_cap realises the audit's mechanism exactly: target on a boundary face, vanishing omitted weights, and omitted views that clean the face.
- It fails only off that face.
- §§4–7 show that within continuous piecewise-linear and concave designs the off-face failures are forced: W2-type failures by Theorem S and C62, W3-type failures by the rotation lemma.

---

## 9. What is excluded, and what escapes remain

**Excluded classes**, all on one-sided U with (LF) and all assuming strict (G):
1. Concave single-level views, and convex-veto/concave two-level lexicographic views, with any number of views, any faces, ties and paid vetoes (Thm C).
2. Orthant-diagonal views of any number (Prop 5.1).
3. Piecewise-constant direction fields (Cor 5.2), for every target.
4. Continuous piecewise-linear single-level views with one-level resolution (Thm S).
5. The explicit cap system Σ_cap, its plain-Brier variant, and (CONJECTURE 7.2) every continuous piecewise-linear cap design.

**Escapes not excluded.**
- (i) Fields that are **not piecewise linear**, or are discontinuous near ∂D_K, other than the specific discontinuities of Σ_cap.
- (ii) **Other resolution patterns**: tie regions that reach outside D_K, face middles settled after the corners, or level-2 regions with their own transitions. The transition analysis of §7.4 is the tool for each.
- (iii) Lexicographic views with non-convex vetoes, or with more than two levels.
- (iv) Non-additive or non-view orders (E61 §7(ii)).
- (v) Two-sided domains (not studied here; FD62 makes them harder).

**Reachable nearby results (for the paper).**
- Theorem C is a clean, axiom-level-style exclusion of the whole concave and VB-type finite-view family, including the incomplete orders with paid vetoes that the audit wanted examined.
- The free-sign lemma E3 and the slab lemma E2 are the general reason why "omitted views eliminate incoherent minimisers" is a strong requirement.
- The cut-point solvability (§7.2) shows that C62's corner obstruction is a statement about **one-level** resolution, not about finite-view rankings in general.

## 10. Files (`in63py/`)

| File | Content |
|---|---|
| `capcut.py` / `.out` | cut-point direction system; p = 0 reduces to the C62 corner system |
| `capcut_sym.py` / `.out` | cyclic-symmetric solutions x(p); discriminant; positivity |
| `capcut_search.py` / `.out` | non-symmetric numeric search (NUMERICS) |
| `sigma_cap.py` / `.out` | Σ_cap exact checks: signs, face structure, strips, witnesses W2 and W3 |
| `freesign_witness.py` / `.out` | witness W1 (free-sign failure, plain-Brier variant) |
