# Round 67 report: completion round

26 October 2026. Agents: RF67a, RF67b, OUT67, CC67 and LDGO67. Referees: RF67a and RF67b (independent), REF67_out, REF67_cc and REF67_ldgo. Labels: PROVED (refereed; the referees are named) / CHECKED / CONJECTURE.

## 1. Outcome

The mathematical package for both definitive papers is complete and checked. Each paper has a proof outline, a scope statement, a cut list and a glossary. No new construction was searched for.

## 2. Full-domain theorem, any set of worlds (RF67a, RF67b, independently; auditor's proof)

**Setting.**
- Ω is any set.
- E is a separable, sup-norm-closed space of bounded gambles. It contains 1, or an order unit that is bounded below.
- μ is a finite Borel measure with a finite first moment (M1). It gives measure zero to the set where each credal set's lower prevision is exactly zero (M2).
- Models are classes of sets modulo μ.

**Theorem (PROVED).** Every incoherent model X has a coherent N that:
- improves on X by a uniform positive margin at every state;
- satisfies N ⊆ hull(X∖N) (the hull of a set with no supporting state is all of E);
- lies inside hull(X) when X has a supporting state, and otherwise inside hull(X₊) ⊆ {q* > 0}.

**Consequences.**
- The simple ranking on E has as its undominated models exactly the coherent models.
- It covers every coherent target D_Q, including precise and finitely generated ones. Literal local freedom holds, with neighbourhood E.
- Coverage needs only (M1) and (M2). Full support (M3) is used only to tell distinct credal sets apart.

**What the referees corrected or added.**
- *A false sentence.* "Sure losses are uniformly negative a.e." is false. A counterexample is −(ω−s)² on C[0,1]. It is also not needed: no D_Q contains a gamble with sup h ≤ 0.
- *Test for when a coherent model can make a change.* It must read "Q_B = ∅ or μ(A ∩ hull B) > 0".
- *A new result, proved by both referees independently.* N coherent, N ⊆ hull(X∖N) and a gain at every world together imply that no coherent model can make the change. Under the null-boundary condition a strict gain at every world suffices (RF67b). Without it, a uniform gain suffices.
- *A simpler inconsistent case (RF67a).* One minimax gives the repair directly, with no trimming.
- *Special cases.* TS66's finite full-domain result is a special case, and the theorem extends it to measures singular to Lebesgue. Every hull-closed domain is a corollary.

## 3. Application paper: proof outline (OUT67; REF67_out)

`OUT67_application_outline.md`, about 11,000 words. It is jargon-free and has no claim left unrefereed, apart from one sketch that is marked as such. The chain:
1. **Setting.** Coherence is relative to μ.
2. **One minimax lemma**, for any region and reference point. Corollary: a model has no supporting state iff some part of it loses at every world.
3. **Trimming (contraction) lemma, and the change lemma.** The change lemma says when no coherent model can make a change: (a) a strict gain under null boundaries; (b) a uniform gain without that condition; (c) the gain is non-null in the consistent case.
4. **Repair theorem**, in two cases.
   - *Consistent commitments:* optimise inside the hull, then trim. This is now proved directly on E, so the one-sided result really is a restriction.
   - *Inconsistent commitments:* drop the part that loses at every world, then optimise inside hull(X₊). The half-space alternative is a remark.
5. **Ranking corollary.** It satisfies every agreed property, and it is not transitive (an example on ℝ²).
6. **Corollaries for restricted domains:**
   - hull-closed domains;
   - one-sided D_{K′}, with the exact local-freedom conditions in finite and infinite dimensions;
   - finite worlds, assuming Lebesgue null sets.
7. **Scope.** Arbitrary worlds versus a separable order-unit gamble space; coherence relative to μ; strict versus uniform gains.
   - Open: nonseparable spaces, spaces with no order unit, and domains that are not hull-closed.
   - Unrefereed sketch: for μ concentrated on a separable subspace, the theorems transfer, but distinct credal sets can no longer be told apart.
8. **One structured construction.** The general veto–Brier theorem on the visibility class, refereed in round 61. It is kept because its world rankings are complete and transitive and score individual errors in an intelligible way. If it is kept, the application paper must also carry the Zorn-lemma admissibility argument (REF67_ldgo).
9. **Cut list and glossary.**

## 4. LDG: compactness and proof outline (CC67, REF67_cc; LDGO67, REF67_ldgo)

**Compactness.**
- **The abstract condition (CC) is equivalent to the conclusion (W)** (PROVED; cofinite topology; uses the axiom of choice).
- **The local finite-to-compact theorem is a genuine theorem** (PROVED).
  - Its hypotheses imply that some undominated coherent model is best at every world, so the conclusion does not imply them.
  - A new example: dominance and the finite-world conditions hold everywhere, yet the local hypotheses fail. So the compact family does real work.
  - For finite Ω, the local hypotheses are exactly the old finite condition.
- **Exact relationship (Proposition R1, PROVED by REF67_cc and REF67_ldgo).** The old pair of infinite-world conditions holds iff the local hypotheses hold for a compact family that also has closed comparison sets against every model. So the old pair adds exactly this closedness. Every LDG application has lower semicontinuous losses and therefore lies in the region where the two coincide.
- **The audit's separation example is correct.** Two worlds already suffice, so even for finite Ω the finite condition does not imply the old pair.

**LDG outline** (`LDGO67_outline.md`; about 22–24 pages, against 43 for v3.3).
- **Leading theorems:** the Bayes-choice theorems for loss rankings, for finite and for arbitrary Ω, whose hypotheses can be checked.
- **General theorems:** for finite worlds, any ranking via KKM, with no "certificates"; for arbitrary worlds, the local theorem.
- **Main example:** a transitive loss-ranking example showing that a compact family is indispensable.
- **Cut:** the admissibility route (no LDG result uses it).
- **Applications:** proper scores, probabilism on arbitrary domains, conditional reports, the countable example, and the Joyce counterexample as a short foil.
- **Referee corrections:**
  - the remark on constructing rankings needed "guidance protects coherent models"; it is now Proposition 9.1 with a short proof, which has not yet been refereed;
  - "no compact family has closed full comparison sets" needed a qualifier;
  - the v3.3 pointers were replaced with proofs.

## 5. Status
- **Mathematics for both definitive papers:** complete and refereed.
- **Ready to write:**
  - the definitive LDG, from LDGO67;
  - the definitive application paper, from OUT67.
- **Open questions, which do not block either paper:**
  - nonseparable gamble spaces;
  - spaces with no order unit;
  - domains that are not hull-closed (n ≥ 3);
  - the philosophical question of independent accuracy-based justification.
