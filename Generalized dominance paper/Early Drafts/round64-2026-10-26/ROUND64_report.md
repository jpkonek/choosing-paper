# Round 64 report: (TC) without transitivity, comparison deletion, a partially cevian cover, and the covering paper

25–26 October 2026. Four agents: OR64 (negative), ES64 (escape), PC64 (partially cevian triangle) and W64 (paper). Five referees: REF64_or, REF64_es, REF64_pc, REF64_paper and REF64_bx (a second refereeing of the paper's new sections). Labels: PROVED (refereed once unless stated) / CHECKED / CONJECTURE / NUMERICS. The framework is the one binding in AUDIT_r64: reflexive relations, (TC) only, no transitivity, no completeness. Notes are in this folder.

## 1. Headline: under (TC) alone, protecting the target costs nothing (REF64_es)

**Deletion lemma (PROVED).** Take a complete score order and delete some of its comparisons. If deletions are symmetric whenever the two scores are tied, the resulting relation satisfies (TC). It even satisfies the stronger finite-chain consistency condition, because the score order extends it.

**Theorem 3.2, comparison-deleted Brier Δ(𝒩) (PROVED, refereed CORRECT in full).**
- *Construction.* Start from the Brier ranking. Fix any family 𝒩 of coherent models. For each N ∈ 𝒩 and each Y that is Brier-weakly better than N at every world, delete "Y ⪯_i N" at one world i. The world is chosen as a function of the record (Y∖N, N∖Y) alone, and never at a world where Y is guidance-better.
- *Axioms.* The result satisfies reflexivity, strict (G), (IB) and (TC). It is not transitive: (TP) fails, with an exact instance.
- *Protection.* No member of 𝒩 has any weak dominator.
- *Undominated models.* These are exactly 𝒩, with direct (C), (W) and incoherent-model dominance, if and only if condition (★) holds. Sufficiency is ES64's; necessity was added by the referee. (★) says: every model outside 𝒩 has a Brier-better defender in 𝒩 whose change "attacks" no member of 𝒩.

**Consequences.**
- *Protection is free.* In the binding framework, "the target is undominated" carries no information on its own. All the content of a cover lies in the dominance half: global coherence, plus incoherent-model dominance by changes that attack no undominated model.
- *(H) would give a universal ranking.* Take 𝒩 = all coherent models. Then (★) is equivalent to (H) (both directions PROVED): every incoherent X has a coherent N, Brier-better at every world, such that N∖X meets the coherent hull of X∖N in positive measure.
  - If (H) holds, one ranking makes the undominated models exactly the coherent ones, for every target at once. The covering problem is then trivial, and no axiom-level impossibility exists.
  - (H) is a CONJECTURE. It is PROVED for several classes:
    - models that miss part of the positive orthant;
    - every non-Bayes model, which is strictly dominated by a Bayes act;
    - full thin boxes beyond the face midpoints;
    - small holes and bumps kept away from a Bayes act's boundary (referee's cases R1, R2).
  - The collar trades D_K ∪ P with pieces near the face midpoints are CHECKED with a repaired defender (the referee's version).
  - Random defects: 17 of 30 certified exactly; no violation of (H) found (NUMERICS).
- *Where the degeneracy lies.* A world's verdict depends on whether a change attacks a coherent model, so the accuracy ranking is built from coherence itself. Record-level (context) conditions cannot see this.
- *What excludes it (CHECKED exactly):*
  - transitivity;
  - (TP);
  - a weaker condition, **disjoint additivity (Add)**: X ⪯_i Y and Y ⪯_i Z with (X△Y) ∩ (Y△Z) = ∅ imply X ⪯_i Z. Equivalently, under (IB): two accepted records with disjoint supports combine into an accepted record.
  - (Add) holds in every construction in the covering paper, since a sum of lexicographically non-positive vectors is lexicographically non-positive.
  - Finite-chain consistency does **not** exclude Δ(𝒩).

## 2. Ordinal collar argument (OR64, refereed by REF64_or)

**E61 under (TC).**
- *The box lemma fails for E61's own notion of priority region (PROVED).* Counter-model M1 adds one accepted record at two worlds to pure guidance. It satisfies all relational axioms on the actual model space. So (TC) does not imply (TP).
- *It holds again under two ordinal notions (PROVED).*
  - **Strong priority:** no model meeting R is ⪯_j any model avoiding R. This needs only strict (G).
  - **Strict priority:** this needs (TC), and genuinely so (M1b).
- *Earlier theorems are undamaged (PROVED).* Every region actually used in E61, O61 and IN63 is strong. The referee closed the Pareto and depth-leximax cases: under (IB), a region is strong iff no accepted record adds part of R while removing none.
- *Priority regions are not forced.* Additive charts have none, and boxes are covered by one.

**New necessary relational lemmas (PROVED).**
- **Lemma T:** a dominance record never applies to an undominated model.
- **Lemma OC:** for every non-null j-wrong set R in the collar, some coherent undominated model meeting R dominates the dented box. Its credal set omits a vertex of K.
  - Lemma OC uses strict (G), incoherent-model dominance and (LF). It does not use (TC), transitivity, global coherence or direct (C).
  - *Scope:* it excludes vetoes that refuse every coherent undominated model meeting R. It does **not** exclude every relational veto; E61-type priority regions survive without (TP) (referee).

**Diagnostic 𝒯 (PROVED).**
- An explicit incomplete, non-transitive relation keeps D_K undominated and refuses every collar trade at every world.
- It satisfies the relational axioms, direct (C) and target undominatedness.
- It **fails** global coherence and incoherent-model dominance at the one-world improvements of D_K.
- So the collar trade alone gives no ordinal contradiction.

**Scoped and calibration results.**
- **Theorem VA (PROVED, scoped).** No cover exists if each world (VA1) protects the collar by a relational veto and (VA2) accepts collar trades that raise its own summed payoff outside that veto. VA2 is the only place a price enters. VA contains E61 Cor 5.3's no-cover consequence.
- **Prop K (PROVED).** Let a sign-correct measurable chart family have every minimiser coherent at every prior (boundary priors included), and D_K as its unique Bayes act. Then it is a cover in the binding framework. So an axiom-level impossibility would also settle that chart problem negatively.

**Architecture ledger (PROVED by inspection, with referee additions).** The step at which each exclusion leaves the framework:
- E61 Cor 5.3 and Thm 5.1: the Brier comparison and the chart reduction.
- O61 Thm A: scalarising the error vector into one prior.
- IN63 Thm C: separation into view weights.
- DC63 and C62: a single numerical chart from the start.
- W62 `lem:dominance`: the (C) step uses **transitivity**. In the paper this is now Lemma 2.6(b).

**Against the success criteria:** (A), an axiom-level impossibility, was not achieved. (B), a scoped impossibility, was achieved as Theorem VA. (C), a new necessary relational lemma, was achieved as Lemmas T and OC. Section 1 now explains why (A) is out of reach unless (H) fails or the framework is strengthened.

## 3. A partially cevian triangle is covered (PC64; REF64_pc; second check REF64_bx)

**The triangle.** T = conv{(1,2,2), (2,1,2), (3,1,1)}/5.
- Its one cevian edge is the segment from (1,2,2)/5 to (3,1,1)/5, on the line m₂ = m₃ through e₁.
- Two vertices are not strictly visible.
- *Not orthant-planar and not VB-type* (PROVED).

**The cover (PROVED, every requirement CHECKED exactly by two independent scripts).**
- Domain: U = {22h₁ + 11h₂ + 17h₃ > 0}.
- World 1: −∫min(h₁, 6h₁), which counts wrong acceptances six times as much as correct ones.
- World 2: Brier.
- World 3: the veto ∫(q·h)⁻ with q = (2,1,2)/5, then Brier.
- Mechanism: at weights (1,2,2) the summed chart is min(5p·h, 10s·h), which is positive exactly on the cone of the cevian edge. The veto then adds the vertex q.

**Theorem BX (PROVED, refereed twice).**
- In the veto–Brier ranking, replace Brier by a box chart min(l_j h_j, u_j h_j). Then one whole normalised box may be exempt from visibility; it may be degenerate or lie on ∂Δ. Every cevian segment is a degenerate box.
- Uniqueness needs only β·l > 0.
- Coherence holds because the second level is a maximum of linear functionals −w·h with w ≥ 0 and 𝟙·w > 0. Concavity is genuinely needed: a convex chart gives a non-convex Bayes set.

**Corollaries (PROVED).**
- **BX3:** an interior triangle is a veto–box target exactly when it has at most one non-strictly-visible vertex (class V), or exactly two, joined by a cevian edge (class X).
- **Corollary 7.9 of the paper:** the paper's constructions reach exactly class V, class X and the all-cevian triangles.

**Consequences.**
- The proposed three-world characterisation, VB class ∪ orthant-planar polygons, is **false**.
- The older O61 §7 remark is overbroad. It said polytopes with two or more non-visible vertices need an error level that is neither Brier-type nor convex. That remark was never a theorem, and no refereed theorem is contradicted. The convex-error exclusion holds for:
  - the reversed triangle;
  - the interior pari-mutuel triangles (all three faces forced, nonsingular ray system);
  - polytopes with at least two all-crossing vertices.
- **Replacement conjecture:** an interior triangle is covered iff every edge joining two non-strictly-visible vertices is cevian. Its "only if" half would settle the reversed triangle negatively.

## 4. The covering paper (W64; REF64_paper; REF64_bx)

`Covering coherent sets of desirable gambles (draft).tex/.pdf`: 44 pages; compiles with no warnings, undefined references or overfull boxes.

**Framework (§2).**
- Reflexive (TC) relations, with the requirements as binding.
- (W) appears only as a stronger objective.
- Lemma 2.6: part (a) needs no order axiom; part (b) needs transitivity.
- Remark 2.7: we do not know whether the other requirements imply (C), so (C) is listed separately.
- §2.5: what strict guidance alone forces, including the domain dichotomy.

**Positive theorems.**
- §3, the admissibility route.
- §4, veto–Brier and visibility.
- §5, orthant-planar and boxes.
- §6, veto–box, with BX, BX3 and the cover of T.
- §7, composition: Theorem F and the [1,2]⁴ example; Theorem BE and the pentagon; the n = 3 interior limitation as Theorem 7.8; Corollary 7.9.

**Scoped exclusions (§8).**
- Each is tied to its construction class.
- The contamination exclusion applies to centres with exactly one zero coordinate, and is strengthened to "not an undominated model of any composed ranking".
- New Corollary 8.16: no pari-mutuel model, in any n ≥ 3, is a veto–box or chart target.
- The paper does not say pari-mutuel models are impermissible.

**Open problems (§9),** including the replacement conjecture with its caveat.

**Referees.**
- No mathematical error in any numbered result.
- Two false sentences were fixed: a missing (G) in §8.3 item (1), and "exactly two" in the introduction.
- A gap in Corollary 7.9 was fixed with a domain-free argument, now Lemma 5.8.

**Still flagged.**
- §8.3 records six exclusions without proof, attributed to unpublished notes. A journal version needs proofs.
- The citations to Rockafellar 6.3, 11.3 and 13.2 and to Schrijver §8.5 are unverified and are marked in the source.
- The framework section does not yet discuss (Add) or Section 1 of this report.

## 5. Coverage map after round 64

**Covered exactly:**
- the VB class (one-sided domains);
- class X (veto–box, one-sided domains);
- boxes and orthant-planar polygons (full domain and one-sided domains);
- composed targets, new for n ≥ 4 and for boundary exempt points;
- precise targets (full domain).

**Interior triangles, by known constructions:** exactly classes V and X and the all-cevian triangles.

**Open:**
- triangles whose two non-visible vertices are joined by a non-cevian edge;
- triangles with three non-visible vertices and some non-cevian edge, including the reversed triangle and the pari-mutuel triangles;
- zero-support contaminations;
- T1 on two-sided domains.

**Framework-level:** under (G) + (IB) + (TC) alone, the covering question for every target reduces to the dominance half; if (H) holds, it is trivial.

## 6. Decision needed from the author

Is comparison deletion (Δ(𝒩)) an acceptable ranking? It satisfies every agreed axiom, but its world verdicts are defined from coherence.
- **If acceptable:** the programme's main question becomes (H), a concrete geometric statement about Brier dominance. Proving (H) gives a universal cover. Refuting it is necessary, though not sufficient, for an axiom-level impossibility.
- **If not acceptable:** some closure axiom must be added. The weakest identified candidate is **(Add)**, transitivity along non-overlapping chains. It holds in every positive construction and excludes Δ(𝒩), M1 and 𝒯. The round-65 question would then be whether (G) + (IB) + (TC) + (Add) still allows protection for free, or a cover of the reversed triangle.
