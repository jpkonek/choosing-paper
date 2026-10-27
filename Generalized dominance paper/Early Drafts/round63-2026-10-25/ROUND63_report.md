# Round 63 report: composition, incomplete rankings, direction-continuous charts, LDG v3.2

25 October 2026. Five agents: RC63, CC63, IN63, DC63 and W63. Two referees: REF63_comp and REF63_neg. Labels: PROVED (refereed once unless stated) / CHECKED / CONJECTURE / NUMERICS. Notes are in `round63-2026-10-25/`.

## 1. Composition (auditor's construction L⋆K0 = conv{ν(q⊙m)})

**The theorem is correct (RC63, refereed).** Three things were checked:
- the composition theorem itself;
- the reach lemma;
- the closure lemma: composing two orthant-diagonal maps gives an orthant-diagonal map again, and the two commute.

There is also a shorter proof: the composed ranking is VB(L′, A) run on the pushed-forward measure c₊μ. So every VB result transfers, including the exact undominated family (refereed).

**Three worlds, interior factors: nothing new (RC63 + CC63, refereed).**
- **Count.** For full-dimensional K0, N(L⋆K0) = N(L). Here N counts the interior extreme points that are not strictly visible.
- **Lemma U.** Every extreme point outside ν(π*⊙K0) is uniformly visible.
- **Consequence.** In three worlds, every interior composed target is already of VB type with one exempt point. This holds for every compact convex L.
- **Triangles.** An interior triangle is a composed target exactly when it is VB-type.

**Genuinely new covered targets (refereed).** All of these lie outside the VB class and meet every hypothesis of the composition theorem.
- **n ≥ 4, interior targets.**
  - *Theorem F:* normalised-box K0 with a suitable VB-type L.
  - *Explicit target:* the box [1,2]⁴ composed with L = conv(ū, (19/20)p0 + e_j/20), p0 = (4,3,2,1)/10. The hull has 32 vertices and 33 facets; it has 5 bad vertices, 21 facets that are not two-term, and is not orthant-planar.
  - *Second explicit target:* RC63's n = 4 example.
- **Exempt point on a face of the simplex, any n ≥ 3 (Theorem BE).**
  - The three-world instance is an exact pentagon. Three of its five edges do not pass through a simplex vertex ("non-cevian").
  - "Not orthant-planar" is proved for n = 3. For n ≥ 4 it is checked in the test cases; the general proof is open.
- **Scope wording.** The bad vertices of the n ≥ 4 targets are *tangential*, not non-visible in O61's strong sense. So these targets are outside the VB class, but not shown to be outside O61's wider Brier-type class.

**Exclusions (refereed).**
- The reversed triangle and pari-mutuel models cannot be reached in any number of worlds.
- ε-contaminations whose centre has exactly one zero coordinate are never composed targets. Two or more zeros are not treated.
- In three worlds, a triangle with two edges through simplex vertices is never a composed target. A triangle with one such edge is one exactly when an angle criterion holds, and then it is already covered.
- T1 appeared on CC63's list of unreached targets by mistake: it is strictly visible at every vertex and covered by VB.

## 2. Incomplete (finite-view unanimity) rankings for the reversed triangle (IN63, refereed)

**Existence.** Undominated weak dominators exist by compactness, using the views only as coordinates in the proof.

**General lemmas (all correct).**
- *Slab:* a non-null tie at weights positive on every view gives an incoherent efficient model.
- *Free-sign:* on a supporting face, views already used return with weights of either sign.
- *Rank-deficiency:* a constant-direction region is fatal.
- *Limit lemma.*

**Theorem C.** Finite unanimity systems fail for the reversed triangle at any face structure and any tie pattern. The views may be concave gains that are only weakly sign-correct, or convex vetoes (paid by the target or not) followed by such gains. This excludes the paid-veto candidate.

**Theorem S.** If the whole boundary is settled at one level of the face chain, continuous piecewise-linear views fail. This relies on C62 Thm 4.1 as repaired.

**The identified escape: settle the corners one level later.** Cutting tied "caps" off the corners replaces the unsolvable corner system with a solvable cut-point system (exact point p = 1/4). But:
- the caps force one direction on each cap;
- the rotation lemma then forces the design into the "pinned" case.

The exclusion for continuous piecewise-linear caps is a CONJECTURE (7.2) with an outline.

**Explicit six-view system (CHECKED).**
- The target is the unique lexicographic maximiser on its face (weights (1,1,1 | 0,0,0)).
- Every efficient point of that face is coherent (bathtub repair).
- The system fails elsewhere, with exact witnesses W1–W3 at full-support or admissible weights.
- The six-view system is itself discontinuous at the cuts. The paragraph saying its failures are "forced" overstates.

## 3. Direction-continuous charts (DC63, refereed)

**Theorem DC.** No direction-continuous piecewise-linear chart meets the certificate for the reversed triangle, on any one-sided U. This holds for any fan and any positive scale on each cell.
- *Hypotheses:* (C1), (C4), (C3) for priors near u, and (C2) at u. The claim that (C2) is not needed was a real gap; an exact local example shows the step is not local.
- *Corner system:* 2z² − 3z + 2 = 0, which has no real roots.
- *Open:* direction jumps at the corner rays (needs A62's step lemma N5); non-piecewise-linear fields.

## 4. LDG v3.2 (W63)

- **Hypothesis map** (§3.2) with four parts:
  - substantive framework;
  - route A: certificates (B), with (S) a stronger way to obtain them;
  - route B: compact score range, Lemma zorn, then coherence of the undominated models (Prop lexbayes is one lemma here);
  - optional construction restrictions.
- (W) is labelled a stronger objective.
- One sentence separates rescaling invariance of Bayes acceptance sets from invariance of the ranking.
- The hypothesis table is regrouped.
- Small fixes: `\coloneqq` throughout; convexity is needed only for Prop lexbayes; Prop permissible holds under (LA) + (W).
- 37 pages, compiles cleanly.
- Open note: guidance, independence and (LF) are defined in the covering paper; add a cross-reference.

## 5. Coverage map after round 63
- **Covered exactly:**
  - the VB class (one-sided);
  - boxes and orthant-planar polygons (full domain and one-sided);
  - composed targets: new in n ≥ 4 and for boundary exempt points (one-sided);
  - precise targets (full domain).
- **Not covered by any construction:**
  - the reversed triangle and pari-mutuel models;
  - in n = 3 inside the simplex, every target with at least two corners that are not uniformly visible and that is not orthant-planar, including triangles with two cevian edges;
  - zero-support contaminations;
  - T1 on two-sided domains.
- **Reversed triangle, excluded classes:** VB-type; vetoes followed by Brier or convex error levels; concave charts; regular single charts (R15 corner system); continuous piecewise-linear and direction-continuous piecewise-linear charts; composition; finite unanimity with concave or convex-veto views; one-level piecewise-linear views.
- **Reversed triangle, open routes:** non-piecewise-linear or discontinuous fields; continuous piecewise-linear corner caps (Conjecture 7.2); direction jumps at corners; non-additive orders.

## 6. Questions this raises
- In three worlds, the covered interior polygons are characterised by visibility, orthant-planarity, or a combination of the two? Composition does not mix them for n = 3.
- Is the reversed triangle a genuine counterexample under the agreed axioms? Every construction family examined fails at the same corner structure.
