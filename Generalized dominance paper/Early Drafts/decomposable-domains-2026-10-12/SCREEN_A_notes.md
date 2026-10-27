# SCREEN_A. Candidate A (super-majority of a continuum of judges) against S3: the collapse does not need atoms

19 Oct 2026. Design screen under BRIEF_DESIGN1; candidate A as in DESIGN_MEMO §2A. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact rational computation, script in `screenA_py/` (run `python3 -I <script>.py` inside that folder; each `.out` ends with `ALL CHECKS PASSED`).
- **CONJECTURE**: marked where offered. **NUMERICS**: none used.

Scripts:
- `quantile_check.py` → `quantile_check.out`: the one-dimensional core of Lemma 3.2 on 20 000 random weighted instances, and atomless examples.
- `dkstar_rival.py` → `dkstar_rival.out`: the explicit rival of Proposition 4.1 at D_K for five interval models K, including K* = [1/3, 2/3].
- `cycles_ties.py` → `cycles_ties.out`: strict k-cycles for k = ⌈1/(1−θ)⌉, and the mass-slack example of §2.4.

Nothing in a proof rests on a script.

---

## 0. Verdict

**A FAILS screen S3** (PROVED).

**Why.** The blocking-cone collapse does **not** need atoms. The finite proofs (NN1 Lemma 2.1, NN2 Theorem 2.3) are order-statistic arguments. With a judge measure, the order statistics become quantiles, and the same chain of inequalities forces an **atom** in the law of the judges' normalised boundary profiles. Its mass is at least 2θ − 1 at every world. This replaces "n − 2b + 2 judges", and it is a blocking mass (> 1 − θ) exactly when θ > 2/3, the (TC) threshold.

- **Atoms are produced, not assumed.** The proof needs atoms neither in π nor in the profile law. It *produces* a profile atom.
- **Why the memo's hook fails.** A point lying in every blocking cone of one world has Tukey depth ≥ θ > 1/2. A law with no atom at that point has depth ≤ 1/2 there. The centrepoint theorem guarantees only depth 1/(d+1), which is not what (QS) needs (Remark 3.4).
- **The two-world target.** Every interior index of BRIEF_DESIGN1's two-world target is an edge index. So (QS) fails at D_{K*}, and at every non-degenerate interval model, whenever the law of the judges' boundary switch ratio has no atom of mass ≥ 2θ − 1 common to both worlds. An explicit two-sector rival does this (Proposition 4.1, CHECKED for five interval models).
- **With such an atom, A gains nothing.** A is then a quorum committee containing a coincident bloc. On the boundary that bloc is one score with one exchange rate, exactly as for finite quorums. A gains nothing at S3 over the quorum line.

**Design checks (Q1).**

| Check | Status | Condition |
|---|---|---|
| (IB) | PROVED | — |
| strict (G) | PROVED | needs 0 ≤ ψ(s) ≤ s |
| no non-trivial ties | PROVED | θ > 1/2 and ψ > 0 on (0, ∞) |
| (TC) | PROVED | θ > 2/3 |
| closed sections | PROVED | reverse Fatou; joint measurability |
| direct (C) | PROVED | — |
| selected admissibility | PROVED | — |
| strict cycles | PROVED; CHECKED | exactly the lengths k ≥ ν(θ) := ⌈1/(1−θ)⌉ ≥ 4 |
| lifting lemma | PROVED (conditional); CHECKED | compactness survives (relaxed controls), but only with a **strict mass slack** (U2); without slack it fails already for one comparison |

**Nearby result (what survives).** Proposition 4.1 is an exact local test usable on any super-majority rule: the two-sector rivals are defeated iff the two worlds' ratio laws have a common "deep point" c. To escape S3, a rule must break one of the three inputs of the collapse:
1. the linear response of each judge to swap masses (additivity of judges);
2. blocking mass below 1/2 (no ties);
3. two active worlds.

On the two-world target only input 1 can go. So the next primitive must make the **individual** judge non-additive. Candidate B's record-dependent exchange is one such primitive. Candidate A should be merged into the quorum line, not pursued as a new primitive.

---

## 1. Setting

- **Worlds and judges.** At world i, (V_i, π_i) is a probability space of judges. Each judge v has a strictly guiding loss ℓ_iv(h, a): strictly increasing in world-i rank, good 0 < silence 1 < bad 2 < contradiction 3.
- **Standing hypothesis (M).**
  - (v, h) ↦ ℓ_iv(h, a) is jointly measurable.
  - There is a common envelope e ∈ L¹(μ) with |ℓ_iv(h, a)| ≤ e(h) for all v, a.
  - Only §2.4 uses that e is common to all judges. Everything else needs only per-judge integrability.
