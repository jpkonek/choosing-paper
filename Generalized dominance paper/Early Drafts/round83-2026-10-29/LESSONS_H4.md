# LESSONS_H4: 19–26 October 2026 (rounds 34–66)

Reader H4. **Access note.** The Projects tool (`project_read`) was not available to me. I read the project docs from local copies instead: the mechanism memo (`/mnt/user-data/outputs/mechanism_design_memo_2026-10-19.md`, the 1,549-line version, §§1–8.29), the round 61–66 reports (scratchpad `r61`…`r67`), `VB_dominance_note.md`, and the LDG v3/v3.1 change logs. I also read the separation-gated evaluators material through the memo §8.2–8.5 and the device audit note. I read every listed device file and subfolder file, plus PP12 and PP14 (round 42) for the exact statements of Theorems E and N. I did not read the `.tex` of the separation-gated evaluators paper itself.

---

## 1. Chronology of attempts

### Phase I (19–20 Oct): screening non-additive mechanisms
**1. Three candidate rules (memo §2, §5).** *Aim:* an independent, strictly guiding, (TC)-consistent rule that is not additive in disguise. *Assumptions:* (IB), strict (G), (TC), (S), direct (C).
- **A. Super-majority of a continuum of additive judges.** FAILS (PROVED, Screen A Thm 3.3). The finite-statistics collapse does not need atoms: judges of mass ≥ 2θ−1 must share one boundary profile. *Mechanism:* any committee of additive judges collapses to one score near selected boundaries.
- **B. Exchange licensing with non-conservative rates.** FAILS (PROVED). (TC) forces every exchange cycle to have rate-product ≤ 1, so a fixed potential endorses everything. *Mechanism:* screen **S8**: a rule whose accepted records form a convex cone either has an additive endorser or violates (TC).
- **C. Transition pricing.** FAILS in two worlds (PROVED); three or more worlds is a CONJECTURE. Every rule that satisfies the axioms and judges each problem separately has an additive endorser.
- *Lesson drawn at the time:* a viable rule must be non-convex **and** not assembled from additive judges.

**2. Author's proposals 1–3 (memo §7).**
- **Two measures μ⁺, μ⁻.** Either an intersection of additive rankings (μ⁺ ≤ μ⁻) or a (TC) failure (the "sticky" direction). PROVED.
- **Base-dependent measure.** (IB) reduces it to Proposal 1 or to C (Lemma P2.1, sketch).
- **Pair-indexed weighting.** In literal form it collapses to additive I_λ (PROVED). The pair-indexed scoring variant falls to the new screen **S9** (anchoring collapse, PROVED): if one score decides the verdicts near an "anchor" pattern, (TC) makes the whole world that one additive loss.

**3. Separation-gated evaluators (memo §8.2–8.5; 20 Oct).** *Aim:* design around (S).
- *Construction:* a rank-step priority key; compare two models only when every step added has key below every step removed; any continuous verdict Φ is allowed behind the gate.
- *Two worlds:* PROVED and refereed. Every axiom holds, including (S) with closed sections, even for the sticky Φ = 2·added − removed, which has 730,964 (TC) violations without the gate. *Mechanism:* the gate alone gives (TC), and threshold sets give (S).
- *Three worlds:* FAILS. **S10/S11 (PP2 Thm 6, refereed):** a fixed-key gate plus KKM forces the key to be constant on the level-1 steps, so (S) fails for any verdicts.
- *Lesson:* the two-world laboratory no longer discriminates between verdicts.

### Phase II (20–21 Oct): record-level allocation under (S)
**4. Round 37: triple-local certificates.** These are **exactly** (TC) (PROVED twice), so they are not a new mechanism. The audit adds a **symmetry obstruction**: any comparison-preserving bijection maps undominated models to undominated models. So a ranking that reads only finitely many cell-transition masses cannot have an undominated coherent model that cuts through a cell. Finite cells cannot discriminate (PP3): additive rules pass on atoms but fail in the atomless setting (FF2).

**5. Round 38: allocating worlds to records (AF, greedy).** FAILS (CHECKED and PROVED). Rival records forced onto one world make (TC) refuse "return" records.

