# REFEREE_Z_PP19. Referee report on PP18 (Theorem Z and related claims), audit's short proof of Lemma R, and PP19

22 October 2026. Independent referee; one reader.

**Labels.** PROVED: complete proof given here or verified line by line in the note. CHECKED: exact exhaustive finite-cell computation. These check bookkeeping only and say nothing about (S). CONJECTURE / OPEN: as stated. No NUMERICS were used.

**Scripts.** `r9/PP22_py/split_defender.py` → `split_defender.out` (ALL PASS). I also re-ran `PP19_py/pointwise.py` (ALL PASS) and `PP18_py/s1_zones.py`. The second reproduces `s1_zones.out` byte for byte. It needs `python3 -B` without `-I`, because it imports `lib` from its own folder.

**Axioms used for checking.** These are exactly Brief 45's: reflexivity, strict (G), (IB), (TC) in the form "A ⪯ B ⪯ C implies not C ≺ A", (S), (LA) and direct (C). I treat transitivity, absence of single-world ties, absence of all-world ties between coherent models, and strictness of a repair at more than one world as **not** available.

---

## 0. Verdicts at a glance

| Claim | Verdict |
|---|---|
| PP18 Lemma 1.2 | correct |
| PP18 Lemma Z0, Cor 2.1 | correct |
| PP18 Lemma R | correct (strengthened in §2) |
| PP18 Theorem Z | correct |
| PP18 Z1, Z2 | correct, relative to the definition of the class |
| PP18 Z3 | correct with a wording repair |
| PP18 Props 4.1, 4.2, 4.3 | correct |
| PP18 §5: 5.1, 5.2, 5.4 | correct |
| PP18 §5: 5.3 | correct as stated in the body; "T-local" in §0 is undefined |
| PP18 §5: threshold-3 remark | slightly overstated |
| Audit's homogeneity proof of Lemma R | correct in the stated setting. It holds for **every** non-null Q in a bounded annulus, and in fact for every Q that is not a.e. a cone. This is sharp. |
| PP19 Lemmas 0.2–0.4, Theorem 1, Cor 1.1, Props 1.2, 2, 3 | correct |
| PP19 Theorem 4 (a)–(c) | correct |
| PP19 Theorem 4 (d) | correct under its stated no-tie hypothesis. Repair: drop that hypothesis for every non-conic E. |
| PP19 Lemma 5.0, Theorem 5 | correct |
| PP19 Cor 5.2 | correct with repair: it needs exposure |
| PP19 Theorem 6 | correct |
| PP19 Theorem 6 "Reading" (sharing within a class is unconstrained) | **wrong**; counterexample and Prop S below |
| PP19 Theorem 7 (a), and the dichotomy in (b) | correct |
| PP19 Theorem 7 (b)(i), "acceptance at i is not monotone in the rival" (also Remark 7.1, Q2′, §6.2) | **wrong**: the pattern is the monotone one |
| PP19 Lemma 8 (a)–(c) | correct |
| PP19 Lemma 8 (d) | informal, unclear |
| PP19 Prop 9 | correct. The tie caveat is explicit in (a) but dropped in §6.3. Repair for non-conic D′. |
| PP19 Prop 10 | correct but weak: it is an abstract relation with no (IB)/(G) closure |
| PP19 Prop 11 | (a), (c)–(f) correct. (b) understates what transfers. The C(iii) remark is correct. |

No PP19 proof silently uses transitivity, the absence of single-world ties, or strict repairs at several worlds. Every dependence on such assumptions is stated as a hypothesis. The list is in §4.

---

## 1. PP18

**Lemma 1.2 (correct; PROVED).** Around an accepted 3-cycle at w, each problem's rank returns to its start. Where the protected link goes up across ℓ, one of the other two links goes down across ℓ. The pigeonhole step gives a non-null set for one of them, and that is exactly what the zone forbids. A (TC) violation A ⪯ B ⪯ C ≺ A contains the cycle A ⪯ B ⪯ C ⪯ A.

The remark on the essential union of zones is also correct: the essential union equals a countable sub-union, and the zone property is an a.e. property. The sentence "every pointwise protection argument is of this form" is a description, not a theorem. It is fine as the definition of the class to which Z1 applies.

