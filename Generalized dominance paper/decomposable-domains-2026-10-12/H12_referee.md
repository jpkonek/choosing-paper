# Referee report on H1_notes.md and H2_notes.md

15 Oct 2026, round 17. This is an adversarial reading against:
- BRIEF15 and the files it lists: E1_notes, F1/F2_notes, F12_referee, and the D2 notes and referees;
- write-up §§2–3, §7.7 (Prop. M0, Thm. Estructure, Thm. M0closed(a),(b), Thm. kkm, Lemma vectorform) and §8.5.

**Scripts.** The author scripts were rerun with `python3 -I` (`h1py/h1_localization.py`, `h2py/h2_mirrored_d2.py`).
Both outputs are byte-identical to the stored `.out`; the reruns are in `h12ref_py/*.rerun`. My own checks are in
`h12ref_py/h12ref_checks.py` (output in `.out`). No verdict rests on numerics.

## 0. Verdicts

| Item | Verdict |
|---|---|
| H1 §1 (definitions; (E1)/(E2) and (R); base ⇒ D-localized) | **CORRECT** |
| Lemma H1.0(a) (d_t > 0; infimum attained) | **CORRECT** |
| Lemma H1.0(b) | **CORRECT**, with a one-line omission: finiteness of Φ(Y) is used but not shown (§1.2) |
| Lemma H1.0(c) | **CORRECT** |
| Lemma H1.1 (admissibility automatic) and the answer to brief step (2) | **CORRECT** |
| Theorem H1.2 | **CORRECT**. The use of M0closed(a) without integrability is sound; a robust one-line justification is in §1.4 |
| Theorem H1.3 (both versions) | **CORRECT** |
| Corollary H1.4; the WARNING as settled in §5 | **CORRECT** as scoped in §5. The §0 wording is broader than what is proved |
| "E1.5 holds without (h)" (H1 §0 Consequence 1, §5 "Relation", §4 remarks) | **GAP (wording)**. What is proved is narrower; the correct statement is in §1.6 |
| H1 §6, "exactly one of (A), (B), (C)" / "a cover needs one of" | **GAP**. The list is neither exhaustive nor exclusive, and (B) is too coarse after H2.3 (§1.7, §3) |
| H2.0 | **CORRECT** |
| H2.1(a) | **CORRECT** |
| H2.1(b) | **CORRECT** for integrable ρ_j, which is the case H2.3 uses. **GAP (fixable)** for a.e.-finite ρ_j: the endorsement reading is unspecified (§2.2) |
| H2.2 | **CORRECT**. Joint reweighting is not new: E1.4 is already stated and proved for all worlds at once. The new content is (h′) |
| Theorem H2.3 | **CORRECT**, including the pigeonhole step and the finiteness hypothesis. **Strengthening (PROVED here, §2.4):** (h′) is superfluous |
| Corollary H2.3′, "at least two worlds fail to add up" | **GAP (fixable)**: the partners given by H2.1(a) can coincide (§2.5) |
| H2 §5.1 (CHECKED geometry) | **CORRECT** at CHECKED level |
| H2 §5.2 | **CORRECT** for ψ with (b). "and in fact for every admissible shadow (E1.1)" is **unjustified**, and one citation is wrong (§2.6) |
| H2 §5.3, displayed "(PROVED)" | **CORRECT** |
| Theorem H2.4 (mirrored D2) | **CORRECT**: every axiom re-derived independently. One wording slip at b = 1, harmless (§2.7) |
| H1 (B) versus H2.Q | **Not the same residual.** H2's is strictly smaller; the precise statement is in §3 |

Net assessment:
- Nothing is WRONG.
- H1.0 and H1.2 are the strongest results of the round. They remove both the heaviness hypothesis and the
  integrability hypothesis at one world.
- Combining H1.0 with H2's walk removes (h′) from H2.3 as well, so that heaviness plays no role anywhere in the
  end-protected route.

---

## 1. H1

### 1.1 H1.0(a): compactness and attainment (CORRECT)

- **The coherent models of M_U** are exactly the D_K with K ⊇ K′. If D_K ⊆ U a.e., then D_K ⊆ U because both are
  open convex sets; and P_K ≤ P_{K′} gives the converse.
