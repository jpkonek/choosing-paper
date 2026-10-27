# LDGO67: proof outline for the definitive LDG

26 October 2026. Role: LDGO67 (BRIEF67). The source is LDG v3.3 (`LDG_v3.3.tex`, 43 pages). Binding inputs: `AUDIT_r67_message2.md`, BRIEF67 decisions 3–5, `CC67_notes.md`, and `REF67_cc_notes.md`, which arrived before this outline was finished and is incorporated throughout.

**Revision 2.** The referee report `REF67_ldgo_notes.md` found the mathematics correct. This revision makes its required changes 1–8. It also adopts its recommendations A–G, as the lead instructed:
- the loss-ranking Example 5.6 is now the main example;
- the direct argument is now the proof in Example 4.7;
- randomisation, one sentence locating Joyce's error, and Proposition B.6 (marked optional) are kept in condensed form;
- the cross-paper point about the Zorn lemma is recorded in Part 4.

The paper contains no pointers to v3.3 proofs. Every "[v3.3 n.m]" tag below is provenance for this outline only, and the proof is copied into the paper.

This is a mathematical skeleton, not a manuscript. Every statement below is written the way it should appear in the paper: in words, with no labels such as (B), (S), (I), (CC), (W), and no "certificates", "records", "safe" or "routes". The glossary (Part 10) maps the old terms to the new ones.

## Status labels

- **[v3.3 n.m]** Carried over from LDG v3.3, result n.m, which passed the earlier review rounds. The proof is either unchanged or only reworded. Where the statement is reworded, the reason is given.
- **[CC67; refereed REF67_cc]** Proved in CC67 and independently checked by REF67_cc, which found no error. REF67_cc's repairs are made here.
- **[REF67_cc]** Proved by the referee REF67_cc and not checked by anyone else. Each such result is a few lines long.
- **[assembled]** Combines refereed results with no new argument. The assembly is given in full.
- **[new here; unrefereed]** My own argument. The appendix lists all of these. After REF67_ldgo, no unrefereed mathematics remains except the short revision-2 copies listed there.

## Conventions for the manuscript

- Theorem-like environments are unnamed: `\begin{theorem}\label{...}`.
- Definitions use `\coloneqq`.
- The objects are always called "models".
- Dominance nomenclature:
  - *weakly dominates*: at least as good at every world;
  - *dominates*: weakly dominates, and the two are not tied at every world;
  - *strictly dominates*: strictly better at every world;
  - *uniformly dominates*: better by a fixed ε > 0 at every world, with finite losses.
- No commentary comparing versions.

---

## Manuscript plan (order of sections; estimated length)

| § | Title | Content | Pages |
|---|---|---|---|
| 1 | Introduction | The headline results stated informally: Theorems 4.2 and 5.1 (Bayes choices with lower semicontinuous losses), probabilism on arbitrary domains (Theorem 8.2), and proper scores. Then the general theorem behind them (Theorems 4.3 and 5.2). | 1.5 |
| 2 | Models, rankings and dominance | Part 1 below | 1.5 |
| 3 | Coherence and the dominance conclusion | Part 1 below | 1.5 |
| 4 | Finitely many worlds | Part 2 below; Figures 1 and 2 | 3.5 |
| 5 | Infinitely many worlds | Part 3 below | 3 |
| 6 | Margins, Bayes models and strict dominance | Part 3, §3.4 below | 2.5 |
| 7 | What the dominance conclusion gives | Part 5 below | 2 |
| 8 | Applications | Part 6 below | 5 |
| 9 | Constructing rankings; scope | Parts 7–8 below | 1.5 |
| | References | | 1 |

**Estimated total: 23–25 pages**, against 43 for v3.3, or 24–26 with the optional Proposition 4.8. There is no appendix. If the editor wants one, §6 and the proofs in §8.3 can move there without renumbering the main results.

**Dependency chain** (for the reader of this outline; the paper has no table):

```
Lemma 4.1 (KKM) ──┬─ Theorem 4.3 (finite, any ranking) ── Cor 4.4 (closed competitive choice) ── Theorem 4.2 (finite, Bayes choices)
                  ├─ Theorem 5.2 (any worlds, any ranking; compactness step)
                  └─ Theorem 5.1 (any worlds, Bayes choices; direct proof; derivation from 5.2 is a remark)
Lemma 2.3 (Bayes ⇒ competitive) feeds Theorems 4.2, 5.1 and 6.1
Theorem 6.1 (margins) ── Cor 6.2 (Bayes models exist), Prop 6.3 (strict = uniform, finite worlds)
Prop 3.1 (consequences of the dominance conclusion) ── §7 (permissibility, transitivity)
§8 applications ← Theorems 4.2 / 5.1, 6.1, Prop 6.3
```

Theorems 4.2 and 5.1 can be proved directly from the refereed v3.3 argument, without Theorem 5.2. So no application depends on the new local theorem. The local theorem is the general statement behind them, and CC67 and REF67_cc have checked it.

---

## Part 1. Setting and dominance notions (manuscript §§2–3)

### 1.1 Worlds, models, rankings

- Ω is a nonempty set of **worlds** and M a nonempty set of **models**. Neither carries any structure.
- A **ranking** L has a nonempty **evaluation domain** M_L ⊆ M. For each world ω it has a binary relation ⪯_ω on M_L. We read m ⪯_ω m′ as "m performs at least as well as m′ at ω". We write m ≺_ω m′ when m ⪯_ω m′ and not m′ ⪯_ω m.
- **No property of the relations is assumed.** They need not be reflexive, transitive or complete. When they are reflexive and transitive we speak of a **preorder ranking**.
- A **loss** L: M_L × Ω → [0,∞] generates a ranking: m ⪯_ω m′ iff L(m,ω) ≤ L(m′,ω). Smaller losses are better. A loss ranking is a complete preorder ranking. L(m) ≔ L(m,·) is the **loss profile** of m.
- Δ_F is the simplex of **priors** on a finite nonempty F ⊆ Ω, with the Euclidean topology. supp p ≔ {ω : p_ω > 0}, and δ_ω is the point mass. A prior p **charges** ω if p_ω > 0. For finite Ω, Δ ≔ Δ_Ω.

### 1.2 Dominance notions [v3.3 §1]

All of these are defined model by model, relative to one ranking.
- c **weakly dominates** m if c ⪯_ω m at every world.
- m and c are **tied at every world** if each weakly dominates the other.
- c **dominates** m if c weakly dominates m and the two are not tied at every world. Given weak dominance, this holds iff c ≺_ω m at some world. No property of the relations is needed for this equivalence.
- c **strictly dominates** m if c ≺_ω m at every world.
- For a loss ranking, c **uniformly dominates** m if L(c) is finite and, for some ε > 0, L(c,ω) + ε ≤ L(m,ω) at every world. For finitely many worlds, strict and uniform dominance coincide.
- **On S**, for a nonempty set S of worlds: the same notions with Ω replaced by S.
- c is **competitive on S** if every model m has some world ω ∈ S with c ⪯_ω m.
- U_L ≔ the undominated models of M_L.

**Lemma 2.1** [v3.3 §1]. A model competitive on S is not strictly dominated on S. If the relations at the worlds of S are complete, the converse holds.

*Proof.* If m strictly dominated c on S, no ω ∈ S would have c ⪯_ω m. Conversely, with completeness, failure of c ⪯_ω m at every ω ∈ S gives m ≺_ω c at every ω ∈ S. ∎

### 1.3 Loss rankings, Bayes models, lower semicontinuity [v3.3 A.1–A.2]

- For a finitely supported prior π, the expected loss is π·L(m) ≔ Σ_{ω∈supp π} π_ω L(m,ω). Worlds that π does not charge do not enter, even if the loss there is infinite.
- V(π) ≔ inf_{m∈M_L} π·L(m). A model is a **Bayes model for π** if π·L(m) = V(π).
- A function h is **lower semicontinuous** if every set {h ≤ a} is closed. In words: at a limit, loss may drop but cannot jump up.

**Lemma 2.2** [v3.3 A.1]. Let each f_ω be strictly increasing on a set containing the values of L(·,ω), and put L′(m,ω) ≔ f_ω(L(m,ω)). Then L and L′ generate the same ranking. Hence every hypothesis and conclusion of §§3–5 and §7 that refers only to the ranking holds for L′ iff it holds for L. If each f_ω is continuous, lower semicontinuity of the losses along a family transfers as well.

*Proof.* f_ω preserves and reflects ≤. A continuous increasing function of a lower semicontinuous function is lower semicontinuous. ∎

**Lemma 2.3** [v3.3 A.2]. If c is a Bayes model for a finitely supported π, then c is competitive on every S ⊇ supp π.

*Proof.* Suppose some m has L(m,ω) < L(c,ω) for every ω ∈ S. Then π·L(m) is finite.
- If π·L(c) = ∞, then π·L(m) < π·L(c).
- Otherwise every term is strictly smaller, since π_ω > 0 on supp π ≠ ∅.

Either way c is not Bayes for π. Completeness of loss rankings and Lemma 2.1 turn "not strictly dominated on S" into competitiveness. ∎

### 1.4 Coherence, the family of rankings, and the dominance conclusion [v3.3 §2 opening, §3.1]

- The **coherent class** C ⊆ M is given in advance, independently of the rankings.
- 𝔏 is a family of **reasonable rankings**.
- For L ∈ 𝔏, the **undominated coherent models** of L are
  C_L ≔ {c ∈ C ∩ M_L : no m ∈ M_L dominates c}.
  So C_L ⊆ U_L, by definition.

Four conditions on the family carry descriptive names. They are stated in words inside every result that uses them.
- **Evaluability:** every model is evaluated by some ranking in 𝔏.
- **Coherent admissibility:** every coherent model is an undominated coherent model of some ranking in 𝔏.
- **Closure under ties** (for one ranking L): a model tied at every world with an undominated coherent model of L is itself an undominated coherent model of L.
- **The dominance conclusion** (for one ranking L): every evaluable model is weakly dominated by an undominated coherent model of L.

Two points about these conditions.
- *Nonemptiness of C_L is not a separate assumption.* Every theorem below has hypotheses that supply members of C_L.
- *The point of closure under ties.* Different models may be tied at every world, for example when they differ only in a way the ranking cannot see. An incoherent model tied with an undominated coherent one is not dominated by it. Closure under ties excludes this. It compares individual models and does not presuppose that ties are transitive.

**Proposition 3.1** [v3.3 3.1].
- (a) Suppose every evaluable model is weakly dominated by an undominated coherent model. Then every undominated model is tied at every world with an undominated coherent model. If closure under ties also holds, then:
  - the undominated models are exactly the undominated coherent models;
  - every other evaluable model is dominated by an undominated coherent model.
- (b) Conversely, suppose every undominated model is coherent, and every incoherent evaluable model is dominated by some undominated model. Then the undominated models are exactly the undominated coherent models, and every incoherent model is weakly dominated by one of them.

*Proof.*
- (a) Let m be undominated, and let c ∈ C_L weakly dominate it. If not m ⪯ c, then c dominates m. So m and c are tied. Under closure under ties, a model m ∉ C_L is not tied with its weak dominator c ∈ C_L. Since c ⪯ m, it follows that not m ⪯ c, so c dominates m. Hence U_L ⊆ C_L ⊆ U_L.
- (b) C_L = C ∩ U_L, which is U_L when U_L ⊆ C. Dominance implies weak dominance. ∎

