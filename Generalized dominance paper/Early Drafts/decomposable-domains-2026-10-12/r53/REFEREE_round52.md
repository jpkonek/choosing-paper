# REFEREE round 52 (PP60): section topology, radial transport, PP49–PP53

23 October 2026. Independent referee report for Brief 53. I referee the two audit notes and PP49–PP53 against the setting of BRIEF53 (three worlds, Gaussian μ, four-advice domain, posterior family C_a = D_{M_a}, ε = 3/10 for the kink).

**Labels.**
- PROVED: a complete argument is given or checked here.
- CHECKED: an exact computation in `r9/PP60_py/` (Fractions or integers). Every script ends ALL PASS.
- NUMERICS: floating-point or sampled evidence.
- CONJECTURE / OPEN: as stated.

**Verdict scale.** correct / correct with repair / wrong (counterexample) / unclear.

---

## 0. Summary

| Item | Verdict |
|---|---|
| Section topology §1: face preservation; continuous face-preserving maps are onto | correct |
| §2: ideal I; one conic model per I-class; addition lemma (closed fibres) | correct |
| §3: local construction theorem, (TC) proof | correct with repair: Q must contain guidance (weak (G)), not only strict (G). A counterexample shows this is needed. |
| §3: the 3-of-4 strict vote has no accepted triangle, but has strict 4-cycles | correct (CHECKED) |
| Radial transport: J, transfer of (G), (IB), (TC), defence and protection; the annular section condition; "isomorphism, not reduction" | correct; one caveat on measures |
| PP49 Theorem A (1)–(5) | correct; scope: no single-world ties, by design |
| PP49 "exactness" paragraph | correct with repair. It overstates "the remaining gap is exactly strictness and continuity". |
| PP49 Lemma 3.4(i), the three-valued triangle criterion | correct (sufficient); exact given its first clause (PP53) |
| PP49 boundary treatment: Prop 4.3, Rem 4.4, Prop 5.2 | correct; (H4)(b) needs PP53's normalised form (H4)(b′) |
| PP49 Theorem N | unclear: it rests on FF2's import chain, not re-refereed here. Lemma 7.2 is correct. |
| PP50 Theorem K and the box certificate (Prop 6.2) | correct as stated; re-run identical; box independently sampled |
| PP51 Thm 5.1 and its instance | correct. Its (R0) justification cites a theorem that needs strict CG2, but the step holds without it (Lemma R2 below). |
| **New: the kink survives single-world ties in the gate union** (Thm K′) | PROVED here: strict CG2 can be dropped; only a.e.-unique own-Bayes of the odd model is used |
| PP52 Thm 4.1 (KKM test) | correct; survives single-world ties; its continuity hypothesis is genuinely stronger than (S) and should be stated for the whole verdict |
| PP52 Prop 7.3 | the gap is confirmed as written; correct with repair (an extra hypothesis and dense padding); the hypothesis is checked on a grid for the kink pairs |
| PP52 OA theory (Thms 3.1–3.6, Lemma 3.2) | correct; scope: (PX) plus strict (G) forbid all single-world ties |
| PP53 four-model certificate | correct (re-run identical; type set and world-1 infeasibility independently confirmed) |
| PP53 boundary results (Lemma 2.1, Props 2.2–2.5) | correct; Prop 2.2's zero-weight sub-cases are sketched |
| PP53 width budget (Lemma 3.4) | correct |
| PP53 spectator constraints (Lemma 3.5) | correct with repair: its last step uses refused reverses, which fails under its own common-shape hypothesis. That configuration is a single-world tie, not a (TC) violation (CHECKED). |

**Main points for Brief 53.**

1. **The kink obstruction in the gate-union architecture does not depend on forbidding single-world ties.** The step "closed triple test fails ⇒ (TC) fails" holds under (R0) using only the pair sandwich (Lemma R2). (TC) itself forces that sandwich by a tie-robust triangle.

   The only strictness Thm 5.1 needs is that the odd model is strictly Bayes, or CG2 is strict, on a non-null part of **one** of the two certificate cells.

   So the residual escape inside the architecture is narrow: the odd model must be **exactly indifferent between answering and silence, a.e. on both certificate cells**. That is PP51's Gap, sharpened (§4.3).
