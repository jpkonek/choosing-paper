# REF67_ldgo: referee report on the LDG proof outline (`LDGO67_outline.md`)

26 October 2026. I am an independent referee. Every proof in the outline was re-derived from `LDG_v3.3.tex`, `CC67_notes.md`, `REF67_cc_notes.md`, `AUDIT_r67_compactness.md` and `AUDIT_r67_message2.md`. For each "[v3.3 n.m]" item I compared the outline's statement with the v3.3 statement and proof line by line.

**Labels.**
- PROVED: checked line by line here.
- CHECKED: exact or numerical computation in `ref67ldgo_py/`, run with `python3 -I`. Every `.out` file ends in ALL PASS.

**Scripts**
- `ex47.py [G]`: Example 4.7, two-world form, exact rationals on a t-grid that contains the switching points. It checks:
  - reflexivity, the intransitivity witness, C_L, the dominance facts, and closure under ties;
  - the data for Theorem 4.3 (guarantee and coverage at every grid prior);
  - both steps of the new direct argument (full comparison set = complement of {c_p = c_q}; the vertices force c₀ and c₁).
  - Runs: G = 12 and G = 30.
- `ex56_rel.py [W]`: Example 5.6, relational form, truncated to W worlds with e_n for n < W. It checks C_L, the failure of the dominance conclusion, closure under ties, intransitivity, (TC), and guarantees with coverage on every F with |F| ≤ 3 and p₁ on a 1/12 grid.
- `ex56_loss.py [W]`: the new loss-ranking variant of Example 5.6, with integer losses. It checks:
  - pairwise incomparability of the e_n, and that every e_n is undominated;
  - that no e_n weakly dominates x, and closure under ties;
  - that the constant assignment e_{max F} is ideal on every F with |F| ≤ 3.
  - Runs: W = 9 and W = 14.
- `misc.py`:
  - Example 4.6: the only Bayes models for interior p are the endpoints, and p is Bayes for p under the quadratic loss.
  - Example 6.4: the stated profiles, that m is not strictly dominated, and the jump of V.
  - Example 8.5: the profiles and the limit computation.
  - Proposition 8.6: the identity Σ p_ω(L(m,ω) − L(p,ω)) = ‖m − p‖².
  - Proposition 9.2 (Joyce foil): L₁(x*) < 9/25; every coherent b has max(L₁, L₂) > 9/25 on a grid with step 1/300; truth-directedness on 20,000 random moves.

**Overall.** The mathematics of the outline is sound. Every theorem, proposition and example I checked is correct, and both new unrefereed items are correct. The required changes are of four kinds:
- one mathematical ERROR, in Remark 9.1, where a hypothesis is misattributed;
- one statement that is literally false as worded, the unqualified "no compact family has closed full comparison sets", which occurs in three places;
- several places where the definitive text would rely on unpublished v3.3 proofs or v3.3 terminology;
- a few wording errors about what uses completeness and what depends only on the ranking.

The cut list loses nothing that any LDG theorem or application needs. Three items are worth keeping in condensed form for the paper's framing (§8 below).

---

## Verdict table

