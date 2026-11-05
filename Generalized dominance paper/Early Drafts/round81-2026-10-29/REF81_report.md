# REF81: referee report on FS81_report.md and S81_report.md

Labels: PROVED (I re-derived it) / CHECKED (I checked every step as written) / WRONG / UNCLEAR.
Conventions: LDG uses ⪯ for "at least as good"; the application uses ⪰. I follow each report's own convention.

## Summary

- **FS81.** Every mathematical claim survives. The finite-sequence theorem, the weakest hypothesis (TD), the strict chain (A3) ⇒ (T∀) ⇒ (W) ⇒ (TD) and its three counterexamples, Lemma G with all three triples, Theorem 4.1′, the claim that (A2) is not used, and the two-world (A1)+(A4) counterexample are all correct. One fix is needed in the paper-ready LaTeX.
- **S81.** The core results are correct: Prop C, Theorem A, Corollary A1, Prop 1, Prop B as stated, the R2 counterexample, R\*, R\*_Q, L_lin, consistency, and the R5 example once ½ is in the interior of Q. Three statements are **wrong as worded**: the headline of results-table item 2, the "price of (S)" sentence, and the "necessity" remark on tie classes. Each drops the score-consistency hypothesis, and §S below gives a counterexample. The paraphrase of Prop B in item 5 overstates what Prop B proves.

---

## Part F: FS81_report.md

### F1. The finite-sequence theorem

- **§1.1, theorem under (TD): PROVED.** Take k least with m_k dominating m_{k−1}. Each earlier consecutive pair weakly dominates without dominating, so the pair is tied at every world. Then (TD) carries dominance down the chain. No reflexivity, completeness or transitivity is used.
- **The auditor's proof under worldwise (A3): CHECKED.**
  - Every substitution in it is through a pair tied at every world: (x₀,x₁), …, and finally (x₀,z).
  - So it already runs under (T∀).
- **Equivalence (a) ⇔ (b) ⇔ (c): PROVED.** The direction (c) ⇒ (a) uses the sequence m, m′, c with r = 1. Because m′ is tied with m, m′ does not dominate m, so c must.
- **Chain (A3) ⇒ (T∀) ⇒ (W) ⇒ (TD): PROVED.** For (W) ⇒ (TD): apply (W) to the tied pair (c, m), with m′ weakly dominating m. This makes c and m′ tied, a contradiction.
- **Strictness examples: CHECKED.** I checked all three against the definitions.
  - (T∀) without (A3): the m∼m′ tie holds at ω₁ only.
  - (W) without (T∀): the weak-dominator sets of m and m′ are both {m, m′}.
  - (TD) without (W): (TD) holds vacuously, and c weakly dominates m′ but not m.
- **§1.3, a hypothesis is needed: CHECKED.**
  - The one-world, three-model example works.
  - The complete variant, which adds m₀ ∼ c, also works: c ≺ m₁ strictly, and nothing dominates m₀.
- **§1.4, existence of a sequence is equivalent to dominance under (TD): PROVED.** It is trivial with r = 0.

### F2. Lemma G (geometric lemma)

**Audit of where undominatedness enters: CHECKED.** Undominatedness enters only:
- in the last sentence of Lemma 3.4(i);
- in the opening clause of Lemma 3.4(ii), where only (U1) is needed;
- through Lemma 3.3.

Lemmas 3.5 and 3.6 use only (U1), (U2), (M3) and, in 3.5(c), (M2). app_long already has the ranking-free form: its lem:U2 assumes only (U1) and not (U2).

**Step A: CHECKED.**
- The identities Z∖W = E₊₊∖W and W∖Z = W∩(−E₊₊) are exact.
- The change is guided at every world.
- The change is non-null exactly when W violates (U1).

**Step B (c = 1): CHECKED.**

| Requirement of def:change | Verification |
|---|---|
| Masses | All three sets have mass t. G₂ has room: μ_c(W∩B(d,ρ)∖G₁) ≥ μ_c(B(d,ρ)) − t > t, using (U1), (M3) and t < ½μ_c(B(d,ρ)). |
| Disjointness | G₁∩G₂ = ∅ by construction. G₃∩W = ∅ while G₁∪G₂ ⊆ W. |
| Margin on the sets themselves | inf(z′−x′−y′) ≥ 2δ − 3ρ = δ/2 pointwise on the balls. So κ = δ/2 works for every point of the sets, not just a.e. |
| Inclusions | Exact. |
| Atoms | Excluded by Lemma 2.8(a), as Sierpiński's theorem requires. |

