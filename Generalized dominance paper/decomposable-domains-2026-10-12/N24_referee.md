# N24. Referee report on N22_notes.md (part (A) for coherent almost-preference rankings)

13 Oct 2026. Independent referee. I did not write N22 and assumed nothing in it was correct until I had re-derived it.

**Read.** BRIEF6, BRIEF7; N11 (all: Prop 1.1, Fact 1.2, Lemma 3.1, Cor 3.2, Thm 2.1, Prop 5.1–5.2, Thm 5.5, Prop 5.6);
N13 (Props A, B and §1 on Walley); N14 §5.1 (Lemma Y, Theorem C2); N12 §1 (setting, (R1)/(R2), Lemma 1.1, Prop 1.2,
Prop 1.4); N15 §0 and §7 (Thm 7.1, Cor 7.2, Cor 7.3); N18 and N20 verdict tables (in particular N20's repair "(R1) is
needed at **every** q"); BRIEF.md (decomposable domains, axioms); Walley 1991 §§3.7–3.8 (w1991.txt 8200–8600); Walley 2000 §6
labels (w2000.txt). R11 Lemma IC / Lemma K / Fact 0 and CCIBU are used only as imported by N11/N13 (refereed there).

**Scripts** (`n24py/checks.py`, output in `n24py/checks_output.txt`). NUMERICS only. No verdict rests on them.
- (1) Lemma 1.1 bookkeeping: ∏_{j≥1}(1−2^{−j−1}) = 0.5776 ≥ ½. The counting inequality μ{f ≥ 1−η} ≥ (1−η)μ(A′)
  held in 4 000 random trials.
- (2) A discrete illustration of the Kneser step. inf_f max_P = max_P inf_f holds by LP duality. The value is 0 exactly
  when the *union* of the supports is ≤ η². This shows why Lemma 1.1 needs small carriers for **every** member of M,
  mixtures included, and not only for the generators.
- (3) A tie set lying outside the unit ball. This motivates the window repair in Prop 3.3 and Prop 4.1.

Verdict scale: CORRECT / CORRECT WITH REPAIR (local fix given) / GAP / FALSE.

---

## 0. Summary table

| Item | Verdict | One-line reason |
|---|---|---|
| Lemma 1.0 (strict (G) ⇔ P̄_i(A) > 0 on non-null non-singleton A) | **CORRECT** | (⇐) A_δ = {f ≥ δ} ∩ A; (⇒) W_i(M) worsened on A, then N11 Prop 1.1(ii) |
| Lemma 1.1 (common null set; Kneser) | **CORRECT** | Each member is pure on A, so it has small carriers (Lemma Y). Kneser applies: M weak-* compact convex, Φ convex, pairing bilinear and weak-* continuous in P. The level-set count and iteration check. Countable additivity is used only for μ |
| **Theorem 1.2** (𝒫_i^+ ≠ ∅, mixture-stable) | **CORRECT WITH REPAIR** (cosmetic) | P* = Σ2^{−k}P_k is in M_i as the norm limit of the *normalised* partial sums. Standing hypothesis: μ finite and atomless. "Absorbing" in the table is the wrong word: the property is "(1−t)P + tQ ∈ 𝒫^+ for t < 1" |
| Theorem 2.1 (α) T1 ψ^P-Bayes at interior p_T | **CORRECT** | N11 Cor 3.2(d). (FS^c) is now supplied by Thm 1.2. Splice off a common carrier of n pure parts, then Lyapunov, separation, and the IC push |
| Theorem 2.1 (β) coherent Bayes model at every p | **CORRECT** | N13 Prop B (β) re-derived. Only inequalities between full-charge values are used, and the integral minimum is always attained |
| Theorem 2.1 (γ) E(P) null; unique coherent off E(P) | **CORRECT** (proviso stated) | Tonelli on H × Δ. Needs distinct kinds of advice in the advice range to differ in some world's rank a.e. That is automatic for {+,0,−,×} with strict background orders. E(P) is Borel |
| Theorem 2.1 (δ) vertex models | **CORRECT** | Strict guidance, then the vertex lemma |
| §2 "gaps (2), (3) irrelevant on the integral route" | **CORRECT** | Atoms enter only through finitely many small carriers. Separation happens in integral coordinates |
| **Corollary 2.3** (cover ⇒ E(P) ≠ ∅ ∀P) | **CORRECT** | Contrapositive. E(P) = ∅ gives N12's (R1) at **every** interior q, which N15/N20 require. Null-set uniqueness alone would **not** suffice, and N22 does not claim it does (§2.3 below) |
| Lemma 3.0 (charge minimisers are pointwise CA minimisers) | **CORRECT** | Strict CA gain off a carrier, with pure parts unchanged |
| **Prop 3.3** (i), (ii) | **CORRECT WITH REPAIR** | The window R = (Z∖F) ∩ {\|g\| < 1} can be null (`checks.py` (3)). Use {\|g\| < r} with r large. The rest checks |
| **Theorem 3.1** (complete worlds: attainment at every p, unique coherent selected minimisers, E = ∅) | **CORRECT** | Steps 1–4 re-derived. Closed sections (S) plus completeness give l.s.c. along the selection. One-dimensional value intervals come from the integral part off a carrier. Bookkeeping: use ν_{C_m}(H∖F) > δ for large m |
| **Corollary 3.2** (no complete (CP-a) cover of T1) | **CORRECT** | Needs (UN) and non-adjacency. The alternative route via N15 Cor 7.3 also checks: T1 is the φ-minimiser at p_T by Lemma 3.0 and p_T ∉ E |
| Remarks 3.3 (CBOI consistency; why incomplete fails) | **CORRECT** | The diagnosis of Step 3 (converse of (W)) is right |
| §3.3 (D^CA) ⇒ (U) | **CORRECT** | N11 Thm 2.1's aggregate has E = ∅. Cor 2.3's argument applies to any field with (α)–(δ) and E = ∅, membership in ∏𝒫^+ is not needed |
| **Prop 4.1** (anatomy at a tie weight, CA members) | **CORRECT WITH REPAIR** | (iii) must start from a **coherent** B_0 (from (β)); otherwise "B′ incoherent" does not follow. Same window repair. (i) with ≥ 3 tied kinds of advice uses Lyapunov for partitions |
| N22.5 (shape of a cover) | **CORRECT** | Assembled correctly from Cor 3.2, Cor 2.3, Prop 3.3(ii), Prop 4.1(ii) |
| §4 sketches ("two-valued directional support functions", fans, rank-deficient vertex maps) | **NOT VERIFIED** (not load-bearing) | Labelled CHECKED (sketch) in N22. Nothing depends on them. The countable-t claim in item 2 is correct (atoms of a push-forward) |
| §5 (CP-a) definition vs Walley 1991 Thm 3.8.1 | **CORRECT WITH REPAIR** | Faithful: R0–R5 ⇔ D0–D4 ⇔ P̲ ⇔ credal set, with losses −Λ. Repairs: (ii) also needs the lower-envelope theorem (Walley 3.3.3 / 3.6.1); "Walley's D5 (conglomerability)" is Walley **2000**'s label, since in Walley 1991 D5 is avoiding partial loss; state the null-set reading as an equivalence (§5 below) |
| §5 suggested theorem, part (a) | **CORRECT WITH REPAIR** | Add (UN), or restrict to M_U. Read "(LF) at T1" as its domain clause, since T1 ∈ C_L is the hypothesis being refuted |
| §5 suggested theorem, part (b) | **CORRECT** | It is a reduction, not a no-go. The paper should say so explicitly |
| CONJ N22.U, N22.D | **Open** (correctly labelled) | §6 gives two referee reductions of (U) |

**Overall.** N22 contains no false step. The four repairs are local:
- the window radius;
- a coherent B_0 in Prop 4.1(iii);
- the normalised partial sums in Thm 1.2;
- (UN) in the suggested statement.

The headline results stand:
- Thm 1.2: (FS^c) is automatic;
- Thm 2.1: the integral reduction under (CP-a) alone;
- Cor 2.3: the sharp residual (U);
- Thm 3.1 / Cor 3.2: complete worlds cannot cover T1, with atoms allowed.

---

## 1. §1: full support (Lemma 1.0, Lemma 1.1, Theorem 1.2)

**Lemma 1.0.**
- (⇐) f ≥ 0 a.e. and f vanishes on problems whose advice range is a singleton (every evaluable model gives the same advice), so A ⊆ N_i a.e.
- A = ∪_δ ({f ≥ δ} ∩ A), so some A_δ is non-null.
- Then P(f) ≥ δP(A_δ) for every state, and the maximum over the weak-* compact M_i is attained.
- Strictness follows from N11 Prop 1.1(ii).
- (⇒) W_i(M) exists (finite measurable advice ranges). The worsened Y is in M (splicing), and 0 ≤ f ≤ 2‖λ_i‖1_A.
- CORRECT.

**Lemma 1.1.** I checked each point.
- *Per-member value.* For P ∈ M, P^c vanishes on subsets of A, so P(f) = P^s(f) for 0 ≤ f ≤ 1_{A′}. Lemma Y (N14
  §5.1, re-checked: λ_n = ν ∧ nμ is countably additive and below ν, hence 0) gives F with μ(F) < η²μ(A′) and
  P^s(H∖F) = 0. Then 1_{B_0}, with B_0 ⊆ A′∖F, lies in Φ and has P(1_{B_0}) = 0. This needs μ atomless.
- *Minimax.* The relevant form of Kneser (1952) / Fan (1953):
  - Y compact convex, X convex, F(x,·) concave and usc on Y, F(·,y) convex on X;
  - then sup_Y inf_X F = inf_X sup_Y F.
  - Here Y = M (weak-* compact, convex), X = Φ, F(f,P) = P(f), bilinear and weak-* continuous in P.
  - So inf_Φ max_M P(f) = max_M inf_Φ P(f) = 0. The outer max exists because inf_f P(f) is usc in P.
  - The point the script illustrates: the right-hand side is 0 because **every** P ∈ M, mixtures included, has
    inf_Φ P = 0. That is the hypothesis "P^c(A) = 0 for every P ∈ M". In a finite space it fails for mixtures, and the
    value is positive (`checks.py` (2)).
- *Level set.* (1−η²)μ(A′) = ∫f ≤ μ(B) + (1−η)(μ(A′) − μ(B)) gives μ(B) ≥ (1−η)μ(A′). Also 1_B ≤ f/(1−η).
- *Iteration.* ∏(1−2^{−j−1}) ≈ 0.578 ≥ ½. N = ∩B_k is non-null by σ-additivity of μ, and P(N) ≤ 2^{−k} for all k.
- CORRECT.

**Theorem 1.2.**
- *Essential supremum.* By the ccc, s* = ∪_k {ρ_{P_k} > 0}. For every P ∈ M_i, {ρ_P > 0} ⊆ s* a.e. So P^c(N_i∖s*) = 0
  for all P, and Lemma 1.1 plus Lemma 1.0 give s* ⊇ N_i.
- *Repair.* Σ_{k≤K}2^{−k}P_k has mass 1 − 2^{−K} and is not in M_i. Its normalisation is in M_i (convexity) and converges
  in norm to P*. Norm-closedness then gives P* ∈ M_i.
- The band projection is linear and contractive, so ρ_{P*} = Σ2^{−k}ρ_{P_k} in L¹.
- Mixture stability: ρ_{(1−t)P+tQ} = (1−t)ρ_P + tρ_Q.
- CORRECT WITH REPAIR.

The remark "false without weak-* closedness" is right. A non-closed convex hull of pure states with P̄(A) = 1 for every
non-null A has 𝒫^+ = ∅. By Thm 1.2 its weak-* closure must contain a full-support CA part.

*Standalone value.* Theorem 1.2 is a clean functional-analytic fact worth stating on its own: a weak-* compact convex set
of states on L^∞(μ) that charges every non-null set contains a state whose normal part is equivalent to μ.

---

## 2. §2: Theorem 2.1 and Corollary 2.3

### 2.1 Theorem 2.1

**(α).** N11 Cor 3.2(d), refereed CORRECT in N13, with (FS^c) now automatic.
- Lemma 3.1's splice needs one common carrier of the n pure parts. Lemma Y applied to Σ_iP_i^s gives it, atoms included.
- Lyapunov is used only for the integral coordinates.
- The push to int Δ uses the Lemma-IC model for proper S and ρ_{P_i} > 0 a.e.
- CORRECT.

**(β).** Re-derived. With a = min Σp_iψ_i (pointwise) and b = inf Σp_iπ_i(Λ_i·):
- X_m (A_m on Z_m, B off Z_m) has p·P(ΛX_m) → a + b;
- the selected C_m ⪯ X_m satisfy a ≤ p·ψ(C_m) ≤ p·P(ΛX_m) − b → a.
- (W) is used for the full members only.
- Compactness in measure of coherent models (CBOI lem:compact), closedness of M in measure and continuity of ψ in measure
  (integrable envelope) give a coherent ψ-p-Bayes C_∞ ∈ M.
- No charge infimum needs to be attained. Valid for every p ∈ Δ, boundary included.
- CORRECT.

**(γ).** Z := {(g,p) : two distinct kinds of advice in the advice range both minimise Σp_iρ_i(g)λ_i(g,·)} is jointly Borel: finite measurable
advice ranges and Carathéodory integrands. So E(P) = {p : μ(Z_p) > 0} is Borel, by Tonelli.
- For a.e. g and distinct a, b ∈ A(g), w := (ρ_i(λ_i(g,a) − λ_i(g,b)))_i ≠ 0. (A nonzero w suffices, not "all coordinates
  ≠ 0" as N13 wrote: {p ∈ aff Δ : p·w = 0} is empty if w ∝ 𝟙 and a hyperplane otherwise.)
- This uses the proviso that distinct kinds of advice differ in some world's rank a.e. That holds for advice ranges ⊆ {+,0,−,×}, whose
  background orders are strict at every world (BRIEF, on decomposable domains).
- Every ψ-p-Bayes model is a pointwise minimiser. Off E(P) it is therefore unique and equals the coherent C_∞ of (β).
- CORRECT.

**(δ).** CORRECT.

*Remark (referee).* (β), (γ) and (δ) use only (H) + (CP-a). Coverage enters only through (α). So E(P) and its
properties (and the criterion of §6.1) are invariants of **every** (CP-a) system satisfying (H).

### 2.2 Corollary 2.3: does it really follow from N15?

N15 Thm 7.1 (with N12.1's setting, and N20's repair) requires, for the field c on U:
- (R1) at **every** q ∈ int Δ: null tie set, and B_q = D_{K_q} a.e.;
- (R2) K_{p\*} = T;
- (LF).

N20 §8 shows that continuity of q ↦ K_q, the only regularity N15 uses, comes from (R1) holding at *every* q (N12
Prop 1.2). An a.e.-in-q version leaves "K_{p\*} = T" vacuous.

What Cor 2.3 uses is the contrapositive. Suppose E(P) = ∅. On M_U, put c_i(g) := ρ_i(g)(λ_i(g,0) − λ_i(g,+)). It has
the strict sign of g_i a.e. on U = N_i, because ρ_i > 0 there and λ_i is strictly rank-increasing. Then:
- the tie set of c is null at every interior q (E = ∅);
- the Bayes model there is a.e. unique (γ) and coherent (β), hence D_{K_q} (N12 Lemma 1.1);
- T1 is Bayes at p_T (α), hence the Bayes model at p_T;
- (LF) is a domain property of M, which ψ shares.

That is exactly (R1) + (R2) + (LF). Thm 7.1 (M_U) or Cor 7.2 (non-adjacent, via N14 §3(iv)) gives a contradiction.

So:
- **the argument is valid**;
- **E(P) ≠ ∅ is the correct conclusion**;
- **"outside a null set" is not enough** to invoke N15, and N22 does not claim it is.

The residual (U) is therefore genuine and correctly identified. Verdict: CORRECT.

---

## 3. §3: Lemma 3.0, Prop 3.3, Theorem 3.1, Corollary 3.2

**Lemma 3.0.** Pure terms are unchanged because |P_i^s((Λ_iX′ − Λ_iX)1_{Y∖F})| ≤ c P_i^s(H∖F) = 0. The strict CA gain on
Y∖F (μ ≥ μ(Y)/2) comes from the definition of Y; ρ_i > 0 is not even needed. CORRECT.

**Prop 3.3.**
- (i) Fact 0(a), (W), Lemma 3.0, then uniqueness off Z_p. CORRECT.
- (ii), coherence of attainers: p interior forces φ_i(C) = φ_i(B) for each i. Detection then gives C ~ B, and (C) gives
  B ∈ C_L. CORRECT.
- (ii), Z non-null: R = (Z∖F) ∩ {|g| < 1} can be null, since a tie set of a non-homogeneous field need not meet the unit
  ball.
  - **Repair:** choose r with μ((Z∖F) ∩ {|g| < r}) > 0. R2 Lemma U applies to any bounded non-null set, since a non-null
    cone mod null sets is unbounded.
  - With this, B′ attains (tied integral value, unchanged pure value), so B′ is coherent and B △ B′ = R is a bounded cone:
    contradiction.
  - CORRECT WITH REPAIR.

**Theorem 3.1.** Re-derived step by step.
- Step 1: selected C_m with φ(C_m) ≤ φ(X_m). Compactness gives q*, C_∞ (coherent) and z with p·z = I.
- Step 2:
  - ν_C is a finite atomless measure on H∖F, so φ_i(C) + [0, ν_C(H∖F)] ⊆ V_i. Splices stay in M, and the pure part
    is unchanged off F.
  - ν_{C_m}(H∖F) → ν_{C_∞}(H∖F) by convergence in measure of the (discrete) advice and dominated convergence.
  - That limit is positive: by (UN), C_∞ gives the world-i-best advice on U_+∖F (non-null), and ρ_i > 0 there.
  - Bookkeeping: for large m, ν_{C_m}(H∖F) > δ, which is all that is used.
- Step 3: completeness turns φ_i(C_{q_m}) < φ_i(X) into C_{q_m} ⪯_i X. (S)'s closed section gives q* ∈ A_i(X). One q*
  serves all i.
- Step 4: p·φ(C_{q*}) ≤ p·z = I.
- (b): coordinatewise equality, then representation, then (C); uniqueness by complementary splices and linearity of each
  P_i, then R2 Lemma U (window repair as above).
- (c): Prop 3.3(ii), since φ-ties are L-ties.
- CORRECT.

**Corollary 3.2.** CORRECT, with (UN) and non-adjacency as stated. The alternative route via N15 Cor 7.3 is also right:
by Lemma 3.0 the φ-minimiser at p_T is a pointwise ψ-minimiser, and p_T ∉ E, so it is T1.

*Significance (referee).* Complete (CP-a) worlds are exactly additive rankings with bounded charge penalties vanishing
on null sets. So Cor 3.2 **discharges the existence proviso of N15 Cor 7.3 / N14 Thm C2** for such rankings, using (S).
"Existence of interior Bayes minimisers for charges" was the open part-(A) item of N14 §5.1 and N15.9(b). For complete
rankings it is now closed, atoms included.

---

## 4. §4: Prop 4.1 and N22.5

- (i) 𝔉 is the range of a non-atomic vector measure, so it is compact and convex. It is not a point because w ≠ 0 a.e.
  on Z. With ≥ 3 tied kinds of advice on part of Z, use Lyapunov for measurable partitions; the conclusion is the same.
  CORRECT.
- (ii) CORRECT.
- (iii) "B′ is not a.e. a cone, so incoherent" is a non sequitur as written, since B′ is not itself a bounded set.
  - What is true: if B_0 and B′ were both coherent, B_0 △ B′ (bounded, non-null) would be a cone.
  - **Repair:** take B_0 to be the coherent Bayes model of (β), and use the radius-r window. Then B′ is incoherent, and the
    rest checks: Fact 0(a); ψ(C) = ψ(B′); C ≺_j B′ at some j by (C); then N11 Prop 1.1(ii).
  - CORRECT WITH REPAIR.
- N22.5: each bullet follows from the cited item. CORRECT.
- §4 "On proving (U)". The countable-t claim is right: for fixed p₀, a tie for P_t at g means t = t(g), and positive
  measure requires an atom of the push-forward. I did not verify the "two-valued directional support function" sketch;
  nothing depends on it.

---

## 5. §5: faithfulness of (CP-a) to Walley 1991

- **Thm 3.8.1 correspondence.** On a linear space 𝒦 of gambles containing constants:
  - coherent P̲ ↔ coherent almost-desirable classes D0–D4 (closed convex cones ⊇ non-negative gambles, with no uniformly
    negative gamble; §3.7.3) ↔ almost-preferences R0–R5 (§3.7.6), via X ≽ Y iff P̲(X − Y) ≥ 0;
  - with rewards −Λ_iX: X ⪯_i Y iff P̲_i(Λ_iY − Λ_iX) ≥ 0, as N22 writes.
  - Form (ii) additionally needs the lower-envelope theorem and weak-* compactness of 𝓜(P̲) (Walley 3.3.3, 3.6.1), not
    only §3.8.4. That is a citation repair.
- **Null-set reading.** The cleanest faithful statement, which I recommend for the paper:

  > *(CP-a) holds iff there is a Walley-coherent lower prevision P̲_i on the linear space of bounded measurable gambles
  > on H that is **null-invariant**: P̲_i(f) = P̲_i(f′) whenever f = f′ μ-a.e. Equivalently, P̄_i(1_N) = 0 for every
  > μ-null N. Equivalently, every P ∈ 𝓜(P̲_i) vanishes on null sets.*

  Proof:
  - A null-invariant coherent P̲ satisfies P̲(f) ≥ ess inf f. Modify f on a null set so that it is ≥ ess inf f
    everywhere.
  - So it descends to a coherent lower prevision on L^∞(μ), with D0/D1 read with ess sup/ess inf.
  - Conversely, composition with the quotient map is coherent (ess inf ≥ inf) and null-invariant.
  - Restricting Walley's gambles to measurable ones is coherence relative to a subspace (Thm 3.8.1 holds for any linear
    space containing constants). Natural extension recovers all gambles.

  So the "only modification" claim is right, and it is a restriction in Walley's own sense, not a change of axioms.
- **Relation on models only.** L ranks models, not all gambles. "⪯_i is the pull-back of a coherent ≽ on L^∞(μ)" is
  equivalent to Walley's coherence of the induced relation *relative to the set of model pairs* (§3.7.5 general
  definition, with §3.7.4(d)). Worth one sentence in the paper, since it shows (CP-a) is Walley's notion and not merely
  inspired by it.
