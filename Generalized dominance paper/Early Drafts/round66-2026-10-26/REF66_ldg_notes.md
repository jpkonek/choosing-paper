# REF66_ldg: referee report on LDG v3.3, route C (26 Oct 2026)

**Under review**
- `LDG_v3.3.tex` and its PDF: §3.7 (Theorem 3.13, Remarks 3.14–3.15, the set-valued paragraph, Lemma 3.16, Example 3.17), and the edits to §1–§3.2, §7 and Appendix E;
- `LDG66_changes.md`;
- `ldg66py/example.py`.

The baseline is `LDG_v3.2.tex`.

**Labels**
- PROVED: I checked the argument line by line.
- CHECKED: exact computation, run with `python3 -I` from `ref66ldg_py/`.

**Scripts** (each output file ends in ALL PASS)
- `ref66ldg_py/check_example.py`: an independent bitmask enumeration of Example 3.17. It checks every clause of Theorem 3.13 and Remark 3.14, and Lemma 3.16(a) on all 27 records.
- `ref66ldg_py/stress_abstract.py`: Theorem 3.13 (a)–(f) and Remarks 3.14–3.15 on 4,000 random finite instances, with coarse and finest records, random coherent classes, random guided sets and integer scores.
- `ref66ldg_py/stress_setvalued.py`: the set-valued paragraph and Lemma 3.16 on 1,500 random atom systems that include null (weight-0) atoms. It also checks that record-based comparisons are equivalent to the (IB) condition of W62.

**Compile.** I recompiled from source in `ref66ldg_py/build/`: 41 pages, 0 warnings, no overfull or underfull boxes, and no undefined references. The result matches the supplied PDF.

**Overall verdict.** The mathematics is correct. Every proof in §3.7 is complete, and I found no unstated assumption. The required changes are textual:
- one sentence in §1 that the new material makes false;
- a misattached hypothesis in Lemma 3.16 and its table row;
- four places where conditional conclusions are stated without their hypotheses.

---

## Verdict table

| # | Item | Verdict |
|---|---|---|
| 1a | Thm 3.13(a): reflexivity, no cycles, no nontrivial ties, (TC) and the finite-chain condition, strict guidance | CORRECT (PROVED; CHECKED) |
| 1b | Thm 3.13(b): protection of coherent models under (GP) | CORRECT (PROVED; CHECKED) |
| 1c | Thm 3.13(c): strict dominance under (SI) | CORRECT (PROVED; CHECKED) |
| 1d | Thm 3.13(d): C_L = U_L = C∩M_L ≠ ∅, (LA), (C), (W) | CORRECT (PROVED; CHECKED) |
| 1e | Thm 3.13(e): independence under (RS) | CORRECT (PROVED; CHECKED). (RS) is slightly stronger than needed (optional O2) |
| 1f | Thm 3.13(f): (Add) along T under (TG), (TS) | CORRECT (PROVED; CHECKED). In the set-valued instance it is exactly BRIEF65's (Add) |
| 1g | Are the hypotheses exactly what the proof needs? Any unstated ones? | CORRECT: nothing is unstated. Two wording GAPs: the §3.7 opening and the §3.2 sentence (R3) |
| 2a | Remark 3.14 (necessity) | CORRECT. Wording GAP: "(SI) is necessary for (c)" (R4) |
| 2b | Remark 3.15 (finest records give a trivial theorem) | CORRECT and worth keeping. Minor GAP in its (A) sentence (R3) |
| 3a | Set-valued instance: "applies", the composition identity on T, (TS), (RS), (GI), (TG) | CORRECT (PROVED; CHECKED, including null atoms) |
| 3b | "Record-based comparisons are exactly §3.2's independence condition" | CORRECT under the evident reading. It is exactly W62's (IB) when M_L is all measurable subsets of U. A precise one-line statement is recommended (O4) |
| 4a | Lemma 3.16(a), the hull test | CORRECT. Its setting is stated (set-valued models, M_L all measurable subsets of U modulo null sets, least coherent supersets) |
| 4b | Lemma 3.16(b), (GP) for countable Ω | CORRECT. GAP: the least-coherent-superset hypothesis is attached to (b), which does not use it, and the table lists it as (b)'s hypothesis (R2). Countability is essential (§4) |
| 5 | Example 3.17 | CORRECT (CHECKED independently). Minor: the supplied script does not check every clause the text says it checks (R5) |
| 6a | §3.2 hypothesis map | CORRECT, with a conditional-wording GAP (R3) |
| 6b | §7 Scope and limits | CORRECT, with a conditional-wording GAP (R3) |
| 6c | Appendix E table | GAP in the Lemma 3.16(b) row (R2). Nit in the 3.13(b) row (O8) |
| 6d | No existing result's statement changed | CORRECT (diff-verified) |
| 6e | §1: "Strict and uniform dominance appear only in Appendix A" | ERROR, now plainly false (R1) |
| 7 | Conventions: unnamed environments, \coloneqq, "models", nomenclature, (W) as a stronger objective, no comparison of versions, clean compile | CORRECT |

