# Mechanism design memo: candidate primitives for non-additive accuracy rankings

19 October 2026. A design document, not a results note. Nothing here is a theorem unless labelled; arguments marked "design check" are short sanity arguments that still need writing up. It responds to audit's *Matching and Joint Defence – Mechanism Audit* (19 Oct).

## 1. What a mechanism must get past

Each item below is something a candidate rule must be checked against before any construction work starts.

- **S1. Accounting identity (audit §1).** If every accepted exchange conserves or increases one fixed positive weighted value, that value is an additive endorser. The mechanism is then additive in disguise.
- **S2. Product obstruction (audit §2).** If each world tests each region separately, a rival can combine one region that world 1 won't defend with another that world 2 won't defend. Compensation must work *across* regions.
- **S3. Finite-statistics collapse (NN1 Lemma 2.1 / NN2 Thm 2.3, unrefereed; consolidated in "Quorum Rankings and the Contamination Triangle").**
  - What it covers: every rule built from finitely many fixed additive scores (additive, lexicographic, rate-adjusted, quorum).
  - What it does: near selected boundaries such rules collapse to one score, which the old results exclude.
  - How it works: it is a counting argument that needs finitely many scores with *coinciding* directions.
- **S4. The single-weighting barrier (FF2 Thm 4.1, refereed; survives without transitivity and without independence).** No single integrable weighting may endorse all local comparisons out of selected models near the target.
- **S5. The swap rival (LL1, refereed).**
  - What it is: equal tiny swaps on the two sides of a boundary point. Every per-problem score sees them as almost cancelling.
  - What it rules out: any rule demanding a margin proportional to the size of the change. Small rivals must be beaten by sign alone (strict-sign lifting, refereed).
- **S6. Ties with incoherent models.**
  - The hazard: a rule in which leaving an advice state can be costly in *both* directions ("hysteresis") creates ties between distinct models.
  - Why it matters: direct (C) then requires every model tied with a coherent undominated one to be coherent itself.
  - Rules that judge each problem separately are especially exposed, because the set of models each rule protects is then a product over problems, while coherent models are not. (Design check needed: this is a hazard, not a proved exclusion.)
- **S7. Independence at record level.** A verdict may depend only on what changes (old and new advice on the changed problems). In particular it may not use "the starting model is coherent", which depends on shared advice (audit §3).

## 2. Three explicit candidate rules

### A. Super-majority of a continuum of judges

- **Rule.** At world i, take a probability space (V, π_i) of judges. Each judge v has an integrable, strictly guiding additive loss ℓ_iv, jointly measurable in (v, problem, advice) with an integrable envelope. Fix θ_i ∈ (2/3, 1). Accept "C no worse than X" at world i iff
  π_i{ v : L_iv(X) − L_iv(C) ≥ ψ(d_iv(C, X)) } ≥ θ_i,
  with ψ a shrinking margin as in the strict-sign lifting lemma (or strict signs and lifting).
- **What comes free (design checks: these are the finite-quorum proofs with mass in place of counting):**
  - **Independence:** the verdict is a function of the record.
  - **Strict guidance:** every judge supports a pure improvement.
  - **No ties:** θ > 1/2, so two supporting sets overlap in positive mass, and no judge can support both directions.
  - **(TC):** three supporting sets of mass > 2/3 share a judge, who cannot support all three edges of a forbidden triangle.
  - **Closed sections:** each judge's condition is closed in the index. Reverse Fatou gives π{v : condition at the limit} ≥ limsup ≥ θ.
  - **Direct (C) and admissibility:** these come automatically, as for finite quorums.
- **Why it might escape S3.** The collapse proofs force a *positive number* of judges to share one direction. With an atomless judge distribution, the analogous statement looks like a centre-point (Tukey-depth) conclusion: one common direction lying in every blocking cone, not a positive mass of coinciding judges.
  - A single common direction carries zero judge mass, so it need not reduce the committee to one score. This is the specific hook.
  - It is a conjecture to check first.
- **Main risk.** OO1's chain (sub-lemmas L1 → Link → S0 → FF) may go through for measures as well. The first test is whether NN2 Thm 2.3 genuinely needs atoms.
- **Honest classification.** This is the infinite limit of the quorum line, not a new primitive. Its value is that it targets the exact step the collapse proof uses.

### B. Exchange licensing with non-conservative rates

- **Ingredients.** Treat each changed problem as an item carrying its transition τ = (problem, old advice, new advice). At world i every item is a gain or a loss, with size ℓ_i(τ) (rank steps times a density). World i has:
  - an exchange relation E_i between loss types and gain types;
  - a rate κ_i(τ, σ) > 0 for each permitted pair.
- **Rule.** Accept "C no worse than X" at world i iff X's world-i gains can be *paid for* by X's world-i losses. That is, there is a transport plan supported on E_i, covering every unit of X's gain, under which each unit of loss is used at most once at its rate.
- **What comes free:**
  - **Independence:** the rule is a function of the record.
  - **Cross-region compensation (S2):** the plan may match gains in one region with losses in another.
  - **Strict guidance:** a pure improvement has nothing to pay for, and its reverse has nothing to pay with.
  - **Small scales:** the plan is continuous in measure, so arbitrarily small rivals are handled.
- **Why it can escape S1 and S4.** Suppose the rates are *conservative*: every cycle of permitted exchanges has rate-product 1. Then a potential exists, and it is an additive endorser (S1). With *non-conservative* rates (an "arbitrage" cycle of length ≥ 4), no single potential exists.
  - **The non-endorsement certificate** is then exactly the cycle of exchanges. Audit's composability point enters here: the cycle can be completed only by exchanges that consume one another's advice states.
  - **Cycle cost:** cycles of length 3 must be absent from E_i, or (TC) can fail. That makes (TC) a constraint on the exchange graph's short cycles (design check).
- **Duality gives the structure.** For one record, feasibility of the plan is a linear program. Its dual supplies a *record-dependent* potential. So each accepted comparison has its own additive endorser, which may differ from record to record.
  - This is the infinite-dimensional analogue of a quorum's "mixture that changes with the branch", without the finite-statistics structure that S3 exploits.
- **Main risks.**
  - (TC) for composites of two chained exchanges.
  - S6 ties when rates make compensation cheap in both directions.
  - Closed sections, which need lower semicontinuity of plan feasibility in the index.

### C. Transition pricing (a calibration case, expected to fail)

- **Rule.** Accept "C no worse than X" at world i iff ∫ c_i(h, a_C(h), a_X(h)) dμ ≥ 0. Here c_i(h, a, b) is the cost of moving from advice a to advice b, chosen *not* of the potential form ρ(h, b) − ρ(h, a). For example, a two-step jump costs less than its two single steps.
- **What it shows.** It formally escapes S1 and S4: relative to a fixed starting model it is additive, but the effective weighting depends on that model's advice.
- **Why it probably fails.** It judges each problem separately. So it is exposed to S6 (hysteresis ties) and S2-style splitting.
- **Why run it anyway.** A quick exact test would show whether S6 is a theorem, and that would screen out every problem-by-problem rule at once.

## 3. Screened out before design work

- **Ordinary matching** (S1: the rank-integral endorser).
- **Stochastic-dominance or majorisation of rank distributions on the changed set.** These are intersections of finitely many additive rankings, already excluded.
- **Choquet or lower-expectation rules with a sup over a credal set of densities.** Again intersections of additive rankings, excluded.
- **Rules with "some density in a credal set endorses".** These are unions of additive rankings: (TC) fails unless the union is a super-majority, which is A.
- **Sequential licensing that installs every composable chain.** This is transitive closure, and drifts back towards additivity.

## 4. Proposed first experiments (screening only, no main theorems)

All on audit's two-world target: interior credal set [1/3, 2/3], full four-advice domain.

1. **A versus S3.** Does the blocking-cone collapse need atoms? Either:
   - an atomless judge distribution that passes the local branch conditions with no positive-mass coincidence; or
   - a measure version of the collapse.
2. **B, a minimal instance.**
   - Specify E_i and κ_i with a 4-cycle of arbitrage among transition types, scale-invariant (conic), on the two-world domain.
   - Check (TC), no ties and strict guidance on exact finite cell models.
   - Exhibit a non-endorsement certificate *out of the coherent selected models of [1/3, 2/3]'s family*, where the exchange actually supplies a defence the other world doesn't.
3. **C, calibration.** Make the S6 hazard a proved screen, or find that it is not one.

**Success means** a rule that passes S1–S7 on paper, and an exact finite certificate out of coherent selected models in which compensation across regions is essential. Only then would a full two-world construction be worth a proving round.

---

## 5. Screening results (19 October 2026, afternoon)

**Sources.** Three screening notes, unrefereed: `SCREEN_A_notes.md`, `SCREEN_B_notes.md`, `SCREEN_C_notes.md`, with exact-arithmetic scripts in `screenA_py/`, `screenB_py/` and `screenC_py/`. All three use audit's two-world target K* = {m_1 ∈ [1/3, 2/3]} on the full four-advice domain.

**All three candidates fail.** Each fails for a precise reason, and together the reasons map the design space.

### A. Super-majority of a continuum of judges: FAILS S3 (PROVED)
- **What passes:** all the design checks. (IB), strict (G), no ties, (TC), closed sections, direct (C) and admissibility hold. Strict cycles occur exactly for lengths k ≥ ⌈1/(1−θ)⌉, so k ≥ 4.
- **Measure collapse (Thm 3.3).** The collapse does NOT need atoms. With quantiles in place of order statistics, the same chain of inequalities forces judges of total mass ≥ 2θ − 1 to share one normalised boundary profile. With θ > 2/3 that coincident set is a blocking set, and it propagates to every world.
- **The memo's centre-point hook fails.** A direction in every blocking cone needs Tukey depth ≥ θ > 1/2. A profile law with no atom there has depth ≤ 1/2.
- **Two-world target (Prop 4.1; CHECKED for D_{K*} and four nearby interval models).** A two-sector rival at the two boundary rays defeats the strict-sign test unless the two worlds' laws of the boundary switch ratio share an atom of mass ≥ 2θ − 1. An atomless example (ratios uniform on [1,2]) fails for every θ > 1/2.
- **Lifting lemma.** It survives a continuum only under a strict-slack version of (QS). Bare strict signs at exactly θ do not lift (CHECKED example).
- **Lesson.** The collapse uses three things: judges that are each additive, blocking mass < 1/2, and at least two active worlds. On the two-world target only the first can be dropped, so **a new primitive must make the individual judges non-additive.** Candidate A is folded into the quorum line.

### C. Transition pricing: passes S6 as posed, but FAILS as a mechanism (two worlds PROVED; three or more worlds CONJECTURE)
- **(TC) has an exact criterion** (finite cell models): there is one weight triple λ with c(x,z) ≥ λ₁c(x,y) + λ₂c(y,z) + λ₃c(z,x) on every problem.
- **(TC) alone excludes hysteresis:** a round trip a → b → a can never have positive total cost (two-problem swap, CHECKED). So the S6 tie hazard is pre-empted by (TC), not by (C).
- **Competitiveness.** At weight w it is problem-by-problem stability, and the set of stable models is a product over problems. With (LA), (S) and direct (C), the stable advice must be unique a.e.
- **A full two-world system with a non-potential cost exists.** Discounting the direct accept ↔ reject jump symmetrically gives a system through K* satisfying every axiom (no-reversal for every cycle length; intransitive).
  - **BUT** in two worlds every axiom-satisfying linear problem-separable rule has, at each world, an integrable strictly guiding additive penalty endorsing every comparison out of a selected model.
  - So it is additive in disguise (S1), and FF2's hypothesis holds without localisation.
- **Lesson.** Problem-by-problem rules are screened out in two worlds. Open: three or more worlds (gaps at face-selected models and a zero-cost edge case), jumping selections, and nonlinear separable rules (which fall to S3).

### B. Exchange licensing: FAILS (PROVED; 43 exact checks)
- **What passes:** (IB), S7, strict (G) and closed sections.
- **(TC) has an exact condition.** No exchange cycle may have rate-product > 1, and every edge on a product-1 cycle must have its reverse at the inverse rate.
  - So the memo's design (a 4-cycle of arbitrage, no 3-cycles) FAILS (TC). Two accepted records give X ⪯ Y ⪯ Z with Z a pure improvement of X (CHECKED on 5 cells).
- **When (TC) holds, a fixed positive potential endorses every accepted comparison,** so S1 fails. The record-level LP dual gives a fixed finite panel of gain/loss price pairs, not record-dependent potentials.
- **S3:** B is not outside the finite-statistics class. A one-type B is LL3's margin judge.
- **S5:** passes iff the rates across each selected boundary multiply to at least 1. The minimal instance fails.
- **The experimental target is impossible as posed:** with (TC) there is an endorser. Natural (comonotone) interval families admit no certificates (LL3 Lemma B0).
- **Nearby result (CHECKED).** A 4-record certificate out of K* and the nested, non-selected model [2/5, 3/5]: a cross-region exchange is K*'s only defence against a rival that world 2 rejects. But the same exchanges, re-sited, form a "pump" that breaks (TC).
- **Narrow window (PROVED; CHECKED).** With un-decomposed transition types, arbitrage routed only through the contradiction state keeps (TC) with no endorser (sharp at rate 3). But comparisons out of coherent models never see it, so it is irrelevant to coverage.

