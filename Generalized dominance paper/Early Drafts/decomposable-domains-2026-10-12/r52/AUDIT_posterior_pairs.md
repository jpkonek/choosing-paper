# Posterior family passes the pair-type obstruction

23 October 2026. Author-checked proof, not independently refereed. This is a geometric result and a construction brief, not a ranking satisfying the milestone.

## 1. Family

Let M be a nonempty compact convex subset of the interior of the probability simplex. For a in Delta define

    M_a = { (a_i p_i)_i / (a dot p) : p in M }, C_a = D_{M_a}.

These are the original diagonal-rescaling/posterior models, not a newly invented family. The following result connects them to the obstruction in PP45/PP47.

There is eta>0 with p_i>=eta for all p in M and i. Hence a dot p>=eta on Delta times M. The projective map is continuous uniformly on this compact set. Its image M_a is compact and convex: projective normalization maps a line segment to the line segment between the normalized endpoints, with a reparameterized mixing coefficient. Thus a maps continuously to M_a in Hausdorff distance.

At uniform a, M_a=M. At e_i, M_a={e_i}. At a boundary index, M_a lies on exactly that index's face. For finite-polytope M, the induced advice is continuous in measure: the vertex expectations vary continuously, and their zero planes at a fixed index are null. This applies to the contamination triangle.

The interior family is genuinely (n-1)-dimensional. For i,j,

    max_{q in M_a} q_i/q_j = (a_i/a_j) max_{p in M} p_i/p_j.

The rightmost maximum is positive and finite. Thus M_a determines all odds a_i/a_j, and determines a. Compact subsets of the interior are therefore homeomorphic to their images.

## 2. The pair ordering theorem

Take strictly positive a,b. At a gamble g where C_a and C_b give different advice, let W be the worlds at which C_b's advice is worse and R those at which it is better, under correct < silence < wrong. Coordinate-zero problems can be omitted as null. Set r_i=b_i/a_i.

**Theorem.**

    min_{i in W} r_i < max_{j in R} r_j.

Equivalently, D_i=log(a_i/b_i) satisfies PP45's necessary type inequality

    max_W D_i > min_R D_i.

The same vector D works for every disagreement problem of this pair. This holds for arbitrary dimension and every M as above.

**Proof, silence to an answer.** Let the new answer be represented by h=+g or -g. W={i:h_i<0}, R={i:h_i>0}. Since the old model did not accept h, some p in M has sum p_i a_i h_i<=0. The new model accepts h, so sum p_i b_i h_i>0 for every p. If max_R r_i<=min_W r_i, choose k between them. On positive terms r_i<=k, and on negative terms r_i>=k. Thus sum p_i b_i h_i<=k sum p_i a_i h_i<=0 for that p, contradiction.

**Proof, an answer to silence.** Let h be the old accepted answer. Now W={i:h_i>0}, R={i:h_i<0}. If min_W r_i>=max_R r_i, choose k between them. Then sum p_i b_i h_i>=k sum p_i a_i h_i>0 for every p, so the new model still accepts h, contradiction.

**Opposite answers.** Apply the first argument to the newly accepted answer, which the old model did not accept. These exhaust disagreements between coherent advice. QED.

Exact arithmetic check: 30,000 sampled integer likelihood pairs and gambles for epsilon=3/10 produced 9,855 disagreements; every one satisfied the inequality using rational comparisons, with no logarithmic approximation. The proof supplies the general quantifiers.

## 3. What this proves and does not prove

It eliminates the specific pair-type obstruction to the combined-cut box on the entire interior posterior family, not merely on sampled pairs. The family includes a target, true interior variation, and coherent boundary limits in one formula.

It does NOT construct gate fields, prove CG2, prove triangle compatibility, or prove sections of a ranking. Passing a necessary ordering test is not sufficient for any of those conclusions. Boundary-weight gate tests must be treated separately; the logarithmic proof uses positive a,b.

It imposes NO equivariance on the rankings. Previous impossibility results for rescaling-invariant rankings do not apply merely because this coherent family is used. Fields can depend on absolute gamble coordinates, the target, and the individual model.

Do not force compatibility constants to equal a_i/b_i. Their existence as a type certificate is only a geometric fact. Installing the same ratios as globally consistent gate constants could recreate a single-witness construction.

## 4. Proposed positive programme

Replace the box/fan geometry experiment by joint field construction on a two-dimensional posterior patch through the target, with a complete edge as the next boundary test. Leave the family adjustable if actual comparison constraints require it.

Use three non-collinear interior indices, including the uniform index. Include their bounded fills, retreats and one rival modified on pieces on which different members disagree. Construct fields jointly at all three worlds, with universal competitiveness and the actual zero-accepting triangle test. Passing the pair-type test is no longer the research task; it is proved above.

Search for a parameter-dependent formula, not independent fields fitted at each sampled index. Preserve the compactness/envelope mechanism for fixed-rival closed sections where feasible. Do not require a global endorser, exact source-index Bayes weights, or rescaling invariance.

In parallel, investigate selective use of evaluators: an additive field can propose acceptable worlds without requiring every positive comparison at every world to be accepted. This is a genuinely broader class, but needs its own universal-defence, TC, protection and section proofs. Avoid presenting a greedy allocation as such a proof.

## 5. Audit cautions

PP47's Proposition 2.6(b) and Corollary 3.3 cannot literally exclude a combined cut from dominating ANY rival: every coherent model is pointwise better at all worlds than the always-contradictory model. Keep the special two-valued fill hypotheses and the required non-guidance acceptance explicit.

PP47 Theorem 4.1 is stated under strict pairwise CG2. It does not justify an unconditional claim that zero-accepting gate systems satisfying TC must be free of single-world ties.

A global witness is allowed as an intermediate construction. Its presence limits what that construction can establish under the applicable impossibility theorems; it is not itself a violation of the accuracy axioms.
