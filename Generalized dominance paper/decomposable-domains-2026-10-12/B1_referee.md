# Referee report on B1_notes.md (round 14): edge leading densities and the link class

15 Oct 2026. Checked against writeup/"The Contamination Triangle.tex": §2.1 (models, advice, background order),
§2.5 (U-domain), §2.6 (error encoding E_i(X) = X △ P_i), §2.7 (regular models, relevant comparisons, Def. addup,
(M0)/(M1)/(M2)), §7.7 (Theorem M0closed, Cor. M0closed, Cor. CPaU), §8.5 "Notation" (P_i, M, N_+, R_ij, (H_U)),
Lemma Q34, the definition of a leading charge, Theorem S21 and its proof sketch, Theorem Q36, Corollary Q37.
Scripts: `b1py/` rerun with `python3 -I`; independent checks in `b1ref_py/ref_checks.py` (+ `.out`).

## Summary of verdicts

| Item | Verdict |
|---|---|
| (i) R_ij = Q_i ∪ Q_j, R_ij ∩ R_ik = Q_i, Q_l non-null | **CORRECT** (one cosmetic fix) |
| (ii) Lemma B1.0 | **CORRECT** |
| (ii) Lemma B1.1 (gluing) | **CORRECT** |
| (iii) Lemma B1.2 (transfer chain), both cases | **CORRECT** (one sentence to add: common m) |
| (iv) Theorem B1.3, and "adds up" in the write-up's sense | **CORRECT** |
| (v) Corollary B1.4 (at the status of M0closed(b)) | **CORRECT** |
| (v) "Strengthening" via S21 | **CORRECT at CHECKED** (one sentence to add) |
| (vi) Corollary B1.5(a) | **GAP (fixable)**: the strictness in "X ≺_i C" is not given by the first claim of B1.3 |
| (vi) Corollary B1.5(b) | **CORRECT but too weak**: it models "agree" as equality of measures; the ordinal version is needed and holds |
| §0 headline sentence | **WRONG as stated** (true under the hypothesis of B1.3, which is all that is used) |
| Scripts | Reproduce exactly |

Nothing in the mathematical core is wrong. The new content (B1.1 + B1.2 ⇒ B1.3) is sound and is a real
strengthening of Cor. Q37's contrapositive: a world of a cover must already fail to have a leading density on a
**single** edge region, not just on M.

---

## (i) Edge regions and sign classes — CORRECT

- Write-up §8.5: R_ij := {h ∈ U : h_i h_j < 0}, M = mixed gambles of U, N_+ = nonnegative gambles of U, and
  U = M ∪ N_+ mod null. U contains no nonzero h ≤ 0 (K′ ⊆ Δ°), so no all-negative gambles.
- Off coordinate planes, a mixed h ∈ ℝ³ has exactly one coordinate l whose sign differs from the other two, so
  h ∈ Q_l for exactly one l. Then h_i h_j < 0 holds iff the odd coordinate is i or j. So R_ij = Q_i ∪ Q_j, and
  R_ij ∩ R_ik = Q_i ∪ (Q_j ∩ Q_k) = Q_i.
- Non-nullity. r_23 = (κ+1, −1, −1) has pattern (+,−,−), so it is in Q_1. Likewise r_31 ∈ Q_2 and r_12 ∈ Q_3. Each lies
  in cl D_{T1} ∖ 0 ⊆ U, and U is open, so a neighbourhood of each ray lies in U and keeps the same strict pattern.
  This agrees with the write-up's linking sentence (proof of S21 / Q36): e_i − η(e_j + e_k) ∈ Q_i.
- NUMERICS (`ref_checks.py` §1, ε = 0.3, s = 0.9, 3·10⁵ Gaussian samples): every identity holds sample by sample.
  Each Q_l has about 21.5 % of the U-mass. The corner rays lie in U and on ∂D_{T1}.
- *Cosmetic fix.* Line 11: "M = Q_1 ∪ Q_2 ∪ Q_3 (disjoint up to null sets)" → "the Q_l are pairwise disjoint and
  their union is M up to the null coordinate planes".

