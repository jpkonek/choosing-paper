**Proceed with the diagnostic, but correct two statements before encoding anything. Otherwise the “ties allowed” run could still exclude solutions permitted by the axioms.**

First, **it is not established that every impossibility used a prohibition of single-world ties**. In particular, PP52 Theorem 4.1 explicitly concludes that the protected model is either dominated **or tied at every world with an incoherent model**. The latter is excluded by (C). Its stated obstruction therefore survives allowing single-world ties; its additional assumption is closedness along changing-rival mass paths.

My previous assessment should have distinguished that result from the triangle-exclusion machinery more sharply. The new experiment is worthwhile, but we must not assume its outcome.

Second, the proposed protection encoding is stronger than undominatedness when the rival is coherent.

### 1. Atomlessness: exact embedding, not numerical stabilisation

Run search and proof in parallel, but **do not use stabilisation under refinement as the evidential standard**.

A finite unsatisfiable instance can already prove impossibility if:

- its cells are actual positive-measure measurable sets;
- its models and records have an exact realisation on those sets;
- guidance and common-context identifications are correct;
- every clause follows from an axiom.

No persistence through further refinements is then necessary.

Conversely, satisfiability at subdivision levels 1–4 proves little about arbitrary measurable splits. Stabilisation does not change that.

Use subdivisions to discover interactions. For every claimed obstruction, provide the **continuum interpretation of the certificate**. Do not assume verdicts depend only on masses: that is another restriction on rankings. Different measurable records with equal mass may receive different verdicts unless an axiom identifies them.

### 2. Sections: omit the proposed neighbour rule

Choose **(a)**.

The proposed rule—“an index cannot refuse when all its neighbours accept”—is not a consequence of closed sections. A closed set can surround an open region of refusal. A finite grid has no intrinsic notion of the required limiting behaviour.

There is one legitimate way to introduce sections into a certificate:

> Exhibit an actual sequence \(a_k\to a\), with the **same measurable rival \(X\)** throughout, and prove acceptance at every \(a_k\). Then (S) forces acceptance at \(a\).

The sequence argument can be symbolic rather than enumerated. But a ring of nearby grid points is no substitute.

I would omit the neighbour heuristic even from the side run: we already have enough optional assumptions to disentangle.

### 3. Translate forced disjunctions, not artificially assigned defenders

**Yes: the forced-disjunction translation is the right task.**

For each selected \(C_a\) and rival \(X\), encode
\[
\bigvee_{i\in\operatorname{supp}(a)}[C_a\preceq_i X].
\]

Do not choose its defending world in advance. Different choices must remain available until other clauses genuinely eliminate them.

Nor should we presume that the gate kink certificate has an axiom-level translation. A perfectly informative outcome would be:

> The contradiction requires a field inequality for which no corresponding axiom-level comparison constraint has been established.

That identifies an architectural obstruction. It is not a failed translation.

### 4. Encode undominatedness exactly

Write
\[
A_i=[C_a\preceq_i X],\qquad B_i=[X\preceq_i C_a].
\]

Undominatedness of \(C_a\) requires
\[
\boxed{\quad
\left(\bigwedge_{i=1}^{3}B_i\right)
\Longrightarrow
\left(\bigwedge_{i=1}^{3}A_i\right).
\quad}
\]

In words: if \(X\) is no worse at every world, it must not be strictly better anywhere.

Your proposed condition,
\[
\bigvee_{i=1}^{3}\neg B_i,
\]
also forbids an all-world tie with a **distinct coherent** rival. That is stronger than undominatedness and should not be imposed universally.

For an **incoherent** rival, undominatedness together with direct (C) does imply this stronger refusal condition: the rival may neither dominate nor tie everywhere with the selected coherent model.

Thus distinguish:

| Rival | Required protection |
|---|---|
| Incoherent \(X\) | Some world refuses \(X\preceq_i C_a\). |
| Coherent \(X\) | Either some world refuses it, or the comparison is a tie at every world. |

**Use all three worlds for domination and direct (C).** The support restriction belongs to the defence clause of (S). Do not replace the global conditions by support-only versions.

Also, a module checking selected models does not yet verify (C) for every coherent undominated model in the eventual system. Record that remaining scope explicitly.

### 5. The ledger should run in parallel

Use a dedicated ledger, but do not make it a prerequisite for starting the base experiment.

The search can begin immediately with the axioms themselves:

- exact guidance;
- exact (IB) identifications;
- actual (TC);
- support-defence disjunctions;
- exact undominatedness;
- direct (C), with coherent and incoherent rivals distinguished.

Import derived clauses only after their hypotheses have been checked. Unchecked consequences belong in separately labelled conditional runs.

### What should make this round consequential?

The main deliverable should be **a comparison pattern that the stronger architectures forbid but the actual axioms permit**, together with a credible measurable implementation—or an exact axiom-level contradiction.

In particular, ask the constructor to identify:

1. Which single-world ties are essential?
2. Which reverse comparisons require abandoning old-side coherent realisers?
3. Which refusals preserve protection at the other worlds?
4. Whether those choices survive arbitrary measurable splits and common-context copies.

Do not count an arbitrary satisfying finite table as the desired positive result. Extract the rule behind it.

Finally, triangle completion itself is not new to the project; earlier work found failures ending in strict guidance. **The new task is to determine whether the kink admits a different completion once defender choices remain disjunctive and protection is encoded exactly.** That is the experiment worth running. It can tell us whether the remaining freedom is usable, rather than merely reminding us that it exists.