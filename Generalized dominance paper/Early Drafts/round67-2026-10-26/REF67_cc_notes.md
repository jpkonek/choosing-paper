# REF67_cc: referee report on CC67 (compactness in LDG)

26 October 2026. Independent referee of `CC67_notes.md` and `cc67py/`. I re-derived every proof from LDG v3.3 (`LDG_v3.3.tex`), the audit (`AUDIT_r67_compactness.md`) and the binding message (`AUDIT_r67_message2.md`). I did not rely on CC67's scripts: mine were written from the source texts.

**Labels.** PROVED: checked line by line here. CHECKED: exact rational computation in `ref67cc_py/`, run with `python3 -I`; each `.out` ends in ALL PASS.

**Scripts**
- `ref67cc_py/ref_audit_example.py [G]`: the AUDIT §5 example.
  - Two-world form: (LA), (C), (W), reflexivity, (TC), ties kept, intransitivity, and condition (B) on Δ with realiser c_{p₂}.
  - Copies form: the local coverage (b) and the realisation (a) on every F with at most 3 worlds.
  - Runs: G = 12 and G = 30. The t-grid contains every θ value tested, so the exact switching points θ = s occur.
- `ref67cc_py/ref_escape_example.py [W]`: the CC67 §3.5 example and its reduced form (e_n, h, x). Run with W = 7 and W = 5. It checks:
  - (TC), (LA), (C) and (W);
  - (B) on every F with |F| ≤ 4, on an exact grid with denominator 12, with the listed sets written as closed p₁-intervals;
  - the finite core of the failure argument, over **all** coherent c and **all** supports S;
  - the reduced example.
- Mutation tests:
  - Letting e_n meet z at worlds 1 and 2 breaks the failure core (140 failures).
  - Moving the z-threshold above ½ breaks (B3).
  - Moving it to ¼ still passes. The threshold ⅓ is not tight: any value in (0, ½] works.
  - Widening the audit's x_q section at type 1 to [0, q] breaks (a).

**Overall.** CC67's mathematics is correct throughout. I found no false theorem and no broken proof. The defects are as follows:
- item 4 misstates *what* separates the old hypotheses from the new ones;
- two summary sentences are inaccurate;
- the edit list for LDGO67 is incomplete;
- the line-157 replacement cites the wrong form of the example and omits that compactness is still needed.

All have short repairs (§7). I also add one exact characterisation that sharpens item 4 (§4.1).

---

## Verdict table

| # | Item | Verdict | Repair |
|---|---|---|---|
| 1a | (CC) ⇒ (W) under (LA) | CORRECT (PROVED) | — |
| 1b | (W) ⇒ (CC) via the cofinite topology on C_L; no reflexivity needed | CORRECT (PROVED). Choice is used to pick d(x), and this construction cannot avoid it. | Say "uses the axiom of choice" in the remark. |
| 1c | Compact Hausdorff and compact metrizable variants | Hausdorff: CORRECT. Metrizable: CORRECT *as a conditional*. The cardinality proviso is genuinely needed (§1). | Keep the proviso, and add one sentence saying that metrizability adds only a cardinality bound, not content. |
| 2a | AUDIT §5 example | CORRECT (PROVED; CHECKED). The intransitivity is correctly flagged. | — |
| 2b | Two-world simplification; for finite Ω, (B) does not imply (I)+(B∞) | CORRECT (PROVED; CHECKED). New relative to v3.3: Prop. `prop:necessary` gives equivalence for compact K, and nothing in v3.3 separates the two. | — |
| 2c | Re-interpretation: `ex:hole` already shows (I)+(B∞) is strictly stronger than (W); the AUDIT example separates (I)+(B∞) from the local hypotheses | CORRECT (PROVED) | Add: by §4.1 the separation is *exactly* the failure of (I) for every compact family. |
| 3a | Statement and proof of the local theorem | CORRECT (PROVED). It uses no property of ⪯_ω. | Optionally add the necessary consequence "an ideal member of C_L at each world" (§3). |
| 3b | Hypotheses imply (B) on every finite set, so they do not collapse to (W) | CORRECT, with a definitional GAP. "(B) on G" must use realisers from C_L, which is defined with all of Ω. CC67's Notation says this, but LDG's (B) for the restricted ranking would use the restricted class. | In LDG, state it as "the finite condition on G with realisers in C_L". The non-collapse witnesses are unaffected, since in them Ω is finite or all coherent models are tied. |
| 3c | Trivial choices fail (cofinite topology with Brier on two worlds; constant choices); a rival-dependent index collapses | CORRECT (PROVED). The Brier argument works for any set Θ with the cofinite topology and any realiser map, not only Θ = C_L. | — |
| 3d | §3.5 example: (W), (LA), (C) and (B) on every finite set hold, but the local hypotheses fail | CORRECT (PROVED; finite core CHECKED independently). Unstated: it also satisfies reflexivity and (TC) (CHECKED). | State (TC). |
| 3e | For finite Ω the hypotheses are exactly (B) | CORRECT (PROVED) | — |
| 3f | Hierarchy, strict at each step | CORRECT (PROVED). Strictness for *infinite* Ω at steps 1 and 4 needs the duplication of worlds, which CC67 does not mention (§3). | One sentence: duplicate worlds by type. |
| 3.6 | Ultrafilter characterisation of the compact link | CORRECT (PROVED) | Remark at most, as CC67 says. |
| 4 | What (I)+(B∞) gives beyond the local theorem; which LDG results need (I) and lsc | Row-by-row table: CORRECT. Headline: **ERROR** (minor, in the formulation). (I)+(B∞) does **not** give comparisons with bounds that are not losses of models; LDG line 777 says so, and `ex:discontinuous` shows it. The exact gap is (I) itself (§4.1). Summary sentence "none … except `cor:bayes`": GAP (§4.2). | Replace the headline by Proposition R1 (§4.1), and correct the summary sentence. |
| 5 | Applications meet the local hypotheses directly | CORRECT (PROVED). By R1, in every application the local hypotheses *coincide* with (I)+(B∞) for the family used, since lsc implies (I). | Say so. The weakening matters only when no compact family has closed full comparison sections. |
| 6 | Line 157 and the restructuring | Diagnosis CORRECT. Replacement text: GAP. It cites the two-world form for an infinite-Ω sentence, and it omits that some compact family remains necessary. Edit list: GAP, since it is incomplete (§6). | Use the replacement text and the complete edit list in §6. |

