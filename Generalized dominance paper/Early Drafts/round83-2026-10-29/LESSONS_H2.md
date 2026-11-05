# LESSONS_H2: 9–12 October 2026, when independence (IB) was introduced

Reader H2. **Access note.** I had no Projects tool in this session. I read the project documents from their device copies in `~/mnt/Generalized dominance paper/Early Drafts/`, which have the same titles and Oct 9–12 timestamps, together with all the listed `~/mnt/CPMs/outputs/` folders. I read the short notes in full: v3, BA, CC, CBOI, VTTC, CANA, OB and the status and review .md files. For the long notes I read the summaries, all the theorem statements and the key proofs: TAW is 168 KB, FSE 145 KB, *Incomplete Rankings and Coverage* (IRC) 205 KB and *P1 Status Round 5* 196 KB. I did not audit those four line by line.

---

## 0. Which independence was used? This matters for the current audit

**Throughout 9–12 Oct, IB was the symmetric-pair version.** v3 (§1) states it as follows. For measurable A = −A and F, G ⊆ Aᶜ,
(X∩A)∪F ⪯ᵢ (Y∩A)∪F ⇔ (X∩A)∪G ⪯ᵢ (Y∩A)∪G.
The stated reason is "the symmetry of A keeps the two orientations of each binary problem together." All later notes work on H = {g₁>0} and change advice on ±Q, which is the same condition.

**This is not the audit's IB.** The audit allows an arbitrary measurable D. The difference is forced by the background order:
- From v3 onward, (G) used the **four-rank advice order** on pairs: good ≺ silence ≺ bad ≺ contradictory. v3 notes that under this order, *removing* the correct half of a contradictory pair is an improvement.
- Under arbitrary-D independence, take D to be the single orientation g. Adding g when −g is absent turns silence into good, which is better. Adding g when −g is present turns bad into contradictory, which is worse. The comparison flips. So **the four-rank order with strict (G) is incompatible with the audit's arbitrary-D IB.**
- The audit's error-set order E_ω(X) = X Δ {g: g(ω)>0} is the gamble-level order that arbitrary-D IB fits.

**Consequences.**
1. *Impossibility results transfer, with one check.* Arbitrary-D IB implies the symmetric version. On **regular models** (never contradictory, correct on unanimous problems), the four-rank order and the error-inclusion order agree (v3 §1). The impossibility proofs in this slice use (G) only through regular models, as far as I could see. So they should transfer to the audit's setting. This needs an explicit check that no proof uses the four-rank (G) on contradictory models. The completeness hypotheses also need a check, because "complete on all models" means different things under the two orders.
2. *A sharper structure under the audit's IB (my observation; confidence moderate to high).* Each model corresponds one-to-one to its error set at world i. The audit's IB then says that E ⪯ᵢ E′ depends only on E∖E′ and E′∖E, whatever the common part. With (G), ⪯ᵢ is a **strictly monotone, possibly incomplete de Finetti comparative probability on the measure algebra of error sets.** It has one layer.
   - The 9–12 Oct notes needed two layers ("debt" and "credit") and an exchange rate κ between them (CCF Theorem 15). The audit's framework removes that layer.
   - This makes the CCF route more direct: completeness plus fineness gives, by Savage–Wakker, an almost-agreeing finitely additive score ν_i(E_i(X)). The CBOI obstruction then applies.
3. *Positive constructions must be re-checked.* v3's two-world tables give contradiction the cost 2·(bad), which is not gamble-additive. The gamble-additive form gives contradiction (bad) − (silence). I checked v3's two-world table in that form. Accepting g and accepting −g are never both Bayes-optimal, because that would need c > ab/(a+b), while c_w ≤ ab/(a+b). So **v3's two-world full coverage appears to survive in the audit's setting.** Confidence moderate; this needs writing out.
   - The audit's "box-weight" baseline s_i = ∫_X ψ_i dμ is exactly the gamble-additive form of CANA eqs. (3)–(4). Its condition λ_i ≤ η_i is precisely the condition that rules out Bayes-optimal contradictions.

---

## 1. Chronological list of attempts

Abbreviations follow the notes.

