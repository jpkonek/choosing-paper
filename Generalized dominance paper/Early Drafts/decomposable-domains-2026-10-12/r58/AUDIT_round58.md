**Yes. The next round should change its organising idea: study repairs of different classes together, rather than treating class-3 repair as the template for everything.** Several conclusions from round 57 depend on keeping the repair class fixed. That restriction may be steering us toward the wrong alternatives.

I also need to correct my previous recommendation: breaking symmetry on the existing curve cannot, by itself, solve the problem. Every member of that curve is pointwise no better than T at world 3. A class-1 or class-2 fill of T improves T at world 3. Consequently, **no member of that curve can dominate those fills**, whatever asymmetric verdicts we install. New coherent models are necessary.

Here is the plan I would send to the collaborator.

### 1. Organise the construction by the class of each repair

There is a useful necessary condition that should become the basic bookkeeping rule.

Suppose B dominates a class-\(k\) fill of a selected C. Then
\[
C\not\preceq_i B\quad(i\ne k),
\qquad
C\preceq_k B.
\]
The refusals follow from (TC) and guidance; the remaining acceptance follows from C’s defence obligation.

Thus the repair specifies **exactly which world C must use to defend itself against B**.

An immediate consequence is:

> **The same ordered pair \((C,B)\) cannot repair fills of two different classes.**

Two different class labels would force C to refuse B at all three worlds. Therefore, a source with non-null silence in all three classes needs at least three distinct coherent defenders across those obligations.

This is a structural constraint, not a scoring assumption. It explains why one descending chain repeatedly runs out of room.

### 2. Test mixed-class recurrence—the genuinely new alternative

PP71 proves that a cycle consisting entirely of class-3 repairs requires non-transitivity at worlds 1 and 2. **That proof does not apply to a cycle whose repair classes change.**

Consider the pattern
\[
C_0\xrightarrow{\text{class }3}C_1
\xrightarrow{\text{class }1}C_2
\xrightarrow{\text{class }2}C_0.
\]
The required source-to-defender comparisons occur at different worlds. No single world is required to improve strictly all the way around the cycle.

For illustration, the following loss vectors realise the required comparisons *between the three sources*:
\[
C_0:(0,0,0),\qquad
C_1:(-1,-1,2),\qquad
C_2:(1,-2,1).
\]
Each transition improves the two appropriate majority worlds and worsens the remaining world.

**This is not a repair construction.** In particular, fixed score gaps will cause trouble for arbitrarily small fills. Its significance is narrower: the claimed choice between “transitive endless chains” and “intransitive recurrence” disappears once the repair class can change.

I would make this the principal new construction attempt:

> Find coherent models and measurable repair families supporting mixed-class recurrence, with T included, rather than another same-class four-cycle.

Do not require one successor to serve every fill of its predecessor. That uniformity has repeatedly created avoidable obstructions. Different fills may take different branches.

### 3. Supply three directions of coherent candidates

Retain the useful geometry from rounds 56–57, but use all three permutations.

For each \(k\), let
\[
M_0^k=\text{projection of }M\text{ from }e_k\text{ onto the opposite edge},
\qquad
N_k=D_{\operatorname{conv}(M\cup M_0^k)}.
\]

The existing seven-model module already shows that T and these three initial repair directions can coexist at the partial level. Use that as the starting example.

Then allow:

- rival-dependent refinements toward each opposite edge;
- interpolations back toward T;
- additional coherent models connecting different repair directions.

The candidates should be screened using the forced comparison pattern in item 1 and the agreement obstruction: **a proposed dominator cannot agree everywhere with the fill on its modified set.**

But do not impose guidance-worsening at every transition. Mixed-class recurrence needs the freedom to leave one direction and enter another.

### 4. Separate the two hard obligations, then prove them together

A repair construction needs both:

1. **Domination:** the chosen B is no worse than the rival at every world, with the required strictness.
2. **Defence:** every registered coherent model remains competitive against every measurable rival.

Neither can be postponed indefinitely.

For the next round, ask for a single relation containing the proposed repair comparisons and satisfying universal defence and protection of its registered models. The relation may be partial where the axioms leave choices, but the defence disjunctions must be jointly satisfiable—not checked independently.

In particular:

- Do not preserve every comparison from an additive certificate.
- Do not equate an unassigned comparison with a refusal.
- Do not accept every geometrically available repair.
- Propagate both positive and negative consequences of (TC).
- Include the splice rivals that defeated the previous cycle from the beginning.

A certificate is useful only if it establishes the joint obligations. It need not be additive, complete, or transitive.

### 5. Make the continuum test unavoidable

The main deliverable should quantify over arbitrary measurable fill sets, including arbitrarily small ones. A new finite-cell cycle is not the target.

For any proposed repair \(B(C,E)\), require the proof to address:

- overlapping and nested \(E\);
- all common-context copies;
- two repairs whose records compose;
- a repair followed by a defence comparison;
- the same rival compared with nearby selected sources.

The last item is essential. Varying both the source and the rival does not test closed sections.

A productive adversarial configuration is:

> Fix one rival X, approach a source through two different repair branches, and determine whether the accepted comparisons force an incoherent all-world tie at the limit.

That tests the coexistence of the branches rather than merely their separate geometry.

### 6. Keep the successful one-dimensional module as a benchmark

PP69 should not be discarded. It provides a demanding benchmark that a new mechanism ought to match:

- all measurable rivals;
- a non-isolated coherent family;
- repeatable repairs;
- closed sections along that family.

But its complete additive rows should not be frozen into the new construction. Preserve the successful *obligations* where possible, not every verdict used to witness them.

Also correct the “two-dimensional sheet” claim before using it strategically. Off-curve accumulation does not establish a sheet, and Proposition 5.3 does not apply to arbitrary transitive rankings.

### 7. Define success and failure precisely

**Substantial success:** one mixed-class, measurable repair mechanism that handles the rivals generated by its own defenders, with universal defence, protection, (IB), (TC), and closed sections on a non-isolated assigned family.

That is still not full coverage, but it would introduce the missing mechanism rather than another safe fragment.

**Useful failure:** a proof that the mixed-class obligations themselves conflict, with no additive certificate, fixed successor, symmetry or guidance-worsening assumption doing the work.

**Insufficient outcomes:** another finite cycle, another curve without its other-class rivals, or another conditional theorem saying that a consistent completion would give coverage.

The main moral is this: **the last round studied recurrence under a single repair direction, while the full problem requires several directions.** We should now exploit that difference constructively. Mixed-class repair may avoid both the forced descent of the chain and the same-world cycles that defeated recurrent designs. Whether it survives measurable rivals and sections is the right next question—not yet another alteration of a class-3 mechanism.