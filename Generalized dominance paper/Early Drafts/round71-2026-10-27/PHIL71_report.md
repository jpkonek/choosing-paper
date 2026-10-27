# PHIL71: justification of replacements for condition (3) of Prop 6.3 (27 Oct 2026)

## Recommendations

1. **Reject P1.** The refusing world cannot be chosen on principled grounds (see "Arbitrary choice" below).
2. **P2 (R∩) is not clearly better justified than P0.** It withholds fewer score comparisons. But it loses disjoint additivity (L4), and it makes verdicts depend on scores at other worlds in a perverse direction. Present it as an alternative with stated costs, not as the paper's ranking.
3. **Replace Prop 6.3's justificatory role with a P3-style sufficiency statement.** Keep R0 as the paper's ranking. R0 is the smallest member of the P3 class. Its verdict at a world depends only on scores at that world, it is disjointly additive, and its protection is proved rather than assumed. Prop 6.3 may stay as a description of R0 only.
4. **Revise the Introduction's "Dominance is proved, not assumed."** Under P3 as a general statement, protection of coherent models is a hypothesis. It is a theorem only for R0, via condition (3) and Lemma 6.5.

Paper-ready prose:

> Condition (3) is stronger than coverage requires. Suppose a ranking accepts every guided comparison, accepts a comparison between distinct models only when it strictly improves the score, judges a change only by what it adds and removes, and leaves every coherent model undominated. If it also accepts every change that no coherent model could make, at each world where that change improves the score, then it covers every credal set. Our ranking is the smallest such ranking. Larger ones exist, but they can lose disjoint additivity, and their verdict at one world can depend on scores at other worlds (Example X). In all of them the coherent class enters as a premise, so the result represents coherence rather than deriving it from accuracy.

## Where each package mentions the coherent class

| Package | Mentions the coherent class in | Form of that premise |
|---|---|---|
| P0 | (3) | local: one comparison at one world |
| P1 | protection (4) only | global: whole ranking, all worlds |
| P2 | protection (4); also "neutrality" as L3 states it (through "dangerous") | global |
| P3 | protection (4) and (5') | global, plus a lower bound on what must be accepted |

Neutrality can be stated without mentioning the coherent class: *if a change is accepted at some world where it is not guided, it is accepted at every unguided world where it improves the score.* With 1–4, this gives exactly R∩. (For a change improving everywhere and available to a coherent model, acceptance at one unguided world forces acceptance everywhere, which protection forbids.) So P2 needs the coherent class only in (4). So read, it is a world-impartiality principle with some independent appeal. **[math check: confirm.]**

## The principle "withhold no favourable comparison unless needed to protect coherent models"

It has two parts, and they have different standing.

- **"Withhold no favourable comparison."** Read as "record every score fact unless there is a reason not to", this part has independent standing. A refused comparison at w with a positive score difference amounts to a refusal to say what the accuracy measure says at w. This is the strongest ground for preferring P1–P3 to P0. Caveat: incompleteness is acceptable in this literature, so "more comparisons is better" is a methodological preference, not an accuracy axiom.
- **"Unless needed to protect coherent models."** This part names the coherent class, and it cannot be stated without it. In L4 the vacuous coherent model D_S is beaten **at every world** by the incoherent model D_S ∪ A. So integrated payoff alone does not favour coherence. Any ranking that protects coherent models must override the score in favour of the coherent class.

Verdict: the full principle presupposes the coherent class. Its only gain over (3) is where the presupposition sits. It sits in one premise, "coherent models are undominated", which is the companion paper's admissibility premise for a single ranking and half of the intended conclusion. It no longer sits in an unexplained ban on individual comparisons. The gain is real but modest; the verdict "represents, does not derive" stands.

## Package-by-package

**P0 (R0).** Strengths: the verdict at w uses only w's score, guidance at w, and one fact about the change that does not vary by world; it is disjointly additive; no choices are made; protection is proved. Weakness: (3) has no rationale. It withholds comparisons that threaten no one. In L3's two-world case, d ≈ (1,−2) is refused at world a only because a model that is precise at b could make the change, yet that change cannot dominate anything. §9.2's concession that (3) is unjustified is correct.

**P1 (auditor's maximal rankings).** Better than P0 on the first half of the principle. Costs:
- *Arbitrary choice.* The paper notes that multiplying a world's score by a positive constant leaves the ranking unchanged, because only signs matter (Scope, "The score"). Every change the auditor calls dangerous has the same sign pattern: it is positive everywhere. So no rule that respects this rescaling invariance can choose j(r) from the scores. Only H(r) and the identity of the change remain, and they do not settle it. The arbitrariness is ineliminable, not a gap awaiting a cleverer rule.
- *Dependence on other worlds.* Whether the change is refused at j depends on whether it improves everywhere.
- *No disjoint additivity* (L4).

**P2 (R∩).** It removes the arbitrariness by refusing at every unguided world: it levels down. Costs:
- *Dependence on other worlds, in a perverse direction.* Take a change with d = (1,−2). R∩ accepts it at a. If the change is made *better* at b, so that d = (1, ε), R∩ refuses it at a. An improvement elsewhere turns acceptance here into refusal. R0 never does this.
- *No disjoint additivity.* In L4, s and t are both accepted at x, but their disjoint union is refused there. Integrated payoff is itself additive over disjoint sets of gambles. Refusing a whole while accepting its disjoint parts shows the refusal protects coherent models rather than tracking accuracy at x. R0 also departs from the score (Example 6.4), but it does so through one criterion that is closed under disjoint unions.
- *Size-blindness.* Arguably no cost: under per-world rescaling invariance sizes are not comparable across worlds, so "refuse where the gain is smallest" is unavailable. The real cost is levelling down.
- *Change of logical form.* Prop 6.3 works at one fixed world; protection concerns the whole ranking, so P2 is not a drop-in replacement.

Net: P2 gains on minimal withholding and canonicity, loses locality and additivity, and depends no less on the coherent class. Better on one criterion, not better justified overall.

**P3 (class).** This is the best justified *as a theorem*. Its assumptions are strictly weaker than P0's, and R0 belongs to the class. (5') only **permits**: it never forces a refusal. Refusals are constrained only by protection. Weakness: it describes a class, so R0's distinguishing features (locality, additivity, proved protection) must be stated separately. (5') still mentions the coherent class. It cannot be weakened to "accept every change that improves everywhere", because by L4 that would leave D_S dominated.

## Open questions for the lead (math, not appraisal)

- Does disjoint additivity together with 1–4 and class-free neutrality have a largest member? Is it R0 when there are three or more worlds? If so, (3) would be **derived** from protection, impartiality and additivity, and only protection would mention the coherent class. That would be the best vindication of R0. L5 suggests failure in two worlds (R∩ ⊋ R0, apparently additive); then claim only that R0 is additive.
- Does the class-free neutrality version of P2 give exactly R∩ (sketch above)?
- Does P3 carry over to domains closed under coherent hulls (Cor 7.1)?
