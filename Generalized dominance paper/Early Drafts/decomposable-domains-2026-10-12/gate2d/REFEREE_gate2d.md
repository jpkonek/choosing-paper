# Referee report: "Separation-Gated Evaluators in Two Worlds" (20 Oct 2026)

Adversarial reading of `gate2d/Separation-Gated-Evaluators.tex`. The note itself was not edited. New files, all in `gate2d/`:
- `referee_check.py`: an independent exact-arithmetic checker, written from the note's definitions rather than from `check.py`;
- `referee_tc.py`: (TC) counts for the shipped verdict and for the note's verdict;
- `referee_precise.py`: targeted runs with cells inside a precise band (l = u);
- `referee_check_out.txt`: the output.

## Summary of verdicts

| Item | Verdict |
|---|---|
| 1. Lemma 1 (threshold sets) | **CONFIRMED** |
| 2. Lemma 2 (no cycles) | **CONFIRMED** |
| 3. Lemma 3, Theorem 4 | **CONFIRMED**, with two wording repairs (direct (C); "excludes ... at either world") |
| 4. Prop 5(a) | **CONFIRMED** |
| 4. Prop 5(b) | **CONFIRMED WITH REPAIR**: the case l(p) = u(p) needs a different rival. The intro's "near *any* selected boundary point" is **WRONG** and must read "almost every". "Neither adds up" also needs a finitely-additive extension (supplied below). |
| 4. Scripts vs Prop 5 | **WRONG as shipped**: `check.py` uses a different world-2 verdict from the note. The note's numbers reproduce only after a one-line fix. |
| 5. Prop 6 | **CONFIRMED (PROVED)** |
| 5. Paragraph after Prop 6 | Correctly labelled CONJECTURE. One small step needs adding. Intro item 4 and Next steps item 2 **overstate** it as a result. |
| 5. Remark 8 (triangle) | **CONFIRMED WITH REPAIR**: the product condition follows only if the reverse swaps are also judged by the rule. As written, the derivation skips the strict link. |
| 6. Remark 7 | Bullet 1 **CONFIRMED**. Bullet 2: the leading-charge point can be upgraded to **PROVED** by a direct argument (below), but "CHECKED by analogy" is a misuse of the label. Bullets 3–4 **CONFIRMED WITH REPAIR** (small). |
| 7. Finite checks | No cycle, no (TC) violation, no competitiveness failure, no dominated selected model, no failure of the section identity and no strict-(G) failure, for the note's verdict, on 75 configurations (3 families × 5 cell layouts × 5 seeds, up to 1024 models). A deliberately invalid control family is caught. |

Nothing was found that breaks Theorem 4. The main defects are:
- the scripts do not test the stated instance at world 2;
- one overstated sentence in the intro about non-endorsement;
- overstated claims about three worlds in the intro and Next steps;
- an under-argued Remark 8.

---

## 1. Lemma 1 (selected models are threshold sets): CONFIRMED

I checked the following line by line.

- **Mixed problems.** For g = r(1−t, −t), m·g = r(m₁ − t). So 𝒟_[l,u] accepts g iff t < l, and accepts −g iff t > u. The world-1 ranks are 0/1/2 on the three bands, and the world-2 ranks are 2/1/0.
- **(g,1) steps.** (g,1) ∈ U₁(C_p) ⟺ t ≥ l(p) ⟺ l⁻¹(t) ≥ p. This is exact, because l is a strictly increasing continuous bijection of [0,1].
- **(g,2) steps.** (g,2) ∈ U₁(C_p) ⟺ t > u(p) ⟺ u⁻¹(t) > p. This differs from {k₁ ≥ p} only on {t = u(p)}, which is null.
- **World 2.** (g,1) ∈ U₂ ⟺ t ≤ u(p) ⟺ 1 − u⁻¹(t) ≥ 1 − p, and (g,2) ∈ U₂ ⟺ t < l(p) ⟺ 1 − l⁻¹(t) > 1 − p. Both are correct.
- **Unanimous problems and j = 3.** C_p is correct on unanimous problems (ranks (0,0)) and never contradictory, so these steps are never in U_i(C_p). Their keys −1 − τ ∈ (−2, −1) lie below every threshold p, 1 − p ∈ [0,1]. Correct, including at p = 0, where U₁(C₀) is all mixed (g,1) and (g,2) steps, and at p = 1, where U₁(C₁) = ∅.
- **Null level sets.** {l⁻¹(t) = c} = {t = l(c)}, and similarly for u⁻¹. The level sets of τ are null by hypothesis. A level set of k_i is a union of at most three null sets.
- **Precise indices (l(p) = u(p)).** Nothing breaks: the silent band is a null set.

