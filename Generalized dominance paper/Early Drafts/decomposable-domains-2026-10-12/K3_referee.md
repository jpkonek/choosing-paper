# Referee report on K3_notes.md (round 19)

15 Oct 2026. Adversarial reading. I did not write K3.

- **Read against:** BRIEF16; N17_notes §0, N17.1, Lemma 3.1; Q12_referee (N1–N4, the Q1.2 repair); D2_notes; F1_notes
  §§2–3 (F1.2, F1.4); H1_notes (H1.0–H1.3); H12_referee §1; H2_notes §1 and H2.4; E1_notes §2.1–2.3; write-up §§2–3,
  §7.7 (Prop. M0, Thm. Estructure, Lemmas quasilin/ball, Props. crosspin/chainchords/carrying, Thm. M0closed), §8.5.
- **Verdicts:** CORRECT / GAP (fixable, with the fix) / WRONG.
- **Scripts:** the three author scripts were rerun with `python3 -I` from `k3py/`. All three outputs are
  byte-identical to the stored `.out` files; the reruns are in `k3ref_py/*.rerun`. My own check is
  `k3ref_py/between_diag.py` (+ `.out`). No verdict rests on numerics.

---

## 0. Verdicts

| Item | Verdict |
|---|---|
| K3.1(a) Hahn–Banach endorser | **CORRECT** |
| K3.1(b) localization of the p.f.a. part; CA part endorses off it | **CORRECT** |
| K3.1(c) blind set Λ; "adds up ⇔ Λ null" | **CORRECT**, with one unstated presupposition: (NC_𝔚) (§1.3) |
| K3.1(d) Λ_∞, D^∞, D̂, ρ_∞ | **CORRECT**. "Canonical D̂" is a wording slip: Λ_∞ is canonical, D̂ and ρ_∞ are not (§1.4) |
| K3.1(e) (S_int) ⇔ Λ_∞ null | **CORRECT** |
| K3.1(f) ratio-certificate characterization | **CORRECT** (notation of 𝒦′ should be clarified, §1.5) |
| K3.2 (E) vacuous; (E_b) ⇒ (S); classification ⇔ (N) = ∅ | **CORRECT** |
| K3.3 tilted world: every axiom but closed world-1 sections; (M2); Λ_∞ = M; ¬(S) | **CORRECT** (every axiom re-derived, §3) |
| K3.3 reading / §0 item 3 "must use closedness against certificates whose positive parts do not pairwise meet" | **GAP (wording)**: the provable statement is narrower (§4.2) |
| K3.4 (pairwise-meeting families are localizable) | **CORRECT** as a lemma |
| K3.4 "Consequences", last two bullets | **GAP (non sequitur, flagged by the author as "no theorem")**: "not pairwise meeting" does not give "pairwise disjoint" (§4.2) |
| K3.5 patch theorem | **CORRECT** |
| K3.5′(a), (b), (c) | **CORRECT** |
| K3.5′ residual (R-i)/(R-ii) and "case (ii) closed except…" | **CORRECT** but (R-ii) is the literal negation of (P2); a sharper reading is available (§5.3) |
| K3.6 (sheltered or shadowed) | **CORRECT** |
| K3.7′ ("between" lemma) | **CORRECT**. NUMERICS diagnosis mislabelled (§6.1) |
| K3.7 first sentence, (α), (β), (β′), (γ) | **CORRECT** |
| Reduction to Q_A | **CORRECT**. Q_A is well posed; I add necessary conditions and locate exactly where M0closed(a) breaks (§7, PROVED here) |
| K3.8 (Λ_D initial segments next to an additive world) | **CORRECT** |
| CONJECTURE K3.C | Correctly labelled. **Evidence bullet 2 is overstated (GAP)**: F1.4 does not exclude chain-free *ratio* certificates, because g may concentrate (§8) |
| Q_K3 and its two branches | **CORRECT**; the "No" branch can be sharpened (§5.3) |

**Net.** Nothing is WRONG. K3.1 is a clean, complete execution of the Hahn–Banach / Yosida–Hewitt route, and K3.5–K3.7
are genuine results. K3.3 is not new mathematics: it is Q12_referee N3 plus the Q1.2 repair. It is a correct and useful
repackaging, and its consequence (any proof of (M2) ⇒ (S) must use closed sections at the failing world) is right. The
weak points are interpretive: the K3.4 consequences and the K3.C evidence.

