# Maximal score-consistent extensions preserving coherent admissibility (auditor, 27 Oct 2026; verbatim)

New audit argument, not independently refereed. This note does not amend the definitive manuscripts.

## Setting

Use the full gamble domain, models modulo null sets, and the measure and separable order-unit hypotheses of the application's repair theorem. Write C for the coherent class and s_w(X) for integrated payoff. Equal models have reflexive comparisons. Only non-null changes are considered below.

A change r=(A,B) adds A and removes B. It is available to Z when B is contained in Z and Z misses A, modulo null sets. Its increment d_w(r)=integral_A h(w)-integral_B h(w) does not depend on the starting model to which it is available.

Let P(r)={w:d_w(r)>0} and H(r)={w:r is guided at w}. Let V(r) be the worlds accepting r. Independence means V(r) depends only on (A,B), modulo null sets. Guidance and strict score consistency are exactly

    H(r) subset V(r) subset P(r).

The strict score assumption concerns non-null comparisons only. It excludes reverse comparisons whenever a comparison is accepted, and therefore gives strict guidance, absence of distinct-model ties, and finite-chain consistency.

## Exact protection condition

For a relation satisfying these assumptions, every coherent model is undominated if and only if

    V(r) != Omega whenever r is available to a coherent model.

Proof. If such an r is accepted everywhere, apply it to a coherent starting model C. The resulting distinct model strictly improves its score at every world, so every reverse is refused and C is dominated. Conversely, any dominator of a coherent C supplies such an everywhere-accepted change, by independence and strict score consistency.

Only changes with P(r)=Omega can threaten protection. If an increment is nonpositive somewhere, score consistency already prevents acceptance everywhere. Call r dangerous, for this note only, when it is available to a coherent model and P(r)=Omega.

For a dangerous change, H(r) != Omega. Otherwise it would be an everywhere-guided non-null change available to a coherent model, which the application's guidance-protection lemma excludes. This fact uses the application's actual setting and measure assumptions.

## Axiom package

Consider rankings satisfying:

1. reflexivity and strict guidance;
2. independence;
3. strict score consistency;
4. every coherent model is undominated under this ranking;
5. inclusion-maximality among rankings satisfying 1--4.

Condition 4 is single-ranking protection of all coherent models, stronger than family-level admissibility (each coherent model protected under some ranking). It is not the assertion that all undominated models are coherent. Condition 5 is a proposed comparison-enrichment principle, not an established accuracy axiom.

## Characterisation and existence

The maximal rankings are exactly the following. For each dangerous r choose one world j(r) outside H(r). Set

    V(r)=P(r)                         if r is not dangerous;
    V(r)=Omega minus {j(r)}           if r is dangerous.

Handle null changes by accepting them everywhere. Choices must be made on equivalence classes of changes, not separately for their different starting models.

Proof of sufficiency. Guidance is retained because j(r) is never a guidance world. Every acceptance is strictly score-improving. Independence is built in. The exact protection condition holds. Every remaining positive-score comparison is the sole refusal of a dangerous change; adding it and all its independence copies would dominate a coherent starting model. Nonpositive comparisons cannot be added under score consistency. Hence the relation is maximal.

Proof of necessity. For a non-dangerous change, any omitted positive-score comparison can be added, with all copies, without violating protection. For a dangerous change, at least one refusal is necessary. If two worlds refuse, adding the comparison at one of them preserves the other refusal and protection; maximality fails. The unique refusal cannot be at a guidance world.

Existence holds for arbitrary sets of worlds by choosing a nonguidance world for every dangerous change (using choice in that generality). No limiting argument over a chain of rankings is needed. Such a chain argument would be unsafe in infinite worlds: its union could accept a dangerous change everywhere although every stage still refuses it somewhere.

## Coverage theorem

Every maximal ranking above extends the application's present ranking and covers every coherent target.

Proof. The present ranking accepts guidance, and every positive-score change unavailable to coherent models. The formula retains all those comparisons. The repair theorem gives each incoherent X a coherent N, with a uniform positive score increment, through a change unavailable to every coherent model. Every maximal ranking therefore accepts N over X at every world. The reverse is excluded by score consistency. Coherent N is undominated by condition 4. Thus the undominated models are exactly the coherent ones, and every incoherent model is uniformly dominated by a coherent one. All-world tie closure follows from the absence of distinct-model ties. Local freedom is automatic on the full domain. Strict guidance, independence and finite-chain consistency were established above.

There is no assumption that each incoherent model is dominated in the axiom package. That is derived using the repair theorem.

## A broader class containing the original ranking

Let R0 be the original ranking and Rmax any maximal ranking above. Every relation R with R0 subset R subset Rmax that is reflexive and independent has the same coverage conclusion and strict score consistency. Protection is inherited downward from Rmax; the repairs are inherited upward from R0. Finite-chain consistency follows from score consistency. Thus there is a class including both the current construction and its maximal extensions. The maximal axiom package itself generally excludes R0, since R0 withholds more comparisons than protection requires.

## What is and is not established

- The original ban on non-guidance comparisons available to coherent models is unnecessary for universal coverage. The formula gives its exact relaxation within strict score-consistent, independent rankings with single-ranking protection of every coherent model.
- Score improvement at one world can be accepted even if the change is available to a coherent model. If the same change does not improve the score everywhere, all of its positive-score verdicts may be accepted. If it improves everywhere, one refusal suffices.
- The rule for selecting the refusing world is not determined by the axioms. Maximality need not preserve symmetry, and an independent philosophical justification for it remains to be supplied.
- The rankings need not be transitive or complete. Disjoint additivity is not supplied by this construction: world choices for different changes can conflict when disjoint changes are combined. It is not part of the present covering definition. Do not claim that the construction meets it without another proof.
- If disjoint additivity is required, the above maximality characterisation no longer applies unchanged. In finitely many worlds, one can instead use Zorn to extend R0 maximally within score-consistent, independent, disjoint-additive, guidance-respecting rankings protecting C: chain unions preserve the finitary conditions, and finite-world protection survives a union. Every such extension covers because it contains R0. This argument is not asserted for arbitrary worlds.
- The result is relative to the integrated-payoff score and the existing repair theorem. It is not an abstract dominance theorem for arbitrary scores or arbitrary designated classes of models.
- It does not derive coherence from accuracy alone. It takes coherent admissibility as a substantive premise, but replaces the extra local prohibition by a general maximality principle.

## Suggested independent checks

Check the exact protection equivalence, necessity of the one-world refusal in the maximality characterisation, null-set invariance, the infinite-world choice argument, and which extra requirements (especially disjoint additivity or symmetry) change the conclusion. Keep the philosophical appraisal separate from these mathematical checks.