| # | Item | Verdict | Repair |
|---|---|---|---|
| 1a | Theorem 4.2 (finite Ω, Bayes choices, lsc), assembled from v3.3 Cor 3.5 with Lemma A.2 and line 777 | CORRECT (PROVED). The hypotheses are exactly what the assembly uses. | — |
| 1b | Theorem 5.1 (any Ω, compact family, lsc, continuous Bayes choices), assembled from v3.3 Cor 3.7, Prop 2.4 and Lemma A.2, with a direct proof | CORRECT (PROVED). For weak dominance alone, lsc is stronger than the v3.3 proof needs, which is only closed sets {θ : L(c_θ,ω) ≤ L(m,ω)}. The stronger form is deliberate, since §6 needs lsc. No v3.3 application uses the weaker form, so nothing is lost. | Glossary wording (§1) |
| 1c | The phrase "Bayes model for some prior supported within the support of its index" | CORRECT in the statements, which say "supp p". The glossary's "support of its index" is wrong for Theorem 5.1, where the index is θ ∈ Θ, which has no support. | Say "within the support of the prior to which it is assigned". |
| 2a | Theorem 4.3 versus v3.3 Theorem 3.4 | CORRECT (PROVED). The translation between (B1)–(B3) and the closed sets, guarantee and coverage is exact in both directions (choice picks c_p). The plain-English statement matches. | — |
| 2b | Theorem 5.2 and its proof, with the compactness step written out | CORRECT (PROVED). | GAP: "admissible F" is used in the proofs but never defined, and it clashes with "coherent admissibility". The sets F must be nonempty (§2). |
| 2c | Continuous special case; Theorem 5.1 as a case of 5.2; Theorem 4.3 as the finite case of 5.2 | CORRECT (PROVED). | — |
| 3 | Proposition R1 (Remark 5.7) | CORRECT (PROVED independently). It is nearly a tautology. As written, it compares with "v3.3's pair" and uses "realiser" and "listed", which the definitive paper cannot do. | Reformulate in the paper's own terms (§3). |
| 4a | Remark 5.3 (an assignment that depends on the rival collapses) | CORRECT. A minor GAP: the compact family carrying the singleton K must be named. | Use C_L with the cofinite topology. |
| 4b | Remark 5.4 (the abstract compactness condition is equivalent to the conclusion) | CORRECT (PROVED), including the Hausdorff and metrizable variants and the use of choice. | — |
| 4c | Remark 5.5 (vertex consequence; no-ideal-model witness) | CORRECT (PROVED). | — |
| 4d | Definition: "guarantees on a finite set G", with assigned models from C_L on all of Ω, and the implication from Theorem 5.2's hypotheses | CORRECT (PROVED). Both non-inclusions between "undominated on G" and "undominated on Ω" are witnessed (§4). | — |
| 4e | Example 5.6 (relational) | CORRECT (PROVED; CHECKED). | — |
| 4f | Remark 5.7's consequences and the replacement for line 157 | Content CORRECT. **ERROR as worded:** "no compact family has closed full comparison sets" is literally false, since a one-point family has them. The same wording appears in the remark after Example 4.7 and in Scope item 3. | Add "that meets the hypotheses of Theorem 5.2" (§4). |
| 5 | Cutting the admissibility method from LDG | ACCEPTABLE. No LDG result or application uses it (grep-verified). There is a GAP in the justification, and there is a cross-paper dependency (§5). | Fix the sentence in §9. Confirm that a definitive paper carries the Zorn lemma. |
| 6a | Theorem 6.1 (margins), with the compactness step written out | CORRECT (PROVED). It no longer depends on the deleted Theorem 3.6. | — |
| 6b | Corollary 6.2 | CORRECT (PROVED). | — |
| 6c | Proposition 6.3 (v3.3 A.5 and A.9 merged; cites Theorem 4.2) | CORRECT (PROVED). Case (a) is A.9's first case, which is weaker than A.5's hypothesis. That is a legitimate merge. | One clause: Theorem 4.2's hypotheses are Theorem 5.1's with Θ = Δ, so Theorem 6.1 applies. |
| 6d | Proposition 8.1 (proper scores) | CORRECT. Minor GAP: "V is finite" needs an incoherent model to exist (v3.3 says "when M_L has more than one element"). GAP: the event-forecast reduction cannot pass through Prop 8.1 itself (§6). | Two wording fixes. |
| 6e | Theorem 8.2, Proposition 8.4, Proposition 8.6 | CORRECT (PROVED; 8.6 CHECKED). In 8.6 the proof's step order is inverted: Theorem 5.1 needs C_L = C first. | Reorder. |
| 7a | New: the loss-ranking variant of Example 5.6 | CORRECT (PROVED; CHECKED). Recommend making it the main example (§7). | — |
| 7b | New: the direct argument in Example 4.7 | CORRECT (PROVED; CHECKED). Recommend making it the paper's proof, since the refereed argument cites v3.3 Prop 2.4. | — |
| 8 | Cut list | No cut loses anything that an LDG theorem or application needs. The Joyce counterexample, the conditional-reports application and the countable example are all kept and correct. Recommended retentions are in §8. | §8 |
| 9 | Jargon | Theorem and proposition statements are clean. Remark 5.7 uses "realiser", "listed" and "v3.3's pair". Several proofs are pointers to v3.3. "Admissible" is undefined. | §9 |
| — | Remark 9.1 (constructing rankings) | **ERROR.** Its first bullet attaches the wrong hypothesis. Its second bullet omits hypotheses. Its abstract claims have no proof in either definitive paper (§10). | §10 |
| — | §7.3 "None of the results in §§4–6 uses … completeness"; Scope item 4 "Everything in §§3–5 … depends only on the ranking" | ERROR (wording). Lemma 2.3, and hence Theorems 4.2, 5.1 and all of §6, use completeness and numerical values. | Restrict to Theorems 4.3, 5.2, Cor 4.4 and Prop 3.1. |