**6. Round 39: optional defenders.**
- PROVED: no mixed defence is uniquely forced by (G) plus the defence clause.
- Theorem 3: with the pool κν(added) − ν(removed) and κ ≥ 3, there are two eligible defenders, and the bound 3 is sharp.
- Theorem 4: symmetric thinning (deleting a record together with its reverse) creates no new (TC) violation.
- PP7: almost every rival in an open box needs a **strict** defence (the antichain argument).
- Audit: (S) is one-sided, so reverse records outside the anchored set H are free.

**7. Round 40: joint choice plus weakest-pair deletion.** FAILS (CHECKED; mechanism PROVED).
- A dominating rival whose reverse is also anchored gets a single, additively unsafe defence, and deletion removes it.
- Sections are not closed at the protection boundary.
- Audit diagnosis: every protected defence is endorsed by one **fixed lexicographic additive** loss (J_i, E_i). So the "positive evidence" was additive all along.

**8. Round 41: the coupled module and Theorem J (refereed).**
- Take a silent interior C_a and an edge model C_r that says A on a two-class majority pattern. Each rival record is then accepted at exactly one edge world, and (TC) forces a single cut λ₀.
- **J1:** no system with (G), face obligations and undominatedness has accepted-record sets that are closed in the rival argument.
- *Geometric criterion (audit):* the pattern exists iff the edge window is **strictly nested** inside the interior model's conditional projection (l < a ≤ b < u).
- So Theorem J is about selections with nested edge windows (the homothetic family: 129/129 pairs nested). It is not about T1.

**9. Round 42: the rescaled (posterior) family K_p = {p∘m/(p·m)}.**
- **Theorem E (PP12, PROVED).** No system invariant under positive diagonal maps works, and invariance under one non-scalar map already fails.
  - *Rival:* Λ, which takes the majority orientation on every mixed problem and is correct on unanimous ones. Λ is fixed by the group.
  - *Argument:* under invariance, {p : C_p ⪯_i Λ} is empty or all of int Δ. Closed sections then push the comparison to the vertex models B^m, and strict (G) refuses it there for m ≠ i.
  - It uses only strict (G), T1's competitiveness, and closed sections at the vertices. No (TC) or (IB).
  - The two-world analogue fails too, with the vacuous model D_Δ as rival.
  - *Survivor:* local invariance on records away from the coordinate planes. It never meets the section clause (Lemma D). Under (TC), complete, additive and lexicographic local rules are still excluded (Theorem L). Whether any locally invariant (TC) system exists is OPEN.
- **No forced cuts (PP14, PROVED).**
  - *Translation lemma:* on each edge, every member's credal projection is a multiplicative translate of one log-odds interval, and translates are never strictly nested. So no J-pattern exists anywhere.
  - *Theorem N:* "accept exactly where guidance accepts" satisfies every record-level clause into selected models: face obligations, undominatedness, direct (C).
  - *Consequence:* closed accepted-record sets are **not excluded** for this family (OPEN).
- **Where the difficulty moved.** Forward records: T1's own defence against one-class, unanchored rivals (the split-cell rival), and (TC) for repair records. PP13: two repairs plus a guidance link give a forbidden triangle.
- **Audit's global counting construction ("Rescaling and a Global Nonadditive Construction").**
  - An explicit multiscale cell-count ranking on all measurable models.
  - PROVED: (G), (IB), (TC) with no ties, a closed graph, (LA), direct (C), and a finite non-additivity certificate from coherent undominated sources including T1.
  - FAILS the (S) defence clause: T1 is refused at every world against a split-cell rival. *Cause:* excess protection. Every *regular* model, including incoherent ones, is undominated.
- **Additional results.**
  - The conditional-envelope family K(p) between M and B(M) keeps the posterior boundary and frees the interior.
  - The advice-step reflection obstruction: a rule that sees only rank increments cannot let a coherent model dominate fills of its own silences.
  - The box scaffold creates doubly anchored dominating rivals, as an exact rational example shows.