- **Compactness.**
  - The credal sets containing K′ form a Hausdorff-compact family: Blaschke selection, plus closedness of "⊇ K′".
  - |P_{K_n}(g) − P_K(g)| ≤ |g|·d_H gives pointwise convergence of the indicators off {P_K = 0} ∪ {g ≥ 0}.
  - {P_K = 0} is null. P_K(𝟏) = 1 > 0, so {P_K > 0} is the interior of the closed convex cone {P_K ≥ 0}: concavity
    along a segment from 𝟏 rules out a zero at an interior point. Hence {P_K = 0} is a convex-set boundary.
  - Dominated convergence (μ finite) gives convergence in measure.
- **Lower semicontinuity.** Pass to a subsequence that attains the liminf, then to an a.e.-convergent
  sub-subsequence, then apply Fatou. This is valid for [0, ∞]-valued Φ, i.e. for non-integrable ρ₁.
- **Conclusion.**
  - The infimum is attained at a coherent C* ≠ B_t (mod null).
  - Z_t is null, so |t·c| > 0 a.e. and Φ(C*) > 0.
  - d_t = +∞ is allowed and harmless.

So the answer to the brief's question is yes: the infimum is attained and positive.

### 1.2 H1.0(b) (CORRECT; one omitted line)

The sign identity, the pointwise identity and the integrability of the *difference* are all right. The difference
vanishes off Y △ Y′, which at every world k lies in E_kY ∪ E_kY′.

**What is missing.** The statement "Φ(Y) − Φ(Y′) = …" needs Φ(Y), Φ(Y′) < ∞, or at least one of them finite. The
proof does not show this.

**Fix (one line).** On Y △ B_t, the worlds at which B_t is right are exactly the worlds at which Y errs. Hence
|t·c| ≤ Σ_{k : g ∈ E_kY} t_kρ_k, and so Φ(Y) ≤ Σ_k t_k ρ_kμ(E_kY) < ∞.

This is checked pointwise, with a non-integrable ρ₁, in `h12ref_checks.py` (1)–(2): 0 failures out of 200 random t.

### 1.3 H1.0(c) and Lemma H1.1 (CORRECT)

**H1.0(c).** (R) for (E2) gives ρ_kμ(E_kC) ≤ ρ_kμ(E_kX) < ∞. Coherent C is regular. Then (b) applies with
Y = C and Y′ = X.

**H1.1.** Each step re-derives.
1. Competitiveness of T1 comes from Thm. kkm: T1 is tied at every world with a selected C_p, which is competitive on
   supp p. Any k ∈ supp p suffices, since endorsement is assumed at every world.
2. Both (E2) masses are finite because A ⊆ M ∖ D_m.
3. Separation of the compact convex Lyapunov range R_m from −int ℝ³₊ forces a normal p ≥ 0.
4. In the limit step, M ∖ D_m ⊆ M ∖ D_{m′} for m′ ≥ m, and μ(⋂D_m) = 0.
5. Interiority uses the (−,−,+) region near r₁₂. At p*₃ = 0 it gives p*·v = −p*₁ρ₁ − p*₂ρ₂ < 0 there.
6. The last step uses v = c on D_{T1} ∩ M and v = −c off it, with N₊ ⊆ B_{p*}.

**Consequence for brief step (2).**
- With D_m = (deep ends) ∪ ({ρ_k > m} ∩ M), the comparison T1 ⪯_k Y with Y = T1 on D_m is a base comparison. So
  every tuple of base endorsers (integrable, or a.e.-finite under (E2)) is admissible.
- The brief's target "∏G_i contains no admissible tuple" is therefore impossible under (H_U) whenever every G_i is
  nonempty. **CORRECT.**
- This needs countably many ends, for the summable choice of depths.

### 1.4 Theorem H1.2 (CORRECT)

Every step was re-derived:
- **D′_m.** It is a localizing family. D′-localized implies D-localized.
- **Admissibility.** H1.1 with D′ applies: ρ₁ ≤ m on M ∖ D′_m.
- **A weight in I_ρ.** Tonelli gives null ties for a.e. t.
- **X_m.**
  - X_m is regular.
  - Where B_t errs at world 1, |t·c| = −σ₁ t·c ≤ t₂ρ₂ + t₃ρ₃. Checked in `h12ref_checks.py` (1).
  - Hence Φ(X_m) ≤ ∫_{D′_m}(ρ₂ + ρ₃) → 0.
  - E₁X_m ⊆ M ∖ D′_m, so its ρ₁-cost is ≤ m·μ(M).
