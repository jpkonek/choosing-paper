**Round 47 followed the intended brief, but it did not deliver the intended extension mechanism.** It made a useful advance in understanding which comparisons can coexist. The proposed two-weighting construction, however, risks returning to the same additive patching approach unless its specification changes.

I read the brief and PP28–PP30. PP32 and the new referee report are not in the local copy, so I cannot independently endorse their proofs.

### What the round achieved

**PP28’s separation lemma is the strongest constructive insight.** Two selected models can generate the dangerous decomposition of an inverted departure only if their credal sets are disjoint. This explains why allowing the coherent family to vary really matters: some conflicts disappear through the geometry of the selected models, without changing the axioms.

But the conclusion is conditional. Overlapping credal sets prevent **this particular conflict**; they do not guarantee that adding a model preserves all its defence obligations, undominatedness or closed sections. “Overlap is free” needs that qualification.

**PP29 also answers the intended question.** The support obligations do not, by themselves, force the two pieces of one dangerous decomposition onto the same world. That removes an apparent obstruction. Its allocation cannot simply be applied independently to every departure, however: a comparison can participate in several decompositions.

**PP30 supplies a particularly important constraint on the next construction.** T’s defence against a rival transfers, through (IB), into other contexts. Consequently, we cannot retain all the ordinary \(|g_i|\)-weighted comparisons out of even one precise model—not even a vertex model—while making T competitive.

That last result directly bears on the proposed next round.

### Where execution fell short

The brief explicitly required closed sections to constrain the construction from the beginning. PP28 instead supplies:

> A certificate layer that preserves closed sections, **provided the base already has them**.

That is a useful preservation theorem, but the explicit base does not have them. Nor does its growth rule establish that an enlarged base with those properties exists.

Moreover, a base already satisfying full support competitiveness, closed sections and the required protection of its coherent selections would already have solved much of the difficult existence problem. Adding a safe class of non-additive comparisons afterwards cannot substitute for constructing that base.

So the brief was appropriate; **the implementation solved the certificate-compatibility part while leaving the central extension step open.** The notes mostly acknowledge this, but the next-round proposal obscures it.

### Why “two weightings” is not yet a construction

The observations

- T is Bayes for the balanced field; and
- precise edge models are Bayes for the stake-weighted field

do not establish compatibility between their comparisons. In particular, a balanced primary field can make many regular models tie. T being a minimiser there is a weak fact.

More decisively, **PP30 already excludes preserving the stake-weighted verdicts wholesale at the edges or vertices.** The same disagreement may occur both in a comparison involving T and in one involving an edge model. Under (IB), it receives one verdict, regardless of which part of the selection produced it.

Thus:

> Two fields may help propose comparisons. They cannot define two independently functioning parts of the ranking.

A boundary layer in index space does not resolve this shared-record problem.

Also, PP32’s wording needs clarification before it becomes a foundation. A weighting of worlds, a collection of world-specific densities on problems, and an additive loss with separate advice penalties are different objects. The reported conclusion that every interior selected model must be precise is especially strong. The next report must give its exact quantifiers and explain its relationship to the previously covered imprecise additive examples.

### My instructions for the next round

**Make the main task a joint construction of the forced defences and their replacement dominators. Do not make it another interpolation between additive systems.**

PP30 gives an explicit family on which to do this.

Fix a precise model \(D_p\) and a bounded measurable \(G\) inside T’s silent region. Define:

\[
X=T[G\mapsto D_p],\qquad
R=D_p[G\mapsto\text{silence}].
\]

T must defend against \(X\) at some world \(w\). Independence then requires

\[
R\preceq_w D_p.
\]

For a non-null \(E\subseteq G\), let \(Z\) be \(R\) with the correct answer at \(w\) restored on \(E\). Guidance and (TC) force

\[
D_p\not\preceq_w Z.
\]

Yet \(Z\), being an incoherent bounded modification, needs a coherent dominator under the desired full system. **Choose that dominator as part of the construction**, rather than selecting it from an already fixed family.

The next round should therefore deliver the following.

1. **Choose the defence world and the replacement credal set jointly.**  
   Construct a rule producing \(w\) and \(K\), with \(D_K\preceq_i Z\) at every world, while preserving T’s undominatedness. The choice of \(K\) must remain genuinely variable.

2. **Handle the entire measurable family, not a single example.**  
   Start with all three vertex models, arbitrary admissible \(G\), and arbitrarily small \(E\). This tests the unavoidable boundary obligations without prematurely prescribing an edge family.

3. **Register every new defender and include its obligations.**  
   A defender cannot merely dominate the rival it was introduced for. Its comparisons with T, the other defenders and their rivals must also be handled. Check shared disagreement records and mixed triangles across different choices of \(G\) and \(E\).

4. **Include the section constraint in the rule.**  
   State where each new defender is selected and prove the relevant fixed-rival sections closed. Relative closedness on a partial index domain must be labelled as such; it is not a substitute for extension to the simplex.

5. **Use the two additive fields only as optional witnesses.**  
   Retain neither field’s complete comparison set. A verdict may agree with either field, both or neither. Any restriction requiring one of them to endorse every accepted comparison must be stated and justified separately.

There is one further restriction to remove: **do not require T to dominate every inverted departure, with every reverse refused.** PP29 shows that this universal commitment itself creates additional exclusions. Keep only those certificate comparisons that the construction actually needs; other incoherent rivals may have different coherent dominators.

The success criterion should be a **repeatable extension rule that survives adding its own defenders**, with a proved invariant—not another safe collection of comparisons whose missing base must already satisfy (S).

This remains difficult, and I do not have that extension theorem. But it targets what the latest results actually reveal: **defending T changes comparisons elsewhere, which displaces existing dominators. The construction must solve both effects together.** Patching the scores first and finding replacement dominators afterwards repeats the failure we now understand.