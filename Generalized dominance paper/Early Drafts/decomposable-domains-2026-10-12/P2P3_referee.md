# P2P3 referee report (round 11, 14 Oct 2026)

Independent, adversarial reading of `P3_notes.md` (the extension lemma) and `P2_notes.md` (holonomy, flexible worlds, Theorem LX).

**Sources read**
- BRIEF10.
- *Coverage after Neutral Abstention* §§1–3 (Thm limit, (4), Thm closure).
- *Vacuous Targets and Transfinite Construction* §5.
- The write-up (*The Contamination Triangle.tex*): §2 (axioms, Thm kkm, U-domain, adding up); §3 (Prop necessary, Prop reduction with its converse, Thm ccibu); §4 in full (Lemmas signs → edgebox, Thm pivot, Thm nosliding, Lemma twoslope, Prop blowup, Cor PCNS, Prop boxbridge, Prop T1); §5 Thm gm; §6 Thm complete; §7 (Prop M0, Thm Estructure, Thm pstarE, Prop Epsi, residuals R-a′/R-b′, Thm N26.1, Thm Ltwo).
- *Three Complete Rankings* (Thm main statement).
- N17 §6 (N17.7, N17.8); N19 (nearby lemma); R10a/R12 (Thm M).
- Both notes' scripts.

**Independent checks** are in `p23ref_py/`, run with `python3 -I`; this is my own code, and it reads only the saved parameter vectors from `p2py/*.npy`:
- `box_exact.py`, output `box_exact.out`;
- `rotation_check.py`, output `rotation_check.out`;
- `p3_examples.py`, output `p3_examples.out`;
- `nested_check.py`, output `nested_check.out`.

**Verdict labels:** CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG.

---

## Summary table

| Claim | Note's label | Verdict |
|---|---|---|
| P3.1 transport (Lemma 2.1), Cor 2.2 | PROVED | CONFIRMED on M_U; one slip in the general-domain formula (repair R-P3a) |
| P3.2 Thm 3.1 (R5, exact extension, "iff") | PROVED | CONFIRMED (both directions; R5 interacts correctly with R3, R4) |
| P3.3 Thm 4.1 compactness; failure at R5 | PROVED | CONFIRMED |
| P3.4 (ET), compulsory comparisons, transported Lemma R | PROVED | CONFIRMED |
| P3.5 Example 1 | PROVED | CONFIRMED (independent NUMERICS agree); scope remark |
| P3.6 Example 2 | PROVED | CONFIRMED (independent NUMERICS agree); interpretive sentence overstated (R-P3b) |
| P3.7 Thm 7.1, witnessed EL* | PROVED | CONFIRMED; content is close to tautological (remark) |
| P3.7 tests: reproduces listed covers | CHECKED | CONFIRMED for precise, box and gauge-mixture covers; v3 accepted at statement level |
| P3.7 tests: no false covers | PROVED | T1 part CONFIRMED; V part CONFIRMED WITH REPAIR (domain; R-P3c) |
| P3.8.2 witnessed T1 covers are M0 with (E_ψ), E(ψ) ≠ ∅ | PROVED | CONFIRMED |
| P3.8.3(1) pre-systems not excluded; reduce to R-a′/R-b′ for ψ | PROVED / open | CONFIRMED WITH REPAIR ((α) for pre-systems; R-P3d) |
| P3.8.3(2) (ET) never forces the chord tie | PROVED | CONFIRMED (weak statement) |
| P3.C1 Villegas-type conjecture | CONJECTURE | label correct; "what R5 gives" CONFIRMED; hypothesis is non-generic in n = 3 and the target can be weakened (R-P3e) |
| P2.1 vector form | PROVED | CONFIRMED |
| P2.2 one kink makes chart data consistent | NUMERICS | CONFIRMED as NUMERICS (independently reproduced). Its significance must be restated: kinked data are excluded by coherence (R-P2a) |
| P2.3 linearity "not an additivity input" | CHECKED | dependency reading CONFIRMED; the interpretation is CONFIRMED WITH REPAIR; the localisation ("near T1", "one facet arc") is a GAP |
| P2.4 flexible worlds (a)–(d) | PROVED | CONFIRMED |
| P2.4 (e) | CHECKED | CONFIRMED (CHECKED level) |
| P2.5 Theorem LX | PROVED | CONFIRMED; class statement needs repair (R-P2c); the "layering neutralised" summary holds for two levels only |
| P2.6 Lemmas 5.1, 5.2 | PROVED | CONFIRMED |
| P2.6 Prop 5.3 | CHECKED | CONFIRMED (CHECKED); the word "far" in (β) is unjustified |
| P2.7 Lemma 6.1 | PROVED | CONFIRMED (Monte Carlo spot check agrees) |
| P2.7 "LX recovers the n = 2 conclusion" | — | CONFIRMED WITH REPAIR (two-level lexicographic class only) |

