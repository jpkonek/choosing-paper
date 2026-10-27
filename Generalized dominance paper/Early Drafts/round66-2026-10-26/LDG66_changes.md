# LDG66: changes from LDG_v3.2 to LDG_v3.3 (26 Oct 2026)

Output: `LDG_v3.3.tex` and `LDG_v3.3.pdf` (41 pages). The file compiles cleanly with pdflatex/latexmk, with 0 warnings and 0 overfull boxes. The finite example is checked by `ldg66py/example.py`, with output in `example.out` (CHECKED, exact integer enumeration).

## Status table

| Item | Status |
|---|---|
| Thm 3.13 (a)–(f), the safe-improvement construction theorem | PROVED (in the paper, full proof) |
| Remark 3.14: given (GI), (GP) is necessary for (b), and (SI) is necessary for (c) apart from the guided-at-every-world alternative | PROVED (in the remark) |
| Remark 3.15: with the finest record structure, safety means "rival incoherent" and (e) is vacuous | PROVED (immediate) |
| Set-valued instance: (RS), (GI), (TG), (TS) hold; the record composition identity holds | PROVED |
| Lemma 3.16 (a) hull test; (b) sufficient condition for (GP) with countably many worlds | PROVED |
| Example 3.17 | CHECKED (exact enumeration) |

## What was added, and where

1. **New §3.7, "A route through safe improvements"** (`\label{sec:safe}`), placed after §3.6 (route B) and before §4.
   - **The setting, stated for this subsection only.** Models need not be sets. A *record structure* is any map r : M_L × M_L → 𝓡 with a null record 0, such that r(m,m′) = 0 iff m = m′.
     - A record ρ *applies* to z iff ρ = r(z′, z) for some z′ ∈ M_L.
     - A record is *safe* iff it applies to no member of C ∩ M_L.
     - Each world has guided records 𝒢_ω ∋ 0 and a real score φ_ω.
     - No measurability or topology is assumed.
   - **The safe-improvement ranking.** m ⪯_ω m′ iff r(m,m′) ∈ 𝒢_ω, or r(m,m′) is safe and φ_ω(m) > φ_ω(m′).
   - **Hypotheses, each named where it is used.**
     - (GI): guided non-null changes strictly improve φ_ω.
     - (GP): guidance at every world takes no model to a coherent one other than itself.
     - (SI): the repair hypothesis.
     - Used only for structural clauses: (RS), recorded score comparisons, for independence; (TG) and (TS), guidance composes and safety is inherited along a set T of non-overlapping triples, for disjoint additivity.
   - **Theorem 3.13** (`thm:safe`).
     - (a) Reflexivity. Every accepted cycle is trivial, so there are no nontrivial ties and the chain condition holds. Strict guidance.
     - (b) Under (GP), each coherent evaluable model has no weak dominator except itself.
     - (c) Under (SI), strict dominance of every incoherent model.
     - (d) C_L = U_L = C ∩ M_L ≠ ∅, together with (LA), (C) and (W).
     - (e) Under (RS), the ranking is record-based.
     - (f) Under (TG) and (TS), comparisons compose along T.
     - The theorem is presented as a construction theorem, not an axiom. The text says that (SI) must be proved in each application.
   - **Remark 3.14** (`rem:safe-tight`): how tight the hypotheses are; see the status table.
   - **Remark 3.15** (`rem:safe-records`):
     - the record structure carries the content of the theorem, and the finest-records degenerate case is spelled out;
     - since C_L = C ∩ M_L, (A) reduces to evaluability;
     - the ranking refers to C through safety. This is stated as fact, not as an objective.
   - **"Set-valued models" paragraph.** This is the leading instance: measurable subsets of U modulo null sets, with r(X,Y) = (X∖Y, Y∖X).
     - The paragraph proves the characterisation of "applies".
     - It identifies record-based comparisons with the §3.2 independence condition.
     - It proves the identity r(X,Z) = r(X,Y) ⊔ r(Y,Z) and (TS) for triples with (X△Y) ∩ (Y△Z) null.
     - It proves (RS), (GI) and (TG) for integral scores with sign-based guidance.
   - **Lemma 3.16** (`lem:hull-test`): (a) if least coherent supersets exist, then (A,B) is safe iff μ(A ∩ hull(B)) > 0; (b) with Ω countable, (GP) holds when coherent models contain the sure-gain part and the sure-loss part of U is null.
   - **Plain-English mechanism.** The new acceptances are implied by the removed ones, so no coherent model can undergo the change. The desirable-gambles application is cited in words only, as a forthcoming companion; none of its geometry is imported.
   - **Example 3.17** (`ex:safe`), the single illustrative example. It is finite and abstract:
     - U = {a,b,c} with counting measure;
     - coherence means "a implies c";
     - there are two worlds.
     - (SI) holds via the record ({c},{a}).
     - Plain score comparison would weakly dominate the coherent models ∅ and {a,b,c}. The safe-improvement ranking leaves those pairs incomparable at both worlds.