**1. v3, *Independent Rankings of Binary Advice* (9 Oct; device: independent-guidance-v3, independence-general-n).**
- *Aim:* restore IB, which v2's benchmark recipe lacked, while keeping full coverage.
- *Axioms:* strict (G) in the four-rank order; symmetric IB; (E), (LA), (A), (S) with closed sections {p: C_p ⪯ᵢ X}; (C).
- *Construction:* additive local penalties ℓ_i(g, a), with good < silence < bad < contradiction, integrated over H. If pointwise Bayes advice is unique and coherent at every p, all the axioms follow (Thm 4).
  - Two worlds: silence cost c_w = ab/((1+w)(a+b)) yields intervals of width w.
- *Outcome:*
  - **PROVED:** v2's ordinal recipe fails IB (Prop 1: "a common change can erase a comparison").
  - **PROVED:** full two-world coverage, including boundary intervals and V.
  - **PROVED** for n ≥ 3: no additive ranking with (LA) and (S) leaves any target with three vertices undominated (Thm 8, App. C).
  - **PROVED:** a positive result in every dimension for precise models.
- *Mechanism:*
  - Prop 1: a whole-model rule (benchmark or default comparison) can be switched by adding shared advice, for example contradictions on the unanimous cone. **This is the same failure mode as Round 82's cover loss.**
  - Obstruction: (LA) and (S), through KKM, give coherent Bayes models at every prior. An undominated target is Bayes somewhere, by separating hyperplanes.
  - A three-vertex target forces each edge face to be vacuous. That bounds the edge contrast ratio ψ_i/(−ψ_j) by p_j/p_i.
  - But coherence of Bayes models across a third payoff sign forces that ratio F_ij(g_i/−g_j) to be unbounded (the three-world compatibility lemma).
  - Remark 2: a fixed additive penalty cannot realise the homothetic K_p, because "+ uniquely Bayes at p and at q implies the same at (p+q)/2."

**2. BA, *Beyond Additive Guidance Rankings* (9 Oct).**
- *Aim:* escape additivity with incomplete or non-additive rankings.
- *Outcome:*
  - **PROVED:** intersections of additive rankings, even infinitely many, have an additive weak extension, so the v3 obstruction applies (Thm 3, Cor 4).
  - **PROVED:** a genuinely non-additive (G)+(IB) ranking covers every coherent model at once. It is built from a 6-region lift of a finite comparative order with no additive representation (KPS-type). It fails (S).
  - **PROVED:** finite-sample rankings make only the ideals D_i competitive, so (S) fails because the simplex is connected.
  - **PROVED:** lexicographic "bad advice first" rankings have coherent Bayes models at every prior but no (S) selection.
- *Mechanism:* (S) needs comparisons dense enough that a coherent model is weakly better than every rival at some supported world. Sparse orders lose competitiveness; additive certificates bring back the obstruction.

**3. CC, *Closed Choice for Independent Rankings* (9 Oct).**
- *Outcome:*
  - **PROVED:** the obstruction needs an additive weak extension only on regular models.
  - **PROVED:** complete, measure-continuous rankings on regular models, or intersections of them, have such an extension (Debreu-type), so V is dominated.
  - **PROVED,** structural consequences of (S), using strict (G):
    - face lemma: if C is competitive on S, its credal set lies in Δ_S;
    - C_{e_i} = D_i;
    - uncountably many tie classes along every edge;
    - V can be tied only with full-support selections.
  - **Conjecture:** no (G)+(IB)+(LA)+(S) ranking leaves V undominated for n ≥ 3.
- *Mechanism:* strict (G) plus competitiveness pins vertex and edge selections. Closed sections plus connectedness force continuum-many edge selections.

**4. CBOI, *Closed Choice Beyond Ordinary Integrals* (9 Oct).**
- *Outcome:*
  - **PROVED:** a strictly positive *finitely additive* weak extension on regular models still dominates every three-vertex target (Thm 2). Incompleteness is allowed.
  - **PROVED:** (S) does *not* force an ordinary additive extension. There is a complete counterexample with a pure-charge term and C_p precise.
  - **PROVED:** a primary that is blind on arbitrarily small sets is constant along edges.
- *Mechanism:* finitely additive charges keep the Bayes, KKM and separation machinery. IB gives cancellation but not the finite-cancellation conditions an additive extension needs.

**5. EDL, *Edge Dichotomy and Leverage* (9 Oct).**
- *Outcome:*
  - **PROVED:** only a *one-sided* extension is needed, for comparisons from a coherent undominated model to a regular model (Prop 1).
  - The extension exists if and only if there is no "leverage sequence" (Thm 2, later identified as Berti–Pratelli–Rigo).
  - An additive primary is either strict or blind on mixed problems, so lexicographic additive hierarchies fail.
  - Two additive worlds force the meeting face to be vacuous.
  - **UNCLEAR:** Thm 2 and Cor 20 had no independent check at the time.

