# Referee report C12 (round 15): C1_notes.md (glued credal worlds) and C2_notes.md ((LD) counterexample)

15 Oct 2026. Only the round-15 notes at the top of each file are refereed; the archived round-10 notes are not.
Checked against: BRIEF13/BRIEF14; B1_notes.md §2 (definitions, B1.0–B1.3) and B1_referee.md; write-up §2
(models, advice, background order, decomposable domains, axioms (G), (IB), (LA), (S), (C), (LF), U-domain, (CP-a),
Def. addup, (M0)/(M1)/(M2)), §7.7 (Thm M0closed, Cor M0closed, Cor CPaU), §8.5 (Lemma Q34, Prop Q35, definition of
a leading charge, Thm S21, Thm Q36, Cor Q37); B3_notes/B3_referee for B3.1–B3.2.

Scripts: `c2py/ld_two_world.py` and `c1py/glue_dichotomy.py` rerun with `python3 -I`; outputs reproduce the stored
`.out` files byte for byte apart from timing lines (`c12ref_py/*.rerun.out`). Independent checks written for this
report: `c12ref_py/ref_c2.py` (+ `.out`), `c12ref_py/ref_c1.py` (+ `.out`), `c12ref_py/negctl_count.py`. No verdict
rests on numerics.

## Summary of verdicts

| Item | Verdict |
|---|---|
| **C2.1** (two-world counterexample to (LD), every axiom) | **CORRECT**, with three small fixable gaps (G1–G3) and one wording fix in §0 |
| C2.1(5): no nonzero leading density, no nonzero leading charge (finitely additive included) | **CORRECT** after G1 (densities that may vanish) and G3 (wording); an S21-free proof is supplied below |
| C2.2 (envy form) | **CORRECT** |
| C2.3 (edge comonotonicity: separation, sweep, comonotone, ray) | **CORRECT** |
| C2.4 ("exact characterisation") | **GAP (wording)**: necessity and sufficiency are stated for different classes |
| C2.5 (edge inputs cannot prove (LD)) | **CORRECT for the listed abstract inputs; the final sentence overreaches** |
| C2.6 (link rigidity) | **CORRECT** |
| C2.7 | **CORRECT** (the claim that it covers the box densities of *Coverage after NA* (4) is not re-checked here) |
| C2.8 | identity **CORRECT**; the "concretely" consequences are sketches → label CHECKED/heuristic, not PROVED |
| **C1.1** (dichotomy: collapse vs glued measures endorse everything) | **CORRECT** |
| C1.2 | **CORRECT** |
| C1.3 (credal transfer chain) | **CORRECT**; script checks only weak acceptance of steps (tighten) |
| **C1.4** (strict-G ⊆ closure ⊆ weak-G) | **CORRECT** |
| C1.5 (gluing refines edges) | **CORRECT** (one line to add on strict separation) |
| **C1.6** (design dead) | **CORRECT at the status of Thm M0closed(b)**; the §0 headline "design is dead / no third case" must be scoped to G-weak worlds |
| C1.7 (credal B1.3, G-band) | **CORRECT** |
| C1.8 | **CORRECT at CHECKED** (Savage import; one line on strict fineness) |
| **C1.9** (finite G-obstruction) | **CORRECT**; the trailing "supports must cross" remark is unproved |

Nothing is WRONG. The headline mathematics of both notes stands.

---

## 1. Theorem C2.1 — every axiom re-derived

Setting: n = 2, K′ = [α′, β′] ⊆ (0,1) (t = weight of world 2), U = D_{K′}, M_U = all measurable subsets of U mod
null. U = M⁻ ⊔ M⁺ ⊔ N_+ up to null sets (U contains no nonzero h ≤ 0).

