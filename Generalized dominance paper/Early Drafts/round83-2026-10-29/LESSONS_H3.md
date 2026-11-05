# LESSONS_H3: 12–19 October 2026 (domains, splice closure, the contamination triangle, non-additive rankings)

**Sources.** The Projects tool was not available to me. I read the project documents from copies on the device, in `Generalized dominance paper/Early Drafts/`: the Audit of Imported Assumptions and its Addendum, START HERE, the Exploration Map, the T1 Status Map, *Quorum Rankings and the Contamination Triangle*, gamble-based-hurwicz, and the intro and §§3–6 of *The Contamination Triangle*. *Splicing* and *Intersections* exist only as summaries in scratch (`r9/SPLICING_summary.md`, `r9/INTERSECTIONS_additive.md`). I read all 28 auditor assessments dated 12–19 Oct and the domain-axioms .tex; that folder contains no .md files. I spot-read FF1 and GG3. The *Consolidated Statements* and the *Round Report* I only skimmed.

**Notation.** T1 is the ε-contamination of the uniform distribution in three worlds. The "posterior" (rescaled) family is K_p = {p∗m/(p·m) : m ∈ T1}, the same family Round 82 used. "Adds up" means that some strictly positive weight endorses every relevant comparison out of the coherent undominated models. TC is the two-step no-reversal condition; FC is the finite-chain condition.

---

## 1. Chronology of attempts

**1. Audit of imported assumptions (12 Oct).**
- *Aim:* find assumptions that are not axioms.
- *Finding:* every obstruction up to then silently assumed that all measurable models are evaluable (an all-model domain). That was dropped. Three replacements were introduced:
  - local freedom (LF) at the target;
  - splice closure (SC);
  - extendability (Ext).
- *Outcome:* the framework changed. *Mechanism:* each old no-go used far-away competitors: the ideals D_i, face gambles, and contradictory models.

**2. Domain Closure and Extendability (12 Oct).** PROVED, author-checked.
- (SC) together with closure in measure is equivalent to an advice-range description, i.e. a decomposable domain.
- (Ext) is automatic on decomposable domains, so it adds nothing.
- Without (LF) there is a cheap cover: evaluate only the subsets of U = {P̲_K > 0} with the standard penalties. Every axiom plus (Ext) holds, and the target is Bayes.
- *Mechanism:* (LF) is the only condition that forces borderline competitors into the domain.

**3. R1–R9, two-world rigidity (assessed 12 Oct).** PROVED for two worlds, for sandwiched rankings and two-level lexicographic rankings. These reproduce only additive undominated families.
- *Mechanism:* closed choice makes the non-ideal levels countable, while convexity makes them open, so there are none.
- Two side counterexamples:
  - Bayes uniqueness is not selection uniqueness: C_t = B_{t²} also satisfies (S).
  - An error-only primary is compatible with every axiom.
- The prescribed contamination family (1−ε)σ(q) + εΔ is excluded, but only that parametrisation.

**4. R10–R13 and CCIBU (13 Oct).**
- Vertex anchoring (PROVED): with strict guidance, (LF) forces each vertex model to contain e_i.
- No plateau (PROVED): T1 cannot be Bayes on an open set of weights.
- **CCIBU (PROVED, n = 3):** if every interior weighted objective has a unique coherent minimiser, then (LA), (S) and (C) hold. The selection minimises Q_p(x) = Σ p_i(x_i − a_i)², so it is not Bayes at its own index.

**5. T1 for additive rankings (13–14 Oct).** PROVED, refereed.
- Main theorem: on the U-domain and non-adjacent domains.
- **Theorem gm:** on every (LF) decomposable domain, by three independent routes.
- *Mechanism:*
  - Additivity together with (S) and (C) forces a unique, coherent, Hausdorff-continuous interior Bayes family K_q through T1, with **half-plane charts**: {q : g ∈ B_q} = {q : q·c(g) > 0}.
  - At T1's corners the facet data must satisfy x + 1/x = κ + 1 with κ = (1+2ε)/(1−ε), so x ≠ 1.
  - The edges and vertex pinning force diagonal-projective facet maps, which need x = 1.
  - Hexagons and 9-gons near T1 are coverable, so the obstruction is the corner geometry of triangles.

**6. Permitted negligible-stakes ties (13–14 Oct).** FAILS. The theorem survives small-stakes ties: for every band width in the sup norm, and up to a threshold in the Euclidean norm.