**Lemma Z0 (correct; PROVED).**
- Step 1 uses the zone only to get Z = X a.e. on Q. The correct answer at w is unique a.e.
- Steps 2–5: (N[D→Z], N) is a copy of rec(Z, X), because X = N on D.
- (IB) transfers both the weak verdicts and the failed reverse.

Only (IB), reflexivity and N's undominatedness are used. **Cor 2.1** is correct, because T is silent on R_i (audit's table, §13), so T[Q → majority] is a w-correct fill at both worlds j ≠ i.

**Lemma R (correct; PROVED).** I checked each step.
- Boundaries of open convex cones are null.
- A density point exists in Sil or in −C_K. The case C_K is impossible, because N would be w-correct on the cap.
- "An open convex set containing a.e. point of an open set contains all of it": put a small simplex around the point with vertices in the dense full-measure subset.
- Sil case: the cone over the segments from a ball B ⊆ C_K (which misses ±Ū) to q ∈ Q meets the open angular annulus in a non-null open set. There D_{K′} accepts, but X = N is silent.
- −C_K case: x ∈ −U is the midpoint of x ± v with v orthogonal to the plane of x and −g₀. With tan⁻¹(|v|/|x|) = 1.5r, both points lie at angle between 1.5r and about 1.8r from −g₀. So they are in C_K ∖ ±Ū, which gives −U ⊆ C_{K′}. Together with q ∈ C_{K′} this is impossible.

The proof only needs Q ⊆ U. So PP18's version already holds for **every** non-null Q inside the chosen cap U, not only for Q′ ∩ U.

**Theorem Z (correct; PROVED).**
- Lemma B uses only competitiveness at a vertex and strict (G).
- The vertex choice is right: V_j fails to be w-correct exactly on M_j ∪ M_w. The two vertices other than w cover all mixed problems.
- KKM applies, because for p in face I, supp p ⊆ I.
- Direct (C) is used only against the incoherent X, as the brief allows. Strictness is needed at one world only.
- Step 5 is Lemma Z0's copy argument with P := Q.
- Neither (TC) nor T1 is used. Single-world ties are irrelevant.

With §2 below, Q can be taken to be **any** non-null bounded subset of Q′. So the improving comparisons C_p ⪯_w X reach every bounded part of every mixed set.

**Z1, Z2 (correct).** Z1 is correct for the class as defined: mechanisms that rely on a 1-zone of positive measure in the mixed problems. Z2 is correct: the forbidden comparison has a selected better side and is a strict all-world domination of an incoherent fill. The "Scope" paragraph is accurate. Theorem Z excludes the invariant, not composition control.

**Z3 (correct with repair).** Run the same argument with N = T, an undominated coherent T, and R ⊆ Sil(T). The phrase "dominated at every world" should read "weakly dominated at every world and strictly at one".

**Prop 4.1 (correct; PROVED).** The disjoint Q_v exist by atomless splitting: choose each Q_v with measure below a third of the smallest remaining set. The rival is then refused at every v ∈ I.

**Prop 4.2 (correct; PROVED; cells CHECKED).**
- On R_i, T is silent, while Λ_T and V_{c*} give the majority answer. Indeed c*·g = d > 0 near (1, 1, −(2−3d)), from audit §13.
- For Y_12: world 3 is refused by strict (G), world 1 by the zone R_2, and world 2 by the zone R_1.
- The remark that the same holds for every selected source is correct in substance. Each of audit's C_i is silent on two of the three zones seen by every world, so it fails Prop 4.1.

**Prop 4.3 (correct; PROVED).**
- (a) The ν_w-weighted change is −ν_w((M_i ∪ M_k) ∩ Sil T) < 0.
- (b) Convexity follows from Lyapunov's theorem applied to the six atomless signed measures. Separation from the open negative orthant gives λ ≥ 0 with λ ≠ 0. On a full domain, minimisation is pointwise a.e.
- The costs are: silence a + b, majority 2a, minority 2b. Hence a = b on Sil T ∩ M_i.