**Geometry (CORRECT).** For g ∈ M⁻ (g₁ < 0 < g₂), g ∈ U ⟺ (1−α′)g₁ + α′g₂ > 0 ⟺ σ < α′; for g ∈ M⁺, ⟺ τ > β′.
For α ≤ α′ ≤ β′ ≤ β, D_{[α,β]} ⊆ U, and since E_1 = X △ P_1 with P_1 = M⁺ ∪ N_+:
E_1(D_{[α,β]}) ∩ M⁻ = D ∩ M⁻ = {σ < α}, E_1 ∩ M⁺ = M⁺ ∖ D = {τ ≤ β}. With x as defined, E_1(C_s) ∩ M = {x < s}
(mod the null rays {x = s}), E_2(C_s) ∩ M = {x ≥ s} (on M exactly one world errs), and C_s ⊇ N_+, so C_s is regular.
C_0 = D_{[0,β′]} = P_1 and C_1 = D_{[α′,1]} = P_2 mod null. s ↦ μ{x < s} is continuous and strictly increasing
(level sets are rays; every open angular sector has positive Gaussian mass). Independent Monte Carlo check
(`ref_c2.py` §1, 25 551 Gaussian samples in U, six values of s including 0 and 1): 0 mismatches, including
world-2 complementarity and acceptance of N_+.

**(LF) at C_s, s ∈ (0,1) (CORRECT).** K′ lies in the relative interior of [α′s, β′+(1−β′)s], so every g ≠ 0 with
P_{K_s}(g) = 0 has P_{K′}(g) > 0; ∂D_{C_s} ∖ 0 ⊆ U and N = U works, since R △ C_s ⊆ U forces R ⊆ U.

**Preorders, strict (G), (IB) (CORRECT).** On M_U each pair meeting U has two available kinds of advice (accept or
silence); at world i exactly one is correct, and the background order makes the other strictly worse (good ≺ no
advice for h_i > 0; no advice ≺ bad for h_i < 0). Pairs with neither orientation in U carry silence for every
model. So "X at least as good as Y a.e. at world i" ⟺ E_iX ⊆ E_iY a.e., and every member gives ≤; on a non-null
difference every member gives < because F_aρ₀ > 0 on M and φ_a > 0 on N_+ a.e. Unanimity (finite or infinite) of
preorders is a preorder, and strictness for every member gives X ≺_i Y. (IB): for A = −A and F, G ⊆ A^c,
ν(E_i((D∩A)∪F)) − ν(E_i((E∩A)∪F)) = ν(E_iD ∩ A ∩ U) − ν(E_iE ∩ A ∩ U), independent of F, member by member.

**Competitiveness on supp p (CORRECT).** Vertices: E_1(C_0) = ∅ and E_2(C_1) = ∅. For s ∈ (0,1) and any
X ∈ M_U (regular or not), with A = E_1X ∩ M and N = N_+ ∖ X: if some b has ν_b(M∖c) > ν_b(M∖A) + ν_b(N), then
ν_b(A) − ν_b(c) > ν_b(N) ≥ 0. For each a, k := r_ab(s−) = sup_{x<s} r_ab ≤ r_ab(s) < ∞ separates, and
ν_a(A) − ν_a(c) = ∫_{A∖c} r dν_b − ∫_{c∖A} r dν_b ≥ k(ν_b(A) − ν_b(c)) ≥ 0, so ν_a(E_1X) ≥ ν_a(c). Holds for
every a, so C_s ⪯_1 X. Independent check (`ref_c2.py` §2): exact per-pair fractional knapsack (the continuum worst
case by Lyapunov) with a radius-dependent ρ₀ and an unbounded member (1−x)^{−1/2}, 19 values of s, 6 pairs: minimum
relative slack −9·10⁻¹⁵ (rounding). Negative control with a world-2 density that is not a function of x: 38
failures (§3), as C2.3 predicts.

**Closed sections for EVERY evaluable model (CORRECT).** s ↦ ν_a(c_s) is continuous (finite measure, null level
sets) and nondecreasing with value 0 at s = 0, so {s : ν_a(c_s) ≤ ν_a(E_1X)} = [0, s_a]; the intersection over a
(any cardinality) is a closed initial segment. World 2 symmetric (closed final segment containing 1). p ↦ p₂ is
continuous. Nothing here uses regularity of X, so non-regular models (N ≠ ∅) are covered. Independent check
(`ref_c2.py` §4, 25 random models, half non-regular, 41-point grid): sections are [0,s₁] and [s₂,1] and cover the
grid, 0 violations.

