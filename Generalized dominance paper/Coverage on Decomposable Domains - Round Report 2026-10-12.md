# Coverage on decomposable domains: round report, 12 October 2026 (revised 23:30)

**Setting.** The accepted guidance orders: strict four-rank, the D_Δ exception, and Σ_T. Together with (IB), (LA), (S), (C), (E), (LF) at the target, and decomposable domains (SC plus closedness in measure). The working briefs are `decomposable-domains-2026-10-12/BRIEF.md` and `BRIEF2.md`.

**This revision follows the auditor's assessment** (`CPMs/outputs/decomposable-domain-audit/Assessment of Decomposable Domain Results 2026-10-12.md`). The earlier summary of this report overstated the results. In particular:
- it claimed that the evidence points decisively towards impossibility;
- it called Bayes uniqueness a uniqueness of the selection;
- it treated the contamination-family obstruction as an obstruction to the target;
- it said that only one exotic escape remained.

All four statements are withdrawn.

**Where the statements are.** Every result, in corrected form and with its status, is in `decomposable-domains-2026-10-12/Consolidated Statements - Decomposable Domains 2026-10-12.md`. The section below, "Round 3 addendum", covers R10a, R10b, R11, R12 and R13. Statuses are those of independent AI referee passes; nothing has been checked by a human.

## What is and is not established

**Closed choice and non-additive rankings.**
- Closed competitive choice rules out several natural ways of making the set of undominated models larger than additive rankings allow.
- In two worlds this gives additive-family equivalence for two classes: sandwichable rankings (R5 Thm UN with R2 Thm R) and two-level additive lexicographic rankings (R7 Thm 1′₂).
- In three or more worlds the sandwiching results give necessary pairwise restrictions only.
- For a single target there is a stronger reduction. If a sandwiched system of any cardinality vindicates a target T, then a single additive system on the same decomposable domain makes T Bayes at an interior prior. That system also satisfies every interior and vertex condition. This is R11 Thm W with R13 Prop S.
- That additive system satisfies (S) once the condition (BT) holds: no non-null Bayes ties at non-vertex boundary priors. In three worlds such ties can occur at only countably many points of each edge (R13 Prop E).

**The three-world contamination triangle T1.**
- **Not excluded.** Additive coverage of the single target T1 remains open.
- **Excluded unconditionally.** No additive system covers T1 with a Bayes family that is constant on an open set of priors (a "plateau"). The same holds for every interior target with two vertices whose credal-set boundary crosses a coordinate hyperplane, which includes every interior triangle and every ε-contamination in any n ≥ 3. This is R10b Thm PL.
- **Excluded for concave charts.** Concave charts cover no triangle in general position (R10a Thm R).
- **Excluded for one natural family, conditionally.** Full-dimensional selections near the target are excluded, conditional on the CPM-folder no-go chain and on regularity hypothesis (H1).
- **Open cases** (R10a, R10b, R12):
  - adjacent two-sided charts (advice range {+,0,−}) with degenerate selected sets;
  - charts with dense discontinuities;
  - the "zero exterior ratio" regime. This regime is inhabited by covered polygons near T1, so arguments that use only facet crossings cannot close T1; corner rays are needed.

**Nearby positive results.**
- Gauge mixtures K_p = ν(Σ p_i M_i) cover hexagons and 9-gons arbitrarily close to T1 (R10a Thm M, Prop M′).
- These approximants are polygons. Approximation as such was already known from v19's parallel bodies (cor:approx-all), and the mixture formula is NAL prop:average.
- New here: condition (M2) is exactly what makes the charts sign-preserving on the largest possible acceptance region Av (the gambles that some evaluable model accepts).

**Arbitrary ordinal coverage remains open.** None of this shows that full coverage fails under the adopted axioms. Nor does it show that a failure would extend to Σ_T, or to n > 3, without a separate argument.

## Round 3 addendum: statements and status

All statements below are as repaired by R12 and R13.

### R10a
- **Thm V: REFEREED-CORRECT.** Assume (S), strict (G), (LA), (LF) at D_K, and n ≥ 3. For every e_i ∉ K, the vertex model is D_{V_i} with e_i ∈ V_i. Consequently, under these hypotheses, no mixed gamble with a negative coordinate is accepted by every evaluable model. Cor V3 is restricted to mixed gambles.
- **Prop V4: REFEREED-REPAIRED.** It characterises the compatible vertex tuples. Its converse produces the targets Σ p_i V_i, not a prescribed target.
- **Lemma E: REFEREED-CORRECT.** It concerns boundary priors. Its use in place of FA's step (K4) needs a limiting step; R10b Lemma FS supplies it.
- **Thm M: REFEREED-CORRECT; overlap noted.** The system is the gauge mixture: f_i(h) = min_{M_i} m·h, acceptance region Av = ∪ D_{V_i} (the gambles that some evaluable model accepts), and conditions (M1) and (M2). It gives a unique, coherent Bayes model D_{K_p} at every prior, with K_p = ν(Σ p_i M_i). Every K_{p*} with p* interior and K_{p*} ⊆ int Δ is covered with (LF).
  - The formula is NAL prop:average.
  - Restricting to a convex cone gives a v19 concave CPM realisation.
- **Prop M′: REFEREED-CORRECT.** It gives covered polygons W ⊆ K_u with Hausdorff distance to T1 of order a/b + (ε − ε′). Approximation itself was already known (v19 cor:approx-all).
- **Thm R (ray lemma): REFEREED-CORRECT.** No triangle in general position has a realisation with concave, sign-preserving chart components near ∂D_K, for any prior p*. For T1 this was implied by NOGO; the general-triangle version and the short proof are new.
- **Thm P: correct under non-adjacency (Sp) plus R4 (K1) and (K3).** Superseded by R10b Thm PL, which needs neither.
- **Theorem O's "plateaus excluded unconditionally": FALSE AS LABELLED in R10a.** The claim is true via R10b Thm PL.

