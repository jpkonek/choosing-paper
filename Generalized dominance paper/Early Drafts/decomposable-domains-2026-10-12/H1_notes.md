# H1. Holonomy in the compatibility of endorsing weights with one non-adding-up world: failure report, and the obstruction as a theorem (localization)

15 Oct 2026, round 17 (BRIEF15; BRIEF13 rules). Labels: **PROVED** (full proof here, from results the write-up marks
proved), **CHECKED**, **CONJECTURE**, **NUMERICS** (scripts in `h1py/`, run with `python3 -I`; no proof depends on
them). No assumption is added. Setting and notation: write-up §§2–3, §7.7, §8.5 "Notation"; E1_notes §1–§2.1; F2_notes
§1.1. So n = 3, ε ∈ (0,1), K′ = u + s(T1 − u), U = D_{K′}, M_U, P_i, E_i(X) = X △ P_i, M (mixed part of U), N₊, R_ij,
σ_i = sign h_i, and (H_U) = strict (G), (IB), (LA), (S) (selection p ↦ C_p), (C), T1 ∈ C_L.

---

## 0. Outcome

**No cover was constructed. The route closes before any selection is chosen, by a theorem.**

**Where it broke.** Step (2) of the brief asks for base endorsing families G_i with *no* admissible tuple in ∏G_i,
even after end reweighting. That cannot happen. Admissibility of every tuple of (localized) endorsers is automatic: it
follows from competitiveness of T1 alone (Lemma H1.1). Even with an admissible tuple, the M0closed argument then goes
through without any heaviness at the ends (Theorem H1.2). So the brief's WARNING (end-light bases) is moot. An
end-light base is excluded outright, with no collapse argument needed.

**The single obstruction (Theorem H1.2, PROVED): failures of adding up that can be localized are invisible.**
- **Hypotheses.**
  - Two worlds add up with integrable densities.
  - The third world has a density that is positive and finite a.e. (σ-finite, not necessarily integrable).
  - That density endorses, in the cancellation sense, every relevant comparison of the third world whose vector is
    ≤ 0 on some member of a vanishing family of sets D_m (μ(D_m) → 0).
- **Conclusion.** (H_U) is contradictory: no cover.
- **Mechanism (Lemma H1.0).**
  - At an incoherent Bayes weight t, every coherent model is a fixed positive cost d_t above the Bayes minimum.
  - A regular model X_m that copies the Bayes model except on D_m, where it is made correct at the exceptional world,
    costs at most ∫_{D_m}(ρ_j + ρ_k) → 0 more than the minimum.
  - Its KKM dominator compares into X_m by localized comparisons only. Endorsement would put a coherent model within
    that cost of the minimum.

**Consequences.**
1. **E1.5 holds without (h).** It needs no end-heaviness, no end-protection structure and no location of the ends. An
   end-protected world whose base has *any* integrable (indeed any a.e.-finite) endorser cannot be the exceptional
   world of a cover next to two worlds that add up integrably. This holds at near-unanimous ends and at
   ∂U ∩ {h_i < 0}, whether the base is end-heavy or end-light (Corollary H1.4).
2. **Several exceptional worlds (Theorem H1.3, PROVED).** The same exclusion holds when every world has an integrable
   localized endorser and the localizing sets are T1-correct at their worlds. These are automatically compatible
   across worlds. So E1.5 holds with (h) replaced by "each end is eventually T1-correct at its world", which is
   automatic at ∂U ∩ {h_i < 0} (F2.1).