- **Dominators.** The kkm dominator's world-1 vector is ≤ 0 on D′_m, so it is D′-localized and endorsed.
- **The (E1) variant.** With ρ₁μ(E₁T1) < ∞, the finiteness that H1.1 step 1 needs holds, and (R) holds for (E1).

**The cancellation sense.** (E2) is invoked only on comparisons whose positive part has finite ρ₁-mass:
- T1 ⪯₁ T1 △ A with A ⊆ M ∖ D′_m;
- C_m ⪯₁ X_m.

So the vacuous case ∞ ≤ ∞ never enters, and the theorem holds under any reading that has (R).

**M0closed(a) without integrability.**
- The write-up records "integrability is not used" (§7.7, standing data and status of (a)).
- The point is in fact trivial, and the note should say so.
- c and c̃ := c/|c| have the same strict Bayes sets B_q, the same tie sets Z_q and the same E. c̃ is strictly signed
  and bounded, hence integrable.
- Both property (γ) and "D_{T1} = B_{p*} ∪ S, S ⊆ Z_{p*}" are statements about these sets only. So M0closed(a) for
  any measurable strictly signed field follows from its integrable case.
- **Requested addition:** this sentence.

### 1.5 Theorem H1.3 and Corollary H1.4 (CORRECT)

**H1.3, first version.**
- X_m = T1 on D_m is world-k-correct on D^k_m ∩ {T1 correct at k}.
- Φ(X_m) ≤ ∫_{D_m} Σρ → 0.
- Note the scope. Endorsement of all (D^k, T1)-localized comparisons is *stronger* than base endorsement when world k
  has T1-wrong ends: there such a comparison may be W-positive.

**H1.3, second version.** Off R_ij, correctness at i and at j is the same advice, so the pairwise conditions give a
consistent X_m.

**The remark on T1-correct sets.** Such sets are automatically compatible, since T1 is correct at exactly one of i, j
on R_ij. **CORRECT.**

**H1.4.**
- (a) and (b) follow from H1.2 together with "base ⇒ D-localized" (H1 §1, which uses end-protection).
- The D2sigma example in (b) endorses in the (E2) sense. Relevant comparisons out of C_b have δ⁻ ⊆ c_b, which has
  finite φ-mass (F1.7(a)). Generator comparisons are endorsed as finite ≤ ∞.

**WARNING (§5).** Settled within H1.4's setting (one exceptional world next to two integrable full endorsers). §0
item (1)(a) ("the system is excluded") should carry that scope.

### 1.6 "E1.5 holds without (h)": GAP (wording)

**What E1.5 hypothesises.** E1.5 allows every world to be end-protected and assumes only base endorsers. So
"E1.5 without (h)" literally means (b) alone, with ends that may be T1-wrong.

**What H1 proves.**
- **(i) One exceptional world (H1.2).** The other two worlds must have integrable *full* endorsers.
- **(ii) All worlds (H1.3).** This needs all ends eventually T1-correct.
  - (h) implies T1-correctness. Admissibility (step 1 of E1.5, which has no (h)) gives T1 = B_{p*} up to ties.
    Deep in an end of world i, (h) gives p*·cσ_i ≥ p*_iρ_i − p*_jρ_j − p*_kρ_k > 0.
  - So E1.5 is a special case of H1.3.

Neither (i) nor (ii) covers E1.5 with T1-wrong ends.

**Correct statement.**
> E1.5 holds with (h) replaced by eventual T1-correctness of every end (H1.3), a condition that (h) implies; and,
> for finite families of ends, with (h) dropped altogether unless the conflict digraph has a directed cycle (H2.3 as
> strengthened in §2.4 below).

### 1.7 H1 §6: GAP (the list is not exhaustive)

**What H1.2 and H1.3 exclude.**
- (H1.2) one world with an a.e.-finite D-localized endorser, next to two integrable full endorsers.
- (H1.3) all worlds with integrable endorsers whose localizations are compatible, or with (D, T1)-localized
  endorsement.

**What the complement contains**, besides (A), (B), (C):
- **(D)** Configurations in which every world has an a.e.-finite localized endorser, the localizations are
  compatible, but:
  - at least two worlds' endorsers are non-integrable; or
  - one world's endorser is non-integrable and the others have only localized, not full, integrable endorsers.

  H1 itself notes that "a σ-finite version for two or more worlds is not proved". This is a genuine obstacle.
  - If min(ρ_i, ρ_j) is non-integrable on R_ij, every model has infinite cost at world i or at world j there.
  - So no X with finite costs at both worlds is available near B_t.