**Example 3.2** [v3.3 3.2; keep as two sentences]. The dominance conclusion is stronger than the statement that undominated = coherent and every incoherent model is dominated. With one world, take M_L = {u, x, a₁, a₂, …} and C = {u, a₁, a₂, …}, with u ⪯ x and a_{n+1} ⪯ a_n, closed under reflexivity and transitivity. Then U_L = C_L = {u}, and x is dominated by u, but no member of C_L weakly dominates any a_n.

---

## Part 2. The main finite-world theorem (manuscript §4)

### 2.1 The KKM lemma [v3.3 3.3]

**Lemma 4.1.** Let F be finite and nonempty, and let (A_ω)_{ω∈F} be closed subsets of Δ_F such that every p ∈ Δ_F lies in A_ω for some ω ∈ supp p. Then ⋂_{ω∈F} A_ω ≠ ∅.

*Proof* (Knaster–Kuratowski–Mazurkiewicz 1929, via Brouwer).
1. Each A_ω contains δ_ω, since supp δ_ω = {ω}.
2. Let d_ω(p) ≔ dist(p, A_ω) and s(p) ≔ Σ_ω d_ω(p). The map G(p)_ω ≔ (p_ω + d_ω(p))/(1 + s(p)) is a continuous self-map of Δ_F.
3. Brouwer's theorem gives a fixed point p. At a fixed point, p_ω s(p) = d_ω(p) for every ω.
4. Choose ω ∈ supp p with p ∈ A_ω. Then p_ω s(p) = 0 with p_ω > 0, so s(p) = 0. Hence p lies in every A_ω. ∎

**Figure 1** [v3.3 Fig. 1; keep]. The lemma for |F| = 2 and |F| = 3.

### 2.2 Statements

The paper leads with the checkable form for loss rankings. The general form follows it.

**Theorem 4.2** [assembled: v3.3 3.5 + A.2; for finite Ω, (S) with Bayes choices]. Let Ω be finite and let the ranking be generated by a loss L: M_L × Ω → [0,∞]. Suppose that to each prior p on Ω is assigned an undominated coherent model c_p such that:
- (i) **Bayes choice:** c_p is a Bayes model for some prior whose support lies within supp p; and
- (ii) **lower semicontinuity:** for each world ω, the loss L(c_p, ω) is a lower semicontinuous function of p on Δ.

Then every model is weakly dominated by one of the assigned models c_p. If, in addition, every model with the same loss profile as an undominated coherent model is coherent, then:
- the undominated models are exactly the undominated coherent ones; and
- every other model is dominated by an undominated coherent model.

*Notes for the text.*
- The prior in (i) may differ from p, and it need not vary continuously. §8.3 needs this freedom.
- The assignment p ↦ c_p need not be continuous. Only its losses must be lower semicontinuous.
- The Bayes property is required only of the assigned models. It is not required of every Bayes model.

**Theorem 4.3** [v3.3 3.4, restated without certificates]. Let Ω be finite and let L be any ranking. Suppose that to each prior p on Ω is assigned an undominated coherent model c_p, **the same model whichever rival it is compared with**. Suppose also that to each model m and world ω is assigned a **closed** set A_ω(m) of priors such that:
- (i) **guarantee:** at every prior in A_ω(m), the assigned model is at least as good as m at ω; and
- (ii) **support-wise coverage:** for every model m, every prior p lies in A_ω(m) for some world ω that p charges.

Then:
- (a) for each model m, some prior lies in every A_ω(m), and the model assigned to any such prior weakly dominates m;
- (b) every undominated model is tied at every world with an undominated coherent model;
- (c) if closure under ties holds, the undominated models are exactly the undominated coherent ones, and every other evaluable model is dominated by one of them.

*Plain gloss for the text.* A_ω(m) is the set of priors at which the comparison with m at ω is *guaranteed*.
- The assigned model may make further comparisons that are not guaranteed.
- It may jump as p varies.
- Only the guaranteed comparisons must vary in a closed way.
- One assigned model must serve against every rival at once.

*Equivalence with v3.3's (B)* (for the cut list; not in the paper). Given (B), let c_p be a realiser and A_ω(m) ≔ {p : m ∈ B_ω(p)}; (B1) gives closedness, (B3) the guarantee and (B2) coverage. Conversely, put B_ω(p) ≔ {m : p ∈ A_ω(m)}, with realiser c_p. So Theorem 4.3 *is* v3.3 Theorem 3.4.

### 2.3 Proofs

*Proof of Theorem 4.3.*
- (a) Fix m. The sets A_ω(m), ω ∈ Ω, are closed, and by (ii) they satisfy the hypothesis of Lemma 4.1. So some p* lies in all of them. By (i), c_{p*} ⪯_ω m at every ω.
- (b) and (c): Proposition 3.1(a).

No property of the relations is used: no reflexivity, transitivity or completeness. Nor is any topology on models, any parametrisation of C_L, or any numerical value. ∎

**Corollary 4.4** [v3.3 3.5 with 2.1; "closed competitive choice"]. Let Ω be finite. Suppose that to each prior p is assigned an undominated coherent model c_p, competitive on supp p, such that each set {p : c_p ⪯_ω m} is closed. Then the conclusions of Theorem 4.3 hold.

*Proof.* Take A_ω(m) ≔ {p : c_p ⪯_ω m}. The guarantee holds by definition, and coverage is competitiveness. ∎

*Proof of Theorem 4.2.*
- By Lemma 2.3 and (i), c_p is competitive on supp p.
- The set {p : L(c_p, ω) ≤ L(m, ω)} is closed: it is a sublevel set of a lower semicontinuous function, or all of Δ if L(m,ω) = ∞.
- Apply Corollary 4.4.
- For a loss ranking, "same profile as an undominated coherent model" is the same as "tied at every world". A model with that profile is automatically undominated. So the extra hypothesis is closure under ties. ∎

### 2.4 Figures and examples kept in §4

**Figure 2** [v3.3 Fig. 2; keep both panels; rewrite the caption without (S)].
- (a) Two worlds, a loss ranking. The assigned profiles run from one axis to the other and avoid the quadrant of profiles strictly worse than L(m). So they must meet the quadrant of profiles that weakly dominate L(m).
- (b) Example 4 of Schervish, Seidenfeld and Kadane (2009), with assigned model p. The assigned profiles jump at (½,½) and skip the dominating quadrant. **No coherent model weakly dominates m**, which is what shows that closedness cannot be dropped. Lower semicontinuity would force the profile at (½,½) into that quadrant, and the closed sets of Theorem 4.3 fail to be closed.

**Example 4.5** [v3.3 2.3; keep, 3 lines]. Coverage cannot be weakened to "not strictly dominated on supp p" when rankings have incomparabilities. Take one world, M_L = {a, b} with a and b incomparable, and C = {a}. Then C_L = {a}, and no model strictly dominates a. But b is undominated and is weakly dominated by no coherent model.

**Example 4.6** [v3.3 A.7 and the paragraph after it; condensed]. Theorem 4.3 is strictly more general than Theorem 4.2, even for loss rankings, because of rescaling (Lemma 2.2).
- *Setting.* Two worlds, M_L = [0,1]², C = {c₁ + c₂ = 1}, with quadratic losses L₁(c) = (1−c₁)² + c₂² and L₂(c) = c₁² + (1−c₂)², rescaled by t ↦ t^{1/4} at both worlds.
- *Corollary 4.4 applies.* The identity assignment p ↦ (p₁, p₂) satisfies it. It does so for the quadratic loss, where p is Bayes for p and the losses are continuous, and Lemma 2.2 transfers this. So every incoherent model is dominated, indeed strictly.
- *Theorem 4.2 does not apply.*
  - Coherent profiles become a(√(1−s), √s), with a = 2^{1/4}.
  - For a prior charging both worlds, the expected loss along the coherent arc is strictly concave, so the only Bayes models are the endpoints (1,0) and (0,1). Incoherent models are never Bayes models, since each is strictly worse at both worlds than its coherent counterpart.
  - An assignment satisfying (i) must therefore take only endpoint values, with (1,0) at δ₁ and (0,1) at δ₂.
  - By (ii), the sets {p : c_p = (1,0)} = {p : L(c_p,1) ≤ 0} and {p : c_p = (0,1)} are closed. They are disjoint and nonempty, and they cover Δ, which contradicts connectedness.
- *Randomisation* [v3.3 A.8, condensed to 3–4 lines; REF67_ldgo §8 rec. C]. This answers the question "why not apply the randomised complete-class theorem?"
  - Allowing random choice among finitely many models gives the convex hull of the profiles.
  - Every interior coherent profile (0 < s < 1) is strictly dominated by a mixture of the two endpoint profiles. So the undominated randomised profiles are the segment from (a,0) to (0,a), and the original and randomised undominated sets share only the endpoints.
  - No original profile lies weakly below (a/2, a/2), so a randomised dominator need not be matched by any original model.
  - Proof (5 lines, copied from v3.3 A.8):
    - coherent profiles lie on x² + y² = a², with x + y ≥ a, and equality only at the endpoints;
    - subtract (x+y−a)/2 from both coordinates to reach the segment;
    - every profile lies on or above x + y = a;
    - (a/2, a/2) would need √(1−s) ≤ ½ and √s ≤ ½, which is impossible.
  - So the randomised complete-class theorem (Schervish, Seidenfeld, Stern and Kadane 2020) concerns a different decision class, and does not by itself identify the undominated original models.

**Example 4.7** [the AUDIT example in its two-world form; CC67 §2b; refereed REF67_cc §2; keep, about half a page]. Theorem 4.3 is strictly more general than Corollary 4.4.
- *Setting.*
  - Two worlds. Coherent models c_t and incoherent models x_t, for t ∈ [0,1].
  - Start from the scores c_t ↦ (t, 1−t) and x_t ↦ (2, 2), with lower better.
  - Keep every score comparison except c_q ⪯₁ x_q for q > 0, and c₀ ⪯₂ x₀.
  - The relations are reflexive and acyclic, but **not transitive**.
- *Dominance facts.* C_L = {c_t}. Each x_q is dominated by every c_s with s ≠ q. Closure under ties holds.
- *Theorem 4.3 applies.*
  - Assign c_{p₂} to p.
  - Guarantee c_s at world 1 when p₂ ≤ s, and at world 2 when p₂ ≥ s.
  - Guarantee x_q (q > 0) at world 1 when p₂ = 0, and at world 2 always.
  - Guarantee x₀ at world 1 always, and at world 2 when p₂ = 1.
  - All these sets are closed, and coverage holds.
- *Corollary 4.4 fails for every assignment.* Proof for the paper [direct argument; refereed REF67_ldgo §7b, PROVED and CHECKED]:
  - Suppose p ↦ c_p satisfies Corollary 4.4.
  - For q > 0, the full comparison set {p : c_p ⪯₁ x_q} is Δ ∖ {p : c_p = c_q}, because only c_q fails against x_q at world 1. Likewise {p : c_p ⪯₂ x₀} = Δ ∖ {p : c_p = c₀}.
  - Both sets are closed, so every set {p : c_p = c_t} is open.
  - These sets partition the connected simplex Δ, so the assignment is constant.
  - But competitiveness at δ₁ forces c₀, the only model at least as good as every model at world 1, and at δ₂ it forces c₁.