No issue.

## 2. Lemma 2 (no cycles): CONFIRMED

- **"Ranks determine advice."** True at each world separately, on both kinds of problem. Mixed: P, S, M, C ↦ 0, 1, 2, 3 at world 1 and 2, 1, 0, 3 at world 2. Unanimous: correct, silent, wrong, contradictory ↦ 0, 1, 2, 3. Problems with a zero coordinate are null. So U_i(X) = U_i(Y) a.e. forces X = Y a.e.
- **Does guidance always add a non-null set?** Yes. A nontrivial step accepted by guidance has T^off null, so T^on is non-null.
- **The window argument.**
  - β_j < esssup_{T^on_j} k ≤ γ_j uses only that T^on_j is non-null and that level sets are null.
  - γ := min_j γ_j over the finitely many nontrivial steps satisfies γ > β*.
  - Every T^off_j lies a.e. in {k ≥ γ_j} ⊆ {k ≥ γ}, so no step removes anything from W = {β* < k < γ}.
  - T^on_{j*} ∩ {β* < k < γ} is non-null: T^on_{j*} ∩ {k < β* + δ} is non-null for every δ > 0, and {k = β*} is null.
  - T^on_{j*} is disjoint from U_i(X_{j*}) ⊇ U_i(X₀) ∩ W, so the inclusion is strict. This contradicts X_m = X₀.
  - The case γ = +∞ (all steps are guidance steps) is covered.
- **Consequences.** (TC) and antisymmetry follow directly. X ⪯ Y ⪯ Z with Z ≺ X gives a cycle, which is nontrivial unless X = Y = Z, and that case is excluded by reflexivity.
- **No dependence on Φ.** The argument never uses Φ. It is a pure gate argument.

Airtight. I also checked it exactly (topological sort of the whole accepted relation; §7): acyclic in every configuration.

## 3. Lemma 3 and Theorem 4: CONFIRMED (two wording repairs)

- **Lemma 3.** T^on(C_p, X) ⊆ I ∖ U₁(C_p) ⊆ {k₁ ≤ p} and T^off ⊆ U₁(C_p) ⊆ {k₁ ≥ p}, so esssup T^on ≤ p ≤ essinf T^off. World 2 is the same with threshold 1 − p. Correct.
- **(IB).** The keys are fixed functions of the problem. T^on, T^off and the gate depend only on the advice on the difference set, and Φ_i does by hypothesis. Correct.
- **Strict (G).** Correct. The guidance clause gives "no worse". For "strict", T^on is null and T^off is non-null, so neither the guidance clause nor the gate (which needs T^on non-null) applies.
- **Section identity A_i(X) = {p : Φ_i(C_p, X) ≥ 0}.** The four cases are exhaustive and each is right. (V2) is used exactly where needed: both sets null, T^off null, and T^on null with T^off non-null. Closedness then follows from (V1). No hidden use of transitivity.
- **Competitiveness.** For p ∈ (0,1) it follows from (V3) and the identity. At the vertices, U₁(C₁) and U₂(C₀) are null (Lemma 1), so the guidance clause applies. Correct.
- **Undominatedness.**
  - From X ⪯₁ C_p, the gate would need esssup of a non-null set inside {k₁ ≥ p} (which is > p, by null level sets) to be ≤ essinf of a set inside {k₁ ≤ p} (which is ≤ p). That is impossible, so T^off is null and U₁(X) ⊆ U₁(C_p).
  - The rank-pair argument is correct. On mixed problems, (0,2), (1,1) and (2,0) are pairwise incomparable and (3,3) is worse than all three. On unanimous problems, (0,0) is uniquely best.