**§5.**
- **5.1 (correct).** Here "error" means rank ≥ 2.
- **5.2 (correct).** Both the inclusion statement and the crossing corollary hold.
- **5.3 (correct as stated in the body).** It concerns rivals that agree with T on E_{w_T}. In §0, "T-local rival" is undefined and should be replaced by that phrase.
- **5.4 (CHECKED).** The table and the T[all W → majority] rival match the re-run cells.
- **Threshold-2 claim (correct).** Theorem Z's argument does not reach threshold 2: the dominator may be silent on part of Q, and then Lemma Z0's copy argument fails. The claim is only that the argument fails, not that error zones are consistent, and that claim is accurate.
- **Threshold-3 remark (slightly overstated).** It is true between coherent models. But a 3-zone can protect repairs of contradictory rivals, so "protects nothing a source field needs" is too strong. This does not matter for the next round.

---

## 2. Audit's homogeneity proof of Lemma R

**Verdict: valid in the stated setting.** The setting is problems g ∈ R³ modulo sign, μ Gaussian (so μ and Lebesgue measure have the same null sets), and the full measurable domain.

- A coherent model D_K depends only on the direction of g, so the disagreement set {C ≠ N} of two coherent models is invariant under nonzero scaling.
- In polar coordinates, a conic set S has Lebesgue measure zero iff its spherical trace has surface measure zero, iff S ∩ {‖g‖ > b} is null.
- So agreement off a bounded annulus forces agreement a.e.

**Lemma H (homogeneity; PROVED).** Let N be coherent and X any model. If {X ≠ N} is not a.e. equal to a cone, then X is not a.e. equal to any coherent model.

*Proof.* If X = C a.e. with C coherent, then {X ≠ N} = {C ≠ N} a.e., and that set is conic. ∎

Consequences:
1. **Yes, Lemma R holds for every non-null Q in an annulus,** and more generally for every non-null Q ⊆ Q′ that is not a.e. conic, e.g. any bounded Q. The reason is that {N[Q → w-correct] ≠ N} = Q.
2. **Sharpness.** For conic Q the conclusion can fail. Take N = V_j and Q = M_j ∪ M_w. Then N[Q → w-correct] = V_w, which is coherent.
3. **Scope.** The homogeneity proof needs non-conic models in the domain and μ not concentrated on an annulus. PP18's cap proof needs neither, and also works if problems are taken to be directions only. Both are valid here.

Lemma H is also what repairs the tie-dependent parts of PP19 (§3.2 and §3.6). Under direct (C), an all-world tie between a coherent protected model and a splice of it is possible only when the splice set is a.e. conic.

---

## 3. PP19

### 3.1 Q1 results

- **Lemma 0.2 (correct).** Only (TC) is used, and the note correctly says that the conclusion is a refusal, not strict superiority.
- **Lemma 0.3 (correct).** Φ_T = ⋂_w A_w(T) because T is undominated, so Φ_T is closed. It lies in the interior of the simplex: if p is in Φ_T with k ∉ supp p, take a majority fill on M_k ∩ Sil(T). By Lemma 0.2, C_p cannot accept it at i or at j, so C_p is not competitive. This argument does not need T's competitiveness.
- **Lemma 0.4 (correct).**
- **Theorem 1 (correct).** It uses only T ⪯_w C_p for p ∈ Φ_T, (TC), closed sections, and compactness of Φ_T.
- **Cor 1.1 (correct).** For fills, I(X) is computed correctly from strict (G). The "Sources" bullet takes audit's strict pattern as a hypothesis, so it is not a silent assumption.
- **Prop 1.2 (correct).**
- **Prop 2 (correct).** (a)–(c) follow from Theorem 1. (e) states its no-tie hypothesis, and its tie-allowing half does not assume that ≈ is transitive.
- **Prop 3 (correct).**
  - The Ramsey colouring is well defined because C_{n_j} is competitive.
  - The models are distinct by reflexivity.
  - Case (ii) consists of world-3 ties, which the brief permits.
  - (b) assumes the strict pattern C_n ≺_{1,2} T as a hypothesis; (a) does not.

### 3.2 Theorem 4

(a)–(c) are correct.
- (b) "T ⪯_k C" uses T's competitiveness against C.
- (c) uses KKM for nonemptiness and (a) for disjointness.

**(d): correct under its hypothesis, and repairable without it (PROVED).** The no-tie hypothesis enters only at "T[D → C_p] = T". Drop it and use direct (C) instead:
1. T′ := T[D → C_p] is all-world tied with T, so T′ is coherent.
2. Hence D = {T′ ≠ T} is a.e. conic.
3. But D = S ∖ E with S := {C_p ≠ T}. S is conic, and S ⊇ E because C_p = A on M_k while T ≠ A on E.
4. So E = S ∖ D a.e. is conic.

