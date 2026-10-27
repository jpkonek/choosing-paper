# MM3 referee (round 41, BRIEF33): the strict-sign lifting lemma, the fixed-margin exclusion, and LL3's certificate

18 Oct 2026. Independent referee. Labels:
- **PROVED**: the argument is written or re-derived here, line by line. One reader (me).
- **CHECKED**: exact rational computation in `mm3py/mm3_check.py` → `mm3_check.out` (112 checks, `ALL CHECKS PASSED`; run `python3 -I mm3_check.py` inside `mm3py/`). I wrote it from the text of LL3, not from LL3's scripts. I also reran `ll3py/{foundations,geometry,certificate}.py`; the outputs are byte-identical to the stored `.out` files. I reran `ll1py/*.py` and `ll2py/{gap_check,swap_T1}.py`; their verdicts agree with the stored outputs.
- **CONJECTURE**, **NUMERICS**: none used.

No assumption is added. Every hypothesis below belongs to a stated result.

---

## 0. Verdicts

| Item | Verdict |
|---|---|
| (1) Strict-sign lifting lemma, (QS) ⟺ some ψ-rule makes every C_p competitive | **Correct** (PROVED). Small presentational repairs only (§1.6). |
| (1) Consequences for the ψ-rule: (IB), strict (G), no nontrivial ties, (TC), closed sections, direct (C), admissibility, T1 undominated, (LA) | **Correct** (PROVED). The quorum hypotheses are 2q > n for ties, (C) and admissibility, and 3q > 2n for (TC). Strict (G) needs ψ(s) ≤ s. Closed sections need ψ continuous. |
| (1) Exact 216-branch test and the uniqueness certificate (AUDIT_LL) | **Correct** (PROVED). The certificate is sufficient, and correctly not claimed to be necessary. |
| (2) LL1 Lemma 2.1, Thm 3.1, Cor 3.2, Lemma 4.2a, Lemma 4.1, Thm 4.2 | **Correct** (PROVED). |
| (2) LL2 Lemma 2.1, Lemma 3.1, Lemma 3.2, Prop 4.1, Thm 5.1 (Sierpiński), Prop 6.1 | **Correct** (PROVED). Repair: Cor 6.2 needs a one-line amendment for precise K (§2.3). |
| (2) Scope of the exclusion | Selections continuous in measure: excluded for **every** n and every q ≥ 1. Selections with closed sections only: excluded when there are **no nontrivial ties** (2q > n, or a proper weighted game). See §2.4. |
| (3) LL3 §3.5 eight-comparison certificate out of A = C_(17/50,33/100,33/100) and B = C_(33/100,17/50,33/100) | **Correct** (re-derived; CHECKED). The scope caveat of BRIEF33 stands: A and B are coherent **candidate** models, not models proved selected in a full covering system. |
| (3) LL3 Thm A (Nakamura conditions), Cor B1′ (M\*), Thm B2, Thm B3, Cor B3′ | **Correct with one repair.** The wording of the (TC) counterexample in Thm A(b) is ambiguous and needs one specific mass choice (§3.3). The certificate and Thm A are about the fixed-margin rule. Their transfer to the ψ-rule is stated in §3.5. |

**New observations (PROVED):**
- R1 (§1.5). If a coherent family through two distinct vertex models satisfies (QS), then liminf_{s↓0} δ(s)/s = 0. Hence every working ψ has liminf ψ(s)/s = 0.
- R2 (§1.5). For the ψ-rule on the full domain with 0 < ψ(s) < s and ψ continuous, closed sections together with competitiveness of coherent selected models force continuity in measure. So the continuity hypothesis in (QS) costs nothing in this class.
- R3 (§3.5). Theorem A transfers to the ψ-rule. In particular strict 4-cycles occur for (n, q) = (4, 3). The LL3 certificate is accepted by any ψ-rule at scales where ψ(x) ≤ 3x/29, and by R1 such scales exist for every working ψ.

---

## 1. The strict-sign lifting lemma

### 1.1 Setting (as in AUDIT_LL; AUDIT_LL's "menu domain" is the write-up's decomposable domain)

- **Worlds and judges.** There are finitely many worlds. At world i there are judges v = 1, …, n. Judge iv has a measurable penalty ℓ_iv(h, a), defined for a ∈ A(h). It is strictly increasing in world-i rank on A(h) for a.e. h, and it has an integrable envelope g: |ℓ_iv(h, a)| ≤ g(h).
- **Measure and domain.** μ is finite and atomless. The domain M is a decomposable domain with advice range A(·). Equivalently, M is the class of all models whose advice is a.e. a measurable selection of A (write-up Remark 2.1). The full domain is the case A ≡ {+, 0, −, ×}.
- **Quorum.** There is a quorum q with 3q > 2n. Hence q > 2n/3 ≥ n/2, so 2q > n.
- **Selection.** p ↦ C_p is a coherent selection on Δ, continuous in measure.
- **Notation.** Δ_iv(p, X) = L_iv(X) − L_iv(C_p) and d_iv(p, X) = ∫ |ℓ_iv(h, a_X) − ℓ_iv(h, a_{C_p})| dμ. D = max_iv d_iv, b_i is the q-th largest of the n numbers Δ_iv, and r(p, X) = max_{i∈supp p} b_i. Every |Δ| and every d is at most M := ∫ 2g dμ. We may take M > 0.

