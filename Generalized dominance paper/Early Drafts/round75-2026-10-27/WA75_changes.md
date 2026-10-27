# WA75: changes to the application paper

Base: `REFL75_core.tex`. Output: `app_revised.tex`, `app_revised.pdf` (17 pages). The PDF compiles cleanly with pdflatex: no warnings, no undefined references, no overfull or underfull boxes. The full diff against the base is in `WA75_app.diff`.

Theorem 4.1 (`thm:dominance`), Corollary 4.10 (`cor:admissible`) and Proposition 5.5 (`prop:axioms`) keep their numbers. Within Section 1, numbers after Definition 1.5 move up by one because a new remark was inserted. Lemma `lem:measure` is now 1.7, `def:advice` 1.9 and `prop:advice` 1.10.

## 1. Names (brief item 1)
- Every definition now has a short name:
  - Worlds and gambles
  - States and credal sets
  - The measure
  - Atoms and diffuse part
  - Models and coherence
  - Advice
  - Support
  - Supporting states and coherent hull
  - Changes
  - Margin triples
  - Consolidation of a model
  - Rankings
  - Dominance
  - Axioms
  - Sure-gain conditions
  - Score
  - Integral ranking
  - Fractional membership
- The axioms keep their names (Guidance, Three-model condition, Transitivity through ties, Consolidation, Admissibility of 𝒦).
- Lemmas, theorems, propositions and corollaries are unnamed.

## 2. Advice states (item 2)
- Definition 1.9 (Advice) now explains in plain English that f = g − h represents the choice between g and h. Taking g rather than h gains f(ω) at ω. Accepting f judges taking g rather than h worthwhile, and the advice on the choice depends on both judgements.
- The four states are listed (i)–(iv) exactly as in the brief.
- Proposition 1.10 and (M4) are kept.
- After (M4) in Definition 1.4, one new sentence: "whether a choice opportunity is negligible should not depend on which way round it is written".

## 3. What μ measures (item 3)
- New Remark 1.6 (What the measure represents):
  - μ gives the relative frequency or importance of advice opportunities.
  - Each result holds uniformly over every μ satisfying the conditions that result states.
  - No result is claimed for every finite Borel measure.
- A table gives a plain-English sentence for each of (M1), (M2), (M3), (M3′) and (M4), with the results that use it.
- The old "uses" paragraph at the end of Definition 1.5 is replaced by this table.
- `\usepackage{array}` is added for the table.
- I checked the whole text: no sentence says or suggests that a result holds for every finite Borel measure.

## 4. Consolidation explained (item 4)
- The gloss of (A4) keeps its first sentence. The old mass sentence is replaced by an "Explanation" list with five items:
  - **the two forms:** masses (m, m, m) and (m, m, 2m);
  - **what the masses supply:** they fix how much is replaced, not how often choices occur together. This item defines a *grouping of opportunities for comparison* with explicit groupings:
    - for the sum form, μ|G₁⊗μ|G₂⊗μ|G₃/m², which has total mass m and exactly the restricted marginals;
    - for the midpoint form, μ|G₁⊗μ|G₂⊗μ|G₃⊗μ|G₃/(4m³), which has total mass m, marginals μ|G₁ and μ|G₂, and ½μ|G₃ on each of the last two factors. Each group matches two original opportunities with two replacement ones.

    Because the per-group inequality holds for every group, the grouping does not matter;
  - **every context:** the axiom applies even where creating or resolving contradictory advice is involved, and silence is not treated as a default choice;
  - **judgements, not whole choices:** this is the item 7 caveat, below;
  - **the remaining commitment:** payoff advantages can compensate across advice opportunities. The measure makes the quantities comparable but does not establish that compensation. A final sentence notes that no coherent model satisfies the hypotheses on W, by the argument in the proof of Proposition 5.5, which uses no condition on μ.
- All the mass and marginal computations were checked by hand.

## 5. Two conclusions (item 5)
- Theorem 4.1 is unchanged: assuming (M2), (M3′) and (A1)–(A4), every incoherent model is dominated.
- Corollary 4.10(a) now reads: "If the ranking also satisfies (A5) for a family 𝒦 of coherent models, then every member of 𝒦 is undominated, while every incoherent model is dominated."
- Part (b) is marked "In particular" as the special case where 𝒦 is all coherent models.

