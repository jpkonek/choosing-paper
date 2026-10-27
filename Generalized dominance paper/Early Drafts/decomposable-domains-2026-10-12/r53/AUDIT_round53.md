**Round 52 is genuine progress, but it does not justify another round whose main task is finding a smaller family for the same gates.** The four-model constructions establish something we previously lacked. The kink obstruction then shows why that success does not extend through the posterior family.

I have done two pieces of work that change my recommendation:

1. A topological argument rules out the proposed **continuous posterior-tripod completion** over the whole simplex.
2. A positive construction lemma shows how to obtain **(G), (IB), (TC), and closed fixed-rival sections without requiring continuous verdicts as rivals vary**.

The second result opens a materially different construction route. It does not yet deliver coverage.

## What to retain—and correct—from round 52

The four-model results answer the checkpoint I proposed. They should be retained as a positive result: actual gate fields can have compatible triples without globally compatible constants. That was not merely another numerical near-miss.

The kink theorem is correspondingly useful. But its scope remains the gate architecture, including the stated Bayes and compatibility assumptions. It does not show that the posterior family itself is unsuitable for general ordinal rankings.

There are also two qualifications to PP52:

- Its “rule-independent” obstruction assumes **closed verdicts along paths of changing rivals**. That is stronger than (S), which fixes the rival and varies the selected model.
- Proposition 7.3’s written padding argument excludes one alternative realiser. It does not, as written, establish uniqueness among a continuum of realisers. That needs an additional argument. The selective kink exclusion also remains conjectural.

These distinctions are construction opportunities, not minor qualifications.

## First result: the continuous tripod is not a global escape

Suppose the selection has the form
\[
a\longmapsto C_{f(a)},
\]
where \(C_b\) is the posterior family and \(f:\Delta\to\Delta\) is continuous.

Competitiveness on the support of \(a\), together with strict (G), forces
\[
\operatorname{supp}f(a)\subseteq\operatorname{supp}a.
\]
Otherwise, the selected credal set puts probability outside that face. There are then problems on which every world in the face benefits from replacing its advice by the correct answer. That contradicts competitiveness there.

Thus \(f\) preserves faces. **Every continuous face-preserving map of the simplex onto itself is surjective.**

Here is a short proof. Fix an interior \(q\), and set
\[
F_i=\{a:f_i(a)\ge q_i\}.
\]
These sets are closed. On each face, their corresponding members cover that face because the coordinates of \(f(a)\) supported there sum to one. KKM supplies a point in every \(F_i\). Since both vectors sum to one, \(f(a)=q\).

Consequently:

> A continuous whole-simplex posterior selection cannot avoid the kink neighbourhood by mapping its indices onto a tripod or another locally null subset of posterior models.

A **local** tripod remains possible. A discontinuous selection with closed sections is not excluded by this argument. But “construct a tripod now and continuously complete it later” is not a viable global plan under the present hypotheses.

I would therefore remove that route from the lead position.

## The positive idea: separate changes of advice from changes of coherent model

The repeated constructions have treated these two kinds of variation with the same continuity machinery:

- changing a coherent selected model;
- changing a rival on part of gamble space.

They are fundamentally different because coherent models are cones.

**Two distinct coherent models cannot differ only on a bounded set of gambles.** Their disagreement extends along rays.

That elementary fact yields the following useful theorem.

### Arbitrary bounded-disagreement additions preserve closed sections

Start with any relation having closed fixed-rival sections along a continuous coherent selection. Add any collection of comparisons whose disagreement sets are bounded.

**The resulting relation still has closed fixed-rival sections.**

For a fixed rival \(X\), at most one coherent model can differ from \(X\) only on a bounded set. Therefore the additions can change its section only by adding the closed fibre of that one coherent model. Adding a closed fibre to a closed section preserves closedness.

The added verdicts can be discontinuous as the rival changes. No integral representation or closed gate region is needed.

This is an **addition theorem**, not permission to delete comparisons arbitrarily. Deleting a comparison at the limiting model could still break a section.

It also extends beyond bounded disagreements. One can use any collection of disagreement sets closed under subsets and finite unions that contains no non-null cone. For example, sets having finite total radial length along almost every direction qualify, even when they are unbounded.

Thus this is not protection of one fixed bounded patch.

### A concrete construction follows

