# Changes, round 16 (15 Oct 2026)

Backup of the round-14/15 file: `The Contamination Triangle pre-round16.tex` (2738 lines, a copy). The new file has
2931 lines. It compiles cleanly with `pdflatex` run twice: 146 pages (previously 131). There are no errors, no
undefined or multiply defined references and no overfull boxes; the only warnings are 7 underfull boxes. Line numbers
refer to the **new** file.

Inputs: D2_notes.md, D2_referee.md, D2_referee2.md, D1_notes.md, D1_referee.md, E1_notes.md.

## Conventions

- No theorem names inside theorem environments. Note numbers (D2.1, D1.7, E1.5, ...) appear only in status lines.
- `\coloneqq` throughout; `grep ':='` finds nothing.
- The terminology check (`grep -niE 'menu|forced[- ]silen|accept-or-silence|available action|forced acceptance|forced advice'`)
  finds only line 262, the existing "Earlier terminology" paragraph, which is allowed.
- Statuses are as the referees assign:
  - D2 items: "proved; confirmed by two independent referees";
  - D1 items: "proved; confirmed by one referee", with Cor D1.7 "at the status of Claim B2.0, reduced import list";
  - E1 items: "proved in a note, not yet refereed".
- No referee marked an earlier result of the write-up wrong, so no dated correction notes were needed and nothing was
  deleted. Superseded statements about the state of knowledge (for example "no world failing to add up is known")
  were revised in place and carry a "Round 16" marker.
- No new mathematics. Two places where my wording is more careful than a note:
  - **Prop D2sigma.** It is stated for the design built in Lemma D2.2. Referee 2's proof uses that design: each block
    contributes a fixed amount to ∫_{Q_γ} ρ. The status says that any nondecreasing ρ with ∫_{Q_γ} ρ = ∞ for every γ
    works, which is how referee 2 states it.
  - **"What a cover still needs".** E1 §3 says that for every admissible shadow there must be unendorsed dominator
    comparisons that are eventually zero at every end. What the cited results give is narrower:
    - for every admissible shadow, unendorsed dominator comparisons (E1.1);
    - for the end-heavy shadows of E1.4, which exist alongside every admissible one, these comparisons are never
      end-positive;
    - at an end-protected world they are eventually zero.

    The write-up states it in this form.

## Notation (renamed to avoid clashes; content unchanged)

| In the notes | In the write-up | Reason |
|---|---|---|
| D2's λ = μ/μ(M) | μ̄ | the write-up's existing symbol for the same measure |
| D2's generators g = (P_g, Q_g), g_* | γ = (P_γ, Q_γ), γ_* | g denotes gambles |
| D2's design conditions (D1)–(D4) | (d1)–(d4) | "D1" is a note name |
| D2's scale blocks B_m | J_m | B_t denotes Bayes models |
| D2's 𝒦₀, R⁻, R⁺, R⁰ | 𝒦₀, (R⁻), (R⁺), (R⁰) | — |
| D1's "(R2)" | "full-atom residual" | as in round 14/15 |
| D1's "Prop B2.0" | "Claim B2.0" | as in round 14/15 |
| D1's Lemma M | Lemma PL2 (R10b Lemma M) | the write-up's existing name |
| D1's N28 Lemma 3.4 | step (iii) of Thm TSalways | the write-up's existing name |
| D2_referee2's "N17.B′_σ" | Conjecture conj:sigmaB | no names in environments |

## 1. Front matter, introduction and status table

| Line | Change |
|---|---|
| 42 | Date: "(rounds 14--16)". |
| 69 | Item 6: "No world failing to add up has been found in a full system, for any target" → "Until round 16 no world failing to add up was known in a full system, for any target; round 16 constructs one in two worlds". |
| 69 | Item 6: appended a paragraph "New in round 16", with referee status. It covers D2.1, the σ-finite scoping (Prop D2sigma, Conj sigmaB), E1.1/E1.5, and D1. |
| 73 | **Summary for T1 rewritten.** See the list after this table. |
| 200–209 | New block "Round 16" in the status table, with 9 rows: D2.1 and Lemmas D2.2–D2.4; the refutations; Prop D2sigma; Conj sigmaB; Thm D1; Prop D10; Cor D17; Thms E11/E12; Lemmas E13/E14, Thm E15, Prop E16. |
| 210 | N17.B′ row: now "false in two worlds (Thm D21), so (R2) answered negatively". It also records the σ-finite form (Conj sigmaB), that no three-world counterexample is known, and the remaining items for T1. (R2) is removed from that list and "unendorsed dominator comparisons that are not end-positive" is added. |