## 6. Integral ranking and repair (item 6)
- Sections 5–6 are unchanged.
- Corollary 5.6 already lists (M4), and the existence measure is already symmetric (from REFL75).

## Correction to REFL75's Remark `rem:unordered`
- **The error.** The remark claimed μ(B∪(−B)) = π(B∪(−B)) = 2μ_π(B) for every Borel B. That is false when B∩(−B) has positive π-measure; for a symmetric B, μ_π(B) = π(B).
- **The correct identity.** Since 𝟙_B(f)+𝟙_B(−f) = 𝟙_{B∪−B}(f)+𝟙_{B∩−B}(f),

  μ_π(B) = ½π(B∪−B) + ½π(B∩−B).

  Hence μ_π(B) ≤ π(B∪−B) ≤ 2μ_π(B).
- **What survives.** The conclusion that μ ~ μ_π ⟺ (M4) still holds, and the remark now gives the two-line argument.
- **Use in the interpretation.** The identity is stated in the remark: a set with no pair f, −f carries half the weight of the choices it touches. The (A4) interpretation uses it.

## 7. Open check: G_i meeting −G_j (item 7)

**Verdict:**
- The formal axiom needs no change.
- The interpretation needed one caveat, which is now added. The units grouped in the comparison are single judgements (the acceptance of one oriented gamble), not whole choices.

**Why the axiom is unaffected:**
- **Nothing in the definitions involves −G.** Definitions 1.19, 1.20 and (A4) never refer to −G_i. Pairwise disjointness of G₁, G₂, G₃ already ensures that no judgement is both withdrawn and supplied.
- **The integral ranking still satisfies (A4).** The proof in Proposition 5.5 uses only additivity of m_ω over the disjoint sets G_i, so it covers overlapping triples unchanged.
- **The advice of W′ is well defined.** Under (M4), Proposition 1.10 makes the advice of W′ determined up to null sets whatever the overlaps.
- **The accounting stays consistent choice by choice.** Each judgement f contributes f(ω) with its own μ-weight. The two judgements on one choice therefore add up, and a choice that contributes to two parts is counted once for each judgement, with no double counting. Under a symmetric μ this matches the per-choice score of Remark 1.11:
  - strict advice for f: f(ω);
  - strict advice against f: −f(ω);
  - silence and contradictory advice: 0.

**What the overlaps mean (all checked by hand):**
- **−z ∈ G₁ (or G₂) and z ∈ G₃.** The consolidation reverses W's advice on that choice, from strict advice against z to strict advice for z. The margin condition then gives z ≥ (y + cκ𝟙)/(c+1) for every y ∈ G₂. This consequence is not stated in the paper.
- **z, −z ∈ G₃.** The consolidation supplies contradictory advice. Adding the two margin inequalities gives x + y ≤ −cκ𝟙 for all x ∈ G₁ and y ∈ G₂, so the withdrawn pairs are uniform sure losses. This is stated in the paper.
- **x ∈ G₁ and −x ∈ G₂.** Contradictory advice is withdrawn. Taking the pair (x, −x) gives z ≥ κ𝟙 for every z ∈ G₃. This is stated in the paper.
- **x, −x ∈ G₁.** The margin condition then gives z ≥ (|x| + y)/c + κ pointwise. This is not stated in the paper.

**Why not restrict the axiom instead:**
- An alternative is to restrict (A4) to triples with (∪G_i) ∩ −(∪G_i) = ∅, so that the units could be whole choices. That would weaken the axiom and require re-checking the dominance proof.
- In Lemma 4.6 (`lem:U2`), (U1) rules out every cross-overlap except G₁∩−G₁, and that one can be avoided by choosing G₁ inside a Borel half-space H with H∩−H = ∅. The Borel half-space comes from a countable separating sequence of functionals.
- Lemma 4.9 (`lem:gap`) was **not checked**.
- Since the axiom is consistent with the advice reading as it stands, no restriction is made.

## Style
- Plain English throughout, using \coloneqq and "models".
- None of the listed jargon words appear.
- No introduction, summary or discussion was added, and there is no commentary comparing versions.