---

## 1. (CC) ⟺ (W)

**(CC) ⇒ (W).** Fix x. Clause 3 gives the finite intersection property for the closed sets K_ω(x). Compactness gives θ in all of them, and clause 2 gives c_θ ⪯_ω x at every ω. Proposition `prop:W`(a) then gives the rest. PROVED.

**(W) ⇒ (CC).**
- Θ = C_L with the cofinite topology is compact. Every open cover has a member with finite complement, and finitely many further members cover that complement.
- Take B_ω(θ) = {x : d(x) = θ}. Then K_ω(x) = {d(x)}, a singleton, which is closed in the cofinite topology.
- Clauses 2 and 3 are immediate.
- Reflexivity is not used: a coherent x may have d(x) ≠ x.
- Choice is used to fix d. The choice-free variant B_ω(θ) = {x : θ ⪯ x} fails, because its sections {θ : θ ⪯ x} can be infinite proper subsets, which are not closed.

PROVED.

**Hausdorff.** Use the one-point compactification of the discrete space C_L. Its points of C_L are isolated and singletons are closed. Set c_∞ arbitrary and B_ω(∞) = ∅. PROVED.

**Metrizable.** A compact metrizable space has at most continuum many points, so at most continuum many distinct realisers. CC67's proviso cannot be dropped. With a single world and more than continuum many pairwise incomparable coherent models (reflexive relations only), (W) holds trivially. But clause 3 for x = c forces c to be a realiser, for every c. So metrizable (CC) is strictly stronger than (W), purely for reasons of cardinality. This supports CC67's conclusion that no amount of topology on Θ gives (CC) content: it adds only a cardinality bound.

The rival-specific variant (AUDIT §6) collapses with Θ_x = {d(x)}. PROVED.

## 2. The AUDIT separation example

I re-derived every clause.
- **Relation.** Every accepted comparison is a score comparison. The removed ones are strict (q < 2, 1 < 2), and every score tie survives in both directions. Hence:
  - reflexivity holds;
  - (TC) holds: A ⪯ B ⪯ C and C ⪯ A force equal scores, and then A ⪯ C;
  - accepted cycles contain no strict step.

  The relation is intransitive: c_q ⪯₁ c_s ⪯₁ x_q, but not c_q ⪯₁ x_q.
- **Dominance.**
  - c_t is weakly dominated only by itself.
  - x_q is dominated by every c_s with s ≠ q.
  - c_q never weakly dominates x_q.
  - So (LA), (C) and (W) hold, with U_L = C_L = {c_t}.