### New screen S8 (convexity), from Screen B, Lemma 5
- **PROVED for polyhedral cones in rung-type masses:** a rule whose accepted records form a convex cone in finitely many type masses either has a positive additive endorser or violates (TC). The convexity lets two accepted records be added into a "pump".
- **Scope:** for multi-rung transition types it is CONJECTURE B.1.
- **Why quorums escaped it:** their acceptance set is a union of cones, not a convex cone.

## 6. What the screens show about the design space

Combining S8 with the collapse results (NN1/NN2 for finitely many judges; Screen A for a continuum) gives two cases.

1. **The rule's accepted records form a CONVEX set** (in type masses). Then (TC) forces an additive endorser. This covers additive rankings, intersections, transition pricing and exchange licensing.
2. **The accepted set is NON-CONVEX but built from additive judges.** That includes unions or super-majorities, finite or continuum. Then the collapse forces a coincident blocking set of judges near selected boundaries, and the committee reduces to one additive score.

So a viable primitive must be **non-convex AND not assembled from additive judges.** Its non-additivity has to sit inside each individual verdict, not in how additive verdicts are aggregated.

That is a sharp design question, which I put to the author and audit:

> Is there an independent (record-based), strictly guiding, (TC)-consistent acceptance rule whose accepted records form a non-convex set that is not a super-majority of additive judges?

**Examples of what that could look like (unscreened ideas, recorded only):**
- verdicts that depend on how changes are **arranged** across problem space, beyond type masses, for instance on their geometric spread or ordering;
- judges that are themselves **lexicographic or threshold-based** inside one verdict;
- rules defined by **comparing patterns as wholes**, not by summing.

Each must be screened against S1–S8 before any construction work.

**Withdrawn from the original memo:**
- §2A's centre-point hook;
- §2B's "no 3-cycles" condition and its "record-dependent potentials" claim;
- the expectation that S6 would be the decisive screen for C. (TC) pre-empts hysteresis, and the decisive failure is S1.

---

## 7. Author's proposals, screened (19 October 2026, afternoon)

### Proposal 1: two measures, one for added errors and one for removed errors

**The rule.** Write E_X = X ∇ D_i for the world-i error set of X (∇ is symmetric difference). Take finite measures μ⁺_i and μ⁻_i, and set

X ⪯_i Y ⟺ μ⁺_i(E_Y ∖ E_X) ≥ μ⁻_i(E_X ∖ E_Y).

So μ⁺ prices the errors Y adds and μ⁻ the errors Y removes. Independence holds automatically, because only the changed gambles enter.

**Verdict.** In the direction that keeps (TC), the rule is an intersection of additive rankings. In every other direction it breaks (TC). Details:

- **Case μ⁺ ≤ μ⁻ everywhere** ("removing an error is worth at least what adding it costs").
  - **The rule is exactly the unanimity of the additive rankings ν with μ⁺ ≤ ν ≤ μ⁻ (PROVED).** The added and removed sets are disjoint, so the worst member of the band prices additions at μ⁺ and removals at μ⁻.
  - Hence it is transitive, and every world adds up. The rankings are the classical density-band credal ranking.
  - For T1 it is excluded by the intersection theorem plus gm. It fails S1. Random exact checks (150 instances) confirm both transitivity and the identity with the band.
- **Case μ⁺ > μ⁻ on a non-null set S** ("sticky": leaving the status quo is costly in both directions). (TC) fails (PROVED for atomless μ).
  - Take P, Q ⊆ S with μ⁻(P) = μ⁻(Q) = m, μ⁺ ≥ (1+δ)μ⁻ on S, and any R with μ⁻(R) ≤ δm.
  - Let X have errors on Q and R; let Y have errors on P and R; let Z have an error on Q only.
  - Then X ⪯ Y and Y ⪯ Z, while Z is a strict guidance improvement on X.
  - Exact instance (CHECKED): μ⁺ = 2, μ⁻ = 1 on P, Q, R.
- **Mixed cases** fail (TC) on the sticky part.
- **One further point.** Measured through error sets on the full domain, contradictory advice has error set {−g}, smaller than bad advice's {g, −g}. So the error-set form ranks contradiction above bad advice, against the adopted guidance order. This is harmless on domains without contradictory advice.

**Relation to earlier work.** This is a special case of candidate C (§2C, screened in §5): problem-separable transition pricing with cost μ⁺ for adding an error and gain μ⁻ for removing one. Its (TC)-safe case coincides with the intersections of additive rankings.

### Proposal 2: a measure that depends on the base model

**The rule.** X ⪯_i Y ⟺ μ_X(E_Y ∖ E_X) ≥ μ_X(E_X ∖ E_Y). The pricing measure is chosen per base model X.

**Verdict.** Independence removes almost all of the added freedom. The independent version reduces to Proposal 1 or candidate C. The independent version that keeps real freedom lets the measure depend on the record, not on X.

**Lemma P2.1 (sketch; needs writing up).** Suppose the rule satisfies (IB) and the μ_X are finite and atomless. Then μ_X has a density of the form c(X)·ρ(h, a_X(h)): a positive factor depending on X globally, which cancels, times a function of X's advice at the problem h alone.

*Sketch.*
- By (IB), the verdict on adding A and removing R depends only on X's advice on A ∪ R.
- Atomless measures are fixed up to scale by such cross-comparisons. So μ_X restricted to any set S is fixed up to scale by X on S.
- Additivity over a partition of A, applied to arbitrarily small pieces, makes the density ratio at two problems depend only on the advice at those two problems.

**Consequence.**
- In binary error-set terms (h either is or is not an error of X), ρ(h, out) and ρ(h, in) are exactly Proposal 1's μ⁺ and μ⁻.
- On the full four-advice domain the density may also depend on the status of −h. That is general problem-by-problem transition pricing (candidate C). In two worlds it is additive in disguise (Screen C), and (TC) excludes the "sticky" direction (Proposal 1).
- Any dependence of μ_X on X's advice elsewhere breaks (IB). For example, take μ_X = ν when X is coherent and ν′ otherwise, with ν(A) ≥ ν(R) but ν′(A) < ν′(R). Two bases that agree on A ∪ R, one coherent and one not, then get opposite verdicts on the same change. This is audit's S7.

**The independent version that keeps freedom.** Let the measure depend on the RECORD t = (changed set, old advice, new advice): X ⪯ Y iff μ_t(E_Y ∖ E_X) ≥ μ_t(E_X ∖ E_Y).
- (IB) then holds automatically.
- Because μ_t changes with t, the accepted set need not be convex, so S8 does not apply.
- The five-patch licences are of this form.
- So is the author's earlier "splicing at a pair-indexed weighting", here with (TC) in place of transitivity.
- What is unconstrained: any (IB) rule can be written this way, so the content lies entirely in a structured choice of t ↦ μ_t.
- **Design questions:**
  - which structured record-dependence keeps (TC) and closed sections;
  - whether it avoids the finite-statistics collapse. That collapse applies when μ_t depends on t through finitely many fixed additive statistics.

### Proposal 3: a pair-indexed weighting from the coherent family

**Reconstruction.**
- Take λ symmetric (λ(−S) = λ(S)) and abs. continuous. Then h_{X,Y} = ∫_{X∖Y} g dλ − ∫_{Y∖X} g dλ ∈ R^n.
- Its i-th coordinate is exactly I_λ(Y,i) − I_λ(X,i), where I_λ(X,i) = ∫_{X∇D_i} |g_i| dλ is the standard additive (truth-directed) loss. So h is the vector of world-wise additive advantages of X over Y. This is the disagreement vector of the author's splicing note, with the opposite sign.
- As written, e_{X,Y} mixes signs: ∫ g_i over error sets is not a loss. Its natural reading coincides with h.
- Also as written, the right-hand side "P_m(e) ≥ 0" does not depend on i. A per-world version is needed.

**Obstruction for the literal form (PROVED).** Suppose world i's verdict depends on the pair only through h_{X,Y}, i.e. X ⪯_i Y iff F_i(h_{X,Y}). Then strict (G) forces F_i(h) = [h_i > 0] whenever h_i ≠ 0.
- *Reason.* Every vector h with h_i > 0 arises from a pure world-i improvement: X accepts a small wedge S of gambles with g_i > 0 that Y leaves unaccepted, giving h = ∫_S g dλ, in any direction with positive i-th coordinate. Strict (G) then requires X ⪯_i Y, and rejects the reverse.
- *Consequence.* World i is the additive I_λ ranking with ties at h_i = 0 broken somehow. That is the "adds up" class (excluded for T1).
- Moreover, in any number of worlds an imprecise model is never competitive for I_λ. Its Bayes acts are precise, so some rival beats it at every world.
- The same argument applies to any rule that sees a record only through finitely many integrals in which world i's coordinate is a strictly guiding loss difference.

**A version that could work: pair-indexed proper scoring.** Use the pair only to CHOOSE a scoring rule, and let the verdict see the whole record.
- For each m, fix an additive strictly guiding penalty ℓ^m under which C_m is the m-Bayes model.
- Let the record t of the pair choose m(t), for example m(t) ∈ argmax_m P_m(h_t) as proposed, or the splicing note's σ(v).
- Set X ⪯_i Y iff L^{m(t)}_i(X) ≤ L^{m(t)}_i(Y).

What comes free:
- **(IB)** holds automatically.
- **Strict (G)** holds, since each ℓ^m is strictly guiding.
- **Ties.** None at world i between distinct models whenever ℓ^m is strict.

**The competitiveness requirement, exactly.** C_p is competitive against Y if C_p is ℓ^{m(t)}-Bayes at some weight supported in supp p, where t = rec(C_p, Y).
- The record shows C_p's advice only on the changed set. So m(t) must work for EVERY selected model with that local advice.
- Hence the requirement is a decoding condition: from the local advice one must pick an m whose scoring rule makes all those selected models win.
- In two worlds, with strictly monotone endpoint maps l(p), u(p), a record touching a boundary of C_p reveals l(p) or u(p), and so p itself. That makes decoding plausible.

**Open checks:**
- (TC): pair-dependent rules can cycle; the splicing note found a strict 3-cycle with the homothetic base.
- Closed sections: m(t) may jump with t.
- Records that touch no boundary.
- Whether the comparisons are non-additive in the relevant sense. If one ℓ works for every m, the rule is just additive, and gm excludes T1.
- This is the author's splicing proposal with the verdict re-routed through a Bayes-adapted penalty.

**Corrected e (author, 20 Oct).** e_{X,Y}(ω_i) := ∫_{(E^i_X∖E^i_Y) ∪ (E^i_Y∖E^i_X)} g_i dλ.
- The two error-set differences together form E^i_X △ E^i_Y = (X △ D_i) △ (Y △ D_i) = X △ Y, which does not depend on i. So e_{X,Y} = ∫_{X△Y} g dλ.
- This is symmetric in X and Y, so it carries no information about which model is better.
- With λ symmetric, a full reversal on a problem (X accepts g, Y accepts −g) contributes g_i + (−g_i) = 0.
- So e cannot serve as the evaluated quantity. Restoring direction with |g_i| gives I_λ(Y,i) − I_λ(X,i) = h_i, and the literal-form obstruction applies.

**The penalty ℓ^m, explicitly.**
- *Additive* means: a per-problem penalty at each world, integrated over problems.
- *Strictly guiding* means: at world i the penalty strictly increases in the advice's world-i rank (good < silence < bad < contradiction).
- *C_m best for m* means: C_m minimises the m-weighted total loss Σ_i m_i L^m_i over all models, and is therefore undominated under ℓ^m.

**Construction.** For a credal set M = M_m with m ∈ M ⊂ interior of Δ:
- Let q(x) ∈ argmin_{q∈M} q·x, so that q(x)·x = P_M(x).
- Define the world-i penalty for accepting gamble x as π_i(x) := −x_i q_i(x)/m_i, with not accepting priced at 0.
- The penalty of an advice on the problem {g, −g} is the sum over the accepted gambles. Contradiction is overridden to cost strictly more than bad advice; a contradictory model is then never best.
- **Guidance.** The sign of π_i(x) is −sign(x_i).
- **Best choice.** Σ_i m_i π_i(x) = −P_M(x). So the m-weighted best advice accepts x iff P_M(x) > 0, which is exactly C_m = D_M (unique a.e.).

**Screen of pair-indexed scoring (SCREEN_P3_notes.md, 20 Oct; unrefereed).** Setting: ℓ^m is any family of strictly guiding additive penalties, and Bayes-adaptedness is dropped.
- **(IB) and strict (G):** automatic.
- **Competitiveness and direct (C) never bind on their own (PROVED).** For every record out of a selected base, some strictly guiding penalty makes the base win at an active world. So everything turns on (TC) and closed sections.
- **If the choice depends only on the unordered record,** every pair is comparable, so (TC) is the same as transitivity. With a rich penalty family these rules are exactly the independent, strictly guiding total preorders, the write-up's "total world" question.
- **The literal choice argmax_m P_m(h) always picks a vertex (PROVED).** Indeed P_m(h) ≤ m·h ≤ max_i h_i = P_{e_i}(h). So it reduces to a choice between n scores and collapses by S9.

**New screen S9 (anchoring collapse; PROVED, any number of worlds, any record-based rule).**
- *Hypothesis:* for one model C and one additive loss ℓ, the verdicts on records out of C containing a fixed small "anchor" pattern are exactly ℓ's.
- *Conclusion:* (TC) forces ℓ to endorse every small comparison away from the anchor. For rules complete on records, the world IS ℓ there. If every score the rule uses is anchored somewhere, the world is one global additive loss.
- *Exact failure instance:* two scores on chained records give Z ⪯₁ C ⪯₁ X with X ≺₁ Z, the same mechanism as the splicing 3-cycle.
- *Consequence:* a locally constant choice of penalty near a selected model is fatal, and the collapse is to a GLOBAL single loss, not just a local CPM problem.