---

## 1. Theorem 3.13

**Setting.** As stated in the paper:
- r : M_L × M_L → 𝓡, with r(m,m′) = 0 iff m = m′;
- "applies" and "safe" are defined from r alone;
- 0 ∈ 𝒢_ω, and φ_ω is real-valued;
- m ⪯_ω m′ iff r(m,m′) ∈ 𝒢_ω, or r(m,m′) is safe and φ_ω(m) > φ_ω(m′).

The convention that m ⪯_ω m′ means "m is at least as good as m′" matches LDG §1.

**(a) PROVED.** The key monotonicity step is this: if m ⪯_ω m′ and m ≠ m′, then φ_ω(m) > φ_ω(m′). This holds by (GI) on the guided branch and by definition on the safe branch.
- An accepted cycle gives φ(m_0) ≥ … ≥ φ(m_0). So every step is an equality, and every step is trivial.
- With k = 1 there are no nontrivial ties. So each ⪯_ω is antisymmetric and acyclic, and its transitive closure is a partial order.
- "No chain has m_k ≺_ω m_0" is the finite-chain condition. With k = 2 it is (TC) in the AD65/ES64 sense: X ⪯ Y ⪯ Z ⇒ ¬(Z ≺ X).
- Strict guidance follows from antisymmetry.
- Reflexivity uses only the "if" direction of r(m,m′) = 0 ⇔ m = m′.

**(b) PROVED.**
- r(m,c) applies to c (take z′ = m), so it is never safe.
- So a weak dominator must be guided at every world, and (GP) gives m = c.
- A dominator weakly dominates and is not tied, so it is distinct from c. This is excluded.
- (GI) is not used in (b) (O8).

**(c) PROVED.** c ≠ m because one is coherent and the other is not. Then (a)'s "no nontrivial ties" excludes m ⪯_ω c. This is where (GI) matters: without it, m ⪯_ω c could hold through guidance.

**(d) PROVED.**
- C_L = C ∩ M_L ∩ U_L, by the definition in (LA). By (b) this equals C ∩ M_L.
- Nonemptiness: if M_L has an incoherent model, (SI) supplies a coherent one; otherwise M_L ⊆ C. The proof states only the first case; the second is immediate.
- U_L ⊆ C follows from (c).
- (W) follows from reflexivity together with (c).
- (C) follows from (b): if m ≈ c, then m weakly dominates c, so m = c.

**(e) PROVED.** Guidance and safety are properties of the record. (RS) makes the strict score comparison a property of the record too.

**(f) PROVED.**
- If both steps are guided, (TG) applies.
- Otherwise at least one step is not guided, so it was accepted on the safe branch and its score inequality is strict. (TS) makes r(m,m″) safe, and the chain gives φ(m) > φ(m″).
- The degenerate case m = m″ cannot reach the safe branch: there r(m,m″) = 0, and 0 is safe only if C ∩ M_L = ∅, which would require φ(m) > φ(m). In any case reflexivity gives the conclusion directly.

**Are these exactly the hypotheses needed?**
- **(GI)** is needed for (a), (c), (d) and (f), but not for (b). Without it, a guided 2-cycle breaks antisymmetry and (c).
- **(GP)** is equivalent to (b), even without (GI). This is CHECKED: (GP) ⇔ (b) held on all 4,000 random instances.
- **(SI)** is sufficient. It is necessary only up to the guided-at-every-world alternative of Remark 3.14 (see O1).
- **(RS)** is used only for safe, non-guided records. The comparison of guided or unsafe records does not consult φ (see O2).
- **(TG)** and **(TS)** are used exactly as stated.

**Possible unstated assumptions.**
- *Null records.* The faithfulness condition r(m,m′) = 0 ⇔ m = m′ and the condition 0 ∈ 𝒢_ω are both stated. The theorem uses only r(m,m) = 0 ∈ 𝒢_ω. The "only if" direction is used in Lemma 3.16(b) and in the set-valued instance.
- *Reflexivity versus a.e. identification.* In the set-valued instance, faithfulness forces models to be identified modulo null sets, because records are identified modulo null sets. The paper does identify them. My null-atom stress test confirms that the construction is consistent on equivalence classes.
- *Measurability, topology, Ω.* Nothing is needed. Ω is nonempty by LDG §1.
- *Coherent models outside M_L.* These are irrelevant, since safety quantifies over C ∩ M_L. This is consistent with the definition of C_L.

---

## 2. Remarks 3.14 and 3.15

