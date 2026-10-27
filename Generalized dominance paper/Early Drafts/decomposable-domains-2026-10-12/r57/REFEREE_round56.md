# REFEREE for round 57 (file name as briefed: REFEREE_round56): PP67, PP68 and the audit's geometry

24 October 2026. Independent referee. Scope: PP67 (Prop 1.1, Lemma 3.1, Prop 3.2, Thms 4.1, 5.1, 6.1, Props 7.1–7.4); PP68 (§1 including §1(b), Props 2.1–2.2, §3, §4, §5); the geometric claims in AUDIT_round57.md, AUDIT_round57_two_direction.md and AUDIT_round57_answers.md. I read these with BRIEF57, BRIEF56, LEAD_selection_count §1, AUDIT_completion, the PP59 ledger and DESIGN_MEMO §8.25 (including its correction bullets). Setting and axioms are those of Brief 57. I add no axiom; every extra hypothesis I need is named where it enters.

**Labels.**
- PROVED: the argument is complete here, or I checked the author's argument line by line.
- CHECKED: an exact computation in `r9/REFEREE56_py/`, marked *re-run* (author's script, output identical) or *independent* (my code, written from scratch).
- NUMERICS: sampled, illustration only.

**Verdict scale.** correct / correct with repair / wrong.

**Conventions.**
- X ⪯_w Y: X is at least as good as Y at world w.
- (TC) is used only in its triangle form: an accepted triangle X ⪯ Y ⪯ Z ⪯ X needs all three reverses. I re-checked that every derivation below closes with an explicit third link, usually a guidance link, and never uses plain transitivity.
- L := {T ≠ N}. P_w := the part of L where N is strictly w-better than T.
- Q₃ := Sil(T) ∩ M₃, and R_B := M₃ ∩ {T = B}.
- Sil(N) ∩ M₃ = Q₃ ∪ R_B = {g ∈ M₃ : v₃·g < 0}.

---

## 0. Verdicts

| # | Item | Verdict |
|---|---|---|
| 1a | PP67 Prop 1.1 (N is the least coherent model weakly 3-worse than T) | **correct** (independent exact polygon check). The surrounding claim that G-closure is "derived" is **wrong**: it is optional, as the audit says (§1.1). |
| 1b | PP67 Lemma 3.1 (signed closure) | **correct with repair** (wording of the range of H′ in (b); §1.2) |
| 1c | PP67 Prop 3.2 | **correct with repair**: its Z_H row is vacuous (§1.3) |
| 1d | PP67 Thm 4.1 (certificate) | **correct**. It is total. It satisfies reflexivity, (IB), strict (G) and (TC) for all measurable models, and protection, direct (C) and defence for T, N and D\*. It does not give (S), sections or global (C). N strictly dominates every X_E, E = E₀ included. Two misprints in the text (§1.4). |
| 1e | PP67 Thm 5.1 | **correct within the module**. The costs are those PP68 Prop 2.1 identifies (§1.5). |
| 1f | PP67 Thm 6.1 | **correct** (re-run, and independent census and LP: 39 types; §1.6) |
| 1g | PP67 Prop 7.1 | fill half **correct**. Retreat half **vacuous**, as the audit says (P₁ ∪ P₂ = L, CHECKED). A non-vacuous single-world form holds (§1.7). |
| 1h | PP67 Props 7.2, 7.3, 7.4 | **correct**, under the exact hypotheses listed in §1.8. 7.2(ii) needs "uniform". |
| 2a | PP68 §1: Thm 1.1, Lemma 1.2, Prop 1.3, Prop 1.4 | **correct with repair**. Minor provisos: E_m must be non-conic in §1(b), and E₀ must meet {m·g > 0} in Prop 1.3(c). §1(b) (upward sharing) stands under its hypothesis (§2.1). |
| 2b | PP68 Props 2.1, 2.2 | **correct** |
| 2c | PP68 §3 | **correct** |
| 2d | PP68 Lemma 4.1, Lemma 4.2, Thm 4.3 | **correct** (re-run; independent SAT using only (TC), (G), (IB) and defence). The 3-cycle core does not need its first edge (§2.4). |
| 2e | PP68 Thm 4.4 | **correct with repair**. The edge relation must be domination, not just →₃ (§2.4). |
| 2f | PP68 Prop 4.5 | geometry **correct**. "L₀ dominates N's fills, CHECKED on cells" does **not** cover all measurable fills. **Repaired**: a full-domain certificate 𝒲⁺ (PROVED, §2.5). |
| 2g | PP68 Prop 4.6 (the chain conv(v₃ + t(h₁₂ − v₃), M₀)) | **correct**. It is now PROVED for all t, not only checked on a grid. It is geometry only (§2.6). |
| 2h | PP68 Prop 4.7 | (a) **correct**. (b) **wrong**: the comparison is reversed, as the audit says. 𝒲 is an explicit model of the axioms in which the clause it cites fails (§2.7). |
| 2i | PP68 §5 (mixed classes) | **correct** at certificate level (§2.8) |
| 3a | Audit: path obstruction | **correct**. The exact example is confirmed (−2/30 and 14/30). It is PP36 Lemma E(ii) in this family (§3.1). |
| 3b | Audit: vacuity P₁ ∪ P₂ = L | **correct** (§3.2) |
| 3c | Audit: thresholds τ for F_t; quartile window; recurrence | **correct**. The closed quartile window works because τ has an atomless law (§3.3). |
| 3d | Audit: thresholds σ for R_α; restore/withdraw lemma | **correct**. The guarantee is at world 3 only: I give an α at which R_α is pointwise worse at world 2 (§3.4). |
| 3e | Audit: splice identity N[H ↦ T] = T[L∖H ↦ N] | **correct** (§3.5) |
| 3f | Audit: bridge J_β; K_{L₀} ⊆ K_N; advice changes only on {N ≠ L₀} | **correct** (§3.5) |
| 3g | Audit: F₀ = N on the world-3 minority region M₃ | **correct** (§3.5) |

**Bottom line.**
- **The first-generation module stands.** That is PP67 Prop 1.1, Lemma 3.1, Thms 4.1, 5.1 and 6.1, together with PP68's forced structure.
- **The audit's three corrections are confirmed**: the reversed comparison in Prop 4.7(b), the vacuity of the retreat half of Prop 7.1, and the optionality of G-closure. Every geometric claim the audit makes is correct.
- **Two items are strengthened here:**
  - L₀'s domination of N's class-3 fills now has a certificate for **all measurable fills**, not only cells;
  - PP68's chain is now proved for all t.
- **Two hypotheses need tightening:** PP68 Thm 4.4 needs domination, and PP68 §1(b) needs E_m to be non-conic.

---

## 1. PP67

### 1.1 Prop 1.1, and whether G-closure is derived

**Prop 1.1: correct.**
- *Polyhedral duality.* The cone P = {g : m·g > 0 for m ∈ M, g₃ < 0} is convex. Its dual is cone(M) + cone(−e₃).
- *Intersection with the simplex.* Δ ∩ P\* = ∪_m [m, π(m)] is convex. It contains M and M₀, and lies in conv(M ∪ M₀).
- *Inclusion.* A coherent model weakly 3-worse than T must say + a.e. on P, which puts K inside P\*. Since K ⊆ K_N, the model answers wherever N does, with N's answer.
- *N = T ∧ D\*.* This is the min-over-a-union identity.
- **CHECKED (independent, exact; `geom_ref.py` A5).** The extreme rays of cl P are (16,−7,0), (−7,16,0), (23,−7,−7) and (−7,23,−7). The polygon Δ ∩ P\* has exactly the five vertices v₁, v₂, v₃, d₁, d₂. A2 confirms N = T ∧ D\* on every cell of the arrangement.

**G-closure is optional; the audit is right.** PP65 Prop 2.4 forces the *verdict* T ⪯₃ N_E. It does not force pointwise 3-worseness. PP67's derivation (§1.1) rests on the remark that non-guidance acceptances at u are what kill edge defences. Two facts undercut it:
- (i) The module handles every such kill by an eager refusal anyway (Lemma 3.1(a)–(c), Thm 5.1(iv)).
- (ii) PP68 Prop 2.2, which I confirm (§2.2), shows that T must make non-guidance acceptances against a continuum of N's class-1 or class-2 fills, whatever is chosen.

So "derived, not imposed" should read "a design choice". What remains true is the audit's refinement: once N is kept, T ⪯₃ N *is* a guidance verdict, because its status is fixed by the two models' advice.

### 1.2 Lemma 3.1 (signed closure): correct with repair

I checked each item as a triangle with an explicit closing link.
- **(a)** The closing link is the guidance link X_E ⪯_w T.
- **(b), first part.** The closing link is X_E ⪯_w Z, by guidance.
- **(c)** The splice instance is right: rec(T[L_N∖H ↦ N], N) = rec(T, T[H ↦ N]), and X_E ⊵_w Z strictly holds when P^N_w ⊆ H.
- **(d)** Both strictness statements are right.

**Repair, in (b) second part.** The proof uses E = E₀. For Z = T[L_{D\*}∖H′ ↦ D\*] to lie weakly below X_E one needs P^{D\*}_w ⊆ H′ ∪ E and E₀∖E ⊆ H′. With E = E₀ this is P^{D\*}_w∖E₀ ⊆ H′, and strictness fails exactly when H′ = L_{D\*}∖E₀. So the excluded case is **H′ ≠ L_{D\*}∖E₀**, not "≠ L_{D\*}∖E" with E free.

### 1.3 Prop 3.2 (forced rivals of N and D\*): correct with repair

- **Rows I checked.**
  - The fill row of Y_E. Its (TC) triangle T → Y_E → N → T closes with the committed N ⪯_w T (C3).
  - The D\*[E ↦ S] row (PP65 Lemma 2.1).
  - The swaps row.
  - The copies line. Neither T nor D\* is S on L_N ∪ E. N is not D\* on L_{D\*}∖E. Neither N nor D\* equals T on L_N or L_{D\*}.
- **Repair.** In the Z_H row, "for H ⊇ P^N₁ ∪ P^N₂ (H ≠ L_N): none" describes an empty family (§1.7, §3.2).

### 1.4 Theorem 4.1 (the certificate 𝒲): correct

The brief's three questions:

- **Total?** Yes.
  - Φ₁ and Φ₂ are real-valued on every measurable model, because |f| ≤ C·ω(g)|g| is μ-integrable. So worlds 1 and 2 are total preorders.
  - World 3 is the lexicographic order of (κ, Φ₃), also a total preorder.
  - Hence reflexivity and (TC) hold on every triangle.
  - κ(X) − κ(Y) and Φ(X) − Φ(Y) depend only on the record. So (IB) holds with all copies, including location-dependent ones (κ is anchored on E₀; no invariance is imposed).
  - The field is strictly rank-monotone and κ is monotone in 3-rank. So strict (G) holds.
- **All axioms except final sections?** No. Only the following are certified:
  - for **all** measurable models: reflexivity, (IB), strict (G) and (TC);
  - (LA);
  - for **T, N and D\*** only: protection, direct (C) and support defence.

  The (S) selection is not certified at all: neither competitiveness at the remaining indices nor closed sections. Global (C) is not certified either. I did not test whether 𝒲 has incoherent undominated models, and PP67 makes no claim about it (its §7 says so).

  Within that scope the proof is complete:
  - **Step 3.** It uses only λ ≥ 0, the uniqueness of the pointwise argmin, and κ(T) = κ(N) = 0.
  - **Defence with world 3 as the Bayes world.** If κ(Y) > 0 then N ≺₃ Y; otherwise Φ₃ decides.
  - **D\*.** It is handled on its support, with λ_D = (1, 1, 0).
- **Does N strictly dominate every X_E?** Yes, including E = E₀.
  - In 𝒲: κ(N) = 0 < μ(E) = κ(X_E) at world 3.
  - Worlds 1 and 2: Φ_w(X_E) ≥ Φ_w(X_{E₀}), and the first inequality of Step 5 holds once W > W₀.
  - At the level of Σ_fam the strictness is Lemma 3.1(d). E₀ itself has a non-null proper subset because μ is atomless.

**CHECKED.**
- *Re-run.* `witness67`, `types7` and `geom67`: outputs identical, ALL PASS.
- *Independent.* `cert_ref.py` P1 re-implements the per-type check (signs, and unique argmins for λ_T, λ_N, λ_D on all 15 types).

**Misprints in the text** (the script is right):
- Step 1 prints b = (1, 1, 5/2) for type (B,S,A). The vector used is (1, 1, −5/2), as the stated sign pattern requires. With +5/2, B would not be T's argmin.
- Step 5's "a_w = b_w = 1" should read |a_w| = b_w = 1.

The world-3 key is a lexicographic *proof device*. Brief 56 forbade lexicographic levels in the ranking, and AUDIT_round57_answers explicitly allows them as proof devices. PP67 uses it only in the certificate, so this is in order.

### 1.5 Theorem 5.1: correct within the module

- **(i)–(iii).** These follow from the finiteness of the assigned set (three isolated indices) and the fixed balls.
- **(iv).** Each listed kill clause has a literal refused on a full ball: Lemma 3.1(a)–(c) plus Res.
- **What it does not give.** The theorem gives the invariant 𝓘 for a three-index partial system. Closed sections come only at the end, through PP64 Thm 2.3 with every index assigned. PP67 says this itself.
- **The cost.** Kept for future refusals, the fixed-ball policy forces tie plateaus. This is PP68 Prop 2.1, confirmed in §2.2.

### 1.6 Theorem 6.1: correct

**CHECKED.**
- *Re-run.* `types7`: identical output.
- *Independent.* `cells7_ref.py` and `cert_ref.py` P2, with my own exact cell enumeration:
  - With the 15 planes I find 158 cells, matching Euler (V = 120, E = 276), and 39 mixed types.
  - The three edge midpoints are not generators of any credal set. With the 12 generator planes there are 104 cells and the same 39 types.
  - An independent LP followed by an exact rational check finds vectors with all seven unique argmins on all 39 types.

**Decoupling: re-derived.**
- On R_B^k, T's answer is k′-wrong for both k′ ≠ k. So N_{k′} = D\*_{k′} = T there, because they keep every k′-wrong answer of T.
- Keys: κ_w(N_k) = κ_w(X^k_E) = 0 for w ≠ k. Also κ_w(D\*_{k′}) = 0 for w ≠ k′: on Q_w, D\*_{k′} ∈ {S, B_w}, and B_w is w-correct.
- So every defence and protection argument at a keyed world reduces to Φ_w, exactly as in Thm 4.1.

### 1.7 Prop 7.1: fill half correct; retreat half vacuous

**Fill half.**
- Y_E is incoherent when E is non-conic (Lemma H).
- T ⋠_{1,2} Y_E, by the triangle closed by (C3).
- N ⋠_{1,2} Y_E and D\* ⋠₃ Y_E, by strict (G).

**Retreat half: vacuous.**
- On L, T's answer is 3-correct (N keeps every 3-wrong answer of T) and N = S.
- A 3-correct answer to a mixed problem is wrong at world 1 or at world 2. So every point of L lies in P₁ ∪ P₂, and P₁ ∪ P₂ = L a.e.
- CHECKED (independent, `geom_ref.py` A4): on every cell of L, N is strictly better than T at world 1 or at world 2.
- Hence no H satisfies P₁ ∪ P₂ ⊆ H ⊊ L with L∖H non-null.

**Nearby non-vacuous result (PROVED).** Let w ∈ {1, 2}, let H be non-conic with P_w ⊆ H ⊆ L, and let L∖H be non-null. Then Z_H = T[H ↦ N] is incoherent, and none of T, N, D\* dominates it:
- T ⋠_w Z_H, by Lemma 3.1(c);
- N ⋠₃ Z_H, by strict (G), since Z_H is 3-better on L∖H;
- D\* ⋠₃ Z_H, since Z_H ⊵₃ N ⊵₃ D\*.

The family is not empty: P₁ ≠ L because L ∩ M₂ is non-null, and symmetrically for P₂ (CHECKED, A4b). For H containing neither P₁ nor P₂, T may dominate Z_H as far as the module's literals go.

### 1.8 Props 7.2–7.4: correct, with exact hypotheses

- **7.2.**
  - (i) N ∧ D\* = (T ∧ D\*) ∧ D\* = N.
  - (ii) needs the dominator to serve **every** Y_E, E ⊆ E₀. Only then does the A-part exclusion (PP68 Lemma 1.2(c)) make it ≠ A a.e. on E₀.
  - (iii) Vertical-segment argument: each σk·g increases as |g₃| decreases, because k₃ ≥ 0. A coherent model answering A at a point of R_B therefore answers A on the T-silent part of the segment, an open subset of Q₃. Correct.
- **7.3.** Hypotheses:
  - world 3 is represented by ∫f₃ with f₃(·, a) integrable;
  - μ is atomless;
  - one fixed N with N ⋠₃ T and N ⪯₃ X_E for E of arbitrarily small measure.

  Absolute continuity then gives Φ₃(N) ≤ Φ₃(T), against the refusal. (d) is a correct remark.
- **7.4.** Hypotheses:
  - (H1) ⪯_w is represented by Φ_w = ∫f_w at the world w used, with each f_w(·, a) integrable, so inf_Z Φ_w > −∞. "Bounded field" is more than needed.
  - (H2) α_w = ∫_{E₀}(f_w(S) − f_w(A)) > 0. This follows from strict (G) for the representation on E₀.
  - (H3) all N^j are silent on **one fixed** non-null E₀.
  - (H4) N^{j+1} ⪯_w N^j[E₀ ↦ A] for the **maximal** fill.

  One world suffices. No (TC), coherence or protection is used. The proposition says nothing about chains whose common silence shrinks (PP68's F_t), or whose members serve only sub-fills.

---

## 2. PP68

### 2.1 §1 forced structure: correct with repair

**Theorem 1.1.**
- (ii)–(iv) are triangles closed by guidance links, and correct.
- One imprecision in the w = 3 gloss of (ii): "Y = A on E" should be "Y ⊴₃ A on E", i.e. Y ∈ {A, ×}.
- (v) cites PP64 Lemma 4.1(b), which was refereed earlier.

**Lemma 1.2.**
- (a) Both records have support {C ≠ T}∖E.
- (b) The three acceptances kill X_E ⪯_w C at w = 1, 2, 3, which contradicts T's competitiveness at u. Correct.
- (c) Correct.

**Prop 1.3.**
- (a), (b) are correct. A carrier would refuse its own copy at every world.
- (c) needs the proviso that E₀ ∩ {m·g > 0} is non-null. This is automatic for E₀ = Q₃, since m·g > 0 near v₃·g = 0⁻ when m ≠ v₃. For a small E₀ lying in {m·g < 0}, D_m is not a carrier.

**Prop 1.4(a).** The conclusion (a constant p(E) is consistent) is independently established by PP67 Thm 4.1 for N. The closure argument given for N\* is a sketch. Its SAT check is evidence only.

**§1(b) = Prop 1.4(b) (upward sharing): correct, with one hypothesis made explicit.**
- If C_p ⪯_w X_{E_m} for every n ≥ m and every w, closed sections for the **fixed** rival X_{E_m} pass this to the limit index p on the closed edge.
- PP65 Prop 2.3(b) then forbids C_p ⪯_w X_{E_m} at all three worlds. Its proof uses (IB), T's protection and direct (C) on the model C_p[E_m ↦ S], and this needs **E_m non-conic**, so that the model is incoherent.
- I agree with the audit that the argument needs one fixed rival served infinitely often. It is independent of the error in Prop 4.7(b).

### 2.2 Props 2.1 and 2.2: correct

**Prop 2.1.**
- Suppose C_q ≉ M at q ∈ B_M. Undominatedness of C_q gives M ⋠_w C_q at some w.
- That refusal, reserved on B_M, says C_q ⋠_w M ⊕ rec(M, C_q) = C_q, against reflexivity.
- At ∂B_M, closed sections for the rival M and M's protection give the tie.
- The hypothesis (every later refusal at M is reserved on the fixed ball) is stated.

**Prop 2.2.**
- N ⋠₃ T by strict (G), so N defends against T at world 1 or 2.
- With N ⪯₁ T, the triangle N ⪯₁ T ⪯₁ Z ⪯₁ N (the last link by guidance) refuses T ⪯₁ Z for every strict 1-improvement Z of N.
- For Z_F = N[F ↦ A], F ⊆ Q₂, T's remaining defence worlds are 2 and 3. At world 2 Z_F is better on R_B. At world 3 it is better on F. So both acceptances are non-guidance.
- PP67 commits both N ⪯₁ T and N ⪯₂ T, so this happens for F ⊆ Q₁ and for F ⊆ Q₂.

### 2.3 §3: correct

- **(1)** Correct, and it agrees with PP67 Lemma 3.1(b).
- **(2)** The entailed clause ¬[N ⪯₁ D] ∨ ¬[N ⪯₂ D] holds for every open-edge D. D defends against a class-3 fill Y_F of N at some i ∈ {1, 2}, and N ⪯_i D ⪯_i Y_F ⪯_i N (the last link by guidance) is a triangle whose reverse N ⪯_i Y_F is refused.

  Note the direction: **N is on the old side.** This is the clause misused in Prop 4.7(b).
- I did not re-derive the remark that a tied non-identical model in B_N is fatal at a finite stage. The repair "keep Ĉ = M itself" is sound.

### 2.4 §4: the edge lemma, the cycle cores, and Theorem 4.4

**Lemma 4.1.**
- Z = N[F ↦ A] carries β = rec(N, Y[F′ ↦ A]), because F is disjoint from {N ≠ Y} ∪ F′.
- Z ⊕ β = Y[F ∪ F′ ↦ A], and the triangle Y → Z → Y[F ∪ F′ ↦ A] → Y closes by guidance.
- Correct.

**Lemma 4.2 and Theorem 4.3.** Correct, as triangles closed by guidance.

**CHECKED.**
- *Re-run.* All 13 PP68 scripts, identical outputs.
- *Independent.* `sat_ref.py`, a fresh encoding with a different solver (Glucose4). It uses **only** weak and strict (G), record variables for (IB), triangle (TC), and defence; there are no coherence declarations.
  - Lemma 4.1 is UNSAT at w = 1 and w = 2, and each literal alone is SAT.
  - Lemma 4.2: B →₃ C forces C ⋠₁ B, C ⋠₂ B and C ⪯₃ B. B →₃ C is UNSAT when B is pointwise 3-better than C.
  - Theorem 4.3: the 3-cycle with T strictly 3-better than N\* is UNSAT. A 2-cycle of mixed models is SAT and forces the world-3 tie.

**Soundness of lib68.** Every encoded clause is an axiom instance. Strict (G) is valid because two different advices always have different ranks. Its "incoherent" declarations cover every model other than the selected ones. That is a strong reading of direct (C), but it is harmless for the UNSAT cores quoted. I re-derived those cores without any such declaration.

**Observation (CHECKED).** The quoted 3-cycle core does not need its first edge.
- Y →₃ N\* and T →₃ Y already give N\* ⪯₃ Y ⪯₃ T.
- With the guidance link T ⪯₃ N\* this is an accepted triangle whose reverse N\* ⪯₃ T is refused. PP68's own `cycle68c.out` shows "H2 + H3: UNSAT".
- So the obstruction is a two-step fill path B →₃ C →₃ D with D pointwise strictly 3-better than B. It is not specifically a 3-cycle.

**Theorem 4.4: correct with repair.**
- The proof uses Lemma E(ii) (PP36), which needs **domination**: acceptance at all three worlds, so that T's protection and direct (C) apply.
- With →₃ alone (acceptance at worlds 1 and 2 only), the step "L_{k+1} is silent on part of F_k" fails. In 𝒲, D\* ⪯_{1,2} Y_E for every E, and D\* is G-closed relative to N. So D\* →₃ N with (GC), D\* = A on all of M₃, and the finite set {T, N, D\*} is closed under →₃: D\* has no class-3 fills.
- With "dominates", which is what the theorem's Reading uses, the statement and proof are correct.

### 2.5 Prop 4.5 and "L₀ dominates every N-fill": geometry correct; the cell check is insufficient; repaired

**Geometry (i)–(iii): correct.**
- CHECKED (independent, `geom_ref.py` A3, all 48 cells of the 8-plane arrangement, Euler-complete): L₀ = N on all of M₃, and L₀'s only new answers are B on M₁ ∪ M₂.

**Does the cell check cover all measurable fills? No.**
- `gen2_68` G1 is SAT on a 108-model sub-universe. It has two E₀-atoms, one R_B-atom, and one (S,S,B,B) block and one (A,S,S,S) block per side.
  - It omits the four-model types (S,S,S,S), (S,S,B,S), (A,S,B,S), (A,A,A,A) and (B,B,B,B) on M₁ and M₂.
  - Its fills are unions of two atoms.
- By the sub-universe principle, SAT is evidence only. So "CHECKED on cells" does not establish consistency for measurable fills, and DESIGN_MEMO's "dominates all of N's fills (CHECKED on cells)" overstates it.

**Repair: Theorem R (PROVED; per-type data CHECKED exactly, `cert_ref.py` P3).** There is a total relation 𝒲⁺ on all measurable models such that:
- reflexivity, (IB), strict (G) and (TC) hold for all measurable models;
- T, N, D\* and L₀ are protected (D\* on its support), satisfy direct (C), and are defended against every model;
- PP67's commitments C0–C3 hold, together with D\* ⪯_{1,2} Y_E for E ⊆ E₀;
- **L₀ ⪯_w N[E ↦ A] at every w, strictly at world 3, for every non-null measurable E ⊆ Sil(N) ∩ M₃ = Q₃ ∪ R_B.** This is all class-3 majority fills of N, not only those inside E₀.

*Construction.*
- Use the 17 mixed four-model types of my census.
- Take rational vectors (a_τ, b_τ) such that T, N, D\* and L₀ are the unique argmins of λ_T = (1,1,1), λ_N = (1,1,½), λ_D = (1,1,0) and λ_L = (1,1,¼).
  - They are listed in `cert_ref.out`, checked exactly, with class 2 the mirror image of class 1.
  - On S := {N ≠ L₀}, of type (S,S,B,B), b = (−4, 1, 8) on M₁.
- Weights: ω = W on R_B, ω = W′ on S, and ω = 1 elsewhere. The key is κ⁺(Z) := μ{g ∈ Sil(N) ∩ M₃ : rank₃ Z ≥ 2}. κ⁺(T) = κ⁺(N) = κ⁺(L₀) = 0, since T = B is 3-correct on R_B.

*Proof.*
- Protection and defence are proved exactly as in PP67 Thm 4.1 Steps 3–4. They use unique pointwise argmins and κ⁺ = 0 at the four registered models.
- World 3: κ⁺(L₀) = 0 < μ(E) = κ⁺(N[E ↦ A]).
- Worlds w = 1, 2: by the 1↔2 symmetry of M, M₀ and μ,

  Φ_w(N) − Φ_w(L₀) = W′(4 − 1)∫_{S∩M₁}|g| dμ.

  This is at least ∫_{Q₃}|f_w(A)| dμ + W∫_{R_B}|f_w(A)| dμ once W′ is chosen after W. Hence Φ_w(N[E ↦ A]) ≥ Φ_w(L₀) for every E.
- PP67's four inequalities hold for W large. The S-terms only help them, since there T = N = S and D\* = L₀ = B, and b_o > b₂.
- The finite instance (13 atoms, 3¹³ models) confirms the whole verdict list exhaustively.

*What it does not give.* As for 𝒲: no (S), no sections and no global (C). It also says nothing about L₀'s own fills, or about N's class-1 and class-2 fills. In this certificate L₀ cannot dominate those, because it is 3-worse than N there.

### 2.6 Prop 4.6 (the chain): correct; PROVED here for all t

Write K_t = conv(v_t, M₀).

- **Monotone.** v_t ∈ [v_s, h₁₂] ⊆ K_s for s ≤ t. So K_t ⊆ K_s, and L(t) answers wherever L(s) does, with the same answer.
- **New answers are 3-wrong.**
  - On M₃, d₁·g and d₂·g are positive, so L(t) ∈ {S, A}.
  - On M₁ (signs normalised so that g₁ > 0 > g₂, g₃), L(t) = A = − requires d₁·g < 0 and d₂·g < 0. Then g₁ + g₂ < 0, so v₃·g = (7(g₁ + g₂) + 16g₃)/30 < 0 and v_s·g < 0 for every s. So L(s) = − already.
  - The new answers are therefore A on M₃ and B on M₁ ∪ M₂, all 3-wrong. The same holds on M₂ by symmetry, and unanimous g are unaffected.
- **Silence shrinks.** Sil(L(t)) ∩ M₃ = {τ ≥ t}, which decreases to ∅ as t → 1 (§3.3).
- **Endpoint.** L(1) = D_{M₀} = D\*, because h₁₂ ∈ M₀.

This is **geometry only.** No comparison between chain members is established, as the audit's correction says.

### 2.7 Prop 4.7: (a) correct; (b) wrong

- **(a)** Every dominator of Y lies in the closed set A₁(Y), and p_L ∉ A₁(Y) by strict (G).
- **(b)** The limit edge model C_{p∞} inherits literals of the form [C ⪯_w L_j], with C on the **old** side.
  - §3(2) establishes only ¬[N ⪯₁ D] ∨ ¬[N ⪯₂ D], with the edge model on the **new** side.
  - The clause cited, ¬[C ⪯₁ L_j] ∨ ¬[C ⪯₂ L_j], is not entailed. 𝒲 (Thm 4.1) satisfies every finitary axiom and accepts D\* ⪯₁ N and D\* ⪯₂ N (C3), with C = D\* an edge model and L_j = N. So the cited clause fails in an explicit model of the axioms.
  - The conclusion "the defence world must eventually be constant" is therefore **unsupported**. It is not shown false.

### 2.8 §5 (mixed classes): correct at certificate level

- World 1 is keyed in 𝒲₇. If F ∩ E₀¹ is non-null, κ₁(X) > 0 = κ₁(N₃). Otherwise Φ₁ decides.
- World 2 is keyed with κ₂ = 0 on both sides.
- The bound used is uniform in E and F, so a single enlarged W₃ serves all such X.
- X ⋠₁ N₃ is right: X ⪯₁ N₃ ⪯₁ X_E ⪯₁ X is a triangle closed by guidance whose reverse X ⪯₁ X_E is refused.
- "No new kill pattern" is a remark, not proved.

---

## 3. The audit's geometric claims

### 3.1 Path obstruction: correct

- **The argument.** Let C_s be registered, and let C_t = A a.e. on a bounded non-null E ⊆ Sil(C_s). Put X = C_s[E ↦ A].
  - rec(C_t, X) = rec(Z, C_s), with Z = C_t[E ↦ S]. Both supports are {C_t ≠ C_s}∖E.
  - If C_t dominates X, (IB) gives Z ⪯_w C_s at every w.
  - Protection of C_s installs the reverses, and (C) registers Z.
  - But Z differs from the coherent C_t on a bounded non-null set, so it is incoherent (Lemma H). This is F2.
- **Scope.** This is PP36 Lemma E(ii) for this family, and it applies to *any* candidate equal to the fill on all of E.
- **The numbers.** v_t·(1, 1, −r) = 1 − b_t(1 + r) with b_t = (1 − t)·16/30, and both endpoints of M₀ give 1. For s = 0, t = ½, r = 1 the values are −2/30 and 14/30. At g = (1, 1, −1), F₀ is silent, F_{1/2} says the majority answer, and T and N are silent.
- **The open region for s < t < 1.** It is 1/b_s − 1 < r < 1/b_t − 1, of width (15/8)(t − s)/((1 − s)(1 − t)) > 0, opened up by perturbing g₁ and g₂.
- CHECKED: `thresh_ref.py` B1 (sympy and exact), and `sat_ref.py` P (the (IB) + protection + (C) step, UNSAT, with a SAT control).

### 3.2 Vacuity: correct

See §1.7.

### 3.3 Thresholds τ, the quartile window, recurrence: correct

**Domain.** On M₃ both endpoints of M₀ give positive values. So N, F₀ and every F_t take values in {+, S} there, i.e. {A, S}. Each answers A iff its third generator does: v₃ for N and F₀ (§2.5), v_t for F_t. The common silence of N and F₀ in M₃ is {v₃·g < 0} = Q₃ ∪ R_B.

**τ.** v_t·g = (1 − t)v₃·g + t·h₁₂·g is affine in t, negative at t = 0 and positive at t = 1 (h₁₂·g > 0 on M₃). So

  τ(g) = −v₃·g/(h₁₂·g − v₃·g) ∈ (0, 1),

and F_t is S for t ≤ τ(g), A for t > τ(g), and never B.

**Quartile window.** Each level set {τ = c} = {v_c·g = 0} is a plane, hence null. So on any non-null E the law of τ is atomless, its distribution function is continuous, and the quartiles satisfy q₁ < q₃.
- For t in the **closed** window [q₁, q₃], F_t answers on exactly the fraction ν{τ < t} ∈ [¼, ¾] of E and is silent on the rest.
- Without atomlessness only the half-open window (q₁, q₃] would be safe; here it is not needed.

**Recurrence.** Sil(F_s) ∩ M₃ = {τ ≥ s}. So the class-3 fills of F_s have τ ≥ s, and τ > s a.e.

**What is proved.** That the candidates exist. Not that they dominate, as the audit says.

CHECKED: `thresh_ref.py` B2, exact on 1,874 sampled g, with the level-set planes checked symbolically. B7 is a NUMERICS illustration of the window.

### 3.4 Thresholds σ for R_α and the restore/withdraw lemma: correct (world 3 only)

**σ.** The support function of a Minkowski combination is the combination of support functions:

  min_{K_α} σk·g = (1 − α)·min_M σm·g + α·min_{K_N} σk·g.

- On L, with σ = T's answer, this is affine in α, positive at 0 and ≤ 0 at 1 (< 0 a.e.). So it has one root σ(g) ∈ (0, 1).
- R_α is T for α < σ(g) and S after. It never gives the opposite answer, because max_{K_α} ≥ min_M > 0.
- Off L, R_α = T = N.
- CHECKED: `thresh_ref.py` B3 (Minkowski generators, exact).

**The lemma.** Let α₀ be the essential supremum of σ on H. Suppose every α has μ(H ∩ {σ > α}) = 0 or μ((L∖H) ∩ {σ < α}) = 0.
- Then H ⊆ {σ ≤ α₀} and L∖H ⊆ {σ ≥ α₀}.
- The level set {σ = α₀} is piecewise planar, hence null. So H = {σ < α₀} a.e., and Z_H = R_{α₀}.
- The edge cases (H null, H = L) give T and N.
- So if Z_H is incoherent, some α restores on a non-null part of H and withdraws on a non-null part of L∖H. Threshold cuts are cones, so every non-conic H qualifies.

**Caution (CHECKED, B6).** The gain-and-loss holds at **world 3**. It need not hold at worlds 1 and 2.
- Take H = (L ∩ (M₂ ∪ M₃)) ∪ B₁, with B₁ ⊆ L ∩ M₁ ∩ {σ < α₀} bounded and non-null. Then Z_H is incoherent, because H is non-conic.
- The restored part lies in M₂ ∪ M₃, where T is 2-wrong. The withdrawn part lies in M₁, where T is 2-correct. On B₁, R_{α₀} = S = Z_H.
- So R_{α₀} is pointwise worse than Z_H at world 2 and cannot dominate it.
- B6 exhibits the pointwise pattern at explicit g and α. This confirms the audit's own warning that "every repair is mixed at every world" is unchecked. The α must be chosen per rival, with each world's balance checked.

### 3.5 Splice identity, bridge J_β, and F₀ = N on M₃: correct

- **Splice identity.** Both sides equal T on H and N elsewhere. So it is set algebra, and since N = S on L, Z_H = T[H ↦ S] = T[H ↦ N]. CHECKED for all 2¹⁰ unions of the cells of L (B5).
- **Bridge.**
  - K_{L₀} ⊆ K_N, from the generators (A6).
  - Where N and L₀ agree, both support functions have the same sign, so J_β agrees.
  - Where they differ, N = S and L₀ answers. J_β switches from S to L₀'s answer at one threshold in β, and never takes a third value. So J_β changes only on {N ≠ L₀}, the (S,S,B,B) cells of M₁ ∪ M₂, and J_β = N on M₃.
  - CHECKED: B4.
- **F₀ = N on M₃.** Correct. CHECKED on every cell (A3).

---

## 4. What this means for the round-57 construction (referee's remarks)

1. **Usable as stated.**
   - PP67's module, with Thm 4.1 as its consistency certificate;
   - PP68's forced structure and edge lemma;
   - the audit's geometry: τ, σ, J_β, and the splice identity.
2. **Use Theorem R in place of "CHECKED on cells".** L₀ consistently dominates *every* measurable class-3 fill of N, including fills of R_B, in a full-domain certificate. But L₀ cannot be the repair for N's class-1 and class-2 fills, as the audit anticipated.
3. **Single-world form of the splice exclusion.** The non-vacuous form of Prop 7.1's splice half is: for non-conic H with P_w ⊆ H ⊆ L for **one** w and L∖H non-null, T, N and D\* all fail. So the splice rivals that genuinely need new dominators are those H, and R_α is the natural candidate family. §3.4 shows that α must be chosen per rival and checked world by world.
4. **Fill paths, not just cycles.** By the §2.4 observation, any two-step fill path B →₃ C →₃ D with D pointwise strictly 3-better than B is already inconsistent. Recurrent designs (PP71) must avoid that pattern, not only short cycles.

---

## 5. Scripts (`r9/REFEREE56_py/`; run `python3 -I -B <script>.py` in that folder; each ends ALL PASS)

| Script → output | Content | Kind |
|---|---|---|
| `geomlib.py` | Exact geometry and exact enumeration of the cells of a central arrangement (counted against Euler) | library |
| `geom_ref.py` → `.out` | A1–A6: type census of (T, N, D\*, L₀), N = T ∧ D\*, L₀ = N on M₃, P₁ ∪ P₂ = L, Prop 1.1 polygon, K_{L₀} ⊆ K_N | independent |
| `cells7_ref.py` → `.out`, `types7_ref.json` | Seven-model module: 158 cells (15 planes) or 104 cells (12 planes), 39 types | independent |
| `cert_ref.py` → `.out` | P1: PP67's field. P2: Thm 6.1 LP plus exact check. P3: certificate 𝒲⁺ (Theorem R) with an exhaustive 3¹³ instance | independent |
| `sat_ref.py` → `.out` | Lemma 4.1, Lemma 4.2, Thm 4.3, and the path obstruction step: a fresh encoding without coherence declarations | independent |
| `thresh_ref.py` → `.out` | B1–B7: path numbers, τ, σ, J_β, splice identity, the world-2 counterexample, quartile NUMERICS | independent |
| `rerun/PP67_py`, `rerun/PP68_py` | All 16 author scripts re-run on copies (`*.rerun.out`); every output is identical to the author's | re-run |