**10. Rounds 43–46: extensions that protect the target.**
- **Guard extension (21 Oct).** A real extension theorem: (G), (IB), (TC), (LA), direct (C), and every rival that keeps the guards is strictly dominated. But (S) fails:
  - F1: one forced repair makes T indefensible;
  - Theorem B: one-class rivals force a 1-defender repair;
  - Theorem O: rivals that change two guards.
- **Reciprocal six-source module (22 Oct).** PROVED, with no finite positive weak endorser. **Theorem Z (PROVED):** a "correctness zone" (a region where no accepted comparison makes advice correct) must lie in the unanimous problems. This kills protection by reserved regions.
- **Completion closure (round 45).**
  - PP20 handles every rival that changes T only where T is silent.
  - But Prop 1: if every accepted comparison is guidance, starts at T, or has unbounded support, then only T and the three vertex models are competitive. So (S) fails (Cor 3).
- **Round 46.** R46.1: Ω-type balanced rules are incompatible with (S). The audit corrects the scope and shows the precise-Bayes additive system satisfies (S) at the edges.

### Phase III (22–24 Oct): fields, gates, posterior patches, sections
**11. Rounds 47–51: single fields, kernels and gate unions.**
- PP32 (rank-linear only): no single field endorses both the edge-selected models and T1's fills.
- PP41 Thm 2.4 and PP43 Thm 3.4: the jump from T's fibre to the edge kills every single-valuation and fixed-kernel design.
- PP42 Thm 2.1: a single witness field registers only its own Bayes models.
- Multicap family: T and a combined cut can never both be gated members (PROVED with LP certificates). Only the tripod/star of single cuts survives.

**12. Round 52: the posterior family in gate unions.**
- **Pair-ordering theorem (PROVED):** one vector D = log(a/b) certifies every disagreement of a pair.
- Sufficiency theorem PP49 A.
- **Theorem K (PROVED):** under union gating, posterior index sets meet a neighbourhood of u in measure zero (the "kink").
- **Tripod surjectivity:** a continuous face-preserving selection is onto. So a null posterior image is impossible for continuous selections.
- **Addition lemma:** additions supported in a non-conic ideal preserve closed sections.

**13. Rounds 53–54: what sections actually force.**
- **Theorem L:** a lexicographic balanced relation satisfies every axiom except closed sections on the 2-D posterior neighbourhood.
- **Theorem Q:** if a relation contains the strict part of an additive first level, closed sections force acceptance of the balanced swap.
- **Theorem E (PP62, a second "Theorem E"):** acceptances endorsed by u¹ cannot have closed sections.
- So acceptances must lie **strictly between** u¹'s two envelopes.
- Robust refusal lemma, and PP61 Theorem C: no finite or countable instance fixed in advance can give an obstruction.
- PP63 Theorem J (a different Theorem J): additive kernels with negative two-cycles fail on a four-member kite.

**14. Rounds 55–60: global extension and repair.**
- PP64 Thm 2.3: a completion theorem (a total system that keeps the invariant satisfies every axiom).
- Conjecture 3.4 is false (the guidance trap). Signed propagation repairs it; accumulation of acceptances remains open.
- PP67: a uniform first-generation module for all fills X_E.
- The path obstruction: no fixed later C_t dominates every fill.
- PP72 Thm 6.2 is FALSE (section limit, then copy); the margin repair 6.2′ works.
- **Zero-sum obstruction:** a rule "accept iff v_i ≥ 0" with v zero-sum and antisymmetric has no strict domination.
- PP74 preservation theorem; PP78 proves Conjecture G on the three-ray star.
- **PP77 Thm 4.2:** the essential mixed refusal **requires u¹-non-endorsed acceptances**.
- *Final position (memo §8.29):* the decisive open problem is a non-endorsed acceptance class closed under (TC), copying and section limits.

### Phase IV (24–26 Oct): (B), admissibility, universal coverage
**15. The bounds condition (B) (24 Oct audit of LDG v2).** Adopted. Details in §4 below.