- **Guaranteed sets.** They are [0,s], [s,1], {0}, Θ and {1}. Realisation at each θ was checked case by case.
- **Local version.** θ(p), the type-2 mass, is continuous, and coverage holds in all cases. This includes F containing worlds of only one type, where θ is constantly 0 or 1.
- **Failure of (I)+(B∞).** Theorem `thm:infinite-bounds` forces f to be onto C_L, because the only weak dominator of c_t is c_t. Condition (I) makes Ξ∖E_q closed for q > 0 (type 1, rival x_q) and Ξ∖E₀ closed (type 2, rival x₀). So {E_t} is a partition of the compact space Ξ into uncountably many nonempty open sets, which is impossible.

All PROVED. Every finite clause was CHECKED.

The impossibility is genuinely infinitary. On any finite t-grid, Θ = grid with the discrete topology satisfies (I). So no script can check that part, and none should claim to.

**Two worlds (2b).** CORRECT. With Ω = {1,2}, cofinality forces Ω ∈ 𝔉, and the same partition argument applies. (B) holds with B_ω(p) = {r : p₂ ∈ K_ω(r)} and realiser c_{p₂} (CHECKED). This is new relative to v3.3. Prop. `prop:necessary` makes (B) and (I)+(B∞) equivalent when K is compact, and v3.3 has no separation for non-compact K.

**Re-interpretation (2c).** CORRECT.
- `ex:hole` has (W), and fails (B). Since (I)+(B∞) implies (B) for finite Ω (Prop. `prop:SBinfty`), it also fails (I)+(B∞).
- For an infinite-Ω witness, duplicate the two worlds. (B) on a two-world set with one world of each type is then `ex:hole` itself.

## 3. The local theorem

**Statement and proof (3a).**
- KKM on the closed sets A^F_ω(x), with coverage (b), gives p_F.
- Then (a) gives θ_F(p_F) ∈ ⋂_{ω∈F} K_ω(x).
- Cofinality gives the finite intersection property, and compactness gives θ*.

PROVED. The continuous special case, with A = θ_F⁻¹(K), is also PROVED.

**A useful necessary consequence.** At the vertex δ_ω, (b) forces δ_ω ∈ A^F_ω(x) for every x. So c_{θ_F(δ_ω)} matches or beats every model at ω: there is an ideal member of C_L at every world. This is the cleanest one-line reason the hypotheses do not collapse to (W). It is CC67's "no ideal model" witness, which is a loss ranking and therefore transitive.

**Implication to finite (B) (3b).** The proof (choose F ⊇ G, restrict to the face Δ_G, use realiser c_{θ_F(p)}) is CORRECT for CC67's notion, in which realisers are drawn from C_L defined with all of Ω. A realiser in C_L need not be undominated for the ranking restricted to G, so this is not literally LDG's (B) for that restricted ranking. Use CC67's notion and name it explicitly. None of the separating examples is affected:
- `ex:hole` and the no-ideal-model example have finite Ω;
- in §3.5 and its reduced form, all coherent models are tied, so the two classes coincide.

**Trivial choices (3c).**
- *Cofinite topology, Brier on two worlds.*
  - The KKM point for the rival c_s yields an index whose model is c_s, so every c_t is a realiser.
  - A model c_t with t > s fails c_s at world 2. So (a) excludes world 2 for it, and (b) puts its index in K₁(c_s).
  - So K₁(c_s) is infinite, hence equal to Θ. It then contains the index of c₀, which fails c_s at world 1 when s > 0.

  PROVED, for any set Θ with the cofinite topology and any realiser map.
- *Constant θ_F.* The vertices force a model that is ideal at every world of F. PROVED.
- *Rival-dependent index.* This collapses the theorem: take θ^x ≡ d(x), K = {d(x)} and A = Δ_F. PROVED.

**§3.5 example (3d).** Re-derived in full.
- (LA), (C) and (W) hold.
- (B) holds on every finite F with the stated realisers and listed sets.
- Failure argument:
  - The KKM point for x has a realiser meeting x on F ∋ 1, so the realiser is d or some e_n with n ≥ max F.
  - Rival w_{max F} excludes d.
  - Since e_n meets z only at world 1, rival z puts the index in K₁(z).
  - The finite intersection property and compactness then give a coherent model meeting x everywhere and z at world 1. No such model exists.

PROVED. My independent script confirms the finite core over all coherent c and all supports S, not only CC67's realisers (CHECKED).

Additional facts:
- The relations are reflexive and satisfy (TC) (CHECKED). Only coherent models are related to coherent models, and coherent models are all tied.
- The reduced example (e_n, h, x) is correct. It has (B) on every finite set, but no member of C_L meets x at every world (CHECKED). This is the witness that **some** compact family is indispensable.