2. **PP52 Thm 4.1 survives ties**, as the brief says. Its real extra hypothesis is closedness of the verdict along a path of *changing* rivals. The audit's local construction (§3) can violate that hypothesis on bounded records, so Thm 4.1 does not bind it.
3. **PP49, PP52's OA and PP53's certificates are all tie-free architectures.** PP49 Lemma 3.2 and PP52 Lemma 3.2 (with strict (G)) each exclude every single-world tie. None of their sufficiency results can say anything about the tie-permitting branch.

---

## 1. AUDIT_section_topology

### §1. Face preservation and surjectivity — correct (PROVED)

**Face preservation.** I checked the argument.
- If K = M_{f(a)} meets the complement of Δ_S, then g = (1 on S, −L off S) has min_K p·g < 0 for large L. This holds on an open set E.
- D_K is not "accept g" there.
- The rival C_{f(a)}[E ↦ accept g] is a strict improvement at every world of S, so strict (G) refuses it at every w ∈ S. That contradicts competitiveness on supp a.

No tie assumption is used. For the posterior family, supp M_b = supp b, so supp f(a) ⊆ supp a.

**Surjectivity.** The KKM covering is right. On Δ_S, Σ_{i∈S} f_i(a) = 1 ≥ Σ_{i∈S} q_i, so some i ∈ S has f_i ≥ q_i. Boundary q follow by compactness.

Two small notes:
- Since b ↦ C_b is a continuous injection of the compact Δ into L⁰(μ), it is a homeomorphism onto its image. So the theorem applies to any selection a ↦ C_{f(a)} that is **continuous in measure**; continuity of f itself need not be assumed.
- The consequence "cannot avoid the kink neighbourhood" is correct relative to Theorem K. By §4 below it also holds without strict CG2, provided the selected models near T are a.e.-uniquely Bayes.

### §2. The ideal I, one conic model per class, the addition lemma — correct (PROVED)

**The second example ideal.** It is closed under subsets and finite unions. It contains no non-null cone: for a cone over a non-null set Θ of directions, the radial integral is ∞ on Θ. It contains every null set, by Fubini in polar coordinates.

**Uniqueness.** Two conic models with d(C, D) ∈ I differ on a conic set in I, which is null. Hence there is at most one conic C with d(C, X) ∈ I.

**Addition lemma.** For a fixed X, the added index set is ∅ or the fibre {a : C_a = C}. That fibre is closed when the selection is continuous in measure, and a union of two closed sets is closed.

The caveats in the note are right:
- this is addition only;
- (IB) is preserved only if B_i is record-closed;
- nothing about (G), (TC), defence or (C) follows.

### §3. Local construction theorem — correct with repair (PROVED; CHECKED)

**The (TC) case split is exhaustive and correct.** It has three cases:
- ≥ 2 links in I: the third link is in I, so all three are in Q;
- exactly 1 link in I: two guidance links, and strict (G) of Q kills a non-trivial third link;
- 0 links in I: all three links are guidance.

The step "all three links belong to Q_i" uses **Q ⊇ guidance on I-supported records**. The hypothesis says only "strict (G)".

**Counterexample showing the hypothesis is needed (CHECKED, `construction_ref.py`, control Q_bad2).** Take:
- Q = reflexivity plus all common-context copies of two records B → C and C → A, where A is a strict guidance improvement of B, all supported in J;
- J = the "I" part of a finite model.

This Q has strict (G), (IB) and (TC). But R = guidance ∪ (I ∧ Q) has 48 violating ordered triples: A ⪯ B (guidance), B ⪯ C, C ⪯ A, and B ⪯ A is refused.

