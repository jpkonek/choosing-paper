# INC72: inclusion-maximality (E-incl) in the score-free class 𝓡

27 Oct 2026. Setting: Ω={1,2}, E=R², μ standard Gaussian (positive density, finite first moment, null sets = Lebesgue null sets). Axioms (R),(G),(I),(SC),(P) exactly as in BRIEF72, with 𝓟 = all coherent models. Closure under ties is not assumed anywhere.

## Answers

1. **Q1. PROVED.** For finite Ω, unions of ⊆-chains in 𝓡 stay in 𝓡, so by Zorn's lemma every member of 𝓡 lies below an inclusion-maximal member. 𝓡 is nonempty. Unions can only turn strict pairs into ties, never the reverse. So (G) and (P) cannot fail in a union, and (SC) is preserved because every chain is finite.
2. **Q2. PROVED (negative).** Inclusion-maximality does not eliminate incoherent admissibility. Let R₀ be the manuscript's own rule (Def. `def:ranking`, app.tex) with the distorted score s′ in place of m. Then R₀ ∈ 𝓡, and in **every** R′ ∈ 𝓡 with R′ ⊇ R₀, X* has **no weak dominator** other than itself. So X* is undominated in every inclusion-maximal extension of R₀. Since R₀ ⊆ R_{s′}, this also covers every inclusion-maximal member containing R_{s′}. Tying X* to rivals cannot help.
3. **Q2 corollary. PROVED.** For any property Φ, if some member of 𝓡 with Φ extends R₀, then 𝓡+Φ does not imply that every incoherent model is dominated. This covers E-strict maximality, E-incl maximality, and every other extension principle that R₀ can meet.
4. **Q3(a). PROVED (entrenchment lemma).** For the manuscript rule R_σ with any truth-directed integral score σ, every strict comparison of R_σ stays strict in every R′ ⊇ R_σ that satisfies (G) and the three-model condition (TC). So above R_σ, E-incl extensions are E-strict extensions. The distinction between the two notions has no effect there.
5. **Q3(b). PROVED.** Dominance under inclusion-maximality is genuine where it occurs. In every R′ ∈ 𝓡 with R′ ⊇ R_m (the original covering ranking), every incoherent model is **strictly dominated at every world**, by the same coherent model as in R_m. Coverage therefore survives every inclusion extension, and it is not produced by an accumulation of ties.
6. **Q3(c). PROVED / CHECKED.** Guided changes are not the only strict comparisons in maximal rankings: maximal extensions of R_σ keep every clause-(ii) strict comparison (PROVED). Maximal extensions can contain ties between distinct models, which R_σ never has (CHECKED: an explicit admissible tie is added below). A full classification of maximal members is **not attempted**, and it is unclear whether some maximal member has guidance as its only source of strictness.
7. **Q4. Philosophical, kept separate.** Collapsing an established strict preference into a tie is a revision, not a gain in decisiveness, so E-incl maximality has a weaker rationale than E-strict maximality. By item 4 the point is moot for the rankings at issue.

Bottom line: under both E-strict and E-incl, maximality does not turn coherent admissibility into incoherent inadmissibility. The obstruction is already present in the minimal manuscript-rule ranking R₀, before any maximality is applied: X* is robustly undominated above R₀. **Nearby available result:** maximality *preserves* coverage. Every inclusion-maximal extension of a covering ranking of the form R_σ that dominates incoherent models still dominates them strictly (item 5). Any principle that yields the dominance theorem for every member must exclude R₀ itself. Note that R₀ satisfies disjoint additivity, has no ties, is positively homogeneous, and uses world-wise integral scores. So the needed condition must constrain how payoff magnitudes are aggregated *across* worlds. This matches the auditor's §4 diagnosis, but it is now forced by R₀ rather than by a maximal object.

---

## 0. Notation

For a change d = (A,B) (add A, remove B), the score change is Δ_ω(d) = σ_ω(A) − σ_ω(B), where σ_ω(X) = ∫_X g_ω dμ. Δ is additive along chains, because 1_X − 1_Z = (1_X − 1_Y) + (1_Y − 1_Z). A *truth-directed score* means g_ω is μ-integrable with g_ω(h)·h(ω) > 0 for μ-a.e. h. Examples are m (g_ω = h(ω)) and s′ (g₁ = h₁, g₂ = f(h₂), with f(t) = 2t for t ≥ 0 and t/2 for t < 0).

The **manuscript rule** R_σ accepts a change at ω iff (i) it is guided by ω, or (ii) no coherent model could make it and Δ_ω > 0. Define R₀ := R_{s′}^{rule}. This is **not** the auditor's R_{s′}: R₀ refuses every non-guided change that a coherent model could make.

