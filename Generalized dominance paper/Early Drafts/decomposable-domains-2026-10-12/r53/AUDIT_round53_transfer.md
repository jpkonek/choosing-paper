**The collaborator’s objection is right: the addition lemma alone does not address the angular comparisons responsible for the kink. I would change the plan, rather than begin another construction with additive gates on those comparisons.**

I have worked out a transfer theorem that simplifies the task substantially: **a sufficiently strong bounded-disagreement construction can handle *all* disagreements. We do not necessarily need two separately designed layers or a subsequent mixed-triangle extension.**

This is a reduction, not a solution. Its value is that it identifies exactly what the bounded construction must deliver—and which continuity requirement remains genuinely difficult.

### The new step: compress every disagreement into one annulus

Let
\[
A=\{g:1<\|g\|<2\}.
\]
Map every nonzero gamble into \(A\), preserving its direction:
\[
F(r\theta)=\left(1+\frac{r}{1+r}\right)\theta.
\]

This is a bijection preserving null sets in both directions. Crucially, **coherent models give the same advice at \(g\) and \(F(g)\)**.

Encode any model \(X\) as \(JX\): put its compressed advice inside \(A\), and put the same fixed background advice outside \(A\). Every comparison between encoded models now has bounded disagreement.

Given a relation \(Q_i\), define
\[
X\preceq_i Y
\quad\Longleftrightarrow\quad
JX\,Q_i\,JY.
\]

Then:

- **(G), (IB), and (TC) transfer directly** from \(Q\).
- If \(Q\) defends every selected coherent model against every modification inside \(A\), the transported relation defends it against **every measurable rival**, including angularly local cone rivals.
- Protection against domination and against all-world ties transfers in the same way.

The defence argument uses (IB). Comparing \(JC_a\) with \(JX\) is the same disagreement as comparing the actual coherent model \(C_a\) with a rival that equals \(JX\) inside \(A\) and equals \(C_a\) outside.

**So a universal bounded-modification construction is already much more than a small local module.** Its relational properties can solve the corresponding unbounded and angular problems too.

### The important catch: which sections must close?

We need, for every fixed measurable advice assignment \(Z\) on \(A\),
\[
\{a:JC_a\,Q_i\,JZ\}
\]
to be closed.

Call this the **annular section condition**. It fixes the rival’s advice inside the annulus and varies the selected coherent advice there.

The earlier addition lemma does **not** establish this condition. When we rewrite the comparison as \(C_a\,Q_i\,X_a\), the rival \(X_a\) changes outside the annulus with \(a\). That is precisely where the previous argument stops.

This distinction prevents us from falsely claiming that the difficult part has disappeared. But it also removes an unnecessary burden: **we can design one relation on the annulus, rather than one local relation, another cross-class relation, and a separate mechanism to reconcile them.**

I have written the proof and limitations in [Radial transport and the next milestone](</Users/jk13942/Documents/CPMs/outputs/decomposable-domain-audit/round53/Radial transport and the next milestone.md>). It is author-checked, not refereed.

### Answers to the collaborator’s questions

**1. Which cross-class rule?**

I would not start with either per-model additive gates or another continuous-integral quorum. Those are optional restrictions, and the proposed angular-Bayes check would largely investigate why the same restrictions fail again.

Instead, **replace the two-layer construction with one annular rule**. Angular complexity remains, but no separate rule for unbounded records is needed.

I do not yet have a successful explicit formula for that rule. It would be misleading to label another untested scoring formula a breakthrough. The concrete advance here is a transfer theorem that eliminates an entire extension problem.

**2. Is continuity along the selection acceptable?**

Yes—but require **closed annular sections**, not continuity of all verdicts.

A proof by continuity is acceptable if it works. It must not silently reintroduce closedness as the rival varies, which is the stronger assumption used in PP52’s obstruction.

**3. Must the local rule defend on its own? What about votes?**

Yes. Under this approach, it must defend every selected coherent trace against every measurable rival on the annulus, on the appropriate support. This is the substantive construction task.

Weak votes are permitted if (TC) is separately proved. But I would not make four judges—or any fixed voting architecture—a requirement. The earlier strict-vote example demonstrated compatibility of certain structural properties; it was not a proposed solution to universal defence.

The PP32 check can be a short diagnostic. It should not become the main round.

**4. Design jointly or sequentially?**

Jointly. Under the annular formulation, there is only one relation to design. Its accepted comparisons, refusals, support defences, and section behaviour must be chosen together.

Do not first install all comparisons favoured by some evaluators and then try to delete the problematic ones. That commitment has repeatedly created the obstruction.

**5. Module or sufficiency theorem?**

Both—but use the transfer theorem above as the sufficiency framework, rather than commissioning another general theorem with an unknown compatibility condition.

The first module should include the kink configuration **and varying nearby selected models**, against arbitrary measurable annular rivals. Three isolated selected models cannot test the section requirement adequately.

### A sharper brief for the next round

I would give the constructors this objective:

> Construct one disagreement-based relation on measurable advice assignments in an annulus. It must satisfy (G), (IB), and (TC); defend and protect the specified coherent traces against every measurable rival; and have closed sections when the rival is fixed and the coherent trace varies. Verdicts may be discontinuous when the rival varies. No additive gate, Bayes representation, fixed electorate, or prohibition of single-world ties is prescribed.

The work should proceed through three decisive checks:

1. **Universal rival defence and protection.** Solve these for the kink triple with arbitrary measurable splits—not indivisible cells, and not merely comparisons among the three selected models.
2. **Moving-source sections.** Extend to a continuously varying coherent family near the triple while keeping each fixed-rival section closed. This must be an explicit part of the construction, not a promised later consequence.
3. **Global continuation.** Extend the same rule to the posterior family’s edges and vertices. Radial transport then handles all original measurable rivals automatically.

The adversary should attack those exact claims, rather than impose an additive representation and rediscover the kink.

**The ambition should be to construct a complete rule on a bounded problem space that transfers globally—not another safe collection of exceptional comparisons.** Compression does not make the mathematics easy or remove the kink. It does show that “bounded versus angular” need not split the project into two difficult constructions, and it places the remaining difficulty squarely in one place: universal defence together with the correct, fixed-rival section condition.