The rewritten Summary for T1 (line 73):

- **Excluded.** Unchanged.
- **D2.** Worlds that do not add up now exist in full systems (D2.1, two referees). It refutes N17.B′ (two worlds) and
  Q1.C1, and answers (R2) negatively.
- **Scoping.** The failure is exactly non-integrability at the protected end (Prop D2sigma). The σ-finite form
  (Conj sigmaB) is open.
- **None in three worlds.** No world that does not add up is known in three worlds or in a cover.
- **Properties (i)–(iv).** Unchanged.
- **New (v).** A world of a cover that does not add up is not of the D2 type when the other worlds add up with
  integrable densities (E1.5, E1.6). This rests on "protection and visibility exclude each other" (E1.1–E1.4) and is
  not yet refereed.
- **What a cover still needs.** As in the second bullet under Conventions.
- **Remaining problems.**
  - (R2) removed as answered.
  - Added: Conj sigmaB, and unprotected certificates in three worlds.
  - Case (i) of R3 kept, noting that after E1.2 it is no longer needed for unendorsed comparisons near T1.
- **Off the U-domain.**
  - D1 under (LF): the target weighting is never exceptional, so the full-atom residual is empty, independently of
    Claim B2.0.
  - Cor D17 at the status of Claim B2.0.
  - What remains is p\* ∉ E: E = ∅ at the status of Thm ccibu; E ≠ ∅ conditional.

## 2. Edits to existing text outside the new blocks

| Line | Section | Change |
|---|---|---|
| 354 | §2.6, after Def addup | New paragraph. Weights are real-valued, hence bounded, which is the N19 convention; Yosida–Hewitt presupposes it. Round 16: the convention matters (D2.1, Prop D2sigma, the extended-valued weight in the D2.1 status). |
| 1578 | §8.1 "The remaining target" | Two dated sentences. N17.B′ is false in two worlds, so a proof for covers of T1 must use an input that D2's system lacks. Round 16 shows that a non-adding-up world can occur and that its mechanism is invisible to M0closed and cannot carry a cover. |
| 1624 | §8.3, item "Rankings that do not add up" | "No system is known, for any target, in which (M1) or (M2) occurs ... with (S)" → "Until round 16 no system was known ...; Round 16 gives one ... (M2) ... (Thm D21). No such system is known in three worlds." Status: "N17.B′ is false in two worlds (Thm D21, round 16); before that it was narrowed ...". |
| 1756 | §8.4(c) "The precise open class in two worlds" | Dated note: the class is inhabited (D21). World 1 has the required properties, as Thms fullsupport, E2, E3 (CHECKED) require. So N17.B′ and N17.B′(2) fail; the σ-finite form is Conj sigmaB. |
| 1758 | §8.4(c) "Three worlds" status | "N17.B′ in three worlds is open (in two worlds it is false, Thm D21)". |
| 1761 | §8.5 lead-in | "Neither was achieved" → "Neither was achieved in round 12", followed by "Round 16 constructs one in two worlds (Thm D21, part (e))". New sentence on round 16 (notes, referee reports, where each block is; E1 not refereed). |
| 1801 | Thm R3 status | Dated sentence: E12 gives case (ii)'s conclusion without the split, with admissible shadows (not refereed). |
| 2022 | §8.5(c) "Ratio certificates" | Dated sentence: such certificates occur in a full system next to an additive world (D21, step 7). |
| 2050 | Cor SR status | Dated sentence: (R2) answered negatively in that setting; Q1.C1 is false. |
| 2119 | Prop LIN status | Dated sentence: (R2) answered negatively. In D2 the generator sources have η₁(P,1) at most of order μ̄(P)², a superlinear rate (both D2 referees). |
| 2245 | §8.5(e) heading | "... every axiom except one closed section, and (round 16) a full system." |
| 2261 | §8.5(e), tilt paragraph | "No construction is claimed" → "No construction is claimed here", plus a dated note that D21 is such a construction, with the weight a σ-finite measure. |
| 2380 | §8.5(f) heading | "Rounds 14 to 16: ..., general domains, and what Theorem M0closed needs." |
| 2380 | §8.5(f) lead-in | "No world that fails to add up was found in a full system, for any target" → "Rounds 14 and 15 found no world ...; round 16 found one in two worlds (Thm D21, end of part (e))". Pointer to the two round-16 blocks at the end of (f). |
| 2679 | Prop B2ex status | Dated sentence: the restated full-atom conjecture holds under (LF) alone, without (β), (δ) and without Claim B2.0 (Thm D1). |
| 2702 | §8.5(f) "The branch p\* ∉ E" | Round-16 paragraph. See the list after this table. |
| 2704 | §8.5(f) "Consequence for (M0) on general domains" | Dated sentence. Under (LF) the p\* ∈ E alternative is empty (D1; Cor D17 at the status of Claim B2.0, reduced imports). What remains is p\* ∉ E, with E = ∅ at the status of Thm ccibu and E ≠ ∅ conditional. |
| 2918–2923 | Sources | Added D1_notes, D1_referee, D2_notes, D2_referee, D2_referee2, E1_notes. |

