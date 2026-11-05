# Round 80 brief: rewrite LDG §8 "Applications" (writer WAP80)

Folder (write ONLY here): /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r79/

**Base file.** ldg_full.tex is the current full LDG, identical to the author's device version. Output ldg_full_r80.tex and its PDF, plus WAP80_changes.md.

**Author's instruction (binding).** "Rewrite the applications section to include very brief discussions of all of these comparisons. The point of this section is to use the results of LDG to unify the results in the literature, to the greatest extent possible. The discussion of each result, however, should be concise and to the point."

## Sources

Use only **refereed** findings:
- ROUND79_report.md, the summary;
- REF79a_report.md and REF79b_report.md, the referees. Their corrections override the checker reports;
- the checker reports J79, PS79, P79, N79 and NC79 for detail and draft texts.

The papers' texts are in papers/*.txt. For Predd, use papers/predd_ieee.txt, the IEEE version.

## Organisation of the new §8

One opening sentence: each application states the setting, identifies M, C and the rankings, says which of (E), (A), (S), (T) hold and by which route, and what thm:argument (and §5, for strict or uniform dominance) then yields; where a condition fails, it says so and why.

Then one short subsection per group. Aim for 3–8 sentences each, plus a statement or proposition only where a result is ours. Prefer one compact proposition per subsection, with a short proof.

### 1. Proper scores on finite domains
Cover Pettigrew (2022, non-additive), Predd et al. (2009) and SSK (2009). Keep and tighten prop:proper and the event-forecast paragraph.
- **Strictly proper, lower semicontinuous, values in [0,∞].** All four conditions hold (route: thm:bayes-finite with c_p = p). State the reading "continuous as a map into [0,∞]" in prop:proper and prop:strict(b) wherever infinite losses matter, e.g. the log score.
- **Recovers:** Pettigrew's Theorem 1, Predd Theorem 1, SSK Theorem 2/Conclusion 3, with uniform dominance via prop:strict.
- **Gap in Pettigrew.** His proof of Theorem 1 fails with infinite losses (enhanced log score, c = (0,0,½,1)). The theorem is still true, by prop:strict(b). One sentence.
- **Merely proper scores.** (T) fails: give the flat-score example, (0.4,0.4) tied with (0.4,0.6). prop:profiles still identifies the undominated forecasts as those with a coherent profile, i.e. SSK's Lemma 5 situation.
- **Scores infinite somewhere in (0,1).** (A) fails (example from PS79/REF79b). Predd §7.2.1's assertion that "Proposition 2 also holds" in this generalised case is false; SSK's Assumption 3 is needed. One sentence.
- **SSK's discontinuous Examples 4–6.** One sentence each at most, or a combined sentence. Use the referees' corrected verdicts: Example 4 has an incoherent undominated forecast, (½, 3/10). Keep the Figure that illustrates SSK if one exists.

### 2. Probabilism on arbitrary domains (Nielsen 2023)
Keep thm:nielsen. Apply N79's corrections as refereed:
- the "remains open" sentence is wrong under thm:nielsen's hypotheses. Use the lifted SSK Example 2 (ex:ssk-sharp) as the counterexample, and say the question stays open only for infinite Ω under continuity;
- qualify "removes a boundedness assumption": Nielsen's Theorem 2 already dropped it, and his question is about strict dominance;
- (S) holds via thm:bayes-infinite. Say it in one line.

### 3. Conditional reports
Keep def:conditional-systems, lem:section, def:block-reports, def:block-propriety and prop:blocks. Then add:
- **cor:updating for Nielsen (2021)**, as drafted in NC79 §5, with REF79a's three wording fixes. Proposition 8.9 (prop:blocks) is the general result, and Nielsen (2021) with bounded scores is a special case.
- **Briggs–Pettigrew's claim (III)** is (A) for the class of probabilistic conditionalizing strategies, and fails: Nielsen's counterexample. One sentence.
- **The log-score case** lies outside prop:blocks, which needs finite block losses. Handled directly by thm:bayes-finite: the undominated strategies are exactly C_W, and (T) fails for the coherent class of cor:updating. One or two sentences.
- **SSK's conditional forecasts.** Under SSK's coherence₁, (A) fails already for Brier: (0.6, 0.4) dominates the coherent (0.9, 0.7). This is because coherence₁ is matched to strict dominance. prop:blocks is the replacement for a single finite partition. Keep the existing SSK conjecture/SSK14 sentence if still accurate.

### 4. The countable example
Keep prop:countable, tightened.

### 5. Joyce (2009)
Keep prop:joyce. Rewrite the surrounding text using J79 §5 texts as corrected by REF79a.
- State Joyce's hypotheses exactly, including the permutation-invariance footnote.
- Theorem 2 is false under them; give the two gaps.
  - **The Lemma 1\* gap (sums > 1)** corresponds to the failure of (S): competitiveness fails at (½,½,0).
  - **The tie gap in Lemmas 2/2\*** corresponds to the failure of (T). Two-cell example: L₁ = (1−x₁+x₂)², L₂ = (1+x₁−x₂)², under which every credence is tied with a coherent one.
- **The additive, strictly convex counterexample**, with REF79a's general-N version s(b,1) = 3(1−b)² + 2(N−1)(1−b), s(b,0) = 3b² + 2b. Note that it HAS ties, but none with coherent credences. This partly answers the Scope open question: update Scope accordingly.
- **Repairs.**
  - Strict propriety plus lsc gives all four conditions (it reduces to prop:proper).
  - *Face coherent admissibility* gives (S) via cor:closed-choice with c_p = p: for every coherent p, no credence is strictly better than p at every world p charges. With continuity, this works because for loss rankings competitiveness on supp p is exactly face coherent admissibility, closedness follows from continuity, and CA makes the assigned models undominated. Adding "no credence tied with a coherent credence" gives (T).
  - Prove the repair in a few lines as a proposition or as part of the Joyce proposition. Do NOT include the unproved claim about additive rules with Lindley's endpoint conditions.

## Global edits
- Update the intro paragraph that previews §8 (around "Applications include…") and the §1 sentence listing the literature, so they match. Keep them short.
- Update the Scope section's open questions (Joyce) and any sentence about Nielsen's open question.
- Add bibliography items: Briggs & Pettigrew 2020 (Noûs 54(1) 162–181) and Nielsen 2021 (Philos. Stud. 178 (2021) 3217–3236). Keep \cite keys consistent.
- Do not change §§2–7 except for the prop:strict(b) "continuous into [0,∞]" reading and cross-reference fixes.

## Style
- Concise. Plain English. Named definitions only. \coloneqq.
- No jargon ("certificate", "record", "safe", "route" in the sense of a proof route, or "dangerous"). Write "by Theorem X" rather than "route".
- No version-comparison commentary.
- Every claimed result has a proof or a verified counterexample in the text, kept short.
- Labels of existing results stay.

Compile with pdflatex until references settle: no errors, no undefined references, no overfull boxes.

Final message: under 250 words, with the page count of §8 and of the whole paper.