**16. The VB dominance theorem (25 Oct, refereed once).** The veto–Brier ranking on U = D_{K′} is lexicographic: first a veto ∫φ_m, then the Brier score.
- PROVED: every model is weakly dominated by an undominated one (compact score range plus Zorn), and every undominated model is coherent (Lyapunov convexity, then separation, then a unique minimiser).
- So T1 is covered on the U-domain, although VB fails (S) and **admits no closed-section selection at all** (L3 Thm 3.4: vetoes cannot be paid).
- General form: the visibility class K = conv(K′ ∪ A_1 ∪ … ∪ A_n), which includes every interior ε-contamination in any number of worlds.

**17. Rounds 61–63: classifying score-generated covers.**
- Covered: the visibility class, plus one exempt point; orthant-planar targets; boxes on the full domain; composition L⋆K₀ (new targets for n ≥ 4).
- Excluded for the reversed (pari-mutuel) triangle: vetoes followed by Brier or convex error levels, concave charts, continuous and direction-continuous piecewise-linear charts, composition, finite unanimity of views.
- F61's two-sided domain A_K gives only relative coherence; the audit gives an explicit counterexample.
- FD62: under global coherence, every domain is one-sided or full (n ≥ 3). On the full domain, regular charts reach exactly the orthant-planar targets.

**18. Round 64: comparison-deleted Brier Δ(𝒩).**
- Take the Brier ranking and delete one comparison per threatened coherent model, choosing the world from the record alone.
- This satisfies strict (G), (IB) and (TC). **Protection is free.** Coverage reduces to (H).
- Veto–box (class X) covers a partially cevian triangle.

**19. Round 65: Theorem H (PROVED, refereed twice).** Every incoherent X has a coherent N that is strictly Brier-better at every world, with the added part inside hull(X∖N).
- *Proof:* relative minimax inside hull(X), then a uniform shrink, then the contraction lemma.
- So every full-dimensional credal set is covered on a one-sided domain, including the reversed triangle.

**20. Round 66: the safe-improvement ranking.**
- *Definition:* accept a change if it is guidance, or if it is safe (it cannot be applied to any coherent model) and strictly raises that world's Brier score.
- PROVED and refereed:
  - every agreed axiom, plus (Add) and finite-chain consistency;
  - **every credal set covered on ℝⁿ** (TS66);
  - an infinite-world version on separable order-unit spaces;
  - (CC) compact certificates strictly weaker than (I)+(B∞).
- *Caveat recorded at the time:* the ranking is built from coherence, so it represents coherence rather than justifying it independently.

---

## 2. Recurring obstructions

- **Additive collapse / finite statistics** (S1, S3, S8, S9, Screen A, PP42 Thm 2.1, PP32, FF2 Thm 4.1; memo §§5–8.20). Any rule assembled from finitely many, or a continuum of, additive judges, or a convex acceptance set, or a locally anchored score, reduces to one additive score. Near selected boundaries that is fatal by FF2 / Theorem gm.
- **Selection forces fineness / closed sections.** This is the single most persistent obstruction in the slice:
  - L3 Thm 3.4: a paid veto blocks closed choice;
  - PP41 and PP43: the jump;
  - Theorem K: the kink;
  - Theorems Q and E: the two-envelope squeeze;
  - PP72: section-then-copy;
  - Theorem E (PP12): invariant sections are all or nothing.

  Every non-section axiom was satisfiable locally (Theorem L, Theorem R, PP61 Thm C). (S) was the binding constraint.
