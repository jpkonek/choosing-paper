# PP43. The two-gate test of the fixed-kernel design

23 October 2026. Secondary task of Brief 50 (audit round 50). One reader (me); not refereed.

**Labels.** PROVED: complete argument here, or a cited result that has been proved or refereed. CHECKED: exact rational computation in `PP43_py/exact43.py` (ALL PASS). NUMERICS: Monte Carlo in `PP43_py/killer43_mc.py`; no proof depends on it. CONJECTURE: as stated.

**Inputs.** BRIEF50 and AUDIT_round50 (binding); PP41 (design Γ_K, (J), (J_T), (J_B), Lemma 1.2); PP40 (Lemma 2.2: the margin h_0 > 0; Lemma 1.3 and (B3): shadows; Lemma 2.1: inheritance); PP38 (kernel, Thm 3.1, Cor 4.3, Thm 6.2: the forced jump); PP37 (gates, Lemma 3.3); AUDIT_completion (rules I–IV, F1/F2, extension theorem). Also REFEREE_round49, as relayed by the coordinator during this task: §4.3 (Lemma R2, Prop 3.4R and its hypothesis (R)) and §4.4 (counterexample to PP41 Prop 4.1(b)). I add no axioms. Every extra hypothesis is named where it enters.

---

## 0. Verdict

**The test fails, and the failure is in section inheritance, not in the gate interaction.** The interaction can be made clean. The jump cannot.

1. **The interaction works (§2, PROVED; design inequalities CHECKED).** I give an explicit aggregation rule (AR) and a criterion, *gate dominance*. Under it, a union of gates satisfies all of the following, with every common-context copy included:
   - strict (G), (IB) and (TC), including triangles whose edges pass through different gates;
   - undominatedness of every registered model;
   - direct (C) for the registered models: no all-world tie with any other model. So rules II–IV of AUDIT_completion are inert, and neither F1 nor F2 occurs.

   The criterion is met by a concrete pair: T and a post-jump-type segment B = B_12(t), t ≠ 1, at an interior index. Their valuations are genuinely different. The pair also satisfies PP41's jump requirement (J_T): T's valuation rates B at least as well as T at world 3. B's gate accepts the field-negative jump record B ⪯_3 T[E ↦ A], and PP40's shadows are refused automatically.
2. **Direct (C) for a union needs such a criterion.** PP41 Prop 4.1(b) is false (REFEREE_round49 §4.4). That counterexample uses strictly positive gate values, not zero rules, so restricting zero rules alone does not repair it. Gate dominance does (Prop 2.2).
3. **Section inheritance at the jump is impossible for every choice of valuations (Thm 3.4, PROVED).** Put T at p_0 and segments B_n ∈ B_ij(t_n) at interior indices p_n → p_0. Closed sections then force B_n's own valuation to be at most o(1) better than T's at the edge worlds (Lemma 3.1). Together with the kernel's margin h_0 > 0, this lets one build, for large n, an explicit measurable rival X_n* such that **B_n is refused against X_n* at every world**. So B_n is not competitive. The literal two-model version (one B at indices accumulating at p_0) is the constant-sequence case.
   - The proof needs none of PP41's hypotheses (H_P), (H_inst), (NA) or t* ≠ 1, no convergence of valuations, and no zero rule.
   - It also needs no hypothesis (R): a thin shell on which the rival says "contradiction" stops every other coherent model from realising either side of the killing record (Lemma 3.3). This also removes (R) from REFEREE_round49's Prop 3.4R (Cor 3.5).
4. **Classification of the failure.**
   - It is forced by the **axioms**: closed sections at p_0, strict (G), and competitiveness on full support.
   - It is forced by the **kernel**: post-jump models are Φ-Bayes at an edge weight with a uniform margin h_0 over T (PP38 Cor 4.3, Thm 6.2; PP40 Lemma 2.2).
   - It is forced by **one design commitment**: a member's verdict is the sign of one additive valuation, which adds the kernel's value of a record's bounded part to the gate's value of its tail.
   - It is **not** forced by the chosen valuations, the zero rules, or cross-gate (TC). PP41's Options A and B both fall under Thm 3.4. Option B adds only refusals, and the killer rival is a missing acceptance.
5. **The reachable aim (§4).** Thm 3.4 applies only to gates whose verdict is the sign of one additive valuation. A *tail-first lexicographic* gate escapes the killing rival. I show it passes Lemma 3.1's tests and gives competitiveness (Prop 4.1). Whether it gives full inheritance and cross-gate (TC) is CONJECTURE 4.2. The more robust repair is the audit's main task: revise the bounded kernel so that post-jump models need not keep a Bayes margin over T.