**Fact 0. PROVED.** R_σ ∈ 𝓡 for every truth-directed σ, and R₀ ⊆ R_{s′}.
The proofs of Prop. `prop:structure` and Prop. `prop:protect` use only one property of the score: a non-null guided change strictly raises the score at its world. That holds here, since Δ_ω = ∫_A|g_ω| + ∫_B|g_ω| > 0. This gives (R), (I), (SC), (G), and (P), the last using μ{P_S = 0} = 0.
For the inclusion R₀ ⊆ R_{s′}:
- A guided change raises s′_ω, and R_{s′} refuses only at non-guided worlds.
- A clause-(ii) change is not coherent-available, and R_{s′} refuses only coherent-available changes.

**Regions** (all modulo null axes). P_ω = {h(ω) > 0} and N_ω = {h(ω) < 0}. Q₊₊ and Q₋₋ are the open quadrants.

| Part of… | Region | Definition |
|---|---|---|
| X* | S₁ | h₁ > 0, −2h₁ < h₂ < 0 |
| X* | S₂ | h₂ > 0, −2h₂ < h₁ < 0 |
| E∖X* | R₁ | h₁ > 0, h₂ < −2h₁ |
| E∖X* | R₂ | h₂ > 0, h₁ < −2h₂ |

Then X* = Q₊₊ ∪ S₁ ∪ S₂, and E∖X* = R₁ ∪ R₂ ∪ Q₋₋. These identities were also checked numerically in `check72.py`. Swapping coordinates swaps index 1 with index 2 and fixes X*.

**Fact H. PROVED.**
- (a) If A ⊆ R₁ is non-null, then Q_A ⊆ {q₁ ≥ 2q₂}, so hull(A) ⊇ Q₊₊ ∪ S₁. Symmetrically, for A ⊆ R₂, hull(A) ⊇ Q₊₊ ∪ S₂.
  *Proof.* If q ∈ Q_A, some h ∈ A has q₁h₁ ≥ q₂|h₂| > 2q₂h₁ when q₂ > 0. Then D_{conv{δ₁, (2/3, 1/3)}} = {h₁ > 0, h₂ > −2h₁}, and Lemma `lem:states`(e) gives the inclusion.
- (b) A non-null subset of Q₋₋ is inconsistent. A set with non-null parts in both R₁ and R₂ is inconsistent: (a) and its mirror give q₁ ≥ 2q₂ ≥ 4q₁, so q = 0.

## 1. Existence of inclusion-maximal members (Q1). PROVED

Let (R^α) be a ⊆-chain in 𝓡 (inclusion at each world), and let R be its union. Then:
- **(R) and (I).** Each world's relation is a union of sets of accepted changes, so both hold.
- **Strictness.** Y ≻_ω X in R means Y ⪰ X lies in some R^α and X ⪰ Y lies in no R^β. So a pair strict in R is strict in every stage that contains it. Unions only *lose* strictness, by creating ties.
- **(G).** Guided pairs are in every stage, and their reverses are in none. So (G) holds in R.
- **(SC).** A violating chain uses finitely many pairs. All of them lie in one stage, and the closing pair is strict there by the strictness point above.
- **(P).** If Y dominates a coherent C in R, the weak comparisons at the finitely many worlds lie in one stage R^α, and the strict comparison is strict in R^α. So Y dominates C in R^α, a contradiction.

The worry that ties might make (P) or (G) fail is unfounded: creating ties only removes strictness, so it can only remove dominance. With 𝓡 ∋ R₀ (or the guided-only ranking), Zorn gives maximal members above any given member.

Finite Ω is used **only** in the (P) step. With infinitely many worlds, the weak comparisons can appear at different stages with no common stage. This is the obstacle already noted in GUIDANCE §7, and it is unchanged under E-incl.

## 2. Main theorem (Q2). PROVED

**Theorem.** Let R′ ∈ 𝓡 with R₀ ⊆ R′, and let Y ≠ X* a.e. Then for some ω, Y ⪰′_ω X* fails. Hence X* has no weak dominator in R′, and it is undominated in every inclusion-maximal extension of R₀ (and of R_{s′}).

Write d = X*→Y = (A,B), with A = Y∖X* ⊆ R₁∪R₂∪Q₋₋ and B = X*∖Y ⊆ Q₊₊∪S₁∪S₂.

Sign table for d:

| World | Good part | Bad part |
|---|---|---|
| 1 | A∩R₁, B∩S₂ | A∩(R₂∪Q₋₋), B∩(Q₊₊∪S₁) |
| 2 | A∩R₂, B∩S₁ | A∩(R₁∪Q₋₋), B∩(Q₊₊∪S₂) |