2. **§3 opening sentence:** notes that §3.7 constructs a ranking rather than starting from a given one.
3. **§3.2, map of the hypotheses:**
   - "four kinds" becomes "five kinds";
   - new paragraph **"Route C: explicit safe improvements"**;
   - the framework paragraph notes that route C rankings satisfy forms of the guidance and independence constraints (Thm 3.13 (a), (e));
   - the construction-restrictions list now includes "record structures and world scores (route C)";
   - "Both routes" becomes "All three routes", and the Proposition 5.1 remark now cites "routes B and C".
4. **§7, Scope and limits:**
   - new paragraph: Theorem 3.13 is sufficient, transfers the question to (SI), and does not supply (SI);
   - one sentence added on (A) for route C families.
5. **Appendix E:**
   - the intro now lists route C;
   - new legend entry "records";
   - new table group "Route C: explicit safe improvements", with rows for Thm 3.13 (a)–(f), Remark 3.14, Lemma 3.16 (a) and (b), and Example 3.17.
6. **Date** set to 26 October 2026. New macros: `\Rec`, `\G`, `\hull`.

Nothing else in v3.2 was changed. There is no commentary comparing versions.

## Answers to the brief's specific requests

- **Are the abstract hypotheses exactly what the proof needs?**
  - Set-valued models are not needed. The lemma needs only a record map with r(m,m′) = 0 ⇔ m = m′. "Applies" and "safe" are defined from the record map alone.
  - The set-valued structure is presented as the leading instance, not as an assumption. The setting paragraph says that it is used in §3.7 only.
  - Items the audit sketch left implicit are now explicit:
    - the null record (in 𝒢_ω, and faithful);
    - closure of guidance under composition, (TG), needed only for (f);
    - upward inheritance of safety, (TS), needed only for (f);
    - record-determination of the score sign, (RS), needed only for (e).
  - Measurability is not needed abstractly.
- **No topology** is used anywhere in route C.

## Flags

- **F1: the finest-records degeneracy.** It is stated openly in Remark 3.15. With r(m,m′) = (m,m′), Theorem 3.13 holds trivially: safety means "rival incoherent", and (SI) says only that every incoherent model is strictly improved upon by a coherent one. So the abstract theorem is mathematically light; its weight lies in coarse records together with (SI). I judged that a referee would raise this point, so it is better stated in the paper. The author may prefer to shorten it.
- **F2: (GP) for uncountable Ω.** The sufficient condition in Lemma 3.16(b) is stated for countable Ω only. The arbitrary-Ω version needs a countable norming set, as in the audit's infinite-world Step E, which is under refereeing. It was deliberately not imported.
- **F3: wording about the companion paper.** The companion is described as proving (SI) "for a score of this integral form, on finitely many worlds". Adjust this if the companion's final scope differs.
- **F4: the (P1) recipe and the hypotheses of Proposition 5.1.** These still name (B), or (I) and (B∞). The route C link goes through the existing §3.2 sentence: Proposition 5.1 uses those conditions only through (W). They were left unchanged to keep the edit minimal.

---

# Revision 2 (26 Oct 2026): responses to REF66_ldg and SR66 §3