---

## 1. Theorems 4.2 and 5.1

**Theorem 4.2. PROVED.**
1. *Competitiveness.* By (i) and Lemma 2.3, c_p is competitive on supp p.
   - Lemma 2.3 is correct, including the case V(π) = ∞.
   - If some m were strictly better than c on S ⊇ supp π, then π·L(m) would be finite. That rules out V(π) = ∞, and in the finite case it makes c fail to be Bayes for π.
2. *Closedness.* {p : L(c_p,ω) ≤ L(m,ω)} is a sublevel set of an lsc function, or all of Δ when L(m,ω) = ∞.
3. *Corollary 4.4* then gives Theorem 4.3's data with A_ω(m) = {p : c_p ⪯_ω m}:
   - the guarantee holds by definition;
   - coverage is competitiveness.
4. *The final clause.* For a loss ranking, a model with the same profile as some c ∈ C_L is automatically undominated, because a dominator of it would dominate c. So "every such model is coherent" is exactly closure under ties.

The hypotheses are exactly what v3.3 §6.1 uses: (S) through Bayes choices and lsc. Nothing is missing:
- (LA) is supplied by the assignment into C_L.
- The notes are accurate: the prior may differ from p and need not vary continuously; the assignment need not be continuous; only the assigned models must be Bayes.

**Theorem 5.1. PROVED.** I checked the direct proof (steps 1–5) against v3.3 Theorem 3.6 and Cor 3.7:
- T_F and the A_ω are closed by lsc and the continuity of σ_F.
- Coverage holds by Lemma 2.3.
- KKM gives T_F ≠ ∅.
- Finite intersections of the T_F contain some T_G, where G is a finite set in the family containing their union.
- Compactness gives θ*. Every world lies in some F.

Compactness alone suffices; no Hausdorff property is needed. The assembly from v3.3 (I), (S∞) and Lemma A.2 is exact. "For finite Ω this is Theorem 4.2" holds in both directions:
- Cofinality forces F = Ω.
- The composition of an lsc map with a continuous σ is lsc.
- Conversely, take Θ = Δ and σ the identity.

**Compact family with continuous assignments.** Continuity of σ_F is used only to make the A_ω closed. Theorem 5.2 shows that it can be dropped when closed guarantee sets are given directly. The statement and the direct proof are consistent with this.

**Dependency claim.** No application depends on Theorem 5.2. This is CORRECT, because Theorem 5.1 has a self-contained proof.
- Minor: the dependency diagram draws "Theorem 5.2 ── Theorem 5.1".
- The paper should present the direct proof as primary and the derivation from 5.2 as a remark, or the reverse, but should say which one it uses.

## 2. Theorems 4.3 and 5.2

**Theorem 4.3. PROVED.** The equivalence with v3.3 (B) is exact:
- (B1) gives closed A;
- (B2) gives coverage;
- (B3) gives the guarantee with one model per p.

The plain-English statement is faithful to v3.3 Theorem 3.4(a)–(c). No property of the relations is used.

**Theorem 5.2. PROVED.**
- Step 1: KKM on each F.
- Step 2: the finite intersection property via a set F containing the given worlds.
- Step 3: compactness.

The continuous special case is PROVED, with A = θ_F⁻¹(K). So is the finite reduction in both directions.

**GAP, "admissible F".**
- The proofs (5.2 steps 1–2, 5.1 step 5, 6.1 step 4, 5.3) speak of "admissible" sets F. The statements never introduce the word.
- The word also collides with "coherent admissibility" and with the cut "admissibility route".
- Separately, the empty set is a finite set. If an empty F were allowed, Δ_∅ = ∅ and step 1 would be vacuous. This causes no harm, because step 2 always chooses an F that contains worlds, but the statement should say "nonempty".
- Repair: in Theorem 5.2(2) and 5.1(ii), write "every finite set of worlds is contained in a nonempty finite set F of worlds for which …; call such sets F *linked*". Any word other than "admissible" will do.