## (ii) Lemma B1.0 — CORRECT

All steps check.

- **The set S ∖ E_iZ is non-null.** If S ⊆ E_iZ a.e., then E_iY ∖ E_iZ ⊆ (Y △ Z) ∖ E_iZ ⊆ S ∖ E_iZ, which is null,
  so g ≤ 0.
- **Strict (G) gives Z ≺_i Z′.** Z′ = Z △ e with e ⊆ S ∖ E_iZ. On e, Z is correct and Z′ errs. In U, error is
  strictly worse in the background order: if h_i > 0, no advice is worse than good; if h_i < 0, bad is worse than no
  advice. Elsewhere the two models agree.
- **Z′ is regular and in M_U.** e ⊆ M, so Z′ still accepts N_+, and Z′ ⊆ U.
- **The bound ≥ g − 2ρ(e).** Moving e into E_iZ lowers ρ(E_iY ∖ ·) by at most ρ(e) and raises ρ(· ∖ E_iY) by at
  most ρ(e).
- **Applying (L1).** (L1) is applied with the ordered pair (Z′, Y), and it yields Z′ ⪯_i Y.
- **The cycle.** Z ≺_i Z′ ⪯_i Y ⪯_i Z gives Z ≺_i Z, which is impossible in a preorder.
- **What positivity is used.** Only that ρμ is atomless. Positivity of ρ is **not** used. This matters for the
  strengthening in (v).

## (ii) Lemma B1.1 — CORRECT

- **Radon–Nikodym and the choice of a, δ.** f = ρ^{ik}/ρ^{ij} is defined a.e. on Q_i because ρ^{ij} > 0 there.
  Since f > 0, the set S_− = {f < a − δ} can be non-null only if a − δ > 0. Hence η > 0 with
  (a − δ)(1 + η) < a + δ exists.
- **Choosing A and B.** For b small, ρ^{ij}(S_−) ≥ (1+η)b. A and B exist by the intermediate-value property of the
  atomless scalar measure ρ^{ij}μ. This is Sierpiński's theorem; Lyapunov is more than is needed, though harmless.
- **The models Y, Z (the role of N_+).** Take Y := P_i △ B and Z := P_i △ A. Both are subsets of U, and both accept
  all of N_+ ⊆ P_i because A, B ⊆ M. So both are regular. Then E_iY = B, E_iZ = A and Y △ Z = A ∪ B ⊆ Q_i. Hence
  Y △ Z lies in both edge regions, and both (L1) for ρ^{ij} and (L2) for ρ^{ik} (from B1.0) apply. Regularity is
  needed only because the leading property is defined for regular pairs. Every subset of M is the error set of a
  regular model, P_i △ A, which is the write-up's identification of world orders with orders on error sets ⊆ M.
- **The contradiction.** It runs in the stated direction: ρ^{ij}(A) > ρ^{ij}(B) gives Y ⪯_i Z, and Y ⪯_i Z with
  ρ^{ik}(A) < ρ^{ik}(B) violates (L2).
- **Glued density.** It is well defined because the two pieces agree a.e. on the overlap Q_i. Rescaling preserves
  (L1). The glued density is positive and integrable on R_ij ∪ R_ik = M.

## (iii) Lemma B1.2 — CORRECT

Every region membership and every exact change was re-derived.

- **Bookkeeping.**
  - D = C △ X ⊆ M, and E_iX = E_iC △ D, so Δ = ρ(D ∖ E_iC) − ρ(D ∩ E_iC) = s_C(D).
  - s_C(D) = s_a + s_b, because D ⊆ Q_1 ∪ Q_2 ∪ Q_3 a.e.
- **Pieces.** Split D_l ∩ E_iC and D_l ∖ E_iC separately into m pieces of equal ρ-mass; this is Lyapunov for a
  2-vector. Every piece is toggled exactly once, so its points still have their status in C when it is toggled.
  Hence each piece changes the ρ-error by s_C(D_l)/m, whatever has been toggled before.