**Remark 3.14: CORRECT. PROVED; CHECKED on random instances.**
- If (GP) fails, there is m ≠ c that is guided over c at every world. By (a), m strictly dominates c.
- If a coherent c dominates an incoherent m, then at every world r(c,m) is guided or safe-improving, and either way φ_ω(c) > φ_ω(m) by (GI). Safety does not depend on ω. So r(c,m) is either safe and improving at every world, or guided at every world.
- The resulting characterisation was CHECKED: an incoherent m is dominated by a coherent model iff (SI) holds at m or some coherent c is guided over m at every world. In either case the dominance is strict.
- *Wording (R4).* (c) is an implication from (SI), so "(SI) is necessary for (c)" is a category slip. The remark actually shows that (SI) is necessary, up to the guided alternative, for the conclusion that every incoherent model is dominated by a coherent one. The same argument shows it is necessary for (W).

**Remark 3.15: CORRECT, and it should stay.**
- With r(m,m′) = (m,m′) for m ≠ m′:
  - r(m,m′) applies only to m′, so it is safe iff m′ is incoherent (CHECKED);
  - (SI) reduces to "every incoherent model is strictly improved at every world by a coherent one";
  - (RS) holds trivially and (e) is vacuous.
- Is the remark needed? Yes. It anticipates the obvious referee objection that the abstract theorem is close to a tautology. It locates the content correctly: in a coarse record structure, which makes (e) a genuine independence property and (SI) a genuine repair theorem.
- It could be shortened by one or two sentences. I recommend against deleting it.
- *Minor GAP (R3).* "Since C_L = C ∩ M_L, a family … satisfies (A) as soon as every coherent model is evaluable by one of them." This needs each ranking in the family to satisfy (GI) and (GP), which are the hypotheses of (b). Given those and (E), the argument is ⋃_L C_L = ⋃_L (C ∩ M_L) = C ∩ M = C. Add "each satisfying (GI) and (GP)".

---

## 3. Set-valued models

**"Applies" characterisation (PROVED; CHECKED with null atoms).** The record (A,B) applies to Z iff B ⊆ Z and μ(A ∩ Z) = 0.
- Converse: take Z′ = (Z∖B) ∪ A. Then
  - Z′∖Z = A∖Z = A a.e.;
  - Z∖Z′ = (Z∩B)∖A = B, using A ∩ B = ∅ and B ⊆ Z.
- The converse needs M_L to be all measurable subsets of U, which the paper assumes.

**Composition on T (PROVED; CHECKED).** If (X△Y) ∩ (Y△Z) is null, then r(X,Z) = (A₁∪A₂, B₁∪B₂). I checked both inclusions for each component.
- (TS) follows by monotonicity of "applies" in the record.
- (TG) holds because the componentwise union of subsets of {h_ω > 0} (respectively {h_ω < 0}) is again such a subset.
- (RS) holds because φ_ω(X) − φ_ω(Y) = ∫_A h_ω − ∫_B h_ω.
- (GI) holds because a non-null subset of {h_ω > 0} has positive integral for any measure. No σ-finiteness is needed.

**(f) is BRIEF65's (Add).** On the set-valued instance, clause (f) with this T is literally AD65's (Add): X ⪯ Y, Y ⪯ Z and (X△Y) ∩ (Y△Z) = ∅ ⇒ X ⪯ Z. With (e), it is equivalent to the accepted records at ω being closed under disjoint union (AD65 Lemma 1.1). The realising triple is X = A₁∪A₂, Y = B₁∪A₂, Z = B₁∪B₂.

**"Record-based = §3.2's independence condition": CORRECT.** Section 3.2 states independence informally ("depends only on where they differ"). The only sensible reading is "depends only on what each model contains where they differ", that is, on (X∩D, Y∩D) with D = X△Y, which is (A,B). This reading coincides with W62's (IB) when M_L is all measurable subsets of U:
- *(⇒)* If X∖S = Y∖S, X′∖S = Y′∖S, X∩S = X′∩S and Y∩S = Y′∩S, then X∖Y = (X∩S)∖(Y∩S) = X′∖Y′, and likewise Y∖X = Y′∖X′. So r(X,Y) = r(X′,Y′).
- *(⇐)* If r(X,Y) = r(X′,Y′) = (A,B), apply (IB) with S = A ∪ B.

This was CHECKED for the safe-improvement ranking on all random instances with |M| ≤ 8. The reading "depends only on the set X△Y" would be absurd, since it would identify (A,B) with (B,A). So the equivalence should be stated in this precise form (O4).

---

## 4. Lemma 3.16

**(a) CORRECT (PROVED; CHECKED).**
- *Setting.* The setting is stated: the set-valued instance (M_L all measurable subsets of U modulo null sets, records (X∖Y, Y∖X)), plus the existence of a least coherent superset hull(B) ∈ C ∩ M_L for every measurable B ⊆ U.
- *Proof.* If μ(A ∩ hull(B)) = 0, then (A,B) applies to hull(B). Conversely, if (A,B) applies to a coherent Z, then hull(B) ⊆ Z, so A ∩ hull(B) is null.
- *Degenerate cases.*
  - B null: hull(∅) is the least coherent model, and (A,∅) is safe iff A meets it non-null. In the round-65 setting this is D_Δ, the sure gains.
  - Q_B = Δ: the same case.