The conclusion holds: W′ misses G₂ ⊆ E₊₊, which has positive mass, so W′ violates (U1).

**Step C (c ∈ {1,2}): CHECKED.** I recomputed every bound.
- B(vᵢ′, r) ⊆ B(vᵢ, 9η/8) ⊆ V.
- B(z₀, r) ∩ cl V = ∅, because inf(s − z) ≥ η/c − r > 0 and cl V + E₊₊ ⊆ V.
- The margin is η/c − r − 2r/c. This is 5η/8 for c = 1 and η/4 for c = 2, so κ = η/4 works.
- J₀ ⊆ B(v₁, 3η/2) ⊆ V, and inf(x − w) > r on B(v₁′, r) × J₀.
- The four mass bounds on t give room for G₁ (mass t), G₂ (mass t) and G₃ (mass ct).
- μ_c(J) ≥ μ_c(J₀) − t > 0, and J ⊆ W₁.
- Taking w ∈ J∩supp J and x ∈ G₁∩supp G₁ gives a violation of (U2).

The existence of v₁, v₂ follows from the contrapositive of lem:identify(c). That lemma uses (M2) for {P_K = 0} null and for atoms (Lemma 2.8(c)), and (U1) for where the atoms fall. No ranking is used.

**Case split: CHECKED.** Case (a) has r = 0. Case (b) has r = 1. Case (c) has r = 1 if X₁ violates (U1), and r = 2 otherwise, via Step B. Whether r = 2 is ever unavoidable remains UNCLEAR, as FS81 says; nothing depends on it.

### F3. The revised theorem

- **(A3) ⇒ (A3′): PROVED.** The second use of (A3) is through the tie X ∼_ω Y, applied with Z ⪰_ω X.
- **Theorem 4.1′ under (A1), (A4) and (A3′): PROVED.**
  - (A1) gives strictness at every world, so Z dominates X_r.
  - (A4) gives the weak steps.
  - (A3′) is needed only for pairs consisting of a model and its consolidation.
- **(A2) is unused: CHECKED.**
  - In the old proof, (A2) enters only the strictness step of Lemma 3.3 (app_long lem:tie and lem:constie).
  - (A3) alone gives that step by the global argument.
  - The consistency proposition verifies (A2) but nothing uses it, so dropping it changes nothing else.
  - I did not re-audit the repair theorem (app_long §6). The claim that it uses no ranking axioms is plausible from its statement, but I have not CHECKED it.
- **(A1) and (A4) alone fail: PROVED.** I checked every clause.
  - (A1) holds. In clause (ii), the consolidation margin forces z(ω) > 0 on G₃, which contradicts guidance. Clause (iii) is excluded outright.
  - Every model satisfying (U1) is undominated. For finite Ω, ∩_ω{h(ω) > 0} = E₊₊, so a guided-everywhere change from it is null. A consolidation change from such a model is never guided at every world, so clauses (ii) and (iii) answer each other.
  - X = E₊₊ ∪ B((1,−1), ¼) is incoherent. The set 2(D∩U) ⊆ B((2,−2), ½) is non-null and misses X.
  - (M2) holds for the Gaussian, since boundaries of convex sets are null.

### F4. Paper-ready LaTeX: one fix

- **lem:up-step.** The instruction "text … from 'Put 4δ'" leaves out the choice of x and z.
  - Either begin the proof with "Take x∈supp X and z∈supp(E∖X) with z−x∈E₊₊."
  - Or, better, cite or copy app_long's lem:U2, which is already this lemma.
- The rest is correct, and \M_L and lem:ties exist in LDG.
- The proposed line edits point at the right places: ldgshort l.244, and ldg_full l.51, l.548 and l.654.

---

## Part S: S81_report.md

### S1. Preliminary facts

- **F1 to F4: CHECKED.**
  - F1 holds because r·h ≠ 0 a.e.
  - F2 is Lyapunov's theorem, with (M1) for finiteness.
  - F3 follows from separation inside aff Δ, using P over conv(A∪{δ_ω}) = min(P_A, h_ω).
  - F4 works because a coherent D is a cone and null sets are scale-invariant. If D_Q∖B = D a.e., then the scaled ball λB, which is disjoint from B and inside D_Q, gives a non-null difference.

### S2. Theorem A, Prop C, Corollary A1, Prop 1

