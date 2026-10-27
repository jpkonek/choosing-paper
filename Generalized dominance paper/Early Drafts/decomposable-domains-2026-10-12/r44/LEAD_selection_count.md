# Lead's note (22 October): how many selected models (S) needs

Status: lead's proofs, not yet refereed. Labels as stated.

## Setting
Three worlds; full four-advice domain, models modulo null sets. A selection p ↦ C_p on the closed 2-simplex Δ satisfies (S) if every C_p is coherent and undominated, C_p is competitive on supp p (for every model X there is w ∈ supp p with C_p ⪯_w X), and every section A_w(X) := {p : C_p ⪯_w X} is closed, for every fixed X and world w. Strict (G): if Y is pointwise no worse than X at w and strictly better on a non-null set, then Y ≺_w X. Write M ≈ N ("all-world tie") when M ⪯_w N and N ⪯_w M at all three worlds. Strict means A ≺_w B iff A ⪯_w B and not B ⪯_w A. Undominated: no Y with Y ⪯_w M at every w and Y ≺_w M at some w.

## Lemma A (tie fibres are closed). PROVED
For every selected M, Φ_M := {p : C_p ≈ M} is closed.

Proof. Φ_M ⊆ ∩_w A_w(M). Conversely, if C_p ⪯_w M at every w, then since M is undominated, none of these is strict, so M ⪯_w C_p at every w, i.e. C_p ≈ M. Hence Φ_M = ∩_w A_w(M), an intersection of closed sets. ∎

## Lemma B (vertex models). PROVED
Let V_i be the precise coherent model at e_i (correct at world i on a.e. problem). Then C_{e_i} = V_i, and V_i has no all-world tie with any other model.

Proof. Competitiveness at e_i gives C_{e_i} ⪯_i X for every X. If C_{e_i} ≠ V_i, then V_i is pointwise no worse at i and strictly better on a non-null set, so V_i ≺_i C_{e_i} by strict (G), contradicting C_{e_i} ⪯_i V_i. For any M ≠ V_i, strict (G) gives V_i ≺_i M, so M ⪯_i V_i fails. ∎

## Theorem C (the selection cannot be finite; without ties it is uncountable)
(i) PROVED. No selection satisfying (S) and strict (G) takes only finitely many values.
(ii) PROVED. If no two distinct selected models are all-world tied, then every fibre F_M := {p : C_p = M} is closed and the selection takes uncountably many values.
(iii) OPEN. Countably many values, with some tie component that is infinite and whose index set is not closed. Referee PP17 shows by an explicit labelling that closedness facts alone cannot settle this; more of the axioms are needed.

Proof. Put an edge between distinct selected models that are all-world tied. For a connected component K of this graph let U_K := {p : C_p ∈ K}. For M ∈ K, Φ_M ⊆ U_K, and F_M ⊆ Φ_M; hence U_K = ∪_{M∈K} Φ_M.
(i) With finitely many values, each U_K is a finite union of closed sets (Lemma A), so the U_K partition Δ into finitely many closed sets. By Lemma B, {V_1} and {V_2} are different components, so there are at least two nonempty pieces. This disconnects Δ. Contradiction.
(ii) With no ties, F_M = Φ_M is closed (Lemma A), so the fibres partition Δ into closed sets, at least three of them (Lemma B). Sierpiński's theorem: a continuum is not a countable union of two or more pairwise disjoint nonempty closed sets. So there are uncountably many fibres. ∎

## Lemma D (private witnesses are countable). PROVED
Suppose {S_t : t ∈ I} are models and each S_t has a non-null set R_t on which S_t is definite (gives an answer) while every S_s, s ≠ t, is silent. Then I is countable.

Proof. If s ≠ t, S_t is definite on R_t and silent on R_s, so R_s ∩ R_t is null. A σ-finite measure admits only countably many pairwise almost-disjoint non-null sets. ∎

Relevance (repaired after referee PP17). Audit's three- and six-source proofs (sections 9–14) protect group i by a set R_i on which both members of group i are definite and every other selected source, T and every rival are silent. The same argument applied to groups shows: a family of groups, each with such a set private to that group, is countable. By (ii), if the construction creates no ties, then all but countably many groups' worth of selected models must be protected some other way: by witnesses shared across uncountably many groups.

## Lemma E (T's tie fibre stays inside). PROVED for T1, using (TC)
If T is selected, Φ_T is a compact subset of the open simplex. Let p be on an edge, supp p = {i, j}, with C_p ≈ T. Take a non-null set E of problems where T1 is silent and worlds i, j agree. The model X that fills E with their common answer satisfies X ≺_i T and X ≺_j T by strict (G). If C_p ⪯_i X, then T ⪯_i C_p ⪯_i X and X ≺_i T, violating (TC); likewise at j. So C_p is not competitive at p. Vertices are excluded by Lemma B.