Output: `LDG_v3.3.tex` and `LDG_v3.3.pdf`, revised in place. The PDF now has 43 pages. It compiles with 0 warnings, 0 overfull or underfull boxes and 0 undefined references.

Numbering in the revised §3.7:
- Thm 3.13 and Remarks 3.14–3.15 keep their numbers.
- **New Lemma 3.16** (`lem:set-records`) covers the set-valued claims.
- The hull-test lemma is now **Lemma 3.17**, and the example is **Example 3.18**.

## Required changes (REF66_ldg R1–R5)

| # | Change | Where |
|---|---|---|
| R1 | The §1 sentence now reads: "Strict dominance also appears in Corollary cor:strict-ordinal and Section sec:safe; uniform dominance appears only in Appendix sec:real, under additional hypotheses." | §1 |
| R2 | The least-coherent-superset supposition now applies only to Lemma 3.17(a). The Appendix E row for (b) no longer lists it. | Lemma 3.17, App. E |
| R3 | Conditional wording, in four places (next table). | various |
| R4 | Remark 3.14 is rewritten as an exact equivalence (see O1 below). The phrase "(SI) is necessary for (c)" is gone. | Remark 3.14 |
| R5 | Example checked by `ldg66py/check_example.py`, an adaptation of the referee's checker extended to the revision-2 claims. Output in `check_example.out`, ending ALL PASS. The sentence after the example now names exactly what the enumeration confirms. | after Example 3.18 |

The four R3 locations:

| Location | New wording |
|---|---|
| §3.7 opening | Names (GI), (GP) and (SI), and says that its hypotheses, above all (SI), must be proved in each application. |
| §3.2 framework paragraph | "satisfy, under (GI) and (RS) respectively, a form of the first two". |
| §7 Scope | "For rankings built by Theorem 3.13 that satisfy (GP) … What remains is to prove (GI), (GP) and (SI)". The transfer to (SI) is stated as holding "given (GI) and (GP)". |
| Remark 3.15 | "each satisfying (GP)". |

On the Remark 3.15 wording: only (GP) is needed for C_L = C ∩ M_L, because Theorem 3.13(b) does not use (GI), as the referee's O8 notes. So I wrote "(GP)" rather than the referee's "(GI) and (GP)".

## Optional improvements made

- **O1, exact (SI).**
  - (SI) now reads: "a coherent c with either r(c,m) ∈ 𝒢_ω for every ω, or r(c,m) safe and φ_ω(c) > φ_ω(m) for every ω". A sentence after (SI) says that the second alternative is the substantive one.
  - The proof of Theorem 3.13(c) covers both alternatives.
  - Remark 3.14 now proves: (GP) ⇔ (b). It also proves that, given (GI), (SI) ⇔ every incoherent model is dominated by a coherent one ⇔ every incoherent model is weakly dominated by a coherent one, and that every such weak dominance is strict. Given (GI) and (GP), (SI) ⇔ (W).
- **O8, folded into the theorem.**
  - Theorem 3.13 no longer assumes (GI) globally. Clause (a)'s reflexivity and clause (b) are stated without it; (c), (d) and (f) list (GI) explicitly.
  - The Appendix E rows were rewritten to match, clause by clause.
- **O4, numbered lemma.** The new Lemma 3.16 (`lem:set-records`) contains:
  - (a) the record structure, the "applies" characterisation, and null-invariance of guidance and safety;
  - (b) record-based ⇔ independence, where independence is now stated precisely in the W62 (IB) form;
  - (c) the composition identity on T, and (TS);
  - (d) (RS), (GI) and (TG) for integral scores;
  - (e) given record-based comparisons, clause (f) ⇔ the accepted records are closed under disjoint union, with the realising triple.

  A sentence after the lemma explains that "applies" coincides with the set-theoretic attack relation only because M_L contains every measurable subset of U.
