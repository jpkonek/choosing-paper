# P4B. Referee report on P4_notes.md, Part B (N17.B′ in two worlds with a nested selection; §6 on n = 3)

14 Oct 2026, round 11. Independent, adversarial referee; I did not write P4.

- **Read:** BRIEF10; N17_notes (§§0–3, 6); N19_referee (§§0–4, Lemma R1, Props R2/R3, §4 "nearby results"); N9_notes
  §1 (N9.4 normal form); writeup §§2–3 (setting, axioms, U-domain, Def. addup, (M0)/(M1)/(M2)); N22 Lemma 1.1 and
  Thm 1.2; R2 Thm 7 and Prop 8; P4 §§5–8 and scripts `p4py/lex_n2.py`, `p4py/shells.py`.
- **Verdicts:** CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG.
- **New statements** (§8) are labelled PROVED (full proof here), CHECKED (proof complete apart from one cited
  literature theorem) or NUMERICS. They are kept separate from the verdicts.
- **Scripts:** `p4bref_py/`, run with `python3 -I`. I re-ran `p4py/lex_n2.py`, and it reproduces.

---

## 0. Summary

| Item (P4) | Verdict | One-line reason |
|---|---|---|
| §5.1 setting ("map onto I, E₁(C_b) = [0,b), C_L the path") | CONFIRMED WITH REPAIR (presentational) | The only hypothesis needed is (Nest): the world-1 error sets of the members of C_L form a chain. The rest follows (Lemma N0): β(p) = μ(E₁C_p) is continuous and onto, C_L is the selection, and p-sections are closed iff b-sections are. A measure-preserving identification with [0,1] that carries *every* set is not available in general, but no proof needs one: read [s,t) as E_t∖E_s. |
| Lemma B0 | CONFIRMED | — |
| **Lemma B1 (strict escape)** | **CONFIRMED** | Uses exactly (K) at interior b, closed world-2 sections, and strict (G) at world 2. P4's own "more generally" clause also covers b = 0: φ₁(A) > 0 for every non-null A (Cor N1). P4 states B1 only for b ∈ (0,1); the case b = 0 is used heavily below. |
| Prop B2(a) "closed sections, fails SP" | CONFIRMED WITH REPAIR | ν⁺(I) = 1 is implicit. "Fails SP" is **false for {0,1}-valued ν⁺**: there λ + ν⁺ endorses every comparison. It is true when ν⁺ has infinitely many disjoint sets of positive mass, for instance the Banach-limit density (proof in §3). |
| Prop B2(b) | CONFIRMED WITH REPAIR | A witness D with 0 < ν⁺(D) < 1 need not exist (ultrafilter case). D = (x₀+h,1), which is ν⁺-null, works for **every** ν⁺: φ₁(c_{x₀} ∪ D) = x₀. B2(b) is also a special case of Thm E2. |
| Remarks after B2 (ν⁻ fails closedness; diffuse pfa primary) | CONFIRMED | ν⁻: A = (x₀−h,x₀) gives S₁(A) = [0,x₀) for every ν⁻. The diffuse-pfa remark is now PROVED in general (Thm E2). |
| **Theorem B3** | **CONFIRMED**, with three remarks | Every step re-derived. **(a)** Entering the levels in order is *necessary* for closedness, not sufficient: an exact in-order 3-level example with an open section (NUMERICS), explained by R2 Thm 7. **(b)** Once (K) is added, B3's class collapses (Thm E2). A world-1 of this kind in a full n = 2 system must have its first level with density > 0 a.e. Every multi-level in-order world violates strict escape (explicit witness). **(c)** The mechanism of B3(i) is R2 Thm 7's local-minimum argument, applied along the chain; this should be credited. The claim "first exclusion of (M2) by (S)" is fair in the SP/𝔚^reg formulation. |
| §5.5 reduction (¬SP ⇔ some non-null 𝓜-null set ⇔ certificates for all ε) | **CONFIRMED** | 𝓜 is a weak*-compact convex set of states, so N22 Lemma 1.1 and the Thm 1.2 mixture apply verbatim. Separation in (L^∞, ba) is correct. "Minimal shape c_a ≤₁ A_j" is heuristic and should be labelled so. |
| CONJECTURE N17.B′(2) | **Open in general; substantially narrowed (§8)** | PROVED here: (i) every world with a nonzero *leading charge* (all lexicographic worlds whose levels are arbitrary charges, countably or finitely additive); (ii) no set is ≤₁ sets that shrink to finitely many points. CHECKED (via Savage's theorem): (iii) every complete world. Known (N22 Thm 1.2): (iv) CP-a worlds. **Open:** incomplete worlds that are not CP-a, have no leading charge, and whose certificates are not point-localised. |
| Lemma B4 (removal lemma, any n) | CONFIRMED | It is R2 Thm 7 extended to countably many levels; it should be credited as such. |
| §6 "Why n = 2 does not transfer" | CONFIRMED WITH REPAIR | Item 2 misattributes: B3 does **not** use B1 (P4 itself says "no competitiveness is used"). B1 is used in B2(b), and now in E2 and T. What B3(ii) does use is the left/right (cut) structure of 𝔚^reg, which crossing error sets destroy in n = 3. |
| §6 necessary conditions for an n = 3 counterexample | CONFIRMED | Bullet 1 is the (M1)/(M2) dichotomy plus N17.3 (≥ 4 comparisons for ≤ 0, ≠ 0 certificates, N19). Bullet 2 is B4. Bullet 3 is (S) itself. |
| §7 "a construction needs a non-valuation (incomplete) world" (n = 2) | GAP in P4, closed here | P4 excluded only lexicographic worlds with CA levels and jump-type pfa. Complete non-lexicographic worlds were not excluded there. Thm E3 (CHECKED) excludes them, so the sentence becomes true as "incomplete, non-CP-a, without leading charge". |
| Axiom bookkeeping (§8 of P4: "hypotheses added: none") | CONFIRMED | (Nest) is the declared hypothesis of the n = 2 case. (C) and (E) are not used in Part B. (LA) enters only through non-emptiness. (Cl) is used only at regular models, which is weaker than (S). Strict (G) and (K) are used exactly where claimed (table in §7). |

**Net.** Part B is mathematically sound. The repairs are local: B2's quantifier over ν⁺ and its witness, and one
misattribution in §6. The main correction is to the *reading*.
- Strict escape is much stronger than P4 uses it. With its b = 0 case and two "drop" lemmas, it gives Thm E2: the
  leading charge of any lexicographic world is either zero or strictly positive. So the countable-lexicographic class
  of B3, and every lexicographic world with charge levels, is harmless in n = 2.
- It also gives Lemma T and, via Savage, Thm E3 (complete worlds).
- What remains of N17.B′(2) is a precise class of incomplete, non-linear worlds.

---

## 1. Setting (§5.1)

Hypothesis **(Nest)**: n = 2 on M_U, with strict (G), (IB), (LA), (S), and {E₁(C) : C ∈ C_L} a chain mod null. This
is N19 §4 item 1, with N19's repair that nestedness is needed for C_L, not only for the selection.

**Lemma N0 (PROVED).** Assume (Nest), and write M for the mixed problems of U and β(p) := μ(E₁C_p)/μ(M).
- (i) β is continuous on Δ, with β(e₁) = 0 and β(e₂) = 1. Hence every b ∈ [0,1] is attained, and the chain is
  {E_b : b ∈ [0,1]}, with μ(E_b) = bμ(M).
- (ii) C_L = {C_p} as models.
- (iii) A p-section {p : C_p ⪯_i X} is closed iff the b-section {b : E_b ≤_i E_i X} is closed.
- (iv) Every b ∈ (0,1) equals β(p) for some interior p, so (K) holds at every interior b.

*Proof.*
- **Vertex values.** C_{e₁} is competitive on {1}, so C_{e₁} ⪯₁ P₁ = U ∩ {h₁ > 0}, whose E₁ is ∅. Strict (G) gives
  β(e₁) = 0. Likewise β(e₂) = 1, since E₂ = M∖E₁ on mixed problems.
- **No missing values.** Suppose t ∈ (0,1) is not a value of β.
  - Let X be regular with E₁X = ⋃{E₁C_p : β(p) < t}. Monotonicity and strict (G) along the chain give
    {p : C_p ⪯₁ X} = {β < t}, and this set is closed by (S).
  - Symmetrically, using world 2 and E₂ = M∖E₁, the set {β > t} is closed.
  - These are two disjoint nonempty closed sets covering the connected set Δ. Contradiction.
- **Continuity.** Since every value occurs, the sets {β ≤ b} and {β ≥ b} are sections at chain models (worlds 1 and 2
  respectively), hence closed. So β is continuous.
- **(ii).** A set comparable with every E_b equals E_{b\*} with b\* = sup{b : E_b ⊆ it}. A coherent (hence regular)
  model is determined by E₁.
- **(iii).** A continuous surjection from a compact space pulls closed sets back to closed sets, and maps closed
  (compact) sets onto compact sets.
- **(iv).** β(e₁) = 0 and β(e₂) = 1. ∎

*Remark (identification).* A measure-preserving map M → [0,1] with E_b ↦ [0,b) that carries every measurable set
exists only if the chain generates the measure algebra. Nothing in B0–B4, or in §8 below, needs this.
- Read c_b := E_b, d_b := M∖E_b and [s,t) := E_t∖E_s.
- In B3(i), replace "Lebesgue density point b₀ of G := {k<j} ∩ d_a" by
  b₀ := inf{b : μ(G ∩ E_b) ≥ ½μ(G)} ∈ (a,1). Then every slab [b′,b₀), b′ < b₀, meets G in a non-null set.

---

## 2. Lemmas B0, B1 (claim 1)

**B0: CONFIRMED.**
- S₁(A) is an initial segment: E_{b′} ⊆ E_b ≤₁ A. Closedness gives [0,φ₁(A)]. φ₁(c_b) = b by strict (G).
- S₂ is the mirror image.
- (K) ⇔ φ₁(A) ≥ φ₂(A^c): if φ₁ < φ₂, any b strictly between lies in (0,1) and violates (K). The converse is the same
  argument.

**B1: CONFIRMED.** Re-derivation:
- For b′ ∈ (φ₁(A),1), (K) gives d_{b′} ≤₂ A^c. Closedness of S₂(A^c) gives d_{φ₁(A)} ≤₂ A^c.
- If A ⊋ c_b and φ₁(A) = b, then A^c ⊊ d_b, and strict (G)₂ is violated.
- Inputs: (K) only at interior b′; closed sections of world 2 at regular models; strict (G)₂. No (C), (LA), (IB) or
  world-1 closedness is used.
- The dual statement is checked the same way.

**Cor N1 (PROVED; the b = 0 case).** For every non-null A, φ₁(A) > 0. Dually, φ₂(A′) < 1 for every non-null A′.

*Proof.*
- Suppose φ₁(A) = 0 < 1. For every b′ ∈ (0,1), (K) gives d_{b′} ≤₂ A^c.
- Closedness then gives d₀ = M ≤₂ A^c, contradicting strict (G)₂. ∎

So strict escape holds at **every** b ∈ [0,1): A ⊋ c_b implies φ₁(A) > b. This excludes, for instance, the world
lex(right density at 0⁺, λ). That world has closed sections and SP, but φ₁(A) = 0 for every ν-null A.

---

## 3. Prop B2 (claim 3)

**(a) Sections: CONFIRMED.**
- Assume ν⁺(I) = 1 (implicit in P4; needed for ν⁺([0,x₀]) = 0). Then c_b ≤₁ A depends only on
  (ν⁺(A), λ(A)), through (ν⁺(A) − 1[b > x₀], λ(A) − b) ≥_lex 0.
- The three section formulas are exact, and all three sections are closed (`b2_check.py` (a): 0 violations on an
  exact grid, with the supremum checked).

**(a) "fails SP₁": WRONG as stated for arbitrary ν⁺; CONFIRMED WITH REPAIR.**
- *Counterexample.* Let ν⁺ be {0,1}-valued: an ultrafilter of the measure algebra containing every (x₀,x₀+h). It
  satisfies P4's hypotheses. Put ν := λ + ν⁺. Then:
  - b ≤ x₀, ν⁺(A) = 1: ν(A) ≥ 1 ≥ b = ν(c_b);
  - b ≤ x₀, ν⁺(A) = 0, λ(A) ≥ b: ν(A) ≥ ν(c_b);
  - b > x₀ (so ν⁺(A) = 1 and λ(A) ≥ b): ν(A) = λ(A) + 1 ≥ b + 1 = ν(c_b).
  ν is strictly positive, so **SP₁ holds** (`b2_check.py` (b)).
- More generally, if ν⁺ takes only finitely many values, then λ + (1/m)ν⁺ endorses, where m is its least positive
  value.
- *Repair.* Add the hypothesis "ν⁺ has infinitely many disjoint sets of positive mass". P4's own example satisfies it:
  - Let ν⁺ be a Banach limit of λ(·∩(x₀,x₀+h))/h. Let S_j ⊆ [½,1) be disjoint, with λ(S_j) = 2^{−j−1}, and put
    A_j := ⋃_m (x₀ + 2^{−m}S_j) ∩ (x₀,1).
  - For h ∈ [2^{−M−1}, 2^{−M}], λ(A_j ∩ (x₀,x₀+h)) ≥ Σ_{m>M} 2^{−m}2^{−j−1} ≥ h·2^{−j−1}. Hence ν⁺(A_j) ≥ 2^{−j−1} > 0.
  - (P4's "= 2^{−j}" is not needed and is not shown.) Then ν(c_{x₀}) ≤ inf_j ν(A_j) = 0 for every ν ∈ 𝓜.

**(b) CONFIRMED WITH REPAIR.**
- P4's witness needs 0 < ν⁺(D) < 1, which fails for {0,1}-valued ν⁺.
- Use D := (x₀+h,1) with h < 1−x₀. Then ν⁺(D) = 0, so ν⁺(c_{x₀} ∪ D) = 0, and φ₁ = min(x₀, 1−h) = x₀ although
  c_{x₀} ∪ D ⊋ c_{x₀}. This contradicts B1 for every ν⁺ (`b2_check.py` (c)).
- So "closedness alone does not give SP; competitiveness is needed" stands, using the Banach-limit instance.

---

## 4. Theorem B3 (claim 2)

**CONFIRMED.**
- (i): A = c_{b₀}∖Z is a proper subset of c_{b₀}. Then:
  - c_{b′}∖A = Z and A∖c_{b′} = [b′,b₀) for b′ ∈ (a,b₀);
  - π_m(Z) = 0 for m < j, and [b′,b₀) has positive π_m-mass at some m < j;
  - so the first nonzero coordinate is positive, and S₁(A) = [0,b₀) is not closed.
  - Hence {k ≥ j} = [t_j,1) mod null, with t_j nondecreasing and s_k ↑ 1.
- (ii): A∖c_b ⊆ R_{≥j}, and π_m vanishes on R_{>m}. The lex inequality forces π_m(c_b∖A) = 0 for m < j and
  π_j(c_b∖A) ≤ π_j(A ∩ [b,s_j)). Multiplying by α_j gives ν(c_b) ≤ ν(A).
- Hypotheses used: (Cl)₁ at regular models, strict (G)₁ (a.e. some w_k > 0), and the cancellation normal form. No (K),
  as claimed. Implicit: each w_k is integrable, so that each π_k is finite. This should be stated.
- NUMERICS: `lexsec.py` computes sections **exactly**, by recursion over levels with exact piecewise-linear zero sets.
  - (1) The out-of-order trimmed set has the open section [0,3/4).
  - (2) In order, with 3 levels and *random* weights α_k: 1499 closed sections, all endorsed (0 violations).

**Remark (a): in order is necessary, not sufficient.**
- `lexsec.py` (2) also found an exact in-order 3-level world and a set A whose section is [0, 23/144), which is open.
- Mechanism: at b = 23/144 the first level ties exactly, and the second level (nonzero on R₁) is negative.
- This is R2 Thm 7. A point where π₁(c_·) strictly increases cannot be "improvable". So inside each R_k the deeper
  densities must be Neyman–Pearson ordered along the chain (for instance, vanish there).
- This does not affect B3, which is an implication from closedness. It does mean that B3's class is thinner than §5.4's
  "Reading" suggests.

**Remark (b): with (K), the class collapses.**
- By Thm E2 below, in a full n = 2 system the first nonzero level must have density > 0 a.e. Then SP is trivial: the
  first level itself endorses.
- Explicit check. For world 1 = lex(λ|_{[0,½)}, λ), which is in order and has closed sections:
  - φ₁(c_b ∪ D) = b for every b < ½ and every D ⊆ [½,1). Strict escape fails in 110/110 exact cases
    (`lexsec.py` (3)).
  - With world 2 = λ, (K) fails at b = 5/8 for P = [0,¼), Q = [5/8,1): P ≰₁ Q and Q ≰₂ P.
  - By contrast, lex(ρλ, λ) with ρ > 0 passes strict escape in 396/396 cases (`lexsec.py` (4)).

**Remark (c): attribution.** B3(i) is R2 Thm 7's local-minimum argument run along the chain, and Lemma B4 is its
countable-level version. "First case in which (S) excludes (M2)" is accurate for the 𝔚^reg/SP formulation of N19 §4,
not for exclusion of lexicographic rankings in general (R2 Prop 8, R3 Thm L and N9.6 already did that).

---

## 5. §5.5 reduction (claim 4)

**CONFIRMED.**
- 𝓜 = {states ν on L^∞(M) : ν(1_A − 1_{c_b}) ≥ 0 whenever c_b ≤₁ A}. It is weak*-closed, defined by linear
  inequalities, and hence weak*-compact and convex. It is nonempty by (NC⁺_𝔚) for nested chains (N17.3) and IRC
  Thm NC(a).
- ¬SP ⇒ non-null 𝓜-null set:
  - let s\* be the essential union of {ρ_ν > 0}, ν ∈ 𝓜, realised by countably many ν_k;
  - if M∖s\* is non-null, N22 Lemma 1.1 gives a non-null N with ν(N) = 0 for all ν ∈ 𝓜;
  - otherwise Σ2^{−k}ν_k ∈ 𝓜 has an a.e.-positive CA part, hence is strictly positive (Lemma R1 converse).
  - The converse direction is trivial.
- 𝓜-null ⇔ certificates for every ε: bipolar theorem in (L^∞, ‖·‖)′ = ba, applied to cone(𝔚^reg) + L^∞₊, as in P4.
- Correction: "The minimal shape of a certificate is c_a ≤₁ A_j for disjoint A_j" is a heuristic, not a theorem.
  Label it so.
- Useful reformulation (PROVED, immediate):
  - c_b ≤₁ A ⇔ P ≤₁ Q, with P := c_b∖A ⊆ c_b and Q := A∖c_b ⊆ d_b.
  - Every pair (P,Q) with P left of a cut and Q right of it arises this way.
  - So 𝔚^reg₁ is exactly the set of world-1 "left ≤ right" cut comparisons, and (K) says that every cut pair (P,Q) has
    P ≤₁ Q or Q ≤₂ P.

---

## 6. Lemma B4 and §6 (claim 5)

**B4: CONFIRMED.**
- X := C_{p₀} with Z′ removed from its world-i error set. X is regular, because E_i of a coherent model contains no
  nonnegative gamble.
- X ≺_i C_{p₀}, and v(E_iX) agrees with v(E_iC_{p₀}) below level j.
- So v(E_iC_{p_m}) <_lex v(E_iX), hence C_{p_m} ⪯_i X while p₀ ∉ A_i(X).
- Uses only (S)-closedness at a regular model and strict (G). It holds for any n. It is R2 Thm 7 with an
  ℝ^{j−1}-valued lexicographic primary.

**"Why n = 2 does not transfer": CONFIRMED WITH REPAIR.**
- Item 1 (approach from below along the chain) is correct.
- Item 2 is wrong as attribution: B3 does not use Lemma B1. B3 uses (a) the chain, for approach from below, and
  (b) the cut structure of 𝔚^reg (A∖E(C) lies beyond the cut), which B3(ii) needs.
- Strict escape (B1, and hence E2, T, E3 below) is the part that needs the complementary world E₂ = M∖E₁.
- Both (b) and B1 fail along crossing error sets in n = 3.

**Necessary conditions for n = 3: CONFIRMED.**
- Bullet 1 is the logical dichotomy plus N17.3, as refereed in N19 (4 comparisons for ≤ 0, ≠ 0 certificates).
- Bullet 2 is B4: no p_m → p₀ with strictly smaller shallow valuation, i.e. a weak local minimum, since lex is total
  on ℝ^{j−1}.
- Bullet 3 restates (S).
- Nothing in §8 below transfers to n = 3 as it stands. Each result uses strict escape, which needs a complementary
  world along a chain.

---

## 7. Use of axioms (checked)

| Statement | (Cl)₁ | (Cl)₂ | (K) | strict (G) | (IB) normal form | (C) | (LA) |
|---|---|---|---|---|---|---|---|
| N0 | chain models | chain models | vertices, (S) | yes | — | — | yes |
| B0 | yes | yes | for the ⇔ | yes | — | — | — |
| B1, N1 | — | yes | yes | world 2 | — | — | — |
| B2(a) | (property) | — | — | yes | yes | — | — |
| B3 | yes | — | — | world 1 | yes | — | — |
| §5.5 | — | — | — | — | — | — | (𝓜 ≠ ∅ via N17.3) |
| B4 | world i | — | — | yes | levels additive | — | — |
| E2, T, E3 (§8) | yes | yes (via B1) | yes (via B1) | both | yes | — | — |

Closedness is used only at **regular** models, which is weaker than (S) for every model, so no quantifier is
overstated.

---

## 8. New results (separate from the verdicts)

Setting: (Nest), with world orders as relations on measurable subsets of M (N9.4 normal form). Strict escape (SE)
means B1 together with Cor N1: for every b ∈ [0,1) and non-null A ⊋ c_b, φ₁(A) > b.

### 8.1 Two "drop" lemmas (PROVED)

**Lemma DL (drop a left slab; uses (Cl)₁ and cancellation).** Let x ∈ (0,1], let Z ⊆ c_{x−η} be non-null, and let
F ⊆ d_x be measurable. If Z ≤₁ [b,x) ∪ F for every b ∈ (x−η,x), then Z ≤₁ F. With F = ∅ the hypothesis is impossible.

*Proof.*
- Put A := (c_x∖Z) ∪ F.
- For b ∈ (x−η,x): c_b∖A = Z and A∖c_b = [b,x) ∪ F, so (x−η,x) ⊆ S₁(A). Since S₁(A) is an initial segment,
  [0,x) ⊆ S₁(A).
- Closedness gives x ∈ S₁(A), i.e. c_x∖A = Z ≤₁ A∖c_x = F.
- F = ∅ would give Z ≤₁ ∅, against strict (G). ∎

**Lemma DR (drop a right slab; uses SE).** Let x ∈ [0,1), z > x, and let D ⊆ d_z be non-null. There is y > x such
that L ∪ R ≤₁ L ∪ D for every R ⊆ [x,y) and every L disjoint from [x,y) ∪ D.

*Proof.*
- x′ := φ₁(c_x ∪ D) > x by SE, and c_{x′} ≤₁ c_x ∪ D means [x,x′)∖D ≤₁ D ∩ d_{x′}.
- Put y := min(x′,z). Then R ⊆ [x,x′)∖D, so R ≤₁ D by monotonicity.
- Cancellation adds L to both sides. ∎

### 8.2 Lemma T (PROVED): no set is dominated by sets shrinking to finitely many points

Let x₁ < … < x_m be points of [0,1] and Z non-null. There is no sequence of non-null Q_j ⊆ ⋃_i (x_i−1/j, x_i+1/j)
with Z ≤₁ Q_j for all j.

*Proof.*
1. **Replace Z by a slab.**
   - t₀ := φ₁(Z) > 0 (Cor N1), and c_{t₀} ≤₁ Z ≤₁ Q_j.
   - Choose a slab Z′ = [u,v) ⊂ (0,t₀) lying strictly left of every positive x_i and at distance > η from all x_i
     (u > η if x₁ = 0).
   - For j > 1/η, cancellation gives Z′ ⊆ c_{t₀}∖Q_j ≤₁ Q_j∖c_{t₀} ⊆ Q_j.
2. **Fix the targets.**
   - Fix b < 1 close to 1, and κ, κ′ > 0 with b + κ < 1 − κ′.
   - Fix disjoint non-null slabs D_i ⊆ [b, b+κ), one for each x_i < 1.
   - Lemma DR gives y_i ∈ (x_i, x_i+η) for each such x_i.
3. **Apply DR, then monotonicity.**
   - Given any b_i ∈ (x_i−η, x_i) for the positive x_i < 1, take j large.
   - Replace the right pieces Q_j ∩ [x_i, x_i+1/j) by the D_i (DR, successively; the remaining pieces are disjoint
     from each [x_i,y_i) ∪ D_i).
   - Enlarge the left pieces to [b_i,x_i). If x_m = 1, enlarge its left piece to [1−κ′,1).
   - This gives Z′ ≤₁ ⋃_i [b_i,x_i) ∪ ⋃_i D_i ∪ [1−κ′,1), where the last term is present only if x_m = 1.
4. **Apply DL** at the positive x_i < 1 in increasing order. Each time F is the union of everything to the right.
   This gives Z′ ≤₁ ⋃D_i ∪ [1−κ′,1) ⊆ [b,1).
5. **Conclude.** This holds for every b near 1. DL at x = 1 with F = ∅ is a contradiction. ∎

*Content.*
- "Infinitely heavy points" are excluded in every world, complete or not: one-sided, two-sided, or several at once.
- So are their finite combinations.
- The B2 jump-type world is the special case Z = c_{x₀}, Q_j = (x₀, x₀+1/j).
- In particular, a certificate of P4's minimal shape c_a ≤₁ A_j (A_j disjoint) cannot have its A_j inside shrinking
  neighbourhoods of a fixed finite set.

### 8.3 Theorem E2 (PROVED): a leading charge is zero or strictly positive

Call a charge π ≥ 0 on M, vanishing on null sets, a **leading charge** of world 1 if for all A, B:

  π(B∖A) > π(A∖B) ⇒ A ≤₁ B ⇒ π(B∖A) ≥ π(A∖B).

Under (Nest), (Cl) at both worlds, (K) and strict (G): every leading charge is either 0 or has CA density ρ > 0 a.e.
In the second case π is strictly positive and endorses every relevant comparison, so **SP^reg₁ (N17.B′) holds**.

*Proof.*
Put f(b) := π(c_b), which is nondecreasing with f(0) = 0. Write π = ρλ + σ (Yosida–Hewitt), with σ purely finitely
additive and carriers Z_m: μ(Z_m) → 0 and σ(M∖Z_m) = 0.

1. **No left jumps (uses (Cl)₁).** Suppose J := f(β) − f(β−) > 0 for some β ∈ (0,1].
   - Take b < β with ∫_{[b,β)}ρ < J, then m with μ(Z_m) < μ([b,β)).
   - Put A := c_β∖([b,β)∖Z_m) ⊊ c_β. Then π(A) > f(β) − J ≥ f(b′) for all b′ < β, so c_{b′} ≤₁ A by the first
     implication.
   - But c_β ≰₁ A by strict (G). So S₁(A) = [0,β), which is not closed.
2. **Strict escape in terms of f.**
   - For b ∈ [0,1) and non-null D ⊆ d_b, SE and the second implication give some b′ > b with
     f(b′) ≤ f(b) + π(D).
   - Choosing D ⊆ d_b∖Z_m with small ∫_Dρ shows that f is right-continuous. With step 1, f is continuous on [0,1].
   - If D can be taken π-null, f is constant on some [b,b′].
3. **The set N := {ρ = 0}.** Suppose N is non-null, and let s := ess sup N.
   - For every b ∈ [0,s), (N ∩ d_b)∖Z_m is π-null and non-null. So f is right-locally constant on [0,s); being
     continuous, f ≡ 0 on [0,s].
   - Hence π(c_s) = 0 and N = c_s mod null.
   - If s = 1, then π = 0.
   - If s < 1, then ρ > 0 a.e. on d_s. Take Z := c_{s/2} and A := c₁∖Z. For b′ ∈ [s,1),
     π([b′,1)) > 0 = π(Z), so c_{b′} ≤₁ A. Then S₁(A) = [0,1), which is not closed.
4. **Conclusion.** So π = 0 or ρ > 0 a.e. In the latter case π(D) ≥ ∫_Dρ > 0 for every non-null D, and
   c_b ≤₁ A implies π(A) ≥ π(c_b) by the second implication. ∎

**Corollary E2′ (PROVED).** Let world 1 be lexicographic with countably many levels π_k, where the π_k are arbitrary
bounded charges ≥ 0 vanishing on null sets (countably additive, purely finitely additive or mixed). Then the first
nonzero level is strictly positive, and N17.B′ holds at world 1.
- It subsumes B2(b) (π = ν⁺ has ρ = 0) and P4's remark on diffuse pfa primaries.
- It shows that **B3's multi-level in-order worlds cannot occur in a full n = 2 system**: their first level vanishes
  on R_{≥2}.

*Proof.* Strict (G) rules out the case where all levels vanish. The first nonzero level is a leading charge. ∎

### 8.4 Theorem E3 (CHECKED): complete worlds

If ≤₁ is complete (total), then N17.B′ holds at world 1.

*Proof.*
- Fix a non-null Z. By Lemma T with m = 1, each x ∈ [0,1] has a neighbourhood whose non-null subsets Q satisfy
  Z ≰₁ Q, hence Q <₁ Z by completeness.
- Compactness gives a finite partition of M into slabs, each ≤₁ Z. So ≤₁, a de Finetti qualitative probability by
  N9.4, is *fine* in Savage's sense.
- By Savage (1954, §3.3; see Fishburn 1986, Statist. Sci. 1, §3), a fine qualitative probability has a (unique)
  finitely additive P that *almost agrees* with it: B ≤ C ⇒ P(B) ≤ P(C).
- With n pieces ≤₁ Z we get 1 ≤ nP(Z), so P is strictly positive. Null sets are tied with ∅, so P vanishes on them.
- P endorses every relevant comparison. ∎
- (CHECKED: the only imported step is Savage's theorem, whose proof is purely Boolean, so it applies on the measure
  algebra.)

### 8.5 Status of N17.B′(2) after this report

N17.B′(2) holds at world 1 whenever world 1:
- (i) is CP-a (N22 Thm 1.2: strict (G) alone gives a member with an a.e.-positive CA part; no (S) is needed);
- (ii) has a nonzero leading charge (E2), in particular any lexicographic world with charge levels (E2′);
- (iii) is complete (E3, CHECKED).

Any counterexample must have a world 1 that:
- is **incomplete, not CP-a, and has no nonzero leading charge**. This is the class of non-linear acceptance cones,
  like N17.7's 𝒢_i;
- has strict escape at every b ∈ [0,1) and closed sections, which by Lemmas DL and DR lets thin one-sided slabs be
  dropped;
- has ¬SP certificates in which no non-null set is ≤₁ sets shrinking to finitely many points (Lemma T). For example,
  c_a ≤₁ A_j with disjoint A_j spread over a set of positive measure.

What blocks a proof for spread A_j: SE moves mass to the right only out of slabs whose width depends on (b,D), so
Vitali covering always leaves a residual. Closedness gives a left-limit only for a single cut. A proof would need a
uniform version of DR, or a closedness statement for a countable family of cuts.

---

## 9. Files (`p4bref_py/`, run with `python3 -I`)

- `lexsec.py` (+ `.out`): exact section computation for lexicographic worlds with piecewise-constant levels.
  - (1) B3 out of order: an open section.
  - (2) In order with 3 levels: 1499 closed sections with 0 endorsement violations under random α, and 1 exact
    in-order open section (Remark 4(a)).
  - (3) In-order lex(λ|_{[0,½)}, λ): strict escape fails in 110/110 cases, and explicit (K) failure with world 2 = λ
    (Remark 4(b), Thm E2).
  - (4) lex(ρλ, λ), ρ > 0: strict escape holds in 396/396 cases.
- `b2_check.py` (+ `.out`): Prop B2.
  - (a) Sections closed.
  - (b) {0,1}-valued ν⁺: λ + ν⁺ endorses, so SP holds (repair to B2(a)).
  - (c) The repaired witness for B2(b).
- No proof depends on the scripts.