- *Scope.* The lemma does not claim that hulls exist in any particular application. Existence in the round-65 setting is the companion paper's business (hull(B) = D_{Q_B}, which needs boundary-null μ). This is appropriate.
- *Numerical checks.* Of the 1,500 random instances, 1,061 had least coherent supersets, and the equivalence held on every record of each of them.

**(b) Mathematically CORRECT (PROVED; CHECKED), with a presentation GAP (R2).**
- *Proof.* A ⊆ {h_ω > 0} a.e. for each ω. A countable union of null sets is null, so A ⊆ S⁺ ⊆ c, where S⁺ = U ∩ ⋂_ω {h_ω > 0}. But A = X∖c, so A is null. Similarly B ⊆ S⁻ = U ∩ ⋂_ω {h_ω < 0}, which is null.
- *GAP.* The lemma's preamble imposes the least-coherent-superset hypothesis on both parts, but (b) never uses it. The Appendix E row for Lemma 3.16(b) also lists "least coherent supersets" as its hypothesis. That row should list "coherent models contain S⁺; S⁻ null".
- *Countability is essential.* Take:
  - H = U = [0,1] with Lebesgue measure and Ω = [0,1];
  - h_ω = 1 off {ω} and −1 at ω;
  - C = {∅}.

  Then S⁺ = S⁻ = ∅, so every non-countability hypothesis holds. But (U, ∅) = r(U, ∅) is guided at every world, since U ⊆ {h_ω > 0} a.e. So (GP) fails. The countability hypothesis is therefore not cosmetic. This also confirms flag F2 in `LDG66_changes.md`.
- *Sharper form (O3), PROVED.* For countable Ω, (GP) holds iff every coherent model contains S⁺ a.e. and meets S⁻ only in a null set.
  - *(⇐)* As in the paper, but using c ∩ S⁻ null in place of S⁻ null.
  - *(⇒)* If a coherent c misses a non-null P ⊆ S⁺, then r(c ∪ P, c) = (P, ∅) is guided at every world. If c ∩ S⁻ is non-null, use r(c∖S⁻, c) instead.

  In applications where U contains no sure losses this makes no difference, but the iff is cleaner.

---

## 5. Example 3.17

**CORRECT. CHECKED by an independent bitmask enumeration (`check_example.py`, ALL PASS).** Every assertion in the text was verified:
- **Classes and hull.** The 6 coherent and 2 incoherent models, and the hull formula.
- **Scores and repairs.**
  - The score vectors (1,−2), (0,−1), (2,−1) and (1,0).
  - Both repairs have record ({c},{a}), which is safe.
  - Each incoherent model has exactly one safe strict improver: {c} for {a}, and {b,c} for {a,b}.
- **(GP)** holds via Lemma 3.16(b), since no item has the same sign at both worlds.
- **Lemma 3.16(a)** holds on all 27 records. These are all disjoint pairs, and every disjoint pair is a record.
- **Theorem 3.13:**
  - (a): reflexivity, acyclicity by DFS, no ties, strict guidance, (TC), and a strict score increase along every accepted step;
  - (b);
  - (c): strict dominance at both worlds;
  - (d): U_L = C_L = C, (W) and (C);
  - (e) and (RS);
  - (f), (TS), (TG) and the composition identity on every triple in T.
- **Remark 3.14's characterisation** holds.
- **Plain score comparison.** The plain-score weak dominators of coherent models are exactly the two pairs named in the text: ({b,c}, ∅) and ({c}, {a,b,c}). Each pair is incomparable at both worlds under the safe-improvement ranking, for the reasons the text gives.
- **Observation.** The ranking in this example happens to be transitive at both worlds. This is harmless, and the text does not claim otherwise.

**Minor (R5).** The text says that "direct enumeration … confirms every clause of Theorem 3.13". The supplied `ldg66py/example.py` checks antisymmetry, (GP), (SI), the undominated set, the transitivity count and (Add). It does not check:
- strict dominance in (c);
- (e)/(RS);
- (W) and (C) as such.

Acyclicity does follow from antisymmetry plus zero transitivity failures. Either extend the script (my `check_example.py` can be used) or soften the sentence.

**Optional (O5).** The item c in U = {a,b,c} collides with the letter c used throughout for coherent models, including in Theorem 3.13 and Remark 3.14. Renaming the items, for instance to x, y, z, would avoid misreading "the coherent model {c}".

---

## 6. Consistency with the rest of LDG

- **§1, line 42 (ERROR, R1).** The sentence reads: "The main results concern weak dominance and dominance. Strict and uniform dominance appear only in Appendix A, under additional hypotheses."
  - It was already inaccurate in v3.2, because Corollary `cor:strict-ordinal` in §3.5 concerns strict dominance on S.
  - It is now plainly false: Theorem 3.13(c) and (d) and Remark 3.14 assert strict dominance in §3.7.
  - Repair: "Strict dominance also appears in Corollary \ref{cor:strict-ordinal} and Section \ref{sec:safe}; uniform dominance appears only in Appendix \ref{sec:real}."