- **Increments.** L_iv(X) := ∫ ℓ_iv(h, a_X(h)) dμ, d_iv(C, X) := ∫ |ℓ_iv(h, a_X) − ℓ_iv(h, a_C)| dμ, and Δ_iv(p, X) := L_iv(X) − L_iv(C_p).
- **Margin.** ψ : [0, ∞) → [0, ∞) is continuous and nondecreasing, with ψ(0) = 0 and 0 < ψ(s) ≤ s for s > 0.
- **Rule.** Judge v supports "C no worse than X" iff L_iv(X) − L_iv(C) ≥ ψ(d_iv(C, X)). World i accepts C R_i X iff the supporters have π_i-mass ≥ θ_i, with θ_i ∈ (2/3, 1).
- **Blocking mass.** β_i := 1 − θ_i ∈ (0, 1/3).
- **(QS_θ)** at p: for every X ≠ C_p, some i ∈ supp p has π_i{v : Δ_iv(p, X) > 0} ≥ θ_i.

**Lemma 1.1 (branch form; PROVED).** Assume v ↦ Δ_iv(p, X) is measurable, which (M) and Fubini give. Then (QS_θ) fails at p iff there are X ≠ C_p and, at every active i, a set B_i with π_i(B_i) > β_i and Δ_iv(p, X) ≤ 0 on B_i.

*Proof.* (QS_θ) fails for X iff, at every active i, π_i{Δ > 0} < θ_i. That holds iff π_i{Δ ≤ 0} > 1 − θ_i = β_i. ∎

Blocking sets are thus defined by a **strict** inequality, mass > β. Below, this strictness is exactly what pays for uniformity in v (Proposition 3.5).

---

## 2. Design checks (Q1)

### 2.1 (IB), strict (G), ties, (TC), direct (C), admissibility (PROVED)

These are LL3 A1, A3, A4, A5 and A7 with π-mass in place of counting.

- **(IB).** L_iv(X) − L_iv(C) and d_iv(C, X) are integrals over the changed set of functions of (h, old advice, new advice). π_i and θ_i are fixed. So the verdict is a function of the record, and it is null-invariant.
- **Strict (G).** Let X be at world i at least as good as Y a.e., and strictly better on a non-null set.
  - Every judge has L(Y) − L(X) = d > 0 and d ≥ ψ(d). So the supporters of "X no worse than Y" have mass 1.
  - For the reverse, a judge would need L(X) − L(Y) = −d ≥ ψ(d) ≥ 0, which is impossible. The reverse has mass 0 < θ.
- **No non-trivial ties.** Suppose C R_i X and X R_i C. Then the two supporter sets have masses ≥ θ > 1/2, so they overlap in mass ≥ 2θ − 1 > 0.
  - A judge in both has Δ ≥ ψ(d) and −Δ ≥ ψ(d). So ψ(d) = 0, hence d = 0, hence X = C a.e. by strict guidance.
  - With ψ ≡ 0 (bare weak signs) this fails: a positive mass of judges with Δ = 0 is possible. The margin is needed.
- **(TC).** Suppose acceptances X R Y, Y R Z, Z R X hold among distinct models.
  - Three supporter sets of mass ≥ θ share mass ≥ 3θ − 2 > 0.
  - A shared judge satisfies L(X) ≤ L(Y) − ψ, L(Y) ≤ L(Z) − ψ and L(Z) ≤ L(X) − ψ. Summing gives Σψ(d) ≤ 0, so all d = 0, a contradiction.
  - So not even a 3-cycle of acceptances exists. Repeated-model cases follow from "no ties", as in LL3 A5.
- **Direct (C).** Ties are trivial.
- **Selected admissibility.** Suppose Y ≠ C_p dominates C_p. By "no ties", Y is strictly better at every world, which contradicts competitiveness of C_p on supp p.

### 2.2 Closed sections (PROVED)

Fix X and i, and put F_v(p) := L_iv(X) − L_iv(C_p) − ψ(d_iv(C_p, X)).