| Item | Result | Label |
|---|---|---|
| Aggregation rule; refusal is global | (AR), §1 | definition |
| Cross-gate (TC), strict (G), (IB) with all copies; undominatedness; direct (C) for registered members; closure inert | Thm 2.1 (gate dominance) | PROVED |
| Without dominance, direct (C) fails for a union, even with strict zero rules | Prop 2.2 (REFEREE_round49 §4.4) | PROVED there |
| Explicit pair T, B_12(t), t ≠ 1, meeting Thm 2.1 with (J_T), the jump record and shadows | Thm 2.3 | PROVED; inequalities CHECKED |
| Design at t = 1 | impossible in this form (Remark 2.4) | PROVED |
| Inheritance forces v_w^{(n)} := V^{B_n}_w(B_n → T) ≤ o(1) at all worlds | Lemma 3.1 | PROVED |
| Local attainability at B_12(t)'s Φ-ties | Lemma 3.2 | PROVED; CHECKED |
| Contradiction shell blocks all other realisers | Lemma 3.3 | PROVED |
| **No additive-gate jump, any valuations** | **Thm 3.4** | **PROVED** |
| Prop 3.4R without (R) | Cor 3.5 | PROVED |
| Arithmetic of the killer at t = 1/2, 2 | §3.4 | NUMERICS |
| Tail-first lexicographic gate passes Lemma 3.1's tests and competitiveness | Prop 4.1 | PROVED |
| It gives full inheritance and cross-gate (TC) | Conj 4.2 | CONJECTURE |

---

## 1. Setting and the aggregation rule

Brief 50's setting and PP38's notation are used throughout:
- the kernel field Φ = ℓ^T, with Φ_w(r) = L_w(new) − L_w(old), finite for every record;
- T, the segments B_ij(t), the vertex models V_k, and Sil(T);
- for B = B_12(t), the disagreement cone D := {T ≠ B} and the Bayes weight μ = μ(t) := (t, 1, 0)/(1 + t).

Every coherent model D_K (K ≠ ∅) is **conic** and never says "contradiction" on a non-null set.

**Valuations.** Each registered member C carries V^C = Φ + Π^C, where Π^C is a **tail functional** with an angular penalty field ψ^C_w(ĝ, a) ≥ 0:

  Π^C_w(r) := LIM_{R→∞} ∫_{S²} [ψ^C_w(ĝ, new(Rĝ)) − ψ^C_w(ĝ, old(Rĝ))] · 1[Rĝ ∈ supp r] dσ(ĝ),

with LIM a Banach limit. This gives:
- Π^C vanishes on bounded records;
- Π^C is additive under composition and disjoint union (it is linear in the pointwise difference);
- on conic records Π^C is the angular integral of the field, so on the conic sub-records of a fixed conic record it is a non-atomic finite vector measure;
- every inequality that holds pointwise for the field passes to Π^C.

This is PP41's (V1)–(V2). Π^C is **weakly guiding** if ψ^C_w(ĝ, ·) is nondecreasing in the w-rank. Then V^C is strictly guiding, because Φ is.

**(AR) Aggregation rule.** A record r is accepted at w iff at least one of the following holds:
1. **guidance:** r is a weak w-worsening;
2. **kernel:** r is bounded and Φ_w(r) ≥ 0;
3. **gate:** some registered C realises the old side of r (C = old side a.e. on supp r) and V^C_w(r) > 0;
4. **installed:** r is a copy of an installed domination record (§3 only; none in §2).

Otherwise r is refused at w. **A refusal is global.** A record refused by one gate but passed by another is accepted. Every clause depends only on the record and the registered family, so all common-context copies of a record receive the same verdict. That is (IB), with every copy included.

**Zero rule.** Gates are **strict**: zero-value records pass only through the kernel (bounded records) or as trivial guidance. This follows the coordinator's item (3). Symmetric zero clauses that pass through a realiser of the *new* side are what produce REFEREE_round49's F2 in PP37 §1.6. Thm 3.4 does not depend on this choice (§3).

---

## 2. The interaction: two gates that do not interfere

### 2.1 Gate dominance

**Theorem 2.1 (gate dominance; PROVED).** Let 𝒫 be a registered family of coherent models with gates V^C = Φ + Π^C under (AR). Suppose there is one functional U = Φ + Π^U, with Π^U a weakly guiding tail functional, such that:
- **(D1)** U_w(r) ≥ V^C_w(r) for every C ∈ 𝒫, every w, and every record r whose old side C realises;
- **(D2)** each C ∈ 𝒫 is the a.e.-unique λ_C-Bayes model of U, for some λ_C ∈ Δ.