- **§3.2 hypothesis map: CORRECT, with two conditional-wording points (R3).**
  - The route C paragraph accurately states the three hypotheses and the conclusions. "Guidance alone weakly dominates no coherent model" would be more precise as "no model other than c weakly dominates a coherent c through guided comparisons alone".
  - The framework paragraph says route C rankings "satisfy a form of the first two (Theorem 3.13(a) and (e))". This holds under (GI) and (RS) respectively, so say so.
  - "All three routes establish (W)" is CORRECT under (GI), (GP) and (SI).
  - The claim that Proposition 5.1's conclusions hold "in particular for rankings treated by routes B and C" is CORRECT. Parts (a) and (b) and the final part hold via (W) and (C), which Theorem 3.13(d) supplies. Part (c) is conditional on the ranking being a preorder, which route C rankings need not be, so the claim does not overreach.
- **§3.7 opening (R3).** "Theorem 3.13 shows that this ranking satisfies (LA), (C) and (W), provided one repair hypothesis holds." This understates the hypotheses, which are (GI), (GP) and (SI). Repair: "provided guided changes improve the score, guidance protects coherent models, and a repair hypothesis holds".
- **§7 Scope (R3).** Two fixes:
  - "For rankings built by Theorem 3.13, every evaluable coherent model is undominated" needs (GI) and (GP).
  - "What remains is to prove (SI)" should read "to prove (GP) and (SI)". In the integral instance with finitely many worlds, (GP) is cheap by Lemma 3.16(b), but it is still a hypothesis.

  The new paragraph is otherwise accurate: it says the theorem is sufficient, transfers the question to (SI), and does not supply (SI).
- **Appendix E (R2, O8).**
  - The Lemma 3.16(b) row is wrong (see §4).
  - The Theorem 3.13(b),(c) row lists (GI) for both parts. (b) does not need it. This is optional.
  - The other rows are accurate.
  - The set-valued paragraph proves (RS), (GI), (TG), (TS) and the composition identity, but it is not a numbered result, so the table cannot cite it (O4).
- **No existing result's statement changed.** Diff-verified. Outside §3.7 the changes are:
  - the macros and the date;
  - one clause in the §3 opening;
  - §3.2 ("five kinds", the route C paragraph, the construction-restrictions list, and "All three routes … routes B and C");
  - one new §7 paragraph and one sentence added to the next;
  - the Appendix E introduction and table rows.

  §3.7 is the last subsection of §3, so no later theorem numbers shift.
- **(P1) recipe.** It still names only (B), or (I) and (B∞). This is acknowledged in flag F4, and it is acceptable given the §3.2 sentence. Optionally (O6), add "or (W) by another route, such as Theorem 3.13".

---

## 7. Conventions

| Convention | Status |
|---|---|
| No names on theorem-like environments | CORRECT. grep finds no `\begin{theorem}[…]` and the like. Hypothesis labels follow the existing (E)/(LA) style |
| \coloneqq | CORRECT. Six uses in §3.7. The single `:\Longleftrightarrow` for the defining biconditional is acceptable; optionally write "we put m ⪯_ω m′ when …" |
| "models" | CORRECT |
| Dominance nomenclature (weakly dominates, dominates, strictly dominates, tied at every world) | CORRECT and consistent with §1 |
| (W) as a stronger objective | CORRECT. The §3.2 paragraph is retained |
| No commentary comparing versions | CORRECT. None found |
| Binding decisions | CORRECT. Route C is presented as a construction theorem, not an axiom, and the extra hypotheses (RS), (TG), (TS) are construction hypotheses. Reference to C through safety is stated as a fact, not as an objective. The companion paper is cited only in words, and no gamble geometry is imported |
| Clean compile | CORRECT. Reproduced: 41 pages, 0 warnings |

---

## Ranked list of required changes

1. **R1 (ERROR, §1).** Replace "Strict and uniform dominance appear only in Appendix A" with: "Strict dominance also appears in Corollary \ref{cor:strict-ordinal} and Section \ref{sec:safe}; uniform dominance only in Appendix \ref{sec:real}."
2. **R2 (GAP, Lemma 3.16 and Appendix E).** Move the least-coherent-superset supposition into clause (a). In the table row for Lemma 3.16(b), replace "least coherent supersets" with "coherent models contain U∩⋂_ω{h_ω>0}; U∩⋂_ω{h_ω<0} null". Optionally use the iff form (O3).
3. **R3 (GAP, conditional wording).** State the hypotheses in four places:
   - **§3.7 opening:** name (GI), (GP) and (SI), not "one repair hypothesis".
   - **§3.2 framework paragraph:** "satisfy, under (GI) and (RS), a form of the first two".
   - **§7:** "for rankings built by Theorem 3.13 that satisfy (GI) and (GP) … What remains is to prove (GP) and (SI)".
   - **Remark 3.15, (A) sentence:** add "each satisfying (GI) and (GP)".