Editorial (requested throughout):
- **"(S)" is overloaded.** It is the axiom "closed competitive choice" (write-up §2) and K3's class "localized σ-finite
  endorsement". Both appear in K3.8 (hypothesis list vs. conclusion) and in K3.5′(c). Rename the class, e.g. (Loc)
  and (Loc_int).
- **"(γ)" is overloaded.** It is property (γ) of the field, and item (γ) "admissibility" of K3.7. Rename the item.

---

## 1. K3.1 (the Yosida–Hewitt classification)

### 1.1 (a) CORRECT

- If −1 ∈ cl 𝒦 then some δ̂ + f ≤ −1 + η with η < 1. So δ̂ ≤ −(1 − η), and rescaling contradicts (NC_𝔚).
- Separating the point −1 from the closed convex cone cl 𝒦 gives φ ≥ 0 on 𝒦 and φ(−1) < 0. Positivity on L^∞₊ makes φ a
  positive charge vanishing on μ-null sets, and φ/φ(1) ∈ 𝒩.
- **Answer to the brief's question.** The endorser is **bounded** (an element of ba(μ) = (L^∞)*, μ finite on M) and
  **nonnegative**. It is not strictly positive, and K3 never claims or needs strict positivity except in (c), where
  it is handled through Λ.
- Not-(M1) ⇒ (NC_𝔚), since a combination ≤ −1 is an (M1) certificate (M is non-null). So "𝒩 ≠ ∅ in (M2)" is right.

### 1.2 (b) CORRECT

- **Step 1.** λ(A) = inf_{B⊆A}(π(B) + μ(A∖B)) is the lattice infimum π ∧ μ in ba. It is ≤ μ, so it is continuous at ∅
  and hence countably additive. Since π is purely finitely additive, λ = 0. This is the standard characterization of
  purely finitely additive μ-continuous charges (π ∧ μ = 0).
- **Step 2.** D^ν_m = ⋃_{k≥m} E_k is decreasing, with μ(D_m) < 2^{1−m} and π(M ∖ D_m) < 2^{−m}.
- **Step 3.** π(δ1_{D_{m′}}) ≤ 0, since δ ≤ 0 there and π ≥ 0 vanishes on null sets. |δ| ≤ 1 gives
  π(δ1_{M∖D_{m′}}) ≤ 2^{−m′}. Let m′ → ∞.

The "localized endorsement" conclusion is exactly H1.2's hypothesis, with an **integrable** density ≥ 0.

### 1.3 (c) CORRECT, with a presupposition

- (F1) "if": a countably additive λ ≤ π is μ-continuous, so λ = fμ by Radon–Nikodym, and λ(M) ≤ ∫_E f + ε → 0.
- (F2): the truncation and union estimate is right (μ(E) < ε/2, remainder mass ≤ ε).
- The maximal-support argument is right (μ finite; the family of supports is closed under countable unions).
- "Λ null ⇒ adds up": every δ ∈ 𝔚 vanishes on N₊, because B is coherent, X is regular, and both are correct on N₊ at
  every world. So ν* + μ|_{N₊} works.
- "Adds up ⇒ Λ null" is N19 Lemma R1. The proof is re-derived correctly.

**Presupposition (GAP, trivial fix).** (c) says "there is ν* ∈ 𝒩", which needs 𝒩 ≠ ∅, i.e. (NC_𝔚). The standing
hypotheses do not include it, and (M1) worlds may fail it. The same applies to Λ_D in (d): 𝒩(𝔚_D) can be non-empty when
𝒩 is empty.

**Fix.** State (c)–(f) under (NC_𝔚), or set Λ := M when 𝒩 = ∅ (and likewise for Λ_D). Then "Λ_D ⊆ Λ" survives. Nothing
downstream is affected, since K3 only applies (c)–(f) in (M0)/(M2), where (NC_𝔚) holds.

### 1.4 (d), (e) CORRECT

- **Antitone.** D ≤ D′ ⇒ 𝔚_{D′} ⊆ 𝔚_D ⇒ Λ_{D′} ⊆ Λ_D.
- **Directed.** Λ_{D∪D′} ⊆ Λ_D ∩ Λ_{D′}. The essential infimum is realised by a countable subfamily.
- **Diagonal family D^∞.**
  - It is decreasing.
  - μ(D^∞_m) → 0 by dominated convergence for series.
  - D^∞-localized ⇒ D^{(k)}-localized, because D^{(k)}_{m+j_k} ⊆ D^∞_m.
