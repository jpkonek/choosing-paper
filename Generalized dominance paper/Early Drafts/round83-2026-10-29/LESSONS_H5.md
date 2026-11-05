# LESSONS_H5: rounds 67–82 and the post-82 audit notes (26–29 Oct 2026)

**Sources.** The Projects tool was not available in this session, so I could not open the `claude/…` project docs directly. I used the local source material those docs were written from:
- scratchpad `r67`–`r82`: the ROUND, REF, BRIEF and AUDIT files; S81, FS81, REF81, W82 and REF82; `rescaled-coverage.tex`; `appshort.tex`, read in full;
- `/mnt/attach/outputs/r71`–`r82`;
- the auditor's messages in `/mnt/user-data/attachments`;
- every requested device `.md` file. `definition-audit-2026-10-27/` and `desirability-scope-2026-10-28/` contain no `.md` files; I skimmed their diffs.

I did not read the axiom inventories (AX70A/L) or the proof outlines (OUT67/LDGO67) line by line; I worked from their summaries.

**Labels.**
- PROVED (refereed) or CHECKED: as recorded in the documents.
- H5-PROVED: my own argument, not refereed.
- H5-EVIDENCE: a numerical check only.

---

## 1. Chronology of attempts

**R67. Full-domain repair theorem (completion round).**
- *Aim:* finish the mathematics for both papers.
- *Assumptions:*
  - Ω arbitrary;
  - E separable, sup-norm closed, containing 1;
  - (M1) finite first moment and (M2) null boundaries;
  - models taken modulo μ.
- *Result:* PROVED. Every incoherent X has a coherent N that improves on it by a uniform margin at every world, with N ⊆ hull(X∖N), so no coherent model could make the change X→N.
- *Also PROVED:* LDG's compactness condition (CC) is equivalent to its conclusion, and the local finite-to-compact theorem is genuine.
- *Mechanism:* a single minimax lemma ("optimise in the hull, then trim"). Coherence enters the ranking only through the clause "no coherent model could make the change".

**R68–70. Definitive manuscripts and the axiom audit.**
- *Result:* PROVED, with manuscript-level refereeing.
- *Changes made:*
  - Acyclicity was replaced by finite-chain consistency, which allows ties.
  - Reflexivity was dropped from the definition of a ranking.
  - The fact that LDG derives dominance, rather than assuming it, was made explicit.
  - The ranking R0 was characterised by maximality: guidance is accepted; accepted comparisons strictly raise the integrated payoff; and **condition (3)**: a change available to a coherent model is accepted only through guidance.
- *Mechanism of the audit:* separate assumptions, sufficient conditions and conclusions. This found real slippage, such as sufficient conditions read as necessary and "some ranking" read as "every ranking".

**R71. Maximal score-consistent extensions.**
- *Assumptions:*
  - (G) guidance;
  - (I) independence;
  - strict score consistency;
  - single-ranking protection of every coherent model;
  - maximality.
- *PROVED:*
  - **Exact protection criterion:** every coherent model is undominated iff every change available to a coherent model is refused somewhere.
  - **Maximal rankings:** V(r) = P(r) (the worlds where r improves the score), except that each *dangerous* change r (available to a coherent model and improving everywhere) is refused at exactly one non-guided world j(r).
  - **Class theorem:** every ranking between R0 and a maximal ranking covers. So condition (3) is unnecessary; it only selects the smallest member of the class.
  - Maximality is incompatible with disjoint additivity (a 3-world, six-ball example).
- *Mechanism:* each condition constrains one change at a time, so the problem factorises change by change.
- *Limitation:* everything rests on strict score consistency with the integral, so it does not meet the score-free goal.

**R72. Score-free maximality.**
- *Assumptions:* (R), (G), (I), the chain condition (SC) and (P), under strict-preserving maximality or under inclusion.
- *Outcome:* FAILS (PROVED).
- *Counterexample:*
  - Ω = {1,2}, Gaussian μ;
  - s′₁ = ∫h₁ and s′₂ = ∫f(h₂), with f(t) = 2t for t ≥ 0 and t/2 for t < 0;
  - X* = {h₁ + f(h₂) > 0} is a non-convex cone (incoherent), yet it is strictly preferred to every rival at some world.
- *Mechanism:* sign-respecting scores that distort magnitudes differently at different worlds reward splitting a commitment. The failure lies in comparisons the ranking already makes, not in missing ones, so no extension principle can repair it. This identified **splitting** as the defect.