4. **R4 (wording, Remark 3.14).** Replace "(SI) is necessary for (c)" with "(SI) is necessary, up to one degenerate alternative, for every incoherent model to be dominated by a coherent one (and for (W))".
5. **R5 (verification claim, Example 3.17).** Either extend `ldg66py/example.py` to check (c) strictness, (e)/(RS), (W) and (C) explicitly, or point to an exhaustive check that does. `ref66ldg_py/check_example.py` does all of these.

## Optional improvements (not required)

- **O1.** Replace (SI) by (SI′): "for every incoherent m there is a coherent c such that either r(c,m) is safe and φ_ω(c) > φ_ω(m) for every ω, or r(c,m) ∈ 𝒢_ω for every ω." Theorem 3.13 holds verbatim, and Remark 3.14 then says that, given (GI), (SI′) is equivalent to every incoherent model being dominated by a coherent model. This makes the necessity statement exact.
- **O2.** Weaken (RS) to records that are safe and not in 𝒢_ω; only those records consult φ_ω. This is cosmetic.
- **O3.** Lemma 3.16(b) as an iff: for countable Ω, (GP) holds iff every coherent model contains S⁺ and meets S⁻ only in a null set (proof in §4).
- **O4.** Turn the set-valued paragraph's proved claims into a numbered lemma, so that Appendix E can cite them. The lemma would cover:
  - the "applies" characterisation;
  - the composition identity on T and (TS);
  - (RS), (GI) and (TG) for integral scores;
  - the precise equivalence "record-based ⇔ (IB)", with the two-line proof in §3.

  Add one sentence noting that, with (e), clause (f) is equivalent to the accepted records at ω being closed under disjoint union.
- **O5.** Rename the atoms in Example 3.17 to avoid the clash with c for coherent models.
- **O6.** Mention route C in (P1), for instance "or (W) by another route".
- **O7.** In Remark 3.15, consider dropping one of the two closing sentences on reasonableness. The point is already made in §3.2 and §7.
- **O8.** In Appendix E, (GI) is not needed for Theorem 3.13(b).

---

# Second round: LDG v3.3, revision 2 (26 Oct 2026)

**What I reviewed**
- the revised `LDG_v3.3.tex` and PDF, which now has 43 pages;
- the "Revision 2" section of `LDG66_changes.md`;
- the scripts `ldg66py/check_example.py` and `.out`, and `search_intrans.py`.

**New scripts of mine** (in `ref66ldg_py/`, all ending in ALL PASS)
- `check_example_r2.py`: my independent enumeration, adapted to the revised data h₁(z) = 3. It adds checks of the stated intransitivity and of the revised Remark 3.14.
- `stress_abstract_r2.py`: the exact form of (SI) and the new Remark 3.14 equivalences, including (SI) ⇔ (W) under (GP), tested on 4,000 random abstract instances.

**Recompile.** I recompiled from source in `ref66ldg_py/build/`: 43 pages, 0 warnings, 0 overfull or underfull boxes.

**Verdict.** All the new mathematics is correct. Required changes R2–R5 were made correctly. R1 was made as I worded it, but my wording was itself incomplete, because uniform dominance also appears in §6.2. This is a residual error that predates v3.3; one more sentence fixes it.

## Verdict table (second round)

| # | Item | Verdict |
|---|---|---|
| S1 | Exact (SI) (guided at every world, or safe and strictly improving at every world) and the revised proof of Thm 3.13(c) | CORRECT (PROVED; CHECKED) |
| S2 | Remark 3.14 as an equivalence: (GP) ⇔ (b); under (GI), (i) (SI) ⇔ (ii) dominance ⇔ (iii) weak dominance; strictness; under (GI) and (GP), (SI) ⇔ (W) | CORRECT (PROVED; CHECKED on 4,000 random instances and in the example) |
| S3 | Thm 3.13 with per-clause hypotheses: (a) reflexivity unconditional and the rest under (GI); (b) under (GP) only; (c) under (GI) and (SI); (d) under (GI), (GP) and (SI); (e) under (RS) only; (f) under (GI), (TG) and (TS) | CORRECT. Each clause names exactly what its proof uses. The (b) proof now cites reflexivity explicitly, which is correct and needs no (GI) |
| S4 | Sentence after the theorem: the relations are not in general transitive | CORRECT. It is witnessed by Example 3.18 |
| S5 | New Lemma 3.16 (set-valued claims) (a)–(e), the precise definition of independence, and the remark about proper subfamilies | CORRECT (PROVED; CHECKED) |
| S6 | Lemma 3.17(a), with the hull hypothesis now local to (a) | CORRECT |
| S7 | Lemma 3.17(b) as an iff, plus the uncountable counterexample | CORRECT (PROVED). Countability is used only in "⇐" |
| S8 | Proposition 5.1, now assuming (LA) and (W), with a revised proof | CORRECT. A strict generalisation with the same conclusions; the proof is valid |
| S9 | The (P1) recipe | CORRECT |
| S10 | Example 3.18 (h₁(z) = 3, intransitivity) | CORRECT (CHECKED independently) |
| S11 | The §3.2, §7 and Remark 3.15 wordings, and Appendix E | CORRECT |
| R1 | §1 sentence on strict dominance | Made as worded, but still inaccurate: uniform dominance is also used in §6.2 (see below) |
| R2–R5 | Lemma hypotheses, conditional wording, the Remark 3.14 rewording, the example script | All CORRECTLY made |
| Conv. | Unnamed environments, \coloneqq, nomenclature, no commentary comparing versions, clean compile | CORRECT |

