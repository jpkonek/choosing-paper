# WA70: changes for the axiom audit (AX70A, R1–R12)

**File:** `r70/Coherence and accuracy for sets of desirable gambles.tex`, revised from a copy of the r69 file.

**Build:** pdflatex ×3 into `r70/build/`, then the PDF was copied to `r70/`. The log is clean: no warnings, undefined references, overfull or underfull boxes. **Length: 28 pages** (r69: 26).

The changes add no new axioms and no new mathematics. Line numbers refer to the r70 `.tex`.

## Revision map

| Rev | Change | Location |
|---|---|---|
| **R1** (option A) | **Definition of a ranking on a domain.** Reflexivity and the clause "a.e.-equal models tied" are removed. The models on U are linked to the companion paper's evaluation domain. ≺ and "tied" are now defined for every ranking, and the dominance notions of §6.2 are said to apply to any ranking on U. The text states "As in [companion], no property of the relations is assumed". | §6.3, L1004–1011 |
| | **Requirements stated as to be proved.** A conspicuous bold sentence: each of the six requirements must be proved for a ranking before it can be said to cover K; none is assumed, and none is a hypothesis of any result. | §6.3, L1013–1016 |
| | **What each requirement concerns.** (1) concerns each world's relation alone. (2), (3), (4b) and (5) concern the induced dominance relations, with (4b) involving the target. (4a) and (6) concern only the domain and the target. | §6.3, L1013–1016 |
| | **Requirement (4) split** into (4a) "the target lies in the domain" and (4b) "the target is undominated". Knock-on edits: Thm 6.8 proof (e); Cor 7.1(d) proof; "(4a) and (6) automatic on E". | §6.3 list, L1032–1033; Thm 6.8 proof; Cor 7.1(d) proof, L1149 |
| | **Target versus protection.** New sentence: coverage asks only that the target be undominated, whereas protection is a feature of Def 6.1. | after the list |
| **R2** | **Renaming.** (2), (3), (4b) and (5) are renamed "the dominance requirements". | §6.3 preamble |
| | **Contrast with the companion's property.** New paragraph contrasting them with the companion's dominance property (every model is weakly dominated by an undominated coherent model). That property, with closure under ties, gives (2) and (5); the converse fails. Every ranking studied here has both (Thm 6.8(c), Cor 7.1(c), Thm 8.1(b),(c)). | L1056 |
| | **Introduction, "dominance property".** It now reads "in the sense of the companion paper … (Theorem 6.8(c))". | L153 |
| | **Note after Thm 6.8.** "Part (c) is the dominance property in the sense of the companion paper". | L1101 |
| | **"Dominance property" elsewhere.** Other uses (abstract L59; §9.1 L1316, L1326) are in the companion's sense or are generic, and are left unchanged. | — |
| **R3** | **Introduction.** Strict guidance, independence and finite-chain consistency are "all that coverage asks of each world's comparisons". Disjoint additivity and the absence of distinct-model ties are marked as not required. | L134–139 |
| **R4** | **Introduction, "What this achieves".** The constraints are named: strict guidance, independence and finite-chain consistency. | L179–182 |
| **R5(a)** | **§9.1.** Changed to "Under the instance μ{P_S=0}=0 of (M2), property (3) … alone protects coherent models". | L1307 |
| **R5(b)** | **§9.2 rewritten, with a label.** The rewrite separates three conditions: protection (under this ranking), coherent admissibility (family-level, "under at least one ranking … not necessarily under every one"), and target undominatedness. It shows that (3) implies protection under the {P_S=0} instance, and says why (3) is stronger (Ex 6.4; comparisons between incoherent models). It notes that (3) is not needed for coverage: veto–Brier dominates the coherent model D_{p}. Independent justification is left open. | L1328ff |
| **R5(c)** | **Open question.** Now asks about weakening (3) to protection for a single ranking, and notes that coherent admissibility is the relevant weakening if a family may share the work. | L1394 |
| **R6** | **§9.1.** The requirements of coverage are separated from the two properties that coverage does not require (disjoint additivity, no distinct-model ties). | §9.1, first paragraph (L1293) |
| **R7** | **Renaming "acyclicity" → "finite-chain consistency" throughout:** intro L135; Prop 6.2(b) L827; requirement (1); §6.3 explanatory paragraph L1046; Thm 8.1(a) "hence finite-chain consistent" L1237; §8 L1264; §9.1. | as listed |
| | **Additions** to the §6.3 paragraph: the case k = 2 is the three-model condition; it is Suzumura consistency, weaker than transitivity and stronger than acyclicity of the strict part. `grep -i acycl` now finds only "acyclicity of the strict part". | §6.3, L1046 |
| **R8** | **§9.3, roles of (M2).** Now lists three roles: ordinary optimal choices; consistent models inside their hulls, giving the test of Lemma 2.6; and coherent sets of desirable gambles coinciding with coherent models. Protection uses only μ{P_S=0}=0, which is essential (Ex B.2). | L1371 |
| **R9** | **Weaker stated hypotheses.** Lemma 6.5, Prop 6.6 and Prop 6.7 now assume only "μ{P_S=0}=0 (an instance of (M2))". This weakens the stated hypotheses; the proofs use only this instance. The same instance is named in §9.1 (R5a), §9.2 (R5b) and the inventory (A). | L942, L963, L978 |
| **R10** | **Thm 8.1(d).** Now reads "D_K ⊆ U; and U is open and contains ∂D_K∖{0} …". This makes (4a) explicit; it is proved in App D, Step 9. | L1245 |
| **R11** | **§8 "Reach".** The target is renamed K̃, to avoid a clash with Prop C.1's K′. | L1277 |
| **R12** | **§9.1 companion paragraph.** Def 6.1 is mapped onto the companion's construction. Its two guidance conditions are Prop 6.2(b) (guided changes improve the score) and Lemma 6.5 with Prop 6.6 (guidance protects coherent models). The required improvements come from Thm 5.1. | L1321 |