Therefore **Theorem 4(d) holds without any tie hypothesis for every E ⊆ M_k ∩ {T ≠ A} that is not a.e. conic**, e.g. every bounded E. For conic E it remains conditional. The full-fill step is still needed there when D is null.

### 3.3 Lemma 5.0 and Theorem 5

**Lemma 5.0 (correct; PROVED).** I re-derived each region:
- On D_Y, A₀ = C, because on D_Y ∖ D we have C = X = T.
- On D ∩ E, X ≤_w C.
- On D ∖ (E ∪ D_Y), T ≤_w C, by the covering hypothesis.
- Elsewhere the two models agree.

(B₀, Z₀) is a genuine copy of rec(T, Y), because B₀ = T on D_Y. Strictness comes from E ∩ D. The lemma uses (IB), strict (G) and (TC), and nothing about T.

**Theorem 5 (correct; PROVED).**
- Only weak acceptances C ⪯_i X_{E_i} and C ⪯_j X_{E_j} are used. No strictness of the repair at any world is assumed.
- Exposure (C ≠ A on part of E) is a hypothesis. Lemma 0.4 shows that exposure is automatic for any dominator that is strict at even one world when T is undominated.
- The class description is right: on M_k, being better at i or j and worse at k means "more A-ward"; on M_i and M_j it means "more B-ward"; on U it never happens. CHECKED in PP19 and independently in `split_defender.py` part 2.

**Corollaries.**
- 5.1: correct.
- 5.3: correct. The comparison with PP16's Theorem B is right: a minority-world-pointwise-no-worse dominator is excluded already by Lemma 0.2, strict (G) and rank injectivity.
- **5.2: correct with repair.** Theorem 5 needs exposure, C ≠ A on part of the full fill. Add "for a dominator strict at some world" and cite Lemma 0.4. Without strictness, a weak all-world dominator saying A on all of M_k is not excluded by the cited argument.

### 3.4 Theorem 6 and within-class sharing

**Theorem 6 (correct; PROVED).** The pointwise table is right.
- On M_3, a feasible y exists iff C is not strictly more A-ward than C′.
- On M_1 and M_2, y is forced to equal C, and it is feasible iff C is not strictly more B-ward than C′.
- On U, y = A always works.
- X never obstructs.

**The "Reading" claim that sharing within a class is not constrained is wrong.** Theorem 6 is silent about within-class sharing, but Lemma 5.0 does constrain it once the two worlds are served by different defenders.

**Proposition S (split-defender compensation; PROVED; table and example CHECKED).**