- **Labels.** Walley 1991's D5 is "avoiding partial loss" (§3.7.8). Conglomerability is D5 of Walley **2000** (w2000.txt
  l. 594) and §6.8 of Walley 1991. Fix the parenthesis.
- **Excluded variants.** "(CP-s), (CP-b) with D = D⁺ inconsistent with (S) in the additive case" matches N13 Prop A
  (Case CA, strictly positive, two worlds with different ideals). For general M_i this is N13's CONJECTURE N13.A. Keep
  the qualifier.
- **Suggested theorem.**
  - (a) needs (UN). It holds on M_U, but it is not part of "non-adjacent".
  - (b) is a reduction; it should not be read as a no-go.
  - The "(LF) at T1" clause should name only the domain condition.

---

## 6. Referee additions: two reductions of (U)

### 6.1 Prop R1 (PROVED on M_U; CHECKED-level expectation for non-adjacent domains). (U) is a continuity property

**Setting.** Fix P ∈ ∏𝒫_i^+ and c as in §2.2. For q ∈ Ω∖E(P), let K_q be the unique credal set with B_q = D_{K_q} a.e.
(N12 Lemma 1.1).

**Claim.**
- (a) q ↦ K_q is Hausdorff-continuous on Ω∖E(P).
- (b) For p₀ ∈ Ω, p₀ ∉ E(P) iff K has a limit at p₀ along Ω∖E(P) (a dense set of full measure). In that case
  B_{p₀} = D_{K_{p₀}} a.e.