- **(A)** need not add "the other two worlds are integrable". Without that clause it is the right negation, and it
  then subsumes (C): a world adding up only through a purely finitely additive weight has no a.e.-finite
  endorser.
- **"Exactly one"** is false as a logical claim: (B) and (C) can co-occur.

**Requested change.** Replace "exactly one of" by "at least one of (A′) [= (A) without its last clause], (B), (D)",
and narrow (B) as in §3.

---

## 2. H2

### 2.1 H2.0 and H2.1(a) (CORRECT)

**H2.0.**
- Kept pieces are ends.
- Positivity transfers by pigeonhole over twelve pieces.
- "Eventually ≥ 0 / = 0" transfers by taking the maximum of finitely many depths.
- Finiteness of a family is preserved.

**H2.1(a)**, re-derived:
- At j ∈ A(W), X is strictly better everywhere it differs, so T1 ⋠_j X by strict (G).
- At i, δ_i = 1_R − 1_p is −1 at every depth of W and positive only off the deep ends, so end-protection forbids
  T1 ⪯_i X.
- Competitiveness of T1 then gives a world in V(W).
- The disjoint p_n exist. Infinitely many layers W_m ∖ W_{m+1} are non-null, and μ is non-atomic.
- R is fixed before n.
- Pigeonhole over |V(W)| ≤ 2 then gives a world j, and boundedness of ν gives ν(R) ≤ inf_n ν(p_n) = 0.

A corollary worth stating: if V(W) = {j}, every a.e.-finite (E2) endorser of j's out-of-T1 comparisons has
ρ_j(W_m) = ∞ for every m. Otherwise one chooses p ⊆ W_m that meets every depth with ρ_j(p) < ρ_j(R).

### 2.2 H2.1(b) (CORRECT for integrable ρ_j; GAP for a.e.-finite ρ_j)

**The argument is right.** Two points need care:
- **Raising M.** M may be raised freely: the supposition at M implies it at every M′ ≥ M, because the S_M decrease.
  This is what makes "R stays non-null for M large" and "T1-wrong ends of V(W)-worlds are disjoint from W at depth M"
  legitimate. Both use finiteness of 𝒮_j.
- **p is a base comparison.** δ_j = 1_p − 1_R vanishes on every S_M with S ∈ 𝒮_j, so it is a base comparison out of
  T1.

**The GAP.** The note allows ρ_j "finite a.e." but does not fix the reading of endorsement.
- Under the total-cost reading (E1), ρ_jμ(E_jT1) may be ∞. The comparison T1 ⪯_j X is then endorsed vacuously and no
  contradiction follows. This is exactly the F12_referee §5.2 defect.
- **Fix:** state (E2), under which ρ_j(R) ≤ ρ_j(p) with both finite; or assume ρ_jμ(E_jT1) < ∞.

H2.3 uses ρ_j ∈ L¹, so H2.3 is unaffected.

### 2.3 H2.2 (CORRECT, not new except (h′))

E1.4 already reweights all worlds simultaneously. Its f_i are built for "each world i" at once, and its proof notes
that f_k = 0 wherever T1 errs at k.

H2.2's addition is (h′):
- On S_{m_l(S)}, ρ′_i ≥ l(ρ_j + ρ_k) ≥ l·Σ_{k∈W(g)}ρ′_k, since f_k = 0 for k ∈ W(g).
- So the ratio is ≥ l. ✓

"What does not transfer is (b)" repeats E1.5's scope remark. ✓

### 2.4 Theorem H2.3 (CORRECT) and a strengthening: (h′) is superfluous (PROVED here)

**Check of the note's proof.**
- **Step 1** is H1.1 with D_m = deep ends.
- **Step 2.**
  - H2.1(b) needs integrable base endorsers at the V(W)-worlds and finite families. Both are available.
- **Step 3.**
  - m(t) is uniform because the families are finite.
- **Step 4 (the walk).**
  - Not eventually 0 on a T1-correct end implies not eventually ≥ 0, and then W-positivity for a T1-wrong W.
  - Covering D ∩ W_{m′(M)} by finitely many S_M, then pigeonhole: one S works for infinitely many M, hence for all M.
  - The arrow condition μ(W_k ∩ S_k) > 0 for every k needs D ∩ W_{max(k, m′(M))} rather than D ∩ W_{m′(M)}. This is
    a trivial adjustment.
  - On D ∩ S_M, C ≠ B_t and B_t is right at j, so δ_j = −1.