**Wording.** "Its conclusions (b) and (c) are those of Theorem 4.3" should read "and conclusions (b) and (c) of Theorem 4.3 hold".

## 3. Proposition R1 (Remark 5.7): independent check

**Statement checked.** The following are equivalent:
- (I)+(B∞) for some compact family;
- Theorem 5.2's hypotheses for some compact family whose full comparison sets {θ : c_θ ⪯_ω m} are closed.

**(⇒).**
- K_ω(m) := {θ : c_θ ⪯_ω m}. It is closed by (I), and the guarantee holds trivially.
- A^F_ω(m) := {p : m ∈ B_{F,ω}(p)}. It is closed by (B∞).
- θ_F(p) := an index from (B∞)(i), chosen by choice.
- Then (a) holds: p ∈ A^F_ω(m) ⇒ m ∈ B_{F,ω}(p) ⇒ c_{θ_F(p)} ⪯_ω m ⇒ θ_F(p) ∈ K_ω(m).
- And (b) is (B∞)(ii).

**(⇐).**
- B_{F,ω}(p) := {m : p ∈ A^F_ω(m)}. Its sections are the closed sets A, and (ii) is (b).
- For (i), take θ = θ_F(p). Then (a) and item 1 give c_θ ⪯_ω m.
- (I) is assumed.

PROVED. Both sides quantify existentially over the family, and the same family works on both sides.

**Assessment.** R1 is correct but nearly tautological. In the definitive paper there is no "v3.3 pair" to compare with, so R1 as written cannot appear. It uses "realiser" and "listed", and "v3.3's pair" is commentary comparing versions.

**Repair: suggested replacement for Remark 5.7.**
> If the family's full comparison sets {θ : c_θ ⪯_ω m} are closed — for loss rankings, this holds when the losses along the family are lower semicontinuous — then item 1 of Theorem 5.2 holds with K_ω(m) taken to be these sets, and item 2(a) says only that the model assigned to p is at least as good as m at ω whenever p ∈ A^F_ω(m). This is the form in which every application of §8 meets the hypotheses. It is not necessary: in Example 4.7, and in its version with each world copied infinitely often, Theorem 5.2 applies, but no compact family whose full comparison sets are closed satisfies its hypotheses.

## 4. Supporting remarks, the definitional point, and Example 5.6

- **Remark 5.3.** CORRECT. To make "K_ω(m) := {that dominator's index}" closed, the family must be named. Take Θ := C_L with the cofinite topology and c_θ := θ, as in Remark 5.4.
- **Remark 5.4.** CORRECT. The cofinite topology is compact, singletons are closed, and choice fixes d(m).
  - Hausdorff variant: use the one-point compactification. CORRECT.
  - Metrizable variant: it adds only a cardinality bound, as REF67_cc showed. CORRECT.
- **Remark 5.5.** CORRECT.
  - At δ_ω, coverage forces δ_ω ∈ A_ω(m) for every m, so one member of C_L is ideal at ω.
  - The witness has profiles (t, 1−t) with t ∈ (0,1]. They are pairwise incomparable, the conclusion holds trivially, and no model has loss 0 at world 1.
- **Definitional point.** CORRECT. Both non-inclusions hold:
  - (0,5) is undominated on {1} but dominated on Ω by (0,1);
  - (1,0) is undominated on Ω but dominated on {1} by (0,1).

  Restricting to a face Δ_G ⊆ Δ_F keeps closedness, the guarantee and coverage, because supp p ⊆ G. PROVED.
- **Example 5.6 (relational).** CORRECT (PROVED; CHECKED by `ex56_rel.py`).
  - Coherent models are mutually tied and only coherent models relate to them, so C_L = {e_n} ∪ {h}.
  - x is undominated and no coherent model weakly dominates it, so the conclusion fails.
  - The assignment e_N or h, with the stated closed sets, satisfies the guarantee and coverage on every F.
  - The relations are reflexive, satisfy (TC), and are intransitive (h ⪯₁ e₁ ⪯₁ x, but not h ⪯₁ x).