**6. FAED, *Finitely Additive Edge Dichotomy* (10 Oct).**
- **PROVED:** the finitely additive version of EDL's dichotomy. No IB is used.

**7. IC, *Independence Chains* (10 Oct).** The first essential use of IB.
- *Chain lemma:* competitiveness of V and of an edge model C gives two accepted changes. IB transports a change accepted in one context to another context with the same advice on the change set. Transitivity then reverses strict (G) at world 1.
- **PROVED:** with two additive worlds, or with path-closedness, every edge selection at e₁ contains an endpoint (the endpoint property, EP).
- **PROVED:** V is dominated under several conditions on the additive worlds: flat thresholds, homogeneous penalties, constant ρ.
- **OPEN:** a residual configuration.

**8. DT, *Dense Thresholds and Debt Reduction* (10 Oct).**
- **PROVED,** with a correction: thresholds of useful selections are dense; F and G jump in every interval; a strip bound on c₃/c₂ suffices for domination.
- CCF's referee found an invalid reservoir placement in the original proof. It was repaired; the repair is author-checked only.

**9. ECS, *Edge Cycles and Separability* (10 Oct).**
- **PROVED:** an undominated V forces separable ratios ρ = f(t₁₂)/h(t₁₃) on P₁. No completeness is used.
- The converse, passing edge-cycle tests, does *not* give (S).

**10. CCF, *Closed Choice Forces Fineness* (10 Oct).**
- *Idea:* by IB, a world's comparisons of pure debt sets (and separately of pure credit sets) are de Finetti comparative probabilities. Closed sections at edge selections with EP make them **fine**. Savage–Wakker gives almost-agreeing finitely additive probabilities. One exchange rate κ combines them into a CBOI-type extension.
- **PROVED:**
  - two worlds with finitely additive one-sided extensions plus a complete IB third world dominate V (Thm 18);
  - with all rankings complete and EP on every edge, every three-vertex target is dominated (Thm 16).
- *Corollary:* a counterexample needs an edge selection omitting both endpoints.

**11. TAW, *Two Additive Worlds Without Completeness* (11 Oct).**
- **PROVED:** n = 3; two worlds with finitely additive one-sided extensions (W); a third world that is any IB preorder. Then V is dominated, and no completeness is used anywhere.
- *Mechanism:*
  - "Routing primaries" derive additive comparisons of debt sets from moves at edge selections.
  - A "silent target" (a non-coherent Bayes model at a jump corner) has a KKM dominator, which yields a forbidden debt–credit trade.
  - Closedness at the other world of an edge kills pure-charge germs.

**12. FSE, *Fineness Spreads Along Edges* (11 Oct), and P1 Status Round 5.**
- **PROVED** (complete rankings, n = 3):
  - one fine world implies all worlds fine, so V is dominated;
  - a fine edge suffices; one "tame" world suffices;
  - low-cone heaviness (LH)/(DH) holds at every world;
  - fineness does not follow from completeness + (G) + IB.
- **OPEN** at the time: P1, whether V is dominated for complete rankings.
- P1 Round 5 gave conditional attacks ending in a "race of lightness rates". These are superseded.

**13. FFNW, *Fineness for Any Finite Number of Worlds*, and IRWAS, *Independent Rankings Without Additive Structure* (11 Oct).**
- FFNW: **PROVED** for n ≥ 3 that one fine world implies all fine, using the regions O_v where one world disagrees with all the others.
- IRWAS: **PROVED** that a single-world complete strict-(G)+IB order exists with no group-valued primary and no local finitely additive extension, satisfying (LH)/(DH). No (S) is constructed. It is a KPS order lifted by ultrafilters.
- *Mechanism:* IB alone does not give additivity. Anything further must come from (S).

**14. TCR, *Three Complete Rankings Cannot Cover* (11 Oct).**
- **PROVED:** n = 3, complete preorders with (G) and IB, plus (S), make V dominated.
- *Mechanism:*
  - "No saturated cut": (S) and completeness give a finite chain from D_v to D_w of descents and perturbations on any band-dense family. IB is not needed for this step.
  - Counting lemma, which uses only weak (G), IB and transitivity: a chain of length ℓ admits at most ℓ disjoint heavy sets.
  - Uncountably many heavy ultrafilters (from FSE) contradict finitely many per level.