Hence E(P) is exactly the discontinuity set of the coherent Bayes family of ψ^P. And (U) holds iff some P admits a
Hausdorff-continuous coherent ψ^P-Bayes family on all of int Δ.

*Proof.*
- (a) This is N12 Prop 1.2's argument, which needs null ties only at the limit point: if q_n → q ∉ E, then
  1{q_n·c > 0} → 1{q·c > 0} off the null tie set of q.
- (b), "⇒": this is (a).
- (b), "⇐": let K_q → K₀ as q → p₀ in Ω∖E.
  1. J := {(g,q) ∈ U × (Ω∖E) : 1{q·c(g) > 0} ≠ 1{P_{K_q}(g) > 0}} is jointly measurable, since P_{K_q}(g) is
     Carathéodory on (Ω∖E) × U. Every q-section is μ-null, so J is null. For a.e. g the g-section is λ-null.
  2. Take such a g with g ∉ ∂D_{K₀}. This excludes a null set: a convex cone has Lebesgue-null boundary, and μ is
     absolutely continuous. Then P_{K_q}(g) → P_{K₀}(g) ≠ 0, since |P_K(g) − P_{K′}(g)| ≤ ‖g‖d_H(K,K′).
  3. So sign P_{K_q}(g) is constant for q ∈ V∖E, V a neighbourhood of p₀. Hence sign(q·c(g)) is constant for λ-a.e.
     q ∈ V.
  4. If p₀·c(g) = 0, then c(g) is not ∝ 𝟙 (else c(g) = 0, which is excluded by strict signs). So q ↦ q·c(g) takes both
     signs on positive-measure subsets of V. Contradiction.
  5. So Z_{p₀} ⊆ ∂D_{K₀} ∪ (null), which is null. And sign(p₀·c(g)) = sign P_{K₀}(g) a.e. ∎

