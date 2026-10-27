**I would change several defaults before starting.** The useful move is to isolate the equal-loss class \(H\). It would be a mistake to use that identification to reintroduce cancellation, register every posterior model, or return automatically to the old additive-generator constructions.

Two distinctions are especially important.

**First, (IB) is not a licence to add comparisons.** On the accept-or-silence restriction, a comparison can indeed be represented by the errors removed and the errors added. Common errors cancel from its description. But that is different from finite cancellation—the requirement that sums of acceptable trades remain acceptable.

Use the error-set representation. Do **not** assume finite cancellation, additive closure, or transitivity. Check precisely what N9.4 calls “cancellation”: if it means common-context independence, fine; if it means a stronger trading principle, it must be proved from our current axioms.

**Second, a zero-sum perturbation may preserve the very obstruction we are trying to escape.** Suppose PP66 assigns each record a vector \(v(r)\), accepts at world \(i\) exactly when \(v_i(r)\geq0\), and satisfies

\[
\sum_i v_i(r)=0,\qquad v(r^{-1})=-v(r).
\]

Then acceptance at all three worlds forces \(v(r)=0\). The reverse is also accepted everywhere, so there is no strict domination. Making the perturbation nonlinear, record-dependent or lopsided does not change that argument.

PP66 might still supply useful **individual witnesses**, but before adopting it as the mechanism, identify exactly how the final rule escapes this calculation. Otherwise we will reproduce the balanced-rule failure in new notation.

Here are my answers and the revised brief.

1. **Use \(H\) as a local test domain, not as an identification with the entire old U-domain problem.**

   Advice outside \(R\) is fixed, and the available coherent models, selected supports and indexing requirements may differ from the old setting. Restricting the full relation to \(H\) preserves some axioms, but does not automatically preserve the hypotheses of every full-cover theorem.

   Keep the record-based formulation primary. Error sets are an equivalent and potentially convenient representation here. Import old results individually, with their hypotheses stated. In particular, “blind endorsers are necessary” is not yet a construction principle.

2. **The separating principle should concern coherent completion of advice, not distance from a threshold.**

   There is a concrete geometric object worth computing. For an answer set \(X\subseteq R\), define its compatible likelihoods by

   \[
   \mathcal P(X)=\{m:C_m\text{ agrees with }X\text{ almost everywhere on }R\}.
   \]

   More usefully, impose agreement on specified subsets of \(R\), obtaining partial compatibility sets. Their defining acceptance inequalities are explicit.

   These sets tell us which advice requirements can coexist in a posterior model, and which combinations cannot. **They do not themselves define a ranking**, and \(\mathcal P(X)=\varnothing\) means “not represented by this posterior family”, not “incoherent”. Nevertheless, they provide information about the arrangement of advice that the balanced integrals discard.

   The constructive question is whether incompatible requirements can guide the choice of a defender and its necessary refusals. That is a more substantive direction than perturbing a conserved total.

3. **Every incoherent \(H\)-model is the eventual test; not every coherent \(H\)-model must be protected.**

   Protect T and the coherent models the construction actually needs. Other coherent models may be dominated.

   In particular, **do not register every nearby posterior model by default**. That is an enormous collection of additional defence obligations. We are co-designing the undominated family, not proving that a predetermined posterior neighbourhood is entirely undominated.

   Also distinguish “a posterior model considered as a candidate” from “a model committed to being undominated”. Geometry can examine many candidates without protecting all of them.

4. **Choose indices jointly with the relation.**

   Likelihood indexing is an available candidate, not the default constraint. A posterior parameter describes a coherent model; a selection index specifies the support on which that model must defend itself. Those roles need not coincide.

   The construction must eventually supply a genuine selection and closed fixed-rival sections. But an unsuccessful likelihood-indexed construction should not be reported as failure of the model family.

5. **Yes: “works twice” includes both kinds of splice.**

   Require uniform treatment of incoherent measurable splices between a source and its new defender, and between newly committed defenders. Include their common-context copies.

   This is the minimum test that prevents a repair from merely moving the unresolved problem to its output.

6. **Geometry and relation must develop together.**

   A theorem that a rescaling satisfies “every coupled refusal” is not purely geometric: refusals are relational commitments. Geometry can rule out candidates when guidance contradicts those commitments, but surviving that test does not establish relational compatibility.

   Ask the geometer for an explicit **candidate correspondence**, together with the necessary conditions it satisfies. Ask the constructor, concurrently, which additional conditions would make one candidate usable. Neither should assume the other half will follow.

**The central deliverable should change slightly.**

Do not ask merely for an operation that adds a dominator. Ask for an operation that outputs

\[
\boxed{\text{defender }B
\;+\;\text{required acceptances}
\;+\;\text{required refusals}
\;+\;\text{surviving defence options}.}
\]

It must preserve the existing obligations after common-context copying, (TC), and section closure. Its second application must handle rivals involving its first output.

There is an important constructive freedom here: **different rivals can have different coherent defenders, and competing candidate defenders need not all be installed.** A successful choice can therefore avoid obligations that would be unavoidable if we protected the whole posterior family in advance.

I would make that freedom the centre of the round. Use rescaling inequalities to expose the available choices, then select defenders according to which joint defence options remain—not according to a fixed score, nearest-model rule, or predetermined path.

That is an ambitious but concrete next step. The proposed defaults otherwise risk rebuilding the original problem with three unnecessary commitments: cancellation, universal registration of posterior models, and likelihood indexing.