- *Corollary:* full coverage under strict (G) + IB + (S) **requires incomplete rankings.**

**15. CRAN, *Complete Rankings for Any Number of Worlds* (11 Oct).**
- **PROVED:** the same result for every n ≥ 3. The device is the regions O_v, where one world disagrees with all the others: changes there improve every world outside the active triple.
- **Clique theorem, PROVED but conditional:** if D_K with ≥ 3 vertices is undominated, the edges among K's vertices have EP and are fine, and some other edge lacks EP.
- **OPEN:** universal domination of proper three-vertex targets for n ≥ 4, for example conv{e₁,e₂,e₃} in Δ₄.
- *Why the gap:* the dominance arguments need a base model that is silent on the regions they change. A target omitting e_x gives bad-at-x advice on O_x.

**16. IRC, *Incomplete Rankings and Coverage* (11 Oct).**
- **PROVED:**
  - one (W)-world plus one complete world dominates V;
  - if V is undominated, each (W)-world forces both other worlds to be incomplete;
  - Theorems A/B: under a pointwise edge-openness condition T1o, an undominated V forces EP on every edge and fineness everywhere, and at most one incomplete world makes V dominated;
  - (S) does not imply T1o (the Conf(θ) example);
  - finite cancellation (NC) characterises a full weak extension at fine worlds.
- **OPEN:** three residual alternatives (R-a1, R-a2″, R-b′). The key question is whether fine IB worlds can violate (NC).

**17. VTTC, *Vacuous Targets and Transfinite Construction* (12 Oct).**
- **PROVED:** without (S), V can be the unique minimiser of strict additive rankings (silence cost c < 1/n).
- **PROVED:** tying good with silence on mixed problems gives complete IB rankings with constant selection C_p = V. This is the "neutral abstention" exception, and it breaks strict (G).
- **PROVED:** increasing unions preserve (G), IB and a protected target, but not closed sections. Permanent open forbidden neighbourhoods would suffice. The extension lemma is **OPEN**.

**18. CANA, *Coverage after Neutral Abstention*, and OB, *Omission Blindness and Four Rank Guidance* (12 Oct).**
- *Decision:* accept the V exception, limited to V.
- **PROVED:** strict, complete, additive two-slope losses cover the normalised boxes K_{p,ε} = {p∗a/(p·a): a ∈ [ε,1]ⁿ}, and more generally boxes with bounds 0 < λ_i ≤ η_i. As ε → 0 they converge uniformly to the exception.
- **PROVED:** an exact consistency test. Given a family and closed sections, the least closure under four rules (reflexivity, transitivity, IB transfer, undominatedness) succeeds if and only if no forbidden outcome is derived. Finitely many stages suffice. It does not show that suitable sections exist.
- OB, **PROVED:** omission-blind write-in losses give full coverage, but their guidance weakening depends on the target. **Rejected** for that reason.

**19. CSE, *Conditional Shunning of Error* (12 Oct).**
- *Construction:* systems Σ_T weaken (G) at the worlds in T.
- **PROVED:**
  - the systems cover normalised boxes with vanishing lower bounds, faces, V, all two-world targets, and some proper three-vertex targets;
  - they do *not* cover ε-contamination classes, segments from an interior point to a vertex, or conv(Δ₁₂₃ ∪ {p}) in n = 4;
  - a three-vertex target needs |E∖T| ≤ 1;
  - Bayes selections fail (S) when n ≥ 3 and ∅ ≠ T ≠ Ω.

---

## 2. Recurring obstructions

1. **Model-wide rules fail IB** (v3 Prop 1; Round 82).
   - Any comparison whose rule depends on a global property of the models, such as which benchmark applies, whether a cover exists, or a default comparison, can be switched by changing shared advice elsewhere.
   - The v3 witness adds a common block of contradictions on the unanimous cones.
   - Round 82 is a recurrence of this pattern, not a new one.
2. **Coherent Bayes at every prior** (v3 Lemma 9a; CC; CBOI; CCF Lemma 1).
   - Whenever a world has even a one-sided, finitely additive, strictly positive extension, (LA) and (S) give, via KKM, coherent minimisers at every prior.
   - Combined with three-world compatibility (edge ratios must be unbounded, yet a three-vertex target bounds them by p_j/p_i), **every target with three vertices is dominated.**
   - This is the central additive obstruction. It survives incompleteness, intersections, finite additivity and lexicographic hierarchies.