## Details

**S1–S3: Theorem 3.13 and exact (SI)**
- **(c), first alternative.** Guided at every world gives c ⪯_ω m by definition. c ≠ m, and (a) under (GI) excludes m ⪯_ω c. So the dominance is strict at every world. This is correct.
- **(d).** The nonemptiness argument now covers both cases explicitly.
- **(b).** The proof is valid without (GI). If (GP) holds and m weakly dominates c, then r(m,c) is unsafe because it applies to c, so it is guided at every world, and m = c. A dominator would differ from c, because c ⪯ c holds by reflexivity, and reflexivity does not need (GI).
- **Remark 3.14.**
  - *(GP) ⇔ (b).* A record guided at every world is accepted at every world, so it is a weak dominance.
  - *(iii) ⇒ (i).* At each world (GI) gives φ_ω(c) > φ_ω(m) on either branch. Safety is independent of ω, so either the record is safe and improving at every world, or it is guided at every world.
  - *(W) ⇒ (iii).* Uses C_L ⊆ C ∩ M_L.
  - *(SI) ⇒ (W).* Clause (d), under (GI) and (GP).

  Every step checks. The random tests confirmed (i) ⇔ (ii) ⇔ (iii), strictness of every coherent weak dominance of an incoherent model, and (SI) ⇔ (W) whenever (GP) holds. In these tests (GI) was enforced by rejection.
- **Accepted correction to my R3.** For Remark 3.15's sentence on (A), the author wrote "each satisfying (GP)" rather than my "(GI) and (GP)". This is right: C_L = C ∩ M_L follows from (b), which does not use (GI). My suggested wording was stronger than needed.

**S5: Lemma 3.16**
- **(a).** r(X,Y) = 0 means X△Y is null, so X = Y. "Applies" is characterised as before. Null-invariance holds because records and G_ω are defined on equivalence classes.
- **(b).** The proof is correct in both directions.
  - *(⇒):* X△Y ⊆ S, so X∖Y = (X∩S)∖(Y∩S).
  - *(⇐):* take S = A∪B. Then X△Y = S = X′△Y′, X∩S = A because B is disjoint from X, and Y∩S = B.

  The new precise definition of independence is W62's (IB). It settles my O4.
- **(c) and (d).** As refereed in round 1.
- **(e).**
  - *Closure ⇒ (f):* by (c).
  - *(f) ⇒ closure:* the triple X = A₁∪A₂, Y = B₁∪A₂, Z = B₁∪B₂ realises the records. I rechecked that r(X,Y) = (A₁,B₁) and r(Y,Z) = (A₂,B₂). This uses A₁∩A₂, A₂∩B₁ and B₁∩B₂ null, which follows from the disjoint supports, and A_i ∩ B_i = ∅. Since the ranking is record-based, (f) then gives acceptance of the union.
- **Sentence after the lemma.** It says that a proper subfamily of models would need (TS) checked separately. This is accurate and useful.

**S7: Lemma 3.17(b) as an iff**
- *(⇒):* if P = S⁺∖c is non-null, then (P, ∅) is guided at every world. If c ∩ S⁻ is non-null, then (∅, c∩S⁻) is guided at every world. Neither step needs countability.
- *(⇐):* this direction needs countability, to take the union of the null sets.
- *Counterexample.* The uncountable counterexample is stated correctly. All its other hypotheses hold, and (U, ∅) is guided at every world a.e.

**S8–S9: Proposition 5.1 and (P1)**
- **Statement.** It now assumes (LA) and (W).
- **Proof.**
  - (a) and (b) follow from Proposition 3.1(a), which assumes (LA) and (W), plus (C) for (b).
  - (c) follows from Proposition 3.8, whose hypothesis is literally (W) for preorder rankings.
  - The rest of the proof is unchanged and uses only (b) and (c).