No claim is WRONG in its mathematical content. The repairs concern scope, one formula slip, and interpretations that go beyond what is proved.

---

# Part A: P3_notes.md

## A1. Lemma 2.1 and Cor 2.2 (exchange normal form and transport): CONFIRMED on M_U

**The M_U form.**
- On M_U, (IB) is exactly the statement that X ⪯_i Y depends only on σ = 1_X − 1_Y. The shared-advice set is {σ = 0}, and A ∪ (−A) is a legal symmetric set because U ∩ (−U) = ∅.
- (Σ) is exactly transitivity under (IB). Given σ, τ ∈ 𝒮_i with σ + τ ∈ 𝒞, one realises X, Y, Z as follows:
  - Y = 0 on {σ = 1}, Y = 1 on {σ = −1}, Y = 1 on {τ = 1}, Y = 0 on {τ = −1};
  - conflicts occur only where σ + τ = ±2, which is excluded.
- (P) and (N) are weak and strict (G) in exchange coordinates. With 1_{E_iY} − 1_{E_iX} = sgn_i·σ, X is weakly better exactly when sgn_i·σ ≥ 0.
- (T) is (Comp):
  - for q ∈ Comp(σ), X := C_q − σ is a legal model with 1_{C_q} − 1_X = σ;
  - conversely, every (q, X) arises this way.
- (Und) and (C_sel) are the undominatedness and (c) conditions verbatim.
- I checked the transport step from (B_u, U∖A) to (B_r, B_r∖A) against (IB) as stated in write-up §2. Take A′ = A ∪ (−A), F = U∖A and G = B_r∖A. This gives exactly the pair (B_r, B_r∖A).

**Repair R-P3a (slip).** The general-domain sentence should read "Comp(e) = {q : a_{C_q} = a_{C_p} on Z}". The note's "a_{C_q} = a_X on Z" would make the transported model equal to C_q.

## A2. Theorem 3.1 (exact extension with the limit rule R5): CONFIRMED

Checked in both directions.

**Direction (1): a clean total closure is a successful system.**
- R1 and R2 give preorders.
- R3 gives (IB) in both directions, because the inverse replacement is also a replacement.
- The background comparisons give weak (G). Strict (G) holds because a reversal of a strict background comparison is outcome (a).
- R4 gives (U_sel).
- κ total gives (Comp).
- R5 gives closed sections. Δ is metrizable, so sequential closure suffices, for every X and every model of the domain.
- (C) comes from Thm kkm, which needs only (LA) and (S), both now in place. The argument runs:
  1. B ∈ C_L is weakly dominated by some C_p.
  2. Since B is undominated, B ~ C_p.
  3. A model Y tied with B is then tied with C_p, so it is coherent by the absence of (c).
  4. Y is undominated by the transitivity argument in the note.

**Direction (2): every successful system contains a clean closure.**
- A successful system contains the generators, for any κ read off from it.
- It is closed under R3 by (IB).
- It is closed under R4: otherwise X would dominate C_p.
- It is closed under R5 by (Cl).
- Leastness gives Cl₅(κ) ⊆ (⪯_i).
- Outcome (a) would be inherited by the system.
- An outcome-(c) tie would be a tie in the system with C_p ∈ C_L, which (C) forbids.

