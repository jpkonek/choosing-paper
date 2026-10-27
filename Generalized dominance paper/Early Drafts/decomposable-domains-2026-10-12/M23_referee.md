# Referee report on M2_notes.md and M3_notes.md (round 20)

16 Oct 2026. Both notes were read against BRIEF17 and these background files:
- L4_notes and L4_referee;
- K2_notes and K2_referee;
- K3_notes §§1–2;
- L3_notes and L23_referee;
- B2_notes and B2_referee;
- D1_notes and D1_referee;
- R10b §5 and N28 §3;
- the write-up §§2–7: setting, Prop. necessary, §5 (N₀, Thm TS, TSalways), §6 (route I1), and §7.7 (quasilin, ball,
  crosspin, chainchords, carrying, M0closed).

I assumed every claim was wrong until I had re-derived it. Where I only read a step rather than re-derive it, I say so.

**Numerics.**
- `m2py/m2_checks.py` and `m3py/m3_checks.py` were rerun with `python3 -I` from inside their folders. Both outputs are
  byte-identical to the stored `.out` files (copies in `m23ref_py/`).
- My own scratch checks are in `m23ref_py/ref_checks.py` (+ `.out`). They are NUMERICS only; no verdict rests on them.

---

## 0. Verdicts

### M2

| Item | Verdict |
|---|---|
| (RL), forced pairs, limit pairs, 𝔉𝔏 (§1) | CORRECT |
| M2.1 (lower semicontinuity) | CORRECT |
| M2.2 (acceptance and divisibility; limit pairs, step 4) | CORRECT |
| M2.3 (endorser exists; maximal support) | CORRECT. **GAP (wording):** "no hypothesis on world 1 beyond strict (G) and (IB)" is false as written; world 1's competitiveness and closed sections are used (§1.3) |
| **M2.4 step 3 (limit-pair margin)** | **CORRECT** (§2) |
| M2.4 overall ((γ₀), any n) | CORRECT |
| **M2.5 step 1 (the π-part vanishes)** | **CORRECT**: it vanishes exactly (§3) |
| M2.5 steps 2–4 | CORRECT |
| **M2.6** | **CORRECT, and it can be sharpened.** L4_referee's Proposition R applies verbatim and removes (I₂)/(I₃). Only configuration (V) remains (§4) |
| M2.6, "L4.9 itself is unrefereed"; Q_M2 "answered no" | out of date / overclaim (§4) |
| **M2.7** | **CORRECT** |
| §6, "the single obstruction … in exactly one place" | **GAP (wording):** (RL-1) is used in two places, M2.1 and M2.4 step 3 (§5) |
| §6, "why no proof of (NC)" (CHECKED) | consistent with what I could check; not re-derived |
| m2py | reruns identical. Docstring labels are wrong: (A) is M2.5, not M2.3; (B) is M2.4, not M2.2. In (B) world 1 is additive, so the new content (a world 1 without (NC)) is not exercised |

### M3

| Item | Verdict |
|---|---|
| **M3.0 normal form (two rank steps per {+,0,−} pair)** | **CORRECT** |
| M3.1 (K3.1 on the ladder, including the adds-up clause) | CORRECT |
| **M3.2(a)** | The structural claim (endorser = charge on Γ_k = pair (ν^s, ν^w)) is CORRECT. **GAP:** "nothing in the axioms reduces the pair" is asserted without a witness. A one-line witness and a restricted strong form are given in §6.2 |
| **M3.2(b) (incompatibility)** | **CORRECT as an implication.** But on (Av)-domains it is vacuous, because M3.10 leaves no non-degenerate fixed point to be incompatible with. Its non-vacuous remnant is a weak inequality valid at every fixed point (§6.2) |
| M3.2(c) | CORRECT |
| M3.3 (absorption on the ladder) | CORRECT |
| **M3.4 (fixed point on every decomposable domain)** | **CORRECT**, all four items |
| **M3.5 (Claim B2.0; Cor. D1.7)** | **CORRECT.** Documentation GAP: the supporting assessment ψ must be identified with the ladder field ψ^{ν̂} (§6.5) |
| **§4, Theorem gm audit** | The "Prop. necessary(a) iff E = ∅" analysis is CORRECT. "gm uses the axioms only through Prop. necessary (a)–(d)" is CHECKED only and not re-verified here. **Not load-bearing:** M3.8 covers E = ∅ |
| **M3.6 (local one-sidedness)** | **CORRECT**, (a)–(e). Step (c)3 is stronger than stated (§6.7) |
| M3.7 | CORRECT. In (c), the third item rests on the CHECKED off-E transfer of R4 Thm B (D1 imports); label it so |
| **M3.8 (route I1 off chords)** | **CORRECT given (C2), (C3).** Every replacement was checked (§6.9) |
| **M3.9 (CHECKED)** | **CHECKED stands; not upgraded.** Checklist: (i) supported; **(ii) GAP (fixable)**, Thm PL with approximate walls is only sketched; (iii) acceptable at CHECKED. (Av) appears in the statement but seems not to be used, which matters for M3.C (§6.10) |
| M3.10, M3.10′ | CORRECT modulo M3.9 (and modulo M3.6–M3.8, now read once). L3.1(a) is now refereed CORRECT (L23_referee); the note still says "not yet refereed" |
| **M3.11** | **GAP (fixable):** "wrong-blindness never creates a tie at a vertex" is false on Λ^s_k ∩ Λ^w_k and on {+,−} pairs. The consequence e_k ∈ K needs an extra hypothesis (§6.12) |
| **Conjecture M3.C** | Well posed, but **incomplete as a reduction**: N21.6 needs (PC), (NS), which come from M3.9, and M3.9 is stated under (Av) (§6.13) |
| m3py | reruns identical |