- **Continuity in p, for each v.** Both |L_iv(C_p) − L_iv(C_{p′})| and |d_iv(C_p, X) − d_iv(C_{p′}, X)| are ≤ 2∫_{C_p ≠ C_{p′}} e_v dμ. This tends to 0 as p′ → p, by continuity in measure of the selection. ψ is continuous.
- **Measurability in v.** By (M) and Fubini.
- **Closedness.** Let p_k → p with π{F_v(p_k) ≥ 0} ≥ θ. Any v in infinitely many of the sets {F_v(p_k) ≥ 0} has F_v(p) ≥ 0. So reverse Fatou gives π{F_v(p) ≥ 0} ≥ π(limsup_k{F_v(p_k) ≥ 0}) ≥ limsup_k π{F_v(p_k) ≥ 0} ≥ θ.
- **Other direction.** The same argument applies to sections of "X R_i C_p".

No uniformity in v is needed here.

### 2.3 Cycles: exactly the lengths k ≥ ν(θ) = ⌈1/(1−θ)⌉ (PROVED; CHECKED `cycles_ties.out` Part 1)

**Necessity.** Take a cycle of acceptances among distinct consecutive models.
- The supporter sets S_0, …, S_{k−1} have masses ≥ θ.
- A judge in all of them would have strictly increasing loss around the cycle: d > 0 on each edge forces ψ(d) > 0. So π(∩S_m) = 0.
- Hence 1 ≤ Σ π(S_m^c) ≤ k(1 − θ).

**Sufficiency (π atomless, or V splittable into k sets of mass ≤ 1 − θ).**
- **Classes.** Split V into classes G_0, …, G_{k−1}, each of mass ≤ 1 − θ.
- **Models.** Take LL3 Theorem A(c)'s cells F_0, …, F_{k−1}. Model A_m has silence on F_m and good advice elsewhere.
- **Judges.** A judge in class j has cell masses x_m = s·R^{(m−j−1) mod k}.
- **Margin condition.** Edge m ≠ j needs (R − 1)x_m ≥ ψ((R + 1)x_m). This holds if ψ(u)/u ≤ (R − 1)/(R + 1) on the range used, and choosing s small and R large arranges that.
- **Strictness.** Edge m is supported by V ∖ G_m, of mass ≥ θ. Its reverse is supported only by G_m, of mass ≤ 1 − θ < θ.
- **Longer cycles.** Every k ≥ ν is obtained by repetition, as in LL3.

For θ ∈ (2/3, 3/4] the shortest strict cycle has length 4; for θ ∈ (3/4, 4/5] it has length 5; and so on. Checked exactly for θ ∈ {2003/3000, 7/10, 3/4, 4/5, 9/10} and ψ ∈ {s/2, s²/(1+s)}.

### 2.4 The strict-sign lifting lemma (AUDIT_LL) for a continuum

**What breaks.** The finite proof uses two things:
1. compactness of the attainable set of finitely many (Δ_iv, d_iv), via Lyapunov purification;
2. integer counts, so that "≥ q judges with Δ > 0" has slack.

Both fail for a continuum:
- Lyapunov's theorem fails for infinitely many integrands.
- π{Δ > 0} = θ exactly can hold while π{Δ ≥ c} < θ for every c > 0.

**Example 2.1 (PROVED; CHECKED `cycles_ties.out` Part 3).** Take θ = 3/4 and v ~ U[0, 1]. The record C → X worsens a cell of judge-mass W_v = 1 and improves one of mass I_v = 2 − v − θ. Then:
- Δ_v = v − (1 − θ), so π{Δ_v > 0} = θ: the strict-sign super-majority holds;
- d_v ≥ 1 for every v, so ψ(d_v) ≥ ψ(1) > 0. The supporters under any margin ψ > 0 have mass < θ. The exact bounds are 1/12 for ψ = s/2, 0.0308 for s²/(1+s), and 0.749998 for s/10⁶.

So strict signs do not lift to any margin, even for a single comparison.

**Proposition 2.2 (continuum lifting; PROVED, short).**
- **Hypotheses.** Assume (M) with a common envelope, a selection continuous in measure on Δ, and:
  - **(U2) relaxed strict-slack (QS):** for every p and every *relaxed* rival X ≠ C_p (a measurable h ↦ probability on A(h)), some active i has π_i{Δ_iv(p, X) > 0} > θ_i.
- **Conclusion.** There is a ψ as in §1 (also with ψ(s)/s → 0) such that rule A makes every C_p competitive.