- **Conclusion.** An infinite walk in a 3-vertex digraph has a cycle. In the acyclic case every comparison is a base
  comparison, and then C = B_t a.e.

**Finiteness** is used exactly where the note says: the pigeonhole and the uniform m(t). With countably many ends the
covering in Step 4 can use a different S at each M, and the argument fails.

**Proposition R.1 (PROVED).** Theorem H2.3 holds without (h′): (H_U), finite refined families 𝒮_i, ρ_i ∈ L¹ with
ρ_i > 0 a.e. and (b) give a contradiction whenever Γ is acyclic.

*Proof.*
1. **A weight.** ψ is admissible (Step 1). Take t ∈ I_ψ.
2. **The localized models.** Choose depths a_S(m) ↑ ∞ beyond each end's T1-purity depth, and let D_m := ⋃ S_{a_S(m)}
   over all ends of all worlds. Put X_m := T1 on D_m and B_t off D_m.
   - X_m is regular.
   - Φ(X_m) ≤ ∫_{D_m}Σρ → 0 by H1.0(b).
   - All costs are finite.
3. **Dominators.** Let C_m be a kkm dominator of X_m, with vectors δ_k := 1_{E_kX_m} − 1_{E_kC_m}.
   - δ_k ≤ 0 deep in T1-correct ends of k, and δ_k ≥ 0 deep in T1-wrong ends of k, because X_m = T1 there.
   - This replaces Step 3 of H2.3, which is the only place (h′) was used.
4. **The walk.** Step 4 of H2.3 runs verbatim with X_m in place of B_t.
   - Suppose δ_i is W-positive and D := {δ_i = 1} ∩ W.
   - H2.1(b) (static, (h′)-free) covers D at large depth by finitely many T1-correct S_M, S ∈ 𝒮_j, j ∈ V(W). Take
     M ≥ max a_S(m).
   - On D ∩ S_M, X_m = T1 is right at j and C_m ≠ X_m, so δ_j = −1 at every depth.
   - So i → j, and δ_j is not eventually ≥ 0 on a T1-correct end.
5. **Conclusion.** Acyclic Γ makes every δ_k eventually 0 on every end. Then every dominator comparison is a base
   comparison and is endorsed by (b), against H1.0(c) once Φ(X_m) < d_t. ∎

**Consequences.**
- Heaviness ((h), (h′)) plays no role anywhere in the finite-ends, integrable-base route.
- H2.2 is not needed for H2.3.
- H2.Q should be restated without (h′) (§3).

### 2.5 Corollary H2.3′ (GAP, fixable)

**The defect.** "Every world on the cycle has a partner that fails to add up, so at least two worlds fail to add up"
does not follow when |V(W)| = 2. Example: a 2-cycle 1 ⇄ 2 with W₁ in (+,−,−) and W₂ in (−,+,−). Then
V(W₁) = {2,3} and V(W₂) = {1,3}, and H2.1(a) may return world 3 both times.

**What does hold:**
- **(a)** If the cycle's ends have singleton V (as in the §5.1 template, V(A) = {3}, V(B) = {1}), the two partners
  differ. Then two worlds fail to add up in the bounded sense.
- **(b)** In general, H1.2 alone shows the following for any cover in H2.3's class: **at least two worlds have no
  integrable density endorsing all their relevant comparisons.**
  - Otherwise two worlds have integrable full endorsers, and the third has an integrable base endorser, which is
    D-localized with D = its deep ends.
  - H1.2 then gives a contradiction.

  This needs no cycle.

**Fix:** use (b), and keep the bounded-sense claim only under (a).

### 2.6 H2 §5 (CORRECT, with two corrections)

**§5.1.** CHECKED-level geometry. `h12ref_checks.py` (3):
- T1 accepts no sample in the ∂U collar;
- the (+,+,−) and (−,+,+) collar pieces have the stated correctness patterns.

**§5.2 is correct for ψ with (b).** The walk forces C to accept non-null parts of A and of B at every depth, and the
signs of δ₁, δ₂, δ₃ are right. Two corrections:
- **"and in fact for every admissible shadow (E1.1)": delete.**
  - For an admissible ν without (b), the unendorsed dominator comparison may be a base comparison.
  - Nothing then forces a germ exchange.