- **Case 1 (Q_i ∖ D non-null).**
  - The room c ⊆ Q_i ∖ D is restored at the end of every round, so it has its C-status at the start of each round.
  - Order (a,b): step a changes the ρ-error by s_a/m + σρ(c), with σ = +1 for R⁺ and −1 for R⁻; step b changes it by
    s_b/m − σρ(c).
  - Order (b,a): step b changes it by s_b/m + σρ(c), and step a by s_a/m − σρ(c).
  - With τ = Δ/(2m) − s_a/m, the note's four sign/order combinations are exactly those that give both steps the change
    Δ/(2m). So whichever of R⁺, R⁻ is non-null serves both signs of τ.
  - Regions:
    - step a toggles a piece of D_i, a piece of D_j, and possibly c, all inside Q_i ∪ Q_j = R_ij;
    - step b toggles a piece of D_k and possibly c, inside Q_k ∪ Q_i = R_ik.
  - Fit: τ = (Δ/2 − s_a)/m, so |τ| decreases like 1/m and c fits for all large m.
  - Δ = 0 is covered: τ = −s_a/m and every step has change 0.
- **Case 2 (Q_i ⊆ D a.e.).**
  - **Leg values.** Lyapunov for the 6-vector halves all six numbers, so s_C(D′) = s_C(D″) = Δ/2. On D″ the
    intermediate model Z = C △ D′ has C's status, so s_Z(D″) = s_C(D″) = Δ/2.
  - **Room.** Room for leg 1 is D″ ∩ Q_i, of ρ-mass ρ(Q_i)/2 > 0; room for leg 2 is D′ ∩ Q_i, which is room relative
    to Z. Both are correct.
  - *Add one sentence* to justify "both legs use the same m": since |τ| ∝ 1/m in each leg, any m at least the larger
    of the two legs' thresholds fits both. So a common m exists, and every step then has change Δ/(4m).
- **End point and regularity.** Correct: all toggles lie in M, and every intermediate model is a measurable subset of
  U.
- NUMERICS. My own implementation of the chain, written independently of `b1py` (`ref_checks.py` §2), uses exact
  rationals. It ran 1683 instances: 834 in Case 1, 849 in Case 2, and 436 with Δ = 0. Every step lies in R_ij or
  R_ik. In Case 1 every step change equals Δ/N exactly. The changes sum to Δ, and no room cell is overdrawn.
  `b1py/transfer_chain.py` asserts only change > 0 and sum = Δ, not equality of the changes; my check closes that.

## (iv) Theorem B1.3 — CORRECT, and it yields "adds up" exactly in the sense of Def. addup

- **First claim.** By B1.2, every step Z_t → Z_{t+1} has its difference inside one region and a positive change.
  For regular pairs whose difference lies inside one region, ρ_i(E_iZ_{t+1} ∖ E_iZ_t) > ρ_i(E_iZ_t ∖ E_iZ_{t+1}) is
  the same as a positive change. On R_ij, ρ_i = ρ^{ij}; on R_ik, ρ_i = ρ^{ik}/c. Both are leading, so
  Z_t ⪯_i Z_{t+1}, and transitivity gives C ⪯_i X.
- **Second claim.** For regular Y, Z, the difference Y △ Z ⊆ M holds automatically. The first claim is therefore
  (L1) on S = M, and B1.0 gives (L2).
- **Additive case.** The steps have change ≥ 0, and each is accepted by the additive edge representation. Correct.
- **"Adds up" (Def. addup(b)).**
  - ν_i = ρ_iμ|_M + μ|_{N_+} is countably (hence finitely) additive on U. It vanishes on null sets, and it is positive
    on every non-null subset of U, because ρ_i > 0 a.e. on M and μ > 0 on N_+.
  - Relevant comparisons are B ⪯_i X with B ∈ C_L and X regular. B is coherent, so it agrees a.e. with some D_K,
    which contains the positive orthant; so B is regular.
  - Hence E_iB and E_iX both lie in M, ν_i(E_i·) = ρ_i(E_i·), and the second claim gives
    ν_i(E_iB) ≤ ν_i(E_iX). It endorses every regular comparison, which is more than is required.
  - Def. addup(c): the countably additive part is ν_i itself, with density ρ_i on M and 1 on N_+, which is > 0 a.e.
