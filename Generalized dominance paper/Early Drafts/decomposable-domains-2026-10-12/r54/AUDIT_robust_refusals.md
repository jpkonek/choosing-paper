# Round 53 review: robust refusals and the scope of the section obstruction

23 October 2026. Author-checked; not refereed. This note audits the written arguments, not the archived scripts.

## 1. Robust refusal lemma

Assume PP56's two-valued interior family S, its common balanced strictly guiding field u, and its continuous coherent selection. Let N=C_a be a selected model, fix a measurable rival X and a world w, and suppose X is strictly better than N at w on a non-null set.

Then there is a bounded strictly positive measurable multiplier q, common to all worlds, such that PP56's lexicographic construction using q u satisfies all of Theorem L's non-section conclusions and refuses C_b <=_w X throughout a neighbourhood of a.

Proof. Put d(g)=u_w(g,X(g))-u_w(g,N(g)). This is integrable and negative on a non-null set. Choose E contained in {d<0} with int_E d <0. Set q=1+K 1_E. For finite K sufficiently large,

    int q d = int d + K int_E d <0.

Multiplication by q preserves strict guidance and the pointwise common-weight Bayes inequalities used in Theorem L; q is bounded above and bounded below by 1. Use q u at the first level and its rational-box localisations at later levels. PP56's proof of the non-section axioms carries over verbatim.

For fixed X, continuity in measure of C_b and the integrable envelope give continuity of b -> int q[u_w(X)-u_w(C_b)]. This integral is strictly negative at a, so remains negative on a neighbourhood. The first level therefore refuses C_b <=_w X throughout that neighbourhood, including every sufficiently small pure w-improving shift. QED.

The lemma also applies to arbitrary measurable rivals, not only bounded swaps. No section conclusion for the resulting relation is claimed: it still has open sections elsewhere.

## 2. Quantifiers matter for the next proof attempt

For each fixed mixed rival and each specified world, a rule satisfying all non-section axioms can robustly refuse there. Thus those axioms cannot universally force acceptance at that world along all small pure shifts toward it for that rival.

This does not say that one rule can meet every required robust refusal simultaneously. Nor does it refute a theorem with quantifiers 'for every rule there exists a rival family producing a section failure'. A genuine negative route must couple demands across rivals, or choose the rival in dependence on the rule. It cannot prove the fixed-rival, fixed-world universal forcing statement contradicted above.

The positive next target is simultaneous robust refusal for several selected sources and their mutually inverse swap records, with universal defence still available elsewhere. Reweighting one common field is only a control construction: Theorem Q rules out using it as a global solution when balanced swaps remain.

## 3. Audit of PP55 Proposition SR

Part (a), the closedness of guidance sections under selection continuity, is correct for weak guidance.

Part (b) wrongly passes strict improvement to a limit. For example, if C_{b_k} is a pure w-worsening of C_a tending to C_a, X=C_a is strictly better than every C_{b_k}, but equal to the limit. Strict improvement is not preserved. This invalidates the stated justification that the set W_infinity contains all worlds available at the limiting index.

Part (c) does not follow from individual literals being unforced. Coupled disjunctions and actual section-limit implications can impose new restrictions even when no non-guidance literal is individually forced by a finite base instance. Finite propositional compactness does not automatically apply to an entire infinite-premise section implication.

This is not a disproof of every possible repaired finite-shadow theorem. It means the present proof does not justify the blanket claim that no finite reasoning can contribute to a section obstruction, or that a two-parameter family is logically necessary.

## 4. Scope of Theorems L and Q

Theorem L's central construction works under its two-valued, common-answer, interior-support hypotheses. The proof uses a common pointwise weak Bayes field and a countable separating family of localisations. It is a valid non-section countermodel in that setting, not a whole-simplex construction.

Theorem Q's main sequence argument is sound: preserving strict additive verdicts, combined with pure-shift improvements and closed fixed-rival sections, forces acceptance at a zero-value comparison. A balanced nonconic swap then violates undominatedness or, if tied, direct (C). Q(ii) needs that protection context: an incoming weak domination by itself does not alone violate (C).

Q does not establish that every additive or lexicographic first level fails in every construction. It requires its strict-verdict inclusion and the relevant null swap (or the additional argument producing one). A general relation need not have a 'first level' at all.

PP57 Lemma 5.1 is local openness of refusal sets. It does not prove global monotonicity along a shift ray.

PP56 Proposition 5.2 supplies a consistent one-parameter set of selected comparisons, not a full relation on all models; it does not prove that every section obstruction needs two rival parameters.
