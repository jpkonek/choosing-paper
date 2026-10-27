# Referee report, round 50: PP42, AUDIT_multicap, PP43

23 October 2026. Independent referee. I read BRIEF51_multicap, AUDIT_multicap, AUDIT_round51, AUDIT_round51_answers, BRIEF50, BRIEF49, AUDIT_completion §3–6, REFEREE_PP32_penalties §3.2 (the field ℓ^T), REFEREE_round49, PP42 and PP43 in full. I checked each listed claim line by line and edited no note. My scripts are in `r9/PP48_py/`. The authors' exact scripts were re-run from copies in `PP48_py/rerun/`; outputs are identical and ALL PASS (§4).

**Labels.** PROVED: complete argument, here or in the note, checked by me. CHECKED: exact rational computation. NUMERICS: sampling. CONJECTURE: unproved. "Unclear" means a gap I could neither close nor refute.

**Overall.** The positive core of PP42 survives: Lemma 3.0, the sufficiency half of Thm 3.1, Thm 3.2 (with two scope repairs), Thm 4.2, and the section argument of Prop 5.2. The audit's five repair items are all real. For three of them I supply the repair, and in two cases the repaired statement is stronger than the original.

1. **Thm 3.1(c): the agreement-region hypothesis is unnecessary.** Failure of the CG2 sandwich at a world breaks (TC) at that world, with no hypothesis about where the two models agree (§1.2; PROVED, CHECKED).
2. **An exact (TC) test for two-valued families (new, Thm R1).** Suppose no three gated members ever give three different answers at one problem, as in the multicap family. Then, under strict gates, (TC) holds iff every pair passes the sandwich and every triple admits common *nonnegative* constants. Under (BR) the constants can be taken positive. So for the multicap family with (BR), AUDIT_multicap's closed interval-triangle test is **necessary as well as sufficient**. A failed triple is then a failure of the gate-union design with those fields, not merely of a stronger sufficient test (§1.2; PROVED, CHECKED).
3. **Thm 4.3(a) is repaired** by a pointwise ratio bound, which is finite by homogeneity and compactness (§1.5; PROVED; constants NUMERICS).
4. **Thm 4.3(c): the stronger conclusion is true.** At world v the cap path admits **no** additive witness at all, of any form, not just no globally consistent rescaling constants (§1.5; PROVED).
5. **Thm 2.1(a) "iff" is false** (simple counterexample). Prop 5.1's "local finiteness" is unsupported in its uniform reading, and is in fact violated by Thm 4.3's own dominators (§1.1, §1.7).
6. **The section argument is stated as a general lemma (Lemma S, §1.8).** It needs no common integrable envelope: L¹-continuity of the field differences suffices.
7. **The union lemma is exactly true**, with no null-set exceptions, for all s with s_i + s_j ≤ ε. Its sign claim needs s_i ≤ 2ε/3 (CHECKED, 71,888 problems).
8. **PP43 Thm 2.1, Lemmas 3.1–3.3 and Thm 3.4 are correct.** Two small details in Lemma 3.2 and Lemma 3.3 should be written out (§3).

---

## 0. Verdicts at a glance

