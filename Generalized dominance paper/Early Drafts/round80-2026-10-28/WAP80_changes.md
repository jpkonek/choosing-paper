# WAP80: changes to LDG (ldg_full.tex -> ldg_full_r80.tex)

Output: ldg_full_r80.tex and ldg_full_r80.pdf (35 pp.; was 31). Section 8 runs pp. 24–33, about 8.5 pp. (was about 5). It compiles cleanly with pdflatex: no errors, no undefined references, no overfull or underfull boxes, no warnings.

Verification scripts (exact arithmetic where possible), both passing:
- wap80/check_proper.py: flat score; score infinite inside (0,1); SSK Examples 4–6; SSK conditional (0.9,0.7) vs (0.6,0.4); Pettigrew enhanced-log gap.
- wap80/check_other.py: lifted SSK Example 2; Nielsen 2021 Brier and log-score examples; Joyce tie example; additive example for N = 3, 4, 5, 7 (Bayes models, ties, margin 1/6 for N = 3); permutation invariance of prop:joyce.

## Section 8 (rewritten)

- **Opening.** One sentence.
- **8.1.**
  - prop:proper now reads "continuous as a map into [0,∞]".
  - New one-line (A)/(S)/(T) statement after the proof.
  - **Pettigrew paragraph.** Recovers Theorem 1 and gives the gap in his proof for infinite losses (enhanced log score, c = (0,0,½,1); the projection is δ₂).
  - **Event forecasts**, split into four paragraphs:
    - strictly proper, continuous into [0,∞]: all four conditions; (S) on Ω via thm:bayes-infinite; Predd Theorem 1 and §VII.A;
    - proper, finite on (0,1): flat-score (T) failure, (0.4,0.4) ~ (0.4,0.6); prop:profiles; SSK Theorem 2, Conclusion 3;
    - infinite inside (0,1): (A) fails (0 dominates 0.3). Predd §VII.B.1's "Proposition 2 also holds" is false, by SSK Lemma 3. This was checked against the IEEE PDF (Prop. 2 asserts φ bounded);
    - SSK Examples 4–6 with the referees' verdicts. Example 4: (½, 3/10) undominated, with a footnote proof. Example 2 = ex:ssk-sharp.
  - Figure fig:profiles(b) is kept and cited.
- **8.2.** thm:nielsen and its proof are unchanged. The paragraph after it is rewritten:
  - (A)/(S)/(T), with (S) by thm:bayes-infinite;
  - Nielsen's admissible measures lie in the class;
  - his Theorem 2 already drops local boundedness (note 27), and his question concerns strict dominance;
  - lifted ex:ssk-sharp: strict dominance fails under thm:nielsen's hypotheses;
  - under continuity with finite Ω, prop:strict(b) gives uniform dominance, so the question is open only for infinite Ω.
- **8.3.**
  - One-line (A)/(S)/(T) statement after prop:blocks.
  - New paragraph "Plans for updating" and **cor:updating** (NC79 draft), with REF79a's three wording fixes:
    - "every J satisfying the hypotheses of Corollary";
    - "if J is continuous …";
    - B&P's (III) stated as their claim, not as "counts as coherent".
  - B&P's (III) is (A) and fails.
  - Necessity of the smaller-support Bayes prior: the proof is given in two sentences.
  - **Log score.** Undominated = C_W, proved in a footnote via thm:bayes-finite; (T) fails; Nielsen's Theorem 4(a) fails under 0·∞ = 0.
  - **SSK conditional forecasts.** (A) fails under coherence₁ for Brier; (0.6,0.4) dominates (0.9,0.7). The SSK conjecture and SSK14 sentences are kept.
- **8.4.** prop:countable is unchanged, plus one sentence giving (E), (A), (S), (T).
- **8.5.**
  - Joyce's hypotheses are stated exactly (finite, continuous, truth-directed, permutation invariance p. 271 n. 9, CA p. 280; "dominated" = our strict, p. 267).
  - **Tie gap** (Lemmas 2/2*), with the two-cell example: (T) fails and (S) holds.
  - prop:joyce now states finiteness and permutation invariance, with a symmetry line in the proof; the paragraph after it ties the Lemma 1* gap to competitiveness at (½,½,0).
  - New **ex:joyce-additive** (general N, REF79a version): it has ties, none with coherent credences.
  - Definition of face coherent admissibility (automatic for N = 2).
  - New **prop:joyce-repair**: (a) strict propriety reduces to prop:proper; (b) CA + face CA + lsc give (S) via cor:closed-choice with c_p = p, and with no ties to coherent credences also (T).

## Outside Section 8

- §1: the literature sentence adds conditionalization [BP20, Nielsen21]. The applications paragraph is rewritten to match §8.
- prop:strict(b): "continuous as a map into [0,∞]".
- §6.1, after def:argument-assumptions: a cross-reference sentence now says "most applications … verify it in this form; that section also notes where it fails". The old wording claimed that all §8 rankings satisfy (S).
- rem:closed-comparisons: the cross-reference now notes that prop:joyce-repair(b) goes through cor:closed-choice, not thm:bayes-infinite.
- Scope:
  - the "Bayes choices in every application" sentence now names the one exception;
  - the open questions are updated (Nielsen: infinite Ω under continuity only; Joyce: partly answered by ex:joyce-additive and prop:joyce-repair).
- Bibliography: added BP20 (Noûs 54 (2020) 162–181) and Nielsen21 (Philos. Stud. 178 (2021) 3217–3236). The key Nielsen still means the 2023 Mind paper.
- The abstract is unchanged.

## Report claims not included

- **N79's claim that Nielsen's proof already yields uniform dominance.** Not refereed (REF79b did not check it).
- **J79: Joyce's argument is sound up to ties for credences summing to less than one.** Correct (REF79a), but omitted for brevity.
- **J79 §3.5 item 2 (additive rules with Lindley's endpoint conditions or 0/1-symmetry).** Excluded on the brief's instruction.
- **PS79:**
  - full-conditional-probability results for SSK conditional forecasts, including the log-score failure: not refereed (layer induction unchecked);
  - the possible gap in SSK Lemma 12: unchecked;
  - the claim that the lsc route covers exactly scores with endpoint jumps: unrefereed.
- **REF79b: cor:closed-choice fails for every assignment for the infinite-inside score, while thm:finite applies.** Correct, but omitted for brevity.
- **REF79a/NC79: B&P's claim (I) and the proof gap in Nielsen's Theorem 4(b) under the log score.** Only Theorem 4(a) is mentioned.
- **P79:**
  - Pettigrew's Lemma 4(ii) and LSE remarks: harmless or unchecked;
  - Theorem 2 (chance dominance): not cited by LDG.
- **J79 footnote-to-def:dominance edit about Joyce's terminology.** Not made, since §2 is frozen; §8.5 states the terminology instead.