- **Direct (C).** The proof shows only that no model is tied with a *selected* model. The axiom quantifies over *all* coherent undominated models.
  - **Repair (either one):**
    - (a) cite antisymmetry (Lemma 2): a tie at any world already forces equality; or
    - (b) note that the final paragraph shows every non-selected model is dominated, so the coherent undominated models are exactly the C_p.
  - Both are one line. As written, the proof of (C) depends on a paragraph that comes after it.
- **Domination of the rest.**
  - A₁(X) ∋ 1 and A₂(X) ∋ 0. Both are closed, and they cover [0,1] by (V3) and the vertex facts, so they meet. Correct.
  - The sentence "the preceding paragraph excludes X ⪯_i C_q at either world" is imprecise. That paragraph shows only that X ⪯₁ C_q forces U₁(X) ⊆ U₁(C_q). To exclude it you also need C_q ⪯₁ X and antisymmetry, or ranks determining advice.
  - **Repair:** "Since C_q ⪯_i X, antisymmetry (Lemma 2) excludes X ⪯_i C_q unless X = C_q."
- **(LA), (LF), (SC).** Trivial on the full domain.

No escaping rival, non-closed section or hidden use of transitivity was found. Both in the proof and in the finite checks, the only place closedness matters is the meeting point q. In finite cell models this step fails as expected: A₁(X) is half-open because of atoms.
- Example (3 mixed + 1 unanimous cell, seed 1): X = (P,S,S,P) has A₂(X) = [0, 2749/4000] and A₁(X) = (2749/4000, 1].
- So "every non-selected model is dominated" is not finitely checkable. The note correctly does not claim it was checked.

## 4. Proposition 5

### (a) (V1)–(V3): CONFIRMED
- **(V1).** Continuity comes from μ(C_p △ C_q) → 0. The bound is at most two steps per problem per world (the note says three, which is harmless).
- **(V2).** Immediate.
- **(V3).** The bookkeeping is correct:
  - a regular-to-regular change moves the world-1 and world-2 ranks by δ and −δ, with equal ν-mass;
  - moves into contradiction, and moves on unanimous problems, add steps at both worlds and remove none.
  - Φ₁ + Φ₂ = a + b + 2c₁ + 2c₂ ≥ 0 is right.
- **"Accepts everything additive ν accepts."** Correct, because the gate is automatic out of selected models. Checked: `additive_not_accepted = 0` in every configuration using the note's verdict.

### (b) Non-endorsement: CONFIRMED WITH REPAIR

**The notion.** "Endorses" means ∫_{U_i(C_p)} f ≤ ∫_{U_i(X)} f whenever C_p ⪯_i X, with f > 0 a.e. on I. This is the right FF2-type notion on the full domain: every strictly guiding problem-separable loss has the form ℓ(g, r) = Σ_{j≤r} f(g, j). The Lebesgue-point argument is correct:
- the averages are with respect to μ = ρ dt ds, with ρ continuous and positive;
- Q_ε and R_ε are regular subsets of a square of side 6ε, so averages over them converge at Lebesgue points;
- X_ε is regular;
- the gate is automatic (Lemma 3);
- the world-2 version is symmetric and correct.

**Gap (a): indices with l(p) = u(p).** The hypotheses allow l = u, even on whole intervals; the note's own example has l < u only on (0,1). Where l = u, "use the boundary below the band instead" does not work: there is no band, and the obvious analogue compares f(·,2) on one side with f(·,1) on the other, which gives no contradiction. If l = u on an interval, such t₀ form a set of positive measure, so the a.e. claim genuinely needs a fix.

**Repair.** At t₀ = l(p) = u(p), C_p accepts g below t₀ (rank 0) and accepts −g above (rank 2).
- Make X silent on Q below t₀. This adds (g,1) steps, mass m.
- Make X accept g on R above t₀, with μ(R) = μ(Q). This removes (g,1) and (g,2), mass 2m.
- Then Φ₁ = 2m − 2m = 0, so C_p ⪯₁ X. Endorsement needs ∫_R (f₁ + f₂) ≤ ∫_Q f₁. At a common Lebesgue point of f₁ and f₂, this gives f₂(g₀) ≤ 0, a contradiction.
- World 2 is symmetric.