**R73. Consolidation and Theorem D′.**
- *Assumptions:*
  - (A1) guidance at every world;
  - (A2) the three-model condition;
  - (A3) transitivity through ties;
  - (A4) margin consolidation: sums with masses t, t, t, and midpoints with masses t, t, 2t;
  - measure conditions (M2) and (M3′).
- *Outcome:* PROVED. **Under these, every incoherent model is dominated**, for any Ω. The proof uses no score, independence, admissibility or maximality.
- R0 satisfies (A1)–(A4) and protects every almost coherent model, so the class is nonempty.
- *Mechanism:* a model that is undominated must keep its consolidations tied with it. Incoherence then gives at most two consolidations followed by a guided-everywhere change.
- *Sharpness:* (M3) cannot be dropped (CHECKED, 3-ball LP).

**R74–R78. Writing rounds.**
- The application was rebuilt around D′. Irrationality now means "dominated under every ranking".
- R76: coherence means (D1)–(D4); models are "almost coherent" if equal a.e. to a coherent set.
- R78: LDG's argument is (E), (A), (S), (T) ⇒ the permissible models are exactly the coherent ones, with (S) in the v2 form (undominated coherent assigned models).
- No new mathematics.

**R79–80. The literature under LDG's conditions.** PROVED and refereed.
- *Mixed verdicts:*
  - merely proper scores fail (T);
  - SSK Examples 4–6 fail;
  - Joyce's class fails (S) for every N ≥ 3 and fails (T).
- Gaps in Pettigrew 2022, Nielsen 2021 and Predd §7.2 were found.
- *Mechanism:* (S) and (T) are exactly where published arguments are silent: discontinuity, flatness, and infinite values.

**R81. Linking desirability to LDG.**
- *Finite-sequence theorem:* PROVED. Suppose x₁,…,x_r each weakly dominate their predecessor, starting from x₀, and z weakly dominates x_r, strictly at some world. Then some member of the sequence dominates x₀.
  - The weakest hypothesis needed is (TD): models tied at every world have the same dominators.
  - (A3) ⇒ (T∀) ⇒ (W) ⇒ (TD), and each implication is strict.
- *Geometric lemma:* PROVED, ranking-free. Every incoherent model admits at most two consolidations followed by a guided-everywhere change.
- *Theorem 4.1′:* (A1), (A4) and (TD) suffice; (A2) was never needed.
- *(S) for R0:* FAILS for n ≥ 2 (see §1a below).
- *Coherence-floor ranking R\*:* PROVED to satisfy (S). It works by stipulating that all almost coherent models are tied, which costs score consistency.

**R82. Cover loss on rescaled families.**
- *Assumptions:* (M1), (M3) and the new (M5) (bounded density along constant shifts); the conditions (CC), (Lip) and (Dom); finitely many worlds.
- *Outcome:* PROVED and refereed. (E), (A), (S) and (T) hold for 𝔏 = {L^M}, with c_p = D_{K_p} and K_p = {p∗m/(p·m)}. (CC) is proved for the rescaled family.
- *Outcome:* FAILS independence (post-82 Assessment, §1b) and FAILS (A4).

**Post-82 audit (29 Oct).**
- Three repairs of R82 fail (§1c).
- *Distance-to-target* L_C(X) = μ(X Δ C): satisfies (A1), independence, (S) and (T). It fails world-by-world guidance and is rejected.
- *Domain-restricted payoff:* evaluating only subsets of D_M gives everything, plus the original (S). Rejected because the domain is restricted.
- *Theorem W:* PROVED.
- *Weakened selection for R0:* FAILS (2-world counterexample).
- *Box baseline:* PROVED (§1d).

### 1a. Why (S) fails for the integral ranking (S81 and REF81)

**Prop 1 (CHECKED).**
- A change from a coherent rival X to c_p is available to X. So clause (ii) of R0 is blocked, and c_p ⪰_ω X iff the change is guided at ω.
- Serving the vacuous rival V and the interior precise rivals D_q forces c_p = H_ω := {h_ω > 0} for some ω ∈ supp p.
- The sets A_ω(D_q) ⊆ {p : c_p = H_ω} are then disjoint closed sets that cover the connected Δ. This is impossible.