The round-16 paragraph on the branch p\* ∉ E (line 2702) states:

- D1 empties the branch p\* ∈ E.
- The case E = ∅ also needs an argument (the D1 referee's caveat): Thm ccibu, or an audit that uses Prop
  necessary(b),(c). It holds at that status.
- The case E ≠ ∅ is described.
- D1.6 shows that the wall step crosses chords. TSalways also needs N28 Prop 3.1 and Lemma 3.2, which is the referee's
  narrowing.
- D1's proposed next step is labelled CONJECTURE.

## 3. New block in §8.5(e): D2 (lines 2302–2378)

| Line | Item | Status |
|---|---|---|
| 2302 | Setting: C21's path reparametrised as in (e); coordinate x; tails τ_f and D(f); designs (d1)–(d4); the cone 𝒦₀; rules (R⁻), (R⁺), (R⁰); the two world orders; "in words". | — |
| 2323 | **Lemma D22** (= D2.2, designs exist), with the projective-plane construction in the proof sketch. | Proved; confirmed by both referees; NUMERICS (both design_check scripts). |
| 2331 | **Lemma D23** (= D2.3, preorder, strict (G), (IB)). | Proved; confirmed by both referees. Status notes the equivalence of transitivity with sum closure (referee 2 §1) and the referees' stress tests. |
| 2341 | **Lemma D24** (= D2.4, closed sections for every model). | Proved; confirmed by both. Bounds are stated before closedness (referee 1's repair). Status: (d3) does the work; the contrast with Prop S32 (referee 1 §3). |
| 2353 | **Theorem D21** (= D2.1), with "bounded (equivalently, real-valued)" and type (M2) in the statement. The proof sketch has steps 1–8. | **Proved; confirmed by two independent referees.** See the status contents after this table. |
| 2361 | Consequences paragraph. | Proved, from D21. See the list after this table. |
| 2363–2373 | **Scoping paragraph and Proposition D2sigma** (referee 2 §3.1): the σ-finite measure ρμ̄ with ρ = 1/(1−x) endorses every comparison between regular models; its Bayes sets are path members. The status contains the "Reading" that the failure is *exactly* non-integrability at the protected end, that the refutations are unaffected (bounded charges), and the second (M2) proof. | Proved in a referee report (D2_referee2), one reader; NUMERICS. |
| 2375 | **Conjecture sigmaB** (= referee 2's N17.B′_σ): every world of a full system on M_U has a countably additive endorsing measure with a.e. positive, locally integrable density. The status covers: why D2 does not refute it; referee 2's remark on Prop M0 for T1; D2.C would refute only the bounded form; a pointer to E11. | CONJECTURE. |

The status of Theorem D21 (line 2353) records:

- **Step 4.** The case b = 1 is treated separately (both referees).
- **Boundedness.** Referee 1's extended-valued weight shows why boundedness matters. The corpus convention is bounded
  charges.
- **Step 8.** The direct proofs of (M2) by both referees replace D2's appeal to N17.3.
- **Step 5.** Referee 2's direct proof avoids Thm kkm.
- **Prop S32(d).** Why it does not apply (referee 2 §2.7).
- **Consistency.** SR₁, QC₁, Lemma T₁, Prop Q15, and a\* = a (Cor IS).
- **Not claimed.** The remarks "why R⁺", "why the protected end" and "what made it work" are heuristic (both
  referees) and are not claimed.
- **NUMERICS.** The status includes the caveats: T4 ran once, and the proxy artefact at cuts inside the last block.

The consequences paragraph (line 2361) records:

- N17.B′ is false, including N17.B′(2) (P4 §5.5, P4B §8.5);
- Q1.C1 is false;
- (R2) has a negative answer;
- the failure is of type (M2).

Its scope remark says:

- The result is n = 2 and not a cover.
- The exclusion route "N17.B′ then M0closed" fails as stated.
- D2 §5's "positive route open again" is a reading (referee 1 §6).
- Conjecture D2.C is stated in words, as not attempted.
- There is a pointer to E15/E16.

**Not adopted.** The two referees comment differently on Prop S33(c):

- referee 1 §5: "right-packing fails, because of the near-one clause";
- referee 2 §2.7: "the base cone right-packs".

The write-up records neither. Neither remark is used by any result.

## 4. New blocks in §8.5(f)

### D1 (lines 2680–2701), after Prop B2ex

| Line | Item | Status |
|---|---|---|
| 2680 | Setting: (LF) at D_T1; ψ strictly guiding, integral penalties, integrable envelope, (γ); E(ψ). | — |
| 2682 | **Theorem D1** (no non-null ties at p\*; the full-atom residual is empty under (LF)). The proof sketch has steps (1)–(7), with all referee repairs built in: genericity excludes fan and charged-pencil points; c′-ties are included; x ∈ N; the cone over α₀; non-collinearity via convergence of K⁺(t) to a face model ⊇ T1 (D1.2, third item); "a.e. shell gamble"; a.e.-then-continuity; the open-chart argument replaces R4 Thm B in Step 1 of Lemma M. | Proved; confirmed with repairs (D1_referee), one reader. Status: GA/GB proved, not NUMERICS; uses / not used; B2.R (restated) proved under (LF) alone; an independent route on M_U. |
| 2690 | **Proposition D10** (= Example D1.0 with the K^i structure; three-atom field without (LF), with T1 interior to the face). | Proved; confirmed (D1_referee §7); NUMERICS. |
| 2695 | **Remark (heuristic), unlabelled**: the gluing inequality x_k + 1/x_{k+1} > κ+1, labelled as not derived and not used. | As the referee requires. |
| 2697 | **Corollary D17** (= D1.7), with the reduced import list ((α\*), (γ), ρ_i > 0 a.e. on non-singleton advice ranges) in the hypotheses. | At the status of Claim B2.0 (D1_referee §8). (β), (δ) and the regular-splice step are not needed. |

### E1 (lines 2705–2778), at the end of (f)

Every item is labelled "proved in a note, not yet refereed".

| Line | Item |
|---|---|
| 2705 | Setting: shadows' fields c^ν, B^ν_t, Z^ν_t; *admissible* shadow; *dominator comparison*. |
| 2707 | **Theorem E11** (= E1.1 (a)–(c)). The status covers which comparisons are used; that T1's out-comparisons are not used; the relation to M0closed(b) ((c) is a different sufficient condition); the index non-locality; which worlds. |
| 2720 | **Theorem E12** (= E1.2, Theorem R3 without the case split). The status says it is the conclusion of R3(ii) with admissible shadows, that the dominator may be T1, and that leaving T1's out-comparisons unendorsed breaks nothing. NUMERICS. |
| 2728 | Definitions: end, S-positive, eventually ≥ 0 / = 0, end-protected. D2's world 1 is end-protected (E1 §2.1). |
| 2730 | **Lemma E13** (= E1.3 (a), (b)). The status covers the same argument at any C_p and where ends can sit (near-unanimous limits). |
| 2742 | **Lemma E14** (= E1.4, sink-heavy reweighting). NUMERICS. |
| 2750 | **Theorem E15** (= E1.5). Status: scope; worlds with no ends; gauge mixtures satisfy (h) (CHECKED by inspection). |
| 2763 | **Proposition E16** (= E1.6, D2's failure is invisible). NUMERICS; comparison with Prop D2sigma. |
| 2776 | Paragraph "The obstruction: protection and visibility exclude each other". It explains base versus protection, supersedes D2 §5's sentence for the D2 type proper, and says D2.C does not bear on T1. |
| 2778 | Paragraph "What a cover still needs" (E1 §3), in the precise form described under Conventions. D2 §0's transport claim is labelled heuristic. Three worlds are open, and no conjecture is stated. |

## 5. §8.5(g) (lines 2780–2823)

| Line | Change |
|---|---|
| 2780 | **"What a cover on M_U still needs" rewritten.** See the list after this table. |
| 2787 | New bullet: not of the D2 type when the other worlds add up with integrable densities (E15, E16), and ends only at near-unanimous limits (E13). Round 16, not refereed. |
| 2789 | **Rewritten paragraph after the bullets.** See the list after this table. |
| 2794 | (R2): appended "Round 16: answered negatively" (D21, Q15), "So Q1.C1 is false", and the σ-finite analogue (D2sigma, Conj sigmaB). The question text is kept. |
| 2795 | (R3): "(round 16: Q1.C1 is false, Theorem D21, where this rate holds)". |
| 2803 | Lifting bullet 2: round-16 sentence. With (R2) negative and N17.B′ false in two nested worlds, this route cannot be completed as stated; the σ-finite analogue is open; E15. |
| 2804 | Lifting bullet 3 (case (i) of R3): round-16 sentence. E12 and E11 make excluding case (i) unnecessary for that purpose. |
| 2806 | "Three worlds: questions from rounds 14 to 16." Item "At T1 itself" annotated. New items "σ-finite endorsement" (Conj sigmaB) and "Unprotected certificates" (E1 §3; D2.C does not bear on T1). |
| 2820 | "Off the U-domain", second bullet, rewritten. See the list after this table. |
| 2823 | Status line. See the list after this table. |

The rewritten opening of "What a cover on M_U still needs" (line 2780) says:

- such worlds are no longer hypothetical (D21, D2sigma);
- none is known in three worlds or in a cover;
- "Every such world i" now reads "Every world of a cover that does not add up". Bullets 1–5 are unchanged.

The rewritten paragraph after the bullets (line 2789) contains:

- R3, plus the visibility requirement (E11, E12, E14), in the precise form;
- that protected failures are invisible to M0closed;
- the conclusion sentence, extended by "whose failure is carried, for every end-heavy admissible shadow, by unendorsed
  dominator comparisons that are not end-positive".

It replaces "No such world is known in a full system, for any target; the only world without a leading density known
in a full system (C21) adds up" with "No such world is known. C21 gives a world without a leading density in a full
system, and it adds up; D21 gives a world that does not add up in a full system, and its failure is invisible in this
sense (E16)". It also notes that (R2) is now answered and that the three-world questions run to round 16.

The rewritten "Off the U-domain" bullet (line 2820) says:

- Claim B2.0 must still be written; Cor B22 is conditional on it;
- under (LF) the full-atom residual is empty independently of Claim B2.0 (D1), which proves the restated conjecture;
- without (LF) the residual occurs (B2ex, D10);
- the ranking form is Cor D17;
- what remains under (LF) is p\* ∉ E: E = ∅ at the status of ccibu or after an audit, and E ≠ ∅ conditional, or open
  if E accumulates at p\*;
- D1's next step is a CONJECTURE.

The status line (line 2823) now reads:

- "(R1) open ...; (R2) answered negatively in round 16";
- the restated full-atom conjecture is removed from the open list;
- a new round-16 sentence lists what is false, what is open (Conj sigmaB, unprotected certificates), what is proved
  (D1) and what is not refereed (E1 items).

## 6. Not changed

- §§1–7, apart from the introduction, the status table and the paragraph after Def addup.
- The statements and statuses of all earlier results. Only dated "Round 16" sentences were appended to the status
  lines of Thm R3, Cor SR, Prop LIN and Prop B2ex.
- §8.2, §8.6 and §9.
- Labels of existing environments.
- Other files. Only `The Contamination Triangle.tex`, its backup `The Contamination Triangle pre-round16.tex`, this
  file and the pdflatex outputs in `writeup/` were written.
