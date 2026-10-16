# Accuracy rankings: current status and reading guide

Updated 12 October 2026, **after acceptance of the vacuous-target exception**; see the dated section immediately below for the later decisions of 12 October.

This is the current entry point. Earlier notes describe successive versions of the question; their opening claims that “the problem remains open” are not reliable statements of the present status. The original files have been left in place to preserve references.

## Glossary (14 October 2026; corrected after the auditor's remarks)

**Basic setting.**
- *Worlds, gambles.* Three worlds Ω = {1,2,3}; a gamble is a vector g ∈ ℝ³ (its payoff in each world).
- *Binary problem.* The choice represented by a gamble g, which −g represents too, with the options swapped. As bookkeeping only, each such pair {g,−g} is indexed by its member with g₁ > 0; the set of these indices is H, with a Gaussian measure μ. H is the sample space of the accuracy rankings; Ω is the sample space of the gambles.
- *Advice.* On each problem a model accepts g, accepts −g, is silent, or accepts both (contradiction).
- *Model.* A measurable assignment of advice to problems, identified up to μ-null sets. *Coherent model* D_K: accepts g iff m·g > 0 for all m in the credal set K.
- *T1.* D_K for K = (1−ε)u + εΔ, u uniform, 0 < ε < 1.
- *Regular model.* A model that gives the correct advice on unanimous problems (all coordinates of g of one sign).

**Domains.**
- *What a gamble represents.* A gamble f represents the binary choice {f,0}, equivalently the choice {g,h} for any g,h with f = g − h. f and −f represent the same choice with the options swapped. A model D advises choosing g iff f ∈ D and −f ∉ D; choosing h iff −f ∈ D and f ∉ D; it gives no advice iff neither is in D; it gives contradictory advice iff both are.
- *Domain (class of evaluable models).* A ranking's domain is the class of models it evaluates. Restricting the domain means only restricting which models are evaluated. No decision problem is removed, altered or given restricted options, and the world orders still concern every binary problem. Domains are required to be closed under splicing and under convergence in measure (*decomposable domains*).
- *Advice range.* For a decomposable domain, the advice range at f is the set of kinds of advice that evaluable models give on the choice represented by f. Every decomposable domain is exactly the class of models whose advice lies in its advice ranges (Domain Closure and Extendability, Prop. 2).
- *Two-sided domain.* A domain on which, for problems near the target, evaluable models may accept f, accept −f, or give no advice (advice range {+,0,−}).
- *(LF), local freedom at the target.* There is an open set N of gambles containing every nonzero boundary point of the target's cone, such that the domain contains every model differing from the target only on gambles in N.
- *U-domain for T1.* Shrink K towards u: K′ = u + s(K − u), 0 < s < 1. Its cone U = D_{K′} is slightly larger than T1's cone. The evaluable models are exactly the measurable subsets D of U. This is a restriction on the class of evaluable models and nothing more. U never contains both f and −f, so no evaluated model gives contradictory advice.
  - For f ∈ U and any g,h with f = g − h, D advises choosing g in {g,h} iff f ∈ D, and gives no advice otherwise.
  - For −f ∈ U the roles of g and h swap.
  - For f with f ∉ U and −f ∉ U, every evaluated D gives no advice. These problems remain decision problems; they simply do not distinguish evaluable models.
  - Evaluable models are guaranteed to agree on f (all giving no advice) only when f ∉ U and −f ∉ U. It is not enough that f ∉ U: if −f ∈ U, evaluable models differ on f. In particular a pair indexed by its representative g with g₁ > 0 is not outside the domain when −g ∈ U.
- *Non-adjacent (additive rankings).* On problems meeting U, accepting g and accepting −g never compete directly as best advice across a boundary between interior weightings (silence may separate them). This depends on the penalties as well as on the domain; a domain whose evaluable models never accept −f for f near the target is a sufficient special case.

**Rankings and choice.**
- *Ranking.* One preorder per world on the models of the domain. *Competitive on a set S of worlds*: for every model X, some world in S ranks it no worse than X.
- *Weighting.* A probability q on the worlds. *Additive ranking*: world i scores L_i(X) = ∫ ℓ_i(g, advice of X at g) dμ(g). *Bayes model at q*: a minimiser of q₁L₁ + q₂L₂ + q₃L₃.

