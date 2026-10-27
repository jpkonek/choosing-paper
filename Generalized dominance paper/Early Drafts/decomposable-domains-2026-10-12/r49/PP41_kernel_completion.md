# PP41. Completing PP38's kernel: the jump cannot be additive

23 October 2026. Task PP41 of Brief 49. One reader (me); not refereed.

**Labels.** PROVED: complete argument here, or a cited refereed or re-derived result. CHECKED: exact rational computation in `PP41_py/exact41.py` (ALL PASS). NUMERICS: linear programming on an empirical Gaussian sample in `PP41_py/twofield_lp.py`; no proof depends on it. CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF49 and the audit's answers (binding); PP38 (kernel K_ℓ, field ℓ^T, Cor 4.3, Thms 5.1, 6.2, 6.3, 6.5, Prop 6.6); PP37 (gates, Thm 5.1, Thm 5.6, Prop 6.1, Conj 7.1); PP40, as relayed by the coordinator and read in r9 (Prop 5.2 of PP38 is false, and is repaired by the shadow condition (B3); inheritance Lemma 2.1; Props 2.3–2.6; K^S Prop 3.1; Thm 3.3; Prop 3.4); REFEREE_PP32_penalties (ℓ^T); REFEREE_round48; LEAD_selection_count (Lemmas A, B, E); AUDIT_completion (rules I–IV, F1/F2). Only Brief 49's axioms are used. Every extra hypothesis is named where it enters.

---

## 0. Verdict

**The milestone is not completed. Its first step, the jump, cannot be completed in the form PP38's kernel invites. I identify the commitment responsible, state the redesign, and show the redesign passes the first test that kills the original.**

1. **The jump admits no additive completion (Theorem 2.4, PROVED).** Keep PP38's kernel on bounded records. Suppose that at each world the unbounded verdicts out of registered models are the sign of **one valuation per world**. "Valuation" means an additive record functional that agrees with the kernel on bounded records and is strictly guiding with angular densities. Then the milestone is impossible, *whatever* the zero rules are: strict, symmetric, mixed, or record-dependent. This covers:
   - the maximal ℓ^T preorder (PP40 Prop 1.1);
   - any second field added on unbounded records (two-scale valuations Φ + Π, Π a tail functional);
   - PP37's iso-level and single-strict-world patterns, transplanted to the kernel.