**Repair.** State "Q_i satisfies (G), i.e. weak and strict guidance". The 3-of-4 vote does contain guidance: all four strictly guiding judges strictly favour a nontrivial worsening.

**Exhaustive finite check (CHECKED).** On 256 models over 4 points with I = subsets of 3 points, for Q = the 3-of-4 vote and Q = a weak single-judge preorder (with ties):
- Q and R both satisfy reflexivity, weak and strict (G), (IB) and (TC) over all 256³ triples.

**The vote example.** The 9-versus-8 vote count is correct. 2-cycles are also excluded, since 6 votes would be needed and at most 4 are available. An explicit strict 4-cycle exists: judge k has magnitude 4 − ((r − k) mod 4) on region r, and every edge gets exactly 3 strict votes (CHECKED).

**§4 classification.** The ideal relation is an equivalence, so a triangle has 3, 1 or 0 within-class links, never exactly 2. This is correct.

---

## 2. AUDIT_radial_transport — correct (PROVED)

**F and J.** F is a diffeomorphism of H∖{0} onto A ∩ H, with r ↦ 1 + r/(1 + r) a bijection (0, ∞) → (1, 2). It preserves null sets and directions, hence ranks. J maps records bijectively onto A-supported records and commutes with common-context substitution.

**What transfers.** (G), strict (G), (IB) and (TC) transfer verbatim. The identity JC_a Q X ⇔ C_a Q X_a uses Q's (IB) between pairs with **different exteriors** (B versus C_a). So Q must be a relation on all A-supported records, not only on encoded models. The note says this ("comparisons supported in A"), and it is the right reading.

**Protection.** The transfer of defence, domination and all-world-tie exclusion is correct. The tie clause as stated ("no all-world tie with any distinct A-supported modification") is stronger than direct (C), which permits ties with coherent rivals. That is harmless as a sufficient condition, but a construction may want the weaker, (C)-exact version: "no all-world tie with X_a for incoherent X".

**The annular section condition.** It is exactly R's section condition. The ordinary Q-section condition does not imply it, since the rival X_a moves with a.

**Exact isomorphism.** Confirmed. Relations with (IB) on all records of H correspond one-to-one with relations with (IB) on A-supported records, preserving every axiom.

**One caveat (not an error).** F does not preserve μ.
- Additive fields, envelopes, L¹-continuity and the (H4)-type hypotheses transport with the weight dF_*μ/dμ.
- So a "Gaussian" annular construction is a construction for a different measure on H, and conversely.
- Any later continuity or integrability argument on A must state which measure it uses.
- Also, every encoded comparison has bounded support, but the encoded coherent traces JC_a are not conic. So the addition lemma of §2 gives nothing on A, as the note says.

---

## 3. PP49 (sufficiency theorem)

### 3.1 Theorem A — correct (PROVED); scope is tie-free

I checked every step.
- **Lemma 3.2.** Under (H2) every nontrivial accepted record has its reverse refused, so **no single-world ties exist for any pair of models**. Theorem A is therefore a tie-free sufficiency theorem by design.

  The proof also needs finite gate values, which is (H4)(b), although the lemma lists only (H0), (H2), (H5). PP53's wording point about V_w is right.
- **Lemma 3.3.** The shortcut/old-value argument is correct.
- **§4.2 (TC).**
  - Case |F| ≤ 2: telescoping uses integrability of U, from (H4)(b).
  - Case |F| = 3: this is (H3).
  - "(TC) ⇔ (H3)" needs (H4)(b) as well as (H0), (H2), (H5).
- **§4.3.**
  - Competitiveness via weak (H1) is correct.
  - The strong undominatedness argument is correct, including b = e_w and a = e_w.
- **Prop 4.3.**
  - The three-term realisation bound and the value convergence are correct.
  - Remark 4.4 is correct, with one repair: the closure of {(a, b) ∈ F_w(X) : b ≠ e_w} adds only points with b = e_w, whose records are guidance-accepted. So π₁ of the closure lies in G_w(X) ∪ π₁F_w(X).