- **Generalisation.** The old hypotheses imply the new ones, by Theorems 3.4 and 3.6, as the parenthesis says. So this strictly generalises the result, and its conclusions are unchanged.
- **Downstream.** Proposition 5.2 inherits "the hypotheses of Proposition 5.1", and its proof uses only 5.1(c). So it remains valid under the broader hypotheses.
- **Table.** The Appendix E rows were updated consistently (Ω "any", technical condition "(W)").
- **Route C rankings.** They satisfy (LA), (C) and (W) by Theorem 3.13(d), so (a), (b) and the last part apply. Part (c) needs preorder rankings, which route C rankings need not be; since (c) is conditional, nothing is overclaimed.
- **(P1).** It now asks for (LA), (C) and (W), and lists all three routes. This is correct.
- **No other statements changed.** A diff against v3.2 confirms that no other pre-existing result statement changed. The full list of hunks outside §3.7 is:
  - the date and macros;
  - §1;
  - the §3 opening;
  - §3.2;
  - (P1), Proposition 5.1 and its proof;
  - §7;
  - the Appendix E introduction, the Proposition 5.1 row and the route C rows.

**S10: Example 3.18**
- **Exact enumeration** (`check_example_r2.py`, ALL PASS) confirms every stated value:
  - the scores {x} (1,−2), {x,y} (0,−1), {z} (3,−1), {y,z} (2,0), {x,y,z} (3,−2) and ∅ (0,0);
  - the repairs {z} → {x} and {y,z} → {x,y}, both with record ({z},{x}), which is safe;
  - (GP) via S⁺ = S⁻ = ∅;
  - exactly the two plain-score pairs named, each incomparable at both worlds;
  - every clause of Theorem 3.13 and Remark 3.14.
- **Exact (SI).** With the new data, {x} has the improvers {z} and {y,z}, and {x,y} has {y,z}. The text claims only the two it names, so nothing is overclaimed.
- **Stated intransitivity.** {y,z} ⪯₁ {x}: the record ({y,z},{x}) is safe, and 2 > 1. {x} ⪯₁ ∅: the record is guided at world 1. But {y,z} and ∅ are incomparable at world 1. The triple is not in T, because the changes overlap in x, so this is consistent with (f).
- **Transitivity failures.** World 1 has exactly two: ({y,z},{x},∅) and ({x,y,z},{y,z},{x}). World 2 has none.
- **The "exhaustive enumeration" sentence.** The author's `check_example.py` does cover every clause the sentence lists. Its checks include:
  - Theorem 3.13 (a)–(f);
  - Remark 3.14 (i)–(iii), (SI) ⇔ (W) and (GP) ⇔ (b);
  - Lemma 3.16(a), (b) and (e);
  - Lemma 3.17(a) and (b).

  Cosmetic nits in that script: one check still carries an `or len(COH) == 6` escape, and several messages still use the old letters a, b, c. Neither affects any verdict.

**S11 and R2–R5: wording and table**
- **§3.7 opening:** names (GI), (GP) and (SI). ✓
- **§3.2:**
  - the framework sentence now says "under (GI) and (RS) respectively". ✓
  - the route C paragraph has the precise (GP) wording and the (SI) equivalence. ✓
- **§7:**
  - "given (GI) and (GP)". ✓
  - "for rankings … that satisfy (GP)". ✓
  - "prove (GI), (GP) and (SI)". ✓
- **Remark 3.15:**
  - "each satisfying (GP)". ✓
  - "(SI) says only that every incoherent model is improved upon at every world by a coherent one" is accurate under (GI). Without (GI), the guided alternative need not improve the score. Optional nit: add "(given (GI))".
- **Appendix E:** the route C rows match the per-clause hypotheses, and the Lemma 3.17(b) row has no spurious hypothesis. ✓
- **Remark 3.14:** "necessary for (c)" is gone. ✓
- **Example script (R5):** now covers every listed clause. ✓

**R1: residual inaccuracy, which my own round-1 wording missed**
- The §1 sentence now says that uniform dominance "appears only in Appendix A". But §6.2 ("Probabilism on arbitrary domains") has a paragraph headed *Uniform dominance* that proves uniform dominance in the main text. §6 also proves strict dominance in places (Pettigrew and §6.3).
- This predates v3.3, and my suggested wording reproduced it.
- Repair: "The main results concern weak dominance and dominance. Strict dominance also appears in Corollary \ref{cor:strict-ordinal}, Section \ref{sec:safe} and some applications in Section \ref{sec:apps}; uniform dominance is defined in Appendix \ref{sec:real} and used there and in Section \ref{sec:nielsen}."

## Required changes (second round)

1. **R1′ (minor ERROR, §1).** Replace the sentence as shown above, so that it no longer says uniform dominance appears only in Appendix A.

There are no other required changes.

**Optional**
- Add "(given (GI))" to the description of (SI) in Remark 3.15.
- The setting sentence "Scores are functions of models, so score comparisons compose along chains of models" is true but adds nothing; consider deleting it.
- Tidy the leftover escape and message strings in `ldg66py/check_example.py`.