**Gap (b): "near any selected boundary point" (intro item 3) is WRONG as stated.** For a *fixed* selected model, endorsement of the comparisons localised near a fixed boundary point can hold.
- Fix p with l(p) < u(p) and t₀ = l(p). Take f(g,1) = 1 for t > t₀ and 11 for t < t₀, and f(g,2) = f(g,3) = 11, near g₀.
- For any record out of C_p supported in a neighbourhood of g₀ that avoids {t = u(p)}, T^off consists only of (g,1) steps above t₀, where f = 1. All of T^on has f = 11.
- Acceptance gives ν(T^off) ≤ 2ν(T^on). Hence ∫_{T^off} f = ν(T^off) ≤ 2ν(T^on) ≤ 11 ν(T^on) = ∫_{T^on} f. This f is integrable, positive and endorses.
- Prop 5(b) itself correctly says "for a.e. g₀", which by Fubini gives a dense set of indices p.
- **Repair:** "near almost every selected boundary point (a dense set of indices, in particular arbitrarily close to C_{1/2})". That is still enough for the FF2 use near the target.
- Caution: "a.e. t₀" gives "a.e. p" only if l⁻¹ maps null sets to null sets. For a general continuous strictly increasing l it need not, so say "dense".

**Gap (c): "neither adds up" (Remark 7) needs the finitely additive case.** The write-up's Def. addup allows a *finitely additive* weight that is positive on non-null sets; (b) excludes only integrable f.

**Repair (proof sketch, I believe complete).**
- Write π = ρν + π_p (Yosida–Hewitt decomposition).
- Positivity on non-null sets forces ρ > 0 a.e. If ρ = 0 on a non-null A, a carrier Z of π_p with ν(Z) < ν(A) leaves A ∖ Z non-null with π(A ∖ Z) = 0.
- In the (b) construction, choose a carrier Z_ε of π_p with ν(Z_ε) at most a small fraction of the square's mass, and replace Q_ε, R_ε by Q_ε ∖ Z_ε and a subset of R_ε ∖ Z_ε with twice its mass.
- These still occupy a fraction of the square bounded below, π_p vanishes on both, and the Lebesgue-point estimate for ρ gives the same contradiction.

With this paragraph, "neither world adds up" is PROVED in the write-up's sense.

**Weak (non-strict) fields.** These endorse trivially: for example, f = 1 on j = 3 steps and 0 elsewhere, since selected models have no j = 3 steps. That is expected, and the restriction to f > 0 is the right one. Mention it, so that no one reads (b) as excluding all fields.

### Scripts vs the stated instance: WRONG as shipped (repair: one line)

- `check.py` line 63 is `return 2*m(on) - m(off) if w == 1 else m(on) - 2*m(off)`. So world 2 uses Φ₂ = on − 2·off, which is **not** the note's Φ₂ = 2on − off.
  - The shipped world-2 verdict is the *anti-sticky* direction μ⁺ ≤ μ⁻, the intersection-of-additive case of the design memo.
  - It is stricter than additive: 290–7932 additive-accepted comparisons are rejected per configuration (`additive_not_accepted` > 0).
  - Ungated, it gives **0** (TC) violations at world 2 (`referee_tc.py`).
  - So the status block's checks at world 2 did not test the stated instance.
- `chains.py` as shipped gives **365,482** ungated (TC) violations on the 256 models, not 730,964. The figure 730,964 is reproduced only with the note's Φ (365,482 at each world).
- **Further discrepancies:**
  - `chains.py` uses 120 random starts with 4 mixed cells (the note says 150);
  - neither script runs the 2-mixed + 2-unanimous configuration the status block mentions.
- The intro's "both worlds read one record-based verdict with opposite signs" and Remark 6 describe the *script's* verdict (−Φ₁ on regular records). Prop 5 uses 2on − off at both worlds. Both satisfy (V1)–(V3): with the script's Φ₂, Φ₁ + Φ₂ = 2c₁ + c₂ ≥ 0. But they are different instances, and **only the note's version supports Prop 5(b) at world 2.** With on − 2·off at world 2, ν itself endorses world 2.
- **Repair:**
  - set `phi_sticky` to `2*m(on) - m(off)` at both worlds;
  - fix "150" and add the (2,2) run;
  - reword "one verdict with opposite signs" to "the same sticky verdict at both worlds".