- **§4.5.** The KKM dominance and the characterisation of the undominated class are correct.

### 3.2 The exactness paragraph — correct with repair

The claim "the remaining gap between the hypotheses and the axioms is exactly the strictness in (H2) and the L¹-continuity in (H4)" is too strong. Gaps 2 and 3 of §6 are not strictness or continuity issues:
- positive constants for one-signed pairs (a bounded-ratio condition);
- positivity of κ at three-valued points.

Also, (H1)'s necessity and (H0)'s "essential" necessity are relative to the gate-union architecture (H5).

**Repair.** "Within the gate union (H5), the hypotheses exceed what the axioms force only by:
- strictness in (H2);
- positive constants on one-signed pairs;
- (H4)(b)."

### 3.3 Lemma 3.4 (the three-valued criterion) — correct (PROVED)

- **Enumeration.** I re-derived it: P_ab, P_bc, P_ca, Q_o.
- **(i)** is a correct sufficient condition.
- **(ii)** is correct.
- **(iii)** is correct. In the "rays" step the zero-sum relation can occur with all signs reversed, which is the same condition. "Exact on two-valued triples" relies on PP47 under (BR).
- **PP53's sharpening is correct:** given its first clause, (i) is necessary and sufficient for (H3).

### 3.4 Boundary treatment — correct

- **Lemma 1.1** is correct.
- **Lemma 1.2** is correct. (A1) was re-run: ALL PASS, identical output.
- **Prop 5.2** I re-derived case by case, including the degenerate orders and k = 0. It is correct.
- **§5.2's two sentences are inconsistent.** One says "This gate is needed"; the next says "I do not claim these gates are necessary". Keep the second.
- **(H4)(b) at edges.** It fails for the natural transported design (PP53 Prop 2.5). Theorem A should be stated with PP53's (H4)(b′).

### 3.5 Theorem N — unclear

Lemma 7.2 is correct.
- (a) is immediate.
- (b): the countable supremum, the shortcut loss of γ/4, and the limit for b ∉ Q with c* = 0 allowed are all correct.

Theorem N itself is only as good as FF2 Thm 4.1 / Cor 4.3 and its import chain, which I did not re-referee. Corollary 7.3 uses a *pointwise* witness, whereas Theorem N excludes *integrated* ones. That is fine, since 7.3 is motivation. Theorem N, like Theorem A, assumes the strict (H2).

---

## 4. The kink: PP50 Theorem K, PP51 Thm 5.1, and ties

### 4.1 Re-runs (CHECKED)

All outputs are identical to the authors' (`PP60_py/rerun_*.out`):
- `kink_check.py` at t = 1 and t = 1/10;
- `kink_box.py`: 220 determinants, none uncertified, ALL PASS;
- `kink51.py`;
- `kinkscan51.py`: the table matches PP51 §5.2;
- `four_model_exact.py` on both JSONs;
- `posterior_checks.py`.

### 4.2 Independent check of the instance and the box (CHECKED, `kink_ref.py`)

My own cell enumeration (`ref_lib.py`, written from scratch) gives the following.
- At t = 1 and t = 1/10:
  - 18 two-valued disagreement types;
  - both A-alone cells (Wr = {1} and Wr = {2, 3});
  - (K3);
  - strict admissible orders 3 > 1 > 2 (AB) and 2 > 1 > 3 (AD).
- **Weak form of (K2).** Under weak Bayes and closed CG2, the per-type pair condition is: max_W d > min_R d, **or d is constant** (Lemma R1 below).

  So the weakly admissible vectors are the strict ones plus the all-tied vector. Both satisfy z^B_2 ≥ z^A_2 ≥ z^D_2. (K2) holds as Thm 5.1 states it, with "≥". The scripts' "no tied vector is admissible" is true for the strict test only, and is harmless.
