# WL70: changes to *Coherence and Dominance under General Rankings*, after the AX70L axiom audit

**Files**
- Source: `r69/Coherence and Dominance under General Rankings.tex`, copied to `r70/`. The unedited copy is `r70/build/LDG_r69_copy.tex`.
- Edits: `build/r70edit.py`, plus one follow-up edit to the §6.3 list.

**Compile.** Three pdflatex runs into `r70/build/`. The log has no warnings, no undefined references and no overfull or underfull boxes. The PDF is copied to `r70/`. **25 pages**, up from 23. The increase comes from the new §2.2 inventory (about one page) and the family-assumptions paragraph.

## Revisions R1–R12 (AX70L §4), using AX70L's replacement text

| Rev. | What | Where in the r70 file |
|---|---|---|
| R1 | Evaluability and coherent admissibility are now stated before the theorems. The new paragraph *Families of rankings* explains that coherent admissibility asks for undominatedness under some ranking, not under every ranking, and that no proof uses evaluability. The bullet list in §6.3 is replaced by a back-reference. | §2.1, just before Lemma 2.4. §6.3, opening paragraph. |
| R2 | New text after Thm 4.1: the proof of (a), and likewise the proofs of Thms 3.2, 3.3 and 4.6, obtain weak domination by an assigned model without using that the assigned models are coherent or undominated. Membership in C_L is used only to reach the dominance property, and in (b) and (c). | §4.1, paragraph after the proof of Thm 4.1. |
| R2 (optional) | §8 opening: "(this establishes the hypothesis that the assigned models are undominated coherent models, before Theorem 3.2 or 3.3 is applied)". | §8, first paragraph. |
| R3 | "Coherent admissibility" is no longer used for a property of a single ranking. | §1 last paragraph (Joyce sentence); §7 last paragraph ("…each coherent model be undominated under at least one ranking in the family"); §8 opening ("every coherent model", plus a sentence contrasting a single loss with admissibility across the family); §8.5 closing paragraph. |
| R4 | Necessity wording replaced by sufficiency wording. | Abstract ("are also required to belong"); §1 ¶4 (one feature of the hypotheses; rival-dependence collapses to the conclusion); §4.1 ("cannot be relaxed without making the hypotheses equivalent to the conclusion"); §4.2 italic heading, now "…do not suffice by themselves", and its closing two sentences; §9 "Sufficient conditions" (link not omissible from Thm 4.6, but not necessary for the dominance property). |
| R5 | Prop 6.3 and Prop 6.5(c) now need only transitivity. | Prop 6.3 statement ("relations are transitive (for instance, a preorder ranking)"); end of its proof ("Reflexivity is not used"); Prop 6.5(c); the "iff" claim of Prop 6.5 ("closed under ties or has transitive relations"); §9 "What depends only on the ranking" (new sentence on Props 6.3 and 7.1). |
| R6 | Each permissibility conclusion now carries exactly the conditions it uses. | Prop 6.5: hypothesis examples now list Thms 3.2, 3.3, 4.1, 4.6 and Prop 7.1(c); "Coherent admissibility alone, without the dominance property, makes every coherent model permissible. If, in addition, every ranking … is closed under ties, …". Closing sentence after Prop 6.5: evaluability removed, theorems listed, and a note that evaluability is not needed. |
| R7 | Prop 7.1's hypotheses are stated accurately. Closure under ties is moved to (b), where it follows from protection alone; (c) keeps "Assume both conditions" and concludes only strict dominance. "We say that a change is available…" marks a definition. The new sentence states that Sections 2–6 use no reflexivity, no finite-chain consistency and no three-model case, and that the cycle property is recorded only for comparison. | §7: list item 2; Prop 7.1(b) and (c); proof of (b) (sentence moved from (c)); paragraph after the proof. |
| R8 | The dangling "answers the third question" now reads "…thus gives a second route to the dominance property, independent of Sections 3 and 4." | §7, paragraph after the proof. |
| R9 | Garbled clause: "the ranking is obtained as a consequence" becomes "the dominance property of its ranking follows, as in Proposition 7.1(c)". | §7, companion paragraph. |
| R10 | Thm 3.2 now names closure under ties, giving the loss-profile form as an equivalent. Thm 3.3 inherits this by reference. | Thm 3.2 statement. |
| R11 | The C_L convention is now stated in both directions: C_L = C ∩ U_L "names a subclass and asserts nothing". | §2.1, after the display defining C_L. |
| R12 | The abstract's permissibility clause now carries its conditions: a family of rankings each with the dominance property and closed under ties, plus coherent admissibility. | Abstract. |

## Lead's corrections

| Correction | Where |
|---|---|
| Prop 6.3 and 6.5(c) need only transitivity. | R5 above. |
| Prop 7.1(c)'s hypotheses stated accurately. | R7 above. (c) assumes both guidance conditions. Closure under ties comes from (b). |
| Prop 8.1's uniform-dominance clause needs uniqueness. | Prop 8.1, last sentence now reads: "If p is the only Bayes model for p, for every p, and moreover every probability has finite losses or … continuous, then …". The proof is unchanged and already used uniqueness. |
| Permissibility conclusions carry exactly their conditions. | R6 above. The "iff" claim needs the dominance property for every ranking, plus closure under ties or transitivity. "Coherent ⊆ permissible" needs coherent admissibility alone. "Permissible = coherent" needs the dominance property and closure under ties for every ranking, plus coherent admissibility. Evaluability is used for none of these. |

## Reader-facing inventory (lead item 3)

New **§2.2 "What is assumed and what is proved"** (label `sec:inventory`), directly after Lemma 2.4. It is a six-item list of about one page, in the required order:
1. setting;
2. substantive assumptions: evaluability and coherent admissibility under *some* ranking (on the family), and closure under ties (on a ranking);
3. ordering properties: none assumed. Finite-chain consistency is not used. Completeness enters only via Lemma 2.3 in Thms 3.2–3.3 and their applications. Transitivity enters only via Prop 6.3. Reflexivity is used only in §7, where it is proved;
4. the alternative sufficient packages: the selection argument (Cor 4.2), its finite-world weakening (Thm 4.1), the local infinite-world conditions (Thm 4.6), and the loss-based conditions (Thms 3.2–3.3). These are "not cumulative axioms", and none is implied by the dominance property;
5. Prop 7.1 as a separate method with its own premises;
6. the conclusions that are proved, each with its conditions.

Only descriptive names are used, never old labels.

## Terminology (lead item 4)
- "Dominance property" keeps its meaning: every evaluable model is weakly dominated by an undominated coherent model of L.
- "Finite-chain consistency" appears in §2.2(3) and in §7, each time glossed as "no chain of comparisons ending in a strict reversal", and each time stated to be unused.
- No new axioms. No mathematical statement changed except the Prop 8.1 and Prop 6.3/6.5(c) corrections the lead asked for. Both are wording that matches what the proofs use: 8.1 is now explicit, and 6.3/6.5(c) weaken the hypothesis to the transitivity actually used.

## Not changed
- New label `sec:permissible` on §6.3, used by the R1 paragraph.
- AX70L's "checked and needs no change" items are left as they are.

## Lead edits after AX70L verification
- §2.2 items (2), (3), (4): applied AX70L fixes F1–F3 verbatim.