Then the following hold.
- **(a)** Reflexivity, strict (G), (IB) and (TC) hold for the aggregate. In particular (TC) holds for triangles whose edges pass through different gates, through the kernel, through guidance, or through copies of these records in third contexts.
- **(b)** Every C ∈ 𝒫 is undominated and has no all-world tie with any model X ≠ C. So direct (C) holds for the registered members. Starting from 𝒫, rules II–IV of AUDIT_completion add nothing, F1 and F2 do not occur, and the extension theorem of AUDIT_completion §3 applies.
- **(c)** If moreover each C is the a.e.-unique λ_C-Bayes model of its own V^C with λ_C ∈ Δ_{s(C)}, then each C is competitive against every measurable rival on its support, through its own gate.

*Proof.*
1. **Every accepted record has U_w ≥ 0.**
   - A guidance record has U_w ≥ 0, since U is strictly guiding.
   - A kernel record is bounded, so U_w = Φ_w ≥ 0.
   - A gate record through C has U_w ≥ V^C_w > 0, by (D1).
   - Moreover U_w > 0 on every accepted record except trivial records and bounded records with Φ_w = 0. (A nontrivial weak worsening has Φ_w > 0.)
2. **Strict (G).** A nontrivial pure w-improvement has U_w < 0, because Φ_w < 0 and Π^U_w ≤ 0. So no clause accepts it.
3. **(TC).** Around an accepted triangle the three U_w-values sum to 0, since U is a difference of potentials. All three are ≥ 0, so all are 0. By step 1 each edge is trivial, or bounded with Φ_w = 0. The reverse of such an edge is bounded with Φ_w = 0, so the kernel accepts it. Hence every accepted triangle has its reverses.
4. **(IB).** Each clause of (AR) is a function of the record (§1).
5. **Undominated and no ties, (b).** Suppose X ⪯_w C at every w. By step 1, U_w(X → C) ≥ 0, so U_w(C → X) ≤ 0 at every w, and λ_C · U(C → X) ≤ 0. Uniqueness in (D2) gives λ_C · U(C → X) > 0 unless X = C. So X = C. An all-world tie is a special case.
   - Rule III's premise therefore holds only with X = C. Rule IV registers nothing new. Rule II adds nothing, by (TC).
6. **(c).** For X ≠ C, λ_C · V^C(C → X) > 0. So some w ∈ supp λ_C ⊆ s(C) has V^C_w(C → X) > 0, and C realises the old side. ∎

(D1) is a cross-gate compatibility condition. It implies the necessary condition REFEREE_round49 states after its §4.4: for members C ≠ C′ and a conic S ⊆ {C ≠ C′}, the vectors V^C(C → C[S ↦ C′]) and V^{C′}(C → C[S ↦ C′]) must not lie in the open positive and open negative orthants respectively.

Indeed, U(C → C[S ↦ C′]) ≥ V^C(C → C[S ↦ C′]). Applying (D1) to C′ gives U(C[S ↦ C′] → C) ≥ V^{C′}(C[S ↦ C′] → C). If the first vector were > 0 and the second < 0 at every world, the first inequality would give U > 0 at every world and the second U < 0 at every world. These contradict each other.

**Proposition 2.2 (without dominance, a union can fail direct (C); PROVED in REFEREE_round49 §4.4).** Take T and B_12(1/2) with valuations satisfying all of PP41's (I_Γ). There is an incoherent X = T[S ↦ B] with:
- V^T_w(T → X) > 0 at every w;
- V^B_w(X → T) > 0 at every w.

So T ≈ X at all worlds, and rule IV registers X: F2. The gate values are **strictly positive**, so strict zero rules do not prevent this. It is (D1) that excludes it.

### 2.2 The explicit pair

Fix t ∈ (0, 1). The case t > 1 is the mirror image under exchanging worlds 1 and 2 and replacing M_1 by M_2; it is CHECKED in (a).

Let R ⊆ R_t := M_1 ∩ Sil(T) ∩ {G⁻¹(t) < θ < β} be a cone of positive angular measure σ(R). R_t is non-null by PP41 Lemma 1.2(c), and witnesses are CHECKED in (a). On R:
- T = S, with ranks (1, 1, 1);
- B = A, with ranks (2, 0, 0);
- the change T → B has rank pattern (+1, −1, −1).

**The valuations.** Choose constants K > 0 and 0 ≤ c_w, and put

  φ_3 := K,   φ_2 := (tK + t c_1 + c_2)/(1 − t) + 1,   φ_1 := φ_2 + φ_3,