### R10b
- **Prop V, Lemma FS, Lemma UVN, Prop L, Lemma M, Lemma P, Thm PL, Cor PL2: REFEREED-CORRECT.**
  - Lemma D: the set involved is only relatively open.
  - The claim that every interior triangle has at least two crossing vertices is true; R12 supplies a valid proof.
- **Thm PL.** Let K have two vertices that cross coordinate hyperplanes. Then no open set of priors keeps both vertices in K_q while staying in their crossing wedges. In particular, K_q = K on an open set is impossible. This is unconditional and holds for every n ≥ 3 and every interior baseline.
- **Prop L (locality barrier).** The constant family K_q ≡ K is realisable on compact subsets of int Δ. So any obstruction must use priors approaching ∂Δ.

### R11 (with R13)
- **Lemma V, Lemma IC, Lemma RS, Fact 0, Lemma K, Thm W (a)–(e), Cor W1, Lemma SF_n, Prop LX: REFEREED-CORRECT.**
  - Lemma IC remark (ii) is FALSE as worded.
  - Cor T's list of instances must drop R1 Thm 4.1.
- **Lemma BT: REFEREED-REPAIRED.** A non-null boundary tie makes (S) fail for selections indexed by interior Bayes models. Reindexing by a power, as in C_t = B_{t²}, cannot rescue this; only blow-up reindexing can.
- **R13 Prop S (new).** Every sandwiched world is countably sandwiched, because L¹ is separable. So Thm W applies to all sandwiched systems.
- **R13 Prop E (new).** In three worlds, non-null boundary ties occur at only countably many points of each edge.
- **Not verified:** the n = 3 blow-up reindexing (§4.3).

## Next questions (from the auditor, updated)

1. Additive coverage of T1. The remaining cases are those listed under "The three-world contamination triangle" above; corner-ray arguments are needed.
2. Remove (BT) from the single-target reduction. Countably many tie points per edge, plus a blow-up reindexing, would do it.
3. Find a structural property of arbitrary (IB) preorders under (S), beyond the classes built from additive components.
4. Keep the strict-guidance conclusions separate from Σ_T.
5. Do not infer the case n > 3 from n = 3.

## Round 4 addendum (13 October): negligible-stakes indifference (NSI_θ)

**Definition.** NSI_θ was accepted in principle by the author. At world i, on a mixed problem whose world-i stake satisfies |g_i| ≤ θ‖g‖, good advice and silence tie. Everything else is strict.

**Result (REFEREED, N4).** For additive rankings on decomposable domains, NSI_θ covers the contamination triangle T1 for NO θ > 0, in either norm and for every ε. The same holds for ε-contamination of every interior baseline in every n ≥ 3.
- **Mechanism.** (G) forces exact ties on band problems. So the decision on a band problem cannot depend on how much weight its world receives: acceptance is constant along lines through that world's corner. Near the corner, strict guidance forces acceptance of nearby gambles with larger stakes. Coherence then forces acceptance of band gambles that the target rejects.
- **Proofs.** There are two independent complete proofs: N2 Cor C1, and N1 Thm 4.3 with Lemma 4.2. Neither uses boundary priors or regularity hypotheses.
- **Small thresholds are the worst case.** Every full-dimensional interior target is excluded below a positive threshold θ_cap(K) (N2 Thm Z).
- **Σ_T is no help here.** Σ_T with T containing a relevant world also fails for T1 (N4).
- **Ties permitted rather than forced.** This class contains the strict systems, but nothing shows that it has the same coverage. *(Corrected 13 Oct: the earlier sentence "T1 is the open strict problem again" was wrong; see `Audit of Imported Assumptions - Addendum 2026-10-13.md`, A1.)*

**Positive by-products.**
- Closed choice follows from unique coherent interior Bayes models under any guidance order in three worlds (N1 Thm 3.1, Chebyshev selection; N3 Thm CC_θ via blow-up; both REFEREED).
- The extension of CCIBU's selection step to n ≥ 4 is open beyond vertices and edges (R14).
- Under (DF), (ND) and non-adjacency, T1 and every all-facing triangle are excluded for strictly guiding additive systems (R15 Thm 6.2, REFEREED R18).