- **"Uses / not used".** Accurate: B1.3 needs only the preorder property, strict (G) and atomlessness. (IB) is
  genuinely not used.
- *Recommended framing for the write-up.* B1.3 says that ρ_iμ|_M is a **leading charge of world i on M** in the
  write-up's sense (§8.5, definition before Thm S21), since both properties hold. So it slots in as a new item of
  Theorem Q36: "(a′) n = 3: if world i has positive integrable leading densities on R_ij and R_ik, it has a leading
  charge on M, so (a) applies." It also strengthens Cor. Q37's hypothesis list to "has leading densities on both edge
  regions at e_i".

## (v) Corollary B1.4 and the strengthening — CORRECT

- **B1.4.** Under (H_U), if every world had positive integrable leading densities on both of its edge regions, B1.3
  would make every world add up. That is (M0), which Theorem M0closed(b) excludes. M0closed(b) is stated under
  exactly (H_U)'s axioms. The dependency is the only one, so the label "at the status of M0closed(b)" is right.
  Equivalent route: B1.3 ⇒ leading charge on M ⇒ Cor. Q37, with the same status.
- **The "in particular" clause.** Under strict (G), an additive representation on R_ij with a density ≥ 0
  automatically has density > 0 a.e.: adding a ρ-null non-null set would be a tie, against strict (G). So "not
  additive on one edge region" is correct as stated.
- **Strengthening via S21.** I checked the proof sketch of Theorem S21 line by line.
  - It fixes j with π(R_ij) > 0 and uses:
    - the leading property only for comparisons C_q versus X^{ij}_A, with q ∈ e_ij and A ⊆ R_ij. Both models equal
      P_i off R_ij (Lemma Q34), so their difference lies in R_ij and B1's (L1) applies;
    - strict (G) at worlds i and j;
    - competitiveness and closed sections at edge indices;
    - the generic-level argument on the segment e_ij.
  - The "no π-null sets" step then gives π > 0 on R_ij. The linking step is not needed for this.
  - **Add one sentence:** S21 uses **both** properties of a leading charge, and for a density ρ ≥ 0 that is only
    (L1)-leading, (L2) is supplied by B1.0. B1.0 does not use positivity (see (ii)).
  - With that sentence, "positive" in B1.4 may indeed be weakened to "≥ 0 and not a.e. zero on R_ij", and B1.1 can
    then be applied to the positive densities S21 produces. CHECKED is the right label, since this is by inspection
    of a sketch.
- *Scope remark (not a gap).* B1.4 concerns **integrable** (countably additive) densities. B1.1 needs Radon–Nikodym,
  and B1.2 needs Lyapunov, so neither covers finitely additive edge charges or non-integrable σ-finite densities. The
  natural nearby statement worth stating as open is: "two leading *charges* on R_ij, R_ik that are > 0 on Q_i are
  proportional there". The S21 small-set trick replaces atomlessness, but Lyapunov-type equal splitting for charges
  is not automatic.

## (vi) Corollary B1.5

**(a) GAP (fixable).** "A reversed comparison C ⪯_i X with ψ_i(C) > ψ_i(X) gives X ≺_i C ⪯_i X, a strict cycle."

- The first claim of B1.3 gives only X ⪯_i C, not X ≺_i C.
- The conclusion is right, but the justification is the **second** claim. That claim directly forbids
  C ⪯_i X when ψ_i(C) > ψ_i(X), and the strict cycle lives inside its proof (B1.0, through strict (G)).
- *Fix:* "A reversed comparison C ⪯_i X with ψ_i(C) > ψ_i(X) contradicts the second claim of B1.3 (by B1.0 it would
  produce a strict cycle through a strict-(G) perturbation)."