- **O5, atoms renamed.** The items are now x, y, z, so the letter c is used only for coherent models.
- **O6, route C in (P1) and Proposition 5.1.**
  - (P1) now requires (LA), (C) and (W), "obtained by route A ((B), or (I) and (B∞)), by route B, or by route C".
  - **Statement change to flag.** Proposition 5.1 (`prop:permissible`) now assumes (LA) and (W). A parenthesis notes that (B), or (I) and (B∞), give this by Theorems 3.4 and 3.6, and the proof now cites Proposition 3.1(a) and Proposition 3.8. This generalises the statement; it does not change its conclusions.
  - The §3.2 sentence and the Appendix E row (Ω "any", technical condition "(W)") were updated to match.
- **O3, the iff form of the hull-test lemma's (b): made.** Its proof is short and complete. For countable Ω, (GP) holds iff every coherent model contains S⁺ and meets S⁻ in a null set. After the lemma, the referee's uncountable counterexample shows that countability matters.

Not made: O2 (weakening (RS)) and O7 (Remark 3.15 now ends with a single sentence on reasonableness).

## SR66 §3: is each hypothesis stated or shown unnecessary?

| SR66 item | In LDG v3.3 |
|---|---|
| (R0) null record ∈ G_ω | Stated in the setting: 0 ∈ 𝒢_ω, with faithfulness r(m,m′) = 0 ⇔ m = m′ |
| (R1) guided changes strictly improve | (GI) |
| (R2) G_ω closed under ⊔, used only for (Add) | (TG), used only for (f) |
| (R3) guidance cannot reach a coherent model | (GP) |
| (R4) strict safe repair | (SI), in its exact form (O1) |
| (R5) converse needs "everywhere-guided records are safe" | Unnecessary: (SI) includes the everywhere-guided alternative, so Remark 3.14 is an exact equivalence with no extra hypothesis |
| Potential form of the scores | Stated: φ_ω is a function on models, and the setting says that score comparisons compose along chains. Record dependence of the score sign is (RS), used only for (e). The difference d_ω itself is not needed. |
| Read "safe" as "attacks"; otherwise decomposability is needed | Abstractly, safety is defined from r ("applies"), and its upward inheritance is the explicit hypothesis (TS). In the set-valued instance, "applies" equals "attacks" because M_L contains all measurable subsets (Lemma 3.16(a)), and (TS) is proved there (Lemma 3.16(c)). The paper notes that a proper subfamily would need (TS) checked separately. |
| G_ω and safety invariant under null sets | Lemma 3.16(a) |
| Measurability, topology, finiteness of Ω | Not used; stated in the opening of §3.7 and in Remark 3.14 |
| Without records the lemma is nearly trivial | Remark 3.15 (finest records), now with the sentence that (e), (f) and a substantive (SI) are what coarse records add |
| (Tr) fails; do not claim transitivity | Nothing claims transitivity. After Theorem 3.13: "The theorem does not assert that the relations ⪯_ω are transitive, and in general they are not." The last paragraph of Example 3.18 exhibits a failure: {y,z} ⪯₁ {x} ⪯₁ ∅, but {y,z} and ∅ are incomparable at world 1. |

## Flag: changed example data

To exhibit intransitivity inside the single permitted example, I changed one score, h₁(z), from 2 to 3. Found by `ldg66py/search_intrans.py`.
- With the old value the ranking happened to be transitive.
- With the new value, the structure the referee verified is unchanged: the same incoherent models, the same repair record ({z},{x}), and the same two plain-score pairs, each incomparable at both worlds.
- The new score vectors are {z} (3,−1), {y,z} (2,0) and {x,y,z} (3,−2).
- `{x}` now has two safe strict improvers, {z} and {y,z}.

All claims were re-verified by `ldg66py/check_example.py` (ALL PASS). `ldg66py/closure_probe.py` confirms that, in this example, even the transitive closure of the ranking leaves every coherent model undominated. The paper does not claim this.

Files in `ldg66py/`: `check_example.py` and `.out`, `search_intrans.py`, `closure_probe.py`. The revision-1 `example.py` was retired; `check_example.py` supersedes it.

## Revision 3 (lead)
- §1 sentence on strict and uniform dominance rewritten per REF66_ldg second round: strict dominance also appears in Cor. strict-ordinal, §3.7 and §6; uniform dominance is defined in Appendix A and used there and in §6.2.