- *Remark for the text* [qualifier per REF67_ldgo §4]. Duplicate each world into infinitely many copies of its type. Theorem 5.2 then applies, but **no compact family whose full comparison sets are closed meets the hypotheses of Theorem 5.2**.
  - Proof [CC67; refereed REF67_cc §2]: such a family must contain a weak dominator of each c_t, which is c_t itself, so it maps onto {c_t}. Its full comparison sets against x_q make every fibre {θ : c_θ = c_t} open, giving infinitely many disjoint nonempty open sets covering a compact space.
  - Without the qualifier the claim is false: a one-point family trivially has closed full comparison sets.

**Proposition 4.8** [v3.3 B.5–B.6; optional, about 0.6 page; the author's choice per REF67_ldgo §8 rec. E]. Let Ω be finite, let the ranking be generated by a finite loss, and let the set K of loss profiles of undominated coherent models be compact. Then the hypotheses of Theorem 4.3 hold iff every model is weakly dominated by an undominated coherent model.

*Proof* (the ray construction, copied from v3.3).
- Let K↑ ≔ {y : y ≥ k for some k ∈ K}. It is closed, by compactness of K.
- Fix β above every coordinate of every point of K. For p ∈ Δ, let t(p) be the largest t ≥ 0 with β𝟙 − tp ∈ K↑, and put Q(p) ≔ β𝟙 − t(p)p.
- t is well defined, positive and continuous: upper semicontinuity by closedness of K↑, and lower semicontinuity because β𝟙 − (t(p) − ε)p lies strictly above some k at every world.
- Assign to p an undominated coherent model whose profile lies below Q(p). Let A_ω(m) ≔ {p : Q(p)(ω) ≤ L(m,ω)}, which is closed by continuity; the guarantee then holds.
- Coverage: if L(m,ω) < Q(p)(ω) on supp p, let y ≔ L(m) on supp p and β elsewhere. Then y ∈ K↑ by hypothesis, and y ≤ β𝟙 − (t(p)+δ)p for small δ, which contradicts the maximality of t(p).
- The converse is Theorem 4.3. ∎

*Remark, if kept.* The guarantees here are built from the conclusion. The content of Theorem 4.3 is that *any* guarantees will do, and in practice they come from Bayes choices. Compactness of K cannot be dropped: Remark 5.5's witness has non-compact K.

---

## Part 3. The infinite-world theorem (manuscript §5)

### 3.1 Statements

**Theorem 5.1** [assembled: v3.3 3.7 + 2.4 + A.2; the proof is the refereed v3.3 argument]. Let Ω be any nonempty set and let the ranking be generated by a loss L: M_L × Ω → [0,∞]. Suppose there are a compact space Θ and, for each θ ∈ Θ, an undominated coherent model c_θ, such that:
- (i) **lower semicontinuity:** for each world ω, θ ↦ L(c_θ, ω) is lower semicontinuous on Θ; and
- (ii) **continuous Bayes choices on finite sets of worlds:** every finite set of worlds is contained in a nonempty finite set F of worlds (call such sets *linked*) for which there is a continuous map σ_F from priors on F into Θ, such that each c_{σ_F(p)} is a Bayes model for some prior whose support lies within supp p.

Then every model is weakly dominated by some c_θ. With closure under ties, the conclusions of Theorem 4.2 follow. For finite Ω this is Theorem 4.2, with Θ ≔ Δ, F ≔ Ω and σ the identity.

**Theorem 5.2** [CC67 §3.1; refereed REF67_cc §3]. Let Ω be any nonempty set and L any ranking. Suppose:
1. **A compact family of undominated coherent models with closed guaranteed comparisons.** There are a compact space Θ and, for each θ ∈ Θ, an undominated coherent model c_θ. For each world ω and model m there is a closed set K_ω(m) ⊆ Θ such that c_θ is at least as good as m at ω for every θ ∈ K_ω(m). (Not every comparison that c_θ makes need be guaranteed.)
2. **Local guarantees on finite sets of worlds.** Every finite set of worlds is contained in a nonempty finite set F of worlds (call such sets *linked*) for which there are the following:
   - a map θ_F from priors on F into Θ, which need not be continuous and is **the same for every rival**;
   - for each ω ∈ F and model m, a closed set A^F_ω(m) of priors on F.

   These satisfy:
   - (a) the local guarantees are global guarantees: θ_F(p) ∈ K_ω(m) whenever p ∈ A^F_ω(m);
   - (b) support-wise coverage: for every model m, every prior p on F lies in A^F_ω(m) for some world ω that p charges.

Then every model is weakly dominated by some c_θ, and conclusions (b) and (c) of Theorem 4.3 hold.

*Plain-English version for the text* (CC67 §3.1, lightly edited). On each finite set of worlds, every prior is assigned one member of a fixed compact family of undominated coherent models, and this one member must serve against every rival. For each rival and world, the priors at which the comparison is guaranteed form a closed set, and every rival is guaranteed at some world that the prior charges. In the compact family, the members guaranteed to match or beat a given rival at a given world also form a closed set. Then a single member of the family matches or beats the rival at every world.

**Continuous special case** [CC67; refereed]. If each θ_F is continuous, (a) and (b) may be replaced by one requirement: for every model m and every prior p on F, some world ω charged by p has θ_F(p) ∈ K_ω(m). Then take A^F_ω(m) ≔ θ_F⁻¹(K_ω(m)), which is closed.

### 3.2 Proofs (the compactness step)

*Proof of Theorem 5.2.* Fix a model m.
1. **KKM on each finite set.** For each linked F, the sets A^F_ω(m), ω ∈ F, are closed, and by (b) they satisfy the hypothesis of Lemma 4.1. So some p_F lies in all of them, and by (a), θ_F(p_F) ∈ ⋂_{ω∈F} K_ω(m).
2. **Finite intersection property.** Given finitely many worlds ω₁, …, ω_k, choose a linked F containing them. Then ⋂_i K_{ω_i}(m) ⊇ ⋂_{ω∈F} K_ω(m) ∋ θ_F(p_F). So the closed sets K_ω(m), ω ∈ Ω, have the finite intersection property.
3. **Compactness.** Since Θ is compact, some θ* lies in every K_ω(m). Then c_{θ*} ⪯_ω m at every world.
4. Conclusions (b) and (c) follow from Proposition 3.1(a).

No property of the relations is used. ∎

*Proof of Theorem 5.1* (direct; this is v3.3's refereed proof of 3.6/3.7). Fix m.
1. The sets T_F ≔ {θ : L(c_θ, ω) ≤ L(m, ω) for all ω ∈ F} are closed by (i).
2. On Δ_F the sets A_ω ≔ σ_F⁻¹{θ : L(c_θ,ω) ≤ L(m,ω)} are closed, by (i) and the continuity of σ_F.
3. By (ii), Lemma 2.3 and completeness, every p lies in some A_ω with ω ∈ supp p.
4. Lemma 4.1 gives p_F with σ_F(p_F) ∈ T_F, so T_F ≠ ∅.
5. Finite intersections of the T_F contain a T_G, so compactness gives θ* in every T_F. Every world lies in some F. ∎

*Theorem 5.1 as a case of Theorem 5.2* (for the text). Take K_ω(m) ≔ {θ : L(c_θ,ω) ≤ L(m,ω)}, θ_F ≔ σ_F, and apply the continuous special case.

*Theorem 4.3 as the finite case of Theorem 5.2* [CC67 §3.2; refereed].
- If Ω is finite, then Ω itself must be one of the linked sets F. Put c_p ≔ c_{θ_Ω(p)} and A_ω(m) ≔ A^Ω_ω(m).
- Conversely, given the data of Theorem 4.3, take Θ ≔ Δ, K_ω(m) ≔ A_ω(m) and θ_Ω the identity.

So for finitely many worlds nothing is lost.

### 3.3 Why this form: remarks and examples kept in §5

**Remark 5.3** [v3.3 §4.3, second point; extended by CC67 §3.3; refereed]. **The assigned model must not depend on the rival.** Suppose each rival m could have its own assignment p ↦ c^m_p. Then the hypotheses would follow from the conclusion:
- take the compact family Θ ≔ C_L with the cofinite topology, and c_θ ≔ θ (as in Remark 5.4);
- choose a weak dominator d(m) ∈ C_L of m;
- take c^m_p ≔ d(m), A_ω(m) ≔ Δ_F, and K_ω(m) ≔ {d(m)}, which is closed in that topology. The content of Theorems 4.3 and 5.2 lies in **one assigned model per prior, serving all rivals**.

**Remark 5.4** [CC67 §1; refereed REF67_cc §1]. **An abstract compactness condition would be equivalent to the conclusion.** Consider asking only for a compact family with closed guaranteed comparisons (item 1 of Theorem 5.2) such that, for each model m and each finite set of worlds, some single θ is guaranteed against m at every world of that set. Steps 2–3 of the proof then give the conclusion. But the conclusion also gives back such a family:
- give C_L the cofinite topology, which is compact (any open cover has a member with finite complement);
- let c_θ ≔ θ;
- choose, using the axiom of choice, a weak dominator d(m) ∈ C_L for each m;
- put K_ω(m) ≔ {d(m)}, which is finite and hence closed.

Requiring Θ to be Hausdorff (use the one-point compactification of the discrete space C_L) or metrizable (which adds only a cardinality bound) does not change this. Such a condition therefore does not explain why dominance holds. The local guarantees of item 2 are what give Theorem 5.2 content.

**Remark 5.5** [REF67_cc §3, necessary consequence; refereed in substance via CC67 §3.3]. **The hypotheses are not implied by the conclusion.** At the vertex δ_ω, coverage forces δ_ω ∈ A^F_ω(m) for every m. So the hypotheses of Theorems 4.3 and 5.2 imply that at every world some undominated coherent model is at least as good as every model. Hence they fail for the following loss ranking, in which the conclusion holds trivially.
- Two worlds, M_L = C, with loss profiles (t, 1−t) for t ∈ (0,1].
- These profiles are pairwise incomparable, so every model is undominated and weakly dominates itself.
- No model has loss 0 at world 1.

v3.3's Example B.7, which has ideal models at both worlds and still fails the hypotheses, is **omitted**. The vertex witness above makes the point, and the paper cannot point to v3.3.

*The finite-world condition used in Example 5.6 and in this section* [REF67_cc §3b, definitional point]. "Guarantees on a finite set G of worlds" means the data of Theorem 4.3 for the worlds of G: priors on G, closed sets A_ω(m) for ω ∈ G, guarantee and support-wise coverage. **The assigned models are taken from the undominated coherent models of the ranking on all of Ω**, not from those of the ranking restricted to G. A model can be undominated on G without being undominated on Ω, and the converse also fails, so the paper must say this explicitly. With this definition, Theorem 5.2's hypotheses imply guarantees on every finite set of worlds: choose a linked F ⊇ G, restrict to the face Δ_G, and assign c_{θ_F(p)} [CC67 §3.2; refereed REF67_cc §3b].

**Example 5.6** [the loss-ranking example; new in round 67; refereed REF67_ldgo §7a, PROVED and CHECKED; the main example per the lead]. **Guarantees on finite sets of worlds do not suffice without a compact family linking them.** This is about five lines in the paper.
- *Setting.* Ω = ℕ. Coherent models e_n (n ≥ 1) and one incoherent model x, with losses:
  - L(e_n, ω) ≔ 0 for ω ≤ n, and 2 + n for ω > n;
  - L(x, ·) ≡ 1.

  This is a loss ranking, hence a complete preorder ranking, so no caveat about order properties is needed. (The bounded loss 3 − 1/n beyond n also works.)
- *Dominance facts.*
  - For m > n, e_m is better than e_n on (n, m] and worse beyond m. So the e_n are pairwise incomparable.
  - x is worse than every e_n at world 1. So every e_n is undominated, and C_L = {e_n : n ≥ 1}.
  - No e_n weakly dominates x, since 2 + n > 1 beyond n. So x is undominated and incoherent, and the conclusion fails.
  - Closure under ties holds trivially.
- *Guarantees on every finite set hold*, with assigned models from C_L as defined on all of Ω. On a finite F, e_{max F} has loss 0 throughout F, so it is at least as good as every model at every world of F. So the constant assignment p ↦ e_{max F}, with every A_ω(m) ≔ Δ_F, satisfies the guarantee and coverage.
- *It also shows that Theorem 5.1 needs its compact family.* On every finite F there is a constant, hence continuous, Bayes choice, and its losses are lower semicontinuous. Yet the conclusion fails, because the e_{max F} have no limit among the models.

*Optional relational variant* [CC67 §3.6; refereed REF67_cc §3]. Use it only if a non-numerical witness is wanted.
- Coherent e_n and h are all tied with one another, and x is related only to itself.
- e_n ⪯_ω x iff ω ≤ n, and h ⪯_ω x iff ω ≥ 2.
- Its relations are reflexive and acyclic, but not transitive.

**Remark 5.7** [the content of REF67_cc's Proposition R1, rewritten in the paper's own terms as REF67_ldgo §3 suggests; refereed REF67_cc §4.1 and REF67_ldgo §3]. **When every comparison of the family is closed.**

*Text for the paper:*
> Suppose that every comparison the compact family makes has closed sections: {θ : c_θ ⪯_ω m} is closed for every world ω and model m. For loss rankings this holds when the losses along the family are lower semicontinuous. Then item 1 of Theorem 5.2 holds with K_ω(m) taken to be these sets, and item 2(a) says only that the model assigned to p is at least as good as m at ω whenever p ∈ A^F_ω(m). This is the form in which every application in §8 meets the hypotheses, which is why none of them needs more than Theorem 5.1. The requirement is not necessary: in Example 4.7, and in its version with each world copied infinitely often, Theorem 5.2 applies, but no compact family whose full comparison sets are closed meets its hypotheses.

*Sentence before §6, in its correct form.* The results of §6 need lower semicontinuous losses along the family. That is stronger than closed comparison sections, and it is what supplies comparisons with arbitrary numerical bounds, the x of Theorem 6.1. This replaces CC67's §4 headline, which REF67_cc found wrong.

*Closing paragraph of §5.3* (replaces v3.3 line 157; REF67_cc §6 reworded, with REF67_ldgo's qualifier):
> For infinitely many worlds, the models that meet the local guarantees must come from one compact family of undominated coherent models, in which the guaranteed comparisons form closed sets (Theorem 5.2). Asking this of every comparison the family makes is one way to secure it (Remark 5.7), and lower semicontinuous losses do so. It is not necessary: Example 4.7, with each of its two worlds copied infinitely often, satisfies the hypotheses of Theorem 5.2, but no compact family whose full comparison sets are closed meets those hypotheses; with two worlds the same failure already occurs. Guarantees on finite sets of worlds do not suffice without a compact family linking them: in Example 5.6 there are such guarantees on every finite set of worlds, yet some model is weakly dominated by no coherent model. For finitely many worlds, Theorem 4.3 needs no compact family.

**Dropped from §5** (preserve in CC67/REF67_cc):
- CC67 §3.5 (the w_k, z example): the compact link has content beyond the conclusion together with finite guarantees.
- The ultrafilter characterisation (CC67 §3.6).
- The hierarchy and its strictness.

### 3.4 What Bayes choices add: margins, Bayes models, strict dominance (manuscript §6)

These results use the numerical values of the losses. They need lower semicontinuity and Bayes choices, which are exactly the hypotheses of Theorem 5.1. REF67_cc §4 confirms that none needs more, and none follows from Theorem 5.2 alone.

**Theorem 6.1** [v3.3 A.4; proof self-contained]. Assume the hypotheses of Theorem 5.1. For x: Ω → (−∞, ∞], the following are equivalent:
- (a) some model has L(·,ω) ≤ x(ω) at every world;
- (b) some c_θ does;
- (c) π·x ≥ V(π) for every finitely supported prior π.

*Proof.*
- (b) ⇒ (a) is trivial.
- (a) ⇒ (c): V(π) ≤ π·L(c) ≤ π·x.
- (c) ⇒ (b):
  1. Fix F, and let A_ω ≔ {p : L(c_{σ_F(p)}, ω) ≤ x(ω)}. These sets are closed.
  2. Coverage. Suppose some p lies in no A_ω with ω ∈ supp p. Let c ≔ c_{σ_F(p)}, Bayes for π with supp π ⊆ supp p. Then x < L(c) on supp π, so x is finite there and π·x < π·L(c) = V(π), contradicting (c). (If π·L(c) = ∞, the inequality is immediate.)
  3. Lemma 4.1 gives a θ in T_F ≔ {θ : L(c_θ,·) ≤ x on F}, which is closed by lower semicontinuity.
  4. The closed sets T_F have the finite intersection property, because every finite union of linked sets lies in a linked G and T_G is contained in each T_F. Compactness of Θ gives a θ in every T_F. ∎

  *Textual dependency, redirected* [REF67_cc §4.2]. v3.3's proof of A.4 cited "the compactness argument in the proof of Theorem 3.6". The proof above writes that step out (steps 2–3 of the proof of Theorem 5.2, with T_F in place of K). So Theorem 6.1 does not depend on the deleted Theorem 3.6, and it does not use Theorem 5.2's hypotheses.

*Consequences.* With x ≔ L(m) − ε (where ∞ − ε = ∞): a model with finite losses is uniformly dominated, by some model or equivalently by some c_θ, iff for some ε > 0 its expected loss is at least V(π) + ε for every finitely supported π. Theorem 5.1's weak dominance is the case x = L(m).

**Corollary 6.2** [v3.3 A.3]. Under the hypotheses of Theorem 5.1, every finitely supported prior π has a Bayes model among the c_θ.

*Proof.* θ ↦ π·L(c_θ) is lower semicontinuous on a compact space, so it has a minimiser θ*. Every model m is weakly dominated by some c_θ, so π·L(c_{θ*}) ≤ π·L(m). ∎

The paper says nothing about the necessity of lower semicontinuity here. v3.3's Example B.4 is omitted, since the paper cannot point to v3.3.

**Proposition 6.3** [v3.3 A.5 and A.9, merged]. Let Ω be finite and assume the hypotheses of Theorem 4.2. These are the hypotheses of Theorem 5.1 with Θ ≔ Δ, F ≔ Ω and σ the identity, so Theorem 6.1 applies. Suppose V is upper semicontinuous on Δ. This holds if:
- (a) the assigned models have finite losses; or
- (b) V is finite, each c_p is a Bayes model for p itself, and each p ↦ L(c_p, ω) is continuous.

Then a model is strictly dominated iff it is a Bayes model for no prior, and in that case some assigned model uniformly dominates it. In particular, if every Bayes model is an undominated coherent model, every other model is uniformly dominated by an undominated coherent model.

*Proof.*
- **⇒.** A strict dominator has finite losses and smaller expected loss under every prior.
- **⇐.** Let m be a Bayes model for no prior.
  1. V is finite: if V(π) = ∞, every model would be Bayes for π.
  2. Let Ω_∞ ≔ {L(m,·) = ∞}. Put x_n ≔ L(m) − 1/n off Ω_∞, and x_n ≔ n on Ω_∞.
  3. The functions g_n(π) ≔ π·x_n − V(π) are lower semicontinuous and increase in n. They tend to π·L(m) − V(π) > 0 when π(Ω_∞) = 0, and to ∞ otherwise.
  4. By compactness, some g_N > 0 on all of Δ. Theorem 6.1 then gives an assigned model c_p ≤ x_N, which uniformly dominates m.
- **Upper semicontinuity.**
  - In case (a), V(π) = inf_p π·L(c_p), because every model is weakly dominated by an assigned model (Theorem 4.2). This is an infimum of continuous functions.
  - Case (b) (copied from v3.3 A.9; refereed REF67_ldgo §6). Fix p and ε > 0.
    1. For an interior prior q, V(q) is finite, so the Bayes model c_q has finite losses. Hence π ↦ π·L(c_q) is continuous.
    2. As interior q → p, p·L(c_q) → p·L(c_p) = V(p). This uses continuity of the losses, which are finite on supp p.
    3. Choose q with p·L(c_q) < V(p) + ε/2. Then π·L(c_q) < V(p) + ε for π near p, so V(π) < V(p) + ε there. ∎

*Textual dependency, redirected* [REF67_cc §4.2]. v3.3's proof of A.5 cited Corollary 3.7, the infinite theorem. Since Ω is finite here, the citation is now Theorem 4.2. Nothing else changes.

**Example 6.4** [v3.3 A.12, which is SSK09 Example 2; condensed to about 8 lines]. Neither sufficient condition for upper semicontinuity can simply be dropped.
- *Setting.* Ω = {1,2} and M_L = [0,1]², with L(f,1) = (1−f₁)² + g₀(f₂) and L(f,2) = f₁² + g₁(f₂), where:
  - g₀(0) = 0 and g₀(y) = 1 + y for y > 0;
  - g₁(y) = y − log y and g₁(0) = ∞.
- The hypotheses of Theorem 4.2 hold with c_p ≔ p, which is the unique Bayes model for p, and closure under ties holds.
- But m = (½, 0) is a Bayes model for no prior, and no model strictly dominates it.
- Here the coherent model (1,0) has infinite loss at world 2, and V jumps at δ₁.

*Verification paragraph* (in the paper; about 8 lines; CHECKED REF67_ldgo `misc.py`).
- The p-expected loss is p₁(1−f₁)² + p₂f₁² + p₁g₀(f₂) + p₂g₁(f₂). The first part has the unique minimiser f₁ = p₁.
- If p₂ = 0, the second part is g₀(f₂), with unique minimiser 0.
- If p₂ > 0, it is ∞ at f₂ = 0 and has derivative 1 − p₂/f₂ for f₂ > 0, so its unique minimiser is p₂.
- So c_p is the unique Bayes model for p, with V(p) = p₁p₂ + 1 − p₂ log p₂ for p₂ > 0, and V(δ₁) = 0. Since V is finite, a weak dominator of c_p is Bayes for p and so equals it. This gives C_L = C and closure under ties.
- The losses along c_p are lower semicontinuous, because g₀ jumps up only away from 0.
- L(m) = (¼, ∞). So p·L(m) > V(p) for every p, and m is a Bayes model for no prior.
- (1,0), with profile (0, ∞), dominates m. But L(f,1) < ¼ forces f₂ = 0, and then L(f,2) = ∞. So no model strictly dominates m.
- V(p) → 1 as p → δ₁ with p₂ > 0, while V(δ₁) = 0.

---

## Part 4. The admissibility route: decision

**Decision: cut it from LDG** (v3.3 Lemma 3.11, Prop. 3.12 and the Lyapunov paragraph). LDG keeps one sentence in §9 (scope):

> For rankings that are lexicographic in finitely many numerical scores with a compact range of score vectors, Zorn's lemma gives every model an undominated weak dominator directly; it then remains to show, for the ranking at hand, that every undominated model is coherent. This method is used for the structured construction in [application paper].

**Justification.**
1. **No LDG result or application uses it.** Every application in §8 runs through Theorem 4.2 or 5.1 (grep-verified, REF67_ldgo §5).
2. **Its only consumer is the application paper.** The veto–Brier construction (OUT67 Part 8) is a two-level lexicographic integral ranking.
   - **Cross-paper requirement** (REF67_ldgo §5): OUT67 Part 8 is only a sketch, and it points to the covering-paper *draft* (Lemmas "lyap", "zorn", "sep", "unique"; Theorem `thm:route`).
   - If the definitive application paper keeps its structured example, it must itself carry the Zorn lemma, about 10 lines (the covering paper's `lem:zorn` is already specific to gambles), together with the separation step. Otherwise the example rests on an unpublished draft.
   - This is not a reason to keep the lemma in LDG. **The lead should confirm that OUT67's successor includes it.**
3. **It is not a general alternative to the main theorems.**
   - Lemma 3.11 gives only "every model is weakly dominated by an *undominated* model".
   - The decisive step, "undominated ⇒ coherent", is ranking-specific. The only general tool LDG offered for it (Prop. 3.12) needs finitely many worlds, exactly two levels and a convex score range.
   - In the integral setting, compactness and convexity of the range come from Lyapunov's theorem, which needs finite dimensions and a non-atomic measure. That belongs to the application.
   - Lemma 3.11 holds for any set of worlds. But the second step, as LDG offered it (Prop. 3.12 and Lyapunov), needs finitely many worlds. The author's standing preference is to avoid lexicographic devices unless their results extend to infinitely many worlds.
4. **Keeping it would bring back the "three routes" architecture** that decision 3 removes. The paper's message is one mechanism, KKM plus compactness, behind checkable sufficient conditions.

---

## Part 5. What the dominance conclusion gives (manuscript §7)

### 5.1 Rational permissibility [v3.3 §5]

**The dominance principle** (stated in words, once):
- A model is **irrational** if every ranking in the family that evaluates it has an undominated model that dominates it.
- It is **rationally permissible** if it is undominated under some ranking in the family.

The paragraph on interpretation should be kept and shortened: tasks, multi-dimensional performance, why the whole family matters. The (P1)–(P4) list becomes one sentence: *given evaluability and coherent admissibility, and given that every ranking satisfies the dominance conclusion and closure under ties, the permissible models are exactly the coherent ones, and every incoherent model is irrational.*

**Proposition 7.1** [v3.3 5.1]. Suppose every ranking in the family satisfies the dominance conclusion. Then for each ranking L:
- (a) every undominated model is tied at every world with an undominated coherent model;
- (b) if L satisfies closure under ties, its undominated models are exactly its undominated coherent models, and every other evaluable model is dominated by one of them;
- (c) if L is a preorder ranking, its undominated models are exactly those tied at every world with an undominated coherent model, and every other evaluable model is dominated by an undominated coherent model.

If every ranking satisfies closure under ties or is a preorder ranking, then a model is undominated under no ranking iff, under every ranking that evaluates it, some undominated model dominates it. With coherent admissibility, every coherent model is permissible. If every ranking also satisfies closure under ties, the permissible models are exactly the coherent ones.

*Proof.* As in v3.3 5.1: (a) and (b) from Proposition 3.1(a); (c) from Proposition 7.2; the rest by unwinding the definitions. ∎

### 5.2 The role of closure under ties

- Closure under ties is what turns weak dominance into dominance (Proposition 3.1(a)).
- It fails for some natural rankings. Two examples, one sentence each:
  - merely proper scores (§8.1, last paragraph);
  - SSK09 Example 1. After rescaling by t ↦ e^t at each world, its total scores give a loss ranking with the same dominance relation. Corollary 4.4 applies to it with c_p ≔ (p(A₁), p(A₂)), and Lemma 2.2 transfers the conclusion, since both depend only on the ranking. The incoherent forecast (1,0) is tied with the coherent (0,0) at every world, so this is a failure of closure under ties, not of the dominance theorem. Theorem 4.2 cannot be used here: the Bayes property does not survive the nonlinear rescaling, and the original scores take the values ±∞ (REF67_ldgo §8).
- Without it, but with transitivity, the conclusions hold for loss profiles instead of models (Proposition 7.1(c)).

**Remark 7.5** [v3.3 5.2, folded into a remark with its 5-line proof]. Let ∼ be an equivalence on models, such as equal loss profiles or equality up to null sets, and write [X] for the set of models equivalent to a member of X. Suppose:
- every ranking in the family is a preorder ranking satisfying the dominance conclusion;
- for each ranking L, the models tied at every world with an undominated coherent model of L are exactly the evaluable models in [C_L].

Then the union of the undominated sets U_L equals the union of the sets M_L ∩ [C_L], and is contained in [C]. Equality with [C] holds if [C] ⊆ ⋃_L (M_L ∩ [C_L]). This follows from coherent admissibility when every M_L, or C itself, is closed under ∼.

*Proof.*
- By Proposition 7.1(c) and the second hypothesis, U_L = M_L ∩ [C_L] ⊆ [C].
- Suppose every M_L is closed under ∼, and m ∼ c ∈ C. Coherent admissibility gives L with c ∈ C_L, so m ∈ M_L ∩ [C_L].
- If C is closed under ∼, then [C] = C = ⋃_L C_L ⊆ ⋃_L (M_L ∩ [C_L]).
- When ∼ is equality, the second hypothesis is closure under ties. ∎

### 5.3 The role of transitivity

**Proposition 3.1, Theorems 4.3 and 5.2, and Corollary 4.4 use no transitivity, reflexivity or completeness.**
- This matters because the rankings constructed in the application paper are not transitive (its full-domain example; OUT67 Example 5.9).
- The results for loss rankings (Theorems 4.2 and 5.1, and all of §6) do use completeness through Lemma 2.3, and §6 uses numerical values. Loss rankings are complete preorders, so this costs nothing there.

Transitivity enters only in the following.

**Proposition 7.2** [v3.3 3.8]. Let L be a preorder ranking in which every model is weakly dominated by an undominated coherent model. Then U_L = {m : m is tied at every world with some c ∈ C_L}, and every model outside U_L is dominated by a member of C_L.

*Proof.* As in v3.3: transitivity shows that a model tied with an undominated coherent c is undominated, since a dominator of m would dominate c. ∎

**Example 7.3** [v3.3 3.9]. Without transitivity the reverse inclusion fails. Take one world, M_L = {c, m, m′} and C = {c}, with the pairs cc, mm, m′m′, cm, mc, cm′ and m′m. Then m is tied with c, but m′ dominates m, so U_L = {c}.

**Corollary 7.4** [v3.3 3.10; hypothesis restated as the dominance conclusion, which is all its proof uses (REF67_cc §4.2)]. Let the relations be transitive, and let every model be weakly dominated by an undominated coherent model. If some model strictly dominates m on S, then some undominated coherent model strictly dominates m on S.

*Proof.* Let c weakly dominate the strict dominator m′. At each ω ∈ S, c ⪯_ω m′ ≺_ω m. Transitivity gives c ⪯_ω m, and m ⪯_ω c would give m ⪯_ω m′. ∎

---

## Part 6. Applications (manuscript §8)

The applications share three steps:
1. Prove that every coherent model is undominated, so C_L = C. This is the work specific to each application.
2. Apply Theorem 4.2 or 5.1 through an explicit assignment of Bayes models.
3. Obtain uniform or strict dominance from Theorem 6.1 or Proposition 6.3.

This verifies the single-ranking conditions. Coherent admissibility for a family holds when the losses considered jointly cover the intended coherent class.

### 6.1 Proper scores on finite domains [v3.3 §6.1 and §A.7; condensed]

**Proposition 8.1.**
- *Hypotheses.*
  - Ω finite and C = Δ ⊆ M_L.
  - **Lower semicontinuity:** each p ↦ L(p, ω) is lower semicontinuous on Δ.
  - **Strict propriety relative to M_L:** for each p, p is a Bayes model for p, and every Bayes model for p has the profile L(p).
- *Conclusions.*
  - Every coherent model is undominated.
  - Every model is weakly dominated by a coherent one.
  - The undominated models are exactly those with a coherent loss profile.
  - If p is the *only* Bayes model for p, then the undominated models are exactly the coherent ones, and every incoherent model is dominated by a coherent one.
  - If moreover every probability has finite losses, or each p ↦ L(p, ω) is continuous, every incoherent model is uniformly dominated by a coherent one.

*Proof.*
- A weak dominator of p is a Bayes model for p, so it has profile L(p). Hence C_L = C.
- Theorem 4.2 applies with c_p ≔ p. Then use Proposition 7.2.
- With unique Bayes models, closure under ties holds, and no incoherent model is a Bayes model.
- For the uniform clause, suppose some model is incoherent (otherwise the clause is vacuous). Then V is finite: if V(p) = ∞, every model would be a Bayes model for p, including an incoherent one, contrary to uniqueness. Proposition 6.3, case (a) or (b), gives uniform dominance. ∎

*Recovered result.* Pettigrew's Theorem 1 is the case where uniqueness and continuity hold (one sentence).

*Event forecasts* (paragraph of about 10 lines; it applies **Theorem 4.2 and Proposition 6.3(b) directly on Δ_{τ(Ω)}, not Proposition 8.1**, whose hypotheses do not fit, since C ≠ Δ and p ↦ (p(E_i))_i is not injective; REF67_ldgo §6).
- *Setting* (Predd et al.). Events E₁, …, E_n; a continuous score s(·,·) into [0,∞]; L(f, ω) = Σ_i s(𝟙_{E_i}(ω), f_i); coherent forecasts c_p ≔ (p(E_i))_i, for priors p on the finite set τ(Ω) of truth-value patterns.
- The loss depends on ω only through τ(ω), so we may work on τ(Ω).
- Assign c_p to p ∈ Δ_{τ(Ω)}. The p-expected loss of f is Σ_i G_{p(E_i)}(f_i), where G_t(y) = t s(1,y) + (1−t) s(0,y).
- *Strictly proper s.*
  - Each G_t has a finite unique minimiser t, so c_p is the unique Bayes model for p, and V is finite.
  - A weak dominator of c_p is Bayes for p, so it equals c_p. This gives C_L = C and closure under ties.
  - Continuity of s makes the losses along c_p continuous.
  - So Theorem 4.2 and Proposition 6.3(b) give: every incoherent forecast is uniformly dominated by a coherent one. This is Predd et al., Theorem 1.
- *Merely proper continuous s_i,* with s_i(0,y) < ∞ for y < 1 and s_i(1,y) < ∞ for y > 0, normalised so that s_i(0,0) = s_i(1,1) = 0.
  - c_p is a Bayes model for p, and V is finite.
  - By SSK09 Lemma 5, any other Bayes model f has L(f) = L(c_p), so C_L = C, although closure under ties may fail.
  - Theorem 4.2 and Proposition 7.2 then show that the undominated forecasts are those with a coherent loss profile.
  - Proposition 6.3(b) shows that every forecast that is a Bayes model for no prior is uniformly dominated by a coherent one. This is SSK09 Theorem 2, Conclusion 3, for unconditional forecasts.

SSK09's continuity counterexample (their Example 4) is not lower semicontinuous on the probabilities (Figure 2(b)).

### 6.2 Probabilism on arbitrary domains [v3.3 Theorem 6.1; Nielsen-type]

*Setting.*
- Ω is arbitrary, and M_L = [0,1]^{2^Ω}, the credence functions on all subsets.
- C is the set of finitely additive probabilities. It is compact in the topology of pointwise convergence on subsets, which on C is the weak-star topology.
- E_q f ≔ sup{q(h) : h bounded, h ≤ f} for [0,∞]-valued f (Nielsen, Appendix A).

**Theorem 8.2.**
- *Hypotheses.*
  - **Quasi-strict propriety:** E_q L(q,·) ≤ E_q L(m,·) for every q ∈ C and m, strictly when m ∉ C.
  - **Lower semicontinuity:** for each world ω, q ↦ L(q, ω) is lower semicontinuous on C.
- *Conclusion.* The undominated models are exactly the finitely additive probabilities, and every other model is dominated by one.
- *Uniform dominance.* If in addition each probability has bounded loss across worlds, every other model is uniformly dominated by a probability.

*Proof.*
1. **C_L = C** [v3.3; the Nielsen adaptation].
   - Suppose L(m) ≤ L(q) with q ∈ C and L(m,w) < L(q,w). Then E_q L(m) = E_q L(q) < ∞, and L(m,w) is finite.
   - Put q_n ≔ (1/n)δ_w + (1 − 1/n)q. Linearity of E in the probability (Nielsen, Appendix A, Proposition 1) and quasi-strict propriety at q_n and at q give L(q_n, w) ≤ L(m, w).
   - Lower semicontinuity then gives L(q, w) ≤ L(m, w), a contradiction.
2. **Theorem 5.1 applies.** Take Θ ≔ C, c_q ≔ q, and σ_F(p) ≔ p viewed in C, which is continuous.
   - For finitely supported p, E_p f = Σ_ω p_ω f(ω): truncate f at n and let n → ∞ [REF67_cc §5 checked this line].
   - So quasi-strict propriety makes p a Bayes model for p.
3. **Closure under ties.** If L(m) = L(q), then E_q L(m) = E_q L(q), so m ∈ C.
4. **Uniform dominance.**
   - Put D(q) ≔ E_q L(m) − E_q L(q) ∈ (0,∞]. It is lower semicontinuous under local boundedness (Nielsen, Lemmas 1 and 3), so it has a positive minimum ε on C.
   - For finitely supported p, p·L(m) = V(p) + D(p) ≥ V(p) + ε.
   - Theorem 6.1 with x ≔ L(m) − ε gives the dominator. ∎

*Text after the theorem (two sentences).* Nielsen's Theorem 1 assumes continuity of q ↦ E_p L(q) for every p, together with local boundedness. Theorem 8.2 needs only lower semicontinuity at each world, and drops local boundedness for ordinary dominance, which answers Nielsen §4.2.1 for that conclusion; strict dominance without local boundedness remains open.

*Hypotheses used.* Quasi-strict propriety; lower semicontinuity at each world; compactness of C (automatic); bounded loss of each probability, for the uniform part only.

### 6.3 Conditional reports, including null events [v3.3 6.2–6.4; condensed]

*Setting.* Keep v3.3's setting:
- a finite partition E₁, …, E_k of an arbitrary Ω;
- the compact set Γ of systems (q₀, q₁, …, q_k), with q_j the conditional probability when q₀(E_j) > 0 and free otherwise;
- block losses S_j, report maps ρ_j, and L(x, ω) = S₀(x₀, ω) + S_j(x_j, ω) for ω ∈ E_j.

**Lemma 8.3** [v3.3 6.2]. For finite F, an explicit continuous map p ↦ γ(p) ∈ Γ exists with supp q₀ ⊆ supp p. Cells of small probability get zero weight in q₀, while their conditional reports move continuously to fixed fallback probabilities. The proof is v3.3's (about 6 lines).

**Proposition 8.4** [v3.3 6.3].
- *Hypotheses.*
  - **Block propriety:** each ρ_j(q) minimises q-expected block loss, and every minimiser has the same block losses on F_j.
  - **Lower semicontinuity along coherent systems:** γ ↦ L(ρ(γ), ω) is lower semicontinuous on Γ.
  - Finitely many cells.
- *Conclusions.*
  - Every coherent model is undominated.
  - Every model is weakly dominated by a coherent one.
  - The undominated models are those with a coherent loss profile.
  - If the minimisers are unique, the undominated models are exactly the coherent ones, and every incoherent model is dominated by a coherent one.

*Proof.* As in v3.3:
- Admissibility is block by block, with null cells compared against their own q_j.
- Then Theorem 5.1 with Θ ≔ Γ, c ≔ ρ and σ_F from Lemma 8.3. The Bayes prior is q₀, not p.
- Then Proposition 7.2. ∎

**Example 8.5** [v3.3 6.4; condensed to the computation that matters]. Three worlds, E = {1,2}, and quadratic blocks.
- No assignment with lower semicontinuous losses makes each assigned model a Bayes model for its own index. So the prior in Theorem 4.2(i) must be allowed to differ from p.
- Some Bayes models are dominated: (0,0,1,0,0,1) is dominated by (0,0,1,½,½,1).

Keep the displayed losses and the limit computation along (εt, ε(1−t), 1−ε).

*Drop* the SSK09 comparison paragraph, keeping one sentence: Proposition 8.4 gives a dominance characterisation for a single finite partition with conditional reports that are probabilities on each cell, as SSK09 §6 anticipated.

*Keep* v3.3's sentence on countably many cells (REF67_ldgo §8). With countably many cells, a finitely additive q₀ that is not conglomerable in the partition gives conditional forecasts that are uniformly dominated, under a uniform similarity condition on the scores (SSK14, Theorem 2). So every coherent model being undominated can fail, which is why the number of cells must be finite.

### 6.4 A countable example with non-closed coherent profiles [v3.3 C.1]

**Proposition 8.6.**
- *Setting.*
  - Ω = ℕ, and M_L is the set of square-summable m ∈ [0,1]^ℕ (credences in singletons).
  - L(m, ω) = ‖m‖² + 1 − 2m_ω, the Brier score.
  - C = {m : Σ_n m_n ≤ 1}.
- *Conclusions.*
  - The undominated models are exactly the coherent ones.
  - Every other model is uniformly dominated by a coherent one, with margin d², where d is the ℓ²-distance to C.
  - Neither the coherent loss profiles nor those of Bayes models for finitely supported priors form a closed set.

*Proof* (steps in the order REF67_ldgo §6 requires: C_L = C first, since Theorem 5.1 needs undominated coherent c_θ).
1. **C_L = C and closure under ties.**
   - For c ∈ C, let θ ≔ Σ c_n δ_n + (1 − Σ c_n)θ_∞, where θ_∞ vanishes on finite sets, for example a limit along a free ultrafilter.
   - Every m ∈ M_L has m_ω → 0, so θ(m) = Σ c_n m_n.
   - Then θ(L(m)) − θ(L(c)) = ‖m − c‖², so L(m) ≤ L(c) forces m = c.
2. **Theorem 5.1 applies.**
   - Θ ≔ the finitely additive probabilities on ℕ, and c_θ ≔ (θ{n})_n ∈ C = C_L.
   - Losses are lower semicontinuous: Σ θ{n}² is a supremum of continuous partial sums.
   - σ_F(p) ≔ p. Since Σ p_ω (L(m,ω) − L(p,ω)) = ‖m − p‖² ≥ 0, p is a Bayes model for itself.
3. **Uniform margin.** For m ∉ C and finitely supported p, p·L(m) − V(p) = ‖m − p‖² ≥ d². Here C is ℓ²-closed by Fatou's lemma. Apply Theorem 6.1.
4. **Non-closedness.** L(δ_k) → 2·𝟙 pointwise, and no model has that profile. ∎

*Text.* The dominance claims are known (Kelley 2023, Theorems 3.4 and 4.26; SSK14 Example 3 for m = 0). The point of the example is that Theorem 5.1 does not need the coherent profiles to be closed.

*Hypotheses used.* Lower semicontinuity of the Brier score along the compact family; Bayes for itself.

### Hypotheses used by each application (summary for this outline)

| Application | Worlds | Theorem used | Hypotheses |
|---|---|---|---|
| Prop 8.1 | finite | 4.2; 6.3 | strict propriety relative to M_L; lsc on Δ; uniqueness for closure under ties; finite or continuous losses for uniform dominance |
| Thm 8.2 | any | 5.1; 6.1 | quasi-strict propriety; lsc at each world; bounded loss per probability, for the uniform part only |
| Prop 8.4 | any (finitely many cells) | 5.1 with the Bayes prior ≠ index; 7.2 | block propriety; lsc along Γ; unique minimisers for closure under ties |
| Prop 8.6 | countable | 5.1; 6.1 | Brier score; lsc along the finitely additive probabilities |

All four rest only on refereed v3.3 arguments, so none depends on the new Theorem 5.2.

---

## Part 7. A short remark on constructing rankings (manuscript §9.1)

*Repair of REF67_ldgo's ERROR.* The earlier version attached the wrong hypothesis to protection, and it gave pointers instead of proofs. Of REF67_ldgo's two options, the cleaner is (i): a short proposition, about 0.6 page, with the compressed proofs of v3.3 Theorem 3.13(a), (b), (d) and Remark 3.14. Decision 4 allows a short abstract proposition, and this way the claims are proved in LDG itself.

**Setting** (one paragraph). LDG starts from a *given* ranking; one can also start from the coherent class and *build* one.
- To each ordered pair of evaluable models assign **the change** from the second to the first. The change from a model to itself is the null change, and distinct pairs give non-null changes.
- A change **can be made to** z if it is the change from z to some evaluable model.
- For each world ω, fix a set of changes **guided by the truth at ω**, containing the null change, and a real-valued **world score** φ_ω.
- Rank by: m ⪯_ω m′ iff the change from m′ to m is guided at ω, or no coherent evaluable model can undergo it and φ_ω(m) > φ_ω(m′).

**Proposition 9.1** [v3.3 3.13(a), (b), (d) and 3.14; refereed REF66_ldg; hypotheses stated in words per REF67_ldgo §10].
- (a) Each ⪯_ω is reflexive. If every non-null change guided at ω strictly raises φ_ω (**guided changes improve the score**), then m ⪯_ω m′ with m ≠ m′ implies φ_ω(m) > φ_ω(m′). Hence every accepted cycle consists of equal models, and distinct models are never tied at ω.
- (b) If no model other than a coherent c is reached from c by a change guided at every world (**guidance protects coherent models**), then no model other than c weakly dominates a coherent evaluable model c. So every coherent evaluable model is an undominated coherent model.
- (c) Assume both conditions. Then the following are equivalent:
  - every evaluable model is weakly dominated by an undominated coherent model;
  - every incoherent evaluable model m has a coherent evaluable model c such that the change from m to c is either guided at every world, or can be made to no coherent model and raises the score at every world.

  When these hold, closure under ties holds, and every incoherent model is strictly dominated by an undominated coherent model.

*Proof.*
- (a) The null change is guided, so each ⪯_ω is reflexive. For m ≠ m′, an accepted change raises φ_ω: on the guided branch by hypothesis, on the other branch by definition. Around a cycle the scores are therefore equal, so every step is trivial.
- (b) The change from c to a weak dominator m can be made to c. So it is accepted at every world only as a guided change, and protection gives m = c. A dominator would weakly dominate c and differ from it, because c is tied with itself by reflexivity.
- (c), first ⇒ second. Let an undominated coherent c weakly dominate an incoherent m. At each world the change is guided or improving, and by (a) φ_ω(c) > φ_ω(m) either way. Whether the change can be made to a coherent model does not depend on the world. So either it can be made to none and improves everywhere, or it is guided at every world.
- (c), second ⇒ first.
  - c ⪯_ω m at every world, c ≠ m, and by (a) m ⪯_ω c fails. So c strictly dominates m.
  - By (b), the coherent evaluable models are exactly the undominated coherent ones, and each weakly dominates itself.
  - Closure under ties: a model tied with a coherent c weakly dominates c, so it is c, by (b). ∎

*Text after the proposition* (one paragraph).
- The ranking is acyclic but not in general transitive. Cite the application paper's full-domain example.
- The substantive mathematics is the existence of the improvements in (c). For coherent sets of desirable gambles, the application paper proves this with a uniform margin on an arbitrary set of worlds (its repair theorem), and its ranking is then a corollary.
- Cite the application paper only for that theorem, not for the abstract claims, which are proved here.

---

## Part 8. Scope (manuscript §9.2)

Half a page, in prose.

1. **One ranking at a time.** The theorems identify the undominated models of a given ranking. They do not construct a family satisfying coherent admissibility. That is the application paper's task (Proposition 9.1 and the text after it).
2. **Sufficient conditions, not characterisations.**
   - The hypotheses of Theorems 4.3 and 5.2 are not implied by the conclusion (Remark 5.5).
   - An abstract compactness condition that would be equivalent to the conclusion has no explanatory content (Remark 5.4).
   - The content lies in how the guarantees are obtained. In every application they come from Bayes choices with lower semicontinuous losses, and neither ingredient mentions dominance.
   - *Optional (author's choice):* for loss rankings on finitely many worlds with a compact set of coherent loss profiles, the hypotheses of Theorem 4.3 are equivalent to its conclusion (Proposition 4.8, if kept). Without that fact, a reader may overestimate the content of Theorem 4.3 in the commonest case.
3. **Guarantees on finite sets of worlds do not suffice without a compact family linking them** (Example 5.6). A compact family *exists* whenever the conclusion holds (Remark 5.4), so the point is that the local guarantees must be linked through one. The family need not have closed coherent profiles (Proposition 8.6). Nor need its full comparison sets be closed: in Example 4.7 with worlds duplicated, no compact family whose full comparison sets are closed meets the hypotheses of Theorem 5.2, yet the theorem applies.
4. **What depends only on the ranking.**
   - Proposition 3.1, Theorems 4.3 and 5.2, Corollary 4.4 and §7 depend only on the ranking. They use no completeness, and they are invariant under increasing rescaling at each world (Lemma 2.2).
   - Theorems 4.2 and 5.1 use completeness (through Lemma 2.3) and the numerical form of Bayes choices; Bayes choices are not preserved by nonlinear rescaling (Example 4.6).
   - Margins, uniform and strict dominance, and the existence of Bayes models (§6) use the numerical values. They need lower semicontinuity and Bayes choices.
5. **No order properties are assumed** by Proposition 3.1, Theorems 4.3 and 5.2, or Corollary 4.4 (§7.3).
6. **Truth-directedness does not supply the missing condition.** Keep one proposition as the foil, per the author's preference for a brief foil.

   **Proposition 9.2** [v3.3 D.3; keep with its proof, about 0.6 page]. There is a continuous, truth-directed loss on three partition credences such that:
   - every coherent credence is undominated, with no ties;
   - yet (1,1,0) is weakly dominated by no coherent credence, and some incoherent credence is undominated.

   The loss is L_i(x) = (1 − s_i(x))² + (1/250)(Σ_j x_j − 1)², with s the softmax. Statement and loss: CHECKED REF67_ldgo `misc.py`.

   *Text after the proposition* (two sentences; REF67_ldgo §8 rec. D):
   - It contradicts Joyce's Theorem 2 (2009, pp. 287–288) as stated, so some further condition, such as those of Theorems 4.2 and 4.3, is needed.
   - The failure is located in the sign claim of Joyce's Lemma 1* (pp. 295–296), for credences whose coordinates sum to more than one. At the vertex b³ = (½, ½, 0) built from c = (1,1,0), the required negative signs at the two omitted vertices are in fact positive.
7. **Lexicographic rankings:** the one-sentence pointer of Part 4.

---

## Part 9. Cut list for LDG v3.3

"Stays" means kept with its proof, reworded without jargon. "Condense" means shortened, or turned into a remark. "Goes" means removed from LDG; it is preserved in v3.3 and the round notes.

| v3.3 item | Decision | New place / note |
|---|---|---|
| Title, authors | Stays | — |
| §1 setting; dominance notions; competitiveness | Stays | §2. Delete the sentence listing where strict and uniform dominance appear. |
| §2 opening: 𝔏, M_L, (E), (LA), (A), (C) | Stays, renamed | §3: evaluability, coherent admissibility, closure under ties. Nonemptiness of C_L becomes a consequence of the hypotheses. |
| §2.1 (B), its gloss | Stays, restated | Theorem 4.3 and its gloss |
| §2.1 (S), Prop. 2.1 | Condense | Corollary 4.4 (one-line proof) |
| Prop. 2.2 (defending worlds) | Goes | The gloss after Theorem 4.3 carries its point |
| Ex. 2.3 | Stays | Example 4.5 |
| §2.2 (I), (B∞), (S∞), Prop. 2.4 | Condense | Theorems 5.1 and 5.2; Remark 5.7 |
| Line 157 ("nothing shows (I) can be dropped") | Goes; it is false | Replaced by the text in Remark 5.7 |
| §3 opening (three parts) | Goes | — |
| §3.1 (W), Prop. 3.1, Ex. 3.2 | Stays | Prop. 3.1; Example 3.2 in two sentences |
| §3.2 "Map of the hypotheses" (five kinds, routes A–C, construction restrictions) | Goes | Two sentences in §1 (given ranking versus construction; checkable conditions first) |
| Lemma 3.3 (KKM), Fig. 1 | Stays | Lemma 4.1, Figure 1 |
| Thm. 3.4 | Stays, restated | Theorem 4.3 |
| Cor. 3.5, Fig. 2 | Stays | Corollary 4.4, Theorem 4.2, Figure 2 (new caption) |
| Thm. 3.6, Cor. 3.7 | Stays as Theorem 5.1 (Bayes form) and inside the proof of Theorem 5.2 | Their proof is the proof of 5.1 |
| Paragraph after Cor. 3.7 | Condense | One sentence after Theorem 5.2 |
| §3.5 Prop. 3.8, Ex. 3.9 | Stays | Proposition 7.2, Example 7.3 |
| Cor. 3.10 | Stays, hypothesis restated | Corollary 7.4 |
| §3.6 Lemma 3.11, Prop. 3.12, Lyapunov paragraph | Goes | Part 4; covering paper `lem:zorn`, `thm:route` |
| §3.7 Thm. 3.13(a), (b), (d) and Rem. 3.14 | Condense | Proposition 9.1, with its own short proof and hypotheses in words |
| §3.7 Thm. 3.13(e), (f), Rem. 3.15, set-valued paragraph, Lemmas 3.16–3.17, Ex. 3.18 | Goes | The application paper treats the set-valued case |
| §4.1 "Two separations" | Condense | The gloss after Theorem 4.3, and the note after Theorem 4.2 that the Bayes prior may differ from the index |
| §4.2 Prop. 4.1, Rem. 4.2 (three-world separation of (B) and (S)) | Goes | Replaced by Example 4.7, which is two worlds, refereed, and also gives the infinite separation |
| §4.3 "What certificates do not provide" | Condense | Remarks 5.3–5.5 |
| §5 (D), interpretation, (P1)–(P4) | Condense | §7.1 in prose; the (P) list becomes one sentence |
| Prop. 5.1 | Stays | Proposition 7.1 |
| Prop. 5.2, (C∼), (A∼) | Condense | Remark 7.5 |
| §6 opening paragraph | Stays, shortened | §8 opening |
| §6.1 proper scores; Pettigrew; Predd | Stays, condensed | §8.1, Proposition 8.1 |
| Thm. 6.1 (Nielsen) and its proof | Stays | Theorem 8.2 |
| The two paragraphs comparing with Nielsen | Condense | Two sentences |
| Lemma 6.2, Prop. 6.3, (P), (LSC) | Stays, renamed | Lemma 8.3, Proposition 8.4 (block propriety; lower semicontinuity along coherent systems) |
| Ex. 6.4 | Condense | Example 8.5 |
| SSK conditional-forecast paragraph | Goes | One sentence |
| §7 Scope; §7.1 truth-directedness | Condense | §9.2 |
| App. A.1 lsc, uniform dominance; Prop. A.1 | Stays | §2 (Lemma 2.2), §6 |
| Lemma A.2 | Stays | Lemma 2.3 |
| Cor. A.3 | Stays | Corollary 6.2 |
| Thm. A.4 | Stays | Theorem 6.1 |
| Cor. A.5, Prop. A.9 | Stays, merged | Proposition 6.3 |
| Cor. A.6 (mixtures) | Goes | — |
| Ex. A.7 | Condense | Example 4.6 (rescaling; no Bayes-choice assignment) |
| Prop. A.8 (randomisation; SSSK) | Condense (3–4 lines) | Appended to Example 4.6: the paper's answer to "why not the randomised complete-class theorem?" |
| §A.7 finite event forecasts | Condense | §8.1, about 10 lines; it applies Theorem 4.2 and Prop 6.3(b) on Δ_{τ(Ω)} directly |
| Rem. A.10 (direct Nielsen-type proof) | Goes | — |
| §A.9 Lemma A.11 and the paragraph on numerical certificates | Goes | — |
| §A.10 Ex. A.12 | Condense | Example 6.4 (sharpness) |
| §A.10 SSK Examples 1 and 7 | Condense / goes | One sentence on Example 1 (§7.2); Example 7 goes |
| App. B: Ex. B.1 (closedness needed) | Goes | Figure 2(b) makes the point |
| Lemma B.2, Thm. B.3 (continuous choice of profiles) | Goes | Analysis of (S) |
| Ex. B.4 (no Bayes model) | Goes | Nothing is said in its place (no v3.3 pointers) |
| Lemma B.5, Prop. B.6 (ray construction; equivalence for compact profiles) | Optional (author's choice) | Proposition 4.8, with its proof inline, if kept |
| Rem. B.8 | Goes | — |
| Ex. B.7 | Goes | The vertex witness in Remark 5.5 suffices |
| App. C, Prop. C.1 | Stays | Proposition 8.6 |
| App. D: Lemma D.1, Prop. D.2, §D.3 (comparison with Joyce's appendix) | Goes, except one sentence | The sentence after Proposition 9.2 locates the error (Joyce's Lemma 1*, pp. 295–296). Preserve the rest separately |
| Prop. D.3 | Stays, condensed | Proposition 9.2 (foil) |
| App. E hypothesis table | Goes | Every statement now names its hypotheses in words |
| Bibliography | Condense | Keep KKM, Nielsen, Pettigrew, Predd, SSK09, SSK14, Kelley, Joyce. Drop SSSK and CPMNote |

### 9.1 REF67_cc's line-by-line edit list, and what happens to each item

The definitive paper is a rewrite, not a patch. So every edit is either absorbed into the new structure or made obsolete by a cut. Line numbers refer to `LDG_v3.3.tex`.

| Line(s) | REF67_cc edit | Disposition in the definitive LDG |
|---|---|---|
| 130–157 | Add the local hypotheses; keep (I), (B∞), (S∞) as sufficient conditions; add R1; replace line 157 | Absorbed. Theorem 5.2 states the local hypotheses. The old conditions survive only as Theorem 5.1 (lower semicontinuity plus Bayes choices) and Remark 5.7 (R1). Line 157 is replaced by the text at the end of Remark 5.7. |
| 188 | Route-A paragraph: "(I) together with (B∞)" | Obsolete: §3.2 "Map of the hypotheses" goes |
| 320–341 | Local theorem leads; Thm 3.6 and Cor 3.7 become corollaries; line 341's "compactness of Θ in (I)" | Absorbed. Theorem 5.2 is the general theorem and Theorem 5.1 its Bayes-choice case, with both derivations given. The sentence after the proof of 5.2 reads "compactness of the family carrying the closed guaranteed comparisons". |
| 362–367 | Cor 3.10: replace the hypotheses by (W) | Done: Corollary 7.4 |
| 580 | Extend the rival-dependence remark to infinitely many worlds; add (CC) ⟺ (W) | Done: Remarks 5.3 and 5.4 |
| 603, 610 | (P1) and the parenthetical in Prop 5.1 | Absorbed. Proposition 7.1 assumes only the dominance conclusion; the (P) list becomes one sentence that cites Theorems 4.3 and 5.2. |
| 777 | "(I) … suffices for the dominance results" becomes "one way to meet the local hypotheses" | Absorbed into Remark 5.7 and the sentence before §6 (the corrected formulation) |
| 779 | Prop A.1: add the local hypotheses | Done: Lemma 2.2 transfers every hypothesis that refers only to the ranking, which includes Theorems 4.3 and 5.2 |
| 808–814 | Cor A.3: optionally restate the hypothesis | Corollary 6.2 is stated under Theorem 5.1's hypotheses, which are lsc on the family plus Bayes choices. The optional weakening ("lsc, and every model weakly dominated by a member of the family") is noted in one clause after the proof. |
| 840 | Thm A.4 proof: redirect the compactness argument | Done: step 4 of the proof of Theorem 6.1, written out |
| 854 | Cor A.5 proof cites Cor 3.7 | Done: Proposition 6.3 cites Theorem 4.2 |
| Paragraph after Lemma A.11 (lines 953ff) | Assumes (B∞) with numerical certificates | Obsolete: Lemma A.11 and the paragraph go (Part 9 table) |
| 1167–1175, 1205 | Table rows | Obsolete: the hypothesis table goes |
| 657, 710, 1054 (applications) | Optionally note "hence the local hypotheses" | Not needed: the applications cite Theorem 5.1 directly. One sentence in Remark 5.7 explains why lower semicontinuity puts them where the two conditions coincide. |

**The three textual dependencies on the old infinite theorem** (REF67_cc §4.2). None of them is invalid; all are redirected or removed:
1. The paragraph after Lemma A.11 (numerical certificates with (B∞)) goes, together with Lemma A.11.
2. The proof of Cor A.5 now cites Theorem 4.2 (Proposition 6.3).
3. The proof of Thm A.4 now writes out its compactness step (Theorem 6.1, step 4).

**Also from REF67_cc.**
- The definition of guarantees on a finite set G, with assigned models from the undominated coherent models on all of Ω, is stated before Example 5.6 (REF67_cc §3b).
- Remark 5.4 says that it uses the axiom of choice, and that metrizability adds only a cardinality bound (REF67_cc §1).
- Example 5.6 is the three-line reduced example, with its order properties stated (REF67_cc §§3d, 6).
- Example 4.7 is cited in its two-world form for finitely many worlds, and duplicated by type for infinitely many (REF67_cc §6).

**New material** (not in v3.3):
- Theorem 5.2 and its continuous special case;
- Remarks 5.3–5.5 and 5.7;
- Example 4.7 (two-world form, with the direct proof);
- Example 5.6 (the loss ranking);
- Proposition 9.1 (in place of v3.3 §3.7).

**Kept in condensed form:** randomisation (Example 4.6), and the sentence locating Joyce's error. **Optional:** Proposition 4.8.

The new material comes to about 2.5 pages. With Proposition 4.8 the total rises by about 0.6 page.

**Page estimate.** v3.3 has 43 pages. Of the cut material:
- §3.2, §3.6, §3.7 and §4 come to about 11 pages;
- Appendices B, D and E come to about 9;
- the rest of Appendix A, minus what is kept, comes to about 3.

Adding the new and condensed material gives **23–25 pages**, or 24–26 with Proposition 4.8.

---

## Part 10. Glossary (current term → plain replacement)

| v3.3 term | Definitive LDG |
|---|---|
| certificate B_ω(p) | the priors at which a comparison is guaranteed (the closed set A_ω(m)); "the comparison with m at ω is guaranteed at p" |
| realiser | the assigned model c_p (or c_θ) |
| (B) | the hypotheses of Theorem 4.3: an assigned undominated coherent model per prior, closed guarantees, support-wise coverage |
| (B1) / (B2) / (B3) | closed guarantees / support-wise coverage / one assigned model serving all rivals |
| (S), selection map, chosen model | closed competitive choice (Cor 4.4); assignment; assigned model |
| "makes Bayes choices" | each assigned model is a Bayes model for some prior supported within the support of the prior to which it is assigned |
| (I) | a compact family of undominated coherent models; "with closed full comparison sets" (Remark 5.7); "with lower semicontinuous losses" |
| (B∞) | local guarantees on finite sets of worlds (Theorem 5.2, item 2) |
| (S∞) | continuous (Bayes) choices on finite sets of worlds (Theorem 5.1(ii)) |
| (CC), "compact certificates" | not used; Remark 5.4 describes it in words |
| defending world d_m(p) | dropped |
| route A / B / C; "Map of the hypotheses" | dropped; results are named by what they prove |
| (E) | evaluability: every model is evaluated by some ranking |
| (LA) | (implicit) each ranking has an undominated coherent model; supplied by the hypotheses |
| C_L | the undominated coherent models of L |
| U_L | the undominated models of L |
| (A) | coherent admissibility: every coherent model is undominated under some ranking |
| (C) | closure under ties |
| (W) | the dominance conclusion: every evaluable model is weakly dominated by an undominated coherent model |
| (D) | the dominance principle |
| (P1)–(P4) | one sentence in §7.1 |
| (C∼), (A∼) | Remark 7.5, in words |
| profile; K, R, U_R | loss profile; "the coherent loss profiles", in words; U_R = K becomes "the undominated models are those with a coherent loss profile" |
| K^S, Q^ray, t(p) | dropped |
| competitive on S | kept (defined in §2) |
| (P), (LSC) [conditional reports] | block propriety; lower semicontinuity along coherent systems |
| lexicographic with k levels; Z | dropped (Part 4) |
| record, null record, applies, safe | the change from one model to another; "can be made to z"; "can be made to no coherent model" (Proposition 9.1 only) |
| guided records 𝒢_ω | changes guided by the truth at ω |
| (GI), (GP), (SI) | in words in Proposition 9.1: guided changes improve the score; guidance protects coherent models; every incoherent model has a coherent improvement of the stated kind |
| (RS), (TG), (TS) | dropped from LDG |
| 𝔉, cofinal family (in proofs: "admissible F") | linked sets F: nonempty finite sets of worlds, every finite set of worlds lying in one |
| safe-improvement ranking | "rankings built from guidance and coherence-closed improvements" (Proposition 9.1); "the ranking" in the application paper |
| uniform dominance (as in v3.3 §A.1) | unchanged |
| "weak dominance" in SSK and Joyce | our "dominance" (one footnote in §2) |

---

## Appendix: referee status after REF67_cc and REF67_ldgo

**Refereed by REF67_ldgo** (no mathematical error in the outline; required changes 1–8 made in revision 2):
- Theorems 4.2, 4.3, 5.1 and 5.2, with their proofs.
- Remarks 5.3–5.5.
- The definitional point on guarantees on a finite set G.
- Theorem 6.1, Corollary 6.2 and Proposition 6.3.
- All of §8.
- Proposition 9.2.
- **Both formerly new items:**
  - the loss-ranking Example 5.6, now the main example (§7a, CHECKED `ex56_loss.py`);
  - the direct argument in Example 4.7, now the paper's proof (§7b, CHECKED `ex47.py`).

**Refereed by REF67_cc** (CC67's results):
- Theorem 5.2 and the finite reduction;
- Remarks 5.3 and 5.4 (use of choice; metrizability adds only a cardinality bound);
- Example 4.7's failure for every compact family with closed full comparison sets that meets the hypotheses of Theorem 5.2;
- the relational variant of Example 5.6;
- Corollary 7.4 under the weaker hypothesis.

**Proved by referees only:**
- Remark 5.7's content, Proposition R1. Proved by REF67_cc and checked independently by REF67_ldgo §3, and now written in the paper's own terms. It is nearly tautological.

**Changed in revision 2 and not yet re-refereed** (each repairs a REF67_ldgo finding; all are short):
1. **Proposition 9.1** replaces Remark 9.1. Its statement uses the hypotheses REF67_ldgo §10 names: guidance protects coherent models for (b), and both conditions for (c). The proof is a compression of v3.3 Theorem 3.13(a), (b), (d) and Remark 3.14, which REF66_ldg refereed.
2. **The proof of Remark 7.5** (copied from v3.3 Prop. 5.2) and **the verification paragraph of Example 6.4** (copied from v3.3 A.12, CHECKED by REF67_ldgo).
3. **The case (b) argument in Proposition 6.3** (copied from v3.3 A.9; REF67_ldgo re-derived it).
4. **The event-forecast paragraph** in §8.1, rerouted through Theorem 4.2 and Proposition 6.3(b).
5. **The randomisation lines in Example 4.6** (copied from v3.3 A.8).
6. **Optional Proposition 4.8** (copied from v3.3 B.5–B.6).

**Editorial decisions:**
- **The admissibility method is cut from LDG** (Part 4).
- **Cross-paper requirement:** if the application paper keeps its veto–Brier example, it must carry the Zorn lemma and the separation step itself.