*Proof.* The proof is AUDIT_LL's, with three changes.
1. **Compactness.** Relaxed controls form a weak*-compact, metrisable subset of L^∞(μ)⁴. Δ_v and d_v are affine in X and weak*-continuous for each v. Base changes C_{p_k} → C_p cost at most 2∫_{C_{p_k} ≠ C_p} e, uniformly in v.
2. **The limit is not C_p.** Let r_i(p, X) := sup{t : π_i{Δ_iv ≥ t} ≥ θ_i}, and suppose r(p_k, X_k) → 0 with D(p_k, X_k) := sup_v d_v ≥ a. Take a weak* limit X*. It is not C_p: weak* convergence of indicator controls to the pure control C_p forces μ{X_k ≠ C_p} → 0, hence D → 0.
3. **Contradiction with (U2).** For every t > 0, pointwise convergence and Fatou give π{Δ_v(X*) ≥ 2t} ≤ liminf_k π{Δ_v(X_k) ≥ t} < θ. So π{Δ_v(X*) > 0} ≤ θ at every active world, contradicting (U2).
4. **Closing.** As in AUDIT_LL: π{Δ ≥ r(p, X)} ≥ θ by left-continuity, and ψ(d_v) ≤ ψ(D) < δ(D) ≤ r. ∎

*What uniformity in v is needed.*
- **A common envelope.** It is used for the base change and for step 2.
- **The strict mass slack of (U2), on relaxed rivals.** Example 2.1 shows the slack cannot be dropped. With finitely many judges, (U2) is equivalent to (QS), by Lyapunov and integer counts.
- **Optional: L¹-relative compactness.** If {ℓ_iv(·, a)}_v is relatively compact in L¹(μ), then relaxed increments are *uniform-in-v* limits of pure ones. (U2) then reads "(QS) with slack on the uniform closure of the pure rivals".

So compactness survives a continuum, but the hypothesis of the lemma becomes a robust (QS), not bare (QS).

---

## 3. The key screen (Q2): a measure version of the collapse forces positive-mass coincidence

### 3.1 Abstract statements

Let E be a finite-dimensional real vector space and ψ ∈ E* (here ψ is a normalising functional, not the margin).

- **Profiles.** For a probability space (V, π) and measurable a : V → E with ψ(a_v) > 0, write â_v := a_v/ψ(a_v).
- **Measure cone.** cone_π(T) := {∫_T a ρ dπ : ρ ≥ 0, ρ|a| integrable}.
- **Coinciding judges.** "Judges coincide" means they have equal â, i.e. positively proportional profiles.

**Lemma 3.1 (generic projection; PROVED).** Let λ be a finite Borel measure on E. For all f ∈ E* outside a countable union of proper linear subspaces, every atom of f_*λ is f(z) for exactly one atom z of λ, with the same mass. In particular, f_*(atomless part) has no atoms.

*Proof.*
1. **Pure subspaces.** Write λ = λ_a + λ_c (atomic plus atomless parts). Call an affine subspace W *pure* if λ_c(W) > 0 and λ_c(W′) = 0 for every proper affine W′ ⊊ W.
2. **There are countably many.** Two distinct pure W, W′ of equal dimension meet in a proper affine subspace of each, which is λ_c-null. So the pure subspaces of each dimension are a.e.-disjoint sets of positive mass, hence countably many. All have dim ≥ 1, since λ_c is atomless.
3. **Every positive-mass subspace contains one.** Any affine H with λ_c(H) > 0 contains a pure W: take a minimal-dimensional affine subspace of H of positive λ_c-mass.
4. **Choice of f.** Choose f non-constant on every pure W, which excludes the annihilators of their direction spaces. Choose it also injective on the countable atom set of λ_a, which excludes the annihilators of differences.
5. **Conclusion.** A level set of f contains no pure subspace, so it is λ_c-null. It contains at most one atom of λ_a. ∎

**Lemma 3.2 (two-colour median lemma for measures; PROVED; 1-D core CHECKED `quantile_check.out` Part 1).**
- **Setting.** Let (V, π, a) and (U, ν, b) be as above, and β_a, β_b ∈ [0, 1/2).
- **Hypothesis.** For every f ∈ E* and t ∈ ℝ, it is **not** the case that both π{f(â) > t} > β_a and ν{f(b̂) < t} > β_b. (H1)
- **Conclusion.** There is z with ψ(z) = 1, π{â = z} ≥ 1 − 2β_a and ν{b̂ = z} ≥ 1 − 2β_b. Moreover, every other point carries π-mass ≤ β_a and ν-mass ≤ β_b. So for β < 1/3, z is the unique point of mass > β.
- **The CHECKED part.** In one dimension, (H1) holds iff some c has P(<c), P(>c), Q(<c), Q(>c) all ≤ β. This was checked on 20 000 random weighted instances with β ∈ {1/5, 1/4, 3/10, 97/300, 2/5}.