## Reader-facing inventory (lead's item 2)

- **Placement.** A new opening of §6, before §6.1 (L751ff). It is under one page, a five-item list with descriptive names.
  - **(A) The setting (assumed).** It covers the role of each measure condition. Full support only tells credal sets apart and characterises local freedom; no existence or dominance claim uses it.
  - **(B) The coverage requirements (to be proved).** They are never assumed.
  - **(C) The construction's own commitments (chosen).** These are the three conditions and maximality of Prop 6.3. They are flagged as characterising this construction only, and the third is flagged as stronger than coherent admissibility and left open (§9.2).
  - **(D) What is proved about this ranking.** Completeness and transitivity fail in general (Ex 6.4). "No ties" and disjoint additivity are not requirements on every covering ranking.
  - **(E) The veto–Brier example's separate assumptions.** These are n ≥ 2, Lebesgue null sets, an interior contamination target and the half-space domain, plus Lyapunov and Zorn. None enters §§2–7.

## Not changed

- **No mathematical statement was changed**, apart from two things. R9 weakens stated hypotheses to what the proofs use. R1 removes the unused reflexivity from the definition of a ranking on a domain, which strengthens the necessity claims of Cor 7.1(d) and Prop C.1(a),(c), since they now quantify over more rankings. The proofs of those claims use only (4a) and (6), so they hold unchanged.
- **No citation of a numbered result of the companion paper.** AX70A's suggested "[companion, Prop. 6.1]" was dropped, because the companion has been restructured and its numbering may have changed. The claim is cited to the paper as a whole.

**Requires sign-off.** None of these changes affects the mathematics. The lead may wish to confirm the two items in "Not changed": dropping reflexivity (R1 option A) and citing the companion without a proposition number.

## Lead edits after AX70A verification
- Applied AX70A fixes F1–F4 (coverage-definition sentence; companion citation and 'dominance requirements'; 'it says nothing'; scope of (M3)).