Let \(Q_i\) be any disagreement-based relation satisfying (G) and (TC). Define
\[
X\preceq_i Y
\quad\Longleftrightarrow\quad
\begin{cases}
X\text{ is pointwise no worse than }Y\text{ at }i;\\
\text{or}\\
X,Y\text{ differ on a bounded set and }X\,Q_i\,Y.
\end{cases}
\]

This relation satisfies:

- **(G);**
- **(IB);**
- **(TC);**
- **closed fixed-rival sections along every continuous coherent selection.**

The (TC) proof is short. In an accepted triangle:

- if two disagreements are bounded, the third is bounded too, so \(Q_i\) handles the triangle;
- otherwise at least two links are guidance comparisons, and the remaining link cannot reverse their composite without violating strict (G).

The same proof works for the larger collections of disagreement sets just described.

For an explicit nontransitive \(Q_i\), use four strictly guiding judges and accept a nontrivial comparison when **at least three strictly favour it**. Such a rule has no directed triangle: three accepted links require nine votes, whereas four judges can supply at most eight votes around a strict triangle. It can have strict four-cycles. Reflexivity is added separately.

The voting mechanism itself is familiar from our earlier work. **The new contribution is the construction theorem showing how such discontinuous verdicts coexist with the section requirement, without a shrinking-margin device or continuous gate fields.**

I have written the proofs and limitations in [Section topology and local comparison freedom](</Users/jk13942/Documents/CPMs/outputs/decomposable-domain-audit/round52/Section topology and local comparison freedom.md>). They are author-checked, not independently refereed.

## What this achieves—and what it leaves open

This gives an actual class of relations satisfying four requirements simultaneously. It shows that the continuity assumption driving PP52’s obstruction need not be built into the next construction.

It **does not** establish:

- the defence clause of (S);
- T’s undominatedness;
- (LA) or (C);
- absence of an additive endorser.

A four-cycle alone does not establish the last point: a weak endorser could tie its members.

Nor should we keep an additive rule on all remaining disagreements. That would repeat the earlier mistake of placing exceptional comparisons inside an otherwise additive construction.

## The next ambitious construction

I recommend designing the ranking on **two kinds of disagreement**, with neither governed by a frozen additive field:

1. **Disagreements that cannot separate two distinct coherent models.** Use the freedom proved above. Verdicts may be discontinuous as rivals vary, and need not arise from gates.
2. **Disagreements that can separate coherent models.** Design these jointly with the selected family, including the boundary. These comparisons must supply the remaining support defences and control how the first kind interacts with them.

This gives an exact simplification of (TC). Declare two models related when their disagreement belongs to the chosen collection of “small along rays” sets. A triangle is then either:

- entirely within one such class;
- between three different classes;
- or has exactly one within-class link and two between-class links.

The first case is already handled by the construction theorem. **The decisive new problem is the third case:** a local defence followed by two comparisons involving other coherent possibilities.

This is not solved by the lemma. But it is a sharper and less restrictive construction problem than searching for another family of Bayes gates. In particular, the local verdict need not obey the continuity or linear inequalities responsible for the kink proof.

One important safeguard: the local rule must still depend on the disagreement. It cannot secretly use “the coherent model in this class,” since changing the common context can change that model and violate (IB).

## Revised brief for round 53

I would give the collaborator these instructions:

1. **Check the two lemmas above first.** In particular, verify the section-preserving addition theorem and the mixed-triangle proof. Also confirm the face-preserving obstruction to continuous posterior tripods.
2. **Retain the posterior family for the first test, but abandon per-model additive gates as the default architecture.** Use the exact kink triple as the test case.
3. **Construct verdicts for its arbitrary measurable local modifications, allowing discontinuity along rival mass paths.** Require (G), (IB), (TC), and support defence. Do not impose own-Bayes conditions, closed gate verdicts, strict CG2, or absence of single-world ties.
4. **Then solve the mixed triangles with comparisons between different coherent models.** Include all common-context copies. A solution that handles only comparisons among selected models does not count.
5. **Keep the whole-simplex section obligation visible.** The addition lemma supplies one part of the proof; it does not excuse an unresolved global base relation.

**The strategic change is to stop using continuity of evaluators to obtain closed sections automatically.** We now have a direct section argument that permits substantially more relational freedom. That is the opening I would pursue before another tripod, fan, or half-plane gate family.

We still do not have a cover. But this round need not end with “try a different shape”: there is a proved way to remove one of the architectural restrictions that has repeatedly blocked the constructions.