- **D̂ := D^∞ ∪ D′.** A D̂-localized δ lies in 𝔚_{D^∞} and is D′-localized, so ∫ρ_∞δ ≥ 0. The sandwich
  Λ_∞ ⊆ Λ_{D̂} ⊆ Λ_{D^∞} = Λ_∞ is right.
- **(e).** Both directions are right. For integrable ρ, (E2) is ∫ρδ ≥ 0.

**Wording.** §0 item 1 calls D̂ "a canonical family". Only Λ_∞ is canonical (mod null). D̂ and ρ_∞ depend on choices.
Write "some localizing family D̂".

**Observation (not an error).** (N) ⊆ {Λ_∞ non-null} is strict in principle. A world could be (S) with a non-integrable
ρ while Λ_∞ ≠ ∅. I tried the obvious repair: truncate ρ ∧ m and add {ρ > m} to the localizing family. It does not give
(S_int), because the truncation level needed depends on the comparison. So K3 is right not to claim (S) ⇔ (S_int).
This is why Q_K3's "Yes" branch must say "without (S)", as it does.

### 1.5 (f) CORRECT

- **Rates.** ν ≥ cμ|_{B′} ⇔ ρ_ν ≥ c on B′, because cμ|_{B′} is countably additive and ν_c is the largest countably
  additive charge below ν.
- **Duality.** ν ≥ 0 on 𝒦′ with ν(1) = 1:
  - taking f = 0 gives ν ∈ 𝒩(𝔚_D);
  - taking δ̂ = h = 0 gives ν(f) ≥ c∫_{B′} f.
  - The closure criterion and the absorption of h are right.
- **(i) ⇒ (ii).** The case cs < 1 − η contradicts (NC_{𝔚_D}). Otherwise g := f1_{B′}/s satisfies δ̂/s ≤ c − g, since
  f ≥ f1_{B′}.
- **(ii) ⇒ (i).** Use a (c/2)-certificate: ν(g) ≥ c∫g = c.
- The D2 instance (c = ε/μ(c_a), g uniform on c_a) is right.

**Notation.** Write the scalar term of 𝒦′ explicitly as c·(∫_{B′} f dμ)·1. As printed, "cμ(f1_{B′})" reads as a
function.

---

## 2. K3.2 — CORRECT

- **(a).** With 𝒮 = ∅, end-protection reads "S-positive for some S ∈ ∅, or eventually ≥ 0 on every S ∈ ∅". The second
  clause is vacuously true, so every world qualifies. E1.5 does allow "possibly empty".
- **(b).** This is H1 §1's observation. The summable depth choice is possible because each end decreases to a null
  set in a finite measure space. A D-localized δ is S-positive for no S, so it is eventually ≥ 0 by protection and
  eventually = 0 by localization: a base comparison.
- **(c).** Correct. It also shows that the classification "(M1), (E) or (S)" with bare (E) is trivially true, so the
  intended statement must be the (E_b) form.

**Note.** BRIEF16 as filed (43 lines) does not contain the classification "(M1), (E) or (S)" that K3 §0 attributes to
it. Presumably it came from a coordinator message. Cite the source.

---

## 3. K3.3 (the tilted world) — CORRECT

Every claim was re-derived. Notation: A = E₁X ∩ M, N = N₊ ∖ X, P = c_b ∖ A, Q = A ∖ c_b. Then δ₁ = 1_Q − 1_P + 1_N and
δ₂ = 1_P − 1_Q + 1_N.

- **World 1 is a (G)+(IB) world.**
  - Monotonicity in κ: Stieltjes integration by parts on [0,2] with ψ = e^{(κ′−κ)x}, continuous and nondecreasing.
    x takes the value 2 on N₊, which is harmless.
  - Hence 𝒜_tilt is a convex cone. It contains δ ≥ 0, and it contains no nonzero δ ≤ 0 (look at the tail at y = 0).
  - Lemma vectorform then gives transitivity, strict (G) and (IB).