*Reading.* N22's "jump line" and "fan" are exactly the two ways K can fail to extend: one-sided limits, and direction-
dependent limits. A cover must create such a discontinuity for **every** member choice. This puts (U) in the language
of (S), which forces the *selection's* profile to be continuous modulo ties (BRIEF "Known"). The missing link is the one
N22 §4.3 names: the ψ^P-Bayes family is not the selection. For the non-adjacent version, apply the same argument to
K̂_q = conv(K_q ∪ K′). I have not re-checked N14 §3(iv) for this use.

### 6.2 Prop R2 (PROVED). Under countable detection, (U) reduces to attainment

Assume (CD) at every world, e.g. each M_i weak-* separable: finitely generated, contained in CA, or the closed convex hull
of a norm-separable set (N11 Prop 5.1). Then:
- some P̂ ∈ ∏𝒫_i^+ detects every strict comparison: X ≺_i Y ⇒ P̂_i(Λ_iY − Λ_iX) > 0;
- E(P̂) ⊆ NA(P̂) := {p ∈ int Δ : inf_M p·φ^{P̂} is not attained}.

Consequently, on a non-adjacent domain, **(CD) + attainment of the single charge field φ^{P̂} at every interior weight ⇒
T1 is not covered.**

*Proof.*
1. Let {P_{i,k}} be the (CD) family and P_i^+ ∈ 𝒫_i^+ (Thm 1.2). Put P̂_i := ½Σ_k2^{−k}P_{i,k} + ½P_i^+. It lies in M_i
   (normalised partial sums, norm-closedness) and in 𝒫_i^+ (mixture stability).