**Step A: d anti-guided at some ω.** Then d is non-null and its reverse is guided, so X* ≻′_ω Y by (G), and Y ⪰′_ω X* fails.

**Step B: d guided at some ω.**
- A guided-at-1 change from X* adds A ⊆ R₁ ⊆ {h₂ < 0} and removes B ⊆ S₂ ⊆ {h₂ > 0}. So it is available to the coherent model P₂ = {h₂ > 0} = D_{δ₂}. Symmetrically, a guided-at-2 change is available to P₁.
- Let C′ be the result of applying d to that model C. By (G), C′ ≻′_ω C.
- If Y ⪰′_{ω′} X* held at the other world, then (I) would give C′ ⪰′_{ω′} C. So C′ would dominate C, contradicting (P).

(A change guided at both worlds from X* is null: it would add part of Q₊₊∖X* = ∅ and remove part of Q₋₋∩X* = ∅.)

**Step C: d mixed at both worlds** (a non-null good part and a non-null bad part at each world).
- Choose ω₀ with c := Δ_{ω₀}(Y→X*) > 0. This exists because X* uniquely maximises s′₁ + s′₂ = ∫(h₁ + f(h₂)), and the zero set of the integrand is two rays, hence null.
- By the coordinate swap, take ω₀ = 1. The case ω₀ = 2 is the mirror image (swap R₁↔R₂, S₁↔S₂).
- We construct a non-null change g from Y, guided at 1 and *tiny* (Δ₁(g) < c), with the following property. Set Z = Y + g. Then Z→X* cannot be made by any coherent model (Lemma `lem:test`).
- Then Δ₁(Z→X*) = c − Δ₁(g) > 0, so X* ⪰₁ Z in R₀ ⊆ R′ by clause (ii). Also Z ≻′₁ Y by (G).
- So Y ⪰′₁ X* would give the chain Y ⪰′ X* ⪰′ Z together with Z ≻′ Y. This violates (TC), and hence (SC).
- Tiny pieces exist because μ is non-atomic, and Δ₁(g) ≤ 2∫_G‖h‖dμ → 0 as μ(G) → 0.

The cases for A:
- **(a) A∩Q₋₋ non-null, or A∩R₁ and A∩R₂ both non-null.**
  - Let K be half of A∩Q₋₋, or let K = (A∩R₁) ∪ (half of A∩R₂). K is inconsistent by Fact H(b).
  - Let g remove a tiny piece of the other half. That piece lies in Q₋₋ or R₂, both inside N₁, so g is guided at 1.
  - Then Z∖X* ⊇ K, so Z→X* removes an inconsistent set.
- **(b1) A ⊆ R₁, non-null.**
  - Since d is not anti-guided at 2 and A∩R₂ = ∅, the set B∩S₁ is non-null.
  - Let g add a tiny piece G of B∩S₁ (G ⊆ S₁ ⊆ P₁, G∩Y = ∅), leaving a non-null remainder.
  - Then Z→X* removes A and adds B∖G, which meets S₁ ⊆ hull(A) (Fact H(a)) in a non-null set.
- **(b2) A ⊆ R₂, non-null.** Let g add a tiny G ⊆ R₁. This is guided at 1, and R₁∩Y = ∅. Then Z∖X* = A ∪ G is inconsistent by Fact H(b).
- **(b3) A null.**
  - Let g add a tiny G ⊆ R₁.
  - Since d is not anti-guided at 2, the set B∩S₁ is non-null.
  - Z→X* removes G and adds B, which meets S₁ ⊆ hull(G) in a non-null set.

This covers every case. ∎

**Remarks.**
- The proof uses (I) and (P) only in Step B, and there only for P₁ and P₂. It uses only the three-model instance of (SC). It never uses R₀'s refusals: only its clause-(ii) acceptances and (G).
- So tying X* with everything it can be tied with cannot help. A tie at both worlds is a weak dominance, and weak dominance of X* is already impossible in every extension.
- In R₀ itself, X* and Y = X*∖B with B ⊆ S₁∪S₂ are **incomparable at both worlds**, since the change adding B is coherent-available and not guided. Even so, no extension can make Y ⪰′ X* at ω₀. So X* need not be strictly ahead in R₀ for every rival; the protection comes from chains entrenched by (G). This differs from the auditor's mechanism, which keeps X* strictly ahead at some world under R_{s′}.

## 3. Shape of inclusion-maximal rankings; genuineness (Q3)