- **(K) for every model.**
  - If Q ∪ N is non-null, a y₀ > b exists, because {x = b} is null and Q ⊆ {x ≥ b}.
  - Tails at y ≥ b are ≥ 0, since δ₁ ≥ 0 on {x ≥ b}.
  - Tails at y < b are ≥ e^{κy₀}λ̄((Q∪N) ∩ {x ≥ y₀}) − e^{κb}λ̄(P), which is > 0 for large κ, uniformly in y.
  - If Q ∪ N is null, then δ₂ = 1_P ≥ 0.
- **No weak domination of C_b.** At y = b the tail of −δ₁ is −∫_{x≥b} e^{κx}(1_Q + 1_N). Then −1_P must be accepted
  at the additive world 2.
- **Every other model is dominated by C_{b₂}.**
  - World 2: 1 − b₂ ≤ 1 − λ̄(A) + λ̄(N).
  - World 1: band tails λ̄(A ∩ {x ≥ y}) + λ̄(N) − (b₂ − y) ≥ λ̄(A) + λ̄(N) − b₂ ≥ 0, using λ̄({x < y} ∩ M) = y; and
    band ⊆ every κ-cone.
  - So U_L = C_L = {C_b}, and (C) and (LA) hold **without Theorem kkm**. This is the right route, because kkm needs the
    closed sections this system lacks (the Q12_referee Q1.2 lesson).
- **Closed world-2 sections.** S₂(X) = {p : 1 − p₂ ≤ λ̄(E₂X)}.
- **Open world-1 section.** For X with E₁X = c_x ∖ Z, Z ⊆ c_{x−η}:
  - b < x: Q ⊇ [max(b, x−η), x) is non-null, so the comparison is accepted;
  - b = x: δ = −1_Z, rejected;
  - b > x: Q = ∅, rejected.
  - So the section is {p₂ < x}.
- **(b).**
  - (NC⁺) holds on 𝔚 by N17 Lemma 3.1, because the error sets c_b are nested. So the world is not (M1).
  - The disjoint-target argument gives ν(c_b) = 0 for every bounded endorser, so Λ = M.
  - The localized version with Q_n ⊆ d_b ∖ D_m gives Λ_D = M for every D.
- **(c).** The comparison with E₁X = (c_b ∖ P) ∪ Q has δ = 1_Q − 1_P. It is accepted (Q is non-null), relevant, and
  D-localized (δ⁺ = Q misses D_m), and ρ(P) > ρ(Q). Correct for every a.e.-finite ρ > 0.

**Novelty.** World 1 is Q12_referee N3's 𝒜₁. That report already showed it accepts every cut pair with non-null target,
that every endorsing charge lives at 1⁻, and that the section is open. What K3.3 adds is:
- the full axiom check (with the Q1.2-style direct domination, made for the tilt);
- Λ_D = M for **every** localizing D;
- the failure of (S) for every σ-finite ρ.

The note should say "this is Q12_referee N3 completed" rather than present it as a new construction.

---

## 4. K3.4 and the readings drawn from it

### 4.1 Lemma K3.4 — CORRECT

- (a): each δ ∈ 𝔉 meets δ_m⁺ ⊆ T_m non-nully, so it is not ≤ 0 on T_m. The δ_k⁺ ⊆ M, because members of 𝔚 vanish on
  N₊.
- (b) is then immediate.
- **Extension (PROVED here, one line).** The same holds for countably many such families 𝔉_j, using the diagonal
  union of K3.1(d).
- **Stronger and simpler form.** It also holds for any family 𝔉 that is "T-positive" for one localizing T (δ⁺ ∩ T_m
  non-null for all m), without pairwise meeting or small members. This is the form that D2, D2′ and H2.4 actually
  instantiate: S-positivity at the protected end, with T := S.
- In D2 the exotic family's members need not have small δ⁺. K3.4's hypothesis "inf μ(δ⁺) = 0" then holds only through
  the generator subfamily. The note's "(or directly, localizing at the end)" is the clean argument. I checked it for
  H2.4's world 1 (rule R⁰: generator-type δ are ≥ 1_{Q_g} near x = 1, so localized relevant comparisons lie in 𝒦₀ and
  λ endorses them) and for the Q1 worlds.

### 4.2 The readings — GAP (wording)

**What K3.4 proves for an (N) world.** For every pairwise-meeting 𝔉 with inf μ(δ⁺) = 0, every localizing D and every
a.e.-finite ρ > 0, some D-localized member of 𝔚 ∖ 𝔉 is not ρ-endorsed. This is the contrapositive of (b), and it is
correct.