- **Box sampling.** At 40 random exact points of the box × (0, 1/5], with s down to 2·10⁻⁷, the type set equals the s = 1/10 set and the certificate holds.
- **The s = 400/1259 sign change.** At the centre, 2 of the 220 determinant signs flip between s = 0.31761 and 0.31781, as PP50 says. But the **type set does not change**, and t = 1 has the same type set as t = 1/10. PP50's cut at 1/5 is conservative, not necessary.

**Lemma R1 (PROVED; NUMERICS cross-check: 3,000 LPs, 0 disagreements).** For answerer X and silent Y at a type with correct set C and wrong set W, the weak condition is: there is y > 0 with Σ_C y ≤ Σ_W y and Σ_C ρy ≥ Σ_W ρy, where ρ = ω^X/ω^Y.

This holds iff max_C ρ > min_W ρ or ρ is constant.

*Proof.* If max_C ρ ≤ min_W ρ =: r, chain Σ_C ρy ≤ rΣ_C y ≤ rΣ_W y ≤ Σ_W ρy. Equality throughout forces ρ ≡ r. The converse direction is direct. ∎

### 4.3 PP51 Thm 5.1 — correct; where strictness enters

I re-derived steps 1–4. The pairing of signs, forms and cells is right. Two refinements follow.

**(a) Strictness is needed on only one of the two cells.**
- In step 4, the case S_k < z^A_k contradicts with no strictness at all.
- The case S_k > z^A_k contradicts with no strictness at all.
- Only S = z^A needs a strict inequality. There, strictness at **either** cell, on a non-null subset, suffices.