### Net effect, and the nearby results available

1. **M2 + L4_referee (PROVED at the standard of L4.9 and Proposition R; case (II) CHECKED).** Under (H_U) on M_U,
   suppose worlds 2 and 3 satisfy (RL) and world 1 is arbitrary (strongly (M1) allowed). Then T1 can be c-Bayes for
   the forced-limit shadow φ* only at p* = e₁, with Λ♮ ⊋ E₁(T1) ∩ M.
   - This is configuration (V) and nothing else.
   - It is strictly more than M2.6 states, and I recommend it as M2's main theorem.
2. **M3 (PROVED except M3.9, CHECKED).** On every decomposable domain with (LF) and (Av), every cover of T1 in which
   all worlds satisfy (NC) has a ladder-blind world. M3.10′ follows from it: (M0) is closed there.
   - Both items stand at this status.
   - M3.5 closes B2_referee's documentation GAP on Claim B2.0.
3. **Not claimed by either note, but suggested by putting them side by side (CONJECTURE).** M2's forced-KKM device
   should transfer to the ladder. Applied with partners that have strictly positive leading ladder densities, it would
   give M3.4 for a world 1 failing (NC) on (Av)-domains, exactly as M2.6 does on M_U.
   - The needed perturbation is B₊/B₋ on a set where all partners agree against world 1.
   - It changes partner ladder costs by s + w > 0.
   - I have not checked closed sections or lower semicontinuity on the ladder.

---

## 1. M2 §§1–2: (RL), M2.1–M2.3

### 1.1 Setting
- **"Regular" on M_U** is "accepts a.e. nonnegative gamble of U" (write-up Def. addup). So P_j △ A, B△W and T1 △ W
  (A, W ⊆ M) are regular, and every regularity claim in M2 holds.
- **Competitiveness** means "against every X ∈ M_L" (write-up §2). Lemma IC (R11, refereed R13) gives T1 competitive on
  Ω under (LF) and K ⊆ Δ°. So the forced pair (T1, Y) with S = Ω is legitimate.
- **Leading density ⇒ (RL).** (L1) is (RL-1), restricted to regular pairs. B1.0 is (RL-2). Additive worlds and their
  lexicographic refinements satisfy both.

### 1.2 M2.1: CORRECT
- Suppose liminf_m ψ_j(C_{q_m}) < s < ψ_j(C_q).
- The model Y = P_j △ A (A ⊆ M, ρ_jμ(A) = s + η, by atomlessness) is regular. (RL-1) gives C_{q_m} ⪯_j Y on a
  subsequence.
- (S) gives a closed section at world j, so C_q ⪯_j Y.
- (RL-2) gives ψ_j(C_q) ≤ s + η, for every small η. This is a contradiction.

### 1.3 M2.2, M2.3: CORRECT; one wording GAP
- **Step 1.** (RL-2) contraposed gives C ⋠_j X at j ∈ S ∖ {1}. Competitiveness on S then leaves world 1.
- **Step 2.** liminf ψ_j(C_{q_m}) > ψ_j(X) at the finitely many j ∈ S ∖ {1} gives a common tail of forced pairs
  (supp q_m = S, so C_{q_m} is competitive on S). World 1's closed section on Δ then gives C_{q*} ⪯₁ X. Note that
  1 ∈ supp q* is not needed.
- **Step 3.** X′ = C △ supp δ′ is regular, and 1_{E₁X′} − 1_{E₁C} = δ′. By K2 (1.1) on the four measures
  ρ_jμ|_{A_{1j}∩M}, ρ_jμ|_{R_{1j}} applied to δ′^±, one gets ψ_j(X′) − ψ_j(C) = f(ψ_j(X) − ψ_j(C)).
  `ref_checks.py` (4) confirms the identity in fractional form.