| Note | Claim | Verdict |
|---|---|---|
| PP42 | Thm 2.1(a) "⇐" (Bayes ⇒ competitive) | **wrong** (counterexample §1.1); "⇒" correct; "iff" holds for the maximal U-preorder only |
| PP42 | Thm 2.1(b), (c), (d) | correct ((d): on bounded records the witness is Φ) |
| PP42 | Lemma 3.0 | correct |
| PP42 | Thm 3.1(a), (b) (sufficiency of CG2 + CG3) | correct |
| PP42 | Thm 3.1(c) (necessity of CG2) | **correct with repair; stronger**: the agreement-region hypothesis can be dropped (§1.2) |
| PP42 | Thm 3.1(d) (weak necessity of CG3) | correct as a necessary condition; the description of the gap is incomplete (zero constants **and** orientation-dependent constants on D_123) |
| PP42 | §0/table "(TC) ⇔ CG2 + CG3" | **overstated**; the exact form for two-valued families is Thm R1 |
| PP42 | Thm 3.2(a) competitiveness, (b) undominatedness and direct (C), (c) strictness | correct ((c) under (R0) needs strict CG2, as stated) |
| PP42 | Thm 3.2(d) closure inert | **correct with repair**: rule II needs (TC), i.e. CG3 as well; the theorem assumes CG2 only |
| PP42 | Thm 3.2(e) monotone registration | correct for acceptances; "only new obligations are CG2/CG3" omits the new member's Bayes property and **closed sections** |
| PP42 | Prop 3.6 | correct (immediate) |
| PP42 | Lemma 4.1 (i)–(iii) | correct; CHECKED (re-run) |
| PP42 | Lemma 4.1 (iv) | correct (proof sketch adequate). Note that θ is a pointwise supremum and is about 2.4× the integral ratio that PP42's numerics report |
| PP42 | Thm 4.2 | correct |
| PP42 | Thm 4.3(a) | **correct with repair** (pointwise bound R_*, §1.5) |
| PP42 | Thm 4.3(b), (d) | correct ((d) with R replaced by R_*) |
| PP42 | Thm 4.3(c) | argument insufficient for the stated use; **conclusion true**, stronger version proved (§1.5) |
| PP42 | Prop 4.4(a) | correct; it omits a second inequality, which is automatic when a^n_wrong ≥ 1. By Thm R1 it is a genuine (TC) failure |
| PP42 | Prop 4.4(b) | correct, with an orientation slip in the interval (harmless). By §1.2 it is a genuine (TC) failure |
| PP42 | Prop 5.1 | correct under CG2 and (U) |
| PP42 | "local finiteness" | **unsupported** in the uniform reading, and false for Thm 4.3's dominators. The single-fill version is trivial from closed sections |
| PP42 | Prop 5.2 | correct (needs q injective). General form: Lemma S |
| AUDIT | Union lemma | correct, exactly (no null sets) for s_i + s_j ≤ ε; CHECKED |
| AUDIT | Members never give opposite answers | correct when every s_i ≤ 2ε/3 (u ∈ K_s); CHECKED |
| AUDIT | Interval criterion ⇔ CG2; triangle test ⇔ CG3 on this family | correct; with (BR) it is also necessary (Thm R1) |
| PP43 | Thm 2.1 (gate dominance) | correct |
| PP43 | Lemma 3.1 | correct |
| PP43 | Lemma 3.2 | correct; the S-points need G(s_2) < t, which holds for small η by Fact 1's uniform gap |
| PP43 | Lemma 3.3 | correct; P must be a full shell (as used) |
| PP43 | Thm 3.4 | correct |

---

## 1. PP42

### 1.1 Theorem 2.1: necessity only

**(a) "⇐" is false.** The following counterexample is PROVED.
- Take the guidance-only ranking: accept exactly the weak w-worsenings. Then U = ℓ^T is a witness at every world, and T is the a.e.-unique u-Bayes model of ℓ^T.
- Take bounded non-null G_k ⊆ Sil(T) ∩ M_k for k = 1, 2, 3, and put X := T[G_k ↦ k-correct, k = 1, 2, 3].
- At each world w, the piece G_w is a strict w-improvement, so rec(T, X) is a weak worsening at no world. It is refused at all three worlds, and T is not competitive.

**"⇒" is correct.** The argument runs as follows.
- Accepted implies U_w ≥ 0. So competitiveness on s puts the convex range {U(N → X) : X bounded} (Lyapunov) outside the open negative orthant on the coordinates in s.
- Separation then gives λ ∈ Δ_s with λ·U(N → X) ≥ 0.
- Single-point changes N[E ↦ a] give pointwise *weak* λ-optimality.

So "registrable models are exactly the U-Bayes models" (§0 item 1) should read "are among". Equality holds for the maximal preorder.

**(b) and (c)** are correct.
- In (c), sections are sublevel sets {p : U_w(C_p) ≤ U_w(X)}.
- The values U_w(X) fill an interval (Lyapunov), so closedness for every rival is lower semicontinuity.

**(d)** is correct on bounded records: PP43's tail functional vanishes there, so the witness is Φ = ℓ^T. PP43's U is not an integral of a field, but (a) only uses bounded records.

**Corollary 2.2 and Prop 2.3** use only the "⇒" direction, so they stand.

### 1.2 Theorem 3.1: sufficiency correct; necessity sharper than stated

**Lemma 3.0 and Thm 3.1(a), (b): correct.**
- In Lemma 3.0 I checked the shortcut step: δ^N is increasing in rank and gate edges go to every advice. I also checked that a cycle on at most three old values contains a positive simple 2- or 3-cycle.
- The 2-cycles are exactly pointwise CG2 on D_NM. Different members sharing an old value cause no problem.
- In the strict case the slack can be taken measurable and a.e. positive.
- In Thm 3.1 the telescoping is pointwise, and ranks are injective. So an accepted triangle is trivial.

**Thm 3.1(c) without the agreement-region hypothesis (PROVED; CHECKED in `tc_twovalued.out` (B), 324 exact instances with {N = M} empty).** Suppose the sandwich fails at w for gated N, M: ess sup_{f^N<0} f^M/f^N > ess inf_{f^N>0} f^M/f^N. Then (TC) fails at w, under (R) and under (R0).