- Also state the hypothesis precisely: "world i accepts every ψ_i-strict comparison between regular models differing
  inside R_ij or inside R_ik, and ρ_i > 0 a.e."

The same wording issue affects `b1py/t1_chain.py`. Its line "derived: X strictly better than C" is not derived by
the chain, which gives only ⪯. Strictness comes from B1.0. Either change the printout or add this remark to the note.

**(b) CORRECT but too weak.**

- **The measure-equality version.** If ν and ν′ vanish on null sets, it is trivial: S ∖ R_ij ⊆ Q_k ⊆ R_ik.
- **Why it is not the brief's mechanism.** "Several additive scores that agree on edge regions" naturally means that
  they induce the **same comparisons** there, not that they are equal as measures. Equal measures would make
  "min/max" pointless from the start.
- *Fix (replacement statement, proved by B1.1).* Let ψ^1, …, ψ^r be additive at world i with positive integrable
  densities ρ^s on M. Suppose that for each of R_ij and R_ik all ψ^s induce the same comparisons between regular
  models differing inside that region.
  - Additive orders are leading, so B1.1, applied on R_ij (with Q_i replaced by R_ij, the same proof), gives
    ρ^s = a_s ρ^1 on R_ij. Similarly ρ^s = b_s ρ^1 on R_ik.
  - Since Q_i is non-null, a_s = b_s.
  - Hence ψ^s = a_s ψ^1 on all regular models (the error sets lie in M, so there is no additive constant).
  - Any min, max or other monotone aggregate of the ψ^s is therefore the order of ψ^1.

## §0 headline — WRONG as stated (wording fix)

Lines 25–26 say: "a world's comparisons inside its two edge regions determine all of its comparisons on M, by
transitivity through the link class Q_i". Without the leading-density hypothesis this is false, even for preorders
with strict (G) and (IB).

**Counterexample.** Take non-null disjoint a ⊆ Q_j and b ⊆ Q_k. On error sets A, B ⊆ M put

  A ≤ B  iff  A ⊆ B a.e., or (A ∖ B ⊆ a and B ∖ A ⊇ b).

- **It is a preorder.** The only non-trivial composition would need b ⊆ B and b ∩ B = ∅.
- **It is strictly monotone.** A ⊊ B excludes B ≤ A.
- **It satisfies de Finetti cancellation**, since it depends only on A ∖ B and B ∖ A.
- **It has the same edge comparisons as inclusion.** A comparison of the second kind has A ∖ B meeting Q_j and
  B ∖ A meeting Q_k. So it lies in neither edge region.
- **It differs from inclusion**, since a ≤ b.

Brute-force check on 6 atoms: `ref_checks.py` §3 prints True / True / True.

*Fix:* "a world's comparisons inside its two edge regions determine all of its comparisons on M **whenever they admit
leading densities** (Theorem B1.3)". The "Correction to the brief" paragraph ("tame edges constrain the interior
completely") is already correctly qualified. A smaller wording point: §3 says that Q36/Q37 "exclude complete worlds…,
worlds with a nonzero leading charge, (CP-a) worlds". They exclude **rankings all of whose worlds** are of these
kinds, not single worlds.

## Scripts

- `python3 -I b1py/transfer_chain.py` (85 s) and `python3 -I b1py/t1_chain.py` (1 s) reproduce the stored `.out` files
  exactly: 4000 instances, 2000 of them without room; the worked example has 2048 steps of 1/2048; the T1 instance
  gives the three worlds as stated.
- Caveats:
  - `transfer_chain.py` does not test Δ = 0, and it does not assert that the step changes are equal. Both are covered
    by `b1ref_py/ref_checks.py`.
  - The "strictly better" printouts of `t1_chain.py`; see (vi)(a).
- No verdict rests on numerics.

## Files

- `b1ref_py/ref_checks.py`, `b1ref_py/ref_checks.out`: region identities, an independent chain check covering both
  cases and Δ = 0, and the §0 counterexample.
- `b1ref_py/rerun_transfer.out`, `b1ref_py/rerun_t1.out`: the reruns.