with c_w ≤ φ_w for each w. On directions in R define

  ψ^T_w(ĝ, a) := φ_w · r_w(ĝ, a),   k_w(ĝ, a) := c_w · 1[a ≠ T(ĝ)],

and set both to 0 off R. Put Π^T := Π_{ψ^T}, κ := Π_k and Π^B := Π^T + κ. The valuations are

  V^T := Φ + Π^T,   V^B := Φ + Π^B.

They are different whenever c ≠ 0. T and B are registered at different interior indices, so both gates act at all three worlds.

**Theorem 2.3 (the pair passes the interaction test; PROVED; pointwise inequalities CHECKED in (a)).** With U := V^B, the pair 𝒫 = {T, B} satisfies (D1), (D2) and the hypothesis of Thm 2.1(c). Hence all of Thm 2.1 (a)–(c) holds. In addition:
- **(i) (J_T).** If K σ(R) ≥ Φ_3(T → B), then V^T_3(T → B) ≤ 0: T's own valuation rates B at least as well as T at world 3. T's gate therefore refuses T ⪯_3 B.
- **(ii) The jump record.** If (K − c_3) σ(R) ≥ Φ_3(T → B), then for every bounded non-null E ⊆ Sil(T) ∩ M_3, B ⪯_3 T[E ↦ A] is accepted through B's gate. Its field value is Φ_3 < 0 once β_3(E) < Φ_3(T → B).
- **(iii) Shadows.** Every shadow forbidden by PP40 Lemma 1.3 for this acceptance is refused. More generally, no accepted triangle at world 3 contains this record without its reverses.

*Proof.*
1. **Weak guidance.** Π^T is weakly guiding (φ ≥ 0, rank-linear). Π^B is weakly guiding on R because c_w ≤ φ_w. For example, at world 1 the values in increasing order of rank are:

     B-answer c_1 ≤ S φ_1 ≤ A 2φ_1 + c_1 ≤ contradiction 3φ_1 + c_1.

   Worlds 2 and 3 are alike. Off R both fields are 0. (CHECKED (a), at every witness, all four advices.)
2. **(D1) for B** holds with equality, since U = V^B.
3. **(D1) for T.** U − V^T = κ, and κ ≥ 0 on every record whose old side is T, because k(ĝ, T(ĝ)) = 0 ≤ k(ĝ, a).
4. **(D2) and (c) for T at λ = u.**
   - u · Φ(T → X) > 0 for X ≠ T (T is the unique u-Bayes model of Φ).
   - u · Π^T(T → X) ≥ 0, because T is pointwise u-optimal for ψ^T. On R the three regular answers all cost 2φ_2 + 2φ_3, and contradiction costs more (CHECKED).
   - u · κ(T → X) ≥ 0 by step 3.
   - So T is the unique u-Bayes model of both V^T and U.
5. **(D2) and (c) for B at λ = μ.**
   - μ · Φ(B → X) > 0 for X ≠ B (PP38 Lemma 4.1).
   - μ · Π^B(B → X) ≥ 0, because B is pointwise μ-optimal for ψ^B. On R, (1 + t) times the μ-cost is:
     - A: t(2φ_1 + c_1) + c_2;
     - S: tφ_1 + φ_2;
     - B-answer: tc_1 + 2φ_2 + c_2.

     "A ≤ S" is (1 − t)φ_2 ≥ tφ_3 + tc_1 + c_2, which is how φ_2 was chosen. "A ≤ B-answer" is tφ_1 ≤ φ_2, which is implied. (CHECKED.)
   - So B is the unique μ-Bayes model of U = V^B, and μ ∈ Δ ⊆ Δ_{s(B)}.
6. **(i).** Π^T_3(T → B) = −K σ(R), because A is 3-correct on M_1. So V^T_3(T → B) = Φ_3(T → B) − K σ(R) ≤ 0.
7. **(ii).** κ_3(T → B) = c_3 σ(R). So

     V^B_3(B → T[E ↦ A]) = V^B_3(B → T) + β_3(E) = −Φ_3(T → B) + (K − c_3) σ(R) + β_3(E) > 0.

   B realises the old side of this record.
8. **(iii).** This is (TC) from Thm 2.1(a). PP40's Lemma 1.3 shadows are an instance of (TC). Concretely, Q := T[E ↦ A, F ↦ contradiction] has rec(Q, B) realised by no member, and it contains a contradiction → regular improvement at every world, so it is not guidance. It is refused. ∎

NUMERICS (`killer43_mc.out`): Φ(T → B_12(1/2)) ≈ (0.056, −0.186, 0.507), matching REFEREE_round49's (0.053, −0.183, 0.507). The constant K exists exactly; its numerical size only rescales σ(R).