**7. "Adds up" and coherent almost-preferences (14–15 Oct).** FAILS for T1 on M_U, later extended (Q4.2) to all (LF) domains.
- *Mechanism:* a supporting additive assessment inherits (S) and (C) at almost every weight. The exceptional weights lie on chords, and the corner argument survives them.

**8. D2 (15 Oct).** PROVED: the first full two-world system with a world that does not add up. It works on M_U.
- *Construction:* a tail-dominance cone along a one-dimensional coherent chain, plus thin "generator" trades whose targets are finite projective-plane lines that overlap near the end of the chain.
- Audit Theorem 4 (PROVED): no locally integrable endorser exists, which refutes Conjecture σB. D2 still has a σ-finite endorser 1/(1−x).
- Reservoir localisation (PROVED): the targets can sit anywhere, including away from coordinate planes.

**9. Fixed-point reduction (L4, R21) and VB (15–16 Oct).** PROVED (refereed once).
- The Hahn–Banach endorsers of any cover form an undefeated field. A cover therefore needs **blind sets**: some world gives zero ordinary weight to a non-null region.
- **VB (the veto–Brier rankings)** satisfies every axiom except closed sections at boundary priors. "Vetoes cannot be paid" (L3.4) shows that this failure is forced.
- Every known construction uses the D2 recipe: one-dimensional chains, nested error sets, and two worlds.