**Lesson (corrected 13 Oct).** Forced indifference that stops partway through a world creates a new obstruction where the tie region meets the strict region *and meets the target boundary as in N2 Thm B* (N4's repaired statement). The earlier general principle, that every useful weakening must avoid such an interface, is withdrawn. Total indifference at a world, as in Σ_T, does not cover T1 either.

## Round 5 addendum (13 October, afternoon): permitted negligible-stakes ties

**Question.** The author accepted *permitted* ties: on band problems (|g_i| ≤ θ‖g‖) good advice may tie with silence, and the ranking chooses where, even target-dependently. Everything else stays strict. Does this give exact coverage of T1 for small θ? Brief: `decomposable-domains-2026-10-12/BRIEF4.md`. Notes: N5 (structural), N6 (constructive), referee N7.

**Answer: no new route.** Status: REFEREED (N7), additive rankings only.
- **No ties next to the target, from inside.** A tied problem is decided, near world i's corner, by the other worlds alone, so it is rejected on the side of a world where the gamble is bad. A strictly good problem just below it (coordinatewise) is accepted near the corner. Coherent models accept everything above an accepted gamble. So the tie is impossible (N5 Lemma 3.1, N6 Lemma DL; any n, any good~silence tie rule). For T1, ties are null on all of D_T for θ < Θ_NT (sup norm: θ < 1; Euclidean: Θ_NT ≈ 0.92 at ε = 0.3). Near the boundary they can sit only in thin outer "horns" at the six coordinate crossings (N6 Thm NT, N5 Prop 3.2).
- **Vertex anchoring survives** (N5 Prop 3.5, N6 Thm V′). The coordinator's sketch for this was not valid as written; the result holds by a different argument.
- **R15 Thm 6.2 transfers for every θ > 0.** No realisation of T1 satisfies (DF), (ND) and (NA_w), whatever the placement of ties, both norms, every ε, every interior target weight (N5 Thm 5.1; the crossing rows stay positive by a sign argument, N5 Lemma 4.2). The first-order system and the box are literally the strict ones.
- **Closed choice** under permitted ties: N3's blow-up selection still works (CHECKED).

**What remains open.**
- The strict residual, unchanged: R15's escapes (E1)–(E4), i.e. realisations that fail (DF), (ND) or (NA_w) (kinked facets, sliding edges, flat facets, adjacency near vertices).
- Horn ties, outer ties far from ∂D_T and ties on reversed orientations are not excluded; not shown to help a realisation that fails (DF).
- Euclidean θ ∈ [Θ_NT, θ_x): outer ties near corners open (irrelevant for small θ).
- Non-additive rankings: untouched.

**Consequence.** Stake-limited good~silence indifference is inert at the target boundary. For T1 the decisive question is again the exact strict problem: an additive realisation that is non-differentiable at the target weight (auditor's step 2), or a non-additive mechanism (step 3).

## Round 6 addendum (13 October, late afternoon): non-additive rankings

**Question** (brief: `decomposable-domains-2026-10-12/BRIEF5.md`). Do the additive obstructions to covering T1 hold for every ranking satisfying the axioms (preorders, possibly incomplete or non-additive)? Can a non-additive ranking cover T1? Notes: N8 (structure), N9 (constructions), referee N10.

**Correction to the brief.** The "plateau test" as posed was empty. Any selection can be re-parametrised so that it equals the target on an open set of indices (compose with a continuous self-map of the simplex that never enlarges supports; N8 C2/C8, N9.1, REFEREED). The additive no-plateau theorem concerns the Bayes map, not the selection.

**Results (REFEREED, N10, with the repairs recorded there).**
- **Ranking-level facts that survive:** vertex anchoring (the vertex model is the world-i best evaluable model and contains e_i); T1 is competitive on no proper set of worlds, so its indices are interior; a corrected face lemma; no coherent model is competitive on all three pairs of worlds; uncountably many selected profiles on each edge; a nonempty open set of indices whose models are competitive on all worlds but on no pair, with T1's indices strictly inside it; the selected profile cannot factor continuously through a tree.
- **Proofs that do not lift:** interior Bayes uniqueness, R10b's no-plateau lemmas and R15's corner calculus all use a canonical index structure (half-plane charts with strict signs) that general rankings need not have. This shows only that the proofs do not lift, not that the obstruction disappears.
- **Lexicographic rankings are not a route.** Two-level lexicographic systems with additive levels have unique coherent interior lex-Bayes models (N9.5). A design with T1 as the primary ideal (constant lex-Bayes map) satisfies every axiom except (S), which fails by the face-continuum theorem (N9.6, N9.7). If the primary is blind near ∂T, an incoherent model is undominated (N9.8).
- **Normal form (N9.4).** On the U-domain (the evaluable models are the measurable subsets D of U = D_{K′}, K′ a shrunk copy of K; so every evaluable model gives no advice on pairs {f,−f} with f ∉ U and −f ∉ U), a ranking with (G) and (IB) at a world is exactly a strictly monotone comparative ordering of that world's error sets satisfying de Finetti's cancellation condition.

**Frontier (as restated by N10).** Coverage of T1 is open both ways; the additive case is only conditionally excluded. An impossibility proof must produce a forced incoherent undominated model; every known way to do this uses half-plane charts with strict signs, Archimedean continuity, or level counting, and none is available for general (IB) preorders. A construction amounts to three strictly monotone, cancellative comparative orderings of error sets (complete or not, representable by measures or not), plus a closed competitive coherent selection containing T1. "Thinness" of the undominated set is a design aim, not a well-posed criterion until a topology on U_L is named.

## Round 7 addendum (13 October, evening): rankings that are coherent preferences

**Question** (brief: `decomposable-domains-2026-10-12/BRIEF6.md`). Can T1 be shown uncoverable under the adopted axioms plus the hypothesis that each world's ranking is a coherent preference in Walley's sense (1991 §§3.7–3.8; 2000 §6), applied to the loss gambles of a rank-increasing penalty encoding? Notes: N11 (reduction), N12 (additive core); referees N13, N14.

**Correction.** The brief said additive rankings are instances of every Walley variant. That is false for the strict-preference variants (N13 Prop A).

**(A) Reduction to additive rankings (N11; REFEREED, N13).**
- *Almost-preference* (closed cone, credal set M_i of finitely additive previsions): if every strict comparison is detected by some countably additive member of M_i (for instance, if all members are countably additive), then coverage of T1 yields an integral, strictly guiding additive field on the same domain. Its interior Bayes models are unique and coherent, and T1 is Bayes at an interior weighting. In three worlds, CCIBU makes that field cover T1.
- Weaker conclusions hold under countable detection plus strong non-atomicity (charge-valued fields, attained minimisers only), or with one member having a full-support countably additive part (N13 Prop B).
- Not reached: atomic singular parts of the charges; the non-Archimedean variant of Walley 2000 (blocked at "T1 lies in the lexicographic family").
- *Strict preference with openness* (Walley 1991 §3.7.7–3.7.9): with countably additive credal sets of positive density it violates (S) whenever two worlds' ideals differ (N13 Prop A). The class it defines may be empty (Conjecture N13.A), so it is not a useful hypothesis.
- The author's worry (disagreement among complete additive rankings protecting coherent models): harmless for the reduction direction, which runs through competitiveness from (S), not through undominatedness alone (N11.11, REFEREED).

**(B) The additive core (N12; REFEREED, N14).**
- *Reduction to credal families:* on the U-domain a realisation is the same as a family q ↦ K_q with K_q ⊇ K′, K_{p*} = T1, and half-plane positivity sets. The family is automatically Hausdorff-continuous, so the irregularity of the reward field is irrelevant.
- *The edge box holds unconditionally* (no differentiability, non-degeneracy or adjacency hypothesis).
- *Kinks excluded:* if the support functions q ↦ min_{K_q} m·h have one-sided directional derivatives at p*, continuous in the direction and taking both signs (condition (DD), strictly weaker than R15's (DF)+(ND)), T1 has no realisation, for every ε.
- *Charges* concentrated near a closed null set, or spread over dense null sets (small-carrier lemma, proved in N14), reduce to the integral case, provided interior Bayes minimisers exist.
- *Remaining gap:* a realisation would need a facet with a non-isolated set of rays where (DD) fails: oscillating difference quotients, direction-discontinuous derivatives, or flat/half-flat facets. On two-sided domains (advice range {+,0,−}) the adjacency escape (E4) is added.

**Status.** No clean impossibility yet. Conditionally: under almost-preference with countably additive detection, T1 cannot be covered by any ranking whose additive shadow satisfies (DD) at the target weighting. The single remaining analytic question is whether (DD) can fail in a realisation.

## Round 8 addendum (13 October, night): the additive core closed on non-adjacent domains

Notes: N15 (proof), N16 (adversary), N17 (rankings that don't add up), N21 (adjacent domains), N22 (reduction for coherent almost-preferences); referees N18, N19, N20, N23, N24. Consolidated write-up: **The Contamination Triangle.tex / .pdf** (25 pp.), with a faithfulness check report.

- **Main theorem (REFEREED twice, N18 and N20).** On every decomposable domain with (LF) whose pairs meeting D_{K′} are non-adjacent, in particular on the U-domain, no strictly guiding additive ranking satisfying the axioms covers T1, for any ε ∈ (0,1) and any interior target weighting. No regularity is assumed. The same holds for every all-facing triangle in general position, hence every interior ε-contamination, and for bounded charge penalties given interior Bayes minimisers. Key new steps: straight level lines of q ↦ min_{K_q} m·h; no pinning (R10b Cor PL2 off the target weighting); pivot chords; no sliding edges; slope–rotation inequalities, which give Lipschitz control and rule out first-order-flat facets; a blow-up that makes the facet maps projective; then the corner equation and the box. N16's "ratchet" first-order data are not realisable (N18).
- **General (LF) decomposable domains (REFEREED once, N23; R23.1–R23.4 given a second reading in the check report).** A covering must fall into one of two narrowly described configurations, (E5a) or (E4′); neither has been excluded.
- **Coherent almost-preferences (REFEREED once, N24).** On non-adjacent domains: no cover of T1 when every world is complete (with condition (UN)), or when strict comparisons are detected by countably additive previsions. In general, a cover forces an exceptional tie weight; the residual property (U) is a continuity property and is open.
- **Rankings that don't add up (N17; REFEREED, N19).** Not closed and not shown viable. Finite-atom models are useless (they contradict (S)). Fine (NC)-violating worlds exist, but no system with (S) is known to use a violation where it matters.

## Round 9 addendum (14 October): exceptional ties, two-sided domains, two repairs

Notes: N25 (exceptional ties, impossibility side), N26 (exceptional ties, construction side), N27 (the two repairs the auditor asked for), N28 (two-sided domains). Each was checked by one independent referee: N25_referee to N28_referee. The write-up **The Contamination Triangle.tex / .pdf** (now 41 pp.) incorporates these results and the auditor's corrections of 14 October. **The Contamination Triangle - round 9 changes.md** lists every change and its source. The 13 October version is kept as "The Contamination Triangle (13 Oct, pre-round 9)".

New terms.
- *Exceptional weighting:* an interior weighting at which the supporting additive assessment ψ ties a non-null set of problems. There, coherent and incoherent Bayes models coexist.
- *Atom chord:* a straight chord of the simplex made of exceptional weightings. It arises from a non-null set of problems (an *atom*) that all share the same chart line. (A problem's *chart line* is the set of weightings at which ψ is indifferent on that problem.)
- *Fan point:* a single exceptional weighting through which the chart lines of a non-null set of problems pass in a spread of directions.

**Exceptional ties (case M0).**
- **Shape of the exceptional set.** Proved in N25 and confirmed by the referee. The exceptional set is a countable union of atom chords, each cutting off one vertex of the simplex. It may be dense.
- **No fan points.** Proved only in the referee report (Prop F), so nobody else has checked it. It uses only the fact that ψ's Bayes models are coherent at almost every weighting.
- **Chords cannot be avoided.** If a ranking covers T1, then every supporting assessment has at least one atom chord. Choosing a different supporting assessment cannot remove them.
- **When the main theorem's argument fails.** If the target weighting lies on a chord, the argument cannot start: P(·,h) does not tend to 0 there for an open set of boundary gambles h. Proved, and confirmed with a repair.
- **Remaining configurations, both open:**
  - R-a′: the target weighting lies on a chord;
  - R-b′: the target weighting lies off the chords, but chords exist.
- **An ordinal mechanism exists, in two worlds.** N26.1, every axiom re-checked by the referee. It is an explicit two-world ranking that adds up and satisfies every axiom. The target is an intermediate tied model at the exceptional weighting, and every incoherent tied model is strictly dominated at both worlds. So an ordinal ranking can resolve an exceptional additive tie that its supporting assessment cannot. It adds no coverage, since in two worlds every target is already covered.
- **Two-level lexicographic rankings in three worlds.** N26.2–N26.7, confirmed with repairs. Their exceptional chords cannot cross, are rigid, and keep away from the target weighting. The referee's Prop R1 (one reader) adds: if the pivot step of the main proof still holds, there are no chords at all, so no such ranking covers T1. None of this transfers to general rankings that add up.

**Two-sided domains (N28, confirmed with repairs).**
- **(E5a) is impossible.** One of the two round-8 residual configurations is closed. In every additive cover of T1 on an (LF) decomposable domain, the advice range of almost every problem near the target contains both acceptances, and they compete.
- **Further consequences:**
  - the cuts converge to the vertices;
  - no interior credal set contains a vertex of the simplex;
  - credal sets on the crossing chords are never single points.
- **(E4′) becomes a problem about credal families.** It reduces to a geometric problem, CF(T1), about families of credal sets. Coverage holds iff CF(T1) has a solution. The converse direction rests on CCIBU, which so far only the author has checked.
- **Correction.** N28 inferred that nothing in (E4′) is consistent near the vertices. That inference was wrong: the referee's numerical "sector cap" example passes every constraint derived so far.

**Repairs (N27, confirmed).**
- **(LF) neighbourhood.** Every use of a cone-shaped neighbourhood was at bounded scale, so a compact collar inside the (LF) neighbourhood suffices. Nothing needs to be added to (LF), and the U-domain theorem was never affected.
- **Permitted negligible-stakes ties.** The main theorem holds when such ties are allowed:
  - in the sup norm, for every band width θ < 1;
  - in the Euclidean norm, for θ < √((κ²+1)/(κ²+2)), which is above √(2/3) for every ε.
  - The remaining Euclidean window is open; the missing input is (VP), stated in N27.

**Status.** Coverage of T1 is still open. The auditor's two concrete questions stand, now sharper:
- (Q1) Can a ranking that adds up resolve its supporting assessment's atom-chord ties in configuration R-a′ or R-b′?
- (Q2) Does CF(T1) have a solution?

## Interpretation correction (14 October, 12:30; author)

A domain restriction is only a restriction on the class of evaluable models; no decision problem is removed, altered or given restricted options. A gamble f always represents the binary choice {f,0}, equivalently {g,h} for any g,h with f = g − h. On the U-domain the evaluable models are the measurable subsets D of U = D_{K′}. For f ∈ U, D advises choosing g in {g,h} iff f ∈ D, and otherwise gives no advice; for −f ∈ U the same holds with g and h swapped. Evaluable models are guaranteed to agree on f (all giving no advice) only when f ∉ U and −f ∉ U.

This report now uses "decomposable domain", "advice range" and "U-domain" throughout; earlier versions said "menu" and "forced silence"; the files and folders whose names used "Menu Domains" were renamed on 14 October. A check of the whole write-up found no argument that uses more than the restriction of the evaluable class (see "The Contamination Triangle - interpretation changes.md").


## Round 10 addendum (14 October, afternoon): the organised attack; no additive cover on any decomposable domain

**Objective (author and auditor).** Construct an exact additive cover of T1 on a general decomposable domain, or prove that none exists, without adding assumptions. Brief: `decomposable-domains-2026-10-12/BRIEF9.md`. Two construction notes (C1, C2) and two impossibility notes (I1, I2) ran in parallel. Their results were then refereed adversarially (I1_referee, I2_referee, C1C2_referee). A separate note proved the old Prop D (PropD_notes), and a second, independent referee checked the inputs from round 9 (TS_second_referee).

**Main theorem.** For every ε in (0,1) and every interior target weighting, no strictly guiding additive ranking with integral penalties covers T1 on any decomposable domain with (LF).

Three essentially independent proofs:
- **I1** ("the edges pin the chart lines"). The limits of the credal sets at the edges of the triangle of weightings are determined exactly. This pins the chart line of every gamble crossing an edge, which forces three supporting lines near the target weighting. Those lines are compatible only if the facet maps are diagonal, i.e. x = 1, which the corner equation forbids.
- **I2** ("the box returns as a precise collar"). The failing box forces single-point credal sets along a strip at each corner. These are all governed by one diagonal-projective map. Where this strip meets the rest, the three corners give relations that contradict the corner equation.
- **C2, plus a short route.** The forced strips are injective precise regions, and C1's Theorem A shows that no cover has an open precise region with injective σ. C2's exceptional values of ε turn out to be empty.

**Status.**
- Each new argument has been checked by one adversarial referee, who confirmed it with wording-level repairs.
- The inputs from rounds 8–9 that the proofs use now have two independent readings each.
- The old Prop D is now proved (Theorem D: an open precise region is either constant or diagonal-projective). Its constant-or-injective core has been proved independently three times.
- Charges: proved along route I2 only, at the status of N14 Thm C2.
- Consequence for the bare geometric problem: CF(T1) has no solution. The bare-problem consequence is at the status of CCIBU (author-checked); the theorem about rankings does not depend on CCIBU.

**Construction side.**
- No construction was found.
- Every tame family is excluded, and in fact every family (via the forced strips).
- The gauge-mixture polygons close to T1 converge to the plateau family conv(T1 ∪ {q}), which has none of the structure a cover of T1 needs.
- The referee's sector-cap example from round 9 is not part of any cover.

**Corrections to round 9.**
- "Competition at a positive distance from the boundary is impossible" was overstated. What is proved is that the cut d-faces converge into the boundary, with apexes at the corners.
- On the crossing chords, the credal sets lie inside the tangent wedge and touch both tangent lines; they do not poke beyond them.

**What remains open.** Ordinal (non-additive) rankings. The question is whether a ranking satisfying the axioms, but not additive, can escape this theorem. That is the ordinal question the auditor is pursuing on the positive side. On the impossibility side, the natural next test is whether the I1 argument extends to rankings that add up (case M0) and to coherent almost-preferences.


## Round 11 addendum (14 October, night): the positive ordinal attempt

**Objective.** Build non-additive rankings that cover T1 exactly, or find a genuine obstruction (brief: `decomposable-domains-2026-10-12/BRIEF10.md`). Four investigators worked on this:
- P1: tie-type rankings (case M0);
- P2: rankings that don't add up (M1/M2);
- P3: the extension lemma;
- P4: the adversary.

Their results were checked by four referee reports: M0_referee, M0_second_referee, P2P3_referee and P4B_referee.

**No construction was found.** The search is now confined to one class of rankings.

**Case M0 is closed on the U-domain (new; the new parts were read by two referees).**
- No ranking whose worlds all add up on the relevant comparisons covers T1. This holds with or without (E_ψ).
- **Additive form:** no strictly signed integrable field on the U-domain whose Bayes models are coherent at almost every weighting has T1 as a Bayes model at an interior weighting.
- **How it is proved:**
  - the §4 chain survives atom chords (P4 Thm 3.1). This forces the target weighting onto a chord;
  - at that point, every coherent face model must vanish at the six crossings (Prop R.1, as strengthened by the second referee);
  - that excludes the three-atom residual (TP).
- P1's mid-facet escape cannot occur.
- **Closed or superseded:** residuals R-a′ and R-b′ are closed; Conjecture N26.R and the lexicographic residual are superseded.
- **Imports:** the result inherits N13 Prop B and N19 Prop R3(a), each read once.
- **Unrefereed addition:** the write-up's editor added that no CP-a ranking covers T1 on the U-domain. This is labelled CHECKED and needs a referee.

**The extension lemma (P3, confirmed).**
- As posed in *Vacuous Targets* §5, it is false. There are two explicit counterexamples on the U-domain.
- An exact replacement exists: add a limit rule R5 to the four closure rules. A system then exists iff the closure has no forbidden outcome, and closed sections come out automatically. The replacement is exact but formal.

**Rankings that don't add up.**
- **Two worlds (P4 Part B + referee).** Closed choice forces positive error weights for every lexicographic world whose levels are charges, and (CHECKED, via Savage) for every complete world. This is the first exclusion of mode M2 by closed choice.
- **Three worlds (P2 + referee).**
  - The selection of any T1 cover must fail Hausdorff continuity on the interior, or must fail to have straight vertex-respecting charts.
  - Two-level lexicographic designs are excluded (Theorem LX).
  - Rigid "exotic" exchanges would need far dominators.

**Precise remaining target.** A cover of T1 on the U-domain must have a world that does not add up on the relevant comparisons. By the two-world evidence, that world must be:
- incomplete;
- not lexicographic with charge levels;
- without a leading charge;
- not CP-a;
- with spread-out cancellation certificates.

No example of such a world is known in any setting, for any target. Whether one exists is the remaining question for ordinal coverage of T1.


## Round 12 addendum (15 October, morning): does the remaining kind of world exist?

**Task A.** Find, for any target and any number of worlds, a ranking satisfying every axiom in which some world's comparisons cannot be supported by positive error weights (¬SP^reg), or prove that none exists. Notes Q1 (construction), Q2 (exclusion in two worlds) and Q3 (exclusion for T1); referees Q3_referee and Q12_referee.

**Task B.** Referee the editor's claim about coherent almost-preference rankings (CPaU_referee).

**B confirmed (with repairs).** No ranking on the U-domain whose worlds are all Walley-style coherent almost-preferences covers T1, whether its worlds are complete or not. Charges with atoms are included. The connecting step has one reader. Conjecture U is therefore settled on the U-domain; it remains open on other domains.

**A: neither a construction nor a proof, but the question is now a two-world one.**
- **No construction.** No example of the remaining kind of world was found, for any target. Every attempt broke at a closed section or at an edge of the simplex.
  - One system satisfies every axiom except a single closed section (Q1.3). Its failing section is exactly [0, 0.5).
- **Locality barrier (Q3.1, confirmed).** An exclusion must use selection indices approaching the boundary of the simplex. Arguments local at T1 cannot succeed.
- **Corrected shadow theorem (Theorem R3, referee).** One of two things holds:
  - some world's comparisons out of T1 have no endorsing additive shadow;
  - every cover has unendorsed reversals against incoherent models arbitrarily close to T1.
  
  Q3's claim that "load-bearing reversals near T1 are not forced" was wrong.
- **Edge transfer (Q3.4–Q3.7 and Q1.7–Q1.10, confirmed).** On each edge of the simplex a three-world cover behaves like a two-world system. Under edge nestedness (Nest_e), every two-world exclusion applies to the world's comparisons between subsets of a single edge region R_ij, i.e. to the edge system; it says nothing directly about comparisons out of interior selected models, whose error sets cross. For leading charges and complete worlds, positivity on the edges globalises. Hence no cover of T1 exists if every world is coherent (CP-a), or is edge-nested and either has a leading charge or is complete. For other worlds, a two-world exclusion would still need a further step from edge comparisons to interior ones. The complete case rests on Savage's theorem (CHECKED).
  - (Nest_e) holds for the edge models exactly when their endpoints move together, i.e. are comonotone.
- **Two-world structure (Q2, Q1, confirmed with repairs).**
  - Left-fineness (Theorem LF).
  - The null sets of a failing world are initial segments (Corollary IS).
  - Failures come in mirror pairs: if world 1 fails, world 2 fails through the same target sets (Prop MP).
  - A mirrored pair alone gives no contradiction, so any proof must use closedness quantitatively (referee N2).

**Precise remaining questions:**
- (R1) Does a mirrored simple pair exist satisfying every axiom?
- (R2) Do general certificates reduce to simple ones?
- (R3) Can Lemma T be given a rate, i.e. a lower bound on its radius?
- (R4) Does (S) force nestedness (Q2.N; for edges, comonotone endpoints)?

A two-world exclusion would control the edge comparisons. For worlds that are neither complete nor have a leading charge, two further steps would still be needed to reach T1: passing to interior comparisons, and excluding case (i) of Theorem R3.


### Correction (15 October, 09:30)
The bathtub lemma (Lemma R1 of Q3_referee) was stated there with the extra hypothesis that f is bounded on bounded sets. The proof does not use it, and the normalisation step of Prop R2 (f = max(1, 1/ρ_i) off E_iT1) can violate it. It has been deleted in the write-up, and a dated correction has been added to Q3_referee.md. The write-up's three-world statements now say explicitly that the finer two-world restrictions hold only for edge comparisons, and only under (Nest_e).


## Round 13 addendum (15 October, late morning): edge nestedness and mirror-image pairs

**Questions.** (R4): does closed choice force nestedness, i.e. edge endpoints that move together? (R1): does a mirror-image pair exist? Brief: `decomposable-domains-2026-10-12/BRIEF12.md`. Notes S1–S4 were checked in three referee reports: S1_referee, S2_referee and S34_referee. Earlier the same morning, the write-up was corrected: the edge results now carry their qualifications explicitly, and the bathtub lemma no longer has the unused boundedness hypothesis.

**Settled (confirmed by one referee each):**
- **Leading charges need no nestedness (S2.1, any n).** A leading charge is either zero or strictly positive on every non-null set of mixed problems. Hence:
  - Theorem E2 holds without (Nest);
  - Theorem Q36(a),(b) and Corollary Q37 hold without (Nest_e) for every world with a nonzero leading charge.
  
  Edge nestedness is now needed only for complete worlds and for worlds without a leading charge.
- **Two worlds: chains from a leading charge (S2.2).** If either world has a nonzero leading charge, the selected models form a chain.
- **Two worlds: the Level Lemma and its consequences (S1).**
  - Two selected models tied at one world are tied at both.
  - World 1 totally preorders the selected models, and world 2 reverses that order.
  - If either world is monotonely continuous on one half of the comparisons, the selection is a chain.
  - So a non-nested two-world system needs both worlds to fail monotone continuity and to lack a nonzero leading charge.
- **What forces nestedness, if anything, is (C).** There is a full two-world ranking with strict (G), (IB), (LA) and (S) and a crossing selection; only (C) fails.
- **Correction.** The write-up's remark that nestedness "can fail where a tie set is split in crossing ways" is wrong for additive systems. It is replaced by the referee's text, together with a new sufficient condition for (Nest_e) in three worlds.
- **Mirror-image pairs.**
  - One exists in a system satisfying every axiom except closed sections, at both worlds (S3.1).
  - In "band ∪ translates" worlds, closedness forces a positive minimum target size (necessary, not sufficient), which rules mirror pairs out there.
  - A packing lemma is proved (S3.3).
  - Conjecture QC is equivalent at the two worlds, and ¬QC is the weaker form of (R1).
- **Rates.**
  - The rate in Lemma T is equivalent to the absence of "doubly-light" sequences (Theorem RATE).
  - No linear rate follows from the axioms, even with both worlds additive (Example A).
  - The write-up's claim that (R3) "would give Q1.C1" was unsupported and has been corrected.

**Remaining.**
- (R1), with ¬QC as its weaker form.
- (R2).
- (R3), now Conjecture S4.1: no doubly-light sequences.
- (R4), only when both worlds lack monotone continuity and leading charges, with (C) the axiom that must do the work.
- In three worlds: straightening of edge families for complete worlds, and the passage from edge comparisons to interior ones.

## Rounds 14–16 addendum (15 October, afternoon and evening): ambitious attempts at a positive answer

**Directive (author).** Keep pushing T1, aim directly at a cover, no small results. Six full-construction attempts were made (B1, B2, B3, C1, D1, E1), one decisive-theorem attempt (C2), and one existence attempt (D2). Every new result was refereed except E1. Notes and referee reports are in the notes folder; the write-up §8.5(e)–(g) has all of them.

**The one positive breakthrough (D2.1, confirmed by two independent referees).**
- There is a full two-world ranking on the U-domain, with every axiom (closed sections for every model, (C), (LF) at interior selected models), in which one world does **not** add up: no bounded strictly positive weight endorses its relevant comparisons. The failure is of mode (M2).
- The mechanism: finite-projective-plane levels at every scale near one end of the edge chain, so thin source strips are traded for targets that meet at every scale.
- This refutes Conjecture N17.B′ (including its two-world form), Q1.C1, and answers (R2) negatively.
- **Scope (referee 2).** The world is endorsed by the σ-finite density 1/(1−x), which is not integrable at the protected end. So the failure is exactly non-integrability at an end. The σ-finite version of N17.B′ is open.

**Why the breakthrough does not reach T1 (E1, proved in a note, not yet refereed).**
- Theorem M0closed needs only one *admissible shadow*: positive densities for which T1 is Bayes at an interior weight. That shadow must endorse the comparisons from each selected model into the shadow's own Bayes models.
- D2-type protection lives only at "ends" (near-unanimous limits). A shadow can be made heavy there, and then none of the comparisons it needs is protected. "Protection and visibility exclude each other." D2's own world is invisible to the M0closed argument (Prop E1.6).
- Theorem R3 holds without its case split (E1.2).

**Closed doors (all refereed once unless stated).**
- **B1, transfer through the link class.** If a world has leading densities on both of its edge regions, they glue to one density that is leading on all problems, and the world adds up. So a cover needs a world with no leading density on some edge region. (Correct; the headline sentence was qualified by the referee.)
- **C1, glued credal worlds.** Unanimity over different weight sets on the two edges either contradicts itself or adds up. Excluded for T1 at the status of M0closed(b).
- **C2, the leading-density theorem is false.** There is a full two-world system whose unanimity world has no leading density or charge. It adds up, so it does not help T1, but it shows that no edge-only argument can close T1.
- **B3, complete worlds.** The operative property is almost-representability, not nestedness. A world in a cover that does not add up must be incomplete (as reworded by the referee). Conjecture B3.C is open.
- **B2, D1, off the U-domain.** On any decomposable domain with (LF) at T1, an additive field with T1 Bayes at p\* has no ties at p\* (Theorem D1). So "add up with ordinal tie-breaking" through p\* is excluded on all such domains, at the status of the unwritten Prop B2.0. The remaining additive-type branch is p\* not exceptional with exceptional points elsewhere (E ≠ ∅), plus the E = ∅ caveat.

**What a cover of T1 on the U-domain still needs.** A world that fails to add up, lacks a leading density on some edge region, and is not glued-credal. For every end-heavy admissible shadow, it must have unendorsed dominator comparisons that are not protected at any end. No mechanism for such comparisons is known.

**Assessment.** On the U-domain the evidence now points against a cover. The decisive open problem is a σ-finite form of N17.B′ combined with E1's visibility argument. If proved, T1 is not coverable on the U-domain.

## Audit corrections and Rounds 17–18 (15 October, late evening)

**Corrections to the Rounds 14–16 addendum (external audit; F1, F2, F12_referee.md).**
- **Replaces "D2-type protection lives only at ends (near-unanimous limits) …".**
  - An end of a protected world on which T1 is eventually correct for that world is invisible to a suitably reweighted admissible shadow (E1.4).
  - T1-correctness is automatic at ∂U ∩ {h_i < 0} (F2.1). It is forced elsewhere when the other worlds have endorsing densities, finite and positive a.e., for their comparisons out of T1 (E1.3(a), F2.2).
  - Such ends need not be near-unanimous. Under (Nest_e) on both edges they lie at the near-unanimous boundary or at ∂U ∩ {h_i < 0} (F2.3).
  - E1.5 excludes a cover only when every world is end-protected with countably many ends and has integrable, jointly end-heavy base densities.
- **Replaces the B3 line.**
  - Proved: a complete world of a cover of T1 that does not add up is not almost representable on M.
  - That it cannot be complete at all would follow from Conjecture B3.C, which is open.
- **Replaces the σ-finite sentence of the Assessment.**
  - The locally integrable form (Conjecture σB) is false already in D2. Its far end includes R₊(1,0), interior to U, where every endorser has infinite mass (F1.2–F1.3, F2.4; observed by the auditor).
  - Surviving targets: local integrability on the mixed problems (F1.C′, with a (Nest_e) caveat for T1), or a density finite a.e.
- **D2′_A, D2′_B (F1, refereed).** All generator trades sit in a region with payoffs bounded away from zero, with protection at ∂U. Every axiom holds. A literal "targets in one compact subset of U" design cannot carry a certificate next to an additive world (F1.4).

**Round 17 (H1, H2; refereed once in H12_referee.md).**
- **H1.0.** At a weight where the Bayes model is incoherent, every coherent model costs a fixed d_t > 0 more.
- **H1.1.** Tuples of a.e.-finite endorsing densities are automatically admissible.
- **H1.2, H1.3.** A world failing to add up only on sets of small measure cannot carry a cover beside two integrably adding-up worlds. E1.5's heaviness hypothesis is replaced by T1-correctness of ends, in the narrowed form the referee states.
- **H2.2–H2.3.** Joint reweighting is always possible at T1-correct ends. With finitely many ends and integrable base endorsers, a cover needs a directed cycle in the conflict digraph. By the referee's Prop. R.1, heaviness is unnecessary.
- **H2.4.** A full two-world system in which neither world adds up.

**Round 18 (J1; not yet refereed).**
- **Near-Bayes models X_m and pattern switching.** These exclude every conflict cycle with an aligned ordering of worlds, including H2's template.
- **Residual: doubly misaligned cycles (Question J1.Q).** The model picture is a cap shrinking to a ray inside a tube shrinking to a curve, used twice.
- **Not covered:** countably many ends, non-integrable base endorsers, and 3-cycles or 2-cycles whose third world has ends.

**Assessment.** Every positive design tried so far has been forced into a smaller residual. The residual is now geometrically specific, as J1.Q. It is the natural next positive target. A negative answer, together with the uncovered cases, would close end-protected covers.

## Round 19 addendum (15–16 October, night): settle T1 on the U-domain, or find the mechanism of a cover

**Aim.** Either a cover, or a theorem settling T1 on M_U. Neither was achieved. Each attempt ended in a single precise question, and the round produced one structural classification. All results below were refereed once (J1_referee, K1_referee, K2_referee, K3_referee).

- **K3, classification.** A world without a finite (M1) certificate has a bounded endorser (Hahn–Banach).
  - By Yosida–Hewitt, its purely finitely additive part sits on shrinking sets. Off those sets, the countably additive part endorses exactly, except on a canonical blind set Λ_∞.
  - Localizable (integrable) ⟺ Λ_∞ null (K3.1, which assumes (NC)).
  - End-protection adds nothing beyond this (K3.2).
  - The tilted world (Q12 referee N3, completed) is totally blind and fails only closed sections (K3.3).
  - Patch theorem: K3.5/K3.6. Rigidity of Λ_∞: K3.7.
  - **Open:** Q_K3 (can Λ_∞ be non-null in a full system?), Q_A, and Conjecture K3.C.
- **K2, finite certificates.**
  - Divisibility theorem: a certificate made only of divisible comparisons is impossible, for any n and any target (K2.1).
  - Forced comparisons next to worlds with a leading density are divisible (K2.2). So an M1 certificate needs a rigid, unforced comparison.
  - In n = 2, M1 implies a crossing selection, which would refute Q2N (K2.3).
  - The construction scheme K2.5 is empty over generic additive bases (K2.6). The referee strengthened this for Brier to every weak-* closed cone (R6.2).
  - **Open:** Conjecture K2.6′.
- **K1, protected ends.**
  - Countable extensions of J1 (K1.1–K1.5).
  - Safe-test tool (K1.2).
  - K1.6 gives a necessary condition and an exclusion test. Its "iff" is tautological.
  - **Residual:** J1.Q′∞ (with a cycle and no aligned order, is (H_U) contradicted?).
- **J1, refereed.** J1 is correct. Its closure claim was overstated and is corrected via Theorem R.2 and Corollary R.3.

**Assessment.** Four rounds of positive attempts have each ended by excluding the design tried and isolating a sharper residual. The residuals are now three precise questions: Q_K3, J1.Q′∞, and rigid M1 certificates (K2.6′). No construction is in sight for any of them. The common thread is whether closed choice forbids "rigid" structure that no axiom forces.