**Remark 2.4 (t = 1; PROVED).** At t = 1 the inequality (1 − t)φ_2 ≥ tφ_3 + … forces φ_3 = 0, and then (i) fails. So this design cannot place B_12(1) after the jump. This matches PP41 §2.5 and PP40 Prop 2.4(i).

**What Thm 2.3 does and does not give.** It is the interaction the audit asked for: two different valuations, every copy, cross-gate (TC), undominatedness and direct (C), with T's world-3 concession (J_T) and an accepted field-negative record. It is **not** a jump. B sits at an index of its own. §3 shows that no choice of valuations can put B, or a sequence of segments, at indices accumulating at T's index.

---

## 3. Section inheritance at the jump: impossible for additive gates

**Setting of this section.** The design is Γ_K under (AR). Clause 3 may use any zero rule: a symmetric zero clause through the old or the new side changes nothing below. Installed records are as in Γ_K: copies of dominations rec(C, Z) of **repair-class** rivals Z. All registered members are coherent. The selection satisfies:
- T = C_{p_0} for an interior p_0;
- p_n → p_0 are interior indices;
- B_n := C_{p_n} ∈ B_ij(t_n) for one edge {i, j}, with t_n ∈ (0, ∞) arbitrary. No convergence is assumed, and B_n may be constant.