**Entrenchment lemma. PROVED.** Let σ be truth-directed. If X ≻_ω Y in R_σ, then X ≻′_ω Y in every R′ ⊇ R_σ satisfying (G) and (TC) at ω.

*Proof.*
- **Guided case.** If Y→X is guided, (G) gives the claim.
- **Otherwise.** Then d = Y→X = (A,B) is not coherent-available, and Δ_ω(d) = c > 0.
- **A guided move from Y exists.** Y ≠ P_ω a.e., because P_ω maximises σ_ω. So there is a non-null guided-at-ω set G: either G ⊆ P_ω∖Y (to add) or G ⊆ N_ω∩Y (to remove).
- **Shrinking pieces.** Take a decreasing sequence G_n ⊆ G, each non-null, with null intersection. Let Z_n = Y △ G_n. Then Δ_ω(Z_n→X) → c.
- **Z_n→X stays non-available for large n.**
  - *Adding:* the removed set grows (B ⊆ B_n), so inconsistency persists or the hull grows. The added set is A∖G_n, with μ((A∖G_n) ∩ hull(B)) → μ(A ∩ hull(B)).
  - *Removing:* the removed set is B∖G_n ↑ B, and Q_{B∖G_n} ↓ Q_B. If Q_B = ∅, some Q_{B∖G_n} = ∅, by compactness. Otherwise, by compactness, min over Q_{B∖G_n} of q(h) increases to min over Q_B of q(h). Then monotone convergence gives μ(A ∩ hull(B∖G_n)) → μ(A ∩ hull(B)) > 0.
- **Conclusion.** For large n, X ⪰_ω Z_n in R_σ and Z_n ≻′ Y. So Y ⪰′ X would violate (TC). ∎

**Consequences.**
- **(i) Strict comparisons persist. PROVED.** Above any R_σ, every R′ ∈ 𝓡 keeps all of R_σ's strict comparisons. So E-incl and E-strict extensions coincide there, and maximal extensions of R_σ keep every clause-(ii) strict comparison. Guided changes are therefore not the only strict comparisons.
- **(ii) Coverage survives. PROVED.** In R_m, every incoherent X is uniformly dominated by a coherent Y with Y ≺_ω X at every world (Thm `thm:main`(b), Prop. `prop:strict`). In any R′ ∈ 𝓡 with R′ ⊇ R_m, the weak comparisons persist, and the strict ones persist by (i). So Y **strictly** dominates X in R′, and the dominance is genuine. (Y need not stay undominated in R′; the objective does not require it.)
- **(iii) Ties occur. CHECKED.**
  - Take d = (A,B) with A and B both inconsistent (for instance, pieces in Q₋₋ on each side), with Δ₁(d) = 0. Such a d exists by continuity of Δ₁ in the radius of a ball.
  - Adding the tie {d, −d} at world 1 to R₀ keeps the ranking in 𝓡:
    - (G): a non-null change with Δ = 0 is neither guided nor anti-guided.
    - (SC): every strict pair still has Δ₁ > 0, while every chain has Δ₁ ≥ 0.
    - (P): neither d nor −d is available to any coherent model.
  - So maximal extensions can tie distinct models, which R₀ never does. Whether **every** maximal member has ties, and whether some maximal member has guided changes as its only strict comparisons, is **unclear**; it was not pursued.
- **(iv) Starting point decides dominance.** Whether dominance occurs in a maximal ranking depends on the starting ranking, not on the extension notion. Above R_m every incoherent model is strictly dominated. Above R₀, X* is not even weakly dominated.

## 4. Is losing established strict preferences defensible? (philosophy, separate)

E-incl maximality allows a ranking to grow by turning a strict verdict "X is more accurate than Y at ω" into a tie. That is not resolving an open question. It retracts an answer already given, and so it makes the ranking *less* decisive about that pair. The usual motivation for maximality is decisiveness: settle every comparison you consistently can. That motivation supports E-strict extensions (Suzumura's notion), not E-incl ones. E-incl is defensible only if one treats the weak relation as the sole primitive and strictness as the mere absence of an acceptance. On that reading, a strict preference has no standing beyond "not yet accepted in reverse", which sits badly with axioms like (G) that impose strictness as a substantive requirement. In any case the entrenchment lemma makes the issue largely idle here: for rankings of the manuscript's form, guidance plus three-model consistency already forbids collapsing any strict preference. So E-incl buys no extra power against the counterexample. Recommendation: do not adopt E-incl as the official maximality notion. The inclusion branch should be closed with the theorem in §2.

---
Files:
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r72/INC72_report.md`
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r72/check72.py` (NUMERICS: sampling sanity checks of the region identities and Fact H only; no proof relies on it).