- With the fix, every claim in the status block holds (§7): gated chains give 0 violations and 0 weak cycles.

## 5. Proposition 6, the paragraph after it, and Remark 8

**Prop 6: CONFIRMED (PROVED is correct).**
- The rival is well defined because the six problem sets are disjoint.
- a_i ⊆ T^on_i, because contradiction has rank 3 at every world. b_i ⊆ T^off_i, because D_i's advice has world-i rank 0.
- The chain of inequalities is correct, so the gate fails. The pair is not a guidance pair and X ≠ C_p.

**Paragraph after Prop 6 (labelled CONJECTURE).**
- **A missing step.** The inference "every interior selected model is a threshold set at some world" needs the observation that disjointness is no restriction. Crossed pairs can be shrunk: non-null subsets of a and b still cross, and μ is non-atomic. So any three crossed pairs, one per world, can be cut down to pairwise-disjoint problem sets. Add this sentence.
- **Equivalence.** "No crossed pair at world i" ⟺ "U_i(C) is a threshold set {k_i ≥ c}" up to null sets. Check: let α = essinf over U and β = esssup over the complement, test small bands at the two ends, and conclude α ≥ β.
- **Wording.** "The selected models that world i can defend against all rivals form a chain" should read "the interior selected models that are world-i threshold sets form a chain". A threshold set passes the gate, but defending also needs Φ ≥ 0.
- **Precise models.** The claim about precise models (pointwise world-1 dominance iff p ∈ [q, e₁] or the reverse; Farkas) is correct, and a chain then lies on one line through e₁.
- **The real gap is the one the note names.** Nothing shows that (S) forces a two-dimensional image. A selection whose interior image lies in three one-dimensional chains is not excluded. For example, a priori, an image in the three edges, or in a tripod; the tree result is cited for the latter and not verified here.

**Overstatements elsewhere (item 6).**
- Intro item 4: "a gate of this strong form makes (S) fail at interior indices (Proposition 6)".
- Next steps item 2: "A fixed linear priority order per world cannot work (Proposition 6)".

Both state the CONJECTURE as a result. Prop 6 proves failure only at an index where all three worlds have crossed pairs. **Repair:** "makes (S) fail at every interior index whose selected model is a threshold set at no world (Prop 6); that this happens for every two-dimensional selection is CONJECTURE".

**Remark 8 (labelled CHECKED): CONFIRMED WITH REPAIR.**
- **The construction.** Using (IB), the cycle runs through local models W₁ = {b,c}, W₂ = {c,a} and W₃ = {a,b}, which agree elsewhere. Each forward link is a swap whose local advice matches one of the three selected models. The note does not say this, and should.
- **The gap: forward links give only a cycle.** A (TC) violation needs some *reverse* link to be rejected. The reverse swaps (W₂ → W₁ adds b and removes a, and so on) match a selected model only if some selected model has a but not b, and so on. That is the *opposite* cyclic crossing.
  - If only one orientation is crossed among the selected models, the rule does not judge the reverse links, and a designer may accept them all. That makes ties, and (TC) is not violated whatever the product.
- **What is true** (proof below), if both orientations are crossed and all six swaps are judged by ρ with free masses: (TC) forces ρ_ab ρ_bc ρ_ca ≥ 1 and ρ_ac ρ_cb ρ_ba ≥ 1.
  - Write x = m_a/m_b, y = m_b/m_c, and P_f, P_r for the two products.
  - If P_f < 1 and no forward-oriented violation occurs, every reverse link must hold on the whole feasible region. That gives ρ_ac ≤ ρ_ab ρ_bc, ρ_ba ≤ ρ_bc ρ_ca and ρ_cb ≤ ρ_ca ρ_ab, hence P_r ≤ P_f² < 1.
  - Symmetrically, P_f ≤ P_r², so P_r ≤ P_r⁴. This is impossible for 0 < P_r < 1.
  - So P_f < 1 forces a violation in one of the two orientations.