**The rules interact correctly.**
- R5 acts only on section comparisons.
- R3 and R4 act on everything generated, including R5 conclusions.
- The least fixed point exists (Knaster–Tarski) and is reached by stage ω₁, since each rule has at most countably many premises.
- So the "iff" holds in both directions, and closed sections are indeed produced by R5 rather than guessed.

**Remarks (no repair needed).**
- "Minimal successful system" means least among the systems containing a given κ. Different κ give incomparable systems, so there is no absolute minimum.
- The theorem is exact but formal. Existence of a clean total κ is as hard as the original problem.
- Its gain over Thm closure is that the sections need not be prescribed. This is a real simplification for constructions.

## A3. Theorem 4.1 (compactness): CONFIRMED

- Every clause listed in (P), (N), (Σ), (T), (Und) and (C_sel) is finite. (T) has at most 2ⁿ − 1 support patterns.
- Propositional compactness holds for any number of variables.
- (Cl) is exactly the family of infinitary Horn clauses ⋀_k x_{i,σ+d_k} → x_{i,σ}. Check: 1_{C_{p_k}} − 1_X = (1_{C_{p_k}} − 1_{C_p}) + (1_{C_p} − 1_X).
- Example 2 shows that this family is not compact. Each finite set of chosen literals is satisfied by a full system Ψ^{ρ_m}, while the whole set together with (N) and R5 is unsatisfiable.

## A4. §5 (ET), compulsory comparisons, transported Lemma R: CONFIRMED

- The edge-Pareto special case is correct. If C_q (q in the relative interior of edge {i, j}) failed to accept a non-null set where h_i, h_j > 0, adding it would be a strict background improvement at i and j. Then supp q ∖ N(σ) = ∅, and the selection test fails.
- The transported Lemma R is a direct consequence of closedness and (ET).

## A5. Example 1 (P3.5): CONFIRMED

**Hand checks.**
- P_{T1}(a) = 0.7·(1.9/3) − 0.03 = 0.4133 and P_{T1}(a′) = 0.1567.
- r·a = r·a′ = 0.45, and u·a, u·a′ > 0.
- e1·a < 0 and e2·a′, e3·a′ < 0, so no vertex lies in Comp(σ).
- (½, 0, ½) ∈ Comp(σ), while (0, ½, ½) ∉ Comp(σ) because q·a′ = −0.1(q2 + q3).
- σ·sgn_i takes both signs at every world, so N(σ) = ∅.
- B_u = U, because u ∈ K′.

**Monte Carlo (`p3_examples.out`, 4·10⁶ Gaussian samples, conic balls).**
- A ⊆ D_{T1} ∩ B_r.
- Comp contains u, r and (½, 0, ½), and no vertex.
- ∫_A h_i > 0 at all three worlds, so Ψ¹ accepts σ everywhere.

**Logical structure.**
- The state is the background order, which is closed under R1–R4. A coherent model is never background-dominated at every world, because m = 1_X − 1_{C_p} with m·sgn_i ≥ 0 at every i forces m = 0 a.e. on U.
- The state is clean and respects its reservations, and (K_X) holds for every model.
- At u, worlds 2 and 3 are reserved. World 1 transports, by (IB), to B_r ⪯_1 X_r, which is reserved at r.

So EL_res, as posed, is false.

**Scope remark (not a repair).**
- The example refutes the per-model formalisation EL_res of the *Vacuous Targets* §5 lemma. The source itself already flagged a "compatibility obligation", which the example makes precise.
- The selection q ↦ B_q does not contain T1. It must not: with T1 selected, existence of any system is the open question. So the example is a counterexample to a general lemma, not an obstruction for T1.

## A6. Example 2 (P3.6): CONFIRMED