3. **F2's "nearby reachable CONJECTURE"** (E1.1(c)/E1.5 for shadows finite a.e. and integrable off deep ends) is
   **PROVED** for one exceptional world, with a Lyapunov-free admissibility step. A world that adds up σ-finitely in
   the cancellation sense (as D2's world 1 does in two worlds, Prop. D2sigma) cannot be the exceptional world of a
   cover.

**Answers to the brief's steps.**
- **(1) WARNING.** The dichotomy is proved, and it is not about collapse.
  - (a) If the protected world's base has an a.e.-finite endorser of its localized comparisons, the system is
    excluded. End-light or not, no collapse is needed.
  - (b) Otherwise the base itself fails to add up, and it does so *non-locally*. Then the protection carries none of
    the failure that a cover needs.

  The core must therefore be a world whose comparisons, after deleting every comparison that adds errors on some set
  of arbitrarily small measure, still admit no a.e.-finite endorsing density.
- **(2)** The target "no admissible tuple in ∏G_i" is impossible whenever every G_i ≠ ∅ (Lemma H1.1).
- **(3), (4)** were not reached.

**What survives (the proposed shift of aim, §6).** Exactly one of the following.
- **(A) Non-localizable failure at one world.** No a.e.-finite density endorses its D-localized relevant comparisons,
  for any vanishing family D.
- **(B) Mutual sheltering.** Two exceptional worlds i, j, with an end of world i on which T1 errs at world i at every
  depth, inside R_ij, sheltered by world j's protected set.
- **(C) Purely finitely additive endorsers** at the other worlds, which (CP-a) worlds with singular parts can have.

D2-type protection survives only in (B).

---

## 1. Definitions

- **Densities.** ρ = (ρ₁, ρ₂, ρ₃), each measurable on U with 0 < ρ_k < ∞ a.e. Field c_k := ρ_kσ_k. Bayes sets
  B_t := {g ∈ U : t·c(g) > 0}, tie sets Z_t := {t·c = 0}. **Admissible**: D_{T1} = B_{p*} ∪ S with S ⊆ Z_{p*} for some
  p* ∈ Δ°. Put I_ρ := {t ∈ Δ° : Z_t null, B_t incoherent}.
- **Endorsement.** For a world-k comparison C ⪯_k X with vector δ := 1_{E_kX} − 1_{E_kC}:
  - (E2), cancellation: ρ_kμ(δ⁻) ≤ ρ_kμ(δ⁺) in [0,∞];
  - (E1), total cost: ρ_kμ(E_kC) ≤ ρ_kμ(E_kX).

  Both have property (R) of F1 §2.1: if ρ_kμ(E_kX) < ∞, endorsement gives ρ_kμ(E_kC) ≤ ρ_kμ(E_kX) with both finite.
  For integrable ρ_k the two readings coincide.
- **Localizing family.** A decreasing sequence D_m ⊆ M of measurable sets with μ(D_m) → 0.
  - A world-k comparison is **D-localized** if δ ≤ 0 a.e. on D_m for some m. This says that X makes no world-k error on
    D_m that C does not make.
  - It is **(D, T1)-localized** if δ ≤ 0 a.e. on D_m ∩ {T1 is correct at world k} for some m.
- **Ends.** If world k is end-protected with a countable family 𝒮_k (E1 §2.1), choose depths a_S(m) ↑ ∞ with
  Σ_S μ(S_{a_S(m)}) → 0, and put D_m := ⋃_{S∈𝒮_k} S_{a_S(m)}.
  - A D-localized relevant comparison is S-positive for no S, since δ ≤ 0 on S_{a_S(m)}.
  - So it is a **base** comparison (F2 §1.1). Hence **base endorsement implies D-localized endorsement.** Localized
    hypotheses are weaker than E1.5's (b).

---

## 2. The stability lemma

**Lemma H1.0 (PROVED).** Let ρ be as in §1 and t ∈ I_ρ. For a model Y put
Φ(Y) := ∫_{Y △ B_t} |t·c| dμ ∈ [0, ∞], and d_t := inf{Φ(C) : C ∈ M_U coherent}.
- **(a)** d_t > 0.
- **(b)** If Y, Y′ are regular and ρ_kμ(E_kY), ρ_kμ(E_kY′) < ∞ for every k, then
  Φ(Y) − Φ(Y′) = Σ_k t_k[ρ_kμ(E_kY) − ρ_kμ(E_kY′)], all terms finite.
- **(c)** Let X be regular with Φ(X) < d_t and ρ_kμ(E_kX) < ∞ for all k, and let C be coherent with C ⪯_k X for every
  k. Then some world k does not endorse C ⪯_k X.

*Proof.*
- **(a)**
  - *Compactness.* A coherent model of M_U is D_K a.e. with K ⊇ K′ (write-up Prop. reduction (a)). Given coherent
    D_{K_n}, pass to a Hausdorff-convergent subsequence K_n → K. Then P_{K_n}(g) → P_K(g) for every g, so
    1_{D_{K_n}} → 1_{D_K} off {P_K = 0} ∪ {g ≥ 0}. The set {P_K = 0} is the boundary of a convex cone with interior,
    hence null. Since μ is finite, D_{K_n} → D_K in measure. So the coherent models form a compact set for convergence
    in measure (R1 Prop. 3.1).
  - *Lower semicontinuity.* If Y_n → Y in measure, pass to a subsequence that attains liminf Φ(Y_n) and converges a.e.
    Fatou gives Φ(Y) ≤ liminf Φ(Y_n).
  - Hence the infimum is attained at some coherent C*. Since t ∈ I_ρ, C* ≠ B_t (B_t is incoherent), so C* △ B_t is
    non-null. As |t·c| > 0 a.e. (Z_t null), Φ(C*) > 0.
- **(b)** For regular Y, 1_{E_kY} = 1_Y on {σ_k < 0} and 1 − 1_Y on {σ_k > 0}. So
  1_{E_kY} − 1_{E_kY′} = σ_k(1_{Y′} − 1_Y) and Σ_k t_kρ_k(1_{E_kY} − 1_{E_kY′}) = (1_{Y′} − 1_Y)·t·c.
  - Pointwise, (1_{Y△B_t} − 1_{Y′△B_t})|t·c| = (1_{Y′} − 1_Y)·t·c: check t·c > 0 and t·c < 0 separately.
  - Both sides vanish off Y △ Y′ ⊆ ⋃_k(E_kY ∪ E_kY′), where every ρ_k has finite mass, and |t·c| ≤ Σt_kρ_k.
  - So everything is integrable, and integrating gives (b).
- **(c)** Suppose every C ⪯_k X is endorsed. By (R), ρ_kμ(E_kC) ≤ ρ_kμ(E_kX) < ∞ for all k. By (b),
  Φ(C) − Φ(X) ≤ 0, so Φ(C) ≤ Φ(X) < d_t ≤ Φ(C), a contradiction. ∎

This is E1.1(b) made robust. E1.1(b) says that dominator comparisons into the Bayes model B_t itself are unendorsed.
H1.0 says the same for every regular model within d_t of the Bayes cost. Such models can be made *correct on any
prescribed set of small measure*. Protection lives on such sets, which is why it cannot be what produces the failures.

---

## 3. Admissibility is automatic (the compatibility of endorsing weights is never violated)

**Lemma H1.1 (PROVED).** Assume (H_U). Let ρ be as in §1 and D_m a localizing family such that every ρ_k is
integrable on M ∖ D_m for every m. Suppose that for each world k, ρ_kμ endorses in the cancellation sense (E2) every
comparison T1 ⪯_k Y with Y regular and Y = T1 a.e. on some D_m. Then ρ is admissible.

*Proof.* Let v_k(g) := ρ_k(g) if T1 is correct at world k at g, and −ρ_k(g) otherwise (g ∈ M). Toggling the advice of
T1 on a set A ⊆ M changes the world-k error mass by ∫_A v_k.

1. **No strict Pareto improvement off D_m.**
   - Fix m, and suppose some A ⊆ M ∖ D_m has ∫_A v_k < 0 for k = 1, 2, 3. Put Y := T1 △ A. Y is regular and equals
     T1 on D_m.
   - T1 ∈ C_L is undominated. By Theorem kkm it is tied at every world with some selected C_p, which is competitive on
     supp p. So C_p ⪯_k Y for some k, and T1 ⪯_k Y by transitivity.
   - Its vector δ = 1_{E_kY} − 1_{E_kT1} is +1 where T1 is correct and −1 where T1 errs, on A. Endorsement (E2) gives
     ρ_kμ(δ⁻) ≤ ρ_kμ(δ⁺), both finite since A ⊆ M ∖ D_m, i.e. ∫_A v_k ≥ 0. This is a contradiction.
2. **A supporting weight at level m.**
   - v is integrable on M ∖ D_m and μ is non-atomic. By Lyapunov, R_m := {∫_A v dμ : A ⊆ M ∖ D_m} is compact and
     convex. It contains 0 and, by step 1, misses the open convex cone −int ℝ³₊.
   - Separation gives p^{(m)} ∈ Δ with p^{(m)}·y ≥ 0 on R_m. Hence p^{(m)}·v ≥ 0 a.e. on M ∖ D_m.
3. **Limit.**
   - Take p^{(m)} → p* along a subsequence. For fixed m, every later p^{(m′)} satisfies p^{(m′)}·v ≥ 0 a.e. on
     M ∖ D_m ⊆ M ∖ D_{m′}, so p*·v ≥ 0 a.e. on M ∖ D_m.
   - As μ(⋂D_m) = 0, p*·v ≥ 0 a.e. on M. On N₊, v_k = ρ_k > 0 a.e. at every world.
4. **Interior.**
   - Suppose p*₃ = 0. The set D_{T1} ∩ {(−,−,+)} is non-null: it contains a neighbourhood of a point just inside
     D_{T1} near r₁₂. There T1 accepts, so v = (−ρ₁, −ρ₂, ρ₃) and p*·v = −p*₁ρ₁ − p*₂ρ₂ < 0 a.e. This contradicts step 3.
   - The cyclic cases are the same.
5. **Admissible.** On D_{T1}, v = c; off it, v = −c. Step 3 gives p*·c ≥ 0 on D_{T1} and ≤ 0 off it, a.e. So
   B_{p*} ⊆ D_{T1} and D_{T1} ∖ B_{p*} ⊆ Z_{p*}. ∎

*Remarks.*
- Only T1's own out-comparisons are used, and only those that leave a small set untouched.
- For integrable ρ and D_m = ∅ this is N17 Prop. 2.1(α) (Prop. M0 (α)). For ends and base endorsers it is E1.5
  step 1.
- The truncation to M ∖ D_m removes the Lyapunov obstacle for non-integrable densities that F2 §4.3 named as missing.
- **Consequence for step (2) of the brief (PROVED).** If every world is end-protected with countably many ends
  (possibly none), and every world's base has an endorser that is integrable, or merely a.e. finite with (E2), then
  **every** tuple in ∏G_i is admissible. Take D_m as in §1 together with {ρ_k > m} ∩ M. Then
  Y = T1 on D_m makes T1 ⪯_k Y a base comparison. So the brief's design target is unattainable whenever every G_i is
  nonempty.

---

## 4. The theorems

**Theorem H1.2 (one exceptional world; PROVED).** Assume (H_U). Suppose:
- worlds 2 and 3 have integrable densities ρ₂, ρ₃ > 0 a.e. that endorse all their relevant comparisons;
- world 1 has a measurable ρ₁ with 0 < ρ₁ < ∞ a.e.;
- there is a localizing family D_m (possibly D_m = ∅);
- ρ₁μ endorses, in the cancellation sense, every D-localized relevant comparison of world 1.

Then (H_U) is contradictory. Under the total-cost reading (E1) the same holds if ρ₁μ(E₁T1) < ∞.

*Proof.*
- **Setup.** Put D′_m := (D_m ∪ {ρ₁ > m}) ∩ M, a localizing family, with ρ₁ ≤ m on M ∖ D′_m. A D′-localized
  comparison is D-localized, so ρ₁ endorses it. Worlds 2 and 3 endorse everything relevant.
- **Admissibility.**
  - Lemma H1.1 applies with D′: comparisons T1 ⪯_k Y with Y = T1 on D′_m are relevant, and for k = 1 they are
    D′-localized.
  - Under (E1) with ρ₁μ(E₁T1) < ∞, the costs in step 1 of H1.1 are finite. (E1) then gives the same inequality.
- **A weight in I_ρ.** The field c = ρσ is strictly signed and measurable. If I_ρ were null, B_t would be coherent for
  a.e. t ∈ Δ°: Z_t is null for a.e. t by Tonelli, since each {t : t·c(g) = 0} is a line. That is property (γ). With
  admissibility, Theorem M0closed(a) excludes it, and M0closed(a) uses no integrability (its status). So pick
  t ∈ I_ρ.
- **Near-Bayes, localized models.**
  - Let X_m := B_t on U ∖ D′_m, and on D′_m let X_m be world-1-correct: accept where h₁ > 0, reject where h₁ < 0. X_m is
    regular, because D′_m ⊆ M and B_t ⊇ N₊ a.e.
  - Where B_t errs at world 1, sign(t·c) = −σ₁, so |t·c| = −σ₁t·c ≤ t₂ρ₂ + t₃ρ₃.
  - Hence Φ(X_m) ≤ ∫_{D′_m}(ρ₂ + ρ₃) dμ → 0, by absolute continuity.
  - Costs: E₁X_m ⊆ M ∖ D′_m, so ρ₁μ(E₁X_m) ≤ m·μ(M) < ∞; worlds 2 and 3 are integrable.
- **Dominators.**
  - Theorem kkm gives a selected undominated, hence coherent, C_m with C_m ⪯_k X_m for every k. All three comparisons
    are relevant.
  - The world-1 comparison has δ = 1_{E₁X_m} − 1_{E₁C_m} ≤ 0 on D′_m, since X_m is correct there. So it is
    D′-localized and endorsed.
  - Worlds 2 and 3 endorse theirs.
  - Lemma H1.0(c) is contradicted as soon as Φ(X_m) < d_t. ∎

**Theorem H1.3 (several exceptional worlds; PROVED).** Assume (H_U). Suppose there are integrable ρ_k > 0 a.e. and
localizing families (D^k_m)_m, k = 1, 2, 3 (each possibly empty), such that ρ_kμ endorses every (D^k, T1)-localized
relevant comparison of world k. Then (H_U) is contradictory. The same holds with "D^k-localized" in place of
"(D^k, T1)-localized", provided D^i_m ∩ D^j_m ∩ R_ij is null for all i ≠ j and all m.

*Proof.*
- **Admissibility.** Put D_m := ⋃_k D^k_m. Comparisons T1 ⪯_k Y with Y = T1 on D_m have δ = 0 on D_m and are
  localized in either sense, so Lemma H1.1 applies.
- **A weight in I_ρ.** Take t ∈ I_ρ as before.
- **First version.** Let X_m := B_t off D_m and T1 on D_m.
  - On D^k_m ∩ {T1 correct at k}, X_m is correct at k. So every C ⪯_k X_m has δ ≤ 0 there and is (D^k, T1)-localized.
  - Φ(X_m) ≤ Σ_k ∫_{D_m}ρ_k → 0, and all costs are finite (integrable ρ). Conclude by Lemma H1.0(c).
- **Second version.** On D^k_m make X_m correct at world k. This is consistent: two worlds disagree only on R_ij, which
  the hypothesis excludes, and off R_ij correctness at i and at j is the same advice. Then argue as before. ∎

*Remarks on scope.*
- **T1-correct localizing sets.** If D^k_m ⊆ {T1 correct at k}, the two notions of localization coincide. Such sets
  are automatically R_ij-compatible, because T1 is correct at exactly one of i, j on R_ij.
  - Ends eventually T1-correct at their world can be cut to such D^k_m.
  - This is automatic at ∂U ∩ {h_k < 0} (F2.1).
  - It is forced under the hypotheses of E1.3(a).
  - It holds under E1.5's (h): with (h), T1 = B_{p*} up to ties is world-k-correct deep in the ends.

  So **E1.5 holds with (h) replaced by T1-correctness of the ends**, and with base endorsement weakened to localized
  endorsement.
- **Integrability in H1.3.** It is used for Φ(X_m) → 0 when X_m errs at a world whose density is non-integrable on
  D_m. A σ-finite version for two or more worlds is not proved.

---

## 5. Consequences for route H1 (and for D2-type worlds)

**Corollary H1.4 (PROVED).** Assume (H_U), with worlds j and k having integrable endorsing densities (for instance
additive with integral penalties, or adding up with countably additive weights, or with leading densities, B1.0).
Then world i is not:
- **(a)** an end-protected world, with countably many ends anywhere and of any heaviness, whose base has an integrable
  endorser, or an a.e.-finite one in the cancellation sense. Base endorsement implies D-localized endorsement (§1).
- **(b)** a world with an a.e.-finite (E2)-endorser of all its relevant comparisons, i.e. a world that adds up
  σ-finitely. Take D = ∅. In particular, a three-world installation of a world behaving like D2's world 1 is excluded
  as soon as it keeps an a.e.-finite (E2)-endorser. In two worlds that world has one: Prop. D2sigma's φ(x)λ endorses
  in the (E2) sense, with δ⁻ integrable on c_b. F1.2 shows that all its σ-finite endorsers are of this monotone form.

*Proof.* Theorem H1.2. ∎

**The brief's WARNING, settled (PROVED).** Let world i be "base + protected generators" next to j, k as in H1.4.
- **(a)** If the base has an a.e.-finite (E2)-endorser of its localized comparisons, then there is no cover. This
  holds for end-heavy and end-light bases alike, and whatever the core: additive, incomplete or non-additive. No
  collapse argument enters. Admissibility comes from T1's competitiveness (H1.1), and invisibility from H1.0.
- **(b)** Otherwise, for every localizing family D containing the deep ends, the D-localized comparisons, all of which
  are base comparisons, have no a.e.-finite endorser. Then the failure that a cover needs is a failure of the base on
  comparisons that add no errors on an arbitrarily small set. Deleting the generators leaves it intact.

Whether an end-light base can coexist with generators without collapse was not decided. It is irrelevant to covers.

**Holonomy dominators.**
- In the brief's terms, what the cover needs against the holonomy (L3) is, for *every* admissible ν and t ∈ I_ν, an
  unendorsed comparison into every regular model within d_t of the Bayes cost (H1.0).
- Such models can be chosen to agree with the Bayes model off any set of small measure and to be correct on it.
- So the needed failures cannot be located on any vanishing set, at any world whose density is integrable off it.

**Relation to earlier results.**
- **E1.5.** Superseded: no (h), no end-protection, no location, σ-finite at one world.
- **F2 (R-a).** Closed in its integrable and a.e.-finite (E2) sub-cases.
- **F2 §4.3 "nearby reachable CONJECTURE".** PROVED for one exceptional world (H1.2). The "Lyapunov-free admissibility
  step" is the truncation in H1.1.
- **L5 open item "a protected world whose base has no such density".** Narrowed to: no a.e.-finite density endorses
  its D-localized comparisons, for any vanishing D.

---

## 6. What survives: the shift of aim

By H1.2 and H1.3, a cover of T1 on M_U needs one of the following.

- **(A) Non-localizable failure.**
  - *Statement.* Some world i is such that, for every localizing family D and every a.e.-finite positive ρ_i, some
    D-localized relevant comparison of world i is not ρ_i-endorsed (E2). The other two worlds are integrable.
  - *What this rules out.* Every failure that can be pushed into comparisons charging an arbitrarily small set: D2
    generators, ratio certificates with targets at ends, and atoms at single rays.
  - *What is left.* What remains is a failure carried by comparisons that leave every small set alone: an (M1)
    obstruction, or an (M2) family whose sources *and* targets have measure bounded below on a fixed core.
  - *Two-world evidence (F1.4).* In two worlds next to an additive world, no D2-type certificate has sources and targets
    in a core c_{b₀}. That evidence points against (A), but the three-world case is open.
- **(B) Mutual sheltering.**
  - *Statement.* Two exceptional worlds i, j, whose localizations cannot be made T1-correct: an end of world i on which
    T1 errs at world i at every depth, inside R_ij, contained in the protected set of world j.
  - *Why H1.0 does not apply.* On such a set no single regular model is correct at both i and j, and the copy of T1
    errs at i there. So H1.0 cannot be applied with comparisons that are localized at both worlds.
  - *Why E1.3(a) does not apply.* Its argument needs worlds j, k to endorse T1's out-comparisons, and world j's
    protection can absorb those.
  - *Status.* This is the only place where D2-type protection is not excluded by H1.2 and H1.3. On the edge e_ij it is a
    two-world system with **both** worlds protected on a common region of R_ij.
  - *Proposed next target (CONJECTURE: neither direction is claimed).* A full two-world system on M_U in which both
    worlds are end-protected with interpenetrating ends. If no such system exists, (B) is empty and only (A) and (C)
    remain.
- **(C) Finitely additive endorsers at the other worlds.** H1.2 and H1.3 use integrable densities at the non-exceptional
  worlds. Worlds that add up only with purely finitely additive weights, such as (CP-a) worlds with singular parts
  (CPaU (b)), are not covered here.

---

## 7. NUMERICS (`h1py/`, `python3 -I`; illustrative)

**`h1_localization.py` (+ `.out`).** Setting: ε = 0.3, s = 0.9, shadow ν^L with L = 5 (Prop. Q31), 524 976 Monte
Carlo samples in U. At t = (0.45, 0.45, 0.10) and t = (0.15, 0.15, 0.70):
- **B_t is incoherent.** 62 and 135 midpoints of accepted pairs are rejected, so B_t is not convex.
- **Localized correction.** X_m is made world-1-correct on the ∂U-collar D_m = {P_{K′}(h) < 2^{−m}|h|} ∩ {h₁ < 0}:

  | m | Φ(X_m), t = (0.45, 0.45, 0.10) | Φ(X_m), t = (0.15, 0.15, 0.70) |
  |---|---|---|
  | 2 | 1.2·10⁻¹ | 2.2·10⁻¹ |
  | 4 | 2.3·10⁻² | 4.3·10⁻² |
  | 6 | 1.5·10⁻⁴ | 6.0·10⁻⁴ |
  | 8 | 0 | 7·10⁻⁵ |
  | 10 | 0 | 1.7·10⁻⁵ |

- **Coherent models.** The best Φ among 1505 random coherent D_K, with local refinement, is 5.3·10⁻³ and 2.6·10⁻³.
  This is only an upper estimate of d_t; d_t > 0 is proved in H1.0(a).
- At t = (0.03, 0.03, 0.94), B_t turned out to be coherent (the vertex model), so that t ∉ I_ν. This is consistent
  with Prop. Q32: I_ν avoids Q_L but need not contain the vertex corners.

**`h1_scan.py`.** The midpoint-convexity scan used to locate incoherent weights.

## 8. Dependencies

- Theorem kkm (Loss Dominance Generalized v2; proved).
- Theorem M0closed(a) (proved; new parts refereed twice; uses no integrability).
- Lyapunov's convexity theorem.
- Hausdorff compactness of credal sets and R1 Prop. 3.1 (convergence in measure of D_K).
- Write-up Prop. reduction (a) (coherent models of M_U have K ⊇ K′).
- F2.1 (∂U-collar ends are T1-correct; used only in remarks).
- **Not used:** E1.3, E1.4, (h), Lemma vectorform, any edge result, (Nest_e), (C) beyond (H_U).
- Not yet refereed.