*Proof.*
1. As in the note, choose bounded D ⊆ D_NM with ∫_D f^N > 0 > ∫_D f^M, made of a piece A′ ⊆ {f^N > 0} and a piece B′ ⊆ {f^N < 0}. On B′, M is strictly w-better than N, so **N is not w-correct there**.
2. Take a non-null D_0 ⊆ B′, small. Put X := N, Y := N[D ↦ M] and Z := N[D_0 ↦ w-correct].
3. **X ⪯ Y**: this is (D, N → M) through N's gate, with value ∫_D f^N > 0.
4. **Y ⪯ Z**: on its support (D ∖ D_0, or D if M is not w-correct on D_0), the old side is M, so M realises it. Its M-value is −∫_D f^M plus a term of size O(∫_{D_0} env). This is > 0 for small D_0.
5. **Z ⪯ X**: this is (D_0, correct → N), a strict w-worsening, so guidance accepts it.
6. **The reverse X ⪯ Z** is a nontrivial pure w-improvement: every field rates it < 0, and guidance refuses it. ∎

The only difference from the note is that the improvement is placed inside D, where N is necessarily imperfect.

**Degenerate case.** If the move is one-signed, the sandwich holds trivially. CG2 with *positive* constants can still fail if the ratio is unbounded, but then (TC) need not fail. So the exact pair condition is the sandwich, equivalently CG2 with constants in [0, ∞)² ∖ {0}. Under (BR) the two coincide.

**Theorem R1 (exact triple test; PROVED; CHECKED in `tc_twovalued.out` (A)).** Work at world w under (R).
- **(ii) Necessity, for any TWG family.** Assume the sandwich holds for every pair of gated members. Suppose that for gated N_1, N_2, N_3 there is no c ∈ [0, ∞)³ ∖ {0} with c_i δ^i(N_i → N_j) + c_j δ^j(N_j → N_i) ≤ 0 a.e. on D_ij, for all three pairs. Then (TC) fails at w.
- **(iii) Sufficiency, two-valued case.** Suppose D_123 is null for every triple of gated members, and every pair and every triple admits such nonnegative nonzero constants. Then no nontrivial triangle is accepted at w. In particular (TC) holds.
- **(iv) Positivity under (BR).** Under (BR), nonnegative solutions can be perturbed to positive ones. So for two-valued families with (BR), (TC) under (R) holds **iff** the closed interval-triangle test 0 ∈ I_AB + I_BC + I_CA holds for every triple.

*Proof of (ii).*
1. **Three patterns.** Use three types of points:
   - (a) on D_12: X = N_1, Y = N_2, Z = N_1;
   - (b) on D_23: X = Y = N_2, Z = N_3;
   - (c) on D_31: X = N_1, Y = Z = N_3.
2. **Realisers.** Every link is realised by its own gate: rec(X, Y) by N_1, rec(Y, Z) by N_2, rec(Z, X) by N_3. Only two values occur at each point, so this works in any family, including on D_123.
3. **Separation.** The vector of the three gate values ranges over a convex set; take a fractional relaxation and use Lyapunov to recover disjoint sets. If this set misses the open positive orthant, separation gives c ≥ 0, c ≠ 0, with c · (value) ≤ 0. Localising gives the three pairwise inequalities a.e.
4. **Contrapositive.** If no such c exists, some bounded a, b, c give three accepted links.
5. **Reverses.** The reverse of a gate-accepted link is refused by every route:
   - by guidance, since the forward link would then be a weak improvement;
   - by any other realiser P, by the pair condition (N_i, P), using strictness of (R).

*Proof of (iii).*
1. Run Lemma 3.0 with the nonnegative constants. Gate edges of weight 0 create no positive cycle. 3-cycles live on the null set D_123.
2. Every triangle with three distinct gates contains a link whose constant is positive. Its 𝒰-value is then > 0, which contradicts telescoping.
3. Triangles with two gates use the pair constants, and single-gate triangles use the field itself.

*Proof of (iv).* A zero constant c_i with c_j > 0 forces the move N_j → N_i to be one-signed (never worse for N_j). Under (BR) a small positive c_i then still satisfies the inequality. Pairs of zero constants are lifted inside their own (nonempty) pair interval. ∎

**Consequences.**
- **For PP42.** "(TC) ⇔ CG2 + CG3" is right for two-valued families with (BR) under (R), which covers the cap path and the multicap family.
- **For general families.** On D_123, the necessary condition from (ii) plus 3-valued points is **per orientation**: one c for the cycle 1→2→3 and possibly another for 1→3→2. PP42's CG3 asks for one c for both. Thm 3.1(d)'s "the gap is the degenerate case of a zero constant" therefore understates the gap. Whether per-orientation constants suffice in general is OPEN. It is irrelevant to the multicap family, where D_123 is null.
- **For R0.** Under (R0) only the sufficiency (strict versions, Thm 3.1(b)) and the pair necessity are established.

**Numerics of the check.** On 6,000 random two-valued instances, 7,280 triples were tested.
- In all 7,180 triples where criterion N holds, the violation LP is infeasible.
- In each of the 100 triples where N fails, the LP's witness was converted to exact rationals and rebuilt as X, Y, Z. The three links were confirmed accepted and a reverse refused, under every member's gate.
- In finite instances (BR) holds automatically, and no triple needed a zero constant, as (iv) predicts.