Under the kernel this is the forced situation at the jump (PP38 Thm 6.2: path models beyond the last point of T's tie fibre are eventually in one edge family). Let k be the third world and μ_n := μ(t_n), so μ_{n,k} = 0. Put

  v^{(n)} := V^{B_n}(B_n → T) ∈ R³,   p^{(n)} := Φ(B_n → T) = L(T) − L(B_n),   h(t_n) := μ_n · p^{(n)}.

**(H_rc).** No repair-class rival says contradiction on a non-null set. Every family in BRIEF49's repair class is built from silence, correct answers and registered models' answers, so (H_rc) is a description of that class, not a restriction of it.

### 3.1 Inheritance bounds the post-jump valuations

**Lemma 3.1 (PROVED; closed sections at p_0 and strict (G)).** For every w ∈ {1, 2, 3}, limsup_n v_w^{(n)} ≤ 0.

*Proof.* Take a bounded non-null F ⊆ Sil(T) ∩ M_w, and put X := T[F ↦ w-correct].
1. T ⋠_w X by strict (G).
2. Closed sections at p_0 then give N such that B_n ⋠_w X for n ≥ N.
3. B_n realises the old side of rec(B_n, X). So B_n's gate must not pass it: V^{B_n}_w(B_n → X) ≤ 0, and this holds under any zero rule.
4. By additivity, and since Π^{B_n} vanishes on the bounded record T → X,

     V^{B_n}_w(B_n → X) = v_w^{(n)} + Φ_w(T → X) = v_w^{(n)} − α_w(F).

5. So v_w^{(n)} ≤ α_w(F) for n ≥ N, and α_w(F) can be made arbitrarily small. ∎

Only the worlds i and j are used below.

**The margin (PROVED, PP40 Lemma 2.2).** h(t) > 0 for every t, and h is continuous on [0, ∞] with positive limits at 0 and ∞. Hence h_0 := inf_t h(t) > 0. (NUMERICS there: h_0 ≈ 0.086 at ε = 0.3, attained at t = 1; here h(1/2) ≈ h(2) ≈ 0.105.)

### 3.2 Two lemmas

**Lemma 3.2 (local attainability at B's Φ-ties; PROVED; CHECKED (b)).** Let B = B_12(t), t ∈ (0, ∞), and let d ∈ R³ with μ · d > 0. Then there are ε_0 > 0 and, for every ε ∈ (0, ε_0], a bounded perturbation W of B, supported in a fixed ball and in four small balls of M_1, with Φ(B → W) = εd.

*Proof.*
1. **Two kinds of point on M_1.** Write g = (1, −s_2, −s_3) on M_1. B says B-answer (1-correct) iff F(s_2) < t, and S iff F(s_2) ≥ t ≥ G(s_2) (PP41 Lemma 1.2(c)).
   - At s_2 with F(s_2) = t + η, B = S, and the change S → B-answer has field vector |g_1|(−1, t + η, F(s_3)).
   - At s_2 with F(s_2) = t − η, B = B-answer, and the change B-answer → S has field vector |g_1|(1, −t + η, −F(s_3)).
   - Both have μ-value η|g_1|/(1 + t) > 0.
2. **Tie vectors.** With τ(a) := (−1, t, a) ∈ μ^⊥ and a_1 ≠ a_2 values of F(s_3), the four vectors ±τ(a_1), ±τ(a_2) positively span the plane μ^⊥. The four field vectors are ±τ(a_m) + ηe_2.
3. **Decomposition.** Write d = xτ(a_1) + yτ(a_2) + (μ·d)(1 + t)e_2. Give the generator of sign sgn(x) at a_1 the weight |x| + m, the other generator at a_1 the weight m, and likewise at a_2 with y. Then the sum equals d exactly when 4m + |x| + |y| = (μ·d)(1 + t)/η. For small η this gives m > 0, so all four weights are positive. (CHECKED exactly, (b): 40 random targets at each of 12 values of (ε, t).)
4. **From points to balls.** With all weights positive and the generators spanning R³, d lies in the interior of their cone. Replace each point by a small ball on which B's answer is constant. The averaged vectors stay close to the generators, so d is still a positive combination of the four ball values.
5. **Scaling.** The value map on subsets of each ball is a non-atomic vector measure, so its range contains the segment from 0 to the full ball value. Summing over the four balls gives εd for all small ε. ∎

This is REFEREE_round49's Lemma R2 for B_12(t), with explicit generators.

**Lemma 3.3 (contradiction shell; PROVED).** Let C be coherent and let r be a record out of C. Suppose supp r contains a shell piece P := {ρ < |g| < ρ + η}, and the new side of r is "contradiction" on P. Then:
- no coherent model other than C realises the old side of r;
- no coherent model realises the new side of r;
- the contribution of P to every Φ_w is at most ∫_P (α + β + γ)_w dμ, which → 0 as η → 0;
- the contribution of P to every Π is 0, since P is bounded.

*Proof.* Coherent models are conic. A coherent C′ ≠ C differs from C on a non-null cone, which meets the shell in a non-null set, so C′ ≠ old side somewhere on supp r. No coherent model says contradiction on a non-null set. ∎

### 3.3 The theorem

**Theorem 3.4 (no additive-gate jump; PROVED).** In the setting of this section, under (H_rc), the following cannot all hold:
- fixed-rival sections closed at p_0 for the rivals T[F ↦ w-correct], w ∈ {i, j};
- every B_n competitive on supp p_n = {1, 2, 3} against every measurable rival.

More precisely, every n with max_{w ∈ {i,j}} v_w^{(n)} < h(t_n) has an explicit rival X_n* against which B_n is refused at every world. By Lemma 3.1 and h ≥ h_0, every large n is such an n.

*Proof.* Fix such an n, and write B, D, μ, v, p, h for B_n, {T ≠ B_n}, μ_n, v^{(n)}, p^{(n)}, h(t_n).

1. **The tail vector.** Let π(S) := Π^B(B → T on S) for conic S ⊆ D, a non-atomic vector measure. By additivity,

     π(D) = Π^B(B → T) = v − Φ(B → T) = v − p.

   So μ · π(D) = μ · v − h ≤ max_{w ∈ {i,j}} v_w − h < 0, using μ_k = 0 and μ ∈ Δ.
2. **The target.** Put q := −π(D), so c := μ · q > 0. Put d := q − (c/2)·1, so μ · d = c/2 > 0.
3. **The pieces.**
   - By Lemma 3.2 choose ε ∈ (0, 1] and a bounded W supported in a ball B_{R_0} with Φ(B → W) = εd.
   - By Lyapunov choose a cone S ⊆ D with π(S) = ε π(D) = −εq.
   - Choose a shell P outside B_{R_0} with total Φ-envelope below εc/8.
   - Choose R > ρ + η, with ∫_{|g|>R} (α + β + γ)_w dμ < εc/8.
4. **The rival.** Define X_n* to be:
   - W on B_{R_0};
   - contradiction on P;
   - T on S ∖ B_R;
   - B elsewhere.
5. **Its value.** By additivity, with Π vanishing on the bounded parts,

     V^B(B → X_n*) = εd + [P-part] + Φ(B → T on S ∖ B_R) + π(S) = ε(d − q) + O(εc/4) = −(εc/2)·1 + O(εc/4) < 0

   at every world. (The P-part and the far Φ-part are each below εc/8 at every world.)
6. **No route accepts it at any world.**
   - B's own gate: the value is < 0 at every world, under any zero rule.
   - Other gates: by Lemma 3.3 no other coherent member realises the old side, and none realises the new side.
   - Guidance: the record is not a weak worsening at any world. Its part on the four balls contains changes that improve each world (step 1 of Lemma 3.2: world 1 at the B → S points, worlds 2 and 3 at the S → B points).
   - Kernel: the record is unbounded, since S is a non-null cone (π(S) ≠ 0).
   - Installed copies: a copy has the same new side, which says contradiction on P, against (H_rc).
7. So B ⋠_w X_n* at w = 1, 2, 3, while supp p_n = {1, 2, 3}. B is not competitive. ∎

**Corollary 3.5 (Prop 3.4R without (R); PROVED).** In Γ_K under (H_rc), let C be registered and Φ-Bayes at exactly one weight λ. If C is not pointwise λ-Bayes for Π^C, then C is not competitive.

*Proof.* REFEREE_round49's rival C·b·c has V^C(C → C·b·c) = −s(1, 1, 1) + o(1). Add a contradiction shell of Φ-envelope below s/4. Lemma 3.3 then supplies (R), and the other routes are excluded as in step 6. ∎

So **own-gate competitiveness forces common weights unconditionally** in Γ_K. With Cor 3.5 there is a two-line second proof of Thm 3.4: B_n must be Π^{B_n}-Bayes at μ_n, so μ_n · v^{(n)} ≥ μ_n · p^{(n)} = h(t_n) ≥ h_0, and Lemma 3.1 contradicts this. The direct construction above shows the actual failing rival.

### 3.4 The failing configuration, and its source

**Exact failing configuration.**
- Indices p_n → p_0, with T at p_0 and a segment B_n at p_n.
- For large n, B_n has no defence against X_n*. That rival is:
  - B_n with a small bounded perturbation at B_n's own 1-correct/silent threshold on M_1, in the direction d = q − (c/2)·1;
  - plus T's answers on a far sub-cone S of {T ≠ B_n}, carrying the fraction ε of B_n's tail value of the full swap;
  - plus a thin contradiction shell.
- B_n's own valuation scores it below B_n at all three worlds. No other gate, guidance, the kernel, or an installed copy can accept it.

NUMERICS (`killer43_mc.out`, ε = 0.3, the case most favourable to B's gate, v = 0):

| | t = 1/2 | t = 2 |
|---|---|---|
| p | (−0.056, 0.186, −0.507) | (0.184, −0.054, −0.508) |
| μ · π(D) | −0.105 | −0.105 |
| killer value / ε | −0.053 at every world | −0.053 at every world |

**Source (the classification asked for).**
- **Axioms:** closed sections at p_0 (Lemma 3.1), strict (G), competitiveness on full support.
- **Kernel:** post-jump models are Φ-Bayes only at an edge weight, with margin h_0 > 0 over T. This uses PP38 Cor 4.3 and Thm 6.2 and PP40 Lemma 2.2. The margin is exactly the jump the kernel forces: a Bayes family with a continuous path out of T would have h → 0, and step 1 would fail.
- **Design commitment:** a member's verdict is the sign of **one additive valuation that adds the bounded (kernel) value to the tail value**. The killer mixes a bounded part near B_n's Φ-ties with a tail part.
- **Not the valuations:** Π^{B_n} is arbitrary.
- **Not the zero rules:** the value is strictly negative.
- **Not (TC):** no triangle is used.
- **Not (R):** Lemma 3.3 supplies it.

**Consequence.** Under the kernel the jump is forced (PP38 Thm 6.2). So **the milestone is impossible in Γ_K for every choice of per-member valuations.** This covers PP41's Option A, whatever the valuations. It also covers Option B: (J_ref) and the shadows only remove acceptances, and X_n* already has none.

---

## 4. What is reachable

The proof of Thm 3.4 uses one feature of the gate: bounded and tail values are **added** before the sign is taken. A gate that consults the tail first does not have it.

**Tail-first lexicographic gate.** B's gate passes r at w iff B realises the old side and (Π^B_w(r), Φ_w(r)) >_lex (0, 0). Bounded records have Π^B = 0, so they are decided by Φ, as the kernel requires. A single such gate is (TC)-safe: the lexicographic order on R² is a total preorder compatible with addition, so PP37 Lemma 3.3's argument applies verbatim.

**Proposition 4.1 (PROVED).** Let B_n carry a tail-first lexicographic gate, and put π := Π^{B_n}(B_n → T) and p := Φ(B_n → T).

- **(a) Lemma 3.1's tests** reduce to the following requirement at each edge world w: π_w < 0, or π_w = 0 with limsup_n p_w ≤ 0. Since μ_n · p ≥ h_0, π_w < 0 is needed at an edge world where p_w > 0. At t = 1/2 that is world 2 only, since p_1 < 0 (NUMERICS).
- **(b) The jump record** B_n ⪯_k T[E ↦ A] needs π_k > 0, since p_k ≈ −0.5 (NUMERICS).
- **(c) Competitiveness.** If B_n is weakly Π^{B_n}-Bayes at some λ′ ∈ int Δ, then B_n is competitive against every measurable rival.
- **(d) The killer.** X_n* of Thm 3.4 is accepted at k, because its tail part επ has π_k > 0.

*Proof of (c).* For a rival X, let τ := Π^{B_n}(B_n → X).
- If some τ_w > 0, the gate passes at w.
- Otherwise τ ≤ 0 with λ′ · τ ≥ 0, and λ′ > 0, so τ = 0. Then μ_n · Φ(B_n → X) > 0 gives an edge world with Φ_w > 0 and τ_w = 0, and the gate passes there.

(a), (b) and (d) are direct from the definitions and the values. ∎

Requirements (a) and (b) are compatible with (c) in at least one way. Put weight ψ_3 ≫ 0 on R_t, where B → T is (−1, +1, +1). Put weight at world 2 on M_1 ∩ Sil(T) ∩ {θ < F⁻¹(t)}, where B → T is (+1, −1, −1). Add enough world-1 weight on R_t to keep π_1 < 0. Each piece can be made λ′-Bayes for B at an interior λ′. I have not CHECKED this beyond the sign bookkeeping.

**CONJECTURE 4.2.** For t* outside PP40's double-loss set I_2, there are a tail-first lexicographic gate for each post-jump B_n and valuations for T, satisfying a lexicographic form of Thm 2.1's (D1)–(D2), such that inheritance (J) holds at p_0 for every fixed measurable rival.

What is open is (J) for rivals whose tail part vanishes at some world but whose bounded part does not. On those, the gate falls back to Φ, and the argument behind PP40 Prop 2.3 can return. If this conjecture fails, the remaining repair is the audit's main task: revise the bounded kernel, so that post-jump models are not Φ-Bayes with a margin over T. Thm 3.4 says the margin, not the gate interaction, is what kills the fixed-kernel design.

**Answer to the audit, in one line.** With a dominance condition the two-gate interaction is clean (Thm 2.3). Section inheritance at the jump is impossible for every additive-gate design over PP38's kernel (Thm 3.4). So the secondary test is closed negatively, and the main task should not rely on Γ_K.

---

## 5. Status

| Result | Label |
|---|---|
| (AR); global refusal; strict gate zero rule | definition |
| Thm 2.1 (gate dominance: (TC) across gates and copies, strict (G), (IB), undominatedness, direct (C) for registered members, closure inert, competitiveness) | PROVED |
| Prop 2.2 (direct (C) fails for unions without dominance, with strict values) | PROVED (REFEREE_round49 §4.4) |
| Thm 2.3 (explicit pair T, B_12(t), t ≠ 1, with (J_T), jump record, shadows) | PROVED; pointwise design CHECKED (a) |
| Remark 2.4 (t = 1 excluded in this design) | PROVED |
| Lemma 3.1 (inheritance bounds v^{(n)}) | PROVED |
| Lemma 3.2 (local attainability at B_12(t)'s ties) | PROVED; CHECKED (b) |
| Lemma 3.3 (contradiction shell; replaces (R)) | PROVED |
| **Thm 3.4 (no additive-gate jump, every valuation, every zero rule)** | **PROVED** |
| Cor 3.5 (Prop 3.4R without (R)) | PROVED |
| Values of p, h and the killer at t = 1/2, 2 | NUMERICS |
| Prop 4.1 (tail-first lexicographic gate: tests and competitiveness) | PROVED |
| Conj 4.2 (lexicographic gates give full inheritance) | CONJECTURE |

**Scripts** (`r9/PP43_py/`; run `python3 -I -B <script> > <script>.out` inside the folder):

| Script | Content | Label |
|---|---|---|
| `exact43.py` → `exact43.out` | (a) Thm 2.3 at t ∈ {1/3, 1/2, 9/10, 11/10, 2, 3}, ε ∈ {3/10, 1/10}: exact witnesses of R (T silent, B strictly 3-better; the rank pattern is (1, −1, −1) on M_1 for t < 1 and (−1, 1, −1) on M_2 for t > 1); weak guidance of ψ^T and ψ^B; T u-optimal; B μ-optimal; the signs of κ; ψ^T_3 difference −K. (b) Lemma 3.2: exact generator points with F(s_2) = t ± η, B's exact Bayes answers, the field vectors, and exact positive decompositions of 40 random targets for each (ε, t). ALL PASS | CHECKED |
| `killer43_mc.py` → `killer43_mc.out` | p = Φ(B → T), h, and the killer arithmetic at t = 1/2, 2 (N = 400,000) | NUMERICS |
