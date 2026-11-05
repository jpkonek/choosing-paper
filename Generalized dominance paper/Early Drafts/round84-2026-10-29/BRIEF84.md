# Round 84 brief: commission-averse independent rankings under the weak selection package W

Folder (write ONLY here): /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r84/

Read first, all of them:
- ../r83/ROUND83_overview.md (section 0 first: it supersedes the rest where they conflict)
- ../r83/LESSONS_H1.md to LESSONS_H5.md
- The auditor's handoff and assessment, on the device and read-only via `mcp__remote-devices__device_bash`:
  - `$HOME/mnt/CPMs/outputs/ldg-relational-alternatives/Handoff - weaker selection and independent full-domain constructions.md`
  - `$HOME/mnt/CPMs/outputs/round83-review/Assessment and precise-assignment obstruction.md`
- ../r82/appshort.tex (the application paper's definitions).

Never write to the device.

## Binding constraints (no exceptions)
- **Worlds:** finitely many, Ω = {1,…,n}; start with n = 3 where stated.
- **Gambles and measure:** E = ℝⁿ, μ standard Gaussian.
- **Domain:** the full measurable domain; models are taken modulo null sets.
- **Coherent class:** the almost coherent models.
- **World-by-world guidance.** If the change X → Y is non-null, adds only gambles with g_i > 0 and removes only gambles with g_i < 0, then Y ≻_i X.
- **Independence**, for arbitrary measurable D and contexts F, G disjoint from D:
  (X∩D)∪F ⪰_i (Y∩D)∪F ⇔ (X∩D)∪G ⪰_i (Y∩D)∪G.
  Equivalently, the verdict at world i is a function of the change: the pair (added set, removed set).
- **Ordering conditions:**
  - reflexivity;
  - the three-model condition: no a ⪰_i b ⪰_i c with c ≻_i a;
  - transitivity through ties: if z and x are tied at i and y ⪰_i z, then y ⪰_i x.
- **Selection is Theorem W.** There is ONE assignment p ↦ b_p, the same for every rival, and the b_p may be imprecise. For each incoherent rival x there are closed sets A_i(x) ⊆ Δ such that:
  - **(W1)** b_p ⪰_i x for every p ∈ A_i(x);
  - **(W2)** every p lies in some A_i(x) with p_i > 0;
  - **(W3)** at any common point of all the A_i(x), b_p and x are not tied at every world.
- **Admissibility:** one ranking per target. The target D_M must be undominated. The undominated class of the ranking is derived, not assumed.
- **The author's ban on the ordinary integral score.** Do NOT use the payoff integral ∫_X g_i dμ or Brier, which are strictly proper scores, as:
  - a base ranking;
  - a consistency requirement;
  - a source of assigned models.

  The rankings sought are meant to render imprecise models undominated, for example because wrong acceptances (commission) weigh more than wrong rejections (omission).
- **Also forbidden:**
  - domain restriction;
  - distance to the target;
  - all-world guidance in place of world-by-world guidance;
  - stipulated ties among coherent models;
  - an imposed loss profile;
  - an assignment that depends on the rival;
  - assuming dominance.

## Known facts to respect
- **Additive commission-averse scores.**
  - The Hurwicz/box score s_i(X) = ∫_X (l g_i⁺ − u g_i⁻) dμ, with 0 < l ≤ u, satisfies every constraint above, together with the original (S).
  - Its undominated class is the rescaled box family. This is the control example.
  - Concave homogeneous integrands reach only boxes.
- **Theorem gm (refereed, 13–14 Oct).** No additive ranking covers the symmetric contamination triangle T1 = {m : m_i ≥ a}, 0 < a < 1/3, in three worlds with (S) and (C). The cause is half-plane charts versus T1's corners.
- **The audit's copy lemma.** If T is undominated and T ⊆ X ⊆ B, then B cannot dominate X.
- **Whole-model tests.** Rules that test whole models, such as cover existence, are context dependent, which breaks independence (9 Oct v3 Prop. 1; round 82).
- **Theorem E.** Rankings invariant under positive diagonal rescaling fail.

## Agent tasks

### C2: what survives under W (theory map)
For each of the following, decide whether it holds with W in place of (S) and (T). Give a proof or a counterexample, and state the hypotheses precisely.

1. **Complete additive rankings.**
   - Claim: if a ranking has world scores ∫_X ψ_i dμ, with ψ_i sign-respecting, measurable and not necessarily homogeneous or concave, and it satisfies W, then every Bayes set {p·ψ > 0} is almost coherent.
   - Hence Theorem gm's exclusion of T1 survives under W. Check gm's exact hypotheses: read `claude/the-contamination-triangle.tex` from the device copy `$HOME/mnt/Generalized dominance paper/Early Drafts/The Contamination Triangle.tex`, or the nearest file.
2. **Intersections of additive rankings.**
   - Lead's sketch: if D_M is undominated under the intersection, then it maximises a nonnegative combination of all the judges' scores, so it is the Bayes set of one mixture field φ. The mixture ranking's comparisons contain the intersection's. So any incoherent Bayes set of φ is undominated under the intersection, and W fails.
   - Make this rigorous, including zero weights and strictness, or refute it.
3. **Lexicographic combinations of additive scores**, e.g. commission first and omission second: what do they cover under W?
4. **The vacuous model.** Does the 11 Oct theorem (complete rankings with strict guidance, independence and (S) leave V dominated for n ≥ 3; "Three Complete Rankings Cannot Cover", "Complete Rankings for Any Number of Worlds" in the device Early Drafts) survive with W and the arbitrary-set independence?
5. **The audit's copy lemma, generalised.**
   - What does it imply for any incoherent X ⊇ T?
   - What must a dominator of X look like? Note that it must remove a non-null part of X.
   - Find further necessary conditions on rankings for which T is undominated and every incoherent X near T is dominated.

Output **C2_report.md**, with results first and labels PROVED / CHECKED / CONJECTURE / UNCLEAR / FAILS.

### C1: a construction attempt (main task)
**Target.** Build one independent, world-by-world guided, full-domain ranking, with no ordinary integral score, together with ONE common assignment, for:
- **(Step 1)** the audit's two-world pair. T = {g₁ + 3g₂ > 0, 3g₁ + g₂ > 0}, and X = T ∪ (two balls of radius 0.1 at (2,−1) and (−1,2)).
  - Identify X's dominator. It must not contain X.
  - Check it against a neighbourhood of such rivals using the same assignment.
  - Note that the box score with u/l ≥ 3 already handles this example. Use it as a sanity check, not as the answer.
- **(Step 2)** the three-world contamination triangle T1, which lies outside the box class.

**Requirements.** Since additive rankings are excluded for T1 (Theorem gm), the comparisons must be genuinely non-additive. Before proposing any rule:
- screen it for additive collapse (does a single additive field endorse all its strict comparisons out of the coherent undominated models?);
- screen it for dependence on context.

**Candidates to consider**, not to be taken as required:
- commission-averse rules that are lexicographic, threshold-type or region-dependent;
- the rescaled family of T1 as the assignment (the author's original preference), or another imprecise family;
- rules in which the weight on a wrong acceptance at world i depends on the gamble's whole payoff vector, as in round 83's cross-coordinate two-world construction (LESSONS_H5 §6), with non-additive aggregation over the change.

**For any candidate, prove or refute each of:**
- guidance;
- independence;
- the three-model condition;
- transitivity through ties;
- that T is undominated;
- W1–W3 for all incoherent rivals.

If the attempt fails, isolate the exact obstruction, and say whether it is axiom-level or construction-level.

Output **C1_report.md**, with results first.

## Both agents
- Plain English, rigorous, honest labels.
- Write only in the r84 folder.
- Use numerical checks for exploration only. Claims need continuum proofs.
- Final message: under 250 words.