**Finite Ω (3e).** Both directions are PROVED.
- (⇒) Cofinality forces Ω ∈ 𝔉.
- (⇐) Take Θ = Δ, realisers by choice, K_ω(x) = {p : x ∈ B_ω(p)}, θ_Ω the identity, and A = K.

**Hierarchy (3f).** The implications are PROVED. Strictness:
1. (I)+(S∞) versus (I)+(B∞): Prop. `prop:threeworld` together with Prop. `prop:necessary`, since K is compact there.
2. (I)+(B∞) versus the local hypotheses: the AUDIT example.
3. The local hypotheses versus (W) with finite (B): §3.5.
4. (W) with finite (B) versus (W): `ex:hole`.

Steps 1, 2 and 4 are finite-Ω witnesses. For strictness at a given *infinite* Ω, duplicate the worlds by type. Step 2's original example already does this. For step 1, the restriction of (I)+(S∞) to one world of each type would yield (S) on three worlds.

## 4. Item 4: what (I)+(B∞) adds, and which results need more

### 4.1 Exact characterisation (new; PROVED)

**Proposition R1.** (I)+(B∞) holds if and only if the hypotheses of the local theorem hold for a compact family that also satisfies (I).

*Proof.*
- (⇒) This is CC67 §3.2.
- (⇐) Put B_{F,ω}(p) = {x : p ∈ A^F_ω(x)}. Its sections are the closed sets A^F_ω(x). Clause (ii) is (b).
- For (i), take θ = θ_F(p). By (a), θ ∈ K_ω(x), and K_ω(x) ⊆ {θ : c_θ ⪯_ω x}.

So the only thing the old pair adds is (I): closed **full** comparison sections against every **evaluable model**.

CC67's headline ("comparisons with bounds that are not losses of evaluable models") is what *lower semicontinuity* adds, not what (I)+(B∞) adds.
- LDG line 777 says this explicitly: "only the bounds given by the losses of evaluable models matter".
- `ex:discontinuous` confirms it. There (S) holds, hence (I)+(S∞) and (I)+(B∞), yet some prior has no Bayes model.

**Repair.** Replace the headline with R1, followed by: "The appendix results that need more than the local hypotheses need lower semicontinuous losses along the family, which implies (I). None uses (I) without lsc, except through the dominance theorem itself."

### 4.2 Row-by-row table

I checked every row against the proofs (LDG lines 343–367, 777–953, 1032–1061) and the hypothesis table (lines 1145–1223). All rows are CORRECT.

| Result | Verified status |
|---|---|
| `cor:strict-ordinal` | Uses only (W) and transitivity. It can be restated under (W). |
| `prop:ordinal` | Add the local hypotheses to its list: they depend only on the ranking. |
| `cor:bayes` | Needs lsc along a family, and (W) with dominators *in that family*. CC67's restatement is correct. By R1, "lsc + local hypotheses on the same family" is no weaker than the current hypothesis. Only the "(W) in the family" form is a genuine weakening. |
| `thm:margin`, `cor:strict`, `cor:upperconvex`, `prop:strict-general`, `rem:direct` | Unchanged. |
| Paragraph after `lem:bayesbounds` | Unchanged. |
| finite-Ω results | Unchanged. |

The summary sentence "None of them needs (B∞) or the old infinite theorem except Cor. `cor:bayes`" is inaccurate in three places:
- the paragraph after `lem:bayesbounds` assumes (B∞) with numerical certificates;
- the proof of `cor:strict` cites `cor:infinite`;
- the proof of `thm:margin` reuses "the compactness argument in the proof of Theorem `thm:infinite-bounds`".

None of these is invalidated. All three are textual dependencies that must be redirected when `thm:infinite-bounds` becomes a corollary. This is a GAP in the summary only.

## 5. Item 5: applications

All PROVED.
- **Theorem `thm:nielsen`.**
  - p ↦ p is weak-star continuous from Δ_F into C.
  - For finitely supported p, E_p f = Σ p_ω f(ω) for [0,∞]-valued f, so quasi-strict propriety makes p Bayes for p.
  - Lemma `lem:bayes-choice` and completeness give coverage.
  - K is closed by lsc.
  - C_L = C is proved independently, also using lsc.
- **Prop. `prop:blocks`.**
  - σ_F is continuous.
  - ρ(σ_F(p)) is Bayes for q₀, with supp q₀ ⊆ supp p.
- **Prop. `prop:countable`.**
  - Σ_n θ{n} ≤ 1, so c_θ ∈ C ⊆ M_L.
  - The sublevel sets are closed by lsc.
  - p is Bayes for itself.
- **§6.1.** Here Ω is finite, and the local hypotheses equal (B), which (S) gives.