- Example with ρ ≡ ½ and masses (m_a, m_b, m_c) = (1, 2, 3): W₁ ⪯ W₂ ⪯ W₃ ⪯ W₁, and W₁ ⪯ W₃ fails. This is a violation.
- **Label.** This is a short proof under stated hypotheses, not a computation. Label it PROVED (under the two-orientation hypothesis), not CHECKED.
- **The conclusion "the non-additivity cannot sit in two-point swaps around triangles" is too strong.** What is excluded is a triangle product below 1, that is, the sticky direction. A uniform spread ρ ≡ 2 is non-additive on two-point swaps and is triangle-safe, as the remark itself concedes in its last clause. Also, ρ < 1 on some swaps is compatible with the product condition. Reword: "the sticky direction cannot sit in two-point swaps around triangles".

## 6. Remark 7 and other comparative claims

- **Bullet 1 (Prop 1's chain): CONFIRMED.** The first link adds P and removes Q; the second adds Q and removes P ∪ R. The two gate conditions are incompatible.
- **Bullet 2.**
  - "Neither is complete": CONFIRMED.
  - "Neither adds up": CONFIRMED WITH REPAIR, using the finitely-additive extension in §4(b).
  - "Not a convex cone of records": true, but unproved in the note. One line suffices: records (add Q₁, remove R₁) and (add Q₂, remove R₂) with keys Q₁ < R₁ < Q₂ < R₂ are each gated, and their sum fails the gate.
- **Leading charge.**
  - "CHECKED by analogy" misuses the CHECKED label, and the route via S21 is unnecessary. A direct proof makes it **PROVED** on the full domain, under the transposed definition (π a bounded charge ≥ 0 on I, vanishing on null sets, with (i) π(B∖A) > π(A∖B) ⇒ A ≤_i B and (ii) A ≤_i B ⇒ π(A) ≤ π(B), for step sets of models).
  - *Proof.* Suppose π ≠ 0.
    - I is a finite union of "kinds": layer j ∈ {1,2,3} × {mixed, unanimous}. So π(S) > 0 for some non-null S inside one kind. Keys are non-degenerate on each kind.
    - Pick c with S ∩ {k < c} and S ∩ {k > c} both non-null.
    - Pick a non-null D ⊆ S ∩ {k < c} with π(D) < π(S)/2, by splitting into n non-null pieces. Put P = S ∖ D.
    - Then π(P) > π(D) and esssup_P k > c > essinf_D k.
    - Let X have world-i rank j − 1 on the problems under P and rank j on those under D, and let Y swap these two ranks, with X = Y elsewhere. Then T^on = P and T^off = D.
    - (i) demands X ⪯_i Y. But the gate fails and T^off is non-null, so X ⋠_i Y. Hence there is no nonzero leading charge, at either world.
  - This is just incompleteness at work. Say so, because it makes the comparison with the 15 October list less informative than it sounds: any gated world lacks a leading charge for this reason alone.
  - The 15 October claim itself ("open: incomplete, not CP-a, no leading charge, certificates not point-localised") matches `P4B_referee.md`. The note omits "not CP-a" and "certificates not point-localised" from the list; it should either check them or quote the class more loosely.
  - Note also that the worlds here *are* endorsed by a non-strict, purely finitely additive charge: a {0,1}-valued charge concentrated at the bottom of the key order (k → −2). It satisfies (ii) but not (i), and it is not positive on non-null sets. Worth a sentence: it is the "leading" criterion of the lexicographic order in bullet 3.
- **Bullet 3 (lexicographic).**
  - CONFIRMED that each world is contained in the continuum lexicographic order with *low keys first*: X ≺ Y iff some {k < c} meets T^on in a non-null set and T^off in a null set. State the direction.
  - "Not lexicographic over countably many additive criteria" is true for a trivial reason: such orders are complete, and these worlds are not.
  - Whether the write-up's lexicographic exclusions apply to sub-relations of a lexicographic order is not addressed. The bullet should not suggest that the construction "escapes" them in any deeper sense.
- **Bullet 4 (adding five-region patterns): CONFIRMED WITH REPAIR.** The added comparisons must:
  - (1) pass the gate;
  - (2) respect (IB), i.e. be closed under changes off the difference set;
  - (3) for each X, add a closed set of indices to A₁(X), so that sections stay closed.

  Undominatedness is unaffected, because no gated comparison into a selected model exists. (TC) is unaffected by Lemma 2.
- **Intro item 2.** "In fact it has no cycles at all" is CONFIRMED.

## 7. Finite checks

**Setup.** `referee_check.py` is an independent implementation, with exact Fractions and distinct finite keys.

**Families of (l, u):**
- the note's family;
- `precise_band` (l = u on [0.7, 0.8]);
- `wide` (C_{1/2} = 𝒟_[0.1, 0.9]);
- `invalid_control`, with u decreasing on part of its range, as a control.

**Cell layouts:**
- (mixed, unanimous) = (3,1), (2,2), (4,0), (1,3), (3,2);
- 5 seeds each;
- up to 1024 models.

**Tests:**
- full acyclicity of each world (topological sort of the whole accepted relation, which is stronger than two-step chains);
- competitiveness at every critical index (both endpoint pre-images of every cell, midpoints, and a 65-point grid), against every model;
- no model weakly better than a selected model at both worlds;
- the section identity of Theorem 4;
- Prop 5(a) "accepts what additive ν accepts";
- strict (G) on all pairs;
- strict domination of every non-selected model.

**Results** (`referee_check_out.txt`, 25 configurations per row):

| family, verdict | cyclic worlds | competitiveness failures | dominated selected | section-identity failures | additive-accepted but rejected | strict-(G) failures | non-selected models not dominated |
|---|---|---|---|---|---|---|---|
| note, note Φ | 0 | 0 | 0 | 0 | 0 | 0 | 101 (atoms) |
| precise_band, note Φ | 0 | 0 | 0 | 0 | 0 | 0 | 99 (atoms) |
| wide, note Φ | 0 | 0 | 0 | 0 | 0 | 0 | 124 (atoms) |
| note, shipped `check.py` Φ | 0 | 0 | 0 | 0 | **63,373** | 0 | 530 |
| invalid_control, note Φ | 0 | **1,895** | **9** | **5,116** | 4,407 | 0 | 97 |

**Precise band.** Only one random layout put a cell inside the precise band, so `referee_precise.py` places cells there deliberately (6 runs). Again: no failures except the atom artifact.

**The "not dominated" column.** In every case examined, this is the expected atom effect. Each A_i(X) is a half-open interval at a cell breakpoint, so the two sections cover [0,1] without meeting; see the example in §3. It is not evidence against Theorem 4, whose meeting-point step needs the continuity (V1) that finite cells lack.

**(TC) counts** (`referee_tc.py`, the 3 + 1 cells of `chains.py`, seed 5):
- ungated, note Φ: 365,482 violations at each world (730,964 in total, which is the note's figure);
- ungated, shipped Φ: 365,482 at world 1 and 0 at world 2;
- gated, either Φ: 0.

**Not attempted.** No search was attempted for a (TC) violation by a non-gated mechanism, since Lemma 2 is a proof.

## Requested repairs, in one list

1. Theorem 4 proof, direct (C): cite antisymmetry, or move the paragraph after "domination of the rest".
2. Theorem 4 proof, last paragraph: "since C_q ⪯_i X, antisymmetry excludes X ⪯_i C_q unless X = C_q".
3. Prop 5(b): add the l(p) = u(p) rival (silent below; accept g above with equal mass).
4. Prop 5(b), Remark 7: add the finitely-additive (Yosida–Hewitt carrier) paragraph before claiming "neither adds up".
5. Intro item 3: "near almost every selected boundary point (a dense set of indices)", not "near any".
6. `check.py` line 63: use `2*m(on) - m(off)` at both worlds. Also:
   - fix "150 random starts" (the script uses 120);
   - add the (2,2) run;
   - reword "one verdict with opposite signs".
7. Remark 7, leading charges: replace "CHECKED by analogy" with the direct PROVED argument above, and note that it rests on incompleteness. Complete the 15 October class description (not CP-a; certificates not point-localised).
8. Remark 7, bullet 4: state the (IB) and closedness conditions on added patterns.
9. After Prop 6: add the shrinking/disjointness sentence, and fix "can defend against all rivals". In intro item 4 and Next steps item 2, mark the three-world impossibility as CONJECTURE.
10. Remark 8:
    - state that the product condition needs both cyclic orientations among the selected models;
    - give the P_r ≤ P_f² argument;
    - relabel it PROVED (under that hypothesis);
    - weaken "non-additivity cannot sit in two-point swaps" to "the sticky direction cannot".