*Proof.*
1. **Projection.** Fix f generic for both laws (Lemma 3.1), and injective on the union of their atom sets. Let P and Q be the laws of f(â) and f(b̂).
2. **Quantiles.** Put u_P := sup{t : P(>t) > β_a} and l_Q := inf{t : Q(<t) > β_b}.
   - {t : P(>t) > β_a} = (−∞, u_P) is open, since P(>t) is right-continuous.
   - {t : Q(<t) > β_b} = (l_Q, ∞) is open, since Q(<t) is left-continuous.
3. **The chain.** (H1) makes these two half-lines disjoint, so u_P ≤ l_Q. Applying (H1) to −f gives u_Q ≤ l_P, with u_Q, l_P defined in the same way.
   - Since β < 1/2: for t < l_P we have P(<t) ≤ β_a, so P(>t′) ≥ P(≥ t) > β_a for every t′ < t. Hence l_P ≤ u_P, and likewise l_Q ≤ u_Q.
   - So l_P ≤ u_P ≤ l_Q ≤ u_Q ≤ l_P, and all equal one value c.
4. **The atom.** Taking limits from the definitions gives P(<c), P(>c) ≤ β_a, so P{c} ≥ 1 − 2β_a. Likewise Q{c} ≥ 1 − 2β_b.
5. **Back to profiles.** By Lemma 3.1, these atoms are images of atoms z of law(â) and z′ of law(b̂), with the same masses. Injectivity gives z = z′.
6. **Other points.** A point z″ ≠ z has f(z″) ≠ c, so its mass is ≤ P(>c) or ≤ P(<c), hence ≤ β_a. ∎

**Theorem 3.3 (measure blocking-cone collapse; PROVED).**
- **Setting.** S is a set of worlds with |S| ≥ 2. At each i ∈ S, (V_i, π_i, a_i) is as above, with β_i ∈ [0, 1/2).
- **Hypothesis (H_θ).** For every choice of measurable T_i with π_i(T_i) > β_i (all i ∈ S), ∩_i cone_{π_i}(T_i) ≠ {0}.
- **(a) Pairwise atoms.** For every pair i ≠ j there is a common profile atom of mass ≥ 1 − 2β_i at i and ≥ 1 − 2β_j at j.
- **(a′) One atom for all worlds.** If every β_i < 1/3 (θ_i > 2/3), one z serves all worlds: π_i{â = z} ≥ 2θ_i − 1 > β_i.
- **(b)** Under (a′), z ∈ cone_{π_i}(T) for every world i and every T with π_i(T) > β_i.
- **(c)** Under (a′), z is the only normalised point carrying mass > β_i at any world.
- **Converse.** (b) implies (H_θ).

*Proof.*
1. **(H_θ) gives (H1) for each pair (i, j).** Suppose T_i := {f(â) > t} and T_j := {f(b̂) < t} had masses > β_i and > β_j. Choose the other worlds' sets arbitrarily, and let x ≠ 0 be a common point, x = ∫_{T_i} aρ dπ_i = ∫_{T_j} aσ dπ_j. Then (f − tψ)(x) = ∫_{T_i} ψ(a)(f(â) − t)ρ dπ_i > 0, because x ≠ 0 forces ρ ≢ 0. Computed on the world-j side the same quantity is < 0. Contradiction.
2. **(a).** Lemma 3.2.
3. **(a′).** The atom found for (i, j) and the one found for (i, k) both have mass > β_i at i. They coincide by the uniqueness clause.
4. **(b).** The atom set Z_i is admissible as T_i, since 2θ_i − 1 > 1 − θ_i. Its cone is ℝ₊z. Use T_i = Z_i together with any T at world k: the common nonzero point lies in ℝ₊z ∩ cone(T).
5. **(c).** A second ray carrying mass > β would be a blocking set whose cone misses z, contradicting (b). ∎

*Remarks.*
- **Thresholds.** Exactly as in NN2: θ > 1/2 already forces positive-mass coincidence at every pair of worlds. θ > 2/3 turns it into a blocking set common to all worlds. The finite statements are the special case of uniform π on n points, where 1 − 2β = (2q − n)/n.
- **Answer to the requested alternative.** No atomless judge distribution satisfies the local intersection conditions. Theorem 3.3(a) produces a profile atom of mass ≥ 2θ − 1 from the hypothesis alone.
- **The arc example.** Profiles spread on an arc with a density are separated by an explicit linear f with t at the common median, using blocking sets of mass 1/2 at both worlds (`quantile_check.out` Part 2). More generally, for atomless P and Q, any t between their medians separates with masses ≥ 1/2 > β.