- **"No compact family has closed full comparison sets": ERROR as worded.**
  - A one-point family {c} trivially has closed full comparison sets.
  - What CC67 and REF67_cc proved is narrower: no compact family with closed full comparison sets meets the hypotheses of Theorem 5.2, equivalently (I)+(B∞).
  - The proof needs the family to contain a weak dominator of every c_t, and the only weak dominator of c_t is c_t itself, so the family maps onto C_L. Its full comparison sets against x_q then make every fibre E_t open.
  - The unqualified wording occurs in three places:
    - the remark after Example 4.7;
    - the replacement for line 157 ("although no compact family has closed full comparison sets");
    - Scope item 3.
  - Repair: add "that meets the hypotheses of Theorem 5.2" in each.
- **Scope item 3, "Infinitely many worlds need a compact family".** Misleading. By Remark 5.4, a compact family exists whenever the conclusion holds. What Example 5.6 shows is: "guarantees on every finite set of worlds do not suffice without a compact family linking them". Use that wording.

## 5. Cutting the admissibility method

- **No LDG result or application uses it.** I grepped v3.3 for `lem:zorn`, `prop:lexbayes`, `sec:admissibility` and Lyapunov. They are referenced only in §3.2 (the map, which is cut), in §3.6 itself, and in the Appendix E table (also cut). Every §6 application runs through (S), (S∞) or (I). PROVED by inspection.
- **The justification text is inaccurate in one place.** Bullet 3 says "It does not extend to infinitely many worlds".
  - v3.3 Lemma 3.11 (Zorn) holds for arbitrary Ω (product topology on Z).
  - What needs finitely many worlds is the second step: Prop 3.12, and Lyapunov's theorem, which needs finite dimension.
  - Reword the bullet. This affects the outline only, not the paper.