2. If X ≺_i Y, every member gives f ≥ 0 and some P_{i,k}(f) > 0, so P̂_i(f) > 0.
3. Hence the detection hypothesis of Prop 3.3(ii) holds at every weight. Prop 3.3(ii) then gives p ∉ E(P̂) wherever
   φ^{P̂} attains.
4. Apply Cor 2.3. ∎

*Reading.*
- Under (CD), detection disappears entirely. What remains is gap (2), attainment, but only as a sufficient route to (U).
- Without (CD), as in N11 Prop 5.2, both detection and attainment remain.
- Case CA is the sub-case in which attainment is automatic.

---

## 7. What is now proved for coherent-almost-preference rankings

Standing assumptions:
- (H): decomposable domain (a class of evaluable models closed under splicing and in measure) with advice ranges ⊆ {+,0,−,×}; strict (G), (IB), (LA), (S), (C);
- μ finite and atomless (Gaussian-equivalent);
- T1 = D_K, K = (1−ε)u + εΔ, any ε ∈ (0,1);
- the (LF) domain clause at T1;
- each world i is a coherent almost-preference over losses (CP-a): penalties λ_i bounded, measurable and strictly
  rank-increasing, and a null-invariant Walley-coherent P̲_i, equivalently a weak-* compact convex credal set M_i of
  finitely additive probabilities vanishing on null sets.

