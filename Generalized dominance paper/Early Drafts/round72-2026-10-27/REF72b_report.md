# REF72b: referee report on INC72 (Fact 0, Fact H, Main theorem, Entrenchment) and AX72 (C1, C2, C3 spot-check)

27 Oct 2026. Sources: BRIEF72.md (with the REF72 fix that (G) applies only to X ≠ Y a.e.), INC72_report.md, AX72_report.md, app.tex §§2, 6. Hand proofs; numerics only as sanity checks (`ref72b_check.py`, plus a re-run of `check72.py`, all of which passed).

## Verdicts

| # | Claim | Verdict |
|---|---|---|
| 1a | INC72 Fact 0: R_σ ∈ 𝓡 for every truth-directed σ; R₀ ⊆ R_{s'} | **PROVED** (needs μ{P_S=0}=0 and μ{h(ω)=0}=0; both hold for Gaussian μ) |
| 1b | INC72 Fact H(a),(b) | **PROVED** |
| 1c | INC72 Main theorem §2: in every R' ∈ 𝓡 with R' ⊇ R₀, X* has no weak dominator | **PROVED.** The case split is complete, and every constructed g is guided at world 1 with Z→X* unavailable. One remark in §2 is **WRONG** as stated (correction C1 below). |
| 1d | INC72 Q1 (Zorn for E-incl, finite Ω) | **CHECKED** |
| 2a | INC72 §3 Entrenchment lemma | **PROVED for atomless μ**. The proof silently uses atomlessness, which (M1)–(M3) do not imply. It does **not** need finite Ω. With atoms: **UNCLEAR** (correction C3). |
| 2b | INC72 §3 consequence (ii): every R' ∈ 𝓡 with R' ⊇ R_m makes every incoherent model strictly dominated at every world | **PROVED** for any Ω, assuming (M1), (M2) and atomless μ. The parenthetical "Y need not stay undominated" is **WRONG**, and in the safe direction (correction C2). "Coverage survives" is overstated: closure under ties is not shown. |
| 2c | INC72 §3(iii): an admissible tie can be added to R₀ | **CHECKED** |
| 3a | AX72 C1: the common-kink ranking satisfies C1 and leaves {f(h₁)+f(h₂)>0} undominated in a maximal member of 𝓡∩C1 | **PROVED** (checked in full) |
| 3b | AX72 C2 self-defeat: the mirror image D_Q^♯ of an admissible imprecise coherent model is incoherent and admissible | **PROVED** (needs reflection-invariant null sets, (M2) and (M3), all of which AX72 states) |
| 3c | AX72 C3 counterexamples E3–E5, C3.1, C3.7(i) | **No gross errors found** (spot-check only) |

---

## 1. INC72 Fact 0, Fact H, Main theorem

**Fact 0.**
- (R) and (I) hold.
- (G): a non-null guided change has Δ_ω = ∫_A|g_ω| + ∫_B|g_ω| > 0. Its reverse is non-null and not guided, and it has Δ < 0, so it is refused.
- (SC): every accepted comparison between distinct models has Δ_ω > 0.
- (P): the argument of Prop. `prop:protect` uses only clause structure and Lemma `lem:guidedeverywhere`.
- R₀ ⊆ R_{s'}: R_{s'} refuses only at non-guided worlds, and only for coherent-available changes. Clause (ii) changes are never coherent-available. So both clauses of R₀ survive in R_{s'}.

**Fact H.**
- (a): for q ∈ Q_A with q₂ > 0, some h ∈ A ⊆ R₁ has q₁h₁ ≥ q₂|h₂| > 2q₂h₁. So Q_A ⊆ {q₁ ≥ 2/3}, and Lemma `lem:states`(e) gives hull(A) ⊇ {h₁>0, 2h₁+h₂>0} = Q₊₊ ∪ S₁, modulo axes. If Q_A = ∅, then hull = E.
- (b): immediate.

**Main theorem: case analysis checked.**
- *Step A.* Correct.
- *Step B.* Correct.
  - A change guided at 1 from X* has A ⊆ R₁ ⊆ {h₂<0} and B ⊆ S₂ ⊆ P₂, so P₂ = D_{δ₂} can make it.
  - (G) gives C' ≻'₁ C. (I) transfers Y ⪰'₂ X* to C' ⪰'₂ C. That is a domination of a coherent model, contradicting (P).
- *Step C, choice of ω₀.* Correct. X* is the a.e.-unique maximiser of s'₁+s'₂, because {φ=0} is two rays.
- *Step C, the WLOG ω₀ = 1.* It is valid, but the reason is not "coordinate swap symmetry". The swap does **not** preserve s' (s'₁ is linear and s'₂ is kinked). The mirror case works because the score enters Step C only through c > 0 and through Δ_{ω₀}(g) ≤ 2∫_G‖h‖ → 0. Everything else (guidance, Lemma `lem:test`, regions, Fact H) is set-level and swap-equivariant. State this explicitly.
- *Completeness of the case split on A ⊆ R₁∪R₂∪Q₋₋.* If (a) fails, then A∩Q₋₋ is null and at most one of A∩R₁, A∩R₂ is non-null. So A ⊆ R₁ a.e. (b1), A ⊆ R₂ a.e. (b2), or A is null (b3). This includes the case "A ⊆ R₁ with A∩Q₋₋ null". The split is complete.
- *The constructed g and the unavailability of Z→X\*, case by case:*
  - **(a).** G is a tiny subset of the other half of A∩Q₋₋ (or of A∩R₂), with G ⊆ Y. Removing G is guided at 1, since Q₋₋ ∪ R₂ ⊆ N₁. Z→X* removes A∖G ⊇ K, and K is inconsistent by Fact H(b). Since Q_{superset} ⊆ Q_K = ∅ (Lemma `lem:hull`(a)), the change is unavailable. ✓
  - **(b1).** B∩S₁ is non-null because d is not anti-guided at 2 and A∩R₂ is null. G ⊆ B∩S₁ ⊆ P₁ and G∩Y = ∅, so adding G is guided at 1. Z→X* removes A and adds B∖G. If A is consistent, hull(A) ⊇ S₁ by Fact H(a), and (B∖G)∩S₁ is non-null. If A is inconsistent, the change is unavailable directly. ✓
  - **(b2).** Y∩R₁ = A∩R₁ is null, so adding G ⊆ R₁ ⊆ P₁ is a guided change from Y. Z∖X* = A∪G meets both R₁ and R₂ non-null, so it is inconsistent. ✓
  - **(b3).** B∩S₁ is non-null by the same reasoning as in (b1). Z→X* removes G ⊆ R₁ and adds B ⊇ B∩S₁, and S₁ ⊆ hull(G). ✓
- *Closing the chain.* In each case, X* ⪰₁ Z by clause (ii) of R₀ ⊆ R'. Then Y ⪰'₁ X* ⪰'₁ Z together with Z ≻'₁ Y violates (TC). If Z = X* a.e., then d would be anti-guided at 1, which is excluded.
- I could not break the theorem.

**One error in the §2 Remarks (correction C1).** The claim "X* and Y = X*∖B with B ⊆ S₁∪S₂ are incomparable at both worlds in R₀" is **WRONG** in general.
- If B ⊆ S₁, the change Y→X* adds B ⊆ P₁. It is guided at 1, so X* ≻₁ Y in R₀.
- If B is inconsistent, X*→Y is not coherent-available. Example: mass m at small balls near (1,−1.9) and (−1.9,1). Its world-1 increment is −∫_B h₁ ≈ 0.9m > 0, so Y ⪰₁ X* already holds in R₀. (X* then wins at world 2, where the increment is −1.05m, consistent with the theorem.)
- The remark is true when B meets both S₁ and S₂ in non-null sets and B is consistent.
- The theorem does not depend on the remark.

## 2. INC72 §3: Entrenchment and consequence (ii)

**Entrenchment lemma, steps checked.**
- *Existence of a guided move from Y.* σ_ω has P_ω as its a.e.-unique maximiser, and σ_ω(X) > σ_ω(Y), so Y ≠ P_ω a.e. This uses μ{h(ω)=0} = 0, which is (M2) for Q = {δ_ω}.
- *Convergence of the scores.* Δ_ω(Z_n→X) = c − Δ_ω(Y→Z_n) → c by dominated convergence, since g_ω is integrable. ✓
- *Adding case.* Write B_n for the set Z_n→X removes; B_n = B ∪ (G_n∖X) ⊇ B.
  - If B is inconsistent, so is B_n.
  - Otherwise, either Q_{B_n} = ∅, or Q_{B_n} ⊆ Q_B, in which case hull(B_n) ⊇ hull(B) by Lemma `lem:states`(e).
  - Then μ((A∖G_n) ∩ hull(B)) ≥ μ(A∩hull(B)) − μ(G_n) > 0 for large n. ✓
- *Removing case: the limiting / hull-convergence argument.*
  - The removed sets are B∖G_n ↑ B a.e. (∩G_n null), so Q_n := Q_{B∖G_n} is decreasing. Each Q_n is weak-∗ closed (Lemma `lem:hull`(a)) inside the weak-∗ compact S (Lemma `lem:states`(a)).
  - ∩Q_n = Q_B: a state that is a.e. non-negative on each B∖G_n is a.e. non-negative on their union, which is B a.e. ✓
  - If Q_B = ∅, the finite intersection property gives Q_n = ∅ for some n. ✓
  - If Q_B ≠ ∅, then P_{Q_n}(h) ↑ P_{Q_B}(h) pointwise. If P_{Q_n}(h) ≤ t < P_{Q_B}(h) for all n, a weak-∗ cluster point of minimisers lies in ∩Q_n = Q_B and has value ≤ t, which is a contradiction. Here q ↦ q(h) is weak-∗ continuous.
  - So hull(B∖G_n) increases to hull(B), and monotone convergence gives μ(A ∩ hull(B∖G_n)) ↑ μ(A∩hull(B)) > 0. Since the added set contains A, the change is unavailable for large n. ✓
  - The argument is correct, and it needs neither metrizability beyond Lemma `lem:states`(a) nor finite Ω.
- **Hidden hypothesis (correction C3).** "Take a decreasing sequence G_n ⊆ G, each non-null, with null intersection" requires G to have non-null subsets of arbitrarily small measure. That is, μ must be atomless (at least on guided sets).
  - (M1)–(M3) do **not** imply this. By (M2), atoms can sit exactly in D_S ∪ (−D_S): if inf a ≤ 0 ≤ sup a, some state has q(a) = 0 and μ{q=0} > 0. Atoms there are allowed. An example is a Gaussian plus a point mass at 𝟙, which satisfies (M1)–(M3).
  - If P_ω △ Y consists only of heavy atoms, the "tiny guided move" does not exist.
  - In the one such configuration I tried (Y = P₁ minus an atom at 𝟙), a different chain (remove a diffuse K ⊆ Q₊₊, add the atom) still proves entrenchment. So the lemma may survive with atoms, but this is **UNCLEAR**, not proved.

**Precise scope of the lemma.**
- Ω: arbitrary, as in the paper.
- E: as in the paper.
- μ: (M1), (M2), and atomless.
- σ_ω = ∫ g_ω dμ, with g_ω integrable and g_ω(h)·h(ω) > 0 a.e.
- R': any relation at ω that contains R_σ's relation at ω and satisfies (G) and (TC) at ω.
- The lemma is a per-world statement, so finiteness of Ω plays no role.

**Consequence (ii).**
- By Theorem `thm:main`(b) and Prop. `prop:strict`, R_m gives N ≺_ω X at every ω, with N coherent. Inclusion keeps the weak comparisons, and entrenchment, applied world by world, keeps the strictness. So N strictly dominates X in R'.
- **PROVED for any Ω** under (M1), (M2) and atomless μ.
- For infinite Ω, the existence of maximal members is still open (Zorn fails at (P)). So "every inclusion-maximal extension" may be vacuous there, but the statement for every R' ∈ 𝓡 above R_m stands.
- **Correction C2.** The parenthetical "(Y need not stay undominated in R′)" is **WRONG**. R' ∈ 𝓡 carries (P) with 𝓟 = all coherent models, so the coherent dominator *is* undominated in R'. Coverage requirements (5), (2), (4b) and (1) therefore all survive in R'.
- What is **not** shown is closure under ties (3). R' may tie an incoherent model with a coherent one at every world; nothing in 𝓡 forbids that. So "coverage survives every inclusion extension" should read "requirements (1), (2), (4b), (5) survive; (3) is not established".

**Consequence (iii).**
- d and −d each remove an inconsistent subset of Q₋₋, so no coherent model can make either. Both have Δ₁ = 0, so they are neither guided nor anti-guided at 1.
- Strict pairs still have Δ₁ > 0, which keeps (SC).
- R₀ rejects d and −d at world 1, so no strict pair of R₀ is collapsed. The tie is therefore even an E-strict extension.
- (P): a dominator of a coherent C would need C→Y to be d or −d at world 1, but those are unavailable to C. **CHECKED.**

## 3. AX72

**C1 (E1).**
- X*₁ = {f(h₁)+f(h₂) > 0} = {h₁+4h₂ > 0} ∪ {4h₁+h₂ > 0}. This is a non-convex cone; at the witnesses a, b, a+b, F takes the values 0.25, 0.25, −2.5 (numerically confirmed).
- **Refusal rule.** A dangerous change is non-guided at both worlds when there are two worlds:
  - Suppose it is guided at 1 and available to C. Then A misses D_S ⊆ C, so A ⊆ P₁∖Q₊₊ ⊆ N₂.
  - And B ⊆ C is consistent, so B∩Q₋₋ is null and B ⊆ N₁∖Q₋₋ ⊆ P₂.
  - So the change is anti-guided at 2, and Δ₂ < 0, so it is not dangerous.
  - Hence any choice of refusal world keeps (G).
- **C1 holds.**
  - If r is accepted at ω and satisfies the hypotheses toward ω', then d_{ω'} ≥ d_ω > 0, because f is common and increasing.
  - If r were dangerous, the rule would refuse it at ω. The 1→2 hypothesis triggers refusal at 1, and the 2→1 hypothesis triggers refusal at 2. Both cannot hold for a non-null r.
  - So r is not dangerous and is accepted at ω'.
- **Undominated in a maximal member.** The Bayes fact gives X*₁ ≻_ω Y somewhere for every rival Y. C1 is preserved by ⊑-chain unions. REF72 Lemma 2 (finite Ω) then gives a ⊑-maximal member of 𝓡∩C1 in which X*₁ is undominated. **PROVED.**
- R₀ satisfies C1 (CHECKED).
- The C1 violation by R_{s'} is CHECKED numerically: increments +0.1m at world 1 and −1.14m at world 2.

**C2 self-defeat.**
- ♯ is an involution on a.e.-classes when μ and −μ share null sets. Under C2 it preserves every relation ⪰_ω, hence dominance. So D_Q^♯ is admissible whenever D_Q is.
- D_Q^♯ = {max_Q q ≥ 0}, which is a.e. equal to {max_Q q > 0}; this uses (M2) and reflection.
- For q₁ ≠ q₂ in Q, pick k = αh + β𝟙 with q₁(k) = 1 and q₂(k) = −1. Then k−c𝟙 and −k−c𝟙 lie in the open set {max_Q q > 0}.
- Under (M3), Lemma `lem:identify`(a) puts both in any D_{Q'} that is a.e. equal to it. Their sum −2c𝟙 has sup < 0, so it is not in D_{Q'}. So D_Q^♯ is incoherent. **PROVED.**
- With 𝓟 = all coherent models, C2 is therefore outright incompatible with the objective, for every ranking.
- The R₀ violation of C2 is CHECKED: P_Q = −0.4 at both centres, and −A is inconsistent.
- E2's witnesses are CHECKED: 0.2 and −0.1. With odd g and symmetric μ, s(X^♯) = s(X). Guidance is ♯-invariant, so the dual-triggered refusals keep (G), and the strict defence still goes through.

**C3 (spot-check only).** No gross errors.
- E4: f(t) = 2t − |sin t| is superadditive (minimum gap ≥ 0 on 10⁶ pairs) with f' ∈ [1, 3]. The witnesses give 0.304 and −1.689.
- E5: g = min(t, (1+t)/2) is concave. The witnesses give 0.005 and −4.45.
- C3.1: the polar maps (r,φ) ↦ (τ(r), φ+θ(r)) have a triangular Jacobian of determinant τ'(r)·(r-factor), so they preserve μ iff τ transports the radial law. The construction of S is structurally sound.
- C3.7(i): concave + superadditive + g(0) = 0 gives positive homogeneity. That direction is correct.
- C3.7(ii) step 3 is honestly labelled outline-level. I did not referee it.

---

## Corrections to make

- **C1 (INC72 §2, Remarks).** Restrict the incomparability example to B consistent with non-null parts in both S₁ and S₂. For B ⊆ S₁ or B inconsistent, R₀ already compares X* and Y at some world.
- **C2 (INC72 §3(ii)).** Delete "(Y need not stay undominated in R′)". Under (P) with 𝓟 = all coherent models, the dominator is undominated. Replace "coverage survives" with "requirements (1), (2), (4b), (5) survive; closure under ties is not established".
- **C3 (INC72 §3, Entrenchment lemma).** Add the hypothesis "μ atomless", which holds for Lebesgue-equivalent μ on Rⁿ. State that (M2) is used (Lemma `lem:test`, and μ{h(ω)=0} = 0), and that finite Ω is not used. Mark the atomic case UNCLEAR. Under (M2), atoms can only lie in D_S ∪ (−D_S), which may make a repair easy.
- **C4 (INC72 §2, Step C).** Replace "by the coordinate swap" with the actual reason the mirror case works: the score enters only through c > 0 and the smallness of Δ_{ω₀}(g). s' itself is not swap-invariant.
- **C5 (INC72 item 4/5 headline).** Carry the atomless hypothesis into the headline statements of items 4 and 5.