So the uncovered case (PP51's "Gap") is narrower than stated:
- z^A lies on the segment [z^B, z^D];
- A's own-Bayes inequality and the cell's CG2 replacement are **tight a.e. on both** certificate cells.

**(b) The (R0) step "closed test fails ⇒ (TC) fails" is cited to PP47 Thm 4.1.** That theorem assumes strict CG2 a.e. for every pair. But the step is true without strict CG2:

**Lemma R2 (PROVED).** Work under (R0) or (R), at world w. Assume every pair of gated members satisfies the closed sandwich (constants in [0, ∞)² ∖ {0}). Then every gate-accepted record with **strictly positive** value has its reverse refused, by guidance and by every realiser.

*Proof.* Let X → Y be accepted through N with Φ^N > 0, support S.
- Guidance refusing the reverse is immediate: otherwise X → Y would be a weak improvement and Φ^N ≤ 0.
- Let P be a realiser of Y, so S ⊆ D_NP, and take sandwich constants c_N φ^N ≤ c_P φ^P a.e.
  - If c_P = 0, then φ^N ≤ 0 on S, which contradicts Φ^N > 0.
  - If c_N = 0 < c_P, then φ^P ≥ 0, and φ^P ≠ 0 a.e. on S by strict guidance, so ∫_S φ^P > 0.
  - Otherwise ∫_S φ^P ≥ (c_N/c_P)Φ^N > 0.
- In every case Φ^P(Y → X) < 0. ∎

The sandwich is itself forced by (TC) **with ties allowed**: REFEREE_round50 Thm 3.1(c) closes its triangle with a guidance link whose reverse is a pure improvement.

In Thm R1(ii) the separation produces a triangle with all three gate values **strictly** positive. So by Lemma R2:

> Under (R0), (TC) ⇒ the closed triple test with nonnegative constants, for every gated triple, single-world ties allowed.

(K3) then makes the constants positive (R1(iv)'s argument).

### 4.4 Theorem K and a tie-robust version

**Theorem K as stated — correct (PROVED, given Prop 6.2 and Thm 5.1).**
- The density argument is right. Both boxes lie in the 0.2s-ball (chart displacements ≈ 0.146s and 0.126s) and occupy a fixed fraction of it.
- For non-measurable G, read |·| as outer measure; the density theorem holds for outer measure.
- (b)'s phrase "not perfect at some world" should read "not perfect at **every** world of its support". That is the shell-rival hypothesis of PP52 Prop 7.1, and it holds for all non-vertex posterior models.

**Theorem K′ (PROVED here; tie-robust).** Use ε = 3/10 and the gate union under (R0), with integrable fields and weakly own-Bayes gates. Assume (TC) at every world, **single-world ties allowed**. Let G_s be the set of gated indices whose own-Bayes optimum is a.e. unique. Then G_s ∩ U₀ has outer measure 0.

*Proof.* Take a₀ ∈ G_s a density point of G_s. Then B, D are gated, by density of the gated set ⊇ G_s.
- (TC) ⇒ the pair sandwich (Thm 3.1(c)).
- With Lemma R2 and Thm R1(ii), this gives the closed triple test.
- (K3) gives positive constants.
- Thm 5.1, with odd model a₀ strictly Bayes, gives a contradiction. ∎

**Consequence.** With ties allowed but the gate union kept, a positive-measure selection near T is possible only if almost every selected model near T is **exactly indifferent** between its answer and silence, a.e. on both certificate cells of the kink triples through it.

Whether such Bayes-indifferent members can keep direct (C) is OPEN. PP47 Thm 2.5 points to F2. This is the precise target for the "ties allowed" run of Brief 53, inside the gate architecture. It says nothing about non-gate relations.

### 4.5 Smaller points

- PP51 §0 item 4 ("under either strict or zero-accepting gates") is **correct after Lemma R2**, but not by the cited PP47 Thm 4.1.
- PP50 §0 item 5's statement that "every set G of gated posterior indices … is null" includes strict CG2 in its hypotheses. With K′ that can be replaced by "a.e.-uniquely Bayes members".
- PP50 Cor 4.3, Thms 4.1–4.4 and the checkpoint Thms 2.1/2.2 were not in my remit. I did not re-run them.

---

## 5. PP52

### 5.1 Theorem 4.1 (KKM test) — correct; survives ties; hypothesis to be restated

The proof is right.
- The Lyapunov chains E_k(t) give D(s) continuous in measure.
- On the face Δ_S, r(s) is a strict pure improvement at every v ∉ S, so strict (G) confines acceptance to S ∩ supp N.
- KKM and (IB) then give Y ⪯_w M at all three worlds.
- The conclusion is "dominated or all-world tied with an incoherent Y". Undominatedness and direct (C) exclude both, so **no tie prohibition is used**.

**Hypothesis.** Closedness of {s : r(s) accepted at w}, where the rival N[D(s) ↦ M] changes with s. This is **not** (S), which fixes the rival.

The parenthetical "this holds whenever own-gate acceptance is Φ^N(r) ∈ Γ^N_w, Γ closed" is incomplete as written: other realisers and guidance also accept. Correct repair: run KKM on F′_w := {s : N's own gate accepts r(s) at w} ∪ {guidance}. These sets are closed, and they cover the faces **provided N's defence is delivered by its own gate**. That holds in the union (PP49 §4.3) and in OA (Thm 3.1).

The audit's local construction (AUDIT_section_topology §3) assigns arbitrary record-based verdicts to I-supported records, so it need not satisfy this hypothesis. Thm 4.1 does not bind it.

### 5.2 Proposition 7.3 — the gap is confirmed; correct with repair

The proof adds a set E on which M′ ≠ M. Then M′ is no longer a realiser, but **every other** b with C_b = M a.e. on D ∪ E still is.

If D ∪ E stays away (in angle) from M's switching planes, every b in a neighbourhood of M realises the record. So "M is the sole realiser" does not follow. The audit is right.

**Repair (PROVED).** Add the hypothesis:
- (U_NM): no index b ≠ M has C_b = M a.e. on {N ≠ M}; and likewise (U_MN) for the forward side.

Then replace E by a **dense open subset** of int{N ≠ M} with μ(E) < η. Each C_b ≠ C_M differs from C_M on a union of open cells, so if that union meets {N ≠ M}, E meets it in positive measure. So P(D ∪ E) = {M}. Strict argmax and positive maximum survive for small η, and the CG2-necessity triangle then gives a (TC) violation. That violation is itself tie-robust: its closing reverse is a pure improvement.

**Evidence for (U) on the kink pairs (NUMERICS search; candidates CHECKED exactly, `realiser_ref.py`).** On a 40-grid of interior indices plus a fine grid around M:
- the Monte Carlo filter left 14, 9 and 1 candidates for (T, C_B), (T, C_D) and (C_B, T);
- exact cell enumeration rejected all of them.

So no alternative realiser was found. This is evidence, not proof, for all b ∈ Δ.

### 5.3 OA theory (Def 2.0, Lemma 3.2, Thms 3.1–3.6) — correct; scope is tie-free

I checked the following.
- Strict (G) via a.e.-unique own-Bayes.
- Thm 3.1: the defence world lies in supp b because θ^b_w > 0 at a positive maximiser.
- Lemma 3.2 under (PX).
- Thm 3.3.
- Thm 3.4. The stated dual {ζ_w ≥ Σ|ζ_v|, ζ_v ≤ 0} is the dual of {R_w ≥ max(0, R_v)}, not of {R_w = max R_v}. It is valid because own-Bayes uniqueness makes every accepted nontrivial gate record have R_w = max R > 0. This should be said.
- Thm 3.5: the same projection argument as PP49 Prop 4.3. The boundary remark is right.
- Thm 3.6.

**Hidden scope.** (PX) plus strict (G) imply that **no two distinct models are tied at any world**. One direction of a tie is accepted by a gate (Lemma 3.2 refuses the reverse) or by guidance (the reverse is then a pure improvement). OA is therefore no route to the tie-permitting branch. Its extra room (Prop 6.1, tilted certificates) is room among strict relations.

Conjecture 7.2 is correctly labelled. Thm 4.3/Cor 4.4 were not re-refereed.

---

## 6. PP53

**Four-model certificate (Thm 3.3).**
- Re-run identical: ALL PASS for both JSONs.
- Independently (`fourmodel_ref.py`, CHECKED):
  - my own enumeration gives exactly PP53's 28 types, with no three-valued cell;
  - CG2 intervals recomputed from the JSON magnitudes match PP53's table;
  - an exact multiplicative Bellman–Ford finds no global constants at world 1 (both files), and at world 2 for the main file;
  - triple slack holds.
- Own-Bayes was verified by three separate authors' codes, and I did not repeat it.
- Agreement cells are not checked by the script. They are trivially completable: with interior weights, separate magnitudes for the h-versus-silence and −h-versus-silence comparisons make the common advice the strict optimum.
- **Verdict: correct.** This is a tie-free certificate: strict CG2, so no ties.

**Lemma 2.1.** Correct.

**Prop 2.2.** Correct in substance. Two points:
- w* must be chosen with λ^a_{w*} > 0. Prop 5.2's finite-or-+∞ choice of D_{w*} guarantees this.
- The zero-weight sub-cases (step 5) and the "expensive" completion should respect strict guidance: "expensive" only at worlds where the value is wrong.

**Prop 2.3.** Correct.
- The common U with humble scaling is a strict potential, so strict CG2/CG3 follow. It is a witnessed module, as PP53 says.
- The script was not re-run (`boundary_module.out` reports ALL PASS).

**Props 2.4–2.5.** Correct. (a) is the right repair of PP49's (H4)(b).

**Lemma 3.1, Lemma 3.2.** Correct. The pointwise "improvement order" is acyclic because ranks would be equal pointwise around a cycle.

**Lemma 3.4 (width budget).** Correct. The telescoping uses one t_i per triple, and that is legitimate.
- Hypothesis: the triples (X_i, X_{i+1}, F) pass the closed test. By §4.3 this is forced by (TC) under (R0) without strict CG2.
- The PP51 Lemma 2.5 / PP50 diagonal forms are the special case F ∈ cycle.

**Lemma 3.5 (spectator constraints) — correct with repair.**
- The algebra is right: κ·Q_o = α_a + β_b − α_c − β_c, and the pair conditions are as stated.
- "Only together with the spectator inequality" should read "pairs plus α_a ≤ α_c suffice". The spectator inequality is not necessary.
- **The last step is wrong under its own hypothesis.** Common-shape fields make (H2) an *equality* at those points, so PP49 Lemma 3.2 cannot be invoked.

  In fact every reverse link has value 0 and is accepted. `ties_ref.py` (CHECKED) builds the two-type example: all six links have value 0.
- So the conclusion "(H3) fails" is correct. But the configuration is a **legitimate single-world tie**, not a (TC) violation. Under the Brief 53 axioms it is a candidate *use* of indifference, not an obstruction.

**§4 (PP53's check of PP49).** I agree with it, with the additions in §3 above.

---

## 7. Ledger of hidden strictness and other silent assumptions

| Where | Assumption used silently or too broadly | Effect |
|---|---|---|
| Section topology §3 | Q ⊇ guidance (stated only as "strict (G)") | needed; counterexample in §1 |
| PP49 Lemma 3.2, (TC) ⇔ (H3) | finiteness of gate values, i.e. (H4)(b) | add to the hypothesis lists |
| PP49 Thm A, PP52 OA, PP53 certificates | strict (H2) / (PX) / strict CG2 ⇒ no single-world ties anywhere | they are tie-free sufficiency results; silent about Brief 53's branch |
| PP51 Thm 5.1 (R0) step | cited via strict CG2 (PP47 Thm 4.1) | not needed: Lemma R2 |
| PP51 Thm 5.1 convexity step | strict Bayes or strict CG2 for the odd model | needed on one cell only; the residual case is tightness a.e. on both |
| PP50 Thm K | strict CG2 a.e. | replaceable by a.e.-unique own-Bayes (Thm K′) |
| PP52 Thm 4.1 | closedness of the whole verdict along changing-rival paths | stronger than (S); state it for the own-gate route |
| PP52 Prop 7.3 | "M sole realiser" | needs (U_NM), (U_MN) and dense padding |
| PP52 Prop 7.1, Thm K(b) | "not perfect at some world" | read "at every world of its support" |
| PP53 Lemma 3.5 | refused reverses under common shape | false there; ties instead |
| Radial transport | measure | F does not preserve μ; continuity and integrability hypotheses transport with a density |

---

## 8. Scripts (`r9/PP60_py/`; run `python3 -I -B <script> > <script>.out` inside the folder)

| Script | Content | Label |
|---|---|---|
| `ref_lib.py` | own exact posterior advice and cell enumeration (vertex walk) | library |
| `kink_ref.py` | kink instance at t = 1 and 1/10: K1, K3, strict and **weak** K2; 40 exact box points; determinant flips near 400/1259; LP check of Lemma R1 | CHECKED (+ NUMERICS part) |
| `fourmodel_ref.py` | PP53 type set re-derived; intervals, triple slack, exact Bellman–Ford | CHECKED |
| `realiser_ref.py` | search for alternative realisers (Prop 7.3) | NUMERICS filter; exact rejection CHECKED |
| `construction_ref.py` | exhaustive finite check of §3's construction theorem; control showing Q ⊇ guidance is needed; 4-cycle | CHECKED |
| `ties_ref.py` | PP53 Lemma 3.5's zero triangle is a tie, not a (TC) violation | CHECKED |
| `rerun_*.out` | outputs of the authors' scripts re-run unchanged; all identical to theirs | CHECKED |

**Most useful next step for Brief 53.** By Thm K′, inside the gate union the kink survives single-world ties except through **Bayes indifference** of the odd model on both certificate cells.

The axiom-level run should therefore test first:
- whether a pattern in which T (and nearby members) are exactly indifferent between answering and silence on the two A-alone cells can satisfy undominatedness and direct (C) with the exact encoding of the brief;
- then whether a non-gate relation (e.g. §3's construction, transported by §2's radial map) can avoid even that.