Strict guidance gives distinct penalties to distinct advices in A(h), for a.e. h. So d_iv(p, X) > 0 for every judge (i, v) whenever X ≠ C_p mod null. Also r(p, X) > 0 holds iff some active world has at least q judges with Δ_iv > 0. So (QS) ⟺ r > 0 on every X ≠ C_p. ✓

### 1.2 Necessity (PROVED)

Suppose the ψ-rule makes C_p competitive, and let X ≠ C_p.
- Some i ∈ supp p has q supporters.
- Each supporter has Δ_iv ≥ ψ(d_iv), and ψ(d_iv) > 0 because d_iv > 0.

This is (QS). It uses only ψ > 0 on (0, M]. Neither continuity nor monotonicity is needed. ✓

### 1.3 Sufficiency, line by line (PROVED)

**(a) Uniform transfer from C_{p_k} to C_p.** Fix any X. Pointwise, the reverse triangle inequality gives

  | |ℓ(a_X) − ℓ(a_{C_{p_k}})| − |ℓ(a_X) − ℓ(a_{C_p})| | ≤ |ℓ(a_{C_{p_k}}) − ℓ(a_{C_p})| ≤ 2g · 1{a_{C_{p_k}} ≠ a_{C_p}}.

Hence
- |d_iv(p_k, X) − d̃_iv| ≤ ∫_{E_k} 2g dμ, where d̃_iv is d computed against the base C_p;
- |Δ_iv(p_k, X) − Δ̃_iv| = |L_iv(C_p) − L_iv(C_{p_k})| ≤ ∫_{E_k} 2g dμ;

where E_k = {a_{C_{p_k}} ≠ a_{C_p}}. The bound does not involve X. Continuity in measure gives μ(E_k) → 0, and absolute continuity of ∫ g then sends the bound to 0. So the transfer is uniform in X. ✓

**(b) Compactness of the attainable set.** Put c(h) := a_{C_p}(h), and

  φ(h, a) := ( ℓ_iv(h, a) − ℓ_iv(h, c(h)), |ℓ_iv(h, a) − ℓ_iv(h, c(h))| )_{i,v} ∈ ℝ^{2N}.

Here N is the total number of judges.
- **A finite-valued correspondence.** For each fixed a, φ(·, a) is a measurable finite vector. The absolute value is just another measurable function of (h, a), so it causes no difficulty. The correspondence Φ(h) := {φ(h, a) : a ∈ A(h)} has at most four points. Its graph is measurable, because A is measurable.
- **Integrably bounded.** Every coordinate of Φ is bounded by 2g.
- **Selections are models.** Every integrable selection σ of Φ has the form φ(h, s(h)) for a measurable selection s of A: pick the first a in a fixed order with φ(h, a) = σ(h). So s is the advice of an evaluable model X_s ∈ M.
- **Hence A_p = ∫Φ dμ.** The attainable set A_p := {(Δ̃, d̃)(X) : X ∈ M} is the Aumann integral of Φ.
- **Convex and compact.** On an atomless finite measure space, the Aumann integral of a closed-valued, integrably bounded, measurable correspondence into ℝ^m is convex and compact (Aumann 1965, Thms 1 and 4). Equivalently, ∫Φ = ∫co Φ, the relaxed integral, by Lyapunov purification.

So a limit of attainable vectors is attained by an actual model. ✓

**(c) δ(a) > 0.** Suppose not. Then there are p_k, X_k with D(p_k, X_k) ≥ a and r(p_k, X_k) → 0. Pass to a subsequence with p_k → p.
- By (a), the vectors z_k of (p_k, X_k) satisfy |z_k − z̃_k| → 0, where z̃_k ∈ A_p.
- By (b), a further subsequence gives z̃_k → z* = (Δ*, d*) ∈ A_p, realised by some X*. Then z_k → z* as well.
- max d* ≥ a > 0, so X* ≠ C_p.
- By (QS) at p, some i ∈ supp p has q judges with Δ*_iv > 0. Let c > 0 be the least of these q values.
- **Supports.** p_{k,i} → p_i > 0, so i ∈ supp p_k for all large k. This is the right direction: the limit's support is contained in the eventual supports. So the defending world is active along the sequence.
- **Contradiction.** For large k those q increments of (p_k, X_k) exceed c/2. So r(p_k, X_k) ≥ b_i(p_k, X_k) ≥ c/2, contradicting r(p_k, X_k) → 0. ✓

δ is nondecreasing, because the feasible set shrinks as a grows. δ(a) ≤ M where the set is nonempty, and δ = +∞ where it is empty. Put δ̃ := min(δ, M), which is positive and nondecreasing on (0, M]. ✓