- **Prop C: PROVED, under its stated hypothesis** (score-consistency against incoherent rivals).
  - Steps 1–3 use thm:finite(i)–(ii) at the KKM point p\*.
  - In step 4, F4 turns any strict all-coordinate improvement into an incoherent one.
  - Step 5 is separation against the open orthant. Step 6 is F1.
- **Theorem A and Corollary A1: PROVED.**
  - The integral ranking is score-consistent ("Strict score increase").
  - It protects V = D_Δ, which is imprecise for n ≥ 2.
  - The thm:local form reduces to the thm:finite form: G = Ω forces F = Ω.
- **Prop 1 (a)–(f): CHECKED.**
  - In (d), the open set D_q∩H_ω minus the closed set cl D_R is null, hence empty. F3 then gives R ⊆ [q, δ_ω].
  - In (e), the segment [q, δ_ω] with q interior contains only one vertex.
  - In (f), the sets A_ω(D_q) are disjoint closed sets that cover the connected Δ, and at least two are nonempty.
- **The n = 2 numerical claim** (a precise model beats an imprecise one at both worlds) can be upgraded from CHECKED to **PROVED**.
  - Write the arcs as (φ−π/2, φ+π/2).
  - Moving from D_[a,b] to D_t with φ_t = (φ_a+φ_b)/2 = m and half-width d gains 2cos m·(1−cos d) > 0 at world 1 and 2sin m·(1−cos d) > 0 at world 2.
  - Both gains are of second order in d, which matches the observed margin of about 0.26(b−a)².

**WRONG: table item 2, the "price of (S)" sentence, and §5(c), "Prop C shows that tying D_Q with some precise model is necessary".** These state the conclusion of Prop C for any ranking satisfying (S). That is false without score-consistency against incoherent rivals.

Counterexample, for any credal set Q and any Ω, assuming (M1):

> Y ⪰_ω X iff Y = D_Q a.e., or Y = X a.e., or (X is incoherent and s_ω(Y) > s_ω(X)).

This ranking satisfies the following:

| Property | Why it holds |
|---|---|
| (A1) | A guided-everywhere non-null change starts at an incoherent model (lem:guidedeverywhere) and raises every s_ω. The reverse comparison fails. |
| (A2) | In any violation, Z ≠ D_Q and X ≠ D_Q, which forces s(X) ≥ s(Y) ≥ s(Z) > s(X). |
| (A3) | Only trivial ties occur. |
| (A4) | Only incoherent models have consolidations, and a consolidation raises every score. |
| C_L = {D_Q} | D_Q is at least as good as everything, and only D_Q is at least as good as D_Q. |
| (T) | Holds trivially. |
| (S) | Take c_p ≡ D_Q and A_ω ≡ Δ (for thm:local, Θ a singleton). |

So with Q = Δ, V is undominated, satisfies (S), and is tied with no precise model. The family {this ranking : Q a credal set} even satisfies LDG's (E), (A), (S) and (T).

Corrected statement: "Under (S) and score-consistency against incoherent rivals, every member of C_L is tied at every world with a precise member of C_L." The minimal-tie remark ("{D_Q, D_r} fails, since the vertex models must be in T") is correct under the same hypothesis: c_{δ_ω} must beat near-H_ω incoherent models at ω, which forces c_{δ_ω} = H_ω by F1.

Moral: (S), (T) and (A1)–(A4) together are weak constraints. Purely stipulative rankings satisfy them. R\* is not "the cleanest stipulation forced by (S)". It is the cleanest one that keeps score-consistency against incoherent rivals.

### S3. Possibility 1 (consolidation-guided selection)

- **Blocked for the integral ranking: CHECKED.**
  - Coherent models have no consolidations (proof of (A4) in prop:consistent).
  - The obstruction in Prop 1 lies entirely among coherent rivals.
- **(S) is not implied by (A1)–(A4), admissibility and (T): PROVED.**
- Remark: app_long's repair corollary (ldg_full l.654 cites [KCM, Cor 6.9]) gives the integral ranking the dominance property. So Corollary A1 also shows that (S) is strictly stronger than the dominance property. I have not re-checked the repair theorem itself.

### S4. Possibility 2 (coherent all-world ties)

- **R2 violates (A3) and (T∀): CHECKED.**
  - Y = V∪S is incoherent, because the cone property pushes λS outside.
  - Y ⪰₂ V by guidance.
  - H₂ → Y only removes a non-null part of {h₂ > 0}, and the change is available to H₂.