**What §0 item 3 says.** "Any proof must use closedness against certificates whose positive parts do **not** pairwise
meet". This is a reasonable heuristic, but two things are missing:
- the unendorsed objects are single comparisons, not certificates;
- "not in a given pairwise-meeting family" is much weaker than "positive parts do not pairwise meet".

**What §4.2's last bullets say.** "So an (N) world must accept comparisons with many pairwise disjoint small targets."
This does not follow. Avoiding every prescribed small set, and not lying in one intersecting family, are compatible
with every two positive parts meeting. (Take positive parts that are long thin strips, any two of which cross.) The
author does write "No theorem is claimed", but §0 lists this under a PROVED item.

**Fix.** Replace the §0 sentence with the contrapositive of K3.4(b), as stated above. Delete "pairwise disjoint" in §4.2,
or label it a heuristic.

---

## 5. K3.5, K3.5′, K3.6

### 5.1 K3.5 — CORRECT

Every step was re-derived with ρ_k ≥ 0.

- **The family D_m** is localizing, and ρ_k ≤ m on M ∖ D_m.
- **Null ties for a.e. t (Tonelli).** For c(g) ≠ 0, {t ∈ aff Δ : t·c(g) = 0} is a line or empty (empty if c ∥ 𝟏).
  On N₊, t·c = 1.
- **X_m is regular** (D_m ⊆ M, and B_t ⊇ N₊). Its costs are finite: ≤ mμ(M) off D_m, plus (P2).
- **Small Φ.** The H12_referee §1.2 bound |t·c| ≤ Σ_{k : X errs} t_kρ_k holds pointwise with ρ_k ≥ 0. With X_m = Y° on
  D_m and absolute continuity, Φ(X_m) → 0.
- **The kkm dominator's world-k vector** is ≤ 0 off E_kX_m. Since D^k_m ⊆ M ∩ D_m and X_m = Y° there, it is ≤ 0 on
  D^k_m ∖ E_k(Y°). So (P1) applies at the same depth m.
- **H1.0.**
  - (a) needs only that Z_t is null and B_t incoherent.
  - (b) needs only the pointwise identity and finiteness, which (R) and the H12 bound supply.
- **Step 2.**
  - H1.1 applies: comparisons T1 ⪯_k Y with Y = T1 on D_m have δ = 0 on D_m ⊇ D^k_m, so (P1) covers them. Integrability
    off D_m holds, and step 4 uses ρ_k > 0.
  - M0closed(a) applies to strictly signed measurable fields without integrability (H12_referee §1.4: normalise c/|c|).

### 5.2 K3.5′ — CORRECT

- **(a)** Y° = P₁ is regular with E₁(P₁) = ∅. As a small bonus, ρ₂ and ρ₃ need only be integrable on R₁₂ and R₁₃
  respectively.
- **(b)** "(D^k, T1)-localized" is exactly "≤ 0 on D^k_m ∖ E_k(T1)".
- **(c)**
  - (i) makes Y° consistent, since off R_ij correctness at i and at j is the same advice.
  - For m ≥ m₀, E_k(Y°) ∩ D^k_m is null, so (P1) is plain D^k-localized endorsement. Localization at some m < m₀
    implies it at m₀.
  - The error mass of Y° on ⋃_k D^k_{m₀} is at most the first sum in (ii). Off the union it equals min(ρ₊, ρ₋).
  - "The sum in (ii) is Σ_k∫_{E_k(Y°)}ρ_k" should read "**bounds**" (it is equal only if the D^k_{m₀} are disjoint). This
    is harmless.

### 5.3 The residual, and a sharpening — CORRECT, with comments