**Remark 3.4 (why the centrepoint hope fails; PROVED).** The memo's hook (DESIGN_MEMO §2A) was "one common direction in every blocking cone, carrying zero judge mass".
- **The one-world condition is a depth condition.** For one world and a fixed z, z ∈ cone_π(T) for all T with π(T) > β iff every open half-space {f > f(z)} has mass ≤ β. Equivalently, the Tukey depth of z under law(â) is ≥ 1 − β = θ.
- **Atomless laws are too shallow.** If law(â) has no atom at z, Lemma 3.1 gives a hyperplane through z of mass 0, so depth(z) ≤ 1/2 < θ.
- **What the centrepoint theorem gives.** It guarantees depth 1/(d+1), far below θ.
- **The link to no ties.** The inequality θ > 1/2 that makes A tie-free is the same inequality that forces the atom.

### 3.2 From (QS_θ) to the hypothesis, with no alignment step

For a continuum of judges, MM2's alignment (Theorem 3.1) would need an infinite-dimensional separation, and possibly finitely additive weights. I bypass it by building the swap rival directly.

**Definition (admissible essential point).** Let C be a model and (a, b) an advice type. A point h₀ is an admissible essential point of C if:
- **(E1) Both sides have positive lower density.** A′ := {a_C = a, b ∈ A(h)} and B′ := {a_C = b, a ∈ A(h)} both have positive lower μ-density at h₀.
  - This holds, for example, at relative-interior points of a boundary that is locally a Lipschitz graph, for Gaussian μ. All boundary points of D_K off the coordinate axes qualify.
- **(E2) Lebesgue points.** At each world, h₀ is a Lebesgue point of the switch map f_iv := ℓ_iv(·, b) − ℓ_iv(·, a), for π_i-a.e. v. Its Lebesgue value is y_iv(h₀).
  - By (M) and Fubini, μ-a.e. h₀ satisfies (E2).

**Proposition 3.5 (measure multi-site swap; PROVED).**
- **Setting.** Let h_1, …, h_m be distinct admissible essential points of C = C_p, of types (a_k, b_k). Let λ ∈ ℝ^m and z_iv := Σ_k λ_k y_iv(h_k).
- **Hypothesis.** At every active i, π_i{v : z_iv < 0} > β_i.
- **Conclusion.** There is X ≠ C_p with π_i{Δ_iv(p, X) < 0} > β_i at every active i. So (QS_θ) fails at p.

*Proof.*
1. **Shrink to a uniform set.** Since the mass inequality is strict, choose ζ > 0 and B′_i ⊆ {z_iv ≤ −ζ} on which (E2) holds at every h_k, with π_i(B′_i) > β_i.
   - Put ε_v(ρ) := max_k sup_{ρ′ ≤ ρ} μ(B(h_k, ρ′))⁻¹ ∫_{B(h_k, ρ′)} |f_v − y_v(h_k)| dμ.
   - This is measurable in v, nondecreasing in ρ, and tends to 0 for each v ∈ B′_i.
   - Egorov gives B″_i ⊆ B′_i, still with π_i(B″_i) > β_i, on which sup_v ε_v(ρ) → 0.
2. **The sets.** Let c > 0 be a common lower density from (E1). For small m > 0 put E_k := A′_k ∩ B(h_k, ρ_k) if λ_k > 0, and E_k := B′_k ∩ B(h_k, ρ_k) if λ_k < 0. Choose ρ_k by continuity so that μ(E_k) = m|λ_k|. Then ρ_k → 0 as m → 0, and the E_k are disjoint.
3. **The rival.** X switches a_k → b_k on E_k ⊆ A′_k and b_k → a_k on E_k ⊆ B′_k.
4. **Increments.** Δ_iv = Σ_k sgn(λ_k)∫_{E_k} f_v = m z_iv + error, with |error| ≤ Σ_k ε_v(max ρ) μ(B(h_k, ρ_k)) ≤ (m/c) Λ sup_{B″} ε, where Λ := Σ_k|λ_k|.
5. **Conclusion.** For m small, Δ_iv ≤ m(−ζ + o(1)) < 0 on B″_i. ∎

**The point of this proof.** Uniformity in v is never assumed. The strict inequality "mass > β" in Lemma 1.1 leaves room to discard a small mass of badly behaved judges (Egorov).