3. **Face lemma and edge pinning** (CC Lemma 7, Cor 8).
   - Strict (G) plus competitiveness on S forces the credal set into Δ_S, and C_{e_i} = D_i.
   - Connectedness of an edge plus closed sections then forces continuum-many edge selections.
   - This is what drives every edge argument, and it disappears once (G) is weakened (VTTC remark).
4. **Closed choice forces fineness** (CCF Thm 13; FSE; FFNW).
   - IB makes debt and credit orders comparative probabilities. (S) sections at EP edges give fineness, then Savage–Wakker gives an extension, then obstruction 2 applies.
   - Fineness spreads: one fine world makes every world fine.
5. **Endpoint property and its failure** (IC, CCF, FSE, CRAN).
   - A counterexample needs a two-sided edge selection, with neither endpoint in its credal set.
   - EP holds next to any (W)-world. CRAN's endpoint dichotomy says either all edges among S(K) have EP or none do.
6. **Chains plus IB plus transitivity** (IC chain lemma; TCR counting lemma).
   - Comparisons forced by competitiveness compose in context and reverse strict (G).
   - This is the main way IB acts as an obstruction rather than as cancellation.
7. **Closed sections are not preserved under limits** (VTTC; CANA).
   - ∪[0, 1−1/m] = [0, 1). Transfinite and ordinal constructions stall exactly here.
8. **Sparse orders lose competitiveness** (BA finite-sample, lexicographic, blind primaries).
   - If an order is too incomplete, no coherent model is competitive. Incomparabilities must be placed very precisely.
9. **Vacuous-target tension.**
   - Under strict guidance, protecting V requires every pair of worlds to be in silent balance on mixed problems. This conflicts with the strict edge orders that (S) forces near the vertices.
   - The tension was resolved only by tying good advice with silence, which the audit now forbids.

---

## 3. Positive mechanisms that worked, and their exact scope

- **Pointwise-unique Bayes with additive local penalties** (v3 Thm 4): this gives (G), IB, (S), (C) and (LA) at once.
  - Scope: two worlds, all credal intervals; any n, precise models and normalised boxes with 0 < λ_i ≤ η_i (CANA eqs. 3–4).
  - The box family is exactly the "rescaled" form p∗a/(p·a).
- **Splitting by sign pattern:** boxes work because the minimiser over M of m·(p∗g) depends only on the sign pattern of g, not on p.
  - This is my reading of why boxes, and only boxes, come out of the K_p = p∗M ansatz with additive scores.
  - With additive scores, each action's Bayes region in p at fixed g is an intersection of at most two halfspaces. For p∗M it is an intersection over the vertices of M.
  - Confidence moderate. It explains Round 82's failure: non-box M forces a non-additive and hence non-IB rule.
- **Weakened guidance (Σ_T, neutral abstention):** covers faces, V, boxes with zero lower bounds and some three-vertex targets. It requires indifference between good advice and silence at some worlds, which the audit does not allow.
- **Omission blindness:** full coverage, but the weakening depends on the target.
- **Dropping (S):** full coverage by a single genuine non-additive IB ranking (BA). Dropping IB: v2. The two hard constraints really are (S) and IB together.
- **The exact consistency test** (CANA Thm 2) reduces ordinal construction to choosing a family and closed sections. It is a correct and useful reduction, but not a construction.

---

## 4. Assumptions dropped or changed

- **Background order** (v3, 9 Oct): the error-inclusion order was replaced by the four-rank order, because the error order treats contradictions oddly in Prop 1.
  - The audit has since **reverted** to error sets. The two orders agree on regular models.
- **IB:** introduced on 9 Oct in its symmetric-pair form. The audit now uses the arbitrary-D form, which is stronger and gamble-level (§0).
- **Weak extension hypotheses:** weakened step by step. Two-sided ordinary on all models became regular-only (CC), then finitely additive (CBOI), then one-sided from coherent undominated models (EDL), then (W) at only two worlds (TAW).
- **Completeness:** assumed in CCF and FSE, removed in TAW, then shown to be *fatal* in TCR and CRAN: complete rankings cannot protect V.
- **Coverage target:**
  - On 12 Oct full (A) was replaced by "all proper M plus a V-exception system", which ties good with silence on mixed problems.
  - The target-dependent weakening (OB) and conditional shunning (CSE) were explicitly *not* adopted as the standard.
  - **The current audit's strict world-by-world guidance appears to revoke even the V exception.** The lead should confirm this. If so, V is again a required target, and TCR and CRAN then say it cannot be covered by complete rankings.