- **Prop B as stated: PROVED.**
  - F3 gives δ_{ω\*} ∈ Q′.
  - With M small, q′·t₀ < 0, so T misses cl C′.
  - The removal of T is guided at every ω ≠ ω\*.
  - C′ → Y only adds gambles inside H_{ω\*}.
  - Substitution through the tie then gives Y weakly dominating H_{ω\*}.
- **Overstated paraphrase (table item 5 and the "Moral").** Prop B covers only a vertex model H_{ω\*} tied with a coherent proper subset. It does not show that every coherent tie class is incompatible with single-world guidance. The general case is UNCLEAR: the construction needs C∖C′ ⊆ H_{ω\*}. The claim does apply to R\*, because R\* ties every H_ω with its coherent subsets.

### S5. The coherence-floor ranking R\*

- **(A1)–(A4), ties, admissibility and closure: CHECKED.**
  - Ties at a single world occur only between coherent models or between a model and itself. This gives (A3).
  - For (A2), the case analysis forces all three models to be incoherent.
  - C_L = C, and there are no mixed ties.
- **(S) via thm:finite with the closed-subset form: PROVED.**
  - D_p is almost coherent, since it differs from D_p ∪ {h ⪈ 0} only inside {p·h = 0}, which is null.
  - d_ω is continuous, by dominated convergence off {p·h = 0} with dominating function ‖h‖.
  - g_X > 0 on the compact Δ by F1, so ε_X = min g_X > 0.
  - The sets A_ω(X) = {d_ω ≥ ε_X} are closed.
  - The weighted average of d_ω over supp p is at least ε_X, so some ω in supp p serves.
  - The KKM dominator D_{p\*} even beats X in score at every world.
- **Arbitrary Ω via thm:local under (M1), (M2) and separable E: PROVED.** The sketch is complete.
  - S is weak-\* compact and metrizable, since E is separable.
  - θ ↦ ∫θ(h)⁺dμ is continuous by dominated convergence, so g_X attains a positive minimum.
  - θ ↦ m(D_θ) is norm-continuous by Bochner dominated convergence, since the indicators converge off {θ(h) = 0}, a null set by (M2). So each K_ω(X) is closed.
  - θ_F(p) = Σ p_ω δ_ω is continuous.
  - g_X(θ_F(p)) = Σ_F p_ω d_ω, so serving holds.
  - (M3) is not needed.
- **R\*_Q: CHECKED.**
  - The same proofs go through with "almost coherent" replaced by "in T_Q".
  - Other imprecise D_{Q′} are dominated, since they are not weakly Pareto-maximal (F2 and F1).
  - (S) needs only that X ∉ T_Q implies X ≠ D_p.
- **L_lin: CHECKED.**
  - It is a total preorder.
  - C_L is exactly the precise models, including the vertex models, since F1 holds for every r ∈ Δ.
  - It is closed under ties.
  - (S) holds via cor:closed-choice with the closed sets {s_ω(D_p) ≥ s_ω(X)}.
- **"M_m is exactly the interior precise models": UNCLEAR.** The supplied sources do not define M_m. The claim that Theorem A excludes imprecise targets does not depend on it.

### S6. R5 and consistency

- **R5: CHECKED, with one correction.** The example needs **a < ½ < b**, not just ½ ∈ [a,b]. If b = ½, then D_p∖D_Q ⊆ {h₁ > h₂, h₁ > 0}, so S₁ cannot exist. The change then adds only S₂ ⊆ {h₁ > 0}, which is guided at world 1, and D_p serves. With ½ in the interior of Q, the change X → D_p is available to D_Q and guided at neither world, as claimed.
- **Consistency for {R\*}, {R\*_Q} and {L_lin, R\*}: CHECKED.** (E), (A), (S) and (T) hold, as do (A1)–(A4), so LDG thm:argument applies. The integral ranking is excluded from every family that (S) covers, by Corollary A1. The family built from my counterexample ranking in S2 is a further, even more stipulative, consistent family.

---

## Corrections list

1. **FS81 §4.2, lem:up-step:** add the choice of x and z, or use app_long lem:U2.
2. **S81, table item 2, the "price" sentence and §5(c):** add "score-consistent against incoherent rivals". Without it they are WRONG; see the counterexample in S2.
3. **S81, item 5 and the "Moral":** restrict them to ties between a vertex model and a coherent proper subset.
4. **S81 §8, R5:** require a < ½ < b.
5. **S81:** upgrade the n = 2 claim that precise beats imprecise to PROVED, using the formula 2(cos m, sin m)(1 − cos d).
6. **S81:** mark the M_m link UNCLEAR.