**10. Splicing at a pair-indexed weighting (16 Oct, author's proposal).**
- *Construction:* replace the common advice of D and D′ by C_p, where p is chosen from their disagreement vector, then apply a base ranking.
- *Outcome:*
  - PROVED: (G) and (IB) hold for any base satisfying (G).
  - FAILS transitivity: with the homothetic ordinal base there is a strict three-cycle in two worlds. The cycle arises because different pairs are evaluated in different contexts.
  - Both intersection repairs FAIL (S). Closing under substitution collapses the ranking to the background order. Intersecting over contexts that include the vertex contexts kills competitiveness.

**11. Intersections of additive rankings (16 Oct).** FAILS, PROVED.
- A countable dense mixture ψ = Σ w_k L^k carries every strict comparison of the intersection. So ψ covers whatever the intersection covers, contradicting gm.
- *Scope:* countably additive integral families only.

**12. Transition-record programme (16 Oct).** PROVED.
- On the full domain, preorders with (G) and (IB) are exactly the sets of advice-change records that contain guidance, are closed under *realisable* composition, and contain no reversed guidance.
- Conic closure is **not** implied.
- A capacity score is shown to violate (IB).

**13. X1–X3 (16 Oct).** PROVED: distinct interior posterior selections differ **nonlocally**, on strips approaching the coordinate planes.
- Consequence: a model can differ locally from at most one C_p.
- So bounded-support ("local") rules cannot connect the selected models.

**14. Y1–Y3 (17 Oct).**
- Y3 protects T1 and a vertex neighbourhood, but T1 is isolated in its parameter domain.
- Splice cancellation (PROVED): two disjoint strict worsenings cannot cancel, and retained strict primaries force ties.
- Benchmark: a constant selection T1 on an interior patch is trivial. Interior milestones are therefore worthless without a connection to the boundary.

**15. Additive posterior loop (17 Oct).** PROVED, author-checked.
- The posterior family is the a.e.-unique Bayes model of one additive field on the loop [u,e1] ∪ [e1,e2] ∪ [e2,u].
- Z1.8 excludes the full three-arm star plus an edge.
- *Mechanism:* along one-dimensional paths any interval chart is a half-plane. The contradiction needs two dimensions.

**16. AA, BB (17 Oct).**
- AA2 (PROVED): an upper-hemicontinuous Bayes-weight covering argument blocks filling in prescribed boundary data while keeping an additive primary's strict comparisons.
- Audit examples:
  - a lexicographic cone has no bounded endorser;
  - a fully additive three-world system has no continuous endorser.
- So "no continuous density" is not evidence of non-additivity.
- Radial conjugacy invariance (PROVED): any measurable bijection T(g) = s(g)g with s > 0 preserves every axiom and every coherent model.

**17. CC: synchronized seeds (17 Oct).**
- CC1 (CHECKED): four comparisons out of coherent bases, T1 among them, whose records sum to a strict improvement, yet whose actual compositions are blocked.
- CC1's shrinking argument shows that small competitors evade fixed-size seeds.
- Audit fix (PROVED): couple seven regions into bundles and accept a bundle record d when d ≥ 0 or d ≥ g_k.
  - This gives a preorder with strict (G), (IB) and a closed graph.
  - It has finite non-endorsement certificates at every scale, with undominated coherent bases.
  - **There is no (S).**
- Bundle-wise unanimity gives a veto failure: the regions need compensation between them.
- Finite-image selections force all values to be tied. So jumps are not a cheap escape.

**18. DD/EE/FF: threshold sections (17–18 Oct).**
- Ansatz: C_p ⪯_i X iff p_i ≥ r_i(X).
- Exact budgets Σ r_i = 1 FAIL: the all-contradictory model Z forces r(Z) = 0.
- Strict slack (Σ r_i < 1 off the selected family) is PROVED sufficient: it makes the undominated set equal to the selected family and gives every other axiom.
- EE: imposed ties C_p ~_i C_q (when p_i = q_i) need a tie-certificate test.
- FF1 (PROVED, refereed in GG3): the plain posterior family passes that test. The scheme is the order by the upper probability of world i.
- FF1 Prop 8.1: a cover follows if the strict-slack thresholds are *finitely additively separable* world by world. This is OPEN and was never pursued.

**19. GG (18 Oct).** NA-credal representation (PROVED): intersections of additive orders valued in ordered groups are exactly the convex-cone record orders. Conjecture: closed choice forces NA-credal worlds to add up.

**20. Transitivity weakened (18 Oct).** PROVED (HH1): the KKM dominance theorem holds for reflexive relations, with (C) stated directly. Most barriers survive (Q4.2, L4, L3.4).

**21. Rate and protected designs (18 Oct).**
- II1/II2 lifting (PROVED): a weakly guiding additive leading field satisfying (NT) lifts to an FC cover.
- JJ3 with the KK3 domain dichotomy: FAILS for T1 on every (LF) domain.
- *Mechanism:* protection forces interior Bayes models to be unique and coherent, which brings back gm.

**22. Quorum rankings (18–19 Oct; under TC, not FC).**
- *Construction:* 4 additive judges per world, with acceptance by 3 of 4.
- PROVED: (IB), strict (G), no non-identity ties, TC (by vote counting), automatic (C) and admissibility.
- A strict five-cycle shows that no strictly positive weight endorses all of its comparisons, though the cycle's models are arbitrary, not coherent.
- A fixed relative margin FAILS (S) via an essential-range swap.
- The strict-sign lifting lemma (PROVED): (QS) gives a cover with a shrinking margin.
- Two worlds: a full system, precise and then imprecise intervals. PROVED.
- Three worlds: only a single defended model, T1, has been achieved, and it is isolated.
- The blocking-cone collapse (PROVED) kills committee-size escalation.
- The sum-form (SF) question is OPEN.

**23. Mechanism screens (19 Oct).**
- Measure-preserving matching FAILS: ∫rank is an endorser.
- A record capacity FAILS TC (six-cell witness).
- A product or veto of local gadgets FAILS competitiveness (the quantifier swap).

**24. Withdrawal and Five Patches (19 Oct).**
- Withdrawal (PROVED; D2 domain, TC): remove an open, record-defined set of world-2 strict comparisons. World 1 then becomes the *sole* defender on comparisons that no finite charge endorses, at arbitrarily small scales, with (S) intact.
- Five Patches (PROVED): a finite cancellation certificate out of the nested coherent pair [1/4,3/4] ⊃ [2/5,3/5], with sole defence, under TC. It has **no (S)**.

**25. Hurwicz commission–omission penalty (in the slice; date unclear).** PROVED.
- Pen_ω = 2λ∫_D g_ω⁻ + 2μ∫_{G∖D} g_ω⁺.
- The undominated models are exactly the cones of the density-ratio neighbourhoods C_θ = {p : (p_ω/θ_ω)/(p_ω'/θ_ω') ≤ λ/μ}, for any n.
- This is precisely the **rescaled-box** family, i.e. the audit's positive baseline.

---

## 2. Recurring obstructions

- **Half-plane charts (corner rays).** An additive cover forces {q : g ∈ C_q} to be a half-plane for a.e. g (Contamination Triangle, Prop. reduction (e)).
  - *My inference, not stated in the documents:* for the rescaled family, {p : g ∈ D_{K_p}} = ⋂_v {p : p·(v∗g) > 0}, one half-plane per vertex v of K.
  - For a box the minimising vertex is chosen coordinatewise by sign(g_i), so the chart is one half-plane (the Hurwicz result).
  - For T1 it is a wedge wherever the minimising vertex switches with p, i.e. near corner rays. This is the structural reason the Round 82 family cannot satisfy (IB) additively.
  - Confidence: high, from the cited Proposition and Z-loop.
- **Corner equation versus projectivity** (gm, all three routes). x + 1/x = κ + 1 is incompatible with the diagonal maps that edge pinning forces.
- **Endorsement reduction (fixed point).** Any world that adds up hands the problem back to an additive field (L4, Q4.2, M0closed). Non-additivity must sit on *relevant* comparisons out of coherent undominated models. Comparisons among arbitrary models do not count (quorum five-cycle, LL3 limits).
- **Nesting versus crossing.** Every positive construction (D2, P1, T2n, withdrawal, two-world quorum) relies on a one-dimensional chain or comonotone family. In three worlds, interior selected models' error sets cross. Every attempt broke on comparisons *out of interior selected models* (Exploration Map §3.2; X2 lemma; LL3 B0: pointwise-ordered bases give no finite certificate).
- **Closed sections at the boundary.** VB and "vetoes cannot be paid"; AA2's filling obstruction; a fixed quorum margin (the swap lemma); bundle unanimity (veto). The common shape: a defence must persist to the limit index, but the local defender changes.
- **Product versus compensation (quantifier swap).** "Each region has a defender" does not give "one world defends the whole rival" (Matching audit §2; CC §3).
- **Protection returns to additivity.** Protected leading fields, retained strict primaries (Y Prop. 4) and intersections all carry strict comparisons into a single additive ψ, and gm then applies.
- **Isolation.** Y3, the T1-only quorum certificate and the min-cell class all reach T1 *alone*, in locally isolated designs.
- **Blocking-cone collapse.** Quorum blocking cones meeting in common points force proportional judges, whatever the committee size.

---

## 3. Positive mechanisms that worked, with exact scope

- **CCIBU:** n = 3, integrable strictly guiding additive penalties, full measurable domains; selection by quadratic distance.
- **Rescaled boxes (Hurwicz):** any n, full domain, additive, fixed ratio bound λ/μ. Undominated set equals the density-ratio neighbourhoods exactly. Does not reach triangles.
- **Gauge-mixture polygons** (hexagons, 9-gons) arbitrarily close to T1: additive. Approximate coverage only.
- **D2 family:** two worlds, U-domain, transitive, non-additive, but σ-finitely endorsed.
- **Two-world quorum systems** (TC, full domain): every precise target, and any interval [a,b] via periodic judges. Non-endorsement is shown only among arbitrary models.
- **Withdrawal lemma:** deleting a record-invariant, relatively open set of strict comparisons, each still defended elsewhere, preserves (G), (IB), TC, (S) and (C). This is a general tool.
- **Strict-sign lifting lemma:** turns sign conditions (QS) into closed sections automatically.
- **Strict-slack threshold lemmas:** reduce a full cover to the existence of thresholds r with closed caps. FF1 shows the selected layer is clean for the posterior family.
- **Synchronized seeds and Five Patches:** finite non-endorsement out of coherent undominated bases at every scale, with (G), (IB) and TC. No (S).
- **Domain theory:** Ext is automatic on decomposable domains; the KK3 dichotomy: precise vertices with (Av), or one-sided.

---

## 4. Assumptions dropped or changed, and why

- **All-model domains** were dropped on 12 Oct for decomposable domains with (LF) at the target only. They had been imported silently into every no-go.
  - In hindsight it bought nothing: gm and Q4.2 hold on every (LF) domain, and KK3 closes the domain loophole for protected designs.
  - The current audit has restored the full domain.
- **(Ext)** was not adopted, because it is automatic on decomposable domains.
- **The conic neighbourhood in (LF)** was found to be imported (14 Oct). Repairable; the U-domain is unaffected.
- **Bayes-at-own-index selection** was explicitly never used (Addendum B1), and reindexing is kept.
- **Exact threshold budgets** were withdrawn: they contradict guidance.
- **σB** (local integrability of endorsers) was refuted.
- **Continuous-endorser milestones** were rejected: they are coordinate-dependent and met by additive systems.
- **Transitivity was weakened to FC, then TC** (18 Oct), because composition closure was generating the forbidden comparisons. Dominance survives. TC admits strict four- and five-cycles.
- **(C)** is now stated directly, not through quotients by profile.
- **The fixed quorum margin** was replaced by a shrinking margin. **Committee escalation** was retired.
- **Posterior family, coordinate thresholds, seeds, symmetry:** demoted from requirements to candidate choices.

---

## 5. Top five lessons

1. **High confidence. Under (IB), the full domain and strict world-wise guidance, any construction whose strict comparisons are carried by a single additive score fails for T1.** The mechanism is half-plane charts against T1's corners.
   - This covers additive rankings, intersections, protected leading fields and worlds that add up.
   - Round 82's independence failure is this obstruction surfacing.
   - Any IB-preserving repair of the cover loss must be genuinely non-additive on *relevant* comparisons near T1's corner rays.
2. **High confidence. The decisive difficulty is crossing, not locality or regularity.** Every success is one-dimensional or comonotone. The missing tool is a way to rank comparisons out of interior selected models whose error sets cross, with closed sections and compensation across regions.
   - New proposals should be tested first on a nested coherent pair in two worlds, then on a two-dimensional patch. One-dimensional paths and isolated points prove nothing (loop theorem, constant-T1 benchmark).
3. **Medium-high confidence. Finite non-additive gadgets are easy; (S) is the whole problem.** Seeds, Five Patches and quorum cycles all exist with (G), (IB) and TC. None comes with a global competitive closed selection.
   - Report progress only against (S) with all measurable rivals.
   - Before investing in a candidate rule, screen it for an additive endorser (∫rank, the dual of a matching rule).
4. **Medium confidence. Splice closure and non-tangency did their job conceptually but were a detour.** (LF) blocks only the cheap U = int D cover. Domain restriction never rescued an additive or adds-up route.
   - Now that the full domain is mandated, the domain-specific results (U-domain, non-adjacency, (Av)) are mostly irrelevant.
   - Two things carry over: the transition-record calculus and the withdrawal lemma.
5. **Medium confidence. Dropping transitivity to TC is the only change that produced full non-additive systems with (S)** (two-world quorum, withdrawal). It does so at the price of cycles.
   - Whether TC is acceptable is a normative choice the author must make explicitly.
   - If TC is not acceptable, the open target is FF1 Prop 8.1 (finitely separable strict-slack thresholds), which keeps transitivity.

---

## 6. Leads: dropped too early or never tested

- **FF1 Prop 8.1 (strongest lead).** Construct strict-slack thresholds r for the plain posterior family whose world-wise comparisons are finitely additively separable, with witnesses varying with the finite set. This yields a full transitive cover of T1 of type (M2).
  - It was named "the single most important open point" on 17 Oct and then abandoned for rate and quorum designs.
  - It is the (IB)-respecting form of a threshold "cover loss", so it is directly related to Round 82.
- **Pair-indexed splicing under TC.** It gives (G) and (IB) for *any* (G)-base, which is exactly the property Round 82's cover loss lacks.
  - It was rejected for transitivity before the TC weakening. It was never re-tested for TC, closed sections or competitiveness.
  - Cheap test: apply it to the Round 82 cover loss as the base.
- **Sum-form (SF) quorum data of rank ≥ 3** and smooth flat judges. These are explicitly not excluded (Quorum §§9–10). Conjecture NN2 is unproved either way.
- **Synchronized seeds plus compensation between bundles** (CC §5). The proposed extension lemma was never attempted; the work moved to thresholds.
- **Withdrawal on the full domain, with a nested pair.** Extend the withdrawal construction beyond the one-sided domain. Combine it with the Five Patches source relations to obtain a finite certificate together with (S) in two worlds.
- **Varying λ in the Hurwicz penalty per region** or per world, combined with non-additive aggregation. The box baseline is understood exactly; nobody has tested a ranking that is Hurwicz on box-like gambles and non-additive only on the corner-ray wedges identified in Lesson 1.
- **Conjecture GG (does closed choice force NA-credal worlds to add up?).** Open. A proof would make finite-cancellation failure necessary. A counterexample (D2's hull with its sections closed) would be the next construction.