---

## 5. Top five lessons

1. **Under strict guidance, IB and closed-section (S), complete rankings cannot cover V for any n ≥ 3** (TCR, CRAN; refereed by AI passes, and I found nothing wrong in what I read).
   - Under the current audit (strict guidance, arbitrary-D IB) this should transfer, because the audit's IB is stronger and the proofs use regular models.
   - So either the audit admits incomplete rankings with very finely placed incomparabilities, or it weakens (S) to W1–W3 in a way that breaks the closed-section arguments, or it gives up on V.
   - *Confidence:* high for the theorem; moderate to high for the transfer. The transfer needs a regular-models-only check. I could not assess whether W1–W3 escapes it, because those proofs use the exact sections {p: C_p ⪯ᵢ X}.
2. **Any additive, or even finitely additive, certificate at enough worlds kills every three-vertex target.** Under the audit's IB each world is a comparative probability on error sets, so for complete rankings "fine" means "almost additive."
   - The audit's box baseline is therefore not an arbitrary choice. Up to fineness and pure charges, it is roughly what complete rankings are forced to be.
   - What is left to settle is *which targets additive error scores cover*. v3 explicitly left that unclassified for n ≥ 3.
   - *Confidence:* moderate to high.
3. **Never build a comparison from a whole-model property.** v3 Prop 1 already showed in this slice the IB failure that Round 82 hit again.
   - IB-respecting constructions have to be either local (pointwise penalties) or least closures of explicitly chosen sections (CANA Thm 2).
   - *Confidence:* high.
4. **Coverage in this period always came from Bayes uniqueness, not from ordinal cleverness.** Every positive strict result is a pointwise-unique Bayes family. Every ordinal or incomplete attempt either lost (S) (BA) or was never completed (the transfinite and consistency work).
   - If incomplete rankings are needed (lesson 1), the only tool so far is the exact consistency test. There is no existence theorem.
   - *Confidence:* moderate.
5. **Keep separate the two families of results that are often conflated:** V and three-vertex targets on one side, and proper targets with at most two vertices on the other.
   - For n = 3 the impossibility results exclude only V. No proper target was shown uncoverable under strict (G) + IB + (S).
   - Normalised boxes are covered. ε-contamination classes and segments ending at a vertex are uncovered *by the known families*, but no impossibility was proved for them.
   - *Confidence:* high that this is the state of the record.

---

## 6. Leads: dropped too early or never tested

- **Redo the CCF and TAW route at gamble level.** Under the audit's IB, the debt/credit split and the exchange rate κ disappear: each world is a one-layer comparative probability on error sets. Fineness from (S) might then be provable without EP. It is worth one focused attempt, aiming either for a clean impossibility or for the exact place it fails.
- **Classify the targets covered by additive error scores** s_i = ∫_{E_i(X)} ψ_i dμ with general ψ_i(g), not just |g_i|-proportional box weights.
  - v3's two-world table uses non-homogeneous ψ such as c_w(a,b) and covers boundary intervals that boxes miss.
  - So general ψ covers more than boxes when n = 2. Nobody tested what non-homogeneous ψ buys when n ≥ 3, for example for ε-contamination classes or for targets touching the boundary.
- **Port the two-world full-coverage theorem to the audit setting**, with contradiction cost (bad) − (silence). My quick check says it survives.
- **Use incompleteness only where TCR needs it.** IRC shows that at most one incomplete world, if it satisfies T1s, still forces domination. A construction should therefore try two or three incomplete worlds and use the CANA consistency test on a small, explicitly chosen family, for example homothetic rescalings of V, with candidate closed sections. This was never tried concretely.
- **The n ≥ 4 three-vertex gap** (CRAN Remark "open") and **CSE's covered three-vertex targets** suggest that proper three-vertex targets might be coverable under strict rules in n ≥ 4 by non-additive complete rankings. The clique theorem's necessary conditions (EP and fineness inside K, failure of EP outside it) give a specification to aim at.
- **Weakening (S):** the audit's W1–W3 with a rival-independent assignment b_p was not available in this period. Whether TCR's counting argument needs exact closed sections, or only W1–W3, is the most important untested question for the current audit.