**Theorem 3.6 (edge collapse for A; PROVED).**
- **Setting.** Let p have exactly two active worlds i and j (an edge index; in the two-world setting, every interior index). Let (QS_θ) hold at p, and let h_1, …, h_m be admissible essential points of C_p.
- **(a) Opposite signs.** For each k, y_iv(h_k) and y_ju(h_k) have opposite signs (for a.e. v, u). Within a world the sign is common, by guidance.
- **(b) A common atom.** Put a_v := (|y_iv(h_k)|)_k and b_u := (|y_ju(h_k)|)_k, normalised by the first coordinate. There is z ∈ ℝ^m_{>0} with π_i{â = z} ≥ 2θ_i − 1 and π_j{b̂ = z} ≥ 2θ_j − 1. It is the unique point of mass > β.
- **(c) Countably many points at once.** For any countable set D of admissible essential points, there are Z_i ⊆ V_i and Z_j ⊆ V_j with π_i(Z_i) ≥ 2θ_i − 1 > β_i and π_j(Z_j) ≥ 2θ_j − 1 > β_j. All members of Z_i ∪ Z_j have positively proportional switch magnitudes on D, with one common profile.

*Proof.*
1. **(a).** If both worlds had sign s at h_k, then λ = −s·e_k makes z < 0 for every judge, and Proposition 3.5 applies.
2. **Reduction to (H1).** Let s_k be world i's sign at h_k. A rival with λ_k := s_k(f_k − tδ_{k1}) has z_iv = ψ(a_v)(f(â_v) − t) and z_ju = −ψ(b_u)(f(b̂_u) − t). So Proposition 3.5 turns any violation of (H1) into a failure of (QS_θ).
3. **(b).** Lemma 3.2.
4. **(c).** Enumerate D and let Z^{(m)} be the atom set for the first m points. The atom for m + 1 points restricts to an atom of mass > β for the first m points. By uniqueness it is the m-point atom, so Z^{(m+1)} ⊆ Z^{(m)}. Continuity from above gives (c). ∎

**Corollary 3.7 (atomless boundary laws fail; PROVED).** At an edge index, suppose that for some two admissible essential points h_1, h_2 the law under π_i of the switch ratio |y_iv(h_2)|/|y_iv(h_1)| has no atom of mass ≥ 2θ_i − 1. This holds in particular if the law is atomless. Then (QS_θ) fails at p.

**Corollary 3.8 (NN2 Corollary 4.2 for A; PROVED).** At an edge index p, let Γ ⊆ ∂C_p be a relatively open set of admissible essential points on which every judge's switch map is continuous. Suppose no set of world-i judges of positive mass has pairwise constant switch ratios on Γ. Then (QS_θ) fails at p.

*Proof.* Apply Theorem 3.6(c) with D countable and dense in Γ, and use continuity. ∎

### 3.3 Scope

- **What is proved here.** Theorem 3.3 is the measure form of NN2 Theorem 2.3 and NN1 Lemma 2.1. Theorem 3.6 and its corollaries are the measure form of NN1 Theorem 3.2 / Corollary 3.3 and NN2 Corollary 4.2.
- **What is expected to transfer (CONJECTURE, routine, not re-derived here).** The other finite exclusions use the abstract lemma only through (a)–(c): NN2 Corollaries 3.1–3.4 and Theorem 4.1, and NN1 Corollaries 4.2–4.3. I expect them to transfer with "b-set" read as "mass > 1 − θ" and "n − 2b + 2" read as "2θ − 1", with Proposition 3.5 replacing alignment.
- **What does not transfer.** The interior sum form with three active worlds (NN2 §6) is outside the collapse for finite quorums, and it stays outside here. Nothing in this note gives A an advantage there either.
- **Inherited gap.** The plane-wise constants of NN2 Observation 5.1 are inherited unchanged.

---

## 4. The two-world target (Q3): an explicit obstruction at D_{K*} and nearby interval models

**Setting.** There are two worlds. Problems are pairs {g, −g}, g ∈ ℝ², with Gaussian μ, which is uniform in angle. Let K = {m : m_1 ∈ [α, β]} with 0 < α < β < 1.
- **The model.** D_K = {g : αg_1 + (1−α)g_2 ≥ 0, βg_1 + (1−β)g_2 ≥ 0}. It accepts g on D_K, accepts −g on −D_K, and is silent otherwise.
- **The two boundary rays.** R1 = (1−α, −α) and R2 = (−(1−β), β). Across each ray the switch is accept ↔ silence, and both sides have density 1/2.
- **Rank changes for silence → accept g just outside D_K:**
  - at R1: −1 at world 1, +1 at world 2;
  - at R2: +1 at world 1, −1 at world 2.

  These were CHECKED for K ∈ {[1/3, 2/3], [3/10, 7/10], [2/5, 3/5], [1/4, 1/2], [1/3, 1/2]}.
