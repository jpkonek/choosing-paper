# Splicing at a Pair-Indexed Weighting (author's project doc, 16 Oct 2026). Summary for agents

**Setting.**
- Models are measurable subsets of ℝ^n, modulo null sets. A problem is {g, −g}. The background order per world is: good ≺ no advice ≺ bad ≺ contradictory.
- For models D, D′ put N(D,D′) = (D△D′) ∪ −(D△D′), the smallest symmetric set off which they agree, and
  v(D,D′) = ∫_{D′∖D} g dμ − ∫_{D∖D′} g dμ ∈ ℝ^n.
- Let σ(v) be the least-norm point of argmin_{p∈Δ} |p·v|; it is the point nearest 1/n. Put p_{D,D′} = σ(v(D,D′)).
- p_{D,D′} = p_{D′,D}, and it is unchanged by replacing the common advice of D, D′.

**The spliced comparison.**
- Fix a selection p ↦ C_p and base preorders ≼^H_i. With N = N(D,D′) and C = C_{p_{D,D′}}, put
  S_{D,D′}(X) = (X∩N) ∪ (C∖N),  and  D ≼′_i D′ ⟺ S_{D,D′}(D) ≼^H_i S_{D,D′}(D′).
- **Prop.** If every base satisfies (G), then every ≼′_i satisfies (G) and (IB). If the base is itself (IB), then ≼′ = ≼^H.
- **Transitivity.** The construction says nothing about it.
  - With the homothetic ordinal base (Full Coverage by Homothetic Credal Families), in two worlds with a singleton target, there is a STRICT cycle Y ≺′₁ X ≺′₁ Z ≺′₁ Y (conic models).
  - Mechanism: (X,Y) is evaluated in a context C_p with s(p) < 1, where the threshold statistic α ties and β decides; (Y,Z) is evaluated in the context C_{e1}, where α decides. The context caps and floors the threshold statistics.
- **Intersection repairs fail (S).**
  - (a) Closing a class under substitution intersects to the background order, which admits no (S) selection (by connectedness of Δ).
  - (b) Intersecting spliced comparisons over any family of contexts containing the two vertex contexts destroys competitiveness of interior models.
- **Open per the author:** a base that is not independent but whose spliced comparisons are well behaved. Under round 36's weakening, the relevant question is whether the spliced comparisons are (FC) (Suzumura) consistent, or (TC) consistent, for some base, and whether they give closed sections, competitiveness and (C).
