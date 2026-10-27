**This round is more promising than the previous several rounds.** It presents a candidate continuous family through T with universal defence obligations and a mechanism for checking interactions between its rankings. That is closer to the milestone than another isolated repair module.

But I would not yet treat the cap-path theorem as established, and I would **not make extending the single path to an edge the main next task**. The unresolved interaction between different repairs comes first.

I have worked out a larger coherent family and an exact simplification of its compatibility conditions. The argument and audit findings are in [Independent corner cuts and gate compatibility](</Users/jk13942/Documents/CPMs/outputs/decomposable-domain-audit/multicap/Independent corner cuts and gate compatibility.md>).

### What PP42 gets right—and what needs repair

The strongest idea is **using different additive witnesses for different triples of gates**. To exclude a forbidden three-model configuration, one need not produce an additive witness for the entire ranking. This respects the distinction between (TC) and full transitivity.

The compact-family argument for closed sections is also useful: if models and their fields converge appropriately, the gate witnessing an accepted comparison has a convergent subsequence. Acceptance of zero-valued records then preserves the limiting comparison. This mechanism could apply well beyond the particular cap path.

However, I found several qualifications:

- **Theorem 2.1’s “if and only if” is too strong.** An additive witness endorsing every accepted comparison gives a necessary Bayes condition. A nonnegative witness value does not imply that the ranking accepts the comparison. Sufficiency holds for the maximal witness preorder, not an arbitrary subrelation.
- **CG2 and CG3 are not an unrestricted characterisation of (TC).** The necessity argument for CG2 has an additional agreement-region hypothesis. Strong CG3 is sufficient; the stated weak necessary condition is different.
- **The pointwise Bayes proof for the cap path needs repair.** Theorem 4.3(a) uses a bound defined through integrals as a pointwise bound. A suitable pointwise estimate may exist, but it must be supplied.
- **The claimed absence of every additive endorser is not yet established by the argument given.** The proof excludes a globally consistent collection of rescaling constants. Connecting that conclusion to every possible endorser needs an additional argument.
- Proposition 5.1 excludes its particular eventual-domination configuration under its uniformity hypothesis. It does not prove the subsequent general claim of “local finiteness”.

These do not show that the construction fails. They do mean that the report’s strongest conclusions need checking before another construction is built on them.

### The positive step I worked out: make the repairs independent coordinates

Instead of choosing one corner to cut, **allow all three corners to be cut independently**.

Write
\[
M=c\mathbf1+\varepsilon\Delta,\qquad c=(1-\varepsilon)/3.
\]
Choose \(0<\delta<\varepsilon/3\). For
\(\mathbf s=(s_1,s_2,s_3)\in[0,\delta]^3\), put
\[
K_{\mathbf s}
=
M\cap\bigcap_{i=1}^{3}
\{m:m_i\le c+\varepsilon-s_i\}.
\]

This gives a compact, three-parameter family of coherent models, with \(K_{\mathbf0}=M\). It contains individual caps, combinations of two caps, and combinations of all three.

**The useful theorem is that these cuts combine without creating additional advice elsewhere.**

Let \(H_i(s_i)\) be the problems where the corresponding single-cap model answers but T stays silent. Then, up to null sets,
\[
\{D_{K_{\mathbf s}}\ne T\}
=
H_1(s_1)\cup H_2(s_2)\cup H_3(s_3).
\]

These three sets are disjoint.

Here is the reason. The removed corners are disjoint. If a gamble is positive throughout the remaining credal set but not throughout \(M\), its nonpositive portion of \(M\) is connected and lies entirely in the removed corners. It must therefore lie in one corner. Cutting that corner alone already makes the gamble desirable.

All these credal sets contain the centre \(u\). Consequently, **at any particular problem, every member gives either silence or the same definite answer**. Members never recommend opposite answers.

I proved this directly and checked the identity in **80,000 exact rational instances**. The computation checks the geometry; the connectedness argument supplies the general proof.

This is not yet a ranking construction. Its significance is that we now have a coherent family in which repairs in three directions can be studied together, without repeatedly solving coherence or introducing a new family whenever a different corner needs attention.

### The compatibility problem becomes much simpler

For this family, three members never give three distinct advice values at one problem. Therefore **PP42’s extra CG3 inequalities on three distinct advice values disappear**.

What remains is the requirement that three pairwise scaling constraints admit common constants.

For a fixed world, write the allowable interval for
\(\log c_N-\log c_M\) as \(I_{NM}\). It is computed directly from PP42’s ratios of the two fields on their disagreement region.

For three models \(A,B,C\), common constants exist exactly when the individual intervals are nonempty and
\[
0\in I_{AB}+I_{BC}+I_{CA}.
\]

For finite closed bounds \(I_{NM}=[L_{NM},U_{NM}]\), this is simply
\[
L_{AB}+L_{BC}+L_{CA}\le0
\le U_{AB}+U_{BC}+U_{CA}.
\]

I give the short proof in the note. Strict feasible intervals provide a convenient stronger condition for the zero-accepting version.

**This is a concrete field-design problem, not another abstract extension lemma.** The constants may depend on the triple. Requiring one globally consistent set would introduce an unnecessary restriction.

### What must change in the fields

PP42 changes a cap’s field only where that cap differs from T. Its cross-cap conflict arises partly because it leaves the field unchanged on the other caps’ regions.

Remove that restriction.

For each \(K_{\mathbf s}\), allow its field to depend on **all three cut parameters on all three corner regions**, including regions where its model still stays silent. The requirements are that:

- its own model remains uniquely optimal at an appropriate supporting weighting;
- the pair and triple interval conditions hold;
- the fields have the regularity needed for the section argument.

The supporting weighting need not always be \(u\).

This is the co-design freedom we should exploit: **a model’s evaluator may anticipate the other repairs with which it must coexist**. There is no axiom requiring its field to remain equal to T’s wherever the two models agree.

### My proposed next round

I would replace “extend the cap path to the edge” as the principal task with:

> **Construct compatible fields for a small multidirectional family through T, including combined cuts, and use that family to handle the first recursive rivals.**

Concretely:

1. **Referee the cap-path foundation**, including the pointwise Bayes estimate and the precise scope of the compatibility theorem.
2. **Start with four models:** T, a cap at one vertex, a cap at another vertex, and their combined cut. Construct their fields jointly, allowing changes on both corner regions.
3. **Then construct the eight models obtained by independently switching three cuts on or off.** Check every pair and triple using the interval criterion.
4. **Seek a formula valid for an open range of cut sizes**, with uniform bounds and closed sections—not merely one successful finite configuration.
5. **Test the rivals the single-cap path misses**, especially fills by the caps’ own answers and their retreats. Let the combined-cut model be a possible defender, rather than forcing another isolated cap to do the job.
6. Only after simultaneous repairs work, extend a suitable two-dimensional portion of this family towards an edge.

The three cut parameters describe candidate geometry; they are not automatically probability indices, and the whole family need not become selected. The ranking and the eventual index map must determine which members qualify.

**The new opportunity is to replace a chain of isolated repairs with a coherent family that already contains their combinations.** That directly addresses why generation two keeps defeating these constructions. I have established the geometric part and reduced its sufficient (TC) test to explicit interval inequalities. The substantive remaining task is to build the fields jointly—without freezing them outside each model’s own disagreement region.