- **Switch magnitudes.** Write κ_iv(R) > 0 for judge v's switch magnitude at R: its approximate density times the rank step. Put ρ_iv := κ_iv(R2)/κ_iv(R1).

**Proposition 4.1 (PROVED; CHECKED `dkstar_rival.out`).**
- **The rival.** Let X switch silence → accept g on a thin sector just outside D_K at R1, of mass m·t, and on one at R2, of mass m.
- **Increments, up to o(m) uniformly on a set of judges whose mass is as close to 1 as needed (Proposition 3.5):**
  - Δ_1v = m(κ_1v(R2) − t κ_1v(R1)) ≤ 0 iff ρ_1v ≤ t;
  - Δ_2u = m(t κ_2u(R1) − κ_2u(R2)) ≤ 0 iff ρ_2u ≥ t.
- **The mirror rival** (accept g → silence just inside D_K) gives the reversed inequalities.
- **Hence**, (QS_θ) at C_p = D_K against these rivals holds iff some c has π_i{ρ_i < c} ≤ 1 − θ_i and π_i{ρ_i > c} ≤ 1 − θ_i at both worlds (Lemma 3.2 in dimension 1). This forces π_i{ρ_i = c} ≥ 2θ_i − 1 at both worlds.

**Explicit atomless family (CHECKED, exact).**
- **Judges.** Judges are cellwise constant near the rays, with κ_iv(R1) = 1 and κ_iv(R2) = 1 + v, where v ~ U[0, 1] at both worlds.
- **The rival.** Take t = 3/2, that is, sector masses 3m/2 and m.
- **The blocking sets.** Every world-1 judge with v ≤ 1/2, and every world-2 judge with u ≥ 1/2, weakly prefers X. Each set has mass 1/2 > 1 − θ.
- **Conclusion.** D_K is not competitive against X at either world, for every θ > 1/2.
- **Different ratio laws** (ρ_1 = 1 + v², ρ_2 = 3/2 + u/2, or a nearly constant ρ_2) give blocking masses ≥ 0.625.
- **The same rival works for all five interval models.**

**Conclusion for Q3.**
- **The obstruction (PROVED).** No family of judges whose boundary switch-ratio law is atomless can certify D_{K*}. The same holds for any non-degenerate interval model [α, β] selected at an interior index. With radius-dependent judges, essential points at several radii add coordinates to the profile, and the condition only becomes stronger (Theorem 3.6(c)).
- **What can pass this local test.** Judges with a coincident bloc of mass ≥ 2θ − 1 sharing one ratio c(p), and fringes of mass ≤ 1 − θ on each side.
- **What that amounts to.** On ∂C_p the committee is then one score at one exchange rate: the finite-quorum situation. Whether such a family through D_{K*} passes the full test is the open quorum question, with the plane-wise constants gap of NN2 Observation 5.1. It is not a new freedom of A.

---

## 5. Status table

| Item | Status |
|---|---|
| (IB), strict (G), no ties (θ > 1/2, ψ > 0), (TC) (θ > 2/3), direct (C), admissibility | PROVED |
| Closed sections (reverse Fatou; joint measurability only) | PROVED |
| Strict cycles iff k ≥ ⌈1/(1−θ)⌉ (≥ 4) | PROVED; CHECKED |
| Lifting: strict signs at exactly θ do not lift | PROVED; CHECKED |
| Lifting under (U2), common envelope | PROVED (short) |
| Lemma 3.1 generic projection | PROVED |
| Lemma 3.2 measure median lemma (atom ≥ 1 − 2β) | PROVED; CHECKED (1-D) |
| Theorem 3.3 measure blocking-cone collapse | PROVED |
| Remark 3.4 Tukey-depth explanation | PROVED |
| Proposition 3.5 measure swap (Egorov, strict mass slack) | PROVED |
| Theorem 3.6 / Corollaries 3.7–3.8 edge collapse for A | PROVED |
| Transfer of the remaining finite exclusions | CONJECTURE (routine) |
| Proposition 4.1 and the explicit rival at D_{K*} and nearby models | PROVED; CHECKED |
| **Screen S3** | **FAILS** |