On a non-adjacent decomposable domain (e.g. the U-domain M_U, whose evaluable models are the measurable subsets of U = D_{K′}):

1. **(Complete worlds, PROVED.)** If every M_i is a singleton, and (UN) holds (true on M_U), then **T1 ∉ C_L**. The
   member states are arbitrary: purely finitely additive and atomic parts are allowed. Equivalently, no additive
   ranking with bounded charge penalties covers T1. The existence proviso of N15 Cor 7.3 is discharged by (S).
2. **(Countably additive detection, PROVED.)** If (D^CA) holds (each strict comparison is detected by a CA member, e.g.
   all members CA, or M_i the weak-* closure of its CA members), then T1 ∉ C_L (N11 Thm 2.1 + Cor 2.3's argument).
3. **(General (CP-a), PROVED reduction.)** If T1 ∈ C_L, then 𝒫_i^+ ≠ ∅ for every i. For **every** P ∈ ∏𝒫_i^+, the
   integral field ψ^P_i = ∫λ_iρ_{P_i}dμ is strictly guiding on M, and:
   - T1 is ψ^P-Bayes at an interior weight;
   - there is a coherent ψ^P-Bayes model at every weight;
   - the vertex models are coherent;
   - E(P) is Lebesgue-null and **non-empty**;
   - E(P) is exactly the discontinuity set of the coherent Bayes family (Prop R1, M_U).

   At each p₀ ∈ E(P), either the charge field φ^P fails to attain, or a strict comparison between two of its attaining
   models is invisible to P (Prop 3.3). If P is countably additive, the p₀-face of Bayes profiles has dimension ≥ 1, is
   realised by selected models, and carries an undetected strict comparison (Prop 4.1).
4. **(Countable detection, PROVED.)** Under (CD), a cover forces non-attainment of one detecting charge field φ^{P̂} at
   some interior weight (Prop R2).

**Not proved.** (U) in general (CONJ N22.U). Equivalently:
- that the integral Bayes family of some member choice extends continuously; or
- under (CD), attainment of φ^{P̂} at every interior weight. This is OPEN even for finitely generated incomplete M_i.

Also outside the result: the Walley-2000 variant with invisible desirability, (CP-s) (which is near-inconsistent with
(S)), adjacent domains, and n > 3.

**Recommended statement for the paper:**

> *Theorem.* On a non-adjacent decomposable domain satisfying (UN), under (H) with (LF) at T1, if every world's ranking is a
> complete coherent almost-preference over losses, or if strict comparisons are detected by countably additive members,
> then T1 ∉ C_L. In general, a cover forces every full-support member choice to yield an integral field whose coherent
> Bayes family is discontinuous at some interior weight.