- **The §9 sentence** is true as stated (it is Lemma 3.11), but it could be read as yielding the dominance conclusion. Add: "; it then remains to show, for the ranking at hand, that every undominated model is coherent."
- **Cross-paper dependency.** The outline justifies the cut by saying that "the application paper already has it". OUT67 Part 8 is only a proof sketch, and it points to the *covering paper draft* (§3, Lemmas "lyap", "zorn", "sep" and "unique"). If neither definitive paper carries the Zorn step, the structured example rests on an unpublished draft.
  - This is not a reason to keep it in LDG.
  - But the lead should confirm that the application paper includes the Zorn lemma (about 10 lines; the covering paper's `lem:zorn` is already gamble-specific) or a citable source.
- **Verdict.** Nothing essential to LDG is lost.

## 6. Merged strict dominance, proper scores, redirected proofs

**Theorem 6.1. PROVED.**
- (a) ⇒ (c): termwise.
- (c) ⇒ (b), coverage step: if p ∉ A_ω for every ω ∈ supp p, then x < L(c) on supp π, so x is finite there and π·x < π·L(c) = V(π). The case π·L(c) = ∞ is immediate.
- Then KKM, then the finite intersection property of the closed T_F, then compactness.

The compactness step is written out, and there is no dependence on the deleted Theorem 3.6. The consequence for uniform dominance (x = L(m) − ε, m with finite losses) is correct.

**Corollary 6.2. PROVED.** π·L(c_θ) is an lsc map on a compact space, so it attains its infimum. Attainment holds without Hausdorff, via nested nonempty closed sublevel sets.

**Proposition 6.3. PROVED.**
- *⇒.* A strict dominator has finite losses and lower expected loss under every prior.
- *⇐.*
  - V is finite.
  - The g_n are lsc (continuous minus usc, with V finite) and increasing.
  - Their limit is > 0 everywhere, so compactness of Δ gives some g_N > 0.
  - Theorem 6.1 with x_N then gives c_p ≤ x_N, which uniformly dominates m with margin 1/N, and its losses are finite.
- *Upper semicontinuity.*
  - Case (a): V = inf_p π·L(c_p), an infimum of continuous linear functions, by Theorem 4.2.
  - Case (b): I re-derived A.9's interior-approximation argument; it is correct and does not use the dominance theorem.
- *The "in particular" clause* is correct.
- *Textual repair.* Theorem 6.1 is stated under Theorem 5.1's hypotheses. Add one clause saying that Theorem 4.2's hypotheses are those of 5.1 with Θ = Δ and σ the identity. The citation of Theorem 4.2, replacing v3.3 Cor 3.7, is correct.

**Proposition 8.1. CORRECT.**
- C_L = C: a weak dominator of p is Bayes for p, hence has profile L(p).
- Theorem 4.2 with c_p = p.
- Prop 7.2 for "coherent profile".
- Uniqueness gives closure under ties, and no incoherent model is Bayes.
- Prop 6.3(a) or (b) gives uniform dominance.

Two GAPs:
1. "V is finite, since V(p) = ∞ would make every model a Bayes model for p" needs an incoherent model to exist. If M_L = C, the uniform clause is vacuous anyway. Write "if some model is incoherent, V is finite, since …".
2. *The event-forecast paragraph* (Predd et al.; SSK09 Theorem 2, Conclusion 3) is listed as "recovered" under Prop 8.1, but Prop 8.1's hypotheses do not fit:
   - there C is not Δ;
   - p ↦ (p(E_i))_i is not injective.

   The paragraph must apply Theorem 4.2 and Prop 6.3(b) directly on Δ_{τ(Ω)}, as v3.3 §A.7 does. State this in the paragraph.

**Theorem 8.2. PROVED.**
- The C_L = C argument: finiteness of E_q L(q) uses some incoherent m′, which exists.
- The q_n inequality: E_q L(q_n) ≥ E_q L(m) forces finiteness.
- Then lsc.
- Theorem 5.1 data: σ_F(p) = p is weak-star continuous, and p is Bayes for p because E_p equals the finite sum.
- The uniform part.

**Proposition 8.4. PROVED** (via v3.3 6.3). Lemma 8.3 gives σ_F, and the Bayes prior q₀ satisfies supp q₀ ⊆ supp p. Example 8.5's profiles and limit computation are CHECKED.

**Proposition 8.6. PROVED; CHECKED (identity).**
- The Bayes identity.
- The θ_∞ argument for C_L = C, using that θ_∞ vanishes on c₀-type sequences.
- Fatou for ℓ²-closedness of C.
- The margin d².
- Non-closedness via L(δ_k) → 2·𝟙.

The order of steps in the proof is wrong: step 1 applies Theorem 5.1, which needs c_θ ∈ C_L, and that is established only in step 2. Swap steps 1 and 2.

**Example 6.4.** CHECKED. Example 4.6 is CHECKED and PROVED, including the connectedness argument.

## 7. New, unrefereed items

**(a) Loss-ranking variant of Example 5.6. CORRECT (PROVED; CHECKED, `ex56_loss.py`).** The losses are L(e_n, ω) = 0 for ω ≤ n and 2 + n for ω > n, and L(x, ·) ≡ 1.
- For m > n, e_m is better on (n, m] and worse beyond m, so the e_n are pairwise incomparable.
- x weakly dominates no e_n, since 1 > 0 at world 1. So C_L = {e_n}.
- No e_n weakly dominates x, since 2 + n > 1 beyond n. So x is undominated and incoherent, and closure under ties holds.
- On every finite F, e_{max F} is ideal throughout F. So the constant assignment with A = Δ_F works.
- The assigned model is also undominated on F, so it satisfies either notion of "undominated".

**Recommendation.** Make this the main Example 5.6, and drop the relational one or make it optional:
- it is a complete preorder (a loss ranking), so no caveat about transitivity is needed;
- it is just as short;
- it also shows that in **Theorem 5.1** the compact lsc family cannot be dropped. On every finite F there are Bayes choices (constant, hence continuous), yet the conclusion fails.

A bounded version also works: L(e_n, ω) = 3 − 1/n for ω > n.

**(b) Direct argument in Example 4.7. CORRECT (PROVED; CHECKED, `ex47.py`).**
- For q > 0, {p : c_p ⪯₁ x_q} = Δ ∖ {c_p = c_q}, and {p : c_p ⪯₂ x₀} = Δ ∖ {c_p = c₀}.
- So, under Corollary 4.4's hypothesis, every fibre {c_p = c_t} is open.
- Δ is connected, so the assignment is constant.
- But competitiveness at δ₁ forces c₀ and at δ₂ forces c₁ (CHECKED: these are the only models ideal there).

Unlike the refereed argument, it does not need surjectivity onto C_L or v3.3 Prop 2.4. **Recommend that it be the paper's proof.** The refereed version cites "v3.3 Prop. 2.4", which the definitive paper cannot cite.

## 8. Cut list

**Kept, and correct.**
- Joyce counterexample (Prop 9.2): statement and loss CHECKED.
- Conditional reports (Lemma 8.3, Prop 8.4, Example 8.5).
- Countable example (Prop 8.6).
- Proper scores (Prop 8.1).
- Nielsen-type probabilism (Theorem 8.2).
- SSK Example 2 (Example 6.4).

No cut removes anything that a retained theorem or application needs.

**Recommended to keep in condensed form** (framing, not logic):
1. **Randomisation and the complete-class theorem (v3.3 Prop A.8).** The outline drops it as "historical", but it is the paper's only answer to the obvious question "why not apply the (randomised) complete-class theorem?", which is a stated aim of this project. It uses the *same* example as Example 4.6, so 3–4 lines appended to Example 4.6 keep it:
   - mixtures of the endpoint profiles strictly dominate every interior coherent profile;
   - no original profile lies below (a/2, a/2).
2. **Joyce.** "Contradicts Joyce's Theorem 2 as stated" should carry one sentence locating the failure: the sign claim of Lemma 1* (Joyce 2009, pp. 295–296) for credences summing to more than one. Readers of a claim that a published theorem is false will ask for this.
3. **v3.3 Prop B.6.**
   - For loss rankings on finitely many worlds with compact coherent profiles, the hypotheses of Theorem 4.3 are equivalent to its conclusion.
   - Remark 5.5 and Scope item 2 are true, but without this fact a reader may overestimate the content of Theorem 4.3 in the commonest case.
   - Either state it in one sentence with the ray proof (about 0.6 page), or leave it out deliberately. This is an author's choice and not required.

**Lost and optional.** v3.3 Prop 4.1 (three worlds, loss ranking) is the only separation of Theorem 4.3 from Corollary 4.4 for a *loss* ranking with compact connected coherent profiles. Example 4.7 is intransitive. Keeping Prop 4.1 requires Prop B.6 for its "(B) holds" step. I agree it is not essential.

**Must be self-contained, not a pointer.** The definitive paper cannot cite v3.3 for proofs:
- Remark 7.5: include v3.3 Prop 5.2's 5-line proof, or drop the remark.
- Example 6.4: include the verification paragraph (about 8 lines).
- Corollary 6.2's note "this is v3.3 Example B.4": either include the 4-line example or say nothing.
- Remark 5.5's "v3.3's Example B.7": write it as an example of the paper.
- Proofs "as in v3.3" (Props 7.1, 7.2 and 8.4, Lemma 8.3) are fine as instructions to copy.

**Minor.**
- Figure 2(b), which replaces Ex B.1: the caption should state that no coherent model weakly dominates m. That is what makes the figure show that closedness cannot be dropped.
- §8.3: keep v3.3's sentence that with countably many cells C_L = C can fail (SSK14 Theorem 2). It explains why finitely many cells matter.
- §7.2, SSK Example 1: the claim that the dominance theorem applies after rescaling by e^t must go through Corollary 4.4 and Lemma 2.2, which are ranking-only. It cannot go through Theorem 4.2, because the Bayes property is not preserved by the nonlinear rescaling, and the original score takes the values ±∞.

## 9. Jargon and conventions

- **Statements.** Every theorem, proposition and corollary statement is free of "certificate", "route", "record", "safe", "realiser" and the old labels.
- **Remark 5.7.** It uses "realiser", "m listed at p" and "v3.3's pair". Replace it with the text in §3 above.
- **Example 4.7.** "By v3.3 Prop. 2.4 …" must go. Use the direct argument.
- **"Admissible F".** Undefined and clashing (§2).
- **Glossary row "makes Bayes choices".** "support of its index" (§1c).
- **"No commentary comparing versions"** forbids the v3.3 pointers listed in §8.

## 10. Remark 9.1 (constructing rankings): ERROR

**Bullet 1** says such rankings "never let a model other than a coherent model c weakly dominate c, *provided guided changes improve the score*". That condition is v3.3 (GI). The protection clause is v3.3 Theorem 3.13(b), and it needs (GP) instead: no model other than c is guided over c at every world. Counterexample with (GI) holding:
- models c (coherent) and m, with finest records;
- r(m,c) guided at every world, and φ(m) > φ(c) everywhere.

Then m weakly (indeed strictly) dominates c.

**Bullet 2.** The equivalence of the dominance conclusion with the repair condition holds given (GI) *and* (GP) (v3.3 Remark 3.14). State both, in words.

**Proofs.** The "pointers" lead to v3.3 Theorem 3.13 and REF66_ldg, which are unpublished, and to OUT67. OUT67's cut list drops the abstract construction lemma "to a short remark in LDG". So the abstract claims would be proved in neither definitive paper. Repair options:
- (i) State the three claims as a short proposition with hypotheses in words, with v3.3's proofs of 3.13(a), (b) and (d) compressed to about 8 lines. Decision 4 allows "a genuinely useful abstract proposition [of] a few lines".
- (ii) Restrict the remark to describing the application paper's ranking and theorem, with no abstract claims.

---

## Ranked list of required changes

1. **Remark 9.1 (ERROR).**
   - Bullet 1's hypothesis must be "no model other than c is guided over c at every world" (guidance protects coherent models), not "guided changes improve the score".
   - Bullet 2 needs both conditions.
   - Either include a short proof or drop the abstract claims (§10).
2. **The qualifier "that meets the hypotheses of Theorem 5.2" (ERROR as worded).** Add it in the remark after Example 4.7, in the line-157 replacement in Remark 5.7, and in Scope item 3 (§4). Also reword Scope item 3 to "guarantees on finite sets of worlds do not suffice without a compact family linking them".
3. **Remark 5.7.** Rewrite R1 in the paper's own terms, without "v3.3's pair", "realiser" or "listed" (§3).
4. **No v3.3 pointers in the paper.** Include the proofs of Remark 7.5 and Example 6.4. In Example 4.7, replace "v3.3 Prop. 2.4" with the direct argument. Write v3.3's Examples B.4 and B.7 inline or omit them (§8).
5. **§7.3 and Scope item 4 (ERROR, wording).** Limit "uses no transitivity, reflexivity or completeness" and "depends only on the ranking" to Prop 3.1, Theorems 4.3 and 5.2, and Corollary 4.4. The loss-ranking results use completeness (Lemma 2.3) and numerical values.
6. **"Admissible F".** Define the term in the statements of Theorems 5.1 and 5.2 with a non-clashing word, and require F nonempty (§2).
7. **Proper-scores section.** Route the event-forecast reduction through Theorem 4.2 and Prop 6.3(b) on Δ_{τ(Ω)}, not through Prop 8.1. Make "V finite" conditional on an incoherent model existing (§6).
8. **Small fixes.**
   - Prop 8.6: put the proof steps in order.
   - Prop 6.3: add a clause that Θ = Δ, so that Theorem 6.1 applies.
   - Remark 5.3: name the compact family.
   - Glossary: "support of the prior to which it is assigned".
   - Theorem 5.2: reword the closing sentence.
   - SSK Example 1: cite Corollary 4.4 with Lemma 2.2.

## Recommended (not required)

- A. Make the loss-ranking variant the main Example 5.6. It is transitive, and it also shows the compact family is needed in Theorem 5.1 (§7a).
- B. Make the direct argument the proof in Example 4.7 (§7b).
- C. Keep the randomisation and complete-class comparison as 3–4 lines on Example 4.6 (§8.1).
- D. Add one sentence locating the error in Joyce's proof (§8.2).
- E. Optionally state v3.3 Prop B.6 (characterisation for compact profiles), with its proof (§8.3).
- F. Correct the outline's justification for the admissibility cut ("does not extend to infinitely many worlds" applies only to the second step). Add "it remains to show undominated ⇒ coherent" to the §9 sentence. Confirm that a definitive paper carries the Zorn lemma for the structured example (§5).
- G. Figure 2(b) caption: say that no coherent model weakly dominates m. Keep the one sentence on countably many cells in §8.3.