### 1.3 Theorem 3.2 and Proposition 3.6

**(a), (b), (c): correct.**
- (a) and (b) are as written. In (b) the realiser M ≠ N, and D ⊆ D_MN. Vertex models carry no gate.
- The vertex models' own undominatedness needs a separate line, which is easy: V_k is pointwise k-best, so X ⪯_k V_k is refused for X ≠ V_k.
- In (c), under (R0), strictness needs strict CG2. The theorem says so.

**(d) needs CG3.** Rule II is inert only if (TC) holds, and Thm 3.1 needs CG3 (or Thm R1's triple condition). Thm 3.2's hypothesis lists CG2 only, and §0 says "under CG2 alone". The fix is to add the triple condition to (d). Rules III and IV are inert by (b). F1 is excluded by strict (G), and F2 by (b).

**(e): correct as to acceptances.** Registration only adds acceptances, so every defence and every domination survives. The new obligations are:
- the new member's own Bayes property;
- the pair and triple conditions involving it;
- **closed sections.** A new gate accepts records out of every selected model that agrees with the new member on the record's support. Added acceptances along a sequence of indices can break closedness at the limit index.

**Prop 3.6: correct (immediate).** The world-w field drops out of λ·ℓ^M. One caveat: a boundary supporting weight requires uniqueness from the remaining two worlds' fields.

### 1.4 Lemma 4.1 and Theorem 4.2

**Lemma 4.1 (i)–(iii): correct.** In (ii), at the minimiser over M we have σ m_v·g ≤ 0 < σ u·g, which gives σ g_v < 0 strictly, even on the boundary. In (iii) the A/B labels are forced by σ g_v < 0. `caps_exact` re-run: identical output, ALL PASS.

**Lemma 4.1 (iv): correct.** The proof is a sketch, but its ingredients hold:
- u·d = 0 on Γ_v (REFEREE_PP32 Fact 3);
- d is continuous and positively homogeneous;
- d_v/|g| is bounded below near Γ_v (made explicit in §1.5).

One caution about the numbers: θ is a *pointwise* supremum, while PP42's numerics report the integral ratio u·Φ/Φ_v.

| s | θ (pointwise; my numerics) | u·Φ/Φ_v (PP42) |
|---|---|---|
| ε/5 | 0.071 | 0.030 |
| ε/10 | 0.038 | 0.015 |
| ε/20 | 0.019 | 0.008 |
| ε/40 | 0.010 | 0.004 |

All values are at ε = 0.3, v = 3 (my values: `pointwise_R.out`; PP42's: caps_mc). Thm 4.3's requirement θ(s_0) < 1/18 holds from about s_0 = ε/10 (NUMERICS).

**Thm 4.2: correct.** I checked:
- the two Bayes inequalities (a(1 − 3θ) > 1/2 ≥ b; and (a − b)α_v > 0 for −σ);
- the decomposition rec(C, X) = (H_s : σ → S) ∪ (G : S → N), disjoint by (F2);
- the sign choices for a and b;
- CG2 for (T, C): at v it is one-signed with c_T ≤ b·c_C; at w ≠ v, f^C = a·f^T.

### 1.5 Theorem 4.3

**(a) The gap.** The audit is right. The Bayes step needs, at each point of H_s:
- (σ vs S) η(|d_w| + |d_w′|) < ((1 − 3θ) − b)·d_v;
- (S vs −σ) η(|d′_w| + |d′_w′|) < (1 − b)·α_v.

R, however, is defined as a ratio of integrals.

**Repair (PROVED).** Put

  R_* := ess sup over H_{s_0} of max{ (|d_w| + |d_w′|)/d_v , (|d′_w| + |d′_w′|)/α_v },

and choose ηR_* < 1/36. Since ∫|d_w| ≤ R_* ∫ d_v, also R ≤ R_*, so (d) is unaffected.

**R_* is finite for small s_0.**
1. **Upper bound.** α, β, γ are positively homogeneous of degree 1 and ≤ C|g|, because F(θ) ≤ 1 + Lθ and G(s) ≤ max(s/L, 2ds, 2).
2. **Lower bounds on β_v and α_v.**
   - On M_v: β_v = α_v = |g_v|.
   - On M_j (j ≠ v): β_v = |g_j|F(|g_v|/|g_j|) ≥ |g_v|, because F(θ) ≥ θ (F(θ)/θ ≥ min(1/(2d), L) > 1).
   - On M_j: α_v ≥ min(|g_v|, |g_j|)/(1 + L), because G(s) ≥ s/(s + L).
3. **The compact limit set.** As s → 0, the normalised H_s lies in any neighbourhood of Γ_v := {|g| = 1, m_v·g = 0, σ m_j·g ≥ 0 for j ≠ v}.
   - On Γ_v, g_v ≠ 0. If g_v = 0, then Σg = 0 and σg_j, σg_k ≥ 0 force g = 0.
   - On Γ_v ∩ cl M_j, g_j ≠ 0. If g_j = 0, then c·g_k + (c + ε)·g_v = 0 with g_v and g_k of the same sign, forcing g = 0.
4. **Conclusion.** By compactness, |g_v| and |g_j| are ≥ κ|g| on H_{s_0} for some κ > 0. Hence R_* ≤ C(1 + L)/κ.

With b < 1/6 and θ < 1/18, both inequalities hold. NUMERICS (`pointwise_R.out`, ε = 0.3):
- R_* ≈ 8.45. It is driven by the −σ comparison; the σ-vs-S ratio is ≈ 2.95.
- R ≈ 0.5.
- d_v/|g| ≥ 0.40 and α_v/|g| ≥ 0.12 on H_{s_0}.
- With b = 0.1 and η = 1/(40R_*), σ is the strict u-optimum at every sampled point of H_s, for s ∈ {s_0, s_0/2, s_0/4} and s_0 ∈ {ε/10, ε/20, ε/40}.

**(b): correct.**
- Pairs: at v, c_s < b·c_{s′}; at w ≠ v, c_s/c_{s′} ∈ (1 − η, 1 + η), strictly.
- D_123 is empty for nested caps.
- Constants increasing geometrically along each triple work.

**(c): conclusion true, and a stronger form holds.** The note's argument excludes only globally consistent constants. The audit is right that this does not by itself exclude every witness. The following closes the gap.

**Proposition R2 (no witness at world v; PROVED).** In 𝒫_v (any b < 1, under (R) or (R0)), there is no additive U_v, strictly guiding on bounded records, with U_v ≥ 0 on every accepted bounded record at v. So Thm 2.1 does not apply to 𝒫_v, and the cap path is not a single-field realisation.

*Proof.*
1. **The ratio κ.** Let ρ := U_v(σ) − U_v(S), which is > 0 a.e. on H_{s_0}. Put κ := ρ/d_v > 0.
2. **One accepted record.** For s < s_0, take bounded D_1 ⊆ H_s and D_2 ⊆ H_{s_0} ∖ H_s. The record (D_1 : σ → S) ∪ (D_2 : S → σ) is realised by C_s, which is σ on H_s and silent off it. Its C_s-value at v is −b∫_{D_1} d_v + ∫_{D_2} d_v.
3. **The constraint.** Whenever that value is > 0, the witness needs −∫_{D_1} κ d_v + ∫_{D_2} κ d_v ≥ 0. By non-atomicity this forces

     a(s) := ess sup_{H_s} κ ≤ b · ess inf_{H_{s_0} ∖ H_s} κ.

4. **Iteration.** For s < s″ < s_0 this gives a(s) ≤ b·a(s″), and a(s″) is finite. The shells H_{s″} ∖ H_s are non-null, because they contain open sets of planes. Inserting k intermediate cut sizes gives a(s) ≤ b^k·a(s″), so a(s) = 0. This contradicts κ > 0. ∎

**(d): correct** with R replaced by R_*. The checks:
- x > y/2 because Σ_w Φ^T_w(T → X) > 0;
- the self-margin is ≥ (1/2 − 3θ/2 − ηR)Φ_v(s), which uses the integral R correctly;
- the interval (3y, x/b) is nonempty because b < 1/6, and the intermediate value theorem supplies s.

### 1.6 Proposition 4.4

**(a): correct**, with exact constants:
- CG2 is tight with ratio a_m for (T, C_m) and for (C_n, C_m) on H_m ∖ H_n, and a_n for (T, C_n);
- CG3 then forces a_n = 1.

In the humble version, the triangle test gives *two* conditions:
- a^n_corr·a^m_corr ≤ a^m_wrong (stated in the note);
- a^n_wrong·a^m_wrong ≥ a^m_corr (omitted; automatic when a^n_wrong ≥ 1).

All three pairs are two-signed at w ≠ v and satisfy (BR). So by Thm R1(iv) these are genuine (TC) failures under (R), not failures of a sufficient test.

**(b): correct.** The interval on H^{v′} should read c/c′ ∈ [1 − η, 1 + η], not (1/(1 + η), 1/(1 − η)). On H^v, c′ ≤ b·c. The two are incompatible iff b < 1/(1 + η), which holds. The sandwich itself fails (ess sup over the negative region is 1/b > ess inf over the positive region, 1 + η). So by §1.2 this is a genuine (TC) failure of that field pair at world v, not of the test.

### 1.7 Proposition 5.1 and "local finiteness"

**Prop 5.1: correct** under CG2 and (U).
- Closed sections pass C_n ⪯_w X_k to C*.
- CG2 then bounds Φ^T_w(T → C*) ≤ o(1).
- T's uniqueness gives C* = T.
- The last step ("T does not dominate X_k") uses T ⪯_w X_k at all w together with direct (C) for T (Thm 3.2(b)), which yields strictness at some world.

**"Locally finite" is not established.**
- **The trivial part.** For a *single* fill X not dominated by T, closed sections alone show that {p : C_p ⪯_w X for all w} is closed and excludes p_T. No CG2 or (U) is needed.
- **The uniform reading is false.** Read uniformly ("dominators of small fills come from a bounded part of the path"), the claim fails for Thm 4.3 itself. A fill X_k with x_k → 0 needs Φ_v(s_k) < x_k/b, so its dominating cut sizes satisfy s_k → 0. Dominator indices of a vanishing sequence of fills therefore accumulate at p_T, consistently with closed sections.
- **What Prop 5.1 forbids** is only the single-sequence pattern "C_n dominates every X_k for n ≥ n(k)".

### 1.8 Proposition 5.2 and the general section lemma

**Prop 5.2: correct.** I checked each step:
- the realisers' indices are compact;
- 1_{S_n} → 1_{S*} in measure;
- the limit realiser realises the limit record;
- dominated convergence applies with bound (1 + η)·2·env(ℓ^T);
- guidance passes to a.e. limits.

The path q must be a continuous injection, so that the selection is well defined and q is a homeomorphism onto its image; the note does not say this. One side note: under (R0), T's gate now also accepts records with Φ^T_w = 0. That is a (harmless) change to T's verdicts, so "all of T's own verdicts are unchanged" (§0 item 2) should be qualified.

**Lemma S (closed sections for a compact gated family; PROVED).** Fix a world w.

*Data.*
- (Ω, μ) is a finite non-atomic measure space (here R³ with the Gaussian measure). A is a finite advice set, with injective rank r_w.
- **Gated family.** Θ is a compact metric space. For each θ ∈ Θ there are a measurable model N_θ : Ω → A and a field ℓ^θ_w. Put Δ^θ(g; a, b) := ℓ^θ_w(g, b) − ℓ^θ_w(g, a).
- **Selection.** I is a metric space (the index domain), with a map p ↦ C_p into measurable models. C_p need not be gated.
- **Acceptance at w.** rec(Y, X) is accepted iff
  - (G) r_w(X) ≥ r_w(Y) a.e. on {Y ≠ X}; or
  - (R0) some θ ∈ Θ has N_θ = Y a.e. on {Y ≠ X} and ∫_{Y≠X} Δ^θ(g; Y(g), X(g)) dμ ≥ 0.

*Hypotheses.*
- **(S1)** θ ↦ N_θ is continuous in measure.
- **(S2)** For each pair a, b ∈ A, θ ↦ Δ^θ(·; a, b) is continuous from Θ into L¹(μ). A sufficient condition is that the differences converge in measure under a common integrable envelope.
- **(S3)** p ↦ C_p is continuous in measure on I. If C_p = N_{θ(p)} with θ : I → Θ continuous, this follows from (S1).
- **(S4)** There are no other acceptance routes at w: no kernel, no installed records, and no gates outside Θ. Finitely many extra gated models may be added to Θ as isolated points.

*Conclusion.* For every measurable rival X, the section A_w(X) = {p ∈ I : C_p ⪯_w X} is closed in I. In particular, inheritance holds at every limit index in I.

*Proof.* Let p_n → p in I with C_{p_n} ⪯_w X. Pass to a subsequence in which all acceptances use the same route.
1. **Guidance.** Along a further subsequence, C_{p_n}(g) = C_p(g) eventually, for a.e. g, because there are finitely many values. So the rank inequality passes to the limit.
2. **Gates.** Let θ_n be the realisers. By compactness, θ_n → θ along a subsequence. Put S_n := {C_{p_n} ≠ X}, S := {C_p ≠ X} and E_n := {C_{p_n} ≠ C_p}, so μ(E_n) → 0 and S_n Δ S ⊆ E_n.
   - **Realisation.** μ(S ∩ {N_θ ≠ C_p}) ≤ μ(E_n) + μ{N_{θ_n} ≠ N_θ} + μ(E_n) → 0. So N_θ realises rec(C_p, X).
   - **Values.** Put V_n := ∫_{S_n} Δ^{θ_n}(C_{p_n}, X) and V := ∫_S Δ^θ(C_p, X). Then

       |V_n − V| ≤ Σ_{a,b} ‖Δ^{θ_n}(a, b) − Δ^θ(a, b)‖_1 + ∫_{E_n} 2 max_{a,b} |Δ^θ(a, b)|.

     The first term → 0 by (S2). The second → 0 by absolute continuity of a single integral, since μ(E_n) → 0. So V = lim V_n ≥ 0, and (R0) accepts. ∎

*Remarks for round 51.*
1. **Zero acceptance.** Zero acceptance is used only at the last step. Under strict (R) the lemma fails in general, because limits of positive values can be 0. (TC) under (R0) needs the strict compatibility of PP42 Thm 3.1(b); that is a separate obligation from Lemma S.
2. **Compactness of Θ.** The realisers range over **all** gated members, not just the selected ones. So Θ must be the closed family: the box [0, δ]³ including its faces, with T's field as the s = 0 field.
3. **(S1) for the box.** For K_s, s ∈ [0, δ]³, (S1) holds. The vertices of K_s move continuously, and for fixed s the planes {g : k·g = 0} through the vertices are null, so C_{s_n} → C_s a.e.
4. **(S2) for the box.** (S2) is a design requirement. A sufficient form is ℓ^s_w = κ_s·ℓ^0_w, where κ_s is a bounded positive factor, constant on each corner band and each sign region, and ℓ^0 has an integrable envelope. Indicators of H_i(s_i) are continuous in measure (μ(H_i(t) Δ H_i(t′)) → 0), so such factors converge in measure.
5. **(S3) and the index map.** (S3) is a hypothesis of this sufficient lemma, not an axiom. It holds for any continuous index map p ↦ s(p).
6. **Scope of the conclusion.** The lemma is per world, for every measurable rival, bounded or not. It says nothing about (TC), Bayes properties or competitiveness.

---

## 2. AUDIT_multicap

### 2.1 The union lemma: correct, exactly

**The connectedness argument.** It is correct, and it needs no null-set exceptions.
- O_i := {m ∈ M : m_i > c + ε − s_i} is relatively open in M.
- The O_i are pairwise disjoint whenever s_i + s_j ≤ ε. Indeed m_i + m_j > 2c + 2ε − s_i − s_j ≥ 2c + ε = 1 − c ≥ m_i + m_j would be a contradiction. So they stay disjoint even when two corners touch.
- N_g := {m ∈ M : m·g ≤ 0} is convex, hence connected. If N_g ⊆ ⋃ O_i, the traces N_g ∩ O_i partition N_g into relatively open sets, so N_g lies in a single O_i.

**The cases raised in the brief.**
- **Low-dimensional N_g.** If N_g is a segment or a point, the argument above applies unchanged.
- **N_g meeting two corners.** If N_g meets two corners, it is not contained in their union, since it is connected and the corners are disjoint. So it meets K_s, and then K_s, K_i(s_i) and K_j(s_j) are all silent. This agrees with the identity.
- **Conventions.** The identity holds pointwise for every g, under the strict convention (accept g iff min_K m·g > 0) and under the non-strict one (with N_g := {m·g < 0}), provided all models use the same convention.

**Disjointness of the H_i** needs only K_s ≠ ∅. If K_i accepts g and K_j accepts g, then N_g lies in O_i ∩ O_j = ∅, which is impossible. If K_j accepts −g, a common point of K_i and K_j gives a contradiction.

**Members never give opposite answers.** This is correct when **u ∈ K_s, i.e. every s_i ≤ 2ε/3**. All answers then have the sign of u·g, and every member is silent when u·g = 0. If K_s is nonempty but excludes u, members still never give opposite answers (all contain K_s), but the sign claim fails.

**CHECKED (`union_identity.out`, exact rationals, ALL PASS).** The check covers:
- 71,888 problems, under both conventions;
- ε ∈ {1/10, 3/10, 1/2, 9/10};
- random s ∈ [0, δ]³; touching corners s_i + s_j = ε with s_i ≤ 2ε/3; and cuts deeper than 2ε/3, where only (U1)–(U3) are checked;
- random problems, problems orthogonal to a vertex of K_s or M, and problems orthogonal to two vertices (cut points, edges);
- 6,152 problems in the union, of which 3,283 lie on a boundary plane;
- all eight sub-cut models.

A first run that applied the sign check to cuts deeper than 2ε/3 produced sign failures, which confirms that this hypothesis is needed.

### 2.2 The interval criterion: correct

- **CG2 as an interval.** With c_N = e^{x_N}, the condition c_N f^N ≤ c_M f^M is, on {f^N > 0}, x_N − x_M ≤ U_NM, and on {f^N < 0}, x_N − x_M ≥ L_NM. The ratios are positive because the f's share a sign.
- **Reversal.** I_MN = −I_NM: f′ = −f leaves the ratio unchanged and swaps the sign sets.
- **The triangle test** is Minkowski-sum feasibility.
- **Strict version.** The strict feasible set includes an endpoint exactly when the extremum is attained only on a null set. The open-interval version is a safe sufficient choice.
- **Relation to CG3.** By the union lemma D_123 = ∅ for every gated triple in the family. So PP42's CG3 is exactly the triangle test, and the test is sufficient by PP42 Thm 3.1, which is correct and therefore no longer "conditional".
- **Necessity.** The audit asserts no necessity. Thm R1 supplies it: under (R) with (BR), the closed interval test is necessary and sufficient. Without (BR), allow x_N = −∞ (zero constants).
- **Per-triple constants are enough** (Thm 3.1's proof uses one triangle at a time). Global consistency is a strictly stronger, unneeded restriction (Prop 3.5(ii), CHECKED (c) re-run).

**One caution for round 51.** Two-valuedness is a property of the gated multicap family *together with* T. Gating any other model, such as an edge or vertex model, can create three distinct answers at one problem. The D_123 inequalities of CG3 then return.

---

## 3. PP43

**Thm 2.1 (gate dominance): correct.**
- Step 1: every accepted record has U_w ≥ 0, with equality only for trivial records or bounded kernel records with Φ_w = 0. Φ is finite and strictly guiding on all records, and Π^U ≥ 0 on weak worsenings.
- Step 3: U telescopes, because Π^U is a Banach limit of linear functionals. The reverse of a bounded Φ = 0 edge is accepted by the kernel.
- Step 5: "Bayes for U" must be read as Φ pointwise strictly optimal and Π^U pointwise weakly optimal at λ_C. Thm 2.3 verifies exactly that.

**Lemma 3.1: correct.** Refusal through B_n's own gate gives V ≤ 0 under any zero rule. Additivity gives V^{B_n}_w(B_n → X) = v_w + Φ_w(T → X) = v_w − α_w(F).

**Lemma 3.2: correct.** One detail needs writing out. The S-points need G(s_2) ≤ t as well as F(s_2) = t + η, and this holds for small η. Fact 1 gives F(θ)F(1/θ) ≥ κ_0 > 1, so G(s_2) ≤ (t + η)/κ_0 < t. The decomposition (4m + |x| + |y| = (μ·d)(1 + t)/η) and the ball/Lyapunov step are right. ε_0 = 1/max(coefficient). `exact43` re-run: identical, ALL PASS.

**Lemma 3.3: correct.** P must be a full spherical shell, as used, so that every non-null cone meets P ⊆ supp r.

**Thm 3.4: correct.** I checked:
- μ·π(D) ≤ max_{w∈{i,j}} v_w − h < 0;
- d = q − (c/2)·1 has μ·d = c/2;
- Π^B(B → X*) = π(S) = −εq, since for large radii X* agrees with the conic record;
- the total is −(εc/2)·1 + O(εc/4) at every world.

On the excluded routes:
- every other coherent realiser is blocked by the shell;
- guidance is blocked, because both perturbation types carry positive weight (m > 0);
- the kernel is blocked, because the record is unbounded;
- installed copies are blocked by (H_rc).

Lemma 3.1 together with h ≥ h_0 makes every large n qualify. The cited margin h_0 > 0 (PP40 Lemma 2.2) was not re-refereed here.

---

## 4. Scripts (`r9/PP48_py/`; run `python3 -I -B <script> > <script>.out` inside the folder)

| Script | Content | Label |
|---|---|---|
| `union_identity.py` | Union lemma (U1)–(U4), exact, both conventions, boundary problems, touching corners, deep cuts | CHECKED, ALL PASS |
| `tc_twovalued.py` | (A) Thm R1: 7,280 triples; every TC-violating witness rebuilt and verified exactly against all gates; LP duals confirmed. (B) Thm 3.1(c) without the agreement region: 324 exact TC failures | CHECKED (witnesses exact; LPs only propose), ALL PASS |
| `pointwise_R.py` | θ pointwise vs integral; R_*, R; lower bounds on d_v/\|g\| and α_v/\|g\|; humble-field Bayes at sampled points | NUMERICS |
| `rerun/` | PP42 `tc_local_witness`, `caps_exact`; PP43 `exact43`, re-run from copies | identical outputs, ALL PASS |

---

## 5. What round 51 can take as settled

1. **Field design for the box.** For the multicap box with (BR) fields under strict gates, the pair sandwich and the closed interval-triangle test are **exactly** (TC) (Thm R1). A failed triple is then a failure of those fields in the gate-union design, not of an over-strong sufficient test. Under (R0), which Lemma S needs, use the strict (open) test. It is sufficient; its exact necessity under (R0) is OPEN.
2. **Closed sections on the 3-parameter box.** Lemma S gives them for any continuous index map, provided:
   - the box is closed, including its faces and T's field at s = 0;
   - the field differences are L¹-continuous in s;
   - the gates accept zero;
   - there are no other routes.
3. **Bayes estimates must be pointwise.** The bound R_* of §1.5 is the right type of quantity. In the cap computations it is dominated by the −σ comparison.
4. **A template against witnesses.** Prop R2's argument applies to any family that contains a continuum of nested discounted cuts at one world.
5. **Do not rely on "local finiteness".** Only the single-fill version holds.