2. **Mechanism.** The jump forces the limiting edge model B_12(t*) to be *iso-level with T* at world 3 and at one edge world. No pair of models that are Bayes at an interior weight and at an edge weight for one valuation can be iso-level at those two worlds (Lemma 2.5, a two-line Bayes argument).
3. **Tie pattern (task item 1).** The jump needs neither PP37's iso-level pattern nor any zero rule. Iso-level with T is exactly what it *forbids* for a common valuation. What it needs is that **T and the post-jump models are judged by different valuations, which do not converge to each other at the jump** (Prop 2.8).
4. **Commitment responsible (stopping rule):** *one valuation per world, shared by all realisers.* **Redesign:** *per-realiser valuations* (gates, as in PP37 §3, with PP38's kernel as the common bounded part).
   - Under it, universal competitiveness against every rival, bounded or not, holds for every registered model of every generation (Prop 4.1, PROVED).
   - Closure at the jump becomes a per-gate inheritance law (Prop 2.7, PROVED). It forces T's own valuation to rate the post-jump models at least as well as T at world 3. A weakly guiding second field does this at every t ≠ 1 tested (NUMERICS); at t = 1 it is impossible (PROVED).
   - The inheritance law is impossible if the path models' valuations converge to T's at p_0 (Prop 2.8, PROVED). So the path models need valuations that stay apart from T's (Option A), or explicit non-valuation refusals (Option B).
   - Both options are OPEN. For Option B the first cross-gate (TC) configuration is stated exactly (§2.5).
5. **Residues and generations (task items 2–3).** Not completed.
   - Refinements of T (PP37 Conj 7.1) are **not registrable** under PP38's kernel (Prop 3.1, PROVED). The dominators must come from T, B_ij(t) and V_k.
   - With PP40's results, the dominator supply for (b) and (c) is located. Under the redesign, a domination can be endorsed by the *dominator's own* valuation (Prop 3.3), so installed field-rejected records are not forced.
   - The invariant offered for all generations (§4) is an actual allocation: a fixed function of the record and its registered realisers. It survives closure *provided* cross-gate (TC) holds. That proviso is the open part.

| Item | Result | Label |
|---|---|---|
| Edge selection hits every edge model (single valuation) | Lemma 2.2 | PROVED |
| Post-jump models non-accumulating; infinitely many near p_0 | Lemma 2.1 | PROVED |
| Jump forces iso-level limit pair (T, B_12(t*)) at worlds 3 and w_1 | Prop 2.3 | PROVED |
| Iso-level pair impossible for a common valuation | Lemma 2.5, Thm 2.4 | PROVED |
| LP cross-check of Thm 2.4 on a sample (21 values of t, both edge worlds) | §2.3 | NUMERICS |
| Exact geometry used (T ≤_3 B_12(1); edge monotonicity; regions) | Lemma 1.2 | PROVED; CHECKED |
| Redesign: universal competitiveness for all generations | Prop 4.1 | PROVED |
| Redesign: jump closure = per-gate inheritance; necessary (J_B), (J_T) | Prop 2.7 | PROVED |
| (J_T) satisfiable by a weakly guiding T-field, t ≠ 1 | §2.5 | NUMERICS; t = 1 impossible PROVED |
| Path valuations converging to T's: impossible | Prop 2.8 | PROVED under (NA) |
| Common Bayes weights necessary for unbounded competitiveness | Prop 3.4′ | PROVED under (NA) |
| Refinements of T not registrable under the kernel | Prop 3.1 | PROVED |
| Dominations endorsed by the dominator's valuation | Prop 3.3 | PROVED (conditions) |
| Cross-gate (TC); residues installed together; all generations | §§2.5, 3, 4 | OPEN |

---

## 1. Setting

Brief 49's setting, PP38's notation:
- three worlds; Gaussian μ; the full four-advice domain; ranks 0 < 1 < 2 < 3;
- classes M_1, M_2, M_3, U; T = D_M; Sil(T);
- θ = |g_2|/|g_1| on W_12 = M_1 ∪ M_2; the band J = (α, β);
- the kernel K_ℓ: a bounded record r is accepted at w iff Φ_w(r) ≥ 0, where Φ is the ℓ^T value.

Registered models under the kernel are exactly T, B_ij(t) and V_k (PP38 Cor 4.3). On W_12, B_12(t) is 1-correct iff F(θ) < t, 2-correct iff G(θ) > t, and silent otherwise (CHECKED (c)).

**Index domain I.**
- p_T = u;
- the edge [e_1, e_2];
- the three vertices;
- a path P from u to an edge point q_e;
- all limit points.

e_3 is isolated in I, as the milestone's vertex clause requires. That is harmless, since C_{e_3} = V_3 is forced (Lemma B).

Following PP38 Thm 6.2 and PP40 §2: p_0 is the last point of Φ_T along P (Φ_T is closed by Lemma A, and interior by Lemma E), and C_{p_0} = T. Post-jump models B_n := C_{p_n}, with p_n ↓ p_0, eventually lie in one family B_ij(t_n).

**(H_P).** The post-jump family is that of the milestone edge, B_12, so its third world is k = 3. This is used only in Theorem 2.4. The other case is discussed after it.

**Lemma 1.1 (non-accumulation; PROVED).** Every model selected at indices accumulating at p_0 is all-world tied with T. Hence no post-jump model is selected at indices accumulating at p_0: every neighbourhood of p_0 meets infinitely many distinct post-jump models, and the jump cannot land on a constant model.

*Proof.* Φ_B is closed (Lemma A). If it accumulates at p_0, then C_{p_0} = T ≈ B. That puts the index of B in Φ_T, which contradicts the choice of p_0 as the last point of Φ_T. ∎

**Lemma 1.2 (exact geometry; PROVED, CHECKED (a), (b), (d)).**
- **(a) Edge monotonicity.** For s < t, B_12(t) is pointwise weakly 1-better and weakly 2-worse than B_12(s), strictly on non-null sets. (Proof: the 1-correct region grows and the 2-correct region shrinks.)
- **(b)** T is pointwise weakly 3-better than N := B_12(1), strictly on Sil(T) ∩ M_3 (PP40 Prop 2.4(i); re-CHECKED).
- **(c)** For t ∈ (0, ∞) ∖ {1}, the disagreement set D_t := {T ≠ B_12(t)} contains non-null cones where:
  - T is strictly 1-better than B_12(t): M_2 ∩ {θ > G^{-1}(t)} ∩ {s_1 + s_3 > L}, where T = A and B = B;
  - T is strictly 2-better: M_1 ∩ Sil(T) ∩ {θ < F^{-1}(t)}, where T = S and B = B;
  - B_12(t) is strictly 3-better: R_t (PP40 Prop 2.4(ii)), the wedge M_1 ∩ Sil(T) ∩ {G^{-1}(t) < θ < β} for t < 1, and its M_2 mirror for t > 1.

  D_t also contains Sil(T) ∩ M_3.

  CHECKED counts at t ∈ {1/3, 1/2, 9/10, 11/10, 2, 3}, ε ∈ {1/10, 3/10}: every region is hit, and R_1 is empty.

---

## 2. The jump

### 2.1 Single-valuation layers

**Definition (valuation layer).** At each world w, a **valuation** is a map V_w from records to R with:
- **(V1)** additivity: V_w(r^{-1}) = −V_w(r); V_w is additive over composition and over disjoint unions; V_w = Φ_w on bounded records;
- **(V2)** strict guidance with densities: V_w(r) < 0 for every nontrivial weak w-improvement. On records between conic models, supported on cones, V_w is the integral over directions of an integrable density that is > 0 where the w-rank rises, < 0 where it falls, and 0 where it is unchanged.

  Every strictly guiding integrable field gives such densities. So does Φ + Π_ψ, with Π_ψ a Banach-limit tail functional of a weakly guiding angular field ψ.

A relation is **single-valuation** if, for every unbounded record r realised by a registered model:
- **(V3)** V_w(r) > 0 ⇒ r is accepted at w;
- r accepted at w with V_w(r) < 0 ⇒ r is (a copy of) an installed domination.

Zero-value records may be treated in any way, and the treatment may depend on the record.

**(H_inst).** No installed record is a copy of a sub-record of rec(T, B) or of its inverse, for registered conic T, B. Installed records are dominations of bounded perturbations of registered models. A copy of such a sub-record would make a splice of two registered models coherent, which happens only for a null family of splice sets (Remark 2.6).

PP38's maximal fragment (PP40 Prop 1.1) is the single-valuation layer V = Φ. PP33's ρ-extension and every "add a second field on unbounded records" proposal are single-valuation layers too.

**Lemma 2.2 (the edge selection hits every edge model; PROVED, single-valuation).** The edge selection is q ↦ B_12(τ(q)) for a continuous τ : [e_1, e_2] → [0, ∞] with τ(e_1) = ∞ and τ(e_2) = 0. In particular every B_12(t) is registered.

*Proof.*
1. **Form.** Each C_q is B_12(t) for some t ∈ [0, ∞]: competitiveness against bounded rivals forces Bayes at an edge weight (PP38 Thm 3.1(ii), Cor 4.3). τ(e_i) is fixed by Lemma B.
2. **Lower semicontinuity.** Suppose q_m → q with V_w(C_{q_m}) < V_w(C_q) − δ. Let X := C_q[F ↦ w-better] with F bounded and gain below δ. Then V_w(C_{q_m} → X) > 0, so C_{q_m} accepts X by (V3), closure gives C_q ⪯_w X, and strict (G) refuses that. So V_w(C_q) ≤ liminf V_w(C_{q_m}) for w = 1, 2.
3. **Continuity of τ.** By (V2) and Lemma 1.2(a), t ↦ V_1(B_12(t)) is continuous and strictly decreasing, and t ↦ V_2(B_12(t)) is continuous and strictly increasing. Write V_w(X) for differences from a fixed base; this is legitimate by (V1). Lower semicontinuity of V_1 gives τ(q) ≥ limsup τ(q_m), and lower semicontinuity of V_2 gives τ(q) ≤ liminf τ(q_m). So τ is continuous.
4. **Onto.** Apply the intermediate value theorem on the edge. ∎

**Proposition 2.3 (the jump forces an iso-level limit pair; PROVED, single-valuation, (H_P), (H_inst)).** Let t* be a limit point of (t_n) in [0, ∞]. Then:
- **(i)** t* ∈ (0, ∞) ∖ {1}, and B* := B_12(t*) is registered on the edge;
- **(ii)** V_3(T → B*) = 0;
- **(iii)** V_w(T → B*) ≥ 0 for w = 1, 2;
- **(iv)** V_w(T → B*) = 0 for both w = 1, 2.

*Proof.* Pass to a subsequence t_n → t*. By (V2), V_w(B_n → B*) → 0.
1. **Upper bound at 3.** For E ⊆ Sil(T) ∩ M_3 bounded, B_n ⪯_3 T[E ↦ A] is forced for n ≥ N(E) (PP38 Thm 6.3(a), or PP40 Lemma 2.1). By (H_inst) it is not installed, so V_3(B_n → T) + β_3(E) ≥ 0.
2. **Upper bounds at every world.** For F bounded and X′ := T[F ↦ w-better] with gain γ_F, closure refuses B_n ⪯_w X′ eventually, since strict (G) refuses T ⪯_w X′. By (V3), V_w(B_n → T) − γ_F ≤ 0 eventually.
3. **Limits.** Letting E and F shrink gives V_3(B* → T) = 0 and V_w(B* → T) ≤ 0 for all w. Since V(T → B*) = −V(B* → T), this is (ii) and (iii).
4. **t* is not a vertex.** If t* = ∞, then B* = V_1 is pointwise strictly 1-better than T, so V_1(T → V_1) < 0, against (iii). t* = 0 is symmetric.
5. **t* ≠ 1.** At t* = 1, Lemma 1.2(b) and (V2) give V_3(T → N) > 0, against (ii).
6. **Registration.** B* is registered by Lemma 2.2. This proves (i).
7. **(iv).** Put a(S) := V(T → T[S ↦ B*]) ∈ R³ for cones S ⊆ D := D_{t*}. By (V1) and (V2), a is a non-atomic finite vector measure on the cone σ-algebra, and V(B* → B*[S ↦ T]) = −a(S).
   - B* has support {1, 2}. Each splice B*[S ↦ T] is a rival that is neither bounded nor installed, so B*'s defence against it is at some w ∈ {1, 2} with −a_w(S) ≥ 0, by (V3).
   - By Lyapunov the range {(a_1, a_2)(S)} is convex and compact, and it misses the open positive quadrant. Separation gives μ ∈ Δ_{12} with μ · a(S) ≤ 0 for all S.
   - μ is not a vertex. If μ = e_1, then the density of a_1 is ≤ 0 a.e. on D, so T is nowhere strictly 1-better than B*. That contradicts Lemma 1.2(c). μ = e_2 is symmetric.
   - So μ_1, μ_2 > 0. At S = D, μ_1 a_1(D) + μ_2 a_2(D) ≤ 0 with both terms ≥ 0 by (iii), so a_1(D) = a_2(D) = 0. ∎

So the jump does not merely *allow* a tie at the limit: it forces the limiting edge model to have **exactly T's valuation at all three worlds**. With (ii) and (iv), a(D) = 0.

**Theorem 2.4 (no single-valuation jump; PROVED).** Under PP38's kernel, the milestone domain, (H_P) and (H_inst), no single-valuation relation satisfies the milestone. That is, the following cannot hold together:
- closed sections relative to I;
- competitiveness of T, of the post-jump models and of the edge models against their own splices;
- strict (G).

(TC) and the repair class are not even needed.

*Proof.* Use Prop 2.3, with a(D) = 0. T is competitive at full support against the splices T[S ↦ B*], which are not installed by (H_inst). So, as in step 7, there is λ ∈ Δ with λ · a(S) ≥ 0 for all S. Also a(D ∖ S) = −a(S). Hence λ · a ≡ 0, and likewise μ · a ≡ 0. So the density of a lies a.e. in λ^⊥ ∩ μ^⊥.
- **λ not parallel to μ.** Then λ^⊥ ∩ μ^⊥ is a line. On Sil(T) ∩ M_3 the change T → B* is S → A, with density sign pattern (−, −, +). On R_{t*} it is S → A on M_1, with pattern (+, −, −) for t* < 1, or on M_2, with pattern (−, +, −) for t* > 1. Neither pattern is a multiple of (−, −, +). Both regions are non-null by Lemma 1.2(c).
- **λ parallel to μ.** Then λ = μ and λ_3 = 0. On Sil(T) ∩ M_3, λ · density = λ_1(−) + λ_2(−) < 0, so λ · a(S) < 0 for S ⊆ Sil(T) ∩ M_3. ∎

**Lemma 2.5 (the Bayes form of the obstruction; PROVED).** Let V be any valuation for which:
- T is the pointwise strict λ-minimiser against B on D, with λ ∈ int Δ;
- B is a pointwise μ-minimiser against T, with μ_3 = 0 and μ_1, μ_2 > 0.

Then E := V(T) − V(B) cannot vanish at world 3 and at an edge world.

*Proof.* We have λ · E < 0 and μ · E ≥ 0. If E_3 = E_1 = 0, the second gives μ_2 E_2 ≥ 0, while the first gives λ_2 E_2 < 0. The case E_3 = E_2 = 0 is symmetric. ∎

Lemma 2.5 is what the LP of §2.3 found. With λ = u and μ = (t, 1, 0) it gives E_3 < (t − 1)E_1 and E_3 < (1/t − 1)E_2: exactly the certificates printed in `twofield_lp.out`, with ratios y_1/y_3 = 1 − t and y_2/y_3 = 1 − 1/t at every t.

**Remark 2.6 (scope).**
- **(H_inst)** concerns only splices of two registered conic models. The splice sets S for which T[S ↦ B*] is coherent form a null family in the space of cones, and Lyapunov ranges are unchanged by removing them. So (H_inst) can be weakened to "installed records are dominations of bounded perturbations". I have not written that out (OPEN in detail).
- **(H_P).** If the post-jump family is B_13 or B_23, Prop 2.3 (ii) and (iii) still hold with k in place of 3, but B* need not be registered. Running step 7 with the interior-index models B_n gives μ_n ∈ Δ, which can carry weight on k. I have no contradiction then. This is the one place Theorem 2.4's proof does not reach. The path can choose its post-jump family (the jump in measure is forced, the family is not). But a post-jump family different from the edge's family needs a second change of family before q_e, and I have not analysed that junction. Whether this escapes is OPEN (§4).
- **Zero rules.** The proof never used how zero-value records are decided. So PP37's Theorem 5.6 pattern (strict at one world, iso-level) gives no escape once T and the post-jump models share a valuation.

### 2.2 Direct (C) at the ties

In any single-valuation layer, the ties at the jump would be T ≈_w B* at the zero worlds. By Theorem 2.4 these configurations do not exist, so there is nothing left to check. In the redesign (§2.5) the ties are per-gate, and direct (C) is checked there.

### 2.3 NUMERICS cross-check

`twofield_lp.py`: ε = 0.3, n = 4,000 Gaussian problems (3,025 mixed). The unknown is a weakly guiding angular field ψ, and V = ℓ^T + ψ. The constraints are:
- T is pointwise u-optimal;
- every B_12(t) is pointwise (t, 1, 0)-optimal, imposed at the two ℓ^T breakpoints of each problem;
- V_3(B_t) = V_3(T) and V_w(B_t) = V_w(T) for w = 1 or w = 2, in scale-free form.

Results, for 21 values t ∈ [0.1, 10]:
- **both two-world iso problems are infeasible** (max scale s = 0 exactly), with dual certificates (y_3, y_w) matching Lemma 2.5;
- the **world-3 condition alone is feasible** for every t ≠ 1, and infeasible at t = 1 (Lemma 1.2(b)).

The second point is what the redesign uses.

### 2.4 What the jump needs: the commitment and its redesign

The responsible optional commitment is **"one valuation per world, shared by T, the path models and the edge models"**. It is optional: Brief 49's axioms impose (IB) record by record, and they let a realiser's gate decide what its records are worth (PP37 §3 does exactly this).

The forced structure (PP40 Lemma 2.1, Props 2.5, 2.6, and Prop 2.3 above) says what the separate valuations must do:
- **T's valuation must rank the post-jump models at least as well as T at world 3.** This is the k-inversion: T ⋠_3 B_n[E′ ↦ S] for every E′, eventually.
- **The path models' valuations must not rank T's pure improvements below themselves at the edge worlds.** This is inheritance plus lower semicontinuity.

Neither can be done by ℓ^T alone, or by any valuation common to both.

### 2.5 The redesign: gates over the kernel

**Design Γ_K.** Each registered C carries a valuation V^C = Φ + Π^C (V1–V2), where Π^C vanishes on bounded records. A record r is accepted at w iff:
- it is guidance; or
- it is bounded with Φ_w(r) ≥ 0 (the kernel, common to all); or
- it is a copy of an installed domination; or
- some registered C realises a side of r and passes its gate at w.

Gate C passes at w if either:
- C realises the old side and V^C_w(r) > 0; or
- V^C_w(r) = 0, C realises the old side or the new side, and C's zero rule at w is symmetric.

This is PP37's design Γ, with PP38's kernel replacing PP37's L-gate on bounded records.

**Proposition 2.7 (what closure at p_0 needs in Γ_K; PROVED).** Closure at p_0 for every measurable rival is the per-gate inheritance law (PP40 Lemma 2.1):

  (J) for every X and w: if B_n accepts rec(B_n, X) at w for infinitely many n, then T accepts rec(T, X) at w.

It implies the following two conditions.
- **(J_B)** limsup_n V^{B_n}_w(B_n → T) ≤ 0 at every w, and V^{B_n}_3(B_n → T) → 0.
- **(J_T)** limsup_n V^T_3(T → B_n) ≤ 0: **T's own valuation must rate the post-jump models at least as well as T at world 3**, in the limit.

*Proof.*
- **(J_B).** This is steps 1–3 of Prop 2.3, run with B_n's gate. Those steps use only B_n's own verdicts, the kernel and guidance.
- **(J_T).** PP40 Prop 2.5(a) gives T ⋠_3 Y_{E′}, where Y_{E′} = B_n[E′ ↦ S] and n ≥ N(E′). That record is realised by T, so T's gate must not pass it: V^T_3(T → Y_{E′}) ≤ 0. Also V^T_3(T → Y_{E′}) = V^T_3(T → B_n) − β_3(E′). Let E′ shrink. ∎

**Proposition 2.8 (gate continuity is impossible; PROVED under (NA) of Prop 3.4′).** Suppose the path valuations converge to T's at p_0: V^{B_n}_w(r) → V^T_w(r) for every record r, with converging densities. Then (J) fails.

*Proof.*
1. **Common weights.** B_n = B_12(t_n) is Φ-Bayes only at μ_n := (t_n, 1, 0)/(1 + t_n). Competitiveness against unbounded rivals forces the same weight for Π^{B_n} (Prop 3.4′ below). So μ_n · V^{B_n}(B_n → X) ≥ 0 for every X.
2. **Limits.** With converging densities, the limit gives μ* · V^T(B* → X) ≥ 0 for every X, with μ* = (t*, 1, 0)/(1 + t*). By (J_B) in the limit, V^T(B* → T) ≤ 0 at every world, and = 0 at world 3.
3. **Iso-level.** μ* · V^T(B* → T) ≥ 0 with μ*_1, μ*_2 > 0 forces V^T(B* → T) = 0.
4. **Contradiction.** T is the strict u-minimiser for V^T, and B* is a μ*-minimiser for V^T. Lemma 2.5 excludes this. (t* ∉ {0, 1, ∞} as in Prop 2.3(i).) ∎

**What is checked, and what is open.**
- **(J_T) is satisfiable** on its own. NUMERICS (§2.3): a weakly guiding ψ with T pointwise u-optimal, and even every B_12(t) edge-optimal, satisfies V^T_3(B_t) = V^T_3(T) at every tested t ≠ 1. At t = 1 it is impossible (Lemma 1.2(b)), in line with PP40 Prop 2.4.
- **(J) itself.** By Prop 2.8, the path valuations must satisfy (J) **without converging to T's**. This leaves two options.
  - **Option A (valuations).** Non-convergent path valuations. (J) then needs, for every conic T-realised record r, that limsup_n [V^{B_n}_w(B_n → T) + V^{B_n}_w(r)] > 0 implies V^T_w(r) ≥ 0. This is a one-sided comparison between Π^{B_n} and Π^T on records leaving T. It is compatible with additivity, because it is not closed under inversion. Whether it is compatible with each B_n being common-Bayes at μ_n is OPEN; it is again an LP-type question.
  - **Option B (explicit refusal).** A non-valuation rule at the edge worlds:

    (J_ref) for each post-jump B_n and w ∈ {1, 2}: refuse rec(B_n, X) at w whenever T's gate refuses rec(T, X) at w and n ≥ N(X).

    This is PP40's inheritance law used as a rule. It is (IB)-admissible: it depends on the record and on its registered realiser B_n, and X = B_n · r is determined by both. It cannot be a function of the record alone in the kernel's sense, because a fixed record is realised by infinitely many B_n.

  Either way, the jump needs verdicts out of the post-jump models that are **not** the sign of a valuation shared with T. That is the content of Thm 2.4 and Prop 2.8.

**Proposition 3.4′ (common weights are necessary; PROVED under (NA)).** Let C be registered. Suppose C is Φ-Bayes only at λ, while C's gate valuation makes C Π^C-Bayes only at λ′ ≠ λ. Then C is not competitive against some unbounded rival.

**(NA)** is the following hypothesis:
- the Φ-values of bounded perturbations of C fill the open half-space {x : λ · x > 0} (together with 0);
- the Π^C-values of tail perturbations of C (changes on a cone outside a large ball) fill {x : λ′ · x > 0}.

It holds when the pointwise change vectors out of C accumulate on λ^⊥ (resp. λ′^⊥) from every direction, as they do near C's Bayes boundaries.

*Proof.*
1. **The sum of two half-spaces.** Since λ is not parallel to λ′, the sum of the open half-spaces {λ · x > 0} and {λ′ · x > 0} is R³. Pick φ in the first and v in the second with φ + v = −δ(1, 1, 1).
2. **The two changes.** Take a bounded perturbation b of C with Φ-value φ, by (NA). Take a tail perturbation c on a cone outside the ball B_R, disjoint from supp b, with Π^C-value v. Its Φ-value tends to 0 as R → ∞, because ℓ^T is integrable and Π^C is a tail functional.
3. **The rival.** Put X := C · b · c. Then V^C(C → X) = φ + v + Φ(c) < 0 at every world, for large R. So C's gate refuses X at every world.
4. **No other route.** X is not guidance: a weak w-worsening has V^C_w > 0. It is not a kernel record, since it is unbounded. For generic b and c, no other gate realises its old side. ∎

(The proof uses only (NA) and the tail property of Π^C.)

**The first cross-gate configuration under Option B (OPEN, stated exactly).** At world w ∈ {1, 2}:
- a B_n-gate record refused by (J_ref);
- a guidance or kernel record;
- a T-gate record.

These may form an accepted triangle. The audit's (TC) obligation is that no copy of a (J_ref)-refused record is accepted *through another realiser's gate*. In particular, it must not be accepted through the edge models' gates, which realise the same records whenever B_n is also selected on the edge (Lemma 2.2: every B_12(t) is). So (J_ref) must apply to the **model** B_n wherever it is registered. It then constrains the edge sections at the index of B_12(t_n), and closure on the edge must be re-proved with these refusals. I have neither a proof nor a counterexample.

**Answer to task item 1, in one line.** No zero-rule or tie pattern makes the jump work while T and the path models share a valuation (Thm 2.4), or while the path valuations converge to T's (Prop 2.8). The jump needs per-realiser valuations that stay apart from T's at p_0 (Option A), or an explicit inheritance refusal (Option B). Both are OPEN. In Option B, (TC) on the edge is the first open configuration.

---

## 3. The three residue families (task item 2)

### 3.1 Which dominators can be registered

**Proposition 3.1 (PROVED).** Under PP38's kernel no refinement D_K of T, with K ⊊ M, can be registered at any index. Every registered model must be competitive against bounded rivals at a weight in its support, hence ℓ^T-Bayes there (PP38 Thm 3.1(ii)). The only ℓ^T-Bayes coherent models are T, B_ij(t) and V_k (Cor 4.3; Lemma 4.2 for interior weights other than u).

So PP37 Conj 7.1 is **incompatible with PP38's kernel**. The optional commitment responsible is the single bounded field: it fixes the registrable geometry (PP40 §4 agrees).

### 3.2 Records against ℓ^T: what PP40 changes

PP38 Prop 5.2 is false as stated (PP40 §1.3). The repaired interface adds the shadow condition (B3): records undoing an installed record's unbounded part must be refused. PP40 shows its core is necessary. Every installation below must therefore be paired with its shadows. The shadows are refusals of field-endorsed records, so they are again non-additive verdicts, of the same kind as (J_ref).

### 3.3 Dominators endorsed by their own gate

**Proposition 3.3 (PROVED).** In Γ_K, a registered C dominates a rival Z without installation if, at every world w, one of the following holds:
- C ⪯_w Z by guidance;
- rec(C, Z) is bounded with Φ_w ≥ 0;
- V^C_w(C → Z) > 0, or V^C_w(C → Z) = 0 with C's zero rule symmetric at w;

and in addition strictness holds at some world (no gate of a realiser of rec(Z, C) passes there).

For a bounded perturbation Z = Y · z of a registered Y, with C ≠ Y:

  V^C_w(C → Z) = V^C_w(C → Y) + Φ_w(z).

So C's gate endorses Z at w iff V^C_w(C → Y) ≥ −Φ_w(z), with the boundary case decided by the zero rule.

Applied to the residues (the necessary exclusions are PP40's, valid for every layer):
- **(a) The jump record** B_n ⪯_3 T[E ↦ A]. It is endorsed by B_n's gate iff V^{B_n}_3(B_n → T) ≥ −β_3(E). Since β_3(E) can be arbitrarily small, this needs V^{B_n}_3(B_n → T) ≥ −o(1) as n → ∞, i.e. B_n's own valuation must rate T at world 3 no better than itself, in the limit. PP38's (H_3) margin says ℓ^T rates T better by 0.46. So **Π^{B_n} must carry that margin**: this is (J_T)'s mirror for B_n.
- **(b) T's fills** X = T[G ↦ V_j]. PP40 Prop 3.4: V_j is excluded, T ⋠_j C for every dominator C, and edge models off j pass the splice test. In Γ_K a dominator C = B_ik(t) (k ≠ j) endorses X iff V^C_w(C → T) ≥ −Φ_w(G, S → V_j) at all w. At w = j that is V^C_j(C → T) ≥ α_j(G) > 0, so C must be strictly better than T at j in its own valuation. At w ≠ j it is V^C_w(C → T) ≥ −β_w(G).
  - PP38 Thm 6.5 says that with V^C = Φ this fails at some world: isolation, Σ_w Φ_w(C → T) ≥ 3c_3 > 0.
  - With Π^C ≠ 0 it is not excluded. But Π^C is constrained by C's own common-Bayes requirement at its weight, and by Lemma 2.5 against every model whose valuation it must match in a limit.
  - Whether one Π^C can endorse the fills of a whole neighbourhood of T while keeping C Bayes is OPEN. It is a finite-dimensional LP of the type in §2.3, which I have not run.
- **(c) Edge models' forced rivals.** PP40 Thm 3.3: for small rivals Z′ of N = B_12(1), the only clean dominators are B_12(t) with |t − 1| tiny. They are ℓ-endorsed at worlds 1 and 2, and against ℓ at world 3.
  - In Γ_K edge members have no world-3 gate (support {1, 2}), so world 3 needs either an installed record or a world-3 valuation for edge members.
  - Giving B_12(t) a world-3 valuation V^{B_t}_3 with V^{B_t}_3(B_t → N) ≥ −Φ_3(z′) is the same kind of constraint as (a).
  - Its compatibility with Lemma 2.2, which needs t ↦ V_w(B_12(t)) monotone at worlds 1 and 2 for the edge sections, is OPEN.

**Competitiveness against unbounded rivals (task item 2, checked explicitly).** In Γ_K every registered C is competitive against every measurable rival X on its support, provided C is the a.e.-unique common Bayes model of Φ and Π^C at one weight λ_C ∈ Δ_{s(C)} (Prop 4.1). This includes unbounded rivals.

The common weight matters. If C is Φ-Bayes at λ and Π^C-Bayes at λ′ ≠ λ, a rival combining a bounded change with a tail change has values negative at every world (Prop 3.4′). So common weights are **necessary** (under (NA)), not only sufficient, for unbounded competitiveness in Γ_K.

**Proposition 3.4 (where (TC) stands).** In Γ_K, every (TC) failure at a world involves:
- an installed record;
- a (J_ref) or (B3) refusal clashing with a copy accepted through another gate; or
- records accepted through two different gates.

*Proof.* A single gate is a valuation: Lemma 3.3 of PP37 holds verbatim with V^C in place of L, because the zero rule is reversal-symmetric. The kernel and guidance are part of every valuation. ∎

PP37 Thm 3.2's localisation thus transfers. The cross-gate cases are open.

---

## 4. Generations (task item 3)

**Invariant (I_Γ).** Every registered C, of every generation, satisfies the following.
- **(I1)** C is coherent and is the a.e.-unique Bayes model of Φ at some λ_C ∈ Δ_{s(C)}. Hence C ∈ {T, B_ij(t), V_k}, by Prop 3.1.
- **(I2)** C carries a valuation V^C = Φ + Π^C, with Π^C a weakly guiding tail functional for which C is also the a.e.-unique Bayes model at the same λ_C.
- **(I3)** The allocation is A(r) = {w : guidance, kernel, an installed copy, or some realiser's gate passes}. This is a fixed function of the record and of its registered realisers.

**Proposition 4.1 (PROVED).** Under (I_Γ), for any registered family 𝒫 of any generation:
- **(a)** every C ∈ 𝒫 is competitive against every measurable rival on s(C);
- **(b)** no C ∈ 𝒫 has an all-world tie with an incoherent model through gates or the kernel, so direct (C) can fail only through installed records;
- **(c)** registering a new member never removes an existing member's defence. Gates only add acceptances, and the defence of C against X is C's own gate's verdict.

This is for Γ_K as defined, without Option B's refusals. With (J_ref), (a) holds for a post-jump B_n only if, whenever (J_ref) refuses B_n's gate at an edge world, B_n's gate passes at some world of A(T, X) (inheritance with nonempty sets, PP40 Lemma 2.1). That is OPEN.

*Proof.*
- **(a)** For a rival X, Σ_w λ_{C,w} V^C_w(C → X) = λ_C · Φ(C → X) + λ_C · Π^C(C → X). The first term is ≥ 0 by pointwise Bayes, and so is the second (tail densities, weakly guiding). The sum is > 0 unless X = C a.e., by uniqueness. So some w ∈ supp λ_C ⊆ s(C) has V^C_w > 0, and C's gate accepts there.
- **(b)** An all-world tie through C's gate needs V^C_w(C → X) = 0 at every w, so λ_C · V^C = 0, so X = C.
- **(c)** Immediate from the form of (I3). ∎

**What (I_Γ) does not give.**
- **(TC) across gates** (Prop 3.4) is not given.
- **Undominatedness against copies accepted through other gates** is not given. Rule III of AUDIT_completion can install reverses when another member's gate accepts X ⪯_w C at every w.
- **Closed sections with (J_ref)** are not given.

These are exactly where the audit's "allocation after closure" can fail: (I3) is an allocation fixed before closure, and closure rules II–III may add acceptances. Prop 4.1(c) shows that closure never *removes* a member's defence. But closure can add an acceptance that makes a (J_ref) or shadow refusal inconsistent, which is F1.

**Stopping rule applied.**

1. **First failing step.** The jump, under the commitment "one valuation per world" (Thm 2.4).
2. **Redesign.** Per-realiser valuations Γ_K.
3. **First failing step of the redesign.** Gate continuity at p_0 (Prop 2.8; Lemma 2.5 in the limit).
4. **Commitment responsible.** "Gate verdicts are valuation signs."
5. **Redesign of the redesign.** There are two routes:
   - Option A: path valuations kept apart from T's, subject to the one-sided comparison of §2.5;
   - Option B: the explicit inheritance refusal (J_ref) and PP40's shadows (B3), as non-valuation refusals.

   For Option B, the open problem is their (TC) against copies accepted through other gates.

I did not shrink the rival class: every statement above is for every measurable rival.

**The precise open problem left by this round.** Find, on I:
- per-member valuations satisfying (I_Γ);
- the refusals (J_ref) at the post-jump models' edge worlds and (B3) for installed records;

such that no record refused at a world is a copy of a record accepted through another member's gate at that world. In particular this must hold for the edge members B_12(t_n), which share their records with the post-jump models (Lemma 2.2).

A natural candidate is to make the post-jump models and the edge models **different** models: post-jump B_13(t), with (H_P) dropped, and a change of family before q_e. Remark 2.6 shows this is the one place Theorem 2.4's proof does not reach. That it gives a way through is CONJECTURE.

---

## 5. Status

| Result | Label |
|---|---|
| Lemma 1.1 (non-accumulation) | PROVED |
| Lemma 1.2 (edge monotonicity; T ≤_3 B_12(1); regions) | PROVED; CHECKED |
| Lemma 2.2 (edge selection onto, single valuation) | PROVED |
| Prop 2.3 (iso-level limit pair) | PROVED under (H_P), (H_inst) |
| Thm 2.4 (no single-valuation jump), Lemma 2.5 | PROVED under (H_P), (H_inst) |
| LP certificates for Thm 2.4; world-3 condition alone feasible for t ≠ 1 | NUMERICS |
| Prop 2.7 (jump closure in Γ_K) | PROVED |
| Prop 2.8 (gate continuity impossible) | PROVED under (NA) |
| Prop 3.4′ (common Bayes weights necessary) | PROVED under (NA) |
| Options A and B for the jump | OPEN |
| (J_ref) as the minimal non-additive layer; its (TC) on the edge | OPEN |
| Prop 3.1 (refinements not registrable) | PROVED |
| Prop 3.3 (gate-endorsed dominations: conditions for (a), (b), (c)) | PROVED (conditions); feasibility OPEN |
| Prop 3.4 (TC localisation in Γ_K), Prop 4.1 (competitiveness for all generations, incl. unbounded rivals) | PROVED |
| Cross-gate (TC); installation of the residues with shadows; all generations | OPEN |
| Post-jump family ≠ edge family escapes Thm 2.4 | CONJECTURE |

**Scripts** (`r9/PP41_py/`; run `python3 -I -B <script> > <script>.out` inside the folder; `twofield_lp.py` takes the sample size as its argument, 4000 used):

| Script | Content | Label |
|---|---|---|
| `exact41.py` → `exact41.out` | (a) T pointwise 3-better than B_12(1), strict on Sil(T) ∩ M_3; (b) edge monotonicity at worlds 1, 2; (c) threshold form of B_12(t); (d) the regions of Lemma 1.2(c) at six t ≠ 1 and empty R_1. ε ∈ {1/10, 3/10}. ALL PASS. | CHECKED |
| `twofield_lp.py` → `twofield_lp.out` | the two-world iso problem infeasible at 21 values of t for both edge worlds, with Lemma 2.5's certificates; world-3 iso alone feasible for t ≠ 1 | NUMERICS |