**Hand checks.**
- r_k·h = p0·h + δ_k(h1 − p0·h).
- On W′ one has h1 < 0 and r_1·h > 0, which forces p0·h > 0. Convexity along the segment then gives W′ ⊆ B_{r_k} for every k.
- Sh_k = B_{p0} ∖ B_{r_k} ⊆ {h1 < 0}, and the Sh_k decrease.
- The heavy region ρ = M lies in Sh_1 ⊆ {r_1·h ≤ 0}, which is disjoint from W′. So w does not depend on M.
- a_m > 0. Indeed, on U ∩ p0^⊥, combining 3h1 + h2 + h3 = 0 with u·h > 0 forces h1 < 0. Numerically, max h1/|h| = −0.19 there.
- X = B_{p0} ∖ W′ is a strict world-1 background improvement on B_{p0}.
- Every Ψ^ρ (bounded measurable ρ > 0) is a successful system for the same selection, with closed sections for every model:
  - B_q = D_{co(K′∪{q})} is the a.e.-unique q-Bayes model, also at boundary q;
  - so it is undominated and (C) holds.
- The examples genuinely live on M_U, with all axioms in place (T1 is simply not among the covered targets).

**Monte Carlo.**
- W′ is 17.2% of U.
- B_{r_k} ∖ B_{p0} is null in U, so G_k equals the shell term.
- With ρ ≡ 1, G_k falls from 2.5·10⁻³ to 5.7·10⁻⁵ as δ falls from 0.05 to 0.001, against w = 1.6·10⁻². No fixed ρ handles all k.
- The required M grows like 0.28/δ, as stated.

**Repair R-P3b (interpretation).** "Must commit to open reservations with foresight that finite information does not supply" says more than is proved. What is proved is the following.

> Neither "extendable to a successful system with the same selection" nor "Cl₅ of the stage is clean" is preserved by unions of ω-chains of partial choices.

So a transfinite construction needs an invariant that unions preserve. Examples are the reservation invariant of the *Vacuous* Prop, or containment in one fixed successful system (a witness). Whether such an invariant can always be maintained is EL*, which remains open.

## A7. Theorem 7.1 (witnessed extension): CONFIRMED

Ψ is closed under each rule:
- R1–R3, since it is additive and real-valued;
- R4, since by (W2) ψ(X) ≤ ψ(C_p) forces equality;
- R5, by (W3): ψ_i(C_p) ≤ liminf ψ_i(C_{p_k}) ≤ ψ_i(X).

Ψ contains the background order and every ψ-admissible κ, which exists by (W1). Hence Cl₅(κ) ⊆ Ψ with no outcome (a), and (b) and (c) follow. Under (W4), Ψ is clean, and the proof of Thm 3.1(1) applies to Ψ itself.

For (d):
- the reservations {p : ψ_i(C_p) > ψ_i(X)} are open by (W3);
- they are exchange-compatible, because ψ_i(C_q) − ψ_i(C_q − σ) does not depend on q;
- (W1) supplies (ET).

**Remark.** The content is close to tautological. If an additive Ψ with (W1)–(W4) exists, Ψ is already a successful system and the extension lemma is trivial inside it. The useful part is (b): it isolates the (C)-tie as the only failure mode.