- **"both infinitely heavy for it (Lemma H2.1(b))": wrong citation.**
  - The germ at a world's own T1-wrong end is protected by **end-protection** itself: no relevant comparison that is
    −1 at every depth there is accepted unless it is positive at some end.
  - The germ at its T1-correct end is heavy by **H2.1(a)** (germ dominance of the partner).
  - H2.1(b) is shadowing, not heaviness.

**§5.3.** The displayed "(PROVED)" claim is correct.
- World 2 strictly prefers Y, so T1 ⪯₁ Y or T1 ⪯₃ Y.
- Take D_A, D_B to be *all* of {C accepts} ∩ (deep A, B). Then the dominator vector cancels the exchange terms
  exactly.
- The sum is ternary when the supports of γ_k and φ_k are disjoint.
- Lemma vectorform (P2 Lemma 1.1) makes 𝒜_k closed under ternary sums.

The "breaks at realisability" diagnosis is accurate: a vector in 𝒜_k need not be realised by a comparison out of a
selected model, so (b) does not apply to it.

### 2.7 Theorem H2.4 (CORRECT; every axiom re-derived independently)

- **Per-world axioms.**
  - World 2 is D2's world-1 rule in x̃ = 1 − x, which pushes λ|_M to Lebesgue measure.
  - E₂C_b = d_b = {x̃ ≤ 1 − b}, and E₂X ∩ N₊ = N_X. So world 2 has exactly the structure of D2's world 1 with the
    chain reindexed by b̃ = 1 − b.
  - Lemma D2.3 (strict (G), (IB), preorder via ternary-sum closure) and Lemma D2.4 (closed sections, both the regular
    case (ii) and the non-regular case (i)) are single-world statements and transfer.
  - World-2 sections are closed final segments in b, and p ↦ p₂ is continuous.
- **(K) for every model, rederived by hand.**
  - *n = 0.* If λ(Q) ≥ λ(P), then δ₁ ∈ 𝒦₀:
    - it is 1_Q ≥ 0 on {x ≥ b} with b < 1;
    - its tails are ≥ λ(Q) − λ(P).

    Otherwise δ₂ ∈ 𝒦₀′:
    - it is 1_P ≥ 0 on {x < b} with b > 0;
    - its heads are ≥ λ(P) − λ(Q) > 0.
  - *n > 0.* World-1 rejection forces λ(P) > λ(Q) + n, because Q ⊆ {x ≥ t} for t < b. World-2 rejection forces
    λ(Q) > λ(P) + n. These are incompatible.
  - `h12ref_checks.py` (4) is an exact-rational check on random interval unions: 1500 tests, 0 failures. The test is
    non-trivial: 573 cases are accepted only at world 1 and 688 only at world 2.
- **No weak domination.**
  - R⁻ forces n = 0. Then Q is null, and strict (G) at world 2 applied to −δ₂ = −1_P forces P null.
  - **Wording slip (harmless).** "−δ₁ − g_* ∈ 𝒦₀ is impossible, since near x = 1 it is ≤ −1 on Q_g" is false at
    b = 1. There −δ₁ = 1_{M∖A} may be +1 near 1. But at b = 1, Q = A ∖ c₁ = ∅ trivially, so the conclusion "Q null"
    stands.
  - Treat b = 1 separately. This is the same separate case both D2 referees required.
  - b = 0 needs nothing extra: world 2's step uses strict (G) only.
- **Remaining axioms.** U_L = C_L = {C_b}, (C) and (LA) follow via Thm. kkm. (LF) holds by C2.1(4).
- **Neither world adds up.**
  - World 1: D2.1 step 7, which uses only world-1 generator comparisons.
  - World 2: the mirror, with ν(d_{1−a′}) = 0.

The author's NUMERICS reran identically. The remark "Why it does not help T1" is consistent with §1.6: both ends are
target-correct, so H1.3 applies, with or without heaviness.

---

## 3. Priority 3: is H1's "mutual sheltering" (B) the same residual as H2.Q?

**No. H2's residual is strictly smaller, and after §2.4 it supersedes (B).**

**Translation.** Put a class 𝒞 on top of (H_U):
- every world is end-protected with a finite family of ends, refined by H2.0;
- every world has ρ_k ∈ L¹, ρ_k > 0 a.e., endorsing its base comparisons.