- (R-ii) is the literal negation of (ii), so "case (ii) is closed except for (R-i) and (R-ii)" is accurate but close to
  tautological. The genuine content is K3.5 itself (σ-finite densities at several worlds, with integrability required
  only on the patch's error set) and K3.6.
- **Sharpening of Q_K3 "No" (PROVED here).** If Q_K3 has answer "No", every non-(M1) world is (S_int). That includes
  (M0) worlds, since Λ null implies Λ_∞ null. Then all densities in K3.5′(c) are integrable, so (ii) holds
  automatically.
  - Hence under "No", a cover of T1 needs an (M1) world or **sheltering (R-i)**. "Infinite minority mass" cannot
    occur.
  - The §7 sentence "(M1) worlds, or sheltering, or infinite minority mass at two or more worlds" should be shortened
    accordingly.

### 5.4 K3.6 — CORRECT

- R ⊆ R⁰_k ∖ D^k_{m₁} with all ρ_j(R) finite exists. Here R⁰_k is H2's improvement region: T1 accepts, is correct at k
  and wrong at the other two worlds.
- The p_n exist: removing finitely many sets of finite ρ_k-mass from W ∖ ⋃_{V}D^j_n leaves infinite mass, and
  ρ_k(· ∩ {max_j ρ_j ≤ N}) increases to it.
- **The three world checks.**
  - At k: δ_k = 1_R − 1_{p_n} is D^k-localized and unendorsable.
  - At j ∉ V ∪ {k}: toggling p_n and R is good at j, so X_n ≺_j T1 by strict (G).
  - At j ∈ V: δ_j = 1_{p_n} − 1_R has positive part p_n, which misses D^j_n.
- T1 ⪯_j X_n for some j ∈ supp p of the selected model tied with T1, which suffices.
- **Pigeonhole.** p_n ⊆ W ∖ D^j_m for n ≥ m, the p_n are disjoint, and ρ_j(p_n) ≥ ρ_j(R) > 0.
- The "Reading" sentence about J1 refers to an unrefereed note. Label it as a reading.

---

## 6. K3.7′ and K3.7

### 6.1 K3.7′ — CORRECT

**⇐.** m* ∈ K ∩ [e₁, e₂] rejects (−,−,+). D_{conv(A∪B)} = D_A ∩ D_B gives D_K ⊇ U ∩ {g₁, g₂ > 0}.

**⇒.**
- D_K ∩ M = {P_K > 0} ∩ M is open. So a.e. statements on the orthant pieces give:
  - D_K ∩ U ∩ (−,−,+) = ∅;
  - {P_K < 0} ∩ U ∩ (+,+,−) = ∅.
- g_L = (−1, −1, L) ∈ U for large L, because min_{K′} m₃ > 0. A limit point argument then gives K ∩ [e₁, e₂] ≠ ∅.
- **Separation.** Shift by 𝟏 to put α = 0. Then g ∈ D_H ⊆ U ∩ {g₁, g₂ > 0}, g₃ < 0, and P_K(g) < 0 on an open set.

**NUMERICS bookkeeping error (not affecting the lemma).** In `between_lemma.py` the diagnosis loop re-seeds
`default_rng(1)` *without* first drawing the sample G. It therefore inspects a different stream of K's from the main
loop. The case it prints (third coordinate 1.1·10⁻⁵) is **not** the main loop's mismatch.

`k3ref_py/between_diag.py` reproduces the main loop exactly. The single mismatch is trial 255, with extra points
including (0.909, 0.0906, 9.19·10⁻⁵):
- the lemma predicts disagreement, since K misses [e₁, e₂];
- (−1, −1, L) ∈ U is accepted by D_K for L = 10⁵, 10⁶, 10⁸, as the lemma requires;
- it is not accepted for L ≤ 10⁴, which is beyond the script's sampled L ≤ e⁸.

So the author's explanation (a sampling limit) is right in substance. The printed diagnosis should be corrected.

### 6.2 K3.7 — CORRECT

- **First sentence.**
  - Not (M1) ⇒ (M0) or (M2).
  - (M0) is excluded by M0closed(b), since worlds 2 and 3 add up with the weights ρμ.
  - (M2) splits into (S) and (N), and (S) is excluded by H1.2.
- **(α).** If Λ were null, ρ₁ ∈ (0, ∞) a.e. and H1.2 would apply. (γ) follows from K3.5 with Y° = P₁, D¹ = D,
  D² = D³ = ∅; (P3) holds because ρ₂ > 0.
- **(β).**
  - The map (s, θ) ↦ (1−s, sθ, s(1−θ)) has area factor proportional to s.
  - For each g the θ-tie set is at most one point, since ρ₂, ρ₃ > 0.
  - Pointwise sign limits as s → 0 give convergence in measure.
  - Coherent models of M_U are closed under convergence in measure (H12_referee §1.1).
  - θ → 1 and θ → 0 along good θ give S₁ and S₀.
- **(β′).**
  - S₁ = P₁ wherever σ₁ = σ₂, both off Λ (by definition) and on Λ (where P₂ = P₁). So K3.7′ applies.
  - On R₁₂, S₁ = P₁ off Λ and S₁ = U ∖ P₁ on Λ, so Λ ∩ R₁₂ = E₁(S₁) ∩ R₁₂.
  - M = R₁₂ ∪ R₁₃ for mixed gambles. The orthant statement follows.
- **Admissibility ((γ) item).** H1.1's steps 1–3 and 5 use no positivity. The edge exclusions are right: on e₁e₂ minus
  e₁ use −p₂ρ₂ < 0; on e₁e₃ minus e₁ use −p₃ρ₃ < 0; on the closed edge e₂e₃ use p₂ + p₃ = 1. Only p* = e₁ survives, and
  it forces Λ ⊇ E₁(T1) ∩ M.
- "endorses exactly the D-localized relevant comparisons" should read "endorses every D-localized relevant comparison".
- NUMERICS (`splice_rigidity`) were rerun and are identical.
  - In example (1), K₁ and K₀ contain e₁, so Λ ∩ (R₁₂ ∩ R₁₃) is empty (D_{K₁} ⊇ U ∩ (+,−,−), as one checks from the
    vertex inequalities of K′). The "consistency on R₁₂ ∩ R₁₃" line is therefore vacuous there.
  - This is harmless, but an example with Λ ∩ R₁₂ ∩ R₁₃ ≠ ∅ would test more.

---

## 7. Question Q_A: three necessary conditions (PROVED here; one reading)

Hypotheses of Q_A, at an interior p* (write θ* := p*₂/(p*₂ + p*₃)).

**(Q1) On the doubly disagreeing region, Λ lies in T1's world-1 error set:** Λ ∩ (R₁₂ ∩ R₁₃) ⊆ E₁(T1).
- On Λ ∩ (+,−,−), c = (0, −ρ₂, −ρ₃). So p*·c < 0, with no tie, and g ∉ B_{p*} ∪ Z_{p*} ⊇ D_{T1}.
- On Λ ∩ (−,+,+), p*·c > 0, so g ∈ B_{p*} ⊆ D_{T1}. T1 accepts there and errs at world 1.
- In the notation of (β′): D_{T1} ∩ (+,−,−) ⊆ D_{K₁} ∩ D_{K₀}, and D_{K₁} ∩ (−,+,+) ⊆ D_{T1} (likewise for K₀). On this
  region the world-1 error sets of C₁₂ and C₁₃ are **nested inside** that of T1.

**(Q2) A coherent model that copies T1 on Λ and is world-1-correct off Λ.**
- On Λ, p*·c = (p*₂ + p*₃)(θ*ρ₂σ₂ + (1−θ*)ρ₃σ₃). So B_{p*} ∩ Λ = G_{θ*} ∩ Λ, which equals D_{T1} ∩ Λ off Z_{p*}.
- Take good θ → θ* from either side in K3.7(β). On the tie set Z_{p*} ∩ Λ we have σ₂ ≠ σ₃, and the sign of
  θρ₂σ₂ + (1−θ)ρ₃σ₃ is sign(θ − θ*)·σ₂. So the one-sided limits exist, and they are coherent limits in measure of
  coherent S_θ.
- Hence there is a **coherent C*** equal to P₁ on M ∖ Λ and to T1 on Λ ∖ Z_{p*}. So
  E₁(C*) = E₁(T1) ∩ Λ off Z_{p*}: a coherent model whose world-1 error set is T1's, cut down to Λ.

**(Q3) Where M0closed(a) breaks.**
- Every oriented atom contained in Λ has its vector c(g) proportional to (0, ±ρ₂, ∓ρ₃) or (0, ±ρ₂, ±ρ₃). So its normal
  b has b₁ = 0, and its chart line passes **through the vertex e₁**.
- Equivalently, on Λ the Bayes sets depend on t only through θ = t₂/(t₂ + t₃): Λ ∩ R₂₃ is a fan at e₁.
- Thm. Estructure(b) ("ℓ_k misses the vertices and cuts off the odd vertex") and the ball lemma's "strict signs give
  the orthant" are exactly the steps that fail. So Q_A is genuinely beyond M0closed(a). It is not a routine extension.
- A proof of "No" should treat the vertex chords through e₁ as a new configuration, alongside chords, atoms and fans.

(Q1)–(Q3) are offered to the author. No verdict depends on them.

---

## 8. K3.8 and CONJECTURE K3.C

**K3.8: CORRECT.**
- K3.1(b) applied to 𝔚_D makes ρwμ endorse all D″-localized relevant comparisons.
- The cut-pair argument of F1.2(b) goes through with Q ⊆ (d_b ∖ D″_m) ∩ {ρ < c₁}. Since δ⁺ = Q misses D″_m, the
  comparison is localized.
- ess inf_{d_b∖D″_m} ρ ↓ ess inf_{d_b} ρ, because the union of the d_b ∖ D″_m is d_b mod null.
- F(b) < ∞ because ρ ∈ L¹ is finite a.e.
- The maximal support is a final segment. So Λ_D = c_{a_D} and Λ_∞ = c_{a_∞}.

**K3.C: correctly labelled CONJECTURE.** Two comments.

1. **Placement.** K3.C is the **localized repair of Q1.C1** (Q1_notes: "world 2 additive ⇒ SP^reg₁"). D2 refutes
   Q1.C1 as stated (world 1 fails SP^reg next to λ), but D2 has a_∞ = 0. K3.C is also the localized form of
   Q12_referee §6 (R2). Say so. Q12_referee's diagnosis applies verbatim: a proof needs a rate in Lemma T, i.e.
   (R3).

2. **Evidence bullet 2 is overstated (GAP).** "F1.4 excludes every such certificate that is chain-free" does not
   follow.
   - Chain-free means the positive parts are disjoint from the negative parts. For a chain-free c-ratio certificate
     δ̂ ≤ c − g, one gets Σλ1_P ≥ g − c and Σλν₂(Q) ≤ c·ν₂(M).
   - F1.4, however, needs a cover Σw1_P ≥ 1_S of a **fixed** set S. Its constant θ(S, b₀) depends on S through
     m = (1 − e⁻¹)λ(S)/2 via κ_m (Cor. SR, MP♯), with no rate.
   - The density g of a ratio certificate is uncontrolled. K3.1(f) gives existence for each (B′, c), but g may
     concentrate as c → 0.
   - The layer-cake bound gives only Σλν₂(Q) ≥ sup_u u·θ(λ{g > 2u}), roughly. This can tend to 0 at an unknown rate
     as g concentrates. So no contradiction follows.
   - **Fix.** Either restrict the claim to certificates with g ≥ γ on a set of measure ≥ m₀, with γ and m₀ fixed
     independently of c (e.g. uniform g = 1_{B′}/μ(B′)), where F1.4 applies to S = {g ≥ γ}; or state that excluding
     general chain-free ratio certificates needs the same missing rate (R3).
   - Note that uniform g is **not** equivalent to K3.1(f)(ii): a p.f.a. part may carry mass on B′. So the restricted
     statement is weaker evidence.

---

## 9. Q_K3 and the overall assessment (§7 of K3)

- Q_K3 is precisely formulated, and its equivalence with the certificate form is K3.1(f) (under (NC)).
- The "No" branch is sharper than stated (§5.3): (M1) or sheltering.
- The "Yes, without (S)" branch is right. The aiming paragraph is a correct list of requirements, labelled as such.
- BRIEF16 asks for "a single proved obstruction, or a precise single open question". K3 delivers:
  - one proved obstruction to the proof method (K3.3: closedness must be used);
  - three open items (Q_K3, Q_A, K3.C). Q_K3 is the governing one, and K3.C is its two-world form.
  - Q_A is an independent additive question. With K3.7 it handles only the single-exceptional-world case.
  - The note should say plainly that, for T1, settling the (M2) part needs both Q_K3 (or K3.C) and Q_A.

## 10. Requested changes (summary)

1. Rename K3's class "(S)" and the K3.7 item "(γ)".
2. K3.1(c)–(f): state them under (NC_𝔚), or set Λ := M when 𝒩 = ∅. Say "some D̂", not "canonical".
3. Write the scalar term of 𝒦′ explicitly.
4. K3.3: credit it as Q12_referee N3 completed.
5. §0 item 3 and §4.2: replace the pairwise-disjoint reading with the contrapositive of K3.4(b) (§4.2).
6. K3.5′(c): "bounds", not "is". §7: under "No", the residual is (M1) or sheltering.
7. K3.C evidence bullet 2: restrict it or reword it (§8).
8. Fix the `between_lemma.py` diagnosis stream (see `k3ref_py/between_diag.py`).
9. Optionally add (Q1)–(Q3) of §7 to Q_A.
