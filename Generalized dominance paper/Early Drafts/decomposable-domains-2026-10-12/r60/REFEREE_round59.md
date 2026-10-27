# REFEREE_round59. Referee report on PP74, PP75 and PP76 (round 59), and on REFEREE_round58's Theorem 6.2′

24 October 2026. Independent referee for round 60. I read BRIEF60_two_generation, BRIEF59_H_repair, AUDIT_round60 and its answers, LEAD_selection_count §1, AUDIT_completion, PP59_hypotheses_ledger, DESIGN_MEMO §8.27–§8.28 with their correction bullets, PP56 §4 (u¹, (2V), Λ, Theorem L), and PP74, PP75, PP76 and REFEREE_round58 in full.

**Labels.**
- PROVED: I checked the argument, or I give one here.
- CHECKED: exact computation (exact Fraction cells; solid angles in floating point from exact vertices), or exhaustive enumeration on an abstract atom model.
- NUMERICS: deterministic quadrature where noted. No Monte Carlo is used anywhere.

All code is in `r9/REFEREE59_py/` and imports nothing from PP74_py, PP75_py, PP76_py or REFEREE58_py.

**Verdict scale:** correct / correct with repair / wrong.

---

## 0. Verdicts at a glance

| Item | Verdict | Short reason |
|---|---|---|
| PP74 Thm 3.2 (preservation) | **correct with repair** | Every axiom checks. Three hypotheses must be stated: (H) committed models, defenders and rivals are H-models with supports in R; (CM) continuity in measure for the sections bullet; and a corrected Lemma 2.3(ii). It is a one-shot theorem for a whole class, not a recursion. |
| PP74 Cor 3.3 (no joint defeat) | correct | It is immediate from 3.2. The content lies in the class-level hypotheses (c) and (d), which every jointly defeating configuration violates. |
| **Uniform bound α(t) ≤ a·p(t), a < 1** | **PROVED** (for every t₁ > 0) | The first-order identity α′(0) = 2β′(0) holds exactly, by a reflection symmetry. Continuity and positivity do the rest. |
| **The identity α = 2p/3** | **wrong** | It holds only to first order. Exact cells give α/β = 2.0035 at λ = 0.81, α/β > 2 for all small t > 0 on the grid, and α/β = 1.944 at the (2V) edge. |
| PP74 Lemma 4.2 / Thm 4.3 | **correct with repair** | Take θ ∈ (0, θ*], θ* = (1 − a)/(1 + a). The "within reach" condition then holds automatically. θ ≤ 1/5 is restored via the gain-A mass α_A (CHECKED: α_A/p ≤ 0.5572). Conditions (U1), (N1), (c) and (d) were brute-forced on a star sample with no failure. |
| PP74 Prop 4.5 (𝔇₁ closed, record-intrinsic; mass cap) | correct | It uses (CM) along the rays, which I prove for posterior rays. |
| PP74 Cor 4.6 | correct as a conditional | CONJECTURE G is constrained by the three-ray calculation (§4.3). |
| PP74 Thm 5.1 (endpoint clause) | correct | axiom-level ((TC) + (IB)) |
| PP74 Prop 5.2 and the anchoring impossibility | correct; **re-run reproduces it** | T–B₃: 0/254; T–B₁: 0/254; B₃–B₁: 62/62 (937 distinct candidates, not 949) |
| PP75 Boolean model (Lemmas 1.1–1.2) | correct | |
| PP75 Pattern Lemma (Thm 3.1, Cor 3.2) | correct | PROVED; CHECKED on 78 pairs covering all 13 order types, twins and (2V) |
| PP75 (N1), (N2) | correct | |
| PP75 (N3) | correct with repair | "These are all the refusals" is false: extended rivals exist (PP76 Thm 1.1). The rule is complete for *defeat*, which I CHECKED. |
| **PP75 Theorem C** | **correct on its domain (N1 ∧ N2)** | 52,514 configurations, 561 defeats, 0 mismatches. Outside N1 ∧ N2 the formula is false (513 small configurations), which is harmless. |
| PP75 X\*_j (Prop 9.1) | correct | (a) PROVED; (b) explicit certificate; (c) 7 escape candidates re-checked |
| PP76 correction-set lemma (Lemma 1.3, Cor 1.4) | correct | |
| PP76 rigidity of pure-fill refusal worlds | correct | |
| **PP76 "one acceptance never exhausts a full-support source"** | **wrong as stated; correct with repair** | It holds for coupled refusals alone (0/6,750). Once strict-guidance refusals are counted, one acceptance defeats T in 80/6,750 cases (PP76's own check_defeat76: 666/16,212). Cor 1.2 also needs B and C coherent. |
| PP76 Prop 1.5 (sections, one acceptance) | correct with repair | It needs (CM), and it carries the same guidance caveat. |
| **PP76 Prop 1.6 (exhaustion criterion)** | **wrong as a defence criterion; repaired** | It ignores worlds blocked by strict guidance (disagrees in 137/5,640 pairs). The repaired criterion has 0 mismatches. |
| PP76 Lemma 2.2 and the record-level lesson | correct | |
| REFEREE_round58 Thm 6.2′ | **correct under (Sym) + (CM)** | (CM) holds on the two-ray family 𝔽 (PROVED), so 6.2′ is unconditional there. |
| Audit's three-ray calculation | correct | PROVED; CHECKED exactly on all three rays |

---

## 1. PP74

### 1.1 Theorem 3.2 (preservation): correct with repair

I checked every axiom against the proof.

- **Reflexivity, (IB).** These hold because 𝓡 is a union of record classes.
- **Strict (G).** Base strict (G) holds. A strictly reverse-guidance record lies in no d ∈ 𝔇, by (N1).
- **(TC).** By (c), a triangle contains at most one domination: in a 3-cycle every two links are consecutive, and consecutiveness needs X_{d₁} = B_{d₂} on D₁ ∩ D₂. Copies do not matter, because the values on the supports are fixed. The cases split as follows.
  - *No domination.* Base (TC) applies.
  - *Favourable world.* The cycle sum Σ V_w = 0 is contradicted by V_w(d) > 0 together with endorsed links. Lexicographically, the same works for Λ, since the levels add termwise.
  - *Unfavourable world, two guidance links.* (N1) is contradicted.
  - *Unfavourable world, one guidance link.* A non-trivial weak-guidance record is *strict*, because distinct values have distinct ranks. So the other link is a forced refusal, and (d) makes it strictly reverse-guidance.
  - *Unfavourable world, two carried links.* Lemma 2.2 gives a cover, and (d) applies.
- **Protection, no ties, strict domination of X_d.**
  - An all-world acceptance into Z ∈ 𝒦 is either a domination (then Z carries d⁻¹, contradicting (U1)) or a base all-world acceptance (then (B2) gives a tie partner, so the record is trivial).
  - d⁻¹ is refused everywhere: it is not guidance (N1), not carried (U1, B1), and not in 𝔇.
- **Defence.** 𝓡 ⊇ 𝔅 and 𝓡 satisfies (TC), so no base acceptance is withdrawn.
- **Sections.** A section of 𝓡 is the union of the base section and the preimage of the closed set 𝔇 ∪ {∅} under p ↦ rec(C_p, Z).
- **What it does not claim.** Theorem 3.2 does not claim global (C) or (S) beyond these items.

**Repairs (statements, not new mathematics).**

1. **(H) H-scope.** 𝒦 ⊆ H, every B_d and X_d lies in H, and supp d ⊆ R. Lemma 2.1(ii) (O = ∅) and Lemma 2.3(iii) use this. With four-valued intermediates and carriers outside H, covers with O ≠ ∅ are not excluded. The theorem is stated "for any u¹-endorsed base", but its proof is an H-theorem.
2. **(CM) continuity in measure.** For every p_n → p in the index set, μ{C_{p_n} ≠ C_p} → 0. The sections bullet needs this to make p ↦ rec(C_p, Z) continuous. Closed base sections do not supply it.
   - *For posterior families with a continuous index map (CM) is a lemma (PROVED).* C_m(g) depends only on the signs of the three forms Σ_i m_i v^α_i g_i. Off the null union of their zero planes these signs are locally constant in m, so C_{m_n} → C_m pointwise a.e., and dominated convergence gives convergence in measure. The same holds for vertex-wise rescalings with continuous vertex maps.
   - For a general committed defender, (CM) must be assumed together with its index plan.
3. **Lemma 2.3(ii) is misprinted.** "C = X on Bet_w(B, X) ∩ {C ≠ B}" is vacuous for two-valued models: on Bet ⊆ D, C ≠ B forces C = X.
   - The derivation (G₁ ⊆ D ∩ {C = X} and Bet ⊆ G₁) gives **Bet_w(B, X) ⊆ {C = X}**, i.e. Bet_w(B, X) ∩ U_C = ∅.
   - In H this is again U_C ⊆ Up_w(C), which is what (iii) asserts.
   - The application in Thm 4.3 already uses the correct form ("C ≠ X = A on Bet_k(B, X), so it gives nothing").

**Cor 3.3 (no joint defeat): correct.** It is a consequence of the theorem, not an extra fact.
- Hypotheses (c) and (d) are conditions on the whole class 𝔇 against the whole family 𝒦.
- So every jointly defeating configuration must violate them. PP76 Example 1.7 violates (d) at the unfavourable world of one of its two dominations: if both were admissible, Thm 3.2 would leave T a base defence against T ⊕ L, which Example 1.7 excludes.

**Not recursive (agreeing with the audit).** A second application cannot use 𝔅 ∪ 𝔇₁ as a base: d ∈ 𝔇₁ has V_k(d) < 0, so (B1) fails. What a second generation needs is to apply the theorem **once** to 𝔇₁ ∪ 𝔇₂, against:
- a fresh endorsed base 𝔅′ on the enlarged committed family 𝒦′, with (B1), (B2) and closed sections;
- with (U1) re-checked for old records against new committed models (PP76's (U1′));
- with (c) checked across generations;
- with (d) checked for 𝔇₁ against the new carriers.

### 1.2 The uniform bound: PROVED; the identity: wrong

**Definitions (exactly as in PP74 §4).**
- k is fixed and B_{k,t} = C_{u+tδ_k}, i.e. m_k = λ := e^{−3t} with the other two coordinates equal to 1.
- L(t) := {B_{k,t} ≠ T}.
- α(t) := mass of the odd-k part of L(t); β(t) := mass of each odd-i part, i ≠ k (the two are equal by the (i j) symmetry); p := α + β.
- Masses are |g|-masses. These are proportional to solid angles, because |g| and g/|g| are independent under μ.

**The four pieces of the layer** (PROVED; C_m(g) = T(m∘g), c := 16/7, written for k = 3, i = 1, and w(y) := (1 + |y|²)^{−3/2} on unit-distance charts):
- gain A₃: {(x, y, −1) : x, y > 0, cλ < x + y < c};
- lose B₃: {(a, b, 1) : (a, b) ∈ Q ∖ λQ}, where Q is the kite conv{0, (0, −7/16), (−7/23, −7/23), (−7/16, 0)};
- lose A₁: {(−1, y, z) : y, z > 0, y + λz ≤ c < y + z};
- gain B₁: {(1, b, z) : (b, z) ∈ diag(1, 1/λ)Q ∖ Q}.

No other piece occurs: A₃ only gains, B₃ only loses, A₁ only loses, B₁ only gains. Then α is the sum of the first two masses and β the sum of the last two. Orientation (s > 0) never binds on the (2V) range λ ≥ 7/16; note that cλ ≥ 1 iff λ ≥ 7/16.

**Theorem U (PROVED).** For every t₁ > 0,

  a(t₁) := sup_{0<t≤t₁} α(t)/p(t) < 1,  and  α(t)/p(t) → 2/3 as t → 0.

*Proof.*
1. **Continuity and positivity.** α and β are continuous on [0, t₁] by (CM) along the ray. β(t) > 0 for t > 0, since lose A₁ contains an open set.
2. **First order.** Divide each mass by 1 − λ and let λ → 1. Dominated convergence on the explicit integrals gives:
   - gain A₃ → c∫₀^c w(x, c − x) dx;
   - lose A₁ → ∫₀^c z·w(c − z, z) dz;
   - lose B₃ → ∫_{∂Q} (x·n) w ds (the radial field);
   - gain B₁ → ∫_{∂Q} x₂n₂ w ds (stretch of the second coordinate).

   Reflect by x ↔ c − x, using w(a, b) = w(b, a). This gives ∫₀^c z w(c − z, z) dz = ½c∫₀^c w. The kite and w are symmetric under (x₁, x₂) ↦ (x₂, x₁), which gives ∫ x₂n₂ w = ½∫(x·n) w. So β′(0) = ½α′(0) exactly, and α/β → 2.
3. **Conclusion.** α/β is continuous on (0, t₁] with a finite limit at 0, hence bounded by some M. So α/p = (α/β)/(1 + α/β) ≤ M/(1 + M) < 1. ∎

NUMERICS (quadrature, `layer59.out`):
- α′(0) = 0.790178, made up of gain A 0.579715 and lose B 0.210463;
- β′(0) = 0.395089;
- both reflection ratios are 0.500000000.

**The identity α = 2p/3 is false (CHECKED, `layer59.out`, `peak59.out`).** α/β is:
- 2.000003 at λ = 0.9999;
- 2.000261 at λ = 0.99;
- 2.0035 at its peak, λ ≈ 0.81;
- 1.9440 at the (2V) edge λ = 7/16.

PP74's own numbers agree with mine to five digits (α = 0.22310, β = 0.11140 at (20/21)⁶). Their "β/p = 0.333" was a rounding of 0.33303. On the grid, α/p > 2/3 for all small t > 0.

So Lemma 4.2's step "mass(E ∩ L(t₋)) ≤ α(t₋) = (2/3)(1 + θ)e ≤ (1 − θ)e for θ ≤ 1/5" **fails at θ = 1/5 at every small scale**, by about 10⁻⁴.

**Quantitative bounds (CHECKED by monotonicity).** α, β and α_A are non-decreasing in t, because the layers are nested (nesting checked, 0 violations). So on each grid interval,

  α/p ≤ α(t_{j+1})/(α(t_{j+1}) + β(t_j)).

A geometric grid in 1 − λ (ratio 1.01, 1,332 points) gives, on all of 10⁻⁶ ≤ 1 − λ ≤ 9/16:
- **α/p ≤ 0.6695**;
- **α_A/p ≤ 0.5572**, where α_A := mass of the gain-A_k part, the only part of L(t) that E can meet.

Below 10⁻⁶ the ratios are within 10⁻⁵ of their limits, 2/3 and 0.4891.

### 1.3 Lemma 4.2 and Theorem 4.3: correct with repair

**Repaired Lemma 4.2 (PROVED, given Theorem U).** Fix θ ∈ (0, θ*], with θ* := (1 − a)/(1 + a) and a = a(t₁). Then W_θ(E) ≠ ∅ for **every** non-null measurable E ⊆ Sil(T) ∩ A_k ∩ L_k(t₁).
- The side condition (1 + θ)e ≤ p(t₁) is automatic: e ≤ α_A(t₁) ≤ a·p(t₁), and a(1 + θ) ≤ 1 − θ < 1. So "within reach" can be dropped.
- *Proof.* As in PP74, with mass(E ∩ L(t₋)) ≤ α_A(t₋) ≤ α(t₋) ≤ a(1 + θ)e ≤ (1 − θ)e.

On the (2V) range:
- the α route gives θ* ≥ 0.198 (CHECKED);
- the α_A route gives θ* ≥ 0.284 (CHECKED);
- so θ ≤ 1/5 is valid, but only through α_A, and only as a CHECKED constant.

**The rest of Theorem 4.3: correct.**
- The favourability formula V(d) = (p − e)(1 at i ≠ k, −2 at k) is exact. It does not use the identity.
- (U1), (N1) and (c) are as written. (c) uses Lemma 4.1, whose overlaps I re-computed as non-null for all ray pairs at three scale pairs.
- (d) holds. The refusal part follows from Cor 1.4 of PP76. For the cover part, I re-derived that the only cover is (B_{k,t′}, T) with t′ > t, and that its link is (E ∖ L : h → S) ⊕ (D″ : B_{k,t′} → T), which is strictly reverse-guidance at k.
- (B2) for 𝔅_Λ holds:
  - Λ is a linear order per world, so it is acyclic and (TC) is vacuous.
  - Removing uncarried acceptances keeps acyclicity, protection, and committed defences (a committed source's defence record is carried by itself).

**CHECKED (`check43_59.out`): brute force, independent of PP74's proof.**
- *Sample.* T, B_{3,λ} for λ ∈ {20/21, 9/10, 4/5}, and B_{1,λ}, B_{2,λ} for λ ∈ {20/21, 17/20}. This gives 86 atom signatures and 26 rivals E, each with three states per group (in, out, split), and 42 (E, defender) pairs.
- *Triangles enumerated.* Every triangle through a copy of d, with **W and Y four-valued and atoms splittable**.
- *Results.* (N1), (U1), (c) and (d) at world 3 all hold, with 0 failures in each.
- *Control (`control43_59.out`).* The same test at the favourable worlds 1 and 2 finds 126 refusal failures and 96 cover failures. That is as it must be: there the sum argument, not (d), closes the triangles.

### 1.4 Prop 4.5: correct

I checked the proof step by step.
- Along a subsequence, k_n is constant and t_n → t*.
- E_n → E* in measure: E_n ∖ L_n = D_n ∖ L_n, and E_n ∩ L_n = (L_n ∩ Sil(T) ∩ A_k) ∖ D_n.
- The window inequalities are closed.
- If e_n → 0, the cap p ≤ Ke forces t_n → 0, so r = ∅.

**Two remarks.**
- The proof uses (CM) along the rays (L_n → L(t*)), which holds by §1.1.
- The cap is genuinely needed. Without it, the limit rec(B_t → T) would be accepted at all worlds, which is even a strict-(G) violation at k, because B_t ⊴_k T.

Section closure followed by copying cannot leave 𝔇₁ ∪ {∅}, because membership is a property of the record.

### 1.5 Theorem 5.1 and Prop 5.2: correct

**Theorem 5.1.** I re-derived the triangle.
- Y′ is equal to B″ on P, X on Q, C on F, and X off D″ ∪ F.
- Its links are (P : D → B″) ⊕ (F : D → C), carried by D, and (Q : C → B″) ⊕ (F : C → D), carried by C.
- Only (TC) and (IB) are used, so it is axiom-level.

**Prop 5.2.**
- (i) and (ii) follow from Cor 1.4 of PP76 and the two-value observation.
- (iii) The δ's satisfy δ₁ + δ₂ + δ₃ = 0 and are pairwise independent. So sδ_i − rδ_j = tδ_k with s, r ≥ 0 and t > 0 forces (i, s, r) = (k, t, 0), i.e. c = b.

### 1.6 Anchoring impossibility: re-run (CHECKED, `anchor59.out`)

**Re-implementation.**
- Exact cells come from my own code.
- The candidate families were generated afresh: a 7 × 7 posterior grid, vertex-wise single-world down-shifts, and vertex-wise mixed rescalings. They contain **937 distinct models, not 949**. Twelve coincide across families, and the grid contains T itself.
- ASR's affectedness was computed from PP76 Thm 1.1, both with all copies and with the restricted family.

**Results.**
- T–B₃ splices: 254/254 have a candidate passing (N1) and (U1), but **0/254** have an anchored candidate, in both modes.
- T–B₁ splices: the same, **0/254**.
- B₃–B₁ splices: **62/62** have an anchored candidate, in both modes.

PP74's numbers are reproduced. This confirms that anchoring, not (N1) or (U1), is what fails.

---

## 2. PP75

**Boolean model (Lemmas 1.1–1.2): correct.** On R the two available choices have j-ranks {0, 2} and 1, so W_j = A Δ I_j. Guidance is inclusion of error sets.

**Pattern Lemma (Thm 3.1, Cor 3.2): correct (PROVED; CHECKED, `pattern59.out`).**
- *The A_k cell.* Vertex k binds, since the vertex-i form exceeds it by 9(m_ih_i − m_kh_k) > 0. C_m accepts iff m_ih_i + m_jh_j > 16m_k/7.
- *The B_k cell.* The kite argument is right: contractions map Q into itself, and a dilation moves the vertex (−7/16, 0) out of it.
- *Check.* 78 random exact pairs, six for each of the 13 weak orders of r. There were 0 pattern-set mismatches, 0 twin-source failures, 0 (2V) violations, and 0 failures of "pointwise comparable at w iff r is a single raise of w".

**(N1), (N2): correct.** N1 is strict (G). N2 is right: B′ := B[Δ(Z, X) ↦ Z] is an all-world tie partner of Z, and it is incoherent when Δ(Z, X) is not a.e. conic.

**(N3): correct with repair.** The triangle is right: Y ⪯ B by (IB), B ⪯ X, and X ⪯ Y by guidance, so (TC) would reverse strict guidance.

The sentence "these are *all* the refusals one domination forces on Z-carried records" is false. Copies with a context W ≠ X off D refuse the *extended* rivals Z[G₁ ↦ B][G₂ ↦ n] (PP76 Thm 1.1, Prop 3.2).

The restricted family is, however, **complete for defeat**: an independent all-copies brute force (`exh59b.out`) finds 59 defeats among 5,129 single dominations, and all 59 are realised by some T[S ↦ B]. So Theorem C is an exact *defeat* test, but not a description of all surviving defence options.

**Theorem C: correct on its domain (CHECKED, `thmC59.out`).**
- *Enumeration.* Abstract atoms have kind ∈ {A, B}, an odd world, and values (Z, B, X) ∈ {h, S}³, giving 36 relevant kinds. I took **all** configurations of at most 4 kinds, plus 30,000 random ones with 5–7 kinds: 96,711 configurations in all. Brute force ran over S ⊆ Δ(Z, B) with three states per atom, with defeat meaning that every world is blocked by strict guidance or by the refusal block.
- *On (N1) ∧ (N2).* There are 52,514 configurations, 561 of them defeats, and the closed form agrees in every case.
- *(N1) ⟺ covering identity.* 0 mismatches.
- *Outside (N1) ∧ (N2).* The closed form misses 513 defeats with at most 3 atoms. The simplest is one A₁ atom with (Z, B, X) = (S, h, S) (`thmC59b.out`). The parenthetical "non-nullity" clauses do not make the statement general. This is harmless, because N1 is necessary for any domination. Repair: state Theorem C under (N1) and (N2).

**X\*_j (Prop 9.1): correct (`xstar59.out`).**
- (a) W_j(X\*_j) = ∅, so no H-model beats X\*_j at j: PROVED. On cells, no member of 𝒮 = {u, six shifts by 21/20} is strictly 3-better anywhere.
- (b) Incoherence. I gave an explicit certificate:
  - a is just outside A(T) near the junction (−7/9, 16/9, 0), with a₃ = 10⁻⁶; there a ∈ R and X\*₃(a) = h;
  - b = (0.3, 0.9, −0.2) is deep in A(T) ∖ R, with X\*₃(b) = h;
  - a point of the segment, at relative position 5·10⁻⁶ in R with h₃ < 0, has X\*₃ silent there, on an open cell.

  A coherent acceptance set is a convex cone, so X\*₃ is incoherent.
- (c) Escape. C_{u∘(1+te₃)} for t ∈ {1/5, 21/100, 1/2, 1, 2, 299/100, 3} passes (N1), (N2), and the general four-valued copy-defeat test at T. For t ≥ 3 it answers −h on 8 cells of R. So the dominators lie outside H, as claimed.

---

## 3. PP76

**Correction-set lemma (Lemma 1.3; Cor 1.4(i)): correct.**
- If N = X a.e. on D, then rec(B → X) = rec(N[D ↦ B] → N). Protection then gives a tie, and direct (C) makes N[D ↦ B] coherent.
- But it differs from the coherent N exactly on the non-conic D, which is impossible.
- The hypotheses are needed as stated: D not a.e. a cone, and N coherent and protected.

**Cor 1.4(ii)–(iv) and rigidity: correct.** I re-derived (ii) from Theorem 1.1 with two values.
- On G₁ we get N = X.
- U_N must lie in D ∖ G₁, which forces U_N ⊆ Up_w(N).
- L_N ∩ Up_w ⊆ G, and G ∖ L_N ⊆ Up_w.
- (d) is automatic.

Rigidity (iv) follows because U_N ⊆ E: for a pure E, W_N = Up(E) for every dominator.

**Cor 1.2(i): correct as a statement about coupled refusals, with one missing hypothesis.**
- The proof needs B and C to be **coherent**, i.e. correct at unanimous problems. "No contradictory advice" is not enough: a C that is silent at a unanimous point admits n strictly better at all three worlds.
- With that hypothesis, my enumeration (`exh59.out`, 6,750 admissible acceptances) finds 0 cases where coupled refusals alone cover all three worlds.

**"One acceptance never exhausts a full-support source": wrong as stated.** A source cannot defend at w against a rival that is strictly w-better (strict (G)). Counting those refusals, a **single** acceptance leaves T without a defence in **80 of 6,750** cases.
- *Example.* Atoms (A₁, B₁, A₃, A₂), T = (S, S, S, S), B = T ⊕ {3, 4}, X = T ⊕ {1}. Then T refuses B at worlds 2 and 3 (coupled rule), while B is strictly 1-better than T. This is the forced pattern of REFEREE_round57.
- This is consistent with PP75 Theorem C (its (Da)/(Db) use guidance-blocked worlds) and with PP76's own `check_defeat76` (666/16,212).
- *Repair.* Say "the coupled refusals of one acceptance never cover all three worlds". Then defeat by one acceptance is decided exactly by Theorem C, and that is a constraint on the choice of dominator.

**Prop 1.5: correct with repair.** "A.e. g has C_{q_n}(g) = C_p(g) for large n" is (CM), along a subsequence. Closed sections do not provide it. The proposition shows that r itself does not force C_p ⋠_k Z. It does not exclude a refusal by strict guidance at the limit, i.e. a Theorem-C defeat at p. The gloss "never creates a section-limit conflict" should be read with that caveat.

**Prop 1.6 (exhaustion criterion): wrong as a criterion for defence; repaired (CHECKED, `exh59.out`).** As stated, every world must be assigned to an acceptance. Its brute force also counts coupled refusals only. Against true defeat (strict guidance counted), it disagrees on **137 of 5,640** random pairs.

**Repaired criterion.** Let σ map each world to an acceptance or to "g" (guidance). Then T has no defence against some rival iff for some σ:
- G₀ := ⋃_{σ(i)≠g} (L_{σ(i)} ∩ Up_i(T)) lies in Ω_σ;
- Ω_σ is non-empty;
- here Ω_σ := ⋂_{σ(i)=g} Up_i(T) ∩ ⋂_{σ(i)≠g} [R ∖ U_{σ(i)} ∖ (Down_i(T) ∖ L_{σ(i)})].

It agrees with brute force on all 5,640 pairs. Example 1.7 survives as an example of exhaustion by two acceptances.

**Lemma 2.2 and the record-level lesson: correct.** The proof is one line: the closed section at c, then (IB).

---

## 4. REFEREE_round58 Theorem 6.2′, and the three-ray calculation

### 4.1 Hypotheses

- **(Sym)** u¹ is PP56's field for an S₃-symmetric (2V) reference family containing 𝔽 ∪ 𝓘.
- **(CM)** For a_n → a in 𝔽, μ{C_{a_n} ≠ C_a} → 0. 𝔽 consists of posterior models with likelihood index, so (CM) holds (§1.1). It is stated here as the hypothesis the proof actually uses.

### 4.2 Theorem 6.2′ re-derived (PROVED)

**Statement.** Under (Sym) and (CM), 𝓡′_θ (PP72's 𝓡_θ, with 𝒟₀ replaced by the margin rule 𝒟₀^κ, κ ∈ (0, 1]) has every conclusion of PP72 Thm 6.2 on 𝔽. The defenders 𝓘 still carry no section obligation.

**Where (CM) enters, and nowhere else:**
- (i) **Step 1 (all acceptances have V_w ≥ 0) survives section limits.** |V(rec(C_{a_n} → X)) − V(rec(C_a → X))| ≤ ∫_{C_{a_n} ≠ C_a} 2 max|u¹| dμ → 0, by uniform integrability of |g|.
- (ii) **D_θ and K^κ are closed along sections.** V is continuous, and |m(supp_n) − m(supp)| ≤ m{C_{a_n} ≠ C_a} → 0.
- (iii) **G₁ is closed along sections.** A subsequence converges pointwise a.e., and discrete values then agree eventually.

**The rest is exact.**
- *Null limits.* If the limit is null, V(C_{a_n} → X) = Γ(a, a_n) by additivity of Φ.
- *The four Γ-shapes of 𝔽.* These are (p, p, −2p), (−p, −p, 2p), (q, −2q, q) and (−q, 2q, −q). Each has a negative coordinate (so it is not in D_θ), no κ-margin at world 1 (not in K^κ), and Γ₁ ≠ 0 (not in Z₁). So only G₁ remains, and its limit has V₁ > 0, which is a contradiction.
- *Non-null limits.* They stay in their class. V ≠ 0 is open, but it is given in this case.
- *(TC) reverses.* They land in Z₁.
- *Rules III–IV.* They never fire.
- *Copies.* They do not matter, because every class is record-intrinsic.

I re-checked the admissibility of 𝒟₀^κ. If V₁ is the only non-negative coordinate, then ΣV ≥ 0 for installed sources gives V₁ = |V|∞ ≥ max V_i + κ|V|∞. The theorem is correct.

### 4.3 The audit's three-ray calculation: correct (PROVED; CHECKED, `threeray59.out`)

On the down-shift ray of world k, V(T → B_{k,t}) = p(t)(3e_k − 1). This follows from PP73 Lemma 1.4's ledger and needs only β_i = β_j, not α = 2β.

By additivity of Φ, for a_n closer to T than a,

  V(C_{a_n} → C_a) = (p(t_a) − p(t_n))(2e_k − e_i − e_j).

So for X balanced against C_a, V(C_{a_n} → X) = γ_n(2e_k − e_i − e_j) with γ_n > 0.

Direct exact computation between pairs of ray members on all three rays gives V/γ = (2, −1, −1), (−1, 2, −1) and (−1, −1, 2) to six decimals, with γ = p(a) − p(a_n).

Consequences:
- An endorsed base defends C_{a_n} against X only at k, and closed sections force C_a ⪯_k X.
- On the δ₁-ray, the inward Γ-vector γ(2, −1, −1) has world-1 margin 3γ = 1.5|V|∞. So it lies in K^κ for every κ ≤ 1, and the section step of invariant (J) fails there.
- More generally, **no endorsed sectioned base on a family containing the down-shift ray of w₀ can refuse every balanced record at w₀**. The fixed-world refusal of 6.2′ cannot survive on the three-ray star.

**Coincidence test (PROVED; for Conjecture G).** Balancedness V(ρ) = 0 is a property of the record. The forcing above acts on ρ itself, through any interior ray-k carrier, followed by (IB). So:
- a null record ρ carried by interior members of all three rays is accepted at **all three** worlds;
- it is then dangerous exactly when ρ⁻¹ is carried by a committed model on a non-conic support, by the (N2)/Lemma 1.3 mechanism.

This is the precise "coincide after copying and section limits" test the brief asks the allocator to run.

---

## 5. What this changes for round 60

1. **Quantitative input.**
   - Use Theorem U with θ ≤ (1 − a)/(1 + a). Drop "α = 2p/3"; it is false.
   - For θ = 1/5, use α_A (CHECKED).
   - Write (CM) into every section transfer. For posterior and vertex-wise families it is a lemma; for other defenders it is a hypothesis.
2. **Theorem 3.2's real form is class-level and one-shot.** A two-generation construction must verify (c) across generations and (d) against the new carriers, over a fresh endorsed base on the enlarged committed family. PP74's condition (iv), strict-guidance refusals only, is the only part the audit asks to weaken. Its role in the proof is exactly the two "(d)" bullets of §1.1.
3. **Defence bookkeeping must count strict-guidance refusals.** PP76's exhaustion criterion needs the repaired form (§3). "One acceptance never exhausts" is true only for coupled refusals; Theorem C is the exact single-acceptance defeat test.
4. **The three-ray allocation.** Its first concrete obstruction test is the coincidence test of §4.3: a null record carried balanced by interior members of all three rays.

---

## 6. Scripts (`r9/REFEREE59_py/`; run `python3 -I -B <script>.py > <script>.out` inside the folder)

| Script → output | Content | Label |
|---|---|---|
| `lib59.py` | exact cells (Fractions), answers, ranks, types, solid angles | library |
| `layer59.py` → `.out` | α, β, α_A, V/p along the ray; (2V); first-order rates and reflection ratios; Lemma 4.1 overlaps; nesting | CHECKED, NUMERICS (quadrature) |
| `layerA59.py` → `.out` | α_A versus β_A (the 2β_A ≥ α_A route fails: min 0.781) | CHECKED |
| `peak59.py` → `.out` | 1,332-point geometric grid; monotone interval bounds α/p ≤ 0.6695, α_A/p ≤ 0.5572 | CHECKED |
| `check43_59.py` → `.out`; `control43_59.py` → `.out` | Thm 4.3: (N1), (U1), (c), (d) by brute force over four-valued W, Y with splitting; control at favourable worlds | CHECKED |
| `anchor59.py` → `.out` | re-run of the anchoring impossibility, all copies and restricted | CHECKED |
| `pattern59.py` → `.out` | Pattern Lemma, 13 order types | CHECKED |
| `thmC59.py`, `thmC59b.py` → `.out` | Theorem C against brute force; mismatches classified | CHECKED |
| `xstar59.py` → `.out` | X\*_3: (a), certificate for (b), escape candidates (c) | CHECKED |
| `exh59.py`, `exh59b.py` → `.out` | Cor 1.2 with and without guidance; Prop 1.6 and its repair; restricted-family completeness for defeat | CHECKED |
| `threeray59.py` → `.out` | three-ray Γ-shapes, direct between ray members | CHECKED |