**Prop C (PROVED, with REF81's added hypothesis).**
- *Setting:* finite Ω, μ with Lebesgue null sets, (M1).
- *Hypothesis:* the ranking is score-consistent against incoherent rivals (c ⪰_ω Y with Y incoherent ⇒ s_ω(c) ≥ s_ω(Y)), and (S) holds.
- *Conclusion:* every c ∈ C_L is tied at every world with a precise D_r ∈ C_L.
- *Theorem A:* with score consistency in both directions, C_L contains only precise models.
- *Mechanism:*
  - Incoherent models are dense: perturbation fact F4.
  - So defending on supp p\* against all incoherent rivals means weak Pareto-maximality of the score vector in the convex Lyapunov range.
  - Separation then makes the model a Bayes model, and Bayes models are unique (F1).
  - An imprecise D_Q is strictly beaten at both worlds by a precise D_t, by 2(cos m, sin m)(1 − cos d) > 0.
- Without score consistency the conclusion fails. REF81's write-in ranking (D_Q is weakly best) satisfies (A1)–(A4), (S) and (T).

### 1b. Exactly why round 82 fails independence

The loss is defined by cases:
- if some benchmark covers X at i (E_i(X) ⊆ E_i(D_{K_p}) a.e.), then L(X,i) = inf over covers of [1 − p_i − η·μ(E_i(D_p) ∖ E_i(X))];
- if none does, L(X,i) = 2 + μ(E_i(X)).

Whether a cover exists is a property of the **whole** error set. Shared advice that every coherent benchmark rejects (a strictly negative patch F) puts F into the error set of both models. No benchmark covers F, so both models switch to the fallback regime, which compares raw error masses.

**Explicit reversal (Assessment §2).**
- Take X = D₁∖A, with A a small positive ball and μ(A) = a < ½, and Y = D₂.
- Before adding F: L(X,1) = 2 + a > 1 = L(Y,1).
- After adding F to both: L(X∪F,1) = 2 + a + f < 2 + ½ + f = L(Y∪F,1).
- Taking F ∪ (−F) gives the binary-problem version of the reversal.

**Consolidation (A4) also fails.** If both models contain a negative F, a sum consolidation raises the fallback loss by t at every world.

### 1c. The audit's three failed repairs (unrefereed, direct)

1. **Add the comparisons that independence copies.**
   - Take nested A₁ ⊊ A₂, X_k = D₁∖A_k, and Y = D₂.
   - Independence plus the old comparisons force X_k ⪰₁ Y and Y ⪰₁ X_k for both k.
   - Guidance forces X₁ ≻₁ X₂. The chain X₂ ⪰ Y ⪰ X₁ with X₁ ≻ X₂ violates (A2).
   - So acceptances must be deleted, not only added.
2. **Delete context-sensitive comparisons**, keeping only verdicts that survive every replacement of shared advice.
   - Take the symmetric contamination target T = D_M with M = {m_i ≥ a}.
   - Put X = T ∪ E₁ ∪ E₂ ∪ E₃, where E_i is a silent patch negative only at world i. At each world X adds two correct patches and one wrong one.
   - With a shared negative F, the old loss prefers X∪F at every world.
   - So the subrelation must refuse T ⪰_i X at every world, and T cannot be an assigned universal defender. (T may still be protected through incomparability.)
3. **Apply the cover test only on H = X Δ Y.**
   - This is independent, but it has a strict 3-cycle even for K_p = {p}.
   - The four locations are a = (1,1,1), b = (4,6,−3), c = (3,4,−3), d = (−3,4,−5), with error sets {a}, {b,d} and {b,c}.
   - The cover values 4/7, 1/2 and 3/7 give X ≻ Y ≻ Z ≻ X, with gap 1/14. The cycle survives on small balls.
   - The whole-model compatibility condition (CC) does not hold for restricted tests.

### 1d. Theorem W, and the box baseline

**Theorem W.**
- *Data:* one rival-independent assignment p ↦ b_p, and for each x ∉ C closed sets A_i(x).
- *Conditions:*
  - **W1:** b_p ⪰_i x on A_i(x);
  - **W2:** every p lies in some A_i(x) with p_i > 0;
  - **W3:** at every common point, b_p and x are not tied at every world.
- *Conclusion:* KKM gives a dominator b_p of every x ∉ C.

Relative to (S), W:
- drops the obligations against coherent rivals;
- drops coherence and undominatedness of b_p;
- requires closed witnessing subsets only;
- excludes ties only at intersections;
- does not require the target to be assigned.

(S) and (T) imply W, strictly (one-world example). Open strict defences can be turned into W through a partition of unity, but that method forces every b_p ∈ C.

**W fails for R0** (2 worlds).
- Under R0, the models that defend against every incoherent rival are exactly V₁ and V₂.
- X\* = N∖U (with N = {h₁ + h₂ > 0} and U a small ball about (1,1)) is weakly dominated by neither.
- So A₁(X\*) and A₂(X\*) would be disjoint closed sets covering [0,1], which is impossible.

**Box baseline.**
- *Score:* s_i(X) = ∫_X ψ_i, with ψ_i = l_i g_i⁺ − u_i g_i⁻.
- *Properties:* complete, additive, independent, guided world by world, on the full domain.
- *Bayes models:* the Bayes set at p is D_{K_p}, where K_p is the rescaling of the normalised box. So C_L = {D_{K_p}}, and (S) and (T) hold.
- *Coverage:* every interior 2-world interval; in 3 worlds only normalised boxes (e.g. a hexagon).

---

## 2. Recurring obstructions

1. **Coherent-availability blocking.**
   - *Where:* S81 Prop 1; "Relational"; "Counterexample to weakened selection".
   - *Mechanism:* R0 protects coherent models by refusing every non-guided change available to some almost coherent model. The same clause stops an interior precise D_p from defending against nearby incoherent rivals such as D_p∖(A∪B), because that change is available to the vacuous model.
   - *Consequence:* only vertex models defend universally, and connectivity of Δ then gives a contradiction. This kills (S) and also W.
2. **Score consistency forces precision (Prop C).**
   - Incoherent models are dense, so universal defence against incoherent rivals means Pareto-maximality of the score vector, which means the model is Bayes.
   - *H5-PROVED (direct adaptation):* the same argument applies to W. If a ranking is score-consistent against incoherent rivals, W1–W2 at p force b_p = D_{r(p)} a.e., with supp r(p) ⊆ supp p. So **W implies that every incoherent model is dominated by a precise model.**
   - The same holds with any additive sign-respecting score ψ in place of the payoff: the assigned models must then be ψ-Bayes models.
3. **Independence couples protection with defence.**
   - Independence makes the verdict on "add S" the same in D_M → D_M∪S and in D_r∖S → D_r.
   - Protecting D_M needs that verdict to be refused at some world. Defence needs it to be accepted at some world in supp p.
   - Every construction has to choose these world sets consistently and closed-set-wise. This is the core tension in 1b, 1c and 2.1.
4. **Whole-model benchmark tests violate independence (R82).** Localising them breaks consistency (repair 3).
5. **Rival dependence versus a common assignment.**
   - Consolidation and repair produce dominators that depend on the rival. (S) and W need a p-indexed family.
   - A rival-dependent assignment is equivalent to dominance itself, so it is tautological. This appears in AUDIT_B, S81 §3, "Relational" §4 and the Handoff §3.
6. **Splitting under distorted magnitudes** (R72). Any score family must exclude rewards for splitting. Consolidation does this; per-world-kinked scores do not.
7. **Stipulative rankings pass the abstract tests.** Examples:
   - R\*, R\*_Q;
   - REF81's write-in ranking;
   - ℓ + 3ι;
   - distance to target;
   - domain restriction.

   (S), (T), (A1)–(A4), and even independence with all-world (A1), are weak. Each positive result must be checked first against world-by-world guidance and the full domain.
8. **All-world (A1) versus world-by-world (A1\*).**
   - Many easy successes use only (A1).
   - REF82: the obstruction for M = Δ holds under (A1\*) and fails under (A1).
9. **Exact versus almost coherence.** Null modifications such as D ∪ {0} are tied with D, so (T) fails for exact coherence. All the theorems concern almost coherence.
10. **Infinite Ω.**
    - A union of a chain need not preserve protection (R71, R72).
    - Theorem A's extension to thm:local is UNCLEAR.
    - R82's budget estimates are finite-dimensional.

---

## 3. Positive mechanisms that worked, and their exact scope

- **Repair theorem** (R67). Any Ω; separable E containing 1; (M1) and (M2).
  - Every incoherent model is uniformly dominated by an undominated coherent model under R0.
- **Consolidation dominance** (D′ and 4.1′). Any Ω; (M2) and (M3).
  - Every ranking satisfying (A1), (A4) and (TD) dominates every incoherent model.
  - The proof is score-free and independent of admissibility. It is the cleanest result in the period.
- **R0 itself.** It satisfies:
  - (A1)–(A4);
  - **world-by-world guidance** (clause (i) together with the strict score increase);
  - **independence** (the verdict depends only on (A,B));
  - the full domain;
  - protection of all almost coherent models under a single ranking.

  So every binding constraint except (S) and W is already met. What it lacks is the LDG selection mechanism.
- **Bayes and KKM selection** for complete, additive, continuous scores: L_lin, boxes, R\*, the domain-restricted payoff. (S) is easy whenever the undominated class is the Bayes family of a continuous additive score.
- **R82 geometry** (CC, Lip, Dom, and (M5) ⇒ (M2)): valid, reusable lemmas.
- **Theorem W and its compact version:** valid abstract results, with an honest strictness proof.
- **R71 protection criterion:** exact, but only within the score-consistent class.

---

## 4. Assumptions dropped or changed, and why

| Assumption | What happened, and why |
|---|---|
| Acyclicity as "every cycle consists of identical models" | Became finite-chain consistency (R68). The old form was too strong and banned harmless ties. |
| Condition (3), the coherent-availability ban, as an axiom | R71: unnecessary; it only selects the smallest covering ranking. |
| Strict score consistency and integral recognition as axioms | Removed by the guidance after R71: the integral must not hide inside the general axioms. |
| Maximality as the bridge principle | Replaced by consolidation after the R72 counterexample. Retired in R74. |
| Independence | Part of the R72 class; unused by D′ and absent from appshort's (A1)–(A4). **Binding again** after the post-82 audit. |
| (A1) all-world guidance | Now superseded by world-by-world guidance (Handoff), because (A1) admits distance-to-target rankings. |
| (A2) | Dropped in R81: never used. |
| (A3) | Weakened to (TD) in R81. |
| Coherence of models | Became "almost coherence" (R76, desirability-scope): null modifications cannot be distinguished. |
| Consolidation as a requirement | Not required in the post-82 direction, because the cover loss fails it. Note that boxes still satisfy it (§6). |
| Universal admissibility | Became family-level or target-relative admissibility (A5 for 𝒦), so that each ranking can be tied to its target. |
| Dominator coherent and undominated | Weakened to ordinary dominance (R71 guidance; LDG irrationality redefined). |
| (S) form | v2 C_L form (R78), then W1–W3 allowed (post-82). |
| Domain | Full domain is binding. Restricted domains are rejected because they make the target maximal by fiat. |

---

## 5. Top five lessons

1. **Test candidates against "independence couples protection and defence" before building.** (Confidence: high.)
   - Every proposal in this period failed at the point where one shared change had to be refused (to protect the target) and accepted (for some p to defend):
     - R0 fails (S) and W;
     - R82 fails independence;
     - the repairs of R82 fail.
   - Specify V(A,B) ⊆ Ω, the set of worlds accepting each change, as the primary object. Check guidance, independence and W against it directly, not after building a whole-model loss.
2. **Under score consistency, selection pushes assigned models onto the Bayes family.**
   - (Confidence: high for (S), refereed; medium-high for the W extension, which is mine.)
   - So the W route should not aim to assign the imprecise target. Assign precise or Bayes models.
   - Protect the target separately, by incompleteness on exactly the changes that would dominate it, while keeping its near-incoherent perturbations dominated by assigned models.
   - Equivalently, W plus score consistency requires every incoherent model to have a *precise* dominator. That is a cheap first test for any candidate.
3. **Complete additive rankings are a closed question: decide it once and move on.** (Confidence: high for the reduction; medium-low for the 3-world limit.)
   - For s_i = ∫ψ_i, the undominated class is exactly the Bayes family {B_p}. All the other constraints are then automatic.
   - So the only question is whether every B_p is almost coherent (§6).
   - If the answer is "boxes only" for n ≥ 3, the next construction must be incomplete or non-additive. Independence does not require additivity: the verdict may be any relation on pairs (A,B).
4. **Keep the two dominance routes separate.** (Confidence: high.)
   - D′ plus the finite-sequence theorem is a complete, robust desirability result for every Ω.
   - (S) and W are a different, stronger mechanism.
   - Do not feed rival-dependent dominators into a "selection"; that is equivalent to dominance itself.
   - LDG gains a second general theorem: the finite-sequence theorem.
5. **State acceptance tests and binding constraints up front.** (Confidence: high.)
   - Rounds 81–82 produced valid theorems that were later ruled inadmissible: R\*, ℓ + 3ι, distance to target, domain restriction, and (A1) in place of (A1\*).
   - A short checklist would have flagged each at once: world-by-world guidance, arbitrary-context independence, full domain, a derived C_L, and no rival-dependent assignment.

---

## 6. My view of the box construction

**It is useful, but as a diagnostic and a consistency proof, not as a base to extend by tuning weights.**

- **It meets every binding constraint at once, together with the original (S) and (T).** It also satisfies (A4).
  - ψ_i = l g⁺ − u g⁻ with u ≥ l is concave and positively homogeneous, hence superadditive and monotone. So ψ(z) ≥ ψ(x + y + κ𝟙) > ψ(x) + ψ(y), and the midpoint case follows from concavity.
  - This matches MU73: among sign-respecting per-world integral scores, the consolidation-compatible ones are exactly a∫h⁺ − b∫h⁻ with b ≥ a.
  - No other construction in the record satisfies everything at once for some imprecise target.
- **It marks the limit of the obvious class (H5-PROVED).**
  - A concave, positively homogeneous ψ_i with sign(ψ_i) = sign(g_i) must be l g_i⁺ − u g_i⁻: its superdifferential is forced onto the ray through e_i.
  - So the box family is exactly the class of "concave additive" world-guided rankings.
  - The undominated class of any complete additive ranking is {B_p = {p·ψ > 0}}: Lyapunov, separation and uniqueness.
  - Hence a non-box target needs non-concave ψ all of whose mixtures still have convex positive sets.
  - Equivalently: for each g, the set {p : g ∈ B_p} must be one half-space section of Δ. A rescaled non-box family fails this, because that set is an intersection of one half-space per extreme point.
- **Two-world extension (H5-PROVED; H5-EVIDENCE confirms).**
  - Allow cross-coordinate weights ψ_i = w_i(g) g_i. On a mixed quadrant, give the positive coordinate weight 1/(1+t), with t = g_pos/|g_neg|.
  - Every B_p is then a convex cone, and B_u is the **vacuous** model.
  - More generally, any increasing F on each mixed quadrant gives coherent Bayes sets. So in two worlds every interval, including the boundary-touching and vacuous ones, is covered by complete, additive, independent, full-domain, world-guided rankings.
  - The weights depend on the other world's payoff. That is philosophically substantive, but not banned by the constraints.
- **Three worlds (H5-EVIDENCE, only suggestive).**
  - For the contamination triangle (a = 0.2), I built the symmetric cross-coordinate ψ whose uniform-prior Bayes set equals D_M exactly. The boundary of D_M is linear on the two-positive orthants and kinked on the one-positive orthants.
  - Its Bayes set at p ≈ (0.30, 0.56, 0.14) is non-convex. Such a set would be an incoherent undominated model.
  - The naive argmin-weighted ψ fails the same way.
  - My conjecture: in n ≥ 3, complete additive world-guided rankings cover only targets whose boundary is linear on each orthant, which are essentially the normalised boxes. Confidence about 50%. If true, the author's doubt is right for coverage, and the box's main value is to show that completeness plus additivity is the barrier.

---

## 7. Leads dropped too early or never tested

1. **Round-71 maximal rankings combined with W.** Never tested. A target-relative or canonical-j variant is the natural form.
   - They satisfy world-by-world guidance, independence, the full domain, (A1)–(A4), and protection of all coherent models.
   - They escape the two-world W counterexample. A dangerous change is refused at only one world, so D_p (|supp p| ≥ 2) always has a defending world in supp p by Bayes, and vertex models defend by guidance.
   - What remains:
     - a rule for the refusing world j(r) that makes the witnessing sets closed. The guidance after R71 had already withdrawn the "arbitrariness is ineliminable" objection;
     - the test from Lesson 2: does every incoherent model, e.g. D_Q∖U with U a mixed-sign ball, have a precise dominator?
2. **Cross-coordinate additive integrands** (§6). Settle the 3-world half-space problem for the contamination triangle in one bounded round, including asymmetric choices.
3. **Incomplete independent relations built on a Bayes ranking.** Start from L_lin, or the cross-coordinate version, to supply W with precise b_p = D_p. Delete exactly the acceptances that would let a precise model dominate D_M, using refusals at one world, as in R71.
4. **A finite-sequence analogue of W.** Combine consolidation sequences, which handle near-coherent rivals, with W, which is common selection, used only away from C. Untested.
5. **Prop C for infinite Ω, and R5 with selections other than D_p.** Both UNCLEAR and left open.