- **Step 4 (limit pairs, author's risk 2).**
  - ψ_j(X′) ≤ (1−f)L_j + fψ_j(X) < L_j. This uses ψ_j(C_{q*}) ≤ L_j (M2.1) and f > 0.
  - So (C_{q*}, X′) is a limit pair along the same sequence, which has constant support S. Step 2 then applies.
  - CORRECT.
- **M2.3.**
  - K2.1 needs a finite family of atomless finite measures ≪ μ containing μ|_U. ℳ qualifies; the measures are the same
    for every member.
  - K3.1(a) is pure Hahn–Banach against cone 𝔊 + L^∞₊ (K3_notes §2), so it holds for any family of bounded functions.
  - 𝒩(𝔉𝔏) is convex and norm-closed, so (F2) gives φ*.
  - 𝔉𝔏 ⊆ 𝔚₁ (M2.2), hence 𝒩(𝔚₁) ⊆ 𝒩(𝔉𝔏) and Λ♮ ⊆ Λ₁.
- **GAP (wording).** "These hold with no hypothesis on world 1 beyond strict (G) and (IB)" (M2.3, and §0 for M2.6) is
  false as written. Step 1 uses competitiveness of C_q and of T1 at world 1. Step 2 uses world 1's closed sections.
  Both are part of (S) and of the standing hypotheses, so nothing is lost.
  - **Fix:** "with no (NC), additivity or endorsement hypothesis on world 1".

---

## 2. Theorem M2.4: CORRECT (author's risk 1)

**Step 0.**
- Q^{(1)} = {σ_j = −σ₁, j ≠ 1} ∩ M contains a neighbourhood of (L, −1, …, −1) for large L, since min_{K′} m₁ > 0 with
  K′ compact. For n = 3 it is Q₁. It is non-null, so W ⊆ Q^{(1)} ∖ D_m exists for large m.
- On W all partners agree. B₊ (world 1's side) errs at every j ≠ 1, and B₋ errs at world 1. Hence
  ψ_j(B₊) − ψ_j(B₋) = ρ_jμ(W) > 0 at **every** j ≠ 1, because ρ_j > 0 a.e. at every partner.
- The world-1 cost moves by at most φ(W) ≤ ρ₁μ(W) + π(M ∖ D_m) ≤ η + 2^{−m}.

**Step 1 (KKM).**
- The F_j (j ≠ 1) are closed by (S), and F₁ = cl O is closed by definition.
- Covering condition. Fix q. Competitiveness of C_q on supp q against B₊ gives a witness i ∈ supp q.
  - If some witness i ≠ 1 exists, q ∈ F_i.
  - If not, every j ∈ supp q ∖ {1} has C_q ⋠_j B₊. Then the witness is 1, so 1 ∈ supp q and q ∈ O.
- So q ∈ ⋃_{i∈supp q} F_i for every q. That is the face-wise KKM hypothesis, and the lemma gives q* ∈ ⋂F_i.

**Step 2.** C_{q*} ⪯_j B₊ is relevant, so (RL-2) gives ψ_j(C_{q*}) ≤ ψ_j(B₊) ≤ ψ_j(B) + η.

**Step 3 (the margin).**
- There are finitely many supports, so q_m ∈ O, q_m → q*, can be taken with constant support S. S ∋ 1 because O
  requires it.
- For j ∈ S ∖ {1}, (RL-1) contraposed reads C ⋠_j X ⇒ ψ_j(C) ≥ ψ_j(X), with C ∈ C_L and X regular. This gives
  ψ_j(C_{q_m}) ≥ ψ_j(B₊) for all m, hence L_j ≥ ψ_j(B₊) = ψ_j(B₋) + ρ_jμ(W) > ψ_j(B₋).
- The strict inequality the definition of a limit pair requires is supplied by the perturbation, not by the limit.
  That is exactly why B± are introduced.
- (C_{q*}, B₋) is a limit pair, so φ(E₁C_{q*}) ≤ φ(E₁B₋) ≤ φ(E₁B) + η + 2^{−m}.
- **One point worth stating.** q* may have 1 ∉ supp q*, e.g. on the face opposite e₁. This is harmless: the limit-pair
  definition constrains only the approximating sequence, and world 1's closed section is on all of Δ (M2.2 step 2).
- The case S = {1} is correctly handled.

**Step 4.**
- The coherent infimum is ≤ the regular infimum + O(η + 2^{−m}). Lemma L4.0 has a proof that is n-free.
- **Cosmetic.** The index m is used both for D_m and for q_m. Rename one.

---

## 3. Proposition M2.5: CORRECT (author's risk 3)

- **Step 1.** W ⊆ M ∖ D_m, and D_m is decreasing (K3.1(b) Step 2). So δ_W = 0 on every D_{m′} with m′ ≥ m, and
  |π(δ_W)| ≤ π(M ∖ D_{m′}) ≤ 2^{−m′} for all m′. Hence **π(δ_W) = 0 exactly**, not merely asymptotically.
  - Forcedness of (T1, Y_W) through S = Ω needs T1 ∈ C_L (from (H_U)) and Lemma IC.
- **Step 2.**
  - v(W) = ∫_W χc dμ was checked sign by sign: on D_{T1} the world-k error indicator changes by σ_k, and off D_{T1}
    by −σ_k.
  - The range is convex and compact by Lyapunov (c ∈ L¹, atomless).
  - Separation from the open negative orthant N gives w ≠ 0 with w·r ≥ α ≥ sup_N w·n. Since N is a cone with 0 in its
    closure, w ≥ 0 and α ≥ 0. So the weight lies in Δ after normalisation.
- **Step 3.** For m ≥ m₀, χw^m·c ≥ 0 a.e. on M ∖ D_{m₀} (the sets increase). Pass to the limit, then take the union
  over m₀. ⋂D_m is null.
- **Step 4.** I checked the three cases.
  - On (−,−,+) ∩ D_{T1} with p*₃ = 0 < p*₂: p*·c ≤ −p*₂ρ₂ < 0, which is a contradiction.
  - The other two cases are the same.
  - The surviving cases are p* ∈ Δ° and p* = e₁. At e₁ the condition is exactly ρ₁ = 0 on E₁(T1) ∩ M.
- NUMERICS (A) reproduce the facet-switching weight. (The docstring calls this "Prop. M2.3".)

---

## 4. Theorem M2.6: CORRECT, and sharper than stated

**The proof.**
- φ* gives (γ₀) by M2.4.
- Since c ≠ 0 a.e. (ρ₂ > 0), L4.1.2's directional-limit argument makes every B_q coherent. This is exactly the
  hypothesis that L4_referee §1.3 attaches to that clause.
- M2.5 gives T1 = B_{p*} ∪ S.
- K3.7(β), (β′) and (Q1) need only (γ), ρ₂, ρ₃ > 0 and ρ₁ > 0 off Λ₁ (re-read in L4_referee §4.1). So (B1) holds
  with Λ₁ := Λ♮.
- If Λ♮ is null, p* = e₁ is impossible (E₁(T1) ∩ M is non-null), so p* ∈ Δ°. M0closed(a) applies, by the argument of
  L4_referee §2.

**Sharpening.**
- L4_referee §4.2 proved **Proposition R**: under (B1) with p* ∈ Δ°, (I₂) and (I₃) are impossible. Case (II) is then
  excluded at CHECKED status (L4 §5.4, confirmed in L4_referee §5).
- Proposition R uses only the field: B_{p*} coherent, the shell lemma, and carrying(c), (d) on F₁.
- M2.6 supplies exactly (B1). Hence:

> **M2.6′.** Under (H_U), with worlds 2 and 3 satisfying (RL) and world 1 arbitrary, either (H_U) is contradictory, or
> p* = e₁ and Λ♮ ⊋ E₁(T1) ∩ M (configuration (V); the equality case is excluded by Example L4.7, which needs only (B1)).

  Status: PROVED except case (II) (CHECKED); Proposition R has one reading.

**Corrections.**
- "L4.9 itself is unrefereed" and the reference to (I₂)/(I₃) in §0, §5 and the table are out of date.
- "Q_M2 … second answered **no** by M2.6" overclaims. What is shown is narrower: a world failing (NC) next to two (RL)
  partners creates no configuration beyond those available to (NC) worlds. After the sharpening, that is (V) alone.
  Whether (V) can occur is open.

---

## 5. Proposition M2.7 and §6

- **M2.7: CORRECT.** I re-read L4.1:
  - step 1 endorses only kkm dominance pairs, and Theorem kkm supplies a *selected* dominator;
  - step 3 endorses only T1's localized out-comparisons;
  - steps 2 and 4 use no endorsement;
  - K3.1(a) applies to the family 𝔇_k ∪ 𝔗_k.
- "𝔗_k alone satisfies (NC⁺)": with one base, the error sets form a chain, so N17.3 Lemma 3.1 applies. CORRECT.
- **GAP (wording): "(RL-1) is needed in exactly one place, step 3".** (RL-1) is also the engine of M2.1, and M2.1 is
  what makes limit pairs divisible (M2.2 step 4).
  - Without (RL-1) at a partner j, the step-3 conclusion is lost, and so is lsc of ψ_j(C_q). Then the sub-moves of a
    limit pair need not be limit pairs.
  - The obstruction is still single in substance, since both uses are about the same partner. But "exactly one place"
    should read "M2.1 and M2.4 step 3".

---

## 6. M3

### 6.1 Normal form (M3.0, M3.1): CORRECT (priority 1)
- Γ_k = {(g,j) : g ∈ M, 1 ≤ j ≤ |A′(g)| − 1} does not depend on k. The steps are:
  - two steps for {+,0,−} pairs (silence, then wrong acceptance);
  - one step for {+,0}, {0,−} and {+,−} pairs;
  - none for forced advice.
- The ladder profile is the staircase encoding of world-k rank. So (a) and (b) are immediate.
- The table of §1 was checked: c_k ∈ {s_k, −w_k}, c′_k ∈ {−w_k, s_k}, d_k = ±(s_k + w_k).
- **Definition to flag.** "Regular" now also requires × on a null set only. This differs from the M_U definition and
  should be marked as a definition.
  - It shrinks 𝔚_k, which only weakens (NC_k).
  - The Gap and absorption arguments use the same class consistently (X_m in M3.3 gives no ×), so nothing breaks.
- **M3.1, last clause.** ν̂(A × {j}) = ∫_A (λ_k(g,a_j) − λ_k(g,a_{j−1})) dν_k telescopes to ν_k(λ_k a_X − λ_k a_B).
  - For bounded f ≥ 0, (fν)_c = fν_c, because fν_p ≤ ‖f‖ν_p is purely finitely additive.
  - So the density is ρ_{ν_k} times the λ-increments. This is > 0 a.e. by N19 Lemma R1 and strict guidance of λ_k.
  - CORRECT.

### 6.2 M3.2 (priority 1)
- **(a), the structural claim: CORRECT.**
- **(a), "no axiom reduces the pair to one graded charge": GAP.** The sentence is asserted without a witness, and it
  has two readings.
  - **Weak reading: endorsers need not be graded.** A one-line witness suffices. Take an additive world with ladder
    densities (s, w), w ≠ s on a non-null set. Its own ladder charge (s, w)μ is an endorser and is not graded. Such
    systems satisfy the axioms (e.g. ℓ(bad) = 3ℓ(silent) with coherent interior Bayes models) at the status of Thm
    ccibu.
  - **Strong reading: some world has no graded endorser.** This holds in a restricted form.
    - Let B ∈ C_L be silent on a non-null set A₀ of two-sided pairs at world k, with w > s on a non-null part of A₀.
    - Move B to the correct advice on A ⊆ A₀ and to the wrong advice on A′ ⊆ A₀. The comparison B ⪯_k X holds iff
      w(A′) ≥ s(A).
    - A graded σ must then satisfy σ(A′) ≥ σ(A) whenever w(A′) ≥ s(A). At a density point with w > s, this forces
      σ = 0 there.
    - So no graded endorser is positive on that part of A₀.
    - (I found no argument for the case w < s: the analogous comparison needs a base that errs and is correct near the
      same point.)
  - **Fix:** cite the weak witness, and state the strong form only as above.
- **(b): CORRECT as an implication.**
  - Adding the two silence-optimality inequalities gives Σp*(s − w) ≤ 0 (`ref_checks.py` (2): the identity
    c·p + c′·p = p·(s − w)).
  - Equality forces c·p* = c′·p* = 0, so +, 0 and − are all optimal. B2.1(d) excludes **every** triple tie at p*,
    including the degenerate case c ∝ −c′ that arises when s = w. B2's "apex" requires c ∦ c′, but (d) is stated for
    the advice sets themselves, so the case is covered.
- **On the headline "incompatible with every non-degenerate fixed point".** On (Av)-domains, M3.10 (at its status)
  says there is no non-degenerate fixed point at all, so (b) adds nothing there.
- **The non-vacuous remnant (PROVED by the same two lines).** At **every** fixed point, degenerate ones included,
  Σ_k p*_k (w_k − s_k) ≥ 0 a.e. on T1's silent two-sided pairs.
  - This weak form is what M3.11's remark "w cannot vanish at every world on T1's silent set" can legitimately cite.
    That remark currently cites (b), which needs strict guidance.
  - Correct form: on T1's silent set, w can vanish at every world of supp p* only where s does too.
- **(c): CORRECT.**

### 6.3 M3.3: CORRECT
- π^t_a is the image of a restriction of π under the ≤ 2-to-1 projection Γ → M. It is purely finitely additive by
  K3.1(c)(F1): push the small sets E forward.
- The upper and lower bounds are as in L4.0. Coherent models of 𝓜 give a measurable selection of A′ a.e.

### 6.4 M3.4: CORRECT (priority 2)
- **1.** Theorem kkm holds for any ranking with (LA) and (S), on any domain.
- **2.**
  - Coherent ∩ 𝓜 is compact in measure, since 𝓜 is closed in measure.
  - ψ^t is continuous in measure, by dominated convergence with an L¹ envelope.
  - So the coherent minimiser exists at **every** t ∈ Δ.
  - Strict guidance gives tie lines {v·q = 0} with v mixed, never ∝ 𝟙, and Tonelli gives (γ).
  - D♭_q is coherent (countable meet of generic D^θ_q), though it is **not** Bayes at d-ties. The note claims only
    coherence, which is right.
- **3.** H1.1 with finitely many alternatives:
  - {∫Σ_a f_aΔℓ_a : f_a ≥ 0, Σf_a ≤ 1} is convex, and its values are attained by indicators (Lyapunov);
  - the separating weight is ≥ 0, as in §3 above;
  - T1 ⪯_k Y at some k by the tie with a competitive C_p (or directly by Lemma IC).
- **4.** Each Δℓ_k ≤ 0 and Σp*_kΔℓ_k ≥ 0, so every term vanishes.
  - The ladder-step bookkeeping (s and w versus w alone versus s alone) is right.
  - The non-null witnesses (accepted gambles near r_ij, and silent h − s𝟙 near the middle arc of F_l) were checked
    against the facet sign patterns.
  - Silence is available by (LF), so strict guidance forces p* ∈ Ω.

### 6.5 M3.5: CORRECT; documentation GAP
- **The identification M3.5(a) needs, which the note leaves implicit.**
  - With ν̂ as in M3.1, ℓ^{ν̂}_k(g,a) = ρ_k(g)(λ_k(g,a) − λ_k(g,a₀(g))), where a₀ is the rank-0 advice.
  - So the supporting assessment ∫λ_kρ_k and the ladder field differ by a function of g alone. They have the same Bayes
    models, ties and E.
  - Off the ladder (unanimous pairs, ×) both are strictly guiding, and correct advice is optimal.
- With this, M3.4 gives (α*) (interior, from strict guidance), (β) ((γ₀)), (γ) and (δ) (unique vertex minimiser,
  coherent by (γ₀)).
- B2_referee's GAP on B2.0 is closed. D1_referee §8 needs only (α*), (γ) and ρ > 0, so Cor. D1.7 is at the status of
  Thm D1.
- Import status: K3.1, H1.1 and kkm, each read once or more.

### 6.6 §4, the Theorem gm audit (priority 3)
- **Correct:**
  - the fixed-point field has integral penalties with an L¹ envelope, satisfies Prop. necessary (b), (c), and (d) when
    non-degenerate, and is strictly guiding iff non-degenerate;
  - "(a) iff E(ψ) = ∅": the "if" uses (γ₀) and continuity of Bayes models at q ∉ E.
- **The CHECKED claim** (gm's proofs touch (LA), (S), (C) only through Prop. necessary and the field) was not
  re-verified here.
  - It is not load-bearing. M3.10 runs through M3.8, which includes E = ∅.
  - The alternative route through Thm ccibu is also correct: at E = ∅, T1 is the unique interior Bayes model, hence
    undominated and in C_L. Its status is that of ccibu.

### 6.7 M3.6: CORRECT (priority 4)
- **(a)** For |q − p*|₁ < r, the optimum is unchanged off G_r = {margin ≤ 2r·env}, and G_r decreases to a null set.
  This is also true of D♭.
- **(b)**
  - K ↦ 1_{D_K} is a homeomorphism from a compact space onto its image (R1 Prop. 3.1).
  - Inner parallel body: if x ∈ T1, dist(x,∂T1) > η and x ∉ K, then pushing x by η′ ∈ (η, dist) along the separating
    normal gives a point of T1 at distance > η from K. CORRECT.
- **(c)**
  - Step 1: when the tie is three-way, the set of directions favouring −h is an open sector, not a half-plane. It still
    has positive measure, so Fubini applies.
  - Step 3 is **stronger than stated.** "c′ − a·d ∈ ℝ𝟙 with a > 0" is impossible for every mixed h: it would need
    b < 0 at a positive coordinate and b > 0 at a negative one. Non-parallel closed half-planes always meet with
    interior.
    - So either W(h) = ∅ or W(h) = cl R(−h). `ref_checks.py` (1): 20 000 random instances, W ≠ ∅ ⇒ R(−h) ≠ ∅, 0
      failures.
  - Step 4 checked.
- **(d)** The three cases check, using |P_K − P_{T1}| ≤ d_H·|g|. If T1 strongly accepts g, then + must be q-optimal
  (otherwise no coherent q-Bayes model accepts g), and some positive-measure set of directions breaks the tie away from
  +. The compactness step uses ∂D_{T1} ∖ 0 ⊆ cone(int N₀).
- **(e)** On B₂ and for a.e. g near g₀ − t𝟙, acceptance is the half-plane {c(g)·q > 0}, with its boundary line if
  g ∈ A. That is the hypothesis of the first half of quasilin(a) and of its mirror image.

### 6.8 M3.7: CORRECT
- (a) {P^♭ > 0} is open because K^♭ is upper semicontinuous: strict optima persist. Two open convex sets that agree
  a.e. are equal.
- (b) Advice converges a.e. at q ∉ E.
- (d) For |S| = 2, test with (η, η, −1). At a vertex both acceptances are available under (Av).
- **Label.** (c), third item, uses R4 Thm B at q ∉ E, which is a CHECKED import (D1 §1). M3.8 does not use it.

### 6.9 M3.8: CORRECT given (C2), (C3) (priority 5)
- **Prop. E, step 3.** At q ∉ E with c(g)·q > 0, + beats silence. So a.e. nearby g has ±g ∈ D_{K_q}, and strict
  straddling (an open condition) is excluded for every g in the open set.
- **Step 4** is the mirror case.
- **Thm R.** Limits through Ω ∖ E suffice. S(g) is closed, and R(g) = {P(·,g) > 0} at q ∉ E (M3.7(a)).
- **No atoms among pinned gambles.**
  - ℓ_g determines g up to a positive factor, because aff Δ spans ℝ³. Two distinct edge points then fix the c-line.
  - So each of the countably many atom lines is the c-line of a null set of pinned g.
  - B2 §2 gives E ⊆ atom lines ∪ a countable set, so a generic c-chord meets E countably.
- **Lemma S** at q_n ∉ E on the c-chord, and the window point q ∉ E (the open side of C₁ minus a null set): CORRECT.
- **Lemma veccluster (C3)** is a statement about the vectors c(g). Its proof needs only the B₁ half-plane charts
  (M3.6(c)) and the cluster clause (from M3.9).
- The normalisations p* = u and x = x₊ preserve strict guidance, (γ₀), (LF) and (Av), because σ fixes D_{T1}.

### 6.10 M3.9 (CHECKED): label confirmed, with one fixable GAP (priority 6)

Against the note's own checklist:
- **(i) Chords accumulating at p\*: supported.**
  - The write-up's N₀ paragraph (N27 inventory, re-derived in N27_referee) states that every gamble used in §5 lies in
    the compact collar N₀. So M3.6(c)–(e) cover every near-facet use on B₂.
  - The non-local uses are UVN and quasi-concavity on Ω. Both are available for K^δ (D1.1(b), (c)).
  - For K^♭, UVN follows from M3.7(d), since K^♭_q → {e_l} under (Av).
  - Chords through p* are impossible (frozen ties, p* ∉ E), so lines through p* meet E ∩ B₂ countably. That is
    chainchords' only use of p* ∉ E.
- **(ii) Thm PL with approximate walls: GAP (fixable).**
  - R10b's Thm PL ends with a nearest-point argument on the **closed** set Z_v ∪ Z_{v′}. The approximate walls
    {q ∉ E : K_q ⊆ B(v,η)} are not closed.
  - The note replaces the nearest point by the first point of cl β_{v′}. That is the right idea, but two things must be
    written out.
    - (a) Lemma P and Lemma M are then needed along *specific* segments [o, A]. D1.6 proves its wall statement only for
      a.e. (o, y). Fix: O and the ball B_A around an approximate-wall point A ∉ E are open, so o and A can be chosen
      generically (transversal to atom lines, off non-generic points).
    - (b) In the case Q ∈ E, D1.6 case (B) must be restated for the segment toward A, not toward V_l.
  - Neither looks hard. Until they are written, Lemma 3.2 of N28 for (γ)-fields is not at CHECKED-plus standard.
- **(iii) R23.1 for K^♭ with chords in the ball: acceptable at CHECKED.**
  - PL2 for K^♭, chords allowed, is chainchords' item, and B2 Lemma 7 (one tie type, M3.6(d)) replaces Lemma ball.
  - The α-point is p*, with K^♭_{p*} = T1.
- **Additional point.** M3.9's statement includes (Av), but I found no step that uses it. Its uses of UVN go through
  D1.1(c) under (LF), and edge confinement (M3.7(d)) is used only in M3.8. If it is indeed not used, drop it. §6.13
  needs this.

### 6.11 M3.10, M3.10′: CORRECT modulo M3.9 (priority 7)
- **The logic.** Strict guidance ⇒ M3.4 ((γ), p* ∈ Ω) ⇒ D1 (p* ∉ E) ⇒ M3.6–M3.9 ⇒ M3.8 contradiction. So some ladder
  density vanishes on a non-null set, and ν* gives the canonical blind set.
- **The (Av) clause.** L3.1(a) gives C_{e_i} = {g_i > 0} a.e., and mixed ±g each have a positive coordinate. L3.1(a)
  is now **refereed CORRECT** (L23_referee §B.1); update the note.
- **M3.10′** follows through M3.5.
- **Status line.** "PROVED except M3.9 (CHECKED); M3.6–M3.8 one reading (this report); D1 one reading with repairs."

### 6.12 M3.11: GAP (fixable) (priority 7)
- **At e_k the losses are 0, s_k, s_k + w_k.**
  - On Λ^s_k ∩ Λ^w_k all three advices cost 0. `ref_checks.py` (3) shows the three-way tie.
  - On {+,−} pairs the only ladder step is the wrong step, and its blindness ties the two acceptances.
  - So "wrong-blindness never creates a tie at a vertex" is false on those sets.
  - The consequence "D_K ⊆ D_{e_k}, i.e. e_k ∈ K" fails if a directional fan model accepts a world-k-wrong orientation
    on a non-null doubly-blind set.
- **Fix.** "Vertex ties at e_k occur exactly where the ladder step adjacent to the correct advice is blind. Wrong
  acceptance is optimal at e_k only where every step is blind." Then:
  - add "Λ^s_k ∩ Λ^w_k null (and no blind {+,−} step)" as a hypothesis for the three bullets;
  - or prove that set null at a fixed point. I do not see how to do that from M3.4.4, which constrains blindness only
    on joint T1-error sets.
- The pointer to L3.6(b) should note that L23_referee rates L3.6(b), (b′) GAP (fixable).

### 6.13 Conjecture M3.C (priority 8)
- **The statement is well posed:** N21.6 and N21.7(a), (b) for non-degenerate (γ₀)-fields.
- **The claimed reduction is incomplete.** "Given M3.C, Thm M3.10 holds on every decomposable domain with (LF)" needs
  (PC) and (NS) as inputs to N21.6. These come from M3.9, which is stated under (Av), the very property M3.C is supposed
  to yield.
  - **Fix:** prove M3.9 without (Av) (§6.10 suggests it does not use it), or include (TS), (PC) and (NS) without (Av)
    in the conjecture.
- With that fix the logic is right.
  - Without (Av), M3.C contradicts the domain, as Cor. TSalways(b) does for additive covers.
  - With (Av), M3.10 applies.
  - The U-domain case also falls under M3.C, so it does not need L4.1.

---

## 7. Requested changes

**M2.**
1. M2.3 and §0: replace "no hypothesis on world 1 beyond strict (G) and (IB)" by "no (NC), additivity or endorsement
   hypothesis on world 1" (§1.3).
2. M2.4: rename one of the two indices m. Add the remark that q* may have 1 ∉ supp q*, and why that is harmless (§2).
3. M2.6: state M2.6′ (only configuration (V)), citing L4_referee Proposition R. Delete "L4.9 is unrefereed" and the
   (I₂)/(I₃) clause. Reword Q_M2's "answered no" (§4).
4. §6: "(RL-1) is used in M2.1 and in M2.4 step 3", not "exactly one place" (§5).
5. m2py docstring: (A) is M2.5, (B) is M2.4. Note that (B) has an additive world 1.

**M3.**
6. M3.0: flag the general-domain definition of "regular" (× null) as a definition (§6.1).
7. M3.2(a): give the one-line witness (an additive world with w ≠ s). State "no graded endorser" only in the
   restricted form of §6.2. M3.2(b): add the weak inequality for all fixed points, and note that (b) is vacuous on
   (Av)-domains given M3.10 (§6.2).
8. M3.5: write the identification ψ = ψ^{ν̂} + (function of g) (§6.5).
9. M3.6(c) step 3: state the stronger dichotomy W(h) ∈ {∅, cl R(−h)} (§6.7).
10. M3.7(c): label the R4 Thm B item CHECKED (import).
11. M3.9: write out Thm PL with approximate walls, with generic o and A (checklist (ii)). Drop (Av) from the statement
    if it is unused (§6.10).
12. M3.10: update L3.1(a)'s status to refereed CORRECT. Revise the status line (§6.11).
13. M3.11: restate it with the first-step blindness and a doubly-blind hypothesis (§6.12).
14. M3.C: add M3.9 without (Av) to the conjecture, or prove it (§6.13).

## 8. Files
- `m23ref_py/m2_rerun.out`, `m23ref_py/m3_rerun.out`: reruns, identical to `m2py/m2_checks.out` and
  `m3py/m3_checks.out`.
- `m23ref_py/ref_checks.py` (+ `.out`), four checks:
  - (1) W(h) ≠ ∅ ⇒ R(−h) ≠ ∅, 20 000 instances, 0 failures;
  - (2) the M3.2(b) identity, 0 violations;
  - (3) the doubly-blind three-way tie at a vertex (M3.11 GAP);
  - (4) the M2.2 sub-move identity, 0 violations.