**(d) Construction of ψ.** Put γ(s) := ½ min(δ̃(s), s) on (0, M], and optionally also take the minimum with s²/M, or with κ̲(s) := min_{t∈[s,M]} κ(t) for a prescribed positive continuous cap κ. Each of these is positive and nondecreasing. Two explicit constructions work.
- **Averaging (simpler than the audit's grid).** ψ(s) := (1/s)∫₀^s γ(t) dt and ψ(0) := 0.
  - ψ is continuous on (0, M].
  - It is nondecreasing, because the running average of a nondecreasing function is nondecreasing.
  - It is positive.
  - ψ(s) ≤ γ(s) ≤ s/2 → 0, so ψ is continuous at 0.
  - With the s²/M option, ψ(s)/s ≤ s/(2M) → 0. With the cap option, ψ ≤ κ.
- **Dyadic grid (the audit's construction).** Put s_k := M2^{−k}, c_0 := γ(s_1) and c_k := min(c_{k−1}, γ(s_{k+1})). Interpolate linearly on [s_{k+1}, s_k] and set ψ(0) = 0.
  - On [s_{k+1}, s_k], ψ ≤ c_k ≤ γ(s_{k+1}) ≤ γ(s).
  - c_k ↓ 0 because γ(s) ≤ s/2.

Either way, ψ is continuous and nondecreasing with ψ(0) = 0 and 0 < ψ(s) ≤ s/2 < s. Moreover ψ(s) ≤ δ̃(s)/2 < δ(s) wherever δ is finite. ✓

**(e) Competitiveness.** Let X ≠ C_p and D := D(p, X) > 0. Then (p, X) lies in the feasible set at level D, so r(p, X) ≥ δ(D). Some active i has q judges with

  Δ_iv ≥ δ(D) > ψ(D) ≥ ψ(d_iv),

using d_iv ≤ D and monotonicity of ψ. The identity comparison has Δ = d = 0 = ψ(0) and all votes. ✓

**Verdict on the lemma: correct.** Clean statement in §4.

### 1.4 Consequences for the ψ-rule (PROVED)

The rule: judge iv supports X R_i Y iff L_iv(Y) − L_iv(X) ≥ ψ(d_iv(X, Y)), and X R_i Y is accepted iff at least q judges at world i support it. Throughout, ψ is continuous and nondecreasing, ψ(0) = 0, and 0 < ψ(s) ≤ s.

- **Reflexive.** The identity has n votes.
- **(IB).** Take the models (D∩A)∪F and (E∩A)∪F, with A = −A and F ⊆ A^c. They agree on A^c, so both increments and both gross changes are integrals over A of quantities fixed by D and E. They do not change when F is replaced by G. ✓
- **Strict (G).** Let X be at world-i at least as good as Y a.e.
  - Every judge then has L(Y) − L(X) = d(X, Y) ≥ ψ(d). This **needs ψ(s) ≤ s**. So all n judges support X R_i Y.
  - If X is strictly better on a non-null set, then d > 0. For the reverse, L(X) − L(Y) = −d < 0 < ψ(d), so no judge supports Y R_i X.
  - So X is strictly ranked above Y. ✓
- **No nontrivial ties.** Let X ≠ Y. A judge supporting both directions would have Δ ≥ ψ(d) > 0 and −Δ ≥ ψ(d) > 0, which is impossible. The two coalitions of supporters are therefore disjoint. Two q-sets intersect when 2q > n. ✓
- **(TC)** (BRIEF28: A ⪯ B ⪯ C ⇒ ¬(C ≺ A)).
  - *Distinct models.* Every vote on an edge between distinct models has Δ ≥ ψ(d) > 0. A judge supporting all three edges of X R Y, Y R Z, Z R X would have strictly increasing loss around the triangle, which is impossible. So each judge supports at most two edges.
  - *Counting.* The three accepted edges need 3q votes, but at most 2n are available. Since 3q > 2n, this is a contradiction. In fact this excludes every 3-cycle of R, not just the forbidden pattern.
  - *Repeated models.* If X = Y, then Y R Z gives X R Z, which contradicts Z ≺ X. If Y = Z, then X R Y contradicts Y ≺ X. X = Z is excluded by reflexivity.
  - The ψ-version goes through because only ψ(d) > 0 for d > 0 is used, and no linearity. ✓
- **Closed sections.** Fix any evaluable X: an arbitrary model, a selected C_{p′}, or C_p itself. By §1.3(a), p ↦ Δ_iv(C_p, X) and p ↦ d_iv(C_p, X) are continuous. Since ψ is continuous, each vote set {p : Δ − ψ(d) ≥ 0} is closed. The section is a finite union, over q-sets, of finite intersections of these sets, so it is closed.
  - At points with C_p = X, the same continuous function vanishes. Nothing special happens there.
  - Non-injectivity of the selection plays no role, since sections are preimages. ✓
- **Direct (C).** A tie at even one world forces X = C (no nontrivial ties). ✓
- **Selected admissibility.** Suppose Y ≠ C_p dominates C_p. Then Y R_i C_p at every world, so by no-ties ¬(C_p R_i Y) at every world. This contradicts competitiveness on supp p ≠ ∅. ✓
- **(LA), (S), T1.** (LA) holds since C_p ∈ C_L. (S) holds by §1.3 and closed sections. T1 = C_{p₀} is coherent and undominated, so T1 ∈ C_L. (LF) at T1 is trivial on the full domain, and is a hypothesis on the domain otherwise.
- **(FC) fails in general.** See §3.5. "No (FC) claim" is the correct wording.

So **(QS) for a coherent family through T1, continuous in measure, gives a cover of T1 under (TC)** in the write-up's sense, with reflexive (TC) relations in place of preorders. Theorem 2.1 of the write-up (KKM) is stated for preorders and is not used. ✓

### 1.5 Further consequences (PROVED)

**R1 (the advantage must be superlinearly small along some sequence).** Let the domain have W_1 ≠ W_2, which holds on the full domain or with (LF) at T1 (LL2 Lemma 5.0). If a coherent family, continuous in measure, satisfies (QS), then liminf_{s↓0} δ(s)/s = 0. Every common ψ that works must also satisfy liminf_{s↓0} ψ(s)/s = 0.
- *Proof.*
  - Suppose δ(s) ≥ cs on (0, s₀] with c > 0. Put ψ(s) := ½ min(c, 1)·min(s, s₀).
  - Then ψ ≤ δ̃/2: for s ≤ s₀ this follows from δ(s) ≥ cs, and for s > s₀ from monotonicity of δ. Also ψ ≤ s/2.
  - By §1.3(e), the ψ-rule makes every C_p competitive. It is linear near 0 for every judge, so it satisfies (E_i) at every world (LL2 instance (iii)).
  - LL2 Theorem 5.1(a) then forbids continuity in measure, which is a contradiction.
  - The ψ claim is LL2 Cor 5.2, third bullet, read for a common ψ. ∎
- *Reading.* The mirror-swap records of LL1 Lemma 2.1 must still be won **by sign**: a quorum must see a strictly positive second-order increment. They cannot be won by any margin proportional to d.
- By LL1 Thm 3.1(b), applied to the defending relation "some quorum strictly positive", a continuous family through W_1 ≠ W_2 contains models with such swap points. This does not refute (QS). It locates where (QS) must be checked hardest.

**R2 (continuity is automatic for coherent ψ-covers on the full domain).** Assume the full domain, ψ continuous with 0 < ψ(s) < s, and 2q > n. Let p ↦ C_p be coherent, with closed sections and each C_p ψ-competitive on supp p. Then the selection is continuous in measure.
- *Proof.* LL1 Lemma 4.1 goes through with ψ in place of ηd:
  - In step 2, Δ(C*, X_E) − ψ(d(C*, X_E)) = d − ψ(d) > 0, which uses ψ(s) < s. The limits use continuity of ψ.
  - In step 4, Δ ≥ ψ(d) and −Δ ≥ ψ(d) give ψ(d) = 0, so d = 0.
  - Then apply Lemma 4.2a (coherent models are compact) and the closed-graph theorem, exactly as in LL1 Thm 4.2. ∎
- The lifting lemma's ψ has ψ ≤ s/2 < s.

### 1.6 Repairs to the presentation (no mathematical change)

1. **Terminology.** "Full measurable menu domain" should read "decomposable domain (for instance the full domain)". The proof uses only Remark 2.1 of the write-up.
2. **Two different bounds.** The theorem states 0 < ψ(s) ≤ s, but the construction gives ψ ≤ s/2. Strict (G) needs only ψ ≤ s. R2 and the transfer of Theorem A in §3.5 use ψ(s) < s, or ψ(s) ≤ cs with c < 1, so state the s/2 bound.
3. **Empty feasible sets.** Where the feasible set is empty, say "δ := +∞, and use δ̃ := min(δ, M)".
4. **Quorum hypotheses.** The consequences need 2q > n (ties, (C), admissibility) and 3q > 2n ((TC)). Both follow from 3q > 2n.
5. **Domain hypothesis.** For a cover on a decomposable domain other than the full domain, (LF) at T1 must be assumed of the domain.

### 1.7 The exact branch test (AUDIT_LL) (PROVED)

For n = 4 and q = 3, "fewer than 3 judges with Δ > 0" is equivalent to "at least 2 judges with Δ ≤ 0". So (QS) fails at p iff some X ≠ C_p and pairs F_i (i ∈ supp p) have Δ_iv ≤ 0 on F. At full support there are 6³ = 216 branches. ✓
- **Branch criterion.** A branch passes iff A_p ∩ {Δ_F ≤ 0} = {0}. Here 0 is the full vector: d = 0 forces X = C_p, and |Δ| ≤ d. ✓
- **Optimisation form.** The intersection is compact and convex, so max Σd over it is attained. It is 0 iff the branch passes. Points of A_p are realised by models (§1.3(b)), so this is exact, not a relaxation. ✓
- **Uniqueness certificate.** Suppose some w ≥ 0, w ≠ 0, on F has C_p as unique minimiser of Σ_F w L. Then every X ≠ C_p has w·Δ_F > 0, so some branch increment is positive. This is sufficient. It is not necessary in general, because a convex set can touch the orthant only at 0 without an exposing functional that is strictly positive off the identity. Not claiming necessity is correct. ✓
- **LL2 Prop 8.3 is weaker.** It separates A_p from the **open** orthant {Δ_F < 0}. So it is necessary only, as BRIEF33 correction 3 says. ✓

---

## 2. The fixed-margin exclusion

### 2.1 LL1

- **Lemma 2.1 (mirror swap). Correct.**
  - Set r < η_* y_*/(1 + η_*). Since η ↦ η/(1+η) is increasing, this gives r(1 + η_iv) ≤ η_iv|y_iv| for every (i, v).
  - The pointwise bounds |δ − y| < r on E_A ∪ E_B give |Δ_iv| < 2rm and d_iv > 2m(|y_iv| − r). These are strict on non-null sets.
  - Then Δ < 2rm ≤ η·2m(|y| − r) < ηd. ✓ Only (Q1) and η_iv > 0 are used.
- **Thm 3.1. Correct.**
  - *(a).* The pigeonhole step uses finitely many advice pairs and monotonicity in r. The 2-Lipschitz map Λ ↦ δ^{ab} = Λ_b − Λ_a carries common essential values to common essential values. Nonzero entries follow from y ∈ Y\*\*. Lindelöf supplies a countable cover.
  - *(b).* A clopen subset of a compact metrisable K is a finite union of basic open sets, so there are countably many patterns. Also d_K(c_C, c_D) = μ(Λ^{-1}K ∩ {a_C ≠ a_D}) ≤ ϱ(C, D). A countable pseudometric space has no connected subset of positive diameter.
  - *σ-compactness of G.* G ∩ {|y| ≤ m, all relevant entries ≥ 1/m} is a closed bounded subset of Y\*\*. ✓
- **Cor 3.2. Correct.**
  - At e_i, a world-i improvement X has Δ = −d < 0 < ηd for every judge, so C_{e_i} = W_i.
  - On the full domain W_1 ≠ W_2 on {f ∈ H : f_2 < 0}. Note that on H = {f_1 > 0}, W_1 is "+ everywhere".
  - The decomposable-domain remark, using label-matched swaps and (LF) for W_1 ≠ W_2, is correct. ✓
- **Lemma 4.2a. Correct.** Suppose P_K(g) = 0 at an interior point of {P_K ≥ 0}. Then P_K(g − t𝟙) = −t < 0 for small t > 0, a contradiction. So {P_K = 0} lies in the boundary of a convex cone, which is null. Dominated convergence and Blaschke compactness of credal sets finish the proof. ✓
- **Lemma 4.1. Correct.**
  - *Step 2.* × is worst at every world, so Δ(C*, X_E) = d > 0 for every world-i judge. Continuity in measure in the first argument puts p_k in the section for large k. The section is closed, so p lies in it. Pass to the limit along X_{E_m} → C* with a recurring coalition.
  - *Step 3.* The limit is taken along a subsequence with fixed (i, J′). The world i need not be active at p; step 2 holds at every world.
  - *Step 4.* Properness, that is (Q2), gives a common judge. ✓
  - It needs the full domain, because × must be available. LL1 says so.
- **Thm 4.2. Correct.** A map into a compact metric space with closed graph is continuous. Then apply Cor 3.2(a). ✓
  - (Q2) can be weakened to properness of the game, which is what Step 4 actually uses.

### 2.2 LL2

- **Lemma 2.1. Correct.**
  - *Convexity.* Lyapunov applies to the 2|I_S|-dimensional measure, and decomposability makes the splice evaluable.
  - *Open orthant.* Exact Lyapunov scaling to tX keeps z(X_t) = t z(X) < 0 with small G, and (E_i) rejects X_t.
  - *Separation.* This gives α ≥ 0 with α·z ≥ 0 on Z.
  - *Pointwise form.* Switch on the measurable set P.
  - *Converse.* In the brief's class, any n − q + 1 judges form a blocking family (instance (iii) with s₀ = ∞). So the test is exact per branch. ✓
- **Lemma 3.1 (gap). Correct.**
  - |1 − t| < η(1 + t) ⟺ t ∈ (1/κ, κ).
  - Strictness uses a nonempty support and |Δ| > 0.
  - Model-dependent margins (Remark 4.2) enter only through min η. ✓
- **Lemma 3.2. Correct.** I re-derived A_1 ≤ ρ²R in both sign cases and the bound (ρ − 1)(1 + ρ²)R < η(1 + 1/ρ)R. For ρ = 1 + η/4 and η < 1, the left constant is < 0.641η and the right is ≥ 1.8η. The two-free-world failure (N, N, 1) / (N, N + 2, 1) gives 3/4 ≥ 0 on both sides; rerun output confirms. ✓
- **Prop 4.1 (countability). Correct.**
  - The pieces K_{P,m} are compact.
  - Ratio balls of half-width ρ^{1/2} give pairwise ratios in (1/ρ, ρ).
  - Each ball contains the weights of at most one model, and finitely many balls cover each piece. ✓
- **Thm 5.1. Correct.**
  - (a) A countable metric space with two points is disconnected.
  - (b) Closed sections at selected models, reflexivity and no nontrivial ties make the level sets P_k closed. A continuum is not a countable union of at least two pairwise disjoint nonempty closed sets (Sierpiński). Lemma 5.0 supplies the two values W_1 ≠ W_2. ✓
- **Prop 6.1. Correct.**
  - θ = η/3 < η/(1 + η) for η < 1.
  - Density-0 removal leaves non-null sets, since both sides have positive lower density.
  - |N| ≤ 2θm|δ| < 2η(1 − θ)m|δ| ≤ ηG. ✓

### 2.3 Repair in LL2 Cor 6.2 (not one of the items to referee; recorded for completeness)

The text says the switch at ∂D_K is + → 0. That holds when max_{m∈K} m·h₀ > 0. For a precise K = {m}, both h₀ and −h₀ lie on the boundary, and the switch is + → −. The corollary holds with "+ → 0 or + → −", by the same proof. Theorem 5.1 does not use 6.2.

### 2.4 Verdict on scope (PROVED)

**Clean statement.** Fix finitely many worlds, finitely many integrable strictly guiding judges per world, and margins η_iv ∈ (0, 1), which may depend on the world, the judge, or (LL2 Remark 4.2) the selected model. Each world uses a monotone family of winning coalitions not containing ∅: a q-of-n quota with any 1 ≤ q ≤ n, or a weighted game with any τ > 0. The domain is the full domain or any decomposable domain with W_1 ≠ W_2 (for instance with (LF) at T1).
- **(i) Continuous selections.** No selection, coherent or not, continuous in measure on Δ, has every C_p competitive on supp p. (LL1 Cor 3.2; LL2 Thm 5.1(a).) This holds for **every** q.
- **(ii) Closed sections.** If the game is proper (2q > n for quotas), so that there are no nontrivial ties, then no selection with closed sections at selected models has every C_p competitive on supp p. (LL2 Thm 5.1(b), any decomposable domain with W_1 ≠ W_2; LL1 Thm 4.2, full domain with coherent selections.) For improper games (2q ≤ n), (ii) is **not** proved. It is irrelevant to this round, which requires 3q > 2n.
- **(iii) Mixed margins.** (i) and (ii) extend to margin functions with ψ_iv(s) ≥ ηs near 0 on a blocking family at every world except at most one (LL2 Cor 5.2).

The headline "any quorum" is correct for (i), and must carry "with no nontrivial ties" for (ii). BRIEF33 correction 1 is right.

---

## 3. LL3: the certificate and the general (n, q)/ν statements

### 3.1 The eight-comparison certificate (re-derived; CHECKED in `mm3_check.out` Part 1)

**Geometry.** ε = 3/10 and world 1. On mixed g, C_p accepts g iff φ_p(g) := c₀Σp_jg_j + ε min_j p_jg_j > 0.
- **Lipschitz bound.** I used the exact sup-norm Lipschitz constant c₀Σp + ε max p ≈ 0.335, rather than LL3's bound of 1.
- **The R_AB box** (centre g_AB, radius 59/300000):
  - φ_A(g) ≈ 1.28·10⁻³ and φ_A(−g) ≈ −4.6·10⁻², while the Lipschitz constant times the radius is ≈ 6.6·10⁻⁵. So A accepts g and not −g on the whole box.
  - φ_B(±g) < −3.9·10⁻⁴, so B is silent on the whole box.
- **The R_BA box (centre g_BA):** symmetric, with B accepting and A silent.
- **Both boxes:** they are mixed, have g_1 > 0, have every |g_j| above the radius, and are disjoint. ✓

**Records.** Pieces Q^X_{k,w} (k ≠ w) have mass 1 and R^X_w has mass 1/4, in units s. Judge v has density 2 on N^X_v and 1 elsewhere.
- **Votes.** For each of the eight records, every v ≠ k has (I, W) = (13/4, 4). Judge k has (13/2, 3) and dissents with W − I < 0. The supporters' (W − I)/(W + I) = 3/29 ≥ 1/16, so each record is accepted with exactly 3 votes. Every reverse comparison has ≤ 1 supporter. ✓
- **Net.** Every Q piece carries exactly one good → silence move (from the A-record or the B-record) and one silence → good move (from the other base's record), so its net is 0. Every R piece is improved once. So the summed loss change is −∫_{∪R}(ℓ(silence) − ℓ(good)) < 0 for **every** strictly guiding ℓ with finite integrals. For the four judges it is −1, −1, −1, −1 in units s.
- **Error indicators.** Only rank 0 and rank 1 moves occur, so the same combination is an (M1) obstruction for every positive error weight.
- **Regularity.** Only mixed problems change, so all X are regular. ✓

**Verdict: correct.** The certificate shows that coherence of the two bases alone gives no single endorsing field. It does not show non-endorsement inside a completed covering system: A and B are plain-posterior **candidates**, "selected in any cover that uses the plain posterior family", and nothing proves such a cover exists. This is BRIEF33 correction 2, which I confirm.

**Robustness claims.** These are LL3's `geometry.out`, rerun identically. The verification is by centre margins plus the Lipschitz bound, which is a valid proof for each listed instance.

### 3.2 Cor B1′, Thm B2, Thm B3, Cor B3′ (PROVED; arithmetic CHECKED, Part 3)

- **B1.** The ℓ\*-increment is f-superadditive on improvements and g-subadditive on worsenings. The chain ∫_PΔ\* ≤ Σ_{S₀} y I ≤ Σ y r W ≤ ∫_QΔ\* is correct, and so is the envelope bound. ✓
- **B1′.** Using 2q > n, top_q − bot_q = Σ_{j>q} x_j − Σ_{j≤n−q} x_j ≤ (n − q)(x_n − x_1). This gives M\* = 1 + 2qη/((n − q)(1 − η)). The table values 7/5, 4, 7, 55; 23/15, 5, 9, 73; 4/3, 7/2, 6, 46 are confirmed. ✓
  - LL2 Prop 7.1's threshold, about 1.2832 for the **sum** field, is smaller. This is consistent: LL3's ℓ\* is a min-of-sums field.
- **B2.** The counting identities hold:
  - #{D′ ⊆ D^c, |D′| = n − q} = C(q, n − q);
  - the number of those containing v is C(q − 1, n − q − 1);
  - c/N′ = r(1 + (M − 1)(n − q)/q) > 1 ⟺ M > M\*.
  - Two-copy layering: the worsening pieces have total mass N′b < a, so they fit inside the improvement piece of the other base's record. ✓
  - CHECKED for (n, q) ∈ {(4,3), (5,4), (7,5), (5,3), (6,5), (9,7)} and η ∈ {1/16, 1/3, 1/2, 9/10}: accepted at M\*(1 + 10⁻³), and (N′, c] is empty at M\*.
- **B3.** This combines Stiemke's alternative on the finitely generated cone V with Farkas on each Γ_S: Σr y z ≤ f_z ≤ y·z. (E) extends from the generators to K because g is subadditive and f superadditive. The realisation step lays each type's worsening inside its improvement, ball by ball. ✓
- **B3′.** The extreme rays of K_M are the z_A, ∅ ≠ A ⊊ [n]. The feasible y-families form a convex set invariant under permutations, so a symmetric family y^S = a𝟙_S exists if any does. The gap function in |A| decreases up to |A| = n − q and increases after. ✓

### 3.3 Theorem A (Nakamura conditions): correct with one repair (PROVED; formula CHECKED, Part 2)

- **(c) Cycles.**
  - Necessity: no judge supports every edge of a cycle of distinct consecutive models, by strict per-judge monotonicity.
  - Sufficiency: I verified the construction with masses r^{−((m − j(v) − 1) mod k)}. Judge v supports exactly the edges m ≠ j(v), with equality, and the reverse of edge j(v) only.
  - Strictness: the reverse supporters {j(v) = m} ⊆ S_m^c are losing in a proper game. ✓
- **(a) Ties.** The two-cell construction with masses 1 and 1/r is correct. ✓
- **(b) (TC).**
  - The reduction to S_1 ∩ S_2 losing is correct: under properness, at most one of the pairwise-disjoint pairwise intersections can be winning.
  - **Repair.** The phrase "judges in only one S_j get one margin-steep pair and equal masses otherwise" is ambiguous. With cells c_X, c_Y, c_Z, an S_2-only judge given m(c_X) = m(c_Y) = 1 and m(c_Z) = 1/r **supports X R Z**. That spoils the claim that the supporters of X R Z are exactly S_1 ∩ S_2.
  - A correct choice:
    - S_1-only: (m_X, m_Y, m_Z) = (1, 1/r, 1);
    - S_2-only: (1/r, 1, 1/r);
    - S_3-only: (1/r, 1/r, 1).
  - Each judge still supports its own steep edge, with equality in the margin. For X R Z the increment m_Z − m_X is 0, 0 and 1 − 1/r < 0 respectively, all below ηd, so none of these judges supports X R Z. The supporters of X R Z are exactly S_1 ∩ S_2, as required. (Extra supports of other edges, such as Z R Y by S_1-only judges, are harmless.) LL3's own CHECKED realisations of forbidden triangles are unaffected.
- **(d) and (e).**
  - For quotas, k q-sets have empty intersection iff the complements cover [n] iff k(n − q) ≥ n. So ν = ⌈n/(n − q)⌉, with ν ≥ 3 ⟺ 2q > n and ν ≥ 4 ⟺ 3q > 2n. The weighted sufficient condition kτ > (k − 1)W ⇒ ν ≥ k + 1 is correct. ✓
  - CHECKED: the brute-force Nakamura number equals ⌈n/(n − q)⌉ for all n ≤ 6, and the two equivalences hold for n ≤ 9.

### 3.4 Prop A8 and Cor B4

Not among the items I was asked to referee. I did not re-derive HH1 Prop 1(b) or FF2's import chain.

### 3.5 Transfer to the ψ-rule (PROVED)

- **Necessity parts of Theorem A transfer for every ψ > 0 on (0, ∞).** For any proper game, a cycle of distinct consecutive models has length ≥ ν; ties need disjoint winning coalitions; and (TC) holds when ν ≥ 4.
- **Sufficiency parts transfer when ψ(s) ≤ cs on some (0, s₁] with c < 1.** The lifting lemma's ψ ≤ s/2 qualifies. Replace the ratio 1/r by t > 1 with (t − 1)/(t + 1) ≥ c, and work at mass scale small enough that every gross change is ≤ s₁.
  - Supported edges then have Δ/d ≥ (t − 1)/(t + 1) ≥ c, so Δ ≥ ψ(d).
  - Every intended non-support has Δ ≤ 0 < ψ(d).
- **Consequence.** For (4, 3), ψ-rule worlds with strict 4-cycles exist (ν = 4), so (FC) fails in the class.
- **The certificate.** It is accepted by the ψ-rule at mass scale s iff ψ(29s/4) ≤ 3s/4, i.e. ψ(x) ≤ 3x/29 at x = 29s/4. This holds for all small s when ψ(s)/s → 0. By R1 it holds along a sequence of scales for every ψ that works for a (QS) family.
  - The certificate's judges are LL3's, so this says only that the ψ-class also escapes every single endorsing field out of two coherent candidates. Theorem B1's threshold M\* has no direct ψ analogue: as the effective margin tends to 0, M\* → 1.

---

## 4. Clean statements

**Theorem (strict-sign lifting; PROVED).**
- **Setting.**
  - Finitely many worlds and an atomless finite measure.
  - A decomposable domain M.
  - At each world, n judges whose penalties are strictly guiding on the advice range and have integrable envelopes.
  - A quorum with 3q > 2n.
  - A coherent selection p ↦ C_p, continuous in measure on all of Δ.
- **Equivalence.** The following are equivalent.
  - **(QS).** For every p and every evaluable X ≠ C_p, some i ∈ supp p has at least q judges with L_iv(X) > L_iv(C_p).
  - **(Ψ).** There is a continuous nondecreasing ψ: [0, M] → [0, ∞) with ψ(0) = 0 and 0 < ψ(s) ≤ s/2 on (0, M] such that, under the rule "iv supports X R_i Y iff L_iv(Y) − L_iv(X) ≥ ψ(d_iv(X, Y)); accept with ≥ q votes", every C_p is competitive on supp p. Under (QS), ψ may also be chosen with ψ(s)/s → 0, or below any positive continuous cap.
- **Cover.** Under (Ψ) the rankings are reflexive and satisfy (IB), strict (G), (TC) and closed sections for every X. They have no nontrivial ties. Direct (C), (LA) and (S) hold, and every C_p is undominated.
  - So if T1 = C_{p₀} and (LF) holds at T1 (automatic on the full domain), this is a cover of T1 under (TC).
  - (FC) can fail.
- **Necessary conditions (R1).** Under W_1 ≠ W_2:
  - liminf_{s↓0} δ(s)/s = 0, where δ(a) := inf{r(p, X) : D(p, X) ≥ a};
  - every working ψ has liminf ψ(s)/s = 0.
- **Continuity is automatic (R2).** On the full domain, any coherent selection with closed sections that is ψ-competitive, with 0 < ψ(s) < s, is continuous in measure.

**Theorem (fixed-margin exclusion; PROVED).** As stated in §2.4: (i) for every q, and (ii) under no nontrivial ties.

**Proposition (LL3 certificate; PROVED, CHECKED).** Take ε = 3/10, world 1, n = 4, q = 3, η = 1/16, judges with density ratio ≤ 2, and A, B as above. Then eight accepted comparisons out of A and B have records whose sum is a pure improvement. So no strictly guiding field, and no positive error weight, endorses them all.
- A and B are coherent, but they are not shown to be selected in any covering system.
- The same certificate is accepted by any ψ-rule at a scale where ψ(x) ≤ 3x/29.

**Theorem A (LL3; PROVED, with the §3.3 mass repair).** For any monotone game with Nakamura number ν and any margins:
- no ties ⟺ ν ≥ 3;
- (TC) ⟺ ν ≥ 4;
- strict k-cycles ⟺ the game is proper and k ≥ ν.

For quotas ν = ⌈n/(n − q)⌉. These statements hold verbatim for ψ-rules with ψ(s) ≤ cs, c < 1, near 0. The "⟸" directions of no-ties and (TC), and the "⟹" direction of the cycle statement, hold for every ψ > 0.

## 5. Files

- `mm3py/mm3_check.py` → `mm3py/mm3_check.out`: 112 exact checks, ending `ALL CHECKS PASSED`.
  - Part 1: boxes with the exact Lipschitz constant, the eight records, votes, reverses, the net, and the 3/29 ratio.
  - Part 2: Nakamura numbers of quotas.
  - Part 3: Thm B2 at M\*(1 + 10⁻³) and M\* for 24 (n, q, η) cases.
- Reruns of LL1–LL3 scripts: outputs identical or with matching verdicts; no new files written.