**What escapes.** No selected model may have an anchor, and the world must not be an "almost representable" total order (write-up Cor. B32, Thm E3, imported). No instance is known.

**Verdict.** Pair-indexed scoring is screened out unless a choice rule with no anchors exists. It formally escapes S3 and S8, but every anchored instance is additive.

---

## 8. Designing around (S): separation-gated evaluators (20 October 2026)

### 8.1 Where the five-region construction stood
- **Author's construction** (*Disagreement-Selected Evaluators*, 20 Oct). World 1 picks an additive evaluator from the unordered pattern of disagreement. Four exceptional patterns defend A = D_[1/4,3/4] and B = D_[2/5,3/5]; every other mixed disagreement is judged by unanimity of all positive weightings. World 2 uses guidance only.
- **What it achieved.** Strict (G), (IB), (TC), (LA), direct (C), and closed sections along continuous families. No fixed positive weighting supports the four defences.
- **Why it failed.** (S) fails for every selection (PROVED in audit's note): the rival A ∪ a ∪ (−e) is defended at neither world, and any (S)-selection would have to pass through A.
- **Audit's guidance.** Design both worlds' obligations jointly around (S), keep the verdicts record-based, closed and (TC), and put the non-additivity into the defences that are actually needed.

### 8.2 The construction (note: *Separation-Gated Evaluators in Two Worlds*; one referee, repairs incorporated)
- **Rank steps.** For world i, a model X has the set U_i(X) of rank steps (g, j) with r_i(g, X) ≥ j, j = 1, 2, 3. In passing from X to Y, world i loses the steps Y adds and gains the steps Y removes.
- **Priority order (keys).** At world 1, step (g,1) has key l⁻¹(t) and step (g,2) has key u⁻¹(t). At world 2 the keys are 1 − u⁻¹(t) and 1 − l⁻¹(t). Contradiction steps and unanimous-problem steps get keys spread over (−2, −1).
- **Threshold lemma (PROVED).** Every selected model C_p = D_[l(p),u(p)] is a threshold set: U_1(C_p) = {key ≥ p}, and U_2(C_p) = {key ≥ 1 − p}.
- **The rule.** X ⪯_i Y iff (a) X = Y; or (b) Y is a pointwise weak world-i worsening; or (c) the pair is *separated* at world i and Φ_i(X, Y) ≥ 0.
  - *Separated* means: Y adds a non-null set of steps, and every step Y adds has a key no higher than every step Y removes.
  - Every other mixed comparison is incomparable.
- **Main theorem (PROVED; confirmed by one referee).** Suppose Φ_i is record-based, continuous along the family, has the right signs on pure comparisons, and is covering (Φ_1 ≥ 0 or Φ_2 ≥ 0 out of every selected model). Then the system satisfies every axiom on the full four-advice domain:
  - reflexivity, strict (G), (IB), (TC);
  - (S) with every C_p undominated and every section closed;
  - (LA), direct (C), (LF), (SC).
  - There are no cycles of any length.
  - Every non-selected model is strictly dominated by a selected one.
- **Division of labour.**
  - The gate alone gives (TC). An accepted comparison adds before it removes, so a cycle would have to undo, low in the order, steps it only ever adds.
  - The threshold lemma gives (S). Every disagreement with a selected model passes the gate at both worlds.
  - The verdict is otherwise free.
- **Non-additive instance (PROVED; confirmed by one referee with three repairs).** Φ_i = 2·(added step mass) − (removed step mass) at both worlds. This is the author's Proposition 1 in rank-step form, sticky direction, μ⁺ = 2μ⁻.
  - On its own it violates (TC). Gated, it satisfies every axiom.
  - No integrable strictly guiding field, and no finitely additive weight positive on non-null sets, endorses either world's comparisons out of selected models. The failure already occurs near almost every selected boundary point (a dense set of indices). It need not occur at a fixed point: some positive field endorses everything localised at one given boundary point.
- **Checks (CHECKED, exact finite cells).**
  - Two independent implementations; the referee's covers 75 configurations up to 1,024 models, including a precise band l = u. No cycles, no competitiveness failures, no dominated selected model, and a deliberately invalid family is caught.
  - The same verdict ungated: 730,964 (TC) violations.

### 8.3 What this does and does not show
- **The two-world laboratory no longer discriminates.** Any continuous verdict passes. So success here says nothing about which verdicts can work for T1.
- **New screen S10 (strong gates in three worlds; PROVED in the stated form).** Suppose each world compares only pairs separated in a fixed priority order. At an interior index, if every world has a "crossed pair" for C_p (on disjoint problems), then C_p is not competitive. So every interior selected model must be a threshold set at some world. Threshold sets of one order are nested, and nested coherent models form one-dimensional chains.
- **CONJECTURE.** Fixed-order gates are excluded in three worlds altogether. The gap: nothing yet shows that (S) forces a two-dimensional image. If the selection is continuous in measure along the chains, a winding argument should finish it (the boundary of the simplex would have to wind around the loop the three chains form), but this is not written out.
- **Triangle condition (PROVED, one reader, assuming the selected models' step sets cross cyclically in both orientations).** With a ratio rule "added ≥ ρ·removed" on two-point swaps, (TC) requires both triangle products to be at least 1. The sticky rule ρ = 1/2 fails this.
  - So in three worlds the sticky direction cannot sit in small swaps around such triangles. Spreads in the other direction (ρ ≥ 1) are triangle-safe.
  - The spread zones must be defended at another world.

### 8.4 Next design questions
1. Done: the two-world theorem and instance were refereed (REFEREE_gate2d.md).
2. Three-world gates that are not one fixed order:
   - (a) priority orders chosen from the disagreement itself, with (TC) checked directly;
   - (b) envelopes with a bid–ask spread on swaps.
   Screen both against FF2 Thm 4.1, S3, S9 and S10 before any proving round.
3. Check whether the five-region patterns can be added to a gated system as closed exceptional sets. In principle they can, if each pattern passes the gate; A and B are not nested, so the patterns must be re-sited on a nested family.

### 8.5 Round 36: the weak gate in three worlds (20 October, afternoon)
- **Audit's extensions (refereed, repairs incorporated in the note).**
  - **Coordinated verdict** (α = 2 below t = 1/2, 1/2 above). It makes each world's non-additive defences indispensable, in the sense that the other world's own verdict refuses them. Non-endorsement needs records of mass ratio 3/2 rather than 2. It holds across a dense set of selected models; out of any single selected model a positive field endorses everything.
  - **Weak gate** (ess inf of added steps < ess inf of removed steps). The two-world theorem holds verbatim.
  - **Three-world count.** Σ off_i ≤ 2 Σ on_i, sharp, out of a model that is regular on mixed problems and correct on unanimous ones.
- **New screen S11: fixed-key gates are excluded in three worlds (PROVED, PP2 Thm 6; one referee, REFEREE_PP2.md).**
  - **Statement.** Suppose world 1 compares only pairs passing a weak gate for a fixed key, and that key is not essentially constant on the level-1 steps of the problems cutting off e1. Suppose worlds 2 and 3 satisfy strict (G). Then (S) with closed sections fails, for any verdicts, any selection and any target.
  - **Why.** KKM forces two families of world-1 threshold models to be selected, on the edges [e1,e2] and [e1,e3]. Their thresholds force the key to be constant.
  - **What it settles.** This proves the S10 CONJECTURE (strong gates are a special case). It also covers tie-broken keys (referee's R1).
  - **What survives (referee's R2, sketch).** A surviving fixed key must be essentially constant on all mixed level-1 steps. All the content then sits in a record-based secondary rule, so this route reduces to (a).
- **Construction side (PP1).**
  - **PROVED.** A shared problem order fails for every verdict. Mass-sensitive verdicts (sticky, coordinated, additive-type) fail with any keys once two selected credal sets are crossed: small triangles and hexagons both are.
  - **Partial positive result (PROVED).** Keys = "largest p_w of a selected model still having the step" give competitiveness and KKM dominators for rivals with ψ₁+ψ₂+ψ₃ < 1.
  - **NUMERICS.** SAT searches find no key orders satisfying competitiveness and dominators together on 6–8 line arrangements, even with the most permissive verdict.
- **Consequence.** In three worlds the priority order cannot be fixed. Only route (a) remains open: orders chosen from the disagreement itself. Its no-cycle guarantee is lost, so (TC) must be designed directly. PP1's exact SAT harness can screen such rules.

### 8.6 Round 37: designing for (TC) itself (20 October, evening; unrefereed)
- **Audit's proposal: triple-local certificates.** For every three models, some strictly guiding additive evaluator supports the world's comparisons among them. This gives (TC) at once, and audit's 5-region example shows that longer non-additive cycles are allowed.
  - **Lead's check (CHECKED).** The example survives (IB) propagation: all 32 models, 0 (TC) violations, and a certificate for every one of the 4,210 triples that have comparisons.
- **The certificates are exactly (TC) (PROVED twice, independently: PP4 Thm 1 and PP3 §2, at the level of measures).** Under strict (G), including its weak half, a triple has a certificate iff (TC) holds on it. Certificates on four or more models are strictly stronger.
  - So every screen that uses only (TC) binds certificate designs unchanged: the triangle condition, S8, S9, Screen B/C.
  - Two screens neither bind them nor are escaped by them. S3 does not, because the triple evaluators need not form a finite committee. FF2 Thm 4.1 does not, because it needs one field for all comparisons.
- **Small swaps (PP4, PROVED).** On two-point swaps, (TC) imposes exactly three conditions:
  - no hysteresis;
  - every 3-cycle sum is non-negative;
  - a 3-cycle with sum zero has reciprocal pairs.
  - **Three locations.** Up to three locations, a mass-based, scale-free, monotone verdict built from finitely many linear tests is endorsed by one positive potential.
  - **Four locations.** Here a (TC) world exists with a strict 4-cycle out of selected models and no integrable endorser. The monotone version of that world is only CHECKED.
- **Three worlds near the target (PP4, PROVED).** Suppose the minority world keeps strict spreads on its own class of problems. Then the two majority worlds must carry opposite total orders on that class: the two-world gate structure again, in the place S11 does not reach.
  - PP4's candidate scheme Σ_loc already has a proved gap: same-class records with nested key ranges are refused at both majority worlds.
- **Most-permissive solver screen (PP3, NUMERICS).** No gates, keys or formulas: any record-based verdicts with strict (G), (TC), support clause, KKM dominators and undominatedness.
  - **Results.** 14 of PP1's 19 arrangements are SAT, and on every one of them a plain additive ranking works. 2 defeat additive rankings and are undecided for free verdicts. 3 are undecided.
  - **PROVED: finite cells cannot discriminate.** On atoms, competitiveness does not force Bayes-ness, so additive rules pass. In any atomless refinement they fail (FF2 Thm 4.1).
  - **Consequence.** PP1's UNSAT results were failures of fixed keys and gates, not of the axioms. Any future finite screen needs fractional rivals near each line and split models.
- **Net position.**
  - **(TC) itself is not the bottleneck.** No finite obstruction to (TC) designs is known.
  - **The constraint is (S) in the atomless setting.** Non-additivity of small records must sit on at least four locations, or in infinite chains. Near the target it must be carried by opposite majority-world orders.

### 8.7 Round 38: the allocation problem (20–21 October; unrefereed)
- **Audit's plan.**
  - **Family:** K_p = p + 3ε min_j p_j (Δ − u).
  - **Anchor sets:** A(d) = the indices whose model agrees with the base on the disagreement.
  - **Exact defence clause:** if A(d) meets face I, the record must be accepted at a world in I.
  - **Pool:** Φ_i = 2ν(added) − ν(removed).
  - **Lead's reading.** With priority orders chosen per record, the gate is idle. The design is an allocation of worlds to records, and (TC) must be imposed on it directly.
- **PP5: the diagnostic and the repair.**
  - **Audit's greedy rule fails (CHECKED).** The triple was certified exactly, with two independent computations at interval width below 10⁻³⁵. Anchor sets are single points. C_c beats C_a pointwise at world 1 (PROVED). The greedy rule fails on whole regions near e₁ (NUMERICS).
  - **Audit's local repair (CHECKED: it creates new violations).** It moves the first record to world 3 and the second to world 2. Removing world 1 makes the reverse direction strict there, and new (TC) violations appear at every radius.
  - **AF ("additive first": accept wherever the additive balance is ≥ 0, use the sticky test only when no world's is).** Among selected models near e₁ it reduces to ordering by expected rank, and no violations appeared (NUMERICS; PROVED given that).
  - **With rivals it fails (PROVED).** At every interior index and world, some rival records are forced onto a single world. (TC) then requires that world to refuse every "return" record into the source's improvement cone at that world. An exact instance violates (TC) under both AF and greedy. The return is eligible at the other worlds, so this is slack, not impossibility.
- **PP6: the selected-to-selected layer.**
  - **Not obstructed.** Plain additive acceptance (ν(P_i) ≥ ν(Q_i)) passes every requirement. This is PROVED given (AC): no selected model is additively Pareto-dominated by another. (AC) is PROVED on the boundary, NUMERICS in the interior, and CONJECTURE in general.
  - **Infinitesimal shape lemma (PROVED).** For small triangles, (TC) holds iff each world's accepted directions lie in a closed half-circle (order-like) or are symmetric (reciprocal).
  - **Grids (CHECKED).** Six grids are SAT. Strict 4-cycles are realizable at every world. The greedy rule's minimal core is two world-1 links that compose to a strict improvement along [e1,e3].
- **Consequences.**
  - The selected-to-selected layer does not discriminate, since the additive rule passes it and FF2 excludes that rule for the whole system.
  - The decisive test is mixed triples (C_q, C_p, X) with spliced rivals X. In particular: closed refusal of the "return" records that PP5 shows (TC) forces, compatible with the face obligations.

### 8.8 Round 39: optional defenders and mixed triples (21 October)
- **Audit's note** *Optional Defenders and Symmetric Repairs* (refereed: REFEREE_optional_defenders.md; every item CONFIRMED).
  - **Theorem 2.** No genuinely mixed defence is uniquely forced by (G) plus the defence clause.
  - **Theorem 3, sharp.** For κ ≥ 3 the pool κν(added) − ν(removed) gives two eligible interior defenders, with margin (κ−3)/4·μ(D).
  - **Theorem 4.** Deleting a record together with its reverse cannot create a new (TC) violation.
  - **The referee's strengthening (PROVED).** For κ ≥ 3 every record has two eligible worlds, or one eligible world that is additively safe. So forced sticky records occur exactly when κ < 3.
  - **Edge version (PROVED, sharp).** Coverage holds for κ ≥ 1. Two eligible edge defenders are never guaranteed, but a sole one is always additively safe. Vertex defences are guidance.
- **PP7: mixed triples (unrefereed). Additive-first + Φ⁴ + symmetric thinning fails at every interior selected model.**
  - **Pair step (PROVED).** Suppose a rival Y additively dominates C_q. Then additive-first accepts the reverse of the defence at every world, so the defence of C_q is a tie wherever it is made.
  - **Antichain argument (PROVED).** Take nested sticky rivals on one C_p. Ties at one world combined with guidance between the rivals violate (TC), and guidance cannot be thinned. So each world's defended rivals form an antichain; three null antichains cannot cover an open box of rivals. This holds at every interior p, for every ε, at arbitrarily small scale.
  - **Second mechanism (PROVED given a NUMERICS hypothesis on ∇L).** Ties through many selected models.
  - **Configurations that cannot be repaired (CHECKED, exact SAT over all reachable thinning states).**
    - one selected model plus 6 nested sticky rivals;
    - one rival plus 14–15 selected models;
    - two selected models plus 6–8 rivals.
  - **Non-additive defences are compulsory.** A purely additive rule leaves C_q dominated by Y. Under additive-first those defences are ties, and the ties break (TC).
- **Proposed shift: "sticky-strict".** At the defending world, refuse the additive reverse, so the sticky defence becomes strict.
  - **NUMERICS.** SAT on every configuration that additive-first fails. Solutions re-check with no violations and no ties, and each world gives each rival its own value above its additive loss.
  - **OPEN.**
    - closedness at the boundary of the sticky region;
    - a record-level rule for the refusals it needs;
    - screens S9, PP4 (P), FF2 Cor 4.3.

### 8.9 Round 40: audit's joint-defence rule with weakest-pair deletion (21 October; unrefereed, two independent attacks)
- **The rule.** Both directions of a disagreement are chosen jointly, among 64 states, with strict defences preferred. Then, in one simultaneous pass, the lowest-priority removable pair of every violating triple is deleted in both directions.
  - **What it secures.** (G), (IB) and (TC); for (TC), via symmetric deletion.
- **The positive result (PROVED, PP9).** No violating triple consists only of protected (s=1) pairs and guidance. So protected defences are never deleted. Audit's §6 worry (all protected defenders of one record deleted) cannot occur.
- **Failure 1: defence clause (CHECKED in all four settings, independently in PP8 and PP9; mechanism PROVED in PP8).**
  - **Setup.** Let Y beat C_a additively at every world, with Y's disagreement also realised out of another selected C_q. Then the reverse is anchored, so the forward record is unprotected (s=0).
  - **Single defence.** The joint choice gives C_a a single defence, at one world j*. That defence is additively unsafe, so its priority is m < 3/2.
  - **Deletion.** Let Z = C_a improved at j* on a tiny cone. The triangle C_a ⪯ Y ⪯ Z ≺ C_a deletes the defence, which leaves the record accepted at no world.
  - **An edge variant also exists.** The defence of an edge-anchored reverse is deleted, and C_p's protected defence leaves only world 3.
  - PP7's certified pools survive (NUMERICS). The failure is specific to dominating rivals with an anchored reverse.
- **Failure 2: sections (CHECKED; PROVED in PP9 from checked data).**
  - The deletion set is not open.
  - For a fixed rival there is a path of protected (never-deleted) records whose limit lies on the boundary b₁ = 0, where it is unprotected and deleted. So {p : C_p R_i X} is not closed.
  - The initial choice R⁰ is itself not closed at exact ties.
- **Nearby patches (PP8, PP9).** Each moves the failure:
  - protecting every additively dominated defence loses edge-anchored returns;
  - allowing ties is worse;
  - protecting sole initial covers lets one triangle delete both initial defenders of a selected-to-selected record;
  - protecting the closed class breaks PP9's main theorem.
- **Proposed shift (PP8).** Keep the joint choice, but replace one-shot lowest-priority deletion by deletion constrained to leave every face obligation a defender (a SAT problem on pools). A closed record-level version is open.
- **Pattern across rounds 38–40.** Every one-shot or greedy allocation fails on the same object: a dominating rival whose reverse is also anchored, so that it is explained by a nearby selected model. Its defences are additively unsafe, so they lose any priority based on margin. And the boundary of "strictly dominated" is where sections stop being closed.

### 8.10 Round 41: the coupled module (21 October; Theorem J refereed once)
- **Audit's diagnosis (CHECKED by the lead).** PP9's protected defences are all endorsed by one fixed lexicographic additive ranking, (J_i, E_i): first errors on the minority class M_i, then total errors. This follows from the pointwise identity δ_j + δ_k + 2·1_{M_i}δ_i ≥ 0.
  - Mirror rivals Y_plus (majority advice on silent patches) and Y_minus (minority advice) are favoured by E and by J respectively, at every world.
- **Construction side (PP10; unrefereed).** No rule meets the whole module.
  - **R_VE.** It accepts by V_i = E_i + J_i where V covers interior faces, and falls back to E on edges.
  - **What R_VE secures (PROVED):** (G), (IB), closed sections, and every face obligation on the full domain.
  - **What it fails:** (TC) where an E-link meets a V-link (instance CHECKED); direct (C) on the balanced Y_plus; undominatedness at edge balance.
  - **Not a new mechanism.** Every acceptance is endorsed by V or by E.
  - **Theorem C (PROVED).** No fixed positive field per world serves.
  - **Theorem D (PROVED, inputs CHECKED).** On the balanced majority rival, world 3 must refuse along the path toward e₃. So world 1 or 2 must accept, although additive scoring refuses at both.
- **Obstruction side (PP11; Theorem J refereed: REFEREE_PP11.md).**
  - **No contradiction from the axioms on the module (CHECKED, exact solver, four settings).** 312 comparisons are forced, all by closed sections.
  - **Theorem J (PROVED; CONFIRMED by the referee).**
    - *Setup.* Take a silent interior selected C_a, and an edge model C_r saying A on a two-class majority pattern. Such patterns exist at every interior index, every ε and every edge.
    - *Exactly one world.* Each record rec(X_λ, C_a) is accepted at exactly one of the two edge worlds. At least one comes from the face obligation; not both, because the third world accepts by guidance and C_a would be dominated.
    - *Cut.* With (TC), the defending world switches at a single cut λ₀.
  - **J1 (CONFIRMED WITH REPAIR).** Under Theorem J's hypotheses (three worlds, a silent interior selected model, an edge model saying A on the pattern), no system satisfying (G), the face obligations and undominatedness has accepted-record sets closed in the rival argument.
    - J1 needs neither (TC) nor closed sections.
    - Unqualified it is false: additive Bayes systems with precise interior selections are closed.
    - In two worlds it fails too: gate2d is closed, because nothing anchors the pattern there and there is no third world.
    - At least two of the three worlds' accepted sets fail to be closed.
  - **Consequence (corrected in §8.11).** For selections with strictly nested edge windows, such as the homothetic family, accepted comparisons must jump as the rival varies, exactly at a cut the axioms force. This does not hold for the rescaled family. That excludes every closed rule tried in rounds 38–40: AF, Φ^κ-eligibility, audit's §6 greedy rule, and the anchor plan's closed-R_i target.
  - **Referee's prediction.** The §6 rule must leave some interior C_a dominated; the explicit λ is not computed.
- **Next design target.** Rules closed along fixed-rival sections, discontinuous across rivals at forced cuts, and incomplete where closed-section refusals require it.

### 8.11 Round 42: the rescaled (posterior) family (21 October; unrefereed)
- **Family.** K_p = {p∘m/(p·m) : m ∈ M}, with M = c·1 + εΔ (author's rescaling note). For interior p, C_p = T1∘S_p with S_p(g) = p∘g (PROVED, CHECKED); edges are further orbits and vertices are fixed points.
- **Equivariance fails (PP12, Theorem E, PROVED).** No ranking system invariant under positive diagonal maps works.
  - *Rival.* Λ: majority orientation on every mixed problem, correct on unanimous ones. Λ is fixed by every diagonal map.
  - *Argument.* Under invariance its interior sections are empty or everything, so closed sections push the defence to the vertex models, where strict (G) refuses it.
  - *Extent.* Invariance under one non-scalar map already fails, and the two-world analogue fails too. Round 26's equivariant systems (X2) fall to this.
  - *Survivor.* Local invariance, imposed only on records bounded away from the coordinate planes. It never touches sections. Under (TC), complete, additive and lexicographic local rules are still excluded (Theorem L). OPEN whether any locally invariant (TC) system exists.
- **No forced cuts on this family (PP14, PROVED; CHECKED).**
  - *Translation lemma.* Projected onto an edge (ratio x_j/x_i), every member's credal set is a translate of one interval, and translates are never strictly nested. So Theorem J's hypotheses fail at every index, every edge, every ε.
  - *Contrast.* The homothetic family is strictly nested everywhere (129/129). Correct §8.10 accordingly: J1 applies to nested-window selections, not to this family. Audit's closed construction fails here because of the split-cell rival, not because of J1.
  - *Theorem N.* Accepting exactly where guidance accepts meets every face obligation, undominatedness and direct (C) whenever guidance decides a world.
  - *Consequence.* Closed accepted-record sets are not excluded for this family (OPEN).
  - *Scope.* These are properties of the selection, holding for any rescaled family of a credal set inside the simplex.
  - *Gated variants.* PP2-type weak gates would need the log-odds translation keys, chosen per edge.
- **Repairs (PP13).**
  - **Certificate inside the family (PROVED for every ε; CHECKED exactly at ε = 3/10, 1/10).** Four selected models, including T1, reproduce audit's four-defence non-additivity certificate. The defences are indispensable in audit's ranking, not forced by the axioms.
  - **Repair lemma.**
    - Condition (a), no guidance obstruction, always holds on a nonempty open set of indices (PROVED, open KKM).
    - Exposure is PROVED near a vertex index for broad classes: coherent rivals, local modifications, edge, vertex and certificate rivals. It is CHECKED for 15 named rivals, and OPEN for arbitrary measurable rivals.
    - The working indices are far from the rival.
  - **(TC) fails for repair records (CHECKED exactly).** Two repairs plus a guidance link give a forbidden triangle, at every world. *Mechanism:* each silent band has bounded width, so an exposed new side can contain a sub-pattern of another selected model.
    - *Axiom-level corollary (PROVED).* The dominators of tiny patches cannot all be local.
    - *One-directional repairs (PROVED).* Add-only or remove-only repair classes satisfy (TC), but do not cover.
  - **PP8's doubly anchored rival does not exist in this family** (no three-class pump; PROVED).
- **Position after round 42.**
  - The rescaled family escapes the forced-cut obstruction and the PP8 pump that defeated rounds 38–41's rules.
  - The live problem is coordinating mixed repairs across rivals so that (TC) survives.
  - PP13's suggested first test: an exact SAT search on the three-cone module.

### 8.12 Round 43: audit's guard construction (21–22 October; one referee for the construction, PP15/PP16 unrefereed)
- **Audit's construction.** Three guards G_i, where T gives the minority-i answer. Defenders D_K are taken near the vertices. Repairs C ⪯_w X are installed at every world for guard-preserving rivals, subject to the exposure filters (E_T) and (E_C). The base is target-referenced: from T, any worsening at world i, off the guards, is accepted at i.
- **Referee (REFEREE_guard.md).**
  - **CONFIRMED:**
    - the guard (TC) engine: no 2- or 3-cycle passes through a repair, for any subcollection;
    - Lemma 3, the co-designed defenders, and non-additivity (infinite obstruction);
    - direct (C), in the stronger form that there are no distinct ties even at one world.
  - **WRONG.**
    - *F1.* "Further extension open" is false. A forced repair by C₃ makes T indefensible against C₃: (TC) blocks worlds 1 and 2, strict (G) blocks world 3. So (S) with T selected is impossible.
    - *F2.* (E_C) is not a safeguard; the trap returns through (IB) copies.
- **PP16: Theorem B (PROVED; CHECKED).** One-class rivals (majority on a cone where T is not A but every 2-/3-defender is) force a 1-defender repair. T then loses to Y_C at every world: strict (G) at world 1, a (TC) triangle at worlds 2 and 3.
  - This uses only strict (G), (IB) and (TC). No selection containing T works, plateau designs included.
  - *Couplings.* Every other selected model is isolated from T. Tilt continua reaching a vertex dominate T. The modified edge verdict Ψ_w = min(Φ_w, Φ_w − Φ_other) keeps the two-world edge system and refuses the records that would kill T's defences.
  - *Screen.* Dominate one-class rivals by models on the opposite edge.
- **PP15: guard-changing rivals.**
  - **§13's Y.** It is defensible after one more filter, (F₃) (PROVED; CHECKED).
  - **Theorem C (PROVED).** A classification of all 2- and 3-cycles.
  - **Theorem P (PROVED; CHECKED).** The extended rule covers every guard-changing rival outside a residual class 𝒵:
    - accept target-referenced records that change T on G_w and either convert neither other guard fully, or are weakly worse off the guards;
    - add filter (F*).
  - **Theorem O (PROVED; CHECKED).** For the X_F rivals the guards force a 3-defender C, pointwise no worse than T at world 3. T then has no defence against Y_C in any extension with (G) and (TC). This is stronger than F1: concentrated pools cannot escape it.
    - *Only escape:* a continuum of intermediate selected models straddling every cut m₃ = θ, θ ∈ (c, c+ε).
  - **KKM.** Concentrated defenders cannot dominate pure two-guard changes. An intermediate e₃-tilt can (CHECKED on cells) but conflicts with the type-(i) defences.
- **Position.**
  - The guard architecture with T selected is closed: F1, Theorem B and Theorem O agree.
  - Live directions:
    - (a) an intermediate defender continuum straddling the cuts of Theorem O;
    - (b) T unselected but tied with a selected model;
    - (c) opposite-edge dominators for one-class rivals.

### 8.13 Round 44: reciprocal source protection and (S) (22 October; PP17 is a referee report; PP18 checked by the lead; PP19 unrefereed)
- **Audit's six-source extension** (AUDIT_six_source.md §§9–14).
  - Three coherent groups {C_i, F_i}, with reciprocal source defences installed before the repairs. Every rival that changes T on A_1–A_3, B_1–B_3 is dominated at all worlds.
  - (TC) is protected by sets R_i on which group i alone gives the correct majority answer.
  - Non-endorsement: δ = L_i(C_i) − L_i(F_i) ≤ ν(E_n) for infinitely many disjoint E_n.
- **Referee PP17 (REFEREE_six_source.md).**
  - **Audit's theorem: CONFIRMED,** with four presentational repairs:
    - R1: fix d once.
    - R2: non-installation proved by identifying records.
    - R3: name the endorser class (finite, finitely additive, positive rank-step charges).
    - R4: list "F_i no worse than C_i at world i" among the conditions used.
  - Signs are PROVED for every 0 < ε < 1 and CHECKED exactly. An independent record-algebra check found nothing.
  - **NEW GAP.** In the module as built, T has no defence at any world against many rivals in its own class, e.g. X* = T[A_1 ∪ A_2 → majority].
    - Adding T ⪯_w X at every world where X worsens T fails through an (IB) copy.
    - Adding it at one world passes all finite checks; there is no measurable proof.
- **Lead's note (LEAD_selection_count.md; PP17: correct, wording repaired).**
  - Tie fibres Φ_M = {p : C_p ≈ M} are closed.
  - C_{e_i} = V_i, and V_i has no ties.
  - **Theorem C:**
    - (i) (S) never holds with finitely many selected models;
    - (ii) with no all-world ties, fibres are closed and the selection is uncountable (Sierpiński);
    - (iii) countably many, with an infinite tie component whose index set is not closed: OPEN; closedness facts alone cannot settle it.
  - Lemma D: private protection sets serve only countably many groups.
  - Lemma E: Φ_T is compact in the open simplex (it suffices that T is undominated).
- **PP18: Theorem Z (PROVED; lead checked; not yet independently refereed).**
  - Call a set P a *correctness zone* at w if no accepted comparison makes world-w advice correct on a non-null part of P.
  - Under (IB), strict (G), (S) and direct (C), every correctness zone lies in the unanimous problems.
  - Proof:
    - fill a vertex model V_j with the w-correct answer on a small set Q;
    - it becomes incoherent (Lemma R, rigidity);
    - KKM gives a selected strict dominator;
    - exposure (Lemma Z0) forces that dominator to make advice correct on part of Q.
  - No (TC) and no T1 are used.
  - **Consequences:**
    - Audit's R_i protection (any witness geometry, any number of sources) is incompatible with (S).
    - While the R_i protect, no model dominates a fill of T inside them (Cor 2.1).
    - In audit's pattern T has no defence against Λ_T, against the precise uniform model (which is coherent), or against T[R_1 ∪ R_2 → majority].
    - Every competitive model is correct on some world's zone (Prop 4.1).
    - Protection by integrated charges must be exactly balanced on T's silence (Prop 4.3).
  - **Survives:** *error zones* (no accepted comparison removes an error there).
    - On them, accepted comparisons respect inclusion of error sets (5.2), a key-like order that still has to be tested against PP2 Thm 6.
    - Audit's W_ij are natural error zones.
    - T's clean world must be handled by composition control alone (5.3).
- **PP19: necessary conditions near T (PROVED; unrefereed).**
  - *Theorem 1.* For each fixed rival there is a neighbourhood of Φ_T in which selected models are competitive only at worlds where the rival does not improve T.
  - *Theorem 4.* Dominators of rivals improving T at worlds i and j fall into three disjoint classes. Each is at positive distance from Φ_T, and T defends against each only at world k.
  - *Theorem 5 (compensation necessity).* Every dominator of a majority fill on E must, off E, beat T at a majority world somewhere world k does not. So compensation sets like B_i and R_i are forced.
  - *Theorem 7.* Audit's discontinuity is forced and is compatible with closed sections.
  - *Prop 9.* T must refuse "T with part of C's advice" at some world for each selected C. This supports the one-world target-reference fix.
  - *Prop 10.* T and the sources have a consistent local skeleton.
  - The tie route (b) remains open.
- **Position after round 44.**
  - Compensation is forced (PP19 Thm 5), but it cannot be protected by correctness zones (PP18 Thm Z).
  - The remaining protection mechanisms are:
    - error zones, which need a PP2-type KKM test first;
    - pure composition control: every permitted composition nets to a guidance-worsening at its world (audit's a/b cancellation).
  - T's defence against fills of its own silence on the compensation sets is now the binding requirement.

### 8.14 Round 45: completing comparisons instead of protecting regions (22 October; PP22 is a referee report; PP20, PP21 unrefereed)
- **Audit's closure framework (AUDIT_completion.md; lead checked).**
  - For a reflexive relation, (TC) holds exactly when every accepted triangle has all three reverses.
  - The least closure under the four rules:
    - I: (IB) copies;
    - II: triangle completion;
    - III: protection of registered models;
    - IV: propagation through all-world ties.
  - If the closure has neither failure, then (G), (IB), (TC) and (LA) hold, and the registered models are coherent and undominated. The failures are:
    - F1: a strict guidance comparison is reversed;
    - F2: an incoherent model is registered.
  - F1 and F2 are genuine obstructions.
  - Under a completed (S), the KKM argument makes P exactly the undominated class.
- **Referee PP22 (REFEREE_Z_PP19.md).**
  - Theorem Z and Lemma R: CONFIRMED.
  - Audit's homogeneity proof of Lemma R is valid.
  - **Lemma H (PROVED):** a model differing from a coherent model on a set that is not a.e. a cone is incoherent. This is sharp.
  - PP19 is mostly correct, with two claims WRONG:
    - "Sharing within a class is unconstrained" is wrong. The correct statement is **Prop S (PROVED):** defenders serving rivals that harm different worlds have jointly constrained compensation.
    - The "non-monotone acceptance" claim in Theorem 7(b) is wrong.
  - Three PP19 results needed stated hypotheses: no all-world ties, the strict source pattern, or T selected.
  - Every PP19 obstruction closes with a strict guidance link. So completion cannot rescue them; doing so would be F1.
- **PP21: exact closure engine on cells (CHECKED; cells are conic only).**
  - On cells, the whole joint class closes cleanly, for every defender order and every choice of T's defence worlds. Ties never rescued a failing choice.
  - Minimal failures use 2 requests, or 4 with ties. Their shapes:
    - a two-link F1 (a defence of T composed with a defender copy);
    - exposure onto another protected model, giving F2;
    - a tie triangle whose completion produces a two-link F1.
  - What separates good defenders from bad: T must defend against the defenders' own partial sources (Prop S).
  - **Lemma Q (PROVED):** for a k-corner cut D_K, every new answer is wrong at world k. So T beats D_K and all its partial sources at k by guidance.
- **PP20: a measurable extension (PROVED; unrefereed).**
  - **Lemma 1.3.** Completion can tie only three mixed comparisons. Any triangle with a guidance link is degenerate or F1.
  - **Theorem 3.2.** The defenders are three coarsenings C_w = D_{conv(M ∪ {q_w})}, silent wherever T is silent, with compensation on T's answered region (their "footprints"). The installed comparisons are:
    - T ⪯_w C_w;
    - C_{w(X)} ⪯ X at all worlds;
    - T ⪯_w X at each non-improving world.

    Result: for every rival equal to T off T's silent set (every measurable fill, including the old A, B, R regions, X*, Y_12, Λ_T and V_{c*}):
    - the closure is clean;
    - there are no triangles and no ties;
    - every rival is strictly dominated at every world;
    - no finite positive additive charge endorses the relation.
  - **Theorem 4.3.** T is competitive against every model; the cascades have PP19 Lemma 5.0's shape and can always be avoided at some world.
  - **Prop 5.1 (where the difficulty went).** No domination makes advice correct on the footprints. Theorem Z therefore forces any (S)-extension to dominate rivals that change T on the footprints, where Lemma 5.0, Theorems 5–6 and Prop S bite.
  - **Cells (CHECKED).** One design dominates every incoherent model (588 of 729) while T defends against all 729. Getting this required ordering one recurring family of leftover models first.
  - **Conjecture 6.1.** There is a clean closure in which every incoherent model is strictly dominated by an undominated coherent model, with footprint-rival dominators chosen per rival.
- **Position after round 45.**
  - Every rival that changes T only where T is silent is handled measurably, with T competitive against every model and no protected region in the proof's statement.
  - The joint class was a weak test, because coarsenings carry compensation outside T's silence.
  - The live problem is rivals on the defenders' footprints:
    - Theorem-Z fills covering a footprint's errors;
    - T[F_w ∩ Err_u → silent];
    - whether rival-dependent coarsening triples can share footprints while each defender still loses to T at its own world outside the other footprints.
  - Selection and closed sections come after that.

### 8.15 Round 46: local defences for every selected model (22 October; all unrefereed; referee running)
- **Audit (AUDIT_local_defences.md; lead checked Prop 1).**
  - *Prop 1.* Consider a relation whose only non-guidance records either have T as old side or have unbounded support. In it, every model other than T and V_1, V_2, V_3 fails competitiveness against a bounded rival.
  - So PP20's competitive models are exactly {T, V_1, V_2, V_3}, and no selection makes PP20 satisfy (S).
  - The missing ingredient: defenders need their own local defence rules, co-designed with their geometry.
- **Lead's observations (Brief 46):**
  - uniformity of local defences comes free from (IB);
  - triangle lemma: every triangle has 0, 2 or 3 unbounded edges;
  - departures;
  - the departure–retreat pump;
  - region structure.
- **PP26: regional lift.**
  - **Correction to the lead.** A region M_k is a one-parameter family of two-world problems (pencils through the extended opposite edge), not one such problem.
  - **Theorem V.** A veto region at any world kills (S). The witness is the rival (B on M_i, B on M_j, A on M_k).
    - Consequently AND, lexicographic-by-region and every region-sign rule fail (Theorem M).
    - Linear region-constant weights collapse to additive endorsement (Theorem R).
  - **Theorem C.** A one-parameter chain (homotheties of T1 toward e_1) with full competitiveness against every model, no cycles, and no integrable endorser.
  - **Conjecture.** Regionally nested families are at most one-dimensional.
- **PP24: two-model test, uniform in a parameter.** Passed with T-priority fixed gates on three one-parameter paths:
  - full competitiveness against every model, no cycles, non-endorsed local defences;
  - but excluded for (S) by PP2 Thm 6, so the test is non-discriminating.
  - The members' own footprint rivals are undominated (Prop 6.5).
  - Possible escape: tie T's steps on each world's vertex class (§7.5, conjecture).
- **PP25: adversary.**
  - **Theorem A.** A uniform-weight balanced additive rule on bounded records (ρ = 2 on one's own minority class) with lexicographic tie-breaks gives every coherent model strict local defences.
  - (a)+(b) cannot be obstructed by the local layer. Any obstruction lies in the choice of dominators:
    - Theorem B: local defences and dominations decouple if dominators beat the member somewhere at every world;
    - Theorem C: (TC) holds iff there is no triangle of two dominations plus guidance, and such triangles need a "shadow" (Lemma 6).
- **PP23: local rule.**
  - **Ω (Theorem 3.1).** Lexicographic integrals, own minority class counted twice. Every regular model is competitive against every rival; each world is a linear order. But:
    - there is no room for dominations (Prop 3.2);
    - Ω is endorsed by an integrable field, hence excluded by FF2 Thm 4.1 *for selections continuous in measure* (Prop 3.3). Lead's note: (S) does not require that continuity.
  - **Departures.** They satisfy (TC) (Theorem 2.1), but a world accepting all departures blocks retreats there. So every interior coherent model is dominated by its own partial retreat (Cor 2.4).
  - **Room reduction (Theorem 4.5).** Inverted departures (silence → A on higher lines, B on lower lines of one class) never pump with coherent-realizable old sides. Room for them at every world is equivalent to a splitting condition (iii) on the covering part.
    - Full Ω violates (iii); B-heavy cases fail over any Ω-subset (Props 4.6–4.7).
    - Cells satisfy (iii) (Prop 4.8).
    - The A-heavy continuum case is Conjecture 4.9. If true, the local rule is not endorsed by any integrable field.
- **Lead's synthesis.**
  - **Balance identity.** If at every tie-break level the three world scores sum to zero, then every model is competitive and no record is accepted at all three worlds. Competitiveness-for-all and room for dominations pull in opposite directions through this identity.
  - **Room must come from records that certify incoherence:** inverted departures (PP23), dominators that beat the member everywhere with no shadows (PP25), or the members' footprint rivals (PP24).
  - **The two-model test is non-discriminating.** The discriminating targets are:
    - a two-dimensional family;
    - room for dominations of the members' own rivals;
    - escaping FF2 (or showing its continuity hypothesis is not forced by (S)).
- **Referee of round 46 (REFEREE_round46.md).**
  - **R46.1 (PROVED, new).** Ω-type balanced rules are incompatible with (S) with no continuity assumption.
    - FF2's Step 1 forces edge-selected models to be vertex models.
    - Closed sections for the rival D_[e_i,e_j] then contradict strict (G) by a one-dimensional KKM step.
    - Consequence: in any (S)-system the non-additive acceptances must occur out of edge-selected models, at that edge's own worlds.
  - **PP26:** Theorems V, M, C and R(i)–(ii) are correct. R(iii) needs a capacity hypothesis and (IB), and does not cover every local comparison.
  - **PP23:**
    - departures and Ω (Theorems 2.1, 3.1) are correct; so are Lemma 4.4 and Theorem 4.5.
    - Props 4.6–4.7 are WRONG as stated. The counterexample is a B-part hugging the e_k corner. The repair adds three hypotheses: the B-part bounded away from the corner, steep padding lines, and enough padding mass.
    - Prop 4.8's cell evidence does not transfer to the continuum.
  - **PP25:** Theorem A needs the tie-break family to be a π-system (rational boxes are). Theorems B and C are correct. The last sentence of Lemma 6 is unproved.
  - **PP24:** correct. PP2 Thm 6 needs even less than PP24 says. The §7.5 escape is WRONG, already excluded by REFEREE_PP2's R1.

### 8.16 Round 47: selected-family co-design with incoherence certificates (22 October; unrefereed)
- **Audit (AUDIT_selected_realizability.md, AUDIT_answers47.md).**
  - R46.1 does not force non-additivity at the edges. The additive system L_i = ∫|g_i| r_i dμ with precise selections D_{p} satisfies (S); lead checked. Lead withdrew "build from the edges".
  - Defence obligations come only from selected realisations: A(r) ∩ supp p ≠ ∅ for p ∈ P(r).
  - A pointwise sweep does not give joint realisation (swap-symmetry counterexample).
  - T dominates its own inverted rivals.
- **PP28: co-design (PROVED unless stated).**
  - *Separation lemma.* If both pieces of a split of d⁻¹ have coherent realisers, those realisers have disjoint credal sets separated by a line of the class.
  - *Certificates sit cleanly on any (TC) base whose non-guidance acceptances have selected-realised old sides.*
    - (TC) holds iff no world accepts both pieces of a split.
    - No ties are added, no selected model is dominated, and closure forces nothing.
    - Certificate sections are base sections plus at most one fibre.
  - *Theorem 4.1.* If the non-vertex selected credal sets pairwise intersect, every inverted departure is accepted at every world.
    - Explicit instance: T plus segment models D_[m₀,p], with vertex models, over Ω.
    - It admits the repaired B-heavy adversary, dominated by T at all worlds.
    - Comparisons out of T are endorsed by no integrable field.
  - *Growth rule.* An intersecting newcomer is free. A separated pair must pass an exact cone test.
  - *Limits.*
    - Every (S)-system contains separated non-vertex pairs, because of the edges (Prop 6.1).
    - Ω cannot be the base at the edges.
    - Open: the base layer (E) near the boundary (Conjecture 6.5: join the additive edge system to an intersecting core).
- **PP29: adversary.**
  - Audit's strong forced-realisation theorem FAILS for single departures (Theorem 4.1).
    - The "retreat split": B-retreats are accepted at the owner world, A-retreats at the opponents.
    - It meets every support obligation; supports never collide.
  - Prop 4.7's obstruction rests on additivity at the opponent worlds, not on universal realisation (Theorem 5.1).
  - The escapes are classified.
    - The rule cannot be applied to all departures at once (Prop 6.2).
    - Sections need condition J_d.
  - Cells: every inverted departure can be accepted everywhere under the full axioms (SAT in all six configurations).
  - Real obstruction candidates: the *star* reduction, and domination-record-as-piece. The frontier is Conjecture 6.6.
- **PP30: surgery on the additive (S)-system.**
  - **Theorem 3.1 (PROVED; lead checked).** Use T's competitiveness against T[G → a] and copy it under (IB). Every model N with answers a on a piece G of Sil(T) has a world w with N[G → S] ⪯_w N. At w, N refuses every improved silencing.
  - **Theorem 3.2.** The additive system violates this for every precise model. So no (S)-system selecting T1 keeps S_0's comparisons for any precise model, vertices included.
  - Prop 3.4: an exact test for rank-weighted bases on Sil(T). Balanced weights pass; |g| weights fail.
  - Prop 4.2: dominators of the improved silencings differ from them on unbounded sets.
  - **Problem-space surgery (PROVED under keep-S_0-on-Ans(T)).**
    - Interior selected models are precise models or refinements D_K with K ⊆ M.
    - Edge models are precise models on their own edge.
    - Coarsenings cannot be selected.
    - The kept part decides no comparison between distinct selected models.
- **Lead's synthesis and conjecture (general additive barrier).**
  - If T is competitive under a base endorsed by fixed densities ρ_w, then by convexity T is λ-Bayes. So the base is balanced on Sil(T): λ_kρ_k = λ_iρ_i + λ_jρ_j on Sil(T) ∩ M_k, with all λ > 0 (cf. PP18 Prop 4.3).
  - A non-vertex edge model on [e_1,e_2] that is competitive under the same base is two-world Bayes. On Sil(T) ∩ M_1 its acceptance set is then both {ρ_2/ρ_1 < const} and a set of the ratio |g_1|/|g_2| alone.
  - Likewise for an edge model on [e_1,e_3], with |g_1|/|g_3|.
  - Balance makes ρ_3/ρ_1 an affine function of ρ_2/ρ_1. If the two edge models' thresholds meet inside T's silent band, an |g_1|/|g_2|-set must equal an |g_1|/|g_3|-set on an open region, which is impossible.
  - **CONJECTURE (general-field R46.1):** no fixed-density additive base can endorse the comparisons out of T and out of the edge-selected models. The missing step is showing that edge selections realise thresholds inside the band.
  - The non-additivity would then have to live in records on Sil(T) out of edge-adjacent models, or out of T.
- **Referee of round 47 (REFEREE_round47.md; all 10 author scripts reproduce).**
  - **PP28.** Correct: separation lemma, Thm 3.1, Lemma 3.4, Thm 4.1, Thm 5.1, Cor 5.1′, Cor 5.3, Prop 6.1. Thm 4.1 also settles PP29 Conj 6.6 for pairwise-intersecting selections.
    - Hidden hypothesis in §0: the base must itself be closed under I–IV.
    - Prop 3.3 needs undominatedness in the full system.
    - Prop 5.2's 2A/3A conditions are incomplete (exact counterexample), but "forcing iff crossed" stands.
    - **§4.2 instance FAILS closed sections** at the boundary of M (NUMERICS): a jump in the leading level.
    - It also leaves an incoherent undominated model (T silenced on a bounded part of Ans(T); PROVED).
    - The open edges are missing from the index set.
    - A continuous interpolation removes the jump at the boundary of M; the jumps at the vertices remain.
  - **PP29.** Thm 4.1 is correct and meets every support obligation, including from vertex and edge models (Lemma 3.3; referee's own cells: 0 failures in 474,384 decompositions). Thm 5.1 and Props 5.2, 6.2, 6.4 are correct.
    - Three rows of the escape classification overclaim. Not forced is shown only for supports, guidance and the vertex/edge structure. Whether x is realised is open (Prop 5.2 forces a trichotomy). σ's failure in the continuum rests on cells only.
    - Prop 6.1 needs joint padding capacity.
  - **PP30.** All listed claims are correct. Thm 3.2 was checked exactly (364 cases). Prop 4.2 needs T to be selected.
- **PP32: general additive barrier (PROVED; unrefereed).**
  - **Thm 3.1.** No single positive field endorses both the comparisons out of the models selected on [e_1,e_2] (at worlds 1 and 2) and T1's acceptances of majority fills of its silence.
    - Uses only strict (G) at worlds 1 and 2, closed sections for the one rival D_{(1/2,1/2,0)}, and T competitive. Endorsement is needed only on three bounded pieces of Sil(T).
    - Key new Lemma 2.2: every edge point lies in the credal set of some selected edge model.
    - The contradiction comes from a majority fill straddling the seam g_3 = 0.
  - The lead's four-quadrant step was invalid (Example 4.3: piecewise-constant ratios); it is replaced by the seam argument.
  - **Cor 3.3:** in any single-field-endorsed (S)-system, every selected model with credal set in int Δ is precise.
  - **Cor 5.2:** relative to any field, the non-endorsed part must contain one of three fixed open cones near the edge seams.
  - **Cor 2.5:** an endorsing field must have ρ_j/ρ_i nondecreasing in |g_j|/|g_i| (Ω fails; |g_w| passes).
  - Survives restriction to bounded or Sil(T)-supported records. Lexicographic stacks led by a positive density are excluded.
  - **OPEN:** unions of fields. Under {Ω, |g_w|}, T1 is Ω-Bayes and every precise edge model is |g_w|-Bayes.
- **Position after round 47.**
  - Certificates and the retreat split work for intersecting cores.
  - Separated pairs are forced by the edges.
  - Any single additive field fails (PP32).
  - The live architecture is a two-field union: a balanced field for T and the core, the |g_w| field for the edges, with the shared records controlled by (IB) and (TC). It needs a boundary layer that closes sections, unlike PP28 §4.2.

### 8.17 Round 48: forced defences and their replacement dominators (22 October; PP35 is a referee report; PP33, PP34, PP36 unrefereed)
- **Audit (AUDIT_round48_instructions.md).** The two-weighting plan is withdrawn: under (IB) two fields cannot run independent parts of the ranking. The main task is a JOINT rule for PP30's forced-defence family.
  - X = T[G ↦ D_p], R = D_p[G ↦ S] ⪯_w D_p.
  - Z = R with the w-correct answer on E.
  - Choose w and the dominator K together. Register the defenders. Include sections.
- **PP35: referee of PP32 and the penalty question.**
  - PP32 is correct (with small repairs) but RANK-LINEAR only; "additive" → "rank-linear" throughout. Cor 5.2's FF2 comparison is overstated.
  - Under general penalties, Thm 3.1 and Cor 3.3 FAIL: an explicit cheap-silence field ℓ^T; the known normalised-box coverage of hexagons.
  - They hold when silence costs at least the geometric midpoint at the seam (α₁α₂ ≥ β₁β₂; Thm A).
  - For any single field, no precise edge model with threshold in J is selected (Cor A′).
  - T1 stays excluded for single general fields by existing results: the Contamination Triangle main theorem, Q4.2 / M3.10′, FF2. The abstention field at u has an incoherent Bayes model at p = (200, 800, 1)/1001.
  - The lead's "possible major opening" was RETRACTED.
- **PP33: joint rule (PROVED unless stated).**
  - *Theorem 3.1 (axiom-level).* World j must refuse every bounded record Z → V_j[H ↦ D_K]. Under a potential with a positive leading density this gives a budget L_j(D_K) ≤ L_j(Z). So w fixes Z, and Z fixes the budget for K. Dominators of small rivals → V_j in measure.
  - *The rule.*
    - w: every world where PP25's L accepts the record.
    - K: precise ray models R_j(d) toward the centre, inside the budget; applied recursively.
    - Selection: rays plus vertices plus T at an isolated interior index.
  - *Theorem 5.1.* Strict (G), (IB) and (TC) hold for the whole relation, including mixed triangles across (G, E, j). No single-world ties; all registered models undominated; closure forces nothing.
  - Key fact: installed dominations never shadow each other (wedge geometry).
  - Sections are closed only relative to the partial index domain.
  - *Open:*
    - unbounded rivals: judging them by L breaks (TC) (Prop 8.2), so the far layer at the non-vertex worlds must be non-additive;
    - backward rivals of the ray models: the natural dominators shadow;
    - the edges; dominators of T's fills.
- **PP34: adversary.** NO obstruction found. All failures came from optional comparisons or from cell geometry.
  - Lemma 2.1 / Cor 2.2: padded undo-refusals in every context.
  - Prop 2.3: the w-rule alone cannot be refuted.
  - Shared records reduce the family to the first-order condition **(CC)**: no selected model has a retreat record refused at every world of its support.
  - **Largest-loss w-rule** (accept a departure at the world with the largest error mass; ties by priority) satisfies (CC) at first order (Prop 5.2). Ω and tie-sharing rules fail (CC), which is R46.1/PP32 again.
  - **Silent-wedge dominators** D_[e_j, λ] (credal segment from e_j to a point λ on [e_j, e_w]) never form a forbidden pair with T's departures (Prop 5.4).
  - Costs: the w-rule is non-additive, cross-world and mass-sensitive; triangle completion forces some second-world acceptances; arbitrary pieces are not handled.
  - Cells: exact SAT is satisfiable for V_1's whole family with forced silent-wedge dominators.
- **PP36: exact search.**
  - The w choice barely matters (Lemma 1).
  - T dominates every Z whose E meets V_j's w-errors (Prop SD). T can never dominate a pure retreat (Lemma E).
  - **Prop K:** if N ⪯_i Z and Z beats D pointwise at i, then D ⋠_i N.
    - Cor K2: no single dominator can serve rivals that together beat a selected model at every world of its support.
    - Cor K3: precise non-vertex models err inside Sil(T) at every world, so T cannot be the universal dominator if precise models are selected.
  - Targets:
    - (A) one dominator per (answerer, defence world);
    - (B) T as the universal dominator, selecting only models with no errors in Sil(T) at some world of their support (e.g. credal sets containing a vertex).
- **Lead's synthesis.**
  - PP34's silent-wedge dominators D_[e_j, λ] and PP36's target (B) are the same class, found independently: vertex-anchored models (K ∋ e_j), which are never wrong at world j.
  - That points to a vertex-anchored selected family as the next construction, combined with:
    - PP34's largest-loss w-rule (to meet (CC));
    - PP33's invariant and non-shadowing (for (TC));
    - a non-additive far layer at the non-vertex worlds (PP33 §8).

### 8.18 Round 49: the recursive milestone (22–23 October; PP39 is a referee report; PP37, PP38, PP40, PP41 unrefereed)
- **Audit (AUDIT_round49_brief.md, AUDIT_round49_answers.md).**
  - Corrections to the lead's round-48 synthesis:
    - PP33's budget is optional (Cor 3.2), not axiom-level;
    - PP33's balanced bounded layer cannot be kept;
    - PP34's largest-error rule is first-stage only;
    - PP36's real content is pair-dependent defence worlds, not vertex anchoring.
  - Milestone (binding):
    - index domain = T's index, the vertices, one complete edge, a connected path to it, and all limit points;
    - every registered model universally competitive;
    - sections closed for every rival;
    - repair class = vertex rivals, forward and backward forced rivals of every registered model for every generation, T's fills T[G ↦ N], and the edge models' forced rivals;
    - the invariant must be an actual allocation that survives closure.
- **PP39 (referee of round 48).**
  - PP33 Thm 3.1 and 5.1 correct. Ray models are not competitive against V_1.
  - PP34: Prop 4.1(f) WRONG; Prop 5.2 only in repaired form.
  - PP36: the one-answerer-per-dominator safety claim is WRONG. Counterexample: D_(1/2,1/2,0) with two balls. Repair: index dominators by (answerer, safe world).
- **PP37 (main construction; milestone not reached).**
  - Support-gated potentials give universal competitiveness of every registered model at every generation (Thm 3.1).
  - (TC) failures need dominations or two gates (Thm 3.2).
  - The first two-gate case is solved by a ratio inequality, which forces Cor A′ from (TC) (Thm 4.1).
  - **Obstruction: ties against closed sections.**
    - strict tie-breaking on the path forces path models = T (Thm 5.1);
    - accept-all-ties gives F2 (Prop 5.5);
    - world 3 cannot break ties (Prop 5.4);
    - the only survivor is the iso-level pattern (Thm 5.6, under four hypotheses).
  - Prop 6.1: realised budgets accumulate over generations. Conjecture 7.1: refinements of T as dominators.
- **PP38 (bounded kernel).**
  - The ℓ^T potential on bounded records: (G), (IB), (TC). Competitive against bounded rivals ⇔ ℓ^T-Bayes at a weight in the support. (CC) holds at every order.
  - Coherent Bayes models = T, three families of imprecise edge segments B_ij(t), and the vertices. No precise non-vertex model can be registered.
  - "No subordinate cone" screen.
  - The path must jump in measure.
  - Three residue families (against ℓ): the jump defence, T's small fills, and the edge models' second-generation rivals.
- **PP40 (adversary on PP38).**
  - Kernel confirmed; coherence lemma confirmed by blind search (177 weights).
  - **PP38 Prop 5.2 FALSE**; repaired by a necessary "shadow" condition.
  - Unbounded competitiveness comes free on the fragment but fails closed sections at the jump, so it is open in the milestone.
  - At the jump (PROVED): inheritance of accepting worlds; inversion at world k; a field-rejected edge-world record at every jump, landing on T itself for t* in about [0.65, 1.55] (a 4th residue family).
  - Splice form of Prop K.
  - Edge-rival dominators: only B_12(t) with |t − 1| ≲ 0.005 survive (field-endorsed at worlds 1 and 2, installed at world 3).
  - V_j never dominates T's j-fills.
- **PP41 (completion of PP38; milestone not reached).**
  - **Thm 2.4 (PROVED).** With PP38's kernel and one shared strictly guiding valuation per world on unbounded records, the milestone is impossible, whatever the zero rule. The jump forces B_12(t*) to be iso-level with T at two worlds, which is impossible for two Bayes models of one valuation (Lemma 2.5; LP duals match).
    - Hypotheses: the post-jump models come from the edge family; no installed record copies a T-to-edge piece.
    - The responsible commitment is "one valuation per world".
  - **Redesign:** a separate valuation per registered model (gates over PP38's kernel).
    - The jump then needs T's valuation to rate the post-jump models at least as well as T at world 3: LP-feasible at every tested t ≠ 1, impossible at t = 1.
    - Option A (keep valuations apart) or Option B (inheritance refusals). First cross-gate (TC) configuration stated.
  - Refinements of T cannot be registered under the kernel; dominators must come from T, B_ij(t), V_k.
  - Unbounded competitiveness ⇔ each model is Bayes for both parts of its valuation at one weight.
  - Generations: the allocation is a fixed function of the record and its realisers. Registration never removes a defence. Survival under closure needs cross-gate (TC) (open).
- **Position after round 49.**
  - The jump from T's fibre to the edge is the crux. Every single-valuation design fails there (PP37 Thm 5.1–5.6; PP41 Thm 2.4).
  - The surviving design is model-specific valuations (gates) over a single-field bounded kernel. The open core is cross-gate (TC) on the edge, with the shadow condition.
  - The repair families narrow to dominators B_12(t) near t = 1 for the edge rivals, plus open conditions for T's fills.

### 8.19 Round 50: revising the bounded kernel together with the defenders (23 October; PP44 is a referee report; PP42, PP43 unrefereed)
- **Audit (AUDIT_round50.md).**
  - "The jump is the crux" holds only after fixing PP38's kernel. The kernel's Bayes restriction is a cost of the kernel.
  - PP41 (NA) is impossible as written. PP41 Prop 4.1(b) does not give direct (C) for unions of gates.
  - Refusals are global verdicts.
  - Main task: revise the kernel jointly with the defenders. Secondary: a two-gate test.
- **PP44 (referee of round 49).**
  - **PP37 Thm 5.6's surviving pattern is WRONG.** It gives F2: T tied at all worlds with T[O_A ∪ O_B ↦ S].
  - **PP41 Prop 4.1(b) is FALSE** (explicit F2 through T's gate and B_12(1/2)'s gate). Common cause: a union over gates with symmetric zero rules.
  - PP41 (NA) is impossible. Prop 3.4′ holds in a local small-scale form under an explicit hypothesis (R).
  - Correct: PP37 Thm 3.1, 3.2, 4.1, Prop 4.3, 5.4, 6.1. PP38 Thm 3.1, coherence lemma, Cor 4.3, no-subordinate-cone. PP40's shadow repair, inheritance, inversion, splice Prop K. PP41 Thm 2.4 (exact hypotheses) and Lemma 2.5.
  - PP38 Prop 5.2 is false.
  - The "null family" claim is unsupported.
- **PP43 (two-gate test).**
  - *Thm 2.1, gate dominance.* If one functional U dominates each gate on the records its model realises, and each registered model is a unique U-Bayes model, then (TC), undominatedness and direct (C) hold for the union, with all copies.
  - *Thm 2.3.* T and B_12(t), t ≠ 1, satisfy gate dominance and the jump requirement.
  - **Thm 3.4 (PROVED).** In the fixed-kernel gate design, section inheritance at the jump is impossible for EVERY choice of valuations.
    - A kernel Bayes margin plus closed sections gives an explicit rival refused at every world, with a contradiction shell that blocks other gates.
    - This removes hypothesis (R) and covers both of PP41's options.
  - Escape candidate: tail-first lexicographic gates (Conjecture 4.2).
- **PP42 (kernel revision).**
  - **Thm 2.1 (PROVED).** Any design with a single additive witness field (≥ 0 on every accepted bounded record) can register only that field's coherent Bayes models. This covers PP38, any single revised field, and PP43's gate dominance. A single witness forces T's isolation and the jump.
  - **Replacement design.** Each registered model carries its own field (T keeps ℓ^T). A record is accepted iff it is guidance or some realiser of its old side rates it positively. A refusal is global: every realiser refuses.
  - **Thm 3.1.** (TC) is triangle-local. Sufficient: a pairwise ratio condition CG2 plus common constants for triples (CG3). Necessary: CG2, and CG3 in a weak form.
  - **Thm 3.2 (under CG2).** Every registered model:
    - is universally competitive;
    - is undominated, with no all-world ties (direct (C) for members).
    
    Also: dominations are strict; closure adds nothing; registration never removes a defence. The referee's F2 counterexamples violate CG2.
  - **First recursive repair: T's fills, by vertex caps** (M with a small corner cut at a vertex v; refinements of T that cannot be registered under ℓ^T).
    - Lemma 4.1 (cap geometry).
    - Thm 4.2: one fill, one excluded defender, module {T, V_i, cap}.
    - **Thm 4.3 / Prop 5.2: a continuous path out of T.** Shrinking caps with slightly self-critical fields, continuous in measure and tending to T, so NO JUMP. Members are universally competitive; (TC) and direct (C) hold. Fixed-rival sections are closed for every rival, including at T's index. Every small fill is dominated except fills hugging the boundary strip.
  - **Prop 5.1 (under hypothesis (U)):** a family where one dominator eventually dominates every small fill cannot have closed sections.
  - *Open:*
    - caps at different vertices conflict under CG2 (Prop 4.4(b));
    - amplification is limited by CG3;
    - extending the path to the edge (edge models' world-3 fields are free, Prop 3.6);
    - generation 2; the caps' rivals; the vertex and edge rivals.
- **Position after round 50.**
  - The frozen kernel is gone. Model-specific fields with pairwise compatibility (CG2/CG3) are the working mechanism.
  - First recursive success: T's fills, along a continuous path out of T with closed sections.
  - Next: the edge extension and the remaining repair classes. An adversary on PP42 is needed.

### 8.20 Round 51: compatible fields on the multicap family (23 October; PP48 is a referee report; PP45–PP47 unrefereed)
- **Audit (AUDIT_round51.md, AUDIT_multicap.md, AUDIT_round51_answers.md).**
  - Multicap family K_s = M ∩ {m_i ≤ c+ε−s_i}.
  - Union lemma: {C_s ≠ T} = ⊔ H_i(s_i); members never give opposite answers.
  - Interval criterion: 0 ∈ I_AB + I_BC + I_CA.
  - Each member's field may change on all corner bands; T's field may move; λ_s are free.
  - Repair class includes the two-corner rival X = T[G_i ↦ C_s, G_j ↦ C_t].
  - Index map required.
- **PP48 (referee of round 50).**
  - **Thm R1 (PROVED):** with no three-answer problems, under strict gates, (TC) ⇔ every pair passes CG2 and every triple has common nonnegative constants. So the interval test is exact.
  - CG2 necessity needs no agreement-region hypothesis.
  - **Lemma S (general section lemma, PROVED).** Hypotheses:
    - (S1) gated models continuous in measure;
    - (S2) cost differences L¹-continuous;
    - (S3) the selection continuous in measure;
    - (S4) no other acceptance routes; zero accepted.
    
    Conclusion: closed fixed-rival sections. The set of gated models must be the closed box.
  - PP42 Thm 2.1: "if" direction wrong.
  - Thm 4.3(a): repaired with a pointwise R_* ≈ 8.45. Thm 4.3(c): proved in full (no additive witness at world v).
  - Prop 4.4: genuine (TC) failures. Prop 5.1: uniform local finiteness false.
  - Union lemma: exact for s_i + s_j ≤ ε. "Never opposite" needs s_i ≤ 2ε/3.
  - PP43 Thm 2.1 and 3.4 confirmed.
- **PP45 / PP46 / PP47 (constructor, computation, adversary; three independent derivations agree).**
  - **Theorem (PP45 Thm 3.1 = PP46 Thm A = PP47 confirmed; PROVED, with LP Farkas certificates).** T and the combined cut C_(a,b,0) cannot both be gated members, for ANY fields and supporting weights.
    - Pair Bayes plus CG2 combine into one vector D ∈ R³.
    - Answer types correct at exactly one world occur for all three worlds, so no world can carry max D.
    - The pair condition is empty.
  - **Pair criterion:** two members are compatible iff, going from one to the other, at most one cut grows and at most one shrinks. With T present only the tripod/star (single cuts at one vertex) survives. No 2-D gated family through T exists in the box.
  - PP47 Thm 2.5 closes the non-unique-Bayes loophole (F2 under zero-accepting gates; T non-competitive under strict).
  - The obstruction also covers lexicographic gates with additive bounded verdicts, and combined cuts used as ungated dominators. Non-additive bounded verdicts escape (Prop 2.6).
  - The axioms themselves are not shown to exclude T together with a combined cut.
  - **PP47 Thm 4.1 (PROVED, CHECKED):** under zero-accepting gates, (TC) ⇔ the closed interval test with positive constants AND no tight triple with all three bounding extremes attained. This is the correct test for Lemma S designs. The open-interval test is stronger than needed; the closed test alone is too weak.
  - PP43 Thm 3.4 does not bite in gate unions (own margins vanish). The selection must converge to T at T's index.
  - **Two-corner rival:**
    - no dominator (gated or not) may be a refinement of T missing two vertices (Cor 3.3);
    - excluded dominators: T, third-vertex caps, caps containing their piece;
    - dominators of shrinking rivals converge to T;
    - open: whether any tripod cap dominates it (none found numerically).
  - **Nearby result: the tripod/star (PP45 Thm 5.1, PP46 Thm D, PROVED).** Closed-form fields for T plus single caps at all three vertices, for all δ < ε/3, give:
    - pointwise unique own-Bayes;
    - strict pairwise CG2; the triple test passes;
    - continuity and an envelope (Lemma S applies);
    - universal competitiveness, undominatedness, no all-world ties;
    - an explicit continuous 2-D index map (cut vertex = lowest coordinate of p − p_T).
    
    Caveats:
    - it is globally witnessed (single field at the bounded level; an audit ruling is needed);
    - the open-interval test fails;
    - repairs are weak: none of T's gen-2 fills on single-correct pieces; about 11% of two-corner rivals; cap retreats essentially none.
    - PP42's discount raises coverage 3–4×, but it breaks cross-vertex pairs (a genuine (TC) failure).
  - PP45 Prop 5.6: a pointwise Bayes estimate with constant 3.
  - **Fan:** T plus single-vertex cuts of arbitrary tilt (2 parameters per vertex). Every sampled pair passes the pair test (1,640/1,640; NUMERICS). Joint fields are still to be designed.
  - Edge models B_12(t), t ∈ [0.5, 2], pass the pair test against T (NUMERICS).
- **Position after round 51.**
  - Within gate-union designs with additive bounded verdicts, combined cuts are impossible.
  - The working geometry is the fan of single-vertex cuts, with Thm 4.1 as the (TC) criterion under zero-accepting gates.
  - Open:
    - joint fan fields;
    - dominators for gen-2 fills, two-corner rivals and retreats;
    - whether a single global witness is acceptable;
    - non-additive bounded verdicts as an escape.

### 8.21 Round 52: the posterior family, whole simplex, and no global prices (23 October; PP54 is a referee report; PP49–PP53 unrefereed)
- **Audit (AUDIT_round52.md, AUDIT_posterior_pairs.md, AUDIT_round52_answers.md).**
  - Posterior family C_a = D_{M_a}.
  - **Pair-ordering theorem:** the single vector D = log(a/b) certifies every disagreement.
  - Whole-simplex reduction accepted, subject to one consolidated proof.
  - Index = likelihood; λ_a free.
  - Target: triples feasible but a 4-cycle infeasible (no global prices).
  - Boundary from the outset. A selective branch now.
- **PP49 (PROVED): consolidated sufficiency theorem (Theorem A).**
  - *Setting:* the posterior selection on the closed simplex, with zero-accepting gate unions.
  - *Hypotheses:*
    - (H0) strictly guiding fields;
    - (H1) WEAK own-Bayes at λ_a with supp λ_a ⊆ supp a;
    - (H2) strict CG2 for every pair (V_w at world w exempt);
    - (H3) an exact triangle condition for every ordered triple (a new criterion, since the family is NOT two-valued globally);
    - (H4) continuity in measure and L¹-continuous field differences;
    - (H5) no other routes.
  - *Conclusions:*
    - all axioms; no single-world ties between distinct models;
    - (S) with closed sections, including boundary realisers;
    - (LA) and direct (C);
    - KKM dominance strict at every world;
    - explicit repairs unnecessary.
  - (H3) is necessary for (TC).
  - *Theorem N:* any solution lacks global prices at some world (via FF2 and the Contamination Triangle).
- **PP53 (adversary).**
  - Exact four-model certificate: T, (11,10,9)/30, (11,11,8)/30, (10,11,9)/30. It has strict own-Bayes, strict CG2, triples passing PP47 Thm 4.1 with slack, and NO global constants at worlds 1 and 2.
  - Boundary:
    - supporting weights have exactly the index's support;
    - every pair, boundary included, admits fields;
    - a joint boundary module passes on 148 point types;
    - the transported ℓ^T(a∘g) fails at the vertices.
  - Necessary conditions for continuation: a width budget; spectator constraints at three-valued points.
  - Reduction: no gap.
- **PP51 (LP search).**
  - Weights are forced; cell-constant fields suffice. No global constants at a world ⇔ no additive endorser at that world.
  - The checkpoint is met for two arrangements, at all three worlds, as a PERTURBATION of the likelihood witness (constants ∝ 1/N_w).
  - **Kink obstruction (rigorous certificate):** the two-valued triple u, (406,421,373)/1200, (406,373,421)/1200 at ε = 3/10 admits no own-Bayes fields passing the closed triple test. Instances occur down to 2·10⁻⁴ from u.
  - Field ratios: e^1–e^8 for 4–6 members; PP53's width budget is met almost with equality.
- **PP50.**
  - The checkpoint is met exactly (deficit −1 in log₃ at world 1); scale-invariant toward T. PP53's certificate and PP51's kink were verified independently.
  - **Theorem K (PROVED, box certificate):** gated posterior index sets meet a neighbourhood of u in measure zero. So under union acceptance NO positive-measure posterior family or 2-D patch through T can be realised.
    - Cause: the architecture plus wedge-shaped answer regions near the corner rays.
    - Exits: selective acceptance, or half-plane families.
  - Regular continua: exact indifference at thresholds; nearby intervals collapse to a "price 1-form", so missing prices come from second-order curvature or far pairs.
  - Null route: posterior tripods through u showed no kink certificate (evidence only).
- **PP52 (selective branch).**
  - Own-argmax rule OA: theory PROVED (defence, sections, protection via (PX), (TC) via tilted certificates, KKM dominators).
  - A single designated winner breaks sections; the D-role rule is undefined for incoherent rivals.
  - **The combined-cut obstruction is RULE-INDEPENDENT:** a KKM argument inside one gate. It holds for any rule with closed verdicts, without CG2, (TC) or T's uniqueness.
  - OA keeps the type test and admits strictly more field systems, but never removes a witness the union has.
  - Every selected model must be gated under any realiser-gated rule. So "a kink-free gated subfamily plus designated realisers" is impossible.
  - Kink vs OA: no (PX) found (NUMERICS; CONJECTURE that the kink survives OA).
- **PP54 (referee of round 51).**
  - All scripts reproduce.
  - PP47 "a combined cut cannot dominate any rival": WRONG (a bounded unanimous-retreat counterexample). It holds for rivals that agree with T off a bounded set.
  - PP45/PP46/PP47 main theorems correct, with hidden hypotheses (T's uniqueness; universal competitiveness). The tripod and star are single-field realisations along a weight path.
  - PP47 Thm 4.1 holds only under strict CG2.
  - Pair-ordering theorem correct and extends to boundary pairs. D is a potential difference, so orderings can never block global prices; only interval sizes can.
- **Position after round 52.**
  - The sufficiency theorem gives a clean target, and four-model triple-local designs exist.
  - But union gating of a 2-D posterior patch through T is impossible (Thm K), and selective argmax rules appear not to escape it.
  - Remaining routes:
    - (i) a selection whose image near T is a NULL set of posterior models (curves or tripods), PP50's null route;
    - (ii) families with half-plane answer regions (PP50, PP52);
    - (iii) rules whose verdicts are not closed (no current section proof).

### 8.22 Round 53: does the kink survive single-world indifference? (23 October; PP60 is a referee report; PP55–PP57, PP59 unrefereed)
- **Audit (AUDIT_round53*.md, AUDIT_section_topology.md, AUDIT_radial_transport.md).**
  - Continuous posterior tripods are ruled out: face preservation plus KKM make the selection map surjective.
  - Addition lemma: arbitrary additions with ideal-I supports preserve closed sections.
  - Local construction theorem (Q must CONTAIN guidance; repair by PP60).
  - Radial transport is an exact isomorphism (not a reduction).
  - Plan: test whether the kink depends on forbidding single-world ties, using three runs:
    - V1: ties allowed;
    - V2: ties forbidden;
    - V3: gate constraints.
  - Exact encodings: defence disjunctions; undominatedness (∧B ⟹ ∧A); direct (C) split by coherent and incoherent rivals.
- **PP59 (hypotheses ledger).**
  - SAFE in a ties-allowed, non-gate module: PP19 Thm 1, 4(a)(b), 5, Prop S; PP30 Thm 3.1; PP33 Thm 3.1; Prop K/splice (with a guidance closing link); Lemma A; pair ordering.
  - Conditional (need the whole simplex or changing-rival closedness): Theorem Z, Lemma B/E, Thm C(i), tripod surjectivity, PP52 Thm 4.1.
  - NOT safe: everything gate-, field- or strictness-based (PP32, PP38, PP43, PP45–47, PP49 A/N, Theorem K, PP51 5.1, R1, Lemma S).
  - Memo §8.21 overstated Theorem K: the kink needs strict own-Bayes for T or strict CG2 on two cells.
- **PP56 (translation of the kink).**
  - Every contradiction-carrying step is gate-only (orthant separability). There is NO axiom-level kink without sections.
  - **Theorem L (PROVED, CHECKED):** a lexicographic balanced relation Λ (PP25 Thm A type) satisfies (G), (IB), (TC), defence, undominatedness, direct (C) and (LA) on the 2-D posterior neighbourhood N_u, against all rivals, with NO ties.
    - It uses an exact first-level Bayes tie, non-closed verdicts along rival paths, and realiser-free acceptances.
  - Prop 5.1: Λ's sections are not closed on any 2-D neighbourhood. Prop 5.2: one-parameter rival families admit a closed staircase.
- **PP55 (three-version exact search).**
  - V1 and V2 SAT at every level; **Prop F (PROVED): on any finite cell instance, lexicographic piece orders satisfy every axiom clause**, so nothing beyond guidance is forced finitely.
  - V3 UNSAT, with a 10-group minimal core on 4 cells.
  - **Thm 5.1′ (PROVED):** the all-indifferent tie gap fails too, given (H*). With zero accepted, T accepts its own silencing at every world (direct (C) fails); with zero refused, T is undefended.
  - Prop SR: finite section clauses cannot create UNSAT. An axiom-level kink needs NON-FINITARY section arguments over 2-parameter rival families.
- **PP57 (constructor).**
  - Tie–pad lemma: a gate-accepted kink triangle cannot be completed by ties.
  - **Theorem Q (PROVED):** if the relation accepts the strict part of an additive (or lexicographic-additive) first-level score out of selected models, closed sections force acceptance of every zero-first-level rival at every world, via pure likelihood-shift sequences. For Λ that is the kink's balanced swap, so direct (C) fails. No tie-break repairs Λ (Cor 4.3).
  - Prop 4.5: at each world exactly one of two sections is open; closing all three forces an incoherent all-world tie.
  - Axiom-level only Lemma 5.1 (shift monotonicity of refusals).
  - A successful rule needs a first level that is neither lexicographic-additive nor single-additive: it must sometimes refuse comparisons out of slightly improved members that its own increments favour.
- **PP60 (referee of round 52 and audit lemmas).**
  - Theorem K′: in gate unions the kink survives single-world ties. Only exact indifference escapes, and PP55 Thm 5.1′ closes that too.
  - Audit §§1–3 correct (with the Q ⊇ guidance repair); radial transport correct (density factor).
  - PP49 Thm A correct but tie-free by design; two missing hypotheses; Thm N unclear (FF2 chain).
  - Theorem K and PP51 5.1 correct. PP52 Thm 4.1 correct (extra hypothesis: changing-rival closedness); Prop 7.3 needs a hypothesis.
  - PP53 correct except the spectator lemma's last step (a legitimate tie).
- **Position after round 53.**
  - The kink is a gate (pricing) artefact. Single-world ties are NOT the lever.
  - Everything except closed sections is solved on the 2-D posterior neighbourhood (Theorem L).
  - The whole remaining difficulty is closed fixed-rival sections, under the constraint of Theorem Q: the first level must be non-additive in a specific sense.
  - Open:
    - (i) whether the non-section axioms force acceptance along pure-shift sequences for 2-parameter balanced swaps (axiom-level obstruction or not);
    - (ii) a first-level rule escaping Theorem Q with closed sections.