*Setting.* Assume (IB), strict (G) and (TC), and that T must be competitive against the rival Y constructed below (true under PP19's (H)). Take majority fills on M_k with majority worlds i and j. Suppose:
- C ⪯_i X_E and C″ ⪯_j X_{E′};
- both are exposed: C ≠ A on a non-null part of E, and C″ ≠ A on a non-null part of E′.

Put K_i := {C <_i T} ∖ E, K_j := {C″ <_j T} ∖ E′, K := K_i ∪ K_j, and P_i(C) := K_i ∖ {C <_k T}.

*Claim.* The following set is non-null:

  O := [K ∩ (E ∪ E′)] ∪ P_i(C) ∪ P_j(C″) ∪ [K_j ∩ M_i ∩ {C strictly more B-ward than C″}] ∪ [K_i ∩ M_j ∩ {C″ strictly more B-ward than C}].

(Points where either model says X are ignored in the last two terms.) With C″ = C this is exactly Theorem 5.

*Proof.* Suppose O is null.
1. K_i is non-null. Otherwise X_E ≤_i C everywhere, strictly on the exposed part, and that contradicts C ⪯_i X_E.
2. Outside O, a.e. on K there is advice y with y ≤_i C, y ≤_j C″ and y ≤_k T, and y ≠ T on K_i. This is the exhaustive table in part 1, 65 cases.
3. Put Y := T[K → y]. Lemma 5.0 for C at i, and for C″ at j, gives T ⋠_i Y and T ⋠_j Y.
4. Y ≤_k T pointwise, strictly on K_i, so Y ≺_k T by strict (G).
5. So T has no defence against Y. ∎

**Counterexample to the Reading (CHECKED, part 3).** Work on M_3. Take disjoint sets:
- H_1 ⊆ M_1 ∩ Sil T and H_2 ⊆ M_2 ∩ Sil T, on which C and C″ both say A;
- G_2 ⊆ M_2, where C says B;
- G_1 ⊆ M_1, where C″ says B.

Each model passes Theorem 5 on its own: P(C) = G_2 and P(C″) = G_1. But O is null. So T has no defence against

  Y = T[H_1 ∪ H_2 → majority],

which is an X*-type rival of exactly the kind Brief 45 requires T to answer.

The lesson for co-design: if a world-1 defender's own compensation is all world-2-type, and a world-2 defender's is all world-1-type, then the majority regions they share on M_1 ∪ M_2 must cross (the last two terms of O).

### 3.5 Theorem 7

**(a) (correct).** It uses only Lemma 0.2 at i and j and T's undominatedness. The special cases are stated as hypotheses. The tie case "C ⪯_k T" is handled correctly as a tie at k.

**(b) (correct, except for one sentence).** The dichotomy itself is correct and trivial: either q_0 ∈ Φ_T or not. In case (i), C_{q_n} ⋠_{i,j} X_{E_m} for large n follows from Theorem 1.

**The last sentence of (i) is wrong.** For m < n with E_m ⊇ E_n, X_{E_m} is a pointwise i-improvement of X_{E_n}. The model C_{q_n} accepts against the **worse** rival X_{E_n} and refuses against the **better** rival X_{E_m}. That is the monotone pattern.

Counterexample: any transitive, guidance-respecting world-i score s_i (e.g. an additive expected rank) with s_i(X_{E_m}) < s_i(C_{q_n}) ≤ s_i(X_{E_n}) realises it.

What regime (i) really forces is **escape**: the fills accepted at i by C_{q_n} leave every fixed fill. That is Prop 2(c). So Remark 7.1, Q2′ and §6.2 should say "creeping, escaping acceptance", not "non-monotone". The compatibility verdict in Remark 7.1 is unaffected, and it is correctly labelled an explanation, not a proof.

### 3.6 Lemma 8 and Propositions 9–11

**Lemma 8 (a)–(c) (correct).** I verified the record identities. For example, in (a) the third bullet works because on E ∖ D_C both H and C equal T. (d) is a heuristic ("only here can new constraints arise") with no precise statement; mark it **unclear**.

**Prop 9 (correct; PROVED).**
- The identity rec(T, X) = rec(C°, C) holds.
- In (a), C's undominatedness turns all-world weak acceptance into a tie, and direct (C) is applied correctly.
- "X is never a pointwise weak worsening of T at all three worlds" holds **without** the no-tie regime. If it were one, strict (G) would make T ≺_w X at every w, against the tie.
- **Repair (PROVED).** If D′ is not a.e. conic, then X = T[D′ → C] is incoherent by Lemma H. Under direct (C), the tie branch of (a) is then impossible. So **W_T(X) is a proper subset for every non-conic D′, with ties allowed.**
- §6.3 drops the tie caveat. It is correct only for non-conic D′, or under no ties.

**Prop 10 (correct, weak).** The two relations are strict linear orders, so (TC), mutual undominatedness, in-family competitiveness and the stated sections hold. But it is a relation on abstract labels. It is not closed under (IB) copies and it is not checked against strict (G) for actual models. "Consistent local skeleton" should be read only in that sense.

**Prop 11.** (a), (c), (d), (e), (f) are correct; I verified the copies in (c), (e) and (f).

(b) understates what transfers to an unselected but undominated T:
- Lemma 5.0 still yields refusals T ⋠_w Y. What is lost is only the contradiction from refusal at every world.
- Theorem 7(a) transfers in full, since it needs only undominatedness.
- Theorem 4(b) transfers except "T ⪯_k C".
- Theorem 4(a), 4(c) disjointness, and Theorems 5 and 6 do not transfer.

The Theorem C(iii) remark is correct. Its "necessary condition" restates the lead's (iii). The new consequence holds: p_0 ∉ U_K forces distinct M_n, by closedness of Φ_M, and Theorem 1 then applies with N = C_{p_0}.

---

## 4. Where extra assumptions enter

**Transitivity.** It is never used. Prop 10 has transitive orders, but as an example only.

**No distinct all-world ties** is stated in each place it is used:
- Prop 2(e), first sentence;
- Theorem 4(d) — repaired in §3.2 for non-conic E;
- Prop 9(a), last two sentences — repaired in §3.6 for non-conic D′;
- §6.1 ("absent ties");
- §6.3, where the caveat is missing.

**Strict source pattern C ≺_1 T, C ≺_2 T** is stated as a hypothesis in:
- Cor 1.1 "Sources";
- Prop 3(b);
- the first special case of Theorem 7(a).

If the new defenders tie T at world 1 or 2, these three do not apply. Prop 3(a) and the general part of Theorem 7(a) still do.

**Strict repairs at every world.** Never used. Theorem 5, Theorem 6 and Prop S use weak acceptances, plus exposure, and exposure needs strictness at one world (Lemma 0.4).

**Absence of single-world ties.** Never used. Wherever a single-world tie could occur, the notes conclude refusals (⋠), not strict preference.

**T selected (H).** This is a real dependence, and PP19 states it. Theorem 4(a) and (b) "T ⪯_k C", Theorems 5 and 6, and Prop S need T to be competitive against the specific (IB)-built rival Y. Theorem 1, Cor 1.1, Props 1.2–3 and Theorem 4(c) need a selection with closed sections.

---

## 5. What survives if single-world ties and triangle completion are allowed

1. **Everything proved above survives verbatim.** Triangle completion is what (TC) already demands of any system that satisfies it, so allowing it does not enlarge the class of systems that satisfy the axioms. Every PP18 and PP19 result derived from the axioms therefore remains a necessary condition. What the next construction gives up is only the extra hypotheses listed in §4.
2. **The kills cannot be absorbed by completion.** These kills all close a triangle with a **strict guidance** link:
   - Lemma 0.2 with a fill rival;
   - Lemma 5.0;
   - Theorem 4(b);
   - Theorems 5 and 6;
   - Prop S.

   (The step Y ≺_k T in Theorem 5 and Prop S is also strict (G).) Theorem Z and Lemma Z0 are different: they end in a domination of an undominated model, not in a triangle, so completion cannot affect them either. Completing such a triangle would install the reverse of a strict guidance comparison, which is audit's **F1**. So these obstructions are F1 instances in the closure framework. They are not merely triangles to be completed.

   Only conclusions whose strict link is a *non-guidance* verdict can shift when completion turns a stipulated strict verdict into a tie. These are Theorem 1 and Prop 1.2 for non-fill X, and the source-pattern items in §4. They stay true of the final relation, but their hypotheses may then fail.
3. **All-world ties buy little away from cones.** Direct (C) plus Lemma H gives: a coherent protected model can be all-world tied only with models differing from it on an a.e. conic set. So for bounded or otherwise non-conic splices:
   - the no-tie conclusions of Theorem 4(d) and Prop 9 hold unconditionally;
   - in the closure, every all-world tie of such a splice with a member of P is F2.

   Single-world ties are unrestricted by this.
4. **Constraints on variable defenders that remain in force.** Any registered C with C R_i X_E and C R_j X_E, for a majority fill on M_k, strict at one world, carries Theorem 5 compensation outside E. These compensations remain constrained even when defenders vary:
   - between majority-fill and minority-fill dominators (Theorem 6);
   - within one class when different defenders serve different worlds (Prop S).

   In both cases the killing rival can be an X*-type majority fill on M_i ∪ M_j. Choosing a new C after seeing X does not escape these constraints. It only changes which C must satisfy them.
5. **What they bind on depends on (H).** Theorems 5 and 6 and Prop S bind T only if T must be competitive against the rival Y they build. Brief 45's minimum class lists only X*, Y_12, Λ_T and V_{c*} for T. So in a construction where T is not selected (the tie route), these become obligations on T's selected tie partner (Prop 11) rather than on T. Under (H) they bind T directly.
6. **PP18 is unaffected.** Theorem Z still forbids any correctness zone of positive measure in the mixed problems. The next construction does not use zones, so PP18's live content is §5. It is CONJECTURE / OPEN whether error zones can carry a selection.
