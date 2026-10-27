**The next round should build the missing defences, not further strengthen the non-additive example.** We now have an explicit mechanism with (G), (IB), (TC), closed sections, and indispensable non-additive defences out of coherent undominated models. But its protection of incoherent models makes it unusable as it stands.

I suggest sending the collaborator the following brief.

---

**Objective: construct a three-world covering system through T1 using the rescaled family, with non-additivity doing necessary work.**

Use
\[
K_p=\left\{\frac{p*m}{p\cdot m}:m\in T1\right\}.
\]
Treat these as proposed selections. Their membership in \(\mathcal C_R\) remains something to prove. Do not assume that they exhaust \(\mathcal C_R\).

Do **not** preserve the entire new ranking. Preserve, if possible, its finite non-additivity certificate and indispensable defences. The bulk of its comparisons are expendable.

**1. Put the non-additive certificate inside the proposed family.**

The current certificate uses T1 and three other coherent models, but those three were not constructed as posterior family members. Resolve that mismatch first.

Find four indices \(p_0=u,p_1,p_2,p_3\) and four positive-measure regions \(B_0,\ldots,B_3\) such that:

- \(C_{p_j}\) is silent on \(B_j\);
- it gives world-1-correct advice on each other \(B_k\);
- the regions have the same sign pattern.

These conditions reproduce the existing finite certificate using actual proposed selections.

This is a concrete geometric problem: search for separating gambles against the vertices of the four credal sets, then verify strict inequalities with rational arithmetic. Numerical search is appropriate here because it is finding a finite geometric witness, not pretending to verify (S).

**Success would give non-additivity that any covering construction retaining those defences must possess.** Failure of these particular geometric conditions would require a different certificate, not an impossibility claim.

**2. Reverse the construction problem: find coherent repairs of rivals.**

Previous rounds mostly asked, “Which world should defend this selected model?” That repeatedly protected coherent and incoherent models alike.

Instead ask:

> Given a rival \(X\), which posterior model could replace it, and what in their disagreement justifies that replacement?

Here is a specific geometric lemma to attack.

For every \(X\) outside the proposed family, seek \(C_p\) such that:

- **No guidance obstruction:** at no world is \(X\) a strict pointwise improvement over \(C_p\).
- **The disagreement exposes the rival:** no family member agrees with \(X\) everywhere on the disagreement between \(C_p\) and \(X\).

Writing \(D=\{g:C_p(g)\ne X(g)\}\), the second condition is
\[
\forall q,\qquad
\mu\{g\in D:C_q(g)\ne X(g)\}>0.
\]

Its significance is concrete. If we declare \(C_p\) no worse than \(X\), independence transports that comparison to other contexts. But the losing advice pattern on \(D\) cannot occur in any proposed selected model. **The new comparison therefore cannot, by that direct transport, make a selected model lose.**

This uses the old idea of coherent explanations, but asks a new substantive question: **can such comparisons supply coherent replacements for arbitrary rivals?** It does not rank records by margins or choose a preferred explanation greedily.

Do not impose either condition on every accepted comparison. They are proposed sufficient conditions for a useful class of repair comparisons.

A counterexample to this lemma should be explicit and geometrically explained. It would reject this repair mechanism, not the axioms.

**3. Turn those repairs into a relation—and confront (TC) immediately.**

For successful repair pairs, generate their comparison records and all their (IB) copies. Combine them with guidance and the retained non-additive certificate.

The central proof obligation is now specific:

> Can repair records coexist without producing a forbidden three-model reversal?

Check actual compositions of records, including comparisons involving two repairs and one guidance comparison. A repair’s coherent source in its original context does not guarantee that its other contexts are coherent.

Do not use unrestricted addition of trades, a common endorsing weight, or a fixed priority order to obtain this proof. Those would change the construction being investigated.

**4. Prove both clauses of (S), separately.**

Even successful coherent repairs do not establish (S) under (TC). In particular, **do not compose comparisons as though transitivity were available.**

The completed relation must independently establish:

- every proposed selected model has a defender against every rival on the appropriate support;
- for each fixed rival, the acceptance sections in \(p\) are closed.

Do not require the whole comparison relation to be closed. The new example achieved that stronger property, but it is not an obligation for its successor.

Also calculate the actual undominated class. Do not identify it with the chosen family by definition.

---

**The highest-priority task is the repair lemma, not another finite allocation search.** It asks whether the rescaled family has the geometric property needed for a genuinely different construction: using disagreement to recognize an unacceptable advice pattern and justify its replacement.

There are three worthwhile outcomes for this round:

1. An explicit repair rule with a continuum proof of its geometric properties and compatibility with (TC).
2. A complete covering construction, with both clauses of (S) checked.
3. An exact obstruction showing why this proposed repair mechanism cannot work.

Another collection of non-additive comparisons, another finite satisfying assignment, or another claim that “only one lemma remains” would not meet the objective.

The important change is this: **we should now use non-additivity to distinguish coherent advice from incoherent advice—not merely to keep selected models unbeaten.** The new construction demonstrates how much can be achieved while entirely missing that distinction.