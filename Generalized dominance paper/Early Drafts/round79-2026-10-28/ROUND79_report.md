# Round 79: do the cited papers' rankings satisfy LDG's conditions? (28 Oct 2026)

**Conditions checked.** These are the hypotheses of LDG's dominance argument (thm:argument, §6.1):
- **(E)** evaluability;
- **(A)** coherent admissibility;
- **(S)** selection: undominated coherent assigned models, satisfying thm:finite, cor:closed-choice or thm:local, or the loss routes thm:bayes-finite and thm:bayes-infinite;
- **(T)** closure under ties.

**Method.** One checker per paper wrote J79, PS79, P79, N79 and NC79. Two independent referees (REF79a, REF79b) then checked every FAILS verdict and every claimed error in a published proof. Verdicts below are as corrected by the referees.

## Verdicts

| Paper / class | (E) | (A) | (S) | (T) |
|---|---|---|---|---|
| Pettigrew 2022, whole class (continuous strictly proper, possibly non-additive, values in [0,∞]) | holds | holds | holds (thm:bayes-finite, c_p = p) | holds |
| Nielsen 2023, whole class; also LDG thm:nielsen's larger class | holds | holds | holds (thm:bayes-infinite) | holds |
| Predd et al. 2009 / SSK 2009: strictly proper, continuous, unconditional (infinite values allowed) | holds | holds | holds | holds |
| … merely proper, continuous, finite on (0,1) | holds | holds | holds | **FAILS** |
| … merely proper, infinite somewhere in (0,1) | holds | **FAILS** | thm:finite only | — |
| SSK Example 4 (discontinuous) | holds | holds | **FAILS** | holds |
| SSK Example 5 | holds | holds | **FAILS** | **FAILS** |
| SSK Example 6 | holds | **FAILS** | | |
| SSK conditional forecasts (SSK's coherence), even under Brier | holds | **FAILS** | unclear | holds (strictly proper) |
| Joyce 2009, his full class (finite, continuous, truth-directed, his CA) | holds | holds | **FAILS** for every N ≥ 3 | **FAILS** |
| Nielsen 2021 (conditionalization), his Blackwell class, bounded scores | holds | holds | holds (smaller-support assignment) | holds |
| … Briggs–Pettigrew's class, at least two cells | holds | **FAILS** | | |
| … his class with an infinite-valued score (log, 0·∞ = 0) | holds | holds | | **FAILS** |

Wherever a condition fails, the counterexample checked by the referees also falsifies the dominance argument's conclusion for that ranking. The exception is (T) failing for merely proper scores: there LDG's transitivity route (prop:profiles) still identifies the undominated forecasts as those with a coherent loss profile.

## Key counterexamples (refereed)

- **Merely proper, (T) fails.** Take a continuous proper score that is flat on [⅓, ⅔]. Then the incoherent forecast (0.4, 0.4) is tied at every world with the coherent (0.4, 0.6), so it is undominated.
- **SSK Example 4.** (½, 3/10) is incoherent and undominated. PS79's claim that every incoherent forecast is dominated there is WRONG.
- **SSK conditional forecasts.** Under Brier, (0.6, 0.4) dominates the coherent (0.9, 0.7).
- **Joyce, (T) fails.** Two cells, losses L₁ = (1−x₁+x₂)² and L₂ = (1+x₁−x₂)². Every credence is tied with a coherent one.
- **Joyce, (S) fails.** For any N ≥ 3, take an additive, extensional, strictly convex score with s(b,1) = 3(1−b)² + 2(N−1)(1−b) and s(b,0) = 3b² + 2b. With N = 3, the credence (⅔, ⅔, 0) has no coherent weak dominator.
- **Nielsen 2021, (T) fails.** Under the log score with 0·∞ = 0, his counterexample strategy ties with its Blackwell repair at (∞, 5.545, 5.545).

## Errors found in published proofs (refereed)

- **Joyce 2009, a second gap.** In Lemmas 2 and 2*, the case where all differences are zero is a tie, and his CA does not exclude it. This is in addition to the gap LDG already reports.
- **Pettigrew 2022, Theorem 1.** The proof fails when losses can be infinite: take the enhanced log score and c = (0, 0, ½, 1). The theorem is still true, and LDG's prop:strict(b) proves it, uniformly.
- **Nielsen 2021, under the log score with 0·∞ = 0.** Nielsen allows values in [0,∞] and never fixes this convention. The following then fail:
  - Lemma 2, Theorem 3(a)(3) and Theorem 4(a) are false;
  - Briggs–Pettigrew's claim (I) is false;
  - the proof of Theorem 4(b) has a gap, though the statement is true.
- **Predd et al. 2009, §7.2.** It asserts that φ stays bounded for scores with infinite values. This is false; the paper tacitly needs SSK's Assumption 3. The source is a WebFetch summary of arXiv v1, so check the PDF before citing.

## LDG §8: needed changes (replacement texts are in the reports)

- **prop:proper and prop:strict(b):** "continuous" should read "continuous as a map into [0,∞]".
- **Event forecasts:**
  - state the 0·∞ = 0 convention;
  - (S) holds on Ω itself;
  - add an explicit example where (T) fails, and its effect on thm:argument;
  - explain why the finiteness condition is needed.
- **Conditional reports:** (A) fails under SSK's coherence.
- **thm:nielsen:**
  - the sentence "Whether strict dominance holds without local boundedness remains open" is wrong under its own hypotheses. The lifted SSK Example 2 is a counterexample. Under Nielsen's continuity, the question is open only for infinite Ω;
  - qualify "removes a boundedness assumption": Nielsen's Theorem 2 already drops it, and his question concerns strict dominance.
- **prop:joyce:**
  - state the permutation-invariance footnote;
  - name the second gap;
  - the new additive counterexample partly answers the open question in Scope;
  - Joyce's losses do have ties.
- **New, optional:** a corollary on Nielsen 2021 (cor:updating, drafted in NC79), with the three qualifier fixes in REF79a.

## Not verified

- The published IEEE version of Predd et al.
- The theorem numbering in the published *Decision Analysis* version of SSK. The local file matches Technical Report 865, which LDG cites.