**Reproduction of the covers (brief's question): CONFIRMED.**
- *Precise and Brier families, and normalised boxes.* *Coverage after NA* proves a unique minimising advice at every p, boundary included, coherence, and continuity by dominated convergence.
- *Gauge mixtures.* R10a Thm M(b), refereed CORRECT in R12, gives a.e.-unique coherent Bayes models at every p.
- In each case the selection is the Bayes map, so (W1)–(W4) hold and Thm 7.1(c) returns Ψ.
- *v3 two-world intervals.* Accepted at the level of the cited statement only; I did not re-read v3.

**No false covers.**
- *T1:* CONFIRMED. A Ψ with (W1)–(W4) and T1 selected would contradict Thm gm.
- *V:* **repair R-P3c.** *Three Complete Rankings* Thm main is stated for n = 3 on the all-model domain, without (C). The claim must be restricted:
  - to that domain, with n = 3, or n ≥ 3 if *Complete Rankings for Any Number of Worlds* is cited for general n;
  - it is not shown for an arbitrary decomposable domain M, on which Thm 7.1 is formulated.

## A8. §8 (what the lemma gives for T1)

**8.2: CONFIRMED.** Cl₅(κ) ⊆ Ψ, so ψ (countably additive, ρ_i > 0) endorses every comparison of the cover. Hence (H_M0) and (E_ψ) hold. Prop M0 gives E(ψ) ≠ ∅, and Thm Estructure and Prop Epsi apply.

**8.3(1): CONFIRMED WITH REPAIR (R-P3d).**
- KKM makes every unique interior Bayes model of a pre-system selected, hence coherent, without (C). So (γ) and Thm Estructure apply to ψ.
- Prop M0's last sentence also needs (α): T1 is ψ-Bayes at an *interior* weighting.
  - For a pre-system this is not quoted from anywhere; it must be derived.
  - Derivation: (W2) gives a supporting weight t ≥ 0. If t₃ = 0, say, then B_t would contain every h ∈ U with h1, h2 > 0 > h3. This includes gambles just outside the middle arc of F_3, which D_{T1} rejects. Vertices are excluded likewise.
  - This should be written into the note.

**8.3(2): CONFIRMED.**
- If e_i ∈ Comp(w), then w·sgn_i ≥ 0, so "both signs at world i" excludes the vertex e_i.
- Minimal transversals of the three edges have two elements, so (ET) never forces I(w) = Ω.
- This is only a non-exclusion by (ET). It says nothing about (Σ), (Und) or R5, as the note itself says.

**P3.C1: CONJECTURE label correct.**
- The derivation "what R5 gives" is CONFIRMED, by de Finetti cancellation (N9.4) applied to E_i(C_{p_k}) = E_0 ∪ S_k.
- **Repair R-P3e (two cautions).**
  - (i) The hypothesis needs world-i error sets *nested* along the path (E_0 ⊆ E_i(C_{p_k})). By P2 Lemma 6.1 (confirmed below), in n = 3 that forces the credal sets to share both tangent lines from e_i, which is a codimension-2 condition. So the conjecture covers only special selections. The general R5 content is continuity of ≤_i along Y_k → Y with Y_k = E_i(C_{p_k}), without monotonicity.
  - (ii) For the intended exclusion, countable additivity is more than needed. Thm complete already handles complete worlds represented exactly by an arbitrary (finitely additive) state. The nearby target is "R5 forces exact representability by a state", not Villegas's countable additivity.

---

# Part B: P2_notes.md

## B1. P2.1 (vector form): CONFIRMED

- Lemma 1.1 was checked case by case.
- Rules 1–3 produce the 𝒞-sum-closure of G_i ∪ 𝒞_{≥0}: by exchange invariance, any 𝒞-valued sum is realised by a chain, as in A1.
- The reformulation through acceptance sets 𝒜_i is correct.

## B2. P2.2 (one kink): CONFIRMED as NUMERICS, with its significance restated

**Independent reproduction.**
- `box_exact.py` uses its own chart code and parametrises A and B by ρ and σ directly, inverting the affine facet parametrisation exactly. It uses log grids 10⁻¹³ to 10¹³ (1.2·10⁵ points) and measures a *relative* margin, so the degenerate ends cannot hide a sign.
- Results (`box_exact.out`):

| | ε = 0.05 | ε = 0.3 | ε = 0.6 |
|---|---|---|---|
| linear x₊, absolute margin | −0.094 | −0.144 | −0.110 |
| one kink on F₁, minimum relative margin | 0.077 | 0.478 | 1.385 |

- For the one-kink solutions: absolute margins ≥ 0 to rounding, NS exact (≤ 10⁻¹⁶), strict signs (margin ≥ 3·10⁻⁴), and rotation monotone on all three facets (`rotation_check.out`).
- So the claim holds as stated.

**Caveats on the evidence offered in P2.**
- (i) The brute-force checker (`holonomy_check.out`) reports "violations: 0" for the *linear* x₊ at ε = 0.9, a known violation. It is not a reliable validator; the box-margin computation is.
- (ii) "76/76 corner-sector configurations fail" and "no single kink at ε = 0.9" are search outcomes, not claims, as the note says.
- (iii) The flat-middle-sector runs (D2) were not independently re-run.

**Repair R-P2a (significance).** Kinked data cannot be the facet data of any family to which the §4 derivations of (sign), (NS) and (box) apply.
- Those derivations assume a coherent, Hausdorff-continuous family with half-plane charts. Lemma twoslope then forces a = αn to be affine, so c_k is linear.
- A kink is excluded concretely. At the break of the ε = 0.3 solution, the jump of a′ pairs with δ = n ∓ 5w (both in C_J) to give −30.1 and +15.2 (`rotation_check.out`). So a·δ is not concave on C_J.
- The kinked direction field is also not Möbius, so no positive rescaling makes it affine: L_A⁻¹L_B would have to be scalar, and continuity at the break would then give L_A = L_B.

Correct reading:

> P2.2 shows that Prop T1's contradiction uses (LIN) on all three facets: dropping it on any one facet makes the remaining finite system consistent.

That is a diagnosis of which ingredient is load-bearing. It is not a construction route. P2's own §2.3 effectively says this, but the summary table and the verdict paragraph present P2.2 as "removing the contradiction", which is misleading.

## B3. P2.3 (linearity is "not an additivity input"): dependency reading CONFIRMED; interpretation CONFIRMED WITH REPAIR; localisation GAP

**The dependency reading is correct.** After Prop reduction, §4 uses the ranking only through the Bayes family q ↦ K_q. I traced every lemma:
- *Lemma chords, Lemma levels:* half-plane charts plus joint continuity.
- *Lemma sandwich:* convexity of the level sets.
- *Lemma caps, Lemma rotation, Prop regularity, Prop blowup, Lemma twoslope:* concavity of τ ↦ P(q, h(τ)), which is coherence.
- *Lemma UVN:* the vertex behaviour of the family.
- *Lemma PL2, Lemma nopin:* charts H(h). The non-adjacency hypothesis is automatic on M_U.
- *Thm pivot, Thm nosliding, Cor PCNS:* family-level throughout.
- *Lemma edgebox:* superadditivity of P (coherence), plus vertex-respecting half-plane charts. "c(A + λB) negative in coordinates a and b ⇒ the closed edge misses cl H" uses only that the chart is a half-plane with e_a, e_b ∉ cl H.
- *Prop boxbridge, Prop T1:* algebra.

**Repair R-P2b (interpretation).** By the *converse* of Prop reduction (N12 Prop 1.4), the hypotheses are equivalent to the family being the Bayes family of an additive ranking (a realisation). The hypotheses are:
- a Hausdorff-continuous family q ↦ K_q ⊇ K′ on Δ°;
- K_{p*} = T1;
- vertex-respecting half-plane charts (Prop reduction (e)).

So "straight charts" *is* additivity, at the level of the selection. The potential is not removed from the picture; it is reconstructed from the chart normals. The exact statement P2.3 supports is this:

> **Established (from Thm main + Prop reduction converse).** Let L be any ranking on M_U (additive or not) that covers T1 with strict (G), (IB), (LA), (S), (C), with selection p ↦ C_p = D_{K_p}.
> - T1 is selected at an interior index, by the edge-Pareto argument of A8.
> - Then q ↦ K_q restricted to Δ° violates at least one of:
>   - Hausdorff continuity on Δ°;
>   - for a.e. g ∈ U, {q ∈ Δ° : P(q, g) > 0} is (a.e.) an open half-plane H(g) ∩ Δ° with e_i ∈ H(g) if g_i > 0 and e_i ∉ cl H(g) if g_i < 0.
> - (K_q ⊇ K′ is automatic on M_U.)

**GAP (localisation).**
- The verdict says a cover "must keep U_L **near T1** from containing a straight-chart family on **at least one facet arc**". That is not proved.
- The chain for one facet map uses the charts of gambles in (F_k + ℝ𝟙) ∩ U, through the shifts g − t𝟙 of Lemma levels, at weightings across all of Δ°:
  - UVN near the vertices;
  - PL2 and nopin on sets leaving every ball around p*;
  - the box at the edges of Δ.
- The write-up's own "Localisation" paragraph (§7) records that Hausdorff continuity is used on sets covering Δ°.
- A version localised near p* would be a new theorem.

## B4. P2.4 (flexible worlds)

**(a)–(d): CONFIRMED.**
- (a) Convexity: realise λm and (1 − λ)m′ disjointly inside Cap by (F2) and atomlessness, then use (Σ) and (F1). Cone ∩ Cap ⊆ 𝔄 by (F2) and repeated disjoint addition.
- (b) The construction of δ′ was checked:
  - its masses equal those of δ;
  - its positive and negative parts are disjoint from those of δ in the right way;
  - so δ + δ′ = −1_{δ⁻∖δ′⁺} − 1_R, contradicting (N).
- (c) Separation of the convex cone π(cone 𝔄) from the open negative orthant gives w ≥ 0, w ≠ 0. "No M1" holds because integration over the cells is linear: a certificate Σλ_kδ_k ≤ 0, nonzero, yields an element of K in −ℝ^N_{≥0} ∖ {0}.
- (d) Stiemke's step: for a closed convex cone, the absence of w ≫ 0 is equivalent to cl K ∩ (−ℝ^N_{≥0}) ≠ {0}, by strict separation from the compact base of the orthant. The cell-fine correction vectors were checked coordinate by coordinate.

**(e): CONFIRMED at the CHECKED level.** It is lexicographic separation (Martínez-Legaz–Singer).

**Scope.**
- "Flexible" is invariance under a *fixed finite* partition. Additive worlds with non-cellwise-constant densities are not flexible.
- The "consequence" sentence (N17's heuristic "turned into a theorem") holds for this class only.

## B5. P2.5 Theorem LX: CONFIRMED (proof checked step by step)

**Facts 1 and 2.**
- *Fact 1.* The local-minimum argument is correct. An improvable X ∈ U_L is tied with a selected C_p with equal (F, S) profile, by KKM and the lexicographic form of ties. Then F_i(C_{q_m}) < F_i(Z) puts q_m in the closed section A_i(Z). Local-minimum values of a function on a second-countable space form a countable set.
- *Fact 2.* Lyapunov convexity and compactness of the range, plus a non-vertical supporting line at an interior abscissa. The Lagrangian computation (r = −c^S/c^F, chain in λ, atoms T_λ) was checked.

**Step 1.**
- W = L ∪ ⋃_{v∈V} Z_v.
- *Case 1.*
  - ∇V(t) = F(B_t) holds because the F-profile of the t·F-minimisers is unique off E; the free problems do not affect F.
  - ∂_iV is constant on the cone, and the distributional identity ∂_i²V = −∫δ(t·c^F)(c_i^F)² dμ gives (a_i).
- *Case 2.*
  - The Baire step is valid.
  - Closedness of 𝓛_i gives B_t ∈ 𝓛_i everywhere.
  - "A point does not separate a disk" plus injectivity forces int I into one atom interval, which gives (b_i).

**Step 2.** Each case was re-derived:
- A = {i}: constancy along lines through e_i, because c^F_i = 0;
- |A| = 2: t·c^F has constant sign;
- A = Ω: free moving set.

Shrinking disks preserves (a_i) and (b_i).

**Repair R-P2c (class statement).** "This class contains … 𝓛₂ˢ" is inaccurate as written. In the write-up, 𝓛₂ˢ has a strictly signed primary and an *arbitrary* secondary, while LX assumes c^S_i strictly signed. The proof extends with one change:
- With a strictly signed primary, Case 1 forces B to be constant on W₁, which is impossible. So only Case 2 occurs, and conclusion (ii) is vacuous.
- The Lagrangian chain runs over λ ∈ ℝ, and on T_a one gets c^S_i = −a c^F_i with a ∈ ℝ.

So for 𝓛₂ˢ, LX holds with "α_i ∈ ℝ" in place of "α_i > 0". The order on M″ is still that of c^F_i (when α_i ≤ 0 the secondary never decides). State it this way.

**Scope.**
- LX is for **two** levels.
- P2's verdict ("layering is neutralised by closed sections") and D1 rely on it. Via 3.1(e), flexible M2 worlds may need r > 2 levels, for which LX is not proved. The note lists this as nearby result 1. The summary should say "two-level layering".

**Cor LX.1 (CHECKED): CONFIRMED.** In particular, overlap of moving sets forces the same case and the same constants.

## B6. P2.6 (rigid acceptances act only at a distance)

**Lemmas 5.1 and 5.2: CONFIRMED.**
- In N17.7: μ(δ⁺) ≥ 0.4 − 1.2κ. The flexible part G_θ is endorsed by μ.
- In N17.8: |T^θ_x(δ)| ≤ ‖δ‖₁ gives ‖δ‖ ≥ c*_i. 𝒜_band is endorsed by λ through T₀.

**Prop 5.3: CONFIRMED (CHECKED).**
- The chain C_{p_k} ⪯_j X_k ⪯_j Y_{m,j} uses (G), from the inclusion of error sets.
- Closedness gives C_{p̄} ⪯_j Y_{m,j}.
- Summability gives Y_{m,j} → T1.
- The trichotomy follows from the undominatedness of T1.
- Wording: in (β), C_{p̄} need not be "far" from T1. It is just some coherent C ≠ T1 tied with T1 at every world.

## B7. P2.7 (n = 2 versus n = 3)

**Lemma 6.1: CONFIRMED.**
- The reduction of the inclusion to (1) and (2) was checked.
- So was the dual-cone identification: the dual of D_M ∩ {h_i < 0} is cl(cone M − ℝ₊e_i).
- Monte Carlo spot check (`nested_check.out`):
  - homothety at e₁ with factor 1.2 is nested (missed measure 0);
  - factor 0.8 is reverse-nested;
  - homothety at u and a translation are nested in neither direction (missed measures ≈ 6·10⁻³).

**Repair.** The n = 2 "nearby lemma" (N19: closed sections force the Archimedean property along nested paths) concerns *general* worlds. LX recovers its conclusion in n = 3 only for two-level lexicographic worlds with additive levels. "Crossing is not what escapes" is therefore established for that class only.

---

## C. Cross-note observations

1. **P2 settles a premise of P3.C1.** P3.C1 needs nested world-i error sets along selection paths. P2 Lemma 6.1 shows these are non-generic in n = 3.
2. **P2.3 and P3.8 point the same way.** Every known control of R5 or of the facet maps passes through an additive object: P3's witness ψ, or P2's straight charts, which are equivalent to a realisation. The precise residual is the same in both notes: R-a′/R-b′ for a pre-system, plus ordinal tie-breaking (Q1).
3. **Stronger nearby target.** P3.8.3(1) asks for an additive pre-system with (W1)–(W3). By the established statement in B3, such a ψ with E(ψ) = ∅ is impossible. So the pre-system must carry atom chords, which is exactly R-b′ (or R-a′ if p* lies on a chord). No new route is opened.

## D. Files

`p23ref_py/`:
- `box_exact.py`, `box_exact.out`: P2.2, exact box margins by ratio parametrisation; linear and kinked cases at ε = 0.05, 0.3, 0.6.
- `rotation_check.py`, `rotation_check.out`: monotone rotation of the kinked maps; the jump of a′ pairs with C_J in both signs (twoslope obstruction).
- `p3_examples.py`, `p3_examples.out`: Monte Carlo geometry of P3 Examples 1 and 2.
- `nested_check.py`, `nested_check.out`: Monte Carlo spot check of P2 Lemma 6.1.