As noted above, by R1 each application lies in the region where the local hypotheses coincide with (I)+(B∞), because lsc implies (I). CC67's "no application needs the weakening" is therefore exactly right, and the paper should say why.

## 6. Line 157 and the restructuring

**Diagnosis.** CORRECT. Once the local theorem is in the paper, the sentence "nothing in this paper shows that (I) can be dropped when Ω is infinite" is false.

**Replacement (GAP in CC67's version).**
- CC67 cites the *two-world* form for a sentence about infinite Ω. Cite the original form with copies (or the two-world form duplicated by type) for infinite Ω, and the two-world form for the finite statement.
- CC67 does not say that a compact family is still required. The reduced example shows this, and the audit's §7 says "Compactness cannot be discarded without replacement". Suggested text, without jargon:

> For infinite Ω the models that meet the local guarantees must come from one compact family, and the guaranteed comparisons must form closed sets in it (Theorem [local]). Condition (I), which asks this of every comparison the family makes, is one way to secure it; by Proposition R1 it is the only thing the pair (I), (B∞) adds. It is not necessary: Example [audit] satisfies the hypotheses of Theorem [local], but no compact family satisfies (I) and (B∞), and this already happens with two worlds. Some compact family is needed: in Example [reduced], the finite condition holds on every finite set of worlds, yet some model is weakly dominated by no coherent model. For finite Ω, Theorem `thm:main` needs only (B).

**Complete edit list for LDGO67.** CC67 §6 covers items marked *. Line numbers refer to `LDG_v3.3.tex`.

| Line(s) | Change |
|---|---|
| 130–157* | Add the local hypotheses. Keep (I), (B∞) and (S∞) as sufficient conditions, and add R1. Replace line 157 as above. |
| 188 | The route-A paragraph says "(I) together with (B∞)" for arbitrary Ω. Change to the local hypotheses. |
| 320–341* | The local theorem leads. `thm:infinite-bounds` and `cor:infinite` become corollaries. Line 341 ("compactness of Θ in (I)") becomes "compactness of the family carrying the closed guaranteed comparisons". |
| 362–367 | `cor:strict-ordinal`: replace "(B) with Ω finite, or (I) and (B∞)" by (W). |
| 580* | Extend the remark on rival-dependent certificates to infinite Ω. Add the remark that (CC) is equivalent to (W). |
| 603, 610 | (P1) and the parenthetical in `prop:permissible`: replace "(I) and (B∞)" by the local hypotheses. |
| 777 | "(I) … suffices for the dominance results" becomes "(I) is one way to meet the local hypotheses". |
| 779* | `prop:ordinal`: add the local hypotheses. |
| 808–814* | `cor:bayes`: hypothesis optionally restated as "(I) with lsc, and every model weakly dominated by a member of the family". |
| 840 | `thm:margin` proof: redirect "the compactness argument in the proof of Theorem `thm:infinite-bounds`" to the local theorem's proof. |
| 854 | `cor:strict` proof cites `cor:infinite`. This is still valid, or replace it by `thm:main`, since Ω is finite there. |
| 1167–1175, 1205* | Table rows. Add rows for the local theorem, R1 and (CC) ⟺ (W). `thm:infinite-bounds` and `cor:infinite` become "corollary". The `cor:strict-ordinal` row becomes "(W)". Update the `cor:bayes` row if restated. |
| Applications 657, 710, 1054 | No change is needed. Optionally add "hence the local hypotheses", by R1. |

**Recommendation on examples.** Include the reduced example (three lines) in preference to the full §3.5 example. It carries the more important message: a compact family is indispensable. Keep §3.5 as an optional remark, stating that its relations are reflexive, intransitive and satisfy (TC). Cite the AUDIT example in both its two-world and its copied forms.

## 7. Summary of repairs

1. **Item 4.** Replace the headline by Proposition R1. The difference between old and new is exactly (I). What the numerical appendix needs is lsc, which implies (I).
2. **Item 4.** Correct the summary sentence. Three further textual dependencies on (B∞) and the old proof exist (the `lem:bayesbounds` paragraph, the `cor:strict` proof and the `thm:margin` proof). All remain valid.
3. **Item 3b.** Define "the finite condition on G with realisers in C_L" explicitly. Do not call it LDG's (B) for the restricted ranking.
4. **Item 3f.** Add one sentence on duplicating worlds by type, for strictness at infinite Ω.
5. **Item 3d.** Record that the §3.5 example satisfies reflexivity and (TC).
6. **Item 1c.** Keep the metrizable proviso. It is necessary, and it carries only cardinality, not content.
7. **Item 6.** Use the replacement text in §6, which cites the copies form and the reduced example, and use the complete edit list.