**Domination, U_L, C_L, (LA), (C) (CORRECT, gap G2).** Sections [0,s₁] ∪ [s₂,1] = [0,1] give s₂ ≤ s₁, so C_s weakly
dominates X for s ∈ [s₂,s₁]; not strict ⟹ tied (strict part of a preorder). Tie forcing for s ∈ (0,1) with
(a*, b*) from (St): world-2 tie gives ν_{b*}(A) − ν_{b*}(c) = ν_{b*}(N); the integral identity gives
ν_{a*}(A) − ν_{a*}(c) ≥ k ν_{b*}(N) ≥ 0; the world-1 tie gives it ≤ −ν_{a*}(N); hence N null and, r strictly
increasing (r − k > 0 on {x > s}, k − r > 0 on {x < s}), A = c. Undominatedness of every C_s, including s = 0, 1,
follows by strict (G) along the chain. Hence U_L = {C_s : s ∈ [0,1]}, all coherent, so **C_L = {C_s}** as claimed;
(LA) and (C) hold.

- **G2 (endpoints).** The proof says "choose k as in (2)", but (2) defines k only for s ∈ (0,1); at s = 1,
  k = sup r may be +∞ (e.g. F_a = (1−x)^{−1/2}, G_b = 1 satisfies (Co), (St)). *Fix:* add "For s = 0 a world-1 tie
  gives ν_a(E_1X) = ν_a(∅) = 0, so E_1X is null and X = P_1 = C_0 by strict (G); s = 1 is the mirror at world 2.
  For s ∈ (0,1), k = r(s−) ≤ r(s) < ∞."

**World 1 has no nonzero leading density (CORRECT after G1).** The argument for ρ > 0 a.e. is right (k > δ > 0
can be chosen since f > 0; Y = P_1 △ Q, Z = P_1 △ P are regular, Y △ Z ⊆ M; ρ(P) > ρ(Q) but ν_a(Q) > ν_a(P)).

- **G1.** B1 §2 says "positive integrable ρ", but C2's headline and B1.4 say "no *nonzero* leading density", and
  B1_referee (ii) notes positivity is not used in B1.0. If ρ ≥ 0 is allowed to vanish, f = F_aρ₀/ρ is undefined on
  {ρ = 0}. *Fix (one sentence):* "If Z := M ∩ {ρ = 0} is non-null, take non-null Q ⊆ Z and P ⊆ M ∖ Z with
  ν_a(P) < ν_a(Q) (atomless); then ρ(P) > 0 = ρ(Q) forces P_1 △ Q ⪯_1 P_1 △ P, i.e. ν_a(Q) ≤ ν_a(P), a
  contradiction. So ρ > 0 a.e. on M and the argument above applies."

**No nonzero leading charge, finitely additive included (CORRECT; G3 wording).** Leading charge (write-up §8.5):
π ≥ 0 on U, bounded, null on μ-null sets; (P1) π(B∖A) > π(A∖B) ⇒ A ≤_1 B; (P2) A ≤_1 B ⇒ π(B∖A) ≥ π(A∖B).
Q and P_e are disjoint and incomparable; the contrapositive of (P1) applied to (Q, P_e) and to (P_e, Q) gives
π(P_e) = π(Q); finite additivity gives π(e′ ∖ e) = 0 for admissible e ⊊ e′; S21 (n = 2: strict (G), (IB), (S), all
verified above) then forces π(M) = 0.

- **G3.** "Both properties of a leading charge then give" → "Property (P1), applied to (Q, P_e) and to (P_e, Q),
  gives". (P2) is not used.
- **Robustness (optional, removes the S21 import).** With D := e′ ∖ e non-null and π(D) = 0, if π(M) > 0 split
  M ∖ D into finitely many pieces of ν_a-mass < ν_a(D); one piece E has π(E) > 0 = π(D), so (P1) gives D ≤_1 E,
  i.e. ν_a(D) ≤ ν_a(E), a contradiction. Purely finitely additive π are covered since only finite additivity and
  nullity on μ-null sets are used.

**Selected example.** 𝒜 = {1+x, 1+3x²}, ℬ = {1}: ratios 1+x and 1+3x² are strictly increasing, integrable,
non-proportional. ℬ = {1, 2−x}: all four ratios strictly increasing. Both refute (LD).

**Remark (ii) (CP-a, adds up) — CORRECT.** Unanimity over the normalised states ν_a/ν_a(U) and their weak-* closed
convex hull is (CP-a) with the error-indicator penalty; each member endorses every comparison, so both worlds add
up. C2.1 therefore refutes (LD) only in the form "any n ≥ 2"; it is not a step towards a T1 cover, as the note
itself says. Its strength is exactly as stated: it disposes of the n-independent (LD) and shows that B1.4's escape
is realisable in two worlds by worlds that nevertheless add up.