**On the U-domain.**
- *Error set.* E_i(X) = the gambles h ∈ U with h_i > 0 that X does not accept, together with those with h_i < 0 that X accepts.
- *Relevant comparisons at world i.* Pairs B ⪯_i X with B coherent and undominated and X regular. (Restricting to regular X is essential: a lexicographic priority on unanimous errors can destroy adding-up for unrestricted comparisons without helping coverage; N19 §3.3.)
- *Adding up at world i.* Some finitely additive weight ν on U, zero on null sets and positive on non-null sets, endorses every relevant comparison: ν(E_i(B)) ≤ ν(E_i(X)).
- *Supporting additive assessment.* An integral loss built from such weights. It endorses the relevant comparisons but need not be close to the ranking and can lose distinctions the ranking makes.
- *(M0).* Every world adds up. Then (N13 Prop B, N22 Thm 2.1) the supporting assessment ψ has: the same domain; T1 as Bayes model at an interior weighting; at least one coherent Bayes model at every weighting; a unique coherent Bayes model at almost every interior weighting. At the exceptional weightings coherent and incoherent minimisers coexist; ψ cannot tell them apart, the original ranking may.
- *(M1).* At some world a finite family of relevant comparisons is an obstruction to any positive weighting of errors (a positive combination of their error-difference vectors is ≤ 0 and ≠ 0). It need not be an executable sequence of trades.
- *(M2).* At some world there is no finite obstruction, but still no strictly positive weight endorses all relevant comparisons.
- The M0/M1/M2 division is logical bookkeeping. The substantive result is the reduction behind M0. The four-trade, overlapping-gain and crossing restrictions apply only to M1 certificates in the stated formulation.

**Geometry of T1's cone.**
- *Facet:* gambles with lower prevision 0 under K, attained at one vertex. *Corner ray:* where two facets meet (lower prevision 0 along a whole edge of the triangle). *Crossing:* a facet gamble with one coordinate 0.