- **Strict nesting forces cuts (Theorem J/J1, round 41).** This applies only to selections with nested edge windows. The rescaled family escapes it exactly (translation lemma).
- **Equivariance (Theorem E, PP12).** A single group-fixed incoherent rival (Λ, or D_Δ in two worlds) has infinite Haar mass. Invariant verdicts make its sections trivial. Any system on the rescaled family must break the diagonal symmetry on such records.
- **Fixed priority orders and nesting (S10/S11, PP2 Thm 6).** Fixed-key gates force selected threshold sets to be nested, and so one-dimensional. KKM then forces the key to be constant.
- **Protection by territory (Theorem Z; F1/B/O in round 43).** Reserved correctness zones conflict with (S). Every protection device that forbids correct advice somewhere eventually leaves T undefended.
- **Excess protection.** Counting constructions and PP20 make too many models undominated, or leave only T and the vertices competitive (Prop 1, round 45).
- **Additively unsafe defences get deleted** (rounds 38–40). Dominating rivals with doubly anchored reverses recur; the priority rules sacrifice exactly the non-additive defence.
- **Zero-sum / endorsement** (rounds 58–60). Accepting only u¹-endorsed records gives no strict domination of the equal-loss class H. The essential repairs need non-endorsed acceptances, with no (TC) potential known.
- **Reversed triangle corner system** (C62, DC63, IN63). Every certificate-chart class fails at the same corner equations, which have no real roots: x ↦ 3/2 − 1/x, and 2z² − 3z + 2 = 0. These are exclusions of construction classes only. Theorem H later shows they are not axiom-level.
- **Domain dichotomy** (FD62, F61 counterexample). Under global coherence and n ≥ 3, every domain is one-sided or full. One-sided (LF) needs a full-dimensional target.

## 3. Positive mechanisms that worked, and their scope

- **Separation gating** (two worlds, every axiom). Two worlds only. Excluded in three worlds with fixed keys.
- **Record installation with a shared transition** (guards, six-source modules). Gives global (G), (IB), (TC), (LA) and direct (C) for a continuum of rivals. Never gave (S).
- **Symmetric thinning** (round 39 Thm 4). Deleting a record with its reverse never creates (TC) violations. A general tool.
- **Addition lemma** (round 52). Comparisons supported in a non-conic ideal preserve closed sections. Radial transport turns bounded modules into global ones.
- **Admissibility route** (VB; LDG v3.1 Lemma 3.11 and Prop 3.12). Compact score range plus Zorn, then separation to lexicographic Bayes, then a unique minimiser that is coherent. Exact scope: one-sided U-domains, complete lexicographic integral rankings, and target classes reachable by charts (visibility, orthant-planar, boxes, composition, veto–box).
- **The deletion lemma** (round 64): delete some comparisons from a complete score order, symmetrically at ties, and (TC) holds. **Theorem H** (round 65): relative minimax plus shrink plus contraction. **The safe-improvement ranking** (round 66): every credal set on ℝⁿ, in finitely many worlds, and the infinite-world separable case.
- **(B) and (CC)** as proof devices. They state precisely what dominance needs, without closed full comparison sections.

## 4. Assumptions dropped or changed, and why

- **(S) replaced by (B) (24 Oct).**
  - *Definition of finite (B):* closed certificate sets B_i(p) for each fixed rival; support-wise coverage (some i ∈ supp p certifies each X); and one coherent undominated realiser c at each p that beats every certified rival at every world. The realiser may jump.
  - *Why (B) was adopted:*
    1. (B) suffices for the dominance theorem, by exactly the KKM argument used for (S);
    2. LDG v2 already contained a three-world example where (B) holds and (S) is impossible;
    3. the closed-section obstructions (L3 Thm 3.4 for VB, and Q/E/K) were defeating (S), not dominance;
    4. VB was then shown to satisfy the dominance conclusion directly.
  - **Defending-world form** (v3.1 Prop 2.2): one rival-independent map u and rival-dependent defending worlds, where only the chosen defences must survive limits. This is close to the brief's W1–W3 with a common assignment p ↦ b_p.
- **(S) and (B) both demoted to optional routes.** (W) became the stated objective (v3.1, v3.2 hypothesis map), and routes B (admissibility) and C (safe construction) were added. The V3 review warns that (W) is the conclusion, not an explanation.
- **Transitivity and completeness dropped** (round 64 framework). Only (TC) was kept. This made protection free. (Add) was assessed and kept optional: it excludes Δ(𝒩) but not the safe ranking.
- **Full four-advice domain replaced by one-sided U-domains** for VB-type covers, then returned to ℝⁿ with the safe ranking.
- **A prescribed selected family** (homothetic, then posterior, then multicap) gave way to a coherent undominated class **derived from the ranking**. The audit insisted on this throughout.
- **Index = Bayes weight, continuity of selections, global record-closedness.** All three were dropped as unnecessary for (S) (rounds 39, 46, 52).