**Wording in §0.** "The same holds for every comonotone family of members at either world" → "for every families
satisfying (Co) and (St)"; without (St) the tie forcing, hence (C) and U_L = {C_s}, can fail (constant ratios on an
interval leave ties).

**NUMERICS claims.** All reproduce. Cosmetic: the knapsack minimum for system (ii) is −1.39·10⁻¹⁶, slightly below
the "≥ −1·10⁻¹⁶" stated for (i); "19 of 19" is right (19 indices are tested, `negctl_count.py`).

## 2. C2.2–C2.8

**C2.2 — CORRECT.** r_b = F + λ is strictly increasing; on M the error sets are complementary, so the identity
ν_b(E_1X ∩ M) = ν_a(E_1X ∩ M) − λν₂(E_2X ∩ M) + λν₂(M) holds.

**C2.3 — CORRECT.** (a): with ρ_b(Q) = (1+η)ρ_b(P), A = (c∖P) ∪ Q, both worlds strictly prefer X^{ij}_A, against
competitiveness on {i,j} at an open-edge index. (b): the cover P₁ ∪ P₂ = e_ij, the identifications
P₂ = e_ij ∩ S_i(X^{ij}_{R∖H}) and P₁ = e_ij ∩ S_j(X^{ij}_L), and the connectedness contradiction all check. The
null-level hypothesis is not even needed there: ess inf_{R∖c} r > λ₂ already gives r > λ₂ a.e. on R∖c. (c): the
discordant set is a countable union of rectangles {r<λ₁, r′>μ₂} × {r>λ₂, r′<μ₁}; (b) puts P inside and Q outside
one c_p; (a) for r′ gives μ₂ ≤ μ₁. (d) as in C2.1(5), with the G1 sentence added.

**C2.4 — GAP (wording).** The necessary direction gives pairwise comonotone ratios on M; the sufficient direction
(C2.1) needs the ratios to be monotone functions of the chain coordinate of a coherent path, plus (St). These
coincide only after showing that the comonotone ratios' level sets are coherent sector sets (true in spirit by
C2.3(b) and coherence of c_p, but not argued). *Fix:* replace "exact characterisation" by "a necessary condition
(C2.3(c)) and a sufficient condition (C2.1)".

**C2.5 — CORRECT for the listed abstract inputs; the last sentence overreaches.** C2.1 is an abstract edge system
with strict (G), the normal form, edge competitiveness, (K) and closed sections at edge test models, and no
leading density, so those inputs cannot prove (LD). But "Hence any proof of (LD) for n = 3 must use the link class
Q_i or the third world" also excludes proofs that use the R³-geometry of coherent edge models, competitiveness
against non-edge models, or interior indices, none of which C2.1 tests. A transported abstract system is not a
three-world ranking. *Fix:* "Hence any proof of (LD) for n = 3 must use an input outside this list: the third
world, the link class, interior indices, or the shape of coherent edge models in R³."

**C2.6 — CORRECT.** Step 1: comonotone (X, Y) = (1/A, ψ_b/A) on R_12 has Y ∈ [F(X−), F(X+)]; the law of A on W has
no atoms, so ψ_b = Φ₁(A) a.e. on W. Step 3: Fubini on rectangles plus connectedness gives Φ₁ ≡ κ a.e. on I_A.
Step 4: monotonicity extends F(y) = κy to every interior point, with both one-sided limits, so ψ_b = κ wherever
A ∈ I_A; the same κ serves on R_13.

**C2.7 — CORRECT** for the stated linear-per-sign-class densities. The image of W under h ↦ (h₂/|h₁|, h₃/|h₁|)
(constants absorbed) is the convex open set {k₂A + k₃B > k₁ ∀k ∈ K′}, and both projections are (0,∞) because
k₂, k₃ > 0. The map is a submersion, so the law is equivalent to Lebesgue measure. The consequence for T1 (B1.3 +
M0closed(b)) holds at the status of M0closed(b).

**C2.8 — identity CORRECT** (by hand: the cross terms cancel because σ₁² = 1; numerically, max error 1.8·10⁻¹⁵ in
`ref_c2.py` §5). The two "concretely" bullets about edge conditions are not proved in the note. *Fix:* label them
CHECKED (sketch) or CONJECTURE.

## 3. C1: the dichotomy and the closure

