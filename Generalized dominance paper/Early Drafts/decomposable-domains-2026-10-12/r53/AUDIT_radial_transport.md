# Radial transport and the next milestone

23 October 2026. Author-checked, not refereed. This is a transfer theorem, not an existence proof for coverage.

Let H be the problem half-space, modulo the usual null sets. Let A={g in H:1<||g||<2}. The radial map

    F(r theta) = (1+r/(1+r)) theta

is a smooth bijection H\{0} -> A preserving null sets in both directions. Coherent advice is unchanged along a ray, so C(F(g))=C(g).

Fix arbitrary common advice B outside A. Encode any measurable model X as JX: on A put (JX)(F(g))=X(g), and outside A put JX=B. All encoded comparisons have bounded disagreement. J respects disagreement records and common-context substitution. It also preserves the world-wise advice order.

Suppose Q_i is a relation on models, with (G), (IB), and (TC). It is enough to assume these properties for comparisons supported in A, since all comparisons between encoded models have that support. Define

    X R_i Y iff JX Q_i JY.

Then R has (G), (IB), and (TC), by direct transport. This transfers only those properties already proved for Q; it does not manufacture them.

For a coherent selected C_a and arbitrary X, define X_a to equal JX on A and C_a outside A. Since JC_a equals C_a on A, (IB) gives

    JC_a Q_i JX iff C_a Q_i X_a,

and likewise in reverse. Thus if every C_a has support defence against every A-supported modification, every C_a has support defence against every measurable rival under R. If no A-supported modification dominates C_a under Q, no arbitrary model dominates it under R. If all-world ties with C_a under Q are impossible for distinct A-supported modifications, they are impossible for arbitrary models under R. These assertions include edge supports.

The remaining section condition is exactly:

    for every measurable Z on A and every i,
    {a: JC_a Q_i JZ} is closed.

Here JZ means Z on A with B outside. Call this the annular section condition. If it holds, R has the section part of (S). Combined with the appropriate protection/tie assumptions and the existing dominance theorem, this gives the desired full system.

Crucial limitation: the ordinary section condition for Q along the original coherent selection does NOT imply this annular condition. In the comparison C_a Q_i X_a, the rival X_a changes with a. Nor does the earlier addition lemma establish it. The models JC_a have a common exterior and are generally not coherent models on the original full space.

Consequences for strategy:

1. A universal bounded-modification construction is not a minor radial module: its defence, protection, (IB), and (TC) content transfers to all angular and unbounded rivals.
2. There is no need to construct separate cross-class comparisons and solve mixed-class triangles if this route succeeds. All comparisons are evaluated by one annular rule.
3. Angular complexity remains inside A; compression does not eliminate the kink or prove feasibility.
4. Verdicts need not be closed as Z varies. The annular section condition fixes Z and varies the coherent trace.
5. Choosing gates or ordinary continuous integral quorums remains an optional architectural restriction. This theorem does not supply a new successful formula for Q.

Recommended checkpoint: one relation on all measurable advice assignments on A, covering the kink triple and a varying coherent neighbourhood, satisfying (G), (IB), (TC), defence and protection for every measurable rival on A, and the annular section condition. A finite-cell check or a finite collection of isolated sources does not establish this checkpoint. Keep a separate list of structural properties proved and section properties still open.