**Relevance to the current brief.** The current constraints re-impose **full domain** and **(S) or W1–W3**, so most of Phase IV's wins are out of scope:
- VB and the chart covers live on one-sided U.
- The safe ranking fails (S) badly: a change out of a coherent model is never safe, so a selected b_p beats a coherent rival only by guidance.
- F61 already proved that on the full domain, convex first levels give only normalised boxes. This matches the audit's "positive baseline covers only rescaled normalised boxes".

## 5. Top five lessons

1. **The binding constraint has always been selection with closed sections, not (TC) or independence.** (High confidence.) Theorems L and R and PP61 Thm C show every non-section axiom is locally satisfiable. Every Phase II–III failure came at sections. If (S) or W1–W3 is binding again, design the realiser map p ↦ b_p and its closed defending sets **first**, and build the comparisons around it.
2. **Choose the family before the rule, and make it non-nested.** (High confidence.)
   - Theorem J and the PP8 pump came from strict nesting of edge windows; the rescaled family removes them (translation lemma, Theorem N).
   - But the rescaled family's symmetry must not be inherited by the ranking (Theorem E).
   - Round 82's independence failure is consistent with this: a rule built from K_p's covers inherits K_p's structure on whole models.
3. **Additive endorsement is the default failure mode.** (High confidence.) Any rule that is a union, intersection, majority, convex cone, single witness, or locally anchored additive judge collapses. The working non-additivity always came from **record identity**:
   - which advice is replaced, not rank increments (the reflection obstruction);
   - shared transitions (guards);
   - incoherent-realisable partial advice (PP23, PP28; the safety test).
4. **Protection is cheap; incoherent-model dominance plus competitiveness is the content.** (Medium-high confidence.) Rounds 43–46 and 64 show that keeping the target undominated is easy. The hard part is that the *same* realisers must defend against everything. Measure progress by the defence clause, not by undominatedness.
5. **Finite and cell evidence cannot certify either direction.** (High confidence.)
   - PP3: atoms admit additive rules.
   - Prop F: finite lexicographic orders satisfy everything.
   - Theorem C: no finite or countable fixed instance gives an obstruction.
   - Obstructions need a rival chosen *after* the relation, and positive results need measurable proofs.

## 6. Leads: dropped too early or never tested

- **Locally invariant systems on the rescaled family** (PP12 §5; OPEN). Theorem E kills only global invariance, and Lemma D says local invariance never touches sections. Theorem L requires local incomparability near the vertices, and no one built such a system.
- **"Accept exactly where guidance accepts" (Theorem N) as the reverse-record layer** for the rescaled family, combined with a forward-record design for one-class split-cell rivals. Whether a ρ-closed system exists on the rescaled family was left OPEN and then abandoned in favour of gates.
- **The defending-world form of (B)** (v3.1 Prop 2.2), applied to the **full-domain** posterior family. It allows non-closed refusal sets and jumping comparisons other than the chosen defence, which is exactly where Phases II–III died. It was never run on the rescaled family before the programme switched to admissibility.
- **Testing W1–W3 / (B) on full-domain box or chart rankings.** FD62 and F61 covers live on the full domain for boxes and orthant-planar targets. It is unclear whether anyone checked whether their selection can be made rival-independent with closed chosen defences.
- **Non-endorsed acceptance classes with their own (TC) potential** (memo §8.29). This was the stated decisive problem when the programme pivoted. It was never attacked directly.
- **Two-world gated systems as an edge layer.** These are fully proved (gate2d), and Ψ_w = min(Φ_w, Φ_w − Φ_other) keeps them (PP16). They were never combined with a non-fixed-key interior rule under (B).
- **Theorem H's mechanism without the coherence-referencing safety test.** Relative minimax inside the rival's own hull is a coherence-free statement about Brier geometry. Whether a record-based acceptance rule can certify "added advice lies in the hull of removed advice" without naming coherence is unclear and untested.