**C1.1(a) — CORRECT.**
- K_2 is closed: it is the cone over a compact convex base that avoids 0.
- Strict separation of the compact B_1 from the closed cone K_2 gives ⟨f,·⟩ ≤ 0 on K_2 and ≥ α > 0 on B_1, and
  likewise for g.
- h₀ = f/α − g/β separates with margins ±1. The (c/8)-net and the Lyapunov realisation (range of a finite
  non-atomic vector measure = {∫φ : 0 ≤ φ ≤ 1}, with 0 ≤ h^± ≤ 1/2) give γ(A) − γ(B) ≥ c/2 on Γ_ij and
  σ(B) − σ(A) ≥ c/2 on Γ_ik.
- Uniform integrability of the norm-compact Γ_ij gives e with sup γ(e) < c/2, and μ(A ∪ B) ≤ μ(Q_i)/2 leaves room
  for it.
- This yields the 2-cycle Y ≺ Y′ ⊏⊏_ij Z ⊏⊏_ik Y.
- *Cosmetic:* "Y △ Z ⊆ Y △ Y′ ∪ (Y′ △ Z) ⊆ Q_i" should read "all three models agree off Q_i".

**C1.1(b) — CORRECT.** Every ν ∈ G ∖ 0 has λ, λ′ > 0 and so is > 0 a.e. on M. ⪯_G is an (IB)-closed preorder
containing ⊑_ij ∪ ⊑_ik, so ⪯^gl ⊆ ⪯_G. For strict (G), split S into S ∩ R_ij and S ∩ Q_k and take two ⊑-steps.
Endorsement is the inclusion ⪯^gl ⊆ ⪯_G. Independent check (`ref_c1.py`, 400 random cell instances): exactly one
of "G ≠ {0}" and "a separating h exists" holds in every instance (158/242/0/0).

**C1.2 — CORRECT.**

**C1.3 — CORRECT** (all steps re-derived).
- *Farkas.* The system in t ∈ V* is finite. A certificate (λ, μ) ≥ 0 with Σλρ|Q_i = Σμσ|Q_i is a member ν of G
  with ν(δ) < η(Σλ + Σμ). This is impossible for η < θc₀, because ν(M) ≥ c₀(Σλ + Σμ). Independent check
  (`ref_c1.py`): θ > 0 ⟺ a decomposition with η > 0 exists, in 790/790 random cases.
- *Rounds.* F_r has content (δ′1_{Q_j∪Q_i} + τ₁)/m = φ/m. S_r has (δ′1_{Q_k} − τ₁)/m = ψ′/m, using
  u ⊆ Q_k ∪ Q_i.
- *Last step.* S_m has ψ′/m − T(1_y) + 1_u ≥ ψ′/m once σ_m(y) ≤ σ_m(u), and σ_m(y) = O(1/m).
- *Mirror mode.* S_0 = σ(u) − σ(y′) > 0 for m large, and S_m = ψ′/m + T(1_{y′}).
- *Bookkeeping.* The states of x and y are consistent across rounds. Disjoint x, y with prescribed vector
  integrals exist once ‖g₁‖_∞ ≤ m (Dvoretzky–Wald–Wolfowitz). The halving in Case 2 is valid because each ν ∈ G is
  a generator combination on R_ij and on Q_k, and D″ ∩ Q_i is non-null.
- (UI) ⟺ T_S onto for every non-null S ⊆ Q_i: correct (annihilator argument in finite dimension).
- *Script.* `run_chain` rejects a step only if a generator integral is `< 0`. So the NUMERICS confirm weak
  acceptance, while C1.3 claims strict acceptance (needed for C1.7). *Fix:* reject at `<= 0` for every non-vacuous
  step, or reword the NUMERICS line as "weakly accepted".

**C1.4 — CORRECT** (C1.3 + C1.1(b)). "CP-a with credal set G up to boundary ties" is informal; harmless.

**C1.5 — CORRECT; one line to add.** Farkas gives a functional φ ≥ 0 on Ĝ_ij with φ(ρ_{l₀}) < 0. Strict positivity
on Ĝ_ij ∖ 0 needs "Ĝ_ij is pointed (it consists of positive measures), so φ + ε·(ν ↦ ν(R_ij)) is > 0 on Ĝ_ij ∖ 0
and still negative at ρ_{l₀} for small ε; extend it to f ∈ L^∞(R_ij) by Hahn–Banach". The rest checks: ν(δ) =
∫f ν|R_ij > 0 for every ν ∈ G ∖ 0, because ν|R_ij ≠ 0.