**Interpretation of domains (14 October, author's correction).** A domain restriction is only a restriction on the class of evaluable models. Older versions of these notes used the words "menu" and "forced silence"; files and folders whose names used them were renamed on 14 October (e.g. `decomposable-domains-2026-10-12/`). The mathematics is unaffected, because every result compares evaluable models only (checked across the write-up; see "The Contamination Triangle - interpretation changes.md").

## Update, 16 October 2026, early morning (supersedes everything below where it conflicts)

**Round 19 aimed to settle T1 on the U-domain or find a cover. It did neither. It did produce a structural classification that organises everything that remains. All results below are refereed once.**
- **Classification (K3.1).** Suppose a world fails to add up but has no finite certificate. Then it is endorsed exactly off a family of shrinking sets, except on a canonical "blind set" Λ_∞. If Λ_∞ is null, the failure is localizable; "protected ends" add nothing beyond this (K3.2). Closed sections are essential: without them a totally blind world exists (K3.3).
- **Patch theorem (K3.5).** This unifies the earlier exclusions (H1, H2, J1). A localizable failure can carry a cover only through "sheltering" (worlds whose bad regions sit inside each other's protected regions) or through infinite minority mass.
- **Finite certificates (K2).**
  - Such a certificate must contain a rigid comparison that no axiom forces (divisibility theorem K2.1).
  - In two worlds such a world would refute Conjecture Q2N.
  - The natural construction scheme is empty over Brier-type additive bases.
- **Protected ends (K1).** Extended to infinitely many ends. Acyclic conflict and aligned orders are excluded. The remaining question is the class question itself.

**What a cover of T1 on the U-domain must use (one of):**
- a world with a finite certificate built on rigid, unforced comparisons;
- a world with a non-null blind set (Question Q_K3);
- sheltering cycles with no aligned order (Question J1.Q′∞).

## Update, 15 October 2026, late evening (supersedes everything below where it conflicts, including the "evening" update)

**Corrections after the external audit (refereed in F12_referee.md).**
- **E1 was overstated.** Its exclusion (E1.5) covers only covers in which every world is end-protected with integrable base endorsers. It does not show that protection must sit at nearly unanimous problems. Ends need only be places where T1 is correct for the protected world; that holds automatically at ∂U ∩ {h_i < 0} (F2.1–F2.3).
- **B3 was overstated.** Proved: a complete world of a cover that does not add up is not almost representable. "It must be incomplete" would follow from Conjecture B3.C, which is open.
- **Conjecture σB is false (observed by the auditor; proved in F1, F2).** D2's far end includes the ray through (1,0), which is inside U. Every endorser of D2's world 1 puts infinite mass there. The repaired forms (local integrability on the mixed problems only, or densities finite a.e.) are open.
- **D2′ (F1, refereed).** D2 can be rebuilt with every non-additive trade bounded away from zero and protection at ∂U.

**Rounds 17–18 (positive attempts using the lessons).**
- **H1 (refereed once).** One world that fails to add up only on sets of small measure never suffices: with two other worlds adding up integrably, there is no cover.
- **H2 (refereed once).**
  - The exclusion extends to protection anywhere, unless the "conflict digraph" has a cycle: two or more worlds, each with an end where T1 is wrong for it, sheltered by another world's end.
  - A full two-world system in which **neither** world adds up exists (H2.4).
- **J1 (not yet refereed).**
  - Most such cycles are excluded.
  - The one residual configuration is a "doubly misaligned" cycle, in which a cap shrinking to a ray sits inside a tube shrinking to a curve. It is Question J1.Q.

**Status of T1 on the U-domain.** Open. Within end-protected designs with finitely many ends and integrable base endorsers, the only surviving configurations are the doubly misaligned cycles. Designs outside that class are untouched: two or more worlds with only non-integrable endorsers, countably many ends, and failures not of end-protected form.

## Update, 15 October 2026, evening (supersedes everything below where it conflicts)

- **Breakthrough (two referees).** The first full ranking with a world that genuinely fails to add up exists: a two-world system on the U-domain (D2.1). This refutes N17.B′, so "closed choice forces adding up" is false for bounded weights. The world is still endorsed by an unbounded (σ-finite) weight.
- **But it does not help T1 (E1, not yet refereed).** The exclusion argument needs only one well-chosen weighting, and D2-type failures are invisible to it.
- **Further closed doors.**
  - Tame edges force a whole world to add up (B1).
  - Glued credal worlds add up (C1).
  - (LF) forbids ties at the target weighting on every decomposable domain (D1).
- **Status of T1 on the U-domain.** Open, but the evidence points against a cover. The decisive problem is the σ-finite form of N17.B′ combined with E1.
- **Details.** See the Rounds 14–16 addendum in *Coverage on Decomposable Domains - Round Report* and §8.5(e)–(g) of the write-up.

## Update, 15 October 2026, late morning (supersedes everything below where it conflicts)

- **New exclusion.** No cover of T1 on the U-domain exists in which every world is CP-a or has a nonzero leading charge. This needs no nestedness; the step that removed the nestedness assumption is S2.1, confirmed by one referee. Complete worlds are excluded too, but still only under edge nestedness.
- **Two worlds.** A non-nested selection needs both worlds to lack a leading charge and to fail monotone continuity. Closed choice alone does not force nestedness; (C) must.
- **Mirror-image pairs.** They exist if closed sections are dropped. Whether closed choice excludes them is open (R1, and its weaker form ¬QC).
- **Details.** See the round 13 addendum in *Coverage on Decomposable Domains - Round Report*.

## Update, 15 October 2026, morning (supersedes everything below where it conflicts)

- **Excluded for T1 on the U-domain:**
  - additive rankings (on every decomposable domain, in fact);
  - rankings that add up with ties;
  - every ranking whose worlds are Walley-style coherent almost-preferences (new; the connecting step has one reader);
  - every ranking whose worlds are edge-nested and complete or have a leading charge.
- **What is left:** worlds that fail to add up and are incomplete, without a leading charge and not CP-a. The decisive problem is a two-world question, (R1)–(R4) in the round 12 addendum: mirrored certificate pairs, reduction of general certificates to simple ones, a rate in Lemma T, and nestedness.
- **No example** of such a world is known for any target.

## Update, 14 October 2026, night (supersedes everything below where it conflicts)

- **Additive rankings:** no cover of T1 on any decomposable domain (§6 of the write-up).
- **Rankings that add up but have ties (case M0):** no cover of T1 on the U-domain. The new parts of the proof have been read by two referees (§7.7).
- **The only route left for an ordinal cover of T1 on the U-domain:** a world whose errors do not add up. It must be incomplete, non-lexicographic, without a leading charge, and not a coherent almost-preference. No such world is known anywhere.
- **The extension lemma** for step-by-step constructions is false as previously stated. An exact replacement exists (a limit closure rule), and it is formal.
- **Details:** the round 11 addendum in *Coverage on Decomposable Domains - Round Report*.

## Update, 14 October 2026, afternoon (supersedes everything below where it conflicts)

- **Additive rankings: settled for T1.** No strictly guiding additive ranking with integral penalties covers T1 on any decomposable domain with (LF), for any ε and any interior target weighting. There are three essentially independent proofs; each was confirmed by one adversarial referee, and its inputs have two readings. Bounded charges are covered along one route. See *The Contamination Triangle.pdf*, §6, and the round 10 addendum in *Coverage on Decomposable Domains - Round Report*. Consequently the geometric problem CF(T1) has no solution, at the status of CCIBU.
- **What remains open:** non-additive (ordinal) rankings. The auditor is pursuing the positive ordinal route (building the ordinal relations directly). The natural impossibility-side test is whether the new argument extends to rankings that add up (M0) and to coherent almost-preferences.

## Strategy update, 14 October 2026 (supersedes the 13 October bullets below where they conflict)

- **Read first:** *The Contamination Triangle.pdf* (41 pp., 14 Oct). Then the round 9 addendum in *Coverage on Decomposable Domains - Round Report*.
- **Settled (additive rankings, the U-domain and non-adjacent domains):** no cover of T1. This now also holds with permitted negligible-stakes ties: for every band width in the sup norm, and below √((κ²+1)/(κ²+2)) in the Euclidean norm (N27).
- **The auditor's two open questions**, now sharper:
  - **(Q1) Exceptional ties.** Take a ranking that adds up (case M0). Its supporting assessment's ties lie on countably many *atom chords*: straight chords of the simplex, each cutting off a vertex. A cover of T1 forces at least one chord. Two configurations remain open:
    - R-a′: the target weighting lies on a chord;
    - R-b′: the target weighting lies off the chords.
    - Background: in two worlds an explicit ranking satisfying every axiom does resolve such a tie (N26.1), so ordinal tie-breaking is a real mechanism. For two-level lexicographic rankings in three worlds, only rigid non-crossing chords away from the target weighting remain (N26).
  - **(Q2) Two-sided domains** (evaluable models may accept f, accept −f, or give no advice near the target). (E5a) is closed (N28). Additive coverage of T1 on (LF) decomposable domains is equivalent to a geometric problem, CF(T1), about families of credal sets. The converse direction rests on CCIBU. The open case is sector caps at the vertices.
- **Single-reader results to be re-checked** before any of them is relied on in the paper: "no fan points" (N25 referee, Prop F); Prop R1 (N26 referee); the impossibility of (E5a) (N28, one referee).
- **Unchanged:** no positive evidence for rankings that do not add up (M1, M2). For n ≥ 4, additive rankings cannot cover credal sets containing three vertices. The framing decision remains with the author.

## Strategy at a glance, 13 October 2026 (read this first)

- **Definitions used throughout.**
  - *T1 (the three-world contamination triangle).* Fix ε ∈ (0,1) (computations use ε = 0.3) and let u = (1/3,1/3,1/3). The credal set is K = (1−ε)u + εΔ, the triangle with vertices v_i = (1−ε)u + εe_i. Its lower prevision is P(g) = (1−ε)(g_1+g_2+g_3)/3 + ε·min_i g_i. The target model is the coherent set of desirable gambles D_K = {g : m·g > 0 for all m ∈ K} = {g : (1−ε)(g_1+g_2+g_3)/3 + ε g_i > 0 for i = 1,2,3}.
  - *(LF), local freedom at the target (non-cheapness).* A ranking L with domain M_L satisfies (LF) at a target D if D ∈ C_L and there is an open cone N containing every nonzero boundary point of D such that M_L contains every model that differs from D only on gambles in N. On a decomposable domain this means: for almost every problem {g, −g} with g ∈ N, the advice range contains both "accept g" and silence. Purpose: to exclude cheap realisations in which every evaluable model gives the target's advice near its own boundary (the analogue of V = target, φ = identity for CPMs). Away from N, advice ranges may be smaller, down to a single kind of advice that every evaluable model gives.

- **Goal.** Dominance (D) is done (LDG v2). Coverage (A): for each coherent model, some reasonable ranking leaves it undominated; D_Δ by the agreed exception.
- **Method.** One ranking per target.
- **Covered:** precise models; normalized boxes; gauge-mixture polygons (incl. polygons arbitrarily close to T1); every target in two worlds; D_Δ; every target approximately.
- **Test case:** T1, the three-world contamination triangle. **Read first: *The Contamination Triangle.pdf* (this folder; 25 pp., 13 Oct).**
  - **Additive rankings: no cover of T1 on non-adjacent decomposable domains** (e.g. the U-domain), any ε, any interior target weighting, no regularity assumed; also every all-facing triangle in general position. Refereed independently twice (N18, N20).
  - General (LF) decomposable domains: two narrow residual configurations, (E5a) and (E4′), remain open.
  - Coherent almost-preference rankings (Walley 1991): no cover when worlds are complete, or with countably additive detection; in general reduced to a continuity property (U), which is open.
  - Small-stakes ties (forced or permitted): no help. Lexicographic rankings: fail (S). Rankings that don't add up: open, with no positive evidence.
- **Second reason to go non-additive:** for n ≥ 4, additive rankings cannot cover credal sets containing three vertices (v3).
- **Decision pending (author):** whether to treat exact coverage of T1 as excluded for "reasonable" rankings (the additive and coherent-preference cases), and how to frame the coverage half of the paper (a covered class plus approximation, an impossibility theorem, or an axiom change).

## Current state, 12 October 2026, 16:45 (supersedes the sections below where they conflict)

Decisions taken on 12 October, in order:

1. **Exception for the vacuous model.** The vacuous model is now written **D_Δ**; older notes write V. It is covered by the exceptional system in which good advice and silence tie on mixed problems. Write-in omission-blind losses for every other target are **not** adopted.
2. **Conditional values (Σ_T) are accepted.** Conditional on the worlds in T, the evaluator only shuns error; elsewhere (G) is strict. See *Conditional Shunning of Error*: closed choice via non-Bayes selections, coverage of closures of normalized boxes.
3. **Domains need not contain all models.** Every obstruction in this folder assumed that each ranking evaluates every measurable model. That assumption is not one of the axioms (see *Audit of Imported Assumptions 2026-10-12*). Domains need not be cones or convex.
4. **Non-cheapness is required at the target only.** The condition is local freedom (LF). The target D lies in C_L, and the domain contains every model that differs from D only on gambles in some open set containing the nonzero boundary points of D. Tangency at limit or boundary priors is allowed.
5. **Nothing may make (G) or (IB) empty.** Anything that does so is cheap.
6. **Domains are decomposable domains.** Domains must be closed under splicing (SC) and closed under convergence in measure. Equivalently, a domain is described by a measurable advice range A(g) on each binary problem (the kinds of advice that evaluable models give there), the domain being every measurable model whose advice lies in the advice ranges.
   - On decomposable domains, any rankings satisfying (G) and (IB) extend exactly to all models (*Domain Closure and Extendability*, in `CPMs/outputs/domain-axioms/`, author-checked). So (Ext) is not adopted as an axiom.
   - The extension does not carry closed choice or the target's admissibility, so the all-models impossibility results may **not** be applied through it.
7. **Notation.** M_L is the domain of ranking L. U_L is the set of gambles that evaluable models of a cone-type domain may accept (the evaluable models are its measurable subsets). D_Δ is the vacuous model.

**The open problem.** Under the accepted guidance orders, (IB), (LA), (S), (C), (E), (LF) at the target, and decomposable domains: can every coherent target be covered? Known positive cases:
- precise targets;
- normalized boxes and their Σ_T closures;
- parallel bodies (v19, on cone domains);
- every target when n = 2 (v3);
- D_Δ, via the exception.

Additive (integral) rankings on decomposable domains amount to realisation by measurable sign-preserving maps restricted to the advice ranges, a measurable version of the CPM problem. Escaping CPM therefore needs non-additive rankings that satisfy (IB).

**Evening update (revised 23:30, after the auditor's assessment).** See *Coverage on Decomposable Domains - Round Report 2026-10-12.md* and `decomposable-domains-2026-10-12/Consolidated Statements - Decomposable Domains 2026-10-12.md`. The open problem is unsolved, and neither impossibility nor the general rigidity of non-additive rankings is established. Three results are referee-checked, though not by a human:
- In two worlds, two classes of non-additive rankings select only what additive ones can: sandwiched rankings and two-level lexicographic rankings.
- For a single target, any sandwiched ranking reduces to an additive one, provided boundary ties are null.
- The three-world contamination triangle cannot be covered with a Bayes family that is constant near its prior. Additive coverage of the triangle itself is still open.

Polygons arbitrarily close to it are covered by gauge mixtures.

Everything below this section was written before these decisions. In particular, its claims that obstructions bind assume all-model domains.

**Attribution correction, later on 12 October:** this guide originally overlooked [truth_directed_losses.tex](/Users/jk13942/Documents/CPMs/truth_directed_losses.tex) and [nonadditive_losses.tex](/Users/jk13942/Documents/CPMs/nonadditive_losses.tex), from the 4–5 October investigation. The omission-blind treatment of V, the unanimous-problem repair, and the constant odds-ratio limit were already there. The recent limit note adapts them to the four-rank order and adds the explicit uniform bound. Its underlying coverage idea is not new.

**Conditional full coverage:** [Omission Blindness and Four Rank Guidance](<Omission Blindness and Four Rank Guidance.tex>) checks the adaptation of the old write-in losses to contradiction ranked worst, on all models. It preserves (IB), (S), and (C), and covers every coherent target **if every target may ignore missed gains outside its own interior**. That broader weakening has not been adopted: the exception is limited to V, because it is induced by a change to the background order (decision of 12 October). For any other target the write-in tie set depends on the target's own interior.

## The question we are now trying to answer

For each proper credal set M ⊊ Δ, find some ordinal ranking system under which its coherent SDG is undominated. The system must satisfy the standard axioms, including strict guidance improvement (G), independence across binary problems (IB), and closed competitive coherent selection (S). We continue to seek (C), with coherence understood modulo null sets. The constructions discussed here evaluate all measurable models.

Add **one exceptional system covering V = D_Δ**, in which good advice and silence tie on mixed problems. It retains strictness on unanimous problems, and retains (IB), (S), (LA), and (C). This indifference applies in every common context. In this system, Dᵢ ties with V at world i. Its constant selection is Cₚ = V.

Coverage (A) is existential **across systems**. It never required one system to leave every coherent model undominated.

**Current answer:** coverage of V is resolved under the agreed exception; full coverage of the remaining proper credal sets is still open for n ≥ 3. Incomparabilities are neither known to be necessary nor proved sufficient for this revised question.

## What is resolved

| Question | Answer | Proof location |
|---|---|---|
| Can the exceptional system cover V, keeping independence and closed choice? | Yes. Complete additive rankings; V is the unique undominated model modulo null sets. | [Vacuous Targets and Transfinite Construction](<Vacuous Targets and Transfinite Construction.tex>), Proposition “A precise way to allow neutral abstention”; also the limit theorem in the new note below. |
| Is the exception connected to strict rankings? | Yes. Strict, complete, independent rankings cover nested normalized boxes tending to Δ; their losses converge uniformly over models to the exceptional losses. | [Coverage after Neutral Abstention](<Coverage after Neutral Abstention.tex>), adapting **nonadditive_losses.tex**, Remark `twoshun`. The new details are the contradiction penalty and explicit bound. |
| Two worlds: can every coherent target be covered? | Yes, even under the original strict (G). This includes boundary intervals and V. | [Full Coverage by Homothetic Credal Families v3](<Full Coverage by Homothetic Credal Families v3.tex>), “Full coverage in two worlds”. |
| Every dimension: are there positive strict examples? | Yes: all precise models, and all normalized boxes with positive bounds on their supporting face. | v3, general Bayes construction and precise-model example; [Coverage after Neutral Abstention](<Coverage after Neutral Abstention.tex>), equations (3)–(4). This is an adaptation of the global concave-CPM construction to the current contradiction penalty. |
| Does strict (G) alone rule out an undominated V? | No. It is possible with complete additive independent rankings when (S) is omitted. | [Vacuous Targets and Transfinite Construction](<Vacuous Targets and Transfinite Construction.tex>), first proposition. |
| Original question: can complete strict rankings cover V when n ≥ 3? | No, with (IB) and (S). This resolves the old complete-ranking full-coverage question. | [Three Complete Rankings Cannot Cover](<Three Complete Rankings Cannot Cover.tex>); [Complete Rankings for Any Number of Worlds](<Complete Rankings for Any Number of Worlds.tex>), main theorem. |
| Does allowing finitely additive penalties solve the original obstruction? | No. The obstruction also applies to the specified positive finitely additive one-sided extensions. | [Closed Choice Beyond Ordinary Integrals](<Closed Choice Beyond Ordinary Integrals.tex>), main theorem; the one-sided strengthening is recorded in [Edge Dichotomy and Leverage](<Edge Dichotomy and Leverage.tex>). |
| Does the V exception permit full revised coverage by ordinary additive losses in all dimensions? | No for n ≥ 4. A proper credal set can contain three vertices, e.g. conv{e₁,e₂,e₃} in four worlds. The existing additive obstruction still excludes it under strict (G). | v3, additive obstruction and Appendix C; CBOI for the stated finitely additive extension class. |
| Is transfinite closure itself needed once the family and exact closed sections are chosen? | No. A least ordinal construction is obtained after countably many rounds of elementary rules, and every failure has a finite derivation. **Existence of consistent family/section choices remains open.** | [Coverage after Neutral Abstention](<Coverage after Neutral Abstention.tex>), “Exact consistency test”. **New, author-checked.** |

## The active open questions

1. **Coverage of all proper targets for n ≥ 3.** Can each be covered under strict (G), (IB), and (S), with the other standard requirements? Existing positive subclasses do not cover arbitrary interior, boundary, or lower-dimensional credal sets.
2. **Complete versus incomplete rankings for those targets.** The theorem excluding V under strict (G) no longer proves that incomparabilities are necessary. There is also no construction proving their sufficiency.
3. **Proper targets containing three vertices, n ≥ 4.** Complete rankings have not been universally ruled out. The clique theorem forces the endpoint property and fineness on edges between the contained vertices, and requires failure of the endpoint property on some other edge. That is a necessary condition, not a contradiction. Additive and specified finitely additive extension methods are already excluded.
4. **A consistent ordinal construction.** Choose a coherent family containing the target and closed sets Aᵢ(X) satisfying the face-cover condition. Their generated comparisons must avoid reversing strict guidance, creating comparisons outside the intended sections, or tying incoherent models with protected coherent ones. The new consistency theorem makes this task exact; it does not solve it.

The old problem of protecting V using *incomplete* rankings while retaining strict (G) remains mathematically open, but it is **not required by the revised coverage objective**. Its technical residual cases should not organize the main investigation now.

## Earlier results that must be kept in view

- [truth_directed_losses.tex](/Users/jk13942/Documents/CPMs/truth_directed_losses.tex), Theorem 2.4 (`thm:obstruction`): under truth-directedness, the specified domain closure, and the exchange-rate bound, targets with incomparable boundary supports are dominated. Vanishing exchange rates suffice. This includes suitable nonadditive losses and applies already in two worlds. It is not a restriction on all ordinal rankings satisfying (G), (IB), and (S).
- [LSP_CPMs_v19b.tex](/Users/jk13942/Documents/CPMs/LSP_CPMs_v19b.tex), Corollary 12.11: CPM error losses cannot cover targets with two boundary points of different supports, including nested supports. This geometric CPM result should not be conflated with the incomparable-support exchange-rate argument. Deriving vanishing rates for CPMs additionally requires the domain and weight conditions in the truth-directed note.
- **truth_directed_losses.tex**, Section 4 (`prop:ob`, `thm:coverage`): omission-blind write-in losses already cover every coherent target under the older background requirement. In the local copy these results are Proposition 4.3 and Theorem 4.4; the collaborator quoted a version numbered 4.4 and 4.6. Use the labels and section to identify the results.
- [nonadditive_losses.tex](/Users/jk13942/Documents/CPMs/nonadditive_losses.tex), Remark `twoshun`: mixing ordinary error loss with world-wise shun-error loss gives normalized boxes; crediting unanimous gains repairs the pure shun-error endpoint. This is the earlier source for the limit construction.
- [Omission Blindness and Four Rank Guidance](<Omission Blindness and Four Rank Guidance.tex>): the four-rank adaptation changes only contradiction penalties, leaving selected profiles intact. The broader policy gives full coverage; it is not proved necessary for general boundary-target coverage.

The older exchange-rate obstruction and the later unrestricted-additive obstruction have **different hypotheses**. Neither should simply be reported as the stronger version of the other. In particular, strict two-world coverage shows that boundary targets do not universally require omission-blindness.

## Why the apparent shortcuts are not proofs

- **Taking a limit of increasingly many comparisons:** independence, transitivity, and a protected target can survive a directed union, but closed sections need not. Closing them afterwards can force further comparisons through independence and transitivity. The required extension lemma has not been proved.
- **Restricting a proper target to a three-world face:** a change that improves the three selected worlds can worsen an additional world. The complete-ranking many-world paper explains the specific failure of its transfer argument outside the set of vertices contained in the target. An impossibility proof on a face is not automatically a proof of domination in the full model.
- **Importing the LP-CPM realization theorem wholesale:** v19a's proper-domain losses evaluate a restricted model domain. They do not directly provide rankings on all measurable advice with our global strict guidance order. The global normalized-box construction does provide a positive subclass after assigning contradiction the appropriate larger penalty.
- **Inferring an additive representation from independence:** this is false without additional conditions. The existing nonadditive single-world example does not, however, supply (S) or a full coverage configuration.

## The shortest useful reading route

1. [Loss Dominance Generalized v2](<Loss Dominance Generalized v2.tex>): abstract axioms, dominance and competitiveness, the simplex argument, and the meaning of coverage across ranking systems.
2. [Full Coverage by Homothetic Credal Families v3](<Full Coverage by Homothetic Credal Families v3.tex>): current guidance order and independence; positive two-world construction; the ordinary additive obstruction.
3. [Coverage after Neutral Abstention](<Coverage after Neutral Abstention.tex>): the accepted change of objective, the limit construction, the exact ordinal consistency test, and what is still open.
4. [Complete Rankings for Any Number of Worlds](<Complete Rankings for Any Number of Worlds.tex>): main and clique theorems; read the final “What remains for coherent models with three vertices” remark before trying to extend the impossibility conclusion.
5. [Incomplete Rankings and Coverage](<Incomplete Rankings and Coverage.tex>): consult individual results as needed for genuinely partial rankings. Its residual V problem is now optional background, not the main coverage target.

For the detailed three-world counting proof, insert [Three Complete Rankings Cannot Cover](<Three Complete Rankings Cannot Cover.tex>) before item 4. For finitely additive methods, insert CBOI before item 5.

## Where the technical results live

| File | What to use it for | Present role |
|---|---|---|
| [Full Coverage by Homothetic Credal Families v2](<Full Coverage by Homothetic Credal Families v2.tex>) | Full coverage via benchmark scores and refinements before imposing (IB). | Its construction is not independent. Positive background and source of the family idea. |
| [Loss Relations from Credal Families](<Loss Relations from Credal Families.tex>) | Early conditions (U), (U*), budget and family constructions. | Historical construction toolkit; not a solution to the present independent problem. |
| [Ordinal Refinement by Slack Envelopes](<Ordinal Refinement by Slack Envelopes.tex>) | The failure of an unrestricted refinement lemma; positive slack-envelope refinement. | Does not prove the extension lemma needed with (IB). |
| [Beyond Additive Guidance Rankings](<Beyond Additive Guidance Rankings.tex>) | Full-coverage examples without (S), and obstructions to simple priority constructions. | Shows exactly why retaining closed choice matters. |
| [Closed Choice for Independent Rankings](<Closed Choice for Independent Rankings.tex>) | Original ordinary-integral extension obstruction. | Superseded in strength by CBOI, but useful simpler proof. |
| [Closed Choice Beyond Ordinary Integrals](<Closed Choice Beyond Ordinary Integrals.tex>) | Positive finitely additive extension obstruction; an example with no ordinary-integral extension. | Active restriction on possible methods for proper three-vertex targets. |
| [Edge Dichotomy and Leverage](<Edge Dichotomy and Leverage.tex>) | One-sided extension suffices; leverage test; early additive edge restrictions. | Extension toolkit. The leverage criterion should be attributed as in Independence Chains. |
| [Finitely Additive Edge Dichotomy](<Finitely Additive Edge Dichotomy.tex>) | Edge behavior of charges. | Technical dependency for later extension arguments. |
| [Independence Chains](<Independence Chains.tex>) | Essential use of (IB) to join forced comparisons; original debt-transfer methods. | Earlier residual-case descriptions are superseded. |
| [Dense Thresholds and Debt Reduction](<Dense Thresholds and Debt Reduction.tex>) | Corrected debt reduction, including Theorem 10 used by later notes. | Technical dependency; use the corrected file. |
| [Edge Cycles and Separability](<Edge Cycles and Separability.tex>) | Cross-world threshold restrictions. | Technical intermediate results. |
| [Closed Choice Forces Fineness](<Closed Choice Forces Fineness.tex>) | Endpoint property, fineness, and extension results. | Dependency for FSE and the complete-case proof. |
| [Two Additive Worlds Without Completeness](<Two Additive Worlds Without Completeness.tex>) | Three worlds: two one-sided finitely additive extensions plus an arbitrary (IB) partner exclude V. | Settles the old two-additive-world problem; potential toolkit, not a general proper-target theorem. |
| [Fineness Spreads Along Edges](<Fineness Spreads Along Edges.tex>) | Fineness transfer, own-region arguments, and the earlier complete-case reductions. | Dependency for the complete-case solution. Its original complete-case open problem is now settled. |
| [Fineness for Any Finite Number of Worlds](<Fineness for Any Finite Number of Worlds.tex>) | One fine world implies all worlds fine; three-vertex domination; further finite-world transfers. | The propagation result remains useful. Its V conclusions are weaker than the later complete-case theorem. |
| [Independent Rankings Without Additive Structure](<Independent Rankings Without Additive Structure.tex>) | A complete independent single-world order with no suitable additive structure. | Has no (S) construction; not a coverage counterexample. |
| [Three Complete Rankings Cannot Cover](<Three Complete Rankings Cannot Cover.tex>) | Finite-chain counting, light sets, and the three-world complete impossibility theorem. | Definitive for the original complete V question. |
| [Complete Rankings for Any Number of Worlds](<Complete Rankings for Any Number of Worlds.tex>) | Extension of the complete V theorem; conditional clique restriction on proper targets. | Active: keep its unconditional and conditional conclusions separate. |
| [Incomplete Rankings and Coverage](<Incomplete Rankings and Coverage.tex>) | Partial-ranking reductions, finite cancellation, and counterexamples to some continuity implications. | Active toolkit; its final strict-V residual alternatives are optional for the revised goal. |
| [Vacuous Targets and Transfinite Construction](<Vacuous Targets and Transfinite Construction.tex>) | Exceptional V system; union lemma; permanent open forbidden neighborhoods. | The exception is now accepted. Its unresolved bookkeeping issue is sharpened by the new consistency theorem. |

## Historical status reports and qualifications

- [Assessment and Remaining Question](<Assessment and Remaining Question.md>) is dated 11 October. Its statement that the complete case remains open is **superseded** by the two complete-ranking papers.
- [P1 Status Round 5](<P1 Status Round 5.md>) contains earlier conditional attacks. The new counting proof does not depend on its proposed near-vertex comparability lemma. Its open-status headings are historical.
- [Review of Complete Rankings 2026-10-12](<Review of Complete Rankings 2026-10-12.md>) records the scope of the preceding audit and two important qualifications to informal summaries:
  1. The finite-cancellation equivalence is for a **full weak extension on all regular comparisons**, under its stated hypotheses. A separate result gives a sufficient one-sided criterion; do not conflate the two.
  2. The most general final residual alternative gives fine **debt** orders and nonextendibility at at least two worlds. Credit fineness, and hence the stronger conclusion about two violations of finite cancellation, needs extra hypotheses.

These are qualifications to summaries, not reported errors in the written theorems.

## Verification and copies

The supplied complete- and incomplete-ranking notes are reported by their author as checked by AI referee passes. The preceding review found no gap in the main complete-case argument and checked its principal finite-world extension, but did not freshly audit every line of the 46-page incomplete note and all dependencies. No human verification is asserted here.

The limit adaptation and exact consistency theorem in **Coverage after Neutral Abstention** were directly checked and compiled; the collaborator subsequently reported checking them without finding an error. The box construction and its limit have the earlier sources credited above. The exact consistency argument is a least-closure argument, not an existence proof for consistent sections. The new four-rank write-in adaptation has been author-checked and compiled but has not received an independent referee pass. No human verification is asserted.

Main reading folder:
`/Users/jk13942/Documents/GitHub/choosing-paper/Generalized dominance paper/`

Working source copies of the new note and this guide:
`/Users/jk13942/Documents/CPMs/outputs/coverage-after-neutral-abstention/`

Earlier working copies from this collaboration are in `outputs/independent-guidance-v3/`, `outputs/independence-oct11/`, and `outputs/independence-oct12/` under `/Users/jk13942/Documents/CPMs/`.

**Next substantive target:** a construction or impossibility proof for proper credal targets under strict (G), (IB), and (S). Further progress on strict-V exotic rankings is not needed unless it supplies a tool for that target.