Within 𝒞, take as the localization of world k its deep ends. Then H1.3's compatibility condition fails iff Γ has an
arrow.
- On R_ij, two overlapping ends cannot both be T1-correct, or both T1-wrong, at their worlds. T1 is correct at exactly
  one of i, j there.
- So an overlap at every depth is precisely a T1-wrong end of one world meeting a T1-correct end of the other: an
  arrow.
- By H2.1(b), every T1-wrong end is shadowed, so it produces an arrow.

Hence, within 𝒞:
- **H1 (B) ⟺ Γ has an arrow ⟺ some world has a T1-wrong end.**
- **H2's residual ⟺ Γ has a directed cycle**, and by Prop. R.1 this holds without (h′).

The gap between them consists of the configurations with an arrow but no cycle. These are excluded by H2.3. So (B)
must be narrowed.

(B) is also inaccurate in two smaller ways:
- Its statement is one-directional, although its name says "mutual".
- It speaks of "two exceptional worlds", which omits 3-cycles.

**Precise common residual (R\*).** A ranking with (H_U) in class 𝒞 whose conflict digraph Γ contains a directed
cycle (a 2-cycle or a 3-cycle). In any cover of type R\*:
1. At least two worlds have T1-wrong ends.
2. At least two worlds have no integrable full endorser (§2.5(b)). If the cycle's ends have singleton V, two worlds
   fail to add up in the bounded sense (H2.1(a)).
3. **What the dominators must do.** For every admissible ψ with (b) (heaviness not required), every t ∈ I_ψ, and every
   m, with X_m = T1 on deep ends and B_t elsewhere:
   - every kkm dominator C of X_m is W-positive at some world of the cycle;
   - along the walk, C gives non-T1 advice on non-null sets at every depth of the T1-wrong ends of a cycle;
   - and C errs at every depth on the shadowing T1-correct ends (the germ exchange of H2 §5.2).
4. **H2.Q, restated without (h′) and with X_m in place of B^ψ_t:** can these germ exchanges be accepted, for a
   non-null set of t, with closed sections and T1 competitive?

**Outside 𝒞, both notes leave the following open:**
- (A′) some world has no a.e.-finite endorser of its D-localized comparisons, for any vanishing D;
- (D) σ-finite-only endorsers at two or more worlds (§1.7);
- countably many ends: H2.3's pigeonhole fails, although H1.3 still covers the T1-correct case;
- non-end protection;
- (C) is contained in (A′).

---

## 4. Requested changes

1. **H1.0(b).** Add Φ(Y) ≤ Σ_k t_kρ_kμ(E_kY) (§1.2).
2. **H1.2.** Add the normalization c/|c| as the justification for M0closed(a) without integrability (§1.4).
3. **H1 §0 Consequence 1, §4 remarks and §5 "Relation".** Replace "E1.5 holds without (h)" by the statement in §1.6.
   Scope §0 item (1)(a) to H1.4's setting.
4. **H1 §6.** Replace "exactly one of (A), (B), (C)" by "at least one of (A′), (B), (D)". Narrow (B) to "Γ has a
   directed cycle", citing H2.3 and Prop. R.1 (§§1.7, 3).
5. **H2.1(b).** Fix the endorsement reading to (E2), or assume ρ_jμ(E_jT1) < ∞ (§2.2).
6. **H2.2.** Credit joint reweighting to E1.4. The new content is (h′).
7. **H2.3.** Record Prop. R.1: (h′) is superfluous. Correct the arrow-depth detail (§2.4).
8. **H2.3′.** Replace "at least two worlds fail to add up" as in §2.5.
9. **H2 §5.2.** Delete "in fact for every admissible shadow". Correct the citation to end-protection plus H2.1(a)
   (§2.6).
10. **H2.4 step 3.** Treat b = 1 separately (§2.7).
11. **H2.Q.** Restate without (h′) and with X_m (§3).

## 5. Files (`h12ref_py/`)

- `h1_localization.rerun`, `h2_mirrored_d2.rerun`: byte-identical reruns of the author scripts.
- `h12ref_checks.py` (+ `.out`):
  - (1) the H1.0(b) identity and the bound where B_t errs at world 1, with a non-integrable ρ₁;
  - (2) the bound Φ ≤ Σt_kρ_kμ(E_k·);
  - (3) the §5.1 collar geometry;
  - (4) exact (K) for H2.4.