**C1.6 — CORRECT at the status of M0closed(b); scope wording required.**
- *Kind (i).* K_1 ∩ K_2 = {0} contradicts strict (G) by C1.1(a). Otherwise any ν ∈ G ∖ 0 plus μ|N_+ is a strictly
  positive countably additive weight endorsing every comparison between regular models, which includes every
  relevant one.
- *Kinds (ii)–(iv).* These are Cor CPaU(b), S21 and B3.2 (B3_referee: CORRECT).
- *Conclusion.* (M0) holds, so M0closed(b) applies. (UI) is indeed not needed.
- *Scope.* Kind (i) assumes every comparison is G-weak, so it is nearly CP-a by hypothesis. The §0 lines "The glued
  credal design is dead … There is no third case" and "the object task (2) presupposes … does not exist" are true
  of the closure and of G-weak worlds only. Γ-leading worlds with further comparisons (the G-band) are open:
  C1.Q, which §5 concedes.
- *Fix:* replace the §0 headline by "Every glued world whose comparisons are G-weak (in particular the glued closure)
  either collapses or adds up; the residual of the design is the incomplete G-band (C1.7–C1.9, Question C1.Q)".

**C1.7 — CORRECT.** (L1_G) is C1.3. In (L2_G), M ∖ E_iX is non-null, e is small against every member of the compact
G_1, X ≺ X′ ⪯ C ⪯ X, and this is the right strict cycle.

**C1.8 — CORRECT at CHECKED.** As written, the pieces satisfy only P ⪯_i S. Savage's fineness needs P ≺ S. *Fix:*
apply (L1_G) to S′ ⊊ S with S ∖ S′ non-null and m_{S′} > max ν(P); then P ⪯ S′ ≺ S by strict (G). Savage, then
B3.1–B3.2, as stated.

**C1.9 — CORRECT.**
- G_1 is norm-compact for norm-compact Γ's: λ, λ′ are bounded by the normalisation and min γ(R_ij) > 0. It is
  convex.
- ν ↦ ν(δ) is continuous. The finite intersection property gives a common endorser, which is > 0 a.e.
- Minimax (Sion, compact convex G_1 × Δ_n, bilinear) gives c.
- Independent check (`ref_c1.py`): "common endorser in G_1" and "finite obstruction" are exclusive and exhaustive,
  23/135/0/0.
- The closing paragraph ("cannot be chained: their supports must cross") is unproved. *Fix:* mark it heuristic, or
  delete it.

## 4. Reading for the programme (nearby true statements)

- (LD) in its n-independent form is dead. The nearby true statements are:
  - two worlds: a leading density exists iff the edge credal set is a ray (C2.3(d));
  - three worlds: proportionality under non-degenerate link pricing (C2.6, C2.7).
- The right replacement aim is C2.C, together with C1.Q. These are the same residual seen from two sides: an
  incomplete edge-credal world whose interior comparisons are not G-weak. C2.6 shows that C2.C needs only the link
  class. C1.9 shows that a counterexample to "credal edges ⇒ adds up" needs a finite G-obstruction.
- A useful single target is therefore: "under (S) with closed sections for every model, a Γ-leading world (F, UI)
  admits no finite G-obstruction". If that is proved, C1.Q is answered negatively, and the density-unanimity part of
  B1.4's escape is closed for T1.

## 5. Required edits (all small)

1. C2.1(3): the endpoint sentence (G2).
2. C2.1(5): the ρ ≥ 0 sentence (G1); "(P1) applied twice" (G3); optionally the S21-free closing.
3. C2 §0: "(Co) and (St)" in place of "comonotone".
4. C2.4: "necessary condition / sufficient condition".
5. C2.5: the reworded final sentence.
6. C2.8: labels.
7. C1 §0 and C1.6: the scope sentence.
8. C1.5: the pointedness and perturbation line.
9. C1.8: strict fineness.
10. C1.9: the closing paragraph marked heuristic.
11. `glue_dichotomy.py`: check strict acceptance, or reword the NUMERICS line.
12. Cosmetic: C1.1(a) "agree off Q_i"; the C2 NUMERICS bound −1.4·10⁻¹⁶ for system (ii).
